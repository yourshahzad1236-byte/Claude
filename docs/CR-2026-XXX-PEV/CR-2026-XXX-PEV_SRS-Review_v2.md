# 1. Review summary

| Item | Value |
|---|---|
| SRS reviewed | CR-2026-XXX-PEV_SRS_v0.3.md, version 0.3 (impact analysis re-done against the schema) |
| MoM available for coverage check | Yes: 5 workflow points (M-01 to M-08). Coverage is unchanged from review v1 |
| Schema context used | User-supplied full DDL exports (09-Oct-2026): HRD, DEFINITIONS, PAYROLL, HIS, REGISTRATION, including package bodies and trigger source, plus `schema/skm/*.md`. APEX applications and Oracle Forms are not included |
| Recommendation | Return to BA / client |
| Findings | Blocker 4 · Major 10 · Minor 5 · Observation 4 (RV-01 – RV-20 from v1, plus RV-21 – RV-24 new) |

Checking against the real HRD schema changes the picture a lot. HRD already has most of what this CR asks for: a probation record with status, a probation-expiry alert to HR, an evaluation and confirm/extend screen (S07FRM00362), acting-for delegation, and a full appraisal engine with templates, multi-level routing, send-back and HR hand-over. Building the SRS's proposed new tables (v0.2 IMP-16 to IMP-20) would duplicate these. The biggest technical risk is the probation status: setting `PROBATION_STATUS = 'C'` confirms the employee, sets the confirmation date and creates incentive queue entries through triggers. The workflow must never write it before HR confirmation. Blockers RV-01 to RV-03 from v1 still need HR answers. RV-02 is now partly answered (a hierarchy engine exists), and RV-11 (no schema) is resolved.

# 2. Findings

Findings RV-01 to RV-20 are carried over from review v1, with these status changes: **RV-02** is partly answered (the PA hierarchy engine and pending-task framework exist, so only the hierarchy levels remain open for HR). **RV-07** now has a candidate solution (`HRD.ACTING_FOR`, `PKG_PERFORMANCE_APPRAISAL.SET_ROUTING_AS_LEAVE`). **RV-11** is resolved in v0.3: the impact analysis is now verified against the schema. New findings:

| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
|---|---|---|---|---|---|---|
| RV-21 | Blocker | FR-017, IMP-15, IMP-34 | FR-017: "update the probation request status automatically at each workflow event". In HRD the probation request is `HRD.EMPLOYEE_PROBATION_HISTORY`. Code-verified: `PROBATION_STATUS = 'C'` fires `EMP_INCENTIVE_QUEUE` (incentive queue via `PKG_EMP_INCENTIVE.P_INS_QUEUE`), `EMP_PROBATION_HISTORY_INFO_UPD` (sets `INFORMATION.CONFIRMATION_DATE`) and `TR_PROBATION_EXPIRE_QUEUE_DEL`. | Writing a workflow status into this column, or writing 'C' at the wrong step, confirms the employee and starts allowances before HR has decided. That is a payroll and HR-compliance error. | Reword FR-017: "The system shall record the evaluation workflow status (RULE-08) on the evaluation record at each workflow event. The system shall set the probation record status to Confirmed only when HR completes a confirmation (FR-016)." Add RULE-11: "Only the HR completion step may change `PROBATION_STATUS`. An extension updates the probation period instead." | HR / IT (Q-25) |
| RV-22 | Major | §2, FR-001, FR-002, IMP-22, IMP-27 | The SRS describes a new queue, but HRD already has (a) alert 001: probation expiry → `HR_ALERT_QUEUE`, shown to HR users by `PKG_PENDING_TASKS.PROBATION_EXPIRE_QUEUE`, and (b) form S07FRM00362, an evaluation and confirm/extend flow (`PKG_S07FRM00362`, `EVALUATION_ALERT_QUEUE`, `EMPLOYEE_EVALUATION_HISTORY`). | Without a decision, HR and supervisors get duplicate items, and two places record the decision. | Add a "Relationship to existing process" subsection to §3: the supervisor queue replaces or feeds alert 001 and S07FRM00362, as agreed in Q-24. Add an FR to retire or adapt the old path if it is replaced. | HR / IT (Q-24) |
| RV-23 | Major | §8, IMP-16 – IMP-20, Q-26 | The new tables proposed in v0.2 (`HRD_PROBATION_EVAL_MST/DTL/APPROVAL_TRN/HIERARCHY_MST`) duplicate the PA engine: `PA_DEF_TYPE`, `PA_DEF_TEMPLATE` (with `APEX_OBJECT_CODE`), `PA_HIERARCHY`, `PA_PERFORM_MASTER`, `PA_PERFORM_APPRAISER` (roles R/A/F/S, `ORDER_BY`), `PKG_PERFORMANCE_APPRAISAL`. | Duplicating a workflow engine doubles maintenance and creates inconsistent behaviour. Reusing it changes appraisal views and queues (IMP-25), which then need filtering. | v0.3 already presents Option A (reuse PA) and Option B (new tables). The SA should decide at design (Q-26). Recommendation: Option A, unless `PA_TYPE_PERIOD`'s period-based model cannot support rolling probation dates. Note: the FRs stay solution-neutral. | SA |
| RV-24 | Minor | FR-002, Q-04, IMP-14 | "respective supervisor" now has concrete candidates: `HRD.INFORMATION.MANAGER_MRNO` ("manager code of employee") or `DEFINITIONS.DEPARTMENT.DEPARTMENT_MANAGER` / `DEPARTMENT_HEAD`. | It still has to be confirmed, but HR can now pick from named options. | Q-04 has been reworded in v0.3. Once answered, put the chosen source into RULE-02. | HR |

# 3. MoM coverage

Unchanged from review v1. M-03, M-06, M-07 and M-08 remain *Partially* covered, pending Q-04, Q-16, Q-17 and Q-09/Q-25.

# 4. Impact analysis verification

## 4.1 Confirmed items

| IMP-ID | Object | Verified against | Result |
|---|---|---|---|
| IMP-14 | `HRD.INFORMATION` (`MRNO`, `MANAGER_MRNO`, `DEPARTMENT_ID`, `JOINING_DATE`, `PROBATION_PERIOD_DAYS`, `CONFIRMATION_DATE`, `ACTIVE` H/Y/N) | HRD DDL | Exists. Column names and types as in v0.3 |
| IMP-15 | `HRD.EMPLOYEE_PROBATION_HISTORY` (PK `MRNO`, `START_DATE`; `PROBATION_STATUS` VARCHAR2(1) default 'P') | HRD DDL + trigger source | Exists. 'C' = confirmed (code-verified) |
| IMP-22 | Alert 001, `HR_ALERT_QUEUE`, `PKG_HR_ALERTS`, `PKG_PENDING_TASKS.PROBATION_EXPIRE_QUEUE` | Package bodies | Exists. Shows to HR users only |
| IMP-23 | `F_PROBATION_END_DATE`, `F_PROBATION_YN`, `PKG_COMMON.F_CHECK_EMP_PROBATION_STATUS` | Function source | Exists. End date = `MAX(END_DATE)` of probation history |
| IMP-11, IMP-16, IMP-17, IMP-19, IMP-20 | PA engine tables and `PKG_PERFORMANCE_APPRAISAL` | HRD DDL + spec | Exists |
| IMP-27 | `PKG_S07FRM00362`, `EVALUATION_ALERT_QUEUE`, `EMPLOYEE_EVALUATION_HISTORY` | Package spec/body, DDL | Exists |
| IMP-28 | `HRD.ACTING_FOR`, `ACTING_FOR_USER_TASK_WISE` | HRD DDL | Exists |
| IMP-29 | `DEFINITIONS.DEPARTMENT.DEPARTMENT_HEAD`, `DEPARTMENT_MANAGER` | DEFINITIONS DDL | Exists |
| IMP-10, IMP-13, IMP-30 | `HRD.ALERTS`, `ALERT_RECIPIENTS` | HRD DDL | Exists |

## 4.2 Missed dependencies (now added in v0.3)

| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
|---|---|---|---|---|---|
| `EMP_INCENTIVE_QUEUE`, `EMP_PROBATION_HISTORY_INFO_UPD`, `TR_PROBATION_EXPIRE_QUEUE_DEL` | Triggers | `EMPLOYEE_PROBATION_HISTORY.PROBATION_STATUS` | Trigger source | FR-016, FR-017 | IMP-15, IMP-34 (added) |
| `PKG_EMPLOYEE_INFO`, `PKG_HR_EMPLOYEE_RECORD`, `EMAILS`, `PKG_HR_ALERTS` | Package bodies | `EMPLOYEE_PROBATION_HISTORY` | Package bodies | FR-017 | IMP-24 (added) |
| `PKG_S07FRM00362` | Package (form S07FRM00362) | `EVALUATION_ALERT_QUEUE`, `EMPLOYEE_EVALUATION_HISTORY` | Spec/body | FR-015, FR-016 | IMP-27 (added) |
| `VU_PA_PERFORM_QUEUE`, `VU_PA_ROUTING`, `VU_PERFORM_VAL_RATING`, `V_EMP_PROMOTION_REPORT`, `PKG_HR_PA_PENDING_TASK` | Views / package | `PA_PERFORM_APPRAISER`, `PA_HIERARCHY` | View SQL | FR-011 (Option A) | IMP-25 (added) |
| `V_HR_EMP_DOCUMENTS` | View | `EMPLOYEE_EVALUATION_HISTORY`, `EMPLOYEE_PROBATION_HISTORY` | View SQL | FR-018 | IMP-26 (added) |

## 4.3 Incorrect or unverifiable items

| IMP-ID | Object | Problem | Correction |
|---|---|---|---|
| IMP-05 (v0.2) | "Existing queue/inbox page" | Too vague | Now `PKG_PENDING_TASKS` with its standard procedure signature. The APEX inbox page is still not verifiable (not in export) |
| IMP-07, IMP-12 | APEX pages, authorization schemes | APEX not in export | Keep PROVISIONAL. Export the APEX application(s) before Gate 2 |
| IMP-16 – IMP-20 (v0.2) | New `HRD_PROBATION_*` tables | Duplicate the existing PA engine | Reframed as Option B in v0.3 (RV-23) |

# 5. NFR coverage

Unchanged from review v1. Additional note: NFR-INT-01 should name `HRD.INFORMATION` and `HRD.EMPLOYEE_PROBATION_HISTORY` as the sources, and add payroll/incentive (IMP-34) as an affected integration.

# 6. Patient-safety and compliance notes

- No clinical impact.
- `HRD.INFORMATION.MRNO` has an FK to `REGISTRATION.PATIENT(MRNO)`: employees are registered as patients under the same number. Evaluation screens must not show or link to patient-registration data.
- Compliance: confirmation (`PROBATION_STATUS = 'C'`) has payroll/allowance effects. Only HR may trigger it (RV-21).
- The schema export contains hardcoded internal SMTP host IPs, default user passwords and a password hash in some package bodies (HIS, HRD). This doesn't affect this CR, but it should be raised with IT security. Don't commit these exports to a repository without redaction.

# 7. Resolution log

| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
|---|---|---|---|
| RV-01 – RV-20 | | See review v1. RV-11 resolved | 0.2 / 0.3 |
| RV-21 | | Needs Q-25 answer; FR-017 rewording proposed | |
| RV-22 | | Needs Q-24 answer | |
| RV-23 | | Options A/B documented in §8; SA to decide (Q-26) | 0.3 (partial) |
| RV-24 | | Q-04 reworded with candidates | 0.3 |
