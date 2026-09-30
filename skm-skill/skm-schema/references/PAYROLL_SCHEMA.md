# PAYROLL schema - reference


payroll (pay, loans, expenses, employee pay components, performance income and related processing).

**Counts:** 183 tables, 5 views, 78 packages, 52 standalone procedures/functions, 1 sequences, 117 synonyms.

## Conventions
- Standard audit columns on nearly every table: `USER_ID, TERMINAL, TRN_DATE, ORIGINAL_USER_ID, ORIGINAL_TERMINAL, ORIGINAL_TRN_DATE`.
- Multi-location columns: `ORG_ID, ZON_ID, LOC_ID, WS_SYNC_DATE` (location where the record was first created).
- Insert/update/delete triggers fill the audit columns and copy deleted rows to audit tables through `SYN_*` synonyms - do not set audit columns manually.
- Flag columns are usually `CHAR/VARCHAR2(1)` with `'Y'/'N'` (e.g. `ACTIVE`).
- Cross-schema FKs from this schema point to: FINANCE (25 FKs), DEFINITIONS (23 FKs), HRD (14 FKs), BILLING (2 FKs).

## Rules
- Use only tables/columns that exist in the Tables part below; never guess names.
- Qualify objects with the schema (`PAYROLL.TABLE`).
- For joins across schemas use the skill `skm-schema` and the other schema reference file.

## Table index
- `ACTUAL_PI`
- `AD_EXCEPTIONAL`
- `DEF_AD_GROUP`
- `DEF_ALLOWANCE_DEDUCTION` - This table is used to define different types of allowances / deductions which are used in salary processing. It also describes different formulas to calculate allowances and deductions
- `ALLOWANCE_DEDUCTION_DETAIL`
- `ALLOWANCE_DEDUCTION_SETUP`
- `DEF_ARREAR`
- `ARREAR_DETAIL`
- `ARREAR_EXCEPTIONAL`
- `BASE_TABLE`
- `CBR_DATA_FILE`
- `CHANGE_SALARY_ALLOW`
- `CM_DEF_ADMIN_GROUP`
- `CM_BILL_MASTER`
- `CM_DEF_CONNECTION`
- `CM_CONNECTION_REQUEST`
- `CM_BILL_DETAIL`
- `CM_CONNECTION_REQ_DOCUMENT`
- `CM_CONNECTION_TRANSACTIONS`
- `CM_DEF_ADMIN_GROUP_DTL`
- `CM_INVOICES`
- `DEF_AD_CHART`
- `DEF_AD_CHART_DETAIL`
- `DEF_AD_CONSTANT`
- `DEF_AD_NATURE_TYPE`
- `DEF_AD_SETUP` - This table is used to location wise define def_allowances_deduction.
- `DEF_AD_SETUP_DC` - This table is used to define designation category wise ad setup.
- `DEF_AD_SETUP_PT` - This table is used to define patient type group wise ad setup.
- `DEF_AD_SETUP_UNPAID_LT`
- `DEF_EMP_JOB` - This table is used to define organizational hierarchy of employees
- `DEF_GL_SETUP_MASTER` - This table is used to define different setups for payroll jornal voucher
- `DEF_INCOME_TAX` - This table is used to define different setups for income tax calculation according to govt. policy
- `DEF_EMP_FINANCIAL` - This table is used to define financial parameters of empoyee which are used to entertain different financial activities
- `DEF_EXPENSE`
- `DEF_EXPENSE_CONSTANT`
- `DEF_EXPENSE_DETAIL`
- `DEF_EXPENSE_DETAIL_SLAB`
- `DEF_EXPENSE_TAXABLE_ACC`
- `DEF_EXPENSE_WORKFLOW`
- `DEF_FINANCIAL_SETUP` - This table is used to define different formulas and rules applied to Govt. and corporate. It contains only one record.
- `DEF_FS_ELEMENT`
- `DEF_FS_ELEMENT_DETAIL`
- `DEF_FS_SALARY_ELEMENTS`
- `DEF_FS_WORKFLOW_Q`
- `DEF_GL_SETUP_DETAIL` - This table is used to define different setups for automatic payroll jornal voucher
- `DEF_GL_SETUP_DETAIL_FS` - This table is used to define different setups for automatic payroll final settlement jornal voucher
- `DEF_GL_VOUCHER` - This table is used to define different setups for payroll jornal voucher
- `DEF_PERCENTAGE_SETUP`
- `DEF_GRADE_WISE_PERCENTAGE`
- `DEF_INCREMENT_TYPE` - This table is used to define different types of increments such as Annual, promotional etc.
- `DEF_ITAX_ADJUSTMENT`
- `PAY_FINANCIAL_YEAR`
- `DEF_ITAX_DETAIL_AD`
- `DEF_ITAX_MR_SLAB`
- `DEF_ITAX_SLAB`
- `DEF_LETTER_TYPE` - This table is used to define different letter types
- `DEF_LETTER_TEMPLATE` - This table is used to define different letter templates to be issued to employees such as joining, experience etc.
- `DEF_LIABILITY`
- `DEF_LOAN_INTEREST_RATE`
- `DEF_LOAN_TYPE` - This table is used to define different types of loan such as Advance against salary, Car loan, house loan etc.
- `DEF_LOAN_TYPE_CONSTANT`
- `DEF_MONTH_CHANGE`
- `DEF_PAYROLL_LOCATION`
- `DEF_PAYROLL_WORKFLOW`
- `DEF_PAYSCALE`
- `DEF_PAYSCALE_DETAIL`
- `DEF_PAY_VOUCHER_LOCATION`
- `DEF_PAY_VOUCHER_TYPE`
- `DEF_PAY_VOUCHER_SETUP`
- `DEF_PAY_VOUCHER_SETUP_DTL`
- `DEF_PF_SETUP`
- `DEF_PROJECT`
- `DEF_SCHEDULE_WORKFLOW_CC`
- `DEF_SETUP_CONSTANT`
- `DEF_SETUP`
- `DEF_TAX_AMOUNT_OTHER_THAN_SAL`
- `EMPLOYEE_INCOME_DETAIL`
- `EMPLOYEE_INCOME_DETAIL_FQ`
- `EMP_ALLOWANCE_DEDUCTION` - This table is used to link employees with different types of allowances and deductions
- `EMP_ALLOWANCE_DEDUCTION_DETAIL`
- `EMP_AWARDS`
- `EMP_AWARD_PAYMENT`
- `EMP_EXPENSE`
- `EMP_EXPENSE_LIST`
- `EMP_EXPENSE_LIST_DTL`
- `EMP_EXP_DET_PROJECT`
- `EMP_INCREMENT_MASTER`
- `EMP_INCREMENT_DETAIL`
- `EMP_ITAX_ADJUSTMENT`
- `EMP_ITAX_ADJUSTMENT_DTL`
- `EMP_ITAX_ADJUSTMENT_DTL_M`
- `EMP_ITAX_ADJUSTMENT_MONTHLY`
- `EMP_LIABILITY`
- `EMP_NEW_SAL`
- `EMP_PAYMENT`
- `EMP_TAX_AMOUNT_OTHER_THAN_SAL`
- `EXPENSE_CLAIM_MASTER`
- `EXPENSE_CLAIM_DETAIL`
- `EXPENSE_CLAIM_DOCUMENT`
- `EXPENSE_CLAIM_HIERARCHY`
- `EXPENSE_CLAIM_HIERARCHY_ORG`
- `EXPENSE_CLAIM_PROJECT`
- `EXPENSE_CLAIM_WORKFLOW`
- `EXPENSE_CLAIM_WORKFLOW_Q`
- `FINAL_SETTLEMENT`
- `FINAL_SETTLEMENT_ELEMENT`
- `FINAL_SETTLEMENT_WF`
- `FINAL_SETTLEMENT_WF_Q`
- `GENERIC_REPORT_MASTER`
- `GENERIC_REPORT_FIELD`
- `GENERIC_REPORT_FIELD_DTL`
- `HOLD_ORDER`
- `ITAX_PAYMENT_DETAIL`
- `ITAX_PAYMENT_MASTER`
- `LEAVE_DAYS_TEST`
- `LOAN_INSTALLMENT_DETAIL`
- `LOAN_PAYMENT_INTEREST`
- `LOAN_PAYMENT_MASTER` - This table is used to entertain opening balances and transactions of staff advances
- `LOAN_PAYMENT_MASTER_N` - This table is used to entertain opening balances and transactions of staff advances
- `LOAN_PAYMENT_MASTER_TEST`
- `LOAN_REFUND_MASTER` - This table is used to entertain transactions of refunds advances or deductions of advances against salary
- `LOAN_REFUND_DETAIL` - This table is used to entertain transactions of refunds advances or deductions of advances against salary
- `LOAN_REFUND_MASTER_N` - This table is used to entertain transactions of refunds advances or deductions of advances against salary
- `LOAN_REFUND_DETAIL_N` - This table is used to entertain transactions of refunds advances or deductions of advances against salary
- `LOAN_REFUND_MASTER_TEST`
- `LOAN_REFUND_DETAIL_TEST`
- `LOAN_REFUND_OPENING`
- `MANUAL_MONTH_MASTER`
- `MANUAL_PAY_MASTER`
- `MANUAL_ALLOWANCE_DEDUCTION`
- `MONTH_CHANGE_REQUEST`
- `MONTH_CHANGE_REQUEST_TEMP`
- `PAY_AD_BALANCE`
- `PAY_AD_BALANCE_TEST`
- `PAY_MASTER` - Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.
- `PAY_ALLOWANCE_DEDUCTION` - Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.
- `PAY_MASTER_TEST` - Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.
- `PAY_ALLOWANCE_DEDUCTION_TEST` - Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.
- `PAY_ARREAR`
- `PAY_ARREAR_TEST`
- `PAY_DAILY_AD_TEST`
- `PAY_DAILY_TEMP`
- `PAY_DAILY_TEMP_UNPAID`
- `PAY_DR_FEE`
- `PAY_EXCEPTIONAL`
- `PAY_ITAX_DETAIL`
- `PAY_ITAX_DETAIL_HISTORY`
- `PAY_ITAX_DTL_TMP`
- `PAY_ITAX_INCOME_DETAIL`
- `PAY_LEAVES`
- `PAY_PF_VOUCHER`
- `PAY_REPORT_FILE`
- `PAY_REPORT_FORMAT` - This table is used to define groups of different allowances / deductions, this group will be used into formatting salary sheets
- `PAY_REPORT_ROUTING`
- `PAY_STATUS`
- `PAY_TMP_BANK`
- `PAY_TMP_EMP`
- `PAY_TMP_MPA`
- `PAY_TMP_REPORT`
- `PAY_VOUCHER`
- `PAY_VOUCHER_MASTER`
- `PAY_VOUCHER_DETAIL`
- `PAY_VOUCHER_TEMP`
- `PAY_VOUCHER_TMP`
- `PENDING_LOANS`
- `PF_FINAL_SETTLEMENT`
- `PROCESS_INCREMENT_MASTER`
- `PROCESS_MEMBERS`
- `PROFIT_VOUCHER_TMP`
- `REP_LOAN_LEDGER` - This is a temporary table to generate trial balances / ledgers of advances and loans
- `RPT_SALARY_TAX_LINE_ITEM`
- `R_COST_TO_COMPANY_TEMP`
- `SALARY_ELEMENT`
- `SALARY_SLABS`
- `TARGET_TABLE`
- `TAX_CALCULATION_LOG`
- `TEMP_INCREMENT_MASTER`
- `TEMP_INCREMENT_DETAIL`
- `TEMP_INDIVIDUAL_ITAX`
- `TEMP_ITAX`
- `TEMP_SALARY_RECONCILE_DATA`
- `TMP_LOAN_SUMMARY`
- `TRAVEL_ADVANCE_APPROVAL`


# PART: Tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

### PAYROLL.ACTUAL_PI

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


### PAYROLL.AD_EXCEPTIONAL

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


### PAYROLL.DEF_AD_GROUP

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
- **CHECK** `CK_DAG_ACTIVE`: ACTIVE IN ('N','Y')
- **CHECK** `CK_DEF_AD_GROUP_1`: AD_TYPE IN ('A','D')
- **CHECK** `CK_DEF_AD_GROUP_NN`: AD_TYPE IS NOT NULL
- **Triggers**: `DEF_AD_GROUP_CEA` (before insert or update or delete), `DEF_AD_GROUP_DEL` (after delete), `DEF_AD_GROUP_INS` (before insert), `DEF_AD_GROUP_UPD` (before update), `TRG_WS_KZL_DN_VB_Q` (after insert or update or delete)

### PAYROLL.DEF_ALLOWANCE_DEDUCTION
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
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_1`: AD_TYPE IN ('A', 'D')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_10`: TAXABLE_ANNUALLY IN ('Y', 'N')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_2`: CALC_TYPE IN ('A', 'O')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_3`: DED_TYPE IN ('I','P','B','M','C','E','O','R')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_4`: VALUE_TYPE IN ('A', 'P')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_5`: INCLUDE_IN_GROSS IN ('Y', 'N')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_6`: ACTIVE IN ('Y', 'N')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_7`: OT_CALC_BASE IN ('G', 'B')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_8`: PRACTICE_INCOME IN ('Y', 'N', 'G')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_9`: ENTRY_TYPE IN ('S','T')
- **CHECK** `CK_DEF_ALLOWANCE_DEDUCTION_NN`: AD_GROUP_CODE IS NOT NULL
- **Triggers**: `DEF_ALLOWANCE_DEDUCTION_DEL` (after delete), `DEF_ALLOWANCE_DEDUCTION_INS` (before insert), `DEF_ALLOWANCE_DEDUCTION_UPD` (before update)

### PAYROLL.ALLOWANCE_DEDUCTION_DETAIL

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

### PAYROLL.ALLOWANCE_DEDUCTION_SETUP

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

### PAYROLL.DEF_ARREAR

| Column | Type | Null | Comment |
|---|---|---|---|
| ARREAR_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| AD_TYPE | CHAR(1) default 'A' | Y |  |
| CBR_AMOUNT_CODE | VARCHAR2(4) | Y |  |

- **PK** `PK_DEF_ARREAR`: ARREAR_CODE
- **CHECK** `CK_DEF_ARREAR_1`: ACTIVE IN ('Y', 'N')
- **CHECK** `CK_DEF_ARREAR_2`: AD_TYPE IN ('A','D')
- **Triggers**: `DEF_ARREAR_CEA` (before insert or update or delete), `DEF_ARREAR_DEL` (after delete), `DEF_ARREAR_INS` (before insert), `DEF_ARREAR_UPD` (before update), `TRG_WS_WVB_PD_FA_Q` (after insert or update or delete)

### PAYROLL.ARREAR_DETAIL

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

### PAYROLL.ARREAR_EXCEPTIONAL

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

### PAYROLL.BASE_TABLE

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


### PAYROLL.CBR_DATA_FILE

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


### PAYROLL.CHANGE_SALARY_ALLOW

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


### PAYROLL.CM_DEF_ADMIN_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N |  |
| NAME | VARCHAR2(250) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `DEF_ADMIN_GROUP_PK`: ADMIN_GROUP_ID
- **Triggers**: `CM_DEF_ADMIN_GROUP_DEL` (after delete), `CM_DEF_ADMIN_GROUP_INS` (before insert), `CM_DEF_ADMIN_GROUP_UPD` (before update)

### PAYROLL.CM_BILL_MASTER

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

### PAYROLL.CM_DEF_CONNECTION

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

### PAYROLL.CM_CONNECTION_REQUEST

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

### PAYROLL.CM_BILL_DETAIL

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

### PAYROLL.CM_CONNECTION_REQ_DOCUMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(13) | N |  |
| REQUEST_ID | VARCHAR2(10) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CM_CONNECTION_REQ_DOCUMENT`: DOCUMENT_ID
- **FK** `FK_CM_CONNECTION_REQ_DOCUMENT`: (REQUEST_ID) -> PAYROLL.CM_CONNECTION_REQUEST(REQUEST_ID)
- **Triggers**: `CM_CONNECTION_REQ_DOCUMENT_DEL` (after delete), `CM_CONNECTION_REQ_DOCUMENT_INS` (before insert), `CM_CONNECTION_REQ_DOCUMENT_UPD` (before update)

### PAYROLL.CM_CONNECTION_TRANSACTIONS

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

### PAYROLL.CM_DEF_ADMIN_GROUP_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_GROUP_ID | VARCHAR2(2) | N |  |
| ADMIN_MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_ADMIN_GROUP_DTL`: ADMIN_GROUP_ID, ADMIN_MRNO
- **Triggers**: `CM_DEF_ADMIN_GROUP_DTL_DEL` (after delete), `CM_DEF_ADMIN_GROUP_DTL_INS` (before insert), `CM_DEF_ADMIN_GROUP_DTL_UPD` (before update)

### PAYROLL.CM_INVOICES

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_ID | VARCHAR2(12) | N |  |
| CONTACT_NUMBER | VARCHAR2(40) | N |  |
| BILL_AMOUNT | NUMBER(10,2) | Y |  |
| BILL_MONTH_ID | VARCHAR2(12) | Y |  |
| BILL_REQUEST_ID | VARCHAR2(10) | Y |  |

- **PK** `PK_CM_INVOICES`: MONTH_ID, CONTACT_NUMBER
- **Triggers**: `CM_INVOICES_DEL` (after delete), `CM_INVOICES_INS` (before insert), `CM_INVOICES_UPD` (before update)

### PAYROLL.DEF_AD_CHART

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

### PAYROLL.DEF_AD_CHART_DETAIL

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

### PAYROLL.DEF_AD_CONSTANT

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

### PAYROLL.DEF_AD_NATURE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_NATURE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| DED_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DEF_AD_NATURE_TYPE`: AD_NATURE_TYPE_ID
- **Triggers**: `DEF_AD_NATURE_TYPE_CEA` (before insert or update or delete), `DEF_AD_NATURE_TYPE_DEL` (after delete), `DEF_AD_NATURE_TYPE_INS` (before insert), `DEF_AD_NATURE_TYPE_UPD` (before update), `TRG_WS_FHI_YZ_ST_Q` (after insert or update or delete)

### PAYROLL.DEF_AD_SETUP
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
- **CHECK** `CK_DEF_AD_SETUP_1`: TAXABLE_ANNUALLY IN ('Y', 'N')
- **CHECK** `CK_DEF_AD_SETUP_2`: ATTENDANCE_BASED IN ('A', 'O')
- **CHECK** `CK_DEF_AD_SETUP_4`: INCLUDE_IN_GROSS IN ('Y', 'N')
- **CHECK** `CK_DEF_AD_SETUP_5`: ACTIVE IN ('Y', 'N')
- **CHECK** `CK_DEF_AD_SETUP_6`: ENTRY_TYPE IN ('S','T')
- **CHECK** `CK_DEF_AD_SETUP_NN`: AD_GROUP_CODE IS NOT NULL
- **Triggers**: `DEF_AD_SETUP_CEA` (before insert or update or delete), `DEF_AD_SETUP_DEL` (after delete), `DEF_AD_SETUP_INS` (before insert), `DEF_AD_SETUP_UPD` (before update), `TRG_WS_WKA_UZ_BE_Q` (after insert or update or delete)

### PAYROLL.DEF_AD_SETUP_DC
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

### PAYROLL.DEF_AD_SETUP_PT
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

### PAYROLL.DEF_AD_SETUP_UNPAID_LT

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

### PAYROLL.DEF_EMP_JOB
This table is used to define organizational hierarchy of employees

| Column | Type | Null | Comment |
|---|---|---|---|
| JOB_CODE | VARCHAR2(18) | N | PK - Auto generated field |
| DESCRIPTION | VARCHAR2(255) | N | Name of Job |

- **PK** `PK_DEF_EMP_JOB`: JOB_CODE
- **Triggers**: `DEF_EMP_JOB_DEL` (after delete), `DEF_EMP_JOB_INS` (before insert), `DEF_EMP_JOB_UPD` (before update)

### PAYROLL.DEF_GL_SETUP_MASTER
This table is used to define different setups for payroll jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |
| ACTIVE | CHAR(1) default 'Y' | Y | Either row is currenctly availabe for transactions or not |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_S_GL_SETUP_MASTER`: GL_SETUP_CODE
- **CHECK** `CK_S_GL_SETUP_MASTER_1`: ACTIVE IN ('Y', 'N')
- **Triggers**: `DEF_GL_SETUP_MASTER_CEA` (before insert or update or delete), `DEF_GL_SETUP_MASTER_DEL` (after delete), `DEF_GL_SETUP_MASTER_INS` (before insert), `DEF_GL_SETUP_MASTER_UPD` (before update), `TRG_WS_TTB_AI_IF_Q` (after insert or update or delete)

### PAYROLL.DEF_INCOME_TAX
This table is used to define different setups for income tax calculation according to govt. policy

| Column | Type | Null | Comment |
|---|---|---|---|
| S_ITAX_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Name of  income tax setup |

- **PK** `PK_DEF_INCOME_TAX`: S_ITAX_CODE
- **Triggers**: `DEF_INCOME_TAX_DEL` (after delete), `DEF_INCOME_TAX_INS` (before insert), `DEF_INCOME_TAX_UPD` (before update)

### PAYROLL.DEF_EMP_FINANCIAL
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
- **CHECK** `CK_DEF_EMP_FINANCIAL_1`: PAYMENT_MODE IN ('C', 'B', 'Q')
- **CHECK** `CK_DEF_EMP_FINANCIAL_2`: INCLUDE_IN_EOBI IN ('Y', 'N')
- **CHECK** `CK_DEF_EMP_FINANCIAL_3`: INCLUDE_IN_ESSI IN ('Y', 'N')
- **CHECK** `CK_DEF_EMP_FINANCIAL_4`: INCLUDE_IN_ED_CESS IN ('Y', 'N')
- **CHECK** `CK_DEF_EMP_FINANCIAL_5`: EMP_TYPE IN ('D','C','O')
- **Triggers**: `DEF_EMP_FINANCIAL_COST_CENTER_NULL` (before update), `DEF_EMP_FINANCIAL_DEL` (after delete), `DEF_EMP_FINANCIAL_INS` (before insert), `DEF_EMP_FINANCIAL_UPD` (before update)

### PAYROLL.DEF_EXPENSE

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
- **CHECK** `CK_DEF_EXPENSE_1`: ACTIVE IN ('Y', 'N')
- **CHECK** `CK_DEF_EXPENSE_2`: TYPE IN ('M','L','O','B','S')
- **CHECK** `CK_DEF_EXPENSE_3`: GROSS_BASIC IN ('G','B', 'F')
- **Triggers**: `DEF_EXPENSE_CEA` (before insert or update or delete), `DEF_EXPENSE_DEL` (after delete), `DEF_EXPENSE_INS` (before insert), `DEF_EXPENSE_UPD` (before update), `TRG_WS_BAN_JP_PG_Q` (after insert or update or delete)

### PAYROLL.DEF_EXPENSE_CONSTANT

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

### PAYROLL.DEF_EXPENSE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_TYPE_ID | VARCHAR2(3) | N |  |
| EXPENSE_CODE | CHAR(3) | Y |  |
| DESCRIPTION | VARCHAR2(64) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DAYS_REQUIRED | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEF_EXPENSE_DETAIL`: EXPENSE_TYPE_ID
- **Triggers**: `DEF_EXPENSE_DETAIL_CEA` (before insert or update or delete), `DEF_EXPENSE_DETAIL_DEL` (after delete), `DEF_EXPENSE_DETAIL_INS` (before insert), `DEF_EXPENSE_DETAIL_UPD` (before update), `TRG_WS_WFR_HS_SR_Q` (after insert or update or delete)

### PAYROLL.DEF_EXPENSE_DETAIL_SLAB

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_TYPE_ID | VARCHAR2(3) | N |  |
| SLAB_ID | VARCHAR2(12) | N |  |
| IS_DEFAULT | CHAR(1) default 'N' | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEF_EXPENSE_DETAIL_SLAB`: EXPENSE_TYPE_ID, SLAB_ID
- **FK** `FK_DEF_EXPENSE_DETAIL_SLAB1`: (EXPENSE_TYPE_ID) -> PAYROLL.DEF_EXPENSE_DETAIL(EXPENSE_TYPE_ID)
- **Triggers**: `DEF_EXPENSE_DETAIL_SLAB_CEA` (before insert or update or delete), `DEF_EXPENSE_DETAIL_SLAB_DEL` (after delete), `DEF_EXPENSE_DETAIL_SLAB_INS` (before insert), `DEF_EXPENSE_DETAIL_SLAB_UPD` (before update), `TRG_WS_PHJ_BK_HS_Q` (after insert or update or delete)

### PAYROLL.DEF_EXPENSE_TAXABLE_ACC

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

### PAYROLL.DEF_EXPENSE_WORKFLOW

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

### PAYROLL.DEF_FINANCIAL_SETUP
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
- **CHECK** `CK_DEF_FINANCIAL_SETUP_1`: OT_CALC_BASE IN ('G', 'B')
- **CHECK** `CK_DEF_FINANCIAL_SETUP_2`: NIGHT_CALC_BASE IN ('G', 'B')
- **CHECK** `CK_DEF_FINANCIAL_SETUP_3`: GRP_INS_CALC_BASE IN ('G', 'B')
- **CHECK** `CK_DEF_FINANCIAL_SETUP_4`: PF_CALC_BASE IN ('G', 'B')
- **CHECK** `CK_DEF_FINANCIAL_SETUP_5`: LFA_CALC_BASE IN ('G', 'B')
- **Triggers**: `DEF_FINANCIAL_SETUP_DEL` (after delete), `DEF_FINANCIAL_SETUP_INS` (before insert), `DEF_FINANCIAL_SETUP_UPD` (before update)

### PAYROLL.DEF_FS_ELEMENT

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

### PAYROLL.DEF_FS_ELEMENT_DETAIL

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

### PAYROLL.DEF_FS_SALARY_ELEMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ELEMENTS | VARCHAR2(8) | N |  |
| AMOUNT | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_DEF_FS_SALARY_ELEMENTS`: ELEMENTS

### PAYROLL.DEF_FS_WORKFLOW_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

_No standard audit columns._


### PAYROLL.DEF_GL_SETUP_DETAIL
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
- **CHECK** `CK_S_GL_SETUP_DETAIL_3`: TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O', 'R', 'E')
- **Triggers**: `DEF_GL_SETUP_DETAIL_DEL` (after delete), `DEF_GL_SETUP_DETAIL_INS` (before insert), `DEF_GL_SETUP_DETAIL_UPD` (before update)

### PAYROLL.DEF_GL_SETUP_DETAIL_FS
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

### PAYROLL.DEF_GL_VOUCHER
This table is used to define different setups for payroll jornal voucher

| Column | Type | Null | Comment |
|---|---|---|---|
| GL_SETUP_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |

- **PK** `PK_DEF_GL_VOUCHER_01`: GL_SETUP_CODE
- **Triggers**: `DEF_GL_VOUCHER_DEL` (after delete), `DEF_GL_VOUCHER_INS` (before insert), `DEF_GL_VOUCHER_UPD` (before update)

### PAYROLL.DEF_PERCENTAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| MINIMUM_VALUE | NUMBER(20,2) | Y |  |
| MAX_VALUE | NUMBER(20,2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_PERCENTAGE_SETUP`: PERCENTAGE_SETUP_ID
- **Triggers**: `DEF_PERCENTAGE_SETUP_CEA` (before insert or update or delete), `DEF_PERCENTAGE_SETUP_DEL` (after delete), `DEF_PERCENTAGE_SETUP_INS` (before insert), `DEF_PERCENTAGE_SETUP_UPD` (before update), `TRG_WS_FJA_HA_AY_Q` (after insert or update or delete)

### PAYROLL.DEF_GRADE_WISE_PERCENTAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| PERCENTAGE_SETUP_ID | VARCHAR2(3) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_DEF_GRADE_WISE_PERCENTAGE`: PERCENTAGE_SETUP_ID, GRADE_ID
- **FK** `FK_DEF_GRADE_PERCENT_01`: (PERCENTAGE_SETUP_ID) -> PAYROLL.DEF_PERCENTAGE_SETUP(PERCENTAGE_SETUP_ID)
- **Triggers**: `DEF_GRADE_WISE_PERCENTAGE_CEA` (before insert or update or delete), `DEF_GRADE_WISE_PERCENTAGE_DEL` (after delete), `DEF_GRADE_WISE_PERCENTAGE_INS` (before insert), `DEF_GRADE_WISE_PERCENTAGE_UPD` (before update), `TRG_WS_FLB_GV_CW_Q` (after insert or update or delete)

### PAYROLL.DEF_INCREMENT_TYPE
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
- **CHECK** `CK_DEF_INCREMENT_TYPE_1`: ACTIVE IN ('Y', 'N')
- **Triggers**: `DEF_INCREMENT_TYPE_CEA` (before insert or update or delete), `DEF_INCREMENT_TYPE_DEL` (after delete), `DEF_INCREMENT_TYPE_INS` (before insert), `DEF_INCREMENT_TYPE_UPD` (before update), `TRG_WS_LHW_SF_PB_Q` (after insert or update or delete)

### PAYROLL.DEF_ITAX_ADJUSTMENT

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
- **CHECK** `CK_DEF_ITAX_ADJUSTMENT`: ACTIVE IN ('Y','N')
- **Triggers**: `DEF_ITAX_ADJUSTMENT_CEA` (before insert or update or delete), `TRG_WS_NEL_OY_ZL_Q` (after insert or update or delete)

### PAYROLL.PAY_FINANCIAL_YEAR

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
- **CHECK** `CK_PAY_FINANCIAL_YEAR_1`: YEAR_STATUS IN ('O', 'C', 'S')
- **CHECK** `CK_PAY_FINANCIAL_YEAR_2`: CURRENT_YEAR IN ('Y', 'N')
- **CHECK** `CK_PAY_FINANCIAL_YEAR_3`: FROM_DATE = TRUNC(FROM_DATE)
- **CHECK** `CK_PAY_FINANCIAL_YEAR_4`: TO_DATE = TRUNC(TO_DATE)
- **CHECK** `CK_PAY_FINANCIAL_YEAR_5`: MARGINAL_RELIEF IN( 'Y','N')
- **CHECK** `CK_PAY_FINANCIAL_YEAR_6`: PF_EXEMPT_BASE IN ('G', 'B')
- **Triggers**: `PAY_FINANCIAL_YEAR_CEA` (before insert or update or delete), `PAY_FINANCIAL_YEAR_DEL` (after delete), `PAY_FINANCIAL_YEAR_INS` (before insert), `PAY_FINANCIAL_YEAR_UPD` (before update), `TRG_WS_WNQ_VQ_RO_Q` (after insert or update or delete)

### PAYROLL.DEF_ITAX_DETAIL_AD

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
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_001`: TAXABLE IN ('Y','N')
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_002`: GROSS_BASIC_OTHER IN ('B','G','O')
- **CHECK** `CK_DEF_ITAX_DETAIL_AD_003`: ACTIVE IN ('Y','N')
- **Triggers**: `DEF_ITAX_DETAIL_AD_CEA` (before insert or update or delete), `TRG_WS_ACE_JF_AP_Q` (after insert or update or delete)

### PAYROLL.DEF_ITAX_MR_SLAB

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

### PAYROLL.DEF_ITAX_SLAB

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

### PAYROLL.DEF_LETTER_TYPE
This table is used to define different letter types

| Column | Type | Null | Comment |
|---|---|---|---|
| LETTER_CODE | CHAR(3) | N | PK-self explainatory |
| DESCRIPTION | VARCHAR2(255) | N | Type of the letter i.e. joining, experience, termination etc. |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short name of the |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |

- **PK** `PK_DEF_LETTER_TYPE`: LETTER_CODE
- **CHECK** `CK_DEF_LETTER_TYPE_1`: ACTIVE IN ('Y', 'N')
- **Triggers**: `DEF_LETTER_TYPE_DEL` (after delete), `DEF_LETTER_TYPE_INS` (before insert), `DEF_LETTER_TYPE_UPD` (before update)

### PAYROLL.DEF_LETTER_TEMPLATE
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
- **CHECK** `CK_DEF_LETTER_TEMPLATE_1`: ACTIVE IN ('Y', 'N')

### PAYROLL.DEF_LIABILITY

| Column | Type | Null | Comment |
|---|---|---|---|
| LIABILITY_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_LIABILITY`: LIABILITY_CODE
- **Triggers**: `DEF_LIABILITY_DEL` (after delete), `DEF_LIABILITY_INS` (before insert), `DEF_LIABILITY_UPD` (before update)

### PAYROLL.DEF_LOAN_INTEREST_RATE

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

### PAYROLL.DEF_LOAN_TYPE
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
- **CHECK** `CK_DEF_LOAN_TYPE_1`: MEDICAL_OTHER IN ('M', 'O')
- **CHECK** `CK_DEF_LOAN_TYPE_2`: INSTALLMENT_ALLOW IN ('Y', 'N')
- **CHECK** `CK_DEF_LOAN_TYPE_3`: DEDUCTION_FROM_SALARY IN ('Y', 'N')
- **CHECK** `CK_DEF_LOAN_TYPE_4`: ACTIVE IN ('Y', 'N')
- **Triggers**: `DEF_LOAN_TYPE_CEA` (before insert or update or delete), `DEF_LOAN_TYPE_DEL` (after delete), `DEF_LOAN_TYPE_INS` (before insert), `DEF_LOAN_TYPE_UPD` (before update), `TRG_WS_IAP_QA_QL_Q` (after insert or update or delete)

### PAYROLL.DEF_LOAN_TYPE_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| MODULE | VARCHAR2(2) | Y | PF, GL, CP, GP |

- **PK** `PK_DEF_LOAN_CONST`: LOAN_CODE
- **Triggers**: `DEF_LOAN_TYPE_CONSTANT_CEA` (before insert or update or delete), `DEF_LOAN_TYPE_CONSTANT_DEL` (after delete), `DEF_LOAN_TYPE_CONSTANT_INS` (before insert), `DEF_LOAN_TYPE_CONSTANT_UPD` (before update), `TRG_WS_YTS_VH_XA_Q` (after insert or update or delete)

### PAYROLL.DEF_MONTH_CHANGE

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

### PAYROLL.DEF_PAYROLL_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | N | The location on which pay process is to be executed |
| EMP_LOCATION_ID | VARCHAR2(3) | N | The locations of employees which are grouped with payroll location |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEF_PAYROLL_LOCATION`: ORGANIZATION_ID, PAYROLL_LOCATION_ID, EMP_LOCATION_ID
- **UK** `UK_DEF_PAYROLL_LOCATION`: ORGANIZATION_ID, EMP_LOCATION_ID
- **Triggers**: `DEF_PAYROLL_LOCATION_CEA` (before insert or update or delete), `DEF_PAYROLL_LOCATION_DEL` (after delete), `DEF_PAYROLL_LOCATION_INS` (before insert), `DEF_PAYROLL_LOCATION_UPD` (before update), `TRG_WS_VTC_YQ_HK_Q` (after insert or update or delete)

### PAYROLL.DEF_PAYROLL_WORKFLOW

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

### PAYROLL.DEF_PAYSCALE

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

### PAYROLL.DEF_PAYSCALE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| STAGE_NO | NUMBER(2) | N |  |
| AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_DEF_PAYSCALE_DETAIL`: YEAR_CODE, GRADE_ID, STAGE_NO
- **FK** `FK_DEF_PAYSCALE_DETAIL1`: (YEAR_CODE, GRADE_ID) -> PAYROLL.DEF_PAYSCALE(YEAR_CODE, GRADE_ID) [disabled]
- **Triggers**: `DEF_PAYSCALE_DETAIL_CEA` (before insert or update or delete), `DEF_PAYSCALE_DETAIL_DEL` (after delete), `DEF_PAYSCALE_DETAIL_INS` (before insert), `DEF_PAYSCALE_DETAIL_UPD` (before update), `TRG_WS_SAN_MB_CF_Q` (after insert or update or delete)

### PAYROLL.DEF_PAY_VOUCHER_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| EMP_LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEF_PAY_VOUCHER_LOCATION`: PAY_VOUCHER_TYPE, LOCATION_ID, EMP_LOCATION_ID
- **Triggers**: `DEF_PAY_VOUCHER_LOCATION_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_LOCATION_DEL` (after delete), `DEF_PAY_VOUCHER_LOCATION_INS` (before insert), `DEF_PAY_VOUCHER_LOCATION_UPD` (before update), `TRG_WS_MYU_RJ_JI_Q` (after insert or update or delete)

### PAYROLL.DEF_PAY_VOUCHER_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PAY_VOUCHER_TYPE | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CATEGORY | VARCHAR2(2) | Y | GL or PF |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEF_PAY_VOUCHER_TYPE`: PAY_VOUCHER_TYPE
- **Triggers**: `DEF_PAY_VOUCHER_TYPE_CEA` (before insert or update or delete), `DEF_PAY_VOUCHER_TYPE_DEL` (after delete), `DEF_PAY_VOUCHER_TYPE_INS` (before insert), `DEF_PAY_VOUCHER_TYPE_UPD` (before update), `TRG_WS_GXP_UF_OU_Q` (after insert or update or delete)

### PAYROLL.DEF_PAY_VOUCHER_SETUP

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

### PAYROLL.DEF_PAY_VOUCHER_SETUP_DTL

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

### PAYROLL.DEF_PF_SETUP

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

### PAYROLL.DEF_PROJECT

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

### PAYROLL.DEF_SCHEDULE_WORKFLOW_CC

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

### PAYROLL.DEF_SETUP_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(10) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MENDATORY | CHAR(1) | Y |  |

- **PK** `PK_CONST_ID`: CONSTANT_ID
- **Triggers**: `DEF_SETUP_CONSTANT_CEA` (before insert or update or delete), `DEF_SETUP_CONSTANT_DEL` (after delete), `DEF_SETUP_CONSTANT_INS` (before insert), `DEF_SETUP_CONSTANT_UPD` (before update), `TRG_WS_IKV_BH_WN_Q` (after insert or update or delete)

### PAYROLL.DEF_SETUP

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

### PAYROLL.DEF_TAX_AMOUNT_OTHER_THAN_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| TAXABLE_AMOUNT_ID | NUMBER(5) | N |  |
| TAXABLE_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TAXABLE_AMOUNT_ID`: TAXABLE_AMOUNT_ID
- **Triggers**: `DEF_TAX_AMOUNT_OTHER_THAN_SAL_CEA` (before insert or update or delete), `DEF_TAX_AMOUNT_OTHER_THAN__DEL` (after delete), `DEF_TAX_AMOUNT_OTHER_THAN__INS` (before insert), `DEF_TAX_AMOUNT_OTHER_THAN__UPD` (before update), `TRG_WS_ALH_HY_ST_Q` (after insert or update or delete)

### PAYROLL.EMPLOYEE_INCOME_DETAIL

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


### PAYROLL.EMPLOYEE_INCOME_DETAIL_FQ

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


### PAYROLL.EMP_ALLOWANCE_DEDUCTION
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

### PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL

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
- **CHECK** `CK_EMP_ALL_DED_DETAIL_1`: POSTED IN ('Y','N')
- **Triggers**: `EMP_ALLOWANCE_DEDUCTION_DE_DEL` (after delete), `EMP_ALLOWANCE_DEDUCTION_DE_INS` (before insert), `EMP_ALLOWANCE_DEDUCTION_DE_UPD` (before update)

### PAYROLL.EMP_AWARDS

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

### PAYROLL.EMP_AWARD_PAYMENT

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

### PAYROLL.EMP_EXPENSE

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
- **CHECK** `CK_EMP_EXPENSE_1`: SELF_DEPEND IN ('S', 'D')
- **CHECK** `CK_EMP_EXPENSE_2`: CANCELLED IN ('Y', 'N')
- **CHECK** `CK_EMP_EXPENSE_3`: INCLUDE_IN_TAX IN ('Y', 'N')
- **Triggers**: `EMP_EXPENSE_DEL` (after delete), `EMP_EXPENSE_INS` (before insert), `EMP_EXPENSE_UPD` (before update)

### PAYROLL.EMP_EXPENSE_LIST

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

### PAYROLL.EMP_EXPENSE_LIST_DTL

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

### PAYROLL.EMP_EXP_DET_PROJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_NO | VARCHAR2(12) | N |  |
| PROJECT_ID | VARCHAR2(7) | N |  |
| AMOUNT | NUMBER | Y |  |

- **PK** `PK_EMP_EXP_DET_PROJECT`: DOCUMENT_NO, PROJECT_ID
- **Triggers**: `EMP_EXP_DET_PROJECT_DEL` (after delete), `EMP_EXP_DET_PROJECT_INS` (before insert), `EMP_EXP_DET_PROJECT_UPD` (before update)

### PAYROLL.EMP_INCREMENT_MASTER

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
- **CHECK** `CK_EMP_INCREMENT_MASTER_1`: POSTED IN ('Y','N')
- **Triggers**: `EMP_INCREMENT_MASTER_DEL` (after delete), `EMP_INCREMENT_MASTER_INS` (before insert), `EMP_INCREMENT_MASTER_UPD` (before update)

### PAYROLL.EMP_INCREMENT_DETAIL

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

### PAYROLL.EMP_ITAX_ADJUSTMENT

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

### PAYROLL.EMP_ITAX_ADJUSTMENT_DTL

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

### PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M

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

### PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY

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

### PAYROLL.EMP_LIABILITY

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
- **CHECK** `CK_EMP_LIABILITY_1`: STATUS IN ('C', 'N')
- **Triggers**: `EMP_LIABILITY_DEL` (after delete), `EMP_LIABILITY_INS` (before insert), `EMP_LIABILITY_UPD` (before update)

### PAYROLL.EMP_NEW_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | NUMBER | Y |  |
| CURRENT_SAL | NUMBER | Y |  |
| INC_AGE | NUMBER | Y |  |
| INCR_AMNT | NUMBER | Y |  |
| NEW_SAL | NUMBER | Y |  |


### PAYROLL.EMP_PAYMENT

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

### PAYROLL.EMP_TAX_AMOUNT_OTHER_THAN_SAL

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

### PAYROLL.EXPENSE_CLAIM_MASTER

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

### PAYROLL.EXPENSE_CLAIM_DETAIL

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

### PAYROLL.EXPENSE_CLAIM_DOCUMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(13) | N |  |
| CLAIM_NO | VARCHAR2(12) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_EXPENSE_CLAIM_DOCUMENT`: DOCUMENT_ID
- **FK** `FK_EXPENSE_CLAIM_DOCUMENT`: (CLAIM_NO) -> PAYROLL.EXPENSE_CLAIM_MASTER(CLAIM_NO)

### PAYROLL.EXPENSE_CLAIM_HIERARCHY

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

### PAYROLL.EXPENSE_CLAIM_HIERARCHY_ORG

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_ID | NUMBER | N |  |
| AUTHORITY_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORDERBY | NUMBER | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

_No standard audit columns._

- **Triggers**: `TRG_EXP_CLAIM_HIERARCHY_ORG_ID` (before insert)

### PAYROLL.EXPENSE_CLAIM_PROJECT

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

### PAYROLL.EXPENSE_CLAIM_WORKFLOW

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

### PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| CLAIM_NO | VARCHAR2(12) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

- **PK** `PK_EXPENSE_CLAIM_WF_Q`: CLAIM_NO, WFE_NO, ASSIGNEE_MRNO
- **Triggers**: `EXPENSE_CLAIM_WORKFLOW_Q_APPR_INS` (before insert), `EXPENSE_CLAIM_WORKFLOW_Q_INS` (before insert)

### PAYROLL.FINAL_SETTLEMENT

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

### PAYROLL.FINAL_SETTLEMENT_ELEMENT

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

### PAYROLL.FINAL_SETTLEMENT_WF

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


### PAYROLL.FINAL_SETTLEMENT_WF_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

_No standard audit columns._

- **Triggers**: `FS_WORKFLOW_PQ_INS` (before insert)

### PAYROLL.GENERIC_REPORT_MASTER

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

### PAYROLL.GENERIC_REPORT_FIELD

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

### PAYROLL.GENERIC_REPORT_FIELD_DTL

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

### PAYROLL.HOLD_ORDER

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

### PAYROLL.ITAX_PAYMENT_DETAIL

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

### PAYROLL.ITAX_PAYMENT_MASTER

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

### PAYROLL.LEAVE_DAYS_TEST

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
- **CHECK** `CHK_LEAVE_DAYS_TEST`: UNPAID_STATUS IN ('N','D','U')

### PAYROLL.LOAN_INSTALLMENT_DETAIL

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

### PAYROLL.LOAN_PAYMENT_INTEREST

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

### PAYROLL.LOAN_PAYMENT_MASTER
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
- **CHECK** `CK_LOAN_PAYMENT_MASTER_1`: TRANS_TYPE IN ('O', 'L')
- **CHECK** `CK_LOAN_PAYMENT_MASTER_2`: CANCELLED IN ('Y', 'N')
- **CHECK** `CK_LOAN_PAYMENT_MASTER_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N')
- **Triggers**: `LOAN_PAYMENT_MASTER_DEL` (after delete), `LOAN_PAYMENT_MASTER_INS` (before insert), `LOAN_PAYMENT_MASTER_UPD` (before update)

### PAYROLL.LOAN_PAYMENT_MASTER_N
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
- **CHECK** `CK_LOAN_PAYMENT_MASTER_N_1`: TRANS_TYPE IN ('O', 'L', 'R')
- **CHECK** `CK_LOAN_PAYMENT_MASTER_N_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N')
- **Triggers**: `LOAN_PAYMENT_MASTER_N_DEL` (after delete), `LOAN_PAYMENT_MASTER_N_INS` (before insert), `LOAN_PAYMENT_MASTER_N_UPD` (before update)

### PAYROLL.LOAN_PAYMENT_MASTER_TEST

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
- **CHECK** `CK_LOAN_PAYMENT_MASTER_TEST_2`: CANCELLED IN ('Y', 'N')
- **CHECK** `CK_LOAN_PAYMENT_MASTER_TEST_3`: STOP_AUTO_DEDUCTION IN ('Y', 'N')

### PAYROLL.LOAN_REFUND_MASTER
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
- **CHECK** `CK_LOAN_REFUND_MASTER_1`: CANCELLED IN ('Y', 'N')
- **CHECK** `CK_LOAN_REFUND_MASTER_2`: REFUND_TYPE IN ('M', 'S')
- **Triggers**: `LOAN_REFUND_MASTER_DEL` (after delete), `LOAN_REFUND_MASTER_INS` (before insert), `LOAN_REFUND_MASTER_UPD` (before update)

### PAYROLL.LOAN_REFUND_DETAIL
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

### PAYROLL.LOAN_REFUND_MASTER_N
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
- **CHECK** `CK_LOAN_REFUND_MASTER_N_2`: REFUND_TYPE IN ('M', 'S')
- **Triggers**: `LOAN_REFUND_MASTER_N_DEL` (after delete), `LOAN_REFUND_MASTER_N_INS` (before insert), `LOAN_REFUND_MASTER_N_UPD` (before update)

### PAYROLL.LOAN_REFUND_DETAIL_N
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

### PAYROLL.LOAN_REFUND_MASTER_TEST

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
- **CHECK** `CK_LOAN_REFUND_MASTER_TEST_1`: CANCELLED IN ('Y', 'N')
- **CHECK** `CK_LOAN_REFUND_MASTER_TEST_5`: REFUND_TYPE IN ('M', 'S')

### PAYROLL.LOAN_REFUND_DETAIL_TEST

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

### PAYROLL.LOAN_REFUND_OPENING

| Column | Type | Null | Comment |
|---|---|---|---|
| LOAN_NO | VARCHAR2(12) | N |  |
| SR_NO | NUMBER(2) | N |  |
| REFUND_DATE | DATE | Y |  |
| REFUND_TYPE | CHAR(1) | Y |  |
| REFUND_AMOUNT | NUMBER(20,2) | Y |  |

- **PK** `PK_LOAN_REFUND_OPENING`: LOAN_NO, SR_NO
- **Triggers**: `LOAN_REFUND_OPENING_DEL` (after delete), `LOAN_REFUND_OPENING_INS` (before insert), `LOAN_REFUND_OPENING_UPD` (before update)

### PAYROLL.MANUAL_MONTH_MASTER

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

### PAYROLL.MANUAL_PAY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| AMOUNT | NUMBER(7) | Y |  |

- **PK** `PK_MANUAL_PAY_MASTER`: START_DATE, END_DATE, SERIAL_NO, MRNO
- **FK** `FK_MANUAL_PAY_MASTER`: (START_DATE, END_DATE, SERIAL_NO) -> PAYROLL.MANUAL_MONTH_MASTER(START_DATE, END_DATE, SERIAL_NO)

### PAYROLL.MANUAL_ALLOWANCE_DEDUCTION

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

### PAYROLL.MONTH_CHANGE_REQUEST

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

### PAYROLL.MONTH_CHANGE_REQUEST_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_NAME | VARCHAR2(2000) | Y |  |
| RESULT_COUNT | NUMBER | Y |  |
| MON_START_DATE | DATE | Y |  |
| MON_END_DATE | DATE | Y |  |

_No standard audit columns._


### PAYROLL.PAY_AD_BALANCE

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

### PAYROLL.PAY_AD_BALANCE_TEST

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

### PAYROLL.PAY_MASTER
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

### PAYROLL.PAY_ALLOWANCE_DEDUCTION
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

### PAYROLL.PAY_MASTER_TEST
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

### PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST
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

### PAYROLL.PAY_ARREAR

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

### PAYROLL.PAY_ARREAR_TEST

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

### PAYROLL.PAY_DAILY_AD_TEST

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

### PAYROLL.PAY_DAILY_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| AD_CODE | CHAR(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| DAY | DATE | N |  |
| AMOUNT | NUMBER(10,2) | Y |  |

- **PK** `PK_PAY_DAILY_TEMP`: MRNO, AD_CODE, DAY

### PAYROLL.PAY_DAILY_TEMP_UNPAID

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

### PAYROLL.PAY_DR_FEE

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


### PAYROLL.PAY_EXCEPTIONAL

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


### PAYROLL.PAY_ITAX_DETAIL

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

### PAYROLL.PAY_ITAX_DETAIL_HISTORY

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


### PAYROLL.PAY_ITAX_DTL_TMP

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

### PAYROLL.PAY_ITAX_INCOME_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| PARAMETER | VARCHAR2(32) | N |  |
| AMOUNT | NUMBER(15,3) | Y |  |

_No standard audit columns._

- **PK** `PK_PAY_ITAX_INCOME_DETAIL`: MRNO, START_DATE, END_DATE, PARAMETER

### PAYROLL.PAY_LEAVES

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

### PAYROLL.PAY_PF_VOUCHER

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

### PAYROLL.PAY_REPORT_FILE

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_CODE | NUMBER(2) | N |  |
| REPORT_TITLE | VARCHAR2(255) | Y |  |
| SUMMARY_DETAIL | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PAY_REPORT_FILE`: REPORT_CODE

### PAYROLL.PAY_REPORT_FORMAT
This table is used to define groups of different allowances / deductions, this group will be used into formatting salary sheets

| Column | Type | Null | Comment |
|---|---|---|---|
| AD_GROUP_CODE | CHAR(3) | N | PK-Self explainatory |
| DESCRIPTION | VARCHAR2(255) | Y | Group description (House Rent, Utilities, Income Tax, Others etc.) |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y | Short description of Group, to be displayed onto Salary Sheet |
| ACTIVE | CHAR(1) default 'Y' | Y | Either record is available currently for transactions or not |

- **PK** `PK_DEF_ALLOW_DEDUCT_GROUP`: AD_GROUP_CODE
- **CHECK** `CK_DEF_ALLOW_DEDUCT_GROUP_1`: ACTIVE IN ('Y', 'N')

### PAYROLL.PAY_REPORT_ROUTING

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_CODE | NUMBER(2) | N |  |
| AD_CODE | CHAR(3) | N |  |
| AD_GROUP_CODE | CHAR(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PAY_REPORT_ROUTING`: REPORT_CODE, AD_CODE, AD_GROUP_CODE
- **FK** `FK_PAY_REPORT_ROUTING_1`: (REPORT_CODE) -> PAYROLL.PAY_REPORT_FILE(REPORT_CODE)
- **FK** `FK_PAY_REPORT_ROUTING_2`: (AD_GROUP_CODE) -> PAYROLL.PAY_REPORT_FORMAT(AD_GROUP_CODE)

### PAYROLL.PAY_STATUS

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
- **CHECK** `CHK_PAY_STATUS_01`: STATUS IN ('N','S')
- **Triggers**: `PAY_STATUS_DEL` (after delete), `PAY_STATUS_INS` (before insert), `PAY_STATUS_UPD` (before update)

### PAYROLL.PAY_TMP_BANK

| Column | Type | Null | Comment |
|---|---|---|---|
| BRANCH_ID | VARCHAR2(3) | Y |  |
| BRANCH_DESCRIPTION | VARCHAR2(255) | Y |  |
| BANK_ID | VARCHAR2(6) | Y |  |
| BANK_DESCRIPTION | VARCHAR2(255) | Y |  |
| SELECTED | CHAR(1) | Y |  |
| USERID | VARCHAR2(30) | Y |  |
| PARENT_BRANCH_ID | VARCHAR2(3) | Y |  |


### PAYROLL.PAY_TMP_EMP

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


### PAYROLL.PAY_TMP_MPA

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


### PAYROLL.PAY_TMP_REPORT

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


### PAYROLL.PAY_VOUCHER

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
- **CHECK** `CK_PAY_VOUCHER_1`: PF_CANCELLED IN ('Y','N')
- **CHECK** `CK_PAY_VOUCHER_2`: GL_CANCELLED IN ('Y','N')
- **CHECK** `CK_PAY_VOUCHER_3`: LOAN_CANCELLED IN ('Y','N')
- **Triggers**: `PAY_VOUCHER_DEL` (after delete), `PAY_VOUCHER_INS` (before insert), `PAY_VOUCHER_UPD` (before update)

### PAYROLL.PAY_VOUCHER_MASTER

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

### PAYROLL.PAY_VOUCHER_DETAIL

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

### PAYROLL.PAY_VOUCHER_TEMP

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

- **CHECK** `CK_PAY_VOUCHER_TEMP_1`: TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O')

### PAYROLL.PAY_VOUCHER_TMP

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

### PAYROLL.PENDING_LOANS

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


### PAYROLL.PF_FINAL_SETTLEMENT

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

### PAYROLL.PROCESS_INCREMENT_MASTER

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

### PAYROLL.PROCESS_MEMBERS

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

### PAYROLL.PROFIT_VOUCHER_TMP

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

### PAYROLL.REP_LOAN_LEDGER
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


### PAYROLL.RPT_SALARY_TAX_LINE_ITEM

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

### PAYROLL.R_COST_TO_COMPANY_TEMP

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

### PAYROLL.SALARY_ELEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| FINAL_SETTLEMENT_ID | VARCHAR2(9) | Y |  |
| SRNO | NUMBER | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| AMOUNT | NUMBER(10) | Y |  |

_No standard audit columns._


### PAYROLL.SALARY_SLABS

| Column | Type | Null | Comment |
|---|---|---|---|
| FROM_RANGE | NUMBER(6) | Y |  |
| TO_RANGE | NUMBER(6) | Y |  |
| INCR_PERCENT | NUMBER(5,2) | Y |  |
| NO_OF_EMP | NUMBER(4) | Y |  |
| TOTAL_SALARY | NUMBER(8) | Y |  |
| TOT_INC | NUMBER | Y |  |
| INCR_AGE | NUMBER | Y |  |


### PAYROLL.TARGET_TABLE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| AD_CODE | CHAR(3) | Y |  |
| AD_VALUE | NUMBER | Y |  |


### PAYROLL.TAX_CALCULATION_LOG

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


### PAYROLL.TEMP_INCREMENT_MASTER

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

### PAYROLL.TEMP_INCREMENT_DETAIL

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

### PAYROLL.TEMP_INDIVIDUAL_ITAX

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


### PAYROLL.TEMP_ITAX

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


### PAYROLL.TEMP_SALARY_RECONCILE_DATA

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


### PAYROLL.TMP_LOAN_SUMMARY

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


### PAYROLL.TRAVEL_ADVANCE_APPROVAL

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



# PART: Views

### PAYROLL.PAD_DR_FEE
```sql
create or replace force view payroll.pad_dr_fee as
select mrno, start_date, end_date, ad_code, pad.actual_amount, pad.calc_amount, pad.calc_amount_guarantee, pad.pending_amount
from payroll.pay_allowance_deduction pad
where pad.ad_code in ('007','043');
```

### PAYROLL.PAYMASTER_VIEW
```sql
create or replace force view payroll.paymaster_view as
select MRNo, P_Fund_Amount, P_Fund_Loan, posted
from payroll.pay_master;
```

### PAYROLL.PM_DR_FEE
```sql
create or replace force view payroll.pm_dr_fee as
select mrno, start_date, end_date, practice_income, practice_income_tax
from payroll.pay_master;
```

### PAYROLL.VU_PAY_STATUS
```sql
CREATE OR REPLACE FORCE VIEW PAYROLL.VU_PAY_STATUS AS
SELECT p.serial_no,
       p.mrno,
       p.date_from,
       p.date_to,
       p.status,
       p.disciplinary_reason_id,
       p.original_user_id,
       p.original_terminal,
       p.original_trn_date,
       p.user_id,
       p.terminal,
       p.trn_date,
       p.user_comments,
       substr(p.mrno, -11) emp_code,
       i.name,
       i.department,
       i.department_id,
       i.designation,
       m.pay_calc_date,
       m.pay_process,
       m.month
  FROM payroll.pay_status p, hrd.vu_information i, definitions.months m
 WHERE p.mrno = i.mrno
   AND p.date_from = m.pay_start_date
   AND p.date_to = m.pay_end_date;
```

### PAYROLL.V_PAYMASTER
```sql
CREATE OR REPLACE FORCE VIEW PAYROLL.V_PAYMASTER AS
SELECT MRNO, P_FUND_LOAN FROM PAYROLL.PAY_MASTER;
```



# PART: Packages, procedures, functions, sequences

### Sequences
- LOAN_NO

### Packages (specifications)

#### PAYROLL.PKG_AD_DETAIL
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_AD_DETAIL AS

  /***********************************************************************************************
         OBJECTIVE :=
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        02-MAY-2018   Muhammad Ali Khubaib   1. Created this Package.
  
  ************************************************************************************************/
  ---------------------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ---------------------------------------------------------------------------
  PROCEDURE INSERT_AD_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_ROW               IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL%ROWTYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);

  ------------------------------------------------------------
  -- FOLLOWING FUNCTION WILL RETURN AD PERCENTAGE IN GROSS  --
  ------------------------------------------------------------
  FUNCTION GET_CURR_AD_CALC_PERCENT(P_AD_CODE    IN PAYROLL.ALLOWANCE_DEDUCTION_SETUP.AD_CODE%TYPE,
                                    P_TRANS_DATE IN DATE)
    RETURN PAYROLL.ALLOWANCE_DEDUCTION_SETUP.CALC_PERCENT%TYPE;

  ---------------------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ---------------------------------------------------------------------------
  PROCEDURE INSERT_CURRENT_MONTH_AD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_AD_CODE           IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                                    P_MRNO              IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                                    P_AMOUNT            IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
                                    P_REMARKS           IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
                                    P_NO_OF_DAYS        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.NO_OF_DAYS%TYPE DEFAULT 0,
                                    P_PROCESS_ID        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  ---------------------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ---------------------------------------------------------------------------
  PROCEDURE DELETE_CURRENT_MONTH_AD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_START_DATE        IN DATE,
                                    P_END_DATE          IN DATE,
                                    P_AD_CODE           IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                                    P_MRNO              IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                                    P_PROCESS_ID        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  ---------------------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ---------------------------------------------------------------------------
  PROCEDURE OVERRIGHT_CURRENT_MONTH_AD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_AD_CODE           IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                                    P_MRNO              IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                                    P_AMOUNT            IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
                                    P_REMARKS           IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
                                    P_NO_OF_DAYS        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.NO_OF_DAYS%TYPE DEFAULT 0,
                                    P_PROCESS_ID        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_CHECK_REMARKS        IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);

END PKG_AD_DETAIL;
```

#### PAYROLL.PKG_AD_UTILITIES
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_AD_UTILITIES IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-AUG-2018   Shahid Jamal (8317)    1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -------------------------------------------------
  -- Procedure to Execute all pre itax processes --
  -------------------------------------------------
  PROCEDURE RUN_PAYMENT_PROCESSES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);

  ---------------------------------------------------
  -- Procedure to update Unposted Claimed Expenses --
  ---------------------------------------------------
  PROCEDURE PROCESS_CLAIMED_EXP(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_START_DATE        IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE,
                                P_END_DATE          IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  ------------------------------------
  -- Procedure to insert LFA Amount --
  ------------------------------------
  PROCEDURE PROCESS_LFA_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  ----------------------------------
  -- Procedure to undo LFA Amount --
  ----------------------------------
  PROCEDURE PROCESS_LFA_PAYMENT_UNDO(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MON_START_DATE    IN DATE,
                                     P_MON_END_DATE      IN DATE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);

  --------------------------------------------
  -- Procedure to insert Unclaimed Expenses --
  --------------------------------------------
  PROCEDURE INSERT_EXPENSE_ALLOWANCES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT VARCHAR2);
  --------------------------------------------------
  -- Procedure will HOLD and UNHOLD Salary Process --
  --------------------------------------------------
  PROCEDURE PROCESS_PAY_HOLD_ORDER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_START_DATE    IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE,
                                   P_PAY_END_DATE      IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE,
                                   P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                   P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT VARCHAR2);
  -------------------------------------------
  -- Procedure to insert loan installments --
  -------------------------------------------
  PROCEDURE PROCESS_LOAN_INSTALLMENTS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_MON_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                      P_MON_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                      P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                      P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                      P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT VARCHAR2);
  PROCEDURE PROCESS_LSA_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MON_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_MON_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);
  PROCEDURE PROCESS_LSA_PAYMENT_UNDO(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MON_START_DATE    IN DATE,
                                     P_MON_END_DATE      IN DATE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
END PKG_AD_UTILITIES;
```

#### PAYROLL.PKG_ARREAR_DETAIL
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_ARREAR_DETAIL AS

  /***********************************************************************************************
         OBJECTIVE :=
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-SEP-2020   Muhammad Ali Khubaib   1. Created this Package.
  
  ************************************************************************************************/
  --------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ARREAR_DETAIL --
  --------------------------------------------------------------
  PROCEDURE INSERT_ARREAR_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_ROW               IN PAYROLL.ARREAR_DETAIL%ROWTYPE,
                                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                 P_USER_MRNO         IN VARCHAR2,
                                 P_TERMINAL          IN VARCHAR2,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);

  --------------------------------------------------------------
  -- This Procedure will insert data in PAYROLL.ARREAR_DETAIL --
  --------------------------------------------------------------
  PROCEDURE INSERT_CURRENT_MONTH_ARREAR(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_ARREAR_CODE       IN PAYROLL.ARREAR_DETAIL.ARREAR_CODE%TYPE,
                                        P_AD_CODE           IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE,
                                        P_MRNO              IN PAYROLL.ARREAR_DETAIL.MRNO%TYPE,
                                        P_ARREAR_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE,
                                        P_ARREAR_END_DATE   IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE,
                                        P_AMOUNT            IN PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE,
                                        P_REMARKS           IN PAYROLL.ARREAR_DETAIL.REMARKS%TYPE,
                                        P_DAYS_HOURS        IN PAYROLL.ARREAR_DETAIL.DAYS_HOURS%TYPE DEFAULT 0,
                                        P_PROCESS_ID        IN PAYROLL.ARREAR_DETAIL.PROCESS_ID%TYPE,
                                        P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                        P_USER_MRNO         IN VARCHAR2,
                                        P_TERMINAL          IN VARCHAR2,
                                        P_ALERT_TEXT        OUT VARCHAR2,
                                        P_STOP              OUT CHAR);

END PKG_ARREAR_DETAIL;
```

#### PAYROLL.PKG_AWARD_PAYMENT
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_AWARD_PAYMENT IS
  /***********************************************************************************************
         OBJECTIVE := This package was created for Employee Expense entry/adjustments
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        31-JAN-2022   Shahid Jamal           1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  FUNCTION GET_PAID_AMOUNT(P_AWARD_ID IN PAYROLL.EMP_AWARD_PAYMENT.AWARD_ID%TYPE)
    RETURN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE;
  ----------------------------------------------------------------------------------------------------------
  -- This procedure will be used to generate counter no for pyament id field of PAYROLL.EMP_AWARD_PAYMENT table --
  ----------------------------------------------------------------------------------------------------------
  PROCEDURE GEN_PAYMENT_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_TRAN_DATE         IN DATE,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                           P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_PAYMENT_ID        OUT PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_ID%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);
  PROCEDURE GEN_AWARD_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_TRAN_DATE         IN DATE,
                         P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                         P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                         P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                         P_AWARD_ID          OUT PAYROLL.EMP_AWARDS.AWARD_ID%TYPE,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT VARCHAR2);
  PROCEDURE INS_LFA_PAYMENT_SAL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MRNO              IN PAYROLL.EMP_AWARDS.MRNO%TYPE,
                                P_DUE_DATE          IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE,
                                P_AMOUNT            IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
                                P_MON_START_DATE    IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE,
                                P_MON_END_DATE      IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  PROCEDURE INS_AWARD_AND_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO              IN PAYROLL.EMP_AWARDS.MRNO%TYPE,
                                  P_DUE_DATE          IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE,
                                  P_EXPENSE_CODE      IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE,
                                  P_PAYMENT_BASE      IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE,
                                  P_PAYMENT_RATE      IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE,
                                  P_AMOUNT            IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
                                  P_AD_CODE           IN PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE,
                                  P_MON_START_DATE    IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE,
                                  P_MON_END_DATE      IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE,
                                  P_DOCUMENT_NO       IN PAYROLL.EMP_AWARD_PAYMENT.DOCUMENT_NO %TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  -------------------------
  -- POST Award Paymemnt --
  -------------------------
  PROCEDURE INSERT_EMP_AWARD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_MRNO              IN PAYROLL.EMP_AWARDS.MRNO%TYPE,
                             P_DUE_DATE          IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE,
                             P_EXPENSE_CODE      IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE,
                             P_PAYMENT_BASE      IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE,
                             P_PAYMENT_RATE      IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE,
                             P_AMOUNT            IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
                             P_AWARD_ID          OUT PAYROLL.EMP_AWARDS.AWARD_ID%TYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  PROCEDURE INSERT_EMP_AWARD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_MRNO              IN PAYROLL.EMP_AWARDS.MRNO%TYPE,
                             P_DUE_DATE          IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE,
                             P_EXPENSE_CODE      IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE,
                             P_PAYMENT_BASE      IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE,
                             P_PAYMENT_RATE      IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE,
                             P_AMOUNT            IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  ---------------------------
  -- INSERT PAYMENT DETAIL --
  ---------------------------
  PROCEDURE INSERT_AWARD_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_AWARD_ID          IN PAYROLL.EMP_AWARDS.AWARD_ID%TYPE,
                                 P_AMOUNT            IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
                                 P_AD_CODE           IN PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE,
                                 P_MON_START_DATE    IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE,
                                 P_MON_END_DATE      IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE,
                                 P_DOCUMENT_NO       IN PAYROLL.EMP_AWARD_PAYMENT.DOCUMENT_NO %TYPE,
                                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                 P_USER_MRNO         IN VARCHAR2,
                                 P_TERMINAL          IN VARCHAR2,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);
  PROCEDURE INSERT_LSA_AWARDS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_FROM_DATE         IN DATE,
                              P_TO_DATE           IN DATE,
                              P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  PROCEDURE CANCEL_AWARD_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_MRNO              IN PAYROLL.Emp_Awards.MRNO%TYPE,
                                 P_AD_CODE           IN PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE,
                                 P_MON_START_DATE    IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE,
                                 P_MON_END_DATE      IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE,
                                 P_DOCUMENT_NO       IN PAYROLL.EMP_AWARD_PAYMENT.DOCUMENT_NO %TYPE,
                                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                 P_USER_MRNO         IN VARCHAR2,
                                 P_TERMINAL          IN VARCHAR2,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);
 PROCEDURE INSERT_LFA_ADJUSTMENTS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_FROM_DATE         IN DATE,
                            P_TO_DATE           IN DATE,
                            P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_USER_MRNO         IN VARCHAR2,
                            P_TERMINAL          IN VARCHAR2,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT CHAR);
END PKG_AWARD_PAYMENT;
```

#### PAYROLL.PKG_BANK
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_BANK AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL Bank & Branches
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                  Description
         ---------  -----------   --------------------    -----------------------------------
         1.0        03-AUG-2021   MUHAMMAD ALI KHUBAIB    1. Created this Package.
  ************************************************************************************************/

  FUNCTION GET_BANK_NAME(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE)
    RETURN VARCHAR2;

  FUNCTION GET_PARENT_ADDRESS(P_BANK_ID   IN DEFINITIONS.BANK.BANK_ID%TYPE,
                              P_BRANCH_ID IN DEFINITIONS.BANK_BRANCH.BRANCH_ID%TYPE)
    RETURN VARCHAR2;

  FUNCTION GET_BRANCH_ADDRESS(P_BANK_ID   IN DEFINITIONS.BANK.BANK_ID%TYPE,
                              P_BRANCH_ID IN DEFINITIONS.BANK_BRANCH.BRANCH_ID%TYPE)
    RETURN VARCHAR2;

  FUNCTION GET_BANK_ACCOUNT_NO(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE)
    RETURN VARCHAR2;

END;
```

#### PAYROLL.PKG_CARD_MANAGEMENT
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_CARD_MANAGEMENT AS
  /***********************************************************************************************
         OBJECTIVE := This package is created for common function related the card management
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                   Description
         ---------  -----------   ---------------------    -----------------------------------
         1.0        03-SEP-2024   M. Abu bakar Khalid (17114)    1. Created this Package.
         2.0        09-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Approve_request)
                                                                 2. Created Procedure(Sign_request)
                                                                 3. Created Procedure(Cancel_request)
         3.0        14-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Populate_Monthly_Bills)
         4.0        23-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Insert_Payment_method)
         5.0        24-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Post_Monthly_Payments)
                                                                 2. Created Procedure(Finalize_Monthly_payments)
         6.0        24-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Post_Monthly_Payments)
                                                                 2. Created Procedure(Finalize_Monthly_payments)
         7.0        26-SEP-2024   M. Abu bakar Khalid (17114)    1. Created Procedure(Post_Excess_Amount)
         8.0        27-SEP-2024   M. Abu bakar Khalid (17114)    1. Updated Procedure(Post_Monthly_Payments)
                                                                    ( Added a loop to insert in all given record
                                                                      and a cursor to check if the record exixts
                                                                      exixts initially)
                                                                 2. Updated Procedure(Finalize_Monthly_payments)
                                                                    ( Added a loop to insert in all given record
                                                                      and a cursor to check if the record exixts
                                                                      exixts initially)
         9.0        30-SEP-2024   M. Abu bakar Khalid (17114)    1. Updated Procedure(Approve Request)
                                                                    ( Corrected def_connection_transection
                                                                      insertion)
  
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  FUNCTION GET_CONTACT_NUMBER(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE)
    RETURN VARCHAR2;
  FUNCTION GET_CONTACT_NUMBER(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                              P_DATE       PAYROLL.CM_CONNECTION_TRANSACTIONS.TO_DATE%TYPE)
    RETURN VARCHAR2;
  FUNCTION GET_CONTACT_NUMBER_NETWORK(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE)
    RETURN VARCHAR2;
  FUNCTION GET_PAYMENT_METHOD_DESC(P_METHOD IN PAYROLL.CM_BILL_DETAIL.PAYMENT_METHOD%TYPE)
    RETURN VARCHAR2;
  FUNCTION IS_CONNECTION_ISSUED(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE)
    RETURN VARCHAR2;
  PROCEDURE GEN_REQUEST_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_REQUEST_ID        OUT VARCHAR2,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);
  ------------------------------------------------------------------------
  -- Following prodedrue will be used to activate the connnection/sim   --
  ------------------------------------------------------------------------
  PROCEDURE ACTIVATE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE,
                                P_ALERT_TEXT    OUT VARCHAR2,
                                P_STOP          OUT VARCHAR2);
  ------------------------------------------------------------------------
  -- Following prodedrue will be used to INactivate the connnection/sim   --
  ------------------------------------------------------------------------
  PROCEDURE INACTIVATE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE,
                                  P_ALERT_TEXT    OUT VARCHAR2,
                                  P_STOP          OUT VARCHAR2);

  ------------------------------------------------------------------------
  -- Following prodedrue will be used to transfer the connnection/sim   --
  ------------------------------------------------------------------------
  PROCEDURE VACANT_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE,
                              P_ALERT_TEXT    OUT VARCHAR2,
                              P_STOP          OUT VARCHAR2);
  PROCEDURE ISSUE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE,
                             p_REQUEST_ID    IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                             P_ALERT_TEXT    OUT VARCHAR2,
                             P_STOP          OUT VARCHAR2);
  ------------------------------------------------------------------------
  -- Following prodedrue will be used to check the status of the id   --
  ------------------------------------------------------------------------
  PROCEDURE CONNECTION_STATUS(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                              P_ALERT_TEXT OUT VARCHAR2,
                              P_STOP       OUT VARCHAR2);

  ------------------------------------------------------------------------
  -- Following prodedrue will be used to check the sign status   --
  ------------------------------------------------------------------------
  PROCEDURE SIGN_REQUEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_REQUEST_ID        IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                         P_USER_MRNO         IN VARCHAR2,
                         P_TERMINAL          IN VARCHAR2,
                         P_OBJECT_CODE       IN VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT VARCHAR2);
  ------------------------------------------------------------------------
  -- Following prodedrue will be used to check the Active REQUEST   --
  ------------------------------------------------------------------------
  PROCEDURE APPROVE_REQUEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_REQUEST_ID        IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                            P_CONNECTION_ID     IN PAYROLL.CM_CONNECTION_REQUEST.CONNECTION_ID%TYPE,
                            P_USER_MRNO         IN VARCHAR2,
                            P_TERMINAL          IN VARCHAR2,
                            P_OBJECT_CODE       IN VARCHAR2,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT VARCHAR2);
  ------------------------------------------------------------------------
  -- Following prodedrue will be used to check the CANCLE REQUEST   --
  ------------------------------------------------------------------------

  PROCEDURE CANCEL_REQUEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_REQUEST_ID        IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);

  ------------------------------------------------------------------------
  -- Following function to populate    --
  ------------------------------------------------------------------------
  Procedure POPULATE_MONTHLY_BILLS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MONTH_ID          IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE,
                                   P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- wrong request --------------------------------------------
  ---------------------------------------------------------------------------------------------------------------
  PROCEDURE DELETE_BILL_DETAILS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MONTH_ID          IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE,
                                P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- insert payment method --------------------------------------------
  ---------------------------------------------------------------------------------------------------------------

  PROCEDURE PAYMENT_METHOD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_DETAIL.ADMIN_GROUP_ID%TYPE,
                           P_MONTH_ID          IN PAYROLL.CM_BILL_DETAIL.MONTH_ID%TYPE,
                           P_REQUEST_ID        IN PAYROLL.CM_BILL_DETAIL.REQUEST_ID%TYPE,
                           P_PAYMENT_METHOD    IN VARCHAR2,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- STATUS OF FORM MONTLY_PAYMENTS ---------------------------------
  ---------------------------------------------------------------------------------------------------------------

  PROCEDURE POST_MONTHLY_PAYMENTS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MONTH_ID          IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE,
                                  P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- FINALIZE OF FORM MONTLY_PAYMENTS ---------------------------------
  ---------------------------------------------------------------------------------------------------------------

  PROCEDURE FINALIZE_MONTHLY_PAYMENTS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_MONTH_ID          IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE,
                                      P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE,
                                      P_USER_MRNO         IN VARCHAR2,
                                      P_TERMINAL          IN VARCHAR2,
                                      P_OBJECT_CODE       IN VARCHAR2,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT VARCHAR2);
  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- CALCULATE EXCESS AMOUNT ---------------------------------
  ---------------------------------------------------------------------------------------------------------------

  PROCEDURE POST_EXCESS_AMOUNT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ADMIN_GROUP_ID    IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE,
                               P_MONTH_ID          IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);
  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- TRANSFER CONNECTION ---------------------------------
  ---------------------------------------------------------------------------------------------------------------
  PROCEDURE TRANSFER_CONNECTIONS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 -- P_MRNO              IN HRD.VU_INFORMATION.MRNO%TYPE,
                                 P_CONNECTION_ID  IN PAYROLL.CM_CONNECTION_TRANSACTIONS.CONNECTION_ID%TYPE,
                                 P_TRANSACTION_ID IN PAYROLL.CM_CONNECTION_TRANSACTIONS.TRANS_ID%TYPE,
                                 P_REQUEST_ID     IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                                 P_USER_MRNO      IN VARCHAR2,
                                 P_TERMINAL       IN VARCHAR2,
                                 P_ALERT_TEXT     OUT VARCHAR2,
                                 P_STOP           OUT VARCHAR2);
  PROCEDURE SEND_PAYMENT_SMS(P_SMS_NUMBER    IN VARCHAR2,
                             P_EMPLOYEE_NAME IN VARCHAR2,
                             P_MONTH         IN VARCHAR2,
                             P_BILL_AMOUNT   IN NUMBER,
                             P_ALERT_TEXT    OUT VARCHAR2,
                             P_STOP          OUT CHAR);
  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- IS_DATA_SIM--------------------------------------------
  ---------------------------------------------------------------------------------------------------------------
  FUNCTION IS_DATA_SIM(P_CONTACT_NUMBER IN PAYROLL.CM_DEF_CONNECTION.CONTACT_NUMBER%TYPE)
    RETURN VARCHAR2;
 ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- TRANSFER CONTACT NUMBER-------------------------------------------
  ---------------------------------------------------------------------------------------------------------------

  PROCEDURE TRANSFER_NUMBER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_REQUEST_ID        IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                            P_DEPARTMENT_ID     IN PAYROLL.CM_CONNECTION_REQUEST.DEPARTMENT_ID%TYPE,
                            P_REQUEST_TYPE      IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_TYPE%TYPE,
                            P_FROM_DATE         IN PAYROLL.CM_CONNECTION_REQUEST.FROM_DATE%TYPE,
                            P_MRNO              IN PAYROLL.CM_CONNECTION_REQUEST.MRNO%TYPE,
                            P_LIMIT_ALLOWED     IN PAYROLL.CM_CONNECTION_REQUEST.LIMIT_ALLOWED%TYPE,
                            P_USER_MRNO         IN VARCHAR2,
                            P_TERMINAL          IN VARCHAR2,
                            P_OBJECT_CODE       IN VARCHAR2,
                            P_NEW_REQUEST       OUT PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT VARCHAR2);
  ---------------------------------------------------------------------------------------------------------------
  ----------------------------------------------- REQUEST NUMBER-------------------------------------------
  ---------------------------------------------------------------------------------------------------------------                           

  PROCEDURE REQUEST_CONNECTION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ROW               IN PAYROLL.CM_CONNECTION_REQUEST%ROWTYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_REQUEST_ID        OUT PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);
  ----------------------------------------------------------------------------------------------------
--------------------------- Package END ------------------------------------------------------------
------------------------------------------------------------------------   ----------------------------
----------------------------------------------------------------------------------------------------
--------------------------- Package END ------------------------------------------------------------
------------------------------------------------------------------------   ----------------------------

END PKG_CARD_MANAGEMENT;
```

#### PAYROLL.PKG_COMMON
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_COMMON IS

  -- Author  : Asma Hashmi
  -- Created : 06/10/2014 11:02:25 AM
  -- Purpose : Common procedure/functions used in PAYROLL module
  FUNCTION GET_DEFSETUP_LOC_DESC(P_LOCATION_ID IN VARCHAR2,
                                 P_ALERT_TEXT  OUT VARCHAR2) RETURN VARCHAR2;

  -- Created by: Asma Hashmi
  -- Creation Date: 19-06-2014 3:57PM
  -- Purpose: Function return constant values from payroll.def_setup
  FUNCTION GET_CONSTANT_VALUE(P_LOCATION_ID IN VARCHAR2,
                              P_DATE        IN DATE DEFAULT SYSDATE,
                              P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                              P_STOP        OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2) RETURN VARCHAR2;

  -- Created by: Asma Hashmi
  -- Creation Date: 09-06-2014 2:25PM
  -- Purpose: Function to the Expense Description
  FUNCTION GET_EXPENSE_DESC(P_EXPENSE_CODE IN VARCHAR2,
                            P_LEVEL        IN VARCHAR2,
                            P_ALERT_TEXT   OUT VARCHAR2) RETURN VARCHAR2;
  /***********************************************************************/
  FUNCTION GET_PF_AMOUNT(P_MRNO      IN VARCHAR2,
                         P_FROM_DATE IN DATE,
                         P_TO_DATE   IN DATE) RETURN NUMBER;
  /******************************************************************************/
  FUNCTION GET_LFA_AMOUNT(P_MRNO      IN VARCHAR2,
                          P_FROM_DATE IN DATE,
                          P_TO_DATE   IN DATE) RETURN NUMBER;
  /******************************************************************************/
  FUNCTION GET_MEDICAL_EXPENSE(P_MRNO      IN VARCHAR2,
                               P_FROM_DATE IN DATE,
                               P_TO_DATE   IN DATE) RETURN NUMBER;
  /******************************************************************************/
  FUNCTION GET_OTHERS_EXPENSE(P_MRNO      IN VARCHAR2,
                              P_FROM_DATE IN DATE,
                              P_TO_DATE   IN DATE) RETURN NUMBER;
  /******************************************************************************/
  -----------------------------------------------------------
  -- Following funtion will get the payroll constant value --
  -----------------------------------------------------------
  FUNCTION GET_CONSTANT_VALUE(P_ORGANIZATION_ID     IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                              P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                              P_DATE                IN DATE,
                              P_CONSTANT_ID         IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                              P_DEFAULT_VAL         IN PAYROLL.DEF_SETUP.VALUE%TYPE)
    RETURN PAYROLL.DEF_SETUP.VALUE%TYPE;
  -----------------------------------------------------------
  -- Following funtion will get the payroll constant value --
  -----------------------------------------------------------
  FUNCTION GET_CONSTANT_NUM_VALUE(P_ORGANIZATION_ID     IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                                  P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                                  P_DATE                IN DATE,
                                  P_CONSTANT_ID         IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                                  P_DEFAULT_VAL         IN NUMBER)
    RETURN NUMBER;
END;
```

#### PAYROLL.PKG_DATALOADER
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_DATALOADER AS

  /***********************************************************************************************
          OBJECTIVE := This package is created for Data Loader Scheme
          ----------------------------------------------------------------------------------
          REVISIONS:
          Ver        Date          Author                  Description
          ---------  -----------   --------------------    -----------------------------------
          1.0        05-Aug-2020   Muhammad Ali Khubaib    1. Created this Package.
  ************************************************************************************************/
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -----------------------------------------------------------------------------
  -- This procedure will insert data into PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  -----------------------------------------------------------------------------
  PROCEDURE IMP_ALL_DED_SHEET(P_AD_CODE    IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                              P_MRNO       IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                              P_AMOUNT     IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
                              P_REMARKS    IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
                              P_NO_OF_DAYS IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.NO_OF_DAYS%TYPE DEFAULT 0,
                              P_PROCESS_ID IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE,
                              P_ALERT_TEXT OUT VARCHAR2,
                              P_STOP       OUT CHAR);

  ----------------------------------------------------------------
  -- This procedure will insert data into PAYROLL.ARREAR_DETAIL --
  ----------------------------------------------------------------
  PROCEDURE IMP_ARREARS_SHEET(P_ARREAR_CODE       IN PAYROLL.ARREAR_DETAIL.ARREAR_CODE%TYPE,
                              P_MRNO              IN PAYROLL.ARREAR_DETAIL.MRNO%TYPE,
                              P_AMOUNT            IN PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE,
                              P_ARREAR_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE,
                              P_ARREAR_END_DATE   IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE,
                              P_REMARKS           IN PAYROLL.ARREAR_DETAIL.REMARKS%TYPE,
                              P_DAYS_HOURS        IN PAYROLL.ARREAR_DETAIL.DAYS_HOURS%TYPE DEFAULT 0,
                              P_PROCESS_ID        IN PAYROLL.ARREAR_DETAIL.PROCESS_ID%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  ------------------------------------------------------------------
  -- This procedure will insert data into PAYROLL.EXP_EXPENSE_TMP --
  ------------------------------------------------------------------
  PROCEDURE IMP_EXPENSE(P_EXPENSE_LIST_ID IN VARCHAR2,
                        P_MRNO            IN VARCHAR2,
                        P_AMOUNT          IN VARCHAR2,
                        P_TAX_DEDUCTED    IN VARCHAR2,
                        P_ALERT_TEXT      OUT VARCHAR2,
                        P_STOP            OUT CHAR);
END PKG_DATALOADER;
```

#### PAYROLL.PKG_DEF_ALLOWANCE_DEDUCTION
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_DEF_ALLOWANCE_DEDUCTION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Abdul Wadood
  -- Created : 01-Dec-2019 11:30
  -- Purpose : 
  -- Public type declarations
  --type <TypeName> is <Datatype>;
  -- Public constant declarations
  --<ConstantName> constant <Datatype> := <Value>;
  -- Public variable declarations
  --<VariableName> <Datatype>;
  -- Public function and procedure declarations
  --function <FunctionName>(<COLUMNmeter> <Datatype>) return <Datatype>;
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_AD_CODE             IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                    P_ORGANIZATION_ID     IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE,
                    P_LOCATION_ID         IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE,
                    P_ROW                 OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE,
                    P_IGNORE_NO_DATA      IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_AD_CODE             IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                  P_ORGANIZATION_ID     IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE,
                  P_LOCATION_ID         IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_LOCATION_ID IN VARCHAR2,
                  P_CALLING_OBJECT      IN VARCHAR2,
                  P_CALLING_USER        IN VARCHAR2,
                  P_CALLING_EVENT       IN VARCHAR2,
                  P_ROWID               OUT ROWID,
                  P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_AD_CODE             IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                    P_ORGANIZATION_ID     IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE,
                    P_LOCATION_ID         IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE,
                    P_ROW                 IN OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE,
                    P_UPDATE_NULL         IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_AD_CODE             IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                    P_ORGANIZATION_ID     IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE,
                    P_LOCATION_ID         IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEF_ALLOWANCE_DEDUCTION;
```

#### PAYROLL.PKG_DEF_SETUP
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_DEF_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Abdul Wadood
  -- Created : 01-Dec-2019 11:41
  -- Purpose : 
  -- Public type declarations
  --type <TypeName> is <Datatype>;
  -- Public constant declarations
  --<ConstantName> constant <Datatype> := <Value>;
  -- Public variable declarations
  --<VariableName> <Datatype>;
  -- Public function and procedure declarations
  --function <FunctionName>(<COLUMNmeter> <Datatype>) return <Datatype>;
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_CONSTANT_ID     IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                    P_LOCATION_ID     IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE,
                    P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                    P_ROW             OUT PAYROLL.DEF_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CONSTANT_ID     IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                  P_LOCATION_ID     IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE,
                  P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_LOCATION_ID     IN VARCHAR2,
                  P_CALLING_OBJECT  IN VARCHAR2,
                  P_CALLING_USER    IN VARCHAR2,
                  P_CALLING_EVENT   IN VARCHAR2,
                  P_ROWID           OUT ROWID,
                  P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT PAYROLL.DEF_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CONSTANT_ID     IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                    P_LOCATION_ID     IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE,
                    P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                    P_ROW             IN OUT PAYROLL.DEF_SETUP%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CONSTANT_ID     IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE,
                    P_LOCATION_ID     IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE,
                    P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEF_SETUP;
```

#### PAYROLL.PKG_EMP_EXPENSE
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_EMP_EXPENSE IS
  /***********************************************************************************************
         OBJECTIVE := This package was created for Employee Expense entry/adjustments
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        07-AUG-2018   Shahid Jamal           1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ----------------------------------------------------------------
  -- Function to get AD Code specified against given parameters --
  ----------------------------------------------------------------
  FUNCTION GET_EXPENSE_AD_CODE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_EXPENSE_CODE      IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE)
    RETURN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE;
  ----------------
  TYPE ALL_DED_DATA IS RECORD(
    MRNO         REGISTRATION.PATIENT.MRNO%TYPE,
    START_DATE   PAYROLL.EMP_EXPENSE.START_DATE%TYPE,
    END_DATE     PAYROLL.EMP_EXPENSE.END_DATE%TYPE,
    EXPENSE_CODE PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE,
    AD_CODE      PAYROLL.DEF_EXPENSE.AD_CODE%TYPE,
    TRANS_DATE   PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.TRANS_DATE%TYPE,
    AMOUNT       PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    REMARKS      PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
    CLAIM_NO     PAYROLL.EMP_EXPENSE.CLAIM_NO%TYPE);
  -----------------------------------------------------------
  -- Tab declaration based on above mentioned Record Group --
  -----------------------------------------------------------
  TYPE ALL_DED_DATA_TAB IS TABLE OF ALL_DED_DATA;
  -----------------------------------------------------------------
  -- Function to get unclaimed expenses against given parameters --
  -----------------------------------------------------------------
  FUNCTION GET_UNCLAIMED_EXPENSES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_START_DATE        IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE,
                                  P_END_DATE          IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE)
    RETURN PAYROLL.PKG_EMP_EXPENSE.ALL_DED_DATA_TAB
    PIPELINED;
  --------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN TYPE WISE YEARLY PAID EXPENSES --
  --------------------------------------------------------------
  FUNCTION GET_ACC_TYPE_EXPENSE(P_YEAR_CODE PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                P_MRNO      PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                                P_TYPE      VARCHAR2) RETURN NUMBER;
  --------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN TYPE WISE YEARLY PAID EXPENSES --
  --------------------------------------------------------------
  FUNCTION GET_ACC_TYPE_EXPENSE(P_FROM_DATE PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                P_TO_DATE   PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE,
                                P_MRNO      PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                                P_TYPE      VARCHAR2) RETURN NUMBER;
  ----------------------------------------------------------------------------------------------------------
  -- This procedure will be used to generate counter no for expense no field of PAYROLL.EMP_EXPENSE table --
  ----------------------------------------------------------------------------------------------------------
  PROCEDURE GEN_EXPENSE_NO(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_TRAN_DATE         IN DATE,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                           P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_EXPENSE_NO        OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);
   ---------------------------
  -- POST EMP EXPENSE LIST --
  ---------------------------
  PROCEDURE INSERT_EMP_EXPENSE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_EXPENSE_LIST_ID   IN PAYROLL.EMP_EXPENSE_LIST_DTL.EXPENSE_LIST_ID%TYPE,
                                    P_MRNO              IN PAYROLL.EMP_EXPENSE_LIST_DTL.MRNO%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
END PKG_EMP_EXPENSE;
```

#### PAYROLL.PKG_EMP_FINANCIAL
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_EMP_FINANCIAL AUTHID CURRENT_USER AS
  /***********************************************************************************************
         OBJECTIVE := This Package will be used for the following purpose
                      In this package, all the procedures/functions related to
                      invoice data copy
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        13-Jul-2018   Shahid Jamal           1. Created this Package.
         2.0        28-Jun-2019   M. Ali Khubaib         2. Modifications
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ------------------------------------------------
  -- This function will return Employee NTN No. --
  ------------------------------------------------
  FUNCTION GET_EMPLOYEE_NTN(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN VARCHAR2;
  ----------------------------------------------------------
  -- This function will return Employee CURRENT tax setup --
  ----------------------------------------------------------
  FUNCTION GET_EMPLOYEE_TAX_SETUP(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION.CURRENT_AMOUNT%TYPE;

  -----------------------------------------------------------------------------------------------
  -- This function will return Basic salary of employee in default currency i.e. USA, AED, etc --
  -----------------------------------------------------------------------------------------------
  FUNCTION GET_BASIC_DEFAULT_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_DATE IN DATE) RETURN NUMBER;

  -----------------------------------------------------------------------------------
  -- This function will return Basic salary of employee in local currency i.e. PKR --
  -----------------------------------------------------------------------------------
  FUNCTION GET_BASIC_LOCAL_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_DATE IN DATE) RETURN NUMBER;

  -----------------------------------------------------------------------------------------------
  -- This function will return GROSS salary of employee in default currency i.e. USA, AED, etc --
  -----------------------------------------------------------------------------------------------
  FUNCTION GET_GROSS_DEFAULT_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_DATE IN DATE) RETURN NUMBER;
  FUNCTION GET_EXT_GROSS_DEF_CURR(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_DATE IN DATE) RETURN NUMBER;
FUNCTION GET_EXT_GROSS_DEF_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_DATE IN DATE) RETURN NUMBER;                                  
  -----------------------------------------------------------------------------------
  -- This function will return gross salary of employee in local currency i.e. PKR --
  -----------------------------------------------------------------------------------
  FUNCTION GET_GROSS_LOCAL_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_DATE IN DATE) RETURN NUMBER;
  ------------------------------------------------
  -- This function will return Employee cOST CENTER. --
  ------------------------------------------------
  FUNCTION GET_COST_CENTRE_ID(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN PAYROLL.DEF_EMP_FINANCIAL.COST_CENTRE_ID%TYPE;

  FUNCTION GET_ACTUAL_GROSS(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_DATE IN DATE) RETURN NUMBER;
  -----------------------------------------------------------------
  -- This function will return yes if an employee is daily wager --
  -----------------------------------------------------------------
  FUNCTION IS_DAILY_WAGER(P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE)
    RETURN BOOLEAN;
  ---------------------------------------------------
  -- This function will return Taxable LFA amount. --
  ---------------------------------------------------
  FUNCTION GET_EXCL_LFA_INTAX(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN PAYROLL.DEF_EMP_FINANCIAL.EXCL_LFA_INTAX%TYPE;
    --------------------------------------------------------
  -- This function will return alloance deduction rate. --
  --------------------------------------------------------
  FUNCTION GET_AD_DEFAULT_CURRENCY(P_MRNO    IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_AD_CODE IN PAYROLL.Def_Ad_Constant.AD_CODE%TYPE,
                                   P_DATE    IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
     --------------------------------------------------------
  -- This function will return EMPLOYEE TYPE. --
  --------------------------------------------------------                                  
  FUNCTION GET_EMPLOYEE_TYPE(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN VARCHAR2;
    
END PKG_EMP_FINANCIAL;
```

#### PAYROLL.PKG_EXPENSE_CLAIM
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_EXPENSE_CLAIM IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-OCT-2018   Shahid Jamal (8317)    1. Created this Package.
         1.1        26-NOV-2017   Farhan Akram           1. Expenses amount not calculated properly
         1.2        01-JUN-2020   Muhammad Ali Khubaib   1. Workflow Implementation
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ----------------------------------------------------------------
  -- Record type declaration for collection of EMP Expense Data --
  ----------------------------------------------------------------
  TYPE EMP_EXPENSE_REC IS RECORD(
    DOCUMENT_NO           PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
    VOUCHER_TYPE          PAYROLL.EMP_EXPENSE.VOUCHER_TYPE%TYPE,
    VOUCHER_NO            PAYROLL.EMP_EXPENSE.VOUCHER_NO%TYPE,
    EXPENSE_CODE          PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE,
    MRNO                  PAYROLL.EMP_EXPENSE.MRNO%TYPE,
    TRANS_DATE            PAYROLL.EMP_EXPENSE.TRANS_DATE%TYPE,
    CURRENT_GROSS         PAYROLL.EMP_EXPENSE.CURRENT_GROSS%TYPE,
    CURRENT_BASIC         PAYROLL.EMP_EXPENSE.CURRENT_BASIC%TYPE,
    CURRENT_LFA           PAYROLL.EMP_EXPENSE.CURRENT_LFA%TYPE,
    SELF_DEPEND           PAYROLL.EMP_EXPENSE.SELF_DEPEND%TYPE,
    DEPENDANT_MRNO        PAYROLL.EMP_EXPENSE.DEPENDANT_MRNO%TYPE,
    APPROVED_BY           PAYROLL.EMP_EXPENSE.APPROVED_BY%TYPE,
    AMOUNT                PAYROLL.EMP_EXPENSE.AMOUNT%TYPE,
    REMARKS               PAYROLL.EMP_EXPENSE.REMARKS%TYPE,
    CANCELLED             PAYROLL.EMP_EXPENSE.CANCELLED%TYPE,
    CANCELED_VOUCHER_TYPE PAYROLL.EMP_EXPENSE.CANCELED_VOUCHER_TYPE%TYPE,
    CANCELED_VOUCHER_NO   PAYROLL.EMP_EXPENSE.CANCELED_VOUCHER_NO%TYPE,
    LFA_DUE_DATE          PAYROLL.EMP_EXPENSE.LFA_DUE_DATE%TYPE,
    SERVICE_YEARS         PAYROLL.EMP_EXPENSE.SERVICE_YEARS%TYPE,
    BONUS_PERCENT         PAYROLL.EMP_EXPENSE.BONUS_PERCENT%TYPE,
    GROSS_BASIC           PAYROLL.EMP_EXPENSE.GROSS_BASIC%TYPE,
    JOINING_DATE          PAYROLL.EMP_EXPENSE.JOINING_DATE%TYPE,
    LONG_SERVICE_DATE     PAYROLL.EMP_EXPENSE.LONG_SERVICE_DATE%TYPE,
    LFA_ADJUST_NO         PAYROLL.EMP_EXPENSE.LFA_ADJUST_NO%TYPE,
    INCLUDE_IN_TAX        PAYROLL.EMP_EXPENSE.INCLUDE_IN_TAX%TYPE,
    ORGANIZATION_ID       PAYROLL.EMP_EXPENSE.ORGANIZATION_ID%TYPE,
    LOCATION_ID           PAYROLL.EMP_EXPENSE.LOCATION_ID%TYPE,
    CLAIM_NO              PAYROLL.EMP_EXPENSE.CLAIM_NO%TYPE);

  -- Ref Cursor --
  TYPE EMP_EXPENSE_REF IS REF CURSOR RETURN EMP_EXPENSE_REC;
  -- Associative Array --
  TYPE EMP_EXPENSE_TAB IS TABLE OF EMP_EXPENSE_REC INDEX BY BINARY_INTEGER;
  --------------------------------------------------------------------------
  -- This Procedure will be used to process claims into employee expenses --
  --------------------------------------------------------------------------
  PROCEDURE PROCESS_EMP_EXPENSE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CLAIM_NO          IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);
  ---------------------------------------------------------------------------------
  -- Record type for collection of project wise allowances deduction detail data --
  ---------------------------------------------------------------------------------
  TYPE ALL_DED_DET_PROJECT_REC IS RECORD(
    DOCUMENT_NO PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
    PROJECT_ID  PAYROLL.EXPENSE_CLAIM_PROJECT.PROJECT_ID%TYPE,
    PERCENTAGE  PAYROLL.EXPENSE_CLAIM_PROJECT.EXP_PERCENTAGE%TYPE,
    AMOUNT      PAYROLL.EMP_EXP_DET_PROJECT.AMOUNT%TYPE);
  --------------------------------------------------------------------------------
  -- table type for collection of project wise allowances deduction detail data --
  --------------------------------------------------------------------------------
  TYPE ALL_DED_DET_PROJECT_TAB IS TABLE OF ALL_DED_DET_PROJECT_REC;
  -----------------------------------------------------------------------------------------
  -- This procedure will be used to insert claim expenses into PAYROLL.EMP_EXPENSE Table --
  -----------------------------------------------------------------------------------------
  PROCEDURE INSERT_EMP_EXPENSE(P_BLOCK_DATA        IN OUT EMP_EXPENSE_TAB,
                               P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);

  --------------------------------------------------
  -- This procedure will used to calculate amount --
  --------------------------------------------------
  PROCEDURE CALCULATE_SLAB_AMOUNT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_CLIAM_NO          IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);
  -------------------------------------
  -- Function to get defualt slab id --
  -------------------------------------
  FUNCTION GET_DEFAULT_SLAB_ID(P_EXPENSE_TYPE_ID IN PAYROLL.DEF_EXPENSE_DETAIL_SLAB.EXPENSE_TYPE_ID%TYPE)
    RETURN PAYROLL.DEF_EXPENSE_DETAIL_SLAB.SLAB_ID%TYPE;

  -----------------------------------------
  -- Function to get department HOD MRNO --
  -----------------------------------------
  FUNCTION GET_DEPT_HOD_MRNO(P_MRNO IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;

  -----------------------------------------
  -- Function to get employee manager MRNO --
  -----------------------------------------
  FUNCTION GET_EMP_MNGR_MRNO(P_MRNO IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;

  --------------------------------------------------------------------
  -- Function to get runtime user from DEFINITIONS.EVENT_USER table --
  --------------------------------------------------------------------
  FUNCTION GET_USER_RUNTIME(P_EVENT_ID IN DEFINITIONS.EVENT.EVENT_ID%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;

  ---------------------------------------------------------------------------------------------------------
  -- This procedure will be used to generate counter no for claim no field of expense claim detail table --
  ---------------------------------------------------------------------------------------------------------
  PROCEDURE GEN_COUNTER_EXPENSE_CLAIM(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_CLAIM_NO          OUT PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
                                      P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT VARCHAR2);

  --------------------------------------------------------------------------------------------------------
  -- This procedure will be used to generate counter no for expense no field of PAYROLL.EMP_EXPENSE table --
  --------------------------------------------------------------------------------------------------------
  PROCEDURE GEN_EXPENSE_NO(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_TRAN_DATE         IN DATE,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                           P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_EXPENSE_NO        OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);
  FUNCTION GET_EVENT_DESC(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE;
FUNCTION GET_EVENT_LABEL(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.LABEL_DESC%TYPE;
FUNCTION GET_EVENT_COLOR(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.COLOR_CODE%TYPE;
  FUNCTION GET_EVENT_DESC(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                          P_WFE_NO   IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE)
    RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE;

  FUNCTION GET_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                        P_WFE_NO   IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE)
    RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE;

  FUNCTION GET_CURRENT_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE)
    RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE;

  FUNCTION GEN_WFE_NO(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE)
    RETURN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE;

  PROCEDURE GET_EXPENSE_WORKFLOW(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_EXPENSE_CODE      IN PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE,
                                 P_COST_CENTRE_ID    IN PAYROLL.DEF_EMP_FINANCIAL.COST_CENTRE_ID%TYPE DEFAULT NULL,
                                 P_WORKFLOW_REC      OUT RADIATION.PKG_WORKFLOW.T_WORKFLOW_REC,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);

  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE INITIALIZE_WORKFLOW(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CLAIM_NO          IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);

  PROCEDURE POST_WORKFLOW_EVENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CLAIM_NO          IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                P_EVENT_ID          IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                                P_WORKFLOW_REMARKS  IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.REMARKS%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);

  PROCEDURE PERFORM_EVENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_CLAIM_NO          IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                          P_EVENT_ID          IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                          P_USER_MRNO         IN VARCHAR2,
                          P_TERMINAL          IN VARCHAR2,
                          P_OBJECT_CODE       IN VARCHAR2,
                          P_ALERT_TEXT        OUT VARCHAR2,
                          P_STOP              OUT CHAR);
  PROCEDURE PROCESS_SMS_ALERT(P_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_CLAIM_NO      IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                              P_NEXT_EVENT_ID IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.EVENT_ID%TYPE,
                              P_EVENT         IN VARCHAR2,
                              P_USER_MRNO     IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_OBJECT_CODE   IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_ALERT_TEXT    OUT VARCHAR2,
                              P_STOP          OUT VARCHAR2);
  ---------------------------------------------------------------
  -- FOLLOWING PRCEDURE WILL POPULATE QUEUE OF RELAVENT PERSON --
  ---------------------------------------------------------------
  PROCEDURE POPULATE_QUEUE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_CLAIM_NO          IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                           P_EVENT_ID          IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                           P_WFE_NO            IN PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q.WFE_NO%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);

  ----------------------------------------------------------------------------
  -- This fuction will return total number of documents attached with claim --
  ----------------------------------------------------------------------------
  FUNCTION GET_NO_OF_DOCUMENTS(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE)
    RETURN NUMBER;

  --------------------------------------------------------
  -- This fuction will return event id against claim no --
  --------------------------------------------------------
  FUNCTION CURRENT_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE)
    RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE;

  -- FUNCTION WILL RETURN HOD OF COST CENTRE
  FUNCTION GET_HOD_CC(P_COST_CENTRE IN MMS.COST_CENTRE_HEAD.SUB_LDGR_ITEM_CODE%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;

  ---------------------------------------------------------------
  -- This Function is used to return purchase type description --
  ---------------------------------------------------------------
  FUNCTION GET_NEXT_EVENT_ID(P_SCHEMA_ID        IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE,
                             P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE,
                             P_WORK_FLOW_ID     IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE,
                             P_EVENT_ID         IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE;

  ------------------------------------------------------
  -- This Procedure will show the EXPENSE CLAIM QUEUE --
  ------------------------------------------------------
  PROCEDURE EXPENSE_CLAIM_APPROVAL_Q(P_MRNO          IN VARCHAR2,
                                     P_ACTING_FOR    IN VARCHAR2,
                                     P_OBJECT_CODE   IN VARCHAR2,
                                     P_PROCESS_ID    IN VARCHAR2,
                                     P_TERMINAL      IN VARCHAR2,
                                     P_EVENT         IN VARCHAR2,
                                     P_ASSIGNMENT_ID IN NUMBER);

  --------------------------------------------------------------------------------------------
  -- This Function is used to return name of the employee in which claim request is pending --
  --------------------------------------------------------------------------------------------
  FUNCTION GET_IN_QUEUE_USERS(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE)
    RETURN VARCHAR2;

  --------------------------------------------------------------------------------
  -- This function will check the user is authorized to query all claims or not --
  --------------------------------------------------------------------------------
  FUNCTION QUERY_ALL_REC_GROUP(P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN NUMBER;

  ------------------------------------------------------------
  -- This Procedure is used to get SMS text from SMS Setup --
  ------------------------------------------------------------
  PROCEDURE GET_SMS_TEXT(P_SMS_ALERT_ID IN HIS.SMS_ALERT_SETUP.DESCRIPTION%TYPE,
                         P_SMS_TEXT     OUT HIS.SMS_ALERT_SETUP.SMS_TEXT%TYPE,
                         P_ALERT_TEXT   OUT VARCHAR2,
                         P_STOP         OUT CHAR);

  PROCEDURE LINK_POSTED_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_OLD_VOUCHER_TYPE  IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_TYPE%TYPE,
                                P_OLD_VOUCHER_NO    IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_NO%TYPE,
                                P_NEW_VOUCHER_TYPE  IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_TYPE%TYPE,
                                P_NEW_VOUCHER_NO    IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_NO%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
END PKG_EXPENSE_CLAIM;
```

#### PAYROLL.PKG_INCREMENT
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_INCREMENT IS
  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-AUG-2018   Farhan Akram(5156)     1. Created this Package.
         1.1        25-JUL-2019   Farhan Akram(5156)     1. Bug fixation
         1.2        18-JAN-2023   Farhan Akram(5156)     1. Adding INSERT_SETUP_AD
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ------------------------------------------------------
  -- Procedure to process increment based on proposal --
  ------------------------------------------------------
  PROCEDURE PROCESS_INCREMENT_PROPOSAL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_YEAR_CODE         IN HRD.INC_PROP_DETAIL.YEAR_CODE%TYPE,
                                       P_PROPOSAL_NO       IN HRD.INC_PROP_DETAIL.PROPOSAL_NO%TYPE,
                                       P_SERIAL_NO         IN HRD.INC_PROP_DETAIL.SERIAL_NO%TYPE,
                                       P_MRNO              IN HRD.INC_PROP_DETAIL.MRNO%TYPE,
                                       
                                       P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                       P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                       P_OBJECT_CODE    IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                       P_USER_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE,
                                       P_TERMINAL       IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                       P_ALERT_TEXT     OUT VARCHAR2,
                                       P_STOP           OUT VARCHAR2);
  -- following function is created for year wise ADDITIONAL GROSS sallary for incrment 2024
  FUNCTION GET_ADD_GROSS_FOR_INC(P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                 P_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN NUMBER;
  ---------------------------------------------------
  -- Procedure to update Unposted Claimed Expenses --
  ---------------------------------------------------
  PROCEDURE PROCESS_EMP_INCREMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                  P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                  P_INCREMENT_CODE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_CODE%TYPE,
                                  P_EFFECTIVE_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                  P_INC_AMOUNT        IN PAYROLL.EMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE,
                                  P_INC_PERCETAGE     IN PAYROLL.EMP_INCREMENT_MASTER.INCR_PERCENT%TYPE,
                                  P_INCREMENTED_GROSS IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
                                  P_REMARKS           IN PAYROLL.EMP_INCREMENT_MASTER.REMARKS%TYPE,
                                  P_ARREAR_PAID       IN PAYROLL.EMP_INCREMENT_MASTER.ARREAR_PAID%TYPE DEFAULT 'N',
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);
  -----------------------------------------------------
  -- Procedure to Rewise grade if need to be updated --
  -----------------------------------------------------
  PROCEDURE EMPLOYEE_GRADE_REVISION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                    P_INCREMENTED_GROSS IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
                                    P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
  -----------------------------------------------------
  -- Procedure to Rewise grade if need to be updated --
  -----------------------------------------------------
  PROCEDURE EMPLOYEE_GRADE_REVERT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                  P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);
  -----------------------------------------------------
  -- Procedure to Rewise grade if need to be updated --
  -----------------------------------------------------
  PROCEDURE PROCESS_INCREMENT_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                      P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                      P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT VARCHAR2);
  PROCEDURE REVERT_INCREMENT_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                     P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
  ----------------------------------------------------------------------
  -- Following function will calculate arrear amount based month days --
  ----------------------------------------------------------------------
  FUNCTION CALC_INCR_ARREAR_AMOUNT(P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                   P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                   P_INCR_AMOUNT    IN PAYROLL.EMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE)
    RETURN NUMBER;
  -----------------------------------------------------
  -- Procedure to Rewise grade if need to be updated --
  -----------------------------------------------------
  PROCEDURE PROCESS_PF_REVESION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                P_CURRENT_GROSS     IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
                                P_ARREAR_AMOUNT     IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
                                P_EFFECTIVE_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  PROCEDURE REVERT_PF_REVESION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                               P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                               P_EFFECTIVE_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);
  TYPE T_EMP_INC_DETAIL IS TABLE OF PAYROLL.EMP_INCREMENT_DETAIL%ROWTYPE INDEX BY BINARY_INTEGER;
  ------------------------------------------
  -- Procedure to insert increment detail --
  ------------------------------------------
  PROCEDURE GET_INCREMENT_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                 P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                 P_INC_DETAIL        OUT T_EMP_INC_DETAIL,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT VARCHAR2);
  PROCEDURE INSERT_INCREMENT_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO              PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                    P_INCREMENT_DATE    PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
  -------------------------------------------------------------------------
  -- This Procedure will sync def emp financial based on latest incremnt --
  -------------------------------------------------------------------------
  PROCEDURE SYNC_EMPLOYEE_FINANCIAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO            IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE,
                                    P_USER_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL        IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT      OUT VARCHAR2,
                                    P_STOP            OUT CHAR);
  PROCEDURE SYNC_EMPLOYEE_FINANCIAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO            IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE,
                                    P_NEW_JOINER      IN VARCHAR2,
                                    P_USER_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL        IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT      OUT VARCHAR2,
                                    P_STOP            OUT CHAR);
  ---------------------------------------------------------------
  -- This Procedure will validate the incrment processing date --
  ---------------------------------------------------------------
  PROCEDURE VALIDATE_INCREMENT_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO            IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE,
                                    P_INCREMENT_DATE  IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                    P_EFFECTIVE_DATE  IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                    P_ALERT_TEXT      OUT VARCHAR2,
                                    P_STOP            OUT CHAR);
  FUNCTION GET_BASIC_PERCENTAGE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE;
  FUNCTION GET_PF_PERCENTAGE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE;
  PROCEDURE REVERT_EMP_INCREMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                 P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                 P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT VARCHAR2);
  ---------------------------------------------------------------
  -- Following procedure will insert setup Allowance/Dedctions --
  ---------------------------------------------------------------
  PROCEDURE INSERT_SETUP_AD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_AD_CODE           PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                            P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                            P_AMOUNT            IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
                            P_FROM_DATE         IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.FROM_DATE%TYPE,
                            P_TO_DATE           IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.TO_DATE%TYPE,
                            P_REMARKS           IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
                            P_PROCESS_ID        IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE,
                            P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------
  -- Procedure to insert increment for allowances if required --
  --------------------------------------------------------------
  PROCEDURE INS_ALLOWANCE_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                  P_AD_CODE           IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE,
                                  P_AD_AMOUNT         IN PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE,
                                  P_INCREMENT_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                  P_EFFECTIVE_DATE    IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);
  FUNCTION GET_MIN_WAGE_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_DATE IN DATE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
  FUNCTION GET_INFLATION_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_DATE IN DATE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
  FUNCTION GET_MERIT_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_DATE IN DATE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
END PKG_INCREMENT;
```

#### PAYROLL.PKG_ITAX
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_ITAX AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        13-JUL-2018   Farhan Akram           Created this Package.
           1.1        11-JAN-2021   M.Ali Khubaib          Modifications.
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  -----------------------------------------------------
  -- This Function will return the yearly taxable pf --
  -----------------------------------------------------
  FUNCTION YEARLY_TAXABLE_PF(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             
                             P_YEAR_CODE NUMBER,
                             P_MRNO      VARCHAR2) RETURN NUMBER;

  FUNCTION YEARLY_TAXABLE_PF_V3(P_ORGANIZATION_ID      IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_LAST_PAY_EDATE       IN DATE,
                                P_CURR_MON_PFUND_AMT   IN NUMBER,
                                P_SEPRATE_CURR_MON_AMT IN VARCHAR2,
                                P_YEAR_CODE            IN NUMBER,
                                P_MRNO                 IN VARCHAR2)
    RETURN NUMBER;
  FUNCTION GET_YEARLY_PF_AMOUNT(P_ORGANIZATION_ID      IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_PAYROLL_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_LAST_PAY_EDATE       IN DATE,
                                P_CURR_MON_PF_AMOUNT   IN NUMBER,
                                P_SEPRATE_CURR_MON_AMT IN VARCHAR2,
                                P_YEAR_CODE            IN NUMBER,
                                P_MRNO                 IN VARCHAR2)
    RETURN NUMBER;
  FUNCTION CALC_MONTHLY_PF(P_ORGANIZATION_ID      IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_PAYROLL_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_LAST_PAY_EDATE       IN DATE,
                           P_CURR_MON_PF_AMOUNT   IN NUMBER,
                           P_SEPRATE_CURR_MON_AMT IN VARCHAR2,
                           P_YEAR_CODE            IN NUMBER,
                           P_MRNO                 IN VARCHAR2) RETURN NUMBER;
  -----------------------------------------------------
  -- This Function will return the yearly taxable pf --
  -----------------------------------------------------
  FUNCTION YEARLY_TAXABLE_PF_TEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_YEAR_CODE         NUMBER,
                                  P_MRNO              VARCHAR2) RETURN NUMBER;
  ----------------------------------------------------
  -- This Function will return other taxable amount --
  ----------------------------------------------------
  FUNCTION F_GET_EMP_OTHER_TAXABLE_AMOUNT(P_MRNO                   IN VARCHAR2,
                                          P_YEAR                   IN VARCHAR2,
                                          P_TAXABLE_AMOUNT_TYPE_ID IN VARCHAR2)
    RETURN NUMBER;

  TYPE T_ITAX_DTL_TAB IS TABLE OF NUMBER(15, 3) INDEX BY VARCHAR2(32);

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  PROCEDURE CALC_YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO               IN VARCHAR2,
                                    P_YEAR_CODE          IN VARCHAR2,
                                    P_LAST_MON_EDATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                    P_EXCHANGE_RATE      IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                    P_MONTHS_REMAIN      OUT NUMBER,
                                    P_INCOME_DTL         OUT T_ITAX_DTL_TAB,
                                    P_UP_LEAVES_AMOUNT   OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                    P_TOT_TAXABLE_AMOUNT OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT VARCHAR2);
  --------------------------------------------------
  -- This Function will get the total taxable pay TEST--
  --------------------------------------------------
  PROCEDURE CALC_YEARLY_TAXABLE_PAY_TEST(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                         P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_MRNO               IN VARCHAR2,
                                         P_YEAR_CODE          IN VARCHAR2,
                                         P_LAST_MON_EDATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                         P_EXCHANGE_RATE      IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                         P_MONTHS_REMAIN      OUT NUMBER,
                                         P_INCOME_DTL         OUT T_ITAX_DTL_TAB,
                                         P_UP_LEAVES_AMOUNT   OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                         P_TOT_TAXABLE_AMOUNT OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                         P_ALERT_TEXT         OUT VARCHAR2,
                                         P_STOP               OUT VARCHAR2);
  --------------------------------------------------
  -- This Function will get the total taxable pay NEW--
  --------------------------------------------------
  PROCEDURE CALC_YEARLY_TAXABLE_PAY_NEW(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_MRNO               IN VARCHAR2,
                                        P_YEAR_CODE          IN VARCHAR2,
                                        P_LAST_MON_EDATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                        P_EXCHANGE_RATE      IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                        P_CURR_NET_PAYABLE   IN NUMBER DEFAULT NULL,
                                        P_CURR_PFUND         IN NUMBER DEFAULT NULL,
                                        P_MONTHS_REMAIN      OUT NUMBER,
                                        P_INCOME_DTL         OUT T_ITAX_DTL_TAB,
                                        P_UP_LEAVES_AMOUNT   OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                        P_TOT_TAXABLE_AMOUNT OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                        P_ALERT_TEXT         OUT VARCHAR2,
                                        P_STOP               OUT VARCHAR2);

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  PROCEDURE CALC_PERIODICLE_TAXABLE_PAY(P_ORGANIZATION_ID        IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOGIN_LOCATION_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_MRNO                   IN VARCHAR2,
                                        P_START_DATE             IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                        P_END_DATE               IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                        P_PAID_ARREARS           OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_COA_BASED_EXPENSE OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_EXPENSES          OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_GROSS_PAY         OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_LFA_AMOUNT        OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_NIGHTS            OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_OTHER_ALLOWANCES  OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_OVERTIME          OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_PAID_PRACTICE_INCOME   OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_TAXABLE_PF_AMOUNT      OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_OTHER_TAXABLE_AMOUNT   OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                        P_ALERT_TEXT             OUT VARCHAR2,
                                        P_STOP                   OUT VARCHAR2);

  ------------------------------
  -- Record Type for Balances --
  ------------------------------
  TYPE PERIODICLE_TAXABLE_PAY_REC IS RECORD(
    MRNO               REGISTRATION.PATIENT.MRNO%TYPE,
    NAME               REGISTRATION.PATIENT.NAME%TYPE,
    GROSS              PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    PRACTICE_INCOME    PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    MONTHLY_TAXABLE_PF PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    LFA_PAID           PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    TAXABLE_EXPENSE    PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    OTHER_TAXABLE      PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    COA_BASED_EXPENSE  PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    TOTAL_INCOME       PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    TAX                PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE);

  --------------------------------------
  -- Associative Array / PL SQL Table --
  --------------------------------------
  TYPE PERIODICLE_TAXABLE_PAY_TAB IS TABLE OF PERIODICLE_TAXABLE_PAY_REC;

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION CALC_PERIODICLE_TAXABLE_PAY(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_MRNO              IN VARCHAR2,
                                       P_EMP_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_START_DATE        IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                       P_END_DATE          IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
  
   RETURN PERIODICLE_TAXABLE_PAY_TAB
    PIPELINED;

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_MRNO            IN VARCHAR2,
                              P_YEAR_CODE       IN VARCHAR2,
                              P_LAST_MON_EDATE  IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                              P_LOG             IN CHAR DEFAULT 'N')
    RETURN NUMBER;

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION YEARLY_TAXABLE_PAY_LEAVER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MRNO              IN VARCHAR2,
                                     P_SETTLEMENT_AMOUNT IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                     P_TRANS_DATE        IN DATE DEFAULT SYSDATE)
    RETURN NUMBER;
  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION YEARLY_TAXABLE_PAY_NEW(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO                IN VARCHAR2,
                                  P_YEAR_CODE           IN VARCHAR2,
                                  P_CURRENT_MON_PAYABLE IN NUMBER,
                                  P_CURRENT_MON_PFUND   IN NUMBER,
                                  P_LAST_MON_EDATE      IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                  P_LOG                 IN CHAR DEFAULT 'N')
    RETURN NUMBER;

  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION GET_YEARLY_TAXABLE_PAY(P_MRNO VARCHAR2, P_YEAR_CODE NUMBER)
    RETURN NUMBER;
  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION GET_YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO            IN VARCHAR2,
                                  P_YEAR_CODE       IN NUMBER) RETURN NUMBER;
  --------------------------------------------------
  -- This Function will get the total taxable pay --
  --------------------------------------------------
  FUNCTION GET_YEARLY_TAXABLE_PAY(P_MRNO           VARCHAR2,
                                  P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
    RETURN NUMBER;
  ---------------------------------------------------------
  FUNCTION GET_DIRECT_PAID_EXP_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_YEAR_CODE         IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                   P_FROM_DATE         IN FINANCE.GL_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                   P_TO_DATE           IN FINANCE.GL_FINANCIAL_YEAR.TO_DATE%TYPE,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN NUMBER;
  --------------------------------
  FUNCTION GET_YEARLY_PAID_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_YEAR_CODE         IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE)
    RETURN NUMBER;
  ---------------------------------
  FUNCTION GET_TAX_ADJUSTED_MONTHLY(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_YEAR_CODE         IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                    P_YEARLY_TAX        IN CHAR DEFAULT 'N')
    RETURN NUMBER;
  ----------------------
  FUNCTION GET_TAX_ADJUSTMENT_MONTHLY(P_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE)
    RETURN NUMBER;
  --------------------------------
  FUNCTION GET_PERIODICLE_PAID_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   --                                   P_YEAR_CODE         IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                   P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                   P_END_DATE   IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
    RETURN NUMBER;

  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CALCULATE MONTHLY TAX TO BE DEDUCTED --
  --------------------------------------------------------------
  PROCEDURE CALC_NEXT_MONTH_TAX_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_YEAR_CODE         IN NUMBER,
                                       P_MRNO              IN VARCHAR2,
                                       P_YEAR_TAX_DUE      IN NUMBER,
                                       P_EXCHANGE_RATE     IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                       P_MONTHS_REMAIN     IN NUMBER,
                                       P_TAX_PAID_SALARY   OUT NUMBER,
                                       P_TAX_PAID_DIRECT   OUT NUMBER,
                                       P_TAX_PAID_ADJUST   OUT NUMBER,
                                       P_TAX_PAID_TOTAL    OUT NUMBER,
                                       P_UNDISTRIBUTED_TAX OUT NUMBER,
                                       P_NEXT_MONTH_TAX    OUT NUMBER,
                                       P_ALERT_TEXT        OUT VARCHAR2,
                                       P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CALCULATE MONTHLY TAX TO BE DEDUCTED --
  --------------------------------------------------------------
  PROCEDURE CALC_NEXT_MONTH_TAX_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_YEAR_CODE         IN NUMBER,
                                       P_MRNO              IN VARCHAR2,
                                       P_YEAR_TAX_DUE      IN NUMBER,
                                       P_EXCHANGE_RATE     IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                       P_MONTHS_REMAIN     IN NUMBER,
                                       P_TAX_PAID_SALARY   OUT NUMBER,
                                       P_TAX_PAID_DIRECT   OUT NUMBER,
                                       P_TAX_PAID_ADJUST   OUT NUMBER,
                                       P_TAX_PAID_TOTAL    OUT NUMBER,
                                       P_NEXT_MONTH_TAX    OUT NUMBER,
                                       P_ALERT_TEXT        OUT VARCHAR2,
                                       P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CALCULATE MONTHLY TAX TO BE DEDUCTED TEST--
  --------------------------------------------------------------
  PROCEDURE CALC_NEXT_MONTH_TAX_DETAIL_TEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                            P_YEAR_CODE         IN NUMBER,
                                            P_MRNO              IN VARCHAR2,
                                            P_YEAR_TAX_DUE      IN NUMBER,
                                            P_EXCHANGE_RATE     IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                            P_MONTHS_REMAIN     IN NUMBER,
                                            P_TAX_PAID_SALARY   OUT NUMBER,
                                            P_TAX_PAID_DIRECT   OUT NUMBER,
                                            P_TAX_PAID_ADJUST   OUT NUMBER,
                                            P_TAX_PAID_TOTAL    OUT NUMBER,
                                            P_UNDISTRIBUTED_TAX OUT NUMBER,
                                            P_NEXT_MONTH_TAX    OUT NUMBER,
                                            P_ALERT_TEXT        OUT VARCHAR2,
                                            P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CALCULATE MONTHLY TAX TO BE DEDUCTED --
  --------------------------------------------------------------
  PROCEDURE CALC_NEXT_MONTH_TAX_DETAIL_TEST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                            P_YEAR_CODE         IN NUMBER,
                                            P_MRNO              IN VARCHAR2,
                                            P_YEAR_TAX_DUE      IN NUMBER,
                                            P_EXCHANGE_RATE     IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                            P_MONTHS_REMAIN     IN NUMBER,
                                            P_TAX_PAID_SALARY   OUT NUMBER,
                                            P_TAX_PAID_DIRECT   OUT NUMBER,
                                            P_TAX_PAID_ADJUST   OUT NUMBER,
                                            P_TAX_PAID_TOTAL    OUT NUMBER,
                                            P_NEXT_MONTH_TAX    OUT NUMBER,
                                            P_ALERT_TEXT        OUT VARCHAR2,
                                            P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CALCULATE MONTHLY TAX TO BE DEDUCTED --
  --------------------------------------------------------------
  PROCEDURE CALC_NEXT_MONTH_TAX_MONTHLY(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_YEAR_CODE          IN NUMBER,
                                        P_MRNO               IN VARCHAR2,
                                        P_YEAR_TAX_DUE       IN NUMBER,
                                        P_EXCHANGE_RATE      IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                        P_MONTHS_REMAIN      IN NUMBER,
                                        P_YEARLY_TAXABLE_PAY IN NUMBER,
                                        P_TAX_PAID_SALARY    OUT NUMBER,
                                        P_TAX_PAID_DIRECT    OUT NUMBER,
                                        P_TAX_PAID_ADJUST    OUT NUMBER,
                                        P_TAX_PAID_TOTAL     OUT NUMBER,
                                        P_UNDISTRIBUTED_TAX  OUT NUMBER,
                                        P_NEXT_MONTH_TAX     OUT NUMBER,
                                        P_ALERT_TEXT         OUT VARCHAR2,
                                        P_STOP               OUT VARCHAR2);
  -------------------------------------------------
  --  GET MIN TAX DEDUCTION FOR A FINANCIAL YEAR --
  -------------------------------------------------
  FUNCTION GET_MIN_TAX_DEDUCTION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_YEAR_CODE         IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE)
    RETURN PAYROLL.Pay_Financial_Year.MIN_TAX_DEDUCTION%TYPE;
  -------------------------------------------------
  --  GET MIN TAX DEDUCTION FOR A FINANCIAL YEAR --
  -------------------------------------------------
  FUNCTION GET_MIN_TAX_DEDUCTION(P_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE)
    RETURN PAYROLL.PAY_FINANCIAL_YEAR.MIN_TAX_DEDUCTION%TYPE;
  -----------------------------
  --  GET TAXABLE LFA AMOUNT --
  -----------------------------
  PROCEDURE GET_TAXABLE_LFA_AMOUNT(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MRNO                IN VARCHAR2,
                                   P_FIN_YEAR            IN PAYROLL.PAY_FINANCIAL_YEAR%ROWTYPE,
                                   P_MONTHS_REMAIN       IN NUMBER,
                                   P_PAID_LFA_AMOUNT     OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                   P_EXPECTED_LFA_AMOUNT OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
                                   P_ALERT_TEXT          OUT VARCHAR2,
                                   P_STOP                OUT VARCHAR2);
  FUNCTION GET_TAXABLE_LFA_AMOUNT(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO                IN VARCHAR2,
                                  P_FIN_YEAR            IN PAYROLL.PAY_FINANCIAL_YEAR%ROWTYPE,
                                  P_MONTHS_REMAIN       IN NUMBER)
    RETURN PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE;
  ----------------------------------------------------------
  -- this procedure will return tax based on anual income --
  ----------------------------------------------------------
  PROCEDURE GET_TAX_CALCULATION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_YEAR_CODE         IN NUMBER,
                                P_TAXABLE_AMOUNT    IN NUMBER,
                                P_GENDER            IN CHAR DEFAULT 'M',
                                P_TAX_AMOUNT        OUT NUMBER,
                                P_SLAB_BASE         OUT PAYROLL.DEF_ITAX_SLAB.BASE_TAX_AMOUNT%TYPE,
                                P_SLAB_PERCENT      OUT PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);
  ---------------------------------------------------
  -- This Function will return unpaid leave amount --
  ---------------------------------------------------
  FUNCTION GET_UNPAID_LEAVE_AMOUNT(P_MRNO      IN VARCHAR2,
                                   P_FROM_DATE IN DATE,
                                   P_TO_DATE   IN DATE) RETURN NUMBER;

  FUNCTION GET_TAX_SLAB_PERCENTAGE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_YEAR_CODE         IN NUMBER,
                                   P_TAXABLE_AMOUNT    IN NUMBER,
                                   P_GENDER            IN CHAR DEFAULT 'M')
    RETURN PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE;
  --------------------------------------------------------------------------------
  -- This Function will return percentage of salary days of employee in a month --
  --------------------------------------------------------------------------------
  FUNCTION GET_DAYS_PERCENTAGE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_MON_START_DATE    IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                               P_MON_END_DATE      IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                               P_MRNO              IN PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE)
    RETURN PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE;

  --------------------------------------------------
  -- This Function will get the total taxable pay for leaver--
  --------------------------------------------------
  PROCEDURE CALC_YEARLY_TAXABLE_PAY_LEAVER(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                           P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                           P_MRNO               IN VARCHAR2,
                                           P_YEAR_CODE          IN VARCHAR2,
                                           P_LAST_MON_EDATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                           P_EXCHANGE_RATE      IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE,
                                           P_LEAVER             IN BOOLEAN DEFAULT FALSE,
                                           P_SETTLEMENT_AMOUNT  IN NUMBER,
                                           P_MONTHS_REMAIN      OUT NUMBER,
                                           P_INCOME_DTL         OUT T_ITAX_DTL_TAB,
                                           P_UP_LEAVES_AMOUNT   OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                           P_TOT_TAXABLE_AMOUNT OUT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
                                           P_ALERT_TEXT         OUT VARCHAR2,
                                           P_STOP               OUT VARCHAR2);

  ------------------------------------------
  -- Purpose: RECALCULATE PENSION FUND AFTER SALARY CHANGE--
  ------------------------------------------

  PROCEDURE PENSION_FUND_CONTRIBUTION_RECAL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                            P_MRNO              IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                                            P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                            P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                            P_ADJUSTMENT_CODE   IN NUMBER,
                                            P_TERMINAL          IN VARCHAR2,
                                            P_USER_MRNO         IN VARCHAR2,
                                            P_ALERT_TEXT        OUT VARCHAR2,
                                            P_STOP              OUT VARCHAR2);

  ----------------------------------------------------
  -- This Procedure will post and unpost the record --
  ----------------------------------------------------
  PROCEDURE POST_PENSION_FUND_CONTRIBUTION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                           P_POST_UNPOST       IN CHAR,
                                           P_YEAR_CODE         IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE,
                                           P_START_DATE        IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE,
                                           P_END_DATE          IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE,
                                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                           P_ADJUSTMENT_CODE   IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ADJUSTMENT_CODE%TYPE,
                                           P_CURRENT_INCOME    IN NUMBER,
                                           P_CURRENT_TAX       IN NUMBER,
                                           P_EXEMPT_AMOUNT     OUT NUMBER,
                                           P_OBJECT_CODE       IN VARCHAR2,
                                           P_TERMINAL          IN VARCHAR2,
                                           P_USER_MRNO         IN VARCHAR2,
                                           P_ALERT_TEXT        OUT VARCHAR2,
                                           P_STOP              OUT CHAR);

END PKG_ITAX;
```

#### PAYROLL.PKG_ITAX_EXEMPTION
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_ITAX_EXEMPTION AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PF Final Settlement
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        01-NOV-2021   FAHAD QADIR         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMP IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DESIGNATION     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    GRADE           DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    YEAR_CODE       PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE,
    FROM_DATE       DATE,
    TO_DATE         DATE,
    ADJUSTMENT_CODE PAYROLL.EMP_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE,
    ADJUSTMENT_DESC VARCHAR2(500),
    AMOUNT          NUMBER(20, 2),
    REMARKS         PAYROLL.EMP_ITAX_ADJUSTMENT.REMARKS%TYPE,
    CURRENT_TAX     PAYROLL.EMP_ITAX_ADJUSTMENT.CURRENT_TAX%TYPE,
    CURRENT_INCOME  PAYROLL.EMP_ITAX_ADJUSTMENT.CURRENT_INCOME%TYPE,
    POSTED          PAYROLL.EMP_ITAX_ADJUSTMENT.POSTED%TYPE,
    START_DATE      PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE,
    END_DATE        PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_EMP IS REF CURSOR RETURN REC_EMP;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_EMP IS TABLE OF REC_EMP INDEX BY BINARY_INTEGER;

  -----------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_ITAX_ADJUSTMENT --
  -----------------------------------------------------------
  PROCEDURE QUERY_EMP_ITAX(P_RESULT          IN OUT REF_EMP,
                           P_MRNO            IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_YEAR_CODE       IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.YEAR_CODE%TYPE,
                           P_START_DATE      IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE,
                           P_END_DATE        IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE,
                           P_ADJUSTMENT_CODE IN PAYROLL.DEF_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE);

  ------------------------------------------------------------
  -- This procedure will insert PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE INSERT_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE UPDATE_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE DELETE_ITAX(P_RESULT IN OUT TAB_EMP);

  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_ITAX_ADJUSTMENT --
  ----------------------------------------------------------
  PROCEDURE LOCK_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_ITAX_DETAIL IS RECORD(
    YEAR_CODE       PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE,
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    ADJUSTMENT_CODE PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ADJUSTMENT_CODE%TYPE,
    SRNO            PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.SRNO%TYPE,
    AMOUNT          PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.AMOUNT%TYPE,
    REMARKS         PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.REMARKS%TYPE,
    ENTRY_DATE      PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ENTRY_DATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_ITAX_DETAIL IS REF CURSOR RETURN REC_ITAX_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE ITAX_DETAIL_TAB IS TABLE OF REC_ITAX_DETAIL INDEX BY BINARY_INTEGER;

  ----------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M --
  ----------------------------------------------------------------
  ------------------------------------------
  -- This Procedure will the exempted tax --
  ------------------------------------------
  PROCEDURE CALCULATE_EXEMPTED_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_YEAR_CODE         IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_ADJUSTMENT_CODE   IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ADJUSTMENT_CODE%TYPE,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_CURRENT_INCOME    OUT NUMBER,
                                   P_CURRENT_TAX       OUT NUMBER,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);

  ----------------------------------------------------
  -- This Procedure will post and unpost the record --
  ----------------------------------------------------
  PROCEDURE POST_UNPOST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                        P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_POST_UNPOST       IN CHAR,
                        P_YEAR_CODE         IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE,
                        P_START_DATE        IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE,
                        P_END_DATE          IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE,
                        P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                        P_ADJUSTMENT_CODE   IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ADJUSTMENT_CODE%TYPE,
                        P_CURRENT_INCOME    IN NUMBER,
                        P_CURRENT_TAX       IN NUMBER,
                        P_OBJECT_CODE       IN VARCHAR2,
                        P_TERMINAL          IN VARCHAR2,
                        P_USER_MRNO         IN VARCHAR2,
                        P_ALERT_TEXT        OUT VARCHAR2,
                        P_STOP              OUT CHAR);

END;
```

#### PAYROLL.PKG_LOAN
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_LOAN IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                           Description
         ---------  -----------   ---------------------------      ------------------------------
         1.0        01-Feb-2019   Muhammad Ali Khubaib (7033)      1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ----------------------
  TYPE PF_PROFIT_MEM_REC IS RECORD(
    YEAR_CODE          FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.PF_PROFIT_MEMBERS.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_PROFIT_MEMBERS.SUB_LDGR_ITEM_CODE%TYPE,
    PF_PROFIT          FINANCE.PF_PROFIT_MEMBERS.PF_PROFIT%TYPE);

  TYPE PF_PROFIT_MEM_TAB IS TABLE OF PF_PROFIT_MEM_REC;

  -----------------------------------------------------------
  -- Following function will fetch PF_Profit memebers data --
  -----------------------------------------------------------
  FUNCTION GET_PF_PROFIT_MEMBERS(P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE)
    RETURN PF_PROFIT_MEM_TAB
    PIPELINED;

  -------------------------------------------------------------------------------------------------
  -- This Procedure will insert the data of profit holder members into PAYROLL.PF_PROFIT_MEMBERS --
  -------------------------------------------------------------------------------------------------
  PROCEDURE INSERT_PF_PROFIT_MEMBERS(P_YEAR_CODE  IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                     P_PF_TYPE    IN VARCHAR2,
                                     P_ALERT_TEXT OUT VARCHAR2,
                                     P_STOP       OUT CHAR);

  -----------------------------------------------------------
  -- This function will return the file no against loan no --
  -----------------------------------------------------------
  FUNCTION GET_FILE_NO(P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE)
    RETURN FINANCE.GL_COA.COA_FILE_NO%TYPE;

  --------------------------------------------------------------------
  -- This function will check the employee is profit memeber or not --
  --------------------------------------------------------------------
  FUNCTION CHECK_PROFIT_MEMBER(P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN BOOLEAN;

  ---------------------------------------------------
  -- This function will check the loan is PF or GL --
  ---------------------------------------------------
  FUNCTION GET_LOAN_MODULE(P_LOAN_CODE       IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                           P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN VARCHAR2;

  -----------------------------------------------------
  -- This function will get file no agaist loan code --
  -----------------------------------------------------
  FUNCTION GET_FILE_NO(P_LOAN_CODE       IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                       P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                       P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE;

  ---------------------------------------------
  -- This function will return profit member --
  ---------------------------------------------
  FUNCTION IS_PROFIT_MEMBER(P_EMP_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_PF_TYPE   FINANCE.PF_PROFIT_MEMBERS.PF_TYPE%TYPE,
                            P_TRAN_DATE IN DATE)
    RETURN FINANCE.PF_PROFIT_MEMBERS.PF_PROFIT%TYPE;
  FUNCTION IS_PROFIT_MEMBER(P_EMP_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_PF_TYPE   IN FINANCE.PF_PROFIT_MEMBERS.PF_TYPE%TYPE,
                            P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE)
    RETURN FINANCE.PF_PROFIT_MEMBERS.PF_PROFIT%TYPE;
  ------------------------------------------------
  -- This function will return interest on loan --
  ------------------------------------------------
  FUNCTION IS_INTEREST_ON_LOAN(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_LOAN_CODE       IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE)
    RETURN PAYROLL.DEF_LOAN_TYPE.INTEREST%TYPE;
  ------------------------------------------------
  -- This function will return interest rate on loan --
  ------------------------------------------------
  FUNCTION GET_INTEREST_RATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_LOAN_CODE       IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                             P_YEAR_CODE       IN PAYROLL.DEF_LOAN_INTEREST_RATE.YEAR_CODE%TYPE)
    RETURN PAYROLL.DEF_LOAN_INTEREST_RATE.INTEREST_RATE%TYPE;
  ---------------------------------------------------------
  -- This function will check receipt is required or not --
  ---------------------------------------------------------
  FUNCTION IS_REFUND_THROUGH_RECEIPT(P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE)
    RETURN CHAR;

  -- ADD IN PAYROLL.PKG_LOAN
  PROCEDURE GEN_LOAN_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                        P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_TRAN_DATE       IN DATE,
                        P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                        P_TERMINAL        IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                        P_USER_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                        P_LOAN_NO         OUT PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                        P_ALERT_TEXT      OUT VARCHAR2,
                        P_STOP            OUT VARCHAR2);

  ---------------------------------------------------------------------------------
  -- This procedure will used to calculate loan interest amount and installments --
  ---------------------------------------------------------------------------------
  PROCEDURE CALCULATE_LOAN_INTEREST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_LOAN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_LOAN_CODE         IN PAYROLL.DEF_LOAN_INTEREST_RATE.LOAN_CODE%TYPE,
                                    P_LOAN_DATE         IN DATE,
                                    P_PRINCIPAL_AMOUNT  IN PAYROLL.LOAN_PAYMENT_INTEREST.PRINCIPAL_AMOUNT%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_INT_YEAR_CODE     OUT PAYROLL.DEF_LOAN_INTEREST_RATE.YEAR_CODE%TYPE,
                                    P_INTEREST_RATE     OUT PAYROLL.DEF_LOAN_INTEREST_RATE.INTEREST_RATE%TYPE,
                                    P_INT_NO_OF_MONTHS  OUT PAYROLL.LOAN_PAYMENT_INTEREST.NO_OF_MONTHS%TYPE,
                                    P_INTEREST_AMOUNT   OUT PAYROLL.LOAN_PAYMENT_INTEREST.INTEREST_AMOUNT%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
  PROCEDURE CALCULATE_LOAN_INTEREST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PRINCIPAL_AMOUNT  IN PAYROLL.LOAN_PAYMENT_INTEREST.PRINCIPAL_AMOUNT%TYPE,
                                    P_LOAN_INSTALLMENT  IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_INSTALLMENT%TYPE,
                                    P_INTEREST_RATE     IN PAYROLL.DEF_LOAN_INTEREST_RATE.INTEREST_RATE%TYPE,
                                    P_INT_NO_OF_MONTHS  OUT PAYROLL.LOAN_PAYMENT_INTEREST.NO_OF_MONTHS%TYPE,
                                    P_INTEREST_AMOUNT   OUT PAYROLL.LOAN_PAYMENT_INTEREST.INTEREST_AMOUNT%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
  -----------------------------------------------------
  -- This procedule is used to finalize loan PAYMENT --
  -----------------------------------------------------
  PROCEDURE FINALIZE_POST_LOAN_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOAN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_LOAN_NO           IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                       P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                       P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                       P_LOGIN_LOCATION_ID IN VARCHAR2,
                                       P_USER_MRNO         IN VARCHAR2,
                                       P_TERMINAL          IN VARCHAR2,
                                       P_OBJECT_CODE       IN VARCHAR2,
                                       P_ALERT_TEXT        OUT VARCHAR2,
                                       P_STOP              OUT CHAR);
  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan PAYMENT --
  ---------------------------------------------------------------------
  PROCEDURE FINALIZE_UNPOST_LOAN_PAYMENT(P_ORGANIZATION_ID        IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                         P_LOAN_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_LOAN_NO                IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                                         P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                         P_CANCELLED_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                         P_LOGIN_LOCATION_ID      IN VARCHAR2,
                                         P_USER_MRNO              IN VARCHAR2,
                                         P_TERMINAL               IN VARCHAR2,
                                         P_OBJECT_CODE            IN VARCHAR2,
                                         P_ALERT_TEXT             OUT VARCHAR2,
                                         P_STOP                   OUT CHAR);
  -------------------------------------------------------------
  -- This procedure will insert annual loan markups in Loans --
  -------------------------------------------------------------
  PROCEDURE POST_ANNUAL_LOAN_MARKUP(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                    P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                    P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                    P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                    P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_OBJECT_CODE       IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  -------------------------------------------------------------
  -- This procedure will insert pending loan markups in Loans --
  -------------------------------------------------------------
  PROCEDURE POST_DEFER_MARKUP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                      P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                      P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                      P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                      P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      P_USER_MRNO         IN VARCHAR2,
                                      P_TERMINAL          IN VARCHAR2,
                                      P_OBJECT_CODE       IN VARCHAR2,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT CHAR);
  -------------------------------------------------------------
  -- This procedure will cancel annual loan markups in Loans --
  -------------------------------------------------------------
  PROCEDURE CANCEL_LOAN_MARKUP(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                               P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ----------------------------------------------------------------------------
  -- This procedule is used to varify diferrent checks for loan eligibility --
  ----------------------------------------------------------------------------
  PROCEDURE CHECK_LOAN_ELIGIBILITY(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_LOAN_CODE         IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                                   P_MRNO              IN PAYROLL.LOAN_REFUND_MASTER_N.MRNO%TYPE,
                                   P_LOAN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_TRANS_DATE        IN PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);

  -------------------------------------------------------------------------------
  -- This function will return the number of days pasted after loan settlement --
  -------------------------------------------------------------------------------
  FUNCTION GET_LOAN_SETTLED_DAYS(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN NUMBER;

  ---------------------------------------------
  -- This procedule is used for loan reports --
  ---------------------------------------------
  PROCEDURE POPULATE_LOAN_TEMP_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_FROM_DATE       IN DATE,
                                    P_TO_DATE         IN DATE,
                                    P_FROM_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TO_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_FROM_LOAN_CODE  IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                    P_TO_LOAN_CODE    IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                    P_SUPRESS_ZERO    IN CHAR,
                                    P_USERID          IN CHAR,
                                    P_TERMINAL        IN CHAR,
                                    P_ALERT_TEXT      OUT VARCHAR2,
                                    P_STOP            OUT CHAR);
  PROCEDURE POPULATE_LOAN_TEMP_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_FROM_DATE       IN DATE,
                                    P_TO_DATE         IN DATE,
                                    P_FROM_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TO_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_FROM_LOAN_CODE  IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                    P_TO_LOAN_CODE    IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                    P_USERID          IN CHAR,
                                    P_TERMINAL        IN CHAR,
                                    P_ALERT_TEXT      OUT VARCHAR2,
                                    P_STOP            OUT CHAR);

  ---------------------------------------------
  -- This procedule is used for loan reports --
  ---------------------------------------------
  PROCEDURE POPULATE_TMP_LOAN_SUMMARY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_FROM_DATE       IN DATE,
                                      P_TO_DATE         IN DATE,
                                      P_FROM_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TO_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_FROM_LOAN_CODE  IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                      P_TO_LOAN_CODE    IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE,
                                      P_USERID          IN CHAR,
                                      P_TERMINAL        IN CHAR,
                                      P_ALERT_TEXT      OUT VARCHAR2,
                                      P_STOP            OUT CHAR);

  ---------------------------------------------
  -- This procedule is used for TRAVEL loan VOUCHER--
  ---------------------------------------------                                      
  PROCEDURE TRAVEL_LOAN_VOUCHER(P_MRNO             IN VARCHAR2,
                                P_REQUEST_NO       IN VARCHAR2,
                                P_LOAN_LOCATION_ID IN VARCHAR2,
                                P_ADVANCE_AMOUNT   IN NUMBER,
                                P_REMARKS          IN VARCHAR2,
                                P_VOUCHER_TYPE     IN VARCHAR2 DEFAULT 'BPV',
                                P_ALERT_TEXT       OUT VARCHAR2,
                                P_STOP             OUT CHAR);

END PKG_LOAN;
```

#### PAYROLL.PKG_LOAN_REFUND
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_LOAN_REFUND IS
  /***********************************************************************************************
         OBJECTIVE := This package contains Procedures  relavant to Loan Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        22-FEB-2019   Farhan Akram(5156)     1. Directed to create this Package.
         1.0        22-FEB-2019   Muhammad Farhan(7098)  1. Created this Package.
  ************************************************************************************************/
  ----------------------------------------------------
  -- This procedure will used to generate refund no --
  ----------------------------------------------------
  PROCEDURE GEN_REFUND_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_TRAN_DATE       IN DATE,
                          P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                          P_TERMINAL        IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                          P_USER_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_REFUND_NO       OUT PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                          P_ALERT_TEXT      OUT VARCHAR2,
                          P_STOP            OUT VARCHAR2);
  -------------------------------------------------------------------------------
  -- This procedure will used to insert data into PAYROLL.LOAN_INTEREST_DETAIL --
  -------------------------------------------------------------------------------
  PROCEDURE POPULATE_LOAN_INSTALLMENTS(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_MON_START_DATE      IN DATE,
                                       P_MON_END_DATE        IN DATE,
                                       P_PAY_START_DATE      IN DATE,
                                       P_PAY_END_DATE        IN DATE,
                                       P_OVERWRITE           IN CHAR,
                                       P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                       P_TERMINAL            IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                                       P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                       P_ALERT_TEXT          OUT VARCHAR2,
                                       P_STOP                OUT VARCHAR2);
  --------------------------------------------
  -- This procdure will create loan refunds --
  --------------------------------------------
  PROCEDURE POST_LOAN_REFUND(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID  IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                             P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                             P_PAY_START_DATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                             P_PAY_END_DATE       IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                             P_MRNO               IN HRD.INFORMATION.MRNO%TYPE,
                             P_OBJECT_CODE        IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_USER_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_TERMINAL           IN DEFINITIONS.TERMINALS.NAME%TYPE,
                             P_ALERT_TEXT         OUT VARCHAR2,
                             P_STOP               OUT VARCHAR2);
  --------------------------------------------
  -- This procdure will cancel loan refunds --
  --------------------------------------------
  PROCEDURE UNPOST_LOAN_REFUND(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID  IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                               P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                               P_PAY_START_DATE     IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                               P_PAY_END_DATE       IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                               P_MRNO               IN HRD.INFORMATION.MRNO%TYPE,
                               P_OBJECT_CODE        IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_USER_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_TERMINAL           IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT         OUT VARCHAR2,
                               P_STOP               OUT VARCHAR2);

  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan refund --
  ---------------------------------------------------------------------
  PROCEDURE FINALIZE_POST_LOAN_REFUND(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_REFUND_NO          IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                      P_VOUCHER_TYPE       IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                      P_VOUCHER_NO         IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      P_LOGIN_LOCATION_ID  IN VARCHAR2,
                                      P_USER_MRNO          IN VARCHAR2,
                                      P_TERMINAL           IN VARCHAR2,
                                      P_OBJECT_CODE        IN VARCHAR2,
                                      P_ALERT_TEXT         OUT VARCHAR2,
                                      P_STOP               OUT CHAR);
  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan refund --
  ---------------------------------------------------------------------
  PROCEDURE FINALIZE_UNPOST_LOAN_REFUND(P_ORGANIZATION_ID        IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_REFUND_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_REFUND_NO              IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                        P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                        P_CANCELLED_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                        P_LOGIN_LOCATION_ID      IN VARCHAR2,
                                        P_USER_MRNO              IN VARCHAR2,
                                        P_TERMINAL               IN VARCHAR2,
                                        P_OBJECT_CODE            IN VARCHAR2,
                                        P_ALERT_TEXT             OUT VARCHAR2,
                                        P_STOP                   OUT CHAR);
  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan refund --
  ---------------------------------------------------------------------
  PROCEDURE POST_LOAN_REFUND_OLD(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_REFUND_NO          IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                 P_VOUCHER_TYPE       IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO         IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                 P_LOGIN_LOCATION_ID  IN VARCHAR2,
                                 P_USER_MRNO          IN VARCHAR2,
                                 P_TERMINAL           IN VARCHAR2,
                                 P_OBJECT_CODE        IN VARCHAR2,
                                 P_ALERT_TEXT         OUT VARCHAR2,
                                 P_STOP               OUT CHAR);
  ------------------------------------------------------
  -- This procedule is used to unfinalize loan refund --
  ------------------------------------------------------
  PROCEDURE UNPOST_LOAN_REFUND_OLD(P_ORGANIZATION_ID        IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_REFUND_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_REFUND_NO              IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                   P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_CANCELLED_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_LOGIN_LOCATION_ID      IN VARCHAR2,
                                   P_USER_MRNO              IN VARCHAR2,
                                   P_TERMINAL               IN VARCHAR2,
                                   P_OBJECT_CODE            IN VARCHAR2,
                                   P_ALERT_TEXT             OUT VARCHAR2,
                                   P_STOP                   OUT CHAR);
 TYPE REFUND_REC IS RECORD(
 LOAN_NO         PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
 REFUND_AMOUNT   PAYROLL.LOAN_REFUND_DETAIL_N.REFUND_AMOUNT%TYPE);
 
 TYPE REFUND_TAB IS TABLE OF REFUND_REC INDEX BY BINARY_INTEGER;
 PROCEDURE GENERATE_REFUND(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID  IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                            P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE,
                            P_MRNO               IN HRD.INFORMATION.MRNO%TYPE,
                            P_MODULE             IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE,
                            P_LOAN_TAB           IN REFUND_TAB,
                            P_TEMP_POST          IN VARCHAR2,
                            P_REMARKS            IN PAYROLL.Loan_Refund_Master_N.REMARKS%TYPE,
                            P_VOUCHER_TYPE       IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                            P_VOUCHER_NO         IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                            P_OBJECT_CODE        IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_USER_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_TERMINAL           IN DEFINITIONS.TERMINALS.NAME%TYPE,
                            P_REFUND_NO          OUT PAYROLL.Loan_Refund_Master_n.REFUND_NO%TYPE,
                            P_ALERT_TEXT         OUT VARCHAR2,
                            P_STOP               OUT VARCHAR2);
END PKG_LOAN_REFUND;
```

#### PAYROLL.PKG_MONTH
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_MONTH AS

  /***********************************************************************************************
         OBJECTIVE := This package was created to get information related to payroll month
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                   Description
         ---------  -----------   ---------------------    -----------------------------------
         1.0        09-NOV-2018   M. Ali Khubaib (7033)    1. Created this Package.
         1.1        15-APR-2019   FARHAN AKRAM             1. ADDED SET MONTH PROCESS FLAG
         1.2        14-OCT-2019   M. Ali Khubaib (7033)    1. Added procedure GET_PROCESSED_PAY_MONTH
  ************************************************************************************************/
  ------------------------------------------------------------------------
  -- Following cursors will be used to fetch data for various functions --
  ------------------------------------------------------------------------
  CURSOR C_CURR_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) IS
    SELECT TRUNC(MON_START_DATE) AS START_DATE,
           TRUNC(MON_END_DATE) AS END_DATE,
           TRUNC(PAY_START_DATE) AS PAY_START_DATE,
           TRUNC(PAY_END_DATE) AS PAY_END_DATE,
           TO_NUMBER(TRUNC(TO_DATE(PAY_END_DATE, 'DD-MM-RRRR')) -
                     TRUNC(TO_DATE(PAY_START_DATE, 'DD-MM-RRRR'))) + 1,
           MONTH
      FROM DEFINITIONS.LOCATION_WISE_MONTHS M
     WHERE M.ORGANIZATION_ID = P_ORGANIZATION_ID
       AND M.LOCATION_ID = P_LOCATION_ID
       AND PAY_FLAG = 'Y';

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  --------------------------------------------------------------------------------------------
  -- This Procedure will be used to get master payroll location for an employee location id --
  --------------------------------------------------------------------------------------------
  PROCEDURE FETCH_PAYROLL_LOCATION_ID(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_EMP_LOCATION_ID     IN PAYROLL.DEF_PAYROLL_LOCATION.EMP_LOCATION_ID%TYPE,
                                      P_PAYROLL_LOCATION_ID OUT PAYROLL.DEF_PAYROLL_LOCATION.PAYROLL_LOCATION_ID%TYPE,
                                      P_ALERT_TEXT          OUT VARCHAR2,
                                      P_STOP                OUT VARCHAR2);
  --------------------------------------------------------------------------------------------
  -- This function will be used to get master payroll location for an employee location id --
  --------------------------------------------------------------------------------------------
  FUNCTION GET_CURRENT_PAY_MONTH(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;
  FUNCTION GET_PAYROLL_LOCATION_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOCATION_ID     IN PAYROLL.DEF_PAYROLL_LOCATION.EMP_LOCATION_ID%TYPE)
    RETURN PAYROLL.DEF_PAYROLL_LOCATION.PAYROLL_LOCATION_ID%TYPE;
  ----------------------------------------------------------------------
  -- Record type declaration for collection of current pay month data --
  ----------------------------------------------------------------------
  TYPE PAY_MONTH_REC IS RECORD(
    MON_START_DATE DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
    MON_END_DATE   DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
    PAY_START_DATE DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
    PAY_END_DATE   DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
    MONTH_DAYS     NUMBER,
    MONTH          DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE);

  -- User defined table declaration --
  TYPE PAY_MONTH_TAB IS TABLE OF PAYROLL.PKG_MONTH.PAY_MONTH_REC;

  --------------------------------------------------------------------------------
  -- This function will be used to get current month and pay start and end date --
  --------------------------------------------------------------------------------
  FUNCTION GET_CURRENT_PAY_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;

  --------------------------------------------------------------------------------
  -- This function will be used to get last month and pay start and end date --
  --------------------------------------------------------------------------------
  FUNCTION GET_LAST_PROCESSED_MON(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;
  --------------------------------------------------------------------------------
  -- This function will be used to get last month and pay start and end date --
  --------------------------------------------------------------------------------
  FUNCTION GET_LAST_PROCESSED_MON(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_FROM_DATE         IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                  P_TO_DATE           IN PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;
  ---------------------------------------------------------------------------------
  -- This Procedure will be used to get current month and pay start and end date --
  ---------------------------------------------------------------------------------
  PROCEDURE FETCH_CURRENT_PAY_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                    P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                    P_PAY_START_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                    P_PAY_END_DATE      OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                                    P_MONTH_DAYS        OUT NUMBER,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------
  -- This Procedure will be used to get current month and pay start and end date --
  ---------------------------------------------------------------------------------
  PROCEDURE FETCH_CURRENT_PAY_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                    P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                    P_PAY_START_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                    P_PAY_END_DATE      OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                                    P_MONTH_DAYS        OUT NUMBER,
                                    P_MONTH             OUT DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);

  --------------------------------------------------------------------
  -- This procedure will return Payroll Month against provided date --
  --------------------------------------------------------------------
  PROCEDURE FETCH_MONTH_DATES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_TRANS_DATE        IN DATE,
                              P_MONTH_START_DATE  OUT DATE,
                              P_MONTH_END_DATE    OUT DATE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);

  ----------------------------------------------------------------------------
  -- This procedure will return Practice Income Month against provided date --
  ----------------------------------------------------------------------------
  PROCEDURE FETCH_PI_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_TRANS_DATE        IN DATE,
                           P_MONTH_START_DATE  OUT DATE,
                           P_MONTH_END_DATE    OUT DATE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);

  -----------------------------------------------------------------
  -- Following function will fetch last processed month end date --
  -----------------------------------------------------------------
  FUNCTION GET_LAST_MON_END_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE;
  -----------------------------------------------------------------
  -- Following function will fetch last processed month end date --
  -----------------------------------------------------------------
  FUNCTION GET_LAST_MON_END_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_FROM_DATE         IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                 P_TO_DATE           IN PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE;
  --------------------------------------------------
  -- This procedure will check month for updation --
  --------------------------------------------------
  PROCEDURE CHECK_MONTH_FOR_UPDATION(P_OBJECT_CODE IN VARCHAR2,
                                     P_EVENT       IN VARCHAR2,
                                     P_USER        IN VARCHAR2,
                                     P_EMP_CODE    IN VARCHAR2,
                                     P_AD_CODE     IN VARCHAR2,
                                     P_TRANS_DATE  IN DATE,
                                     P_START_DATE  IN DATE,
                                     P_END_DATE    IN DATE,
                                     P_ALERT_TEXT  OUT VARCHAR2,
                                     P_STOP        OUT VARCHAR2);

  -----------------------------------------------------------------------
  -- This Procedure will be used to get current month for pay voucher  --
  -----------------------------------------------------------------------
  PROCEDURE FETCH_VOUCHER_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                P_PAY_START_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                P_PAY_END_DATE      OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  --------------------------------------------------------------------------------
  -- This Procedure will be used to get next unprocessed month for pay voucher  --
  --------------------------------------------------------------------------------
  PROCEDURE FETCH_NEXT_UNPROCESSED_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                         P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                         P_PAY_START_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                         P_PAY_END_DATE      OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                                         P_ALERT_TEXT        OUT VARCHAR2,
                                         P_STOP              OUT VARCHAR2);

  ----------------------------------------------------------------------------------
  -- This function will be used to get processed month and pay start and end date --
  ----------------------------------------------------------------------------------
  FUNCTION GET_PROCESSED_PAY_MONTHS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;

  --------------------------------------------------------------------------------
  -- This function will be used to get current month and pay start and end date --
  --------------------------------------------------------------------------------
  FUNCTION GET_PROCESSED_PAY_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;
  ----------------------------------------------------------------------------------------
  -- This Procedure will be used to get last processed month and pay start and end date --
  ----------------------------------------------------------------------------------------
  PROCEDURE FETCH_LAST_PROCESSED_MON(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                     P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                                     P_PAY_START_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                     P_PAY_END_DATE      OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------
  -- This funcation will be used to check the processed salary --
  ---------------------------------------------------------------
  FUNCTION IS_PAY_PROCESSED(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_START_DATE        IN DATE,
                            P_END_DATE          IN DATE) RETURN BOOLEAN;

  -----------------------------------------------------------
  -- This Procedure will be used to get start and end date --
  -----------------------------------------------------------
  PROCEDURE FETCH_MONTH_DATES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_PAY_START_DATE    IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                              P_PAY_END_DATE      IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                              P_MONTH_START_DATE  OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                              P_MONTH_END_DATE    OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------
  -- This Procedure will be used set pay calucation date and status after execution of pay process --
  ---------------------------------------------------------------------------------------------------
  PROCEDURE SET_MONTH_PROCESS_FLAG(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MONTH             IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT VARCHAR2);

  ------------------------------------------------------------------------------------------------
  -- This Procedure will be used set pay calucation date and status after execution of pay post --
  ------------------------------------------------------------------------------------------------
  PROCEDURE SET_MONTH_POST_FLAG(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MONTH             IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  ------------------------------------------
  -- Following function will fetch  month --
  ------------------------------------------
  FUNCTION GET_MONTH_FROM_PAY_DATES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PAY_START_DATE    IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                                    P_PAY_END_DATE      IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE;

  ------------------------------------------
  -- Following function will fetch  month --
  ------------------------------------------
  FUNCTION GET_MONTH_FROM_MON_DATES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    
                                    P_MON_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                    P_MON_END_DATE   IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE;

  TYPE LOCATION_REC IS RECORD(
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE);
  TYPE LOCATION_TAB IS TABLE OF LOCATION_REC;

  ----------------------------------------------------------------------
  -- Record type declaration for collection of current pay month data --
  ----------------------------------------------------------------------
  TYPE PAY_ALL_MONTH_REC IS RECORD(
    MON_START_DATE DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
    MON_END_DATE   DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
    PAY_START_DATE DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
    PAY_END_DATE   DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
    MONTH_DAYS     NUMBER,
    MONTH          DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
    PAY_POST_DATE  DEFINITIONS.LOCATION_WISE_MONTHS.PAY_POST_DATE%TYPE,
    PAY_CALC_DATE  DEFINITIONS.Location_Wise_Months.PAY_CALC_DATE%TYPE,
    PAY_PROCESS    DEFINITIONS.LOCATION_WISE_MONTHS.PAY_PROCESS%TYPE,
    CURRENT_MONTH  DEFINITIONS.LOCATION_WISE_MONTHS.CURRENT_MONTH%TYPE,
    SHORT_DESC     DEFINITIONS.LOCATION_WISE_MONTHS.SHORT_DESC%TYPE,
    PAY_FLAG       DEFINITIONS.LOCATION_wISE_MONTHS.PAY_FLAG%TYPE);
  -- User defined table declaration --
  TYPE PAY_ALL_MONTH_TAB IS TABLE OF PAYROLL.PKG_MONTH.PAY_ALL_MONTH_REC;
  --------------------------------------------------------------------------
  -- This function will be used to get data of location_wise_months table --
  --------------------------------------------------------------------------
  FUNCTION GET_ALL_MONTHS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_ALL_MONTH_TAB
    PIPELINED;

  --------------------------------------------------
  -- Following function will fetch PAY_START_DATE --
  --------------------------------------------------
  FUNCTION GET_MON_START_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_MONTH             IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE;

  FUNCTION GET_MON_END_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_MONTH             IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE;
  FUNCTION GET_PAY_START_DATE(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_MONTH               IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE;
  FUNCTION GET_PAY_END_DATE(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_MONTH               IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE;
  --------------------------------------------------------------------
  -- This Procedure will be used to validate increment process date --
  --------------------------------------------------------------------
  PROCEDURE VALIDATE_INCREMENT_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    
                                    P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                                    P_ALERT_TEXT     OUT VARCHAR2,
                                    P_STOP           OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  -- This function will be used to get unprocessed months and pay start and end date --
  -------------------------------------------------------------------------------------
  FUNCTION GET_UNPROCESSED_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB
    PIPELINED;
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE FINALIZE_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_START_DATE  IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                               P_PAY_END_DATE    IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                               P_ALERT_TEXT      OUT VARCHAR2,
                               P_STOP            OUT CHAR);
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE REVERT_MONTH_FINALIZATION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_PAY_START_DATE  IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                      P_PAY_END_DATE    IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                      P_ALERT_TEXT      OUT VARCHAR2,
                                      P_STOP            OUT CHAR);
  -------------------------------------------------------
  -- THIS PROCEDURE WILL INSERT NEW ROW IN MONTH TABLE --
  -------------------------------------------------------
  PROCEDURE INSERT_NEXT_MONTH(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_NEXT_MONTH_DAY      IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                              P_NO_OF_MONTHS        IN NUMBER DEFAULT 1,
                              P_MONTH               OUT DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                              P_ALERT_TEXT          OUT VARCHAR2,
                              P_STOP                OUT CHAR);
  PROCEDURE INSERT_NEXT_MONTH(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_NEXT_MONTH_DAY    IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                              P_NO_OF_MONTHS      IN NUMBER DEFAULT 1,
                              P_MONTH             OUT DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);

  ------------------------------------------------
  -- Following function will fetch pay end date --
  ------------------------------------------------
  FUNCTION GET_PAY_END_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_MON_END_DATE      IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
    RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE;
  --------------------------------------------------------------------------
  -- Following function will return the no of days in month of given date --
  --------------------------------------------------------------------------
  FUNCTION GET_PAY_MONTH_DAYS(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_TRANS_DATE          IN DATE) RETURN NUMBER;
  --------------------------------------------------------------------------
  -- Following function will return the month descrition --
  --------------------------------------------------------------------------
  FUNCTION GET_MONTH_DESC(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_START_DATE      IN DATE,
                          P_END_DATE        IN DATE) RETURN VARCHAR2;
END PKG_MONTH;
```

#### PAYROLL.PKG_PAY
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PAY IS

  /******************************************************************************/
  -- AUTHOR    : MUHAMMAD USMAN TAHIR (7297)
  -- CREATED ON: 05-10-2018
  -- REVISIONS:
  --       Ver        Date          Author                   Description
  ---------  -----------   ---------------------    -----------------------------------
  --       1.0        14-FEB-2025   M. Abu bakar Khalid (17114)    1. Created Procedure(Populate_Cost_To_Company)
  /******************************************************************************/

  --------------------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN ALLOWNCES AND DEDUCTION GAINST GIVEN PARAMETERS  --
  --------------------------------------------------------------------------------
  FUNCTION GET_EMP_AD_AMOUNT(P_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_MRNO          IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                             P_START_DATE    IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE,
                             P_END_DATE      IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE,
                             P_AD_CODE       IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                             P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER;

  --------------------------------------------
  -- THIS FUNCTION WILL RETURN PAYMENT RATE --
  --------------------------------------------
  FUNCTION GET_PAYMENT_RATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_PAY_START_DATE  IN PAYROLL.PAY_ARREAR.START_DATE%TYPE,
                            P_PAY_END_DATE    IN PAYROLL.PAY_ARREAR.END_DATE%TYPE,
                            P_MRNO            IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                            P_ARREAR_TYPE     IN PAYROLL.DEF_ARREAR.AD_TYPE%TYPE,
                            P_ARREAR_CODE     IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE,
                            P_DAYS_HOURS      IN PAYROLL.ARREAR_DETAIL.DAYS_HOURS%TYPE,
                            P_AD_CODE         IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE)
    RETURN NUMBER;
  -------------------------------------------------------------------------
  -- This Function will return the PF account calculated in current month --
  -------------------------------------------------------------------------
  FUNCTION GET_EMP_PF_AMOUNT(P_PF_TYPE        IN VARCHAR2,
                             P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_PAY_START_DATE IN DATE,
                             P_PAY_END_DATE   IN DATE) RETURN NUMBER;

  -------------------------------------------------
  -- This Function will return the current gross --
  -------------------------------------------------
  FUNCTION GET_GROSS_PAYABLE(P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_PAY_START_DATE IN DATE,
                             P_PAY_END_DATE   IN DATE)
    RETURN PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE;

  -----------------------------------------------
  -- This Function will return the current net --
  -----------------------------------------------
  FUNCTION GET_NET_PAYABLE(P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE)
    RETURN PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE;

  PROCEDURE POPUATE_SALARY_SHEET(P_ORIGINAL_TEST   IN VARCHAR2,
                                 P_ORGANIZATION_ID IN VARCHAR2,
                                 P_LOCATION_ID     IN VARCHAR2,
                                 P_START_DATE      IN DATE,
                                 P_END_DATE        IN DATE,
                                 P_USER            IN CHAR,
                                 P_TERMINAL        IN CHAR);

  -----------------------------------------------
  -- This procedure will populate cost to company report --
  -----------------------------------------------                               
  PROCEDURE POPULATE_COST_TO_COMPANY(P_ORGANIZATION_ID IN VARCHAR2,
                                     P_LOCATION_ID     IN VARCHAR2,
                                     P_PAY_START_DATE  IN PAYROLL.R_COST_TO_COMPANY_TEMP.START_DATE%TYPE,
                                     P_PAY_END_DATE    IN PAYROLL.R_COST_TO_COMPANY_TEMP.END_DATE%TYPE,
                                     P_USER_MRNO       IN VARCHAR2,
                                     P_TERMINAL        IN VARCHAR2,
                                     P_ALERT_TEXT      OUT VARCHAR2,
                                     P_STOP            OUT VARCHAR2);

  -----------------------------------------------
  --  -- THIS Function  WILL RETURN PF VOUCHER AMOUNT  --
  -----------------------------------------------                               
  

  FUNCTION GET_PF_VOUCHER_AMOUNT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_MRNO              IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE,
                                 P_JOINING_DATE      IN DATE,
                                 P_PAY_END_DATE      IN DATE,
                                 P_TYPE              IN VARCHAR2 -- 'E' = Employee, 'S' = Society
                                 ) RETURN NUMBER;

END PKG_PAY;
```

#### PAYROLL.PKG_PAYROLL
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PAYROLL IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        11-SEP-2018   Shahid Jamal (8317)    1. Created this Package.
         2.0        09-NOV-2018   Muhammad Ali Khubaib   1. Modifications.
         2.1        03-SEP-2019   Farhan Akram           1. Removed Definitions.Month
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ----------------------------------------------------------------------------------
  -- Get Patient Mobile Number active for SMS at the time of patient registration --
  ----------------------------------------------------------------------------------
  FUNCTION GET_SMS_NUMBER(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN VARCHAR2;

  ------------------------------------------------------------------------------
  -- Procedure for Sending SMS to PATIENT --
  -- This Procedure will send the sms without checking any No. Used for HIS SMS
  ------------------------------------------------------------------------------
  PROCEDURE SEND_SMS(P_EVENT       IN VARCHAR2,
                     P_MRNO        IN VARCHAR2,
                     P_SMS_TXT     IN VARCHAR2,
                     P_USER_MRNO   IN VARCHAR2,
                     P_SR_NO       IN REGISTRATION.SCHEDULE.SR_NO%TYPE,
                     P_OBJECT_CODE IN VARCHAR2,
                     P_ALERT_TEXT  OUT VARCHAR2,
                     P_STOP        OUT CHAR);

  -----------------
  -- Process SMS --
  -----------------
  PROCEDURE PROCESS_SMS_ALERT(P_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_CLAIM_NO    IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                              P_EVENT       IN VARCHAR2,
                              P_USER_MRNO   IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_ALERT_TEXT  OUT VARCHAR2,
                              P_STOP        OUT VARCHAR2);

  ----------------------
  TYPE EMP_WISE_LOC_REC IS RECORD(
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  TYPE EMP_WISE_LOC_TAB IS TABLE OF EMP_WISE_LOC_REC;
  -----------------------------------------------------------------------------------------
  -- Following pipeline function will return all the linked locations of a login loction --
  -----------------------------------------------------------------------------------------
  FUNCTION GET_PAYROLL_LOC_GROUP(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN EMP_WISE_LOC_TAB
    PIPELINED;
  -----------------------------------------------------
  -- Following function will fetch employee location --
  -----------------------------------------------------
  FUNCTION GET_USER_LOCATIONS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_EMP_CODE          IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN EMP_WISE_LOC_TAB
    PIPELINED;

  -----------------------------------------------------
  -- Following function will fetch employee location --
  -----------------------------------------------------
  FUNCTION GET_EMPLOYEE_LOCATION(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN DEFINITIONS.LOCATION.LOCATION_ID%TYPE;
  --------------------------------------------------------------------
  -- Following function will fetch employee master payroll location --
  --------------------------------------------------------------------
  FUNCTION GET_PAYROLL_LOCATION(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN DEFINITIONS.LOCATION.LOCATION_ID%TYPE;
  -------------------------------------------------------------
  -- This Procedure will be used to varify environment setup --
  -------------------------------------------------------------
  PROCEDURE VARIFY_ENV_SETUP(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT VARCHAR2);

  --------------------------------------------------------------------------
  -- This Procedure will generate the EAR Indeminity Alert Pending Tasks --
  -- for Review from Authorities
  --------------------------------------------------------------------------
  PROCEDURE TRAVEL_REQUEST_APPROVAL(P_MRNO          IN VARCHAR2,
                                    P_ACTING_FOR    IN VARCHAR2,
                                    P_OBJECT_CODE   IN VARCHAR2,
                                    P_PROCESS_ID    IN VARCHAR2,
                                    P_TERMINAL      IN VARCHAR2,
                                    P_EVENT         IN VARCHAR2,
                                    P_ASSIGNMENT_ID IN NUMBER);

  ------------------------------------------------------------------
  -- Following function will fetch the current pay financial year --
  ------------------------------------------------------------------
  FUNCTION GET_CURRENT_PAY_FINANCIAL_YEAR(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE;

  --------------------------------------------------------------------
  -- This function will return the Loan description against Loan_code --
  --------------------------------------------------------------------
  FUNCTION GET_LOAN_DESCRIPTION(P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE)
    RETURN PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE;

  ------------------------------------------------------------
  -- This Function will return Currency short Description --
  ----------------------------------------------------------
  FUNCTION GET_CURRENCY_SHORT_DESC(P_CURRENCY_ID IN DEFINITIONS.CURRENCY.CURRENCY_ID%TYPE)
    RETURN DEFINITIONS.CURRENCY.MARKETING_SHORT_DESC%TYPE;
  -----------------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN ALLOWANCES AND DEDUCTIONS --
  -----------------------------------------------------------------
  TYPE T_AD_SETUP_REC IS RECORD(
    ORGANIZATION_ID        PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
    LOCATION_ID            PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
    AD_CODE                PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE,
    PATIENT_TYPE_ID        PAYROLL.DEF_AD_SETUP_PT.PATIENT_TYPE_ID%TYPE,
    DESCRIPTION            PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    SHORT_DESCRIPTION      PAYROLL.DEF_AD_SETUP.SHORT_DESCRIPTION%TYPE,
    AD_GROUP_CODE          PAYROLL.DEF_AD_SETUP.AD_GROUP_CODE%TYPE,
    ATTENDANCE_BASED       PAYROLL.DEF_AD_SETUP.ATTENDANCE_BASED%TYPE,
    AD_NATURE_TYPE_ID      PAYROLL.DEF_AD_SETUP.AD_NATURE_TYPE_ID%TYPE,
    ENTRY_TYPE             PAYROLL.DEF_AD_SETUP.ENTRY_TYPE%TYPE,
    CALCULATION_TYPE       PAYROLL.DEF_AD_SETUP.CALCULATION_TYPE%TYPE,
    CALC_PERCENTAGE        PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE,
    TAXABLE                PAYROLL.DEF_AD_SETUP.TAXABLE%TYPE,
    TAXABLE_ANNUALLY       PAYROLL.DEF_AD_SETUP.TAXABLE_ANNUALLY%TYPE,
    INCLUDE_IN_GROSS       PAYROLL.DEF_AD_SETUP.INCLUDE_IN_GROSS%TYPE,
    EXCLUDE_FROM_GROSS_PAY PAYROLL.DEF_AD_SETUP.EXCLUDE_FROM_GROSS_PAY%TYPE,
    ACTIVE                 PAYROLL.DEF_AD_SETUP.ACTIVE%TYPE,
    PERCENTAGE_SETUP_ID    PAYROLL.DEF_AD_SETUP.PERCENTAGE_SETUP_ID%TYPE,
    SLAB_ID                PAYROLL.DEF_AD_SETUP.SLAB_ID%TYPE);
  TYPE T_AD_SETUP_TAB IS TABLE OF T_AD_SETUP_REC INDEX BY BINARY_INTEGER;
  FUNCTION GET_AD_SETUP(P_ORGANIZATION_ID  IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                        P_LOCATION_ID      IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                        P_PATIENT_TYPE_ID  IN PAYROLL.DEF_AD_SETUP_PT.PATIENT_TYPE_ID%TYPE,
                        P_MRNO             IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE,
                        P_AD_TYPE          IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
                        P_AD_CODE          IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
                        P_ENTRY_TYPE       IN PAYROLL.DEF_AD_SETUP.ENTRY_TYPE%TYPE,
                        P_INCLUDE_IN_GROSS IN PAYROLL.DEF_AD_SETUP.INCLUDE_IN_GROSS%TYPE,
                        P_ACTIVE           IN PAYROLL.DEF_AD_SETUP.ACTIVE%TYPE)
    RETURN SYS_REFCURSOR;
  -----------------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN ALLOWANCES AND DEDUCTIONS --
  -----------------------------------------------------------------
  FUNCTION GET_AD_SETUP(P_ORGANIZATION_ID  IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                        P_LOCATION_ID      IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                        P_PATIENT_TYPE_ID  IN PAYROLL.DEF_AD_SETUP_PT.PATIENT_TYPE_ID%TYPE,
                        P_MRNO             IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE,
                        P_AD_TYPE          IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
                        P_ENTRY_TYPE       IN PAYROLL.DEF_AD_SETUP.ENTRY_TYPE%TYPE,
                        P_INCLUDE_IN_GROSS IN PAYROLL.DEF_AD_SETUP.INCLUDE_IN_GROSS%TYPE)
    RETURN SYS_REFCURSOR;
  -------------------------------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN PAYMENT PERCENTAGE FOR GIVEN LEAVE TYPE --
  -------------------------------------------------------------------------------
  FUNCTION GET_AD_PAYMENT_PERCENTAGE(P_ORGANIZATION_ID     IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                                     P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                                     P_AD_CODE             IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
                                     P_LEAVE_TYPE_ID       IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE)
    RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.PAYMENT_PERCENTAGE%TYPE;
  --------------------------------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN  LEAVE TYPE FOR A SEPECIFIC DAY IF EXISTS--
  --------------------------------------------------------------------------------
  FUNCTION GET_LEAVE_TYPE_ID(P_ORGANIZATION_ID     IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                             P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                             P_MRNO                IN VARCHAR2,
                             P_DATE                IN DATE)
    RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE;
  ----------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN  AD AMOUNT PER DAY --
  ----------------------------------------------------------
  FUNCTION GET_AD_RATE_PER_DAY(P_ORGANIZATION_ID     IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                               P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                               P_MRNO                IN VARCHAR2,
                               P_AD_CODE             IN PAYROLL.Def_Ad_Setup.AD_CODE%TYPE,
                               P_DATE                IN DATE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
  --------------------------------------------------------
  -- THIS FUNCTION WILL USED TO RETURN  GUARENTEE MONEY --
  --------------------------------------------------------
  FUNCTION CALC_GM(P_ORGANIZATION_ID     IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                   P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                   P_MRNO                IN VARCHAR2,
                   P_FROM_DATE           IN DATE,
                   P_TO_DATE             IN DATE)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
  FUNCTION CALC_CURR_MON_GM(P_MRNO IN VARCHAR2)
    RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE;
  ------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN FINANCIAL YEAR CODE FOR GIVER DATE --
  ------------------------------------------------------------------
  FUNCTION GET_FINACIAL_YEARCODE(P_DATE IN DATE)
    RETURN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE;
  --------------------------------------------------------------------
  -- This function will return the ad description against  AD_code --
  --------------------------------------------------------------------
  FUNCTION GET_AD_DESC(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                       P_LOCATION_ID     IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                       P_AD_CODE         IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE)
    RETURN PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE;
  ------------------------------------------------------------
  -- This function will return the ad type against  AD_code --
  ------------------------------------------------------------
  FUNCTION GET_AD_TYPE(P_AD_CODE IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE)
    RETURN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE;
  ------------------------------------------------------------
  -- This function will return the ad type DESC against  AD_code --
  ------------------------------------------------------------
  FUNCTION GET_AD_TYPE_DESC(P_AD_CODE IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE)
    RETURN VARCHAR2;
  -----------------------------------------------------------------
  -- This function will return if the arrears are added in gross --
  -----------------------------------------------------------------
  FUNCTION IS_ARREAR_IN_GROSS(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE)
    RETURN PAYROLL.DEF_SETUP.VALUE%TYPE;
  ------------------------------------------------
  --- This Function will get the Voucher Status --
  ------------------------------------------------
  FUNCTION GET_VOUCHER_STATUS(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)
    RETURN FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE;

  FUNCTION GET_spell_number(p_number IN NUMBER) RETURN VARCHAR2;

  ------------------------------------------------------------------------------
  -- This function will return true to process payroll for inactive employees --
  ------------------------------------------------------------------------------
  FUNCTION PROCESS_INACTIVE_EMP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN VARCHAR2;

  ----------------------
  TYPE INACTIVE_EMP_REC IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DESIGNATION     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    EMP_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE);

  TYPE INACTIVE_EMP_TAB IS TABLE OF INACTIVE_EMP_REC;

  --------------------------------------------------------------------------------------------------------------------------
  -- Following pipeline function will return all inactive employees for salary but their salary certificate was generated --
  --------------------------------------------------------------------------------------------------------------------------
  FUNCTION GET_INACTIVE_EMP_SAL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_MONTH             IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE,
                                P_MON_START_DATE    IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
                                P_MON_END_DATE      IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)
    RETURN INACTIVE_EMP_TAB
    PIPELINED;

END PKG_PAYROLL;
```

#### PAYROLL.PKG_PAYSCALE
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PAYSCALE IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Cash Refund
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        21-DEC-2018   HAYAT ULLAH (4862)       1. Created this Package.
         2.0        25-Jul-2019   Muhammad Ali Khubaib     2. Modifications.
  ************************************************************************************************/

  --------------------------------------
  -- Procedure will Process Pay Scale --
  --------------------------------------
  PROCEDURE GENERATE_PAYSCALE_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_YEAR_CODE         IN PAYROLL.DEF_PAYSCALE.YEAR_CODE%TYPE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
  -----------------------------------------------------------------------------------------
  -- this function will return patient type group id for patient(excluding defult group) --
  -----------------------------------------------------------------------------------------
  FUNCTION GET_PATIENT_TYPE_GROUP_ID(P_PATIENT_TYPE_ID IN HRD.INFORMATION.PATIENT_TYPE_ID%TYPE)
    RETURN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE;
  -----------------------------------------------------------------------------------------
  -- this function will return designation category id for patient(excluding defult group) --
  -----------------------------------------------------------------------------------------
  FUNCTION GET_DESIGNATION_CATEGORY_ID(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE)
    RETURN DEFINITIONS.DESIGNATION_CATEGORY.DESIGNATION_CATEGORY_ID%TYPE;
  -----------------------------------------------------------------------------------------
  -- this function will return designation category id for patient(excluding defult group) --
  -----------------------------------------------------------------------------------------
  FUNCTION GET_DESIGNATION_CATEGORY_LIST(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                                         P_MRNO           IN HRD.INFORMATION.MRNO%TYPE)
    RETURN SYS_REFCURSOR;
  ----------------------------------------------------------------
  -- this function will employee wise allowances and deductions --
  ----------------------------------------------------------------
  FUNCTION GET_EMP_SETUP_AD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN SYS_REFCURSOR;
  -------------------------------------------------------
  -- this function will employee wise gross allowances  --
  --------------------------------------------------------
  FUNCTION GET_EMP_GROSS_ALL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN SYS_REFCURSOR;
  -----------------------------------------------------------------------
  -- this function will return stage no for sepecified grade and date  --
  -----------------------------------------------------------------------
  FUNCTION GET_STAGE_NO(P_GRADE_ID IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE,
                        P_AMOUNT   IN PAYROLL.DEF_PAYSCALE_DETAIL.AMOUNT%TYPE,
                        P_DATE     IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE DEFAULT SYSDATE)
    RETURN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE;
  -------------------------------------------------------------
  -- this function will return stage no for sepecified MRNO  --
  -------------------------------------------------------------
  FUNCTION GET_EMP_CURR_STAGE_NO(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE;
  ----------------------------------------------------------------------------------
  -- this function will return max amount of stage for sepecified grade and date  --
  ----------------------------------------------------------------------------------
  FUNCTION GET_STAGE_MAX_AMOUNT(P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                P_GRADE_ID  IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE)
    RETURN PAYROLL.DEF_PAYSCALE.MAX_AMOUNT%TYPE;
  ----------------------------------------------------------------------------------------------------
  -- this procedure will return basic and personal pay amount for sepecified grade, stage and date  --
  ----------------------------------------------------------------------------------------------------
  PROCEDURE GET_PAYSCALE_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_YEAR_CODE       IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                P_GRADE_ID        IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE,
                                P_STAGE_NO        IN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE,
                                P_BASIC_AMOUNT    OUT PAYROLL.DEF_PAYSCALE_DETAIL.AMOUNT%TYPE,
                                P_PERSONAL_PAY    OUT PAYROLL.DEF_PAYSCALE_DETAIL.AMOUNT%TYPE,
                                P_ALERT_TEXT      OUT VARCHAR2,
                                P_STOP            OUT VARCHAR2);
  ----------------------------------------------------------------------------------
  -- this procedure will return ad amount from defined chart for sepecified date  --
  ----------------------------------------------------------------------------------
  PROCEDURE GET_AD_CHART_AMOUNT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PATIENT_TYPE_ID   IN HRD.INFORMATION.PATIENT_TYPE_ID%TYPE,
                                P_DESIGNATION_ID    IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                                P_GRADE_ID          IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE,
                                P_AD_CODE           IN PAYROLL.DEF_AD_CHART_DETAIL.AD_CODE%TYPE,
                                P_MRNO              IN HRD.INFORMATION.MRNO%TYPE,
                                P_DATE              IN DATE,
                                P_AMOUNT            OUT PAYROLL.DEF_AD_CHART_DETAIL.AMOUNT%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT VARCHAR2);

  -------------------------------------------------
  -- This procedure will return percentage value --
  -------------------------------------------------
  PROCEDURE GET_PERCENTAGE_VALUE(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_GRADE_ID            IN DEFINITIONS.GRADES.GRADE_ID%TYPE,
                                 P_DEFAULT_PERCENTAGE  IN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE,
                                 P_BASE_VALUE          IN PAYROLL.DEF_EMP_FINANCIAL.CURRENT_GROSS%TYPE,
                                 P_PERCENTAGE_SETUP_ID IN PAYROLL.DEF_PERCENTAGE_SETUP.PERCENTAGE_SETUP_ID%TYPE,
                                 P_AMOUNT              OUT PAYROLL.DEF_AD_CHART_DETAIL.AMOUNT%TYPE,
                                 P_ALERT_TEXT          OUT VARCHAR2,
                                 P_STOP                OUT VARCHAR2);
END PKG_PAYSCALE;
```

#### PAYROLL.PKG_PAY_PROCESS
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PAY_PROCESS AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        07-MAY-2018    Farhan Akram            Created this Package.
           2.0        08-AUG-2018    Muhammad Ali Khubaib    Added new procedure PIN_EMP_ARREARS
           2.1        28-JUN-2019    Muhammad Ali Khubaib    Modifications
           2.2        30-JUL-2019    Farhan Akram            bUG FIXATION.
           2.3        26-NOV-2019    Farhan Akram            Daily wager actual salary bug fixation.
           2.4        14-APR-2020    Muhammad Ali Khubaib    Added two new columns TOTAL_MINUTES and totalPERFORMED_TOTAL_MINUTES
                                                             in PAYROLL.PAY_DAILY_AD_TEST (Procedure: SUB_INS_ALL_DAILY_ALLDED)
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  FUNCTION GET_LEAVE_TYPE_FACTOR(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_LEAVE_TYPE_ID       IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE,
                                 P_AD_CODE             IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.AD_CODE%TYPE)
    RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.PAYMENT_PERCENTAGE%TYPE;
  -------------------------------------------------------------------------
  -- This Function will return the PF account calculated in current month --
  -------------------------------------------------------------------------
  FUNCTION GET_CURR_MONTH_PF_AMOUNT(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PF_TYPE             IN VARCHAR2,
                                    P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_PAY_START_DATE      IN DATE,
                                    P_PAY_END_DATE        IN DATE)
    RETURN NUMBER;
  TYPE CONSTANT_VALUE IS TABLE OF VARCHAR2(100) INDEX BY VARCHAR2(100);
  -------------------------------------------------------------------------
  -- This Function will return the Total income last month --
  -------------------------------------------------------------------------
  FUNCTION GET_TOTAL_INCOME_LAST_MON(P_PAY_START_DATE       IN DATE,
                                     P_MRNO                 IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                                     P_TAXABLE_GROSS        IN NUMBER,
                                     P_NEW_MONTH_TAXABLE_PF IN NUMBER)
    RETURN NUMBER;
  -------------------------------------------------------------------------
  -- This Function will return the Total TAX Paid last month --
  -------------------------------------------------------------------------
  FUNCTION GET_TAX_PAID_LAST_MONTH(P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE)
    RETURN NUMBER;
  --------------------------------------
  -- Purpose: Function CALCULATE LOAN --
  --------------------------------------
  PROCEDURE CALCULATE_PAYROLL(P_PAY_START_DATE     IN DATE,
                              P_PAY_END_DATE       IN DATE,
                              P_EMP_SAL_START_DATE IN OUT DATE,
                              P_EMP_SAL_END_DATE   IN OUT DATE,
                              P_SALCERMONTH        IN CHAR,
                              P_USERNAME           IN VARCHAR2,
                              P_TERMINAL           IN VARCHAR2,
                              P_ND_END_DATE        IN DATE,
                              P_ND_START_DATE      IN DATE,
                              P_PAY_MONTH_DAYS     IN NUMBER,
                              P_LOCATION_ID        IN VARCHAR2,
                              P_ORGANIZATION_ID    IN VARCHAR2,
                              P_STOP               OUT VARCHAR2,
                              P_ALERT_TEXT         OUT VARCHAR2);

  ----------------------------------------
  -- Purpose: Procedure For Post_Payroll--
  ----------------------------------------
  PROCEDURE POST_PAYROLL(P_PAY_START_DATE IN DATE,
                         P_PAY_END_DATE   IN DATE,
                         P_STOP           OUT VARCHAR2,
                         P_ALERT_TEXT     OUT VARCHAR2);
  ------------------------------------------
  -- Purpose: Procedure For uncalc_payroll--
  ------------------------------------------
  PROCEDURE UNCALC_PAYROLL(P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  ------------------------------------------
  -- Purpose: Procedure For unpost_payroll--
  ------------------------------------------
  PROCEDURE UNPOST_PAYROLL(P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);
  ------------------------------------------
  -- Purpose: ET_CAR_ALLOWANCE_MONTHLY--
  ------------------------------------------
  FUNCTION GET_NO_CASH_TAX_APPLICABLE(P_ORGANIZATION_ID     DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_PAYROLL_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_MRNO                IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE,
                                      P_END_DATE            IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE)
    RETURN NUMBER;
  ------------------------------------------
  -- Purpose: ET_CAR_ALLOWANCE_MONTHLY--
  ------------------------------------------
  PROCEDURE NO_CASH_TAX_APPLICABLE(P_ORGANIZATION_ID             IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_PAYROLL_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MRNO                        IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                                   P_PAY_START_DATE              IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                   P_PAY_END_DATE                IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                   P_MONTHS_REMAIN               IN NUMBER,
                                   P_CASH_TAX_APPLICABLE_MONTHLY OUT NUMBER,
                                   P_CASH_TAX_APPLICABLE_YEARLY  OUT NUMBER,
                                   p_REV_CURR_MON_NC_TAX         OUT NUMBER,
                                   P_ALERT_TEXT                  OUT VARCHAR2,
                                   P_STOP                        OUT VARCHAR2);

  
END PKG_PAY_PROCESS;
```

#### PAYROLL.PKG_PAY_VOUCHER
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PAY_VOUCHER AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        07-MAY-2018    Farhan Akram            Created this Package.
           2.0        27-JUN-2019    Muhammad Ali Khubaib    Modifications.
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE ADD_VOUCHER_REFERENCES(P_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_VOUCHER_TYPE   IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_OLD_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_NEW_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                   P_PAY_END_DATE   IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                   P_ALERT_TEXT     OUT VARCHAR2,
                                   P_STOP           OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_PAY_END_DATE   IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                P_VOUCHER_TYPE   IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO     IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_ALERT_TEXT     OUT VARCHAR2,
                                P_STOP           OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                      P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                      P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                      P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      P_TRANS_DATE        IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                      P_CURRENCY_ID       IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                      P_CURRENCY_RATE     IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                      P_REMARKS           IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                      P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_USER_MRNO         IN VARCHAR2,
                                      P_TERMINAL          IN VARCHAR2,
                                      P_OBJECT_CODE       IN VARCHAR2,
                                      P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                             P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                             P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                             P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                             P_LOGIN_LOCATION_ID IN VARCHAR2,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_OBJECT_CODE       IN VARCHAR2,
                             P_NEW_VOUCHER_NO    OUT VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);
  ---------------------------------------------------------------------
  -- This function will add get the maximum serial no in voucher     --
  ---------------------------------------------------------------------
  FUNCTION GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)
    RETURN NUMBER;
  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                               P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                               P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_LOGIN_LOCATION_ID IN VARCHAR2,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);

  /*****************************************************************
   Author    : MUHAMMAD ALI KHUBAIB (7033)
   Created on: 18-06-2019
   Purpose   : This Procedure will check GL/COA setup for voucher
  *****************************************************************/
  PROCEDURE CHECK_GL_SETUP(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                           P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);
  ------------------------------------------------------------
  -- This function will Y/N if pay voucher is posted or not --
  ------------------------------------------------------------
  FUNCTION IS_PAY_VOUCHER_POSTED(P_ORGANIZATION_ID  IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                                 P_LOCATION_ID      IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                                 P_PAY_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                 P_PAY_END_DATE     IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                 P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE)
    RETURN CHAR;

END PKG_PAY_VOUCHER;
```

#### PAYROLL.PKG_PF_VOUCHER
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PF_VOUCHER AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        07-MAY-2018    Farhan Akram            Created this Package.
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ---------------------------
  -- Voucher detail Record --
  ---------------------------
  TYPE TRAN_DETAIL_REC IS RECORD(
    DEBIT_CREDIT       CHAR(1),
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    IS_NEW             CHAR(1));

  TYPE TRAN_DETAIL_TAB IS TABLE OF TRAN_DETAIL_REC;
  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  FUNCTION GET_TRAN_DETAIL(P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                           P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE)
    RETURN SYS_REFCURSOR;
  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE GET_VOUCHER_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                               P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_RESULT            OUT SYS_REFCURSOR,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE ADD_VOUCHER_REFERENCES(P_LOCATION_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_TYPE     IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_OLD_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_NEW_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_PAY_START_DATE   IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                                   P_PAY_END_DATE     IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                                   P_ALERT_TEXT       OUT VARCHAR2,
                                   P_STOP             OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_PF_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                     P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                                     P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                                     P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                     P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                     P_TRANS_DATE        IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                                     P_CURRENCY_ID       IN FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
                                     P_CURRENCY_RATE     IN FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                     P_REMARKS           IN FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_USER_MRNO         IN VARCHAR2,
                                     P_TERMINAL          IN VARCHAR2,
                                     P_OBJECT_CODE       IN VARCHAR2,
                                     P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_PF_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                            P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                            P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                            P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                            P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                            P_LOGIN_LOCATION_ID IN VARCHAR2,
                            P_USER_MRNO         IN VARCHAR2,
                            P_TERMINAL          IN VARCHAR2,
                            P_OBJECT_CODE       IN VARCHAR2,
                            P_NEW_VOUCHER_NO    OUT VARCHAR2,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_PF_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                   P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                                   P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                                   P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_LOGIN_LOCATION_ID IN VARCHAR2,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_PF_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                              P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                              P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                              P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_LOGIN_LOCATION_ID IN VARCHAR2,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_OBJECT_CODE       IN VARCHAR2,
                              P_NEW_VOUCHER_TYPE  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  --------------------------------------------------------------------------
  -- THIS PROCEDURE IS COMMON WHICH WILL BE USED TO CANCEL ANY PF VOUCHER --
  --------------------------------------------------------------------------
  PROCEDURE CANCEL_PF_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_CANCEL_TRANS_DATE IN FINANCE.Pf_Tran_Master.TRANS_DATE%TYPE DEFAULT NULL,
                              P_LOGIN_LOCATION_ID IN VARCHAR2,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_OBJECT_CODE       IN VARCHAR2,
                              P_NEW_VOUCHER_TYPE  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  ------------------------------------------------------------
  -- This Procedure will generate PF voucher for given fund --
  ------------------------------------------------------------
  PROCEDURE GENERATE_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PF_TYPE         IN VARCHAR2,
                                P_START_DATE      IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_END_DATE        IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                P_ORIGINAL_TEMP   IN CHAR,
                                P_VOUCHER_TYPE    IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO      OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO       IN VARCHAR2,
                                P_TERMINAL        IN VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2,
                                P_STOP            OUT CHAR);
  ------------------------------------------------------------
  -- This Procedure will generate PF voucher for given fund --
  ------------------------------------------------------------
  PROCEDURE POST_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_VOUCHER_TYPE    IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                            P_VOUCHER_NO      IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                            P_TRANS_DATE      IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                            P_PF_TYPE         IN VARCHAR2,
                            P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_USER_MRNO       IN VARCHAR2,
                            P_TERMINAL        IN VARCHAR2,
                            P_ALERT_TEXT      OUT VARCHAR2,
                            P_STOP            OUT CHAR);
  ------------------------------------------------------------------------
  -- THIS PROCEDURE IS COMMON WHICH WILL BE USED TO POST ANY PF VOUCHER --
  ------------------------------------------------------------------------
  PROCEDURE POST_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_VOUCHER_TYPE    IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                            P_VOUCHER_NO      IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                            P_TRANS_DATE      IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                            P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_USER_MRNO       IN VARCHAR2,
                            P_TERMINAL        IN VARCHAR2,
                            P_NEW_VOUCHER_NO  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                            P_ALERT_TEXT      OUT VARCHAR2,
                            P_STOP            OUT CHAR);
  -------------------------------------------------------------------------
  -- This Function will return the PF account balance for the given year --
  -------------------------------------------------------------------------
  FUNCTION GET_FUND_BALANCE(P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                            P_PF_TYPE   IN VARCHAR2,
                            P_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN NUMBER;
  ------------------------------------------------------------
  -- This Procedure will generate PF voucher for given fund --
  ------------------------------------------------------------
  PROCEDURE PF_VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE        IN CHAR,
                                      P_FROM_VOUCHER_NO     IN CHAR,
                                      P_TO_VOUCHER_NO       IN CHAR,
                                      P_USERID              IN CHAR,
                                      P_FROM_DATE           IN DATE,
                                      P_TO_DATE             IN DATE,
                                      P_ORGANIZATION_ID     IN VARCHAR2,
                                      P_LOCATION_ID         IN VARCHAR2,
                                      P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO           IN VARCHAR2,
                                      P_TERMINAL            IN VARCHAR2,
                                      P_ALERT_TEXT          OUT VARCHAR2,
                                      P_STOP                OUT CHAR,
                                      P_FROM_NEW_VOUCHER_NO OUT CHAR,
                                      P_TO_NEW_VOUCHER_NO   OUT CHAR);
  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
  ---------------------------------------------------------------------
  -- This function will add get the maximum serial no in voucher     --
  ---------------------------------------------------------------------
  FUNCTION GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)
    RETURN NUMBER;
END PKG_PF_VOUCHER;
```

#### PAYROLL.PKG_PROFIT_VOUCHER
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_PROFIT_VOUCHER AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        07-MAY-2018    Farhan Akram            Created this Package.
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ---------------------------
  -- Voucher detail Record --
  ---------------------------
  TYPE TRAN_DETAIL_REC IS RECORD(
    DEBIT_CREDIT       CHAR(1),
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE);

  TYPE TRAN_DETAIL_TAB IS TABLE OF TRAN_DETAIL_REC;
  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE GET_VOUCHER_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                               P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                               P_PROFIT_RATIO      IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE,
                               P_ENTRY_TYPE        IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE,
                               P_LOAN_CODE         IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_RESULT            OUT SYS_REFCURSOR,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE ADD_VOUCHER_REFERENCES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                   P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                   P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                   P_PROFIT_RATIO      IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE,
                                   P_ENTRY_TYPE        IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE DEFAULT NULL,
                                   P_LOAN_CODE         IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE DEFAULT NULL,
                                   P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_OLD_VOUCHER_NO    IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_NEW_VOUCHER_NO    IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_PROFIT_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                         P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                         P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                         P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                         P_PROFIT_RATIO      IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE,
                                         P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                         P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                         P_TRANS_DATE        IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                                         P_CURRENCY_ID       IN FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
                                         P_CURRENCY_RATE     IN FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                         P_REMARKS           IN FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
                                         P_ENTRY_TYPE        IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE,
                                         P_LOAN_CODE         IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
                                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_USER_MRNO         IN VARCHAR2,
                                         P_TERMINAL          IN VARCHAR2,
                                         P_OBJECT_CODE       IN VARCHAR2,
                                         P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                         P_ALERT_TEXT        OUT VARCHAR2,
                                         P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_PROFIT_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_ENTRY_TYPE        IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_NEW_VOUCHER_NO    OUT VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_PROFIT_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                       P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                       P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                       P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                       P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                       P_LOGIN_LOCATION_ID IN VARCHAR2,
                                       P_USER_MRNO         IN VARCHAR2,
                                       P_TERMINAL          IN VARCHAR2,
                                       P_OBJECT_CODE       IN VARCHAR2,
                                       P_ALERT_TEXT        OUT VARCHAR2,
                                       P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_PROFIT_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                  P_YEAR_CODE         IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                  P_SERIAL_NO         IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_LOGIN_LOCATION_ID IN VARCHAR2,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_TYPE  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  ---------------------------------------------
  -- This function will return new serial no --
  ---------------------------------------------
  FUNCTION GET_SERIAL_NO(P_ORGANIZATION_ID  IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                         P_YEAR_CODE        IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE)
    RETURN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE;
END PKG_PROFIT_VOUCHER;
```

#### PAYROLL.PKG_S16APX00110
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16APX00110 IS
  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for FINAL SETTLEMENT
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        03-Sep-2025   Fahad Qadir           1. Created this Package.
  ************************************************************************************************/
  ------------------------------------------------------
  -- This procedure will POPULATE PAYROLL.FINAL_SETTLEMENT --
  ------------------------------------------------------
  PROCEDURE POPULATE_FINAL_SETTLEMENT(P_ORGANIZATION_ID          IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOGIN_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_MRNO                     IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_CLEARANCE_CERTIFICATE_ID IN HRD.EMP_CLEARANCE_CERTIFICATE.CLEARANCE_CERTIFICATE_ID%TYPE,
                                      P_CC_LOCATION_ID           IN HRD.EMP_CLEARANCE_CERTIFICATE.LOCATION_ID%TYPE,
                                      P_OBJECT_CODE              IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_USER_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL                 IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_ALERT_TEXT               OUT VARCHAR2,
                                      P_STOP                     OUT CHAR
                                      
                                      );
  ------------------------------------------------------
  -- This procedure will POPULATE PAYROLL.SALARY_ELEMENT --
  ------------------------------------------------------
  PROCEDURE POPULATE_SALARY_ELEMENT(P_MRNO                     IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_ORGANIZATION_ID          IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_FINAL_SETTLEMENT_ID      IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                    P_clearance_certificate_id IN PAYROLL.FINAL_SETTLEMENT.CLEARANCE_CERTIFICATE_ID%TYPE,
                                    P_OBJECT_CODE              IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_USER_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TERMINAL                 IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT               OUT VARCHAR2,
                                    P_STOP                     OUT CHAR
                                    
                                    );

  ------------------------------------------------------
  -- This Procedure use to get UNIT/VALUE/AMOUNT of element --
  ------------------------------------------------------

  FUNCTION GET_ELEMENT_VALUE(P_MRNO                     IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_clearance_certificate_id IN HRD.EMP_CLEARANCE_CERTIFICATE.CLEARANCE_CERTIFICATE_ID%TYPE,
                             P_ELEMENT                  IN PAYROLL.DEF_FS_ELEMENT.ELEMENT_CODE%TYPE)
    RETURN PAYROLL.FINAL_SETTLEMENT_ELEMENT.VALUE%TYPE;

  FUNCTION GET_ELEMENT_AMOUNT(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                              P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_ELEMENT             IN PAYROLL.DEF_FS_ELEMENT.ELEMENT_CODE%TYPE,
                              P_VALUE               IN PAYROLL.FINAL_SETTLEMENT_ELEMENT.VALUE%TYPE)
    RETURN PAYROLL.FINAL_SETTLEMENT_ELEMENT.AMOUNT%TYPE;

  ------------------------------------------------------
  -- This procedure will CALCULATE ELEMENT --
  ------------------------------------------------------
  PROCEDURE CALCULATE_ELEMENT(P_FINAL_SETTLEMENT_ID      IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                              P_MRNO                     IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_clearance_certificate_id IN PAYROLL.FINAL_SETTLEMENT.CLEARANCE_CERTIFICATE_ID%TYPE,
                              P_AMOUNT_INITIATE          IN VARCHAR2,
                              P_ORGANIZATION_ID          IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_OBJECT_CODE              IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_USER_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_TERMINAL                 IN DEFINITIONS.TERMINALS.NAME%TYPE,
                              P_ALERT_TEXT               OUT VARCHAR2,
                              P_STOP                     OUT CHAR
                              
                              );

  ------------------------------------------------------
  -- This procedure will CALCULATE INCOME TAX --
  ------------------------------------------------------
  PROCEDURE CALCULATE_INCOME_TAX(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                 P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                 P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                 P_ALERT_TEXT          OUT VARCHAR2,
                                 P_STOP                OUT CHAR
                                 
                                 );
  ----------------------------------------------------------------
  -- Record type declaration for collection of EMP Expense Data --
  ----------------------------------------------------------------
  TYPE EMP_EXPENSE_REC IS RECORD(
    DOCUMENT_NO           PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
    VOUCHER_TYPE          PAYROLL.EMP_EXPENSE.VOUCHER_TYPE%TYPE,
    VOUCHER_NO            PAYROLL.EMP_EXPENSE.VOUCHER_NO%TYPE,
    EXPENSE_CODE          PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE,
    MRNO                  PAYROLL.EMP_EXPENSE.MRNO%TYPE,
    TRANS_DATE            PAYROLL.EMP_EXPENSE.TRANS_DATE%TYPE,
    CURRENT_GROSS         PAYROLL.EMP_EXPENSE.CURRENT_GROSS%TYPE,
    CURRENT_BASIC         PAYROLL.EMP_EXPENSE.CURRENT_BASIC%TYPE,
    CURRENT_LFA           PAYROLL.EMP_EXPENSE.CURRENT_LFA%TYPE,
    SELF_DEPEND           PAYROLL.EMP_EXPENSE.SELF_DEPEND%TYPE,
    DEPENDANT_MRNO        PAYROLL.EMP_EXPENSE.DEPENDANT_MRNO%TYPE,
    APPROVED_BY           PAYROLL.EMP_EXPENSE.APPROVED_BY%TYPE,
    AMOUNT                PAYROLL.EMP_EXPENSE.AMOUNT%TYPE,
    REMARKS               PAYROLL.EMP_EXPENSE.REMARKS%TYPE,
    CANCELLED             PAYROLL.EMP_EXPENSE.CANCELLED%TYPE,
    CANCELED_VOUCHER_TYPE PAYROLL.EMP_EXPENSE.CANCELED_VOUCHER_TYPE%TYPE,
    CANCELED_VOUCHER_NO   PAYROLL.EMP_EXPENSE.CANCELED_VOUCHER_NO%TYPE,
    LFA_DUE_DATE          PAYROLL.EMP_EXPENSE.LFA_DUE_DATE%TYPE,
    SERVICE_YEARS         PAYROLL.EMP_EXPENSE.SERVICE_YEARS%TYPE,
    BONUS_PERCENT         PAYROLL.EMP_EXPENSE.BONUS_PERCENT%TYPE,
    GROSS_BASIC           PAYROLL.EMP_EXPENSE.GROSS_BASIC%TYPE,
    JOINING_DATE          PAYROLL.EMP_EXPENSE.JOINING_DATE%TYPE,
    LONG_SERVICE_DATE     PAYROLL.EMP_EXPENSE.LONG_SERVICE_DATE%TYPE,
    LFA_ADJUST_NO         PAYROLL.EMP_EXPENSE.LFA_ADJUST_NO%TYPE,
    INCLUDE_IN_TAX        PAYROLL.EMP_EXPENSE.INCLUDE_IN_TAX%TYPE,
    ORGANIZATION_ID       PAYROLL.EMP_EXPENSE.ORGANIZATION_ID%TYPE,
    LOCATION_ID           PAYROLL.EMP_EXPENSE.LOCATION_ID%TYPE,
    CLAIM_NO              PAYROLL.EMP_EXPENSE.CLAIM_NO%TYPE);

  -- Ref Cursor --
  TYPE EMP_EXPENSE_REF IS REF CURSOR RETURN EMP_EXPENSE_REC;
  -- Associative Array --
  TYPE EMP_EXPENSE_TAB IS TABLE OF EMP_EXPENSE_REC INDEX BY BINARY_INTEGER;

  --------------------------------------------------------------------------------------------------------
  -- This procedure will be used to generate counter no for expense no field of PAYROLL.EMP_EXPENSE table --
  --------------------------------------------------------------------------------------------------------
  PROCEDURE GEN_EXPENSE_NO(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_TRAN_DATE         IN DATE,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                           P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_EXPENSE_NO        OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------------------
  -- This Procedure will be used to process final settlement into employee expenses --
  --------------------------------------------------------------------------
  PROCEDURE PROCESS_EMP_EXPENSE(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_ALERT_TEXT          OUT VARCHAR2,
                                P_STOP                OUT VARCHAR2);
  -----------------------------------------------------------------------------------------
  -- This procedure will be used to insert final settlement into PAYROLL.EMP_EXPENSE Table --
  -----------------------------------------------------------------------------------------
  PROCEDURE INSERT_EMP_EXPENSE(P_BLOCK_DATA        IN OUT EMP_EXPENSE_TAB,
                               P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);

  -----------------------------------------
  -- Function to get department HOD MRNO --
  -----------------------------------------
  FUNCTION GET_DEPT_HOD_MRNO(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;
  -- FUNCTION WILL RETURN HOD OF COST CENTRE
  FUNCTION GET_HOD_CC(P_COST_CENTRE IN MMS.COST_CENTRE_HEAD.SUB_LDGR_ITEM_CODE%TYPE)
    RETURN REGISTRATION.PATIENT.MRNO%TYPE;

  FUNCTION GET_EVENT_LABEL(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.LABEL_DESC%TYPE;

  FUNCTION GET_EVENT_COLOR(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.COLOR_CODE%TYPE;

  FUNCTION GET_EVENT_DESC(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE;

  FUNCTION GET_EVENT_DESC(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                          P_WFE_NO              IN PAYROLL.FINAL_SETTLEMENT_WF.WFE_NO%TYPE)
    RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE;

  ---------------------------------------------------------------
  -- This Function is used to return purchase type description --
  ---------------------------------------------------------------
  FUNCTION GET_NEXT_EVENT_ID(P_SCHEMA_ID        IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE,
                             P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE,
                             P_WORK_FLOW_ID     IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE,
                             P_EVENT_ID         IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE)
    RETURN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE;

  FUNCTION GEN_WFE_NO(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE)
    RETURN PAYROLL.FINAL_SETTLEMENT_WF.WFE_NO%TYPE;

  PROCEDURE GET_FS_WORKFLOW(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_WORKFLOW_REC      OUT RADIATION.PKG_WORKFLOW.T_WORKFLOW_REC,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT CHAR);

  --------------------------------------------------------------------------------------------
  -- This Function is used to return name of the employee in which final settlement request is pending --
  --------------------------------------------------------------------------------------------
  FUNCTION GET_IN_QUEUE_USERS(P_FINAL_SETTLEMENT_ID PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE)
    RETURN VARCHAR2;
  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE INITIALIZE_WORKFLOW(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_FINAL_SETTLEMENT_ID PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_ALERT_TEXT          OUT VARCHAR2,
                                P_STOP                OUT CHAR);

  PROCEDURE POST_WORKFLOW_EVENT(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                P_EVENT_ID            IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                                P_WORKFLOW_REMARKS    IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.REMARKS%TYPE,
                                P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_ALERT_TEXT          OUT VARCHAR2,
                                P_STOP                OUT CHAR);

  PROCEDURE PERFORM_EVENT(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                          P_EVENT_ID            IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                          P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                          P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                          P_ALERT_TEXT          OUT VARCHAR2,
                          P_STOP                OUT CHAR);

  PROCEDURE PROCESS_SMS_ALERT(P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                              P_NEXT_EVENT_ID       IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.EVENT_ID%TYPE,
                              P_EVENT               IN VARCHAR2,
                              P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_ALERT_TEXT          OUT VARCHAR2,
                              P_STOP                OUT VARCHAR2);
  ---------------------------------------------------------------
  -- FOLLOWING PRCEDURE WILL POPULATE QUEUE OF RELAVENT PERSON --
  ---------------------------------------------------------------
  PROCEDURE POPULATE_QUEUE(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                           P_EVENT_ID            IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                           P_WFE_NO              IN PAYROLL.FINAL_SETTLEMENT_WF_Q.WFE_NO%TYPE,
                           P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                           P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_ALERT_TEXT          OUT VARCHAR2,
                           P_STOP                OUT CHAR);

  FUNCTION GET_PARAMETER_VALUE(P_SCHEMA_ID        IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE,
                               P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE,
                               P_WORK_FLOW_ID     IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE,
                               P_EVENT_ID         IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                               P_PARAMETER_TYPE   IN DEFINITIONS.EVENT_WISE_PARAMETER.PARAMETER_TYPE%TYPE)
    RETURN DEFINITIONS.EVENT_WISE_DETAIL.PARAMETER_VALUE%TYPE;

  -------------------------------------------------------------
  -- Check GL setup --
  -------------------------------------------------------------
  PROCEDURE CHECK_GL_SETUP(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                           P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                           P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_ALERT_TEXT          OUT VARCHAR2,
                           P_STOP                OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_PAY_VOUCHER(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE,
                                      P_VOUCHER_TYPE        IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                      P_VOUCHER_NO          IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      P_TRANS_DATE          IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                      P_CURRENCY_ID         IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                      P_CURRENCY_RATE       IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                      P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_REMARKS             IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                      P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TERMINAL            IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                      P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_NEW_VOUCHER_NO      OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                      p_new_voucher_type    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                      P_ALERT_TEXT          OUT VARCHAR2,
                                      P_STOP                OUT CHAR);

  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                             P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_NEW_VOUCHER_NO    OUT VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
END PKG_S16APX00110;
```

#### PAYROLL.PKG_S16APX00127
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16APX00127 AS

  PROCEDURE APPROVE_MONTH_CHANGE(P_ORGANIZATION_ID IN VARCHAR2,
                                 P_LOCATION_ID     IN VARCHAR2,
                                 P_REQUEST_NO      IN NUMBER,
                                 P_APPROVED_BY     IN VARCHAR2,
                                 P_STOP            OUT VARCHAR2,
                                 P_ALERT_TEXT      OUT VARCHAR2);

END PKG_S16APX00127;
```

#### PAYROLL.PKG_S16FRM00023
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00023 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL DISCHARGE
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                  Description
         ---------  -----------   --------------------    -----------------------------------
         1.0        28-JAN-2019   MUHAMMAD ALI KHUBAIB    1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PAY_TMP_BANK IS RECORD(
    BRANCH_ID          PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE,
    BRANCH_DESCRIPTION PAYROLL.PAY_TMP_BANK.BRANCH_DESCRIPTION%TYPE,
    BANK_ID            PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE,
    BANK_DESCRIPTION   PAYROLL.PAY_TMP_BANK.BANK_DESCRIPTION%TYPE,
    SELECTED           PAYROLL.PAY_TMP_BANK.SELECTED%TYPE,
    USERID             PAYROLL.PAY_TMP_BANK.USERID%TYPE,
    TERMINAL           PAYROLL.PAY_TMP_BANK.TERMINAL%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PAY_TMP_BANK IS REF CURSOR RETURN REC_PAY_TMP_BANK;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PAY_TMP_BANK IS TABLE OF REC_PAY_TMP_BANK INDEX BY BINARY_INTEGER;

  --------------------------------------------
  -- This procedure will query PAY_TMP_BANK --
  --------------------------------------------
  PROCEDURE QUERY_PAY_TMP_BANK(P_RESULT   IN OUT REF_PAY_TMP_BANK,
                               P_USERID   IN PAYROLL.PAY_TMP_BANK.USERID%TYPE,
                               P_TERMINAL IN PAYROLL.PAY_TMP_BANK.TERMINAL%TYPE);

  --------------------------------------------
  -- This procedure will update PAY_TMP_BANK --
  --------------------------------------------
  PROCEDURE UPDATE_PAY_TMP_BANK(P_RESULT IN OUT TAB_PAY_TMP_BANK);

  --------------------------------------------
  -- This procedure will lock PAY_TMP_BANK --
  --------------------------------------------
  PROCEDURE LOCK_PAY_TMP_BANK(P_RESULT IN OUT TAB_PAY_TMP_BANK);

  -------------------------------------------------------------
  -- This procedure will update select flag Y/N PAY_TMP_BANK --
  -------------------------------------------------------------
  PROCEDURE SELECT_PAY_TMP_BANK(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_SINGLE_ALL        IN CHAR,
                                P_BANK_ID           IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE,
                                P_BRANCH_ID         IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE,
                                P_USERID            IN SECURITY.USERS.USERID%TYPE,
                                P_SELECTED          IN PAYROLL.PAY_TMP_BANK.SELECTED%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);

  -----------------------------------------------
  -- This procedure will populate PAY_TMP_BANK --
  -----------------------------------------------
  PROCEDURE POPULATE_PAY_TMP_BANK(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_BANK_ID           IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE,
                                  P_FROM_BANK_CODE    IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE,
                                  P_FROM_BRANCH_CODE  IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE,
                                  P_TO_BANK_CODE      IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE,
                                  P_TO_BRANCH_CODE    IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE,
                                  P_USERID            IN SECURITY.USERS.USERID%TYPE,
                                  P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                  P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);

  -----------------------------------------------
  -- This procedure will show account breakups --
  -----------------------------------------------
  PROCEDURE PROC_SHOW_ACCOUNT_BREAKUPS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_FROM_DATE         IN DATE,
                                       P_TO_DATE           IN DATE,
                                       P_BANK_ID           IN DEFINITIONS.BANK.BANK_ID%TYPE,
                                       P_ONLINE_ACCOUNT    IN CHAR,
                                       P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                       P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                       P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                                       P_ALERT_TEXT        OUT VARCHAR2,
                                       P_STOP              OUT CHAR);

END;
```

#### PAYROLL.PKG_S16FRM00028
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00028 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL EMP ALLOWANCES AND DEDUCTION
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        15-Oct-2018   M. ALI KHUBAIB            1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE AD_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15),
    PAY_START_DATE    DATE,
    PAY_END_DATE      DATE,
    AD_CODE           PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
    AD_DESC           VARCHAR2(250));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE AD_REF IS REF CURSOR RETURN AD_REC;

  ------------------------------------------------------------------
  -- This procedure will query PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ------------------------------------------------------------------
  PROCEDURE QUERY_AD(P_RESULT           IN OUT AD_REF,
                     P_MONTH_START_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE,
                     P_MONTH_END_DATE   IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE,
                     P_AD_CODE          IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE AD_DETAIL_REC IS RECORD(
    MRNO          REGISTRATION.PATIENT.MRNO%TYPE,
    NAME          REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION   DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE         DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    START_DATE    PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE,
    END_DATE      PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE,
    AD_CODE       PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE,
    AD_CODE_DESC  PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    AD_TYPE       PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
    NO_OF_DAYS    PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.NO_OF_DAYS%TYPE,
    AMOUNT        PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    REMARKS       PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE,
    TRANS_DATE    PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.TRANS_DATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE AD_DETAIL_REF IS REF CURSOR RETURN AD_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE AD_DETAIL_TAB IS TABLE OF AD_DETAIL_REC INDEX BY BINARY_INTEGER;

  ------------------------------------------------------------------
  -- This procedure will query PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  ------------------------------------------------------------------
  PROCEDURE QUERY_PAYROLL_AD(P_RESULT      IN OUT AD_DETAIL_REF,
                             P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_START_DATE  IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE,
                             P_END_DATE    IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE,
                             P_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_AD_CODE     IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE,
                             P_ORDER_BY    IN VARCHAR2);

  -------------------------------------------------------------------
  -- This procedure will insert PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  -------------------------------------------------------------------
  PROCEDURE INSERT_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB);

  -------------------------------------------------------------------
  -- This procedure will update PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  -------------------------------------------------------------------
  PROCEDURE UPDATE_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB);

  -------------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  -------------------------------------------------------------------
  PROCEDURE DELETE_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB);

  -----------------------------------------------------------------
  -- This procedure will lock PAYROLL.ALLOWANCE_DEDUCTION_DETAIL --
  -----------------------------------------------------------------
  PROCEDURE LOCK_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB);

END;
```

#### PAYROLL.PKG_S16FRM00029
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00029 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL ARREARS
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        28-Sep-2018   M. ALI KHUBAIB            1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE ARREAR_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15),
    PAY_START_DATE    DATE,
    PAY_END_DATE      DATE,
    ARREAR_CODE       PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE,
    ARREAR_DESC       PAYROLL.DEF_ARREAR.DESCRIPTION%TYPE,
    ARREAR_TYPE       PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE ARREAR_REF IS REF CURSOR RETURN ARREAR_REC;

  -----------------------------------------------------
  -- This procedure will query PAYROLL.ARREAR_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_ARREARS(P_RESULT           IN OUT ARREAR_REF,
                          P_MONTH_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE,
                          P_MONTH_END_DATE   IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE,
                          P_MONTH            IN VARCHAR2,
                          P_ARREAR_CODE      IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE ARREAR_DETAIL_REC IS RECORD(
    MRNO              REGISTRATION.PATIENT.MRNO%TYPE,
    NAME              REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION       DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT        DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE             DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    LOCATION_ID       DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC     DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    START_DATE        PAYROLL.ARREAR_DETAIL.START_DATE%TYPE,
    END_DATE          PAYROLL.ARREAR_DETAIL.END_DATE%TYPE,
    ARREAR_START_DATE PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE,
    ARREAR_END_DATE   PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE,
    ARR_MONTH         VARCHAR2(20), --
    ARREAR_CODE       PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE,
    ARREAR_DESC       PAYROLL.DEF_ARREAR.DESCRIPTION%TYPE,
    ARREAR_TYPE       PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
    AD_CODE           PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE,
    AD_DESC           PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    AD_TYPE           PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
    DAYS_HOURS        PAYROLL.ARREAR_DETAIL.DAYS_HOURS%TYPE,
    AMOUNT            PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE,
    DED_DAYS_HOURS    PAYROLL.ARREAR_DETAIL.DED_DAYS_HOURS%TYPE,
    DED_AMOUNT        PAYROLL.ARREAR_DETAIL.DED_AMOUNT%TYPE,
    REMARKS           PAYROLL.ARREAR_DETAIL.REMARKS%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE ARREAR_DETAIL_REF IS REF CURSOR RETURN ARREAR_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE ARREAR_DETAIL_TAB IS TABLE OF ARREAR_DETAIL_REC INDEX BY BINARY_INTEGER;

  -----------------------------------------------------
  -- This procedure will query PAYROLL.ARREAR_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_PAYROLL_ARREARS(P_RESULT      IN OUT ARREAR_DETAIL_REF,
                                  P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_START_DATE  IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE,
                                  P_END_DATE    IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE,
                                  P_ARREAR_CODE IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE,
                                  P_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_AD_CODE     IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE,
                                  P_ORDER_BY    IN VARCHAR2);

  ------------------------------------------------------
  -- This procedure will insert PAYROLL.ARREAR_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB);

  ------------------------------------------------------
  -- This procedure will update PAYROLL.ARREAR_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB);

  ------------------------------------------------------
  -- This procedure will DELETE PAYROLL.ARREAR_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB);

  ----------------------------------------------------
  -- This procedure will lock PAYROLL.ARREAR_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB);

END;
```

#### PAYROLL.PKG_S16FRM00030
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00030 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL ARREARS
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        18-Feb-2022   Farhan Akram           1. Created this Package.
  ************************************************************************************************/
  PROCEDURE POST_AWARD_PAYMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_DOCUMENT_NO       IN PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);

  PROCEDURE GET_AMOUNTS(P_LOCATION_ID       IN PAYROLL.EMP_EXPENSE.LOCATION_ID%TYPE,
                        P_EMPLOYEE_NO       IN PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                        P_MRNO              IN PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                        P_EXPENSE_CODE      IN PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE,
                        P_JOINING_DATE      IN PAYROLL.EMP_EXPENSE.JOINING_DATE%TYPE,
                        P_CURRENT_GROSS     OUT PAYROLL.EMP_EXPENSE.CURRENT_GROSS%TYPE,
                        P_CURRENT_BASIC     OUT PAYROLL.EMP_EXPENSE.CURRENT_BASIC%TYPE,
                        P_CURRENT_LFA       OUT PAYROLL.EMP_EXPENSE.CURRENT_LFA%TYPE,
                        P_AMOUNT            OUT PAYROLL.EMP_EXPENSE.AMOUNT%TYPE,
                        P_LFA_DUE_DATE      OUT PAYROLL.EMP_EXPENSE.LFA_DUE_DATE%TYPE,
                        P_GROSS_BASIC       OUT PAYROLL.EMP_EXPENSE.GROSS_BASIC%TYPE,
                        P_BONUS_PERCENT     OUT PAYROLL.EMP_EXPENSE.BONUS_PERCENT%TYPE,
                        P_SERVICE_YEARS     OUT PAYROLL.EMP_EXPENSE.SERVICE_YEARS%TYPE,
                        P_LONG_SERVICE_DATE OUT PAYROLL.EMP_EXPENSE.LONG_SERVICE_DATE%TYPE,
                        P_ALERT_TEXT        OUT VARCHAR2,
                        P_STOP              OUT CHAR);

  PROCEDURE VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE   IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_NO     IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_USERID         IN VARCHAR2,
                                   P_TRAN_DATE      IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                   P_DOCUMENT_NO    IN PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
                                   P_MRNO           IN PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                                   P_LFA_DUE_DATE   IN PAYROLL.EMP_EXPENSE.LFA_DUE_DATE%TYPE,
                                   P_NEW_VOUCHER_NO OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_ALERT_TEXT     OUT VARCHAR2,
                                   P_STOP           OUT CHAR);

  -----------------------------------------------------------
  -- This procedure will update reference no     --
  -----------------------------------------------------------
  PROCEDURE UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO      IN CHAR,
                                     P_VOUCHER_TYPE    IN CHAR,
                                     P_NEW_VOUCHER_NO  IN CHAR,
                                     P_OBJECT_CODE     IN CHAR,
                                     P_STOP            OUT CHAR,
                                     P_ALERT_TEXT      OUT VARCHAR2);
END;
```

#### PAYROLL.PKG_S16FRM00031
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00031 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL EMPLOYEE INCREMENT
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        11-MAR-2021   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_INCREMENT_MASTER IS RECORD(
    MRNO               REGISTRATION.PATIENT.MRNO%TYPE,
    EMPLOYEE_NAME      REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION        DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT         DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE              DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    JOINING_DATE       DATE,
    DAYILY_WAGER       PAYROLL.DEF_EMP_FINANCIAL.DAILY_WAGER%TYPE,
    INCREMENT_DATE     PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
    INCREMENT_CODE     PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_CODE%TYPE,
    INCR_DESC          PAYROLL.DEF_INCREMENT_TYPE.DESCRIPTION%TYPE,
    APPROVED_BY        REGISTRATION.PATIENT.MRNO%TYPE,
    APPROVED_BY_NAME   REGISTRATION.PATIENT.NAME%TYPE,
    INCR_AMOUNT        PAYROLL.EMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE,
    INCR_PERCENT       PAYROLL.EMP_INCREMENT_MASTER.INCR_PERCENT%TYPE,
    CURRENT_BASIC      PAYROLL.EMP_INCREMENT_MASTER.CURRENT_BASIC%TYPE,
    CURRENT_GROSS      PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
    REMARKS            PAYROLL.EMP_INCREMENT_MASTER.REMARKS%TYPE,
    INCREMENT_END_DATE PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_END_DATE%TYPE,
    PREVIOUS_BASIC     PAYROLL.EMP_INCREMENT_MASTER.PREVIOUS_BASIC%TYPE,
    PREVIOUS_GROSS     PAYROLL.EMP_INCREMENT_MASTER.PREVIOUS_GROSS%TYPE,
    POSTED             PAYROLL.EMP_INCREMENT_MASTER.POSTED%TYPE,
    EFFECTIVE_DATE     PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
    ARREAR_PAID        PAYROLL.EMP_INCREMENT_MASTER.ARREAR_PAID%TYPE,
    PROCESS_ID         PAYROLL.EMP_INCREMENT_MASTER.PROCESS_ID%TYPE,
    ACTIVE             CHAR(1),
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    EMPLOYEE_TYPE      DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_INCREMENT_MASTER IS REF CURSOR RETURN REC_INCREMENT_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_INCREMENT_MASTER IS TABLE OF REC_INCREMENT_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_INCREMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE QUERY_INCREMENT_MASTER(P_RESULT     IN OUT REF_INCREMENT_MASTER,
                                   P_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_CURRENT    IN CHAR,
                                   P_EMP_ACTIVE IN CHAR);
  -------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE INSERT_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE UPDATE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE DELETE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_INCREMENT_MASTER --
  -----------------------------------------------------------
  PROCEDURE LOCK_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_INCREMENT_DETAIL IS RECORD(
    AD_CODE           PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
    AD_DESC           PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    MRNO              REGISTRATION.PATIENT.MRNO%TYPE,
    INCREMENT_DATE    PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE,
    CURRENT_AMOUNT    PAYROLL.EMP_INCREMENT_DETAIL.CURRENT_AMOUNT%TYPE,
    PREVIOUS_AMOUNT   PAYROLL.EMP_INCREMENT_DETAIL.PREVIOUS_AMOUNT%TYPE,
    ORGANIZATION_ID   DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
    LOCATION_ID       DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    AD_NATURE_TYPE_ID PAYROLL.DEF_AD_SETUP.AD_NATURE_TYPE_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_INCREMENT_DETAIL IS REF CURSOR RETURN REC_INCREMENT_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE EMP_INCREMENT_DETAIL_TAB IS TABLE OF REC_INCREMENT_DETAIL INDEX BY BINARY_INTEGER;

  ------------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_INCREMENT_DETAIL --
  ------------------------------------------------------------
  PROCEDURE QUERY_INCREMENT_DETAIL(P_RESULT         IN OUT REF_INCREMENT_DETAIL,
                                   P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE,
                                   P_AD_CODE        IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE);
  ------------------------------------------------------------
  -- This procedure will insert PAYROLL.EMP_INCREMENT_DETAIL --
  ------------------------------------------------------------
  PROCEDURE INSERT_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_INCREMENT_DETAIL --
  -------------------------------------------------------------
  PROCEDURE UPDATE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_INCREMENT_DETAIL --
  -------------------------------------------------------------
  PROCEDURE DELETE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_INCREMENT_DETAIL --
  -----------------------------------------------------------
  PROCEDURE LOCK_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
END PKG_S16FRM00031;
```

#### PAYROLL.PKG_S16FRM00036
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00036 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for POST VOUCHER
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        27-Apr-2022   Fahad Qadir           1. Created this Package.
  ************************************************************************************************/

  PROCEDURE VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE        IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_FROM_VOUCHER_NO     IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_TO_VOUCHER_NO       IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_USERID              IN VARCHAR2,
                                   P_FROM_DATE           IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                   P_TO_DATE             IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                   P_FROM_NEW_VOUCHER_NO OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_TO_NEW_VOUCHER_NO   OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_ORGANIZATION_ID     IN VARCHAR2,
                                   P_LOCATION_ID         IN VARCHAR2,
                                   P_USER_MRNO           IN VARCHAR2,
                                   P_TERMINAL            IN VARCHAR2,
                                   P_ALERT_TEXT          OUT VARCHAR2,
                                   P_STOP                OUT CHAR);


  PROCEDURE UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO      IN CHAR,
                                     P_VOUCHER_TYPE    IN CHAR,
                                     P_NEW_VOUCHER_NO  IN CHAR,
                                     P_OBJECT_CODE     IN CHAR,
                                     P_STOP            OUT CHAR,
                                     P_ALERT_TEXT      OUT VARCHAR2);

END PKG_S16FRM00036;
```

#### PAYROLL.PKG_S16FRM00037
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00037 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        12-dec-2018   Farhan Akram           1. Created this Package.
         2.0        04-09-2019    M. Ali Khubaib         1. Modifications
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_MASTER IS RECORD(
    REFUND_NO              PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
    REFUND_DATE            PAYROLL.LOAN_REFUND_MASTER.TRANS_DATE%TYPE,
    MRNO                   PAYROLL.LOAN_REFUND_MASTER.MRNO%TYPE,
    NAME                   REGISTRATION.PATIENT.NAME%TYPE,
    REFUND_AMOUNT          PAYROLL.LOAN_REFUND_MASTER.REFUND_AMOUNT%TYPE,
    REFUND_REMARKS         PAYROLL.LOAN_REFUND_MASTER.REMARKS%TYPE,
    CANCELLED              PAYROLL.LOAN_REFUND_MASTER.CANCELLED%TYPE,
    CANCELLED_VOUCHER_TYPE PAYROLL.LOAN_REFUND_MASTER.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCELLED_VOUCHER_NO   PAYROLL.LOAN_REFUND_MASTER.CANCELLED_VOUCHER_NO%TYPE,
    REFUND_TYPE            PAYROLL.LOAN_REFUND_MASTER.REFUND_TYPE%TYPE,
    START_DATE             PAYROLL.LOAN_REFUND_MASTER.START_DATE%TYPE,
    END_DATE               PAYROLL.LOAN_REFUND_MASTER.END_DATE%TYPE,
    LOCATION_ID            DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    VOUCHER_TYPE           FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO             FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    VOUCHER_STATUS         FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_MASTER IS REF CURSOR RETURN REC_LOAN_REFUND_MASTER;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_MASTER IS TABLE OF REC_LOAN_REFUND_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will QUERY FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_MASTER(P_RESULT    IN OUT REF_LOAN_REFUND_MASTER,
                                     P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                     P_MRNO      IN PAYROLL.LOAN_REFUND_MASTER.MRNO%TYPE);
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------------------------------------------
  -- This procedure will DELETE LOAN_REFUND_MASTER --
  ------------------------------------------------------
  PROCEDURE DELETE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_DETAIL IS RECORD(
    REFUND_NO          PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
    LOAN_NO            PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
    LOAN_DATE          PAYROLL.LOAN_PAYMENT_MASTER.TRANS_DATE%TYPE,
    LOAN_TYPE          PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    REFUND_LOCATION    DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    LOAN_AMOUNT        PAYROLL.LOAN_PAYMENT_MASTER.LOAN_AMOUNT%TYPE,
    REFUND_AMOUNT      PAYROLL.LOAN_REFUND_DETAIL.REFUND_AMOUNT%TYPE,
    BALANCE            NUMBER(20, 2),
    TEMP_REFUND_AMOUNT PAYROLL.LOAN_REFUND_DETAIL.TEMP_REFUND_AMOUNT%TYPE,
    MRNO               PAYROLL.LOAN_REFUND_DETAIL.MRNO%TYPE,
    REFUND_LOCATION_ID PAYROLL.LOAN_REFUND_DETAIL.REFUND_LOCATION_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_DETAIL IS REF CURSOR RETURN REC_LOAN_REFUND_DETAIL;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_DETAIL IS TABLE OF REC_LOAN_REFUND_DETAIL INDEX BY BINARY_INTEGER;
  ----------------------------------------------------------
  -- This procedure will query PAYROLL.LOAN_REFUND_MASTER --
  ----------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_DETAIL(P_RESULT    IN OUT REF_LOAN_REFUND_DETAIL,
                                     P_MRNO      IN HRD.INFORMATION.MRNO%TYPE,
                                     P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE);

  --------------------------------------------------------------------
  -- This procedure will update PAYROLL.LOAN_REFUND_DETAIL --
  --------------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_DETAIL(P_RESULT    IN OUT TAB_LOAN_REFUND_DETAIL,
                                      P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE);
  --------------------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_REFUND_(MASTER/DETAIL) --
  --------------------------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_DETAIL(P_RESULT    IN OUT TAB_LOAN_REFUND_DETAIL,
                                    P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    REFUND_NO       PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    REFERENCE_NO    FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    PARTY_NAME      FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    PARTY_SUB_CODE  FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    MRNO            FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    LOCATION_ID     FINANCE.GL_TRAN_MASTER.LOCATION_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT    IN OUT REF_GL_TRAN_MASTER,
                                 P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE);

  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ------------------------------------------------------
  -- This procedure will Delete FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);

  ----------------------------------------------------
  -- FOLLOWING PROCEDURE WILL INSERT GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE        IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID       IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE     IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS           IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                              P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_LOGIN_LOCATION_ID IN VARCHAR2,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_OBJECT_CODE       IN VARCHAR2,
                              P_NEW_VOUCHER_NO    OUT VARCHAR2,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_LOGIN_LOCATION_ID IN VARCHAR2,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_LOGIN_LOCATION_ID IN VARCHAR2,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  --------------------------------------------------------------------
  -- Following function is used to get payroll process end date  --
  --------------------------------------------------------------------
  FUNCTION IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN DATE;

  -----------------------------------------------------------------------------------------
  -- Following function is used to validate employee to populate necessary information   --
  -----------------------------------------------------------------------------------------
  FUNCTION IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN BOOLEAN;

  ----------------------------------------------------------------------------------
  -- Following function is used to generate refund number w.r.t location id    --
  ----------------------------------------------------------------------------------
  FUNCTION GENERATE_REFUND_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN VARCHAR2;
  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);

  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan refund --
  ---------------------------------------------------------------------
  PROCEDURE FINALIZE_LOAN_REFUND(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                 P_LOGIN_LOCATION_ID IN VARCHAR2,
                                 P_USER_MRNO         IN VARCHAR2,
                                 P_TERMINAL          IN VARCHAR2,
                                 P_OBJECT_CODE       IN VARCHAR2,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);
  ---------------------------------------------------------------------
  -- This procedule is used to finalize loan refund --
  ---------------------------------------------------------------------
  PROCEDURE UNFINALIZE_LOAN_REFUND(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                   P_LOGIN_LOCATION_ID IN VARCHAR2,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
END PKG_S16FRM00037;
```

#### PAYROLL.PKG_S16FRM00038
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00038 IS

  TYPE CONSTANT_VALUE IS TABLE OF VARCHAR2(100) INDEX BY VARCHAR2(100);

  TYPE MSG_REC IS RECORD(
    MESSAGE_TEXT   VARCHAR2(500),
    MESSAGE_NATURE VARCHAR2(1));
  TYPE MSG_TAB IS TABLE OF MSG_REC INDEX BY BINARY_INTEGER;

  TYPE POST_MSG_TAB IS TABLE OF MSG_REC INDEX BY BINARY_INTEGER;

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Function CALCULATE LOAN
  PROCEDURE CALCULATE_LOAN(P_MRNO           IN VARCHAR2,
                           P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For calculate_payroll
  PROCEDURE CALCULATE_PAYROLL(P_PAY_START_DATE     IN DATE,
                              P_PAY_END_DATE       IN DATE,
                              P_EMP_SAL_START_DATE IN OUT DATE,
                              P_EMP_SAL_END_DATE   IN OUT DATE,
                              P_SALCERMONTH        IN CHAR,
                              P_USERNAME           IN VARCHAR2,
                              P_TERMINAL           IN VARCHAR2,
                              P_ND_END_DATE        IN DATE,
                              P_ND_START_DATE      IN DATE,
                              P_PAY_MONTH_DAYS     IN NUMBER,
                              P_LOCATION_ID        IN VARCHAR2,
                              P_ORGANIZATION_ID    IN VARCHAR2,
                              P_STOP               OUT VARCHAR2,
                              P_ALERT_TEXT         OUT VARCHAR2 /*,
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      P_CALC_MSG           IN OUT VARCHAR2*/);

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For Post_Payroll
  PROCEDURE POST_PAYROLL(P_PAY_START_DATE IN DATE,
                         P_PAY_END_DATE   IN DATE,
                         P_STOP           OUT VARCHAR2,
                         P_ALERT_TEXT     OUT VARCHAR2);

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For uncalc_payroll
  PROCEDURE UNCALC_PAYROLL(P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For unpost_payroll
  PROCEDURE UNPOST_PAYROLL(P_PAY_START_DATE IN DATE,
                           P_PAY_END_DATE   IN DATE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For all_emp_monthly_sal
  PROCEDURE ALL_EMP_MONTHLY_SAL(P_USER_ID          IN VARCHAR2,
                                P_TERMINAL         IN VARCHAR2,
                                P_MRNO             IN VARCHAR2,
                                P_LOCATION_ID      IN VARCHAR2,
                                P_MONTH_START_DATE DATE,
                                P_MONTH_END_DATE   DATE,
                                P_MONTH_DAYS       NUMBER,
                                P_CALC_PCTAGE      NUMBER,
                                ----
                                -- P_CALC_MESSAGE       IN OUT VARCHAR2,
                                P_PAY_START_DATE     IN DATE,
                                P_PAY_END_DATE       IN DATE,
                                P_EMP_SAL_START_DATE IN DATE,
                                P_EMP_SAL_END_DATE   IN DATE,
                                P_ND_END_DATE        IN DATE
                                ----,P_STOP       OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2
                                );

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 11:46AM
  -- Purpose: Procedure For emp_monthly_Salary
  PROCEDURE EMP_MONTHLY_SALARY(P_MRNO             IN VARCHAR2,
                               P_USER_ID          IN VARCHAR2,
                               P_TERMINAL         IN VARCHAR2,
                               P_MONTH_START_DATE IN DATE,
                               P_MONTH_END_DATE   IN DATE,
                               P_MONTH_DAYS       IN NUMBER,
                               P_DAILY_WAGER      IN CHAR,
                               ----
                               P_PAY_START_DATE IN DATE,
                               P_PAY_END_DATE   IN DATE,
                               --  p_salcermonth        in varchar2,
                               P_EMP_SAL_START_DATE IN DATE,
                               P_EMP_SAL_END_DATE   IN DATE --,P_STOP       OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2
                               );

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 02:20PM
  -- Purpose: Procedure For employee_daily_salary
  PROCEDURE EMPLOYEE_DAILY_SALARY(P_MRNO             IN VARCHAR2,
                                  P_DATE             IN DATE,
                                  P_USER_ID          IN VARCHAR2,
                                  P_TERMINAL         IN VARCHAR2,
                                  P_MONTH_START_DATE IN DATE,
                                  P_MONTH_END_DATE   IN DATE,
                                  P_MONTH_DAYS       IN NUMBER,
                                  P_PAID_UNPAID      IN CHAR,
                                  P_DAILY_WAGER      IN CHAR,
                                  P_DAILY_RATE       OUT NUMBER,
                                  ---
                                  P_PAY_START_DATE IN DATE,
                                  P_PAY_END_DATE   IN DATE --,
                                  ---              P_STOP       OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2
                                  );

  -- Created by: Asma Hashmi
  -- Creation Date: 09-07-2014 3:26PM
  -- Purpose: Procedure For Employee_Daily_AD
  PROCEDURE EMPLOYEE_DAILY_AD(P_MRNO               IN VARCHAR2,
                              P_AD_CODE            IN CHAR,
                              P_MONTH_START_DATE   IN DATE,
                              P_MONTH_END_DATE     IN DATE,
                              P_MONTH_DAYS         IN NUMBER,
                              P_AMOUNT             OUT NUMBER,
                              P_EMP_SAL_START_DATE IN DATE,
                              P_EMP_SAL_END_DATE   IN DATE
                              --P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2
                              );

  FUNCTION F_GET_PAYROLL_EMP_LOCATION(P_START_DATE DATE,
                                      P_END_DATE   DATE,
                                      P_MRNO       VARCHAR2) RETURN VARCHAR2;
  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: Procedure Base Block PAYROLL.PAY_TMP_EMP
  TYPE PAY_TMP_EMP_REC IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    SELECT_FLAG     PAYROLL.PAY_TMP_EMP.SELECT_FLAG%TYPE,
    START_DATE      PAYROLL.PAY_TMP_EMP.START_DATE%TYPE,
    END_DATE        PAYROLL.PAY_TMP_EMP.END_DATE%TYPE,
    DESIGNATION     VARCHAR2(250),
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
    LOCATION_DESC   DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    ERROR_TEXT      VARCHAR2(4000));

  TYPE PAY_TMP_EMP_REF IS REF CURSOR RETURN PAY_TMP_EMP_REC;

  --- Table of Records---
  TYPE PAY_TMP_EMP_TAB IS TABLE OF PAY_TMP_EMP_REC INDEX BY BINARY_INTEGER;

  --- Query PAY_TMP_EMP ---
  PROCEDURE QUERY_PAY_TMP_EMP(P_RESULT              IN OUT PAY_TMP_EMP_REF,
                              P_EXCEPTION_RECORDS   IN CHAR,
                              P_PAYROLL_LOCATION_ID IN PAYROLL.PAY_TMP_EMP.PAYROLL_LOCATION_ID%TYPE);
  ----------------------------------------------------------------------
  -- This Procedure will insert the recods into PAYROLL.PAY_TMP_EMP --
  ----------------------------------------------------------------------
  PROCEDURE UPDATE_PAY_TMP_EMP(P_BLOCK_DATA IN OUT PAY_TMP_EMP_TAB);
  --------------------------------------------------------------------
  -- This Procedure will Lock the PAYROLL.PAY_TMP_EMP--
  --------------------------------------------------------------------
  PROCEDURE LOCK_PAY_TMP_EMP(P_BLOCK_DATA IN OUT PAY_TMP_EMP_TAB);
  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: Insert into PAYROLL.PAY_TMP_EMP
  PROCEDURE INSERT_PAY_TEMP_EMP(P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_NAME                REGISTRATION.PATIENT.NAME%TYPE,
                                P_SELECT_FLAG         IN PAYROLL.PAY_TMP_EMP.SELECT_FLAG%TYPE,
                                P_START_DATE          IN DATE,
                                P_END_DATE            IN DATE,
                                P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_ALERT_TEXT          OUT VARCHAR2,
                                P_STOP                OUT CHAR);

  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: Populate payroll data
  PROCEDURE POPULATE_DATA(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_CAL_POST            IN CHAR,
                          P_PAY_START_DATE      IN DATE,
                          P_PAY_END_DATE        IN DATE,
                          P_MON_START_DATE      IN DATE,
                          P_MON_END_DATE        IN DATE,
                          P_MONTH_CODE          IN VARCHAR2,
                          P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_FROM_COST_CENTRE    IN DEFINITIONS.GL_DIV_DEPT_CC.COST_CENTRE_ID%TYPE,
                          P_TO_COST_CENTRE      IN DEFINITIONS.GL_DIV_DEPT_CC.COST_CENTRE_ID%TYPE,
                          P_FROM_EMP_CODE       IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_TO_EMP_CODE         IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_SINGLE_EMP_CODE     IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_FROM_SALARY         IN NUMBER,
                          P_TO_SALARY           IN NUMBER,
                          P_OBJECT_CODE         IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                          P_USER_MRNO           IN VARCHAR2,
                          P_TERMINAL            IN VARCHAR2,
                          P_ALERT_TEXT          OUT VARCHAR2,
                          P_STOP                OUT CHAR);

  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: Insert into PAYROLL.PAY_MASTER_TEST
  PROCEDURE INSERT_PAY_MASTER_TEST(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_START_DATE      IN DATE,
                                   P_PAY_END_DATE        IN DATE,
                                   P_PAY_MONTH_DAYS      IN PAYROLL.PAY_MASTER_TEST.MONTH_DAYS%TYPE,
                                   P_ALERT_TEXT          OUT VARCHAR2,
                                   P_STOP                OUT CHAR);

  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: CHECK PAYROLL PROCESS PREREQUSITS
  PROCEDURE CHECK_PREREQUSITS(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_SALCERMONTH         IN CHAR,
                              P_FUNCTIONALITY       IN VARCHAR2,
                              P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_TAB                 OUT PAYROLL.PKG_S16FRM00038.MSG_TAB,
                              P_ALERT_TEXT          OUT VARCHAR2,
                              P_STOP                OUT CHAR);

  -- Created by: Muhammad Ali Khubaib
  -- Creation Date: 05-11-2018
  -- Purpose: CHEKC PAYROLL PROCESS POSTREQUSITS
  PROCEDURE CHECK_POSTREQUSITS(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_FUNCTIONALITY       IN VARCHAR2,
                               P_TAB                 OUT PAYROLL.PKG_S16FRM00038.POST_MSG_TAB,
                               P_ALERT_TEXT          OUT VARCHAR2,
                               P_STOP                OUT CHAR);
END;
```

#### PAYROLL.PKG_S16FRM00039
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00039 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-OCT-2017   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC   DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_START_DATE  PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
    PAY_END_DATE    PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS   DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT       IN OUT REF_GL_TRAN_MASTER,
                                 P_LOCATION_ID  IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                 P_START_DATE   IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                 P_END_DATE     IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
END;
```

#### PAYROLL.PKG_S16FRM00042
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00042 IS
  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL ARREARS
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        28-Sep-2018   Farhan Akram           1. Created this Package.
  ************************************************************************************************/
  ------------------
  -- Record Group --
  ------------------
  TYPE TAX_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE TAX_REF IS REF CURSOR RETURN TAX_REC;
  ------------------------------------------
  -- This procedure will query TAX MONTH  --
  ------------------------------------------
  PROCEDURE QUERY_TAX(P_RESULT           IN OUT TAX_REF,
                      P_MONTH_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                      P_MONTH_END_DATE   IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE);
  ------------------
  -- Record Group --
  ------------------
  TYPE ITAX_DETAIL_REC IS RECORD(
    START_DATE            PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
    END_DATE              PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
    MRNO                  PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE,
    NAME                  REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION           DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT            DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE                 DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    EMP_LOCATION_ID       DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    AD_CODE               PAYROLL.PAY_ITAX_DETAIL.AD_CODE%TYPE,
    SETUP_TAX             PAYROLL.PAY_ITAX_DETAIL.SETUP_TAX%TYPE,
    PROPOSED_TAX          PAYROLL.PAY_ITAX_DETAIL.PROPOSED_TAX%TYPE,
    DEDUCTED_TAX          PAYROLL.PAY_ITAX_DETAIL.DEDUCTED_TAX%TYPE,
    EXPECTED_YTAXABLE_AMT PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
    EXPECTED_YEARLY_TAX   PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAX%TYPE,
    YEARLY_PAID_TAX       PAYROLL.PAY_ITAX_DETAIL.YEARLY_PAID_TAX%TYPE,
    SELECT_FLAG           PAYROLL.PAY_ITAX_DETAIL.SELECT_FLAG%TYPE,
    ORGANIZATION_ID       PAYROLL.PAY_ITAX_DETAIL.ORGANIZATION_ID%TYPE,
    LOCATION_ID           PAYROLL.PAY_ITAX_DETAIL.LOCATION_ID%TYPE,
    LOG                   PAYROLL.PAY_ITAX_DETAIL.LOG%TYPE,
    NET_SALARY            PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE ITAX_DETAIL_REF IS REF CURSOR RETURN ITAX_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE ITAX_DETAIL_TAB IS TABLE OF ITAX_DETAIL_REC INDEX BY BINARY_INTEGER;

  -----------------------------------------------------
  -- This procedure will query PAYROLL.PAY_ITAX_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_ITAX_DETAIL(P_RESULT      IN OUT ITAX_DETAIL_REF,
                              P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_START_DATE  IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                              P_END_DATE    IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                              P_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_ORDER_BY    IN VARCHAR2);

  ------------------------------------------------------
  -- This procedure will update PAYROLL.PAY_ITAX_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);

  ----------------------------------------------------
  -- This procedure will lock PAYROLL.PAY_ITAX_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);
  --------------------------------------------------------------------------------------
  -- Following procedue will use to calculate proposed tax for all/specified employee --
  --------------------------------------------------------------------------------------
  PROCEDURE NEXT_MONTH_PROPOSED_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MON_START_DATE    IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                                    P_MON_END_DATE      IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                                    P_MRNO              IN PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
  PROCEDURE NEXT_MONTH_PROPOSED_TAX2(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_MON_START_DATE    IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                                     P_MON_END_DATE      IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
  --------------------------------------------------------------------------------------
  -- Following procedue will use to update proposed tax for all/specified employee --
  --------------------------------------------------------------------------------------
  PROCEDURE UPDATE_PROPOSED_TAX_ALL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_MON_START_DATE    IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                                    P_MON_END_DATE      IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT VARCHAR2);
END PKG_S16FRM00042;
```

#### PAYROLL.PKG_S16FRM00046
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00046 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL EMPLOYEE INCREMENT
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        11-MAR-2021   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_INCREMENT_MASTER IS RECORD(
    MRNO               REGISTRATION.PATIENT.MRNO%TYPE,
    EMPLOYEE_NAME      REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION        DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT         DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE              DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    JOINING_DATE       DATE,
    DAYILY_WAGER       PAYROLL.DEF_EMP_FINANCIAL.DAILY_WAGER%TYPE,
    INCREMENT_DATE     PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
    INCREMENT_CODE     PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_CODE%TYPE,
    INCR_DESC          PAYROLL.DEF_INCREMENT_TYPE.DESCRIPTION%TYPE,
    APPROVED_BY        REGISTRATION.PATIENT.MRNO%TYPE,
    APPROVED_BY_NAME   REGISTRATION.PATIENT.NAME%TYPE,
    INCR_AMOUNT        PAYROLL.EMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE,
    INCR_PERCENT       PAYROLL.EMP_INCREMENT_MASTER.INCR_PERCENT%TYPE,
    CURRENT_BASIC      PAYROLL.EMP_INCREMENT_MASTER.CURRENT_BASIC%TYPE,
    CURRENT_GROSS      PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE,
    REMARKS            PAYROLL.EMP_INCREMENT_MASTER.REMARKS%TYPE,
    INCREMENT_END_DATE PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_END_DATE%TYPE,
    PREVIOUS_BASIC     PAYROLL.EMP_INCREMENT_MASTER.PREVIOUS_BASIC%TYPE,
    PREVIOUS_GROSS     PAYROLL.EMP_INCREMENT_MASTER.PREVIOUS_GROSS%TYPE,
    POSTED             PAYROLL.EMP_INCREMENT_MASTER.POSTED%TYPE,
    EFFECTIVE_DATE     PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
    ARREAR_PAID        PAYROLL.EMP_INCREMENT_MASTER.ARREAR_PAID%TYPE,
    PROCESS_ID         PAYROLL.EMP_INCREMENT_MASTER.PROCESS_ID%TYPE,
    ACTIVE             CHAR(1),
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    EMPLOYEE_TYPE      DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_INCREMENT_MASTER IS REF CURSOR RETURN REC_INCREMENT_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_INCREMENT_MASTER IS TABLE OF REC_INCREMENT_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_INCREMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE QUERY_INCREMENT_MASTER(P_RESULT IN OUT REF_INCREMENT_MASTER,
                                   P_MRNO   IN REGISTRATION.PATIENT.MRNO%TYPE);
  -------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE INSERT_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE UPDATE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_INCREMENT_MASTER --
  -------------------------------------------------------------
  PROCEDURE DELETE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  -----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_INCREMENT_MASTER --
  -----------------------------------------------------------
  PROCEDURE LOCK_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_INCREMENT_DETAIL IS RECORD(
    AD_CODE           PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
    AD_DESC           PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    MRNO              REGISTRATION.PATIENT.MRNO%TYPE,
    INCREMENT_DATE    PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE,
    CURRENT_AMOUNT    PAYROLL.EMP_INCREMENT_DETAIL.CURRENT_AMOUNT%TYPE,
    PREVIOUS_AMOUNT   PAYROLL.EMP_INCREMENT_DETAIL.PREVIOUS_AMOUNT%TYPE,
    ORGANIZATION_ID   DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
    LOCATION_ID       DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    AD_NATURE_TYPE_ID PAYROLL.DEF_AD_SETUP.AD_NATURE_TYPE_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_INCREMENT_DETAIL IS REF CURSOR RETURN REC_INCREMENT_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE EMP_INCREMENT_DETAIL_TAB IS TABLE OF REC_INCREMENT_DETAIL INDEX BY BINARY_INTEGER;

  ------------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_INCREMENT_DETAIL --
  ------------------------------------------------------------
  PROCEDURE QUERY_INCREMENT_DETAIL(P_RESULT         IN OUT REF_INCREMENT_DETAIL,
                                   P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE,
                                   P_AD_CODE        IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE);
  ------------------------------------------------------------
  -- This procedure will insert PAYROLL.EMP_INCREMENT_DETAIL --
  ------------------------------------------------------------
  PROCEDURE INSERT_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_INCREMENT_DETAIL --
  -------------------------------------------------------------
  PROCEDURE UPDATE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_INCREMENT_DETAIL --
  -------------------------------------------------------------
  PROCEDURE DELETE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
  -----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_INCREMENT_DETAIL --
  -----------------------------------------------------------
  PROCEDURE LOCK_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB);
END PKG_S16FRM00046;
```

#### PAYROLL.PKG_S16FRM00060
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00060 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for STOP SALARY PAYMENT
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        29-APR-2021   M. ALI KHUBAIB            1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE MONTH_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15),
    PAY_START_DATE    DATE,
    PAY_END_DATE      DATE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE MONTH_REF IS REF CURSOR RETURN MONTH_REC;
  TYPE TAB_MONTH IS TABLE OF MONTH_REC;
  -----------------------------------------------------
  -- This procedure will query PAYROLL.SALARY_STOP --
  -----------------------------------------------------
  PROCEDURE QUERY_MONTH(P_RESULT           IN OUT MONTH_REF,
                        P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE,
                        P_MONTH_END_DATE   IN PAYROLL.PAY_STATUS.DATE_TO%TYPE);

  -- pipeline Function for query Balances --                          
  FUNCTION F_QUERY_MONTH_APEX(P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE,
                              P_MONTH_END_DATE   IN PAYROLL.PAY_STATUS.DATE_TO%TYPE)
    RETURN TAB_MONTH
    PIPELINED;
  ------------------
  -- Record Group --
  ------------------
  TYPE SALARY_STOP_REC IS RECORD(
    
    SERIAL_NO              PAYROLL.PAY_STATUS.SERIAL_NO%TYPE,
    MRNO                   PAYROLL.PAY_STATUS.MRNO%TYPE,
    NAME                   REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION            DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT             DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE                  DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    LOCATION_ID            DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    DATE_FROM              PAYROLL.PAY_STATUS.DATE_FROM%TYPE,
    DATE_TO                PAYROLL.PAY_STATUS.DATE_TO%TYPE,
    STATUS                 PAYROLL.PAY_STATUS.STATUS%TYPE,
    DISCIPLINARY_REASON_ID PAYROLL.PAY_STATUS.DISCIPLINARY_REASON_ID%TYPE,
    USER_COMMENTS          PAYROLL.PAY_STATUS.USER_COMMENTS%TYPE,
    PAY_CALC_DATE          DEFINITIONS.LOCATION_WISE_MONTHS.PAY_CALC_DATE%TYPE,
    PAY_PROCESS            DEFINITIONS.LOCATION_WISE_MONTHS.PAY_PROCESS%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE SALARY_STOP_REF IS REF CURSOR RETURN SALARY_STOP_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE SALARY_STOP_TAB IS TABLE OF SALARY_STOP_REC INDEX BY BINARY_INTEGER;

  --------------------------------------------------
  -- This procedure will query PAYROLL.PAY_STATUS --
  --------------------------------------------------
  PROCEDURE QUERY_SALARY_STOP(P_RESULT           IN OUT SALARY_STOP_REF,
                              P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE,
                              P_MONTH_END_DATE   IN PAYROLL.PAY_STATUS.DATE_TO%TYPE,
                              P_MRNO             IN REGISTRATION.PATIENT.MRNO%TYPE);

  ---------------------------------------------------
  -- This procedure will insert PAYROLL.PAY_STATUS --
  ---------------------------------------------------
  PROCEDURE INSERT_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB);

  ---------------------------------------------------
  -- This procedure will update PAYROLL.PAY_STATUS --
  ---------------------------------------------------
  PROCEDURE UPDATE_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB);

  ---------------------------------------------------
  -- This procedure will DELETE PAYROLL.PAY_STATUS --
  ---------------------------------------------------
  PROCEDURE DELETE_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB);

  -------------------------------------------------
  -- This procedure will lock PAYROLL.PAY_STATUS --
  -------------------------------------------------
  PROCEDURE LOCK_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB);

END;
```

#### PAYROLL.PKG_S16FRM00061
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00061 IS
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : The following record type, table types will be used
  --             for dml of FINANCE.GL_TRAN_MASTER
  /******************************************************************************/

  TYPE TRAN_MASTER_REC IS RECORD(
    
    VOUCHER_TYPE           FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO             FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE             FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    REFERENCE_NO           FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS                FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    ENTERED_BY             FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    CURRENCY_ID            FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    VOUCHER_STATUS         FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    APPROVED_BY            FINANCE.GL_TRAN_MASTER.APPROVED_BY%TYPE,
    MODULE_ID              FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    THIRTEENTH_MONTH       FINANCE.GL_TRAN_MASTER.THIRTEENTH_MONTH%TYPE,
    ND_CURRENCY_SHORT_DESC definitions.currency.short_description%TYPE,
    CURRENCY_RATE          FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    POSTED_BY              FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    POSTED_DATE            FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    TEMPOSTED_BY           FINANCE.GL_TRAN_MASTER.TEMPOSTED_BY%TYPE,
    UNTEMPOSTED_BY         FINANCE.GL_TRAN_MASTER.UNTEMPOSTED_BY%TYPE,
    --TEMPOSTED_DATE     FINANCE.GL_TRAN_MASTER.TEMPOSTED_DATE%TYPE,
    --UNTEMPOSTED_DATE   FINANCE.GL_TRAN_MASTER.UNTEMPOSTED_DATE%TYPE,
    ENTERED_DATE      FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    APPROVED_DATE     FINANCE.GL_TRAN_MASTER.APPROVED_DATE%TYPE,
    TEMPOSTED_DATE    FINANCE.GL_TRAN_MASTER.TEMPOSTED_DATE%TYPE,
    UNTEMPOSTED_DATE  FINANCE.GL_TRAN_MASTER.UNTEMPOSTED_DATE%TYPE,
    USER_ID           FINANCE.GL_TRAN_MASTER.USER_ID%TYPE,
    TERMINAL          FINANCE.GL_TRAN_MASTER.TERMINAL%TYPE,
    TRN_DATE          FINANCE.GL_TRAN_MASTER.TRN_DATE%TYPE,
    CF_FILE_NO        FINANCE.GL_TRAN_MASTER.CF_FILE_NO%TYPE,
    CF_LINE_NO        FINANCE.GL_TRAN_MASTER.CF_LINE_NO%TYPE,
    PARTY_NAME        FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    ORIGINAL_USER_ID  FINANCE.GL_TRAN_MASTER.ORIGINAL_USER_ID%TYPE,
    ORIGINAL_TERMINAL FINANCE.GL_TRAN_MASTER.ORIGINAL_TERMINAL%TYPE,
    ORIGINAL_TRN_DATE FINANCE.GL_TRAN_MASTER.ORIGINAL_TRN_DATE%TYPE,
    MRNO              FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    PBS_GL_SETUP_ID   FINANCE.GL_TRAN_MASTER.PBS_GL_SETUP_ID%TYPE,
    PARTY_SUB_CODE    FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    TEMP_VOUCHER_TYPE FINANCE.GL_TRAN_MASTER.TEMP_VOUCHER_TYPE%TYPE,
    TEMP_VOUCHER_NO   FINANCE.GL_TRAN_MASTER.TEMP_VOUCHER_NO%TYPE,
    MMS_REFERENCE     FINANCE.GL_TRAN_MASTER.MMS_REFERENCE%TYPE,
    POSTED_REMARKS    FINANCE.GL_TRAN_MASTER.POSTED_REMARKS%TYPE);

  TYPE TRAN_MASTER_TBL IS TABLE OF TRAN_MASTER_REC INDEX BY PLS_INTEGER;
  TYPE TRAN_MASTER_TBL_PF IS TABLE OF TRAN_MASTER_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : The following record type, table types will be used
  --             for dml of FINANCE.GL_TRAN_DETAIL
  /******************************************************************************/
  TYPE GL_TRAN_DETAIL_REC IS RECORD(
    voucher_no            FINANCE.GL_TRAN_DETAIL.voucher_no%TYPE,
    voucher_type          FINANCE.GL_TRAN_DETAIL.voucher_type%TYPE,
    ledger_type_code      FINANCE.GL_TRAN_DETAIL.ledger_type_code%TYPE,
    trans_date            FINANCE.GL_TRAN_DETAIL.trans_date%TYPE,
    serial_no             FINANCE.GL_TRAN_DETAIL.serial_no%TYPE,
    coa_code              FINANCE.GL_TRAN_DETAIL.coa_code%TYPE,
    ND_COA_DESCRIPTION    finance.gl_coa.coa_description%TYPE,
    sub_ldgr_item_code    FINANCE.GL_TRAN_DETAIL.sub_ldgr_item_code%TYPE,
    ND_SUB_LDGR_ITEM_DESC finance.gl_sub_ledgers.sub_ldgr_item_desc%TYPE,
    reference_no          FINANCE.GL_TRAN_DETAIL.reference_no%TYPE,
    narration             FINANCE.GL_TRAN_DETAIL.narration%TYPE,
    dr_amount             FINANCE.GL_TRAN_DETAIL.dr_amount%TYPE,
    cr_amount             FINANCE.GL_TRAN_DETAIL.cr_amount%TYPE,
    pre_post_dr           FINANCE.GL_TRAN_DETAIL.pre_post_dr%TYPE,
    pre_post_cr           FINANCE.GL_TRAN_DETAIL.pre_post_cr%TYPE,
    coa_status            FINANCE.GL_TRAN_DETAIL.coa_status%TYPE,
    COST_CENTRE_ID        FINANCE.GL_TRAN_DETAIL.COST_CENTRE_ID%TYPE,
    currency_id           FINANCE.GL_TRAN_DETAIL.currency_id%TYPE,
    currency_rate         FINANCE.GL_TRAN_DETAIL.currency_rate%TYPE);

  TYPE GL_TRAN_DETAIL_TBL IS TABLE OF GL_TRAN_DETAIL_REC INDEX BY PLS_INTEGER;
  TYPE GL_TRAN_DETAIL_TBL_PF IS TABLE OF GL_TRAN_DETAIL_REC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : This procedure will be used for querying data of
  --             FINANCE.GL_TRAN_MASTER
  /******************************************************************************/
  FUNCTION F_TRAN_MASTER_QRY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                             P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)
    RETURN TRAN_MASTER_TBL_PF
    PIPELINED;
  /******************************************************************************/
  PROCEDURE P_TRAN_MASTER_QRY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_DATA         IN OUT TRAN_MASTER_TBL,
                              P_STOP         OUT VARCHAR2,
                              P_ALERT_TEXT   OUT VARCHAR2);
  /******************************************************************************/

  PROCEDURE P_TRAN_MASTER_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                              P_DATA            IN TRAN_MASTER_REC,
                              P_STOP            OUT VARCHAR2,
                              P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : This procedure will be used for inserting data in
  --             FINANCE.GL_TRAN_MASTER.
  /******************************************************************************/

  PROCEDURE P_TRAN_MASTER_INS(P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_DATA         IN OUT TRAN_MASTER_TBL,
                              P_STOP         OUT VARCHAR2,
                              P_ALERT_TEXT   OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : This procedure will be used for locking data of
  --             FINANCE.GL_TRAN_MASTER.
  /******************************************************************************/

  PROCEDURE P_TRAN_MASTER_LCK(P_DATA       IN OUT TRAN_MASTER_TBL,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : This procedure will be used for updating data of
  --             FINANCE.GL_TRAN_MASTER.
  /******************************************************************************/

  PROCEDURE P_TRAN_MASTER_UPD(P_DATA       IN OUT TRAN_MASTER_TBL,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_MASTER
  -- Purpose   : This procedure will be used for deleting data of
  --             FINANCE.GL_TRAN_MASTER.
  /******************************************************************************/

  PROCEDURE P_TRAN_MASTER_DEL(P_DATA       IN OUT TRAN_MASTER_TBL,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/

  FUNCTION GET_COA_DESCRIPTION(P_COA_CODE IN VARCHAR2) RETURN VARCHAR2;

  /******************************************************************************/

  FUNCTION GET_SUB_LDGR_ITEM_DESC(P_ledger_type_code   IN VARCHAR2,
                                  P_sub_ldgr_item_code IN VARCHAR2)
    RETURN VARCHAR2;

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_DETAIL
  -- Purpose   : This procedure will be used for querying data of
  --             FINANCE.GL_TRAN_DETAIL
  /******************************************************************************/

  FUNCTION F_GL_TRAN_DETAIL_QY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE,
                               P_VOUCHER_NO   IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE,
                               P_SERIAL_NO    IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE)
    RETURN GL_TRAN_DETAIL_TBL_PF
    PIPELINED;
  /******************************************************************************/
  PROCEDURE P_GL_TRAN_DETAIL_QY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO   IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE,
                                P_SERIAL_NO    IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
                                P_DATA         IN OUT GL_TRAN_DETAIL_TBL,
                                P_STOP         OUT VARCHAR2,
                                P_ALERT_TEXT   OUT VARCHAR2);

  /******************************************************************************/
  PROCEDURE P_GL_TRAN_DETAIL_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                 P_DATA            IN GL_TRAN_DETAIL_REC,
                                 P_STOP            OUT VARCHAR2,
                                 P_ALERT_TEXT      OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_DETAIL
  -- Purpose   : This procedure will be used for inserting data in
  --             FINANCE.GL_TRAN_DETAIL.
  /******************************************************************************/

  PROCEDURE P_GL_TRAN_DETAIL_INS(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE,
                                 P_SERIAL_NO    IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
                                 P_DATA         IN OUT GL_TRAN_DETAIL_TBL,
                                 P_STOP         OUT VARCHAR2,
                                 P_ALERT_TEXT   OUT VARCHAR2);

  /******************************************************************************/
  PROCEDURE P_GL_TRAN_DETAIL_LCK(P_DATA       IN OUT GL_TRAN_DETAIL_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_DETAIL
  -- Purpose   : This procedure will be used for locking data of
  --             FINANCE.GL_TRAN_DETAIL.

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_DETAIL
  -- Purpose   : This procedure will be used for updating data of
  --             FINANCE.GL_TRAN_DETAIL.
  /******************************************************************************/

  PROCEDURE P_GL_TRAN_DETAIL_UPD(P_DATA       IN OUT GL_TRAN_DETAIL_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 30-JULY-2013
  -- Scope     : GL_TRAN_DETAIL
  -- Purpose   : This procedure will be used for deleting data of
  --             FINANCE.GL_TRAN_DETAIL.
  /******************************************************************************/

  PROCEDURE P_GL_TRAN_DETAIL_DEL(P_DATA       IN OUT GL_TRAN_DETAIL_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);

  /**********************************************************************/
  PROCEDURE PRO_INSERT_GL_TRAN_MASTER(P_START_DATE    IN DATE,
                                      P_END_DATE      IN DATE,
                                      P_USER_MRNO     IN VARCHAR2,
                                      P_REMARKS       IN VARCHAR2,
                                      P_CURRENCY_ID   IN VARCHAR2,
                                      P_CURRENCY_RATE IN NUMBER,
                                      P_VOUCHER_TYPE  IN VARCHAR2,
                                      P_LOCATION_ID   IN VARCHAR2,
                                      P_VOUCHER_NO    OUT VARCHAR2,
                                      P_STOP          OUT VARCHAR2,
                                      P_ALERT_TEXT    OUT VARCHAR2);
  /**********************************************************************/
  PROCEDURE PRO_GENRATE_PESSI_VOUCHER(P_START_DATE    IN DATE,
                                      P_END_DATE      IN DATE,
                                      P_VOUCHER_NO    IN OUT VARCHAR2,
                                      P_VOUCHER_TYPE  IN VARCHAR2,
                                      P_REMARKS       IN VARCHAR2,
                                      P_USER_MRNO     IN VARCHAR2,
                                      P_CURRENCY_ID   IN VARCHAR2,
                                      P_CURRENCY_RATE IN VARCHAR2,
                                      P_LOCATION_ID   IN VARCHAR2,
                                      P_STOP          OUT CHAR,
                                      P_ALERT_TEXT    OUT VARCHAR2);
  --=====================================================================
  FUNCTION GET_TEMP_VOUCHER_NO(P_TRANS_DATE   DATE,
                               P_VOUCHER_TYPE VARCHAR2,
                               P_MRNO         IN VARCHAR2,
                               P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2;
  --======================================================================
  PROCEDURE PRO_UPDATE_SSC_CAL_MAST(P_START_DATE   IN DATE,
                                    P_END_DATE     IN DATE,
                                    P_VOUCHER_NO   IN VARCHAR2,
                                    P_VOUCHER_TYPE IN VARCHAR2,
                                    P_LOCATION_ID  IN VARCHAR2,
                                    P_STOP         OUT CHAR,
                                    P_ALERT_TEXT   OUT VARCHAR2);
  --===============================================================
  PROCEDURE PRO_CANCEL_BTN(P_VOUCHER_NO   IN VARCHAR2,
                           P_VOUCHER_TYPE IN VARCHAR2,
                           P_STOP         OUT CHAR,
                           P_ALERT_TEXT   OUT VARCHAR2);

  --===============================================================
  PROCEDURE PRO_CHECK_PESSI_AMOUNT(P_FROM_DATE    IN DATE,
                                   P_TO_DATE      IN DATE,
                                   P_VOUCHER_NO   IN VARCHAR2,
                                   P_VOUCHER_TYPE IN VARCHAR2,
                                   P_LOCATION_ID  IN VARCHAR2,
                                   P_FORM_AMOUNT  IN NUMBER,
                                   P_STOP         OUT CHAR,
                                   P_ALERT_TEXT   OUT VARCHAR2);

/**********************************************************************/

END PKG_S16FRM00061;
```

#### PAYROLL.PKG_S16FRM00070
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00070 IS

  /***********************************************************************************************
         OBJECTIVE := THIS PACKAGE WAS CREATED FOR CASH REFUND
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-JUL-2018   SHAHID JAMAL (8317)    1. CREATED THIS PACKAGE.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE VERSION OF THIS PACKAGE --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ---------------------------------------------------
  -- RECORD TYPE DECLARATION FOR MASTER TABLE DATA --
  ---------------------------------------------------
  TYPE EXP_CLAIM_MASTER_REC IS RECORD(
    CLAIM_NO          PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
    EXPENSE_CODE      PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE,
    EXPENSE_TYPE      DEFINITIONS.EXPENSE.DESCRIPTION%TYPE,
    MRNO              PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE,
    EMPLOYEE_NAME     REGISTRATION.PATIENT.NAME%TYPE,
    EMPLOYEE_DESIG    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    EMPLOYEE_DEPT     DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    EMPLOYEE_GRADE    DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    TRANS_DATE        PAYROLL.EXPENSE_CLAIM_MASTER.TRANS_DATE%TYPE,
    ADVANCE_GIVEN     PAYROLL.EXPENSE_CLAIM_MASTER.ADVANCE_GIVEN%TYPE,
    SIGN_BY           PAYROLL.EXPENSE_CLAIM_MASTER.SIGN_BY%TYPE,
    SIGN_BY_NAME      REGISTRATION.PATIENT.NAME%TYPE,
    SIGN_BY_DESIG     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    SIGN_DATE         PAYROLL.EXPENSE_CLAIM_MASTER.SIGN_DATE%TYPE,
    STATUS_ID         PAYROLL.EXPENSE_CLAIM_MASTER.STATUS_ID%TYPE,
    STATUS_DESC       DEFINITIONS.ORDER_STATUS.DESCRIPTION%TYPE,
    APPROVER_REMARKS  PAYROLL.EXPENSE_CLAIM_MASTER.APPROVER_REMARKS%TYPE,
    APPROVED_BY       PAYROLL.EXPENSE_CLAIM_MASTER.APPROVED_BY%TYPE,
    APPROVE_BY_NAME   REGISTRATION.PATIENT.NAME%TYPE,
    APPROVE_BY_DESIG  DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    APPROVE_BY_DEPT   DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    APPROVED_DATE     PAYROLL.EXPENSE_CLAIM_MASTER.APPROVED_DATE%TYPE,
    TRAVEL_REQUEST_NO PAYROLL.EXPENSE_CLAIM_MASTER.TRAVEL_REQUEST_NO%TYPE,
    REVISION_NO       PAYROLL.EXPENSE_CLAIM_MASTER.REVISION_NO%TYPE,
    ORGANIZATION_ID   PAYROLL.EXPENSE_CLAIM_MASTER.ORGANIZATION_ID%TYPE,
    LOCATION_ID       PAYROLL.EXPENSE_CLAIM_MASTER.LOCATION_ID%TYPE,
    LOCATION_DESC     DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    DEPARTURE_DATE    PAYROLL.EXPENSE_CLAIM_MASTER.DEPARTURE_DATE%TYPE,
    RETURN_DATE       PAYROLL.EXPENSE_CLAIM_MASTER.RETURN_DATE%TYPE,
    REMARKS           PAYROLL.EXPENSE_CLAIM_MASTER.REMARKS%TYPE,
    EXPENSE_CON_TYPE  PAYROLL.DEF_EXPENSE_CONSTANT.TYPE%TYPE,
    WFE_NO            PAYROLL.EXPENSE_CLAIM_MASTER.WFE_NO%TYPE,
    SCHEMA_ID         PAYROLL.EXPENSE_CLAIM_WORKFLOW.SCHEMA_ID%TYPE,
    WORKFLOW_TYPE_ID  PAYROLL.EXPENSE_CLAIM_WORKFLOW.WORKFLOW_TYPE_ID%TYPE,
    WORK_FLOW_ID      PAYROLL.EXPENSE_CLAIM_WORKFLOW.WORK_FLOW_ID%TYPE,
    EVENT_ID          DEFINITIONS.EVENT.EVENT_ID%TYPE,
    EVENT_ORDERBY     DEFINITIONS.PR_TYPE_FLOW_EVENT.ORDER_BY%TYPE,
    EVENT_DESC        DEFINITIONS.EVENT.DESCRIPTION%TYPE,
    NEXT_EVENT_ID     DEFINITIONS.EVENT.EVENT_ID%TYPE,
    ENTERED_BY        REGISTRATION.PATIENT.MRNO%TYPE);

  -- REF CURSOR --
  TYPE EXP_CLAIM_MASTER_REF IS REF CURSOR RETURN EXP_CLAIM_MASTER_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE EXP_CLAIM_MASTER_TAB IS TABLE OF EXP_CLAIM_MASTER_REC INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA FROM EXPENSE CLAIM MASTER TABLE --
  -------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_MASTER(P_RESULT    IN OUT EXP_CLAIM_MASTER_REF,
                                   P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_CLAIM_NO  IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                   P_MRNO      IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE);
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO INSERT DATA INTO EXPENSE CLAIM MASTER TABLE --
  --------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE DATA IN EXPENSE CLAIM MASTER TABLE --
  ------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO DELETE DATA FROM EXPENSE CLAIM MASTER TABLE --
  ---------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ---------------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO LOCK RECORD FOR DMLS ON EXPENSE CLAIM MASTER TABLE --
  ---------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ---------------------------------------------------
  -- RECORD TYPE DECLARATION FOR DETAIL TABLE DATA --
  ---------------------------------------------------
  TYPE EXP_CLAIM_DETAIL_REC IS RECORD(
    CLAIM_NO          PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
    SRNO              PAYROLL.EXPENSE_CLAIM_DETAIL.SRNO%TYPE,
    EXPENSE_TYPE_ID   PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE,
    EXPENSE_TYPE_DESC DEFINITIONS.EXPENSE.DESCRIPTION%TYPE,
    FROM_DATE         PAYROLL.EXPENSE_CLAIM_DETAIL.FROM_DATE%TYPE,
    TO_DATE           PAYROLL.EXPENSE_CLAIM_DETAIL.TO_DATE%TYPE,
    CLAIM_AMOUNT      PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_AMOUNT%TYPE,
    APPROVED_AMOUNT   PAYROLL.EXPENSE_CLAIM_DETAIL.APPROVED_AMOUNT%TYPE,
    REMARKS           PAYROLL.EXPENSE_CLAIM_DETAIL.REMARKS%TYPE,
    DAYS_CLAIMED      PAYROLL.EXPENSE_CLAIM_DETAIL.DAYS_CLAIMED%TYPE,
    DAYS_APPROVED     PAYROLL.EXPENSE_CLAIM_DETAIL.DAYS_APPROVED%TYPE,
    SLAB_ID           BILLING.DEF_SLAB.SLAB_ID%TYPE,
    SLAB_DESCRIPTION  BILLING.DEF_SLAB.DESCRIPTION%TYPE,
    ENTRY_TYPE        PAYROLL.EXPENSE_CLAIM_DETAIL.ENTRY_TYPE%TYPE,
    CALC_METHOD       PAYROLL.EXPENSE_CLAIM_DETAIL.CALC_METHOD%TYPE);
  -- REF CURSOR --
  TYPE EXP_CLAIM_DETAIL_REF IS REF CURSOR RETURN EXP_CLAIM_DETAIL_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE EXP_CLAIM_DETAIL_TAB IS TABLE OF EXP_CLAIM_DETAIL_REC INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA FROM EXPENSE CLAIM DETAIL TABLE --
  -------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_DETAIL(P_RESULT          IN OUT EXP_CLAIM_DETAIL_REF,
                                   P_CLAIM_NO        IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
                                   P_SR_NO           IN PAYROLL.EXPENSE_CLAIM_DETAIL.SRNO%TYPE,
                                   P_EXPENSE_TYPE_ID IN PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE,
                                   P_FROM_DATE       IN PAYROLL.EXPENSE_CLAIM_DETAIL.FROM_DATE%TYPE,
                                   P_TO_DATE         IN PAYROLL.EXPENSE_CLAIM_DETAIL.TO_DATE%TYPE);
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO INSERT DATA INTO EXPENSE CLAIM DETAIL TABLE --
  --------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE DATA IN EXPENSE CLAIM DETAIL TABLE --
  ------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO DELETE DATA FROM EXPENSE CLAIM DETAIL TABLE --
  --------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ---------------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO LOCK RECORD FOR DMLS ON EXPENSE CLAIM DETAIL TABLE --
  ---------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ----------------------------------------------------
  -- RECORD TYPE DECLARATION FOR PROJECT TABLE DATA --
  ----------------------------------------------------
  TYPE EXP_CLAIM_PROJECT_REC IS RECORD(
    CLAIM_NO       PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
    PROJECT_ID     PAYROLL.EXPENSE_CLAIM_PROJECT.PROJECT_ID%TYPE,
    PROJECT_NAME   PAYROLL.DEF_PROJECT.PROJECT_NAME%TYPE,
    EXP_PERCENTAGE PAYROLL.EXPENSE_CLAIM_PROJECT.EXP_PERCENTAGE%TYPE,
    REMARKS        PAYROLL.EXPENSE_CLAIM_PROJECT.REMARKS%TYPE);
  -- REF CURSOR --
  TYPE EXP_CLAIM_PROJECT_REF IS REF CURSOR RETURN EXP_CLAIM_PROJECT_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE EXP_CLAIM_PROJECT_TAB IS TABLE OF EXP_CLAIM_PROJECT_REC INDEX BY BINARY_INTEGER;
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA FROM EXPENSE CLAIM PROJECT TABLE --
  --------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_PROJECT(P_RESULT         IN OUT EXP_CLAIM_PROJECT_REF,
                                    P_CLAIM_NO       IN PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
                                    P_PROJECT_ID     IN PAYROLL.EXPENSE_CLAIM_PROJECT.PROJECT_ID%TYPE,
                                    P_EXP_PERCENTAGE IN PAYROLL.EXPENSE_CLAIM_PROJECT.EXP_PERCENTAGE%TYPE,
                                    P_REMARKS        IN PAYROLL.EXPENSE_CLAIM_PROJECT.REMARKS%TYPE);
  ---------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO INSERT DATA INTO EXPENSE CLAIM PROJECT TABLE --
  ---------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  -------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE DATA IN EXPENSE CLAIM PROJECT TABLE --
  -------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  ---------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO DELETE DATA FROM EXPENSE CLAIM PROJECT TABLE --
  ---------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  ----------------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO LOCK RECORD FOR DMLS ON EXPENSE CLAIM PROJECT TABLE --
  ----------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);

  ----------------------------------------------------
  -- RECORD TYPE DECLARATION FOR PROJECT TABLE DATA --
  ----------------------------------------------------
  TYPE EXP_CLAIM_TRACK_REC IS RECORD(
    CLAIM_NO       PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
    WFE_NO         PAYROLL.EXPENSE_CLAIM_MASTER.WFE_NO%TYPE,
    EVENT          DEFINITIONS.EVENT.DESCRIPTION%TYPE,
    PERFORMED_MRNO REGISTRATION.PATIENT.MRNO%TYPE,
    PERFORMED_BY   REGISTRATION.PATIENT.NAME%TYPE,
    DATETIME       DATE,
    REMARKS        PAYROLL.EXPENSE_CLAIM_WORKFLOW.REMARKS%TYPE);
  -- REF CURSOR --
  TYPE EXP_CLAIM_TRACK_REF IS REF CURSOR RETURN EXP_CLAIM_TRACK_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE EXP_CLAIM_TRACK_TAB IS TABLE OF EXP_CLAIM_TRACK_REC INDEX BY BINARY_INTEGER;
  ------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA FROM EXPENSE CLAIM QUEUE TABLE --
  ------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_TRACK(P_RESULT   IN OUT EXP_CLAIM_TRACK_REF,
                                  P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q.CLAIM_NO%TYPE);
  ------------------------------------------------------------------------------------
  TYPE TRAVEL_VISIT_DETAIL_REC IS RECORD(
    CLAIM_NO     PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
    SRNO         HRD.TRAVEL_ACTIVITY_DETAIL.SRNO%TYPE,
    VISIT_DETAIL VARCHAR2(15000),
    ENTRY_DATE   HRD.TRAVEL_ACTIVITY_DETAIL.ENTRY_DATE%TYPE,
    STATUS       HRD.TRAVEL_ACTIVITY_DETAIL.STATUS%TYPE,
    DOCUMENT_ID  LOB.DOCUMENTS_STORE.DOCUMENT_ID%TYPE,
    ATTACHED_BY  HRD.TRAVEL_ACTIVITY_DETAIL.ATTACHED_BY%TYPE,
    IS_EXEMPT    HRD.TRAVEL_ACTIVITY_DETAIL.IS_EXEMPT%TYPE  );
    
  TYPE TRAVEL_VISIT_DETAIL_REF IS REF CURSOR RETURN TRAVEL_VISIT_DETAIL_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE TRAVEL_VISIT_DETAIL_TAB IS TABLE OF TRAVEL_VISIT_DETAIL_REC INDEX BY BINARY_INTEGER;
  --------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USE FOR VISIT DETAIL QUERY DATA
  ------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_DETAIL_QRY(P_REF_DATA IN OUT TRAVEL_VISIT_DETAIL_REF,
                                      P_CLAIM_NO PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE);

  ------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_DETAIL_INS(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB);
  -------------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_DETAIL_UPD(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB);
  -----------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_DETAIL_DEL(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB);
  ------------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_DETAIL_LOCK(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB);
  ----------------------------------------------------------------------------------------
  
  
  
  
    TYPE TRAVEL_VISIT_ATTACHMENT_REC IS RECORD(
    SR_NO                  HRD.TRAVLE_VISIT_ATTACHMENT.SR_NO%TYPE,
    CLAIM_NO               HRD.TRAVLE_VISIT_ATTACHMENT.CLAIM_NO%TYPE,
    MRNO                   HRD.V_INFORMATION.MRNO%TYPE ,
    DOCUMENT_ID            LOB.DOCUMENTS_STORE.DOCUMENT_ID%TYPE,
    DOCUMENT_DESCRIPTION   HRD.TRAVLE_VISIT_ATTACHMENT.DOCUMENT_DESCRIPTION%TYPE,
    ATTACHED_BY            HRD.TRAVLE_VISIT_ATTACHMENT.ATTACHED_BY%TYPE  );
    
  TYPE TRAVEL_VISIT_ATTACHMENT_REF IS REF CURSOR RETURN TRAVEL_VISIT_ATTACHMENT_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE TRAVEL_VISIT_ATTACHMENT_TAB IS TABLE OF TRAVEL_VISIT_ATTACHMENT_REC INDEX BY BINARY_INTEGER;
  
 -----------------------------------------------------------------------------------------------------------
     PROCEDURE P_TRAVEL_VISIT_ATTACHMENT_QRY(P_REF_DATA IN OUT  TRAVEL_VISIT_ATTACHMENT_REF,
                                      P_CLAIM_NO PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE) ;
                                      
 ----------------------------------------------------------------------------------------------------------------
  PROCEDURE P_TRAVEL_VISIT_ATTACHMENT_INS(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB) ;
  ------------------------------------
  
   PROCEDURE P_TRAVEL_VISIT_ATTACHMENT_UPD(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB) ;    
   
   ----------------------------------------------------------------------------------------------------------
   
    PROCEDURE P_TRAVEL_VISIT_ATTACHMENT_DEL(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB) ;    
    
    --------------------------------------------------------------------------------------------
    
    PROCEDURE P_TRAVEL_VISIT_ATTACHMENT_LOCK(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB);                           
                                      
    ----------------------------------------------------
    FUNCTION F_GET_DECISION_LIST (
      p_claim_no            IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.CLAIM_NO%TYPE,
      p_schema_id           IN NUMBER,
      p_workflow_type_id    IN NUMBER,
      p_work_flow_id        IN NUMBER,
      p_event_id            IN NUMBER,
      p_event_orderby       IN NUMBER,
      p_next_event_id       IN NUMBER
  ) RETURN SYS_REFCURSOR;
  

END PKG_S16FRM00070;
```

#### PAYROLL.PKG_S16FRM00072
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00072 IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for Exployee Expense Approval
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-JUL-2018   Shahid Jamal (8317)     1. Created this Package.
         2.0        18-JUN-2020   M. Ali Khubaib          1. Rewrite
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  -----------------------------------------------------------------
  -- Record Type Declaration for collection of Master Table data --
  -----------------------------------------------------------------
  TYPE EXP_CLAIM_MASTER_REC IS RECORD(
    CLAIM_NO               PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
    EXPENSE_CODE           PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE,
    EXPENSE_TYPE           DEFINITIONS.EXPENSE.DESCRIPTION%TYPE,
    MRNO                   PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE,
    EMPLOYEE_NAME          REGISTRATION.PATIENT.NAME%TYPE,
    EMPLOYEE_DESIG         DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    EMPLOYEE_DEPT          DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    EMPLOYEE_GRADE         DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    TRANS_DATE             PAYROLL.EXPENSE_CLAIM_MASTER.TRANS_DATE%TYPE,
    ADVANCE_GIVEN          PAYROLL.EXPENSE_CLAIM_MASTER.ADVANCE_GIVEN%TYPE,
    SIGN_BY                PAYROLL.EXPENSE_CLAIM_MASTER.SIGN_BY%TYPE,
    SIGN_BY_NAME           REGISTRATION.PATIENT.NAME%TYPE,
    SIGN_BY_DESIG          DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    SIGN_DATE              PAYROLL.EXPENSE_CLAIM_MASTER.SIGN_DATE%TYPE,
    STATUS_ID              PAYROLL.EXPENSE_CLAIM_MASTER.STATUS_ID%TYPE,
    STATUS_DESC            DEFINITIONS.ORDER_STATUS.DESCRIPTION%TYPE,
    APPROVER_REMARKS       PAYROLL.EXPENSE_CLAIM_MASTER.APPROVER_REMARKS%TYPE,
    APPROVED_BY            PAYROLL.EXPENSE_CLAIM_MASTER.APPROVED_BY%TYPE,
    APPROVE_BY_NAME        REGISTRATION.PATIENT.NAME%TYPE,
    APPROVE_BY_DESIG       DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    APPROVE_BY_DEPT        DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    APPROVED_DATE          PAYROLL.EXPENSE_CLAIM_MASTER.APPROVED_DATE%TYPE,
    TRAVEL_REQUEST_NO      PAYROLL.EXPENSE_CLAIM_MASTER.TRAVEL_REQUEST_NO%TYPE,
    REVISION_NO            PAYROLL.EXPENSE_CLAIM_MASTER.REVISION_NO%TYPE,
    RN_TRAVEL_REQUEST_NO   VARCHAR2(4000),
    ORGANIZATION_ID        PAYROLL.EXPENSE_CLAIM_MASTER.ORGANIZATION_ID%TYPE,
    LOCATION_ID            PAYROLL.EXPENSE_CLAIM_MASTER.LOCATION_ID%TYPE,
    LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    DEPARTURE_DATE         PAYROLL.EXPENSE_CLAIM_MASTER.DEPARTURE_DATE%TYPE,
    RETURN_DATE            PAYROLL.EXPENSE_CLAIM_MASTER.RETURN_DATE%TYPE,
    REMARKS                PAYROLL.EXPENSE_CLAIM_MASTER.REMARKS%TYPE,
    EXPENSE_CON_TYPE       PAYROLL.DEF_EXPENSE_CONSTANT.TYPE%TYPE,
    AUTHORITY_MRNO         PAYROLL.EXPENSE_CLAIM_MASTER.AUTHORITY_MRNO%TYPE,
    WFE_NO                 PAYROLL.EXPENSE_CLAIM_MASTER.WFE_NO%TYPE,
    SCHEMA_ID              PAYROLL.EXPENSE_CLAIM_WORKFLOW.SCHEMA_ID%TYPE,
    WORKFLOW_TYPE_ID       PAYROLL.EXPENSE_CLAIM_WORKFLOW.WORKFLOW_TYPE_ID%TYPE,
    WORK_FLOW_ID           PAYROLL.EXPENSE_CLAIM_WORKFLOW.WORK_FLOW_ID%TYPE,
    EVENT_ID               DEFINITIONS.EVENT.EVENT_ID%TYPE,
    EVENT_ORDERBY          DEFINITIONS.PR_TYPE_FLOW_EVENT.ORDER_BY%TYPE,
    EVENT_DESC             DEFINITIONS.EVENT.DESCRIPTION%TYPE,
    NEXT_EVENT_ID          DEFINITIONS.EVENT.EVENT_ID%TYPE,
    CURRENT_GROSS          PAYROLL.PAY_MASTER.CALC_BASIC%TYPE,
    VOUCHER_TYPE           PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO             PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_NO%TYPE,
    CANCELLED_VOUCHER_TYPE PAYROLL.EXPENSE_CLAIM_MASTER.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCELLED_VOUCHER_NO   PAYROLL.EXPENSE_CLAIM_MASTER.CANCELLED_VOUCHER_NO%TYPE,
    REFUND_NO              PAYROLL.EXPENSE_CLAIM_MASTER.REFUND_NO%TYPE,
    CURRENT_STAUS          DEFINITIONS.EVENT.DESCRIPTION%TYPE,
    DOCUMENT_ATTACHED      VARCHAR2(1));
  -- Ref Cursor --
  TYPE EXP_CLAIM_MASTER_REF IS REF CURSOR RETURN EXP_CLAIM_MASTER_REC;
  -- Associative Array --
  TYPE EXP_CLAIM_MASTER_TAB IS TABLE OF EXP_CLAIM_MASTER_REC INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------------
  -- This procedure will be used to query data from Expense Claim Master Table --
  -------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_MASTER(P_BLOCK_DATA     IN OUT EXP_CLAIM_MASTER_REF,
                                   P_CLAIM_NO       IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                   P_EXPENSE_TYPE   IN PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE,
                                   P_MRNO           IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE,
                                   P_AUTHORITY_MRNO IN PAYROLL.EXPENSE_CLAIM_MASTER.AUTHORITY_MRNO%TYPE,
                                   P_EVENT_ID       IN DEFINITIONS.EVENT.EVENT_ID%TYPE);
  --------------------------------------------------------------------------------
  -- This procedure will be used to insert data into Expense Claim Master Table --
  --------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ------------------------------------------------------------------------------
  -- This procedure will be used to update data in Expense Claim Master Table --
  ------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  --------------------------------------------------------------------------------
  -- This procedure will be used to delete data from Expense Claim Master Table --
  ---------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ---------------------------------------------------------------------------------------
  -- This procedure will be used to lock record for DMLs on Expense Claim Master Table --
  ---------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB);
  ---------------------------------------------------
  -- Record Type declaration for Detail Table Data --
  ---------------------------------------------------
  TYPE EXP_CLAIM_DETAIL_REC IS RECORD(
    CLAIM_NO          PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
    SRNO              PAYROLL.EXPENSE_CLAIM_DETAIL.SRNO%TYPE,
    EXPENSE_TYPE_ID   PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE,
    EXPENSE_TYPE_DESC DEFINITIONS.EXPENSE.DESCRIPTION%TYPE,
    FROM_DATE         PAYROLL.EXPENSE_CLAIM_DETAIL.FROM_DATE%TYPE,
    TO_DATE           PAYROLL.EXPENSE_CLAIM_DETAIL.TO_DATE%TYPE,
    CLAIM_AMOUNT      PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_AMOUNT%TYPE,
    APPROVED_AMOUNT   PAYROLL.EXPENSE_CLAIM_DETAIL.APPROVED_AMOUNT%TYPE,
    REMARKS           PAYROLL.EXPENSE_CLAIM_DETAIL.REMARKS%TYPE,
    DAYS_CLAIMED      PAYROLL.EXPENSE_CLAIM_DETAIL.DAYS_CLAIMED%TYPE,
    DAYS_APPROVED     PAYROLL.EXPENSE_CLAIM_DETAIL.DAYS_APPROVED%TYPE,
    SLAB_ID           BILLING.DEF_SLAB.SLAB_ID%TYPE,
    SLAB_DESCRIPTION  BILLING.DEF_SLAB.DESCRIPTION%TYPE,
    ENTRY_TYPE        PAYROLL.EXPENSE_CLAIM_DETAIL.ENTRY_TYPE%TYPE,
    CALC_METHOD       PAYROLL.EXPENSE_CLAIM_DETAIL.CALC_METHOD%TYPE);
  -- Ref Cursor --
  TYPE EXP_CLAIM_DETAIL_REF IS REF CURSOR RETURN EXP_CLAIM_DETAIL_REC;
  -- Associative Array --
  TYPE EXP_CLAIM_DETAIL_TAB IS TABLE OF EXP_CLAIM_DETAIL_REC INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------------
  -- This procedure will be used to query data from Expense Claim Detail Table --
  -------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_DETAIL(P_BLOCK_DATA      IN OUT EXP_CLAIM_DETAIL_REF,
                                   P_CLAIM_NO        IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE,
                                   P_EXPENSE_TYPE_ID IN PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE);
  --------------------------------------------------------------------------------
  -- This procedure will be used to insert data into Expense Claim Detail Table --
  --------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ------------------------------------------------------------------------------
  -- This procedure will be used to update data in Expense Claim Detail Table --
  ------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  --------------------------------------------------------------------------------
  -- This procedure will be used to delete data from Expense Claim Detail Table --
  --------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ---------------------------------------------------------------------------------------
  -- This procedure will be used to lock record for DMLs on Expense Claim Detail Table --
  ---------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB);
  ----------------------------------------------------
  -- Record Type declaration for Project Table Data --
  ----------------------------------------------------
  TYPE EXP_CLAIM_PROJECT_REC IS RECORD(
    CLAIM_NO       PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
    PROJECT_ID     PAYROLL.EXPENSE_CLAIM_PROJECT.PROJECT_ID%TYPE,
    PROJECT_NAME   PAYROLL.DEF_PROJECT.PROJECT_NAME%TYPE,
    EXP_PERCENTAGE PAYROLL.EXPENSE_CLAIM_PROJECT.EXP_PERCENTAGE%TYPE,
    REMARKS        PAYROLL.EXPENSE_CLAIM_PROJECT.REMARKS%TYPE);
  -- Ref Cursor --
  TYPE EXP_CLAIM_PROJECT_REF IS REF CURSOR RETURN EXP_CLAIM_PROJECT_REC;
  -- Associative Array --
  TYPE EXP_CLAIM_PROJECT_TAB IS TABLE OF EXP_CLAIM_PROJECT_REC INDEX BY BINARY_INTEGER;
  --------------------------------------------------------------------------------
  -- This procedure will be used to query data from Expense Claim Project Table --
  --------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_REF,
                                    P_CLAIM_NO   IN PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE);
  ---------------------------------------------------------------------------------
  -- This procedure will be used to insert data into Expense Claim Project Table --
  ---------------------------------------------------------------------------------
  PROCEDURE INSERT_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  -------------------------------------------------------------------------------
  -- This procedure will be used to update data in Expense Claim Project Table --
  -------------------------------------------------------------------------------
  PROCEDURE UPDATE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  ---------------------------------------------------------------------------------
  -- This procedure will be used to delete data from Expense Claim Project Table --
  ---------------------------------------------------------------------------------
  PROCEDURE DELETE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);
  ----------------------------------------------------------------------------------------
  -- This procedure will be used to lock record for DMLs on Expense Claim Project Table --
  ----------------------------------------------------------------------------------------
  PROCEDURE LOCK_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_DETAIL IS RECORD(
    CLAIM_NO           PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE,
    REFUND_NO          PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
    LOAN_NO            PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
    LOAN_DATE          PAYROLL.LOAN_PAYMENT_MASTER.TRANS_DATE%TYPE,
    LOAN_TYPE          PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    REFUND_LOCATION    DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    LOAN_AMOUNT        PAYROLL.LOAN_PAYMENT_MASTER.LOAN_AMOUNT%TYPE,
    REFUND_AMOUNT      PAYROLL.LOAN_REFUND_DETAIL.REFUND_AMOUNT%TYPE,
    BALANCE            NUMBER(20, 2),
    TEMP_REFUND_AMOUNT PAYROLL.LOAN_REFUND_DETAIL.TEMP_REFUND_AMOUNT%TYPE,
    MRNO               PAYROLL.LOAN_REFUND_DETAIL.MRNO%TYPE,
    REFUND_LOCATION_ID PAYROLL.LOAN_REFUND_DETAIL.REFUND_LOCATION_ID%TYPE,
    LINK_TRAVEL        VARCHAR2(50));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_DETAIL IS REF CURSOR RETURN REC_LOAN_REFUND_DETAIL;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_DETAIL IS TABLE OF REC_LOAN_REFUND_DETAIL INDEX BY BINARY_INTEGER;
  -------------------------------------------
  -- This procedure will query LOAN_REFUND --
  -------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT REF_LOAN_REFUND_DETAIL,
                                     P_CLAIM_NO   IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                                     P_MRNO       IN HRD.INFORMATION.MRNO%TYPE,
                                     P_REFUND_NO  IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE,
                                     P_REQUEST_ID IN PAYROLL.LOAN_PAYMENT_MASTER.TRAVEL_REQUEST_NO%TYPE);

  ---------------------------------------------------------------------
  -- This procedure will be used to update data in LOAN_REFUND Table --
  ---------------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT TAB_LOAN_REFUND_DETAIL);
  ------------------------------------------------------------------------------
  -- This procedure will be used to lock record for DMLs on LOAN_REFUND Table --
  ------------------------------------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT TAB_LOAN_REFUND_DETAIL);

END PKG_S16FRM00072;
```

#### PAYROLL.PKG_S16FRM00076
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00076 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-OCT-2017   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC   DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_START_DATE  PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
    PAY_END_DATE    PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS   DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT       IN OUT REF_GL_TRAN_MASTER,
                                 P_LOCATION_ID  IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                 P_START_DATE   IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                 P_END_DATE     IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_TMP_DETAIL IS RECORD(
    LOCATION_ID        PAYROLL.PAY_VOUCHER_TEMP .LOCATION_ID%TYPE,
    PAY_START_DATE     PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
    PAY_END_DATE       PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    MRNO               PAYROLL.PAY_VOUCHER_TEMP.MRNO%TYPE,
    NAME               VARCHAR2(250),
    GRADE              VARCHAR2(250),
    DESIGNATION        VARCHAR2(250),
    DEPARTMENT         VARCHAR2(250),
    DESCRIPTION        VARCHAR2(250),
    GL_SETUP_CODE      PAYROLL.PAY_VOUCHER_TEMP.GL_SETUP_CODE%TYPE,
    GL_SETUP_DESC      PAYROLL.DEF_GL_SETUP_MASTER.DESCRIPTION%TYPE,
    AMOUNT             PAYROLL.PAY_VOUCHER_TEMP2.DR_AMOUNT%TYPE,
    ARREARS            PAYROLL.PAY_ARREAR.AMOUNT%TYPE,
    AD_AMOUNT          PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_TMP_DETAIL IS REF CURSOR RETURN REC_TMP_DETAIL;
  PROCEDURE QUERY_TMP_DETAIL_CR(P_RESULT             IN OUT REF_TMP_DETAIL,
                                P_LOCATION_ID        IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                P_START_DATE         IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                P_END_DATE           IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                P_LEDGER_TYPE_CODE   IN FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
                                P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                                P_COA_CODE           IN FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
                                P_MRNO               IN PAYROLL.PAY_VOUCHER_TEMP.MRNO%TYPE,
                                P_ORDER_BY           IN VARCHAR2);
  PROCEDURE QUERY_TMP_DETAIL_DR(P_RESULT             IN OUT REF_TMP_DETAIL,
                                P_LOCATION_ID        IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                P_START_DATE         IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                P_END_DATE           IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                P_LEDGER_TYPE_CODE   IN FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
                                P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                                P_COA_CODE           IN FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
                                P_MRNO               IN PAYROLL.PAY_VOUCHER_TEMP.MRNO%TYPE,
                                P_ORDER_BY           IN VARCHAR2);
END;
```

#### PAYROLL.PKG_S16FRM00077
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00077 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL LOAN PAYMENT
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        25-Jan-2019   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_PAYMENT_MASTER IS RECORD(
    LOAN_NO                     PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    ND_EMPLOYEE_NAME            REGISTRATION.PATIENT.NAME%TYPE,
    ND_LOAN_TYPE_DESC           PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    ND_CURRENCY_DESC            DEFINITIONS.CURRENCY.DESCRIPTION%TYPE,
    LOAN_LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    TRANS_TYPE                  PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_TYPE%TYPE,
    TRANS_DATE                  PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE,
    MRNO                        REGISTRATION.PATIENT.MRNO%TYPE,
    LOAN_CODE                   PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_CODE%TYPE,
    OPEN_ACTUAL_DATE            PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_DATE%TYPE,
    OPEN_ACTUAL_LOAN            PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_LOAN%TYPE,
    OPEN_ACTUAL_INSTALLMENTS    PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_INSTALLMENTS%TYPE,
    OPEN_ACTUAL_MONTHLY         PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_MONTHLY%TYPE,
    TEMP_LOAN_AMOUNT            PAYROLL.LOAN_PAYMENT_MASTER_N.TEMP_LOAN_AMOUNT%TYPE,
    LOAN_AMOUNT                 PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    INTEREST_AMOUNT             PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_AMOUNT%TYPE,
    NO_OF_INSTALLMENTS          PAYROLL.LOAN_PAYMENT_MASTER_N.NO_OF_INSTALLMENTS%TYPE,
    LOAN_INSTALLMENT            PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_INSTALLMENT%TYPE,
    INTEREST_INSTALLMENT        PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_INSTALLMENT%TYPE,
    REFUND_AMOUNT               PAYROLL.LOAN_PAYMENT_MASTER_N.REFUND_AMOUNT%TYPE,
    PAID_INTEREST               PAYROLL.LOAN_PAYMENT_MASTER_N.PAID_INTEREST%TYPE,
    VOUCHER_TYPE                FINANCE.GL_VOUCHER_TYPE.VOUCHER_TYPE%TYPE,
    VOUCHER_NO                  FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    STOP_AUTO_DEDUCTION         PAYROLL.LOAN_PAYMENT_MASTER_N.STOP_AUTO_DEDUCTION%TYPE,
    REMARKS                     PAYROLL.LOAN_PAYMENT_MASTER_N.REMARKS%TYPE,
    CANCEL_VOUCHER_TYPE         PAYROLL.LOAN_PAYMENT_MASTER_N.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCEL_VOUCHER_NO           PAYROLL.LOAN_PAYMENT_MASTER_N.CANCELLED_VOUCHER_NO%TYPE,
    STOP_AUTO_DEDUCTION_TILL    PAYROLL.LOAN_PAYMENT_MASTER_N.STOP_AUTO_DEDUCTION_TILL%TYPE,
    BASE_AMOUNT                 PAYROLL.LOAN_PAYMENT_MASTER_N.TEMP_LOAN_AMOUNT%TYPE,
    BASE_CURRENCY_ID            PAYROLL.LOAN_PAYMENT_MASTER_N.BASE_CURRENCY_ID%TYPE,
    BASE_CURRENCY_EXCHANGE_RATE PAYROLL.LOAN_PAYMENT_MASTER_N.BASE_CURRENCY_EXCHANGE_RATE%TYPE,
    LOAN_LOCATION_ID            DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    VOUCHER_STATUS              FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE                      PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE,
    STATUS_ID                   ORDERENTRY.ORDER_STATUS.ORDER_STATUS_ID%TYPE,
    STATUS_DESC                 ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_PAYMENT_MASTER IS REF CURSOR RETURN REC_LOAN_PAYMENT_MASTER;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_PAYMENT_MASTER IS TABLE OF REC_LOAN_PAYMENT_MASTER INDEX BY BINARY_INTEGER;
  -----------------------------------------------------------
  -- This procedure will QUERY PAYROLL.LOAN_PAYMENT_MASTER --
  -----------------------------------------------------------
  PROCEDURE QUERY_LOAN_PAYMENT_MASTER(P_RESULT  IN OUT REF_LOAN_PAYMENT_MASTER,
                                      P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                                      P_MRNO    IN REGISTRATION.PATIENT.MRNO%TYPE);
  ------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE INSERT_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ------------------------------------------------------------
  -- This procedure will update PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE DELETE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_PAYMENT_MASTER --
  ----------------------------------------------------------
  PROCEDURE LOCK_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PROFIT IS RECORD(
    LOAN_NO             PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    YEAR_CODE           PAYROLL.LOAN_PAYMENT_INTEREST.YEAR_CODE%TYPE,
    PRINCIPAL_AMOUNT    PAYROLL.LOAN_PAYMENT_INTEREST.PRINCIPAL_AMOUNT%TYPE,
    NO_OF_MONTHS        PAYROLL.LOAN_PAYMENT_INTEREST.NO_OF_MONTHS%TYPE,
    INTEREST_AMOUNT     PAYROLL.LOAN_PAYMENT_INTEREST.INTEREST_AMOUNT%TYPE,
    INTEREST_RATE       NUMBER,
    VOUCHER_TYPE        PAYROLL.LOAN_PAYMENT_INTEREST.VOUCHER_TYPE%TYPE,
    VOUCHER_NO          PAYROLL.LOAN_PAYMENT_INTEREST.VOUCHER_NO%TYPE,
    CANCEL_VOUCHER_TYPE PAYROLL.LOAN_PAYMENT_INTEREST.CANCEL_VOUCHER_TYPE%TYPE,
    CANCEL_VOUCHER_NO   PAYROLL.LOAN_PAYMENT_INTEREST.CANCEL_VOUCHER_NO%TYPE,
    CANCELLED           PAYROLL.LOAN_PAYMENT_INTEREST.CANCELLED%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PROFIT IS REF CURSOR RETURN REC_PROFIT;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PROFIT IS TABLE OF REC_PROFIT; -- INDEX BY BINARY_INTEGER;

  --------------------------------------------
  -- This procedure will query Profit Block --
  --------------------------------------------
  PROCEDURE QUERY_PROFIT(P_RESULT  IN OUT REF_PROFIT,
                         P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    LOAN_NO         PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    REFERENCE_NO    FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    PARTY_NAME      FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    PARTY_SUB_CODE  FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    MRNO            FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    LOCATION_ID     FINANCE.GL_TRAN_MASTER.LOCATION_ID%TYPE,
    DR_CR_GENERAL   FINANCE.GL_VOUCHER_TYPE.DR_CR_GENERAL%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT  IN OUT REF_GL_TRAN_MASTER,
                                 P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                                 P_MODULE  IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will Delete FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                 P_MODULE       IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL1 IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL1 IS REF CURSOR RETURN REC_GL_TRAN_DETAIL1;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB1 IS TABLE OF REC_GL_TRAN_DETAIL1 INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL1(P_RESULT       IN OUT REF_GL_TRAN_DETAIL1,
                                  P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_MODULE       IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1,
                                   P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1,
                                   P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1,
                                   P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1,
                                 P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ---------------------------
  -- Voucher detail Record --
  ---------------------------
  TYPE TRAN_DETAIL_REC IS RECORD(
    DEBIT_CREDIT       CHAR(1),
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    IS_NEW             CHAR(1));

  TYPE TRAN_DETAIL_TAB IS TABLE OF TRAN_DETAIL_REC;

  ----------------------------------------------------
  -- FOLLOWING PROCEDURE WILL GENERATE TEMP VOUCHER --
  ----------------------------------------------------
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID       IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID           IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_LOAN_NO               IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                                  P_VOUCHER_TYPE          IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO            IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_COA_CODE              IN FINANCE.GL_TRANSFER_DETAIL.COA_CODE%TYPE,
                                  P_LEDGER_TYPE_CODE      IN FINANCE.GL_TRANSFER_DETAIL.LEDGER_TYPE_CODE%TYPE,
                                  P_SUB_LEDGER_ITEM_CODE  IN FINANCE.GL_TRANSFER_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                                  P_INTEREST_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_INTEREST_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE            IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID           IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE         IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS               IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                  P_LOGIN_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO             IN VARCHAR2,
                                  P_TERMINAL              IN VARCHAR2,
                                  P_OBJECT_CODE           IN VARCHAR2,
                                  P_NEW_VOUCHER_NO        OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT            OUT VARCHAR2,
                                  P_STOP                  OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_TEMP_VOUCHER(P_ORGANIZATION_ID       IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID           IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_LOAN_NO               IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                              P_VOUCHER_TYPE          IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO            IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_INTEREST_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_INTEREST_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_TEMP_LOAN_AMOUNT      IN PAYROLL.LOAN_PAYMENT_MASTER_N.TEMP_LOAN_AMOUNT%TYPE,
                              P_LOGIN_LOCATION_ID     IN VARCHAR2,
                              P_USER_MRNO             IN VARCHAR2,
                              P_TERMINAL              IN VARCHAR2,
                              P_OBJECT_CODE           IN VARCHAR2,
                              P_NEW_VOUCHER_NO        OUT VARCHAR2,
                              P_ALERT_TEXT            OUT VARCHAR2,
                              P_STOP                  OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_LOAN_NO           IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_LOGIN_LOCATION_ID IN VARCHAR2,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID       IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID           IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_LOAN_NO               IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                                  P_VOUCHER_TYPE          IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO            IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_INTEREST_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_INTEREST_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_LOGIN_LOCATION_ID     IN VARCHAR2,
                                  P_USER_MRNO             IN VARCHAR2,
                                  P_TERMINAL              IN VARCHAR2,
                                  P_OBJECT_CODE           IN VARCHAR2,
                                  P_NEW_VOUCHER_TYPE      OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_NEW_VOUCHER_NO        OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT            OUT VARCHAR2,
                                  P_STOP                  OUT CHAR);
  --------------------------------------------------------------------
  -- Following function is used to get payroll process end date  --
  --------------------------------------------------------------------
  FUNCTION IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN DATE;

  -----------------------------------------------------------------------------------------
  -- Following function is used to validate employee to populate necessary information   --
  -----------------------------------------------------------------------------------------
  FUNCTION IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN BOOLEAN;

  ----------------------------------------------------------------------------------
  -- Following function is used to generate refund number w.r.t location id    --
  ----------------------------------------------------------------------------------
  FUNCTION GENERATE_LOAN_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN VARCHAR2;
  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);

  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
  -----------------------------------------------------------
  -- This function will get reference required or not     --
  -----------------------------------------------------------
  FUNCTION GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2)
    RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE;
END PKG_S16FRM00077;
```

#### PAYROLL.PKG_S16FRM00078
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00078 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        19-Feb-2019   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_MASTER IS RECORD(
    REFUND_NO              PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
    REFUND_DATE            PAYROLL.LOAN_REFUND_MASTER_N.TRANS_DATE%TYPE,
    MRNO                   PAYROLL.LOAN_REFUND_MASTER_N.MRNO%TYPE,
    NAME                   REGISTRATION.PATIENT.NAME%TYPE,
    REFUND_AMOUNT          PAYROLL.LOAN_REFUND_MASTER_N.REFUND_AMOUNT%TYPE,
    REFUND_REMARKS         PAYROLL.LOAN_REFUND_MASTER_N.REMARKS%TYPE,
    CANCELLED_VOUCHER_TYPE PAYROLL.LOAN_REFUND_MASTER_N.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCELLED_VOUCHER_NO   PAYROLL.LOAN_REFUND_MASTER_N.CANCELLED_VOUCHER_NO%TYPE,
    REFUND_TYPE            PAYROLL.LOAN_REFUND_MASTER_N.REFUND_TYPE%TYPE,
    START_DATE             PAYROLL.LOAN_REFUND_MASTER_N.PAY_START_DATE%TYPE,
    END_DATE               PAYROLL.LOAN_REFUND_MASTER_N.PAY_END_DATE%TYPE,
    LOCATION_ID            DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    VOUCHER_TYPE           FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO             FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    VOUCHER_STATUS         FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE                 PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE,
    RECEIPT_NO             PAYROLL.LOAN_REFUND_MASTER_N.RECEIPT_NO%TYPE,
    STATUS_ID              ORDERENTRY.ORDER_STATUS.ORDER_STATUS_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_MASTER IS REF CURSOR RETURN REC_LOAN_REFUND_MASTER;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_MASTER IS TABLE OF REC_LOAN_REFUND_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will QUERY FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_MASTER(P_RESULT    IN OUT REF_LOAN_REFUND_MASTER,
                                     P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                     P_MRNO      IN PAYROLL.LOAN_REFUND_MASTER_N.MRNO%TYPE);
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------------------------------------------
  -- This procedure will DELETE LOAN_REFUND_MASTER_N --
  ------------------------------------------------------
  PROCEDURE DELETE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_DETAIL IS RECORD(
    REFUND_NO          PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
    LOAN_NO            PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    LOAN_DATE          PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE,
    LOAN_TYPE          PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    REFUND_LOCATION    DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    LOAN_AMOUNT        PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    REFUND_AMOUNT      PAYROLL.LOAN_REFUND_DETAIL_N.REFUND_AMOUNT%TYPE,
    LOAN_BALANCE       PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    INTEREST_AMOUNT    PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_AMOUNT%TYPE,
    BALANCE            PAYROLL.LOAN_PAYMENT_MASTER_N.REFUND_AMOUNT%TYPE,
    TEMP_REFUND_AMOUNT PAYROLL.LOAN_REFUND_DETAIL_N.TEMP_REFUND_AMOUNT%TYPE,
    MRNO               REGISTRATION.PATIENT.MRNO%TYPE,
    REFUND_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    MODULE             PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_DETAIL IS REF CURSOR RETURN REC_LOAN_REFUND_DETAIL;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_DETAIL IS TABLE OF REC_LOAN_REFUND_DETAIL INDEX BY BINARY_INTEGER;
  ----------------------------------------------------------
  -- This procedure will query PAYROLL.LOAN_REFUND_MASTER_N --
  ----------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_DETAIL(P_RESULT    IN OUT REF_LOAN_REFUND_DETAIL,
                                     P_MRNO      IN HRD.INFORMATION.MRNO%TYPE,
                                     P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL_N.REFUND_NO%TYPE,
                                     P_MODULE    IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE);

  --------------------------------------------------------------------
  -- This procedure will update PAYROLL.LOAN_REFUND_DETAIL_N --
  --------------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL);
  --------------------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_REFUND_(MASTER/DETAIL) --
  --------------------------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    REFUND_NO       PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    REFERENCE_NO    FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    PARTY_NAME      FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    PARTY_SUB_CODE  FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    MRNO            FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    LOCATION_ID     FINANCE.GL_TRAN_MASTER.LOCATION_ID%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT    IN OUT REF_GL_TRAN_MASTER,
                                 P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                 P_MODULE    IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);

  ------------------------------------------------------
  -- This procedure will Delete FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);

  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER,
                                P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                 P_MODULE       IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                  P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB,
                                P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE);

  ----------------------------------------------------
  -- FOLLOWING PROCEDURE WILL INSERT GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MODULE            IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE,
                                  P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE        IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID       IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE     IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS           IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_MODULE            IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE,
                              P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                              P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_LOGIN_LOCATION_ID IN VARCHAR2,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_OBJECT_CODE       IN VARCHAR2,
                              P_NEW_VOUCHER_NO    OUT VARCHAR2,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_MODULE            IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE,
                                P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_LOGIN_LOCATION_ID IN VARCHAR2,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MODULE            IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE,
                                  P_REFUND_NO         IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_LOGIN_LOCATION_ID IN VARCHAR2,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  --------------------------------------------------------------------
  -- Following function is used to get payroll process end date  --
  --------------------------------------------------------------------
  FUNCTION IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN DATE;

  -----------------------------------------------------------------------------------------
  -- Following function is used to validate employee to populate necessary information   --
  -----------------------------------------------------------------------------------------
  FUNCTION IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE)
    RETURN BOOLEAN;

  ----------------------------------------------------------------------------------
  -- Following function is used to generate refund number w.r.t location id    --
  ----------------------------------------------------------------------------------
  FUNCTION GENERATE_REFUND_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN VARCHAR2;
  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);

  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
END PKG_S16FRM00078;
```

#### PAYROLL.PKG_S16FRM00080
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00080 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-OCT-2017   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PF_TRAN_MASTER IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC      DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_START_DATE     PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
    PAY_END_DATE       PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
    PAY_VOUCHER_TYPE   PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
    PAY_VOUCHER_TYPE_D PAYROLL.DEF_PAY_VOUCHER_TYPE.DESCRIPTION%TYPE,
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC    DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS      DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS            FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS     FINANCE.PF_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID          FINANCE.PF_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE       FINANCE.PF_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY         FINANCE.PF_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE        FINANCE.PF_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY          FINANCE.PF_TRAN_MASTER.POSTED_BY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PF_TRAN_MASTER IS REF CURSOR RETURN REC_PF_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PF_TRAN_MASTER IS TABLE OF REC_PF_TRAN_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will query FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_PF_TRAN_MASTER(P_RESULT           IN OUT REF_PF_TRAN_MASTER,
                                 P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE,
                                 P_LOCATION_ID      IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                 P_START_DATE       IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                 P_END_DATE         IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                 P_VOUCHER_TYPE     IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO       IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);
  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PF_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.PF_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.PF_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.PF_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.PF_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.PF_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.PF_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PF_TRAN_DETAIL IS REF CURSOR RETURN REC_PF_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE PF_TRAN_DETAIL_TAB IS TABLE OF REC_PF_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_PF_TRAN_DETAIL(P_RESULT       IN OUT REF_PF_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
END;
```

#### PAYROLL.PKG_S16FRM00085
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00085 IS

  /***********************************************************************************************
         OBJECTIVE := This package will be used for the calculations of Package Billing
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        26-DEC-2018   Farhan Akram          1. Creation of this package
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  --------------------------------------------
  -- Record Type for Employee Final Invoice --
  --------------------------------------------
  TYPE PIM_REC IS RECORD(
    PROCESS_ID          BILLING.CORPORATE_INVOICE_MASTER .PROCESS_ID%TYPE,
    PROCESS_DATE        BILLING.CORPORATE_INVOICE_MASTER.PROCESS_DATE%TYPE,
    STATUS_ID           BILLING.CORPORATE_INVOICE_MASTER.STATUS_ID%TYPE,
    STATUS_DESC         ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE,
    REMARKS             BILLING.CORPORATE_INVOICE_MASTER.REMARKS%TYPE,
    POSTED_BY_NAME      VARCHAR2(192),
    POSTED_DATE         BILLING.CORPORATE_INVOICE_MASTER.POSTED_DATE%TYPE,
    CANCELLED_BY_NAME   VARCHAR2(192),
    CANCELLED_DATE      BILLING.CORPORATE_INVOICE_MASTER.CANCELLED_DATE%TYPE,
    INCREMENT_CODE      PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_CODE%TYPE,
    INCREMTNT_DESC      PAYROLL.DEF_INCREMENT_TYPE.DESCRIPTION%TYPE,
    INCREMENT_DATE      PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
    EFFECTIVE_DATE      PAYROLL.PROCESS_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE,
    ADD_ARREARS         PAYROLL.PROCESS_INCREMENT_MASTER.ADD_ARREARS%TYPE,
    INCREASE_STAGE      PAYROLL.DEF_INCREMENT_TYPE.INCREASE_STAGE%TYPE,
    PAYROLL_LOCATION_ID BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
    ORGANIZATION_ID     BILLING.CORPORATE_INVOICE_MASTER.ORGANIZATION_ID%TYPE,
    INCR_SLAB_ID        PAYROLL.PROCESS_INCREMENT_MASTER.INCR_SLAB_ID%TYPE,
    SLAB_DESC           BILLING.DEF_SLAB.DESCRIPTION%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE PIM_REF IS REF CURSOR RETURN PIM_REC;

  -----------
  -- Array --
  -----------
  TYPE PIM_TAB IS TABLE OF PIM_REC INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------
  -- This Procedure will Query the Corporate Invoice Master --
  -------------------------------------------------------------
  /*PROCEDURE QUERY_CIM(P_RESULT     IN OUT BILLING.PKG_S16FRM00085.CFI_REF,
                      P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                      P_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE);
  
  -------------------------------------------------------------
  -- This Procedure will Insert the Corporate Invoice Master --
  -------------------------------------------------------------
  PROCEDURE INSERT_CIM(P_BLOCK_DATA  IN OUT BILLING.PKG_S16FRM00085.EFI_TAB);
  
  -------------------------------------------------------------
  -- This Procedure will update the Corporate Invoice Master --
  -------------------------------------------------------------
  PROCEDURE UPDATE_CIM(P_BLOCK_DATA IN OUT BILLING.PKG_S16FRM00085.EFI_TAB);
  
  ----------------------------------------------------------------------------
  -- This Procedure will Delete the Employee Cafe + Indemnity Final Invoice --
  ----------------------------------------------------------------------------
  PROCEDURE DELETE_CIM(P_BLOCK_DATA IN OUT BILLING.PKG_S16FRM00085.EFI_TAB);
  
  ----------------------------------------------------------------------------
  -- This Procedure will Lock the Employee Cafe + Indemnity Final Invoice --
  ----------------------------------------------------------------------------
  PROCEDURE LOCK_CIM(P_BLOCK_DATA IN OUT BILLING.PKG_S16FRM00085.EFI_TAB);*/

  ----------------------------------------------
  -- Record type for Process Patient Packages --
  ----------------------------------------------
  TYPE INC_MEMBER_REC IS RECORD(
    PROCESS_ID       BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
    MRNO             REGISTRATION.PATIENT.MRNO%TYPE,
    PATIENT_TYPE_ID  PAYROLL.PROCESS_MEMBERS.PATIENT_TYPE_ID%TYPE,
    EMPLOYEE_TYPE    DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
    DESIGNATION_ID   PAYROLL.PROCESS_MEMBERS.DESIGNATION_ID%TYPE,
    DESIGNATION_DESC DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    GRADE_ID         PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
    GRADE_DESC       DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    DEPARTMENT_ID    PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
    DEPARTMENT_DESC  DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    LOCATION_ID      PAYROLL.PROCESS_MEMBERS.LOCATION_ID%TYPE,
    ORGANIZATION_ID  PAYROLL.PROCESS_MEMBERS.ORGANIZATION_ID%TYPE,
    JOINING_DATE     PAYROLL.PROCESS_MEMBERS.JOINING_DATE%TYPE,
    SELECT_FLAG      PAYROLL.PROCESS_MEMBERS.SELECT_FLAG%TYPE,
    PROCESS_LOG      PAYROLL.PROCESS_MEMBERS.PROCESS_LOG%TYPE,
    STATUS_ID        PAYROLL.PROCESS_MEMBERS.STATUS_ID%TYPE,
    STATUS_DESC      ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE,
    INCR_AMOUNT      PAYROLL.TEMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE,
    INCR_PERCENT     PAYROLL.TEMP_INCREMENT_MASTER.INCR_PERCENT%TYPE,
    SETUP_BASIC      PAYROLL.TEMP_INCREMENT_MASTER.SETUP_BASIC%TYPE,
    SETUP_GROSS      PAYROLL.TEMP_INCREMENT_MASTER.SETUP_GROSS%TYPE,
    PROPOSED_BASIC   PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_BASIC%TYPE,
    PROPOSED_GROSS   PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE,
    REMARKS          PAYROLL.TEMP_INCREMENT_MASTER.REMARKS%TYPE,
    ARREAR_PAID      PAYROLL.TEMP_INCREMENT_MASTER.ARREAR_PAID%TYPE,
    EMP_NAME         VARCHAR2(250),
    STAGE_NO         PAYROLL.PROCESS_MEMBERS.STAGE_NO%TYPE,
    EFFECTIVE_DATE   PAYROLL.PROCESS_MEMBERS.EFFECTIVE_DATE%TYPE,
    VERIFIED         PAYROLL.PROCESS_MEMBERS.VERIFIED%TYPE);
  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE INC_MEMBER_TAB IS TABLE OF INC_MEMBER_REC INDEX BY BINARY_INTEGER;

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE INC_MEMBER_REF IS REF CURSOR RETURN INC_MEMBER_REC;
  TYPE TAB_POPULATE IS TABLE OF INC_MEMBER_REC;

  ----------------------------------------
  -- Record group for Service Type wise --
  ----------------------------------------
  TYPE INC_DETAIL_REC IS RECORD(
    PROCESS_ID      PAYROLL.TEMP_INCREMENT_DETAIL.PROCESS_ID%TYPE,
    MRNO            PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
    AD_CODE         PAYROLL.TEMP_INCREMENT_DETAIL.AD_CODE%TYPE,
    AD_DESC         PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    AD_TYPE         PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
    ENTRY_TYPE      PAYROLL.TEMP_INCREMENT_DETAIL.ENTRY_TYPE%TYPE,
    SETUP_AMOUNT    PAYROLL.TEMP_INCREMENT_DETAIL.SETUP_AMOUNT%TYPE,
    PROPOSED_AMOUNT PAYROLL.TEMP_INCREMENT_DETAIL.PROPOSED_AMOUNT%TYPE,
    PROPOSED_CHANGE PAYROLL.TEMP_INCREMENT_DETAIL.PROPOSED_CHANGE%TYPE);

  ----------------
  -- Ref cursor --
  ----------------
  TYPE INC_DETAIL_REF IS REF CURSOR RETURN INC_DETAIL_REC;

  TYPE INC_DETAIL_TAB IS TABLE OF INC_DETAIL_REC INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------
  -- This Procedure will Query the Corporate Invoice Master --
  -------------------------------------------------------------
  PROCEDURE QUERY_PIM(P_RESULT              IN OUT PIM_REF,
                      P_PROCESS_ID          IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                      P_INCREMENT_CODE      IN PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_CODE%TYPE,
                      P_INCREMENT_DATE      IN PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_DATE%TYPE,
                      P_PAYROLL_LOCATION_ID IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE);
  -------------------------------------------------------------
  -- This Procedure will Insert the Corporate Invoice Master --
  -------------------------------------------------------------
  PROCEDURE INSERT_PIM(P_BLOCK_DATA IN OUT PIM_TAB);
  -------------------------------------------------------------
  -- This Procedure will update the Corporate Invoice Master --
  -------------------------------------------------------------
  PROCEDURE UPDATE_PIM(P_BLOCK_DATA IN OUT PIM_TAB);
  ---------------------------------
  -- This Procedure will Delete  --
  ---------------------------------
  PROCEDURE DELETE_PIM(P_BLOCK_DATA IN OUT PIM_TAB);
  -------------------------------------------------------------------
  -- This Procedure will Lock the BILLING.CORPORATE_INVOICE_MASTER --
  -------------------------------------------------------------------
  PROCEDURE LOCK_PIM(P_BLOCK_DATA IN OUT PIM_TAB);

  TYPE GROUP_REC IS RECORD(
    PROCESS_ID      BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
    DESCRIPTION     VARCHAR2(500),
    PATIENT_TYPE_ID PAYROLL.PROCESS_MEMBERS.PATIENT_TYPE_ID%TYPE,
    DEPARTMENT_ID   PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
    GRADE_ID        PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE);
  ----------------
  -- Ref cursor --
  ----------------
  TYPE GROUP_REF IS REF CURSOR RETURN GROUP_REC;

  ------------------------------------------------
  -- This procedure will query DYNAMIC GROUPS   --
  ------------------------------------------------
  PROCEDURE QUERY_GROUP(P_RESULT     IN OUT GROUP_REF,
                        P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                        P_GROUP_TYPE IN VARCHAR2);

  ------------------------------------------------
  -- This procedure will query Process Members --
  ------------------------------------------------
  PROCEDURE QUERY_PROCESS_MEMBERS(P_RESULT          IN OUT INC_MEMBER_REF,
                                  P_PROCESS_ID      IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                  P_PATIENT_TYPE_ID IN PAYROLL.PROCESS_MEMBERS.PATIENT_TYPE_ID%TYPE,
                                  P_DEPARTMENT_ID   IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                                  P_GRADE_ID        IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                                  P_FILTER          IN VARCHAR2,
                                  P_MRNO            IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE);
  -------------------------------------------------
  -- This procedure will update Process Members --
  -------------------------------------------------
  PROCEDURE UPDATE_PROCESS_MEMBERS(P_BLOCK_DATA IN OUT INC_MEMBER_TAB);
  -----------------------------------------------
  -- This procedure will lock Process Members --
  -----------------------------------------------
  PROCEDURE LOCK_PROCESS_MEMBERS(P_BLOCK_DATA IN OUT INC_MEMBER_TAB);
  -----------------------------------------------------------------
  -- This Procedure will query the PAYROLL.TEMP_INCREMENT_DETAIL --
  -----------------------------------------------------------------
  PROCEDURE QUERY_TEMP_INC_DET(P_RESULT     IN OUT INC_DETAIL_REF,
                               P_PROCESS_ID IN PAYROLL.TEMP_INCREMENT_DETAIL.PROCESS_ID%TYPE,
                               P_MRNO       IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                               P_AD_TYPE    IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE);
  -----------------------------------------------------------------
  -- This procedure will insert in PAYROLL.TEMP_INCREMENT_DETAIL --
  -----------------------------------------------------------------
  PROCEDURE INSERT_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB);
  ----------------------------------------------------------------------
  -- This procedure will update data in PAYROLL.TEMP_INCREMENT_DETAIL --
  ----------------------------------------------------------------------
  PROCEDURE UPDATE_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB);
  --------------------------------------------------------------------
  -- This procedure will lock data in PAYROLL.TEMP_INCREMENT_DETAIL --
  --------------------------------------------------------------------
  PROCEDURE LOCK_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB);

  ---------------------------------------------------
  -- This procedure will query Members to populate --
  ---------------------------------------------------
  PROCEDURE QUERY_POPULATE(P_RESULT              IN OUT INC_MEMBER_TAB,
                           P_PROCESS_ID          IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                           P_FMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                           P_TMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                           P_FDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                           P_TDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                           P_FGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                           P_TGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                           P_PTG_ID              IN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE,
                           P_DC_ID               IN DEFINITIONS.DESIGNATION_CATEGORY.DESIGNATION_CATEGORY_ID%TYPE,
                           P_EMP_LOCATION_ID     IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                           P_PAYROLL_LOCATION_ID IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                           P_EMP_TYPE            IN PAYROLL.DEF_EMP_FINANCIAL.EMP_TYPE%TYPE);

  -------------------------------------------------------------
  -- pipeline Function for query Populate --                 
  -----------------------------------------------------------         
  FUNCTION F_QUERY_POPULATE_APEX(P_PROCESS_ID          IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                 P_FMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                                 P_TMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                                 P_FDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                                 P_TDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                                 P_FGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                                 P_TGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                                 P_PTG_ID              IN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE,
                                 P_DC_ID               IN DEFINITIONS.DESIGNATION_CATEGORY.DESIGNATION_CATEGORY_ID%TYPE,
                                 P_EMP_LOCATION_ID     IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                                 P_PAYROLL_LOCATION_ID IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                                 P_EMP_TYPE            IN PAYROLL.DEF_EMP_FINANCIAL.EMP_TYPE%TYPE)
    RETURN TAB_POPULATE
    PIPELINED;
  ---------------------------------------------------------
  -- This Procedure will add/remove the prorcess members --
  ---------------------------------------------------------
  PROCEDURE PROC_ADD_REMOVE_MEMBERS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                    P_ADD_REM           IN VARCHAR2,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  ---------------------------------------------------------
  -- This Procedure will add/remove the prorcess members FOR APEX --
  ---------------------------------------------------------
  PROCEDURE PROC_ADD_REMOVE_MEMBERS_APEX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                         P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                         P_ADD_REM           IN VARCHAR2,
                                         P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                         P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                         P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                         ---
                                         P_FMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                                         P_TMRNO               IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE,
                                         P_FDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                                         P_TDEPARTMENT_ID      IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE,
                                         P_FGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                                         P_TGRADE_ID           IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE,
                                         P_PTG_ID              IN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE,
                                         P_DC_ID               IN DEFINITIONS.DESIGNATION_CATEGORY.DESIGNATION_CATEGORY_ID%TYPE,
                                         P_EMP_LOCATION_ID     IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                                         P_PAYROLL_LOCATION_ID IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE,
                                         P_EMP_TYPE            IN PAYROLL.DEF_EMP_FINANCIAL.EMP_TYPE%TYPE,
                                         P_ALERT_TEXT          OUT VARCHAR2,
                                         P_STOP                OUT CHAR);
  --------------------------------------------------------
  -- This Procedure will clear all the prorcess members --
  --------------------------------------------------------
  PROCEDURE PROC_DELETE_ALL_MEMBERS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                    P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                    P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  -------------------------------------------
  -- This Procedure will toggle select all --
  -------------------------------------------
  PROCEDURE TOGGLE_SELECT_ALL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                              P_SELECT_ALL        IN VARCHAR2,
                              P_IS_ADMIN          IN VARCHAR2,
                              P_FILTER            IN VARCHAR2,
                              P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  -------------------------------------------------------------------------------------
  -- This procedure will validate if process master information can be alterd or not --
  -------------------------------------------------------------------------------------
  PROCEDURE CHECK_CHANGE_ALLOWED(P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                 P_ALERT_TEXT OUT VARCHAR2,
                                 P_STOP       OUT CHAR);
  ----------------------------------------------------------------
  -- Following function will calculate Proposed temp basic amount --
  ----------------------------------------------------------------
  FUNCTION GET_PROPOSED_BASIC(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_PROCESS_ID      IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE,
                              P_MRNO            IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE)
    RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE;
  ---------------------------------------------------------------------------------
  -- Following function will calculate Proposed temp basic + personal pay amount --
  ---------------------------------------------------------------------------------
  FUNCTION GET_PROPOSED_BASIC_PERSONAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                       P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_PROCESS_ID      IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE,
                                       P_MRNO            IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE)
    RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE;
  ----------------------------------------------------------------
  -- Following function will calculate posted temp gross amount --
  ----------------------------------------------------------------
  FUNCTION GET_PROPOSED_GROSS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_PROCESS_ID      IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE,
                              P_MRNO            IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE)
    RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE;
  ---------------------------------------------------------------------
  -- Following procedure will execute and propose the salary changes --
  ---------------------------------------------------------------------
  PROCEDURE RUN_PROCESS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                        P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                        P_CALCULATE_ALL     IN BOOLEAN,
                        P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                        P_USER_MRNO         IN VARCHAR2,
                        P_TERMINAL          IN VARCHAR2,
                        P_ALERT_TEXT        OUT VARCHAR2,
                        P_STOP              OUT CHAR);
  ------------------------------------------------------------------
  -- Following procedure will execute and perform salry increment --
  ------------------------------------------------------------------
  PROCEDURE POST_MEMBERS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                         P_USER_MRNO         IN VARCHAR2,
                         P_TERMINAL          IN VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT CHAR);
  ----------------------------------------------------------------------
  -- Following procedure will execute and uppost the salary increment --
  ----------------------------------------------------------------------
  PROCEDURE UNPOST_MEMBERS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);
  ------------------------------------------
  -- This Procedure will finalize the Process --
  ------------------------------------------
  PROCEDURE FINALIZE_PROCESS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                             P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                             P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  ------------------------------------------
  -- This Procedure will finalize the Process --
  ------------------------------------------
  PROCEDURE UNFINALIZE_PROCESS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ---------------------------------
  -- ADD ARREARS OF POSTED CHAGE --
  ---------------------------------
  PROCEDURE POST_INCREMENT_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                   P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                   P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                   P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT VARCHAR2);
  ------------------------------------
  -- REMOVE ARREARS OF POSTED CHAGE --
  ------------------------------------
  PROCEDURE UNPOST_INCREMENT_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_PROCESS_ID        IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE,
                                     P_MRNO              IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
  ------------------------------------
  -- CHECK IF MANUAL ENTRIES EXISTS --
  ------------------------------------
  FUNCTION CHECK_MANUAL_ENTRIES(P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE)
    RETURN BOOLEAN;
END PKG_S16FRM00085;
```

#### PAYROLL.PKG_S16FRM00087
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00087 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL LOAN PAYMENT
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        25-Jan-2019   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    LOAN_NO         PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    REFERENCE_NO    FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    PARTY_NAME      FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    PARTY_SUB_CODE  FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    MRNO            FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    LOCATION_ID     FINANCE.GL_TRAN_MASTER.LOCATION_ID%TYPE,
    DR_CR_GENERAL   FINANCE.GL_VOUCHER_TYPE.DR_CR_GENERAL%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT       IN OUT REF_GL_TRAN_MASTER,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                 P_MODULE       IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                 P_MODULE       IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE);

END PKG_S16FRM00087;
```

#### PAYROLL.PKG_S16FRM00089
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00089 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL LOAN PAYMENT
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        11-Jul-2019   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_PAYMENT_MASTER IS RECORD(
    LOAN_NO                     PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    ND_EMPLOYEE_NAME            REGISTRATION.PATIENT.NAME%TYPE,
    ND_LOAN_TYPE_DESC           PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    ND_CURRENCY_DESC            DEFINITIONS.CURRENCY.DESCRIPTION%TYPE,
    LOAN_LOCATION_DESC          DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    TRANS_TYPE                  PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_TYPE%TYPE,
    TRANS_DATE                  PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE,
    MRNO                        REGISTRATION.PATIENT.MRNO%TYPE,
    LOAN_CODE                   PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_CODE%TYPE,
    OPEN_ACTUAL_DATE            PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_DATE%TYPE,
    OPEN_ACTUAL_LOAN            PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_LOAN%TYPE,
    OPEN_ACTUAL_INSTALLMENTS    PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_INSTALLMENTS%TYPE,
    OPEN_ACTUAL_MONTHLY         PAYROLL.LOAN_PAYMENT_MASTER_N.OPEN_ACTUAL_MONTHLY%TYPE,
    TEMP_LOAN_AMOUNT            PAYROLL.LOAN_PAYMENT_MASTER_N.TEMP_LOAN_AMOUNT%TYPE,
    LOAN_AMOUNT                 PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    INTEREST_AMOUNT             PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_AMOUNT%TYPE,
    NO_OF_INSTALLMENTS          PAYROLL.LOAN_PAYMENT_MASTER_N.NO_OF_INSTALLMENTS%TYPE,
    LOAN_INSTALLMENT            PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_INSTALLMENT%TYPE,
    INTEREST_INSTALLMENT        PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_INSTALLMENT%TYPE,
    REFUND_AMOUNT               PAYROLL.LOAN_PAYMENT_MASTER_N.REFUND_AMOUNT%TYPE,
    PAID_INTEREST               PAYROLL.LOAN_PAYMENT_MASTER_N.PAID_INTEREST%TYPE,
    VOUCHER_TYPE                FINANCE.GL_VOUCHER_TYPE.VOUCHER_TYPE%TYPE,
    VOUCHER_NO                  FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    STOP_AUTO_DEDUCTION         PAYROLL.LOAN_PAYMENT_MASTER_N.STOP_AUTO_DEDUCTION%TYPE,
    REMARKS                     PAYROLL.LOAN_PAYMENT_MASTER_N.REMARKS%TYPE,
    CANCEL_VOUCHER_TYPE         PAYROLL.LOAN_PAYMENT_MASTER_N.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCEL_VOUCHER_NO           PAYROLL.LOAN_PAYMENT_MASTER_N.CANCELLED_VOUCHER_NO%TYPE,
    STOP_AUTO_DEDUCTION_TILL    PAYROLL.LOAN_PAYMENT_MASTER_N.STOP_AUTO_DEDUCTION_TILL%TYPE,
    BASE_AMOUNT                 PAYROLL.LOAN_PAYMENT_MASTER_N.TEMP_LOAN_AMOUNT%TYPE,
    BASE_CURRENCY_ID            PAYROLL.LOAN_PAYMENT_MASTER_N.BASE_CURRENCY_ID%TYPE,
    BASE_CURRENCY_EXCHANGE_RATE PAYROLL.LOAN_PAYMENT_MASTER_N.BASE_CURRENCY_EXCHANGE_RATE%TYPE,
    LOAN_LOCATION_ID            DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    VOUCHER_STATUS              FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE                      PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE,
    STATUS_ID                   ORDERENTRY.ORDER_STATUS.ORDER_STATUS_ID%TYPE,
    STATUS_DESC                 ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_PAYMENT_MASTER IS REF CURSOR RETURN REC_LOAN_PAYMENT_MASTER;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_PAYMENT_MASTER IS TABLE OF REC_LOAN_PAYMENT_MASTER INDEX BY BINARY_INTEGER;
  -----------------------------------------------------------
  -- This procedure will QUERY PAYROLL.LOAN_PAYMENT_MASTER --
  -----------------------------------------------------------
  PROCEDURE QUERY_LOAN_PAYMENT_MASTER(P_RESULT  IN OUT REF_LOAN_PAYMENT_MASTER,
                                      P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
                                      P_MRNO    IN REGISTRATION.PATIENT.MRNO%TYPE);
  ------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE INSERT_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ------------------------------------------------------------
  -- This procedure will update PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.LOAN_PAYMENT_MASTER --
  ------------------------------------------------------------
  PROCEDURE DELETE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);
  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_PAYMENT_MASTER --
  ----------------------------------------------------------
  PROCEDURE LOCK_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_OPENING IS RECORD(
    LOAN_NO       PAYROLL.LOAN_REFUND_OPENING.LOAN_NO%TYPE,
    SR_NO         PAYROLL.LOAN_REFUND_OPENING.SR_NO%TYPE,
    REFUND_DATE   PAYROLL.LOAN_REFUND_OPENING.REFUND_DATE%TYPE,
    REFUND_TYPE   PAYROLL.LOAN_REFUND_OPENING.REFUND_TYPE%TYPE,
    REFUND_AMOUNT PAYROLL.LOAN_REFUND_OPENING.REFUND_AMOUNT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_OPENING IS REF CURSOR RETURN REC_LOAN_REFUND_OPENING;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_OPENING IS TABLE OF REC_LOAN_REFUND_OPENING INDEX BY BINARY_INTEGER;
  -----------------------------------------------------------
  -- This procedure will QUERY PAYROLL.LOAN_REFUND_OPENING --
  -----------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_OPENING(P_RESULT  IN OUT REF_LOAN_REFUND_OPENING,
                                      P_LOAN_NO IN PAYROLL.LOAN_REFUND_OPENING.LOAN_NO%TYPE);
  ------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.LOAN_REFUND_OPENING --
  ------------------------------------------------------------
  PROCEDURE INSERT_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING);
  ------------------------------------------------------------
  -- This procedure will update PAYROLL.LOAN_REFUND_OPENING --
  ------------------------------------------------------------
  PROCEDURE UPDATE_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING);
  ------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.LOAN_REFUND_OPENING --
  ------------------------------------------------------------
  PROCEDURE DELETE_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING);
  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_REFUND_OPENING --
  ----------------------------------------------------------
  PROCEDURE LOCK_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING);

  -------------------------------------------------------
  -- This Procedure will post the loan payment opening --
  -------------------------------------------------------
  PROCEDURE POST_LOAN_PAYMENT_OPENING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                      P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_LOAN_NO           IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                                      P_LOGIN_LOCATION_ID IN VARCHAR2,
                                      P_USER_MRNO         IN VARCHAR2,
                                      P_TERMINAL          IN VARCHAR2,
                                      P_OBJECT_CODE       IN VARCHAR2,
                                      P_ALERT_TEXT        OUT VARCHAR2,
                                      P_STOP              OUT CHAR);
  -------------------------------------------------------
  -- This Procedure will unpost the loan payment opening --
  -------------------------------------------------------
  PROCEDURE UNPOST_LOAN_PAYMENT_OPENING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_LOAN_NO           IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE,
                                        P_LOGIN_LOCATION_ID IN VARCHAR2,
                                        P_USER_MRNO         IN VARCHAR2,
                                        P_TERMINAL          IN VARCHAR2,
                                        P_OBJECT_CODE       IN VARCHAR2,
                                        P_ALERT_TEXT        OUT VARCHAR2,
                                        P_STOP              OUT CHAR);

END PKG_S16FRM00089;
```

#### PAYROLL.PKG_S16FRM00090
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00090 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for LOAN PAYMENT DETAIL
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        19-JUL-2019   M. ALI KHUBAIB         1. Created this Package.
         1.0        14-OCT-2019   M. ALI KHUBAIB         1. Modifications.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE LOAN_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15),
    PAY_START_DATE    DATE,
    PAY_END_DATE      DATE,
    LOAN_CODE         PAYROLL.DEF_LOAN_TYPE_CONSTANT.LOAN_CODE%TYPE,
    LOAN_DESC         PAYROLL.DEF_LOAN_TYPE_CONSTANT.DESCRIPTION%TYPE,
    MODULE            PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE LOAN_REF IS REF CURSOR RETURN LOAN_REC;

  -----------------------------------------------------
  -- This procedure will query PAYROLL.LOAN_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_LOANS(P_RESULT         IN OUT LOAN_REF,
                        P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                        P_PAY_END_DATE   IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                        P_MONTH          IN VARCHAR2,
                        P_LOAN_CODE      IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.LOAN_CODE%TYPE,
                        P_PENDING_ALL    IN CHAR);

  ------------------
  -- Record Group --
  ------------------
  TYPE LOAN_DETAIL_REC IS RECORD(
    MRNO                    REGISTRATION.PATIENT.MRNO%TYPE,
    NAME                    REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION             DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT              DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE                   DEFINITIONS.GRADES.GRADE_ID%TYPE,
    LOCATION_ID             DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC           DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_START_DATE          PAYROLL.LOAN_INSTALLMENT_DETAIL.PAY_START_DATE%TYPE,
    PAY_END_DATE            PAYROLL.LOAN_INSTALLMENT_DETAIL.PAY_END_DATE%TYPE,
    LOAN_NO                 PAYROLL.LOAN_INSTALLMENT_DETAIL.LOAN_NO%TYPE,
    TRANS_DATE              PAYROLL.LOAN_INSTALLMENT_DETAIL.TRANS_DATE%TYPE,
    LOAN_CODE               PAYROLL.LOAN_INSTALLMENT_DETAIL.LOAN_CODE%TYPE,
    REFUND_WITH_PAY_VOUCHER PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_WITH_PAY_VOUCHER%TYPE,
    REFUND_AD_CODE          PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_AD_CODE%TYPE,
    PRINCIPAL_AMOUNT        PAYROLL.LOAN_INSTALLMENT_DETAIL.PRINCIPAL_AMOUNT%TYPE,
    LOAN_INSTALLMENT        PAYROLL.LOAN_INSTALLMENT_DETAIL.LOAN_INSTALLMENT%TYPE,
    INTEREST_INSTALLMENT    PAYROLL.LOAN_INSTALLMENT_DETAIL.INTEREST_INSTALLMENT%TYPE,
    ACTUAL_INSTALLMENT      PAYROLL.LOAN_INSTALLMENT_DETAIL.ACTUAL_INSTALLMENT%TYPE,
    TEMP_REFUND_AMOUNT      PAYROLL.LOAN_INSTALLMENT_DETAIL.TEMP_REFUND_AMOUNT%TYPE,
    REFUND_AMOUNT           PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_AMOUNT%TYPE,
    REFUND_NO               PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_NO%TYPE,
    SALARY_DEDUCTION_TYPE   PAYROLL.LOAN_INSTALLMENT_DETAIL.SALARY_DEDUCTION_TYPE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE LOAN_DETAIL_REF IS REF CURSOR RETURN LOAN_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE LOAN_DETAIL_TAB IS TABLE OF LOAN_DETAIL_REC INDEX BY BINARY_INTEGER;

  ---------------------------------------------------------------
  -- This procedure will query PAYROLL.LOAN_INSTALLMENT_DETAIL --
  ---------------------------------------------------------------
  PROCEDURE QUERY_LOAN_INS_DETAIL(P_RESULT      IN OUT LOAN_DETAIL_REF,
                                  P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_START_DATE  IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                                  P_END_DATE    IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                                  P_LOAN_CODE   IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.LOAN_CODE%TYPE,
                                  P_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_REFUND_NO   IN PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_NO%TYPE,
                                  P_PENDING_ALL IN CHAR,
                                  P_ORDER_BY    IN VARCHAR2);

  ----------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.LOAN_INSTALLMENT_DETAIL --
  ----------------------------------------------------------------
  PROCEDURE DELETE_LOAN_INS_DETAIL(P_RESULT IN OUT LOAN_DETAIL_TAB);

  --------------------------------------------------------------
  -- This procedure will lock PAYROLL.LOAN_INSTALLMENT_DETAIL --
  --------------------------------------------------------------
  PROCEDURE LOCK_LOAN_INS_DETAIL(P_RESULT IN OUT LOAN_DETAIL_TAB);

  ---------------------------------------------------------------------
  -- This procedure will used to populate current month installments --
  ---------------------------------------------------------------------
  PROCEDURE POPULATE_CURRENT_INSTALLMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                          P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                          P_USER_MRNO       IN REGISTRATION.PATIENT.MRNO%TYPE,
                                          P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                          P_TERMINAL        IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                          P_ALERT_TEXT      OUT VARCHAR2,
                                          P_STOP            OUT CHAR);

END;
```

#### PAYROLL.PKG_S16FRM00093
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00093 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        09-OCT-2017   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_TRAN_MASTER IS RECORD(
    YEAR_CODE          FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
    PAY_VOUCHER_TYPE   PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
    ORGANIZATION_ID    DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    SERIAL_NO          PAYROLL.PAY_VOUCHER.SERIAL_NO%TYPE,
    YEAR_DESC          PAYROLL.PAY_FINANCIAL_YEAR.YEAR_DESCRIPTION%TYPE,
    LOCATION_DESC      DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_VOUCHER_TYPE_D PAYROLL.DEF_PAY_VOUCHER_TYPE.DESCRIPTION%TYPE,
    PROFIT_RATIO       FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE,
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC    DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS      DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS            FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS     FINANCE.PF_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID          FINANCE.PF_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE       FINANCE.PF_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY         FINANCE.PF_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE        FINANCE.PF_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY          FINANCE.PF_TRAN_MASTER.POSTED_BY%TYPE,
    LOAN_CODE          PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
    LOAN_DESCRIPTION   PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    ENTRY_TYPE         FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_TRAN_MASTER IS REF CURSOR RETURN REC_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_TRAN_MASTER IS TABLE OF REC_TRAN_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will query FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_TRAN_MASTER(P_RESULT           IN OUT REF_TRAN_MASTER,
                              P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE,
                              P_LOCATION_ID      IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                              P_YEAR_CODE        IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                              P_VOUCHER_TYPE     IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO       IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                              P_ENTRY_TYPE       IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE,
                              P_LOAN_CODE        IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE);
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER);
  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.PF_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.PF_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.PF_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.PF_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.PF_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.PF_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_TRAN_DETAIL IS REF CURSOR RETURN REC_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE PF_TRAN_DETAIL_TAB IS TABLE OF REC_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_TRAN_DETAIL(P_RESULT       IN OUT REF_TRAN_DETAIL,
                              P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                              P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
END PKG_S16FRM00093;
```

#### PAYROLL.PKG_S16FRM00094
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00094 IS

  /*******************************************************************************************************
         OBJECTIVE :=   This package is used to encapsulate procedure/function(s) of CT Worksheet
         -------------------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        12-NOV-2019  Farhan Akram            1. Created this Package.
  ************************************************************************************************/
  -------------------------------------------------------------------
  -- This Function is used to return the Version of this Package --
  -------------------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------
  -- Record Group --
  ------------------
  TYPE COA_INQ_QUERY_REC IS RECORD(
    COA_CODE             FINANCE.GL_COA_INQUIRY.COA_CODE%TYPE,
    LEDGER_TYPE_CODE     FINANCE.GL_COA_INQUIRY.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE   FINANCE.GL_COA_INQUIRY.SUB_LDGR_ITEM_CODE%TYPE,
    TRANS_DATE           FINANCE.GL_COA_INQUIRY.TRANS_DATE%TYPE,
    VOUCHER_TYPE         FINANCE.GL_COA_INQUIRY.VOUCHER_TYPE%TYPE,
    VOUCHER_NO           FINANCE.GL_COA_INQUIRY.VOUCHER_NO%TYPE,
    SERIAL_NO            FINANCE.GL_COA_INQUIRY.SERIAL_NO%TYPE,
    REFERENCE_NO         FINANCE.GL_COA_INQUIRY.REFERENCE_NO%TYPE,
    NARRATION            FINANCE.GL_COA_INQUIRY.NARRATION%TYPE,
    DR_AMOUNT            FINANCE.GL_COA_INQUIRY.DR_AMOUNT%TYPE,
    CR_AMOUNT            FINANCE.GL_COA_INQUIRY.CR_AMOUNT%TYPE,
    BALANCE              FINANCE.GL_COA_INQUIRY.BALANCE%TYPE,
    COA_DESCRIPTION      FINANCE.GL_COA_INQUIRY.COA_DESCRIPTION%TYPE,
    SUB_LEDGER_ITEM_DESC FINANCE.GL_COA_INQUIRY.SUB_LEDGER_ITEM_DESC%TYPE,
    USER_ID              FINANCE.GL_COA_INQUIRY.USER_ID%TYPE,
    TERMINAL             FINANCE.GL_COA_INQUIRY.TERMINAL%TYPE);

  TYPE COA_INQ_QUERY_REF IS REF CURSOR RETURN COA_INQ_QUERY_REC;

  PROCEDURE COA_INQ_QUERY(P_RESULT IN OUT COA_INQ_QUERY_REF);

  FUNCTION GET_REPORTING_PERIOD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN FINANCE.GL_COMPANY.REPORTING_PERIOD%TYPE;
  PROCEDURE FETCH_YEARLY_BALANCE(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_YEAR_CODE          IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                 P_FROM_DATE          IN FINANCE.PF_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                 P_TO_DATE            IN FINANCE.PF_FINANCIAL_YEAR.TO_DATE%TYPE,
                                 P_COA_CODE           IN FINANCE.GL_COA_INQUIRY.COA_CODE%TYPE,
                                 P_LEDGER_TYPE_CODE   IN FINANCE.GL_COA_INQUIRY.LEDGER_TYPE_CODE%TYPE,
                                 P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_COA_INQUIRY.SUB_LDGR_ITEM_CODE%TYPE,
                                 P_OPENING_BALANCE    OUT FINANCE.GL_OPENING_BALANCES.OPEN_DR%TYPE,
                                 P_ALERT_TEXT         OUT VARCHAR2,
                                 P_STOP               OUT CHAR);
  PROCEDURE POPULATE_TRANSACTIONS(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_YEAR_CODE          IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                  P_FROM_DATE          IN FINANCE.PF_FINANCIAL_YEAR.FROM_DATE%TYPE,
                                  P_TO_DATE            IN FINANCE.PF_FINANCIAL_YEAR.TO_DATE%TYPE,
                                  P_COA_CODE           IN FINANCE.GL_COA_INQUIRY.COA_CODE%TYPE,
                                  P_LEDGER_TYPE_CODE   IN FINANCE.GL_COA_INQUIRY.LEDGER_TYPE_CODE%TYPE,
                                  P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_COA_INQUIRY.SUB_LDGR_ITEM_CODE%TYPE,
                                  P_VOUCHER_TYPE       IN FINANCE.PF_TRAN_DETAIL.VOUCHER_TYPE%TYPE,
                                  P_NARRATION          IN FINANCE.PF_TRAN_DETAIL.NARRATION%TYPE,
                                  P_REFERENCE_NO       IN FINANCE.PF_TRAN_DETAIL.REFERENCE_NO%TYPE,
                                  P_MIN_AMOUNT         IN FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
                                  P_MAX_AMOUNT         IN FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
                                  P_USER_MRNO          IN VARCHAR2,
                                  P_USER_ID            IN VARCHAR2,
                                  P_TERMINAL           IN VARCHAR2,
                                  P_OBJECT_CODE        IN VARCHAR2,
                                  P_OPENING_BALANCE    OUT FINANCE.GL_OPENING_BALANCES.OPEN_DR%TYPE,
                                  P_RUNNING_BALANCE    OUT FINANCE.GL_OPENING_BALANCES.OPEN_DR%TYPE,
                                  P_CLOSING_BALANCE    OUT FINANCE.GL_OPENING_BALANCES.OPEN_DR%TYPE,
                                  P_ALERT_TEXT         OUT VARCHAR2,
                                  P_STOP               OUT CHAR);
END PKG_S16FRM00094;
```

#### PAYROLL.PKG_S16FRM00095
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00095 IS

  /*******************************************************************************************************
         OBJECTIVE :=   This package is used to view employee salary detail
         -------------------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        30-MAR-2020   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/
  -------------------------------------------------------------------
  -- This Function is used to return the Version of this Package --
  -------------------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMPLOYEE_INFO IS RECORD(
    EMPLOYEE_CODE REGISTRATION.PATIENT.MRNO%TYPE,
    NAME          REGISTRATION.PATIENT.NAME%TYPE,
    AGE           VARCHAR2(100),
    DESIGNATION   DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE         DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    EMPLOYEE_TYPE HRD.EMPLOYEE_TYPE.DESCRIPTION%TYPE,
    JOINING_DATE  DATE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_EMPLOYEE_INFO IS REF CURSOR RETURN REC_EMPLOYEE_INFO;

  ----------------------------------------------------
  -- This procedure will query employee information --
  ----------------------------------------------------
  PROCEDURE QUERY_EMPLOYEE(P_RESULT        IN OUT REF_EMPLOYEE_INFO,
                           P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_ORIGINAL_TEST IN CHAR);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_MONTHS IS RECORD(
    EMPLOYEE_CODE     REGISTRATION.PATIENT.MRNO%TYPE,
    MONTH             VARCHAR2(100),
    MONTH_START_DATE  DATE,
    MONTH_END_DATE    DATE,
    SALARY_START_DATE DATE,
    SALARY_END_DATE   DATE,
    MONTH_DAYS        PAYROLL.PAY_MASTER.MONTH_DAYS%TYPE,
    SALARY_DAYS       PAYROLL.PAY_MASTER.SALARY_DAYS%TYPE,
    ----------------
    GROSS_PAY_RATE       PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    OTHER_ALLOWANCE      PAYROLL.PAY_MASTER.OTHER_ALLOWANCES%TYPE,
    NIGH_OVERTIME        PAYROLL.PAY_MASTER.NIGHTS_AMOUNT%TYPE,
    ARREARS              PAYROLL.PAY_MASTER.ARREARS%TYPE,
    GROSS_PAYABLES       PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE,
    DEDUCTIONS           NUMBER(20, 2), --PAYROLL.PAY_MASTER%TYPE,
    NET_PAY              PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE,
    PRACTICE_INCOME      PAYROLL.PAY_MASTER.PRACTICE_INCOME%TYPE,
    REIMBERSMENTS        PAYROLL.PAY_MASTER.REIMBURSEMENT%TYPE,
    CURRENT_MONTH_UNPAID NUMBER(20, 2), --PAYROLL.PAY_MASTER%TYPE,
    PRV_MONTH_UNPAID     PAYROLL.PAY_MASTER.PREV_UNPAID_LEAVES%TYPE,
    SALARY_ON_CARD_SWIPE PAYROLL.PAY_MASTER.SALARY_ON_CARD_SWIPE%TYPE,
    CURRENCY_RATE        PAYROLL.PAY_MASTER.CURRENCY_EXCHANGE_RATE%TYPE,
    PAYROLL_LOCATION     DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    EMPLOYEE_LOCATION    DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_MONTHS IS REF CURSOR RETURN REC_MONTHS;

  ------------------------------------------------------
  -- This procedure will query employee salary months --
  ------------------------------------------------------
  PROCEDURE QUERY_MONTHS(P_RESULT        IN OUT REF_MONTHS,
                         P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE,
                         P_MONTH         IN VARCHAR2,
                         P_ORIGINAL_TEST IN CHAR);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_ALL_DED IS RECORD(
    EMPLOYEE_CODE           REGISTRATION.PATIENT.MRNO%TYPE,
    SALARY_START_DATE       DATE,
    SALARY_END_DATE         DATE,
    AD_CODE                 PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
    DESCRIPTION             PAYROLL.DEF_AD_CHART.DESCRIPTION%TYPE,
    ACTUAL_AMOUNT           PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    PAYMENT_PAID            PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    OTHER_AMOUNTS_PAID      PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE, ---(PI/REIMBURSMENT)
    DEDUCTION_PAID          PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    PAYMENT_ON_CARD_SWIPE   PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE,
    DEDUCTION_ON_CARD_SWIPE PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_ALL_DED IS REF CURSOR RETURN REC_ALL_DED;

  ------------------------------------------------------------------
  -- This procedure will query employee allowances and deductions --
  ------------------------------------------------------------------
  PROCEDURE QUERY_ALL_DED(P_RESULT         IN OUT REF_ALL_DED,
                          P_EMPLOYEE_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_PAY_START_DATE IN DATE,
                          P_PAY_END_DATE   IN DATE,
                          P_ORIGINAL_TEST  IN CHAR);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_DAY_WISE_CAL IS RECORD(
    EMPLOYEE_CODE        REGISTRATION.PATIENT.MRNO%TYPE,
    SALARY_START_DATE    DATE,
    SALARY_END_DATE      DATE,
    AD_CODE              PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
    DAY                  PAYROLL.PAY_DAILY_AD_TEST.DAY%TYPE,
    LEAVE_TYPE_ID        PAYROLL.PAY_DAILY_AD_TEST.LEAVE_TYPE_ID%TYPE,
    LEAVE_TYPE           HRD.LEAVE_TYPE.DESCRIPTION%TYPE,
    PAYMENT_FACTOR       PAYROLL.PAY_DAILY_AD_TEST.PAYMENT_FACTOR%TYPE,
    ACTUAL_MINUTES       PAYROLL.PAY_DAILY_AD_TEST.ACTUAL_WORKING_TIME%TYPE,
    PERFORMED_MINUTES    PAYROLL.PAY_DAILY_AD_TEST.ACTUAL_PERFORM_TIME%TYPE,
    ACTUAL_DAY           NUMBER(6),
    SAL_CALCULATED_DAY   NUMBER(6),
    SALARY_ON_CARD_SWIPE PAYROLL.PAY_DAILY_AD_TEST.CALC_SALARY_ON_CARD_SWIPE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_DAY_WISE_CAL IS REF CURSOR RETURN REC_DAY_WISE_CAL;

  ------------------------------------------------------------------
  -- This procedure will query employee allowances and deductions --
  ------------------------------------------------------------------
  PROCEDURE QUERY_DAY_WISE_CAL(P_RESULT         IN OUT REF_DAY_WISE_CAL,
                               P_EMPLOYEE_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_PAY_START_DATE IN DATE,
                               P_PAY_END_DATE   IN DATE,
                               P_AD_CODE        IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
                               P_ORIGINAL_TEST  IN CHAR);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PREV_UNPAID_LEAVE IS RECORD(
    EMPLOYEE_CODE     REGISTRATION.PATIENT.MRNO%TYPE,
    SALARY_START_DATE DATE,
    SALARY_END_DATE   DATE,
    DAY               PAYROLL.PAY_DAILY_AD_TEST.DAY%TYPE,
    LEAVE_TYPE_ID     PAYROLL.PAY_DAILY_AD_TEST.LEAVE_TYPE_ID%TYPE,
    LEAVE_TYPE        HRD.LEAVE_TYPE.DESCRIPTION%TYPE,
    TOTAL_AMOUNT      PAYROLL.PAY_DAILY_AD_TEST.ACTUAL_SALARY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PREV_UNPAID_LEAVE IS REF CURSOR RETURN REC_PREV_UNPAID_LEAVE;

  -----------------------------------------------------
  -- This procedure will query previour unpaid leave --
  -----------------------------------------------------
  PROCEDURE QUERY_PREV_UNPAID_LEAVE(P_RESULT         IN OUT REF_PREV_UNPAID_LEAVE,
                                    P_EMPLOYEE_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_PAY_START_DATE IN DATE,
                                    P_PAY_END_DATE   IN DATE,
                                    P_AD_CODE        IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
                                    P_ORIGINAL_TEST  IN CHAR);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PREV_UNPAID_AD IS RECORD(
    EMPLOYEE_CODE     REGISTRATION.PATIENT.MRNO%TYPE,
    SALARY_START_DATE DATE,
    SALARY_END_DATE   DATE,
    AD_CODE           PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
    DAY               PAYROLL.PAY_DAILY_TEMP_UNPAID.DAY%TYPE,
    DESCRIPTION       PAYROLL.DEF_AD_CHART.DESCRIPTION%TYPE,
    AMOUNT            PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PREV_UNPAID_AD IS REF CURSOR RETURN REC_PREV_UNPAID_AD;

  -------------------------------------------------------------------------
  -- This procedure will query previour unpaid allowances and deductions --
  -------------------------------------------------------------------------
  PROCEDURE QUERY_PREV_UNPAID_AD(P_RESULT         IN OUT REF_PREV_UNPAID_AD,
                                 P_EMPLOYEE_CODE  IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_PAY_START_DATE IN DATE,
                                 P_PAY_END_DATE   IN DATE,
                                 P_AD_CODE        IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE,
                                 P_DAY            IN DATE,
                                 P_ORIGINAL_TEST  IN CHAR);

END PKG_S16FRM00095;
```

#### PAYROLL.PKG_S16FRM00097
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00097 IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for expense claim pending queue
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        16-JUN-2020   M. Ali Khubaib         1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ---------------------------------------------------
  -- Record Type declaration for Master Table Data --
  ---------------------------------------------------
  TYPE EXP_CLAIM_Q_REC IS RECORD(
    CLAIM_NO        PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
    EXPENSE_CODE    PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE,
    EXPENSE_TYPE    DEFINITIONS.EXPENSE.DESCRIPTION%TYPE,
    MRNO            PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE,
    EMPLOYEE_NAME   REGISTRATION.PATIENT.NAME%TYPE,
    EMPLOYEE_DESIG  DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    EMPLOYEE_DEPT   DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    EMPLOYEE_GRADE  DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    ENTERED_BY      REGISTRATION.PATIENT.MRNO%TYPE,
    ENTERED_BY_NAME REGISTRATION.PATIENT.NAME%TYPE,
    NO_OF_DOCS      NUMBER(2),
    EVENT_DESC      DEFINITIONS.EVENT.DESCRIPTION%TYPE);

  -- Ref Cursor --
  TYPE EXP_CLAIM_Q_REF IS REF CURSOR RETURN EXP_CLAIM_Q_REC;
  -- Associative Array --
  TYPE EXP_CLAIM_Q_TAB IS TABLE OF EXP_CLAIM_Q_REC INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------------
  -- This procedure will be used to query data from Expense Claim Master Table --
  -------------------------------------------------------------------------------
  PROCEDURE QUERY_EXP_CLAIM_Q(P_RESULT    IN OUT EXP_CLAIM_Q_REF,
                              P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_CLAIM_NO  IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE,
                              P_MRNO      IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE);

  ------------------------------------------------------
  -- This Procedure will show the EXPENSE CLAIM QUEUE --
  ------------------------------------------------------
  PROCEDURE EXPENSE_CLAIM_QUEUE(P_MRNO          IN VARCHAR2,
                                P_ACTING_FOR    IN VARCHAR2,
                                P_OBJECT_CODE   IN VARCHAR2,
                                P_PROCESS_ID    IN VARCHAR2,
                                P_TERMINAL      IN VARCHAR2,
                                P_EVENT         IN VARCHAR2,
                                P_ASSIGNMENT_ID IN NUMBER);
END PKG_S16FRM00097;
```

#### PAYROLL.PKG_S16FRM00099
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00099 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PF Final Settlement
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        30-SEP-2020   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMP IS RECORD(
    EMPLOYEE_CODE          REGISTRATION.PATIENT.MRNO%TYPE,
    NAME                   REGISTRATION.PATIENT.NAME%TYPE,
    DEPARTMENT             DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DESIGNATION            DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    GRADE                  DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    SR_NO                  PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
    TRANS_DATE             PAYROLL.PF_FINAL_SETTLEMENT.TRANS_DATE%TYPE,
    TYPE                   PAYROLL.PF_FINAL_SETTLEMENT.TYPE%TYPE, -- FS -> FINAL SETTLEMENT, PW -> PERMANET WIDTHDRAW
    PF_TYPE                PAYROLL.PF_FINAL_SETTLEMENT.PF_TYPE%TYPE,
    RACK_RATE              PAYROLL.PF_FINAL_SETTLEMENT.RACK_RATE%TYPE,
    REMARKS                PAYROLL.PF_FINAL_SETTLEMENT.REMARKS%TYPE,
    VOUCHER_TYPE           PAYROLL.PF_FINAL_SETTLEMENT.VOUCHER_TYPE%TYPE,
    VOUCHER_NO             PAYROLL.PF_FINAL_SETTLEMENT.VOUCHER_NO%TYPE,
    CANCELLED_VOUCHER_TYPE PAYROLL.PF_FINAL_SETTLEMENT.CANCELLED_VOUCHER_TYPE%TYPE,
    CANCELLED_VOUCHER_NO   PAYROLL.PF_FINAL_SETTLEMENT.CANCELLED_VOUCHER_NO%TYPE,
    STATUS_ID              PAYROLL.PF_FINAL_SETTLEMENT.STATUS_ID%TYPE,
    STATUS_DESC            DEFINITIONS.ORDER_STATUS.DESCRIPTION%TYPE,
    GROSS_PAYABLE          PAYROLL.PF_FINAL_SETTLEMENT.GROSS_PAYABLE%TYPE,
    AGE                    VARCHAR2(30),
    NO_OF_MONTHS           PAYROLL.PF_FINAL_SETTLEMENT.NO_OF_MONTHS%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_EMP IS REF CURSOR RETURN REC_EMP;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_BAL IS TABLE OF PAYROLL.PKG_S16FRM00099.REC_BALANCE;
  TYPE TAB_EMP IS TABLE OF REC_EMP INDEX BY BINARY_INTEGER;

  ------------------------------------------------------
  -- This procedure will query FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_PF_FINAL_SETTLEMENT(P_RESULT   IN OUT REF_EMP,
                                      P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TYPE     IN PAYROLL.PF_FINAL_SETTLEMENT.TYPE%TYPE);

  ------------------------------------------------------------
  -- This procedure will INSERT PAYROLL.PF_FINAL_SETTLEMENT --
  ------------------------------------------------------------
  PROCEDURE INSERT_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP);
  ------------------------------------------------------------
  -- This procedure will update PAYROLL.PF_FINAL_SETTLEMENT --
  ------------------------------------------------------------
  PROCEDURE UPDATE_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP);
  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.PF_FINAL_SETTLEMENT --
  ----------------------------------------------------------
  PROCEDURE LOCK_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_BALANCE IS RECORD(
    MRNO        REGISTRATION.PATIENT.MRNO%TYPE,
    COA_CODE    FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
    DESCRIPTION FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    BALANCE     FINANCE.GL_OPENING_BALANCES.OPEN_CR%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_BALANCE IS REF CURSOR RETURN REC_BALANCE;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_BALANCE IS TABLE OF REC_BALANCE INDEX BY BINARY_INTEGER;
  ----------------------------------------
  -- This procedure will query Balances --
  ----------------------------------------
  PROCEDURE QUERY_BALANCE(P_RESULT          IN OUT REF_BALANCE,
                          P_SETTLEMENT_TYPE IN PAYROLL.DEF_PAY_VOUCHER_SETUP.PAY_VOUCHER_TYPE%TYPE,
                          P_RACK_RATE       IN PAYROLL.PF_FINAL_SETTLEMENT.RACK_RATE%TYPE,
                          P_MRNO            IN HRD.INFORMATION.MRNO%TYPE,
                          P_AMOUNT          IN PAYROLL.PF_FINAL_SETTLEMENT.GROSS_PAYABLE%TYPE,
                          P_MONTHS          IN PAYROLL.PF_FINAL_SETTLEMENT.NO_OF_MONTHS%TYPE);

  -- pipeline Function for query Balances --                          
  FUNCTION F_QUERY_BALANCE_APEX(P_SETTLEMENT_TYPE IN PAYROLL.DEF_PAY_VOUCHER_SETUP.PAY_VOUCHER_TYPE%TYPE,
                                P_RACK_RATE       IN PAYROLL.PF_FINAL_SETTLEMENT.RACK_RATE%TYPE,
                                P_MRNO            IN HRD.INFORMATION.MRNO%TYPE,
                                P_AMOUNT          IN PAYROLL.PF_FINAL_SETTLEMENT.GROSS_PAYABLE%TYPE,
                                P_MONTHS          IN PAYROLL.PF_FINAL_SETTLEMENT.NO_OF_MONTHS%TYPE)
    RETURN TAB_BAL
    PIPELINED;

  ------------------------------------------------------------------------------------------------------------------                                    
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_LOAN_REFUND_DETAIL IS RECORD(
    LOAN_NO            PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE,
    LOAN_DATE          PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE,
    LOAN_TYPE          PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    REFUND_LOCATION    DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    LOAN_AMOUNT        PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    REFUND_AMOUNT      PAYROLL.LOAN_REFUND_DETAIL_N.REFUND_AMOUNT%TYPE,
    LOAN_BALANCE       PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_AMOUNT%TYPE,
    INTEREST_AMOUNT    PAYROLL.LOAN_PAYMENT_MASTER_N.INTEREST_AMOUNT%TYPE,
    BALANCE            PAYROLL.LOAN_PAYMENT_MASTER_N.REFUND_AMOUNT%TYPE,
    TEMP_REFUND_AMOUNT PAYROLL.LOAN_REFUND_DETAIL_N.TEMP_REFUND_AMOUNT%TYPE,
    MRNO               REGISTRATION.PATIENT.MRNO%TYPE,
    REFUND_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    MODULE             PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOAN_REFUND_DETAIL IS REF CURSOR RETURN REC_LOAN_REFUND_DETAIL;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_LOAN_REFUND_DETAIL IS TABLE OF REC_LOAN_REFUND_DETAIL INDEX BY BINARY_INTEGER;
  ----------------------------------------------------------
  -- This procedure will query PAYROLL.LOAN_REFUND_MASTER_N --
  ----------------------------------------------------------
  PROCEDURE QUERY_LOAN_REFUND_DETAIL(P_RESULT       IN OUT REF_LOAN_REFUND_DETAIL,
                                     P_MRNO         IN HRD.INFORMATION.MRNO%TYPE,
                                     P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                     P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PF_TRAN_MASTER IS RECORD(
    PAY_VOUCHER_TYPE   PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
    PAY_VOUCHER_TYPE_D PAYROLL.DEF_PAY_VOUCHER_TYPE.DESCRIPTION%TYPE,
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC    DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS      DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS            FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS     FINANCE.PF_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID          FINANCE.PF_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE       FINANCE.PF_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY         FINANCE.PF_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE        FINANCE.PF_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY          FINANCE.PF_TRAN_MASTER.POSTED_BY%TYPE,
    REFERENCE_NO       FINANCE.PF_TRAN_MASTER.REFERENCE_NO%TYPE,
    PARTY_NAME         FINANCE.PF_TRAN_MASTER.PARTY_NAME%TYPE,
    DR_CR_GENERAL      FINANCE.GL_VOUCHER_TYPE.DR_CR_GENERAL%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PF_TRAN_MASTER IS REF CURSOR RETURN REC_PF_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PF_TRAN_MASTER IS TABLE OF REC_PF_TRAN_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will query FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE QUERY_PF_TRAN_MASTER(P_RESULT           IN OUT REF_PF_TRAN_MASTER,
                                 P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_TYPE     IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO       IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  -------------------------------------------------------
  -- This procedure will insert FINANCE.PF_TRAN_MASTER --
  -------------------------------------------------------
  PROCEDURE INSERT_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);

  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PF_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.PF_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.PF_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.PF_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.PF_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.PF_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.PF_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.PF_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.PF_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.PF_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PF_TRAN_DETAIL IS REF CURSOR RETURN REC_PF_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE PF_TRAN_DETAIL_TAB IS TABLE OF REC_PF_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_PF_TRAN_DETAIL_D(P_RESULT       IN OUT REF_PF_TRAN_DETAIL,
                                   P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  PROCEDURE QUERY_PF_TRAN_DETAIL_S(P_RESULT       IN OUT REF_PF_TRAN_DETAIL,
                                   P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.PF_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.PF_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB);

  ---------------------------
  -- Voucher detail Record --
  ---------------------------
  TYPE TRAN_DETAIL_REC IS RECORD(
    DEBIT_CREDIT       CHAR(1),
    LEDGER_TYPE_CODE   FINANCE.PF_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.PF_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.PF_TRAN_DETAIL.COA_CODE%TYPE,
    DR_AMOUNT          FINANCE.PF_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.PF_TRAN_DETAIL.CR_AMOUNT%TYPE,
    REMARKS            PAYROLL.PROFIT_VOUCHER_TMP.REMARKS%TYPE,
    COA_STATUS         FINANCE.Pf_Tran_Detail.COA_STATUS%TYPE);

  TYPE TRAN_DETAIL_TAB IS TABLE OF TRAN_DETAIL_REC;
  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE GET_VOUCHER_DETAIL(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PF_FINAL_SETTLEMENT IN PAYROLL.PF_FINAL_SETTLEMENT%ROWTYPE,
                               P_DR_CR_GENERAL       IN FINANCE.Gl_Voucher_Type.DR_CR_GENERAL%TYPE,
                               P_YEAR_CODE           IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                               P_COA_CODE            FINANCE.GL_VOUCHER_TYPE_DETAIL.COA_CODE%TYPE,
                               P_LEDGER_TYPE_CODE    FINANCE.GL_VOUCHER_TYPE_DETAIL.LEDGER_TYPE_CODE%TYPE,
                               P_SUB_LDGR_ITEM_CODE  FINANCE.GL_VOUCHER_TYPE_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                               P_USER_MRNO           IN VARCHAR2,
                               P_TERMINAL            IN VARCHAR2,
                               P_OBJECT_CODE         IN VARCHAR2,
                               P_RESULT              OUT SYS_REFCURSOR,
                               P_ALERT_TEXT          OUT VARCHAR2,
                               P_STOP                OUT CHAR);
  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE ADD_VOUCHER_REFERENCES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_SERIAL_NO         IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                                   P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_OLD_VOUCHER_NO    IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_NEW_VOUCHER_NO    IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO               IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_YEAR_CODE          IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                  P_SERIAL_NO          IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                                  P_VOUCHER_TYPE       IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO         IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE         IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID        IN FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE      IN FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS            IN FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
                                  P_COA_CODE           FINANCE.GL_VOUCHER_TYPE_DETAIL.COA_CODE%TYPE,
                                  P_LEDGER_TYPE_CODE   FINANCE.GL_VOUCHER_TYPE_DETAIL.LEDGER_TYPE_CODE%TYPE,
                                  P_SUB_LDGR_ITEM_CODE FINANCE.GL_VOUCHER_TYPE_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                                  P_PARTY_NAME         IN FINANCE.PF_TRAN_MASTER.PARTY_NAME%TYPE,
                                  P_REFERENCE_NO       IN FINANCE.PF_TRAN_MASTER.REFERENCE_NO%TYPE,
                                  P_LOGIN_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO          IN VARCHAR2,
                                  P_TERMINAL           IN VARCHAR2,
                                  P_OBJECT_CODE        IN VARCHAR2,
                                  P_NEW_VOUCHER_NO     OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT         OUT VARCHAR2,
                                  P_STOP               OUT CHAR);
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_YEAR_CODE         IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                                  P_SERIAL_NO         IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE        IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID       IN FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE     IN FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS           IN FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                         P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                         P_YEAR_CODE         IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                         P_SERIAL_NO         IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                         P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                         P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_USER_MRNO         IN VARCHAR2,
                         P_TERMINAL          IN VARCHAR2,
                         P_OBJECT_CODE       IN VARCHAR2,
                         P_NEW_VOUCHER_NO    OUT VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                P_MRNO              IN PAYROLL.PF_FINAL_SETTLEMENT.MRNO%TYPE,
                                P_SERIAL_NO         IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_LOGIN_LOCATION_ID IN VARCHAR2,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_SERIAL_NO         IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE,
                           P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                           P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                           P_LOGIN_LOCATION_ID IN VARCHAR2,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_NEW_VOUCHER_TYPE  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                           P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);
  ---------------------------------------------
  -- This function will return new serial no --
  ---------------------------------------------
  FUNCTION GET_SERIAL_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_MRNO            IN PAYROLL.PF_FINAL_SETTLEMENT.MRNO%TYPE)
    RETURN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE;

  -------------------------------------------------
  -- This function will return Current Year Code --
  -------------------------------------------------
  FUNCTION F_GET_CURRENT_YEAR RETURN NUMBER;
  FUNCTION GET_LAST_RACK_RATE
    RETURN PAYROLL.Pf_Final_Settlement.RACK_RATE%TYPE;
  FUNCTION GET_NO_OF_MONTHS
    RETURN PAYROLL.Pf_Final_Settlement.NO_OF_MONTHS%TYPE;
  -----------------------------------------------------------
  -- This function will get reference required or not     --
  -----------------------------------------------------------
  FUNCTION GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2)
    RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE;

  PROCEDURE R_PF_FINAL_SETTLEMENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  p_rack_rate         in varchar2,
                                  p_no_of_month       in varchar,
                                  p_emp_code          IN VARCHAR2,
                                  P_ZAKAT             IN VARCHAR2,
                                  P_PROFIT_MEMBER     IN VARCHAR2,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT VARCHAR2);
  TYPE REC_PF_SUMMARY IS RECORD(
    RACK_RATE          NUMBER,
    MONTHS             NUMBER,
    EMP_CON_DESC       VARCHAR2(4000),
    EMP_CON_OPN        VARCHAR2(4000),
    EMP_CON_TRANS      VARCHAR2(4000),
    EMP_CON_PFT        VARCHAR2(4000),
    CONT_SUB_TOTAL     VARCHAR2(4000),
    EMP_PFT_TOTAL      VARCHAR2(4000),
    ORG_CON_DESC       VARCHAR2(4000),
    ORG_CON_OPN        VARCHAR2(4000),
    ORG_CON_TRANS      VARCHAR2(4000),
    ORG_CON_PFT        VARCHAR2(4000),
    ORG_SUB_TOTAL      VARCHAR2(4000),
    ORG_PFT_TOTAL      VARCHAR2(4000),
    OUTSTANDING_LOAN   VARCHAR2(4000),
    ZAKAT_AMOUNT       VARCHAR2(4000),
    PROFIT_MEMBER      VARCHAR2(1),
    CONTRIBUTION_TOTAL VARCHAR(4000),
    TOTAL_PROFIT       VARCHAR2(4000),
    GRAND_TOTAL        VARCHAR2(4000),
    NET_PAYABLE        VARCHAR2(4000),
    NAME               VARCHAR2(4000),
    DEPARTMENT         VARCHAR(4000),
    DESIGNATION        VARCHAR(4000),
    joining_date       date,
    leaving_date       date,
    last_year_end      date,
    year_start         date,
    EMP_LOCATION       varchar2(4000),
    ZAKAT_LIMIT        VARCHAR2(4000));
  TYPE TAB_PF_SUMMARY IS TABLE OF REC_PF_SUMMARY;

  FUNCTION GET_PF_SUMMARY(P_EMP_CODE        REGISTRATION.PATIENT.MRNO%TYPE,
                          P_NO_OF_MONTH     NUMBER DEFAULT NULL,
                          P_RACK_RATE       NUMBER DEFAULT NULL,
                          P_ZAKAT           VARCHAR2 DEFAULT 'N',
                          P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE)
    RETURN TAB_PF_SUMMARY
    PIPELINED;

END;
```

#### PAYROLL.PKG_S16FRM00100
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00100 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PAYROLL GL VOUCHER
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        05-Apr-2021   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC      DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    PAY_START_DATE     PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
    PAY_END_DATE       PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
    PAY_VOUCHER_TYPE   PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
    PAY_VOUCHER_TYPE_D PAYROLL.DEF_PAY_VOUCHER_TYPE.DESCRIPTION%TYPE,
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC    DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    CURR_DEFAULTS      DEFINITIONS.CURRENCY.DEFAULTS%TYPE,
    REMARKS            FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    VOUCHER_STATUS     FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID          FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE       FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY         FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE        FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY          FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT           IN OUT REF_GL_TRAN_MASTER,
                                 P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE,
                                 P_LOCATION_ID      IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE,
                                 P_START_DATE       IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE,
                                 P_END_DATE         IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE,
                                 P_VOUCHER_TYPE     IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO       IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);

  -------------------------------------------------------
  -- This procedue will check if user has active month --
  -------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);

  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  FUNCTION GET_TRAN_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                           P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE)
    RETURN SYS_REFCURSOR;

  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);
  ------------------------------------------------------------
  -- This function will Y/N if pay voucher is posted or not --
  ------------------------------------------------------------
  FUNCTION IS_PAY_VOUCHER_POSTED(P_ORGANIZATION_ID  IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE,
                                 P_LOCATION_ID      IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE,
                                 P_PAY_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                 P_PAY_END_DATE     IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                 P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE)
    RETURN CHAR;

  ---------------------------
  -- Voucher detail Record --
  ---------------------------
  TYPE TRAN_DETAIL_REC IS RECORD(
    DEBIT_CREDIT       CHAR(1),
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    IS_NEW             CHAR(1));

  TYPE TRAN_DETAIL_TAB IS TABLE OF TRAN_DETAIL_REC;

  -------------------------------------------------------------
  -- This Function will return entries for tran detail right --
  -------------------------------------------------------------
  PROCEDURE GET_VOUCHER_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_PAY_START_DATE    IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                               P_PAY_END_DATE      IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_RESULT            OUT SYS_REFCURSOR,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);

  ------------------------------------------------------------------
  -- This procedule will add voucher references in payroll tables --
  ------------------------------------------------------------------
  PROCEDURE ADD_VOUCHER_REFERENCES(P_LOCATION_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                   P_VOUCHER_TYPE     IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                   P_OLD_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_NEW_VOUCHER_NO   IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                                   P_PAY_START_DATE   IN DEFINITIONS.MONTHS.START_DATE%TYPE,
                                   P_PAY_END_DATE     IN DEFINITIONS.MONTHS.END_DATE%TYPE,
                                   P_ALERT_TEXT       OUT VARCHAR2,
                                   P_STOP             OUT CHAR);
  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_LOCATION_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                P_PAY_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_PAY_END_DATE     IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                P_VOUCHER_TYPE     IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO       IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_ALERT_TEXT       OUT VARCHAR2,
                                P_STOP             OUT CHAR);
  -------------------------------------------------------------
  -- This Procedure will generate the tempory salary voucher --
  -------------------------------------------------------------
  PROCEDURE GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                                  P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                  P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_TRANS_DATE        IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
                                  P_CURRENCY_ID       IN FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
                                  P_CURRENCY_RATE     IN FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
                                  P_REMARKS           IN FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
   PROCEDURE CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                               P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                               P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_LOGIN_LOCATION_ID IN VARCHAR2,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                               P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                               P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                               P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_TRANS_DATE        IN DATE,
                               P_LOGIN_LOCATION_ID IN VARCHAR2,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                               P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);

  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_PAY_VOUCHER_TYPE  IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE,
                         P_PAY_START_DATE    IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                         P_PAY_END_DATE      IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                         P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                         P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                         P_LOGIN_LOCATION_ID IN VARCHAR2,
                         P_USER_MRNO         IN VARCHAR2,
                         P_TERMINAL          IN VARCHAR2,
                         P_OBJECT_CODE       IN VARCHAR2,
                         P_NEW_VOUCHER_NO    OUT VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT CHAR);

  ---------------------------------------------------------------------
  -- This function will add get the maximum serial no in voucher     --
  ---------------------------------------------------------------------
  FUNCTION GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)
    RETURN NUMBER;

END;
```

#### PAYROLL.PKG_S16FRM00101
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00101 IS

  /********************************************************************************************************
         OBJECTIVE :=   Base Package of S16FRM00101 - DEF_BATCH CR Id: To be entered JIRA Ticket: To be entered
         --------------------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        21-May-2021   Muhammad Farhan         1. Created this Package.
  ********************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------------------------------
  -- Employee Expense List Record Group --
  ------------------------------------------
  TYPE EMP_EXP_REC IS RECORD(
    EXPENSE_LIST_ID     PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE,
    EXPENSE_CODE        PAYROLL.EMP_EXPENSE_LIST.EXPENSE_CODE%TYPE,
    EXPENSE_DESCRIPTION PAYROLL.DEF_EXPENSE.DESCRIPTION%TYPE,
    TRANS_DATE          PAYROLL.EMP_EXPENSE_LIST.TRANS_DATE%TYPE,
    REMARKS             PAYROLL.EMP_EXPENSE_LIST.REMARKS%TYPE,
    VOUCHER_TYPE        PAYROLL.EMP_EXPENSE_LIST.VOUCHER_TYPE%TYPE,
    VOUCHER_NO          PAYROLL.EMP_EXPENSE_LIST.VOUCHER_NO%TYPE,
    START_DATE          PAYROLL.EMP_EXPENSE_LIST.START_DATE%TYPE,
    END_DATE            PAYROLL.EMP_EXPENSE_LIST.END_DATE%TYPE,
    PAYROLL_LOCATION_ID PAYROLL.EMP_EXPENSE_LIST.PAYROLL_LOCATION_ID%TYPE,
    UPD_ALLOWED     CHAR(1));

  ----------------------------------------
  -- Employee Expense List Ref Cursor --
  ----------------------------------------
  TYPE EMP_EXP_REF IS REF CURSOR RETURN EMP_EXP_REC;

  -----------------------------
  -- Employee Expense Array --
  -----------------------------
  TYPE EMP_EXP_TAB IS TABLE OF EMP_EXP_REC INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------
  -- This Procedure is used to query Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE QUERY_EMP_EXP(P_RESULT          IN OUT EMP_EXP_REF,
                          P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE);

  -------------------------------------------------------------
  -- This Procedure is used to Insert Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE INSERT_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB);

  -------------------------------------------------------------
  -- This Procedure is used to Update Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE UPDATE_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB);

  -------------------------------------------------------------
  -- This Procedure is used to Delete Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE DELETE_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB);

  -------------------------------------------------------------
  -- This Procedure is used to Lock Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE LOCK_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB);

  -------------------------------------------------
  -- Employee Expense List Detail Record Group --
  -------------------------------------------------
  TYPE EMP_EXP_DTL_REC IS RECORD(
    EXPENSE_LIST_ID PAYROLL.EMP_EXPENSE_LIST_DTL.EXPENSE_LIST_ID%TYPE,
    MRNO            PAYROLL.EMP_EXPENSE_LIST_DTL.MRNO%TYPE,
    NAME            HRD.VU_INFORMATION.NAME%TYPE,
    DEPARTMENT      HRD.VU_INFORMATION.DEPARTMENT%TYPE,
    DESIGNATION     HRD.VU_INFORMATION.DESIGNATION%TYPE,
    AMOUNT          PAYROLL.EMP_EXPENSE_LIST_DTL.AMOUNT%TYPE,
    TAX_DEDUCTED    PAYROLL.EMP_EXPENSE_LIST_DTL.TAX_DEDUCTED%TYPE,
    STATUS_ID       PAYROLL.EMP_EXPENSE_LIST_DTL.STATUS_ID%TYPE,
    STATUS_DESC     ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE,
    SELECT_FLAG     PAYROLL.EMP_EXPENSE_LIST_DTL.SELECT_FLAG%TYPE,
    ERROR_LOG       PAYROLL.EMP_EXPENSE_LIST_DTL.ERROR_LOG%TYPE);

  -----------------------------------------------
  -- Employee Expense List Detail Ref Cursor --
  -----------------------------------------------
  TYPE EMP_EXP_DTL_REF IS REF CURSOR RETURN EMP_EXP_DTL_REC;

  ------------------------------------
  -- Employee Expense Detail Array --
  ------------------------------------
  TYPE EMP_EXP_DTL_TAB IS TABLE OF EMP_EXP_DTL_REC INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------
  -- This Procedure is used to query Employee Expense List --
  -------------------------------------------------------------
  PROCEDURE QUERY_EMP_EXP_DTL(P_RESULT          IN OUT EMP_EXP_DTL_REF,
                              P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST_DTL.EXPENSE_LIST_ID%TYPE,
                              P_MRNO            IN PAYROLL.EMP_EXPENSE_LIST_DTL.MRNO%TYPE,
                              P_QUERY           IN CHAR);

  -------------------------------------------------------------------
  -- This Procedure is used to Insert Employee Expense List Detail --
  -------------------------------------------------------------------
  PROCEDURE INSERT_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB);

  -------------------------------------------------------------------
  -- This Procedure is used to Update Employee Expense List Detail --
  -------------------------------------------------------------------
  PROCEDURE UPDATE_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB);

  -------------------------------------------------------------------
  -- This Procedure is used to Delete Employee Expense List Detail --
  -------------------------------------------------------------------
  PROCEDURE DELETE_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB);

  -------------------------------------------------------------------
  -- This Procedure is used to Lock Employee Expense List Detail --
  -------------------------------------------------------------------
  PROCEDURE LOCK_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB);
  -------------------------------------------------------------------
  -- This Procedure is used to POST Employee Expense List Detail --
  -------------------------------------------------------------------
  PROCEDURE POST_EXPENSE_LIST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_EXPENSE_LIST_ID   IN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE,
                              P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                              P_USER_MRNO         IN VARCHAR2,
                              P_TERMINAL          IN VARCHAR2,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);
  FUNCTION GEN_EXPENSE_LIST_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_TRAN_DATE         IN DATE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE;

END PKG_S16FRM00101;
```

#### PAYROLL.PKG_S16FRM00102
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00102 IS
  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for Employee tax calculation comparison
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        13-Aug-2021   M. Ali Khubaib         1. Created this Package.
  ************************************************************************************************/
  ------------------
  -- Record Group --
  ------------------
  TYPE TAX_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(15));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE TAX_REF IS REF CURSOR RETURN TAX_REC;
  TYPE TAB_TAX IS TABLE OF TAX_REC;
  ------------------------------------------
  -- This procedure will query TAX MONTH  --
  ------------------------------------------
  PROCEDURE QUERY_TAX(P_RESULT              IN OUT TAX_REF,
                      P_MONTH_START_DATE    IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                      P_MONTH_END_DATE      IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                      P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE);

  -- pipeline Function for query TAX --                          
  FUNCTION F_QUERY_TAX_APEX(P_MONTH_START_DATE    IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE,
                            P_MONTH_END_DATE      IN PAYROLL.PAY_STATUS.DATE_TO%TYPE,
                            P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN TAB_TAX
    PIPELINED;
  ------------------
  ------------------
  -- Record Group --
  ------------------
  TYPE DEP_REC IS RECORD(
    START_DATE            PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
    END_DATE              PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
    DEPARTMENT_ID         DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT            DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    PREVIOUS_AMOUNT       NUMBER(20, 2),
    CURRENT_AMOUNT        NUMBER(20, 2),
    DIFFERENCE            NUMBER(20, 2),
    PERCENTAGE            NUMBER(20, 2),
    TOTAL_PREVIOUS_AMOUNT NUMBER(20, 2),
    TOTAL_CURRENT_AMOUNT  NUMBER(20, 2),
    TOTAL_DIFFERENCE      NUMBER(20, 2));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE DEP_REF IS REF CURSOR RETURN DEP_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE DEP_TAB IS TABLE OF DEP_REC INDEX BY BINARY_INTEGER;
  TYPE DEP_TAB_APEX IS TABLE OF DEP_REC;
  -----------------------------------------------------
  -- This procedure will query PAYROLL.PAY_ITAX_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_DEPARTMENT(P_RESULT              IN OUT DEP_REF,
                             P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_START_DATE          IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                             P_END_DATE            IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                             P_DEPARTMENT          IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                             P_CRITERIA_ID         IN NUMBER,
                             P_DIFFERENCE          IN CHAR,
                             P_ORDER_BY            IN VARCHAR2);
  -- pipeline Function for query DEPARTMNET --                          
  FUNCTION F_QUERY_DEPARTMENT_APEX(P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_START_DATE          IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                                   P_END_DATE            IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                                   P_DEPARTMENT          IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                                   P_CRITERIA_ID         IN NUMBER,
                                   P_DIFFERENCE          IN CHAR,
                                   P_ORDER_BY            IN VARCHAR2)
    RETURN DEP_TAB_APEX
    PIPELINED;
  ------------------
  ------------------
  -- Record Group --
  ------------------
  TYPE ITAX_DETAIL_REC IS RECORD(
    START_DATE      PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
    END_DATE        PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
    MRNO            PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT_ID   DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE           DEFINITIONS.GRADES.GRADE_ID%TYPE,
    EMP_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PREVIOUS_AMOUNT NUMBER(20, 2),
    CURRENT_AMOUNT  NUMBER(20, 2),
    NEW_JOINER      NUMBER(3),
    DIFFERENCE      NUMBER(20, 2),
    PERCENTAGE      NUMBER(20, 2));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE ITAX_DETAIL_REF IS REF CURSOR RETURN ITAX_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE ITAX_DETAIL_TAB IS TABLE OF ITAX_DETAIL_REC INDEX BY BINARY_INTEGER;
  TYPE DEP_ITAX_APEX IS TABLE OF ITAX_DETAIL_REC;
  -----------------------------------------------------
  -- This procedure will query PAYROLL.PAY_ITAX_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_ITAX_DETAIL(P_RESULT              IN OUT ITAX_DETAIL_REF,
                              P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_START_DATE          IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                              P_END_DATE            IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                              P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                              P_CRITERIA_ID         IN NUMBER,
                              P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_DIFFERENCE          IN CHAR,
                              P_ORDER_BY            IN VARCHAR2);

  -- pipeline Function for query DEPARTMNET --                          
  FUNCTION F_QUERY_ITAX_DETAIL_APEX(P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_START_DATE          IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                                    P_END_DATE            IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                                    P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                                    P_CRITERIA_ID         IN NUMBER,
                                    P_DIFFERENCE          IN CHAR,
                                    P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_ORDER_BY            IN VARCHAR2)
    RETURN DEP_ITAX_APEX
    PIPELINED;
  ------------------
  -----------------------------------------------------------------------
  -- This procedure will populate comparison data into temporary table --
  -----------------------------------------------------------------------
  PROCEDURE POPULATE_DATA(P_ORGANIZATION_ID     IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_CSTART_DATE         IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                          P_CEND_DATE           IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                          P_USER_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_TERMINAL            IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                          P_ALERT_TEXT          OUT VARCHAR2,
                          P_STOP                OUT CHAR);

  --------------------------------------------------------------
  -- This function will return total of previous month amount --
  --------------------------------------------------------------
  FUNCTION GET_PREV_MONTH_TOTAL(P_START_DATE          IN DATE,
                                P_END_DATE            IN DATE,
                                P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CRITERIA_ID         IN NUMBER)
    RETURN NUMBER;

  -------------------------------------------------------------
  -- This function will return total of current month amount --
  -------------------------------------------------------------
  FUNCTION GET_CURR_MONTH_TOTAL(P_START_DATE          IN DATE,
                                P_END_DATE            IN DATE,
                                P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CRITERIA_ID         IN NUMBER)
    RETURN NUMBER;

END PKG_S16FRM00102;
```

#### PAYROLL.PKG_S16FRM00103
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00103 IS
  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        22-SEP-2021   M. Ali Khubaib         1. Created this Package.
  ************************************************************************************************/
  ------------------
  -- Record Group --
  ------------------
  TYPE MONTH_REC IS RECORD(
    MON_START_DATE    DATE,
    MON_END_DATE      DATE,
    MONTH_DESCRIPTION VARCHAR2(50));

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE MONTH_REF IS REF CURSOR RETURN MONTH_REC;
  ------------------------------------------
  -- This procedure will query MONTH MONTH  --
  ------------------------------------------
  PROCEDURE QUERY_MONTH(P_RESULT           IN OUT MONTH_REF,
                        P_MONTH_START_DATE IN DEFINITIONS.Location_Wise_Months.MON_START_DATE%TYPE,
                        P_MONTH_END_DATE   IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE EMP_DETAIL_REC IS RECORD(
    START_DATE        DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE,
    END_DATE          DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE,
    MRNO              REGISTRATION.PATIENT.MRNO%TYPE,
    NAME              REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION       DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT        DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    GRADE             DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    EMP_LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    EMP_LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    VOUCHER_TYPE      FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO        FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    AMOUNT            NUMBER(20, 2),
    STATUS_ID         PAYROLL.EMP_PAYMENT.STATUS_ID%TYPE,
    STATUS_DESC       VARCHAR2(50),
    EXPENSE_CODE      PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE EMP_DETAIL_REF IS REF CURSOR RETURN EMP_DETAIL_REC;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE EMP_DETAIL_TAB IS TABLE OF EMP_DETAIL_REC INDEX BY BINARY_INTEGER;

  -----------------------------------------------------
  -- This procedure will query PAYROLL.PAY_ITAX_DETAIL --
  -----------------------------------------------------
  PROCEDURE QUERY_EMP_DETAIL(P_RESULT              IN OUT EMP_DETAIL_REF,
                             P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_START_DATE          IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE,
                             P_END_DATE            IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE,
                             P_PAYMENT_MODE        IN PAYROLL.PAY_MASTER.PAYMENT_MODE%TYPE,
                             P_CRITERIA            IN NUMBER,
                             P_MRNO                IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_ORDER_BY            IN VARCHAR2);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_MASTER IS RECORD(
    DOCUMENT_NO     PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE,
    VOUCHER_TYPE    FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO      FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    TRANS_DATE      FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE,
    CURRENCY_ID     FINANCE.GL_TRAN_MASTER.CURRENCY_ID%TYPE,
    CURRENCY_RATE   FINANCE.GL_TRAN_MASTER.CURRENCY_RATE%TYPE,
    CURR_SHORT_DESC DEFINITIONS.CURRENCY.SHORT_DESCRIPTION%TYPE,
    REFERENCE_NO    FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
    REMARKS         FINANCE.GL_TRAN_MASTER.REMARKS%TYPE,
    PARTY_NAME      FINANCE.GL_TRAN_MASTER.PARTY_NAME%TYPE,
    PARTY_SUB_CODE  FINANCE.GL_TRAN_MASTER.PARTY_SUB_CODE%TYPE,
    VOUCHER_STATUS  FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE,
    MODULE_ID       FINANCE.GL_TRAN_MASTER.MODULE_ID%TYPE,
    ENTERED_DATE    FINANCE.GL_TRAN_MASTER.ENTERED_DATE%TYPE,
    ENTERED_BY      FINANCE.GL_TRAN_MASTER.ENTERED_BY%TYPE,
    POSTED_DATE     FINANCE.GL_TRAN_MASTER.POSTED_DATE%TYPE,
    POSTED_BY       FINANCE.GL_TRAN_MASTER.POSTED_BY%TYPE,
    MRNO            FINANCE.GL_TRAN_MASTER.MRNO%TYPE,
    LOCATION_ID     FINANCE.GL_TRAN_MASTER.LOCATION_ID%TYPE,
    DR_CR_GENERAL   FINANCE.GL_VOUCHER_TYPE.DR_CR_GENERAL%TYPE,
    OBJECT_CODE     FINANCE.GL_TRAN_MASTER.OBJECT_CODE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_MASTER IS REF CURSOR RETURN REC_GL_TRAN_MASTER;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_GL_TRAN_MASTER IS TABLE OF REC_GL_TRAN_MASTER INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query FINANCE.GL_TRAN_MASTER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_MASTER(P_RESULT       IN OUT REF_GL_TRAN_MASTER,
                                 P_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_START_DATE   IN DATE,
                                 P_END_DATE     IN DATE,
                                 P_PAYMENT_MODE IN CHAR,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);

  ------------------------------------------------------
  -- This procedure will INSERT FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ------------------------------------------------------
  -- This procedure will Delete FINANCE.GL_TRAN_MASTER --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);

  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_MASTER --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER);
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_GL_TRAN_DETAIL IS RECORD(
    VOUCHER_TYPE       FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
    VOUCHER_NO         FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
    SERIAL_NO          FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE,
    TRANS_DATE         FINANCE.GL_TRAN_DETAIL.TRANS_DATE%TYPE,
    LEDGER_TYPE_CODE   FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
    SUB_LDGR_ITEM_CODE FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
    SUB_LDGR_ITEM_DESC FINANCE.GL_SUB_LEDGERS.SUB_LDGR_ITEM_DESC%TYPE,
    COA_CODE           FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
    COA_CODE_DESC      FINANCE.GL_COA.COA_DESCRIPTION%TYPE,
    REFERENCE_NO       FINANCE.GL_TRAN_DETAIL.REFERENCE_NO%TYPE,
    NARRATION          FINANCE.GL_TRAN_DETAIL.NARRATION%TYPE,
    PRE_POST_DR        FINANCE.GL_TRAN_DETAIL.PRE_POST_DR%TYPE,
    PRE_POST_CR        FINANCE.GL_TRAN_DETAIL.PRE_POST_CR%TYPE,
    DR_AMOUNT          FINANCE.GL_TRAN_DETAIL.DR_AMOUNT%TYPE,
    CR_AMOUNT          FINANCE.GL_TRAN_DETAIL.CR_AMOUNT%TYPE,
    COA_STATUS         FINANCE.GL_TRAN_DETAIL.COA_STATUS%TYPE,
    CURRENCY_ID        FINANCE.GL_TRAN_DETAIL.CURRENCY_ID%TYPE,
    CURRENCY_RATE      FINANCE.GL_TRAN_DETAIL.CURRENCY_RATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_GL_TRAN_DETAIL IS REF CURSOR RETURN REC_GL_TRAN_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE GL_TRAN_DETAIL_TAB IS TABLE OF REC_GL_TRAN_DETAIL INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PAY VOUCHER --
  -------------------------------------------
  PROCEDURE QUERY_GL_TRAN_DETAIL(P_RESULT       IN OUT REF_GL_TRAN_DETAIL,
                                 P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                 P_VOUCHER_NO   IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE);
  ------------------------------------------------------
  -- This procedure will insert FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will update FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ------------------------------------------------------
  -- This procedure will DELETE FINANCE.GL_TRAN_DETAIL --
  ------------------------------------------------------
  PROCEDURE DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);
  ----------------------------------------------------
  -- This procedure will lock FINANCE.GL_TRAN_DETAIL --
  ----------------------------------------------------
  PROCEDURE LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB);

  --------------------------------------------------------------------------------------------
  -- This procedure will populate employee expense detail and generate GL temporary voucher --
  --------------------------------------------------------------------------------------------
  PROCEDURE GENERATE_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_PAYMENT_MODE      IN CHAR,
                             P_START_DATE        IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                             P_END_DATE          IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                             P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_EXPENSE_CODE      IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE,
                             P_TRANS_DATE        IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE,
                             P_CURRENCY_ID       IN FINANCE.PF_TRAN_MASTER.CURRENCY_ID%TYPE,
                             P_CURRENCY_RATE     IN FINANCE.PF_TRAN_MASTER.CURRENCY_RATE%TYPE,
                             P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE,
                             P_COA_CODE          IN FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE,
                             P_LEDGER_TYPE_CODE  IN FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE,
                             P_SUBSIDARY_CODE    IN FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE,
                             P_REFERENCE_NO      IN FINANCE.GL_TRAN_MASTER.REFERENCE_NO%TYPE,
                             P_REMARKS           IN FINANCE.PF_TRAN_MASTER.REMARKS%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_OBJECT_CODE       IN VARCHAR2,
                             P_NEW_VOUCHER_TYPE  OUT FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                             P_NEW_VOUCHER_NO    OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);

  ----------------------------------------------------
  -- This Procedure will post the temporary voucher --
  ----------------------------------------------------
  PROCEDURE POST_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_VOUCHER_TYPE      IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                         P_VOUCHER_NO        IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE,
                         P_START_DATE        IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE,
                         P_END_DATE          IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE,
                         P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_USER_MRNO         IN VARCHAR2,
                         P_TERMINAL          IN VARCHAR2,
                         P_OBJECT_CODE       IN VARCHAR2,
                         P_NEW_VOUCHER_NO    OUT VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT CHAR);

  ------------------------------------------------------
  -- Following procedure will delete voucher refrences --
  -------------------------------------------------------
  PROCEDURE DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                P_LOGIN_LOCATION_ID IN VARCHAR2,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);

  ------------------------------------------------------
  -- This Procedure will cancel the posted voucher GL --
  ------------------------------------------------------
  PROCEDURE CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_LOGIN_LOCATION_ID IN VARCHAR2,
                                  P_USER_MRNO         IN VARCHAR2,
                                  P_TERMINAL          IN VARCHAR2,
                                  P_OBJECT_CODE       IN VARCHAR2,
                                  P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                                  P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                                  P_ALERT_TEXT        OUT VARCHAR2,
                                  P_STOP              OUT CHAR);

  ----------------------------------------------------
  -- Following procedure will cancel/delete voucher --
  ----------------------------------------------------
  PROCEDURE CANCEL_VOUCHER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_VOUCHER_TYPE      IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                           P_VOUCHER_NO        IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                           P_LOGIN_LOCATION_ID IN VARCHAR2,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_NEW_VOUCHER_TYPE  OUT FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE,
                           P_NEW_VOUCHER_NO    OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);

  ---------------------------------------------------------------------
  -- This procedule will add insert gl opening balance if not exists --
  ---------------------------------------------------------------------
  PROCEDURE INIT_GL_OPENING_BALANCE(P_COA_CODE           IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE,
                                    P_LEDGER_TYPE_CODE   IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE,
                                    P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE,
                                    P_ALERT_TEXT         OUT VARCHAR2,
                                    P_STOP               OUT CHAR);

  -----------------------------------------------------------
  -- This procedue will check if user has active month     --
  -----------------------------------------------------------
  PROCEDURE CHECK_ACTIVE_MONTH(P_USER_ID    IN FINANCE.GL_MONTH_USERS.USERID%TYPE,
                               P_TRAN_DATE  IN DATE,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT VARCHAR2);
  -----------------------------------------------------------
  -- This function will get reference required or not     --
  -----------------------------------------------------------
  FUNCTION GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2)
    RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE;

  -----------------------------------------------------------
  -- This procedure will update reference no     --
  -----------------------------------------------------------
  PROCEDURE UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO      IN CHAR,
                                     P_VOUCHER_TYPE    IN CHAR,
                                     P_NEW_VOUCHER_NO  IN CHAR,
                                     P_OBJECT_CODE     IN CHAR,
                                     P_STOP            OUT CHAR,
                                     P_ALERT_TEXT      OUT VARCHAR2);

END PKG_S16FRM00103;
```

#### PAYROLL.PKG_S16FRM00104
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00104 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for PF Final Settlement
         -----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        01-NOV-2021   M. ALI KHUBAIB         1. Created this Package.
  ************************************************************************************************/

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMP IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DESIGNATION     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    GRADE           DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    YEAR_CODE       PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE,
    FROM_DATE       DATE,
    TO_DATE         DATE,
    ADJUSTMENT_CODE PAYROLL.EMP_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE,
    ADJUSTMENT_DESC VARCHAR2(500),
    AMOUNT          NUMBER(20, 2),
    REMARKS         PAYROLL.EMP_ITAX_ADJUSTMENT.REMARKS%TYPE,
    CURRENT_TAX     PAYROLL.EMP_ITAX_ADJUSTMENT.CURRENT_TAX%TYPE,
    CURRENT_INCOME  PAYROLL.EMP_ITAX_ADJUSTMENT.CURRENT_INCOME%TYPE,
    POSTED          PAYROLL.EMP_ITAX_ADJUSTMENT.POSTED%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_EMP IS REF CURSOR RETURN REC_EMP;
  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_EMP IS TABLE OF REC_EMP INDEX BY BINARY_INTEGER;

  -----------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_ITAX_ADJUSTMENT --
  -----------------------------------------------------------
  PROCEDURE QUERY_EMP_ITAX(P_RESULT          IN OUT REF_EMP,
                           P_MRNO            IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_YEAR_CODE       IN PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE,
                           P_ADJUSTMENT_CODE IN PAYROLL.DEF_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE);

  ------------------------------------------------------------
  -- This procedure will insert PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE INSERT_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE UPDATE_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_ITAX_ADJUSTMENT --
  ------------------------------------------------------------
  PROCEDURE DELETE_ITAX(P_RESULT IN OUT TAB_EMP);

  ----------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_ITAX_ADJUSTMENT --
  ----------------------------------------------------------
  PROCEDURE LOCK_ITAX(P_RESULT IN OUT TAB_EMP);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_ITAX_DETAIL IS RECORD(
    YEAR_CODE       PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE,
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    ADJUSTMENT_CODE PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE,
    SRNO            PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.SRNO%TYPE,
    AMOUNT          PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.AMOUNT%TYPE,
    REMARKS         PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.REMARKS%TYPE,
    ENTRY_DATE      PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ENTRY_DATE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_ITAX_DETAIL IS REF CURSOR RETURN REC_ITAX_DETAIL;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE ITAX_DETAIL_TAB IS TABLE OF REC_ITAX_DETAIL INDEX BY BINARY_INTEGER;

  ---------------------------------------------------------------
  -- This procedure will query PAYROLL.EMP_ITAX_ADJUSTMENT_DTL --
  ---------------------------------------------------------------
  PROCEDURE QUERY_ITAX_DETAIL(P_RESULT          IN OUT REF_ITAX_DETAIL,
                              P_YEAR_CODE       IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE,
                              P_MRNO            IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_ADJUSTMENT_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE);
  ----------------------------------------------------------------
  -- This procedure will insert PAYROLL.EMP_ITAX_ADJUSTMENT_DTL --
  ----------------------------------------------------------------
  PROCEDURE INSERT_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);
  ----------------------------------------------------------------
  -- This procedure will update PAYROLL.EMP_ITAX_ADJUSTMENT_DTL --
  ----------------------------------------------------------------
  PROCEDURE UPDATE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);
  ----------------------------------------------------------------
  -- This procedure will DELETE PAYROLL.EMP_ITAX_ADJUSTMENT_DTL --
  ----------------------------------------------------------------
  PROCEDURE DELETE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);
  --------------------------------------------------------------
  -- This procedure will lock PAYROLL.EMP_ITAX_ADJUSTMENT_DTL --
  --------------------------------------------------------------
  PROCEDURE LOCK_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB);

  ------------------------------------------
  -- This Procedure will the exempted tax --
  ------------------------------------------
  PROCEDURE CALCULATE_EXEMPTED_TAX(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_YEAR_CODE         IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_ADJUSTMENT_CODE   IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE,
                                   P_OBJECT_CODE       IN VARCHAR2,
                                   P_TERMINAL          IN VARCHAR2,
                                   P_USER_MRNO         IN VARCHAR2,
                                   P_CURRENT_INCOME    OUT NUMBER,
                                   P_CURRENT_TAX       OUT NUMBER,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);

  ----------------------------------------------------
  -- This Procedure will post and unpost the record --
  ----------------------------------------------------
  PROCEDURE POST_UNPOST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                        P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_POST_UNPOST       IN CHAR,
                        P_YEAR_CODE         IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE,
                        P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                        P_ADJUSTMENT_CODE   IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE,
                        P_CURRENT_INCOME    IN NUMBER,
                        P_CURRENT_TAX       IN NUMBER,
                        P_OBJECT_CODE       IN VARCHAR2,
                        P_TERMINAL          IN VARCHAR2,
                        P_USER_MRNO         IN VARCHAR2,
                        P_ALERT_TEXT        OUT VARCHAR2,
                        P_STOP              OUT CHAR);

END;
```

#### PAYROLL.PKG_S16FRM00106
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16FRM00106 IS

  /*******************************************************************************************************
         OBJECTIVE :=   This package is used to encapsulate procedure/function(s) of Emp Awards - S16FRM00106
         -------------------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                     Description
         ---------  -----------   -----------------------   -----------------------------------
         1.0        21-FEB-2022  Muhammad Farhan 600-7098    1. Created this Package.
  ************************************************************************************************/
  -------------------------------------------------------------------
  -- This Function is used to return the Version of this Package --
  -------------------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMP_AWARD IS RECORD(
    AWARD_ID            PAYROLL.EMP_AWARDS.AWARD_ID%TYPE,
    MRNO                PAYROLL.EMP_AWARDS.MRNO%TYPE,
    NAME                HRD.VU_INFORMATION.NAME%TYPE,
    DESIGNATION         HRD.VU_INFORMATION.DESIGNATION%TYPE,
    DEPARTMENT          HRD.VU_INFORMATION.DEPARTMENT%TYPE,
    EXPENSE_CODE        PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE,
    EXPENSE_CODE_DESC   PAYROLL.DEF_EXPENSE.DESCRIPTION%TYPE,
    DUE_DATE            PAYROLL.EMP_AWARDS.DUE_DATE%TYPE,
    JOINING_DATE        PAYROLL.EMP_AWARDS.JOINING_DATE%TYPE,
    ENTRY_DATE          PAYROLL.EMP_AWARDS.ENTRY_DATE%TYPE,
    PAYROLL_LOCATION_ID PAYROLL.EMP_AWARDS.PAYROLL_LOCATION_ID%TYPE,
    PAYMENT_BASE        VARCHAR2(50),
    PAYMENT_RATE        PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE,
    AWARD_AMOUNT        PAYROLL.EMP_AWARDS.AWARD_AMOUNT%TYPE,
    ADJ_DUE_AMOUNT      PAYROLL.EMP_AWARDS.ADJ_DUE_AMOUNT%TYPE,
    ADJ_DUE_DATE        PAYROLL.EMP_AWARDS.ADJ_DUE_DATE%TYPE,
    BALANCE             NUMBER(20, 2));

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_EMP_AWARD IS REF CURSOR RETURN REC_EMP_AWARD;

  -------------------------------------------------
  -- This Procedure is used to query Emp Awards --
  -------------------------------------------------
  PROCEDURE QUERY_EMP_AWARDS(P_RESULT         IN OUT REF_EMP_AWARD,
                             P_AWARD_ID       IN PAYROLL.EMP_AWARDS.AWARD_ID%TYPE,
                             P_PAY_START_DATE IN DATE,
                             P_PAY_END_DATE   IN DATE,
                             P_EXPENSE_CODE   IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_EMP_AWARD_PAY IS RECORD(
    PAYMENT_ID          PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_ID%TYPE,
    AWARD_ID            PAYROLL.EMP_AWARD_PAYMENT.AWARD_ID%TYPE,
    PAYROLL_LOCATION_ID PAYROLL.EMP_AWARD_PAYMENT.PAYROLL_LOCATION_ID%TYPE,
    BASE_GROSS          PAYROLL.EMP_AWARD_PAYMENT.BASE_GROSS%TYPE,
    BASE_BASIC          PAYROLL.EMP_AWARD_PAYMENT.BASE_BASIC%TYPE,
    AMOUNT              PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE,
    PAYMENT_BY          PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_BY%TYPE,
    PAYMENT_BY_NAME     REGISTRATION.PATIENT.NAME%TYPE,
    PAYMENT_DATE        PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_DATE%TYPE,
    MON_START_DATE      PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE,
    MON_END_DATE        PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE,
    AD_CODE             PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE,
    DOCUMENT_NO         PAYROLL.EMP_AWARD_PAYMENT.DOCUMENT_NO%TYPE,
    STATUS_ID           PAYROLL.EMP_AWARD_PAYMENT.STATUS_ID%TYPE,
    ORDER_STATUS_DESC   ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE,
    PAYMENT_MODE        VARCHAR2(100));

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_EMP_AWARD_PAY IS REF CURSOR RETURN REC_EMP_AWARD_PAY;

  ---------------------------------------------------------
  -- This Procedure is used to query Emp Awards Payment --
  ---------------------------------------------------------
  PROCEDURE QUERY_EMP_AWARD_PAY(P_RESULT     IN OUT REF_EMP_AWARD_PAY,
                                P_PAYMENT_ID IN PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_ID%TYPE,
                                P_AWARD_ID   IN PAYROLL.EMP_AWARD_PAYMENT.AWARD_ID%TYPE);

END PKG_S16FRM00106;
```

#### PAYROLL.PKG_S16REP00003
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00003 IS
  FUNCTION GET_NET_SALARY_REG_TOT(P_ORGANIZATION_ID IN VARCHAR2,
                                  P_LOCATION_ID     IN VARCHAR2,
                                  P_START_DATE      IN DATE,
                                  P_END_DATE        IN DATE,
                                  P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /*************************************************************/
  FUNCTION GET_NET_SALARY_EXP_TOT(P_ORGANIZATION_ID IN VARCHAR2,
                                  P_LOCATION_ID     IN VARCHAR2,
                                  P_START_DATE      IN DATE,
                                  P_END_DATE        IN DATE,
                                  P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /*****************************************************************/
  FUNCTION GET_NET_SALARY_CONS_TOT(P_ORGANIZATION_ID IN VARCHAR2,
                                   P_LOCATION_ID     IN VARCHAR2,
                                   P_START_DATE      IN DATE,
                                   P_END_DATE        IN DATE,
                                   P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /**********************************************************************/
  FUNCTION GET_NET_SALARY_LOCUM_TOT(P_ORGANIZATION_ID IN VARCHAR2,
                                    P_LOCATION_ID     IN VARCHAR2,
                                    P_START_DATE      IN DATE,
                                    P_END_DATE        IN DATE,
                                    P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /*****************************************************************************/
  FUNCTION GET_NET_SALARY_REG_B(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /*****************************************************************************/
  FUNCTION GET_NET_SALARY_REG_C(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;

  /*****************************************************************************/
  FUNCTION GET_NET_SALARY_REG_Q(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /*****************************************************************************/
  FUNCTION GET_NET_SALARY_EXP_B(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/
  FUNCTION GET_NET_SALARY_EXP_C(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/
  FUNCTION GET_NET_SALARY_EXP_Q(P_ORGANIZATION_ID IN VARCHAR2,
                                P_LOCATION_ID     IN VARCHAR2,
                                P_START_DATE      IN DATE,
                                P_END_DATE        IN DATE,
                                P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/
  FUNCTION GET_NET_SALARY_CONS_B(P_ORGANIZATION_ID IN VARCHAR2,
                                 P_LOCATION_ID     IN VARCHAR2,
                                 P_START_DATE      IN DATE,
                                 P_END_DATE        IN DATE,
                                 P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/
  function GET_NET_SALARY_CONS_C(P_ORGANIZATION_ID IN VARCHAR2,
                                 P_LOCATION_ID     IN VARCHAR2,
                                 P_START_DATE      IN DATE,
                                 P_END_DATE        IN DATE,
                                 P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/

  FUNCTION GET_NET_SALARY_CONS_Q(P_ORGANIZATION_ID IN VARCHAR2,
                                 P_LOCATION_ID     IN VARCHAR2,
                                 P_START_DATE      IN DATE,
                                 P_END_DATE        IN DATE,
                                 P_ORIGINAL_TEST   IN VARCHAR2) RETURN NUMBER;
  /**********************************************************************************/
  FUNCTION GET_NET_SALARY_LOCUM_B(P_ORGANIZATION_ID IN VARCHAR2,
                                  P_LOCATION_ID     IN VARCHAR2,
                                  P_START_DATE      IN DATE,
                                  P_END_DATE        IN DATE,
                                  P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /**********************************************************************************/
  FUNCTION GET_NET_SALARY_LOCUM_C(P_ORGANIZATION_ID IN VARCHAR2,
                                  P_LOCATION_ID     IN VARCHAR2,
                                  P_START_DATE      IN DATE,
                                  P_END_DATE        IN DATE,
                                  P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER;
  /**********************************************************************************/
    FUNCTION GET_NET_SALARY_LOCUM_Q(P_ORGANIZATION_ID IN VARCHAR2,
                                  P_LOCATION_ID     IN VARCHAR2,
                                  P_START_DATE      IN DATE,
                                  P_END_DATE        IN DATE,
                                  P_ORIGINAL_TEST   IN VARCHAR2)
    RETURN NUMBER ;
      /**********************************************************************************/
END;
```

#### PAYROLL.PKG_S16REP00079
```sql
create or replace package payroll.PKG_S16REP00079 is

  -- Author  : MHBAIG
  -- Created : 01/11/2017 1:05:07 PM
  -- Purpose : TO GET ALLOWANCES

  FUNCTION GET_FS_OTHER_SALARY(P_YEAR_CODE PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
                               P_MRNO      PAYROLL.EMP_EXPENSE.MRNO%TYPE,
                               P_TYPE      VARCHAR2) RETURN NUMBER;

end PKG_S16REP00079;
```

#### PAYROLL.PKG_S16REP00096
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00096 AS
  ----------------------------
  TYPE DATA_REC IS RECORD(

    department          DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    MRNO                REGISTRATION.PATIENT.MRNO%TYPE,
    emp_code            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME                REGISTRATION.PATIENT.NAME%TYPE,
    actual_pay_rate     payroll.pay_master_test.actual_pay_rate%TYPE,
    gross_salary        payroll.pay_master_test.gross_payable%TYPE,
    deductions          NUMBER(20),
    net_salary          NUMBER(20),
    practice_income     payroll.pay_master_test.pi_before_ded%TYPE,
    Total               NUMBER(20),
    practice_income_tax payroll.pay_master_test.practice_income_tax%TYPE,
    income_tax          payroll.pay_master_test.income_tax%TYPE);

  TYPE DATA_TAB IS TABLE OF DATA_REC;

  FUNCTION PAY_CONSULTANT_TAX(P_ORIGINAL_TEST   IN VARCHAR2,
                              P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_START_DATE      IN DATE,
                              P_END_DATE        IN DATE) RETURN DATA_TAB
    PIPELINED;

END PKG_S16REP00096;
```

#### PAYROLL.PKG_S16REP00110
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00110 IS

  /***********************************************************************************************
        -- THIS PACKAGE IS USED TO FETCH DATA ON EMP_SAL_CHANGE_NEW S16REP00110
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        23-JUN-2016   MUHAMMAD FARHAN         1. CREATED THIS PACKAGE.
  ************************************************************************************************/

  ---------------------------------------
  -- Record Type for PATIENT BILL PACKAGE --
  ---------------------------------------

  TYPE CHANGE_SAL_ALLOW_REC IS RECORD(
    EMP_MRNO        HRD.INFORMATION.MRNO%TYPE,
    SALARY_STATUS   VARCHAR2(10),
    EMP_NAME        REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION     DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    NEW_VALUE       VARCHAR2(20),
    CHANGE_DATE     PAYROLL.CHANGE_SALARY_ALLOW.CHANGE_DATE%TYPE,
    CHANGED_BY      REGISTRATION.PATIENT.NAME%TYPE,
    OLD_VALUE       VARCHAR2(20),
    EMAIL_SENT_DATE PAYROLL.CHANGE_SALARY_ALLOW.EMAIL_SEND_DATE%TYPE);

  --------------------------------------
  -- Associative Array / PL SQL Table --
  --------------------------------------
  TYPE CHANGE_SAL_ALLOW_TAB IS TABLE OF PAYROLL.PKG_S16REP00110.CHANGE_SAL_ALLOW_REC;

  --------------------------------------------------------
  --THIS FUNCTION WILL RETURN EMP CHANGE / NEW SALARY --
  ---------------------------------------------------------
  FUNCTION GET_EMP_SAL_CHANGE_NEW(P_FROM_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_TO_MRNO        IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_FROM_DATE      IN PAYROLL.CHANGE_SALARY_ALLOW.CHANGE_DATE%TYPE,
                                  P_TO_DATE        IN PAYROLL.CHANGE_SALARY_ALLOW.CHANGE_DATE%TYPE,
                                  P_TERMINAL       IN VARCHAR2,
                                  P_CALLING_OBJECT IN VARCHAR2,
                                  P_CALLING_USER   IN VARCHAR2,
                                  P_CALLING_EVENT  IN VARCHAR2)
    RETURN PAYROLL.PKG_S16REP00110.CHANGE_SAL_ALLOW_TAB
    PIPELINED;
  /***********************************************************************************************/
END PKG_S16REP00110;
```

#### PAYROLL.PKG_S16REP00114
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00114 IS
  TYPE ITAX_ADJUSTMENT_REC IS RECORD(

    MRNO            PAYROLL.EMP_ITAX_ADJUSTMENT.MRNO%TYPE,
    NAME            HRD.V_INFORMATION.NAME%TYPE,
    ADJUSTMENT_CODE PAYROLL.EMP_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE,
    DESCRIPTION     PAYROLL.DEF_ITAX_ADJUSTMENT.DESCRIPTION%TYPE,
    AMOUNT          PAYROLL.EMP_ITAX_ADJUSTMENT.AMOUNT%TYPE,
    REMARKS         PAYROLL.EMP_ITAX_ADJUSTMENT.REMARKS%TYPE);

  TYPE ITAX_ADJUSTMENT_REC_TAB IS TABLE OF ITAX_ADJUSTMENT_REC;

  FUNCTION EMP_ITAX_ADJUSTMENT(P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE)
    RETURN ITAX_ADJUSTMENT_REC_TAB
    PIPELINED;
END PKG_S16REP00114;
```

#### PAYROLL.PKG_S16REP00115
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00115 AS
  /*********************************************************************************
         OBJECTIVE := This package was created for EMPLOYEES NOT IN PAYROLL Report 
         ---------------------------------------------------------------------------
          Ver         Date          Author             Description
         -----    -----------    -----------      -------------------
          1.0     10-05-2018      USMAN TAHIR   1. Created this Package.
  *****************************************************************************/
  -----------------------------
  -- Record for PAYROLL --
  -----------------------------
  TYPE PAY_REC IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    NAME            REGISTRATION.PATIENT.NAME%TYPE,
    EMPLOYEE_TYPE   DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
    DESIGNATION     HRD.V_INFORMATION.DESIGNATION %TYPE,
    GRADE           HRD.V_INFORMATION.GRADE%TYPE,
    DEPARTMENT      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    JOINING_DATE    DATE,
    SAL             CHAR(3),
    SAL_CERTIFICATE CHAR(3));
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE PAY_TAB IS TABLE OF PAY_REC;
  ------------------------------------------------------------------------------
  -- This function will return the CASH_SUMMARY data against given Parameters --
  ------------------------------------------------------------------------------
  FUNCTION GET_MISSING_EMP_SAL(P_MONTH           DEFINITIONS.MONTHS.MONTH%TYPE,
                               P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAY_TAB
    PIPELINED;
END PKG_S16REP00115;
```

#### PAYROLL.PKG_S16REP00116
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00116 AS
  TYPE GEN_REP_REC IS RECORD(
    PROMPT  PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    AD_CODE PAYROLL.GENERIC_REPORT_FIELD.AD_CODE%TYPE);
  TYPE GEN_REP_TAB IS TABLE OF GEN_REP_REC INDEX BY PAYROLL.GENERIC_REPORT_FIELD.FIELD_CODE%TYPE;

  TYPE DISPLAY_TEXT_REC IS RECORD(
    MRNO_D          PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    START_DATE_D    PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    END_DATE_D      PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    EMPLOYEE_TYPE_D PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    DESIGNATION_D   PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    GRADE_D         PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    DEPARTMENT_D    PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    EMP_NO_D        PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    NAME_D          PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    CNIC_D          PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A01_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A02_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A03_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A04_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A05_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A06_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A07_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A08_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A09_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A10_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A11_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A12_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A13_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A14_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A15_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A16_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A17_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A18_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A19_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A20_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A21_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A22_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A23_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A24_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A_OTHERS_D      PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    A_TOTAL_D       PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D01_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D02_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D03_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D04_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D05_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D06_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D07_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D08_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D09_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D10_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D11_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D12_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D13_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D14_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D15_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D16_D           PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D_OTHERS_D      PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    D_TOTAL_D       PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    ARREARS_D       PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    NET_PAYABLE_D   PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    BANK_D          PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE);
  ----------------------------------
  TYPE DISPLAY_TEXT_TAB IS TABLE OF DISPLAY_TEXT_REC;
  ---------------------------------
  TYPE PAY_SLIP_REC IS RECORD(
    MRNO          PAYROLL.PAY_MASTER.MRNO%TYPE,
    START_DATE    PAYROLL.PAY_MASTER.START_DATE%TYPE,
    END_DATE      PAYROLL.PAY_MASTER.END_DATE%TYPE,
    EMPLOYEE_TYPE DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
    DESIGNATION   PAYROLL.PAY_MASTER.DESIGNATION%TYPE,
    GRADE         DEFINITIONS.GRADES.DESCRIPTION%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    EMP_NO        VARCHAR2(8),
    NAME          VARCHAR2(250),
    CNIC          REGISTRATION.PATIENT.NIC_NEW%TYPE,
    A01           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A02           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A03           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A04           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A05           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A06           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A07           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A08           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A09           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A10           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A11           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A12           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A13           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A14           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A15           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A16           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A17           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A18           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A19           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A20           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A21           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A22           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A23           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A24           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A_OTHERS      PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    A_TOTAL       PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D01           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D02           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D03           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D04           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D05           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D06           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D07           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D08           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D09           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D10           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D11           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D12           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D13           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D14           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D15           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D16           PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D_OTHERS      PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    D_TOTAL       PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    ARREARS       PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    NET_PAYABLE   PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    BANK          DEFINITIONS.BANK.DESCRIPTION%TYPE,
    GROUP_BY      VARCHAR2(500));
  ----------------------------------
  TYPE PAY_SLIP_TAB IS TABLE OF PAY_SLIP_REC;
  ---------------------------------------------------------------------------------
  --                   Retrive Data rows for report                            ----
  ---------------------------------------------------------------------------------
  FUNCTION PAY_SLIP_DETAIL(P_ORIGINAL_TEST      IN VARCHAR2,
                           P_ORGANIZATION_ID    IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_START_DATE         IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                           P_END_DATE           IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                           P_PATIENT_TYPE_ID    IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                           P_DESIGNATION_ID     IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                           P_FROM_GRADE_ID      IN DEFINITIONS.GRADES.GRADE_ID%TYPE,
                           P_TO_GRADE_ID        IN DEFINITIONS.GRADES.GRADE_ID%TYPE,
                           P_FROM_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                           P_TO_DEPARTMENT_ID   IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                           P_FROM_MRNO          IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                           P_TO_MRNO            IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                           P_PAYMENT_MODE       IN VARCHAR2,
                           P_GROUP_BY           IN VARCHAR2)
    RETURN PAYROLL.PKG_S16REP00116.PAY_SLIP_TAB
    PIPELINED;

  FUNCTION GET_AD_VALUE(P_FIELD_CODE IN VARCHAR2,
                        P_MRNO       IN PAYROLL.PAY_MASTER.MRNO%TYPE)
    RETURN NUMBER;
  ---------------------------------------------------------------------------------
  -- Get sum of all allowances/Deductions which are not part of report columns ----
  ---------------------------------------------------------------------------------
  FUNCTION GET_OTHER_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                        P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                        P_MRNO            IN PAYROLL.PAY_MASTER.MRNO%TYPE,
                        P_AD_TYPE         IN VARCHAR2) RETURN NUMBER;
  ---------------------------------------------------------------------------------
  --                 Get sum of all Deductions                                 ----
  ---------------------------------------------------------------------------------
  FUNCTION GET_TOTAL_DEDUCTIONS(P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE)
    RETURN NUMBER;
  ---------------------------------------------------------------------------------
  --                  Get column names defined in setup                        ----
  ---------------------------------------------------------------------------------
  FUNCTION GET_PROMPT(P_FIELD_CODE IN VARCHAR2) RETURN VARCHAR2;
  ---------------------------------------------------------------------------------
  --                  Retrieve column names for report headings                ----
  ---------------------------------------------------------------------------------
  FUNCTION COLUMN_HEADING(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN PAYROLL.PKG_S16REP00116.DISPLAY_TEXT_TAB
    PIPELINED;

  -- Fetch report fields in PL_SETUP_TAB --
  PROCEDURE FETCH_REPORT_FIELDS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE);

END;
```

#### PAYROLL.PKG_S16REP00118
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00118 AS
  /***********************************************************************************************
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-Jul-2018   Shahid Jamal           1. Created this Package.
         2.0        27-Jul-2018   Muhammad ALi Khubaib   1. Modified.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  --------------------------------------
  -- Record Group for PBS TRAN DETAIL --
  --------------------------------------
  TYPE ITAX_MASTER_REC IS RECORD(
    ORIG_DUP            VARCHAR2(64),
    srno                VARCHAR2(32),
    issue_date          VARCHAR2(32),
    total_tax           NUMBER,
    TOTAL_TAX_IN_WORDS2 VARCHAR2(64),
    PERSON_NAME         VARCHAR2(64),
    PERSON_ADDRESS      PAYROLL.ITAX_PAYMENT_MASTER.PERSON_ADDRESS%TYPE,
    PERSON_ADDRESS_2    PAYROLL.ITAX_PAYMENT_MASTER.PERSON_ADDRESS%TYPE,
    PERSON_NTN          PAYROLL.DEF_EMP_FINANCIAL.NTN_NO%TYPE,
    PERSON_CNIC         VARCHAR2(32),
    YEAR_DESCRIPTION    VARCHAR2(32),
    FROM_DATE           DATE,
    TO_DATE             DATE,
    SECTION_CODE        PAYROLL.ITAX_PAYMENT_MASTER.SECTION_CODE%TYPE,
    SECTION_DESCRIPTION PAYROLL.ITAX_PAYMENT_MASTER.SECTION_DESCRIPTION%TYPE,
    VIDE                PAYROLL.ITAX_PAYMENT_MASTER.VIDE%TYPE,
    TOTAL_INCOME        NUMBER,
    COMPANY_NAME        PAYROLL.ITAX_PAYMENT_MASTER.COMPANY_NAME%TYPE,
    COMPANY_ADDRESS     VARCHAR2(150),
    COMPANY_NAME_2      VARCHAR2(64),
    COMPANY_ADDRESS_2   VARCHAR2(64),
    COMPANY_date        VARCHAR2(32),
    COMPANY_NTN         VARCHAR2(32),
    AUTHORITY_NAME      VARCHAR2(150),
    AUTHORITY_NAME_2    VARCHAR2(64),
    DESIGNATION         DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    SIGNATURE           VARCHAR2(32),
    SEAL                VARCHAR2(32),
    SEAL_2              VARCHAR2(32),
    TOTAL_TAX_AMOUNT    NUMBER);

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE ITAX_MASTER_TAB IS TABLE OF ITAX_MASTER_REC;

  -----------------------------------------------------
  -- This function will return PBS_TRAN_DETAIL table --
  -----------------------------------------------------
  FUNCTION GET_ITAX_MASTER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_YEAR_CODE         IN VARCHAR2,
                           P_FROM_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_TO_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN ITAX_MASTER_TAB
    PIPELINED;
  --------------------------------------------
  TYPE ITAX_DETAIL_REC IS RECORD(
    DEPOSIT_DATE  PAYROLL.ITAX_PAYMENT_DETAIL.DEPOSIT_DATE%TYPE,
    BANK_TREASURY PAYROLL.ITAX_PAYMENT_DETAIL.BANK_TREASURY%TYPE,
    BRANCH_CITY   PAYROLL.ITAX_PAYMENT_DETAIL.BRANCH_CITY%TYPE,
    ACCOUNT       PAYROLL.ITAX_PAYMENT_DETAIL.ACCOUNT%TYPE,
    AMOUNT        PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    CPRNO         PAYROLL.ITAX_PAYMENT_DETAIL.CPRNO%TYPE,
    MRNO          PAYROLL.PAY_ALLOWANCE_DEDUCTION.MRNO%TYPE);

  TYPE ITAX_DETAIL_TAB IS TABLE OF ITAX_DETAIL_REC;

  FUNCTION GET_ITAX_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_YEAR_CODE         IN VARCHAR2,
                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN ITAX_DETAIL_TAB
    PIPELINED;

END PKG_S16REP00118;
```

#### PAYROLL.PKG_S16REP00119
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00119 AS

  /***********************************************************************************************
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-Jul-2018   Shahid Jamal           1. Created this Package.
         2.0        27-Jul-2018   Muhammad ALi Khubaib   1. Modified.
         3.0        20-NOV-2018   MUHAMMAD USMAN TAHIR   1. Modified.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  --------------------------------------
  -- Record Group for PBS TRAN DETAIL --
  --------------------------------------
  TYPE PAY_ALLOWANCE_DED_REC IS RECORD(
    AD_CODE      PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
    AD_CODE_DESC PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    AD_TYPE      PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE,
    TOTAL_AMOUNT PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE);

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE PAY_ALLOWANCE_DED_TAB IS TABLE OF PAY_ALLOWANCE_DED_REC;

  -----------------------------------------------------
  -- This function will return PBS_TRAN_DETAIL table --
  -----------------------------------------------------
  FUNCTION GET_AD_CODE_WISE_SUMMARY(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                    P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE,
                                    P_ORIGINAL_TEST     IN VARCHAR2,
                                    P_DESIGNATION_ID    IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                    P_FROM_GRADE_ID     IN DEFINITIONS.GRADES.GRADE_ID%TYPE,
                                    P_TO_GRADE_ID       IN DEFINITIONS.GRADES.GRADE_ID%TYPE,
                                    P_DEPARTMENT_ID     IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                    P_EMPLOYEE_TYPE_ID  IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                                    P_FROM_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_TO_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_AD_CODE           IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                                    P_PGROUP_ID         IN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE)
    RETURN PAY_ALLOWANCE_DED_TAB
    PIPELINED;

END PKG_S16REP00119;
```

#### PAYROLL.PKG_S16REP00120
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00120 IS

  /***********************************************************************************************
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        22-NOV-2018   MUHAMMAD USMAN TAHIR           1. CREATED THIS PACKAGE.
  ************************************************************************************************/
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE & DEDUCTION --
  ---------------------------------------------
  TYPE PAY_ALLOWANCE_DED_REC IS RECORD(
    MRNO          PAYROLL.PAY_MASTER.MRNO%TYPE,
    EMPLOYEE_NAME REGISTRATION.PATIENT.FIRST_NAME%TYPE,
    AD_CODE       PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
    DESCRIPTION   PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    CALC_AMOUNT   PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    ADJUSTMENTS   PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    START_DATE    PAYROLL.PAY_MASTER.START_DATE%TYPE,
    END_DATE      PAYROLL.PAY_MASTER.END_DATE%TYPE,
    GROUP_BY      VARCHAR2(250));

  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_ALLOWANCE_DED_TAB IS TABLE OF PAY_ALLOWANCE_DED_REC;

  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN PBS_TRAN_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_AD_CODE_WISE_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_GROUP_BY        VARCHAR2,
                                   P_START_DATE      IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                   P_END_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE,
                                   P_ORIGINAL_TEST   IN VARCHAR2,
                                   P_AD_CODE         IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
                                   P_PGROUP_ID       IN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE)
    RETURN PAY_ALLOWANCE_DED_TAB
    PIPELINED;

END PKG_S16REP00120;
```

#### PAYROLL.PKG_S16REP00122
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00122 AS

  /***********************************************************************************************
  OBJECTIVE := THIS PACKAGE WILL BE USED FOR THE FOLLOWING PURPOSE
           ----------------------------------------------------------------------------------
           REVISIONS:
           VER        DATE          AUTHOR                 DESCRIPTION
           ---------  -----------   -------------------    -----------------------------------
           1.0        25-SEP-2018   SHAHID JAMAL           CREATED THIS PACKAGE.
           2.0        15-Jan-2019   Muhammad Ali Khubaib   Modifications.
    ************************************************************************************************/
  -----------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE VERSION OF THIS PACKAGE --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -----------------------------------------------------------
  TYPE PAY_MASTER_REC IS RECORD(
    MRNO_M                 PAYROLL.PAY_MASTER.MRNO%TYPE,
    START_DATE_M           PAYROLL.PAY_MASTER.START_DATE%TYPE,
    END_DATE_M             PAYROLL.PAY_MASTER.END_DATE%TYPE,
    EMP_CODE               PAYROLL.PAY_MASTER.MRNO%TYPE,
    NAME                   HRD.VU_INFORMATION.NAME%TYPE,
    DESIGNATION            PAYROLL.PAY_MASTER.DESIGNATION%TYPE,
    DEPARTMENT             PAYROLL.PAY_MASTER.DEPARTMENT%TYPE,
    NET_PAYABLE            PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE,
    MONTHLY_SALARY         PAYROLL.PAY_MASTER.ACTUAL_PAY_RATE%TYPE,
    PAY_MODE               VARCHAR2(500),
    BANK                   DEFINITIONS.BANK_BRANCH.DESCRIPTION%TYPE,
    AC_NO                  PAYROLL.PAY_MASTER.BANK_ACCOUNT_NO%TYPE,
    SALARY_DAYS            PAYROLL.PAY_MASTER.ACTUAL_MONTH_DAYS%TYPE,
    CALC_BASIC             PAYROLL.PAY_MASTER.CALC_BASIC%TYPE,
    SHIFT_ALLOW            PAYROLL.PAY_MASTER.NIGHTS_AMOUNT%TYPE,
    OVERTIME_AMOUNT        PAYROLL.PAY_MASTER.OVERTIME_AMOUNT%TYPE,
    ARREARS                PAYROLL.PAY_MASTER.ARREARS%TYPE,
    EOBI_EMPLOYEE          PAYROLL.PAY_MASTER.EOBI_EMPLOYEE%TYPE,
    P_TOTAL                PAYROLL.PAY_MASTER.P_FUND_BALANCE%TYPE,
    P_CONTRIBUTION         PAYROLL.PAY_MASTER.P_FUND_BALANCE%TYPE,
    CURRENCY_EXCHANGE_RATE PAYROLL.PAY_MASTER.CURRENCY_EXCHANGE_RATE%TYPE,
    NATIONALITY            HRD.VU_INFORMATION.NATIONALITY%TYPE,
    UNPAID_LEAVES          PAYROLL.PAY_MASTER.UNPAID_LEAVES%TYPE,
    PREV_UNPAID_LEAVES     PAYROLL.PAY_MASTER.PREV_UNPAID_LEAVES%TYPE,
    DAILY_WAGER            PAYROLL.PAY_MASTER.DAILY_WAGER%TYPE,
    ACTUAL_PERFORMED_DAYS  PAYROLL.PAY_MASTER.ACTUAL_PERFORMED_DAYS%TYPE,
    DAILY_RATE             PAYROLL.PAY_MASTER.DAILY_RATE%TYPE,
    SHORT_WORKING_HOUR     PAYROLL.PAY_MASTER.SHORT_WORKING_HOUR%TYPE,
    JOINING_DATE           HRD.VU_INFORMATION.JOINING_DATE%TYPE,
    GRADE                  HRD.V_INFORMATION.GRADE%TYPE,
    CNIC                   VARCHAR2(60),
    NTN_NUMBER             PAYROLL.DEF_EMP_FINANCIAL.NTN_NO%TYPE,
    GP_FUND_NO             PAYROLL.DEF_EMP_FINANCIAL.GP_FUND_NO%TYPE,
    CIVIL_NO              REGISTRATION.PATIENT_OTHER_INFO.CIVIL_NO%TYPE,
    TOTAL_EMP_ALLOWANCES  NUMBER,
    TOTAL_EMP_DEDUCTIONS  NUMBER,
    TOTAL_PAY_LEAVES      NUMBER,
    TOTAL_LOAN_REFUND     NUMBER,
    TOTAL_PRACTICE_INCOME NUMBER,
    TOTAL_PAY_YD          NUMBER,
    TOTAL_PAY_YD_PI       NUMBER,
    TOTAL_PAY_ALL_YD      NUMBER,
    TOTAL_PAY_DED_YD      NUMBER,
    TOTAL_PAY_LOAD_REF_YD NUMBER,
    TOTAL_PAY_ARREARS     NUMBER,
    TOTAL_DED_ARREARS     NUMBER,
    TOTAL_PAY_AD_BALANCE  NUMBER);

  TYPE PAY_MASTER_TAB IS TABLE OF PAY_MASTER_REC;

  FUNCTION GET_PAY_MASTER(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_ORIGINAL_TEST     IN VARCHAR2,
                          P_FROM_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_TO_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_START_DATE        IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                          P_END_DATE          IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                          P_YEAR_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                          P_PAYMENT_MODE      IN PAYROLL.PAY_MASTER.PAYMENT_MODE%TYPE,
                          P_COST_CENTRE_CODE  IN PAYROLL.PAY_MASTER.COST_CENTRE_ID%TYPE,
                          P_CONS_OTHERS       IN PAYROLL.DEF_EMP_FINANCIAL.EMP_TYPE%TYPE,
                          P_DEPARTMENT_ID     IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_MASTER_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_ALLOWANCES_REC IS RECORD(
    MRNO_AL         PAYROLL.PAY_ALLOWANCE_DEDUCTION.MRNO%TYPE,
    START_DATE_AL   PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
    END_DATE_AL     PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE,
    AD_CODE         PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE,
    ALLOWANCE_TYPE  PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    ALLOWANCES      PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    PUBLIC_COA_CODE PAYROLL.Def_Ad_Constant.PUBLIC_COA_CODE%TYPE);

  TYPE PAY_ALLOWANCES_TAB IS TABLE OF PAY_ALLOWANCES_REC;

  FUNCTION GET_PAY_ALLOWANCES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_ORIGINAL_TEST     IN VARCHAR2,
                              P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                              P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_ALLOWANCES_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_DEDUCTIONS_REC IS RECORD(
    MRNO_DE         PAYROLL.PAY_ALLOWANCE_DEDUCTION.MRNO%TYPE,
    START_DATE_DE   PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
    END_DATE_DE     PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE,
    DEDUCTION_TYPE  PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    DEDUCTIONS      PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE,
    AD_CODE_DE      PAYROLL.DEF_AD_SETUP.AD_GROUP_CODE%TYPE,
    PUBLIC_COA_CODE PAYROLL.Def_Ad_Constant.PUBLIC_COA_CODE%TYPE);

  TYPE PAY_DEDUCTIONS_TAB IS TABLE OF PAY_DEDUCTIONS_REC;

  FUNCTION GET_PAY_DEDUCTIONS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_ORIGINAL_TEST     IN VARCHAR2,
                              P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                              P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_DEDUCTIONS_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_LEAVES_REC IS RECORD(
    MRNO_LE         PAYROLL.PAY_LEAVES.MRNO%TYPE,
    START_DATE_LE   PAYROLL.PAY_LEAVES.START_DATE%TYPE,
    END_DATE_LE     PAYROLL.PAY_LEAVES.END_DATE%TYPE,
    LEAVE_TYPE_ID   HRD.LEAVE_TYPE.LEAVE_TYPE_ID%TYPE,
    LEAVE_TYPE      HRD.LEAVE_TYPE.DESCRIPTION%TYPE,
    OPENING_BALANCE PAYROLL.PAY_LEAVES.OPENING_BALANCE%TYPE,
    AVAILED         PAYROLL.PAY_LEAVES.AVAILED%TYPE,
    CLOSING_BALANCE PAYROLL.PAY_LEAVES.CLOSING_BALANCE%TYPE);

  TYPE PAY_LEAVES_TAB IS TABLE OF PAY_LEAVES_REC;

  FUNCTION GET_PAY_LEAVES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_ORIGINAL_TEST     IN VARCHAR2,
                          P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                          P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                          P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_LEAVES_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_LOAN_REFUND_REC IS RECORD(
    MRNO_LO       PAYROLL.LOAN_PAYMENT_MASTER.MRNO%TYPE,
    START_DATE_LO PAYROLL.LOAN_REFUND_DETAIL.START_DATE%TYPE,
    END_DATE_LO   PAYROLL.LOAN_REFUND_DETAIL.END_DATE%TYPE,
    LOAN_TYPE     PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    REFUND_AMOUNT PAYROLL.LOAN_REFUND_DETAIL.REFUND_AMOUNT%TYPE,
    NATIONALITY   HRD.V_INFORMATION.NATIONALITY%TYPE,
    EXCHANGE_RATE PAYROLL.PAY_MASTER.CURRENCY_EXCHANGE_RATE%TYPE);

  TYPE PAY_LOAN_REFUND_TAB IS TABLE OF PAY_LOAN_REFUND_REC;

  FUNCTION GET_PAY_LOAN_REFUND(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ORIGINAL_TEST     IN VARCHAR2,
                               P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                               P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_LOAN_REFUND_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PRACTICE_INCOME_REC IS RECORD(
    MRNO_PI       PAYROLL.PAY_MASTER_TEST.MRNO%TYPE,
    START_DATE_PI PAYROLL.PAY_MASTER_TEST.START_DATE%TYPE,
    END_DATE_PI   PAYROLL.PAY_MASTER_TEST.END_DATE%TYPE,
    PI_TYPE       VARCHAR2(500),
    PI            NUMBER,
    DISP_PI       VARCHAR2(500));

  TYPE PRACTICE_INCOME_TAB IS TABLE OF PRACTICE_INCOME_REC;

  FUNCTION GET_PRACTICE_INCOME(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ORIGINAL_TEST     IN VARCHAR2,
                               P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                               P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PRACTICE_INCOME_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_YEAR_TO_DATE_REC IS RECORD(
    MRNO_YT           PAYROLL.PAY_MASTER.MRNO%TYPE,
    NET_PAYABLE_YT    PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE,
    MONTHLY_SALARY_YT PAYROLL.PAY_MASTER.ACTUAL_PAY_RATE%TYPE,
    BASIC_YT          PAYROLL.PAY_MASTER.CALC_BASIC%TYPE,
    EOBI_YT           PAYROLL.PAY_MASTER.EOBI_EMPLOYEE%TYPE,
    SHIFT_ALLOW_YT    PAYROLL.PAY_MASTER.NIGHTS_AMOUNT%TYPE,
    OVERTIME_YT       PAYROLL.PAY_MASTER.OVERTIME_AMOUNT%TYPE,
    ARREARS_YT        PAYROLL.PAY_MASTER.ARREARS%TYPE);

  TYPE PAY_YEAR_TO_DATE_TAB IS TABLE OF PAY_YEAR_TO_DATE_REC;

  FUNCTION GET_PAY_YEAR_TO_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_ORIGINAL_TEST     IN VARCHAR2,
                                P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_YEAR_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                P_END_DATE          IN PAYROLL.PAY_MASTER.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_YEAR_TO_DATE_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_YEAR_TO_DATE_PI_REC IS RECORD(
    MRNO_PIYT  PAYROLL.PAY_MASTER.MRNO%TYPE,
    PI_TYPE_YT VARCHAR2(500),
    PI_YT      NUMBER);

  TYPE PAY_YEAR_TO_DATE_PI_TAB IS TABLE OF PAY_YEAR_TO_DATE_PI_REC;

  FUNCTION GET_PAY_YEAR_TO_DATE_PI(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_ORIGINAL_TEST     IN VARCHAR2,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_YEAR_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                                   P_END_DATE          IN PAYROLL.PAY_MASTER.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_YEAR_TO_DATE_PI_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_ALL_YEAR_TO_DATE_REC IS RECORD(
    MRNO_ALYT         PAYROLL.PAY_ALLOWANCE_DEDUCTION.MRNO%TYPE,
    ALLOWANCE_TYPE_YT PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE,
    AD_CODE_ALYT      PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE,
    ALLOWANCES_YT     PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE);

  TYPE PAY_ALL_YEAR_TO_DATE_TAB IS TABLE OF PAY_ALL_YEAR_TO_DATE_REC;

  FUNCTION GET_PAY_ALL_YEAR_TO_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_ORIGINAL_TEST     IN VARCHAR2,
                                    P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                    P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_ALL_YEAR_TO_DATE_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_DED_YEAR_TO_DATE_REC IS RECORD(
    MRNO_DEYT         PAYROLL.PAY_ALLOWANCE_DEDUCTION.MRNO%TYPE,
    DEDUCTION_TYPE_YT PAYROLL.DEF_AD_GROUP.DESCRIPTION%TYPE,
    AD_CODE_DEYT      PAYROLL.DEF_AD_SETUP.AD_GROUP_CODE%TYPE,
    DEDUCTIONS_YT     PAYROLL.PAY_ALLOWANCE_DEDUCTION.CALC_AMOUNT%TYPE);

  TYPE PAY_DED_YEAR_TO_DATE_TAB IS TABLE OF PAY_DED_YEAR_TO_DATE_REC;

  FUNCTION GET_PAY_DED_YEAR_TO_DATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_ORIGINAL_TEST     IN VARCHAR2,
                                    P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                    P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_DED_YEAR_TO_DATE_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_LOAN_REFUND_YT_REC IS RECORD(
    MRNO_LOYT        PAYROLL.LOAN_PAYMENT_MASTER.MRNO%TYPE,
    LOAN_TYPE_YT     PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE,
    LOAN_CODE_YT     PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE,
    REFUND_YT        PAYROLL.LOAN_REFUND_DETAIL.REFUND_AMOUNT%TYPE,
    NATIONALITY_YT   HRD.V_INFORMATION.NATIONALITY%TYPE,
    EXCHANGE_RATE_YT PAYROLL.PAY_MASTER.CURRENCY_EXCHANGE_RATE%TYPE);

  TYPE PAY_LOAN_REFUND_YT_TAB IS TABLE OF PAY_LOAN_REFUND_YT_REC;

  FUNCTION GET_PAY_LOAN_REFUND_YT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                  P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_ORIGINAL_TEST     IN VARCHAR2,
                                  P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                  P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_LOAN_REFUND_YT_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_ARREARS_REC IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    PAY_ARREAR_CODE PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
    DESCRIPTION     PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    AMOUNT          PAYROLL.PAY_ARREAR.AMOUNT%TYPE,
    PUBLIC_COA_CODE PAYROLL.DEF_AD_CONSTANT.PUBLIC_COA_CODE%TYPE);

  TYPE PAY_ARREARS_TAB IS TABLE OF PAY_ARREARS_REC;

  FUNCTION GET_PAY_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_ORIGINAL_TEST     IN VARCHAR2,
                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                           P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_ARREARS_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE DED_ARREARS_REC IS RECORD(
    MRNO            REGISTRATION.PATIENT.MRNO%TYPE,
    DED_ARREAR_CODE PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE,
    DESCRIPTION     PAYROLL.DEF_AD_CONSTANT.DESCRIPTION%TYPE,
    AMOUNT          PAYROLL.PAY_ARREAR.AMOUNT%TYPE,
    PUBLIC_COA_CODE PAYROLL.DEF_AD_CONSTANT.PUBLIC_COA_CODE%TYPE);

  TYPE DED_ARREARS_TAB IS TABLE OF DED_ARREARS_REC;

  FUNCTION GET_DED_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_ORIGINAL_TEST     IN VARCHAR2,
                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                           P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                           P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.DED_ARREARS_TAB
    PIPELINED;

  -----------------------------------------------------------
  TYPE PAY_AD_BALANCE_REC IS RECORD(
    MRNO           PAYROLL.PAY_AD_BALANCE.MRNO%TYPE,
    START_DATE     PAYROLL.PAY_AD_BALANCE.START_DATE%TYPE,
    END_DATE       PAYROLL.PAY_AD_BALANCE.END_DATE%TYPE,
    BALANCE_AMOUNT PAYROLL.PAY_AD_BALANCE.BALANCE_AMOUNT%TYPE,
    DESCRIPTION    VARCHAR2(500));

  TYPE PAY_AD_BALANCE_TAB IS TABLE OF PAY_AD_BALANCE_REC;

  FUNCTION GET_PAY_AD_BALANCE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                              P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_ORIGINAL_TEST     IN VARCHAR2,
                              P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                              P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                              P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PKG_S16REP00122.PAY_AD_BALANCE_TAB
    PIPELINED;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_EMP_ALLOWANCE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_ORIGINAL_TEST     IN VARCHAR2,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                   P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_EMP_DEDUCTION(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_ORIGINAL_TEST     IN VARCHAR2,
                                   P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                   P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                   P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_LEAVES(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_ORIGINAL_TEST     IN VARCHAR2,
                                P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE,
                                P_LEAVE_TYPE        IN CHAR) RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_LOAN_REFUND(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_ORIGINAL_TEST     IN VARCHAR2,
                                     P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                     P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PRACTICE_INCOME(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_ORIGINAL_TEST     IN VARCHAR2,
                                     P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                     P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_YD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                            P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                            P_ORIGINAL_TEST     IN VARCHAR2,
                            P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                            P_YEAR_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                            P_END_DATE          IN PAYROLL.PAY_MASTER.END_DATE%TYPE,
                            P_PAY_YD_TYPE       IN VARCHAR2) RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_YD_PI(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ORIGINAL_TEST     IN VARCHAR2,
                               P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_YEAR_START_DATE   IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                               P_END_DATE          IN PAYROLL.PAY_MASTER.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_ALL_YD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_ORIGINAL_TEST     IN VARCHAR2,
                                P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_DED_YD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_ORIGINAL_TEST     IN VARCHAR2,
                                P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_LOAN_REF_YD(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_ORIGINAL_TEST     IN VARCHAR2,
                                     P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_YEAR_START_DATE   IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                     P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_ORIGINAL_TEST     IN VARCHAR2,
                                 P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                 P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_DED_ARREARS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_ORIGINAL_TEST     IN VARCHAR2,
                                 P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                 P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                 P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_TOTAL_PAY_AD_BALANCE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_ORIGINAL_TEST     IN VARCHAR2,
                                    P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                                    P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                                    P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN NUMBER;

  -----------------------------------------------------------
  FUNCTION GET_NATIONALITY(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN HRD.V_INFORMATION.NATIONALITY%TYPE;

  -----------------------------------------------------------
  FUNCTION GET_EXCHANGE_RATE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_ORIGINAL_TEST     IN VARCHAR2,
                             P_MRNO              IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_START_DATE        IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE,
                             P_END_DATE          IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE)
    RETURN PAYROLL.PAY_MASTER_TEST.CURRENCY_EXCHANGE_RATE%TYPE;

END PKG_S16REP00122;
```

#### PAYROLL.PKG_S16REP00130
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_S16REP00130 IS

  /***********************************************************************************************
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        25-JUL-2020   Farhan Akram           1. CREATED THIS PACKAGE.
  ************************************************************************************************/
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE  --
  ---------------------------------------------
  TYPE PAY_ITAX_REC IS RECORD(
    YEAR_CODE             PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE,
    FROM_DATE             PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE,
    TO_DATE               PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE,
    LAST_END_DATE         PAYROLL.PAY_MASTER.END_DATE%TYPE,
    REMAINING_MONTH       NUMBER(2),
    EMP_CODE              PAYROLL.PAY_MASTER.MRNO%TYPE,
    EMPLOYEE_NAME         REGISTRATION.PATIENT.FIRST_NAME%TYPE,
    DESIGNATION           VARCHAR2(250),
    DEPARTMENT            VARCHAR2(250),
    EMPLOYEE_TYPE         VARCHAR2(250),
    GRADE                 VARCHAR2(250),
    JOINING_DATE          DATE,
    CURR_GROSS            NUMBER,
    TOTAL_ANNUAL_INCOME   PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAXABLE_AMOUNT%TYPE,
    TAX_SLAB_PCNTG        PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE,
    TOTAL_TAX             PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAX%TYPE,
    PAID_TAX              PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAX%TYPE,
    ADJUSTED_TAX          PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAX%TYPE,
    RAMAINING_TAX         PAYROLL.PAY_ITAX_DETAIL.EXPECTED_YEARLY_TAX%TYPE,
    REMAINING_MONTHLY_TAX PAYROLL.PAY_ITAX_DETAIL.PROPOSED_TAX%TYPE,
    LOCATION_ID           DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    ORGANIZATION_ID       DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
    PAID_LFA              NUMBER);

  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_ITAX_TAB IS TABLE OF PAY_ITAX_REC;

  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN PBS_TRAN_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_ITAX_DETAIL(P_MRNO      IN VARCHAR2,
                           P_YEAR_CODE IN VARCHAR2,
                           P_MONTH     IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN PAY_ITAX_TAB
    PIPELINED;

 -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN PBS_TRAN_DETAIL TABLE TEST--
  -----------------------------------------------------
  FUNCTION GET_ITAX_DETAIL_TEST(P_MRNO      IN VARCHAR2,
                           P_YEAR_CODE IN VARCHAR2,
                           P_MONTH     IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE)
    RETURN PAY_ITAX_TAB
    PIPELINED;
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE  --
  ---------------------------------------------
  TYPE PAY_INCOME_DET_REC IS RECORD(
    EMPLOYEE_CODE PAYROLL.PAY_MASTER.MRNO%TYPE,
    PROMPT        PAYROLL.GENERIC_REPORT_FIELD.PROMPT%TYPE,
    AMOUNT        PAYROLL.PAY_ITAX_INCOME_DETAIL.AMOUNT%TYPE);
  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_INCOME_DET_TAB IS TABLE OF PAY_INCOME_DET_REC;
  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN GET_INCOME_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_INCOME_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_INCOME_DET_TAB
    PIPELINED;
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE  --
  ---------------------------------------------
  TYPE PAY_REC IS RECORD(
    MONTH           VARCHAR2(64),
    PAID_GROSS      PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE,
    OTHER_ALLOW     PAYROLL.PAY_MASTER.OTHER_ALLOWANCES%TYPE,
    TAX_PAID        PAYROLL.PAY_MASTER.INCOME_TAX%TYPE,
    PI_TAX_PAID     PAYROLL.PAY_MASTER.INCOME_TAX%TYPE,
    PRACTICE_INCOME PAYROLL.PAY_MASTER.PI_BEFORE_DED%TYPE);
  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_TAB IS TABLE OF PAY_REC;

  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN PBS_TRAN_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_PAID_SALARY(P_MRNO      IN VARCHAR2,
                           P_FROM_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE,
                           P_TO_DATE   IN PAYROLL.PAY_MASTER.END_DATE%TYPE)
    RETURN PAY_TAB
    PIPELINED;
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE  --
  ---------------------------------------------
  TYPE PAY_EXP_DET_REC IS RECORD(
    EMPLOYEE_CODE PAYROLL.EMP_EXPENSE.MRNO%TYPE,
    TRAN_TYPE     VARCHAR2(250),
    QTY           NUMBER,
    AMOUNT        PAYROLL.EMP_EXPENSE.AMOUNT%TYPE);
  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_EXP_DET_TAB IS TABLE OF PAY_EXP_DET_REC;
  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN GET_INCOME_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_EXP_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_EXP_DET_TAB
    PIPELINED;
  ---------------------------------------------
  -- RECORD GROUP FOR ALLOWNCE  --
  ---------------------------------------------
  TYPE PAY_TAX_ADJ_REC IS RECORD(
    EMPLOYEE_CODE PAYROLL.EMP_EXPENSE.MRNO%TYPE,
    DESCRIPTION   PAYROLL.DEF_ITAX_ADJUSTMENT.DESCRIPTION%TYPE,
    AMOUNT        PAYROLL.EMP_ITAX_ADJUSTMENT.AMOUNT%TYPE);
  -----------------------
  -- ASSOCIATIVE ARRAY --
  -----------------------
  TYPE PAY_TAX_ADJ_TAB IS TABLE OF PAY_TAX_ADJ_REC;
  -----------------------------------------------------
  -- THIS FUNCTION WILL RETURN GET_INCOME_DETAIL TABLE --
  -----------------------------------------------------
  FUNCTION GET_TAX_ADJ_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_TAX_ADJ_TAB
    PIPELINED;
END PKG_S16REP00130;
```

#### PAYROLL.PKG_SALARY_RECONCILIATION
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_SALARY_RECONCILIATION AS

  TYPE SAL_RECON_REC IS RECORD(
    MRNO               VARCHAR2(14),
    ENAME              REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION        VARCHAR2(255),
    LEAVING_DATE       DATE,
    DEPARTMENT         VARCHAR2(255),
    DEPARTMENT_LEAVER  VARCHAR2(255),
    CURR_NOS           NUMBER(6),
    PREV_NOS           NUMBER(6),
    CURR_JGROSS        NUMBER(20, 2),
    CURR_LGROSS        NUMBER(20, 2),
    PREV_GROSS         NUMBER(20, 2),
    CURR_GROSS         NUMBER(20, 2),
    CURR_TRPT_DOCTOR   NUMBER(20, 2),
    CURR_TRPT_NURSES   NUMBER(20, 2),
    CURR_SPECIAL_ALLOW NUMBER(20, 2),
    CURR_ON_CALL_DOC   NUMBER(20, 2),
    CURR_BRADFORD      NUMBER(20, 2),
    CURR_OTHERS        NUMBER(20, 2),
    
    PREV_TRPT_DOCTOR   NUMBER(20, 2),
    PREV_TRPT_NURSES   NUMBER(20, 2),
    PREV_SPECIAL_ALLOW NUMBER(20, 2),
    PREV_ON_CALL_DOC   NUMBER(20, 2),
    PREV_BRADFORD      NUMBER(20, 2),
    PREV_OTHERS        NUMBER(20, 2),
    CURR_SHIFT_ALLOW   NUMBER(20, 2),
    CURR_OVERTIME      NUMBER(20, 2),
    CURR_ARREAR        NUMBER(20, 2),
    PREV_SHIFT_ALLOW   NUMBER(20, 2),
    PREV_OVERTIME      NUMBER(20, 2),
    PREV_ARREAR        NUMBER(20, 2));

  ------
  TYPE SAL_RECON_TAB IS TABLE OF SAL_RECON_REC;
  FUNCTION SALARY_RECONCILIATION(P_PREV_START      DATE,
                                 P_PREV_END        DATE,
                                 P_CURR_START      DATE,
                                 P_CURR_END        DATE,
                                 P_LOCATION_ID     VARCHAR2,
                                 P_ORGANIZATION_ID VARCHAR2)
    RETURN SAL_RECON_TAB
    PIPELINED;
  FUNCTION EMP_GROSS(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE)
    RETURN NUMBER;
  FUNCTION JGROSS(P_MRNO       CHAR,
                  P_START_DATE DATE,
                  P_END_DATE   DATE,
                  P_PREV_START DATE,
                  P_PREV_END   DATE) RETURN NUMBER;
  FUNCTION LGROSS(P_MRNO       CHAR,
                  P_START_DATE DATE,
                  P_END_DATE   DATE,
                  P_PREV_START DATE,
                  P_PREV_END   DATE) RETURN NUMBER;

  FUNCTION EMP_ALLOW(P_AD_CODE    CHAR,
                     P_MRNO       CHAR,
                     P_START_DATE DATE,
                     P_END_DATE   DATE) RETURN NUMBER;
  FUNCTION NSHIFT(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE)
    RETURN NUMBER;
  FUNCTION OVERTIME(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE)
    RETURN NUMBER;
  FUNCTION ARREAR(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE)
    RETURN NUMBER;
  FUNCTION EMPLOYEENO(P_MRNO VARCHAR2, P_START_DATE DATE, P_END_DATE DATE)
    RETURN NUMBER;
  FUNCTION DEPARTMENT(P_MRNO VARCHAR2, P_START_DATE DATE, P_END_DATE DATE)
    RETURN VARCHAR2;
  FUNCTION DEPARTMENT_LEAVER(P_MRNO       VARCHAR2,
                             P_START_DATE DATE,
                             P_END_DATE   DATE) RETURN VARCHAR2;

  FUNCTION DESIGNATION(P_MRNO VARCHAR2) RETURN VARCHAR2;
  FUNCTION DEPT_JOINER(P_DEPT            VARCHAR2,
                       P_PREV_START      DATE,
                       P_PREV_END        DATE,
                       P_START_DATE      DATE,
                       P_END_DATE        DATE,
                       P_LOCATION_ID     VARCHAR2,
                       P_ORGANIZATION_ID VARCHAR2) RETURN NUMBER;
  /***********************************************************************************************/
  FUNCTION DEPT_LEAVER(P_DEPT            VARCHAR2,
                       P_PREV_START      DATE,
                       P_PREV_END        DATE,
                       P_START_DATE      DATE,
                       P_END_DATE        DATE,
                       P_LOCATION_ID     VARCHAR2,
                       P_ORGANIZATION_ID VARCHAR2) RETURN NUMBER;
  /************************************************************************************************/
  PROCEDURE P_GET_PAYROLL_MONTH(P_FROM_DATE  IN DATE,
                                P_TO_DATE    IN DATE,
                                P_EVENT      IN CHAR,
                                P_START_DATE OUT DATE,
                                P_END_DATE   OUT DATE,
                                P_STOP       OUT CHAR,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  PROCEDURE P_SALARY_RECONCILIATION_INSERT(P_CURRENT_START_DATE IN DATE,
                                           P_PRE_START_DATE     IN DATE,
                                           P_MRNO               IN VARCHAR2);
  /**********************************************************************************/
  PROCEDURE P_SALARY_RECONCILIATION(P_FROM_DATE  IN DATE,
                                    P_TO_DATE    IN DATE,
                                    P_STOP       OUT CHAR,
                                    P_ALERT_TEXT OUT VARCHAR2);
  /**********************************************************************************/
END PKG_SALARY_RECONCILIATION;
```

#### PAYROLL.PKG_SALARY_SLIP_EMPLOYEE
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_SALARY_SLIP_EMPLOYEE AS

  FUNCTION GET_TAXABLE_INCOME(P_MRNO IN VARCHAR2, P_START_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_TAX_SLAB(P_MRNO IN VARCHAR2, P_START_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_TAX_CHARGEABLE(P_MRNO IN VARCHAR2, P_START_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_TAX_CREDIT_ADJ(P_ORGANIZATION_ID   IN VARCHAR2,
                              P_LOGIN_LOCATION_ID IN VARCHAR2,
                              P_MRNO              IN VARCHAR2,
                              P_START_DATE        IN DATE,
                              P_YEARLY_TAX        IN VARCHAR2) RETURN NUMBER;

  FUNCTION GET_TAX_DEDUCTED(P_MRNO IN VARCHAR2, P_START_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_TAX_PAYABLE(P_ORGANIZATION_ID   IN VARCHAR2,
                           P_LOGIN_LOCATION_ID IN VARCHAR2,
                           P_MRNO              IN VARCHAR2,
                           P_START_DATE        IN DATE,
                           P_YEARLY_TAX        IN VARCHAR2) RETURN NUMBER;

 FUNCTION GET_EMPLOYEE_CONTRIBUTION_OP(P_MRNO     IN VARCHAR2,
                                     P_END_DATE IN DATE) RETURN NUMBER;
                                     
  FUNCTION GET_EMPLOYEE_CONTRIBUTION(P_MRNO     IN VARCHAR2,
                                     P_END_DATE IN DATE) RETURN NUMBER;
                                     
  FUNCTION GET_EMPLOYER_CONTRIBUTION_OP(P_MRNO     IN VARCHAR2,
                                     P_END_DATE IN DATE) RETURN NUMBER;
                                     
  FUNCTION GET_EMPLOYER_CONTRIBUTION(P_MRNO     IN VARCHAR2,
                                     P_END_DATE IN DATE) RETURN NUMBER;

  FUNCTION GET_EMPLOYEE_PROFIT(P_MRNO IN VARCHAR2, P_END_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_SKMT_PROFIT(P_MRNO IN VARCHAR2, P_END_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_PERMANENT_WITHDRAWAL(P_MRNO IN VARCHAR2, P_END_DATE IN DATE)
    RETURN NUMBER;

  FUNCTION GET_TOTAL_PROVIDENT_FUND(P_MRNO IN VARCHAR2, P_END_DATE IN DATE)
    RETURN NUMBER;
    
   FUNCTION GET_CURRENT_MONTH_PF(P_MRNO IN VARCHAR2, P_END_DATE IN DATE)
    RETURN NUMBER;  
    
END PKG_SALARY_SLIP_EMPLOYEE;
```

#### PAYROLL.PKG_YEAR_CLOSING
```sql
CREATE OR REPLACE PACKAGE PAYROLL.PKG_YEAR_CLOSING AS

  /***********************************************************************************************
  OBJECTIVE := This package will be used for the following purpose
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date          Author                 Description
           ---------  -----------   -------------------    -----------------------------------
           1.0        07-MAY-2018    Farhan Akram            Created this Package.
    ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  ----------------------------------------------
  -- This PROCEDURE will process year closing --
  ----------------------------------------------
  PROCEDURE PROCESS_PF_YEAR_CLOSING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_FILE_NO           IN FINANCE.GL_COA_FILES.COA_FILE_NO%TYPE,
                                    P_OPENING_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                    P_CLOSING_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE,
                                    P_USER_MRNO         IN VARCHAR2,
                                    P_TERMINAL          IN VARCHAR2,
                                    P_OBJECT_CODE       IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
END PKG_YEAR_CLOSING;
```

#### PAYROLL.SALARY_DASHBOARD
```sql
create or replace package payroll.SALARY_DASHBOARD is

  -- Author  : MUDASSARMEHMOOD
  -- Created : 21-Aug-26 4:17:16 PM
  -- Purpose : This package will be used to maintain the procedure related to salary dashboard
  TYPE t_month_arr IS TABLE OF NUMBER INDEX BY PLS_INTEGER; -- key = fiscal month 1..12
  TYPE t_matrix IS TABLE OF t_month_arr INDEX BY PLS_INTEGER; -- key = SR_NO
  TYPE t_ad_amt IS TABLE OF t_month_arr INDEX BY VARCHAR2(80); -- key = AD_CODE||'|'||PAYMENT_SOURCE
  PROCEDURE BUILD_SALARY_TAX_MATRIX(p_mrno       IN VARCHAR2,
                                    p_tax_year   IN NUMBER,
                                    p_alert_text out varchar2,
                                    p_stop       out char);



/*************************/
PROCEDURE PRC_LOAD_SALARY_TAX_LINE_ITEM
(
   p_alert_text OUT VARCHAR2,
   p_stop       OUT VARCHAR2
);
end SALARY_DASHBOARD;
```

### Standalone procedures and functions (headers)

#### PAYROLL.CALC_GM (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.CALC_GM(P_MRNO VARCHAR2) RETURN NUMBER IS
```

#### PAYROLL.CURRENT_BASIC (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.CURRENT_BASIC
 (P_MRNO VARCHAR2, P_DATE DATE)
 RETURN NUMBER AUTHID CURRENT_USER IS
```

#### PAYROLL.CURRENT_GROSS (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.CURRENT_GROSS
 (P_MRNO VARCHAR2, P_DATE DATE)
 RETURN NUMBER AUTHID CURRENT_USER IS
```

#### PAYROLL.ERROR_HANDLING (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.ERROR_HANDLING(P_ERROR IN APEX_ERROR.T_ERROR)
  RETURN APEX_ERROR.T_ERROR_RESULT IS
```

#### PAYROLL.F_EMPLOYEE_GROSS (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.F_EMPLOYEE_GROSS(P_MRNO CHAR)
  RETURN NUMBER AUTHID CURRENT_USER IS
```

#### PAYROLL.F_GET_CAR_ALLOWANCE_MONTH (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.F_GET_CAR_ALLOWANCE_MONTH
(
    P_MRNO       IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE,
    P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE
)
RETURN NUMBER
IS
```

#### PAYROLL.F_GET_CAR_ALLOWANCE_YEAR (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.F_GET_CAR_ALLOWANCE_YEAR
(
    P_MRNO       IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE,
    P_START_YEAR_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE,
    P_END_YEAR_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.END_DATE%TYPE
)
RETURN NUMBER
IS
```

#### PAYROLL.F_GET_EMP_OTHER_TAXABLE_AMOUNT (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.F_GET_EMP_OTHER_TAXABLE_AMOUNT(P_MRNO                   IN VARCHAR2,
                                                                  P_YEAR                   IN VARCHAR2,
                                                                  P_TAXABLE_AMOUNT_TYPE_ID IN VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.F_GET_URL (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.f_get_url(p_value IN VARCHAR2)
  RETURN VARCHAR2 IS
```

#### PAYROLL.GET_EXPENSE_DESC (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.GET_EXPENSE_DESC(P_EXPENSE_CODE IN VARCHAR2,
                                                    P_LEVEL        IN VARCHAR2,
                                                    P_ALERT_TEXT   OUT VARCHAR2) RETURN VARCHAR2 AS
```

#### PAYROLL.LFA_ADJUSTMENT_AMOUNT (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_ADJUSTMENT_AMOUNT(P_MRNO         VARCHAR2,
                                                         P_LFA_DUE_DATE DATE)
  RETURN NUMBER IS
```

#### PAYROLL.LFA_AMOUNT (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.LFA_AMOUNT(P_MRNO              IN CHAR,
                                               P_LFA_DUE_DATE      IN DATE,
                                               P_GROSS             OUT NUMBER,
                                               P_BASIC             OUT NUMBER,
                                               P_LFA_AMOUNT        OUT NUMBER,
                                               P_PREV_YEAR_START   OUT DATE,
                                               P_PREV_YEAR_END     OUT DATE,
                                               P_PREV_LEAVE_START  OUT DATE,
                                               P_PREV_LEAVE_END    OUT DATE,
                                               P_PREV_VOUCHER_TYPE OUT CHAR,
                                               P_PREV_VOUCHER_NO   OUT CHAR,
                                               P_PREV_GROSS        OUT NUMBER,
                                               P_PREV_BASIC        OUT NUMBER,
                                               P_PREV_LFA_AMOUNT   OUT NUMBER,
                                               P_PREV_TRANS_DATE   OUT DATE)
  AUTHID CURRENT_USER IS
```

#### PAYROLL.LFA_AMOUNT_FUN (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_AMOUNT_FUN(P_MRNO         CHAR,
                                                  P_LFA_DUE_DATE DATE)
  RETURN NUMBER IS
```

#### PAYROLL.LFA_AMOUNT_YEAR (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_AMOUNT_YEAR(P_MRNO      CHAR,
                                                   P_YEAR_CODE NUMBER)
  RETURN NUMBER IS
```

#### PAYROLL.LFA_PAID_AMOUNT_GL (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_PAID_AMOUNT_GL(P_MRNO      IN CHAR,
                                                      P_FROM_DATE IN DATE,
                                                      P_TO_DATE   IN DATE)
  RETURN NUMBER IS
```

#### PAYROLL.LFA_PAID_AMOUNT_SALARY (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_PAID_AMOUNT_SALARY(P_MRNO      IN CHAR,
                                                          P_FROM_DATE IN DATE,
                                                          P_TO_DATE   IN DATE)
  RETURN NUMBER IS
```

#### PAYROLL.LFA_PAID_AMOUNT (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LFA_PAID_AMOUNT(P_MRNO      IN CHAR,
                                                   P_FROM_DATE IN DATE,
                                                   P_TO_DATE   IN DATE)
  RETURN NUMBER IS
```

#### PAYROLL.LSB_AMOUNT (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.LSB_AMOUNT(P_MRNO         VARCHAR2,
                                              P_EXPENSE_CODE NUMBER)
  RETURN NUMBER IS
```

#### PAYROLL.NEXT_MONTH_TAX (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.NEXT_MONTH_TAX(P_YEAR_CODE NUMBER,
                                                  P_MRNO      VARCHAR2,
                                                  P_YEAR_TAX  NUMBER)
  RETURN NUMBER IS
```

#### PAYROLL.PF_CALCULATION (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.PF_CALCULATION(P_GROSS_SALARY IN CHAR)
  RETURN NUMBER AS
```

#### PAYROLL.TAXABLE_PAY (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.TAXABLE_PAY
 (P_YEAR_CODE NUMBER, P_MRNO VARCHAR2)
 RETURN NUMBER IS
```

#### PAYROLL.SETUP_TAX_CALCULATION (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.SETUP_TAX_CALCULATION(P_YEAR_CODE NUMBER, P_MRNO CHAR) RETURN NUMBER IS
```

#### PAYROLL.TAX_CALCULATION (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.TAX_CALCULATION(P_YEAR_CODE NUMBER, P_AMOUNT NUMBER, P_GENDER CHAR) RETURN NUMBER IS
```

#### PAYROLL.TAX_DIRECT_PAID_EXP (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.TAX_DIRECT_PAID_EXP(P_YEAR_CODE NUMBER,
                                                       P_FROM_DATE DATE,
                                                       P_TO_DATE   DATE,
                                                       P_MRNO      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.TAX_SLAB (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.TAX_SLAB
 (P_YEAR_CODE NUMBER, P_AMOUNT NUMBER, P_GENDER CHAR) RETURN NUMBER IS
```

#### PAYROLL.YEARLY_TAXABLE_PF (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.yearly_taxable_pf(p_year_code NUMBER,
                                                     p_mrno      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.YEARLY_PF_EXEMPTION (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.yearly_pf_exemption(p_year_code NUMBER,
                                                       p_mrno      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.YEARLY_TAXABLE_PAY (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.YEARLY_TAXABLE_PAY(P_YEAR_CODE NUMBER,
                                                      P_MRNO      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.YEARLY_TAXABLE_PF_TEST (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.yearly_taxable_pf_test(p_year_code NUMBER,
                                                          p_mrno      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.YEARLY_TAXABLE_PAY_TEST (function)
```sql
CREATE OR REPLACE FUNCTION PAYROLL.YEARLY_TAXABLE_PAY_TEST(P_YEAR_CODE NUMBER,
                                                           P_MRNO      VARCHAR2)
  RETURN NUMBER IS
```

#### PAYROLL.ACTIVATE (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.ACTIVATE(
    P_REQUEST_ID    IN PAYROLL.CONNECTION_REQUEST.REQUEST_ID%TYPE,
    P_ISSUE_TO      OUT VARCHAR2,
    P_ISSUE_DATE    OUT DATE,
    P_STOP          OUT VARCHAR2,
    P_ALERT_TEXT    OUT VARCHAR2
) AS
```

#### PAYROLL.ANNUAL_ITAX (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.ANNUAL_ITAX(P_FROM_DATE DATE,
                                                P_TO_DATE   DATE,
                                                P_USERID    CHAR,
                                                P_TERMINAL  CHAR) IS
```

#### PAYROLL.BUILD_SALARY_TAX_MATRIX (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.BUILD_SALARY_TAX_MATRIX(p_mrno       IN VARCHAR2,
                                                            p_tax_year   IN NUMBER,
                                                            p_alert_text out varchar2,
                                                            p_stop       out char) IS
```

#### PAYROLL.CM_ACTIVATE (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.CM_ACTIVATE(
    P_REQUEST_ID    IN PAYROLL.CONNECTION_REQUEST.REQUEST_ID%TYPE,
    P_ISSUE_TO      OUT VARCHAR2,
    P_ISSUE_DATE    OUT DATE,
    P_STOP          OUT VARCHAR2,
    P_ALERT_TEXT    OUT VARCHAR2
) AS
```

#### PAYROLL.COST_TO_COMPANY_JOB (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.COST_TO_COMPANY_JOB AS
```

#### PAYROLL.DBJOB (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.dbjob AS
```

#### PAYROLL.DELETE_AD_END_DATE (procedure)
```sql
create or replace procedure payroll.DELETE_AD_END_DATE is
```

#### PAYROLL.EMERGENCY (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.EMERGENCY IS
```

#### PAYROLL.EMP_AD_UPDATION (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.EMP_AD_UPDATION(P_MRNO           VARCHAR2,
                                                    P_INC_DATE       DATE,
                                                    P_CURRENT_BASIC  NUMBER,
                                                    P_CURRENT_GROSS  NUMBER,
                                                    P_PREVIOUS_GROSS NUMBER,
                                                    P_PREVIOUS_BASIC NUMBER,
                                                    P_STOP OUT CHAR,
                                                    P_ALERT_TEXT OUT VARCHAR2) AS
```

#### PAYROLL.EMP_INCREMENT_MASTER_UPDATION (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.EMP_INCREMENT_MASTER_UPDATION(P_MRNO           VARCHAR2,
                                                                  P_INC_DATE       DATE,
                                                                  P_EFFECTIVE_DATE DATE,
                                                                  P_PROPOSAL_NO    NUMBER,
                                                                  P_YEAR_CODE      VARCHAR2,
                                                                  P_INCREMENT_CODE VARCHAR2,
                                                                  P_STOP           OUT CHAR,
                                                                  P_ALERT_TEXT     OUT VARCHAR2) AS
```

#### PAYROLL.GL_RECONCILE_LOAN (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.GL_RECONCILE_LOAN IS
```

#### PAYROLL.INACTIVATE (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.INACTIVATE(
    P_CONNECTION_ID IN PAYROLL.DEF_CONNECTION.CONNECTION_ID%TYPE,
    P_STOP          OUT VARCHAR2,
    P_ALERT_TEXT    OUT VARCHAR2
) AS
```

#### PAYROLL.INDIVIDUAL_ITAX (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.INDIVIDUAL_ITAX(P_MRNO      CHAR,
                                                    P_YEAR_CODE CHAR,
                                                    P_USER      CHAR,
                                                    P_TERMINAL  CHAR) IS
```

#### PAYROLL.LFA_DETAIL (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.lfa_detail(p_mrno         IN CHAR,
                                               p_lfa_due_date IN DATE,
                                               p_payment_date OUT DATE,
                                               p_gross        OUT NUMBER,
                                               p_basic        OUT NUMBER,
                                               p_lfa_amount   OUT NUMBER) IS
```

#### PAYROLL.MPA_REPORTS (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.MPA_REPORTS(P_START_DATE0 IN DATE,
                                                P_END_DATE0   IN DATE,
                                                P_START_DATE1 IN DATE,
                                                P_END_DATE1   IN DATE,
                                                P_START_DATE2 IN DATE,
                                                P_END_DATE2   IN DATE,
                                                P_START_DATE3 IN DATE,
                                                P_END_DATE3   IN DATE,
                                                P_USER_ID     IN CHAR,
                                                P_TERMINAL    IN CHAR) IS
```

#### PAYROLL.MPA_REPORTS_2MONTHS (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.MPA_REPORTS_2MONTHS(P_START_DATE2 IN DATE,
                                                        P_END_DATE2   IN DATE,
                                                        P_START_DATE3 IN DATE,
                                                        P_END_DATE3   IN DATE,
                                                        P_USER_ID     IN CHAR,
                                                        P_TERMINAL    IN CHAR) IS
```

#### PAYROLL.NEXT_MONTH_TAX_DETAIL (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.NEXT_MONTH_TAX_DETAIL(P_YEAR_CODE      IN NUMBER,
                                                          P_MRNO           IN VARCHAR2,
                                                          P_YEAR_TAX       IN NUMBER,
                                                          P_NEXT_MONTH_TAX OUT NUMBER,
                                                          P_PAID_TAX       OUT NUMBER) IS
```

#### PAYROLL.PROC_PAYROLL_JOB (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.PROC_PAYROLL_JOB AS
```

#### PAYROLL.SALARY_SHEET (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.salary_sheet(p_start_date      DATE,
                                                 p_end_date        DATE,
                                                 p_user            CHAR,
                                                 p_terminal        CHAR,
                                                 p_location_id     varchar2,
                                                 p_organization_id varchar2) IS
```

#### PAYROLL.SALARY_SHEET_OLD (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.SALARY_SHEET_OLD(p_start_date DATE,p_end_date DATE,
  p_user CHAR,p_terminal CHAR) IS
```

#### PAYROLL.SALARY_SHEET_TEST (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.SALARY_SHEET_TEST(P_START_DATE      DATE,
                                                      P_END_DATE        DATE,
                                                      P_USER            CHAR,
                                                      P_TERMINAL        CHAR,
                                                      P_ORGANIZATION_ID VARCHAR2,
                                                      P_LOCATION_ID     VARCHAR2) IS
```

#### PAYROLL.SALARY_WISE_GRADE_CHANGE (procedure)
```sql
CREATE OR REPLACE PROCEDURE PAYROLL.SALARY_WISE_GRADE_CHANGE IS
```



# PART: Synonyms

| Synonym | Target |
|---|---|
| SYN_ALLOWANCE_DEDUCTION_DETAIL | PAYROLLAUDIT.ALLOWANCE_DEDUCTION_DETAIL |
| SYN_ARREAR_DETAIL | PAYROLLAUDIT.ARREAR_DETAIL |
| SYN_ARREAR_EXCEPTIONAL | PAYROLLAUDIT.ARREAR_EXCEPTIONAL |
| SYN_CM_BILL_DETAIL | PAYROLLAUDIT.CM_BILL_DETAIL |
| SYN_CM_BILL_MASTER | PAYROLLAUDIT.CM_BILL_MASTER |
| SYN_CM_CONNECTION_REQUEST | PAYROLLAUDIT.CM_CONNECTION_REQUEST |
| SYN_CM_CONNECTION_REQ_DOCUMENT | PAYROLLAUDIT.CM_CONNECTION_REQ_DOCUMENT |
| SYN_CM_CONNECTION_TRANSACTIONS | PAYROLLAUDIT.CM_CONNECTION_TRANSACTIONS |
| SYN_CM_DEF_ADMIN_GROUP | PAYROLLAUDIT.CM_DEF_ADMIN_GROUP |
| SYN_CM_DEF_ADMIN_GROUP_DTL | PAYROLLAUDIT.CM_DEF_ADMIN_GROUP_DTL |
| SYN_CM_DEF_CONNECTION | PAYROLLAUDIT.CM_DEF_CONNECTION |
| SYN_CM_INVOICES | PAYROLLAUDIT.CM_INVOICES |
| SYN_DEF_AD_CHART | PAYROLLAUDIT.DEF_AD_CHART |
| SYN_DEF_AD_CHART_DETAIL | PAYROLLAUDIT.DEF_AD_CHART_DETAIL |
| SYN_DEF_AD_CONSTANT | PAYROLLAUDIT.DEF_AD_CONSTANT |
| SYN_DEF_AD_GROUP | PAYROLLAUDIT.DEF_AD_GROUP |
| SYN_DEF_AD_NATURE_TYPE | PAYROLLAUDIT.DEF_AD_NATURE_TYPE |
| SYN_DEF_AD_SETUP | PAYROLLAUDIT.DEF_AD_SETUP |
| SYN_DEF_AD_SETUP_DC | PAYROLLAUDIT.DEF_AD_SETUP_DC |
| SYN_DEF_AD_SETUP_PT | PAYROLLAUDIT.DEF_AD_SETUP_PT |
| SYN_DEF_AD_SETUP_UNPAID_LT | PAYROLLAUDIT.DEF_AD_SETUP_UNPAID_LT |
| SYN_DEF_ALLOWANCE_DEDUCTION | PAYROLLAUDIT.DEF_ALLOWANCE_DEDUCTION |
| SYN_DEF_ARREAR | PAYROLLAUDIT.DEF_ARREAR |
| SYN_DEF_EMP_FINANCIAL | PAYROLLAUDIT.DEF_EMP_FINANCIAL |
| SYN_DEF_EMP_JOB | PAYROLLAUDIT.DEF_EMP_JOB |
| SYN_DEF_EXPENSE | PAYROLLAUDIT.DEF_EXPENSE |
| SYN_DEF_EXPENSE_CONSTANT | PAYROLLAUDIT.DEF_EXPENSE_CONSTANT |
| SYN_DEF_EXPENSE_DETAIL | PAYROLLAUDIT.DEF_EXPENSE_DETAIL |
| SYN_DEF_EXPENSE_DETAIL_SLAB | PAYROLLAUDIT.DEF_EXPENSE_DETAIL_SLAB |
| SYN_DEF_FINANCIAL_SETUP | PAYROLLAUDIT.DEF_FINANCIAL_SETUP |
| SYN_DEF_FS_ELEMENT | PAYROLLAUDIT.DEF_FS_ELEMENT |
| SYN_DEF_FS_ELEMENTS | PAYROLLAUDIT.DEF_FS_ELEMENTS |
| SYN_DEF_GL_SETUP_DETAIL | PAYROLLAUDIT.DEF_GL_SETUP_DETAIL |
| SYN_DEF_GL_SETUP_DETAIL_FS | PAYROLLAUDIT.DEF_GL_SETUP_DETAIL_FS |
| SYN_DEF_GL_SETUP_MASTER | PAYROLLAUDIT.DEF_GL_SETUP_MASTER |
| SYN_DEF_GL_VOUCHER | PAYROLLAUDIT.DEF_GL_VOUCHER |
| SYN_DEF_GRADE_WISE_PERCENTAGE | PAYROLLAUDIT.DEF_GRADE_WISE_PERCENTAGE |
| SYN_DEF_INCOME_TAX | PAYROLLAUDIT.DEF_INCOME_TAX |
| SYN_DEF_INCREMENT_TYPE | PAYROLLAUDIT.DEF_INCREMENT_TYPE |
| SYN_DEF_LETTER_TYPE | PAYROLLAUDIT.DEF_LETTER_TYPE |
| SYN_DEF_LIABILITY | PAYROLLAUDIT.DEF_LIABILITY |
| SYN_DEF_LOAN_INTEREST_RATE | PAYROLLAUDIT.DEF_LOAN_INTEREST_RATE |
| SYN_DEF_LOAN_TYPE | PAYROLLAUDIT.DEF_LOAN_TYPE |
| SYN_DEF_LOAN_TYPE_CONSTANT | PAYROLLAUDIT.DEF_LOAN_TYPE_CONSTANT |
| SYN_DEF_MONTH_CHANGE | PAYROLLAUDIT.DEF_MONTH_CHANGE |
| SYN_DEF_PAYROLL_LOCATION | PAYROLLAUDIT.DEF_PAYROLL_LOCATION |
| SYN_DEF_PAYROLL_WORKFLOW | PAYROLLAUDIT.DEF_PAYROLL_WORKFLOW |
| SYN_DEF_PAYSCALE | PAYROLLAUDIT.DEF_PAYSCALE |
| SYN_DEF_PAYSCALE_DETAIL | PAYROLLAUDIT.DEF_PAYSCALE_DETAIL |
| SYN_DEF_PAY_VOUCHER_LOCATION | PAYROLLAUDIT.DEF_PAY_VOUCHER_LOCATION |
| SYN_DEF_PAY_VOUCHER_SETUP | PAYROLLAUDIT.DEF_PAY_VOUCHER_SETUP |
| SYN_DEF_PAY_VOUCHER_SETUP_DTL | PAYROLLAUDIT.DEF_PAY_VOUCHER_SETUP_DTL |
| SYN_DEF_PAY_VOUCHER_TYPE | PAYROLLAUDIT.DEF_PAY_VOUCHER_TYPE |
| SYN_DEF_PERCENTAGE_SETUP | PAYROLLAUDIT.DEF_PERCENTAGE_SETUP |
| SYN_DEF_PF_SETUP | PAYROLLAUDIT.DEF_PF_SETUP |
| SYN_DEF_PROJECT | PAYROLLAUDIT.DEF_PROJECT |
| SYN_DEF_SETUP | PAYROLLAUDIT.DEF_SETUP |
| SYN_DEF_SETUP_CONSTANT | PAYROLLAUDIT.DEF_SETUP_CONSTANT |
| SYN_DEF_TAX_AMNT_OTH_THAN_SAL | PAYROLLAUDIT.DEF_TAX_AMOUNT_OTHER_THAN_SAL |
| SYN_EMP_ALLOWANCE_DEDUCTION | PAYROLLAUDIT.EMP_ALLOWANCE_DEDUCTION |
| SYN_EMP_ALLO_DED_DET | PAYROLLAUDIT.EMP_ALLOWANCE_DEDUCTION_DETAIL |
| SYN_EMP_AWARDS | PAYROLLAUDIT.EMP_AWARDS |
| SYN_EMP_AWARD_PAYMENT | PAYROLLAUDIT.EMP_AWARD_PAYMENT |
| SYN_EMP_EXPENSE | PAYROLLAUDIT.EMP_EXPENSE |
| SYN_EMP_EXP_DET_PROJECT | PAYROLLAUDIT.EMP_EXP_DET_PROJECT |
| SYN_EMP_INCREMENT_DETAIL | PAYROLLAUDIT.EMP_INCREMENT_DETAIL |
| SYN_EMP_INCREMENT_MASTER | PAYROLLAUDIT.EMP_INCREMENT_MASTER |
| SYN_EMP_ITAX_ADJUSTMENT | PAYROLLAUDIT.EMP_ITAX_ADJUSTMENT |
| SYN_EMP_ITAX_ADJUSTMENT_DTL_M | PAYROLLAUDIT.EMP_ITAX_ADJUSTMENT_DTL_M |
| SYN_EMP_ITAX_ADJ_MONTHLY | PAYROLLAUDIT.EMP_ITAX_ADJ_MONTHLY |
| SYN_EMP_LIABILITY | PAYROLLAUDIT.EMP_LIABILITY |
| SYN_EMP_PAYMENT | PAYROLLAUDIT.EMP_PAYMENT |
| SYN_EMP_TAX_AMNT_OTHER_SAL | PAYROLLAUDIT.EMP_TAX_AMOUNT_OTHER_THAN_SAL |
| SYN_EXPENSE_CLAIM_DETAIL | PAYROLLAUDIT.EXPENSE_CLAIM_DETAIL |
| SYN_EXPENSE_CLAIM_MASTER | PAYROLLAUDIT.EXPENSE_CLAIM_MASTER |
| SYN_EXPENSE_CLAIM_PROJECT | PAYROLLAUDIT.EXPENSE_CLAIM_PROJECT |
| SYN_FINAL_SETTLEMENT | PAYROLLAUDIT.FINAL_SETTLEMENT |
| SYN_FINAL_SETTLEMENT_ELEMENT | PAYROLLAUDIT.FINAL_SETTLEMENT_ELEMENT |
| SYN_GENERIC_REPORT_FIELD | PAYROLLAUDIT.GENERIC_REPORT_FIELD |
| SYN_GENERIC_REPORT_MASTER | PAYROLLAUDIT.GENERIC_REPORT_MASTER |
| SYN_HOLD_ORDER | PAYROLLAUDIT.HOLD_ORDER |
| SYN_ITAX_PAYMENT_DETAIL | PAYROLLAUDIT.ITAX_PAYMENT_DETAIL |
| SYN_ITAX_PAYMENT_MASTER | PAYROLLAUDIT.ITAX_PAYMENT_MASTER |
| SYN_LOAN_PAYMENT_INTEREST | PAYROLLAUDIT.LOAN_PAYMENT_INTEREST |
| SYN_LOAN_PAYMENT_MASTER | PAYROLLAUDIT.LOAN_PAYMENT_MASTER |
| SYN_LOAN_PAYMENT_MASTER_N | PAYROLLAUDIT.LOAN_PAYMENT_MASTER_N |
| SYN_LOAN_REFUND_DETAIL | PAYROLLAUDIT.LOAN_REFUND_DETAIL |
| SYN_LOAN_REFUND_DETAIL_N | PAYROLLAUDIT.LOAN_REFUND_DETAIL_N |
| SYN_LOAN_REFUND_MASTER | PAYROLLAUDIT.LOAN_REFUND_MASTER |
| SYN_LOAN_REFUND_MASTER_N | PAYROLLAUDIT.LOAN_REFUND_MASTER_N |
| SYN_LOAN_REFUND_OPENING | PAYROLLAUDIT.LOAN_REFUND_OPENING |
| SYN_MONTH_CHANGE_APPROVAL | PAYROLLAUDIT.MONTH_CHANGE_APPROVAL |
| SYN_MONTH_CHANGE_REQUEST | PAYROLLAUDIT.MONTH_CHANGE_REQUEST |
| SYN_PAY_AD_BALANCE | PAYROLLAUDIT.PAY_AD_BALANCE |
| SYN_PAY_ALLOWANCE_DEDUCTION | PAYROLLAUDIT.PAY_ALLOWANCE_DEDUCTION |
| SYN_PAY_ARREAR | PAYROLLAUDIT.PAY_ARREAR |
| SYN_PAY_DAILY_AD_TEST | PAYROLLAUDIT.PAY_DAILY_AD_TEST |
| SYN_PAY_FINANCIAL_YEAR | PAYROLLAUDIT.PAY_FINANCIAL_YEAR |
| SYN_PAY_ITAX_DETAIL | PAYROLLAUDIT.PAY_ITAX_DETAIL |
| SYN_PAY_ITAX_INCOME_DETAIL | PAYROLLAUDIT.PAY_ITAX_INCOME_DETAIL |
| SYN_PAY_LEAVES | PAYROLLAUDIT.PAY_LEAVES |
| SYN_PAY_MASTER | PAYROLLAUDIT.PAY_MASTER |
| SYN_PAY_MASTER_X | PAYROLLAUDIT.PAY_MASTER_X |
| SYN_PAY_PF_VOUCHER | PAYROLLAUDIT.PAY_PF_VOUCHER |
| SYN_PAY_STATUS | PAYROLLAUDIT.PAY_STATUS |
| SYN_PAY_VOUCHER | PAYROLLAUDIT.PAY_VOUCHER |
| SYN_PAY_VOUCHER_DETAIL | PAYROLLAUDIT.PAY_VOUCHER_DETAIL |
| SYN_PAY_VOUCHER_MASTER | PAYROLLAUDIT.PAY_VOUCHER_MASTER |
| SYN_PF_FINAL_SETTLEMENT | PAYROLLAUDIT.PF_FINAL_SETTLEMENT |
| SYN_PROCESS_INCREMENT_MASTER | PAYROLLAUDIT.PROCESS_INCREMENT_MASTER |
| SYN_PROCESS_MEMBERS | PAYROLLAUDIT.PROCESS_MEMBERS |
| SYN_RPT_SALARY_TAX_LINE_ITEM | PAYROLLAUDIT.RPT_SALARY_TAX_LINE_ITEM |
| SYN_R_COST_TO_COMPANY | PAYROLLAUDIT.R_COST_TO_COMPANY |
| SYN_SYN_EMP_ITAX_ADJ_MON | PAYROLLAUDIT.EMP_ITAX_ADJUSTMENT_MONTHLY |
| SYN_TEMP_INCREMENT_DETAIL | PAYROLLAUDIT.TEMP_INCREMENT_DETAIL |
| SYN_TEMP_INCREMENT_MASTER | PAYROLLAUDIT.TEMP_INCREMENT_MASTER |
| SYN_TRAVEL_ADVANCE_APPROVAL | PAYROLLAUDIT.TRAVEL_ADVANCE_APPROVAL |
