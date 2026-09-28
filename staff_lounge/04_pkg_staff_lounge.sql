--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 04 - PKG_STAFF_LOUNGE
--
-- Transaction control: no procedure in this package COMMITs, except the
-- autonomous error logger. The caller (card-reader REST handler, APEX page,
-- scheduler job, payroll run) owns the transaction, so a payroll run that
-- fails rolls back its lounge deductions together with the salary posting.
--------------------------------------------------------------------------------

CREATE OR REPLACE PACKAGE HRD.PKG_STAFF_LOUNGE
AUTHID DEFINER
AS
    -- Swipe types
    C_CHECK_IN          CONSTANT VARCHAR2(10) := 'CHECK_IN';
    C_CHECK_OUT         CONSTANT VARCHAR2(10) := 'CHECK_OUT';

    -- Charge statuses
    C_STATUS_PENDING    CONSTANT VARCHAR2(20) := 'PENDING';
    C_STATUS_DEDUCTED   CONSTANT VARCHAR2(20) := 'DEDUCTED';
    C_STATUS_REVERSED   CONSTANT VARCHAR2(20) := 'REVERSED';

    -- P_RECORD_SWIPE result codes
    C_RESULT_OK             CONSTANT VARCHAR2(30) := 'OK';
    C_RESULT_INVALID_TYPE   CONSTANT VARCHAR2(30) := 'INVALID_SWIPE_TYPE';
    C_RESULT_UNKNOWN_CARD   CONSTANT VARCHAR2(30) := 'UNKNOWN_CARD';
    C_RESULT_CARD_BLOCKED   CONSTANT VARCHAR2(30) := 'CARD_BLOCKED';
    C_RESULT_DUPLICATE      CONSTANT VARCHAR2(30) := 'DUPLICATE_SWIPE';
    C_RESULT_INVALID_TIME   CONSTANT VARCHAR2(30) := 'INVALID_SWIPE_TIME';
    C_RESULT_NO_RATE        CONSTANT VARCHAR2(30) := 'NO_CHARGE_RATE';
    C_RESULT_SYSTEM_ERROR   CONSTANT VARCHAR2(30) := 'SYSTEM_ERROR';

    -- A second read of the same card and swipe type within this many seconds
    -- is treated as a hardware double-read and not charged again.
    C_DUPLICATE_WINDOW_SEC  CONSTANT NUMBER := 60;

    ----------------------------------------------------------------------------
    -- Returns the charge for a swipe type on a given date (600 by default).
    ----------------------------------------------------------------------------
    FUNCTION F_GET_CHARGE_AMOUNT
    (
        P_SWIPE_TYPE  IN VARCHAR2,
        P_SWIPE_DATE  IN DATE DEFAULT SYSDATE
    ) RETURN NUMBER;

    ----------------------------------------------------------------------------
    -- Called on every card swipe at the lounge entry / exit reader.
    -- Never raises for business errors: the outcome is returned in
    -- P_RESULT_CODE / P_RESULT_MSG and every rejected swipe is written to
    -- HRD_LOUNGE_SWIPE_ERR_LOG.
    --
    -- P_SWIPE_TYPE accepts CHECK_IN / CHECK_OUT (also "Check-in", "check out").
    ----------------------------------------------------------------------------
    PROCEDURE P_RECORD_SWIPE
    (
        P_CARD_NO          IN  VARCHAR2,
        P_SWIPE_TYPE       IN  VARCHAR2,
        P_SWIPE_TIMESTAMP  IN  TIMESTAMP DEFAULT SYSTIMESTAMP,
        P_LOUNGE_CODE      IN  VARCHAR2  DEFAULT 'MAIN',
        P_DEVICE_ID        IN  VARCHAR2  DEFAULT NULL,
        P_LOUNGE_SWIPE_ID  OUT NUMBER,
        P_RESULT_CODE      OUT VARCHAR2,
        P_RESULT_MSG       OUT VARCHAR2
    );

    ----------------------------------------------------------------------------
    -- HR correction: cancels a PENDING charge (e.g. wrong swipe). Deducted
    -- charges cannot be reversed here; refund them through payroll.
    ----------------------------------------------------------------------------
    PROCEDURE P_REVERSE_SWIPE
    (
        P_LOUNGE_SWIPE_ID  IN NUMBER,
        P_REASON           IN VARCHAR2
    );

    ----------------------------------------------------------------------------
    -- Day-end report: (re)builds HRD_LOUNGE_DAY_END_RPT for P_REPORT_DATE with
    -- one row per employee who checked in and/or out that day.
    ----------------------------------------------------------------------------
    PROCEDURE P_GENERATE_DAY_END_REPORT
    (
        P_REPORT_DATE    IN  DATE DEFAULT TRUNC(SYSDATE),
        P_EMPLOYEE_COUNT OUT NUMBER
    );

    ----------------------------------------------------------------------------
    -- Preview: pending lounge charges for an employee up to P_PERIOD_TO
    -- (from P_PERIOD_FROM when P_INCLUDE_ARREARS = 'N').
    ----------------------------------------------------------------------------
    FUNCTION F_GET_PENDING_DEDUCTION
    (
        P_EMPLOYEE_ID       IN NUMBER,
        P_PERIOD_FROM       IN DATE,
        P_PERIOD_TO         IN DATE,
        P_INCLUDE_ARREARS   IN VARCHAR2 DEFAULT 'Y'
    ) RETURN NUMBER;

    ----------------------------------------------------------------------------
    -- Payroll hook. Call once inside the payroll run, before net pay is
    -- calculated. For every employee (or only P_EMPLOYEE_ID when given):
    --   * marks PENDING charges up to the period end as DEDUCTED with P_PAYROLL_ID
    --   * writes the total to HRD_LOUNGE_DEDUCTION_DTL (the amount to deduct)
    -- Arrears (charges before P_PERIOD_FROM never deducted, e.g. an employee
    -- skipped in an earlier run) are included unless P_INCLUDE_ARREARS = 'N'.
    --
    -- Safe to call again for the same payroll: employees already processed
    -- for P_PAYROLL_ID are skipped.
    ----------------------------------------------------------------------------
    PROCEDURE P_PROCESS_PAYROLL_DEDUCTION
    (
        P_PAYROLL_ID        IN  NUMBER,
        P_PERIOD_FROM       IN  DATE,
        P_PERIOD_TO         IN  DATE,
        P_EMPLOYEE_ID       IN  NUMBER   DEFAULT NULL,
        P_INCLUDE_ARREARS   IN  VARCHAR2 DEFAULT 'Y',
        P_EMPLOYEE_COUNT    OUT NUMBER,
        P_TOTAL_AMOUNT      OUT NUMBER
    );

    ----------------------------------------------------------------------------
    -- Amount deducted from an employee's salary for a payroll run
    -- (0 when the employee had no lounge usage).
    ----------------------------------------------------------------------------
    FUNCTION F_GET_PAYROLL_DEDUCTION
    (
        P_PAYROLL_ID   IN NUMBER,
        P_EMPLOYEE_ID  IN NUMBER
    ) RETURN NUMBER;

END PKG_STAFF_LOUNGE;
/

CREATE OR REPLACE PACKAGE BODY HRD.PKG_STAFF_LOUNGE
AS
    EX_INVALID_INPUT       EXCEPTION;
    PRAGMA EXCEPTION_INIT(EX_INVALID_INPUT, -20110);

    ----------------------------------------------------------------------------
    FUNCTION F_CURRENT_USER RETURN VARCHAR2
    AS
    BEGIN
        RETURN COALESCE(SYS_CONTEXT('APEX$SESSION', 'APP_USER'), SYS_CONTEXT('USERENV', 'SESSION_USER'));
    END F_CURRENT_USER;

    ----------------------------------------------------------------------------
    -- 'Check-in', 'check in', 'CHECKIN', 'IN' -> CHECK_IN ; NULL when invalid
    ----------------------------------------------------------------------------
    FUNCTION F_NORMALIZE_SWIPE_TYPE
    (
        P_SWIPE_TYPE IN VARCHAR2
    ) RETURN VARCHAR2
    AS
        V_TYPE VARCHAR2(100) := REGEXP_REPLACE(UPPER(TRIM(P_SWIPE_TYPE)), '[^A-Z]', NULL);
    BEGIN
        RETURN CASE
                   WHEN V_TYPE IN ('CHECKIN', 'IN')   THEN C_CHECK_IN
                   WHEN V_TYPE IN ('CHECKOUT', 'OUT') THEN C_CHECK_OUT
               END;
    END F_NORMALIZE_SWIPE_TYPE;

    ----------------------------------------------------------------------------
    -- Autonomous: the rejection is kept even if the caller rolls back.
    ----------------------------------------------------------------------------
    PROCEDURE P_LOG_SWIPE_ERROR
    (
        P_CARD_NO          IN VARCHAR2,
        P_EMPLOYEE_ID      IN NUMBER,
        P_LOUNGE_CODE      IN VARCHAR2,
        P_DEVICE_ID        IN VARCHAR2,
        P_SWIPE_TYPE       IN VARCHAR2,
        P_SWIPE_TIMESTAMP  IN TIMESTAMP,
        P_ERROR_CODE       IN VARCHAR2,
        P_ERROR_MESSAGE    IN VARCHAR2
    )
    AS
        PRAGMA AUTONOMOUS_TRANSACTION;
    BEGIN
        INSERT INTO HRD.HRD_LOUNGE_SWIPE_ERR_LOG
        (
            CARD_NO, EMPLOYEE_ID, LOUNGE_CODE, DEVICE_ID, SWIPE_TYPE,
            SWIPE_TIMESTAMP, ERROR_CODE, ERROR_MESSAGE, CREATED_BY
        )
        VALUES
        (
            SUBSTR(P_CARD_NO, 1, 50), P_EMPLOYEE_ID, SUBSTR(P_LOUNGE_CODE, 1, 30),
            SUBSTR(P_DEVICE_ID, 1, 50), SUBSTR(P_SWIPE_TYPE, 1, 30),
            P_SWIPE_TIMESTAMP, P_ERROR_CODE, SUBSTR(P_ERROR_MESSAGE, 1, 4000), F_CURRENT_USER
        );
        COMMIT;
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;  -- logging must never break the swipe flow
    END P_LOG_SWIPE_ERROR;

    ----------------------------------------------------------------------------
    FUNCTION F_GET_CHARGE_AMOUNT
    (
        P_SWIPE_TYPE  IN VARCHAR2,
        P_SWIPE_DATE  IN DATE DEFAULT SYSDATE
    ) RETURN NUMBER
    AS
        V_CHARGE_AMOUNT HRD.HRD_LOUNGE_CHARGE_MST.CHARGE_AMOUNT%TYPE;
    BEGIN
        SELECT CHARGE_AMOUNT
        INTO   V_CHARGE_AMOUNT
        FROM   HRD.HRD_LOUNGE_CHARGE_MST
        WHERE  SWIPE_TYPE = F_NORMALIZE_SWIPE_TYPE(P_SWIPE_TYPE)
        AND    TRUNC(P_SWIPE_DATE) >= EFFECTIVE_FROM
        AND    (EFFECTIVE_TO IS NULL OR TRUNC(P_SWIPE_DATE) <= EFFECTIVE_TO)
        ORDER  BY EFFECTIVE_FROM DESC
        FETCH  FIRST 1 ROW ONLY;

        RETURN V_CHARGE_AMOUNT;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RETURN NULL;
    END F_GET_CHARGE_AMOUNT;

    ----------------------------------------------------------------------------
    PROCEDURE P_RECORD_SWIPE
    (
        P_CARD_NO          IN  VARCHAR2,
        P_SWIPE_TYPE       IN  VARCHAR2,
        P_SWIPE_TIMESTAMP  IN  TIMESTAMP DEFAULT SYSTIMESTAMP,
        P_LOUNGE_CODE      IN  VARCHAR2  DEFAULT 'MAIN',
        P_DEVICE_ID        IN  VARCHAR2  DEFAULT NULL,
        P_LOUNGE_SWIPE_ID  OUT NUMBER,
        P_RESULT_CODE      OUT VARCHAR2,
        P_RESULT_MSG       OUT VARCHAR2
    )
    AS
        V_SWIPE_TYPE      VARCHAR2(10);
        V_SWIPE_TS        TIMESTAMP := NVL(P_SWIPE_TIMESTAMP, SYSTIMESTAMP);
        V_CARD_ID         HRD.HRD_LOUNGE_CARD_MST.LOUNGE_CARD_ID%TYPE;
        V_EMPLOYEE_ID     HRD.HRD_LOUNGE_CARD_MST.EMPLOYEE_ID%TYPE;
        V_IS_ACTIVE       HRD.HRD_LOUNGE_CARD_MST.IS_ACTIVE%TYPE;
        V_CHARGE_AMOUNT   NUMBER;
        V_DUPLICATE_COUNT NUMBER;

        PROCEDURE P_REJECT
        (
            P_CODE IN VARCHAR2,
            P_MSG  IN VARCHAR2
        )
        AS
        BEGIN
            P_RESULT_CODE := P_CODE;
            P_RESULT_MSG  := P_MSG;
            P_LOG_SWIPE_ERROR(P_CARD_NO, V_EMPLOYEE_ID, P_LOUNGE_CODE, P_DEVICE_ID,
                              P_SWIPE_TYPE, V_SWIPE_TS, P_CODE, P_MSG);
        END P_REJECT;
    BEGIN
        P_LOUNGE_SWIPE_ID := NULL;

        V_SWIPE_TYPE := F_NORMALIZE_SWIPE_TYPE(P_SWIPE_TYPE);
        IF V_SWIPE_TYPE IS NULL THEN
            P_REJECT(C_RESULT_INVALID_TYPE, 'Swipe type must be CHECK_IN or CHECK_OUT.');
            RETURN;
        END IF;

        -- Reject clock-skewed readers (more than 5 minutes in the future)
        IF V_SWIPE_TS > SYSTIMESTAMP + INTERVAL '5' MINUTE THEN
            P_REJECT(C_RESULT_INVALID_TIME, 'Swipe time is in the future.');
            RETURN;
        END IF;

        -- Lock the card row: serialises concurrent reads of the same card so the
        -- duplicate check below is reliable.
        BEGIN
            SELECT LOUNGE_CARD_ID, EMPLOYEE_ID, IS_ACTIVE
            INTO   V_CARD_ID, V_EMPLOYEE_ID, V_IS_ACTIVE
            FROM   HRD.HRD_LOUNGE_CARD_MST
            WHERE  CARD_NO = TRIM(P_CARD_NO)
            FOR UPDATE;
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                P_REJECT(C_RESULT_UNKNOWN_CARD, 'Card is not registered for lounge access.');
                RETURN;
        END;

        IF V_IS_ACTIVE <> 'Y' THEN
            P_REJECT(C_RESULT_CARD_BLOCKED, 'Card is blocked.');
            RETURN;
        END IF;

        SELECT COUNT(*)
        INTO   V_DUPLICATE_COUNT
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN
        WHERE  EMPLOYEE_ID     = V_EMPLOYEE_ID
        AND    SWIPE_TYPE      = V_SWIPE_TYPE
        AND    STATUS         <> C_STATUS_REVERSED
        AND    SWIPE_TIMESTAMP BETWEEN V_SWIPE_TS - NUMTODSINTERVAL(C_DUPLICATE_WINDOW_SEC, 'SECOND')
                                   AND V_SWIPE_TS + NUMTODSINTERVAL(C_DUPLICATE_WINDOW_SEC, 'SECOND');

        IF V_DUPLICATE_COUNT > 0 THEN
            P_REJECT(C_RESULT_DUPLICATE, 'Same swipe already recorded within '
                                         || C_DUPLICATE_WINDOW_SEC || ' seconds.');
            RETURN;
        END IF;

        V_CHARGE_AMOUNT := F_GET_CHARGE_AMOUNT(V_SWIPE_TYPE, CAST(V_SWIPE_TS AS DATE));
        IF V_CHARGE_AMOUNT IS NULL THEN
            P_REJECT(C_RESULT_NO_RATE, 'No lounge charge configured for ' || V_SWIPE_TYPE
                                       || ' on ' || TO_CHAR(V_SWIPE_TS, 'YYYY-MM-DD') || '.');
            RETURN;
        END IF;

        INSERT INTO HRD.HRD_LOUNGE_SWIPE_TRN
        (
            EMPLOYEE_ID, LOUNGE_CARD_ID, LOUNGE_CODE, DEVICE_ID,
            SWIPE_TYPE, SWIPE_TIMESTAMP, CHARGE_AMOUNT, STATUS
        )
        VALUES
        (
            V_EMPLOYEE_ID, V_CARD_ID, NVL(SUBSTR(P_LOUNGE_CODE, 1, 30), 'MAIN'), SUBSTR(P_DEVICE_ID, 1, 50),
            V_SWIPE_TYPE, V_SWIPE_TS, V_CHARGE_AMOUNT, C_STATUS_PENDING
        )
        RETURNING LOUNGE_SWIPE_ID INTO P_LOUNGE_SWIPE_ID;

        P_RESULT_CODE := C_RESULT_OK;
        P_RESULT_MSG  := V_SWIPE_TYPE || ' recorded. Charge: ' || TO_CHAR(V_CHARGE_AMOUNT, 'FM999G999G990D00');
    EXCEPTION
        WHEN OTHERS THEN
            P_LOUNGE_SWIPE_ID := NULL;
            P_RESULT_CODE     := C_RESULT_SYSTEM_ERROR;
            P_RESULT_MSG      := 'Swipe could not be recorded. Please contact HR.';
            P_LOG_SWIPE_ERROR(P_CARD_NO, V_EMPLOYEE_ID, P_LOUNGE_CODE, P_DEVICE_ID, P_SWIPE_TYPE, V_SWIPE_TS,
                              C_RESULT_SYSTEM_ERROR,
                              SQLERRM || CHR(10) || DBMS_UTILITY.FORMAT_ERROR_BACKTRACE);
    END P_RECORD_SWIPE;

    ----------------------------------------------------------------------------
    PROCEDURE P_REVERSE_SWIPE
    (
        P_LOUNGE_SWIPE_ID  IN NUMBER,
        P_REASON           IN VARCHAR2
    )
    AS
        V_STATUS HRD.HRD_LOUNGE_SWIPE_TRN.STATUS%TYPE;
    BEGIN
        IF TRIM(P_REASON) IS NULL THEN
            RAISE_APPLICATION_ERROR(-20110, 'A reason is required to reverse a lounge charge.');
        END IF;

        SELECT STATUS
        INTO   V_STATUS
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN
        WHERE  LOUNGE_SWIPE_ID = P_LOUNGE_SWIPE_ID
        FOR UPDATE;

        IF V_STATUS <> C_STATUS_PENDING THEN
            RAISE_APPLICATION_ERROR(-20110, 'Only PENDING lounge charges can be reversed (current status: '
                                            || V_STATUS || ').');
        END IF;

        UPDATE HRD.HRD_LOUNGE_SWIPE_TRN
        SET    STATUS          = C_STATUS_REVERSED,
               REVERSAL_REASON = SUBSTR(TRIM(P_REASON), 1, 500)
        WHERE  LOUNGE_SWIPE_ID = P_LOUNGE_SWIPE_ID;
    EXCEPTION
        WHEN NO_DATA_FOUND THEN
            RAISE_APPLICATION_ERROR(-20110, 'Lounge swipe ' || P_LOUNGE_SWIPE_ID || ' not found.');
    END P_REVERSE_SWIPE;

    ----------------------------------------------------------------------------
    PROCEDURE P_GENERATE_DAY_END_REPORT
    (
        P_REPORT_DATE    IN  DATE DEFAULT TRUNC(SYSDATE),
        P_EMPLOYEE_COUNT OUT NUMBER
    )
    AS
        V_REPORT_DATE DATE := TRUNC(NVL(P_REPORT_DATE, SYSDATE));
    BEGIN
        DELETE FROM HRD.HRD_LOUNGE_DAY_END_RPT
        WHERE  REPORT_DATE = V_REPORT_DATE;

        INSERT INTO HRD.HRD_LOUNGE_DAY_END_RPT
        (
            REPORT_DATE, EMPLOYEE_ID, CHECK_IN_COUNT, CHECK_OUT_COUNT,
            FIRST_CHECK_IN, LAST_CHECK_OUT, TOTAL_CHARGE, GENERATED_BY
        )
        SELECT V_REPORT_DATE,
               ST.EMPLOYEE_ID,
               COUNT(CASE WHEN ST.SWIPE_TYPE = C_CHECK_IN  THEN 1 END),
               COUNT(CASE WHEN ST.SWIPE_TYPE = C_CHECK_OUT THEN 1 END),
               MIN(CASE WHEN ST.SWIPE_TYPE = C_CHECK_IN  THEN ST.SWIPE_TIMESTAMP END),
               MAX(CASE WHEN ST.SWIPE_TYPE = C_CHECK_OUT THEN ST.SWIPE_TIMESTAMP END),
               SUM(ST.CHARGE_AMOUNT),
               F_CURRENT_USER
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN ST
        WHERE  ST.SWIPE_TIMESTAMP >= V_REPORT_DATE
        AND    ST.SWIPE_TIMESTAMP <  V_REPORT_DATE + 1
        AND    ST.STATUS          <> C_STATUS_REVERSED
        GROUP  BY ST.EMPLOYEE_ID;

        P_EMPLOYEE_COUNT := SQL%ROWCOUNT;
    END P_GENERATE_DAY_END_REPORT;

    ----------------------------------------------------------------------------
    FUNCTION F_GET_PENDING_DEDUCTION
    (
        P_EMPLOYEE_ID       IN NUMBER,
        P_PERIOD_FROM       IN DATE,
        P_PERIOD_TO         IN DATE,
        P_INCLUDE_ARREARS   IN VARCHAR2 DEFAULT 'Y'
    ) RETURN NUMBER
    AS
        V_AMOUNT NUMBER;
    BEGIN
        SELECT NVL(SUM(CHARGE_AMOUNT), 0)
        INTO   V_AMOUNT
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN
        WHERE  EMPLOYEE_ID     = P_EMPLOYEE_ID
        AND    STATUS          = C_STATUS_PENDING
        AND    SWIPE_TIMESTAMP < TRUNC(P_PERIOD_TO) + 1
        AND    (P_INCLUDE_ARREARS = 'Y' OR SWIPE_TIMESTAMP >= TRUNC(P_PERIOD_FROM));

        RETURN V_AMOUNT;
    END F_GET_PENDING_DEDUCTION;

    ----------------------------------------------------------------------------
    PROCEDURE P_PROCESS_PAYROLL_DEDUCTION
    (
        P_PAYROLL_ID        IN  NUMBER,
        P_PERIOD_FROM       IN  DATE,
        P_PERIOD_TO         IN  DATE,
        P_EMPLOYEE_ID       IN  NUMBER   DEFAULT NULL,
        P_INCLUDE_ARREARS   IN  VARCHAR2 DEFAULT 'Y',
        P_EMPLOYEE_COUNT    OUT NUMBER,
        P_TOTAL_AMOUNT      OUT NUMBER
    )
    AS
        V_PERIOD_FROM DATE := TRUNC(P_PERIOD_FROM);
        V_PERIOD_TO   DATE := TRUNC(P_PERIOD_TO);
        V_NOW         TIMESTAMP := SYSTIMESTAMP;
    BEGIN
        IF P_PAYROLL_ID IS NULL OR V_PERIOD_FROM IS NULL OR V_PERIOD_TO IS NULL THEN
            RAISE_APPLICATION_ERROR(-20110, 'Payroll id and period are required.');
        END IF;

        IF V_PERIOD_TO < V_PERIOD_FROM THEN
            RAISE_APPLICATION_ERROR(-20110, 'Payroll period end is before period start.');
        END IF;

        IF NVL(P_INCLUDE_ARREARS, 'X') NOT IN ('Y', 'N') THEN
            RAISE_APPLICATION_ERROR(-20110, 'P_INCLUDE_ARREARS must be Y or N.');
        END IF;

        -- 1. Claim the pending charges for this payroll run (row locks prevent a
        --    concurrent reversal or a second payroll run from taking them).
        UPDATE HRD.HRD_LOUNGE_SWIPE_TRN ST
        SET    ST.STATUS      = C_STATUS_DEDUCTED,
               ST.PAYROLL_ID  = P_PAYROLL_ID,
               ST.DEDUCTED_ON = V_NOW
        WHERE  ST.STATUS          = C_STATUS_PENDING
        AND    ST.SWIPE_TIMESTAMP < V_PERIOD_TO + 1
        AND    (P_INCLUDE_ARREARS = 'Y' OR ST.SWIPE_TIMESTAMP >= V_PERIOD_FROM)
        AND    (P_EMPLOYEE_ID IS NULL OR ST.EMPLOYEE_ID = P_EMPLOYEE_ID)
        AND    NOT EXISTS (SELECT 1
                           FROM   HRD.HRD_LOUNGE_DEDUCTION_DTL DD
                           WHERE  DD.PAYROLL_ID  = P_PAYROLL_ID
                           AND    DD.EMPLOYEE_ID = ST.EMPLOYEE_ID);

        -- 2. Amount to be deducted per employee. Rows claimed above are the ones
        --    carrying this payroll id for employees not yet in the detail table.
        SELECT COUNT(DISTINCT ST.EMPLOYEE_ID),
               NVL(SUM(ST.CHARGE_AMOUNT), 0)
        INTO   P_EMPLOYEE_COUNT,
               P_TOTAL_AMOUNT
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN ST
        WHERE  ST.PAYROLL_ID = P_PAYROLL_ID
        AND    NOT EXISTS (SELECT 1
                           FROM   HRD.HRD_LOUNGE_DEDUCTION_DTL DD
                           WHERE  DD.PAYROLL_ID  = P_PAYROLL_ID
                           AND    DD.EMPLOYEE_ID = ST.EMPLOYEE_ID);

        INSERT INTO HRD.HRD_LOUNGE_DEDUCTION_DTL
        (
            PAYROLL_ID, EMPLOYEE_ID, PERIOD_FROM, PERIOD_TO,
            CHECK_IN_COUNT, CHECK_OUT_COUNT, DEDUCTION_AMOUNT, CREATED_BY
        )
        SELECT P_PAYROLL_ID,
               ST.EMPLOYEE_ID,
               V_PERIOD_FROM,
               V_PERIOD_TO,
               COUNT(CASE WHEN ST.SWIPE_TYPE = C_CHECK_IN  THEN 1 END),
               COUNT(CASE WHEN ST.SWIPE_TYPE = C_CHECK_OUT THEN 1 END),
               SUM(ST.CHARGE_AMOUNT),
               F_CURRENT_USER
        FROM   HRD.HRD_LOUNGE_SWIPE_TRN ST
        WHERE  ST.PAYROLL_ID = P_PAYROLL_ID
        AND    NOT EXISTS (SELECT 1
                           FROM   HRD.HRD_LOUNGE_DEDUCTION_DTL DD
                           WHERE  DD.PAYROLL_ID  = P_PAYROLL_ID
                           AND    DD.EMPLOYEE_ID = ST.EMPLOYEE_ID)
        GROUP  BY ST.EMPLOYEE_ID;
    END P_PROCESS_PAYROLL_DEDUCTION;

    ----------------------------------------------------------------------------
    FUNCTION F_GET_PAYROLL_DEDUCTION
    (
        P_PAYROLL_ID   IN NUMBER,
        P_EMPLOYEE_ID  IN NUMBER
    ) RETURN NUMBER
    AS
        V_AMOUNT NUMBER;
    BEGIN
        SELECT NVL(SUM(DEDUCTION_AMOUNT), 0)
        INTO   V_AMOUNT
        FROM   HRD.HRD_LOUNGE_DEDUCTION_DTL
        WHERE  PAYROLL_ID  = P_PAYROLL_ID
        AND    EMPLOYEE_ID = P_EMPLOYEE_ID;

        RETURN V_AMOUNT;
    END F_GET_PAYROLL_DEDUCTION;

END PKG_STAFF_LOUNGE;
/
