---
name: skmch-hrd-system-context
description: Reference knowledge of the SKMCH HRD Oracle schema and applications. Covers tables and columns, keys, indexes, triggers, packages and their procedures/functions, views, sequences, APEX applications and pages, and which code, views and APEX pages reference each table (dependency / where-used), plus system documents. Use whenever an SKMCH task needs to know what currently exists in the HRD database or applications. That includes impact analysis for an SRS or design doc, finding which packages or APEX pages use a table or column, checking whether a table/column/procedure exists and its exact name and data type, verifying object names in a review, or answering "where is X stored / handled" questions about HRD.
---

# SKMCH HRD system context

This skill is a searchable snapshot of the HRD schema. The SDLC skills (SRS, review,
design, development, QA, system documentation) use it for impact analysis. **It is the
only permitted source for claiming an object exists** (alongside files the user attaches).

## How to use it
1. Read `references/INDEX.md`. It gives counts and one line per table and code object.
   Check the snapshot date/source at the top and mention it in any impact analysis.
2. Open only the files you need:
   - `references/tables/<TABLE>.md`: columns (type, null, default, PK), FKs, child FKs,
     indexes, triggers and **Referenced by** (packages, views, triggers, APEX pages).
     That list is the dependency list for impact analysis.
   - `references/programs/<NAME>.md`: package spec units with signatures, and tables used.
   - `references/apex/app_<ID>.md`: pages and the tables each page touches.
   - `references/objects.json`: the same data in machine-readable form. Use it with
     Python for bulk questions ("every table with column EMPLOYEE_ID").
   - `references/src/` (if present): raw source. Grep it for columns and literal usage
     that the index can't show, e.g. `grep -rn "LEAVE_STATUS" references/src`.
3. The index finds references by name matching. Dynamic SQL, synonyms and database links
   can hide dependencies. Say so when an impact analysis relies only on the index for a
   high-risk change.
4. If an object isn't in the index, report it as "not found in schema snapshot <date>".
   Never assume it exists.

## Status
If `references/INDEX.md` says NOT YET INDEXED, the schema folder hasn't been indexed yet. Tell the
user that impact analysis is PROVISIONAL, and that a maintainer should run:
```bash
python scripts/build_schema_index.py <shared-schema-folder> --copy-src
```
from the skills repository, then re-package and re-upload this skill (see repository README).
