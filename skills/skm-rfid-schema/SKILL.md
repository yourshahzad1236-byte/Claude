---
name: skm-rfid-schema
description: "RFID Oracle schema of the SKM database: RFID/attendance machines, attendance records, machine access rights and door logs. Use for any question, SQL, PL/SQL or change involving RFID.* tables (43), views (15), packages (15) - columns, keys, relationships, comments."
---

# RFID schema

RFID/attendance machines, attendance records, machine access rights and door logs.

**Counts:** 43 tables, 15 views, 15 packages, 4 standalone procedures/functions, 5 sequences, 31 synonyms.

## References (read only what you need)
- `references/tables.md` - every table: columns, types, nullability, column comments, PK/UK/FK/CHECK, indexes, triggers. **Search it by `## RFID.TABLE_NAME`.**
- `references/views.md` - view definitions.
- `references/code-objects.md` - package specs, procedure/function headers, sequences.
- `references/synonyms.md` - synonym -> target mapping (many synonyms point at *_AUDIT schemas and are used by delete-audit triggers).

## Conventions
- Standard audit columns on nearly every table: `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_USER_ID, ORIGINAL_TERMINAL, ORIGINAL_TRN_DATE`.
- Multi-location columns: `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` (location where the record was first created).
- Insert/update/delete triggers fill the audit columns and copy deleted rows to audit tables through `SYN_*` synonyms - do not set audit columns manually.
- Flag columns are usually `CHAR/VARCHAR2(1)` with `'Y'/'N'` (e.g. `ACTIVE`).
- Cross-schema FKs from this schema point to: DEFINITIONS (4 FKs), HRD (1 FKs), SECURITY (1 FKs).

## Rules
- Use only tables/columns that exist in `references/tables.md`; never guess names.
- Qualify objects with the schema (`RFID.TABLE`).
- For joins across schemas load the master skill `skm-schema-master` and the other schema skill.

## Table index
- `ATTENDANCE`
- `ATTENDANCE_EMPLOYEE`
- `ATTENDANCE_INCORRECT` - This table is used to store failed insertions of RFID.RFID_ATTENDANCE table, mainly due to incorrect date and time.
- `DEPT_WISE_DESIG_ACCESS`
- `MACHINE_TYPE`
- `RFID_CATEGORY`
- `RFID_MACHINES`
- `MACHINE_COMPLETE_DEPARTMENT`
- `MACHINE_WISE_COUNTER`
- `MACHINE_WISE_EMPLOYEE`
- `RFID_ACCESS_DEPARTMENT`
- `RFID_ACCESS_SYNC_LOG`
- `RFID_ACL_ADMIN`
- `RFID_CARD_TYPE`
- `RFID_CARDS`
- `RFID_CARDS_ACS`
- `RFID_CARD_CATEGORY_ACS`
- `RFID_CARD_ISSUE_ACS`
- `RFID_CARD_ISSUE_RECORD`
- `RFID_CATEGORY_DEPARTMENTS`
- `RFID_CATEGORY_MACHINES`
- `RFID_CATEGORY_MACHINES_ACS`
- `RFID_CATEGORY_TIMERANGE_ACS`
- `RFID_CONFIDENTIAL_Q`
- `RFID_CONFIDENTIAL_Q_HIS`
- `RFID_CONFI_MACHINE_RIGHTS`
- `RFID_DATA_TRANSFER`
- `RFID_DEFAULT_ACCESS`
- `RFID_DELETED_ACCESS_AUDIT`
- `RFID_DEPT_GENERAL_ACCESS`
- `RFID_DESIG_WISE_SP_ACCESS`
- `RFID_DOORS_LOG` - This table is used to log door status which are opened manually.
- `RFID_EMP_WISE_SP_ACCESS`
- `RFID_MACHINES_DATA`
- `RFID_MACHINE_CATEGORY_ACS`
- `RFID_MACHINE_COMMAND`
- `RFID_MACHINE_TIMESTAMP`
- `RFID_MACHIN_IDENTIFIER_MAPPING`
- `SECTION_WISE_ATTENDANCE`
- `TEMP_CARD_SETUP`
- `TEMP_RFID_REGISTERED_USERS` - This table will be used to retrieve registered users of RFID machines on temporary basis. So that fingerprints and RFId cards can be mapped to original users later on. Data in this table is temporary and can be removed if required.
- `TMP_SELECTED_MACHINES_PR`
- `TRAINING_ATTENDANCE_STG`
