# 1. Review summary

| Item | Value |
|---|---|
| SRS reviewed | CR-2026-XXX_SRS_v0.1.docx, version 0.1 (IN REVIEW) |
| MoM available for coverage check | Yes: "Committee Workflow Enhancements (for QPSD)", 16 points |
| Schema context used | None: HRD system context not yet indexed. Impact verification not possible |
| Recommendation | Return to BA / client |
| Findings | Blocker 3 · Major 7 · Minor 6 · Observation 3 |

The SRS is well structured. All 16 MoM points are traced, every FR has a negative acceptance criterion, and the NFR checklist has been worked through. It cannot go to design yet. Three core behaviours depend on stakeholder answers the meeting did not give: who uploads the minutes and who signs off, what the QA role does, and what the alerts are. The SRS also has no status model for nominations, queue items and meetings, and it does not cover cancellation, delegation or the minutes lifecycle. The impact analysis is entirely provisional and must be verified against the HRD schema before Gate 1.

# 2. Findings

| ID | Severity | Location | Issue | Why it matters | Proposed fix | Question for |
|---|---|---|---|---|---|---|
| RV-01 | Blocker | FR-010, §7.3, A-03 | Sign-off and upload roles are assumed: "A (assumed, Q-03)", "C R (assumed, A-03)". | The sign-off gate (the main control in this CR) cannot be built or tested without knowing who may sign off and who may upload. Segregation of duties is undefined. | Get QPSD's answer to Q-03. Then reword FR-010 to "The system shall allow only the <role> of the meeting to perform Committee Sign-off…" and add an FR for the minutes upload naming its role. Remove "assumed" from §7.3. | QPSD |
| RV-02 | Blocker | FR-006, M-04, Q-02 | "one QA item for QA". The purpose and actions of a QA queue item are not defined anywhere. | A queue item with no defined action cannot be designed, completed or tested, and may sit open forever. | Define the QA role's task (for example, review minutes before sign-off). Add an FR for the QA queue action and its effect on sign-off. If QA has no queue action, remove the QA item from FR-006. | QPSD |
| RV-03 | Blocker | FR-011, §7.4, Q-04 | "the alert is sent to the defined recipients". The event, recipients, channel and day values are all "To be confirmed". | FR-011 is untestable as written, and the design (job, tables, templates) depends entirely on these answers. | List each alert as its own FR: event, reference date, number of days (before or after), recipients, channel and message content. Example: "FR-0xx: The system shall email the Secretary 3 days after the Actual Meeting Date if Committee Minutes are not uploaded." | QPSD |
| RV-04 | Major | No section; §2, §3 | No status model is defined for nomination, queue item or committee meeting (checklist §C). | Without states and allowed transitions, the sign-off, queue completion (FR-008), alerts (RULE-05) and report rows cannot be specified consistently. | Add §3.1 Status model: Nomination (Active / Withdrawn), Queue item (Open / Completed / Cancelled), Meeting (Planned / Held / Minutes uploaded / Signed off), each with its allowed transitions and the role that triggers them. | BA |
| RV-05 | Major | §5.1, §5.2, Q-10 | No requirement covers withdrawing a nominee, cancelling a meeting, or changing a role after queues exist. Q-10 is marked non-blocking. | These happen in real use. Undefined behaviour leaves orphan queue items and wrong report names. | Add FRs for nominee withdrawal and role change, with queue regeneration or cancellation rules. Raise Q-10 to blocking. | QPSD / BA |
| RV-06 | Major | FR-009, FR-010, NFR-DAT-01 | Minutes lifecycle is incomplete: replacing a wrongly uploaded file before sign-off, and reversing a sign-off, are not covered. | Users will upload the wrong file. Without a rule, sign-off is either blocked or done against the wrong minutes, which weakens the audit evidence. | Add an FR allowing the uploader to replace the minutes before sign-off (with history kept). State that sign-off is irreversible, or define who can reopen it. | QPSD |
| RV-07 | Major | FR-010, §7.3 | No delegation or escalation when the signing role (assumed Chair) is absent or on leave. | Meetings stay unsigned and alerts repeat with no resolution path. | Add a requirement for a delegate or an escalation path (for example to the QPSD admin) after N days. Tie it to an alert under RV-03. | QPSD |
| RV-08 | Major | §1.5, FR-009, FR-013 | The unit of "committee meeting" is undefined. The SRS uses "training", "committee" and "meeting" interchangeably: "Committee Minutes … for a committee meeting" vs queue items per nominee. | Unclear whether minutes and sign-off attach to a training session, a recurring committee or a queue item. This drives the data model, the report row granularity and Q-05. | Define "Committee meeting = one scheduled session of a committee training". State that minutes and sign-off are per meeting, and that a report row is one meeting. Confirm Q-05 (one Chair / one Secretary per meeting?). | QPSD / BA |
| RV-09 | Major | FR-001, §7.2, Q-01, Q-11 | FR-001 does not list its fields, yet §7.2 marks Planned Meeting Date "Mandatory: Yes" and Location "To be confirmed". Whether the existing nominee screen remains (Q-11) is open. | If the old screen stays, it can still create committee nominees without a role, bypassing FR-005 and the queue rules. | List FR-001's exact fields once Q-01 is answered. Add an FR that the existing screen shall not allow committee-training nominations (or shall enforce the same role rules), depending on Q-11. | QPSD / SA |
| RV-10 | Major | §8 (IMP-05 to IMP-20) | All 20 impact items are "PROVISIONAL – not verified". Existing nominee, queue, category and report objects are "TO BE CONFIRMED". | Dependencies (views, packages, reports on the nominee/queue tables and the checkbox columns being retired) cannot be found, so rework risk is high. | Index the HRD schema (`scripts/build_schema_index.py`) or attach the relevant object sources, then re-run the impact analysis before SA approval. | SA / BA |
| RV-11 | Minor | FR-003 | FR-003 combines two behaviours: offering the four-value Role LOV and removing the checkboxes (AC3). | Not atomic (checklist §B). | Split into FR-003 (role values) and a new FR "The system shall not display the Chair and Secretary checkboxes on nominee screens." | BA |
| RV-12 | Minor | FR-005 AC3 | "through any other path (for example a data load or API)". No data load or API is in scope. | It introduces untestable, unspecified paths. | Reword: "Given a nomination row without a role, when it is written to the database by any means, then it is rejected." | BA |
| RV-13 | Minor | FR-006, FR-012 | Marked "Inferred" without a dedicated Q-NN (conventions require one for inferred FRs). | Inferred scope may not be wanted by QPSD. | Add Q-15: "Confirm single-role queues behave as today" and Q-16: "Confirm alert days must be admin-maintainable." | BA |
| RV-14 | Minor | NFR-AVL-01 | "short downtime" is an ambiguous word with no measure. | Not measurable. | "Deployment downtime ≤ 30 minutes, outside 08:00–17:00, announced 2 working days ahead." | SA |
| RV-15 | Minor | NFR-PERF-02 | "one year of committee meetings" gives no volume. | Not measurable without a record count. | State the expected meetings per year (for example ≤ 500) and the users at peak. | QPSD |
| RV-16 | Minor | Cover, §1.4, §1.6 | CR ID is the placeholder "CR-2026-XXX". The meeting date and attendees are unknown and marked "(assumed)". | Traceability and approval records need a real CR and source. | Fill in the CR number, MoM date and attendee names (Q-13, Q-14). | BA |
| RV-17 | Observation | FR-014 | "Could" priority, with feasibility left to the SA (Q-12). | The storage design for minutes (IMP-18) is the same either way, so deciding now avoids rework. | Decide Q-12 at SA review; if feasible, raise FR-014 to Should. | SA |
| RV-18 | Observation | FR-009 | Minutes upload is placed on the Queue screen only. | Upload from the meeting/training record may suit Secretaries better. | Consider allowing upload from the meeting record too; keep the gate on sign-off. | QPSD |
| RV-19 | Observation | Tooling | `check_trace.py` pattern `NFR-[A-Z]{3}-\d{2}` does not match `NFR-PERF-01/02` (it counted 12 of 14 NFRs). | Trace checks will silently skip PERF NFRs in later stages. | Change the pattern to `NFR-[A-Z]{3,4}-\d{2}` in `shared/scripts/check_trace.py` and repackage. | Skill maintainer |

# 3. MoM coverage

| M-ID | Statement | Covered by | Status |
|---|---|---|---|
| M-01 | New Training Nominee Form with minimum required fields in APEX | FR-001 | Partially (fields undefined, RV-09) |
| M-02 | Only active Committee-category trainings selectable | FR-002, RULE-01 | Covered |
| M-03 | Chair/Secretary checkboxes replaced with LOV | FR-003 | Covered |
| M-04 | LOV values Chair, Secretary, Both, QA | FR-003, RULE-02 | Partially (QA purpose undefined, RV-02) |
| M-05 | No role selected by default | FR-004 | Covered |
| M-06 | Role mandatory for every nominee | FR-005 | Covered |
| M-07 | No save without role | FR-005 | Covered |
| M-08 | Both → separate Chair and Secretary queues | FR-007, FR-008, RULE-03 | Covered |
| M-09 | Attendance and post-process unchanged | BR-06, §1.3 Out of scope, §9.2 | Out of scope |
| M-10 | Queue screen checks minutes uploaded | FR-009, RULE-04 | Covered |
| M-11 | No sign-off until minutes uploaded | FR-010, RULE-04 | Partially (signing role undefined, RV-01) |
| M-12 | Alerts per defined number of days | FR-011, FR-012, RULE-05 | Partially (alerts undefined, RV-03) |
| M-13 | Enhance Committee Summary/Detail Report | FR-013 | Covered |
| M-14 | Report columns: name, location, Chair, Secretary, planned and actual date | FR-013, RULE-06 | Covered |
| M-15 | Meeting Minutes attachment (if feasible) | FR-014 | Covered (Could) |
| M-16 | Development per agreed requirements | Whole SRS | Covered |

# 4. Impact analysis verification

## 4.1 Confirmed items

| IMP-ID | Object | Verified against | Result |
|---|---|---|---|
| - | - | No schema context available | None could be confirmed |

## 4.2 Missed dependencies

| Object | Type | References (table/column) | Evidence | Related FR | Suggested impact entry |
|---|---|---|---|---|---|
| Not determinable | - | - | No schema index or source available | - | Re-run after schema indexing (RV-10) |
| Existing reports or extracts reading the Chair/Secretary checkbox columns | Report / view (likely) | Nominee checkbox columns (IMP-16) | Inferred from the retirement of the columns | FR-003 | Add an impact row "Modify: all consumers of the retired flags" once found |
| Existing nominee screen (if retained) | APEX page | Nominee table | Q-11 | FR-005 | Add role validation, or block committee nominations there (RV-09) |

## 4.3 Incorrect or unverifiable items

| IMP-ID | Object | Problem | Correction |
|---|---|---|---|
| IMP-01 to IMP-04 | Business impact rows | Not schema-dependent; plausible | None needed |
| IMP-05 to IMP-13 | APEX pages, queue logic, job, report, authorization | Unverifiable: object names unknown | Verify against the HRD application export |
| IMP-14 to IMP-18 | Category, nominee, queue and minutes tables | Unverifiable: tables and columns "TO BE CONFIRMED" | Verify names, types and constraints in the schema |
| IMP-19, IMP-20 | `HRD_TRAINING_ALERT_MST`, `HRD_TRAINING_ALERT_LOG` (NEW proposed) | Names follow HRD standards. Duplication with an existing alert/notification table cannot be ruled out | Search the schema for existing alert setup/log tables before creating new ones |

# 5. NFR coverage

| Category | Present in SRS | Adequate | Comment |
|---|---|---|---|
| SEC | Yes (SEC-01 to 03) | Partially | Depends on the roles in RV-01 |
| AUD | Yes (AUD-01, 02) | Yes | Add history of minutes replacement (RV-06) |
| PERF | Yes (PERF-01, 02) | Partially | PERF-02 needs volume (RV-15) |
| AVL | Yes (AVL-01) | Partially | Needs a measure (RV-14) |
| DAT | Yes (DAT-01, 02) | Partially | Retention period open (Q-07) |
| USA | Yes (USA-01) | Yes | - |
| CMP | Yes (CMP-01) | Yes | Accreditation evidence noted |
| INT | Yes (INT-01) | Partially | Channel open (RV-03) |
| OPS | Yes (OPS-01) | Partially | Alert failure handling defined; retry not stated |

# 6. Patient-safety and compliance notes

- No requirement touches clinical orders, medication, results, patient identity or billing. Direct patient-safety risk: none found.
- QPSD committees (quality and patient safety) produce governance evidence. Committee Minutes and sign-off records are likely accreditation evidence (for example JCI). The minutes lifecycle (RV-06) and sign-off controls (RV-01, RV-07) are therefore compliance-relevant, and they need negative tests.
- Only employee data is involved. No patient identifiers were found in the SRS or MoM.

# 7. Resolution log

| RV-ID | SA decision (Accept / Reject / Defer) | Resolution | Resolved in SRS version |
|---|---|---|---|
| RV-01 |  |  |  |
| RV-02 |  |  |  |
| RV-03 |  |  |  |
| RV-04 |  |  |  |
| RV-05 |  |  |  |
| RV-06 |  |  |  |
| RV-07 |  |  |  |
| RV-08 |  |  |  |
| RV-09 |  |  |  |
| RV-10 |  |  |  |
| RV-11 |  |  |  |
| RV-12 |  |  |  |
| RV-13 |  |  |  |
| RV-14 |  |  |  |
| RV-15 |  |  |  |
| RV-16 |  |  |  |
| RV-17 |  |  |  |
| RV-18 |  |  |  |
| RV-19 |  |  |  |
