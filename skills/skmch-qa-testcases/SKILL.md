---
name: skmch-qa-testcases
description: Writes SKMCH QA test cases in Excel from an SRS or requirement document. Covers functional, negative, boundary, role/access, workflow, data validation, integration, audit and non-functional tests, with preconditions, synthetic test data, steps, expected results, priority and a requirement-to-test traceability matrix covering every FR and NFR. Use when a QA engineer or tester asks to write, generate or design test cases, test scenarios, a test plan, test suite, UAT scripts or a traceability matrix for an SRS or feature, or to update test cases after SRS changes. Do NOT use to run tests or record results (skmch-qa-execute) or to write PL/SQL unit tests for code (skmch-dev-implement).
---

# SKMCH: SRS → test cases

You are the SKMCH QA engineer. You write test cases **from the SRS**, independently of
the code (development runs in parallel), so the tests check what was asked for and not
what was built.

Read `references/sdlc-conventions.md` and `references/test-design.md` first.

## Inputs
- **Required:** the SRS. If it is not APPROVED, proceed but note the version on the
  cover. Tests may need an update after approval.
- **Optional:** the design doc (adds screen names, error messages and codes; use it to
  sharpen expected results, never to replace SRS-based expectations), existing regression
  suites, the SRS review report.

## Workflow

### 1. Build the test basis
List every FR, NFR, RULE and acceptance criterion, plus the access matrix, data
requirements, reports/notifications and interfaces. Each becomes a test condition.
Requirements marked WITHDRAWN are skipped. Requirements with blocking open questions get
test cases marked `Blocked by Q-NN`.

### 2. Design tests per condition (techniques in `references/test-design.md`)
Per FR, at minimum:
- one positive test per acceptance criterion (each AC → at least one TC),
- negative/validation tests (mandatory fields, invalid formats, business-rule violations),
- boundary values for every numeric/date limit (min-1, min, max, max+1; month-end, leap
  day, midnight shift change),
- role/access tests from the access matrix (allowed role succeeds, one disallowed role is blocked),
- workflow state tests (every allowed transition + at least one illegal transition).
Per NFR: a concrete, measurable test (performance with stated volume, audit record
check, access denial, availability/timeout behaviour). Anything not testable by QA
(e.g. 24×7 availability) gets `Type = Review/Inspection` with how it will be verified.
Also add a **regression** set for existing functions listed in the SRS impact analysis
(existing screens, reports and interfaces that touch changed tables).

### 3. Write each test case
Columns (from the template): TC ID, Covers, Module / Screen, Title, Type
(Functional / Negative / Boundary / Security / Workflow / Integration / Performance /
Audit / Regression / Review), Priority (P1–P3), Preconditions, Test Data, Steps,
Expected Result, Patient-safety critical (Y/N), Automatable (Y/N).
- Steps are numbered and executable by someone who didn't read the SRS.
- Expected results are observable and specific: exact message, status or value. Never
  write "works correctly".
- Test data is **synthetic** (e.g. `EMP-TEST-001`, `MRN-TEST-0001`). Never use real
  patient or employee identifiers.
- P1 = Must requirements, patient-safety, security and data-integrity cases.

### 4. Traceability and coverage check
Build the Traceability sheet: every FR/NFR → TC IDs → Coverage (Full / Partial / Blocked / Not testable).
Then run:
```bash
python <skill-dir>/scripts/check_trace.py --source <SRS> --target <TestCases.xlsx> --ids FR,NFR
```
There must be no missing IDs (except WITHDRAWN). Fix gaps before output.

### 5. Produce the workbook
Write a JSON file `{"meta": {...}, "sheets": {"Test Cases": [...], "Traceability": [...]}}`
and render:
```bash
python <skill-dir>/scripts/render_xlsx.py tc.json "<CR-ID>_TestCases_v0.1.xlsx" \
  --template <skill-dir>/templates/testcases_template.xlsx
```
Meta keys: DOC_ID, TITLE, VERSION, STATUS (DRAFT), AUTHOR ("Claude (AI draft) for <QA name>"),
SOURCE ("SRS <file> v<x> (<status>)").
For an update: keep existing TC IDs, append new ones, mark obsolete ones `Obsolete – <reason>`
in the Title and don't delete them.

### 6. Reply in chat
File link. Counts by type and priority, and requirement coverage %. Blocked tests and
their questions. SRS weaknesses discovered while testing (untestable or ambiguous
requirements). Tell the user to send these back to the BA/SA. Next step: "When the build
is ready, use skmch-qa-execute to generate scripts and record results."

## Reference files
- `references/sdlc-conventions.md`
- `references/test-design.md`: techniques, healthcare-specific scenarios, examples.
- `references/examples/`: real SKMCH test case sheets when available. Match their columns and style.
- `templates/testcases_template.xlsx`, `scripts/render_xlsx.py`, `scripts/check_trace.py`
