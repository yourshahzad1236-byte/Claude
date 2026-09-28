--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction - installer
-- Run in SQL*Plus / SQLcl as HRD (or a DBA):  @install.sql
--------------------------------------------------------------------------------
WHENEVER SQLERROR EXIT SQL.SQLCODE ROLLBACK
SET DEFINE OFF

PROMPT 01 - Tables
@@01_ddl_tables.sql
PROMPT 02 - Triggers
@@02_triggers.sql
PROMPT 03 - Views
@@03_views.sql
PROMPT 04 - PKG_STAFF_LOUNGE
@@04_pkg_staff_lounge.sql
PROMPT 05 - PKG_LOUNGE_DEVICE
@@05_pkg_lounge_device.sql
PROMPT 06 - Scheduler job
@@06_scheduler_jobs.sql
PROMPT 07 - Grants
@@07_grants.sql

PROMPT Staff lounge module installed.
