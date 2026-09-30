# CLAUDE.md

## Oracle SQL / PL/SQL work

For any Oracle SQL or PL/SQL task (writing, reviewing, or debugging packages, procedures, functions, cursors, triggers, queries, tuning), invoke the `anthropic-skills:oracle-developer` skill FIRST, before writing any code. Read the relevant guides it lists (e.g. cursors, package design, error handling) and follow them.

Conventions from that skill to apply by default:
- Naming: `p_` parameters, `l_` locals, `g_` package globals, `c_` cursors, `r_` loop records.
- Anchor variables with `%TYPE` / `%ROWTYPE`.
- Prefer cursor FOR loops; close explicit cursors and REF CURSORs (check `%ISOPEN` in handlers).
- Never use `WHEN OTHERS THEN NULL`; log and re-raise.
