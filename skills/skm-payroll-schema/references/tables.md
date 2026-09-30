# PAYROLL tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

## PAYROLL.ACTUAL_PI

| Column | Type | Null | Comment |
|---|---|---|---|
| PERFORM_DOCTOR | VARCHAR2(14) | N |  |
| PERFORM_MONTH | DATE | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| PAY_START_DATE | DATE | Y |  |
| PAY_END_DATE | DATE | Y |  |
| CALC_INCOME | NUMBER | Y |  |
| WAIVE_OFF_B_INV | NUMBER | Y |  |
| WAIVE_OFF_A_INV | NUMBER | Y |  |


## PAYROLL.AD_EXCEPTIONAL

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| TRANS_DATE | DATE | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| NO_OF_DAYS | NUMBER(5,2) | Y |  |
| PENDING_AMOUNT | NUMBER(20,2) | Y |  |


## PAYROLL.DEF_AD_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_GROUP_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| AD_TYPE | CHAR(1) default 'A' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DEF_AD_GROUP`: AD_GROUP_CODE
- **CHECK** `CK_DAG_ACTIVE`: ACTIVE IN ('N','Y'
- **CHECK** `CK_DEF_AD_GROUP_1`: AD_TYPE IN ('A','D'
- **CHECK** `CK_DEF_AD_GROUP_NN`: AD_TYPE IS NOT NULL
- **Triggers**: `DEF_AD_GROUP_CEA` (before insert or update or delete), `DEF_AD_GROUP_DEL` (after delete), `DEF_AD_GROUP_INS` (before insert), `DEF_AD_GROUP_UPD` (before update), `TRG_WS_KZL_DN_VB_Q` (after insert or update or delete)

## PAYROLL.DEF_ALLOWANCE_DEDUCTION
This table is used to define different types of allowances / deductions which are used in salary processing. It also describes different formulas to calculate allowances and deductions

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N | Auto-generated Allowance / Deduction Code (PK) |
| DESCRIPTION | VARCHAR2(255) | N | Name of Allowance or deduction |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short Name of Allowance or deduction, to be used in some reports |
| AD_TYPE | CHAR(1) default 'A' | Y | Either it is Allowance or Deduction |
| CALC_TYPE | CHAR(1) default 'A' | Y | Either calculation is dependant on attendance or not |
| DED_TYPE | CHAR(1) default 'O' | Y | Either deduction is Income Tax, P-Fund or any other type |
| VALUE_TYPE | CHAR(1) default 'A' | Y | Either allowance / deduction is based on percentage or value |
| INCLUDE_IN_GROSS | CHAR(1) default 'Y' | Y | Either allowance / deduction is included into Gross salary or not |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |
| OT_CALC_BASE | CHAR(1) default 'G' | Y |  |
| PRACTICE_INCOME | CHAR(1) default 'N' | Y |  |
| ENTRY_TYPE | CHAR(1) default 'S' | Y |  |
| CBR_AMOUNT_CODE | VARCHAR2(4) | Y |  |
| AD_GROUP_CODE | CHAR(3) | Y |  |
| TAXABLE | CHAR(1) default 'N' | Y |  |
| TAXABLE_ANNUALLY | CHAR(1) default 'N' | Y | This column is effecitve for entry type as Transaction only |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| EXCLUDE_FROM_GROSS_PAY | CHAR(1) default 'N' | Y | This column add for LFA salary with payment |

- **PK** `PK_DEF_ALLOWANCE_DEDUCTION`: AD_CODE, ORGANIZATION_ID, LOCATION_ID
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_1`: (AD_GROUP_CODE) -> PAYROLL.DEF_AD_GROUP(AD_GROUP_CODE) [disabled]
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_3`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_1`: AD_TYPE IN ('A', 'D'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_10`: TAXABLE_ANNUALLY IN ('Y', 'N'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_2`: CALC_TYPE IN ('A', 'O'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_3`: DED_TYPE IN ('I','P','B','M','C','E','O','R'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_4`: VALUE_TYPE IN ('A', 'P'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_5`: INCLUDE_IN_GROSS IN ('Y', 'N'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_6`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_7`: OT_CALC_BASE IN ('G', 'B'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_8`: PRACTICE_INCOME IN ('Y', 'N', 'G'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_9`: ENTRY_TYPE IN ('S','T'
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_NN`: AD_GROUP_CODE IS NOT NULL
- **Triggers**: `DEF_ALLOWANCE_DEDUCTION_DEL` (after delete), `DEF_ALLOWANCE_DEDUCTION_INS` (before insert), `DEF_ALLOWANCE_DEDUCTION_UPD` (before update)

## PAYROLL.ALLOWANCE_DEDUCTION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| TRANS_DATE | DATE | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| NO_OF_DAYS | NUMBER(5,2) | Y |  |
| CALC_AMOUNT_GUARANTEE | NUMBER(10) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y | This column will be used for Cafe Deduction Process, Data will be inserted into this column along with Deduction amount detail |

- **PK** `PK_ALLOWANCE_DEDUCTION_DETAIL`: START_DATE, END_DATE, AD_CODE, MRNO, TRANS_DATE
- **FK** `FK_ALLOWANCE_DEDUCTION_DETAIL1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_DEDUCTION_DETAIL`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **FK** `FK_DEDUCTION_DETAIL_03`: (PROCESS_ID) -> BILLING.CORPORATE_INVOICE_MASTER(PROCESS_ID) [disabled]
- **Triggers**: `ALLOWANCE_DEDUCTION_DETAIL_DEL` (after delete), `ALLOWANCE_DEDUCTION_DETAIL_INS` (before insert), `ALLOWANCE_DEDUCTION_DETAIL_UPD` (before update)

## PAYROLL.ALLOWANCE_DEDUCTION_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N |  |
| CALC_BASIC_GROSS | CHAR(1) | Y |  |
| CALC_PERCENT | NUMBER(5,2) | Y |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ALLOWANCE_DEDUCTION_SETUP`: AD_CODE, FROM_DATE
- **FK** `FK_ALLOWANCE_DEDUCTION`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]

## PAYROLL.DEF_ARREAR

| Column | Type | Null | Comment |
|---|---|---|---|
| ARREAR_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| AD_TYPE | CHAR(1) default 'A' | Y |  |
| CBR_AMOUNT_CODE | VARCHAR2(4) | Y |  |

- **PK** `PK_DEF_ARREAR`: ARREAR_CODE
- **CHECK** `CK_DEF_ARREAR_1`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DEF_ARREAR_2`:  AD_TYPE IN ('A','D'
- **Triggers**: `DEF_ARREAR_CEA` (before insert or update or delete), `DEF_ARREAR_DEL` (after delete), `DEF_ARREAR_INS` (before insert), `DEF_ARREAR_UPD` (before update), `TRG_WS_WVB_PD_FA_Q` (after insert or update or delete)

## PAYROLL.ARREAR_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| ARREAR_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ARREAR_START_DATE | DATE | Y |  |
| ARREAR_END_DATE | DATE | Y |  |
| DED_DAYS_HOURS | NUMBER(5,2) | Y |  |
| DED_AMOUNT | NUMBER(20,2) | Y |  |
| DAYS_HOURS | NUMBER(5,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_CODE | CHAR(3) default '000' | N |  |
| PROCESS_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_ARREAR_DETAIL`: START_DATE, END_DATE, ARREAR_CODE, MRNO, AD_CODE
- **FK** `FK_ARREAR_DETAIL_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_ARREAR_DETAIL_2`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **FK** `FK_ARREAR_DETAIL_3`: (ARREAR_CODE) -> PAYROLL.DEF_ARREAR(ARREAR_CODE)
- **FK** `FK_ARREAR_DETAIL_4`: (ARREAR_START_DATE, ARREAR_END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **Triggers**: `ARREAR_DETAIL_DEL` (after delete), `ARREAR_DETAIL_INS` (before insert), `ARREAR_DETAIL_UPD` (before update)

## PAYROLL.ARREAR_EXCEPTIONAL

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| ARREAR_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ARREAR_START_DATE | DATE | Y |  |
| ARREAR_END_DATE | DATE | Y |  |
| DED_DAYS_HOURS | NUMBER(5,2) | Y |  |
| DED_AMOUNT | NUMBER(7,2) | Y |  |
| DAYS_HOURS | NUMBER(5,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_CODE | CHAR(3) default '000' | N | this column specify that arrear blongs to sepcified ad code only |

- **Triggers**: `ARREAR_EXCEPTIONAL_DEL` (after delete), `ARREAR_EXCEPTIONAL_INS` (before insert), `ARREAR_EXCEPTIONAL_UPD` (before update)

## PAYROLL.BASE_TABLE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| INC_AMT | NUMBER | Y |  |
| INC_PCT | NUMBER | Y |  |
| INC_DATE | DATE | Y |  |
| BASIC | NUMBER | Y |  |
| GROSS | NUMBER | Y |  |
| C000 | NUMBER | Y |  |
| C001 | NUMBER | Y |  |
| C002 | NUMBER | Y |  |
| C003 | NUMBER | Y |  |
| C006 | NUMBER | Y |  |
| C008 | NUMBER | Y |  |


## PAYROLL.CBR_DATA_FILE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(10) | N |  |
| SALARY_MONTH | VARCHAR2(100) | Y |  |
| SALARY_PERIOD_FROM | DATE | Y |  |
| SALARY_PERIOD_TO | DATE | Y |  |
| EMP_CODE_FROM | VARCHAR2(14) | Y |  |
| EMP_CODE_TO | VARCHAR2(14) | Y |  |
| FILE_PATH | VARCHAR2(100) | Y |  |
| REG_DATE_TO | DATE | Y |  |
| REG_DATE_FROM | DATE | Y |  |
| PAYMENT_SR_NO | NUMBER(2) | Y |  |


## PAYROLL.CHANGE_SALARY_ALLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| INCREMENT_DATE | DATE | Y |  |
| CHANGE_DATE | DATE | Y |  |
| CHANGE_PARAM | VARCHAR2(255) | Y |  |
| CHANGE_TYPE | VARCHAR2(255) | Y |  |
| OLD_VALUE | NUMBER(20,2) | Y |  |
| NEW_VALUE | NUMBER(20,2) | Y |  |
| CHANGE_BY | VARCHAR2(60) | Y |  |
| EMAIL_SEND_DATE | DATE | Y |  |


## PAYROLL.CM_DEF_ADMIN_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N |  |
| NAME | VARCHAR2(250) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `DEF_ADMIN_GROUP_PK`: ADMIN_GROUP_ID
- **Triggers**: `CM_DEF_ADMIN_GROUP_DEL` (after delete), `CM_DEF_ADMIN_GROUP_INS` (before insert), `CM_DEF_ADMIN_GROUP_UPD` (before update)

## PAYROLL.CM_BILL_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N | Foreign key references PAYROLL.DEF_ADMIN_GROUP.ADMIN_GROUP_ID |
| MONTH_ID | VARCHAR2(12) | N | Primary key |
| ENTRY_DATE | DATE | Y |  |
| FINALIZED_BY | VARCHAR2(8) | Y |  |
| FINALIZED_DATE | DATE | Y |  |
| POSTED_BY | VARCHAR2(14) | Y |  |
| POSTED_DATE | DATE | Y |  |
| EXCESS_CALCULATION_BY | VARCHAR2(14) | Y |  |
| EXCESS_CAL_DATE | DATE | Y |  |
| FINAL_POST_DATE | DATE | Y |  |
| FINAL_POST_BY | VARCHAR2(14) | Y |  |
| MON_START_DATE | DATE | Y |  |
| MON_END_DATE | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| VOUCHER_REFERENCE | VARCHAR2(100) | Y |  |

- **PK** `PK_BILL_MASTER`: MONTH_ID, ADMIN_GROUP_ID
- **FK** `FK_BILL_MASTER_ADMIN_GROUP`: (ADMIN_GROUP_ID) -> PAYROLL.CM_DEF_ADMIN_GROUP(ADMIN_GROUP_ID)
- **Triggers**: `CM_BILL_MASTER_DEL` (after delete), `CM_BILL_MASTER_INS` (before insert), `CM_BILL_MASTER_UPD` (before update)

## PAYROLL.CM_DEF_CONNECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| CONNECTION_ID | VARCHAR2(8) | N |  |
| CONTACT_NUMBER | VARCHAR2(40) | N |  |
| NETWORK | VARCHAR2(2) default 'jz' | N | JZ: JAZZ, UF: UFONE, TL: TELENOR, ZO: ZONG, PT: PTCL, ST: STROMFIBER |
| CONNECTION_TYPE | CHAR(1) default 'N' | N | N: NORMAL, D: DATA |
| PACKAGE_INFO | VARCHAR2(250) | Y |  |
| ADMIN_GROUP_ID | VARCHAR2(2) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_CONNECTION`: CONNECTION_ID
- **UK** `CM_DEF_CONNECTION_UK01`: CONTACT_NUMBER
- **FK** `FK_ADMIN_GROUP`: (ADMIN_GROUP_ID) -> PAYROLL.CM_DEF_ADMIN_GROUP(ADMIN_GROUP_ID)
- **Triggers**: `CM_DEF_CONNECTION_DEL` (after delete), `CM_DEF_CONNECTION_INS` (before insert), `CM_DEF_CONNECTION_UPD` (before update)

## PAYROLL.CM_CONNECTION_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_ID | VARCHAR2(10) | N |  |
| REQUEST_TYPE | CHAR(1) default 'D' | N | P: Pool, D: Dedicated |
| ADMIN_GROUP_ID | VARCHAR2(2) | Y |  |
| REQUEST_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | Y | If request is raised for an employee then it will be entered |
| DEPARTMENT_ID | VARCHAR2(7) | Y | If request is raised for pool then it will be entered |
| OFFICIAL_DEVICE | CHAR(1) | Y | Is official device provided with the connection |
| DEVICE_INFO | VARCHAR2(250) | Y |  |
| OWNER_TYPE | CHAR(1) default 'P' | N | O: Official, P: Personal |
| CONNECTION_ID | VARCHAR2(8) | Y | Filled in case of official device |
| CONTACT_NUMBER | VARCHAR2(40) | Y | Filled in case of personal number |
| NETWORK | VARCHAR2(2) default 'JZ' | Y | Filled in case of personal number |
| BILL_TYPE | CHAR(1) default 'P' | N | P: Prepaid, O: Postpaid |
| LIMIT_ALLOWED | NUMBER(12) | Y | Monthly approved amount |
| PAID_BY | CHAR(1) default 'O' | N | O: Office, S: Self |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| STATUS_ID | VARCHAR2(3) default '100' | Y |  |

- **PK** `PK_CONNECTION_REQUEST`: REQUEST_ID
- **FK** `FK_CONNECTION_REQUEST_CONNECTION`: (CONNECTION_ID) -> PAYROLL.CM_DEF_CONNECTION(CONNECTION_ID)
- **Triggers**: `CM_CONNECTION_REQUEST_DEL` (after delete), `CM_CONNECTION_REQUEST_INS` (before insert), `CM_CONNECTION_REQUEST_UPD` (before update)

## PAYROLL.CM_BILL_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N |  |
| MONTH_ID | VARCHAR2(12) | N |  |
| REQUEST_ID | VARCHAR2(10) | N |  |
| BILL_AMOUNT | NUMBER(10,2) | Y |  |
| PAYMENT_AMOUNT | NUMBER(10,2) | Y |  |
| PAYMENT_METHOD | VARCHAR2(8) | Y | lo (load), cd (card), ch (cash), np (no payment) |
| PAYMENT_DATE | DATE | Y |  |
| EXCESS_AMOUNT | NUMBER(10,2) | Y |  |
| DEDUCTION_AD_CODE | VARCHAR2(8) | Y |  |
| LIMIT_ALLOWED | NUMBER(12) | Y |  |
| INACTIVE_EMPLOYEE | VARCHAR2(1) | Y |  |
| REQUEST_EXPIRED | VARCHAR2(1) | Y |  |
| PAID_BY_SELF | VARCHAR2(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| CONTACT_NUMBER | VARCHAR2(40) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_BILL_DETAIL`: ADMIN_GROUP_ID, MONTH_ID, REQUEST_ID
- **UK** `CM_BILL_DETAIL_UK01`: MONTH_ID, CONTACT_NUMBER
- **FK** `FK_BILL_MASTER`: (MONTH_ID, ADMIN_GROUP_ID) -> PAYROLL.CM_BILL_MASTER(MONTH_ID, ADMIN_GROUP_ID)
- **FK** `FK_CONNECTION_REQUEST`: (REQUEST_ID) -> PAYROLL.CM_CONNECTION_REQUEST(REQUEST_ID)
- **Triggers**: `CM_BILL_DETAIL_DEL` (after delete), `CM_BILL_DETAIL_INS` (before insert), `CM_BILL_DETAIL_UPD` (before update)

## PAYROLL.CM_CONNECTION_REQ_DOCUMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(13) | N |  |
| REQUEST_ID | VARCHAR2(10) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CM_CONNECTION_REQ_DOCUMENT`: DOCUMENT_ID
- **FK** `FK_CM_CONNECTION_REQ_DOCUMENT`: (REQUEST_ID) -> PAYROLL.CM_CONNECTION_REQUEST(REQUEST_ID)
- **Triggers**: `CM_CONNECTION_REQ_DOCUMENT_DEL` (after delete), `CM_CONNECTION_REQ_DOCUMENT_INS` (before insert), `CM_CONNECTION_REQ_DOCUMENT_UPD` (before update)

## PAYROLL.CM_CONNECTION_TRANSACTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANS_ID | VARCHAR2(8) | N |  |
| TRANS_DATE | DATE | Y |  |
| REQUEST_ID | VARCHAR2(10) | Y |  |
| CONNECTION_ID | VARCHAR2(8) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

- **PK** `PK_CONNECTION_TRANSACTIONS`: TRANS_ID
- **FK** `FK_CONNECTION_TRANSACTIONS`: (CONNECTION_ID) -> PAYROLL.CM_DEF_CONNECTION(CONNECTION_ID)
- **FK** `FK_CONNECTION_TRANSACTIONS_REQUEST`: (REQUEST_ID) -> PAYROLL.CM_CONNECTION_REQUEST(REQUEST_ID)
- **Triggers**: `CM_CONNECTION_TRANSACTIONS_DEL` (after delete), `CM_CONNECTION_TRANSACTIONS_INS` (before insert), `CM_CONNECTION_TRANSACTIONS_UPD` (before update)

## PAYROLL.CM_DEF_ADMIN_GROUP_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N |  |
| ADMIN_MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_ADMIN_GROUP_DTL`: ADMIN_GROUP_ID, ADMIN_MRNO
- **Triggers**: `CM_DEF_ADMIN_GROUP_DTL_DEL` (after delete), `CM_DEF_ADMIN_GROUP_DTL_INS` (before insert), `CM_DEF_ADMIN_GROUP_DTL_UPD` (before update)

## PAYROLL.CM_INVOICES

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_ID | VARCHAR2(12) | N |  |
| CONTACT_NUMBER | VARCHAR2(40) | N |  |
| BILL_AMOUNT | NUMBER(10,2) | Y |  |
| BILL_MONTH_ID | VARCHAR2(12) | Y |  |
| BILL_REQUEST_ID | VARCHAR2(10) | Y |  |

- **PK** `PK_CM_INVOICES`: MONTH_ID, CONTACT_NUMBER
- **Triggers**: `CM_INVOICES_DEL` (after delete), `CM_INVOICES_INS` (before insert), `CM_INVOICES_UPD` (before update)

## PAYROLL.DEF_AD_CHART

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | VARCHAR2(3) | N |  |
| SRNO | NUMBER(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_AD_CODE`: AD_CODE, SRNO
- **Triggers**: `DEF_AD_CHART_CEA` (before insert or update or delete), `DEF_AD_CHART_DEL` (after delete), `DEF_AD_CHART_INS` (before insert), `DEF_AD_CHART_PK` (before insert), `DEF_AD_CHART_UPD` (before update), `TRG_WS_DKJ_UV_FC_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_CHART_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | VARCHAR2(3) | N |  |
| SRNO | NUMBER(3) | N |  |
| PATIENT_TYPE_GROUP_ID | VARCHAR2(3) | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_DEF_AD_CHART_DETAIL`: AD_CODE, SRNO, PATIENT_TYPE_GROUP_ID, DESIGNATION_CATEGORY_ID, GRADE_ID
- **FK** `FK_DEF_AD_CHART_DETAIL1`: (PATIENT_TYPE_GROUP_ID) -> DEFINITIONS.PATIENT_TYPE_GROUPS(GROUP_ID) [disabled]
- **FK** `FK_DEF_AD_CHART_DETAIL2`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID) [disabled]
- **Triggers**: `DEF_AD_CHART_DETAIL_CEA` (before insert or update or delete), `DEF_AD_CHART_DETAIL_DEL` (after delete), `DEF_AD_CHART_DETAIL_INS` (before insert), `DEF_AD_CHART_DETAIL_UPD` (before update), `TRG_WS_TKR_PZ_OS_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| AD_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PUBLIC_COA_CODE | VARCHAR2(16) | Y | This field stores the COA code from Public secter COA |
| SORTING_NO | NUMBER(3) | Y |  |

- **PK** `PK_DEF_AD_CONSTANT`: AD_CODE
- **Triggers**: `DEF_AD_CONSTANT_CEA` (before insert or update or delete), `DEF_AD_CONSTANT_DEL` (after delete), `DEF_AD_CONSTANT_INS` (before insert), `DEF_AD_CONSTANT_UPD` (before update), `TRG_WS_NXW_PQ_TN_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_NATURE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_NATURE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| DED_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DEF_AD_NATURE_TYPE`: AD_NATURE_TYPE_ID
- **Triggers**: `DEF_AD_NATURE_TYPE_CEA` (before insert or update or delete), `DEF_AD_NATURE_TYPE_DEL` (after delete), `DEF_AD_NATURE_TYPE_INS` (before insert), `DEF_AD_NATURE_TYPE_UPD` (before update), `TRG_WS_FHI_YZ_ST_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_SETUP
This table is used to location wise define def_allowances_deduction.

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| AD_CODE | CHAR(3) | N | Auto-generated Allowance / Deduction Code (PK) |
| DESCRIPTION | VARCHAR2(255) | N | Name of Allowance or deduction |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short Name of Allowance or deduction, to be used in some reports |
| AD_GROUP_CODE | CHAR(3) | Y |  |
| ATTENDANCE_BASED | CHAR(1) default 'A' | Y | Either calculation is dependant on attendance or not |
| AD_NATURE_TYPE_ID | VARCHAR2(3) default '000' | Y | Refers to def_ad_nature_type |
| ENTRY_TYPE | CHAR(1) default 'S' | Y |  |
| CALCULATION_TYPE | VARCHAR2(2) default 'OT' | Y | PS Payscale, PB Basic(%), PG Gross(%), CH AD Chart, FZ Freeze, FX Fix, OB Obsleted, OT Other |
| CALC_PERCENTAGE | NUMBER(5,2) | Y | Value of Percentage if calculation_type is PG or PB |
| TAXABLE | CHAR(1) default 'N' | Y |  |
| TAXABLE_ANNUALLY | CHAR(1) default 'N' | Y | This column is effecitve for entry type as Transaction only |
| INCLUDE_IN_GROSS | CHAR(1) default 'Y' | Y | Either allowance / deduction is included into Gross salary or not |
| EXCLUDE_FROM_GROSS_PAY | CHAR(1) default 'N' | Y | This column add for LFA salary with payment |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | Y |  |
| SLAB_ID | VARCHAR2(12) | Y |  |
| DISTRIBUTE_TAX | CHAR(1) default 'Y' | N | Either deduct the whole tax in one salary or devide on remaining months |

- **PK** `PK_DEF_AD_SETUP`: ORGANIZATION_ID, LOCATION_ID, AD_CODE
- **FK** `FK_DEF_AD_SETUP_1`: (AD_GROUP_CODE) -> PAYROLL.DEF_AD_GROUP(AD_GROUP_CODE) [disabled]
- **FK** `FK_DEF_AD_SETUP_2`: (AD_NATURE_TYPE_ID) -> PAYROLL.DEF_AD_NATURE_TYPE(AD_NATURE_TYPE_ID) [disabled]
- **FK** `FK_DEF_AD_SETUP_3`: (SLAB_ID) -> BILLING.DEF_SLAB(SLAB_ID) [disabled]
- **CHECK** `CK_DEF_AD_SETUP_1`: TAXABLE_ANNUALLY IN ('Y', 'N'
- **CHECK** `CK_DEF_AD_SETUP_2`: ATTENDANCE_BASED IN ('A', 'O'
- **CHECK** `CK_DEF_AD_SETUP_4`: INCLUDE_IN_GROSS IN ('Y', 'N'
- **CHECK** `CK_DEF_AD_SETUP_5`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DEF_AD_SETUP_6`: ENTRY_TYPE IN ('S','T'
- **CHECK** `CK_DEF_AD_SETUP_NN`: AD_GROUP_CODE IS NOT NULL
- **Triggers**: `DEF_AD_SETUP_CEA` (before insert or update or delete), `DEF_AD_SETUP_DEL` (after delete), `DEF_AD_SETUP_INS` (before insert), `DEF_AD_SETUP_UPD` (before update), `TRG_WS_WKA_UZ_BE_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_SETUP_DC
This table is used to define designation category wise ad setup.

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| AD_CODE | CHAR(3) | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| CALCULATION_TYPE | VARCHAR2(2) default 'OT' | Y |  |
| CALC_PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | Y |  |
| SLAB_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_DEF_AD_SETUP_DC`: ORGANIZATION_ID, LOCATION_ID, AD_CODE, DESIGNATION_CATEGORY_ID
- **Triggers**: `DEF_AD_SETUP_DC_CEA` (before insert or update or delete), `DEF_AD_SETUP_DC_DEL` (after delete), `DEF_AD_SETUP_DC_INS` (before insert), `DEF_AD_SETUP_DC_UPD` (before update), `TRG_WS_BUF_UB_DI_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_SETUP_PT
This table is used to define patient type group wise ad setup.

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| AD_CODE | CHAR(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| CALCULATION_TYPE | VARCHAR2(2) default 'OT' | Y |  |
| CALC_PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | Y |  |
| SLAB_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_DEF_AD_SETUP_PT`: ORGANIZATION_ID, LOCATION_ID, AD_CODE, PATIENT_TYPE_ID
- **Triggers**: `DEF_AD_SETUP_PT_CEA` (before insert or update or delete), `DEF_AD_SETUP_PT_DEL` (after delete), `DEF_AD_SETUP_PT_INS` (before insert), `DEF_AD_SETUP_PT_UPD` (before update), `TRG_WS_MMZ_TB_FP_Q` (after insert or update or delete)

## PAYROLL.DEF_AD_SETUP_UNPAID_LT

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| AD_CODE | VARCHAR2(3) | N |  |
| PAYMENT_PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_AD_SETUP_UNPAID_LT`: ORGANIZATION_ID, LOCATION_ID, LEAVE_TYPE_ID, AD_CODE
- **Triggers**: `DEF_AD_SETUP_UNPAID_LT_CEA` (before insert or update or delete), `DEF_AD_SETUP_UNPAID_LT_DEL` (after delete), `DEF_AD_SETUP_UNPAID_LT_INS` (before insert), `DEF_AD_SETUP_UNPAID_LT_UPD` (before update), `TRG_WS_TWV_IJ_IA_Q` (after insert or update or delete)

## PAYROLL.DEF_EMP_JOB
This table is used to define organizational hierarchy of employees

| Column | Type | Null | Comment |
|---|---|---|---|
| JOB_CODE | VARCHAR2(18) | N | PK - Auto generated field |
| DESCRIPTION | VARCHAR2(255) | N | Name of Job |

- **PK** `PK_DEF_EMP_JOB`: JOB_CODE
- **Triggers**: `DEF_EMP_JOB_DEL` (after delete), `DEF_EMP_JOB_INS` (before insert), `DEF_EMP_JOB_UPD` (before update)

## PAYROLL.DEF_GL_SETUP_MASTER
This table is used to define different setups for payroll jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |
| ACTIVE | CHAR(1) default 'Y' | Y | Either row is currenctly availabe for transactions or not |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_S_GL_SETUP_MASTER`: GL_SETUP_CODE
- **CHECK** `CK_S_GL_SETUP_MASTER_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `DEF_GL_SETUP_MASTER_CEA` (before insert or update or delete), `DEF_GL_SETUP_MASTER_DEL` (after delete), `DEF_GL_SETUP_MASTER_INS` (before insert), `DEF_GL_SETUP_MASTER_UPD` (before update), `TRG_WS_TTB_AI_IF_Q` (after insert or update or delete)

## PAYROLL.DEF_INCOME_TAX
This table is used to define different setups for income tax calculation according to govt. policy

| Column | Type | Null | Comment |
|---|---|---|---|
| S_ITAX_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Name of  income tax setup |

- **PK** `PK_DEF_INCOME_TAX`: S_ITAX_CODE
- **Triggers**: `DEF_INCOME_TAX_DEL` (after delete), `DEF_INCOME_TAX_INS` (before insert), `DEF_INCOME_TAX_UPD` (before update)

## PAYROLL.DEF_EMP_FINANCIAL
This table is used to define financial parameters of empoyee which are used to entertain different financial activities

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | PK-Self explainatory |
| COST_CENTRE_ID | CHAR(10) | Y | FK-Self explainatory |
| BRANCH_ID | VARCHAR2(3) | Y | FK-Self explainatory |
| BANK_ID | VARCHAR2(6) | Y | FK-Self explainatory |
| S_ITAX_CODE | CHAR(3) | Y | Used to calculated income tax |
| CURRENCY_ID | VARCHAR2(3) | N | Currency of salary payment |
| JOB_CODE | VARCHAR2(18) | Y | Manpower structure Id, i.e. according to organizational structure employee comes under which hierarchy |
| PAYMENT_MODE | CHAR(1) default 'C' | Y | Salry payment through Cash, Chequeor Bank Transfer |
| BANK_ACCOUNT_NO | VARCHAR2(50) | Y | Employees Bank accounts no where salary is transferred |
| INCLUDE_IN_EOBI | CHAR(1) default 'Y' | Y | Either this employee is included into calculation of EOBI or not |
| INCLUDE_IN_ESSI | CHAR(1) default 'Y' | Y | Either this employee is included into calculation of ESSI or not |
| INCLUDE_IN_ED_CESS | CHAR(1) default 'Y' | Y | Either this employee is included into calculation of Education Cess or not |
| INITIAL_GROSS | NUMBER(20,2) | Y | Gross salary of employee when he/she was hired |
| INITIAL_BASIC | NUMBER(20,2) | Y | Basic salary of employee when he/she was hired |
| CURRENT_GROSS | NUMBER(20,2) | Y | Current gross salary of employee |
| CURRENT_BASIC | NUMBER(20,2) | Y | Current basic salary of employee |
| GL_SETUP_CODE | CHAR(3) | Y | It is used to generate the Payroll Journel Voucher |
| SALARY_ON_CARD_SWIPE | CHAR(1) | Y |  |
| EOBI_NO | VARCHAR2(18) | Y |  |
| FBS_DEPT_CODE | VARCHAR2(3) | Y |  |
| EMP_TYPE | CHAR(1) default 'O' | Y |  |
| PASSPORT_NO | VARCHAR2(15) | Y |  |
| EOBI_JOINING_DATE | DATE | Y |  |
| NTN_NO | VARCHAR2(13) | Y |  |
| DAILY_WAGER | CHAR(1) | Y |  |
| DAILY_RATE | NUMBER(4) | Y |  |
| EXCL_LFA_INTAX | CHAR(1) default 'N' | Y |  |
| PF_JOINING_DATE | DATE | Y |  |
| ONLINE_ACCOUNT | CHAR(1) default 'N' | Y |  |
| ADD_CPI_PAYROLL | CHAR(1) default 'N' | Y | Values of this column must be Y or N, Y means if CPI is calculated then on posting Add CPI into payroll.allowance_deduction_detail against AD CODE 049, N means don't add CPI into payroll |
| PRINT_PAYSLIP | CHAR(1) default 'N' | Y |  |
| GP_FUND_NO | VARCHAR2(30) | Y |  |
| IBAN | VARCHAR2(68) | Y |  |
| BANK_AC_TITLE | VARCHAR2(256) | Y |  |
| MANUAL_TAX | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEF_EMP_FINANCIAL`: MRNO
- **FK** `FK_DEF_EMP_FINANCIAL_1`: (COST_CENTRE_ID) -> DEFINITIONS.GL_DIV_DEPT_CC(COST_CENTRE_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_2`: (BRANCH_ID, BANK_ID) -> DEFINITIONS.BANK_BRANCH(BRANCH_ID, BANK_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_3`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_DEF_EMP_FINANCIAL_4`: (S_ITAX_CODE) -> PAYROLL.DEF_INCOME_TAX(S_ITAX_CODE)
- **FK** `FK_DEF_EMP_FINANCIAL_5`: (CURRENCY_ID) -> DEFINITIONS.CURRENCY(CURRENCY_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_6`: (JOB_CODE) -> PAYROLL.DEF_EMP_JOB(JOB_CODE)
- **FK** `FK_DEF_EMP_FINANCIAL_7`: (GL_SETUP_CODE) -> PAYROLL.DEF_GL_SETUP_MASTER(GL_SETUP_CODE)
- **CHECK** `CK_DEF_EMP_FINANCIAL_1`: PAYMENT_MODE IN ('C', 'B', 'Q'
- **CHECK** `CK_DEF_EMP_FINANCIAL_2`: INCLUDE_IN_EOBI IN ('Y', 'N'
- **CHECK** `CK_DEF_EMP_FINANCIAL_3`: INCLUDE_IN_ESSI IN ('Y', 'N'
- **CHECK** `CK_DEF_EMP_FINANCIAL_4`: INCLUDE_IN_ED_CESS IN ('Y', 'N'
- **CHECK** `CK_DEF_EMP_FINANCIAL_5`: EMP_TYPE IN ('D','C','O'
- **Triggers**: `DEF_EMP_FINANCIAL_COST_CENTER_NULL` (before update), `DEF_EMP_FINANCIAL_DEL` (after delete), `DEF_EMP_FINANCIAL_INS` (before insert), `DEF_EMP_FINANCIAL_UPD` (before update)

## PAYROLL.DEF_EXPENSE

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| TYPE | CHAR(1) default 'N' | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| SERVICE_YEARS | NUMBER(2) | Y |  |
| BONUS_PERCENT | NUMBER(5,2) | Y |  |
| GROSS_BASIC | CHAR(1) | Y |  |
| FROM_JDATE | DATE | Y |  |
| TO_JDATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| FIXED_AMOUNT | NUMBER(12) | Y |  |
| CLAIMABLE | CHAR(1) default 'N' | Y |  |
| AD_CODE | CHAR(3) | Y |  |
| HOD_APPROVAL_REQ | CHAR(1) default 'N' | Y |  |
| PAYMENT_METHOD | CHAR(1) default 'A' | N | A: All, S: Salary, M: Manual |
| AUTO_ADJ_PAYMENT | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEF_EXPENSE`: EXPENSE_CODE, LOCATION_ID
- **FK** `FK_DEF_EXPENSE_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_DEF_EXPENSE_2`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **CHECK** `CK_DEF_EXPENSE_1`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DEF_EXPENSE_2`: TYPE IN ('M','L','O','B','S'
- **CHECK** `CK_DEF_EXPENSE_3`: GROSS_BASIC IN ('G','B', 'F'
- **Triggers**: `DEF_EXPENSE_CEA` (before insert or update or delete), `DEF_EXPENSE_DEL` (after delete), `DEF_EXPENSE_INS` (before insert), `DEF_EXPENSE_UPD` (before update), `TRG_WS_BAN_JP_PG_Q` (after insert or update or delete)

## PAYROLL.DEF_EXPENSE_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PAY_THROUGH_SALARY | CHAR(1) default 'N' | Y | Column add for LFA payment with salary |
| TAXABLE | CHAR(1) default 'N' | N | Y: Whole Expense, A: Accounts, N: None |

- **PK** `PK_DEF_EXP_CONSTANT`: EXPENSE_CODE
- **Triggers**: `DEF_EXPENSE_CONSTANT_CEA` (before insert or update or delete), `DEF_EXPENSE_CONSTANT_DEL` (after delete), `DEF_EXPENSE_CONSTANT_INS` (before insert), `DEF_EXPENSE_CONSTANT_UPD` (before update), `TRG_WS_YJR_OY_UQ_Q` (after insert or update or delete)

## PAYROLL.DEF_EXPENSE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_TYPE_ID | VARCHAR2(3) | N |  |
| EXPENSE_CODE | CHAR(3) | Y |  |
| DESCRIPTION | VARCHAR2(64) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DAYS_REQUIRED | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEF_EXPENSE_DETAIL`: EXPENSE_TYPE_ID
- **Triggers**: `DEF_EXPENSE_DETAIL_CEA` (before insert or update or delete), `DEF_EXPENSE_DETAIL_DEL` (after delete), `DEF_EXPENSE_DETAIL_INS` (before insert), `DEF_EXPENSE_DETAIL_UPD` (before update), `TRG_WS_WFR_HS_SR_Q` (after insert or update or delete)

## PAYROLL.DEF_EXPENSE_DETAIL_SLAB

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_TYPE_ID | VARCHAR2(3) | N |  |
| SLAB_ID | VARCHAR2(12) | N |  |
| IS_DEFAULT | CHAR(1) default 'N' | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEF_EXPENSE_DETAIL_SLAB`: EXPENSE_TYPE_ID, SLAB_ID
- **FK** `FK_DEF_EXPENSE_DETAIL_SLAB1`: (EXPENSE_TYPE_ID) -> PAYROLL.DEF_EXPENSE_DETAIL(EXPENSE_TYPE_ID)
- **Triggers**: `DEF_EXPENSE_DETAIL_SLAB_CEA` (before insert or update or delete), `DEF_EXPENSE_DETAIL_SLAB_DEL` (after delete), `DEF_EXPENSE_DETAIL_SLAB_INS` (before insert), `DEF_EXPENSE_DETAIL_SLAB_UPD` (before update), `TRG_WS_PHJ_BK_HS_Q` (after insert or update or delete)

## PAYROLL.DEF_EXPENSE_TAXABLE_ACC

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_CODE | CHAR(3) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| VALUE_TYPE | VARCHAR2(4) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_EXPENSE_TAXABLE_ACC`: EXPENSE_CODE, OBJECT_CODE, VALUE_TYPE
- **FK** `FK_DEF_EXPENSE_TAXABLE_AC1`: (EXPENSE_CODE) -> PAYROLL.DEF_EXPENSE_CONSTANT(EXPENSE_CODE)
- **FK** `FK_DEF_EXPENSE_TAXABLE_AC2`: (OBJECT_CODE, VALUE_TYPE) -> FINANCE.VALUE_SETS(OBJECT_CODE, VALUE_TYPE) [disabled]
- **Triggers**: `DEF_EXPENSE_TAXABLE_ACC_CEA` (before insert or update or delete), `TRG_WS_BIZ_EJ_FS_Q` (after insert or update or delete)

## PAYROLL.DEF_EXPENSE_WORKFLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_CODE | VARCHAR2(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| EXPENSE_TYPE_ID | CHAR(1) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_EXPENSE_WORKFLOW`: EXPENSE_CODE
- **Triggers**: `DEF_EXPENSE_WORKFLOW_CEA` (before insert or update or delete), `TRG_WS_DYO_YQ_OR_Q` (after insert or update or delete)

## PAYROLL.DEF_FINANCIAL_SETUP
This table is used to define different formulas and rules applied to Govt. and corporate. It contains only one record.

| Column | Type | Null | Comment |
|---|---|---|---|
| OT_CALC_BASE | CHAR(1) default 'G' | Y | Either overtime is paid on gross salary or on basic salary |
| OT_PERCENTAGE | NUMBER(5,2) | Y | What %age of salary is paid as overtime |
| NIGHT_CALC_BASE | CHAR(1) default 'G' | Y | Either night shift allowance is paid on gross salary or on basic salary |
| NIGHT_PERCENTAGE | NUMBER(5,2) | Y | What %age of salary is paid as night allowance |
| GRP_INS_CALC_BASE | CHAR(1) default 'G' | Y | Either group insurance is paid on gross salary or on basic salary |
| GRP_INS_PERCENTAGE | NUMBER(5,2) | Y | What %age of salary is paid as group insurance |
| PF_CALC_BASE | CHAR(1) default 'G' | Y | Either provident Fund is paid on gross salary or on basic salary |
| PF_PERCENTAGE | NUMBER(5,2) | Y | What %age of salary is paid as provident fund |
| LFA_CALC_BASE | CHAR(1) default 'G' | Y | Either Leave Fare Assistance is paid on gross salary or on basic salary |
| LFA_PERCENTAGE | NUMBER(5,2) | Y | What %age of salary is paid as LFA |
| EOBI_BASE_SALARY | NUMBER(20,2) | Y | What is the base salary for EOBI calculation |
| EOBI_PERCENTAGE | NUMBER(5,2) | Y | What %age of base salary is paid as EOBI |
| EOBI_EMPLOYER_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employer in payment of EOBI |
| EOBI_EMPLOYEE_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employee in payment of EOBI |
| EOBI_MALE_EXCLUSION_AGE | NUMBER(3) | Y | How old men ale excluded in payment of EOBI |
| EOBI_FEMALE_EXCLUSION_AGE | NUMBER(3) | Y | How old women ale excluded in payment of EOBI |
| EC_BASE_SALARY | NUMBER(20,2) | Y | What is the base salary for Education Cess calculation |
| EC_PERCENTAGE | NUMBER(5,2) | Y | What %age of base salary is paid as Education Cess |
| EC_EMPLOYER_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employer in payment of Education Cess |
| EC_EMPLOYEE_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employee in payment of Education Cess |
| ESSI_BASE_SALARY | NUMBER(20,2) | Y | What is the contribution of employer in payment of ESSI |
| ESSI_PERCENTAGE | NUMBER(5,2) | Y | What %age of base salary is paid as EOBI |
| ESSI_EMPLOYER_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employer in payment of ESSI |
| ESSI_EMPLOYEE_CONTRIBUTION | NUMBER(20,2) | Y | What is the contribution of employee in payment of ESSI |
| ESSI_MALE_EXCLUSION_AGE | NUMBER(3) | Y | How old men ale excluded in payment of ESSI |
| ESSI_FEMALE_EXCLUSION_AGE | NUMBER(3) | Y | How old women ale excluded in payment of ESSI |
| BASIC_PER_GROSS | NUMBER(5,2) | Y |  |
| SALARY_ON_CARD_SWIPE | CHAR(1) | Y |  |
| ADV_EXP_CONVERSION_DAYS | NUMBER(3) | Y |  |
| NURSE_TPT_ALLOWANCE | NUMBER(5) | Y |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| LONG_SERVICE_DATE | DATE | Y |  |
| PI_TAX_PERCENTAGE | NUMBER(5,2) | Y |  |
| BACKDATE_REFUND_ALLOW | CHAR(1) default 'N' | Y |  |
| LFA_PMT_ALLOW | NUMBER(2) | Y | Number of months for LFA payment before LFA Due Date |
| COLLEGIALITY_FUND_AMOUNT | NUMBER(10,2) | Y |  |
| OLD_LFA_START | CHAR(6) | Y | For old LFA salary for joiners between 23rd Dec to 31st Dec |
| OLD_LFA_END | CHAR(6) | Y | For old LFA salary for joiners between 23rd Dec to 31st Dec |
| LFA_PAYMENT_DAYS | NUMBER(3) | Y | Number of days for LFA payment before LFA scheduled leave |

- **PK** `PK_DEF_FINANCIAL_SETUP`: FROM_DATE
- **CHECK** `CK_DEF_FINANCIAL_SETUP_1`: OT_CALC_BASE IN ('G', 'B'
- **CHECK** `CK_DEF_FINANCIAL_SETUP_2`: NIGHT_CALC_BASE IN ('G', 'B'
- **CHECK** `CK_DEF_FINANCIAL_SETUP_3`: GRP_INS_CALC_BASE IN ('G', 'B'
- **CHECK** `CK_DEF_FINANCIAL_SETUP_4`: PF_CALC_BASE IN ('G', 'B'
- **CHECK** `CK_DEF_FINANCIAL_SETUP_5`: LFA_CALC_BASE IN ('G', 'B'
- **Triggers**: `DEF_FINANCIAL_SETUP_DEL` (after delete), `DEF_FINANCIAL_SETUP_INS` (before insert), `DEF_FINANCIAL_SETUP_UPD` (before update)

## PAYROLL.DEF_FS_ELEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| ELEMENT_CODE | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(100) | N |  |
| LONG_DESCRIPTION | VARCHAR2(500) | Y |  |
| TYPE | VARCHAR2(1) | Y |  |
| TAXABLE_ELEMENT | VARCHAR2(1) default 'Y' | Y |  |
| ELEMENT_UNIT | VARCHAR2(20) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_DEF_FS_ELEMENTS`: ELEMENT_CODE
- **Triggers**: `DEF_FS_ELEMENT_DEL` (after delete), `DEF_FS_ELEMENT_INS` (before insert), `DEF_FS_ELEMENT_UPD` (before update)

## PAYROLL.DEF_FS_ELEMENT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| EVENT_DETIAL_DESC | VARCHAR2(2000) | Y |  |
| TABLE_SOURCE | VARCHAR2(1000) | Y |  |
| COLUMN_IDENTIFIER_1 | VARCHAR2(500) | Y |  |
| COLUMN_IDENTIFIER_2 | VARCHAR2(500) | Y |  |
| COLUMN_IDENTIFIER_3 | VARCHAR2(500) | Y |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| ELEMENT_CODE | VARCHAR2(8) | N |  |
| IS_FUNCTION | CHAR(1) default 'N' | Y |  |

_No standard audit columns._

- **PK** `DEF_FS_ELEMENT_DETAIL_PK`: ELEMENT_CODE, SR_NO

## PAYROLL.DEF_FS_SALARY_ELEMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ELEMENTS | VARCHAR2(8) | N |  |
| AMOUNT | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_DEF_FS_SALARY_ELEMENTS`: ELEMENTS

## PAYROLL.DEF_FS_WORKFLOW_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

_No standard audit columns._


## PAYROLL.DEF_GL_SETUP_DETAIL
This table is used to define different setups for automatic payroll jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| SERIAL_NO | NUMBER(3) | N | Part of PK |
| STATIC_DESCRIPTION | VARCHAR2(20) | Y | To defince static fields of setup |
| AD_CODE | CHAR(3) | Y | Allowance or deduction code |
| LOAN_CODE | CHAR(3) | Y | Loan type |
| COA_CODE_DR | VARCHAR2(100) | Y | PK-self explainatory (To entertain Dr entries) |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y | PK-self explainatory (To entertain Dr entries) |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y | PK-self explainatory (To entertain Dr entries) |
| COA_CODE_CR | VARCHAR2(100) | Y | PK-self explainatory (To entertain Cr entries) |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y | PK-self explainatory (To entertain Cr entries) |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y | PK-self explainatory (To entertain Cr entries) |
| TRANSACTION_TYPE | CHAR(1) default 'O' | Y | Either "S" for Static or "L" for Loan or "A" for Allowances or "D" for Deductions or "O" for Others |
| STATIC_TYPE | CHAR(1) | Y | Either "G" for Gross Salary or "O" for Overtime or "N" for Night Allowance or "P" for PF-Employer |
| ARREAR_CODE | CHAR(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |
| EXPENSE_CODE | VARCHAR2(3) | Y |  |

- **PK** `PK_S_GL_SETUP_DETAIL`: GL_SETUP_CODE, SERIAL_NO
- **FK** `FK_DEF_GL_SETUP_DETAIL`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **FK** `FK_DEF_GL_SETUP_DETAIL_1`: (ARREAR_CODE) -> PAYROLL.DEF_ARREAR(ARREAR_CODE) [disabled]
- **FK** `FK_S_GL_SETUP_DETAIL_3`: (LEDGER_TYPE_CODE_DR, SUB_LDGR_ITEM_CODE_DR) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) [disabled]
- **FK** `FK_S_GL_SETUP_DETAIL_4`: (COA_CODE_DR) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **FK** `FK_S_GL_SETUP_DETAIL_5`: (GL_SETUP_CODE) -> PAYROLL.DEF_GL_SETUP_MASTER(GL_SETUP_CODE)
- **CHECK** `CK_S_GL_SETUP_DETAIL_3`: TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O', 'R', 'E'
- **Triggers**: `DEF_GL_SETUP_DETAIL_DEL` (after delete), `DEF_GL_SETUP_DETAIL_INS` (before insert), `DEF_GL_SETUP_DETAIL_UPD` (before update)

## PAYROLL.DEF_GL_SETUP_DETAIL_FS
This table is used to define different setups for automatic payroll final settlement jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| SERIAL_NO | NUMBER(3) | N | Part of PK |
| ELEMENT_CODE | VARCHAR2(8) | N | Final settlement Elements code |
| COA_CODE_DR | VARCHAR2(100) | Y | PK-self explainatory (To entertain Dr entries) |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y | PK-self explainatory (To entertain Dr entries) |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y | PK-self explainatory (To entertain Dr entries) |
| COA_CODE_CR | VARCHAR2(100) | Y | PK-self explainatory (To entertain Cr entries) |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y | PK-self explainatory (To entertain Cr entries) |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y | PK-self explainatory (To entertain Cr entries) |

- **PK** `PK_DEF_GL_SETUP_DETAIL_FS`: GL_SETUP_CODE, ELEMENT_CODE
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS`: (ELEMENT_CODE) -> PAYROLL.DEF_FS_ELEMENT(ELEMENT_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_1`: (LEDGER_TYPE_CODE_DR, SUB_LDGR_ITEM_CODE_DR) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_2`: (COA_CODE_DR) -> FINANCE.GL_COA(COA_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_3`: (GL_SETUP_CODE) -> PAYROLL.DEF_GL_SETUP_MASTER(GL_SETUP_CODE)
- **Triggers**: `DEF_GL_SETUP_DETAIL_FS_DEL` (after delete), `DEF_GL_SETUP_DETAIL_FS_INS` (before insert), `DEF_GL_SETUP_DETAIL_FS_UPD` (before update)

## PAYROLL.DEF_GL_VOUCHER
This table is used to define different setups for payroll jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |

- **PK** `PK_DEF_GL_VOUCHER_01`: GL_SETUP_CODE
- **Triggers**: `DEF_GL_VOUCHER_DEL` (after delete), `DEF_GL_VOUCHER_INS` (before insert), `DEF_GL_VOUCHER_UPD` (before update)

## PAYROLL.DEF_PERCENTAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| MINIMUM_VALUE | NUMBER(20,2) | Y |  |
| MAX_VALUE | NUMBER(20,2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_PERCENTAGE_SETUP`: PERCENTAGE_SETUP_ID
- **Triggers**: `DEF_PERCENTAGE_SETUP_CEA` (before insert or update or delete), `DEF_PERCENTAGE_SETUP_DEL` (after delete), `DEF_PERCENTAGE_SETUP_INS` (before insert), `DEF_PERCENTAGE_SETUP_UPD` (before update), `TRG_WS_FJA_HA_AY_Q` (after insert or update or delete)

## PAYROLL.DEF_GRADE_WISE_PERCENTAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_DEF_GRADE_WISE_PERCENTAGE`: PERCENTAGE_SETUP_ID, GRADE_ID
- **FK** `FK_DEF_GRADE_PERCENT_01`: (PERCENTAGE_SETUP_ID) -> PAYROLL.DEF_PERCENTAGE_SETUP(PERCENTAGE_SETUP_ID)
- **Triggers**: `DEF_GRADE_WISE_PERCENTAGE_CEA` (before insert or update or delete), `DEF_GRADE_WISE_PERCENTAGE_DEL` (after delete), `DEF_GRADE_WISE_PERCENTAGE_INS` (before insert), `DEF_GRADE_WISE_PERCENTAGE_UPD` (before update), `TRG_WS_FLB_GV_CW_Q` (after insert or update or delete)

## PAYROLL.DEF_INCREMENT_TYPE
This table is used to define different types of increments such as Annual, promotional etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| INCREMENT_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Name of increment |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short Name of increment |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |
| INCREASE_STAGE | CHAR(1) default 'N' | Y |  |
| NO_OF_JOB_MONTH | NUMBER(2) | Y | Number of months that must be completed to be part of this increment |

- **PK** `PK_DEF_INCREMENT_TYPE`: INCREMENT_CODE
- **CHECK** `CK_DEF_INCREMENT_TYPE_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `DEF_INCREMENT_TYPE_CEA` (before insert or update or delete), `DEF_INCREMENT_TYPE_DEL` (after delete), `DEF_INCREMENT_TYPE_INS` (before insert), `DEF_INCREMENT_TYPE_UPD` (before update), `TRG_WS_LHW_SF_PB_Q` (after insert or update or delete)

## PAYROLL.DEF_ITAX_ADJUSTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| ADJUSTMENT_CODE | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ADJUSTMENT_TYPE | CHAR(1) default 'A' | Y | 'A' FOR ADJUSTMENT, 'C' FOR CREDITS |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CALC_TYPE | CHAR(1) default 'M' | N |  |
| AMOUNT_LIMIT | NUMBER(15) | Y |  |
| PERCENT_LIMIT | NUMBER(5,2) | Y |  |

- **PK** `PK_DEF_ITAX_ADJUSTMENT`: ADJUSTMENT_CODE
- **CHECK** `CK_DEF_ITAX_ADJUSTMENT`: ACTIVE IN ('Y','N'
- **Triggers**: `DEF_ITAX_ADJUSTMENT_CEA` (before insert or update or delete), `TRG_WS_NEL_OY_ZL_Q` (after insert or update or delete)

## PAYROLL.PAY_FINANCIAL_YEAR

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| FROM_DATE | DATE | N |  |
| YEAR_DESCRIPTION | VARCHAR2(25) | N |  |
| TO_DATE | DATE | N |  |
| YEAR_STATUS | CHAR(1) | Y |  |
| CURRENT_YEAR | CHAR(1) default 'N' | Y |  |
| EXEMPT_AGE_MALE | NUMBER(3) default 60 | N |  |
| EXEMPT_AGE_FEMALE | NUMBER(3) default 55 | N |  |
| EXEMPT_TAX_PERCENTAGE_MALE | NUMBER(5,2) default 50 | N |  |
| EXEMPT_TAX_PERCENTAGE_FEMALE | NUMBER(5,2) default 50 | N |  |
| EXEMPT_TAX_AMOUNT_MALE | NUMBER(10) | Y |  |
| EXEMPT_TAX_AMOUNT_FEMALE | NUMBER(10) | Y |  |
| GENERAL_EXEMPTION_AMOUNT | NUMBER(10) default 100000 | N |  |
| CALCULATION_MODE | NUMBER(1) default 2 | N | 1 for Allowance Based Tax System 2 for Gross Based Tax System |
| MIN_TAX_DEDUCTION | NUMBER(10) | Y |  |
| MARGINAL_RELIEF | CHAR(1) default 'N' | Y |  |
| PF_EXEMPT_PCTAGE | NUMBER(5,2) | Y |  |
| PF_TAXABLE_CONTRIBUTION | NUMBER(10) | Y |  |
| PF_EXEMPT_BASE | CHAR(1) default 'G' | Y |  |
| ITAX_SURCHARGE | NUMBER(5,2) default 0 | Y |  |

- **PK** `PK_PAY_FINANCIAL_YEAR`: YEAR_CODE
- **CHECK** `CK_PAY_FINANCIAL_YEAR_1`: YEAR_STATUS IN ('O', 'C', 'S'
- **CHECK** `CK_PAY_FINANCIAL_YEAR_2`: CURRENT_YEAR IN ('Y', 'N'
- **CHECK** `CK_PAY_FINANCIAL_YEAR_3`: FROM_DATE = TRUNC(FROM_DATE
- **CHECK** `CK_PAY_FINANCIAL_YEAR_4`: TO_DATE = TRUNC(TO_DATE
- **CHECK** `CK_PAY_FINANCIAL_YEAR_5`: MARGINAL_RELIEF IN( 'Y','N'
- **CHECK** `CK_PAY_FINANCIAL_YEAR_6`: PF_EXEMPT_BASE IN ('G', 'B'
- **Triggers**: `PAY_FINANCIAL_YEAR_CEA` (before insert or update or delete), `PAY_FINANCIAL_YEAR_DEL` (after delete), `PAY_FINANCIAL_YEAR_INS` (before insert), `PAY_FINANCIAL_YEAR_UPD` (before update), `TRG_WS_WNQ_VQ_RO_Q` (after insert or update or delete)

## PAYROLL.DEF_ITAX_DETAIL_AD

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| AD_CODE | CHAR(3) | N |  |
| TAXABLE | CHAR(1) default 'Y' | N |  |
| GROSS_BASIC_OTHER | CHAR(1) default 'B' | N |  |
| EXEMPT_PERCENT | NUMBER(5,2) | Y |  |
| MAX_EXEMPT_LIMIT | NUMBER(10) default 0 | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DEF_ITAX_DETAIL_AD`: YEAR_CODE, AD_CODE
- **FK** `DEF_ITAX_DETAIL_AD_1`: (YEAR_CODE) -> PAYROLL.PAY_FINANCIAL_YEAR(YEAR_CODE)
- **FK** `FK_DEF_ITAX_DETAIL_AD`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_001`: TAXABLE IN ('Y','N'
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_002`: GROSS_BASIC_OTHER IN ('B','G','O'
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_003`: ACTIVE IN ('Y','N'
- **Triggers**: `DEF_ITAX_DETAIL_AD_CEA` (before insert or update or delete), `TRG_WS_ACE_JF_AP_Q` (after insert or update or delete)

## PAYROLL.DEF_ITAX_MR_SLAB

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| FROM_SALARY_RANGE | NUMBER(10) default 0 | N |  |
| TO_SALARY_RANGE | NUMBER(10) default 9999999999 | N |  |
| TAX_PERCENT | NUMBER(5,2) | N |  |

- **PK** `PK_DEF_ITAX_MR_SLAB`: YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE
- **UK** `UK_DEF_ITAX_MR_SLAB_1`: YEAR_CODE, FROM_SALARY_RANGE
- **FK** `FK_DEF_ITAX_MR_SLAB_1`: (YEAR_CODE) -> PAYROLL.PAY_FINANCIAL_YEAR(YEAR_CODE)
- **Triggers**: `DEF_ITAX_MR_SLAB_CEA` (before insert or update or delete), `TRG_WS_KSE_EA_UF_Q` (after insert or update or delete)

## PAYROLL.DEF_ITAX_SLAB

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| FROM_SALARY_RANGE | NUMBER(10) default 0 | N |  |
| TO_SALARY_RANGE | NUMBER(10) default 9999999999 | N |  |
| BASE_TAX_AMOUNT | NUMBER(10) default 0 | N |  |
| TAX_PERCENT | NUMBER(5,2) | N |  |

- **PK** `PK_DEF_ITAX_SLAB`: YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE
- **UK** `UK_DEF_ITAX_SLAB_1`: YEAR_CODE, FROM_SALARY_RANGE
- **FK** `FK_DEF_ITAX_SLAB_1`: (YEAR_CODE) -> PAYROLL.PAY_FINANCIAL_YEAR(YEAR_CODE)
- **Triggers**: `DEF_ITAX_SLAB_CEA` (before insert or update or delete), `TRG_WS_LIC_JY_WB_Q` (after insert or update or delete)

## PAYROLL.DEF_LETTER_TYPE
This table is used to define different letter types

| Column | Type | Null | Comment |
|---|---|---|---|
| LETTER_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Type of the letter i.e. joining, experience, termination etc. |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short name of the |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |

- **PK** `PK_DEF_LETTER_TYPE`: LETTER_CODE
- **CHECK** `CK_DEF_LETTER_TYPE_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `DEF_LETTER_TYPE_DEL` (after delete), `DEF_LETTER_TYPE_INS` (before insert), `DEF_LETTER_TYPE_UPD` (before update)

## PAYROLL.DEF_LETTER_TEMPLATE
This table is used to define different letter templates to be issued to employees such as joining, experience etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_CODE | CHAR(3) | N | PK-self explainatory |
| LETTER_CODE | CHAR(3) | Y | Letter type |
| DESCRIPTION | VARCHAR2(255) | Y | Template name |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short name for the Template |
| TEMPLATE_HEADER | VARCHAR2(4000) | Y | Header text for template |
| INNER_TEXT | VARCHAR2(4000) | Y | Internal text for template |
| FOOTER | VARCHAR2(4000) | Y | Footer text for template |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |

- **PK** `PK_DEF_LETTER_TEMPLATE`: TEMPLATE_CODE
- **FK** `FK_DEF_LETTER_TEMPLATE_1`: (LETTER_CODE) -> PAYROLL.DEF_LETTER_TYPE(LETTER_CODE)
- **CHECK** `CK_DEF_LETTER_TEMPLATE_1`: ACTIVE IN ('Y', 'N'

## PAYROLL.DEF_LIABILITY

| Column | Type | Null | Comment |
|---|---|---|---|
| LIABILITY_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_LIABILITY`: LIABILITY_CODE
- **Triggers**: `DEF_LIABILITY_DEL` (after delete), `DEF_LIABILITY_INS` (before insert), `DEF_LIABILITY_UPD` (before update)

## PAYROLL.DEF_LOAN_INTEREST_RATE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_CODE | CHAR(3) | N |  |
| YEAR_CODE | NUMBER(4) | N |  |
| INTEREST_RATE | NUMBER(5,2) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DEF_LOAN_INTEREST_RATE`: LOAN_CODE, YEAR_CODE, LOCATION_ID, ORGANIZATION_ID
- **FK** `FK_DEF_LOAN_INTEREST_RATE_1`: (YEAR_CODE) -> FINANCE.PF_FINANCIAL_YEAR(YEAR_CODE) [disabled]
- **Triggers**: `DEF_LOAN_INTEREST_RATE_CEA` (before insert or update or delete), `DEF_LOAN_INTEREST_RATE_DEL` (after delete), `DEF_LOAN_INTEREST_RATE_INS` (before insert), `DEF_LOAN_INTEREST_RATE_UPD` (before update), `TRG_WS_OLB_LH_ZZ_Q` (after insert or update or delete)

## PAYROLL.DEF_LOAN_TYPE
This table is used to define different types of loan such as Advance against salary, Car loan, house loan etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Name of the loan Type |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short name of the loan Type, to be used in salary sheets |
| MEDICAL_OTHER | CHAR(1) default 'O' | Y | Is this medical advance or other |
| INSTALLMENT_ALLOW | CHAR(1) default 'Y' | Y | Installments allowed against this advance or not |
| DEDUCTION_FROM_SALARY | CHAR(1) default 'Y' | Y | Deduction from salary is valid against this record or not |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |
| LEDGER_TYPE_CODE | NUMBER(4) | Y | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| SUB_LDGR_ITEM_CODE | VARCHAR2(18) | Y | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| COA_CODE | VARCHAR2(100) | Y | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| LEDGER_TYPE_CODE_DEBIT | NUMBER(4) | Y | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| SUB_LDGR_ITEM_CODE_DEBIT | VARCHAR2(18) | Y | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| COA_CODE_DEBIT | VARCHAR2(100) | Y | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| REFUND_WITH_PAY_VOUCHER | CHAR(1) | Y |  |
| REFUND_AD_CODE | CHAR(3) | Y |  |
| SALARY_DEDUCTION_TYPE | CHAR(1) default 'D' | N | D Direct, A Arrear, R Deduction |
| INT_LEDGER_TYPE_CODE | NUMBER(4) | Y |  |
| INT_SUB_LDGR_ITEM_CODE | VARCHAR2(18) | Y |  |
| INT_COA_CODE | VARCHAR2(100) | Y |  |
| REFUND_THROUGH_RECEIPT | CHAR(1) default 'N' | Y | This column specify if direct refund is permitted or receipt is required |
| INTEREST | CHAR(1) | Y |  |
| INT_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| GAP_DAYS | NUMBER(3) | Y | No of days gap between the loans of an employee |
| ALLOW_MULTIPLE_LOANS | CHAR(1) default 'Y' | N |  |
| DEFER_INT_VOUCHER | CHAR(1) default on null 'N' | N | If yes then loan markup voucher will not be generated with loan voucher |
| DISP_ON_SALARY_SLIP | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEF_LOAN_TYPE`: LOAN_CODE, ORGANIZATION_ID, LOCATION_ID
- **FK** `FK_DEF_LOAN1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_DEF_LOAN_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_DEF_LOAN_TYPE_1`: (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) [disabled]
- **FK** `FK_DEF_LOAN_TYPE_2`: (COA_CODE) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **CHECK** `CK_DEF_LOAN_TYPE_1`: MEDICAL_OTHER IN ('M', 'O'
- **CHECK** `CK_DEF_LOAN_TYPE_2`: INSTALLMENT_ALLOW IN ('Y', 'N'
- **CHECK** `CK_DEF_LOAN_TYPE_3`: DEDUCTION_FROM_SALARY IN ('Y', 'N'
- **CHECK** `CK_DEF_LOAN_TYPE_4`: ACTIVE IN ('Y', 'N'
- **Triggers**: `DEF_LOAN_TYPE_CEA` (before insert or update or delete), `DEF_LOAN_TYPE_DEL` (after delete), `DEF_LOAN_TYPE_INS` (before insert), `DEF_LOAN_TYPE_UPD` (before update), `TRG_WS_IAP_QA_QL_Q` (after insert or update or delete)

## PAYROLL.DEF_LOAN_TYPE_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| MODULE | VARCHAR2(2) | Y | PF, GL, CP, GP |

- **PK** `PK_DEF_LOAN_CONST`: LOAN_CODE
- **Triggers**: `DEF_LOAN_TYPE_CONSTANT_CEA` (before insert or update or delete), `DEF_LOAN_TYPE_CONSTANT_DEL` (after delete), `DEF_LOAN_TYPE_CONSTANT_INS` (before insert), `DEF_LOAN_TYPE_CONSTANT_UPD` (before update), `TRG_WS_YTS_VH_XA_Q` (after insert or update or delete)

## PAYROLL.DEF_MONTH_CHANGE

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| REPORT_NAME | VARCHAR2(200) | Y |  |
| TABLE_NAME | VARCHAR2(200) | Y |  |
| WHERE_CLAUSE | CLOB | Y |  |
| UPDATE_COLUMN | VARCHAR2(2000) | Y |  |
| ACTIVE_FLAG | CHAR(1) | Y |  |

- **PK** `PK_DEF_MONTH_CHANGE`: ID
- **Triggers**: `DEF_MONTH_CHANGE_DEL` (after delete), `DEF_MONTH_CHANGE_INS` (before insert), `DEF_MONTH_CHANGE_UPD` (before update)

## PAYROLL.DEF_PAYROLL_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | N | The location on which pay process is to be executed |
| EMP_LOCATION_ID | VARCHAR2(3) | N | The locations of employees which are grouped with payroll location |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_PAYROLL_LOCATION`: ORGANIZATION_ID, PAYROLL_LOCATION_ID, EMP_LOCATION_ID
- **UK** `UK_DEF_PAYROLL_LOCATION`: ORGANIZATION_ID, EMP_LOCATION_ID
- **Triggers**: `DEF_PAYROLL_LOCATION_CEA` (before insert or update or delete), `DEF_PAYROLL_LOCATION_DEL` (after delete), `DEF_PAYROLL_LOCATION_INS` (before insert), `DEF_PAYROLL_LOCATION_UPD` (before update), `TRG_WS_VTC_YQ_HK_Q` (after insert or update or delete)

## PAYROLL.DEF_PAYROLL_WORKFLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| TYPE | VARCHAR2(2) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_DEF_PAYROLL_WORKFLOW`: LOCATION_ID, TYPE
- **Triggers**: `DEF_PAYROLL_WORKFLOW_DEL` (after delete), `DEF_PAYROLL_WORKFLOW_INS` (before insert), `DEF_PAYROLL_WORKFLOW_UPD` (before update)

## PAYROLL.DEF_PAYSCALE

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| MIN_AMOUNT | NUMBER(20,2) | Y |  |
| MAX_AMOUNT | NUMBER(20,2) | Y |  |
| INCREMENT_AMOUNT | NUMBER(10,2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MIN_STAGE_NO | NUMBER(2) | Y |  |
| MAX_STAGE_NO | NUMBER(2) | Y |  |

- **PK** `PK_DEF_PAYSCALE`: YEAR_CODE, GRADE_ID
- **Triggers**: `DEF_PAYSCALE_CEA` (before insert or update or delete), `DEF_PAYSCALE_DEL` (after delete), `DEF_PAYSCALE_INS` (before insert), `DEF_PAYSCALE_UPD` (before update), `TRG_WS_MCF_WK_WX_Q` (after insert or update or delete)

## PAYROLL.DEF_PAYSCALE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| STAGE_NO | NUMBER(2) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_DEF_PAYSCALE_DETAIL`: YEAR_CODE, GRADE_ID, STAGE_NO
- **FK** `FK_DEF_PAYSCALE_DETAIL1`: (YEAR_CODE, GRADE_ID) -> PAYROLL.DEF_PAYSCALE(YEAR_CODE, GRADE_ID) [disabled]
- **Triggers**: `DEF_PAYSCALE_DETAIL_CEA` (before insert or update or delete), `DEF_PAYSCALE_DETAIL_DEL` (after delete), `DEF_PAYSCALE_DETAIL_INS` (before insert), `DEF_PAYSCALE_DETAIL_UPD` (before update), `TRG_WS_SAN_MB_CF_Q` (after insert or update or delete)

## PAYROLL.DEF_PAY_VOUCHER_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| EMP_LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_PAY_VOUCHER_LOCATION`: PAY_VOUCHER_TYPE, LOCATION_ID, EMP_LOCATION_ID
- **Triggers**: `DEF_PAY_VOUCHER_LOCATION_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_LOCATION_DEL` (after delete), `DEF_PAY_VOUCHER_LOCATION_INS` (before insert), `DEF_PAY_VOUCHER_LOCATION_UPD` (before update), `TRG_WS_MYU_RJ_JI_Q` (after insert or update or delete)

## PAYROLL.DEF_PAY_VOUCHER_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CATEGORY | VARCHAR2(2) | Y | GL or PF |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEF_PAY_VOUCHER_TYPE`: PAY_VOUCHER_TYPE
- **Triggers**: `DEF_PAY_VOUCHER_TYPE_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_TYPE_DEL` (after delete), `DEF_PAY_VOUCHER_TYPE_INS` (before insert), `DEF_PAY_VOUCHER_TYPE_UPD` (before update), `TRG_WS_GXP_UF_OU_Q` (after insert or update or delete)

## PAYROLL.DEF_PAY_VOUCHER_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_SETUP_ID | VARCHAR2(3) | N |  |
| PAY_VOUCHER_TYPE | VARCHAR2(2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| DEDUCTION_AD_CODE | VARCHAR2(3) | Y |  |
| COA_CODE_DR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |
| MERGE_PROFIT_ON_YEAREND | VARCHAR2(100) | Y |  |
| PRFT_COA_CODE_DR | VARCHAR2(100) | Y |  |
| PRFT_LEDGER_TYPE_CODE_DR | NUMBER(4) | Y |  |
| PRFT_SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |

- **PK** `PK_DEF_PAY_VOUCHER_SETUP`: PAY_VOUCHER_SETUP_ID
- **FK** `FK_DEF_PAY_VOUCHER_SETUP`: (PAY_VOUCHER_TYPE) -> PAYROLL.DEF_PAY_VOUCHER_TYPE(PAY_VOUCHER_TYPE) [disabled]
- **Triggers**: `DEF_PAY_VOUCHER_SETUP_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_SETUP_DEL` (after delete), `DEF_PAY_VOUCHER_SETUP_INS` (before insert), `DEF_PAY_VOUCHER_SETUP_PK` (before insert), `DEF_PAY_VOUCHER_SETUP_UPD` (before update), `TRG_WS_BLA_PZ_PG_Q` (after insert or update or delete)

## PAYROLL.DEF_PAY_VOUCHER_SETUP_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_SETUP_ID | VARCHAR2(3) | N |  |
| SRNO | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| COA_CODE_CR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| PRFT_COA_CODE_CR | VARCHAR2(100) | Y |  |
| PRFT_LEDGER_TYPE_CODE_CR | NUMBER(4) | Y |  |
| PRFT_SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y |  |

- **PK** `PK_DEF_PAY_VOUCHER_SETUP_DTL`: PAY_VOUCHER_SETUP_ID, SRNO
- **FK** `FK_DEF_PAY_VOUCHER_SETUP_DTL1`: (PAY_VOUCHER_SETUP_ID) -> PAYROLL.DEF_PAY_VOUCHER_SETUP(PAY_VOUCHER_SETUP_ID)
- **Triggers**: `DEF_PAY_VOUCHER_SETUP_DTL_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_SETUP_DTL_DEL` (after delete), `DEF_PAY_VOUCHER_SETUP_DTL_INS` (before insert), `DEF_PAY_VOUCHER_SETUP_DTL_UPD` (before update), `TRG_WS_LRB_SM_CW_Q` (after insert or update or delete)

## PAYROLL.DEF_PF_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| COA_CODE_EMPLOYEE_CONT | VARCHAR2(100) | N |  |
| COA_CODE_EMPLOYER_CONT | VARCHAR2(100) | Y |  |
| COA_CODE_SKMT_CONT | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_CONT | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_CONT | VARCHAR2(18) | Y |  |
| COA_CODE_EMPLOYEE_LOAN | VARCHAR2(100) | Y |  |
| COA_CODE_SKMT_LOAN | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_LOAN | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_LOAN | VARCHAR2(18) | Y |  |
| COA_CODE_EMP_PROFIT | VARCHAR2(100) | Y |  |
| COA_CODE_SKMT_PROFIT | VARCHAR2(100) | Y |  |
| COA_CODE_PL | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_PL | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_PL | VARCHAR2(18) | Y |  |

- **PK** `PK_DEF_PF_SETUP`: COA_CODE_EMPLOYEE_CONT
- **FK** `FK_DEF_PF_SETUP_1`: (LEDGER_TYPE_CODE_CONT, SUB_LDGR_ITEM_CODE_CONT) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) [disabled]
- **FK** `FK_DEF_PF_SETUP_2`: (COA_CODE_EMPLOYEE_CONT) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **FK** `FK_DEF_PF_SETUP_3`: (LEDGER_TYPE_CODE_PL, SUB_LDGR_ITEM_CODE_PL) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) [disabled]
- **FK** `FK_DEF_PF_SETUP_4`: (COA_CODE_EMP_PROFIT) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **FK** `FK_DEF_PF_SETUP_5`: (COA_CODE_SKMT_PROFIT) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **FK** `FK_DEF_PF_SETUP_6`: (COA_CODE_PL) -> FINANCE.GL_COA(COA_CODE) [disabled]
- **Triggers**: `DEF_PF_SETUP_DEL` (after delete), `DEF_PF_SETUP_INS` (before insert), `DEF_PF_SETUP_UPD` (before update)

## PAYROLL.DEF_PROJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| PROJECT_ID | VARCHAR2(7) | N |  |
| PROJECT_NAME | VARCHAR2(1000) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| PROJECT_TYPE | VARCHAR2(500) | Y |  |
| CLIENT_ID | VARCHAR2(10) | Y |  |
| CAMPAIGN_ID | VARCHAR2(12) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PROJECT_ID`: PROJECT_ID
- **Triggers**: `DEF_PROJECT_CEA` (before insert or update or delete), `DEF_PROJECT_DEL` (after delete), `DEF_PROJECT_INS` (before insert), `DEF_PROJECT_UPD` (before update), `TRG_WS_XQB_HY_XD_Q` (after insert or update or delete)

## PAYROLL.DEF_SCHEDULE_WORKFLOW_CC

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_CODE | VARCHAR2(3) | N |  |
| TRANS_TYPE | CHAR(1) default 'C' | N |  |
| COST_CENTRE_ID | VARCHAR2(10) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| EXPENSE_TYPE_ID | CHAR(1) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_SCHEDULE_WORKFLOW_CC`: EXPENSE_CODE, TRANS_TYPE, COST_CENTRE_ID

## PAYROLL.DEF_SETUP_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(10) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MENDATORY | CHAR(1) | Y |  |

- **PK** `PK_CONST_ID`: CONSTANT_ID
- **Triggers**: `DEF_SETUP_CONSTANT_CEA` (before insert or update or delete), `DEF_SETUP_CONSTANT_DEL` (after delete), `DEF_SETUP_CONSTANT_INS` (before insert), `DEF_SETUP_CONSTANT_UPD` (before update), `TRG_WS_IKV_BH_WN_Q` (after insert or update or delete)

## PAYROLL.DEF_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| VALUE | VARCHAR2(100) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

- **PK** `PK_CONSTANT`: CONSTANT_ID, LOCATION_ID, ORGANIZATION_ID
- **FK** `FK_CONSTANT1`: (CONSTANT_ID) -> PAYROLL.DEF_SETUP_CONSTANT(CONSTANT_ID)
- **FK** `FK_DEF_SETUP_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_DEF_SETUP_2`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **Triggers**: `DEF_SETUP_CEA` (before insert or update or delete), `DEF_SETUP_DEL` (after delete), `DEF_SETUP_INS` (before insert), `DEF_SETUP_UPD` (before update), `TRG_WS_NML_BL_RN_Q` (after insert or update or delete)

## PAYROLL.DEF_TAX_AMOUNT_OTHER_THAN_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| TAXABLE_AMOUNT_ID | NUMBER(5) | N |  |
| TAXABLE_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TAXABLE_AMOUNT_ID`: TAXABLE_AMOUNT_ID
- **Triggers**: `DEF_TAX_AMOUNT_OTHER_THAN_SAL_CEA` (before insert or update or delete), `DEF_TAX_AMOUNT_OTHER_THAN__DEL` (after delete), `DEF_TAX_AMOUNT_OTHER_THAN__INS` (before insert), `DEF_TAX_AMOUNT_OTHER_THAN__UPD` (before update), `TRG_WS_ALH_HY_ST_Q` (after insert or update or delete)

## PAYROLL.EMPLOYEE_INCOME_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PAY_START_DATE | DATE | N |  |
| PAY_END_DATE | DATE | N |  |
| AD_CODE | VARCHAR2(50) | Y |  |
| AMOUNT | NUMBER(10,2) | N |  |
| PAYMENT_SOURCE | VARCHAR2(100) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| LINE_ITEM | VARCHAR2(4000) | Y |  |
| SOURCE | VARCHAR2(500) | Y |  |

_No standard audit columns._


## PAYROLL.EMPLOYEE_INCOME_DETAIL_FQ

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PAY_START_DATE | DATE | N |  |
| PAY_END_DATE | DATE | N |  |
| AD_CODE | VARCHAR2(50) | Y |  |
| AMOUNT | NUMBER(10,2) | N |  |
| PAYMENT_SOURCE | VARCHAR2(100) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| LINE_ITEM | VARCHAR2(4000) | Y |  |
| SOURCE | VARCHAR2(500) | Y |  |

_No standard audit columns._


## PAYROLL.EMP_ALLOWANCE_DEDUCTION
This table is used to link employees with different types of allowances and deductions

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N | PK- allowance / deduction code |
| MRNO | VARCHAR2(14) | N | PK- Employee medical record number |
| INITIAL_AMOUNT | NUMBER(20,2) | Y | Value at the service joining time |
| CURRENT_AMOUNT | NUMBER(20,2) | Y | Current value |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EMP_ALLOWANCE_DEDUCTION`: AD_CODE, MRNO
- **FK** `FK_EMP_ALLOWANCE_DEDUCTION_2`: (MRNO) -> PAYROLL.DEF_EMP_FINANCIAL(MRNO)
- **FK** `FK_EMP_ALLOW_DEDUC`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **Triggers**: `EMP_ALLOWANCE_DEDUCTION_DEL` (after delete), `EMP_ALLOWANCE_DEDUCTION_INS` (before insert), `EMP_ALLOWANCE_DEDUCTION_UPD` (before update)

## PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(10,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | Y |  |
| POSTED | CHAR(1) default 'N' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y | Ref to payroll.process_increment_master, if increment is processed through a process |

- **PK** `PK_EMP_ALLOWANCE_DED_DETAIL`: AD_CODE, MRNO, FROM_DATE
- **FK** `FK_EMP_ALLOW_DED`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **CHECK** `CK_EMP_ALL_DED_DETAIL_1`: POSTED IN ('Y','N'
- **Triggers**: `EMP_ALLOWANCE_DEDUCTION_DE_DEL` (after delete), `EMP_ALLOWANCE_DEDUCTION_DE_INS` (before insert), `EMP_ALLOWANCE_DEDUCTION_DE_UPD` (before update)

## PAYROLL.EMP_AWARDS

| Column | Type | Null | Comment |
|---|---|---|---|
| AWARD_ID | VARCHAR2(11) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| EXPENSE_CODE | CHAR(3) | Y |  |
| DUE_DATE | DATE | Y |  |
| JOINING_DATE | DATE | Y |  |
| ENTRY_DATE | DATE | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |
| PAYMENT_BASE | CHAR(1) | N |  |
| PAYMENT_RATE | NUMBER(5,2) | N |  |
| AWARD_AMOUNT | NUMBER(20,2) | N |  |
| ADJ_DUE_AMOUNT | NUMBER(20,2) | Y |  |
| ADJ_DUE_DATE | DATE | Y |  |

- **PK** `PK_EMP_AWARDS`: AWARD_ID
- **UK** `UK_EMP_AWARDS`: MRNO, DUE_DATE, EXPENSE_CODE
- **Triggers**: `EMP_AWARDS_DEL` (after delete), `EMP_AWARDS_INS` (before insert), `EMP_AWARDS_UPD` (before update)

## PAYROLL.EMP_AWARD_PAYMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| PAYMENT_ID | VARCHAR2(12) | N |  |
| AWARD_ID | VARCHAR2(11) | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |
| BASE_GROSS | NUMBER(20,2) | N |  |
| BASE_BASIC | NUMBER(20,2) | N |  |
| AMOUNT | NUMBER(20,2) | N |  |
| PAYMENT_BY | VARCHAR2(14) | N |  |
| PAYMENT_DATE | DATE | N |  |
| MON_START_DATE | DATE | Y |  |
| MON_END_DATE | DATE | Y |  |
| AD_CODE | VARCHAR2(3) | Y |  |
| DOCUMENT_NO | VARCHAR2(12) | Y |  |
| STATUS_ID | VARCHAR2(3) | N |  |

- **PK** `PK_EMP_AWARD_PAYMENT`: PAYMENT_ID
- **FK** `FK_EMP_AWARD_PAYMENT`: (AWARD_ID) -> PAYROLL.EMP_AWARDS(AWARD_ID) [disabled]
- **Triggers**: `EMP_AWARD_PAYMENT_DEL` (after delete), `EMP_AWARD_PAYMENT_INS` (before insert), `EMP_AWARD_PAYMENT_UPD` (before update)

## PAYROLL.EMP_EXPENSE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_NO | VARCHAR2(12) | N |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| EXPENSE_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| TRANS_DATE | DATE | N |  |
| CURRENT_GROSS | NUMBER(20,2) | Y |  |
| CURRENT_BASIC | NUMBER(20,2) | Y |  |
| CURRENT_LFA | NUMBER(20,2) | Y |  |
| SELF_DEPEND | CHAR(1) default 'N' | Y |  |
| DEPENDANT_MRNO | VARCHAR2(14) | Y |  |
| APPROVED_BY | VARCHAR2(25) | Y |  |
| AMOUNT | NUMBER(20,2) | N |  |
| REMARKS | VARCHAR2(255) | Y |  |
| CANCELLED | CHAR(1) default 'N' | Y |  |
| CANCELED_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCELED_VOUCHER_NO | CHAR(13) | Y |  |
| LFA_DUE_DATE | DATE | Y |  |
| SERVICE_YEARS | NUMBER(2) | Y |  |
| BONUS_PERCENT | NUMBER(5,2) | Y |  |
| GROSS_BASIC | CHAR(1) | Y |  |
| JOINING_DATE | DATE | Y |  |
| LONG_SERVICE_DATE | DATE | Y |  |
| LFA_ADJUST_NO | VARCHAR2(12) | Y |  |
| INCLUDE_IN_TAX | CHAR(1) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CLAIM_NO | VARCHAR2(12) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| TAX_DEDUCTED | NUMBER(20,2) | Y | This column is added to log manual tax payments |
| EXPENSE_LIST_ID | VARCHAR2(12) | Y | Ref to PAYROLL.EMP_EXPENSE_LIST |

- **PK** `PK_EMP_EXPENSE`: DOCUMENT_NO
- **FK** `FK_EMP_EXPENSE_1`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_EMP_EXPENSE_2`: (CANCELED_VOUCHER_TYPE, CANCELED_VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_EMP_EXPENSE_4`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **CHECK** `CK_EMP_EXPENSE_1`: SELF_DEPEND IN ('S', 'D'
- **CHECK** `CK_EMP_EXPENSE_2`: CANCELLED IN ('Y', 'N'
- **CHECK** `CK_EMP_EXPENSE_3`: INCLUDE_IN_TAX IN ('Y', 'N'
- **Triggers**: `EMP_EXPENSE_DEL` (after delete), `EMP_EXPENSE_INS` (before insert), `EMP_EXPENSE_UPD` (before update)

## PAYROLL.EMP_EXPENSE_LIST

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_LIST_ID | VARCHAR2(9) | N |  |
| EXPENSE_CODE | CHAR(3) | N |  |
| TRANS_DATE | DATE | N |  |
| REMARKS | VARCHAR2(255) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EMP_EXPENSE_LIST`: EXPENSE_LIST_ID

## PAYROLL.EMP_EXPENSE_LIST_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_LIST_ID | VARCHAR2(9) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| TAX_DEDUCTED | NUMBER(20,2) | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| SELECT_FLAG | CHAR(1) | Y |  |
| ERROR_LOG | VARCHAR2(1000) | Y |  |

- **PK** `PK_EMP_EXPENSE_LIST_DTL`: EXPENSE_LIST_ID, MRNO
- **FK** `FK_EMP_EXPENSE_LIST_DTL`: (EXPENSE_LIST_ID) -> PAYROLL.EMP_EXPENSE_LIST(EXPENSE_LIST_ID)

## PAYROLL.EMP_EXP_DET_PROJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_NO | VARCHAR2(12) | N |  |
| PROJECT_ID | VARCHAR2(7) | N |  |
| AMOUNT | NUMBER | Y |  |

- **PK** `PK_EMP_EXP_DET_PROJECT`: DOCUMENT_NO, PROJECT_ID
- **Triggers**: `EMP_EXP_DET_PROJECT_DEL` (after delete), `EMP_EXP_DET_PROJECT_INS` (before insert), `EMP_EXP_DET_PROJECT_UPD` (before update)

## PAYROLL.EMP_INCREMENT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| INCREMENT_DATE | DATE | N |  |
| INCREMENT_CODE | CHAR(3) | N |  |
| APPROVED_BY | VARCHAR2(25) | Y |  |
| INCR_AMOUNT | NUMBER(20,2) | Y |  |
| INCR_PERCENT | NUMBER(6,2) | Y |  |
| CURRENT_BASIC | NUMBER(20,2) | Y |  |
| CURRENT_GROSS | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| INCREMENT_END_DATE | DATE | Y |  |
| PREVIOUS_BASIC | NUMBER(20,2) | Y |  |
| PREVIOUS_GROSS | NUMBER(20,2) | Y |  |
| POSTED | CHAR(1) default 'N' | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| ARREAR_PAID | CHAR(1) | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y | Ref to payroll.process_increment_master, if increment is processed through a process |

- **PK** `PK_EMP_INCREMENT_MASTER`: MRNO, INCREMENT_DATE
- **FK** `FK_EMP_INCREMENT_MASTER_1`: (INCREMENT_CODE) -> PAYROLL.DEF_INCREMENT_TYPE(INCREMENT_CODE)
- **FK** `FK_EMP_INCREMENT_MASTER_2`: (MRNO) -> HRD.INFORMATION(MRNO)
- **CHECK** `CK_EMP_INCREMENT_MASTER_1`: POSTED IN ('Y','N'
- **Triggers**: `EMP_INCREMENT_MASTER_DEL` (after delete), `EMP_INCREMENT_MASTER_INS` (before insert), `EMP_INCREMENT_MASTER_UPD` (before update)

## PAYROLL.EMP_INCREMENT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| INCREMENT_DATE | DATE | N |  |
| CURRENT_AMOUNT | NUMBER(20,2) | Y |  |
| PREVIOUS_AMOUNT | NUMBER(20,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EMP_INCREMENT_DETAIL`: AD_CODE, MRNO, INCREMENT_DATE
- **FK** `FK_EMP_INCREMENT_DETAIL_2`: (MRNO, INCREMENT_DATE) -> PAYROLL.EMP_INCREMENT_MASTER(MRNO, INCREMENT_DATE) [disabled]
- **FK** `FK_EMP_INCR_DETAIL`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **Triggers**: `EMP_INCREMENT_DETAIL_DEL` (after delete), `EMP_INCREMENT_DETAIL_INS` (before insert), `EMP_INCREMENT_DETAIL_UPD` (before update)

## PAYROLL.EMP_ITAX_ADJUSTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ADJUSTMENT_CODE | NUMBER(2) | N |  |
| AMOUNT | NUMBER(10) default 0 | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| CURRENT_TAX | NUMBER(15) | Y |  |
| CURRENT_INCOME | NUMBER(15) | Y |  |
| POSTED | CHAR(1) | Y |  |

- **PK** `PK_EMP_ITAX_ADJUSTMENT`: YEAR_CODE, MRNO, ADJUSTMENT_CODE
- **FK** `FK_EMP_ITAX_ADJUSTMENT`: (YEAR_CODE) -> PAYROLL.PAY_FINANCIAL_YEAR(YEAR_CODE)
- **Triggers**: `EMP_ITAX_ADJUSTMENT_DEL` (after delete), `EMP_ITAX_ADJUSTMENT_INS` (before insert), `EMP_ITAX_ADJUSTMENT_UPD` (before update)

## PAYROLL.EMP_ITAX_ADJUSTMENT_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | VARCHAR2(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ADJUSTMENT_CODE | NUMBER(2) | N |  |
| SRNO | NUMBER(2) | N |  |
| AMOUNT | NUMBER(10) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_EMP_ITAX_ADJUSTMENT_DTL`: YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO

## PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | VARCHAR2(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ADJUSTMENT_CODE | NUMBER(2) | N |  |
| SRNO | NUMBER(2) | N |  |
| AMOUNT | NUMBER(10) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |

- **PK** `PK_EMP_ITAX_ADJUSTMENT_DTL_M_01`: YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO, START_DATE, END_DATE
- **Triggers**: `EMP_ITAX_ADJUSTMENT_DTL_M_DEL` (after delete), `EMP_ITAX_ADJUSTMENT_DTL_M_INS` (before insert), `EMP_ITAX_ADJUSTMENT_DTL_M_UPD` (before update)

## PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| ADJUSTMENT_CODE | NUMBER(2) | N |  |
| AMOUNT | NUMBER(10) default 0 | Y |  |
| MONTHLY_AMOUNT | NUMBER(10) default 0 | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| CURRENT_TAX | NUMBER(15) | Y |  |
| CURRENT_INCOME | NUMBER(15) | Y |  |
| POSTED | CHAR(1) | Y |  |
| ADJUSTED | CHAR(1) default 'N' | Y |  |
| ORDER_BY | NUMBER | Y |  |
| EXEMPTED_AMOUNT | NUMBER(15) | Y |  |

- **PK** `PK_EMP_ITAX_ADJUSTMENT_MONTHLY`: YEAR_CODE, MRNO, ADJUSTMENT_CODE, START_DATE
- **FK** `FK_EMP_ITAX_ADJUSTMENT_MONTHLY`: (YEAR_CODE) -> PAYROLL.PAY_FINANCIAL_YEAR(YEAR_CODE)
- **Triggers**: `SYN_EMP_ITAX_ADJ_MON_DEL` (after delete), `SYN_EMP_ITAX_ADJ_MON_INS` (before insert), `SYN_EMP_ITAX_ADJ_MON_UPD` (before update)

## PAYROLL.EMP_LIABILITY

| Column | Type | Null | Comment |
|---|---|---|---|
| LIABILITY_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| LIABILITY_DATE | DATE | Y |  |
| CLEAR_DATE | DATE | Y |  |
| STATUS | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |

- **PK** `PK_EMP_LIABILITY`: LIABILITY_CODE, MRNO
- **FK** `FK_EMP_LIABILITY_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_LIABILITY_2`: (LIABILITY_CODE) -> PAYROLL.DEF_LIABILITY(LIABILITY_CODE)
- **CHECK** `CK_EMP_LIABILITY_1`: STATUS IN ('C', 'N'
- **Triggers**: `EMP_LIABILITY_DEL` (after delete), `EMP_LIABILITY_INS` (before insert), `EMP_LIABILITY_UPD` (before update)

## PAYROLL.EMP_NEW_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | NUMBER | Y |  |
| CURRENT_SAL | NUMBER | Y |  |
| INC_AGE | NUMBER | Y |  |
| INCR_AMNT | NUMBER | Y |  |
| NEW_SAL | NUMBER | Y |  |


## PAYROLL.EMP_PAYMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| DOCUMENT_NO | VARCHAR2(12) | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EMP_PAYMENT`: START_DATE, END_DATE, MRNO
- **FK** `FK_EMP_PAYMENT_01`: (DOCUMENT_NO) -> PAYROLL.EMP_EXPENSE(DOCUMENT_NO) [disabled]
- **Triggers**: `EMP_PAYMENT_DEL` (after delete), `EMP_PAYMENT_INS` (before insert), `EMP_PAYMENT_UPD` (before update)

## PAYROLL.EMP_TAX_AMOUNT_OTHER_THAN_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| YEAR | VARCHAR2(4) | N |  |
| TAXABLE_AMOUNT_TYPE_ID | NUMBER(5) | N |  |
| TAXABLE_AMOUNT | NUMBER(10) | Y |  |

- **PK** `PK_EMP_TAX_AMOUNT_OTH_SAL`: MRNO, YEAR, TAXABLE_AMOUNT_TYPE_ID
- **FK** `FK_EMP_TAX_AMOUNT_OTH_MRNO`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_TAX_AMOUNT_TYPE_ID`: (TAXABLE_AMOUNT_TYPE_ID) -> PAYROLL.DEF_TAX_AMOUNT_OTHER_THAN_SAL(TAXABLE_AMOUNT_ID) [disabled]
- **Triggers**: `EMP_TAX_AMOUNT_OTHER_THAN__DEL` (after delete), `EMP_TAX_AMOUNT_OTHER_THAN__INS` (before insert), `EMP_TAX_AMOUNT_OTHER_THAN__UPD` (before update)

## PAYROLL.EXPENSE_CLAIM_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| EXPENSE_CODE | VARCHAR2(3) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| TRANS_DATE | DATE | Y |  |
| ADVANCE_GIVEN | NUMBER(10) | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| SIGN_DATE | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| APPROVER_REMARKS | VARCHAR2(500) | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| APPROVED_DATE | DATE | Y |  |
| TRAVEL_REQUEST_NO | NUMBER | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTURE_DATE | DATE | Y |  |
| RETURN_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| REVISION_NO | NUMBER | Y |  |
| AUTHORITY_MRNO | VARCHAR2(14) | Y |  |
| WFE_NO | NUMBER(3) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCELLED_VOUCHER_NO | CHAR(13) | Y |  |
| REFUND_NO | VARCHAR2(12) | Y |  |

- **PK** `PK_EXPENSE_CLAIM_MASTER`: CLAIM_NO
- **Triggers**: `EXPENSE_CLAIM_MASTER_DEL` (after delete), `EXPENSE_CLAIM_MASTER_INS` (after insert), `EXPENSE_CLAIM_MASTER_UPD` (before update)

## PAYROLL.EXPENSE_CLAIM_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| SRNO | NUMBER(2) | N |  |
| EXPENSE_TYPE_ID | VARCHAR2(3) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| CLAIM_AMOUNT | NUMBER(10) | Y |  |
| APPROVED_AMOUNT | NUMBER(10) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| DAYS_CLAIMED | NUMBER(4,1) | Y |  |
| DAYS_APPROVED | NUMBER(4,1) | Y |  |
| SLAB_ID | VARCHAR2(12) | Y |  |
| ENTRY_TYPE | CHAR(1) | Y |  |
| CALC_METHOD | CHAR(1) | Y |  |

- **PK** `PK_EXPENSE_CLAIM_DETAIL`: CLAIM_NO, SRNO
- **FK** `FK_CLAIM_NO`: (CLAIM_NO) -> PAYROLL.EXPENSE_CLAIM_MASTER(CLAIM_NO)
- **Triggers**: `EXPENSE_CLAIM_DETAIL_DEL` (after delete), `EXPENSE_CLAIM_DETAIL_INS` (before insert), `EXPENSE_CLAIM_DETAIL_UPD` (before update)

## PAYROLL.EXPENSE_CLAIM_DOCUMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(13) | N |  |
| CLAIM_NO | VARCHAR2(12) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_EXPENSE_CLAIM_DOCUMENT`: DOCUMENT_ID
- **FK** `FK_EXPENSE_CLAIM_DOCUMENT`: (CLAIM_NO) -> PAYROLL.EXPENSE_CLAIM_MASTER(CLAIM_NO)

## PAYROLL.EXPENSE_CLAIM_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_ID | NUMBER | N |  |
| AUTHORITY_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORDERBY | NUMBER | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| REJECTED | VARCHAR2(1) default 'N' | Y |  |
| MODIFICATION | VARCHAR2(1) default 'N' | Y |  |

_No standard audit columns._

- **Triggers**: `TRG_EXP_CLAIM_HIERARCHY_ID` (before insert)

## PAYROLL.EXPENSE_CLAIM_HIERARCHY_ORG

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_ID | NUMBER | N |  |
| AUTHORITY_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORDERBY | NUMBER | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

_No standard audit columns._

- **Triggers**: `TRG_EXP_CLAIM_HIERARCHY_ORG_ID` (before insert)

## PAYROLL.EXPENSE_CLAIM_PROJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| PROJECT_ID | VARCHAR2(7) | N |  |
| EXP_PERCENTAGE | NUMBER | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_EXP_CLAIM_PROJECT`: CLAIM_NO, PROJECT_ID
- **FK** `FK_CLAIM_NO_ECP`: (CLAIM_NO) -> PAYROLL.EXPENSE_CLAIM_MASTER(CLAIM_NO)
- **FK** `FK_PROJECT_ID_ECP`: (PROJECT_ID) -> PAYROLL.DEF_PROJECT(PROJECT_ID) [disabled]
- **CHECK** `CK_PERCENTAGE`: EXP_PERCENTAGE > 0
- **Triggers**: `EXPENSE_CLAIM_PROJECT_DEL` (after delete), `EXPENSE_CLAIM_PROJECT_INS` (before insert), `EXPENSE_CLAIM_PROJECT_UPD` (before update)

## PAYROLL.EXPENSE_CLAIM_WORKFLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | Y |  |
| WORK_FLOW_ID | NUMBER(4) | Y |  |
| EVENT_ID | NUMBER(3) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |

- **PK** `PK_EXPENSE_CLAIM_WORKFLOW`: CLAIM_NO, WFE_NO

## PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

- **PK** `PK_EXPENSE_CLAIM_WF_Q`: CLAIM_NO, WFE_NO, ASSIGNEE_MRNO
- **Triggers**: `EXPENSE_CLAIM_WORKFLOW_Q_APPR_INS` (before insert), `EXPENSE_CLAIM_WORKFLOW_Q_INS` (before insert)

## PAYROLL.FINAL_SETTLEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| TRANS_DATE | DATE | Y |  |
| ZAKAT | VARCHAR2(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| SIGN_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| WFE_NO | NUMBER(3) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | Y | PK of CLEARANCE_CERTIFICATE |
| ORGANIZATION_ID | VARCHAR2(3) | Y | PK of CLEARANCE_CERTIFICATE |
| LOCATION_ID | VARCHAR2(3) | Y | PK of CLEARANCE_CERTIFICATE |
| LFA_STATUS | VARCHAR2(1) | Y | N = None, P = To be Paid, D = To be deducted |
| STATUS_ID | VARCHAR2(3) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| INCOME_TAX | NUMBER(20,2) | Y |  |
| DOCUMENT_NO | VARCHAR2(12) | Y |  |
| PF_CHEQUE_ACK | VARCHAR2(1) | Y |  |

- **PK** `PK_FINAL_SETTLEMENT`: FINAL_SETTLEMENT_ID
- **Triggers**: `FINAL_SETTLEMENT_DEL` (after delete), `FINAL_SETTLEMENT_INS` (before insert), `FINAL_SETTLEMENT_UPD` (before update), `FS_PQ_UPD` (before update)

## PAYROLL.FINAL_SETTLEMENT_ELEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| ELEMENT_CODE | VARCHAR2(8) | N |  |
| AMOUNT | NUMBER(10) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| VALUE | NUMBER(8,4) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTUAL_AMOUNT | NUMBER(10) | Y |  |

- **PK** `PK_FINAL_SETTLEMENT_ELEMENT`: FINAL_SETTLEMENT_ID, ELEMENT_CODE
- **Triggers**: `FINAL_SETTLEMENT_ELEMENT_DEL` (after delete), `FINAL_SETTLEMENT_ELEMENT_INS` (before insert), `FINAL_SETTLEMENT_ELEMENT_UPD` (before update)

## PAYROLL.FINAL_SETTLEMENT_WF

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | Y |  |
| WORK_FLOW_ID | NUMBER(4) | Y |  |
| EVENT_ID | NUMBER(3) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |

_No standard audit columns._


## PAYROLL.FINAL_SETTLEMENT_WF_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

_No standard audit columns._

- **Triggers**: `FS_WORKFLOW_PQ_INS` (before insert)

## PAYROLL.GENERIC_REPORT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_ID | NUMBER(8) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | Y |  |

- **PK** `PK_GENERIC_REPORT_MASTER`: REPORT_ID
- **Triggers**: `GENERIC_REPORT_MASTER_CEA` (before insert or update or delete), `GENERIC_REPORT_MASTER_DEL` (after delete), `GENERIC_REPORT_MASTER_INS` (before insert), `GENERIC_REPORT_MASTER_UPD` (before update), `TRG_WS_WXW_JX_NS_Q` (after insert or update or delete)

## PAYROLL.GENERIC_REPORT_FIELD

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_ID | NUMBER(8) | N |  |
| FIELD_CODE | VARCHAR2(64) | N |  |
| PROMPT | VARCHAR2(500) | Y |  |
| AD_CODE | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| DISPLAY | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `PK_GENERIC_REPORT_FIELD`: REPORT_ID, FIELD_CODE
- **FK** `FK_GENERIC_REPORT_FIELD`: (REPORT_ID) -> PAYROLL.GENERIC_REPORT_MASTER(REPORT_ID)
- **Triggers**: `GENERIC_REPORT_FIELD_CEA` (before insert or update or delete), `GENERIC_REPORT_FIELD_DEL` (after delete), `GENERIC_REPORT_FIELD_INS` (before insert), `GENERIC_REPORT_FIELD_UPD` (before update), `TRG_WS_EMS_YD_EF_Q` (after insert or update or delete)

## PAYROLL.GENERIC_REPORT_FIELD_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_ID | NUMBER(8) | N |  |
| FIELD_CODE | VARCHAR2(64) | N |  |
| SRNO | NUMBER(2) | N |  |
| ADD_SUBSTRACT | CHAR(1) | Y |  |
| SUB_FIELD_CODE | VARCHAR2(64) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_GENERIC_RPT_FIELD_DTL`: REPORT_ID, FIELD_CODE, SRNO
- **FK** `FK_GENERIC_RPT_FIELD_DTL`: (REPORT_ID, FIELD_CODE) -> PAYROLL.GENERIC_REPORT_FIELD(REPORT_ID, FIELD_CODE)
- **Triggers**: `GENERIC_REPORT_FIELD_DTL_CEA` (before insert or update or delete), `GENERIC_REPORT_FIELD_DTL_PK` (before insert), `TRG_WS_IKE_GP_IJ_Q` (after insert or update or delete)

## PAYROLL.HOLD_ORDER

| Column | Type | Null | Comment |
|---|---|---|---|
| HOLD_ORDER_ID | NUMBER(20) | N |  |
| TRANS_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| FROM_MONTH | CHAR(6) | Y |  |
| HOLD | CHAR(1) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| UNHOLD_REASON | VARCHAR2(500) | Y |  |
| UNHOLD_DATE | DATE | Y |  |

- **PK** `PK_HOLD_ORDER`: HOLD_ORDER_ID
- **Triggers**: `HOLD_ORDER_DEL` (after delete), `HOLD_ORDER_INS` (before insert), `HOLD_ORDER_UPD` (before update)

## PAYROLL.ITAX_PAYMENT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| DEPOSIT_DATE | DATE | Y |  |
| BANK_TREASURY | VARCHAR2(64) | Y |  |
| BRANCH_CITY | VARCHAR2(64) | Y |  |
| ACCOUNT | VARCHAR2(32) | Y |  |
| CPRNO | VARCHAR2(32) | Y |  |

- **PK** `PKITAX_PAYMENT_DETAIL`: YEAR_CODE, ORGANIZATION_ID, LOCATION_ID, START_DATE, END_DATE
- **Triggers**: `ITAX_PAYMENT_DETAIL_DEL` (after delete), `ITAX_PAYMENT_DETAIL_INS` (before insert), `ITAX_PAYMENT_DETAIL_UPD` (before update)

## PAYROLL.ITAX_PAYMENT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| YEAR_CODE | NUMBER(4) | N |  |
| PERSON_ADDRESS | VARCHAR2(250) | Y |  |
| SECTION_CODE | VARCHAR2(32) | Y |  |
| SECTION_DESCRIPTION | VARCHAR2(250) | Y |  |
| VIDE | VARCHAR2(250) | Y |  |
| COMPANY_NAME | VARCHAR2(250) | Y |  |
| SIGN_AUTHORITY | VARCHAR2(14) | Y |  |
| PRINT_ALLOWED | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_ITAX_PAYMENT_MASTER`: ORGANIZATION_ID, LOCATION_ID, YEAR_CODE
- **Triggers**: `ITAX_PAYMENT_MASTER_DEL` (after delete), `ITAX_PAYMENT_MASTER_INS` (before insert), `ITAX_PAYMENT_MASTER_UPD` (before update)

## PAYROLL.LEAVE_DAYS_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| SALARY_MONTH | VARCHAR2(6) | Y |  |
| UNPAID_STATUS | CHAR(1) | Y |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_LEAVE_DAYS_TEST`: MRNO, LEAVE_DATE
- **CHECK** `CHK_LEAVE_DAYS_TEST`: UNPAID_STATUS IN ('N','D','U'

## PAYROLL.LOAN_INSTALLMENT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_START_DATE | DATE | N |  |
| PAY_END_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| LOAN_NO | VARCHAR2(12) | N |  |
| TRANS_DATE | DATE | Y |  |
| LOAN_CODE | CHAR(3) | Y |  |
| SALARY_DEDUCTION_TYPE | CHAR(1) | Y |  |
| REFUND_WITH_PAY_VOUCHER | CHAR(1) | Y |  |
| REFUND_AD_CODE | CHAR(3) | Y |  |
| PRINCIPAL_AMOUNT | NUMBER(20,2) | Y |  |
| LOAN_INSTALLMENT | NUMBER(20,2) | Y |  |
| INTEREST_INSTALLMENT | NUMBER(20,2) | Y |  |
| ACTUAL_INSTALLMENT | NUMBER(20,2) | Y |  |
| TEMP_REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_NO | VARCHAR2(12) | Y |  |

- **PK** `PK_LOAN_INSTALLMENT_DETAIL`: PAY_START_DATE, PAY_END_DATE, MRNO, LOAN_NO

## PAYROLL.LOAN_PAYMENT_INTEREST

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N |  |
| YEAR_CODE | NUMBER(4) | N |  |
| TRANS_DATE | DATE | Y |  |
| INTEREST_RATE | NUMBER(5,2) | Y | Current Interest Rate at time of this transaction |
| PRINCIPAL_AMOUNT | NUMBER(20,2) | Y | Total Pending Amount at time of this transaction |
| NO_OF_MONTHS | NUMBER(2) | Y | No of installments in a year |
| INTEREST_AMOUNT | NUMBER(20,2) | Y | Total Calculated Interest Amount |
| VOUCHER_TYPE | VARCHAR2(5) | Y | Interest Voucher Type |
| VOUCHER_NO | CHAR(13) | Y | Interest Voucher No |
| CANCELLED | CHAR(1) default 'N' | Y |  |
| CANCEL_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCEL_VOUCHER_NO | VARCHAR2(13) | Y |  |

- **PK** `PK_LOAN_PAYMENT_INTEREST`: LOAN_NO, YEAR_CODE
- **Triggers**: `LOAN_PAYMENT_INTEREST_DEL` (after delete), `LOAN_PAYMENT_INTEREST_INS` (before insert), `LOAN_PAYMENT_INTEREST_UPD` (before update)

## PAYROLL.LOAN_PAYMENT_MASTER
This table is used to entertain opening balances and transactions of staff advances

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N | Auto-generated Primary Key |
| TRANS_TYPE | CHAR(1) default 'L' | Y | Either "O" for Opening Balance or "L" for Loan / Advance transactions |
| TRANS_DATE | DATE | Y | Date of Loan transaction or Opening balances |
| MRNO | VARCHAR2(14) | Y | Employee code |
| LOAN_CODE | CHAR(3) | Y | LOan type (Advance, Car Loan etc.) |
| OPEN_ACTUAL_DATE | DATE | Y | Date of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_LOAN | NUMBER(20,2) | Y | Amount of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_INSTALLMENTS | NUMBER(5) | Y | Total Installments of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_MONTHLY | NUMBER(20,2) | Y | Monthly deduction (only valid for opening balances entry) |
| LOAN_AMOUNT | NUMBER(20,2) | N | Self explainatory |
| NO_OF_INSTALLMENTS | NUMBER(5) | Y | no. of Monthly installments |
| MONTHLY_INSTALLMENT | NUMBER(20,2) | Y | to be deducted from monthly salary |
| REFUND_AMOUNT | NUMBER(20,2) | Y | Total amount refunded todate |
| VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type |
| VOUCHER_NO | CHAR(13) | Y | GL Voucher number |
| STOP_AUTO_DEDUCTION | CHAR(1) default 'N' | Y | If deduction fomr salarty needs to be stopped then it will be "Y", otherwise "N". By default it will be "N" |
| REMARKS | VARCHAR2(255) | Y | Self explainatory |
| CANCELLED | CHAR(1) default 'N' | Y | If loan transaction needs to be cancelled, then it will be set to "Y", otherwise NULL |
| CANCEL_VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type, If loan transaction needs to be cancelled |
| CANCEL_VOUCHER_NO | VARCHAR2(13) | Y | GL Voucher number, If loan transaction needs to be cancelled |
| STOP_AUTO_DEDUCTION_TILL | DATE | Y |  |
| MERGED_LOAN_NO | VARCHAR2(12) | Y |  |
| MERGE | CHAR(1) default 'N' | Y |  |
| CONVERTED_LOAN_NO | VARCHAR2(12) | Y |  |
| BASE_AMOUNT | NUMBER(20,2) | Y |  |
| BASE_CURRENCY_ID | VARCHAR2(3) default '001' | Y |  |
| BASE_CURRENCY_EXCHANGE_RATE | NUMBER(10,2) default 1 | Y |  |
| TEMP_LOAN_AMOUNT | NUMBER(20,2) | Y |  |
| LOAN_LOCATION_ID | VARCHAR2(3) | Y |  |
| TRAVEL_REQUEST_NO | NUMBER | Y |  |

- **PK** `PK_LOAN_PAYMENT_MASTER`: LOAN_NO
- **FK** `FK_LOAN_PAYMENT_MASTER_1`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_LOAN_PAYMENT_MASTER_3`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **CHECK** `CK_LOAN_PAYMENT_MASTER_1`: TRANS_TYPE IN ('O', 'L'
- **CHECK** `CK_LOAN_PAYMENT_MASTER_2`: CANCELLED IN ('Y', 'N'
- **CHECK** `CK_LOAN_PAYMENT_MASTER_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N'
- **Triggers**: `LOAN_PAYMENT_MASTER_DEL` (after delete), `LOAN_PAYMENT_MASTER_INS` (before insert), `LOAN_PAYMENT_MASTER_UPD` (before update)

## PAYROLL.LOAN_PAYMENT_MASTER_N
This table is used to entertain opening balances and transactions of staff advances

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N | Auto-generated Primary Key |
| TRANS_TYPE | CHAR(1) default 'L' | Y | Either "O" for Opening Balance or "L" for Loan / Advance transactions |
| TRANS_DATE | DATE | Y | Date of Loan transaction or Opening balances |
| MRNO | VARCHAR2(14) | Y | Employee code |
| LOAN_CODE | CHAR(3) | Y | LOan type (Advance, Car Loan etc.) |
| OPEN_ACTUAL_DATE | DATE | Y | Date of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_LOAN | NUMBER(20,2) | Y | Amount of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_INSTALLMENTS | NUMBER(5) | Y | Total Installments of loan (only valid for opening balances entry) |
| OPEN_ACTUAL_MONTHLY | NUMBER(20,2) | Y | Monthly deduction (only valid for opening balances entry) |
| LOAN_AMOUNT | NUMBER(20,2) | N | Self explainatory |
| NO_OF_INSTALLMENTS | NUMBER(5) | Y | no. of Monthly installments |
| REFUND_AMOUNT | NUMBER(20,2) | Y | Total amount refunded todate |
| VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type |
| VOUCHER_NO | CHAR(13) | Y | GL Voucher number |
| STOP_AUTO_DEDUCTION | CHAR(1) default 'N' | Y | If deduction fomr salarty needs to be stopped then it will be "Y", otherwise "N". By default it will be "N" |
| REMARKS | VARCHAR2(255) | Y | Self explainatory |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type, If loan transaction needs to be cancelled |
| CANCELLED_VOUCHER_NO | VARCHAR2(13) | Y | GL Voucher number, If loan transaction needs to be cancelled |
| STOP_AUTO_DEDUCTION_TILL | DATE | Y |  |
| BASE_CURRENCY_ID | VARCHAR2(3) default '001' | Y |  |
| BASE_CURRENCY_EXCHANGE_RATE | NUMBER(10,2) default 1 | Y |  |
| TEMP_LOAN_AMOUNT | NUMBER(20,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOAN_LOCATION_ID | VARCHAR2(3) | Y |  |
| MODULE | VARCHAR2(2) | Y | PF, GL |
| STATUS_ID | VARCHAR2(3) default '100' | N | 100 -> ENTRY, 101 -> POST, 102 -> CANCEL |
| INTEREST_AMOUNT | NUMBER(20,2) | Y |  |
| LOAN_INSTALLMENT | NUMBER(20,2) | Y |  |
| INTEREST_INSTALLMENT | NUMBER(20,2) | Y |  |
| PAID_INTEREST | NUMBER(20,2) | Y |  |

- **PK** `PK_LOAN_PAYMENT_MASTER_N`: LOAN_NO
- **CHECK** `CK_LOAN_PAYMENT_MASTER_N_1`: TRANS_TYPE IN ('O', 'L', 'R'
- **CHECK** `CK_LOAN_PAYMENT_MASTER_N_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N'
- **Triggers**: `LOAN_PAYMENT_MASTER_N_DEL` (after delete), `LOAN_PAYMENT_MASTER_N_INS` (before insert), `LOAN_PAYMENT_MASTER_N_UPD` (before update)

## PAYROLL.LOAN_PAYMENT_MASTER_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N |  |
| TRANS_TYPE | CHAR(1) | Y |  |
| TRANS_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| LOAN_CODE | CHAR(3) | Y |  |
| OPEN_ACTUAL_DATE | DATE | Y |  |
| OPEN_ACTUAL_LOAN | NUMBER(20,2) | Y |  |
| OPEN_ACTUAL_INSTALLMENTS | NUMBER(5) | Y |  |
| OPEN_ACTUAL_MONTHLY | NUMBER(20,2) | Y |  |
| LOAN_AMOUNT | NUMBER(20,2) | N |  |
| NO_OF_INSTALLMENTS | NUMBER(5) | Y |  |
| MONTHLY_INSTALLMENT | NUMBER(20,2) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| STOP_AUTO_DEDUCTION | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| CANCELLED | CHAR(1) | Y |  |
| CANCEL_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCEL_VOUCHER_NO | VARCHAR2(13) | Y |  |
| STOP_AUTO_DEDUCTION_TILL | DATE | Y |  |
| MERGED_LOAN_NO | VARCHAR2(12) | Y |  |
| MERGE | CHAR(1) default 'N' | Y |  |
| CONVERTED_LOAN_NO | VARCHAR2(12) | Y |  |
| BASE_AMOUNT | NUMBER(20,2) | Y |  |
| BASE_CURRENCY_ID | VARCHAR2(3) default '001' | Y |  |
| BASE_CURRENCY_EXCHANGE_RATE | NUMBER(10,2) default 1 | Y |  |
| LOAN_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_LOAN_PAYMENT_MASTER_TEST`: LOAN_NO
- **CHECK** `CK_LOAN_PAYMENT_MASTER_TEST_2`: CANCELLED IN ('Y', 'N'
- **CHECK** `CK_LOAN_PAYMENT_MASTER_TEST_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N'

## PAYROLL.LOAN_REFUND_MASTER
This table is used to entertain transactions of refunds advances or deductions of advances against salary

| Column | Type | Null | Comment |
|---|---|---|---|
| REFUND_NO | VARCHAR2(12) | N | Primary Key - auto-generated key |
| TRANS_DATE | DATE | Y | Date of refund or deduction |
| VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher Type |
| VOUCHER_NO | CHAR(13) | Y | GL Voucher Number |
| MRNO | VARCHAR2(14) | N | Employee code |
| REFUND_AMOUNT | NUMBER(20,2) | N | Amount to be refunded or deducted |
| REMARKS | VARCHAR2(255) | Y | Selef explainatory |
| CANCELLED | CHAR(1) default 'M' | Y | If refund transaction needs to be cancelled, then it will be set to "Y", otherwise NULL |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type, If refund transaction needs to be cancelled |
| CANCELLED_VOUCHER_NO | VARCHAR2(13) | Y | GL Voucher type, If refund transaction needs to be cancelled |
| REFUND_TYPE | CHAR(1) default 'M' | Y | Either "M" for Manul refunds or "S" for Automatic deductions from salary |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |

- **PK** `PK_LOAN_REFUND_MASTER`: REFUND_NO
- **FK** `FK_LOAN_REFUND_MASTER_1`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_LOAN_REFUND_MASTER_2`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **CHECK** `CK_LOAN_REFUND_MASTER_1`: CANCELLED IN ('Y', 'N'
- **CHECK** `CK_LOAN_REFUND_MASTER_2`: REFUND_TYPE IN ('M', 'S'
- **Triggers**: `LOAN_REFUND_MASTER_DEL` (after delete), `LOAN_REFUND_MASTER_INS` (before insert), `LOAN_REFUND_MASTER_UPD` (before update)

## PAYROLL.LOAN_REFUND_DETAIL
This table is used to entertain transactions of refunds advances or deductions of advances against salary

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N | Self explainatory |
| REFUND_NO | VARCHAR2(12) | N | Selef explainatory |
| START_DATE | DATE | Y | Start date of Salary period |
| END_DATE | DATE | Y | End date of Salary period |
| LOAN_AMOUNT | NUMBER(20,2) | Y | Self explainatory |
| REFUND_AMOUNT | NUMBER(20,2) | N | Self explainatory |
| MRNO | VARCHAR2(14) | Y |  |
| TEMP_REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_LOAN_REFUND_DETAIL`: LOAN_NO, REFUND_NO
- **FK** `FK_LOAN_PAYMENT_DETAIL_1`: (LOAN_NO) -> PAYROLL.LOAN_PAYMENT_MASTER(LOAN_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_2`: (REFUND_NO) -> PAYROLL.LOAN_REFUND_MASTER(REFUND_NO)
- **FK** `FK_LOAN_REFUND_DETAIL_1`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **FK** `FK_LOAN_REFUND_DETAIL_2`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **Triggers**: `LOAN_REFUND_DETAIL_DEL` (after delete), `LOAN_REFUND_DETAIL_INS` (before insert), `LOAN_REFUND_DETAIL_UPD` (before update)

## PAYROLL.LOAN_REFUND_MASTER_N
This table is used to entertain transactions of refunds advances or deductions of advances against salary

| Column | Type | Null | Comment |
|---|---|---|---|
| REFUND_NO | VARCHAR2(12) | N | Primary Key - auto-generated key |
| MODULE | VARCHAR2(2) | Y | PF, GL, CP, GP |
| REFUND_TYPE | CHAR(1) default 'M' | Y | Either "M" for Manul refunds or "S" for Automatic deductions from salary |
| TRANS_DATE | DATE | Y | Date of refund or deduction |
| VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher Type |
| VOUCHER_NO | CHAR(13) | Y | GL Voucher Number |
| PAY_START_DATE | DATE | Y |  |
| PAY_END_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | N | Employee code |
| REFUND_AMOUNT | NUMBER(20,2) | N | Amount to be refunded or deducted |
| REMARKS | VARCHAR2(255) | Y | Selef explainatory |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y | GL Voucher type, If refund transaction needs to be cancelled |
| CANCELLED_VOUCHER_NO | VARCHAR2(13) | Y | GL Voucher type, If refund transaction needs to be cancelled |
| RECEIPT_NO | VARCHAR2(13) | Y |  |
| STATUS_ID | VARCHAR2(3) default '100' | N | 100 -> ENTRY, 101 -> POST, 102 -> CANCEL |

- **PK** `PK_LOAN_REFUND_MASTER_N`: REFUND_NO
- **CHECK** `CK_LOAN_REFUND_MASTER_N_2`: REFUND_TYPE IN ('M', 'S'
- **Triggers**: `LOAN_REFUND_MASTER_N_DEL` (after delete), `LOAN_REFUND_MASTER_N_INS` (before insert), `LOAN_REFUND_MASTER_N_UPD` (before update)

## PAYROLL.LOAN_REFUND_DETAIL_N
This table is used to entertain transactions of refunds advances or deductions of advances against salary

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N | Self explainatory |
| REFUND_NO | VARCHAR2(12) | N | Selef explainatory |
| LOAN_AMOUNT | NUMBER(20,2) | Y | Self explainatory |
| REFUND_AMOUNT | NUMBER(20,2) | N | Self explainatory |
| TEMP_REFUND_AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_LOAN_REFUND_DETAIL_N`: LOAN_NO, REFUND_NO
- **FK** `FK_LOAN_PAYMENT_DETAIL_N1`: (LOAN_NO) -> PAYROLL.LOAN_PAYMENT_MASTER_N(LOAN_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_N2`: (REFUND_NO) -> PAYROLL.LOAN_REFUND_MASTER_N(REFUND_NO)
- **Triggers**: `LOAN_REFUND_DETAIL_N_DEL` (after delete), `LOAN_REFUND_DETAIL_N_INS` (before insert), `LOAN_REFUND_DETAIL_N_UPD` (before update)

## PAYROLL.LOAN_REFUND_MASTER_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| REFUND_NO | VARCHAR2(12) | N |  |
| TRANS_DATE | DATE | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| REFUND_AMOUNT | NUMBER(20,2) | N |  |
| REMARKS | VARCHAR2(255) | Y |  |
| CANCELLED | CHAR(1) | Y |  |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCELLED_VOUCHER_NO | VARCHAR2(13) | Y |  |
| REFUND_TYPE | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |

- **PK** `PK_LOAN_REFUND_MASTER_TEST`: REFUND_NO
- **CHECK** `CK_LOAN_REFUND_MASTER_TEST_1`: CANCELLED IN ('Y', 'N'
- **CHECK** `CK_LOAN_REFUND_MASTER_TEST_5`: REFUND_TYPE IN ('M', 'S'

## PAYROLL.LOAN_REFUND_DETAIL_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N |  |
| REFUND_NO | VARCHAR2(12) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| LOAN_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| TEMP_REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_LOAN_REFUND_DETAIL_TEST`: LOAN_NO, REFUND_NO
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_1`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_2`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_3`: (REFUND_NO) -> PAYROLL.LOAN_REFUND_MASTER_TEST(REFUND_NO)
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_4`: (LOAN_NO) -> PAYROLL.LOAN_PAYMENT_MASTER_TEST(LOAN_NO)

## PAYROLL.LOAN_REFUND_OPENING

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N |  |
| SR_NO | NUMBER(2) | N |  |
| REFUND_DATE | DATE | Y |  |
| REFUND_TYPE | CHAR(1) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_LOAN_REFUND_OPENING`: LOAN_NO, SR_NO
- **Triggers**: `LOAN_REFUND_OPENING_DEL` (after delete), `LOAN_REFUND_OPENING_INS` (before insert), `LOAN_REFUND_OPENING_UPD` (before update)

## PAYROLL.MANUAL_MONTH_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| TRANS_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| CANCEL_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCEL_VOUCHER_NO | CHAR(13) | Y |  |
| STATUS | CHAR(1) | Y |  |

- **PK** `PK_MANUAL_MONTH_MASTER`: START_DATE, END_DATE, SERIAL_NO

## PAYROLL.MANUAL_PAY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(7) | Y |  |

- **PK** `PK_MANUAL_PAY_MASTER`: START_DATE, END_DATE, SERIAL_NO, MRNO
- **FK** `FK_MANUAL_PAY_MASTER`: (START_DATE, END_DATE, SERIAL_NO) -> PAYROLL.MANUAL_MONTH_MASTER(START_DATE, END_DATE, SERIAL_NO)

## PAYROLL.MANUAL_ALLOWANCE_DEDUCTION

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| AMOUNT | NUMBER(7) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |

- **PK** `PK_MANUAL_ALLOWANCE_DEDUCTION`: START_DATE, END_DATE, SERIAL_NO, MRNO, AD_CODE
- **FK** `FK_MANUAL_ALLOWANCE_DEDUCTION`: (START_DATE, END_DATE, SERIAL_NO, MRNO) -> PAYROLL.MANUAL_PAY_MASTER(START_DATE, END_DATE, SERIAL_NO, MRNO)

## PAYROLL.MONTH_CHANGE_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_NO | NUMBER | N |  |
| REQUEST_DATE | DATE default SYSDATE | Y |  |
| MON_START_DATE | DATE | Y |  |
| MON_END_DATE | DATE | Y |  |
| PAY_START_DATE | DATE | Y |  |
| PAY_END_DATE | DATE | Y |  |
| NEW_MON_START_DATE | DATE | Y |  |
| NEW_MON_END_DATE | DATE | Y |  |
| APPROVE_STATUS | VARCHAR2(1) | Y | P = Pending, A = Approved, R = Rejected |
| APPROVE_DATE | DATE | Y |  |
| APPROVE_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **Triggers**: `MONTH_CHANGE_REQUEST_DEL` (after delete), `MONTH_CHANGE_REQUEST_INS` (before insert), `MONTH_CHANGE_REQUEST_PQ` (before insert or update), `MONTH_CHANGE_REQUEST_UPD` (before update)

## PAYROLL.MONTH_CHANGE_REQUEST_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_NAME | VARCHAR2(2000) | Y |  |
| RESULT_COUNT | NUMBER | Y |  |
| MON_START_DATE | DATE | Y |  |
| MON_END_DATE | DATE | Y |  |

_No standard audit columns._


## PAYROLL.PAY_AD_BALANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| BALANCE_AMOUNT | NUMBER(20,2) default 0 | Y |  |
| LOAN_AMOUNT | NUMBER(20,2) default 0 | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PAY_AD_BALANCE`: MRNO, START_DATE, END_DATE, AD_CODE
- **Triggers**: `PAY_AD_BALANCE_DEL` (after delete), `PAY_AD_BALANCE_INS` (before insert), `PAY_AD_BALANCE_UPD` (before update)

## PAYROLL.PAY_AD_BALANCE_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| BALANCE_AMOUNT | NUMBER(20,2) default 0 | Y |  |
| LOAN_AMOUNT | NUMBER(20,2) default 0 | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_AD_BALANCE_TEST`: MRNO, START_DATE, END_DATE, AD_CODE

## PAYROLL.PAY_MASTER
Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SALARY_ON_CARD_SWIPE | CHAR(1) | Y |  |
| MONTH_DAYS | NUMBER(2) | Y |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| ACTUAL_PERFORMED_DAYS | NUMBER(5) | Y |  |
| ACTUAL_WORKING_HOURS | NUMBER(5) | Y |  |
| ACTUAL_PERFORMED_HOURS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(2) | Y |  |
| SALARY_DAYS | NUMBER(2) | Y |  |
| SALARY_DAYS_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| ACTUAL_BASIC | NUMBER(20) | Y |  |
| CALC_BASIC | NUMBER(20) | Y |  |
| CALC_BASIC_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| ACTUAL_PAY_RATE | NUMBER(20,2) | Y |  |
| CALC_PAY_RATE | NUMBER(20,2) | Y |  |
| CALC_PAY_RATE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| OTHER_ALLOWANCES | NUMBER(20) | Y |  |
| ARREARS | NUMBER(20) | Y |  |
| OVERTIME_HRS | NUMBER(5) | Y |  |
| OVERTIME_AMOUNT | NUMBER(20) | Y |  |
| NO_OF_NIGHTS | NUMBER(2) | Y |  |
| NIGHTS_AMOUNT | NUMBER(20) | Y |  |
| GROSS_PAYABLE | NUMBER(20) | Y |  |
| GROSS_PAYABLE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| LOAN_DEDUCTION | NUMBER(20) | Y |  |
| OTHER_DEDUCTION | NUMBER(20) | Y |  |
| NET_PAYABLE | NUMBER(20) | Y |  |
| NET_PAYABLE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| GROUP_INSURANCE | NUMBER(20) | Y |  |
| EOBI_BASE | NUMBER(20) | Y |  |
| ESSI_BASE | NUMBER(20) | Y |  |
| EOBI_PAYABLE | NUMBER(20) | Y |  |
| ESSI_PAYABLE | NUMBER(20) | Y |  |
| ECESS_BASE | NUMBER(20) | Y |  |
| ECESS_PAYABLE | NUMBER(20) | Y |  |
| P_FUND_AMOUNT | NUMBER(22,2) | Y |  |
| P_FUND_LOAN | NUMBER(22,2) | Y |  |
| POSTED | CHAR(1) | Y |  |
| PRACTICE_INCOME | NUMBER(10,2) default 0 | Y |  |
| PRACTICE_INCOME_TAX | NUMBER(10,2) default 0 | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| CURRENCY_ID | VARCHAR2(3) | Y |  |
| CURRENCY_EXCHANGE_RATE | NUMBER(10,2) default 0.00 | Y |  |
| DAILY_WAGER | CHAR(1) | Y |  |
| FIXED_ALLOWANCES | NUMBER(7) default 0 | Y |  |
| INCOME_TAX | NUMBER(7) default 0 | Y |  |
| EOBI_EMPLOYEE | NUMBER(20,2) | Y |  |
| DAILY_RATE | NUMBER(4) | Y |  |
| P_FUND_BALANCE | NUMBER(20) | Y |  |
| ACTUAL_MONTH_DAYS | NUMBER(2) | Y |  |
| BRANCH_ID | VARCHAR2(3) | Y |  |
| BANK_ID | VARCHAR2(6) | Y |  |
| PAYMENT_MODE | CHAR(1) | Y |  |
| BANK_ACCOUNT_NO | VARCHAR2(50) | Y |  |
| COST_CENTRE_ID | CHAR(10) | Y |  |
| LOAN_DEDUCTION_PI | NUMBER(20,2) | Y |  |
| LOAN_DEDUCTION_PENDING | NUMBER(20,2) | Y |  |
| CALCULATED_P_FUND_AMOUNT | NUMBER(20,2) | Y |  |
| CALCULATED | CHAR(1) | Y |  |
| PI_BEFORE_DED | NUMBER(20,2) | Y |  |
| ATT_START_DATE | DATE | Y |  |
| ATT_END_DATE | DATE | Y |  |
| PREV_UNPAID_LEAVES | NUMBER(5) | Y |  |
| GL_SETUP_CODE | CHAR(3) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| FIXED_ALLOWANCES_ON_CARD_SWIPE | NUMBER(7) | Y |  |
| SHORT_WORKING_HOUR | NUMBER(5,2) | Y |  |
| OTHER_ALLOWANCES_ON_CARD_SWIPE | NUMBER(20) | Y |  |
| ONLINE_ACCOUNT | CHAR(1) default 'N' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| REIMBURSEMENT | NUMBER(20) | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOGIN_LOCATION_ID | VARCHAR2(3) | Y |  |
| IBAN | VARCHAR2(68) | Y |  |

- **PK** `PK_PAY_MASTER`: MRNO, START_DATE, END_DATE
- **FK** `FK_PAY_MASTER_1`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **FK** `FK_PAY_MASTER_2`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_PAY_MASTER_3`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_PAY_MASTER_4`: (CURRENCY_ID) -> DEFINITIONS.CURRENCY(CURRENCY_ID) [disabled]
- **Triggers**: `PAY_MASTER_DEL` (after delete), `PAY_MASTER_INS` (before insert), `PAY_MASTER_UPD` (before update)

## PAYROLL.PAY_ALLOWANCE_DEDUCTION
Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| ACTUAL_AMOUNT | NUMBER(20,2) | Y |  |
| CALC_AMOUNT | NUMBER(20,2) | Y |  |
| CALC_AMOUNT_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| CALC_AMOUNT_GUARANTEE | NUMBER(10) | Y |  |
| PENDING_AMOUNT | NUMBER(20,2) | Y |  |
| DED_FROM_PI | NUMBER(20,2) | Y |  |
| ATT_START_DATE | DATE | Y |  |
| ATT_END_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PAY_ALLOWANCE_DEDUCTION`: MRNO, START_DATE, END_DATE, AD_CODE
- **FK** `FK_PAY_ALLOWANCE_DED`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **FK** `FK_PAY_ALLOWANCE_DEDUCTION_2`: (MRNO, START_DATE, END_DATE) -> PAYROLL.PAY_MASTER(MRNO, START_DATE, END_DATE)
- **Triggers**: `PAY_ALLOWANCE_DEDUCTION_DEL` (after delete), `PAY_ALLOWANCE_DEDUCTION_INS` (before insert), `PAY_ALLOWANCE_DEDUCTION_UPD` (before update)

## PAYROLL.PAY_MASTER_TEST
Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SALARY_ON_CARD_SWIPE | CHAR(1) | Y |  |
| MONTH_DAYS | NUMBER(2) | Y |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| ACTUAL_PERFORMED_DAYS | NUMBER(5) | Y |  |
| ACTUAL_WORKING_HOURS | NUMBER(5) | Y |  |
| ACTUAL_PERFORMED_HOURS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(2) | Y |  |
| SALARY_DAYS | NUMBER(2) | Y |  |
| SALARY_DAYS_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| ACTUAL_BASIC | NUMBER(20) | Y |  |
| CALC_BASIC | NUMBER(20) | Y |  |
| CALC_BASIC_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| ACTUAL_PAY_RATE | NUMBER(20,2) | Y |  |
| CALC_PAY_RATE | NUMBER(20,2) | Y |  |
| CALC_PAY_RATE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| OTHER_ALLOWANCES | NUMBER(20) | Y |  |
| ARREARS | NUMBER(20) | Y |  |
| OVERTIME_HRS | NUMBER(5) | Y |  |
| OVERTIME_AMOUNT | NUMBER(20) | Y |  |
| NO_OF_NIGHTS | NUMBER(2) | Y |  |
| NIGHTS_AMOUNT | NUMBER(20) | Y |  |
| GROSS_PAYABLE | NUMBER(20) | Y |  |
| GROSS_PAYABLE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| LOAN_DEDUCTION | NUMBER(20) | Y |  |
| OTHER_DEDUCTION | NUMBER(20) | Y |  |
| NET_PAYABLE | NUMBER(20) | Y |  |
| NET_PAYABLE_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| GROUP_INSURANCE | NUMBER(20) | Y |  |
| EOBI_BASE | NUMBER(20) | Y |  |
| ESSI_BASE | NUMBER(20) | Y |  |
| EOBI_PAYABLE | NUMBER(20) | Y |  |
| ESSI_PAYABLE | NUMBER(20) | Y |  |
| ECESS_BASE | NUMBER(20) | Y |  |
| ECESS_PAYABLE | NUMBER(20) | Y |  |
| P_FUND_AMOUNT | NUMBER(20) | Y |  |
| P_FUND_LOAN | NUMBER(20) | Y |  |
| POSTED | CHAR(1) | Y |  |
| PRACTICE_INCOME | NUMBER(10,2) | Y |  |
| PRACTICE_INCOME_TAX | NUMBER(10,2) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| CURRENCY_ID | VARCHAR2(3) | Y |  |
| CURRENCY_EXCHANGE_RATE | NUMBER(10,2) | Y |  |
| DAILY_WAGER | CHAR(1) | Y |  |
| FIXED_ALLOWANCES | NUMBER(7) | Y |  |
| INCOME_TAX | NUMBER(7) | Y |  |
| EOBI_EMPLOYEE | NUMBER(20,2) | Y |  |
| DAILY_RATE | NUMBER(4) | Y |  |
| P_FUND_BALANCE | NUMBER(20) | Y |  |
| ACTUAL_MONTH_DAYS | NUMBER(2) | Y |  |
| BRANCH_ID | VARCHAR2(3) | Y |  |
| BANK_ID | VARCHAR2(6) | Y |  |
| PAYMENT_MODE | CHAR(1) | Y |  |
| BANK_ACCOUNT_NO | VARCHAR2(50) | Y |  |
| COST_CENTRE_ID | CHAR(10) | Y |  |
| LOAN_DEDUCTION_PI | NUMBER(20,2) | Y |  |
| LOAN_DEDUCTION_PENDING | NUMBER(20,2) | Y |  |
| CALCULATED_P_FUND_AMOUNT | NUMBER(20,2) | Y |  |
| CALCULATED | CHAR(1) | Y |  |
| PI_BEFORE_DED | NUMBER(20,2) | Y |  |
| ATT_START_DATE | DATE | Y |  |
| ATT_END_DATE | DATE | Y |  |
| PREV_UNPAID_LEAVES | NUMBER(5) | Y |  |
| GL_SETUP_CODE | CHAR(3) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| FIXED_ALLOWANCES_ON_CARD_SWIPE | NUMBER(7) | Y |  |
| SHORT_WORKING_HOUR | NUMBER(5,2) | Y |  |
| OTHER_ALLOWANCES_ON_CARD_SWIPE | NUMBER(20) | Y |  |
| ONLINE_ACCOUNT | CHAR(1) default 'N' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| REIMBURSEMENT | NUMBER(20) | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOGIN_LOCATION_ID | VARCHAR2(3) | Y |  |
| IBAN | VARCHAR2(68) | Y |  |

- **PK** `PK_PAY_MASTER_TEST`: MRNO, START_DATE, END_DATE
- **FK** `FK_PAY_MASTER_TEST_1`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]

## PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST
Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| ACTUAL_AMOUNT | NUMBER(20,2) | Y |  |
| CALC_AMOUNT | NUMBER(20,2) | Y |  |
| CALC_AMOUNT_ON_CARD_SWIPE | NUMBER(20) | Y | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| CALC_AMOUNT_GUARANTEE | NUMBER(10) | Y |  |
| PENDING_AMOUNT | NUMBER(20,2) | Y |  |
| DED_FROM_PI | NUMBER(20,2) | Y |  |
| ATT_START_DATE | DATE | Y |  |
| ATT_END_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PAY_ALL_DED_TEST`: MRNO, START_DATE, END_DATE, AD_CODE
- **FK** `FK_PAY_ALLOWANCE_DED_TEST`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **FK** `FK_PAY_ALL_DED_TEST_2`: (MRNO, START_DATE, END_DATE) -> PAYROLL.PAY_MASTER_TEST(MRNO, START_DATE, END_DATE)

## PAYROLL.PAY_ARREAR

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| ARREAR_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PAY_ARREAR`: MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE
- **Triggers**: `PAY_ARREAR_DEL` (after delete), `PAY_ARREAR_INS` (before insert), `PAY_ARREAR_UPD` (before update)

## PAYROLL.PAY_ARREAR_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| ARREAR_CODE | CHAR(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_ARREAR_TEST`: MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE

## PAYROLL.PAY_DAILY_AD_TEST

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_START_DATE | DATE | N |  |
| PAY_END_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| DAY | DATE | N |  |
| ATTENDANCE_BASED | CHAR(1) | N |  |
| INCLUDE_IN_GROSS | CHAR(1) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| PAYMENT_FACTOR | NUMBER(5,2) | Y |  |
| AD_NATURE_TYPE_ID | VARCHAR2(3) | N |  |
| AD_TYPE | CHAR(1) | N |  |
| ACTUAL_SALARY | NUMBER(20,4) | Y |  |
| CALC_SALARY | NUMBER(20,4) | Y |  |
| CALC_SALARY_ON_CARD_SWIPE | NUMBER(20,4) | Y |  |
| ACTUAL_PERFORM_TIME | NUMBER(9) | Y |  |
| ACTUAL_WORKING_TIME | NUMBER(9) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_DAILY_AD_TEST`: MRNO, PAY_START_DATE, PAY_END_DATE, AD_CODE, DAY

## PAYROLL.PAY_DAILY_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| DAY | DATE | N |  |
| AMOUNT | NUMBER(10,2) | Y |  |

- **PK** `PK_PAY_DAILY_TEMP`: MRNO, AD_CODE, DAY

## PAYROLL.PAY_DAILY_TEMP_UNPAID

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| DAY | DATE | N |  |
| AMOUNT | NUMBER(10,2) | Y |  |
| ATTENDANCE_BASED | CHAR(1) | Y |  |
| INCLUDE_IN_GROSS | CHAR(1) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| PAYMENT_FACTOR | NUMBER(5,2) | Y |  |
| AD_NATURE_TYPE_ID | VARCHAR2(3) | Y |  |
| AD_TYPE | CHAR(1) | Y |  |
| AMOUNT_ON_CARD_SWIPE | NUMBER(20,2) | Y |  |
| ACTUAL_AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_PAY_DAILY_TEMP_UNPAID`: MRNO, AD_CODE, DAY

## PAYROLL.PAY_DR_FEE

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| GUARANTEE_MONEY | NUMBER(10,2) | Y |  |
| DR_FEE_GROSS | NUMBER(10,2) | Y |  |
| DR_FEE_NET | NUMBER(10,2) | Y |  |
| DR_FEE_CALC | NUMBER(10,2) | Y |  |
| DR_FEE_WAIVED | NUMBER(10,2) | Y |  |
| PREV_REALIZED | NUMBER(10,2) | Y |  |
| CURR_REALIZED | NUMBER(10,2) | Y |  |
| SESSION_PAYMENT | NUMBER(10,2) | Y |  |
| GROSS_PAYABLE | NUMBER(10,2) | Y |  |
| INCOME_TAX | NUMBER(10,2) | Y |  |
| NET_PAYABLE | NUMBER(10,2) | Y |  |


## PAYROLL.PAY_EXCEPTIONAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTUAL_BASIC | NUMBER(20,2) | Y |  |
| ACTUAL_PAY_RATE | NUMBER(20,2) | Y |  |
| DAILY_WAGER | CHAR(1) | Y |  |
| DAILY_RATE | NUMBER(4) | Y |  |

_No standard audit columns._


## PAYROLL.PAY_ITAX_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| SETUP_TAX | NUMBER(12,2) | Y |  |
| PROPOSED_TAX | NUMBER(12,2) | Y |  |
| DEDUCTED_TAX | NUMBER(12,2) | Y |  |
| EXPECTED_YEARLY_TAXABLE_AMOUNT | NUMBER(12,2) | Y |  |
| EXPECTED_YEARLY_TAX | NUMBER(12,2) | Y |  |
| YEARLY_PAID_TAX | NUMBER(12,2) | Y |  |
| SELECT_FLAG | CHAR(1) default 'N' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| AD_ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| AD_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOG | VARCHAR2(4000) | Y |  |
| ACTUAL_PROPOSED_TAX | NUMBER(12,2) | Y |  |
| MONTH_REMAINING | NUMBER(2) | Y |  |
| CURRENCY_EXCHANGE_RATE | NUMBER(10,2) | Y |  |
| LAST_MON_END_DATE | DATE | Y |  |
| UNPAID_LEAVE_AMOUNT | NUMBER(12,2) | Y |  |
| TAX_PAID_SALARY | NUMBER(12,2) | Y |  |
| TAX_PAID_DIRECT | NUMBER(12,2) | Y |  |
| TAX_PAID_ADJUST | NUMBER(12,2) | Y |  |
| UNDISTRIBUTED_TAX | NUMBER(12,2) | Y |  |
| SLAB_PERCENTAGE | NUMBER(5,2) | Y |  |
| DAYS_PERCENTAGE | NUMBER(5,2) default 100 | Y |  |
| MANUAL_CALCULATION | VARCHAR2(1) default 'N' | Y |  |
| REVISED_TAXABLE_INCOME | NUMBER(12,2) | Y |  |
| REVISED_TAX_AMOUNT | NUMBER(12,2) | Y |  |
| REVISED_CURR_MON_TAX | NUMBER(12,2) | Y |  |
| CURR_MON_GROSS_PAYABLE | NUMBER(12,2) | Y |  |
| CURR_MON_PF | NUMBER(12,2) | Y |  |
| CURR_MON_PF_TAXABLE | NUMBER(12,2) | Y |  |
| PREVIOUS_PROPOSED_TAX | NUMBER(12,2) | Y |  |
| PREVIOUS_ACTUAL_PROPOSED_TAX | NUMBER(12,2) | Y |  |
| TOTAL_INCOME_TODATE | NUMBER(12,2) | Y |  |
| TAX_PAID_TILL_MONTH | NUMBER(12,2) | Y |  |
| TAX_ADJUSTED | NUMBER(12,2) | Y |  |
| REVISED_CURR_MON_GROSS_WITH_PF | NUMBER(12,2) | Y |  |
| REVISED_YTD_PAID_INCOME | NUMBER(12,2) | Y |  |
| REVISED_YTD_PAID_TAX | NUMBER(12,2) | Y |  |
| TAX_ADJUSTED_MONTHLY | NUMBER(12,2) | Y |  |
| REV_CURR_MON_NC_TAX | NUMBER(12,2) | Y |  |
| TAX_TO_BEPAID_TILL_MONTH | NUMBER(12,2) | Y |  |

- **PK** `PK_PAY_ITAX_DETAIL`: MRNO, START_DATE, END_DATE
- **FK** `FK_PAY_ITAX_DETAIL`: (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) -> PAYROLL.DEF_ALLOWANCE_DEDUCTION(AD_CODE, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **Triggers**: `PAY_ITAX_DETAIL_DEL` (after delete), `PAY_ITAX_DETAIL_INS` (before insert), `PAY_ITAX_DETAIL_UPD` (before update)

## PAYROLL.PAY_ITAX_DETAIL_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | N |  |
| SETUP_TAX | NUMBER(12,2) | Y |  |
| PROPOSED_TAX | NUMBER(12,2) | Y |  |
| DEDUCTED_TAX | NUMBER(12,2) | Y |  |
| EXPECTED_YEARLY_TAXABLE_AMOUNT | NUMBER(12,2) | Y |  |
| EXPECTED_YEARLY_TAX | NUMBER(12,2) | Y |  |
| YEARLY_PAID_TAX | NUMBER(12,2) | Y |  |
| SELECT_FLAG | CHAR(1) | Y |  |


## PAYROLL.PAY_ITAX_DTL_TMP

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(500) | Y |  |
| DESIGNATION | VARCHAR2(1000) | Y |  |
| DEPARTMENT_ID | VARCHAR2(25) | Y |  |
| DEPARTMENT | VARCHAR2(1000) | Y |  |
| GRADE | VARCHAR2(60) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| CURRENT_AMOUNT | NUMBER(20,2) | Y |  |
| PREVIOUS_AMOUNT | NUMBER(20,2) | Y |  |
| DIFFERENCE | NUMBER(20,2) | Y |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |
| CRITERIA_ID | NUMBER(2) | N |  |

_No standard audit columns._

- **PK** `PK_PAY_ITAX_DTL_TMP`: CRITERIA_ID, START_DATE, END_DATE, PAYROLL_LOCATION_ID, MRNO

## PAYROLL.PAY_ITAX_INCOME_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| PARAMETER | VARCHAR2(32) | N |  |
| AMOUNT | NUMBER(15,3) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_ITAX_INCOME_DETAIL`: MRNO, START_DATE, END_DATE, PARAMETER

## PAYROLL.PAY_LEAVES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| OPENING_BALANCE | NUMBER(3) | Y |  |
| AVAILED | NUMBER(3) | Y |  |
| CLOSING_BALANCE | NUMBER(3) | Y |  |

- **PK** `PK_PAY_LEAVES`: MRNO, START_DATE, END_DATE, LEAVE_TYPE_ID
- **FK** `FK_PAY_LEAVES_1`: (LEAVE_TYPE_ID) -> HRD.LEAVE_TYPE(LEAVE_TYPE_ID) [disabled]
- **FK** `FK_PAY_LEAVES_2`: (MRNO, START_DATE, END_DATE) -> PAYROLL.PAY_MASTER(MRNO, START_DATE, END_DATE) [disabled]
- **Triggers**: `PAY_LEAVES_DEL` (after delete), `PAY_LEAVES_INS` (before insert), `PAY_LEAVES_UPD` (before update)

## PAYROLL.PAY_PF_VOUCHER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| VOUCHER_TYPE_CONTRIBUTION | VARCHAR2(5) | Y |  |
| END_DATE | DATE | N |  |
| VOUCHER_NO_CONTRIBUTION | CHAR(13) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| EMPLOYEE_CONTRIBUTION | NUMBER(20,2) | Y |  |
| EMPLOYER_CONTRIBUTION | NUMBER(20,2) | Y |  |
| VOUCHER_TYPE_LOAN_ADJUST | VARCHAR2(5) | Y |  |
| VOUCHER_NO_LOAN_ADJUST | VARCHAR2(13) | Y |  |

- **PK** `PK_PAY_PF_VOUCHER`: START_DATE, END_DATE, MRNO
- **FK** `FK_PAY_PF_VOUCHER_1`: (VOUCHER_TYPE_CONTRIBUTION, VOUCHER_NO_CONTRIBUTION) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_PAY_PF_VOUCHER_2`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_PAY_PF_VOUCHER_3`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **Triggers**: `PAY_PF_VOUCHER_DEL` (after delete), `PAY_PF_VOUCHER_INS` (before insert), `PAY_PF_VOUCHER_UPD` (before update)

## PAYROLL.PAY_REPORT_FILE

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_CODE | NUMBER(2) | N |  |
| REPORT_TITLE | VARCHAR2(255) | Y |  |
| SUMMARY_DETAIL | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PAY_REPORT_FILE`: REPORT_CODE

## PAYROLL.PAY_REPORT_FORMAT
This table is used to define groups of different allowances / deductions, this group will be used into formatting salary sheets

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_GROUP_CODE | CHAR(3) | N | PK-Self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Group description (House Rent, Utilities, Income Tax, Others etc.) |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short description of Group, to be displayed onto Salary Sheet |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |

- **PK** `PK_DEF_ALLOW_DEDUCT_GROUP`: AD_GROUP_CODE
- **CHECK** `CK_DEF_ALLOW_DEDUCT_GROUP_1`: ACTIVE IN ('Y', 'N'

## PAYROLL.PAY_REPORT_ROUTING

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_CODE | NUMBER(2) | N |  |
| AD_CODE | CHAR(3) | N |  |
| AD_GROUP_CODE | CHAR(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PAY_REPORT_ROUTING`: REPORT_CODE, AD_CODE, AD_GROUP_CODE
- **FK** `FK_PAY_REPORT_ROUTING_1`: (REPORT_CODE) -> PAYROLL.PAY_REPORT_FILE(REPORT_CODE)
- **FK** `FK_PAY_REPORT_ROUTING_2`: (AD_GROUP_CODE) -> PAYROLL.PAY_REPORT_FORMAT(AD_GROUP_CODE)

## PAYROLL.PAY_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(7) | N | Unique serial number |
| MRNO | VARCHAR2(14) | N | Save employee code |
| DATE_FROM | DATE | N | Save salary month start date |
| DATE_TO | DATE | N | Save salary month end date |
| STATUS | CHAR(1) | N | 'S' = 'Stop Payment' |
| DISCIPLINARY_REASON_ID | VARCHAR2(6) | Y |  |
| USER_COMMENTS | VARCHAR2(2000) | Y | Save user remarks |

- **PK** `PK_PAY_STATUS`: SERIAL_NO
- **UK** `UK_PAY_STATUS_1`: MRNO, DATE_FROM, DATE_TO
- **CHECK** `CHK_PAY_STATUS_01`: STATUS IN ('N','S'
- **Triggers**: `PAY_STATUS_DEL` (after delete), `PAY_STATUS_INS` (before insert), `PAY_STATUS_UPD` (before update)

## PAYROLL.PAY_TMP_BANK

| Column | Type | Null | Comment |
|---|---|---|---|
| BRANCH_ID | VARCHAR2(3) | Y |  |
| BRANCH_DESCRIPTION | VARCHAR2(255) | Y |  |
| BANK_ID | VARCHAR2(6) | Y |  |
| BANK_DESCRIPTION | VARCHAR2(255) | Y |  |
| SELECTED | CHAR(1) | Y |  |
| USERID | VARCHAR2(30) | Y |  |
| PARENT_BRANCH_ID | VARCHAR2(3) | Y |  |


## PAYROLL.PAY_TMP_EMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(255) | Y |  |
| SELECT_FLAG | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| LOG | VARCHAR2(4000) | Y |  |
| ERROR_TEXT | VARCHAR2(4000) | Y |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOGIN_LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._


## PAYROLL.PAY_TMP_MPA

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_CODE | CHAR(3) | Y |  |
| GROUP_NAME | VARCHAR2(255) | Y |  |
| DIV_CODE | CHAR(3) | Y |  |
| DIV_NAME | VARCHAR2(255) | Y |  |
| DEPT_CODE | CHAR(3) | Y |  |
| DEPT_NAME | VARCHAR2(255) | Y |  |
| NO_OF_EMP_1 | NUMBER(5) | Y |  |
| SALARY_1 | NUMBER(20,2) | Y |  |
| NO_OF_EMP_2 | NUMBER(5) | Y |  |
| SALARY_2 | NUMBER(20,2) | Y |  |
| NO_OF_EMP_3 | NUMBER(5) | Y |  |
| SALARY_3 | NUMBER(20,2) | Y |  |
| NO_OF_EMP_CHANGE | NUMBER(5) | Y |  |
| SALARY_CHANGE | NUMBER(20,2) | Y |  |
| NO_OF_EMP_0 | NUMBER(5) | Y |  |
| SALARY_0 | NUMBER(20,2) | Y |  |
| NO_OF_EMP_CHANGE2 | NUMBER(5) | Y |  |
| SALARY_CHANGE2 | NUMBER(20,2) | Y |  |


## PAYROLL.PAY_TMP_REPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(183) | Y |  |
| COST_CENTRE_ID | CHAR(10) | Y |  |
| COST_CENTRE_DESCRIPTION | VARCHAR2(255) | Y |  |
| RATE_OF_PAY | NUMBER(20,2) | Y |  |
| G_BASIC | NUMBER(20,2) | Y |  |
| G_HOUSE_RENT | NUMBER(20,2) | Y |  |
| G_UTILITIES | NUMBER(20,2) | Y |  |
| G_CONVEYANCE | NUMBER(20,2) | Y |  |
| G_OTHER_ALLOWANCES | NUMBER(20,2) | Y |  |
| G_OVERTIME | NUMBER(20,2) | Y |  |
| G_NIGHT_ALLOWANCE | NUMBER(20,2) | Y |  |
| G_TOTAL_GROSS | NUMBER(20,2) | Y |  |
| D_PROVIDENT_FUND | NUMBER(20,2) | Y |  |
| D_INCOME_TAX | NUMBER(20,2) | Y |  |
| D_LOAN | NUMBER(20,2) | Y |  |
| D_OTHER_DEDUCTIONS | NUMBER(20,2) | Y |  |
| D_TOTAL_DEDUCTIONS | NUMBER(20,2) | Y |  |
| NET_SALARY | NUMBER(20,2) | Y |  |
| PAYMENT_MODE | CHAR(1) | Y |  |
| SALARY_DAYS | NUMBER(2) | Y |  |
| CURRENCY_EXCHANGE_RATE | NUMBER(10,2) | Y |  |
| CURRENCY_ID | VARCHAR2(3) | Y |  |
| PRACTICE_INCOME_TAX | NUMBER(10,2) default 0 | Y |  |
| PRACTICE_INCOME | NUMBER(10,2) | Y |  |
| GL_SETUP_CODE | CHAR(3) | Y |  |
| PI_BEFORE_DED | NUMBER(20,2) default 0 | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| D_ELECTRICITY_BILL | NUMBER(20,2) | Y |  |
| D_GAS_BILL | NUMBER(20,2) | Y |  |


## PAYROLL.PAY_VOUCHER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(2) | N |  |
| PF_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| PF_VOUCHER_NO | CHAR(13) | Y |  |
| GL_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| GL_VOUCHER_NO | CHAR(13) | Y |  |
| LOAN_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| LOAN_VOUCHER_NO | VARCHAR2(13) | Y |  |
| PF_CANCELLED | CHAR(1) default 'N' | Y |  |
| GL_CANCELLED | CHAR(1) default 'N' | Y |  |
| LOAN_CANCELLED | CHAR(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| GP_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| GP_VOUCHER_NO | CHAR(13) | Y |  |
| GP_CANCELLED | CHAR(1) default 'N' | Y |  |
| CP_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CP_VOUCHER_NO | CHAR(13) | Y |  |
| CP_CANCELLED | CHAR(1) default 'N' | Y |  |
| PAY_VOUCHER_TYPE | VARCHAR2(2) | Y | i.e. GP, PF, CP, GL, LN |
| VOUCHER_TYPE | VARCHAR2(5) | Y | Voucher type for any pay voucher type |
| VOUCHER_NO | CHAR(13) | Y | Voucher No for any pay voucher type |
| CANCELLED | CHAR(1) default 'N' | Y | Voucher cancellation status for any pay voucher type |

- **PK** `PK_PAY_VOUCHER`: START_DATE, END_DATE, SERIAL_NO, LOCATION_ID
- **FK** `FK_PAY_VOUCHER_1`: (PF_VOUCHER_TYPE, PF_VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_PAY_VOUCHER_2`: (GL_VOUCHER_TYPE, GL_VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_PAY_VOUCHER_3`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **CHECK** `CK_PAY_VOUCHER_1`: PF_CANCELLED IN ('Y','N'
- **CHECK** `CK_PAY_VOUCHER_2`: GL_CANCELLED IN ('Y','N'
- **CHECK** `CK_PAY_VOUCHER_3`: LOAN_CANCELLED IN ('Y','N'
- **Triggers**: `PAY_VOUCHER_DEL` (after delete), `PAY_VOUCHER_INS` (before insert), `PAY_VOUCHER_UPD` (before update)

## PAYROLL.PAY_VOUCHER_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| VOUCHER_TYPE | VARCHAR2(5) | N |  |
| VOUCHER_NO | CHAR(13) | N |  |
| TRANS_DATE | DATE | Y |  |

- **PK** `PK_PAY_VOUCHER_MASTER`: START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO
- **FK** `FK_PAY_VOUCHER_MASTER_1`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **FK** `FK_PAY_VOUCHER_MASTER_2`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **Triggers**: `PAY_VOUCHER_MASTER_DEL` (after delete), `PAY_VOUCHER_MASTER_INS` (before insert), `PAY_VOUCHER_MASTER_UPD` (before update)

## PAYROLL.PAY_VOUCHER_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| VOUCHER_TYPE | VARCHAR2(5) | N |  |
| VOUCHER_NO | CHAR(13) | N |  |
| COA_CODE | VARCHAR2(100) | N |  |
| LEDGER_TYPE_CODE | NUMBER(4) | N |  |
| SUB_LDGR_ITEM_CODE | VARCHAR2(18) | N |  |
| DR_AMOUNT | NUMBER(20,2) | Y |  |
| CR_AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_PAY_VOUCHER_DETAIL`: START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO, COA_CODE, LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE
- **FK** `FK_PAY_VOUCHER_DETAIL_1`: (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) -> FINANCE.GL_SUB_LEDGERS(LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **FK** `FK_PAY_VOUCHER_DETAIL_2`: (COA_CODE) -> FINANCE.GL_COA(COA_CODE)
- **FK** `FK_PAY_VOUCHER_DETAIL_3`: (START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO) -> PAYROLL.PAY_VOUCHER_MASTER(START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO)
- **Triggers**: `PAY_VOUCHER_DETAIL_DEL` (after delete), `PAY_VOUCHER_DETAIL_INS` (before insert), `PAY_VOUCHER_DETAIL_UPD` (before update)

## PAYROLL.PAY_VOUCHER_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| SERIAL_NO | NUMBER(3) | Y |  |
| START_DATE | DATE | N |  |
| STATIC_DESCRIPTION | VARCHAR2(20) | Y |  |
| END_DATE | DATE | N |  |
| AD_CODE | CHAR(3) | Y |  |
| LOAN_CODE | CHAR(3) | Y |  |
| COA_CODE_DR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |
| COA_CODE_CR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y |  |
| TRANSACTION_TYPE | CHAR(1) default 'O' | Y |  |
| STATIC_TYPE | CHAR(1) default 'G' | Y |  |
| DR_AMOUNT | NUMBER(20,2) | Y |  |
| CR_AMOUNT | NUMBER(20,2) | Y |  |
| ARREAR_CODE | CHAR(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **CHECK** `CK_PAY_VOUCHER_TEMP_1`: TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O'

## PAYROLL.PAY_VOUCHER_TMP

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_START_DATE | DATE | N |  |
| PAY_END_DATE | DATE | N |  |
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| SERIAL_NO | NUMBER | N |  |
| PAY_VOUCHER_SETUP_ID | VARCHAR2(3) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| COA_CODE_DR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |
| COA_CODE_CR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| AD_CODE | CHAR(3) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_VOUCHER_TMP`: PAY_START_DATE, PAY_END_DATE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO

## PAYROLL.PENDING_LOANS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| LOAN_NO | VARCHAR2(12) | Y |  |
| REFUND_NO | VARCHAR2(12) | Y |  |
| LOAN_AMOUNT | NUMBER(20,2) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |
| LOAN_PENDING | NUMBER(20,2) | Y |  |
| LOAN_LOCATION_ID | VARCHAR2(3) | Y |  |


## PAYROLL.PF_FINAL_SETTLEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SR_NO | NUMBER(2) | N | Auto Increment |
| TRANS_DATE | DATE | Y |  |
| TYPE | VARCHAR2(2) | Y | FS -> Final Settlement, PW -> Permanent Widthdrawal |
| RACK_RATE | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | CHAR(13) | Y |  |
| CANCELLED_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CANCELLED_VOUCHER_NO | VARCHAR2(13) | Y |  |
| STATUS_ID | VARCHAR2(3) default '100' | N |  |
| PF_TYPE | VARCHAR2(2) | Y | PF, CP, GP |
| GROSS_PAYABLE | NUMBER(20,2) | Y |  |
| NO_OF_MONTHS | NUMBER(2) | Y |  |

- **PK** `PK_PF_FINAL_SETTLEMENT`: MRNO, SR_NO
- **Triggers**: `PF_FINAL_SETTLEMENT_DEL` (after delete), `PF_FINAL_SETTLEMENT_INS` (before insert), `PF_FINAL_SETTLEMENT_UPD` (before update)

## PAYROLL.PROCESS_INCREMENT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| INCREMENT_CODE | CHAR(3) | N |  |
| INCREMENT_DATE | DATE | N |  |
| EFFECTIVE_DATE | DATE | Y |  |
| ADD_ARREARS | CHAR(1) | Y |  |
| INCR_SLAB_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_PROCESS_INCREMENT_MASTER`: PROCESS_ID
- **FK** `FK_PROCESS_INCREMENT_MASTER_1`: (INCREMENT_CODE) -> PAYROLL.DEF_INCREMENT_TYPE(INCREMENT_CODE) [disabled]
- **Triggers**: `PROCESS_INCREMENT_MASTER_DEL` (after delete), `PROCESS_INCREMENT_MASTER_INS` (before insert), `PROCESS_INCREMENT_MASTER_UPD` (before update)

## PAYROLL.PROCESS_MEMBERS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| STAGE_NO | NUMBER(2) | Y |  |
| INCREMENT_AMOUNT | NUMBER(20,2) | Y |  |
| LAST_INCREMENT_DATE | DATE | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| JOINING_DATE | DATE | Y |  |
| SELECT_FLAG | CHAR(1) | Y |  |
| PROCESS_LOG | VARCHAR2(1000) | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| POSTED_BY | VARCHAR2(14) | Y |  |
| POSTED_DATE | DATE | Y |  |
| VERIFIED | CHAR(1) default 'N' | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| INCR_SLAB_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_PROCESS_MEMBERS`: PROCESS_ID, MRNO
- **Triggers**: `PROCESS_MEMBERS_DEL` (after delete), `PROCESS_MEMBERS_INS` (before insert), `PROCESS_MEMBERS_UPD` (before update)

## PAYROLL.PROFIT_VOUCHER_TMP

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| SERIAL_NO | NUMBER(2) | N |  |
| DETAIL_SERIAL_NO | NUMBER | N |  |
| PAY_VOUCHER_SETUP_ID | VARCHAR2(3) | Y |  |
| PAY_VOUCHER_SETUP_SRNO | NUMBER(2) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| LOAN_NO | VARCHAR2(12) | Y |  |
| PRINCIPAL_AMOUNT | NUMBER(20,2) | Y |  |
| NO_OF_MONTH | NUMBER(2) | Y |  |
| COA_CODE_DR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_DR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |
| COA_CODE_CR | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE_CR | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE_CR | VARCHAR2(18) | Y |  |
| AMOUNT | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| COA_STATUS | CHAR(1) | Y |  |

_No standard audit columns._

- **PK** `PK_PROFIT_VOUCHER_TMP`: YEAR_CODE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO, DETAIL_SERIAL_NO

## PAYROLL.REP_LOAN_LEDGER
This is a temporary table to generate trial balances / ledgers of advances and loans

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y | Employee Code |
| NAME | VARCHAR2(183) | Y | Employee Name |
| LOAN_CODE | CHAR(3) | Y | Lon type |
| SELECT_FLAG | CHAR(1) | Y | To be used into Form Block (For selection un-selection of employees) |
| OPENING_BALANCE | NUMBER(20,2) | Y | Opening balance of FROM_DATE into Report parameter |
| TOTAL_DEDUCTION | NUMBER(20,2) | Y | Total deduction till TO_DATE into Report parameter |
| CLOSING_BALANCE | NUMBER(20,2) | Y | Opening balance  - Total deduction |


## PAYROLL.RPT_SALARY_TAX_LINE_ITEM

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| LINE_ITEM | VARCHAR2(200) | N |  |
| ROW_TYPE | VARCHAR2(10) | N |  |
| SOURCE | VARCHAR2(50) | Y |  |
| SUBTOTAL_OF | VARCHAR2(200) | Y |  |
| SIGN | NUMBER default 1 | Y |  |
| COMMENTS | VARCHAR2(500) | Y |  |
| AD_CODE | VARCHAR2(50) | Y |  |
| PAYMENT_SOURCE | VARCHAR2(500) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| PRECESSED_CHECK | CHAR(1) | Y |  |

- **Triggers**: `RPT_SALARY_TAX_LINE_ITEM_DEL` (after delete), `RPT_SALARY_TAX_LINE_ITEM_INS` (before insert), `RPT_SALARY_TAX_LINE_ITEM_UPD` (before update)

## PAYROLL.R_COST_TO_COMPANY_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| CALENDER_YEAR | NUMBER(4) | Y |  |
| TAX_YEAR | NUMBER(4) | N |  |
| MONTH | VARCHAR2(41) | Y |  |
| NAME | VARCHAR2(4000) | Y |  |
| CNIC_NO | VARCHAR2(4000) | Y |  |
| DOB | DATE | Y |  |
| EMP_TYPE | CHAR(1) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| MANAGER_MRNO | VARCHAR2(14) | Y |  |
| IBAN | VARCHAR2(64) | Y |  |
| DEPARTMENT_CODE | CHAR(3) | N |  |
| DEPARTMENT_DESCRIPTION | VARCHAR2(255) | Y |  |
| COST_CENTER | CHAR(3) | N |  |
| COST_CENTER_DESCRIPTION | VARCHAR2(255) | Y |  |
| DIVISION_CODE | CHAR(3) | N |  |
| DIVISION_DESCRIPTION | VARCHAR2(255) | N |  |
| LOCATION_CODE | VARCHAR2(3) | N |  |
| LOCATION_DESCRIPTION | VARCHAR2(150) | Y |  |
| CURRENCY | VARCHAR2(60) | Y |  |
| MONTH_DAYS | NUMBER(2) | Y |  |
| PREVIOUS_UNPAID_LEAVE_COUNT | NUMBER(5) | Y |  |
| CURRENT_UNPAID_LEAVE_COUNT | NUMBER(2) | Y |  |
| EMPLOYMENT_TYPE | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | N |  |
| DATE_OF_JOINING | DATE | Y |  |
| CONTRACTUAL_END_DATE | DATE | Y |  |
| CONFIRMATION_DATE | DATE | Y |  |
| DATE_OF_LEAVING | DATE | Y |  |
| GRADE | VARCHAR2(60) | Y |  |
| DESIGNATION | VARCHAR2(4000) | Y |  |
| CURRENT_GROSS | NUMBER(20,2) | Y |  |
| SUPERVISOR_MRNO | VARCHAR2(4000) | Y |  |
| SUPERVISOR_DESIGNATION | VARCHAR2(4000) | Y |  |
| HOD | VARCHAR2(14) | Y |  |
| HOD_DESIGNATION | VARCHAR2(4000) | Y |  |
| BASIC_SALARY | NUMBER | Y |  |
| HOUSE_RENT | NUMBER | Y |  |
| UTILITIES | NUMBER | Y |  |
| GROSS_SALARY | NUMBER | Y |  |
| PI | NUMBER | Y |  |
| CONVEYANCE_ALLOWANCE | NUMBER | Y |  |
| OVERLOAD_PAYMENT | NUMBER | Y |  |
| TRANSPORT_ALLOWANCE_DOCTORS | NUMBER | Y |  |
| SPECIAL_ALLOWANCE | NUMBER | Y |  |
| ON_CALL_ALLOWANCE_DOCTORS | NUMBER | Y |  |
| TRANSPORT_ALLOWANCE_NURSES | NUMBER | Y |  |
| OTHER_ALLOWANCE | NUMBER | Y |  |
| SPECIAL_PAY | NUMBER | Y |  |
| MERIT_PAY | NUMBER | Y |  |
| DOCTORS | NUMBER | Y |  |
| OTHERS | NUMBER | Y |  |
| TOTAL_ALLOWANCE | NUMBER | Y |  |
| OVERTIME | NUMBER(20) | Y |  |
| SHIFT_ALLOWANCE_NIGHT | NUMBER(20) | Y |  |
| ARREARS | NUMBER(20) | Y |  |
| TOTAL | NUMBER | Y |  |
| LFA | NUMBER | Y |  |
| LSA | NUMBER | Y |  |
| TRAVEL | NUMBER | Y |  |
| MEDICAL | NUMBER | Y |  |
| VEHICLE_MAINTENANCE | NUMBER | Y |  |
| BENEFITS_TOTAL | NUMBER | Y |  |
| INCOME_TAX | NUMBER | Y |  |
| EOBI | NUMBER | Y |  |
| PROFESSIONAL_TAX | NUMBER | Y |  |
| PROVIDENT_FUND | NUMBER | Y |  |
| COLLEGIALITY_FUND | NUMBER | Y |  |
| PFUND_LOAN | NUMBER | Y |  |
| FOOD | NUMBER | Y |  |
| TRAVEL_ADVANCE | NUMBER | Y |  |
| SALARY_ADVANCE | NUMBER | Y |  |
| MEDICAL_BILLS | NUMBER | Y |  |
| TELEPHONE | NUMBER | Y |  |
| DONATION_SADQA | NUMBER | Y |  |
| ZAKAT | NUMBER | Y |  |
| CAR_LOAN | NUMBER | Y |  |
| CAFE_BILL | NUMBER | Y |  |
| LAUNDRY | NUMBER | Y |  |
| GIFT_SHOP | NUMBER | Y |  |
| INDEMNITY_PATIENT | NUMBER | Y |  |
| SCRAP | NUMBER | Y |  |
| STORES | NUMBER | Y |  |
| HOUSE_ACCOMMODATION | NUMBER | Y |  |
| KARACHI_PROJECT_DONATION | NUMBER | Y |  |
| OTHER_DEDUCTIONS | NUMBER | Y |  |
| TAX_TOTAL | NUMBER | Y |  |
| E_YEARLY_TAXABLE_AMOUNT | NUMBER | Y |  |
| PAID_COA_WITHIN_MONTH | NUMBER | Y |  |
| EXPECTED_YEARLY_TAX | NUMBER(12,2) | Y |  |
| EXPECTED_YEARLY_TBL | NUMBER(12,2) | Y |  |
| YEARLY_PAID_TAX | NUMBER | Y |  |
| REMAINING_TAX | NUMBER | Y |  |
| MONTH_REMAINING | NUMBER(2) | Y |  |
| ACTUAL_PROPOSED_TAX | NUMBER(12,2) | Y |  |
| PAID_PRACTICE_INCOME | NUMBER | Y |  |
| PAID_GROSS_PAY | NUMBER | Y |  |
| PAID_LFA_AMOUNT | NUMBER | Y |  |
| PAID_OTHER_ALLOWANCES | NUMBER | Y |  |
| PAID_ARREARS | NUMBER | Y |  |
| PAID_COA_BASED_EXPENSE | NUMBER | Y |  |
| PAID_EXPENSES | NUMBER | Y |  |
| PAID_NIGHTS | NUMBER | Y |  |
| PAID_OVERTIME | NUMBER | Y |  |
| DIRECT_PAID_EXPENSES | NUMBER | Y |  |
| EXPECTED_GROSS_PAY | NUMBER | Y |  |
| EXPECTED_OTHER_ALLOWANCES | NUMBER | Y |  |
| EXPECTED_PRACTICE_INCOME | NUMBER | Y |  |
| EXPECTED_TRANS_ALLOWANCES | NUMBER | Y |  |
| EXPECTED_LFA_AMOUNT | NUMBER | Y |  |
| EXPECTED_ARREARS | NUMBER | Y |  |
| EXPECTED_ANNUALLY_TAX | NUMBER | Y |  |
| OTHER_TAXABLE_AMOUNT | NUMBER | Y |  |
| TAXABLE_PF_AMOUNT | NUMBER | Y |  |
| CURRENT_MONTH_NIGHTS | NUMBER | Y |  |
| CURRENT_MONTH_OVERTIME | NUMBER | Y |  |
| TAX_PAID_IN_SALARY | NUMBER | Y |  |
| TAX_PAID_DIRECTLY | NUMBER | Y |  |
| TAX_ADJUSTMENTS | NUMBER | Y |  |
| CURRENCY_EXCHANGE_RATE | NUMBER | Y |  |
| LAST_MONTH_END_DATE | DATE | Y |  |
| UNPAID_LEAVE_AMOUNT | NUMBER | Y |  |
| UNDISTRIBUTED_TAX | NUMBER | Y |  |
| MONTHLY_SALARY | NUMBER(20) | Y |  |
| REIMBURSEMENT | NUMBER(20) | Y |  |
| PRACTICE_INCOME | NUMBER(20) | Y |  |
| NET_PAYABLE | NUMBER(20) | Y |  |
| NET_SALARY_BANK_CREDIT | NUMBER(20) | Y |  |
| DUTY_DAYS | NUMBER(2) | Y |  |
| DUTY_LOCATION | VARCHAR2(60) | Y |  |
| DEPARTMENT_SECTION | VARCHAR2(60) | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| COA_CODE_DR | VARCHAR2(100) | Y |  |
| SUB_LDGR_ITEM_CODE_DR | VARCHAR2(18) | Y |  |

_No standard audit columns._

- **PK** `PK_COST_TO_COMPANY`: START_DATE, END_DATE, MRNO

## PAYROLL.SALARY_ELEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | Y |  |
| SRNO | NUMBER | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| AMOUNT | NUMBER(10) | Y |  |

_No standard audit columns._


## PAYROLL.SALARY_SLABS

| Column | Type | Null | Comment |
|---|---|---|---|
| FROM_RANGE | NUMBER(6) | Y |  |
| TO_RANGE | NUMBER(6) | Y |  |
| INCR_PERCENT | NUMBER(5,2) | Y |  |
| NO_OF_EMP | NUMBER(4) | Y |  |
| TOTAL_SALARY | NUMBER(8) | Y |  |
| TOT_INC | NUMBER | Y |  |
| INCR_AGE | NUMBER | Y |  |


## PAYROLL.TARGET_TABLE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| AD_CODE | CHAR(3) | Y |  |
| AD_VALUE | NUMBER | Y |  |


## PAYROLL.TAX_CALCULATION_LOG

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(30) | Y |  |
| NEW_ANNUAL_TAXABLE_INCOME | NUMBER(18,2) | Y |  |
| NEW_ANNUAL_TAX | NUMBER(18,2) | Y |  |
| TAXABLE_GROSS | NUMBER(18,2) | Y |  |
| TAXABLE_PF | NUMBER(18,2) | Y |  |
| NEW_MONTH_TAXABLE_PF | NUMBER(18,2) | Y |  |
| TOT_INCOME_LAST_MON | NUMBER(18,2) | Y |  |
| TAX_TO_BE_PAID_TILL_MONTH | NUMBER(18,2) | Y |  |
| TAX_PAID_TILL_MONTH | NUMBER(18,2) | Y |  |
| MONTHLY_AMOUNT_ADJ | NUMBER(18,2) | Y |  |
| CURRENT_DEDUCTION | NUMBER(18,2) | Y |  |
| LOG_DATE | DATE default SYSDATE | Y |  |

_No standard audit columns._


## PAYROLL.TEMP_INCREMENT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| INCREMENT_DATE | DATE | N |  |
| INCREMENT_CODE | CHAR(3) | N |  |
| EFFECTIVE_DATE | DATE | Y |  |
| INCR_AMOUNT | NUMBER(20,2) | Y |  |
| INCR_PERCENT | NUMBER(6,2) | Y |  |
| SETUP_BASIC | NUMBER(20,2) | Y |  |
| SETUP_GROSS | NUMBER(20,2) | Y |  |
| PROPOSED_BASIC | NUMBER(20,2) | Y |  |
| PROPOSED_GROSS | NUMBER(20,2) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ARREAR_PAID | CHAR(1) | Y |  |

- **PK** `PK_TEMP_INCREMENT_MASTER`: PROCESS_ID, MRNO
- **Triggers**: `TEMP_INCREMENT_MASTER_DEL` (after delete), `TEMP_INCREMENT_MASTER_INS` (before insert), `TEMP_INCREMENT_MASTER_UPD` (before update)

## PAYROLL.TEMP_INCREMENT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| ENTRY_TYPE | CHAR(1) | Y |  |
| SETUP_AMOUNT | NUMBER(20,2) | Y |  |
| PROPOSED_AMOUNT | NUMBER(20,2) | Y |  |
| PROPOSED_CHANGE | CHAR(1) | Y |  |
| CALCULATION_TYPE | VARCHAR2(2) | Y |  |
| CALC_PERCENT | NUMBER(5,2) | Y |  |
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_TEMP_INCREMENT_DETAIL`: PROCESS_ID, MRNO, AD_CODE
- **FK** `FK_TEMP_INCREMENT_DETAIL_2`: (PROCESS_ID, MRNO) -> PAYROLL.TEMP_INCREMENT_MASTER(PROCESS_ID, MRNO) [disabled]
- **Triggers**: `TEMP_INCREMENT_DETAIL_DEL` (after delete), `TEMP_INCREMENT_DETAIL_INS` (before insert), `TEMP_INCREMENT_DETAIL_UPD` (before update)

## PAYROLL.TEMP_INDIVIDUAL_ITAX

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| YEAR_CODE | CHAR(4) | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| GROSS | NUMBER(20,2) | Y |  |
| OTHER_ALLOW | NUMBER(20,2) | Y |  |
| TAX_PAID | NUMBER(20,2) | Y |  |
| PI_TAX_PAID | NUMBER(20,2) | Y |  |
| PRACTICE_INCOME | NUMBER(20,2) | Y |  |


## PAYROLL.TEMP_ITAX

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| EMP_NAME | VARCHAR2(255) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| ADDRESS | VARCHAR2(1000) | Y |  |
| CNIC | VARCHAR2(20) | Y |  |
| NTN | VARCHAR2(20) | Y |  |
| GENDER | VARCHAR2(20) | Y |  |
| DUTY_CITY | VARCHAR2(255) | Y |  |
| SALARY_MONTH | NUMBER(2) | Y |  |
| GROSS_PAYABLE | NUMBER(12) | Y |  |
| LFA | NUMBER(12) | Y |  |
| PI | NUMBER(12) | Y |  |
| TAXABLE_PF | NUMBER(12) | Y |  |
| TAXABLE_AMOUNT | NUMBER(12) | Y |  |
| ANNUAL_TAX | NUMBER(12) | Y |  |
| ITAX | NUMBER(12) | Y |  |
| PI_TAX | NUMBER(12) | Y |  |
| TOTAL_PAID_TAX | NUMBER(12) | Y |  |
| TAX_CREDIT | NUMBER(12) | Y |  |
| TAX_WITHHELD | NUMBER(12) | Y |  |
| LFA_PAID | NUMBER(12) | Y |  |
| USERID | VARCHAR2(30) | Y |  |
| EMP_TYPE | CHAR(1) | Y |  |
| SALARY_EXP | NUMBER(12) | Y | TAXABLE EXPENSES |
| SURCHARGE_TAX | NUMBER(12) | Y |  |
| TAX_SLAB | NUMBER(5,2) | Y |  |
| MONTHLY_TAXABLE_PF | NUMBER(12) | Y |  |
| NON_SALARY_EXP | NUMBER(12) | Y | NON TAXABLE EXPENSES |
| TAX_DIRECT_PAID_EXP | NUMBER(12) | Y |  |
| SALARY_FS | NUMBER(12) | Y |  |
| LEAVE_ENCASHMENT | NUMBER(12) | Y |  |
| CASH_AWARDS | NUMBER(12) | Y |  |
| INCENTIVES | NUMBER(12) | Y |  |


## PAYROLL.TEMP_SALARY_RECONCILE_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| IN_DEPARTMENT | VARCHAR2(400) | Y |  |
| OUT_DEPARTMENT | VARCHAR2(400) | Y |  |
| START_DATE | DATE | Y |  |
| CURRENT_SALARY | NUMBER | Y |  |
| PREVIOUS_SALARY | NUMBER | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| EVENT | VARCHAR2(400) | Y |  |

_No standard audit columns._


## PAYROLL.TMP_LOAN_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(255) | Y |  |
| DEPARTMENT | VARCHAR2(255) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| SALARY | NUMBER(12,2) | Y |  |
| LOAN_TYPE | VARCHAR2(255) | Y |  |
| OPENING_BALANCE | NUMBER(12,2) | Y |  |
| RECEIVED_AMOUNT | NUMBER(12,2) | Y |  |
| RETURNED_AMOUNT | NUMBER(12,2) | Y |  |
| CLOSING_BALANCE | NUMBER(12,2) | Y |  |
| USERID | VARCHAR2(30) | Y |  |
| LOAN_CODE | CHAR(3) | Y |  |
| TRANS_DATE | DATE | Y |  |
| LOAN_NO | VARCHAR2(12) | Y |  |
| STOP_AUTO_DEDUCTION | CHAR(1) | Y |  |
| NO_OF_INSTALLMENTS | NUMBER(12,2) | Y |  |
| MONTHLY_INSTALLMENT | NUMBER(12,2) | Y |  |
| STOP_AUTO_DEDUCTION_TILL | DATE | Y |  |


## PAYROLL.TRAVEL_ADVANCE_APPROVAL

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_NO | NUMBER | N |  |
| APPROVAL_STATUS | VARCHAR2(1) | Y | P = Pending, A = Approved, R = Rejected |
| APPROVAL_DATE | DATE | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_TRAVEL_ADVANCE_APPROVAL`: REQUEST_NO
- **Triggers**: `TRAVEL_ADVANCE_APPROVAL_DEL` (after delete), `TRAVEL_ADVANCE_APPROVAL_INS` (before insert), `TRAVEL_ADVANCE_APPROVAL_PQ` (before insert or update), `TRAVEL_ADVANCE_APPROVAL_UPD` (before update)

