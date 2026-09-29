# Claude

Claude skills and database documentation for the SKM HIS Oracle database.

| Path | What |
|---|---|
| [`docs/schema/`](docs/schema/README.md) | Schema-wise data dictionary (DEFINITIONS, PAYROLL, RFID): tables, columns, keys, indexes, views, packages, triggers, synonyms |
| [`skm-domain/`](skm-domain/SKILL.md) | `skm-domain` skill — domain knowledge of the database for writing SQL/PL/SQL/APEX (`skm-domain.skill` is the packaged zip) |
| `oracle-plsql-apex-hrd-standards.skill` | Naming-convention standards skill for the HRD schema |
| [`tools/parse_schema.py`](tools/parse_schema.py) | Generator for the docs and skill references from PL/SQL Developer exports |
