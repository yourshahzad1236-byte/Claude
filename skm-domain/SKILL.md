---
name: skm-domain
description: Domain knowledge of the SKM hospital information system (HIS) Oracle database — the DEFINITIONS (master/setup data, CPT/services, locations, departments, beds, clinical setups, system objects), PAYROLL (salary processing, allowances/deductions, income tax, provident fund, loans, expense claims, GL vouchers) and RFID (card/biometric attendance and access-control machines) schemas, plus their links to HRD, FINANCE, REGISTRATION, BILLING and SECURITY. Use whenever writing, reviewing or explaining SQL, PL/SQL, Oracle Forms or APEX code, reports, or data fixes that touch these schemas; when asked which table holds some data, how tables join, what a column/flag means, or which package already implements a calculation.
---

# SKM HIS database — domain skill

The database is the Oracle back end of the SKM hospital information system (a
multi-organization, multi-location cancer-care hospital network; `LOCATION.CC_TYPE`
mentions "Shaukat Khanum Collection Centre"). One application schema per module;
this skill covers three of them in detail:

| Schema | Tables | What it holds | Reference |
|---|---|---|---|
| `DEFINITIONS` | 1070 | Shared master/setup data used by every module: organizations, zones, locations, departments/sections, designations, CPT (billable services/tests) and prices, patient types, doctors, clinics, beds/rooms, ICD/cancer groups, chemo/BMT setups, system constants, application objects/menus, sync metadata | `references/DEFINITIONS.md` |
| `PAYROLL` | 183 | Monthly salary processing, allowances/deductions, arrears, increments, income tax, provident fund (PF), loans, expense claims/awards, GL/PF voucher generation | `references/PAYROLL.md` |
| `RFID` | 43 | RFID-card / biometric attendance machines, card issuance, machine access rights, raw check-in/out data | `references/RFID.md` |

Full human-readable data dictionaries (every column, constraint, index, view SQL,
package signature, trigger, synonym) are in the repo at `docs/schema/<SCHEMA>.md`.

Other schemas are referenced but **not documented here** — don't invent their
columns; ask for the DDL: `HRD` (employee master — the HRD export received was empty),
`FINANCE` (GL), `REGISTRATION` (patients, clinics), `BILLING`, `SECURITY` (users,
terminals), `HIS`, `DIAGNOSTIC`, `DI` (error logging), `ORDERENTRY`, `PHARMACY`,
`ITEM`, `PARTY`, `RADIOLOGY`, `ICU`, `LOB`, `MMS`, `CBR`.

## How to use the references

The reference files are large. **Never read them whole — grep them.**

```bash
# a table's definition (columns, FKs, unique keys, checks)
grep -n -A4 '^## PAY_MASTER\b' references/PAYROLL.md
# which tables have a column
grep -n 'AD_CODE CHAR' references/PAYROLL.md | cut -c1-120
# who references a table
grep -n '→ DEFINITIONS.CPT(' references/*.md
# tables by topic/prefix
grep -n '^## CHEMO_' references/DEFINITIONS.md
# a package's public API
grep -n '^- PKG_ITAX\b' references/PAYROLL.md
```

Compact format: `*` PK column, `!` NOT NULL, `«…»` column comment,
`[+audit]` / `[+ml]` = standard columns (below) present but omitted,
`fk … [disabled]` = relationship is logical only.
For full signatures or view SQL, grep `docs/schema/<SCHEMA>.md` (`### NAME` headings).

## Core identifiers and joins

| Concept | Key | Notes |
|---|---|---|
| Person (employee **and** patient) | `MRNO VARCHAR2(14)` | Medical record no. is also the employee number. Employee master is `HRD.INFORMATION(MRNO)`; patients are in `REGISTRATION.PATIENT`. Columns such as `DEPARTMENT_HEAD`, `SUPERVISED_BY`, `OBSOLETED_BY` also hold an MRNO. |
| Organization | `ORGANIZATION_ID VARCHAR2(3)` | `DEFINITIONS.ORGANIZATION` |
| Zone | `ZONE_ID VARCHAR2(3)` | `DEFINITIONS.ZONES` (unique `ORGANIZATION_ID, ZONE_ID`) |
| Location / site | `LOCATION_ID VARCHAR2(3)` | `DEFINITIONS.LOCATION` — the most-referenced table. Sub-locations resolve via `DEFINITIONS.PKG_COMMON.GET_PARENT_LOCATION_ID`. |
| Department / section | `DEPARTMENT_ID VARCHAR2(7)`, `SECTION_ID` | `DEFINITIONS.DEPARTMENT`, `DEPARTMENT_SECTION` |
| Designation | `DESIGNATION_ID VARCHAR2(6)` | `DEFINITIONS.DESIGNATION` (self-parent `PARENT_DESIGNATION_ID`; `EMPLOYEE_NATURE` O/C/D/N) |
| Service / test / procedure | `CPT_ID VARCHAR2(18)` | `DEFINITIONS.CPT` + `CPT_CATEGORY`, price/costing history tables |
| Patient category | `PATIENT_TYPE_ID VARCHAR2(6)` | `DEFINITIONS.PATIENT_TYPE` (flags: discount/refund/employee/salary allowed…) |
| Payroll month | `(START_DATE, END_DATE)` | `DEFINITIONS.MONTHS` — composite key used everywhere in PAYROLL; flags `CURRENT_MONTH`, `NEXT_MONTH`, `MONTH_CLOSED`, `PAY_PROCESS` |
| Financial / tax year | `YEAR_CODE NUMBER(4)` | `PAYROLL.PAY_FINANCIAL_YEAR` (`CURRENT_YEAR='Y'`, `YEAR_STATUS` O/C/S) |
| GL voucher | `(VOUCHER_TYPE, VOUCHER_NO)` | `FINANCE.GL_TRAN_MASTER`; accounts in `FINANCE.GL_COA`, `GL_SUB_LEDGERS` |
| Allowance/deduction | `AD_CODE CHAR(3)` | `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (PK `AD_CODE, ORGANIZATION_ID, LOCATION_ID`; `AD_TYPE` A/D) |
| RFID machine | `MACHINE_ID VARCHAR2(5)` | `RFID.RFID_MACHINES` |

Codes are short `VARCHAR2`/`CHAR` strings, not numbers — keep leading zeros
(`AD_CODE IN ('007','043')`) and compare as strings.

## Conventions every table follows

**Audit columns** (1,149 of 1,296 tables) — filled by triggers, never by application code:

| Column | Set by | Meaning |
|---|---|---|
| `ORIGINAL_USER_ID`, `ORIGINAL_TERMINAL`, `ORIGINAL_TRN_DATE` | `<TABLE>_INS` (BEFORE INSERT) | who/where/when created |
| `USER_ID`, `TERMINAL`, `TRN_DATE` | `<TABLE>_UPD` (BEFORE UPDATE) | last modified |

**Multi-location columns** `ORG_ID`, `ZON_ID`, `LOC_ID`, `WS_SYNC_DATE`: where the
row was first created and when it was synced — not the business location. For
business filtering use `ORGANIZATION_ID` / `LOCATION_ID`.

**Flags** are `CHAR(1)` `'Y'/'N'` (`ACTIVE`, `DEFAULTS`, `POSTED`, `CANCELLED` …).
Filter active master data with `ACTIVE = 'Y'`. Check constraints document allowed
values — grep `check:` in the reference.

**Standard trigger set per table** (suffix → purpose):

| Suffix | Timing | Purpose |
|---|---|---|
| `_INS` | BEFORE INSERT | stamp `ORIGINAL_*` audit columns |
| `_UPD` | BEFORE UPDATE | stamp `USER_ID/TERMINAL/TRN_DATE`, copy `:OLD` row to audit schema with `TRN_STATUS='UPD'` |
| `_DEL` | AFTER DELETE | copy `:OLD` row to audit schema with `TRN_STATUS='DEL'` |
| `_CEA` | BEFORE I/U/D | distributed-environment guard: blocks DML on the wrong site (CR vs DC) based on `DEFINITIONS.TABLES.MODEL_TYPE_ID` and network topology (STAR/MESH) |
| `_Q` | AFTER I/U/D | queues the DML for replication to other locations (data-sync queue) |

All of them start with `IF SECURITY.F_WS_USER() THEN RETURN; END IF;` (the
web-service/sync user bypasses them). User identity comes from
`SECURITY.CurrentUser(SECURITY.GET_TERMINAL)` and `SECURITY.GET_TERMINAL`.

**Audit history**: every audited table has a synonym `SYN_<TABLE>` pointing to the
matching table in the audit schema (`DEF_AUDIT`, `PAYROLLAUDIT`, `RFID_AUDIT`).
To see change history, query `<SCHEMA>.SYN_<TABLE>` (extra columns `NEW_USER_ID`,
`NEW_TERMINAL`, `NEW_TRN_DATE`, `TRN_STATUS`).

**Foreign keys are mostly DISABLED NOVALIDATE**, especially cross-schema ones. The
database will not stop orphan rows, so:
- validate parent existence yourself in PL/SQL before insert;
- use outer joins when reporting across modules;
- treat the `fk:` lines as the documented join paths.

**Tables without a PK** (≈190, many `TEMP_*`, `TMP_*`, `*_R`, `*_TEST`, `*_BACKUP`,
`*_OLD`) are scratch, backup or report-staging tables — don't build new logic on them.

## Object naming (existing code)

- Screen/report packages are named after the application object code:
  `PKG_S<nn><TYPE><nnnnn>` — `S01…` = DEFINITIONS, `S16…` = PAYROLL; `FRM` = Oracle
  Form, `REP` = report, `APX` = APEX page. The object catalogue is
  `DEFINITIONS.OBJECTS` (`SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID`, `OBJECT_CODE`).
- Generic table-API packages `PKG_<TABLE>` expose `F_SELECT / F_INSERT / F_UPDATE /
  F_DELETE / F_LOCK`; form packages expose `QUERY_x / INSERT_x / UPDATE_x /
  DELETE_x / LOCK_x` (Forms/APEX data-block procedures). Follow the same shape
  for new CRUD packages.
- Most packages have a `GET_VERSION` function and a header comment block
  (OBJECTIVE / REVISIONS table).
- Errors are logged with `DI.WEBTASK_ERROR_ENTRY(code, text)` and raised with
  `RAISE_APPLICATION_ERROR(-20007, '~~~' || msg || '~~~')`.
- For new HRD code, also apply the `oracle-plsql-apex-hrd-standards` skill.

## Configuration: system constants

Behaviour switches live in `DEFINITIONS.SYSTEM_CONSTANTS_DEF` /
`SYSTEM_CONSTANTS_SETUP` (per org/location) / `SYSTEM_CONSTANTS_SETUP_USER`.
Read them with the overloaded
`DEFINITIONS.PKG_COMMON.GET_CONSTANT_VALUE(p_constant_id, p_organization_id, p_location_id, …)`
(or `DIAGNOSTIC.F_GET_CONSTANT`) — never hard-code values. Examples seen in code:
173 = distributed environment Y/N, 671 = network topology, 1003 = setup zone.

## Module guide

### PAYROLL — salary processing

Monthly cycle (`DEFINITIONS.MONTHS` row with `CURRENT_MONTH='Y'`):
1. **Setup**: `DEF_ALLOWANCE_DEDUCTION` (A/D codes, formula, taxable, include-in-gross),
   `DEF_AD_GROUP`, `ALLOWANCE_DEDUCTION_SETUP`, `DEF_EMP_FINANCIAL` / `DEF_FINANCIAL_SETUP`
   (employee pay data), pay scales (`PKG_PAYSCALE`), `DEF_INCOME_TAX` slabs, `DEF_LOAN_TYPE`,
   GL mapping `DEF_GL_SETUP_MASTER`.
2. **Inputs**: `ALLOWANCE_DEDUCTION_DETAIL` (per-employee A/D for a period),
   `ARREAR_DETAIL`, attendance (from RFID/HRD), loans (`LOAN_PAYMENT_MASTER` +
   installments), expense claims (`EXPENSE_CLAIM_MASTER`, `EMP_EXPENSE`).
3. **Processing** (`PKG_PAY_PROCESS.CALCULATE_PAYROLL`, `PKG_S16FRM00038`): writes
   `PAY_MASTER` (one row per `MRNO, START_DATE, END_DATE`: working/performed days,
   basic, gross, deductions, net, EOBI/ESSI, PF, tax) and `PAY_ALLOWANCE_DEDUCTION`
   (line items per `AD_CODE`). `*_ON_CARD_SWIPE` columns mean *without* card swipe
   (per the table comment).
4. **Tax**: `PKG_ITAX`, `PAY_ITAX_DETAIL`, `PAY_FINANCIAL_YEAR` (exemptions,
   `CALCULATION_MODE` 1 = allowance based, 2 = gross based).
5. **Vouchers/posting**: `PKG_PAY_VOUCHER`, `PKG_PF_VOUCHER`, `PKG_PROFIT_VOUCHER`,
   `PAY_VOUCHER` (`PAY_VOUCHER_TYPE` GP/PF/CP/GL/LN) → `FINANCE.GL_TRAN_MASTER`.
6. **Close**: `PKG_MONTH` (current/last processed month), `PKG_YEAR_CLOSING`.

Handy readers: `PKG_PAY.GET_GROSS_PAYABLE / GET_NET_PAYABLE / GET_EMP_AD_AMOUNT`,
`PKG_MONTH.FETCH_CURRENT_PAY_MONTH`, `PKG_SALARY_SLIP_EMPLOYEE`, `PKG_SALARY_RECONCILIATION`.
Reuse these instead of re-deriving salary figures.

### RFID — attendance & access control

- `RFID_MACHINES` (device, IP/port, `MACHINE_TYPE` BW/TFT/IFACE, category,
  location) ← `RFID_CATEGORY`, `MACHINE_TYPE`.
- `RFID_CARDS` / `RFID_CARD_TYPE` / card issue (`RFID_CARD_ISSUE_RECORD`, `…_ACS`).
- `RFID_MACHIN_IDENTIFIER_MAPPING`: maps a machine's numeric `MACHINE_IDENTIFIER`
  to `EMPLOYEE_CODE` (= MRNO) per org/location/machine.
- `ATTENDANCE`: raw punches — `CHECK_TIME`, `CHECK_TYPE` (I = in, O = out),
  `USER_ID` (= machine identifier, not the app user!), `MACHINE_ID`,
  `VERIFICATION_MODE` (card/password/biometric). Resolve to employee via the
  mapping table or `RFID.PKG_COMMON.F_GET_EMPLOYEE_CODE`.
- `ATTENDANCE_EMPLOYEE` (resolved to MRNO), `ATTENDANCE_INCORRECT` (rejects).
- Access rights: `MACHINE_WISE_EMPLOYEE`, `DEPT_WISE_DESIG_ACCESS`,
  `SECTION_WISE_ATTENDANCE`; sync with `PKG_RFID_ACCESS_SYNC`.

### DEFINITIONS — master data (main topic prefixes)

`CPT_*` services, pricing, costing, bans, groups · `PATIENT_*` / `PATIENT_TYPE*` ·
`LOCATION*`, `ORDER_LOCATION*`, `ZONES`, `ORGANIZATION`, geography
(`COUNTRY`/`STATE`/`DISTRICT`/`TEHSIL`/`CITY`) · `DEPARTMENT*`, `DESIGNATION*`,
`GL_*` cost-centre structure · `DOCTOR*`, `CLINIC*`, `SPECIALITY_MASTER` ·
`BEDS`, `ROOMS`, `BUILDING_*` · `ICD*`, `ICDO*`, `CANCER_GROUP*`, `DISEASE*` ·
`CHEMO_*`, `BMT_*`, `VACCINATION*`, `CLINICAL_PATHWAY*` · `PACKAGE*` (service packages) ·
`ARMY_*` (armed-forces patient ranks/units) · `AD_*` (Active Directory groups/committees) ·
`OBJECTS`, `OBJECT_*`, `REPORT_*`, `APPLICATION_*`, `TABLES`, `SCHEMAS` (application
catalogue & data-sync metadata) · `SYSTEM_CONSTANTS*`.
Lookup helpers: `DEFINITIONS.DESCRIPTIONS.*` and `PKG_COMMON.GET_*_DESC`, `PKG_CPT.*`.

## Writing code against this database

1. Grep the reference for every table you touch; use exact column names/types and
   `%TYPE` anchors (`DEFINITIONS.CPT.CPT_ID%TYPE`) as existing code does.
2. Always qualify objects with the schema (`PAYROLL.PAY_MASTER`).
3. Don't set audit or multi-location columns; triggers do it.
4. Filter by `ORGANIZATION_ID` / `LOCATION_ID` for multi-site correctness, and by
   `ACTIVE = 'Y'` for master data.
5. Join payroll data to months with both `START_DATE` and `END_DATE`.
6. Check for an existing package function before writing a new calculation.
7. DML on replicated tables may be rejected by `_CEA` triggers on the wrong site
   (CR vs DC); if a user reports "Transaction of this table is not allowed on DC/CR",
   look at `DEFINITIONS.TABLES.MODEL_TYPE_ID` for that table.
8. When a needed schema (HRD, FINANCE, REGISTRATION…) isn't documented, say so and
   ask for its DDL instead of guessing.

### Example — net salary for current month with department

```sql
SELECT pm.mrno,
       pm.start_date,
       pm.end_date,
       pm.gross_payable,
       pm.net_payable
  FROM payroll.pay_master pm
  JOIN definitions.months m
    ON m.start_date = pm.start_date
   AND m.end_date   = pm.end_date
 WHERE m.current_month = 'Y';
-- department/designation come from HRD.INFORMATION (MRNO) — HRD DDL not documented yet.
```

### Example — allowance/deduction lines of an employee

```sql
SELECT pad.ad_code,
       dad.description,
       dad.ad_type,          -- A = allowance, D = deduction
       pad.calc_amount
  FROM payroll.pay_allowance_deduction pad
  JOIN payroll.def_allowance_deduction dad
    ON dad.ad_code         = pad.ad_code
   AND dad.organization_id = pad.ad_organization_id
   AND dad.location_id     = pad.ad_location_id
 WHERE pad.mrno       = :p_mrno
   AND pad.start_date = :p_start_date
   AND pad.end_date   = :p_end_date
 ORDER BY dad.ad_type, pad.ad_code;
```

## Regenerating

References and `docs/schema/*.md` are generated by `tools/parse_schema.py` from
PL/SQL Developer "Export User Objects" files:

```bash
python tools/parse_schema.py <exports>/*.txt --out docs/schema --skill-refs skm-domain/references
```

Re-run after schema changes, or to add HRD/FINANCE/REGISTRATION when their exports
are available (then add them to the tables above).
