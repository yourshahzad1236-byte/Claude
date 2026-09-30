# 1. Overview
## 1.1 Summary
This design builds the Karachi transport allowance as a self-contained module in the HRD schema. It uses 12 new tables, one PL/SQL package (`HRD.PKG_TRANSPORT_ALLOWANCE`), a REST endpoint for the RFID terminals, 3 scheduled jobs and 10 APEX pages. No existing HRD table is altered: existing systems (employee master, ID cards, attendance, leave, payroll, dashboard) are only read through a small set of adapter functions.

The SRS still has 10 blocking questions, so every open business rule is a **setting in a versioned, maker-checker policy table** (`HRD_TRANSPORT_FORMULA_MST`), not code. When Finance or Mr. Ubaid decides, a user changes the setting, and the build is not blocked by the answers.

## 1.2 Source requirements
| Document | Version | Status |
|---|---|---|
| SRS: Karachi Transport Allowance & RFID Deduction (CR-YYYY-XXX) | 0.3 | DRAFT (not approved) |
| SRS review report | v2 (of SRS v0.2) | IN REVIEW |

> **WARNING: based on SRS v0.3 in status DRAFT; the design may change.** 10 blocking questions are open (Q-02, Q-03, Q-04, Q-05, Q-07, Q-09, Q-11, Q-14, Q-15, Q-17). Section 14.3 shows how each one is handled.

## 1.3 Scope of this design / out of scope
In scope: every FR-001 to FR-018 and NFR in SRS v0.3.

Out of scope:
- RFID reader hardware and its firmware. This design defines only the interface the readers must call (DS-05).
- Changes to the cafeteria or attendance use of the ID card.
- The payroll system's own import screen. This design delivers a payroll export view (DS-10).
- Tax calculation (SRS Q-08; payroll applies tax to the payout).

## 1.4 Schema context used
None. The HRD schema has not been indexed (`skmch-hrd-system-context` reports NOT YET INDEXED). Every reference to an existing object is **PROVISIONAL**. The change inventory (§11) carries a "verify against schema" task for each one, and the new tables deliberately don't depend on any existing table's structure.

# 2. Solution approach
## 2.1 Approach
1. **Capture:** RFID terminals send each swipe (card number, terminal, time, unique reference) to an ORDS REST endpoint. `P_RECORD_SWIPE` resolves the card to an employee through an adapter function, validates it, stores it and posts a dashboard notification. Replays of buffered offline swipes are ignored by their unique reference.
2. **Trips:** a job runs every 15 minutes and turns valid swipes into trips, using the direction and pairing rules in the active policy. Each trip stores its deduction, the fuel price and the formula version used.
3. **Adjustments:** employees request missed trips. Requests route by the policy's routing mode, escalate after N working days, and on approval become MANUAL trips.
4. **Monthly settlement:** Finance closes the period. `P_CLOSE_PERIOD` computes the allowance, deductions and payout per employee using the policy's settlement and proration modes, then Finance sends the register to payroll.
5. **Transparency:** employee self-service pages, the HR/Finance transaction trail, the non-swipe report and a full audit log.

## 2.2 Alternatives considered
| Option | Pros | Cons | Decision |
|---|---|---|---|
| Hard-code the rules as described in the MoM, and change the code when answers arrive | Simpler code | 10 open questions; any answer after the build means rework in the last week of October | Rejected |
| **Versioned policy table with settings for each open rule** | Build proceeds now; answers become data changes; maker-checker and history for free | More test combinations; settings must be explained to Finance | **Chosen** |
| Terminals write directly to a staging table in HRD | No REST layer | Needs DB credentials on devices; no per-swipe validation feedback | Rejected (kept as fallback, Q-19) |
| **ORDS REST endpoint for terminals** | Per-swipe response under 1 second; idempotent replay; no DB credentials on devices | Needs ORDS configured | **Chosen**, subject to vendor capability (Q-19) |
| Add columns to the employee master for eligibility | One place for employee data | Alters an unverified existing table used by many modules | Rejected: new `HRD_TRANSPORT_ELIGIBILITY_DTL` |
| Business logic in APEX page processes | Faster to click together | Rules duplicated across pages; hard to test | Rejected: all logic in `PKG_TRANSPORT_ALLOWANCE` |

## 2.3 Key design decisions
| ID | Decision | Rationale | Related FR/NFR |
|---|---|---|---|
| KD-01 | Every open business rule is a policy setting, versioned by effective date, activated with maker-checker | Unblocks the build; auditable | FR-002, FR-009, NFR-SEC-02 |
| KD-02 | No existing HRD table is altered; existing data is read only through adapter functions `F_GET_EMPLOYEE_BY_CARD`, `F_IS_PRESENT`, `F_IS_ON_LEAVE` and `F_GET_SUPERVISOR` | Existing tables are unverified (RV-10); lowest regression risk; one place to change when the schema is known | FR-004, FR-012, FR-014, NFR-INT-01 |
| KD-03 | Swipes and trips are never deleted; corrections reverse them with a reason | Audit trail | NFR-AUD-01 |
| KD-04 | Each trip stores the fuel price and formula version used | Disputes can be answered from the trip itself | RULE-06, FR-017 |
| KD-05 | Swipe idempotency through a unique `SOURCE_REF` supplied by the terminal | Safe offline replay | NFR-AVL-01 |
| KD-06 | First decision wins on adjustments, enforced by `ROW_VERSION` | Concurrency when two approvers can act | FR-013 AC4 |
| KD-07 | Keep the name `HRD_FUEL_PRICE_HIS`: rows are a price history read by effective date (closes review RV-15) | Consistent with HRD suffix meaning | FR-008 |

# 3. Requirements-to-design traceability
| Requirement | Design elements | Notes |
|---|---|---|
| FR-001 | DS-04, DS-17 | Eligibility periods; page 730 |
| FR-002 | DS-01, DS-09 | Allowance amount and base days in policy; proration mode (Q-04) |
| FR-003 | DS-05 | `P_RECORD_SWIPE` |
| FR-004 | DS-05 | `F_GET_EMPLOYEE_BY_CARD` adapter (PROVISIONAL source, Q-09) |
| FR-005 | DS-03, DS-17 | Terminal master; page 740 |
| FR-006 | DS-06, DS-16 | `P_DERIVE_TRIPS`, job every 15 minutes |
| FR-007 | DS-07 | `F_CALC_TRIP_COST`, RATE_MISSING handling |
| FR-008 | DS-02, DS-17 | Fuel price history, maker-checker; page 710 |
| FR-009 | DS-01, DS-17 | Policy versions with a worked example; page 720 |
| FR-010 | DS-09 | `P_CLOSE_PERIOD`, settlement mode (Q-07) |
| FR-011 | DS-08, DS-17 | `P_SUBMIT_ADJUSTMENT`; page 755 |
| FR-012 | DS-08, DS-16 | Routing mode (Q-11); escalation job |
| FR-013 | DS-08, DS-17 | `P_DECIDE_ADJUSTMENT`, first decision wins; page 760 |
| FR-014 | DS-04, DS-14, DS-17 | Non-swipe query with exemptions; page 780 |
| FR-015 | DS-11 | Notification rows written with each swipe |
| FR-016 | DS-12, DS-17 | `VW_TRANSPORT_MY_TRIPS`; page 750 |
| FR-017 | DS-13, DS-17 | `VW_TRANSPORT_TRAIL`, audit log; page 770 |
| FR-018 | DS-09, DS-10, DS-17 | `P_SEND_TO_PAYROLL`, `VW_TRANSPORT_PAYROLL_EXPORT`; page 790 |
| NFR-PERF-01 | DS-05, DS-11 | Notification written in the same call as the swipe |
| NFR-PERF-02 | DS-05 | Single indexed insert; endpoint budget under 300 ms |
| NFR-AVL-01 | DS-05 | Idempotent `SOURCE_REF`; original `SWIPE_TIME` kept |
| NFR-SEC-01 | DS-15 | Authorization schemes; views filtered by the logged-in employee |
| NFR-SEC-02 | DS-01, DS-02 | Maker ≠ checker check constraint and procedure check |
| NFR-AUD-01 | DS-13 | Audit log; delete-blocking triggers; reversal with reason |
| NFR-DAT-01 | DS-18 | Purge procedure, disabled until Q-18 is answered |
| NFR-CMP-01 | DS-09, DS-10 | Whole-rupee rounding; tax left to payroll |
| NFR-INT-01 | DS-05 | Card resolved through the existing card data |
| NFR-USA-01 | DS-17 | Responsive Universal Theme pages; request form in 3 steps |
| NFR-OPS-01 | DS-03, DS-16 | `LAST_SEEN_ON`; terminal health job |

# 4. Current-state impact analysis
## 4.1 Existing objects involved
| Object | Type | Current role | Change | Evidence |
|---|---|---|---|---|
| Employee master (name TBC) | Table | Employee identity, status | Read-only via adapters | None: PROVISIONAL |
| ID card / RFID mapping (name TBC, used by cafeteria and attendance) | Table or external system | Card number → employee, card status | Read-only via `F_GET_EMPLOYEE_BY_CARD` | MoM M-12: PROVISIONAL |
| Attendance records (name TBC) | Table | Days present | Read-only via `F_IS_PRESENT` | MoM M-12: PROVISIONAL |
| Leave records (name TBC) | Table | Approved leave | Read-only via `F_IS_ON_LEAVE` | SRS IMP-27: PROVISIONAL |
| Reporting line / supervisor (name TBC) | Table | Employee → supervisor | Read-only via `F_GET_SUPERVISOR` | SRS FR-012: PROVISIONAL |
| Payroll import (name TBC) | Interface | Monthly earnings and deductions | Reads `VW_TRANSPORT_PAYROLL_EXPORT` | SRS IMP-10: PROVISIONAL |
| Employee dashboard / self-service app (TBC) | APEX app or portal | Staff home page | Shows `HRD_TRANSPORT_NOTIFY_LOG` rows | SRS Q-13: PROVISIONAL |
| HR APEX application (ID TBC) | APEX app | Hosts HR screens | New pages 710–790 added | PROVISIONAL (Q-20) |

## 4.2 Dependency analysis
| Changed object | Dependent object | Dependent type | Impact | Action |
|---|---|---|---|---|
| None | None | None | No existing table, view, package or trigger is modified | None. Existing modules need no retest, except the HR APEX app, which gets new pages (retest its navigation menu and authorization) |
| New adapter functions | Existing card, attendance, leave and supervisor tables | Read | New read load: one indexed card lookup per swipe | Check the card table has an index on card number (verify at schema indexing) |

## 4.3 Reuse
| Existing unit | What it does | How reused / extended |
|---|---|---|
| Error-logging package, if one exists (e.g. `PKG_*LOG*`) | Central error logging | Use it in `WHEN OTHERS` handlers; otherwise log to `HRD_TRANSPORT_AUDIT_LOG` (verify at schema indexing) |
| Existing APEX authentication and roles | Staff login | Reused; new authorization schemes sit on top (DS-15) |
| Existing working-days or holiday calendar, if one exists | Working days per month | Used by settlement for SCALE_ALLOWANCE and WORKING_DAYS proration; otherwise Monday–Saturday is computed (A-D1) |

# 5. Data design
## 5.1 Entity changes overview
12 new tables, all created by `CR-YYYY-XXX_01_ddl.sql`:
- **Policy and reference data:** `HRD_TRANSPORT_FORMULA_MST` (policy versions), `HRD_FUEL_PRICE_HIS`, `HRD_TRANSPORT_TERMINAL_MST`.
- **Who:** `HRD_TRANSPORT_ELIGIBILITY_DTL` and `HRD_TRANSPORT_EXEMPT_DTL`.
- **Transactions:** swipes (`HRD_TRANSPORT_SWIPE_TRN`) become trips (`HRD_TRANSPORT_TRIP_TRN`). Adjustment requests (`HRD_TRANSPORT_ADJ_REQUEST`) create MANUAL trips.
- **Settlement:** trips belong to a period (`HRD_TRANSPORT_PERIOD_MST`) and are summed into `HRD_TRANSPORT_MONTHLY_DTL`.
- **Cross-cutting:** `HRD_TRANSPORT_NOTIFY_LOG` and `HRD_TRANSPORT_AUDIT_LOG`.

Every table has `CREATED_BY/ON` (defaults from the APEX user) and `MODIFIED_BY/ON` (set by the package). Primary keys use sequence defaults (`NAME_SEQ.NEXTVAL`), so no BI triggers are needed. `EMPLOYEE_ID` columns have no FK until the employee master is confirmed (Q-09).

**Volume (per 1,000 bus users, headcount to be confirmed, Q-22):** about 104,000 swipes and 52,000 trips a month (4 swipes and 2 trips a day × 26 days); about 1.25 million swipe rows a year. Normal heap tables and indexes are enough. If headcount is above 5,000, add monthly interval partitioning on `HRD_TRANSPORT_SWIPE_TRN.SWIPE_TIME`.

## 5.2 New tables
### DS-01 HRD.HRD_TRANSPORT_FORMULA_MST (satisfies FR-002, FR-009, NFR-SEC-02)
Purpose: versioned policy with the allowance, the deduction formula and a setting for each open business rule. One row is ACTIVE for any date. Estimated volume: fewer than 50 rows.
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| FORMULA_ID | NUMBER(10) | N | TRANSPORT_FORMULA_SEQ | PK | |
| VERSION_NO | NUMBER(5) | N | | UK | Human-readable version |
| EFFECTIVE_FROM | DATE | N | | Unique among ACTIVE | Applies to trips and periods from this date |
| ALLOWANCE_AMOUNT | NUMBER(10,2) | N | | > 0 | Reference 24,000 PKR (RULE-01) |
| ALLOWANCE_BASE_DAYS | NUMBER(2) | N | | 1–31 | Reference 24 |
| FORMULA_TYPE | VARCHAR2(20) | N | FUEL_INDEXED | FUEL_INDEXED / FIXED | Q-05 |
| BASE_TRIP_COST | NUMBER(10,2) | N | | > 0 | Reference 500 PKR (RULE-02) |
| REF_FUEL_PRICE | NUMBER(10,2) | N | | > 0 | Fuel price at which the trip costs BASE_TRIP_COST |
| SETTLEMENT_MODE | VARCHAR2(20) | N | | CAP_ZERO / SCALE_ALLOWANCE / DERIVE_TRIP_COST / RECOVER_EXCESS | Q-07 |
| PRORATION_MODE | VARCHAR2(20) | N | | NONE / CALENDAR_DAYS / WORKING_DAYS | Q-04 |
| DEDUCTION_BASIS | VARCHAR2(10) | N | | PER_TRIP / PER_SWIPE | Q-02 |
| SINGLE_SWIPE_RULE | VARCHAR2(20) | N | | COUNT_TRIP / REVIEW | Q-02 |
| DIRECTION_MODE | VARCHAR2(10) | N | | TERMINAL / SEQUENCE | Q-15 |
| ROUTING_MODE | VARCHAR2(20) | N | | SUPERVISOR / COORDINATOR / BOTH_FIRST_WINS | Q-11 |
| LATE_PRICE_MODE | VARCHAR2(20) | N | RECALCULATE | RECALCULATE / FROM_ENTRY | Q-16 |
| REPEAT_SWIPE_MINUTES | NUMBER(3) | N | 2 | 0–120 | FR-006 AC2 (proposed default) |
| ESCALATION_DAYS | NUMBER(2) | N | 2 | 1–30 | FR-012 AC3 (proposed default) |
| ADJ_WINDOW_DAYS | NUMBER(3) | Y | | | Q-10. NULL = no window check |
| PAYROLL_CUTOFF_DAY | NUMBER(2) | Y | | 1–31 | Q-14. Informational; Finance closes the period manually |
| STATUS | VARCHAR2(10) | N | PENDING | PENDING / ACTIVE / REJECTED / RETIRED | |
| MAKER_BY | VARCHAR2(100) | N | | | Who entered it |
| CHECKER_BY | VARCHAR2(100) | Y | | ≠ MAKER_BY | Who activated or rejected it |
| CHECKED_ON | DATE | Y | | | |
| Audit columns | | | | | CREATED_BY/ON, MODIFIED_BY/ON |

**Formula (FUEL_INDEXED, pending Q-05):** trip cost = ROUND(BASE_TRIP_COST × fuel price at trip time ÷ REF_FUEL_PRICE, 0). FIXED: trip cost = BASE_TRIP_COST.

### DS-02 HRD.HRD_FUEL_PRICE_HIS (satisfies FR-008, RULE-06, NFR-SEC-02)
Purpose: fuel price per litre, effective-dated, maker-checker. The price for a moment is the latest ACTIVE row with EFFECTIVE_FROM at or before it. Volume: about 25–50 rows a year.
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| FUEL_PRICE_ID | NUMBER(10) | N | FUEL_PRICE_SEQ | PK | |
| PRICE_PER_LITRE | NUMBER(10,2) | N | | > 0 | |
| EFFECTIVE_FROM | DATE | N | | Unique among ACTIVE | Date and time |
| STATUS | VARCHAR2(10) | N | PENDING | PENDING / ACTIVE / REJECTED | |
| MAKER_BY, CHECKER_BY, CHECKED_ON | | | | CHECKER_BY ≠ MAKER_BY | Maker-checker |
| REMARKS | VARCHAR2(500) | Y | | | For example, the source of the announcement |
| Audit columns | | | | | |

### DS-03 HRD.HRD_TRANSPORT_TERMINAL_MST (satisfies FR-005, NFR-OPS-01)
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| TERMINAL_ID | NUMBER(10) | N | TRANSPORT_TERMINAL_SEQ | PK | |
| TERMINAL_CODE | VARCHAR2(30) | N | | UK | Code the terminal sends, for example KDC-01 |
| TERMINAL_NAME | VARCHAR2(100) | N | | | |
| LOCATION_CODE | VARCHAR2(30) | N | | | KDC, HOSPITAL; more stops possible (Q-01) |
| TERMINAL_DIRECTION | VARCHAR2(10) | N | BOTH | BOARDING / ALIGHTING / BOTH | Used when DIRECTION_MODE = TERMINAL |
| DEVICE_REF | VARCHAR2(100) | Y | | | Vendor serial or IP |
| IS_ACTIVE | CHAR(1) | N | Y | Y/N | |
| LAST_SEEN_ON | DATE | Y | | | Last swipe or heartbeat |
| Audit columns | | | | | |

### DS-04 HRD.HRD_TRANSPORT_ELIGIBILITY_DTL and HRD.HRD_TRANSPORT_EXEMPT_DTL (satisfies FR-001, FR-014 AC3)
Eligibility: `ELIGIBILITY_ID` (PK), `EMPLOYEE_ID`, `EFFECTIVE_FROM`, `EFFECTIVE_TO` (null = open), `BUS_MANDATORY` (Y/N, Q-03), `REMARKS`, audit columns. Periods may not overlap for one employee (checked in `P_SET_ELIGIBILITY`).

Exemptions: `EXEMPT_ID` (PK), `EMPLOYEE_ID`, `EXEMPT_FROM`, `EXEMPT_TO`, `REASON_CODE` (NO_BUS_SHIFT / OWN_TRANSPORT / OTHER), `REMARKS`, `APPROVED_BY`, audit columns. These are days that are not counted as missed trips (FR-014 AC3). Until a roster feed exists (Q-17, IMP-26), HR records shift-without-bus periods here.

### DS-05 HRD.HRD_TRANSPORT_SWIPE_TRN (satisfies FR-003, FR-004, NFR-AVL-01, NFR-AUD-01)
Purpose: every swipe received. Never deleted. Volume: see §5.1.
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| SWIPE_ID | NUMBER(15) | N | TRANSPORT_SWIPE_SEQ | PK | |
| SOURCE_REF | VARCHAR2(100) | N | | UK | Terminal id + device sequence; idempotency key |
| CARD_NO | VARCHAR2(50) | N | | | As read |
| EMPLOYEE_ID | NUMBER(10) | Y | | | Null when the card is unknown |
| TERMINAL_ID | NUMBER(10) | N | | FK → terminal | |
| SWIPE_TIME | DATE | N | | | Time at the terminal |
| RECEIVED_ON | DATE | N | SYSDATE | | Time received (offline replays arrive late) |
| DIRECTION | VARCHAR2(10) | Y | | BOARDING / ALIGHTING | Set on receipt (TERMINAL mode) or by trip derivation (SEQUENCE mode) |
| SWIPE_STATUS | VARCHAR2(15) | N | | VALID / UNKNOWN_CARD / INACTIVE_CARD / NOT_ELIGIBLE / DUPLICATE / REVERSED | |
| TRIP_ID | NUMBER(15) | Y | | FK → trip | Set when used in a trip |
| REVERSAL_REASON | VARCHAR2(500) | Y | | | |
| Audit columns | | | | | |

### DS-06 / DS-07 HRD.HRD_TRANSPORT_TRIP_TRN (satisfies FR-006, FR-007, FR-013)
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| TRIP_ID | NUMBER(15) | N | TRANSPORT_TRIP_SEQ | PK | |
| EMPLOYEE_ID | NUMBER(10) | N | | | |
| PERIOD_ID | NUMBER(10) | N | | FK → period | Period of TRIP_DATE |
| TRIP_DATE | DATE | N | | | Date of the start of the trip |
| TRIP_DIRECTION | VARCHAR2(15) | N | | KDC_TO_HOSP / HOSP_TO_KDC / UNKNOWN | |
| START_TIME, END_TIME | DATE | Y | | | Boarding and alighting swipe times |
| TRIP_SOURCE | VARCHAR2(10) | N | | RFID / MANUAL | MANUAL requires ADJ_REQUEST_ID |
| TRIP_STATUS | VARCHAR2(15) | N | | VALID / INCOMPLETE / RATE_MISSING / REVERSED | |
| FORMULA_ID, FUEL_PRICE_ID | NUMBER(10) | Y | | FKs | Used for the deduction |
| FUEL_PRICE | NUMBER(10,2) | Y | | | Copy of the price used |
| DEDUCTION_AMOUNT | NUMBER(10,2) | Y | | ≥ 0 | Null until calculated |
| ADJ_REQUEST_ID | NUMBER(10) | Y | | FK → adjustment | |
| REVERSAL_REASON | VARCHAR2(500) | Y | | | |
| Audit columns | | | | | |

### DS-08 HRD.HRD_TRANSPORT_ADJ_REQUEST (satisfies FR-011, FR-012, FR-013, RULE-05)
| Column | Data type | Null | Default | Constraint | Description |
|---|---|---|---|---|---|
| ADJ_REQUEST_ID | NUMBER(10) | N | TRANSPORT_ADJ_REQ_SEQ | PK | |
| EMPLOYEE_ID | NUMBER(10) | N | | | Requester |
| TRIP_DATE | DATE | N | | Truncated date | |
| TRIP_DIRECTION | VARCHAR2(15) | N | | KDC_TO_HOSP / HOSP_TO_KDC | |
| REASON | VARCHAR2(500) | N | | ≥ 10 characters | |
| STATUS | VARCHAR2(10) | N | SUBMITTED | SUBMITTED / ESCALATED / APPROVED / REJECTED / CANCELLED | One open or approved request per employee, date and direction |
| APPROVER_ID | NUMBER(10) | Y | | | Current assignee |
| ESCALATED_ON | DATE | Y | | | |
| DECIDED_BY, DECIDED_ON, DECISION_COMMENT | | Y | | | |
| ROW_VERSION | NUMBER(10) | N | 1 | | First decision wins (KD-06) |
| Audit columns | | | | | |

### DS-09 HRD.HRD_TRANSPORT_PERIOD_MST and HRD.HRD_TRANSPORT_MONTHLY_DTL (satisfies FR-002, FR-010, FR-018)
Period: `PERIOD_ID`, `PERIOD_CODE` ('YYYY-MM', UK), `PERIOD_START`, `PERIOD_END`, `STATUS` (OPEN → CLOSED → SENT; REOPENED by Finance only), `CLOSED_BY/ON`, `SENT_BY/ON`, `REOPEN_REASON`, audit columns.

Monthly, one row per period and employee: `ELIGIBLE_DAYS`, `WORKING_DAYS`, `ALLOWANCE_AMOUNT`, `TRIP_COUNT`, `TOTAL_DEDUCTION`, `PRIOR_PERIOD_CORRECTION` (FR-018 AC3), `EXCESS_AMOUNT` (deductions above the allowance), `PAYOUT_AMOUNT`, `FINANCE_REVIEW_FLAG`, and `FORMULA_ID` (policy used). Unique on (PERIOD_ID, EMPLOYEE_ID).

### DS-11 HRD.HRD_TRANSPORT_NOTIFY_LOG and DS-13 HRD.HRD_TRANSPORT_AUDIT_LOG
Notifications: `NOTIFY_ID`, `EMPLOYEE_ID` or `RECIPIENT_ROLE`, `NOTIFY_TYPE` (SWIPE, ADJ_PENDING, ADJ_DECISION, ADJ_ESCALATED, RATE_MISSING, TERMINAL_OFFLINE), `REF_ID`, `MESSAGE_TEXT`, `IS_READ`, `CREATED_ON`.

Audit: `AUDIT_ID`, `ENTITY_NAME`, `ENTITY_ID`, `ACTION_CODE`, `OLD_VALUE` and `NEW_VALUE` (JSON CLOB), `REASON`, `ACTION_BY`, `ACTION_ON`.

## 5.3 Modified tables
None. KD-02: no existing HRD table is altered.

## 5.4 Constraints, indexes, sequences, triggers, views
| DS | Object name | Type | Definition | Reason |
|---|---|---|---|---|
| DS-01 | IDX_TRFORMULA_ACTIVE_FROM | Unique function index | EFFECTIVE_FROM where STATUS = ACTIVE | One active policy per effective date |
| DS-02 | IDX_FUELPRICE_ACTIVE_FROM | Unique function index | EFFECTIVE_FROM where STATUS = ACTIVE | No two active prices at the same moment |
| DS-02 | IDX_FUELPRICE_STATUS_FROM | Index | (STATUS, EFFECTIVE_FROM) | Price lookup |
| DS-05 | UK_TRSWIPE_SOURCE_REF | Unique | SOURCE_REF | Idempotent replay |
| DS-05 | IDX_TRSWIPE_EMP_TIME | Index | (EMPLOYEE_ID, SWIPE_TIME) | Derivation, employee view, trail |
| DS-05 | IDX_TRSWIPE_UNPROCESSED | Function index | SWIPE_TIME where TRIP_ID is null and status VALID | Fast job pickup |
| DS-05 | IDX_TRSWIPE_TERMINAL, IDX_TRSWIPE_TRIP | Index | FK columns | FK indexing |
| DS-06 | IDX_TRTRIP_EMP_PERIOD, IDX_TRTRIP_PERIOD_STATUS | Index | | Settlement, views |
| DS-06 | IDX_TRTRIP_FORMULA, IDX_TRTRIP_FUEL_PRICE, IDX_TRTRIP_ADJ_REQUEST | Index | FK columns | FK indexing |
| DS-06 | IDX_TRTRIP_ONE_PER_LEG | Unique function index | Employee, date, direction, start time for non-reversed trips | No duplicate derived trips |
| DS-08 | IDX_TRADJ_OPEN_UNIQUE | Unique function index | Employee, date, direction for SUBMITTED/ESCALATED/APPROVED | One live request per missed trip |
| DS-08 | IDX_TRADJ_APPROVER_STATUS, IDX_TRADJ_EMP_DATE | Index | | Approver inbox, duplicate checks |
| DS-04 | IDX_TRELIG_EMP_FROM, IDX_TREXEMPT_EMP_FROM | Index | | Lookups by employee and date |
| DS-09 | IDX_TRMONTHLY_FORMULA, IDX_TRMONTHLY_EMP | Index | | FK indexing, employee history |
| DS-11 | IDX_TRNOTIFY_EMP_UNREAD, IDX_TRNOTIFY_ROLE_UNREAD | Index | | Dashboard reads |
| DS-13 | IDX_TRAUDIT_ENTITY, IDX_TRAUDIT_ACTION_ON | Index | | Trail search |
| DS-13 | TRG_TRANSPORT_SWIPE_BD, TRG_TRANSPORT_TRIP_BD | Statement trigger | Raises -20720 / -20721 on DELETE | Never delete (NFR-AUD-01) |
| All | 12 sequences `*_SEQ` | Sequence | Used as column defaults | HRD standard |
| DS-12 | VW_TRANSPORT_MY_TRIPS | View | Trips, deductions and adjustments of the logged-in employee | FR-016 |
| DS-13 | VW_TRANSPORT_TRAIL | View | Swipe → trip → price, formula, adjustment, approver | FR-017 |
| DS-10 | VW_TRANSPORT_PAYROLL_EXPORT | View | SENT periods: employee, period, payout | FR-018 |

## 5.5 Grants, synonyms, VPD / security policies
- `EXECUTE ON HRD.PKG_TRANSPORT_ALLOWANCE` to the APEX parsing schema (if different from HRD) and to the ORDS runtime schema.
- `SELECT ON HRD.VW_TRANSPORT_PAYROLL_EXPORT` to the payroll interface user (name TBC).
- `SELECT ON HRD.HRD_TRANSPORT_NOTIFY_LOG` (or a view over it) to the dashboard's schema (Q-13).
- No direct DML grants on any transport table. All changes go through the package.
- VPD is not needed: views and the package filter by the logged-in employee (DS-15).

## 5.6 Data migration / backfill
None: this is a new module. Seed data (`CR-YYYY-XXX_02_seed.sql`):
- terminals KDC-01 and HOSP-01;
- period 2026-11;
- policy version 1 as PENDING, with the reference values and the default settings in §14.3;
- a first fuel price, as PENDING.

Finance activates both through the maker-checker pages before go-live. The script is re-runnable, guarded by `MERGE` on the codes.

# 6. Application logic design
All units are in `HRD.PKG_TRANSPORT_ALLOWANCE`. Low-level units don't commit. APEX processes, ORDS handlers and jobs own the transaction (commit at the end of the request or job step). Exceptions use -20701 to -20721 (§6.10).

## 6.1 DS-05 P_RECORD_SWIPE (satisfies FR-003, FR-004, FR-015, NFR-AVL-01, NFR-PERF-02) [NEW]
**Signature:**
```sql
PROCEDURE P_RECORD_SWIPE
(
    P_SOURCE_REF     IN  HRD_TRANSPORT_SWIPE_TRN.SOURCE_REF%TYPE,
    P_CARD_NO        IN  HRD_TRANSPORT_SWIPE_TRN.CARD_NO%TYPE,
    P_TERMINAL_CODE  IN  HRD_TRANSPORT_TERMINAL_MST.TERMINAL_CODE%TYPE,
    P_SWIPE_TIME     IN  HRD_TRANSPORT_SWIPE_TRN.SWIPE_TIME%TYPE,
    P_RESULT         OUT VARCHAR2,   -- ACCEPTED / DUPLICATE / REJECTED
    P_MESSAGE        OUT VARCHAR2
);
```
**Logic:**
1. If `SOURCE_REF` already exists, return DUPLICATE with no change (idempotent replay).
2. Find the active terminal by code, otherwise raise -20701 "Unknown or inactive terminal". Set `LAST_SEEN_ON`.
3. Look up the employee with `F_GET_EMPLOYEE_BY_CARD(P_CARD_NO, V_CARD_STATUS)`:
   - no employee → status UNKNOWN_CARD;
   - card inactive → INACTIVE_CARD (FR-004 AC2);
   - not eligible on that date → NOT_ELIGIBLE (FR-001 AC2).
4. Repeat check: if the same employee swiped the same terminal within `REPEAT_SWIPE_MINUTES`, store as DUPLICATE (FR-006 AC2).
5. If DIRECTION_MODE = TERMINAL and the terminal's direction is not BOTH, set DIRECTION from the terminal.
6. Insert the swipe. For a VALID swipe, insert a SWIPE notification: "Swipe recorded: [location], [direction], [HH24:MI]" (FR-015).
7. Return ACCEPTED, or REJECTED with a message for UNKNOWN/INACTIVE cards (the terminal shows it).

**Transaction:** caller (ORDS handler) commits. **Performance:** 2 indexed reads + 2 inserts; target under 300 ms.

## 6.2 DS-06 P_DERIVE_TRIPS (satisfies FR-006, RULE-04) [NEW]
```sql
PROCEDURE P_DERIVE_TRIPS (P_UP_TO IN DATE DEFAULT SYSDATE - 5/1440);
```
1. Take VALID swipes with no TRIP_ID and SWIPE_TIME ≤ P_UP_TO, ordered by employee and time (BULK COLLECT, LIMIT 1000).
2. Per employee, walk the swipes in time order:
   - **TERMINAL mode:** a BOARDING swipe opens a leg; the next ALIGHTING swipe at the other location closes it.
   - **SEQUENCE mode:** the first swipe opens a leg at its location; the next swipe at a *different* location closes it. A swipe at the *same* location after the repeat window opens a new leg, and the previous one becomes single.
3. Closed leg → trip from the start location to the end location, TRIP_SOURCE RFID, TRIP_DATE = TRUNC(start). Link both swipes (TRIP_ID).
4. Single swipe older than 4 hours with no pair:
   - SINGLE_SWIPE_RULE = COUNT_TRIP → VALID trip with the direction inferred from the location;
   - SINGLE_SWIPE_RULE = REVIEW → INCOMPLETE trip for HR review (FR-006 AC3).
5. DEDUCTION_BASIS = PER_SWIPE: each valid swipe produces its own trip row (the settings interpret "trip" as a swipe).
6. Price each new VALID trip with `F_CALC_TRIP_COST` (DS-07).
7. Attach the trip to the OPEN period of TRIP_DATE. If that period is CLOSED or SENT, attach it to the next OPEN period and record it as a prior-period correction (FR-018 AC3).

**Transaction:** commits every 1,000 employees (job). Re-runnable: it only picks up unlinked swipes.

## 6.3 DS-07 F_CALC_TRIP_COST and F_GET_FUEL_PRICE (satisfies FR-007, RULE-02, RULE-06, NFR-CMP-01) [NEW]
```sql
FUNCTION F_GET_FUEL_PRICE (P_AT IN DATE, P_FUEL_PRICE_ID OUT HRD_FUEL_PRICE_HIS.FUEL_PRICE_ID%TYPE)
RETURN HRD_FUEL_PRICE_HIS.PRICE_PER_LITRE%TYPE;

FUNCTION F_CALC_TRIP_COST (P_AT IN DATE, P_FORMULA_ID OUT HRD_TRANSPORT_FORMULA_MST.FORMULA_ID%TYPE,
                           P_FUEL_PRICE_ID OUT HRD_FUEL_PRICE_HIS.FUEL_PRICE_ID%TYPE)
RETURN NUMBER;
```
1. Active policy at P_AT, otherwise raise -20702 "No active transport policy".
2. FIXED → return BASE_TRIP_COST.
3. FUEL_INDEXED → price at P_AT. With no price, return NULL; the caller marks the trip RATE_MISSING and posts a RATE_MISSING alert to the FINANCE role (FR-007 AC3).
4. Return ROUND(BASE_TRIP_COST × price ÷ REF_FUEL_PRICE, 0) (whole rupees, NFR-CMP-01).

## 6.4 DS-01 / DS-02 Policy and fuel price maintenance (satisfies FR-008, FR-009, NFR-SEC-02) [NEW]
```sql
PROCEDURE P_SAVE_FUEL_PRICE   (P_PRICE IN NUMBER, P_EFFECTIVE_FROM IN DATE, P_REMARKS IN VARCHAR2, P_FUEL_PRICE_ID OUT NUMBER);
PROCEDURE P_DECIDE_FUEL_PRICE (P_FUEL_PRICE_ID IN NUMBER, P_DECISION IN VARCHAR2 /* ACTIVATE / REJECT */);
PROCEDURE P_SAVE_FORMULA      (P_REC IN HRD_TRANSPORT_FORMULA_MST%ROWTYPE, P_FORMULA_ID OUT NUMBER);
PROCEDURE P_DECIDE_FORMULA    (P_FORMULA_ID IN NUMBER, P_DECISION IN VARCHAR2);
FUNCTION  F_PREVIEW_TRIP_COST (P_FORMULA_ID IN NUMBER, P_FUEL_PRICE IN NUMBER) RETURN NUMBER;
```
- **Save:** validate (price > 0; formula preview > 0, otherwise -20711, FR-009 AC3). An effective date inside a CLOSED or SENT period raises -20704 "Payroll month closed" (FR-008 AC3). Insert as PENDING with MAKER_BY = current user.
- **Decide:** the current user must differ from MAKER_BY, otherwise -20703 "Maker and checker must be different users". ACTIVATE sets ACTIVE and retires the formula it replaces. Every decision is written to the audit log.
- **Late price (Q-16):** if an activated fuel price has EFFECTIVE_FROM in the past and LATE_PRICE_MODE = RECALCULATE, re-price the VALID and RATE_MISSING trips of OPEN periods from that time, and post an updated notification to affected employees.

## 6.5 DS-04 Eligibility and exemptions (satisfies FR-001, FR-014) [NEW]
```sql
PROCEDURE P_SET_ELIGIBILITY (P_EMPLOYEE_ID IN NUMBER, P_FROM IN DATE, P_TO IN DATE, P_BUS_MANDATORY IN VARCHAR2, P_REMARKS IN VARCHAR2);
PROCEDURE P_SET_EXEMPTION   (P_EMPLOYEE_ID IN NUMBER, P_FROM IN DATE, P_TO IN DATE, P_REASON_CODE IN VARCHAR2, P_REMARKS IN VARCHAR2);
FUNCTION  F_IS_ELIGIBLE     (P_EMPLOYEE_ID IN NUMBER, P_ON IN DATE) RETURN VARCHAR2;  -- Y/N
```
An overlapping eligibility period raises -20710 "Eligibility periods overlap". Both procedures write to the audit log.

## 6.5a DS-14 Non-swipe report (satisfies FR-014, BR-04) [NEW]
```sql
TYPE R_NONSWIPE IS RECORD (EMPLOYEE_ID NUMBER, ISSUE_DATE DATE, ISSUE_TYPE VARCHAR2(20), DETAIL VARCHAR2(200));
TYPE T_NONSWIPE_LIST IS TABLE OF R_NONSWIPE;
FUNCTION F_NONSWIPE_REPORT (P_PERIOD_CODE IN VARCHAR2, P_MIN_TRIPS IN NUMBER DEFAULT NULL)
RETURN T_NONSWIPE_LIST PIPELINED;
```
For each employee eligible in the period with BUS_MANDATORY = Y:
1. **PRESENT_NO_TRIP:** each day with `F_IS_PRESENT = 'Y'`, no VALID, INCOMPLETE or MANUAL trip and no open adjustment request. Days covered by an exemption (FR-014 AC3) or by approved leave are skipped.
2. **INCOMPLETE_TRIP:** each INCOMPLETE trip.
3. **LOW_MONTHLY_TRIPS:** fewer VALID trips than P_MIN_TRIPS (page parameter, so the threshold stays configurable).

Employees who aren't eligible are never listed (FR-014 AC2). The day-by-day walk is fine for an on-demand report (about 30,000 attendance lookups per 1,000 employees). Once the attendance table is known, rewrite it as one set-based query.

## 6.6 DS-08 Adjustments (satisfies FR-011, FR-012, FR-013, RULE-05) [NEW]
```sql
PROCEDURE P_SUBMIT_ADJUSTMENT (P_TRIP_DATE IN DATE, P_TRIP_DIRECTION IN VARCHAR2, P_REASON IN VARCHAR2, P_ADJ_REQUEST_ID OUT NUMBER);
PROCEDURE P_DECIDE_ADJUSTMENT (P_ADJ_REQUEST_ID IN NUMBER, P_ROW_VERSION IN NUMBER, P_DECISION IN VARCHAR2, P_COMMENT IN VARCHAR2);
PROCEDURE P_ESCALATE_ADJUSTMENTS;  -- job
```
**Submit** (the employee comes from the APEX session, never a page item):
1. Reject a non-eligible employee (-20710).
2. Reject a date outside ADJ_WINDOW_DAYS if it is set (-20707, FR-011 AC3).
3. Reject if a non-reversed trip exists for that date and direction (-20706 "Trip already recorded", FR-011 AC2), or if an open request exists (unique index).
4. Assign the approver by ROUTING_MODE: SUPERVISOR → `F_GET_SUPERVISOR`, falling back to the coordinator and flagging HR (FR-012 AC2); COORDINATOR → the coordinator; BOTH_FIRST_WINS → supervisor as assignee, and the coordinator sees the request too.
5. Notify the approver (ADJ_PENDING).

**Decide:**
1. The approver must not be the requester (-20708, FR-013 AC2).
2. Update the request only if `ROW_VERSION = P_ROW_VERSION` and the status is SUBMITTED or ESCALATED. Zero rows updated means someone else decided first: -20709 "Already decided by [name]" (FR-013 AC4).
3. APPROVED → insert a MANUAL trip priced by `F_CALC_TRIP_COST` at the trip date (06:00 for KDC_TO_HOSP, 18:00 for HOSP_TO_KDC, until shift times are known), in the period rule of §6.2 step 7.
4. Notify the employee (ADJ_DECISION) and write the audit log.

**Escalate** (daily 07:00): requests in SUBMITTED for more than ESCALATION_DAYS working days, or whose approver `F_IS_ON_LEAVE` today, move to ESCALATED with the coordinator as approver. Both parties are notified (FR-012 AC3).

## 6.7 DS-09 / DS-10 Period close and payroll (satisfies FR-002, FR-010, FR-018, RULE-01, RULE-03) [NEW]
```sql
PROCEDURE P_CLOSE_PERIOD    (P_PERIOD_CODE IN VARCHAR2);
PROCEDURE P_SEND_TO_PAYROLL (P_PERIOD_CODE IN VARCHAR2);
PROCEDURE P_REOPEN_PERIOD   (P_PERIOD_CODE IN VARCHAR2, P_REASON IN VARCHAR2);
```
**Close** (Finance role; status OPEN or REOPENED):
1. Run `P_DERIVE_TRIPS` up to the period end + 1 day, so no swipe is left unprocessed.
2. For each employee eligible on any day of the period, using the policy active at the period start:
   - ELIGIBLE_DAYS from the eligibility periods; WORKING_DAYS = Monday–Saturday days in the period, or the hospital calendar if one exists (A-D1).
   - Allowance by PRORATION_MODE:
     - NONE: full amount if eligible all month, otherwise the calculation stops with -20713 "Proration rule not configured" (FR-002 AC3);
     - CALENDAR_DAYS: amount × eligible days ÷ days in month;
     - WORKING_DAYS: amount × eligible working days ÷ WORKING_DAYS.
   - SETTLEMENT_MODE = SCALE_ALLOWANCE: allowance = amount ÷ ALLOWANCE_BASE_DAYS × eligible working days (Q-07 b).
   - SETTLEMENT_MODE = DERIVE_TRIP_COST: re-price every VALID trip of the period at allowance ÷ (2 × WORKING_DAYS) (Q-07 c).
   - TOTAL_DEDUCTION = sum of VALID trip deductions. PRIOR_PERIOD_CORRECTION = sum of MANUAL trips for earlier sent periods.
   - Gross = allowance − TOTAL_DEDUCTION − PRIOR_PERIOD_CORRECTION. EXCESS_AMOUNT = GREATEST(−gross, 0).
   - PAYOUT_AMOUNT = GREATEST(gross, 0), or gross when the mode is RECOVER_EXCESS. FINANCE_REVIEW_FLAG = Y when EXCESS_AMOUNT > 0 (FR-010 AC3).
3. MERGE into the monthly table (re-runnable while not SENT). Status → CLOSED.
4. INCOMPLETE or RATE_MISSING trips in the period block the close with -20715, listing the counts, until HR or Finance resolves them.

**Send:** status must be CLOSED. Status → SENT. The rows appear in `VW_TRANSPORT_PAYROLL_EXPORT`. Regeneration is blocked (-20712, FR-018 AC2).

**Reopen:** Finance only, with a reason. SENT → REOPENED, and the action is audited.

## 6.8 DS-05 Adapter functions (satisfies FR-004, FR-012, FR-014, NFR-INT-01) [NEW, source PROVISIONAL]
```sql
FUNCTION F_GET_EMPLOYEE_BY_CARD (P_CARD_NO IN VARCHAR2, P_CARD_STATUS OUT VARCHAR2) RETURN NUMBER;
FUNCTION F_IS_PRESENT           (P_EMPLOYEE_ID IN NUMBER, P_ON IN DATE) RETURN VARCHAR2;
FUNCTION F_IS_ON_LEAVE          (P_EMPLOYEE_ID IN NUMBER, P_ON IN DATE) RETURN VARCHAR2;
FUNCTION F_GET_SUPERVISOR       (P_EMPLOYEE_ID IN NUMBER) RETURN NUMBER;
FUNCTION F_GET_COORDINATOR      RETURN NUMBER;
FUNCTION F_GET_CURRENT_EMPLOYEE RETURN NUMBER;  -- from APEX APP_USER
```
Each one reads a single existing object, still to be named (§4.1). They are the **only** code that touches existing tables. Until the schema is indexed, the developer builds them against the names IS confirms (Q-09). They return NULL/'N' rather than failing when data is missing.

## 6.9 DS-13 / DS-18 Reversal and purge [NEW]
```sql
PROCEDURE P_REVERSE_SWIPE (P_SWIPE_ID IN NUMBER, P_REASON IN VARCHAR2);
PROCEDURE P_REVERSE_TRIP  (P_TRIP_ID IN NUMBER, P_REASON IN VARCHAR2);
PROCEDURE P_PURGE_SWIPE_DETAIL (P_OLDER_THAN_MONTHS IN NUMBER);  -- NFR-DAT-01, disabled until Q-18
PROCEDURE P_SAVE_TERMINAL (P_REC IN HRD_TRANSPORT_TERMINAL_MST%ROWTYPE, P_TERMINAL_ID OUT NUMBER);  -- FR-005, IS admin only
```
Reversal is allowed only in OPEN periods (-20704 otherwise) and is audited. Purge is not scheduled until Finance and HR set the retention period.

## 6.10 Error codes
| Code | Condition | Message |
|---|---|---|
| -20701 | Terminal unknown or inactive | Unknown or inactive terminal |
| -20702 | No active policy for the date | No active transport policy |
| -20703 | Maker = checker | Maker and checker must be different users |
| -20704 | Change in a closed/sent period | Payroll month closed |
| -20706 | Adjustment for an existing trip | Trip already recorded |
| -20707 | Adjustment outside window | Request must be submitted within [n] days |
| -20708 | Approver is requester | You cannot approve your own request |
| -20709 | Request already decided | Already decided by [name] |
| -20710 | Not eligible / overlapping eligibility | Not enrolled in the transport allowance / Eligibility periods overlap |
| -20711 | Formula gives zero or negative cost | Formula produces an invalid trip cost |
| -20712 | Register already sent | Register already sent to payroll; reopen the month first |
| -20713 | Partial month with proration NONE | Proration rule not configured |
| -20714 | Missing role for the action | You are not authorised for this action |
| -20715 | Unresolved trips at close | [n] incomplete and [m] rate-missing trips must be resolved |
| -20720 / -20721 | DELETE on swipes/trips | Cannot be deleted; reverse instead |

# 7. APEX design
Application: the existing HR application, ID TBC (Q-20). Pages 700–799 are reserved. Theme: Universal Theme, responsive (NFR-USA-01). Every page has an authorization scheme; every process calls the package.

| Page | Name | Main components (static IDs) | Package calls | Authorization |
|---|---|---|---|---|
| 710 | Fuel prices | REG_FUEL_PRICES (IR), REG_PENDING; items P710_PRICE, P710_EFFECTIVE_FROM, P710_REMARKS; BTN_SAVE, BTN_ACTIVATE, BTN_REJECT | P_SAVE_FUEL_PRICE, P_DECIDE_FUEL_PRICE | AUTH_TRANSPORT_FINANCE (HR: save only) |
| 720 | Transport policy | REG_POLICY_VERSIONS, REG_POLICY_FORM, REG_PREVIEW (worked example, FR-009 AC2); LOVs LOV_SETTLEMENT_MODE, LOV_PRORATION_MODE, LOV_DIRECTION_MODE, LOV_ROUTING_MODE; BTN_SAVE, BTN_ACTIVATE, BTN_REJECT; DA_REFRESH_PREVIEW | P_SAVE_FORMULA, P_DECIDE_FORMULA, F_PREVIEW_TRIP_COST | AUTH_TRANSPORT_FINANCE |
| 730 | Eligibility and exemptions | REG_ELIGIBILITY, REG_EXEMPTIONS (IG); LOV_EMPLOYEE, LOV_EXEMPT_REASON | P_SET_ELIGIBILITY, P_SET_EXEMPTION | AUTH_TRANSPORT_HR |
| 740 | Terminals | REG_TERMINALS (IG, LAST_SEEN_ON highlighted after 30 min) | P_SAVE_TERMINAL | AUTH_TRANSPORT_ADMIN |
| 750 | My transport | REG_MONTH_SUMMARY (cards: trips, deductions, estimated payout labelled "estimate"), REG_MY_TRIPS, REG_MY_REQUESTS, REG_NOTIFICATIONS; BTN_REQUEST_ADJUSTMENT | VW_TRANSPORT_MY_TRIPS | AUTH_TRANSPORT_EMPLOYEE |
| 755 | Request adjustment (modal) | P755_TRIP_DATE, P755_TRIP_DIRECTION, P755_REASON; BTN_SUBMIT. 3 fields, 1 click (NFR-USA-01) | P_SUBMIT_ADJUSTMENT | AUTH_TRANSPORT_EMPLOYEE |
| 760 | Adjustment approvals | REG_PENDING_REQUESTS (IR with row version hidden); BTN_APPROVE, BTN_REJECT; P760_COMMENT | P_DECIDE_ADJUSTMENT | AUTH_TRANSPORT_APPROVER |
| 770 | Transaction trail | REG_TRAIL (IR, export CSV/XLSX), REG_AUDIT | VW_TRANSPORT_TRAIL, audit log | AUTH_TRANSPORT_HR or AUTH_TRANSPORT_FINANCE |
| 780 | Non-swipe report | REG_NONSWIPE (IR); P780_PERIOD; excludes exempted days | F_IS_PRESENT, exemptions (DS-14) | AUTH_TRANSPORT_HR or AUTH_TRANSPORT_COORDINATOR |
| 790 | Monthly register | REG_PERIODS, REG_REGISTER (IR with FINANCE_REVIEW_FLAG filter); BTN_CLOSE_PERIOD, BTN_SEND_TO_PAYROLL, BTN_REOPEN | P_CLOSE_PERIOD, P_SEND_TO_PAYROLL, P_REOPEN_PERIOD | AUTH_TRANSPORT_FINANCE |

Session state protection is on for every item carrying an ID. The employee is always taken from the session (`F_GET_CURRENT_EMPLOYEE`), never from a page item. This closes the tampering risk seen with `P20_EMP_ID` in the demo schema.

# 8. Integrations, jobs and notifications
| DS | Name | Type | Trigger / schedule | Logic | Failure handling |
|---|---|---|---|---|---|
| DS-05 | ORDS `POST /hrd/transport/v1/swipes` | REST (terminals → HRD) | Each swipe; batches of up to 500 for offline replay | Calls P_RECORD_SWIPE per item; returns per-item result | Terminal retries until accepted; duplicates are ignored (SOURCE_REF). OAuth2 client credentials per terminal vendor |
| DS-05 | ORDS `POST /hrd/transport/v1/heartbeat` | REST | Every 5 minutes per terminal | Updates LAST_SEEN_ON | None needed |
| DS-16 | TRANSPORT_DERIVE_TRIPS_JOB | DBMS_SCHEDULER | Every 15 minutes | P_DERIVE_TRIPS | Error logged; next run picks up the same swipes |
| DS-16 | TRANSPORT_ESCALATE_JOB | DBMS_SCHEDULER | Daily 07:00 | P_ESCALATE_ADJUSTMENTS | Error logged; re-runnable |
| DS-16 | TRANSPORT_TERMINAL_HEALTH_JOB | DBMS_SCHEDULER | Every 15 minutes | Terminals active with LAST_SEEN_ON over 30 minutes old → TERMINAL_OFFLINE alert to TRANSPORT_COORDINATOR and IS roles (once per outage) | None needed |
| DS-10 | VW_TRANSPORT_PAYROLL_EXPORT | View read by payroll | Monthly, after SENT | Employee, period, payout | Payroll confirms the import manually (TBC) |
| DS-11 | Dashboard notifications | Table read by the dashboard | Real time | Unread rows for the employee | Dashboard integration TBC (Q-13). Page 750 shows them in the meantime |

Job names aren't covered by the HRD standards; the `MODULE_PURPOSE_JOB` pattern is proposed.

# 9. Security and audit design
- **Authorization schemes (DS-15):** AUTH_TRANSPORT_EMPLOYEE (any enrolled employee), AUTH_TRANSPORT_APPROVER (has pending requests assigned, or is a coordinator), AUTH_TRANSPORT_COORDINATOR, AUTH_TRANSPORT_HR, AUTH_TRANSPORT_FINANCE, AUTH_TRANSPORT_ADMIN (IS). The role source is TBC (APEX ACL or existing HR role tables, Q-21). They follow the SRS §7.3 access matrix.
- **Row filtering:** `VW_TRANSPORT_MY_TRIPS` filters by `F_GET_CURRENT_EMPLOYEE`. Approver pages filter by APPROVER_ID, plus all requests for coordinators. The package re-checks the role on every write (-20714).
- **Segregation of duties:** maker ≠ checker for price and policy (check constraint and procedure check). Requester ≠ approver for adjustments.
- **Audit:** the audit log records who, when, and old and new JSON for price, policy, eligibility, exemption, adjustment decisions, reversals and period close, send and reopen. Swipes and trips can't be deleted.
- **Privacy:** swipe data shows employee movements. Only the employee, HR, Finance and the coordinator see it. Retention is set by DS-18 once Q-18 is answered.
- **ORDS:** OAuth2 client credentials, one client per terminal vendor. HTTPS only. The endpoint accepts only terminal codes registered in DS-03.

# 10. Non-functional design
| NFR | Design measure | How it will be verified |
|---|---|---|
| NFR-PERF-01 | DS-05/DS-11: notification inserted in the same call as the swipe | Swipe → dashboard in under 60 s (test with a terminal simulator) |
| NFR-PERF-02 | DS-05: 2 indexed reads + 2 inserts; ORDS budget under 300 ms | Load test: 50 swipes/second for 5 minutes, 95th percentile under 1 s end to end |
| NFR-AVL-01 | DS-05: SOURCE_REF idempotency; SWIPE_TIME from the device | Replay the same batch twice: row count unchanged; delayed batch keeps its original times |
| NFR-SEC-01 | DS-15: schemes and filtered views | Negative tests: another employee's trips, direct page URL without role |
| NFR-SEC-02 | DS-01/DS-02: check constraint and procedure check | The same user can't activate their own entry |
| NFR-AUD-01 | DS-13: audit log, delete triggers | DELETE raises -20720; every change has an audit row |
| NFR-DAT-01 | DS-18: purge procedure, unscheduled | Enabled after Q-18 |
| NFR-CMP-01 | DS-07/DS-09: whole-rupee rounding | Unit tests on the formula |
| NFR-INT-01 | DS-05: card lookup through the existing card data | Cards that work in the cafeteria resolve to the same employee |
| NFR-USA-01 | DS-17: responsive pages; 3-field modal | UAT on a phone browser |
| NFR-OPS-01 | DS-03/DS-16: LAST_SEEN_ON and health job | Unplug a terminal: alert within 30 minutes |

# 11. Change inventory
| # | File / object | Path in repo | Change type | DS | Owner |
|---|---|---|---|---|---|
| 1 | 12 sequences, 12 tables, indexes, comments, 2 triggers | db/CR-YYYY-XXX/01_ddl/CR-YYYY-XXX_01_ddl.sql | New | DS-01–DS-13 | DB |
| 2 | Seed: terminals, period 2026-11, policy v1 and first fuel price (PENDING) | db/CR-YYYY-XXX/02_data/CR-YYYY-XXX_02_seed.sql | New | DS-01–DS-03, DS-09 | DB |
| 3 | VW_TRANSPORT_MY_TRIPS, VW_TRANSPORT_TRAIL, VW_TRANSPORT_PAYROLL_EXPORT | db/CR-YYYY-XXX/03_code/VW_TRANSPORT_*.sql | New | DS-10, DS-12, DS-13 | DB |
| 4 | HRD.PKG_TRANSPORT_ALLOWANCE spec | db/CR-YYYY-XXX/03_code/PKG_TRANSPORT_ALLOWANCE.pks | New | DS-01–DS-18 | DB |
| 5 | HRD.PKG_TRANSPORT_ALLOWANCE body | db/CR-YYYY-XXX/03_code/PKG_TRANSPORT_ALLOWANCE.pkb | New | DS-01–DS-18 | DB |
| 6 | Adapter functions against existing card, attendance, leave and supervisor data | Inside #5 | New (**verify against schema**) | DS-05, DS-08, DS-14 | DB |
| 7 | Grants (APEX parsing schema, ORDS, payroll user, dashboard) | db/CR-YYYY-XXX/04_security/CR-YYYY-XXX_04_grants.sql | New | DS-15 | DB/DBA |
| 8 | ORDS module hrd/transport/v1 (swipes, heartbeat) and OAuth client | db/CR-YYYY-XXX/04_security/CR-YYYY-XXX_05_ords.sql | New | DS-05 | DB/Integration |
| 9 | 3 scheduler jobs | db/CR-YYYY-XXX/05_jobs/CR-YYYY-XXX_06_jobs.sql | New | DS-16 | DB |
| 10 | APEX pages 710–790, 6 authorization schemes, 4 LOVs, navigation entries | apex/[app id]/ (split export) | New | DS-15, DS-17 | APEX |
| 11 | Dashboard notification widget | Dashboard app (TBC) | Modify (**verify**) | DS-11 | APEX |
| 12 | Payroll import mapping for the transport payout | Payroll system (TBC) | Modify (**verify**) | DS-10 | Integration |
| 13 | Unit tests | db/CR-YYYY-XXX/90_tests/ | New | All | DB |
| 14 | Rollback | db/CR-YYYY-XXX/99_rollback/CR-YYYY-XXX_99_rollback.sql | New | All | DB |
| 15 | Employee FKs on EMPLOYEE_ID columns | db/CR-YYYY-XXX/01_ddl/ (follow-up) | New (**after schema confirmed**) | DS-04–DS-09 | DB |

# 12. Deployment plan
## 12.1 Script execution order
| Step | Script | Content | Downtime needed |
|---|---|---|---|
| 1 | CR-YYYY-XXX_01_ddl.sql | Sequences, tables, indexes, triggers | No: new objects only |
| 2 | CR-YYYY-XXX_02_seed.sql | Terminals, period, PENDING policy and price | No |
| 3 | VW_TRANSPORT_*.sql | Views | No |
| 4 | PKG_TRANSPORT_ALLOWANCE.pks, .pkb | Package | No |
| 5 | CR-YYYY-XXX_04_grants.sql | Grants | No |
| 6 | CR-YYYY-XXX_05_ords.sql | REST module, OAuth client | No |
| 7 | APEX import | Pages 710–790 | No (import into the running app; brief page cache refresh) |
| 8 | CR-YYYY-XXX_06_jobs.sql | Jobs (created DISABLED) | No |
| 9 | Manual | Finance activates the policy and fuel price (maker-checker); HR loads eligibility; IS enables the jobs; vendor points the terminals at the endpoint | No |

## 12.2 Post-deployment verification
- The verification query at the end of 01_ddl.sql lists 12 tables, 12 sequences and 2 triggers, all VALID.
- `SELECT OBJECT_NAME, STATUS FROM ALL_OBJECTS WHERE OWNER='HRD' AND OBJECT_NAME='PKG_TRANSPORT_ALLOWANCE'` returns VALID for both spec and body.
- A test swipe from the terminal simulator appears in `HRD_TRANSPORT_SWIPE_TRN` with a notification. After the job runs, a trip exists with a deduction.
- All three jobs are enabled and their last run shows SUCCEEDED.

## 12.3 Rollback plan
In reverse order:
1. Disable and drop the jobs.
2. Drop the ORDS module and OAuth client.
3. Delete APEX pages 710–790 and their schemes and LOVs.
4. Revoke the grants.
5. Drop the package and views.
6. Run `CR-YYYY-XXX_99_rollback.sql` (triggers, tables, sequences).

**Data safety:** step 6 destroys all transport data. Before go-live that is fine. After go-live, stop at step 1–3 (disable jobs, block the endpoint, hide the pages) and keep the data for payroll audit.

# 13. Testing notes for developers and QA
- **Unit-test each setting combination that matters:** SETTLEMENT_MODE × 4, PRORATION_MODE × 3, DIRECTION_MODE × 2, SINGLE_SWIPE_RULE × 2. A pairwise set of about 12 cases is enough.
- **Month arithmetic:** November 2026 has 25 Monday–Saturday days and December 2026 has 27. Check that CAP_ZERO gives 0 and a Finance review flag for a full-use employee, and that SCALE_ALLOWANCE gives 25,000 and 27,000 allowances.
- **Swipe edge cases:** replay of the same batch; out-of-order arrival of offline swipes; a swipe exactly at the repeat-window boundary; a night shift crossing midnight (trip date = start date); the last day of the month.
- **Concurrency:** two approvers deciding the same request (one gets -20709); the job running while Finance closes the period (close runs derivation first, and the job skips CLOSED periods).
- **Security:** direct URL to pages without the role; changing P755 items in the browser; maker = checker.
- QA writes the functional test cases from the SRS (`skmch-qa-testcases`). These notes don't replace them.

# 14. Risks, assumptions and open questions
## 14.1 Risks
| Risk | Impact | Mitigation |
|---|---|---|
| Blocking questions answered late or not at all | Wrong settings at go-live | Defaults in §14.3 are the MoM's literal reading; Finance reviews the settings before activation |
| Existing card, attendance, leave and payroll objects differ from assumptions | Adapter rework | All access isolated in 6 adapter functions (KD-02); schema indexing is the first task |
| Terminal vendor can't call REST | Swipe capture blocked | Fallback: vendor writes to a staging table and a job calls P_RECORD_SWIPE (Q-19) |
| Many settings increase the test effort | Schedule | Pairwise testing (§13); only the chosen combination needs full UAT |
| Build window (about 4 weeks) | Late delivery | Phase as proposed in the SRS: capture, notifications and adjustments first; settlement before the November cut-off |

## 14.2 Assumptions
| ID | Assumption |
|---|---|
| A-D1 | Working days are Monday–Saturday unless a hospital calendar exists in the schema |
| A-D2 | ORDS is available on the HRD database for REST endpoints |
| A-D3 | Terminals can send a unique reference per swipe and buffer swipes offline |
| A-D4 | APEX is the frontend for HR, Finance and employee pages, in the existing HR application |
| A-D5 | Manual trips are timed 06:00 (to hospital) and 18:00 (from hospital) for fuel price lookup until shift times are known |

## 14.3 Open questions
Settings for SRS questions. The default is what the seed script loads as PENDING; Finance changes it before activating.

| ID | Question | Handled by | Default in seed | Owner | Blocking for build? |
|---|---|---|---|---|---|
| Q-02 | Per trip or per swipe; single swipes | DEDUCTION_BASIS, SINGLE_SWIPE_RULE | PER_TRIP, REVIEW | Mr. Ubaid, Finance | No |
| Q-03 | Eligibility; bus mandatory | Eligibility table, BUS_MANDATORY | Y | Mr. Ubaid, HR | No (data) |
| Q-04 | Proration | PRORATION_MODE | WORKING_DAYS | HR, Finance | No |
| Q-05 | Formula | FORMULA_TYPE, BASE_TRIP_COST, REF_FUEL_PRICE | FUEL_INDEXED, 500, current price | Finance | No |
| Q-07 | Deductions above the allowance | SETTLEMENT_MODE | CAP_ZERO | Finance, Mr. Ubaid | No |
| Q-09 | Card, attendance, leave and payroll systems | Adapter functions | None | IS | **Yes**: adapters can't be finished without names |
| Q-10 | Adjustment window | ADJ_WINDOW_DAYS | NULL (no limit) | HR | No |
| Q-11 | Approver routing | ROUTING_MODE | SUPERVISOR | Mr. Ubaid, HR | No |
| Q-14 | First month, cut-off | PAYROLL_CUTOFF_DAY, period 2026-11 | NULL | Finance | No |
| Q-15 | Direction detection | DIRECTION_MODE, TERMINAL_DIRECTION | SEQUENCE | Mr. Ubaid, IS | **Yes for hardware**: one or two readers per location |
| Q-16 | Late fuel price | LATE_PRICE_MODE | RECALCULATE | Finance | No |
| Q-17 | Shifts without bus | Exemption table | None | Mr. Ubaid, Nursing, HR | No (data) |
| Q-18 | Retention | Purge procedure, unscheduled | Not scheduled | HR, Finance | No |

New design questions:
| ID | Question | Owner | Blocking |
|---|---|---|---|
| Q-19 | Can the RFID terminals call a REST endpoint with OAuth2 and send a unique reference per swipe, or do they need a staging-table integration? | IS, vendor | Yes, for DS-05 |
| Q-20 | Which APEX application (ID) hosts pages 710–790, and is the employee dashboard in APEX? | IS | No |
| Q-21 | Where do the HR, Finance, coordinator and admin roles come from (APEX ACL, existing role tables, AD groups)? | IS | No |
| Q-22 | How many Karachi staff will be enrolled (for sizing and load tests)? | HR | No |

# Appendix A. Full DDL script
File: `CR-YYYY-XXX_01_ddl.sql`

```sql
@@DDL@@
```

# Appendix B. Rollback script
File: `CR-YYYY-XXX_99_rollback.sql`

```sql
@@ROLLBACK@@
```
