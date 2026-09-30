# RFID tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

## RFID.ATTENDANCE

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

## RFID.ATTENDANCE_EMPLOYEE

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

## RFID.ATTENDANCE_INCORRECT
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


## RFID.DEPT_WISE_DESIG_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEP_WISE_DESIG_ACCESS`: DEPARTMENT_ID, DESIGNATION_ID
- **FK** `FK_DEP_WISE_DESIG_ID`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **Triggers**: `DEPT_WISE_DESIG_ACCESS_DEL` (after delete), `DEPT_WISE_DESIG_ACCESS_INS` (before insert), `DEPT_WISE_DESIG_ACCESS_UPD` (before update)

## RFID.MACHINE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_TYPE | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_MACHINE_TYPE`: MACHINE_TYPE

## RFID.RFID_CATEGORY

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

## RFID.RFID_MACHINES

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

## RFID.MACHINE_COMPLETE_DEPARTMENT

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

## RFID.MACHINE_WISE_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| COUNTER | NUMBER(8) default 1 | Y |  |
| MAXIMUM_COUNTER | NUMBER(8) | Y |  |

- **PK** `PK_MACHINE_ID`: MACHINE_ID
- **Triggers**: `MACHINE_WISE_COUNTER_DEL` (after delete), `MACHINE_WISE_COUNTER_INS` (before insert), `MACHINE_WISE_COUNTER_UPD` (before update)

## RFID.MACHINE_WISE_EMPLOYEE

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

## RFID.RFID_ACCESS_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| IS_REFRESH | CHAR(1) | Y |  |

- **PK** `PK_RFID_ACCESS_DEPARTMENT`: DEPARTMENT_ID
- **FK** `FK_RFID_ACCESS_DEPARTMENT`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **Triggers**: `RFID_ACCESS_DEPARTMENT_DEL` (after delete), `RFID_ACCESS_DEPARTMENT_INS` (before insert), `RFID_ACCESS_DEPARTMENT_UPD` (before update)

## RFID.RFID_ACCESS_SYNC_LOG

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


## RFID.RFID_ACL_ADMIN

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PRIVILEGE_LEVEL | CHAR(1) default '2' | N | 0  Common User, 1  Enroller/Registrar , 2  Admin, 3  Super Administrator |
| USER_PASSWORD | VARCHAR2(500) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_RFID_ACL_ADMIN`: MRNO, PRIVILEGE_LEVEL
- **FK** `FK_RFID_ACL_ADMIN_1`: (MRNO) -> SECURITY.USERS(MRNO)
- **Triggers**: `RFID_ACL_ADMIN_DEL` (after delete), `RFID_ACL_ADMIN_INS` (before insert), `RFID_ACL_ADMIN_UPD` (before update)

## RFID.RFID_CARD_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_TYPE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_RFID_CARD_TYPE`: CARD_TYPE_ID
- **Triggers**: `RFID_CARD_TYPE_DEL` (after delete), `RFID_CARD_TYPE_INS` (before insert), `RFID_CARD_TYPE_UPD` (before update)

## RFID.RFID_CARDS

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

## RFID.RFID_CARDS_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| RFID_CARD_NO | VARCHAR2(30) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| CARD_DESCRIPTION | VARCHAR2(50) | Y |  |

- **PK** `PK_CARDS_01`: RFID_CARD_NO
- **Triggers**: `RFID_CARDS_ACS_DEL` (after delete), `RFID_CARDS_ACS_INS` (before insert), `RFID_CARDS_ACS_UPD` (before update)

## RFID.RFID_CARD_CATEGORY_ACS

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

## RFID.RFID_CARD_ISSUE_ACS

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

## RFID.RFID_CARD_ISSUE_RECORD

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

## RFID.RFID_CATEGORY_DEPARTMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |

- **PK** `RFID_CATEGORY_DEPARTMENTS`: CATEGORY_ID, DEPARTMENT_ID
- **Triggers**: `RFID_CATEGORY_DEPARTMENTS_DEL` (after delete), `RFID_CATEGORY_DEPARTMENTS_INS` (before insert), `RFID_CATEGORY_DEPARTMENTS_UPD` (before update)

## RFID.RFID_CATEGORY_MACHINES

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_RFID_CATEGORY_MACHINES`: MACHINE_ID, CATEGORY_ID
- **FK** `FK_RFID_CATEGORY_MACHINES`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **FK** `FK_RFID_CATEGORY_MACHINES_1`: (CATEGORY_ID) -> RFID.RFID_CATEGORY(CATEGORY_ID) [disabled]
- **Triggers**: `RFID_CATEGORY_MACHINES_DEL` (after delete), `RFID_CATEGORY_MACHINES_INS` (before insert), `RFID_CATEGORY_MACHINES_UPD` (before update)

## RFID.RFID_CATEGORY_MACHINES_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| CATEGORY_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y |  |

- **PK** `PK_MAC_CAT_01`: MACHINE_ID, CATEGORY_ID
- **Triggers**: `RFID_CATEGORY_MACHINES_ACS_DEL` (after delete), `RFID_CATEGORY_MACHINES_ACS_INS` (before insert), `RFID_CATEGORY_MACHINES_ACS_UPD` (before update)

## RFID.RFID_CATEGORY_TIMERANGE_ACS

| Column | Type | Null | Comment |
|---|---|---|---|
| CARD_CATEGORY_ID | NUMBER(4) | N |  |
| UPPER_TIME_LIMIT | VARCHAR2(4) | Y |  |
| LOWER_TIME_LIMIT | VARCHAR2(4) | Y |  |
| SR_NO | NUMBER(4) | N |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y |  |

- **PK** `PK_RFID_TIM_RANGE_01`: CARD_CATEGORY_ID, SR_NO
- **Triggers**: `RFID_CAT_TR_ACS_DEL` (after delete), `RFID_CAT_TR_ACS_INS` (before insert), `RFID_CAT_TR_ACS_UPD` (before update)

## RFID.RFID_CONFIDENTIAL_Q

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

## RFID.RFID_CONFIDENTIAL_Q_HIS

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


## RFID.RFID_CONFI_MACHINE_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CONFI_MACHI_RIGHTS`: MRNO, MACHINE_ID
- **Triggers**: `RFID_CONFI_MACHINE_RIGHTS_DEL` (after delete), `RFID_CONFI_MACHINE_RIGHTS_INS` (before insert), `RFID_CONFI_MACHINE_RIGHTS_UPD` (before update)

## RFID.RFID_DATA_TRANSFER

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

## RFID.RFID_DEFAULT_ACCESS

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

## RFID.RFID_DELETED_ACCESS_AUDIT

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


## RFID.RFID_DEPT_GENERAL_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEPT_WISE_GENERAL_ACCESS`: DEPARTMENT_ID, MACHINE_ID
- **FK** `FK_DEPT_WISE_GENERAL_MACHINE_ID`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID)
- **Triggers**: `RFID_DEPT_GENERAL_ACCESS_DEL` (after delete), `RFID_DEPT_GENERAL_ACCESS_INS` (before insert), `RFID_DEPT_GENERAL_ACCESS_UPD` (before update)

## RFID.RFID_DESIG_WISE_SP_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |

- **PK** `PK_RFID_DESIG_WISE_ACCESS`: DESIGNATION_ID, MACHINE_ID, DEPARTMENT_ID
- **FK** `FK_RFID_DEPT_DESIGN`: (DEPARTMENT_ID, DESIGNATION_ID) -> RFID.DEPT_WISE_DESIG_ACCESS(DEPARTMENT_ID, DESIGNATION_ID)
- **Triggers**: `RFID_DESIG_WISE_SP_ACCESS_DEL` (after delete), `RFID_DESIG_WISE_SP_ACCESS_INS` (before insert), `RFID_DESIG_WISE_SP_ACCESS_UPD` (before update)

## RFID.RFID_DOORS_LOG
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

## RFID.RFID_EMP_WISE_SP_ACCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| MACHINE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RFID_EMP_WISE_SP_ACCESS`: MRNO, MACHINE_ID
- **Triggers**: `RFID_EMP_WISE_SP_ACCESS_DEL` (after delete), `RFID_EMP_WISE_SP_ACCESS_INS` (before insert), `RFID_EMP_WISE_SP_ACCESS_UPD` (before update)

## RFID.RFID_MACHINES_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| REQUEST_DATE | DATE default SYSDATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `RFID_MACHINES_DATA_DEL` (after delete), `RFID_MACHINES_DATA_INS` (before insert), `RFID_MACHINES_DATA_UPD` (before update)

## RFID.RFID_MACHINE_CATEGORY_ACS

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

## RFID.RFID_MACHINE_COMMAND

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

## RFID.RFID_MACHINE_TIMESTAMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | N |  |
| MACHINE_LOCATION_ID | VARCHAR2(3) | N |  |
| MACHINE_TIMESTAMP | VARCHAR2(20) | N |  |
| ACTUAL_TIMESTAMP | DATE default sysdate | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **FK** `FK_RFID_MACH_TIMESTAMP_1`: (MACHINE_ID) -> RFID.RFID_MACHINES(MACHINE_ID) [disabled]

## RFID.RFID_MACHIN_IDENTIFIER_MAPPING

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

## RFID.SECTION_WISE_ATTENDANCE

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

## RFID.TEMP_CARD_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| CARD_NO | VARCHAR2(10) | N |  |
| CARD_DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `TEMP_CARD_SETUP_PK`: CARD_NO
- **Triggers**: `TEMP_CARD_SETUP_DEL` (after delete), `TEMP_CARD_SETUP_INS` (before insert), `TEMP_CARD_SETUP_UPD` (before update)

## RFID.TEMP_RFID_REGISTERED_USERS
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

## RFID.TMP_SELECTED_MACHINES_PR

| Column | Type | Null | Comment |
|---|---|---|---|
| MACHINE_ID | VARCHAR2(5) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## RFID.TRAINING_ATTENDANCE_STG

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

