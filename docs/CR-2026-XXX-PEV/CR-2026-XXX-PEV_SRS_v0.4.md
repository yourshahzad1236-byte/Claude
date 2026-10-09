# 1. Introduction

## 1.1 Purpose

This SRS specifies the Automated Employee Probation Evaluation workflow for the HR module of the HRD system. It covers automatic creation of probation evaluation queue items for supervisors, evaluation entry (Draft or Submit), routing through the configured approval hierarchy, hand-over of completed evaluations to the HR Department, and automatic status updates of the probation request. It is written for the Solution Architect (review and approval), the development team (design and build) and QA (test design).

## 1.2 Background

Employees joining SKMCH serve a probation period. Before the probation end date, the employee's supervisor must evaluate the employee so that HR can decide on confirmation. The requested change automates this: the system starts the evaluation on time, routes it through the approval hierarchy and delivers it to HR, while keeping the probation request status current at every step (M-01 to M-08). How the process is run today (manual forms, e-mail or an existing screen) was not described in the request (Q-02).

## 1.3 Scope

### In scope

- Automatic generation of a probation evaluation queue item for the respective supervisor 15 days before the employee's probation end date (M-02, M-03).
- Evaluation entry by the evaluator with Save as Draft and Submit for approval (M-04, M-05).
- Online evaluation form replacing the Excel form: evaluation criteria and assignments rated 1–5, assessed training needs, reasons/observations with evidence when not recommended (M-09 to M-12, added in v0.4).
- Routing of a submitted evaluation through the configured approval hierarchy (M-06).
- Automatic routing of the completed evaluation to the HR Department (M-07).
- Automatic update of the probation request status throughout the workflow, with status history (M-08).

### Out of scope

- HR's downstream action on the evaluation (confirmation letter, probation extension, termination, payroll/grade changes). Not discussed; HR's exact action on receipt is open (Q-06).
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

(changed in v0.4: confirmed by the user, M-09)

1. A probation-ending alert is e-mailed 15 or 30 days before the probation end date, with an Excel probation evaluation form attached (alert 001 in `HRD.ALERTS` / `HRD.HR_ALERT_QUEUE`).
2. The concerned person fills in the Excel form and sends it back as feedback. Its main sections are: assignments completed during the probationary period rated 1–5; the employee's assessed training needs; and specific reasons and observations with evidence if the employee is not recommended for confirmation.
3. HR records the confirm/extend decision on form S07FRM00362 (`PKG_S07FRM00362`).

Pain points: offline Excel forms, late or missing feedback, no approval routing, evidence not kept with the record, and no status tracking.

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
| BR-06 | Probation evaluations shall be captured online (standard criteria and assignments rated 1–5, assessed training needs, and evidence-based reasons when not recommended for confirmation), replacing the Excel form. | M-09, M-10, M-11, M-12, M-13 | Must |

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

**Description:** The system shall allow the evaluator to submit a completed evaluation for approval after validating that all mandatory fields are filled: every mandatory criterion rated, at least one assignment with a rating, a recommendation, and, when the employee is not recommended for confirmation, the reasons and observations with at least one evidence attachment (changed in v0.4).
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

### FR-021 Record assignments completed during probation

**Description:** The system shall allow the evaluator to add, edit and remove the assignments completed by the employee during the probationary period, rate each assignment from 1 (Very Low) to 5 (Very High) with optional remarks, and shall calculate the total score, obtained score and performance %.
**Priority:** Must
**Source:** M-10 (added in v0.4)
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given an evaluation in Draft, when the evaluator adds three assignments rated 5, 4 and 3, then total score = 15, obtained score = 12 and performance % = 80.00.
- AC2 (negative): Given an assignment without a rating, when the evaluator clicks Submit, then submission is refused and the rating cell is highlighted.
- AC3 (negative): Given an evaluation with no assignments, when the evaluator clicks Submit, then submission is refused with "At least one assignment is required".

### FR-022 Record assessed training needs

**Description:** The system shall allow the evaluator to record one or more assessed training needs of the employee, each with optional remarks, and shall show them to approvers and HR.
**Priority:** Must
**Source:** M-11 (added in v0.4)
**Business rules:** -
**Acceptance criteria:**
- AC1: Given an evaluation in Draft, when the evaluator adds two training needs and saves, then both are shown on the Training Needs tab to the evaluator, the approvers and HR.
- AC2 (negative): Given a submitted evaluation, when the evaluator tries to edit a training need, then the tab is read-only (unless the evaluation is returned).

### FR-023 Reasons, observations and evidence when not recommended for confirmation

**Description:** The system shall require the evaluator to enter specific reasons and observations and to attach at least one evidence document when the recommendation is Extend Probation or Not to Confirm.
**Priority:** Must
**Source:** M-12 (added in v0.4)
**Business rules:** RULE-12
**Acceptance criteria:**
- AC1: Given the recommendation is Extend Probation, when the evaluator enters reasons and attaches an attendance record, then Submit succeeds and approvers and HR can open the evidence.
- AC2 (negative): Given the recommendation is Not to Confirm and no evidence is attached, when the evaluator clicks Submit, then submission is refused with "Reasons, observations and evidence are required when the employee is not recommended for confirmation".
- AC3: Given the recommendation is Confirm, when the evaluator submits without reasons or evidence, then Submit succeeds.

### FR-024 Rate standard evaluation criteria

**Description:** The system shall show the active evaluation criteria (parameter and description, maintained by HR) on the Evaluation Criteria tab, require the evaluator to rate each mandatory criterion from 1 (Very Low) to 5 (Very High) with optional remarks, and include these ratings in the evaluation score.
**Priority:** Must
**Source:** M-13 (added in v0.4)
**Business rules:** RULE-05, RULE-13
**Acceptance criteria:**
- AC1: Given six active criteria, when the evaluator rates them 5, 3, 5, 4, 4, 5, then the tab shows total score 30, obtained score 26 and performance 86.67 %.
- AC2 (negative): Given a mandatory criterion without a rating, when the evaluator clicks Submit, then submission is refused and the parameter is highlighted.
- AC3: Given HR deactivates a criterion, when a new evaluation is created, then that criterion is not shown; existing evaluations keep their ratings.

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
| RULE-11 | `EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS = 'C'` is written only when HR finalizes a confirmation (it fires the incentive, confirmation-date and alert triggers); an extension updates the probation period instead (added in v0.4). | FR-016, FR-017 | Inferred (schema) |
| RULE-12 | When the recommendation is Extend Probation or Not to Confirm, specific reasons and observations and at least one evidence attachment are mandatory on Submit (added in v0.4). | FR-009, FR-023 | M-12 |
| RULE-13 | Overall score uses every rated item: total = (criteria + assignments) × 5, obtained = sum of ratings, performance % = obtained ÷ total × 100 (added in v0.4). | FR-021, FR-024 | M-10, M-13 |

## 7.2 Data requirements

| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
|---|---|---|---|---|---|
| Evaluation number | Unique reference of the evaluation | Yes (system) | System generated | PEV-2026-000123 | FR-002 |
| Employee | Employee being evaluated | Yes (system) | Must be on probation at generation | EMP-TEST-0001 | FR-001, FR-002 |
| Probation start / end date | Probation period evaluated | Yes (system) | From employee record; end ≥ start | 26-Apr-2026 / 25-Oct-2026 | FR-001 |
| Evaluator | Assigned supervisor | Yes | Active employee, not the evaluated employee | EMP-TEST-0100 | FR-002, FR-006 |
| Criterion ratings | Rating 1–5 per standard evaluation criterion maintained by HR (added in v0.4) | Yes on Submit (mandatory criteria) | 1–5; remarks ≤ 1,000 | Job Knowledge – 5 | FR-024 |
| Assignments completed | Assignments completed during probation, each rated 1–5 (changed in v0.4) | Yes on Submit (≥ 1 row, rating per row) | Text ≤ 500; rating 1–5 | Ward admission documentation – 5 | FR-021 |
| Assessed training needs | Training needs identified by the evaluator (added in v0.4) | No | Text ≤ 500 per row | ACLS certification | FR-022 |
| Reasons and observations | Why the employee is not recommended (added in v0.4) | Yes if recommendation E or N | Text ≤ 4,000 | 6 unplanned absences … | FR-023 |
| Evidence | Supporting documents (added in v0.4) | Yes (≥ 1) if recommendation E or N | Attachment + description | attendance_record.pdf | FR-023 |
| Evaluator recommendation | Confirm / Extend / Terminate (values to be confirmed) | Yes on Submit | From LOV (Q-05) | Confirm | FR-009 |
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

> Schema context used (changed in v0.3): (1) the full DDL exports supplied by the user on 09-Oct-2026: `HRD_SCHEMA.txt`, `DEFINITIONS_SCHEMA.txt`, `PAYROLL_SCHMA.txt`, `HIS.txt`, `REGISTRATION.txt` (tables, triggers, views, package specs **and bodies**); (2) the schema summary `schema/skm/*.md`. "Code-verified" below means the package body or trigger source was read. APEX applications are **not** in the export, so APEX pages stay `Likely` or `PROVISIONAL`.

**Key finding (v0.3):** HRD already has most of the building blocks this CR needs: a probation record with status (`HRD.EMPLOYEE_PROBATION_HISTORY`), a probation-expiry pending task (`HRD.PKG_PENDING_TASKS.PROBATION_EXPIRE_QUEUE`), an evaluation alert/confirmation queue (`HRD.EVALUATION_ALERT_QUEUE`, `HRD.EMPLOYEE_EVALUATION_HISTORY`), an acting-for/delegation table (`HRD.ACTING_FOR`) and a configurable performance-appraisal engine with templates, hierarchy, multi-level routing, send-back and HR distribution (`HRD.PA_*`, `HRD.PKG_PERFORMANCE_APPRAISAL`). The design stage must decide between **Option A: configure a new PA type "Probation Evaluation" on the existing PA engine** and **Option B: new probation-evaluation tables (IMP-16 to IMP-20)**. Q-26 records this.

## 8.1 Business impact

| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
|---|---|---|---|---|
| IMP-01 | HR Department: probation management process | Manual tracking of due evaluations is replaced by the system queue and monitoring view. The SOP needs updating. The existing probation-expiry queue and evaluation alert process (IMP-22, IMP-28) change or are replaced. | FR-001, FR-015, FR-019 | N |
| IMP-02 | All departments: supervisors | New queue task 15 days before each subordinate's probation end. Training and communication needed. | FR-002, FR-008, FR-009 | N |
| IMP-03 | Approvers (HODs and above) | New approval items in their queue. If Option A is chosen, they appear alongside performance appraisals. | FR-011, FR-012 | N |
| IMP-04 | Clinical departments | Indirect only: probation outcomes for clinical staff affect staffing. No clinical data is involved. | FR-015 | N (indirect staffing only) |
| IMP-34 | Payroll / incentives | Code-verified: setting `EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS = 'C'` (Confirmed) fires `EMP_INCENTIVE_QUEUE`, which calls `PKG_EMP_INCENTIVE.P_INS_QUEUE` for each eligible allowance, and `EMP_PROBATION_HISTORY_INFO_UPD`, which sets `INFORMATION.CONFIRMATION_DATE = END_DATE + 1`. Writing 'C' anywhere except the HR completion step would confirm the employee and start incentives early (added in v0.3). | FR-016, FR-017 | N |

## 8.2 System impact

| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|
| IMP-05 | Pending-task (queue) framework `HRD.PKG_PENDING_TASKS` and the APEX inbox page that shows it | Modify | Add a probation-evaluation queue procedure that follows the framework's standard signature (`P_USER_MRNO, P_ACTING_FOR, P_OBJECT_CODE, P_PROCESS_ID, P_TERMINAL, P_EVENT, P_ASSIGNMENT_ID`), as `TRAINING_EXPIRE_QUEUE`, `CONTRACT_EXPIRE_QUEUE` and `PROBATION_EXPIRE_QUEUE` do. The inbox APEX page is not in the export. (changed in v0.3) | FR-002, FR-007, FR-011 | HRD_SCHEMA.md: `PKG_PENDING_TASKS` spec | Confirmed in schema (package spec); APEX page Likely |
| IMP-06 | APEX page "Probation Evaluation" | NEW (proposed) or reuse PA template page | Option A: a PA template whose `PA_DEF_TEMPLATE.APEX_OBJECT_CODE` points to the evaluation page. Option B: a new page. Either way the page has Save as Draft / Submit, approval actions and a history region. | FR-007 – FR-014, FR-018 | HRD_SCHEMA.md: `PA_DEF_TEMPLATE` | Likely |
| IMP-07 | APEX page "Probation Evaluation Monitoring" | NEW (proposed) | HR list with filters, overdue flag, exception list and reassignment. | FR-005, FR-006, FR-016, FR-019, FR-020 | None (APEX not in export) | PROVISIONAL – not verified |
| IMP-08 | Approval hierarchy setup | Reuse (Option A) / NEW (Option B) | Option A: the PA hierarchy setup (`HRD.PA_HIERARCHY`) and its existing setup screen. Option B: a new setup page. (changed in v0.3) | FR-011 | HRD_SCHEMA.md: `PA_HIERARCHY` | Confirmed in schema (table); page Likely |
| IMP-09 | Package `HRD.PKG_PROBATION_EVALUATION` | NEW (proposed) | Orchestration: queue generation (`P_GENERATE_EVAL_QUEUE`), save, submit, status update and history. Under Option A it calls `PKG_PERFORMANCE_APPRAISAL` for routing. | FR-001 – FR-018 | None (new) | NEW (proposed) |
| IMP-10 | Daily queue-generation job | NEW (proposed) or configure the alert framework | Either a new DBMS_SCHEDULER job, or a row in `HRD.ALERTS` (`EXECUTION_UNIT`, `EXECUTE_JOB`, `PENDING_QUEUE`, `DAY_GAP`) using the existing alert job. (changed in v0.3) | FR-001, NFR-AVL-01, NFR-OPS-01 | HRD_SCHEMA.md: `ALERTS` | Confirmed in schema (table) |
| IMP-11 | `HRD.PKG_PERFORMANCE_APPRAISAL` | Read-only / reuse (Option A) | Existing routing and finalisation: `SET_HIERARCHY`, `SET_EMP_PERFORM_HIERARCHY`, `P_UPDATE_QUEUE`, `P_FINALIZE_APPRAISAL`, `SET_ROUTING_AS_PREVIOUS` (send back), `SET_ROUTING_AS_LEAVE` / `SET_EMP_ROUTING_AS_LEAVE` (approver on leave), `MOVE_TO_DEPARTMENT`. (changed in v0.3) | FR-011 – FR-015 | HRD_SCHEMA.md: package spec | Confirmed in schema (package spec) |
| IMP-12 | APEX authorization schemes | NEW / Modify | Checks for Evaluator, Approver, HR User and HR Administrator. | NFR-SEC-01 | None (APEX not in export) | PROVISIONAL – not verified |
| IMP-13 | E-mail notifications | Read-only / configure | Existing alert e-mail configuration in `HRD.ALERTS` (`SUBJECT`, `MAIL_TO_DEPT_HEAD`) and `HRD.ALERT_RECIPIENTS`. Trigger `SEND_EMAIL_SUBSTITUTE` on `ACTING_FOR` shows an e-mail mechanism exists. (changed in v0.3) | NFR-OPS-02 | HRD_SCHEMA.md: `ALERTS`, `ALERT_RECIPIENTS`, `ACTING_FOR` | Confirmed in schema (tables); mail package Likely |
| IMP-22 | Existing probation-expiry alert: alert `'001'` in `HRD.ALERTS`, generated by `PKG_HR_ALERTS.JOB_HR_ALERTS` / `GENRATE_EMAIL_ALERT` / `P_ALERT_QUEUE` into `HRD.HR_ALERT_QUEUE`; counted for **HR users only** by `PKG_PENDING_TASKS.PROBATION_EXPIRE_QUEUE` (rights check `PKG_HR_ALERTS.F_CHECK_HR_ALERT_RIGHTS`); removed by trigger `TR_PROBATION_EXPIRE_QUEUE_DEL` (via `PKG_HR_ALERTS.P_DEL_ALERT_QUEUE`) when `PROBATION_STATUS` becomes 'C' | Modify / Retire (TO BE DECIDED) | The current process alerts HR, not the supervisor. The new supervisor queue either replaces alert 001 or runs alongside it as an HR monitoring alert (Q-24). Code-verified. (added in v0.3) | FR-001, FR-002, FR-003, FR-019 | HRD_SCHEMA.txt: `PKG_HR_ALERTS` body, `PKG_PENDING_TASKS` body, trigger source | Confirmed in schema (code-verified) |
| IMP-23 | Probation functions (code-verified: `F_PROBATION_END_DATE` = `MAX(END_DATE)` from `EMPLOYEE_PROBATION_HISTORY`; `F_PROBATION_YN` delegates to `PKG_COMMON.F_CHECK_EMP_PROBATION_STATUS`): `HRD.F_PROBATION_END_DATE(P_MRNO)`, `HRD.F_PROBATION_YN`, `HRD.F_PROBATION_CURRENT_STATUS(P_MRNO, P_EVENT)`, `HRD.F_GET_PROBATION_PERIOD_DAYS`, `PKG_COMMON.F_CHECK_EMP_PROBATION_STATUS` / `F_CHECK_EMP_PROBATION` | Read-only (reuse) | Reuse `F_PROBATION_END_DATE` and `F_PROBATION_YN` for RULE-01 and the eligibility check, so the end date is computed the same way everywhere. (added in v0.3) | FR-001, FR-004 | HRD_SCHEMA.md: function headers, `PKG_COMMON` spec | Confirmed in schema (signatures) |
| IMP-24 | Code that reads `EMPLOYEE_PROBATION_HISTORY` (from package bodies): `PKG_COMMON`, `PKG_EMPLOYEE_INFO`, `PKG_EMP_INCENTIVE`, `PKG_HR_ALERTS`, `PKG_HR_DOCUMENT_RECORD`, `PKG_HR_EMPLOYEE_RECORD`, `LEAVE_AUTOMATION`, `EMAILS`; functions `F_PROBATION_CURRENT_STATUS`, `F_GET_PROBATION_PERIOD_DAYS`; view `V_HR_EMP_DOCUMENTS` | Read-only (regression) | Leave rules, incentive and HR-document logic read probation status. They need regression testing if status values or write timing change. (added in v0.3) | FR-017 | HRD_SCHEMA.txt: package bodies | Confirmed in schema (code-verified) |
| IMP-25 | PA views `HRD.VU_PA_PERFORM_QUEUE`, `HRD.VU_PA_ROUTING`, `HRD.VU_PERFORM_VAL_RATING`, `HRD.V_EMP_PROMOTION_REPORT` and `PKG_HR_PA_PENDING_TASK.APPRAISAL_PERFORMANCE_QUEUE` | Modify / regression (Option A only) | These read `PA_PERFORM_APPRAISER` / `PA_HIERARCHY`. Under Option A, probation evaluations would appear in appraisal queues and reports unless they are filtered by PA type. (added in v0.3) | FR-011, FR-019 | HRD_SCHEMA.md: view SQL, package spec | Confirmed in schema |
| IMP-26 | View `HRD.V_HR_EMP_DOCUMENTS` | Read-only (regression) | Reads `EMPLOYEE_EVALUATION_HISTORY` and `EMPLOYEE_EVALUATION_ATTACHMENT` (source `EMPLOYEE_EVALUATION_HISTORY_PROB`). It is affected if these tables are reused. (added in v0.3) | FR-015, FR-018 | HRD_SCHEMA.md: view SQL | Confirmed in schema |

## 8.3 Database impact

| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|
| IMP-14 | `HRD.INFORMATION`: `MRNO` (VARCHAR2(14), PK), `MANAGER_MRNO`, `DEPARTMENT_ID`, `SECTION_ID`, `DESIGNATION_ID`, `JOINING_DATE`, `PROBATION_PERIOD_DAYS` (NUMBER(3)), `CONFIRMATION_DATE`, `ACTIVE` (H/Y/N) | Read-only | Employee master. It is the source of eligibility and of the evaluator (`MANAGER_MRNO`, "manager code of employee", pending Q-04). (changed in v0.3) | Triggers `CURRENT_EMPLOYEE_UPDATE`, `INFORMATION_*`; view `HRD.V_INFORMATION` | None | FR-001, FR-002, FR-007 | HRD_SCHEMA.md `### HRD.INFORMATION` | Confirmed in schema |
| IMP-15 | `HRD.EMPLOYEE_PROBATION_HISTORY`: PK (`MRNO`, `START_DATE`), `END_DATE`, `PROBATION_PERIOD`, `PROBATION_REASON_ID`, `PROBATION_STATUS` VARCHAR2(1) default `'P'` | Read / Modify (status) | Probably the "probation request" (Q-03). It holds one row per probation period, so it can identify the period (RULE-03). Writes to `PROBATION_STATUS` fire triggers. To avoid side effects (IMP-34), `PROBATION_STATUS` should change only at HR completion, and the intermediate workflow status should be kept in the evaluation record (Q-25). (changed in v0.3) | Triggers `EMP_INCENTIVE_QUEUE` (after update of PROBATION_STATUS), `EMP_PROBATION_HISTORY_INFO_UPD` (after update), `TR_PROBATION_EXPIRE_QUEUE_DEL`; FK to `INFORMATION`; `EMPLOYEE_PROBATION_ATTACHMENT` | Map the existing status values (Q-09) | FR-001, FR-003, FR-017 | HRD_SCHEMA.md `### HRD.EMPLOYEE_PROBATION_HISTORY` | Confirmed in schema |
| IMP-16 | Evaluation header: Option A `HRD.PA_PERFORM_MASTER` (`PA_PERFORM_STATUS_ID`, `RESEARCH_DATA_STATUS` 'F' = HR queue) + `HRD.PA_HIERARCHY` (`APPRAISEE_MRNO`, `PA_TYPE_ID`, `HR_DISTRIBUTE`); Option B `HRD_PROBATION_EVAL_MST` NEW (proposed) | Reuse / NEW | One record per evaluation. Under Option A, a link to `EMPLOYEE_PROBATION_HISTORY` (`MRNO`, `START_DATE`) is still needed: either a new column or a small link table (Q-26). (changed in v0.3) | IMP-25 views | Go-live backlog (Q-10) | FR-002 – FR-017 | HRD_SCHEMA.md `PA_PERFORM_MASTER`, `PA_HIERARCHY` | Confirmed in schema (Option A objects) |
| IMP-17 | Evaluation content: Option A `HRD.PA_DEF_TEMPLATE`, `PA_DEF_SECTION`, `PA_DEF_SECTION_PARAMETER`, `PA_DEF_RATING_VALUE`, `PA_PERFORM_SECTION_PARAM`, `PA_PERFORM_VAL_RATING`; Option B `HRD_PROBATION_EVAL_DTL` NEW (proposed) | Reuse (configure data) / NEW | Criteria and ratings. Option A answers Q-05 by configuring a "Probation Evaluation" template. (changed in v0.3) | `VU_PERFORM_VAL_RATING` | Seed template data | FR-008, FR-009 | HRD_SCHEMA.md `PA_*` tables | Confirmed in schema (Option A objects) |
| IMP-18 | `HRD_PROBATION_EVAL_HIS` | NEW (proposed) | Insert-only status history. Needed under both options: PA keeps per-level status and value-text history, but not a full status history. | IMP-16 | None | FR-018, NFR-AUD-02 | None (new) | NEW (proposed) |
| IMP-19 | Approval levels: Option A `HRD.PA_PERFORM_APPRAISER` (`APPRAISER_ROLE` R=Recommend, A=Approve, F=Final, S=Send back; `ORDER_BY`; `PA_STATUS_ID`; `EMPLOYEE_REIVEW`); Option B `HRD_PROBATION_APPROVAL_TRN` NEW (proposed) | Reuse / NEW | Per-level actions and comments. The existing `S` role covers FR-013 (return). (changed in v0.3) | `VU_PA_ROUTING`, `VU_PA_PERFORM_QUEUE` | None | FR-011 – FR-014 | HRD_SCHEMA.md `PA_PERFORM_APPRAISER` | Confirmed in schema (Option A objects) |
| IMP-20 | Hierarchy definition: Option A `HRD.PA_DEF_TYPE` (new type row; `PREVIOUS_ROUTING_HIERARCHY`), `HRD.PA_TYPE_PERIOD`, `HRD.PA_HIERARCHY`; Option B `HRD_PROBATION_HIERARCHY_MST` NEW (proposed) | Reuse (configure) / NEW | Ordered approval levels. `PA_TYPE_PERIOD` is period-based (PA start/end and cut-off dates), while probation evaluations are rolling. The design must confirm that a rolling probation type fits (Q-26). (changed in v0.3) | `PA_HIERARCHY` FKs | Seed hierarchy | FR-011 | HRD_SCHEMA.md `PA_DEF_TYPE`, `PA_TYPE_PERIOD` | Confirmed in schema (Option A objects) |
| IMP-21 | Sequences and unique key on (`MRNO`, probation `START_DATE`) for the evaluation | NEW (proposed) | Keys and RULE-03 enforcement. Option A: PA keys are VARCHAR2 IDs built by `PKG_PERFORMANCE_APPRAISAL.GET_PERFORM_ID` / `GET_HIERARCHY_ID`. | IMP-16 | None | FR-003 | HRD_SCHEMA.md package spec | Likely |
| IMP-27 | Form package `HRD.PKG_S07FRM00362` (`P_GEN_EVALUATION_ALERT_QUEUE`, `P_INSERT_EVALUATION_DATA`, `P_DECISION`, `P_SEND_REMINDER`, `F_GET_EVALUATION_DATE`; also FPPE HOD/proctor routing) with `HRD.EVALUATION_ALERT_QUEUE` (`IS_CONFIRMED` C/E/P/I, `EXTENDED_DAYS`, `CONFIRMED_BY`) and `HRD.EMPLOYEE_EVALUATION_HISTORY` (`EVALUATION_STATUS` C=Completed, E=Extend, P=Pending, I=In process; `EVALUATION_TYPE` → `HRD.ALERTS`) | Read / Modify / Retire (TO BE DECIDED) | An existing evaluation alert and confirmation mechanism, keyed by employee and alert type. Code-verified: `PKG_S07FRM00362` (form S07FRM00362) generates the evaluation alert queue and records the confirm/extend decision, and `PKG_HR_EMPLOYEE_RECORD` reads the history. This is very likely today's evaluation/confirmation screen. It must be replaced or integrated, not duplicated (Q-24). Its C/E/P/I values are a natural basis for the HR outcome (Q-06). (added in v0.3) | `V_HR_EMP_DOCUMENTS`; `EMPLOYEE_EVALUATION_ATTACHMENT` | Possible migration of open rows | FR-015, FR-016, FR-017 | HRD_SCHEMA.txt: `PKG_S07FRM00362` spec/body, table DDL | Confirmed in schema (code-verified) |
| IMP-28 | `HRD.ACTING_FOR` (`EMP_MRNO`, `ACTOR_MRNO`, `LEAVE_FROM_DATE`, `LEAVE_TO_DATE`, `SUBSTITUTE_TYPE`) and `HRD.ACTING_FOR_USER_TASK_WISE` | Read-only | Existing delegation while a superior is on leave. Use it for Q-21 (delegation); `PKG_PENDING_TASKS` procedures already take `P_ACTING_FOR`. (added in v0.3) | Trigger `SEND_EMAIL_SUBSTITUTE` | None | FR-011, FR-012 | HRD_SCHEMA.md | Confirmed in schema |
| IMP-29 | `DEFINITIONS.DEPARTMENT`: `DEPARTMENT_HEAD`, `DEPARTMENT_MANAGER` | Read-only | Approver resolution for an HOD level, and an alternative evaluator source (Q-04). (added in v0.3) | FK to `HRD.INFORMATION` (disabled) | None | FR-011 | DEFINITIONS_SCHEMA.md | Confirmed in schema |
| IMP-30 | `HRD.ALERTS`, `HRD.ALERT_RECIPIENTS` | Modify (configuration data) | New alert row(s) for the probation evaluation trigger and notifications, if the alert framework is used (IMP-10, IMP-13). (added in v0.3) | Alert job (not in export) | Seed rows | FR-001, NFR-OPS-02 | HRD_SCHEMA.md | Confirmed in schema |
| IMP-31 | `HRD.PROBATION_REASONS` | Read-only | Reason codes, for when HR extends probation (Q-08). (added in v0.3) | `EMPLOYEE_PROBATION_HISTORY.PROBATION_REASON_ID` | None | FR-003, FR-016 | HRD_SCHEMA.md | Confirmed in schema |

Volume: one evaluation per probation period, roughly the number of new hires and extensions per year (A-05). Low growth.

**Privacy note (v0.3):** `HRD.INFORMATION.MRNO` has an FK to `REGISTRATION.PATIENT(MRNO)`, so the employee code is also a patient record number. Evaluation screens and reports must not expose patient-registration data or link to it.

## 8.4 Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Intermediate workflow statuses written to `EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS` fire `EMP_INCENTIVE_QUEUE` and `TR_PROBATION_EXPIRE_QUEUE_DEL` early (incentive or salary change, lost expiry queue). | High if not designed for | High | Keep the workflow status in the evaluation record. Write `PROBATION_STATUS = 'C'` only when HR completes a confirmation; an extension updates `END_DATE` / adds a new period instead (Q-25). Run regression on IMP-24. |
| The new queue duplicates the existing `PROBATION_EXPIRE_QUEUE` / `EVALUATION_ALERT_QUEUE`, so supervisors get two items. | High | Medium | Decide replace or extend before design (Q-24). |
| Under Option A, probation evaluations leak into appraisal queues, scores and reports (IMP-25). | Medium | Medium | Filter by PA type in all PA views and packages, and run regression tests. |
| `MANAGER_MRNO` is incomplete or stale, so queues go to the wrong person or nobody. | Medium | High | HR exception list (FR-005), reassignment (FR-006), a data-quality report before go-live. |
| The daily job fails and nobody notices, so evaluations start late. | Low | High | Catch-up logic (NFR-AVL-01) and failure alerting (NFR-OPS-01). |
| Approvals stall at a level. | Medium | Medium | Overdue flag (FR-020), delegation via `ACTING_FOR` (Q-21), reminders (Q-18). |
| APEX pages and Oracle Forms (e.g. S07FRM00362) were not in the schema export, so screen-level dependencies are missed. | Medium | Medium | Export the APEX application and the form list, and re-run the screen dependency check before Gate 2. |

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
| A-09 | The schema export (`schema/skm/`) reflects production. Package bodies and APEX pages were not included in it. (added in v0.3) | IT |
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
| Q-02 | How is the probation evaluation done today (paper form, existing screen, e-mail)? | §2 | HR | No | — **Answered (v0.4):** e-mailed alert 15/30 days before end date with an Excel form (M-09).
| Q-03 | Is `HRD.EMPLOYEE_PROBATION_HISTORY` (one row per probation period, `PROBATION_STATUS` default 'P') the "probation request"? What do its `PROBATION_STATUS` values mean? (changed in v0.3: table found in schema) | M-08, FR-017, IMP-15 | HR / IT | Yes |
| Q-04 | Is the "respective supervisor" `HRD.INFORMATION.MANAGER_MRNO`, or `DEFINITIONS.DEPARTMENT.DEPARTMENT_MANAGER` / `DEPARTMENT_HEAD`? (changed in v0.3: candidates found in schema) | M-03, FR-002, IMP-14, IMP-29 | HR / IT | Yes |
| Q-05 | What are the evaluation form fields, criteria, rating scale and recommendation values, and which are mandatory? Does it differ for clinical vs non-clinical staff? | FR-007, FR-009 | HR | Yes — **Partly answered (v0.4):** sections = assignments rated 1–5, assessed training needs, reasons/observations with evidence (M-10 to M-12). |
| Q-06 | What does HR do with the completed evaluation in the system: only acknowledge/close, or record a final decision (confirm / extend / terminate)? | M-07, FR-016 | HR | Yes |
| Q-07 | Can an approver return the evaluation to the evaluator, or reject it outright? After re-submission, does approval restart at Level 1? | M-06, FR-013 | HR | Yes |
| Q-08 | When probation is extended, should a new evaluation be generated 15 days before the new end date? | FR-003 | HR | No |
| Q-09 | Which probation request status values should be used (proposed list in RULE-08)? | M-08, FR-017 | HR | Yes |
| Q-10 | At go-live, should evaluations be created for employees whose probation end date is already within 15 days? | FR-001 | HR | No |
| Q-11 | Should an open evaluation be cancelled automatically if the employee separates or is confirmed early? | FR-004 | HR | No |
| Q-12 | If the supervisor changes after the queue is generated, should the evaluation move to the new supervisor automatically? | FR-006 | HR | No |
| Q-13 | Who attended the meeting / who is the HR business owner? | §1.4 | BA | No |
| Q-14 | What is the CR number for this change? | §1.6 | BA | No |
| Q-15 | Partly answered in v0.3: HRD has the pending-task framework `PKG_PENDING_TASKS` and the PA hierarchy and routing engine (`PA_HIERARCHY`, `PA_PERFORM_APPRAISER`, `PKG_PERFORMANCE_APPRAISAL`). Remaining question: which APEX inbox page shows pending tasks? | M-06, FR-011, IMP-05, IMP-11 | IT | No |
| Q-16 | What is the approval hierarchy for probation evaluations (levels, roles, by department or by employee grade)? What happens when the evaluator is also an approver? | M-06, FR-011, FR-014 | HR | Yes |
| Q-17 | Does "after submission, routed to HR" mean after final approval, or should HR receive it (for information) as soon as the evaluator submits? | M-07, FR-015 | HR | Yes |
| Q-18 | Are reminders or escalations needed (e.g. 7 and 3 days before probation end) and to whom? | FR-020, NFR-OPS-02 | HR | No |
| Q-19 | What is the retention period for probation evaluation records? | NFR-DAT-01 | HR | No |
| Q-20 | Can the evaluated employee see or acknowledge their evaluation? | §7.3 | HR | No |
| Q-21 | When the evaluator or an approver is on leave or has left, should approval go to their acting-for person (`HRD.ACTING_FOR`, as `PKG_PERFORMANCE_APPRAISAL.SET_ROUTING_AS_LEAVE` does for appraisals), or should HR reassign the level? (added in v0.2, RV-07; changed in v0.3) | M-06, FR-011, IMP-28 | HR | Yes |
| Q-22 | May the evaluator recall a submitted evaluation before Level 1 acts on it? (added in v0.2, RV-08) | M-05, FR-010 | HR | No |
| Q-23 | How should an employee be handled whose probation is shorter than 15 days, or whose probation end date is less than 15 days away when first recorded? (added in v0.2, RV-18) | FR-001 | HR | No |
| Q-24 | Today, alert 001 (`HR_ALERT_QUEUE`) shows probation expiries to HR, and form S07FRM00362 (`PKG_S07FRM00362`, `EVALUATION_ALERT_QUEUE`) records the confirm/extend decision. Should the new supervisor workflow replace these, feed them, or run alongside? (added in v0.3) | FR-001, FR-015, IMP-22, IMP-27 | HR / IT | Yes |
| Q-25 | Code shows `PROBATION_STATUS = 'C'` confirms the employee (sets `CONFIRMATION_DATE`, creates the incentive queue, clears alert 001). Proposal: write 'C' only on HR confirmation; an extension updates the probation period instead. What other `PROBATION_STATUS` values exist besides 'P' and 'C'? (added in v0.3) | FR-017, IMP-15, IMP-34 | IT / HR | Yes |
| Q-26 | Build on the existing PA engine as a new PA type "Probation Evaluation" (Option A), or with new probation tables (Option B)? To be settled at the design stage. (added in v0.3) | FR-007 – FR-016, IMP-16 – IMP-20 | SA | Yes (for design) |

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
| M-09 | "We already have a probation ending alert … 15 or 30 days before the end date … with an Excel attachment … to provide feedback after updating the Excel probation evaluation form" | Information | §2 As-Is, BR-06, RULE-01 |
| M-10 | "ASSIGNMENTS COMPLETED DURING PROBATIONARY PERIOD with ratings from 1 to 5" | Requirement | BR-06, FR-021 |
| M-11 | "Employee's Assessed Training Needs" | Requirement | BR-06, FR-022 |
| M-12 | "List specific reasons and observations along with evidence, if employee has not been recommended for confirmation" | Requirement | BR-06, FR-023, RULE-12 |
| M-13 | "Add 1st tab as evaluation criteria" (screen shared: Parameter, Description, Rating 1–5, Remarks; rating scale; score bar) | Requirement | BR-06, FR-024, RULE-13 |

# Appendix B. Requirement traceability

| Requirement | Source (M-NN) | Impact items (IMP-NN) |
|---|---|---|
| FR-001 | M-02 | IMP-09, IMP-10, IMP-14, IMP-22, IMP-23, IMP-27, IMP-30 |
| FR-002 | M-02, M-03 | IMP-02, IMP-05, IMP-09, IMP-14, IMP-16, IMP-22 |
| FR-003 | M-02 | IMP-09, IMP-21, IMP-15, IMP-22, IMP-31 |
| FR-004 | M-08 | IMP-09, IMP-16 |
| FR-005 | M-03 | IMP-07, IMP-09 |
| FR-006 | M-03 | IMP-07, IMP-09 |
| FR-007 | M-02, M-03 | IMP-05, IMP-06 |
| FR-008 | M-04 | IMP-06, IMP-16, IMP-17 |
| FR-009 | M-05 | IMP-06, IMP-09, IMP-17 |
| FR-010 | M-05 | IMP-06, IMP-09 |
| FR-011 | M-06 | IMP-08, IMP-09, IMP-11, IMP-19, IMP-20, IMP-28, IMP-29, IMP-25 |
| FR-012 | M-06 | IMP-06, IMP-09, IMP-19 |
| FR-013 | M-06 | IMP-06, IMP-09, IMP-19 |
| FR-014 | M-06 | IMP-09 |
| FR-015 | M-07 | IMP-01, IMP-07, IMP-09, IMP-26, IMP-27 |
| FR-016 | M-07, M-08 | IMP-07, IMP-09 |
| FR-017 | M-08 | IMP-09, IMP-15, IMP-16, IMP-15, IMP-24, IMP-27, IMP-34 |
| FR-018 | M-08 | IMP-06, IMP-18 |
| FR-019 | M-08 | IMP-01, IMP-07 |
| FR-020 | M-02 | IMP-07 |
| FR-021 | M-10 | IMP-06, IMP-16, IMP-17 |
| FR-022 | M-11 | IMP-06, IMP-16 |
| FR-023 | M-12 | IMP-06, IMP-16 |
| FR-024 | M-13 | IMP-06, IMP-16, IMP-17 |
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
