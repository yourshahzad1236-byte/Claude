# RFID schema - reference


RFID/attendance machines, attendance records, machine access rights and door logs.

**Counts:** 43 tables, 15 views, 15 packages, 4 standalone procedures/functions, 5 sequences, 31 synonyms.

## Conventions
- Standard audit columns on nearly every table: `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_USER_ID, ORIGINAL_TERMINAL, ORIGINAL_TRN_DATE`.
- Multi-location columns: `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` (location where the record was first created).
- Insert/update/delete triggers fill the audit columns and copy deleted rows to audit tables through `SYN_*` synonyms - do not set audit columns manually.
- Flag columns are usually `CHAR/VARCHAR2(1)` with `'Y'/'N'` (e.g. `ACTIVE`).
- Cross-schema FKs from this schema point to: DEFINITIONS (4 FKs), HRD (1 FKs), SECURITY (1 FKs).

## Rules
- Use only tables/columns that exist in the Tables part below; never guess names.
- Qualify objects with the schema (`RFID.TABLE`).
- For joins across schemas use the skill `skm-schema` and the other schema reference file.

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


# PART: Tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

### RFID.ATTENDANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECK_TIME | DATE | Y | Timestamp of machine when attendance marked. |
| CHECK_TYPE | VARCHAR2(20) | Y | I: Check In  O: Check Out |
| MACHINE_ID | NUMBER(5) | Y | Reffered as MACHINE_CODE in RFID.RFID_ATTENDANCE |
| VERIFICATION_MODE | NUMBER(5) | Y | Cardswipe/Password/Biometric |
| TRANS_DATE | DATE default SYSDATE | Y | Default insertion Date |
| LOCATION_ID | VARCHAR2(3) | Y | Referred to LOC_ID in RFID.RFID_MACHINES |
| IS_EPARKING | CHAR(1) | Y |  |
| REASON | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **Triggers**: `ATTENDANCE_INS_CS` (after insert), `CHECK_DATE_TIME` (before insert), `RFID_ATTENDANCE_INSERT` (after insert), `RFID_ATTENDANCE_INSERT_EPARK` (after insert), `RFID_ATTENDANCE_INSERT_PAT` (after insert), `RFID_CONFIDENTIAL_QUEUE_INSERT` (after insert)

### RFID.ATTENDANCE_EMPLOYEE

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECK_TIME | DATE | Y |  |
| MACHINE_IDENTIFIER | NUMBER(10) | Y |  |
| MACHINE_ID | NUMBER(5) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REASON | VARCHAR2(4000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| RFID_CODE | VARCHAR2(50) | Y |  |
| SERIAL_NO_FOR_CARD_SWIPE | NUMBER | Y | This column will be used in rfid.attendance_employee table to track record of attendance |
| MACHINE_DEFAULT_CHECK_IN_OUT | CHAR(1) | Y |  |
| SR_NO | VARCHAR2(15) | Y |  |

- **PK** `ATTENDANCE_EMPLOYEE_PK`: SR_NO
- **UK** `ATTENDANCE_EMPLOYEE_UK`: CHECK_TIME, MACHINE_IDENTIFIER, MACHINE_ID
- **Triggers**: `ATTENDANCE_EMPLOYEE_DEL` (after delete), `ATTENDANCE_EMPLOYEE_INS` (before insert), `ATTENDANCE_EMPLOYEE_UPD` (before update), `ATTENDANCE_EMP_SEQ_INSERT` (before insert), `TRAINING_ATTENDANCE_STG_INSERT` (after insert)

### RFID.ATTENDANCE_INCORRECT
This table is used to store failed insertions of RFID.RFID_ATTENDANCE table, mainly due to incorrect date and time.

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECK_TIME | DATE | N |  |
| CHECK_TYPE | VARCHAR2(20) | N |  |
| MACHINE_ID | NUMBER(5) | N | Reffered to MACHINE_CODE in RFID.RFID_MACHINES |
| VERIFICATION_MODE | NUMBER(5) | Y |  |
| TRANS_DATE | DATE default SYSDATE | N |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y | Referred to LOC_ID in RFID.RFID_MACHINES |
| IS_EPARKING | CHAR(1) | Y |  |


### RFID.DEPT_WISE_DESIG_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEP_WISE_DESIG_ACCESS`: DEPARTMENT_ID, DESIGNATION_ID
- **FK** `FK_DEP_WISE_DESIG_ID`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **Triggers**: `DEPT_WISE_DESIG_ACCESS_DEL` (after delete), `DEPT_WISE_DESIG_ACCESS_INS` (before insert), `DEPT_WISE_DESIG_ACCESS_UPD` (before update)

### RFID.MACHINE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_TYPE | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_MACHINE_TYPE`: MACHINE_TYPE

### RFID.RFID_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| IS_DEFAULT | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_RFID_CATEGORY`: CATEGORY_ID
- **Triggers**: `RFID_CATEGORY_DEL` (after delete), `RFID_CATEGORY_INS` (before insert), `RFID_CATEGORY_UPD` (before update)

### RFID.RFID_MACHINES

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(250) | N |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| MACHINE_CODE | VARCHAR2(10) | Y |  |
| IP_ADDRESS | VARCHAR2(15) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| PORT_NO | NUMBER default 4370 | N |  |
| CATEGORY_ID | NUMBER(5) | Y |  |
| STATUS | CHAR(1) default 'Y' | Y | Y: Must verify machine availability on network, N: Do not verify machine availability on network. |
| STATUS_DATE | DATE | Y |  |
| MACHINE_TYPE | VARCHAR2(5) default 'BW' | N | Values could be as follows BW/TFT/IFACE depending upon machine specs |
| MACHINE_ON_OF | CHAR(1) default 'Y' | Y | 'Y' IS ON 'N' IS OFF |
| IS_SELECT | CHAR(1) default 'N' | Y |  |
| IS_CONFIDENTIAL | CHAR(1) default 'N' | Y |  |
| CAPTURE_PICTURE | CHAR(1) default 'N' | N | Device can capture and save pictures |
| CAPTURE_FINGERPRINT | CHAR(1) default 'N' | N | Device can capture and save fingerprints |
| MACHINE_DIGIT_LIMIT | NUMBER(2) | Y |  |
| RFID_CODE_REQUIRED | CHAR(1) default 'Y' | Y |  |
| COMMUNICATION_PASSWORD | VARCHAR2(6) | Y | Password used to connect RFID Machine |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y | THIS COLUMN CONTAINS THE LOCATION WHERE THE MACHINE IS PHYSICALLY LOCATED |
| MARK_ATTENDANCE | CHAR(1) | Y |  |
| MACHINE_LOCATION_ID | VARCHAR2(3) | Y |  |
| CAPTURE_IRIS | CHAR(1) default 'N' | Y | Device can capture and save IRIS features. |
| CAPTURE_FACE | CHAR(1) default 'N' | Y | Device can capture and save face features. |
| MACHINE_CATEGORY | CHAR(1) | Y |  |
| ATTENDANCE_ALLOWED | CHAR(1) | Y |  |
| DEFAULT_CHECK_IN_OUT | CHAR(1) | Y | This column use for default value of the machine in/out. |
| GENDER_ONLY | NUMBER(1) | Y | This column will be use to grant gender wise access on rfid machine null will be for all gender |
| TRAINING_ATTENDANCE_MARK | CHAR(1) default 'N' | Y |  |
| DEVICE_SERIAL_NUM | VARCHAR2(30) | Y |  |
| CAPTURE_PALM | CHAR(1) default 'N' | Y | Device can capture and save palm features. |
| CONNECTION_STATUS | NUMBER(1) default 0 | N |  |

- **PK** `PK_RFID_MACHINE`: MACHINE_ID
- **FK** `FK_RFID_MACHINES_1`: (CATEGORY_ID) -> RFID.RFID_CATEGORY(CATEGORY_ID) [disabled]
- **FK** `FK_RFID_MACHINES_2`: (MACHINE_TYPE) -> RFID.MACHINE_TYPE(MACHINE_TYPE) [disabled]
- **FK** `FK_RFID_MACHINE_3`: (GENDER_ONLY) -> DEFINITIONS.SEX(SEX_ID)
- **CHECK** `CHK_RFID_MACHINES_CONN_STATUS`: CONNECTION_STATUS IN (0, 1)
- **CHECK** `CK_RFID_MACHINE`: ACTIVE IN ('Y','N')
- **Triggers**: `RFID_MACHINES_DEL` (after delete), `RFID_MACHINES_INS` (before insert), `RFID_MACHINES_UPD` (before update), `RFID_SUPER_CARD_MACHINE_INS` (after insert or update or delete)

### RFID.MACHINE_COMPLETE_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| IS_ATTENDANCE_MARK | CHAR(1) | Y |  |

- **PK** `PK_MACHINE_DEPT`: MACHINE_ID, DEPARTMENT_ID
- **FK** `FK_MACHINE_DEPT_1`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **FK** `FK_MACHINE_DEPT_2`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **CHECK** `CK_MACHINE_DEPT_1`: ACTIVE IN ('Y','N')
- **Triggers**: `MAC_COMP_DEPARTMENT_DEL` (after delete), `MAC_COMP_DEPARTMENT_INS` (before insert), `MAC_COMP_DEPARTMENT_UPD` (before update)

### RFID.MACHINE_WISE_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| COUNTER | NUMBER(8) default 1 | Y |  |
| MAXIMUM_COUNTER | NUMBER(8) | Y |  |

- **PK** `PK_MACHINE_ID`: MACHINE_ID
- **Triggers**: `MACHINE_WISE_COUNTER_DEL` (after delete), `MACHINE_WISE_COUNTER_INS` (before insert), `MACHINE_WISE_COUNTER_UPD` (before update)

### RFID.MACHINE_WISE_EMPLOYEE

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ENTRY_TYPE | VARCHAR2(1) default 'I' | Y |  |
| RFID_ATTENDANCE_TYPE | CHAR(1) | Y | 'T' for thumb scan, 'R' for rfid attendance, and 'A' For all |
| MARK_ATTENDANCE | CHAR(1) default 'Y' | Y |  |
| MACHINE_ACCESS_TYPE | VARCHAR2(3) default 'E' | Y | 'E' for employee, 'D' for Designation category wise, 'T' Department Wise 'DAA' DEFAULT ACCES 'DGA' department wise acess, 'DSA' designation wise special access |
| OBJECT_CODE | VARCHAR2(15) | Y |  |
| ACCESS_GRANT_EVENT | VARCHAR2(40) | Y |  |

- **PK** `PK_MACHINE_EMP`: MACHINE_ID, MRNO
- **FK** `FK_MACHINE_EMP_1`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **FK** `FK_MACHINE_EMP_2`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **CHECK** `CK_MACHINE_EMP_1`: ACTIVE IN ('Y','N')
- **Triggers**: `MACHINE_WISE_EMPLOYEE_DEL` (after delete), `MACHINE_WISE_EMPLOYEE_INS` (before insert), `MACHINE_WISE_EMPLOYEE_UPD` (before update)

### RFID.RFID_ACCESS_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| IS_REFRESH | CHAR(1) | Y |  |

- **PK** `PK_RFID_ACCESS_DEPARTMENT`: DEPARTMENT_ID
- **FK** `FK_RFID_ACCESS_DEPARTMENT`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **Triggers**: `RFID_ACCESS_DEPARTMENT_DEL` (after delete), `RFID_ACCESS_DEPARTMENT_INS` (before insert), `RFID_ACCESS_DEPARTMENT_UPD` (before update)

### RFID.RFID_ACCESS_SYNC_LOG

| Column | Type | Null | Comment |
|---|---|---|---|
| LOG_ID | NUMBER | N |  |
| RUN_ID | NUMBER | N |  |
| EVENT_TS | DATE default SYSDATE | N |  |
| EVENT_BY | VARCHAR2(30) default USER | N |  |
| EVENT_TYPE | VARCHAR2(50) | N |  |
| EVENT_SOURCE | VARCHAR2(50) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| MACHINE_ID | VARCHAR2(5) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| SEX_ID | NUMBER | Y |  |
| RFID_SUPER_CARD | VARCHAR2(1) | Y |  |
| MACHINE_ACCESS_TYPE | VARCHAR2(10) | Y |  |
| ACCESS_GRANT_EVENT | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| OLD_ROW_JSON | CLOB | Y |  |
| NEW_ROW_JSON | CLOB | Y |  |

_No standard audit columns._


### RFID.RFID_ACL_ADMIN

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PRIVILEGE_LEVEL | CHAR(1) default '2' | N | 0  Common User, 1  Enroller/Registrar , 2  Admin, 3  Super Administrator |
| USER_PASSWORD | VARCHAR2(500) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_RFID_ACL_ADMIN`: MRNO, PRIVILEGE_LEVEL
- **FK** `FK_RFID_ACL_ADMIN_1`: (MRNO) -> SECURITY.USERS(MRNO)
- **Triggers**: `RFID_ACL_ADMIN_DEL` (after delete), `RFID_ACL_ADMIN_INS` (before insert), `RFID_ACL_ADMIN_UPD` (before update)

### RFID.RFID_CARD_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_TYPE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_RFID_CARD_TYPE`: CARD_TYPE_ID
- **Triggers**: `RFID_CARD_TYPE_DEL` (after delete), `RFID_CARD_TYPE_INS` (before insert), `RFID_CARD_TYPE_UPD` (before update)

### RFID.RFID_CARDS

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_TYPE_ID | NUMBER(4) | Y |  |
| RFID_CARD_NO | VARCHAR2(10) | N |  |
| CATEGORY_ID | NUMBER(5) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CARD_DESCRIPTION | VARCHAR2(50) | Y |  |

- **PK** `PK_RFID_CARDS`: RFID_CARD_NO
- **FK** `FK_RFID_CARDS`: (CARD_TYPE_ID) -> RFID.RFID_CARD_TYPE(CARD_TYPE_ID) [disabled]
- **Triggers**: `RFID_CARDS_DEL` (after delete), `RFID_CARDS_INS` (before insert), `RFID_CARDS_UPD` (before update)

### RFID.RFID_CARDS_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| RFID_CARD_NO | VARCHAR2(30) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| CARD_DESCRIPTION | VARCHAR2(50) | Y |  |

- **PK** `PK_CARDS_01`: RFID_CARD_NO
- **Triggers**: `RFID_CARDS_ACS_DEL` (after delete), `RFID_CARDS_ACS_INS` (before insert), `RFID_CARDS_ACS_UPD` (before update)

### RFID.RFID_CARD_CATEGORY_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_CATEGORY_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| TIME_LIMIT | NUMBER(4) default 0 | Y | RFID Card has the time limit and will be stored in this column |
| TIME_LIMIT_UNIT | CHAR(1) default 'H' | Y | H for Hours, M for Minutes,D for Days,S for Months, Y for Years,  N for No limit |
| MAXIMUM_COUNT | NUMBER(4) | Y | This column contains maximum number of visitors/attendents/guests allowed for each patients/employees |
| REMARKS | VARCHAR2(4000) | Y |  |
| TIME_RANGE_REQ | CHAR(1) default 'N' | Y |  |
| IS_EXTEND_ALLOWED | CHAR(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | N |  |

- **PK** `PK_RFID_CARD_CATEGORY_01`: CARD_CATEGORY_ID, LOCATION_ID
- **UK** `UK_RFID_CARD_CATEGORY_01`: DESCRIPTION
- **Triggers**: `RFID_CARD_CATEGORY_ACS_DEL` (after delete), `RFID_CARD_CATEGORY_ACS_INS` (before insert), `RFID_CARD_CATEGORY_ACS_UPD` (before update)

### RFID.RFID_CARD_ISSUE_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR | NUMBER(20) | N |  |
| RFID_CARD_NO | VARCHAR2(30) | N |  |
| NAME | VARCHAR2(255) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| ISSUE_DATE | DATE | N |  |
| RECEIVE_DATE | DATE | Y |  |
| RETURN | CHAR(1) default 'N' | Y |  |
| CARD_CATEGORY_ID | NUMBER(4) | N |  |
| ISSUED_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| NIC | VARCHAR2(14) | Y |  |
| RELATION_ID | VARCHAR2(6) | Y |  |
| ADDRESS | VARCHAR2(400) | Y |  |
| RETURN_DATE | DATE | Y |  |
| RIGHTS_STATUS | CHAR(1) default 'W' | Y | W for waiting for rights, G for rights granted, R for rights revoked |
| MACHINE_CATEGORY_ID | NUMBER(6) | Y |  |
| RIGHTS_ISSUE_DATE | DATE | Y |  |
| RIGHTS_REVOKE_DATE | DATE | Y |  |
| IS_EXTENDED | CHAR(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | N |  |
| CARD_DESC | VARCHAR2(1000) | Y |  |
| CONTACT_NO | VARCHAR2(500) | Y |  |
| WARD_ID | VARCHAR2(7) | Y |  |
| BUILDING_BLOCK_FLOOR_ID | VARCHAR2(10) | Y |  |
| BUILDING_BLOCK_ID | VARCHAR2(7) | Y |  |
| CARD_VALID_TILL | DATE | Y |  |
| SERIAL_NO_FOR_CARD_SWIPE | NUMBER | Y | This column will be used in rfid.attendance_employee table to track record of attendance |

- **PK** `PK_RFID_CARD_ISSUE_01`: SR, CARD_CATEGORY_ID, MRNO, LOCATION_ID
- **Triggers**: `RFID_CARD_ISSUE_ACS_DEL` (after delete), `RFID_CARD_ISSUE_ACS_INS` (before insert), `RFID_CARD_ISSUE_ACS_UPD` (before update)

### RFID.RFID_CARD_ISSUE_RECORD

| Column | Type | Null | Comment |
|---|---|---|---|
| SR | NUMBER(6) | N |  |
| RFID_CARD_NO | VARCHAR2(10) | N |  |
| NAME | VARCHAR2(255) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| ISSUE_DATE | DATE | N |  |
| RECEIVE_DATE | DATE | Y |  |
| RETURN | CHAR(1) default 'N' | N |  |
| CARD_TYPE_ID | NUMBER(4) | N |  |
| ISSUED_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| NIC | VARCHAR2(14) | Y |  |

- **PK** `PK_RFID_CARD_ISSUE_RECORD`: SR, CARD_TYPE_ID
- **FK** `CARD_NO`: (RFID_CARD_NO) -> RFID.RFID_CARDS(RFID_CARD_NO) [disabled]

### RFID.RFID_CATEGORY_DEPARTMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |

- **PK** `RFID_CATEGORY_DEPARTMENTS`: CATEGORY_ID, DEPARTMENT_ID
- **Triggers**: `RFID_CATEGORY_DEPARTMENTS_DEL` (after delete), `RFID_CATEGORY_DEPARTMENTS_INS` (before insert), `RFID_CATEGORY_DEPARTMENTS_UPD` (before update)

### RFID.RFID_CATEGORY_MACHINES

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_RFID_CATEGORY_MACHINES`: MACHINE_ID, CATEGORY_ID
- **FK** `FK_RFID_CATEGORY_MACHINES`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **FK** `FK_RFID_CATEGORY_MACHINES_1`: (CATEGORY_ID) -> RFID.RFID_CATEGORY(CATEGORY_ID) [disabled]
- **Triggers**: `RFID_CATEGORY_MACHINES_DEL` (after delete), `RFID_CATEGORY_MACHINES_INS` (before insert), `RFID_CATEGORY_MACHINES_UPD` (before update)

### RFID.RFID_CATEGORY_MACHINES_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y |  |

- **PK** `PK_MAC_CAT_01`: MACHINE_ID, CATEGORY_ID
- **Triggers**: `RFID_CATEGORY_MACHINES_ACS_DEL` (after delete), `RFID_CATEGORY_MACHINES_ACS_INS` (before insert), `RFID_CATEGORY_MACHINES_ACS_UPD` (before update)

### RFID.RFID_CATEGORY_TIMERANGE_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_CATEGORY_ID | NUMBER(4) | N |  |
| UPPER_TIME_LIMIT | VARCHAR2(4) | Y |  |
| LOWER_TIME_LIMIT | VARCHAR2(4) | Y |  |
| SR_NO | NUMBER(4) | N |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y |  |

- **PK** `PK_RFID_TIM_RANGE_01`: CARD_CATEGORY_ID, SR_NO
- **Triggers**: `RFID_CAT_TR_ACS_DEL` (after delete), `RFID_CAT_TR_ACS_INS` (before insert), `RFID_CAT_TR_ACS_UPD` (before update)

### RFID.RFID_CONFIDENTIAL_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECK_TIME | DATE | N |  |
| MACHINE_IDENTIFIER | NUMBER(10) | N |  |
| MACHINE_ID | NUMBER(5) | N |  |
| ENTRY_DATE | DATE | Y |  |
| REASON | VARCHAR2(4000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| SR_NO | NUMBER | Y |  |

- **PK** `RFID_CONFIDENTIAL_Q_PK`: CHECK_TIME, MACHINE_IDENTIFIER, MACHINE_ID
- **Triggers**: `RFID_CONFIDENTIAL_Q_DEL` (after delete), `RFID_CONFIDENTIAL_Q_DELETE_HISTORY` (after delete), `RFID_CONFIDENTIAL_Q_INS` (before insert), `RFID_CONFIDENTIAL_Q_UPD` (before update)

### RFID.RFID_CONFIDENTIAL_Q_HIS

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECK_TIME | DATE | Y |  |
| MACHINE_IDENTIFIER | NUMBER(10) | Y |  |
| MACHINE_ID | NUMBER(5) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REASON | VARCHAR2(4000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| SIGNED_BY | VARCHAR2(14) | Y |  |
| SIGNED_DATE | DATE | Y |  |

_No standard audit columns._


### RFID.RFID_CONFI_MACHINE_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CONFI_MACHI_RIGHTS`: MRNO, MACHINE_ID
- **Triggers**: `RFID_CONFI_MACHINE_RIGHTS_DEL` (after delete), `RFID_CONFI_MACHINE_RIGHTS_INS` (before insert), `RFID_CONFI_MACHINE_RIGHTS_UPD` (before update)

### RFID.RFID_DATA_TRANSFER

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_CODE | VARCHAR2(10) | N |  |
| IP_ADDRESS | VARCHAR2(15) | N |  |
| PORT_NO | NUMBER | N |  |
| MACHINE_IDENTIFIER | VARCHAR2(9) | N |  |
| USER_NAME | VARCHAR2(255) | Y |  |
| USER_PASSWORD | VARCHAR2(255) | Y |  |
| PRIVILEGE | NUMBER(1) | N |  |
| ENABLED | CHAR(1) default 'Y' | N |  |
| RFID_CARD_NO | VARCHAR2(30) | Y |  |
| NO_OF_TRIES | NUMBER(3) default 0 | Y |  |
| ALERT_TEXT | VARCHAR2(2000) | Y |  |
| COMPLETE_MRNO | VARCHAR2(14) | Y |  |
| RFID_ATTENDANCE_TYPE | CHAR(1) default 'A' | Y | 'T' for thumb scan, 'R' for rfid attendance, and 'A' For all' |

- **PK** `PK_RFID_DATA_TRANSFER`: MACHINE_CODE, MACHINE_IDENTIFIER, PRIVILEGE, ENABLED
- **Triggers**: `RFID_DATA_TRANSFER_DEL` (after delete), `RFID_DATA_TRANSFER_INS` (before insert), `RFID_DATA_TRANSFER_UPD` (before update)

### RFID.RFID_DEFAULT_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_REFRESH | CHAR(1) | Y |  |

- **PK** `PK_RFID_DEFAULT_ACCESS`: MACHINE_ID, LOCATION_ID
- **FK** `FK_RFID_DEFAULT_ACCESS_MACHINE_ID`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **Triggers**: `RFID_DEFAULT_ACCESS_DEL` (after delete), `RFID_DEFAULT_ACCESS_INS` (before insert), `RFID_DEFAULT_ACCESS_UPD` (before update)

### RFID.RFID_DELETED_ACCESS_AUDIT

| Column | Type | Null | Comment |
|---|---|---|---|
| AUDIT_ID | NUMBER | N |  |
| RUN_ID | NUMBER | N |  |
| SOURCE_TABLE | VARCHAR2(50) | N |  |
| REASON_CODE | VARCHAR2(50) | N |  |
| REASON_TEXT | VARCHAR2(500) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(20) | Y |  |
| MRNO | VARCHAR2(30) | Y |  |
| DEPARTMENT_ID | VARCHAR2(30) | Y |  |
| DESIGNATION_ID | VARCHAR2(30) | Y |  |
| MACHINE_ID | NUMBER | Y |  |
| DELETED_ON | DATE default SYSDATE | N |  |
| DELETED_BY | VARCHAR2(100) default USER | N |  |
| ROW_DATA_JSON | CLOB | Y |  |

_No standard audit columns._


### RFID.RFID_DEPT_GENERAL_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEPT_WISE_GENERAL_ACCESS`: DEPARTMENT_ID, MACHINE_ID
- **FK** `FK_DEPT_WISE_GENERAL_MACHINE_ID`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **Triggers**: `RFID_DEPT_GENERAL_ACCESS_DEL` (after delete), `RFID_DEPT_GENERAL_ACCESS_INS` (before insert), `RFID_DEPT_GENERAL_ACCESS_UPD` (before update)

### RFID.RFID_DESIG_WISE_SP_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |

- **PK** `PK_RFID_DESIG_WISE_ACCESS`: DESIGNATION_ID, MACHINE_ID, DEPARTMENT_ID
- **FK** `FK_RFID_DEPT_DESIGN`: (DEPARTMENT_ID, DESIGNATION_ID) -> RFID.DEPT_WISE_DESIG_ACCESS(DEPARTMENT_ID, DESIGNATION_ID)
- **Triggers**: `RFID_DESIG_WISE_SP_ACCESS_DEL` (after delete), `RFID_DESIG_WISE_SP_ACCESS_INS` (before insert), `RFID_DESIG_WISE_SP_ACCESS_UPD` (before update)

### RFID.RFID_DOORS_LOG
This table is used to log door status which are opened manually.

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N | Machine ID from RFID.RFID_MACHINES |
| DOOR_STATUS | CHAR(1) default 'O' | N | O: Open \| C: Close |
| TRANS_DATE | DATE default SYSDATE | N | Date of transaction |
| EMPLOYEE_CODE | VARCHAR2(15) | Y |  |
| TERMINAL_NAME | VARCHAR2(30) | N | Terminal name  which initiates the door opening request. |
| OS_USER_NAME | VARCHAR2(30) | Y | Current logged in user who initiates the request. |
| MACHINE_LOC | VARCHAR2(3) | Y | RFID Machine Location ID |

_No standard audit columns._

- **FK** `FK_RFID_DOORS_LOG_1`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)

### RFID.RFID_EMP_WISE_SP_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RFID_EMP_WISE_SP_ACCESS`: MRNO, MACHINE_ID
- **Triggers**: `RFID_EMP_WISE_SP_ACCESS_DEL` (after delete), `RFID_EMP_WISE_SP_ACCESS_INS` (before insert), `RFID_EMP_WISE_SP_ACCESS_UPD` (before update)

### RFID.RFID_MACHINES_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| REQUEST_DATE | DATE default SYSDATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `RFID_MACHINES_DATA_DEL` (after delete), `RFID_MACHINES_DATA_INS` (before insert), `RFID_MACHINES_DATA_UPD` (before update)

### RFID.RFID_MACHINE_CATEGORY_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| WARD_ID | VARCHAR2(7) | Y |  |
| IS_DEFAULT_WARD | CHAR(1) default 'Y' | Y |  |
| BUILDING_BLOCK_FLOOR_ID | VARCHAR2(10) | Y |  |
| BUILDING_BLOCK_ID | VARCHAR2(7) | Y |  |

- **Triggers**: `RFID_MACHINE_CATEGORY_ACS_DEL` (after delete), `RFID_MACHINE_CATEGORY_ACS_INS` (before insert), `RFID_MACHINE_CATEGORY_ACS_UPD` (before update)

### RFID.RFID_MACHINE_COMMAND

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER generated by default as identity | Y |  |
| DEVICE_SERIAL | VARCHAR2(50) | N |  |
| COMMAND_NAME | VARCHAR2(255) | Y |  |
| COMMAND_CONTENT | CLOB | Y |  |
| STATUS | NUMBER(11) default 0 | N |  |
| SEND_STATUS | NUMBER(11) default 0 | N |  |
| ERROR_COUNT | NUMBER(11) default 0 | N |  |
| RUN_TIME | DATE | Y |  |
| CREATED_AT | DATE | N |  |
| MODIFIED_AT | DATE | N |  |
| RESPONSE | CLOB | Y |  |

_No standard audit columns._

- **PK** `PK_RFID_MACHINE_COMMAND`: ID

### RFID.RFID_MACHINE_TIMESTAMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| MACHINE_LOCATION_ID | VARCHAR2(3) | N |  |
| MACHINE_TIMESTAMP | VARCHAR2(20) | N |  |
| ACTUAL_TIMESTAMP | DATE default sysdate | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **FK** `FK_RFID_MACH_TIMESTAMP_1`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID) [disabled]

### RFID.RFID_MACHIN_IDENTIFIER_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| RFID_CARD_CODE | VARCHAR2(30) | Y |  |
| MACHINE_IDENTIFIER | NUMBER(10) | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |

- **PK** `PK_RFID_MACHINE_MAPPING`: ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, MACHINE_IDENTIFIER
- **Triggers**: `RFID_MACH_IDENT_MAPING_DEL` (after delete), `RFID_MACH_IDENT_MAPING_INS` (before insert), `RFID_MACH_IDENT_MAPING_UPD` (before update)

### RFID.SECTION_WISE_ATTENDANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| IS_ATTENDANCE_MARK | CHAR(1) | Y |  |

- **PK** `PK_SECTION_WISE_ATTENDANCE`: DEPARTMENT_ID, SECTION_ID, MACHINE_ID
- **FK** `FK_SECTION_WISE_ATTENDANCE_1`: (MACHINE_ID, DEPARTMENT_ID) -> RFID.MACHINE_COMPLETE_DEPARTMENT(MACHINE_ID, DEPARTMENT_ID) [disabled]
- **CHECK** `CHK_SECTION_WISE_ATTENDANCE_1`: ACTIVE IN ('Y', 'N')
- **Triggers**: `SECTION_WISE_ATTENDANCE_DEL` (after delete), `SECTION_WISE_ATTENDANCE_INS` (before insert), `SECTION_WISE_ATTENDANCE_UPD` (before update)

### RFID.TEMP_CARD_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| CARD_NO | VARCHAR2(10) | N |  |
| CARD_DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `TEMP_CARD_SETUP_PK`: CARD_NO
- **Triggers**: `TEMP_CARD_SETUP_DEL` (after delete), `TEMP_CARD_SETUP_INS` (before insert), `TEMP_CARD_SETUP_UPD` (before update)

### RFID.TEMP_RFID_REGISTERED_USERS
This table will be used to retrieve registered users of RFID machines on temporary basis. So that fingerprints and RFId cards can be mapped to original users later on. Data in this table is temporary and can be removed if required.

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| USER_IDENTIFIER | VARCHAR2(20) | N |  |
| USER_NAME | VARCHAR2(30) | Y |  |
| PREVILEGE | VARCHAR2(1) | Y |  |
| USER_ENABLE | VARCHAR2(1) | Y |  |
| USER_PASSWORD | VARCHAR2(10) | Y |  |
| RFID_CARD_NO | VARCHAR2(20) | Y |  |
| FINGERPRINT | VARCHAR2(4000) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| TRANS_DATE | DATE default sysdate | N |  |
| IRIS_VALUE | BLOB | Y |  |

_No standard audit columns._

- **PK** `PK_TRRU_1`: ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, USER_IDENTIFIER

### RFID.TMP_SELECTED_MACHINES_PR

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


### RFID.TRAINING_ATTENDANCE_STG

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| CHECK_TIME | DATE | Y |  |
| MACHINE_ID | NUMBER(5) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REASON | VARCHAR2(4000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| RFID_CODE | VARCHAR2(50) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| TRAINING_ATTENDANCE_MARK | CHAR(1) | Y |  |

- **Triggers**: `TRAINING_ATTENDANCE_STG_DEL` (after delete), `TRAINING_ATTENDANCE_STG_INS` (before insert), `TRAINING_ATTENDANCE_STG_UPD` (before update)



# PART: Views

### RFID.RFID_V_DEPT_GENERAL_ACCESS
```sql
CREATE OR REPLACE FORCE VIEW RFID.RFID_V_DEPT_GENERAL_ACCESS AS
SELECT DA.DEPARTMENT_ID,
       DA.MACHINE_ID,
       DA.ACTIVE,
       RM.DESCRIPTION MACHINE_NAME,
        'DGA' MACHINE_ACCESS_TYPE ,
      'Department wise access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DEPT_GENERAL_ACCESS DA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = DA.MACHINE_ID;
```

### RFID.VU_MACHINE_COMPLETE_DEPARTMENT
```sql
CREATE OR REPLACE FORCE VIEW RFID.VU_MACHINE_COMPLETE_DEPARTMENT AS
SELECT MCD.MACHINE_ID,
       MCD.DEPARTMENT_ID,
       MCD.ACTIVE,
       MCD.IS_ATTENDANCE_MARK,
       D.DESCRIPTION
  FROM RFID.MACHINE_COMPLETE_DEPARTMENT MCD, DEFINITIONS.DEPARTMENT D
 WHERE D.DEPARTMENT_ID = MCD.DEPARTMENT_ID;
```

### RFID.VU_SECTION_WISE_ATTENDANCE
```sql
CREATE OR REPLACE FORCE VIEW RFID.VU_SECTION_WISE_ATTENDANCE AS
SELECT SWA.DEPARTMENT_ID,
       SWA.ACTIVE,
       SWA.SECTION_ID,
       SWA.MACHINE_ID,
       SWA.IS_ATTENDANCE_MARK,
       DS.DESCRIPTION ND_SECTION_DESC
  FROM RFID.SECTION_WISE_ATTENDANCE SWA, DEFINITIONS.DEPARTMENT_SECTION DS
 WHERE DS.DEPARTMENT_ID = SWA.DEPARTMENT_ID
   AND DS.SECTION_ID = SWA.SECTION_ID;
```

### RFID.V_CURRENT_EMPLOYEE
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_CURRENT_EMPLOYEE AS
SELECT E.MRNO,
       E.NAME,
       E.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_NAME (E.MRNO) DEPARTMENT ,
       E.DESIGNATION,
       E.JOINING_DATE,
       HRD.F_GET_EMPLOYEE_DUTY_LOC_ID(E.MRNO)EMPLOYEE_DUTY_LOC,
       HRD.F_GET_EMPLOYEE_LOCATION(E.MRNO) EMPLOYEE_LOCATION
 FROM HRD.V_CURRENT_EMPLOYEE E
 ORDER BY HRD.F_GET_DEPARTMENT_NAME (E.MRNO);
```

### RFID.V_DEPT_WISE_DESIG_ACCESS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_DEPT_WISE_DESIG_ACCESS AS
SELECT DWD.DEPARTMENT_ID, DWD.DESIGNATION_ID, DWD.ACTIVE, D.DESCRIPTION FROM   RFID.DEPT_WISE_DESIG_ACCESS DWD, DEFINITIONS.DESIGNATION D
  WHERE D.DESIGNATION_ID = DWD.DESIGNATION_ID;
```

### RFID.V_DESIGNATION_LOV
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_DESIGNATION_LOV AS
SELECT DISTINCT HRD.F_GET_DESIGNATION_ID(T.MRNO) DESIGNATION_ID,
                D.DESCRIPTION  DESIGNATION,
                t.department_id
  FROM HRD.CURRENT_EMPLOYEES T, DEFINITIONS.DESIGNATION D
  WHERE D.DESIGNATION_ID = HRD.F_GET_DESIGNATION_ID(T.MRNO);
```

### RFID.V_MACHINE_WISE_EMPLOYEE
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_MACHINE_WISE_EMPLOYEE AS
SELECT MWE.MACHINE_ID,
       MWE.MRNO,
       MWE.ACTIVE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(MWE.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(MWE.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(MWE.MRNO) DESIGNATION,
       RFID.PKG_RFID_MACHINES.f_get_rfid_code(MWE.MRNO) RFID_CODE
  FROM RFID.MACHINE_WISE_EMPLOYEE MWE;
```

### RFID.V_RFID_ACCESS_DEPARTMENT
```sql
create or replace force view rfid.v_rfid_access_department as
select rd.department_id, rd.active, d.description dept_name, d.location_id, RD.IS_REFRESH from rfid.rfid_access_department  rd, definitions.department d
where d.department_id = rd.department_id;
```

### RFID.V_RFID_CARD_ISSUE_ACS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_CARD_ISSUE_ACS AS
SELECT C.DESCRIPTION CATERGORY_DESCRIPTION,
       T.SR,
       T.RFID_CARD_NO,
       T.NAME,
       T.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(T.MRNO) PATIENT_NAME,
       T.WARD_ID,
       (select R.DESCRIPTION WARD
          from DEFINITIONS.ROOMS   R
         where R.ROOM_ID = T.WARD_ID) WARD,
       T.ISSUE_DATE,
       T.RECEIVE_DATE,
       T.RETURN,
       T.CARD_CATEGORY_ID,
       T.ISSUED_BY,
       T.REMARKS,
       T.NIC,
       T.RELATION_ID,
       T.ADDRESS,
       T.RETURN_DATE,
       T.RIGHTS_STATUS,
       T.CARD_DESC CARD_DESCRIPTION,
       (SELECT R.DESCRIPTION
          FROM DEFINITIONS.RELATION R
         WHERE R.RELATION_ID = T.RELATION_ID) RELATION,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(T.Issued_By) ISSUED_BY_NAME,
       RM.DESCRIPTION MACHINE_CATEGORY,
       T.MACHINE_CATEGORY_ID,
       T.IS_EXTENDED,
       T.CONTACT_NO,
       t.location_id,
       T.BUILDING_BLOCK_ID,T.BUILDING_BLOCK_FLOOR_ID,
       t.card_valid_till
  FROM RFID.RFID_CARD_ISSUE_ACS       t,
       RFID.RFID_CARD_CATEGORY_ACS    C,
       RFID.RFID_MACHINE_CATEGORY_ACS RM
 WHERE T.CARD_CATEGORY_ID = C.CARD_CATEGORY_ID
   and t.location_id = c.location_id
   AND T.MACHINE_CATEGORY_ID = RM.CATEGORY_ID
   and t.location_id = rm.location_id
 ORDER BY T.ISSUE_DATE DESC;
```

### RFID.V_RFID_CARD_SWIPE_DETAILS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_CARD_SWIPE_DETAILS AS
SELECT CC.DESCRIPTION CARD_CATEGORY,
       CI.SR,
       CI.NAME,
       CI.NIC,
       CI.ADDRESS,
       MC.DESCRIPTION MACHINE_CATEGORY,
       R.DESCRIPTION WARD,
       A.CHECK_TIME IN_TIME,
       NULL OUT_TIME,
       a.check_time,
       CI.MRNO,
       P.name PATIENT_NAME,
       P.ARMY_RANK,
       P.service_no,
       CI.WARD_ID,
       CI.CARD_CATEGORY_ID,
       CI.MACHINE_CATEGORY_ID,
       CI.ISSUE_DATE,
       CI.RETURN_DATE CARD_VALID_TILL,
       CI.RECEIVE_DATE CARD_RECEIVE_DATE,
       CI.LOCATION_ID,
       CI.CONTACT_NO,
       CI.RFID_CARD_NO,
       CI.BUILDING_BLOCK_ID,
       CI.BUILDING_BLOCK_FLOOR_ID,
       A.MACHINE_ID,
       A.MACHINE_DEFAULT_CHECK_IN_OUT,
     /*  (SELECT BB.DESCRIPTION
          FROM DEFINITIONS.BUILDING_BLOCK BB
         WHERE BB.BUILDING_BLOCK_ID = CI.BUILDING_BLOCK_ID
         AND BB.LOCATION_ID = CI.LOCATION_ID)*/NULL BUILDING_BLOCK
  FROM RFID.ATTENDANCE_EMPLOYEE       A,
       RFID.RFID_CARD_ISSUE_ACS       CI,
       RFID.RFID_MACHINE_CATEGORY_ACS MC,
       RFID.RFID_CARD_CATEGORY_ACS    CC,
       DEFINITIONS.ROOMS              R,
       REGISTRATION.V_RFID_PATIENT    P
 WHERE A.MRNO = CI.MRNO
   AND A.RFID_CODE = CI.RFID_CARD_NO
   AND A.SERIAL_NO_FOR_CARD_SWIPE = CI.SERIAL_NO_FOR_CARD_SWIPE
   AND CI.MACHINE_CATEGORY_ID = MC.CATEGORY_ID
   AND CI.CARD_CATEGORY_ID = CC.CARD_CATEGORY_ID
   AND CI.LOCATION_ID = CC.LOCATION_ID
   AND CI.LOCATION_ID = MC.LOCATION_ID
   AND CI.WARD_ID = R.ROOM_ID
   AND CI.MRNO = P.mrno;
```

### RFID.V_RFID_CONFIDENTAIL_Q
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_CONFIDENTAIL_Q AS
SELECT RQ.MACHINE_ID,
           RQ.MRNO,
           HIS.PKG_PATIENT.GET_PATIENT_NAME(RQ.MRNO) NAME,
           HRD.F_GET_DEPARTMENT_NAME(RQ.MRNO) DEPARTMENT,
           HRD.F_GET_DESIGNATION_DESC(RQ.MRNO) DESIGNATION,
           RQ.CHECK_TIME,
           RQ.MACHINE_IDENTIFIER,
           RQ.REASON,
           RQ.SR_NO,
           M.DESCRIPTION MACHINE_DESC  ,
           RFID.PKG_COMMON.F_GET_MACHINE_LOC_ID(RQ.MACHINE_ID) MACHINE_LOC_ID,
           RFID.PKG_COMMON.F_GET_MACHINE_LOC_DESC(RQ.MACHINE_ID) MACHINE_LOC_DESC
      FROM RFID.RFID_CONFIDENTIAL_Q RQ , RFID.RFID_MACHINES M
      WHERE RQ.MACHINE_ID = M.MACHINE_ID
      AND M.IS_CONFIDENTIAL ='Y';
```

### RFID.V_RFID_CONFI_MACHINE_RIGHTS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_CONFI_MACHINE_RIGHTS AS
SELECT R.MRNO, R.MACHINE_ID, R.ACTIVE, M.DESCRIPTION MACHINE_NAME FROM RFID.RFID_CONFI_MACHINE_RIGHTS R, RFID.RFID_MACHINES M
WHERE R.MACHINE_ID = M.MACHINE_ID;
```

### RFID.V_RFID_DEFAULT_ACCESS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_DEFAULT_ACCESS AS
SELECT RDA.MACHINE_ID,
       M.DESCRIPTION MACHINE_NAME,
       RDA.LOCATION_ID,
       RDA.ACTIVE,
       RDA.REMARKS,
       RDA.IS_REFRESH,
       'DAA' MACHINE_ACCESS_TYPE ,
      'DEFUALT ACCESS'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DEFAULT_ACCESS RDA, RFID.RFID_MACHINES M
 WHERE M.MACHINE_ID = RDA.MACHINE_ID;
```

### RFID.V_RFID_DESIG_WISE_SP_ACCESS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_DESIG_WISE_SP_ACCESS AS
SELECT RDA.MACHINE_ID,
       RDA.DESIGNATION_ID,
       RDA.DEPARTMENT_ID,
       RDA.ACTIVE,
       RM.DESCRIPTION MACHINE_NAME,
       'DSA' MACHINE_ACCESS_TYPE ,
      'Designation wis special access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DESIG_WISE_SP_ACCESS RDA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = RDA.MACHINE_ID;
```

### RFID.V_RFID_EMP_WISE_SP_ACCESS
```sql
CREATE OR REPLACE FORCE VIEW RFID.V_RFID_EMP_WISE_SP_ACCESS AS
SELECT
       RA.MRNO,
       RA.MACHINE_ID,
       RM.DESCRIPTION MACHINE_NAME ,
       RA.ACTIVE,
        'E' MACHINE_ACCESS_TYPE ,
      'Employee Wise Access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_EMP_WISE_SP_ACCESS RA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = RA.MACHINE_ID
 AND RM.ACTIVE ='Y';
```



# PART: Packages, procedures, functions, sequences

### Sequences
- ISEQ
- SEQ_RFID_ACCESS_SYNC_LOG
- SEQ_RFID_ACCESS_SYNC_RUN
- SEQ_RFID_CLEANUP_RUN
- SEQ_RFID_DELETED_ACCESS_AUDIT

### Packages (specifications)

#### RFID.PKG_COMMON
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_COMMON IS

  PROCEDURE FOR_CHANGE_RFID_CARD(P_MRNO      IN VARCHAR2,
                                 P_RFID_CODE IN VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_DESIG_WISE_RFID_RIGHTS(P_DESIGNATION_ID   IN VARCHAR2,
                                       P_RFID_CATAGORY_ID IN NUMBER,
                                       P_MRNO             IN VARCHAR2,
                                       P_STOP             OUT VARCHAR2,
                                       P_ALERT_TEXT       OUT VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_CATEGORY_WISE_RFID_RIGHTS(P_RFID_CATAGORY_ID IN NUMBER,
                                          P_MRNO             IN VARCHAR2,
                                          P_STOP             OUT VARCHAR2,
                                          P_ALERT_TEXT       OUT VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_DEPART_WISE_RFID_RIGHTS(P_DEPARTMENT_ID    IN VARCHAR2,
                                        P_RFID_CATAGORY_ID IN NUMBER,
                                        P_MACHINE_ID       IN NUMBER,
                                        P_MRNO             IN VARCHAR2,
                                        P_STOP             OUT VARCHAR2,
                                        P_ALERT_TEXT       OUT VARCHAR2);

  /**********************************************************************/
  /*****************************************************************/
  PROCEDURE PRO_RFID_REVOKE_RIGHTS(P_MRNO       IN VARCHAR2,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  /**********************************************************************/
  FUNCTION F_GET_RFID_CODE(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  /**********************************************************************/
  PROCEDURE P_ASSIGN_RFID_RIGHTS_TO_EMP(P_MRNO        IN VARCHAR2,
                                        P_STOP        OUT VARCHAR2,
                                        P_ALERT_TEXT  OUT VARCHAR2,
                                        P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL);

  /**********************************************************************/
  -------------------------------------------------------------------------------------------------
  -- THIS FUNCTION IS USED TO IDENTIFY EITHER MARKING ATTENDANCE ON A MACHINE IS ALLOWED OR NOT ---
  -------------------------------------------------------------------------------------------------
  FUNCTION F_IS_MARK_ATTENDANCE_ALLOWED(P_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                        P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE)
    RETURN CHAR;

  -----------------------------------------------------------------------------------------------------------
  -- THIS PROCEDURE IS USED TO ASSIGN DEPARTMENTAL/SECTION WIDE RIGHTS TO THE EMPLOYEES ON RFID MACHINE  ---
  -----------------------------------------------------------------------------------------------------------
  PROCEDURE P_INSERT_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                         P_SECTION_ID    IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                         P_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                         P_ALERT_TEXT    OUT VARCHAR2,
                                         P_STOP          OUT CHAR);

  -----------------------------------------------------------------------------------------------------------
  -- THIS PROCEDURE IS USED TO REVERT DEPARTMENTAL/SECTION WIDE RIGHTS TO THE EMPLOYEES ON RFID MACHINE  ---
  -----------------------------------------------------------------------------------------------------------
  PROCEDURE P_REVOKE_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                         P_SECTION_ID    IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                         P_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                         P_ALERT_TEXT    OUT VARCHAR2,
                                         P_STOP          OUT CHAR);

  /*****************************************************************************************/
  PROCEDURE PRO_POPULATE_RFID_DEPARTMENT(P_MACHINE_ID  IN VARCHAR2,
                                         P_LOCATION_ID IN VARCHAR2,
                                         P_ALERT_TEXT  OUT VARCHAR2,
                                         P_STOP        OUT VARCHAR2);

  /*****************************************************************************************/
  FUNCTION F_EMP_CODE_FROM_RFID(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2;
  /*****************************************************************************************/
  PROCEDURE P_INSERT_RFID_ATTENDANCE(P_CHECK_TIME        IN DATE,
                                     P_MACHINE_CODE      IN VARCHAR2,
                                     P_RFID_CODE         IN VARCHAR2,
                                     P_CHECK_TYPE        IN VARCHAR2,
                                     P_VERIFICATION_MODE IN VARCHAR2,
                                     P_STOP              OUT CHAR,
                                     P_ALERT_TEXT        OUT VARCHAR2);
  /*****************************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2,
                               P_LOCATION_ID        IN VARCHAR2)
    RETURN VARCHAR2;
  /*****************************************************************************************/
  PROCEDURE P_GET_RFID_MACHINE_CODE(P_RFID_CODE          IN VARCHAR2,
                                    P_MACHINE_CODE       IN OUT VARCHAR2,
                                    P_MACHINE_IDENTIFIER IN OUT VARCHAR2,
                                    P_LOCATION_ID        IN VARCHAR2,
                                    P_IP_ADDRESS         IN VARCHAR2,
                                    P_MACHINE_CATEGORY   OUT VARCHAR2,
                                    P_EMPLOYEE_CODE      OUT VARCHAR2);
  /*****************************************************************************************/
  FUNCTION F_IS_TRANSPORT_POOL_CARD(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************************/
  FUNCTION F_MACHINE_CODE_FROM_IP(P_IP_ADDRESS IN VARCHAR2) RETURN VARCHAR2;
  /**************************************************************************/
  FUNCTION F_GET_IDENTIFIER(P_MRNO         IN VARCHAR2,
                            P_MACHINE_CODE IN VARCHAR2,
                            P_LOCATION_ID  IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION GET_IDENTIFIER_FROM_RFIDCODE(P_RFID_CODE    IN VARCHAR2,
                                        P_MACHINE_CODE IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_RFID_MACHINE_LOCATION_ID(P_MACHINE_CODE IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_RFID_FROM_MAPPING(P_MACHINE_CODE IN VARCHAR2,
                                   P_MRNO         IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_TYPE(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_CHECH_VEHICLE_MACHINE_RIGHTS(P_MACHINE_ID IN VARCHAR2,
                                          P_MRNO       IN VARCHAR2)
    RETURN CHAR;
  /********************************************************************************/
  FUNCTION F_CHECK_ACTIVE_EMP(P_RFID_CODE IN VARCHAR2) RETURN CHAR;
  /********************************************************************************/
  PROCEDURE P_INS_ATTENDANCE_PAT(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                                 P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                                 P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_REASON             VARCHAR2,
                                 P_STOP               OUT CHAR,
                                 P_ALERT_TEXT         OUT VARCHAR2);
  /***************************************/
  PROCEDURE FOR_REMOVE_RFID_CARD(P_MRNO          IN VARCHAR2,
                                 P_OLD_RFID_CODE IN VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_INS_RFID_QUEUE(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                             P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                             P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                             P_MRNO               VARCHAR2,
                             P_STOP               OUT CHAR,
                             P_ALERT_TEXT         OUT VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_DEL_ALERT_QUEUE(P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                              P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                              P_SRNO               NUMBER,
                              P_STOP               OUT CHAR,
                              P_ALERT_TEXT         OUT VARCHAR2);
  /********************************************************************************/
  FUNCTION F_GET_MACH_IS_CONF(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  PROCEDURE P_INS_TEMP_CARD(P_MRNO        HRD.VU_INFORMATION.MRNO%TYPE,
                            P_ACTUAL_RFID HRD.VU_INFORMATION.RFID_CODE %TYPE,
                            P_TEMP_RFID   VARCHAR2,
                            P_DAY         NUMBER,
                            P_STOP        OUT CHAR,
                            P_ALERT_TEXT  OUT VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_UPDATE_RFID_CODE(P_MRNO       HRD.VU_INFORMATION.MRNO%TYPE,
                               P_RFID_ID    VARCHAR2,
                               P_STOP       OUT CHAR,
                               P_ALERT_TEXT OUT VARCHAR2);
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_LOC_ID(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_LOC_DESC(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;

  /**********************************************************************************/

  PROCEDURE P_INS_ATTENDANCE_EMP(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                                 P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                                 P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_MRNO               VARCHAR2,
                                 P_REASON             VARCHAR2,
                                 P_FROM_DATE          DATE,
                                 P_TO_DATE            DATE,
                                 P_LOCATION_ID        RFID.ATTENDANCE.LOCATION_ID%TYPE,
                                 P_STOP               OUT CHAR,
                                 P_ALERT_TEXT         OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_IS_RFID_NEW_SCHEME(P_DEPARTMENT_ID IN VARCHAR2) RETURN CHAR;

  /***********************************************************************************/
  PROCEDURE P_GRANT_RFID_ACCESS_NEW_SCHEME(P_MRNO        IN VARCHAR2,
                                           P_OBJECT_CODE IN VARCHAR2,
                                           P_STOP        OUT CHAR,
                                           P_ALERT_TEXT  OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_GET_EMP_SEX_ID(P_MRNO IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************************/
  FUNCTION F_GET_RFID_MACHINE_SEX_ID(P_MACHINE_ID IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************************/
  PROCEDURE P_INS_TRAINING_ATTENDANCE_STG(P_CHECKTIME  RFID.ATTENDANCE_EMPLOYEE.CHECK_TIME%TYPE,
                                          P_MACHINE_ID RFID.ATTENDANCE_EMPLOYEE.MACHINE_ID%TYPE,
                                          P_MRNO       VARCHAR2,
                                          P_REASON     VARCHAR2,
                                          P_RFID_CODE  RFID.ATTENDANCE_EMPLOYEE.rfid_code%TYPE,
                                          P_STOP       OUT CHAR,
                                          P_ALERT_TEXT OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_GET_TRAINING_ATTEND_MARK(P_MACHINE_ID RFID.RFID_MACHINES.MACHINE_ID%TYPE)
    RETURN CHAR;

END PKG_COMMON;
```

#### RFID.PKG_RFID_MACHINES
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_MACHINES AS

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.RFID_MACHINES
  /******************************************************************************/

  TYPE RFID_MACHINES_REC IS RECORD(
    MACHINE_ID   RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    ACTIVE       RFID.RFID_MACHINES.ACTIVE%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO      RFID.RFID_MACHINES.PORT_NO%TYPE,
    ORDER_BY     RFID.RFID_MACHINES.ORDER_BY%TYPE,
    CATEGORY_ID  RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  TYPE RFID_MACHINES_TBL IS TABLE OF RFID_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE RFID_MACHINES_TBL_PF IS TABLE OF RFID_MACHINES_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/
  TYPE DEPT_MACHINES_RC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);

  TYPE DEPT_MACHINES_TL IS TABLE OF DEPT_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE DEPT_MACHINES_TL_PF IS TABLE OF DEPT_MACHINES_RC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/
  TYPE DEPT_MACHINES_REC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);

  TYPE DEPT_MACHINES_TBL IS TABLE OF DEPT_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE DEPT_MACHINES_TBL_PF IS TABLE OF DEPT_MACHINES_REC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_REC IS RECORD(
    MACHINE_ID RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO       RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE     RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE);

  TYPE EMP_MACHINES_TBL IS TABLE OF EMP_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TBL_PF IS TABLE OF EMP_MACHINES_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID  RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO        RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    NAME        HRD.V_INFORMATION.NAME%TYPE,
    DISP_MRNO   HRD.V_INFORMATION.DISP_MRNO%TYPE,
    DEPARTMENT  HRD.V_INFORMATION.DEPARTMENT%TYPE,
    DESIGNATION HRD.V_INFORMATION.DESIGNATION%TYPE,
    ACTIVE      RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE   HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following pipelined function will return table of records
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  FUNCTION F_RFID_MACHINES_QRY(P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                               P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                               P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                               P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                               P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                               P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                               P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                               P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE)
    RETURN RFID_MACHINES_TBL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_QRY(P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                                P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                                P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                P_DATA         IN OUT RFID_MACHINES_TBL,
                                P_STOP         OUT VARCHAR2,
                                P_ALERT_TEXT   OUT VARCHAR2,
                                P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                P_DATA            IN RFID_MACHINES_REC,
                                P_STOP            OUT VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_INS(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_LCK(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_UPD(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_DEL(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID.MACHINE_COMPLETE_DEPARTMENT
  -- Purpose   : The following pipelined function will return table of records
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  FUNCTION F_DEPT_MACHINES_QY(P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                              P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                              P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                              P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE)
    RETURN DEPT_MACHINES_TL_PF
    PIPELINED;

  PROCEDURE P_DEPT_MACHINES_QY(P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                               P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                               P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                               P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE,
                               P_DATA          IN OUT DEPT_MACHINES_TL,
                               P_STOP          OUT VARCHAR2,
                               P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                P_DATA            IN DEPT_MACHINES_RC,
                                P_STOP            OUT VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_INS(P_MACHINE_ID    OUT RFID.MACHINE_COMPLETE_DEPARTMENT .MACHINE_ID%TYPE,
                                P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_DATA          IN OUT DEPT_MACHINES_TL,
                                P_STOP          OUT VARCHAR2,
                                P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_LCK(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_UPD(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_DEL(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  FUNCTION F_EMP_MACHINES_QY(P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                             P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                             P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                             P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                             P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                             P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                             P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                             P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE)
    RETURN EMP_MACHINES_TL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                              P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                              P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                              P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                              P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_DATA        IN OUT EMP_MACHINES_TL,
                              P_STOP        OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : USMAN SHAUKAT (3821)
  -- Created on: 17-JUN-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to put data in RFID.RFID_DATA_TRANSFER
  --             for utility to send to machines.
  /******************************************************************************/

  PROCEDURE P_SEND_DATA_TO_MACHINE_V2(P_MACHINE_ID           IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_MRNO                 IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                      P_ACTION               IN CHAR,
                                      P_RFID_CODE            IN VARCHAR2 DEFAULT NULL,
                                      P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                      P_MACHINE_CODE         IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                      P_IP_ADDRESS           IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                      P_PORT_NO              IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                      P_MACHINE_LOCATION_ID  IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                                      P_MACHINE_CATEGORY     IN RFID.RFID_MACHINES.MACHINE_CATEGORY%TYPE,
                                      P_STOP                 OUT VARCHAR2,
                                      P_ALERT_TEXT           OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE P_SEND_DATA_TO_MACHINE(P_MACHINE_ID           IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                   P_MRNO                 IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                   P_ACTION               IN CHAR,
                                   P_STOP                 OUT VARCHAR2,
                                   P_ALERT_TEXT           OUT VARCHAR2,
                                   P_RFID_CODE            IN VARCHAR2 DEFAULT NULL,
                                   P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                   P_OBJECT_CODE          IN VARCHAR2 DEFAULT NULL,
                                   P_ACCESS_GRANT_EVENT   IN VARCHAR2 DEFAULT NULL);
  /*******************************************************************************/
  PROCEDURE P_COPY_MACHINE_RIGHTS(P_TYPE                 IN CHAR,
                                  P_MRNO                 IN VARCHAR2,
                                  P_MASTER_MRNO          IN VARCHAR2,
                                  P_MACHINE_ID           IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_MASTER_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                  P_STOP                 OUT CHAR,
                                  P_ALERT_TEXT           OUT VARCHAR);

  /******************************************************************************/
  -- Author    : USMAN SHAUKAT (3821)
  -- Created on: 17-JUN-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to reload already saved data to machine storage.
  /******************************************************************************/
  PROCEDURE P_RELOAD_MACHINE_DATA(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-SEP-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to get rfid code against emp mrno.
  /******************************************************************************/

  FUNCTION f_get_rfid_code(P_MRNO IN VARCHAR2) return varchar;
  /*******************************************************************/
  PROCEDURE P_INACTIVE_CARD_CATAGORY(P_CARD_TYPE_ID IN RFID.RFID_CARD_TYPE.CARD_TYPE_ID%TYPE,
                                     P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
                                     P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                     P_RFID_CARD_NO IN RFID.RFID_CARDS.RFID_CARD_NO%TYPE,
                                     P_ACTION       IN VARCHAR2,
                                     P_STOP         OUT CHAR,
                                     P_ALERT_TEXT   OUT VARCHAR);
  /*******************************************************************/
  PROCEDURE P_DELETE_EMP_MACHINE_DATA(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO %TYPE,
                                      P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_STOP       OUT CHAR,
                                      P_ALERT_TEXT OUT VARCHAR);
  /*********************************************************************************/
  PROCEDURE P_REVOKE_MACHINE_RIGHTS(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                    P_STOP       OUT CHAR,
                                    P_ALERT_TEXT OUT VARCHAR);
  /*************************************************************************************/
  FUNCTION F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO       IN VARCHAR2,
                                          P_MACHINE_ID IN VARCHAR2)
    RETURN VARCHAR2;
  /************************************************************************************/
  FUNCTION F_IS_RFID_REQUIRED(P_MACHINE_ID IN VARCHAR2) RETURN CHAR;
  /**********************************************************************************/
  FUNCTION F_IS_ALREADY_FOUND_IN_MAPPING(P_MACHINE_ID IN VARCHAR2,
                                         P_MRNO       IN VARCHAR2)
    RETURN CHAR;
  /**********************************************************************************/
  FUNCTION F_GET_RFID_CODE_FROM_MAPPING(P_MACHINE_ID IN VARCHAR2,
                                        P_MRNO       IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/
  FUNCTION F_GET_MACHINE_WISE_MAX_COUNTER(P_MACHINE_ID IN VARCHAR2)
    RETURN NUMBER;
  /*********************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2,
                               P_LOCATION_ID        IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/

  PROCEDURE P_NEW_MACHINE_SUPERCARD_ADD(P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_MACHINE_CODE        IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                        P_IP_ADDRESS          IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                        P_PORT_NO             IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                        P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                                        P_MACHINE_CATEGORY    IN RFID.RFID_MACHINES.MACHINE_CATEGORY%TYPE,
                                        P_EVENT               IN VARCHAR2,
                                        P_STOP                OUT CHAR,
                                        P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/
  PROCEDURE J_MISSED_MACHINE_IN_SUPERCARD(P_ALERT_TEXT OUT VARCHAR2,
                                          P_STOP       OUT VARCHAR2);
  /********************************************************************************************/
  PROCEDURE P_SYN_ATTENDANCE_EMP(P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_FROM_DATE  DATE,
                                 P_TO_DATE    DATE,
                                 P_STOP       OUT CHAR,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /********************************************************************************************/
  FUNCTION RFID_CARD_CODE_CONVERSION(P_STRING_VALUE IN VARCHAR2,
                                     P_MRNO         IN VARCHAR2,
                                     P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE)
    RETURN VARCHAR2;
  /********************************************************************************************/

END PKG_RFID_MACHINES;
```

#### RFID.PKG_48FRM00102
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_48FRM00102 AS
  /**************************************************************************/
  PROCEDURE PRO_POPULATE_DESIGNATION(P_DEPARTMENT_ID IN VARCHAR2,
                                     P_STOP          OUT CHAR,
                                     P_ALERT_TEXT    OUT VARCHAR2);
  /**************************************************************************/
  FUNCTION F_GET_ALREADY_POPULATED(P_DEPARTMENT_ID IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************/
  PROCEDURE P_REFRESH_DEPARTMENT(P_DEPARTMENT_ID IN VARCHAR2,
                                 P_LOCATION_ID   IN VARCHAR2,
                                 P_OBJECT_CODE   IN VARCHAR2,
                                 P_STOP          OUT CHAR,
                                 P_ALERT_TEXT    OUT VARCHAR2);
  /***********************************************************************/
  FUNCTION F_GET_IS_SUPER_CARD(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  /***********************************************************************/
  PROCEDURE P_GRANT_DEFAULT_ACCESS(P_MACHINE_ID         IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                   P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_OBJECT_CODE        IN VARCHAR2,
                                   P_EVENT              IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                   P_ACCESS_GRANT_EVENT IN VARCHAR2,
                                   P_STOP               OUT VARCHAR2,
                                   P_ALERT_TEXT         OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REVOKE_DEFAULT_ACCESS(P_MACHINE_ID         IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                    P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_OBJECT_CODE        IN VARCHAR2,
                                    P_EVENT              IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                    P_ACCESS_GRANT_EVENT IN VARCHAR2,
                                    P_STOP               OUT VARCHAR2,
                                    P_ALERT_TEXT         OUT VARCHAR2);
  /***************************************************************************************/
  PROCEDURE P_REVOKE_DEPT_DESIG_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                       P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_OBJECT_CODE         IN VARCHAR2,
                                       P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                       P_DEPARTMENT_ID       IN VARCHAR2,
                                       P_DESIGNATION_ID      IN VARCHAR2,
                                       P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                       P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                       P_STOP                OUT VARCHAR2,
                                       P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_GRANT_DEPT_DESIG_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_OBJECT_CODE         IN VARCHAR2,
                                      P_DEPARTMENT_ID       IN VARCHAR2,
                                      P_DESIGNATION_ID      IN VARCHAR2,
                                      P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                      P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                      P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                      P_STOP                OUT VARCHAR2,
                                      P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_GRANT_REVOKE_EMP_WISE_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                           P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                           P_OBJECT_CODE         IN VARCHAR2,
                                           P_EMPLOYEE_CODE       IN VARCHAR2,
                                           P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                           P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                           P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                           P_STOP                OUT VARCHAR2,
                                           P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REFRESH_EMP_WISE_ACCESS(P_MRNO        IN VARCHAR2,
                                      P_OBJECT_CODE IN VARCHAR2,
                                      P_STOP        OUT CHAR,
                                      P_ALERT_TEXT  OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REFRESH_EMP_WISE_ACCESS(P_MRNO           IN VARCHAR2,
                                      P_DEPARTMENT_ID  IN VARCHAR2,
                                      P_DESIGNATION_ID IN VARCHAR2,
                                      P_OBJECT_CODE    IN VARCHAR2,
                                      P_STOP           OUT CHAR,
                                      P_ALERT_TEXT     OUT VARCHAR2);
  /****************************************************************************/
END;
```

#### RFID.PKG_ACCESS_CONTROL_REPORTS
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_ACCESS_CONTROL_REPORTS AS
  /***********************************************************************************************
        PACKAGE NAME: RFID.PKG_ACCESS_CONTROL_REPORTS
        PURPOSE: THIS PACKAGE WILL AUTOMATE REPORTS
        ----------------------------------------------------------------------------------
        REVISIONS:
        VER        DATE         AUTHOR                  DESCRIPTION
        ---------  ----------   ---------------         -----------------------------------
       1.0        10-MAY-2024   AQIB KHALID             1. CREATED THIS PACKAGE.
  ************************************************************************************************/
  TYPE ISSUED_CARDS_REC IS RECORD(
    CATERGORY_DESCRIPTION   RFID.V_RFID_CARD_ISSUE_ACS.CATERGORY_DESCRIPTION%TYPE,
    SR                      RFID.V_RFID_CARD_ISSUE_ACS.SR%TYPE,
    RFID_CARD_NO            RFID.V_RFID_CARD_ISSUE_ACS.RFID_CARD_NO%TYPE,
    NAME                    RFID.V_RFID_CARD_ISSUE_ACS.NAME%TYPE,
    MRNO                    RFID.V_RFID_CARD_ISSUE_ACS.MRNO%TYPE,
    PATIENT_NAME            RFID.V_RFID_CARD_ISSUE_ACS.PATIENT_NAME%TYPE,
    ARMY_RANK               REGISTRATION.V_RFID_PATIENT.ARMY_RANK%TYPE,
    service_no              REGISTRATION.V_RFID_PATIENT.service_no%TYPE,
    WARD_ID                 RFID.V_RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    WARD                    RFID.V_RFID_CARD_ISSUE_ACS.WARD%TYPE,
    ISSUE_DATE              RFID.V_RFID_CARD_ISSUE_ACS.ISSUE_DATE%TYPE,
    RECEIVE_DATE            RFID.V_RFID_CARD_ISSUE_ACS.RECEIVE_DATE%TYPE,
    RETURN                  RFID.V_RFID_CARD_ISSUE_ACS.RETURN%TYPE,
    CARD_CATEGORY_ID        RFID.V_RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE,
    ISSUED_BY               RFID.V_RFID_CARD_ISSUE_ACS.ISSUED_BY%TYPE,
    REMARKS                 RFID.V_RFID_CARD_ISSUE_ACS.REMARKS%TYPE,
    NIC                     RFID.V_RFID_CARD_ISSUE_ACS.NIC%TYPE,
    RELATION_ID             RFID.V_RFID_CARD_ISSUE_ACS.RELATION_ID%TYPE,
    ADDRESS                 RFID.V_RFID_CARD_ISSUE_ACS.ADDRESS%TYPE,
    RETURN_DATE             RFID.V_RFID_CARD_ISSUE_ACS.RETURN_DATE%TYPE,
    RIGHTS_STATUS           RFID.V_RFID_CARD_ISSUE_ACS.RIGHTS_STATUS%TYPE,
    CARD_DESCRIPTION        RFID.V_RFID_CARD_ISSUE_ACS.CARD_DESCRIPTION%TYPE,
    RELATION                RFID.V_RFID_CARD_ISSUE_ACS.RELATION%TYPE,
    ISSUED_BY_NAME          RFID.V_RFID_CARD_ISSUE_ACS.ISSUED_BY_NAME%TYPE,
    MACHINE_CATEGORY        RFID.V_RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY%TYPE,
    MACHINE_CATEGORY_ID     RFID.V_RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY_ID%TYPE,
    IS_EXTENDED             RFID.V_RFID_CARD_ISSUE_ACS.IS_EXTENDED%TYPE,
    CONTACT_NO              RFID.V_RFID_CARD_ISSUE_ACS.CONTACT_NO%TYPE,
    location_id             RFID.V_RFID_CARD_ISSUE_ACS.location_id%TYPE,
    BUILDING_BLOCK_ID       RFID.V_RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
    BUILDING_BLOCK_FLOOR_ID RFID.V_RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_FLOOR_ID%TYPE,
    card_valid_till         RFID.V_RFID_CARD_ISSUE_ACS.card_valid_till%TYPE);
  --------------------------------------------------------------------
  TYPE ISSUED_CARDS_TAB IS TABLE OF ISSUED_CARDS_REC;
  -----------------------------------------------------------------------------------
  FUNCTION ISSUED_CARDS_REPORT(P_FROM_DATE   DATE,
                               P_TO_DATE     DATE,
                               P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                               P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                               P_CARD_CAT_ID IN RFID.RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.ISSUED_CARDS_TAB
    PIPELINED;
  ---------------------------------------------------------------------------------
  TYPE BUILD_WISE_WARD_REC IS RECORD(
    WARD              VARCHAR2(4000),
    WARD_ID           RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    LOCATION_ID       RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
    BUILDING_BLOCK_ID RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
    IN_COUNT          NUMBER,
    OUT_COUNT         NUMBER);
  -------------------------------------------------------------------------------------------------------------------------
  TYPE BUILD_WISE_WARD_TAB IS TABLE OF BUILD_WISE_WARD_REC;
  --------------------------------------------------------------------------------------------------------------------------
  FUNCTION BUILDING_WISE_WARDS_COUNT(P_FROM_DATE   DATE,
                                     P_TO_DATE     DATE,
                                     P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                     P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                                     P_WARD_ID     IN RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.BUILD_WISE_WARD_TAB
    PIPELINED;
  /************************************************************************************************/
  TYPE EMP_CARD_INOUT_REC IS RECORD(
    MRNO                RFID.ATTENDANCE_EMPLOYEE.MRNO%TYPE,
    EMP_NAME            VARCHAR2(4000),
    NAME                VARCHAR2(4000),
    ARMY_RANK           VARCHAR2(4000),
    service_no          VARCHAR2(4000),
    IN_TIME             DATE,
    OUT_TIME            DATE,
    MACHINE_LOCATION_ID RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE);
  -------------------------------------------------------------------------------------------------------------------------
  TYPE EMP_CARD_INOUT_TAB IS TABLE OF EMP_CARD_INOUT_REC;
  ----------------------------------------------------------
  FUNCTION EMP_CARD_INOUT_DETAIL(P_FROM_DATE   DATE,
                                 P_TO_DATE     DATE,
                                 P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                 P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.EMP_CARD_INOUT_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------------------------------------
  TYPE TOP_TEN_VISITORS_REC IS RECORD(
    NAME         RFID.V_RFID_CARD_SWIPE_DETAILS.NAME%TYPE,
    NIC          RFID.V_RFID_CARD_SWIPE_DETAILS.NIC%TYPE,
    CONTACT_NO   RFID.V_RFID_CARD_SWIPE_DETAILS.CONTACT_NO%TYPE,
    RFID_CARD_NO RFID.V_RFID_CARD_SWIPE_DETAILS.RFID_CARD_NO%TYPE,
    MRNO         RFID.V_RFID_CARD_SWIPE_DETAILS.MRNO%TYPE,
    PATIENT_NAME RFID.V_RFID_CARD_SWIPE_DETAILS.PATIENT_NAME%TYPE,
    ARMY_RANK    RFID.V_RFID_CARD_SWIPE_DETAILS.ARMY_RANK%TYPE,
    LOCATION_ID  RFID.V_RFID_CARD_SWIPE_DETAILS.LOCATION_ID%TYPE,
    VISITS_COUNT NUMBER);
  -----------------------------------------------------------------------------
  TYPE TOP_TEN_VISITORS_TAB IS TABLE OF TOP_TEN_VISITORS_REC;
  ----------------------------------------------------------------------------------
  FUNCTION TOP_TEN_VISITORS(P_FROM_DATE   DATE,
                            P_TO_DATE     DATE,
                            P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                            P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_TEN_VISITORS_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------------------------------------
  TYPE TOP_FIVE_WARD_REC IS RECORD(
    WARD           RFID.V_RFID_CARD_ISSUE_ACS.WARD%TYPE,
    WARD_ID        RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    LOCATION_ID    RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
    VISITORS_COUNT NUMBER);
  -----------------------------------------------------------------------------
  TYPE TOP_FIVE_WARD_TAB IS TABLE OF TOP_FIVE_WARD_REC;
  ----------------------------------------------------------------------------------
  FUNCTION TOP_FIVE_WARDS(P_FROM_DATE   DATE,
                          P_TO_DATE     DATE,
                          P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                          P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_FIVE_WARD_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------
  FUNCTION F_WARD_WISE_CARD_SWIPE_COUNT(P_LOCATION_ID       RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                        P_BUILDING_BLOCK_ID RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                                        P_WARD_ID           RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
                                        -- P_MACHINE_ID        RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_MACHINE_TYPE RFID.RFID_MACHINES.DEFAULT_CHECK_IN_OUT%TYPE)
    RETURN NUMBER;
END;
```

#### RFID.PKG_MACHINE_WISE_EMPLOYEE
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_MACHINE_WISE_EMPLOYEE AS

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following record type, table types will be used
  --             for dml of HRD.INFORMATION
  /******************************************************************************/

  TYPE HRD_INFO IS RECORD(
    DESIGNATION_ID HRD.INFORMATION.DESIGNATION_ID%TYPE,
    MRNO           HRD.INFORMATION.MRNO%TYPE,
    DISP_MRNO      VARCHAR2(11),
    NAME           REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT     DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DEPARTMENT_ID  DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    JOINING_DATE   HRD.INFORMATION.JOINING_DATE%TYPE,
    RFID_CODE      HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE HRD_INFO_TBL IS TABLE OF HRD_INFO INDEX BY PLS_INTEGER;
  TYPE HRD_INFO_TBL_PF IS TABLE OF HRD_INFO; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID   RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    MRNO         RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE       RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE    HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following pipelined function will return table of records
  --             HRD.INFORMATION.
  /******************************************************************************/

  FUNCTION F_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                          P_MRNO           IN HRD.INFORMATION.MRNO%TYPE,
                          P_DISP_MRNO      IN VARCHAR2,
                          P_NAME           IN REGISTRATION.PATIENT.NAME%TYPE,
                          P_DESIGNATION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                          P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                          P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE)

   RETURN HRD_INFO_TBL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for querying data of
  --             HRD.INFORMATION.
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                           P_MRNO           IN HRD.INFORMATION.MRNO%TYPE,
                           P_DISP_MRNO      IN VARCHAR2,
                           P_NAME           IN REGISTRATION.PATIENT.NAME%TYPE,
                           P_DESIGNATION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                           P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                           P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                           P_DATA           IN OUT HRD_INFO_TBL,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for locking of
  --             HRD.INFORMATION.
  /******************************************************************************/
  /*
  PROCEDURE P_EMP_INFO_LCK(P_DATA       IN OUT HRD_INFO_TBL,
                           P_STOP       OUT VARCHAR2,
                           P_ALERT_TEXT OUT VARCHAR2);*/
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for checking data validations of
  --             HRD.INFORMATION.
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                           P_DATA            IN HRD_INFO,
                           P_STOP            OUT VARCHAR2,
                           P_ALERT_TEXT      OUT VARCHAR2);

  FUNCTION F_EMP_MACHINES_QY(P_MACHINE_ID   IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                             P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                             P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                             P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                             P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                             P_MRNO         IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                             P_ACTIVE       IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                             P_RFID_CODE    IN HRD.INFORMATION.RFID_CODE%TYPE)
    RETURN EMP_MACHINES_TL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for querying data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID   IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                              P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                              P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                              P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                              P_MRNO         IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_ACTIVE       IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE    IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_DATA         IN OUT EMP_MACHINES_TL,
                              P_STOP         OUT VARCHAR2,
                              P_ALERT_TEXT   OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for checking data validations of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for inserting data in
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for locking data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for updating data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for deleting data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-SEP-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to get rfid code against emp mrno.
  /******************************************************************************/

  FUNCTION f_get_rfid_code(P_MRNO IN VARCHAR2) return varchar;
  /******************************************************************************/
  -- Author    : MAHBOOB ALAM (6579)
  -- Created on: 04-11-2015
  -- Scope     : RFID MACHINES FOR SUPER CARD
  /******************************************************************************/
  PROCEDURE P_SUPER_CARD_MACHINE_INS(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                     P_EVENT      IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                                     P_STOP       OUT CHAR,
                                     P_ALERT_TEXT OUT VARCHAR2);
  /**************************************************************************/
  FUNCTION F_IS_CONFIDENTIAL(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /**************************************************************************/
PROCEDURE P_REVOKE_SUP_CARD_ACCESS(P_MRNO        IN VARCHAR2,
                                     P_OBJECT_CODE IN VARCHAR2,
                                     P_STOP        OUT CHAR,
                                     P_ALERT_TEXT  OUT VARCHAR2);
  /**************************************************************************/

END PKG_MACHINE_WISE_EMPLOYEE;
```

#### RFID.PKG_RFID
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID IS

  ----------------------------------------------------------------------
  TYPE RFID_MACHINE_RECORD IS RECORD(
    MACHINE_ID RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    ACCESS_LEVEL CHAR(6));

  ------------------
  -- PL/SQL Array --
  ------------------
  TYPE RFID_MACHINE_TAB IS TABLE OF RFID.PKG_RFID.RFID_MACHINE_RECORD;

  -----------------------------------------------------------------------
  -- Pipelined Function which will return the RFID MACHINES LIST --
  -----------------------------------------------------------------------
  FUNCTION GET_RFID_MACHINES(P_EMP_CODE IN HRD.INFORMATION.MRNO%TYPE)
    RETURN RFID_MACHINE_TAB
    PIPELINED;

END PKG_RFID;
```

#### RFID.PKG_RFID_ACCESS_SYNC
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_ACCESS_SYNC AS

  PROCEDURE LOG_EVENT
  (
      P_RUN_ID              IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE,
      P_EVENT_TYPE          IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE,
      P_EVENT_SOURCE        IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE,
      P_MRNO                IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE,
      P_MACHINE_ID          IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE,
      P_EMP_LOCATION_ID     IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID       IN RFID.RFID_ACCESS_SYNC_LOG.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID      IN RFID.RFID_ACCESS_SYNC_LOG.DESIGNATION_ID%TYPE,
      P_SEX_ID              IN RFID.RFID_ACCESS_SYNC_LOG.SEX_ID%TYPE,
      P_RFID_SUPER_CARD     IN RFID.RFID_ACCESS_SYNC_LOG.RFID_SUPER_CARD%TYPE,
      P_MACHINE_ACCESS_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ACCESS_TYPE%TYPE,
      P_ACCESS_GRANT_EVENT  IN RFID.RFID_ACCESS_SYNC_LOG.ACCESS_GRANT_EVENT%TYPE,
      P_REMARKS             IN RFID.RFID_ACCESS_SYNC_LOG.REMARKS%TYPE,
      P_OLD_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.OLD_ROW_JSON%TYPE,
      P_NEW_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.NEW_ROW_JSON%TYPE
  );

  PROCEDURE GET_EMP_CONTEXT
  (
      P_MRNO             IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_LOCATION_ID      OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID    OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID   OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
      P_RFID_SUPER_CARD  OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
      P_SEX_ID           OUT REGISTRATION.PATIENT.SEX_ID%TYPE
  );

  FUNCTION FN_EFFECTIVE_SETUP_RIGHTS
  (
      P_MRNO             IN HRD.VU_INFORMATION.MRNO%TYPE,
      P_LOCATION_ID      IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID    IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID   IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
      P_RFID_SUPER_CARD  IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
      P_SEX_ID           IN REGISTRATION.PATIENT.SEX_ID%TYPE
  ) RETURN RFID.TAB_SETUP_RIGHT PIPELINED;

  PROCEDURE PR_PREVIEW_EMPLOYEE_SYNC
  (
      P_MRNO               IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_MISSING_IN_MWE     OUT SYS_REFCURSOR,
      P_MWE_MINUS_SETUP    OUT SYS_REFCURSOR
  );

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS
  (
      P_MRNO           IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_DO_COMMIT      IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID         OUT NUMBER --RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS_FAST
  (
      P_MRNO           IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_DO_COMMIT      IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID         OUT NUMBER --RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

  PROCEDURE PR_SYNC_LOCATION_ACCESS
  (
      P_EMP_LOCATION_ID IN  HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL,
      P_DO_COMMIT       IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID          OUT NUMBER -- RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

PROCEDURE PR_CLEANUP_REDUNDANT_RFID_SETUP
(
    P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,   -- NULL = all active employee locations
    P_COMMIT          IN VARCHAR2 DEFAULT 'Y'     -- Y/N
);



END PKG_RFID_ACCESS_SYNC;
```

#### RFID.PKG_RFID_ACCESS_SYNC01
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_ACCESS_SYNC01 AS

  PROCEDURE LOG_EVENT(P_RUN_ID              IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE,
                      P_EVENT_TYPE          IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE,
                      P_EVENT_SOURCE        IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE,
                      P_MRNO                IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE,
                      P_MACHINE_ID          IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE,
                      P_EMP_LOCATION_ID     IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE,
                      P_DEPARTMENT_ID       IN RFID.RFID_ACCESS_SYNC_LOG.DEPARTMENT_ID%TYPE,
                      P_DESIGNATION_ID      IN RFID.RFID_ACCESS_SYNC_LOG.DESIGNATION_ID%TYPE,
                      P_SEX_ID              IN RFID.RFID_ACCESS_SYNC_LOG.SEX_ID%TYPE,
                      P_RFID_SUPER_CARD     IN RFID.RFID_ACCESS_SYNC_LOG.RFID_SUPER_CARD%TYPE,
                      P_MACHINE_ACCESS_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ACCESS_TYPE%TYPE,
                      P_ACCESS_GRANT_EVENT  IN RFID.RFID_ACCESS_SYNC_LOG.ACCESS_GRANT_EVENT%TYPE,
                      P_REMARKS             IN RFID.RFID_ACCESS_SYNC_LOG.REMARKS%TYPE,
                      P_OLD_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.OLD_ROW_JSON%TYPE,
                      P_NEW_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.NEW_ROW_JSON%TYPE);

  PROCEDURE GET_EMP_CONTEXT(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                            P_LOCATION_ID     OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
                            P_DEPARTMENT_ID   OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
                            P_DESIGNATION_ID  OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
                            P_RFID_SUPER_CARD OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                            P_SEX_ID          OUT REGISTRATION.PATIENT.SEX_ID%TYPE);

  FUNCTION FN_EFFECTIVE_SETUP_RIGHTS(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                                     P_LOCATION_ID     IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
                                     P_DEPARTMENT_ID   IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
                                     P_DESIGNATION_ID  IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
                                     P_RFID_SUPER_CARD IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                                     P_SEX_ID          IN REGISTRATION.PATIENT.SEX_ID%TYPE)
    RETURN RFID.TAB_SETUP_RIGHT
    PIPELINED;

  PROCEDURE PR_PREVIEW_EMPLOYEE_SYNC(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                                     P_MISSING_IN_MWE  OUT SYS_REFCURSOR,
                                     P_MWE_MINUS_SETUP OUT SYS_REFCURSOR);

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS(P_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                    P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y',
                                    P_RUN_ID    OUT NUMBER);

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS_FAST(P_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                         P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y',
                                         P_RUN_ID    OUT NUMBER);

  PROCEDURE PR_SYNC_LOCATION_ACCESS(P_EMP_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL,
                                    P_DO_COMMIT       IN VARCHAR2 DEFAULT 'Y',
                                    P_RUN_ID          OUT NUMBER);

  ------------------------------------------------------------------
  -- NEW CLEANUP & PREVIEW PROCEDURES
  ------------------------------------------------------------------

  PROCEDURE PR_PREVIEW_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                             P_RESULT          OUT SYS_REFCURSOR);

  PROCEDURE PR_PREVIEW_REDUNDANT_RFID_ACCESS_SUMMARY(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                                     P_RESULT          OUT SYS_REFCURSOR);

  PROCEDURE PR_CLEANUP_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                             P_COMMIT          IN VARCHAR2 DEFAULT 'Y');

END PKG_RFID_ACCESS_SYNC01;
```

#### RFID.PKG_RFID_CARD_ISSUE_ACS
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_CARD_ISSUE_ACS AS

  /******************************************************************************/
  -- Author    : AQIB KHALID (7346)
  -- Created on: 30-JAN-2024
  -- Purpose   : RFID.PKG_RFID_CARD_ISSUE_ACS.
  /******************************************************************************/

  PROCEDURE P_RFID_CARD_ISSUE(P_EVENT               IN CHAR,
                              P_SR                  IN RFID.RFID_CARD_ISSUE_ACS.SR%TYPE,
                              P_RFID_CARD_NO        IN RFID.RFID_CARD_ISSUE_ACS.RFID_CARD_NO%TYPE,
                              P_NAME                IN RFID.RFID_CARD_ISSUE_ACS.NAME%TYPE,
                              P_MRNO                IN RFID.RFID_CARD_ISSUE_ACS.MRNO%TYPE,
                              P_ISSUE_DATE          IN RFID.RFID_CARD_ISSUE_ACS.ISSUE_DATE%TYPE,
                              P_RECEIVE_DATE        IN RFID.RFID_CARD_ISSUE_ACS.RECEIVE_DATE%TYPE,
                              P_RETURN              IN RFID.RFID_CARD_ISSUE_ACS.RETURN%TYPE,
                              P_CARD_CATEGORY_ID    IN RFID.RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE,
                              P_machine_CATEGORY_ID IN RFID.RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY_ID%TYPE,
                              P_ISSUED_BY           IN RFID.RFID_CARD_ISSUE_ACS.ISSUED_BY%TYPE,
                              P_REMARKS             IN RFID.RFID_CARD_ISSUE_ACS.REMARKS%TYPE,
                              P_NIC                 IN RFID.RFID_CARD_ISSUE_ACS.NIC%TYPE,
                              P_RELATION_ID         IN RFID.RFID_CARD_ISSUE_ACS.RELATION_ID%TYPE,
                              P_ADDRESS             IN RFID.RFID_CARD_ISSUE_ACS.ADDRESS%TYPE,
                              P_CONTACT_NO          IN RFID.RFID_CARD_ISSUE_ACS.CONTACT_NO%TYPE,
                              P_RETURN_DATE         IN RFID.RFID_CARD_ISSUE_ACS.RETURN_DATE%TYPE,
                              P_CARD_DESC           IN RFID.RFID_CARD_ISSUE_ACS.CARD_DESC%TYPE,
                              P_LOCATION_ID         IN VARCHAR2,
                              P_STOP                OUT VARCHAR2,
                              P_ALERT_TEXT          OUT VARCHAR2);

  PROCEDURE JOB_RFID_CARD_RIGHTS_ACS(P_MRNO                IN VARCHAR2 DEFAULT NULL,
                                     P_MACHINE_CATEGORY_ID IN NUMBER DEFAULT NULL);
END PKG_RFID_CARD_ISSUE_ACS;
```

#### RFID.PKG_RFID_DATA_TRANSFER
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_DATA_TRANSFER AS

  TYPE V_RFID_REC IS RECORD(
    MACHINE_CODE  RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
    IP_ADDRESS    RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
    PORT_NO       RFID.RFID_DATA_TRANSFER.PORT_NO%TYPE,
    MRNO          RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
    USER_NAME     RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
    USER_PASSWORD RFID.RFID_DATA_TRANSFER.USER_PASSWORD%TYPE,
    PRIVILEGE     RFID.RFID_DATA_TRANSFER.PRIVILEGE%TYPE,
    ENABLED       RFID.RFID_DATA_TRANSFER.ENABLED%TYPE,
    RFID_CARD_NO  RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
    MACHINE_NAME  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    MACHINE_TYPE  RFID.RFID_MACHINES.MACHINE_TYPE%TYPE--- COLUMN ADDED BY ASMA HASHMI (6-4806) DATED 30-03-2015 11:40AM
    );

  TYPE V_RFID_TBL IS TABLE OF V_RFID_REC INDEX BY PLS_INTEGER;
  TYPE V_RFID_TBL_PF IS TABLE OF V_RFID_REC; /* FOR PIPLINED FUNCTION */

  FUNCTION F_V_RFID_QRY(P_MRNO         IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
                        P_USER_NAME    IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                        P_RFID_CODE    IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                        P_IP_ADDRESS   IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                        P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE)
    RETURN V_RFID_TBL_PF
    PIPELINED;

  PROCEDURE P_V_RFID_QRY(P_MRNO         IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
                         P_USER_NAME    IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                         P_RFID_CODE    IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                         P_IP_ADDRESS   IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                         P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
                         P_DATA         IN OUT V_RFID_TBL,
                         P_STOP         OUT VARCHAR2,
                         P_ALERT_TEXT   OUT VARCHAR2);

  PROCEDURE P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                         P_DATA            IN V_RFID_REC,
                         P_STOP            OUT VARCHAR2,
                         P_ALERT_TEXT      OUT VARCHAR2);

  PROCEDURE P_V_RFID_INS(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_LCK(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_UPD(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_DEL(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

END;
```

#### RFID.PKG_S07FRM00031
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S07FRM00031 AS

  TYPE V_RFID_REC IS RECORD(
    MACHINE_CODE         RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
    IP_ADDRESS           RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
    PORT_NO              RFID.RFID_DATA_TRANSFER.PORT_NO%TYPE,
    MACHINE_IDENTIFIER   RFID.RFID_DATA_TRANSFER.MACHINE_IDENTIFIER%TYPE,
    USER_NAME            RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
    USER_PASSWORD        RFID.RFID_DATA_TRANSFER.USER_PASSWORD%TYPE,
    PRIVILEGE            RFID.RFID_DATA_TRANSFER.PRIVILEGE%TYPE,
    ENABLED              RFID.RFID_DATA_TRANSFER.ENABLED%TYPE,
    RFID_CARD_NO         RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
    MACHINE_NAME         RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    MACHINE_TYPE         RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
    COMPLETE_MRNO        RFID.RFID_DATA_TRANSFER.COMPLETE_MRNO%TYPE,
    RFID_ATTENDANCE_TYPE RFID.RFID_DATA_TRANSFER.RFID_ATTENDANCE_TYPE%TYPE);

  TYPE V_RFID_REC_CUR IS REF CURSOR RETURN V_RFID_REC;
  TYPE V_RFID_TBL IS TABLE OF V_RFID_REC INDEX BY PLS_INTEGER;

  PROCEDURE P_V_RFID_QRY(P_MRNO               IN HRD.V_INFORMATION.MRNO%TYPE,
                         P_USER_NAME          IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                         P_RFID_CODE          IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                         P_IP_ADDRESS         IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                         P_MACHINE_CODE       IN RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
                         P_MACHINE_IDENTIFIER IN RFID.RFID_DATA_TRANSFER.MACHINE_IDENTIFIER%TYPE,
                         P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                         P_DATA               IN OUT V_RFID_REC_CUR,
                         P_STOP               OUT VARCHAR2,
                         P_ALERT_TEXT         OUT VARCHAR2);

  PROCEDURE P_V_RFID_INS(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_LCK(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_UPD(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_DEL(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);
  /**********************************************************************************************/

  PROCEDURE P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                         P_DATA            IN V_RFID_REC,
                         P_STOP            OUT VARCHAR2,
                         P_ALERT_TEXT      OUT VARCHAR2);
END;
```

#### RFID.PKG_S48FRM00024
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00024 AS

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.RFID_MACHINES
  /******************************************************************************/

  /*add by Mahboob Alam */
  TYPE RFID_MACHINES_REC IS RECORD(
    MACHINE_ID   RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    ACTIVE       RFID.RFID_MACHINES.ACTIVE%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO      RFID.RFID_MACHINES.PORT_NO%TYPE,
    ORDER_BY     RFID.RFID_MACHINES.ORDER_BY%TYPE,
    CATEGORY_ID  RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  -----------------------------------------------------------------------
  TYPE RFID_MACHINES_REC_REFCUR IS REF CURSOR RETURN RFID_MACHINES_REC;
  ----------------------------------------------------------------------
  PROCEDURE P_RFID_MACHINES_QRY(P_DATA         IN OUT RFID_MACHINES_REC_REFCUR,
                                P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                                P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                                P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                 P_STOP         OUT VARCHAR2,
                                 P_ALERT_TEXT   OUT VARCHAR2,
                                P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_INS(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/

  -------------------------------------------------------------------------------------
  /* ADD BY MAHBOOB ALAM*/
  TYPE RFID_DEPT_MACHINES_RC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);
  ------------------------------------------------------------
  TYPE RFID_DEPT_MACHINES_REFCUR IS REF CURSOR RETURN RFID_DEPT_MACHINES_RC;

  PROCEDURE P_DEPT_MACHINES_QY(P_DATA          IN OUT RFID_DEPT_MACHINES_REFCUR,
                               P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                               P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                               P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                               P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE,
                               P_STOP          OUT VARCHAR2,
                               P_ALERT_TEXT    OUT VARCHAR2

                               );

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_INS(P_MACHINE_ID    OUT RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                                P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_DATA          IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP          OUT VARCHAR2,
                                P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_WISE_EMPLOYEE
  /******************************************************************************/

  /* ADD BY MAHBOOB ALAM*/
  ------------------------------------------------------------------------------
    TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID  RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO        RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    NAME        HRD.V_INFORMATION.NAME%TYPE,
    DISP_MRNO   HRD.V_INFORMATION.DISP_MRNO%TYPE,
    DEPARTMENT  HRD.V_INFORMATION.DEPARTMENT%TYPE,
    DESIGNATION HRD.V_INFORMATION.DESIGNATION%TYPE,
    ACTIVE      RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE   HRD.INFORMATION.RFID_CODE%TYPE);
    ------------------------------------------------------------------------
  TYPE RFID_EMP_MACHINES_REFCUR IS REF CURSOR RETURN EMP_MACHINES_RC;
  -------------------------------------------------------------------------
  PROCEDURE P_EMP_MACHINES_QY(P_DATA        IN OUT RFID_EMP_MACHINES_REFCUR,
                              P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                              P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                              P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                              P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                              P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE ,
                             P_STOP        OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2
                             );

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  TYPE RFID_CATEGORY_REC IS RECORD(
    CATEGORY_ID       RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
    DESCRIPTION       RFID.RFID_CATEGORY.DESCRIPTION%TYPE,
    SHORT_DESCRIPTION RFID.RFID_CATEGORY.SHORT_DESCRIPTION%TYPE,
    IS_DEFAULT        RFID.RFID_CATEGORY.IS_DEFAULT%TYPE,
    ACTIVE            RFID.RFID_CATEGORY.ACTIVE%TYPE);
  TYPE RFID_CATEGORY_TBL IS TABLE OF RFID_CATEGORY_REC INDEX BY PLS_INTEGER;
  TYPE RFID_CATEGORY_CUR IS REF CURSOR RETURN RFID_CATEGORY_REC;
  /******************************************************************************/
  PROCEDURE P_RFID_CATEGORY_QRY(P_DATA        IN OUT RFID_CATEGORY_CUR,
                                P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
                                P_DESCRIPTION IN RFID.RFID_CATEGORY.DESCRIPTION%TYPE,
                                P_SHORT_DESC  IN RFID.RFID_CATEGORY.SHORT_DESCRIPTION%TYPE,
                                P_DEFAULT     IN RFID.RFID_CATEGORY.IS_DEFAULT%TYPE,
                                P_ACTIVE      IN RFID.RFID_CATEGORY.ACTIVE%TYPE);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_INSERT(R            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_LOCK(R            IN OUT RFID_CATEGORY_TBL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_UPDATE(T            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_DELETE(T            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  TYPE RFID_DESIGNATION_REC IS RECORD(
    DESIGNATION_ID DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
    DESCRIPTION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    CATEGORY_ID    RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  TYPE RFID_DESIGNATION_CUR IS REF CURSOR RETURN RFID_DESIGNATION_REC;
  /******************************************************************************/
  PROCEDURE RFID_DESIGNATION_QRY(P_DATA           IN OUT RFID_DESIGNATION_CUR,
                                 P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                 P_DESCRIPTION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                                 P_CATEGORY_ID    IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  /******************************************************************************/

END PKG_S48FRM00024;
```

#### RFID.PKG_S48FRM00025
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00025 AS

  TYPE HRD_INFO IS RECORD(
    DESIGNATION_ID HRD.INFORMATION.DESIGNATION_ID%TYPE,
    MRNO           HRD.INFORMATION.MRNO%TYPE,
    DISP_MRNO      VARCHAR2(11),
    NAME           REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT     DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DEPARTMENT_ID  DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    JOINING_DATE   HRD.INFORMATION.JOINING_DATE%TYPE,
    RFID_CODE      HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE HRD_INFO_TBL IS TABLE OF HRD_INFO INDEX BY PLS_INTEGER;
  TYPE HRD_INFO_TBL_PF IS TABLE OF HRD_INFO; /* FOR PIPLINED FUNCTION */
  TYPE HRD_INFO_REFCUR IS REF CURSOR RETURN HRD_INFO;
  /***************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID           RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    DESCRIPTION          RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC           RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    MACHINE_CODE         RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS           RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    MRNO                 RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE               RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE            HRD.INFORMATION.RFID_CODE%TYPE,
    MACHINE_INDENTIFIER  RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
    RFID_ATTENDANCE_TYPE RFID.MACHINE_WISE_EMPLOYEE.RFID_ATTENDANCE_TYPE%TYPE,
    MARK_ATTENDANCE      RFID.MACHINE_WISE_EMPLOYEE.MARK_ATTENDANCE%TYPE,
    machine_access_type  VARCHAR2(300));

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  TYPE EMP_MACHINE_REFCUR IS REF CURSOR RETURN EMP_MACHINES_RC;
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_QRY(P_DATA           IN OUT HRD_INFO_REFCUR,
                           P_designation_id IN hrd.information.designation_id%TYPE,
                           P_MRNO           IN hrd.information.mrno%TYPE,
                           P_DISP_MRNO      IN VARCHAR2,
                           P_NAME           IN registration.patient.name%TYPE,
                           P_designation    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                           P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                           P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : HRD.INFORMATION
  -- Purpose   : This procedure will be used for locking data of
  --             HRD.INFORMATION.
  /******************************************************************************/

  /*  PROCEDURE P_EMP_INFO_LCK(P_DATA       IN OUT rfid.PKG_machine_wise_employee.HRD_INFO_TBL,
  P_STOP       OUT VARCHAR2,
  P_ALERT_TEXT OUT VARCHAR2);*/

  /******************************************************************************/

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_WISE_EMPLOYEE
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_DESCRIPTION         IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                              P_SHORT_DESC          IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                              P_MACHINE_CODE        IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                              P_IP_ADDRESS          IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                              P_MRNO                IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_ACTIVE              IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE           IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                              P_DATA                IN OUT EMP_MACHINE_REFCUR,
                              P_STOP                OUT VARCHAR2,
                              P_ALERT_TEXT          OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/
  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /************************************************************************************/
  PROCEDURE P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                           P_DATA            IN HRD_INFO,
                           P_STOP            OUT VARCHAR2,
                           P_ALERT_TEXT      OUT VARCHAR2);
  /**************************************************************************************/
  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);
  /**********************************************************************************/
  FUNCTION f_get_rfid_code(p_mrno IN VARCHAR2) return varchar;
  /******************************************************************************/
  FUNCTION F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO       IN VARCHAR2,
                                          P_MACHINE_ID IN VARCHAR2)
    RETURN NUMBER;

END PKG_S48FRM00025;
```

#### RFID.PKG_S48FRM00060
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00060 AS
  ----------------------------------------------------------
  TYPE RFID_MACHINE_MAPPING_RECORD IS RECORD(
    ORGANIZATION_ID    DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    MACHINE_ID         RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    MACHINE_NAME       RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    IP_ADDRESS         RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO            RFID.RFID_MACHINES.PORT_NO%TYPE,
    RFID_CARD_NO       HRD.INFORMATION.RFID_CODE%TYPE,
    MACHINE_TYPE       RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
    MACHINE_IDENTIFIER RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
    ORIGINAL_MRNO      HRD.VU_INFORMATION.MRNO%TYPE,
    EMPLOYEE_NAME      HRD.VU_INFORMATION.NAME%TYPE);

  TYPE RFID_MACHINE_MAPPING_CUR IS REF CURSOR RETURN RFID_MACHINE_MAPPING_RECORD;

  PROCEDURE RFID_MACHINE_MAPPING_QY(Q_DATA               IN OUT RFID_MACHINE_MAPPING_CUR,
                                    P_MACHINE_ID         IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                    P_MACHINE_NAME       IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                    P_IP_ADDRESS         IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                    P_PORT_NO            IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                    P_RFID_CARD_NO       IN HRD.INFORMATION.RFID_CODE%TYPE,
                                    P_MACHINE_TYPE       IN RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
                                    P_MACHINE_IDENTIFIER IN RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
                                    P_ORIGINAL_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                    P_EMPLOYEE_NAME      IN HRD.VU_INFORMATION.NAME%TYPE,
                                    P_STOP               OUT VARCHAR2,
                                    P_ALERT_TEXT         OUT VARCHAR2);

END;
```

#### RFID.PKG_S48FRM00100
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00100 AS

  /******************************************************************************/
  -- Author    : Irfan Ali
  -- Created on: 16-NOV-2023
  -- Purpose   : RFID MACHINES GRANT AND REVOKE RIGHTS
  /******************************************************************************************/

  PROCEDURE P_RFID_CATEGORY_WISE_RIGHTS(P_CATEGORY_ID         IN NUMBER,
                                        P_DESIGNATION_ID      IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                        P_EVENT               IN VARCHAR2,
                                        P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                        P_MACHINE_ACCESS_TYPE IN CHAR,
                                        P_STOP                OUT CHAR,
                                        P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/

  PROCEDURE P_RFID_CATEGORY_REVOKE_RIGHTS(P_CATEGORY_ID         IN NUMBER,
                                          P_DESIGNATION_ID      IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                          P_EVENT               IN VARCHAR2,
                                          P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                          P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                          P_MACHINE_ACCESS_TYPE IN CHAR,
                                          P_STOP                OUT CHAR,
                                          P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/
END PKG_S48FRM00100;
```

### Standalone procedures and functions (headers)

#### RFID.F_GET_MRNO (function)
```sql
CREATE OR REPLACE FUNCTION RFID.F_GET_MRNO(P_RFID_CODE HRD.INFORMATION.RFID_CODE%TYPE)
  RETURN VARCHAR2
--AUTHOR:           Muhammad Farhan (TSE) 7098
  --SUPPERVISED BY: Sir Shahzad Farooq (TL), Mahboob Alam (SE)
  --QA BY:          Junaid Mahmood (SQA)
  --DESCRIPTION:    Return MRNO against RFID code
  --AS
```

#### RFID.PR_CLEANUP_REDUNDANT_RFID_ACCESS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.PR_CLEANUP_REDUNDANT_RFID_ACCESS
(
    P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,   -- NULL = all active employee locations
    P_COMMIT          IN VARCHAR2 DEFAULT 'Y'     -- Y/N
)
AS
```

#### RFID.PR_RFID_ACCESS_DIFFS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.PR_RFID_ACCESS_DIFFS(P_MRNO                            IN VARCHAR2,
                                                      P_LOCATION_WISE_MINUS_COMPLETE    OUT SYS_REFCURSOR, --1
                                                      P_DEPARTMENT_WISE_MINUS_COMPLETE  OUT SYS_REFCURSOR, --2
                                                      P_DESIGNATION_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, --3
                                                      P_EMPLOYEE_WISE_MINUS_COMPLETE    OUT SYS_REFCURSOR, --4
                                                      P_SETUP_MINUS_COMPLETE            OUT SYS_REFCURSOR, --5
                                                      P_COMPLETE_MINUS_SETUP            OUT SYS_REFCURSOR --6

                                                      ) AS
```

#### RFID.P_COPY_MACHINE_RIGHTS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.P_COPY_MACHINE_RIGHTS(P_MRNO        IN VARCHAR2,
                                                       P_MASTER_MRNO IN VARCHAR2,
                                                       P_MACHINE_ID  IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                                       P_STOP        OUT CHAR,
                                                       P_ALERT_TEXT  OUT VARCHAR) IS
```



# PART: Synonyms

| Synonym | Target |
|---|---|
| SYN_ATTENDANCE_EMPLOYEE | RFID_AUDIT.ATTENDANCE_EMPLOYEE |
| SYN_DEPT_WISE_DESIG_ACCESS | RFID_AUDIT.DEPT_WISE_DESIG_ACCESS |
| SYN_MACHINE_WISE_COUNTER | RFID_AUDIT.MACHINE_WISE_COUNTER |
| SYN_MACHINE_WISE_EMPLOYEE | RFID_AUDIT.MACHINE_WISE_EMPLOYEE |
| SYN_MAC_COMP_DEPARTMENT | RFID_AUDIT.MACHINE_COMPLETE_DEPARTMENT |
| SYN_RFID_ACCESS_DEPARTMENT | RFID_AUDIT.RFID_ACCESS_DEPARTMENT |
| SYN_RFID_ACL_ADMIN | RFID_AUDIT.RFID_ACL_ADMIN |
| SYN_RFID_CARDS | RFID_AUDIT.RFID_CARDS |
| SYN_RFID_CARDS_ACS | RFID_AUDIT.RFID_CARDS_ACS |
| SYN_RFID_CARD_CATEGORY_ACS | RFID_AUDIT.RFID_CARD_CATEGORY_ACS |
| SYN_RFID_CARD_ISSUE_ACS | RFID_AUDIT.RFID_CARD_ISSUE_ACS |
| SYN_RFID_CARD_TYPE | RFID_AUDIT.RFID_CARD_TYPE |
| SYN_RFID_CATEGORY | RFID_AUDIT.RFID_CATEGORY |
| SYN_RFID_CATEGORY_DEPARTMENTS | RFID_AUDIT.RFID_CATEGORY_DEPARTMENTS |
| SYN_RFID_CATEGORY_MACHINES | RFID_AUDIT.RFID_CATEGORY_MACHINES |
| SYN_RFID_CATEGORY_MACHINES_ACS | RFID_AUDIT.RFID_CATEGORY_MACHINES_ACS |
| SYN_RFID_CAT_TR_ACS | RFID_AUDIT.RFID_CATEGORY_TIMERANGE_ACS |
| SYN_RFID_CONFIDENTIAL_Q | RFID_AUDIT.RFID_CONFIDENTIAL_Q |
| SYN_RFID_CONFI_MACHINE_RIGHTS | RFID_AUDIT.RFID_CONFI_MACHINE_RIGHTS |
| SYN_RFID_DATA_TRANSFER | RFID_AUDIT.RFID_DATA_TRANSFER |
| SYN_RFID_DEFAULT_ACCESS | RFID_AUDIT.RFID_DEFAULT_ACCESS |
| SYN_RFID_DEPT_GENERAL_ACCESS | RFID_AUDIT.RFID_DEPT_GENERAL_ACCESS |
| SYN_RFID_DESIG_WISE_SP_ACCESS | RFID_AUDIT.RFID_DESIG_WISE_SP_ACCESS |
| SYN_RFID_EMP_WISE_SP_ACCESS | RFID_AUDIT.RFID_EMP_WISE_SP_ACCESS |
| SYN_RFID_MACHINES | RFID_AUDIT.RFID_MACHINES |
| SYN_RFID_MACHINES_DATA | RFID_AUDIT.RFID_MACHINES_DATA |
| SYN_RFID_MACHINE_CATEGORY_ACS | RFID_AUDIT.RFID_MACHINE_CATEGORY_ACS |
| SYN_RFID_MACH_IDENT_MAPING | RFID_AUDIT.RFID_MACHIN_IDENTIFIER_MAPPING |
| SYN_SECTION_WISE_ATTENDANCE | RFID_AUDIT.SECTION_WISE_ATTENDANCE |
| SYN_TEMP_CARD_SETUP | RFID_AUDIT.TEMP_CARD_SETUP |
| SYN_TRAINING_ATTENDANCE_STG | RFID_AUDIT.TRAINING_ATTENDANCE_STG |
