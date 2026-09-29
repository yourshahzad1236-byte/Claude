# RFID schema

_Generated from `RFID_SCHEMA.txt` by `tools/parse_schema.py`. Do not edit by hand — re-run the script._

## Summary

| Object type | Count |
|---|---|
| Tables | 43 |
| Views | 15 |
| Sequences | 5 |
| Packages | 15 |
| Procedures | 3 |
| Functions | 1 |
| Triggers | 104 |
| Types | 2 |
| Synonyms | 31 |
| Foreign keys | 20 |

### Cross-schema foreign-key dependencies

- **DEFINITIONS**: `DEFINITIONS.DEPARTMENT`, `DEFINITIONS.DESIGNATION`, `DEFINITIONS.SEX`
- **HRD**: `HRD.INFORMATION`
- **SECURITY**: `SECURITY.USERS`

## Tables

| Table | Cols | PK | Description |
|---|---|---|---|
| [ATTENDANCE](#attendance) | 19 |  |  |
| [ATTENDANCE_EMPLOYEE](#attendance_employee) | 16 | SR_NO |  |
| [ATTENDANCE_INCORRECT](#attendance_incorrect) | 18 |  | This table is used to store failed insertions of RFID.RFID_ATTENDANCE table, mainly due to incorrect date and time. |
| [DEPT_WISE_DESIG_ACCESS](#dept_wise_desig_access) | 9 | DEPARTMENT_ID, DESIGNATION_ID |  |
| [MACHINE_TYPE](#machine_type) | 14 | MACHINE_TYPE |  |
| [RFID_CATEGORY](#rfid_category) | 18 | CATEGORY_ID |  |
| [RFID_MACHINES](#rfid_machines) | 43 | MACHINE_ID |  |
| [MACHINE_COMPLETE_DEPARTMENT](#machine_complete_department) | 14 | MACHINE_ID, DEPARTMENT_ID |  |
| [MACHINE_WISE_COUNTER](#machine_wise_counter) | 13 | MACHINE_ID |  |
| [MACHINE_WISE_EMPLOYEE](#machine_wise_employee) | 19 | MACHINE_ID, MRNO |  |
| [RFID_ACCESS_DEPARTMENT](#rfid_access_department) | 9 | DEPARTMENT_ID |  |
| [RFID_ACCESS_SYNC_LOG](#rfid_access_sync_log) | 18 |  |  |
| [RFID_ACL_ADMIN](#rfid_acl_admin) | 14 | MRNO, PRIVILEGE_LEVEL |  |
| [RFID_CARD_TYPE](#rfid_card_type) | 15 | CARD_TYPE_ID |  |
| [RFID_CARDS](#rfid_cards) | 15 | RFID_CARD_NO |  |
| [RFID_CARDS_ACS](#rfid_cards_acs) | 10 | RFID_CARD_NO |  |
| [RFID_CARD_CATEGORY_ACS](#rfid_card_category_acs) | 16 | CARD_CATEGORY_ID, LOCATION_ID |  |
| [RFID_CARD_ISSUE_ACS](#rfid_card_issue_acs) | 33 | SR, CARD_CATEGORY_ID, MRNO, LOCATION_ID |  |
| [RFID_CARD_ISSUE_RECORD](#rfid_card_issue_record) | 21 | SR, CARD_TYPE_ID |  |
| [RFID_CATEGORY_DEPARTMENTS](#rfid_category_departments) | 12 | CATEGORY_ID, DEPARTMENT_ID |  |
| [RFID_CATEGORY_MACHINES](#rfid_category_machines) | 13 | MACHINE_ID, CATEGORY_ID |  |
| [RFID_CATEGORY_MACHINES_ACS](#rfid_category_machines_acs) | 10 | MACHINE_ID, CATEGORY_ID |  |
| [RFID_CATEGORY_TIMERANGE_ACS](#rfid_category_timerange_acs) | 11 | CARD_CATEGORY_ID, SR_NO |  |
| [RFID_CONFIDENTIAL_Q](#rfid_confidential_q) | 13 | CHECK_TIME, MACHINE_IDENTIFIER, MACHINE_ID |  |
| [RFID_CONFIDENTIAL_Q_HIS](#rfid_confidential_q_his) | 8 |  |  |
| [RFID_CONFI_MACHINE_RIGHTS](#rfid_confi_machine_rights) | 9 | MRNO, MACHINE_ID |  |
| [RFID_DATA_TRANSFER](#rfid_data_transfer) | 23 | MACHINE_CODE, MACHINE_IDENTIFIER, PRIVILEGE, ENABLED |  |
| [RFID_DEFAULT_ACCESS](#rfid_default_access) | 11 | MACHINE_ID, LOCATION_ID |  |
| [RFID_DELETED_ACCESS_AUDIT](#rfid_deleted_access_audit) | 13 |  |  |
| [RFID_DEPT_GENERAL_ACCESS](#rfid_dept_general_access) | 9 | DEPARTMENT_ID, MACHINE_ID |  |
| [RFID_DESIG_WISE_SP_ACCESS](#rfid_desig_wise_sp_access) | 10 | DESIGNATION_ID, MACHINE_ID, DEPARTMENT_ID |  |
| [RFID_DOORS_LOG](#rfid_doors_log) | 7 |  | This table is used to log door status which are opened manually. |
| [RFID_EMP_WISE_SP_ACCESS](#rfid_emp_wise_sp_access) | 9 | MRNO, MACHINE_ID |  |
| [RFID_MACHINES_DATA](#rfid_machines_data) | 14 |  |  |
| [RFID_MACHINE_CATEGORY_ACS](#rfid_machine_category_acs) | 15 |  |  |
| [RFID_MACHINE_COMMAND](#rfid_machine_command) | 11 | ID |  |
| [RFID_MACHINE_TIMESTAMP](#rfid_machine_timestamp) | 15 |  |  |
| [RFID_MACHIN_IDENTIFIER_MAPPING](#rfid_machin_identifier_mapping) | 16 | ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, MACHINE_IDENTIFIER |  |
| [SECTION_WISE_ATTENDANCE](#section_wise_attendance) | 15 | DEPARTMENT_ID, SECTION_ID, MACHINE_ID |  |
| [TEMP_CARD_SETUP](#temp_card_setup) | 10 | CARD_NO |  |
| [TEMP_RFID_REGISTERED_USERS](#temp_rfid_registered_users) | 12 | ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, USER_IDENTIFIER | This table will be used to retrieve registered users of RFID machines on temporary basis. So that fingerprints and RFId cards can be mapped to original users later on. Data in this table is temporary and can be removed if required. |
| [TMP_SELECTED_MACHINES_PR](#tmp_selected_machines_pr) | 2 |  |  |
| [TRAINING_ATTENDANCE_STG](#training_attendance_stg) | 16 |  |  |

### ATTENDANCE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CHECK_TIME** | DATE | Y |  | Timestamp of machine when attendance marked. |
| 2 | **USER_ID** | NUMBER(14) | Y |  | Referred to USER_IDENTIFIER in RFID.RFID_MACHIN_IDENTIFIER_MAPPING |
| 3 | **CHECK_TYPE** | VARCHAR2(20) | Y |  | I: Check In  O: Check Out |
| 4 | **MACHINE_ID** | NUMBER(5) | Y |  | Reffered as MACHINE_CODE in RFID.RFID_ATTENDANCE |
| 5 | **VERIFICATION_MODE** | NUMBER(5) | Y |  | Cardswipe/Password/Biometric |
| 6 | **TRANS_DATE** | DATE | Y | SYSDATE | Default insertion Date |
| 7 | **LOCATION_ID** | VARCHAR2(3) | Y |  | Referred to LOC_ID in RFID.RFID_MACHINES |
| 8 | **IS_EPARKING** | CHAR(1) | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 18 | **REASON** | VARCHAR2(4000) | Y |  |  |
| 19 | **REMARKS** | VARCHAR2(4000) | Y |  |  |

- **Index** `IDX_ATTENDANCE_01` (CHECK_TIME)
- **Index** `IDX_RFID_ATTENDANCE_1` (MACHINE_ID, USER_ID)
- **Triggers**: `ATTENDANCE_INS_CS` (after insert), `CHECK_DATE_TIME` (BEFORE INSERT), `RFID_ATTENDANCE_INSERT` (AFTER INSERT), `RFID_ATTENDANCE_INSERT_EPARK` (AFTER INSERT), `RFID_ATTENDANCE_INSERT_PAT` (AFTER INSERT), `RFID_CONFIDENTIAL_QUEUE_INSERT` (AFTER INSERT)

### ATTENDANCE_EMPLOYEE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CHECK_TIME** | DATE | Y |  |  |
| 2 | **MACHINE_IDENTIFIER** | NUMBER(10) | Y |  |  |
| 3 | **MACHINE_ID** | NUMBER(5) | Y |  |  |
| 4 | **ENTRY_DATE** | DATE | Y |  |  |
| 5 | **REASON** | VARCHAR2(4000) | Y |  |  |
| 6 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **RFID_CODE** | VARCHAR2(50) | Y |  |  |
| 14 | **SERIAL_NO_FOR_CARD_SWIPE** | NUMBER | Y |  | This column will be used in rfid.attendance_employee table to track record of attendance |
| 15 | **MACHINE_DEFAULT_CHECK_IN_OUT** | CHAR(1) | Y |  |  |
| 16 | **SR_NO** 🔑 | VARCHAR2(15) | Y |  |  |

- **Primary key** `ATTENDANCE_EMPLOYEE_PK` (SR_NO)
- **Unique** `ATTENDANCE_EMPLOYEE_UK` (CHECK_TIME, MACHINE_IDENTIFIER, MACHINE_ID)
- **Triggers**: `ATTENDANCE_EMPLOYEE_DEL` (AFTER DELETE), `ATTENDANCE_EMPLOYEE_INS` (BEFORE INSERT), `ATTENDANCE_EMPLOYEE_UPD` (BEFORE UPDATE), `ATTENDANCE_EMP_SEQ_INSERT` (BEFORE INSERT), `TRAINING_ATTENDANCE_STG_INSERT` (AFTER INSERT)

### ATTENDANCE_INCORRECT

This table is used to store failed insertions of RFID.RFID_ATTENDANCE table, mainly due to incorrect date and time.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CHECK_TIME** | DATE | N |  |  |
| 2 | **USER_ID** | NUMBER(14) | N |  |  |
| 3 | **CHECK_TYPE** | VARCHAR2(20) | N |  |  |
| 4 | **MACHINE_ID** | NUMBER(5) | N |  | Reffered to MACHINE_CODE in RFID.RFID_MACHINES |
| 5 | **VERIFICATION_MODE** | NUMBER(5) | Y |  |  |
| 6 | **TRANS_DATE** | DATE | N | SYSDATE |  |
| 7 | **COMMENTS** | VARCHAR2(2000) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  | Referred to LOC_ID in RFID.RFID_MACHINES |
| 9 | **IS_EPARKING** | CHAR(1) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Index** `IDX_RFID_ATTN_INCORRECT_1` (MACHINE_ID, USER_ID)
- **Index** `IDX_RFID_ATTN_INCORRECT_2` (CHECK_TIME)

### DEPT_WISE_DESIG_ACCESS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DEPARTMENT_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 2 | **DESIGNATION_ID** 🔑 → `DEFINITIONS.DESIGNATION` | VARCHAR2(7) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEP_WISE_DESIG_ACCESS` (DEPARTMENT_ID, DESIGNATION_ID)
- **FK** `FK_DEP_WISE_DESIG_ID` (DESIGNATION_ID) → `DEFINITIONS.DESIGNATION` (DESIGNATION_ID)
- **Index** `INDX_DA_DESIG_ID` (DESIGNATION_ID)
- **Referenced by**: `RFID_DESIG_WISE_SP_ACCESS`
- **Triggers**: `DEPT_WISE_DESIG_ACCESS_DEL` (AFTER DELETE), `DEPT_WISE_DESIG_ACCESS_INS` (BEFORE INSERT), `DEPT_WISE_DESIG_ACCESS_UPD` (BEFORE UPDATE)

### MACHINE_TYPE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_TYPE** 🔑 | VARCHAR2(5) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 3 | **SHORT_DESC** | VARCHAR2(255) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_MACHINE_TYPE` (MACHINE_TYPE)
- **Referenced by**: `RFID_MACHINES`

### RFID_CATEGORY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CATEGORY_ID** 🔑 | NUMBER(5) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(50) | Y |  |  |
| 4 | **IS_DEFAULT** | CHAR(1) | Y |  |  |
| 5 | **ACTIVE** | CHAR(1) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 16 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 17 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 18 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |

- **Primary key** `PK_RFID_CATEGORY` (CATEGORY_ID)
- **Referenced by**: `RFID_CATEGORY_MACHINES`, `RFID_MACHINES`
- **Triggers**: `RFID_CATEGORY_DEL` (AFTER DELETE), `RFID_CATEGORY_INS` (BEFORE INSERT), `RFID_CATEGORY_UPD` (BEFORE UPDATE)

### RFID_MACHINES

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(250) | N |  |  |
| 3 | **SHORT_DESC** | VARCHAR2(20) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 5 | **MACHINE_CODE** | VARCHAR2(10) | Y |  |  |
| 6 | **IP_ADDRESS** | VARCHAR2(15) | Y |  |  |
| 7 | **ORDER_BY** | NUMBER(3) | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **PORT_NO** | NUMBER | N | 4370 |  |
| 15 | **CATEGORY_ID** → `RFID.RFID_CATEGORY` | NUMBER(5) | Y |  |  |
| 16 | **STATUS** | CHAR(1) | Y | 'Y' | Y: Must verify machine availability on network, N: Do not verify machine availability on network. |
| 17 | **STATUS_DATE** | DATE | Y |  |  |
| 18 | **MACHINE_TYPE** → `RFID.MACHINE_TYPE` | VARCHAR2(5) | N | 'BW' | Values could be as follows BW/TFT/IFACE depending upon machine specs |
| 19 | **MACHINE_ON_OF** | CHAR(1) | Y | 'Y' | 'Y' IS ON 'N' IS OFF |
| 20 | **IS_SELECT** | CHAR(1) | Y | 'N' |  |
| 21 | **IS_CONFIDENTIAL** | CHAR(1) | Y | 'N' |  |
| 22 | **CAPTURE_PICTURE** | CHAR(1) | N | 'N' | Device can capture and save pictures |
| 23 | **CAPTURE_FINGERPRINT** | CHAR(1) | N | 'N' | Device can capture and save fingerprints |
| 24 | **MACHINE_DIGIT_LIMIT** | NUMBER(2) | Y |  |  |
| 25 | **RFID_CODE_REQUIRED** | CHAR(1) | Y | 'Y' |  |
| 26 | **COMMUNICATION_PASSWORD** | VARCHAR2(6) | Y |  | Password used to connect RFID Machine |
| 27 | **ORG_ID** | VARCHAR2(3) | Y |  | THIS COLUMN CONTAINS ORGANIZATION ID FOR MULTI-LOCATION INFO |
| 28 | **ZON_ID** | VARCHAR2(3) | Y |  | THIS COLUMN CONTAINS ZONE ID FOR MULTI-LOCATION INFO |
| 29 | **LOC_ID** | VARCHAR2(3) | Y |  | THIS COLUMN CONTAINS LOCATION ID FOR MULTI-LOCATION INFO |
| 30 | **ORDER_LOCATION_ID** | VARCHAR2(3) | Y |  | THIS COLUMN CONTAINS THE LOCATION WHERE THE MACHINE IS PHYSICALLY LOCATED |
| 31 | **MARK_ATTENDANCE** | CHAR(1) | Y |  |  |
| 32 | **MACHINE_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 33 | **CAPTURE_IRIS** | CHAR(1) | Y | 'N' | Device can capture and save IRIS features. |
| 34 | **CAPTURE_FACE** | CHAR(1) | Y | 'N' | Device can capture and save face features. |
| 35 | **MACHINE_CATEGORY** | CHAR(1) | Y |  |  |
| 36 | **ATTENDANCE_ALLOWED** | CHAR(1) | Y |  |  |
| 37 | **DEFAULT_CHECK_IN_OUT** | CHAR(1) | Y |  | This column use for default value of the machine in/out. |
| 38 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 39 | **GENDER_ONLY** → `DEFINITIONS.SEX` | NUMBER(1) | Y |  | This column will be use to grant gender wise access on rfid machine null will be for all gender |
| 40 | **TRAINING_ATTENDANCE_MARK** | CHAR(1) | Y | 'N' |  |
| 41 | **DEVICE_SERIAL_NUM** | VARCHAR2(30) | Y |  |  |
| 42 | **CAPTURE_PALM** | CHAR(1) | Y | 'N' | Device can capture and save palm features. |
| 43 | **CONNECTION_STATUS** | NUMBER(1) | N | 0 |  |

- **Primary key** `PK_RFID_MACHINE` (MACHINE_ID)
- **FK** `FK_RFID_MACHINES_1` (CATEGORY_ID) → `RFID.RFID_CATEGORY` (CATEGORY_ID) _DISABLED_
- **FK** `FK_RFID_MACHINES_2` (MACHINE_TYPE) → `RFID.MACHINE_TYPE` (MACHINE_TYPE) _DISABLED_
- **FK** `FK_RFID_MACHINE_3` (GENDER_ONLY) → `DEFINITIONS.SEX` (SEX_ID)
- **Check** `CHK_RFID_MACHINES_CONN_STATUS`: `(CONNECTION_STATUS IN (0, 1))`
- **Check** `CK_RFID_MACHINE`: `(ACTIVE IN ('Y','N'))`
- **Index** `INDX_RFID_MACHINE` (GENDER_ONLY)
- **Referenced by**: `MACHINE_COMPLETE_DEPARTMENT`, `MACHINE_WISE_EMPLOYEE`, `RFID_CATEGORY_MACHINES`, `RFID_DEFAULT_ACCESS`, `RFID_DEPT_GENERAL_ACCESS`, `RFID_DOORS_LOG`, `RFID_MACHINE_TIMESTAMP`
- **Triggers**: `RFID_MACHINES_DEL` (AFTER DELETE), `RFID_MACHINES_INS` (BEFORE INSERT), `RFID_MACHINES_UPD` (BEFORE UPDATE), `RFID_SUPER_CARD_MACHINE_INS` (AFTER INSERT OR UPDATE OR DELETE)

### MACHINE_COMPLETE_DEPARTMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 2 | **DEPARTMENT_ID** 🔑 → `DEFINITIONS.DEPARTMENT` | VARCHAR2(7) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **IS_ATTENDANCE_MARK** | CHAR(1) | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_MACHINE_DEPT` (MACHINE_ID, DEPARTMENT_ID)
- **FK** `FK_MACHINE_DEPT_1` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **FK** `FK_MACHINE_DEPT_2` (DEPARTMENT_ID) → `DEFINITIONS.DEPARTMENT` (DEPARTMENT_ID) _DISABLED_
- **Check** `CK_MACHINE_DEPT_1`: `(ACTIVE IN ('Y','N'))`
- **Referenced by**: `SECTION_WISE_ATTENDANCE`
- **Triggers**: `MAC_COMP_DEPARTMENT_DEL` (AFTER DELETE), `MAC_COMP_DEPARTMENT_INS` (BEFORE INSERT), `MAC_COMP_DEPARTMENT_UPD` (BEFORE UPDATE)

### MACHINE_WISE_COUNTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 2 | **COUNTER** | NUMBER(8) | Y | 1 |  |
| 3 | **MAXIMUM_COUNTER** | NUMBER(8) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 11 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 12 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 13 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_MACHINE_ID` (MACHINE_ID)
- **Triggers**: `MACHINE_WISE_COUNTER_DEL` (AFTER DELETE), `MACHINE_WISE_COUNTER_INS` (BEFORE INSERT), `MACHINE_WISE_COUNTER_UPD` (BEFORE UPDATE)

### MACHINE_WISE_EMPLOYEE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 2 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **ENTRY_TYPE** | VARCHAR2(1) | Y | 'I' |  |
| 11 | **RFID_ATTENDANCE_TYPE** | CHAR(1) | Y |  | 'T' for thumb scan, 'R' for rfid attendance, and 'A' For all |
| 12 | **MARK_ATTENDANCE** | CHAR(1) | Y | 'Y' |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 17 | **MACHINE_ACCESS_TYPE** | VARCHAR2(3) | Y | 'E' | 'E' for employee, 'D' for Designation category wise, 'T' Department Wise 'DAA' DEFAULT ACCES 'DGA' department wise acess, 'DSA' designation wise special access |
| 18 | **OBJECT_CODE** | VARCHAR2(15) | Y |  |  |
| 19 | **ACCESS_GRANT_EVENT** | VARCHAR2(40) | Y |  |  |

- **Primary key** `PK_MACHINE_EMP` (MACHINE_ID, MRNO)
- **FK** `FK_MACHINE_EMP_1` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **FK** `FK_MACHINE_EMP_2` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **Check** `CK_MACHINE_EMP_1`: `(ACTIVE IN ('Y','N'))`
- **Triggers**: `MACHINE_WISE_EMPLOYEE_DEL` (AFTER DELETE), `MACHINE_WISE_EMPLOYEE_INS` (BEFORE INSERT), `MACHINE_WISE_EMPLOYEE_UPD` (BEFORE UPDATE)

### RFID_ACCESS_DEPARTMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DEPARTMENT_ID** 🔑 → `DEFINITIONS.DEPARTMENT` | VARCHAR2(7) | N |  |  |
| 2 | **ACTIVE** | CHAR(1) | Y |  |  |
| 3 | **IS_REFRESH** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_RFID_ACCESS_DEPARTMENT` (DEPARTMENT_ID)
- **FK** `FK_RFID_ACCESS_DEPARTMENT` (DEPARTMENT_ID) → `DEFINITIONS.DEPARTMENT` (DEPARTMENT_ID)
- **Triggers**: `RFID_ACCESS_DEPARTMENT_DEL` (AFTER DELETE), `RFID_ACCESS_DEPARTMENT_INS` (BEFORE INSERT), `RFID_ACCESS_DEPARTMENT_UPD` (BEFORE UPDATE)

### RFID_ACCESS_SYNC_LOG

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOG_ID** | NUMBER | N |  |  |
| 2 | **RUN_ID** | NUMBER | N |  |  |
| 3 | **EVENT_TS** | DATE | N | SYSDATE |  |
| 4 | **EVENT_BY** | VARCHAR2(30) | N | USER |  |
| 5 | **EVENT_TYPE** | VARCHAR2(50) | N |  |  |
| 6 | **EVENT_SOURCE** | VARCHAR2(50) | Y |  |  |
| 7 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 8 | **MACHINE_ID** | VARCHAR2(5) | Y |  |  |
| 9 | **EMP_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 10 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 11 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 12 | **SEX_ID** | NUMBER | Y |  |  |
| 13 | **RFID_SUPER_CARD** | VARCHAR2(1) | Y |  |  |
| 14 | **MACHINE_ACCESS_TYPE** | VARCHAR2(10) | Y |  |  |
| 15 | **ACCESS_GRANT_EVENT** | VARCHAR2(100) | Y |  |  |
| 16 | **REMARKS** | VARCHAR2(1000) | Y |  |  |
| 17 | **OLD_ROW_JSON** | CLOB | Y |  |  |
| 18 | **NEW_ROW_JSON** | CLOB | Y |  |  |


### RFID_ACL_ADMIN

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `SECURITY.USERS` | VARCHAR2(14) | N |  |  |
| 2 | **PRIVILEGE_LEVEL** 🔑 | CHAR(1) | N | '2' | 0  Common User, 1  Enroller/Registrar , 2  Admin, 3  Super Administrator |
| 3 | **USER_PASSWORD** | VARCHAR2(500) | N |  |  |
| 4 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_ACL_ADMIN` (MRNO, PRIVILEGE_LEVEL)
- **FK** `FK_RFID_ACL_ADMIN_1` (MRNO) → `SECURITY.USERS` (MRNO)
- **Triggers**: `RFID_ACL_ADMIN_DEL` (AFTER DELETE), `RFID_ACL_ADMIN_INS` (BEFORE INSERT), `RFID_ACL_ADMIN_UPD` (BEFORE UPDATE)

### RFID_CARD_TYPE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CARD_TYPE_ID** 🔑 | NUMBER(4) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(200) | Y |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **ORDER_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 5 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_CARD_TYPE` (CARD_TYPE_ID)
- **Referenced by**: `RFID_CARDS`
- **Triggers**: `RFID_CARD_TYPE_DEL` (AFTER DELETE), `RFID_CARD_TYPE_INS` (BEFORE INSERT), `RFID_CARD_TYPE_UPD` (BEFORE UPDATE)

### RFID_CARDS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CARD_TYPE_ID** → `RFID.RFID_CARD_TYPE` | NUMBER(4) | Y |  |  |
| 2 | **RFID_CARD_NO** 🔑 | VARCHAR2(10) | N |  |  |
| 3 | **CATEGORY_ID** | NUMBER(5) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **CARD_DESCRIPTION** | VARCHAR2(50) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_CARDS` (RFID_CARD_NO)
- **FK** `FK_RFID_CARDS` (CARD_TYPE_ID) → `RFID.RFID_CARD_TYPE` (CARD_TYPE_ID) _DISABLED_
- **Referenced by**: `RFID_CARD_ISSUE_RECORD`
- **Triggers**: `RFID_CARDS_DEL` (AFTER DELETE), `RFID_CARDS_INS` (BEFORE INSERT), `RFID_CARDS_UPD` (BEFORE UPDATE)

### RFID_CARDS_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **RFID_CARD_NO** 🔑 | VARCHAR2(30) | N |  |  |
| 2 | **CATEGORY_ID** | NUMBER(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **CARD_DESCRIPTION** | VARCHAR2(50) | Y |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CARDS_01` (RFID_CARD_NO)
- **Triggers**: `RFID_CARDS_ACS_DEL` (AFTER DELETE), `RFID_CARDS_ACS_INS` (BEFORE INSERT), `RFID_CARDS_ACS_UPD` (BEFORE UPDATE)

### RFID_CARD_CATEGORY_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CARD_CATEGORY_ID** 🔑 | NUMBER(4) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(200) | Y |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 4 | **TIME_LIMIT** | NUMBER(4) | Y | 0 | RFID Card has the time limit and will be stored in this column |
| 5 | **TIME_LIMIT_UNIT** | CHAR(1) | Y | 'H' | H for Hours, M for Minutes,D for Days,S for Months, Y for Years,  N for No limit |
| 6 | **MAXIMUM_COUNT** | NUMBER(4) | Y |  | This column contains maximum number of visitors/attendents/guests allowed for each patients/employees |
| 7 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 8 | **TIME_RANGE_REQ** | CHAR(1) | Y | 'N' |  |
| 9 | **IS_EXTEND_ALLOWED** | CHAR(1) | Y | 'N' |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N | '001' |  |

- **Primary key** `PK_RFID_CARD_CATEGORY_01` (CARD_CATEGORY_ID, LOCATION_ID)
- **Unique** `UK_RFID_CARD_CATEGORY_01` (DESCRIPTION)
- **Triggers**: `RFID_CARD_CATEGORY_ACS_DEL` (AFTER DELETE), `RFID_CARD_CATEGORY_ACS_INS` (BEFORE INSERT), `RFID_CARD_CATEGORY_ACS_UPD` (BEFORE UPDATE)

### RFID_CARD_ISSUE_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR** 🔑 | NUMBER(20) | N |  |  |
| 2 | **RFID_CARD_NO** | VARCHAR2(30) | N |  |  |
| 3 | **NAME** | VARCHAR2(255) | Y |  |  |
| 4 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 5 | **ISSUE_DATE** | DATE | N |  |  |
| 6 | **RECEIVE_DATE** | DATE | Y |  |  |
| 7 | **RETURN** | CHAR(1) | Y | 'N' |  |
| 8 | **CARD_CATEGORY_ID** 🔑 | NUMBER(4) | N |  |  |
| 9 | **ISSUED_BY** | VARCHAR2(14) | Y |  |  |
| 10 | **REMARKS** | VARCHAR2(200) | Y |  |  |
| 11 | **NIC** | VARCHAR2(14) | Y |  |  |
| 12 | **RELATION_ID** | VARCHAR2(6) | Y |  |  |
| 13 | **ADDRESS** | VARCHAR2(400) | Y |  |  |
| 14 | **RETURN_DATE** | DATE | Y |  |  |
| 15 | **RIGHTS_STATUS** | CHAR(1) | Y | 'W' | W for waiting for rights, G for rights granted, R for rights revoked |
| 16 | **MACHINE_CATEGORY_ID** | NUMBER(6) | Y |  |  |
| 17 | **RIGHTS_ISSUE_DATE** | DATE | Y |  |  |
| 18 | **RIGHTS_REVOKE_DATE** | DATE | Y |  |  |
| 19 | **IS_EXTENDED** | CHAR(1) | Y | 'N' |  |
| 20 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 21 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 22 | **TRN_DATE** | DATE | Y |  |  |
| 23 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 24 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 25 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 26 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N | '001' |  |
| 27 | **CARD_DESC** | VARCHAR2(1000) | Y |  |  |
| 28 | **CONTACT_NO** | VARCHAR2(500) | Y |  |  |
| 29 | **WARD_ID** | VARCHAR2(7) | Y |  |  |
| 30 | **BUILDING_BLOCK_FLOOR_ID** | VARCHAR2(10) | Y |  |  |
| 31 | **BUILDING_BLOCK_ID** | VARCHAR2(7) | Y |  |  |
| 32 | **CARD_VALID_TILL** | DATE | Y |  |  |
| 33 | **SERIAL_NO_FOR_CARD_SWIPE** | NUMBER | Y |  | This column will be used in rfid.attendance_employee table to track record of attendance |

- **Primary key** `PK_RFID_CARD_ISSUE_01` (SR, CARD_CATEGORY_ID, MRNO, LOCATION_ID)
- **Triggers**: `RFID_CARD_ISSUE_ACS_DEL` (AFTER DELETE), `RFID_CARD_ISSUE_ACS_INS` (BEFORE INSERT), `RFID_CARD_ISSUE_ACS_UPD` (BEFORE UPDATE)

### RFID_CARD_ISSUE_RECORD

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR** 🔑 | NUMBER(6) | N |  |  |
| 2 | **RFID_CARD_NO** → `RFID.RFID_CARDS` | VARCHAR2(10) | N |  |  |
| 3 | **NAME** | VARCHAR2(255) | Y |  |  |
| 4 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 5 | **ISSUE_DATE** | DATE | N |  |  |
| 6 | **RECEIVE_DATE** | DATE | Y |  |  |
| 7 | **RETURN** | CHAR(1) | N | 'N' |  |
| 8 | **CARD_TYPE_ID** 🔑 | NUMBER(4) | N |  |  |
| 9 | **ISSUED_BY** | VARCHAR2(14) | Y |  |  |
| 10 | **REMARKS** | VARCHAR2(200) | Y |  |  |
| 11 | **NIC** | VARCHAR2(14) | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **TRN_DATE** | DATE | Y |  |  |
| 18 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 19 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 20 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 21 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_CARD_ISSUE_RECORD` (SR, CARD_TYPE_ID)
- **FK** `CARD_NO` (RFID_CARD_NO) → `RFID.RFID_CARDS` (RFID_CARD_NO) _DISABLED_

### RFID_CATEGORY_DEPARTMENTS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CATEGORY_ID** 🔑 | NUMBER(5) | N |  |  |
| 2 | **DEPARTMENT_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 3 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 4 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 5 | **TRN_DATE** | DATE | Y |  |  |
| 6 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 9 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 10 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `RFID_CATEGORY_DEPARTMENTS` (CATEGORY_ID, DEPARTMENT_ID)
- **Triggers**: `RFID_CATEGORY_DEPARTMENTS_DEL` (AFTER DELETE), `RFID_CATEGORY_DEPARTMENTS_INS` (BEFORE INSERT), `RFID_CATEGORY_DEPARTMENTS_UPD` (BEFORE UPDATE)

### RFID_CATEGORY_MACHINES

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 2 | **CATEGORY_ID** 🔑 → `RFID.RFID_CATEGORY` | NUMBER(5) | N |  |  |
| 3 | **ACTIVE** | VARCHAR2(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 11 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 12 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 13 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_CATEGORY_MACHINES` (MACHINE_ID, CATEGORY_ID)
- **FK** `FK_RFID_CATEGORY_MACHINES` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **FK** `FK_RFID_CATEGORY_MACHINES_1` (CATEGORY_ID) → `RFID.RFID_CATEGORY` (CATEGORY_ID) _DISABLED_
- **Triggers**: `RFID_CATEGORY_MACHINES_DEL` (AFTER DELETE), `RFID_CATEGORY_MACHINES_INS` (BEFORE INSERT), `RFID_CATEGORY_MACHINES_UPD` (BEFORE UPDATE)

### RFID_CATEGORY_MACHINES_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 2 | **CATEGORY_ID** 🔑 | NUMBER(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **LOCATION_ID** | VARCHAR2(3) | Y | '001' |  |

- **Primary key** `PK_MAC_CAT_01` (MACHINE_ID, CATEGORY_ID)
- **Triggers**: `RFID_CATEGORY_MACHINES_ACS_DEL` (AFTER DELETE), `RFID_CATEGORY_MACHINES_ACS_INS` (BEFORE INSERT), `RFID_CATEGORY_MACHINES_ACS_UPD` (BEFORE UPDATE)

### RFID_CATEGORY_TIMERANGE_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CARD_CATEGORY_ID** 🔑 | NUMBER(4) | N |  |  |
| 2 | **UPPER_TIME_LIMIT** | VARCHAR2(4) | Y |  |  |
| 3 | **LOWER_TIME_LIMIT** | VARCHAR2(4) | Y |  |  |
| 4 | **SR_NO** 🔑 | NUMBER(4) | N |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **LOCATION_ID** | VARCHAR2(3) | Y | '001' |  |

- **Primary key** `PK_RFID_TIM_RANGE_01` (CARD_CATEGORY_ID, SR_NO)
- **Triggers**: `RFID_CAT_TR_ACS_DEL` (AFTER DELETE), `RFID_CAT_TR_ACS_INS` (BEFORE INSERT), `RFID_CAT_TR_ACS_UPD` (BEFORE UPDATE)

### RFID_CONFIDENTIAL_Q

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CHECK_TIME** 🔑 | DATE | N |  |  |
| 2 | **MACHINE_IDENTIFIER** 🔑 | NUMBER(10) | N |  |  |
| 3 | **MACHINE_ID** 🔑 | NUMBER(5) | N |  |  |
| 4 | **ENTRY_DATE** | DATE | Y |  |  |
| 5 | **REASON** | VARCHAR2(4000) | Y |  |  |
| 6 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **SR_NO** | NUMBER | Y |  |  |

- **Primary key** `RFID_CONFIDENTIAL_Q_PK` (CHECK_TIME, MACHINE_IDENTIFIER, MACHINE_ID)
- **Triggers**: `RFID_CONFIDENTIAL_Q_DEL` (AFTER DELETE), `RFID_CONFIDENTIAL_Q_DELETE_HISTORY` (AFTER DELETE), `RFID_CONFIDENTIAL_Q_INS` (BEFORE INSERT), `RFID_CONFIDENTIAL_Q_UPD` (BEFORE UPDATE)

### RFID_CONFIDENTIAL_Q_HIS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CHECK_TIME** | DATE | Y |  |  |
| 2 | **MACHINE_IDENTIFIER** | NUMBER(10) | Y |  |  |
| 3 | **MACHINE_ID** | NUMBER(5) | Y |  |  |
| 4 | **ENTRY_DATE** | DATE | Y |  |  |
| 5 | **REASON** | VARCHAR2(4000) | Y |  |  |
| 6 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 7 | **SIGNED_BY** | VARCHAR2(14) | Y |  |  |
| 8 | **SIGNED_DATE** | DATE | Y |  |  |


### RFID_CONFI_MACHINE_RIGHTS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CONFI_MACHI_RIGHTS` (MRNO, MACHINE_ID)
- **Triggers**: `RFID_CONFI_MACHINE_RIGHTS_DEL` (AFTER DELETE), `RFID_CONFI_MACHINE_RIGHTS_INS` (BEFORE INSERT), `RFID_CONFI_MACHINE_RIGHTS_UPD` (BEFORE UPDATE)

### RFID_DATA_TRANSFER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_CODE** 🔑 | VARCHAR2(10) | N |  |  |
| 2 | **IP_ADDRESS** | VARCHAR2(15) | N |  |  |
| 3 | **PORT_NO** | NUMBER | N |  |  |
| 4 | **MACHINE_IDENTIFIER** 🔑 | VARCHAR2(9) | N |  |  |
| 5 | **USER_NAME** | VARCHAR2(255) | Y |  |  |
| 6 | **USER_PASSWORD** | VARCHAR2(255) | Y |  |  |
| 7 | **PRIVILEGE** 🔑 | NUMBER(1) | N |  |  |
| 8 | **ENABLED** 🔑 | CHAR(1) | N | 'Y' |  |
| 9 | **RFID_CARD_NO** | VARCHAR2(30) | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **NO_OF_TRIES** | NUMBER(3) | Y | 0 |  |
| 17 | **ALERT_TEXT** | VARCHAR2(2000) | Y |  |  |
| 18 | **COMPLETE_MRNO** | VARCHAR2(14) | Y |  |  |
| 19 | **RFID_ATTENDANCE_TYPE** | CHAR(1) | Y | 'A' | 'T' for thumb scan, 'R' for rfid attendance, and 'A' For all' |
| 20 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 21 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 22 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 23 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_DATA_TRANSFER` (MACHINE_CODE, MACHINE_IDENTIFIER, PRIVILEGE, ENABLED)
- **Index** `INDX_MAC_CODE_EMP_NO_PRIV` (MACHINE_CODE, MACHINE_IDENTIFIER, PRIVILEGE)
- **Triggers**: `RFID_DATA_TRANSFER_DEL` (AFTER DELETE), `RFID_DATA_TRANSFER_INS` (BEFORE INSERT), `RFID_DATA_TRANSFER_UPD` (BEFORE UPDATE)

### RFID_DEFAULT_ACCESS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 5 | **IS_REFRESH** | CHAR(1) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_RFID_DEFAULT_ACCESS` (MACHINE_ID, LOCATION_ID)
- **FK** `FK_RFID_DEFAULT_ACCESS_MACHINE_ID` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **Triggers**: `RFID_DEFAULT_ACCESS_DEL` (AFTER DELETE), `RFID_DEFAULT_ACCESS_INS` (BEFORE INSERT), `RFID_DEFAULT_ACCESS_UPD` (BEFORE UPDATE)

### RFID_DELETED_ACCESS_AUDIT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AUDIT_ID** | NUMBER | N |  |  |
| 2 | **RUN_ID** | NUMBER | N |  |  |
| 3 | **SOURCE_TABLE** | VARCHAR2(50) | N |  |  |
| 4 | **REASON_CODE** | VARCHAR2(50) | N |  |  |
| 5 | **REASON_TEXT** | VARCHAR2(500) | Y |  |  |
| 6 | **EMP_LOCATION_ID** | VARCHAR2(20) | Y |  |  |
| 7 | **MRNO** | VARCHAR2(30) | Y |  |  |
| 8 | **DEPARTMENT_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **DESIGNATION_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **MACHINE_ID** | NUMBER | Y |  |  |
| 11 | **DELETED_ON** | DATE | N | SYSDATE |  |
| 12 | **DELETED_BY** | VARCHAR2(100) | N | USER |  |
| 13 | **ROW_DATA_JSON** | CLOB | Y |  |  |


### RFID_DEPT_GENERAL_ACCESS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DEPARTMENT_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 2 | **MACHINE_ID** 🔑 → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEPT_WISE_GENERAL_ACCESS` (DEPARTMENT_ID, MACHINE_ID)
- **FK** `FK_DEPT_WISE_GENERAL_MACHINE_ID` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **Index** `INDX_GA_MACHINE_ID` (MACHINE_ID)
- **Triggers**: `RFID_DEPT_GENERAL_ACCESS_DEL` (AFTER DELETE), `RFID_DEPT_GENERAL_ACCESS_INS` (BEFORE INSERT), `RFID_DEPT_GENERAL_ACCESS_UPD` (BEFORE UPDATE)

### RFID_DESIG_WISE_SP_ACCESS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DESIGNATION_ID** 🔑 → `RFID.DEPT_WISE_DESIG_ACCESS` | VARCHAR2(6) | N |  |  |
| 2 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **DEPARTMENT_ID** 🔑 → `RFID.DEPT_WISE_DESIG_ACCESS` | VARCHAR2(7) | N |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_RFID_DESIG_WISE_ACCESS` (DESIGNATION_ID, MACHINE_ID, DEPARTMENT_ID)
- **FK** `FK_RFID_DEPT_DESIGN` (DEPARTMENT_ID, DESIGNATION_ID) → `RFID.DEPT_WISE_DESIG_ACCESS` (DEPARTMENT_ID, DESIGNATION_ID)
- **Index** `INDX_DEPT_DESIG_ID` (DESIGNATION_ID, DEPARTMENT_ID, MACHINE_ID)
- **Index** `INDX_DEPT_DESIG_ID_02` (DEPARTMENT_ID, DESIGNATION_ID)
- **Triggers**: `RFID_DESIG_WISE_SP_ACCESS_DEL` (AFTER DELETE), `RFID_DESIG_WISE_SP_ACCESS_INS` (BEFORE INSERT), `RFID_DESIG_WISE_SP_ACCESS_UPD` (BEFORE UPDATE)

### RFID_DOORS_LOG

This table is used to log door status which are opened manually.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  | Machine ID from RFID.RFID_MACHINES |
| 2 | **DOOR_STATUS** | CHAR(1) | N | 'O' | O: Open \| C: Close |
| 3 | **TRANS_DATE** | DATE | N | SYSDATE | Date of transaction |
| 4 | **EMPLOYEE_CODE** | VARCHAR2(15) | Y |  |  |
| 5 | **TERMINAL_NAME** | VARCHAR2(30) | N |  | Terminal name  which initiates the door opening request. |
| 6 | **OS_USER_NAME** | VARCHAR2(30) | Y |  | Current logged in user who initiates the request. |
| 7 | **MACHINE_LOC** | VARCHAR2(3) | Y |  | RFID Machine Location ID |

- **FK** `FK_RFID_DOORS_LOG_1` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID)
- **Index** `IDX_RFID_DOORS_LOG_1` (MACHINE_ID, TRANS_DATE, TERMINAL_NAME)

### RFID_EMP_WISE_SP_ACCESS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_RFID_EMP_WISE_SP_ACCESS` (MRNO, MACHINE_ID)
- **Triggers**: `RFID_EMP_WISE_SP_ACCESS_DEL` (AFTER DELETE), `RFID_EMP_WISE_SP_ACCESS_INS` (BEFORE INSERT), `RFID_EMP_WISE_SP_ACCESS_UPD` (BEFORE UPDATE)

### RFID_MACHINES_DATA

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** | VARCHAR2(5) | N |  |  |
| 2 | **MRNO** | VARCHAR2(14) | N |  |  |
| 3 | **REQUEST_DATE** | DATE | Y | SYSDATE |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Triggers**: `RFID_MACHINES_DATA_DEL` (AFTER DELETE), `RFID_MACHINES_DATA_INS` (BEFORE INSERT), `RFID_MACHINES_DATA_UPD` (BEFORE UPDATE)

### RFID_MACHINE_CATEGORY_ACS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CATEGORY_ID** | NUMBER(5) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(50) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 6 | **WARD_ID** | VARCHAR2(7) | Y |  |  |
| 7 | **IS_DEFAULT_WARD** | CHAR(1) | Y | 'Y' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **BUILDING_BLOCK_FLOOR_ID** | VARCHAR2(10) | Y |  |  |
| 15 | **BUILDING_BLOCK_ID** | VARCHAR2(7) | Y |  |  |

- **Triggers**: `RFID_MACHINE_CATEGORY_ACS_DEL` (AFTER DELETE), `RFID_MACHINE_CATEGORY_ACS_INS` (BEFORE INSERT), `RFID_MACHINE_CATEGORY_ACS_UPD` (BEFORE UPDATE)

### RFID_MACHINE_COMMAND

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ID** 🔑 | NUMBER | Y | as identity |  |
| 2 | **DEVICE_SERIAL** | VARCHAR2(50) | N |  |  |
| 3 | **COMMAND_NAME** | VARCHAR2(255) | Y |  |  |
| 4 | **COMMAND_CONTENT** | CLOB | Y |  |  |
| 5 | **STATUS** | NUMBER(11) | N | 0 |  |
| 6 | **SEND_STATUS** | NUMBER(11) | N | 0 |  |
| 7 | **ERROR_COUNT** | NUMBER(11) | N | 0 |  |
| 8 | **RUN_TIME** | DATE | Y |  |  |
| 9 | **CREATED_AT** | DATE | N |  |  |
| 10 | **MODIFIED_AT** | DATE | N |  |  |
| 11 | **RESPONSE** | CLOB | Y |  |  |

- **Primary key** `PK_RFID_MACHINE_COMMAND` (ID)
- **Triggers**: `PRE_INSERT` (before insert)

### RFID_MACHINE_TIMESTAMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** → `RFID.RFID_MACHINES` | VARCHAR2(5) | N |  |  |
| 2 | **MACHINE_LOCATION_ID** | VARCHAR2(3) | N |  |  |
| 3 | **MACHINE_TIMESTAMP** | VARCHAR2(20) | N |  |  |
| 4 | **ACTUAL_TIMESTAMP** | DATE | N | sysdate |  |
| 5 | **REMARKS** | VARCHAR2(1000) | Y |  |  |
| 6 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **FK** `FK_RFID_MACH_TIMESTAMP_1` (MACHINE_ID) → `RFID.RFID_MACHINES` (MACHINE_ID) _DISABLED_

### RFID_MACHIN_IDENTIFIER_MAPPING

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 4 | **RFID_CARD_CODE** | VARCHAR2(30) | Y |  |  |
| 5 | **MACHINE_IDENTIFIER** 🔑 | NUMBER(10) | N |  |  |
| 6 | **EMPLOYEE_CODE** | VARCHAR2(14) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_RFID_MACHINE_MAPPING` (ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, MACHINE_IDENTIFIER)
- **Index** `INDX_EMPLOYEE_CODE` (EMPLOYEE_CODE)
- **Index** `INDX_RFID_CODE` (RFID_CARD_CODE)
- **Triggers**: `RFID_MACH_IDENT_MAPING_DEL` (AFTER DELETE), `RFID_MACH_IDENT_MAPING_INS` (BEFORE INSERT), `RFID_MACH_IDENT_MAPING_UPD` (BEFORE UPDATE)

### SECTION_WISE_ATTENDANCE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DEPARTMENT_ID** 🔑 → `RFID.MACHINE_COMPLETE_DEPARTMENT` | VARCHAR2(7) | N |  |  |
| 2 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 3 | **SECTION_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 4 | **MACHINE_ID** 🔑 → `RFID.MACHINE_COMPLETE_DEPARTMENT` | VARCHAR2(5) | N |  |  |
| 5 | **IS_ATTENDANCE_MARK** | CHAR(1) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_SECTION_WISE_ATTENDANCE` (DEPARTMENT_ID, SECTION_ID, MACHINE_ID)
- **FK** `FK_SECTION_WISE_ATTENDANCE_1` (MACHINE_ID, DEPARTMENT_ID) → `RFID.MACHINE_COMPLETE_DEPARTMENT` (MACHINE_ID, DEPARTMENT_ID) _DISABLED_
- **Check** `CHK_SECTION_WISE_ATTENDANCE_1`: `(ACTIVE IN ('Y', 'N'))`
- **Triggers**: `SECTION_WISE_ATTENDANCE_DEL` (AFTER DELETE), `SECTION_WISE_ATTENDANCE_INS` (BEFORE INSERT), `SECTION_WISE_ATTENDANCE_UPD` (BEFORE UPDATE)

### TEMP_CARD_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR_NO** | NUMBER | Y |  |  |
| 2 | **CARD_NO** 🔑 | VARCHAR2(10) | N |  |  |
| 3 | **CARD_DESCRIPTION** | VARCHAR2(1000) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `TEMP_CARD_SETUP_PK` (CARD_NO)
- **Triggers**: `TEMP_CARD_SETUP_DEL` (AFTER DELETE), `TEMP_CARD_SETUP_INS` (BEFORE INSERT), `TEMP_CARD_SETUP_UPD` (BEFORE UPDATE)

### TEMP_RFID_REGISTERED_USERS

This table will be used to retrieve registered users of RFID machines on temporary basis. So that fingerprints and RFId cards can be mapped to original users later on. Data in this table is temporary and can be removed if required.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** 🔑 | VARCHAR2(5) | N |  |  |
| 2 | **USER_IDENTIFIER** 🔑 | VARCHAR2(20) | N |  |  |
| 3 | **USER_NAME** | VARCHAR2(30) | Y |  |  |
| 4 | **PREVILEGE** | VARCHAR2(1) | Y |  |  |
| 5 | **USER_ENABLE** | VARCHAR2(1) | Y |  |  |
| 6 | **USER_PASSWORD** | VARCHAR2(10) | Y |  |  |
| 7 | **RFID_CARD_NO** | VARCHAR2(20) | Y |  |  |
| 8 | **FINGERPRINT** | VARCHAR2(4000) | Y |  |  |
| 9 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 10 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 11 | **TRANS_DATE** | DATE | N | sysdate |  |
| 12 | **IRIS_VALUE** | BLOB | Y |  |  |

- **Primary key** `PK_TRRU_1` (ORGANIZATION_ID, LOCATION_ID, MACHINE_ID, USER_IDENTIFIER)

### TMP_SELECTED_MACHINES_PR

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MACHINE_ID** | VARCHAR2(5) | Y |  |  |
| 2 | **MRNO** | VARCHAR2(14) | Y |  |  |


### TRAINING_ATTENDANCE_STG

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR_NO** | NUMBER | Y |  |  |
| 2 | **CHECK_TIME** | DATE | Y |  |  |
| 3 | **MACHINE_ID** | NUMBER(5) | Y |  |  |
| 4 | **ENTRY_DATE** | DATE | Y |  |  |
| 5 | **REASON** | VARCHAR2(4000) | Y |  |  |
| 6 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 7 | **RFID_CODE** | VARCHAR2(50) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **ORDER_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 10 | **TRAINING_ATTENDANCE_MARK** | CHAR(1) | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Triggers**: `TRAINING_ATTENDANCE_STG_DEL` (AFTER DELETE), `TRAINING_ATTENDANCE_STG_INS` (BEFORE INSERT), `TRAINING_ATTENDANCE_STG_UPD` (BEFORE UPDATE)

## Views

### RFID_V_DEPT_GENERAL_ACCESS

Sources: `RFID_DEPT_GENERAL_ACCESS`

```sql
SELECT DA.DEPARTMENT_ID,
       DA.MACHINE_ID,
       DA.ACTIVE,
       RM.DESCRIPTION MACHINE_NAME,
        'DGA' MACHINE_ACCESS_TYPE ,
      'Department wise access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DEPT_GENERAL_ACCESS DA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = DA.MACHINE_ID
```

### VU_MACHINE_COMPLETE_DEPARTMENT

Sources: `MACHINE_COMPLETE_DEPARTMENT`

```sql
SELECT MCD.MACHINE_ID,
       MCD.DEPARTMENT_ID,
       MCD.ACTIVE,
       MCD.IS_ATTENDANCE_MARK,
       D.DESCRIPTION
  FROM RFID.MACHINE_COMPLETE_DEPARTMENT MCD, DEFINITIONS.DEPARTMENT D
 WHERE D.DEPARTMENT_ID = MCD.DEPARTMENT_ID
```

### VU_SECTION_WISE_ATTENDANCE

Sources: `SECTION_WISE_ATTENDANCE`

```sql
SELECT SWA.DEPARTMENT_ID,
       SWA.ACTIVE,
       SWA.SECTION_ID,
       SWA.MACHINE_ID,
       SWA.IS_ATTENDANCE_MARK,
       DS.DESCRIPTION ND_SECTION_DESC
  FROM RFID.SECTION_WISE_ATTENDANCE SWA, DEFINITIONS.DEPARTMENT_SECTION DS
 WHERE DS.DEPARTMENT_ID = SWA.DEPARTMENT_ID
   AND DS.SECTION_ID = SWA.SECTION_ID
```

### V_CURRENT_EMPLOYEE

Sources: `V_CURRENT_EMPLOYEE`

```sql
SELECT E.MRNO,
       E.NAME,
       E.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_NAME (E.MRNO) DEPARTMENT ,
       E.DESIGNATION,
       E.JOINING_DATE,
       HRD.F_GET_EMPLOYEE_DUTY_LOC_ID(E.MRNO)EMPLOYEE_DUTY_LOC,
       HRD.F_GET_EMPLOYEE_LOCATION(E.MRNO) EMPLOYEE_LOCATION
 FROM HRD.V_CURRENT_EMPLOYEE E
 ORDER BY HRD.F_GET_DEPARTMENT_NAME (E.MRNO)
```

### V_DEPT_WISE_DESIG_ACCESS

Sources: `DEPT_WISE_DESIG_ACCESS`

```sql
SELECT DWD.DEPARTMENT_ID, DWD.DESIGNATION_ID, DWD.ACTIVE, D.DESCRIPTION FROM   RFID.DEPT_WISE_DESIG_ACCESS DWD, DEFINITIONS.DESIGNATION D
  WHERE D.DESIGNATION_ID = DWD.DESIGNATION_ID
```

### V_DESIGNATION_LOV

Sources: `CURRENT_EMPLOYEES`

```sql
SELECT DISTINCT HRD.F_GET_DESIGNATION_ID(T.MRNO) DESIGNATION_ID,
                D.DESCRIPTION  DESIGNATION,
                t.department_id
  FROM HRD.CURRENT_EMPLOYEES T, DEFINITIONS.DESIGNATION D
  WHERE D.DESIGNATION_ID = HRD.F_GET_DESIGNATION_ID(T.MRNO)
```

### V_MACHINE_WISE_EMPLOYEE

Sources: `MACHINE_WISE_EMPLOYEE`

```sql
SELECT MWE.MACHINE_ID,
       MWE.MRNO,
       MWE.ACTIVE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(MWE.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(MWE.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(MWE.MRNO) DESIGNATION,
       RFID.PKG_RFID_MACHINES.f_get_rfid_code(MWE.MRNO) RFID_CODE
  FROM RFID.MACHINE_WISE_EMPLOYEE MWE
```

### V_RFID_ACCESS_DEPARTMENT

Sources: `RFID_ACCESS_DEPARTMENT`

```sql
select rd.department_id, rd.active, d.description dept_name, d.location_id, RD.IS_REFRESH from rfid.rfid_access_department  rd, definitions.department d
where d.department_id = rd.department_id
```

### V_RFID_CARD_ISSUE_ACS

Sources: `RELATION`, `RFID_CARD_ISSUE_ACS`, `ROOMS`

```sql
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
 ORDER BY T.ISSUE_DATE DESC
```

### V_RFID_CARD_SWIPE_DETAILS

Sources: `ATTENDANCE_EMPLOYEE`

```sql
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
   AND CI.MRNO = P.mrno
```

### V_RFID_CONFIDENTAIL_Q

Sources: `RFID_CONFIDENTIAL_Q`

```sql
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
      AND M.IS_CONFIDENTIAL ='Y'
```

### V_RFID_CONFI_MACHINE_RIGHTS

Sources: `RFID_CONFI_MACHINE_RIGHTS`

```sql
SELECT R.MRNO, R.MACHINE_ID, R.ACTIVE, M.DESCRIPTION MACHINE_NAME FROM RFID.RFID_CONFI_MACHINE_RIGHTS R, RFID.RFID_MACHINES M
WHERE R.MACHINE_ID = M.MACHINE_ID
```

### V_RFID_DEFAULT_ACCESS

Sources: `RFID_DEFAULT_ACCESS`

```sql
SELECT RDA.MACHINE_ID,
       M.DESCRIPTION MACHINE_NAME,
       RDA.LOCATION_ID,
       RDA.ACTIVE,
       RDA.REMARKS,
       RDA.IS_REFRESH,
       'DAA' MACHINE_ACCESS_TYPE ,
      'DEFUALT ACCESS'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DEFAULT_ACCESS RDA, RFID.RFID_MACHINES M
 WHERE M.MACHINE_ID = RDA.MACHINE_ID
```

### V_RFID_DESIG_WISE_SP_ACCESS

Sources: `RFID_DESIG_WISE_SP_ACCESS`

```sql
SELECT RDA.MACHINE_ID,
       RDA.DESIGNATION_ID,
       RDA.DEPARTMENT_ID,
       RDA.ACTIVE,
       RM.DESCRIPTION MACHINE_NAME,
       'DSA' MACHINE_ACCESS_TYPE ,
      'Designation wis special access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_DESIG_WISE_SP_ACCESS RDA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = RDA.MACHINE_ID
```

### V_RFID_EMP_WISE_SP_ACCESS

Sources: `RFID_EMP_WISE_SP_ACCESS`

```sql
SELECT
       RA.MRNO,
       RA.MACHINE_ID,
       RM.DESCRIPTION MACHINE_NAME ,
       RA.ACTIVE,
        'E' MACHINE_ACCESS_TYPE ,
      'Employee Wise Access'  ACCESS_GRANT_EVENT
  FROM RFID.RFID_EMP_WISE_SP_ACCESS RA, RFID.RFID_MACHINES RM
 WHERE RM.MACHINE_ID = RA.MACHINE_ID
 AND RM.ACTIVE ='Y'
```

## Sequences

| Sequence | Options |
|---|---|
| ISEQ$$_2157281 | minvalue 1 maxvalue 9999999999999999999999999999 start with 21 increment by 1 cache 20 |
| SEQ_RFID_ACCESS_SYNC_LOG | minvalue 1 maxvalue 9999999999999999999999999999 start with 35 increment by 1 nocache |
| SEQ_RFID_ACCESS_SYNC_RUN | minvalue 1 maxvalue 9999999999999999999999999999 start with 11 increment by 1 nocache |
| SEQ_RFID_CLEANUP_RUN | minvalue 1 maxvalue 9999999999999999999999999999 start with 3 increment by 1 nocache |
| SEQ_RFID_DELETED_ACCESS_AUDIT | minvalue 1 maxvalue 9999999999999999999999999999 start with 2181 increment by 1 nocache |

## Packages

### PKG_COMMON

- `procedure FOR_CHANGE_RFID_CARD(P_MRNO IN VARCHAR2, P_RFID_CODE IN VARCHAR2)`
- `procedure PRO_DESIG_WISE_RFID_RIGHTS(P_DESIGNATION_ID IN VARCHAR2, P_RFID_CATAGORY_ID IN NUMBER, P_MRNO IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_CATEGORY_WISE_RFID_RIGHTS(P_RFID_CATAGORY_ID IN NUMBER, P_MRNO IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_DEPART_WISE_RFID_RIGHTS(P_DEPARTMENT_ID IN VARCHAR2, P_RFID_CATAGORY_ID IN NUMBER, P_MACHINE_ID IN NUMBER, P_MRNO IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_RFID_REVOKE_RIGHTS(P_MRNO IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_RFID_CODE(P_MRNO IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_ASSIGN_RFID_RIGHTS_TO_EMP(P_MRNO IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL)`
- `function F_IS_MARK_ATTENDANCE_ALLOWED(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE) RETURN CHAR`
- `procedure P_INSERT_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_SECTION_ID IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure P_REVOKE_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_SECTION_ID IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure PRO_POPULATE_RFID_DEPARTMENT(P_MACHINE_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function F_EMP_CODE_FROM_RFID(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_INSERT_RFID_ATTENDANCE(P_CHECK_TIME IN DATE, P_MACHINE_CODE IN VARCHAR2, P_RFID_CODE IN VARCHAR2, P_CHECK_TYPE IN VARCHAR2, P_VERIFICATION_MODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_EMPLOYEE_CODE(P_MACHINE_CODE IN VARCHAR2, P_MACHINE_IDENTIFIER IN VARCHAR2, P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_GET_RFID_MACHINE_CODE(P_RFID_CODE IN VARCHAR2, P_MACHINE_CODE IN OUT VARCHAR2, P_MACHINE_IDENTIFIER IN OUT VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_IP_ADDRESS IN VARCHAR2, P_MACHINE_CATEGORY OUT VARCHAR2, P_EMPLOYEE_CODE OUT VARCHAR2)`
- `function F_IS_TRANSPORT_POOL_CARD(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2`
- `function F_MACHINE_CODE_FROM_IP(P_IP_ADDRESS IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_IDENTIFIER(P_MRNO IN VARCHAR2, P_MACHINE_CODE IN VARCHAR2, P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2`
- `function GET_IDENTIFIER_FROM_RFIDCODE(P_RFID_CODE IN VARCHAR2, P_MACHINE_CODE IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_RFID_MACHINE_LOCATION_ID(P_MACHINE_CODE IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_RFID_FROM_MAPPING(P_MACHINE_CODE IN VARCHAR2, P_MRNO IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_MACHINE_TYPE(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `function F_CHECH_VEHICLE_MACHINE_RIGHTS(P_MACHINE_ID IN VARCHAR2, P_MRNO IN VARCHAR2) RETURN CHAR`
- `function F_CHECK_ACTIVE_EMP(P_RFID_CODE IN VARCHAR2) RETURN CHAR`
- `procedure P_INS_ATTENDANCE_PAT(P_CHECKTIME RFID.ATTENDANCE.CHECK_TIME%TYPE, P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE, P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE, P_REASON VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure FOR_REMOVE_RFID_CARD(P_MRNO IN VARCHAR2, P_OLD_RFID_CODE IN VARCHAR2)`
- `procedure P_INS_RFID_QUEUE(P_CHECKTIME RFID.ATTENDANCE.CHECK_TIME%TYPE, P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE, P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE, P_MRNO VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEL_ALERT_QUEUE(P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE, P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE, P_SRNO NUMBER, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_MACH_IS_CONF(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_INS_TEMP_CARD(P_MRNO HRD.VU_INFORMATION.MRNO%TYPE, P_ACTUAL_RFID HRD.VU_INFORMATION.RFID_CODE %TYPE, P_TEMP_RFID VARCHAR2, P_DAY NUMBER, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_UPDATE_RFID_CODE(P_MRNO HRD.VU_INFORMATION.MRNO%TYPE, P_RFID_ID VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_MACHINE_LOC_ID(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_MACHINE_LOC_DESC(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_INS_ATTENDANCE_EMP(P_CHECKTIME RFID.ATTENDANCE.CHECK_TIME%TYPE, P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE, P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE, P_MRNO VARCHAR2, P_REASON VARCHAR2, P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID RFID.ATTENDANCE.LOCATION_ID%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_IS_RFID_NEW_SCHEME(P_DEPARTMENT_ID IN VARCHAR2) RETURN CHAR`
- `procedure P_GRANT_RFID_ACCESS_NEW_SCHEME(P_MRNO IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_EMP_SEX_ID(P_MRNO IN VARCHAR2) RETURN NUMBER`
- `function F_GET_RFID_MACHINE_SEX_ID(P_MACHINE_ID IN VARCHAR2) RETURN NUMBER`
- `procedure P_INS_TRAINING_ATTENDANCE_STG(P_CHECKTIME RFID.ATTENDANCE_EMPLOYEE.CHECK_TIME%TYPE, P_MACHINE_ID RFID.ATTENDANCE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO VARCHAR2, P_REASON VARCHAR2, P_RFID_CODE RFID.ATTENDANCE_EMPLOYEE.rfid_code%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_TRAINING_ATTEND_MARK(P_MACHINE_ID RFID.RFID_MACHINES.MACHINE_ID%TYPE) RETURN CHAR`

### PKG_RFID_MACHINES

- `function F_RFID_MACHINES_QRY(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_ACTIVE IN RFID.RFID_MACHINES.ACTIVE%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATE...`
- `procedure P_RFID_MACHINES_QRY(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_ACTIVE IN RFID.RFID_MACHINES.ACTIVE%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, P_DATA IN OUT RFID_MACHINES_TBL, P_STOP ...`
- `procedure P_RFID_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN RFID_MACHINES_REC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_INS(P_DATA IN OUT RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_LCK(P_DATA IN OUT RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_UPD(P_DATA IN OUT RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_DEL(P_DATA IN OUT RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_DEPT_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE, P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_ACTIVE IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE) RETURN DEPT_MACHINES_TL_PF PIPELINED`
- `procedure P_DEPT_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE, P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_ACTIVE IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE, P_DATA IN OUT DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN DEPT_MACHINES_RC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT .MACHINE_ID%TYPE, P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE, P_DATA IN OUT DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_LCK(P_DATA IN OUT DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_UPD(P_DATA IN OUT DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_DEL(P_DATA IN OUT DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_EMP_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_NAME IN HRD.V_INFORMATION.NAME%TYPE, P_DISP_MRNO IN HRD.V_INFORMATION.DISP_MRNO%TYPE, P_DEPARTMENT IN HRD.V_INFORMATION.DEPARTMENT%TYPE, P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RFID_CODE IN HRD.INFORMATION.RFID_CODE%TYP...`
- `procedure P_EMP_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_NAME IN HRD.V_INFORMATION.NAME%TYPE, P_DISP_MRNO IN HRD.V_INFORMATION.DISP_MRNO%TYPE, P_DEPARTMENT IN HRD.V_INFORMATION.DEPARTMENT%TYPE, P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RFID_CODE IN HRD.INFORMATION.RFID_CODE%TYP...`
- `procedure P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN EMP_MACHINES_RC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_LCK(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_UPD(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_DEL(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_SEND_DATA_TO_MACHINE_V2(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_ACTION IN CHAR, P_RFID_CODE IN VARCHAR2 DEFAULT NULL, P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A', P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, P_MACHINE_LOCATION_ID IN RFID....`
- `procedure P_SEND_DATA_TO_MACHINE(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_ACTION IN CHAR, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_RFID_CODE IN VARCHAR2 DEFAULT NULL, P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A', P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL, P_ACCESS_GRANT_EVENT IN VARCHAR2 DEFAULT NULL)`
- `procedure P_COPY_MACHINE_RIGHTS(P_TYPE IN CHAR, P_MRNO IN VARCHAR2, P_MASTER_MRNO IN VARCHAR2, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_MASTER_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A', P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`
- `procedure P_RELOAD_MACHINE_DATA(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`
- `function F_GET_RFID_CODE(P_MRNO IN VARCHAR2) return varchar`
- `procedure P_INACTIVE_CARD_CATAGORY(P_CARD_TYPE_ID IN RFID.RFID_CARD_TYPE.CARD_TYPE_ID%TYPE, P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_RFID_CARD_NO IN RFID.RFID_CARDS.RFID_CARD_NO%TYPE, P_ACTION IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`
- `procedure P_DELETE_EMP_MACHINE_DATA(P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO %TYPE, P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`
- `procedure P_REVOKE_MACHINE_RIGHTS(P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`
- `function F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO IN VARCHAR2, P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `function F_IS_RFID_REQUIRED(P_MACHINE_ID IN VARCHAR2) RETURN CHAR`
- `function F_IS_ALREADY_FOUND_IN_MAPPING(P_MACHINE_ID IN VARCHAR2, P_MRNO IN VARCHAR2) RETURN CHAR`
- `function F_GET_RFID_CODE_FROM_MAPPING(P_MACHINE_ID IN VARCHAR2, P_MRNO IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_MACHINE_WISE_MAX_COUNTER(P_MACHINE_ID IN VARCHAR2) RETURN NUMBER`
- `function F_GET_EMPLOYEE_CODE(P_MACHINE_CODE IN VARCHAR2, P_MACHINE_IDENTIFIER IN VARCHAR2) RETURN VARCHAR2`
- `function F_GET_EMPLOYEE_CODE(P_MACHINE_CODE IN VARCHAR2, P_MACHINE_IDENTIFIER IN VARCHAR2, P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_NEW_MACHINE_SUPERCARD_ADD(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE, P_MACHINE_CATEGORY IN RFID.RFID_MACHINES.MACHINE_CATEGORY%TYPE, P_EVENT IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT V...`
- `procedure J_MISSED_MACHINE_IN_SUPERCARD(P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure P_SYN_ATTENDANCE_EMP(P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE, P_FROM_DATE DATE, P_TO_DATE DATE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function RFID_CARD_CODE_CONVERSION(P_STRING_VALUE IN VARCHAR2, P_MRNO IN VARCHAR2, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE) RETURN VARCHAR2`

### PKG_48FRM00102

- `procedure PRO_POPULATE_DESIGNATION(P_DEPARTMENT_ID IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_ALREADY_POPULATED(P_DEPARTMENT_ID IN VARCHAR2) RETURN NUMBER`
- `procedure P_REFRESH_DEPARTMENT(P_DEPARTMENT_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_IS_SUPER_CARD(P_MRNO IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_GRANT_DEFAULT_ACCESS(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN VARCHAR2, P_EVENT IN VARCHAR2, P_ACCESS_GRANT_EVENT IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_REVOKE_DEFAULT_ACCESS(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN VARCHAR2, P_EVENT IN VARCHAR2, P_ACCESS_GRANT_EVENT IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_REVOKE_DEPT_DESIG_ACCESS(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN VARCHAR2, P_EVENT IN VARCHAR2, P_DEPARTMENT_ID IN VARCHAR2, P_DESIGNATION_ID IN VARCHAR2, P_ACCESS_GRANT_EVENT IN VARCHAR2, P_MACHINE_ACCESS_TYPE IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GRANT_DEPT_DESIG_ACCESS(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN VARCHAR2, P_DEPARTMENT_ID IN VARCHAR2, P_DESIGNATION_ID IN VARCHAR2, P_EVENT IN VARCHAR2, P_ACCESS_GRANT_EVENT IN VARCHAR2, P_MACHINE_ACCESS_TYPE IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GRANT_REVOKE_EMP_WISE_ACCESS(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN VARCHAR2, P_EMPLOYEE_CODE IN VARCHAR2, P_EVENT IN VARCHAR2, P_ACCESS_GRANT_EVENT IN VARCHAR2, P_MACHINE_ACCESS_TYPE IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_REFRESH_EMP_WISE_ACCESS(P_MRNO IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_REFRESH_EMP_WISE_ACCESS(P_MRNO IN VARCHAR2, P_DEPARTMENT_ID IN VARCHAR2, P_DESIGNATION_ID IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_ACCESS_CONTROL_REPORTS

THIS PACKAGE WILL AUTOMATE REPORTS

- `function ISSUED_CARDS_REPORT(P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE, P_CARD_CAT_ID IN RFID.RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE) RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.ISSUED_CARDS_TAB PIPELINED`
- `function BUILDING_WISE_WARDS_COUNT(P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE, P_WARD_ID IN RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE) RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.BUILD_WISE_WARD_TAB PIPELINED`
- `function EMP_CARD_INOUT_DETAIL(P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE) RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.EMP_CARD_INOUT_TAB PIPELINED`
- `function TOP_TEN_VISITORS(P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE) RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_TEN_VISITORS_TAB PIPELINED`
- `function TOP_FIVE_WARDS(P_FROM_DATE DATE, P_TO_DATE DATE, P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE) RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_FIVE_WARD_TAB PIPELINED`
- `function F_WARD_WISE_CARD_SWIPE_COUNT(P_LOCATION_ID RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE, P_BUILDING_BLOCK_ID RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE, P_WARD_ID RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE, P_MACHINE_TYPE RFID.RFID_MACHINES.DEFAULT_CHECK_IN_OUT%TYPE) RETURN NUMBER`

### PKG_MACHINE_WISE_EMPLOYEE

- `function F_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_DISP_MRNO IN VARCHAR2, P_NAME IN REGISTRATION.PATIENT.NAME%TYPE, P_DESIGNATION IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE, P_RFID_CODE IN HRD.INFORMATION.RFID_CODE%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE) RETURN HRD_INFO_TBL_PF PIPELINED`
- `procedure P_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_DISP_MRNO IN VARCHAR2, P_NAME IN REGISTRATION.PATIENT.NAME%TYPE, P_DESIGNATION IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE, P_RFID_CODE IN HRD.INFORMATION.RFID_CODE%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_DATA IN OUT HRD_INFO_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN HRD_INFO, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_EMP_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RFID_CODE IN HRD.INF...`
- `procedure P_EMP_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RFID_CODE IN HRD.INF...`
- `procedure P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN EMP_MACHINES_RC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_LCK(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_UPD(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_DEL(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_RFID_CODE(P_MRNO IN VARCHAR2) return varchar`
- `procedure P_SUPER_CARD_MACHINE_INS(P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_EVENT IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_IS_CONFIDENTIAL(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure P_REVOKE_SUP_CARD_ACCESS(P_MRNO IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_RFID

- `function GET_RFID_MACHINES(P_EMP_CODE IN HRD.INFORMATION.MRNO%TYPE) RETURN RFID_MACHINE_TAB PIPELINED`

### PKG_RFID_ACCESS_SYNC

- `procedure LOG_EVENT( P_RUN_ID IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE, P_EVENT_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE, P_EVENT_SOURCE IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE, P_MRNO IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE, P_MACHINE_ID IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE, P_EMP_LOCATION_ID IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID IN RFID.RFID_ACCESS_SYNC_LOG.DE...`
- `procedure GET_EMP_CONTEXT( P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_LOCATION_ID OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE, P_DESIGNATION_ID OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE, P_RFID_SUPER_CARD OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE, P_SEX_ID OUT REGISTRATION.PATIENT.SEX_ID%TYPE )`
- `function FN_EFFECTIVE_SETUP_RIGHTS( P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE, P_DESIGNATION_ID IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE, P_RFID_SUPER_CARD IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE, P_SEX_ID IN REGISTRATION.PATIENT.SEX_ID%TYPE ) RETURN RFID.TAB_SETUP_RIGHT PIPELINED`
- `procedure PR_PREVIEW_EMPLOYEE_SYNC( P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_MISSING_IN_MWE OUT SYS_REFCURSOR, P_MWE_MINUS_SETUP OUT SYS_REFCURSOR )`
- `procedure PR_SYNC_EMPLOYEE_ACCESS( P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER )`
- `procedure PR_SYNC_EMPLOYEE_ACCESS_FAST( P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER )`
- `procedure PR_SYNC_LOCATION_ACCESS( P_EMP_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER )`
- `procedure PR_CLEANUP_REDUNDANT_RFID_SETUP( P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL, P_COMMIT IN VARCHAR2 DEFAULT 'Y' )`

### PKG_RFID_ACCESS_SYNC01

- `procedure LOG_EVENT(P_RUN_ID IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE, P_EVENT_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE, P_EVENT_SOURCE IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE, P_MRNO IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE, P_MACHINE_ID IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE, P_EMP_LOCATION_ID IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID IN RFID.RFID_ACCESS_SYNC_LOG.DEP...`
- `procedure GET_EMP_CONTEXT(P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_LOCATION_ID OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE, P_DESIGNATION_ID OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE, P_RFID_SUPER_CARD OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE, P_SEX_ID OUT REGISTRATION.PATIENT.SEX_ID%TYPE)`
- `function FN_EFFECTIVE_SETUP_RIGHTS(P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE, P_DEPARTMENT_ID IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE, P_DESIGNATION_ID IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE, P_RFID_SUPER_CARD IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE, P_SEX_ID IN REGISTRATION.PATIENT.SEX_ID%TYPE) RETURN RFID.TAB_SETUP_RIGHT PIPELINED`
- `procedure PR_PREVIEW_EMPLOYEE_SYNC(P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_MISSING_IN_MWE OUT SYS_REFCURSOR, P_MWE_MINUS_SETUP OUT SYS_REFCURSOR)`
- `procedure PR_SYNC_EMPLOYEE_ACCESS(P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER)`
- `procedure PR_SYNC_EMPLOYEE_ACCESS_FAST(P_MRNO IN HRD.VU_INFORMATION.MRNO%TYPE, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER)`
- `procedure PR_SYNC_LOCATION_ACCESS(P_EMP_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL, P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y', P_RUN_ID OUT NUMBER)`
- `procedure PR_PREVIEW_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL, P_RESULT OUT SYS_REFCURSOR)`
- `procedure PR_PREVIEW_REDUNDANT_RFID_ACCESS_SUMMARY(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL, P_RESULT OUT SYS_REFCURSOR)`
- `procedure PR_CLEANUP_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL, P_COMMIT IN VARCHAR2 DEFAULT 'Y')`

### PKG_RFID_CARD_ISSUE_ACS

- `procedure P_RFID_CARD_ISSUE(P_EVENT IN CHAR, P_SR IN RFID.RFID_CARD_ISSUE_ACS.SR%TYPE, P_RFID_CARD_NO IN RFID.RFID_CARD_ISSUE_ACS.RFID_CARD_NO%TYPE, P_NAME IN RFID.RFID_CARD_ISSUE_ACS.NAME%TYPE, P_MRNO IN RFID.RFID_CARD_ISSUE_ACS.MRNO%TYPE, P_ISSUE_DATE IN RFID.RFID_CARD_ISSUE_ACS.ISSUE_DATE%TYPE, P_RECEIVE_DATE IN RFID.RFID_CARD_ISSUE_ACS.RECEIVE_DATE%TYPE, P_RETURN IN RFID.RFID_CARD_ISSUE_ACS.RETURN%TYPE, P_CARD_CATEGO...`
- `procedure JOB_RFID_CARD_RIGHTS_ACS(P_MRNO IN VARCHAR2 DEFAULT NULL, P_MACHINE_CATEGORY_ID IN NUMBER DEFAULT NULL)`

### PKG_RFID_DATA_TRANSFER

- `function F_V_RFID_QRY(P_MRNO IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE, P_USER_NAME IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE, P_RFID_CODE IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE, P_IP_ADDRESS IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE, P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE) RETURN V_RFID_TBL_PF PIPELINED`
- `procedure P_V_RFID_QRY(P_MRNO IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE, P_USER_NAME IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE, P_RFID_CODE IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE, P_IP_ADDRESS IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE, P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE, P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN V_RFID_REC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_INS(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_LCK(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_UPD(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_DEL(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S07FRM00031

- `procedure P_V_RFID_QRY(P_MRNO IN HRD.V_INFORMATION.MRNO%TYPE, P_USER_NAME IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE, P_RFID_CODE IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE, P_IP_ADDRESS IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE, P_MACHINE_CODE IN RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE, P_MACHINE_IDENTIFIER IN RFID.RFID_DATA_TRANSFER.MACHINE_IDENTIFIER%TYPE, P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_L...`
- `procedure P_V_RFID_INS(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_LCK(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_UPD(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_DEL(P_DATA IN OUT V_RFID_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN V_RFID_REC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S48FRM00024

- `procedure P_RFID_MACHINES_QRY(P_DATA IN OUT RFID_MACHINES_REC_REFCUR, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_ACTIVE IN RFID.RFID_MACHINES.ACTIVE%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, ...`
- `procedure P_RFID_MACHINES_INS(P_DATA IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_LCK(P_DATA IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_UPD(P_DATA IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_MACHINES_DEL(P_DATA IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_QY(P_DATA IN OUT RFID_DEPT_MACHINES_REFCUR, P_MACHINE_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE, P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_ACTIVE IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2 )`
- `procedure P_DEPT_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE, P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE, P_DATA IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_LCK(P_DATA IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_UPD(P_DATA IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_DEPT_MACHINES_DEL(P_DATA IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_QY(P_DATA IN OUT RFID_EMP_MACHINES_REFCUR, P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_NAME IN HRD.V_INFORMATION.NAME%TYPE, P_DISP_MRNO IN HRD.V_INFORMATION.DISP_MRNO%TYPE, P_DEPARTMENT IN HRD.V_INFORMATION.DEPARTMENT%TYPE, P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RF...`
- `procedure P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_DATA IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_LCK(P_DATA IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_UPD(P_DATA IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_DEL(P_DATA IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_CATEGORY_QRY(P_DATA IN OUT RFID_CATEGORY_CUR, P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE, P_DESCRIPTION IN RFID.RFID_CATEGORY.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_CATEGORY.SHORT_DESCRIPTION%TYPE, P_DEFAULT IN RFID.RFID_CATEGORY.IS_DEFAULT%TYPE, P_ACTIVE IN RFID.RFID_CATEGORY.ACTIVE%TYPE)`
- `procedure RFID_CATEGORY_INSERT(R IN RFID_CATEGORY_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure RFID_CATEGORY_LOCK(R IN OUT RFID_CATEGORY_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure RFID_CATEGORY_UPDATE(T IN RFID_CATEGORY_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure RFID_CATEGORY_DELETE(T IN RFID_CATEGORY_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure RFID_DESIGNATION_QRY(P_DATA IN OUT RFID_DESIGNATION_CUR, P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE, P_DESCRIPTION IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE, P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE)`

### PKG_S48FRM00025

- `procedure P_EMP_INFO_QRY(P_DATA IN OUT HRD_INFO_REFCUR, P_designation_id IN hrd.information.designation_id%TYPE, P_MRNO IN hrd.information.mrno%TYPE, P_DISP_MRNO IN VARCHAR2, P_NAME IN registration.patient.name%TYPE, P_designation IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE, P_RFID_CODE IN HRD.INFORMATION.RFID_CODE%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VAR...`
- `procedure P_EMP_MACHINES_QY(P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_DESCRIPTION IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_SHORT_DESC IN RFID.RFID_MACHINES.SHORT_DESC%TYPE, P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_MRNO IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_ACTIVE IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE, P_RFID_CODE IN HRD.INF...`
- `procedure P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE, P_MRNO OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE, P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_LCK(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_UPD(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_DEL(P_DATA IN OUT EMP_MACHINES_TL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN HRD_INFO, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN EMP_MACHINES_RC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function F_GET_RFID_CODE(p_mrno IN VARCHAR2) return varchar`
- `function F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO IN VARCHAR2, P_MACHINE_ID IN VARCHAR2) RETURN NUMBER`

### PKG_S48FRM00060

- `procedure RFID_MACHINE_MAPPING_QY(Q_DATA IN OUT RFID_MACHINE_MAPPING_CUR, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_MACHINE_NAME IN RFID.RFID_MACHINES.DESCRIPTION%TYPE, P_IP_ADDRESS IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE, P_PORT_NO IN RFID.RFID_MACHINES.PORT_NO%TYPE, P_RFID_CARD_NO IN HRD.INFORMATION.RFID_CODE%TYPE, P_MACHINE_TYPE IN RFID.RFID_MACHINES.MACHINE_TYPE%TYPE, P_MACHINE_IDENTIFIER IN RFID.RFID_MACHIN_IDEN...`

### PKG_S48FRM00100

- `procedure P_RFID_CATEGORY_WISE_RIGHTS(P_CATEGORY_ID IN NUMBER, P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE, P_EVENT IN VARCHAR2, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_MACHINE_ACCESS_TYPE IN CHAR, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_RFID_CATEGORY_REVOKE_RIGHTS(P_CATEGORY_ID IN NUMBER, P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE, P_EVENT IN VARCHAR2, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_MACHINE_ACCESS_TYPE IN CHAR, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

## Standalone Procedures

- `PR_CLEANUP_REDUNDANT_RFID_ACCESS( P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL, P_COMMIT IN VARCHAR2 DEFAULT 'Y' )`
- `PR_RFID_ACCESS_DIFFS(P_MRNO IN VARCHAR2, P_LOCATION_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, P_DEPARTMENT_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, P_DESIGNATION_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, P_EMPLOYEE_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, P_SETUP_MINUS_COMPLETE OUT SYS_REFCURSOR, P_COMPLETE_MINUS_SETUP OUT SYS_REFCURSOR )`
- `P_COPY_MACHINE_RIGHTS(P_MRNO IN VARCHAR2, P_MASTER_MRNO IN VARCHAR2, P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR)`

## Standalone Functions

- `F_GET_MRNO(P_RFID_CODE HRD.INFORMATION.RFID_CODE%TYPE) RETURN VARCHAR2`

## Types

- **OBJ_SETUP_RIGHT**: `OBJECT ( MACHINE_ID NUMBER, MACHINE_ACCESS_TYPE VARCHAR2(30), ACCESS_GRANT_EVENT VARCHAR2(100), PRIORITY_NO NUMBER )`
- **TAB_SETUP_RIGHT**: `TABLE OF RFID.OBJ_SETUP_RIGHT`

## Triggers

| Trigger | Table | Event | Row-level |
|---|---|---|---|
| ATTENDANCE_EMPLOYEE_DEL | ATTENDANCE_EMPLOYEE | AFTER DELETE | Y |
| ATTENDANCE_EMPLOYEE_INS | ATTENDANCE_EMPLOYEE | BEFORE INSERT | Y |
| ATTENDANCE_EMPLOYEE_UPD | ATTENDANCE_EMPLOYEE | BEFORE UPDATE | Y |
| ATTENDANCE_EMP_SEQ_INSERT | ATTENDANCE_EMPLOYEE | BEFORE INSERT | Y |
| ATTENDANCE_INS_CS | ATTENDANCE | after insert | Y |
| CHECK_DATE_TIME | ATTENDANCE | BEFORE INSERT | Y |
| DEPT_WISE_DESIG_ACCESS_DEL | DEPT_WISE_DESIG_ACCESS | AFTER DELETE | Y |
| DEPT_WISE_DESIG_ACCESS_INS | DEPT_WISE_DESIG_ACCESS | BEFORE INSERT | Y |
| DEPT_WISE_DESIG_ACCESS_UPD | DEPT_WISE_DESIG_ACCESS | BEFORE UPDATE | Y |
| MACHINE_WISE_COUNTER_DEL | MACHINE_WISE_COUNTER | AFTER DELETE | Y |
| MACHINE_WISE_COUNTER_INS | MACHINE_WISE_COUNTER | BEFORE INSERT | Y |
| MACHINE_WISE_COUNTER_UPD | MACHINE_WISE_COUNTER | BEFORE UPDATE | Y |
| MACHINE_WISE_EMPLOYEE_DEL | MACHINE_WISE_EMPLOYEE | AFTER DELETE | Y |
| MACHINE_WISE_EMPLOYEE_INS | MACHINE_WISE_EMPLOYEE | BEFORE INSERT | Y |
| MACHINE_WISE_EMPLOYEE_UPD | MACHINE_WISE_EMPLOYEE | BEFORE UPDATE | Y |
| MAC_COMP_DEPARTMENT_DEL | MACHINE_COMPLETE_DEPARTMENT | AFTER DELETE | Y |
| MAC_COMP_DEPARTMENT_INS | MACHINE_COMPLETE_DEPARTMENT | BEFORE INSERT | Y |
| MAC_COMP_DEPARTMENT_UPD | MACHINE_COMPLETE_DEPARTMENT | BEFORE UPDATE | Y |
| PRE_INSERT | RFID_MACHINE_COMMAND | before insert | Y |
| RFID_ACCESS_DEPARTMENT_DEL | RFID_ACCESS_DEPARTMENT | AFTER DELETE | Y |
| RFID_ACCESS_DEPARTMENT_INS | RFID_ACCESS_DEPARTMENT | BEFORE INSERT | Y |
| RFID_ACCESS_DEPARTMENT_UPD | RFID_ACCESS_DEPARTMENT | BEFORE UPDATE | Y |
| RFID_ACL_ADMIN_DEL | RFID_ACL_ADMIN | AFTER DELETE | Y |
| RFID_ACL_ADMIN_INS | RFID_ACL_ADMIN | BEFORE INSERT | Y |
| RFID_ACL_ADMIN_UPD | RFID_ACL_ADMIN | BEFORE UPDATE | Y |
| RFID_ATTENDANCE_INSERT | ATTENDANCE | AFTER INSERT | Y |
| RFID_ATTENDANCE_INSERT_EPARK | ATTENDANCE | AFTER INSERT | Y |
| RFID_ATTENDANCE_INSERT_PAT | ATTENDANCE | AFTER INSERT | Y |
| RFID_CARDS_ACS_DEL | RFID_CARDS_ACS | AFTER DELETE | Y |
| RFID_CARDS_ACS_INS | RFID_CARDS_ACS | BEFORE INSERT | Y |
| RFID_CARDS_ACS_UPD | RFID_CARDS_ACS | BEFORE UPDATE | Y |
| RFID_CARDS_DEL | RFID_CARDS | AFTER DELETE | Y |
| RFID_CARDS_INS | RFID_CARDS | BEFORE INSERT | Y |
| RFID_CARDS_UPD | RFID_CARDS | BEFORE UPDATE | Y |
| RFID_CARD_CATEGORY_ACS_DEL | RFID_CARD_CATEGORY_ACS | AFTER DELETE | Y |
| RFID_CARD_CATEGORY_ACS_INS | RFID_CARD_CATEGORY_ACS | BEFORE INSERT | Y |
| RFID_CARD_CATEGORY_ACS_UPD | RFID_CARD_CATEGORY_ACS | BEFORE UPDATE | Y |
| RFID_CARD_ISSUE_ACS_DEL | RFID_CARD_ISSUE_ACS | AFTER DELETE | Y |
| RFID_CARD_ISSUE_ACS_INS | RFID_CARD_ISSUE_ACS | BEFORE INSERT | Y |
| RFID_CARD_ISSUE_ACS_UPD | RFID_CARD_ISSUE_ACS | BEFORE UPDATE | Y |
| RFID_CARD_TYPE_DEL | RFID_CARD_TYPE | AFTER DELETE | Y |
| RFID_CARD_TYPE_INS | RFID_CARD_TYPE | BEFORE INSERT | Y |
| RFID_CARD_TYPE_UPD | RFID_CARD_TYPE | BEFORE UPDATE | Y |
| RFID_CATEGORY_DEL | RFID_CATEGORY | AFTER DELETE | Y |
| RFID_CATEGORY_DEPARTMENTS_DEL | RFID_CATEGORY_DEPARTMENTS | AFTER DELETE | Y |
| RFID_CATEGORY_DEPARTMENTS_INS | RFID_CATEGORY_DEPARTMENTS | BEFORE INSERT | Y |
| RFID_CATEGORY_DEPARTMENTS_UPD | RFID_CATEGORY_DEPARTMENTS | BEFORE UPDATE | Y |
| RFID_CATEGORY_INS | RFID_CATEGORY | BEFORE INSERT | Y |
| RFID_CATEGORY_MACHINES_ACS_DEL | RFID_CATEGORY_MACHINES_ACS | AFTER DELETE | Y |
| RFID_CATEGORY_MACHINES_ACS_INS | RFID_CATEGORY_MACHINES_ACS | BEFORE INSERT | Y |
| RFID_CATEGORY_MACHINES_ACS_UPD | RFID_CATEGORY_MACHINES_ACS | BEFORE UPDATE | Y |
| RFID_CATEGORY_MACHINES_DEL | RFID_CATEGORY_MACHINES | AFTER DELETE | Y |
| RFID_CATEGORY_MACHINES_INS | RFID_CATEGORY_MACHINES | BEFORE INSERT | Y |
| RFID_CATEGORY_MACHINES_UPD | RFID_CATEGORY_MACHINES | BEFORE UPDATE | Y |
| RFID_CATEGORY_UPD | RFID_CATEGORY | BEFORE UPDATE | Y |
| RFID_CAT_TR_ACS_DEL | RFID_CATEGORY_TIMERANGE_ACS | AFTER DELETE | Y |
| RFID_CAT_TR_ACS_INS | RFID_CATEGORY_TIMERANGE_ACS | BEFORE INSERT | Y |
| RFID_CAT_TR_ACS_UPD | RFID_CATEGORY_TIMERANGE_ACS | BEFORE UPDATE | Y |
| RFID_CONFIDENTIAL_QUEUE_INSERT | ATTENDANCE | AFTER INSERT | Y |
| RFID_CONFIDENTIAL_Q_DEL | RFID_CONFIDENTIAL_Q | AFTER DELETE | Y |
| RFID_CONFIDENTIAL_Q_DELETE_HISTORY | RFID_CONFIDENTIAL_Q | AFTER DELETE | Y |
| RFID_CONFIDENTIAL_Q_INS | RFID_CONFIDENTIAL_Q | BEFORE INSERT | Y |
| RFID_CONFIDENTIAL_Q_UPD | RFID_CONFIDENTIAL_Q | BEFORE UPDATE | Y |
| RFID_CONFI_MACHINE_RIGHTS_DEL | RFID_CONFI_MACHINE_RIGHTS | AFTER DELETE | Y |
| RFID_CONFI_MACHINE_RIGHTS_INS | RFID_CONFI_MACHINE_RIGHTS | BEFORE INSERT | Y |
| RFID_CONFI_MACHINE_RIGHTS_UPD | RFID_CONFI_MACHINE_RIGHTS | BEFORE UPDATE | Y |
| RFID_DATA_TRANSFER_DEL | RFID_DATA_TRANSFER | AFTER DELETE | Y |
| RFID_DATA_TRANSFER_INS | RFID_DATA_TRANSFER | BEFORE INSERT | Y |
| RFID_DATA_TRANSFER_UPD | RFID_DATA_TRANSFER | BEFORE UPDATE | Y |
| RFID_DEFAULT_ACCESS_DEL | RFID_DEFAULT_ACCESS | AFTER DELETE | Y |
| RFID_DEFAULT_ACCESS_INS | RFID_DEFAULT_ACCESS | BEFORE INSERT | Y |
| RFID_DEFAULT_ACCESS_UPD | RFID_DEFAULT_ACCESS | BEFORE UPDATE | Y |
| RFID_DEPT_GENERAL_ACCESS_DEL | RFID_DEPT_GENERAL_ACCESS | AFTER DELETE | Y |
| RFID_DEPT_GENERAL_ACCESS_INS | RFID_DEPT_GENERAL_ACCESS | BEFORE INSERT | Y |
| RFID_DEPT_GENERAL_ACCESS_UPD | RFID_DEPT_GENERAL_ACCESS | BEFORE UPDATE | Y |
| RFID_DESIG_WISE_SP_ACCESS_DEL | RFID_DESIG_WISE_SP_ACCESS | AFTER DELETE | Y |
| RFID_DESIG_WISE_SP_ACCESS_INS | RFID_DESIG_WISE_SP_ACCESS | BEFORE INSERT | Y |
| RFID_DESIG_WISE_SP_ACCESS_UPD | RFID_DESIG_WISE_SP_ACCESS | BEFORE UPDATE | Y |
| RFID_EMP_WISE_SP_ACCESS_DEL | RFID_EMP_WISE_SP_ACCESS | AFTER DELETE | Y |
| RFID_EMP_WISE_SP_ACCESS_INS | RFID_EMP_WISE_SP_ACCESS | BEFORE INSERT | Y |
| RFID_EMP_WISE_SP_ACCESS_UPD | RFID_EMP_WISE_SP_ACCESS | BEFORE UPDATE | Y |
| RFID_MACHINES_DATA_DEL | RFID_MACHINES_DATA | AFTER DELETE | Y |
| RFID_MACHINES_DATA_INS | RFID_MACHINES_DATA | BEFORE INSERT | Y |
| RFID_MACHINES_DATA_UPD | RFID_MACHINES_DATA | BEFORE UPDATE | Y |
| RFID_MACHINES_DEL | RFID_MACHINES | AFTER DELETE | Y |
| RFID_MACHINES_INS | RFID_MACHINES | BEFORE INSERT | Y |
| RFID_MACHINES_UPD | RFID_MACHINES | BEFORE UPDATE | Y |
| RFID_MACHINE_CATEGORY_ACS_DEL | RFID_MACHINE_CATEGORY_ACS | AFTER DELETE | Y |
| RFID_MACHINE_CATEGORY_ACS_INS | RFID_MACHINE_CATEGORY_ACS | BEFORE INSERT | Y |
| RFID_MACHINE_CATEGORY_ACS_UPD | RFID_MACHINE_CATEGORY_ACS | BEFORE UPDATE | Y |
| RFID_MACH_IDENT_MAPING_DEL | RFID_MACHIN_IDENTIFIER_MAPPING | AFTER DELETE | Y |
| RFID_MACH_IDENT_MAPING_INS | RFID_MACHIN_IDENTIFIER_MAPPING | BEFORE INSERT | Y |
| RFID_MACH_IDENT_MAPING_UPD | RFID_MACHIN_IDENTIFIER_MAPPING | BEFORE UPDATE | Y |
| RFID_SUPER_CARD_MACHINE_INS | RFID_MACHINES | AFTER INSERT OR UPDATE OR DELETE | Y |
| SECTION_WISE_ATTENDANCE_DEL | SECTION_WISE_ATTENDANCE | AFTER DELETE | Y |
| SECTION_WISE_ATTENDANCE_INS | SECTION_WISE_ATTENDANCE | BEFORE INSERT | Y |
| SECTION_WISE_ATTENDANCE_UPD | SECTION_WISE_ATTENDANCE | BEFORE UPDATE | Y |
| TEMP_CARD_SETUP_DEL | TEMP_CARD_SETUP | AFTER DELETE | Y |
| TEMP_CARD_SETUP_INS | TEMP_CARD_SETUP | BEFORE INSERT | Y |
| TEMP_CARD_SETUP_UPD | TEMP_CARD_SETUP | BEFORE UPDATE | Y |
| TRAINING_ATTENDANCE_STG_DEL | TRAINING_ATTENDANCE_STG | AFTER DELETE | Y |
| TRAINING_ATTENDANCE_STG_INS | TRAINING_ATTENDANCE_STG | BEFORE INSERT | Y |
| TRAINING_ATTENDANCE_STG_INSERT | ATTENDANCE_EMPLOYEE | AFTER INSERT | Y |
| TRAINING_ATTENDANCE_STG_UPD | TRAINING_ATTENDANCE_STG | BEFORE UPDATE | Y |

## Synonyms

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

