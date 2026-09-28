# Staff Lounge Usage Tracking & Payroll Deduction (HRD)

Records staff lounge card swipes, charges **600 per check-in** and **600 per check-out**, produces a day-end usage report, and deducts the accumulated charges from salary when payroll runs.

Naming follows the HRD Oracle SQL/PLSQL standards (`PKG_`, `P_`, `F_`, `V_`, `C_`, `EX_`, `TRG_`, `VW_`, `IDX_`, `_SEQ`, and the `MST`/`TRN`/`DTL`/`LOG` table suffixes).

## Install

```sql
-- SQL*Plus / SQLcl, connected as HRD (or a DBA)
@install.sql
```

Requires Oracle 12c+ (sequence `DEFAULT`, `FETCH FIRST`). The scripts assume the existing employee master is `HRD.HRD_EMPLOYEE_MST` with primary key `EMPLOYEE_ID`. If yours is named differently, change the foreign keys in `01_ddl_tables.sql`.

| Script | Contents |
|---|---|
| `01_ddl_tables.sql` | Sequences, tables, constraints, indexes, and the seeded 600/600 charge rates |
| `02_triggers.sql` | Audit columns, audit trail, and protection of financial data |
| `03_views.sql` | `VW_LOUNGE_DAILY_USAGE`, `VW_LOUNGE_PENDING_CHARGES` |
| `04_pkg_staff_lounge.sql` | `PKG_STAFF_LOUNGE`, which holds the business logic |
| `05_pkg_lounge_device.sql` | `PKG_LOUNGE_DEVICE`, the narrow swipe-only entry point for card readers |
| `06_scheduler_jobs.sql` | Day-end report job (00:10 daily, reports on the previous day) |
| `07_grants.sql` | Device, HR, and payroll roles (no direct table DML) |
| `08_payroll_integration_example.sql` | How to call the deduction from the existing payroll run (reference only) |

## Data model

| Table | Purpose |
|---|---|
| `HRD_LOUNGE_CHARGE_MST` | Rate per swipe type with an effective-date range. The seeded rate is CHECK_IN = 600 and CHECK_OUT = 600. |
| `HRD_LOUNGE_CARD_MST` | Lounge card number → `EMPLOYEE_ID`, with an active/blocked flag |
| `HRD_LOUNGE_SWIPE_TRN` | **The new swipe table.** Columns: `EMPLOYEE_ID`, `SWIPE_TYPE`, `SWIPE_TIMESTAMP`, `CHARGE_AMOUNT`, `STATUS` (`PENDING` → `DEDUCTED` or `REVERSED`), `PAYROLL_ID`, and audit columns |
| `HRD_LOUNGE_SWIPE_ERR_LOG` | Rejected or failed swipes |
| `HRD_LOUNGE_AUDIT_LOG` | Append-only history of every charge insert and status change |
| `HRD_LOUNGE_DEDUCTION_DTL` | The amount to deduct, one row per employee per payroll run |
| `HRD_LOUNGE_DAY_END_RPT` | Day-end summary: check-ins, check-outs, first in, last out, and total charge per employee per day |

The charge is copied onto each swipe row when the swipe is recorded. Changing the rate later never alters charges already recorded.

## Flow

1. **Swipe**: the reader calls `PKG_LOUNGE_DEVICE.P_RECORD_SWIPE(card_no, 'CHECK_IN' | 'CHECK_OUT', ...)`.
   It returns `P_RESULT_CODE` (`OK`, `UNKNOWN_CARD`, `CARD_BLOCKED`, `DUPLICATE_SWIPE`, `INVALID_SWIPE_TYPE`, `INVALID_SWIPE_TIME`, `NO_CHARGE_RATE`, `SYSTEM_ERROR`) and does not raise an error.
   Every rejected swipe is written to `HRD_LOUNGE_SWIPE_ERR_LOG` in an autonomous transaction.
   A repeat read of the same card with the same swipe type within 60 seconds counts as a hardware double-read and is not charged again.
2. **Day end**: `JOB_LOUNGE_DAY_END_REPORT` fills `HRD_LOUNGE_DAY_END_RPT` for the previous day, so it lists who checked in and who checked out.
   To regenerate a day manually, call `P_GENERATE_DAY_END_REPORT(date, n)`.
   For an event-level listing, APEX can query `VW_LOUNGE_DAILY_USAGE WHERE SWIPE_DATE = :P_DATE`.
3. **Payroll run**: the payroll run calls `PKG_STAFF_LOUNGE.P_PROCESS_PAYROLL_DEDUCTION(payroll_id, period_from, period_to, ...)` in its own transaction. This:
   - claims `PENDING` charges up to the period end (arrears included by default) and marks them `DEDUCTED` with the `PAYROLL_ID`
   - writes the per-employee sum to `HRD_LOUNGE_DEDUCTION_DTL`. Payroll posts that amount as a salary deduction (see `08_...`).

   The call is safe to repeat for the same payroll. If the payroll run rolls back, all the charges go back to `PENDING`.
4. **Corrections**: `P_REVERSE_SWIPE(id, reason)` cancels a `PENDING` charge. Deducted charges are locked, and any refund goes through payroll.

## Controls

- **Audit trail**: triggers log each charge insert and status change with the user, IP address, and time. The audit log is append-only.
- **Integrity**: the swipe's employee, type, time, and amount cannot be changed after the swipe is recorded. `DEDUCTED` and `REVERSED` rows are final. Rows cannot be deleted.
- **Security**: package access is definer-rights with static SQL and bind variables. Roles get `EXECUTE` on the packages, not DML on the tables. Card readers can only record swipes.
- **Scale**: the swipe path is one indexed lookup plus one insert. Payroll and reporting are set-based statements, not loops. There are indexes for status/time, employee/time, and payroll. See the partitioning note in `01_ddl_tables.sql` for very high volumes.

## Assumptions to confirm

- Charges apply to **each** check-in and **each** check-out, so one visit (in + out) costs 1,200.
- The employee master is `HRD_EMPLOYEE_MST(EMPLOYEE_ID)`. Payroll table and element names in `08_...` are placeholders.
- Unpaid charges from before the payroll period (arrears) are deducted in the next run. To limit a run to the period itself, pass `P_INCLUDE_ARREARS => 'N'`.
