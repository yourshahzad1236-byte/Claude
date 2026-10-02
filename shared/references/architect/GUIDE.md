<!-- SKMCH Architect standards. The four guides in this folder come from the organization's
Architect_Skill set. Edit them in shared/references/architect/ (never the copies inside skills),
then run scripts/package_skills.py. -->
# Architect standards: data modeling, ERD, partitioning, tablespaces

Use these guides for every data-design decision in an SRS review or a design doc/RFC.
Read only the guide(s) that match the decision, and only the sections you need
(`grep -n "^## " <file>` lists them).

| Decision | Read |
|---|---|
| New entity or table, relationships, cardinality, M:N junction tables, self-referencing hierarchies | `erd-design.md` §1–2 |
| Normalization check (1NF–BCNF), repeating groups, CSV-in-a-column, derived values | `erd-design.md` §3, §7 |
| Keys (sequence vs identity), deferrable constraints, virtual and invisible columns | `erd-design.md` §5 |
| OLTP vs reporting/DW model, star/snowflake, ODS, slowly changing dimensions (history) | `data-modeling.md` §2–7 |
| Data types, PCTFREE/INITRANS, compression | `data-modeling.md` §8 |
| Sensitive data (patient/employee identifiers), least privilege, VPD, FGA, encryption | `data-modeling.md` "Security Considerations" |
| Large or fast-growing table (log, history, attendance, transactions): partition or not, which type, local vs global indexes | `partitioning-strategy.md` §8 first, then §1–6 |
| Archive/purge strategy, rolling windows | `partitioning-strategy.md` §7 |
| Which tablespace, LOB placement, sizing, growth estimate | `tablespace-design.md` §5–6, §9 |

## SKMCH rules that override the generic guides

The guides are generic Oracle advice. At SKMCH these rules win:

1. **Names:** HRD naming standards (`hrd-naming-standards.md`) decide all object names
   (tables, constraints, indexes, sequences, triggers, views). Ignore the naming tables in
   `erd-design.md` §4 where they differ. Do keep its reserved-word list: never use
   reserved words as column names.
2. **Existing objects are not remodelled.** Don't propose renaming, re-keying or
   re-normalizing existing tables unless the SRS requires it. Extend them, and record
   any legacy design weakness as a risk or follow-up, not as a change.
3. **Follow the conventions already in the schema.** Check the schema files first:
   - **Tablespace:** put new tables and indexes in the tablespace the schema already
     uses (HRD → `HR`, PAYROLL → `PAYROLL`, REGISTRATION → `REGISTRATION`, DEFINITIONS →
     `DEFINITIONS`, RFID → `RFID`, TRAINING → `TRAINING`, HIS → `REGISTRATION`). Never
     `SYSTEM`, `SYSAUX` or `USERS`. Propose a new tablespace only with a reason, as a
     DBA action in the deployment plan.
   - **Audit and multi-location columns:** existing SKMCH tables carry `USER_ID`,
     `TERMINAL`, `TRN_DATE`, `ORIGINAL_USER_ID`, `ORIGINAL_TERMINAL`, `ORIGINAL_TRN_DATE`,
     `ORG_ID`, `ZON_ID`, `LOC_ID`, `WS_SYNC_DATE`, filled by `<TABLE>_INS/_UPD/_DEL`
     triggers. New tables follow the same pattern as their neighbours unless the SRS
     says otherwise. Say which pattern you copied, and from which table.
   - **Keys:** check how similar tables in the same schema generate their keys (their
     triggers and packages). For new surrogate keys, use a `_SEQ` sequence per HRD
     standards. Use identity columns only if the architect agrees.
   - **Partitioning:** some tables are already partitioned (HIS, REGISTRATION, HRD,
     TRAINING and others). Follow the existing pattern for similar tables. Partitioning
     needs the Enterprise Edition Partitioning option, so note that in the design.
4. **Oracle 19c baseline.** Anything that needs 21c/23ai/26ai must be marked as such.
   Hybrid Columnar Compression (`COMPRESS FOR QUERY HIGH`) needs Exadata/ZFS/ODA: don't
   propose it unless the platform is confirmed. Advanced Compression, partitioning,
   Diagnostics/Tuning packs and TDE are licensed options: flag each one as an
   assumption to confirm.
5. **No live database.** SKMCH staff have no direct DB access. Size estimates come from
   the SRS volumes and the schema files, not from `DBA_` views. Put any monitoring query
   in the deployment/verification plan for the DBA to run.
6. **Patient and employee data.** Treat MRNO, CNIC/NIC, names, phone numbers, diagnosis
   and salary as sensitive (PHI/PII): least privilege, no sensitive values in logs or
   error messages, audit/history per the NFRs.
7. **Every design decision cites its reason**, and the guide section when one applies
   (e.g. "monthly interval partitioning on CHECK_TIME, per partitioning-strategy.md §8:
   about 12M rows/year, queries filter by date").
