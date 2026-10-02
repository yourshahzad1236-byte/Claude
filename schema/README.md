# Schema folder (private)

SKMCH staff have no direct database access, so the skills work from schema export files.
The master copy lives on the SKMCH workstation at **`D:\SKM_SCHEMA`**. It currently
holds one export per schema: HRD, PAYROLL, REGISTRATION, DEFINITIONS and RFID (PL/SQL
Developer "Export User Objects" `.txt`/`.sql` files).

Accepted files: table DDL, package specs/bodies, procedures, functions, triggers, views,
synonyms (`.sql`, `.txt`, `.pks`, `.pkb`, …), APEX exports (`f<app>.sql`), a
data-dictionary CSV (`OWNER, TABLE_NAME, COLUMN_NAME, DATA_TYPE, DATA_LENGTH, NULLABLE,
COMMENTS`) and system documents.

**This repository is public. Never commit real schema files.** `.gitignore` keeps this
folder's contents and the generated snapshot out of git.

## Three ways the skills get the schema
1. **Attach** the files (or a zip of `D:\SKM_SCHEMA`) to the conversation or Claude
   Project. Each skill indexes them on the fly with `scripts/build_schema_index.py`.
2. **Claude Code / Claude Desktop on the workstation:** the skills read `D:\SKM_SCHEMA`
   (or the folder in `SKMCH_SCHEMA_DIR`).
3. **Built-in snapshot (private upload only):** build it into the system-context skill
   and upload that `.skill` to your organization, not to GitHub:
   ```bash
   python shared/scripts/build_schema_index.py D:\SKM_SCHEMA --zip-src
   python scripts/package_skills.py
   ```
   Remove passwords, DB links with credentials and server names from the exports first.
