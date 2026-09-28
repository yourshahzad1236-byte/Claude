--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 08 - Payroll integration example (reference only, not part of install)
--
-- Add the call below to the existing payroll run, inside the same
-- transaction, before net salary is calculated. Replace the HRD_PAYROLL_*
-- names with the real payroll tables / deduction codes.
--------------------------------------------------------------------------------

/*
-- Inside PKG_PAYROLL.P_PROCESS_PAYROLL (existing), after the payroll header
-- (V_PAYROLL_ID, V_PERIOD_FROM, V_PERIOD_TO) is created:

    HRD.PKG_STAFF_LOUNGE.P_PROCESS_PAYROLL_DEDUCTION
    (
        P_PAYROLL_ID      => V_PAYROLL_ID,
        P_PERIOD_FROM     => V_PERIOD_FROM,
        P_PERIOD_TO       => V_PERIOD_TO,
        P_EMPLOYEE_COUNT  => V_LOUNGE_EMP_COUNT,
        P_TOTAL_AMOUNT    => V_LOUNGE_TOTAL
    );

    -- Post one deduction line per employee into the payroll detail
    INSERT INTO HRD.HRD_PAYROLL_DTL
    (
        PAYROLL_ID, EMPLOYEE_ID, ELEMENT_CODE, ELEMENT_TYPE, AMOUNT
    )
    SELECT LD.PAYROLL_ID,
           LD.EMPLOYEE_ID,
           'LOUNGE_CHARGES',
           'DEDUCTION',
           LD.DEDUCTION_AMOUNT
    FROM   HRD.HRD_LOUNGE_DEDUCTION_DTL LD
    WHERE  LD.PAYROLL_ID = V_PAYROLL_ID;

    -- ... net salary calculation picks up the LOUNGE_CHARGES deduction ...

    -- The payroll run's own COMMIT makes the deduction final; a ROLLBACK
    -- returns every lounge charge to PENDING.

-- Per-employee payroll loops can instead call, for each employee:
--     P_PROCESS_PAYROLL_DEDUCTION(..., P_EMPLOYEE_ID => CUR_REC.EMPLOYEE_ID, ...)
--     V_LOUNGE_AMT := HRD.PKG_STAFF_LOUNGE.F_GET_PAYROLL_DEDUCTION(V_PAYROLL_ID, CUR_REC.EMPLOYEE_ID);
*/
