# SRS structure: SKMCH template `MIS\REQM\DOC-SRS` Version 1.3

The SRS follows the official SKMCH template **MIS\REQM\DOC-SRS v1.3**. Sections 1–7 keep
the template's order and headings exactly. Sections 8–10 and the appendices are the
SKMCH SDLC additions that the review, design and QA skills rely on (impact analysis, IDs,
traceability). They come **after** section 7, so the template itself is never changed.

Rules:
- Never delete a section. Unknown → `TBD (owner: <role/name>)`. Not relevant → `Not applicable: <reason>`.
- The cover page (Document Information, Document Revision History, Document Approval /
  Sign Off Sheet) comes from the Word template `templates/srs_template.docx`. Don't
  repeat it in the Markdown.
- Template status values: `Draft` → `Rework` → `Reviewed` → `Approved`. Claude writes
  `Draft` (or `Rework` when revising after review comments). Only a named human sets
  `Reviewed` or `Approved`.
- Leave Task ID, reviewers, approvers, issue date and distribution as placeholders unless
  the user gives them. Use the CR ID as the Task ID only if the user confirms it is the
  same number.

```markdown
# 1. Change Request Information
| Category | Information |
|---|---|
| Task ID | <<Task ID from the ticket system, or TBD>> |
| CR ID | <CR-ID> |
| Author | <BA name, or "Claude (AI draft) for <BA name>"> |
| Status | Draft |
| Initial Reviewer(s) | <<Peer reviewer(s) within team>> |
| Final Reviewer(s) | <<Review from stakeholders>> |
| Approver(s) | <<Approval from Team Lead / Project Manager>> |
| Issue Date | <<Date of issue for further development>> |
| Distribution | <<List of all stakeholders to whom document is distributed>> |

# 2. Requirement Specification Estimation
| Select | Complexity | Effort |
|---|---|---|
| [ ] | Very Simple | <= 1 day |
| [ ] | Simple | > 1 day and <= 5 days |
| [ ] | Moderate | > 5 days and <= 15 days |
| [ ] | Complex | > 15 days and <= 45 days |
| [ ] | Very Complex | > 45 days |
**Basis for estimate:** <!-- Mark exactly one row [x]. Give the basis: number of FRs, screens, reports, new/changed tables and packages from the impact analysis, integrations, data migration. -->

# 3. Introduction
## 3.1 Purpose
<!-- The product/module and release this SRS covers, and the scope: which part of the system. -->
## 3.2 Problem Statement
<!-- The problem or opportunity, from the MoM / CR Requirement Study (cite M-NN). -->
## 3.3 Solution Summary
<!-- 3–6 sentences, business level. -->
## 3.4 Detail Solution
### 3.4.1 Scope
**In scope:** …
**Out of scope:** … <!-- items explicitly excluded or deferred, with M-NN refs -->
### 3.4.2 Stakeholders
| Name / Role | Department | Interest / responsibility | Attended meeting |
### 3.4.3 User roles and access matrix
| Function / screen | Role A | Role B | … |
<!-- Cells: C R U D A (Approve) or - -->
### 3.4.4 Data requirements
| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
### 3.4.5 System interfaces
**Hardware interfaces:** … or "Not applicable"
**Software interfaces:** | System / module | Direction (in/out) | Data exchanged | Frequency | Related FR |
## 3.5 Workflow
### 3.5.1 Current (As-Is)
<!-- How it works today, screens/reports used, pain points. -->
### 3.5.2 Proposed (To-Be)
<!-- Numbered steps or swimlane table: Step | Actor | Action | Screen | Decision / exception. -->
## 3.6 Screen Layouts
<!-- Per screen: name, menu location, object code (from the schema/APEX files, or TBD), and a field-level mock-up table:
| Field / button | Type | Mandatory | Default / LOV | Validation | Related FR | -->
## 3.7 Description
<!-- Narrative description of the requirement, with concrete examples (e.g. ranges, formats, counts). -->
## 3.8 Functional Requirements
### 3.8.1 Business requirements
| ID | Business requirement | Source (M-NN) | Priority |
### 3.8.2 Functional requirements
#### FR-NNN <short title>
**Description:** The system shall …
**Priority:** Must / Should / Could / Won't (this release)
**Source:** M-NN, M-NN
**Business rules:** RULE-NN (if any)
**Acceptance criteria:**
- AC1: Given … When … Then …
- AC2 (negative): Given … When … Then …
**Notes / open questions:** Q-NN (if any)
### 3.8.3 Non-functional requirements
| ID | Category | Requirement | Measure / target | Source | Status |
<!-- Status: "Discussed" (from MoM) or "Proposed (not discussed in meeting)". -->
## 3.9 Business Rules
| ID | Rule | Applies to (FR) | Source |

# 4. Reports
<!-- Purpose, functionality and expected data of the reports. One 4.x block per report if several; "Not applicable" if none. -->
## 4.1 Purpose
## 4.2 Report Layout
<!-- Menu location, object code (or TBD), and a column layout table: | Column | Source / formula | Sort / group | -->
## 4.3 Input Parameters
| Parameter | Type | Mandatory | Default / LOV | Validation |
**Report users and roles:** …
<!-- Notifications (email/SMS/alerts) also go here: | Notification | Audience | Trigger | Content | Related FR | -->

# 5. Requirement Acceptance Criteria
| Criteria | Author | Reviewer | Details |
|---|---|---|---|
| Unambiguous / Clear | [ ] | [ ] | |
| Unique | [ ] | [ ] | |
| Traceable | [ ] | [ ] | |
| Complete | [ ] | [ ] | |
| Testable | [ ] | [ ] | |
| Implementable | [ ] | [ ] | |
| Consistent | [ ] | [ ] | |
<!-- Tick the Author column [x] ONLY for criteria actually met, with the evidence in Details (e.g. "Traceable: every FR cites M-NN, see Appendix B"). Never tick the Reviewer column. Keep the template's criteria definitions out of the body; they are in the reviewer's checklist. -->

# 6. Test Cases
| Sr. No | Test Case Description | Expected Results | Actual Results | Status |
|---|---|---|---|---|
| 1 | <numbered steps> (FR-NNN AC1) | <expected result> | | |
<!-- Sanity level: at least one per Must FR (happy path) and one negative case per Must FR. Leave Actual Results and Status blank. Full test design is done by QA (skmch-qa-testcases). -->

# 7. Abbreviations & Acronyms
| Abbreviation | Full form |
<!-- Every acronym used anywhere in the document. -->

<!-- highlight -->
# 8. Impact Analysis
> Schema context used: <source, schemas covered and snapshot date / "none: impact analysis is PROVISIONAL">
## 8.0 Impact summary
| Measure | Count |
|---|---|
| Existing tables / columns affected | n |
| Existing packages / views / triggers / APEX pages affected | n |
| New objects proposed | n |
| Schemas touched | HRD, … |
| High-risk items | n |
| Names from the MoM not found in schema | n |
## 8.1 Business impact
| ID | Area / department / process | Impact | Related FR | Patient-safety relevant (Y/N) |
## 8.2 System impact
| ID | Application / page / package / report / job / interface | Change type | Description | Related FR | Evidence | Confidence |
## 8.3 Database impact
| ID | Table / column / object | Change type | Description | Dependent objects | Data migration | Related FR | Evidence | Confidence |
## 8.4 Risks
| Risk | Likelihood | Impact | Mitigation |
## 8.5 Not found in schema
| Name used in MoM | Searched where | Result | Action (Q-NN / NEW) |
<!-- /highlight -->

# 9. Assumptions, constraints and dependencies
## 9.1 Assumptions
| ID | Assumption | Needs confirmation from |
## 9.2 Constraints
## 9.3 Dependencies

# 10. Open questions
| ID | Question | Raised because (M-NN / FR) | Addressed to | Blocking? |

# Appendix A. Minutes of meeting breakdown
| M-ID | Original statement | Type | Mapped to |
<!-- Every M-NN appears. Mapped to: BR/FR/NFR/RULE IDs, "Out of scope", or Q-NN. -->

# Appendix B. Requirement traceability
| Requirement | Source (M-NN) | Impact items (IMP-NN) | Test cases (section 6) |

# Appendix C. Additional deliverables
<!-- Only when asked: user stories, process model, business case, KPI/report spec, stakeholder map/RACI, risk register, UAT plan, change and training plan. Formats are in references/senior-ba/GUIDE.md "Other deliverables". Otherwise: "Not applicable". -->
```
