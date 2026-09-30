# HRD schema folder

Put the shared schema folder here (or upload it as `schema.zip`). Include any of:
- table DDL (`.sql`, `.ddl`, `.tab`)
- package specs/bodies, procedures, functions, triggers, views (`.pks`, `.pkb`, `.sql`, …)
- APEX application exports (`f<app>.sql` or split exports)
- a data-dictionary export as CSV (`TABLE_NAME, COLUMN_NAME, DATA_TYPE, DATA_LENGTH, NULLABLE, COMMENTS`)
- system documents (`.docx`, `.pdf`, `.md`)

Then build the system-context skill:
```bash
python scripts/build_schema_index.py schema --copy-src
python scripts/package_skills.py
```
**No data, only structure and code.** Remove passwords, DB links with credentials and
server names before uploading.
