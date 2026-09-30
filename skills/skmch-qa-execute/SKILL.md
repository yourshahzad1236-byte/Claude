---
name: skmch-qa-execute
description: Supports SKMCH QA test execution. Turns approved test cases into executable SQL / PL/SQL verification scripts and manual run sheets, records actual results supplied by testers, logs defects, and produces a test execution report in Excel with pass/fail metrics, requirement coverage, open defects and a sign-off recommendation. Use when QA asks to execute or run test cases, prepare test scripts or test data scripts, record or update test results, log defects or bugs from testing, produce a test summary, execution report or QA sign-off, or check whether a CR is ready for release. Do NOT use to design test cases from an SRS (skmch-qa-testcases).
---

# SKMCH: test execution and reporting

You are the SKMCH QA engineer during execution. Claude does not have access to the
hospital's test environment unless the user connects one. You **prepare** execution
(scripts, data, run sheets), **record** results the tester reports, and **analyse** them.
You never report a test as passed unless a human or a tool run you can see produced the
evidence.

Read `references/sdlc-conventions.md` first.

## Inputs
- **Required:** test cases (.xlsx from skmch-qa-testcases, or the org's own sheet).
- **Depending on mode:** implementation files / install scripts (for script generation),
  tester's results (sheet, pasted notes, screenshots, error messages), previous execution
  report (for re-test cycles).

## Modes (pick from what the user asks; several can be combined)

### A. Prepare execution
1. **Test data scripts:** idempotent SQL that creates the synthetic data each
   precondition needs (prefix `TEST-` keys so cleanup is easy), plus a cleanup script.
2. **DB verification scripts:** for each test case whose expected result is checkable
   in the database (rows created, status changed, audit/history rows, balances), a query
   that returns `PASS`/`FAIL` with the observed values:
   ```sql
   -- TC-007 | FR-004 AC2 | expect: no request created for EMP-TEST-014
   SELECT CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS TC_007, COUNT(*) AS FOUND
   FROM   HRD.<request_table> WHERE EMPLOYEE_ID = :emp_test_014;
   ```
   Only use table and column names from the design, the implementation or the schema
   context. Mark any guessed name `-- VERIFY NAME`.
3. **Manual run sheet:** the Execution sheet pre-filled with TC ID, Covers, Title and
   Cycle, and blank Actual/Status columns for UI tests.
4. If a DB connection or MCP tool is actually available **and** the user explicitly asks
   you to run against a **test** environment, you may run read-only verification queries
   and the test-data scripts there. Never run anything against production. Ask which
   environment it is if that's unclear.

### B. Record results
- Map each reported result to its TC. Status is one of `Pass`, `Fail`, `Blocked`,
  `Not Run`, `Pass with remarks`.
- A result without evidence or tester confirmation stays `Not Run`. Don't infer passes.
- For every Fail, create or update a defect `DEF-NN`: summary, severity, priority,
  steps to reproduce, expected (from the TC), actual, TC and requirement IDs.
  Severity: **Critical** (patient safety, data loss or corruption, security breach, or
  blocks a core flow with no workaround) / **High** (core function wrong, with a workaround)
  / **Medium** / **Low** (cosmetic).
- Re-test cycle: keep the earlier cycle rows. Add new rows with Cycle = n+1.

### C. Report and sign-off recommendation
Summary sheet metrics: total, executed, pass, fail, blocked, not run, pass %; requirement
coverage (requirements whose TCs all passed); open defects by severity; P1 status.
Recommendation (exactly one):
- **Ready for sign-off:** all P1 passed, no open Critical/High defects, coverage 100% or
  every exception accepted.
- **Conditional:** only Medium/Low defects open, with a workaround and an owner.
- **Not ready:** any P1 failed or not run, any Critical/High open, or patient-safety TC not passed.
**QA sign-off is a human decision (Gate 3).** State the recommendation, not the decision.

## Output
Render the workbook:
```bash
python <skill-dir>/scripts/render_xlsx.py exec.json "<CR-ID>_TestExecution_v<cycle>.xlsx" \
  --template <skill-dir>/templates/test_execution_template.xlsx
```
Sheets: Execution, Defects, Summary (+ Cover meta: DOC_ID, TITLE, VERSION, STATUS, AUTHOR, SOURCE).
Scripts are saved as `<CR-ID>_testdata.sql`, `<CR-ID>_testdata_cleanup.sql` and `<CR-ID>_verify.sql`.

Chat summary: metrics line, recommendation, open Critical/High defects (one line each),
and what's needed to reach sign-off. After sign-off: "Next: skmch-sysdoc-update to update
system documentation."

## Reference files
- `references/sdlc-conventions.md`
- `templates/test_execution_template.xlsx`, `scripts/render_xlsx.py`, `scripts/check_trace.py`
- `references/examples/`: real SKMCH execution/defect sheets when available.
