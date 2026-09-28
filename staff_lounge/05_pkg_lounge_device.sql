--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 05 - PKG_LOUNGE_DEVICE
--
-- Narrow entry point for card readers / middleware. Granting EXECUTE on this
-- package lets a device account record swipes without any access to the
-- payroll, reversal or reporting procedures in PKG_STAFF_LOUNGE.
--------------------------------------------------------------------------------

CREATE OR REPLACE PACKAGE HRD.PKG_LOUNGE_DEVICE
AUTHID DEFINER
AS
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

END PKG_LOUNGE_DEVICE;
/

CREATE OR REPLACE PACKAGE BODY HRD.PKG_LOUNGE_DEVICE
AS
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
    BEGIN
        HRD.PKG_STAFF_LOUNGE.P_RECORD_SWIPE
        (
            P_CARD_NO          => P_CARD_NO,
            P_SWIPE_TYPE       => P_SWIPE_TYPE,
            P_SWIPE_TIMESTAMP  => P_SWIPE_TIMESTAMP,
            P_LOUNGE_CODE      => P_LOUNGE_CODE,
            P_DEVICE_ID        => P_DEVICE_ID,
            P_LOUNGE_SWIPE_ID  => P_LOUNGE_SWIPE_ID,
            P_RESULT_CODE      => P_RESULT_CODE,
            P_RESULT_MSG       => P_RESULT_MSG
        );
        COMMIT;  -- each swipe is its own unit of work for the device
    END P_RECORD_SWIPE;

END PKG_LOUNGE_DEVICE;
/
