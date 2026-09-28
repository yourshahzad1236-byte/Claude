--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 06 - Day-end report job
--
-- Runs shortly after midnight for the day that just ended, so swipes made
-- right up to 23:59:59 are included. Re-running for a date rebuilds it.
--------------------------------------------------------------------------------

BEGIN
    DBMS_SCHEDULER.CREATE_JOB
    (
        JOB_NAME        => 'HRD.JOB_LOUNGE_DAY_END_REPORT',
        JOB_TYPE        => 'PLSQL_BLOCK',
        JOB_ACTION      => q'[
            DECLARE
                V_EMPLOYEE_COUNT NUMBER;
            BEGIN
                HRD.PKG_STAFF_LOUNGE.P_GENERATE_DAY_END_REPORT
                (
                    P_REPORT_DATE    => TRUNC(SYSDATE) - 1,
                    P_EMPLOYEE_COUNT => V_EMPLOYEE_COUNT
                );
                COMMIT;
            END;]',
        START_DATE      => SYSTIMESTAMP,
        REPEAT_INTERVAL => 'FREQ=DAILY; BYHOUR=0; BYMINUTE=10; BYSECOND=0',
        ENABLED         => TRUE,
        COMMENTS        => 'Staff lounge day-end usage report (previous day)'
    );
END;
/
