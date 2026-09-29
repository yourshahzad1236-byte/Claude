# PAYROLL schema

_Generated from `PAYROLL_SCHMA.txt` by `tools/parse_schema.py`. Do not edit by hand — re-run the script._

## Summary

| Object type | Count |
|---|---|
| Tables | 183 |
| Views | 5 |
| Sequences | 1 |
| Packages | 78 |
| Procedures | 23 |
| Functions | 29 |
| Triggers | 429 |
| Types | 0 |
| Synonyms | 117 |
| Foreign keys | 136 |

### Cross-schema foreign-key dependencies

- **BILLING**: `BILLING.CORPORATE_INVOICE_MASTER`, `BILLING.DEF_SLAB`
- **DEFINITIONS**: `DEFINITIONS.BANK_BRANCH`, `DEFINITIONS.CURRENCY`, `DEFINITIONS.DESIGNATION_CATEGORY`, `DEFINITIONS.GL_DIV_DEPT_CC`, `DEFINITIONS.LOCATION`, `DEFINITIONS.MONTHS`, `DEFINITIONS.ORGANIZATION`, `DEFINITIONS.PATIENT_TYPE_GROUPS`
- **FINANCE**: `FINANCE.GL_COA`, `FINANCE.GL_SUB_LEDGERS`, `FINANCE.GL_TRAN_MASTER`, `FINANCE.PF_FINANCIAL_YEAR`, `FINANCE.VALUE_SETS`
- **HRD**: `HRD.INFORMATION`, `HRD.LEAVE_TYPE`

## Tables

| Table | Cols | PK | Description |
|---|---|---|---|
| [ACTUAL_PI](#actual_pi) | 19 |  |  |
| [AD_EXCEPTIONAL](#ad_exceptional) | 19 |  |  |
| [DEF_AD_GROUP](#def_ad_group) | 18 | AD_GROUP_CODE |  |
| [DEF_ALLOWANCE_DEDUCTION](#def_allowance_deduction) | 29 | AD_CODE, ORGANIZATION_ID, LOCATION_ID | This table is used to define different types of allowances / deductions which are used in salary processing. It also describes different formulas to calculate allowances and deductions |
| [ALLOWANCE_DEDUCTION_DETAIL](#allowance_deduction_detail) | 24 | START_DATE, END_DATE, AD_CODE, MRNO, TRANS_DATE |  |
| [ALLOWANCE_DEDUCTION_SETUP](#allowance_deduction_setup) | 19 | AD_CODE, FROM_DATE |  |
| [DEF_ARREAR](#def_arrear) | 16 | ARREAR_CODE |  |
| [ARREAR_DETAIL](#arrear_detail) | 25 | START_DATE, END_DATE, ARREAR_CODE, MRNO, AD_CODE |  |
| [ARREAR_EXCEPTIONAL](#arrear_exceptional) | 24 |  |  |
| [BASE_TABLE](#base_table) | 22 |  |  |
| [CBR_DATA_FILE](#cbr_data_file) | 20 |  |  |
| [CHANGE_SALARY_ALLOW](#change_salary_allow) | 19 |  |  |
| [CM_DEF_ADMIN_GROUP](#cm_def_admin_group) | 14 | ADMIN_GROUP_ID |  |
| [CM_BILL_MASTER](#cm_bill_master) | 25 | MONTH_ID, ADMIN_GROUP_ID |  |
| [CM_DEF_CONNECTION](#cm_def_connection) | 18 | CONNECTION_ID |  |
| [CM_CONNECTION_REQUEST](#cm_connection_request) | 31 | REQUEST_ID |  |
| [CM_BILL_DETAIL](#cm_bill_detail) | 26 | ADMIN_GROUP_ID, MONTH_ID, REQUEST_ID |  |
| [CM_CONNECTION_REQ_DOCUMENT](#cm_connection_req_document) | 13 | DOCUMENT_ID |  |
| [CM_CONNECTION_TRANSACTIONS](#cm_connection_transactions) | 16 | TRANS_ID |  |
| [CM_DEF_ADMIN_GROUP_DTL](#cm_def_admin_group_dtl) | 13 | ADMIN_GROUP_ID, ADMIN_MRNO |  |
| [CM_INVOICES](#cm_invoices) | 15 | MONTH_ID, CONTACT_NUMBER |  |
| [DEF_AD_CHART](#def_ad_chart) | 18 | AD_CODE, SRNO |  |
| [DEF_AD_CHART_DETAIL](#def_ad_chart_detail) | 16 | AD_CODE, SRNO, PATIENT_TYPE_GROUP_ID, DESIGNATION_CATEGORY_ID, GRADE_ID |  |
| [DEF_AD_CONSTANT](#def_ad_constant) | 16 | AD_CODE |  |
| [DEF_AD_NATURE_TYPE](#def_ad_nature_type) | 14 | AD_NATURE_TYPE_ID |  |
| [DEF_AD_SETUP](#def_ad_setup) | 29 | ORGANIZATION_ID, LOCATION_ID, AD_CODE | This table is used to location wise define def_allowances_deduction. |
| [DEF_AD_SETUP_DC](#def_ad_setup_dc) | 19 | ORGANIZATION_ID, LOCATION_ID, AD_CODE, DESIGNATION_CATEGORY_ID | This table is used to define designation category wise ad setup. |
| [DEF_AD_SETUP_PT](#def_ad_setup_pt) | 19 | ORGANIZATION_ID, LOCATION_ID, AD_CODE, PATIENT_TYPE_ID | This table is used to define patient type group wise ad setup. |
| [DEF_AD_SETUP_UNPAID_LT](#def_ad_setup_unpaid_lt) | 16 | ORGANIZATION_ID, LOCATION_ID, LEAVE_TYPE_ID, AD_CODE |  |
| [DEF_EMP_JOB](#def_emp_job) | 12 | JOB_CODE | This table is used to define organizational hierarchy of employees |
| [DEF_GL_SETUP_MASTER](#def_gl_setup_master) | 14 | GL_SETUP_CODE | This table is used to define different setups for payroll jornal voucher |
| [DEF_INCOME_TAX](#def_income_tax) | 12 | S_ITAX_CODE | This table is used to define different setups for income tax calculation according to govt. policy |
| [DEF_EMP_FINANCIAL](#def_emp_financial) | 45 | MRNO | This table is used to define financial parameters of empoyee which are used to entertain different financial activities |
| [DEF_EXPENSE](#def_expense) | 28 | EXPENSE_CODE, LOCATION_ID |  |
| [DEF_EXPENSE_CONSTANT](#def_expense_constant) | 17 | EXPENSE_CODE |  |
| [DEF_EXPENSE_DETAIL](#def_expense_detail) | 15 | EXPENSE_TYPE_ID |  |
| [DEF_EXPENSE_DETAIL_SLAB](#def_expense_detail_slab) | 14 | EXPENSE_TYPE_ID, SLAB_ID |  |
| [DEF_EXPENSE_TAXABLE_ACC](#def_expense_taxable_acc) | 14 | EXPENSE_CODE, OBJECT_CODE, VALUE_TYPE |  |
| [DEF_EXPENSE_WORKFLOW](#def_expense_workflow) | 16 | EXPENSE_CODE |  |
| [DEF_FINANCIAL_SETUP](#def_financial_setup) | 51 | FROM_DATE | This table is used to define different formulas and rules applied to Govt. and corporate. It contains only one record. |
| [DEF_FS_ELEMENT](#def_fs_element) | 14 | ELEMENT_CODE |  |
| [DEF_FS_ELEMENT_DETAIL](#def_fs_element_detail) | 12 | ELEMENT_CODE, SR_NO |  |
| [DEF_FS_SALARY_ELEMENTS](#def_fs_salary_elements) | 2 | ELEMENTS |  |
| [DEF_FS_WORKFLOW_Q](#def_fs_workflow_q) | 3 |  |  |
| [DEF_GL_SETUP_DETAIL](#def_gl_setup_detail) | 29 | GL_SETUP_CODE, SERIAL_NO | This table is used to define different setups for automatic payroll jornal voucher |
| [DEF_GL_SETUP_DETAIL_FS](#def_gl_setup_detail_fs) | 15 | GL_SETUP_CODE, ELEMENT_CODE | This table is used to define different setups for automatic payroll final settlement jornal voucher |
| [DEF_GL_VOUCHER](#def_gl_voucher) | 12 | GL_SETUP_CODE | This table is used to define different setups for payroll jornal voucher |
| [DEF_PERCENTAGE_SETUP](#def_percentage_setup) | 15 | PERCENTAGE_SETUP_ID |  |
| [DEF_GRADE_WISE_PERCENTAGE](#def_grade_wise_percentage) | 13 | PERCENTAGE_SETUP_ID, GRADE_ID |  |
| [DEF_INCREMENT_TYPE](#def_increment_type) | 16 | INCREMENT_CODE | This table is used to define different types of increments such as Annual, promotional etc. |
| [DEF_ITAX_ADJUSTMENT](#def_itax_adjustment) | 17 | ADJUSTMENT_CODE |  |
| [PAY_FINANCIAL_YEAR](#pay_financial_year) | 30 | YEAR_CODE |  |
| [DEF_ITAX_DETAIL_AD](#def_itax_detail_ad) | 21 | YEAR_CODE, AD_CODE |  |
| [DEF_ITAX_MR_SLAB](#def_itax_mr_slab) | 14 | YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE |  |
| [DEF_ITAX_SLAB](#def_itax_slab) | 15 | YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE |  |
| [DEF_LETTER_TYPE](#def_letter_type) | 14 | LETTER_CODE | This table is used to define different letter types |
| [DEF_LETTER_TEMPLATE](#def_letter_template) | 9 | TEMPLATE_CODE | This table is used to define different letter templates to be issued to employees such as joining, experience etc. |
| [DEF_LIABILITY](#def_liability) | 14 | LIABILITY_CODE |  |
| [DEF_LOAN_INTEREST_RATE](#def_loan_interest_rate) | 15 | LOAN_CODE, YEAR_CODE, LOCATION_ID, ORGANIZATION_ID |  |
| [DEF_LOAN_TYPE](#def_loan_type) | 38 | LOAN_CODE, ORGANIZATION_ID, LOCATION_ID | This table is used to define different types of loan such as Advance against salary, Car loan, house loan etc. |
| [DEF_LOAN_TYPE_CONSTANT](#def_loan_type_constant) | 14 | LOAN_CODE |  |
| [DEF_MONTH_CHANGE](#def_month_change) | 12 | ID |  |
| [DEF_PAYROLL_LOCATION](#def_payroll_location) | 14 | ORGANIZATION_ID, PAYROLL_LOCATION_ID, EMP_LOCATION_ID |  |
| [DEF_PAYROLL_WORKFLOW](#def_payroll_workflow) | 13 | LOCATION_ID, TYPE |  |
| [DEF_PAYSCALE](#def_payscale) | 18 | YEAR_CODE, GRADE_ID |  |
| [DEF_PAYSCALE_DETAIL](#def_payscale_detail) | 14 | YEAR_CODE, GRADE_ID, STAGE_NO |  |
| [DEF_PAY_VOUCHER_LOCATION](#def_pay_voucher_location) | 14 | PAY_VOUCHER_TYPE, LOCATION_ID, EMP_LOCATION_ID |  |
| [DEF_PAY_VOUCHER_TYPE](#def_pay_voucher_type) | 14 | PAY_VOUCHER_TYPE |  |
| [DEF_PAY_VOUCHER_SETUP](#def_pay_voucher_setup) | 22 | PAY_VOUCHER_SETUP_ID |  |
| [DEF_PAY_VOUCHER_SETUP_DTL](#def_pay_voucher_setup_dtl) | 20 | PAY_VOUCHER_SETUP_ID, SRNO |  |
| [DEF_PF_SETUP](#def_pf_setup) | 24 | COA_CODE_EMPLOYEE_CONT |  |
| [DEF_PROJECT](#def_project) | 17 | PROJECT_ID |  |
| [DEF_SCHEDULE_WORKFLOW_CC](#def_schedule_workflow_cc) | 18 | EXPENSE_CODE, TRANS_TYPE, COST_CENTRE_ID |  |
| [DEF_SETUP_CONSTANT](#def_setup_constant) | 15 | CONSTANT_ID |  |
| [DEF_SETUP](#def_setup) | 16 | CONSTANT_ID, LOCATION_ID, ORGANIZATION_ID |  |
| [DEF_TAX_AMOUNT_OTHER_THAN_SAL](#def_tax_amount_other_than_sal) | 13 | TAXABLE_AMOUNT_ID |  |
| [EMPLOYEE_INCOME_DETAIL](#employee_income_detail) | 9 |  |  |
| [EMPLOYEE_INCOME_DETAIL_FQ](#employee_income_detail_fq) | 9 |  |  |
| [EMP_ALLOWANCE_DEDUCTION](#emp_allowance_deduction) | 18 | AD_CODE, MRNO | This table is used to link employees with different types of allowances and deductions |
| [EMP_ALLOWANCE_DEDUCTION_DETAIL](#emp_allowance_deduction_detail) | 22 | AD_CODE, MRNO, FROM_DATE |  |
| [EMP_AWARDS](#emp_awards) | 22 | AWARD_ID |  |
| [EMP_AWARD_PAYMENT](#emp_award_payment) | 23 | PAYMENT_ID |  |
| [EMP_EXPENSE](#emp_expense) | 42 | DOCUMENT_NO |  |
| [EMP_EXPENSE_LIST](#emp_expense_list) | 19 | EXPENSE_LIST_ID |  |
| [EMP_EXPENSE_LIST_DTL](#emp_expense_list_dtl) | 17 | EXPENSE_LIST_ID, MRNO |  |
| [EMP_EXP_DET_PROJECT](#emp_exp_det_project) | 13 | DOCUMENT_NO, PROJECT_ID |  |
| [EMP_INCREMENT_MASTER](#emp_increment_master) | 26 | MRNO, INCREMENT_DATE |  |
| [EMP_INCREMENT_DETAIL](#emp_increment_detail) | 19 | AD_CODE, MRNO, INCREMENT_DATE |  |
| [EMP_ITAX_ADJUSTMENT](#emp_itax_adjustment) | 18 | YEAR_CODE, MRNO, ADJUSTMENT_CODE |  |
| [EMP_ITAX_ADJUSTMENT_DTL](#emp_itax_adjustment_dtl) | 9 | YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO |  |
| [EMP_ITAX_ADJUSTMENT_DTL_M](#emp_itax_adjustment_dtl_m) | 15 | YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO, START_DATE, END_DATE |  |
| [EMP_ITAX_ADJUSTMENT_MONTHLY](#emp_itax_adjustment_monthly) | 20 | YEAR_CODE, MRNO, ADJUSTMENT_CODE, START_DATE |  |
| [EMP_LIABILITY](#emp_liability) | 16 | LIABILITY_CODE, MRNO |  |
| [EMP_NEW_SAL](#emp_new_sal) | 15 |  |  |
| [EMP_PAYMENT](#emp_payment) | 16 | START_DATE, END_DATE, MRNO |  |
| [EMP_TAX_AMOUNT_OTHER_THAN_SAL](#emp_tax_amount_other_than_sal) | 14 | MRNO, YEAR, TAXABLE_AMOUNT_TYPE_ID |  |
| [EXPENSE_CLAIM_MASTER](#expense_claim_master) | 36 | CLAIM_NO |  |
| [EXPENSE_CLAIM_DETAIL](#expense_claim_detail) | 23 | CLAIM_NO, SRNO |  |
| [EXPENSE_CLAIM_DOCUMENT](#expense_claim_document) | 13 | DOCUMENT_ID |  |
| [EXPENSE_CLAIM_HIERARCHY](#expense_claim_hierarchy) | 8 |  |  |
| [EXPENSE_CLAIM_HIERARCHY_ORG](#expense_claim_hierarchy_org) | 5 |  |  |
| [EXPENSE_CLAIM_PROJECT](#expense_claim_project) | 14 | CLAIM_NO, PROJECT_ID |  |
| [EXPENSE_CLAIM_WORKFLOW](#expense_claim_workflow) | 20 | CLAIM_NO, WFE_NO |  |
| [EXPENSE_CLAIM_WORKFLOW_Q](#expense_claim_workflow_q) | 13 | CLAIM_NO, WFE_NO, ASSIGNEE_MRNO |  |
| [FINAL_SETTLEMENT](#final_settlement) | 28 | FINAL_SETTLEMENT_ID |  |
| [FINAL_SETTLEMENT_ELEMENT](#final_settlement_element) | 14 | FINAL_SETTLEMENT_ID, ELEMENT_CODE |  |
| [FINAL_SETTLEMENT_WF](#final_settlement_wf) | 10 |  |  |
| [FINAL_SETTLEMENT_WF_Q](#final_settlement_wf_q) | 3 |  |  |
| [GENERIC_REPORT_MASTER](#generic_report_master) | 17 | REPORT_ID |  |
| [GENERIC_REPORT_FIELD](#generic_report_field) | 17 | REPORT_ID, FIELD_CODE |  |
| [GENERIC_REPORT_FIELD_DTL](#generic_report_field_dtl) | 16 | REPORT_ID, FIELD_CODE, SRNO |  |
| [HOLD_ORDER](#hold_order) | 18 | HOLD_ORDER_ID |  |
| [ITAX_PAYMENT_DETAIL](#itax_payment_detail) | 20 | YEAR_CODE, ORGANIZATION_ID, LOCATION_ID, START_DATE, END_DATE |  |
| [ITAX_PAYMENT_MASTER](#itax_payment_master) | 20 | ORGANIZATION_ID, LOCATION_ID, YEAR_CODE |  |
| [LEAVE_DAYS_TEST](#leave_days_test) | 7 | MRNO, LEAVE_DATE |  |
| [LOAN_INSTALLMENT_DETAIL](#loan_installment_detail) | 26 | PAY_START_DATE, PAY_END_DATE, MRNO, LOAN_NO |  |
| [LOAN_PAYMENT_INTEREST](#loan_payment_interest) | 22 | LOAN_NO, YEAR_CODE |  |
| [LOAN_PAYMENT_MASTER](#loan_payment_master) | 40 | LOAN_NO | This table is used to entertain opening balances and transactions of staff advances |
| [LOAN_PAYMENT_MASTER_N](#loan_payment_master_n) | 40 | LOAN_NO | This table is used to entertain opening balances and transactions of staff advances |
| [LOAN_PAYMENT_MASTER_TEST](#loan_payment_master_test) | 34 | LOAN_NO |  |
| [LOAN_REFUND_MASTER](#loan_refund_master) | 23 | REFUND_NO | This table is used to entertain transactions of refunds advances or deductions of advances against salary |
| [LOAN_REFUND_DETAIL](#loan_refund_detail) | 19 | LOAN_NO, REFUND_NO | This table is used to entertain transactions of refunds advances or deductions of advances against salary |
| [LOAN_REFUND_MASTER_N](#loan_refund_master_n) | 25 | REFUND_NO | This table is used to entertain transactions of refunds advances or deductions of advances against salary |
| [LOAN_REFUND_DETAIL_N](#loan_refund_detail_n) | 15 | LOAN_NO, REFUND_NO | This table is used to entertain transactions of refunds advances or deductions of advances against salary |
| [LOAN_REFUND_MASTER_TEST](#loan_refund_master_test) | 19 | REFUND_NO |  |
| [LOAN_REFUND_DETAIL_TEST](#loan_refund_detail_test) | 15 | LOAN_NO, REFUND_NO |  |
| [LOAN_REFUND_OPENING](#loan_refund_opening) | 15 | LOAN_NO, SR_NO |  |
| [MANUAL_MONTH_MASTER](#manual_month_master) | 20 | START_DATE, END_DATE, SERIAL_NO |  |
| [MANUAL_PAY_MASTER](#manual_pay_master) | 15 | START_DATE, END_DATE, SERIAL_NO, MRNO |  |
| [MANUAL_ALLOWANCE_DEDUCTION](#manual_allowance_deduction) | 17 | START_DATE, END_DATE, SERIAL_NO, MRNO, AD_CODE |  |
| [MONTH_CHANGE_REQUEST](#month_change_request) | 18 |  |  |
| [MONTH_CHANGE_REQUEST_TEMP](#month_change_request_temp) | 4 |  |  |
| [PAY_AD_BALANCE](#pay_ad_balance) | 18 | MRNO, START_DATE, END_DATE, AD_CODE |  |
| [PAY_AD_BALANCE_TEST](#pay_ad_balance_test) | 8 | MRNO, START_DATE, END_DATE, AD_CODE |  |
| [PAY_MASTER](#pay_master) | 93 | MRNO, START_DATE, END_DATE | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| [PAY_ALLOWANCE_DEDUCTION](#pay_allowance_deduction) | 26 | MRNO, START_DATE, END_DATE, AD_CODE | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| [PAY_MASTER_TEST](#pay_master_test) | 89 | MRNO, START_DATE, END_DATE | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| [PAY_ALLOWANCE_DEDUCTION_TEST](#pay_allowance_deduction_test) | 22 | MRNO, START_DATE, END_DATE, AD_CODE | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| [PAY_ARREAR](#pay_arrear) | 18 | MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE |  |
| [PAY_ARREAR_TEST](#pay_arrear_test) | 8 | MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE |  |
| [PAY_DAILY_AD_TEST](#pay_daily_ad_test) | 16 | MRNO, PAY_START_DATE, PAY_END_DATE, AD_CODE, DAY |  |
| [PAY_DAILY_TEMP](#pay_daily_temp) | 8 | MRNO, AD_CODE, DAY |  |
| [PAY_DAILY_TEMP_UNPAID](#pay_daily_temp_unpaid) | 16 | MRNO, AD_CODE, DAY |  |
| [PAY_DR_FEE](#pay_dr_fee) | 24 |  |  |
| [PAY_EXCEPTIONAL](#pay_exceptional) | 7 |  |  |
| [PAY_ITAX_DETAIL](#pay_itax_detail) | 55 | MRNO, START_DATE, END_DATE |  |
| [PAY_ITAX_DETAIL_HISTORY](#pay_itax_detail_history) | 17 |  |  |
| [PAY_ITAX_DTL_TMP](#pay_itax_dtl_tmp) | 15 | CRITERIA_ID, START_DATE, END_DATE, PAYROLL_LOCATION_ID, MRNO |  |
| [PAY_ITAX_INCOME_DETAIL](#pay_itax_income_detail) | 5 | MRNO, START_DATE, END_DATE, PARAMETER |  |
| [PAY_LEAVES](#pay_leaves) | 17 | MRNO, START_DATE, END_DATE, LEAVE_TYPE_ID |  |
| [PAY_PF_VOUCHER](#pay_pf_voucher) | 19 | START_DATE, END_DATE, MRNO |  |
| [PAY_REPORT_FILE](#pay_report_file) | 15 | REPORT_CODE |  |
| [PAY_REPORT_FORMAT](#pay_report_format) | 14 | AD_GROUP_CODE | This table is used to define groups of different allowances / deductions, this group will be used into formatting salary sheets |
| [PAY_REPORT_ROUTING](#pay_report_routing) | 14 | REPORT_CODE, AD_CODE, AD_GROUP_CODE |  |
| [PAY_STATUS](#pay_status) | 17 | SERIAL_NO |  |
| [PAY_TMP_BANK](#pay_tmp_bank) | 8 |  |  |
| [PAY_TMP_EMP](#pay_tmp_emp) | 11 |  |  |
| [PAY_TMP_MPA](#pay_tmp_mpa) | 20 |  |  |
| [PAY_TMP_REPORT](#pay_tmp_report) | 34 |  |  |
| [PAY_VOUCHER](#pay_voucher) | 33 | START_DATE, END_DATE, SERIAL_NO, LOCATION_ID |  |
| [PAY_VOUCHER_MASTER](#pay_voucher_master) | 15 | START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO |  |
| [PAY_VOUCHER_DETAIL](#pay_voucher_detail) | 19 | START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO, COA_CODE, LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE |  |
| [PAY_VOUCHER_TEMP](#pay_voucher_temp) | 20 |  |  |
| [PAY_VOUCHER_TMP](#pay_voucher_tmp) | 16 | PAY_START_DATE, PAY_END_DATE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO |  |
| [PENDING_LOANS](#pending_loans) | 19 |  |  |
| [PF_FINAL_SETTLEMENT](#pf_final_settlement) | 24 | MRNO, SR_NO |  |
| [PROCESS_INCREMENT_MASTER](#process_increment_master) | 16 | PROCESS_ID |  |
| [PROCESS_MEMBERS](#process_members) | 30 | PROCESS_ID, MRNO |  |
| [PROFIT_VOUCHER_TMP](#profit_voucher_tmp) | 22 | YEAR_CODE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO, DETAIL_SERIAL_NO |  |
| [REP_LOAN_LEDGER](#rep_loan_ledger) | 17 |  | This is a temporary table to generate trial balances / ledgers of advances and loans |
| [RPT_SALARY_TAX_LINE_ITEM](#rpt_salary_tax_line_item) | 17 |  |  |
| [R_COST_TO_COMPANY_TEMP](#r_cost_to_company_temp) | 138 | START_DATE, END_DATE, MRNO |  |
| [SALARY_ELEMENT](#salary_element) | 4 |  |  |
| [SALARY_SLABS](#salary_slabs) | 17 |  |  |
| [TARGET_TABLE](#target_table) | 13 |  |  |
| [TAX_CALCULATION_LOG](#tax_calculation_log) | 12 |  |  |
| [TEMP_INCREMENT_MASTER](#temp_increment_master) | 23 | PROCESS_ID, MRNO |  |
| [TEMP_INCREMENT_DETAIL](#temp_increment_detail) | 20 | PROCESS_ID, MRNO, AD_CODE |  |
| [TEMP_INDIVIDUAL_ITAX](#temp_individual_itax) | 11 |  |  |
| [TEMP_ITAX](#temp_itax) | 36 |  |  |
| [TEMP_SALARY_RECONCILE_DATA](#temp_salary_reconcile_data) | 9 |  |  |
| [TMP_LOAN_SUMMARY](#tmp_loan_summary) | 19 |  |  |
| [TRAVEL_ADVANCE_APPROVAL](#travel_advance_approval) | 12 | REQUEST_NO |  |

### ACTUAL_PI

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PERFORM_DOCTOR** | VARCHAR2(14) | N |  |  |
| 2 | **PERFORM_MONTH** | DATE | Y |  |  |
| 3 | **START_DATE** | DATE | Y |  |  |
| 4 | **END_DATE** | DATE | Y |  |  |
| 5 | **PAY_START_DATE** | DATE | Y |  |  |
| 6 | **PAY_END_DATE** | DATE | Y |  |  |
| 7 | **CALC_INCOME** | NUMBER | Y |  |  |
| 8 | **WAIVE_OFF_B_INV** | NUMBER | Y |  |  |
| 9 | **WAIVE_OFF_A_INV** | NUMBER | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### AD_EXCEPTIONAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** | DATE | N |  |  |
| 2 | **END_DATE** | DATE | N |  |  |
| 3 | **AD_CODE** | CHAR(3) | N |  |  |
| 4 | **MRNO** | VARCHAR2(14) | N |  |  |
| 5 | **TRANS_DATE** | DATE | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **NO_OF_DAYS** | NUMBER(5,2) | Y |  |  |
| 15 | **PENDING_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### DEF_AD_GROUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_GROUP_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 4 | **AD_TYPE** | CHAR(1) | Y | 'A' |  |
| 5 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 6 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 7 | **AD_ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **AD_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_AD_GROUP` (AD_GROUP_CODE)
- **Check** `CK_DAG_ACTIVE`: `(active in ('N','Y'))`
- **Check** `CK_DEF_AD_GROUP_1`: `(ad_type in ('A','D'))`
- **Check** `CK_DEF_AD_GROUP_NN`: `(ad_type is not null)`
- **Referenced by**: `DEF_AD_SETUP`, `DEF_ALLOWANCE_DEDUCTION`
- **Triggers**: `DEF_AD_GROUP_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_GROUP_DEL` (AFTER DELETE), `DEF_AD_GROUP_INS` (BEFORE INSERT), `DEF_AD_GROUP_UPD` (BEFORE UPDATE), `TRG_WS_KZL_DN_VB_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_ALLOWANCE_DEDUCTION

This table is used to define different types of allowances / deductions which are used in salary processing. It also describes different formulas to calculate allowances and deductions

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 | CHAR(3) | N |  | Auto-generated Allowance / Deduction Code (PK) |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of Allowance or deduction |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short Name of Allowance or deduction, to be used in some reports |
| 4 | **AD_TYPE** | CHAR(1) | Y | 'A' | Either it is Allowance or Deduction |
| 5 | **CALC_TYPE** | CHAR(1) | Y | 'A' | Either calculation is dependant on attendance or not |
| 6 | **DED_TYPE** | CHAR(1) | Y | 'O' | Either deduction is Income Tax, P-Fund or any other type |
| 7 | **VALUE_TYPE** | CHAR(1) | Y | 'A' | Either allowance / deduction is based on percentage or value |
| 8 | **INCLUDE_IN_GROSS** | CHAR(1) | Y | 'Y' | Either allowance / deduction is included into Gross salary or not |
| 9 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
| 10 | **OT_CALC_BASE** | CHAR(1) | Y | 'G' |  |
| 11 | **PRACTICE_INCOME** | CHAR(1) | Y | 'N' |  |
| 12 | **ENTRY_TYPE** | CHAR(1) | Y | 'S' |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **TRN_DATE** | DATE | Y |  |  |
| 19 | **CBR_AMOUNT_CODE** | VARCHAR2(4) | Y |  |  |
| 20 | **AD_GROUP_CODE** → `PAYROLL.DEF_AD_GROUP` | CHAR(3) | Y |  |  |
| 21 | **TAXABLE** | CHAR(1) | Y | 'N' |  |
| 22 | **TAXABLE_ANNUALLY** | CHAR(1) | Y | 'N' | This column is effecitve for entry type as Transaction only |
| 23 | **ORGANIZATION_ID** 🔑 → `DEFINITIONS.ORGANIZATION` | VARCHAR2(3) | N |  |  |
| 24 | **LOCATION_ID** 🔑 → `DEFINITIONS.LOCATION` | VARCHAR2(3) | N |  |  |
| 25 | **EXCLUDE_FROM_GROSS_PAY** | CHAR(1) | Y | 'N' | This column add for LFA salary with payment |
| 26 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 27 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 28 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 29 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID)
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_1` (AD_GROUP_CODE) → `PAYROLL.DEF_AD_GROUP` (AD_GROUP_CODE) _DISABLED_
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_2` (LOCATION_ID) → `DEFINITIONS.LOCATION` (LOCATION_ID) _DISABLED_
- **FK** `FK_DEF_ALLOWANCE_DEDUCTION_3` (ORGANIZATION_ID) → `DEFINITIONS.ORGANIZATION` (ORGANIZATION_ID) _DISABLED_
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_1`: `(AD_TYPE IN ('A', 'D'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_10`: `(TAXABLE_ANNUALLY IN ('Y', 'N'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_2`: `(CALC_TYPE IN ('A', 'O'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_3`: `(DED_TYPE IN ('I','P','B','M','C','E','O','R'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_4`: `(VALUE_TYPE IN ('A', 'P'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_5`: `(INCLUDE_IN_GROSS IN ('Y', 'N'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_6`: `(ACTIVE IN ('Y', 'N'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_7`: `(OT_CALC_BASE IN ('G', 'B'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_8`: `(Practice_Income IN ('Y', 'N', 'G'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_9`: `(ENTRY_TYPE IN ('S','T'))`
- **Check** `CK_DEF_ALLOWANCE_DEDUCTION_NN`: `(AD_GROUP_CODE IS NOT NULL)`
- **Index** `IDX_DEF_ALLOWANCE_DEDUCTION_1` (DED_TYPE)
- **Index** `IDX_DEF_ALLOWANCE_DEDUCTION_2` (NVL(INCLUDE_IN_GROSS,'N'))
- **Referenced by**: `ALLOWANCE_DEDUCTION_DETAIL`, `ALLOWANCE_DEDUCTION_SETUP`, `DEF_GL_SETUP_DETAIL`, `DEF_ITAX_DETAIL_AD`, `EMP_ALLOWANCE_DEDUCTION_DETAIL`, `EMP_ALLOWANCE_DEDUCTION`, `EMP_INCREMENT_DETAIL`, `PAY_ALLOWANCE_DEDUCTION_TEST`, `PAY_ALLOWANCE_DEDUCTION`, `PAY_ITAX_DETAIL`
- **Triggers**: `DEF_ALLOWANCE_DEDUCTION_DEL` (AFTER DELETE), `DEF_ALLOWANCE_DEDUCTION_INS` (BEFORE INSERT), `DEF_ALLOWANCE_DEDUCTION_UPD` (BEFORE UPDATE)

### ALLOWANCE_DEDUCTION_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 4 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 5 | **TRANS_DATE** 🔑 | DATE | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **NO_OF_DAYS** | NUMBER(5,2) | Y |  |  |
| 15 | **CALC_AMOUNT_GUARANTEE** | NUMBER(10) | Y |  |  |
| 16 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 17 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 18 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 19 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 20 | **PROCESS_ID** → `BILLING.CORPORATE_INVOICE_MASTER` | VARCHAR2(12) | Y |  | This column will be used for Cafe Deduction Process, Data will be inserted into this column along with Deduction amount detail |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 24 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_ALLOWANCE_DEDUCTION_DETAIL` (START_DATE, END_DATE, AD_CODE, MRNO, TRANS_DATE)
- **FK** `FK_ALLOWANCE_DEDUCTION_DETAIL1` (MRNO) → `HRD.INFORMATION` (MRNO)
- **FK** `FK_DEDUCTION_DETAIL` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **FK** `FK_DEDUCTION_DETAIL_03` (PROCESS_ID) → `BILLING.CORPORATE_INVOICE_MASTER` (PROCESS_ID) _DISABLED_
- **Index** `IDX_ALLOW_DEDUCTION_DETAIL_1` (MRNO)
- **Index** `IDX_ALLOW_DEDUCTION_DETAIL_3` (AD_CODE)
- **Triggers**: `ALLOWANCE_DEDUCTION_DETAIL_DEL` (AFTER DELETE), `ALLOWANCE_DEDUCTION_DETAIL_INS` (BEFORE INSERT), `ALLOWANCE_DEDUCTION_DETAIL_UPD` (BEFORE UPDATE)

### ALLOWANCE_DEDUCTION_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 2 | **CALC_BASIC_GROSS** | CHAR(1) | Y |  |  |
| 3 | **CALC_PERCENT** | NUMBER(5,2) | Y |  |  |
| 4 | **FROM_DATE** 🔑 | DATE | N |  |  |
| 5 | **TO_DATE** | DATE | Y |  |  |
| 6 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 7 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 9 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_ALLOWANCE_DEDUCTION_SETUP` (AD_CODE, FROM_DATE)
- **FK** `FK_ALLOWANCE_DEDUCTION` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_

### DEF_ARREAR

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ARREAR_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **AD_TYPE** | CHAR(1) | Y | 'A' |  |
| 12 | **CBR_AMOUNT_CODE** | VARCHAR2(4) | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_ARREAR` (ARREAR_CODE)
- **Check** `CK_DEF_ARREAR_1`: `(ACTIVE IN ('Y', 'N'))`
- **Check** `CK_DEF_ARREAR_2`: `( AD_TYPE IN ('A','D'))`
- **Referenced by**: `ARREAR_DETAIL`, `DEF_GL_SETUP_DETAIL`
- **Triggers**: `DEF_ARREAR_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_ARREAR_DEL` (AFTER DELETE), `DEF_ARREAR_INS` (BEFORE INSERT), `DEF_ARREAR_UPD` (BEFORE UPDATE), `TRG_WS_WVB_PD_FA_Q` (AFTER INSERT OR UPDATE OR DELETE)

### ARREAR_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 3 | **ARREAR_CODE** 🔑 → `PAYROLL.DEF_ARREAR` | CHAR(3) | N |  |  |
| 4 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 5 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 7 | **ARREAR_START_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  |  |
| 8 | **ARREAR_END_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **DED_DAYS_HOURS** | NUMBER(5,2) | Y |  |  |
| 16 | **DED_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 17 | **DAYS_HOURS** | NUMBER(5,2) | Y |  |  |
| 18 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 19 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **AD_CODE** 🔑 | CHAR(3) | N | '000' |  |
| 21 | **PROCESS_ID** | VARCHAR2(12) | Y |  |  |
| 22 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 23 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 24 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 25 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_ARREAR_DETAIL` (START_DATE, END_DATE, ARREAR_CODE, MRNO, AD_CODE)
- **FK** `FK_ARREAR_DETAIL_1` (MRNO) → `HRD.INFORMATION` (MRNO)
- **FK** `FK_ARREAR_DETAIL_2` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **FK** `FK_ARREAR_DETAIL_3` (ARREAR_CODE) → `PAYROLL.DEF_ARREAR` (ARREAR_CODE)
- **FK** `FK_ARREAR_DETAIL_4` (ARREAR_START_DATE, ARREAR_END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **Index** `IDX_ARREAR_DETAIL_1` (MRNO)
- **Index** `IDX_ARREAR_DETAIL_3` (ARREAR_CODE)
- **Index** `IDX_ARREAR_DETAIL_4` (ARREAR_START_DATE, ARREAR_END_DATE)
- **Triggers**: `ARREAR_DETAIL_DEL` (AFTER DELETE), `ARREAR_DETAIL_INS` (BEFORE INSERT), `ARREAR_DETAIL_UPD` (BEFORE UPDATE)

### ARREAR_EXCEPTIONAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** | DATE | N |  |  |
| 2 | **END_DATE** | DATE | N |  |  |
| 3 | **ARREAR_CODE** | CHAR(3) | N |  |  |
| 4 | **MRNO** | VARCHAR2(14) | N |  |  |
| 5 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 7 | **ARREAR_START_DATE** | DATE | Y |  |  |
| 8 | **ARREAR_END_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **DED_DAYS_HOURS** | NUMBER(5,2) | Y |  |  |
| 16 | **DED_AMOUNT** | NUMBER(7,2) | Y |  |  |
| 17 | **DAYS_HOURS** | NUMBER(5,2) | Y |  |  |
| 18 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 19 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **AD_CODE** | CHAR(3) | N | '000' | this column specify that arrear blongs to sepcified ad code only |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 24 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Triggers**: `ARREAR_EXCEPTIONAL_DEL` (AFTER DELETE), `ARREAR_EXCEPTIONAL_INS` (BEFORE INSERT), `ARREAR_EXCEPTIONAL_UPD` (BEFORE UPDATE)

### BASE_TABLE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **INC_AMT** | NUMBER | Y |  |  |
| 3 | **INC_PCT** | NUMBER | Y |  |  |
| 4 | **INC_DATE** | DATE | Y |  |  |
| 5 | **BASIC** | NUMBER | Y |  |  |
| 6 | **GROSS** | NUMBER | Y |  |  |
| 7 | **C000** | NUMBER | Y |  |  |
| 8 | **C001** | NUMBER | Y |  |  |
| 9 | **C002** | NUMBER | Y |  |  |
| 10 | **C003** | NUMBER | Y |  |  |
| 11 | **C006** | NUMBER | Y |  |  |
| 12 | **C008** | NUMBER | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **TRN_DATE** | DATE | Y |  |  |
| 19 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 20 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 21 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 22 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### CBR_DATA_FILE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SERIAL_NO** | NUMBER(10) | N |  |  |
| 2 | **SALARY_MONTH** | VARCHAR2(100) | Y |  |  |
| 3 | **SALARY_PERIOD_FROM** | DATE | Y |  |  |
| 4 | **SALARY_PERIOD_TO** | DATE | Y |  |  |
| 5 | **EMP_CODE_FROM** | VARCHAR2(14) | Y |  |  |
| 6 | **EMP_CODE_TO** | VARCHAR2(14) | Y |  |  |
| 7 | **FILE_PATH** | VARCHAR2(100) | Y |  |  |
| 8 | **REG_DATE_TO** | DATE | Y |  |  |
| 9 | **REG_DATE_FROM** | DATE | Y |  |  |
| 10 | **PAYMENT_SR_NO** | NUMBER(2) | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### CHANGE_SALARY_ALLOW

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **INCREMENT_DATE** | DATE | Y |  |  |
| 3 | **CHANGE_DATE** | DATE | Y |  |  |
| 4 | **CHANGE_PARAM** | VARCHAR2(255) | Y |  |  |
| 5 | **CHANGE_TYPE** | VARCHAR2(255) | Y |  |  |
| 6 | **OLD_VALUE** | NUMBER(20,2) | Y |  |  |
| 7 | **NEW_VALUE** | NUMBER(20,2) | Y |  |  |
| 8 | **CHANGE_BY** | VARCHAR2(60) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(60) | Y |  |  |
| 10 | **EMAIL_SEND_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### CM_DEF_ADMIN_GROUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ADMIN_GROUP_ID** 🔑 | VARCHAR2(2) | N |  |  |
| 2 | **NAME** | VARCHAR2(250) | N |  |  |
| 3 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `DEF_ADMIN_GROUP_PK` (ADMIN_GROUP_ID)
- **Referenced by**: `CM_BILL_MASTER`, `CM_DEF_CONNECTION`
- **Triggers**: `CM_DEF_ADMIN_GROUP_DEL` (AFTER DELETE), `CM_DEF_ADMIN_GROUP_INS` (BEFORE INSERT), `CM_DEF_ADMIN_GROUP_UPD` (BEFORE UPDATE)

### CM_BILL_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ADMIN_GROUP_ID** 🔑 → `PAYROLL.CM_DEF_ADMIN_GROUP` | VARCHAR2(2) | N |  | Foreign key references PAYROLL.DEF_ADMIN_GROUP.ADMIN_GROUP_ID |
| 2 | **MONTH_ID** 🔑 | VARCHAR2(12) | N |  | Primary key |
| 3 | **ENTRY_DATE** | DATE | Y |  |  |
| 4 | **FINALIZED_BY** | VARCHAR2(8) | Y |  |  |
| 5 | **FINALIZED_DATE** | DATE | Y |  |  |
| 6 | **POSTED_BY** | VARCHAR2(14) | Y |  |  |
| 7 | **POSTED_DATE** | DATE | Y |  |  |
| 8 | **EXCESS_CALCULATION_BY** | VARCHAR2(14) | Y |  |  |
| 9 | **EXCESS_CAL_DATE** | DATE | Y |  |  |
| 10 | **FINAL_POST_DATE** | DATE | Y |  |  |
| 11 | **FINAL_POST_BY** | VARCHAR2(14) | Y |  |  |
| 12 | **MON_START_DATE** | DATE | Y |  |  |
| 13 | **MON_END_DATE** | DATE | Y |  |  |
| 14 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 18 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 19 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 20 | **TRN_DATE** | DATE | Y |  |  |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 24 | **WS_SYNC_DATE** | DATE | Y |  |  |
| 25 | **VOUCHER_REFERENCE** | VARCHAR2(100) | Y |  |  |

- **Primary key** `PK_BILL_MASTER` (MONTH_ID, ADMIN_GROUP_ID)
- **FK** `FK_BILL_MASTER_ADMIN_GROUP` (ADMIN_GROUP_ID) → `PAYROLL.CM_DEF_ADMIN_GROUP` (ADMIN_GROUP_ID)
- **Referenced by**: `CM_BILL_DETAIL`
- **Triggers**: `CM_BILL_MASTER_DEL` (AFTER DELETE), `CM_BILL_MASTER_INS` (BEFORE INSERT), `CM_BILL_MASTER_UPD` (BEFORE UPDATE)

### CM_DEF_CONNECTION

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CONNECTION_ID** 🔑 | VARCHAR2(8) | N |  |  |
| 2 | **CONTACT_NUMBER** | VARCHAR2(40) | N |  |  |
| 3 | **NETWORK** | VARCHAR2(2) | N | 'jz' | JZ: JAZZ, UF: UFONE, TL: TELENOR, ZO: ZONG, PT: PTCL, ST: STROMFIBER |
| 4 | **CONNECTION_TYPE** | CHAR(1) | N | 'N' | N: NORMAL, D: DATA |
| 5 | **PACKAGE_INFO** | VARCHAR2(250) | Y |  |  |
| 6 | **ADMIN_GROUP_ID** → `PAYROLL.CM_DEF_ADMIN_GROUP` | VARCHAR2(2) | Y |  |  |
| 7 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 8 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 18 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_CONNECTION` (CONNECTION_ID)
- **Unique** `CM_DEF_CONNECTION_UK01` (CONTACT_NUMBER)
- **FK** `FK_ADMIN_GROUP` (ADMIN_GROUP_ID) → `PAYROLL.CM_DEF_ADMIN_GROUP` (ADMIN_GROUP_ID)
- **Referenced by**: `CM_CONNECTION_REQUEST`, `CM_CONNECTION_TRANSACTIONS`
- **Triggers**: `CM_DEF_CONNECTION_DEL` (AFTER DELETE), `CM_DEF_CONNECTION_INS` (BEFORE INSERT), `CM_DEF_CONNECTION_UPD` (BEFORE UPDATE)

### CM_CONNECTION_REQUEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REQUEST_ID** 🔑 | VARCHAR2(10) | N |  |  |
| 2 | **REQUEST_TYPE** | CHAR(1) | N | 'D' | P: Pool, D: Dedicated |
| 3 | **ADMIN_GROUP_ID** | VARCHAR2(2) | Y |  |  |
| 4 | **REQUEST_DATE** | DATE | Y |  |  |
| 5 | **MRNO** | VARCHAR2(14) | Y |  | If request is raised for an employee then it will be entered |
| 6 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  | If request is raised for pool then it will be entered |
| 7 | **OFFICIAL_DEVICE** | CHAR(1) | Y |  | Is official device provided with the connection |
| 8 | **DEVICE_INFO** | VARCHAR2(250) | Y |  |  |
| 9 | **OWNER_TYPE** | CHAR(1) | N | 'P' | O: Official, P: Personal |
| 10 | **CONNECTION_ID** → `PAYROLL.CM_DEF_CONNECTION` | VARCHAR2(8) | Y |  | Filled in case of official device |
| 11 | **CONTACT_NUMBER** | VARCHAR2(40) | Y |  | Filled in case of personal number |
| 12 | **NETWORK** | VARCHAR2(2) | Y | 'JZ' | Filled in case of personal number |
| 13 | **BILL_TYPE** | CHAR(1) | N | 'P' | P: Prepaid, O: Postpaid |
| 14 | **LIMIT_ALLOWED** | NUMBER(12) | Y |  | Monthly approved amount |
| 15 | **PAID_BY** | CHAR(1) | N | 'O' | O: Office, S: Self |
| 16 | **FROM_DATE** | DATE | Y |  |  |
| 17 | **TO_DATE** | DATE | Y |  |  |
| 18 | **APPROVED_BY** | VARCHAR2(14) | Y |  |  |
| 19 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 20 | **DOCUMENT_ID** | VARCHAR2(13) | Y |  |  |
| 21 | **STATUS_ID** | VARCHAR2(3) | Y | '100' |  |
| 22 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 23 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 24 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 25 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 26 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 27 | **TRN_DATE** | DATE | Y |  |  |
| 28 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 29 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 30 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 31 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CONNECTION_REQUEST` (REQUEST_ID)
- **FK** `FK_CONNECTION_REQUEST_CONNECTION` (CONNECTION_ID) → `PAYROLL.CM_DEF_CONNECTION` (CONNECTION_ID)
- **Index** `IDX_CM_CONNECTION_REQUEST_01` (CONNECTION_ID)
- **Referenced by**: `CM_BILL_DETAIL`, `CM_CONNECTION_REQ_DOCUMENT`, `CM_CONNECTION_TRANSACTIONS`
- **Triggers**: `CM_CONNECTION_REQUEST_DEL` (AFTER DELETE), `CM_CONNECTION_REQUEST_INS` (BEFORE INSERT), `CM_CONNECTION_REQUEST_UPD` (BEFORE UPDATE)

### CM_BILL_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ADMIN_GROUP_ID** 🔑 → `PAYROLL.CM_BILL_MASTER` | VARCHAR2(2) | N |  |  |
| 2 | **MONTH_ID** 🔑 → `PAYROLL.CM_BILL_MASTER` | VARCHAR2(12) | N |  |  |
| 3 | **REQUEST_ID** 🔑 → `PAYROLL.CM_CONNECTION_REQUEST` | VARCHAR2(10) | N |  |  |
| 4 | **BILL_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 5 | **PAYMENT_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 6 | **PAYMENT_METHOD** | VARCHAR2(8) | Y |  | lo (load), cd (card), ch (cash), np (no payment) |
| 7 | **PAYMENT_DATE** | DATE | Y |  |  |
| 8 | **EXCESS_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 9 | **DEDUCTION_AD_CODE** | VARCHAR2(8) | Y |  |  |
| 10 | **LIMIT_ALLOWED** | NUMBER(12) | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **WS_SYNC_DATE** | DATE | Y |  |  |
| 21 | **INACTIVE_EMPLOYEE** | VARCHAR2(1) | Y |  |  |
| 22 | **REQUEST_EXPIRED** | VARCHAR2(1) | Y |  |  |
| 23 | **PAID_BY_SELF** | VARCHAR2(1) | Y |  |  |
| 24 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 25 | **CONTACT_NUMBER** | VARCHAR2(40) | Y |  |  |
| 26 | **MRNO** | VARCHAR2(14) | Y |  |  |

- **Primary key** `PK_BILL_DETAIL` (ADMIN_GROUP_ID, MONTH_ID, REQUEST_ID)
- **Unique** `CM_BILL_DETAIL_UK01` (MONTH_ID, CONTACT_NUMBER)
- **FK** `FK_BILL_MASTER` (MONTH_ID, ADMIN_GROUP_ID) → `PAYROLL.CM_BILL_MASTER` (MONTH_ID, ADMIN_GROUP_ID)
- **FK** `FK_CONNECTION_REQUEST` (REQUEST_ID) → `PAYROLL.CM_CONNECTION_REQUEST` (REQUEST_ID)
- **Triggers**: `CM_BILL_DETAIL_DEL` (AFTER DELETE), `CM_BILL_DETAIL_INS` (BEFORE INSERT), `CM_BILL_DETAIL_UPD` (BEFORE UPDATE)

### CM_CONNECTION_REQ_DOCUMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DOCUMENT_ID** 🔑 | VARCHAR2(13) | N |  |  |
| 2 | **REQUEST_ID** → `PAYROLL.CM_CONNECTION_REQUEST` | VARCHAR2(10) | N |  |  |
| 3 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CM_CONNECTION_REQ_DOCUMENT` (DOCUMENT_ID)
- **FK** `FK_CM_CONNECTION_REQ_DOCUMENT` (REQUEST_ID) → `PAYROLL.CM_CONNECTION_REQUEST` (REQUEST_ID)
- **Index** `IDX_CM_CONNECTION_REQ_DOCUMENT` (REQUEST_ID)
- **Triggers**: `CM_CONNECTION_REQ_DOCUMENT_DEL` (AFTER DELETE), `CM_CONNECTION_REQ_DOCUMENT_INS` (BEFORE INSERT), `CM_CONNECTION_REQ_DOCUMENT_UPD` (BEFORE UPDATE)

### CM_CONNECTION_TRANSACTIONS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **TRANS_ID** 🔑 | VARCHAR2(8) | N |  |  |
| 2 | **TRANS_DATE** | DATE | Y |  |  |
| 3 | **REQUEST_ID** → `PAYROLL.CM_CONNECTION_REQUEST` | VARCHAR2(10) | Y |  |  |
| 4 | **CONNECTION_ID** → `PAYROLL.CM_DEF_CONNECTION` | VARCHAR2(8) | Y |  |  |
| 5 | **FROM_DATE** | DATE | Y |  |  |
| 6 | **TO_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CONNECTION_TRANSACTIONS` (TRANS_ID)
- **FK** `FK_CONNECTION_TRANSACTIONS` (CONNECTION_ID) → `PAYROLL.CM_DEF_CONNECTION` (CONNECTION_ID)
- **FK** `FK_CONNECTION_TRANSACTIONS_REQUEST` (REQUEST_ID) → `PAYROLL.CM_CONNECTION_REQUEST` (REQUEST_ID)
- **Triggers**: `CM_CONNECTION_TRANSACTIONS_DEL` (AFTER DELETE), `CM_CONNECTION_TRANSACTIONS_INS` (BEFORE INSERT), `CM_CONNECTION_TRANSACTIONS_UPD` (BEFORE UPDATE)

### CM_DEF_ADMIN_GROUP_DTL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ADMIN_GROUP_ID** 🔑 | VARCHAR2(2) | N |  |  |
| 2 | **ADMIN_MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 4 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_ADMIN_GROUP_DTL` (ADMIN_GROUP_ID, ADMIN_MRNO)
- **Triggers**: `CM_DEF_ADMIN_GROUP_DTL_DEL` (AFTER DELETE), `CM_DEF_ADMIN_GROUP_DTL_INS` (BEFORE INSERT), `CM_DEF_ADMIN_GROUP_DTL_UPD` (BEFORE UPDATE)

### CM_INVOICES

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MONTH_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **CONTACT_NUMBER** 🔑 | VARCHAR2(40) | N |  |  |
| 3 | **BILL_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 4 | **BILL_MONTH_ID** | VARCHAR2(12) | Y |  |  |
| 5 | **BILL_REQUEST_ID** | VARCHAR2(10) | Y |  |  |
| 6 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_CM_INVOICES` (MONTH_ID, CONTACT_NUMBER)
- **Triggers**: `CM_INVOICES_DEL` (AFTER DELETE), `CM_INVOICES_INS` (BEFORE INSERT), `CM_INVOICES_UPD` (BEFORE UPDATE)

### DEF_AD_CHART

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **SRNO** 🔑 | NUMBER(3) | N |  |  |
| 3 | **START_DATE** | DATE | Y |  |  |
| 4 | **END_DATE** | DATE | Y |  |  |
| 5 | **DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 6 | **ACTIVE** | CHAR(1) | Y |  |  |
| 7 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_AD_CODE` (AD_CODE, SRNO)
- **Triggers**: `DEF_AD_CHART_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_CHART_DEL` (AFTER DELETE), `DEF_AD_CHART_INS` (BEFORE INSERT), `DEF_AD_CHART_PK` (BEFORE INSERT), `DEF_AD_CHART_UPD` (BEFORE UPDATE), `TRG_WS_DKJ_UV_FC_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_CHART_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **SRNO** 🔑 | NUMBER(3) | N |  |  |
| 3 | **PATIENT_TYPE_GROUP_ID** 🔑 → `DEFINITIONS.PATIENT_TYPE_GROUPS` | VARCHAR2(3) | N |  |  |
| 4 | **DESIGNATION_CATEGORY_ID** 🔑 → `DEFINITIONS.DESIGNATION_CATEGORY` | VARCHAR2(3) | N |  |  |
| 5 | **GRADE_ID** 🔑 | VARCHAR2(6) | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
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

- **Primary key** `PK_DEF_AD_CHART_DETAIL` (AD_CODE, SRNO, PATIENT_TYPE_GROUP_ID, DESIGNATION_CATEGORY_ID, GRADE_ID)
- **FK** `FK_DEF_AD_CHART_DETAIL1` (PATIENT_TYPE_GROUP_ID) → `DEFINITIONS.PATIENT_TYPE_GROUPS` (GROUP_ID) _DISABLED_
- **FK** `FK_DEF_AD_CHART_DETAIL2` (DESIGNATION_CATEGORY_ID) → `DEFINITIONS.DESIGNATION_CATEGORY` (DESIGNATION_CATEGORY_ID) _DISABLED_
- **Triggers**: `DEF_AD_CHART_DETAIL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_CHART_DETAIL_DEL` (AFTER DELETE), `DEF_AD_CHART_DETAIL_INS` (BEFORE INSERT), `DEF_AD_CHART_DETAIL_UPD` (BEFORE UPDATE), `TRG_WS_TKR_PZ_OS_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_CONSTANT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  |  |
| 3 | **AD_TYPE** | CHAR(1) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **PUBLIC_COA_CODE** | VARCHAR2(16) | Y |  | This field stores the COA code from Public secter COA |
| 12 | **SORTING_NO** | NUMBER(3) | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_AD_CONSTANT` (AD_CODE)
- **Triggers**: `DEF_AD_CONSTANT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_CONSTANT_DEL` (AFTER DELETE), `DEF_AD_CONSTANT_INS` (BEFORE INSERT), `DEF_AD_CONSTANT_UPD` (BEFORE UPDATE), `TRG_WS_NXW_PQ_TN_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_NATURE_TYPE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_NATURE_TYPE_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **DED_TYPE** | CHAR(1) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
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

- **Primary key** `PK_DEF_AD_NATURE_TYPE` (AD_NATURE_TYPE_ID)
- **Referenced by**: `DEF_AD_SETUP`
- **Triggers**: `DEF_AD_NATURE_TYPE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_NATURE_TYPE_DEL` (AFTER DELETE), `DEF_AD_NATURE_TYPE_INS` (BEFORE INSERT), `DEF_AD_NATURE_TYPE_UPD` (BEFORE UPDATE), `TRG_WS_FHI_YZ_ST_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_SETUP

This table is used to location wise define def_allowances_deduction.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **AD_CODE** 🔑 | CHAR(3) | N |  | Auto-generated Allowance / Deduction Code (PK) |
| 4 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of Allowance or deduction |
| 5 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short Name of Allowance or deduction, to be used in some reports |
| 6 | **AD_GROUP_CODE** → `PAYROLL.DEF_AD_GROUP` | CHAR(3) | Y |  |  |
| 7 | **ATTENDANCE_BASED** | CHAR(1) | Y | 'A' | Either calculation is dependant on attendance or not |
| 8 | **AD_NATURE_TYPE_ID** → `PAYROLL.DEF_AD_NATURE_TYPE` | VARCHAR2(3) | Y | '000' | Refers to def_ad_nature_type |
| 9 | **ENTRY_TYPE** | CHAR(1) | Y | 'S' |  |
| 10 | **CALCULATION_TYPE** | VARCHAR2(2) | Y | 'OT' | PS Payscale, PB Basic(%), PG Gross(%), CH AD Chart, FZ Freeze, FX Fix, OB Obsleted, OT Other |
| 11 | **CALC_PERCENTAGE** | NUMBER(5,2) | Y |  | Value of Percentage if calculation_type is PG or PB |
| 12 | **TAXABLE** | CHAR(1) | Y | 'N' |  |
| 13 | **TAXABLE_ANNUALLY** | CHAR(1) | Y | 'N' | This column is effecitve for entry type as Transaction only |
| 14 | **INCLUDE_IN_GROSS** | CHAR(1) | Y | 'Y' | Either allowance / deduction is included into Gross salary or not |
| 15 | **EXCLUDE_FROM_GROSS_PAY** | CHAR(1) | Y | 'N' | This column add for LFA salary with payment |
| 16 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
| 17 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **TRN_DATE** | DATE | Y |  |  |
| 20 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 21 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 22 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 23 | **PERCENTAGE_SETUP_ID** | VARCHAR2(3) | Y |  |  |
| 24 | **SLAB_ID** → `BILLING.DEF_SLAB` | VARCHAR2(12) | Y |  |  |
| 25 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 26 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 27 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 28 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 29 | **DISTRIBUTE_TAX** | CHAR(1) | N | 'Y' | Either deduct the whole tax in one salary or devide on remaining months |

- **Primary key** `PK_DEF_AD_SETUP` (ORGANIZATION_ID, LOCATION_ID, AD_CODE)
- **FK** `FK_DEF_AD_SETUP_1` (AD_GROUP_CODE) → `PAYROLL.DEF_AD_GROUP` (AD_GROUP_CODE) _DISABLED_
- **FK** `FK_DEF_AD_SETUP_2` (AD_NATURE_TYPE_ID) → `PAYROLL.DEF_AD_NATURE_TYPE` (AD_NATURE_TYPE_ID) _DISABLED_
- **FK** `FK_DEF_AD_SETUP_3` (SLAB_ID) → `BILLING.DEF_SLAB` (SLAB_ID) _DISABLED_
- **Check** `CK_DEF_AD_SETUP_1`: `(TAXABLE_ANNUALLY IN ('Y', 'N'))`
- **Check** `CK_DEF_AD_SETUP_2`: `(attendance_based IN ('A', 'O'))`
- **Check** `CK_DEF_AD_SETUP_4`: `(INCLUDE_IN_GROSS IN ('Y', 'N'))`
- **Check** `CK_DEF_AD_SETUP_5`: `(ACTIVE IN ('Y', 'N'))`
- **Check** `CK_DEF_AD_SETUP_6`: `(ENTRY_TYPE IN ('S','T'))`
- **Check** `CK_DEF_AD_SETUP_NN`: `(AD_GROUP_CODE IS NOT NULL)`
- **Index** `IDX_DEF_AD_SETUP_1` (AD_NATURE_TYPE_ID)
- **Index** `IDX_DEF_AD_SETUP_2` (NVL(INCLUDE_IN_GROSS,'N'))
- **Triggers**: `DEF_AD_SETUP_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_SETUP_DEL` (AFTER DELETE), `DEF_AD_SETUP_INS` (BEFORE INSERT), `DEF_AD_SETUP_UPD` (BEFORE UPDATE), `TRG_WS_WKA_UZ_BE_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_SETUP_DC

This table is used to define designation category wise ad setup.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 4 | **DESIGNATION_CATEGORY_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 5 | **CALCULATION_TYPE** | VARCHAR2(2) | Y | 'OT' |  |
| 6 | **CALC_PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 7 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **PERCENTAGE_SETUP_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **SLAB_ID** | VARCHAR2(12) | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_AD_SETUP_DC` (ORGANIZATION_ID, LOCATION_ID, AD_CODE, DESIGNATION_CATEGORY_ID)
- **Triggers**: `DEF_AD_SETUP_DC_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_SETUP_DC_DEL` (AFTER DELETE), `DEF_AD_SETUP_DC_INS` (BEFORE INSERT), `DEF_AD_SETUP_DC_UPD` (BEFORE UPDATE), `TRG_WS_BUF_UB_DI_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_SETUP_PT

This table is used to define patient type group wise ad setup.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 4 | **PATIENT_TYPE_ID** 🔑 | VARCHAR2(6) | N |  |  |
| 5 | **CALCULATION_TYPE** | VARCHAR2(2) | Y | 'OT' |  |
| 6 | **CALC_PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 7 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **PERCENTAGE_SETUP_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **SLAB_ID** | VARCHAR2(12) | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_AD_SETUP_PT` (ORGANIZATION_ID, LOCATION_ID, AD_CODE, PATIENT_TYPE_ID)
- **Triggers**: `DEF_AD_SETUP_PT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_SETUP_PT_DEL` (AFTER DELETE), `DEF_AD_SETUP_PT_INS` (BEFORE INSERT), `DEF_AD_SETUP_PT_UPD` (BEFORE UPDATE), `TRG_WS_MMZ_TB_FP_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_AD_SETUP_UNPAID_LT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **LEAVE_TYPE_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 4 | **AD_CODE** 🔑 | VARCHAR2(3) | N |  |  |
| 5 | **PAYMENT_PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 6 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
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

- **Primary key** `PK_DEF_AD_SETUP_UNPAID_LT` (ORGANIZATION_ID, LOCATION_ID, LEAVE_TYPE_ID, AD_CODE)
- **Triggers**: `DEF_AD_SETUP_UNPAID_LT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_AD_SETUP_UNPAID_LT_DEL` (AFTER DELETE), `DEF_AD_SETUP_UNPAID_LT_INS` (BEFORE INSERT), `DEF_AD_SETUP_UNPAID_LT_UPD` (BEFORE UPDATE), `TRG_WS_TWV_IJ_IA_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EMP_JOB

This table is used to define organizational hierarchy of employees

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **JOB_CODE** 🔑 | VARCHAR2(18) | N |  | PK - Auto generated field |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of Job |
| 3 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 4 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 10 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 11 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 12 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_EMP_JOB` (JOB_CODE)
- **Referenced by**: `DEF_EMP_FINANCIAL`
- **Triggers**: `DEF_EMP_JOB_DEL` (AFTER DELETE), `DEF_EMP_JOB_INS` (BEFORE INSERT), `DEF_EMP_JOB_UPD` (BEFORE UPDATE)

### DEF_GL_SETUP_MASTER

This table is used to define different setups for payroll jornal voucher

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GL_SETUP_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |
| 3 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either row is currenctly availabe for transactions or not |
| 4 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **LOCATION_ID** | VARCHAR2(3) | N |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_S_GL_SETUP_MASTER` (GL_SETUP_CODE)
- **Check** `CK_S_GL_SETUP_MASTER_1`: `(ACTIVE IN ('Y', 'N'))`
- **Referenced by**: `DEF_EMP_FINANCIAL`, `DEF_GL_SETUP_DETAIL_FS`, `DEF_GL_SETUP_DETAIL`
- **Triggers**: `DEF_GL_SETUP_MASTER_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_GL_SETUP_MASTER_DEL` (AFTER DELETE), `DEF_GL_SETUP_MASTER_INS` (BEFORE INSERT), `DEF_GL_SETUP_MASTER_UPD` (BEFORE UPDATE), `TRG_WS_TTB_AI_IF_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_INCOME_TAX

This table is used to define different setups for income tax calculation according to govt. policy

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **S_ITAX_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of  income tax setup |
| 3 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 4 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 10 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 11 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 12 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_INCOME_TAX` (S_ITAX_CODE)
- **Referenced by**: `DEF_EMP_FINANCIAL`
- **Triggers**: `DEF_INCOME_TAX_DEL` (AFTER DELETE), `DEF_INCOME_TAX_INS` (BEFORE INSERT), `DEF_INCOME_TAX_UPD` (BEFORE UPDATE)

### DEF_EMP_FINANCIAL

This table is used to define financial parameters of empoyee which are used to entertain different financial activities

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  | PK-Self explainatory |
| 2 | **COST_CENTRE_ID** → `DEFINITIONS.GL_DIV_DEPT_CC` | CHAR(10) | Y |  | FK-Self explainatory |
| 3 | **BRANCH_ID** → `DEFINITIONS.BANK_BRANCH` | VARCHAR2(3) | Y |  | FK-Self explainatory |
| 4 | **BANK_ID** → `DEFINITIONS.BANK_BRANCH` | VARCHAR2(6) | Y |  | FK-Self explainatory |
| 5 | **S_ITAX_CODE** → `PAYROLL.DEF_INCOME_TAX` | CHAR(3) | Y |  | Used to calculated income tax |
| 6 | **CURRENCY_ID** → `DEFINITIONS.CURRENCY` | VARCHAR2(3) | N |  | Currency of salary payment |
| 7 | **JOB_CODE** → `PAYROLL.DEF_EMP_JOB` | VARCHAR2(18) | Y |  | Manpower structure Id, i.e. according to organizational structure employee comes under which hierarchy |
| 8 | **PAYMENT_MODE** | CHAR(1) | Y | 'C' | Salry payment through Cash, Chequeor Bank Transfer |
| 9 | **BANK_ACCOUNT_NO** | VARCHAR2(50) | Y |  | Employees Bank accounts no where salary is transferred |
| 10 | **INCLUDE_IN_EOBI** | CHAR(1) | Y | 'Y' | Either this employee is included into calculation of EOBI or not |
| 11 | **INCLUDE_IN_ESSI** | CHAR(1) | Y | 'Y' | Either this employee is included into calculation of ESSI or not |
| 12 | **INCLUDE_IN_ED_CESS** | CHAR(1) | Y | 'Y' | Either this employee is included into calculation of Education Cess or not |
| 13 | **INITIAL_GROSS** | NUMBER(20,2) | Y |  | Gross salary of employee when he/she was hired |
| 14 | **INITIAL_BASIC** | NUMBER(20,2) | Y |  | Basic salary of employee when he/she was hired |
| 15 | **CURRENT_GROSS** | NUMBER(20,2) | Y |  | Current gross salary of employee |
| 16 | **CURRENT_BASIC** | NUMBER(20,2) | Y |  | Current basic salary of employee |
| 17 | **GL_SETUP_CODE** → `PAYROLL.DEF_GL_SETUP_MASTER` | CHAR(3) | Y |  | It is used to generate the Payroll Journel Voucher |
| 18 | **SALARY_ON_CARD_SWIPE** | CHAR(1) | Y |  |  |
| 19 | **EOBI_NO** | VARCHAR2(18) | Y |  |  |
| 20 | **FBS_DEPT_CODE** | VARCHAR2(3) | Y |  |  |
| 21 | **EMP_TYPE** | CHAR(1) | Y | 'O' |  |
| 22 | **PASSPORT_NO** | VARCHAR2(15) | Y |  |  |
| 23 | **EOBI_JOINING_DATE** | DATE | Y |  |  |
| 24 | **NTN_NO** | VARCHAR2(13) | Y |  |  |
| 25 | **DAILY_WAGER** | CHAR(1) | Y |  |  |
| 26 | **DAILY_RATE** | NUMBER(4) | Y |  |  |
| 27 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 28 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 29 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 30 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 31 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 32 | **TRN_DATE** | DATE | Y |  |  |
| 33 | **EXCL_LFA_INTAX** | CHAR(1) | Y | 'N' |  |
| 34 | **PF_JOINING_DATE** | DATE | Y |  |  |
| 35 | **ONLINE_ACCOUNT** | CHAR(1) | Y | 'N' |  |
| 36 | **ADD_CPI_PAYROLL** | CHAR(1) | Y | 'N' | Values of this column must be Y or N, Y means if CPI is calculated then on posting Add CPI into payroll.allowance_deduction_detail against AD CODE 049, N means don't add CPI into payroll |
| 37 | **PRINT_PAYSLIP** | CHAR(1) | Y | 'N' |  |
| 38 | **GP_FUND_NO** | VARCHAR2(30) | Y |  |  |
| 39 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 40 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 41 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 42 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 43 | **IBAN** | VARCHAR2(68) | Y |  |  |
| 44 | **BANK_AC_TITLE** | VARCHAR2(256) | Y |  |  |
| 45 | **MANUAL_TAX** | CHAR(1) | Y | 'N' |  |

- **Primary key** `PK_DEF_EMP_FINANCIAL` (MRNO)
- **FK** `FK_DEF_EMP_FINANCIAL_1` (COST_CENTRE_ID) → `DEFINITIONS.GL_DIV_DEPT_CC` (COST_CENTRE_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_2` (BRANCH_ID, BANK_ID) → `DEFINITIONS.BANK_BRANCH` (BRANCH_ID, BANK_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_3` (MRNO) → `HRD.INFORMATION` (MRNO)
- **FK** `FK_DEF_EMP_FINANCIAL_4` (S_ITAX_CODE) → `PAYROLL.DEF_INCOME_TAX` (S_ITAX_CODE)
- **FK** `FK_DEF_EMP_FINANCIAL_5` (CURRENCY_ID) → `DEFINITIONS.CURRENCY` (CURRENCY_ID)
- **FK** `FK_DEF_EMP_FINANCIAL_6` (JOB_CODE) → `PAYROLL.DEF_EMP_JOB` (JOB_CODE)
- **FK** `FK_DEF_EMP_FINANCIAL_7` (GL_SETUP_CODE) → `PAYROLL.DEF_GL_SETUP_MASTER` (GL_SETUP_CODE)
- **Check** `CK_DEF_EMP_FINANCIAL_1`: `(PAYMENT_MODE IN ('C', 'B', 'Q'))`
- **Check** `CK_DEF_EMP_FINANCIAL_2`: `(INCLUDE_IN_EOBI IN ('Y', 'N'))`
- **Check** `CK_DEF_EMP_FINANCIAL_3`: `(INCLUDE_IN_ESSI IN ('Y', 'N'))`
- **Check** `CK_DEF_EMP_FINANCIAL_4`: `(INCLUDE_IN_ED_CESS IN ('Y', 'N'))`
- **Check** `CK_DEF_EMP_FINANCIAL_5`: `(EMP_TYPE IN ('D','C','O'))`
- **Index** `IDX_DEF_EMP_FINANCIAL_1` (COST_CENTRE_ID)
- **Index** `IDX_DEF_EMP_FINANCIAL_2` (BRANCH_ID, BANK_ID)
- **Index** `IDX_DEF_EMP_FINANCIAL_4` (S_ITAX_CODE)
- **Index** `IDX_DEF_EMP_FINANCIAL_5` (CURRENCY_ID)
- **Index** `IDX_DEF_EMP_FINANCIAL_6` (JOB_CODE)
- **Index** `IDX_DEF_EMP_FINANCIAL_7` (GL_SETUP_CODE)
- **Referenced by**: `EMP_ALLOWANCE_DEDUCTION`
- **Triggers**: `DEF_EMP_FINANCIAL_COST_CENTER_NULL` (BEFORE UPDATE), `DEF_EMP_FINANCIAL_DEL` (AFTER DELETE), `DEF_EMP_FINANCIAL_INS` (BEFORE INSERT), `DEF_EMP_FINANCIAL_UPD` (BEFORE UPDATE)

### DEF_EXPENSE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  |  |
| 4 | **TYPE** | CHAR(1) | Y | 'N' |  |
| 5 | **ACTIVE** | CHAR(1) | Y | 'N' |  |
| 6 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **SERVICE_YEARS** | NUMBER(2) | Y |  |  |
| 13 | **BONUS_PERCENT** | NUMBER(5,2) | Y |  |  |
| 14 | **GROSS_BASIC** | CHAR(1) | Y |  |  |
| 15 | **FROM_JDATE** | DATE | Y |  |  |
| 16 | **TO_JDATE** | DATE | Y |  |  |
| 17 | **ORGANIZATION_ID** → `DEFINITIONS.ORGANIZATION` | VARCHAR2(3) | Y |  |  |
| 18 | **LOCATION_ID** 🔑 → `DEFINITIONS.LOCATION` | VARCHAR2(3) | N |  |  |
| 19 | **FIXED_AMOUNT** | NUMBER(12) | Y |  |  |
| 20 | **CLAIMABLE** | CHAR(1) | Y | 'N' |  |
| 21 | **AD_CODE** | CHAR(3) | Y |  |  |
| 22 | **HOD_APPROVAL_REQ** | CHAR(1) | Y | 'N' |  |
| 23 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 24 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 25 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 26 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 27 | **PAYMENT_METHOD** | CHAR(1) | N | 'A' | A: All, S: Salary, M: Manual |
| 28 | **AUTO_ADJ_PAYMENT** | CHAR(1) | N | 'N' |  |

- **Primary key** `PK_DEF_EXPENSE` (EXPENSE_CODE, LOCATION_ID)
- **FK** `FK_DEF_EXPENSE_1` (LOCATION_ID) → `DEFINITIONS.LOCATION` (LOCATION_ID) _DISABLED_
- **FK** `FK_DEF_EXPENSE_2` (ORGANIZATION_ID) → `DEFINITIONS.ORGANIZATION` (ORGANIZATION_ID) _DISABLED_
- **Check** `CK_DEF_EXPENSE_1`: `(ACTIVE IN ('Y', 'N'))`
- **Check** `CK_DEF_EXPENSE_2`: `(type in ('M','L','O','B','S'))`
- **Check** `CK_DEF_EXPENSE_3`: `(gross_basic in ('G','B', 'F'))`
- **Triggers**: `DEF_EXPENSE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_EXPENSE_DEL` (AFTER DELETE), `DEF_EXPENSE_INS` (BEFORE INSERT), `DEF_EXPENSE_UPD` (BEFORE UPDATE), `TRG_WS_BAN_JP_PG_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EXPENSE_CONSTANT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  |  |
| 4 | **TYPE** | CHAR(1) | Y |  |  |
| 5 | **ACTIVE** | CHAR(1) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **PAY_THROUGH_SALARY** | CHAR(1) | Y | 'N' | Column add for LFA payment with salary |
| 13 | **TAXABLE** | CHAR(1) | N | 'N' | Y: Whole Expense, A: Accounts, N: None |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_EXP_CONSTANT` (EXPENSE_CODE)
- **Referenced by**: `DEF_EXPENSE_TAXABLE_ACC`
- **Triggers**: `DEF_EXPENSE_CONSTANT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_EXPENSE_CONSTANT_DEL` (AFTER DELETE), `DEF_EXPENSE_CONSTANT_INS` (BEFORE INSERT), `DEF_EXPENSE_CONSTANT_UPD` (BEFORE UPDATE), `TRG_WS_YJR_OY_UQ_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EXPENSE_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_TYPE_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **EXPENSE_CODE** | CHAR(3) | Y |  |  |
| 3 | **DESCRIPTION** | VARCHAR2(64) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **DAYS_REQUIRED** | CHAR(1) | Y | 'N' |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_EXPENSE_DETAIL` (EXPENSE_TYPE_ID)
- **Referenced by**: `DEF_EXPENSE_DETAIL_SLAB`
- **Triggers**: `DEF_EXPENSE_DETAIL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_EXPENSE_DETAIL_DEL` (AFTER DELETE), `DEF_EXPENSE_DETAIL_INS` (BEFORE INSERT), `DEF_EXPENSE_DETAIL_UPD` (BEFORE UPDATE), `TRG_WS_WFR_HS_SR_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EXPENSE_DETAIL_SLAB

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_TYPE_ID** 🔑 → `PAYROLL.DEF_EXPENSE_DETAIL` | VARCHAR2(3) | N |  |  |
| 2 | **SLAB_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 3 | **IS_DEFAULT** | CHAR(1) | N | 'N' |  |
| 4 | **ACTIVE** | CHAR(1) | N | 'N' |  |
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

- **Primary key** `PK_DEF_EXPENSE_DETAIL_SLAB` (EXPENSE_TYPE_ID, SLAB_ID)
- **FK** `FK_DEF_EXPENSE_DETAIL_SLAB1` (EXPENSE_TYPE_ID) → `PAYROLL.DEF_EXPENSE_DETAIL` (EXPENSE_TYPE_ID)
- **Triggers**: `DEF_EXPENSE_DETAIL_SLAB_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_EXPENSE_DETAIL_SLAB_DEL` (AFTER DELETE), `DEF_EXPENSE_DETAIL_SLAB_INS` (BEFORE INSERT), `DEF_EXPENSE_DETAIL_SLAB_UPD` (BEFORE UPDATE), `TRG_WS_PHJ_BK_HS_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EXPENSE_TAXABLE_ACC

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_CODE** 🔑 → `PAYROLL.DEF_EXPENSE_CONSTANT` | CHAR(3) | N |  |  |
| 2 | **OBJECT_CODE** 🔑 → `FINANCE.VALUE_SETS` | VARCHAR2(11) | N |  |  |
| 3 | **VALUE_TYPE** 🔑 → `FINANCE.VALUE_SETS` | VARCHAR2(4) | N |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_EXPENSE_TAXABLE_ACC` (EXPENSE_CODE, OBJECT_CODE, VALUE_TYPE)
- **FK** `FK_DEF_EXPENSE_TAXABLE_AC1` (EXPENSE_CODE) → `PAYROLL.DEF_EXPENSE_CONSTANT` (EXPENSE_CODE)
- **FK** `FK_DEF_EXPENSE_TAXABLE_AC2` (OBJECT_CODE, VALUE_TYPE) → `FINANCE.VALUE_SETS` (OBJECT_CODE, VALUE_TYPE) _DISABLED_
- **Triggers**: `DEF_EXPENSE_TAXABLE_ACC_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_BIZ_EJ_FS_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_EXPENSE_WORKFLOW

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_CODE** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **SCHEMA_ID** | VARCHAR2(3) | N |  |  |
| 3 | **WORKFLOW_TYPE_ID** | NUMBER(3) | N |  |  |
| 4 | **WORK_FLOW_ID** | NUMBER(4) | N |  |  |
| 5 | **EXPENSE_TYPE_ID** | CHAR(1) | N |  |  |
| 6 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
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

- **Primary key** `PK_DEF_EXPENSE_WORKFLOW` (EXPENSE_CODE)
- **Triggers**: `DEF_EXPENSE_WORKFLOW_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_DYO_YQ_OR_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_FINANCIAL_SETUP

This table is used to define different formulas and rules applied to Govt. and corporate. It contains only one record.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **OT_CALC_BASE** | CHAR(1) | Y | 'G' | Either overtime is paid on gross salary or on basic salary |
| 2 | **OT_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of salary is paid as overtime |
| 3 | **NIGHT_CALC_BASE** | CHAR(1) | Y | 'G' | Either night shift allowance is paid on gross salary or on basic salary |
| 4 | **NIGHT_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of salary is paid as night allowance |
| 5 | **GRP_INS_CALC_BASE** | CHAR(1) | Y | 'G' | Either group insurance is paid on gross salary or on basic salary |
| 6 | **GRP_INS_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of salary is paid as group insurance |
| 7 | **PF_CALC_BASE** | CHAR(1) | Y | 'G' | Either provident Fund is paid on gross salary or on basic salary |
| 8 | **PF_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of salary is paid as provident fund |
| 9 | **LFA_CALC_BASE** | CHAR(1) | Y | 'G' | Either Leave Fare Assistance is paid on gross salary or on basic salary |
| 10 | **LFA_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of salary is paid as LFA |
| 11 | **EOBI_BASE_SALARY** | NUMBER(20,2) | Y |  | What is the base salary for EOBI calculation |
| 12 | **EOBI_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of base salary is paid as EOBI |
| 13 | **EOBI_EMPLOYER_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employer in payment of EOBI |
| 14 | **EOBI_EMPLOYEE_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employee in payment of EOBI |
| 15 | **EOBI_MALE_EXCLUSION_AGE** | NUMBER(3) | Y |  | How old men ale excluded in payment of EOBI |
| 16 | **EOBI_FEMALE_EXCLUSION_AGE** | NUMBER(3) | Y |  | How old women ale excluded in payment of EOBI |
| 17 | **EC_BASE_SALARY** | NUMBER(20,2) | Y |  | What is the base salary for Education Cess calculation |
| 18 | **EC_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of base salary is paid as Education Cess |
| 19 | **EC_EMPLOYER_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employer in payment of Education Cess |
| 20 | **EC_EMPLOYEE_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employee in payment of Education Cess |
| 21 | **ESSI_BASE_SALARY** | NUMBER(20,2) | Y |  | What is the contribution of employer in payment of ESSI |
| 22 | **ESSI_PERCENTAGE** | NUMBER(5,2) | Y |  | What %age of base salary is paid as EOBI |
| 23 | **ESSI_EMPLOYER_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employer in payment of ESSI |
| 24 | **ESSI_EMPLOYEE_CONTRIBUTION** | NUMBER(20,2) | Y |  | What is the contribution of employee in payment of ESSI |
| 25 | **ESSI_MALE_EXCLUSION_AGE** | NUMBER(3) | Y |  | How old men ale excluded in payment of ESSI |
| 26 | **ESSI_FEMALE_EXCLUSION_AGE** | NUMBER(3) | Y |  | How old women ale excluded in payment of ESSI |
| 27 | **BASIC_PER_GROSS** | NUMBER(5,2) | Y |  |  |
| 28 | **SALARY_ON_CARD_SWIPE** | CHAR(1) | Y |  |  |
| 29 | **ADV_EXP_CONVERSION_DAYS** | NUMBER(3) | Y |  |  |
| 30 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 31 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 32 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 33 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 34 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 35 | **TRN_DATE** | DATE | Y |  |  |
| 36 | **NURSE_TPT_ALLOWANCE** | NUMBER(5) | Y |  |  |
| 37 | **FROM_DATE** 🔑 | DATE | N |  |  |
| 38 | **TO_DATE** | DATE | Y |  |  |
| 39 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 40 | **LONG_SERVICE_DATE** | DATE | Y |  |  |
| 41 | **PI_TAX_PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 42 | **BACKDATE_REFUND_ALLOW** | CHAR(1) | Y | 'N' |  |
| 43 | **LFA_PMT_ALLOW** | NUMBER(2) | Y |  | Number of months for LFA payment before LFA Due Date |
| 44 | **COLLEGIALITY_FUND_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 45 | **OLD_LFA_START** | CHAR(6) | Y |  | For old LFA salary for joiners between 23rd Dec to 31st Dec |
| 46 | **OLD_LFA_END** | CHAR(6) | Y |  | For old LFA salary for joiners between 23rd Dec to 31st Dec |
| 47 | **LFA_PAYMENT_DAYS** | NUMBER(3) | Y |  | Number of days for LFA payment before LFA scheduled leave |
| 48 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 49 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 50 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 51 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_FINANCIAL_SETUP` (FROM_DATE)
- **Check** `CK_DEF_FINANCIAL_SETUP_1`: `(OT_CALC_BASE IN ('G', 'B'))`
- **Check** `CK_DEF_FINANCIAL_SETUP_2`: `(NIGHT_CALC_BASE IN ('G', 'B'))`
- **Check** `CK_DEF_FINANCIAL_SETUP_3`: `(GRP_INS_CALC_BASE IN ('G', 'B'))`
- **Check** `CK_DEF_FINANCIAL_SETUP_4`: `(PF_CALC_BASE IN ('G', 'B'))`
- **Check** `CK_DEF_FINANCIAL_SETUP_5`: `(LFA_CALC_BASE IN ('G', 'B'))`
- **BITMAP Index** `IDX_DEF_FINANCIAL_SETUP_1` (OT_CALC_BASE)
- **Triggers**: `DEF_FINANCIAL_SETUP_DEL` (AFTER DELETE), `DEF_FINANCIAL_SETUP_INS` (BEFORE INSERT), `DEF_FINANCIAL_SETUP_UPD` (BEFORE UPDATE)

### DEF_FS_ELEMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR_NO** | NUMBER | Y |  |  |
| 2 | **ELEMENT_CODE** 🔑 | VARCHAR2(8) | N |  |  |
| 3 | **DESCRIPTION** | VARCHAR2(100) | N |  |  |
| 4 | **LONG_DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 5 | **TYPE** | VARCHAR2(1) | Y |  |  |
| 6 | **TAXABLE_ELEMENT** | VARCHAR2(1) | Y | 'Y' |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **ELEMENT_UNIT** | VARCHAR2(20) | Y |  |  |
| 14 | **ACTIVE** | VARCHAR2(1) | Y | 'Y' |  |

- **Primary key** `PK_DEF_FS_ELEMENTS` (ELEMENT_CODE)
- **Referenced by**: `DEF_GL_SETUP_DETAIL_FS`
- **Triggers**: `DEF_FS_ELEMENT_DEL` (AFTER DELETE), `DEF_FS_ELEMENT_INS` (BEFORE INSERT), `DEF_FS_ELEMENT_UPD` (BEFORE UPDATE)

### DEF_FS_ELEMENT_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR_NO** 🔑 | NUMBER | N |  |  |
| 2 | **EVENT_DETIAL_DESC** | VARCHAR2(2000) | Y |  |  |
| 3 | **TABLE_SOURCE** | VARCHAR2(1000) | Y |  |  |
| 4 | **COLUMN_IDENTIFIER_1** | VARCHAR2(500) | Y |  |  |
| 5 | **COLUMN_IDENTIFIER_2** | VARCHAR2(500) | Y |  |  |
| 6 | **COLUMN_IDENTIFIER_3** | VARCHAR2(500) | Y |  |  |
| 7 | **WHERE_CLAUSE** | VARCHAR2(4000) | Y |  |  |
| 8 | **ORDER_BY** | NUMBER | Y |  |  |
| 9 | **ACTIVE** | CHAR(1) | Y |  |  |
| 10 | **REMARKS** | VARCHAR2(2000) | Y |  |  |
| 11 | **ELEMENT_CODE** 🔑 | VARCHAR2(8) | N |  |  |
| 12 | **IS_FUNCTION** | CHAR(1) | Y | 'N' |  |

- **Primary key** `DEF_FS_ELEMENT_DETAIL_PK` (ELEMENT_CODE, SR_NO)

### DEF_FS_SALARY_ELEMENTS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ELEMENTS** 🔑 | VARCHAR2(8) | N |  |  |
| 2 | **AMOUNT** | NUMBER | Y |  |  |

- **Primary key** `PK_DEF_FS_SALARY_ELEMENTS` (ELEMENTS)

### DEF_FS_WORKFLOW_Q

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** | VARCHAR2(9) | N |  |  |
| 2 | **WFE_NO** | NUMBER(3) | N |  |  |
| 3 | **ASSIGNEE_MRNO** | VARCHAR2(14) | N |  |  |


### DEF_GL_SETUP_DETAIL

This table is used to define different setups for automatic payroll jornal voucher

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GL_SETUP_CODE** 🔑 → `PAYROLL.DEF_GL_SETUP_MASTER` | CHAR(3) | N |  | PK-self explainatory |
| 2 | **SERIAL_NO** 🔑 | NUMBER(3) | N |  | Part of PK |
| 3 | **STATIC_DESCRIPTION** | VARCHAR2(20) | Y |  | To defince static fields of setup |
| 4 | **AD_CODE** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | Y |  | Allowance or deduction code |
| 5 | **LOAN_CODE** | CHAR(3) | Y |  | Loan type |
| 6 | **COA_CODE_DR** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 7 | **LEDGER_TYPE_CODE_DR** → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 8 | **SUB_LDGR_ITEM_CODE_DR** → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 9 | **COA_CODE_CR** | VARCHAR2(100) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 10 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 11 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 12 | **TRANSACTION_TYPE** | CHAR(1) | Y | 'O' | Either "S" for Static or "L" for Loan or "A" for Allowances or "D" for Deductions or "O" for Others |
| 13 | **STATIC_TYPE** | CHAR(1) | Y |  | Either "G" for Gross Salary or "O" for Overtime or "N" for Night Allowance or "P" for PF-Employer |
| 14 | **ARREAR_CODE** → `PAYROLL.DEF_ARREAR` | CHAR(3) | Y |  |  |
| 15 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 18 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 19 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 20 | **TRN_DATE** | DATE | Y |  |  |
| 21 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 22 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 23 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 24 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 25 | **EXPENSE_CODE** | VARCHAR2(3) | Y |  |  |
| 26 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 27 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 28 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 29 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_S_GL_SETUP_DETAIL` (GL_SETUP_CODE, SERIAL_NO)
- **FK** `FK_DEF_GL_SETUP_DETAIL` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **FK** `FK_DEF_GL_SETUP_DETAIL_1` (ARREAR_CODE) → `PAYROLL.DEF_ARREAR` (ARREAR_CODE) _DISABLED_
- **FK** `FK_S_GL_SETUP_DETAIL_3` (LEDGER_TYPE_CODE_DR, SUB_LDGR_ITEM_CODE_DR) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) _DISABLED_
- **FK** `FK_S_GL_SETUP_DETAIL_4` (COA_CODE_DR) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **FK** `FK_S_GL_SETUP_DETAIL_5` (GL_SETUP_CODE) → `PAYROLL.DEF_GL_SETUP_MASTER` (GL_SETUP_CODE)
- **Check** `CK_S_GL_SETUP_DETAIL_3`: `(TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O', 'R', 'E'))`
- **Index** `IDX_DEF_GL_SETUP_DETAIL_1` (AD_CODE)
- **Index** `IDX_DEF_GL_SETUP_DETAIL_2` (LOAN_CODE)
- **Index** `IDX_DEF_GL_SETUP_DETAIL_3` (LEDGER_TYPE_CODE_DR, SUB_LDGR_ITEM_CODE_DR)
- **Index** `IDX_DEF_GL_SETUP_DETAIL_4` (COA_CODE_DR)
- **Triggers**: `DEF_GL_SETUP_DETAIL_DEL` (AFTER DELETE), `DEF_GL_SETUP_DETAIL_INS` (BEFORE INSERT), `DEF_GL_SETUP_DETAIL_UPD` (BEFORE UPDATE)

### DEF_GL_SETUP_DETAIL_FS

This table is used to define different setups for automatic payroll final settlement jornal voucher

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GL_SETUP_CODE** 🔑 → `PAYROLL.DEF_GL_SETUP_MASTER` | CHAR(3) | N |  | PK-self explainatory |
| 2 | **SERIAL_NO** | NUMBER(3) | N |  | Part of PK |
| 3 | **ELEMENT_CODE** 🔑 → `PAYROLL.DEF_FS_ELEMENT` | VARCHAR2(8) | N |  | Final settlement Elements code |
| 4 | **COA_CODE_DR** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 5 | **LEDGER_TYPE_CODE_DR** → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 6 | **SUB_LDGR_ITEM_CODE_DR** → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | Y |  | PK-self explainatory (To entertain Dr entries) |
| 7 | **COA_CODE_CR** | VARCHAR2(100) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 8 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 9 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  | PK-self explainatory (To entertain Cr entries) |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_GL_SETUP_DETAIL_FS` (GL_SETUP_CODE, ELEMENT_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS` (ELEMENT_CODE) → `PAYROLL.DEF_FS_ELEMENT` (ELEMENT_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_1` (LEDGER_TYPE_CODE_DR, SUB_LDGR_ITEM_CODE_DR) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_2` (COA_CODE_DR) → `FINANCE.GL_COA` (COA_CODE)
- **FK** `FK_DEF_GL_SETUP_DETAIL_FS_3` (GL_SETUP_CODE) → `PAYROLL.DEF_GL_SETUP_MASTER` (GL_SETUP_CODE)
- **Triggers**: `DEF_GL_SETUP_DETAIL_FS_DEL` (AFTER DELETE), `DEF_GL_SETUP_DETAIL_FS_INS` (BEFORE INSERT), `DEF_GL_SETUP_DETAIL_FS_UPD` (BEFORE UPDATE)

### DEF_GL_VOUCHER

This table is used to define different setups for payroll jornal voucher

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GL_SETUP_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  | Name of  Voucher Setup i.e. (Finance, Pathology, MIS etc.) |
| 3 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 4 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 10 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 11 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 12 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_GL_VOUCHER_01` (GL_SETUP_CODE)
- **UNIQUE Index** `SYS_C008646` (GL_SETUP_CODE)
- **Triggers**: `DEF_GL_VOUCHER_DEL` (AFTER DELETE), `DEF_GL_VOUCHER_INS` (BEFORE INSERT), `DEF_GL_VOUCHER_UPD` (BEFORE UPDATE)

### DEF_PERCENTAGE_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PERCENTAGE_SETUP_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(250) | Y |  |  |
| 3 | **MINIMUM_VALUE** | NUMBER(20,2) | Y |  |  |
| 4 | **MAX_VALUE** | NUMBER(20,2) | Y |  |  |
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

- **Primary key** `PK_DEF_PERCENTAGE_SETUP` (PERCENTAGE_SETUP_ID)
- **Referenced by**: `DEF_GRADE_WISE_PERCENTAGE`
- **Triggers**: `DEF_PERCENTAGE_SETUP_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PERCENTAGE_SETUP_DEL` (AFTER DELETE), `DEF_PERCENTAGE_SETUP_INS` (BEFORE INSERT), `DEF_PERCENTAGE_SETUP_UPD` (BEFORE UPDATE), `TRG_WS_FJA_HA_AY_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_GRADE_WISE_PERCENTAGE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PERCENTAGE_SETUP_ID** 🔑 → `PAYROLL.DEF_PERCENTAGE_SETUP` | VARCHAR2(3) | N |  |  |
| 2 | **GRADE_ID** 🔑 | VARCHAR2(6) | N |  |  |
| 3 | **PERCENTAGE** | NUMBER(5,2) | Y |  |  |
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

- **Primary key** `PK_DEF_GRADE_WISE_PERCENTAGE` (PERCENTAGE_SETUP_ID, GRADE_ID)
- **FK** `FK_DEF_GRADE_PERCENT_01` (PERCENTAGE_SETUP_ID) → `PAYROLL.DEF_PERCENTAGE_SETUP` (PERCENTAGE_SETUP_ID)
- **Triggers**: `DEF_GRADE_WISE_PERCENTAGE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_GRADE_WISE_PERCENTAGE_DEL` (AFTER DELETE), `DEF_GRADE_WISE_PERCENTAGE_INS` (BEFORE INSERT), `DEF_GRADE_WISE_PERCENTAGE_UPD` (BEFORE UPDATE), `TRG_WS_FLB_GV_CW_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_INCREMENT_TYPE

This table is used to define different types of increments such as Annual, promotional etc.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **INCREMENT_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of increment |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short Name of increment |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **INCREASE_STAGE** | CHAR(1) | Y | 'N' |  |
| 12 | **NO_OF_JOB_MONTH** | NUMBER(2) | Y |  | Number of months that must be completed to be part of this increment |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_INCREMENT_TYPE` (INCREMENT_CODE)
- **Check** `CK_DEF_INCREMENT_TYPE_1`: `(ACTIVE IN ('Y', 'N'))`
- **Referenced by**: `EMP_INCREMENT_MASTER`, `PROCESS_INCREMENT_MASTER`
- **Triggers**: `DEF_INCREMENT_TYPE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_INCREMENT_TYPE_DEL` (AFTER DELETE), `DEF_INCREMENT_TYPE_INS` (BEFORE INSERT), `DEF_INCREMENT_TYPE_UPD` (BEFORE UPDATE), `TRG_WS_LHW_SF_PB_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_ITAX_ADJUSTMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ADJUSTMENT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(100) | Y |  |  |
| 3 | **ADJUSTMENT_TYPE** | CHAR(1) | Y | 'A' | 'A' FOR ADJUSTMENT, 'C' FOR CREDITS |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
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
| 15 | **CALC_TYPE** | CHAR(1) | N | 'M' |  |
| 16 | **AMOUNT_LIMIT** | NUMBER(15) | Y |  |  |
| 17 | **PERCENT_LIMIT** | NUMBER(5,2) | Y |  |  |

- **Primary key** `PK_DEF_ITAX_ADJUSTMENT` (ADJUSTMENT_CODE)
- **Check** `CK_DEF_ITAX_ADJUSTMENT`: `(ACTIVE IN ('Y','N'))`
- **Triggers**: `DEF_ITAX_ADJUSTMENT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_NEL_OY_ZL_Q` (AFTER INSERT OR UPDATE OR DELETE)

### PAY_FINANCIAL_YEAR

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 2 | **FROM_DATE** | DATE | N |  |  |
| 3 | **YEAR_DESCRIPTION** | VARCHAR2(25) | N |  |  |
| 4 | **TO_DATE** | DATE | N |  |  |
| 5 | **YEAR_STATUS** | CHAR(1) | Y |  |  |
| 6 | **CURRENT_YEAR** | CHAR(1) | Y | 'N' |  |
| 7 | **EXEMPT_AGE_MALE** | NUMBER(3) | N | 60 |  |
| 8 | **EXEMPT_AGE_FEMALE** | NUMBER(3) | N | 55 |  |
| 9 | **EXEMPT_TAX_PERCENTAGE_MALE** | NUMBER(5,2) | N | 50 |  |
| 10 | **EXEMPT_TAX_PERCENTAGE_FEMALE** | NUMBER(5,2) | N | 50 |  |
| 11 | **EXEMPT_TAX_AMOUNT_MALE** | NUMBER(10) | Y |  |  |
| 12 | **EXEMPT_TAX_AMOUNT_FEMALE** | NUMBER(10) | Y |  |  |
| 13 | **GENERAL_EXEMPTION_AMOUNT** | NUMBER(10) | N | 100000 |  |
| 14 | **CALCULATION_MODE** | NUMBER(1) | N | 2 | 1 for Allowance Based Tax System 2 for Gross Based Tax System |
| 15 | **MIN_TAX_DEDUCTION** | NUMBER(10) | Y |  |  |
| 16 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **TRN_DATE** | DATE | Y |  |  |
| 19 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 20 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 21 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 22 | **MARGINAL_RELIEF** | CHAR(1) | Y | 'N' |  |
| 23 | **PF_EXEMPT_PCTAGE** | NUMBER(5,2) | Y |  |  |
| 24 | **PF_TAXABLE_CONTRIBUTION** | NUMBER(10) | Y |  |  |
| 25 | **PF_EXEMPT_BASE** | CHAR(1) | Y | 'G' |  |
| 26 | **ITAX_SURCHARGE** | NUMBER(5,2) | Y | 0 |  |
| 27 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 28 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 29 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 30 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **Check** `CK_PAY_FINANCIAL_YEAR_1`: `(YEAR_STATUS IN ('O', 'C', 'S'))`
- **Check** `CK_PAY_FINANCIAL_YEAR_2`: `(CURRENT_YEAR IN ('Y', 'N'))`
- **Check** `CK_PAY_FINANCIAL_YEAR_3`: `(FROM_DATE = TRUNC(FROM_DATE))`
- **Check** `CK_PAY_FINANCIAL_YEAR_4`: `(TO_DATE = TRUNC(TO_DATE))`
- **Check** `CK_PAY_FINANCIAL_YEAR_5`: `(marginal_relief in( 'Y','N'))`
- **Check** `CK_PAY_FINANCIAL_YEAR_6`: `(PF_EXEMPT_BASE IN ('G', 'B'))`
- **Referenced by**: `DEF_ITAX_DETAIL_AD`, `DEF_ITAX_MR_SLAB`, `DEF_ITAX_SLAB`, `EMP_ITAX_ADJUSTMENT_MONTHLY`, `EMP_ITAX_ADJUSTMENT`
- **Triggers**: `PAY_FINANCIAL_YEAR_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `PAY_FINANCIAL_YEAR_DEL` (AFTER DELETE), `PAY_FINANCIAL_YEAR_INS` (BEFORE INSERT), `PAY_FINANCIAL_YEAR_UPD` (BEFORE UPDATE), `TRG_WS_WNQ_VQ_RO_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_ITAX_DETAIL_AD

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.PAY_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 2 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 3 | **TAXABLE** | CHAR(1) | N | 'Y' |  |
| 4 | **GROSS_BASIC_OTHER** | CHAR(1) | N | 'B' |  |
| 5 | **EXEMPT_PERCENT** | NUMBER(5,2) | Y |  |  |
| 6 | **MAX_EXEMPT_LIMIT** | NUMBER(10) | N | 0 |  |
| 7 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 8 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 10 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 11 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
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

- **Primary key** `PK_DEF_ITAX_DETAIL_AD` (YEAR_CODE, AD_CODE)
- **FK** `DEF_ITAX_DETAIL_AD_1` (YEAR_CODE) → `PAYROLL.PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **FK** `FK_DEF_ITAX_DETAIL_AD` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **Check** `CK_DEF_ITAX_DETAIL_AD_001`: `(TAXABLE IN ('Y','N'))`
- **Check** `CK_DEF_ITAX_DETAIL_AD_002`: `(GROSS_BASIC_OTHER IN ('B','G','O'))`
- **Check** `CK_DEF_ITAX_DETAIL_AD_003`: `(ACTIVE IN ('Y','N'))`
- **Triggers**: `DEF_ITAX_DETAIL_AD_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_ACE_JF_AP_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_ITAX_MR_SLAB

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.PAY_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 2 | **FROM_SALARY_RANGE** 🔑 | NUMBER(10) | N | 0 |  |
| 3 | **TO_SALARY_RANGE** 🔑 | NUMBER(10) | N | 9999999999 |  |
| 4 | **TAX_PERCENT** | NUMBER(5,2) | N |  |  |
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

- **Primary key** `PK_DEF_ITAX_MR_SLAB` (YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE)
- **Unique** `UK_DEF_ITAX_MR_SLAB_1` (YEAR_CODE, FROM_SALARY_RANGE)
- **FK** `FK_DEF_ITAX_MR_SLAB_1` (YEAR_CODE) → `PAYROLL.PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **Triggers**: `DEF_ITAX_MR_SLAB_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_KSE_EA_UF_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_ITAX_SLAB

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.PAY_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 2 | **FROM_SALARY_RANGE** 🔑 | NUMBER(10) | N | 0 |  |
| 3 | **TO_SALARY_RANGE** 🔑 | NUMBER(10) | N | 9999999999 |  |
| 4 | **BASE_TAX_AMOUNT** | NUMBER(10) | N | 0 |  |
| 5 | **TAX_PERCENT** | NUMBER(5,2) | N |  |  |
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

- **Primary key** `PK_DEF_ITAX_SLAB` (YEAR_CODE, FROM_SALARY_RANGE, TO_SALARY_RANGE)
- **Unique** `UK_DEF_ITAX_SLAB_1` (YEAR_CODE, FROM_SALARY_RANGE)
- **FK** `FK_DEF_ITAX_SLAB_1` (YEAR_CODE) → `PAYROLL.PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **Triggers**: `DEF_ITAX_SLAB_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `TRG_WS_LIC_JY_WB_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_LETTER_TYPE

This table is used to define different letter types

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LETTER_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Type of the letter i.e. joining, experience, termination etc. |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short name of the |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
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

- **Primary key** `PK_DEF_LETTER_TYPE` (LETTER_CODE)
- **Check** `CK_DEF_LETTER_TYPE_1`: `(ACTIVE IN ('Y', 'N'))`
- **Referenced by**: `DEF_LETTER_TEMPLATE`
- **Triggers**: `DEF_LETTER_TYPE_DEL` (AFTER DELETE), `DEF_LETTER_TYPE_INS` (BEFORE INSERT), `DEF_LETTER_TYPE_UPD` (BEFORE UPDATE)

### DEF_LETTER_TEMPLATE

This table is used to define different letter templates to be issued to employees such as joining, experience etc.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **TEMPLATE_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **LETTER_CODE** → `PAYROLL.DEF_LETTER_TYPE` | CHAR(3) | Y |  | Letter type |
| 3 | **DESCRIPTION** | VARCHAR2(255) | Y |  | Template name |
| 4 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short name for the Template |
| 5 | **TEMPLATE_HEADER** | VARCHAR2(4000) | Y |  | Header text for template |
| 6 | **INNER_TEXT** | VARCHAR2(4000) | Y |  | Internal text for template |
| 7 | **FOOTER** | VARCHAR2(4000) | Y |  | Footer text for template |
| 8 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
| 9 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_LETTER_TEMPLATE` (TEMPLATE_CODE)
- **FK** `FK_DEF_LETTER_TEMPLATE_1` (LETTER_CODE) → `PAYROLL.DEF_LETTER_TYPE` (LETTER_CODE)
- **Check** `CK_DEF_LETTER_TEMPLATE_1`: `(ACTIVE IN ('Y', 'N'))`
- **Index** `IDX_DEF_LETTER_TEMPLATE_1` (LETTER_CODE)

### DEF_LIABILITY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LIABILITY_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  |  |
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

- **Primary key** `PK_DEF_LIABILITY` (LIABILITY_CODE)
- **Referenced by**: `EMP_LIABILITY`
- **Triggers**: `DEF_LIABILITY_DEL` (AFTER DELETE), `DEF_LIABILITY_INS` (BEFORE INSERT), `DEF_LIABILITY_UPD` (BEFORE UPDATE)

### DEF_LOAN_INTEREST_RATE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **YEAR_CODE** 🔑 → `FINANCE.PF_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 3 | **INTEREST_RATE** | NUMBER(5,2) | Y |  |  |
| 4 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 5 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
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

- **Primary key** `PK_DEF_LOAN_INTEREST_RATE` (LOAN_CODE, YEAR_CODE, LOCATION_ID, ORGANIZATION_ID)
- **FK** `FK_DEF_LOAN_INTEREST_RATE_1` (YEAR_CODE) → `FINANCE.PF_FINANCIAL_YEAR` (YEAR_CODE) _DISABLED_
- **Triggers**: `DEF_LOAN_INTEREST_RATE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_LOAN_INTEREST_RATE_DEL` (AFTER DELETE), `DEF_LOAN_INTEREST_RATE_INS` (BEFORE INSERT), `DEF_LOAN_INTEREST_RATE_UPD` (BEFORE UPDATE), `TRG_WS_OLB_LH_ZZ_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_LOAN_TYPE

This table is used to define different types of loan such as Advance against salary, Car loan, house loan etc.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_CODE** 🔑 | CHAR(3) | N |  | PK-self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  | Name of the loan Type |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short name of the loan Type, to be used in salary sheets |
| 4 | **MEDICAL_OTHER** | CHAR(1) | Y | 'O' | Is this medical advance or other |
| 5 | **INSTALLMENT_ALLOW** | CHAR(1) | Y | 'Y' | Installments allowed against this advance or not |
| 6 | **DEDUCTION_FROM_SALARY** | CHAR(1) | Y | 'Y' | Deduction from salary is valid against this record or not |
| 7 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
| 8 | **LEDGER_TYPE_CODE** → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | Y |  | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| 9 | **SUB_LDGR_ITEM_CODE** → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | Y |  | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| 10 | **COA_CODE** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  | GL Code to link with Loan Code (For automatic entry no loan transaction) |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORGANIZATION_ID** 🔑 → `DEFINITIONS.ORGANIZATION` | VARCHAR2(3) | N |  |  |
| 18 | **LOCATION_ID** 🔑 → `DEFINITIONS.LOCATION` | VARCHAR2(3) | N |  |  |
| 19 | **LEDGER_TYPE_CODE_DEBIT** | NUMBER(4) | Y |  | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| 20 | **SUB_LDGR_ITEM_CODE_DEBIT** | VARCHAR2(18) | Y |  | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| 21 | **COA_CODE_DEBIT** | VARCHAR2(100) | Y |  | This column will be used for Payroll JV loan DR. (GL setup code will not be used for Loan DR) |
| 22 | **REFUND_WITH_PAY_VOUCHER** | CHAR(1) | Y |  |  |
| 23 | **REFUND_AD_CODE** | CHAR(3) | Y |  |  |
| 24 | **SALARY_DEDUCTION_TYPE** | CHAR(1) | N | 'D' | D Direct, A Arrear, R Deduction |
| 25 | **INT_LEDGER_TYPE_CODE** | NUMBER(4) | Y |  |  |
| 26 | **INT_SUB_LDGR_ITEM_CODE** | VARCHAR2(18) | Y |  |  |
| 27 | **INT_COA_CODE** | VARCHAR2(100) | Y |  |  |
| 28 | **REFUND_THROUGH_RECEIPT** | CHAR(1) | Y | 'N' | This column specify if direct refund is permitted or receipt is required |
| 29 | **INTEREST** | CHAR(1) | Y |  |  |
| 30 | **INT_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 31 | **GAP_DAYS** | NUMBER(3) | Y |  | No of days gap between the loans of an employee |
| 32 | **ALLOW_MULTIPLE_LOANS** | CHAR(1) | N | 'Y' |  |
| 33 | **DEFER_INT_VOUCHER** | CHAR(1) | N | on null 'N' | If yes then loan markup voucher will not be generated with loan voucher |
| 34 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 35 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 36 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 37 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 38 | **DISP_ON_SALARY_SLIP** | CHAR(1) | Y | 'N' |  |

- **Primary key** `PK_DEF_LOAN_TYPE` (LOAN_CODE, ORGANIZATION_ID, LOCATION_ID)
- **FK** `FK_DEF_LOAN1` (LOCATION_ID) → `DEFINITIONS.LOCATION` (LOCATION_ID) _DISABLED_
- **FK** `FK_DEF_LOAN_1` (ORGANIZATION_ID) → `DEFINITIONS.ORGANIZATION` (ORGANIZATION_ID) _DISABLED_
- **FK** `FK_DEF_LOAN_TYPE_1` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) _DISABLED_
- **FK** `FK_DEF_LOAN_TYPE_2` (COA_CODE) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **Check** `CK_DEF_LOAN_TYPE_1`: `(MEDICAL_OTHER IN ('M', 'O'))`
- **Check** `CK_DEF_LOAN_TYPE_2`: `(INSTALLMENT_ALLOW IN ('Y', 'N'))`
- **Check** `CK_DEF_LOAN_TYPE_3`: `(DEDUCTION_FROM_SALARY IN ('Y', 'N'))`
- **Check** `CK_DEF_LOAN_TYPE_4`: `(ACTIVE IN ('Y', 'N'))`
- **Index** `IDX_DEF_LOAN_TYPE_1` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **Index** `IDX_DEF_LOAN_TYPE_2` (COA_CODE)
- **Triggers**: `DEF_LOAN_TYPE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_LOAN_TYPE_DEL` (AFTER DELETE), `DEF_LOAN_TYPE_INS` (BEFORE INSERT), `DEF_LOAN_TYPE_UPD` (BEFORE UPDATE), `TRG_WS_IAP_QA_QL_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_LOAN_TYPE_CONSTANT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_CODE** 🔑 | CHAR(3) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(255) | N |  |  |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  |  |
| 4 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **TRN_DATE** | DATE | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **MODULE** | VARCHAR2(2) | Y |  | PF, GL, CP, GP |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_LOAN_CONST` (LOAN_CODE)
- **Triggers**: `DEF_LOAN_TYPE_CONSTANT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_LOAN_TYPE_CONSTANT_DEL` (AFTER DELETE), `DEF_LOAN_TYPE_CONSTANT_INS` (BEFORE INSERT), `DEF_LOAN_TYPE_CONSTANT_UPD` (BEFORE UPDATE), `TRG_WS_YTS_VH_XA_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_MONTH_CHANGE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ID** 🔑 | NUMBER | N |  |  |
| 2 | **REPORT_NAME** | VARCHAR2(200) | Y |  |  |
| 3 | **TABLE_NAME** | VARCHAR2(200) | Y |  |  |
| 4 | **WHERE_CLAUSE** | CLOB | Y |  |  |
| 5 | **UPDATE_COLUMN** | VARCHAR2(2000) | Y |  |  |
| 6 | **ACTIVE_FLAG** | CHAR(1) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_MONTH_CHANGE` (ID)
- **Triggers**: `DEF_MONTH_CHANGE_DEL` (AFTER DELETE), `DEF_MONTH_CHANGE_INS` (BEFORE INSERT), `DEF_MONTH_CHANGE_UPD` (BEFORE UPDATE)

### DEF_PAYROLL_LOCATION

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **PAYROLL_LOCATION_ID** 🔑 | VARCHAR2(3) | N |  | The location on which pay process is to be executed |
| 3 | **EMP_LOCATION_ID** 🔑 | VARCHAR2(3) | N |  | The locations of employees which are grouped with payroll location |
| 4 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 5 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **TRN_DATE** | DATE | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_PAYROLL_LOCATION` (ORGANIZATION_ID, PAYROLL_LOCATION_ID, EMP_LOCATION_ID)
- **Unique** `UK_DEF_PAYROLL_LOCATION` (ORGANIZATION_ID, EMP_LOCATION_ID)
- **Triggers**: `DEF_PAYROLL_LOCATION_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAYROLL_LOCATION_DEL` (AFTER DELETE), `DEF_PAYROLL_LOCATION_INS` (BEFORE INSERT), `DEF_PAYROLL_LOCATION_UPD` (BEFORE UPDATE), `TRG_WS_VTC_YQ_HK_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAYROLL_WORKFLOW

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **SCHEMA_ID** | VARCHAR2(3) | N |  |  |
| 4 | **WORKFLOW_TYPE_ID** | NUMBER(3) | N |  |  |
| 5 | **WORK_FLOW_ID** | NUMBER(4) | N |  |  |
| 6 | **TYPE** 🔑 | VARCHAR2(2) | N |  |  |
| 7 | **ACTIVE** | VARCHAR2(1) | N | 'Y' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_DEF_PAYROLL_WORKFLOW` (LOCATION_ID, TYPE)
- **Triggers**: `DEF_PAYROLL_WORKFLOW_DEL` (AFTER DELETE), `DEF_PAYROLL_WORKFLOW_INS` (BEFORE INSERT), `DEF_PAYROLL_WORKFLOW_UPD` (BEFORE UPDATE)

### DEF_PAYSCALE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 2 | **GRADE_ID** 🔑 | VARCHAR2(6) | N |  |  |
| 3 | **MIN_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 4 | **MAX_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 5 | **INCREMENT_AMOUNT** | NUMBER(10,2) | Y |  |  |
| 6 | **ACTIVE** | CHAR(1) | Y |  |  |
| 7 | **MIN_STAGE_NO** | NUMBER(2) | Y |  |  |
| 8 | **MAX_STAGE_NO** | NUMBER(2) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_PAYSCALE` (YEAR_CODE, GRADE_ID)
- **Referenced by**: `DEF_PAYSCALE_DETAIL`
- **Triggers**: `DEF_PAYSCALE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAYSCALE_DEL` (AFTER DELETE), `DEF_PAYSCALE_INS` (BEFORE INSERT), `DEF_PAYSCALE_UPD` (BEFORE UPDATE), `TRG_WS_MCF_WK_WX_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAYSCALE_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.DEF_PAYSCALE` | NUMBER(4) | N |  |  |
| 2 | **GRADE_ID** 🔑 → `PAYROLL.DEF_PAYSCALE` | VARCHAR2(6) | N |  |  |
| 3 | **STAGE_NO** 🔑 | NUMBER(2) | N |  |  |
| 4 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
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

- **Primary key** `PK_DEF_PAYSCALE_DETAIL` (YEAR_CODE, GRADE_ID, STAGE_NO)
- **FK** `FK_DEF_PAYSCALE_DETAIL1` (YEAR_CODE, GRADE_ID) → `PAYROLL.DEF_PAYSCALE` (YEAR_CODE, GRADE_ID) _DISABLED_
- **Triggers**: `DEF_PAYSCALE_DETAIL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAYSCALE_DETAIL_DEL` (AFTER DELETE), `DEF_PAYSCALE_DETAIL_INS` (BEFORE INSERT), `DEF_PAYSCALE_DETAIL_UPD` (BEFORE UPDATE), `TRG_WS_SAN_MB_CF_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAY_VOUCHER_LOCATION

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_VOUCHER_TYPE** 🔑 | VARCHAR2(2) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **EMP_LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
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

- **Primary key** `PK_DEF_PAY_VOUCHER_LOCATION` (PAY_VOUCHER_TYPE, LOCATION_ID, EMP_LOCATION_ID)
- **Triggers**: `DEF_PAY_VOUCHER_LOCATION_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAY_VOUCHER_LOCATION_DEL` (AFTER DELETE), `DEF_PAY_VOUCHER_LOCATION_INS` (BEFORE INSERT), `DEF_PAY_VOUCHER_LOCATION_UPD` (BEFORE UPDATE), `TRG_WS_MYU_RJ_JI_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAY_VOUCHER_TYPE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_VOUCHER_TYPE** 🔑 | VARCHAR2(2) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(250) | Y |  |  |
| 3 | **CATEGORY** | VARCHAR2(2) | Y |  | GL or PF |
| 4 | **ACTIVE** | CHAR(1) | N | 'N' |  |
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

- **Primary key** `PK_DEF_PAY_VOUCHER_TYPE` (PAY_VOUCHER_TYPE)
- **Referenced by**: `DEF_PAY_VOUCHER_SETUP`
- **Triggers**: `DEF_PAY_VOUCHER_TYPE_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAY_VOUCHER_TYPE_DEL` (AFTER DELETE), `DEF_PAY_VOUCHER_TYPE_INS` (BEFORE INSERT), `DEF_PAY_VOUCHER_TYPE_UPD` (BEFORE UPDATE), `TRG_WS_GXP_UF_OU_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAY_VOUCHER_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_VOUCHER_SETUP_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **PAY_VOUCHER_TYPE** → `PAYROLL.DEF_PAY_VOUCHER_TYPE` | VARCHAR2(2) | Y |  |  |
| 3 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 4 | **EMP_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 5 | **DEDUCTION_AD_CODE** | VARCHAR2(3) | Y |  |  |
| 6 | **COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 7 | **LEDGER_TYPE_CODE_DR** | NUMBER(4) | Y |  |  |
| 8 | **SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **MERGE_PROFIT_ON_YEAREND** | VARCHAR2(100) | Y |  |  |
| 16 | **PRFT_COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 17 | **PRFT_LEDGER_TYPE_CODE_DR** | NUMBER(4) | Y |  |  |
| 18 | **PRFT_SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |
| 19 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 20 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 21 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 22 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_PAY_VOUCHER_SETUP` (PAY_VOUCHER_SETUP_ID)
- **FK** `FK_DEF_PAY_VOUCHER_SETUP` (PAY_VOUCHER_TYPE) → `PAYROLL.DEF_PAY_VOUCHER_TYPE` (PAY_VOUCHER_TYPE) _DISABLED_
- **Referenced by**: `DEF_PAY_VOUCHER_SETUP_DTL`
- **Triggers**: `DEF_PAY_VOUCHER_SETUP_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAY_VOUCHER_SETUP_DEL` (AFTER DELETE), `DEF_PAY_VOUCHER_SETUP_INS` (BEFORE INSERT), `DEF_PAY_VOUCHER_SETUP_PK` (BEFORE INSERT), `DEF_PAY_VOUCHER_SETUP_UPD` (BEFORE UPDATE), `TRG_WS_BLA_PZ_PG_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PAY_VOUCHER_SETUP_DTL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_VOUCHER_SETUP_ID** 🔑 → `PAYROLL.DEF_PAY_VOUCHER_SETUP` | VARCHAR2(3) | N |  |  |
| 2 | **SRNO** 🔑 | NUMBER(2) | N |  |  |
| 3 | **DESCRIPTION** | VARCHAR2(250) | Y |  |  |
| 4 | **COA_CODE_CR** | VARCHAR2(100) | Y |  |  |
| 5 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  |  |
| 6 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  |  |
| 7 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **PRFT_COA_CODE_CR** | VARCHAR2(100) | Y |  |  |
| 15 | **PRFT_LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  |  |
| 16 | **PRFT_SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_PAY_VOUCHER_SETUP_DTL` (PAY_VOUCHER_SETUP_ID, SRNO)
- **FK** `FK_DEF_PAY_VOUCHER_SETUP_DTL1` (PAY_VOUCHER_SETUP_ID) → `PAYROLL.DEF_PAY_VOUCHER_SETUP` (PAY_VOUCHER_SETUP_ID)
- **Triggers**: `DEF_PAY_VOUCHER_SETUP_DTL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PAY_VOUCHER_SETUP_DTL_DEL` (AFTER DELETE), `DEF_PAY_VOUCHER_SETUP_DTL_INS` (BEFORE INSERT), `DEF_PAY_VOUCHER_SETUP_DTL_UPD` (BEFORE UPDATE), `TRG_WS_LRB_SM_CW_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_PF_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **COA_CODE_EMPLOYEE_CONT** 🔑 → `FINANCE.GL_COA` | VARCHAR2(100) | N |  |  |
| 2 | **COA_CODE_EMPLOYER_CONT** | VARCHAR2(100) | Y |  |  |
| 3 | **COA_CODE_SKMT_CONT** | VARCHAR2(100) | Y |  |  |
| 4 | **LEDGER_TYPE_CODE_CONT** → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | Y |  |  |
| 5 | **SUB_LDGR_ITEM_CODE_CONT** → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | Y |  |  |
| 6 | **COA_CODE_EMPLOYEE_LOAN** | VARCHAR2(100) | Y |  |  |
| 7 | **COA_CODE_SKMT_LOAN** | VARCHAR2(100) | Y |  |  |
| 8 | **LEDGER_TYPE_CODE_LOAN** | NUMBER(4) | Y |  |  |
| 9 | **SUB_LDGR_ITEM_CODE_LOAN** | VARCHAR2(18) | Y |  |  |
| 10 | **COA_CODE_EMP_PROFIT** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  |  |
| 11 | **COA_CODE_SKMT_PROFIT** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  |  |
| 12 | **COA_CODE_PL** → `FINANCE.GL_COA` | VARCHAR2(100) | Y |  |  |
| 13 | **LEDGER_TYPE_CODE_PL** → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | Y |  |  |
| 14 | **SUB_LDGR_ITEM_CODE_PL** → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | Y |  |  |
| 15 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 18 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 19 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 20 | **TRN_DATE** | DATE | Y |  |  |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 24 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_PF_SETUP` (COA_CODE_EMPLOYEE_CONT)
- **FK** `FK_DEF_PF_SETUP_1` (LEDGER_TYPE_CODE_CONT, SUB_LDGR_ITEM_CODE_CONT) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) _DISABLED_
- **FK** `FK_DEF_PF_SETUP_2` (COA_CODE_EMPLOYEE_CONT) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **FK** `FK_DEF_PF_SETUP_3` (LEDGER_TYPE_CODE_PL, SUB_LDGR_ITEM_CODE_PL) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) _DISABLED_
- **FK** `FK_DEF_PF_SETUP_4` (COA_CODE_EMP_PROFIT) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **FK** `FK_DEF_PF_SETUP_5` (COA_CODE_SKMT_PROFIT) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **FK** `FK_DEF_PF_SETUP_6` (COA_CODE_PL) → `FINANCE.GL_COA` (COA_CODE) _DISABLED_
- **Index** `IDX_DEF_PF_SETUP_1` (LEDGER_TYPE_CODE_CONT, SUB_LDGR_ITEM_CODE_CONT)
- **Index** `IDX_DEF_PF_SETUP_2` (COA_CODE_EMPLOYEE_CONT)
- **Triggers**: `DEF_PF_SETUP_DEL` (AFTER DELETE), `DEF_PF_SETUP_INS` (BEFORE INSERT), `DEF_PF_SETUP_UPD` (BEFORE UPDATE)

### DEF_PROJECT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PROJECT_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 2 | **PROJECT_NAME** | VARCHAR2(1000) | N |  |  |
| 3 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 4 | **PROJECT_TYPE** | VARCHAR2(500) | Y |  |  |
| 5 | **CLIENT_ID** | VARCHAR2(10) | Y |  |  |
| 6 | **CAMPAIGN_ID** | VARCHAR2(12) | Y |  |  |
| 7 | **ACTIVE** | CHAR(1) | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PROJECT_ID` (PROJECT_ID)
- **Referenced by**: `EXPENSE_CLAIM_PROJECT`
- **Triggers**: `DEF_PROJECT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_PROJECT_DEL` (AFTER DELETE), `DEF_PROJECT_INS` (BEFORE INSERT), `DEF_PROJECT_UPD` (BEFORE UPDATE), `TRG_WS_XQB_HY_XD_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_SCHEDULE_WORKFLOW_CC

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_CODE** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **TRANS_TYPE** 🔑 | CHAR(1) | N | 'C' |  |
| 3 | **COST_CENTRE_ID** 🔑 | VARCHAR2(10) | N |  |  |
| 4 | **SCHEMA_ID** | VARCHAR2(3) | N |  |  |
| 5 | **WORKFLOW_TYPE_ID** | NUMBER(3) | N |  |  |
| 6 | **WORK_FLOW_ID** | NUMBER(4) | N |  |  |
| 7 | **EXPENSE_TYPE_ID** | CHAR(1) | N |  |  |
| 8 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_DEF_SCHEDULE_WORKFLOW_CC` (EXPENSE_CODE, TRANS_TYPE, COST_CENTRE_ID)

### DEF_SETUP_CONSTANT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CONSTANT_ID** 🔑 | NUMBER(10) | N |  |  |
| 2 | **DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 3 | **SHORT_DESC** | VARCHAR2(50) | Y |  |  |
| 4 | **ACTIVE** | CHAR(1) | Y |  |  |
| 5 | **MENDATORY** | CHAR(1) | Y |  |  |
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

- **Primary key** `PK_CONST_ID` (CONSTANT_ID)
- **Referenced by**: `DEF_SETUP`
- **Triggers**: `DEF_SETUP_CONSTANT_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_SETUP_CONSTANT_DEL` (AFTER DELETE), `DEF_SETUP_CONSTANT_INS` (BEFORE INSERT), `DEF_SETUP_CONSTANT_UPD` (BEFORE UPDATE), `TRG_WS_IKV_BH_WN_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_SETUP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CONSTANT_ID** 🔑 → `PAYROLL.DEF_SETUP_CONSTANT` | NUMBER | N |  |  |
| 2 | **LOCATION_ID** 🔑 → `DEFINITIONS.LOCATION` | VARCHAR2(3) | N |  |  |
| 3 | **ORGANIZATION_ID** 🔑 → `DEFINITIONS.ORGANIZATION` | VARCHAR2(3) | N |  |  |
| 4 | **VALUE** | VARCHAR2(100) | Y |  |  |
| 5 | **FROM_DATE** | DATE | Y |  |  |
| 6 | **TO_DATE** | DATE | Y |  |  |
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

- **Primary key** `PK_CONSTANT` (CONSTANT_ID, LOCATION_ID, ORGANIZATION_ID)
- **FK** `FK_CONSTANT1` (CONSTANT_ID) → `PAYROLL.DEF_SETUP_CONSTANT` (CONSTANT_ID)
- **FK** `FK_DEF_SETUP_1` (LOCATION_ID) → `DEFINITIONS.LOCATION` (LOCATION_ID) _DISABLED_
- **FK** `FK_DEF_SETUP_2` (ORGANIZATION_ID) → `DEFINITIONS.ORGANIZATION` (ORGANIZATION_ID) _DISABLED_
- **Triggers**: `DEF_SETUP_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_SETUP_DEL` (AFTER DELETE), `DEF_SETUP_INS` (BEFORE INSERT), `DEF_SETUP_UPD` (BEFORE UPDATE), `TRG_WS_NML_BL_RN_Q` (AFTER INSERT OR UPDATE OR DELETE)

### DEF_TAX_AMOUNT_OTHER_THAN_SAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **TAXABLE_AMOUNT_ID** 🔑 | NUMBER(5) | N |  |  |
| 2 | **TAXABLE_DESCRIPTION** | VARCHAR2(500) | Y |  |  |
| 3 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
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

- **Primary key** `PK_TAXABLE_AMOUNT_ID` (TAXABLE_AMOUNT_ID)
- **Referenced by**: `EMP_TAX_AMOUNT_OTHER_THAN_SAL`
- **Triggers**: `DEF_TAX_AMOUNT_OTHER_THAN_SAL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `DEF_TAX_AMOUNT_OTHER_THAN__DEL` (AFTER DELETE), `DEF_TAX_AMOUNT_OTHER_THAN__INS` (BEFORE INSERT), `DEF_TAX_AMOUNT_OTHER_THAN__UPD` (BEFORE UPDATE), `TRG_WS_ALH_HY_ST_Q` (AFTER INSERT OR UPDATE OR DELETE)

### EMPLOYEE_INCOME_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | N |  |  |
| 2 | **PAY_START_DATE** | DATE | N |  |  |
| 3 | **PAY_END_DATE** | DATE | N |  |  |
| 4 | **AD_CODE** | VARCHAR2(50) | Y |  |  |
| 5 | **AMOUNT** | NUMBER(10,2) | N |  |  |
| 6 | **PAYMENT_SOURCE** | VARCHAR2(100) | N |  |  |
| 7 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 8 | **LINE_ITEM** | VARCHAR2(4000) | Y |  |  |
| 9 | **SOURCE** | VARCHAR2(500) | Y |  |  |


### EMPLOYEE_INCOME_DETAIL_FQ

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | N |  |  |
| 2 | **PAY_START_DATE** | DATE | N |  |  |
| 3 | **PAY_END_DATE** | DATE | N |  |  |
| 4 | **AD_CODE** | VARCHAR2(50) | Y |  |  |
| 5 | **AMOUNT** | NUMBER(10,2) | N |  |  |
| 6 | **PAYMENT_SOURCE** | VARCHAR2(100) | N |  |  |
| 7 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 8 | **LINE_ITEM** | VARCHAR2(4000) | Y |  |  |
| 9 | **SOURCE** | VARCHAR2(500) | Y |  |  |


### EMP_ALLOWANCE_DEDUCTION

This table is used to link employees with different types of allowances and deductions

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  | PK- allowance / deduction code |
| 2 | **MRNO** 🔑 → `PAYROLL.DEF_EMP_FINANCIAL` | VARCHAR2(14) | N |  | PK- Employee medical record number |
| 3 | **INITIAL_AMOUNT** | NUMBER(20,2) | Y |  | Value at the service joining time |
| 4 | **CURRENT_AMOUNT** | NUMBER(20,2) | Y |  | Current value |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 14 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EMP_ALLOWANCE_DEDUCTION` (AD_CODE, MRNO)
- **FK** `FK_EMP_ALLOWANCE_DEDUCTION_2` (MRNO) → `PAYROLL.DEF_EMP_FINANCIAL` (MRNO)
- **FK** `FK_EMP_ALLOW_DEDUC` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **Index** `IDX_EMP_ALLOWANCE_DEDUCTION_2` (MRNO)
- **Triggers**: `EMP_ALLOWANCE_DEDUCTION_DEL` (AFTER DELETE), `EMP_ALLOWANCE_DEDUCTION_INS` (BEFORE INSERT), `EMP_ALLOWANCE_DEDUCTION_UPD` (BEFORE UPDATE)

### EMP_ALLOWANCE_DEDUCTION_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **AMOUNT** | NUMBER(10,2) | Y |  |  |
| 4 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 5 | **FROM_DATE** 🔑 | DATE | N |  |  |
| 6 | **TO_DATE** | DATE | Y |  |  |
| 7 | **POSTED** | CHAR(1) | Y | 'N' |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 17 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 18 | **PROCESS_ID** | VARCHAR2(12) | Y |  | Ref to payroll.process_increment_master, if increment is processed through a process |
| 19 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 20 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 21 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 22 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EMP_ALLOWANCE_DED_DETAIL` (AD_CODE, MRNO, FROM_DATE)
- **FK** `FK_EMP_ALLOW_DED` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **Check** `CK_EMP_ALL_DED_DETAIL_1`: `(posted in ('Y','N'))`
- **Triggers**: `EMP_ALLOWANCE_DEDUCTION_DE_DEL` (AFTER DELETE), `EMP_ALLOWANCE_DEDUCTION_DE_INS` (BEFORE INSERT), `EMP_ALLOWANCE_DEDUCTION_DE_UPD` (BEFORE UPDATE)

### EMP_AWARDS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AWARD_ID** 🔑 | VARCHAR2(11) | N |  |  |
| 2 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 3 | **EXPENSE_CODE** | CHAR(3) | Y |  |  |
| 4 | **DUE_DATE** | DATE | Y |  |  |
| 5 | **JOINING_DATE** | DATE | Y |  |  |
| 6 | **ENTRY_DATE** | DATE | Y |  |  |
| 7 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **PAYMENT_BASE** | CHAR(1) | N |  |  |
| 9 | **PAYMENT_RATE** | NUMBER(5,2) | N |  |  |
| 10 | **AWARD_AMOUNT** | NUMBER(20,2) | N |  |  |
| 11 | **ADJ_DUE_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 12 | **ADJ_DUE_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 19 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 21 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 22 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_EMP_AWARDS` (AWARD_ID)
- **Unique** `UK_EMP_AWARDS` (MRNO, DUE_DATE, EXPENSE_CODE)
- **Referenced by**: `EMP_AWARD_PAYMENT`
- **Triggers**: `EMP_AWARDS_DEL` (AFTER DELETE), `EMP_AWARDS_INS` (BEFORE INSERT), `EMP_AWARDS_UPD` (BEFORE UPDATE)

### EMP_AWARD_PAYMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAYMENT_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **AWARD_ID** → `PAYROLL.EMP_AWARDS` | VARCHAR2(11) | Y |  |  |
| 3 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 4 | **BASE_GROSS** | NUMBER(20,2) | N |  |  |
| 5 | **BASE_BASIC** | NUMBER(20,2) | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | N |  |  |
| 7 | **PAYMENT_BY** | VARCHAR2(14) | N |  |  |
| 8 | **PAYMENT_DATE** | DATE | N |  |  |
| 9 | **MON_START_DATE** | DATE | Y |  |  |
| 10 | **MON_END_DATE** | DATE | Y |  |  |
| 11 | **AD_CODE** | VARCHAR2(3) | Y |  |  |
| 12 | **DOCUMENT_NO** | VARCHAR2(12) | Y |  |  |
| 13 | **STATUS_ID** | VARCHAR2(3) | N |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 20 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 21 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 22 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 23 | **WS_SYNC_DATE** | DATE | Y |  |  |

- **Primary key** `PK_EMP_AWARD_PAYMENT` (PAYMENT_ID)
- **FK** `FK_EMP_AWARD_PAYMENT` (AWARD_ID) → `PAYROLL.EMP_AWARDS` (AWARD_ID) _DISABLED_
- **Triggers**: `EMP_AWARD_PAYMENT_DEL` (AFTER DELETE), `EMP_AWARD_PAYMENT_INS` (BEFORE INSERT), `EMP_AWARD_PAYMENT_UPD` (BEFORE UPDATE)

### EMP_EXPENSE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DOCUMENT_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 3 | **VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 4 | **EXPENSE_CODE** | CHAR(3) | N |  |  |
| 5 | **MRNO** → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 6 | **TRANS_DATE** | DATE | N |  |  |
| 7 | **CURRENT_GROSS** | NUMBER(20,2) | Y |  |  |
| 8 | **CURRENT_BASIC** | NUMBER(20,2) | Y |  |  |
| 9 | **CURRENT_LFA** | NUMBER(20,2) | Y |  |  |
| 10 | **SELF_DEPEND** | CHAR(1) | Y | 'N' |  |
| 11 | **DEPENDANT_MRNO** | VARCHAR2(14) | Y |  |  |
| 12 | **APPROVED_BY** | VARCHAR2(25) | Y |  |  |
| 13 | **AMOUNT** | NUMBER(20,2) | N |  |  |
| 14 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 15 | **CANCELLED** | CHAR(1) | Y | 'N' |  |
| 16 | **CANCELED_VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 17 | **CANCELED_VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 18 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 19 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 20 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 21 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 22 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 23 | **TRN_DATE** | DATE | Y |  |  |
| 24 | **LFA_DUE_DATE** | DATE | Y |  |  |
| 25 | **SERVICE_YEARS** | NUMBER(2) | Y |  |  |
| 26 | **BONUS_PERCENT** | NUMBER(5,2) | Y |  |  |
| 27 | **GROSS_BASIC** | CHAR(1) | Y |  |  |
| 28 | **JOINING_DATE** | DATE | Y |  |  |
| 29 | **LONG_SERVICE_DATE** | DATE | Y |  |  |
| 30 | **LFA_ADJUST_NO** | VARCHAR2(12) | Y |  |  |
| 31 | **INCLUDE_IN_TAX** | CHAR(1) | Y |  |  |
| 32 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 33 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 34 | **CLAIM_NO** | VARCHAR2(12) | Y |  |  |
| 35 | **START_DATE** | DATE | Y |  |  |
| 36 | **END_DATE** | DATE | Y |  |  |
| 37 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 38 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 39 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 40 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 41 | **TAX_DEDUCTED** | NUMBER(20,2) | Y |  | This column is added to log manual tax payments |
| 42 | **EXPENSE_LIST_ID** | VARCHAR2(12) | Y |  | Ref to PAYROLL.EMP_EXPENSE_LIST |

- **Primary key** `PK_EMP_EXPENSE` (DOCUMENT_NO)
- **FK** `FK_EMP_EXPENSE_1` (VOUCHER_TYPE, VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_EMP_EXPENSE_2` (CANCELED_VOUCHER_TYPE, CANCELED_VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_EMP_EXPENSE_4` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **Check** `CK_EMP_EXPENSE_1`: `(SELF_DEPEND IN ('S', 'D'))`
- **Check** `CK_EMP_EXPENSE_2`: `(CANCELLED IN ('Y', 'N'))`
- **Check** `CK_EMP_EXPENSE_3`: `(INCLUDE_IN_TAX IN ('Y', 'N'))`
- **Index** `IDX_EMP_EXPENSE_1` (VOUCHER_TYPE, VOUCHER_NO)
- **Index** `IDX_EMP_EXPENSE_2` (CANCELED_VOUCHER_TYPE, CANCELED_VOUCHER_NO)
- **Index** `IDX_EMP_EXPENSE_3` (EXPENSE_CODE)
- **Index** `IDX_EMP_EXPENSE_4` (MRNO)
- **Index** `IDX_EMP_EXPENSE_6` (TRUNC(TRANS_DATE))
- **Referenced by**: `EMP_PAYMENT`
- **Triggers**: `EMP_EXPENSE_DEL` (AFTER DELETE), `EMP_EXPENSE_INS` (BEFORE INSERT), `EMP_EXPENSE_UPD` (BEFORE UPDATE)

### EMP_EXPENSE_LIST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_LIST_ID** 🔑 | VARCHAR2(9) | N |  |  |
| 2 | **EXPENSE_CODE** | CHAR(3) | N |  |  |
| 3 | **TRANS_DATE** | DATE | N |  |  |
| 4 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 5 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 6 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 7 | **START_DATE** | DATE | Y |  |  |
| 8 | **END_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 18 | **WS_SYNC_DATE** | DATE | Y |  |  |
| 19 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_EMP_EXPENSE_LIST` (EXPENSE_LIST_ID)
- **Referenced by**: `EMP_EXPENSE_LIST_DTL`

### EMP_EXPENSE_LIST_DTL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **EXPENSE_LIST_ID** 🔑 → `PAYROLL.EMP_EXPENSE_LIST` | VARCHAR2(9) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 4 | **TAX_DEDUCTED** | NUMBER(20,2) | Y |  |  |
| 5 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 6 | **SELECT_FLAG** | CHAR(1) | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **WS_SYNC_DATE** | DATE | Y |  |  |
| 17 | **ERROR_LOG** | VARCHAR2(1000) | Y |  |  |

- **Primary key** `PK_EMP_EXPENSE_LIST_DTL` (EXPENSE_LIST_ID, MRNO)
- **FK** `FK_EMP_EXPENSE_LIST_DTL` (EXPENSE_LIST_ID) → `PAYROLL.EMP_EXPENSE_LIST` (EXPENSE_LIST_ID)

### EMP_EXP_DET_PROJECT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DOCUMENT_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **PROJECT_ID** 🔑 | VARCHAR2(7) | N |  |  |
| 3 | **AMOUNT** | NUMBER | Y |  |  |
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

- **Primary key** `PK_EMP_EXP_DET_PROJECT` (DOCUMENT_NO, PROJECT_ID)
- **Triggers**: `EMP_EXP_DET_PROJECT_DEL` (AFTER DELETE), `EMP_EXP_DET_PROJECT_INS` (BEFORE INSERT), `EMP_EXP_DET_PROJECT_UPD` (BEFORE UPDATE)

### EMP_INCREMENT_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 2 | **INCREMENT_DATE** 🔑 | DATE | N |  |  |
| 3 | **INCREMENT_CODE** → `PAYROLL.DEF_INCREMENT_TYPE` | CHAR(3) | N |  |  |
| 4 | **APPROVED_BY** | VARCHAR2(25) | Y |  |  |
| 5 | **INCR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **INCR_PERCENT** | NUMBER(6,2) | Y |  |  |
| 7 | **CURRENT_BASIC** | NUMBER(20,2) | Y |  |  |
| 8 | **CURRENT_GROSS** | NUMBER(20,2) | Y |  |  |
| 9 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **INCREMENT_END_DATE** | DATE | Y |  |  |
| 17 | **PREVIOUS_BASIC** | NUMBER(20,2) | Y |  |  |
| 18 | **PREVIOUS_GROSS** | NUMBER(20,2) | Y |  |  |
| 19 | **POSTED** | CHAR(1) | Y | 'N' |  |
| 20 | **EFFECTIVE_DATE** | DATE | Y |  |  |
| 21 | **ARREAR_PAID** | CHAR(1) | Y |  |  |
| 22 | **PROCESS_ID** | VARCHAR2(12) | Y |  | Ref to payroll.process_increment_master, if increment is processed through a process |
| 23 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 24 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 25 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 26 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EMP_INCREMENT_MASTER` (MRNO, INCREMENT_DATE)
- **FK** `FK_EMP_INCREMENT_MASTER_1` (INCREMENT_CODE) → `PAYROLL.DEF_INCREMENT_TYPE` (INCREMENT_CODE)
- **FK** `FK_EMP_INCREMENT_MASTER_2` (MRNO) → `HRD.INFORMATION` (MRNO)
- **Check** `CK_EMP_INCREMENT_MASTER_1`: `(posted in ('Y','N'))`
- **Index** `IDX_EMP_INCREMENT_MASTER_1` (INCREMENT_CODE)
- **Referenced by**: `EMP_INCREMENT_DETAIL`
- **Triggers**: `EMP_INCREMENT_MASTER_DEL` (AFTER DELETE), `EMP_INCREMENT_MASTER_INS` (BEFORE INSERT), `EMP_INCREMENT_MASTER_UPD` (BEFORE UPDATE), `EMP_INC_MAS_CHANGE_SAL` (AFTER UPDATE OF "CURRENT_GROSS"), `EMP_INC_MAS_DEL_SAL` (AFTER DELETE), `EMP_INC_MAS_INS_SAL` (AFTER INSERT)

### EMP_INCREMENT_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 2 | **MRNO** 🔑 → `PAYROLL.EMP_INCREMENT_MASTER` | VARCHAR2(14) | N |  |  |
| 3 | **INCREMENT_DATE** 🔑 → `PAYROLL.EMP_INCREMENT_MASTER` | DATE | N |  |  |
| 4 | **CURRENT_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 5 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 7 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **PREVIOUS_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 12 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 15 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EMP_INCREMENT_DETAIL` (AD_CODE, MRNO, INCREMENT_DATE)
- **FK** `FK_EMP_INCREMENT_DETAIL_2` (MRNO, INCREMENT_DATE) → `PAYROLL.EMP_INCREMENT_MASTER` (MRNO, INCREMENT_DATE) _DISABLED_
- **FK** `FK_EMP_INCR_DETAIL` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **Index** `IDX_EMP_INCREMENT_DETAIL_2` (MRNO, INCREMENT_DATE)
- **Triggers**: `EMP_INCREMENT_DETAIL_DEL` (AFTER DELETE), `EMP_INCREMENT_DETAIL_INS` (BEFORE INSERT), `EMP_INCREMENT_DETAIL_UPD` (BEFORE UPDATE)

### EMP_ITAX_ADJUSTMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.PAY_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **ADJUSTMENT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 4 | **AMOUNT** | NUMBER(10) | Y | 0 |  |
| 5 | **REMARKS** | VARCHAR2(255) | Y |  |  |
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
| 16 | **CURRENT_TAX** | NUMBER(15) | Y |  |  |
| 17 | **CURRENT_INCOME** | NUMBER(15) | Y |  |  |
| 18 | **POSTED** | CHAR(1) | Y |  |  |

- **Primary key** `PK_EMP_ITAX_ADJUSTMENT` (YEAR_CODE, MRNO, ADJUSTMENT_CODE)
- **FK** `FK_EMP_ITAX_ADJUSTMENT` (YEAR_CODE) → `PAYROLL.PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **Triggers**: `EMP_ITAX_ADJUSTMENT_DEL` (AFTER DELETE), `EMP_ITAX_ADJUSTMENT_INS` (BEFORE INSERT), `EMP_ITAX_ADJUSTMENT_UPD` (BEFORE UPDATE)

### EMP_ITAX_ADJUSTMENT_DTL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | VARCHAR2(4) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **ADJUSTMENT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 4 | **SRNO** 🔑 | NUMBER(2) | N |  |  |
| 5 | **AMOUNT** | NUMBER(10) | Y |  |  |
| 6 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 7 | **ENTRY_DATE** | DATE | Y |  |  |
| 8 | **START_DATE** | DATE | Y |  |  |
| 9 | **END_DATE** | DATE | Y |  |  |

- **Primary key** `PK_EMP_ITAX_ADJUSTMENT_DTL` (YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO)

### EMP_ITAX_ADJUSTMENT_DTL_M

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | VARCHAR2(4) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **ADJUSTMENT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 4 | **SRNO** 🔑 | NUMBER(2) | N |  |  |
| 5 | **AMOUNT** | NUMBER(10) | Y |  |  |
| 6 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 7 | **ENTRY_DATE** | DATE | Y |  |  |
| 8 | **START_DATE** 🔑 | DATE | N |  |  |
| 9 | **END_DATE** 🔑 | DATE | N |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_EMP_ITAX_ADJUSTMENT_DTL_M_01` (YEAR_CODE, MRNO, ADJUSTMENT_CODE, SRNO, START_DATE, END_DATE)
- **Triggers**: `EMP_ITAX_ADJUSTMENT_DTL_M_DEL` (AFTER DELETE), `EMP_ITAX_ADJUSTMENT_DTL_M_INS` (BEFORE INSERT), `EMP_ITAX_ADJUSTMENT_DTL_M_UPD` (BEFORE UPDATE)

### EMP_ITAX_ADJUSTMENT_MONTHLY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 → `PAYROLL.PAY_FINANCIAL_YEAR` | NUMBER(4) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **START_DATE** 🔑 | DATE | N |  |  |
| 4 | **END_DATE** | DATE | Y |  |  |
| 5 | **ADJUSTMENT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 6 | **AMOUNT** | NUMBER(10) | Y | 0 |  |
| 7 | **MONTHLY_AMOUNT** | NUMBER(10) | Y | 0 |  |
| 8 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 9 | **CURRENT_TAX** | NUMBER(15) | Y |  |  |
| 10 | **CURRENT_INCOME** | NUMBER(15) | Y |  |  |
| 11 | **POSTED** | CHAR(1) | Y |  |  |
| 12 | **ADJUSTED** | CHAR(1) | Y | 'N' |  |
| 13 | **ORDER_BY** | NUMBER | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 20 | **EXEMPTED_AMOUNT** | NUMBER(15) | Y |  |  |

- **Primary key** `PK_EMP_ITAX_ADJUSTMENT_MONTHLY` (YEAR_CODE, MRNO, ADJUSTMENT_CODE, START_DATE)
- **FK** `FK_EMP_ITAX_ADJUSTMENT_MONTHLY` (YEAR_CODE) → `PAYROLL.PAY_FINANCIAL_YEAR` (YEAR_CODE)
- **Triggers**: `SYN_EMP_ITAX_ADJ_MON_DEL` (AFTER DELETE), `SYN_EMP_ITAX_ADJ_MON_INS` (BEFORE INSERT), `SYN_EMP_ITAX_ADJ_MON_UPD` (BEFORE UPDATE)

### EMP_LIABILITY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LIABILITY_CODE** 🔑 → `PAYROLL.DEF_LIABILITY` | CHAR(3) | N |  |  |
| 2 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 3 | **LIABILITY_DATE** | DATE | Y |  |  |
| 4 | **CLEAR_DATE** | DATE | Y |  |  |
| 5 | **STATUS** | CHAR(1) | Y | 'N' |  |
| 6 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EMP_LIABILITY` (LIABILITY_CODE, MRNO)
- **FK** `FK_EMP_LIABILITY_1` (MRNO) → `HRD.INFORMATION` (MRNO)
- **FK** `FK_EMP_LIABILITY_2` (LIABILITY_CODE) → `PAYROLL.DEF_LIABILITY` (LIABILITY_CODE)
- **Check** `CK_EMP_LIABILITY_1`: `(STATUS IN ('C', 'N'))`
- **Index** `IDX_EMP_LIABILITY_1` (MRNO)
- **Triggers**: `EMP_LIABILITY_DEL` (AFTER DELETE), `EMP_LIABILITY_INS` (BEFORE INSERT), `EMP_LIABILITY_UPD` (BEFORE UPDATE)

### EMP_NEW_SAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | NUMBER | Y |  |  |
| 2 | **CURRENT_SAL** | NUMBER | Y |  |  |
| 3 | **INC_AGE** | NUMBER | Y |  |  |
| 4 | **INCR_AMNT** | NUMBER | Y |  |  |
| 5 | **NEW_SAL** | NUMBER | Y |  |  |
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


### EMP_PAYMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 4 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 5 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 6 | **DOCUMENT_NO** → `PAYROLL.EMP_EXPENSE` | VARCHAR2(12) | Y |  |  |
| 7 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_EMP_PAYMENT` (START_DATE, END_DATE, MRNO)
- **FK** `FK_EMP_PAYMENT_01` (DOCUMENT_NO) → `PAYROLL.EMP_EXPENSE` (DOCUMENT_NO) _DISABLED_
- **Triggers**: `EMP_PAYMENT_DEL` (AFTER DELETE), `EMP_PAYMENT_INS` (BEFORE INSERT), `EMP_PAYMENT_UPD` (BEFORE UPDATE)

### EMP_TAX_AMOUNT_OTHER_THAN_SAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 2 | **YEAR** 🔑 | VARCHAR2(4) | N |  |  |
| 3 | **TAXABLE_AMOUNT_TYPE_ID** 🔑 → `PAYROLL.DEF_TAX_AMOUNT_OTHER_THAN_SAL` | NUMBER(5) | N |  |  |
| 4 | **TAXABLE_AMOUNT** | NUMBER(10) | Y |  |  |
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

- **Primary key** `PK_EMP_TAX_AMOUNT_OTH_SAL` (MRNO, YEAR, TAXABLE_AMOUNT_TYPE_ID)
- **FK** `FK_EMP_TAX_AMOUNT_OTH_MRNO` (MRNO) → `HRD.INFORMATION` (MRNO)
- **FK** `FK_EMP_TAX_AMOUNT_TYPE_ID` (TAXABLE_AMOUNT_TYPE_ID) → `PAYROLL.DEF_TAX_AMOUNT_OTHER_THAN_SAL` (TAXABLE_AMOUNT_ID) _DISABLED_
- **Triggers**: `EMP_TAX_AMOUNT_OTHER_THAN__DEL` (AFTER DELETE), `EMP_TAX_AMOUNT_OTHER_THAN__INS` (BEFORE INSERT), `EMP_TAX_AMOUNT_OTHER_THAN__UPD` (BEFORE UPDATE)

### EXPENSE_CLAIM_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CLAIM_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **EXPENSE_CODE** | VARCHAR2(3) | Y |  |  |
| 3 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 4 | **TRANS_DATE** | DATE | Y |  |  |
| 5 | **ADVANCE_GIVEN** | NUMBER(10) | Y |  |  |
| 6 | **SIGN_BY** | VARCHAR2(14) | Y |  |  |
| 7 | **SIGN_DATE** | DATE | Y |  |  |
| 8 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **APPROVER_REMARKS** | VARCHAR2(500) | Y |  |  |
| 10 | **APPROVED_BY** | VARCHAR2(14) | Y |  |  |
| 11 | **APPROVED_DATE** | DATE | Y |  |  |
| 12 | **TRAVEL_REQUEST_NO** | NUMBER | Y |  |  |
| 13 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **DEPARTURE_DATE** | DATE | Y |  |  |
| 16 | **RETURN_DATE** | DATE | Y |  |  |
| 17 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 18 | **REVISION_NO** | NUMBER | Y |  |  |
| 19 | **AUTHORITY_MRNO** | VARCHAR2(14) | Y |  |  |
| 20 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 21 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 22 | **TRN_DATE** | DATE | Y |  |  |
| 23 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 24 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 25 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 26 | **WFE_NO** | NUMBER(3) | Y |  |  |
| 27 | **ENTERED_BY** | VARCHAR2(14) | Y |  |  |
| 28 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 29 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 30 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 31 | **CANCELLED_VOUCHER_NO** | CHAR(13) | Y |  |  |
| 32 | **REFUND_NO** | VARCHAR2(12) | Y |  |  |
| 33 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 34 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 35 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 36 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EXPENSE_CLAIM_MASTER` (CLAIM_NO)
- **Index** `IDX_EXPENSE_CLAIM_MASTER1` (ENTERED_BY)
- **Referenced by**: `EXPENSE_CLAIM_DETAIL`, `EXPENSE_CLAIM_DOCUMENT`, `EXPENSE_CLAIM_PROJECT`
- **Triggers**: `EXPENSE_CLAIM_MASTER_DEL` (AFTER DELETE), `EXPENSE_CLAIM_MASTER_INS` (AFTER INSERT), `EXPENSE_CLAIM_MASTER_UPD` (BEFORE UPDATE)

### EXPENSE_CLAIM_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CLAIM_NO** 🔑 → `PAYROLL.EXPENSE_CLAIM_MASTER` | VARCHAR2(12) | N |  |  |
| 2 | **SRNO** 🔑 | NUMBER(2) | N |  |  |
| 3 | **EXPENSE_TYPE_ID** | VARCHAR2(3) | Y |  |  |
| 4 | **FROM_DATE** | DATE | Y |  |  |
| 5 | **TO_DATE** | DATE | Y |  |  |
| 6 | **CLAIM_AMOUNT** | NUMBER(10) | Y |  |  |
| 7 | **APPROVED_AMOUNT** | NUMBER(10) | Y |  |  |
| 8 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **DAYS_CLAIMED** | NUMBER(4,1) | Y |  |  |
| 16 | **DAYS_APPROVED** | NUMBER(4,1) | Y |  |  |
| 17 | **SLAB_ID** | VARCHAR2(12) | Y |  |  |
| 18 | **ENTRY_TYPE** | CHAR(1) | Y |  |  |
| 19 | **CALC_METHOD** | CHAR(1) | Y |  |  |
| 20 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 21 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 22 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 23 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EXPENSE_CLAIM_DETAIL` (CLAIM_NO, SRNO)
- **FK** `FK_CLAIM_NO` (CLAIM_NO) → `PAYROLL.EXPENSE_CLAIM_MASTER` (CLAIM_NO)
- **Triggers**: `EXPENSE_CLAIM_DETAIL_DEL` (AFTER DELETE), `EXPENSE_CLAIM_DETAIL_INS` (BEFORE INSERT), `EXPENSE_CLAIM_DETAIL_UPD` (BEFORE UPDATE)

### EXPENSE_CLAIM_DOCUMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **DOCUMENT_ID** 🔑 | VARCHAR2(13) | N |  |  |
| 2 | **CLAIM_NO** → `PAYROLL.EXPENSE_CLAIM_MASTER` | VARCHAR2(12) | N |  |  |
| 3 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
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

- **Primary key** `PK_EXPENSE_CLAIM_DOCUMENT` (DOCUMENT_ID)
- **FK** `FK_EXPENSE_CLAIM_DOCUMENT` (CLAIM_NO) → `PAYROLL.EXPENSE_CLAIM_MASTER` (CLAIM_NO)
- **Index** `IDX_EXPENSE_CLAIM_DOCUMENT` (CLAIM_NO)

### EXPENSE_CLAIM_HIERARCHY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **HIERARCHY_ID** | NUMBER | N |  |  |
| 2 | **AUTHORITY_ID** | VARCHAR2(3) | N |  |  |
| 3 | **ACTIVE** | VARCHAR2(1) | Y | 'Y' |  |
| 4 | **ORDERBY** | NUMBER | N |  |  |
| 5 | **LOCATION_ID** | VARCHAR2(3) | N |  |  |
| 6 | **DEPARTMENT_ID** | VARCHAR2(7) | N |  |  |
| 7 | **REJECTED** | VARCHAR2(1) | Y | 'N' |  |
| 8 | **MODIFICATION** | VARCHAR2(1) | Y | 'N' |  |

- **Triggers**: `TRG_EXP_CLAIM_HIERARCHY_ID` (BEFORE INSERT)

### EXPENSE_CLAIM_HIERARCHY_ORG

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **HIERARCHY_ID** | NUMBER | N |  |  |
| 2 | **AUTHORITY_ID** | VARCHAR2(3) | N |  |  |
| 3 | **ACTIVE** | VARCHAR2(1) | Y | 'Y' |  |
| 4 | **ORDERBY** | NUMBER | N |  |  |
| 5 | **ORGANIZATION_ID** | VARCHAR2(3) | N |  |  |

- **Triggers**: `TRG_EXP_CLAIM_HIERARCHY_ORG_ID` (BEFORE INSERT)

### EXPENSE_CLAIM_PROJECT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CLAIM_NO** 🔑 → `PAYROLL.EXPENSE_CLAIM_MASTER` | VARCHAR2(12) | N |  |  |
| 2 | **PROJECT_ID** 🔑 → `PAYROLL.DEF_PROJECT` | VARCHAR2(7) | N |  |  |
| 3 | **EXP_PERCENTAGE** | NUMBER | Y |  |  |
| 4 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
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

- **Primary key** `PK_EXP_CLAIM_PROJECT` (CLAIM_NO, PROJECT_ID)
- **FK** `FK_CLAIM_NO_ECP` (CLAIM_NO) → `PAYROLL.EXPENSE_CLAIM_MASTER` (CLAIM_NO)
- **FK** `FK_PROJECT_ID_ECP` (PROJECT_ID) → `PAYROLL.DEF_PROJECT` (PROJECT_ID) _DISABLED_
- **Check** `CK_PERCENTAGE`: `(EXP_PERCENTAGE > 0)`
- **Index** `IDX_EXPENSE_CLAIM_PROJECT_1` (CLAIM_NO)
- **Index** `IDX_EXPENSE_CLAIM_PROJECT_2` (PROJECT_ID)
- **Triggers**: `EXPENSE_CLAIM_PROJECT_DEL` (AFTER DELETE), `EXPENSE_CLAIM_PROJECT_INS` (BEFORE INSERT), `EXPENSE_CLAIM_PROJECT_UPD` (BEFORE UPDATE)

### EXPENSE_CLAIM_WORKFLOW

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CLAIM_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **WFE_NO** 🔑 | NUMBER(3) | N |  |  |
| 3 | **SCHEMA_ID** | VARCHAR2(3) | Y |  |  |
| 4 | **WORKFLOW_TYPE_ID** | NUMBER(3) | Y |  |  |
| 5 | **WORK_FLOW_ID** | NUMBER(4) | Y |  |  |
| 6 | **EVENT_ID** | NUMBER(3) | Y |  |  |
| 7 | **ENTERED_BY** | VARCHAR2(14) | Y |  |  |
| 8 | **ENTERED_DATE** | DATE | Y |  |  |
| 9 | **OBJECT_CODE** | VARCHAR2(11) | Y |  |  |
| 10 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_EXPENSE_CLAIM_WORKFLOW` (CLAIM_NO, WFE_NO)

### EXPENSE_CLAIM_WORKFLOW_Q

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **CLAIM_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **WFE_NO** 🔑 | NUMBER(3) | N |  |  |
| 3 | **ASSIGNEE_MRNO** 🔑 | VARCHAR2(14) | N |  |  |
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

- **Primary key** `PK_EXPENSE_CLAIM_WF_Q` (CLAIM_NO, WFE_NO, ASSIGNEE_MRNO)
- **Triggers**: `EXPENSE_CLAIM_WORKFLOW_Q_APPR_INS` (BEFORE INSERT), `EXPENSE_CLAIM_WORKFLOW_Q_INS` (BEFORE INSERT)

### FINAL_SETTLEMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** 🔑 | VARCHAR2(9) | N |  |  |
| 2 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 3 | **TRANS_DATE** | DATE | Y |  |  |
| 4 | **ZAKAT** | VARCHAR2(1) | Y |  |  |
| 5 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 6 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 7 | **SIGN_BY** | VARCHAR2(14) | Y |  |  |
| 8 | **SIGN_DATE** | DATE | Y |  |  |
| 9 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 10 | **WFE_NO** | NUMBER(3) | Y |  |  |
| 11 | **ENTERED_BY** | VARCHAR2(14) | Y |  |  |
| 12 | **ENTERED_DATE** | DATE | Y |  |  |
| 13 | **CLEARANCE_CERTIFICATE_ID** | NUMBER(5) | Y |  | PK of CLEARANCE_CERTIFICATE |
| 14 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  | PK of CLEARANCE_CERTIFICATE |
| 15 | **LOCATION_ID** | VARCHAR2(3) | Y |  | PK of CLEARANCE_CERTIFICATE |
| 16 | **LFA_STATUS** | VARCHAR2(1) | Y |  | N = None, P = To be Paid, D = To be deducted |
| 17 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 18 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 19 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 20 | **INCOME_TAX** | NUMBER(20,2) | Y |  |  |
| 21 | **DOCUMENT_NO** | VARCHAR2(12) | Y |  |  |
| 22 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 23 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 24 | **TRN_DATE** | DATE | Y |  |  |
| 25 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 26 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 27 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 28 | **PF_CHEQUE_ACK** | VARCHAR2(1) | Y |  |  |

- **Primary key** `PK_FINAL_SETTLEMENT` (FINAL_SETTLEMENT_ID)
- **Triggers**: `FINAL_SETTLEMENT_DEL` (AFTER DELETE), `FINAL_SETTLEMENT_INS` (BEFORE INSERT), `FINAL_SETTLEMENT_UPD` (BEFORE UPDATE), `FS_PQ_UPD` (BEFORE UPDATE)

### FINAL_SETTLEMENT_ELEMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** 🔑 | VARCHAR2(9) | N |  |  |
| 2 | **ELEMENT_CODE** 🔑 | VARCHAR2(8) | N |  |  |
| 3 | **AMOUNT** | NUMBER(10) | Y |  |  |
| 4 | **FROM_DATE** | DATE | Y |  |  |
| 5 | **TO_DATE** | DATE | Y |  |  |
| 6 | **VALUE** | NUMBER(8,4) | Y |  |  |
| 7 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 8 | **ACTUAL_AMOUNT** | NUMBER(10) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_FINAL_SETTLEMENT_ELEMENT` (FINAL_SETTLEMENT_ID, ELEMENT_CODE)
- **Triggers**: `FINAL_SETTLEMENT_ELEMENT_DEL` (AFTER DELETE), `FINAL_SETTLEMENT_ELEMENT_INS` (BEFORE INSERT), `FINAL_SETTLEMENT_ELEMENT_UPD` (BEFORE UPDATE)

### FINAL_SETTLEMENT_WF

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** | VARCHAR2(9) | N |  |  |
| 2 | **WFE_NO** | NUMBER(3) | N |  |  |
| 3 | **SCHEMA_ID** | VARCHAR2(3) | Y |  |  |
| 4 | **WORKFLOW_TYPE_ID** | NUMBER(3) | Y |  |  |
| 5 | **WORK_FLOW_ID** | NUMBER(4) | Y |  |  |
| 6 | **EVENT_ID** | NUMBER(3) | Y |  |  |
| 7 | **ENTERED_BY** | VARCHAR2(14) | Y |  |  |
| 8 | **ENTERED_DATE** | DATE | Y |  |  |
| 9 | **OBJECT_CODE** | VARCHAR2(11) | Y |  |  |
| 10 | **REMARKS** | VARCHAR2(255) | Y |  |  |


### FINAL_SETTLEMENT_WF_Q

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** | VARCHAR2(9) | N |  |  |
| 2 | **WFE_NO** | NUMBER(3) | N |  |  |
| 3 | **ASSIGNEE_MRNO** | VARCHAR2(14) | N |  |  |

- **Triggers**: `FS_WORKFLOW_PQ_INS` (BEFORE INSERT)

### GENERIC_REPORT_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_ID** 🔑 | NUMBER(8) | N |  |  |
| 2 | **ORGANIZATION_ID** | VARCHAR2(3) | N |  |  |
| 3 | **LOCATION_ID** | VARCHAR2(3) | N |  |  |
| 4 | **OBJECT_CODE** | VARCHAR2(11) | N |  |  |
| 5 | **ACTIVE** | CHAR(1) | N | 'Y' |  |
| 6 | **FROM_DATE** | DATE | N |  |  |
| 7 | **TO_DATE** | DATE | Y |  |  |
| 8 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **TRN_DATE** | DATE | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_GENERIC_REPORT_MASTER` (REPORT_ID)
- **Referenced by**: `GENERIC_REPORT_FIELD`
- **Triggers**: `GENERIC_REPORT_MASTER_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `GENERIC_REPORT_MASTER_DEL` (AFTER DELETE), `GENERIC_REPORT_MASTER_INS` (BEFORE INSERT), `GENERIC_REPORT_MASTER_UPD` (BEFORE UPDATE), `TRG_WS_WXW_JX_NS_Q` (AFTER INSERT OR UPDATE OR DELETE)

### GENERIC_REPORT_FIELD

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_ID** 🔑 → `PAYROLL.GENERIC_REPORT_MASTER` | NUMBER(8) | N |  |  |
| 2 | **FIELD_CODE** 🔑 | VARCHAR2(64) | N |  |  |
| 3 | **PROMPT** | VARCHAR2(500) | Y |  |  |
| 4 | **AD_CODE** | VARCHAR2(3) | Y |  |  |
| 5 | **ACTIVE** | CHAR(1) | Y | 'Y' |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **DISPLAY** | CHAR(1) | Y | 'Y' |  |
| 13 | **ORDER_BY** | NUMBER(3) | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_GENERIC_REPORT_FIELD` (REPORT_ID, FIELD_CODE)
- **FK** `FK_GENERIC_REPORT_FIELD` (REPORT_ID) → `PAYROLL.GENERIC_REPORT_MASTER` (REPORT_ID)
- **Referenced by**: `GENERIC_REPORT_FIELD_DTL`
- **Triggers**: `GENERIC_REPORT_FIELD_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `GENERIC_REPORT_FIELD_DEL` (AFTER DELETE), `GENERIC_REPORT_FIELD_INS` (BEFORE INSERT), `GENERIC_REPORT_FIELD_UPD` (BEFORE UPDATE), `TRG_WS_EMS_YD_EF_Q` (AFTER INSERT OR UPDATE OR DELETE)

### GENERIC_REPORT_FIELD_DTL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_ID** 🔑 → `PAYROLL.GENERIC_REPORT_FIELD` | NUMBER(8) | N |  |  |
| 2 | **FIELD_CODE** 🔑 → `PAYROLL.GENERIC_REPORT_FIELD` | VARCHAR2(64) | N |  |  |
| 3 | **SRNO** 🔑 | NUMBER(2) | N |  |  |
| 4 | **ADD_SUBSTRACT** | CHAR(1) | Y |  |  |
| 5 | **SUB_FIELD_CODE** | VARCHAR2(64) | Y |  |  |
| 6 | **ACTIVE** | CHAR(1) | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_GENERIC_RPT_FIELD_DTL` (REPORT_ID, FIELD_CODE, SRNO)
- **FK** `FK_GENERIC_RPT_FIELD_DTL` (REPORT_ID, FIELD_CODE) → `PAYROLL.GENERIC_REPORT_FIELD` (REPORT_ID, FIELD_CODE)
- **Triggers**: `GENERIC_REPORT_FIELD_DTL_CEA` (BEFORE INSERT OR UPDATE OR DELETE), `GENERIC_REPORT_FIELD_DTL_PK` (BEFORE INSERT), `TRG_WS_IKE_GP_IJ_Q` (AFTER INSERT OR UPDATE OR DELETE)

### HOLD_ORDER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **HOLD_ORDER_ID** 🔑 | NUMBER(20) | N |  |  |
| 2 | **TRANS_DATE** | DATE | Y |  |  |
| 3 | **MRNO** | VARCHAR2(14) | N |  |  |
| 4 | **FROM_MONTH** | CHAR(6) | Y |  |  |
| 5 | **HOLD** | CHAR(1) | N |  |  |
| 6 | **REMARKS** | VARCHAR2(500) | Y |  |  |
| 7 | **UNHOLD_REASON** | VARCHAR2(500) | Y |  |  |
| 8 | **UNHOLD_DATE** | DATE | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_HOLD_ORDER` (HOLD_ORDER_ID)
- **Triggers**: `HOLD_ORDER_DEL` (AFTER DELETE), `HOLD_ORDER_INS` (BEFORE INSERT), `HOLD_ORDER_UPD` (BEFORE UPDATE)

### ITAX_PAYMENT_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 2 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 4 | **START_DATE** 🔑 | DATE | N |  |  |
| 5 | **END_DATE** 🔑 | DATE | N |  |  |
| 6 | **DEPOSIT_DATE** | DATE | Y |  |  |
| 7 | **BANK_TREASURY** | VARCHAR2(64) | Y |  |  |
| 8 | **BRANCH_CITY** | VARCHAR2(64) | Y |  |  |
| 9 | **ACCOUNT** | VARCHAR2(32) | Y |  |  |
| 10 | **CPRNO** | VARCHAR2(32) | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PKITAX_PAYMENT_DETAIL` (YEAR_CODE, ORGANIZATION_ID, LOCATION_ID, START_DATE, END_DATE)
- **Triggers**: `ITAX_PAYMENT_DETAIL_DEL` (AFTER DELETE), `ITAX_PAYMENT_DETAIL_INS` (BEFORE INSERT), `ITAX_PAYMENT_DETAIL_UPD` (BEFORE UPDATE)

### ITAX_PAYMENT_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **ORGANIZATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 2 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 3 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 4 | **PERSON_ADDRESS** | VARCHAR2(250) | Y |  |  |
| 5 | **SECTION_CODE** | VARCHAR2(32) | Y |  |  |
| 6 | **SECTION_DESCRIPTION** | VARCHAR2(250) | Y |  |  |
| 7 | **VIDE** | VARCHAR2(250) | Y |  |  |
| 8 | **COMPANY_NAME** | VARCHAR2(250) | Y |  |  |
| 9 | **SIGN_AUTHORITY** | VARCHAR2(14) | Y |  |  |
| 10 | **PRINT_ALLOWED** | CHAR(1) | Y | 'Y' |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_ITAX_PAYMENT_MASTER` (ORGANIZATION_ID, LOCATION_ID, YEAR_CODE)
- **Triggers**: `ITAX_PAYMENT_MASTER_DEL` (AFTER DELETE), `ITAX_PAYMENT_MASTER_INS` (BEFORE INSERT), `ITAX_PAYMENT_MASTER_UPD` (BEFORE UPDATE)

### LEAVE_DAYS_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **LEAVE_DATE** 🔑 | DATE | N |  |  |
| 3 | **SALARY_MONTH** | VARCHAR2(6) | Y |  |  |
| 4 | **UNPAID_STATUS** | CHAR(1) | Y |  |  |
| 5 | **SALARY_START_DATE** | DATE | Y |  |  |
| 6 | **SALARY_END_DATE** | DATE | Y |  |  |
| 7 | **LEAVE_TYPE_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_LEAVE_DAYS_TEST` (MRNO, LEAVE_DATE)
- **Check** `CHK_LEAVE_DAYS_TEST`: `(UNPAID_STATUS IN ('N','D','U'))`

### LOAN_INSTALLMENT_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_START_DATE** 🔑 | DATE | N |  |  |
| 2 | **PAY_END_DATE** 🔑 | DATE | N |  |  |
| 3 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 4 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 5 | **TRANS_DATE** | DATE | Y |  |  |
| 6 | **LOAN_CODE** | CHAR(3) | Y |  |  |
| 7 | **SALARY_DEDUCTION_TYPE** | CHAR(1) | Y |  |  |
| 8 | **REFUND_WITH_PAY_VOUCHER** | CHAR(1) | Y |  |  |
| 9 | **REFUND_AD_CODE** | CHAR(3) | Y |  |  |
| 10 | **PRINCIPAL_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 11 | **LOAN_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 12 | **INTEREST_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 13 | **ACTUAL_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 14 | **TEMP_REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 15 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 16 | **REFUND_NO** | VARCHAR2(12) | Y |  |  |
| 17 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 20 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 21 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 22 | **TRN_DATE** | DATE | Y |  |  |
| 23 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 24 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 25 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 26 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_INSTALLMENT_DETAIL` (PAY_START_DATE, PAY_END_DATE, MRNO, LOAN_NO)

### LOAN_PAYMENT_INTEREST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 3 | **TRANS_DATE** | DATE | Y |  |  |
| 4 | **INTEREST_RATE** | NUMBER(5,2) | Y |  | Current Interest Rate at time of this transaction |
| 5 | **PRINCIPAL_AMOUNT** | NUMBER(20,2) | Y |  | Total Pending Amount at time of this transaction |
| 6 | **NO_OF_MONTHS** | NUMBER(2) | Y |  | No of installments in a year |
| 7 | **INTEREST_AMOUNT** | NUMBER(20,2) | Y |  | Total Calculated Interest Amount |
| 8 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  | Interest Voucher Type |
| 9 | **VOUCHER_NO** | CHAR(13) | Y |  | Interest Voucher No |
| 10 | **CANCELLED** | CHAR(1) | Y | 'N' |  |
| 11 | **CANCEL_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 12 | **CANCEL_VOUCHER_NO** | VARCHAR2(13) | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 19 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 20 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 21 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 22 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_PAYMENT_INTEREST` (LOAN_NO, YEAR_CODE)
- **Triggers**: `LOAN_PAYMENT_INTEREST_DEL` (AFTER DELETE), `LOAN_PAYMENT_INTEREST_INS` (BEFORE INSERT), `LOAN_PAYMENT_INTEREST_UPD` (BEFORE UPDATE)

### LOAN_PAYMENT_MASTER

This table is used to entertain opening balances and transactions of staff advances

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  | Auto-generated Primary Key |
| 2 | **TRANS_TYPE** | CHAR(1) | Y | 'L' | Either "O" for Opening Balance or "L" for Loan / Advance transactions |
| 3 | **TRANS_DATE** | DATE | Y |  | Date of Loan transaction or Opening balances |
| 4 | **MRNO** → `HRD.INFORMATION` | VARCHAR2(14) | Y |  | Employee code |
| 5 | **LOAN_CODE** | CHAR(3) | Y |  | LOan type (Advance, Car Loan etc.) |
| 6 | **OPEN_ACTUAL_DATE** | DATE | Y |  | Date of loan (only valid for opening balances entry) |
| 7 | **OPEN_ACTUAL_LOAN** | NUMBER(20,2) | Y |  | Amount of loan (only valid for opening balances entry) |
| 8 | **OPEN_ACTUAL_INSTALLMENTS** | NUMBER(5) | Y |  | Total Installments of loan (only valid for opening balances entry) |
| 9 | **OPEN_ACTUAL_MONTHLY** | NUMBER(20,2) | Y |  | Monthly deduction (only valid for opening balances entry) |
| 10 | **LOAN_AMOUNT** | NUMBER(20,2) | N |  | Self explainatory |
| 11 | **NO_OF_INSTALLMENTS** | NUMBER(5) | Y |  | no. of Monthly installments |
| 12 | **MONTHLY_INSTALLMENT** | NUMBER(20,2) | Y |  | to be deducted from monthly salary |
| 13 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  | Total amount refunded todate |
| 14 | **VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  | GL Voucher type |
| 15 | **VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  | GL Voucher number |
| 16 | **STOP_AUTO_DEDUCTION** | CHAR(1) | Y | 'N' | If deduction fomr salarty needs to be stopped then it will be "Y", otherwise "N". By default it will be "N" |
| 17 | **REMARKS** | VARCHAR2(255) | Y |  | Self explainatory |
| 18 | **CANCELLED** | CHAR(1) | Y | 'N' | If loan transaction needs to be cancelled, then it will be set to "Y", otherwise NULL |
| 19 | **CANCEL_VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher type, If loan transaction needs to be cancelled |
| 20 | **CANCEL_VOUCHER_NO** | VARCHAR2(13) | Y |  | GL Voucher number, If loan transaction needs to be cancelled |
| 21 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 22 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 23 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 24 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 25 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 26 | **TRN_DATE** | DATE | Y |  |  |
| 27 | **STOP_AUTO_DEDUCTION_TILL** | DATE | Y |  |  |
| 28 | **MERGED_LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 29 | **MERGE** | CHAR(1) | Y | 'N' |  |
| 30 | **CONVERTED_LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 31 | **BASE_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 32 | **BASE_CURRENCY_ID** | VARCHAR2(3) | Y | '001' |  |
| 33 | **BASE_CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y | 1 |  |
| 34 | **TEMP_LOAN_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 35 | **LOAN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 36 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 37 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 38 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 39 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 40 | **TRAVEL_REQUEST_NO** | NUMBER | Y |  |  |

- **Primary key** `PK_LOAN_PAYMENT_MASTER` (LOAN_NO)
- **FK** `FK_LOAN_PAYMENT_MASTER_1` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **FK** `FK_LOAN_PAYMENT_MASTER_3` (VOUCHER_TYPE, VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **Check** `CK_LOAN_PAYMENT_MASTER_1`: `(TRANS_TYPE IN ('O', 'L'))`
- **Check** `CK_LOAN_PAYMENT_MASTER_2`: `(CANCELLED IN ('Y', 'N'))`
- **Check** `CK_LOAN_PAYMENT_MASTER_3`: `(STOP_AUTO_DEDUCTION IN ('Y', 'N'))`
- **Index** `IDX_LOAN_PAYMENT_MASTER_1` (MRNO)
- **Index** `IDX_LOAN_PAYMENT_MASTER_2` (LOAN_CODE)
- **Index** `IDX_LOAN_PAYMENT_MASTER_3` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `LOAN_REFUND_DETAIL`
- **Triggers**: `LOAN_PAYMENT_MASTER_DEL` (AFTER DELETE), `LOAN_PAYMENT_MASTER_INS` (BEFORE INSERT), `LOAN_PAYMENT_MASTER_UPD` (BEFORE UPDATE)

### LOAN_PAYMENT_MASTER_N

This table is used to entertain opening balances and transactions of staff advances

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  | Auto-generated Primary Key |
| 2 | **TRANS_TYPE** | CHAR(1) | Y | 'L' | Either "O" for Opening Balance or "L" for Loan / Advance transactions |
| 3 | **TRANS_DATE** | DATE | Y |  | Date of Loan transaction or Opening balances |
| 4 | **MRNO** | VARCHAR2(14) | Y |  | Employee code |
| 5 | **LOAN_CODE** | CHAR(3) | Y |  | LOan type (Advance, Car Loan etc.) |
| 6 | **OPEN_ACTUAL_DATE** | DATE | Y |  | Date of loan (only valid for opening balances entry) |
| 7 | **OPEN_ACTUAL_LOAN** | NUMBER(20,2) | Y |  | Amount of loan (only valid for opening balances entry) |
| 8 | **OPEN_ACTUAL_INSTALLMENTS** | NUMBER(5) | Y |  | Total Installments of loan (only valid for opening balances entry) |
| 9 | **OPEN_ACTUAL_MONTHLY** | NUMBER(20,2) | Y |  | Monthly deduction (only valid for opening balances entry) |
| 10 | **LOAN_AMOUNT** | NUMBER(20,2) | N |  | Self explainatory |
| 11 | **NO_OF_INSTALLMENTS** | NUMBER(5) | Y |  | no. of Monthly installments |
| 12 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  | Total amount refunded todate |
| 13 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher type |
| 14 | **VOUCHER_NO** | CHAR(13) | Y |  | GL Voucher number |
| 15 | **STOP_AUTO_DEDUCTION** | CHAR(1) | Y | 'N' | If deduction fomr salarty needs to be stopped then it will be "Y", otherwise "N". By default it will be "N" |
| 16 | **REMARKS** | VARCHAR2(255) | Y |  | Self explainatory |
| 17 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher type, If loan transaction needs to be cancelled |
| 18 | **CANCELLED_VOUCHER_NO** | VARCHAR2(13) | Y |  | GL Voucher number, If loan transaction needs to be cancelled |
| 19 | **STOP_AUTO_DEDUCTION_TILL** | DATE | Y |  |  |
| 20 | **BASE_CURRENCY_ID** | VARCHAR2(3) | Y | '001' |  |
| 21 | **BASE_CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y | 1 |  |
| 22 | **TEMP_LOAN_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 23 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 24 | **LOAN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 25 | **MODULE** | VARCHAR2(2) | Y |  | PF, GL |
| 26 | **STATUS_ID** | VARCHAR2(3) | N | '100' | 100 -> ENTRY, 101 -> POST, 102 -> CANCEL |
| 27 | **INTEREST_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 28 | **LOAN_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 29 | **INTEREST_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 30 | **PAID_INTEREST** | NUMBER(20,2) | Y |  |  |
| 31 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 32 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 33 | **TRN_DATE** | DATE | Y |  |  |
| 34 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 35 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 36 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 37 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 38 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 39 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 40 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_PAYMENT_MASTER_N` (LOAN_NO)
- **Check** `CK_LOAN_PAYMENT_MASTER_N_1`: `(TRANS_TYPE IN ('O', 'L', 'R'))`
- **Check** `CK_LOAN_PAYMENT_MASTER_N_3`: `(STOP_AUTO_DEDUCTION IN ('Y', 'N'))`
- **Index** `IDX_LOAN_PAYMENT_MASTER_N_1` (MRNO)
- **Index** `IDX_LOAN_PAYMENT_MASTER_N_2` (LOAN_CODE)
- **Index** `IDX_LOAN_PAYMENT_MASTER_N_3` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `LOAN_REFUND_DETAIL_N`
- **Triggers**: `LOAN_PAYMENT_MASTER_N_DEL` (AFTER DELETE), `LOAN_PAYMENT_MASTER_N_INS` (BEFORE INSERT), `LOAN_PAYMENT_MASTER_N_UPD` (BEFORE UPDATE)

### LOAN_PAYMENT_MASTER_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **TRANS_TYPE** | CHAR(1) | Y |  |  |
| 3 | **TRANS_DATE** | DATE | Y |  |  |
| 4 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 5 | **LOAN_CODE** | CHAR(3) | Y |  |  |
| 6 | **OPEN_ACTUAL_DATE** | DATE | Y |  |  |
| 7 | **OPEN_ACTUAL_LOAN** | NUMBER(20,2) | Y |  |  |
| 8 | **OPEN_ACTUAL_INSTALLMENTS** | NUMBER(5) | Y |  |  |
| 9 | **OPEN_ACTUAL_MONTHLY** | NUMBER(20,2) | Y |  |  |
| 10 | **LOAN_AMOUNT** | NUMBER(20,2) | N |  |  |
| 11 | **NO_OF_INSTALLMENTS** | NUMBER(5) | Y |  |  |
| 12 | **MONTHLY_INSTALLMENT** | NUMBER(20,2) | Y |  |  |
| 13 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 14 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 15 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 16 | **STOP_AUTO_DEDUCTION** | CHAR(1) | Y |  |  |
| 17 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 18 | **CANCELLED** | CHAR(1) | Y |  |  |
| 19 | **CANCEL_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 20 | **CANCEL_VOUCHER_NO** | VARCHAR2(13) | Y |  |  |
| 21 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 22 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 23 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 24 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 25 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 26 | **TRN_DATE** | DATE | Y |  |  |
| 27 | **STOP_AUTO_DEDUCTION_TILL** | DATE | Y |  |  |
| 28 | **MERGED_LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 29 | **MERGE** | CHAR(1) | Y | 'N' |  |
| 30 | **CONVERTED_LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 31 | **BASE_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 32 | **BASE_CURRENCY_ID** | VARCHAR2(3) | Y | '001' |  |
| 33 | **BASE_CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y | 1 |  |
| 34 | **LOAN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_LOAN_PAYMENT_MASTER_TEST` (LOAN_NO)
- **Check** `CK_LOAN_PAYMENT_MASTER_TEST_2`: `(CANCELLED IN ('Y', 'N'))`
- **Check** `CK_LOAN_PAYMENT_MASTER_TEST_3`: `(STOP_AUTO_DEDUCTION IN ('Y', 'N'))`
- **Referenced by**: `LOAN_REFUND_DETAIL_TEST`

### LOAN_REFUND_MASTER

This table is used to entertain transactions of refunds advances or deductions of advances against salary

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REFUND_NO** 🔑 | VARCHAR2(12) | N |  | Primary Key - auto-generated key |
| 2 | **TRANS_DATE** | DATE | Y |  | Date of refund or deduction |
| 3 | **VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  | GL Voucher Type |
| 4 | **VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  | GL Voucher Number |
| 5 | **MRNO** → `HRD.INFORMATION` | VARCHAR2(14) | N |  | Employee code |
| 6 | **REFUND_AMOUNT** | NUMBER(20,2) | N |  | Amount to be refunded or deducted |
| 7 | **REMARKS** | VARCHAR2(255) | Y |  | Selef explainatory |
| 8 | **CANCELLED** | CHAR(1) | Y | 'M' | If refund transaction needs to be cancelled, then it will be set to "Y", otherwise NULL |
| 9 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher type, If refund transaction needs to be cancelled |
| 10 | **CANCELLED_VOUCHER_NO** | VARCHAR2(13) | Y |  | GL Voucher type, If refund transaction needs to be cancelled |
| 11 | **REFUND_TYPE** | CHAR(1) | Y | 'M' | Either "M" for Manul refunds or "S" for Automatic deductions from salary |
| 12 | **START_DATE** | DATE | Y |  |  |
| 13 | **END_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 17 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **TRN_DATE** | DATE | Y |  |  |
| 20 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 21 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 22 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 23 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_REFUND_MASTER` (REFUND_NO)
- **FK** `FK_LOAN_REFUND_MASTER_1` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **FK** `FK_LOAN_REFUND_MASTER_2` (VOUCHER_TYPE, VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **Check** `CK_LOAN_REFUND_MASTER_1`: `(CANCELLED IN ('Y', 'N'))`
- **Check** `CK_LOAN_REFUND_MASTER_2`: `(REFUND_TYPE IN ('M', 'S'))`
- **Index** `IDX_LOAN_REFUND_MASTER_1` (MRNO)
- **Index** `IDX_LOAN_REFUND_MASTER_2` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `LOAN_REFUND_DETAIL`
- **Triggers**: `LOAN_REFUND_MASTER_DEL` (AFTER DELETE), `LOAN_REFUND_MASTER_INS` (BEFORE INSERT), `LOAN_REFUND_MASTER_UPD` (BEFORE UPDATE)

### LOAN_REFUND_DETAIL

This table is used to entertain transactions of refunds advances or deductions of advances against salary

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 → `PAYROLL.LOAN_PAYMENT_MASTER` | VARCHAR2(12) | N |  | Self explainatory |
| 2 | **REFUND_NO** 🔑 → `PAYROLL.LOAN_REFUND_MASTER` | VARCHAR2(12) | N |  | Selef explainatory |
| 3 | **START_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  | Start date of Salary period |
| 4 | **END_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  | End date of Salary period |
| 5 | **LOAN_AMOUNT** | NUMBER(20,2) | Y |  | Self explainatory |
| 6 | **REFUND_AMOUNT** | NUMBER(20,2) | N |  | Self explainatory |
| 7 | **MRNO** → `HRD.INFORMATION` | VARCHAR2(14) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **TEMP_REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 15 | **REFUND_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_REFUND_DETAIL` (LOAN_NO, REFUND_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_1` (LOAN_NO) → `PAYROLL.LOAN_PAYMENT_MASTER` (LOAN_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_2` (REFUND_NO) → `PAYROLL.LOAN_REFUND_MASTER` (REFUND_NO)
- **FK** `FK_LOAN_REFUND_DETAIL_1` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **FK** `FK_LOAN_REFUND_DETAIL_2` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **Index** `IDX_LOAN_REFUND_DETAIL_2` (REFUND_NO)
- **Triggers**: `LOAN_REFUND_DETAIL_DEL` (AFTER DELETE), `LOAN_REFUND_DETAIL_INS` (BEFORE INSERT), `LOAN_REFUND_DETAIL_UPD` (BEFORE UPDATE)

### LOAN_REFUND_MASTER_N

This table is used to entertain transactions of refunds advances or deductions of advances against salary

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REFUND_NO** 🔑 | VARCHAR2(12) | N |  | Primary Key - auto-generated key |
| 2 | **MODULE** | VARCHAR2(2) | Y |  | PF, GL, CP, GP |
| 3 | **REFUND_TYPE** | CHAR(1) | Y | 'M' | Either "M" for Manul refunds or "S" for Automatic deductions from salary |
| 4 | **TRANS_DATE** | DATE | Y |  | Date of refund or deduction |
| 5 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher Type |
| 6 | **VOUCHER_NO** | CHAR(13) | Y |  | GL Voucher Number |
| 7 | **PAY_START_DATE** | DATE | Y |  |  |
| 8 | **PAY_END_DATE** | DATE | Y |  |  |
| 9 | **MRNO** | VARCHAR2(14) | N |  | Employee code |
| 10 | **REFUND_AMOUNT** | NUMBER(20,2) | N |  | Amount to be refunded or deducted |
| 11 | **REMARKS** | VARCHAR2(255) | Y |  | Selef explainatory |
| 12 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  | GL Voucher type, If refund transaction needs to be cancelled |
| 13 | **CANCELLED_VOUCHER_NO** | VARCHAR2(13) | Y |  | GL Voucher type, If refund transaction needs to be cancelled |
| 14 | **RECEIPT_NO** | VARCHAR2(13) | Y |  |  |
| 15 | **STATUS_ID** | VARCHAR2(3) | N | '100' | 100 -> ENTRY, 101 -> POST, 102 -> CANCEL |
| 16 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **TRN_DATE** | DATE | Y |  |  |
| 19 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 20 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 21 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 22 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 23 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 24 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 25 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_REFUND_MASTER_N` (REFUND_NO)
- **Check** `CK_LOAN_REFUND_MASTER_N_2`: `(REFUND_TYPE IN ('M', 'S'))`
- **Index** `IDX_LOAN_REFUND_MASTER_N_1` (MRNO)
- **Index** `IDX_LOAN_REFUND_MASTER_N_2` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `LOAN_REFUND_DETAIL_N`
- **Triggers**: `LOAN_REFUND_MASTER_N_DEL` (AFTER DELETE), `LOAN_REFUND_MASTER_N_INS` (BEFORE INSERT), `LOAN_REFUND_MASTER_N_UPD` (BEFORE UPDATE)

### LOAN_REFUND_DETAIL_N

This table is used to entertain transactions of refunds advances or deductions of advances against salary

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 → `PAYROLL.LOAN_PAYMENT_MASTER_N` | VARCHAR2(12) | N |  | Self explainatory |
| 2 | **REFUND_NO** 🔑 → `PAYROLL.LOAN_REFUND_MASTER_N` | VARCHAR2(12) | N |  | Selef explainatory |
| 3 | **LOAN_AMOUNT** | NUMBER(20,2) | Y |  | Self explainatory |
| 4 | **REFUND_AMOUNT** | NUMBER(20,2) | N |  | Self explainatory |
| 5 | **TEMP_REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
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

- **Primary key** `PK_LOAN_REFUND_DETAIL_N` (LOAN_NO, REFUND_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_N1` (LOAN_NO) → `PAYROLL.LOAN_PAYMENT_MASTER_N` (LOAN_NO)
- **FK** `FK_LOAN_PAYMENT_DETAIL_N2` (REFUND_NO) → `PAYROLL.LOAN_REFUND_MASTER_N` (REFUND_NO)
- **Index** `IDX_LOAN_REFUND_DETAIL_N_2` (REFUND_NO)
- **Triggers**: `LOAN_REFUND_DETAIL_N_DEL` (AFTER DELETE), `LOAN_REFUND_DETAIL_N_INS` (BEFORE INSERT), `LOAN_REFUND_DETAIL_N_UPD` (BEFORE UPDATE)

### LOAN_REFUND_MASTER_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REFUND_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **TRANS_DATE** | DATE | Y |  |  |
| 3 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 4 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 5 | **MRNO** | VARCHAR2(14) | N |  |  |
| 6 | **REFUND_AMOUNT** | NUMBER(20,2) | N |  |  |
| 7 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 8 | **CANCELLED** | CHAR(1) | Y |  |  |
| 9 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 10 | **CANCELLED_VOUCHER_NO** | VARCHAR2(13) | Y |  |  |
| 11 | **REFUND_TYPE** | CHAR(1) | Y |  |  |
| 12 | **START_DATE** | DATE | Y |  |  |
| 13 | **END_DATE** | DATE | Y |  |  |
| 14 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 17 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **TRN_DATE** | DATE | Y |  |  |

- **Primary key** `PK_LOAN_REFUND_MASTER_TEST` (REFUND_NO)
- **Check** `CK_LOAN_REFUND_MASTER_TEST_1`: `(CANCELLED IN ('Y', 'N'))`
- **Check** `CK_LOAN_REFUND_MASTER_TEST_5`: `(REFUND_TYPE IN ('M', 'S'))`
- **Index** `IDX_LOAN_REFUND_MASTER_TEST_1` (MRNO)
- **Index** `IDX_LOAN_REFUND_MASTER_TEST_2` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `LOAN_REFUND_DETAIL_TEST`

### LOAN_REFUND_DETAIL_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 → `PAYROLL.LOAN_PAYMENT_MASTER_TEST` | VARCHAR2(12) | N |  |  |
| 2 | **REFUND_NO** 🔑 → `PAYROLL.LOAN_REFUND_MASTER_TEST` | VARCHAR2(12) | N |  |  |
| 3 | **START_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  |  |
| 4 | **END_DATE** → `DEFINITIONS.MONTHS` | DATE | Y |  |  |
| 5 | **LOAN_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **MRNO** → `HRD.INFORMATION` | VARCHAR2(14) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **TEMP_REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 15 | **REFUND_LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_LOAN_REFUND_DETAIL_TEST` (LOAN_NO, REFUND_NO)
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_1` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_2` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_3` (REFUND_NO) → `PAYROLL.LOAN_REFUND_MASTER_TEST` (REFUND_NO)
- **FK** `FK_LOAN_REFUND_DETAIL_TEST_4` (LOAN_NO) → `PAYROLL.LOAN_PAYMENT_MASTER_TEST` (LOAN_NO)
- **Index** `IDX_LOAN_REFUND_DETAIL_TEST_2` (REFUND_NO)

### LOAN_REFUND_OPENING

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **LOAN_NO** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **SR_NO** 🔑 | NUMBER(2) | N |  |  |
| 3 | **REFUND_DATE** | DATE | Y |  |  |
| 4 | **REFUND_TYPE** | CHAR(1) | Y |  |  |
| 5 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **ORG_ID** | VARCHAR2(3) | Y |  |  |
| 13 | **ZON_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **LOC_ID** | VARCHAR2(3) | Y |  |  |
| 15 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_LOAN_REFUND_OPENING` (LOAN_NO, SR_NO)
- **Triggers**: `LOAN_REFUND_OPENING_DEL` (AFTER DELETE), `LOAN_REFUND_OPENING_INS` (BEFORE INSERT), `LOAN_REFUND_OPENING_UPD` (BEFORE UPDATE)

### MANUAL_MONTH_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **SERIAL_NO** 🔑 | NUMBER(3) | N |  |  |
| 4 | **TRANS_DATE** | DATE | Y |  |  |
| 5 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 6 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 7 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 8 | **CANCEL_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 9 | **CANCEL_VOUCHER_NO** | CHAR(13) | Y |  |  |
| 10 | **STATUS** | CHAR(1) | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_MANUAL_MONTH_MASTER` (START_DATE, END_DATE, SERIAL_NO)
- **Referenced by**: `MANUAL_PAY_MASTER`

### MANUAL_PAY_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `PAYROLL.MANUAL_MONTH_MASTER` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `PAYROLL.MANUAL_MONTH_MASTER` | DATE | N |  |  |
| 3 | **SERIAL_NO** 🔑 → `PAYROLL.MANUAL_MONTH_MASTER` | NUMBER(3) | N |  |  |
| 4 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 5 | **AMOUNT** | NUMBER(7) | Y |  |  |
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

- **Primary key** `PK_MANUAL_PAY_MASTER` (START_DATE, END_DATE, SERIAL_NO, MRNO)
- **FK** `FK_MANUAL_PAY_MASTER` (START_DATE, END_DATE, SERIAL_NO) → `PAYROLL.MANUAL_MONTH_MASTER` (START_DATE, END_DATE, SERIAL_NO)
- **Referenced by**: `MANUAL_ALLOWANCE_DEDUCTION`

### MANUAL_ALLOWANCE_DEDUCTION

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `PAYROLL.MANUAL_PAY_MASTER` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `PAYROLL.MANUAL_PAY_MASTER` | DATE | N |  |  |
| 3 | **SERIAL_NO** 🔑 → `PAYROLL.MANUAL_PAY_MASTER` | NUMBER(3) | N |  |  |
| 4 | **MRNO** 🔑 → `PAYROLL.MANUAL_PAY_MASTER` | VARCHAR2(14) | N |  |  |
| 5 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 6 | **AMOUNT** | NUMBER(7) | Y |  |  |
| 7 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_MANUAL_ALLOWANCE_DEDUCTION` (START_DATE, END_DATE, SERIAL_NO, MRNO, AD_CODE)
- **FK** `FK_MANUAL_ALLOWANCE_DEDUCTION` (START_DATE, END_DATE, SERIAL_NO, MRNO) → `PAYROLL.MANUAL_PAY_MASTER` (START_DATE, END_DATE, SERIAL_NO, MRNO)

### MONTH_CHANGE_REQUEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REQUEST_NO** | NUMBER | N |  |  |
| 2 | **REQUEST_DATE** | DATE | Y | SYSDATE |  |
| 3 | **MON_START_DATE** | DATE | Y |  |  |
| 4 | **MON_END_DATE** | DATE | Y |  |  |
| 5 | **PAY_START_DATE** | DATE | Y |  |  |
| 6 | **PAY_END_DATE** | DATE | Y |  |  |
| 7 | **NEW_MON_START_DATE** | DATE | Y |  |  |
| 8 | **NEW_MON_END_DATE** | DATE | Y |  |  |
| 9 | **APPROVE_STATUS** | VARCHAR2(1) | Y |  | P = Pending, A = Approved, R = Rejected |
| 10 | **APPROVE_DATE** | DATE | Y |  |  |
| 11 | **APPROVE_BY** | VARCHAR2(14) | Y |  |  |
| 12 | **REMARKS** | VARCHAR2(2000) | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Triggers**: `MONTH_CHANGE_REQUEST_DEL` (AFTER DELETE), `MONTH_CHANGE_REQUEST_INS` (BEFORE INSERT), `MONTH_CHANGE_REQUEST_PQ` (BEFORE INSERT OR UPDATE), `MONTH_CHANGE_REQUEST_UPD` (BEFORE UPDATE)

### MONTH_CHANGE_REQUEST_TEMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_NAME** | VARCHAR2(2000) | Y |  |  |
| 2 | **RESULT_COUNT** | NUMBER | Y |  |  |
| 3 | **MON_START_DATE** | DATE | Y |  |  |
| 4 | **MON_END_DATE** | DATE | Y |  |  |


### PAY_AD_BALANCE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 | DATE | N |  |  |
| 3 | **END_DATE** 🔑 | DATE | N |  |  |
| 4 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 5 | **BALANCE_AMOUNT** | NUMBER(20,2) | Y | 0 |  |
| 6 | **LOAN_AMOUNT** | NUMBER(20,2) | Y | 0 |  |
| 7 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_AD_BALANCE` (MRNO, START_DATE, END_DATE, AD_CODE)
- **Triggers**: `PAY_AD_BALANCE_DEL` (AFTER DELETE), `PAY_AD_BALANCE_INS` (BEFORE INSERT), `PAY_AD_BALANCE_UPD` (BEFORE UPDATE)

### PAY_AD_BALANCE_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 | DATE | N |  |  |
| 3 | **END_DATE** 🔑 | DATE | N |  |  |
| 4 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 5 | **BALANCE_AMOUNT** | NUMBER(20,2) | Y | 0 |  |
| 6 | **LOAN_AMOUNT** | NUMBER(20,2) | Y | 0 |  |
| 7 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_PAY_AD_BALANCE_TEST` (MRNO, START_DATE, END_DATE, AD_CODE)

### PAY_MASTER

Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 3 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 4 | **SALARY_ON_CARD_SWIPE** | CHAR(1) | Y |  |  |
| 5 | **MONTH_DAYS** | NUMBER(2) | Y |  |  |
| 6 | **ACTUAL_WORKING_DAYS** | NUMBER(5) | Y |  |  |
| 7 | **ACTUAL_PERFORMED_DAYS** | NUMBER(5) | Y |  |  |
| 8 | **ACTUAL_WORKING_HOURS** | NUMBER(5) | Y |  |  |
| 9 | **ACTUAL_PERFORMED_HOURS** | NUMBER(5) | Y |  |  |
| 10 | **UNPAID_LEAVES** | NUMBER(2) | Y |  |  |
| 11 | **SALARY_DAYS** | NUMBER(2) | Y |  |  |
| 12 | **SALARY_DAYS_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 13 | **ACTUAL_BASIC** | NUMBER(20) | Y |  |  |
| 14 | **CALC_BASIC** | NUMBER(20) | Y |  |  |
| 15 | **CALC_BASIC_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 16 | **ACTUAL_PAY_RATE** | NUMBER(20,2) | Y |  |  |
| 17 | **CALC_PAY_RATE** | NUMBER(20,2) | Y |  |  |
| 18 | **CALC_PAY_RATE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 19 | **OTHER_ALLOWANCES** | NUMBER(20) | Y |  |  |
| 20 | **ARREARS** | NUMBER(20) | Y |  |  |
| 21 | **OVERTIME_HRS** | NUMBER(5) | Y |  |  |
| 22 | **OVERTIME_AMOUNT** | NUMBER(20) | Y |  |  |
| 23 | **NO_OF_NIGHTS** | NUMBER(2) | Y |  |  |
| 24 | **NIGHTS_AMOUNT** | NUMBER(20) | Y |  |  |
| 25 | **GROSS_PAYABLE** | NUMBER(20) | Y |  |  |
| 26 | **GROSS_PAYABLE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 27 | **LOAN_DEDUCTION** | NUMBER(20) | Y |  |  |
| 28 | **OTHER_DEDUCTION** | NUMBER(20) | Y |  |  |
| 29 | **NET_PAYABLE** | NUMBER(20) | Y |  |  |
| 30 | **NET_PAYABLE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 31 | **GROUP_INSURANCE** | NUMBER(20) | Y |  |  |
| 32 | **EOBI_BASE** | NUMBER(20) | Y |  |  |
| 33 | **ESSI_BASE** | NUMBER(20) | Y |  |  |
| 34 | **EOBI_PAYABLE** | NUMBER(20) | Y |  |  |
| 35 | **ESSI_PAYABLE** | NUMBER(20) | Y |  |  |
| 36 | **ECESS_BASE** | NUMBER(20) | Y |  |  |
| 37 | **ECESS_PAYABLE** | NUMBER(20) | Y |  |  |
| 38 | **P_FUND_AMOUNT** | NUMBER(22,2) | Y |  |  |
| 39 | **P_FUND_LOAN** | NUMBER(22,2) | Y |  |  |
| 40 | **POSTED** | CHAR(1) | Y |  |  |
| 41 | **PRACTICE_INCOME** | NUMBER(10,2) | Y | 0 |  |
| 42 | **PRACTICE_INCOME_TAX** | NUMBER(10,2) | Y | 0 |  |
| 43 | **VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 44 | **VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 45 | **CURRENCY_ID** → `DEFINITIONS.CURRENCY` | VARCHAR2(3) | Y |  |  |
| 46 | **CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y | 0.00 |  |
| 47 | **DAILY_WAGER** | CHAR(1) | Y |  |  |
| 48 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 49 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 50 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 51 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 52 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 53 | **TRN_DATE** | DATE | Y |  |  |
| 54 | **FIXED_ALLOWANCES** | NUMBER(7) | Y | 0 |  |
| 55 | **INCOME_TAX** | NUMBER(7) | Y | 0 |  |
| 56 | **EOBI_EMPLOYEE** | NUMBER(20,2) | Y |  |  |
| 57 | **DAILY_RATE** | NUMBER(4) | Y |  |  |
| 58 | **P_FUND_BALANCE** | NUMBER(20) | Y |  |  |
| 59 | **ACTUAL_MONTH_DAYS** | NUMBER(2) | Y |  |  |
| 60 | **BRANCH_ID** | VARCHAR2(3) | Y |  |  |
| 61 | **BANK_ID** | VARCHAR2(6) | Y |  |  |
| 62 | **PAYMENT_MODE** | CHAR(1) | Y |  |  |
| 63 | **BANK_ACCOUNT_NO** | VARCHAR2(50) | Y |  |  |
| 64 | **COST_CENTRE_ID** | CHAR(10) | Y |  |  |
| 65 | **LOAN_DEDUCTION_PI** | NUMBER(20,2) | Y |  |  |
| 66 | **LOAN_DEDUCTION_PENDING** | NUMBER(20,2) | Y |  |  |
| 67 | **CALCULATED_P_FUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 68 | **CALCULATED** | CHAR(1) | Y |  |  |
| 69 | **PI_BEFORE_DED** | NUMBER(20,2) | Y |  |  |
| 70 | **ATT_START_DATE** | DATE | Y |  |  |
| 71 | **ATT_END_DATE** | DATE | Y |  |  |
| 72 | **PREV_UNPAID_LEAVES** | NUMBER(5) | Y |  |  |
| 73 | **GL_SETUP_CODE** | CHAR(3) | Y |  |  |
| 74 | **DEPARTMENT** | VARCHAR2(60) | Y |  |  |
| 75 | **DESIGNATION** | VARCHAR2(255) | Y |  |  |
| 76 | **FIXED_ALLOWANCES_ON_CARD_SWIPE** | NUMBER(7) | Y |  |  |
| 77 | **SHORT_WORKING_HOUR** | NUMBER(5,2) | Y |  |  |
| 78 | **OTHER_ALLOWANCES_ON_CARD_SWIPE** | NUMBER(20) | Y |  |  |
| 79 | **ONLINE_ACCOUNT** | CHAR(1) | Y | 'N' |  |
| 80 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 81 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 82 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 83 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 84 | **GRADE_ID** | VARCHAR2(6) | Y |  |  |
| 85 | **PATIENT_TYPE_ID** | VARCHAR2(6) | Y |  |  |
| 86 | **REIMBURSEMENT** | NUMBER(20) | Y |  |  |
| 87 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 88 | **LOGIN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 89 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 90 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 91 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 92 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 93 | **IBAN** | VARCHAR2(68) | Y |  |  |

- **Primary key** `PK_PAY_MASTER` (MRNO, START_DATE, END_DATE)
- **FK** `FK_PAY_MASTER_1` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **FK** `FK_PAY_MASTER_2` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **FK** `FK_PAY_MASTER_3` (VOUCHER_TYPE, VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_PAY_MASTER_4` (CURRENCY_ID) → `DEFINITIONS.CURRENCY` (CURRENCY_ID) _DISABLED_
- **Index** `IDX_PAY_MASTER_1` (START_DATE, END_DATE)
- **Index** `IDX_PAY_MASTER_3` (END_DATE)
- **Referenced by**: `PAY_ALLOWANCE_DEDUCTION`, `PAY_LEAVES`
- **Triggers**: `PAY_MASTER_DEL` (AFTER DELETE), `PAY_MASTER_INS` (BEFORE INSERT), `PAY_MASTER_UPD` (BEFORE UPDATE)

### PAY_ALLOWANCE_DEDUCTION

Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `PAYROLL.PAY_MASTER` | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 → `PAYROLL.PAY_MASTER` | DATE | N |  |  |
| 3 | **END_DATE** 🔑 → `PAYROLL.PAY_MASTER` | DATE | N |  |  |
| 4 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 5 | **ACTUAL_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **CALC_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **CALC_AMOUNT_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns. |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **CALC_AMOUNT_GUARANTEE** | NUMBER(10) | Y |  |  |
| 15 | **PENDING_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 16 | **DED_FROM_PI** | NUMBER(20,2) | Y |  |  |
| 17 | **ATT_START_DATE** | DATE | Y |  |  |
| 18 | **ATT_END_DATE** | DATE | Y |  |  |
| 19 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 21 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 22 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 23 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 24 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 25 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 26 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_ALLOWANCE_DEDUCTION` (MRNO, START_DATE, END_DATE, AD_CODE)
- **FK** `FK_PAY_ALLOWANCE_DED` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **FK** `FK_PAY_ALLOWANCE_DEDUCTION_2` (MRNO, START_DATE, END_DATE) → `PAYROLL.PAY_MASTER` (MRNO, START_DATE, END_DATE)
- **Index** `IDX_PAY_ALLOWANCE_DEDUCTION_1` (AD_CODE)
- **Index** `IDX_TEMP_START_DATE` (START_DATE, END_DATE)
- **Triggers**: `PAY_ALLOWANCE_DEDUCTION_DEL` (AFTER DELETE), `PAY_ALLOWANCE_DEDUCTION_INS` (BEFORE INSERT), `PAY_ALLOWANCE_DEDUCTION_UPD` (BEFORE UPDATE)

### PAY_MASTER_TEST

Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 3 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 4 | **SALARY_ON_CARD_SWIPE** | CHAR(1) | Y |  |  |
| 5 | **MONTH_DAYS** | NUMBER(2) | Y |  |  |
| 6 | **ACTUAL_WORKING_DAYS** | NUMBER(5) | Y |  |  |
| 7 | **ACTUAL_PERFORMED_DAYS** | NUMBER(5) | Y |  |  |
| 8 | **ACTUAL_WORKING_HOURS** | NUMBER(5) | Y |  |  |
| 9 | **ACTUAL_PERFORMED_HOURS** | NUMBER(5) | Y |  |  |
| 10 | **UNPAID_LEAVES** | NUMBER(2) | Y |  |  |
| 11 | **SALARY_DAYS** | NUMBER(2) | Y |  |  |
| 12 | **SALARY_DAYS_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 13 | **ACTUAL_BASIC** | NUMBER(20) | Y |  |  |
| 14 | **CALC_BASIC** | NUMBER(20) | Y |  |  |
| 15 | **CALC_BASIC_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 16 | **ACTUAL_PAY_RATE** | NUMBER(20,2) | Y |  |  |
| 17 | **CALC_PAY_RATE** | NUMBER(20,2) | Y |  |  |
| 18 | **CALC_PAY_RATE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 19 | **OTHER_ALLOWANCES** | NUMBER(20) | Y |  |  |
| 20 | **ARREARS** | NUMBER(20) | Y |  |  |
| 21 | **OVERTIME_HRS** | NUMBER(5) | Y |  |  |
| 22 | **OVERTIME_AMOUNT** | NUMBER(20) | Y |  |  |
| 23 | **NO_OF_NIGHTS** | NUMBER(2) | Y |  |  |
| 24 | **NIGHTS_AMOUNT** | NUMBER(20) | Y |  |  |
| 25 | **GROSS_PAYABLE** | NUMBER(20) | Y |  |  |
| 26 | **GROSS_PAYABLE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 27 | **LOAN_DEDUCTION** | NUMBER(20) | Y |  |  |
| 28 | **OTHER_DEDUCTION** | NUMBER(20) | Y |  |  |
| 29 | **NET_PAYABLE** | NUMBER(20) | Y |  |  |
| 30 | **NET_PAYABLE_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 31 | **GROUP_INSURANCE** | NUMBER(20) | Y |  |  |
| 32 | **EOBI_BASE** | NUMBER(20) | Y |  |  |
| 33 | **ESSI_BASE** | NUMBER(20) | Y |  |  |
| 34 | **EOBI_PAYABLE** | NUMBER(20) | Y |  |  |
| 35 | **ESSI_PAYABLE** | NUMBER(20) | Y |  |  |
| 36 | **ECESS_BASE** | NUMBER(20) | Y |  |  |
| 37 | **ECESS_PAYABLE** | NUMBER(20) | Y |  |  |
| 38 | **P_FUND_AMOUNT** | NUMBER(20) | Y |  |  |
| 39 | **P_FUND_LOAN** | NUMBER(20) | Y |  |  |
| 40 | **POSTED** | CHAR(1) | Y |  |  |
| 41 | **PRACTICE_INCOME** | NUMBER(10,2) | Y |  |  |
| 42 | **PRACTICE_INCOME_TAX** | NUMBER(10,2) | Y |  |  |
| 43 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 44 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 45 | **CURRENCY_ID** | VARCHAR2(3) | Y |  |  |
| 46 | **CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y |  |  |
| 47 | **DAILY_WAGER** | CHAR(1) | Y |  |  |
| 48 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 49 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 50 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 51 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 52 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 53 | **TRN_DATE** | DATE | Y |  |  |
| 54 | **FIXED_ALLOWANCES** | NUMBER(7) | Y |  |  |
| 55 | **INCOME_TAX** | NUMBER(7) | Y |  |  |
| 56 | **EOBI_EMPLOYEE** | NUMBER(20,2) | Y |  |  |
| 57 | **DAILY_RATE** | NUMBER(4) | Y |  |  |
| 58 | **P_FUND_BALANCE** | NUMBER(20) | Y |  |  |
| 59 | **ACTUAL_MONTH_DAYS** | NUMBER(2) | Y |  |  |
| 60 | **BRANCH_ID** | VARCHAR2(3) | Y |  |  |
| 61 | **BANK_ID** | VARCHAR2(6) | Y |  |  |
| 62 | **PAYMENT_MODE** | CHAR(1) | Y |  |  |
| 63 | **BANK_ACCOUNT_NO** | VARCHAR2(50) | Y |  |  |
| 64 | **COST_CENTRE_ID** | CHAR(10) | Y |  |  |
| 65 | **LOAN_DEDUCTION_PI** | NUMBER(20,2) | Y |  |  |
| 66 | **LOAN_DEDUCTION_PENDING** | NUMBER(20,2) | Y |  |  |
| 67 | **CALCULATED_P_FUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 68 | **CALCULATED** | CHAR(1) | Y |  |  |
| 69 | **PI_BEFORE_DED** | NUMBER(20,2) | Y |  |  |
| 70 | **ATT_START_DATE** | DATE | Y |  |  |
| 71 | **ATT_END_DATE** | DATE | Y |  |  |
| 72 | **PREV_UNPAID_LEAVES** | NUMBER(5) | Y |  |  |
| 73 | **GL_SETUP_CODE** | CHAR(3) | Y |  |  |
| 74 | **DEPARTMENT** | VARCHAR2(60) | Y |  |  |
| 75 | **DESIGNATION** | VARCHAR2(255) | Y |  |  |
| 76 | **FIXED_ALLOWANCES_ON_CARD_SWIPE** | NUMBER(7) | Y |  |  |
| 77 | **SHORT_WORKING_HOUR** | NUMBER(5,2) | Y |  |  |
| 78 | **OTHER_ALLOWANCES_ON_CARD_SWIPE** | NUMBER(20) | Y |  |  |
| 79 | **ONLINE_ACCOUNT** | CHAR(1) | Y | 'N' |  |
| 80 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 81 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 82 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 83 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 84 | **GRADE_ID** | VARCHAR2(6) | Y |  |  |
| 85 | **PATIENT_TYPE_ID** | VARCHAR2(6) | Y |  |  |
| 86 | **REIMBURSEMENT** | NUMBER(20) | Y |  |  |
| 87 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 88 | **LOGIN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 89 | **IBAN** | VARCHAR2(68) | Y |  |  |

- **Primary key** `PK_PAY_MASTER_TEST` (MRNO, START_DATE, END_DATE)
- **FK** `FK_PAY_MASTER_TEST_1` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **Index** `IDX_PAY_MASTER_TEST_1` (START_DATE, END_DATE)
- **Index** `IDX_PAY_MASTER_TEST_3` (END_DATE)
- **Referenced by**: `PAY_ALLOWANCE_DEDUCTION_TEST`

### PAY_ALLOWANCE_DEDUCTION_TEST

Please consider “ON_CARD_SWIPE” as “WITHOUT_CARD_SWIPE” for the NUMBER columns.

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `PAYROLL.PAY_MASTER_TEST` | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 → `PAYROLL.PAY_MASTER_TEST` | DATE | N |  |  |
| 3 | **END_DATE** 🔑 → `PAYROLL.PAY_MASTER_TEST` | DATE | N |  |  |
| 4 | **AD_CODE** 🔑 → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 5 | **ACTUAL_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **CALC_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **CALC_AMOUNT_ON_CARD_SWIPE** | NUMBER(20) | Y |  | Please consider ON_CARD_SWIPE as WITHOUT_CARD_SWIPE for the NUMBER columns. |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **CALC_AMOUNT_GUARANTEE** | NUMBER(10) | Y |  |  |
| 15 | **PENDING_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 16 | **DED_FROM_PI** | NUMBER(20,2) | Y |  |  |
| 17 | **ATT_START_DATE** | DATE | Y |  |  |
| 18 | **ATT_END_DATE** | DATE | Y |  |  |
| 19 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 21 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 22 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_PAY_ALL_DED_TEST` (MRNO, START_DATE, END_DATE, AD_CODE)
- **FK** `FK_PAY_ALLOWANCE_DED_TEST` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **FK** `FK_PAY_ALL_DED_TEST_2` (MRNO, START_DATE, END_DATE) → `PAYROLL.PAY_MASTER_TEST` (MRNO, START_DATE, END_DATE)
- **Index** `IDX_PAY_ALL_DED_TEST_1` (AD_CODE)

### PAY_ARREAR

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **ARREAR_CODE** 🔑 | CHAR(3) | N |  |  |
| 4 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 5 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **TRN_DATE** | DATE | Y |  |  |
| 12 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 15 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 16 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 17 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 18 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_ARREAR` (MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE)
- **Triggers**: `PAY_ARREAR_DEL` (AFTER DELETE), `PAY_ARREAR_INS` (BEFORE INSERT), `PAY_ARREAR_UPD` (BEFORE UPDATE)

### PAY_ARREAR_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **ARREAR_CODE** 🔑 | CHAR(3) | N |  |  |
| 4 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 5 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 6 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Primary key** `PK_PAY_ARREAR_TEST` (MRNO, START_DATE, END_DATE, AD_CODE, ARREAR_CODE)

### PAY_DAILY_AD_TEST

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_START_DATE** 🔑 | DATE | N |  |  |
| 2 | **PAY_END_DATE** 🔑 | DATE | N |  |  |
| 3 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 4 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 5 | **DAY** 🔑 | DATE | N |  |  |
| 6 | **ATTENDANCE_BASED** | CHAR(1) | N |  |  |
| 7 | **INCLUDE_IN_GROSS** | CHAR(1) | N |  |  |
| 8 | **LEAVE_TYPE_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **PAYMENT_FACTOR** | NUMBER(5,2) | Y |  |  |
| 10 | **AD_NATURE_TYPE_ID** | VARCHAR2(3) | N |  |  |
| 11 | **AD_TYPE** | CHAR(1) | N |  |  |
| 12 | **ACTUAL_SALARY** | NUMBER(20,4) | Y |  |  |
| 13 | **CALC_SALARY** | NUMBER(20,4) | Y |  |  |
| 14 | **CALC_SALARY_ON_CARD_SWIPE** | NUMBER(20,4) | Y |  |  |
| 15 | **ACTUAL_PERFORM_TIME** | NUMBER(9) | Y |  |  |
| 16 | **ACTUAL_WORKING_TIME** | NUMBER(9) | Y |  |  |

- **Primary key** `PK_PAY_DAILY_AD_TEST` (MRNO, PAY_START_DATE, PAY_END_DATE, AD_CODE, DAY)
- **Index** `PAY_DAILY_AD_TEST_IDX1` (PAY_START_DATE, PAY_END_DATE, MRNO)

### PAY_DAILY_TEMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 3 | **START_DATE** | DATE | Y |  |  |
| 4 | **END_DATE** | DATE | Y |  |  |
| 5 | **DAY** 🔑 | DATE | N |  |  |
| 6 | **AMOUNT** | NUMBER(10,2) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |

- **Primary key** `PK_PAY_DAILY_TEMP` (MRNO, AD_CODE, DAY)
- **Index** `IDX_PAY_DAILY_TEMP_1` (MRNO, START_DATE, END_DATE, AD_CODE)

### PAY_DAILY_TEMP_UNPAID

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 3 | **START_DATE** | DATE | Y |  |  |
| 4 | **END_DATE** | DATE | Y |  |  |
| 5 | **DAY** 🔑 | DATE | N |  |  |
| 6 | **AMOUNT** | NUMBER(10,2) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ATTENDANCE_BASED** | CHAR(1) | Y |  |  |
| 10 | **INCLUDE_IN_GROSS** | CHAR(1) | Y |  |  |
| 11 | **LEAVE_TYPE_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **PAYMENT_FACTOR** | NUMBER(5,2) | Y |  |  |
| 13 | **AD_NATURE_TYPE_ID** | VARCHAR2(3) | Y |  |  |
| 14 | **AD_TYPE** | CHAR(1) | Y |  |  |
| 15 | **AMOUNT_ON_CARD_SWIPE** | NUMBER(20,2) | Y |  |  |
| 16 | **ACTUAL_AMOUNT** | NUMBER(20,2) | Y |  |  |

- **Primary key** `PK_PAY_DAILY_TEMP_UNPAID` (MRNO, AD_CODE, DAY)
- **Index** `IDX_PAY_DAILY_TEMP_UNPAID_1` (MRNO, START_DATE, END_DATE, AD_CODE)
- **Index** `PAY_DAILY_TEMP_UNPAID_IDX1` (START_DATE, END_DATE, MRNO)

### PAY_DR_FEE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** | DATE | Y |  |  |
| 2 | **END_DATE** | DATE | Y |  |  |
| 3 | **DOCTOR_MRNO** | VARCHAR2(14) | Y |  |  |
| 4 | **GUARANTEE_MONEY** | NUMBER(10,2) | Y |  |  |
| 5 | **DR_FEE_GROSS** | NUMBER(10,2) | Y |  |  |
| 6 | **DR_FEE_NET** | NUMBER(10,2) | Y |  |  |
| 7 | **DR_FEE_CALC** | NUMBER(10,2) | Y |  |  |
| 8 | **DR_FEE_WAIVED** | NUMBER(10,2) | Y |  |  |
| 9 | **PREV_REALIZED** | NUMBER(10,2) | Y |  |  |
| 10 | **CURR_REALIZED** | NUMBER(10,2) | Y |  |  |
| 11 | **SESSION_PAYMENT** | NUMBER(10,2) | Y |  |  |
| 12 | **GROSS_PAYABLE** | NUMBER(10,2) | Y |  |  |
| 13 | **INCOME_TAX** | NUMBER(10,2) | Y |  |  |
| 14 | **NET_PAYABLE** | NUMBER(10,2) | Y |  |  |
| 15 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 18 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 19 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 20 | **TRN_DATE** | DATE | Y |  |  |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 24 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### PAY_EXCEPTIONAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **START_DATE** | DATE | Y |  |  |
| 3 | **END_DATE** | DATE | Y |  |  |
| 4 | **ACTUAL_BASIC** | NUMBER(20,2) | Y |  |  |
| 5 | **ACTUAL_PAY_RATE** | NUMBER(20,2) | Y |  |  |
| 6 | **DAILY_WAGER** | CHAR(1) | Y |  |  |
| 7 | **DAILY_RATE** | NUMBER(4) | Y |  |  |


### PAY_ITAX_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 | DATE | N |  |  |
| 3 | **END_DATE** 🔑 | DATE | N |  |  |
| 4 | **AD_CODE** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | CHAR(3) | N |  |  |
| 5 | **SETUP_TAX** | NUMBER(12,2) | Y |  |  |
| 6 | **PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 7 | **DEDUCTED_TAX** | NUMBER(12,2) | Y |  |  |
| 8 | **EXPECTED_YEARLY_TAXABLE_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 9 | **EXPECTED_YEARLY_TAX** | NUMBER(12,2) | Y |  |  |
| 10 | **YEARLY_PAID_TAX** | NUMBER(12,2) | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **SELECT_FLAG** | CHAR(1) | Y | 'N' |  |
| 18 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 19 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 20 | **AD_ORGANIZATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 21 | **AD_LOCATION_ID** → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` | VARCHAR2(3) | Y |  |  |
| 22 | **LOG** | VARCHAR2(4000) | Y |  |  |
| 23 | **ACTUAL_PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 24 | **MONTH_REMAINING** | NUMBER(2) | Y |  |  |
| 25 | **CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y |  |  |
| 26 | **LAST_MON_END_DATE** | DATE | Y |  |  |
| 27 | **UNPAID_LEAVE_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 28 | **TAX_PAID_SALARY** | NUMBER(12,2) | Y |  |  |
| 29 | **TAX_PAID_DIRECT** | NUMBER(12,2) | Y |  |  |
| 30 | **TAX_PAID_ADJUST** | NUMBER(12,2) | Y |  |  |
| 31 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 32 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 33 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 34 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |
| 35 | **UNDISTRIBUTED_TAX** | NUMBER(12,2) | Y |  |  |
| 36 | **SLAB_PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 37 | **DAYS_PERCENTAGE** | NUMBER(5,2) | Y | 100 |  |
| 38 | **MANUAL_CALCULATION** | VARCHAR2(1) | Y | 'N' |  |
| 39 | **REVISED_TAXABLE_INCOME** | NUMBER(12,2) | Y |  |  |
| 40 | **REVISED_TAX_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 41 | **REVISED_CURR_MON_TAX** | NUMBER(12,2) | Y |  |  |
| 42 | **CURR_MON_GROSS_PAYABLE** | NUMBER(12,2) | Y |  |  |
| 43 | **CURR_MON_PF** | NUMBER(12,2) | Y |  |  |
| 44 | **CURR_MON_PF_TAXABLE** | NUMBER(12,2) | Y |  |  |
| 45 | **PREVIOUS_PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 46 | **PREVIOUS_ACTUAL_PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 47 | **TOTAL_INCOME_TODATE** | NUMBER(12,2) | Y |  |  |
| 48 | **TAX_PAID_TILL_MONTH** | NUMBER(12,2) | Y |  |  |
| 49 | **TAX_ADJUSTED** | NUMBER(12,2) | Y |  |  |
| 50 | **REVISED_CURR_MON_GROSS_WITH_PF** | NUMBER(12,2) | Y |  |  |
| 51 | **REVISED_YTD_PAID_INCOME** | NUMBER(12,2) | Y |  |  |
| 52 | **REVISED_YTD_PAID_TAX** | NUMBER(12,2) | Y |  |  |
| 53 | **TAX_ADJUSTED_MONTHLY** | NUMBER(12,2) | Y |  |  |
| 54 | **REV_CURR_MON_NC_TAX** | NUMBER(12,2) | Y |  |  |
| 55 | **TAX_TO_BEPAID_TILL_MONTH** | NUMBER(12,2) | Y |  |  |

- **Primary key** `PK_PAY_ITAX_DETAIL` (MRNO, START_DATE, END_DATE)
- **FK** `FK_PAY_ITAX_DETAIL` (AD_CODE, AD_ORGANIZATION_ID, AD_LOCATION_ID) → `PAYROLL.DEF_ALLOWANCE_DEDUCTION` (AD_CODE, ORGANIZATION_ID, LOCATION_ID) _DISABLED_
- **Triggers**: `PAY_ITAX_DETAIL_DEL` (AFTER DELETE), `PAY_ITAX_DETAIL_INS` (BEFORE INSERT), `PAY_ITAX_DETAIL_UPD` (BEFORE UPDATE)

### PAY_ITAX_DETAIL_HISTORY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** | DATE | N |  |  |
| 3 | **END_DATE** | DATE | N |  |  |
| 4 | **AD_CODE** | CHAR(3) | N |  |  |
| 5 | **SETUP_TAX** | NUMBER(12,2) | Y |  |  |
| 6 | **PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 7 | **DEDUCTED_TAX** | NUMBER(12,2) | Y |  |  |
| 8 | **EXPECTED_YEARLY_TAXABLE_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 9 | **EXPECTED_YEARLY_TAX** | NUMBER(12,2) | Y |  |  |
| 10 | **YEARLY_PAID_TAX** | NUMBER(12,2) | Y |  |  |
| 11 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **SELECT_FLAG** | CHAR(1) | Y |  |  |


### PAY_ITAX_DTL_TMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **PAYROLL_LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 4 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 5 | **NAME** | VARCHAR2(500) | Y |  |  |
| 6 | **DESIGNATION** | VARCHAR2(1000) | Y |  |  |
| 7 | **DEPARTMENT_ID** | VARCHAR2(25) | Y |  |  |
| 8 | **DEPARTMENT** | VARCHAR2(1000) | Y |  |  |
| 9 | **GRADE** | VARCHAR2(60) | Y |  |  |
| 10 | **EMP_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **CURRENT_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 12 | **PREVIOUS_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 13 | **DIFFERENCE** | NUMBER(20,2) | Y |  |  |
| 14 | **PERCENTAGE** | NUMBER(5,2) | Y |  |  |
| 15 | **CRITERIA_ID** 🔑 | NUMBER(2) | N |  |  |

- **Primary key** `PK_PAY_ITAX_DTL_TMP` (CRITERIA_ID, START_DATE, END_DATE, PAYROLL_LOCATION_ID, MRNO)

### PAY_ITAX_INCOME_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 | DATE | N |  |  |
| 3 | **END_DATE** 🔑 | DATE | N |  |  |
| 4 | **PARAMETER** 🔑 | VARCHAR2(32) | N |  |  |
| 5 | **AMOUNT** | NUMBER(15,3) | Y |  |  |

- **Primary key** `PK_PAY_ITAX_INCOME_DETAIL` (MRNO, START_DATE, END_DATE, PARAMETER)
- **Index** `PAY_ITAX_INCOME_DET_IDX` (START_DATE, END_DATE, PARAMETER)

### PAY_LEAVES

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 → `PAYROLL.PAY_MASTER` | VARCHAR2(14) | N |  |  |
| 2 | **START_DATE** 🔑 → `PAYROLL.PAY_MASTER` | DATE | N |  |  |
| 3 | **END_DATE** 🔑 → `PAYROLL.PAY_MASTER` | DATE | N |  |  |
| 4 | **LEAVE_TYPE_ID** 🔑 → `HRD.LEAVE_TYPE` | VARCHAR2(3) | N |  |  |
| 5 | **OPENING_BALANCE** | NUMBER(3) | Y |  |  |
| 6 | **AVAILED** | NUMBER(3) | Y |  |  |
| 7 | **CLOSING_BALANCE** | NUMBER(3) | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_LEAVES` (MRNO, START_DATE, END_DATE, LEAVE_TYPE_ID)
- **FK** `FK_PAY_LEAVES_1` (LEAVE_TYPE_ID) → `HRD.LEAVE_TYPE` (LEAVE_TYPE_ID) _DISABLED_
- **FK** `FK_PAY_LEAVES_2` (MRNO, START_DATE, END_DATE) → `PAYROLL.PAY_MASTER` (MRNO, START_DATE, END_DATE) _DISABLED_
- **Index** `IDX_PAY_LEAVES_1` (MRNO, START_DATE, LEAVE_TYPE_ID)
- **Triggers**: `PAY_LEAVES_DEL` (AFTER DELETE), `PAY_LEAVES_INS` (BEFORE INSERT), `PAY_LEAVES_UPD` (BEFORE UPDATE)

### PAY_PF_VOUCHER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 2 | **VOUCHER_TYPE_CONTRIBUTION** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 3 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 4 | **VOUCHER_NO_CONTRIBUTION** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 5 | **MRNO** 🔑 → `HRD.INFORMATION` | VARCHAR2(14) | N |  |  |
| 6 | **EMPLOYEE_CONTRIBUTION** | NUMBER(20,2) | Y |  |  |
| 7 | **EMPLOYER_CONTRIBUTION** | NUMBER(20,2) | Y |  |  |
| 8 | **VOUCHER_TYPE_LOAN_ADJUST** | VARCHAR2(5) | Y |  |  |
| 9 | **VOUCHER_NO_LOAN_ADJUST** | VARCHAR2(13) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_PF_VOUCHER` (START_DATE, END_DATE, MRNO)
- **FK** `FK_PAY_PF_VOUCHER_1` (VOUCHER_TYPE_CONTRIBUTION, VOUCHER_NO_CONTRIBUTION) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_PAY_PF_VOUCHER_2` (MRNO) → `HRD.INFORMATION` (MRNO) _DISABLED_
- **FK** `FK_PAY_PF_VOUCHER_3` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **Index** `IDX_PAY_PF_VOUCHER_1` (VOUCHER_TYPE_CONTRIBUTION, VOUCHER_NO_CONTRIBUTION)
- **Index** `IDX_PAY_PF_VOUCHER_2` (MRNO)
- **Triggers**: `PAY_PF_VOUCHER_DEL` (AFTER DELETE), `PAY_PF_VOUCHER_INS` (BEFORE INSERT), `PAY_PF_VOUCHER_UPD` (BEFORE UPDATE)

### PAY_REPORT_FILE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_CODE** 🔑 | NUMBER(2) | N |  |  |
| 2 | **REPORT_TITLE** | VARCHAR2(255) | Y |  |  |
| 3 | **SUMMARY_DETAIL** | CHAR(1) | Y |  |  |
| 4 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 5 | **ACTIVE** | CHAR(1) | Y |  |  |
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

- **Primary key** `PK_PAY_REPORT_FILE` (REPORT_CODE)
- **Referenced by**: `PAY_REPORT_ROUTING`

### PAY_REPORT_FORMAT

This table is used to define groups of different allowances / deductions, this group will be used into formatting salary sheets

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **AD_GROUP_CODE** 🔑 | CHAR(3) | N |  | PK-Self explainatory |
| 2 | **DESCRIPTION** | VARCHAR2(255) | Y |  | Group description (House Rent, Utilities, Income Tax, Others etc.) |
| 3 | **SHORT_DESCRIPTION** | VARCHAR2(10) | Y |  | Short description of Group, to be displayed onto Salary Sheet |
| 4 | **ACTIVE** | CHAR(1) | Y | 'Y' | Either record is available currently for transactions or not |
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

- **Primary key** `PK_DEF_ALLOW_DEDUCT_GROUP` (AD_GROUP_CODE)
- **Check** `CK_DEF_ALLOW_DEDUCT_GROUP_1`: `(ACTIVE IN ('Y', 'N'))`
- **Referenced by**: `PAY_REPORT_ROUTING`

### PAY_REPORT_ROUTING

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REPORT_CODE** 🔑 → `PAYROLL.PAY_REPORT_FILE` | NUMBER(2) | N |  |  |
| 2 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 3 | **AD_GROUP_CODE** 🔑 → `PAYROLL.PAY_REPORT_FORMAT` | CHAR(3) | N |  |  |
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

- **Primary key** `PK_PAY_REPORT_ROUTING` (REPORT_CODE, AD_CODE, AD_GROUP_CODE)
- **FK** `FK_PAY_REPORT_ROUTING_1` (REPORT_CODE) → `PAYROLL.PAY_REPORT_FILE` (REPORT_CODE)
- **FK** `FK_PAY_REPORT_ROUTING_2` (AD_GROUP_CODE) → `PAYROLL.PAY_REPORT_FORMAT` (AD_GROUP_CODE)
- **Index** `IDX_PAY_REPORT_ROUTING_2` (AD_GROUP_CODE)
- **Index** `IDX_PAY_REPORT_ROUTING_3` (AD_CODE)

### PAY_STATUS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SERIAL_NO** 🔑 | NUMBER(7) | N |  | Unique serial number |
| 2 | **MRNO** | VARCHAR2(14) | N |  | Save employee code |
| 3 | **DATE_FROM** | DATE | N |  | Save salary month start date |
| 4 | **DATE_TO** | DATE | N |  | Save salary month end date |
| 5 | **STATUS** | CHAR(1) | N |  | 'S' = 'Stop Payment' |
| 6 | **DISCIPLINARY_REASON_ID** | VARCHAR2(6) | Y |  |  |
| 7 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_COMMENTS** | VARCHAR2(2000) | Y |  | Save user remarks |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_STATUS` (SERIAL_NO)
- **Unique** `UK_PAY_STATUS_1` (MRNO, DATE_FROM, DATE_TO)
- **Check** `CHK_PAY_STATUS_01`: `(STATUS IN ('N','S'))`
- **Triggers**: `PAY_STATUS_DEL` (AFTER DELETE), `PAY_STATUS_INS` (BEFORE INSERT), `PAY_STATUS_UPD` (BEFORE UPDATE)

### PAY_TMP_BANK

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **BRANCH_ID** | VARCHAR2(3) | Y |  |  |
| 2 | **BRANCH_DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 3 | **BANK_ID** | VARCHAR2(6) | Y |  |  |
| 4 | **BANK_DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 5 | **SELECTED** | CHAR(1) | Y |  |  |
| 6 | **USERID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **PARENT_BRANCH_ID** | VARCHAR2(3) | Y |  |  |


### PAY_TMP_EMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **NAME** | VARCHAR2(255) | Y |  |  |
| 3 | **SELECT_FLAG** | CHAR(1) | Y |  |  |
| 4 | **START_DATE** | DATE | Y |  |  |
| 5 | **END_DATE** | DATE | Y |  |  |
| 6 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 7 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **LOG** | VARCHAR2(4000) | Y |  |  |
| 9 | **ERROR_TEXT** | VARCHAR2(4000) | Y |  |  |
| 10 | **PAYROLL_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **LOGIN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Index** `IDX_PAY_TEMP_EMP_1` (SELECT_FLAG, MRNO)

### PAY_TMP_MPA

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GROUP_CODE** | CHAR(3) | Y |  |  |
| 2 | **GROUP_NAME** | VARCHAR2(255) | Y |  |  |
| 3 | **DIV_CODE** | CHAR(3) | Y |  |  |
| 4 | **DIV_NAME** | VARCHAR2(255) | Y |  |  |
| 5 | **DEPT_CODE** | CHAR(3) | Y |  |  |
| 6 | **DEPT_NAME** | VARCHAR2(255) | Y |  |  |
| 7 | **NO_OF_EMP_1** | NUMBER(5) | Y |  |  |
| 8 | **SALARY_1** | NUMBER(20,2) | Y |  |  |
| 9 | **NO_OF_EMP_2** | NUMBER(5) | Y |  |  |
| 10 | **SALARY_2** | NUMBER(20,2) | Y |  |  |
| 11 | **NO_OF_EMP_3** | NUMBER(5) | Y |  |  |
| 12 | **SALARY_3** | NUMBER(20,2) | Y |  |  |
| 13 | **NO_OF_EMP_CHANGE** | NUMBER(5) | Y |  |  |
| 14 | **SALARY_CHANGE** | NUMBER(20,2) | Y |  |  |
| 15 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **NO_OF_EMP_0** | NUMBER(5) | Y |  |  |
| 18 | **SALARY_0** | NUMBER(20,2) | Y |  |  |
| 19 | **NO_OF_EMP_CHANGE2** | NUMBER(5) | Y |  |  |
| 20 | **SALARY_CHANGE2** | NUMBER(20,2) | Y |  |  |


### PAY_TMP_REPORT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **NAME** | VARCHAR2(183) | Y |  |  |
| 3 | **COST_CENTRE_ID** | CHAR(10) | Y |  |  |
| 4 | **COST_CENTRE_DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 5 | **RATE_OF_PAY** | NUMBER(20,2) | Y |  |  |
| 6 | **G_BASIC** | NUMBER(20,2) | Y |  |  |
| 7 | **G_HOUSE_RENT** | NUMBER(20,2) | Y |  |  |
| 8 | **G_UTILITIES** | NUMBER(20,2) | Y |  |  |
| 9 | **G_CONVEYANCE** | NUMBER(20,2) | Y |  |  |
| 10 | **G_OTHER_ALLOWANCES** | NUMBER(20,2) | Y |  |  |
| 11 | **G_OVERTIME** | NUMBER(20,2) | Y |  |  |
| 12 | **G_NIGHT_ALLOWANCE** | NUMBER(20,2) | Y |  |  |
| 13 | **G_TOTAL_GROSS** | NUMBER(20,2) | Y |  |  |
| 14 | **D_PROVIDENT_FUND** | NUMBER(20,2) | Y |  |  |
| 15 | **D_INCOME_TAX** | NUMBER(20,2) | Y |  |  |
| 16 | **D_LOAN** | NUMBER(20,2) | Y |  |  |
| 17 | **D_OTHER_DEDUCTIONS** | NUMBER(20,2) | Y |  |  |
| 18 | **D_TOTAL_DEDUCTIONS** | NUMBER(20,2) | Y |  |  |
| 19 | **NET_SALARY** | NUMBER(20,2) | Y |  |  |
| 20 | **PAYMENT_MODE** | CHAR(1) | Y |  |  |
| 21 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 22 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 23 | **TRN_DATE** | DATE | Y |  |  |
| 24 | **SALARY_DAYS** | NUMBER(2) | Y |  |  |
| 25 | **CURRENCY_EXCHANGE_RATE** | NUMBER(10,2) | Y |  |  |
| 26 | **CURRENCY_ID** | VARCHAR2(3) | Y |  |  |
| 27 | **PRACTICE_INCOME_TAX** | NUMBER(10,2) | Y | 0 |  |
| 28 | **PRACTICE_INCOME** | NUMBER(10,2) | Y |  |  |
| 29 | **GL_SETUP_CODE** | CHAR(3) | Y |  |  |
| 30 | **PI_BEFORE_DED** | NUMBER(20,2) | Y | 0 |  |
| 31 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 32 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 33 | **D_ELECTRICITY_BILL** | NUMBER(20,2) | Y |  |  |
| 34 | **D_GAS_BILL** | NUMBER(20,2) | Y |  |  |


### PAY_VOUCHER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 3 | **SERIAL_NO** 🔑 | NUMBER(2) | N |  |  |
| 4 | **PF_VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 5 | **PF_VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 6 | **GL_VOUCHER_TYPE** → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | Y |  |  |
| 7 | **GL_VOUCHER_NO** → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | Y |  |  |
| 8 | **LOAN_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 9 | **LOAN_VOUCHER_NO** | VARCHAR2(13) | Y |  |  |
| 10 | **PF_CANCELLED** | CHAR(1) | Y | 'N' |  |
| 11 | **GL_CANCELLED** | CHAR(1) | Y | 'N' |  |
| 12 | **LOAN_CANCELLED** | CHAR(1) | Y | 'N' |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **TRN_DATE** | DATE | Y |  |  |
| 19 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 20 | **GP_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 21 | **GP_VOUCHER_NO** | CHAR(13) | Y |  |  |
| 22 | **GP_CANCELLED** | CHAR(1) | Y | 'N' |  |
| 23 | **CP_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 24 | **CP_VOUCHER_NO** | CHAR(13) | Y |  |  |
| 25 | **CP_CANCELLED** | CHAR(1) | Y | 'N' |  |
| 26 | **PAY_VOUCHER_TYPE** | VARCHAR2(2) | Y |  | i.e. GP, PF, CP, GL, LN |
| 27 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  | Voucher type for any pay voucher type |
| 28 | **VOUCHER_NO** | CHAR(13) | Y |  | Voucher No for any pay voucher type |
| 29 | **CANCELLED** | CHAR(1) | Y | 'N' | Voucher cancellation status for any pay voucher type |
| 30 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 31 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 32 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 33 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_VOUCHER` (START_DATE, END_DATE, SERIAL_NO, LOCATION_ID)
- **FK** `FK_PAY_VOUCHER_1` (PF_VOUCHER_TYPE, PF_VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_PAY_VOUCHER_2` (GL_VOUCHER_TYPE, GL_VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_PAY_VOUCHER_3` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **Check** `CK_PAY_VOUCHER_1`: `(PF_CANCELLED IN ('Y','N'))`
- **Check** `CK_PAY_VOUCHER_2`: `(GL_CANCELLED IN ('Y','N'))`
- **Check** `CK_PAY_VOUCHER_3`: `(LOAN_CANCELLED IN ('Y','N'))`
- **Index** `IDX_PAY_VOUCHER_1` (PF_VOUCHER_TYPE, PF_VOUCHER_NO)
- **Index** `IDX_PAY_VOUCHER_2` (GL_VOUCHER_TYPE, GL_VOUCHER_NO)
- **Triggers**: `PAY_VOUCHER_DEL` (AFTER DELETE), `PAY_VOUCHER_INS` (BEFORE INSERT), `PAY_VOUCHER_UPD` (BEFORE UPDATE)

### PAY_VOUCHER_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `DEFINITIONS.MONTHS` | DATE | N |  |  |
| 3 | **VOUCHER_TYPE** 🔑 → `FINANCE.GL_TRAN_MASTER` | VARCHAR2(5) | N |  |  |
| 4 | **VOUCHER_NO** 🔑 → `FINANCE.GL_TRAN_MASTER` | CHAR(13) | N |  |  |
| 5 | **TRANS_DATE** | DATE | Y |  |  |
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

- **Primary key** `PK_PAY_VOUCHER_MASTER` (START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO)
- **FK** `FK_PAY_VOUCHER_MASTER_1` (VOUCHER_TYPE, VOUCHER_NO) → `FINANCE.GL_TRAN_MASTER` (VOUCHER_TYPE, VOUCHER_NO) _DISABLED_
- **FK** `FK_PAY_VOUCHER_MASTER_2` (START_DATE, END_DATE) → `DEFINITIONS.MONTHS` (START_DATE, END_DATE) _DISABLED_
- **Index** `IDX_PAY_VOUCHER_MASTER_1` (VOUCHER_TYPE, VOUCHER_NO)
- **Referenced by**: `PAY_VOUCHER_DETAIL`
- **Triggers**: `PAY_VOUCHER_MASTER_DEL` (AFTER DELETE), `PAY_VOUCHER_MASTER_INS` (BEFORE INSERT), `PAY_VOUCHER_MASTER_UPD` (BEFORE UPDATE)

### PAY_VOUCHER_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 → `PAYROLL.PAY_VOUCHER_MASTER` | DATE | N |  |  |
| 2 | **END_DATE** 🔑 → `PAYROLL.PAY_VOUCHER_MASTER` | DATE | N |  |  |
| 3 | **VOUCHER_TYPE** 🔑 → `PAYROLL.PAY_VOUCHER_MASTER` | VARCHAR2(5) | N |  |  |
| 4 | **VOUCHER_NO** 🔑 → `PAYROLL.PAY_VOUCHER_MASTER` | CHAR(13) | N |  |  |
| 5 | **COA_CODE** 🔑 → `FINANCE.GL_COA` | VARCHAR2(100) | N |  |  |
| 6 | **LEDGER_TYPE_CODE** 🔑 → `FINANCE.GL_SUB_LEDGERS` | NUMBER(4) | N |  |  |
| 7 | **SUB_LDGR_ITEM_CODE** 🔑 → `FINANCE.GL_SUB_LEDGERS` | VARCHAR2(18) | N |  |  |
| 8 | **DR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 9 | **CR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PAY_VOUCHER_DETAIL` (START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO, COA_CODE, LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **FK** `FK_PAY_VOUCHER_DETAIL_1` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE) → `FINANCE.GL_SUB_LEDGERS` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **FK** `FK_PAY_VOUCHER_DETAIL_2` (COA_CODE) → `FINANCE.GL_COA` (COA_CODE)
- **FK** `FK_PAY_VOUCHER_DETAIL_3` (START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO) → `PAYROLL.PAY_VOUCHER_MASTER` (START_DATE, END_DATE, VOUCHER_TYPE, VOUCHER_NO)
- **Index** `IDX_PAY_VOUCHER_DETAIL_1` (LEDGER_TYPE_CODE, SUB_LDGR_ITEM_CODE)
- **Index** `IDX_PAY_VOUCHER_DETAIL_2` (COA_CODE)
- **Triggers**: `PAY_VOUCHER_DETAIL_DEL` (AFTER DELETE), `PAY_VOUCHER_DETAIL_INS` (BEFORE INSERT), `PAY_VOUCHER_DETAIL_UPD` (BEFORE UPDATE)

### PAY_VOUCHER_TEMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **GL_SETUP_CODE** | CHAR(3) | Y |  |  |
| 2 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 3 | **SERIAL_NO** | NUMBER(3) | Y |  |  |
| 4 | **START_DATE** | DATE | N |  |  |
| 5 | **STATIC_DESCRIPTION** | VARCHAR2(20) | Y |  |  |
| 6 | **END_DATE** | DATE | N |  |  |
| 7 | **AD_CODE** | CHAR(3) | Y |  |  |
| 8 | **LOAN_CODE** | CHAR(3) | Y |  |  |
| 9 | **COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 10 | **LEDGER_TYPE_CODE_DR** | NUMBER(4) | Y |  |  |
| 11 | **SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |
| 12 | **COA_CODE_CR** | VARCHAR2(100) | Y |  |  |
| 13 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  |  |
| 14 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  |  |
| 15 | **TRANSACTION_TYPE** | CHAR(1) | Y | 'O' |  |
| 16 | **STATIC_TYPE** | CHAR(1) | Y | 'G' |  |
| 17 | **DR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 18 | **CR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 19 | **ARREAR_CODE** | CHAR(3) | Y |  |  |
| 20 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |

- **Check** `CK_PAY_VOUCHER_TEMP_1`: `(TRANSACTION_TYPE IN ('S', 'L', 'A', 'D', 'O'))`
- **Index** `IDX_PAY_VOUCHER_TEMP_1` (GL_SETUP_CODE, SERIAL_NO)
- **Index** `IDX_PAY_VOUCHER_TEMP_2` (MRNO, START_DATE, END_DATE)

### PAY_VOUCHER_TMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PAY_START_DATE** 🔑 | DATE | N |  |  |
| 2 | **PAY_END_DATE** 🔑 | DATE | N |  |  |
| 3 | **PAY_VOUCHER_TYPE** 🔑 | VARCHAR2(2) | N |  |  |
| 4 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 5 | **SERIAL_NO** 🔑 | NUMBER | N |  |  |
| 6 | **PAY_VOUCHER_SETUP_ID** | VARCHAR2(3) | N |  |  |
| 7 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 8 | **EMP_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 10 | **LEDGER_TYPE_CODE_DR** | NUMBER(4) | Y |  |  |
| 11 | **SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |
| 12 | **COA_CODE_CR** | VARCHAR2(100) | Y |  |  |
| 13 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  |  |
| 14 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  |  |
| 15 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 16 | **AD_CODE** | CHAR(3) | Y |  |  |

- **Primary key** `PK_PAY_VOUCHER_TMP` (PAY_START_DATE, PAY_END_DATE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO)

### PENDING_LOANS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **START_DATE** | DATE | Y |  |  |
| 3 | **END_DATE** | DATE | Y |  |  |
| 4 | **LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 5 | **REFUND_NO** | VARCHAR2(12) | Y |  |  |
| 6 | **LOAN_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **REFUND_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 8 | **LOAN_PENDING** | NUMBER(20,2) | Y |  |  |
| 9 | **LOAN_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 17 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 18 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 19 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### PF_FINAL_SETTLEMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 2 | **SR_NO** 🔑 | NUMBER(2) | N |  | Auto Increment |
| 3 | **TRANS_DATE** | DATE | Y |  |  |
| 4 | **TYPE** | VARCHAR2(2) | Y |  | FS -> Final Settlement, PW -> Permanent Widthdrawal |
| 5 | **RACK_RATE** | NUMBER(20,2) | Y |  |  |
| 6 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 7 | **VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 8 | **VOUCHER_NO** | CHAR(13) | Y |  |  |
| 9 | **CANCELLED_VOUCHER_TYPE** | VARCHAR2(5) | Y |  |  |
| 10 | **CANCELLED_VOUCHER_NO** | VARCHAR2(13) | Y |  |  |
| 11 | **STATUS_ID** | VARCHAR2(3) | N | '100' |  |
| 12 | **PF_TYPE** | VARCHAR2(2) | Y |  | PF, CP, GP |
| 13 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **TRN_DATE** | DATE | Y |  |  |
| 16 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 19 | **GROSS_PAYABLE** | NUMBER(20,2) | Y |  |  |
| 20 | **NO_OF_MONTHS** | NUMBER(2) | Y |  |  |
| 21 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 22 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 23 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 24 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PF_FINAL_SETTLEMENT` (MRNO, SR_NO)
- **Triggers**: `PF_FINAL_SETTLEMENT_DEL` (AFTER DELETE), `PF_FINAL_SETTLEMENT_INS` (BEFORE INSERT), `PF_FINAL_SETTLEMENT_UPD` (BEFORE UPDATE)

### PROCESS_INCREMENT_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PROCESS_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **INCREMENT_CODE** → `PAYROLL.DEF_INCREMENT_TYPE` | CHAR(3) | N |  |  |
| 3 | **INCREMENT_DATE** | DATE | N |  |  |
| 4 | **EFFECTIVE_DATE** | DATE | Y |  |  |
| 5 | **ADD_ARREARS** | CHAR(1) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **INCR_SLAB_ID** | VARCHAR2(12) | Y |  |  |
| 13 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 14 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 15 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 16 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PROCESS_INCREMENT_MASTER` (PROCESS_ID)
- **FK** `FK_PROCESS_INCREMENT_MASTER_1` (INCREMENT_CODE) → `PAYROLL.DEF_INCREMENT_TYPE` (INCREMENT_CODE) _DISABLED_
- **Triggers**: `PROCESS_INCREMENT_MASTER_DEL` (AFTER DELETE), `PROCESS_INCREMENT_MASTER_INS` (BEFORE INSERT), `PROCESS_INCREMENT_MASTER_UPD` (BEFORE UPDATE)

### PROCESS_MEMBERS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PROCESS_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **STAGE_NO** | NUMBER(2) | Y |  |  |
| 4 | **INCREMENT_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 5 | **LAST_INCREMENT_DATE** | DATE | Y |  |  |
| 6 | **PATIENT_TYPE_ID** | VARCHAR2(6) | Y |  |  |
| 7 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 8 | **GRADE_ID** | VARCHAR2(6) | Y |  |  |
| 9 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 10 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 12 | **JOINING_DATE** | DATE | Y |  |  |
| 13 | **SELECT_FLAG** | CHAR(1) | Y |  |  |
| 14 | **PROCESS_LOG** | VARCHAR2(1000) | Y |  |  |
| 15 | **STATUS_ID** | VARCHAR2(3) | Y |  |  |
| 16 | **POSTED_BY** | VARCHAR2(14) | Y |  |  |
| 17 | **POSTED_DATE** | DATE | Y |  |  |
| 18 | **VERIFIED** | CHAR(1) | Y | 'N' |  |
| 19 | **EFFECTIVE_DATE** | DATE | Y |  |  |
| 20 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 21 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 22 | **TRN_DATE** | DATE | Y |  |  |
| 23 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 24 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 25 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 26 | **INCR_SLAB_ID** | VARCHAR2(12) | Y |  |  |
| 27 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 28 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 29 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 30 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_PROCESS_MEMBERS` (PROCESS_ID, MRNO)
- **Triggers**: `PROCESS_MEMBERS_DEL` (AFTER DELETE), `PROCESS_MEMBERS_INS` (BEFORE INSERT), `PROCESS_MEMBERS_UPD` (BEFORE UPDATE)

### PROFIT_VOUCHER_TMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **YEAR_CODE** 🔑 | NUMBER(4) | N |  |  |
| 2 | **PAY_VOUCHER_TYPE** 🔑 | VARCHAR2(2) | N |  |  |
| 3 | **ORGANIZATION_ID** | VARCHAR2(3) | N |  |  |
| 4 | **LOCATION_ID** 🔑 | VARCHAR2(3) | N |  |  |
| 5 | **SERIAL_NO** 🔑 | NUMBER(2) | N |  |  |
| 6 | **DETAIL_SERIAL_NO** 🔑 | NUMBER | N |  |  |
| 7 | **PAY_VOUCHER_SETUP_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **PAY_VOUCHER_SETUP_SRNO** | NUMBER(2) | Y |  |  |
| 9 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 10 | **EMP_LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 11 | **LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 12 | **PRINCIPAL_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 13 | **NO_OF_MONTH** | NUMBER(2) | Y |  |  |
| 14 | **COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 15 | **LEDGER_TYPE_CODE_DR** | NUMBER(4) | Y |  |  |
| 16 | **SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |
| 17 | **COA_CODE_CR** | VARCHAR2(100) | Y |  |  |
| 18 | **LEDGER_TYPE_CODE_CR** | NUMBER(4) | Y |  |  |
| 19 | **SUB_LDGR_ITEM_CODE_CR** | VARCHAR2(18) | Y |  |  |
| 20 | **AMOUNT** | NUMBER(20,2) | Y |  |  |
| 21 | **REMARKS** | VARCHAR2(4000) | Y |  |  |
| 22 | **COA_STATUS** | CHAR(1) | Y |  |  |

- **Primary key** `PK_PROFIT_VOUCHER_TMP` (YEAR_CODE, PAY_VOUCHER_TYPE, LOCATION_ID, SERIAL_NO, DETAIL_SERIAL_NO)

### REP_LOAN_LEDGER

This is a temporary table to generate trial balances / ledgers of advances and loans

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  | Employee Code |
| 2 | **NAME** | VARCHAR2(183) | Y |  | Employee Name |
| 3 | **LOAN_CODE** | CHAR(3) | Y |  | Lon type |
| 4 | **SELECT_FLAG** | CHAR(1) | Y |  | To be used into Form Block (For selection un-selection of employees) |
| 5 | **OPENING_BALANCE** | NUMBER(20,2) | Y |  | Opening balance of FROM_DATE into Report parameter |
| 6 | **TOTAL_DEDUCTION** | NUMBER(20,2) | Y |  | Total deduction till TO_DATE into Report parameter |
| 7 | **CLOSING_BALANCE** | NUMBER(20,2) | Y |  | Opening balance  - Total deduction |
| 8 | **USER_ID** | VARCHAR2(14) | Y |  | User who is running the report |
| 9 | **TERMINAL** | VARCHAR2(30) | Y |  | Terminal from where report is running |
| 10 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### RPT_SALARY_TAX_LINE_ITEM

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **SR_NO** | NUMBER | N |  |  |
| 2 | **LINE_ITEM** | VARCHAR2(200) | N |  |  |
| 3 | **ROW_TYPE** | VARCHAR2(10) | N |  |  |
| 4 | **SOURCE** | VARCHAR2(50) | Y |  |  |
| 5 | **SUBTOTAL_OF** | VARCHAR2(200) | Y |  |  |
| 6 | **SIGN** | NUMBER | Y | 1 |  |
| 7 | **COMMENTS** | VARCHAR2(500) | Y |  |  |
| 8 | **AD_CODE** | VARCHAR2(50) | Y |  |  |
| 9 | **PAYMENT_SOURCE** | VARCHAR2(500) | Y |  |  |
| 10 | **ORDER_BY** | NUMBER | Y |  |  |
| 11 | **PRECESSED_CHECK** | CHAR(1) | Y |  |  |
| 12 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 13 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 14 | **TRN_DATE** | DATE | Y |  |  |
| 15 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 16 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 17 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |

- **Triggers**: `RPT_SALARY_TAX_LINE_ITEM_DEL` (AFTER DELETE), `RPT_SALARY_TAX_LINE_ITEM_INS` (BEFORE INSERT), `RPT_SALARY_TAX_LINE_ITEM_UPD` (BEFORE UPDATE)

### R_COST_TO_COMPANY_TEMP

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **START_DATE** 🔑 | DATE | N |  |  |
| 2 | **END_DATE** 🔑 | DATE | N |  |  |
| 3 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 4 | **CALENDER_YEAR** | NUMBER(4) | Y |  |  |
| 5 | **TAX_YEAR** | NUMBER(4) | N |  |  |
| 6 | **MONTH** | VARCHAR2(41) | Y |  |  |
| 7 | **NAME** | VARCHAR2(4000) | Y |  |  |
| 8 | **CNIC_NO** | VARCHAR2(4000) | Y |  |  |
| 9 | **DOB** | DATE | Y |  |  |
| 10 | **EMP_TYPE** | CHAR(1) | Y |  |  |
| 11 | **PATIENT_TYPE_ID** | VARCHAR2(6) | Y |  |  |
| 12 | **DEPARTMENT_ID** | VARCHAR2(7) | Y |  |  |
| 13 | **DESIGNATION_ID** | VARCHAR2(6) | Y |  |  |
| 14 | **MANAGER_MRNO** | VARCHAR2(14) | Y |  |  |
| 15 | **IBAN** | VARCHAR2(64) | Y |  |  |
| 16 | **DEPARTMENT_CODE** | CHAR(3) | N |  |  |
| 17 | **DEPARTMENT_DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 18 | **COST_CENTER** | CHAR(3) | N |  |  |
| 19 | **COST_CENTER_DESCRIPTION** | VARCHAR2(255) | Y |  |  |
| 20 | **DIVISION_CODE** | CHAR(3) | N |  |  |
| 21 | **DIVISION_DESCRIPTION** | VARCHAR2(255) | N |  |  |
| 22 | **LOCATION_CODE** | VARCHAR2(3) | N |  |  |
| 23 | **LOCATION_DESCRIPTION** | VARCHAR2(150) | Y |  |  |
| 24 | **CURRENCY** | VARCHAR2(60) | Y |  |  |
| 25 | **MONTH_DAYS** | NUMBER(2) | Y |  |  |
| 26 | **PREVIOUS_UNPAID_LEAVE_COUNT** | NUMBER(5) | Y |  |  |
| 27 | **CURRENT_UNPAID_LEAVE_COUNT** | NUMBER(2) | Y |  |  |
| 28 | **EMPLOYMENT_TYPE** | VARCHAR2(60) | N |  |  |
| 29 | **ACTIVE** | VARCHAR2(1) | N |  |  |
| 30 | **DATE_OF_JOINING** | DATE | Y |  |  |
| 31 | **CONTRACTUAL_END_DATE** | DATE | Y |  |  |
| 32 | **CONFIRMATION_DATE** | DATE | Y |  |  |
| 33 | **DATE_OF_LEAVING** | DATE | Y |  |  |
| 34 | **GRADE** | VARCHAR2(60) | Y |  |  |
| 35 | **DESIGNATION** | VARCHAR2(4000) | Y |  |  |
| 36 | **CURRENT_GROSS** | NUMBER(20,2) | Y |  |  |
| 37 | **SUPERVISOR_MRNO** | VARCHAR2(4000) | Y |  |  |
| 38 | **SUPERVISOR_DESIGNATION** | VARCHAR2(4000) | Y |  |  |
| 39 | **HOD** | VARCHAR2(14) | Y |  |  |
| 40 | **HOD_DESIGNATION** | VARCHAR2(4000) | Y |  |  |
| 41 | **BASIC_SALARY** | NUMBER | Y |  |  |
| 42 | **HOUSE_RENT** | NUMBER | Y |  |  |
| 43 | **UTILITIES** | NUMBER | Y |  |  |
| 44 | **GROSS_SALARY** | NUMBER | Y |  |  |
| 45 | **PI** | NUMBER | Y |  |  |
| 46 | **CONVEYANCE_ALLOWANCE** | NUMBER | Y |  |  |
| 47 | **OVERLOAD_PAYMENT** | NUMBER | Y |  |  |
| 48 | **TRANSPORT_ALLOWANCE_DOCTORS** | NUMBER | Y |  |  |
| 49 | **SPECIAL_ALLOWANCE** | NUMBER | Y |  |  |
| 50 | **ON_CALL_ALLOWANCE_DOCTORS** | NUMBER | Y |  |  |
| 51 | **TRANSPORT_ALLOWANCE_NURSES** | NUMBER | Y |  |  |
| 52 | **OTHER_ALLOWANCE** | NUMBER | Y |  |  |
| 53 | **SPECIAL_PAY** | NUMBER | Y |  |  |
| 54 | **MERIT_PAY** | NUMBER | Y |  |  |
| 55 | **DOCTORS** | NUMBER | Y |  |  |
| 56 | **OTHERS** | NUMBER | Y |  |  |
| 57 | **TOTAL_ALLOWANCE** | NUMBER | Y |  |  |
| 58 | **OVERTIME** | NUMBER(20) | Y |  |  |
| 59 | **SHIFT_ALLOWANCE_NIGHT** | NUMBER(20) | Y |  |  |
| 60 | **ARREARS** | NUMBER(20) | Y |  |  |
| 61 | **TOTAL** | NUMBER | Y |  |  |
| 62 | **LFA** | NUMBER | Y |  |  |
| 63 | **LSA** | NUMBER | Y |  |  |
| 64 | **TRAVEL** | NUMBER | Y |  |  |
| 65 | **MEDICAL** | NUMBER | Y |  |  |
| 66 | **VEHICLE_MAINTENANCE** | NUMBER | Y |  |  |
| 67 | **BENEFITS_TOTAL** | NUMBER | Y |  |  |
| 68 | **INCOME_TAX** | NUMBER | Y |  |  |
| 69 | **EOBI** | NUMBER | Y |  |  |
| 70 | **PROFESSIONAL_TAX** | NUMBER | Y |  |  |
| 71 | **PROVIDENT_FUND** | NUMBER | Y |  |  |
| 72 | **COLLEGIALITY_FUND** | NUMBER | Y |  |  |
| 73 | **PFUND_LOAN** | NUMBER | Y |  |  |
| 74 | **FOOD** | NUMBER | Y |  |  |
| 75 | **TRAVEL_ADVANCE** | NUMBER | Y |  |  |
| 76 | **SALARY_ADVANCE** | NUMBER | Y |  |  |
| 77 | **MEDICAL_BILLS** | NUMBER | Y |  |  |
| 78 | **TELEPHONE** | NUMBER | Y |  |  |
| 79 | **DONATION_SADQA** | NUMBER | Y |  |  |
| 80 | **ZAKAT** | NUMBER | Y |  |  |
| 81 | **CAR_LOAN** | NUMBER | Y |  |  |
| 82 | **CAFE_BILL** | NUMBER | Y |  |  |
| 83 | **LAUNDRY** | NUMBER | Y |  |  |
| 84 | **GIFT_SHOP** | NUMBER | Y |  |  |
| 85 | **INDEMNITY_PATIENT** | NUMBER | Y |  |  |
| 86 | **SCRAP** | NUMBER | Y |  |  |
| 87 | **STORES** | NUMBER | Y |  |  |
| 88 | **HOUSE_ACCOMMODATION** | NUMBER | Y |  |  |
| 89 | **KARACHI_PROJECT_DONATION** | NUMBER | Y |  |  |
| 90 | **OTHER_DEDUCTIONS** | NUMBER | Y |  |  |
| 91 | **TAX_TOTAL** | NUMBER | Y |  |  |
| 92 | **E_YEARLY_TAXABLE_AMOUNT** | NUMBER | Y |  |  |
| 93 | **PAID_COA_WITHIN_MONTH** | NUMBER | Y |  |  |
| 94 | **EXPECTED_YEARLY_TAX** | NUMBER(12,2) | Y |  |  |
| 95 | **EXPECTED_YEARLY_TBL** | NUMBER(12,2) | Y |  |  |
| 96 | **YEARLY_PAID_TAX** | NUMBER | Y |  |  |
| 97 | **REMAINING_TAX** | NUMBER | Y |  |  |
| 98 | **MONTH_REMAINING** | NUMBER(2) | Y |  |  |
| 99 | **ACTUAL_PROPOSED_TAX** | NUMBER(12,2) | Y |  |  |
| 100 | **PAID_PRACTICE_INCOME** | NUMBER | Y |  |  |
| 101 | **PAID_GROSS_PAY** | NUMBER | Y |  |  |
| 102 | **PAID_LFA_AMOUNT** | NUMBER | Y |  |  |
| 103 | **PAID_OTHER_ALLOWANCES** | NUMBER | Y |  |  |
| 104 | **PAID_ARREARS** | NUMBER | Y |  |  |
| 105 | **PAID_COA_BASED_EXPENSE** | NUMBER | Y |  |  |
| 106 | **PAID_EXPENSES** | NUMBER | Y |  |  |
| 107 | **PAID_NIGHTS** | NUMBER | Y |  |  |
| 108 | **PAID_OVERTIME** | NUMBER | Y |  |  |
| 109 | **DIRECT_PAID_EXPENSES** | NUMBER | Y |  |  |
| 110 | **EXPECTED_GROSS_PAY** | NUMBER | Y |  |  |
| 111 | **EXPECTED_OTHER_ALLOWANCES** | NUMBER | Y |  |  |
| 112 | **EXPECTED_PRACTICE_INCOME** | NUMBER | Y |  |  |
| 113 | **EXPECTED_TRANS_ALLOWANCES** | NUMBER | Y |  |  |
| 114 | **EXPECTED_LFA_AMOUNT** | NUMBER | Y |  |  |
| 115 | **EXPECTED_ARREARS** | NUMBER | Y |  |  |
| 116 | **EXPECTED_ANNUALLY_TAX** | NUMBER | Y |  |  |
| 117 | **OTHER_TAXABLE_AMOUNT** | NUMBER | Y |  |  |
| 118 | **TAXABLE_PF_AMOUNT** | NUMBER | Y |  |  |
| 119 | **CURRENT_MONTH_NIGHTS** | NUMBER | Y |  |  |
| 120 | **CURRENT_MONTH_OVERTIME** | NUMBER | Y |  |  |
| 121 | **TAX_PAID_IN_SALARY** | NUMBER | Y |  |  |
| 122 | **TAX_PAID_DIRECTLY** | NUMBER | Y |  |  |
| 123 | **TAX_ADJUSTMENTS** | NUMBER | Y |  |  |
| 124 | **CURRENCY_EXCHANGE_RATE** | NUMBER | Y |  |  |
| 125 | **LAST_MONTH_END_DATE** | DATE | Y |  |  |
| 126 | **UNPAID_LEAVE_AMOUNT** | NUMBER | Y |  |  |
| 127 | **UNDISTRIBUTED_TAX** | NUMBER | Y |  |  |
| 128 | **MONTHLY_SALARY** | NUMBER(20) | Y |  |  |
| 129 | **REIMBURSEMENT** | NUMBER(20) | Y |  |  |
| 130 | **PRACTICE_INCOME** | NUMBER(20) | Y |  |  |
| 131 | **NET_PAYABLE** | NUMBER(20) | Y |  |  |
| 132 | **NET_SALARY_BANK_CREDIT** | NUMBER(20) | Y |  |  |
| 133 | **DUTY_DAYS** | NUMBER(2) | Y |  |  |
| 134 | **DUTY_LOCATION** | VARCHAR2(60) | Y |  |  |
| 135 | **DEPARTMENT_SECTION** | VARCHAR2(60) | Y |  |  |
| 136 | **POSITION_ID** | VARCHAR2(6) | Y |  |  |
| 137 | **COA_CODE_DR** | VARCHAR2(100) | Y |  |  |
| 138 | **SUB_LDGR_ITEM_CODE_DR** | VARCHAR2(18) | Y |  |  |

- **Primary key** `PK_COST_TO_COMPANY` (START_DATE, END_DATE, MRNO)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP01` (CALENDER_YEAR)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP02` (EMP_TYPE)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP03` (PATIENT_TYPE_ID)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP04` (DEPARTMENT_ID)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP05` (DESIGNATION_ID)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP06` (LOCATION_CODE)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP07` (MONTH)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP08` (COST_CENTER)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP09` (MRNO)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP10` (EMPLOYMENT_TYPE)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP11` (END_DATE)
- **Index** `IDX_R_COST_TO_COMPANY_TEMP12` (TAX_YEAR)

### SALARY_ELEMENT

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FINAL_SETTLEMENT_ID** | VARCHAR2(9) | Y |  |  |
| 2 | **SRNO** | NUMBER | Y |  |  |
| 3 | **DESCRIPTION** | VARCHAR2(100) | Y |  |  |
| 4 | **AMOUNT** | NUMBER(10) | Y |  |  |


### SALARY_SLABS

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **FROM_RANGE** | NUMBER(6) | Y |  |  |
| 2 | **TO_RANGE** | NUMBER(6) | Y |  |  |
| 3 | **INCR_PERCENT** | NUMBER(5,2) | Y |  |  |
| 4 | **NO_OF_EMP** | NUMBER(4) | Y |  |  |
| 5 | **TOTAL_SALARY** | NUMBER(8) | Y |  |  |
| 6 | **TOT_INC** | NUMBER | Y |  |  |
| 7 | **INCR_AGE** | NUMBER | Y |  |  |
| 8 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 9 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 11 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **TRN_DATE** | DATE | Y |  |  |
| 14 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 15 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 16 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 17 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### TARGET_TABLE

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **AD_CODE** | CHAR(3) | Y |  |  |
| 3 | **AD_VALUE** | NUMBER | Y |  |  |
| 4 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 5 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 6 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 11 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 12 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 13 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |


### TAX_CALCULATION_LOG

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(30) | Y |  |  |
| 2 | **NEW_ANNUAL_TAXABLE_INCOME** | NUMBER(18,2) | Y |  |  |
| 3 | **NEW_ANNUAL_TAX** | NUMBER(18,2) | Y |  |  |
| 4 | **TAXABLE_GROSS** | NUMBER(18,2) | Y |  |  |
| 5 | **TAXABLE_PF** | NUMBER(18,2) | Y |  |  |
| 6 | **NEW_MONTH_TAXABLE_PF** | NUMBER(18,2) | Y |  |  |
| 7 | **TOT_INCOME_LAST_MON** | NUMBER(18,2) | Y |  |  |
| 8 | **TAX_TO_BE_PAID_TILL_MONTH** | NUMBER(18,2) | Y |  |  |
| 9 | **TAX_PAID_TILL_MONTH** | NUMBER(18,2) | Y |  |  |
| 10 | **MONTHLY_AMOUNT_ADJ** | NUMBER(18,2) | Y |  |  |
| 11 | **CURRENT_DEDUCTION** | NUMBER(18,2) | Y |  |  |
| 12 | **LOG_DATE** | DATE | Y | SYSDATE |  |

- **Index** `IDX_TAX_CALC_LOG_MRNO` (MRNO)

### TEMP_INCREMENT_MASTER

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PROCESS_ID** 🔑 | VARCHAR2(12) | N |  |  |
| 2 | **MRNO** 🔑 | VARCHAR2(14) | N |  |  |
| 3 | **INCREMENT_DATE** | DATE | N |  |  |
| 4 | **INCREMENT_CODE** | CHAR(3) | N |  |  |
| 5 | **EFFECTIVE_DATE** | DATE | Y |  |  |
| 6 | **INCR_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **INCR_PERCENT** | NUMBER(6,2) | Y |  |  |
| 8 | **SETUP_BASIC** | NUMBER(20,2) | Y |  |  |
| 9 | **SETUP_GROSS** | NUMBER(20,2) | Y |  |  |
| 10 | **PROPOSED_BASIC** | NUMBER(20,2) | Y |  |  |
| 11 | **PROPOSED_GROSS** | NUMBER(20,2) | Y |  |  |
| 12 | **REMARKS** | VARCHAR2(255) | Y |  |  |
| 13 | **ARREAR_PAID** | CHAR(1) | Y |  |  |
| 14 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 15 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 16 | **TRN_DATE** | DATE | Y |  |  |
| 17 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 18 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 19 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 20 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 21 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 22 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 23 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_TEMP_INCREMENT_MASTER` (PROCESS_ID, MRNO)
- **Referenced by**: `TEMP_INCREMENT_DETAIL`
- **Triggers**: `TEMP_INCREMENT_MASTER_DEL` (AFTER DELETE), `TEMP_INCREMENT_MASTER_INS` (BEFORE INSERT), `TEMP_INCREMENT_MASTER_UPD` (BEFORE UPDATE)

### TEMP_INCREMENT_DETAIL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **PROCESS_ID** 🔑 → `PAYROLL.TEMP_INCREMENT_MASTER` | VARCHAR2(12) | N |  |  |
| 2 | **MRNO** 🔑 → `PAYROLL.TEMP_INCREMENT_MASTER` | VARCHAR2(14) | N |  |  |
| 3 | **AD_CODE** 🔑 | CHAR(3) | N |  |  |
| 4 | **ENTRY_TYPE** | CHAR(1) | Y |  |  |
| 5 | **SETUP_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 6 | **PROPOSED_AMOUNT** | NUMBER(20,2) | Y |  |  |
| 7 | **PROPOSED_CHANGE** | CHAR(1) | Y |  |  |
| 8 | **CALCULATION_TYPE** | VARCHAR2(2) | Y |  |  |
| 9 | **CALC_PERCENT** | NUMBER(5,2) | Y |  |  |
| 10 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 11 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 12 | **TRN_DATE** | DATE | Y |  |  |
| 13 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 14 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 15 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 16 | **PERCENTAGE_SETUP_ID** | VARCHAR2(3) | Y |  |  |
| 17 | **ORG_ID** | VARCHAR2(3) | Y |  | This column contains ORG_ID where record in created in table first time (Multi-Location Information) |
| 18 | **ZON_ID** | VARCHAR2(3) | Y |  | This column contains ZON_ID where record in created in table first time (Multi-Location Information) |
| 19 | **LOC_ID** | VARCHAR2(3) | Y |  | This column contains LOC_ID where record in created in table first time (Multi-Location Information) |
| 20 | **WS_SYNC_DATE** | DATE | Y |  | This column contains WS_SYNC_DATE where record in created in table first time (Multi-Location Information) |

- **Primary key** `PK_TEMP_INCREMENT_DETAIL` (PROCESS_ID, MRNO, AD_CODE)
- **FK** `FK_TEMP_INCREMENT_DETAIL_2` (PROCESS_ID, MRNO) → `PAYROLL.TEMP_INCREMENT_MASTER` (PROCESS_ID, MRNO) _DISABLED_
- **Triggers**: `TEMP_INCREMENT_DETAIL_DEL` (AFTER DELETE), `TEMP_INCREMENT_DETAIL_INS` (BEFORE INSERT), `TEMP_INCREMENT_DETAIL_UPD` (BEFORE UPDATE)

### TEMP_INDIVIDUAL_ITAX

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **YEAR_CODE** | CHAR(4) | Y |  |  |
| 3 | **SALARY_END_DATE** | DATE | Y |  |  |
| 4 | **GROSS** | NUMBER(20,2) | Y |  |  |
| 5 | **OTHER_ALLOW** | NUMBER(20,2) | Y |  |  |
| 6 | **TAX_PAID** | NUMBER(20,2) | Y |  |  |
| 7 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 8 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 9 | **TRN_DATE** | DATE | Y |  |  |
| 10 | **PI_TAX_PAID** | NUMBER(20,2) | Y |  |  |
| 11 | **PRACTICE_INCOME** | NUMBER(20,2) | Y |  |  |


### TEMP_ITAX

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **FROM_DATE** | DATE | Y |  |  |
| 3 | **TO_DATE** | DATE | Y |  |  |
| 4 | **EMP_NAME** | VARCHAR2(255) | Y |  |  |
| 5 | **DESIGNATION** | VARCHAR2(255) | Y |  |  |
| 6 | **ADDRESS** | VARCHAR2(1000) | Y |  |  |
| 7 | **CNIC** | VARCHAR2(20) | Y |  |  |
| 8 | **NTN** | VARCHAR2(20) | Y |  |  |
| 9 | **GENDER** | VARCHAR2(20) | Y |  |  |
| 10 | **DUTY_CITY** | VARCHAR2(255) | Y |  |  |
| 11 | **SALARY_MONTH** | NUMBER(2) | Y |  |  |
| 12 | **GROSS_PAYABLE** | NUMBER(12) | Y |  |  |
| 13 | **LFA** | NUMBER(12) | Y |  |  |
| 14 | **PI** | NUMBER(12) | Y |  |  |
| 15 | **TAXABLE_PF** | NUMBER(12) | Y |  |  |
| 16 | **TAXABLE_AMOUNT** | NUMBER(12) | Y |  |  |
| 17 | **ANNUAL_TAX** | NUMBER(12) | Y |  |  |
| 18 | **ITAX** | NUMBER(12) | Y |  |  |
| 19 | **PI_TAX** | NUMBER(12) | Y |  |  |
| 20 | **TOTAL_PAID_TAX** | NUMBER(12) | Y |  |  |
| 21 | **TAX_CREDIT** | NUMBER(12) | Y |  |  |
| 22 | **TAX_WITHHELD** | NUMBER(12) | Y |  |  |
| 23 | **LFA_PAID** | NUMBER(12) | Y |  |  |
| 24 | **USERID** | VARCHAR2(30) | Y |  |  |
| 25 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 26 | **EMP_TYPE** | CHAR(1) | Y |  |  |
| 27 | **SALARY_EXP** | NUMBER(12) | Y |  | TAXABLE EXPENSES |
| 28 | **SURCHARGE_TAX** | NUMBER(12) | Y |  |  |
| 29 | **TAX_SLAB** | NUMBER(5,2) | Y |  |  |
| 30 | **MONTHLY_TAXABLE_PF** | NUMBER(12) | Y |  |  |
| 31 | **NON_SALARY_EXP** | NUMBER(12) | Y |  | NON TAXABLE EXPENSES |
| 32 | **TAX_DIRECT_PAID_EXP** | NUMBER(12) | Y |  |  |
| 33 | **SALARY_FS** | NUMBER(12) | Y |  |  |
| 34 | **LEAVE_ENCASHMENT** | NUMBER(12) | Y |  |  |
| 35 | **CASH_AWARDS** | NUMBER(12) | Y |  |  |
| 36 | **INCENTIVES** | NUMBER(12) | Y |  |  |


### TEMP_SALARY_RECONCILE_DATA

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **IN_DEPARTMENT** | VARCHAR2(400) | Y |  |  |
| 3 | **OUT_DEPARTMENT** | VARCHAR2(400) | Y |  |  |
| 4 | **START_DATE** | DATE | Y |  |  |
| 5 | **CURRENT_SALARY** | NUMBER | Y |  |  |
| 6 | **PREVIOUS_SALARY** | NUMBER | Y |  |  |
| 7 | **LOCATION_ID** | VARCHAR2(3) | Y |  |  |
| 8 | **ORGANIZATION_ID** | VARCHAR2(3) | Y |  |  |
| 9 | **EVENT** | VARCHAR2(400) | Y |  |  |


### TMP_LOAN_SUMMARY

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **MRNO** | VARCHAR2(14) | Y |  |  |
| 2 | **NAME** | VARCHAR2(255) | Y |  |  |
| 3 | **DEPARTMENT** | VARCHAR2(255) | Y |  |  |
| 4 | **DESIGNATION** | VARCHAR2(255) | Y |  |  |
| 5 | **SALARY** | NUMBER(12,2) | Y |  |  |
| 6 | **LOAN_TYPE** | VARCHAR2(255) | Y |  |  |
| 7 | **OPENING_BALANCE** | NUMBER(12,2) | Y |  |  |
| 8 | **RECEIVED_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 9 | **RETURNED_AMOUNT** | NUMBER(12,2) | Y |  |  |
| 10 | **CLOSING_BALANCE** | NUMBER(12,2) | Y |  |  |
| 11 | **USERID** | VARCHAR2(30) | Y |  |  |
| 12 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 13 | **LOAN_CODE** | CHAR(3) | Y |  |  |
| 14 | **TRANS_DATE** | DATE | Y |  |  |
| 15 | **LOAN_NO** | VARCHAR2(12) | Y |  |  |
| 16 | **STOP_AUTO_DEDUCTION** | CHAR(1) | Y |  |  |
| 17 | **NO_OF_INSTALLMENTS** | NUMBER(12,2) | Y |  |  |
| 18 | **MONTHLY_INSTALLMENT** | NUMBER(12,2) | Y |  |  |
| 19 | **STOP_AUTO_DEDUCTION_TILL** | DATE | Y |  |  |


### TRAVEL_ADVANCE_APPROVAL

| # | Column | Type | Null | Default | Comment |
|---|---|---|---|---|---|
| 1 | **REQUEST_NO** 🔑 | NUMBER | N |  |  |
| 2 | **APPROVAL_STATUS** | VARCHAR2(1) | Y |  | P = Pending, A = Approved, R = Rejected |
| 3 | **APPROVAL_DATE** | DATE | Y |  |  |
| 4 | **APPROVED_BY** | VARCHAR2(14) | Y |  |  |
| 5 | **REMARKS** | VARCHAR2(2000) | Y |  |  |
| 6 | **USER_ID** | VARCHAR2(30) | Y |  |  |
| 7 | **TERMINAL** | VARCHAR2(30) | Y |  |  |
| 8 | **TRN_DATE** | DATE | Y |  |  |
| 9 | **ORIGINAL_USER_ID** | VARCHAR2(30) | Y |  |  |
| 10 | **ORIGINAL_TERMINAL** | VARCHAR2(30) | Y |  |  |
| 11 | **ORIGINAL_TRN_DATE** | DATE | Y |  |  |
| 12 | **MRNO** | VARCHAR2(14) | Y |  |  |

- **Primary key** `PK_TRAVEL_ADVANCE_APPROVAL` (REQUEST_NO)
- **Triggers**: `TRAVEL_ADVANCE_APPROVAL_DEL` (AFTER DELETE), `TRAVEL_ADVANCE_APPROVAL_INS` (BEFORE INSERT), `TRAVEL_ADVANCE_APPROVAL_PQ` (BEFORE INSERT OR UPDATE), `TRAVEL_ADVANCE_APPROVAL_UPD` (BEFORE UPDATE)

## Views

### PAD_DR_FEE

Sources: `PAY_ALLOWANCE_DEDUCTION`

```sql
select mrno, start_date, end_date, ad_code, pad.actual_amount, pad.calc_amount, pad.calc_amount_guarantee, pad.pending_amount
from payroll.pay_allowance_deduction pad
where pad.ad_code in ('007','043')
```

### PAYMASTER_VIEW

Sources: `PAY_MASTER`

```sql
select MRNo, P_Fund_Amount, P_Fund_Loan, posted
from payroll.pay_master
```

### PM_DR_FEE

Sources: `PAY_MASTER`

```sql
select mrno, start_date, end_date, practice_income, practice_income_tax
from payroll.pay_master
```

### VU_PAY_STATUS

Sources: `PAY_STATUS`

```sql
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
   AND p.date_to = m.pay_end_date
```

### V_PAYMASTER

Sources: `PAY_MASTER`

```sql
SELECT MRNO, P_FUND_LOAN FROM PAYROLL.PAY_MASTER
```

## Sequences

| Sequence | Options |
|---|---|
| LOAN_NO | minvalue 0 maxvalue 9999999999999999999999999999 start with 1 increment by 1 nocache |

## Packages

### PKG_AD_DETAIL

- `procedure INSERT_AD_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ROW IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL%ROWTYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_CURR_AD_CALC_PERCENT(P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_SETUP.AD_CODE%TYPE, P_TRANS_DATE IN DATE) RETURN PAYROLL.ALLOWANCE_DEDUCTION_SETUP.CALC_PERCENT%TYPE`
- `procedure INSERT_CURRENT_MONTH_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_AMOUNT IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE, P_REMARKS IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE, P_NO_OF_DAYS IN PAYROLL.AL...`
- `procedure DELETE_CURRENT_MONTH_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_PROCESS_ID IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.O...`
- `procedure OVERRIGHT_CURRENT_MONTH_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_AMOUNT IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE, P_REMARKS IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE, P_NO_OF_DAYS IN PAYROLL.AL...`

### PKG_AD_UTILITIES

This package was created for Cash Refund

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure RUN_PAYMENT_PROCESSES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure PROCESS_CLAIMED_EXP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE, P_END_DATE IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OU...`
- `procedure PROCESS_LFA_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure PROCESS_LFA_PAYMENT_UNDO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN DATE, P_MON_END_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure INSERT_EXPENSE_ALLOWANCES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure PROCESS_PAY_HOLD_ORDER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT...`
- `procedure PROCESS_LOAN_INSTALLMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%T...`
- `procedure PROCESS_LSA_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE...`
- `procedure PROCESS_LSA_PAYMENT_UNDO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN DATE, P_MON_END_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`

### PKG_ARREAR_DETAIL

- `procedure INSERT_ARREAR_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ROW IN PAYROLL.ARREAR_DETAIL%ROWTYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure INSERT_CURRENT_MONTH_ARREAR(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ARREAR_CODE IN PAYROLL.ARREAR_DETAIL.ARREAR_CODE%TYPE, P_AD_CODE IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.ARREAR_DETAIL.MRNO%TYPE, P_ARREAR_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE, P_ARREAR_END_DATE IN PAYROLL.ARREAR_DETAIL.ARREA...`

### PKG_AWARD_PAYMENT

This package was created for Employee Expense entry/adjustments

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_PAID_AMOUNT(P_AWARD_ID IN PAYROLL.EMP_AWARD_PAYMENT.AWARD_ID%TYPE) RETURN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE`
- `procedure GEN_PAYMENT_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAYMENT_ID OUT PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_...`
- `procedure GEN_AWARD_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_AWARD_ID OUT PAYROLL.EMP_AWARDS.AWARD_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VA...`
- `procedure INS_LFA_PAYMENT_SAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_AWARDS.MRNO%TYPE, P_DUE_DATE IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE, P_AMOUNT IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE, P_MON_START_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYP...`
- `procedure INS_AWARD_AND_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_AWARDS.MRNO%TYPE, P_DUE_DATE IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE, P_EXPENSE_CODE IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE, P_PAYMENT_BASE IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE, P_PAYMENT_RATE IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE, P_AMOUNT I...`
- `procedure INSERT_EMP_AWARD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_AWARDS.MRNO%TYPE, P_DUE_DATE IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE, P_EXPENSE_CODE IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE, P_PAYMENT_BASE IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE, P_PAYMENT_RATE IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE, P_AMOUNT I...`
- `procedure INSERT_EMP_AWARD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_AWARDS.MRNO%TYPE, P_DUE_DATE IN PAYROLL.EMP_AWARDS.DUE_DATE%TYPE, P_EXPENSE_CODE IN PAYROLL.EMP_AWARDS.EXPENSE_CODE%TYPE, P_PAYMENT_BASE IN PAYROLL.EMP_AWARDS.PAYMENT_BASE%TYPE, P_PAYMENT_RATE IN PAYROLL.EMP_AWARDS.PAYMENT_RATE%TYPE, P_AMOUNT I...`
- `procedure INSERT_AWARD_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_AWARD_ID IN PAYROLL.EMP_AWARDS.AWARD_ID%TYPE, P_AMOUNT IN PAYROLL.EMP_AWARD_PAYMENT.AMOUNT%TYPE, P_AD_CODE IN PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE, P_MON_START_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON...`
- `procedure INSERT_LSA_AWARDS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CANCEL_AWARD_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.Emp_Awards.MRNO%TYPE, P_AD_CODE IN PAYROLL.EMP_AWARD_PAYMENT.AD_CODE%TYPE, P_MON_START_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON_START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.EMP_AWARD_PAYMENT.MON_END_DATE%TYPE, P_DOCUMENT_NO IN PAYROLL.EMP_AWARD_PAYMENT....`
- `procedure INSERT_LFA_ADJUSTMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_BANK

1. This Package will be used for PAYROLL Bank & Branches

- `function GET_BANK_NAME(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE) RETURN VARCHAR2`
- `function GET_PARENT_ADDRESS(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE, P_BRANCH_ID IN DEFINITIONS.BANK_BRANCH.BRANCH_ID%TYPE) RETURN VARCHAR2`
- `function GET_BRANCH_ADDRESS(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE, P_BRANCH_ID IN DEFINITIONS.BANK_BRANCH.BRANCH_ID%TYPE) RETURN VARCHAR2`
- `function GET_BANK_ACCOUNT_NO(P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE) RETURN VARCHAR2`

### PKG_CARD_MANAGEMENT

This package is created for common function related the card management

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_CONTACT_NUMBER(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE) RETURN VARCHAR2`
- `function GET_CONTACT_NUMBER(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_DATE PAYROLL.CM_CONNECTION_TRANSACTIONS.TO_DATE%TYPE) RETURN VARCHAR2`
- `function GET_CONTACT_NUMBER_NETWORK(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE) RETURN VARCHAR2`
- `function GET_PAYMENT_METHOD_DESC(P_METHOD IN PAYROLL.CM_BILL_DETAIL.PAYMENT_METHOD%TYPE) RETURN VARCHAR2`
- `function IS_CONNECTION_ISSUED(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE) RETURN VARCHAR2`
- `procedure GEN_REQUEST_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REQUEST_ID OUT VARCHAR2, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure ACTIVATE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure INACTIVATE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure VACANT_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure ISSUE_CONNECTION(P_CONNECTION_ID IN PAYROLL.CM_DEF_CONNECTION.CONNECTION_ID%TYPE, p_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure CONNECTION_STATUS(P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure SIGN_REQUEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure APPROVE_REQUEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_CONNECTION_ID IN PAYROLL.CM_CONNECTION_REQUEST.CONNECTION_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure CANCEL_REQUEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure POPULATE_MONTHLY_BILLS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure DELETE_BILL_DETAILS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure PAYMENT_METHOD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_DETAIL.ADMIN_GROUP_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_DETAIL.MONTH_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_BILL_DETAIL.REQUEST_ID%TYPE, P_PAYMENT_METHOD IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE I...`
- `procedure POST_MONTHLY_PAYMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure FINALIZE_MONTHLY_PAYMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure POST_EXCESS_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ADMIN_GROUP_ID IN PAYROLL.CM_BILL_MASTER.ADMIN_GROUP_ID%TYPE, P_MONTH_ID IN PAYROLL.CM_BILL_MASTER.MONTH_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure TRANSFER_CONNECTIONS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CONNECTION_ID IN PAYROLL.CM_CONNECTION_TRANSACTIONS.CONNECTION_ID%TYPE, P_TRANSACTION_ID IN PAYROLL.CM_CONNECTION_TRANSACTIONS.TRANS_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TE...`
- `procedure SEND_PAYMENT_SMS(P_SMS_NUMBER IN VARCHAR2, P_EMPLOYEE_NAME IN VARCHAR2, P_MONTH IN VARCHAR2, P_BILL_AMOUNT IN NUMBER, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function IS_DATA_SIM(P_CONTACT_NUMBER IN PAYROLL.CM_DEF_CONNECTION.CONTACT_NUMBER%TYPE) RETURN VARCHAR2`
- `procedure TRANSFER_NUMBER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REQUEST_ID IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_DEPARTMENT_ID IN PAYROLL.CM_CONNECTION_REQUEST.DEPARTMENT_ID%TYPE, P_REQUEST_TYPE IN PAYROLL.CM_CONNECTION_REQUEST.REQUEST_TYPE%TYPE, P_FROM_DATE IN PAYROLL.CM_CONNECTION_REQUEST.FROM_DATE%TYPE, P_MRNO...`
- `procedure REQUEST_CONNECTION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ROW IN PAYROLL.CM_CONNECTION_REQUEST%ROWTYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_REQUEST_ID OUT PAYROLL.CM_CONNECTION_REQUEST.REQUEST_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`

### PKG_COMMON

- `function GET_DEFSETUP_LOC_DESC(P_LOCATION_ID IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2) RETURN VARCHAR2`
- `function GET_CONSTANT_VALUE(P_LOCATION_ID IN VARCHAR2, P_DATE IN DATE DEFAULT SYSDATE, P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2) RETURN VARCHAR2`
- `function GET_EXPENSE_DESC(P_EXPENSE_CODE IN VARCHAR2, P_LEVEL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2) RETURN VARCHAR2`
- `function GET_PF_AMOUNT(P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `function GET_LFA_AMOUNT(P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `function GET_MEDICAL_EXPENSE(P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `function GET_OTHERS_EXPENSE(P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `function GET_CONSTANT_VALUE(P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_DATE IN DATE, P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_DEFAULT_VAL IN PAYROLL.DEF_SETUP.VALUE%TYPE) RETURN PAYROLL.DEF_SETUP.VALUE%TYPE`
- `function GET_CONSTANT_NUM_VALUE(P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_DATE IN DATE, P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_DEFAULT_VAL IN NUMBER) RETURN NUMBER`

### PKG_DATALOADER

This package is created for Data Loader Scheme

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure IMP_ALL_DED_SHEET(P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_AMOUNT IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE, P_REMARKS IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.REMARKS%TYPE, P_NO_OF_DAYS IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.NO_OF_DAYS%TYPE DEFAULT 0, P_PROCESS_ID IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.PROCESS_ID%TYPE, P_ALERT_TE...`
- `procedure IMP_ARREARS_SHEET(P_ARREAR_CODE IN PAYROLL.ARREAR_DETAIL.ARREAR_CODE%TYPE, P_MRNO IN PAYROLL.ARREAR_DETAIL.MRNO%TYPE, P_AMOUNT IN PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE, P_ARREAR_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE, P_ARREAR_END_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE, P_REMARKS IN PAYROLL.ARREAR_DETAIL.REMARKS%TYPE, P_DAYS_HOURS IN PAYROLL.ARREAR_DETAIL.DAYS_HOURS%TYPE DEFAULT 0, P...`
- `procedure IMP_EXPENSE(P_EXPENSE_LIST_ID IN VARCHAR2, P_MRNO IN VARCHAR2, P_AMOUNT IN VARCHAR2, P_TAX_DEDUCTED IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_DEF_ALLOWANCE_DEDUCTION

- `function F_SELECT(P_AD_CODE IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE, P_ROW OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE, P_IGNORE_NO_DATA IN CHAR DEFAULT NULL, P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EV...`
- `function F_LOCK(P_AD_CODE IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ROWID OUT ROWID, P_ERROR OUT ...`
- `function F_INSERT(P_ROW IN OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE, P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL, P_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ERROR OUT VARCHAR2) RETURN BOOLEAN`
- `function F_UPDATE(P_AD_CODE IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE, P_ROW IN OUT PAYROLL.DEF_ALLOWANCE_DEDUCTION%ROWTYPE, P_UPDATE_NULL IN CHAR DEFAULT NULL, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2...`
- `function F_DELETE(P_AD_CODE IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.AD_CODE%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_ALLOWANCE_DEDUCTION.LOCATION_ID%TYPE, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ERROR OUT VARCHAR2) RETURN BO...`

### PKG_DEF_SETUP

- `function F_SELECT(P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_ROW OUT PAYROLL.DEF_SETUP%ROWTYPE, P_IGNORE_NO_DATA IN CHAR DEFAULT NULL, P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ERROR OUT VARCHAR2) RETURN BO...`
- `function F_LOCK(P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ROWID OUT ROWID, P_ERROR OUT VARCHAR2) RETURN BOOLEAN`
- `function F_INSERT(P_ROW IN OUT PAYROLL.DEF_SETUP%ROWTYPE, P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL, P_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ERROR OUT VARCHAR2) RETURN BOOLEAN`
- `function F_UPDATE(P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_ROW IN OUT PAYROLL.DEF_SETUP%ROWTYPE, P_UPDATE_NULL IN CHAR DEFAULT NULL, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN...`
- `function F_DELETE(P_CONSTANT_ID IN PAYROLL.DEF_SETUP.CONSTANT_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_SETUP.LOCATION_ID%TYPE, P_ORGANIZATION_ID IN PAYROLL.DEF_SETUP.ORGANIZATION_ID%TYPE, P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N', P_CALLING_LOCATION_ID IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2, P_ERROR OUT VARCHAR2) RETURN BOOLEAN`

### PKG_EMP_EXPENSE

This package was created for Employee Expense entry/adjustments

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_EXPENSE_AD_CODE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_EXPENSE_CODE IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE) RETURN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE`
- `function GET_UNCLAIMED_EXPENSES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.EMP_EXPENSE.START_DATE%TYPE, P_END_DATE IN PAYROLL.EMP_EXPENSE.END_DATE%TYPE) RETURN PAYROLL.PKG_EMP_EXPENSE.ALL_DED_DATA_TAB PIPELINED`
- `function GET_ACC_TYPE_EXPENSE(P_YEAR_CODE PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_MRNO PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_TYPE VARCHAR2) RETURN NUMBER`
- `function GET_ACC_TYPE_EXPENSE(P_FROM_DATE PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE, P_MRNO PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_TYPE VARCHAR2) RETURN NUMBER`
- `procedure GEN_EXPENSE_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_EXPENSE_NO OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP ...`
- `procedure INSERT_EMP_EXPENSE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST_DTL.EXPENSE_LIST_ID%TYPE, P_MRNO IN PAYROLL.EMP_EXPENSE_LIST_DTL.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_EMP_FINANCIAL

This Package will be used for the following purpose In this package, all the procedures/functions related to invoice data copy

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_EMPLOYEE_NTN(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN VARCHAR2`
- `function GET_EMPLOYEE_TAX_SETUP(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION.CURRENT_AMOUNT%TYPE`
- `function GET_BASIC_DEFAULT_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_BASIC_LOCAL_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_GROSS_DEFAULT_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_EXT_GROSS_DEF_CURR(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_EXT_GROSS_DEF_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_GROSS_LOCAL_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function GET_COST_CENTRE_ID(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN PAYROLL.DEF_EMP_FINANCIAL.COST_CENTRE_ID%TYPE`
- `function GET_ACTUAL_GROSS(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN NUMBER`
- `function IS_DAILY_WAGER(P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE) RETURN BOOLEAN`
- `function GET_EXCL_LFA_INTAX(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN PAYROLL.DEF_EMP_FINANCIAL.EXCL_LFA_INTAX%TYPE`
- `function GET_AD_DEFAULT_CURRENCY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_AD_CODE IN PAYROLL.Def_Ad_Constant.AD_CODE%TYPE, P_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function GET_EMPLOYEE_TYPE(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN VARCHAR2`

### PKG_EXPENSE_CLAIM

This package was created for Cash Refund

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure PROCESS_EMP_EXPENSE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure INSERT_EMP_EXPENSE(P_BLOCK_DATA IN OUT EMP_EXPENSE_TAB, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure CALCULATE_SLAB_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLIAM_NO IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_DEFAULT_SLAB_ID(P_EXPENSE_TYPE_ID IN PAYROLL.DEF_EXPENSE_DETAIL_SLAB.EXPENSE_TYPE_ID%TYPE) RETURN PAYROLL.DEF_EXPENSE_DETAIL_SLAB.SLAB_ID%TYPE`
- `function GET_DEPT_HOD_MRNO(P_MRNO IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `function GET_EMP_MNGR_MRNO(P_MRNO IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `function GET_USER_RUNTIME(P_EVENT_ID IN DEFINITIONS.EVENT.EVENT_ID%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `procedure GEN_COUNTER_EXPENSE_CLAIM(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO OUT PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure GEN_EXPENSE_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_EXPENSE_NO OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP ...`
- `function GET_EVENT_DESC(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE`
- `function GET_EVENT_LABEL(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.LABEL_DESC%TYPE`
- `function GET_EVENT_COLOR(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.COLOR_CODE%TYPE`
- `function GET_EVENT_DESC(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_WFE_NO IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE) RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE`
- `function GET_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_WFE_NO IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE) RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE`
- `function GET_CURRENT_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE) RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE`
- `function GEN_WFE_NO(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE) RETURN PAYROLL.EXPENSE_CLAIM_WORKFLOW.WFE_NO%TYPE`
- `procedure GET_EXPENSE_WORKFLOW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_EXPENSE_CODE IN PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE, P_COST_CENTRE_ID IN PAYROLL.DEF_EMP_FINANCIAL.COST_CENTRE_ID%TYPE DEFAULT NULL, P_WORKFLOW_REC OUT RADIATION.PKG_WORKFLOW.T_WORKFLOW_REC, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure INITIALIZE_WORKFLOW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure POST_WORKFLOW_EVENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_WORKFLOW_REMARKS IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.REMARKS%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALE...`
- `procedure PERFORM_EVENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure PROCESS_SMS_ALERT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_NEXT_EVENT_ID IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.EVENT_ID%TYPE, P_EVENT IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure POPULATE_QUEUE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_WFE_NO IN PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q.WFE_NO%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT O...`
- `function GET_NO_OF_DOCUMENTS(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE) RETURN NUMBER`
- `function CURRENT_EVENT_ID(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE) RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE`
- `function GET_HOD_CC(P_COST_CENTRE IN MMS.COST_CENTRE_HEAD.SUB_LDGR_ITEM_CODE%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `function GET_NEXT_EVENT_ID(P_SCHEMA_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE, P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE, P_WORK_FLOW_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE`
- `procedure EXPENSE_CLAIM_APPROVAL_Q(P_MRNO IN VARCHAR2, P_ACTING_FOR IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_PROCESS_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_EVENT IN VARCHAR2, P_ASSIGNMENT_ID IN NUMBER)`
- `function GET_IN_QUEUE_USERS(P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE) RETURN VARCHAR2`
- `function QUERY_ALL_REC_GROUP(P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN NUMBER`
- `procedure GET_SMS_TEXT(P_SMS_ALERT_ID IN HIS.SMS_ALERT_SETUP.DESCRIPTION%TYPE, P_SMS_TEXT OUT HIS.SMS_ALERT_SETUP.SMS_TEXT%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure LINK_POSTED_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OLD_VOUCHER_TYPE IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_TYPE%TYPE, P_OLD_VOUCHER_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_NO%TYPE, P_NEW_VOUCHER_TYPE IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_TYPE%TYPE, P_NEW_VOUCHER_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.VOUCHER_NO%...`

### PKG_INCREMENT

This package was created for Cash Refund

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure PROCESS_INCREMENT_PROPOSAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN HRD.INC_PROP_DETAIL.YEAR_CODE%TYPE, P_PROPOSAL_NO IN HRD.INC_PROP_DETAIL.PROPOSAL_NO%TYPE, P_SERIAL_NO IN HRD.INC_PROP_DETAIL.SERIAL_NO%TYPE, P_MRNO IN HRD.INC_PROP_DETAIL.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE...`
- `function GET_ADD_GROSS_FOR_INC(P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN NUMBER`
- `procedure PROCESS_EMP_INCREMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_INCREMENT_CODE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_CODE%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE, P_INC_...`
- `procedure EMPLOYEE_GRADE_REVISION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENTED_GROSS IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGI...`
- `procedure EMPLOYEE_GRADE_REVERT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYP...`
- `procedure PROCESS_INCREMENT_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYP...`
- `procedure REVERT_INCREMENT_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYP...`
- `function CALC_INCR_ARREAR_AMOUNT(P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE, P_INCR_AMOUNT IN PAYROLL.EMP_INCREMENT_MASTER.INCR_AMOUNT%TYPE) RETURN NUMBER`
- `procedure PROCESS_PF_REVESION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_CURRENT_GROSS IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE, P_ARREAR_AMOUNT IN PAYROLL.EMP_INCREMENT_MASTER.CURRENT_GROSS%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE, P_OBJECT_C...`
- `procedure REVERT_PF_REVESION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGIST...`
- `procedure GET_INCREMENT_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_INC_DETAIL OUT T_EMP_INC_DETAIL, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure INSERT_INCREMENT_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_A...`
- `procedure SYNC_EMPLOYEE_FINANCIAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure SYNC_EMPLOYEE_FINANCIAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE, P_NEW_JOINER IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure VALIDATE_INCREMENT_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTER.EFFECTIVE_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_BASIC_PERCENTAGE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE`
- `function GET_PF_PERCENTAGE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE`
- `procedure REVERT_EMP_INCREMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYP...`
- `procedure INSERT_SETUP_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_AD_CODE PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_AMOUNT IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE, P_FROM_DATE IN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.FROM_DATE%TYPE, P_TO_DATE IN PAYROL...`
- `procedure INS_ALLOWANCE_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_AD_CODE IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE, P_AD_AMOUNT IN PAYROLL.ARREAR_DETAIL.AMOUNT%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_EFFECTIVE_DATE IN PAYROLL.EMP_INCREMENT_MASTE...`
- `function GET_MIN_WAGE_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function GET_INFLATION_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function GET_MERIT_AMOUNT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`

### PKG_ITAX

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `function YEARLY_TAXABLE_PF(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE NUMBER, P_MRNO VARCHAR2) RETURN NUMBER`
- `function YEARLY_TAXABLE_PF_V3(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LAST_PAY_EDATE IN DATE, P_CURR_MON_PFUND_AMT IN NUMBER, P_SEPRATE_CURR_MON_AMT IN VARCHAR2, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2) RETURN NUMBER`
- `function GET_YEARLY_PF_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LAST_PAY_EDATE IN DATE, P_CURR_MON_PF_AMOUNT IN NUMBER, P_SEPRATE_CURR_MON_AMT IN VARCHAR2, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2) RETURN NUMBER`
- `function CALC_MONTHLY_PF(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LAST_PAY_EDATE IN DATE, P_CURR_MON_PF_AMOUNT IN NUMBER, P_SEPRATE_CURR_MON_AMT IN VARCHAR2, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2) RETURN NUMBER`
- `function YEARLY_TAXABLE_PF_TEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE NUMBER, P_MRNO VARCHAR2) RETURN NUMBER`
- `function F_GET_EMP_OTHER_TAXABLE_AMOUNT(P_MRNO IN VARCHAR2, P_YEAR IN VARCHAR2, P_TAXABLE_AMOUNT_TYPE_ID IN VARCHAR2) RETURN NUMBER`
- `procedure CALC_YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN OUT NUMBER, P_INCOME_DTL OUT T_ITAX_DTL_TAB, P_UP_LEAVES_AMOUNT O...`
- `procedure CALC_YEARLY_TAXABLE_PAY_TEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN OUT NUMBER, P_INCOME_DTL OUT T_ITAX_DTL_TAB, P_UP_LEAVES_AMOUNT O...`
- `procedure CALC_YEARLY_TAXABLE_PAY_NEW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_CURR_NET_PAYABLE IN NUMBER DEFAULT NULL, P_CURR_PFUND IN NUMBER DEFAULT NULL, P...`
- `procedure CALC_PERIODICLE_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAID_ARREARS OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE, P_PAID_COA_BASED_EXPENSE OUT PAYROLL.PAY_MASTER.GROSS_...`
- `function CALC_PERIODICLE_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_EMP_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN PERIODICLE_TAXABLE_PAY_TAB PIPELINED`
- `function YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_LOG IN CHAR DEFAULT 'N') RETURN NUMBER`
- `function YEARLY_TAXABLE_PAY_LEAVER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_SETTLEMENT_AMOUNT IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_TRANS_DATE IN DATE DEFAULT SYSDATE) RETURN NUMBER`
- `function YEARLY_TAXABLE_PAY_NEW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_CURRENT_MON_PAYABLE IN NUMBER, P_CURRENT_MON_PFUND IN NUMBER, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_LOG IN CHAR DEFAULT 'N') RETURN NUMBER`
- `function GET_YEARLY_TAXABLE_PAY(P_MRNO VARCHAR2, P_YEAR_CODE NUMBER) RETURN NUMBER`
- `function GET_YEARLY_TAXABLE_PAY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN NUMBER) RETURN NUMBER`
- `function GET_YEARLY_TAXABLE_PAY(P_MRNO VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN NUMBER`
- `function GET_DIRECT_PAID_EXP_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_FROM_DATE IN FINANCE.GL_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE IN FINANCE.GL_FINANCIAL_YEAR.TO_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN NUMBER`
- `function GET_YEARLY_PAID_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE) RETURN NUMBER`
- `function GET_TAX_ADJUSTED_MONTHLY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_YEARLY_TAX IN CHAR DEFAULT 'N') RETURN NUMBER`
- `function GET_TAX_ADJUSTMENT_MONTHLY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE) RETURN NUMBER`
- `function GET_PERIODICLE_PAID_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN NUMBER`
- `procedure CALC_NEXT_MONTH_TAX_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX_DUE IN NUMBER, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_TAX_PAID_SALARY OUT NUMBER, P_TAX_PAID_DIRECT OUT NUMBER, P_TAX_PAID_ADJUST OUT NUMBER, P_TAX_PAID_T...`
- `procedure CALC_NEXT_MONTH_TAX_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX_DUE IN NUMBER, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_TAX_PAID_SALARY OUT NUMBER, P_TAX_PAID_DIRECT OUT NUMBER, P_TAX_PAID_ADJUST OUT NUMBER, P_TAX_PAID_T...`
- `procedure CALC_NEXT_MONTH_TAX_DETAIL_TEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX_DUE IN NUMBER, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_TAX_PAID_SALARY OUT NUMBER, P_TAX_PAID_DIRECT OUT NUMBER, P_TAX_PAID_ADJUST OUT NUMBER, P_TAX_PAID_T...`
- `procedure CALC_NEXT_MONTH_TAX_DETAIL_TEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX_DUE IN NUMBER, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_TAX_PAID_SALARY OUT NUMBER, P_TAX_PAID_DIRECT OUT NUMBER, P_TAX_PAID_ADJUST OUT NUMBER, P_TAX_PAID_T...`
- `procedure CALC_NEXT_MONTH_TAX_MONTHLY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX_DUE IN NUMBER, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_YEARLY_TAXABLE_PAY IN NUMBER, P_TAX_PAID_SALARY OUT NUMBER, P_TAX_PAID_DIRECT OUT NUMBER, P_TAX_PAID...`
- `function GET_MIN_TAX_DEDUCTION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE) RETURN PAYROLL.Pay_Financial_Year.MIN_TAX_DEDUCTION%TYPE`
- `function GET_MIN_TAX_DEDUCTION(P_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE) RETURN PAYROLL.PAY_FINANCIAL_YEAR.MIN_TAX_DEDUCTION%TYPE`
- `procedure GET_TAXABLE_LFA_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_FIN_YEAR IN PAYROLL.PAY_FINANCIAL_YEAR%ROWTYPE, P_MONTHS_REMAIN IN NUMBER, P_PAID_LFA_AMOUNT OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE, P_EXPECTED_LFA_AMOUNT OUT PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VAR...`
- `function GET_TAXABLE_LFA_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_FIN_YEAR IN PAYROLL.PAY_FINANCIAL_YEAR%ROWTYPE, P_MONTHS_REMAIN IN NUMBER) RETURN PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE`
- `procedure GET_TAX_CALCULATION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_TAXABLE_AMOUNT IN NUMBER, P_GENDER IN CHAR DEFAULT 'M', P_TAX_AMOUNT OUT NUMBER, P_SLAB_BASE OUT PAYROLL.DEF_ITAX_SLAB.BASE_TAX_AMOUNT%TYPE, P_SLAB_PERCENT OUT PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VAR...`
- `function GET_UNPAID_LEAVE_AMOUNT(P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `function GET_TAX_SLAB_PERCENTAGE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN NUMBER, P_TAXABLE_AMOUNT IN NUMBER, P_GENDER IN CHAR DEFAULT 'M') RETURN PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE`
- `function GET_DAYS_PERCENTAGE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_MRNO IN PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE) RETURN PAYROLL.DEF_ITAX_SLAB.TAX_PERCENT%TYPE`
- `procedure CALC_YEARLY_TAXABLE_PAY_LEAVER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_LAST_MON_EDATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_EXCHANGE_RATE IN DEFINITIONS.CURRENCY.CURRENT_EXCHANGE_RATE%TYPE, P_LEAVER IN BOOLEAN DEFAULT FALSE, P_SETTLEMENT_AMOUNT IN NUMBER, P_MONTHS_REMAIN...`
- `procedure PENSION_FUND_CONTRIBUTION_RECAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_ADJUSTMENT_CODE IN NUMBER, P_TERMINAL IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VA...`
- `procedure POST_PENSION_FUND_CONTRIBUTION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_POST_UNPOST IN CHAR, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE, P_START_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE, P_END_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_...`

### PKG_ITAX_EXEMPTION

1. This Package will be used for PF Final Settlement

- `procedure QUERY_EMP_ITAX(P_RESULT IN OUT REF_EMP, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.YEAR_CODE%TYPE, P_START_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE, P_END_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.DEF_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE)`
- `procedure INSERT_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure UPDATE_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure DELETE_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure LOCK_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure CALCULATE_EXEMPTED_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.ADJUSTMENT_CODE%TYPE, P_OBJECT_CODE IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_CURR...`
- `procedure POST_UNPOST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_POST_UNPOST IN CHAR, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL_M.YEAR_CODE%TYPE, P_START_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.START_DATE%TYPE, P_END_DATE IN PAYROLL.EMP_ITAX_ADJUSTMENT_MONTHLY.END_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_...`

### PKG_LOAN

This package was created for Cash Refund

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_PF_PROFIT_MEMBERS(P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE) RETURN PF_PROFIT_MEM_TAB PIPELINED`
- `procedure INSERT_PF_PROFIT_MEMBERS(P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_PF_TYPE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_FILE_NO(P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE) RETURN FINANCE.GL_COA.COA_FILE_NO%TYPE`
- `function CHECK_PROFIT_MEMBER(P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN BOOLEAN`
- `function GET_LOAN_MODULE(P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN VARCHAR2`
- `function GET_FILE_NO(P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE`
- `function IS_PROFIT_MEMBER(P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PF_TYPE FINANCE.PF_PROFIT_MEMBERS.PF_TYPE%TYPE, P_TRAN_DATE IN DATE) RETURN FINANCE.PF_PROFIT_MEMBERS.PF_PROFIT%TYPE`
- `function IS_PROFIT_MEMBER(P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PF_TYPE IN FINANCE.PF_PROFIT_MEMBERS.PF_TYPE%TYPE, P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE) RETURN FINANCE.PF_PROFIT_MEMBERS.PF_PROFIT%TYPE`
- `function IS_INTEREST_ON_LOAN(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE) RETURN PAYROLL.DEF_LOAN_TYPE.INTEREST%TYPE`
- `function GET_INTEREST_RATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE, P_YEAR_CODE IN PAYROLL.DEF_LOAN_INTEREST_RATE.YEAR_CODE%TYPE) RETURN PAYROLL.DEF_LOAN_INTEREST_RATE.INTEREST_RATE%TYPE`
- `function IS_REFUND_THROUGH_RECEIPT(P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE) RETURN CHAR`
- `procedure GEN_LOAN_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_LOAN_NO OUT PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT...`
- `procedure CALCULATE_LOAN_INTEREST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_CODE IN PAYROLL.DEF_LOAN_INTEREST_RATE.LOAN_CODE%TYPE, P_LOAN_DATE IN DATE, P_PRINCIPAL_AMOUNT IN PAYROLL.LOAN_PAYMENT_INTEREST.PRINCIPAL_AMOUNT%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_COD...`
- `procedure CALCULATE_LOAN_INTEREST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PRINCIPAL_AMOUNT IN PAYROLL.LOAN_PAYMENT_INTEREST.PRINCIPAL_AMOUNT%TYPE, P_LOAN_INSTALLMENT IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_INSTALLMENT%TYPE, P_INTEREST_RATE IN PAYROLL.DEF_LOAN_INTEREST_RATE.INTEREST_RATE%TYPE, P_INT_NO_OF_MONTHS OUT PAYROLL.LOAN_PAYMENT_IN...`
- `procedure FINALIZE_POST_LOAN_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOAN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CO...`
- `procedure FINALIZE_UNPOST_LOAN_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOAN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_CANCELLED_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VA...`
- `procedure POST_ANNUAL_LOAN_MARKUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MAS...`
- `procedure POST_DEFER_MARKUP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MAS...`
- `procedure CANCEL_LOAN_MARKUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VA...`
- `procedure CHECK_LOAN_ELIGIBILITY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE, P_MRNO IN PAYROLL.LOAN_REFUND_MASTER_N.MRNO%TYPE, P_LOAN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRANS_DATE IN PAYROLL.LOAN_PAYMENT_MASTER_N.TRANS_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT C...`
- `function GET_LOAN_SETTLED_DAYS(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN NUMBER`
- `procedure POPULATE_LOAN_TEMP_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_FROM_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_TO_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_SUPRESS_ZERO...`
- `procedure POPULATE_LOAN_TEMP_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_FROM_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_TO_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_USERID IN CH...`
- `procedure POPULATE_TMP_LOAN_SUMMARY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_FROM_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_TO_LOAN_CODE IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_CODE%TYPE, P_USERID IN CH...`
- `procedure TRAVEL_LOAN_VOUCHER(P_MRNO IN VARCHAR2, P_REQUEST_NO IN VARCHAR2, P_LOAN_LOCATION_ID IN VARCHAR2, P_ADVANCE_AMOUNT IN NUMBER, P_REMARKS IN VARCHAR2, P_VOUCHER_TYPE IN VARCHAR2 DEFAULT 'BPV', P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_LOAN_REFUND

This package contains Procedures relavant to Loan Refund

- `procedure GEN_REFUND_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_REFUND_NO OUT PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP O...`
- `procedure POPULATE_LOAN_INSTALLMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN DATE, P_MON_END_DATE IN DATE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_OVERWRITE IN CHAR, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS....`
- `procedure POST_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIO...`
- `procedure UNPOST_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIO...`
- `procedure FINALIZE_POST_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJEC...`
- `procedure FINALIZE_UNPOST_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_CANCELLED_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL ...`
- `procedure POST_LOAN_REFUND_OLD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJEC...`
- `procedure UNPOST_LOAN_REFUND_OLD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_REFUND_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_CANCELLED_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_CANCELLED_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL ...`
- `procedure GENERATE_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_REFUND_LOCATION_ID IN PAYROLL.PAY_MASTER.LOCATION_ID%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE, P_LOAN_TAB IN REFUND_TAB, P_TEMP_POST IN VARCHAR2, P_REMARKS IN PAYROLL.Loan_Refund_Master_N.REMARKS%TYPE, P_VOUCHER...`

### PKG_MONTH

This package was created to get information related to payroll month

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure FETCH_PAYROLL_LOCATION_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_EMP_LOCATION_ID IN PAYROLL.DEF_PAYROLL_LOCATION.EMP_LOCATION_ID%TYPE, P_PAYROLL_LOCATION_ID OUT PAYROLL.DEF_PAYROLL_LOCATION.PAYROLL_LOCATION_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_CURRENT_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `function GET_PAYROLL_LOCATION_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_PAYROLL_LOCATION.EMP_LOCATION_ID%TYPE) RETURN PAYROLL.DEF_PAYROLL_LOCATION.PAYROLL_LOCATION_ID%TYPE`
- `function GET_CURRENT_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `function GET_LAST_PROCESSED_MON(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `function GET_LAST_PROCESSED_MON(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE IN PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `procedure FETCH_CURRENT_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAY_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE OUT DEFINITIONS.LOCATION_W...`
- `procedure FETCH_CURRENT_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAY_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE OUT DEFINITIONS.LOCATION_W...`
- `procedure FETCH_MONTH_DATES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRANS_DATE IN DATE, P_MONTH_START_DATE OUT DATE, P_MONTH_END_DATE OUT DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure FETCH_PI_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRANS_DATE IN DATE, P_MONTH_START_DATE OUT DATE, P_MONTH_END_DATE OUT DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_LAST_MON_END_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE`
- `function GET_LAST_MON_END_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE IN PAYROLL.PAY_FINANCIAL_YEAR.TO_DATE%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE`
- `procedure CHECK_MONTH_FOR_UPDATION(P_OBJECT_CODE IN VARCHAR2, P_EVENT IN VARCHAR2, P_USER IN VARCHAR2, P_EMP_CODE IN VARCHAR2, P_AD_CODE IN VARCHAR2, P_TRANS_DATE IN DATE, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure FETCH_VOUCHER_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAY_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE OUT DEFINITIONS.LOCATION_W...`
- `procedure FETCH_NEXT_UNPROCESSED_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAY_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE OUT DEFINITIONS.LOCATION_W...`
- `function GET_PROCESSED_PAY_MONTHS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `function GET_PROCESSED_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `procedure FETCH_LAST_PROCESSED_MON(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE, P_PAY_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE OUT DEFINITIONS.LOCATION_W...`
- `function IS_PAY_PROCESSED(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE) RETURN BOOLEAN`
- `procedure FETCH_MONTH_DATES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_MONTH_START_DATE OUT DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MONTH_END_DATE OUT DEFINITIONS.LOCATION_WIS...`
- `procedure SET_MONTH_PROCESS_FLAG(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure SET_MONTH_POST_FLAG(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_MONTH_FROM_PAY_DATES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE`
- `function GET_MONTH_FROM_MON_DATES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MON_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE`
- `function GET_ALL_MONTHS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_ALL_MONTH_TAB PIPELINED`
- `function GET_MON_START_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE`
- `function GET_MON_END_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE`
- `function GET_PAY_START_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE`
- `function GET_PAY_END_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE`
- `procedure VALIDATE_INCREMENT_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_UNPROCESSED_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_MONTH.PAY_MONTH_TAB PIPELINED`
- `procedure FINALIZE_PAY_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure REVERT_MONTH_FINALIZATION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure INSERT_NEXT_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_NEXT_MONTH_DAY IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_NO_OF_MONTHS IN NUMBER DEFAULT 1, P_MONTH OUT DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure INSERT_NEXT_MONTH(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_NEXT_MONTH_DAY IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_NO_OF_MONTHS IN NUMBER DEFAULT 1, P_MONTH OUT DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_PAY_END_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE`
- `function GET_PAY_MONTH_DAYS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRANS_DATE IN DATE) RETURN NUMBER`
- `function GET_MONTH_DESC(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE) RETURN VARCHAR2`

### PKG_PAY

- `function GET_EMP_AD_AMOUNT(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_START_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_PAYMENT_RATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_ARREAR.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_ARREAR.END_DATE%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_ARREAR_TYPE IN PAYROLL.DEF_ARREAR.AD_TYPE%TYPE, P_ARREAR_CODE IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE, P_DA...`
- `function GET_EMP_PF_AMOUNT(P_PF_TYPE IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE) RETURN NUMBER`
- `function GET_GROSS_PAYABLE(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE) RETURN PAYROLL.PAY_MASTER.GROSS_PAYABLE%TYPE`
- `function GET_NET_PAYABLE(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE) RETURN PAYROLL.PAY_MASTER.NET_PAYABLE%TYPE`
- `procedure POPUATE_SALARY_SHEET(P_ORIGINAL_TEST IN VARCHAR2, P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_USER IN CHAR, P_TERMINAL IN CHAR)`
- `procedure POPULATE_COST_TO_COMPANY(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_PAY_START_DATE IN PAYROLL.R_COST_TO_COMPANY_TEMP.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.R_COST_TO_COMPANY_TEMP.END_DATE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_PF_VOUCHER_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.MRNO%TYPE, P_JOINING_DATE IN DATE, P_PAY_END_DATE IN DATE, P_TYPE IN VARCHAR2 ) RETURN NUMBER`

### PKG_PAYROLL

This package was created for Cash Refund

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_SMS_NUMBER(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN VARCHAR2`
- `procedure SEND_SMS(P_EVENT IN VARCHAR2, P_MRNO IN VARCHAR2, P_SMS_TXT IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_SR_NO IN REGISTRATION.SCHEDULE.SR_NO%TYPE, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure PROCESS_SMS_ALERT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_EVENT IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_PAYROLL_LOC_GROUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN EMP_WISE_LOC_TAB PIPELINED`
- `function GET_USER_LOCATIONS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN EMP_WISE_LOC_TAB PIPELINED`
- `function GET_EMPLOYEE_LOCATION(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN DEFINITIONS.LOCATION.LOCATION_ID%TYPE`
- `function GET_PAYROLL_LOCATION(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN DEFINITIONS.LOCATION.LOCATION_ID%TYPE`
- `procedure VARIFY_ENV_SETUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure TRAVEL_REQUEST_APPROVAL(P_MRNO IN VARCHAR2, P_ACTING_FOR IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_PROCESS_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_EVENT IN VARCHAR2, P_ASSIGNMENT_ID IN NUMBER)`
- `function GET_CURRENT_PAY_FINANCIAL_YEAR(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE`
- `function GET_LOAN_DESCRIPTION(P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE.LOAN_CODE%TYPE) RETURN PAYROLL.DEF_LOAN_TYPE.DESCRIPTION%TYPE`
- `function GET_CURRENCY_SHORT_DESC(P_CURRENCY_ID IN DEFINITIONS.CURRENCY.CURRENCY_ID%TYPE) RETURN DEFINITIONS.CURRENCY.MARKETING_SHORT_DESC%TYPE`
- `function GET_AD_SETUP(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_PATIENT_TYPE_ID IN PAYROLL.DEF_AD_SETUP_PT.PATIENT_TYPE_ID%TYPE, P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE, P_AD_TYPE IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE, P_ENTRY_TYPE IN PAYROLL.DEF_AD_SETUP.ENTRY_TYPE%TYPE, P_INCL...`
- `function GET_AD_SETUP(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_PATIENT_TYPE_ID IN PAYROLL.DEF_AD_SETUP_PT.PATIENT_TYPE_ID%TYPE, P_MRNO IN PAYROLL.DEF_EMP_FINANCIAL.MRNO%TYPE, P_AD_TYPE IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE, P_ENTRY_TYPE IN PAYROLL.DEF_AD_SETUP.ENTRY_TYPE%TYPE, P_INCLUDE_IN_GROSS IN PAYROLL.DEF_AD_SETUP.INCLUDE_IN_GRO...`
- `function GET_AD_PAYMENT_PERCENTAGE(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE, P_LEAVE_TYPE_ID IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE) RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.PAYMENT_PERCENTAGE%TYPE`
- `function GET_LEAVE_TYPE_ID(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_DATE IN DATE) RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE`
- `function GET_AD_RATE_PER_DAY(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_AD_CODE IN PAYROLL.Def_Ad_Setup.AD_CODE%TYPE, P_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function CALC_GM(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_MRNO IN VARCHAR2, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function CALC_CURR_MON_GM(P_MRNO IN VARCHAR2) RETURN PAYROLL.EMP_ALLOWANCE_DEDUCTION_DETAIL.AMOUNT%TYPE`
- `function GET_FINACIAL_YEARCODE(P_DATE IN DATE) RETURN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE`
- `function GET_AD_DESC(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE) RETURN PAYROLL.DEF_AD_SETUP.DESCRIPTION%TYPE`
- `function GET_AD_TYPE(P_AD_CODE IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE) RETURN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE`
- `function GET_AD_TYPE_DESC(P_AD_CODE IN PAYROLL.DEF_AD_SETUP.AD_CODE%TYPE) RETURN VARCHAR2`
- `function IS_ARREAR_IN_GROSS(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE) RETURN PAYROLL.DEF_SETUP.VALUE%TYPE`
- `function GET_VOUCHER_STATUS(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE) RETURN FINANCE.GL_TRAN_MASTER.VOUCHER_STATUS%TYPE`
- `function GET_SPELL_NUMBER(p_number IN NUMBER) RETURN VARCHAR2`
- `function PROCESS_INACTIVE_EMP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN VARCHAR2`
- `function GET_INACTIVE_EMP_SAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE, P_MON_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_START_DATE%TYPE, P_MON_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE) RETURN INACTIVE_EMP...`

### PKG_PAYSCALE

This package was created for Cash Refund

- `procedure GENERATE_PAYSCALE_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN PAYROLL.DEF_PAYSCALE.YEAR_CODE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_PATIENT_TYPE_GROUP_ID(P_PATIENT_TYPE_ID IN HRD.INFORMATION.PATIENT_TYPE_ID%TYPE) RETURN DEFINITIONS.PATIENT_TYPE_GROUPS.GROUP_ID%TYPE`
- `function GET_DESIGNATION_CATEGORY_ID(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE) RETURN DEFINITIONS.DESIGNATION_CATEGORY.DESIGNATION_CATEGORY_ID%TYPE`
- `function GET_DESIGNATION_CATEGORY_LIST(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN SYS_REFCURSOR`
- `function GET_EMP_SETUP_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN SYS_REFCURSOR`
- `function GET_EMP_GROSS_ALL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN SYS_REFCURSOR`
- `function GET_STAGE_NO(P_GRADE_ID IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE, P_AMOUNT IN PAYROLL.DEF_PAYSCALE_DETAIL.AMOUNT%TYPE, P_DATE IN PAYROLL.PAY_FINANCIAL_YEAR.FROM_DATE%TYPE DEFAULT SYSDATE) RETURN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE`
- `function GET_EMP_CURR_STAGE_NO(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE`
- `function GET_STAGE_MAX_AMOUNT(P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_GRADE_ID IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE) RETURN PAYROLL.DEF_PAYSCALE.MAX_AMOUNT%TYPE`
- `procedure GET_PAYSCALE_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_GRADE_ID IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE, P_STAGE_NO IN PAYROLL.DEF_PAYSCALE_DETAIL.STAGE_NO%TYPE, P_BASIC_AMOUNT OUT PAYROLL.DEF_PAYSCALE_DETAIL.AMOUNT%TYPE, P_PERSONAL_PAY OUT PAYROLL.DEF_PAYSCALE_...`
- `procedure GET_AD_CHART_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PATIENT_TYPE_ID IN HRD.INFORMATION.PATIENT_TYPE_ID%TYPE, P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE, P_GRADE_ID IN PAYROLL.DEF_PAYSCALE_DETAIL.GRADE_ID%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_CHART_DETAIL.AD_CODE%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P...`
- `procedure GET_PERCENTAGE_VALUE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_GRADE_ID IN DEFINITIONS.GRADES.GRADE_ID%TYPE, P_DEFAULT_PERCENTAGE IN PAYROLL.DEF_AD_SETUP.CALC_PERCENTAGE%TYPE, P_BASE_VALUE IN PAYROLL.DEF_EMP_FINANCIAL.CURRENT_GROSS%TYPE, P_PERCENTAGE_SETUP_ID IN PAYROLL.DEF_PERCENTAGE_SETUP.PERCENTAGE_SETUP_ID%TYPE, P_AMOUNT ...`

### PKG_PAY_PROCESS

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_LEAVE_TYPE_FACTOR(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LEAVE_TYPE_ID IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.LEAVE_TYPE_ID%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_SETUP_UNPAID_LT.AD_CODE%TYPE) RETURN PAYROLL.DEF_AD_SETUP_UNPAID_LT.PAYMENT_PERCENTAGE%TYPE`
- `function GET_CURR_MONTH_PF_AMOUNT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PF_TYPE IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE) RETURN NUMBER`
- `function GET_TOTAL_INCOME_LAST_MON(P_PAY_START_DATE IN DATE, P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE, P_TAXABLE_GROSS IN NUMBER, P_NEW_MONTH_TAXABLE_PF IN NUMBER) RETURN NUMBER`
- `function GET_TAX_PAID_LAST_MONTH(P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE) RETURN NUMBER`
- `procedure CALCULATE_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_EMP_SAL_START_DATE IN OUT DATE, P_EMP_SAL_END_DATE IN OUT DATE, P_SALCERMONTH IN CHAR, P_USERNAME IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ND_END_DATE IN DATE, P_ND_START_DATE IN DATE, P_PAY_MONTH_DAYS IN NUMBER, P_LOCATION_ID IN VARCHAR2, P_ORGANIZATION_ID IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure POST_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure UNCALC_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure UNPOST_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function GET_NO_CASH_TAX_APPLICABLE(P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE) RETURN NUMBER`
- `procedure NO_CASH_TAX_APPLICABLE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_MONTHS_REMAIN IN NUMBER, P_CASH_TAX_APPLICABLE_MONTHLY OUT NUMBER, P_CASH_TAX_APPLICABLE_YEARLY OUT NUMBER, p_REV_...`

### PKG_PAY_VOUCHER

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure ADD_VOUCHER_REFERENCES(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_OLD_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_NEW_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure DELETE_TEMP_VOUCHER(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure GENERATE_TEMP_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DAT...`
- `procedure POST_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN ...`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE) RETURN NUMBER`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN ...`
- `procedure CHECK_GL_SETUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function IS_PAY_VOUCHER_POSTED(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE) RETURN CHAR`

### PKG_PF_VOUCHER

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_TRAN_DETAIL(P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE) RETURN SYS_REFCURSOR`
- `procedure GET_VOUCHER_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_RESULT OUT SYS_...`
- `procedure ADD_VOUCHER_REFERENCES(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_OLD_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_NEW_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.EN...`
- `procedure GENERATE_TEMP_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER....`
- `procedure POST_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER....`
- `procedure DELETE_TEMP_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER....`
- `procedure CANCEL_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER....`
- `procedure CANCEL_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_CANCEL_TRANS_DATE IN FINANCE.Pf_Tran_Master.TRANS_DATE%TYPE DEFAULT NULL, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2...`
- `procedure GENERATE_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PF_TYPE IN VARCHAR2, P_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_ORIGINAL_TEMP IN CHAR, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO OUT FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_OBJEC...`
- `procedure POST_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE, P_PF_TYPE IN VARCHAR2, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR...`
- `procedure POST_PF_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.PF_TRAN_MASTER.TRANS_DATE%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHA...`
- `function GET_FUND_BALANCE(P_YEAR_CODE IN FINANCE.GL_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_PF_TYPE IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN NUMBER`
- `procedure PF_VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE IN CHAR, P_FROM_VOUCHER_NO IN CHAR, P_TO_VOUCHER_NO IN CHAR, P_USERID IN CHAR, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR, P_FROM_NEW_VOUCHER_NO OUT CHAR, P_TO_NEW_VOUCHER_NO OUT ...`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE) RETURN NUMBER`

### PKG_PROFIT_VOUCHER

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure GET_VOUCHER_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_PROFIT_RATIO IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE, P_ENTRY_TYPE IN FINANCE.GL_PF_VOUCHE...`
- `procedure ADD_VOUCHER_REFERENCES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_PROFIT_RATIO IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE, P_ENTRY_TYPE IN FINANCE.GL_PF_VOUCHE...`
- `procedure GENERATE_TEMP_PROFIT_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_PROFIT_RATIO IN FINANCE.GL_PF_VOUCHER.PROFIT_RATIO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.V...`
- `procedure POST_PROFIT_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VO...`
- `procedure DELETE_TEMP_PROFIT_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VO...`
- `procedure CANCEL_PROFIT_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_SERIAL_NO IN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VO...`
- `function GET_SERIAL_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE) RETURN FINANCE.GL_PF_VOUCHER.SERIAL_NO%TYPE`

### PKG_S16APX00110

1. This Package will be used for FINAL SETTLEMENT

- `procedure POPULATE_FINAL_SETTLEMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CLEARANCE_CERTIFICATE_ID IN HRD.EMP_CLEARANCE_CERTIFICATE.CLEARANCE_CERTIFICATE_ID%TYPE, P_CC_LOCATION_ID IN HRD.EMP_CLEARANCE_CERTIFICATE.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRN...`
- `procedure POPULATE_SALARY_ELEMENT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_clearance_certificate_id IN PAYROLL.FINAL_SETTLEMENT.CLEARANCE_CERTIFICATE_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_...`
- `function GET_ELEMENT_VALUE(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_clearance_certificate_id IN HRD.EMP_CLEARANCE_CERTIFICATE.CLEARANCE_CERTIFICATE_ID%TYPE, P_ELEMENT IN PAYROLL.DEF_FS_ELEMENT.ELEMENT_CODE%TYPE) RETURN PAYROLL.FINAL_SETTLEMENT_ELEMENT.VALUE%TYPE`
- `function GET_ELEMENT_AMOUNT(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ELEMENT IN PAYROLL.DEF_FS_ELEMENT.ELEMENT_CODE%TYPE, P_VALUE IN PAYROLL.FINAL_SETTLEMENT_ELEMENT.VALUE%TYPE) RETURN PAYROLL.FINAL_SETTLEMENT_ELEMENT.AMOUNT%TYPE`
- `procedure CALCULATE_ELEMENT(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_clearance_certificate_id IN PAYROLL.FINAL_SETTLEMENT.CLEARANCE_CERTIFICATE_ID%TYPE, P_AMOUNT_INITIATE IN VARCHAR2, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OB...`
- `procedure CALCULATE_INCOME_TAX(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR )`
- `procedure GEN_EXPENSE_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_EXPENSE_NO OUT PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP ...`
- `procedure PROCESS_EMP_EXPENSE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VAR...`
- `procedure INSERT_EMP_EXPENSE(P_BLOCK_DATA IN OUT EMP_EXPENSE_TAB, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_DEPT_HOD_MRNO(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `function GET_HOD_CC(P_COST_CENTRE IN MMS.COST_CENTRE_HEAD.SUB_LDGR_ITEM_CODE%TYPE) RETURN REGISTRATION.PATIENT.MRNO%TYPE`
- `function GET_EVENT_LABEL(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.LABEL_DESC%TYPE`
- `function GET_EVENT_COLOR(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.COLOR_CODE%TYPE`
- `function GET_EVENT_DESC(P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE`
- `function GET_EVENT_DESC(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_WFE_NO IN PAYROLL.FINAL_SETTLEMENT_WF.WFE_NO%TYPE) RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE`
- `function GET_NEXT_EVENT_ID(P_SCHEMA_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE, P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE, P_WORK_FLOW_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE) RETURN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE`
- `function GEN_WFE_NO(P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE) RETURN PAYROLL.FINAL_SETTLEMENT_WF.WFE_NO%TYPE`
- `procedure GET_FS_WORKFLOW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_WORKFLOW_REC OUT RADIATION.PKG_WORKFLOW.T_WORKFLOW_REC, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_IN_QUEUE_USERS(P_FINAL_SETTLEMENT_ID PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE) RETURN VARCHAR2`
- `procedure INITIALIZE_WORKFLOW(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure POST_WORKFLOW_EVENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_WORKFLOW_REMARKS IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.REMARKS%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DE...`
- `procedure PERFORM_EVENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS...`
- `procedure PROCESS_SMS_ALERT(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_NEXT_EVENT_ID IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.EVENT_ID%TYPE, P_EVENT IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `procedure POPULATE_QUEUE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_WFE_NO IN PAYROLL.FINAL_SETTLEMENT_WF_Q.WFE_NO%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TE...`
- `function GET_PARAMETER_VALUE(P_SCHEMA_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE, P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE, P_WORK_FLOW_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE, P_EVENT_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE, P_PARAMETER_TYPE IN DEFINITIONS.EVENT_WISE_PARAMETER.PARAMETER_TYPE%TYPE) RETURN DEFINITIONS.EVENT_WISE_DETAIL.PARAMETER_VALUE%TYPE`
- `procedure CHECK_GL_SETUP(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure GENERATE_TEMP_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FINAL_SETTLEMENT_ID IN PAYROLL.FINAL_SETTLEMENT.FINAL_SETTLEMENT_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE, P_CURRENCY_ID IN FINANCE...`
- `procedure POST_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, ...`

### PKG_S16APX00127

- `procedure APPROVE_MONTH_CHANGE(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_REQUEST_NO IN NUMBER, P_APPROVED_BY IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S16FRM00023

1. This Package will be used for PAYROLL DISCHARGE

- `procedure QUERY_PAY_TMP_BANK(P_RESULT IN OUT REF_PAY_TMP_BANK, P_USERID IN PAYROLL.PAY_TMP_BANK.USERID%TYPE, P_TERMINAL IN PAYROLL.PAY_TMP_BANK.TERMINAL%TYPE)`
- `procedure UPDATE_PAY_TMP_BANK(P_RESULT IN OUT TAB_PAY_TMP_BANK)`
- `procedure LOCK_PAY_TMP_BANK(P_RESULT IN OUT TAB_PAY_TMP_BANK)`
- `procedure SELECT_PAY_TMP_BANK(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_SINGLE_ALL IN CHAR, P_BANK_ID IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE, P_BRANCH_ID IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE, P_USERID IN SECURITY.USERS.USERID%TYPE, P_SELECTED IN PAYROLL.PAY_TMP_BANK.SELECTED%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,...`
- `procedure POPULATE_PAY_TMP_BANK(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_BANK_ID IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE, P_FROM_BANK_CODE IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE, P_FROM_BRANCH_CODE IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%TYPE, P_TO_BANK_CODE IN PAYROLL.PAY_TMP_BANK.BANK_ID%TYPE, P_TO_BRANCH_CODE IN PAYROLL.PAY_TMP_BANK.BRANCH_ID%...`
- `procedure PROC_SHOW_ACCOUNT_BREAKUPS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_BANK_ID IN DEFINITIONS.BANK.BANK_ID%TYPE, P_ONLINE_ACCOUNT IN CHAR, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, ...`

### PKG_S16FRM00028

1. This Package will be used for PAYROLL EMP ALLOWANCES AND DEDUCTION

- `procedure QUERY_AD(P_RESULT IN OUT AD_REF, P_MONTH_START_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE, P_MONTH_END_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE)`
- `procedure QUERY_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_REF, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.END_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_AD_CODE IN PAYROLL.ALLOWANCE_DEDUCTION_DETAIL.AD_CODE%TYPE, P_ORDER_BY IN VARCHAR2)`
- `procedure INSERT_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB)`
- `procedure UPDATE_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB)`
- `procedure DELETE_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB)`
- `procedure LOCK_PAYROLL_AD(P_RESULT IN OUT AD_DETAIL_TAB)`

### PKG_S16FRM00029

1. This Package will be used for PAYROLL ARREARS

- `procedure QUERY_ARREARS(P_RESULT IN OUT ARREAR_REF, P_MONTH_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE, P_MONTH_END_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE, P_MONTH IN VARCHAR2, P_ARREAR_CODE IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE)`
- `procedure QUERY_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_REF, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_START_DATE%TYPE, P_END_DATE IN PAYROLL.ARREAR_DETAIL.ARREAR_END_DATE%TYPE, P_ARREAR_CODE IN PAYROLL.DEF_ARREAR.ARREAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_AD_CODE IN PAYROLL.ARREAR_DETAIL.AD_CODE%TYPE, P_ORDER_BY IN VARCHAR2)`
- `procedure INSERT_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB)`
- `procedure UPDATE_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB)`
- `procedure DELETE_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB)`
- `procedure LOCK_PAYROLL_ARREARS(P_RESULT IN OUT ARREAR_DETAIL_TAB)`

### PKG_S16FRM00030

1. This Package will be used for PAYROLL ARREARS

- `procedure POST_AWARD_PAYMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_DOCUMENT_NO IN PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure GET_AMOUNTS(P_LOCATION_ID IN PAYROLL.EMP_EXPENSE.LOCATION_ID%TYPE, P_EMPLOYEE_NO IN PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_MRNO IN PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_EXPENSE_CODE IN PAYROLL.EMP_EXPENSE.EXPENSE_CODE%TYPE, P_JOINING_DATE IN PAYROLL.EMP_EXPENSE.JOINING_DATE%TYPE, P_CURRENT_GROSS OUT PAYROLL.EMP_EXPENSE.CURRENT_GROSS%TYPE, P_CURRENT_BASIC OUT PAYROLL.EMP_EXPENSE.CURRENT_BASIC%TYPE, P_CURRENT_LFA OUT ...`
- `procedure VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_USERID IN VARCHAR2, P_TRAN_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE, P_DOCUMENT_NO IN PAYROLL.EMP_EXPENSE.DOCUMENT_NO%TYPE, P_MRNO IN PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_LFA_DUE_DATE IN PAYROLL.EMP_EXPENSE.LFA_DUE_DATE%TYPE, P_NEW_VOUCHER_NO OUT FINANCE.GL_TRAN_MASTER.VOUCHE...`
- `procedure UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO IN CHAR, P_VOUCHER_TYPE IN CHAR, P_NEW_VOUCHER_NO IN CHAR, P_OBJECT_CODE IN CHAR, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S16FRM00031

1. This Package will be used for PAYROLL EMPLOYEE INCREMENT

- `procedure QUERY_INCREMENT_MASTER(P_RESULT IN OUT REF_INCREMENT_MASTER, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CURRENT IN CHAR, P_EMP_ACTIVE IN CHAR)`
- `procedure INSERT_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure UPDATE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure DELETE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure LOCK_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure QUERY_INCREMENT_DETAIL(P_RESULT IN OUT REF_INCREMENT_DETAIL, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE)`
- `procedure INSERT_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure UPDATE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure DELETE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure LOCK_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`

### PKG_S16FRM00036

1. This Package will be used for POST VOUCHER

- `procedure VOUCHER_PERMANENT_POST(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_FROM_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TO_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_USERID IN VARCHAR2, P_FROM_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE, P_TO_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE, P_FROM_NEW_VOUCHER_NO OUT FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TO_NEW_VOUCHER_NO ...`
- `procedure UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO IN CHAR, P_VOUCHER_TYPE IN CHAR, P_NEW_VOUCHER_NO IN CHAR, P_OBJECT_CODE IN CHAR, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S16FRM00037

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure QUERY_LOAN_REFUND_MASTER(P_RESULT IN OUT REF_LOAN_REFUND_MASTER, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_MRNO IN PAYROLL.LOAN_REFUND_MASTER.MRNO%TYPE)`
- `procedure INSERT_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure UPDATE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure DELETE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure LOCK_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure QUERY_LOAN_REFUND_DETAIL(P_RESULT IN OUT REF_LOAN_REFUND_DETAIL, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE)`
- `procedure UPDATE_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL, P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE)`
- `procedure LOCK_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL, P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL.REFUND_NO%TYPE)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE)`
- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.GL_TRAN_MASTER.TRANS_DATE%TYPE, P_CURRENCY_ID IN FINANCE.GL_TRAN_MASTER.CU...`
- `procedure POST_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN...`
- `procedure DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN...`
- `procedure CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN...`
- `function IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN DATE`
- `function IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN BOOLEAN`
- `function GENERATE_REFUND_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN VARCHAR2`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure FINALIZE_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure UNFINALIZE_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`

### PKG_S16FRM00038

- `procedure CALCULATE_LOAN(P_MRNO IN VARCHAR2, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure CALCULATE_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_EMP_SAL_START_DATE IN OUT DATE, P_EMP_SAL_END_DATE IN OUT DATE, P_SALCERMONTH IN CHAR, P_USERNAME IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ND_END_DATE IN DATE, P_ND_START_DATE IN DATE, P_PAY_MONTH_DAYS IN NUMBER, P_LOCATION_ID IN VARCHAR2, P_ORGANIZATION_ID IN VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2 )`
- `procedure POST_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure UNCALC_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure UNPOST_PAYROLL(P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure ALL_EMP_MONTHLY_SAL(P_USER_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_MRNO IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_MONTH_START_DATE DATE, P_MONTH_END_DATE DATE, P_MONTH_DAYS NUMBER, P_CALC_PCTAGE NUMBER, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_EMP_SAL_START_DATE IN DATE, P_EMP_SAL_END_DATE IN DATE, P_ND_END_DATE IN DATE )`
- `procedure EMP_MONTHLY_SALARY(P_MRNO IN VARCHAR2, P_USER_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_MONTH_START_DATE IN DATE, P_MONTH_END_DATE IN DATE, P_MONTH_DAYS IN NUMBER, P_DAILY_WAGER IN CHAR, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_EMP_SAL_START_DATE IN DATE, P_EMP_SAL_END_DATE IN DATE )`
- `procedure EMPLOYEE_DAILY_SALARY(P_MRNO IN VARCHAR2, P_DATE IN DATE, P_USER_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_MONTH_START_DATE IN DATE, P_MONTH_END_DATE IN DATE, P_MONTH_DAYS IN NUMBER, P_PAID_UNPAID IN CHAR, P_DAILY_WAGER IN CHAR, P_DAILY_RATE OUT NUMBER, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE )`
- `procedure EMPLOYEE_DAILY_AD(P_MRNO IN VARCHAR2, P_AD_CODE IN CHAR, P_MONTH_START_DATE IN DATE, P_MONTH_END_DATE IN DATE, P_MONTH_DAYS IN NUMBER, P_AMOUNT OUT NUMBER, P_EMP_SAL_START_DATE IN DATE, P_EMP_SAL_END_DATE IN DATE )`
- `function F_GET_PAYROLL_EMP_LOCATION(P_START_DATE DATE, P_END_DATE DATE, P_MRNO VARCHAR2) RETURN VARCHAR2`
- `procedure QUERY_PAY_TMP_EMP(P_RESULT IN OUT PAY_TMP_EMP_REF, P_EXCEPTION_RECORDS IN CHAR, P_PAYROLL_LOCATION_ID IN PAYROLL.PAY_TMP_EMP.PAYROLL_LOCATION_ID%TYPE)`
- `procedure UPDATE_PAY_TMP_EMP(P_BLOCK_DATA IN OUT PAY_TMP_EMP_TAB)`
- `procedure LOCK_PAY_TMP_EMP(P_BLOCK_DATA IN OUT PAY_TMP_EMP_TAB)`
- `procedure INSERT_PAY_TEMP_EMP(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_NAME REGISTRATION.PATIENT.NAME%TYPE, P_SELECT_FLAG IN PAYROLL.PAY_TMP_EMP.SELECT_FLAG%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOCATION_ID IN DEFINIT...`
- `procedure POPULATE_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CAL_POST IN CHAR, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_MON_START_DATE IN DATE, P_MON_END_DATE IN DATE, P_MONTH_CODE IN VARCHAR2, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, ...`
- `procedure INSERT_PAY_MASTER_TEST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_PAY_MONTH_DAYS IN PAYROLL.PAY_MASTER_TEST.MONTH_DAYS%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP O...`
- `procedure CHECK_PREREQUSITS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_SALCERMONTH IN CHAR, P_FUNCTIONALITY IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TAB OUT PAYROLL.PKG_S16FRM00038.MSG_TAB, P_AL...`
- `procedure CHECK_POSTREQUSITS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FUNCTIONALITY IN VARCHAR2, P_TAB OUT PAYROLL.PKG_S16FRM00038.POST_MSG_TAB, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_S16FRM00039

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`

### PKG_S16FRM00042

1. This Package will be used for PAYROLL ARREARS

- `procedure QUERY_TAX(P_RESULT IN OUT TAX_REF, P_MONTH_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE)`
- `procedure QUERY_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_REF, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ORDER_BY IN VARCHAR2)`
- `procedure UPDATE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure LOCK_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure NEXT_MONTH_PROPOSED_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_MRNO IN PAYROLL.PAY_ITAX_DETAIL.MRNO%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P...`
- `procedure NEXT_MONTH_PROPOSED_TAX2(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE,...`
- `procedure UPDATE_PROPOSED_TAX_ALL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MON_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MON_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE,...`

### PKG_S16FRM00046

1. This Package will be used for PAYROLL EMPLOYEE INCREMENT

- `procedure QUERY_INCREMENT_MASTER(P_RESULT IN OUT REF_INCREMENT_MASTER, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)`
- `procedure INSERT_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure UPDATE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure DELETE_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure LOCK_INCREMENT_MASTER(P_RESULT IN OUT TAB_INCREMENT_MASTER)`
- `procedure QUERY_INCREMENT_DETAIL(P_RESULT IN OUT REF_INCREMENT_DETAIL, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_INCREMENT_DATE IN PAYROLL.EMP_INCREMENT_DETAIL.INCREMENT_DATE%TYPE, P_AD_CODE IN PAYROLL.DEF_AD_CONSTANT.AD_CODE%TYPE)`
- `procedure INSERT_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure UPDATE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure DELETE_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`
- `procedure LOCK_INCREMENT_DETAIL(P_RESULT IN OUT EMP_INCREMENT_DETAIL_TAB)`

### PKG_S16FRM00060

1. This Package will be used for STOP SALARY PAYMENT

- `procedure QUERY_MONTH(P_RESULT IN OUT MONTH_REF, P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_STATUS.DATE_TO%TYPE)`
- `function F_QUERY_MONTH_APEX(P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_STATUS.DATE_TO%TYPE) RETURN TAB_MONTH PIPELINED`
- `procedure QUERY_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_REF, P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_STATUS.DATE_TO%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)`
- `procedure INSERT_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB)`
- `procedure UPDATE_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB)`
- `procedure DELETE_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB)`
- `procedure LOCK_SALARY_STOP(P_RESULT IN OUT SALARY_STOP_TAB)`

### PKG_S16FRM00061

- `function F_TRAN_MASTER_QRY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE) RETURN TRAN_MASTER_TBL_PF PIPELINED`
- `procedure P_TRAN_MASTER_QRY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_DATA IN OUT TRAN_MASTER_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_TRAN_MASTER_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN TRAN_MASTER_REC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_TRAN_MASTER_INS(P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_DATA IN OUT TRAN_MASTER_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_TRAN_MASTER_LCK(P_DATA IN OUT TRAN_MASTER_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_TRAN_MASTER_UPD(P_DATA IN OUT TRAN_MASTER_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_TRAN_MASTER_DEL(P_DATA IN OUT TRAN_MASTER_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `function GET_COA_DESCRIPTION(P_COA_CODE IN VARCHAR2) RETURN VARCHAR2`
- `function GET_SUB_LDGR_ITEM_DESC(P_ledger_type_code IN VARCHAR2, P_sub_ldgr_item_code IN VARCHAR2) RETURN VARCHAR2`
- `function F_GL_TRAN_DETAIL_QY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE, P_SERIAL_NO IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE) RETURN GL_TRAN_DETAIL_TBL_PF PIPELINED`
- `procedure P_GL_TRAN_DETAIL_QY(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE, P_SERIAL_NO IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE, P_DATA IN OUT GL_TRAN_DETAIL_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GL_TRAN_DETAIL_VAL(P_VALIDATION_TYPE IN VARCHAR2, P_DATA IN GL_TRAN_DETAIL_REC, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GL_TRAN_DETAIL_INS(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_DETAIL.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_DETAIL.VOUCHER_NO%TYPE, P_SERIAL_NO IN FINANCE.GL_TRAN_DETAIL.SERIAL_NO%TYPE, P_DATA IN OUT GL_TRAN_DETAIL_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GL_TRAN_DETAIL_LCK(P_DATA IN OUT GL_TRAN_DETAIL_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GL_TRAN_DETAIL_UPD(P_DATA IN OUT GL_TRAN_DETAIL_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_GL_TRAN_DETAIL_DEL(P_DATA IN OUT GL_TRAN_DETAIL_TBL, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_INSERT_GL_TRAN_MASTER(P_START_DATE IN DATE, P_END_DATE IN DATE, P_USER_MRNO IN VARCHAR2, P_REMARKS IN VARCHAR2, P_CURRENCY_ID IN VARCHAR2, P_CURRENCY_RATE IN NUMBER, P_VOUCHER_TYPE IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_VOUCHER_NO OUT VARCHAR2, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_GENRATE_PESSI_VOUCHER(P_START_DATE IN DATE, P_END_DATE IN DATE, P_VOUCHER_NO IN OUT VARCHAR2, P_VOUCHER_TYPE IN VARCHAR2, P_REMARKS IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_CURRENCY_ID IN VARCHAR2, P_CURRENCY_RATE IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `function GET_TEMP_VOUCHER_NO(P_TRANS_DATE DATE, P_VOUCHER_TYPE VARCHAR2, P_MRNO IN VARCHAR2, P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2`
- `procedure PRO_UPDATE_SSC_CAL_MAST(P_START_DATE IN DATE, P_END_DATE IN DATE, P_VOUCHER_NO IN VARCHAR2, P_VOUCHER_TYPE IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_CANCEL_BTN(P_VOUCHER_NO IN VARCHAR2, P_VOUCHER_TYPE IN VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure PRO_CHECK_PESSI_AMOUNT(P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_VOUCHER_NO IN VARCHAR2, P_VOUCHER_TYPE IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_FORM_AMOUNT IN NUMBER, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S16FRM00070

THIS PACKAGE WAS CREATED FOR CASH REFUND

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EXP_CLAIM_MASTER(P_RESULT IN OUT EXP_CLAIM_MASTER_REF, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_MRNO IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE)`
- `procedure INSERT_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure UPDATE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure DELETE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure LOCK_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure QUERY_EXP_CLAIM_DETAIL(P_RESULT IN OUT EXP_CLAIM_DETAIL_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE, P_SR_NO IN PAYROLL.EXPENSE_CLAIM_DETAIL.SRNO%TYPE, P_EXPENSE_TYPE_ID IN PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE, P_FROM_DATE IN PAYROLL.EXPENSE_CLAIM_DETAIL.FROM_DATE%TYPE, P_TO_DATE IN PAYROLL.EXPENSE_CLAIM_DETAIL.TO_DATE%TYPE)`
- `procedure INSERT_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure UPDATE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure DELETE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure LOCK_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure QUERY_EXP_CLAIM_PROJECT(P_RESULT IN OUT EXP_CLAIM_PROJECT_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE, P_PROJECT_ID IN PAYROLL.EXPENSE_CLAIM_PROJECT.PROJECT_ID%TYPE, P_EXP_PERCENTAGE IN PAYROLL.EXPENSE_CLAIM_PROJECT.EXP_PERCENTAGE%TYPE, P_REMARKS IN PAYROLL.EXPENSE_CLAIM_PROJECT.REMARKS%TYPE)`
- `procedure INSERT_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure UPDATE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure DELETE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure LOCK_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure QUERY_EXP_CLAIM_TRACK(P_RESULT IN OUT EXP_CLAIM_TRACK_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_WORKFLOW_Q.CLAIM_NO%TYPE)`
- `procedure P_TRAVEL_VISIT_DETAIL_QRY(P_REF_DATA IN OUT TRAVEL_VISIT_DETAIL_REF, P_CLAIM_NO PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE)`
- `procedure P_TRAVEL_VISIT_DETAIL_INS(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB)`
- `procedure P_TRAVEL_VISIT_DETAIL_UPD(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB)`
- `procedure P_TRAVEL_VISIT_DETAIL_DEL(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB)`
- `procedure P_TRAVEL_VISIT_DETAIL_LOCK(P_BLOCK_DATA IN OUT TRAVEL_VISIT_DETAIL_TAB)`
- `procedure P_TRAVEL_VISIT_ATTACHMENT_QRY(P_REF_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_REF, P_CLAIM_NO PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE)`
- `procedure P_TRAVEL_VISIT_ATTACHMENT_INS(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB)`
- `procedure P_TRAVEL_VISIT_ATTACHMENT_UPD(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB)`
- `procedure P_TRAVEL_VISIT_ATTACHMENT_DEL(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB)`
- `procedure P_TRAVEL_VISIT_ATTACHMENT_LOCK(P_BLOCK_DATA IN OUT TRAVEL_VISIT_ATTACHMENT_TAB)`
- `function F_GET_DECISION_LIST( p_claim_no IN PAYROLL.EXPENSE_CLAIM_WORKFLOW.CLAIM_NO%TYPE, p_schema_id IN NUMBER, p_workflow_type_id IN NUMBER, p_work_flow_id IN NUMBER, p_event_id IN NUMBER, p_event_orderby IN NUMBER, p_next_event_id IN NUMBER ) RETURN SYS_REFCURSOR`

### PKG_S16FRM00072

This package was created for Exployee Expense Approval

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_EXPENSE_TYPE IN PAYROLL.EXPENSE_CLAIM_MASTER.EXPENSE_CODE%TYPE, P_MRNO IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE, P_AUTHORITY_MRNO IN PAYROLL.EXPENSE_CLAIM_MASTER.AUTHORITY_MRNO%TYPE, P_EVENT_ID IN DEFINITIONS.EVENT.EVENT_ID%TYPE)`
- `procedure INSERT_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure UPDATE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure DELETE_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure LOCK_EXP_CLAIM_MASTER(P_BLOCK_DATA IN OUT EXP_CLAIM_MASTER_TAB)`
- `procedure QUERY_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_DETAIL.CLAIM_NO%TYPE, P_EXPENSE_TYPE_ID IN PAYROLL.EXPENSE_CLAIM_DETAIL.EXPENSE_TYPE_ID%TYPE)`
- `procedure INSERT_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure UPDATE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure DELETE_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure LOCK_EXP_CLAIM_DETAIL(P_BLOCK_DATA IN OUT EXP_CLAIM_DETAIL_TAB)`
- `procedure QUERY_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_REF, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_PROJECT.CLAIM_NO%TYPE)`
- `procedure INSERT_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure UPDATE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure DELETE_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure LOCK_EXP_CLAIM_PROJECT(P_BLOCK_DATA IN OUT EXP_CLAIM_PROJECT_TAB)`
- `procedure QUERY_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT REF_LOAN_REFUND_DETAIL, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER.REFUND_NO%TYPE, P_REQUEST_ID IN PAYROLL.LOAN_PAYMENT_MASTER.TRAVEL_REQUEST_NO%TYPE)`
- `procedure UPDATE_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT TAB_LOAN_REFUND_DETAIL)`
- `procedure LOCK_LOAN_REFUND_DETAIL(P_BLOCK_DATA IN OUT TAB_LOAN_REFUND_DETAIL)`

### PKG_S16FRM00076

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure QUERY_TMP_DETAIL_CR(P_RESULT IN OUT REF_TMP_DETAIL, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE, P_COA_CODE IN FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE, P_MRNO IN PAYRO...`
- `procedure QUERY_TMP_DETAIL_DR(P_RESULT IN OUT REF_TMP_DETAIL, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_TRAN_DETAIL.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_TRAN_DETAIL.SUB_LDGR_ITEM_CODE%TYPE, P_COA_CODE IN FINANCE.GL_TRAN_DETAIL.COA_CODE%TYPE, P_MRNO IN PAYRO...`

### PKG_S16FRM00077

1. This Package will be used for PAYROLL LOAN PAYMENT

- `procedure QUERY_LOAN_PAYMENT_MASTER(P_RESULT IN OUT REF_LOAN_PAYMENT_MASTER, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)`
- `procedure INSERT_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure UPDATE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure DELETE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure LOCK_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure QUERY_PROFIT(P_RESULT IN OUT REF_PROFIT, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure QUERY_GL_TRAN_DETAIL1(P_RESULT IN OUT REF_GL_TRAN_DETAIL1, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure UPDATE_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure DELETE_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure LOCK_GL_TRAN_DETAIL1(P_RESULT IN OUT GL_TRAN_DETAIL_TAB1, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_COA_CODE IN FINANCE.GL_TRANSFER_DETAIL.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_TRANSFER_DET...`
- `procedure POST_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_INTEREST_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_INTEREST_VOUCHER_NO IN FINANCE...`
- `procedure DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VA...`
- `procedure CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_INTEREST_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_INTEREST_VOUCHER_NO IN FINANCE...`
- `function IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN DATE`
- `function IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN BOOLEAN`
- `function GENERATE_LOAN_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN VARCHAR2`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2) RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE`

### PKG_S16FRM00078

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure QUERY_LOAN_REFUND_MASTER(P_RESULT IN OUT REF_LOAN_REFUND_MASTER, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_MRNO IN PAYROLL.LOAN_REFUND_MASTER_N.MRNO%TYPE)`
- `procedure INSERT_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure UPDATE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure DELETE_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure LOCK_LOAN_REFUND_MASTER(P_RESULT IN OUT TAB_LOAN_REFUND_MASTER)`
- `procedure QUERY_LOAN_REFUND_DETAIL(P_RESULT IN OUT REF_LOAN_REFUND_DETAIL, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_DETAIL_N.REFUND_NO%TYPE, P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE)`
- `procedure UPDATE_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL)`
- `procedure LOCK_LOAN_REFUND_DETAIL(P_RESULT IN OUT TAB_LOAN_REFUND_DETAIL)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB, P_MODULE IN PAYROLL.LOAN_REFUND_MASTER_N.MODULE%TYPE)`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_TRANS_DATE IN FINANCE.GL_TRAN_MASTER.T...`
- `procedure POST_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_...`
- `procedure DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_...`
- `procedure CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MODULE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.MODULE%TYPE, P_REFUND_NO IN PAYROLL.LOAN_REFUND_MASTER_N.REFUND_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_...`
- `function IS_EXIST_IN_UNPOSTED_PAY_MONTH(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN DATE`
- `function IS_EMPLOYEE_VALIDATED(P_MRNO IN HRD.INFORMATION.MRNO%TYPE) RETURN BOOLEAN`
- `function GENERATE_REFUND_NO(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN VARCHAR2`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`

### PKG_S16FRM00080

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure QUERY_PF_TRAN_MASTER(P_RESULT IN OUT REF_PF_TRAN_MASTER, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure UPDATE_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure LOCK_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure QUERY_PF_TRAN_DETAIL(P_RESULT IN OUT REF_PF_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure UPDATE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure DELETE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure LOCK_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`

### PKG_S16FRM00085

This package will be used for the calculations of Package Billing

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_PIM(P_RESULT IN OUT PIM_REF, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_INCREMENT_CODE IN PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_CODE%TYPE, P_INCREMENT_DATE IN PAYROLL.PROCESS_INCREMENT_MASTER.INCREMENT_DATE%TYPE, P_PAYROLL_LOCATION_ID IN BILLING.CORPORATE_INVOICE_MASTER.LOCATION_ID%TYPE)`
- `procedure INSERT_PIM(P_BLOCK_DATA IN OUT PIM_TAB)`
- `procedure UPDATE_PIM(P_BLOCK_DATA IN OUT PIM_TAB)`
- `procedure DELETE_PIM(P_BLOCK_DATA IN OUT PIM_TAB)`
- `procedure LOCK_PIM(P_BLOCK_DATA IN OUT PIM_TAB)`
- `procedure QUERY_GROUP(P_RESULT IN OUT GROUP_REF, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_GROUP_TYPE IN VARCHAR2)`
- `procedure QUERY_PROCESS_MEMBERS(P_RESULT IN OUT INC_MEMBER_REF, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_PATIENT_TYPE_ID IN PAYROLL.PROCESS_MEMBERS.PATIENT_TYPE_ID%TYPE, P_DEPARTMENT_ID IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE, P_GRADE_ID IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE, P_FILTER IN VARCHAR2, P_MRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE)`
- `procedure UPDATE_PROCESS_MEMBERS(P_BLOCK_DATA IN OUT INC_MEMBER_TAB)`
- `procedure LOCK_PROCESS_MEMBERS(P_BLOCK_DATA IN OUT INC_MEMBER_TAB)`
- `procedure QUERY_TEMP_INC_DET(P_RESULT IN OUT INC_DETAIL_REF, P_PROCESS_ID IN PAYROLL.TEMP_INCREMENT_DETAIL.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE, P_AD_TYPE IN PAYROLL.DEF_AD_CONSTANT.AD_TYPE%TYPE)`
- `procedure INSERT_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB)`
- `procedure UPDATE_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB)`
- `procedure LOCK_TEMP_INC_DET(P_BLOCK_DATA IN OUT INC_DETAIL_TAB)`
- `procedure QUERY_POPULATE(P_RESULT IN OUT INC_MEMBER_TAB, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_FMRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE, P_TMRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE, P_FDEPARTMENT_ID IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE, P_TDEPARTMENT_ID IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE, P_FGRADE_ID IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE, P_TGRADE_ID ...`
- `function F_QUERY_POPULATE_APEX(P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_FMRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE, P_TMRNO IN PAYROLL.TEMP_INCREMENT_DETAIL.MRNO%TYPE, P_FDEPARTMENT_ID IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE, P_TDEPARTMENT_ID IN PAYROLL.PROCESS_MEMBERS.DEPARTMENT_ID%TYPE, P_FGRADE_ID IN PAYROLL.PROCESS_MEMBERS.GRADE_ID%TYPE, P_TGRADE_ID IN PAYROLL.PROCESS_MEMBERS.GRADE...`
- `procedure PROC_ADD_REMOVE_MEMBERS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_ADD_REM IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P...`
- `procedure PROC_ADD_REMOVE_MEMBERS_APEX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_ADD_REM IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_FMRNO IN PAYROLL.TEMP_INCR...`
- `procedure PROC_DELETE_ALL_MEMBERS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure TOGGLE_SELECT_ALL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_SELECT_ALL IN VARCHAR2, P_IS_ADMIN IN VARCHAR2, P_FILTER IN VARCHAR2, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS....`
- `procedure CHECK_CHANGE_ALLOWED(P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GET_PROPOSED_BASIC(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE) RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE`
- `function GET_PROPOSED_BASIC_PERSONAL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE) RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE`
- `function GET_PROPOSED_GROSS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN PAYROLL.PROCESS_MEMBERS.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.PROCESS_MEMBERS.MRNO%TYPE) RETURN PAYROLL.TEMP_INCREMENT_MASTER.PROPOSED_GROSS%TYPE`
- `procedure RUN_PROCESS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_CALCULATE_ALL IN BOOLEAN, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT...`
- `procedure POST_MEMBERS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure UNPOST_MEMBERS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure FINALIZE_PROCESS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure UNFINALIZE_PROCESS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure POST_INCREMENT_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P...`
- `procedure UNPOST_INCREMENT_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE, P_MRNO IN PAYROLL.EMP_INCREMENT_MASTER.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P...`
- `function CHECK_MANUAL_ENTRIES(P_PROCESS_ID IN BILLING.CORPORATE_INVOICE_MASTER.PROCESS_ID%TYPE) RETURN BOOLEAN`

### PKG_S16FRM00087

1. This Package will be used for PAYROLL LOAN PAYMENT

- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_MODULE IN PAYROLL.LOAN_PAYMENT_MASTER_N.MODULE%TYPE)`

### PKG_S16FRM00089

1. This Package will be used for PAYROLL LOAN PAYMENT

- `procedure QUERY_LOAN_PAYMENT_MASTER(P_RESULT IN OUT REF_LOAN_PAYMENT_MASTER, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER_N.LOAN_NO%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)`
- `procedure INSERT_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure UPDATE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure DELETE_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure LOCK_LOAN_PAYMENT_MASTER(P_RESULT IN OUT TAB_LOAN_PAYMENT_MASTER)`
- `procedure QUERY_LOAN_REFUND_OPENING(P_RESULT IN OUT REF_LOAN_REFUND_OPENING, P_LOAN_NO IN PAYROLL.LOAN_REFUND_OPENING.LOAN_NO%TYPE)`
- `procedure INSERT_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING)`
- `procedure UPDATE_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING)`
- `procedure DELETE_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING)`
- `procedure LOCK_LOAN_REFUND_OPENING(P_RESULT IN OUT TAB_LOAN_REFUND_OPENING)`
- `procedure POST_LOAN_PAYMENT_OPENING(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure UNPOST_LOAN_PAYMENT_OPENING(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_LOAN_NO IN PAYROLL.LOAN_PAYMENT_MASTER.LOAN_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_S16FRM00090

1. This Package will be used for LOAN PAYMENT DETAIL

- `procedure QUERY_LOANS(P_RESULT IN OUT LOAN_REF, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_MONTH IN VARCHAR2, P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.LOAN_CODE%TYPE, P_PENDING_ALL IN CHAR)`
- `procedure QUERY_LOAN_INS_DETAIL(P_RESULT IN OUT LOAN_DETAIL_REF, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_LOAN_CODE IN PAYROLL.DEF_LOAN_TYPE_CONSTANT.LOAN_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_REFUND_NO IN PAYROLL.LOAN_INSTALLMENT_DETAIL.REFUND_NO%TYPE, P_PENDING_ALL IN CHAR, P_ORDER_BY IN VAR...`
- `procedure DELETE_LOAN_INS_DETAIL(P_RESULT IN OUT LOAN_DETAIL_TAB)`
- `procedure LOCK_LOAN_INS_DETAIL(P_RESULT IN OUT LOAN_DETAIL_TAB)`
- `procedure POPULATE_CURRENT_INSTALLMENTS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.NAME%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`

### PKG_S16FRM00093

1. This Package will be used for PAYROLL JOUNAL VOUCHER VIEW

- `procedure QUERY_TRAN_MASTER(P_RESULT IN OUT REF_TRAN_MASTER, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_ENTRY_TYPE IN FINANCE.GL_PF_VOUCHER.ENTRY_TYPE%TYPE, P_LOAN_COD...`
- `procedure INSERT_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER)`
- `procedure UPDATE_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER)`
- `procedure LOCK_TRAN_MASTER(P_RESULT IN OUT TAB_TRAN_MASTER)`
- `procedure QUERY_TRAN_DETAIL(P_RESULT IN OUT REF_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure UPDATE_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure DELETE_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure LOCK_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`

### PKG_S16FRM00094

This package is used to encapsulate procedure/function(s) of CT Worksheet

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure COA_INQ_QUERY(P_RESULT IN OUT COA_INQ_QUERY_REF)`
- `function GET_REPORTING_PERIOD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN FINANCE.GL_COMPANY.REPORTING_PERIOD%TYPE`
- `procedure FETCH_YEARLY_BALANCE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_FROM_DATE IN FINANCE.PF_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE IN FINANCE.PF_FINANCIAL_YEAR.TO_DATE%TYPE, P_COA_CODE IN FINANCE.GL_COA_INQUIRY.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_COA_INQUIRY.LE...`
- `procedure POPULATE_TRANSACTIONS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN FINANCE.PF_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_FROM_DATE IN FINANCE.PF_FINANCIAL_YEAR.FROM_DATE%TYPE, P_TO_DATE IN FINANCE.PF_FINANCIAL_YEAR.TO_DATE%TYPE, P_COA_CODE IN FINANCE.GL_COA_INQUIRY.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_COA_INQUIRY.LE...`

### PKG_S16FRM00095

This package is used to view employee salary detail

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EMPLOYEE(P_RESULT IN OUT REF_EMPLOYEE_INFO, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_ORIGINAL_TEST IN CHAR)`
- `procedure QUERY_MONTHS(P_RESULT IN OUT REF_MONTHS, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_MONTH IN VARCHAR2, P_ORIGINAL_TEST IN CHAR)`
- `procedure QUERY_ALL_DED(P_RESULT IN OUT REF_ALL_DED, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_ORIGINAL_TEST IN CHAR)`
- `procedure QUERY_DAY_WISE_CAL(P_RESULT IN OUT REF_DAY_WISE_CAL, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_AD_CODE IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE, P_ORIGINAL_TEST IN CHAR)`
- `procedure QUERY_PREV_UNPAID_LEAVE(P_RESULT IN OUT REF_PREV_UNPAID_LEAVE, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_AD_CODE IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE, P_ORIGINAL_TEST IN CHAR)`
- `procedure QUERY_PREV_UNPAID_AD(P_RESULT IN OUT REF_PREV_UNPAID_AD, P_EMPLOYEE_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_AD_CODE IN PAYROLL.DEF_AD_CHART.AD_CODE%TYPE, P_DAY IN DATE, P_ORIGINAL_TEST IN CHAR)`

### PKG_S16FRM00097

This package was created for expense claim pending queue

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EXP_CLAIM_Q(P_RESULT IN OUT EXP_CLAIM_Q_REF, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_CLAIM_NO IN PAYROLL.EXPENSE_CLAIM_MASTER.CLAIM_NO%TYPE, P_MRNO IN PAYROLL.EXPENSE_CLAIM_MASTER.MRNO%TYPE)`
- `procedure EXPENSE_CLAIM_QUEUE(P_MRNO IN VARCHAR2, P_ACTING_FOR IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_PROCESS_ID IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_EVENT IN VARCHAR2, P_ASSIGNMENT_ID IN NUMBER)`

### PKG_S16FRM00099

1. This Package will be used for PF Final Settlement

- `procedure QUERY_PF_FINAL_SETTLEMENT(P_RESULT IN OUT REF_EMP, P_EMP_CODE IN REGISTRATION.PATIENT.MRNO%TYPE, P_TYPE IN PAYROLL.PF_FINAL_SETTLEMENT.TYPE%TYPE)`
- `procedure INSERT_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP)`
- `procedure UPDATE_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP)`
- `procedure LOCK_PF_FINAL_SETTLEMENT(P_RESULT IN OUT TAB_EMP)`
- `procedure QUERY_BALANCE(P_RESULT IN OUT REF_BALANCE, P_SETTLEMENT_TYPE IN PAYROLL.DEF_PAY_VOUCHER_SETUP.PAY_VOUCHER_TYPE%TYPE, P_RACK_RATE IN PAYROLL.PF_FINAL_SETTLEMENT.RACK_RATE%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_AMOUNT IN PAYROLL.PF_FINAL_SETTLEMENT.GROSS_PAYABLE%TYPE, P_MONTHS IN PAYROLL.PF_FINAL_SETTLEMENT.NO_OF_MONTHS%TYPE)`
- `function F_QUERY_BALANCE_APEX(P_SETTLEMENT_TYPE IN PAYROLL.DEF_PAY_VOUCHER_SETUP.PAY_VOUCHER_TYPE%TYPE, P_RACK_RATE IN PAYROLL.PF_FINAL_SETTLEMENT.RACK_RATE%TYPE, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_AMOUNT IN PAYROLL.PF_FINAL_SETTLEMENT.GROSS_PAYABLE%TYPE, P_MONTHS IN PAYROLL.PF_FINAL_SETTLEMENT.NO_OF_MONTHS%TYPE) RETURN TAB_BAL PIPELINED`
- `procedure QUERY_LOAN_REFUND_DETAIL(P_RESULT IN OUT REF_LOAN_REFUND_DETAIL, P_MRNO IN HRD.INFORMATION.MRNO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure QUERY_PF_TRAN_MASTER(P_RESULT IN OUT REF_PF_TRAN_MASTER, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure UPDATE_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure LOCK_PF_TRAN_MASTER(P_RESULT IN OUT TAB_PF_TRAN_MASTER)`
- `procedure QUERY_PF_TRAN_DETAIL_D(P_RESULT IN OUT REF_PF_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure QUERY_PF_TRAN_DETAIL_S(P_RESULT IN OUT REF_PF_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure UPDATE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure DELETE_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure LOCK_PF_TRAN_DETAIL(P_RESULT IN OUT PF_TRAN_DETAIL_TAB)`
- `procedure GET_VOUCHER_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PF_FINAL_SETTLEMENT IN PAYROLL.PF_FINAL_SETTLEMENT%ROWTYPE, P_DR_CR_GENERAL IN FINANCE.Gl_Voucher_Type.DR_CR_GENERAL%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_COA_CODE FINANCE.GL_VOUCHER_TYPE_DETAIL.COA_CODE%TYPE, P_LEDGER_TYPE_CODE FINANCE...`
- `procedure ADD_VOUCHER_REFERENCES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_OLD_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_NEW_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHE...`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P...`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P...`
- `procedure POST_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_YEAR_CODE IN PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYP...`
- `procedure DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_MRNO IN PAYROLL.PF_FINAL_SETTLEMENT.MRNO%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUC...`
- `procedure CANCEL_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_SERIAL_NO IN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%...`
- `function GET_SERIAL_NO(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.PF_FINAL_SETTLEMENT.MRNO%TYPE) RETURN PAYROLL.PF_FINAL_SETTLEMENT.SR_NO%TYPE`
- `function F_GET_CURRENT_YEARRETURN NUMBER`
- `function GET_LAST_RACK_RATERETURN PAYROLL.Pf_Final_Settlement.RACK_RATE%TYPE`
- `function GET_NO_OF_MONTHSRETURN PAYROLL.Pf_Final_Settlement.NO_OF_MONTHS%TYPE`
- `function GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2) RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE`
- `procedure R_PF_FINAL_SETTLEMENT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, p_rack_rate in varchar2, p_no_of_month in varchar, p_emp_code IN VARCHAR2, P_ZAKAT IN VARCHAR2, P_PROFIT_MEMBER IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_PF_SUMMARY(P_EMP_CODE REGISTRATION.PATIENT.MRNO%TYPE, P_NO_OF_MONTH NUMBER DEFAULT NULL, P_RACK_RATE NUMBER DEFAULT NULL, P_ZAKAT VARCHAR2 DEFAULT 'N', P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE) RETURN TAB_PF_SUMMARY PIPELINED`

### PKG_S16FRM00100

1. This Package will be used for PAYROLL GL VOUCHER

- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE, P_LOCATION_ID IN PAYROLL.PAY_VOUCHER.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_VOUCHER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_VOUCHER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_TRAN_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE) RETURN SYS_REFCURSOR`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function IS_PAY_VOUCHER_POSTED(P_ORGANIZATION_ID IN PAYROLL.DEF_AD_SETUP.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN PAYROLL.DEF_AD_SETUP.LOCATION_ID%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.DEF_PAY_VOUCHER_TYPE.PAY_VOUCHER_TYPE%TYPE) RETURN CHAR`
- `procedure GET_VOUCHER_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.END_DATE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_RESULT OUT SYS_...`
- `procedure ADD_VOUCHER_REFERENCES(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_OLD_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_NEW_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_PAY_START_DATE IN DEFINITIONS.MONTHS.START_DATE%TYPE, P_PAY_END_DATE IN DEFINITIONS.MONTHS.EN...`
- `procedure DELETE_TEMP_VOUCHER(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure GENERATE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER....`
- `procedure CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER....`
- `procedure CANCEL_PAY_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER....`
- `procedure POST_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAY_VOUCHER_TYPE IN PAYROLL.PAY_VOUCHER.PAY_VOUCHER_TYPE%TYPE, P_PAY_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_PAY_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER....`
- `function GET_VOUCHER_SERIAL_NO(P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE) RETURN NUMBER`

### PKG_S16FRM00101

Base Package of S16FRM00101 - DEF_BATCH CR Id: To be entered JIRA Ticket: To be entered

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EMP_EXP(P_RESULT IN OUT EMP_EXP_REF, P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE)`
- `procedure INSERT_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB)`
- `procedure UPDATE_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB)`
- `procedure DELETE_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB)`
- `procedure LOCK_EMP_EXP(P_BLOCK_DATA IN OUT EMP_EXP_TAB)`
- `procedure QUERY_EMP_EXP_DTL(P_RESULT IN OUT EMP_EXP_DTL_REF, P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST_DTL.EXPENSE_LIST_ID%TYPE, P_MRNO IN PAYROLL.EMP_EXPENSE_LIST_DTL.MRNO%TYPE, P_QUERY IN CHAR)`
- `procedure INSERT_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB)`
- `procedure UPDATE_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB)`
- `procedure DELETE_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB)`
- `procedure LOCK_EMP_EXP_DTL(P_BLOCK_DATA IN OUT EMP_EXP_DTL_TAB)`
- `procedure POST_EXPENSE_LIST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_EXPENSE_LIST_ID IN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `function GEN_EXPENSE_LIST_ID(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_TRAN_DATE IN DATE, P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN PAYROLL.EMP_EXPENSE_LIST.EXPENSE_LIST_ID%TYPE`

### PKG_S16FRM00102

1. This Package will be used for Employee tax calculation comparison

- `procedure QUERY_TAX(P_RESULT IN OUT TAX_REF, P_MONTH_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)`
- `function F_QUERY_TAX_APEX(P_MONTH_START_DATE IN PAYROLL.PAY_STATUS.DATE_FROM%TYPE, P_MONTH_END_DATE IN PAYROLL.PAY_STATUS.DATE_TO%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN TAB_TAX PIPELINED`
- `procedure QUERY_DEPARTMENT(P_RESULT IN OUT DEP_REF, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_CRITERIA_ID IN NUMBER, P_DIFFERENCE IN CHAR, P_ORDER_BY IN VARCHAR2)`
- `function F_QUERY_DEPARTMENT_APEX(P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_DEPARTMENT IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_CRITERIA_ID IN NUMBER, P_DIFFERENCE IN CHAR, P_ORDER_BY IN VARCHAR2) RETURN DEP_TAB_APEX PIPELINED`
- `procedure QUERY_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_REF, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_CRITERIA_ID IN NUMBER, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_DIFFERENCE IN CHAR, P_ORDER_BY IN VARCHAR2)`
- `function F_QUERY_ITAX_DETAIL_APEX(P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE, P_CRITERIA_ID IN NUMBER, P_DIFFERENCE IN CHAR, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ORDER_BY IN VARCHAR2) RETURN DEP_ITAX_APEX PIPELINED`
- `procedure POPULATE_DATA(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CSTART_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_CEND_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TERMINAL IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE, P_ALERT_TEXT OUT VARCHAR2...`
- `function GET_PREV_MONTH_TOTAL(P_START_DATE IN DATE, P_END_DATE IN DATE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CRITERIA_ID IN NUMBER) RETURN NUMBER`
- `function GET_CURR_MONTH_TOTAL(P_START_DATE IN DATE, P_END_DATE IN DATE, P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_CRITERIA_ID IN NUMBER) RETURN NUMBER`

### PKG_S16FRM00103

1. This Package will be used for

- `procedure QUERY_MONTH(P_RESULT IN OUT MONTH_REF, P_MONTH_START_DATE IN DEFINITIONS.Location_Wise_Months.MON_START_DATE%TYPE, P_MONTH_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.MON_END_DATE%TYPE)`
- `procedure QUERY_EMP_DETAIL(P_RESULT IN OUT EMP_DETAIL_REF, P_PAYROLL_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ITAX_DETAIL.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ITAX_DETAIL.END_DATE%TYPE, P_PAYMENT_MODE IN PAYROLL.PAY_MASTER.PAYMENT_MODE%TYPE, P_CRITERIA IN NUMBER, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ORDER_BY IN VARCHAR2)`
- `procedure QUERY_GL_TRAN_MASTER(P_RESULT IN OUT REF_GL_TRAN_MASTER, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE, P_PAYMENT_MODE IN CHAR, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure UPDATE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure DELETE_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure LOCK_GL_TRAN_MASTER(P_RESULT IN OUT TAB_GL_TRAN_MASTER)`
- `procedure QUERY_GL_TRAN_DETAIL(P_RESULT IN OUT REF_GL_TRAN_DETAIL, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE)`
- `procedure INSERT_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure UPDATE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure DELETE_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure LOCK_GL_TRAN_DETAIL(P_RESULT IN OUT GL_TRAN_DETAIL_TAB)`
- `procedure GENERATE_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_PAYMENT_MODE IN CHAR, P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_EXPENSE_CODE IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE, P_TRANS_DATE ...`
- `procedure POST_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.PF_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.PF_TRAN_MASTER.VOUCHER_NO%TYPE, P_START_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_START_DATE%TYPE, P_END_DATE IN DEFINITIONS.LOCATION_WISE_MONTHS.PAY_END_DATE%TYPE, P_MRNO IN REGISTRATI...`
- `procedure DELETE_TEMP_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CANCEL_POSTED_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_NEW_VOUCHER_TYPE OUT FINANCE.GL_TRAN_MASTER.V...`
- `procedure CANCEL_VOUCHER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_VOUCHER_TYPE IN FINANCE.GL_TRAN_MASTER.VOUCHER_TYPE%TYPE, P_VOUCHER_NO IN FINANCE.GL_TRAN_MASTER.VOUCHER_NO%TYPE, P_LOGIN_LOCATION_ID IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_NEW_VOUCHER_TYPE OUT FINANCE.GL_TRAN_MASTER.V...`
- `procedure INIT_GL_OPENING_BALANCE(P_COA_CODE IN FINANCE.GL_OPENING_BALANCES.COA_CODE%TYPE, P_LEDGER_TYPE_CODE IN FINANCE.GL_OPENING_BALANCES.LEDGER_TYPE_CODE%TYPE, P_SUB_LDGR_ITEM_CODE IN FINANCE.GL_OPENING_BALANCES.SUB_LDGR_ITEM_CODE%TYPE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT CHAR)`
- `procedure CHECK_ACTIVE_MONTH(P_USER_ID IN FINANCE.GL_MONTH_USERS.USERID%TYPE, P_TRAN_DATE IN DATE, P_ALERT_TEXT OUT VARCHAR2, P_STOP OUT VARCHAR2)`
- `function GET_REF_REQUIRED(P_VOUCHER_TYPE IN VARCHAR2) RETURN FINANCE.GL_VOUCHER_TYPE.REF_REQUIRED%TYPE`
- `procedure UPDATE_VOUCHER_REFERENCE(P_VOUCHER_NO IN CHAR, P_VOUCHER_TYPE IN CHAR, P_NEW_VOUCHER_NO IN CHAR, P_OBJECT_CODE IN CHAR, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_S16FRM00104

1. This Package will be used for PF Final Settlement

- `procedure QUERY_EMP_ITAX(P_RESULT IN OUT REF_EMP, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.DEF_ITAX_ADJUSTMENT.ADJUSTMENT_CODE%TYPE)`
- `procedure INSERT_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure UPDATE_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure DELETE_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure LOCK_ITAX(P_RESULT IN OUT TAB_EMP)`
- `procedure QUERY_ITAX_DETAIL(P_RESULT IN OUT REF_ITAX_DETAIL, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE)`
- `procedure INSERT_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure UPDATE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure DELETE_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure LOCK_ITAX_DETAIL(P_RESULT IN OUT ITAX_DETAIL_TAB)`
- `procedure CALCULATE_EXEMPTED_TAX(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE, P_OBJECT_CODE IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_USER_MRNO IN VARCHAR2, P_CURRENT_...`
- `procedure POST_UNPOST(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_POST_UNPOST IN CHAR, P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.YEAR_CODE%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_ADJUSTMENT_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT_DTL.ADJUSTMENT_CODE%TYPE, P_CURRENT_INCOME IN NUMBER, P_CURRENT_TAX IN NUMBER, P_OBJECT_C...`

### PKG_S16FRM00106

This package is used to encapsulate procedure/function(s) of Emp Awards - S16FRM00106

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure QUERY_EMP_AWARDS(P_RESULT IN OUT REF_EMP_AWARD, P_AWARD_ID IN PAYROLL.EMP_AWARDS.AWARD_ID%TYPE, P_PAY_START_DATE IN DATE, P_PAY_END_DATE IN DATE, P_EXPENSE_CODE IN PAYROLL.DEF_EXPENSE.EXPENSE_CODE%TYPE)`
- `procedure QUERY_EMP_AWARD_PAY(P_RESULT IN OUT REF_EMP_AWARD_PAY, P_PAYMENT_ID IN PAYROLL.EMP_AWARD_PAYMENT.PAYMENT_ID%TYPE, P_AWARD_ID IN PAYROLL.EMP_AWARD_PAYMENT.AWARD_ID%TYPE)`

### PKG_S16REP00003

- `function GET_NET_SALARY_REG_TOT(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_EXP_TOT(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_CONS_TOT(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_LOCUM_TOT(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_REG_B(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_REG_C(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_REG_Q(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_EXP_B(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_EXP_C(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_EXP_Q(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_CONS_B(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_CONS_C(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_CONS_Q(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_LOCUM_B(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_LOCUM_C(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`
- `function GET_NET_SALARY_LOCUM_Q(P_ORGANIZATION_ID IN VARCHAR2, P_LOCATION_ID IN VARCHAR2, P_START_DATE IN DATE, P_END_DATE IN DATE, P_ORIGINAL_TEST IN VARCHAR2) RETURN NUMBER`

### PKG_S16REP00079

- `function GET_FS_OTHER_SALARY(P_YEAR_CODE PAYROLL.PAY_FINANCIAL_YEAR.YEAR_CODE%TYPE, P_MRNO PAYROLL.EMP_EXPENSE.MRNO%TYPE, P_TYPE VARCHAR2) RETURN NUMBER`

### PKG_S16REP00096

- `function PAY_CONSULTANT_TAX(P_ORIGINAL_TEST IN VARCHAR2, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN DATE, P_END_DATE IN DATE) RETURN DATA_TAB PIPELINED`

### PKG_S16REP00110

- `function GET_EMP_SAL_CHANGE_NEW(P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_FROM_DATE IN PAYROLL.CHANGE_SALARY_ALLOW.CHANGE_DATE%TYPE, P_TO_DATE IN PAYROLL.CHANGE_SALARY_ALLOW.CHANGE_DATE%TYPE, P_TERMINAL IN VARCHAR2, P_CALLING_OBJECT IN VARCHAR2, P_CALLING_USER IN VARCHAR2, P_CALLING_EVENT IN VARCHAR2) RETURN PAYROLL.PKG_S16REP00110.CHANGE_SAL_ALLOW_TAB PIPELINED`

### PKG_S16REP00114

- `function EMP_ITAX_ADJUSTMENT(P_YEAR_CODE IN PAYROLL.EMP_ITAX_ADJUSTMENT.YEAR_CODE%TYPE) RETURN ITAX_ADJUSTMENT_REC_TAB PIPELINED`

### PKG_S16REP00115

This package was created for EMPLOYEES NOT IN PAYROLL Report

- `function GET_MISSING_EMP_SAL(P_MONTH DEFINITIONS.MONTHS.MONTH%TYPE, P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAY_TAB PIPELINED`

### PKG_S16REP00116

- `function PAY_SLIP_DETAIL(P_ORIGINAL_TEST IN VARCHAR2, P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PATIENT_TYPE_ID IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE, P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE, P_FROM_GRA...`
- `function GET_AD_VALUE(P_FIELD_CODE IN VARCHAR2, P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE) RETURN NUMBER`
- `function GET_OTHER_AD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE, P_AD_TYPE IN VARCHAR2) RETURN NUMBER`
- `function GET_TOTAL_DEDUCTIONS(P_MRNO IN PAYROLL.PAY_MASTER.MRNO%TYPE) RETURN NUMBER`
- `function GET_PROMPT(P_FIELD_CODE IN VARCHAR2) RETURN VARCHAR2`
- `function COLUMN_HEADING(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE) RETURN PAYROLL.PKG_S16REP00116.DISPLAY_TEXT_TAB PIPELINED`
- `procedure FETCH_REPORT_FIELDS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)`

### PKG_S16REP00118

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_ITAX_MASTER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN VARCHAR2, P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN ITAX_MASTER_TAB PIPELINED`
- `function GET_ITAX_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_YEAR_CODE IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN ITAX_DETAIL_TAB PIPELINED`

### PKG_S16REP00119

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_AD_CODE_WISE_SUMMARY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE, P_FROM_GRADE_ID IN DEFINITIONS.GRADES.GRADE_ID...`

### PKG_S16REP00120

- `function GET_AD_CODE_WISE_DETAIL(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_GROUP_BY VARCHAR2, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_AD_CODE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.AD_CODE%TYPE, P_PGROUP_ID IN DEFINITIONS.PATIENT_TY...`

### PKG_S16REP00122

THIS PACKAGE WILL BE USED FOR THE FOLLOWING PURPOSE

- `function GET_VERSIONRETURN VARCHAR2`
- `function GET_PAY_MASTER(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_FROM_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_TO_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_MASTER.START...`
- `function GET_PAY_ALLOWANCES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_ALLOWANCES_TAB PIPELINED`
- `function GET_PAY_DEDUCTIONS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_DEDUCTIONS_TAB PIPELINED`
- `function GET_PAY_LEAVES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_LEAVES_TAB PIPELINED`
- `function GET_PAY_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_LOAN_REFUND_TAB PIPELINED`
- `function GET_PRACTICE_INCOME(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PRACTICE_INCOME_TAB PIPELINED`
- `function GET_PAY_YEAR_TO_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_YEAR_TO_DATE_TAB PIPELINED`
- `function GET_PAY_YEAR_TO_DATE_PI(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_YEAR_TO_DATE_PI_TAB PIPELINED`
- `function GET_PAY_ALL_YEAR_TO_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_ALL_YEAR_TO_DATE_TAB PIPELINED`
- `function GET_PAY_DED_YEAR_TO_DATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_DED_YEAR_TO_DATE_TAB PIPELINED`
- `function GET_PAY_LOAN_REFUND_YT(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_LOAN_REFUND_YT_TAB PIPELINED`
- `function GET_PAY_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_ARREARS_TAB PIPELINED`
- `function GET_DED_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.DED_ARREARS_TAB PIPELINED`
- `function GET_PAY_AD_BALANCE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PKG_S16REP00122.PAY_AD_BALANCE_TAB PIPELINED`
- `function GET_TOTAL_EMP_ALLOWANCE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_EMP_DEDUCTION(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_LEAVES(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE, P_LEAVE_TYPE IN CHAR) RETURN NUMBER`
- `function GET_TOTAL_PAY_LOAN_REFUND(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PRACTICE_INCOME(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_YD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE, P_PAY_YD_TYPE IN VARCHAR2) RETURN NUMBER`
- `function GET_TOTAL_PAY_YD_PI(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_ALL_YD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_DED_YD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_LOAN_REF_YD(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_YEAR_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_DED_ARREARS(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_TOTAL_PAY_AD_BALANCE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN NUMBER`
- `function GET_NATIONALITY(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE) RETURN HRD.V_INFORMATION.NATIONALITY%TYPE`
- `function GET_EXCHANGE_RATE(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_ORIGINAL_TEST IN VARCHAR2, P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.START_DATE%TYPE, P_END_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION.END_DATE%TYPE) RETURN PAYROLL.PAY_MASTER_TEST.CURRENCY_EXCHANGE_RATE%TYPE`

### PKG_S16REP00130

- `function GET_ITAX_DETAIL(P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN PAY_ITAX_TAB PIPELINED`
- `function GET_ITAX_DETAIL_TEST(P_MRNO IN VARCHAR2, P_YEAR_CODE IN VARCHAR2, P_MONTH IN DEFINITIONS.LOCATION_WISE_MONTHS.MONTH%TYPE) RETURN PAY_ITAX_TAB PIPELINED`
- `function GET_INCOME_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_INCOME_DET_TAB PIPELINED`
- `function GET_PAID_SALARY(P_MRNO IN VARCHAR2, P_FROM_DATE IN PAYROLL.PAY_MASTER.START_DATE%TYPE, P_TO_DATE IN PAYROLL.PAY_MASTER.END_DATE%TYPE) RETURN PAY_TAB PIPELINED`
- `function GET_EXP_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_EXP_DET_TAB PIPELINED`
- `function GET_TAX_ADJ_DETAIL(P_MRNO IN VARCHAR2) RETURN PAY_TAX_ADJ_TAB PIPELINED`

### PKG_SALARY_RECONCILIATION

- `function SALARY_RECONCILIATION(P_PREV_START DATE, P_PREV_END DATE, P_CURR_START DATE, P_CURR_END DATE, P_LOCATION_ID VARCHAR2, P_ORGANIZATION_ID VARCHAR2) RETURN SAL_RECON_TAB PIPELINED`
- `function EMP_GROSS(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function JGROSS(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE, P_PREV_START DATE, P_PREV_END DATE) RETURN NUMBER`
- `function LGROSS(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE, P_PREV_START DATE, P_PREV_END DATE) RETURN NUMBER`
- `function EMP_ALLOW(P_AD_CODE CHAR, P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function NSHIFT(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function OVERTIME(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function ARREAR(P_MRNO CHAR, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function EMPLOYEENO(P_MRNO VARCHAR2, P_START_DATE DATE, P_END_DATE DATE) RETURN NUMBER`
- `function DEPARTMENT(P_MRNO VARCHAR2, P_START_DATE DATE, P_END_DATE DATE) RETURN VARCHAR2`
- `function DEPARTMENT_LEAVER(P_MRNO VARCHAR2, P_START_DATE DATE, P_END_DATE DATE) RETURN VARCHAR2`
- `function DESIGNATION(P_MRNO VARCHAR2) RETURN VARCHAR2`
- `function DEPT_JOINER(P_DEPT VARCHAR2, P_PREV_START DATE, P_PREV_END DATE, P_START_DATE DATE, P_END_DATE DATE, P_LOCATION_ID VARCHAR2, P_ORGANIZATION_ID VARCHAR2) RETURN NUMBER`
- `function DEPT_LEAVER(P_DEPT VARCHAR2, P_PREV_START DATE, P_PREV_END DATE, P_START_DATE DATE, P_END_DATE DATE, P_LOCATION_ID VARCHAR2, P_ORGANIZATION_ID VARCHAR2) RETURN NUMBER`
- `procedure P_GET_PAYROLL_MONTH(P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_EVENT IN CHAR, P_START_DATE OUT DATE, P_END_DATE OUT DATE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `procedure P_SALARY_RECONCILIATION_INSERT(P_CURRENT_START_DATE IN DATE, P_PRE_START_DATE IN DATE, P_MRNO IN VARCHAR2)`
- `procedure P_SALARY_RECONCILIATION(P_FROM_DATE IN DATE, P_TO_DATE IN DATE, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`

### PKG_SALARY_SLIP_EMPLOYEE

- `function GET_TAXABLE_INCOME(P_MRNO IN VARCHAR2, P_START_DATE IN DATE) RETURN NUMBER`
- `function GET_TAX_SLAB(P_MRNO IN VARCHAR2, P_START_DATE IN DATE) RETURN NUMBER`
- `function GET_TAX_CHARGEABLE(P_MRNO IN VARCHAR2, P_START_DATE IN DATE) RETURN NUMBER`
- `function GET_TAX_CREDIT_ADJ(P_ORGANIZATION_ID IN VARCHAR2, P_LOGIN_LOCATION_ID IN VARCHAR2, P_MRNO IN VARCHAR2, P_START_DATE IN DATE, P_YEARLY_TAX IN VARCHAR2) RETURN NUMBER`
- `function GET_TAX_DEDUCTED(P_MRNO IN VARCHAR2, P_START_DATE IN DATE) RETURN NUMBER`
- `function GET_TAX_PAYABLE(P_ORGANIZATION_ID IN VARCHAR2, P_LOGIN_LOCATION_ID IN VARCHAR2, P_MRNO IN VARCHAR2, P_START_DATE IN DATE, P_YEARLY_TAX IN VARCHAR2) RETURN NUMBER`
- `function GET_EMPLOYEE_CONTRIBUTION_OP(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_EMPLOYEE_CONTRIBUTION(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_EMPLOYER_CONTRIBUTION_OP(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_EMPLOYER_CONTRIBUTION(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_EMPLOYEE_PROFIT(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_SKMT_PROFIT(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_PERMANENT_WITHDRAWAL(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_TOTAL_PROVIDENT_FUND(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`
- `function GET_CURRENT_MONTH_PF(P_MRNO IN VARCHAR2, P_END_DATE IN DATE) RETURN NUMBER`

### PKG_YEAR_CLOSING

This package will be used for the following purpose

- `function GET_VERSIONRETURN VARCHAR2`
- `procedure PROCESS_PF_YEAR_CLOSING(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE, P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE, P_FILE_NO IN FINANCE.GL_COA_FILES.COA_FILE_NO%TYPE, P_OPENING_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_CLOSING_YEAR_CODE IN FINANCE.GL_PF_VOUCHER.YEAR_CODE%TYPE, P_USER_MRNO IN VARCHAR2, P_TERMINAL IN VARCHAR2, P_OBJECT_CODE IN VARCHAR2, P_ALERT_TEXT OUT...`

### SALARY_DASHBOARD

- `procedure BUILD_SALARY_TAX_MATRIX(p_mrno IN VARCHAR2, p_tax_year IN NUMBER, p_alert_text out varchar2, p_stop out char)`
- `procedure PRC_LOAD_SALARY_TAX_LINE_ITEM( p_alert_text OUT VARCHAR2, p_stop OUT VARCHAR2 )`

## Standalone Procedures

- `LFA_AMOUNT(P_MRNO IN CHAR, P_LFA_DUE_DATE IN DATE, P_GROSS OUT NUMBER, P_BASIC OUT NUMBER, P_LFA_AMOUNT OUT NUMBER, P_PREV_YEAR_START OUT DATE, P_PREV_YEAR_END OUT DATE, P_PREV_LEAVE_START OUT DATE, P_PREV_LEAVE_END OUT DATE, P_PREV_VOUCHER_TYPE OUT CHAR, P_PREV_VOUCHER_NO OUT CHAR, P_PREV_GROSS OUT NUMBER, P_PREV_BASIC OUT NUMBER, P_PREV_LFA_AMOUNT OUT NUMBER, P_PREV_TRANS_DATE OUT DATE) AUTHID CURRENT_...`
- `ACTIVATE( P_REQUEST_ID IN PAYROLL.CONNECTION_REQUEST.REQUEST_ID%TYPE, P_ISSUE_TO OUT VARCHAR2, P_ISSUE_DATE OUT DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2 )`
- `ANNUAL_ITAX(P_FROM_DATE DATE, P_TO_DATE DATE, P_USERID CHAR, P_TERMINAL CHAR)`
- `BUILD_SALARY_TAX_MATRIX(p_mrno IN VARCHAR2, p_tax_year IN NUMBER, p_alert_text out varchar2, p_stop out char)`
- `CM_ACTIVATE( P_REQUEST_ID IN PAYROLL.CONNECTION_REQUEST.REQUEST_ID%TYPE, P_ISSUE_TO OUT VARCHAR2, P_ISSUE_DATE OUT DATE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2 )`
- `COST_TO_COMPANY_JOB`
- `DBJOB`
- `DELETE_AD_END_DATE`
- `EMERGENCY`
- `EMP_AD_UPDATION(P_MRNO VARCHAR2, P_INC_DATE DATE, P_CURRENT_BASIC NUMBER, P_CURRENT_GROSS NUMBER, P_PREVIOUS_GROSS NUMBER, P_PREVIOUS_BASIC NUMBER, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `EMP_INCREMENT_MASTER_UPDATION(P_MRNO VARCHAR2, P_INC_DATE DATE, P_EFFECTIVE_DATE DATE, P_PROPOSAL_NO NUMBER, P_YEAR_CODE VARCHAR2, P_INCREMENT_CODE VARCHAR2, P_STOP OUT CHAR, P_ALERT_TEXT OUT VARCHAR2)`
- `GL_RECONCILE_LOAN`
- `INACTIVATE( P_CONNECTION_ID IN PAYROLL.DEF_CONNECTION.CONNECTION_ID%TYPE, P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2 )`
- `INDIVIDUAL_ITAX(P_MRNO CHAR, P_YEAR_CODE CHAR, P_USER CHAR, P_TERMINAL CHAR)`
- `LFA_DETAIL(p_mrno IN CHAR, p_lfa_due_date IN DATE, p_payment_date OUT DATE, p_gross OUT NUMBER, p_basic OUT NUMBER, p_lfa_amount OUT NUMBER)`
- `MPA_REPORTS(P_START_DATE0 IN DATE, P_END_DATE0 IN DATE, P_START_DATE1 IN DATE, P_END_DATE1 IN DATE, P_START_DATE2 IN DATE, P_END_DATE2 IN DATE, P_START_DATE3 IN DATE, P_END_DATE3 IN DATE, P_USER_ID IN CHAR, P_TERMINAL IN CHAR)`
- `MPA_REPORTS_2MONTHS(P_START_DATE2 IN DATE, P_END_DATE2 IN DATE, P_START_DATE3 IN DATE, P_END_DATE3 IN DATE, P_USER_ID IN CHAR, P_TERMINAL IN CHAR)`
- `NEXT_MONTH_TAX_DETAIL(P_YEAR_CODE IN NUMBER, P_MRNO IN VARCHAR2, P_YEAR_TAX IN NUMBER, P_NEXT_MONTH_TAX OUT NUMBER, P_PAID_TAX OUT NUMBER)`
- `PROC_PAYROLL_JOB`
- `SALARY_SHEET(p_start_date DATE, p_end_date DATE, p_user CHAR, p_terminal CHAR, p_location_id varchar2, p_organization_id varchar2)`
- `SALARY_SHEET_OLD(p_start_date DATE,p_end_date DATE, p_user CHAR,p_terminal CHAR)`
- `SALARY_SHEET_TEST(P_START_DATE DATE, P_END_DATE DATE, P_USER CHAR, P_TERMINAL CHAR, P_ORGANIZATION_ID VARCHAR2, P_LOCATION_ID VARCHAR2)`
- `SALARY_WISE_GRADE_CHANGE`

## Standalone Functions

- `CALC_GM(P_MRNO VARCHAR2) RETURN NUMBER`
- `CURRENT_BASIC(P_MRNO VARCHAR2, P_DATE DATE) RETURN NUMBER AUTHID CURRENT_USER`
- `CURRENT_GROSS(P_MRNO VARCHAR2, P_DATE DATE) RETURN NUMBER AUTHID CURRENT_USER`
- `ERROR_HANDLING(P_ERROR IN APEX_ERROR.T_ERROR) RETURN APEX_ERROR.T_ERROR_RESULT`
- `F_EMPLOYEE_GROSS(P_MRNO CHAR) RETURN NUMBER AUTHID CURRENT_USER`
- `F_GET_CAR_ALLOWANCE_MONTH( P_MRNO IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE, P_START_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE ) RETURN NUMBER`
- `F_GET_CAR_ALLOWANCE_YEAR( P_MRNO IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.MRNO%TYPE, P_START_YEAR_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.START_DATE%TYPE, P_END_YEAR_DATE IN PAYROLL.PAY_ALLOWANCE_DEDUCTION_TEST.END_DATE%TYPE ) RETURN NUMBER`
- `F_GET_EMP_OTHER_TAXABLE_AMOUNT(P_MRNO IN VARCHAR2, P_YEAR IN VARCHAR2, P_TAXABLE_AMOUNT_TYPE_ID IN VARCHAR2) RETURN NUMBER`
- `F_GET_URL(p_value IN VARCHAR2) RETURN VARCHAR2`
- `GET_EXPENSE_DESC(P_EXPENSE_CODE IN VARCHAR2, P_LEVEL IN VARCHAR2, P_ALERT_TEXT OUT VARCHAR2) RETURN VARCHAR2`
- `LFA_ADJUSTMENT_AMOUNT(P_MRNO VARCHAR2, P_LFA_DUE_DATE DATE) RETURN NUMBER`
- `LFA_AMOUNT_FUN(P_MRNO CHAR, P_LFA_DUE_DATE DATE) RETURN NUMBER`
- `LFA_AMOUNT_YEAR(P_MRNO CHAR, P_YEAR_CODE NUMBER) RETURN NUMBER`
- `LFA_PAID_AMOUNT_GL(P_MRNO IN CHAR, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `LFA_PAID_AMOUNT_SALARY(P_MRNO IN CHAR, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `LFA_PAID_AMOUNT(P_MRNO IN CHAR, P_FROM_DATE IN DATE, P_TO_DATE IN DATE) RETURN NUMBER`
- `LSB_AMOUNT(P_MRNO VARCHAR2, P_EXPENSE_CODE NUMBER) RETURN NUMBER`
- `NEXT_MONTH_TAX(P_YEAR_CODE NUMBER, P_MRNO VARCHAR2, P_YEAR_TAX NUMBER) RETURN NUMBER`
- `PF_CALCULATION(P_GROSS_SALARY IN CHAR) RETURN NUMBER`
- `TAXABLE_PAY(P_YEAR_CODE NUMBER, P_MRNO VARCHAR2) RETURN NUMBER`
- `SETUP_TAX_CALCULATION(P_YEAR_CODE NUMBER, P_MRNO CHAR) RETURN NUMBER`
- `TAX_CALCULATION(P_YEAR_CODE NUMBER, P_AMOUNT NUMBER, P_GENDER CHAR) RETURN NUMBER`
- `TAX_DIRECT_PAID_EXP(P_YEAR_CODE NUMBER, P_FROM_DATE DATE, P_TO_DATE DATE, P_MRNO VARCHAR2) RETURN NUMBER`
- `TAX_SLAB(P_YEAR_CODE NUMBER, P_AMOUNT NUMBER, P_GENDER CHAR) RETURN NUMBER`
- `YEARLY_TAXABLE_PF(p_year_code NUMBER, p_mrno VARCHAR2) RETURN NUMBER`
- `YEARLY_PF_EXEMPTION(p_year_code NUMBER, p_mrno VARCHAR2) RETURN NUMBER`
- `YEARLY_TAXABLE_PAY(P_YEAR_CODE NUMBER, P_MRNO VARCHAR2) RETURN NUMBER`
- `YEARLY_TAXABLE_PF_TEST(p_year_code NUMBER, p_mrno VARCHAR2) RETURN NUMBER`
- `YEARLY_TAXABLE_PAY_TEST(P_YEAR_CODE NUMBER, P_MRNO VARCHAR2) RETURN NUMBER`

## Triggers

| Trigger | Table | Event | Row-level |
|---|---|---|---|
| ALLOWANCE_DEDUCTION_DETAIL_DEL | ALLOWANCE_DEDUCTION_DETAIL | AFTER DELETE | Y |
| ALLOWANCE_DEDUCTION_DETAIL_INS | ALLOWANCE_DEDUCTION_DETAIL | BEFORE INSERT | Y |
| ALLOWANCE_DEDUCTION_DETAIL_UPD | ALLOWANCE_DEDUCTION_DETAIL | BEFORE UPDATE | Y |
| ARREAR_DETAIL_DEL | ARREAR_DETAIL | AFTER DELETE | Y |
| ARREAR_DETAIL_INS | ARREAR_DETAIL | BEFORE INSERT | Y |
| ARREAR_DETAIL_UPD | ARREAR_DETAIL | BEFORE UPDATE | Y |
| ARREAR_EXCEPTIONAL_DEL | ARREAR_EXCEPTIONAL | AFTER DELETE | Y |
| ARREAR_EXCEPTIONAL_INS | ARREAR_EXCEPTIONAL | BEFORE INSERT | Y |
| ARREAR_EXCEPTIONAL_UPD | ARREAR_EXCEPTIONAL | BEFORE UPDATE | Y |
| CM_BILL_DETAIL_DEL | CM_BILL_DETAIL | AFTER DELETE | Y |
| CM_BILL_DETAIL_INS | CM_BILL_DETAIL | BEFORE INSERT | Y |
| CM_BILL_DETAIL_UPD | CM_BILL_DETAIL | BEFORE UPDATE | Y |
| CM_BILL_MASTER_DEL | CM_BILL_MASTER | AFTER DELETE | Y |
| CM_BILL_MASTER_INS | CM_BILL_MASTER | BEFORE INSERT | Y |
| CM_BILL_MASTER_UPD | CM_BILL_MASTER | BEFORE UPDATE | Y |
| CM_CONNECTION_REQUEST_DEL | CM_CONNECTION_REQUEST | AFTER DELETE | Y |
| CM_CONNECTION_REQUEST_INS | CM_CONNECTION_REQUEST | BEFORE INSERT | Y |
| CM_CONNECTION_REQUEST_UPD | CM_CONNECTION_REQUEST | BEFORE UPDATE | Y |
| CM_CONNECTION_REQ_DOCUMENT_DEL | CM_CONNECTION_REQ_DOCUMENT | AFTER DELETE | Y |
| CM_CONNECTION_REQ_DOCUMENT_INS | CM_CONNECTION_REQ_DOCUMENT | BEFORE INSERT | Y |
| CM_CONNECTION_REQ_DOCUMENT_UPD | CM_CONNECTION_REQ_DOCUMENT | BEFORE UPDATE | Y |
| CM_CONNECTION_TRANSACTIONS_DEL | CM_CONNECTION_TRANSACTIONS | AFTER DELETE | Y |
| CM_CONNECTION_TRANSACTIONS_INS | CM_CONNECTION_TRANSACTIONS | BEFORE INSERT | Y |
| CM_CONNECTION_TRANSACTIONS_UPD | CM_CONNECTION_TRANSACTIONS | BEFORE UPDATE | Y |
| CM_DEF_ADMIN_GROUP_DEL | CM_DEF_ADMIN_GROUP | AFTER DELETE | Y |
| CM_DEF_ADMIN_GROUP_DTL_DEL | CM_DEF_ADMIN_GROUP_DTL | AFTER DELETE | Y |
| CM_DEF_ADMIN_GROUP_DTL_INS | CM_DEF_ADMIN_GROUP_DTL | BEFORE INSERT | Y |
| CM_DEF_ADMIN_GROUP_DTL_UPD | CM_DEF_ADMIN_GROUP_DTL | BEFORE UPDATE | Y |
| CM_DEF_ADMIN_GROUP_INS | CM_DEF_ADMIN_GROUP | BEFORE INSERT | Y |
| CM_DEF_ADMIN_GROUP_UPD | CM_DEF_ADMIN_GROUP | BEFORE UPDATE | Y |
| CM_DEF_CONNECTION_DEL | CM_DEF_CONNECTION | AFTER DELETE | Y |
| CM_DEF_CONNECTION_INS | CM_DEF_CONNECTION | BEFORE INSERT | Y |
| CM_DEF_CONNECTION_UPD | CM_DEF_CONNECTION | BEFORE UPDATE | Y |
| CM_INVOICES_DEL | CM_INVOICES | AFTER DELETE | Y |
| CM_INVOICES_INS | CM_INVOICES | BEFORE INSERT | Y |
| CM_INVOICES_UPD | CM_INVOICES | BEFORE UPDATE | Y |
| DEF_AD_CHART_CEA | DEF_AD_CHART | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_CHART_DEL | DEF_AD_CHART | AFTER DELETE | Y |
| DEF_AD_CHART_DETAIL_CEA | DEF_AD_CHART_DETAIL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_CHART_DETAIL_DEL | DEF_AD_CHART_DETAIL | AFTER DELETE | Y |
| DEF_AD_CHART_DETAIL_INS | DEF_AD_CHART_DETAIL | BEFORE INSERT | Y |
| DEF_AD_CHART_DETAIL_UPD | DEF_AD_CHART_DETAIL | BEFORE UPDATE | Y |
| DEF_AD_CHART_INS | DEF_AD_CHART | BEFORE INSERT | Y |
| DEF_AD_CHART_PK | DEF_AD_CHART | BEFORE INSERT | Y |
| DEF_AD_CHART_UPD | DEF_AD_CHART | BEFORE UPDATE | Y |
| DEF_AD_CONSTANT_CEA | DEF_AD_CONSTANT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_CONSTANT_DEL | DEF_AD_CONSTANT | AFTER DELETE | Y |
| DEF_AD_CONSTANT_INS | DEF_AD_CONSTANT | BEFORE INSERT | Y |
| DEF_AD_CONSTANT_UPD | DEF_AD_CONSTANT | BEFORE UPDATE | Y |
| DEF_AD_GROUP_CEA | DEF_AD_GROUP | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_GROUP_DEL | DEF_AD_GROUP | AFTER DELETE | Y |
| DEF_AD_GROUP_INS | DEF_AD_GROUP | BEFORE INSERT | Y |
| DEF_AD_GROUP_UPD | DEF_AD_GROUP | BEFORE UPDATE | Y |
| DEF_AD_NATURE_TYPE_CEA | DEF_AD_NATURE_TYPE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_NATURE_TYPE_DEL | DEF_AD_NATURE_TYPE | AFTER DELETE | Y |
| DEF_AD_NATURE_TYPE_INS | DEF_AD_NATURE_TYPE | BEFORE INSERT | Y |
| DEF_AD_NATURE_TYPE_UPD | DEF_AD_NATURE_TYPE | BEFORE UPDATE | Y |
| DEF_AD_SETUP_CEA | DEF_AD_SETUP | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_SETUP_DC_CEA | DEF_AD_SETUP_DC | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_SETUP_DC_DEL | DEF_AD_SETUP_DC | AFTER DELETE | Y |
| DEF_AD_SETUP_DC_INS | DEF_AD_SETUP_DC | BEFORE INSERT | Y |
| DEF_AD_SETUP_DC_UPD | DEF_AD_SETUP_DC | BEFORE UPDATE | Y |
| DEF_AD_SETUP_DEL | DEF_AD_SETUP | AFTER DELETE | Y |
| DEF_AD_SETUP_INS | DEF_AD_SETUP | BEFORE INSERT | Y |
| DEF_AD_SETUP_PT_CEA | DEF_AD_SETUP_PT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_SETUP_PT_DEL | DEF_AD_SETUP_PT | AFTER DELETE | Y |
| DEF_AD_SETUP_PT_INS | DEF_AD_SETUP_PT | BEFORE INSERT | Y |
| DEF_AD_SETUP_PT_UPD | DEF_AD_SETUP_PT | BEFORE UPDATE | Y |
| DEF_AD_SETUP_UNPAID_LT_CEA | DEF_AD_SETUP_UNPAID_LT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_AD_SETUP_UNPAID_LT_DEL | DEF_AD_SETUP_UNPAID_LT | AFTER DELETE | Y |
| DEF_AD_SETUP_UNPAID_LT_INS | DEF_AD_SETUP_UNPAID_LT | BEFORE INSERT | Y |
| DEF_AD_SETUP_UNPAID_LT_UPD | DEF_AD_SETUP_UNPAID_LT | BEFORE UPDATE | Y |
| DEF_AD_SETUP_UPD | DEF_AD_SETUP | BEFORE UPDATE | Y |
| DEF_ALLOWANCE_DEDUCTION_DEL | DEF_ALLOWANCE_DEDUCTION | AFTER DELETE | Y |
| DEF_ALLOWANCE_DEDUCTION_INS | DEF_ALLOWANCE_DEDUCTION | BEFORE INSERT | Y |
| DEF_ALLOWANCE_DEDUCTION_UPD | DEF_ALLOWANCE_DEDUCTION | BEFORE UPDATE | Y |
| DEF_ARREAR_CEA | DEF_ARREAR | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_ARREAR_DEL | DEF_ARREAR | AFTER DELETE | Y |
| DEF_ARREAR_INS | DEF_ARREAR | BEFORE INSERT | Y |
| DEF_ARREAR_UPD | DEF_ARREAR | BEFORE UPDATE | Y |
| DEF_EMP_FINANCIAL_COST_CENTER_NULL | DEF_EMP_FINANCIAL | BEFORE UPDATE | Y |
| DEF_EMP_FINANCIAL_DEL | DEF_EMP_FINANCIAL | AFTER DELETE | Y |
| DEF_EMP_FINANCIAL_INS | DEF_EMP_FINANCIAL | BEFORE INSERT | Y |
| DEF_EMP_FINANCIAL_UPD | DEF_EMP_FINANCIAL | BEFORE UPDATE | Y |
| DEF_EMP_JOB_DEL | DEF_EMP_JOB | AFTER DELETE | Y |
| DEF_EMP_JOB_INS | DEF_EMP_JOB | BEFORE INSERT | Y |
| DEF_EMP_JOB_UPD | DEF_EMP_JOB | BEFORE UPDATE | Y |
| DEF_EXPENSE_CEA | DEF_EXPENSE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_EXPENSE_CONSTANT_CEA | DEF_EXPENSE_CONSTANT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_EXPENSE_CONSTANT_DEL | DEF_EXPENSE_CONSTANT | AFTER DELETE | Y |
| DEF_EXPENSE_CONSTANT_INS | DEF_EXPENSE_CONSTANT | BEFORE INSERT | Y |
| DEF_EXPENSE_CONSTANT_UPD | DEF_EXPENSE_CONSTANT | BEFORE UPDATE | Y |
| DEF_EXPENSE_DEL | DEF_EXPENSE | AFTER DELETE | Y |
| DEF_EXPENSE_DETAIL_CEA | DEF_EXPENSE_DETAIL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_EXPENSE_DETAIL_DEL | DEF_EXPENSE_DETAIL | AFTER DELETE | Y |
| DEF_EXPENSE_DETAIL_INS | DEF_EXPENSE_DETAIL | BEFORE INSERT | Y |
| DEF_EXPENSE_DETAIL_SLAB_CEA | DEF_EXPENSE_DETAIL_SLAB | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_EXPENSE_DETAIL_SLAB_DEL | DEF_EXPENSE_DETAIL_SLAB | AFTER DELETE | Y |
| DEF_EXPENSE_DETAIL_SLAB_INS | DEF_EXPENSE_DETAIL_SLAB | BEFORE INSERT | Y |
| DEF_EXPENSE_DETAIL_SLAB_UPD | DEF_EXPENSE_DETAIL_SLAB | BEFORE UPDATE | Y |
| DEF_EXPENSE_DETAIL_UPD | DEF_EXPENSE_DETAIL | BEFORE UPDATE | Y |
| DEF_EXPENSE_INS | DEF_EXPENSE | BEFORE INSERT | Y |
| DEF_EXPENSE_TAXABLE_ACC_CEA | DEF_EXPENSE_TAXABLE_ACC | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_EXPENSE_UPD | DEF_EXPENSE | BEFORE UPDATE | Y |
| DEF_EXPENSE_WORKFLOW_CEA | DEF_EXPENSE_WORKFLOW | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_FINANCIAL_SETUP_DEL | DEF_FINANCIAL_SETUP | AFTER DELETE | Y |
| DEF_FINANCIAL_SETUP_INS | DEF_FINANCIAL_SETUP | BEFORE INSERT | Y |
| DEF_FINANCIAL_SETUP_UPD | DEF_FINANCIAL_SETUP | BEFORE UPDATE | Y |
| DEF_FS_ELEMENT_DEL | DEF_FS_ELEMENT | AFTER DELETE | Y |
| DEF_FS_ELEMENT_INS | DEF_FS_ELEMENT | BEFORE INSERT | Y |
| DEF_FS_ELEMENT_UPD | DEF_FS_ELEMENT | BEFORE UPDATE | Y |
| DEF_GL_SETUP_DETAIL_DEL | DEF_GL_SETUP_DETAIL | AFTER DELETE | Y |
| DEF_GL_SETUP_DETAIL_FS_DEL | DEF_GL_SETUP_DETAIL_FS | AFTER DELETE | Y |
| DEF_GL_SETUP_DETAIL_FS_INS | DEF_GL_SETUP_DETAIL_FS | BEFORE INSERT | Y |
| DEF_GL_SETUP_DETAIL_FS_UPD | DEF_GL_SETUP_DETAIL_FS | BEFORE UPDATE | Y |
| DEF_GL_SETUP_DETAIL_INS | DEF_GL_SETUP_DETAIL | BEFORE INSERT | Y |
| DEF_GL_SETUP_DETAIL_UPD | DEF_GL_SETUP_DETAIL | BEFORE UPDATE | Y |
| DEF_GL_SETUP_MASTER_CEA | DEF_GL_SETUP_MASTER | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_GL_SETUP_MASTER_DEL | DEF_GL_SETUP_MASTER | AFTER DELETE | Y |
| DEF_GL_SETUP_MASTER_INS | DEF_GL_SETUP_MASTER | BEFORE INSERT | Y |
| DEF_GL_SETUP_MASTER_UPD | DEF_GL_SETUP_MASTER | BEFORE UPDATE | Y |
| DEF_GL_VOUCHER_DEL | DEF_GL_VOUCHER | AFTER DELETE | Y |
| DEF_GL_VOUCHER_INS | DEF_GL_VOUCHER | BEFORE INSERT | Y |
| DEF_GL_VOUCHER_UPD | DEF_GL_VOUCHER | BEFORE UPDATE | Y |
| DEF_GRADE_WISE_PERCENTAGE_CEA | DEF_GRADE_WISE_PERCENTAGE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_GRADE_WISE_PERCENTAGE_DEL | DEF_GRADE_WISE_PERCENTAGE | AFTER DELETE | Y |
| DEF_GRADE_WISE_PERCENTAGE_INS | DEF_GRADE_WISE_PERCENTAGE | BEFORE INSERT | Y |
| DEF_GRADE_WISE_PERCENTAGE_UPD | DEF_GRADE_WISE_PERCENTAGE | BEFORE UPDATE | Y |
| DEF_INCOME_TAX_DEL | DEF_INCOME_TAX | AFTER DELETE | Y |
| DEF_INCOME_TAX_INS | DEF_INCOME_TAX | BEFORE INSERT | Y |
| DEF_INCOME_TAX_UPD | DEF_INCOME_TAX | BEFORE UPDATE | Y |
| DEF_INCREMENT_TYPE_CEA | DEF_INCREMENT_TYPE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_INCREMENT_TYPE_DEL | DEF_INCREMENT_TYPE | AFTER DELETE | Y |
| DEF_INCREMENT_TYPE_INS | DEF_INCREMENT_TYPE | BEFORE INSERT | Y |
| DEF_INCREMENT_TYPE_UPD | DEF_INCREMENT_TYPE | BEFORE UPDATE | Y |
| DEF_ITAX_ADJUSTMENT_CEA | DEF_ITAX_ADJUSTMENT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_ITAX_DETAIL_AD_CEA | DEF_ITAX_DETAIL_AD | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_ITAX_MR_SLAB_CEA | DEF_ITAX_MR_SLAB | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_ITAX_SLAB_CEA | DEF_ITAX_SLAB | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_LETTER_TYPE_DEL | DEF_LETTER_TYPE | AFTER DELETE | Y |
| DEF_LETTER_TYPE_INS | DEF_LETTER_TYPE | BEFORE INSERT | Y |
| DEF_LETTER_TYPE_UPD | DEF_LETTER_TYPE | BEFORE UPDATE | Y |
| DEF_LIABILITY_DEL | DEF_LIABILITY | AFTER DELETE | Y |
| DEF_LIABILITY_INS | DEF_LIABILITY | BEFORE INSERT | Y |
| DEF_LIABILITY_UPD | DEF_LIABILITY | BEFORE UPDATE | Y |
| DEF_LOAN_INTEREST_RATE_CEA | DEF_LOAN_INTEREST_RATE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_LOAN_INTEREST_RATE_DEL | DEF_LOAN_INTEREST_RATE | AFTER DELETE | Y |
| DEF_LOAN_INTEREST_RATE_INS | DEF_LOAN_INTEREST_RATE | BEFORE INSERT | Y |
| DEF_LOAN_INTEREST_RATE_UPD | DEF_LOAN_INTEREST_RATE | BEFORE UPDATE | Y |
| DEF_LOAN_TYPE_CEA | DEF_LOAN_TYPE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_LOAN_TYPE_CONSTANT_CEA | DEF_LOAN_TYPE_CONSTANT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_LOAN_TYPE_CONSTANT_DEL | DEF_LOAN_TYPE_CONSTANT | AFTER DELETE | Y |
| DEF_LOAN_TYPE_CONSTANT_INS | DEF_LOAN_TYPE_CONSTANT | BEFORE INSERT | Y |
| DEF_LOAN_TYPE_CONSTANT_UPD | DEF_LOAN_TYPE_CONSTANT | BEFORE UPDATE | Y |
| DEF_LOAN_TYPE_DEL | DEF_LOAN_TYPE | AFTER DELETE | Y |
| DEF_LOAN_TYPE_INS | DEF_LOAN_TYPE | BEFORE INSERT | Y |
| DEF_LOAN_TYPE_UPD | DEF_LOAN_TYPE | BEFORE UPDATE | Y |
| DEF_MONTH_CHANGE_DEL | DEF_MONTH_CHANGE | AFTER DELETE | Y |
| DEF_MONTH_CHANGE_INS | DEF_MONTH_CHANGE | BEFORE INSERT | Y |
| DEF_MONTH_CHANGE_UPD | DEF_MONTH_CHANGE | BEFORE UPDATE | Y |
| DEF_PAYROLL_LOCATION_CEA | DEF_PAYROLL_LOCATION | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAYROLL_LOCATION_DEL | DEF_PAYROLL_LOCATION | AFTER DELETE | Y |
| DEF_PAYROLL_LOCATION_INS | DEF_PAYROLL_LOCATION | BEFORE INSERT | Y |
| DEF_PAYROLL_LOCATION_UPD | DEF_PAYROLL_LOCATION | BEFORE UPDATE | Y |
| DEF_PAYROLL_WORKFLOW_DEL | DEF_PAYROLL_WORKFLOW | AFTER DELETE | Y |
| DEF_PAYROLL_WORKFLOW_INS | DEF_PAYROLL_WORKFLOW | BEFORE INSERT | Y |
| DEF_PAYROLL_WORKFLOW_UPD | DEF_PAYROLL_WORKFLOW | BEFORE UPDATE | Y |
| DEF_PAYSCALE_CEA | DEF_PAYSCALE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAYSCALE_DEL | DEF_PAYSCALE | AFTER DELETE | Y |
| DEF_PAYSCALE_DETAIL_CEA | DEF_PAYSCALE_DETAIL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAYSCALE_DETAIL_DEL | DEF_PAYSCALE_DETAIL | AFTER DELETE | Y |
| DEF_PAYSCALE_DETAIL_INS | DEF_PAYSCALE_DETAIL | BEFORE INSERT | Y |
| DEF_PAYSCALE_DETAIL_UPD | DEF_PAYSCALE_DETAIL | BEFORE UPDATE | Y |
| DEF_PAYSCALE_INS | DEF_PAYSCALE | BEFORE INSERT | Y |
| DEF_PAYSCALE_UPD | DEF_PAYSCALE | BEFORE UPDATE | Y |
| DEF_PAY_VOUCHER_LOCATION_CEA | DEF_PAY_VOUCHER_LOCATION | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAY_VOUCHER_LOCATION_DEL | DEF_PAY_VOUCHER_LOCATION | AFTER DELETE | Y |
| DEF_PAY_VOUCHER_LOCATION_INS | DEF_PAY_VOUCHER_LOCATION | BEFORE INSERT | Y |
| DEF_PAY_VOUCHER_LOCATION_UPD | DEF_PAY_VOUCHER_LOCATION | BEFORE UPDATE | Y |
| DEF_PAY_VOUCHER_SETUP_CEA | DEF_PAY_VOUCHER_SETUP | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAY_VOUCHER_SETUP_DEL | DEF_PAY_VOUCHER_SETUP | AFTER DELETE | Y |
| DEF_PAY_VOUCHER_SETUP_DTL_CEA | DEF_PAY_VOUCHER_SETUP_DTL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAY_VOUCHER_SETUP_DTL_DEL | DEF_PAY_VOUCHER_SETUP_DTL | AFTER DELETE | Y |
| DEF_PAY_VOUCHER_SETUP_DTL_INS | DEF_PAY_VOUCHER_SETUP_DTL | BEFORE INSERT | Y |
| DEF_PAY_VOUCHER_SETUP_DTL_UPD | DEF_PAY_VOUCHER_SETUP_DTL | BEFORE UPDATE | Y |
| DEF_PAY_VOUCHER_SETUP_INS | DEF_PAY_VOUCHER_SETUP | BEFORE INSERT | Y |
| DEF_PAY_VOUCHER_SETUP_PK | DEF_PAY_VOUCHER_SETUP | BEFORE INSERT | Y |
| DEF_PAY_VOUCHER_SETUP_UPD | DEF_PAY_VOUCHER_SETUP | BEFORE UPDATE | Y |
| DEF_PAY_VOUCHER_TYPE_CEA | DEF_PAY_VOUCHER_TYPE | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PAY_VOUCHER_TYPE_DEL | DEF_PAY_VOUCHER_TYPE | AFTER DELETE | Y |
| DEF_PAY_VOUCHER_TYPE_INS | DEF_PAY_VOUCHER_TYPE | BEFORE INSERT | Y |
| DEF_PAY_VOUCHER_TYPE_UPD | DEF_PAY_VOUCHER_TYPE | BEFORE UPDATE | Y |
| DEF_PERCENTAGE_SETUP_CEA | DEF_PERCENTAGE_SETUP | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PERCENTAGE_SETUP_DEL | DEF_PERCENTAGE_SETUP | AFTER DELETE | Y |
| DEF_PERCENTAGE_SETUP_INS | DEF_PERCENTAGE_SETUP | BEFORE INSERT | Y |
| DEF_PERCENTAGE_SETUP_UPD | DEF_PERCENTAGE_SETUP | BEFORE UPDATE | Y |
| DEF_PF_SETUP_DEL | DEF_PF_SETUP | AFTER DELETE | Y |
| DEF_PF_SETUP_INS | DEF_PF_SETUP | BEFORE INSERT | Y |
| DEF_PF_SETUP_UPD | DEF_PF_SETUP | BEFORE UPDATE | Y |
| DEF_PROJECT_CEA | DEF_PROJECT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_PROJECT_DEL | DEF_PROJECT | AFTER DELETE | Y |
| DEF_PROJECT_INS | DEF_PROJECT | BEFORE INSERT | Y |
| DEF_PROJECT_UPD | DEF_PROJECT | BEFORE UPDATE | Y |
| DEF_SETUP_CEA | DEF_SETUP | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_SETUP_CONSTANT_CEA | DEF_SETUP_CONSTANT | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_SETUP_CONSTANT_DEL | DEF_SETUP_CONSTANT | AFTER DELETE | Y |
| DEF_SETUP_CONSTANT_INS | DEF_SETUP_CONSTANT | BEFORE INSERT | Y |
| DEF_SETUP_CONSTANT_UPD | DEF_SETUP_CONSTANT | BEFORE UPDATE | Y |
| DEF_SETUP_DEL | DEF_SETUP | AFTER DELETE | Y |
| DEF_SETUP_INS | DEF_SETUP | BEFORE INSERT | Y |
| DEF_SETUP_UPD | DEF_SETUP | BEFORE UPDATE | Y |
| DEF_TAX_AMOUNT_OTHER_THAN_SAL_CEA | DEF_TAX_AMOUNT_OTHER_THAN_SAL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| DEF_TAX_AMOUNT_OTHER_THAN__DEL | DEF_TAX_AMOUNT_OTHER_THAN_SAL | AFTER DELETE | Y |
| DEF_TAX_AMOUNT_OTHER_THAN__INS | DEF_TAX_AMOUNT_OTHER_THAN_SAL | BEFORE INSERT | Y |
| DEF_TAX_AMOUNT_OTHER_THAN__UPD | DEF_TAX_AMOUNT_OTHER_THAN_SAL | BEFORE UPDATE | Y |
| EMP_ALLOWANCE_DEDUCTION_DEL | EMP_ALLOWANCE_DEDUCTION | AFTER DELETE | Y |
| EMP_ALLOWANCE_DEDUCTION_DE_DEL | EMP_ALLOWANCE_DEDUCTION_DETAIL | AFTER DELETE | Y |
| EMP_ALLOWANCE_DEDUCTION_DE_INS | EMP_ALLOWANCE_DEDUCTION_DETAIL | BEFORE INSERT | Y |
| EMP_ALLOWANCE_DEDUCTION_DE_UPD | EMP_ALLOWANCE_DEDUCTION_DETAIL | BEFORE UPDATE | Y |
| EMP_ALLOWANCE_DEDUCTION_INS | EMP_ALLOWANCE_DEDUCTION | BEFORE INSERT | Y |
| EMP_ALLOWANCE_DEDUCTION_UPD | EMP_ALLOWANCE_DEDUCTION | BEFORE UPDATE | Y |
| EMP_AWARDS_DEL | EMP_AWARDS | AFTER DELETE | Y |
| EMP_AWARDS_INS | EMP_AWARDS | BEFORE INSERT | Y |
| EMP_AWARDS_UPD | EMP_AWARDS | BEFORE UPDATE | Y |
| EMP_AWARD_PAYMENT_DEL | EMP_AWARD_PAYMENT | AFTER DELETE | Y |
| EMP_AWARD_PAYMENT_INS | EMP_AWARD_PAYMENT | BEFORE INSERT | Y |
| EMP_AWARD_PAYMENT_UPD | EMP_AWARD_PAYMENT | BEFORE UPDATE | Y |
| EMP_EXPENSE_DEL | EMP_EXPENSE | AFTER DELETE | Y |
| EMP_EXPENSE_INS | EMP_EXPENSE | BEFORE INSERT | Y |
| EMP_EXPENSE_UPD | EMP_EXPENSE | BEFORE UPDATE | Y |
| EMP_EXP_DET_PROJECT_DEL | EMP_EXP_DET_PROJECT | AFTER DELETE | Y |
| EMP_EXP_DET_PROJECT_INS | EMP_EXP_DET_PROJECT | BEFORE INSERT | Y |
| EMP_EXP_DET_PROJECT_UPD | EMP_EXP_DET_PROJECT | BEFORE UPDATE | Y |
| EMP_INCREMENT_DETAIL_DEL | EMP_INCREMENT_DETAIL | AFTER DELETE | Y |
| EMP_INCREMENT_DETAIL_INS | EMP_INCREMENT_DETAIL | BEFORE INSERT | Y |
| EMP_INCREMENT_DETAIL_UPD | EMP_INCREMENT_DETAIL | BEFORE UPDATE | Y |
| EMP_INCREMENT_MASTER_DEL | EMP_INCREMENT_MASTER | AFTER DELETE | Y |
| EMP_INCREMENT_MASTER_INS | EMP_INCREMENT_MASTER | BEFORE INSERT | Y |
| EMP_INCREMENT_MASTER_UPD | EMP_INCREMENT_MASTER | BEFORE UPDATE | Y |
| EMP_INC_MAS_CHANGE_SAL | EMP_INCREMENT_MASTER | AFTER UPDATE OF "CURRENT_GROSS" | Y |
| EMP_INC_MAS_DEL_SAL | EMP_INCREMENT_MASTER | AFTER DELETE | Y |
| EMP_INC_MAS_INS_SAL | EMP_INCREMENT_MASTER | AFTER INSERT | Y |
| EMP_ITAX_ADJUSTMENT_DEL | EMP_ITAX_ADJUSTMENT | AFTER DELETE | Y |
| EMP_ITAX_ADJUSTMENT_DTL_M_DEL | EMP_ITAX_ADJUSTMENT_DTL_M | AFTER DELETE | Y |
| EMP_ITAX_ADJUSTMENT_DTL_M_INS | EMP_ITAX_ADJUSTMENT_DTL_M | BEFORE INSERT | Y |
| EMP_ITAX_ADJUSTMENT_DTL_M_UPD | EMP_ITAX_ADJUSTMENT_DTL_M | BEFORE UPDATE | Y |
| EMP_ITAX_ADJUSTMENT_INS | EMP_ITAX_ADJUSTMENT | BEFORE INSERT | Y |
| EMP_ITAX_ADJUSTMENT_UPD | EMP_ITAX_ADJUSTMENT | BEFORE UPDATE | Y |
| EMP_LIABILITY_DEL | EMP_LIABILITY | AFTER DELETE | Y |
| EMP_LIABILITY_INS | EMP_LIABILITY | BEFORE INSERT | Y |
| EMP_LIABILITY_UPD | EMP_LIABILITY | BEFORE UPDATE | Y |
| EMP_PAYMENT_DEL | EMP_PAYMENT | AFTER DELETE | Y |
| EMP_PAYMENT_INS | EMP_PAYMENT | BEFORE INSERT | Y |
| EMP_PAYMENT_UPD | EMP_PAYMENT | BEFORE UPDATE | Y |
| EMP_TAX_AMOUNT_OTHER_THAN__DEL | EMP_TAX_AMOUNT_OTHER_THAN_SAL | AFTER DELETE | Y |
| EMP_TAX_AMOUNT_OTHER_THAN__INS | EMP_TAX_AMOUNT_OTHER_THAN_SAL | BEFORE INSERT | Y |
| EMP_TAX_AMOUNT_OTHER_THAN__UPD | EMP_TAX_AMOUNT_OTHER_THAN_SAL | BEFORE UPDATE | Y |
| EXPENSE_CLAIM_DETAIL_DEL | EXPENSE_CLAIM_DETAIL | AFTER DELETE | Y |
| EXPENSE_CLAIM_DETAIL_INS | EXPENSE_CLAIM_DETAIL | BEFORE INSERT | Y |
| EXPENSE_CLAIM_DETAIL_UPD | EXPENSE_CLAIM_DETAIL | BEFORE UPDATE | Y |
| EXPENSE_CLAIM_MASTER_DEL | EXPENSE_CLAIM_MASTER | AFTER DELETE | Y |
| EXPENSE_CLAIM_MASTER_INS | EXPENSE_CLAIM_MASTER | AFTER INSERT | Y |
| EXPENSE_CLAIM_MASTER_UPD | EXPENSE_CLAIM_MASTER | BEFORE UPDATE | Y |
| EXPENSE_CLAIM_PROJECT_DEL | EXPENSE_CLAIM_PROJECT | AFTER DELETE | Y |
| EXPENSE_CLAIM_PROJECT_INS | EXPENSE_CLAIM_PROJECT | BEFORE INSERT | Y |
| EXPENSE_CLAIM_PROJECT_UPD | EXPENSE_CLAIM_PROJECT | BEFORE UPDATE | Y |
| EXPENSE_CLAIM_WORKFLOW_Q_APPR_INS | EXPENSE_CLAIM_WORKFLOW_Q | BEFORE INSERT | Y |
| EXPENSE_CLAIM_WORKFLOW_Q_INS | EXPENSE_CLAIM_WORKFLOW_Q | BEFORE INSERT | Y |
| FINAL_SETTLEMENT_DEL | FINAL_SETTLEMENT | AFTER DELETE | Y |
| FINAL_SETTLEMENT_ELEMENT_DEL | FINAL_SETTLEMENT_ELEMENT | AFTER DELETE | Y |
| FINAL_SETTLEMENT_ELEMENT_INS | FINAL_SETTLEMENT_ELEMENT | BEFORE INSERT | Y |
| FINAL_SETTLEMENT_ELEMENT_UPD | FINAL_SETTLEMENT_ELEMENT | BEFORE UPDATE | Y |
| FINAL_SETTLEMENT_INS | FINAL_SETTLEMENT | BEFORE INSERT | Y |
| FINAL_SETTLEMENT_UPD | FINAL_SETTLEMENT | BEFORE UPDATE | Y |
| FS_PQ_UPD | FINAL_SETTLEMENT | BEFORE UPDATE | Y |
| FS_WORKFLOW_PQ_INS | FINAL_SETTLEMENT_WF_Q | BEFORE INSERT | Y |
| GENERIC_REPORT_FIELD_CEA | GENERIC_REPORT_FIELD | BEFORE INSERT OR UPDATE OR DELETE | Y |
| GENERIC_REPORT_FIELD_DEL | GENERIC_REPORT_FIELD | AFTER DELETE | Y |
| GENERIC_REPORT_FIELD_DTL_CEA | GENERIC_REPORT_FIELD_DTL | BEFORE INSERT OR UPDATE OR DELETE | Y |
| GENERIC_REPORT_FIELD_DTL_PK | GENERIC_REPORT_FIELD_DTL | BEFORE INSERT | Y |
| GENERIC_REPORT_FIELD_INS | GENERIC_REPORT_FIELD | BEFORE INSERT | Y |
| GENERIC_REPORT_FIELD_UPD | GENERIC_REPORT_FIELD | BEFORE UPDATE | Y |
| GENERIC_REPORT_MASTER_CEA | GENERIC_REPORT_MASTER | BEFORE INSERT OR UPDATE OR DELETE | Y |
| GENERIC_REPORT_MASTER_DEL | GENERIC_REPORT_MASTER | AFTER DELETE | Y |
| GENERIC_REPORT_MASTER_INS | GENERIC_REPORT_MASTER | BEFORE INSERT | Y |
| GENERIC_REPORT_MASTER_UPD | GENERIC_REPORT_MASTER | BEFORE UPDATE | Y |
| HOLD_ORDER_DEL | HOLD_ORDER | AFTER DELETE | Y |
| HOLD_ORDER_INS | HOLD_ORDER | BEFORE INSERT | Y |
| HOLD_ORDER_UPD | HOLD_ORDER | BEFORE UPDATE | Y |
| ITAX_PAYMENT_DETAIL_DEL | ITAX_PAYMENT_DETAIL | AFTER DELETE | Y |
| ITAX_PAYMENT_DETAIL_INS | ITAX_PAYMENT_DETAIL | BEFORE INSERT | Y |
| ITAX_PAYMENT_DETAIL_UPD | ITAX_PAYMENT_DETAIL | BEFORE UPDATE | Y |
| ITAX_PAYMENT_MASTER_DEL | ITAX_PAYMENT_MASTER | AFTER DELETE | Y |
| ITAX_PAYMENT_MASTER_INS | ITAX_PAYMENT_MASTER | BEFORE INSERT | Y |
| ITAX_PAYMENT_MASTER_UPD | ITAX_PAYMENT_MASTER | BEFORE UPDATE | Y |
| LOAN_PAYMENT_INTEREST_DEL | LOAN_PAYMENT_INTEREST | AFTER DELETE | Y |
| LOAN_PAYMENT_INTEREST_INS | LOAN_PAYMENT_INTEREST | BEFORE INSERT | Y |
| LOAN_PAYMENT_INTEREST_UPD | LOAN_PAYMENT_INTEREST | BEFORE UPDATE | Y |
| LOAN_PAYMENT_MASTER_DEL | LOAN_PAYMENT_MASTER | AFTER DELETE | Y |
| LOAN_PAYMENT_MASTER_INS | LOAN_PAYMENT_MASTER | BEFORE INSERT | Y |
| LOAN_PAYMENT_MASTER_N_DEL | LOAN_PAYMENT_MASTER_N | AFTER DELETE | Y |
| LOAN_PAYMENT_MASTER_N_INS | LOAN_PAYMENT_MASTER_N | BEFORE INSERT | Y |
| LOAN_PAYMENT_MASTER_N_UPD | LOAN_PAYMENT_MASTER_N | BEFORE UPDATE | Y |
| LOAN_PAYMENT_MASTER_UPD | LOAN_PAYMENT_MASTER | BEFORE UPDATE | Y |
| LOAN_REFUND_DETAIL_DEL | LOAN_REFUND_DETAIL | AFTER DELETE | Y |
| LOAN_REFUND_DETAIL_INS | LOAN_REFUND_DETAIL | BEFORE INSERT | Y |
| LOAN_REFUND_DETAIL_N_DEL | LOAN_REFUND_DETAIL_N | AFTER DELETE | Y |
| LOAN_REFUND_DETAIL_N_INS | LOAN_REFUND_DETAIL_N | BEFORE INSERT | Y |
| LOAN_REFUND_DETAIL_N_UPD | LOAN_REFUND_DETAIL_N | BEFORE UPDATE | Y |
| LOAN_REFUND_DETAIL_UPD | LOAN_REFUND_DETAIL | BEFORE UPDATE | Y |
| LOAN_REFUND_MASTER_DEL | LOAN_REFUND_MASTER | AFTER DELETE | Y |
| LOAN_REFUND_MASTER_INS | LOAN_REFUND_MASTER | BEFORE INSERT | Y |
| LOAN_REFUND_MASTER_N_DEL | LOAN_REFUND_MASTER_N | AFTER DELETE | Y |
| LOAN_REFUND_MASTER_N_INS | LOAN_REFUND_MASTER_N | BEFORE INSERT | Y |
| LOAN_REFUND_MASTER_N_UPD | LOAN_REFUND_MASTER_N | BEFORE UPDATE | Y |
| LOAN_REFUND_MASTER_UPD | LOAN_REFUND_MASTER | BEFORE UPDATE | Y |
| LOAN_REFUND_OPENING_DEL | LOAN_REFUND_OPENING | AFTER DELETE | Y |
| LOAN_REFUND_OPENING_INS | LOAN_REFUND_OPENING | BEFORE INSERT | Y |
| LOAN_REFUND_OPENING_UPD | LOAN_REFUND_OPENING | BEFORE UPDATE | Y |
| MONTH_CHANGE_REQUEST_DEL | MONTH_CHANGE_REQUEST | AFTER DELETE | Y |
| MONTH_CHANGE_REQUEST_INS | MONTH_CHANGE_REQUEST | BEFORE INSERT | Y |
| MONTH_CHANGE_REQUEST_PQ | MONTH_CHANGE_REQUEST | BEFORE INSERT OR UPDATE | Y |
| MONTH_CHANGE_REQUEST_UPD | MONTH_CHANGE_REQUEST | BEFORE UPDATE | Y |
| PAY_AD_BALANCE_DEL | PAY_AD_BALANCE | AFTER DELETE | Y |
| PAY_AD_BALANCE_INS | PAY_AD_BALANCE | BEFORE INSERT | Y |
| PAY_AD_BALANCE_UPD | PAY_AD_BALANCE | BEFORE UPDATE | Y |
| PAY_ALLOWANCE_DEDUCTION_DEL | PAY_ALLOWANCE_DEDUCTION | AFTER DELETE | Y |
| PAY_ALLOWANCE_DEDUCTION_INS | PAY_ALLOWANCE_DEDUCTION | BEFORE INSERT | Y |
| PAY_ALLOWANCE_DEDUCTION_UPD | PAY_ALLOWANCE_DEDUCTION | BEFORE UPDATE | Y |
| PAY_ARREAR_DEL | PAY_ARREAR | AFTER DELETE | Y |
| PAY_ARREAR_INS | PAY_ARREAR | BEFORE INSERT | Y |
| PAY_ARREAR_UPD | PAY_ARREAR | BEFORE UPDATE | Y |
| PAY_FINANCIAL_YEAR_CEA | PAY_FINANCIAL_YEAR | BEFORE INSERT OR UPDATE OR DELETE | Y |
| PAY_FINANCIAL_YEAR_DEL | PAY_FINANCIAL_YEAR | AFTER DELETE | Y |
| PAY_FINANCIAL_YEAR_INS | PAY_FINANCIAL_YEAR | BEFORE INSERT | Y |
| PAY_FINANCIAL_YEAR_UPD | PAY_FINANCIAL_YEAR | BEFORE UPDATE | Y |
| PAY_ITAX_DETAIL_DEL | PAY_ITAX_DETAIL | AFTER DELETE | Y |
| PAY_ITAX_DETAIL_INS | PAY_ITAX_DETAIL | BEFORE INSERT | Y |
| PAY_ITAX_DETAIL_UPD | PAY_ITAX_DETAIL | BEFORE UPDATE | Y |
| PAY_LEAVES_DEL | PAY_LEAVES | AFTER DELETE | Y |
| PAY_LEAVES_INS | PAY_LEAVES | BEFORE INSERT | Y |
| PAY_LEAVES_UPD | PAY_LEAVES | BEFORE UPDATE | Y |
| PAY_MASTER_DEL | PAY_MASTER | AFTER DELETE | Y |
| PAY_MASTER_INS | PAY_MASTER | BEFORE INSERT | Y |
| PAY_MASTER_UPD | PAY_MASTER | BEFORE UPDATE | Y |
| PAY_PF_VOUCHER_DEL | PAY_PF_VOUCHER | AFTER DELETE | Y |
| PAY_PF_VOUCHER_INS | PAY_PF_VOUCHER | BEFORE INSERT | Y |
| PAY_PF_VOUCHER_UPD | PAY_PF_VOUCHER | BEFORE UPDATE | Y |
| PAY_STATUS_DEL | PAY_STATUS | AFTER DELETE | Y |
| PAY_STATUS_INS | PAY_STATUS | BEFORE INSERT | Y |
| PAY_STATUS_UPD | PAY_STATUS | BEFORE UPDATE | Y |
| PAY_VOUCHER_DEL | PAY_VOUCHER | AFTER DELETE | Y |
| PAY_VOUCHER_DETAIL_DEL | PAY_VOUCHER_DETAIL | AFTER DELETE | Y |
| PAY_VOUCHER_DETAIL_INS | PAY_VOUCHER_DETAIL | BEFORE INSERT | Y |
| PAY_VOUCHER_DETAIL_UPD | PAY_VOUCHER_DETAIL | BEFORE UPDATE | Y |
| PAY_VOUCHER_INS | PAY_VOUCHER | BEFORE INSERT | Y |
| PAY_VOUCHER_MASTER_DEL | PAY_VOUCHER_MASTER | AFTER DELETE | Y |
| PAY_VOUCHER_MASTER_INS | PAY_VOUCHER_MASTER | BEFORE INSERT | Y |
| PAY_VOUCHER_MASTER_UPD | PAY_VOUCHER_MASTER | BEFORE UPDATE | Y |
| PAY_VOUCHER_UPD | PAY_VOUCHER | BEFORE UPDATE | Y |
| PF_FINAL_SETTLEMENT_DEL | PF_FINAL_SETTLEMENT | AFTER DELETE | Y |
| PF_FINAL_SETTLEMENT_INS | PF_FINAL_SETTLEMENT | BEFORE INSERT | Y |
| PF_FINAL_SETTLEMENT_UPD | PF_FINAL_SETTLEMENT | BEFORE UPDATE | Y |
| PROCESS_INCREMENT_MASTER_DEL | PROCESS_INCREMENT_MASTER | AFTER DELETE | Y |
| PROCESS_INCREMENT_MASTER_INS | PROCESS_INCREMENT_MASTER | BEFORE INSERT | Y |
| PROCESS_INCREMENT_MASTER_UPD | PROCESS_INCREMENT_MASTER | BEFORE UPDATE | Y |
| PROCESS_MEMBERS_DEL | PROCESS_MEMBERS | AFTER DELETE | Y |
| PROCESS_MEMBERS_INS | PROCESS_MEMBERS | BEFORE INSERT | Y |
| PROCESS_MEMBERS_UPD | PROCESS_MEMBERS | BEFORE UPDATE | Y |
| RPT_SALARY_TAX_LINE_ITEM_DEL | RPT_SALARY_TAX_LINE_ITEM | AFTER DELETE | Y |
| RPT_SALARY_TAX_LINE_ITEM_INS | RPT_SALARY_TAX_LINE_ITEM | BEFORE INSERT | Y |
| RPT_SALARY_TAX_LINE_ITEM_UPD | RPT_SALARY_TAX_LINE_ITEM | BEFORE UPDATE | Y |
| SYN_EMP_ITAX_ADJ_MON_DEL | EMP_ITAX_ADJUSTMENT_MONTHLY | AFTER DELETE | Y |
| SYN_EMP_ITAX_ADJ_MON_INS | EMP_ITAX_ADJUSTMENT_MONTHLY | BEFORE INSERT | Y |
| SYN_EMP_ITAX_ADJ_MON_UPD | EMP_ITAX_ADJUSTMENT_MONTHLY | BEFORE UPDATE | Y |
| TEMP_INCREMENT_DETAIL_DEL | TEMP_INCREMENT_DETAIL | AFTER DELETE | Y |
| TEMP_INCREMENT_DETAIL_INS | TEMP_INCREMENT_DETAIL | BEFORE INSERT | Y |
| TEMP_INCREMENT_DETAIL_UPD | TEMP_INCREMENT_DETAIL | BEFORE UPDATE | Y |
| TEMP_INCREMENT_MASTER_DEL | TEMP_INCREMENT_MASTER | AFTER DELETE | Y |
| TEMP_INCREMENT_MASTER_INS | TEMP_INCREMENT_MASTER | BEFORE INSERT | Y |
| TEMP_INCREMENT_MASTER_UPD | TEMP_INCREMENT_MASTER | BEFORE UPDATE | Y |
| TRAVEL_ADVANCE_APPROVAL_DEL | TRAVEL_ADVANCE_APPROVAL | AFTER DELETE | Y |
| TRAVEL_ADVANCE_APPROVAL_INS | TRAVEL_ADVANCE_APPROVAL | BEFORE INSERT | Y |
| TRAVEL_ADVANCE_APPROVAL_PQ | TRAVEL_ADVANCE_APPROVAL | BEFORE INSERT OR UPDATE | Y |
| TRAVEL_ADVANCE_APPROVAL_UPD | TRAVEL_ADVANCE_APPROVAL | BEFORE UPDATE | Y |
| TRG_EXP_CLAIM_HIERARCHY_ID | EXPENSE_CLAIM_HIERARCHY | BEFORE INSERT | Y |
| TRG_EXP_CLAIM_HIERARCHY_ORG_ID | EXPENSE_CLAIM_HIERARCHY_ORG | BEFORE INSERT | Y |
| TRG_WS_ACE_JF_AP_Q | DEF_ITAX_DETAIL_AD | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_ALH_HY_ST_Q | DEF_TAX_AMOUNT_OTHER_THAN_SAL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_BAN_JP_PG_Q | DEF_EXPENSE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_BIZ_EJ_FS_Q | DEF_EXPENSE_TAXABLE_ACC | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_BLA_PZ_PG_Q | DEF_PAY_VOUCHER_SETUP | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_BUF_UB_DI_Q | DEF_AD_SETUP_DC | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_DKJ_UV_FC_Q | DEF_AD_CHART | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_DYO_YQ_OR_Q | DEF_EXPENSE_WORKFLOW | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_EMS_YD_EF_Q | GENERIC_REPORT_FIELD | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_FHI_YZ_ST_Q | DEF_AD_NATURE_TYPE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_FJA_HA_AY_Q | DEF_PERCENTAGE_SETUP | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_FLB_GV_CW_Q | DEF_GRADE_WISE_PERCENTAGE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_GXP_UF_OU_Q | DEF_PAY_VOUCHER_TYPE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_IAP_QA_QL_Q | DEF_LOAN_TYPE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_IKE_GP_IJ_Q | GENERIC_REPORT_FIELD_DTL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_IKV_BH_WN_Q | DEF_SETUP_CONSTANT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_KSE_EA_UF_Q | DEF_ITAX_MR_SLAB | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_KZL_DN_VB_Q | DEF_AD_GROUP | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_LHW_SF_PB_Q | DEF_INCREMENT_TYPE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_LIC_JY_WB_Q | DEF_ITAX_SLAB | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_LRB_SM_CW_Q | DEF_PAY_VOUCHER_SETUP_DTL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_MCF_WK_WX_Q | DEF_PAYSCALE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_MMZ_TB_FP_Q | DEF_AD_SETUP_PT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_MYU_RJ_JI_Q | DEF_PAY_VOUCHER_LOCATION | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_NEL_OY_ZL_Q | DEF_ITAX_ADJUSTMENT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_NML_BL_RN_Q | DEF_SETUP | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_NXW_PQ_TN_Q | DEF_AD_CONSTANT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_OLB_LH_ZZ_Q | DEF_LOAN_INTEREST_RATE | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_PHJ_BK_HS_Q | DEF_EXPENSE_DETAIL_SLAB | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_SAN_MB_CF_Q | DEF_PAYSCALE_DETAIL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_TKR_PZ_OS_Q | DEF_AD_CHART_DETAIL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_TTB_AI_IF_Q | DEF_GL_SETUP_MASTER | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_TWV_IJ_IA_Q | DEF_AD_SETUP_UNPAID_LT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_VTC_YQ_HK_Q | DEF_PAYROLL_LOCATION | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_WFR_HS_SR_Q | DEF_EXPENSE_DETAIL | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_WKA_UZ_BE_Q | DEF_AD_SETUP | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_WNQ_VQ_RO_Q | PAY_FINANCIAL_YEAR | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_WVB_PD_FA_Q | DEF_ARREAR | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_WXW_JX_NS_Q | GENERIC_REPORT_MASTER | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_XQB_HY_XD_Q | DEF_PROJECT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_YJR_OY_UQ_Q | DEF_EXPENSE_CONSTANT | AFTER INSERT OR UPDATE OR DELETE | Y |
| TRG_WS_YTS_VH_XA_Q | DEF_LOAN_TYPE_CONSTANT | AFTER INSERT OR UPDATE OR DELETE | Y |

## Synonyms

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

