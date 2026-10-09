# Design Document: Automated Employee Probation Evaluation

- **CR:** CR-2026-XXX-PEV · **Version:** 0.1 DRAFT (Solution Architect approval pending)
- **Based on:** CR v0.3 and SRS v0.3. **Warning:** the SRS is not yet approved, so this design may change.
- **Schema checked against:** HRD, DEFINITIONS, HIS and PAYROLL DDL exports, including package bodies. APEX applications were not in the export.
- **Approach:** dedicated probation tables plus one new package. Existing HRD objects are reused where they already fit.

# 1. Design Summary

- A **daily job** finds employees whose probation ends within 15 days and creates an evaluation for each one's supervisor.
- The **supervisor** fills in the evaluation (criteria ratings and a recommendation), then either saves it as a Draft or submits it.
- On Submit, the evaluation goes through the **approval levels** set up per department (HOD, then Director, and so on). Each approver can approve it or return it.
- After the last approval, it goes to **HR**, who finalize it as Confirm or Extend. Only at this step is the existing probation record updated.
- **Every status change is logged.** HR can see every evaluation on a monitoring screen.

# 2. Key Design Decisions

- **DS-D1 Dedicated tables, not the PA appraisal engine.** This keeps probation separate from the appraisal queues and reports, so `VU_PA_*` and `PKG_PERFORMANCE_APPRAISAL` are not affected.
- **DS-D2 Workflow status kept in the new table, not in `EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS`.** Writing `'C'` to that column fires three triggers:
  - `EMP_INCENTIVE_QUEUE`, which creates incentive/allowance queue entries;
  - `EMP_PROBATION_HISTORY_INFO_UPD`, which sets `INFORMATION.CONFIRMATION_DATE`;
  - `TR_PROBATION_EXPIRE_QUEUE_DEL`, which clears alert 001.

  So `'C'` is written **only at HR finalize**.
- **DS-D3 All logic lives in `HRD.PKG_PROBATION_EVALUATION`.** APEX pages only call package procedures.
- **DS-D4 Queues use the existing pending-task framework:** a new procedure in `HRD.PKG_PENDING_TASKS`, registered in `HIS.USER_ASSIGNMENT`. Items then appear in the existing inbox.
- **DS-D5 Optimistic locking:** a `VERSION_NO` column on the header. Every action passes the version it read; a mismatch raises an error.
- **DS-D6 Approver on leave:** the approval goes to the acting-for person from `HRD.ACTING_FOR`, which already exists.
- **DS-D7 Existing process (alert 001 and form S07FRM00362):** stays as it is until HR decides. The design does not change it.

# 3. DB Structure

![ER diagram](CR-2026-XXX-PEV_ERD.png)

**New tables.** All follow the HRD audit-column pattern (`USER_ID`, `TERMINAL`, `TRN_DATE`, `ORIGINAL_*`, `ORG_ID`/`ZON_ID`/`LOC_ID`) and are filled by triggers.

- **DS-01 `HRD.HRD_PROBATION_EVAL_MST`**: evaluation header, one row per evaluation.
  - **Keys:**
    - `PROBATION_EVAL_ID` NUMBER(12) is the PK.
    - `EVAL_NO` VARCHAR2(20) is unique, in the form `PEV-YYYY-NNNNNN`.
    - `MRNO` VARCHAR2(14) + `PROB_START_DATE` is an FK to `EMPLOYEE_PROBATION_HISTORY`.
  - **Who and where:** `PROB_END_DATE`, `DEPARTMENT_ID` VARCHAR2(7), `EVALUATOR_MRNO` (NULL = HR exception list).
  - **Workflow:** `EVAL_STATUS` VARCHAR2(2) (EP / DR / PA / RT / FH / CM / CN), `CURRENT_LEVEL_NO`, `CURRENT_APPROVER_MRNO`.
  - **Evaluation:**
    - `RECOMMENDATION` (C = Confirm / E = Extend / N = Not to confirm), `EXTEND_DAYS`, `EVALUATOR_COMMENTS` VARCHAR2(4000).
    - `TOTAL_SCORE`, `OBTAINED_SCORE`, `PERFORMANCE_PCT`.
    - `DOCUMENT_ID` for the attachment, and `SUBMITTED_DATE`.
  - **HR decision:** `HR_DECISION` (C / E / O), `HR_EXTEND_DAYS`, `EXTENSION_REASON_ID` (FK to `PROBATION_REASONS`), `HR_DECISION_BY`, `HR_DECISION_DATE`, `HR_REMARKS`.
  - **Control:** `EXCEPTION_REASON`, and `VERSION_NO` for locking.
  - **One active evaluation per probation period** is enforced by the unique index `IDX_PROB_EVAL_ACTIVE_UK`, which ignores cancelled rows.
- **DS-02 `HRD.HRD_PROBATION_CRITERIA_MST`**: evaluation parameters that HR maintains.
  - Columns: `CRITERIA_ID`, `PARAMETER_NAME`, `DESCRIPTION` VARCHAR2(500), `SORT_ORDER`, `MANDATORY`, `ACTIVE`.
  - The existing `EVALUATION_CRITERIA_MASTER` is too limited to reuse: its description is only VARCHAR2(55).
- **DS-03 `HRD.HRD_PROBATION_EVAL_DTL`**: one rating per criterion.
  - Columns: `PROBATION_EVAL_ID`, `CRITERIA_ID`, `RATING` (1–5), `REMARKS`.
  - Unique on (evaluation, criterion).
- **DS-04 `HRD.HRD_PROBATION_HIERARCHY_MST`**: approval levels.
  - Columns: `DEPARTMENT_ID` (NULL = all departments), `LEVEL_NO`, `APPROVER_SOURCE`, `APPROVER_MRNO`, `ACTIVE`.
  - `APPROVER_SOURCE` is DH (department head), DM (department manager) or EMP (named employee).
- **DS-05 `HRD.HRD_PROBATION_APPROVAL_TRN`**: one row per level per evaluation.
  - Columns: `LEVEL_NO`, `APPROVER_MRNO`, `ACTING_FOR_MRNO`, `ACTION`, `ACTION_DATE`, `COMMENTS`.
  - `ACTION` is P (pending), A (approved), R (returned) or S (skipped). Comments are mandatory on Return.
- **DS-06 `HRD.HRD_PROBATION_EVAL_HIS`**: status history.
  - Columns: `OLD_STATUS`, `NEW_STATUS`, `ACTION`, `ACTION_BY`, `ACTION_DATE`, `COMMENTS`.
  - Insert-only: trigger `TRG_PROBATION_EVAL_HIS_BUD` blocks updates and deletes.
- **DS-07 `HRD.HRD_PROBATION_JOB_LOG`**: daily job log.
  - Columns: `RUN_START`, `RUN_END`, `EMPLOYEES_SCANNED`, `QUEUES_CREATED`, `EXCEPTIONS`, `CANCELLED`, `RUN_STATUS`, `ERROR_MSG`.
- **DS-08 Supporting objects:**
  - 7 sequences (`PROBATION_*_SEQ`).
  - Indexes on every FK and on the main searches: status, evaluator, approver, end date.
  - Audit triggers `TRG_<TABLE>_BI` / `_BU`, copying the existing `EMPLOYEE_PROBATION_HISTORY_INS` pattern (`SECURITY.GET_TERMINAL`, `SECURITY.CURRENTUSER`, `HIS.P_GET_CONTEXT_COL`).

**Existing objects used.**

- **Read:**
  - `HRD.INFORMATION`: `MRNO`, `MANAGER_MRNO` (evaluator), `DEPARTMENT_ID`, `ACTIVE` H/Y/N.
  - `DEFINITIONS.DEPARTMENT`: `DEPARTMENT_HEAD`, `DEPARTMENT_MANAGER`.
  - `HRD.ACTING_FOR`.
  - `HRD.PROBATION_REASONS`.
  - `HRD.F_PROBATION_END_DATE`, which returns MAX(`END_DATE`).
- **Written at HR finalize only:** `HRD.EMPLOYEE_PROBATION_HISTORY`.
  - Confirm sets `PROBATION_STATUS = 'C'`.
  - Extend sets a new `END_DATE` and `PROBATION_REASON_ID`, with `PROBATION_STATUS` staying 'P'.
- **Seed data:** `HIS.USER_ASSIGNMENT` (pending-task registration), `HRD.ALERTS` / `ALERT_RECIPIENTS` (notification set-up).

**Data migration:** none. An optional backlog run at go-live creates evaluations for employees who are already within 15 days of their probation end date.

# 4. Technical Details: Package `HRD.PKG_PROBATION_EVALUATION` (NEW)

All procedures use `%TYPE` parameters. The **caller commits** (an APEX page process or the job).

- **`P_GENERATE_EVAL_QUEUE(P_RUN_DATE IN DATE DEFAULT TRUNC(SYSDATE))`**: the daily job. FR-001 to FR-005.
  1. Write a log row (RUNNING).
  2. Do a set-based insert into `EVAL_MST` for active employees on probation where:
     - `F_PROBATION_END_DATE(MRNO)` is between `P_RUN_DATE` and `P_RUN_DATE + 15`;
     - and there is no non-cancelled evaluation for that `MRNO` and probation start date.

     This also catches up on missed days.
  3. Set the evaluator from `INFORMATION.MANAGER_MRNO`. If it is NULL, set `EXCEPTION_REASON = 'Supervisor not defined'`.
  4. Insert one `EVAL_DTL` row for each active criterion, and one history row (action CREATED).
  5. Cancel open evaluations (status EP/DR/PA/RT) for employees whose `INFORMATION.ACTIVE <> 'Y'`. FR-004.
  6. Queue the notification e-mails, update the log to SUCCESS with counts, and commit. On error: roll back, log FAILED and re-raise.
- **`P_SAVE_DRAFT(P_PROBATION_EVAL_ID, P_VERSION_NO, P_RECOMMENDATION, P_EXTEND_DAYS, P_COMMENTS, P_DOCUMENT_ID)`** and **`P_SAVE_RATING(P_PROBATION_EVAL_ID, P_CRITERIA_ID, P_RATING, P_REMARKS)`**. FR-008.
  - The caller must be the evaluator, and the status must be EP, DR or RT.
  - Sets status DR, recalculates the scores and writes history.
  - Mandatory fields are not checked.
- **`P_SUBMIT(P_PROBATION_EVAL_ID, P_VERSION_NO)`**. FR-009, FR-010, FR-011.
  - Checks that every mandatory criterion is rated, that the recommendation and comments are filled, and that Extend has its days. Otherwise it raises -20801.
  - Sets `SUBMITTED_DATE`, then calls `P_ROUTE(level 1)`.
- **`P_ROUTE(P_PROBATION_EVAL_ID, P_LEVEL_NO)`** (internal). FR-011, FR-014, RULE-09.
  1. Read the active level from `HIERARCHY_MST`, using the department's own row or the default (NULL) row.
  2. Resolve the approver from DH / DM / EMP.
  3. If that approver is on leave, use the `HRD.ACTING_FOR` actor.
  4. If the approver is the evaluator or the employee, insert an S (skipped) row and move to the next level.
  5. If the approver cannot be resolved, place the evaluation on the HR exception list.
  6. If there is no next level, set status FH (Forwarded to HR).
  7. Otherwise set status PA, `CURRENT_LEVEL_NO` and `CURRENT_APPROVER_MRNO`, and insert an `APPROVAL_TRN` row with action P.
- **`P_APPROVE(P_PROBATION_EVAL_ID, P_VERSION_NO, P_COMMENTS)`**. FR-012.
  - The caller must be the current approver or the acting-for person.
  - Marks the level A, then calls `P_ROUTE(level + 1)`.
- **`P_RETURN(P_PROBATION_EVAL_ID, P_VERSION_NO, P_COMMENTS)`**. FR-013.
  - Comments are mandatory (-20803).
  - Marks the level R, sets status RT and clears the current approver.
  - On re-submit, approval restarts at level 1. This is pending HR confirmation (Q-07).
- **`P_ASSIGN_EVALUATOR(P_PROBATION_EVAL_ID, P_EVALUATOR_MRNO)`**: HR Administrator only. FR-005, FR-006.
  - Allowed while the status is EP, DR or RT.
- **`P_HR_FINALIZE(P_PROBATION_EVAL_ID, P_VERSION_NO, P_HR_DECISION, P_HR_EXTEND_DAYS, P_EXTENSION_REASON_ID, P_HR_REMARKS)`**: HR role only, and the status must be FH. FR-015, FR-016, RULE-11.
  - **C (Confirm):** `UPDATE EMPLOYEE_PROBATION_HISTORY SET PROBATION_STATUS = 'C'` for that `MRNO` and start date. The existing triggers then set the confirmation date, queue incentives and clear alert 001.
  - **E (Extend):** update `END_DATE = END_DATE + days` and `PROBATION_REASON_ID`. This is pending HR's choice between extending the current period and adding a new one (Q-08).
  - **O (Other):** no change to the probation record.
  - In all cases: set status CM, fill the HR columns and write history.
- **`P_LOG_STATUS(...)`** (internal): inserts the `EVAL_HIS` row on every status change.
- **`F_IS_OVERDUE(P_PROBATION_EVAL_ID) RETURN CHAR`**: returns Y when the end date is before SYSDATE and the status is not FH, CM or CN. FR-020.
- **Error codes:**

  | Code | Meaning |
  |---|---|
  | -20800 | Not authorised for this action |
  | -20801 | Mandatory fields missing |
  | -20802 | Record changed by another user, reload |
  | -20803 | Comments required for Return |
  | -20804 | Invalid status for this action |
  | -20805 | Extension days or reason missing |

**Modified package `HRD.PKG_PENDING_TASKS`:**

- Add `P_PROBATION_EVAL_QUEUE`, with the framework's standard signature (`P_USER_MRNO, P_ACTING_FOR, P_OBJECT_CODE, P_PROCESS_ID, P_TERMINAL, P_EVENT, P_ASSIGNMENT_ID`).
- It counts the user's items and inserts the count into `HIS.TMP_USER_ASSIGNMENT_VAL`, the same as `PROBATION_EXPIRE_QUEUE`. The items counted are:
  - as evaluator: status EP, DR or RT;
  - as current approver: status PA;
  - as HR (`PKG_HR_ALERTS.F_CHECK_HR_ALERT_RIGHTS`): status FH.
- Register it with one row in `HIS.USER_ASSIGNMENT`. `SOURCE_NAME` = the procedure name; `OBJECT_CODE` = the APEX page code.

# 5. GUI Pages (APEX, SKMCH GUI template)

The application ID and page numbers are to be confirmed. Page code `S07APX0XXXX` is a placeholder. Static IDs follow HRD standards (`REG_`, `P<n>_`, `BTN_`, `DA_`, `LOV_`).

- **Page A: My Pending Tasks.** This is the existing inbox, and it lists the new task type.
  - Grid of evaluations assigned to the user, with days left and status. A row click opens Page B.

![Screen 1 – My Pending Tasks](prototypes/01_pending_tasks.png)

- **Page B: Probation Evaluation (NEW).**
  - **Header:** region `REG_EMPLOYEE_INFO` (read-only).
  - **Tabs:** Evaluation Criteria | Recommendation | Approval History | Finalization.
  - **Criteria tab:** grid `REG_CRITERIA` with a rating select list (`LOV_RATING` 1–5) and remarks, the Rating Scale panel and the score bar.
  - **Buttons:**
    - `BTN_SAVE_DRAFT` calls `P_SAVE_DRAFT` / `P_SAVE_RATING`;
    - `BTN_SUBMIT` calls `P_SUBMIT`;
    - `BTN_PREVIEW` opens the print view;
    - `BTN_EXIT`.
  - **Validation:** the package raises the errors and they are shown inline. Missing mandatory cells are highlighted pink.
  - **Hidden item:** `P<n>_VERSION_NO` for optimistic locking.

![Screen 2 – Evaluation, Criteria tab](prototypes/02_evaluation_form.png)

- **Page B, Recommendation tab:**
  - Radio `P<n>_RECOMMENDATION` (C / E / N).
  - `P<n>_EXTEND_DAYS`, enabled only for Extend through `DA_TOGGLE_EXTEND`.
  - File upload `P<n>_DOCUMENT_ID`.
  - Comments textarea (mandatory on Submit).

![Screen 3 – Evaluation, Recommendation tab](prototypes/03_evaluation_recommendation.png)

- **Page C: Approval (NEW).**
  - Routing bar showing the evaluator and each level with its status.
  - The evaluation shown read-only, and the approver comments.
  - `BTN_APPROVE` calls `P_APPROVE`; `BTN_RETURN` calls `P_RETURN`.
  - **Authorization:** the current approver or acting-for person only.

![Screen 4 – Approval](prototypes/04_approver.png)

- **Page D: Probation Approval Hierarchy Setup (NEW).** Interactive Grid on `HRD_PROBATION_HIERARCHY_MST`.
  - LOVs: department, approver source, employee.
  - **Authorization:** HR Administrator.

![Screen 5 – Hierarchy Setup](prototypes/05_hierarchy_setup.png)

- **Page E: HR queue (NEW).** Report of evaluations with status FH, showing recommendation, final approver and performance %. "Process" opens Page F.

![Screen 6 – HR queue](prototypes/06_hr_queue.png)

- **Page F: HR Finalization (NEW).** The Finalization tab of Page B in HR mode.
  - Decision radio, extension days and reason (`LOV_PROBATION_REASONS` from `HRD.PROBATION_REASONS`), remarks.
  - `BTN_FINALIZE` calls `P_HR_FINALIZE`.
  - **Authorization:** HR User.

![Screen 7 – HR Finalization](prototypes/07_hr_decision.png)

- **Page G: Probation Monitoring (NEW).**
  - Filters and an evaluation grid with Overdue and No-supervisor flags. "Assign Evaluator" calls `P_ASSIGN_EVALUATOR`.
  - Status-history report on `HRD_PROBATION_EVAL_HIS`.
  - **Authorization:** HR User; assigning needs HR Administrator.

![Screen 8 – Monitoring](prototypes/08_monitoring.png)

# 6. Jobs, Notifications and Security

- **Job `HRD.JOB_PROBATION_EVAL_QUEUE`** (DBMS_SCHEDULER):
  - Runs daily at 02:00 and calls `P_GENERATE_EVAL_QUEUE`.
  - A failed run is logged in `HRD_PROBATION_JOB_LOG`, and an alert row e-mails IT support.
- **Notification e-mails:**
  - Sent for: evaluation assigned, pending approval, returned, and forwarded to HR.
  - They use `APEX_MAIL`, with sender and recipients configured in `HRD.ALERTS` / `ALERT_RECIPIENTS`. The standard HRD mail API needs IT confirmation (Q-27).
  - A mail failure is logged and does not roll back the workflow.
- **Authorization schemes:**
  - `AUTH_PROB_EVALUATOR`: the logged-in MRNO equals `EVALUATOR_MRNO`.
  - `AUTH_PROB_APPROVER`: the current approver or acting-for person.
  - `AUTH_PROB_HR_USER` and `AUTH_PROB_HR_ADMIN`: security groups, to be confirmed by IT.
- **Data access:** pages query through the package and check the role, so a user who changes the URL cannot see other users' evaluations.
- **Audit:** audit columns on every table, the insert-only history table, and no physical delete (cancel sets status CN).
- **Privacy:** `MRNO` is also the patient MR number. The pages do not join or link to `REGISTRATION` data.

# 7. Requirement Coverage

- **FR-001, FR-002, FR-003, FR-004, FR-005, FR-006** (queue generation, duplicates, cancel, exceptions, reassign): DS-01, DS-07, `P_GENERATE_EVAL_QUEUE`, `P_ASSIGN_EVALUATOR`, Page G.
- **FR-007, FR-008, FR-009, FR-010** (evaluation form, Draft, Submit, lock): DS-01–03, `P_SAVE_DRAFT`, `P_SAVE_RATING`, `P_SUBMIT`, Page B.
- **FR-011, FR-012, FR-013, FR-014** (routing, approve, return, no self-approval): DS-04, DS-05, `P_ROUTE`, `P_APPROVE`, `P_RETURN`, Pages C and D.
- **FR-015 and FR-016** (forward to HR, HR finalize): `P_ROUTE` (status FH), `P_HR_FINALIZE`, Pages E and F.
- **FR-017, FR-018, FR-019, FR-020** (status, history, monitoring, overdue): DS-06, `P_LOG_STATUS`, `F_IS_OVERDUE`, Page G.
- **NFR-SEC-01, NFR-SEC-02:** authorization schemes, plus role checks inside the package.
- **NFR-AUD-01, NFR-AUD-02:** audit triggers, plus the insert-only history table.
- **NFR-PERF-01, NFR-PERF-02:** set-based job SQL, indexes on status, evaluator, approver and end date.
- **NFR-AVL-01:** the job's date window catches up on missed days. **NFR-AVL-02:** new objects only; no downtime needed.
- **NFR-DAT-01:** no physical delete. **NFR-DAT-02:** unique index. **NFR-DAT-03:** `VERSION_NO` with error -20802.
- **NFR-USA-01, NFR-USA-02:** APEX Universal Theme pages in the SKMCH GUI template, plus the APEX "warn on unsaved changes" setting.
- **NFR-CMP-01:** status rules agreed with HR. **NFR-INT-01:** employee data read live from `INFORMATION`.
- **NFR-OPS-01:** job log and failure alert. **NFR-OPS-02:** non-blocking notification e-mails.

# 8. Change Inventory and Deployment

- **Scripts, run in this order** (no downtime: only new objects are added, plus one procedure in `PKG_PENDING_TASKS`):

  | Step | Script | What it does |
  |---|---|---|
  | 0 | `CR-2026-XXX-PEV_00_precheck.sql` | Checks that no `HRD_PROBATION_%` objects exist, and backs up the current `PKG_PENDING_TASKS` source |
  | 1 | `CR-2026-XXX-PEV_01_ddl.sql` | Sequences, 7 tables, indexes, triggers (provided) |
  | 2 | `CR-2026-XXX-PEV_02_pkg_probation_evaluation.pks` / `.pkb` | New package |
  | 3 | `CR-2026-XXX-PEV_03_pkg_pending_tasks.pkb` | Adds `P_PROBATION_EVAL_QUEUE` (spec and body) |
  | 4 | `CR-2026-XXX-PEV_04_seed.sql` | Criteria from HR's form, default hierarchy, the `HIS.USER_ASSIGNMENT` row, alert rows |
  | 5 | `CR-2026-XXX-PEV_05_job.sql` | Creates the scheduler job |
  | 6 | APEX export | Pages B–G, authorization schemes, LOVs |

- **After deployment, verify:**
  - all new objects are VALID (`USER_OBJECTS`);
  - a manual run of `P_GENERATE_EVAL_QUEUE` on test data creates the expected rows and a SUCCESS log row;
  - the inbox shows the task count.
- **Rollback:** `CR-2026-XXX-PEV_99_rollback.sql` (provided). It drops the job, the package and the tables in reverse order, and redeploys the backed-up `PKG_PENDING_TASKS`.
  - It does not revert probation records that HR has already finalized; those are business decisions.
- **Retest these dependents** (they read `EMPLOYEE_PROBATION_HISTORY`): `PKG_COMMON`, `PKG_EMPLOYEE_INFO`, `PKG_EMP_INCENTIVE`, `PKG_HR_ALERTS`, `PKG_HR_DOCUMENT_RECORD`, `PKG_HR_EMPLOYEE_RECORD`, `LEAVE_AUTOMATION`, `EMAILS`, `V_HR_EMP_DOCUMENTS`.

# 9. Risks and Open Questions

- **Risk: probation status written too early.** Mitigation: only `P_HR_FINALIZE` writes it; covered by code review and a unit test.
- **Risk: duplicate queues with alert 001 / S07FRM00362.** Needs HR's decision (Q-24) before go-live.
- **Risk: stale `MANAGER_MRNO`.** Mitigation: HR exception list, plus a data-quality report before go-live.
- **Open questions:**
  - **Q-05 (HR):** criteria list and rating scale. Needed for the seed data.
  - **Q-07 (HR):** after a Return, does approval restart at level 1?
  - **Q-08 (HR):** for an extension, extend the current probation period or add a new one?
  - **Q-16 (HR):** the actual hierarchy levels per department.
  - **Q-24 (HR):** replace or keep alert 001 and S07FRM00362?
  - **Q-27 (IT):** standard mail API and sender, and the security groups for the HR roles.
