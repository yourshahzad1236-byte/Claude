# Test design guide (SKMCH)

## 1. Techniques
| Technique | Use for | Example |
|---|---|---|
| Equivalence partitioning | Input classes | Leave type: Annual / Sick / Casual / invalid code |
| Boundary value analysis | Numeric, date and length limits | Max 30 days → test 29, 30, 31. Name length 100 → 100 and 101 chars |
| Decision table | Combined rules | Eligibility = confirmed employee × balance ≥ days × no overlapping leave |
| State transition | Workflows | Draft → Submitted → Approved/Rejected → Cancelled. Illegal: Approved → Draft |
| Role/permission matrix | Access control | Each function × (one allowed role, one disallowed role) |
| Error guessing | Known risky areas | Double-click submit, back button after save, session timeout mid-form |

## 2. SKMCH / healthcare scenarios to consider every time
- **Date and time:** month-end and payroll cut-off, leap day (29-Feb), night shift that
  crosses midnight, back-dated entries, public holidays, Ramadan timings, fiscal year change.
- **Concurrency:** two approvers acting on the same request. The same user in two tabs.
- **Delegation:** approver on leave. Acting-charge assignments.
- **Data integrity:** duplicate submission, orphan records after cancel, history row written on update.
- **Audit:** CREATED_BY/ON and MODIFIED_BY/ON populated. History table has before/after values.
- **Security:** direct URL to page without the role (APEX authorization). Item value tampering
  (session state protection). Other department's data not visible.
- **Integrations:** payroll/attendance/HIS feed picks up the change. Behaviour when the feed is down.
- **Patient safety** (where applicable): wrong-patient prevention, clinical data not
  altered unintentionally, correct staff credential/roster for clinical areas.
- **Performance:** list/search at expected peak volume. Report generation time at month-end volume.
- **Regression:** existing screens and reports that use changed tables still return the same results.

## 3. Good vs weak expected results
- Weak: "Leave is saved successfully."
- Strong: "Success message 'Leave request LR-<n> submitted' is shown. The request
  appears in the reporting manager's Pending Approvals with status SUBMITTED. The applicant's
  available balance is unchanged until approval."

## 4. Example row (synthetic)
| Field | Value |
|---|---|
| TC ID | TC-007 |
| Covers | FR-004, AC2 |
| Module / Screen | Leave > Apply Leave (Page 20) |
| Title | Submission blocked when reporting manager is not defined |
| Type | Negative |
| Priority | P1 |
| Preconditions | Employee EMP-TEST-014 active, no reporting manager in current posting. Logged in as EMP-TEST-014 |
| Test Data | Leave type Annual, 01-10-2026 to 02-10-2026 |
| Steps | 1. Open Apply Leave. 2. Enter test data. 3. Click Submit |
| Expected Result | Error "Reporting manager not defined. Contact HR" is shown. No request is created (Pending Approvals unchanged, no new row in request list) |
| Patient-safety critical | N |
| Automatable | Y |
