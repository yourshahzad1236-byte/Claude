# Change Request: Automated Employee Probation Evaluation

| Item | Value |
|---|---|
| CR No. | CR-2026-XXX-PEV (placeholder: real CR number to be assigned) |
| Module / Schema | HR (HRD), Oracle APEX |
| Requested by | HR Department |
| Prepared by | Claude (AI draft) for Business Analyst |
| Version / Status | 0.1 / DRAFT |
| Date | 09-Oct-2026 |
| Detailed reference | CR-2026-XXX-PEV_SRS_v0.3 (requirements, acceptance criteria, impact analysis), SRS-Review_v2 |

# 1. Client Needs / Expectations

HR wants the employee probation evaluation to run automatically, on time and with full visibility, without manual follow-up:

1. Every employee on probation is evaluated by their **respective supervisor** before the probation end date. The system starts the evaluation automatically **15 days before** the probation end date.
2. The evaluator can work on the evaluation over more than one sitting (**Save as Draft**) and send it when ready (**Submit for approval**).
3. Every submitted evaluation goes through the **configured approval hierarchy** (for example HOD, then Director).
4. Once approved, the completed evaluation reaches the **HR Department** automatically.
5. HR and supervisors can see the **current status** of every probation evaluation at any time. The status updates itself at each step.

**Expected benefits:** no missed or late evaluations, a consistent approval path, no manual chasing by HR, and an audit trail of who did what and when.

**Today (from the HRD system):** probation-expiry alerts (alert 001, `HRD.HR_ALERT_QUEUE`) go to **HR users only**, and HR records the confirm/extend decision on form S07FRM00362. Supervisors have no system task, and the evaluation is not routed through approvals.

# 2. Workflow

![Probation evaluation workflow](CR-2026-XXX-PEV_Workflow.png)

*Editable source: `CR-2026-XXX-PEV_Workflow.svg`.*

| Step | Actor | Action | System result | Status after step |
|---|---|---|---|---|
| 1 | System (daily job) | Finds employees whose probation end date is within 15 days and who have no evaluation yet | Creates an evaluation queue item for the respective supervisor and notifies them | Evaluation Pending |
| 2a | Supervisor (evaluator) | Fills part of the form and clicks **Save as Draft** | Saves; the item stays in the supervisor's queue | Draft |
| 2b | Supervisor | Completes the form and clicks **Submit** | Validates mandatory fields and routes to Level 1 | Pending Approval – Level 1 |
| 3a | Approver (Level n) | **Approve** | Moves to the next level | Pending Approval – Level n+1 |
| 3b | Approver | **Return** with comments | Back to the supervisor for correction | Returned |
| 4 | System | Last level approves | Routes to the HR Department queue | Forwarded to HR |
| 5 | HR | Processes the evaluation (confirm / extend, per HR policy) | Closes the evaluation and updates the probation record | Completed |

Status names are proposed and need HR to confirm them.

# 3. Functional Requirements

## Requirement 1: Automatic generation of the probation evaluation queue

**Description:** Every day, the system shall identify each employee on probation whose probation end date is within the next 15 days and who has no evaluation for the current probation period. For each one, it shall create a probation evaluation queue item assigned to the employee's respective supervisor.

- One evaluation only per employee per probation period. A re-run never creates a duplicate.
- If a day's run is missed, the next run picks up the employees that were missed.
- If the employee has no supervisor on record, the item goes to an **HR exception list**. HR can assign or reassign the evaluator.
- If the employee leaves (separation) before HR completes the evaluation, the evaluation is cancelled.
- The supervisor is notified by e-mail when an item is assigned.
- Probation end date: taken from the probation record (`HRD.F_PROBATION_END_DATE`). Respective supervisor: `HRD.INFORMATION.MANAGER_MRNO` (to be confirmed by HR).

**Acceptance (summary):**
- An employee whose probation ends on 25-Oct-2026 appears in their supervisor's queue on 10-Oct-2026.
- An employee whose probation ends on 26-Oct-2026 does not appear in the queue on 10-Oct-2026.
- An employee who has been confirmed or has left never appears in the queue.

*Traceability: FR-001 – FR-006, RULE-01 – RULE-03.*

### Prototype: Supervisor pending tasks (queue)

```
+--------------------------------------------------------------------------------+
| My Pending Tasks                                          [Search........] (Go)|
+--------------------------------------------------------------------------------+
| Task                         | Employee            | Dept     | Prob. End  | Due  |
|------------------------------|---------------------|----------|------------|------|
| Probation Evaluation         | EMP-TEST-0001  Ali  | Nursing  | 25-Oct-2026| 15 d |
| Probation Evaluation (Draft) | EMP-TEST-0002  Sara | Pharmacy | 18-Oct-2026|  8 d |
| Probation Eval. (RETURNED)   | EMP-TEST-0003  Omar | Radiology| 14-Oct-2026|  4 d |
+--------------------------------------------------------------------------------+
| Row click -> opens Probation Evaluation form                                   |
+--------------------------------------------------------------------------------+
```

## Requirement 2: Evaluation entry with Save as Draft / Submit

**Description:** The system shall let the assigned evaluator open the evaluation from the queue and fill in the evaluation form.

- The form shows the employee's details: employee no., name, department, designation, joining date, probation start and end dates.
- **Save as Draft:** saves without validation and without routing. Only the evaluator can see a Draft.
- **Submit:** checks that all mandatory fields are filled. If any are missing, it blocks submission and highlights them. Otherwise it routes the evaluation to approval (Requirement 3).
- After Submit the form is **read-only** for the evaluator, unless an approver returns it.
- The form content (criteria, rating scale and recommendation values such as Confirm / Extend / Terminate) comes from HR's form design (**pending from HR**).
- A warning appears if the user leaves the page with unsaved changes. If another user changed the evaluation after it was opened, the save is rejected with "Changed by another user, reload".

**Acceptance (summary):**
- A Draft is saved and reopens with all values intact.
- Submit with a mandatory field empty is refused, and the status does not change.
- A user who is not the evaluator cannot open the form.

*Traceability: FR-007 – FR-010, RULE-04, RULE-05, NFR-DAT-03.*

### Prototype: Probation Evaluation form

```
+--------------------------------------------------------------------------------+
| Probation Evaluation                         Status: DRAFT    Eval No: PEV-000123|
+--------------------------------------------------------------------------------+
| Employee : EMP-TEST-0001  Ali Raza        Designation: Staff Nurse             |
| Dept     : Nursing                        Joining    : 26-Apr-2026             |
| Probation: 26-Apr-2026 to 25-Oct-2026     Evaluator  : EMP-TEST-0100           |
+--------------------------------------------------------------------------------+
| Evaluation Criteria (from HR template)        Rating (1-5)    Remarks          |
|  1. Job knowledge                    *        [ 4 v ]         [............]   |
|  2. Quality of work                  *        [ 3 v ]         [............]   |
|  3. Punctuality & attendance         *        [ 5 v ]         [............]   |
|  4. Teamwork & communication         *        [ 4 v ]         [............]   |
+--------------------------------------------------------------------------------+
| Recommendation *  ( ) Confirm   ( ) Extend probation   ( ) Not to confirm      |
| Extend by (days)  [ .... ]   (enabled only for Extend)                         |
| Evaluator comments [................................................]          |
| Attachments        [Choose file]                                               |
+--------------------------------------------------------------------------------+
| Approval history / comments (read-only)                                        |
+--------------------------------------------------------------------------------+
|                                  [ Save as Draft ]  [ Submit ]  [ Cancel ]     |
+--------------------------------------------------------------------------------+
  * = mandatory on Submit only
```

## Requirement 3: Routing through the configured approval hierarchy

**Description:** On Submit, the system shall route the evaluation to the approval hierarchy configured for probation evaluations, one level at a time in order.

- **Approve** (optional comments): moves the evaluation to the next level.
- **Return** (comments mandatory): sends it back to the evaluator (status Returned). The evaluator corrects it and re-submits.
- No one approves their own case. If the evaluator is also the approver at a level, that level is skipped and the reason is logged. If there is no next level, the evaluation goes to the HR exception list.
- If an approver's level cannot be resolved, the evaluation goes to the HR exception list. It is never lost.
- **Approver on leave:** the evaluation goes to their acting-for person (`HRD.ACTING_FOR`), to be confirmed by HR.
- The hierarchy levels (for example L1 = HOD, L2 = Director, by department or grade) are maintained by the HR Administrator. **The levels are pending from HR.**
- **Recommended approach:** reuse the existing HRD appraisal routing engine (`PA_HIERARCHY`, `PA_PERFORM_APPRAISER`, `PKG_PERFORMANCE_APPRAISAL`), which already supports Recommend / Approve / Final / Send-back and acting-for. The final decision is made at the design stage.

**Acceptance (summary):**
- After Level 1 approves, the evaluation appears in the Level 2 queue and leaves the Level 1 queue.
- A Return without comments is refused.
- The evaluated employee never receives their own evaluation in their queue.

*Traceability: FR-011 – FR-014, RULE-06, RULE-09.*

### Prototype: Approver screen and hierarchy setup

```
+--------------------------------------------------------------------------------+
| Probation Evaluation - Approval       Status: PENDING APPROVAL - LEVEL 1 (HOD) |
+--------------------------------------------------------------------------------+
| [ Evaluation form shown read-only, as in Requirement 2 ]                       |
+--------------------------------------------------------------------------------+
| Routing:  L1 HOD Nursing (you) -> L2 Director Nursing -> HR                    |
| Approver comments [..........................................................] |
|                                    [ Approve ]   [ Return to Evaluator ]       |
+--------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------+
| Probation Approval Hierarchy Setup  (HR Administrator)                         |
+--------------------------------------------------------------------------------+
| Department / Grade | Level | Approver role        | Active |                   |
|--------------------|-------|----------------------|--------|                   |
| Nursing            |   1   | Head of Department   |   Y    |                   |
| Nursing            |   2   | Director Nursing     |   Y    |                   |
| (All)              |   1   | Head of Department   |   Y    |   [Add] [Save]    |
+--------------------------------------------------------------------------------+
```

## Requirement 4: Automatic routing of the completed evaluation to HR

**Description:** When the last approval level approves, the system shall route the completed evaluation to the HR Department queue automatically. HR shall be able to process it and close it.

- HR sees the complete evaluation, the recommendation and the full approval trail.
- HR records the outcome (Confirm / Extend, per HR policy) and closes the evaluation (status Completed).
- **Important (from the HRD code):** the probation record (`HRD.EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS`) is set to **Confirmed ('C') only at this HR step**. Setting 'C' automatically:
  - sets `HRD.INFORMATION.CONFIRMATION_DATE`;
  - creates incentive/allowance queue entries;
  - clears the HR probation alert.
- An extension updates the probation period instead (reason from `HRD.PROBATION_REASONS`).
- **To be confirmed with HR:**
  - Does "after submission" mean after final approval (assumed here), or should HR see it as soon as the supervisor submits?
  - Does this replace the current alert 001 / form S07FRM00362 process?

**Acceptance (summary):**
- After the last-level approval, the evaluation appears in the HR queue with status Forwarded to HR.
- HR cannot process an evaluation that is still pending approval.
- Confirmation date and incentives change only after HR confirms.

*Traceability: FR-015, FR-016, RULE-07, IMP-15, IMP-34.*

### Prototype: HR queue and decision

```
+--------------------------------------------------------------------------------+
| HR - Completed Probation Evaluations                                           |
+--------------------------------------------------------------------------------+
| Employee           | Dept     | Prob. End  | Recommendation | Approved by | Act |
|--------------------|----------|------------|----------------|-------------|-----|
| EMP-TEST-0001 Ali  | Nursing  | 25-Oct-2026| Confirm        | L2 Director | [>] |
| EMP-TEST-0004 Hina | Admin    | 30-Oct-2026| Extend 90 days | L1 HOD      | [>] |
+--------------------------------------------------------------------------------+

+--------------------------------------------------------------------------------+
| HR Decision - EMP-TEST-0001                     Status: FORWARDED TO HR        |
+--------------------------------------------------------------------------------+
| [ Evaluation + approval trail, read-only ]                                     |
| HR decision *   ( ) Confirm   ( ) Extend   ( ) Other (per HR policy)           |
| Extension days  [ .... ]   Reason [ LOV: Probation Reasons v ]                 |
| HR remarks      [..........................................................]   |
|                                         [ Complete ]   [ Cancel ]              |
+--------------------------------------------------------------------------------+
```

## Requirement 5: Automatic status update throughout the workflow

**Description:** The system shall update the evaluation / probation request status automatically at every workflow event. Users cannot edit the status by hand. Every change is kept in an insert-only history.

- Status values (proposed): Evaluation Pending → Draft → Pending Approval – Level n → Returned → Forwarded to HR → Completed, plus Cancelled.
- History records the old status, new status, action, comments, user and date-time.
- HR has a **monitoring screen** of all evaluations, with filters by status, department, evaluator and end date. It flags evaluations as **overdue** when they are not with HR by the probation end date.
- Supervisors and approvers see the status of their own items.

**Acceptance (summary):**
- Submitting a Draft changes the status to Pending Approval – Level 1 with no manual step.
- The history shows each step in time order.
- No user can edit or delete history.

*Traceability: FR-017 – FR-020, RULE-08, RULE-10, NFR-AUD-01/02.*

### Prototype: Monitoring and status history

```
+--------------------------------------------------------------------------------+
| Probation Evaluation Monitoring (HR)                                           |
| Status [All v]  Dept [All v]  Evaluator [.....]  End date [from] - [to]  (Go)  |
+--------------------------------------------------------------------------------+
| Employee          | Prob. End  | Status                 | With          | Flag    |
|-------------------|------------|------------------------|---------------|---------|
| EMP-TEST-0001 Ali | 25-Oct-2026| Pending Approval - L2  | Director Nurs.|         |
| EMP-TEST-0005 Asad| 08-Oct-2026| Draft                  | EMP-TEST-0110 | OVERDUE |
| EMP-TEST-0006 Zoya| 20-Oct-2026| (no supervisor)        | HR exception  | ASSIGN  |
+--------------------------------------------------------------------------------+

 Status history - EMP-TEST-0001
 | Date-time         | From               | To                    | By            | Comments |
 | 10-Oct-2026 02:00 | -                  | Evaluation Pending    | SYSTEM        |          |
 | 12-Oct-2026 10:15 | Evaluation Pending | Draft                 | EMP-TEST-0100 |          |
 | 15-Oct-2026 09:40 | Draft              | Pending Approval - L1 | EMP-TEST-0100 |          |
 | 16-Oct-2026 14:05 | Pending Appr. - L1 | Pending Approval - L2 | EMP-TEST-0200 | Agreed   |
```

# 4. System Interfaces

## Hardware Interfaces

| Interface | Detail |
|---|---|
| End-user devices | Existing hospital desktops/laptops with a supported browser (Chrome / Edge). The screens also work at tablet width (768 px and above). No new hardware is needed. |
| Servers | Existing Oracle Database and APEX/ORDS application servers. No new server. The daily job runs on the existing database scheduler. |
| Mail server | The existing hospital SMTP mail server sends the notification e-mails. No change. |
| Biometric / RFID devices | Not applicable. Attendance devices are not involved. |
| Printers | Optional: print/PDF of the completed evaluation on existing printers. |

## Software Interfaces

| System / object | Direction | Data exchanged | Purpose | Related requirement |
|---|---|---|---|---|
| HRD employee master `HRD.INFORMATION` | Read | Employee no. (`MRNO`), name, department, designation, joining date, supervisor (`MANAGER_MRNO`), active status | Who is on probation and who evaluates them | R1, R2 |
| Probation record `HRD.EMPLOYEE_PROBATION_HISTORY` (+ `F_PROBATION_END_DATE`, `F_PROBATION_YN`) | Read / Write (HR step only) | Probation start/end date, `PROBATION_STATUS` ('C' = Confirmed), period, reason | Eligibility; final confirm/extend | R1, R4, R5 |
| Department setup `DEFINITIONS.DEPARTMENT` | Read | Department head / manager | Resolving approvers | R3 |
| Approval engine `PA_HIERARCHY`, `PA_PERFORM_APPRAISER`, `PKG_PERFORMANCE_APPRAISAL` (recommended reuse) | Read / Write | Levels, routing, approve/return | Approval hierarchy | R3 |
| Delegation `HRD.ACTING_FOR` | Read | Acting-for person and leave dates | Approver on leave | R3 |
| Pending-task framework `HRD.PKG_PENDING_TASKS` / APEX inbox | Write | Queue counts and items per user | Supervisor, approver and HR queues | R1, R3, R4 |
| Alerts / e-mail `HRD.ALERTS`, `HRD.ALERT_RECIPIENTS`, `PKG_HR_ALERTS` | Write | Notification e-mails | Assignment, return and forwarded-to-HR notifications | R1, R3, R4 |
| Existing probation process: alert 001 (`HR_ALERT_QUEUE`), form S07FRM00362 (`PKG_S07FRM00362`, `EVALUATION_ALERT_QUEUE`) | Replace / integrate (HR to decide) | Probation alerts and confirm/extend decision | Avoid duplicate queues and decisions | R1, R4 |
| Payroll / incentives (`PKG_EMP_INCENTIVE`, `EMP_INCENTIVE_QUEUE` via trigger) | Indirect (triggered on confirmation) | Allowance / incentive queue entries | Starts automatically only when HR confirms | R4 |
| Oracle APEX | UI | All screens above | User interface | R1 – R5 |

# 5. Open Points for HR (blocking)

1. Does "after submission" mean HR receives the evaluation after final approval (assumed here), or as soon as the supervisor submits?
2. What are the approval hierarchy levels (by department or by grade)?
3. Evaluation form content: what are the criteria, rating scale and recommendation values, and which fields are mandatory? Please share the current form.
4. Who is the respective supervisor: `MANAGER_MRNO`, the department manager, or the HOD?
5. Does this workflow replace the current alert 001 / form S07FRM00362 process?
6. Are the 15 days calendar days or working days?
7. Can an approver return the evaluation to the evaluator, and does approval then restart at Level 1?
8. When an approver is on leave, should the evaluation go to the acting-for person?

The full list (Q-01 – Q-26) is in SRS v0.3, section 10.
