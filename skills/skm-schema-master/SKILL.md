---
name: skm-schema-master
description: "Entry point for the SKM Oracle database (schemas DEFINITIONS, HRD, PAYROLL, RFID). Routes to the per-schema skills and explains cross-schema relationships. Use first for any SKM database question, SQL/PL-SQL generation, reporting query or schema change."
---

# SKM Schema - Master Skill

The SKM database is split in four Oracle schemas. Each has its own skill; load the one(s) that match the request.

| Skill | Schema | Tables | Views | Packages | Purpose |
|---|---|---|---|---|---|
| `skm-definitions-schema` | DEFINITIONS | 1070 | 63 | 125 | master/lookup data (LOVs, definitions, locations, services, CPT, patients, abbreviations) shared by the other schemas. |
| `skm-hrd-schema` | HRD | 517 | 109 | 191 | human resource data (employees, applicants, leave, PA/appraisal, recruitment and related HR processes). |
| `skm-payroll-schema` | PAYROLL | 183 | 5 | 78 | payroll (pay, loans, expenses, employee pay components, performance income and related processing). |
| `skm-rfid-schema` | RFID | 43 | 15 | 15 | RFID/attendance machines, attendance records, machine access rights and door logs. |

## How to route
1. Identify the business area: lookup/master data -> `skm-definitions-schema`; employees/HR -> `skm-hrd-schema`; salary/loans/expenses -> `skm-payroll-schema`; attendance machines/RFID -> `skm-rfid-schema`.
2. Open that skill's `references/tables.md` and find the table (`## SCHEMA.TABLE`). Read columns, PK and FK lines.
3. Follow `FK` lines across schemas: `DEFINITIONS` is referenced by the others for lookup values; `HRD` employees link to `PAYROLL` and `RFID` records. Load the target schema's skill for the referenced table.
4. Before writing PL/SQL, check `references/code-objects.md` for an existing package/procedure instead of duplicating logic.
5. Use only names present in the skills. If a table or column is missing, say so and ask.

## Common conventions (all schemas)
- Audit columns `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_*` are maintained by triggers.
- Multi-location columns `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` mark where a record was created.
- Deleted rows are copied to `*_AUDIT` schemas via `SYN_*` synonyms.
- Y/N flag columns (e.g. `ACTIVE`) are single-character.
- Always schema-qualify objects; follow the company naming standards skill `oracle-plsql-apex-hrd-standards` for new objects.
