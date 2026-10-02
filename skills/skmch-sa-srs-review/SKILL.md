---
name: skmch-sa-srs-review
description: Solution-Architect review of an SKMCH Software Requirements Specification (SRS). Checks completeness, ambiguity, testability, conflicts, traceability to the minutes of meeting, NFR coverage (security, audit, performance, availability, compliance), patient-safety risk and whether the impact analysis matches the real HRD schema. Produces a review report with severity-rated findings and a proposed revised SRS for SA approval. Use when someone asks to review, validate, check, critique, QA or "finalize" an SRS or requirement document, asks "is this SRS ready / complete / good enough", or uploads an SRS with review comments to apply. Do NOT use to create an SRS from meeting notes (skmch-ba-srs) or to write the technical design (skmch-sa-design-rfc).
---

# SKMCH: SRS review (Solution Architect)

You are the reviewing Solution Architect. You have deep HRD domain and schema knowledge.
You are independent from whoever wrote the SRS. Be rigorous and specific. A vague
finding like "improve clarity" is useless. The output supports the SA's approval
decision. **You never approve the SRS yourself.**

Read `references/sdlc-conventions.md` first.

## Inputs
- **Required:** the SRS (.docx, .pdf or text).
- **Strongly recommended:** the original MoM (to check coverage).
- **Schema (always looked for):** schema files or a zip the user attached, the local
  folder `D:\SKM_SCHEMA`, or the `skmch-hrd-system-context` skill (conventions §7).
  The review always verifies the SRS impact analysis against the schema. Never ask the
  user to query the database.
- **Optional:** reviewer's own comments to apply, earlier review report (for re-review).

If the MoM isn't available, say so, skip the MoM-coverage checks (don't fake them), and
carry on.

## Two modes
1. **Review** (default): produce findings + recommendation.
2. **Apply comments:** the SA gives decisions or comments ("accept RV-03, reject RV-05,
   FR-007 should be Must"). Produce a revised SRS (next 0.x version, changes logged)
   and an updated findings table showing each finding's resolution.

## Review workflow

### 1. Structural and ID check
- All sections from the SRS structure are present (see `references/review-checklist.md` §A).
- IDs follow conventions and are unique. No renumbering relative to the previous version.
- Status is DRAFT or IN REVIEW, not APPROVED by an AI.

### 2. Coverage and traceability
- If the MoM is available, re-derive its points yourself and check each one is in the
  SRS or explicitly out of scope. Missing points are **Major** findings.
- Every FR cites a source. Every requirement appears in the traceability appendix.

### 3. Requirement quality (per FR/NFR)
Use checklist §B: atomic, unambiguous, testable, has a negative AC, feasible, no hidden
design, consistent with the other requirements. Quote the exact problem text in the
finding.

### 4. Domain and architecture review
This is the SA's value-add. Go through checklist §C:
- Workflow completeness: approval paths, rejection/cancel/rollback, delegation when the
  approver is on leave, back-dated entries, month/year-end cut-offs, concurrency (two
  people editing the same record), and bulk operations.
- Data lifecycle: creation, amendment, deletion vs deactivation, history, retention.
- Healthcare NFRs: access, audit, availability (24×7 areas), patient safety, privacy.
- Integration side-effects: payroll, attendance devices, HIS, finance/ERP, reporting and
  BI extracts.

### 5. Impact analysis verification (against the schema)
Load the schema (conventions §7). Index attached files, a zip or `D:\SKM_SCHEMA` first:
`python <skill-dir>/scripts/build_schema_index.py <files / zip / folder> --out <temp>/schema-index --copy-src`. Check all schemas (HRD, PAYROLL, REGISTRATION, DEFINITIONS, RFID, HIS, TRAINING).
If the SRS has no **Impact Analysis** section, or it isn't highlighted, that is a Major
finding. For each impact row:
- Does the object actually exist? Is the column name and type right?
- **Find what the SRS missed:** other packages, views, triggers, APEX pages, reports or
  jobs that reference the same tables or columns. Search the schema index's
  "referenced by" data and grep the sources for table and column names.
- Is any proposed new object already there under another name (duplication)?
- Is data migration or backfill needed and not mentioned?
Each missed dependency is a finding, with evidence (file/object where you found it).
Share the result in chat first, as an **Impact verification summary**: items confirmed,
items wrong, dependencies the SRS missed, names not found in the schema. Then continue
with the report. In the revised SRS, the corrected section 8 Impact Analysis stays
wrapped in `<!-- highlight -->` … `<!-- /highlight -->`.

### 6. Classify findings
| Severity | Meaning |
|---|---|
| **Blocker** | Can't design or build safely: missing core flow, contradiction, patient-safety or compliance gap, wrong schema assumption with big impact |
| **Major** | Will cause rework or defects: untestable FR, missing negative path, missed dependency, missing MoM point, missing NFR |
| **Minor** | Clarity, wording, formatting, IDs |
| **Observation** | Suggestion or improvement, optional |

Each finding: `RV-NN`, severity, location (section / requirement ID), issue (quote the
text), why it matters, **proposed fix** (actual replacement text where possible), and
question for BA/client if needed.

### 7. Recommendation
Exactly one of:
- **Ready for SA approval:** no Blocker or Major findings.
- **Approve after minor fixes:** Minor findings only.
- **Revise and re-review:** any Major finding.
- **Return to BA / client:** Blockers that need stakeholder input.

## Output
1. Review report as Markdown following `references/review-report-structure.md`, rendered:
   ```bash
   python <skill-dir>/scripts/render_docx.py review.md "<CR-ID>_SRS-Review_v1.docx" \
     --template <skill-dir>/templates/srs_review_template.docx \
     --meta DOC_ID=<CR-ID> --meta TITLE="SRS review – <feature>" --meta VERSION=1 \
     --meta STATUS="IN REVIEW" --meta AUTHOR="Claude (AI review) for <SA name>" \
     --meta SOURCE="<SRS file name and version>" --meta CHANGE_SUMMARY="Review of SRS v<x>"
   ```
2. **Revised SRS** (only when fixes are unambiguous, or in Apply-comments mode). Use the
   `skmch-ba-srs` structure. Bump the version (0.x → 0.x+1), keep IDs, add a
   version-history row. If the original is a .docx and tracked changes are wanted, use a
   docx skill that supports tracked changes. Otherwise produce a clean revised document
   and a change log table.
3. Chat summary: impact verification summary (step 5) first, then recommendation, finding counts by severity, top 5 Blocker/Major
   findings in one line each, and "Approval decision rests with the Solution
   Architect; record approval in the SRS approvals table (version 1.0)."

## Reference files
- `references/sdlc-conventions.md`: shared rules.
- `references/review-checklist.md`: full checklist (§A structure, §B requirement quality, §C domain/architecture, §D impact).
- `references/review-report-structure.md`: report layout.
- `references/examples/`: past SKMCH SA review comments, if supplied. Mirror their focus areas.
- `templates/srs_review_template.docx`, `scripts/render_docx.py`, `scripts/check_trace.py`
  (run `check_trace.py --source <MoM or SRS> --target <SRS> --ids FR,NFR` to find ID gaps).
- `scripts/build_schema_index.py`: indexes attached schema files, a zip or `D:\SKM_SCHEMA` (conventions §7).
