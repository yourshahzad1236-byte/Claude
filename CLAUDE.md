# CLAUDE.md

## Default skills for SKMCH SDLC documents

The SKMCH skills in `skills/` are linked into `.claude/skills/`, so every Claude Code
session in this repo loads them as project skills.

- **SRS:** whenever the user asks to create, write or update an SRS (or shares a MoM /
  meeting notes and asks for requirements), always use the `skmch-ba-srs` skill
  (`skills/skmch-ba-srs/SKILL.md` and its `references/`). Produce the Markdown source and
  render the Word file with `skills/skmch-ba-srs/scripts/render_docx.py` and
  `skills/skmch-ba-srs/templates/srs_template.docx`. Do not use a generic docs/document
  skill for SRS work.
- Outputs go to `docs/<CR-ID>/` (use `CR-YYYY-XXX` when no CR number is given), named
  `<CR-ID>_SRS_v<version>.docx` per `shared/references/sdlc-conventions.md`.
- **Schema first (BA and Solution Architect work):** before producing any SRS, SRS review
  or design output, read the SKMCH database schema per §7 of
  `shared/references/sdlc-conventions.md`: the DDL exports the user attaches
  (`HRD_SCHEMA.txt`, `DEFINITIONS_SCHEMA.txt`, `PAYROLL_SCHMA.txt`, `HIS.txt`,
  `REGISTRATION.txt`), `schema/` (including `schema/skm/*_SCHEMA.md`) and the
  `skmch-hrd-system-context` index when built. Verify every object name, read the triggers
  of affected tables, and reuse existing frameworks before proposing new objects. Never
  copy passwords or host IPs found in package bodies into any document.
- **CR documents:** when the user asks for a CR, use the client CR template and section rules in
  `skills/skmch-ba-srs/references/cr-template.md` (graphical swimlane workflow, GUI prototypes in
  the SKMCH GUI template, bullets for rules/data/impact; NFR, Risks and other excluded sections
  left out; no "Notes / open questions" in CR FR blocks; no Approval History / Finalization
  tabs on screens). "DD" means the
  **Design Document**: short, bullet points, ER diagram, technical details and GUI pages, made
  with `skmch-sa-design-rfc` as described in that file.
- For the other stages use the matching skill in `skills/` (`skmch-sa-srs-review`,
  `skmch-sa-design-rfc`, `skmch-dev-implement`, `skmch-qa-testcases`, `skmch-qa-execute`,
  `skmch-sysdoc-update`).
