---
name: skm-schema
description: "Entry point for the SKM Oracle database (schemas DEFINITIONS, HRD, PAYROLL, RFID). Routes to the per-schema skills and explains cross-schema relationships. Use first for any SKM database question, SQL/PL-SQL generation, reporting query or schema change."
---

# SKM Schema

The SKM database is split in four Oracle schemas. Each has its own reference file; read the one(s) that match the request.

| Reference file | Schema | Use for |
|---|---|---|
| `references/DEFINITIONS_SCHEMA.md` | DEFINITIONS | master/lookup data (LOVs, locations, services, CPT, patients, abbreviations) shared by other schemas |
| `references/HRD_SCHEMA.md` | HRD | employees, applicants, leave, appraisal (PA), recruitment, other HR processes |
| `references/PAYROLL_SCHEMA.md` | PAYROLL | pay, loans, expenses, employee pay components, performance income |
| `references/RFID_SCHEMA.md` | RFID | attendance machines, attendance records, access rights, door logs |

Each reference file is one markdown document with four parts: **Tables** (columns, types, nullability, comments, PK/UK/FK/CHECK, indexes, triggers), **Views**, **Packages/procedures/functions/sequences**, **Synonyms**. Search a file for `### SCHEMA.TABLE_NAME` instead of reading it whole.

## How to route
1. Identify the business area: lookup/master data -> `references/DEFINITIONS_SCHEMA.md`; employees/HR -> `references/HRD_SCHEMA.md`; salary/loans/expenses -> `references/PAYROLL_SCHEMA.md`; attendance machines/RFID -> `references/RFID_SCHEMA.md`.
2. Open that reference file and find the table (`### SCHEMA.TABLE`) in the Tables part. Read columns, PK and FK lines.
3. Follow `FK` lines across schemas: Read the target schema's reference file for the referenced table.
4. Before writing PL/SQL, check the Packages part for an existing package/procedure instead of duplicating logic.
5. Use only names present in the skills. If a table or column is missing, say so and ask.

## Common conventions (all schemas)
- Audit columns `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_*` are maintained by triggers.
- Multi-location columns `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` mark where a record was created.
- Deleted rows are copied to `*_AUDIT` schemas via `SYN_*` synonyms.
- Y/N flag columns (e.g. `ACTIVE`) are single-character.
- Always schema-qualify objects; follow the company naming standards skill `oracle-plsql-apex-hrd-standards` for new objects.
