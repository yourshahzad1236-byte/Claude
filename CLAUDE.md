# Project context

Oracle SQL / PL/SQL project. Target version: Oracle 19c unless stated otherwise.

## Database schema (SKM)

- The schema DDL lives in `db/schema/` (DDL only, no data). Source of truth is the SKM_SCHEMA export.
- Before writing, reviewing, testing or designing anything that touches the database:
  1. Read `db/schema/README.md` for the map of tables, domains and naming conventions.
  2. Read the DDL file of every table, view or package you reference.
- Never guess table names, column names, data types, constraints or keys. If something is not in `db/schema/`, say so and ask instead of inventing it.
- If `db/schema/` is empty or missing, stop and tell the user before producing schema-dependent code.
- The real database is not available to this session. Do not ask for data. For tuning work, ask for `DBMS_XPLAN` output or row counts.

## Rules that apply to all work (any skill or none)

- Follow the `oracle-developer` skill standards for all Oracle SQL and PL/SQL.
- Reuse existing tables, constraints and packages before proposing new ones.
- Derive tests from the schema: check constraints, foreign keys, NOT NULL and unique keys.
- Keep sensitive data (personal or customer identifiers) out of code, logs and error messages.
- Keep SQL scripts under `oracle/`, and update `db/schema/` when the schema changes.
