# 1. Introduction

## 1.1 Purpose

This SRS specifies the Automated Employee Probation Evaluation workflow for the HR module of the HRD system. It covers automatic creation of probation evaluation queue items for supervisors, evaluation entry (Draft or Submit), routing through the configured approval hierarchy, hand-over of completed evaluations to the HR Department, and automatic status updates of the probation request. It is written for the Solution Architect (review and approval), the development team (design and build) and QA (test design).

## 1.2 Background

Employees joining SKMCH serve a probation period. Before the probation end date, the employee's supervisor must evaluate the employee so that HR can decide on confirmation. The requested change automates this: the system starts the evaluation on time, routes it through the approval hierarchy and delivers it to HR, while keeping the probation request status current at every step (M-01 to M-08). How the process is run today (manual forms, e-mail or an existing screen) was not described in the request (Q-02).

## 1.3 Scope

### In scope

- Automatic generation of a probation evaluation queue item for the respective supervisor 15 days before the employee's probation end date (M-02, M-03).
- Evaluation entry by the evaluator with Save as Draft and Submit for approval (M-04, M-05).
- Routing of a submitted evaluation through the configured approval hierarchy (M-06).
- Automatic routing of the completed evaluation to the HR Department (M-07).
- Automatic update of the probation request status throughout the workflow, with status history (M-08).

### Out of scope

- HR's downstream action on the evaluation (confirmation letter, probation extension, termination, payroll/grade changes). Not discussed; HR's exact action on receipt is open (Q-06).
- Design of the evaluation form content (criteria, rating scale, recommendation values). Not provided in the request; to be supplied by HR (Q-05). The workflow is in scope; the form content is a dependency.
- Probation evaluation of employees whose probation is ended early (resignation, termination) — the queue is cancelled only (see FR-004); no separate process is specified.
- Self-evaluation by the employee. Not mentioned.
- Automatic confirmation, extension or termination of probation, including when an evaluation is overdue (changed in v0.2, RV-17).

## 1.4 Stakeholders

| Name / Role | Department | Interest / responsibility | Attended meeting |
|---|---|---|---|
| HR Department representative(s) (names not stated, Q-13) | HR | Business owner; receives completed evaluations; owns probation policy | Not stated |
| Supervisors / evaluators | All departments | Complete probation evaluations on time | No |
| Approvers in the approval hierarchy (e.g. HOD) | All departments | Review and approve submitted evaluations | No |
| Employees on probation | All departments | Subject of the evaluation (no system action) | No |
| Business Analyst | IT / Development | Requirement owner for this SRS | Not stated |
| Solution Architect | IT | SRS review and approval (Gate 1) | Not stated |
| Development team / QA | IT | Build and test | Not stated |

## 1.5 Definitions and abbreviations

| Term | Meaning |
|---|---|
| Probation end date | The date on which the employee's probation period ends, as held in the employee's HR record |
| Probation request | The HR record that tracks an employee's probation period and its evaluation outcome (whether this already exists in HRD is to be confirmed, Q-03) |
| Probation request status | The HR-level status of the employee's probation period, updated automatically from the evaluation workflow (changed in v0.2, RV-04; mapping to be finalised with Q-03, Q-09) |
| Evaluation status | The workflow status of a probation evaluation, with the values and transitions in RULE-08 (added in v0.2, RV-04) |
| Probation evaluation | The assessment of an employee on probation, completed by the evaluator and approved through the hierarchy |
| Evaluator | The respective supervisor of the employee, who completes the evaluation |
| Respective supervisor | The employee's direct supervisor / reporting manager on record (source to be confirmed, Q-04) |
| Queue | A pending work item shown to a user on their queue / inbox screen |
| Approval hierarchy | The configured ordered list of approval levels a submitted evaluation passes through |
| Draft | A saved but not submitted evaluation, visible and editable only by the evaluator |
| HOD | Head of Department |
| APEX | Oracle Application Express, the platform for the HRD applications |
| MoM | Minutes of Meeting |

## 1.6 References

- Request: "Automated Employee Probation Evaluation", proposed workflow points 1 to 5 (shared in chat, 2026-10-09). Meeting date and attendees not stated (Q-13).
- Earlier SRS versions: none.
- Related CRs: none known. CR number to be assigned (Q-14). Placeholder `CR-2026-XXX-PEV` used because `CR-2026-XXX` is already used by the Committee Workflow CR.
- HR probation policy / SOP: to be supplied by HR (Q-05, Q-08).

# 2. Current state (As-Is)

The request does not describe the current process (Q-02). Based on the requested changes, the following is assumed (A-01):

1. HR tracks probation end dates and asks supervisors to evaluate employees, manually or by a non-automated means.
2. Supervisors complete the evaluation outside a system workflow (or on a screen without approval routing) and send it to HR.
3. Approval by higher levels (if any) is obtained manually.
4. Probation request status, if a probation request record exists, is updated manually by HR.

Pain points implied by the request: evaluations started late or missed, no consistent approval path, no automatic hand-over to HR, and status that does not reflect where the evaluation actually is.

# 3. Proposed solution overview (To-Be)

1. Every day, the system identifies employees whose probation end date is 15 days away and creates a probation evaluation queue item for each employee's respective supervisor. The probation request status becomes **Evaluation Pending**.
2. The supervisor opens the queue item and fills in the evaluation. They may **Save as Draft** (status **Draft**) and return later, or **Submit** it for approval.
3. On Submit, the system validates the evaluation and routes it to the first level of the configured approval hierarchy. The status becomes **Pending Approval** (with the current level shown).
4. Each approver approves (the evaluation moves to the next level) or returns it to the evaluator for correction (status **Returned**; Q-07).
5. When the last level approves, the system routes the completed evaluation to the HR Department queue. The status becomes **Forwarded to HR**.
6. HR receives and processes the evaluation; on HR closure the status becomes **Completed** (Q-06).
7. Every status change is recorded with date, time and user, so HR and the supervisor can see where each evaluation stands.

The status names above are proposed (A-03) and need HR confirmation (Q-09).

# 4. Business requirements

| ID | Business requirement | Source (M-NN) | Priority |
|---|---|---|---|
| BR-01 | Every employee on probation shall be evaluated by their supervisor before the probation end date, with the evaluation started automatically in good time. | M-01, M-02, M-03 | Must |
| BR-02 | Evaluators shall be able to work on an evaluation over more than one session before committing it. | M-04, M-05 | Must |
| BR-03 | Every submitted evaluation shall be reviewed through the organisation's configured approval hierarchy. | M-06 | Must |
| BR-04 | HR shall receive every completed evaluation without manual follow-up. | M-07 | Must |
| BR-05 | HR and supervisors shall always know the current stage of each probation evaluation. | M-08 | Must |

# 5. Functional requirements

## 5.1 Queue generation

### FR-001 Identify employees due for evaluation

**Description:** The system shall, once every day, identify each employee on probation whose probation end date is on or before 15 calendar days after the current date, is not earlier than the current date, and who has no evaluation for the current probation period (changed in v0.2, RV-05).
**Priority:** Must
**Source:** M-02
**Business rules:** RULE-01, RULE-03
**Acceptance criteria:**
- AC1: Given an employee on probation with a probation end date of 25-Oct-2026, when the daily process runs on 10-Oct-2026, then the employee is identified as due for evaluation.
- AC2 (negative): Given an employee on probation with a probation end date of 26-Oct-2026, when the daily process runs on 10-Oct-2026, then the employee is not identified.
- AC3 (negative): Given an employee who is not on probation (confirmed or separated), when the daily process runs, then the employee is not identified regardless of dates.
- AC4 (catch-up): Given the daily process did not run on 10-Oct-2026 and an employee's probation end date is 25-Oct-2026 with no evaluation, when the process runs on 12-Oct-2026, then the employee is identified.
**Notes / open questions:** Q-01 (calendar vs working days), Q-10 (catch-up for missed runs and go-live backlog).

### FR-002 Generate evaluation queue item for respective supervisor

**Description:** The system shall create a probation evaluation queue item, assigned to the employee's respective supervisor, for each employee identified by FR-001.
**Priority:** Must
**Source:** M-02, M-03
**Business rules:** RULE-02, RULE-03
**Acceptance criteria:**
- AC1: Given employee EMP-TEST-0001 is identified and their supervisor on record is EMP-TEST-0100, when the daily process completes, then a probation evaluation queue item for EMP-TEST-0001 appears in EMP-TEST-0100's queue.
- AC2 (negative): Given employee EMP-TEST-0001 is identified, when the daily process completes, then no other user except the assigned supervisor (and HR monitoring, FR-017) sees the queue item.
**Notes / open questions:** Q-04 (source of "respective supervisor").

### FR-003 Prevent duplicate evaluation queue items

**Description:** The system shall create no more than one active probation evaluation for the same employee and probation period.
**Priority:** Must
**Source:** M-02 (Inferred)
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a queue item already exists for EMP-TEST-0001's current probation period, when the daily process runs again (e.g. re-run of the same day), then no second queue item is created.
- AC2: Given an employee's probation period is extended by HR with a new end date, when the new trigger date is reached, then a new evaluation is created for the new period (subject to Q-08).
**Notes / open questions:** Q-08 (probation extension).

### FR-004 Cancel evaluation when probation ends early

**Description:** The system shall cancel an open probation evaluation and remove it from all queues when the employee is no longer on probation (separation or early confirmation) before the evaluation is completed.
**Priority:** Should
**Source:** M-08 (Inferred)
**Business rules:** RULE-08
**Acceptance criteria:**
- AC1: Given an evaluation in Draft for EMP-TEST-0002, when HR records EMP-TEST-0002's separation, then the evaluation status becomes Cancelled and it disappears from the supervisor's queue.
- AC2 (negative): Given an evaluation already Forwarded to HR, when the employee separates, then the evaluation is not cancelled automatically and remains with HR.
**Notes / open questions:** Q-11.

### FR-005 Handle missing supervisor

**Description:** The system shall, when an identified employee has no respective supervisor on record, create the evaluation unassigned and show it on an HR exception list instead of a supervisor queue.
**Priority:** Must
**Source:** M-03 (Inferred)
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given an identified employee with no supervisor on record, when the daily process runs, then the evaluation appears on the HR exception list with the reason "Supervisor not defined".
- AC2: Given an evaluation on the HR exception list, when an HR Administrator assigns an evaluator using FR-006, then the queue item moves to that evaluator's queue.
- AC3 (negative): Given an identified employee with no supervisor, when the daily process runs, then the process does not fail and continues for the other employees.
**Notes / open questions:** Q-04.

### FR-006 Reassign evaluator

**Description:** The system shall allow an HR Administrator to assign or reassign an evaluation that is unassigned or not yet submitted to a different evaluator (changed in v0.2, RV-15).
**Priority:** Should
**Source:** M-03 (Inferred)
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given an evaluation in Evaluation Pending or Draft, when an HR Administrator reassigns it to EMP-TEST-0101, then it leaves the old supervisor's queue and appears in EMP-TEST-0101's queue with any draft content kept.
- AC2 (negative): Given an evaluation in Pending Approval, when an HR Administrator tries to reassign the evaluator, then the action is not available.
**Notes / open questions:** Q-12 (supervisor change after queue generation).

## 5.2 Evaluation entry

### FR-007 Open evaluation from queue

**Description:** The system shall allow the assigned evaluator to open a probation evaluation from their queue showing the employee's basic details (employee number, name, department, designation, joining date, probation end date) and the evaluation form.
**Priority:** Must
**Source:** M-02, M-03
**Business rules:** -
**Acceptance criteria:**
- AC1: Given a queue item assigned to the evaluator, when they open it, then the employee details and the evaluation form are shown.
- AC2 (negative): Given a user who is not the assigned evaluator, when they try to open the evaluation by URL, then access is denied.
**Notes / open questions:** Q-05 (form content).

### FR-008 Save evaluation as Draft

**Description:** The system shall allow the evaluator to save a partially or fully completed evaluation as Draft without routing it, and to reopen and edit it later.
**Priority:** Must
**Source:** M-04
**Business rules:** RULE-04, RULE-05
**Acceptance criteria:**
- AC1: Given an evaluation with some fields filled, when the evaluator clicks Save as Draft, then the entries are saved, the status becomes Draft, and the item stays in the evaluator's queue.
- AC2: Given an evaluation in Draft, when the evaluator reopens it, then all previously saved values are shown and editable.
- AC3 (negative): Given an evaluation in Draft, when any approver or HR user looks at their queue, then the evaluation is not there.
**Notes / open questions:** -

### FR-009 Submit evaluation for approval

**Description:** The system shall allow the evaluator to submit a completed evaluation for approval after validating that all mandatory fields are filled.
**Priority:** Must
**Source:** M-05
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given an evaluation with all mandatory fields filled, when the evaluator clicks Submit and confirms, then the evaluation is submitted and FR-011 routing starts.
- AC2 (negative): Given an evaluation with a mandatory field empty, when the evaluator clicks Submit, then submission is refused, the missing fields are highlighted, and the status is unchanged.
**Notes / open questions:** Q-05.

### FR-010 Lock submitted evaluation

**Description:** The system shall prevent the evaluator from changing a submitted evaluation unless it has been returned to them.
**Priority:** Must
**Source:** M-05 (Inferred)
**Business rules:** RULE-08
**Acceptance criteria:**
- AC1: Given a submitted evaluation, when the evaluator opens it, then it is read-only.
- AC2: Given an evaluation returned by an approver, when the evaluator opens it, then it is editable again and can be re-submitted.
**Notes / open questions:** Q-07.

## 5.3 Approval routing

### FR-011 Route to configured approval hierarchy

**Description:** The system shall route a submitted evaluation to the first level of the approval hierarchy configured for probation evaluations, resolving the approver for that level from the evaluated employee's department as on the submission date (changed in v0.2, RV-12; pending Q-16).
**Priority:** Must
**Source:** M-06
**Business rules:** RULE-06, RULE-09
**Acceptance criteria:**
- AC1: Given a configured hierarchy of Level 1 = HOD and Level 2 = Director, when an evaluation for an employee in Department D-TEST is submitted, then it appears in the D-TEST HOD's approval queue and the status shows Pending Approval – Level 1.
- AC2 (negative): Given a hierarchy level whose approver cannot be resolved, when the evaluation reaches that level, then it is placed on the HR exception list with the reason "Approver not defined for level n" and is not lost.
**Notes / open questions:** Q-15 (is there an existing approval hierarchy setup), Q-16 (hierarchy basis).

### FR-012 Approve at a level

**Description:** The system shall allow the approver at the current level to approve the evaluation, with optional comments, and move it to the next configured level.
**Priority:** Must
**Source:** M-06
**Business rules:** RULE-06
**Acceptance criteria:**
- AC1: Given an evaluation at Level 1 of a 2-level hierarchy, when the Level 1 approver approves, then it moves to the Level 2 approver's queue and leaves the Level 1 queue.
- AC2 (negative): Given an evaluation at Level 2, when the Level 1 approver tries to approve it again, then the action is not available.
**Notes / open questions:** -

### FR-013 Return evaluation to evaluator

**Description:** The system shall allow an approver to return an evaluation to the evaluator with mandatory comments.
**Priority:** Should
**Source:** M-06 (Inferred)
**Business rules:** RULE-08
**Acceptance criteria:**
- AC1: Given an evaluation at any level, when the approver returns it with comments, then the status becomes Returned and it appears in the evaluator's queue with the comments shown.
- AC2 (negative): Given the approver leaves the comments empty, when they click Return, then the action is refused.
**Notes / open questions:** Q-07 (return vs reject, and where a re-submission restarts).

### FR-014 Prevent self-approval

**Description:** The system shall prevent a user from approving an evaluation in which they are the evaluated employee or the evaluator.
**Priority:** Must
**Source:** M-06 (Inferred)
**Business rules:** RULE-09
**Acceptance criteria:**
- AC1: Given the evaluator is also the resolved Level 1 approver, when the evaluation is submitted, then it moves to the next level and the history records "Skipped: approver is evaluator". If there is no next level, it is placed on the HR exception list (changed in v0.2, RV-06).
- AC2 (negative): Given the evaluated employee is a resolved approver, when routing runs, then the evaluation is never placed in that employee's queue.
**Notes / open questions:** Q-16.

## 5.4 Routing to HR

### FR-015 Forward completed evaluation to HR

**Description:** The system shall automatically route the evaluation to the HR Department queue when the last level of the approval hierarchy approves it.
**Priority:** Must
**Source:** M-07
**Business rules:** RULE-07
**Acceptance criteria:**
- AC1: Given an evaluation at the last configured level, when that approver approves, then the evaluation appears in the HR Department queue and the status becomes Forwarded to HR.
- AC2 (negative): Given an evaluation still at an intermediate level, when HR views its queue, then the evaluation is not in HR's actionable queue (only on the monitoring view, FR-017).
**Notes / open questions:** Q-06, Q-17 ("after submission" timing).

### FR-016 HR closes evaluation

**Description:** The system shall allow an HR user to mark a forwarded evaluation as processed, which completes the evaluation.
**Priority:** Must
**Source:** M-07, M-08
**Business rules:** RULE-08
**Acceptance criteria:**
- AC1: Given an evaluation Forwarded to HR, when an HR user marks it as processed, then the status becomes Completed and it leaves the HR queue.
- AC2 (negative): Given an evaluation in Pending Approval, when an HR user tries to mark it processed, then the action is not available.
**Notes / open questions:** Q-06 (HR actions and outcome values).

## 5.5 Status tracking

### FR-017 Automatic probation request status update

**Description:** The system shall update the probation request status automatically at each workflow event: queue generated, saved as draft, submitted, approved at a level, returned, forwarded to HR, completed and cancelled.
**Priority:** Must
**Source:** M-08
**Business rules:** RULE-08
**Acceptance criteria:**
- AC1: Given an evaluation in Draft, when the evaluator submits it, then the probation request status changes to Pending Approval – Level 1 with no manual step.
- AC2: Given each event in the list, when it occurs, then the status changes to the value defined in RULE-08.
- AC3 (negative): Given a user tries to change the status directly (not through a workflow action), then the system does not allow it.
**Notes / open questions:** Q-09 (status values).

### FR-018 Status history

**Description:** The system shall record every status change of a probation evaluation with old status, new status, action, comments, user and date-time.
**Priority:** Must
**Source:** M-08
**Business rules:** -
**Acceptance criteria:**
- AC1: Given an evaluation that has gone through Draft, Submit and Level 1 approval, when an HR user views its history, then three entries are shown in time order with user and date-time.
- AC2 (negative): Given any user, when they try to edit or delete a history entry, then the action is not available.
**Notes / open questions:** -

### FR-019 Probation evaluation monitoring view

**Description:** The system shall provide HR users with a list of all probation evaluations, filterable by status, department, evaluator and probation end date range.
**Priority:** Should
**Source:** M-08 (Inferred)
**Business rules:** -
**Acceptance criteria:**
- AC1: Given evaluations in several statuses, when an HR user filters by status "Pending Approval", then only those evaluations are listed with their current level and approver.
- AC2 (negative): Given a supervisor without the HR role, when they try to open the monitoring view, then access is denied.
**Notes / open questions:** -

### FR-020 Overdue flag

**Description:** The system shall flag an evaluation as overdue when it is not Forwarded to HR or Completed by the probation end date.
**Priority:** Should
**Source:** M-02 (Inferred)
**Business rules:** RULE-10
**Acceptance criteria:**
- AC1: Given an evaluation in Draft on the day after the probation end date, when HR opens the monitoring view, then the evaluation is shown as overdue.
- AC2 (negative): Given an evaluation Forwarded to HR before the probation end date, then it is never flagged overdue.
**Notes / open questions:** Q-18 (escalation and reminders).

# 6. Non-functional requirements

| ID | Category | Requirement | Measure / target | Source | Status |
|---|---|---|---|---|---|
| NFR-SEC-01 | Security | Access to evaluation, approval, HR and configuration functions is controlled by APEX authorization schemes per the access matrix (§7.3). | 100% of pages/actions protected; verified by role tests | Inferred | Proposed (not discussed in meeting) |
| NFR-SEC-02 | Security | Evaluation content (employee personal/performance data) is visible only to the evaluated employee's evaluator, the approvers in its routing path and HR. | No other user can see content via page, report or URL change | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-01 | Audit | Every evaluation record stores created by/on and modified by/on. | All rows | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-02 | Audit | Status history (FR-018) is retained and cannot be modified by any application user. | Insert-only | M-08 | Discussed |
| NFR-PERF-01 | Performance | The daily queue generation process completes for the full active employee population. | ≤ 5 minutes for up to 15,000 active employees | Inferred | Proposed (not discussed in meeting) |
| NFR-PERF-02 | Performance | Queue, evaluation and monitoring pages load quickly. | ≤ 3 s (95th percentile, hospital LAN, up to 1,000 open evaluations) | Inferred | Proposed (not discussed in meeting) |
| NFR-AVL-01 | Availability | If the daily process does not run on a day (outage), the next run picks up all employees missed. | No employee missed after a gap of up to 7 days | Inferred | Proposed (not discussed in meeting) |
| NFR-AVL-02 | Availability | Deployment needs no downtime of the existing HR application beyond a normal release window. | Within standard release window | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-01 | Data retention | Evaluations and history are retained as part of the employee's HR record and are not deleted by the application. | Per HR record-retention policy (Q-19) | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-02 | Data quality | At most one active evaluation exists per employee per probation period. | Enforced by the system (RULE-03) | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-03 | Data quality | The system rejects a save or workflow action on an evaluation that another user changed after it was opened, with the message "This evaluation was changed by another user. Reload and try again." A repeated Submit or Approve has no further effect (added in v0.2, RV-09). | 0 lost updates; 0 duplicate approvals in concurrency tests | Inferred | Proposed (not discussed in meeting) |
| NFR-USA-01 | Usability | Evaluation form usable on standard hospital desktop browsers and tablet width; English UI. | Chrome/Edge current versions; ≥ 768 px width | Inferred | Proposed (not discussed in meeting) |
| NFR-USA-02 | Usability | Unsaved changes warning when leaving the evaluation page. | Warning shown on navigation away with unsaved data | Inferred | Proposed (not discussed in meeting) |
| NFR-CMP-01 | Compliance | Workflow follows SKMCH HR probation policy (lead time, approval levels, HR outcome) and applicable labour law on probation. | HR sign-off of status model and rules | Inferred | Proposed (not discussed in meeting) |
| NFR-INT-01 | Integration | Employee, probation end date, supervisor and department are read from the HRD employee master in real time (no duplicated master data). | No copied master data except snapshot at queue generation | Inferred | Proposed (not discussed in meeting) |
| NFR-OPS-01 | Operations | The daily process logs start, end, employees processed and errors, and failures are visible to IT support. | Log entry every run; failure alert to IT support | Inferred | Proposed (not discussed in meeting) |
| NFR-OPS-02 | Operations | E-mail / in-app notifications are sent when a queue item is assigned to a user. A notification failure does not block the workflow action, and failures are logged and visible to IT support (changed in v0.2, RV-13). | Within 15 minutes of assignment | Inferred | Proposed (not discussed in meeting) (Q-18) |

# 7. Business rules, data and access

## 7.1 Business rules

| ID | Rule | Applies to (FR) | Source |
|---|---|---|---|
| RULE-01 | Trigger date = probation end date − 15 calendar days. An employee is picked up on the first daily run on or after the trigger date and before the probation end date. | FR-001 | M-02 (calendar vs working days, Q-01) |
| RULE-02 | The evaluator is the employee's respective supervisor on record on the trigger date. If none is on record, the evaluation goes to the HR exception list. | FR-002, FR-005, FR-006 | M-03 |
| RULE-03 | Only one active evaluation per employee per probation period. | FR-001, FR-003 | Inferred |
| RULE-04 | A Draft is never routed and is visible only to the evaluator. | FR-008 | M-04 |
| RULE-05 | Mandatory-field validation applies on Submit only, not on Save as Draft. | FR-008, FR-009 | M-04, M-05 |
| RULE-06 | A submitted evaluation passes through the configured hierarchy levels in order; the hierarchy in effect at submission time applies to that evaluation. | FR-011, FR-012 | M-06 |
| RULE-07 | The evaluation goes to HR after approval at the last configured level (assumption A-02; Q-17). | FR-015 | M-07 |
| RULE-08 | Allowed status transitions (proposed, Q-09): Evaluation Pending → Draft → Pending Approval – Level n → (Pending Approval – Level n+1 \| Returned \| Forwarded to HR); Returned → Draft/Pending Approval – Level 1; Forwarded to HR → Completed; any status before Forwarded to HR → Cancelled. No other transition is allowed. | FR-004, FR-010, FR-013, FR-016, FR-017 | M-08 |
| RULE-09 | A user may not approve an evaluation in which they are the evaluated employee or the evaluator; such a level is skipped and the evaluation moves to the next level, with the reason recorded in history; if there is no next level, the evaluation goes to the HR exception list (changed in v0.2, RV-06; proposed, Q-16). | FR-011, FR-014 | Inferred |
| RULE-10 | An evaluation not Forwarded to HR or Completed by the probation end date is overdue. | FR-020 | Inferred |

## 7.2 Data requirements

| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
|---|---|---|---|---|---|
| Evaluation number | Unique reference of the evaluation | Yes (system) | System generated | PEV-2026-000123 | FR-002 |
| Employee | Employee being evaluated | Yes (system) | Must be on probation at generation | EMP-TEST-0001 | FR-001, FR-002 |
| Probation start / end date | Probation period evaluated | Yes (system) | From employee record; end ≥ start | 26-Apr-2026 / 25-Oct-2026 | FR-001 |
| Evaluator | Assigned supervisor | Yes | Active employee, not the evaluated employee | EMP-TEST-0100 | FR-002, FR-006 |
| Evaluation criteria and ratings | Performance assessment | Yes on Submit | Per HR form design (Q-05) | Punctuality: 4 / 5 | FR-008, FR-009 |
| Evaluator recommendation | Confirm / Extend / Terminate (values to be confirmed) | Yes on Submit | From LOV (Q-05) | Confirm | FR-009 |
| Evaluator comments | Free-text remarks | Q-05 | Max 4,000 characters | "Meets expectations." | FR-009 |
| Current status | Workflow status of the probation request | Yes (system) | RULE-08 values | Pending Approval – Level 1 | FR-017 |
| Current approval level / approver | Where the evaluation is now | Yes when pending approval | From hierarchy | Level 1 / EMP-TEST-0200 | FR-011 |
| Approver action and comments | Decision at a level | Action yes; comments mandatory on Return | Approve / Return | Return – "Add training needs." | FR-012, FR-013 |
| Status history entry | Audit of each status change | Yes (system) | Insert-only | Draft → Pending Approval – L1, EMP-TEST-0100, 15-Oct-2026 10:22 | FR-018 |
| Approval hierarchy configuration | Ordered levels and approver role per level | Yes | At least one level | L1 = HOD, L2 = Director | FR-011 |

## 7.3 User roles and access matrix

| Function / screen | Evaluator (supervisor) | Approver | HR User | HR Administrator | Evaluated employee |
|---|---|---|---|---|---|
| Daily queue generation (system) | - | - | - | - | - |
| My queue (evaluations / approvals) | R | R | R | R | - |
| Evaluation form – edit (Draft / Submit) | C R U | - | - | - | - (Q-20) |
| Evaluation form – view submitted (changed in v0.2, RV-10) | R | R (own path) | R | R | - (Q-20) |
| Approve / Return | - | R A | - | - | - |
| HR queue – mark processed | - | - | R U | R U | - |
| Reassign evaluator / HR exception list | - | - | R | R U | - |
| Monitoring view and history | R (own) | R (own path) | R | R | - |
| Approval hierarchy configuration | - | - | R | C R U D | - |

## 7.4 Reports and notifications

| Report / notification | Audience | Trigger / frequency | Content | Related FR |
|---|---|---|---|---|
| New evaluation assigned (proposed) | Evaluator | Queue item created or reassigned | Employee, probation end date, link | FR-002, FR-006, NFR-OPS-02 |
| Pending approval (proposed) | Approver at current level | Evaluation reaches the level | Employee, evaluator, link | FR-011, FR-012 |
| Evaluation returned (proposed) | Evaluator | Return action | Approver comments, link | FR-013 |
| Evaluation forwarded to HR (proposed) | HR Department | Last-level approval | Employee, recommendation, link | FR-015 |
| Probation evaluation monitoring view | HR | On demand | All evaluations by status, overdue flag | FR-019, FR-020 |
| Reminder / escalation before end date | Evaluator, approver, HR | To be defined (Q-18) | Pending items nearing end date | FR-020 |

## 7.5 Interfaces

| System | Direction (in/out) | Data exchanged | Frequency | Related FR |
|---|---|---|---|---|
| HRD employee master / posting (same schema) | In | Employee status, probation dates, supervisor, department | Daily process and on page load | FR-001, FR-002, FR-007 |
| E-mail (existing HRD mail mechanism, to be confirmed) | Out | Notifications in §7.4 | Event-driven | NFR-OPS-02 |
| Payroll / ERP | Not applicable: HR's downstream action on confirmation is out of scope | - | - | - |

# 8. Impact analysis

> Schema context used: none — the `skmch-hrd-system-context` index is NOT YET INDEXED and `schema/` holds no objects. **Impact analysis is PROVISIONAL.** No existing object names are asserted; every existing object below is TO BE CONFIRMED and every new object is NEW (proposed).

## 8.1 Business impact

| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
|---|---|---|---|---|
| IMP-01 | HR Department – probation management process | Manual tracking of due evaluations replaced by system queue and monitoring view; SOP update needed. | FR-001, FR-015, FR-019 | N |
| IMP-02 | All departments – supervisors | New queue task, 15 days before each subordinate's probation end; training/communication needed. | FR-002, FR-008, FR-009 | N |
| IMP-03 | Approvers (HODs and above) | New approval items in queue. | FR-011, FR-012 | N |
| IMP-04 | Clinical departments | Indirect: probation outcome for clinical staff (nurses, doctors) affects staffing. No direct clinical data. | FR-015 | N (indirect staffing only) |

## 8.2 System impact

| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|
| IMP-05 | HRD APEX application – employee self-service / queue (inbox) page | Modify (TO BE CONFIRMED) | Show probation evaluation and approval items in the existing queue, if one exists (Q-15). | FR-002, FR-007, FR-011 | None (no schema) | PROVISIONAL – not verified |
| IMP-06 | APEX page "Probation Evaluation" | NEW (proposed) | Evaluation form with Save as Draft / Submit, approval actions and history region. | FR-007–FR-014, FR-018 | None | PROVISIONAL – not verified |
| IMP-07 | APEX page "Probation Evaluation Monitoring" | NEW (proposed) | HR list, filters, overdue flag, exception list, reassignment. | FR-005, FR-006, FR-016, FR-019, FR-020 | None | PROVISIONAL – not verified |
| IMP-08 | APEX page "Probation Approval Hierarchy Setup" | NEW (proposed) or reuse existing workflow setup | Configure ordered approval levels. | FR-011 | None | PROVISIONAL – not verified |
| IMP-09 | Package `HRD.PKG_PROBATION_EVALUATION` | NEW (proposed) | Queue generation (`P_GENERATE_EVAL_QUEUE`), save/submit, routing, approve/return, forward to HR, status update and history. | FR-001–FR-018 | None | PROVISIONAL – not verified |
| IMP-10 | Scheduler job (DBMS_SCHEDULER) for daily queue generation | NEW (proposed) | Runs `P_GENERATE_EVAL_QUEUE` daily, with run log. | FR-001, NFR-AVL-01, NFR-OPS-01 | None | PROVISIONAL – not verified |
| IMP-11 | Existing approval/workflow package (if any) | Read-only / Modify (TO BE CONFIRMED) | Reuse for hierarchy resolution if HRD already has one (Q-15). | FR-011 | None | PROVISIONAL – not verified |
| IMP-12 | APEX authorization schemes | NEW / Modify | Evaluator, Approver, HR User, HR Administrator checks. | NFR-SEC-01 | None | PROVISIONAL – not verified |
| IMP-13 | E-mail notification utility | Read-only (TO BE CONFIRMED) | Send notifications in §7.4. | NFR-OPS-02 | None | PROVISIONAL – not verified |

## 8.3 Database impact

| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|
| IMP-14 | Employee master table (name TO BE CONFIRMED) – probation end date, employment status, supervisor columns | Read-only | Source of eligibility and evaluator. Must confirm the columns exist. | Unknown | None | FR-001, FR-002 | None | PROVISIONAL – not verified |
| IMP-15 | Existing "probation request" table (TO BE CONFIRMED, Q-03) – status column | Modify / Read-write | Status updated by the workflow; new status values may be needed. | Unknown | Map existing statuses to RULE-08 (Q-09) | FR-017 | None | PROVISIONAL – not verified |
| IMP-16 | `HRD_PROBATION_EVAL_MST` | NEW (proposed) | One row per evaluation: employee, period, evaluator, status, current level, recommendation, audit columns. | IMP-09 | Go-live backlog creation (Q-10) | FR-002–FR-017 | None | PROVISIONAL – not verified |
| IMP-17 | `HRD_PROBATION_EVAL_DTL` | NEW (proposed) | Criteria ratings / answers per evaluation. | IMP-16 | None | FR-008, FR-009 | None | PROVISIONAL – not verified |
| IMP-18 | `HRD_PROBATION_EVAL_HIS` | NEW (proposed) | Insert-only status history. | IMP-16 | None | FR-018, NFR-AUD-02 | None | PROVISIONAL – not verified |
| IMP-19 | `HRD_PROBATION_APPROVAL_TRN` | NEW (proposed) | Per-level approval actions and comments. | IMP-16 | None | FR-011–FR-014 | None | PROVISIONAL – not verified |
| IMP-20 | `HRD_PROBATION_HIERARCHY_MST` (unless an existing hierarchy setup is reused, Q-15) | NEW (proposed) | Ordered approval levels. | IMP-11 | Seed with HR-agreed levels | FR-011 | None | PROVISIONAL – not verified |
| IMP-21 | Sequences `PROBATION_EVAL_SEQ` etc.; unique index on (employee, probation period) | NEW (proposed) | Keys and RULE-03 enforcement. | IMP-16 | None | FR-003 | None | PROVISIONAL – not verified |

Volume: assumed a few hundred to low thousands of new evaluations per year (one per new hire), low growth (A-05).

## 8.4 Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Supervisor data in employee master is incomplete or stale, so queues go to the wrong person or nobody. | Medium | High | HR exception list (FR-005), reassignment (FR-006), data-quality check before go-live. |
| Probation end date not reliably maintained for all employees. | Medium | High | Data-quality report before go-live; confirm source column (Q-03). |
| No existing approval hierarchy setup, increasing scope. | Medium | Medium | Confirm Q-15 early; design reuse vs new. |
| Daily job failure goes unnoticed and evaluations start late. | Low | High | Catch-up logic (NFR-AVL-01) and failure alerting (NFR-OPS-01). |
| Approvals stall at a level and evaluation is not completed before probation end. | Medium | Medium | Overdue flag (FR-020); reminders/escalation (Q-18). |

# 9. Assumptions, constraints and dependencies

## 9.1 Assumptions

| ID | Assumption | Needs confirmation from |
|---|---|---|
| A-01 | The current process is manual or not workflow-driven (As-Is in §2). | HR |
| A-02 | "After submission … routed to HR" means after final approval in the hierarchy, not immediately on the evaluator's Submit. | HR (Q-17) |
| A-03 | Proposed status values in RULE-08 are acceptable. | HR (Q-09) |
| A-04 | "15 days" means calendar days. | HR (Q-01) |
| A-05 | Evaluation volume is in the hundreds to low thousands per year. | HR |
| A-06 | Priorities not stated in the request are set as Must for the five points given and Should for inferred items. | SA / HR |
| A-07 | The workflow is built in the existing HRD APEX application and HRD schema. | SA |
| A-08 | The active employee population is up to 15,000 (basis for NFR-PERF-01) (added in v0.2, RV-16). | HR / IT |

## 9.2 Constraints

- Oracle Database / PL/SQL and Oracle APEX in the HRD schema, following HRD naming standards.
- No change to HR's downstream processes (confirmation, extension, termination) in this CR.

## 9.3 Dependencies

- HR to provide the evaluation form content (criteria, rating scale, recommendation values) (Q-05).
- HR to define the approval hierarchy levels for probation evaluations (Q-16).
- HRD schema snapshot to confirm the employee master, probation request and any existing workflow/queue objects (Q-03, Q-15).
- A later CR (payroll/benefits on confirmation) may consume the evaluation Completed event; not in this CR (added in v0.2, RV-19).

# 10. Open questions

| ID | Question | Raised because (M-NN / FR) | Addressed to | Blocking? |
|---|---|---|---|---|
| Q-01 | Are the "15 days" calendar days or working days? If the trigger falls on a holiday, is the queue still generated that day? | M-02, FR-001 | HR | Yes |
| Q-02 | How is the probation evaluation done today (paper form, existing screen, e-mail)? | §2 | HR | No |
| Q-03 | Does a "probation request" record/table already exist in HRD? Where are the probation start and end dates held? | M-08, FR-017 | HR / IT | Yes |
| Q-04 | Who is the "respective supervisor": the reporting manager on the employee's current posting, the HOD, or another field? | M-03, FR-002 | HR / IT | Yes |
| Q-05 | What are the evaluation form fields, criteria, rating scale and recommendation values, and which are mandatory? Does it differ for clinical vs non-clinical staff? | FR-007, FR-009 | HR | Yes |
| Q-06 | What does HR do with the completed evaluation in the system: only acknowledge/close, or record a final decision (confirm / extend / terminate)? | M-07, FR-016 | HR | Yes |
| Q-07 | Can an approver return the evaluation to the evaluator, or reject it outright? After re-submission, does approval restart at Level 1? | M-06, FR-013 | HR | Yes |
| Q-08 | When probation is extended, should a new evaluation be generated 15 days before the new end date? | FR-003 | HR | No |
| Q-09 | Which probation request status values should be used (proposed list in RULE-08)? | M-08, FR-017 | HR | Yes |
| Q-10 | At go-live, should evaluations be created for employees whose probation end date is already within 15 days? | FR-001 | HR | No |
| Q-11 | Should an open evaluation be cancelled automatically if the employee separates or is confirmed early? | FR-004 | HR | No |
| Q-12 | If the supervisor changes after the queue is generated, should the evaluation move to the new supervisor automatically? | FR-006 | HR | No |
| Q-13 | Who attended the meeting / who is the HR business owner? | §1.4 | BA | No |
| Q-14 | What is the CR number for this change? | §1.6 | BA | No |
| Q-15 | Does HRD already have an approval hierarchy setup and a common queue/inbox page that this workflow should reuse? | M-06, FR-011 | IT | Yes |
| Q-16 | What is the approval hierarchy for probation evaluations (levels, roles, by department or by employee grade)? What happens when the evaluator is also an approver? | M-06, FR-011, FR-014 | HR | Yes |
| Q-17 | Does "after submission, routed to HR" mean after final approval, or should HR receive it (for information) as soon as the evaluator submits? | M-07, FR-015 | HR | Yes |
| Q-18 | Are reminders or escalations needed (e.g. 7 and 3 days before probation end) and to whom? | FR-020, NFR-OPS-02 | HR | No |
| Q-19 | What is the retention period for probation evaluation records? | NFR-DAT-01 | HR | No |
| Q-20 | Can the evaluated employee see or acknowledge their evaluation? | §7.3 | HR | No |
| Q-21 | When the evaluator or an approver is on leave or has left, should approval be delegated (to whom), or should HR reassign the level? (added in v0.2, RV-07) | M-06, FR-011 | HR | Yes |
| Q-22 | May the evaluator recall a submitted evaluation before Level 1 acts on it? (added in v0.2, RV-08) | M-05, FR-010 | HR | No |
| Q-23 | How should an employee be handled whose probation is shorter than 15 days, or whose probation end date is less than 15 days away when first recorded? (added in v0.2, RV-18) | FR-001 | HR | No |

# Appendix A. Minutes of meeting breakdown

| M-ID | Original statement | Type | Mapped to |
|---|---|---|---|
| M-01 | "Automated Employee Probation Evaluation" (CR title / objective) | Information | BR-01 |
| M-02 | "The system will automatically generate probation evaluation queue 15 days before the probation end date" | Requirement | BR-01, FR-001, FR-002, FR-003, FR-020, RULE-01, Q-01, Q-10 |
| M-03 | "(Respective Supervisor)" — the queue is for the respective supervisor | Requirement | BR-01, FR-002, FR-005, FR-006, RULE-02, Q-04 |
| M-04 | "The evaluator shall be able to save the evaluation as Draft" | Requirement | BR-02, FR-008, RULE-04, RULE-05 |
| M-05 | "… or Submit it for approval" | Requirement | BR-02, FR-009, FR-010, RULE-05 |
| M-06 | "The system shall route the evaluation through the configured approval hierarchy" | Requirement | BR-03, FR-011–FR-014, RULE-06, RULE-09, Q-07, Q-15, Q-16 |
| M-07 | "After submission, the completed evaluation should automatically be routed to HR Department" | Requirement | BR-04, FR-015, FR-016, RULE-07, Q-06, Q-17 |
| M-08 | "The system should automatically update the probation request status throughout the workflow" | Requirement | BR-05, FR-004, FR-017–FR-019, RULE-08, Q-03, Q-09 |

# Appendix B. Requirement traceability

| Requirement | Source (M-NN) | Impact items (IMP-NN) |
|---|---|---|
| FR-001 | M-02 | IMP-09, IMP-10, IMP-14 |
| FR-002 | M-02, M-03 | IMP-02, IMP-05, IMP-09, IMP-14, IMP-16 |
| FR-003 | M-02 | IMP-09, IMP-21 |
| FR-004 | M-08 | IMP-09, IMP-16 |
| FR-005 | M-03 | IMP-07, IMP-09 |
| FR-006 | M-03 | IMP-07, IMP-09 |
| FR-007 | M-02, M-03 | IMP-05, IMP-06 |
| FR-008 | M-04 | IMP-06, IMP-16, IMP-17 |
| FR-009 | M-05 | IMP-06, IMP-09, IMP-17 |
| FR-010 | M-05 | IMP-06, IMP-09 |
| FR-011 | M-06 | IMP-08, IMP-09, IMP-11, IMP-19, IMP-20 |
| FR-012 | M-06 | IMP-06, IMP-09, IMP-19 |
| FR-013 | M-06 | IMP-06, IMP-09, IMP-19 |
| FR-014 | M-06 | IMP-09 |
| FR-015 | M-07 | IMP-01, IMP-07, IMP-09 |
| FR-016 | M-07, M-08 | IMP-07, IMP-09 |
| FR-017 | M-08 | IMP-09, IMP-15, IMP-16 |
| FR-018 | M-08 | IMP-06, IMP-18 |
| FR-019 | M-08 | IMP-01, IMP-07 |
| FR-020 | M-02 | IMP-07 |
| NFR-SEC-01, NFR-SEC-02 | Inferred | IMP-12 |
| NFR-AUD-01, NFR-AUD-02 | M-08 / Inferred | IMP-16, IMP-18 |
| NFR-AVL-01, NFR-OPS-01 | Inferred | IMP-10 |
| NFR-OPS-02 | Inferred | IMP-13 |
| NFR-PERF-01 | Inferred | IMP-10 |
| NFR-PERF-02 | Inferred | IMP-05, IMP-06, IMP-07 |
| NFR-AVL-02 | Inferred | none (release process) |
| NFR-DAT-01 | Inferred | IMP-16, IMP-18 |
| NFR-DAT-02 | Inferred | IMP-21 |
| NFR-DAT-03 | Inferred (RV-09) | IMP-06, IMP-09 |
| NFR-USA-01, NFR-USA-02 | Inferred | IMP-06, IMP-07 |
| NFR-CMP-01 | Inferred | none (policy sign-off) |
| NFR-INT-01 | Inferred | IMP-14 |
