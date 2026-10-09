# 1. Review summary

| Item | Value |
|---|---|
| SRS reviewed | CR-2026-XXX-PEV_SRS_v0.1.docx / .md, version 0.1 (DRAFT) |
| MoM available for coverage check | Yes: "Automated Employee Probation Evaluation" proposed workflow, 5 points (split into M-01 to M-08) |
| Schema context used | None: the HRD system context is not indexed yet and `schema/` holds no objects. Impact verification was not possible |
| Recommendation | Return to BA / client |
| Findings | Blocker 3 · Major 8 · Minor 5 · Observation 4 |

The SRS is well structured. All eight MoM points are traced, every FR has a negative acceptance criterion, the status model is defined (RULE-08), and the NFR checklist has been worked through. It cannot go to design yet. Three core behaviours depend on HR answers that the request does not give: when HR receives the evaluation (after the evaluator submits or after final approval), what the approval hierarchy is and whether HRD already has one, and what the evaluation form contains. The SRS also mixes two status concepts ("probation request status" and "evaluation status"), and it has no delegation, withdrawal or concurrency handling. Several acceptance criteria are not deterministic. The impact analysis is entirely provisional and must be checked against the HRD schema before Gate 1.

# 2. Findings

| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
|---|---|---|---|---|---|---|
| RV-01 | Blocker | M-07, FR-015, RULE-07, A-02, Q-17 | Source point 4 says "After submission, the completed evaluation should automatically be routed to HR Department". The SRS assumes this means after final approval (A-02). | Point 3 (hierarchy) and point 4 (HR) could be sequential, or HR could receive it in parallel on submission. The two readings give different routing, queues and status models. This is the core flow. | Confirm Q-17 with HR. If sequential, keep FR-015 and remove A-02. If parallel, add an FR: "The system shall make a submitted evaluation visible to HR (read-only) at the time of submission" and change RULE-07. | HR |
| RV-02 | Blocker | FR-011, IMP-08, IMP-11, IMP-20, Q-15, Q-16 | "the approval hierarchy configured for probation evaluations". Neither the levels nor the place where they are configured are known, and the SRS cannot say whether HRD already has a hierarchy setup. | If HRD already has a generic approval engine, building `HRD_PROBATION_HIERARCHY_MST` duplicates it. If it doesn't, the scope grows by a setup screen and table. The design depends on the answer. | Get answers to Q-15 (IT) and Q-16 (HR). Then reword FR-011 to name the hierarchy basis, for example "…levels defined per department in <existing setup> for workflow type Probation Evaluation". | HR / IT |
| RV-03 | Blocker | FR-007, FR-009, §7.2, Q-05 | The evaluation content is "Per HR form design (Q-05)". The criteria, rating scale, recommendation values and mandatory fields are all unknown. | FR-009's mandatory validation cannot be tested, and the evaluation detail table and page cannot be designed. If the form differs for clinical and non-clinical staff, a template model is needed. | Attach HR's current probation evaluation form as an appendix. Add §7.2 rows per criterion. State whether there is one form or a template per staff category. | HR |
| RV-04 | Major | FR-017, §1.5, IMP-15, Q-03 | The SRS uses both "probation request status" (FR-017, M-08) and an evaluation workflow status (FR-008 "status becomes Draft"). It does not say whether they are one field or two. | If a probation request entity already exists with its own statuses, writing evaluation statuses into it can break existing screens and reports. If there are two statuses, the mapping between them has to be specified. | In §1.5 and FR-017, state: "Probation request status is the HR-level status of the employee's probation period. Evaluation status is the workflow status in RULE-08. The probation request status shall be set to <value> when …" Add a mapping table once Q-03 and Q-09 are answered. | BA / HR |
| RV-05 | Major | FR-001 vs RULE-01 | FR-001: "whose probation end date is 15 calendar days after the current date" (exact equality). RULE-01: "picked up on the first daily run on or after the trigger date". NFR-AVL-01 requires catch-up. | With exact equality, any missed run, any go-live backlog or any probation shorter than 15 days is never picked up, which contradicts RULE-01 and NFR-AVL-01. | Replace the FR-001 description with: "The system shall, once every day, identify each employee on probation whose probation end date is on or before 15 calendar days after the current date, is not earlier than the current date, and who has no evaluation for the current probation period." Add an AC for the catch-up case. | BA |
| RV-06 | Major | FR-014 AC1, RULE-09 | "Level 1 is skipped or escalated according to RULE-09". | "or" makes the AC untestable. RULE-09 says "escalated to the next level" but does not cover the case where there is no next level. | Make it deterministic: "…then the evaluation moves to the next level and the history records 'Skipped: approver is evaluator'. If there is no next level, the evaluation is placed on the HR exception list." Update RULE-09 to match. | BA / HR (Q-16) |
| RV-07 | Major | §5.3, checklist §C | No delegation or escalation when the approver or the evaluator is on leave or has left. | Evaluations have a hard deadline (probation end date). An absent approver blocks the evaluation and the employee's confirmation. | Add Q-21. Then add an FR for delegation, or HR reassignment of an approval level (an extension of FR-006), and link it to FR-020 overdue handling. | HR |
| RV-08 | Major | §5.2, checklist §C | There is no withdraw / recall of a submitted evaluation by the evaluator before Level 1 acts. FR-010 allows edits only after a Return. | Mistakes found right after Submit need an approver to Return the evaluation. That adds a step, and some organisations want this kept for audit. A decision is needed either way. | Add Q-22. If allowed, add an FR: "The system shall allow the evaluator to recall a submitted evaluation that has not yet been acted on at Level 1", with the status set back to Draft. | HR |
| RV-09 | Major | NFR section, FR-006, FR-012 | Concurrency is not covered: HR reassigns (FR-006) while the evaluator is editing the Draft, or two users act on the same approval, or someone double-clicks Submit. | This can lose draft data, cause duplicate approvals or skip a level. | Add NFR-DAT-03: "The system shall reject a save or workflow action on an evaluation that another user has changed since it was opened, with the message 'This evaluation was changed by another user. Reload and try again.' A repeated Submit or Approve shall have no further effect." | BA |
| RV-10 | Major | §7.3 access matrix | The Approver has "-" on "Evaluation form – Draft / Submit", but approvers must read the submitted evaluation to approve it. NFR-SEC-02 allows approvers "in its routing path". | The matrix and NFR-SEC-02 disagree. A build that follows the matrix would deny approvers access to the content. | Split the row: "Evaluation form – edit (Draft/Submit)": Evaluator C R U, everyone else "-". "Evaluation form – view submitted": Approver R (own path), HR User R, HR Administrator R. | BA |
| RV-11 | Major | §8 (all IMP rows) | The impact analysis is entirely PROVISIONAL. The employee master, supervisor source, probation dates, an existing probation request table, the queue/inbox page and the mail utility are all unverified. | Missed dependencies (existing probation reports, triggers on the employee master, payroll extracts that read probation status) can't be found without the schema. | Load the HRD schema into `schema/`, build the index, and re-run §4 of this review before Gate 1. Keep all IMP rows PROVISIONAL until then. | IT / BA |
| RV-12 | Minor | FR-011 | "resolving the approver for that level from the evaluator's / employee's organisation". | "/" leaves it open whose department decides the approver, and the two can differ (for example a cross-department supervisor). | Choose one: "…from the evaluated employee's department as on the submission date" (pending Q-16). | HR |
| RV-13 | Minor | NFR-OPS-02 | No failure handling for notifications. | A failed e-mail must not stop the workflow, and failures should be visible. | Append: "Notification failure shall not block the workflow action. Failures shall be logged and visible to IT support." | BA |
| RV-14 | Minor | Appendix B | Several NFRs are not in the traceability appendix (PERF-01/02, AVL-02, DAT-01/02, USA-01/02, CMP-01, INT-01). | Incomplete traceability to impact items. | Add rows for them, citing "Inferred" and the relevant IMP items, or "none (process / policy)". | BA |
| RV-15 | Minor | FR-005 AC2 | "an HR Administrator assigns an evaluator". FR-006 is the reassignment function, but FR-005 doesn't reference it. | Duplicate behaviour in two FRs. | Change FR-005 AC2 to "…when an HR Administrator assigns an evaluator using FR-006, then…". Allow FR-006 on unassigned evaluations. | BA |
| RV-16 | Minor | NFR-PERF-01, A-05 | "up to 15,000 active employees" is not from the source and not listed as an assumption. | The figure could be wrong by an order of magnitude. | Add A-08: "Active employee population is up to 15,000", for HR/IT to confirm. | HR / IT |
| RV-17 | Observation | §1.3, §9 | The SRS doesn't say that the system will not auto-confirm or auto-extend probation when an evaluation is overdue. | Stating this avoids a wrong design assumption. Labour-law consequences of a missed evaluation are an HR policy matter. | Add to Out of scope: "Automatic confirmation, extension or termination of probation, including when an evaluation is overdue." | HR |
| RV-18 | Observation | Q-23 (new) | No rule for an employee whose probation is shorter than 15 days, or who joins less than 15 days before a backdated probation end date. | This is an edge case. With the RV-05 fix it is picked up on the next run, but HR should confirm that. | Add Q-23. | HR |
| RV-19 | Observation | §7.5 | Payroll/ERP is marked not applicable. Confirmation often changes benefits or leave entitlement. | It's out of scope for this CR, but a later CR may need the "Completed" event. | Keep it out of scope. Note in §9.3 that a later CR may consume the completion event. | HR |
| RV-20 | Observation | Q-20 | Whether the employee acknowledges the evaluation is open. | Many HR policies require the employee's acknowledgement before confirmation. If it does, a step is added to the workflow. | Keep Q-20 and raise its priority with HR. | HR |

# 3. MoM coverage

| M-ID | Statement | Covered by | Status |
|---|---|---|---|
| M-01 | Automated Employee Probation Evaluation (objective) | BR-01 | Covered |
| M-02 | Generate probation evaluation queue 15 days before probation end date | FR-001, FR-002, FR-003, RULE-01 | Covered (RV-05 consistency fix needed) |
| M-03 | Respective supervisor | FR-002, FR-005, RULE-02 | Partially: supervisor source open (Q-04) |
| M-04 | Save the evaluation as Draft | FR-008, RULE-04 | Covered |
| M-05 | Submit it for approval | FR-009, FR-010 | Covered (RV-08 recall) |
| M-06 | Route through configured approval hierarchy | FR-011 – FR-014 | Partially: hierarchy undefined (RV-02) |
| M-07 | Completed evaluation routed to HR after submission | FR-015, FR-016 | Partially: timing ambiguous (RV-01) |
| M-08 | Automatically update probation request status throughout workflow | FR-017, FR-018, RULE-08 | Partially: two status concepts (RV-04) |

# 4. Impact analysis verification

## 4.1 Confirmed items

| IMP-ID | Object | Verified against | Result |
|---|---|---|---|
| - | - | No schema context available | No item could be confirmed |

## 4.2 Missed dependencies

| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
|---|---|---|---|---|---|
| Existing probation / confirmation reports (if any) | Report | Probation request status | Not verifiable (no schema) | FR-017 | Add IMP row "Existing HR reports on probation status: Read-only / verify" once the schema is available |
| Triggers on the employee master (if any) | Trigger | Employment status, supervisor | Not verifiable | FR-004, FR-006 | Add an IMP row if found. FR-004 cancellation may hook into separation processing |
| Separation / resignation process | Package / APEX | Employee status change | Not verifiable | FR-004 | Add an IMP row: the cancellation of an open evaluation must be called from, or detect, the separation process |
| Employee leave / absence data | Table | Approver availability | Not verifiable | RV-07 | Needed only if delegation is based on leave |

## 4.3 Incorrect or unverifiable items

| IMP-ID | Object | Problem | Correction |
|---|---|---|---|
| IMP-05, IMP-11, IMP-13, IMP-14, IMP-15 | Existing queue page, workflow package, mail utility, employee master, probation request table | Existence not verifiable | Keep as PROVISIONAL / TO BE CONFIRMED. Verify against the schema |
| IMP-16 – IMP-21 | Proposed new tables and sequences | Names follow HRD standards (`HRD_*_MST/DTL/HIS/TRN`, `*_SEQ`). Possible duplication with existing objects not checked | Check for existing probation/workflow tables before design |
| IMP-21 | `PROBATION_EVAL_SEQ` "etc." | "etc." is not specific | List each sequence and the unique key explicitly in the design doc |

# 5. NFR coverage

| Category | Present in SRS | Adequate | Comment |
|---|---|---|---|
| SEC | Yes (SEC-01, SEC-02) | Partially | Conflicts with access matrix (RV-10) |
| AUD | Yes (AUD-01, AUD-02) | Yes | - |
| PERF | Yes (PERF-01, PERF-02) | Partially | Population figure unconfirmed (RV-16) |
| AVL | Yes (AVL-01, AVL-02) | Yes | Catch-up depends on the RV-05 fix |
| DAT | Yes (DAT-01, DAT-02) | Partially | No concurrency rule (RV-09). Retention open (Q-19) |
| USA | Yes (USA-01, USA-02) | Yes | - |
| CMP | Yes (CMP-01) | Yes | Needs HR policy reference |
| INT | Yes (INT-01) | Yes | - |
| OPS | Yes (OPS-01, OPS-02) | Partially | Notification failure handling (RV-13) |

# 6. Patient-safety and compliance notes

- No direct patient-safety impact: no clinical data, orders, medication or billing are touched. The indirect effect is on staffing of clinical departments through probation outcomes (IMP-04).
- Employee confidentiality: evaluation content is sensitive personal and performance data. Access has to be limited to the evaluator, approvers in the routing path and HR (NFR-SEC-02, RV-10). Views by HR should also be considered for audit.
- Labour-law / HR policy: the timing of the evaluation relative to the probation end date, and what happens when it is overdue (RV-17), must follow SKMCH HR policy. HR sign-off is needed under NFR-CMP-01.

# 7. Resolution log

| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
|---|---|---|---|
| RV-01 | | Needs HR answer (Q-17) | |
| RV-02 | | Needs HR/IT answers (Q-15, Q-16) | |
| RV-03 | | Needs HR form (Q-05) | |
| RV-04 | | Clarified in definitions; mapping pending Q-03/Q-09 | 0.2 (partial) |
| RV-05 | | FR-001 reworded, catch-up AC added | 0.2 |
| RV-06 | | FR-014 AC1 and RULE-09 made deterministic | 0.2 |
| RV-07 | | Q-21 added | 0.2 (question only) |
| RV-08 | | Q-22 added | 0.2 (question only) |
| RV-09 | | NFR-DAT-03 added (Proposed) | 0.2 |
| RV-10 | | Access matrix row split | 0.2 |
| RV-11 | | Pending schema load | |
| RV-12 | | Wording narrowed, pending Q-16 | 0.2 |
| RV-13 | | NFR-OPS-02 extended | 0.2 |
| RV-14 | | Appendix B completed | 0.2 |
| RV-15 | | FR-005 AC2 references FR-006 | 0.2 |
| RV-16 | | A-08 added | 0.2 |
| RV-17 | | Out-of-scope bullet added | 0.2 |
| RV-18 | | Q-23 added | 0.2 |
| RV-19 | | Note added to §9.3 | 0.2 |
| RV-20 | | No change (Q-20 retained) | |

The "Resolved in SRS version" column shows the reviewer's proposed changes, already applied in draft v0.2. SA decisions are left blank for the Solution Architect.
