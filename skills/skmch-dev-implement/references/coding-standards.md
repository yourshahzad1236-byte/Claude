# SKMCH PL/SQL, SQL and APEX coding standards

These add to `hrd-naming-standards.md`, which governs names. When the SKMCH code samples in
`examples/` differ from this file, the samples win. Tell the user about the difference so
this file can be updated.

## 1. File header
```sql
/*******************************************************************************
 * Object      : HRD.PKG_LEAVE_MANAGEMENT (body)
 * CR          : CR-2026-014
 * Design      : DS-03, DS-04
 * Requirements: FR-004, FR-005, NFR-AUD-01
 * Author      : Claude (AI) for <developer>
 * Date        : YYYY-MM-DD
 * Description : <one line>
 * Change log  :
 *   YYYY-MM-DD  CR-2026-014  <who>  <what>
 ******************************************************************************/
```

## 2. Packages
- Logic lives in packages. APEX processes, validations and DAs call package units. No
  business logic embedded in APEX pages.
- Public units are declared in the spec. Helpers stay private in the body.
- Types via `%TYPE` / `%ROWTYPE` for parameters and variables tied to columns.
- Parameter prefix `P_`, locals `V_`, constants `C_`, cursors `CUR_`, records `R_`,
  collections `T_`, exceptions `EX_` (from HRD standards).

## 3. Transactions
- Low-level DML procedures do **not** COMMIT. The caller (APEX page / top-level API /
  job) owns the transaction, unless the design says otherwise.
- Autonomous transactions only for logging.

## 4. Errors
- Use `RAISE_APPLICATION_ERROR(-20xxx, 'message')` with the codes defined in the design.
  User-facing messages must be clear and must not expose SQL.
- `WHEN OTHERS` only to log (with `DBMS_UTILITY.FORMAT_ERROR_BACKTRACE`) and re-raise.
  Never swallow errors.
- If the schema already has an error-logging package or table (check the schema context,
  e.g. `PKG_*LOG*`, `*_ERROR_LOG`), use it. Don't create a new one.

## 5. SQL
- Bind variables always. Dynamic SQL only when unavoidable, with `DBMS_ASSERT` on identifiers.
- Set-based SQL over loops. `BULK COLLECT … LIMIT` + `FORALL` for large sets.
- No `SELECT *` in code. Explicit column lists in `INSERT`.
- Uppercase keywords and identifiers (HRD standard §19).
- Dates: no implicit conversion. Use `TO_DATE(…, 'DD-MM-YYYY')` with an explicit format and `TRUNC` deliberately.
- Every new FK column gets an index.

## 6. Audit and data protection
- Populate `CREATED_BY/ON`, `MODIFIED_BY/ON` (APEX user via `NVL(SYS_CONTEXT('APEX$SESSION','APP_USER'), USER)`).
- History tables written in the same transaction (trigger or API, as designed).
- Never log patient or employee personal data in plain text in log tables or `DBMS_OUTPUT`.

## 7. APEX
- Static IDs per HRD standards (REG_, BTN_, DA_, LOV_, P<page>_ items).
- Authorization scheme on every page and every privileged button/process, as in the design.
- Validations call package functions (`F_IS_VALID_…`), so rules live in one place.
- Use Session State Protection for items that carry IDs.

## 8. Scripts
- `install.sql` starts with `SET DEFINE OFF`, `WHENEVER SQLERROR EXIT FAILURE ROLLBACK`, `SPOOL <CR-ID>_install.log`.
- Recompile invalid objects at the end (`DBMS_UTILITY.COMPILE_SCHEMA` only if the DBA
  allows it; otherwise list `ALTER … COMPILE` for dependents from the design §4.2).
- End with a verification query listing the new objects and their status.

## 9. Self-review checklist
- [ ] Every Change-inventory row implemented, or listed as a deviation with reason.
- [ ] Signatures match the design exactly (or deviation logged).
- [ ] Naming 100% HRD standard (packages, units, params, variables, constraints, indexes, triggers, sequences, static IDs).
- [ ] No COMMIT in low-level units. No swallowed exceptions. No `SELECT *`.
- [ ] Bind variables. No string-concatenated SQL with user input.
- [ ] Audit columns and history handled per the design.
- [ ] Rollback script covers every forward step.
- [ ] Unit tests: happy path + each exception + SRS acceptance criteria. Synthetic data only.
- [ ] No real patient or employee data anywhere.
- [ ] Headers carry CR/DS/FR IDs.
