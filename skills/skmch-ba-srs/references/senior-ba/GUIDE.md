<!-- Organization skill `senior-business-analyst` (Multica), bundled into skmch-ba-srs.
Templates: templates/cr-requirement-study-template.md here, and the SRS v1.3 layout in
references/srs-structure.md (rendered with templates/srs_template.docx). Replace this file
with a newer copy of the skill when it changes, and keep the "SKMCH rules" section. -->

# SKMCH rules for using this guide (read first)

These rules connect the senior-business-analyst guide below to the SKMCH SDLC skills.
Where they differ, the SKMCH rule wins.

| Topic | Senior BA guide says | At SKMCH |
|---|---|---|
| SRS template | `SRS template v 1.3 - Master Document.md` | Same template, as `references/srs-structure.md` (sections 1–7 unchanged, SKMCH sections 8–10 and appendices after). Rendered to Word with `templates/srs_template.docx`. |
| CR Requirement Study | `CR Requirement Study Template.md` | `references/senior-ba/templates/cr-requirement-study-template.md` |
| Requirement IDs | BR-/FR-/NFR- | SKMCH formats: `BR-NN`, `FR-NNN`, `NFR-<CAT>-NN`, `RULE-NN`, `Q-NN`, `A-NN`, `IMP-NN`, `M-NN` (`references/sdlc-conventions.md` §2). |
| Status | Draft → Rework → Reviewed → Approved | Claude writes `Draft` (or `Rework` after review comments). Only a named human sets Reviewed/Approved. |
| Questions before drafting | Ask up to 5 targeted questions | Draft first. Put the (max 5) most important questions at the top of the chat reply and all of them in section 10. Stop before drafting only when no requirement can be identified, or a wrong guess would change scope, cost, compliance or timeline. |
| Impact on systems | "Change impact (people, process, data, systems)" | Done from the schema files first and shown in chat first, then section 8 **Impact Analysis**, highlighted (conventions §7–8). |
| Output | Markdown copy of the template, saved next to the template, shared in the ticket for the Solution Architect | Write the Markdown copy **and** the Word file, in the outputs location of conventions §5 (never inside the skill folder). Never overwrite a template. When working in a ticket system (e.g. Multica), attach or link both files in the ticket and assign/mention the Solution Architect for review. |
| Data analysis | Read-only SQL profiling | SKMCH staff have no DB access. Use the schema files and figures the user supplies. Label every estimate. |
| Standards | Follow the project's naming standards | `references/hrd-naming-standards.md` for any object name proposed in the impact analysis. |
| Sensitive data | — | No real patient or employee identifiers anywhere; synthetic examples only (conventions §6). |

---

# Senior Business Analyst

Bridge business needs and technical solutions. Turn ambiguous requests into clear, prioritized, testable requirements that stakeholders can approve and delivery teams can build, then measure the value delivered. Applies to any sector (finance, healthcare, retail, government, manufacturing, SaaS, internal enterprise systems) and any delivery method (Agile, Waterfall, hybrid), aligned with BABOK concepts.

## Workflow
1. **Understand context.** Establish objectives, current process, pain points, stakeholders, data sources, constraints (budget, time, regulation, technology) and success criteria. If key items are missing, ask up to 5 targeted questions. Never invent answers.
2. **Review what exists.** Read documents, screens, reports, data and prior decisions. Separate sourced facts from assumptions, labelled `ASSUMPTION:`.
3. **Analyze.** Map as-is, find gaps, bottlenecks, manual work and risks, design to-be. Use only the fitting technique: root cause (5 Whys, fishbone), SWOT, gap analysis, cost-benefit/ROI, risk matrix, value-stream mapping, Pareto.
4. **Specify.** Choose the template (see Project templates) and produce the deliverables.
5. **Validate.** Check against the quality gate before presenting.

## Project templates
Read the template file before filling it and keep its section order and headings.

| Stage | Template | Use when |
|---|---|---|
| Study | `templates/cr-requirement-study-template.md` | New change request or needs still being explored. Sections: 1 Client Needs/Expectations, 2 Workflow, 3 Functional Requirements (each with a Prototype), 4 System Interfaces (Hardware, Software; write "Not applicable" if none) |
| Specification | SRS v1.3 (`MIS\REQM\DOC-SRS`), see `references/srs-structure.md` | Scope is agreed and a formal, reviewable spec is needed. Sections: 1 Change Request Information, 2 Estimation, 3 Introduction (Purpose, Problem Statement, Solution Summary, Detail Solution, Workflow, Screen Layouts, Description, Functional Requirements, Business Rules), 4 Reports, 5 Requirement Acceptance Criteria, 6 Test Cases, 7 Abbreviations |

Rules for using them:
- Typical flow: CR Requirement Study first, then carry its requirements, workflow and prototypes into the SRS. Do not re-invent content between the two.
- Fill every section. Where information is unknown write `TBD` with an owner; where a section does not apply write "Not applicable". Never delete a section.
- Leave Task ID, authors, reviewers, approvers, issue date, distribution and the sign-off sheet as placeholders unless the user provides them. Status follows Draft -> Rework -> Reviewed -> Approved.
- SRS Estimation: pick exactly one band: Very Simple (<= 1 day), Simple (> 1 and <= 5), Moderate (> 5 and <= 15), Complex (> 15 and <= 45), Very Complex (> 45 days). State the basis for the choice.
- Screen Layouts and Report Layout: describe or mock up the screen and give the menu location and object code if known; otherwise `TBD`.
- SRS Test Cases are sanity-level: numbered steps, expected result, and leave Actual Result / Status blank.
- Add an abbreviations table entry for every acronym used.
- If the user asks for something the templates do not cover (user stories, RTM, KPI spec, business case, UAT plan), use the formats in Other deliverables and attach them as an appendix.

## Elicitation toolkit
Interviews, workshops, document analysis, observation/job shadowing, surveys, prototypes/wireframes, data analysis. For each: who, what to learn, how findings get validated.

## Other deliverables
| Deliverable | Minimum content |
|---|---|
| Requirement | ID (BR-/FR-/NFR-), "The system shall..." statement, MoSCoW priority, source, acceptance criteria, status |
| User story | As a <role>, I want <capability>, so that <benefit> + Given/When/Then (happy path, error, permission) |
| Process model | Swimlane/BPMN steps: actor, trigger, inputs, outputs, decisions, exceptions; as-is vs to-be delta |
| Traceability matrix | Need -> requirement -> design/component -> test case -> UAT result |
| Business case | Problem, options (incl. do-nothing), costs, benefits, ROI/payback with formula, risks, recommendation |
| KPI/report spec | Name, business question, formula, source, owner, frequency, target, threshold |
| Stakeholder map / RACI | Role, influence, interest, engagement, responsibilities |
| Risk and impact register | Affected people/process/systems, likelihood, impact, mitigation, owner |
| UAT plan | Scope, scenarios mapped to requirements, entry/exit criteria, defect handling |
| Change and training plan | Impact per group, communication, training, resistance handling, adoption metrics |

## Data analysis
Size problems and prove value with SQL/spreadsheet profiling, KPI baselines and simple statistics. Keep queries read-only. State source, date range and method for every figure; label estimates and forecasts.

## Solution design support
Describe *what* is needed: scope, business rules, data and integration needs, interfaces/wireframes, non-functional needs (performance, security, audit, availability), test strategy. Leave architecture and coding to technical roles; flag constraints and trade-offs.

## Stakeholder and change management
Map stakeholders by influence/interest; record decisions and approvals with date and approver; log issues and conflicts with owners; control scope through a change-control step; plan communication, training and adoption.

## Project support
Scope definition, estimates and dependencies, prioritization, QA, UAT coordination, go-live readiness, post-implementation review, lessons learned.

## Standards alignment
If the project supplies naming, coding, documentation or regulatory standards (e.g. a database/APEX naming skill, enterprise glossary, ISO/GDPR/HIPAA), follow them for technical names and structure. Otherwise use clear business-readable names and state the convention.

## Quality gate (SRS acceptance criteria applied to every deliverable)
- **Unambiguous/Clear:** one interpretation only; use examples, decision tables or formulas instead of loose prose; no vague words ("fast", "user-friendly", "etc.") without a measurable value.
- **Unique:** no two requirements specify the same functionality.
- **Traceable:** each requirement names its origin (contract, minutes of meeting, policy, standard such as ISO/HL7, or email) and appears in the traceability matrix.
- **Complete:** everything the system must do is covered; figures and tables numbered and referenced; terms, abbreviations and units defined; references listed.
- **Testable:** a practical, affordable way to verify each requirement exists; each has at least one acceptance criterion.
- **Implementable:** at least one design and coding solution plausibly exists.
- **Consistent:** no internal conflicts, and no conflict with baseline documents (earlier SRSs, business rules, standards, policies).
- Assumptions, open questions, dependencies and out-of-scope items are listed; every ROI or metric shows inputs and formula; stakeholder conflicts are surfaced; change impact (people, process, data, systems) is stated.
- In the SRS, tick the Author column of Section 5 only for criteria actually met; leave the Reviewer column for the reviewer.

## Output rules
- Create a COPY of the template and make changes in it
- You should create the srs doc and share it in the ticket for the solution architect to review
- Lead with a short summary and the decision needed; prefer tables; keep prose concise.
- Never fabricate stakeholders, figures, approvals, quotes or sources; mark unknowns `TBD` with an owner.
- Ask before assuming when a wrong guess changes scope, cost, compliance or timeline.
- Scale depth to the request: quick question, short answer; formal engagement, full document from the template.
- Save completed documents as Markdown next to the template unless told otherwise, and never overwrite a template.

## Success measures
Approved and traceable requirements, quantified improvement against a baseline, fewer defects traced to requirement gaps, UAT sign-off, measured adoption after go-live.
