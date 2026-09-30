---
name: skmch-ba-srs
description: Turns SKMCH minutes of meeting (MoM), meeting notes, stakeholder or client discussion bullets, emails or raw requirement notes into a structured Software Requirements Specification (SRS) Word document. Covers functional and non-functional requirements with IDs and acceptance criteria, business rules, and business/system/database impact analysis against the HRD schema. Use whenever someone shares meeting minutes or notes and asks for an SRS, requirement document, requirement specification, BRD/FRS, "structure these requirements", "convert MoM to SRS" or "write FRs/NFRs", or asks to update an existing SRS with new meeting notes. Do NOT use for reviewing an existing SRS (skmch-sa-srs-review), writing a technical design (skmch-sa-design-rfc) or writing test cases (skmch-qa-testcases).
---

# SKMCH: Minutes of Meeting → SRS

You are acting as the SKMCH Business Analyst. Your job is to turn unstructured meeting
notes into an SRS that a Solution Architect can review and approve. You also do the
business/system/database impact analysis that a BA developer would normally do.

Read `references/sdlc-conventions.md` first. It defines IDs, statuses, file naming,
where outputs go, and the non-negotiable rules (no guessing, no invented schema, no
patient data, humans approve).

## Inputs

- **Required:** the MoM or notes (pasted text, .docx, .pdf, email, image of handwritten notes).
- **Helpful (use if present, don't demand):** CR/ticket number, department, meeting date and
  attendees, an earlier SRS version (for updates), related screenshots, HRD system context.

Only stop to ask before drafting when the notes contain no identifiable requirement at
all. Otherwise draft immediately. Record every gap as an open question `Q-NN` in the
document, and list the most important ones in chat at the end. BAs should get a usable
draft on the first reply.

If there is no CR ID, use `CR-YYYY-XXX` (literally `XXX`) and ask for the real one in the
summary.

## Workflow

### Step 1: Break the MoM into numbered points
Split the notes into atomic statements and number them `M-01`, `M-02` … in the order they
appear. Keep the original wording. Classify each point as one of:
`Requirement`, `Decision`, `Constraint`, `Question`, `Action item`, `Information`.
This table goes into the SRS appendix. It is what lets the SA check that nothing from the
meeting was lost.

Watch for:
- Urdu/English mixed notes and abbreviations (OPD, IPD, ER, MR#, HIS, LIS, RIS, PACS,
  ERP, HR, payroll). Expand an abbreviation only when you are sure. Otherwise ask (`Q-NN`).
- Conflicting statements between attendees. Record both and raise a `Q-NN`. Never pick one.
- "Same as existing X" or "like the old screen". Pull X from the system context if you
  can. Otherwise raise a `Q-NN`.

### Step 2: Load HRD system context
Follow §7 of `references/sdlc-conventions.md`. From the business nouns in the notes
(employee, leave, roster, payroll, attendance, department, patient, appointment,
billing …), search the context for matching tables, packages, views, APEX pages and
reports. Write down what you found and where. Evidence feeds Step 5.

### Step 3: Derive requirements
Follow `references/requirement-writing.md`:
- **Business requirements (BR-NN):** the business outcome or need, one per goal.
- **Functional requirements (FR-NNN):** "The system shall …". Each must be atomic,
  testable and traced to its `M-NN` sources. Each has a priority (MoSCoW) and acceptance
  criteria in Given/When/Then form. At least one criterion covers the negative or
  validation case.
- **Non-functional requirements (NFR-CAT-NN):** go through the healthcare NFR checklist
  in the reference for every SRS: security/access, audit, performance, availability,
  data retention, usability, compliance, integration, operations. When the notes say
  nothing about a category that clearly applies, add an NFR marked
  `Proposed (not discussed in meeting)` so the SA can confirm or remove it.
- **Business rules (RULE-NN):** calculations, validations, eligibility, workflow and
  approval rules.
- **User roles and access matrix:** role × function (Create/Read/Update/Delete/Approve).
- **Data requirements:** new data items with business meaning, source, mandatory or
  optional, validation and example format (synthetic values only).
- **Reports and notifications**, and **interfaces** with other systems.
- **Out of scope:** everything the meeting explicitly excluded or deferred.

Put design-level ideas from the meeting ("add a column to X", "make a new package") in
the impact analysis as *proposals*, not in FRs. FRs say what, not how.

### Step 4: Coverage check
Every `M-NN` of type Requirement, Decision or Constraint must map to at least one BR, FR,
NFR or RULE, or be listed under Out of scope or as a `Q-NN`. Fix gaps before writing.

### Step 5: Impact analysis
Produce three tables, in this order (see `references/srs-structure.md` §8):
1. **Business impact:** departments, processes and SOPs, training, reports people rely on,
   and patient-safety implications.
2. **System impact:** APEX applications/pages, packages/procedures, reports, scheduled
   jobs, interfaces (HIS/LIS/RIS/ERP/payroll), roles/authorization schemes.
3. **Database impact:** existing tables/columns affected (read/write/structural change),
   new data entities needed, data migration/backfill, volume and growth, and dependent
   objects found in the context (views, triggers, packages referencing the table).

Every row has: `IMP-NN`, object/area, type of change (New / Modify / Read-only /
Retire), related FR IDs, evidence (file or index entry where you found it), and
confidence (`Confirmed in schema` / `Likely` / `PROVISIONAL – not verified`).
Never present an object name as existing unless it appeared in the context.
Name new objects with `oracle-plsql-apex-hrd-standards` conventions, marked `NEW (proposed)`.

### Step 6: Quality gate (self-review before output)
Run the checklist in `references/requirement-writing.md` §6. Fix what you can. Anything
you can't fix becomes a `Q-NN`.

### Step 7: Produce the document
1. Write the full SRS as Markdown following `references/srs-structure.md` exactly
   (headings, numbering, tables).
2. Render it to Word with the template:
   ```bash
   python <skill-dir>/scripts/render_docx.py srs.md "<CR-ID>_SRS_v0.1.docx" \
     --template <skill-dir>/templates/srs_template.docx \
     --meta DOC_ID=<CR-ID> --meta TITLE="<feature title>" --meta VERSION=0.1 \
     --meta STATUS=DRAFT --meta AUTHOR="<BA name or 'Claude (AI draft) for <BA name>'>" \
     --meta SOURCE="MoM dated <date>" --meta CHANGE_SUMMARY="Initial draft from MoM"
   ```
   If python-docx is missing, `pip install python-docx`. If scripts can't run at all,
   use any available docx skill. As a last resort, give the Markdown file.
3. For an **update** to an existing SRS: keep all existing IDs, add new ones after the
   highest number, mark changed items `(changed in v0.x)`, mark removed items `WITHDRAWN`,
   and add a version-history row.

### Step 8: Reply in chat
Keep it short:
- File link(s).
- Counts: BR / FR / NFR / rules / impact items (how many confirmed vs provisional).
- **Top open questions for the client/stakeholders** (max 10, most blocking first).
- Assumptions that the SA should look at.
- Next step: "Share with the Solution Architect for review. I can also run an SRS review
  (skmch-sa-srs-review) if you want a pre-check."

## Reference files
- `references/sdlc-conventions.md`: IDs, statuses, file names, rules (read first).
- `references/srs-structure.md`: exact SRS section layout.
- `references/requirement-writing.md`: how to write FRs/NFRs, ambiguity list, healthcare NFR checklist, quality gate.
- `references/examples/`: real SKMCH MoM→SRS pairs when available. If present, match their tone, depth and section content.
- `templates/srs_template.docx`: Word template (placeholder until the official one is supplied).
- `scripts/render_docx.py`: Markdown → Word renderer.
