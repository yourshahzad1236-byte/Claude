# SRS structure (Markdown that render_docx.py turns into Word)

Use these headings and numbering exactly. Omit a subsection only when it is truly not
applicable, and in that case write "Not applicable: <reason>" rather than deleting it.
The cover page, version history and approvals table come from the Word template. Do not
repeat them in the Markdown.

```markdown
# 1. Introduction
## 1.1 Purpose
<!-- One paragraph: what this SRS specifies and for whom. -->
## 1.2 Background
<!-- Why the change is needed: the problem or opportunity, from the MoM. -->
## 1.3 Scope
### In scope
### Out of scope
<!-- Bullets. Items explicitly excluded or deferred in the meeting, with M-NN refs. -->
## 1.4 Stakeholders
| Name / Role | Department | Interest / responsibility | Attended meeting |
## 1.5 Definitions and abbreviations
| Term | Meaning |
## 1.6 References
<!-- MoM date(s), earlier SRS versions, related CRs, policies/SOPs. -->

# 2. Current state (As-Is)
<!-- How the process works today; which screens/reports are used; pain points. -->

# 3. Proposed solution overview (To-Be)
<!-- Business-level description of the new process. A numbered step flow is fine. No technical design. -->

# 4. Business requirements
| ID | Business requirement | Source (M-NN) | Priority |

# 5. Functional requirements
## 5.x <Functional area name>
### FR-NNN <short title>
**Description:** The system shall …
**Priority:** Must / Should / Could / Won't (this release)
**Source:** M-NN, M-NN
**Business rules:** RULE-NN (if any)
**Acceptance criteria:**
- AC1: Given … When … Then …
- AC2 (negative): Given … When … Then …
**Notes / open questions:** Q-NN (if any)

# 6. Non-functional requirements
| ID | Category | Requirement | Measure / target | Source | Status |
<!-- Status: "Discussed" (from MoM) or "Proposed (not discussed in meeting)". -->

# 7. Business rules, data and access
## 7.1 Business rules
| ID | Rule | Applies to (FR) | Source |
## 7.2 Data requirements
| Data item | Business meaning | Mandatory | Validation / format | Example (synthetic) | Related FR |
## 7.3 User roles and access matrix
| Function / screen | Role A | Role B | … |
<!-- Cells: C R U D A (Approve) or - -->
## 7.4 Reports and notifications
| Report / notification | Audience | Trigger / frequency | Content | Related FR |
## 7.5 Interfaces
| System | Direction (in/out) | Data exchanged | Frequency | Related FR |

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
| Requirement | Source (M-NN) | Impact items (IMP-NN) |
```
