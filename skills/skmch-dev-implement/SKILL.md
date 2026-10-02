---
name: skmch-dev-implement
description: Implements an approved SKMCH technical design document (Design Doc / RFC) as Oracle code for the HRD schema. Produces ordered DDL scripts, PL/SQL package specs and bodies, procedures, functions, triggers, views, data migration, grants, APEX page change instructions, rollback scripts, a master install script, unit tests and implementation notes, following HRD naming standards and tracing each object to design (DS) and requirement (FR) IDs. Use when a developer shares a design doc or RFC and asks to implement it, write or generate the code, create the DDL, packages, procedures or scripts for a CR, or build the change described in the design. Do NOT use to create the design itself (skmch-sa-design-rfc) or for general Oracle questions unrelated to an SKMCH design.
---

# SKMCH: Design Doc → code

You are the SKMCH developer. You implement exactly what the approved design specifies,
to HRD standards, and you make every deviation visible.

Read first:
- `references/sdlc-conventions.md`
- `references/hrd-naming-standards.md`: mandatory naming for every object, variable and parameter.
- `references/coding-standards.md`: SKMCH PL/SQL and APEX coding rules.
- If an Oracle SQL/PL-SQL development-standards skill is available (e.g. `oracle-developer`), apply it too.

## Inputs
- **Required:** the design doc. Check its status. If it is not APPROVED, warn and continue
  only if the user confirms (they may be prototyping).
- **Strongly recommended:** current source of every object marked MODIFIED (package
  bodies, views, triggers, APEX export). Take it from the repo / schema context. **Never
  rewrite an existing package from memory.** If the current source isn't available, produce
  only the delta (new procedures plus exact instructions for where they go) and say so.
- **Optional:** the SRS (for acceptance criteria and unit tests), the repo's existing folder layout.
- **Schema (always looked for):** schema files or a zip the user attached, the local
  folder `D:\SKM_SCHEMA`, or the `skmch-hrd-system-context` skill (conventions §7).
  Never ask the user to query the database: they have no direct DB access.
  The current source of MODIFIED objects is usually in the schema files: take it from there.

## Workflow

### 0. Schema check and impact re-verification (before writing any code)
Load the schema (conventions §7). Index attached files, a zip or `D:\SKM_SCHEMA` first:
`python <skill-dir>/scripts/build_schema_index.py <files / zip / folder> --out <temp>/schema-index --copy-src`. Then, for every object in the design's change inventory:
- Confirm that objects marked existing really exist, with the same columns, types and
  signatures as the design assumes. Get their **current source** from the schema files.
- Confirm that objects marked NEW don't already exist (name clash) in any schema.
- Re-check dependents (where-used) of every modified table, column and package across
  HRD, PAYROLL, REGISTRATION, DEFINITIONS and RFID, against the design's §2.5. Anything
  the design missed is a **deviation**.
Post an **Impact re-check summary** in chat before the code: confirmed items,
differences from the design, extra dependents to recompile/retest. Stop and ask if the
schema contradicts the design in a way that changes the code (e.g. a column the design
modifies is used by PAYROLL code the design didn't list).

### 1. Build the task list from the design's Change inventory (§11)
One task per row. Add any object the design forgot but you need (for example a sequence
for a new PK). That is a **deviation** and must be logged.

### 2. Decide the file layout
- In a repo (Claude Code): look at existing folders and naming (`git ls-files '*.sql' '*.pks' '*.pkb'`)
  and follow them.
- Otherwise use:
```
<CR-ID>/
  install.sql            # master: SET DEFINE OFF; WHENEVER SQLERROR EXIT FAILURE ROLLBACK; @@ each script in order; SPOOL log
  01_ddl/                # 010_<object>.sql … tables, columns, constraints, indexes, sequences
  02_data/               # migration / seed data (idempotent, guarded)
  03_code/               # <PKG>.pks, <PKG>.pkb, views (VW_), triggers (TRG_), functions/procedures
  04_security/           # grants, synonyms, VPD policies
  05_jobs/               # DBMS_SCHEDULER jobs
  06_apex/               # page change instructions (.md) or split-export files
  90_tests/              # unit tests (utPLSQL if available, else anonymous-block tests)
  99_rollback/           # rollback.sql in reverse order
```

### 3. Write the code
- Follow the design's signatures exactly (names, parameter order and types). If a
  signature can't work as designed, implement the closest correct version and log the
  deviation with the reason.
- Header block on every file: CR-ID, DS-IDs, FR-IDs, author ("Claude (AI) for <dev>"),
  date, and change description. For MODIFIED packages, add a change-log line and mark changed
  regions with `-- <CR-ID> begin/end`.
- DDL: schema-qualified, named constraints, `COMMENT ON` for tables and columns, idempotent
  guards where practical (check `ALL_TAB_COLUMNS` / `ALL_OBJECTS` before `ALTER`/`CREATE`
  in migration blocks).
- Package spec + body in separate files. Body implements the numbered logic from the design.
- APEX: never hand-write APEX export internals. Produce a precise page-change instruction
  sheet (page, component, static ID, property → value, PL/SQL source that calls the
  package). If the user supplied a split export, edit only the needed component files
  and note that the export must be re-imported and verified in the APEX Builder.
- Rollback: every forward script has a reverse step. State where rollback loses data.

### 4. Unit tests
For each new or changed program unit, write tests for the happy path, each raised
exception, and the SRS acceptance criteria that apply to it (use synthetic data, and
roll back or clean up after). Use utPLSQL if the repo uses it. Otherwise use
self-checking anonymous blocks that print PASS/FAIL.

### 5. Self-review (checklist in `references/coding-standards.md` §9)
Fix issues before output. Run `python scripts/check_trace.py --source <design> --target <CR-ID>/ --ids DS`
to confirm every DS is implemented. Use `--ids FR` against the SRS for a rough check.

### 6. Implementation notes document
Markdown per `references/impl-notes-structure.md`, rendered:
```bash
python <skill-dir>/scripts/render_docx.py impl.md "<CR-ID>_ImplNotes_v1.docx" \
  --template <skill-dir>/templates/impl_notes_template.docx \
  --meta DOC_ID=<CR-ID> --meta TITLE="<feature>" --meta VERSION=1 --meta STATUS=DRAFT \
  --meta AUTHOR="Claude (AI) for <developer>" --meta SOURCE="Design <file> v<x>" \
  --meta CHANGE_SUMMARY="Implementation of design v<x>"
```

### 7. Reply in chat
The impact re-check summary (step 0) first. Then files produced (tree). Deviations from design (all of them). What the developer must do
manually (APEX builder steps, compile in DEV, run tests). Reminder: "Scripts are not
executed by Claude. Run in DEV first, then code review before promotion."

## Reference files
- `references/sdlc-conventions.md`, `references/hrd-naming-standards.md`
- `references/coding-standards.md`: SKMCH PL/SQL, SQL and APEX rules plus the self-review checklist.
- `references/impl-notes-structure.md`: implementation notes layout.
- `references/examples/`: real SKMCH code samples when available. Match their style exactly.
- `templates/impl_notes_template.docx`, `scripts/render_docx.py`, `scripts/check_trace.py`
- `scripts/build_schema_index.py`: indexes attached schema files, a zip or `D:\SKM_SCHEMA` (conventions §7).
