# 1. Introduction

## 1.1 Purpose
This SRS specifies the requirements for the **Committee Workflow Enhancements for QPSD** in the Training Management Module. It covers a new APEX Training Nominee Form, mandatory nominee role assignment through a List of Values (LOV), queue generation for the Chair and Secretary roles, a Committee Minutes check before Committee Sign-off, alerts based on a defined number of days, and an enhanced Committee Summary/Detail Report. The audience is the Solution Architect (for review and approval), developers, QA and the QPSD business owners.

## 1.2 Background
Committees run by QPSD are managed as trainings in the Training Management Module. Today, nominee roles are captured with separate Chair and Secretary checkboxes. These allow a nominee to be saved with no role, and they have no option for a QA role. The meeting also agreed that:
- committee nominees should be entered on a simple, dedicated form that only shows committee trainings;
- a nominee who is both Chair and Secretary needs a separate queue for each role;
- a committee meeting should not be signed off until its minutes are uploaded, so that every signed-off meeting has documented evidence;
- reminders should go out automatically after a defined number of days;
- management needs one report showing each committee meeting with its Chair, Secretary, planned and actual dates and minutes.

## 1.3 Scope
### In scope
- New Training Nominee Form in Oracle APEX with the minimum required fields (M-03, M-04).
- Replacement of the Chair/Secretary checkboxes with a mandatory Role LOV: Chair, Secretary, Both, QA (M-05 to M-09).
- Queue generation per role, including two separate queues for a nominee with role Both (M-10).
- Committee Minutes upload check and blocking of Committee Sign-off on the Queue screen (M-12, M-13).
- System-generated alerts based on a defined number of days (M-14).
- Enhancement of the Committee Summary/Detail Report (M-15 to M-21).

### Out of scope
- Any change to the existing attendance workflow (M-11).
- Any change to the existing post-process workflow (M-11).
- Trainings whose category is not marked as Committee. They stay on the existing nominee process (M-04).

## 1.4 Stakeholders
| Name / Role | Department | Interest / responsibility | Attended meeting |
|---|---|---|---|
| QPSD business owner (name TBC, Q-01) | QPSD | Owns the committee process; approves requirements | TBC |
| Committee Chair (nominee) | Various | Works the Chair queue; signs off the committee | No |
| Committee Secretary (nominee) | Various | Works the Secretary queue; uploads minutes (TBC, Q-09) | No |
| QA nominee | QPSD (TBC) | Committee member with the QA role (responsibilities TBC, Q-04) | No |
| Training administrator | Training / HR (TBC) | Maintains training master and categories | TBC |
| Management / report users | QPSD and management | Use the Committee Summary/Detail Report | TBC |
| Business Analyst | IT / Software Development | Owns this SRS | Yes (assumed) |
| Solution Architect | IT / Software Development | Reviews and approves the SRS (Gate 1) | TBC |

## 1.5 Definitions and abbreviations
| Term | Meaning |
|---|---|
| QPSD | Department that owns the committees. Expansion to be confirmed (Q-01) |
| APEX | Oracle Application Express, the web development platform |
| LOV | List of Values (drop-down list) |
| Committee training | A training whose category is marked as Committee |
| Nominee | Employee nominated as a member of a committee training |
| Queue | Work list for a user in a given role (for example, the Chair queue) where actions such as sign-off are taken |
| Committee Minutes | The minutes-of-meeting document uploaded for a committee meeting |
| Committee Sign-off | The action on the Queue screen that formally closes a committee meeting |
| Planned Meeting Date | The date the committee meeting is scheduled for |
| Actual Meeting Date | The date the committee meeting actually took place |

## 1.6 References
- Discussion notes: "Committee Workflow Enhancements (for QPSD)", Training Management Module (meeting date TBC, Q-01).
- Existing Training Management Module screens: nominee entry with Chair/Secretary checkboxes, Queue screen, attendance and post-process, Committee Summary/Detail Report (names to be confirmed, Q-07).
- SKMCH SDLC conventions and HRD naming standards.

# 2. Current state (As-Is)
Based on the discussion notes (details to be confirmed against the live system):
1. Committees are configured as trainings. A training category can be marked as Committee.
2. Nominees are added to a training on the existing nominee screen. The roles Chair and Secretary are set with two checkboxes. A nominee can be saved with neither box ticked, and there is no QA role.
3. Queues are generated for nominees and are used for committee actions, including Committee Sign-off.
4. Attendance and post-process are carried out through the existing workflow.
5. Committee Sign-off can be performed without checking whether the Committee Minutes have been uploaded.
6. The Committee Summary/Detail Report does not show all of: committee name, location, Chair, Secretary, planned and actual meeting dates and minutes.

Pain points: nominees without a role; no QA role; no control that minutes exist before sign-off; no automated reminders; limited reporting.

# 3. Proposed solution overview (To-Be)
1. A QPSD user opens the new **Training Nominee Form** in APEX.
2. The user selects a training. Only **active** trainings in a **Committee** category are listed.
3. The user adds nominees and selects a **Role** for each one from the LOV (Chair, Secretary, Both, QA). No role is pre-selected. The record cannot be saved until a role is selected.
4. On save, the system generates queue entries: a Chair queue entry for Chair, a Secretary queue entry for Secretary, and **two separate entries (one Chair, one Secretary)** for Both. QA queue handling is to be confirmed (Q-04).
5. Attendance and post-process continue exactly as today.
6. On the **Queue screen**, the system shows whether the Committee Minutes have been uploaded. **Committee Sign-off is blocked until the minutes are uploaded.**
7. A scheduled process sends **alerts** when the defined number of days has passed (events and recipients TBC, Q-11).
8. Management runs the enhanced **Committee Summary/Detail Report** to see each committee meeting with its name, location, Chair, Secretary, planned and actual meeting dates, and minutes attachment (if feasible).

# 4. Business requirements
| ID | Business requirement | Source (M-NN) | Priority |
|---|---|---|---|
| BR-01 | QPSD shall be able to nominate committee members for committee trainings through a simple, dedicated form. | M-03, M-04 | Must |
| BR-02 | Every committee nominee shall have one clearly defined committee role. | M-05, M-06, M-07, M-08, M-09 | Must |
| BR-03 | Chair and Secretary responsibilities shall be tracked separately, including when one person holds both roles. | M-10 | Must |
| BR-04 | A committee meeting shall not be signed off without documented minutes. | M-12, M-13 | Must |
| BR-05 | Responsible people shall be reminded automatically when committee actions become due or overdue. | M-14 | Must |
| BR-06 | Management shall have consolidated visibility of committee meetings, their office bearers, dates and minutes. | M-15 to M-21 | Must |

# 5. Functional requirements

## 5.1 Training Nominee Form

### FR-001 Training Nominee Form in APEX
**Description:** The system shall provide a Training Nominee Form in Oracle APEX on which an authorised QPSD user can add nominees to a committee training.
**Priority:** Must
**Source:** M-03
**Business rules:** RULE-01, RULE-02
**Acceptance criteria:**
- AC1: Given an authorised QPSD user, when they open the Training Nominee Form, then they can select a committee training and add one or more nominees to it.
- AC2 (negative): Given a user without the QPSD nominee authorisation, when they try to open the form, then access is denied and no data is shown.
**Notes / open questions:** Q-02 (minimum field list), Q-03 (training vs. session/meeting level), Q-07 (fate of the existing nominee screen).

### FR-002 Committee trainings only in training selection
**Description:** The system shall list in the training selection of the Training Nominee Form only trainings that are active and whose category is marked as Committee.
**Priority:** Must
**Source:** M-04
**Business rules:** RULE-01
**Acceptance criteria:**
- AC1: Given an active training in a category marked as Committee, when the user opens the training selection, then that training is listed.
- AC2 (negative): Given an inactive training in a Committee category, when the user opens the training selection, then that training is not listed.
- AC3 (negative): Given an active training in a category not marked as Committee, when the user opens the training selection, then that training is not listed.
**Notes / open questions:** Q-13 (definition of "active").

### FR-003 Minimum mandatory fields
**Description:** The system shall require the minimum fields agreed for a nominee record before the record can be saved.
**Priority:** Must
**Source:** M-03
**Acceptance criteria:**
- AC1: Given all mandatory fields are entered, when the user saves, then the nominee record is saved.
- AC2 (negative): Given any mandatory field is blank, when the user saves, then the save is blocked and the blank field is highlighted with the message "<Field> is required".
**Notes / open questions:** Q-02. Proposed minimum set (to confirm): Training/Committee, Meeting/Session (if applicable, Q-03), Employee (nominee), Role.

### FR-004 No duplicate nominee per committee training (Inferred)
**Description:** The system shall prevent the same employee from being nominated more than once for the same committee training (or meeting, see Q-03).
**Priority:** Should
**Source:** Inferred (supports M-10: "Both" is the way to give one person two roles)
**Business rules:** RULE-07
**Acceptance criteria:**
- AC1: Given an employee not yet nominated for the training, when the user adds them, then the record is saved.
- AC2 (negative): Given an employee already nominated for the training, when the user adds them again, then the save is blocked with the message "Employee is already a nominee for this committee. Change the existing role instead."
**Notes / open questions:** Q-05.

## 5.2 Nominee role assignment

### FR-005 Role LOV replaces Chair/Secretary checkboxes
**Description:** The system shall capture the nominee's committee role through a single Role LOV, which replaces the existing Chair and Secretary checkboxes.
**Priority:** Must
**Source:** M-05
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given the Training Nominee Form (and the existing nominee screen, if retained, Q-07), when the user views a nominee row, then a Role LOV is shown and no Chair or Secretary checkboxes are shown.
- AC2 (negative): Given a nominee record, when the user tries to set Chair or Secretary through any other control, then no such control exists.

### FR-006 Role LOV values
**Description:** The system shall offer exactly the following values in the Role LOV: Chair, Secretary, Both, QA.
**Priority:** Must
**Source:** M-06
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given the Role LOV, when the user opens it, then exactly the values Chair, Secretary, Both and QA are listed.
- AC2 (negative): Given the Role LOV, when the user tries to type or submit any other value, then the value is rejected.

### FR-007 No default role
**Description:** The system shall show the Role LOV with no value selected when a new nominee is added.
**Priority:** Must
**Source:** M-07
**Acceptance criteria:**
- AC1: Given a new nominee row, when it is created, then the Role LOV shows a blank/"- Select Role -" prompt.
- AC2 (negative): Given a new nominee row, when the user saves without touching the Role LOV, then no role is stored implicitly (see FR-008).

### FR-008 Role is mandatory
**Description:** The system shall block saving a nominee record that has no role selected.
**Priority:** Must
**Source:** M-08, M-09
**Business rules:** RULE-02
**Acceptance criteria:**
- AC1: Given a nominee with a role selected, when the user saves, then the record is saved.
- AC2 (negative): Given a nominee with no role selected, when the user saves, then the save is blocked, the Role field is highlighted, the message "Role is required for every nominee" is shown, and no record (and no queue entry) is created.
- AC3 (negative): Given several nominee rows where one has no role, when the user saves, then none of the invalid rows is saved and the user is told which row is missing a role.

### FR-009 Existing nominee records receive a role (Inferred)
**Description:** The system shall convert existing nominee records from the Chair/Secretary checkboxes to the new Role value, according to the agreed mapping, before the new form goes live.
**Priority:** Must
**Source:** Inferred from M-05, M-08
**Acceptance criteria:**
- AC1: Given an existing nominee with only Chair ticked, after conversion the role is Chair; only Secretary ticked → Secretary; both ticked → Both.
- AC2 (negative): Given an existing nominee with neither box ticked, after conversion the record is reported in a conversion exception list for QPSD to resolve, and is not silently assigned a role.
**Notes / open questions:** Q-06.

## 5.3 Queue management

### FR-010 Queue entry per role
**Description:** The system shall generate a Chair queue entry for a nominee with role Chair, and a Secretary queue entry for a nominee with role Secretary.
**Priority:** Must
**Source:** M-10 (and existing behaviour)
**Business rules:** RULE-03, RULE-04
**Acceptance criteria:**
- AC1: Given a nominee saved with role Chair, when queues are generated, then exactly one Chair queue entry exists for that nominee and meeting.
- AC2 (negative): Given a nominee saved with role Chair, when queues are generated, then no Secretary queue entry exists for that nominee.
**Notes / open questions:** Q-04 (QA queue), Q-08 (queue timing and actions).

### FR-011 Separate queues for role Both
**Description:** The system shall generate and manage two separate queue entries, one as Chair and one as Secretary, for a nominee with role Both.
**Priority:** Must
**Source:** M-10
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a nominee saved with role Both, when queues are generated, then one Chair queue entry and one Secretary queue entry exist for that nominee, each clearly labelled with its role.
- AC2: Given a nominee with role Both, when they complete the action in the Secretary queue entry, then the Chair queue entry stays open and is not affected (and vice versa).
- AC3 (negative): Given a nominee with role Both, when queues are regenerated or the record is re-saved, then no duplicate Chair or Secretary queue entries are created.

### FR-012 Queue update on role change (Inferred)
**Description:** The system shall update the nominee's queue entries when their role is changed before any action has been taken on those queue entries.
**Priority:** Should
**Source:** Inferred from M-10
**Acceptance criteria:**
- AC1: Given a nominee with role Chair and an untouched Chair queue entry, when the role is changed to Both, then a Secretary queue entry is added and the Chair entry remains.
- AC2 (negative): Given a queue entry that has already been actioned (for example, signed off), when the user tries to change the nominee's role, then the change is blocked with the message "Role cannot be changed after queue action has been taken".
**Notes / open questions:** Q-15.

## 5.4 Attendance and post-process

### FR-013 Existing attendance and post-process unchanged
**Description:** The system shall continue to use the existing attendance and post-process workflow, unchanged, for nominees added through the Training Nominee Form.
**Priority:** Must
**Source:** M-11
**Acceptance criteria:**
- AC1: Given nominees added through the new form with any role, when attendance is marked, then the existing attendance screen and rules work exactly as today.
- AC2 (negative): Given a nominee with role Both, when attendance is marked, then the nominee appears only once in attendance (not once per queue).
**Notes / open questions:** Q-16.

## 5.5 Committee Sign-off control

### FR-014 Minutes upload status on Queue screen
**Description:** The system shall show on the Queue screen whether the Committee Minutes have been uploaded for the committee meeting of each queue entry.
**Priority:** Must
**Source:** M-12
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when the queue entry is shown, then its minutes status is "Uploaded".
- AC2 (negative): Given a meeting without minutes, when the queue entry is shown, then its minutes status is "Not uploaded".

### FR-015 Block Committee Sign-off without minutes
**Description:** The system shall not allow Committee Sign-off for a committee meeting until the Committee Minutes for that meeting have been uploaded.
**Priority:** Must
**Source:** M-13
**Business rules:** RULE-05
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when the authorised user performs Committee Sign-off, then the sign-off is recorded.
- AC2 (negative): Given a meeting without minutes, when the user tries Committee Sign-off, then sign-off is blocked with the message "Committee Minutes must be uploaded before sign-off" and the queue entry stays open.
- AC3 (negative): Given minutes that were uploaded and then removed, when the user tries Committee Sign-off, then sign-off is blocked as in AC2.
**Notes / open questions:** Q-09 (who uploads, file rules), Q-10 (which role signs off).

## 5.6 Alerts

### FR-016 Day-based alerts
**Description:** The system shall send system-generated alerts to the defined recipients when the defined number of days for an alert event has been reached.
**Priority:** Must
**Source:** M-14
**Business rules:** RULE-06
**Acceptance criteria:**
- AC1: Given an alert event configured for N days and a meeting that reaches day N, when the alert process runs, then the alert is sent once to the defined recipients.
- AC2 (negative): Given a meeting whose triggering condition has been resolved (for example, minutes uploaded or sign-off completed), when the alert process runs, then no alert is sent for that event.
- AC3 (negative): Given an alert already sent for an event and meeting, when the alert process runs again the next day, then no duplicate is sent unless repeat alerts are configured (Q-11).
**Notes / open questions:** Q-11 (events, recipients, channel, repeat rule).

### FR-017 Maintain alert day settings (Inferred)
**Description:** The system shall allow an authorised administrator to maintain the number of days for each alert event without a code change.
**Priority:** Should
**Source:** Inferred from M-14 ("defined number of days")
**Acceptance criteria:**
- AC1: Given an administrator, when they change the number of days for an alert event, then the next alert run uses the new value.
- AC2 (negative): Given an administrator, when they enter zero, a negative number or a non-number, then the save is blocked with a validation message.
**Notes / open questions:** Q-11.

## 5.7 Committee Summary/Detail Report

### FR-018 Report content
**Description:** The system shall show the following for each committee meeting in the Committee Summary/Detail Report: Training/Committee Name, Location, Chair Name, Secretary Name, Planned Meeting Date and Actual Meeting Date.
**Priority:** Must
**Source:** M-15, M-16, M-17, M-18, M-19, M-20
**Business rules:** RULE-03
**Acceptance criteria:**
- AC1: Given a committee meeting with a Chair, a Secretary, a location, a planned date and an actual date, when the report is run, then all six values are shown on that meeting's row.
- AC2: Given a nominee with role Both, when the report is run, then that person's name is shown as both Chair Name and Secretary Name.
- AC3 (negative): Given a meeting that has not yet taken place, when the report is run, then Actual Meeting Date is blank and the row is still shown.
**Notes / open questions:** Q-12 (report identity, source of dates and location, multiple Chairs).

### FR-019 Meeting minutes in report (if feasible)
**Description:** The system shall allow a report user to open or download the uploaded Committee Minutes from the Committee Summary/Detail Report.
**Priority:** Could
**Source:** M-21
**Acceptance criteria:**
- AC1: Given a meeting with minutes uploaded, when the user clicks the minutes link on the report, then the minutes document opens or downloads.
- AC2 (negative): Given a meeting without minutes, when the report is run, then the minutes column shows "Not uploaded" and has no link.
- AC3 (negative): Given a user not authorised to view minutes, when they run the report, then no download link is shown (NFR-SEC-02).
**Notes / open questions:** Feasibility to be confirmed in design (Q-12).

# 6. Non-functional requirements
| ID | Category | Requirement | Measure / target | Source | Status |
|---|---|---|---|---|---|
| NFR-SEC-01 | Security & access | The Training Nominee Form and alert settings shall be available only to authorised roles, using an APEX authorization scheme. | Unauthorised access denied in 100% of test cases | Inferred | Proposed (not discussed in meeting) |
| NFR-SEC-02 | Security & access | Committee Minutes shall be viewable only by committee nominees, authorised QPSD users and authorised report users. | Access test per role in §7.3 | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-01 | Audit | Nominee records shall record created by/on and modified by/on, and role changes shall keep history (old role, new role, user, timestamp). | All changes traceable | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-02 | Audit | Minutes upload and Committee Sign-off shall record the user and timestamp. | All actions traceable | Inferred | Proposed (not discussed in meeting) |
| NFR-AUD-03 | Audit | Each alert sent shall be logged with event, meeting, recipient and timestamp. | 100% of alerts logged | Inferred | Proposed (not discussed in meeting) |
| NFR-PERF-01 | Performance | The Training Nominee Form, training LOV and Queue screen shall load within 3 seconds. | 95th percentile, hospital LAN | Inferred | Proposed (not discussed in meeting) |
| NFR-PERF-02 | Performance | The Committee Summary/Detail Report shall return within 10 seconds for a 12-month date range. | 95th percentile | Inferred | Proposed (not discussed in meeting) |
| NFR-AVL-01 | Availability | Deployment shall be done outside office hours. Committee functions are not 24×7 clinical services. | No downtime during office hours | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-01 | Data quality | Minutes uploads shall accept agreed file types and size only. | Proposed: PDF, DOC, DOCX; max 10 MB (Q-09) | Inferred | Proposed (not discussed in meeting) |
| NFR-DAT-02 | Data retention | Committee Minutes and sign-off records shall be retained per hospital records policy and shall not be deleted after sign-off. | Retention period TBC (Q-09) | Inferred | Proposed (not discussed in meeting) |
| NFR-USA-01 | Usability | Validation messages shall appear inline next to the field, in plain English, and the user's entered data shall be kept. | All validations in §5 | Inferred | Proposed (not discussed in meeting) |
| NFR-CMP-01 | Compliance | Committee meeting records (minutes, sign-off, attendance) shall be available as evidence for accreditation/quality audits (e.g. JCI). | Report and minutes retrievable per meeting | Inferred | Proposed (not discussed in meeting) |
| NFR-INT-01 | Integration | Alerts shall use the hospital's existing notification channel (e.g. email via APEX mail). | Channel TBC (Q-11) | M-14 | Proposed (not discussed in meeting) |
| NFR-OPS-01 | Operations | The alert process shall run as a scheduled job at least once a day, and job failures shall be logged and visible to support. | Daily run; failures logged | M-14 | Proposed (not discussed in meeting) |

# 7. Business rules, data and access

## 7.1 Business rules
| ID | Rule | Applies to (FR) | Source |
|---|---|---|---|
| RULE-01 | A training is selectable on the Training Nominee Form only if it is active and its category is marked as Committee. | FR-002 | M-04 |
| RULE-02 | Every nominee has exactly one role from {Chair, Secretary, Both, QA}. No role is pre-selected, and a record without a role cannot be saved. | FR-005 to FR-009 | M-05 to M-09 |
| RULE-03 | Role Both means the nominee acts as Chair and as Secretary. Two separate queue entries are generated, and the name is shown as both Chair and Secretary in reports. | FR-011, FR-018 | M-10 |
| RULE-04 | Role QA does not generate a Chair or Secretary queue entry. Any QA queue is TBC. | FR-010 | Inferred, Q-04 |
| RULE-05 | Committee Sign-off is allowed only when at least one Committee Minutes document is uploaded for that meeting. | FR-014, FR-015 | M-12, M-13 |
| RULE-06 | Alerts are sent when the defined number of days for the alert event is reached and the triggering condition is still open. | FR-016, FR-017 | M-14 |
| RULE-07 | An employee can be nominated only once per committee training/meeting. | FR-004 | Inferred, Q-05 |

## 7.2 Data requirements
| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
|---|---|---|---|---|---|
| Training / Committee | Committee training the nominee belongs to | Yes | Active training in Committee category | "Infection Control Committee" | FR-001, FR-002 |
| Meeting / session | Specific meeting of the committee (if nominees are per meeting) | TBC (Q-03) | Existing schedule of the training | "ICC – Meeting 2026-10" | FR-003 |
| Employee (nominee) | Employee nominated to the committee | Yes | Active employee | EMP-TEST-0001 | FR-003, FR-004 |
| Role | Committee role of the nominee | Yes | One of Chair, Secretary, Both, QA; no default | "Both" | FR-005 to FR-008 |
| Committee Minutes | Uploaded minutes document for a meeting | Yes, before sign-off | File type/size per NFR-DAT-01 | MINUTES_TEST_0001.pdf | FR-014, FR-015, FR-019 |
| Alert days | Number of days after/before which an alert event fires | Yes (per event) | Whole number ≥ 1 | 3 | FR-016, FR-017 |
| Location | Venue of the committee meeting | Existing (TBC) | Existing source | "Conference Room A" | FR-018 |
| Planned Meeting Date | Scheduled meeting date | Existing (TBC) | Date | 15-OCT-2026 | FR-018 |
| Actual Meeting Date | Date the meeting took place | Existing (TBC) | Date, not in the future | 16-OCT-2026 | FR-018 |

## 7.3 User roles and access matrix
Roles are proposed and to be confirmed (Q-01, Q-04). C = Create, R = Read, U = Update, D = Delete, A = Approve/Sign-off.

| Function / screen | QPSD user (nominee admin) | Chair | Secretary | QA nominee | Training admin | Management / report user |
|---|---|---|---|---|---|---|
| Training Nominee Form | C R U D | - | - | - | R | - |
| Chair queue | R | R U | - | - | - | - |
| Secretary queue | R | - | R U | - | - | - |
| Upload Committee Minutes | TBC | TBC | C R U (proposed) | - | - | - |
| Committee Sign-off | - | A (proposed, Q-10) | - | - | - | - |
| Alert day settings | C R U | - | - | - | R | - |
| Committee Summary/Detail Report | R | R | R | R | R | R |
| Open minutes from report | R | R | R | R | - | R |

## 7.4 Reports and notifications
| Report / notification | Audience | Trigger / frequency | Content | Related FR |
|---|---|---|---|---|
| Committee Summary/Detail Report (enhanced) | QPSD, management, committee members | On demand | Committee name, location, Chair, Secretary, planned date, actual date, minutes link (if feasible) | FR-018, FR-019 |
| Day-based alert(s) | TBC (Q-11). Proposed: Chair/Secretary/QPSD | Daily scheduled run; fires at the defined number of days | Committee, meeting date, pending action, link to queue | FR-016 |

## 7.5 Interfaces
| System | Direction (in/out) | Data exchanged | Frequency | Related FR |
|---|---|---|---|---|
| Email / notification service (TBC, Q-11) | Out | Alert messages | Daily | FR-016 |
| HR employee master (within HRD, TBC) | In | Active employees for nominee selection | Real-time lookup | FR-003 |

# 8. Impact analysis
> Schema context used: **none. Impact analysis is PROVISIONAL.** No HRD schema snapshot is indexed in `skmch-hrd-system-context`, and `SKMCH_SCHEMA_DIR` is not set. Every object below is described by its business function. Actual object names must be verified against the database by the Solution Architect.

## 8.1 Business impact
| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
|---|---|---|---|---|
| IMP-01 | QPSD committee administration | New form for nominations; a role must be chosen for every nominee | FR-001 to FR-009 | N |
| IMP-02 | Committee Chairs and Secretaries | Separate queue entries per role; sign-off depends on minutes upload | FR-010 to FR-015 | N |
| IMP-03 | Committee governance / accreditation evidence | Every signed-off meeting has minutes; better audit evidence | FR-015, NFR-CMP-01 | N (indirect quality/safety governance) |
| IMP-04 | User training / SOP | Users need a short briefing on the new form, Role LOV, sign-off rule and alerts; QPSD SOP may need an update | All | N |
| IMP-05 | Management reporting | Enhanced Committee Summary/Detail Report | FR-018, FR-019 | N |

## 8.2 System impact
| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|
| IMP-06 | Training Nominee Form (APEX page) | New | New page; static IDs per standards, e.g. `REG_TRAINING_NOMINEE`, `BTN_SAVE`, `LOV_COMMITTEE_TRAINING`, `LOV_NOMINEE_ROLE` | FR-001 to FR-008 | MoM M-03 | NEW (proposed) |
| IMP-07 | Existing nominee entry screen (Chair/Secretary checkboxes) | Modify / Retire | Replace checkboxes with Role LOV, or retire the screen for committee trainings (Q-07) | FR-005 to FR-008 | MoM M-05 | PROVISIONAL – not verified |
| IMP-08 | Queue generation logic (package/procedure/trigger) | Modify | Generate per-role queue entries; two entries for Both; no duplicates; QA handling | FR-010 to FR-012 | MoM M-10 | PROVISIONAL – not verified |
| IMP-09 | Queue screen | Modify | Show minutes status; block Committee Sign-off without minutes; label role per queue entry | FR-011, FR-014, FR-015 | MoM M-12, M-13 | PROVISIONAL – not verified |
| IMP-10 | Committee Minutes upload facility | Read-only / Modify (TBC) | Use existing upload if present; otherwise new upload | FR-014, FR-015 | MoM M-12 (implies upload exists) | PROVISIONAL – not verified |
| IMP-11 | Alert scheduled job (DBMS_SCHEDULER) and alert package | New / Modify | Daily job evaluating alert events against defined days; send and log alerts | FR-016 | MoM M-14 | NEW (proposed) |
| IMP-12 | Alert day settings page (APEX) | New | Admin page to maintain days per alert event | FR-017 | Inferred | NEW (proposed) |
| IMP-13 | Committee Summary/Detail Report | Modify | Add committee name, location, Chair, Secretary, planned/actual dates, minutes link | FR-018, FR-019 | MoM M-15 to M-21 | PROVISIONAL – not verified |
| IMP-14 | APEX authorization schemes | Modify / New | Access to new form, alert settings, minutes | NFR-SEC-01, NFR-SEC-02 | Inferred | PROVISIONAL – not verified |
| IMP-15 | Attendance and post-process | Read-only | No change; regression test only | FR-013 | MoM M-11 | PROVISIONAL – not verified |

## 8.3 Database impact
| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|
| IMP-16 | Training nominee table: Chair and Secretary flag columns | Modify | Add a Role column (values CHAIR, SECRETARY, BOTH, QA; NOT NULL after migration; check constraint) and retire the two flag columns after dependants are updated | Queue logic, reports, nominee screens (TBC) | Yes: map flags to role (FR-009); exceptions list for rows with no flag | FR-005 to FR-009 | MoM M-05 | PROVISIONAL – not verified |
| IMP-17 | Training master: status | Read-only | Filter active trainings | Training LOV | No | FR-002 | MoM M-04 | PROVISIONAL – not verified |
| IMP-18 | Training category: Committee flag | Read-only | Filter Committee categories | Training LOV | No | FR-002 | MoM M-04 ("marked as Committee") | Likely |
| IMP-19 | Queue table | Modify | Store the role of each queue entry (Chair/Secretary) so that Both creates two distinguishable entries; unique key per nominee + meeting + role | Queue screen, sign-off, alerts | Possibly: backfill role on open queue entries | FR-010 to FR-012 | MoM M-10 | PROVISIONAL – not verified |
| IMP-20 | Committee minutes attachment storage | Read-only / New (TBC) | Store minutes per meeting (BLOB, file name, MIME type, uploaded by/on) | Queue screen, report | No | FR-014, FR-015, FR-019 | MoM M-12 | PROVISIONAL – not verified |
| IMP-21 | `HRD_TRAINING_ALERT_CONFIG_MST` | New | Alert event, number of days, recipients rule, active flag, audit columns | Alert job | Seed agreed values | FR-016, FR-017 | Inferred | NEW (proposed) |
| IMP-22 | `HRD_TRAINING_ALERT_LOG` | New | Log of alerts sent (event, meeting, recipient, sent on) to stop duplicates | Alert job | No | FR-016, NFR-AUD-03 | Inferred | NEW (proposed) |
| IMP-23 | Nominee role history (`HRD_TRAINING_NOMINEE_HIS` or existing audit mechanism) | New / Modify | Record role changes | Nominee screens | No | NFR-AUD-01 | Inferred | NEW (proposed) |

## 8.4 Risks
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Existing nominees with no role break saves or queues after the Role column becomes mandatory | High | Medium | Run the FR-009 conversion with an exceptions list before go-live; QPSD resolves exceptions |
| Duplicate queue entries for role Both on re-save or regeneration | Medium | Medium | Unique key per nominee + meeting + role; negative tests (FR-011 AC3) |
| Other code still reads the old Chair/Secretary flags | Medium | High | Dependency search on flag columns during design; keep flags in sync until all dependants are migrated |
| Alerts sent to the wrong people or repeated daily | Medium | Medium | Confirm Q-11; alert log for de-duplication; UAT with test mailbox |
| Sign-off blocked for meetings already held before go-live without minutes | Medium | Low | Agree cut-over rule (Q-09); communicate before go-live |
| Large minutes files slow the report or queue | Low | Low | File size limit (NFR-DAT-01); report shows link only, not content |

# 9. Assumptions, constraints and dependencies

## 9.1 Assumptions
| ID | Assumption | Needs confirmation from |
|---|---|---|
| A-01 | A training category already has an attribute that marks it as Committee. | Training admin / SA |
| A-02 | Trainings already have an Active/Inactive status. | Training admin / SA |
| A-03 | Queues for Chair and Secretary already exist and are generated from the nominee roles. | SA |
| A-04 | A facility to upload Committee Minutes already exists, or will be added on the Queue screen. | QPSD / SA |
| A-05 | Location, Planned Meeting Date and Actual Meeting Date are already captured for committee meetings. | QPSD / SA |
| A-06 | Committee Sign-off is performed by the Chair. | QPSD |
| A-07 | The new form is used for committee trainings only. Non-committee nominations stay on the existing screen. | QPSD |
| A-08 | Priorities for inferred FRs (FR-004, FR-012, FR-017) default to Should. | QPSD / SA |

## 9.2 Constraints
- The Training Nominee Form shall be built in Oracle APEX (M-03).
- The existing attendance and post-process workflow shall not be changed (M-11).
- New and changed HRD objects shall follow the SKMCH Oracle/APEX naming standards.

## 9.3 Dependencies
- Confirmation of the existing object names (nominee, queue, minutes, report) by the Solution Architect.
- Availability of an email/notification channel for alerts (Q-11).
- QPSD decision on the conversion of existing nominee records (Q-06).

# 10. Open questions
| ID | Question | Raised because (M-NN / FR) | Addressed to | Blocking? |
|---|---|---|---|---|
| Q-01 | Please confirm the expansion of "QPSD", the business owner, the meeting date and attendees, and the CR number for this change. | M-01 | QPSD / BA | No |
| Q-02 | What exactly are the "minimum required fields" on the Training Nominee Form? Proposed: Training/Committee, Meeting/Session, Employee, Role. | M-03, FR-003 | QPSD | Yes |
| Q-03 | Are nominees assigned once per committee (training) or per meeting/session? Where are Location and Planned Meeting Date held? | M-03, FR-003, FR-018 | QPSD / SA | Yes |
| Q-04 | What does the QA role do? Does a QA nominee get a queue, take part in attendance, or have any sign-off or review step? | M-06, FR-010 | QPSD | Yes |
| Q-05 | Can a committee have more than one Chair, Secretary or QA? If one nominee has role Both, may anyone else be Chair or Secretary? | M-06, M-10, FR-004 | QPSD | Yes |
| Q-06 | How should existing nominee records be converted (no box ticked / both ticked)? Should historic, closed records also be converted? | M-05, FR-009 | QPSD / SA | Yes |
| Q-07 | Which existing screen has the Chair/Secretary checkboxes, and will it be retired, kept for non-committee trainings, or changed to use the Role LOV as well? | M-05, FR-005 | QPSD / SA | Yes |
| Q-08 | What actions are taken in the Chair queue and in the Secretary queue, and when are queue entries generated (on nominee save, on meeting creation, after attendance)? | M-10, FR-010 | QPSD / SA | Yes |
| Q-09 | Who uploads Committee Minutes, which file types and maximum size are allowed, can minutes be replaced after sign-off, and how should meetings held before go-live be handled? | M-12, FR-015 | QPSD | Yes |
| Q-10 | Which role performs Committee Sign-off: Chair only, or Chair and Secretary? With role Both, which queue entry carries the sign-off? | M-13, FR-015 | QPSD | Yes |
| Q-11 | For alerts: which events (e.g. upcoming meeting, minutes not uploaded, sign-off pending), how many days for each, counted from which date, to whom, by what channel (email/SMS/in-app), and should they repeat? | M-14, FR-016 | QPSD | Yes |
| Q-12 | Which existing report is the "Committee Summary/Detail Report"? Should summary and detail be one report or two? Where does Actual Meeting Date come from? Is the minutes attachment wanted as a download link? | M-15 to M-21, FR-018, FR-019 | QPSD / SA | No |
| Q-13 | What counts as an "active" training: status flag only, or also an end date not yet passed? | M-04, FR-002 | Training admin | No |
| Q-14 | Should nominees be addable or removable after the meeting has been held or signed off? | FR-012 | QPSD | No |
| Q-15 | Can a nominee's role be changed after queue entries have been actioned? | FR-012 | QPSD | No |
| Q-16 | Should a nominee with role Both appear once in attendance? Should QA nominees appear in attendance? | M-11, FR-013 | QPSD | No |

# Appendix A. Minutes of meeting breakdown
| M-ID | Original statement | Type | Mapped to |
|---|---|---|---|
| M-01 | Subject: Committee Workflow Enhancements (for QPSD) | Information | §1, Q-01 |
| M-02 | Module: Training Management Module | Information | §1 |
| M-03 | A new Training Nominee Form with minimum required fields will be developed in APEX. | Requirement | BR-01, FR-001, FR-003, Q-02, Q-03 |
| M-04 | Only active trainings whose category is marked as Committee will be available for selection. | Requirement | BR-01, FR-002, RULE-01, Q-13 |
| M-05 | The existing Chair/Secretary checkboxes will be replaced with a List of Values (LOV). | Decision | BR-02, FR-005, FR-009, Q-06, Q-07 |
| M-06 | The LOV will contain the following options: Chair, Secretary, Both, and QA. | Requirement | BR-02, FR-006, RULE-02, Q-04 |
| M-07 | By default, no role will be selected. | Requirement | BR-02, FR-007, RULE-02 |
| M-08 | Role assignment will be mandatory for every nominee. | Requirement | BR-02, FR-008, RULE-02 |
| M-09 | The system will not allow the record to be saved without assigning a role. | Requirement | BR-02, FR-008, RULE-02 |
| M-10 | If Both is selected, separate queues will be generated and managed for the nominee as Chair and Secretary. | Requirement | BR-03, FR-010, FR-011, FR-012, RULE-03, Q-08 |
| M-11 | The existing attendance and post-process workflow will remain unchanged. | Constraint | FR-013, Out of scope, §9.2 |
| M-12 | On the Queue screen, the system will check whether the Committee Minutes have been uploaded. | Requirement | BR-04, FR-014, RULE-05, Q-09 |
| M-13 | Committee Sign-off will not be allowed until the Committee Minutes are uploaded. | Requirement | BR-04, FR-015, RULE-05, Q-10 |
| M-14 | System-generated alerts will be sent according to the defined number of days. | Requirement | BR-05, FR-016, FR-017, RULE-06, Q-11 |
| M-15 | Enhance the Committee Summary/Detail Report to include: Training/Committee Name | Requirement | BR-06, FR-018 |
| M-16 | … Location | Requirement | BR-06, FR-018 |
| M-17 | … Chair Name | Requirement | BR-06, FR-018 |
| M-18 | … Secretary Name | Requirement | BR-06, FR-018 |
| M-19 | … Planned Meeting Date | Requirement | BR-06, FR-018 |
| M-20 | … Actual Meeting Date | Requirement | BR-06, FR-018 |
| M-21 | … Meeting Minutes attachment (if feasible) | Requirement | BR-06, FR-019, Q-12 |
| M-22 | Action: Development to be carried out as per the above agreed requirements. | Action item | §1.1 (this SRS → SA review → design) |

# Appendix B. Requirement traceability
| Requirement | Source (M-NN) | Impact items (IMP-NN) |
|---|---|---|
| FR-001 | M-03 | IMP-01, IMP-06, IMP-14 |
| FR-002 | M-04 | IMP-06, IMP-17, IMP-18 |
| FR-003 | M-03 | IMP-06 |
| FR-004 | Inferred | IMP-06, IMP-16 |
| FR-005 | M-05 | IMP-06, IMP-07, IMP-16 |
| FR-006 | M-06 | IMP-06, IMP-07, IMP-16 |
| FR-007 | M-07 | IMP-06, IMP-07 |
| FR-008 | M-08, M-09 | IMP-06, IMP-07, IMP-16 |
| FR-009 | Inferred (M-05, M-08) | IMP-16 |
| FR-010 | M-10 | IMP-02, IMP-08, IMP-19 |
| FR-011 | M-10 | IMP-02, IMP-08, IMP-09, IMP-19 |
| FR-012 | Inferred (M-10) | IMP-08, IMP-19 |
| FR-013 | M-11 | IMP-15 |
| FR-014 | M-12 | IMP-09, IMP-10, IMP-20 |
| FR-015 | M-13 | IMP-03, IMP-09, IMP-10, IMP-20 |
| FR-016 | M-14 | IMP-11, IMP-21, IMP-22 |
| FR-017 | Inferred (M-14) | IMP-12, IMP-21 |
| FR-018 | M-15 to M-20 | IMP-05, IMP-13 |
| FR-019 | M-21 | IMP-13, IMP-20 |
| NFR-SEC-01, NFR-SEC-02 | Inferred | IMP-14 |
| NFR-AUD-01 | Inferred | IMP-23 |
| NFR-AUD-03 | Inferred | IMP-22 |
