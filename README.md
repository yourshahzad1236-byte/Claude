# SKMCH SDLC skills for Claude

Claude skills that take on each role in the SKMCH software development lifecycle. Staff
use Claude as they normally would, and **the right skill loads automatically** from what
they ask. For example, a BA pastes meeting notes and writes "make the SRS", and Claude
produces an SRS in Word using the hospital template.

```
 MoM ──► SRS ──► SA review ──► Design doc / RFC ──► Code ──► Test execution ──► System doc
  BA     ba-srs   sa-srs-review  sa-design-rfc     dev-implement   qa-execute      sysdoc-update
                 [Gate 1: SA approves SRS] [Gate 2: SA approves design]  [Gate 3: QA sign-off]
                        └──────────► QA test cases (qa-testcases, parallel with development)
```

Humans still approve at every gate. Claude drafts, checks and traces, and never marks
anything APPROVED.

## Schema first, impact analysis first

Staff have no direct database access, so every skill works from the schema export files
(HRD, PAYROLL, REGISTRATION, DEFINITIONS, RFID, HIS, TRAINING):

1. **Find the schema:** files or a zip attached to the chat or Project, the local folder
   `D:\SKM_SCHEMA`, or the `skmch-hrd-system-context` skill. Attached files and the
   folder are indexed on the fly by `scripts/build_schema_index.py`, which is inside every skill.
2. **Analyse impact** against the schema: tables, columns, dependents (packages, views,
   triggers, APEX pages, synonyms) and cross-schema use.
3. **Share the Impact Analysis Summary in chat first**, then produce the document.
4. The SRS, design doc/RFC, implementation notes and system-doc update each contain an
   **Impact Analysis** section that is **highlighted** (shaded and boxed) in Word. In the
   design doc it is section 2, before the solution design.

## The skills

| Skill | Who uses it | Example prompt | Output |
|---|---|---|---|
| `skmch-ba-srs` | BA | "Here are the minutes from today's meeting with Nursing. Create the SRS." | SRS .docx: FR/NFR, acceptance criteria, impact analysis, open questions |
| `skmch-sa-srs-review` | Solution Architect | "Review this SRS. Is it ready for approval?" | Review report (Blocker/Major/Minor) + revised SRS |
| `skmch-sa-design-rfc` | Solution Architect | "Create the design doc for this approved SRS." | Design .docx: DDL, packages, APEX changes, change inventory, deployment/rollback |
| `skmch-dev-implement` | Developer | "Implement this design doc." | Ordered SQL/PLSQL scripts, rollback, unit tests, implementation notes |
| `skmch-qa-testcases` | QA | "Write test cases for this SRS." | Test cases .xlsx + traceability matrix |
| `skmch-qa-execute` | QA | "Generate test scripts" / "Here are the results, make the execution report." | Test data + verification SQL, execution report .xlsx, defects, sign-off recommendation |
| `skmch-sysdoc-update` | Implementation Engineer | "Update the system documentation for CR-2026-014." | System-doc update .docx |
| `skmch-sdlc-guide` | Anyone | "What's the next step for this CR?" / "Check traceability of these documents." | Process answers, traceability audit |
| `skmch-hrd-system-context` | (used by the other skills) | "Which packages use HRD_LEAVE_REQUEST?" | Schema/dependency lookups for impact analysis |
| `oracle-plsql-apex-hrd-standards` | (used by design/dev) | "Name the new table for leave encashment." | HRD naming conventions |

All IDs, statuses and rules are defined once in `shared/references/sdlc-conventions.md`.

## Rolling out to the organization

### Claude.ai / Claude Desktop (BAs, SAs, QA, implementation engineers)
1. Build the packages: `python scripts/package_skills.py` → `dist/*.skill`.
2. An organization **Owner** uploads each `dist/*.skill` in the Claude admin settings
   (organization skills), which makes them available to all members.
3. Make sure **code execution and file creation** is enabled for the organization. The
   skills use it to produce Word/Excel files.
4. Tell staff that nothing special is needed. They just ask Claude, and it can attach
   their files (MoM, SRS, design doc).
5. Optional: create a shared Claude **Project** "SKMCH SDLC" per module, with the system
   documents in its knowledge, for extra context.

### Claude Code (developers, architects)
```
/plugin marketplace add yourshahzad1236-byte/claude
/plugin install skmch-sdlc@skmch
```
In Claude Code on the SKMCH workstation the skills read the schema from `D:\SKM_SCHEMA`.
Set `SKMCH_SCHEMA_DIR` only if the folder is somewhere else.

## Maintaining the skills

| Task | How |
|---|---|
| Change a skill's behaviour | Edit `skills/<skill>/SKILL.md` or its `references/` |
| Change shared rules (IDs, statuses, gates, schema-first) | Edit `shared/references/sdlc-conventions.md` (never the copies inside skills). Shared scripts live in `shared/scripts/`. |
| Change naming standards | Edit `skills/oracle-plsql-apex-hrd-standards/SKILL.md` |
| Use the official hospital template | Replace `skills/<skill>/templates/<name>.docx/.xlsx` (same file name). In Word templates, put `{{BODY}}` on its own line where content goes, and use `{{DOC_ID}} {{TITLE}} {{VERSION}} {{STATUS}} {{DATE}} {{AUTHOR}} {{SOURCE}} {{CHANGE_SUMMARY}}` where those values go. Excel templates need header rows whose names match the columns in the skill. If section headings differ from the template, update the matching `references/*-structure.md`. |
| Refresh schema knowledge | Update the exports in `D:\SKM_SCHEMA`. For a built-in snapshot (private upload only, never commit it: this repo is public), run `python shared/scripts/build_schema_index.py D:\SKM_SCHEMA --zip-src`, then `python scripts/package_skills.py`. See `schema/README.md`. |
| Add real examples | Curate masked files from `samples/` into `skills/<skill>/references/examples/` |
| Release | `python scripts/package_skills.py`, commit, re-upload the changed `dist/*.skill` files |

`python scripts/package_skills.py --check` runs in CI. It fails if the synced copies are
stale or a skill's frontmatter is invalid.

Placeholder templates are generated by `scripts/build_templates.py`. Re-run it only to
reset the placeholders.

## Samples wanted
See [`samples/README.md`](samples/README.md). Real (masked) MoM → SRS → design → code →
test → system-doc chains make the skills match SKMCH's own style.
