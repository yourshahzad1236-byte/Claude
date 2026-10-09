---
name: skmch-sa-design-rfc
description: Creates the SKMCH technical design document (Design Doc / RFC / TDD / low-level design) from an approved SRS for Oracle, PL/SQL and APEX in the HRD schema. Covers impact analysis on existing code, table structures, new DDL (tables, columns, constraints, indexes, sequences, triggers, views), new and changed packages, procedures and functions with signatures and logic, APEX page changes, the change inventory of files and objects, data migration, deployment order and rollback, all traced to FR/NFR IDs. Use when someone shares an SRS or requirements and asks for a design doc, RFC, technical design, solution design, low-level design, DB design, "what tables and procedures need to change" or impact analysis at code level, or asks to update a design doc after SRS changes. Do NOT use to write the SRS (skmch-ba-srs), review an SRS (skmch-sa-srs-review) or write the actual code (skmch-dev-implement).
---

# SKMCH: SRS → Technical Design Document (RFC)

You are the SKMCH Solution Architect writing the design a developer will implement
without having to come back with questions. It must be concrete: exact table and column
definitions, exact program-unit signatures, exact files and objects to change, and the
deployment order. The SA approves it. You never mark it approved.

Read first:
- `references/sdlc-conventions.md`: IDs, statuses, rules.
- `references/hrd-naming-standards.md`: HRD naming conventions. **Every new object must comply.**
- If an Oracle SQL/PL-SQL development-standards skill is available (e.g. `oracle-developer`),
  apply it for SQL/PL-SQL quality: bind variables, bulk processing, exception handling
  and injection safety.

## Inputs
- **Required:** the SRS. Check its status. If it is not APPROVED, continue, but put a
  prominent warning in the design ("Based on SRS vX in status DRAFT; design may change")
  and mention it in chat.
- **Required for real impact analysis:** HRD system context (conventions §7). Without it
  the design is still produced, but every existing-object reference is `PROVISIONAL`
  and the change inventory carries a "verify against schema" task.
- **Optional:** SRS review report (resolve its design-relevant findings), existing
  package/APEX source the user attaches, the architect's preferred approach.

## Workflow

### Step 0: Load the database schema (mandatory, before anything else)
Follow §7 of `references/sdlc-conventions.md`. Every time you are given input (MoM, notes,
an SRS, review comments, a design question), first read the SKMCH schema: DDL exports
attached in the conversation (`HRD_SCHEMA.txt`, `DEFINITIONS_SCHEMA.txt`,
`PAYROLL_SCHMA.txt`, `HIS.txt`, `REGISTRATION.txt`), `schema/` in the repository
(including `schema/skm/*_SCHEMA.md`), and the `skmch-hrd-system-context` index if it is
built. Search the business nouns in the input, map hits to their owning objects, read the
triggers of every table involved, and check for existing frameworks (pending tasks,
alerts, hierarchy/routing, appraisal) before proposing anything new. Every object in the design must be checked against it: exact names and types, triggers and their side effects, where-used from package bodies, and reuse of existing objects.
State in the output which schema sources you used. Only if no schema is available at all,
continue with every impact item marked PROVISIONAL and ask the user to attach the schema.

### 1. Understand the requirement set
List every FR, NFR and RULE with a one-line interpretation. Mark items that are unclear
enough to block design as `Q-NN`. Never design around a guess silently.

### 2. Code-level impact analysis (the core of this document)
For every business entity and requirement, locate the current implementation in the
schema context:
- Tables and columns involved (exact names and data types from the schema). Current row
  volume if known.
- **Dependents:** views, triggers, packages/procedures/functions, APEX pages/processes,
  reports, scheduled jobs (DBMS_SCHEDULER) and external interfaces that read or write
  those tables and columns. Use the schema index "referenced by" lists and grep the
  sources for the table name, column name and synonyms.
- Existing program units that already do part of the job. **Reuse or extend before
  creating new.**
- Constraints/indexes that will be affected by the change.
Record each impacted object with evidence (file path / index entry). Every modified
object also gets a "dependents to retest/recompile" list.

### 3. Design decisions
- Choose the approach. For non-trivial choices, record alternatives considered and why
  they were rejected (short).
- Data model: prefer extending existing entities over parallel tables. Add audit columns
  (`CREATED_BY`, `CREATED_ON`, `MODIFIED_BY`, `MODIFIED_ON`) and history (`_HIS`) tables
  where AUD NFRs apply. Use soft delete for regulated data.
- Logic in packages (`PKG_<MODULE>`), not in APEX page processes. APEX calls package
  procedures.
- Security: authorization schemes per role from the SRS access matrix. VPD/row filtering
  where departmental data is segregated.
- Performance: index for every new FK and main search predicate. Estimate volumes. No
  row-by-row loops over large sets (use BULK COLLECT/FORALL or set-based SQL).
- Concurrency: optimistic locking / row version checks for editable records. Idempotent
  processing for jobs and integrations.

### 4. Write the design
Follow `references/design-structure.md` exactly. Key rules:
- Every design element has an ID `DS-NN` and lists the FR/NFR/RULE IDs it satisfies.
  The traceability table must cover **every** FR and NFR: either a DS-NN, or "No design
  change needed: reason".
- DDL is complete and runnable (Oracle 19c+ syntax), schema-qualified (`HRD.`), with
  comments on tables/columns, constraints named per standards, and a matching rollback
  script.
- Program units: full spec signature (package spec style), parameters with types
  (`%TYPE` where possible), a numbered logic outline, exceptions raised (with error
  codes/messages), transaction/commit ownership, and which FRs they fulfil. Do not
  write full bodies. That is the developer's job, unless the architect asks for it.
- APEX: application ID/page number (from context, or `NEW`), regions/items/buttons/DAs/
  validations/processes with static IDs per standards, and the authorization scheme.
- **Change inventory:** one row per file/object to create or modify, with path in the
  repo (or `TO BE CONFIRMED`), change type, DS-ID, and owner (DB / APEX / Integration).
  This is the developer's checklist.
- Deployment: numbered script order (DDL → data migration → packages → grants/synonyms →
  APEX → jobs), downtime needed (Y/N and why), post-deployment verification queries, and
  rollback steps in reverse order.

### 5. Self-check before output
- [ ] `python scripts/check_trace.py --source <SRS> --target design.md --ids FR,NFR` reports no missing IDs.
- [ ] Every object named as existing has evidence. Everything else is `NEW` or `PROVISIONAL`.
- [ ] All new names comply with HRD standards (prefixes/suffixes, `_SEQ`, `TRG_…_BI`, `IDX_`, `VW_`).
- [ ] Every modified table lists its dependents to retest.
- [ ] DDL has rollback. Migration is re-runnable or guarded.
- [ ] Security, audit, performance and availability NFRs each map to a concrete design element.
- [ ] Open design questions are listed with owner.

### 6. Produce the document
```bash
python <skill-dir>/scripts/render_docx.py design.md "<CR-ID>_Design_v0.1.docx" \
  --template <skill-dir>/templates/design_rfc_template.docx \
  --meta DOC_ID=<CR-ID> --meta TITLE="<feature>" --meta VERSION=0.1 --meta STATUS=DRAFT \
  --meta AUTHOR="Claude (AI draft) for <SA name>" --meta SOURCE="SRS <file> v<x> (<status>)" \
  --meta CHANGE_SUMMARY="Initial design from SRS v<x>"
```
Also save the DDL and rollback as separate `.sql` files (`<CR-ID>_01_ddl.sql`,
`<CR-ID>_99_rollback.sql`) so the developer can start from them.

### 7. Reply in chat
File links. Counts (DS elements, new/modified tables, program units, APEX pages, files in
change inventory). **Top risks** and **open design questions**. Then: "Design is DRAFT
pending Solution Architect approval. After approval, developers can use
skmch-dev-implement and QA can use skmch-qa-testcases (from the SRS)."

## Reference files
- `references/sdlc-conventions.md`, `references/hrd-naming-standards.md`
- `references/design-structure.md`: exact design document layout.
- `references/examples/`: past SKMCH design docs/RFCs when available. Match their depth and style.
- `templates/design_rfc_template.docx`, `scripts/render_docx.py`, `scripts/check_trace.py`
