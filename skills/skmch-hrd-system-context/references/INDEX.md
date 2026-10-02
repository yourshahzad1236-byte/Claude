# SKMCH system context index: NOT YET INDEXED

No schema snapshot is built into this copy of the skill.

1. If the user attached schema files (or a zip of `D:\SKM_SCHEMA`), index them with
   `python <skill-dir>/scripts/build_schema_index.py <files / zip> --out <temp>/schema-index --copy-src`
   and use that index.
2. In Claude Code / Claude Desktop on the SKMCH workstation, index `D:\SKM_SCHEMA` the same way.
3. Otherwise **every impact analysis must be marked PROVISIONAL**. Ask the user to attach
   the schema files.

Maintainers: run `python shared/scripts/build_schema_index.py D:\SKM_SCHEMA --copy-src`,
then `python scripts/package_skills.py`, and re-upload `dist/skmch-hrd-system-context.skill`.
