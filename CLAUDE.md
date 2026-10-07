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
- For the other stages use the matching skill in `skills/` (`skmch-sa-srs-review`,
  `skmch-sa-design-rfc`, `skmch-dev-implement`, `skmch-qa-testcases`, `skmch-qa-execute`,
  `skmch-sysdoc-update`).
