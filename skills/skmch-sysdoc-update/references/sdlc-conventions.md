# SKMCH SDLC conventions (shared by all SKMCH SDLC skills)

These rules keep every artifact traceable from the meeting notes to the system
documentation. Every SKMCH SDLC skill follows them. Do not invent alternatives.

## 1. The flow

| # | Stage | Owner (human) | Input | Output artifact | Skill |
|---|-------|---------------|-------|-----------------|-------|
| 1 | Requirement gathering | BA | Meetings | Minutes of Meeting (MoM) | (human) |
| 2 | Requirement specification | BA / BA developer | MoM | SRS (.docx) | `skmch-ba-srs` |
| 3 | SRS review and approval | Solution Architect | SRS | Review report + revised SRS | `skmch-sa-srs-review` |
| 4 | Technical design (RFC) | Solution Architect | Approved SRS | Design Doc / RFC (.docx) | `skmch-sa-design-rfc` |
| 5 | Development | Developer | Approved Design Doc | DDL, PL/SQL, APEX changes + implementation notes | `skmch-dev-implement` |
| 6a | Test design (parallel to 5) | QA | Approved SRS | Test cases (.xlsx) | `skmch-qa-testcases` |
| 6b | Test execution | QA | Test cases + build | Test scripts + execution report (.xlsx) | `skmch-qa-execute` |
| 7 | System documentation | Implementation Engineer | SRS + Design + code + test results | System-doc update (.docx) | `skmch-sysdoc-update` |

Human gates. Claude never marks these as passed on its own:
- Gate 1: SA approves the SRS (after stage 3).
- Gate 2: SA approves the Design Doc (after stage 4).
- Gate 3: QA sign-off (after stage 6b), which is needed before the system doc is published.

## 2. Identifiers

| Item | Format | Example | Created in |
|------|--------|---------|------------|
| Change request / feature | `CR-YYYY-NNN`, or the organization's own ticket number if the user gives one | `CR-2026-014` | Stage 2 (ask the user; propose one if none exists) |
| MoM point | `M-NN` | `M-07` | Stage 2: every atomic statement in the notes gets numbered |
| Business requirement | `BR-NN` | `BR-03` | Stage 2 |
| Functional requirement | `FR-NNN` | `FR-012` | Stage 2 |
| Non-functional requirement | `NFR-<CAT>-NN` where CAT is PERF, SEC, AUD, AVL, USA, CMP, DAT, INT or OPS | `NFR-SEC-02` | Stage 2 |
| Business rule | `RULE-NN` | `RULE-05` | Stage 2 |
| Assumption | `A-NN` | `A-02` | Any stage |
| Open question | `Q-NN` | `Q-04` | Any stage |
| Impact item | `IMP-NN` | `IMP-09` | Stages 2 and 4 |
| Review finding | `RV-NN` | `RV-06` | Stage 3 |
| Design element | `DS-NN` | `DS-04` | Stage 4 |
| Test case | `TC-NNN` | `TC-031` | Stage 6a |
| Defect | `DEF-NN` | `DEF-03` | Stage 6b |

Rules:
- Once an ID is published it is never reused or renumbered. A deleted requirement keeps its ID and is marked `WITHDRAWN`.
- New items get the next free number, even if that leaves gaps.
- Every downstream item cites the upstream IDs it covers (FR → DS → code object → TC → system-doc entry).

## 3. Document status and versioning

- Status values: `DRAFT` → `IN REVIEW` → `APPROVED` → `SUPERSEDED`.
- Claude-produced documents are always `DRAFT`, or `IN REVIEW` when a human asks for that. Only a named human sets `APPROVED`, and the approver's name and date are recorded in the approval table.
- Versions: drafts use `0.x` (0.1, 0.2 …). The first approved version is `1.0`. Changes after approval go to `1.1`, `1.2` … and every change is logged in the version-history table.

## 4. File names

`<CR-ID>_<DocType>_v<version>.<ext>`. DocType is one of `MoM`, `SRS`, `SRS-Review`,
`Design`, `TestCases`, `TestExecution`, `ImplNotes` or `SysDoc-Update`.
Example: `CR-2026-014_Design_v0.1.docx`.

## 5. Where outputs go

- claude.ai / Claude Desktop: write final files to `/mnt/user-data/outputs/` (or the
  outputs location the environment specifies) so the user can download them.
- Claude Code: write into the repository path the user names. If they name none, use
  `docs/<CR-ID>/` for documents and `db/<CR-ID>/` for SQL.
- Keep working files (JSON for render_xlsx, helper scripts, scratch notes) in a temporary
  folder, not the output folder. The only exception is the Markdown source of a Word
  document, which may be kept next to the .docx.
- Always also give a short summary in chat: counts of requirements, open questions,
  impacted objects and so on, plus anything that needs a human decision.

## 6. Non-negotiables

1. **Don't guess.** When the input does not support a statement, record it as an
   assumption (`A-NN`) or an open question (`Q-NN`). Never state it as fact.
2. **Don't invent schema.** Name an existing table, column, package or APEX page only
   if it appears in the HRD system context (see §7) or in material the user supplied.
   Everything else is marked `NEW` or `TO BE CONFIRMED`.
3. **No patient data.** Never copy patient identifiers (MR number, name, CNIC, phone,
   diagnosis) from inputs into examples or test data. Use synthetic values such as
   `MRN-TEST-0001`. If an input contains real patient data, tell the user.
4. **No live DB changes.** Produce scripts only. Humans or CI run them.
5. **Humans approve.** Never mark a gate as passed or a document as `APPROVED`.
6. **Standards.** Every new or changed HRD object follows the
   `oracle-plsql-apex-hrd-standards` naming conventions.

## 7. Finding HRD system context (schema, packages, APEX, system docs)

Before any impact analysis, look for context in this order and say which one you used:
1. Files the user attached in this conversation, or the Claude Project's knowledge.
2. The `skmch-hrd-system-context` skill, if it is available. Read its `INDEX.md` first
   and then open only the object files you need.
3. In Claude Code: the folder named by the `SKMCH_SCHEMA_DIR` environment variable, or
   `schema/` in the repository.

If none of these is available, continue, but mark every impact item `PROVISIONAL`,
add a prominent note in the document that impact analysis was done without schema
access, and tell the user.

## 8. Healthcare-specific checks (apply at every stage)

- Patient safety: can a defect here cause a clinical, medication or billing error? If
  so, flag it and require negative tests.
- Confidentiality: role-based access to patient and employee data, masking, audit of
  who viewed or changed what.
- Auditability: created by, created on, modified by, modified on, and history tables
  for regulated data.
- Availability: many hospital services run 24×7, so the deployment and migration plan
  must say whether downtime is needed.
- Integration: HIS, LIS, RIS/PACS, pharmacy, billing and HR/payroll feeds. Name each
  feed that the change touches.
