<!-- Organization skill `oracle-developer`, bundled into skmch-dev-implement so the developer skill always has it. Replace this folder with a newer copy of the skill when it is updated (SKILL.md becomes GUIDE.md, plsql/plsql/ becomes plsql/, and so on). -->
# Oracle Developer

Standards and reference guides for writing production Oracle SQL and PL/SQL. The code this skill supports runs in enterprise systems with sensitive, regulated data, many concurrent users and long service lives, so correctness, security and maintainability matter more than brevity.

## How to use this skill

1. **Apply the core standards below to every answer**, even quick ones. They are short on purpose and cover the mistakes that cause most production incidents.
2. **Open the reference guides that match the task** using the routing table. Read only the relevant sections (each guide has a clear heading structure; `grep -n "^## "` shows it). One to three guides is usually enough; there is no need to read all of them.
3. **Check the version.** Default to code that compiles on 19c. If the user is on 23ai/26ai, or asks for newer features, use them and say they need 23ai+. Each guide ends with an "Oracle Version Notes (19c vs 26ai)" section for this.

## Core standards

**Set-based first.** Solve it in one SQL statement where possible (MERGE, INSERT…SELECT, analytic functions). Each switch between the PL/SQL and SQL engines costs time, so row-by-row loops over large sets are the most common performance bug. When procedural processing is genuinely needed, use `BULK COLLECT … LIMIT` (100–1000) with `FORALL … SAVE EXCEPTIONS`, never an unbounded BULK COLLECT, which can exhaust PGA.

**Bind variables, always.** Never concatenate user input or item values into SQL. Binds prevent SQL injection and let Oracle reuse parsed cursors, avoiding hard-parse storms under load. When an identifier (table or column name) must be dynamic, validate it with `DBMS_ASSERT` or a data-dictionary whitelist. In APEX, reference page items as `:P1_ITEM` binds, never `&P1_ITEM.` substitution inside SQL or PL/SQL.

**Errors are never swallowed.** No `WHEN OTHERS THEN NULL`, and no `WHEN OTHERS` without `RAISE` or `RAISE_APPLICATION_ERROR`. Log with an autonomous-transaction logger that captures `DBMS_UTILITY.FORMAT_ERROR_STACK` and `FORMAT_ERROR_BACKTRACE`, then re-raise. Use application error codes in the -20000 to -20999 range, defined as named constants. Keep sensitive data (patient, customer or personal identifiers) out of error messages and log text; log keys instead.

**Transaction control belongs to the caller.** Reusable APIs don't `COMMIT` or `ROLLBACK`; the outermost caller (a batch job, an APEX page process, a Forms commit) decides. The exception is the autonomous-transaction logger. Mid-loop commits cause ORA-01555 and leave data half-processed on failure.

**Anchor types.** Declare variables with `%TYPE` and `%ROWTYPE` so code survives column changes. Size `VARCHAR2` explicitly and compare in consistent types; implicit conversion in predicates (`WHERE varchar_col = 123`, `TO_CHAR(date_col) = …`) disables indexes. Use `TO_DATE`/`TO_TIMESTAMP` with explicit format masks.

**Handle NULL deliberately.** `= NULL` is never true; use `IS NULL`, `NVL`/`COALESCE`, and remember `NOT IN` against a subquery containing a NULL returns no rows.

**Packages over standalone units.** Group related logic in packages; keep the spec minimal (the public API) and everything else private in the body. Avoid package-level state unless it's intended, since it persists for the session and breaks in connection pools.

**Instrument production code.** Set `DBMS_APPLICATION_INFO.SET_MODULE`/`SET_ACTION` in long-running or batch code so DBAs can find it in `V$SESSION` and ASH.

**Choose AUTHID and privileges consciously.** Definer rights is the default and runs with the owner's privileges; use `AUTHID CURRENT_USER` for utility code that should respect the caller's rights. Grant EXECUTE on APIs, not direct table access.

**Triggers stay thin.** Use them for audit columns and simple integrity, not business logic, and never for cross-table cascades that callers can't see.

## Routing table

Paths are relative to this folder (`references/oracle-developer/`).

| Task | Read |
|---|---|
| Writing or reviewing a package, API design, spec/body split | `plsql/plsql-package-design.md`, `plsql/plsql-patterns.md` |
| Table API (TAPI), audit logging, pipelined functions, REF CURSOR result sets | `plsql/plsql-patterns.md` |
| Exception handling, error logging, ORA- errors raised from PL/SQL | `plsql/plsql-error-handling.md` |
| Loops over data, BULK COLLECT, FORALL, slow PL/SQL, result cache, NOCOPY | `plsql/plsql-performance.md`, `sql-dev/pl-sql-best-practices.md` |
| Collections (associative arrays, nested tables, varrays, TABLE()) | `plsql/plsql-collections.md` |
| Cursors, REF CURSORs, cursor leaks (ORA-01000) | `plsql/plsql-cursors.md` |
| Dynamic SQL, EXECUTE IMMEDIATE, DBMS_SQL | `sql-dev/dynamic-sql.md`, `sql-dev/sql-injection-avoidance.md` |
| Security review, AUTHID, privileges, injection | `plsql/plsql-security.md`, `sql-dev/sql-injection-avoidance.md` |
| Code review, naming conventions, style, complexity | `plsql/plsql-code-quality.md` |
| Debugging, tracing, DBMS_OUTPUT, tkprof, compile warnings | `plsql/plsql-debugging.md` |
| Compiler settings, conditional compilation, native compilation | `plsql/plsql-compiler-options.md` |
| Writing SQL: joins, NULLs, data types, row limiting | `sql-dev/sql-best-practices.md` |
| Analytic functions, CTEs, CONNECT BY, PIVOT, MERGE, MODEL | `sql-dev/sql-patterns.md` |
| Slow query, hints, SQL profiles, plan baselines | `sql-dev/sql-tuning.md`, `performance/explain-plan.md` |
| Reading an execution plan | `performance/explain-plan.md` |
| Which index to create, function-based or bitmap indexes | `performance/index-strategy.md` |
| Stale or missing statistics, histograms, DBMS_STATS | `performance/optimizer-stats.md` |
| Database-wide slowness, AWR report | `performance/awr-reports.md`, `performance/wait-events.md` |
| A specific session or time window was slow | `performance/ash-analysis.md`, `performance/wait-events.md` |
| SGA/PGA sizing, memory errors (ORA-04031, ORA-04036) | `performance/memory-tuning.md` |

**APEX and Forms/Reports:** there is no separate guide for these. Apply the same PL/SQL and SQL guides to code inside page processes, validations, computations, authorization schemes, Forms triggers and Report queries. Prefer moving substantial logic out of the page or form into a database package and calling it with one line, since packaged code is testable, reusable and versioned with the schema.

## What a good answer looks like

**Writing new code:** give complete code that compiles as written (package spec and body, or the full statement), with any DDL it depends on. Follow it with a short note on the key design choices, anything that needs 23ai+, and a brief way to test or verify it (a test block, or the query to confirm the plan or result).

**Reviewing code:** list findings ordered by severity (correctness and security first, then performance, then maintainability), each with the line or construct, why it matters, and the fix. Then give the corrected code.

**Tuning:** ask for or work from the actual plan (`DBMS_XPLAN.DISPLAY_CURSOR` with `ALLSTATS LAST`) rather than guessing; estimated plans hide the real row counts. State what to measure before and after the change.

When several valid approaches exist (for example a single MERGE vs. a BULK/FORALL loop, or a pipelined function vs. a REF CURSOR), briefly compare them and recommend one, with the reason.
