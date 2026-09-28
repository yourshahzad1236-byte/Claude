--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 03 - Views (APEX reports / payroll preview)
--------------------------------------------------------------------------------

----------------------------------------
-- Every lounge swipe with its calendar date; filter on SWIPE_DATE for the
-- "who checked in / who checked out today" report.
----------------------------------------
CREATE OR REPLACE VIEW HRD.VW_LOUNGE_DAILY_USAGE AS
SELECT ST.LOUNGE_SWIPE_ID,
       CAST(TRUNC(ST.SWIPE_TIMESTAMP) AS DATE) AS SWIPE_DATE,
       ST.SWIPE_TIMESTAMP,
       ST.EMPLOYEE_ID,
       CM.CARD_NO,
       ST.LOUNGE_CODE,
       ST.DEVICE_ID,
       ST.SWIPE_TYPE,
       ST.CHARGE_AMOUNT,
       ST.STATUS,
       ST.PAYROLL_ID
FROM   HRD.HRD_LOUNGE_SWIPE_TRN ST
JOIN   HRD.HRD_LOUNGE_CARD_MST  CM ON CM.LOUNGE_CARD_ID = ST.LOUNGE_CARD_ID;

----------------------------------------
-- Charges still waiting for payroll, per employee.
----------------------------------------
CREATE OR REPLACE VIEW HRD.VW_LOUNGE_PENDING_CHARGES AS
SELECT ST.EMPLOYEE_ID,
       COUNT(CASE WHEN ST.SWIPE_TYPE = 'CHECK_IN'  THEN 1 END) AS CHECK_IN_COUNT,
       COUNT(CASE WHEN ST.SWIPE_TYPE = 'CHECK_OUT' THEN 1 END) AS CHECK_OUT_COUNT,
       MIN(ST.SWIPE_TIMESTAMP)                                 AS OLDEST_SWIPE,
       MAX(ST.SWIPE_TIMESTAMP)                                 AS LATEST_SWIPE,
       SUM(ST.CHARGE_AMOUNT)                                   AS PENDING_AMOUNT
FROM   HRD.HRD_LOUNGE_SWIPE_TRN ST
WHERE  ST.STATUS = 'PENDING'
GROUP  BY ST.EMPLOYEE_ID;
