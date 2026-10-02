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
- `references/architect/GUIDE.md`: the organization's **Architect standards** (data
  modeling, ERD and normalization, partitioning, tablespace design) plus the SKMCH rules
  that override them. **Apply them to every data-design decision in section 5.** Its
  routing table says which detailed guide to open:
  `references/architect/erd-design.md`, `references/architect/data-modeling.md`,
  `references/architect/partitioning-strategy.md`, `references/architect/tablespace-design.md`.
- If an Oracle SQL/PL-SQL development-standards skill is available (e.g. `oracle-developer`),
  apply it for SQL/PL-SQL quality: bind variables, bulk processing, exception handling
  and injection safety.

## Inputs
- **Required:** the SRS. Check its status. If it is not APPROVED, continue, but put a
  prominent warning in the design ("Based on SRS vX in status DRAFT; design may change")
  and mention it in chat.
- **Required for real impact analysis:** the schema files (conventions §7): schema
  files or a zip the user attached, the local folder `D:\SKM_SCHEMA`, or the
  `skmch-hrd-system-context` skill. The schema covers HRD, PAYROLL, REGISTRATION,
  DEFINITIONS, RFID, HIS and TRAINING, so check cross-schema use too. Without schema files the design is
  still produced, but every existing-object reference is `PROVISIONAL`, section 2 starts
  with a PROVISIONAL warning, and the change inventory carries a "verify against schema"
  task.
- **Optional:** SRS review report (resolve its design-relevant findings), existing
  package/APEX source the user attaches, the architect's preferred approach.

## Workflow

The order is fixed: **schema → impact analysis → share impact analysis → design document.**
Never write the design before the impact analysis is done and shown to the user.

### 1. Understand the requirement set
List every FR, NFR and RULE with a one-line interpretation. Mark items that are unclear
enough to block design as `Q-NN`. Never design around a guess silently. Write down every
table, column, screen, package or report name the SRS mentions. These are the search
terms for step 2.

### 2. Load and analyse the schema (always first)
1. Find the schema (conventions §7). For attached files, a zip or `D:\SKM_SCHEMA`, index
   them first:
   `python <skill-dir>/scripts/build_schema_index.py <files / zip / folder> --out <temp>/schema-index --copy-src`.
   Read `INDEX.md`, then `schemas/<OWNER>.md`, then only the table and program files
   you need. Grep the raw source (`<temp>/schema-index/src` or the folder) for column
   names and literals that the index can't show.
2. For every SRS entity and requirement, locate the current implementation:
   - Tables and columns involved (exact `OWNER.TABLE.COLUMN`, data types, keys,
     constraints, indexes, triggers).
   - **Dependents (where-used):** views, triggers, packages/procedures/functions, APEX
     pages, reports, jobs, synonyms, and code in **other schemas** (PAYROLL, REGISTRATION,
     DEFINITIONS, RFID, HIS, TRAINING) that read or write those tables and columns. Use each table
     file's "Referenced by" list and grep the source.
   - Existing program units that already do part of the job. **Reuse or extend before
     creating new.**
   - Names from the SRS that are **not found** in the schema.
3. Record each impacted object as `IMP-NN` with change type, risk (High/Medium/Low),
   related FR and evidence (schema file / index entry). Every modified object gets a
   "dependents to recompile/retest" list.

### 2a. Share the impact analysis BEFORE the design
Post an **Impact Analysis Summary** in chat before creating any file:
- Schema source, schemas covered and snapshot date.
- Counts: objects to create, modify, recompile and retest; schemas touched.
- A table of the High-risk impact items, with evidence.
- Names from the SRS not found in the schema, and the proposed action.
- Patient-safety relevant impacts.
- Overall impact rating (High / Medium / Low) with a one-line reason.

Then **stop and ask** if an object the SRS relies on is missing from the schema, or a
High-risk impact needs an architect decision (e.g. change a column used by PAYROLL
programs). Otherwise say "Proceeding to the design document" and continue in the same
reply.

### 3. Design decisions
- Choose the approach. For non-trivial choices, record alternatives considered and why
  they were rejected (short).
- Data model (per `references/architect/GUIDE.md`): prefer extending existing entities
  over parallel tables. Model new entities to 3NF, with explicit cardinality, named
  PK/FK/unique/check constraints and an index on every FK (`erd-design.md`). Copy the
  audit and multi-location columns and triggers that similar tables in the same schema
  use (`USER_ID`, `TERMINAL`, `TRN_DATE`, `ORIGINAL_*`, `ORG_ID`, `ZON_ID`, `LOC_ID`,
  `WS_SYNC_DATE`), and add history (`_HIS`) tables where AUD NFRs apply. Use soft
  delete for regulated data. Reporting needs: say whether an existing table, a view, a
  materialized view or a separate reporting model fits (`data-modeling.md`).
- Physical design: for every new table give the tablespace (the schema's existing one),
  estimated rows/year and growth, PCTFREE if it isn't the default, and LOB placement.
  For large or fast-growing tables (logs, history, attendance, transactions), decide
  partitioning explicitly (type, key, interval, local vs global indexes) using
  `partitioning-strategy.md` §8, or state why not. Flag licensed options (partitioning,
  Advanced Compression) as assumptions to confirm.
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
- **Section 2 is the Impact Analysis**, built from step 2 and wrapped in
  `<!-- highlight -->` … `<!-- /highlight -->` so it renders shaded and boxed in Word.
  It must match what you showed in chat.
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
- [ ] Section 2 Impact Analysis is present, highlighted, and lists the schema source and date.
- [ ] Every object named as existing has evidence. Everything else is `NEW` or `PROVISIONAL`.
- [ ] Cross-schema dependents (PAYROLL, REGISTRATION, DEFINITIONS, RFID, HIS, TRAINING) were checked.
- [ ] All new names comply with HRD standards (prefixes/suffixes, `_SEQ`, `TRG_…_BI`, `IDX_`, `VW_`).
- [ ] Every modified table lists its dependents to retest.
- [ ] Architect standards: new entities normalized (3NF) with cardinality stated; all
      constraints named; every FK indexed; no reserved words as column names; tablespace,
      volume and growth given per new table; partitioning decided for large tables;
      19c compatibility and licensed options flagged (`references/architect/GUIDE.md`).
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
The Impact Analysis Summary comes first (step 2a), then: file links. Counts (DS elements, new/modified tables, program units, APEX pages, files in
change inventory). **Top risks** and **open design questions**. Then: "Design is DRAFT
pending Solution Architect approval. After approval, developers can use
skmch-dev-implement and QA can use skmch-qa-testcases (from the SRS)."

## Reference files
- `references/sdlc-conventions.md`, `references/hrd-naming-standards.md`
- `references/design-structure.md`: exact design document layout.
- `references/architect/`: Architect standards (`GUIDE.md` first, then the matching guide).
- `references/examples/`: past SKMCH design docs/RFCs when available. Match their depth and style.
- `templates/design_rfc_template.docx`, `scripts/render_docx.py`, `scripts/check_trace.py`
- `scripts/build_schema_index.py`: indexes attached schema files, a zip or `D:\SKM_SCHEMA`.
