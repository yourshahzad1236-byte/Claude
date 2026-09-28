--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 07 - Roles and grants
--
-- No role gets direct DML on the lounge tables; all changes go through the
-- packages, which enforce validation and write the audit trail.
-- Run as a DBA / user with CREATE ROLE. Grant the roles to the actual
-- device, APEX parsing-schema-proxy, HR and payroll accounts as needed.
--------------------------------------------------------------------------------

CREATE ROLE HRD_LOUNGE_DEVICE_ROLE;   -- card readers / swipe middleware
CREATE ROLE HRD_LOUNGE_HR_ROLE;       -- HR officers: reports, reversals, cards
CREATE ROLE HRD_LOUNGE_PAYROLL_ROLE;  -- payroll process

-- Devices: record swipes only
GRANT EXECUTE ON HRD.PKG_LOUNGE_DEVICE TO HRD_LOUNGE_DEVICE_ROLE;

-- HR: read usage, manage cards and rates, reverse pending charges
GRANT EXECUTE ON HRD.PKG_STAFF_LOUNGE          TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.VW_LOUNGE_DAILY_USAGE     TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.VW_LOUNGE_PENDING_CHARGES TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.HRD_LOUNGE_DAY_END_RPT    TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.HRD_LOUNGE_SWIPE_ERR_LOG  TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.HRD_LOUNGE_AUDIT_LOG      TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT  ON HRD.HRD_LOUNGE_DEDUCTION_DTL  TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT, INSERT, UPDATE ON HRD.HRD_LOUNGE_CARD_MST   TO HRD_LOUNGE_HR_ROLE;
GRANT SELECT, INSERT, UPDATE ON HRD.HRD_LOUNGE_CHARGE_MST TO HRD_LOUNGE_HR_ROLE;

-- Payroll: run deductions, read results
GRANT EXECUTE ON HRD.PKG_STAFF_LOUNGE          TO HRD_LOUNGE_PAYROLL_ROLE;
GRANT SELECT  ON HRD.VW_LOUNGE_PENDING_CHARGES TO HRD_LOUNGE_PAYROLL_ROLE;
GRANT SELECT  ON HRD.HRD_LOUNGE_DEDUCTION_DTL  TO HRD_LOUNGE_PAYROLL_ROLE;
