---
name: skmch-hrd-system-context
description: Reference knowledge of the SKMCH Oracle schemas (HRD, PAYROLL, REGISTRATION, DEFINITIONS, RFID) and applications, built from schema files with no direct database access. Covers tables and columns, keys, indexes, triggers, packages and their procedures/functions, views, sequences, APEX applications and pages, and which code, views and APEX pages reference each table (dependency / where-used), plus system documents. Use whenever an SKMCH task needs to know what currently exists in the HRD database or applications. That includes impact analysis for an SRS or design doc, finding which packages or APEX pages use a table or column, checking whether a table/column/procedure exists and its exact name and data type, verifying object names in a review, or answering "where is X stored / handled" questions about HRD.
---

# SKMCH system context (HRD, PAYROLL, REGISTRATION, DEFINITIONS, RFID)

This skill is a searchable snapshot of the SKMCH schemas. The SDLC skills (SRS, review,
design, development, QA, system documentation) use it for impact analysis. SKMCH staff
have no direct database access, so **the schema files are the only permitted source for
claiming an object exists** (alongside files the user attaches).

## Where the schema comes from (check in this order)
1. **Files the user attached** in this conversation (schema `.txt`/`.sql` exports, a
   `.zip` of the schema folder, a data-dictionary `.csv`). They are newer than the
   snapshot in this skill. Index them:
   ```bash
   python <skill-dir>/scripts/build_schema_index.py <files / zip / folder> --out <temp>/schema-index --copy-src
   ```
   and use `<temp>/schema-index/` exactly like `references/` below.
2. **The local folder `D:\SKM_SCHEMA`** (or `SKMCH_SCHEMA_DIR`) when running in Claude
   Code / Claude Desktop on the SKMCH workstation. Index it the same way.
3. **This skill's snapshot** in `references/`.

## How to use it
1. Read `INDEX.md`. It gives the schema source and date, counts per schema, and one line
   per table. Mention the source and date in any impact analysis.
2. Open only the files you need:
   - `schemas/<OWNER>.md`: every table, package, procedure, function, view, trigger,
     sequence and synonym of that schema.
   - `tables/<OWNER>.<TABLE>.md`: columns (type, null, default, PK, comment), FKs, child
     FKs, indexes, triggers, synonyms pointing to it, and **Referenced by** (packages,
     views, triggers, APEX pages, in any schema). That list is the dependency list for
     impact analysis.
   - `programs/<OWNER>.<NAME>.md`: package spec units with signatures, tables used, calls,
     and callers.
   - `apex/app_<ID>.md`: pages and the tables each page touches (if APEX exports were given).
   - `objects.json`: the same data in machine-readable form. Use it with Python for bulk
     questions ("every table with column EMPLOYEE_ID").
   - `src/` (if present), or `src.zip` (unzip it to a temp folder first): raw source.
     Grep it for columns and literal usage that the index can't show, e.g.
     `grep -rn "LEAVE_STATUS" <temp>/src`.
3. The index finds references by name matching, schema-aware (it resolves `OWNER.NAME`
   and synonyms). Dynamic SQL and database links can still hide dependencies. Say so
   when an impact analysis relies only on the index for a high-risk change.
4. Tables listed as "referenced only (no DDL found)" exist in code but their CREATE
   statement wasn't in the export. Treat their columns as unknown.
5. If an object isn't in the index, report it as "not found in schema snapshot <date>".
   Never assume it exists.

## Status
If `references/INDEX.md` says NOT YET INDEXED and the user attached no schema files and
`D:\SKM_SCHEMA` isn't reachable, tell the user that impact analysis is PROVISIONAL and ask
them to attach the schema files (or a zip of `D:\SKM_SCHEMA`). A maintainer can also
build the snapshot into this skill:
```bash
python shared/scripts/build_schema_index.py D:\SKM_SCHEMA --copy-src
python scripts/package_skills.py
```
from the skills repository, then re-upload `dist/skmch-hrd-system-context.skill`.
