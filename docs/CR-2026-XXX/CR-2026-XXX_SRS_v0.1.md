# 1. Introduction

## 1.1 Purpose

This SRS specifies the Committee workflow enhancements to the Training Management Module for QPSD. It is written for the Solution Architect (review and approval), the development team (design and build) and QA (test design).

## 1.2 Background

Committee meetings are managed as trainings in the Training Management Module. Today, nominee roles are captured with separate Chair and Secretary checkboxes. A nominee can be saved with no role. Committee sign-off can happen without the meeting minutes on record. The Committee Summary/Detail Report does not show who chaired or recorded each meeting, or when it actually took place. In the meeting, QPSD and the development team agreed the changes below (M-01 to M-16).

## 1.3 Scope

### In scope

- A new APEX Training Nominee Form for committee trainings only (M-01, M-02).
- A mandatory single nominee role chosen from Chair, Secretary, Both or QA, replacing the checkboxes (M-03 to M-07).
- Separate Chair and Secretary queues for a nominee assigned Both (M-08).
- Committee Sign-off blocked until Committee Minutes are uploaded (M-10, M-11).
- System alerts sent on a defined number of days (M-12).
- Enhanced Committee Summary/Detail Report (M-13 to M-15).

### Out of scope

- Any change to the existing attendance and post-process workflow (M-09).
- Non-committee trainings. Their nomination process is not changed (M-02).

## 1.4 Stakeholders

| Name / Role | Department | Interest / responsibility | Attended meeting |
|---|---|---|---|
| QPSD representative(s) (names not in MoM, Q-14) | QPSD | Business owner; committee governance | Yes (assumed) |
| Business Analyst | IT / Development | Requirement owner for this SRS | Yes (assumed) |
| Development team | IT / Development | Build per agreed requirements (M-16) | Yes (assumed) |
| Solution Architect | IT | SRS review and approval (Gate 1) | Not stated |
| Committee Chairs, Secretaries, QA nominees | Various | End users of queues and sign-off | No |

## 1.5 Definitions and abbreviations

| Term | Meaning |
|---|---|
| QPSD | Quality and Patient Safety Department (expansion to be confirmed, Q-14) |
| APEX | Oracle Application Express, the platform for the HRD applications |
| LOV | List of Values (a select list in APEX) |
| Committee training | A training whose category is marked as Committee |
| Nominee | An employee nominated against a committee training |
| Role | The nominee's function in the committee: Chair, Secretary, Both or QA |
| Queue | A work item shown to a nominee on the Queue screen for action |
| Committee Minutes | The minutes document of a committee meeting, uploaded to the system |
| Committee Sign-off | The action on the Queue screen that formally closes a committee meeting |
| MoM | Minutes of Meeting |

## 1.6 References

- MoM: "Committee Workflow Enhancements (for QPSD)", Training Management Module. Meeting date and attendees not stated (Q-14).
- Earlier SRS versions: none.
- Related CRs: none known. CR number to be assigned (Q-13).

# 2. Current state (As-Is)

1. Nominees for committee trainings are entered through the existing nominee screen (screen name to be confirmed, Q-11).
2. Each nominee's committee function is marked with two independent checkboxes, Chair and Secretary. A record can be saved with neither ticked. There is no QA role.
3. Queue items are generated for nominees from the checkbox values (exact logic to be confirmed, Q-02).
4. Attendance is marked and the post-process runs. This part works as required and is not changing.
5. Committee Sign-off is possible from the Queue screen whether or not the Committee Minutes have been uploaded.
6. The Committee Summary/Detail Report does not show the Chair, Secretary, planned versus actual meeting date or the minutes.

Pain points: nominees with no role, no QA role, unclear queue ownership when one person is both Chair and Secretary, meetings signed off with no minutes on record, and limited reporting.

# 3. Proposed solution overview (To-Be)

1. An authorised user opens the new Training Nominee Form and selects a training. Only active trainings whose category is Committee are offered.
2. The user selects the employee and must choose one role: Chair, Secretary, Both or QA. No role is pre-selected. The record cannot be saved without a role.
3. On save, the system creates queue items by role. A nominee with Both receives two independent items, one as Chair and one as Secretary.
4. The meeting takes place. Attendance and the post-process run as they do today.
5. On the Queue screen, the system shows whether the Committee Minutes have been uploaded. Committee Sign-off is refused until they are.
6. The system sends alerts on the configured number of days.
7. Management uses the enhanced Committee Summary/Detail Report to see each committee meeting with its location, Chair, Secretary, planned and actual dates and, if feasible, the minutes.

# 4. Business requirements

| ID | Business requirement | Source (M-NN) | Priority |
|---|---|---|---|
| BR-01 | Every committee nominee shall have exactly one clearly defined committee role, captured at nomination. | M-01, M-02, M-03, M-04, M-05, M-06, M-07 | Must |
| BR-02 | Committee work shall be routed to nominees according to their role, including people who hold two roles. | M-08 | Must |
| BR-03 | No committee meeting shall be signed off without its minutes on record. | M-10, M-11 | Must |
| BR-04 | Responsible people shall be reminded of pending committee actions in good time. | M-12 | Must |
| BR-05 | QPSD and management shall have a single report showing who ran each committee meeting, where and when, with its minutes. | M-13, M-14, M-15 | Must |
| BR-06 | The existing attendance and post-process workflow shall keep working without change. | M-09 | Must |

# 5. Functional requirements

## 5.1 Training Nominee Form

### FR-001 Training Nominee Form

**Description:** The system shall provide a Training Nominee Form in APEX for authorised users to nominate an employee against a committee training, using a minimum set of required fields.
**Priority:** Must
**Source:** M-01
**Business rules:** -
**Acceptance criteria:**
- AC1: Given an authorised user, when they open the Training Nominee Form, then they can enter a training, an employee and a role, and save the nomination.
- AC2 (negative): Given a user without access to the form, when they try to open it, then access is denied.
- AC3 (negative): Given a mandatory field is empty, when the user saves, then the save is refused and the field is highlighted with a message.
**Notes / open questions:** Q-01 (exact field list), Q-11 (does it replace the existing screen for committee trainings).

### FR-002 Committee training selection

**Description:** The system shall offer, in the Training field of the Training Nominee Form, only trainings that are active and whose category is marked as Committee.
**Priority:** Must
**Source:** M-02
**Business rules:** RULE-01
**Acceptance criteria:**
- AC1: Given an active training in a Committee category, when the user opens the Training list, then that training is listed.
- AC2 (negative): Given an inactive training in a Committee category, when the user opens the Training list, then it is not listed.
- AC3 (negative): Given an active training in a non-Committee category, when the user opens the Training list, then it is not listed.
**Notes / open questions:** -

### FR-003 Nominee role selection

**Description:** The system shall capture the nominee's committee role as a single selection from the values Chair, Secretary, Both and QA, in place of the existing Chair and Secretary checkboxes.
**Priority:** Must
**Source:** M-03, M-04
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given the Training Nominee Form, when the user opens the Role field, then exactly the four values Chair, Secretary, Both and QA are offered.
- AC2: Given any of the four values is selected, when the user saves, then the nomination is stored with that role.
- AC3 (negative): Given the Training Nominee Form, when the user looks for the Chair and Secretary checkboxes, then they are not shown.
**Notes / open questions:** Q-06 (existing checkbox data).

### FR-004 No default role

**Description:** The system shall show the Role field empty when a new nomination is started.
**Priority:** Must
**Source:** M-05
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given a new nomination, when the form opens, then the Role field shows no value.
- AC2 (negative): Given a new nomination, when the form opens, then none of Chair, Secretary, Both or QA is pre-selected.
**Notes / open questions:** -

### FR-005 Mandatory role on save

**Description:** The system shall refuse to save a nomination that has no role assigned.
**Priority:** Must
**Source:** M-06, M-07
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given a nomination with a role selected, when the user saves, then the nomination is saved.
- AC2 (negative): Given a nomination with no role, when the user saves, then the save is refused with the message "Please assign a role to the nominee." and no record is created or changed.
- AC3 (negative): Given an attempt to create a nomination with no role through any other path (for example a data load or API), when it is processed, then it is rejected.
**Notes / open questions:** Message wording to be confirmed by QPSD (A-04).

## 5.2 Queue management

### FR-006 Queue per role

**Description:** The system shall generate queue items for a saved nomination according to its role: one Chair item for Chair, one Secretary item for Secretary, and one QA item for QA.
**Priority:** Must
**Source:** M-08 (Inferred for single roles)
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a nomination saved with role Chair, when queues are generated, then exactly one Chair queue item exists for that nominee and meeting.
- AC2: Given a nomination saved with role QA, when queues are generated, then exactly one QA queue item exists for that nominee and meeting.
- AC3 (negative): Given a nomination saved with role Secretary, when queues are generated, then no Chair or QA item is created for it.
**Notes / open questions:** Q-02 (what a QA queue item is for), Q-10 (role changed after generation).

### FR-007 Separate queues for Both

**Description:** The system shall generate two separate queue items, one as Chair and one as Secretary, for a nomination with role Both.
**Priority:** Must
**Source:** M-08
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a nomination saved with role Both, when queues are generated, then the nominee has one Chair queue item and one Secretary queue item, each labelled with its role.
- AC2 (negative): Given a nomination with role Both, when queues are generated, then no single combined item is created.
**Notes / open questions:** -

### FR-008 Independent processing of Both queues

**Description:** The system shall track the status of the Chair and Secretary queue items of a Both nominee independently, so that completing one does not complete or close the other.
**Priority:** Must
**Source:** M-08
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a Both nominee with open Chair and Secretary items, when the Chair item is completed, then the Secretary item remains open.
- AC2 (negative): Given a Both nominee, when the Secretary item is completed, then the Chair item status does not change.
**Notes / open questions:** -

## 5.3 Committee Sign-off control

### FR-009 Minutes upload status on Queue screen

**Description:** The system shall show, on the Queue screen for a committee meeting, whether the Committee Minutes have been uploaded.
**Priority:** Must
**Source:** M-10
**Business rules:** RULE-04
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when the Queue screen opens, then the minutes status shows Uploaded.
- AC2 (negative): Given a meeting with no minutes uploaded, when the Queue screen opens, then the minutes status shows Pending.
**Notes / open questions:** Q-03 (who uploads), Q-07 (one or many files, formats).

### FR-010 Block sign-off without minutes

**Description:** The system shall not allow Committee Sign-off for a committee meeting until its Committee Minutes have been uploaded.
**Priority:** Must
**Source:** M-11
**Business rules:** RULE-04
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when an authorised user performs Committee Sign-off, then the sign-off is recorded.
- AC2 (negative): Given a meeting with no minutes uploaded, when a user attempts Committee Sign-off, then it is refused with the message "Committee Minutes must be uploaded before sign-off." and nothing is changed.
- AC3 (negative): Given a meeting with no minutes, when sign-off is attempted by any path other than the button (for example a direct page submit), then it is still refused.
**Notes / open questions:** Q-03 (which role signs off).

## 5.4 Alerts

### FR-011 Day-based alerts

**Description:** The system shall send system-generated alerts for committee meetings when the defined number of days for each alert is reached.
**Priority:** Must
**Source:** M-12
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given an alert defined at N days and a meeting that reaches that point, when the alert check runs, then the alert is sent to the defined recipients.
- AC2 (negative): Given a meeting that has not reached the defined number of days, when the alert check runs, then no alert is sent.
- AC3 (negative): Given an alert already sent for a meeting and event, when the alert check runs again, then the same alert is not sent twice.
**Notes / open questions:** Q-04 (events, recipients, channel, day values).

### FR-012 Maintain alert days

**Description:** The system shall allow an authorised administrator to set the number of days for each committee alert without a code change.
**Priority:** Should
**Source:** M-12 (Inferred from "defined number of days")
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given an administrator, when they change the number of days for an alert and save, then the next alert check uses the new value.
- AC2 (negative): Given a value that is not a whole number of zero or more, when the administrator saves, then the save is refused with a validation message.
**Notes / open questions:** Q-04.

## 5.5 Reports

### FR-013 Enhanced Committee Summary/Detail Report

**Description:** The system shall show, for each committee meeting in the Committee Summary/Detail Report, the Training/Committee Name, Location, Chair Name, Secretary Name, Planned Meeting Date and Actual Meeting Date.
**Priority:** Must
**Source:** M-13, M-14
**Business rules:** RULE-06
**Acceptance criteria:**
- AC1: Given a committee meeting with a Chair, a Secretary, a location, a planned date and a held meeting, when the report runs, then all six values are shown on that meeting's row.
- AC2: Given a nominee with role Both, when the report runs, then that person appears as both Chair Name and Secretary Name.
- AC3 (negative): Given a meeting not yet held, when the report runs, then Actual Meeting Date is blank and the row is still shown.
**Notes / open questions:** Q-05 (more than one Chair/Secretary), Q-08 (Location source), Q-09 (Actual date source).

### FR-014 Meeting Minutes in report

**Description:** The system shall provide, in the Committee Summary/Detail Report, access to the uploaded Committee Minutes of each meeting.
**Priority:** Could
**Source:** M-15 ("if feasible")
**Business rules:** -
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when an authorised user clicks the minutes link in the report, then the file opens or downloads.
- AC2 (negative): Given a meeting with no minutes, when the report runs, then no link is shown for that meeting.
**Notes / open questions:** Q-12 (feasibility decision).

# 6. Non-functional requirements

| ID | Category | Requirement | Measure / target | Source | Status |
|---|---|---|---|---|---|
| NFR-SEC-01 | Security | Only users with the training administration role shall create or change nominations. | Enforced by an APEX authorization scheme | Inferred | Proposed (not discussed in meeting) |
| NFR-SEC-02 | Security | Only authorised committee roles shall upload Committee Minutes and perform Committee Sign-off. | Enforced server-side, not only by hiding buttons | Inferred | Proposed (not discussed in meeting) |
| NFR-SEC-03 | Security | Committee Minutes shall be viewable only by users authorised for that committee or the report. | Access-checked download | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-01 | Audit | The system shall record created by, created on, modified by and modified on for every nomination, including role changes. | 100% of records | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-02 | Audit | The system shall record who uploaded the minutes and who performed Committee Sign-off, with date and time. | 100% of sign-offs | Inferred | Proposed (not discussed in meeting) |
| NFR-PERF-01 | Performance | The Training Nominee Form and Queue screen shall load within 3 seconds. | 95th percentile, hospital LAN | Inferred | Proposed (not discussed in meeting) |
| NFR-PERF-02 | Performance | The Committee Summary/Detail Report shall return one year of committee meetings within 10 seconds. | 95th percentile | Inferred | Proposed (not discussed in meeting) |
| NFR-AVL-01 | Availability | Deployment may need a short downtime of the Training Management Module, scheduled outside office hours. | Not a 24×7 clinical service | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-01 | Data | Committee Minutes shall not be deletable after Committee Sign-off and shall be retained per the hospital records policy. | Retention period per policy (Q-07) | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-02 | Data | The system shall prevent duplicate nominations of the same employee to the same committee meeting. | Unique check on save | Inferred | Proposed (not discussed in meeting) |
| NFR-USA-01 | Usability | Validation messages shall state what is missing and how to fix it, next to the field concerned. | Inline APEX messages | M-07, M-11 | Discussed |
| NFR-CMP-01 | Compliance | Committee Minutes and sign-off records shall be retrievable as evidence for accreditation audits (for example JCI). | Retrievable per meeting | Inferred | Proposed (not discussed in meeting) |
| NFR-INT-01 | Integration | Alerts shall be sent through the hospital's existing email and/or notification service. | No new external interface | M-12 | Proposed (not discussed in meeting) |
| NFR-OPS-01 | Operations | The alert check shall run as a scheduled job at least daily, and its failures shall be logged and visible to support. | Daily run; failures logged | M-12 | Proposed (not discussed in meeting) |

# 7. Business rules, data and access

## 7.1 Business rules

| ID | Rule | Applies to (FR) | Source |
|---|---|---|---|
| RULE-01 | A training is eligible for nomination on the Training Nominee Form only if its status is Active AND its category is marked Committee. | FR-002 | M-02 |
| RULE-02 | Every nominee has exactly one role from {Chair, Secretary, Both, QA}. No role is the default. A nomination without a role is invalid. | FR-003, FR-004, FR-005 | M-04, M-05, M-06, M-07 |
| RULE-03 | Queue items per nomination: Chair → 1 Chair; Secretary → 1 Secretary; QA → 1 QA; Both → 1 Chair + 1 Secretary, processed independently. | FR-006, FR-007, FR-008 | M-08 |
| RULE-04 | Committee Sign-off is allowed only when at least one Committee Minutes file is uploaded for the meeting. | FR-009, FR-010 | M-10, M-11 |
| RULE-05 | An alert is sent once per meeting and event, when the configured number of days for that event is reached. | FR-011, FR-012 | M-12 |
| RULE-06 | Report Chair Name = nominee(s) with role Chair or Both. Secretary Name = nominee(s) with role Secretary or Both. | FR-013 | M-14 |

## 7.2 Data requirements

| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
|---|---|---|---|---|---|
| Training / Committee | The committee training being nominated against | Yes | Must satisfy RULE-01 | "Infection Control Committee – Q4" | FR-001, FR-002 |
| Employee | The nominated employee | Yes | Active employee | EMP-TEST-0001 | FR-001 |
| Nominee role | The nominee's committee role | Yes | One of CHAIR, SECRETARY, BOTH, QA | BOTH | FR-003 to FR-005 |
| Queue role | The role a queue item is for | Yes | One of CHAIR, SECRETARY, QA | SECRETARY | FR-006 to FR-008 |
| Location | Where the meeting is held | To be confirmed (Q-08) | Text or location list | "Board Room 2" | FR-013 |
| Planned Meeting Date | Scheduled date of the meeting | Yes | Date | 2026-11-15 | FR-013 |
| Actual Meeting Date | Date the meeting was actually held | No (blank until held) | Date, not in the future | 2026-11-17 | FR-013 |
| Committee Minutes file | Uploaded minutes document | Yes before sign-off | Allowed types and size to be confirmed (Q-07) | minutes_test.pdf | FR-009, FR-010, FR-014 |
| Minutes uploaded by / on | Who uploaded the minutes, and when | Yes (system) | System-set | EMP-TEST-0002, 2026-11-18 10:05 | FR-009 |
| Sign-off by / on | Who signed off, and when | Yes (system) | System-set | EMP-TEST-0003, 2026-11-19 14:30 | FR-010 |
| Alert days | Number of days that triggers an alert | Yes | Whole number ≥ 0 | 3 | FR-011, FR-012 |

## 7.3 User roles and access matrix

| Function / screen | Training Admin / Coordinator | Chair | Secretary | QA | QPSD / Management | System Admin |
|---|---|---|---|---|---|---|
| Training Nominee Form | C R U D | - | - | - | R | - |
| Chair queue | R | R U | - | - | R | - |
| Secretary queue | R | - | R U | - | R | - |
| QA queue | R | - | - | R U | R | - |
| Upload Committee Minutes | - | To be confirmed (Q-03) | C R (assumed, A-03) | - | R | - |
| Committee Sign-off | - | A (assumed, Q-03) | - | - | - | - |
| Alert day setup | - | - | - | - | - | C R U |
| Committee Summary/Detail Report | R | R | R | R | R | - |

## 7.4 Reports and notifications

| Report / notification | Audience | Trigger / frequency | Content | Related FR |
|---|---|---|---|---|
| Committee Summary/Detail Report | QPSD, management, committee members | On demand | Training/Committee Name, Location, Chair Name, Secretary Name, Planned and Actual Meeting Date, minutes link (if feasible) | FR-013, FR-014 |
| Committee alert(s) | To be confirmed (Q-04) | Configured number of days, checked daily | To be confirmed (Q-04) | FR-011 |
| Sign-off refusal message | User attempting sign-off | On attempt without minutes | "Committee Minutes must be uploaded before sign-off." | FR-010 |

## 7.5 Interfaces

| System | Direction (in/out) | Data exchanged | Frequency | Related FR |
|---|---|---|---|---|
| Hospital email / notification service | Out | Alert messages | Per alert job run (daily) | FR-011 |

# 8. Impact analysis

> Schema context used: none — the HRD system context is not yet indexed. **This impact analysis is PROVISIONAL.** Every object name must be verified against the HRD schema before design.

## 8.1 Business impact

| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
|---|---|---|---|---|
| IMP-01 | Training coordinators (nomination process) | Use the new Nominee Form for committee trainings; must assign a role to every nominee. Short user briefing needed. | FR-001 to FR-005 | N |
| IMP-02 | Committee Chairs, Secretaries and QA nominees | Work separate role-based queues; Both nominees see two items. | FR-006 to FR-008 | N |
| IMP-03 | Committee governance (QPSD) | Sign-off now depends on minutes upload; meetings without minutes stay open. SOP on minutes upload may need updating. | FR-009, FR-010 | N |
| IMP-04 | QPSD / management reporting | Enhanced report gives evidence for audits and accreditation. | FR-013, FR-014 | N |

## 8.2 System impact

| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|
| IMP-05 | Training Management APEX app: Training Nominee Form page | New | New form page with Training LOV (RULE-01), Employee, Role LOV `LOV_NOMINEE_ROLE` NEW (proposed) and validations | FR-001 to FR-005 | MoM M-01 | PROVISIONAL – not verified |
| IMP-06 | Existing nominee screen (TO BE CONFIRMED) | Modify / Retire | Remove Chair and Secretary checkboxes; decide whether committee nominations move to the new form (Q-11) | FR-003 | MoM M-03 | PROVISIONAL – not verified |
| IMP-07 | Queue generation logic (package TO BE CONFIRMED) | Modify | Generate queue items from the role; two items for Both | FR-006 to FR-008 | MoM M-08 | PROVISIONAL – not verified |
| IMP-08 | Queue screen (APEX page TO BE CONFIRMED) | Modify | Show minutes status; server-side sign-off check | FR-009, FR-010 | MoM M-10, M-11 | PROVISIONAL – not verified |
| IMP-09 | Committee alert scheduled job | New / Modify | Daily DBMS_SCHEDULER job that sends day-based alerts; reuse an existing alert job if one exists | FR-011 | MoM M-12 | PROVISIONAL – not verified |
| IMP-10 | Alert day setup page | New | Admin page to maintain alert days | FR-012 | Inferred | PROVISIONAL – not verified |
| IMP-11 | Committee Summary/Detail Report | Modify | Add six columns and an optional minutes link | FR-013, FR-014 | MoM M-13 to M-15 | PROVISIONAL – not verified |
| IMP-12 | APEX authorization schemes | Modify | Access to the new form, minutes upload, sign-off and alert setup | NFR-SEC-01, NFR-SEC-02 | Inferred | PROVISIONAL – not verified |
| IMP-13 | Attendance and post-process | Read-only | No change; regression test only | - | MoM M-09 | PROVISIONAL – not verified |

## 8.3 Database impact

| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|
| IMP-14 | Training category table: Committee indicator (TO BE CONFIRMED) | Read-only / Modify | Used by the Training LOV filter; add the indicator if it does not exist | Training LOVs, reports | Flag existing committee categories | FR-002 | MoM M-02 | PROVISIONAL – not verified |
| IMP-15 | Nominee table: role column (TO BE CONFIRMED; NEW column proposed) | Modify | Single mandatory role, values CHAIR, SECRETARY, BOTH, QA, with a check constraint | Nominee screens, queue logic, reports | Map existing checkbox values (Q-06) | FR-003 to FR-005 | MoM M-03 to M-07 | PROVISIONAL – not verified |
| IMP-16 | Nominee table: Chair and Secretary flag columns (TO BE CONFIRMED) | Retire | Retire after migration to the role column | Any object reading the flags | Migrated into IMP-15 | FR-003 | MoM M-03 | PROVISIONAL – not verified |
| IMP-17 | Queue table: queue role (TO BE CONFIRMED) | Modify | One row per role; two rows for Both | Queue screen, sign-off | None expected | FR-006 to FR-008 | MoM M-08 | PROVISIONAL – not verified |
| IMP-18 | Committee Minutes storage (TO BE CONFIRMED) | Read-only / New | File, file name, MIME type, uploaded by/on per meeting; sign-off by/on | Queue screen, report | None | FR-009, FR-010, FR-014 | MoM M-10 | PROVISIONAL – not verified |
| IMP-19 | `HRD_TRAINING_ALERT_MST` NEW (proposed) | New | Alert type, number of days, active flag | Alert job | Seed initial values (Q-04) | FR-011, FR-012 | Inferred | PROVISIONAL – not verified |
| IMP-20 | `HRD_TRAINING_ALERT_LOG` NEW (proposed) | New | Sent alerts, to prevent duplicates | Alert job | None | FR-011 | Inferred | PROVISIONAL – not verified |

## 8.4 Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Legacy nominee records with neither checkbox ticked cannot be mapped to a role | Medium | Medium | Agree a migration rule with QPSD (Q-06); report unmapped records before go-live |
| Open committee meetings without minutes become blocked at go-live | Medium | Medium | List open meetings without minutes before deployment and inform Secretaries |
| Changes to queue logic affect attendance or post-process | Low | High | Full regression test of attendance and post-process (M-09) |
| Alert rules unclear, leading to too many or missed alerts | Medium | Low | Resolve Q-04 before design; configurable days (FR-012) |

# 9. Assumptions, constraints and dependencies

## 9.1 Assumptions

| ID | Assumption | Needs confirmation from |
|---|---|---|
| A-01 | Training categories have, or can be given, a Committee indicator. | Solution Architect |
| A-02 | The existing queue mechanism can hold one item per role per nominee. | Solution Architect |
| A-03 | The Secretary uploads the Committee Minutes and the Chair performs Committee Sign-off. | QPSD |
| A-04 | Validation message wording in this SRS is a draft and may be changed by QPSD. | QPSD |
| A-05 | Priorities are Must where the MoM states the point as agreed, unless "if feasible" is stated. | BA |
| A-06 | Only employee data is involved; no patient data. | BA |

## 9.2 Constraints

- Build in Oracle APEX on the HRD schema (M-01).
- The existing attendance and post-process workflow must not change (M-09).
- New objects follow the HRD naming standards (oracle-plsql-apex-hrd-standards).

## 9.3 Dependencies

- QPSD answers to the blocking open questions (Q-01 to Q-05, Q-11).
- A verified HRD schema snapshot for the impact analysis.
- An available email/notification service for alerts.

# 10. Open questions

| ID | Question | Raised because (M-NN / FR) | Addressed to | Blocking? |
|---|---|---|---|---|
| Q-01 | What are the "minimum required fields" on the Training Nominee Form? | M-01, FR-001 | QPSD | Yes |
| Q-02 | What does each queue (Chair, Secretary, QA) let the nominee do? What is the QA role's task? | M-04, M-08, FR-006 | QPSD | Yes |
| Q-03 | Which role uploads the Committee Minutes, and which role performs Committee Sign-off? | M-10, M-11, FR-009, FR-010 | QPSD | Yes |
| Q-04 | Which alerts are needed: event (e.g. before planned date, minutes overdue, sign-off pending), recipients, channel (email/APEX/SMS) and number of days for each? | M-12, FR-011 | QPSD | Yes |
| Q-05 | Can a committee meeting have more than one Chair or Secretary? Should the system restrict it to one each? | M-14, FR-013 | QPSD | Yes |
| Q-06 | How should existing nominee records be migrated, especially those with neither checkbox ticked? | M-03, FR-003 | QPSD | No |
| Q-07 | Can a meeting have more than one minutes file? Allowed file types, maximum size and retention period? | M-10, FR-009 | QPSD / SA | No |
| Q-08 | Where does Location come from: the training schedule or the Nominee Form? | M-14, FR-013 | QPSD / SA | No |
| Q-09 | What is the source of the Actual Meeting Date: attendance date or a separately entered date? | M-14, FR-013 | QPSD / SA | No |
| Q-10 | Can a nominee's role be changed after queue items exist? If yes, what happens to open and completed items? | M-08, FR-006 | QPSD | No |
| Q-11 | Does the new Training Nominee Form replace the existing nominee screen for committee trainings, or sit alongside it? | M-01, M-03 | QPSD / SA | Yes |
| Q-12 | Is the Meeting Minutes link in the report in scope for this release? | M-15, FR-014 | Solution Architect | No |
| Q-13 | What is the CR / ticket number for this change? | Document ID | BA | No |
| Q-14 | What were the meeting date and attendees? Please confirm the QPSD expansion. | MoM header | BA | No |

# Appendix A. Minutes of meeting breakdown

| M-ID | Original statement | Type | Mapped to |
|---|---|---|---|
| M-01 | A new Training Nominee Form with minimum required fields will be developed in APEX. | Requirement | BR-01, FR-001, Q-01, Q-11 |
| M-02 | Only active trainings whose category is marked as Committee will be available for selection. | Requirement | BR-01, FR-002, RULE-01 |
| M-03 | The existing Chair/Secretary checkboxes will be replaced with a List of Values (LOV). | Decision | BR-01, FR-003, Q-06 |
| M-04 | The LOV will contain the following options: Chair, Secretary, Both, and QA. | Requirement | FR-003, RULE-02 |
| M-05 | By default, no role will be selected. | Requirement | FR-004, RULE-02 |
| M-06 | Role assignment will be mandatory for every nominee. | Requirement | FR-005, RULE-02 |
| M-07 | The system will not allow the record to be saved without assigning a role. | Requirement | FR-005, RULE-02, NFR-USA-01 |
| M-08 | If Both is selected, separate queues will be generated and managed for the nominee as Chair and Secretary. | Requirement | BR-02, FR-006, FR-007, FR-008, RULE-03, Q-10 |
| M-09 | The existing attendance and post-process workflow will remain unchanged. | Constraint | BR-06, Out of scope, 9.2 |
| M-10 | On the Queue screen, the system will check whether the Committee Minutes have been uploaded. | Requirement | BR-03, FR-009, RULE-04 |
| M-11 | Committee Sign-off will not be allowed until the Committee Minutes are uploaded. | Requirement | BR-03, FR-010, RULE-04, Q-03 |
| M-12 | System-generated alerts will be sent according to the defined number of days. | Requirement | BR-04, FR-011, FR-012, RULE-05, Q-04 |
| M-13 | Enhance the Committee Summary/Detail Report. | Requirement | BR-05, FR-013 |
| M-14 | Report to include Training/Committee Name, Location, Chair Name, Secretary Name, Planned Meeting Date, Actual Meeting Date. | Requirement | FR-013, RULE-06, Q-05, Q-08, Q-09 |
| M-15 | Report to include Meeting Minutes attachment (if feasible). | Requirement | FR-014, Q-12 |
| M-16 | Action: Development to be carried out as per the above agreed requirements. | Action item | Whole SRS |

# Appendix B. Requirement traceability

| Requirement | Source (M-NN) | Impact items (IMP-NN) |
|---|---|---|
| FR-001 | M-01 | IMP-01, IMP-05 |
| FR-002 | M-02 | IMP-05, IMP-14 |
| FR-003 | M-03, M-04 | IMP-05, IMP-06, IMP-15, IMP-16 |
| FR-004 | M-05 | IMP-05, IMP-15 |
| FR-005 | M-06, M-07 | IMP-01, IMP-05, IMP-15 |
| FR-006 | M-08 | IMP-02, IMP-07, IMP-17 |
| FR-007 | M-08 | IMP-02, IMP-07, IMP-17 |
| FR-008 | M-08 | IMP-02, IMP-07, IMP-17 |
| FR-009 | M-10 | IMP-03, IMP-08, IMP-18 |
| FR-010 | M-11 | IMP-03, IMP-08, IMP-18 |
| FR-011 | M-12 | IMP-09, IMP-19, IMP-20 |
| FR-012 | M-12 | IMP-10, IMP-19 |
| FR-013 | M-13, M-14 | IMP-04, IMP-11 |
| FR-014 | M-15 | IMP-04, IMP-11, IMP-18 |
| NFR-SEC-01, NFR-SEC-02 | Inferred | IMP-12 |
| BR-06 | M-09 | IMP-13 |
