# HRD tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

## HRD.ABSTRACT_LOV_BODY_SYSTEM

| Column | Type | Null | Comment |
|---|---|---|---|
| BODY_SYSTEM_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(300) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| DEFAULT_SELECTED | CHAR(1) default 'N' | N |  |

- **PK** `PK_ABST_LOV_BODY_SYSTEM`: BODY_SYSTEM_ID
- **Triggers**: `ABSTRACT_LOV_BODY_SYSTEM_DEL` (after delete), `ABSTRACT_LOV_BODY_SYSTEM_INS` (before insert), `ABSTRACT_LOV_BODY_SYSTEM_UPD` (before update)

## HRD.ABSTRACT_LOV_SPECIALITY

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIALITY_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(300) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| DEFAULT_SELECTED | CHAR(1) default 'N' | N |  |

- **PK** `PK_ABST_LOV_SPECIALITY`: SPECIALITY_ID
- **Triggers**: `ABSTRACT_LOV_SPECIALITY_DEL` (after delete), `ABSTRACT_LOV_SPECIALITY_INS` (before insert), `ABSTRACT_LOV_SPECIALITY_UPD` (before update)

## HRD.ABSTRACT_NEW

| Column | Type | Null | Comment |
|---|---|---|---|
| ABSTRACT_ID | VARCHAR2(12) | N |  |
| TITLE | VARCHAR2(4000) | N |  |
| PURPOSE | VARCHAR2(4000) | Y |  |
| METHOD | VARCHAR2(4000) | Y |  |
| RESULT | VARCHAR2(4000) | Y |  |
| CONCLUSION | VARCHAR2(4000) | Y |  |
| IMG_ATTACHED | CHAR(1) | Y |  |
| IMG_PATH | VARCHAR2(500) | Y |  |
| DOCUMENT_SERVER_NAME | VARCHAR2(100) | Y |  |
| SUBMISSION_DATE | DATE default (sysdate) | Y |  |
| SERIAL_NO | VARCHAR2(12) | N |  |
| AUTHORS | NUMBER(1) | N |  |
| TYPE | VARCHAR2(12) | Y |  |
| AUTHOR_ID | VARCHAR2(12) | Y |  |
| FNAMEP | VARCHAR2(60) | Y |  |
| MNAMEP | VARCHAR2(60) | Y |  |
| LNAMEP | VARCHAR2(60) | Y |  |
| INSTITUTEP | VARCHAR2(300) | Y |  |
| FNAME1 | VARCHAR2(60) | Y |  |
| MNAME1 | VARCHAR2(60) | Y |  |
| LNAME1 | VARCHAR2(60) | Y |  |
| INSTITUTE1 | VARCHAR2(300) | Y |  |
| FNAME2 | VARCHAR2(60) | Y |  |
| MNAME2 | VARCHAR2(60) | Y |  |
| LNAME2 | VARCHAR2(60) | Y |  |
| INSTITUTE2 | VARCHAR2(300) | Y |  |
| FNAME3 | VARCHAR2(60) | Y |  |
| MNAME3 | VARCHAR2(60) | Y |  |
| LNAME3 | VARCHAR2(60) | Y |  |
| INSTITUTE3 | VARCHAR2(300) | Y |  |
| FNAME4 | VARCHAR2(60) | Y |  |
| MNAME4 | VARCHAR2(60) | Y |  |
| LNAME4 | VARCHAR2(60) | Y |  |
| INSTITUTE4 | VARCHAR2(300) | Y |  |
| FNAME5 | VARCHAR2(60) | Y |  |
| MNAME5 | VARCHAR2(60) | Y |  |
| LNAME5 | VARCHAR2(60) | Y |  |
| INSTITUTE5 | VARCHAR2(300) | Y |  |
| FNAME6 | VARCHAR2(60) | Y |  |
| MNAME6 | VARCHAR2(60) | Y |  |
| LNAME6 | VARCHAR2(60) | Y |  |
| INSTITUTE6 | VARCHAR2(300) | Y |  |
| FILE_NAME | VARCHAR2(200) | Y |  |
| CATEGORY | VARCHAR2(60) | Y |  |
| STATUS | VARCHAR2(10) | Y |  |
| DELETED | CHAR(1) | Y |  |

- **PK** `PK_ABSTRACT_NEW`: ABSTRACT_ID
- **Triggers**: `ABSTRACT_NEW_AFTER_INSERT` (after insert), `ABSTRACT_NEW_AFTER_UPDATE` (after update)

## HRD.ACTING_FOR
Store information about employees who will work on in lieu of higher authority when higher authority will be on line

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_MRNO | VARCHAR2(14) | N | Store  employee code who will be on leave (Employee should be of some higher authority ex Supervisor, Manager etc) |
| ACTOR_MRNO | VARCHAR2(14) | N | Store employee code who will work in absence of actual employee |
| LEAVE_FROM_DATE | DATE | N | Store leave starting date |
| LEAVE_TO_DATE | DATE | Y | Store leave ending date |
| SUBSTITUTE_TYPE | CHAR(1) default 'A' | N | 'A'= Administrative , 'C'= Clinical |
| SOURCE_TYPE | CHAR(1) | Y |  |

- **PK** `PK_ACTING_FOR`: EMP_MRNO, LEAVE_FROM_DATE, SUBSTITUTE_TYPE
- **Triggers**: `ACTING_FOR_DEL` (after delete), `ACTING_FOR_INS` (before insert), `ACTING_FOR_UPD` (before update), `SEND_EMAIL_SUBSTITUTE` (after insert)

## HRD.ACTING_FOR_USER_TASK_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_MRNO | VARCHAR2(14) | N |  |
| ACTOR_MRNO | VARCHAR2(14) | N |  |
| LEAVE_FROM_DATE | DATE | N |  |
| LEAVE_TO_DATE | DATE | Y |  |
| SUBSTITUTE_TYPE | CHAR(1) | Y |  |
| ASSIGNMENT_ID | NUMBER | N |  |

- **PK** `PK_USER_WISE_TASK`: EMP_MRNO, ACTOR_MRNO, LEAVE_FROM_DATE, ASSIGNMENT_ID
- **FK** `FK_ASSIGNMENT_EMP_01`: (ASSIGNMENT_ID) -> HIS.USER_ASSIGNMENT(ASSIGNMENT_ID) [disabled]
- **Triggers**: `ACTING_FOR_USER_TASK_WISE_DEL` (after delete), `ACTING_FOR_USER_TASK_WISE_INS` (before insert), `ACTING_FOR_USER_TASK_WISE_UPD` (before update)

## HRD.LEAVE_TYPE
Contain information of all kinds of employee days (leave days, shift days)

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Store unique leave type ID |
| DESCRIPTION | VARCHAR2(60) | Y | Store leave type description |
| MIN_PRE_EXTENSION | NUMBER(3) | Y |  |
| MIN_NOTIFICATION_DAYS | NUMBER(3) | Y |  |
| MAX_CONSECUTIVE_LEAVES | NUMBER(3) | Y |  |
| MAX_CONSECUTIVE_LEAVE_EMERGENY | NUMBER(3) | Y |  |
| MAX_TIME_DURING_YEAR | NUMBER(3) | Y |  |
| MAX_MONTHLY_LEAVES | NUMBER(3) | Y | the purpose of this column maximum leave allowed in a month |
| MAX_TIME_IN_SERVICE | NUMBER(4) | Y |  |
| MIN_SERVICE_REQUIRED | NUMBER(4) | Y | Store months after which employee is eligible for leave for.ex 12 means 12 months of service is required to avail leave |
| LEAVES_ALLOWED | NUMBER(3) | Y | Maximum leave allowed in a year |
| ENCASHMENT_ALLOWED | VARCHAR2(1) | Y |  |
| ENCASHMENTABLE_LEAVES | NUMBER(3) | Y |  |
| MAX_ACCUMULATED_DAYS | NUMBER(3) | Y |  |
| LAPSE_PERIOD_OTHERS | NUMBER(3) | Y |  |
| LAPSE_PERIOD_MEDICAL | NUMBER(3) | Y |  |
| ACCUMULATION_ALLOWED | VARCHAR2(1) | Y |  |
| MIN_LEAVES | NUMBER(5,2) | Y |  |
| NEGATIVE_ALLOWED | VARCHAR2(1) | Y |  |
| MAX_NEGATIVE_LEAVES | NUMBER(5) | Y |  |
| LEAVE_CASE | VARCHAR2(1) | Y |  |
| ALLOWED_IN_PROBATION | VARCHAR2(1) | Y |  |
| APPLY_IN_PROBATION | VARCHAR2(1) | Y |  |
| YEAR_TYPE | VARCHAR2(1) | Y |  |
| SEX_REQUIRED | NUMBER(1) | Y |  |
| MARITAL_STATUS_ID | VARCHAR2(6) | Y |  |
| LEAV_HOURS | VARCHAR2(2) | Y |  |
| LEAVE_FLAG | VARCHAR2(1) | Y |  |
| OFF_DAY_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| SHORT_LEAVE_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| YEARLY_LEAVE | VARCHAR2(1) default 'N' | Y | Based on some year eg. financial, calender, Employee year |
| MARRIED_STATUS | VARCHAR2(1) default 'N' | Y |  |
| PARENT_LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| REPORT_SEQUENCE | NUMBER(3) default 0 | Y |  |
| SHORT_DESC | VARCHAR2(5) | N |  |
| HR_REP_ORDER | NUMBER(3) | Y |  |
| ADVANCE_PERIOD_ALLOWED | CHAR(1) default 'N' | N | Store Y or N to check leave can be applied in advance or not |
| ADVANCE_PERIOD_DAYS | NUMBER(3) | Y |  |
| BACK_ENTRY_DAYS | NUMBER(3) default 0 | N |  |
| FUTURE_ENTRY_DAYS | NUMBER(4) default 0 | Y |  |
| EMPLOYEE_CAN_FEED | CHAR(1) default 'N' | N |  |
| CHECK_LEAVE_BALANCE | CHAR(1) default 'Y' | Y | Either check Leave Balance or not. |
| DISPLAY_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| REQUIRE_LEAVE_REASON | CHAR(1) default 'N' | Y |  |
| CONVERT_INTO_UNPAID | CHAR(1) default 'N' | Y |  |
| LFA_BEFORE_MONTH | NUMBER(2) | Y |  |
| LFA_AFTER_MONTH | NUMBER(2) | Y |  |
| CARRIED_FORWARD | CHAR(1) default 'N' | Y | This column use for Carried farward leave from previous year |
| LEAVE_ENTITLEMENTS_FOR | CHAR(1) default 'Y' | Y | The purpose of this column define leave is yearly or monthly |
| CARRY_FORWARD_LIMIT | NUMBER(3) default 0 | N | the purpose of this column define limit to carry forward to next year |
| HIERARCHY_REQUIRED | CHAR(1) | Y | This column required for leave hierarchy setup form (S07FRM00431) |
| SPECIAL_LEAVE_SETUP | CHAR(1) | Y |  |
| EHC_CAN_ENTER | CHAR(1) default 'N' | Y | This colum will be use for EHC physician Right on leave they can enter |

- **PK** `PK_LEAVE_TYPE`: LEAVE_TYPE_ID
- **UK** `UK_LEAVE_TYPE`: DESCRIPTION
- **UK** `UK_LEAVE_TYPE_001`: SHORT_DESC
- **CHECK** `CK_LEAVE_TYPE_001`: EMPLOYEE_CAN_FEED IN ('N','Y')
- **CHECK** `CK_LEAVE_TYPE_1`: ADVANCE_PERIOD_ALLOWED IN ('Y','N')
- **CHECK** `CK_LEAVE_TYPE_2`: CHECK_LEAVE_BALANCE IN ('N','Y')
- **Triggers**: `LEAVE_TYPE_DEL` (after delete), `LEAVE_TYPE_INS` (before insert), `LEAVE_TYPE_UPD` (before update)

## HRD.ADJOINT_LEAVE
Store infromation about leaves that can be adjoint with other leaves

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Store main leave type id Ex/ 011 for Casual leave |
| ADJOINT_LEAVE_TYPE_ID | VARCHAR2(3) | N | Store leave type id that can be adoint with main leave type id |
| REMARKS | VARCHAR2(200) | Y | Store remarks |

- **PK** `PK_ADJOINT_LEAVE`: LEAVE_TYPE_ID, ADJOINT_LEAVE_TYPE_ID
- **FK** `FK_ADJOINT_LEAVE`: (LEAVE_TYPE_ID) -> HRD.LEAVE_TYPE(LEAVE_TYPE_ID)
- **Triggers**: `ADJOINT_LEAVE_DEL` (after delete), `ADJOINT_LEAVE_INS` (before insert), `ADJOINT_LEAVE_UPD` (before update)

## HRD.ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | VARCHAR2(3) | N | Store unique alert Id |
| DESCRIPTION | VARCHAR2(80) | N | Store alert description |
| SUBJECT | VARCHAR2(80) | Y | Store email subject |
| ACTIVE | VARCHAR2(1) default 'Y' | Y | Store alert status as 'Y' for active and 'N' for inactive |
| ATTACHMENT | VARCHAR2(1) | Y | Store whether an attachment will be send in email or not |
| QUERY_NAME | VARCHAR2(100) | Y | Store query name as called in XML file |
| QUERY_STRING | VARCHAR2(4000) | Y | Store query on which alert will be send |
| INSERTION_REQUIRED | VARCHAR2(1) default 'N' | Y | Y: A Row will be inserted in table for which email has been generated successfully. |
| EXECUTION_UNIT | CHAR(1) | Y | THIS COLUMN CONTAINS VALUE LIKE YEARLY,MONTHLY,WEEKLY,DAILY,ALTERNATE DAYS |
| ALERT_START_DATE | DATE | Y | THIS COLUMN CONTAINS ALERT START DATE |
| ALERT_END_DATE | DATE | Y | THIS COLUMN CONTAINS ALERT END DATE |
| DAY_GAP | NUMBER | Y |  |
| ALERT_SENDING_TYPE | CHAR(1) default 'E' | Y | This column contains information abount the lert that whether it will send in list , department wise or all |
| DEPARTMENT_ID | VARCHAR2(7) | Y | This column contains organizing/owner department of the alert. |
| SECTION_ID | VARCHAR2(7) | Y | This column contains organizing/owner section of the alert. |
| EXECUTION_PER_DAY | NUMBER | Y | This column contains information that how many times jobs will execute on each day. |
| EXECUTION_TIME | VARCHAR2(5) | Y | This column contains information that when will the job be executed. |
| TIME_GAP | NUMBER | Y | This column contains information that after how many hours job will execute again on same day. |
| EXECUTE_JOB | CHAR(1) default 'N' | Y | This column will be used for job activitation |
| MAIL_TO_DEPT_HEAD | CHAR(1) default 'N' | Y | this column will be used to decide whether mail forwarded to department head or not |
| MAIL_TO_SELF | CHAR(1) default 'N' | Y | this column will be used to decide whether mail forwarded to self or not |
| TRN_STATUS | VARCHAR2(3) | Y |  |
| PENDING_QUEUE | CHAR(1) default 'N' | Y | this column will be used to make a alert pending queue |
| IS_MANDATORY_ON_JOINING | CHAR(1) | Y | IS_MANDATORY_QUIZ_ON_JOINING |
| MAIL_TO_ORGANIZERS | CHAR(1) default 'N' | Y |  |
| CC_ORGANIZERS | CHAR(1) default 'N' | Y |  |
| IS_SUPERVISOR_HIERARCHY | CHAR(1) default 'N' | Y |  |
| MAIL_TO_SUPERVISOR | CHAR(1) default 'N' | Y |  |
| IS_ONCALL_ROSTER_ALERT | CHAR(1) default 'N' | Y |  |
| IS_DOCUMENT_DASHBOARD | CHAR(1) default 'N' | Y |  |
| DOCUMENT_CATEGORY_ID | NUMBER | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| GEN_PRIVILEGES_QUEUE | CHAR(1) default 'N' | Y |  |
| EXECUTE_JOB_MANUALY | CHAR(1) default 'N' | Y |  |

- **PK** `PK_ALERTS`: ALERT_ID
- **CHECK** `CHK_ALERTS_1`: ACTIVE IN ('N','Y')
- **Triggers**: `ALERTS_DEL` (after delete), `ALERTS_INS` (before insert), `ALERTS_UPD` (before update)

## HRD.ALERTS_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(4) | N | Store unique number |
| ALERT_ID | VARCHAR2(3) | N | Store alert Id |
| HEADER | VARCHAR2(2000) | Y | Store text that will appear as header in email like Dear XYZ |
| FOOTER | VARCHAR2(2000) | Y | Store text that will appear as footer in email |
| SIGNATURE | VARCHAR2(600) | Y | Store text that will appear as signature of email like Regards Shumaila Aziz |
| ATTACHMENT_PATH | VARCHAR2(4000) | Y | Store file path that will linked with specified alert |
| SENDER_EMAIL | VARCHAR2(60) | Y | Store email sender mail address like shumaila@skm.org.pk |
| ACTIVE | CHAR(1) default 'Y' | Y | Store alert status as 'Y' for active and 'N' for inactive |
| MESSAGE | VARCHAR2(2000) | Y | Store message of email |
| REMARKS | VARCHAR2(1000) | Y |  |
| TABLE_COLUMN_HEADINGS | VARCHAR2(4000) | Y | this column will be used for HTML header names |
| TABLE_COLUMN_COUNT | NUMBER | Y | this column will be used for HTML header COUNT |

- **PK** `PK_ALERTS_DETAIL`: SERIAL_NO, ALERT_ID
- **FK** `FK_ALERTS_DETAIL`: (ALERT_ID) -> HRD.ALERTS(ALERT_ID) [disabled]
- **CHECK** `CHK_ALERTS_DETAIL_1`: ACTIVE IN ('N','Y')

## HRD.ALERT_RECIPIENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | VARCHAR2(3) | N | Store alert Id |
| DEPARTMENT_ID | VARCHAR2(7) | N | Store department id |
| REQ_DESIG_ID | VARCHAR2(6) | N | Store requesting designation Id |
| RECIPIENT_DESIG_ID | VARCHAR2(6) | Y | Store recipient designation Id |
| RECIPIENT_CODE | VARCHAR2(14) | N | Store recipient employee code |
| RECIPIENT_EMAIL | VARCHAR2(100) | Y | Store recipient email address (Like To field).Separate multiple email addresses by semicolon ';' |
| ACTIVE | CHAR(1) default 'Y' | Y | Store 'Y' for active and 'N' for inactive for current record status |
| CC_EMAIL | VARCHAR2(300) | Y | Store CC email addresses. Separate multiple email addresses by semicolon ';' |
| BCC_EMAIL | VARCHAR2(1000) | Y | Store BCC email addresses.Separate multiple email addresses by semicolon ';' |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_ALERT_RECIPIENT`: ALERT_ID, DEPARTMENT_ID, REQ_DESIG_ID, RECIPIENT_CODE
- **FK** `FK_ALERT_RECIPIENT_1`: (ALERT_ID) -> HRD.ALERTS(ALERT_ID)
- **CHECK** `CHK_ALERT_RECIPIENT_1`: ACTIVE IN ('N','Y')
- **Triggers**: `ALERT_RECIPIENTS_DEL` (after delete), `ALERT_RECIPIENTS_INS` (before insert), `ALERT_RECIPIENTS_UPD` (before update)

## HRD.ALERT_RECIPIENTS_DEPT_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | VARCHAR2(3) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| RECIPIENT_DESIG_ID | VARCHAR2(6) | Y |  |
| RECIPIENT_CODE | VARCHAR2(14) | N |  |
| RECIPIENT_EMAIL | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CC_EMAIL | VARCHAR2(300) | Y |  |
| BCC_EMAIL | VARCHAR2(1000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| EMAIL_TYPE | CHAR(1) | Y |  |

- **Triggers**: `ALERT_RECIPIENTS_DEPT_WISE_DEL` (after delete), `ALERT_RECIPIENTS_DEPT_WISE_INS` (before insert), `ALERT_RECIPIENTS_DEPT_WISE_UPD` (before update)

## HRD.ALERT_RECIPIENTS_EMP_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | VARCHAR2(3) | N |  |
| RECIPIENT_DESIG_ID | VARCHAR2(6) | Y |  |
| RECIPIENT_CODE | VARCHAR2(14) | N |  |
| RECIPIENT_EMAIL | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CC_EMAIL | VARCHAR2(300) | Y |  |
| BCC_EMAIL | VARCHAR2(1000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| EMAIL_TYPE | CHAR(1) | Y |  |

- **Triggers**: `ALERT_RECIPIENTS_EMP_WISE_DEL` (after delete), `ALERT_RECIPIENTS_EMP_WISE_INS` (before insert), `ALERT_RECIPIENTS_EMP_WISE_UPD` (before update)

## HRD.FINANCIAL_YEAR

| Column | Type | Null | Comment |
|---|---|---|---|
| FIN_YEAR | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FORMULA_COMMENTS | VARCHAR2(2000) | Y |  |

- **PK** `PK_FINANCIAL_YEAR`: FIN_YEAR
- **Triggers**: `FINANCIAL_YEAR_CEA` (before insert or update or delete), `TRG_WS_LUV_PU_ZC_Q` (after insert or update or delete)

## HRD.ANNUAL_PERFORMANCE_SHARE

| Column | Type | Null | Comment |
|---|---|---|---|
| PERFORMANCE_TYPE_ID | VARCHAR2(3) | N |  |
| FIN_YEAR | VARCHAR2(6) | N |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_ANNUAL_PERFORMANCE_SHARE`: PERFORMANCE_TYPE_ID, FIN_YEAR
- **FK** `FK_ANNUAL_PERFORMANCE_SHARE_1`: (FIN_YEAR) -> HRD.FINANCIAL_YEAR(FIN_YEAR) [disabled]

## HRD.PRODUCT
Store product description exists in marketing department

| Column | Type | Null | Comment |
|---|---|---|---|
| PRODUCT_ID | VARCHAR2(5) | N | Store unique product id Ex 00001 |
| DESCRIPTION | VARCHAR2(60) | Y | Store product description like Zakat, Co-branding |
| ACTIVE | CHAR(1) | Y | Store product status as Y for active and N for inactive |

- **PK** `PK_PRODUCT`: PRODUCT_ID
- **Triggers**: `PRODUCT_CEA` (before insert or update or delete), `TRG_WS_BEH_BG_EJ_Q` (after insert or update or delete)

## HRD.ANNUAL_PRODUCT

| Column | Type | Null | Comment |
|---|---|---|---|
| FIN_YEAR | VARCHAR2(6) | N |  |
| PRODUCT_ID | VARCHAR2(5) | N |  |

- **PK** `PK_ANNUAL_PRODUCT`: FIN_YEAR, PRODUCT_ID
- **FK** `FK_ANNUAL_PRODUCT_1`: (PRODUCT_ID) -> HRD.PRODUCT(PRODUCT_ID) [disabled]
- **FK** `FK_ANNUAL_PRODUCT_2`: (FIN_YEAR) -> HRD.FINANCIAL_YEAR(FIN_YEAR)

## HRD.REGION
Store region definition

| Column | Type | Null | Comment |
|---|---|---|---|
| REGION_ID | VARCHAR2(3) | N | Store unique region id Ex  001 |
| DESCRIPTION | VARCHAR2(60) | Y | Store region description ex South |
| ACTIVE | CHAR(1) | Y | Store region status as Y for active and N for inactive |

- **PK** `PK_REGION`: REGION_ID
- **Triggers**: `REGION_CEA` (before insert or update or delete), `TRG_WS_FLI_YP_UG_Q` (after insert or update or delete)

## HRD.ANNUAL_PRODUCT_REGION_TARGET

| Column | Type | Null | Comment |
|---|---|---|---|
| FIN_YEAR | VARCHAR2(6) | N |  |
| PRODUCT_ID | VARCHAR2(5) | N |  |
| REGION_ID | VARCHAR2(3) | N |  |
| TARGET | NUMBER(12,2) | Y |  |
| ACTUAL | NUMBER(12,2) | Y |  |

- **PK** `PK_ANUAL_PRODUCT_REGION_TARGET`: FIN_YEAR, PRODUCT_ID, REGION_ID
- **FK** `FK_ANUAL_PROD_REGION_TARGETS_1`: (REGION_ID) -> HRD.REGION(REGION_ID) [disabled]
- **FK** `FK_ANUAL_PROD_REGION_TARGETS_2`: (FIN_YEAR, PRODUCT_ID) -> HRD.ANNUAL_PRODUCT(FIN_YEAR, PRODUCT_ID)

## HRD.CAMPAIGN_ROLE

| Column | Type | Null | Comment |
|---|---|---|---|
| ROLE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CAMPAIGN_ROLE`: ROLE_ID

## HRD.JOB_LEAVING_REASON
Store possible reasons of  job leaving reason

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(3) | N | Store Unique reason id Ex 001 |
| DESCRIPTION | VARCHAR2(60) | Y | Store reason id description Ex Expiry of Contract for 001 |
| ACTIVE | VARCHAR2(1) default 'Y' | Y | Store either Y or N to indicate reason status as active or inactive respectively |
| SHORT_DESC | VARCHAR2(5) | Y | Store short description of reason description Ex  EOC for Expiry of Contract |
| IS_INCLUDE_HRREPORT | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_JOB_LEAVING_REASON`: REASON_ID
- **UK** `UK_JOB_LEAVING_REASON_001`: DESCRIPTION
- **Triggers**: `JOB_LEAVING_REASON_CEA` (before insert or update or delete), `JOB_LEAVING_REASON_DEL` (after delete), `JOB_LEAVING_REASON_INS` (before insert), `JOB_LEAVING_REASON_UPD` (before update), `TRG_WS_NGE_KK_DJ_Q` (after insert or update or delete)

## HRD.LEAVE_ROLE

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_ROLE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_LEAVE_ROLE`: LEAVE_ROLE_ID

## HRD.SHIFT_TYPE
Store shift type existance detail

| Column | Type | Null | Comment |
|---|---|---|---|
| SHIFT_TYPE_ID | VARCHAR2(1) | N | Store shift type id as S or N |
| DESCRIPTION | VARCHAR2(60) | Y | Store shift description as Shift or Non Shift |

- **PK** `PK_SHIFT_TYPE`: SHIFT_TYPE_ID
- **Triggers**: `SHIFT_TYPE_DEL` (after delete), `SHIFT_TYPE_INS` (before insert), `SHIFT_TYPE_UPD` (before update)

## HRD.TR_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_ID | NUMBER(10) | N |  |
| HIERARCHY_DESCRIPTION | VARCHAR2(255) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| HIERARCHY_TYPE | CHAR(1) | Y | 'N' NON-CONSULTANTS, 'C' CONSULTANTS |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `TRH_ID_PK`: HIERARCHY_ID
- **Triggers**: `TRG_WS_TSN_UL_JM_Q` (after insert or update or delete), `TR_HIERARCHY_CEA` (before insert or update or delete), `TR_HIERARCHY_DEL` (after delete), `TR_HIERARCHY_INS` (before insert), `TR_HIERARCHY_UPD` (before update)

## HRD.CONTRACT_TYPE
Store different contract types that can be associated with employees

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_TYPE_ID | VARCHAR2(3) | N | Store unique contract type id |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| PROBATION_PERIOD | NUMBER(3) | Y |  |
| MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) | Y | Store Y or N to allow medical facilities to spouse |
| NO_OF_CHILDREN_ALLOWED | NUMBER(2) default 0 | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y | Store current status of contract, if it is in use then this field will be Y else N |
| CONTRACT_PERIOD | NUMBER(3) | Y |  |

- **PK** `PK_CONTRACT_TYPE`: CONTRACT_TYPE_ID
- **UK** `UK_CONTRACT_TYPE_001`: DESCRIPTION
- **Triggers**: `CONTRACT_TYPE_CEA` (before insert or update or delete), `CONTRACT_TYPE_DEL` (after delete), `CONTRACT_TYPE_INS` (before insert), `CONTRACT_TYPE_UPD` (before update), `TRG_WS_FWH_ZV_ZQ_Q` (after insert or update or delete)

## HRD.EMPLOYEE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_TYPE_ID | VARCHAR2(1) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_EMPLOYEE_TYPE`: EMPLOYEE_TYPE_ID
- **Triggers**: `EMPLOYEE_TYPE_CEA` (before insert or update or delete), `EMPLOYEE_TYPE_DEL` (after delete), `EMPLOYEE_TYPE_INS` (before insert), `EMPLOYEE_TYPE_UPD` (before update), `TRG_WS_QAG_GE_UT_Q` (after insert or update or delete)

## HRD.INFORMATION
Store information about employees

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | Y | Store current designation code of employee on which he/she is working |
| MRNO | VARCHAR2(14) | N | Store unique employee code |
| CONTRACT_ID | VARCHAR2(6) | Y | Store contract code of employee |
| EMPLOYEE_TYPE | VARCHAR2(1) | Y | Store employee type |
| GRADE_ID | VARCHAR2(6) | Y | Store grade Id of employee |
| DEPARTMENT_ID | VARCHAR2(7) | Y | Store current depatment |
| JOINING_DATE | DATE | Y | Store  date on which employee gives his/her joining to organization |
| PROBATION_PERIOD_DAYS | NUMBER(3) default 0 | Y | Store probation days of employees |
| LEAVING_DATE | DATE | Y | Store date on which employee leaves the oragnization |
| SERVICE_BOND_WITH_PREV_EMPL | NUMBER(1) default 1 | Y |  |
| PREPARE_TO_WORK_ANYWHERE_IN_PK | NUMBER(1) default 1 | Y | Store either Y or N to i ndicate employee can work outside the organization in special circumstances |
| PREPARE_FOR_EXTENSIVE_TRAVEL | NUMBER(1) default 1 | Y | Store either Y or N to i ndicate employee can go outside station for official tasks |
| HAVE_DRIVING_LICENCE | NUMBER(1) default 1 | Y | Store either Y or N to i ndicate employee possess driving license or not |
| EVER_DISMISSED_OR_ASK_TO_LEAVE | NUMBER(1) default 1 | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(3) | N | Master location id refer from ORDERENTRY.ORDER_LOCATION |
| MAY_SKMT_APPROACH_EMPLOYER_NOW | NUMBER(1) default 1 | Y |  |
| NATIONALITY | NUMBER(4) | N | Store nationality possessed by the employee |
| ACTIVE | VARCHAR2(1) default 'Y' | N | Store either Y or N to indicate status of employee as active or inactive respectively |
| CONTRACT_TYPE_ID | VARCHAR2(3) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| PARAMEDICAL_STAFF | VARCHAR2(1) default 'Y' | Y |  |
| SHIFT_TYPE_ID | VARCHAR2(1) | Y |  |
| CONFIRMATION_DATE | DATE | Y | Store date on which employee service is confirmed usually after completion of probation |
| CONTRACT_START_DATE | DATE | Y | Store contract start date of employee |
| CONTRACT_END_DATE | DATE | Y | Store contract end date of employee |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| SALARY | NUMBER(12,2) | Y | Store basic salary of employee |
| DISCIPLINARY_ACTION | VARCHAR2(1) default 'N' | Y |  |
| HIRE_TYPE | VARCHAR2(1) default 'R' | Y |  |
| PREDECESSOR_MRNO | VARCHAR2(14) | Y |  |
| BUDGET_TYPE | VARCHAR2(1) default 'B' | Y | Store position type of employee as Budgeted or Non Budgeted |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| CHILDREN_MEDICAL_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| INTERNAL_EMAIL | VARCHAR2(30) | Y | Store internal email of employee Ex abc@skm.org.pk |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y | Store patient type id associated with employee Ex 001003 for Employee(Regular) |
| SECTION_ID | VARCHAR2(7) default '0010001' | N | Store section id of department where employee is working |
| WORKING_AREA_ID | VARCHAR2(7) | Y | Store working area id of section where employee is working |
| FAMILY_CODE | VARCHAR2(15) | Y |  |
| MANAGER_MRNO | VARCHAR2(14) | Y | Store manager code of employee |
| LEAVE_ROLE_ID | VARCHAR2(3) | Y | Store leave role associated with employee |
| PMDC_PNC_NO | VARCHAR2(11) | Y |  |
| PMDC_PNC_DATE | DATE | Y |  |
| BLACK_LISTED | CHAR(1) default 'N' | Y |  |
| EMAIL | VARCHAR2(60) | Y | Store email of employee |
| NEW_JOINING_FOR_LEAVES | DATE | Y |  |
| TRANSPORT_ALLOWED | CHAR(1) | Y |  |
| TRANSPORT_ROUTE_ID | VARCHAR2(3) | Y |  |
| TRANSPORT_ALLOWED_EMERGENCY | CHAR(1) | Y |  |
| TRANSPORT_COMMENTS | VARCHAR2(500) | Y |  |
| HR_REFFERNCE | VARCHAR2(25) | Y |  |
| APPOINTMENT_DATE | DATE | Y |  |
| NOTICE_PERIOD_DAYS | NUMBER(4,2) | Y |  |
| TRANSPORT_ALLOWANCE | CHAR(1) | Y |  |
| LFA_ALLOWED | CHAR(1) default 'Y' | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| RFID_CODE | VARCHAR2(30) | Y |  |
| SSC_DEDUCTION | VARCHAR2(1) default 'N' | Y |  |
| SSC_START_DATE | DATE | Y |  |
| SSC_NO | VARCHAR2(25) | Y |  |
| TRAVEL_HIERARCHY_ID | NUMBER(10) | Y |  |
| RFID_SUPER_CARD | CHAR(1) default 'N' | Y | Store information about employee RFID card is super card or not. |
| NAME | VARCHAR2(255) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y | Store current designation of employee on which he/she is working |
| EMP_NATURE_TYPE | CHAR(1) | Y | 'C' CONSULTANT ,'D' DOCTOR, 'N' NURSE.'O' OTHER |
| CONTRACT_TEMPLATE_ID | VARCHAR2(7) | Y | STORE CONTRACT LEETER TYPE PROVIDED AT JOINING |
| CONTRACT_CHANGE_REMARKS | VARCHAR2(4000) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains ATTACHMENT DESCRIPTION |
| MEDICAL_DATE | DATE | Y | THIS COLUMN CONTAINS EMPLOYEE MEDICAL DATE FOR OSV PURPOSE. |
| PATIENT_MRNO | VARCHAR2(14) | Y |  |
| IS_OSV_REQUIRED | CHAR(1) default 'N' | Y | This column contains OSV REQUIRED OR NOR Y OR N |
| OSV_TYPE | CHAR(1) default 'N' | Y | This column contains OSV TYPE DEGREE, LICENSE, BOTH OR NA |
| SENIOR_INSTRUCTOR | CHAR(1) default 'N' | Y | This column contains the information if the employee is an instructor or not (Y = Instructor , N = Not an Instructor) |
| ANCILLARY_WORKER | CHAR(1) default 'N' | Y | This column contains the information if the employee is an Ancillary_Worker or not (Y = Ancillary_Worker, N = Not an Ancillary_Worker) |
| PARAMEDICAL | CHAR(1) default 'N' | Y | This column contains the information if the employee is a Paramedical or not (Y = Paramedical, N = Not an Paramedical) |
| ALPHANUMERIC_RFID_CODE | VARCHAR2(50) | Y |  |

- **PK** `PK_INFORMATION`: MRNO
- **UK** `UK_INFORMATION_1`: HR_REFFERNCE
- **UK** `UK_INFORMATION_2`: RFID_CODE
- **FK** `FK_HIERARCHY_ID`: (TRAVEL_HIERARCHY_ID) -> HRD.TR_HIERARCHY(HIERARCHY_ID) [disabled]
- **FK** `FK_INFORMATION_1`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **FK** `FK_INFORMATION_10`: (LEAVE_ROLE_ID) -> HRD.LEAVE_ROLE(LEAVE_ROLE_ID) [disabled]
- **FK** `FK_INFORMATION_11`: (TRANSPORT_ROUTE_ID) -> DEFINITIONS.TRANSPORT_ROUTE(TRANSPORT_ROUTE_ID) [disabled]
- **FK** `FK_INFORMATION_12`: (DUTY_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_INFORMATION_2`: (GRADE_ID) -> DEFINITIONS.GRADES(GRADE_ID)
- **FK** `FK_INFORMATION_3`: (CONTRACT_TYPE_ID) -> HRD.CONTRACT_TYPE(CONTRACT_TYPE_ID)
- **FK** `FK_INFORMATION_4`: (REASON_ID) -> HRD.JOB_LEAVING_REASON(REASON_ID)
- **FK** `FK_INFORMATION_5`: (EMPLOYEE_TYPE) -> HRD.EMPLOYEE_TYPE(EMPLOYEE_TYPE_ID)
- **FK** `FK_INFORMATION_6`: (SHIFT_TYPE_ID) -> HRD.SHIFT_TYPE(SHIFT_TYPE_ID)
- **FK** `FK_INFORMATION_7`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_INFORMATION_8`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **CHECK** `CHK_INF_ACTIVE`: ACTIVE IN ('H','Y','N')
- **CHECK** `CK_INFORMATION_001`: DISCIPLINARY_ACTION IN ('Y','N')
- **CHECK** `CK_INFORMATION_002`: HIRE_TYPE IN ('R','N')
- **CHECK** `CK_INFORMATION_003`: BUDGET_TYPE IN ('B','A')
- **CHECK** `CK_INFORMATION_004`: SPOUSE_MEDICAL_ALLOWED IN ('N','Y')
- **CHECK** `CK_INFORMATION_005`: CHILDREN_MEDICAL_ALLOWED IN ('N','Y')
- **CHECK** `CK_INFORMATION_1`: CARD_SWIPE_EXEMPTION IN ('N','Y', 'O')
- **CHECK** `CK_INFORMATION_2`: LFA_ALLOWED IN( 'Y','N')
- **Triggers**: `CURRENT_EMPLOYEE_UPDATE` (after update), `INFORMATION_CEA` (before insert or update or delete), `INFORMATION_DEL` (after delete), `INFORMATION_INS` (before insert), `INFORMATION_UPD` (before update), `INFORMATION_UPD_ACTIVE` (after update of active), `INFORMATION_UPD_MANAGER_MRNO` (after update of manager_mrno), `INFORMATION_UPD_RFID_CODE` (after update of rfid_code), `INFORMATION_UPD_RFID_SUP_CARD` (after update of rfid_super_card), `TRG_WS_LFC_GU_AT_Q` (after insert or update or delete)

## HRD.ANNUAL_PRODUCT_INCENTIVE_PLAN

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| FIN_YEAR | VARCHAR2(6) | N |  |
| PRODUCT_ID | VARCHAR2(5) | N |  |
| REGION_ID | VARCHAR2(3) | N |  |
| ROLE_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| ROT | NUMBER(12,2) | Y |  |
| AA | NUMBER(12,2) | Y |  |
| PR | NUMBER(12,2) | Y |  |
| CAF | NUMBER(12,2) | Y |  |
| TW | NUMBER(12,2) | Y |  |
| PWA | NUMBER(12,2) | Y |  |
| FPA | NUMBER(12,2) | Y |  |
| PWB | NUMBER(12,2) | Y |  |
| FPB | NUMBER(12,2) | Y |  |
| APR | NUMBER(12,2) | Y |  |

- **PK** `PK_ANUAL_PROD_INCENTIVE_PLAN`: MRNO, FIN_YEAR, PRODUCT_ID, REGION_ID
- **FK** `FK_ANUAL_PROD_INCENTIVE_PLAN_1`: (ROLE_ID) -> HRD.CAMPAIGN_ROLE(ROLE_ID) [disabled]
- **FK** `FK_ANUAL_PROD_INCENTIVE_PLAN_2`: (FIN_YEAR, PRODUCT_ID, REGION_ID) -> HRD.ANNUAL_PRODUCT_REGION_TARGET(FIN_YEAR, PRODUCT_ID, REGION_ID) [disabled]
- **FK** `FK_ANUAL_PROD_INCENTIVE_PLAN_3`: (MRNO) -> HRD.INFORMATION(MRNO)

## HRD.ANNUAL_PROD_REGION_ROLE

| Column | Type | Null | Comment |
|---|---|---|---|
| FIN_YEAR | VARCHAR2(6) | N |  |
| PRODUCT_ID | VARCHAR2(5) | N |  |
| REGION_ID | VARCHAR2(3) | N |  |
| ROLE_ID | VARCHAR2(3) | N |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_ANNUAL_PROD_REGION_ROLE`: FIN_YEAR, PRODUCT_ID, REGION_ID, ROLE_ID
- **FK** `FK_ANNUAL_PROD_REGION_ROLE_1`: (FIN_YEAR, PRODUCT_ID, REGION_ID) -> HRD.ANNUAL_PRODUCT_REGION_TARGET(FIN_YEAR, PRODUCT_ID, REGION_ID)
- **FK** `FK_ANNUAL_PROD_REGION_ROLE_2`: (ROLE_ID) -> HRD.CAMPAIGN_ROLE(ROLE_ID) [disabled]

## HRD.APPLICANT_CONSULTANTS

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| APPLICANT_NAME | VARCHAR2(90) | Y |  |
| SPECIALITY_ID | NUMBER | Y |  |
| CONTACT_NO | VARCHAR2(50) | Y |  |
| EMAIL | VARCHAR2(50) | Y |  |
| ENTER_BY | VARCHAR2(14) | Y |  |
| ENTER_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| APPLICANT_TYPE | VARCHAR2(1) | Y | I for internal E for External |
| MRNO | VARCHAR2(14) | Y |  |
| STATUS | VARCHAR2(3) | Y | 1 FOR 'Forwarded to Physician' 2 FOR 'Received from Physician' 3 FOR 'Forwarded to Referee 4 Received from Referee' 5 for forwarded to PSB |
| VERIFICATION_REQ | CHAR(1) | Y |  |
| FRWD_PHYSICIAN_DATE | DATE | Y |  |
| RECD_PHYSICIAN_DATE | DATE | Y |  |
| FRWD_REFEREE_DATE | DATE | Y |  |
| RECD_REFEREE_DATE | DATE | Y |  |
| PSB_DATE | DATE | Y |  |
| REMINDER_NO | NUMBER | Y |  |
| PSB_STATUS | CHAR(1) | Y |  |
| COMMENTS | VARCHAR2(4000) | Y |  |
| EMAIL_ID | NUMBER(4) | Y |  |
| REMINDER_EMAIL_ID | NUMBER(4) | Y |  |
| INSTITUTE_NAME | VARCHAR2(100) | Y |  |

- **PK** `PK_APPLICANT_CONSULTANT`: APPLICANT_ID
- **Triggers**: `APPLICANT_CONSULTANTS_DEL` (after delete), `APPLICANT_CONSULTANTS_INS` (before insert), `APPLICANT_CONSULTANTS_UPD` (before update)

## HRD.APPLICANT_CONSULTANT_PRIVILEGE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| PRIVILEGE_ID | NUMBER | N |  |
| APP_EXEMPTED | CHAR(1) | Y |  |

- **PK** `PK_APPLICANT_CONS_PRIV`: APPLICANT_ID, PRIVILEGE_ID
- **FK** `FK_APPLICANT_CONS_PRIV`: (APPLICANT_ID) -> HRD.APPLICANT_CONSULTANTS(APPLICANT_ID)
- **Triggers**: `APP_CONSULTANT_PRIVILEGE_DEL` (after delete), `APP_CONSULTANT_PRIVILEGE_INS` (before insert), `APP_CONSULTANT_PRIVILEGE_UPD` (before update)

## HRD.APPLICANT_CONSULTANT_REF

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| PRIVILEGE_ID | NUMBER | N |  |
| PRIVILEGES_DETAIL_ID | NUMBER | Y |  |
| REFEREE_NAME | VARCHAR2(90) | Y |  |
| REFEREE_EMAIL | VARCHAR2(60) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| REFEREE_TYPE | CHAR(1) | Y |  |
| STATUS | CHAR(1) | Y | 'F' forward to referee 'R' Received from referee |
| REF_COMMENTS | VARCHAR2(2000) | Y |  |
| FORWARD_DATE | DATE | Y |  |
| RECEIVED_DATE | DATE | Y |  |
| REF_DECISION | CHAR(1) | Y | 'A'  ALL VERIFIED  'N' NONE OF THESE VERIFIED 'E' EXCEPT NO OF VERIFIED |
| DESIGNATION | VARCHAR2(200) | Y |  |
| DEPARTMENT | VARCHAR2(200) | Y |  |
| INSTITUTION | VARCHAR2(200) | Y |  |
| MAILING_ADDRESS | VARCHAR2(2000) | Y |  |
| CANCER_REGISTRY | CHAR(1) | Y |  |
| REMINDER_NO | NUMBER | Y |  |
| EMAIL_ID | NUMBER(4) | Y |  |
| REMINDER_EMAIL_ID | NUMBER(4) | Y |  |

- **PK** `PK_APPLICANT_REFEREE`: APPLICANT_ID, PRIVILEGE_ID, REFEREE_EMAIL
- **FK** `FK_APPLICANT_REF_01`: (APPLICANT_ID, PRIVILEGE_ID) -> HRD.APPLICANT_CONSULTANT_PRIVILEGE(APPLICANT_ID, PRIVILEGE_ID)
- **Triggers**: `APPLICANT_CONSULTANT_REF_DEL` (after delete), `APPLICANT_CONSULTANT_REF_INS` (before insert), `APPLICANT_CONSULTANT_REF_UPD` (before update)

## HRD.APPLICANT_EMPLOYMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(4) | N |  |
| COMPANY_NAME | VARCHAR2(300) | Y |  |
| COMPANY_CONTACT_NO | VARCHAR2(300) | Y |  |
| COMPANY_ADDRESS | VARCHAR2(1000) | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| STATE_ID | NUMBER(4) | Y |  |
| DISTRICT_ID | NUMBER(4) | Y |  |
| TEHSIL_ID | NUMBER(4) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| NAME_OF_SUPERVISOR | VARCHAR2(80) | Y |  |
| LEAVING_REASON_ID | VARCHAR2(3) | Y |  |
| RESPONSIBILITIES | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_APPLICANT_EMPLOYMENT`: APPLICANT_NO, SERIAL_NO
- **FK** `FK_APPLICANT_EMPLOYMENT_1`: (COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]
- **FK** `FK_APPLICANT_EMPLOYMENT_2`: (LEAVING_REASON_ID) -> HRD.JOB_LEAVING_REASON(REASON_ID) [disabled]
- **Triggers**: `APPLICANT_EMPLOYMENT_DEL` (after delete), `APPLICANT_EMPLOYMENT_INS` (before insert), `APPLICANT_EMPLOYMENT_UPD` (before update)

## HRD.RECEIVE_MEDIA

| Column | Type | Null | Comment |
|---|---|---|---|
| RECEIVE_MEDIA_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RECEIVE_MEDIA`: RECEIVE_MEDIA_ID
- **Triggers**: `RECEIVE_MEDIA_CEA` (before insert or update or delete), `RECEIVE_MEDIA_DEL` (after delete), `RECEIVE_MEDIA_INS` (before insert), `RECEIVE_MEDIA_UPD` (before update), `TRG_WS_HVT_VT_XG_Q` (after insert or update or delete)

## HRD.SOURCE_MEDIA

| Column | Type | Null | Comment |
|---|---|---|---|
| SOURCE_MEDIA_ID | VARCHAR2(7) | N | Store unique source media id |
| DESCRIPTION | VARCHAR2(300) | Y | Store source media from which applicant retreive vacany information ex. In response to ad etc |
| REMARKS | VARCHAR2(1000) | Y | Store user remarks |
| ACTIVE | CHAR(1) | Y | Store status of source media as 'Y' for active and 'N' for inactive |

- **PK** `PK_SOURCE_MEDIA`: SOURCE_MEDIA_ID
- **Triggers**: `SOURCE_MEDIA_CEA` (before insert or update or delete), `SOURCE_MEDIA_DEL` (after delete), `SOURCE_MEDIA_INS` (before insert), `SOURCE_MEDIA_UPD` (before update), `TRG_WS_QLH_CW_WM_Q` (after insert or update or delete)

## HRD.SOURCE_MEDIA_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(4) | N |  |
| SOURCE_MEDIA_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SOURCE_MEDIA_DETAIL`: SERIAL_NO, SOURCE_MEDIA_ID
- **FK** `FK_SOURCE_MEDIA_DETAIL`: (SOURCE_MEDIA_ID) -> HRD.SOURCE_MEDIA(SOURCE_MEDIA_ID) [disabled]
- **Triggers**: `SOURCE_MEDIA_DETAIL_DEL` (after delete), `SOURCE_MEDIA_DETAIL_INS` (before insert), `SOURCE_MEDIA_DETAIL_UPD` (before update)

## HRD.APPLICANT_INFORMATION

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N | Store 14 character unique applicant number |
| SERIAL_NO | NUMBER | N | Generate serial no for applicant information with respect to his/her registeration |
| POSITION_ID | VARCHAR2(6) | Y | Store position id for which applicant applied for job |
| DEPARTMENT_ID | VARCHAR2(7) | Y | Store department id in which position exists |
| DESIGNATION_ID | VARCHAR2(7) | Y | Store designation id from which position belongs to |
| APPLIED_DATE | DATE | Y | Store date on which applicant applied for job |
| STATUS_ID | VARCHAR2(6) | N | Store applicant status for specified position |
| REMARKS | VARCHAR2(3000) | Y | Store user remarks |
| ACTIVE | CHAR(1) | Y | Store status of position with respect to applicant as 'Y' for active and 'N' for inactive |
| CLEARANCE_DATE | DATE | Y | Store date on which applicant job status is cleared from HR department |
| SOURCE_MEDIA_ID | VARCHAR2(7) | Y | Store source media from which applicant retreive vacany information |
| MEDIA_SERIAL_NO | NUMBER(4) | Y | Store source media type from which applicant retreive vacany information |
| RECEIVE_MEDIA_ID | VARCHAR2(7) | Y | Store cv receiving media as received by HR department |
| MEDIA_COUNTRY_ID | NUMBER(4) | Y | Store source media country |
| MEDIA_STATE_ID | NUMBER(4) | Y | Store source media state |
| MEDIA_DISTRICT_ID | NUMBER(4) | Y | Store source media district |
| MEDIA_TEHSIL_ID | NUMBER(4) | Y | Store source media tehsil |

- **PK** `PK_APPLICANT_INFORMATION`: APPLICANT_NO, SERIAL_NO
- **FK** `FK_APPLICANT_INFORMATION_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_APPLICANT_INFORMATION_2`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **FK** `FK_APPLICANT_INFORMATION_3`: (MEDIA_SERIAL_NO, SOURCE_MEDIA_ID) -> HRD.SOURCE_MEDIA_DETAIL(SERIAL_NO, SOURCE_MEDIA_ID) [disabled]
- **FK** `FK_APPLICANT_INFORMATION_4`: (RECEIVE_MEDIA_ID) -> HRD.RECEIVE_MEDIA(RECEIVE_MEDIA_ID) [disabled]
- **FK** `FK_APPLICANT_INFORMATION_5`: (MEDIA_COUNTRY_ID, MEDIA_STATE_ID, MEDIA_DISTRICT_ID, MEDIA_TEHSIL_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]
- **Triggers**: `APPLICANT_INFORMATION_DEL` (after delete), `APPLICANT_INFORMATION_INS` (before insert), `APPLICANT_INFORMATION_UPD` (before update)

## HRD.APPLICANT_REGISTRATION

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N | Store 14 character unique applicant number |
| NAME | VARCHAR2(300) | N | Store applicant name |
| FATHER_NAME | VARCHAR2(300) | Y | Store applicant father's name |
| DATE_OF_BIRTH | DATE | Y | Store applicant date of birth |
| CONTACT_NO | VARCHAR2(300) | Y | Store applicant contact number(s) |
| ADDRESS | VARCHAR2(1000) | Y | Store applicant address; that is to be printed on CV acknowledgment letter |
| COUNTRY_ID | NUMBER(4) | Y | Store country id as belongs to address |
| STATE_ID | NUMBER(4) | Y | Store state id as belongs to address |
| DISTRICT_ID | NUMBER(4) | Y | Store district id as belongs to address |
| TEHSIL_ID | NUMBER(4) | Y | Store tehsil id as belongs to address |
| REGISTRATION_DATE | DATE | Y | Store date on which applicant is registered in system |
| REGISTERED_BY | VARCHAR2(14) | Y | Store employee code who register applicant in system |
| NIC | VARCHAR2(13) | Y | Store new NIC |
| FAMILY_CODE | VARCHAR2(6) | Y | Store family code as available on NIC |
| EMAIL | VARCHAR2(60) | Y | Store applicant email address |
| TITLE_ID | NUMBER(4) | Y |  |
| MRNO | VARCHAR2(14) | Y | Save employee code issued to applicant |

- **PK** `PK_APPLICANT_REGISTRATION`: APPLICANT_NO
- **FK** `FK_APPLICANT_REGISTRATION_1`: (COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]
- **FK** `FK_APPLICANT_REGISTRATION_2`: (TITLE_ID) -> MARKETING.DONOR_TITLE(TITLE_ID) [disabled]
- **FK** `FK_APPLICANT_REGISTRATION_3`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **Triggers**: `APPLICANT_REGISTRATION_DEL` (after delete), `APPLICANT_REGISTRATION_INS` (before insert), `APPLICANT_REGISTRATION_UPD` (before update)

## HRD.APPLICANT_OPEN_QUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N |  |
| SUBTYPE_ID | VARCHAR2(7) | N |  |
| QUESTION_TYPE_ID | VARCHAR2(7) | N |  |
| ANSWER | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_APPLICANT_OPEN_QUEST`: APPLICANT_NO, SUBTYPE_ID, QUESTION_TYPE_ID
- **FK** `FK_APPLICANT_OPEN_QUEST_1`: (APPLICANT_NO) -> HRD.APPLICANT_REGISTRATION(APPLICANT_NO)
- **FK** `FK_APPLICANT_OPEN_QUEST_2`: (SUBTYPE_ID, QUESTION_TYPE_ID) -> DEFINITIONS.OPEN_QUESTION_SUBTYPE(SUBTYPE_ID, QUESTION_TYPE_ID) [disabled]
- **Triggers**: `APPLICANT_OPEN_QUEST_DEL` (after delete), `APPLICANT_OPEN_QUEST_INS` (before insert), `APPLICANT_OPEN_QUEST_UPD` (before update)

## HRD.APPLICANT_PRIV_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| PRIVILEGES_ID | NUMBER | N |  |
| PRIVILEGES_DETAIL_ID | NUMBER | N |  |
| NUMBER_REQUIRED | NUMBER | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| BOLD | CHAR(1) | Y |  |
| SP_PRIVILEGE_ID | NUMBER | Y |  |
| PRIVILEGE_OFFERED | CHAR(1) | Y |  |
| PERFORMED_PROCEDURE | NUMBER | Y |  |
| REQUESTED | CHAR(1) default 'N' | Y |  |
| VERIFIED_YN | CHAR(1) default 'N' | Y |  |
| VERIFY_PERFOMED | NUMBER | Y |  |
| SR_NO | NUMBER | Y |  |
| GRANTED | CHAR(1) | Y |  |

- **PK** `PK_APPLICANT_PRIV_DETAIL`: APPLICANT_ID, PRIVILEGES_ID, PRIVILEGES_DETAIL_ID
- **FK** `FK_APPLICANT_PRIV_DET`: (APPLICANT_ID, PRIVILEGES_ID) -> HRD.APPLICANT_CONSULTANT_PRIVILEGE(APPLICANT_ID, PRIVILEGE_ID)
- **Triggers**: `APPLICANT_PRIV_DETAIL_DEL` (after delete), `APPLICANT_PRIV_DETAIL_INS` (before insert), `APPLICANT_PRIV_DETAIL_UPD` (before update)

## HRD.APPLICANT_SCANNED_DOCS

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(4) | N |  |
| TYPE_ID | VARCHAR2(7) | Y |  |
| SUBTYPE_ID | VARCHAR2(7) | Y |  |
| DOCUMENT | BLOB | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_APPLICANT_SCANNED_DOCS`: APPLICANT_NO, SERIAL_NO
- **FK** `FK_APPLICANT_SCANNED_DOCS_1`: (SUBTYPE_ID, TYPE_ID) -> DEFINITIONS.ATTACHMENT_SUBTYPE(SUBTYPE_ID, TYPE_ID) [disabled]
- **FK** `FK_APPLICANT_SCANNED_DOCS_2`: (APPLICANT_NO) -> HRD.APPLICANT_REGISTRATION(APPLICANT_NO)
- **Triggers**: `APPLICANT_SCANNED_DOCS_DEL` (after delete), `APPLICANT_SCANNED_DOCS_INS` (before insert), `APPLICANT_SCANNED_DOCS_UPD` (before update)

## HRD.APPLICANT_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_APPLICANT_STATUS`: STATUS_ID
- **Triggers**: `APPLICANT_STATUS_DEL` (after delete), `APPLICANT_STATUS_INS` (before insert), `APPLICANT_STATUS_UPD` (before update)

## HRD.STUDY_INSTITUTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| INSTITUTE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(225) | Y |  |
| ADDRESS | VARCHAR2(225) | Y |  |
| LOGO | BLOB | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_STUDY_INSTITUTIONS`: INSTITUTE_ID
- **FK** `FK_STUDY_INSTITUTIONS`: (COUNTRY_ID) -> DEFINITIONS.COUNTRY(COUNTRY_ID) [disabled]
- **Triggers**: `STUDY_INSTITUTIONS_CEA` (before insert or update or delete), `STUDY_INSTITUTIONS_DEL` (after delete), `STUDY_INSTITUTIONS_INS` (before insert), `STUDY_INSTITUTIONS_UPD` (before update), `TRG_WS_CAR_TE_HO_Q` (after insert or update or delete)

## HRD.STUDY_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DI | CHAR(1) default 'N' | Y |  |

- **PK** `PK_STUDY_TYPE`: TYPE_ID
- **UK** `UK_STUDY_TYPE_DESCRIPTION`: DESCRIPTION
- **Triggers**: `STUDY_TYPE_CEA` (before insert or update or delete), `STUDY_TYPE_DEL` (after delete), `STUDY_TYPE_INS` (before insert), `STUDY_TYPE_UPD` (before update), `TRG_WS_ICU_BL_GY_Q` (after insert or update or delete)

## HRD.STUDY_PROGRAMS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROGRAM_ID | VARCHAR2(10) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| TYPE_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DI | CHAR(1) default 'N' | Y |  |

- **PK** `PK_STUDY_PROGRAMS`: PROGRAM_ID
- **UK** `UK_STUDY_PROGRAMS_1`: DESCRIPTION
- **FK** `FK_STUDY_PROGRAMS_1`: (TYPE_ID) -> HRD.STUDY_TYPE(TYPE_ID) [disabled]
- **Triggers**: `STUDY_PROGRAMS_DEL` (after delete), `STUDY_PROGRAMS_INS` (before insert), `STUDY_PROGRAMS_UPD` (before update)

## HRD.APPLICANT_STUDY

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(4) | N |  |
| TYPE_ID | VARCHAR2(3) | Y |  |
| PROGRAM_ID | VARCHAR2(10) | Y |  |
| INSTITUTE_ID | NUMBER(4) | Y |  |
| SCALE_ID | VARCHAR2(3) | Y |  |
| SCALE_VALUE_ID | VARCHAR2(10) | Y |  |
| SESSION_START_DATE | DATE | Y |  |
| SESSION_END_DATE | DATE | Y |  |
| ROLL_NO | VARCHAR2(30) | Y |  |
| REGISTRATION_NO | VARCHAR2(60) | Y |  |
| ACHIEVEMENTS | VARCHAR2(1000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| OBTAINED_MARKS | NUMBER | Y |  |
| TOTAL_MARKS | NUMBER | Y |  |

- **PK** `PK_APPLICANT_STUDY`: APPLICANT_NO, SERIAL_NO
- **FK** `FK_APPLICANT_STUDY_1`: (TYPE_ID) -> HRD.STUDY_TYPE(TYPE_ID) [disabled]
- **FK** `FK_APPLICANT_STUDY_2`: (PROGRAM_ID) -> HRD.STUDY_PROGRAMS(PROGRAM_ID) [disabled]
- **FK** `FK_APPLICANT_STUDY_3`: (INSTITUTE_ID) -> HRD.STUDY_INSTITUTIONS(INSTITUTE_ID) [disabled]
- **Triggers**: `APPLICANT_STUDY_DEL` (after delete), `APPLICANT_STUDY_INS` (before insert), `APPLICANT_STUDY_UPD` (before update)

## HRD.STUDY_SUBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SUBJECT_ID | VARCHAR2(10) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DI | CHAR(1) default 'N' | Y |  |

- **PK** `PK_STUDY_SUBJECTS`: SUBJECT_ID
- **UK** `UK_STUDY_SUBJECTS_1`: DESCRIPTION
- **Triggers**: `STUDY_SUBJECTS_DEL` (after delete), `STUDY_SUBJECTS_INS` (before insert), `STUDY_SUBJECTS_UPD` (before update)

## HRD.APPLICANT_STUDY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_NO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(4) | N |  |
| SUBJECT_ID | VARCHAR2(10) | N |  |
| OBTAINED_MARKS | NUMBER | Y |  |
| TOTAL_MARKS | NUMBER | Y |  |
| DISTINCTION | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_APPLICANT_STUDY_DETAIL`: APPLICANT_NO, SERIAL_NO, SUBJECT_ID
- **FK** `FK_APPLICANT_STUDY_DETAIL_1`: (APPLICANT_NO, SERIAL_NO) -> HRD.APPLICANT_STUDY(APPLICANT_NO, SERIAL_NO)
- **FK** `FK_APPLICANT_STUDY_DETAIL_2`: (SUBJECT_ID) -> HRD.STUDY_SUBJECTS(SUBJECT_ID) [disabled]
- **Triggers**: `APPLICANT_STUDY_DETAIL_DEL` (after delete), `APPLICANT_STUDY_DETAIL_INS` (before insert), `APPLICANT_STUDY_DETAIL_UPD` (before update)

## HRD.APPLICANT_WISE_EMAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_EMAIL_ID | NUMBER | N |  |
| ALERT_ID | NUMBER(4) | Y |  |
| EMAIL_TEXT | VARCHAR2(100) | Y |  |
| EMAIL_TYPE_FLAGE | CHAR(1) | Y | R for referee P for Physian |
| REMINDER | CHAR(1) default 'N' | Y | this will be use is this email type is remider Y for reminder |
| INSTITUTE_REQUIRED | CHAR(1) default 'N' | Y |  |

- **PK** `PK_APPLICANT_WISE_EMAIL`: APPLICANT_EMAIL_ID
- **Triggers**: `APPLICANT_WISE_EMAIL_DEL` (after delete), `APPLICANT_WISE_EMAIL_INS` (before insert), `APPLICANT_WISE_EMAIL_UPD` (before update)

## HRD.REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(55) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_REASONS`: REASON_ID
- **Triggers**: `REASONS_CEA` (before insert or update or delete), `TRG_WS_NII_TM_ZE_Q` (after insert or update or delete)

## HRD.TIME_SPAN

| Column | Type | Null | Comment |
|---|---|---|---|
| TIME_ID | NUMBER(5) | N |  |
| REASON_ID | NUMBER(5) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_TIME_SPAN`: TIME_ID
- **FK** `FK_TIME_SPAN`: (REASON_ID) -> HRD.REASONS(REASON_ID) [disabled]

## HRD.AUTHORITY

| Column | Type | Null | Comment |
|---|---|---|---|
| TIME_ID | NUMBER(5) | N |  |
| APPRAISER | VARCHAR2(14) | N |  |
| APPRAISEE | VARCHAR2(14) | N |  |

- **PK** `PK_AUTHORITY`: TIME_ID, APPRAISER, APPRAISEE
- **FK** `FK_AUTHORITY`: (TIME_ID) -> HRD.TIME_SPAN(TIME_ID)
- **Triggers**: `AUTHORITY_DEL` (after delete), `AUTHORITY_INS` (before insert), `AUTHORITY_UPD` (before update)

## HRD.APPRISAL_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| APPRAISAL_ID | NUMBER(5) | N |  |
| TIME_ID | NUMBER(5) | Y |  |
| APPRAISER | VARCHAR2(14) | Y |  |
| APPRAISEE | VARCHAR2(14) | Y |  |
| STRENGTH_ACCOMPLISHMENT | VARCHAR2(500) | Y |  |
| WEAKNESS_SHORTAGE | VARCHAR2(500) | Y |  |
| APPRAISING_START_DATE | DATE | Y |  |
| APPRAISING_END_DATE | DATE | Y |  |
| APPRAISAL_ACCEPTANCE | CHAR(1) | Y |  |
| APPRAISAL_LOCK | CHAR(1) | Y |  |

- **PK** `PK_APPRISAL_MASTER`: APPRAISAL_ID
- **FK** `FK_APPRISAL_MASTER`: (TIME_ID, APPRAISER, APPRAISEE) -> HRD.AUTHORITY(TIME_ID, APPRAISER, APPRAISEE) [disabled]

## HRD.SCALE
Empty table

| Column | Type | Null | Comment |
|---|---|---|---|
| SCALE_ID | NUMBER(4) | N |  |
| MAX_LEVELS | NUMBER(2) | Y |  |
| DESCRIPTION | VARCHAR2(25) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SCALE`: SCALE_ID
- **Triggers**: `SCALE_CEA` (before insert or update or delete), `TRG_WS_YME_AH_DO_Q` (after insert or update or delete)

## HRD.EVALUATION_CRITERIA_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| EVALUATION_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(55) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_EVALUATION_CRITERIA_MASTER`: EVALUATION_ID

## HRD.EVAULATION_CRITERIA_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| EVALUATION_DETAIL_ID | NUMBER(5) | N |  |
| SCALE_ID | NUMBER(4) | Y |  |
| EVALUATION_ID | NUMBER(5) | Y |  |
| DESCRIPTION | VARCHAR2(55) | Y |  |
| DESCRIPTION_DEFINITION | VARCHAR2(150) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_EVAULATION_CRITERIA_DETAIL`: EVALUATION_DETAIL_ID
- **FK** `FK_EVLN_CRITERIA_DETAIL_1`: (SCALE_ID) -> HRD.SCALE(SCALE_ID) [disabled]
- **FK** `FK_EVLN_CRITERIA_DETAIL_2`: (EVALUATION_ID) -> HRD.EVALUATION_CRITERIA_MASTER(EVALUATION_ID) [disabled]

## HRD.RATIO

| Column | Type | Null | Comment |
|---|---|---|---|
| RATIO_ID | NUMBER(5) | N |  |
| SCALE_ID | NUMBER(4) | N |  |
| FROM_VALUE | NUMBER(2) | Y |  |
| TO_VALUE | NUMBER(2) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(55) | Y |  |
| LONG_DESCRIPTION | VARCHAR2(225) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RATIO`: RATIO_ID, SCALE_ID
- **FK** `FK_RATIO`: (SCALE_ID) -> HRD.SCALE(SCALE_ID) [disabled]

## HRD.APPRAISAL_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| APPRAISAL_ID | NUMBER(5) | N |  |
| EVALUATION_DETAIL_ID | NUMBER(5) | N |  |
| APPRAISAL_DETAIL_ID | NUMBER(5) | Y |  |
| SCALE_ID | NUMBER(4) | Y |  |
| SCORE | NUMBER(5) | Y |  |
| ADJESTED_SCORE | NUMBER(4) | Y |  |
| REMARKS | CHAR(18) | Y |  |

- **PK** `PK_APPRAISAL_DETAIL`: APPRAISAL_ID, EVALUATION_DETAIL_ID
- **FK** `FKAPPRAISAL_DETAIL`: (APPRAISAL_ID) -> HRD.APPRISAL_MASTER(APPRAISAL_ID)
- **FK** `FK_APPRAISAL_DETAIL`: (EVALUATION_DETAIL_ID) -> HRD.EVAULATION_CRITERIA_DETAIL(EVALUATION_DETAIL_ID) [disabled]
- **FK** `FK_APPRAISAL_DETAIL_2`: (SCORE, SCALE_ID) -> HRD.RATIO(RATIO_ID, SCALE_ID) [disabled]

## HRD.APP_CONSULTANT_REF_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| PRIVILEGE_ID | NUMBER | N |  |
| PRIVILEGES_DETAIL_ID | NUMBER | N |  |
| NO_PERFORMED_P | VARCHAR2(90) | Y |  |
| REFEREE_EMAIL | VARCHAR2(60) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| STATUS | CHAR(1) | Y |  |
| VERIFIED | CHAR(1) | Y |  |

- **PK** `PK_APP_CONS_REF_DTL`: APPLICANT_ID, PRIVILEGE_ID, PRIVILEGES_DETAIL_ID, REFEREE_EMAIL
- **FK** `FK_APPLICANT_REFEREE`: (APPLICANT_ID, PRIVILEGE_ID, REFEREE_EMAIL) -> HRD.APPLICANT_CONSULTANT_REF(APPLICANT_ID, PRIVILEGE_ID, REFEREE_EMAIL) [disabled]
- **Triggers**: `APP_CONSULTANT_REF_DTL_DEL` (after delete), `APP_CONSULTANT_REF_DTL_INS` (before insert), `APP_CONSULTANT_REF_DTL_UPD` (before update)

## HRD.APP_PSB_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| SIGNING_AUTHORITIES | CHAR(1) | Y | C for Chair PSB , D for Department Head, M forMedical Director |

- **Triggers**: `APP_PSB_HIERARCHY_DEL` (after delete), `APP_PSB_HIERARCHY_INS` (before insert), `APP_PSB_HIERARCHY_UPD` (before update)

## HRD.APP_PSB_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | Y |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| SIGNING_AUTHORITIES | CHAR(1) | Y | C for Chair PSB , D for Department Head, M forMedical Director |
| ORDER_BY | NUMBER | Y |  |

- **Triggers**: `APP_PSB_QUEUE_DEL` (after delete), `APP_PSB_QUEUE_INS` (before insert), `APP_PSB_QUEUE_UPD` (before update)

## HRD.ATTENDANCE_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| PROCESS_TYPE | VARCHAR2(3) | Y |  |
| PROCESS_ID | VARCHAR2(14) | Y |  |
| EMPLOYEE_TYPE_ID | VARCHAR2(3) | Y |  |
| FORM | VARCHAR2(60) | Y |  |
| PROCESS_FROM_DATE | DATE | Y |  |
| PROCESS_TO_DATE | DATE | Y |  |
| MONTH_DAYS | NUMBER(3) | Y |  |
| DUTY_DAYS | NUMBER(3) | Y |  |
| PROCESS_MONTH | VARCHAR2(15) | Y |  |

- **Triggers**: `ATTENDANCE_PARAMETERS_DEL` (after delete), `ATTENDANCE_PARAMETERS_INS` (before insert), `ATTENDANCE_PARAMETERS_UPD` (before update)

## HRD.ATTENDANCE_SHEET
Store attendance sheet of employee in accordance with card swipe

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | Store employee code |
| DUTY_DATE | DATE | N | Store duty date |
| SHIFT_ID | VARCHAR2(2) | Y | Store shift Id in which employee has to perform duty |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y | Store day type id Ex 001 for Duty Day |
| PROCESS_ID | VARCHAR2(12) | N | Store process id |
| ORIGIONAL_TIME_IN | DATE | Y | Store actual time in of employee |
| ORIGIONAL_TIME_OUT | DATE | Y | Store actual out of employee |
| ADJUSTED_TIME_IN | DATE | Y |  |
| ADJUSTED_TIME_OUT | DATE | Y |  |
| TOTAL_TIME | NUMBER(9) | Y | Store total time |
| OVER_TIME | NUMBER(9) | Y |  |
| VERIFIED_OVER_TIME | NUMBER(9) | Y |  |
| OVER_TIME_REASON | VARCHAR2(5) | Y |  |
| CTO | NUMBER(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| PROCESS_TYPE_ID | VARCHAR2(3) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) default 'N' | Y |  |
| SHIFT_TIME | NUMBER(5) default 0 | Y |  |
| OVER_TIME_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y | Store location ID from where employee perform duty like 001 for SKM |
| SHIFT_DESC | VARCHAR2(60) | Y | Duty timings in which employee  has to perform duty like morning, evening, night |
| LEAVE_TYPE_DESC | VARCHAR2(60) | Y | Store type of day like any leave day, duty day, weekly off etc |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) | Y |  |
| REASON_ID | VARCHAR2(3) | Y | This column use to cantain reason of card swipe |
| EMP_SHIFT_SR_NO | NUMBER(2) default 1 | N |  |
| DR_LOCATION_ID | VARCHAR2(3) | Y | This column will use to store the currenct duty roster location_id |

- **PK** `PK_ATTENDANCE_SHEET`: MRNO, DUTY_DATE, PROCESS_ID, EMP_SHIFT_SR_NO
- **CHECK** `CK_ATTENDANCE_SHEET_001`: SHORT_LEAVE IN ('N','Y')
- **CHECK** `CK_ATTENDANCE_SHEET_002`: OVER_TIME_ALLOWED IN ('Y','N')
- **Triggers**: `ATTENDANCE_SHEET_DEL` (after delete), `ATTENDANCE_SHEET_INS` (before insert), `ATTENDANCE_SHEET_UPD` (before update)

## HRD.ATTENDANCE_SHEET_OLD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DUTY_DATE | DATE | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y |  |
| ORIGIONAL_TIME_IN | DATE | Y |  |
| ORIGIONAL_TIME_OUT | DATE | Y |  |
| ADJUSTED_TIME_IN | DATE | Y |  |
| ADJUSTED_TIME_OUT | DATE | Y |  |
| TOTAL_TIME | NUMBER(5) | Y |  |
| OVER_TIME | NUMBER(5) | Y |  |
| VERIFIED_OVER_TIME | VARCHAR2(5) | Y |  |
| OVER_TIME_REASON | VARCHAR2(5) | Y |  |
| CTO | NUMBER(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| PROCESS_TYPE_ID | VARCHAR2(3) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |
| SHIFT_TIME | NUMBER(5) | Y |  |
| OVER_TIME_ALLOWED | VARCHAR2(1) | Y |  |

- **Triggers**: `ATTENDANCE_SHEET_OLD_DEL` (after delete), `ATTENDANCE_SHEET_OLD_INS` (before insert), `ATTENDANCE_SHEET_OLD_UPD` (before update)

## HRD.PROCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| MONTH | VARCHAR2(6) | Y |  |
| PROCESS_TYPE_ID | VARCHAR2(3) | Y |  |
| PROCESS_DATE | DATE | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| MONTH_DAYS | NUMBER(4) | Y |  |
| DUTY_DAYS | NUMBER(4) | Y |  |
| START_TIME | DATE | Y |  |
| END_TIME | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PROCESS`: PROCESS_ID
- **Triggers**: `PROCESS_DEL` (after delete), `PROCESS_INS` (before insert), `PROCESS_UPD` (before update)

## HRD.ATTENDANCE_SHEET_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| SUMMARY_PROCESS_ID | VARCHAR2(10) | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| DAYS_PERFORMED | NUMBER(5) | Y |  |
| ADDITIONAL_WORKING_DAYS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(5) | Y |  |
| ACTUAL_SHIFT_MINUTES | NUMBER(8) | Y |  |
| PERFORMED_MINUTES | NUMBER(8) | Y |  |
| CALCULATED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| APPROVED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| PROPER_SWIPES | NUMBER(5) | Y |  |
| IMPROPER_SWIPES | NUMBER(5) | Y |  |
| NO_SWIPES | NUMBER(5) | Y |  |
| LATE_COMING | NUMBER(5) | Y |  |
| AVG_ARRIVAL_OFFSET_MINUTES | NUMBER(9) | Y |  |
| EARLY_LEAVING | NUMBER(5) | Y |  |
| AVG_LEAVING_OFFSET_MINUTES | NUMBER(9) | Y |  |
| USERID | VARCHAR2(10) | Y |  |
| LEAVE_DAYS | NUMBER(4) default 0 | Y |  |
| NIGHTS | NUMBER(4) default 0 | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| ABSENT | NUMBER(4) | Y |  |
| DR_LOCATION_WHM | NUMBER(4) | Y | this colum will use to summerized the Work from home location from duty roster |
| DR_LOCATION_OUTSIDE_HOSPITAL | NUMBER(4) | Y | this colum will use to summerized the  location outside the hospital from duty roster |

- **FK** `FK_ATT_SHEET_SUMMARY_1`: (PROCESS_ID) -> HRD.PROCESS(PROCESS_ID)
- **Triggers**: `ATTENDANCE_SHEET_SUMMARY_DEL` (after delete), `ATTENDANCE_SHEET_SUMMARY_INS` (before insert), `ATTENDANCE_SHEET_SUMMARY_UPD` (before update)

## HRD.ATTENDANCE_SYSTEM_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| PC_ID_OLD | VARCHAR2(15) | Y |  |
| TERMINAL_TYPE_ID | VARCHAR2(15) | N |  |
| IMAGES_DIR_PATH | VARCHAR2(100) | N |  |
| DUTY_LOC_WISE_ATT | CHAR(1) default 'N' | N |  |
| LOAD_EMPLOYEE_LIST | CHAR(1) default 'N' | N |  |
| EMAIL_LOGGING | CHAR(1) default 'N' | N |  |
| FILE_LOGGING | CHAR(1) default 'Y' | N |  |
| THREAD_SLEEP_DELAY | NUMBER default '1000' | N |  |
| DISPLAY_PC_TIME | CHAR(1) default 'N' | N |  |
| ENABLE_KEYBOARD_INPUT | CHAR(1) default 'N' | N |  |
| CAPTURE_EMP_PIC | CHAR(1) default 'N' | N |  |
| DELETE_EMP_PIC | CHAR(1) default 'N' | N |  |
| EMP_PIC_SAVE_PATH | VARCHAR2(1000) | Y |  |
| PC_ID | VARCHAR2(15) | N | Change Primary Key of the table according to the new format |

- **PK** `PK_ATT_SYSTEM_SETUP`: ORGANIZATION_ID, LOCATION_ID, PC_ID
- **UK** `UK_ATT_SYSTEM_SETUP_1`: PC_ID
- **FK** `FK_ATT_SYSTEM_SETUP_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID)
- **FK** `FK_ATT_SYSTEM_SETUP_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_ATT_SYSTEM_SETUP_3`: (PC_ID) -> MIS_INFO.PC_INFORMATION(PC_ID)
- **FK** `FK_ATT_SYSTEM_SETUP_4`: (TERMINAL_TYPE_ID) -> MIS_INFO.TERMINAL_TYPE(TERMINAL_TYPE_ID) [disabled]
- **Triggers**: `ATTENDANCE_SYSTEM_SETUP_DEL` (after delete), `ATTENDANCE_SYSTEM_SETUP_INS` (before insert), `ATTENDANCE_SYSTEM_SETUP_UPD` (before update)

## HRD.AUTHOR

| Column | Type | Null | Comment |
|---|---|---|---|
| AUTHOR_ID | VARCHAR2(12) | N |  |
| FNAME | VARCHAR2(60) | N |  |
| MNAME | VARCHAR2(60) | Y |  |
| LNAME | VARCHAR2(60) | Y |  |
| INSTITUTE | VARCHAR2(300) | Y |  |
| ABSTRACT_ID | VARCHAR2(12) | N |  |
| INST_ID | NUMBER(1) default 1 | Y |  |


## HRD.BOND_EMPLOYEE_EXTERNAL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| TRAINING_ID | VARCHAR2(9) | N |  |
| NOMINEES_MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(1000) | Y |  |
| CONTACT_NUMBER | VARCHAR2(20) | Y |  |
| COMPANY_NAME | VARCHAR2(500) | Y |  |
| EMAIL | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `BOND_EMPLOYEE_EXTERNAL_PK`: SR_NO
- **Triggers**: `BOND_EMPLOYEE_EXTERNAL_DEL` (after delete), `BOND_EMPLOYEE_EXTERNAL_INS` (before insert), `BOND_EMPLOYEE_EXTERNAL_UPD` (before update)

## HRD.BOND_TRAINING_GURANTEE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| TRAINING_ID | VARCHAR2(9) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| NOMINEES_MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `BOND_TRAINING_GURANTEE_PK`: SR_NO
- **Triggers**: `BOND_TRAINING_GURANTEE_DEL` (after delete), `BOND_TRAINING_GURANTEE_INS` (before insert), `BOND_TRAINING_GURANTEE_UPD` (before update)

## HRD.SERVICE_BOND_TRAINING

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| TRAINING_ID | VARCHAR2(9) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| TRAINING_FEES | NUMBER | Y |  |
| FEE_UNIT | CHAR(1) | Y |  |
| COUNTRY_ID | NUMBER(3) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| TRAINING_VENUE | VARCHAR2(1000) | Y |  |
| INSTITUTE | VARCHAR2(1000) | Y |  |
| STATUS | CHAR(1) default 'D' | Y | 'D' DRAFT , W 'WITHDRWA',P 'POSTED' |
| BOND_FEES | NUMBER | Y |  |
| BOND_FEE_UNIT | CHAR(1) | Y |  |

- **PK** `SERVICE_BOND_TRAINING_PK`: SR_NO, TRAINING_ID
- **Triggers**: `SERVICE_BOND_TRAINING_DEL` (after delete), `SERVICE_BOND_TRAINING_INS` (before insert), `SERVICE_BOND_TRAINING_UPD` (before update)

## HRD.BOND_TRAINING_NOMINEES

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| TRAINING_ID | VARCHAR2(9) | N |  |
| BOND_FEES | NUMBER | Y |  |
| BOND_DURATION | NUMBER | Y |  |
| BOND_DURATION_UNIT | CHAR(1) | Y |  |
| BOND_START_DATE | DATE | Y |  |
| BOND_END_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| VISA_FEES | NUMBER | Y |  |
| TRAVEL_AMOUNT | NUMBER | Y |  |
| ACCOMODATION | NUMBER | Y |  |
| DAILY_ALLOWANCE | NUMBER | Y |  |
| STATUS | CHAR(1) default 'I' | Y | I = INITIAL STAGE , Q = QUEUE STAGE |
| FEE_UNIT | CHAR(1) | Y |  |
| SR_NO_MASTER | NUMBER | Y |  |
| VISA_FEES_UNIT | CHAR(1) | Y |  |
| TRAVEL_FEES_UNIT | CHAR(1) | Y |  |
| ACCOMODATION_UNIT | CHAR(1) | Y |  |
| DAILY_ALLOWANCE_UNIT | CHAR(1) | Y |  |
| BOND_FEES_TWO | NUMBER | Y |  |
| BOND_FEE_UNIT_TWO | CHAR(1) | Y |  |

- **PK** `BOND_TRAINING_NOMINEES_PK`: SR_NO
- **FK** `BOND_TRAINING_NOMINEES_FK`: (SR_NO_MASTER, TRAINING_ID) -> HRD.SERVICE_BOND_TRAINING(SR_NO, TRAINING_ID)
- **Triggers**: `BOND_TRAINING_NOMINEES_DEL` (after delete), `BOND_TRAINING_NOMINEES_INS` (before insert), `BOND_TRAINING_NOMINEES_UPD` (before update)

## HRD.CANCELLED_REQUESTED_CTO

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| TOTAL_MINUTES | NUMBER(5) | Y |  |
| APPROVED_NO | NUMBER(1) | Y |  |
| MAX_AVAIL_DATE | DATE | Y |  |
| BALANCE | NUMBER(3) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| CANCELLED_DATE | DATE | Y |  |
| CANCELLED_BY | VARCHAR2(14) | Y |  |
| STATUS | CHAR(1) | Y |  |

- **PK** `PK_CANCELLED_REQUESTED_CTO`: DUTY_DATE, MRNO, SERIAL_NO

## HRD.CARD_SWIPE
Use to store card swip information

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(14) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| DATE_TIME | DATE | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| FLAG | VARCHAR2(1) | Y |  |
| LATITUDE | VARCHAR2(50) | Y | Value will be filled by mobile app in case of remote attendance |
| LONGITUDE | VARCHAR2(50) | Y | Value will be filled by mobile app in case of remote attendance |
| ATTENDANCE_INCLUDE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CARD_SWIPE`: SERIAL_NO
- **Triggers**: `CARD_SWIPE_DEL` (after delete), `CARD_SWIPE_INS` (before insert), `CARD_SWIPE_UPD` (before update), `SEQ_INSERT` (before insert), `TRG_WS_ZOJ_YC_IN_Q` (after insert or update or delete)

## HRD.CARD_SWIPER_PIC

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(9) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| PICTURE | BLOB | N |  |
| TRANS_TIMESTAMP | DATE default SYSDATE | N |  |

- **FK** `FK_CARD_SWIPER_PIC_1`: (SERIAL_NO) -> HRD.CARD_SWIPE(SERIAL_NO) [disabled]
- **FK** `FK_CARD_SWIPER_PIC_2`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `CARD_SWIPER_PIC_DEL` (after delete), `CARD_SWIPER_PIC_INS` (before insert), `CARD_SWIPER_PIC_UPD` (before update)

## HRD.CARD_SWIPE_HISTORY
Store card swipe history

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(9) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| DATE_TIME | DATE | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| FLAG | VARCHAR2(1) | Y |  |


## HRD.CAREER_PATH_LEVEL

| Column | Type | Null | Comment |
|---|---|---|---|
| LEVEL_ID | NUMBER(5) | N |  |
| DECRIPTION | VARCHAR2(4000) | N |  |
| FROM_SALARY | NUMBER(10) default 0 | N |  |
| TO_SALARY | NUMBER(10) default 0 | N |  |
| SUGGESTED_FROM_SALARY | NUMBER(10) default 0 | N |  |
| SUGGESTED_TO_SALARY | NUMBER(10) default 0 | N |  |
| ACTIVE | CHAR(1) | N |  |
| LEVEL_STAGES | NUMBER(2) default 5 | N |  |
| STAGE_VALUE | NUMBER default 0 | N |  |

_No standard audit columns._

- **PK** `PK_CAREER_PATH_LEVEL`: LEVEL_ID
- **CHECK** `CHK_CPL_01`: ACTIVE IN ('Y', 'N')
- **CHECK** `CHK_CPL_02`: TO_SALARY >= FROM_SALARY
- **CHECK** `CHK_CPL_03`: SUGGESTED_TO_SALARY >= SUGGESTED_FROM_SALARY

## HRD.CC_CARD_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| CC_EMP_CODE | VARCHAR2(14) | Y |  |
| CC_NUMBER | VARCHAR2(3) | Y |  |
| REQUEST_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(300) | Y |  |
| PRINT_YN | CHAR(1) default 'N' | Y |  |
| HIS_USER | CHAR(1) default 'N' | Y |  |


## HRD.CC_EMP_ACTIVATE_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| CC_EMP_CODE | VARCHAR2(14) | N |  |
| CC_EMP_NAME | VARCHAR2(500) | Y |  |
| JOINING_DATE | DATE | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| CC_LOCATION | VARCHAR2(3) | Y |  |
| REQUEST_DATE | DATE | Y |  |
| STATUS_REMARKS | VARCHAR2(4000) | Y |  |
| PREVIOUS_STATUS | CHAR(1) | Y |  |
| ACCEPT | CHAR(1) default 'N' | Y |  |
| REJECT | CHAR(1) default 'N' | Y |  |
| STATUS | CHAR(1) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |
| LEAVE_DATE | DATE | Y |  |
| IN_ACTIVE_REMARKS | VARCHAR2(4000) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |

- **PK** `CC_EMP_ACTIVATE_Q_PK`: CC_EMP_CODE
- **Triggers**: `CC_EMP_ACTIVATE_Q_DEL` (after delete), `CC_EMP_ACTIVATE_Q_DEL_HIS` (after delete or update), `CC_EMP_ACTIVATE_Q_INS` (before insert), `CC_EMP_ACTIVATE_Q_UPD` (before update), `CC_EMP_ACTIVE_QUEUE_PT_UPD` (before update or delete), `CC_EMP_ACTIVE_Q_PT_INS` (after insert )

## HRD.CC_EMP_ACTIVATE_Q_HIS

| Column | Type | Null | Comment |
|---|---|---|---|
| CC_EMP_CODE | VARCHAR2(14) | Y |  |
| CC_EMP_NAME | VARCHAR2(500) | Y |  |
| JOINING_DATE | DATE | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| CC_LOCATION | VARCHAR2(3) | Y |  |
| REQUEST_DATE | DATE | Y |  |
| STATUS_REMARKS | VARCHAR2(4000) | Y |  |
| PREVIOUS_STATUS | CHAR(1) | Y |  |
| ACCEPT | CHAR(1) | Y |  |
| REJECT | CHAR(1) | Y |  |
| STATUS | CHAR(1) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| IN_ACTIVE_REMARKS | VARCHAR2(4000) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| LEAVE_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.CC_EMP_CARD_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.CC_EMP_REGISTRATION

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | N |  |
| CC_NUMBER | VARCHAR2(3) | N |  |
| EMP_NAME | VARCHAR2(50) | N |  |
| F_NAME | VARCHAR2(50) | Y |  |
| HUSBAND_NAME | VARCHAR2(50) | Y |  |
| MARITAL_STATUS | VARCHAR2(10) | Y |  |
| DOB | DATE | Y |  |
| CNIC | VARCHAR2(15) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| JOIN_DATE | DATE | N |  |
| ADDRESS | VARCHAR2(400) | Y |  |
| CITY_ID | NUMBER(4) | Y |  |
| CONTACT_NO | VARCHAR2(12) | Y |  |
| SALARY | NUMBER(7) | Y |  |
| EMP_PIC | BLOB | Y |  |
| CARD_GEN_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| GENDER | CHAR(1) | N |  |
| STATE_ID | NUMBER(4) | Y |  |
| DISTRICT_ID | NUMBER(4) | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| RESIGN_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| TRAINING_TO_DATE | DATE | Y |  |
| TRAINING_FROM_DATE | DATE | Y |  |
| LEAVE_DETAIL | VARCHAR2(500) | Y |  |
| OTHER_QUALIFICATION | VARCHAR2(50) | Y |  |
| OTH_QUAL | VARCHAR2(50) | Y |  |
| QUALIFICATION_ID | VARCHAR2(30) | Y |  |
| STATUS_REMARKS | VARCHAR2(4000) | Y |  |
| IN_ACTIVE_REMARKS | VARCHAR2(4000) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_CC_EMP_CODE`: EMP_CODE, CC_NUMBER
- **FK** `FK_CC_DESIGNATION`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **FK** `FK_CC_NUMBER`: (CC_NUMBER) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `CC_EMP_ACTIVE_INACTIVE` (before update of active), `CC_EMP_ACTIVE_QUEUE` (after insert or update of active), `CC_EMP_REGISTRATION_DEL` (after delete), `CC_EMP_REGISTRATION_INS` (before insert), `CC_EMP_REGISTRATION_UPD` (before update)

## HRD.CC_EMP_PICTURE

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | Y |  |
| CC_NUMBER | VARCHAR2(3) | Y |  |
| EMP_PIC | BLOB | Y |  |

- **FK** `FK_EMP_PIC`: (EMP_CODE, CC_NUMBER) -> HRD.CC_EMP_REGISTRATION(EMP_CODE, CC_NUMBER) [disabled]

## HRD.CHANGED_LEAVE_DATES_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| ACTUAL_FROM_DATE | DATE | N |  |
| ACTUAL_TO_DATE | DATE | N |  |
| ACTUAL_LEAVE_DAYS | NUMBER(7,2) | Y |  |
| CHANGED_FROM_DATE | DATE | N |  |
| CHANGED_TO_DATE | DATE | N |  |
| CHANGED_LEAVE_DAYS | NUMBER(7,2) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ACTOR_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_CHANGED_LEAVE_DATES_HISTORY`: MRNO, SERIAL_NO, ACTUAL_FROM_DATE, ACTUAL_TO_DATE, CHANGED_FROM_DATE, CHANGED_TO_DATE
- **Triggers**: `CHAN_LEAVE_DATES_HIST_INS` (before insert)

## HRD.CHANGED_LEAVE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(3) | Y |  |
| APPLICANT_MRNO | VARCHAR2(14) | Y |  |
| LEAVE_SERIAL_NO | VARCHAR2(14) | Y |  |
| IN_QUEUE | VARCHAR2(14) | Y |  |
| MOVED_QUEUE | VARCHAR2(14) | Y |  |
| OLD_SUBSTITUTE | VARCHAR2(14) | Y |  |
| NEW_SUBSTITUTE | VARCHAR2(14) | Y |  |
| OLD_SUBSTITUTE_CLINICAL | VARCHAR2(14) | Y |  |
| NEW_SUBSTITUTE_CLINICAL | VARCHAR2(14) | Y |  |

- **Triggers**: `CHANGED_LEAVE_HISTORY_DEL` (after delete), `CHANGED_LEAVE_HISTORY_INS` (before insert), `CHANGED_LEAVE_HISTORY_UPD` (before update)

## HRD.CL_DEF_CHECKLIST_PARAMS

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECKLIST_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| CL_PARAMETER_TYPE_ID | NUMBER(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PARAM_TYPE | CHAR(1) | Y | ''O' OPEN  'L' LIST OF VALUES' |
| PRO_TEXT | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(2) | Y |  |

- **PK** `PK_CHECKLIST_PARAM_ID`: PARAMETER_ID, CHECKLIST_ID

## HRD.CL_DEF_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| HEAD_OF_DEPARTMENT | VARCHAR2(14) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_CL_DEF_DEPARTMENT`: DEPARTMENT_ID, LOCATION_ID
- **Triggers**: `CL_DEF_DEPARTMENT_DEL` (after delete), `CL_DEF_DEPARTMENT_INS` (before insert), `CL_DEF_DEPARTMENT_UPD` (before update)

## HRD.CL_DEF_DEPT_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| CL_SECTION_ID | NUMBER(5) | N |  |
| SECTION_HEAD | VARCHAR2(14) | Y |  |
| SECTION_EVENT | VARCHAR2(1000) | Y |  |

- **PK** `PK_CL_DEF_DEPT_SECTION`: DEPARTMENT_ID, CL_SECTION_ID, LOCATION_ID
- **FK** `FK_CL_DEF_DEPT_DEPARTMENT`: (DEPARTMENT_ID, LOCATION_ID) -> HRD.CL_DEF_DEPARTMENT(DEPARTMENT_ID, LOCATION_ID) [disabled]
- **Triggers**: `CL_DEF_DEPT_SECTION_DEL` (after delete), `CL_DEF_DEPT_SECTION_INS` (before insert), `CL_DEF_DEPT_SECTION_UPD` (before update)

## HRD.CL_EMP_PENDING_TASK_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_ID | NUMBER(10) | N |  |
| JOINING_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| CLEARANCE_STATUS | VARCHAR2(3) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| CLEARANCE_TYPE_ID | VARCHAR2(3) | Y |  |
| CLEARANCE_START_DATE | DATE | Y |  |
| CLEARANCE_END_DATE | DATE | Y |  |

- **PK** `CL_EMP_PENDING_TASK_PK`: CLEARANCE_ID, JOINING_DATE, MRNO
- **FK** `CL_EMP_PENDING_TASK_FK`: (CLEARANCE_STATUS) -> DEFINITIONS.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **Triggers**: `CL_EMP_PENDING_TASK_MASTER_DEL` (after delete), `CL_EMP_PENDING_TASK_MASTER_INS` (before insert), `CL_EMP_PENDING_TASK_MASTER_UPD` (before update)

## HRD.COLUMN_WISE_HINTS

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(12) | N |  |
| BLOCK_NAME | VARCHAR2(100) | N |  |
| COLUMN_NAME | VARCHAR2(50) | N |  |
| HINT_DESC | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| DISPLAY_NAME | VARCHAR2(100) | Y |  |

- **PK** `PK_COLUMN_WISE_HINTS`: OBJECT_CODE, BLOCK_NAME, COLUMN_NAME
- **Triggers**: `COLUMN_WISE_HINTS_DEL` (after delete), `COLUMN_WISE_HINTS_INS` (before insert), `COLUMN_WISE_HINTS_UPD` (before update)

## HRD.CONSULTANTS_CV

| Column | Type | Null | Comment |
|---|---|---|---|
| CV_SNO | NUMBER(7) | N |  |
| NAME | VARCHAR2(180) | Y |  |
| CONTACT_NUMBER | VARCHAR2(180) | Y |  |
| EMAIL | VARCHAR2(60) | Y |  |
| DEGREES | VARCHAR2(500) | Y |  |
| FATHER_NAME | VARCHAR2(180) | Y |  |
| SPECIALITY | VARCHAR2(6) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| CARE_OFF | VARCHAR2(180) | Y |  |
| FIRST_SHORT_LIST | CHAR(1) | Y |  |
| FIRST_SHORT_LIST_COMMENTS | VARCHAR2(4000) | Y |  |
| CV_ATTACHMENT | BLOB | Y |  |
| CONSULT_DECSION | CHAR(1) | Y |  |
| CMO_COMMENTS | VARCHAR2(4000) | Y |  |
| REFERENCES_REQUEST | DATE | Y |  |
| REFERENCE_RECEIVED | DATE | Y |  |
| PSB_COMMENTS | VARCHAR2(4000) | Y |  |
| PSB_DECISIONS | CHAR(1) | Y |  |
| INITIAL_CONTRACT_DATE | DATE | Y |  |
| CONTRACT_ATTACHMENT | BLOB | Y |  |
| FINAL_CONTRACT_DATE | DATE | Y |  |
| OFFER_DATE | DATE | Y |  |
| OFFERING_DATE | DATE | Y |  |
| CV_DOC_NAME | VARCHAR2(100) | Y |  |
| CONTRACT_DOC_NAME | VARCHAR2(100) | Y |  |
| DATA_TRANSFER_STATUS | CHAR(1) default 'C' | Y | 'C' for current 'H' for history |
| CMO_SEND_COMMENTS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CV_SNO`: CV_SNO
- **Triggers**: `CONSULTANTS_CV_DEL` (after delete), `CONSULTANTS_CV_INS` (before insert), `CONSULTANTS_CV_UPD` (before update)

## HRD.CONSULTANTS_CONSULT

| Column | Type | Null | Comment |
|---|---|---|---|
| CV_SNO | NUMBER(7) | N |  |
| SNO | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SEND_DATE | DATE | Y |  |
| RECEIVE_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(4000) | Y |  |
| REMINDER | NUMBER(3) | Y |  |
| CONSULTANT_DECISION | VARCHAR2(1) | Y |  |
| CMO_SEND_COMMENTS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CV_SNO_SNO`: CV_SNO, SNO, MRNO
- **FK** `FK_CV_SNO`: (CV_SNO) -> HRD.CONSULTANTS_CV(CV_SNO)
- **Triggers**: `CONSULTANTS_CONSULT_DEL` (after delete), `CONSULTANTS_CONSULT_INS` (before insert), `CONSULTANTS_CONSULT_UPD` (before update)

## HRD.CONSULTANTS_REFERENCES

| Column | Type | Null | Comment |
|---|---|---|---|
| CV_SNO | NUMBER(9) | N |  |
| REF_SNO | NUMBER(3) | N |  |
| NAME | VARCHAR2(180) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| REFERENCE_ATTACHMENT | BLOB | Y |  |
| REFERENCE_DOC_NAME | VARCHAR2(100) | Y |  |
| SEND_DATE | DATE | Y |  |
| RECEIVED_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_REF_SNO`: REF_SNO, CV_SNO
- **FK** `FK_CV_SNO_REF`: (CV_SNO) -> HRD.CONSULTANTS_CV(CV_SNO) [disabled]
- **Triggers**: `CONSULTANTS_REFERENCES_DEL` (after delete), `CONSULTANTS_REFERENCES_INS` (before insert), `CONSULTANTS_REFERENCES_UPD` (before update)

## HRD.PRIVILEGES_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIVILEGES_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PATIENT_CATEGORY | CHAR(1) | Y |  |
| REPORT_HEADER | VARCHAR2(2000) | Y |  |
| REPORT_VERSION | VARCHAR2(200) | Y |  |
| PRIVILEGE_SPECIALITY_ID | NUMBER | Y |  |

- **PK** `PK_PRIVILEGE_SETUP`: PRIVILEGES_ID
- **Triggers**: `PRIVILEGES_SETUP_DEL` (after delete), `PRIVILEGES_SETUP_INS` (before insert), `PRIVILEGES_SETUP_UPD` (before update)

## HRD.CONSULTANT_PRIVIG_GRANT_M

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PRIVILEGE_ID | NUMBER | N |  |

- **PK** `PK_CONS_PRIV_GRANT`: MRNO, PRIVILEGE_ID
- **FK** `FK_CONS_PRIV_GRANT`: (PRIVILEGE_ID) -> HRD.PRIVILEGES_SETUP(PRIVILEGES_ID) [disabled]
- **Triggers**: `CONSULTANT_PRIVIG_GRANT_M_DEL` (after delete), `CONSULTANT_PRIVIG_GRANT_M_INS` (before insert), `CONSULTANT_PRIVIG_GRANT_M_UPD` (before update)

## HRD.CONSULTANT_PRIVIG_GRANT_D

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| PRIVILEGES_ID | NUMBER | Y |  |
| SR_NO | NUMBER(5) | N |  |
| DOC_TYPE_ID | NUMBER(3) | Y |  |
| INITIAL_EFFECTIVE_DATE | DATE | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| PRIVILEGES_DETAIL_ID | NUMBER | Y |  |
| IS_NUMBER_REQUIRED | CHAR(1) | Y |  |
| NUMBER_REQUIRED | NUMBER | Y |  |
| SP_PRIVILEGE_ID | NUMBER | Y |  |
| GRANTED | CHAR(1) | Y |  |
| SP_DESCRIPTION | VARCHAR2(4000) | Y |  |
| PRIVILEGE_TYPE | CHAR(1) | Y |  |
| APPLICANT_ID | NUMBER | Y |  |
| PSB_DATE | DATE | Y |  |
| IS_SEND_EMAIL | CHAR(1) default 'N' | Y |  |

- **PK** `PK_CONSULTANT_PRIV_D`: SR_NO
- **FK** `FK_CONSULTANT_PRIV_D_01`: (MRNO, PRIVILEGES_ID) -> HRD.CONSULTANT_PRIVIG_GRANT_M(MRNO, PRIVILEGE_ID) [disabled]
- **Triggers**: `CONSULTANT_PRIVIG_GRANT_D_DEL` (after delete), `CONSULTANT_PRIVIG_GRANT_D_INS` (before insert), `CONSULTANT_PRIVIG_GRANT_D_UPD` (before update), `CONSULTANT_PRIVILEGES_Q_INSRT` (before insert or update)

## HRD.CONSULTANT_PRIVILEGES_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PRIVILEGES_ID | NUMBER | N |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RESEARCH | VARCHAR2(4000) | Y |  |
| LOCATION_ID | VARCHAR2(14) | Y |  |

- **PK** `PK_PRIVILEGES_MRNO`: MRNO, PRIVILEGES_ID
- **Triggers**: `CONSULTANT_PRIVILEGES_DETAIL_DEL` (after delete), `CONSULTANT_PRIVILEGES_DETAIL_INS` (before insert), `CONSULTANT_PRIVILEGES_DETAIL_UPD` (before update), `CONS_PRIV_DETAIL_DEL` (after delete), `CONS_PRIV_DETAIL_INS` (before insert), `CONS_PRIV_DETAIL_UPD` (before update)

## HRD.CONSULTANT_PRIVILEGES_DOC

| Column | Type | Null | Comment |
|---|---|---|---|
| TASK_ID | VARCHAR2(9) | Y |  |
| DOCUMENT_ID | VARCHAR2(15) | N |  |
| SR_NO | NUMBER(5) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(100) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHMENT_DATE | DATE | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| DISPLAY | CHAR(1) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| DOC_TYPE_ID | NUMBER(3) | Y |  |
| DOCUMENT_QUEUE_STATUS | VARCHAR2(2) | Y |  |
| POSITION_ID | VARCHAR2(255) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| PRIVILEGES_ID | NUMBER | Y |  |
| FROM_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ON_PROBATION | CHAR(1) default 'N' | Y | Either Y or N |
| TO_DATE | DATE | Y |  |
| CONSULTANT_SKILLS | VARCHAR2(1000) | Y | THIS COLUMN STORE CONSULTANT SKILLS |
| PATIENT_CATEGORY | CHAR(1) default 'A' | Y | this column use for consultant privileges category "Adult / Peads" A for All, D for Adult, P for Peads |
| INITIAL_EFFECTIVE_DATE | DATE | Y | This column contains INITIAL EFFECTIVE DAE of privileges |

- **PK** `PK_CONSULTANT_PRIVILEGES_DOC`: DOCUMENT_ID
- **Triggers**: `CONSULTANT_PRIVILEGES_DOC_DEL` (after delete), `CONSULTANT_PRIVILEGES_DOC_INS` (before insert), `CONSULTANT_PRIVILEGES_DOC_UPD` (before update)

## HRD.CONSULTANT_PRIVILEGES_EMAIL_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| PRIVILEGES_ID | NUMBER | Y |  |
| DOC_TYPE_ID | NUMBER(3) | Y |  |
| INITIAL_EFFECTIVE_DATE | DATE | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| PRIVILEGES_DETAIL_ID | NUMBER | Y |  |
| IS_NUMBER_REQUIRED | CHAR(1) | Y |  |
| NUMBER_REQUIRED | NUMBER | Y |  |
| SP_PRIVILEGE_ID | NUMBER | Y |  |
| GRANTED | CHAR(1) | Y |  |
| SP_DESCRIPTION | VARCHAR2(4000) | Y |  |
| PRIVILEGE_TYPE | CHAR(1) | Y |  |
| APPLICANT_ID | NUMBER | Y |  |
| PSB_DATE | DATE | Y |  |
| IS_SEND_EMAIL | CHAR(1) | Y |  |

- **PK** `CONSULTANT_PRIVILEGES_EMAIL_Q_PK`: SR_NO
- **Triggers**: `CONSULTANT_PRIVILEGES_Q_HIS_DEL` (after delete), `CONSULT_PRIV_EMAIL_Q_DEL` (after delete), `CONSULT_PRIV_EMAIL_Q_INS` (before insert), `CONSULT_PRIV_EMAIL_Q_UPD` (before update)

## HRD.CONSULTANT_PRIVILEGES_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER(10) | Y |  |
| TOKEN_NO | VARCHAR2(50) | N |  |
| Q_ROLE | VARCHAR2(3) | Y | R for referee P form Physician C for PSB |
| PREVIEW | CHAR(1) | Y | N FOR UPDATION , P FOR ONLY PREVIEW S FOR FINAL PREVIEW WITH CONSULTANT DATA |
| IN_QUEUE_EMAIL | VARCHAR2(70) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_PRIV_QUEUE`: TOKEN_NO
- **Triggers**: `CONSULTANT_PRIVILEGES_Q_DEL` (after delete), `CONSULTANT_PRIVILEGES_Q_INS` (before insert), `CONSULTANT_PRIVILEGES_Q_UPD` (before update)

## HRD.CONSULTANT_PRIVILEGES_Q_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| PRIVILEGES_ID | NUMBER | Y |  |
| DOC_TYPE_ID | NUMBER(3) | Y |  |
| INITIAL_EFFECTIVE_DATE | DATE | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| PRIVILEGES_DETAIL_ID | NUMBER | Y |  |
| IS_NUMBER_REQUIRED | CHAR(1) | Y |  |
| NUMBER_REQUIRED | NUMBER | Y |  |
| SP_PRIVILEGE_ID | NUMBER | Y |  |
| GRANTED | CHAR(1) | Y |  |
| SP_DESCRIPTION | VARCHAR2(4000) | Y |  |
| PRIVILEGE_TYPE | CHAR(1) | Y |  |
| APPLICANT_ID | NUMBER | Y |  |
| PSB_DATE | DATE | Y |  |
| IS_SEND_EMAIL | CHAR(1) | Y |  |
| ENTRY_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.CONSULTANT_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| CV_SNO | NUMBER(7) | Y |  |
| QUEUE_ID | NUMBER(9) | N |  |
| CONSULTANT_MRNO | VARCHAR2(14) | Y |  |
| CONSULTANT_DECISIONS | VARCHAR2(1) | Y |  |
| CONSULTANT_REMARKS | VARCHAR2(4000) | Y |  |
| SNO | NUMBER(3) | Y |  |
| FORWARD_DATE | DATE | Y |  |

- **PK** `PK_CON_QUEUE_ID`: QUEUE_ID
- **Triggers**: `CONSULTANT_QUEUE_DEL` (after delete), `CONSULTANT_QUEUE_INS` (before insert), `CONSULTANT_QUEUE_UPD` (before update)

## HRD.CONTRACTUAL_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |


## HRD.CONTRACT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_ID | NUMBER(4) | N |  |
| CONTRACT_FACILITY_ID | NUMBER(4) | N |  |

- **PK** `PK_CONTRACT_DETAIL`: CONTRACT_ID, CONTRACT_FACILITY_ID
- **Triggers**: `CONTRACT_DETAIL_DEL` (after delete), `CONTRACT_DETAIL_INS` (before insert), `CONTRACT_DETAIL_UPD` (before update)

## HRD.CONTRACT_TYPE_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_TYPE_ID | VARCHAR2(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| REMARKS | VARCHAR2(3000) | Y |  |

- **PK** `PK_CONTRACT_TYPE_EMPLOYEES`: CONTRACT_TYPE_ID, PATIENT_TYPE_ID
- **FK** `FK_CONTRACT_TYPE_EMPLOYEES_1`: (CONTRACT_TYPE_ID) -> HRD.CONTRACT_TYPE(CONTRACT_TYPE_ID)
- **FK** `FK_CONTRACT_TYPE_EMPLOYEES_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **Triggers**: `CONTRACT_TYPE_EMPLOYEES_DEL` (after delete), `CONTRACT_TYPE_EMPLOYEES_INS` (before insert), `CONTRACT_TYPE_EMPLOYEES_UPD` (before update)

## HRD.CONTRACT_TYPE_LEAVES

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_TYPE_ID | VARCHAR2(3) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| NO_OF_LEAVES_ALLOWED | NUMBER(3) default 0 | Y |  |
| MAX_LEAVE_LIMIT | NUMBER(3) | Y | this colum use for maximum accumulated days |
| MIN_SERVICE_REQUIRED | NUMBER(4) default 0 | Y | Store months after which employee is eligible for leave for.ex 12 means 12 months of service is required to avail leave |
| ENTITLEMENT_LEAVE | NUMBER(3) | Y | this column will be use to store number of total leave according the entitlement (Yearly, Monthly) |
| CARRY_FORWARD_LIMIT | NUMBER(3) default 0 | N |  |

- **PK** `PK_CONTRACT_TYPE_LEAVES`: CONTRACT_TYPE_ID, LEAVE_TYPE_ID
- **Triggers**: `CONTRACT_TYPE_LEAVES_CEA` (before insert or update or delete), `CONTRACT_TYPE_LEAVES_DEL` (after delete), `CONTRACT_TYPE_LEAVES_INS` (before insert), `CONTRACT_TYPE_LEAVES_UPD` (before update), `TRG_WS_HXP_UN_JA_Q` (after insert or update or delete)

## HRD.CON_PRIV_HR_VERIFICATION

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| EMAIL | VARCHAR2(50) | Y |  |
| APPLICANT_TYPE | CHAR(1) | Y |  |
| DISPLAY | CHAR(1) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |

- **PK** `PK_CON_PRIV_HR_VERIFICATION`: APPLICANT_ID
- **Triggers**: `CON_PRIV_HR_VERIFICATION_DEL` (after delete), `CON_PRIV_HR_VERIFICATION_INS` (before insert), `CON_PRIV_HR_VERIFICATION_UPD` (before update)

## HRD.CON_REF_HR_VERIFICATION

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_ID | NUMBER | N |  |
| PRIVILEGE_ID | NUMBER | N |  |
| REFEREE_EMAIL | VARCHAR2(60) | N |  |
| REFEREE_TYPE | CHAR(1) | Y |  |
| DISPLAY | CHAR(1) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |

- **PK** `PK_CON_REF_HR_VERIFICATION`: APPLICANT_ID, PRIVILEGE_ID, REFEREE_EMAIL
- **Triggers**: `CON_REF_HR_VERIFICATION_DEL` (after delete), `CON_REF_HR_VERIFICATION_INS` (before insert), `CON_REF_HR_VERIFICATION_UPD` (before update)

## HRD.COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR | VARCHAR2(2) | N |  |
| COUNTER | VARCHAR2(12) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_COUNTER`: YEAR
- **Triggers**: `COUNTER_DEL` (after delete), `COUNTER_INS` (before insert), `COUNTER_UPD` (before update)

## HRD.COUNTER_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR | VARCHAR2(2) | Y |  |
| COUNTER | VARCHAR2(7) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## HRD.CTO

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| TOTAL_MINUTES | NUMBER(5) | Y |  |
| APPROVED_NO | NUMBER(1) | Y |  |
| MAX_AVAIL_DATE | DATE | Y |  |
| FIRST_AVAILED_DATE | DATE | Y |  |
| BALANCE | NUMBER(3) | Y |  |
| SECOND_AVAILED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |

- **PK** `PK_CTO`: DUTY_DATE, MRNO
- **Triggers**: `CTO_DEL` (after delete), `CTO_INS` (before insert), `CTO_UPD` (before update)

## HRD.CTO_APPROVAL_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | Y |  |
| DUTY_DATE | DATE | Y |  |
| APPLICANT_SERIAL_NO | NUMBER(5) | Y |  |
| BALANCE | NUMBER(3) | Y |  |
| FORWARD_TO | VARCHAR2(14) | Y |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y |  |
| REMARKS | VARCHAR2(300) | Y |  |
| REQUESTING_USER_ID | VARCHAR2(14) | Y |  |
| REQUESTING_TERMINAL | VARCHAR2(30) | Y |  |
| REQUESTING_TRN_DATE | DATE | Y |  |
| DECIDING_USER_ID | VARCHAR2(14) | Y |  |
| DECIDING_TERMINAL | VARCHAR2(30) | Y |  |
| DECIDING_TRN_DATE | DATE | Y |  |


## HRD.CTO_APPROVAL_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | N |  |
| DUTY_DATE | DATE | N |  |
| BALANCE | NUMBER | Y |  |
| FORWARD_TO | VARCHAR2(14) | Y |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y |  |
| REMARKS | VARCHAR2(300) | Y |  |
| REQUESTING_USER_ID | VARCHAR2(14) | Y |  |
| REQUESTING_TERMINAL | VARCHAR2(30) | Y |  |
| REQUESTING_TRN_DATE | DATE | Y |  |

- **PK** `PK_CTO_APPROVAL_QUEUE`: APPLICANT_MRNO, DUTY_DATE

## HRD.CURRENT_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |

- **PK** `CURRENT_EMP_PK`: MRNO
- **Triggers**: `CURRENT_EMPLOYEES_CEA` (before insert or update or delete), `CURRENT_EMPLOYEES_DEL` (after delete), `CURRENT_EMPLOYEES_INS` (before insert), `CURRENT_EMPLOYEES_UPD` (before update), `TRG_WS_WTO_VA_RP_Q` (after insert or update or delete)

## HRD.DAILY_ATTENDANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(193) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| CARD_SWIPE_IN | DATE | Y |  |
| CARD_SWIPE_OUT | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |
| USER_TERMINAL | VARCHAR2(30) | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| SHIFT_START_TIME | DATE | Y |  |
| SHIFT_END_TIME | DATE | Y |  |
| STATUS | CHAR(1) | Y | 'M' = MISSING DUTY ROSTER, 'L' = LEAVE, 'T' = LATE ARRIVAL,'A'=  ABSENT,'O' = OUT OF HOSPITAL, 'R'=TRAVEL REQUEST |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |

- **CHECK** `STATUS`: STATUS IN ('M','L','T','A','O', 'R')

## HRD.DAYS
Not In Use

| Column | Type | Null | Comment |
|---|---|---|---|
| DAY | DATE | N |  |

- **PK** `PK_DAYS`: DAY

## HRD.DEF_ATTENDANCE_DECISION

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTENDANCE_DECISION_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| FORWARDED_TO_HR | CHAR(1) | Y | Decision can be forwarded to HR |

- **PK** `PK_ATTENDANCE_DECISION_ID`: ATTENDANCE_DECISION_ID
- **UK** `UK_ATTENDANCE_DECISION_ID`: DESCRIPTION
- **CHECK** `CK_DEF_ATTENDANCE_DECISION_001`: FORWARDED_TO_HR IN ('Y','N')
- **Triggers**: `DEF_ATTENDANCE_DECISION_DEL` (after delete), `DEF_ATTENDANCE_DECISION_INS` (before insert), `DEF_ATTENDANCE_DECISION_UPD` (before update)

## HRD.DEF_SYMPOSIUM_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SYMPOSIUM_TYPE_ID | VARCHAR2(3) | N | Unique ID to identify each symposium |
| DESCRIPTION | VARCHAR2(100) | Y | Symposium description as published on web or other media |
| ACTIVE | CHAR(1) | Y |  |
| ACTIVATION_DATE | DATE default SYSDATE | Y | Date of insertion |
| SYMPOSIUM_START_DATE | DATE default SYSDATE | Y | Start Date of registration |
| SYMPOSIUM_END_DATE | DATE | Y | End Date of registration |
| MESSAGE_SUBJECT | VARCHAR2(4000) | Y | Not in use |
| MESSAGE_BODY | VARCHAR2(4000) | Y | Not in use |
| EXPIRY_MESSAGE | VARCHAR2(4000) | Y | Not in use |
| FOOTER_TEXT | VARCHAR2(4000) | Y | Display some text as instructions or other information related to symposium |
| EMAIL_CODE | VARCHAR2(1000) | Y | Same as CCWEB.ONLINE_EMAIL_RESPONSE.EMAIL_CODE. Email contents to be used against curent symposium. |

- **PK** `PK_DEF_SYMPOSIUM_TYPE`: SYMPOSIUM_TYPE_ID

## HRD.DELETED_CTO

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| TOTAL_MINUTES | NUMBER(5) | Y |  |
| APPROVED_NO | NUMBER(1) | Y |  |
| MAX_AVAIL_DATE | DATE | Y |  |
| FIRST_AVAILED_DATE | DATE | Y |  |
| BALANCE | NUMBER(3) | Y |  |
| SECOND_AVAILED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| ENTERED_DATE | DATE | Y |  |


## HRD.DEPARTMENT_DOCMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(50) | N |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DESIGNATION_ID | VARCHAR2(50) | Y |  |

- **PK** `DEPARTMENT_WSIE_PK`: DOC_CATEGORY_ID, DOCUMENT_TYPE_ID, DEPARTMENT_ID
- **Triggers**: `DEPARTMENT_DOCMENT_TYPE_DEL` (after delete), `DEPARTMENT_DOCMENT_TYPE_INS` (before insert), `DEPARTMENT_DOCMENT_TYPE_UPD` (before update), `DEPART_WISE_DOC_DEL` (before delete)

## HRD.DEPARTMENT_LEVEL

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| LEVEL_ID | VARCHAR2(6) | N |  |
| LEVEL_DESC | VARCHAR2(200) | Y |  |
| REQUIRED_MORNING_SHIFT | NUMBER(3) | Y |  |
| REQUIRED_EVENING_SHIFT | NUMBER(3) | Y |  |
| REQUIRED_NIGHT_SHIFT | NUMBER(3) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `PK_DEPARTMENT_LEVEL`: DEPARTMENT_ID, LEVEL_ID
- **Triggers**: `DEPARTMENT_LEVEL_CEA` (before insert or update or delete), `TRG_WS_JGO_EN_KC_Q` (after insert or update or delete)

## HRD.DEPARTMENT_SHIFT

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SHIFT_ID | VARCHAR2(2) | N |  |

- **PK** `PK_DEPARTMENT_SHIFT`: DEPARTMENT_ID, SHIFT_ID
- **Triggers**: `DEPARTMENT_SHIFT_CEA` (before insert or update or delete), `DEPARTMENT_SHIFT_DEL` (after delete), `DEPARTMENT_SHIFT_INS` (before insert), `DEPARTMENT_SHIFT_UPD` (before update), `TRG_WS_CSP_PR_YZ_Q` (after insert or update or delete)

## HRD.DEPARTMENT_WISE_WORKFORCE_PLAN

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NUMBER | NUMBER | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| YEAR_CODE | DATE | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| JOINING_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SALARY | NUMBER(20,3) | Y |  |
| NUMBER_OF_POSITIONS | NUMBER | Y |  |

- **PK** `PK_WORKFORCE_PLANNING`: DEPARTMENT_ID, DESIGNATION_ID, YEAR_CODE
- **FK** `FK_WORKFORCE_PLANNING_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **FK** `FK_WORKFORCE_PLANNING_2`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **CHECK** `CHK_WORKFORCE_PLANNING_1`: ACTIVE IN ('Y','N')
- **Triggers**: `DEPARTMENT_WISE_WORKFORCE_PLAN_DEL` (after delete), `DEPARTMENT_WISE_WORKFORCE_PLAN_INS` (before insert), `DEPARTMENT_WISE_WORKFORCE_PLAN_UPD` (before update), `DEPT_WISE_WORKFORCE_PLAN_DEL` (after delete), `DEPT_WISE_WORKFORCE_PLAN_INS` (before insert), `DEPT_WISE_WORKFORCE_PLAN_UPD` (before update)

## HRD.DEPT_DESIG_ORDER

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| REPORT_ORDER | NUMBER(4) default 9999 | N |  |
| DESIGNATION_INCLUDE | CHAR(1) default 'Y' | N |  |
| INCLUDE_IN_SUM | CHAR(1) default 'Y' | Y |  |
| LEVEL_ID | VARCHAR2(6) default '001001' | N |  |

- **PK** `PK_DEPT_DESIG_ORDER`: DEPARTMENT_ID, DESIGNATION_ID, LEVEL_ID
- **FK** `FK_DEPT_DESIG_ORDER_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **FK** `FK_DEPT_DESIG_ORDER_2`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **CHECK** `CK_DEPT_DESIG_ORDER_1`: DESIGNATION_INCLUDE IN ('Y','N')
- **Triggers**: `DEPT_DESIG_ORDER_DEL` (after delete), `DEPT_DESIG_ORDER_INS` (before insert), `DEPT_DESIG_ORDER_UPD` (before update)

## HRD.DEPT_OBJECTIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | Y |  |
| EMP_CODE | NUMBER(20) | Y |  |
| NAME | VARCHAR2(50) | Y |  |
| DEPARTMENT | VARCHAR2(40) | Y |  |
| OBJECTIVE | VARCHAR2(1000) | Y |  |


## HRD.DEPT_WISE_CV_SHORTLIST_EMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `DEPT_WISE_CV_SHORTLIST_EMP_PK`: MRNO, DEPARTMENT_ID
- **Triggers**: `DEPT_WISE_CV_SHORTLIST_EMP_DEL` (after delete), `DEPT_WISE_CV_SHORTLIST_EMP_INS` (before insert), `DEPT_WISE_CV_SHORTLIST_EMP_UPD` (before update)

## HRD.DEPT_WISE_TRAVEL_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| HIERARCHY_ID | NUMBER(10) | N |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DEPT_WISE_TRAVEL_HIERARCHY`: DEPARTMENT_ID, HIERARCHY_ID, FROM_DATE, LOCATION_ID, ORGANIZATION_ID
- **FK** `FK_PK_DEPT_TRAVEL_HIERARCHY_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **FK** `FK_PK_DEPT_TRAVEL_HIERARCHY_2`: (HIERARCHY_ID) -> HRD.TR_HIERARCHY(HIERARCHY_ID) [disabled]
- **FK** `FK_PK_DEPT_TRAVEL_HIERARCHY_3`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_PK_DEPT_TRAVEL_HIERARCHY_4`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **Triggers**: `DEPT_WISE_TRAVEL_HIERARCHY_DEL` (after delete), `DEPT_WISE_TRAVEL_HIERARCHY_INS` (before insert), `DEPT_WISE_TRAVEL_HIERARCHY_UPD` (before update)

## HRD.DESIGNATION_CAREER_PATH

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CAREER_ID | VARCHAR2(4) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| CAREER_LEVEL | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DESIGNATION_CAREER_PATH`: DESIGNATION_CAREER_ID, DESIGNATION_ID

## HRD.DESIGNATION_CATEGORY_USERS

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DESIGNATION_CATEGORY`: DESIGNATION_CATEGORY_ID, MRNO
- **Triggers**: `DESIGNATION_CATEGORY_USERS_DEL` (after delete), `DESIGNATION_CATEGORY_USERS_INS` (before insert), `DESIGNATION_CATEGORY_USERS_UPD` (before update)

## HRD.DESIGNATION_CORRECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) | Y |  |
| DUPLICATE | CHAR(1) | N |  |
| PARENT_DESIGNATION_ID | VARCHAR2(6) | N |  |


## HRD.DESIGNATION_DOCMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DESIGNATION_ID | VARCHAR2(50) | N |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |

- **PK** `DESIGNATION_WISE_PK`: DOC_CATEGORY_ID, DOCUMENT_TYPE_ID, DESIGNATION_ID
- **Triggers**: `DESIGNATION_DOCMENT_TYPE_DEL` (after delete), `DESIGNATION_DOCMENT_TYPE_INS` (before insert), `DESIGNATION_DOCMENT_TYPE_UPD` (before update), `DESIG_WISE_DOC_DEL` (before delete), `DESIG_WISE_DOC_INSERT` (after insert or update of designation_id ,doc_category_id ,document_type_id)

## HRD.DESIGNATION_LEVEL

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| LEVEL_ID | NUMBER(10) | Y |  |
| DESIGNATION_DESC | VARCHAR2(500) | Y |  |
| FROM_SALARY | NUMBER(10) | Y |  |
| TO_SALARY | NUMBER(10) | Y |  |
| SUGGESTED_FROM_SALARY | NUMBER(10) default 0 | N |  |
| SUGGESTED_TO_SALARY | NUMBER(10) default 0 | N |  |
| LEVEL_STAGES | NUMBER(2) default 5 | N |  |
| STAGE_VALUE | NUMBER(10) default 0 | N |  |
| ORDER_BY | NUMBER(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

_No standard audit columns._

- **PK** `PK_DESIGNATION_LEVEL`: DESIGNATION_ID
- **FK** `FK_DESIGNATION_LEVEL_01`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **FK** `FK_DESIGNATION_LEVEL_02`: (LEVEL_ID) -> HRD.CAREER_PATH_LEVEL(LEVEL_ID) [disabled]

## HRD.DESIGNATION_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| DESIGNATION_CAREER_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DESIGNATION_TYPES`: DESIGNATION_TYPE_ID

## HRD.DESIGNATION_WSIE_HOURS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `DESIGNATION_WSIE_HOURS_PK`: DEPARTMENT_ID, DESIGNATION_ID
- **Triggers**: `DESIGNATION_WSIE_HOURS_DEL` (after delete), `DESIGNATION_WSIE_HOURS_INS` (before insert), `DESIGNATION_WSIE_HOURS_UPD` (before update)

## HRD.DISABLE_OS_ACCOUNT_HIST
This table use for save history of actions performed on any employee in Active Directory. 

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| EMAIL | VARCHAR2(60) | Y | REF HRD.INFORMATION.EMAIL (STORE USER EMAIL ADDRESS) |
| ENABLE_ACCOUNT | CHAR(1) | Y | N : Inactive, Y: Activation, E: Email Assignment, D: Designation change, T: Department, C: Cisco Ext, L: Location change, R: Role change, X:Discarded Record |
| REMARKS | VARCHAR2(300) | Y |  |
| JOB_STATUS | CHAR(1) default 'P' | N | P: Pending, C: Complete |
| RETRY_COUNT | NUMBER default 0 | N |  |
| QUEUE_DATE | DATE default SYSDATE | N | When request is generated |
| PERFORM_DATE | DATE | Y | When utility perform action on current request. |
| TITLE | VARCHAR2(200) | Y | Designation of Employee |
| DEPARTMENT | VARCHAR2(200) | Y | Department of Employee |
| DESCRIPTION | VARCHAR2(400) | Y | Designation of Employee in AD |
| SECTION | VARCHAR2(60) | Y | Section of Employee |
| ROLE | VARCHAR2(100) | Y |  |
| MANAGER | CHAR(1) default 'N' | Y |  |
| DIRECTOR | CHAR(1) | Y |  |
| HOD | CHAR(1) | Y |  |
| LOCATION | VARCHAR2(100) | Y |  |
| CISCO_EXTENSION | VARCHAR2(10) | Y |  |
| OS_USER | VARCHAR2(100) | Y |  |
| CENTRAL_LOCATION | VARCHAR2(3) | Y |  |


## HRD.DISABLE_OS_ACCOUNT_Q
This is que table for activity to be performed on Active Directory as per HIS settings

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| EMAIL | VARCHAR2(60) | N |  |
| ENABLE_ACCOUNT | CHAR(1) | N | N : Inactive, Y: Activation, E: Email Assignment, D: Designation change, T: Department, C: Cisco Ext, L: Location change, R: Role change, X:Discarded Record |
| REMARKS | VARCHAR2(500) | Y |  |
| JOB_STATUS | CHAR(1) default 'P' | N | P: Pending, C: Complete |
| RETRY_COUNT | NUMBER default 0 | N |  |
| QUEUE_DATE | DATE default Sysdate | N | Data insertion date |
| PERFORM_DATE | DATE | Y | When action was performed |
| OS_USER | VARCHAR2(100) | Y |  |
| TITLE | VARCHAR2(200) | Y | Designation of Employee |
| DEPARTMENT | VARCHAR2(200) | Y | Department of Employee |
| DESCRIPTION | VARCHAR2(400) | Y | Designation of Employee in AD |
| SECTION | VARCHAR2(60) | Y | Section of Employee |
| ROLE | VARCHAR2(100) | Y |  |
| MANAGER | CHAR(1) default 'N' | Y |  |
| DIRECTOR | CHAR(1) | Y |  |
| HOD | CHAR(1) | Y |  |
| LOCATION | VARCHAR2(100) | Y |  |
| CISCO_EXTENSION | VARCHAR2(10) | Y |  |
| CENTRAL_LOCATION | VARCHAR2(100) | Y | This column will use to mark HOD location central or not IF HOD of any central department THEN VALUE WILL BE "SKMT" else HIS DUTY LOCATION |

- **PK** `PK_DOA_Q`: MRNO, EMAIL

## HRD.DISCIPLINARY_ACTION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| DISCIPLINARY_ACTION_NO | VARCHAR2(7) | N |  |
| DISCIPLINARY_REASON_ID | VARCHAR2(6) | N |  |
| REMARKS | VARCHAR2(200) | Y |  |

- **PK** `PK_DISCIPLINARY_ACTION_DETAIL`: DISCIPLINARY_ACTION_NO, DISCIPLINARY_REASON_ID
- **FK** `FK_DISCIP_ACTION_DETAIL_1`: (DISCIPLINARY_REASON_ID) -> DEFINITIONS.DISCIPLINARY_REASON(DISCIPLINARY_REASON_ID)

## HRD.DISCIPLINARY_ACTION_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| DISCIPLINARY_ACTION_NO | VARCHAR2(7) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SPECIFIC_EXPLANATION | VARCHAR2(1000) | Y |  |
| EXPLANATION_DATE | DATE | Y |  |
| EMPLOYEE_COMMENTS | VARCHAR2(1000) | Y |  |
| EMPLOYEE_COMMENTS_DATE | DATE | Y |  |
| HRD_REVIEW | VARCHAR2(1000) | Y |  |
| HRD_REVIEW_DATE | DATE | Y |  |
| DISCIPLINARY_ACTION_ID | VARCHAR2(6) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| WITH_PAY | VARCHAR2(1) | Y |  |
| PAY_DEDUCTION_DAYS | NUMBER(3) | Y |  |
| GROSS_BASIC | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| AMOUNT | NUMBER(12,2) | Y |  |
| SUSPEND | VARCHAR2(1) | Y |  |
| CLEARED_DATE | DATE | Y |  |
| WITH_DRAW | VARCHAR2(1) default 'N' | N |  |
| WITH_DRAW_DATE | DATE | Y |  |

- **PK** `PK_DISCIPLINARY_ACTION_MASTER`: DISCIPLINARY_ACTION_NO
- **FK** `FK_DISCIP_ACTION_MASTER_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_DISCIP_ACTION_MASTER_2`: (DISCIPLINARY_ACTION_ID) -> DEFINITIONS.DISCIPLINARY_ACTION(DISCIPLINARY_ACTION_ID)
- **CHECK** `CK_DISCIPLINARY_ACTION_MASTER_001`: WITH_DRAW IN ('Y','N')

## HRD.DOCUMENT_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_CATEGORY_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_DOCUMENT_CATEGORY`: DOC_CATEGORY_ID

## HRD.DOCUMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LABEL | VARCHAR2(4000) | Y | THIS COLUMN CONTAINS HINTS |
| IS_REPORT | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(50) | Y |  |
| SECTION_ID | VARCHAR2(50) | Y |  |
| OBJECT_CODE | VARCHAR2(14) | Y |  |
| TABLE_SOURCE | VARCHAR2(1000) | Y |  |
| VERIFY_AUTHORITY | VARCHAR2(14) | Y |  |
| DOCUMENT_IDENTIFIER | VARCHAR2(500) | Y |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| IS_ALL_EMPLOYEE | CHAR(1) | Y |  |
| MRNO_IDENTIFIER | VARCHAR2(500) | Y |  |
| QUERY | VARCHAR2(4000) | Y |  |
| DOCUMENT_TYPE | CHAR(1) | Y | This column is contains value E expired M missing B for Both |
| CHECK_ROW_COUNT | CHAR(1) default 'N' | Y |  |
| CHECK_NOT_APPLICABLE | CHAR(1) default 'N' | Y | If description in the table is set to NA then missing queue will not ge generated for that document |

- **PK** `PK_DOCUMENT_TYPE`: DOCUMENT_TYPE_ID, DOC_CATEGORY_ID
- **FK** `FK_DOC_CAT`: (DOC_CATEGORY_ID) -> HRD.DOCUMENT_CATEGORY(DOC_CATEGORY_ID) [disabled]
- **Triggers**: `DOCUMENT_TYPE_DEL` (after delete), `DOCUMENT_TYPE_INS` (before insert), `DOCUMENT_TYPE_UPD` (before update)

## HRD.DOCUMENT_TYPE_EXPIRE_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LABEL | VARCHAR2(4000) | Y |  |
| IS_REPORT | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(50) | Y |  |
| SECTION_ID | VARCHAR2(50) | Y |  |
| OBJECT_CODE | VARCHAR2(14) | Y |  |
| TABLE_SOURCE | VARCHAR2(1000) | Y |  |
| VERIFY_AUTHORITY | VARCHAR2(14) | Y |  |
| DOCUMENT_IDENTIFIER | VARCHAR2(500) | Y |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| IS_ALL_EMPLOYEE | CHAR(1) | Y |  |
| MRNO_IDENTIFIER | VARCHAR2(500) | Y |  |
| QUERY | VARCHAR2(4000) | Y |  |
| DOCUMENT_TYPE | CHAR(1) | Y |  |
| IDENTIFIER_2 | VARCHAR2(2000) | Y |  |

- **FK** `DOCUMENT_TYPE_Q`: (DOCUMENT_TYPE_ID, DOC_CATEGORY_ID) -> HRD.DOCUMENT_TYPE(DOCUMENT_TYPE_ID, DOC_CATEGORY_ID) [disabled]
- **Triggers**: `DOCUMENT_TYPE_EXPIRE_Q_DEL` (after delete), `DOCUMENT_TYPE_EXPIRE_Q_INS` (before insert), `DOCUMENT_TYPE_EXPIRE_Q_UPD` (before update)

## HRD.DRT_EX

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DUTY_MONTH | VARCHAR2(20) | Y |  |
| DAY_TYPE | VARCHAR2(20) | Y |  |
| DUTY_DATE | DATE | Y |  |


## HRD.DUMMY_CARD_SWIPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_DAYS | DATE | Y |  |

- **Triggers**: `DUMMY_CARD_SWIPE_DEL` (after delete), `DUMMY_CARD_SWIPE_INS` (before insert), `DUMMY_CARD_SWIPE_UPD` (before update)

## HRD.DUMMY_LEAVE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| LEAVE_DATE | DATE | Y |  |
| LEAVE_DAY | VARCHAR2(20) | Y |  |
| APPROVED | VARCHAR2(1) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| LEAVE_SHORT_DESC | VARCHAR2(5) | Y |  |


## HRD.DUMMY_LEAVES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| LEAVE_DAY | VARCHAR2(20) | Y |  |
| APPROVED | VARCHAR2(1) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| LEAVE_SHORT_DESC | VARCHAR2(5) | Y |  |

- **PK** `PK_DUMMY_LEAVES`: MRNO, LEAVE_DATE
- **Triggers**: `DUMMY_LEAVES_DEL` (after delete), `DUMMY_LEAVES_INS` (before insert), `DUMMY_LEAVES_UPD` (before update)

## HRD.DUMMY_LETTER_TEMPLATE_REPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| SUBJECT | VARCHAR2(4000) | Y |  |
| HEADER | VARCHAR2(4000) | Y |  |
| BODY | CLOB | Y |  |
| FOOTER | VARCHAR2(4000) | Y |  |
| TEMPLATE_TYPE_ID | VARCHAR2(7) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

- **Triggers**: `DUMMY_LET_TEMP_REP_DEL` (after delete), `DUMMY_LET_TEMP_REP_INS` (before insert), `DUMMY_LET_TEMP_REP_UPD` (before update)

## HRD.SHIFT

| Column | Type | Null | Comment |
|---|---|---|---|
| SHIFT_ID | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| START_TIME | VARCHAR2(5) | Y |  |
| END_TIME | VARCHAR2(5) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| NORMAL_DURATION | NUMBER(5) | Y |  |
| RAMZAN_START_TIME | VARCHAR2(5) | Y |  |
| RAMZAN_END_TIME | VARCHAR2(5) | Y |  |
| RAMZAN_DURATION | NUMBER(5) | Y |  |
| LATE_ARRIVAL_MINUTES | NUMBER(3) | Y |  |
| EARLY_LEAVE_MINUTES | NUMBER(3) | Y |  |
| LOWER_LIMIT_DAY_GAP | NUMBER(1) | Y |  |
| LOWER_LIMIT | VARCHAR2(5) | Y |  |
| UPPER_LIMIT | VARCHAR2(5) | Y |  |
| UPPER_LIMIT_DAY_GAP | NUMBER(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| NIGHTS | NUMBER(1) default 0 | Y |  |
| CTO | NUMBER(1) default 1 | Y |  |
| END_TIME_DAY_GAP | NUMBER(1) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| TRANSPORT_ALLOWED | CHAR(1) | Y |  |
| TRANSPORT_ALLOWED_EMERGENCY | CHAR(1) | Y |  |
| SHIFT_FLAG | CHAR(1) default 'Y' | Y |  |
| WEEKLY_OFF_DAY | VARCHAR2(3) | Y | This column will use to mark shift wise weekly off |
| FORTNIGHTLY_OFF_DAY | VARCHAR2(3) | Y | This column will use to mark shift wise fortnightly off |
| FORTNIGHTLY_MARK_OPTION | CHAR(1) | Y | 'N' All Fortnightly On, 'A' Both Days Off, 'F' use for alternate of week mark fortnightly |

- **PK** `PK_SHIFT`: SHIFT_ID
- **CHECK** `CK_SHIFT_001`: ACTIVE IN ('N','Y','O')
- **Triggers**: `SHIFT_CEA` (before insert or update or delete), `SHIFT_DEL` (after delete), `SHIFT_INS` (before insert), `SHIFT_UPD` (before update), `TRG_WS_YVO_DG_LA_Q` (after insert or update or delete)

## HRD.DUTY_ROSTER
Store duty roster of employees

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | Store employee code |
| DUTY_DATE | DATE | N | Store duty date in accordance with employee |
| SHIFT_ID | VARCHAR2(2) | N | Store Shift ID Ex N for Night |
| REMARKS | VARCHAR2(200) | Y | Store comments/ remarks |
| OVER_TIME_ALLOWED | VARCHAR2(1) default 'N' | Y | Store either Y or N to indicate employee can take over time or not |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y | Store day/leave type id  Ex 001 for Duty Day, 011 for Casual Leave |
| SHORT_LEAVE | VARCHAR2(1) default 'N' | Y | Store either Y or N to indicate leave taken against day is short leave or not |
| LEAVE_TYPE_DESC | VARCHAR2(5) | Y | Store leave type description Ex DD for Duty Day |
| SHIFT_DESC | VARCHAR2(50) | Y | Store Shift description Ex Night, Morning etc |
| START_TIME | VARCHAR2(5) | Y | Store starting time of duty |
| END_TIME | VARCHAR2(5) | Y | Store ending time of duty |
| LOCATION_ID | VARCHAR2(3) | Y | Store duty location id Ex 001 for SKM |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y | Store duty ORDER location id for SKM |
| MUNAUL_POPULATE | CHAR(1) default 'N' | Y | this colum store information that duty roster is populated by single row |
| SERIAL_NO | NUMBER(3) default 1 | N |  |
| CALLING_OBJECT_CODE | VARCHAR2(11) | Y | THIS COLUMN WILL CONTAIN WHICH OBJECT UPDATE OR INSERT RECORD IN DUTY ROSTER |
| OLD_TR_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DUTY_ROSTER`: MRNO, DUTY_DATE, SHIFT_ID, SERIAL_NO
- **FK** `FK_DUTY_ROSTER_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_SHIFT_TYPE`: (SHIFT_ID) -> HRD.SHIFT(SHIFT_ID)
- **CHECK** `CK_DUTY_ROSTER_001`: SHORT_LEAVE IN ('N','Y')
- **Triggers**: `DUTY_ROSTER_DEL` (after delete), `DUTY_ROSTER_INS` (before insert), `DUTY_ROSTER_UPD` (before update)

## HRD.DUTY_ROSTER_OLD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DUTY_DATE | DATE | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| OVER_TIME_ALLOWED | VARCHAR2(1) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |

- **Triggers**: `DUTY_ROSTER_OLD_DEL` (after delete), `DUTY_ROSTER_OLD_INS` (before insert), `DUTY_ROSTER_OLD_UPD` (before update)

## HRD.DUTY_ROSTER_TABULAR

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DUTY_MONTH | VARCHAR2(6) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| DAY_1 | VARCHAR2(5) | Y |  |
| DAY_2 | VARCHAR2(5) | Y |  |
| DAY_3 | VARCHAR2(5) | Y |  |
| DAY_4 | VARCHAR2(5) | Y |  |
| DAY_5 | VARCHAR2(5) | Y |  |
| DAY_6 | VARCHAR2(5) | Y |  |
| DAY_7 | VARCHAR2(5) | Y |  |
| DAY_8 | VARCHAR2(5) | Y |  |
| DAY_9 | VARCHAR2(5) | Y |  |
| DAY_10 | VARCHAR2(5) | Y |  |
| DAY_11 | VARCHAR2(5) | Y |  |
| DAY_12 | VARCHAR2(5) | Y |  |
| DAY_13 | VARCHAR2(5) | Y |  |
| DAY_14 | VARCHAR2(5) | Y |  |
| DAY_15 | VARCHAR2(5) | Y |  |
| DAY_16 | VARCHAR2(5) | Y |  |
| DAY_17 | VARCHAR2(5) | Y |  |
| DAY_18 | VARCHAR2(5) | Y |  |
| DAY_19 | VARCHAR2(5) | Y |  |
| DAY_20 | VARCHAR2(5) | Y |  |
| DAY_21 | VARCHAR2(5) | Y |  |
| DAY_22 | VARCHAR2(5) | Y |  |
| DAY_23 | VARCHAR2(5) | Y |  |
| DAY_24 | VARCHAR2(5) | Y |  |
| DAY_25 | VARCHAR2(5) | Y |  |
| DAY_26 | VARCHAR2(5) | Y |  |
| DAY_27 | VARCHAR2(5) | Y |  |
| DAY_28 | VARCHAR2(5) | Y |  |
| DAY_29 | VARCHAR2(5) | Y |  |
| DAY_30 | VARCHAR2(5) | Y |  |
| DAY_31 | VARCHAR2(5) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| WORKING_AREA_ID | VARCHAR2(7) | Y |  |
| SERIAL_NO | NUMBER(3) default 1 | N |  |
| MUNAUL_POPULATE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DUTY_ROSTER_TABULAR`: MRNO, DUTY_MONTH, DEPARTMENT_ID, SERIAL_NO
- **Triggers**: `DUTY_ROSTER_TABULAR_DEL` (after delete), `DUTY_ROSTER_TABULAR_INS` (before insert), `DUTY_ROSTER_TABULAR_UPD` (before update)

## HRD.DUTY_ROSTER_TABULAR_HEADER

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_MONTH | VARCHAR2(6) | N |  |
| DAY_1 | DATE | Y |  |
| DAY_2 | DATE | Y |  |
| DAY_3 | DATE | Y |  |
| DAY_4 | DATE | Y |  |
| DAY_5 | DATE | Y |  |
| DAY_6 | DATE | Y |  |
| DAY_7 | DATE | Y |  |
| DAY_8 | DATE | Y |  |
| DAY_9 | DATE | Y |  |
| DAY_10 | DATE | Y |  |
| DAY_11 | DATE | Y |  |
| DAY_12 | DATE | Y |  |
| DAY_13 | DATE | Y |  |
| DAY_14 | DATE | Y |  |
| DAY_15 | DATE | Y |  |
| DAY_16 | DATE | Y |  |
| DAY_17 | DATE | Y |  |
| DAY_18 | DATE | Y |  |
| DAY_19 | DATE | Y |  |
| DAY_20 | DATE | Y |  |
| DAY_21 | DATE | Y |  |
| DAY_22 | DATE | Y |  |
| DAY_23 | DATE | Y |  |
| DAY_24 | DATE | Y |  |
| DAY_25 | DATE | Y |  |
| DAY_26 | DATE | Y |  |
| DAY_27 | DATE | Y |  |
| DAY_28 | DATE | Y |  |
| DAY_29 | DATE | Y |  |
| DAY_30 | DATE | Y |  |
| DAY_31 | DATE | Y |  |

- **PK** `PK_DUTY_ROSTER_TABULAR_HEADER`: DUTY_MONTH

## HRD.EMPLOYEE_ANNUAL_LEAVES
Store information regarding applied/availed annual leaves of  employees

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_START | DATE | N | Store year starting date for which annual leave is applied |
| YEAR_END | DATE | Y | Store year ending date for which annual leave is applied |
| ACTUAL_LEAVE_START | DATE | Y | Store date on which leave actually started |
| ACTUAL_LEAVE_END | DATE | Y | Store date on which leave actually ended |
| VOUCHER_TYPE | VARCHAR2(5) | Y | Store voucher type generated against annual leave by Finance department Ex DUM or BPV |
| VOUCHER_NO | CHAR(13) | Y | Store voucher number generated against voucher type by Finance department |
| MRNO | VARCHAR2(14) | N | Store employee code |
| REMARKS | VARCHAR2(1000) | Y |  |
| EMAIL_TO_FINANCE | CHAR(1) default 'N' | Y |  |
| MONTH_START_DATE | DATE | Y | Reference from definitions pk |
| MONTH_END_DATE | DATE | Y | Reference from definitions pk |

- **PK** `PK_EMPLOYEE_ANNUAL_LEAVES`: YEAR_START, MRNO
- **FK** `FK_EMPLOYEE_ANNUAL_LEAVES_1`: (VOUCHER_TYPE, VOUCHER_NO) -> FINANCE.GL_TRAN_MASTER(VOUCHER_TYPE, VOUCHER_NO) [disabled]
- **Triggers**: `EMPLOYEE_ANNUAL_LEAVES_DEL` (after delete), `EMPLOYEE_ANNUAL_LEAVES_INS` (before insert), `EMPLOYEE_ANNUAL_LEAVES_UPD` (before update)

## HRD.EMPLOYEE_BENEFIT_DETAILS

| Column | Type | Null | Comment |
|---|---|---|---|
| BENEFIT_DETAIL_ID | NUMBER | N |  |
| BENEFIT_ID | NUMBER | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| ENTITLEMEN_OF_CAR | VARCHAR2(500) | Y |  |
| AMOUNT | NUMBER | Y |  |
| FUEL | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `EMPLOYEE_BENEFIT_DETAILS`: BENEFIT_DETAIL_ID, MRNO, START_DATE
- **Triggers**: `EMPLOYEE_BENEFIT_DETAILS_DEL` (after delete), `EMPLOYEE_BENEFIT_DETAILS_INS` (before insert), `EMPLOYEE_BENEFIT_DETAILS_UPD` (before update)

## HRD.EMPLOYEE_CARD_EXEMPTION_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| CARD_EXEMPTION | VARCHAR2(1) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_CARD_EXEMPTION_HIST`: MRNO, START_DATE
- **FK** `FK_CARD_EXEMPTION_HIST_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **CHECK** `CHK_EMP_CARD_SWIPE_HIST`: CARD_EXEMPTION IN ('N','Y','O')

## HRD.EMPLOYEE_CARD_EXPIRY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| ISSUE_DATE | DATE | Y |  |
| EXPIRY_DATE | DATE | N |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_CARD_EXPIRY`: MRNO, EXPIRY_DATE
- **FK** `FK_MRNO`: (MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **Triggers**: `EMPLOYEE_CARD_EXPIRY_DEL` (after delete), `EMPLOYEE_CARD_EXPIRY_INS` (before insert), `EMPLOYEE_CARD_EXPIRY_UPD` (before update), `TRG_WS_HR_EMP_EIR_Q` (after insert or update or delete)

## HRD.EMPLOYEE_CONCLUSION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| INCIDENT_ID | VARCHAR2(20) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| IPC_SRNO | VARCHAR2(20) | Y |  |
| SR_NO | VARCHAR2(20) | Y |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |

- **Triggers**: `EMPLOYEE_CONCLUSION_DETAIL_DEL` (after delete), `EMPLOYEE_CONCLUSION_DETAIL_INS` (before insert), `EMPLOYEE_CONCLUSION_DETAIL_UPD` (before update)

## HRD.EMPLOYEE_CONTRACT
Not in Use

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(2) | N |  |
| CONTRACT_TYPE_ID | VARCHAR2(3) | Y |  |
| PROBATION_PERIOD | NUMBER(3) | Y |  |
| MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| NO_OF_CHILDREN_ALLOWED | NUMBER(2) default 0 | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_EMPLOYEE_CONTRACT`: MRNO, SERIAL_NO
- **Triggers**: `EMPLOYEE_CONTRACT_DEL` (after delete), `EMPLOYEE_CONTRACT_INS` (before insert), `EMPLOYEE_CONTRACT_UPD` (before update)

## HRD.EMPLOYEE_CONTRACT_HISTORY
Store employee current as well as previous contract information

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | Store employee code |
| START_DATE | DATE | N | Store contract starting date |
| END_DATE | DATE | Y | Store contract ending date |
| CONTRACT_ID | VARCHAR2(3) | N | Store contract id of employee |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| EMPLOYEE_TYPE | VARCHAR2(1) | Y | Store employee type id of employee Ex R for Regular, I for Internee |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y | Store Patient type id of employee Ex 001003 for EMPLOYEE(REGULAR) |
| IS_HOLD | CHAR(1) default 'N' | Y |  |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENTS |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| CONTRACT_CATEGORY | VARCHAR2(3) | Y | This column contains Contract Category details, if 'C' Employment Contract and 'E' for Extension of Contract |

- **PK** `PK_CONTRACT_HISTORY`: MRNO, START_DATE
- **FK** `FK_EMP_CONTRACT_HISTORY_1`: (CONTRACT_ID) -> HRD.CONTRACT_TYPE(CONTRACT_TYPE_ID) [disabled]
- **FK** `FK_EMP_CONTRACT_HISTORY_2`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_CONTRACT_HISTORY_3`: (EMPLOYEE_TYPE) -> HRD.EMPLOYEE_TYPE(EMPLOYEE_TYPE_ID)
- **FK** `FK_EMP_CONTRACT_HISTORY_4`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **Triggers**: `EMPLOYEE_CONTRACT_HISTORY_DEL` (after delete), `EMPLOYEE_CONTRACT_HISTORY_INS` (before insert), `EMPLOYEE_CONTRACT_HISTORY_UPD` (before update), `EMP_CONTRACT_PENDING_DEL` (after insert or update), `EMP_CONTRACT_PI_CNT_DTL_UPD` (after update), `TR_CONTRACT_EXPIRE_QUEUE_DEL` (after insert or update)

## HRD.EMPLOYEE_CONTRACT_LEAVES
Store leaves allowed information in accordance with contract type

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | Store employee code |
| SERIAL_NO | NUMBER(2) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Store leave type id Ex 011, 012 |
| NO_OF_LEAVES_ALLOWED | NUMBER(3) default 0 | Y | Store number of leaves allowed in accordance with leave type Ex 8 for 012 |

- **PK** `PK_EMPLOYEE_CONTRACT_LEAVES`: MRNO, SERIAL_NO, LEAVE_TYPE_ID
- **Triggers**: `EMPLOYEE_CONTRACT_LEAVES_DEL` (after delete), `EMPLOYEE_CONTRACT_LEAVES_INS` (before insert), `EMPLOYEE_CONTRACT_LEAVES_UPD` (before update)

## HRD.EMPLOYEE_CRIMINAL_CHARGES

| Column | Type | Null | Comment |
|---|---|---|---|
| CRIMINAL_CHARGES_ID | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |

- **PK** `PK_EMPLOYEE_CRIMINAL_CHARGES`: CRIMINAL_CHARGES_ID, MRNO
- **Triggers**: `EMPLOYEE_CRIMINAL_CHARGES_DEL` (after delete), `EMPLOYEE_CRIMINAL_CHARGES_INS` (before insert), `EMPLOYEE_CRIMINAL_CHARGES_UPD` (before update)

## HRD.EMPLOYEE_DEPARTMENT_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENTS |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |

- **PK** `PK_DEPARTMENT_HISTORY`: MRNO, START_DATE
- **FK** `FK_EMP_DEPARTMENT_HIST_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_DEPARTMENT_HIST_2`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **Triggers**: `CURRENT_EMP_DEPARTMENT_INS` (after update), `CURRENT_EMP_DEPARTMENT_UPDATE` (after insert or update), `EMPLOYEE_DEPARTMENT_HISTORY_CEA` (before insert or update or delete), `EMPLOYEE_DEPARTMENT_HISTORY_DEL` (after delete), `EMPLOYEE_DEPARTMENT_HISTORY_INS` (before insert), `EMPLOYEE_DEPARTMENT_HISTORY_UPD` (before update), `EMPLOYEE_DEPT_HISTORY_DEL` (after delete), `EMPLOYEE_DEPT_HISTORY_INS` (before insert), `EMPLOYEE_DEPT_HISTORY_UPD` (before update), `EMP_DEPT_COST_CENTER_REFRESH` (after insert or update), `EMP_DEPT_RFID_ACCESS_REFRESH` (after insert or update), `TRG_EMPLOYEE_DEPARTMENT_AD_QUEUE` (after insert or update or delete), `TRG_WS_VHQ_XO_LK_Q` (after insert or update or delete)

## HRD.EMPLOYEE_DEPENDANT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPENDANT_MRNO | VARCHAR2(14) | N |  |
| RELATION_ID | VARCHAR2(6) | Y |  |
| FIRST_NAME | VARCHAR2(50) | Y |  |
| MIDDLE_NAME | VARCHAR2(50) | Y |  |
| LAST_NAME | VARCHAR2(50) | Y |  |
| ELIGIBLE | VARCHAR2(1) default 'Y' | Y |  |
| INELIGIBILITY_REASON_ID | VARCHAR2(6) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains ATTACHMENT DESCRIPTION |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENT |
| LIMIT_ALLOWED | CHAR(1) default 'N' | Y | This Flag is used for treatment limit checking against employee dependant if flag marked as 'Y' then comment limit used for employee and dependant. |
| NIC_NEW | VARCHAR2(13) | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |
| NEW_DEPENDANT_MRNO | VARCHAR2(14) | Y | This column contains value of new MRNO generated through script against already existing Dependant MRNO(which was constituted using old scheme of generating dependant MRNOs) |
| TRANS_DATE | DATE | Y |  |
| NEW_MRNO_SCHEME | CHAR(1) | Y |  |
| FORMER_DEP_MRNO | VARCHAR2(14) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |
| IS_MEDICAL_ALLOWED | CHAR(1) | Y | This column is only for Employees (this column show that whether this patient is entiteled for free treatment in SKMCH or not) Values: Y and N |
| ACTIVE | CHAR(1) | Y | EMPLOYEE is still active patient of SKMCH or not Values:Y and N |
| CNIC_SUBMIT | CHAR(1) default 'N' | Y |  |
| CNIC_HOLDER_RELATION_ID | VARCHAR2(6) | Y |  |
| CNIC_SUBMIT_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |

- **PK** `PK_EMPLOYEE_DEPENDANT`: DEPENDANT_MRNO
- **FK** `FPK_EMPLOYEE_DEPENDANT`: (MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **Triggers**: `EMPLOYEE_DEPENDANT_DEL` (after delete), `EMPLOYEE_DEPENDANT_INS` (before insert), `EMPLOYEE_DEPENDANT_TRG01` (after insert or update), `EMPLOYEE_DEPENDANT_UPD` (before update), `SMS_TO_EMP_DEPENDENT_REG` (after insert), `TRG_UPDATE_PATIENT` (after update of is_medical_allowed, active), `TRG_WS_HR_EEE_E_Q` (after insert or update or delete)

## HRD.EMPLOYEE_DESIGNATION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENTS |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |

- **PK** `PK_DESIGNATION_HISTORY`: MRNO, START_DATE
- **FK** `FK_EMPLOYEE_DESIGNATION_HISTORY_001`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `EMPLOYEE_DESIGNATION_HISTORY_CEA` (before insert or update or delete), `EMPLOYEE_DESIGNATION_HISTORY_DEL` (after delete), `EMPLOYEE_DESIGNATION_HISTORY_INS` (before insert), `EMPLOYEE_DESIGNATION_HISTORY_UPD` (before update), `EMPLOYEE_DESIG_HISTORY_DEL` (after delete), `EMPLOYEE_DESIG_HISTORY_INS` (before insert), `EMPLOYEE_DESIG_HISTORY_UPD` (before update), `EMP_DESIG_RFID_ACCESS_REFRESH` (after insert or update), `TRG_WS_TIQ_HC_RP_Q` (after insert or update or delete)

## HRD.EMPLOYEE_DOCUMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| SR_NO | NUMBER(5) | N |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(100) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHMENT_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| JOINING_DATE | DATE | Y |  |
| DOC_CATEGORY_ID | NUMBER | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LABEL | VARCHAR2(4000) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| PA_YEAR | VARCHAR2(10) | Y | This column contain  pa year for appraisal data |
| PA_TYPE_ID | NUMBER(2) | Y | This column contain  pa type ID for appraisal data |
| ORDER_BY | NUMBER | Y | This column contains numeric value to set order by |
| RECORD_DATE | DATE | Y | This column contains record date |

- **PK** `PK_EMP_DOCUMENTS`: SR_NO, MRNO
- **FK** `FK_1_MRNO`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **Triggers**: `EMPLOYEE_DOCUMENTS_DEL` (after delete), `EMPLOYEE_DOCUMENTS_INS` (before insert), `EMPLOYEE_DOCUMENTS_UPD` (before update)

## HRD.EMPLOYEE_DUTY_LOCATION_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(3) | N |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EMPLOYEE_DUTY_LOCATION_HIST`: MRNO, START_DATE
- **FK** `FK_EMP_DUTY_LOCATION_HIST_1`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_EMP_DUTY_LOCATION_HIST_2`: (DUTY_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `EMP_DUTY_LOCATION_HIST_DEL` (after delete), `EMP_DUTY_LOCATION_HIST_INS` (before insert), `EMP_DUTY_LOCATION_HIST_UPD` (before update), `EMP_DUTY_LOC_HIST_DR_LOC_UPD` (before insert or update), `FPPE_EMP_DUTY_LOC_UPD` (after insert or update)

## HRD.EMPLOYEE_EVALUATION_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| EVALUATION_TYPE | VARCHAR2(3) | Y | CHECK EVALUATION TYPE |
| START_DATE | DATE | Y | CHECK START DATE |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y | USE FOR GIVEN REMARKS |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| IS_CORRESPONDENCE | CHAR(1) default 'N' | Y |  |

- **PK** `EMP_EVA_ATTACHMENT_PK`: SR_NO, MRNO
- **Triggers**: `EMP_EVALUATION_ATTACHMENT_DEL` (after delete), `EMP_EVALUATION_ATTACHMENT_INS` (before insert), `EMP_EVALUATION_ATTACHMENT_UPD` (before update)

## HRD.EMPLOYEE_EVALUATION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N | CONSULTANT EVALUACTION START DATE |
| END_DATE | DATE | Y | CONSULTANT EVALUACTION START END |
| TRANSACTION_DATE | DATE | Y | DATA ENTRY DATE |
| REMARKS | VARCHAR2(2000) | Y | OPEN REMARKS FIELD |
| EVALUATION_PERIOD | NUMBER(7,2) | N | EVALUDATION DAYS |
| EVALUATION_REASON_ID | VARCHAR2(3) | Y |  |
| EVALUATION_STATUS | VARCHAR2(1) | N | STATUS IN 'C' COMPLETED , 'E' EXTEND 'P' PENDING 'I' IN PROCESS |
| EVALUATION_TYPE | VARCHAR2(3) | N | ALERT ID REF TO HRD.ALERTS |
| ACTIVE | CHAR(1) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| EMP_JOINING_DATE | DATE | Y |  |
| DOCUMENT_ID_CNFM | VARCHAR2(13) | Y |  |
| ATTACHED_BY_CNFM | VARCHAR2(14) | Y |  |

- **PK** `PK_EVALUATION_HIST`: MRNO, START_DATE, EVALUATION_TYPE
- **Triggers**: `EMPLOYEE_EVALUATION_HISTORY_DEL` (after delete), `EMPLOYEE_EVALUATION_HISTORY_INS` (before insert), `EMPLOYEE_EVALUATION_HISTORY_UPD` (before update), `EMP_EVA_HISTORY_DEL` (after delete), `EMP_EVA_HISTORY_INS` (before insert), `EMP_EVA_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_EXPLANATION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_EXPLANATION_HISTORY`: MRNO, START_DATE
- **FK** `FK_EXPLANATION_HISTORY_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `EMPLOYEE_EXPLANATION_HISTORY_DEL` (after delete), `EMPLOYEE_EXPLANATION_HISTORY_INS` (before insert), `EMPLOYEE_EXPLANATION_HISTORY_UPD` (before update), `EMPLOYEE_EXPLNATION_HIST_DEL` (after delete), `EMPLOYEE_EXPLNATION_HIST_INS` (before insert), `EMPLOYEE_EXPLNTION_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_EXTRA_SKILLS

| Column | Type | Null | Comment |
|---|---|---|---|
| EXTRA_SKILL_ID | NUMBER(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| PROFICIENCY_LEVEL_ID | NUMBER(1) | Y |  |

- **PK** `PK_EMPLOYEE_EXTRA_SKILLS`: EXTRA_SKILL_ID, MRNO
- **Triggers**: `EMPLOYEE_EXTRA_SKILLS_DEL` (after delete), `EMPLOYEE_EXTRA_SKILLS_INS` (before insert), `EMPLOYEE_EXTRA_SKILLS_UPD` (before update)

## HRD.EMPLOYEE_FACE_SHEET

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SR_NO | NUMBER | N |  |
| DATED | DATE | Y |  |
| SUBJECT | VARCHAR2(50) | Y |  |
| HOUR_COUNT | NUMBER | Y |  |
| FACILITATOR | VARCHAR2(100) | Y |  |
| CERTIFICATE | VARCHAR2(100) | Y |  |
| DESCRITION | VARCHAR2(500) | Y |  |
| FILLING_DATE | DATE | Y |  |

- **PK** `PK_EMP_FACE_SHEET`: MRNO, SR_NO
- **Triggers**: `EMPLOYEE_FACE_SHEET_DEL` (after delete), `EMPLOYEE_FACE_SHEET_INS` (before insert), `EMPLOYEE_FACE_SHEET_UPD` (before update)

## HRD.EMPLOYEE_FINANCIAL_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_LOCATION_ID | VARCHAR2(3) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| EMPLOYEE_NATURE | CHAR(1) default 'O' | N | O FOR OTHERS, C FOR CONSULTANTS, D FOR DOCTORS, N FOR NURSES |
| COST_CENTRE_ID | CHAR(10) | Y |  |
| PAY_GL_SETUP_CODE | CHAR(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| POSITION_LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_EMP_FINANCIAL_SETUP`: DUTY_LOCATION_ID, DEPARTMENT_ID, SECTION_ID, EMPLOYEE_NATURE, POSITION_LOCATION_ID
- **FK** `FK_EMP_FINANCIAL_SETUP_1`: (DUTY_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_EMP_FINANCIAL_SETUP_2`: (DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.DEPARTMENT_SECTION(DEPARTMENT_ID, SECTION_ID) [disabled]
- **FK** `FK_EMP_FINANCIAL_SETUP_3`: (COST_CENTRE_ID) -> DEFINITIONS.GL_DIV_DEPT_CC(COST_CENTRE_ID) [disabled]
- **FK** `FK_EMP_FINANCIAL_SETUP_5`: (POSITION_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `EMPLOYEE_FINANCIAL_SETUP_DEL` (after delete), `EMPLOYEE_FINANCIAL_SETUP_INS` (before insert), `EMPLOYEE_FINANCIAL_SETUP_UPD` (before update)

## HRD.EMPLOYEE_GRADE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_GRADE_HISTORY`: MRNO, START_DATE
- **FK** `FK_EMP_GRADE_HIST_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_GRADE_HIST_2`: (GRADE_ID) -> DEFINITIONS.GRADES(GRADE_ID) [disabled]
- **Triggers**: `EMPLOYEE_GRADE_HISTORY_DEL` (after delete), `EMPLOYEE_GRADE_HISTORY_INS` (before insert), `EMPLOYEE_GRADE_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_HOBBIES
Not In Use

| Column | Type | Null | Comment |
|---|---|---|---|
| HOBBY_ID | NUMBER(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |

- **PK** `PK_EMPLOYEE_HOBBIES`: HOBBY_ID, MRNO
- **Triggers**: `EMPLOYEE_HOBBIES_DEL` (after delete), `EMPLOYEE_HOBBIES_INS` (before insert), `EMPLOYEE_HOBBIES_UPD` (before update)

## HRD.EMPLOYEE_JDS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| SR_NO | NUMBER | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| EMP_JOINING_DATE | DATE | Y |  |
| IS_CURRENT | CHAR(1) default 'N' | Y | This column contains value Y or N |
| ACTIVE | CHAR(1) default 'Y' | Y | This column contains value Y or N |
| SIGNED_DATE | DATE | Y | This column contains SIGNED DATE |
| START_DATE | DATE | Y |  |

- **Triggers**: `EMPLOYEE_JDS_DEL` (after delete), `EMPLOYEE_JDS_INS` (before insert), `EMPLOYEE_JDS_UPD` (before update)

## HRD.EMPLOYEE_JOINING_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| OFFER_DATE | DATE | Y | Date on which applicant is called for medical |
| MEDICAL_DATE | DATE | Y | This column can contain either the date on which applicant gets medical clearance  or get medical rejection. If applicant is medically rejected then reason will be mandatory to store in MEDICAL_REJECTION_ID column |
| JOINING_DATE | DATE | Y | Date on which employee joins the organization |
| LEAVING_DATE | DATE | Y | Date on which employee leaves the organization. Record cannot be updated after leaving date is provided |
| MEDICAL_REJECTION_ID | NUMBER | Y |  |
| LEAVING_REASON_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| STATUS | CHAR(1) default 'N' | N |  |
| ASSETS_REMARKS | VARCHAR2(3000) | Y | This column will use when assets are pending and hr department try to job terminal there is will store against employee joining |
| ASSETS_REMARKS_BY | VARCHAR2(14) | Y |  |
| ASSETS_REMARKS_DATE | DATE | Y |  |

- **PK** `PK_EMPLOYEE_JOINING_DATE`: SERIAL_NO, MRNO
- **UK** `UK_EMPLOYEE_JOINING_DATE_1`: MRNO, JOINING_DATE, STATUS
- **FK** `FK_EMPLOYEE_JOINING_DATE_1`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_EMPLOYEE_JOINING_DATE_3`: (LEAVING_REASON_ID) -> HRD.JOB_LEAVING_REASON(REASON_ID) [disabled]
- **Triggers**: `CURRENT_EMPLOYEE_JOINING_HISTORY` (after insert or update ), `EMPLOYEE_EVALUATION_HIST_INS` (after insert or update of joining_date), `EMPLOYEE_EVALUATION_HIST_UPD` (after update), `EMPLOYEE_JOINING_HISTORY_CEA` (before insert or update or delete), `EMPLOYEE_JOINING_HISTORY_DEL` (after delete), `EMPLOYEE_JOINING_HISTORY_INS` (before insert), `EMPLOYEE_JOINING_HISTORY_UPD` (before update), `EMPLOYEE_JOINING_HIST_INS_INFO` (after insert), `EMP_MANDATORY_TRAINING_INS` (after insert or update of joining_date), `FPPE_EMP_JOINING_DATE_UPD` (after insert or update), `NEW_JOINER_ACTIVITY` (after insert), `TRG_WS_WHC_RA_WR_Q` (after insert or update or delete)

## HRD.EMPLOYEE_LEAVES
Store employee leave total duration

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | Employee Code |
| SERIAL_NO | NUMBER(5) | N | Autogenerated number associated with Employee code and leace type |
| FROM_DATE | DATE | N | Leave starting date |
| TO_DATE | DATE | N | Leave ending date |
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Store Leave type id ex 016 for Earned leave |
| LEAVE_REASON | VARCHAR2(800) | Y | Store leave reason |
| APPROVED_FROM_DATE | DATE | Y | Store date from which leave is approved |
| APPROVED_TO_DATE | DATE | Y | Store date till which leave is approved |
| TOTAL_LEAVE_DAYS | NUMBER(7,2) | Y | Store total leave days |
| NORMAL_EMERGENCY | VARCHAR2(1) default 'N' | Y |  |
| APPROVED | VARCHAR2(1) | N |  |
| REMARKS | VARCHAR2(200) | Y | Store remarks against leave |
| SHORT_LEAVE | VARCHAR2(1) default 'N' | Y |  |
| ENTERED_DATE | DATE | Y | Store date on which leave is entered by the user |
| ADVANCE_PERIOD | CHAR(1) default 'N' | N |  |
| DATE_RETURN_TO_WORK | DATE | Y | Store date when employee return on duty after availing leave |
| ACTOR_MRNO | VARCHAR2(14) | Y | Store speciifed employee code who will be responsible in absence of employee on leave |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| IS_CONSULTANT_STAFF_AVAILABLE | CHAR(1) default 'N' | Y |  |
| IS_CLINICAL_ACTIVITIES | CHAR(1) default 'N' | Y |  |
| SHORT_LEAVE_HALF | CHAR(1) default 'N' | Y | This column contains FIRST F OR 2ND HALF S |
| CLINICAL_ACTOR_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_EMPLOYEE_LEAVES`: MRNO, SERIAL_NO
- **FK** `FK_EMPLOYEE_LEAVES_1`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **CHECK** `CK_EMPLOYEE_LEAVES_1`: ADVANCE_PERIOD IN ('Y','N')
- **CHECK** `CK_EMPLOYEE_LEAVES_2`: APPROVED IN ('Y','N','I','W')
- **CHECK** `CK_EMPLOYEE_LEAVES_3`: APPROVED IN ('Y','N','W','I')
- **Triggers**: `EMPLOYEE_LEAVES_DEL` (after delete), `EMPLOYEE_LEAVES_INS` (before insert), `EMPLOYEE_LEAVES_UPD` (before update)

## HRD.EMPLOYEE_LEAVES_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| LEAVE_REASON | VARCHAR2(800) | Y |  |
| APPROVED_FROM_DATE | DATE | Y |  |
| APPROVED_TO_DATE | DATE | Y |  |
| TOTAL_LEAVE_DAYS | NUMBER(7,2) | Y |  |
| NORMAL_EMERGENCY | VARCHAR2(1) | Y |  |
| APPROVED | VARCHAR2(1) | N |  |
| REMARKS | VARCHAR2(200) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ADVANCE_PERIOD | CHAR(1) | N |  |
| DATE_RETURN_TO_WORK | DATE | Y |  |
| ACTOR_MRNO | VARCHAR2(14) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |

- **Triggers**: `EMPLOYEE_LEAVES_HIST_DEL` (after delete), `EMPLOYEE_LEAVES_HIST_INS` (before insert), `EMPLOYEE_LEAVES_HIST_UPD` (before update)

## HRD.ROLE_CHECKLIST_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| ROLE_ID | NUMBER(10) | N |  |
| PARAM_ID | NUMBER(3) | N |  |

- **PK** `PK_ROLE_CHECKLIST_PARAM`: ROLE_ID, PARAM_ID

## HRD.EMPLOYEE_LEAVE_CHECKLIST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| ROLE_ID | NUMBER(3) | N |  |
| PARAM_ID | NUMBER(3) | N |  |
| VALUE | CHAR(1) | Y |  |
| REMARKS | CHAR(1000) | Y |  |

- **PK** `PK_EMPLOYEE_LEAVE_CHECKLIST`: MRNO, SERIAL_NO, ROLE_ID, PARAM_ID
- **FK** `FK_EMPLOYEE_LEAVE_CHECKLIST_1`: (ROLE_ID, PARAM_ID) -> HRD.ROLE_CHECKLIST_PARAM(ROLE_ID, PARAM_ID) [disabled]
- **FK** `FK_EMPLOYEE_LEAVE_CHECKLIST_2`: (MRNO, SERIAL_NO) -> HRD.EMPLOYEE_LEAVES(MRNO, SERIAL_NO)

## HRD.EMPLOYEE_LEAVE_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_START | DATE | N |  |
| YEAR_END | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| CURRENT_YEAR | NUMBER(6,2) | Y |  |
| LAST_YEAR_BALANCE | NUMBER(7,2) | Y |  |
| TOTAL_LEAVES | NUMBER(7,2) | Y |  |
| LEAVE_AVAILED | NUMBER(7,2) | Y |  |
| LEAVE_CARRIED_FORWARD | VARCHAR2(1) | Y |  |
| NO_CARRIED_FORWARD | NUMBER(7,2) default 0 | Y |  |
| ACCRUED_NO | NUMBER(7,2) | Y |  |
| LAPSED_NO | NUMBER(7,2) | Y |  |

- **PK** `PK_EMPLOYEE_LEAVE_SUMMARY`: MRNO, LEAVE_TYPE_ID, YEAR_START, YEAR_END
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_1`: CURRENT_YEAR IS NOT NULL
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_2`: LAST_YEAR_BALANCE IS NOT NULL
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_3`: TOTAL_LEAVES IS NOT NULL
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_4`: LEAVE_AVAILED IS NOT NULL
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_5`: LEAVE_CARRIED_FORWARD IS NOT NULL
- **CHECK** `CK_EMPLOYEE_LEAVE_SUMMARY_6`: NO_CARRIED_FORWARD IS NOT NULL
- **Triggers**: `EMPLOYEE_LEAVE_SUMMARY_DEL` (after delete), `EMPLOYEE_LEAVE_SUMMARY_INS` (before insert), `EMPLOYEE_LEAVE_SUMMARY_UPD` (before update)

## HRD.EMPLOYEE_LEAVE_SUMMARY_YEARLY

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(44) | N |  |
| NAME | VARCHAR2(192) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |
| LEAVING_DATE | DATE | Y |  |
| DEPARTMENT | VARCHAR2(32767) | Y |  |
| DESIGNATION | VARCHAR2(32767) | Y |  |
| JOINING_DATE | DATE | Y |  |
| OPENING_BALANCE | NUMBER(7,2) | Y |  |
| LAPSED_LEAVES | NUMBER | Y |  |
| LEAVE_ADDITION | NUMBER(6,2) | Y |  |
| LEAVE_AVAILED | NUMBER(7,2) | Y |  |
| CURRENT_BALANCE | NUMBER | Y |  |
| PRESENT_SALARY | NUMBER | Y |  |
| DOB | DATE | Y |  |
| YEARLY | CHAR(6) | N |  |

- **PK** `EMP_LEAVE_SUM_BACKUP_YEARLY`: EMP_CODE, YEARLY
- **Triggers**: `EMP_LEAVE_SUMMARY_YEARLY_DEL` (after delete), `EMP_LEAVE_SUMMARY_YEARLY_INS` (before insert), `EMP_LEAVE_SUMMARY_YEARLY_UPD` (before update)

## HRD.EMPLOYEE_PROBATION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| PROBATION_PERIOD | NUMBER(7,2) default 0 | N |  |
| PROBATION_REASON_ID | VARCHAR2(3) | Y |  |
| PROBATION_STATUS | VARCHAR2(1) default 'P' | N |  |
| DEPARTMENT_SHIFT | CHAR(1) default 'N' | Y | This column will be use to shift from one department to an other department |

- **PK** `PK_PROBATION_HISTORY`: MRNO, START_DATE
- **FK** `FK_PROBATION_HISTORY_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `EMPLOYEE_PROBATION_HISTORY_DEL` (after delete), `EMPLOYEE_PROBATION_HISTORY_INS` (before insert), `EMPLOYEE_PROBATION_HISTORY_UPD` (before update), `EMP_INCENTIVE_QUEUE` (after update of probation_status), `EMP_PROBATION_HISTORY_INFO_UPD` (after update), `TR_PROBATION_EXPIRE_QUEUE_DEL` (after insert or update of probation_status )

## HRD.EMPLOYEE_PROBATION_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | Y | CHECK START DATE |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y | USE FOR GIVEN  REMAKRS |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y | THIS COLUMN WILL STORES DOCUMENT TYPE ID |

- **PK** `EMP_PROB_ATCH_PK`: SR_NO, MRNO
- **FK** `FK_EMP_PROB_HIS`: (MRNO, START_DATE) -> HRD.EMPLOYEE_PROBATION_HISTORY(MRNO, START_DATE) [disabled]

## HRD.EMPLOYEE_PROMOTION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| GRADE_ID | VARCHAR2(6) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| FROM_DATE | DATE | Y |  |
| GROSS_SALRAY | NUMBER(12,2) | Y |  |

- **PK** `PK_EMPLOYEE_PROMOTION_HISTORY`: MRNO, GRADE_ID
- **Triggers**: `EMPLOYEE_PROMOTION_HISTORY_DEL` (after delete), `EMPLOYEE_PROMOTION_HISTORY_INS` (before insert), `EMPLOYEE_PROMOTION_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_QUALIFICATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| QUALIFICATION_ID | VARCHAR2(6) | N |  |
| MAJOR | VARCHAR2(100) | Y |  |
| INSTITUTE | VARCHAR2(255) | Y |  |
| DIVISION | NUMBER(1) | Y |  |
| DEGREE_DATE | DATE | Y |  |
| DISTINCTION | VARCHAR2(100) | Y |  |
| GPA | NUMBER(4,3) | Y |  |

- **PK** `PK_EMPLOYEE_QUALIFICATIONS`: MRNO, QUALIFICATION_ID
- **Triggers**: `EMPLOYEE_QUALIFICATIONS_DEL` (after delete), `EMPLOYEE_QUALIFICATIONS_INS` (before insert), `EMPLOYEE_QUALIFICATIONS_UPD` (before update)

## HRD.EMPLOYEE_RECORD_ATTACHMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N | this column will store value of SERIAL NO |
| DOCUMENT_ID | VARCHAR2(13) | Y | this column will store value of DOCUMENT ID |
| DESCRIPTION | VARCHAR2(4000) | Y | this column will store value of DESCRIPTION |
| ENTRY_DATE | DATE | Y | this column will store value of ENTRY DATE |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| TRAINING_ID | VARCHAR2(20) | N | this column will store value of training id and programe id |
| MRNO | VARCHAR2(14) | N |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| TRAINING_START_DATE | DATE | Y |  |
| TRAINING_END_DATE | DATE | Y |  |

- **PK** `PK_ATTACHMENT1`: MRNO, TRAINING_ID, SR_NO
- **Triggers**: `EMPLOYEE_RECORD_ATTACHMENTS_DEL` (after delete), `EMPLOYEE_RECORD_ATTACHMENTS_INS` (before insert), `EMPLOYEE_RECORD_ATTACHMENTS_UPD` (before update), `EMP_RECORD_ATTACH_DEL` (after delete), `EMP_RECORD_ATTACH_INS` (before insert), `EMP_RECORD_ATTACH_UPD` (before update)

## HRD.RESIGNATION_REASONS
Define possible resignation reasons

| Column | Type | Null | Comment |
|---|---|---|---|
| RESIGNATION_REASON_ID | VARCHAR2(6) | N | Store unique resignation reason id |
| DESCRIPTION | VARCHAR2(60) | Y | Store resignation reason descriptoin |
| ACTIVE | VARCHAR2(1) | Y | Define resignation id status as Y for active and N for inactive |

- **PK** `PK_RESIGNATION_REASONS`: RESIGNATION_REASON_ID
- **Triggers**: `RESIGNATION_REASONS_DEL` (after delete), `RESIGNATION_REASONS_INS` (before insert), `RESIGNATION_REASONS_UPD` (before update)

## HRD.EMPLOYEE_RESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| RESIGNATION_DATE | DATE | N |  |
| NOTIFICATION_DAYS | NUMBER(3) | N |  |
| LEAVING_DATE | DATE | Y |  |
| RESIGNATION_REASON_ID | VARCHAR2(6) | Y |  |
| APPROVED | VARCHAR2(1) | Y |  |
| APPROVAL_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| WITHDRAWL_DATE | DATE | Y |  |
| REJECTION_DATE | DATE | Y |  |
| EXTENSION_DAYS | NUMBER(3) default 0 | Y |  |
| LEAVING_REASON | VARCHAR2(2000) | Y |  |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENTS |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| SUBSTITUTE_START_DATE | DATE | Y |  |
| SUBSTITUTE_MRNO_CLINICAL | VARCHAR2(14) | Y |  |
| SUBSTITUTE_END_DATE | DATE | Y |  |
| IS_SUBSTITUTE_REQ | CHAR(1) | Y |  |
| SUBSTITUTE_MRNO | CHAR(14) | Y |  |

- **PK** `PK_EMPLOYEE_RESIGNATION`: MRNO, RESIGNATION_DATE
- **FK** `FK_EMPLOYEE_RESIGNATION_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMPLOYEE_RESIGNATION_2`: (RESIGNATION_REASON_ID) -> HRD.RESIGNATION_REASONS(RESIGNATION_REASON_ID)
- **CHECK** `CHK_APPROVED`: APPROVED IN ('A','W','C','R')
- **Triggers**: `EMPLOYEE_RESIGNATION_DEL` (after delete), `EMPLOYEE_RESIGNATION_INS` (before insert), `EMPLOYEE_RESIGNATION_UPD` (before update), `EMP_BOND_PENDING_Q_DEL` (before update or delete), `SUBSTITUTE_QUEUE_INSERT` (after insert), `SUBSTITUTE_Q_DEL` (after update or delete)

## HRD.EMPLOYEE_SALARY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| ALLOWANCE_TYPE_ID | VARCHAR2(7) | N |  |
| AMOUNT | NUMBER(12,2) | Y |  |
| FROM_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |

- **PK** `PK_EMPLOYEE_SALARY`: MRNO, ALLOWANCE_TYPE_ID
- **FK** `FK_EMPLOYEE_SALARY`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `EMPLOYEE_SALARY_DEL` (after delete), `EMPLOYEE_SALARY_INS` (before insert), `EMPLOYEE_SALARY_UPD` (before update)

## HRD.EMPLOYEE_SALARY_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ALLOWANCE_TYPE_ID | VARCHAR2(7) | Y |  |
| AMOUNT | NUMBER(12,2) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

- **Triggers**: `EMPLOYEE_SALARY_HISTORY_DEL` (after delete), `EMPLOYEE_SALARY_HISTORY_INS` (before insert), `EMPLOYEE_SALARY_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_SECTION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| DEPT_START_DATE | DATE | Y |  |

- **PK** `PK_SECTION_HISTORY`: MRNO, START_DATE
- **FK** `FK_SECTION_HISTORY_1`: (MRNO, DEPT_START_DATE) -> HRD.EMPLOYEE_DEPARTMENT_HISTORY(MRNO, START_DATE) [disabled]
- **FK** `FK_SECTION_HISTORY_2`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_SECTION_HISTORY_3`: (DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.DEPARTMENT_SECTION(DEPARTMENT_ID, SECTION_ID) [disabled]
- **Triggers**: `TR_EMPLOYEE_SECTION_RIGHTS` (before insert), `TR_EMPLOYEE_SECTION_RIGHTS_DEL` (after delete), `TR_EMPLOYEE_SECTION_RIGHTS_UPD` (after update)

## HRD.EMPLOYEE_STUDY_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| INSTITUTION_ID | NUMBER(4) | N |  |
| ROLL_NO | VARCHAR2(30) | Y |  |
| STUDY_SESSION | VARCHAR2(30) | Y |  |
| STUDY_PROGRAM | VARCHAR2(120) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| STUDY_TYPE_ID | VARCHAR2(3) | N |  |
| STUDY_PROGRAM_ID | VARCHAR2(10) | N |  |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains ATTACHMENT DESCRIPTION |
| OSV_DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id for OSV from LOB.DOCUMENT_STORE table |
| OSV_ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY  OSV MRNO |
| OSV_DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains OSV ATTACHMENT DESCRIPTION |
| OSV_STATUS | CHAR(2) | N |  |
| YEAR | VARCHAR2(4) | Y |  |
| CURRENT_DEGREE | CHAR(1) | Y |  |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENT |
| EMP_JOINING_DATE_OSV | DATE | Y | This column contains EMPLOYMENT for OSV |
| OSV_SENT_DATE | DATE | Y | THIS COULUMN CONTAINS  OSV ALERT SENT DATE |
| OSV_SLIP_RECEIVE_DATE | DATE | Y | THIS COULUMN CONTAINS  OSV SLIP RECIEVED DATE |
| IS_OSV_REQUIRED | CHAR(1) default 'Y' | Y | this coulumn contains  OSV CHECK Y OR N |

- **PK** `PK_EMPLOYEE_STUDY_HISTORY`: MRNO, INSTITUTION_ID, STUDY_TYPE_ID, STUDY_PROGRAM_ID, OSV_STATUS
- **FK** `FK_EMP_STUDY_HISTORY_1`: (INSTITUTION_ID) -> HRD.STUDY_INSTITUTIONS(INSTITUTE_ID) [disabled]
- **FK** `FK_EMP_STUDY_HISTORY_2`: (STUDY_TYPE_ID) -> HRD.STUDY_TYPE(TYPE_ID) [disabled]
- **FK** `FK_EMP_STUDY_HISTORY_3`: (STUDY_PROGRAM_ID) -> HRD.STUDY_PROGRAMS(PROGRAM_ID) [disabled]
- **Triggers**: `EMPLOYEE_STUDY_HISTORY_DEL` (after delete), `EMPLOYEE_STUDY_HISTORY_INS` (before insert), `EMPLOYEE_STUDY_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_STUDY_HISTORY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| INSTITUTION_ID | NUMBER(4) | N |  |
| STUDY_TYPE_ID | VARCHAR2(3) | N |  |
| STUDY_PROGRAM_ID | VARCHAR2(10) | N |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| OSV_STATUS | CHAR(2) | N |  |
| OSV_SLIP_RECEIVE_DATE | DATE | Y |  |
| OSV_SENT_DATE | DATE | N |  |
| OSV_STATUS_DET | CHAR(2) | Y |  |

- **PK** `PK_SUDY_HIST1`: MRNO, OSV_SENT_DATE, OSV_STATUS, STUDY_TYPE_ID, STUDY_PROGRAM_ID, INSTITUTION_ID

## HRD.EMPLOYEE_TRANSFER_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| FROM_DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| TO_DEPARTMENT_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_EMPLOYEE_TRANSFER_HISTORY`: MRNO, SERIAL_NO
- **Triggers**: `EMPLOYEE_TRANSFER_HISTORY_DEL` (after delete), `EMPLOYEE_TRANSFER_HISTORY_INS` (before insert), `EMPLOYEE_TRANSFER_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_TRAVEL_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| TRAVEL_ID | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| TRAVEL_TYPE | VARCHAR2(1) | Y |  |
| DATE_FROM | DATE | Y |  |
| DATE_TO | DATE | Y |  |
| COUNTRY_ID | VARCHAR2(2) | Y |  |
| P_ID | VARCHAR2(1) | Y |  |
| D_ID | VARCHAR2(3) | Y |  |
| T_ID | VARCHAR2(4) | Y |  |

- **PK** `PK_EMPLOYEE_TRAVEL_HISTORY`: TRAVEL_ID, MRNO
- **Triggers**: `EMPLOYEE_TRAVEL_HISTORY_DEL` (after delete), `EMPLOYEE_TRAVEL_HISTORY_INS` (before insert), `EMPLOYEE_TRAVEL_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_TYPE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| REMARKS | VARCHAR2(3000) | Y |  |

- **PK** `PK_EMPLOYEE_TYPE_HISTORY`: MRNO, START_DATE
- **FK** `FK_EMPLOYEE_TYPE_HISTORY_1`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_EMPLOYEE_TYPE_HISTORY_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **Triggers**: `EMPLOYEE_TYPE_HISTORY_DEL` (after delete), `EMPLOYEE_TYPE_HISTORY_INS` (before insert), `EMPLOYEE_TYPE_HISTORY_UPD` (before update)

## HRD.EMPLOYEE_VACANCY_SOURCE

| Column | Type | Null | Comment |
|---|---|---|---|
| VACANCY_SOURCE_ID | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_EMPLOYEE_VACANCY_SOURCE`: VACANCY_SOURCE_ID
- **Triggers**: `EMPLOYEE_VACANCY_SOURCE_DEL` (after delete), `EMPLOYEE_VACANCY_SOURCE_INS` (before insert), `EMPLOYEE_VACANCY_SOURCE_UPD` (before update)

## HRD.EMPLOYEE_WORKAREA_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| WORK_AREA_ID | VARCHAR2(5) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_WORKAREA_HISTORY`: MRNO, START_DATE
- **FK** `FK_WORKAREA_HISTORY_1`: (MRNO) -> HRD.INFORMATION(MRNO)

## HRD.EMPLOYEE_WORK_EXPERIENCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| SR_NO | NUMBER | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| EMP_JOINING_DATE | DATE | Y |  |
| OSV_STATUS | CHAR(2) | Y | This column contains Original source verification status |
| OSV_ATTACHED_BY | VARCHAR2(14) | Y | This column contains OSV_ATTACHED_BY |
| OSV_DOCUMENT_ID | VARCHAR2(100) | Y | This column contains OSV_DOCUMENT_ID |
| OSV_SLIP_RECEIVE_DATE | DATE | Y | This column contains OSV RECEIVE DATE |


## HRD.EMPLOYEE_WORK_HIST_DET

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| OSV_STATUS | CHAR(2) | Y |  |
| OSV_SLIP_RECEIVE_DATE | DATE | Y |  |
| OSV_SENT_DATE | DATE | Y |  |
| OSV_STATUS_DET | CHAR(2) | N |  |
| EXPIRY_DATE | DATE | Y |  |
| SR_NO | NUMBER | N |  |

- **PK** `PK_EMP_EXPER`: MRNO, SR_NO, OSV_STATUS_DET
- **Triggers**: `EMPLOYEE_WORK_HIST_DET_DEL` (after delete), `EMPLOYEE_WORK_HIST_DET_INS` (before insert), `EMPLOYEE_WORK_HIST_DET_UPD` (before update)

## HRD.EMPLOYMENT_CONTRACT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | 14 digit Employee Code from HRD.INFORMATION |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y | Employee Type from DEFINITIONS.PATIENT_TYPE |
| DESIGNATION_ID | VARCHAR2(6) | Y | Employee Designation from DEFINITIONS.DESIGNATION |
| GRADE_ID | VARCHAR2(6) | Y | Employee Grade Id from DEFINITIONS.GRADES |
| INITIAL_GROSS | NUMBER(20,3) | Y | Salary at the time of Joining (Format: 99,999,999,999) |
| CONTRACT_START_DATE | DATE | Y | Employment Contract start date (Format: Date) |
| CONTRACT_END_DATE | DATE | Y | Employment Contract end date (Format: Date) |
| PROBATION_PERIOD | NUMBER | Y | Probation period (Format: Number of months) |
| NOTICE_PERIOD | NUMBER | Y | Notice period (Format: Number of days) |
| ACCEPTANCE_DAYS | NUMBER | Y | Employeement offer letter acceptance date in (days) |
| SALARY_RAISE_AFTER_PROBATION | NUMBER(20,3) | Y | After Probation salary (Format: 99,999,999,999) |
| MEDICALLY_FIT | CHAR(1) default 'P' | Y | 'Y' for Medically fit, 'N' for Medically un-fit, 'P' for Medical In-Process |
| ACTIVE | CHAR(1) default 'Y' | Y | 'Y' for Actiev, 'N' for In-Active |
| JOINING_DATE | DATE | Y | Joining date of employee (in Date format) |
| IN_QUEUE_HR_SECTION_ID | VARCHAR2(7) | Y | Stores HR department '7 'digits section ID |
| ORIENTATION_DATE | DATE | Y |  |
| MEDICALLY_UNFIT_REMARKS | VARCHAR2(2000) | Y |  |
| INACTIVE_REMARKS | VARCHAR2(2000) | Y |  |
| IS_ORIENTATION_DONE | CHAR(1) default 'N' | Y |  |
| ACTUAL_ORIENTATION_DATE | DATE | Y | This column contains orignal orientation planed date |
| IS_JOINED | CHAR(1) | Y | THIS COLUMN CONTAINS VALUE EITHER EMPLOYEE IS JOINED OR NO |
| CONTRACT_YEAR | VARCHAR2(4) | Y | THIS COLUMN CONTAINS CONTRACT YEAR |
| IS_EXPENSE_SUBMITTED | CHAR(1) default 'N' | Y |  |
| FARWARD_TO_EHC | CHAR(1) default 'N' | Y | 'Y' for HR FORWARD TO EHC, 'N' HR NO FORWARD TO EHC |
| EHC_BACK_TO_HR | CHAR(1) default 'N' | Y | 'Y' EHC for BACK TO HR, 'N' EHC NO BACK TO HR |
| HR_COMPLETE | CHAR(1) default 'N' | Y | 'Y' COMPLETE , 'N' NOT COMPLETE |
| MEDICAL_REMAKRS | VARCHAR2(4000) | Y |  |
| MEDICAL_RECORD_ACKNOWLEDGE | CHAR(1) default 'N' | Y | 'Y' ACKNOWLEDGE , 'N' NOT ACKNOWLEDGE |
| COLOR_VISION_TEST_RESULT | VARCHAR2(10) default 'P' | Y |  |
| AUDIOMETRY_TEST_RESULT | VARCHAR2(10) default 'P' | Y |  |
| VISION_CHK_RESULT | VARCHAR2(10) default 'P' | Y |  |
| EXTERNAL_REPORT_REVIEWED | CHAR(1) default 'N' | Y | 'Y' REQUIRED , 'N' NOT REQUIRED |
| MEDICAL_RECORD_ACKNOWLEDGE_BY | VARCHAR2(14) | Y |  |
| MEDICAL_RECORD_ACKNOWLEDGE_DATE | DATE | Y |  |
| EHC_ACKNOWLEDGE_BY | VARCHAR2(14) | Y |  |
| EHC_ACKNOWLEDGE_DATE | DATE | Y |  |
| HR_ACKNOWLEDGE_BY | VARCHAR2(14) | Y |  |
| HR_ACKNOWLEDGE_DATE | DATE | Y |  |
| EMP_CONTRACT_ENTRY_DATE | DATE | Y |  |
| MEDICAL_DATE | CHAR(1) default 'N' | Y | 'Y' REQUIRED , 'N' NOT REQUIRED |
| HEARING_TEST | VARCHAR2(10) | Y |  |

- **PK** `PK_EMPLOYMENT_CONTRACT_1`: MRNO
- **FK** `FK_EMPLOYMENT_CONTRACT_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_EMPLOYMENT_CONTRACT_2`: (GRADE_ID) -> DEFINITIONS.GRADES(GRADE_ID) [disabled]
- **Triggers**: `EMPLOYMENT_CONTRACT_DEL` (after delete), `EMPLOYMENT_CONTRACT_HR_PT` (after update of ehc_back_to_hr, hr_complete), `EMPLOYMENT_CONTRACT_INS` (before insert), `EMPLOYMENT_CONTRACT_MR_PT` (after update of external_report_reviewed, medical_record_acknowledge), `EMPLOYMENT_CONTRACT_PT` (after update of farward_to_ehc, ehc_back_to_hr), `EMPLOYMENT_CONTRACT_UPD` (before update), `TRG_UPD_ACTUAL_ORIEN_DATE` (before update )

## HRD.EMPLOYMENT_HISTORY_BENEFITS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(2) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| BENEFIT_ID | NUMBER(3) | Y |  |
| VALUE | NUMBER(9) | Y |  |

- **PK** `PK_EMPLOYMENT_HISTORY_BENEFITS`: SR_NO, MRNO
- **Triggers**: `EMPLOYMENT_HISTORY_BENEFITS_DEL` (after delete), `EMPLOYMENT_HISTORY_BENEFITS_INS` (before insert), `EMPLOYMENT_HISTORY_BENEFITS_UPD` (before update), `EMPLOYMENT_HIST_BENEFITS_DEL` (after delete), `EMPLOYMENT_HIST_BENEFITS_INS` (before insert), `EMPLOYMENT_HIST_BENEFITS_UPD` (before update)

## HRD.EMP_ADDITIONAL_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ORDER_NO | VARCHAR2(50) | Y |  |
| ORDER_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| EMP_JOINING_DATE | DATE | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |

- **PK** `PK_ADD_DEPT_01`: MRNO, START_DATE, DEPARTMENT_ID
- **FK** `FK_ADD_DEPT_01`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_ADD_MRNO_01`: (MRNO) -> HRD.INFORMATION(MRNO)
- **Triggers**: `EMP_ADDITIONAL_DEPT_DEL` (after delete), `EMP_ADDITIONAL_DEPT_INS` (before insert), `EMP_ADDITIONAL_DEPT_UPD` (before update)

## HRD.EMP_CARD_PRINT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SESSION_ID | NUMBER(20) | N |  |

_No standard audit columns._

- **PK** `PK_EMP_CARD_PRINT`: MRNO, SESSION_ID

## HRD.EMP_CARD_SWIPE_ADJUSTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ORIGIONAL_TIME_IN | DATE | Y |  |
| ORIGIONAL_TIME_OUT | DATE | Y |  |
| ADJUSTED_TIME_IN | DATE | Y |  |
| ADJUSTED_TIME_OUT | DATE | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| STATUS | CHAR(1) default 'D' | Y | 'D'DRAFT , 'F','FORWARD' ,'C','COMPLETE' |
| REAMRKS | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| ENTER_BY | VARCHAR2(14) | Y |  |
| DUTY_DATE | DATE | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| REJECTION_REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `EMP_CARD_SWIPE_ADJUSTMENT_PK`: SR_NO, MRNO
- **Triggers**: `EMP_CARD_SWIPE_ADJUSTMENT_DEL` (after delete), `EMP_CARD_SWIPE_ADJUSTMENT_INS` (before insert), `EMP_CARD_SWIPE_ADJUSTMENT_UPD` (before update)

## HRD.EMP_CARD_SWIPE_ADJUSTMENT_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | N |  |
| EMP_ADJUST_SR_NO | NUMBER | N |  |
| FORWARD_TO | VARCHAR2(14) | Y |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y |  |
| AUTORITY_APPROVE_DATE | DATE | Y |  |
| LEAVE_HIERARCHY_AUTH_ID | NUMBER | Y |  |
| HR_REMARKS | VARCHAR2(4000) | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| DUTY_DATE | DATE | Y |  |
| ORIGIONAL_TIME_IN | DATE | Y |  |
| ORIGIONAL_TIME_OUT | DATE | Y |  |
| ADJUSTED_TIME_IN | DATE | Y |  |
| ADJUSTED_TIME_OUT | DATE | Y |  |
| STATUS | CHAR(1) | Y | 'R','RECOMMEND','A','APPROVED' |
| REJECTTION_REMARKS | VARCHAR2(4000) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |

- **PK** `EMP_CARD_SWIPE_ADJUSTMENT_Q_PK`: APPLICANT_MRNO, EMP_ADJUST_SR_NO
- **Triggers**: `EMP_CARD_ADJ_Q_DEL` (after delete), `EMP_CARD_ADJ_Q_INS` (before insert), `EMP_CARD_ADJ_Q_UPD` (before update), `EMP_CARD_SWIPE_ADJ_PT_Q_DEL` (after delete), `EMP_CARD_SWIPE_ADJ_PT_Q_INS` (after insert), `EMP_CARD_SWIPE_ADJ_PT_Q_UPD` (after update), `EMP_CARD_SWIPE_Q_HIS_UPDATE` (after update or delete)

## HRD.EMP_CARD_SWIPE_ADJ_Q_HIS

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | Y |  |
| EMP_ADJUST_SR_NO | NUMBER | Y |  |
| FORWARD_TO | VARCHAR2(14) | Y |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y |  |
| AUTORITY_APPROVE_DATE | DATE | Y |  |
| LEAVE_HIERARCHY_AUTH_ID | NUMBER | Y |  |
| HR_REMARKS | VARCHAR2(4000) | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| DUTY_DATE | DATE | Y |  |
| ORIGIONAL_TIME_IN | DATE | Y |  |
| ORIGIONAL_TIME_OUT | DATE | Y |  |
| ADJUSTED_TIME_IN | DATE | Y |  |
| ADJUSTED_TIME_OUT | DATE | Y |  |
| STATUS | CHAR(1) | Y |  |
| REJECTTION_REMARKS | VARCHAR2(4000) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |

_No standard audit columns._


## HRD.EMP_CLEARANCE_CERTIFICATE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| LAST_WORKING_DAY | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| CLEARANCE_STATUS | VARCHAR2(3) default 018 | Y | 018 is pending from orderentry |
| SUBSTITUTE_ADMIN | VARCHAR2(14) | Y |  |
| SUBSTITUTE_CLINICAL | VARCHAR2(14) | Y |  |
| CLEARANCE_ENTRY_DATE | DATE | Y |  |
| HR_REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CLEARANCE_CER_ID`: CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID
- **Triggers**: `EMP_CLEARANCE_CERTIFICATE_DEL` (after delete), `EMP_CLEARANCE_CERTIFICATE_INS` (before insert), `EMP_CLEARANCE_CERTIFICATE_UPD` (before update)

## HRD.EMP_CLEARANCE_CERTIFICATE_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| LAST_WORKING_DAY | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CLEARANCE_STATUS | VARCHAR2(3) | Y |  |
| SUBSTITUTE_ADMIN | VARCHAR2(14) | Y |  |
| SUBSTITUTE_CLINICAL | VARCHAR2(14) | Y |  |
| STATUS | CHAR(3) | Y |  |


## HRD.EMP_CLEARANCE_DETAIL

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
| SETUP_ID | NUMBER | N |  |
| IS_FUNCTION | CHAR(1) default 'N' | Y |  |

- **PK** `EMP_CLEARANCE_DETAIL_PK`: SR_NO, SETUP_ID
- **Triggers**: `EMP_CLEARANCE_DETAIL_DEL` (after delete), `EMP_CLEARANCE_DETAIL_INS` (before insert), `EMP_CLEARANCE_DETAIL_UPD` (before update)

## HRD.EMP_CLEARANCE_DETAIL_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| SETUP_ID | NUMBER | N |  |
| EVENT_DETIAL_DESC | VARCHAR2(2000) | Y |  |
| TABLE_SOURCE | VARCHAR2(1000) | Y |  |
| COLUMN_IDENTIFIER_1 | VARCHAR2(500) | Y |  |
| COLUMN_IDENTIFIER_2 | VARCHAR2(500) | Y |  |
| COLUMN_IDENTIFIER_3 | VARCHAR2(500) | Y |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| COUNT | NUMBER | Y |  |
| NOT_APPLICABLE | CHAR(1) | Y |  |
| STATUS | VARCHAR2(2) default 'H' | Y | 'H' MEANS HR QUEUE, 'S' MEANS FINANCE BACK TO HR , 'F' MEANS FORWARDED TO FINACNE,'C' MEANS COMPLETE, 'SF', MEANS SEND BACK 'SEND BACK TO FINANCE' |
| IS_FORWARD_FINANCE | CHAR(1) default 'N' | Y |  |
| IS_BACK_HR | CHAR(1) default 'N' | Y |  |
| FORWARD_BY_FINANCE | VARCHAR2(14) | Y |  |
| FORWARD_FINANCE_DATE | DATE | Y |  |
| FORWARD_BACK_HR | VARCHAR2(14) | Y |  |
| FORWARD_BACK_HR_DATE | DATE | Y |  |
| PROCESS_ID | VARCHAR2(12) | N |  |
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| LAST_WORKING_DAY | DATE | Y |  |
| MANUAL_VALUE | NUMBER | Y |  |

- **PK** `EMP_CLEARANCE_DETAIL_EVENT_PK`: SETUP_ID, MRNO, PROCESS_ID, CLEARANCE_CERTIFICATE_ID
- **Triggers**: `EMP_CLEARANCE_BACK_HR_Q` (after update), `EMP_CLEARANCE_DETAIL_EVENT_DEL` (after delete), `EMP_CLEARANCE_DETAIL_EVENT_INS` (before insert), `EMP_CLEARANCE_DETAIL_EVENT_UPD` (before update), `TRG_EMP_CLEARANCE_Q_INS` (after update)

## HRD.EMP_CLEARANCE_EXCEPTION

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| EXCEPTION_ERROR | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |

- **Triggers**: `EMP_CLEARANCE_EXCEPTION_DEL` (after delete), `EMP_CLEARANCE_EXCEPTION_INS` (before insert), `EMP_CLEARANCE_EXCEPTION_UPD` (before update)

## HRD.EMP_CLEARANCE_PENDING_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER | N |  |
| EVENT_DETIAL_DESC | VARCHAR2(2000) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| COUNT | NUMBER | Y |  |
| STATUS | VARCHAR2(2) | Y |  |
| IS_FORWARD_FINANCE | CHAR(1) | Y |  |
| IS_BACK_HR | CHAR(1) | Y |  |
| FORWARD_BY_FINANCE | VARCHAR2(14) | Y |  |
| FORWARD_FINANCE_DATE | DATE | Y |  |
| FORWARD_BACK_HR | VARCHAR2(14) | Y |  |
| FORWARD_BACK_HR_DATE | DATE | Y |  |
| PROCESS_ID | VARCHAR2(12) | N |  |
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| LAST_WORKING_DAY | DATE | Y |  |
| MANUAL_COUNT | NUMBER | Y |  |

- **PK** `EMP_CLEARANCE_PENDING_Q_PK`: SETUP_ID, MRNO, PROCESS_ID, CLEARANCE_CERTIFICATE_ID
- **Triggers**: `EMP_CLEARANCE_FINANCE_Q` (after insert), `EMP_CLEARANCE_FINANCE_Q_DEL` (after delete), `EMP_CLEARANCE_PENDING_Q_DEL` (after delete), `EMP_CLEARANCE_PENDING_Q_INS` (before insert), `EMP_CLEARANCE_PENDING_Q_UPD` (before update)

## HRD.EMP_CLEARANCE_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER(5) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| IN_QUEUE | VARCHAR2(14) | N |  |
| FORWARD_DEPARTENT_ID | VARCHAR2(7) | N |  |
| FORWARD_SECTION_ID | VARCHAR2(7) | Y |  |
| ROLE | VARCHAR2(3) | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| OLD_MRNO | VARCHAR2(14) | Y |  |
| IN_QUEUE_DATE | DATE | Y |  |
| IN_QUEUE_ACTING_FOR | VARCHAR2(14) | Y |  |
| IS_DEPARTMENT_HEAD | CHAR(1) default 'N' | Y |  |

_No standard audit columns._

- **PK** `PK_EMP_CLEARANCE_QUEUE`: QUEUE_ID, CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID
- **FK** `FK_EMP_CLEARANCE_QUEUE`: (CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID) -> HRD.EMP_CLEARANCE_CERTIFICATE(CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID) [disabled]
- **Triggers**: `EMP_CL_QUEUE_AFTER_INS` (before insert)

## HRD.EMP_CLEARANCE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER | N |  |
| EVENT_DESCRIPTION | VARCHAR2(1000) | Y |  |
| MODULE_ID | VARCHAR2(10) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `EMP_CLEARANCE_SETUP`: SETUP_ID
- **Triggers**: `EMP_CLEARANCE_SETUP_DEL` (after delete), `EMP_CLEARANCE_SETUP_INS` (before insert), `EMP_CLEARANCE_SETUP_UPD` (before update)

## HRD.EMP_CL_CHECKLIST

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| CHECKLIST_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| CL_PARAMETER_VALUE_ID | NUMBER(3) | Y |  |
| CL_PARAMETER_TYPE_ID | NUMBER(3) | Y |  |
| PARAM_VAL | VARCHAR2(4000) | Y |  |

- **PK** `PK_PARM_VAL`: CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID, CHECKLIST_ID, PARAMETER_ID
- **FK** `FK_PARM_VAL_1`: (CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID) -> HRD.EMP_CLEARANCE_CERTIFICATE(CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID, LOCATION_ID)
- **Triggers**: `EMP_CL_CHECKLIST_DEL` (after delete), `EMP_CL_CHECKLIST_INS` (before insert), `EMP_CL_CHECKLIST_UPD` (before update)

## HRD.EMP_CL_DEPT_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| CLEARANCE_BY | VARCHAR2(14) | Y |  |
| CLEARANCE_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| SECTION_WISE_STATUS | VARCHAR2(3) default '018' | N |  |
| FORWARD | CHAR(1) default 'N' | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |
| SECTION_EVENT | VARCHAR2(1000) | Y |  |
| SERIAL_NO | NUMBER(5) | N |  |
| EMP_ROLE | VARCHAR2(3) | Y |  |
| SEND_BACK | CHAR(1) default 'N' | Y | 'Y' FOR SEND BACK... 'N' IS DEFAULT |
| SIGNED_BY | VARCHAR2(14) | Y | signed by mrno |
| OLD_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_EMP_CL_DEPT_SECTION`: SERIAL_NO, LOCATION_ID, CLEARANCE_CERTIFICATE_ID, ORGANIZATION_ID
- **Triggers**: `EMP_CL_DEPT_SECTION_DEL` (after delete), `EMP_CL_DEPT_SECTION_INS` (before insert), `EMP_CL_DEPT_SECTION_UPD` (before update)

## HRD.EMP_CL_DEPT_SECTION_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_CERTIFICATE_ID | NUMBER(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| CLEARANCE_BY | VARCHAR2(14) | Y |  |
| CLEARANCE_DATE | DATE | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| SECTION_WISE_STATUS | VARCHAR2(3) | Y |  |
| FORWARD | CHAR(1) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |
| SECTION_EVENT | VARCHAR2(1000) | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| STATUS | CHAR(3) | Y |  |


## HRD.EMP_CONTRACT_PENDING_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DEPT_ID | VARCHAR2(7) | Y |  |
| ALERT_ID | VARCHAR2(5) | Y |  |
| CC_EMAIL | VARCHAR2(1000) | Y |  |
| BCC_EMAIL | VARCHAR2(1000) | Y |  |
| RECIPIENT_EMAIL | VARCHAR2(1000) | Y |  |
| DESIG_ID | VARCHAR2(7) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MANGER_CODE | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(500) | Y |  |
| DEPT | VARCHAR2(500) | Y |  |
| DESIG | VARCHAR2(500) | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| HR_ACKNOWLEDGE | CHAR(1) default 'N' | Y |  |
| HR_ACKNOWLEDGE_DATE | DATE | Y |  |
| EMPLOYEE_ANNIVERSARY_DATE | DATE | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| DISTRIBUTION_DATE | DATE | Y |  |
| IS_DISTRIBUTED | CHAR(1) default 'N' | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |

- **PK** `EMP_CONTRACT_PENDING_Q_PK`: MRNO
- **Triggers**: `APPRAISAL_PENDING_Q_DEL` (after delete), `APPRAISAL_PENDING_Q_INS` (after insert), `EMP_CONTRACT_PENDING` (before insert), `EMP_CONTRACT_PENDING_Q_DEL` (after delete), `EMP_CONTRACT_PENDING_Q_DELETE_HISTORY` (after delete), `EMP_CONTRACT_PENDING_Q_INS` (before insert), `EMP_CONTRACT_PENDING_Q_UPD` (before update)

## HRD.EMP_CONTRACT_PENDING_Q_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DEPT_ID | VARCHAR2(7) | Y |  |
| ALERT_ID | VARCHAR2(5) | Y |  |
| CC_EMAIL | VARCHAR2(1000) | Y |  |
| BCC_EMAIL | VARCHAR2(1000) | Y |  |
| RECIPIENT_EMAIL | VARCHAR2(1000) | Y |  |
| DESIG_ID | VARCHAR2(7) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MANGER_CODE | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(500) | Y |  |
| DEPT | VARCHAR2(500) | Y |  |
| DESIG | VARCHAR2(500) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| HR_ACKNOWLEDGE | CHAR(1) | Y |  |
| HR_ACKNOWLEDGE_DATE | DATE | Y |  |
| EMPLOYEE_ANNIVERSARY_DATE | DATE | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| DISTRIBUTION_DATE | DATE | Y |  |
| IS_DISTRIBUTED | CHAR(1) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |

_No standard audit columns._


## HRD.EMP_INCENTIVE_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PROBATION_START_DATE | DATE | Y |  |
| PROBATION_END_DATE | DATE | Y |  |
| STATUS | CHAR(1) | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| VERIFY_BY | VARCHAR2(14) | Y |  |
| VERIFY_DATE | DATE | Y |  |
| HR_VERIFY_BY | VARCHAR2(14) | Y |  |
| HR_VERIFY_DATE | DATE | Y |  |
| FORWARD_HR | CHAR(1) | Y |  |
| INCENTIVE_START_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| REJECT_BY | VARCHAR2(14) | Y |  |
| REJECT_DATE | DATE | Y |  |
| ALLOWANCE_STATUS | CHAR(1) | Y |  |
| ALLOWANCES_ID | NUMBER | N |  |

- **PK** `EMP_INCENTIVE_QUEUE`: MRNO, ALLOWANCES_ID
- **Triggers**: `EMP_INCENTIVE_QUEUE_DEL` (after delete), `EMP_INCENTIVE_QUEUE_DEL_HIS` (after delete), `EMP_INCENTIVE_QUEUE_INS` (before insert), `EMP_INCENTIVE_QUEUE_UPD` (before update), `EMP_INCENTIVE_QUEUE_UPD_HIS` (after update), `PT_INCENTIVE_Q_HOD` (after insert), `PT_SP_HR_Q_DELETE` (after update of status), `SP_INCENTIVE_HR_PT_Q` (after update of forward_hr, status)

## HRD.EMP_INCENTIVE_QUEUE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PROBATION_START_DATE | DATE | Y |  |
| PROBATION_END_DATE | DATE | Y |  |
| STATUS | CHAR(1) | Y |  |
| Q_ENTRY_DATE | DATE | Y |  |
| VERIFY_BY | VARCHAR2(14) | Y |  |
| VERIFY_DATE | DATE | Y |  |
| HR_VERIFY_BY | VARCHAR2(14) | Y |  |
| HR_VERIFY_DATE | DATE | Y |  |
| FORWARD_HR | CHAR(1) | Y |  |
| INCENTIVE_START_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| REJECT_BY | VARCHAR2(14) | Y |  |
| REJECT_DATE | DATE | Y |  |
| ALLOWANCE_STATUS | CHAR(1) | Y |  |
| TRN_STATUS | VARCHAR2(3) | Y |  |
| ALLOWANCES_ID | NUMBER | Y |  |

_No standard audit columns._


## HRD.EMP_ON_SITE_UNDERSUP_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_UNDERSUPERVISION_HIST_ID | NUMBER(20) | N |  |
| SUPERVISOR_MRNO | VARCHAR2(14) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| IS_UNDERSUPERVISION | CHAR(1) | Y |  |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | N | THIS COLUMN CONATINS THE VALUE FROM CPT GROUP TYPE |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N | THIS COLUMN CONATINS THE VALUE FROM CPT GROUP TYPE |
| PATIENT_TYPE | CHAR(1) | Y |  |

- **PK** `PK_EMP_ON_SITE_UNDERSUP_CPT`: CPT_ID, EMP_UNDERSUPERVISION_HIST_ID, CPT_GROUP_TYPE_ID, CPT_RESTRICTION_TYPE_ID
- **Triggers**: `EMP_ON_SITE_UNDERSUP_CPT_DEL` (after delete), `EMP_ON_SITE_UNDERSUP_CPT_INS` (before insert), `EMP_ON_SITE_UNDERSUP_CPT_UPD` (before update)

## HRD.EMP_PENDING_TASK_CLEARANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| ASSIGNMENT_ID | NUMBER(3) | N |  |
| TASK_DESCRIPTION | VARCHAR2(255) | Y |  |
| TASK_COUNT | NUMBER | Y |  |
| PATH | VARCHAR2(500) | Y |  |
| PROJECT | VARCHAR2(255) | Y |  |
| ACTING_FOR_MRNO | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| LAST_EXE_TIME | DATE | Y |  |
| CLEARED_BY_MRNO | VARCHAR2(14) | Y |  |
| IGNORE_YN | CHAR(1) default 'N' | Y |  |
| HR_CLEARED | CHAR(1) default 'N' | Y |  |
| CLEARANCE_ID | NUMBER(10) | Y |  |
| CLEARED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_EMP_PENDING_TASK_CLEARANCE`: MRNO, ASSIGNMENT_ID
- **Triggers**: `EMP_PENDING_TASK_CLEARANCE_DEL` (after delete), `EMP_PENDING_TASK_CLEARANCE_INS` (before insert), `EMP_PENDING_TASK_CLEARANCE_UPD` (before update)

## HRD.EMP_QR

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_QR_ID | NUMBER | N |  |
| QR_CODE | BLOB | Y |  |
| QR_DATA | CLOB | Y |  |
| QR_LINK | VARCHAR2(4000) | Y |  |
| TOKEN | VARCHAR2(4000) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(4000) | Y |  |

- **PK** `PK_EMP_QR`: EMP_QR_ID
- **Triggers**: `EMP_QR_DEL` (after delete), `EMP_QR_INS` (before insert), `EMP_QR_UPD` (before update)

## HRD.EMP_QR_SOCIAL_MEDIA

| Column | Type | Null | Comment |
|---|---|---|---|
| QR_SOCIAL_ID | NUMBER | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| PLATFORM | VARCHAR2(100) | Y |  |
| PROFILE_LINK | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_QR_EMP_SOCIAL_MEDIA`: QR_SOCIAL_ID
- **Triggers**: `EMP_QR_SOCIAL_MEDIA_DEL` (after delete), `EMP_QR_SOCIAL_MEDIA_INS` (before insert), `EMP_QR_SOCIAL_MEDIA_UPD` (before update)

## HRD.EMP_RECORD_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_MRNO | VARCHAR2(14) | Y |  |
| DOC_CATEGORY_ID | NUMBER | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| CONTEXT_ID | VARCHAR2(500) | Y |  |

_No standard audit columns._


## HRD.EMP_SUBSTITUTES

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_MRNO | VARCHAR2(14) | N | Employee Code which can be marked Substitute |
| SUBSTITUTE_OF | VARCHAR2(14) | N | Employee Code for which EMP_MRNO can be marked as substitute |
| SUBSTITUTE_TYPE | CHAR(1) | N | C=Clinical, A=Administrative |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_EMP_SUBSTITUTES`: EMP_MRNO, SUBSTITUTE_OF, SUBSTITUTE_TYPE
- **FK** `FK_EMP_SUBSTITUTES_1`: (EMP_MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `FK_EMP_SUBSTITUTES_2`: (SUBSTITUTE_OF) -> HRD.INFORMATION(MRNO) [disabled]
- **CHECK** `CHK_EMP_SUBSTITUTES_1`: SUBSTITUTE_TYPE IN ('C', 'A')
- **Triggers**: `EMP_SUBSTITUTES_DEL` (after delete), `EMP_SUBSTITUTES_INS` (before insert), `EMP_SUBSTITUTES_UPD` (before update)

## HRD.EMP_SUBSTITUTE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SUBSTITUTE_MRNO | VARCHAR2(14) | N |  |
| SUBSTITUTE_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `EMP_SUBSTITUTE_SETUP_PK`: SR_NO, MRNO, SUBSTITUTE_MRNO
- **Triggers**: `EMP_SUBSTITUTE_SETUP_DEL` (after delete), `EMP_SUBSTITUTE_SETUP_INS` (before insert), `EMP_SUBSTITUTE_SETUP_UPD` (before update)

## HRD.EMP_TEMP_CARD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| ACTUAL_RFID_CODE | VARCHAR2(10) | Y |  |
| TEMP_RFID_CODE | VARCHAR2(10) | Y |  |
| ISSUE_DAYS | NUMBER | Y |  |
| RFID_STATUS | CHAR(1) | Y | 'R' FOR RECEIVED TEMP CARD AND 'A' ASSIGNED TEMP CARD |
| ENTRY_DATE | DATE | Y |  |

- **PK** `EMP_TEMP_CARD_PK`: MRNO
- **UK** `EMP_TEMP_CARD_UK`: TEMP_RFID_CODE
- **FK** `EMP_TEMP_CARD_FK`: (MRNO) -> HRD.INFORMATION(MRNO)
- **FK** `EMP_TEMP_CARD_FK_2`: (TEMP_RFID_CODE) -> RFID.TEMP_CARD_SETUP(CARD_NO)
- **Triggers**: `EMP_TEMP_CARD_DEL` (after delete), `EMP_TEMP_CARD_INS` (before insert), `EMP_TEMP_CARD_UPD` (before update)

## HRD.EMP_TEMP_RECORD

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_MRNO | VARCHAR2(14) | Y |  |
| CONTEXT_ID | VARCHAR2(50) | Y |  |
| DEPARTMENT_ID | VARCHAR2(10) | Y |  |
| DESIGNATION_ID | VARCHAR2(10) | Y |  |
| DOC_CATEGORY_ID | NUMBER | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| DEPARTMENT | VARCHAR2(200) | Y |  |
| DESIGNATION | VARCHAR2(200) | Y |  |
| JOINING_DATE | DATE | Y |  |
| EMP_NAME | VARCHAR2(200) | Y |  |
| DOCUMENT_STATUS | VARCHAR2(50) | Y |  |
| EMP_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.SP_SESSION

| Column | Type | Null | Comment |
|---|---|---|---|
| SP_SESSION_ID | NUMBER(6) | N |  |
| PROGRAM_ID | VARCHAR2(10) | Y |  |
| SESSION_START_DATE | DATE | N |  |
| SESSION_END_DATE | DATE | N |  |
| DI | CHAR(1) default 'N' | Y |  |

- **PK** `PK_SP_SESSION`: SP_SESSION_ID
- **FK** `FK_SP_SESSION_1`: (PROGRAM_ID) -> HRD.STUDY_PROGRAMS(PROGRAM_ID) [disabled]
- **Triggers**: `SP_SESSION_DEL` (after delete), `SP_SESSION_INS` (before insert), `SP_SESSION_UPD` (before update)

## HRD.SPS_SUBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SPS_SUBJECT_ID | NUMBER(6) | N |  |
| SP_SESSION_ID | NUMBER(6) | N |  |
| SUBJECT_ID | VARCHAR2(10) | N |  |
| SUBJECT_FROM_TIME | CHAR(5) | Y |  |
| SUBJECT_TO_TIME | CHAR(5) | Y |  |
| DAY_ID | NUMBER(1) | Y |  |
| SUBJECT_CREDIT_HOURS | NUMBER(3) | Y |  |
| LECTURE_DURATION | NUMBER(3) default 60 | Y |  |
| SUBJECT_INSTRUCTOR | VARCHAR2(14) | Y |  |
| LECTURE_DURATION_UNIT | VARCHAR2(30) | Y |  |
| DI | CHAR(1) default 'N' | Y |  |

- **PK** `PK_SPS_SUBJECTS`: SPS_SUBJECT_ID
- **FK** `FK_SPS_SUBJECTS_01`: (DAY_ID) -> DEFINITIONS.DAY(DAY_ID) [disabled]
- **FK** `FK_SPS_SUBJECTS_02`: (SUBJECT_ID) -> HRD.STUDY_SUBJECTS(SUBJECT_ID) [disabled]
- **FK** `FK_SPS_SUBJECTS_03`: (SP_SESSION_ID) -> HRD.SP_SESSION(SP_SESSION_ID) [disabled]
- **Triggers**: `SPS_SUBJECTS_DEL` (after delete), `SPS_SUBJECTS_INS` (before insert), `SPS_SUBJECTS_UPD` (before update)

## HRD.SPSS_LECTURES

| Column | Type | Null | Comment |
|---|---|---|---|
| SPSS_LECTURE_ID | NUMBER(6) | N |  |
| SPS_SUBJECT_ID | NUMBER(6) | Y |  |
| LECTURE_START_DATE | DATE | N |  |
| LECTURE_END_DATE | DATE | N |  |
| LECTURE_INSTRUCTOR | VARCHAR2(14) | Y |  |
| LECTURE_TITLE | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| LSD | DATE | N |  |
| LED | DATE | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| CANCELLED_SPSS_LECTURE_ID | NUMBER(6) | Y |  |
| LECTURE_CREDIT_HOURS | NUMBER(3,2) | Y |  |
| TRAINER_NAME | VARCHAR2(200) | Y |  |
| DI | CHAR(1) | Y |  |

- **PK** `PK_SPSS_LECTURES`: SPSS_LECTURE_ID
- **FK** `FK_SPSS_LECTURES_01`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID) [disabled]
- **FK** `FK_SPSS_LECTURES_02`: (SPS_SUBJECT_ID) -> HRD.SPS_SUBJECTS(SPS_SUBJECT_ID) [disabled]
- **FK** `FK_SPSS_LECTURES_03`: (LECTURE_INSTRUCTOR) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **CHECK** `CHK_SPSS_LECTURES_01`: ACTIVE IN ('Y','N')
- **Triggers**: `SPSS_LECTURES_DEL` (after delete), `SPSS_LECTURES_INS` (before insert), `SPSS_LECTURES_UPD` (before update)

## HRD.SPSSL_ATTENDANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(15) | N |  |
| DATE_TIME | DATE | N |  |
| SPSS_LECTURE_ID | NUMBER(6) | Y |  |
| SUBMIT_EVALUATION | CHAR(1) default 'Y' | Y |  |
| DI | CHAR(1) | Y |  |

- **PK** `PK_SPSSL_ATTENDANCE`: MRNO, DATE_TIME, SPSS_LECTURE_ID
- **FK** `FK_SPSSL_ATTENDANCE_02`: (SPSS_LECTURE_ID) -> HRD.SPSS_LECTURES(SPSS_LECTURE_ID)
- **CHECK** `CHK_SPSSL_ATTENDANCE`: SUBMIT_EVALUATION IN ('N','Y')
- **Triggers**: `SPSSL_ATTENDANCE_DEL` (after delete), `SPSSL_ATTENDANCE_INS` (before insert), `SPSSL_ATTENDANCE_UPD` (before update)

## HRD.EMP_TRAINING_OTHER_INFO

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(15) | N |  |
| TRAINING_DATE | DATE | N |  |
| SPSS_LECTURE_ID | NUMBER(6) | N |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(20) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(30) | Y |  |
| STATUS | VARCHAR2(30) | Y |  |
| ORGANIZER | VARCHAR2(50) | Y |  |

- **PK** `PK_EMP_TRAINING_OTHER_INFO`: MRNO, TRAINING_DATE, SPSS_LECTURE_ID
- **FK** `FK_EMP_TRAINING_OTHER_INFO_1`: (MRNO, TRAINING_DATE, SPSS_LECTURE_ID) -> HRD.SPSSL_ATTENDANCE(MRNO, DATE_TIME, SPSS_LECTURE_ID) [disabled]
- **FK** `FK_EMP_TRAINING_OTHER_INFO_2`: (SPSS_LECTURE_ID) -> HRD.SPSS_LECTURES(SPSS_LECTURE_ID) [disabled]
- **Triggers**: `EMP_TRAINING_OTHER_INFO_DEL` (after delete), `EMP_TRAINING_OTHER_INFO_INS` (before insert), `EMP_TRAINING_OTHER_INFO_UPD` (before update)

## HRD.EMP_UNDERSUPERVISION_SUP

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_UNDERSUPERVISION_HIST_ID | NUMBER(20) | N | ref hrd.emp_supervision_hist |
| SUPERVISOR_MRNO | VARCHAR2(14) | N |  |
| PRIVILEGES_ID | VARCHAR2(5) | Y |  |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | Y |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | Y |  |

- **Triggers**: `EMP_UNDERSUPERVISION_SUP_DEL` (after delete), `EMP_UNDERSUPERVISION_SUP_INS` (before insert), `EMP_UNDERSUPERVISION_SUP_UPD` (before update)

## HRD.EMP_UNDERSUPERVISION_SUP_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_UNDERSUPERVISION_HIST_ID | NUMBER(20) | N |  |
| SUPERVISOR_MRNO | VARCHAR2(14) | Y |  |
| CPT_ID | VARCHAR2(18) | N |  |
| IS_UNDERSUPERVISION | CHAR(1) | Y |  |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | N | THIS COLUMN CONATINS THE VALUE FROM CPT GROUP TYPE |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N | THIS COLUMN CONATINS THE VALUE FROM CPT GROUP TYPE |
| PATIENT_TYPE | CHAR(1) | Y |  |

- **PK** `PK_EMP_UNDER_SUP_CPT`: CPT_ID, EMP_UNDERSUPERVISION_HIST_ID, CPT_GROUP_TYPE_ID, CPT_RESTRICTION_TYPE_ID
- **Triggers**: `EMP_UNDERSUPERVISION_SUP_CPT_DEL` (after delete), `EMP_UNDERSUPERVISION_SUP_CPT_INS` (before insert), `EMP_UNDERSUPERVISION_SUP_CPT_UPD` (before update), `EMP_UNDSUPVISION_SUP_CPT_DEL` (after delete), `EMP_UNDSUPVISION_SUP_CPT_INS` (before insert), `EMP_UNDSUPVISION_SUP_CPT_UPD` (before update)

## HRD.EMP_WISE_CPT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| EMP_UNDERSUERVISION_HIST_ID | NUMBER | Y |  |
| SUP_MRNO | VARCHAR2(14) | Y |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | Y |  |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | Y |  |
| PATIENT_TYPE | CHAR(1) | Y |  |


## HRD.EMP_WISE_DOCMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |

- **PK** `EMP_WISE_PK`: DOC_CATEGORY_ID, MRNO, DOCUMENT_TYPE_ID
- **Triggers**: `EMP_WISE_DOCMENT_TYPE_DEL` (after delete), `EMP_WISE_DOCMENT_TYPE_INS` (before insert), `EMP_WISE_DOCMENT_TYPE_UPD` (before update), `EMP_WISE_DOC_DEL` (before delete), `EMP_WISE_DOC_INSERT` (after insert or update of mrno,doc_category_id ,document_type_id)

## HRD.EMP_WISE_DOCUEMENT_REQUIRED

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_CATEGORY_ID | NUMBER | N |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| MRNO | VARCHAR2(14) | N |  |
| DOCUMENTS_STATUS | CHAR(1) | Y |  |
| EMP_WISE | CHAR(1) default 'N' | Y |  |
| DEPT_WISE | CHAR(1) default 'N' | Y |  |
| DESIG_WISE | CHAR(1) default 'N' | Y |  |
| DESIG_CAT_WISE | CHAR(1) default 'N' | Y |  |

- **PK** `EMP_WISE_DOCUEMENT_PK`: DOC_CATEGORY_ID, DOCUMENT_TYPE_ID, MRNO
- **Triggers**: `EMP_WISE_REQ_DEL` (after delete), `EMP_WISE_REQ_INS` (before insert), `EMP_WISE_REQ_UPD` (before update)

## HRD.EMP_WISE_REPLACEMENT_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DETIAL_SR_NO | NUMBER | Y |  |
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
| MRNO | VARCHAR2(14) | N |  |
| NEW_MRNO | VARCHAR2(14) | Y |  |
| COUNT | NUMBER | Y |  |
| NOT_APPLICABLE | CHAR(1) | Y |  |

- **PK** `EMP_WISE_REPLAC_EVENT_PK`: SR_NO, MRNO
- **Triggers**: `EMP_WISE_REPLACEMENT_EVENT_DEL` (after delete), `EMP_WISE_REPLACEMENT_EVENT_INS` (before insert), `EMP_WISE_REPLACEMENT_EVENT_UPD` (before update)

## HRD.EOBI_CALCULATION

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_START | DATE | N |  |
| MONTH_END | DATE | N |  |
| SATUS | CHAR(1) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| JOINING_DATE | DATE | Y |  |
| POSITION_LOCATION_ID | VARCHAR2(3) | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(3) | Y |  |
| IS_POSTED | CHAR(1) default 'N' | Y |  |
| IS_NEW_JOINER | CHAR(1) | Y |  |
| IS_LEAVER | CHAR(1) | Y |  |
| WORKING_DAYS | NUMBER(3) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| POST_DATE | DATE | Y |  |
| POST_BY | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT | VARCHAR2(200) | Y |  |
| DESIGNATION_ID | VARCHAR2(10) | Y |  |
| DESIGNATION | VARCHAR2(200) | Y |  |
| NIC | VARCHAR2(20) | Y |  |
| ADDRESS | VARCHAR2(1000) | Y |  |
| DATE_OF_BIRTH | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| DUTY_LOCATION | VARCHAR2(200) | Y |  |
| GENDER | VARCHAR2(20) | Y |  |
| AGE | VARCHAR2(20) | Y |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | VARCHAR2(13) | Y |  |
| FATHER_NAME | VARCHAR2(100) | Y |  |
| HUSBAND_NAME | VARCHAR2(100) | Y |  |
| RELATIONSHIP_CODE | CHAR(1) | Y |  |
| CITY | VARCHAR2(100) | Y |  |
| PROVINCE | VARCHAR2(100) | Y |  |
| PHONE | VARCHAR2(100) | Y |  |
| EMAIL | VARCHAR2(50) | Y |  |
| PATIENT_AGE | NUMBER | Y |  |
| GENDER_SHORT | CHAR(1) | Y |  |
| DATE_OF_BIRTH_FORMAT | VARCHAR2(20) | Y |  |
| JOINING_DATE_FORMAT | VARCHAR2(20) | Y |  |
| MONTH_ID | VARCHAR2(10) | Y |  |

_No standard audit columns._

- **PK** `PK_EOBI_CALCULATION`: MONTH_START, MONTH_END, MRNO

## HRD.EOBI_CALCULATION_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_ID | VARCHAR2(6) | N |  |
| MONTH_START | DATE | Y |  |
| MONTH_END | DATE | Y |  |
| IS_POSTED | CHAR(1) | Y |  |
| POSTED_DATE | DATE | Y |  |
| POSTED_BY | VARCHAR2(14) | Y |  |

_No standard audit columns._

- **PK** `PK_EOBI_CALCULATION_MASTER`: MONTH_ID

## HRD.EOBI_SUB_DUYT_LOCATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| SUB_LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

_No standard audit columns._

- **PK** `OK_SUB_LOC`: LOCATION_ID, SUB_LOCATION_ID

## HRD.EVALUATION_ALERT_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ALERT_DATE | DATE | Y | EVALUATION ALERT SEND DATE |
| CONFIRMATION_DATE | DATE | Y | EVALUATION CONFIRMATION DATE |
| IS_CONFIRMED | CHAR(1) default 'I' | Y | EVALUATION CONFIRMATION STATUS IN 'C' COMPLETED , 'E' EXTEND 'P' PENDING 'I' IN PROCESS |
| CONFIRMED_BY | VARCHAR2(14) | Y | CONFIRMED BY GLOBAL USER MRNO |
| CONFIRMED_DATE | DATE | Y | SYSDATE |
| JOINING_DATE | DATE | Y |  |
| EVALUATION_TYPE | VARCHAR2(3) | Y | ALERT ID REF TO HRD.ALERTS |
| EXTENDED_DAYS | NUMBER | Y | IF EXTENDED EXTENDED DAYS MUST BE ENTERED OTHERWISE NULL |
| REMARKS | VARCHAR2(4000) | Y | OPEN TEXT FOR REMARKS |

- **Triggers**: `EVALUATION_ALERT_QUEUE_DEL` (after delete), `EVALUATION_ALERT_QUEUE_INS` (before insert), `EVALUATION_ALERT_QUEUE_UPD` (before update)

## HRD.EXPIRED_DOCUMENT_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | VARCHAR2(20) | N |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| EXPIRY_DATE | DATE | Y |  |
| DOCUMENT_CATEGORY_ID | NUMBER | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | Y |  |
| ALERT_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EXP_DOC_01`: QUEUE_ID
- **Triggers**: `EXPIRED_DOCUMENT_DASHBOARD_DEL` (after delete), `EXPIRED_DOCUMENT_DASHBOARD_INS` (after insert), `EXPIRED_DOCUMENT_QUEUE_DEL` (after delete), `EXPIRED_DOCUMENT_QUEUE_INS` (before insert), `EXPIRED_DOCUMENT_QUEUE_PT_DEL` (after delete), `EXPIRED_DOCUMENT_QUEUE_PT_INS` (after insert), `EXPIRED_DOCUMENT_QUEUE_UPD` (before update)

## HRD.EXPIRED_REGISTRATION_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| EXPIRY_DATE | DATE | Y |  |
| REGISTRATION_TYPE_ID | NUMBER(5) | Y |  |

_No standard audit columns._


## HRD.FORM_GUIDELINES

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(12) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DOC_DESCRIPTION | VARCHAR2(200) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHED_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| SR_NO | NUMBER | N |  |
| ATTACHMENT_ID | NUMBER | Y |  |

- **PK** `PK_FORM_GUIDELINES`: SR_NO
- **UK** `UK_FORM_GUIDELINES`: OBJECT_CODE, ATTACHMENT_ID
- **Triggers**: `FORM_GUIDELINES_DEL` (after delete), `FORM_GUIDELINES_INS` (before insert), `FORM_GUIDELINES_UPD` (before update)

## HRD.FPPE_EVALUATION_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| IN_QUEUE_OF | VARCHAR2(14) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| QUEUE_ENTRY_DATE | DATE | Y |  |
| QUEUE_STAUS | CHAR(2) default 'HR' | Y | 'HR QUEUE', 'HD HOD QUEUE, 'PR PROCTOR QUEUE' |
| STATUS | CHAR(1) default 'I' | Y | 'I IN PROCESS  C COMPLETE' |
| QUEUE_FORWARD_TO_HOD | VARCHAR2(14) | Y |  |
| QUEUE_FORWARD_DATE | DATE | Y |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| IN_QUEUE_OF_PROCTOR | VARCHAR2(14) | Y |  |
| IN_QUEUE_OF_HOD | VARCHAR2(14) | Y |  |

- **PK** `FPPE_EVALUATION_QUEUE_PK`: QUEUE_ID
- **Triggers**: `FPPE_EVALUATION_HR_QUEUE` (after insert or update of queue_staus, status), `FPPE_EVALUATION_QUEUE_DEL` (after delete), `FPPE_EVALUATION_QUEUE_INS` (before insert), `FPPE_EVALUATION_QUEUE_UPD` (before update)

## HRD.FPPE_EVAL_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| FPPE_EVAL_ID | VARCHAR2(20) | N |  |
| EMPLOYEE_MRNO | VARCHAR2(14) | N |  |
| PRIVILEGES_ID | NUMBER | N |  |
| PRIVILEGES_DETAIL_ID | NUMBER | N |  |
| SP_PRIVILEGE_ID | NUMBER | N |  |
| NO_REQUIRED | NUMBER | Y |  |
| NOT_APPLICABLE | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `FPPE_EVAL_DTL_PK`: FPPE_EVAL_ID, PRIVILEGES_ID, PRIVILEGES_DETAIL_ID, SP_PRIVILEGE_ID, EMPLOYEE_MRNO
- **Triggers**: `FPPE_EVAL_DTL_DEL` (after delete), `FPPE_EVAL_DTL_INS` (before insert), `FPPE_EVAL_DTL_UPD` (before update)

## HRD.FPPE_EVAL_MST

| Column | Type | Null | Comment |
|---|---|---|---|
| FPPE_EVAL_ID | NUMBER(10) | N |  |
| EMPLOYEE_MRNO | VARCHAR2(14) | N |  |
| EVALUATION_DATE | DATE default SYSDATE | Y |  |
| EVAL_DUE_DATE | DATE | Y |  |
| PROCTOR_MRNO | VARCHAR2(14) | Y |  |
| HOD_APPROVED_BY | VARCHAR2(14) | Y |  |
| HOD_APPROVED_DATE | DATE | Y |  |
| PROCTOR_APPROVED_BY | VARCHAR2(14) | Y |  |
| PROCTOR_APPROVED_DATE | DATE | Y |  |
| STATUS | VARCHAR2(3) | Y |  |
| FINAL_ASSESSMENT_DECISION | CHAR(1) | Y |  |
| EXTENSION_DURATION | NUMBER | Y |  |
| CORRECTIVE_PLAN_REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `FPPE_EVAL_MST_PK`: FPPE_EVAL_ID, EMPLOYEE_MRNO
- **Triggers**: `FPPE_EVAL_MST_DEL` (after delete), `FPPE_EVAL_MST_INS` (before insert), `FPPE_EVAL_MST_UPD` (before update)

## HRD.FPPE_METHOD_REVIEW_MRNO

| Column | Type | Null | Comment |
|---|---|---|---|
| ADD_MRNO | VARCHAR2(14) | N |  |
| ENTRY_DATE | DATE | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| PERORMANCE_INDICATOR_ID | NUMBER | Y |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |

- **PK** `FPPE_METHOD_REVIEW_MRNO_PK`: ADD_MRNO, ENTRY_DATE, EMPLOYEE_CODE
- **Triggers**: `FPPE_METHOD_REVIEW_MRNO_DEL` (after delete), `FPPE_METHOD_REVIEW_MRNO_INS` (before insert), `FPPE_METHOD_REVIEW_MRNO_UPD` (before update)

## HRD.FPPE_PROFORMANCE_INDICATORS

| Column | Type | Null | Comment |
|---|---|---|---|
| PERORMANCE_INDICATOR_ID | NUMBER | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| PERFORMANCE_INDICATOR_TYPE | CHAR(1) | N |  |
| SCORE | VARCHAR2(3) | Y |  |
| NOT_APPLICABLE | CHAR(1) | Y |  |
| MRNO_DATE | VARCHAR2(1000) | Y |  |

- **PK** `FPPE_PROFORMANCE_INDICATORS_PK`: PERORMANCE_INDICATOR_ID, EMPLOYEE_CODE, PERFORMANCE_INDICATOR_TYPE
- **Triggers**: `FPPE_PRO_INDICATORS_DEL` (after delete), `FPPE_PRO_INDICATORS_INS` (before insert), `FPPE_PRO_INDICATORS_UPD` (before update)

## HRD.FRAUD_NATURE

| Column | Type | Null | Comment |
|---|---|---|---|
| INCIDENT_TYPE_ID | NUMBER(3) | N |  |
| INCIDENT_TYPE | CHAR(3) | Y | 3 type of incident type 1 Internal = Employee  ,2 External = Vendor , 3 Patient |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| INCIDENT_CATEGORY_ID | VARCHAR2(10) | Y |  |

- **PK** `FRAUD_NATURE_PK`: INCIDENT_TYPE_ID
- **UK** `FRAUD_NATURE_UK`: INCIDENT_TYPE
- **Triggers**: `FRAUD_NATURE_DEL` (after delete), `FRAUD_NATURE_INS` (before insert), `FRAUD_NATURE_UPD` (before update)

## HRD.FRAUD_REGISTER_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | N | attachement againts  register id |
| MRNO | VARCHAR2(14) | Y |  |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y | Use for given remarks |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| INCIDENT_TYPE_ID | NUMBER(7) | Y |  |

- **PK** `FRAUD_REGISTER_ATTACHMENT_PK`: SR_NO, INCIDENT_REGISTER_ID

## HRD.GRADE_SALARY_RANGE

| Column | Type | Null | Comment |
|---|---|---|---|
| GRADE_ID | VARCHAR2(6) | N |  |
| SALARY_LOWER_LIMIT | NUMBER(8) | N |  |
| SALARY_UPPER_LIMIT | NUMBER(8) | N |  |
| EFFECTIVE_DATE | DATE | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ACTUAL_UPPER_LIMIT | NUMBER(8) | N |  |

- **PK** `PK_GRADE_SALARY_RANGE`: EFFECTIVE_DATE, GRADE_ID
- **FK** `FK_GRADE_SALARY_RANGE_1`: (GRADE_ID) -> DEFINITIONS.GRADES(GRADE_ID) [disabled]
- **CHECK** `CK_GRADE_SALARY_RANGE_001`: ACTIVE IN ('Y','N')
- **Triggers**: `GRADE_SALARY_RANGE_DEL` (after delete), `GRADE_SALARY_RANGE_INS` (before insert), `GRADE_SALARY_RANGE_UPD` (before update)

## HRD.GROUP_EMAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| EMAIL | VARCHAR2(50) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(50) | Y |  |

_No standard audit columns._

- **PK** `PK_GROUP_EMAIL`: EMAIL

## HRD.HINT_OBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(5) | N |  |
| OBJECT_CODE | VARCHAR2(12) | N |  |
| DISPLAY_NAME | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_HINT_OBJECTS`: SCHEMA_ID, OBJECT_CODE
- **Triggers**: `HINT_OBJECTS_DEL` (after delete), `HINT_OBJECTS_INS` (before insert), `HINT_OBJECTS_UPD` (before update)

## HRD.HIRING_REQUEST_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ORDER_BY | NUMBER | Y |  |
| POSITION_CATEGORY | CHAR(1) | N |  |
| FORWORD_TO_HR | CHAR(1) default 'N' | Y |  |
| IS_HOD | CHAR(1) default 'N' | Y | This column will be used to mark the HOD in the Hierarchy in case of HOLD HIRING REQUESTS |
| REVIEW_JD | CHAR(1) default 'N' | Y | This column will be used to mark the level where JD review is compulsory in the Hierarchy. |

- **PK** `PK_HR_HIERARCHY`: DEPARTMENT_ID, MRNO, POSITION_CATEGORY
- **FK** `FK_DEPARTMENT_ID`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **FK** `FK_HR_MRNO`: (MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **Triggers**: `HIRING_REQUEST_HIERARCHY_DEL` (after delete), `HIRING_REQUEST_HIERARCHY_INS` (before insert), `HIRING_REQUEST_HIERARCHY_UPD` (before update)

## HRD.HIRING_REQUEST_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_ID | NUMBER(7) | N |  |
| REQUEST_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENTAL_REMARKS | VARCHAR2(4000) | Y |  |
| REJECTION_REMARKS | VARCHAR2(4000) | Y |  |
| JUSTIFICATION | VARCHAR2(4000) | Y |  |
| CATEGORY_TYPE | CHAR(1) | Y |  |
| POSITION_TYPE | CHAR(1) | Y |  |
| DURATION_UNIT | CHAR(1) | Y |  |
| DURATION | NUMBER(4) | Y |  |
| NO_OF_POSITIONS | NUMBER(4) | Y |  |
| REPLACEMENT_OF | VARCHAR2(14) | Y |  |
| FINANCIAL_YEAR | NUMBER(4) | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| EMPLOYEE_TYPE_ID | VARCHAR2(6) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| POSITION_CATEGORY | CHAR(1) | Y |  |
| MONTH | DATE | Y |  |
| HIRING_REASON | VARCHAR2(4000) | Y |  |
| AVAILABLE_POSITIONS | NUMBER | Y |  |
| JOB_TYPE | VARCHAR2(1) | Y |  |
| HIRING_DESIGNATION_ID | VARCHAR2(6) | Y |  |
| APPROVED_NO_OF_POSITION | NUMBER(3) | Y |  |
| HOLD_TILL_DATE | DATE | Y |  |
| FORWARDED_TO_HR | CHAR(1) default 'N' | Y | If request forwarded to hr (hiring request becomes non editable) |
| SEATING_SPACE_AVAILABLE | CHAR(1) | Y | HOD will check this Seating Space Available check before forwarding the hiring request |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| JOB_CATEGORY_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_REQUEST_ID`: REQUEST_ID
- **Triggers**: `HIRING_REQUEST_MASTER_DEL` (after delete), `HIRING_REQUEST_MASTER_INS` (before insert), `HIRING_REQUEST_MASTER_UPD` (before update)

## HRD.HIRING_REQUEST_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER | N |  |
| REQUEST_ID | NUMBER | N |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| DECISION | VARCHAR2(100) | Y |  |
| IN_QUEUE_OF | VARCHAR2(14) | Y |  |
| AUTHORITY_REMARKS | VARCHAR2(4000) | Y |  |
| AUTHORITY_ORDER | NUMBER | Y |  |
| DECISION_DATE | DATE | Y |  |

- **Triggers**: `HIRING_REQUEST_QUEUE_DEL` (after delete), `HIRING_REQUEST_QUEUE_INS` (before insert), `HIRING_REQUEST_QUEUE_PT_DEL` (after delete), `HIRING_REQUEST_QUEUE_PT_INS` (before insert), `HIRING_REQUEST_QUEUE_PT_UPD` (after update), `HIRING_REQUEST_QUEUE_UPD` (before update)

## HRD.HIRING_REQUEST_QUEUE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_HISTORY_ID | NUMBER | N |  |
| QUEUE_ID | NUMBER | N |  |
| REQUEST_ID | NUMBER | N |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |
| DECISION | VARCHAR2(100) | Y |  |
| IN_QUEUE_OF | VARCHAR2(14) | Y |  |
| AUTHORITY_REMARKS | VARCHAR2(4000) | Y |  |
| DECISION_DATE | DATE | Y |  |
| DECISION_BY | VARCHAR2(14) | Y |  |
| AUTHORITY_ORDER | NUMBER | Y |  |
| APPROVED_NO_OF_POSITION | NUMBER(3) | Y |  |
| HOLD_TILL_DATE | DATE | Y |  |

- **Triggers**: `HIRING_REQ_QUEUE_HISTORY_DEL` (after delete), `HIRING_REQ_QUEUE_HISTORY_INS` (before insert), `HIRING_REQ_QUEUE_HISTORY_UPD` (before update)

## HRD.HOD_EXCEPTION

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| EXCEPTION_ERROR | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.HOD_REPLACEMENT_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| EVENT_DESCRIPTION | VARCHAR2(1000) | Y |  |
| MODULE_ID | VARCHAR2(10) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `HOD_REPLACEMENT_EVENT_PK`: SR_NO
- **Triggers**: `HOD_REPLACEMENT_EVENT_DEL` (after delete), `HOD_REPLACEMENT_EVENT_INS` (before insert), `HOD_REPLACEMENT_EVENT_UPD` (before update)

## HRD.HOD_REPLACEMENT_EVENT_DETAILS

| Column | Type | Null | Comment |
|---|---|---|---|
| DETIAL_SR_NO | NUMBER | N |  |
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

- **PK** `HOD_REPLACEMENT_EVENT_DETAILS_PK`: DETIAL_SR_NO, SR_NO
- **FK** `HOD_REPLACEMENT_EVENT_DETAILS_FK`: (SR_NO) -> HRD.HOD_REPLACEMENT_EVENT(SR_NO)
- **Triggers**: `HOD_REPLAC_EVENT_DETAILS_DEL` (after delete), `HOD_REPLAC_EVENT_DETAILS_INS` (before insert), `HOD_REPLAC_EVENT_DETAILS_UPD` (before update)

## HRD.HOD_REPLACEMENT_SUB_EVENT_DET

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DETIAL_SR_NO | NUMBER | N |  |
| SUB_EVENT_SR_NO | NUMBER | N |  |
| SUB_EVENT_ID | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `HOD_REPLACEMENT_SUB_EVENT_DET_PK`: SR_NO, DETIAL_SR_NO, SUB_EVENT_SR_NO
- **FK** `HOD_REPLACEMENT_SUB_EVENT_DET_FK1`: (DETIAL_SR_NO, SR_NO) -> HRD.HOD_REPLACEMENT_EVENT_DETAILS(DETIAL_SR_NO, SR_NO)
- **Triggers**: `HOD_REPLC_SUB_EVNT_DET_DEL` (after delete), `HOD_REPLC_SUB_EVNT_DET_INS` (before insert), `HOD_REPLC_SUB_EVNT_DET_UPD` (before update)

## HRD.HOD_SUB_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SUB_EVENT_ID | NUMBER | N |  |
| SUB_EVENT_DESC | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `HOD_SUB_EVENT_PK`: SUB_EVENT_ID
- **Triggers**: `HOD_SUB_EVENT_DEL` (after delete), `HOD_SUB_EVENT_UPD` (before update)

## HRD.HOSPITAL_EMP_MEDICAL_SUPPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_MEDICAL_SUPPORT_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| FROM_SALARY_VALUE | NUMBER(9,2) | Y |  |
| TO_SALARY_VALUE | NUMBER(9,2) | Y |  |
| IPD_PERCENTAGE | NUMBER(5,2) | Y |  |
| OPD_PERCENTAGE | NUMBER(5,2) | Y |  |
| IPD_CASH_PERCENTAGE | NUMBER(5,2) | Y |  |
| IPD_CREDIT_PERCENTAGE | NUMBER(5,2) | Y |  |
| OPD_CASH_PERCENTAGE | NUMBER(5,2) | Y |  |
| OPD_CREDIT_PERCENTAGE | NUMBER(5,2) | Y |  |


## HRD.HRD_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SETUP_VALUE | VARCHAR2(60) | Y |  |

- **PK** `PK_HRD_SETUP`: SETUP_ID

## HRD.HR_ALERT_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| ALERT_ID | VARCHAR2(3) | N |  |
| SUBJECT_ID | VARCHAR2(200) | N |  |
| ENTRY_DATE | DATE | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| SCHEDULE_MASTER_ID | VARCHAR2(9) | Y |  |
| PRIVILEGE_ID | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y | Y FOR ACTIVE AND N FOR IN-ACTIVE |
| REMARKS | VARCHAR2(4000) | Y | REMARKS |
| IS_SIGNED | CHAR(1) default 'N' | Y | IS SIGNED BY CHAIR OR SECRETRY |

- **PK** `PK_HR_ALERT_QUEUE`: MRNO, ALERT_ID, SUBJECT_ID
- **Triggers**: `HR_ALERT_QUEUE_DEL` (after delete), `HR_ALERT_QUEUE_INS` (before insert), `HR_ALERT_QUEUE_PT_DEL` (after delete), `HR_ALERT_QUEUE_PT_INS` (before insert), `HR_ALERT_QUEUE_UPD` (before update)

## HRD.HR_DOCUMENT_DASHBOARD_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `HR_DOCUMENT_DASHBOARD_MASTER_PK`: SR_NO
- **Triggers**: `HR_DOC_DASHBOARD_MASTER_DEL` (after delete), `HR_DOC_DASHBOARD_MASTER_INS` (before insert), `HR_DOC_DASHBOARD_MASTER_UPD` (before update)

## HRD.HR_DOCUMENT_DASHBOARD_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DETAIL_ID | NUMBER | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `HR_DOCUMENT_DASHBOARD_DETAIL_PK`: DETAIL_ID, SR_NO
- **FK** `HR_DOCUMENT_DASHBOARD_DETAIL_FK`: (SR_NO) -> HRD.HR_DOCUMENT_DASHBOARD_MASTER(SR_NO)
- **Triggers**: `HR_DOC_DASHBOARD_DETAIL_DEL` (after delete), `HR_DOC_DASHBOARD_DETAIL_INS` (before insert), `HR_DOC_DASHBOARD_DETAIL_UPD` (before update)

## HRD.HR_DOC_REC_HIERARCY

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| GROUP_ID | VARCHAR2(10) | N |  |
| ATTACH_BY_MRNO | VARCHAR2(14) | Y |  |
| DOCUMENT_ROLE | CHAR(1) | Y | 'A' ATTACH DOCUMENT 'V' 'VERIFY DOCUMENT' |
| VERIFY_BY | VARCHAR2(14) | Y |  |

- **PK** `HR_DOC_HIERARCY_PK`: DOCUMENT_TYPE_ID, DOC_CATEGORY_ID, GROUP_ID
- **FK** `HR_DOC_HIERARCY_FK`: (DOCUMENT_TYPE_ID, DOC_CATEGORY_ID) -> HRD.DOCUMENT_TYPE(DOCUMENT_TYPE_ID, DOC_CATEGORY_ID)
- **Triggers**: `HR_DOC_REC_HIERARCY_DEL` (after delete), `HR_DOC_REC_HIERARCY_INS` (before insert), `HR_DOC_REC_HIERARCY_UPD` (before update)

## HRD.HR_DOC_REC_TRACK

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DOC_CATEGORY_ID | NUMBER | N |  |
| DOC_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| STATUS | CHAR(1) | Y | 'D' Draft , I'In Process', V 'Verify','F' FORWARD |
| SECTION_ID | VARCHAR2(50) | Y |  |
| OBJECT_CODE | VARCHAR2(14) | Y |  |
| HR_EMP_DEPARTMENT_ID | VARCHAR2(50) | Y |  |
| IS_FILE_ATTACHED | CHAR(1) default 'N' | Y |  |
| DOCUMENTS_STATUS | CHAR(1) | Y | 'E'Expire ,'M''Miss' |
| IS_VERIFY | CHAR(1) | Y |  |
| GROUP_ID | VARCHAR2(10) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| QUEUE_ID | VARCHAR2(20) | Y |  |

- **PK** `HR_DOC_REC_TRACK_PK`: DOCUMENT_TYPE_ID, DOC_CATEGORY_ID, MRNO
- **FK** `HR_DOC_REC_TRACK_FK`: (DOCUMENT_TYPE_ID, DOC_CATEGORY_ID) -> HRD.DOCUMENT_TYPE(DOCUMENT_TYPE_ID, DOC_CATEGORY_ID)
- **Triggers**: `HR_DOC_REC_TRACK_DEL` (after delete), `HR_DOC_REC_TRACK_INS` (before insert), `HR_DOC_REC_TRACK_UPD` (before update)

## HRD.HR_EXCEPTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| E_DATE | DATE | Y |  |
| EXCEPTION_DESC | VARCHAR2(400) | Y |  |
| E_TYPE | VARCHAR2(80) | Y |  |

- **Triggers**: `HR_EXCEPTIONS_INS` (before insert)

## HRD.HR_JD_ATTACHMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| ATTACHED_DATE | DATE | Y | This column contains ATTACHED DATE |
| REQUEST_ID | NUMBER | Y |  |
| DOCUMENT_TYPE | CHAR(1) | Y | This column contains Document Type from HRD.DOCUMENT_CATEGORY table |
| JD_REVIEWED | CHAR(1) | Y | This column is marked yes if HOD reviewed the JD |

- **PK** `PK_JD_SRNO`: SR_NO
- **FK** `FK_REQUEST_ID`: (REQUEST_ID) -> HRD.HIRING_REQUEST_MASTER(REQUEST_ID) [disabled]
- **Triggers**: `HR_JD_ATTACHMENTS_DEL` (after delete), `HR_JD_ATTACHMENTS_INS` (before insert), `HR_JD_ATTACHMENTS_UPD` (before update)

## HRD.HR_RECORD_DESIG_CATEGORY_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_CATEGORY_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DOCUMENT_TYPE_ID | NUMBER | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |

- **PK** `PK_HR_RECORD_DESIG_CATEGORY`: DOC_CATEGORY_ID, DOCUMENT_TYPE_ID, DESIGNATION_CATEGORY_ID
- **Triggers**: `DESIG_CATEGORY_DOC_DEL` (before delete), `DESIG_CATE_WSIE_DOC_INSERT` (after insert or update of designation_category_id, doc_category_id, document_type_id), `HR_REC_DESIG_CATG_SETUP_DEL` (after delete), `HR_REC_DESIG_CATG_SETUP_INS` (before insert), `HR_REC_DESIG_CATG_SETUP_UPD` (before update)

## HRD.IMPORT_TRG_DATA_FROM_EXCEL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | VARCHAR2(100) | Y |  |
| TRAINING_TYPE | VARCHAR2(100) | Y |  |
| NAME_OF_THE_EMPLOYEE | VARCHAR2(1000) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(100) | Y |  |
| DESIGNATION_ | VARCHAR2(1000) | Y |  |
| DEPARTMENT | VARCHAR2(1000) | Y |  |
| JOINING_DATE | VARCHAR2(100) | Y |  |
| TRAINING_COURSE | VARCHAR2(1000) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(1000) | Y |  |
| TRAINER | VARCHAR2(1000) | Y |  |
| ORGANIZER | VARCHAR2(100) | Y |  |
| FROM_DATE | VARCHAR2(100) | Y |  |
| TO_DATE | VARCHAR2(100) | Y |  |
| TRAINING_DURATION | VARCHAR2(100) | Y |  |
| BOND_DURATION | VARCHAR2(100) | Y |  |
| BOND_COST | VARCHAR2(100) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(100) | Y |  |
| VALIDITY | VARCHAR2(100) | Y |  |
| STATUS | VARCHAR2(100) | Y |  |
| DURATION | VARCHAR2(20) | Y |  |
| DURATION_UNIT | VARCHAR2(20) | Y |  |


## HRD.INACTIVE_EMPLOYEE_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(192) | Y |  |
| DEPARTMENT | VARCHAR2(4000) | Y |  |
| DESIGNATION | VARCHAR2(4000) | Y |  |
| CONTRACT_START_DATE | DATE | Y |  |
| CONTRACT_END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(4000) | Y |  |
| DESIGNATION_ID | VARCHAR2(4000) | Y |  |
| LEAVING_DATE | DATE | Y |  |
| EXPIRY | CHAR(1) | Y |  |
| INTIMATION_SENT_DATE | DATE | Y |  |

_No standard audit columns._

- **Triggers**: `INACTIVE_EMPLOYEE_QUEUE_DEL` (after delete)

## HRD.INCIDENT_COMMITTEE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(8) | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| EMP_ADDED_DATE | DATE | Y | This column use for when committe member added in this |

- **PK** `PK_INCIDENT_COMMITTEE`: SR_NO
- **UK** `UK_INCIDENT_COMMITTEE`: INCIDENT_REGISTER_ID, EMPLOYEE_CODE
- **Triggers**: `INCIDENT_COMMITTEE_DEL` (after delete), `INCIDENT_COMMITTEE_INS` (before insert), `INCIDENT_COMMITTEE_UPD` (before update)

## HRD.INCIDENT_REGISTRATION

| Column | Type | Null | Comment |
|---|---|---|---|
| INCIDENT_REGISTER_ID | VARCHAR2(10) | N |  |
| INCIDENT_TYPE_ID | NUMBER(3) | Y |  |
| INCIDENT_DATE | DATE | Y |  |
| LOGGED_DATE | DATE | Y |  |
| INCIDENT_STATUS | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| CONCLUSION | CLOB | Y |  |
| DESCRIPTION | CLOB | Y |  |
| INCIDENT_REPORTED_ON | DATE | Y |  |
| ISSUE_ASSIGNED_TO | VARCHAR2(14) | Y |  |
| CLOSED_ON | DATE | Y |  |
| PARENT_ID | VARCHAR2(10) | Y |  |

- **PK** `PK_INCIDENT_REGISTER`: INCIDENT_REGISTER_ID
- **FK** `FK_INCIDENT_TYPE_ID`: (INCIDENT_TYPE_ID) -> HRD.FRAUD_NATURE(INCIDENT_TYPE_ID) [disabled]
- **Triggers**: `INCIDENT_REGISTRATION_DEL` (after delete), `INCIDENT_REGISTRATION_INS` (before insert), `INCIDENT_REGISTRATION_UPD` (before update)

## HRD.INCIDENT_FORWARD_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER(8) | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | Y |  |
| IN_QUEUE_OF | VARCHAR2(14) | Y |  |
| ACKNOWLEDGE | CHAR(1) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| INCIDENT_TYPE_ID | NUMBER(3) | Y |  |

- **PK** `PK_INCIDENT_FORWARD_Q`: QUEUE_ID
- **FK** `FK_INCIDENT_FORWARD_Q`: (INCIDENT_REGISTER_ID) -> HRD.INCIDENT_REGISTRATION(INCIDENT_REGISTER_ID) [disabled]
- **Triggers**: `INCIDENT_FORWARD_Q_DEL` (after delete), `INCIDENT_FORWARD_Q_INS` (before insert), `INCIDENT_FORWARD_Q_UPD` (before update)

## HRD.INCIDENT_FORWARD_TO

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(8) | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| ACTION_REQUIRED | CHAR(1) | Y |  |
| ACTION_TO_PERFORM | CLOB | Y |  |
| IS_FARWARD | CHAR(1) | Y |  |
| ACTION_PERFORMED | CLOB | Y |  |
| FORWARD_DATE | DATE | Y |  |
| COMPLETE_DATE | DATE | Y |  |
| ACKNOWLEDGE_DATE | DATE | Y |  |
| REMARKS | CLOB | Y |  |
| DAYS | NUMBER | Y |  |

- **PK** `PK_INCIDENT_FORWARD_TO`: SR_NO
- **UK** `UK_INCIDENT_FORWARD_TO`: INCIDENT_REGISTER_ID, EMPLOYEE_CODE
- **Triggers**: `INCIDENT_FORWARD_TO_DEL` (after delete), `INCIDENT_FORWARD_TO_INS` (before insert), `INCIDENT_FORWARD_TO_UPD` (before update)

## HRD.INCIDENT_NATURE_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ACTIVE_CATEGORY | CHAR(1) | Y |  |
| DEFAULT_CATEGORY | CHAR(1) | Y |  |

- **PK** `PK_INCIDENT_NATURE_CATEGORY`: CATEGORY_ID
- **Triggers**: `INCIDENT_NATURE_CATEGORY_DEL` (after delete), `INCIDENT_NATURE_CATEGORY_INS` (before insert), `INCIDENT_NATURE_CATEGORY_UPD` (before update)

## HRD.INCIDENT_PERSON_INVOLEVE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(8) | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | Y |  |
| INCIDENT_REPORTED_TYPE | CHAR(1) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(120) | Y |  |
| COMPANY_NAME | VARCHAR2(300) | Y |  |
| CONTACT_DETAIL | VARCHAR2(50) | Y |  |
| DOCUMENT_ID | VARCHAR2(50) | Y |  |
| SR_NO_NEW | VARCHAR2(20) | N |  |
| INCIDENT_DETAIL_ID | NUMBER | Y |  |
| INVOLVE_DATE | DATE | Y |  |

- **PK** `PK_INCIDENT_PERSON_INVOLEVE`: SR_NO_NEW
- **FK** `FK_INCIDENT_PERSON_INVOLEVE`: (INCIDENT_REGISTER_ID) -> HRD.INCIDENT_REGISTRATION(INCIDENT_REGISTER_ID) [disabled]
- **Triggers**: `INCIDENT_PERSON_INVOLEVE_DEL` (after delete), `INCIDENT_PERSON_INVOLEVE_INS` (before insert), `INCIDENT_PERSON_INVOLEVE_UPD` (before update)

## HRD.INCIDENT_PREDEFINED_CONCLUSION

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | VARCHAR2(20) | Y |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `INC_PREDEF_CON_DEL` (after delete), `INC_PREDEF_CON_INS` (before insert), `INC_PREDEF_CON_UPD` (before update)

## HRD.INCIDENT_REGISTRATION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| INCIDENT_REGISTER_DETAIL_ID | NUMBER generated always as identity | Y |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | N |  |
| INCIDENT_CATEGORY_ID | VARCHAR2(10) | N |  |
| INCIDENT_TYPE_ID | VARCHAR2(10) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_INCIDENT_REGISTRATION_DETAIL`: INCIDENT_REGISTER_DETAIL_ID
- **Triggers**: `INCIDENT_DETAIL_DEL` (after delete), `INCIDENT_DETAIL_INS` (before insert), `INCIDENT_DETAIL_UPD` (before update)

## HRD.INCIDENT_REPORTED_BY

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(8) | N |  |
| INCIDENT_REGISTER_ID | VARCHAR2(10) | Y |  |
| INCIDENT_REPORTED_ON | DATE | Y |  |
| INCIDENT_REPORTED_TYPE | CHAR(1) | Y |  |
| NAME | VARCHAR2(120) | Y |  |
| COMPANY_NAME | VARCHAR2(300) | Y |  |
| CONTACT_DETAIL | VARCHAR2(50) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_INCIDENT_REPORTED_BY`: SR_NO
- **FK** `FK_INCIDENT_REPORTED_BY`: (INCIDENT_REGISTER_ID) -> HRD.INCIDENT_REGISTRATION(INCIDENT_REGISTER_ID) [disabled]
- **Triggers**: `INCIDENT_REPORTED_BY_DEL` (after delete), `INCIDENT_REPORTED_BY_INS` (before insert), `INCIDENT_REPORTED_BY_UPD` (before update)

## HRD.INCREMENT_LETTER_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(182) | Y |  |
| JOINING_DATE | DATE | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| INCREMENT_DATE | DATE | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| FLAG_INCREMENT | CHAR(1) default 'N' | N |  |
| FLAG_ADJUSTMENT | CHAR(1) default 'N' | N |  |
| FLAG_DESIGNATION_CHANGE | CHAR(1) default 'N' | N |  |
| PREVIOUS_DESIGNATION | VARCHAR2(255) | Y |  |
| PREVIOUS_DESIGNATION_ID | VARCHAR2(7) | Y |  |
| TRANS_DATE | DATE default SYSDATE | Y |  |
| EFFECTIVE_FROM | DATE default SYSDATE | Y |  |
| LETTER_FROM | VARCHAR2(14) | Y |  |
| LETTER_FROM_NAME | VARCHAR2(255) | Y |  |
| LETTER_FROM_DESIGNATION | VARCHAR2(255) | Y |  |
| REPORT_NAME | VARCHAR2(60) | Y |  |
| REPORT_DATE | DATE default SYSDATE | Y |  |


## HRD.INC_PROPOSAL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_CODE | NUMBER(4) | N |  |
| PROPOSAL_NO | NUMBER(2) | N |  |
| MIN_SALARY | NUMBER(8) | Y |  |
| CUT_OFF_DATE | DATE | Y |  |
| PRORATE | CHAR(1) | Y |  |
| MIN_JOIN_DATE_PRORATE | DATE | Y |  |
| MAX_JOIN_DATE_PRORATE | DATE | Y |  |
| APPROVED | CHAR(1) default 'N' | Y |  |
| SEALED | CHAR(1) default 'N' | Y |  |
| INC_PRORATE | CHAR(1) default 'N' | Y |  |
| MIN_INC_DATE_PRORATE | DATE | Y |  |
| MAX_INC_DATE_PRORATE | DATE | Y |  |
| CUT_OFF_PROPOSAL_DATE | DATE | Y |  |
| PROPOSAL_STATUS | VARCHAR2(3) default '214' | Y | This col use to maintain current proposal '213' is open '214' is closed |
| PAYMENT_METHOD | NUMBER(3) | Y | THIS COLUMN CONTAINS DATA FROM HRD.INC_PAYMENT_METHODS |
| MERIT_INCREASE | NUMBER(3) | Y | THIS COLUMN CONTAINS DATA FROM HRD.INC_PAYMENT_METHODS |
| INFLATION_PROPOSAL_NO | NUMBER(2) | Y |  |

- **PK** `PK_INC_PROPOSAL`: YEAR_CODE, PROPOSAL_NO
- **Triggers**: `INC_PROPOSAL_DEL` (after delete), `INC_PROPOSAL_INS` (before insert), `INC_PROPOSAL_UPD` (before update)

## HRD.INFORMATION_COPY

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| CONTRACT_ID | VARCHAR2(6) | Y |  |
| EMPLOYEE_TYPE | VARCHAR2(1) | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| JOINING_DATE | DATE | Y |  |
| PROBATION_PERIOD_DAYS | NUMBER(3) | Y |  |
| LEAVING_DATE | DATE | Y |  |
| SERVICE_BOND_WITH_PREV_EMPL | NUMBER(1) | Y |  |
| PREPARE_TO_WORK_ANYWHERE_IN_PK | NUMBER(1) | Y |  |
| PREPARE_FOR_EXTENSIVE_TRAVEL | NUMBER(1) | Y |  |
| HAVE_DRIVING_LICENCE | NUMBER(1) | Y |  |
| EVER_DISMISSED_OR_ASK_TO_LEAVE | NUMBER(1) | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(6) | Y |  |
| MAY_SKMT_APPROACH_EMPLOYER_NOW | NUMBER(1) | Y |  |
| NATIONALITY | NUMBER(4) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| CONTRACT_TYPE_ID | VARCHAR2(3) | Y |  |
| REASON_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| PARAMEDICAL_STAFF | VARCHAR2(1) | Y |  |
| SHIFT_TYPE_ID | VARCHAR2(1) | Y |  |
| CONFIRMATION_DATE | DATE | Y |  |
| CONTRACT_START_DATE | DATE | Y |  |
| CONTRACT_END_DATE | DATE | Y |  |

- **Triggers**: `INFORMATION_COPY_DEL` (after delete), `INFORMATION_COPY_INS` (before insert), `INFORMATION_COPY_UPD` (before update)

## HRD.INTERVIEW_PANEL

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEDULE_ID | VARCHAR2(14) | N |  |
| SCHEDULE_DETAIL_ID | NUMBER | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |

- **PK** `INTERVIEW_PANEL_PK`: SCHEDULE_ID, SCHEDULE_DETAIL_ID, EMPLOYEE_CODE
- **Triggers**: `INTERVIEW_PANEL_DEL` (after delete), `INTERVIEW_PANEL_INS` (before insert), `INTERVIEW_PANEL_UPD` (before update)

## HRD.INTERVIEW_SCHEDULE_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEDULE_ID | VARCHAR2(14) | N |  |
| SCEDULE_DATE | DATE | Y |  |
| QUEUE_ID | NUMBER(11) | Y |  |
| JD_ID | NUMBER(7) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| CATEGORY_ID | NUMBER(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| HIRING_REQUEST_ID | NUMBER(7) | Y |  |

- **PK** `INTERVIEW_SCHEDULE_MASTER_PK`: SCHEDULE_ID
- **Triggers**: `INTERVIEW_SCHEDULE_MASTER_DEL` (after delete), `INTERVIEW_SCHEDULE_MASTER_INS` (before insert), `INTERVIEW_SCHEDULE_MASTER_UPD` (before update)

## HRD.INTERVIEW_SCHEDULE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEDULE_ID | VARCHAR2(14) | N |  |
| SCHEDULE_DETAIL_ID | NUMBER | N |  |
| CANDIDATE_ID | NUMBER(10) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| JOB_OFFER_STATUS | CHAR(1) | Y |  |
| JOB_OFFER_REAMKRS | VARCHAR2(4000) | Y |  |
| IS_SELECTED | CHAR(1) | Y |  |
| IS_EMIAL_SENT | CHAR(1) | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| HIRING_REQUEST_ID | NUMBER(7) | Y |  |

- **PK** `INTERVIEW_SCHEDULE_DETAIL_PK`: SCHEDULE_DETAIL_ID, SCHEDULE_ID
- **FK** `INTERVIEW_SCHEDULE_DETAIL_FK`: (SCHEDULE_ID) -> HRD.INTERVIEW_SCHEDULE_MASTER(SCHEDULE_ID)
- **Triggers**: `INTERVIEW_SCHEDULE_DETAIL_DEL` (after delete), `INTERVIEW_SCHEDULE_DETAIL_INS` (before insert), `INTERVIEW_SCHEDULE_DETAIL_UPD` (before update)

## HRD.JD_DETAIL_POSITION

| Column | Type | Null | Comment |
|---|---|---|---|
| JD_ID | NUMBER(7) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| POSITION_ID | VARCHAR2(6) | N |  |
| HIRING_REQUEST_ID | NUMBER(7) | N |  |
| QUEUE_ID | NUMBER(11) | N |  |

- **PK** `JD_DETAIL_POSITION_PK`: QUEUE_ID, POSITION_ID, HIRING_REQUEST_ID
- **Triggers**: `JD_DETAIL_POSITION_DEL` (after delete), `JD_DETAIL_POSITION_INS` (before insert), `JD_DETAIL_POSITION_UPD` (before update)

## HRD.JD_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| JD_ID | NUMBER(7) | N |  |
| JD_TITLE | VARCHAR2(255) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'N' | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| JD_GENERAL_CV | CHAR(1) default 'N' | Y | Only one JD for submission of General CV |

- **PK** `PK_JDID`: JD_ID
- **UK** `UK_JD`: DEPARTMENT_ID, DESIGNATION_ID, JD_TITLE, LOCATION_ID
- **FK** `FK_PK_JDID_01`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **FK** `FK_PK_JDID_02`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **Triggers**: `JD_MASTER_DEL` (after delete), `JD_MASTER_INS` (before insert), `JD_MASTER_UPD` (before update)

## HRD.JD_DETAIL_WEB

| Column | Type | Null | Comment |
|---|---|---|---|
| DISPLAY_NO | NUMBER(2) | N |  |
| HEADING | VARCHAR2(255) | Y |  |
| FONT_SIZE | NUMBER(2) default 12 | N |  |
| FONT_BOLD | CHAR(1) default 'N' | N |  |
| DETAIL | VARCHAR2(4000) | Y |  |
| JD_ID | NUMBER(7) | N |  |

- **PK** `PK_JD_DP_NO_WEB`: DISPLAY_NO, JD_ID
- **FK** `FK_JD_ID_WEB`: (JD_ID) -> HRD.JD_MASTER(JD_ID) [disabled]
- **Triggers**: `JD_DETAIL_WEB_DEL` (after delete), `JD_DETAIL_WEB_INS` (before insert), `JD_DETAIL_WEB_UPD` (before update)

## HRD.JD_SHORTLIST_CV

| Column | Type | Null | Comment |
|---|---|---|---|
| CANDIDATE_ID | NUMBER(10) | N |  |
| QUEUE_ID | NUMBER(11) | Y |  |
| JD_ID | NUMBER(7) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| HIRING_REQUEST_ID | NUMBER(7) | Y |  |
| STATUS | CHAR(1) | Y | 'N=New' 'S=Shortlisted' 'R=Rejected''H=HOD Review','P' |
| SCORE | NUMBER(5,2) | Y | Screening/Evaluation Score |
| STAGE | CHAR(1) | Y | 'I' INTERVIEW , 'F' FINAL,'S' SELECTED |
| SHORTLIST_BY | VARCHAR2(14) | Y |  |
| SHORTLIST_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| IS_SELECTED | CHAR(1) | Y |  |
| IS_EMIAL_SENT | CHAR(1) | Y |  |
| JOB_OFFER_STATUS | CHAR(1) | Y | 'A''ACCEPTED', 'R''REJECTED','H','HOLD' |
| JOB_OFFER_REAMKRS | VARCHAR2(2000) | Y |  |
| APPLICANT_NAME | VARCHAR2(1000) | Y |  |
| CATEGORY_ID | NUMBER(3) | Y |  |
| CITY | VARCHAR2(200) | Y |  |
| EMAIL | VARCHAR2(500) | Y |  |
| CNIC | VARCHAR2(50) | Y |  |
| PHONE_NO | VARCHAR2(100) | Y |  |
| IS_SHORTLIST | CHAR(1) default 'S' | Y | 'S' 'SHORT_LIST' |
| SCHEDULE_DATE | DATE | Y |  |
| IS_SCHEDULED | CHAR(1) default 'I' | Y | 'I' IN PROCESS , 'S' 'SCHEDULED' |
| IS_SHORTLISTED_BY_DEPT | CHAR(1) | Y |  |
| SHORTLIST_DATE_DEPT | DATE | Y |  |
| SHORTLIST_DEPT_BY | VARCHAR2(14) | Y |  |
| IS_FORWARDED_TO_HR | CHAR(1) | Y |  |
| IS_FORWARDED_TO_DEPT | CHAR(1) | Y |  |
| IS_REJECTED | CHAR(1) | Y |  |
| IS_HR_ACKNOWLEDGE | CHAR(1) | Y |  |
| HR_ACKNOWLEDGE_BY | VARCHAR2(14) | Y |  |

- **PK** `JD_SHORTLIST_CV`: CANDIDATE_ID
- **Triggers**: `JD_SHORTLIST_CV_DEL` (after delete), `JD_SHORTLIST_CV_INS` (before insert), `JD_SHORTLIST_CV_UPD` (before update), `PT_CV_SHORTLIST_HR_QUEUE` (after update), `PT_CV_SHORT_DEPARTMENT_WISE` (after insert)

## HRD.JOB_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| DETAIL | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'N' | N |  |
| CATEGORY_TYPE | CHAR(1) default 'N' | Y | 'M' for Medical and 'N' for Non-Medical |
| IMAGE | BLOB | Y |  |
| ORDER_BY | NUMBER(2) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| GENERAL_CV | CHAR(1) default 'N' | Y | Only one category for submission of General CV |
| CATEGORY_PAGE | VARCHAR2(255) | Y | To use as CONSTANT, if specific page of Category exists |
| PARENT_CATEGORY_ID | NUMBER(3) | Y | PARENT_CATEGORY_ID IS THE PARENT COLUMN FROM CATEGORY_ID |
| WEB_PAGE_ID | VARCHAR2(50) | Y |  |
| WEB_PAGE_NAME | VARCHAR2(200) | Y |  |
| SHOW_IN_LOV | CHAR(1) default 'N' | Y |  |

- **PK** `PK_CAT_ID`: CATEGORY_ID
- **FK** `DOCUMENT_ID_FK`: (DOCUMENT_ID) -> LOB.DOCUMENTS_STORE(DOCUMENT_ID)
- **Triggers**: `JOB_CATEGORY_DEL` (after delete), `JOB_CATEGORY_INS` (before insert), `JOB_CATEGORY_UPD` (before update)

## HRD.JOB_DAY_SCHEDULE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| DAY_ID | NUMBER | Y |  |
| DAY_DESC | VARCHAR2(20) | Y |  |
| JOB_TIME | VARCHAR2(30) | Y |  |
| START_TIME | VARCHAR2(30) | Y |  |
| END_TIME | VARCHAR2(30) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `JOB_DAY_SCHEDULE_SETUP_DEL` (after delete), `JOB_DAY_SCHEDULE_SETUP_INS` (before insert), `JOB_DAY_SCHEDULE_SETUP_UPD` (before update)

## HRD.JOB_POSTING_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER(11) | N |  |
| CATEGORY_ID | NUMBER(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| NO_OF_POSITIONS | NUMBER(3) | Y |  |
| JD_ID | NUMBER(7) | Y |  |
| WEB_TITLE | VARCHAR2(255) | Y |  |
| PUBLISH_DATE | DATE | Y |  |
| EXPIRY_DATE | DATE | Y |  |
| HOLD | CHAR(1) default 'N' | N |  |
| HOLD_REMARKS | VARCHAR2(1000) | Y |  |
| JD_TITLE | VARCHAR2(255) | Y |  |
| JD_DESCRIPTION | VARCHAR2(4000) | Y |  |
| JD_POST | CHAR(1) default 'N' | Y |  |

- **PK** `PK_QUEUE_ID`: QUEUE_ID
- **FK** `FK_CAT_ID_QUE`: (CATEGORY_ID) -> HRD.JOB_CATEGORY(CATEGORY_ID) [disabled]
- **Triggers**: `JOB_POSTING_QUEUE_DEL` (after delete), `JOB_POSTING_QUEUE_INS` (before insert), `JOB_POSTING_QUEUE_UPD` (before update)

## HRD.JOINERS_LEAVERS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT | VARCHAR2(60) | Y |  |
| MONTH | DATE | Y |  |
| JOINERS | NUMBER(4) | Y |  |
| LEAVERS | NUMBER(4) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |

- **Triggers**: `JOINERS_LEAVERS_DEL` (after delete), `JOINERS_LEAVERS_INS` (before insert), `JOINERS_LEAVERS_UPD` (before update)

## HRD.LANGUAGES_KNOWN

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| SPEAK | NUMBER(1) | Y |  |
| READ | NUMBER(1) | Y |  |
| WRITE | NUMBER(1) | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |

- **PK** `PK_LANGUAGES_KNOWN`: MRNO, LANGUAGE_ID
- **Triggers**: `LANGUAGES_KNOWN_DEL` (after delete), `LANGUAGES_KNOWN_INS` (before insert), `LANGUAGES_KNOWN_UPD` (before update)

## HRD.LAPSED_LEAVES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| MONTH_START_DATE | DATE | N |  |
| MONTH_END_DATE | DATE | N |  |
| CURRENT_YEAR | NUMBER(5,2) | N |  |
| LAST_YEAR_BALANCE | NUMBER(5,2) | N |  |
| LEAVE_AVAILED | NUMBER(5,2) default 0 | N |  |
| NO_LAPSED | NUMBER(5,2) default 0 | N |  |
| NO_UTILIZED | NUMBER(5,2) default 0 | N |  |
| NO_COMPENSATED | NUMBER(5,2) default 0 | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Ref # leave_type (leave_type_id) |

- **PK** `PK_LAPSED_LEAVES`: MRNO, MONTH_START_DATE, LEAVE_TYPE_ID
- **FK** `FK_LEAVE_TYPE_ID`: (LEAVE_TYPE_ID) -> HRD.LEAVE_TYPE(LEAVE_TYPE_ID) [disabled]
- **FK** `FK_LEAVE_TYPE_ID_1`: (MRNO) -> HRD.INFORMATION(MRNO)
- **CHECK** `CK_LAPSED_LEAVES_001`: MONTH_START_DATE = TRUNC(MONTH_START_DATE)
- **CHECK** `CK_LAPSED_LEAVES_002`: MONTH_END_DATE = TRUNC(MONTH_END_DATE)
- **Triggers**: `LAPSED_LEAVES_DEL` (after delete), `LAPSED_LEAVES_INS` (before insert), `LAPSED_LEAVES_UPD` (before update)

## HRD.LEAVE_APPLICATION_HISTORY
Store leave tracking information in accordance with employee and leave type

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | N | Store employee code who will apply for leave |
| EMP_LEAVE_SERIAL_NO | NUMBER(5) | N | Store employee leave serial number |
| APPLICANT_SERIAL_NO | NUMBER(5) | N | Store leave tracking number as it is forward to different levels for approval/rejection purpose |
| FORWARD_TO | VARCHAR2(14) | Y | Store employee code of whom leave will be passed on /forward to |
| ACTING_FOR | VARCHAR2(14) | Y | Store employee code who will work in absence of actual employee |
| REMARKS | VARCHAR2(1000) | Y | Store leave reason |
| DECIDING_USER_ID | VARCHAR2(14) | Y | Store employee code who change status of leave as Approved or Recommended |
| DECIDING_TERMINAL | VARCHAR2(30) | Y | Store terminal of employee who change status of leave as Approved or Recommended Ex/ SKM -0366 |
| DECIDING_TRN_DATE | DATE | Y | Store latest date and time on which deciding user make transaction |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y | Store leave authority level ID of employee to whom leave is passed on/ forward to Ex 001 for Recommend |
| REQUESTING_USER_ID | VARCHAR2(14) | Y | Store employee code who apply for leave |
| REQUESTING_TERMINAL | VARCHAR2(30) | Y | Store terminal from where leave application request is entered |
| REQUESTING_TRN_DATE | DATE | Y | Store date and time on which user made request for leave |
| EHC_QUEUE | CHAR(1) default 'N' | N | Store either Y or N to indicate leave is passed on to employee health clinic or not |
| HR_REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_LEAVE_APPLICATION_HISTORY`: APPLICANT_MRNO, EMP_LEAVE_SERIAL_NO, APPLICANT_SERIAL_NO
- **CHECK** `CK_LEAVE_APPLICATION_HISTORY_1`: EHC_QUEUE IN ('Y','N')
- **Triggers**: `LEAVE_APPLICATION_HISTORY_DEL` (after delete), `LEAVE_APPLICATION_HISTORY_INS` (before insert), `LEAVE_APPLICATION_HISTORY_UPD` (before update)

## HRD.LEAVE_APPLICATION_QUEUE
Store status of leave queues for approval  or rejection purpose

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | N | Store employee code who will apply for leave |
| EMP_LEAVE_SERIAL_NO | NUMBER(5) | N | Store employee leave serial number |
| FORWARD_TO | VARCHAR2(14) | Y | Store employee code of whom leave will be passed on /forward to |
| ACTING_FOR | VARCHAR2(14) | Y | Store employee code who will work in absence of actual employee |
| REMARKS | VARCHAR2(1000) | Y | Store leave reason |
| AUTHORITY_LEVEL_ID | CHAR(3) | Y | Store leave authority level ID of employee to whom leave is passed on/ forward to Ex 001 for Recommend |
| REQUESTING_USER_ID | VARCHAR2(14) | Y | Store employee code who apply for leave |
| REQUESTING_TERMINAL | VARCHAR2(30) | Y | Store terminal from where leave application request is entered |
| REQUESTING_TRN_DATE | DATE | Y | Store date and time on which user made request for leave |
| EHC_QUEUE | CHAR(1) default 'N' | N | Store either Y or N to indicate leave is passed on to employee health clinic or not |
| LEAVE_HIERARCHY_AUTH_ID | NUMBER | Y |  |
| HR_REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_LEAVE_APPLICATION_QUEUE`: APPLICANT_MRNO, EMP_LEAVE_SERIAL_NO
- **CHECK** `CK_LEAVE_APPLICATION_QUEUE_1`: EHC_QUEUE IN ('Y','N')
- **Triggers**: `LEAVE_APPLICATION_PT_DEL` (after delete), `LEAVE_APPLICATION_PT_INS` (before insert), `LEAVE_APPLICATION_PT_UPD` (after update), `LEAVE_APPLICATION_QUEUE_DEL` (after delete), `LEAVE_APPLICATION_QUEUE_INS` (before insert), `LEAVE_APPLICATION_QUEUE_UPD` (before update)

## HRD.LEAVE_APPROVAL_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_HIST_ID | NUMBER(10) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| DECISION | VARCHAR2(50) | Y |  |
| DECISION_BY | VARCHAR2(14) | Y |  |
| DECISION_DATE | DATE | Y |  |
| REQUEST_ID | NUMBER(5) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |


## HRD.LEAVE_AUTHORY
Store information regarding leave authorities

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_AUTHORY_ID | CHAR(3) | N | Store leave authority id Ex 001, 002 |
| DESCRIPTION | VARCHAR2(60) | Y | Store description of leave authority id Ex Recommend for 001 |
| ACTIVE | CHAR(1) | Y | Store either Y or N to indicate leave authority status as active or inactive respectively |

- **PK** `PK_LEAVE_AUTHORY`: LEAVE_AUTHORY_ID

## HRD.LEAVE_CHECKLIST_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER(3) | N |  |
| DESCRIPTION | CHAR(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_LEAVE_CHECKLIST_PARAM`: PARAM_ID

## HRD.LEAVE_DAYS
Store information of leave according to days

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| VERIFIED | VARCHAR2(1) default 'N' | Y |  |
| SHORT_LEAVE | VARCHAR2(1) default 'N' | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SALARY_MONTH | VARCHAR2(6) | Y |  |
| UNPAID_STATUS | CHAR(1) default 'N' | N | N  -- New Row ( No month Dates), D  -- Deducted from Salary   (Month Dates will be populated), U  -- Considered as Unpaid  Salary for the day not Paid (Month Dates will be populated) |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| ORIGINAL_LEAVE_DATE | DATE | N |  |

- **PK** `PK_LEAVE_DAYS`: MRNO, LEAVE_DATE
- **CHECK** `CHK_UNPAID_STATUS`: UNPAID_STATUS IN ('N','D','U')
- **Triggers**: `LEAVE_DAYS_DEL` (after delete), `LEAVE_DAYS_INS` (before insert), `LEAVE_DAYS_UPD` (before update)

## HRD.LEAVE_DAYS_CANCELLED

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| CANCELLATION_DATE | DATE | Y |  |
| SHORT_LEAVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_LEAVE_DAYS_CANCELLED`: MRNO, SERIAL_NO, LEAVE_DATE
- **Triggers**: `LEAVE_DAYS_CANCELLED_DEL` (after delete), `LEAVE_DAYS_CANCELLED_INS` (before insert), `LEAVE_DAYS_CANCELLED_UPD` (before update)

## HRD.LEAVE_QUEUE_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ORDER_BY | NUMBER | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| EHC_QUEUE | CHAR(1) | Y |  |
| HIERARCHY_TYPE | CHAR(1) | Y |  |
| EHC_HEAD | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| GREATER_THEN_90 | CHAR(1) default 'N' | Y |  |

- **Triggers**: `LEAVE_QUEUE_HIERARCHY_DEL` (after delete), `LEAVE_QUEUE_HIERARCHY_INS` (before insert), `LEAVE_QUEUE_HIERARCHY_UPD` (before update)

## HRD.LEAVE_TYPE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| ENTRY_TYPE | VARCHAR2(3) | N | Entry type can be 'EMP' if employee is using otherwise 'HR' |
| NORMAL_PERIOD | NUMBER(3) | Y | Normal period in which leave can be availed; value entered in this column will be considered in months. |
| MIN_GAP | NUMBER(3) | Y | Minimum gap required to avail leave; value entered in this column will be considered in months. |
| CY_ALLOWED | NUMBER(3) default 0 | Y | CY = Current Year |
| MINS_ONE_CTO | NUMBER(5) | Y | Minutes that will be considered for claiming one day CTO |
| MINS_TWO_CTO | NUMBER(5) | Y | Minutes that will be considered for claiming two day CTO |
| CANCEL_ALLOWED | CHAR(1) | Y |  |

- **FK** `FK_LEAVE_TYPE`: (LEAVE_TYPE_ID) -> HRD.LEAVE_TYPE(LEAVE_TYPE_ID) [disabled]

## HRD.LETTER_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_NAME | VARCHAR2(100) | Y |  |

- **Triggers**: `LETTER_CONSTANT_DEL` (after delete), `LETTER_CONSTANT_INS` (before insert), `LETTER_CONSTANT_UPD` (before update)

## HRD.LETTER_TEMPLATE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_TYPE_ID | VARCHAR2(7) | N |  |
| LETTER_SUBJECT | NVARCHAR2(2000) | Y |  |
| LETTER_HEADER | NVARCHAR2(2000) | Y |  |
| LETTER_FOOTER | NVARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LETTER_LOCK | CHAR(1) | Y |  |
| LETTER_BODY | CLOB | Y |  |

- **PK** `PK_LETTER_TEMPLATE_DETAIL_1`: TEMPLATE_TYPE_ID
- **CHECK** `CHK_LETTER_TEMPLATE_DETAIL_1`: ACTIVE IN ('Y','N')
- **CHECK** `CHK_LETTER_TEMPLATE_DETAIL_2`: LETTER_LOCK IN ('Y','N')
- **Triggers**: `LETTER_TEMPLATE_DETAIL_DEL` (after delete), `LETTER_TEMPLATE_DETAIL_INS` (before insert), `LETTER_TEMPLATE_DETAIL_UPD` (before update)

## HRD.LETTER_TEMPLATE_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| PARAM_VALUE | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| TEMPLATE_TYPE_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_PARAM_ID`: PARAM_ID
- **Triggers**: `LETTER_TEMPLATE_PARAM_DEL` (after delete), `LETTER_TEMPLATE_PARAM_INS` (before insert), `LETTER_TEMPLATE_PARAM_UPD` (before update)

## HRD.LFA_EMAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(100) | Y |  |
| DESIGNATION | VARCHAR2(80) | Y |  |
| DEPARTMENT | VARCHAR2(80) | Y |  |
| YEAR_START | DATE | Y |  |
| YEAR_END | DATE | Y |  |
| LFA_DUE_START | DATE | Y |  |
| LFA_DUE_END | DATE | Y |  |
| ACTUAL_LEAVE_START | DATE | Y |  |
| ACTUAL_LEAVE_END | DATE | Y |  |
| VOUCHER_TYPE | VARCHAR2(80) | Y |  |
| VOUCHER_NUMBER | VARCHAR2(80) | Y |  |
| GROSS_SALARY | NUMBER(20,2) | Y |  |
| LFA_AMOUNT | NUMBER(20,2) | Y |  |
| PAYMENT_DATE | DATE | Y |  |

- **Triggers**: `LFA_EMAIL_DEL` (after delete), `LFA_EMAIL_INS` (before insert), `LFA_EMAIL_UPD` (before update)

## HRD.LFA_EMAIL_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(100) | Y |  |
| DESIGNATION | VARCHAR2(80) | Y |  |
| DEPARTMENT | VARCHAR2(80) | Y |  |
| YEAR_START | DATE | Y |  |
| YEAR_END | DATE | Y |  |
| LFA_DUE_START | DATE | Y |  |
| LFA_DUE_END | DATE | Y |  |
| ACTUAL_LEAVE_START | DATE | Y |  |
| ACTUAL_LEAVE_END | DATE | Y |  |
| VOUCHER_TYPE | VARCHAR2(80) | Y |  |
| VOUCHER_NUMBER | VARCHAR2(80) | Y |  |
| GROSS_SALARY | NUMBER(20,2) | Y |  |
| LFA_AMOUNT | NUMBER(20,2) | Y |  |
| PAYMENT_DATE | DATE | Y |  |

- **Triggers**: `LFA_EMAIL_HISTORY_DEL` (after delete), `LFA_EMAIL_HISTORY_INS` (before insert), `LFA_EMAIL_HISTORY_UPD` (before update)

## HRD.LOC_WISE_CLEARANCE_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUPID | VARCHAR2(10) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| EVENT_DESCRIPTION | VARCHAR2(1000) | Y |  |
| CLEARANCE_TYPE | CHAR(1) | Y |  |

- **PK** `LOC_WISE_CLEARANCE_GROUP_PK`: GROUPID, LOCATION_ID
- **UK** `LOC_WISE_CLEARANCE_GROUP_UK`: GROUPID, LOCATION_ID, CLEARANCE_TYPE
- **Triggers**: `LOC_WISE_CLEARANCE_GROUP_DEL` (after delete), `LOC_WISE_CLEARANCE_GROUP_INS` (before insert), `LOC_WISE_CLEARANCE_GROUP_UPD` (before update)

## HRD.MANUAL_ATTENDANCE_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| DAYS_PERFORMED | NUMBER(5) | Y |  |
| ADDITIONAL_WORKING_DAYS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(5) | Y |  |
| ACTUAL_SHIFT_MINUTES | NUMBER(8) | Y |  |
| PERFORMED_MINUTES | NUMBER(8) | Y |  |
| APPROVED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| LEAVE_DAYS | NUMBER(4) | Y |  |
| NIGHTS | NUMBER(4) | Y |  |
| ON_CALL_DAYS | NUMBER(4) | Y |  |
| ON_CALL_ALLOWANCE | NUMBER(12,2) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SALARY_START_DATE | DATE | Y | This column contain value from definitions.location_wise_month (pay_start_date) for salary purpose |
| SALARY_END_DATE | DATE | Y | This column contain value from definitions.location_wise_month (pay_end_date) for salary purpose |

- **PK** `PK_MANUAL_ATTENDANCE_SUMMARY`: MRNO, START_DATE, END_DATE
- **Triggers**: `MANUAL_ATTENDANCE_SUMMARY_DEL` (after delete), `MANUAL_ATTENDANCE_SUMMARY_INS` (before insert), `MANUAL_ATTENDANCE_SUMMARY_UPD` (before update)

## HRD.MEMBER_BUSINESS_CLUBS

| Column | Type | Null | Comment |
|---|---|---|---|
| BUSINESS_CLUB_ID | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |

- **PK** `PK_MEMBER_BUSINESS_CLUBS`: BUSINESS_CLUB_ID, MRNO
- **Triggers**: `MEMBER_BUSINESS_CLUBS_DEL` (after delete), `MEMBER_BUSINESS_CLUBS_INS` (before insert), `MEMBER_BUSINESS_CLUBS_UPD` (before update)

## HRD.MISSING_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| REP_DATE | DATE | Y |  |

- **Triggers**: `MISSING_EMPLOYEES_DEL` (after delete), `MISSING_EMPLOYEES_INS` (before insert), `MISSING_EMPLOYEES_UPD` (before update)

## HRD.MISSING_GRADES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| REASON | VARCHAR2(300) | Y |  |


## HRD.MONTHLY_DEPARTMENT_OVERTIME

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACCEPTED | VARCHAR2(1) | Y |  |

- **PK** `PK_MONTHY_DEPARTMENT_OVERTIME`: PROCESS_ID, DEPARTMENT_ID
- **Triggers**: `MONTHLY_DEPARTMENT_OVERTIME_DEL` (after delete), `MONTHLY_DEPARTMENT_OVERTIME_INS` (before insert), `MONTHLY_DEPARTMENT_OVERTIME_UPD` (before update), `MONTHLY_DEPT_OVERTIME_DEL` (after delete), `MONTHLY_DEPT_OVERTIME_INS` (before insert), `MONTHLY_DEPT_OVERTIME_UPD` (before update)

## HRD.MONTHLY_EARNED_LEAVE_EXCLUDING

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| EARNED_LEAVE_JOB_DATE | DATE | N |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| LEAVE_TYPE | VARCHAR2(3) | Y |  |

- **PK** `MONTHLY_EARNED_LEAVE_EXCLUDING_PK`: MRNO, EARNED_LEAVE_JOB_DATE
- **Triggers**: `MON_EAR_LEAVE_EXCLUDING_DEL` (after delete), `MON_EAR_LEAVE_EXCLUDING_INS` (before insert), `MON_EAR_LEAVE_EXCLUDING_UPD` (before update)

## HRD.MONTHLY_LAPSED_LEAVES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| MONTH_START_DATE | DATE | Y |  |
| MONTH_END_DATE | DATE | N |  |
| CURRENT_YEAR | NUMBER(5,2) | N |  |
| LAST_YEAR_BALANCE | NUMBER(5,2) | N |  |
| LEAVE_AVAILED | NUMBER(5,2) | N |  |
| NO_LAPSED | NUMBER(5,2) | N |  |
| NO_UTILIZED | NUMBER(5,2) | N |  |
| NO_COMPENSATED | NUMBER(5,2) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| ENTRY_MONTH | DATE | Y |  |


## HRD.MONTHLY_LEAVE_DATE_LEAVE_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| VERIFIED | VARCHAR2(1) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SALARY_MONTH | VARCHAR2(6) | Y |  |
| UNPAID_STATUS | CHAR(1) | N |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| ORIGINAL_LEAVE_DATE | DATE | N |  |
| ENTRY_MONTH | DATE | Y |  |


## HRD.MONTHLY_LEAVE_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_DATE | DATE | N |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| VERIFIED | VARCHAR2(1) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SALARY_MONTH | VARCHAR2(6) | Y |  |
| UNPAID_STATUS | CHAR(1) | N |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| ORIGINAL_LEAVE_DATE | DATE | N |  |
| ENTRY_MONTH | DATE | Y |  |


## HRD.MONTH_WISE_EMP_LEAVE_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH | DATE | N |  |
| YEAR_START | DATE | Y |  |
| YEAR_END | DATE | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| CURRENT_YEAR | NUMBER(6,2) | Y |  |
| LAST_YEAR_BALANCE | NUMBER(7,2) | Y |  |
| TOTAL_LEAVES | NUMBER(7,2) | Y |  |
| LEAVE_AVAILED | NUMBER(7,2) | Y |  |
| BALANCE | NUMBER | Y |  |
| NO_CARRIED_FORWARD | NUMBER(7,2) | Y |  |
| TRANSACTION_DATE | DATE | Y |  |
| LAPSED_LEAVES | NUMBER(7,2) | Y |  |
| ADJUSTED_LEAVES | NUMBER(7,2) | Y |  |

- **PK** `MONTH_WISE_EMP_LEAVE_SUMMARY_PK`: MONTH, MRNO, LEAVE_TYPE_ID
- **Triggers**: `MON_WISE_EMP_LEAVE_SUMMARY_DEL` (after delete), `MON_WISE_EMP_LEAVE_SUMMARY_INS` (before insert), `MON_WISE_EMP_LEAVE_SUMMARY_UPD` (after update)

## HRD.NET_PERFORMANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| FIN_YEAR | VARCHAR2(6) | N |  |
| FPA | NUMBER(12,3) | Y |  |
| FPB | NUMBER(12,3) | Y |  |
| FPA_W | NUMBER(12,3) | Y |  |
| FPB_W | NUMBER(12,3) | Y |  |
| NP | NUMBER(12,3) | Y |  |

- **PK** `PK_NET_PERFORMANCE`: MRNO, FIN_YEAR

## HRD.NEW_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |


## HRD.NEW_SAL

| Column | Type | Null | Comment |
|---|---|---|---|
| CODE | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(200) | Y |  |
| DES | VARCHAR2(200) | Y |  |
| CUR | NUMBER(12) | Y |  |
| NEW_SAL | NUMBER(12) | Y |  |


## HRD.NO_CARD_SWIPE_DECISION

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTENDANCE_DECISION_ID | NUMBER(3) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| NO_CARD_SWIPE_FOUND_DATE | DATE | N |  |
| IS_EMAIL_SENT | CHAR(1) default 'N' | Y |  |
| DECISION_DATE | DATE | Y |  |

- **PK** `PK_NO_CARD_SWIPE_DECISION`: MRNO, NO_CARD_SWIPE_FOUND_DATE
- **FK** `FK_NO_CARD_SWIPE_DECISION`: (ATTENDANCE_DECISION_ID) -> HRD.DEF_ATTENDANCE_DECISION(ATTENDANCE_DECISION_ID) [disabled]
- **CHECK** `CHK1_IS_EMAIL_SENT`: IS_EMAIL_SENT IN ('Y','N')
- **Triggers**: `NO_CARD_SWIPE_DECISION_DEL` (after delete), `NO_CARD_SWIPE_DECISION_INS` (before insert), `NO_CARD_SWIPE_DECISION_UPD` (before update)

## HRD.NO_CARD_SWIPE_DECISION_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTENDANCE_DECISION_ID | NUMBER(3) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| NO_CARD_SWIPE_FOUND_DATE | DATE | Y |  |
| IS_EMAIL_SENT | CHAR(1) | Y |  |
| DECISION_DATE | DATE | Y |  |
| SYSTEM_REMARKS | VARCHAR2(500) | Y |  |
| SYSTEM_DECISION_DATE | DATE | Y |  |


## HRD.NURSING_SUP_HIERARCHY_SUMMARY

| Column | Type | Null | Comment |
|---|---|---|---|
| SUPERVISOR_MRNO | VARCHAR2(14) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACCME | NUMBER | Y |  |
| CURRENT_YEAR | VARCHAR2(50) | N |  |
| CURRENT_MONTH_HOUR | NUMBER | Y |  |
| MONTH_START | DATE | Y |  |
| MONTH_END | DATE | Y |  |
| MONTH_NAME | VARCHAR2(50) | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `NURSING_SUP_HIERARCHY_SUMMARY_PK`: MRNO, CURRENT_YEAR, MONTH_NAME, DEPARTMENT_ID, SUPERVISOR_MRNO
- **Triggers**: `NUR_SUP_HIERARCHY_SUM_DEL` (after delete), `NUR_SUP_HIERARCHY_SUM_INS` (before insert), `NUR_SUP_HIERARCHY_SUM_UPD` (before update)

## HRD.NURSING_DOCUMENT_ATTACHEMNT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| SUPERVISOR_MRNO | VARCHAR2(14) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| CURRENT_YEAR | VARCHAR2(50) | N |  |
| MONTH_NAME | VARCHAR2(50) | N |  |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHED_DATE | DATE | Y |  |

- **PK** `NURSING_DOCUMENT_ATTACHEMNT_PK`: SR_NO, SUPERVISOR_MRNO, MRNO, DEPARTMENT_ID, CURRENT_YEAR, MONTH_NAME
- **FK** `NURSING_DOCUMENT_ATTACHMENT_FK`: (MRNO, CURRENT_YEAR, MONTH_NAME, DEPARTMENT_ID, SUPERVISOR_MRNO) -> HRD.NURSING_SUP_HIERARCHY_SUMMARY(MRNO, CURRENT_YEAR, MONTH_NAME, DEPARTMENT_ID, SUPERVISOR_MRNO)
- **Triggers**: `NURSING_DOC_ATTACHEMNT_DEL` (after delete), `NURSING_DOC_ATTACHEMNT_INS` (before insert), `NURSING_DOC_ATTACHEMNT_UPD` (before update)

## HRD.NURSING_SUP_HIERARCHY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SUPERVISOR_MRNO | VARCHAR2(14) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `NUR_SUP_HIERARCHY_DETAIL_DEL` (after delete), `NUR_SUP_HIERARCHY_DETAIL_INS` (before insert), `NUR_SUP_HIERARCHY_DETAIL_UPD` (before update)

## HRD.NURSING_SUP_HIERARCHY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SUPERVISOR_MRNO | VARCHAR2(14) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `NURSING_SUP_HIERARCHY_MASTER_PK`: SUPERVISOR_MRNO, DEPARTMENT_ID
- **Triggers**: `NUR_SUP_HIERARCHY_MASTER_DEL` (after delete), `NUR_SUP_HIERARCHY_MASTER_INS` (before insert), `NUR_SUP_HIERARCHY_MASTER_UPD` (before update)

## HRD.OBJECT_WISE_COLUMNS

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(12) | N |  |
| BLOCK_NAME | VARCHAR2(100) | N |  |
| COLUMN_NAME | VARCHAR2(50) | N |  |
| DISPLAY_NAME | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_OBJECT_WISE_COLUMNS`: OBJECT_CODE, BLOCK_NAME, COLUMN_NAME
- **Triggers**: `OBJECT_WISE_COLUMNS_DEL` (after delete), `OBJECT_WISE_COLUMNS_INS` (before insert), `OBJECT_WISE_COLUMNS_UPD` (before update)

## HRD.ONCALL_SHIFT_ATTENDANCE_TMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ROSTER_DATE | DATE | Y |  |
| ONCALL_ROLE | VARCHAR2(9) | Y |  |
| SHIFT_SOURCE | VARCHAR2(23) | Y |  |
| CREDITED_HOURS | NUMBER | Y |  |
| ACTUAL_SWIPE_HOURS | NUMBER | Y |  |
| SHIFT_START_DT | DATE | Y |  |
| SHIFT_END_DT | DATE | Y |  |
| SWIPE_COUNT | NUMBER | Y |  |
| PRESENCE_STATUS | CHAR(1) | Y |  |
| SCHEDULED_HOURS | NUMBER | Y |  |
| MIN_SWIPE_DT | DATE | Y |  |
| MAX_SWIPE_DT | DATE | Y |  |
| SOURCE_COLUMN | VARCHAR2(9) | Y |  |
| ROSTER_TYPE_ID | NUMBER | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| ROSTER_BATCH_GROUP_ID | VARCHAR2(6) | Y |  |
| ROSTER_BATCH_ID | VARCHAR2(6) | Y |  |
| POST_CALL | CHAR(1) | Y |  |
| SHIFT_KEY | VARCHAR2(35) | Y |  |
| SHIFT_LOWER_BOUND | DATE | Y |  |
| SHIFT_UPPER_BOUND | DATE | Y |  |
| ROSTER_END_DATE | DATE | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |

- **Triggers**: `SHIFT_ATTENDANCE_TMP_DEL` (after delete), `SHIFT_ATTENDANCE_TMP_INS` (before insert), `SHIFT_ATTENDANCE_TMP_UPD` (before update)

## HRD.ONLINE_ABSTRACT_SUBMISSION
This table contains information of online abstract submitters, submitted via Website.

| Column | Type | Null | Comment |
|---|---|---|---|
| SYMPOSIUM_TYPE_ID | VARCHAR2(3) | N |  |
| ABSTRACT_ID | VARCHAR2(6) default '0001' | N | Format = YYxxx First 2 digit Year Rest of 4 digit counter |
| EMAIL_ADDRESS | VARCHAR2(100) | N | Email Address of abstruct submitter |
| CONTACT_NO | VARCHAR2(50) | N |  |
| TITLE | VARCHAR2(4000) | Y | Title of Abstract |
| OBJECTIVE | VARCHAR2(4000) | Y | Objective of Abstract |
| METHOD | VARCHAR2(4000) | Y | Method of Abstract |
| RESULTS | VARCHAR2(4000) | Y | Results of Abstract |
| CONCLUSION | VARCHAR2(4000) | Y | Conclusion of Abstract |
| AUTHORS | VARCHAR2(4000) | Y | Authors list of Abstract |
| INSTITUTE | VARCHAR2(4000) | Y | Institute of presenter |
| BODY_SYSTEM_ID | NUMBER(3) | N | Part of human body on which research was conducted. |
| OTHER_BODY_SYSTEM | VARCHAR2(150) | Y |  |
| SPECIALITY_ID | NUMBER(3) | N | Speciality of researcher |
| OTHER_SPECIALITY | VARCHAR2(150) | Y |  |
| MEDAL_SESSION | CHAR(1) default 'N' | N | Presenter has submitted abstract for Ahsan Rasheed Medal Session |
| FREE_PAPER | CHAR(1) default 'N' | N | Presenter has given Oral Presentation |
| POSTER_PRESENTATION | CHAR(1) default 'N' | N | Presenter has given research for Poster presentation. |
| SUBMISSION_DATE | DATE default SYSDATE | N |  |
| SUBMITTER_NAME | VARCHAR2(150) | Y | name of user submitting the application |
| POSTER_ALLOWED | CHAR(1) default 'N' | Y | N: Cannot submit poster Y:Allowed to upload poster |
| POSTER_PATH | VARCHAR2(1000) | Y | Network Path where poster will be saved |
| POSTER_NAME | VARCHAR2(500) | Y | File name of uploaded poster |
| LOV_KEYWORD_ID | VARCHAR2(255) | Y |  |
| OTHER_LOV_KEYWORD | VARCHAR2(255) | Y |  |

- **PK** `PK_ABSTRACT_SUBMISSION`: SYMPOSIUM_TYPE_ID, ABSTRACT_ID
- **FK** `FK_ABSTRACT_SUBMISSION_1`: (BODY_SYSTEM_ID) -> HRD.ABSTRACT_LOV_BODY_SYSTEM(BODY_SYSTEM_ID) [disabled]
- **FK** `FK_ABSTRACT_SUBMISSION_2`: (SPECIALITY_ID) -> HRD.ABSTRACT_LOV_SPECIALITY(SPECIALITY_ID) [disabled]
- **FK** `FK_ABSTRACT_SUBMISSION_3`: (SYMPOSIUM_TYPE_ID) -> HRD.DEF_SYMPOSIUM_TYPE(SYMPOSIUM_TYPE_ID)
- **Triggers**: `ONLINE_ABSTRACT_SUBMISSION_DEL` (after delete), `ONLINE_ABSTRACT_SUBMISSION_INS` (before insert), `ONLINE_ABSTRACT_SUBMISSION_UPD` (before update)

## HRD.ON_CALL_DUTY_ROSTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ROSTER_TYPE_ID | NUMBER(3) | N |  |
| ROSTER_DATE | DATE | N |  |
| ROSTER_PRIMARY_MRNO | VARCHAR2(14) | Y |  |
| ROSTER_COVERING_MRNO | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| START_TIME | DATE | Y |  |
| END_TIME | DATE | Y |  |
| ROSTER_LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `DUTY_ROSTER_PK_1`: ROSTER_TYPE_ID, ROSTER_DATE, LOCATION_ID, ROSTER_LOCATION_ID
- **Triggers**: `ON_CALL_DUTY_ROSTER_DEL` (after delete), `ON_CALL_DUTY_ROSTER_INS` (before insert), `ON_CALL_DUTY_ROSTER_INSERT` (before insert), `ON_CALL_DUTY_ROSTER_UPD` (before update)

## HRD.ON_CALL_DUTY_ROSTER_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ROSTER_TYPE_ID | NUMBER(3) | Y |  |
| ROSTER_ORGANIZER | VARCHAR2(14) | Y |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ORGANIZER_NAME | VARCHAR2(500) | Y |  |
| ALERT_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ORGANIZER_DESIGNATION_ID | VARCHAR2(6) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| ALERT_TYPE | CHAR(1) default 'T' | Y | T FOR TWO DAYS, O FOR ONE DAY, N FOR NEXT DAY |

- **Triggers**: `ON_CALL_DUTY_ROSTER_ALERTS_DEL` (after delete), `ON_CALL_DUTY_ROSTER_ALERTS_INS` (before insert), `ON_CALL_DUTY_ROSTER_ALERTS_UPD` (before update)

## HRD.ON_CALL_DUTY_ROSTER_NEW

| Column | Type | Null | Comment |
|---|---|---|---|
| ROSTER_TYPE_ID | NUMBER(3) | N |  |
| ROSTER_DATE | DATE | N |  |
| ROSTER_PRIMARY_MRNO | VARCHAR2(14) | Y |  |
| ROSTER_COVERING_MRNO | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| START_TIME | DATE | N |  |
| END_TIME | DATE | Y |  |
| ROSTER_LOCATION_ID | VARCHAR2(3) | N |  |
| ROSTER_SECONDARY_MRNO | VARCHAR2(14) | Y |  |
| ROSTER_END_DATE | DATE | Y |  |
| POST_CALL | CHAR(1) default 'N' | Y |  |
| ROSTER_BATCH_GROUP_ID | VARCHAR2(6) | Y |  |
| ROSTER_BATCH_ID | VARCHAR2(6) | Y |  |
| ONCALL_PERSON_4 | VARCHAR2(14) | Y |  |
| ONCALL_PERSON_5 | VARCHAR2(14) | Y |  |

- **PK** `DUTY_ROSTER_NEW_PK`: ROSTER_TYPE_ID, ROSTER_DATE, LOCATION_ID, ROSTER_LOCATION_ID, START_TIME
- **Triggers**: `ON_CALL_DUTY_ROSTER_NEW_DEL` (after delete), `ON_CALL_DUTY_ROSTER_NEW_INS` (before insert), `ON_CALL_DUTY_ROSTER_NEW_UPD` (before update), `ON_CALL_ROSTER_NEW_INSERT` (before insert)

## HRD.ON_CALL_ROSTER_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ROSTER_TYPE_ID | NUMBER(3) | N |  |
| ROSTER_MRNO | VARCHAR2(14) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `ROSTER_RIGHTS_PK_1`: ROSTER_TYPE_ID, ROSTER_MRNO, LOCATION_ID
- **Triggers**: `ON_CALL_ROSTER_RIGHTS_INSERT` (before insert)

## HRD.ON_CALL_ROSTER_SWAP_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | Y |  |
| SWAPED_EMP_CODE | VARCHAR2(14) | Y |  |
| STATUS | CHAR(1) | Y |  |
| SHIFT_TYPE | CHAR(1) default 'C' | Y |  |
| EMP_ROSTER_SWAP_DATE | DATE | Y |  |
| ROSTER_TYPE_ID | NUMBER(3) | Y |  |
| ROSTER_SWAP_ENTRY_DATE | DATE | Y |  |
| ONCALL_ROSTER_DATE | DATE | Y |  |
| REQUEST_TYPE | CHAR(1) | Y |  |
| SWAP_ONCALL_ROSTER_DATE | DATE | Y |  |
| SWAP_ROSTER_TYPE_ID | NUMBER(3) | Y |  |
| SWAP_ROSTER_SWAP_DATE | DATE | Y |  |
| IS_LFA_REPLACE | CHAR(1) default 'N' | Y |  |
| LFA_START_DATE | DATE | Y |  |
| LFA_END_DATE | DATE | Y |  |

- **Triggers**: `ONCALL_ROSTER_SWAP_REQUEST_PT_INS` (before insert or update of status), `ON_CALL_ROS_SWAP_REQ_DEL` (after delete), `ON_CALL_ROS_SWAP_REQ_INS` (before insert), `ON_CALL_ROS_SWAP_REQ_UPD` (before update)

## HRD.ON_CALL_ROSTER_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ROSTER_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(6) | Y |  |
| ROLE_ID | NUMBER(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SEND_EMAIL | CHAR(1) | Y |  |
| FUTURE_ROSTER_DAYS | NUMBER(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| REPORT_ID | VARCHAR2(11) | Y |  |
| DAY_GAP | CHAR(1) default 'N' | Y | This column contains the flag value (Y, N) |
| ROSTER_ORGANIZER | VARCHAR2(14) | Y | Responsible person to populate on call duty roster |
| IS_QUEUE_GENERATE | CHAR(1) default 'N' | Y | This column contains the information (Y, N) in case of On Call Roster Missing |
| ROSTER_CATEGORY | CHAR(1) default 'C' | Y | This column contains flag informatin. C => Clinical, A => Admin |
| ROSTER_AUTHORIZED_PERSON | VARCHAR2(14) | Y |  |
| ACGME | CHAR(1) default 'Y' | Y |  |
| IS_DASHBOARD | CHAR(1) default 'N' | Y |  |
| ROSTER_BATCH_GROUP_ID | VARCHAR2(6) | Y |  |

- **PK** `ONCALL_ROSTER_PK_1`: ROSTER_TYPE_ID, LOCATION_ID
- **FK** `ONCALL_ROSTER_FK_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `ONCALL_ROSTER_FK_2`: (SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID)
- **FK** `ONCALL_ROSTER_FK_3`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID) [disabled]
- **FK** `ONCALL_ROSTER_FK_4`: (ROLE_ID) -> SECURITY.ROLE(ROLE_ID) [disabled]
- **Triggers**: `ON_CALL_ROSTER_TYPE_DEL` (after delete), `ON_CALL_ROSTER_TYPE_INS` (before insert), `ON_CALL_ROSTER_TYPE_INSERT` (before insert), `ON_CALL_ROSTER_TYPE_UPD` (before update)

## HRD.ORG_TREE_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| INITIAL_STATE | NUMBER(1) | Y |  |
| DEPTH | NUMBER(3) | Y |  |
| LABEL | VARCHAR2(182) | Y |  |
| ICON | VARCHAR2(256) | Y |  |
| DATA | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |


## HRD.OSV_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| OSV_TYPE | VARCHAR2(10) | Y |  |
| ALERT_NO | NUMBER | Y |  |
| OSV_STATUS | CHAR(2) | Y |  |
| INSTITUTION_ID | NUMBER(4) | Y |  |
| STUDY_TYPE_ID | VARCHAR2(3) | Y |  |
| STUDY_PROGRAM_ID | VARCHAR2(10) | Y |  |
| REMINDER_SENT_DATE | DATE | Y |  |
| REGISTRATION_TYPE_ID | NUMBER | Y |  |
| EXPIRY_DATE | DATE | Y |  |

- **Triggers**: `OSV_ALERTS_DEL` (after delete), `OSV_ALERTS_INS` (before insert), `OSV_ALERTS_UPD` (before update)

## HRD.OVERTIME_DEPARTMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(10) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTION_TAKEN | VARCHAR2(1) default 'C' | Y |  |

- **PK** `PK_OVERTIME_DEPARTMENTS`: SERIAL_NO, DEPARTMENT_ID
- **FK** `FK_OVERTIME_DEPARTMENTS_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **CHECK** `CK_OVERTIME_DEPARTMENTS_001`: ACTION_TAKEN IN ('C','A')

## HRD.OVER_TIME_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| GRADE_ID | VARCHAR2(6) | N |  |
| EFFECTIVE_DATE | DATE | N |  |
| MINIMUM_TIME | NUMBER(5) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| RAMZAN_MINIMUM_TIME | NUMBER(5) | Y |  |

- **PK** `PK_OVER_TIME_PARAMETERS`: GRADE_ID, EFFECTIVE_DATE
- **Triggers**: `OVER_TIME_PARAMETERS_CEA` (before insert or update or delete), `OVER_TIME_PARAMETERS_DEL` (after delete), `OVER_TIME_PARAMETERS_INS` (before insert), `OVER_TIME_PARAMETERS_UPD` (before update), `TRG_WS_XLD_JE_QP_Q` (after insert or update or delete)

## HRD.OVER_TIME_TIME_LIMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| FROM_DATE | DATE | Y |  |
| MINIMUM_TIME | NUMBER(3) | Y |  |

- **Triggers**: `OVER_TIME_TIME_LIMIT_DEL` (after delete), `OVER_TIME_TIME_LIMIT_INS` (before insert), `OVER_TIME_TIME_LIMIT_UPD` (before update)

## HRD.PATIENTS_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_MRNO | VARCHAR2(14) | Y |  |
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| CLINIC_ID | VARCHAR2(200) | Y |  |
| TRANS_DATE | DATE | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(7) | Y |  |
| ORDER_TYPE_ID | VARCHAR2(3) | Y |  |
| ORDER_NO | VARCHAR2(9) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| TRANSACTION_NO | NUMBER(4) | Y |  |
| INDICATOR_ID | NUMBER(3) | Y |  |
| IPD_VISITS | NUMBER(4) | Y |  |
| ICU_VISITS | NUMBER(4) | Y |  |
| VISITS | NUMBER(4) | Y |  |
| DAYS | NUMBER(4) | Y |  |
| FCP_DONE | NUMBER(4) | Y |  |
| FCP_NOT_DONE | NUMBER(4) | Y |  |
| REVIEWED_WITHIN_TIME | NUMBER(4) | Y |  |
| REVIEWED_LATE | NUMBER(4) | Y |  |
| REVIEWED_BY | VARCHAR2(300) | Y |  |
| TOT_SESSION | NUMBER(3) | Y |  |
| MDT | NUMBER(3) | Y |  |
| CONSULTANT_NOTE_SIGN_DATE | DATE | Y |  |
| CPT_ID | VARCHAR2(30) | Y |  |
| TOTAL | NUMBER | Y |  |
| NULL_COUNT | NUMBER(4) | Y |  |
| PERCENTAGE | NUMBER | Y |  |
| NO_OF_PATIENT_SEEN | NUMBER(4) | Y |  |
| SESSION_PERFORM_PERCENTAGE | NUMBER(6) | Y |  |
| REVIEWED_INTIME | NUMBER(4) | Y |  |
| TOTAL_HISTOPATH_REPORTS | NUMBER(7) | Y |  |
| NULL_MICRO | NUMBER(7) | Y |  |
| TOTAL_PATIENT_SCHEDULED | NUMBER | Y |  |
| VERIFYING_CONSULTANT_MRNO | VARCHAR2(14) | Y |  |
| PC_MRNO | VARCHAR2(14) | Y |  |
| APPOINTMENT_DATE | DATE | Y |  |
| VERIFYING_CONSULTANT_DATE | DATE | Y |  |
| VERIFICATION_COUNT | NUMBER(5) | Y |  |
| PATIENT_RADIATION_PLANNED | NUMBER | Y |  |
| MDT_DATE | DATE | Y |  |
| YES | NUMBER(4) | Y |  |
| NO | NUMBER(4) | Y |  |
| INSIDE_PROCEDURES | NUMBER(4) | Y |  |
| OUTSIDE_PATIENTS | NUMBER(4) | Y |  |
| DELAYED | NUMBER(7) | Y |  |
| CLINIC | VARCHAR2(300) | Y |  |
| DR_NAME | VARCHAR2(300) | Y |  |
| SESSIONS_PERFORMED | NUMBER(4) | Y |  |
| SESSIONS_CANCELLED | NUMBER(4) | Y |  |
| TOTAL_SESSIONS_TO_BE_PERFORMED | NUMBER(4) | Y |  |
| SESSION_PERFORM_PER | VARCHAR2(300) | Y |  |
| SPECIALITY | VARCHAR2(300) | Y |  |
| NAME | VARCHAR2(1000) | Y |  |
| TOTAL_VISITS | NUMBER | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| RAD_NO | VARCHAR2(30) | Y |  |
| MODALITY | VARCHAR2(30) | Y |  |
| SCAN_DATE | DATE | Y |  |
| SIGN_BY_DOCTOR | VARCHAR2(300) | Y |  |
| SCORE_CATEGORY_DESC | VARCHAR2(300) | Y |  |
| ADMITTED_CONSULTANT | VARCHAR2(300) | Y |  |
| DOCTOR_NAME | VARCHAR2(200) | Y |  |
| DEPARTMENT | VARCHAR2(300) | Y |  |
| CHEMO_VERIFYING_CONSULTANT | VARCHAR2(300) | Y |  |
| PATIENT_NAME | VARCHAR2(1000) | Y |  |
| MAX_CHEMO_DATE | DATE | Y |  |
| DATE_OF_DEATH | DATE | Y |  |
| AGE | NUMBER | Y |  |
| TLOSDA | NUMBER(6) | Y |  |
| TNOA | NUMBER(6) | Y |  |
| ALOSDA | NUMBER(6) | Y |  |
| ICU_TOT_LOS | NUMBER(6) | Y |  |
| ICU_AVG_LOS | NUMBER(6) | Y |  |
| SUBSPECIALITY | VARCHAR2(300) | Y |  |
| VERIFY_CONSULTANT_NAME | VARCHAR2(300) | Y |  |
| REFFERING_INHOUSE_DOCTOR_ID | VARCHAR2(7) | Y |  |
| PRIMARY_CONSULTANT | VARCHAR2(200) | Y |  |
| SLAB_ID | VARCHAR2(13) | Y |  |
| MIN_APP_DATE | DATE | Y |  |
| PAT_NAME | VARCHAR2(300) | Y |  |
| WO_DATE | DATE | Y |  |
| WO_DAY | VARCHAR2(300) | Y |  |
| DISCHARGE_DATE | DATE | Y |  |
| DISCHARGE_DAY | VARCHAR2(300) | Y |  |
| CONSULTANT_NAME | VARCHAR2(200) | Y |  |
| ATTENDING_CONSULTANT | VARCHAR2(300) | Y |  |
| ATTENDING_CONSULTANT_ID | VARCHAR2(14) | Y |  |
| NOT_REVIEWED | NUMBER(4) | Y |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| ORDER_DATE | DATE | Y |  |
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| DOCTOR | VARCHAR2(300) | Y |  |
| CPT_DESC | VARCHAR2(300) | Y |  |
| FREQUENCY | NUMBER(4) | Y |  |
| PATIENT | VARCHAR2(300) | Y |  |
| CPT_CODE | VARCHAR2(30) | Y |  |
| SIGNED_BY | VARCHAR2(300) | Y |  |
| FINAL_SIGN_DATE | DATE | Y |  |
| ADDENDUM_DOCTOR_NAME | VARCHAR2(300) | Y |  |
| ADDENDUM_DATE | DATE | Y |  |
| SECTION_PREFIX | VARCHAR2(30) | Y |  |
| L_SECTION_NO | VARCHAR2(30) | Y |  |
| L_LOCATION | VARCHAR2(200) | Y |  |
| L_SPECIMEN_DATE | DATE | Y |  |
| L_EXPECTED_REPORT_DATE | DATE | Y |  |
| L_FINAL_SIGN_DATE | DATE | Y |  |
| CLINIC_SPECIALITY | VARCHAR2(300) | Y |  |
| ICU_VISIT_DATE | DATE | Y |  |
| CANCER_STATUS | VARCHAR2(10) | Y |  |
| YY | NUMBER(4) | Y |  |
| MM | NUMBER(2) | Y |  |
| PATIENT_RADIATION_PERFORMED | NUMBER | Y |  |
| MON | VARCHAR2(20) | Y |  |
| PLANNING_TECHNIQUE | VARCHAR2(300) | Y |  |
| MEDICINE | VARCHAR2(300) | Y |  |
| ORDER_LOCATION | VARCHAR2(300) | Y |  |
| ENDOSCOPY_SECTION | VARCHAR2(100) | Y |  |
| TOTAL_PERFORMED_PROCEDURES | NUMBER(4) | Y |  |
| COMPLEX_PROCEDURES | NUMBER(4) | Y |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| GR_LOC_ID | VARCHAR2(30) | Y |  |
| GR_LOC_DESC | VARCHAR2(30) | Y |  |
| GR_LOC_SEQ | NUMBER(4) | Y |  |
| OC_LOC_DESC | VARCHAR2(300) | Y |  |
| PATIENT_TYPE | VARCHAR2(300) | Y |  |
| NATURE_DETAIL_DESC | VARCHAR2(30) | Y |  |
| TOTAL_ORDERS | NUMBER(4) | Y |  |
| INTIME | NUMBER | Y |  |
| CARDIOLOGIST_NAME | VARCHAR2(300) | Y |  |
| INTIME_PERFORMED | NUMBER(4) | Y |  |
| DELAY_PERFORMED | NUMBER(4) | Y |  |
| PERFORMED_BY | VARCHAR2(300) | Y |  |
| SURGERY_NOTES_SIGN_BY | VARCHAR2(14) | Y |  |
| PERFORM_DATE | DATE | Y |  |
| SURGEON_NAME | VARCHAR2(200) | Y |  |
| PROCEDURES | VARCHAR2(200) | Y |  |
| COUNT | VARCHAR2(30) | Y |  |
| DELYED | VARCHAR2(200) | Y |  |
| TOTAL_ROW | VARCHAR2(200) | Y |  |
| DOCTOR_ID_NAME | VARCHAR2(500) | Y |  |
| CLINIC_ID_NAME | VARCHAR2(500) | Y |  |
| DUMMY2 | VARCHAR2(30) | Y |  |
| DUMMY1 | VARCHAR2(30) | Y |  |
| DUMMY3 | VARCHAR2(30) | Y |  |
| DUMMY4 | VARCHAR2(30) | Y |  |
| MRNO_PAT_NAME | VARCHAR2(14) | Y |  |
| SEX | VARCHAR2(200) | Y |  |
| REPORT_DATE | DATE | Y |  |
| PROCEDURE_NAME | VARCHAR2(500) | Y |  |
| ADENOMA_DETECTION_RATE | VARCHAR2(5) | Y |  |
| GENDER | VARCHAR2(200) | Y |  |
| EBUS_PROCEDURE_DATE | DATE | Y |  |
| CYTO_REPORT_DATE | DATE | Y |  |
| INADEQUATE | VARCHAR2(200) | Y |  |
| DIAGNOSIS | VARCHAR2(4000) | Y |  |
| WRITTEN_BY | VARCHAR2(200) | Y |  |
| SIGNED_DATE | DATE | Y |  |
| PARAMETER | VARCHAR2(500) | Y |  |
| FIRST_VALUE | VARCHAR2(200) | Y |  |
| SECOND_VALUE | VARCHAR2(200) | Y |  |
| RADIOTHERAPIST | VARCHAR2(200) | Y |  |
| PATIENT_SEEN | NUMBER | Y |  |
| TOTAL_PATIENTS | NUMBER | Y |  |
| WO_MADE | NUMBER | Y |  |
| PAT_SEEN | NUMBER | Y |  |
| DUMMY5 | VARCHAR2(30) | Y |  |
| FRACTION_DATE | DATE | Y |  |
| CLINIC_VISIT_DATE | DATE | Y |  |
| ORDERD_BY | VARCHAR2(500) | Y |  |
| CPT | VARCHAR2(2000) | Y |  |
| CONSULTANT | VARCHAR2(500) | Y |  |
| HB_HCV_HIV_REPORTS_AVAILABLE | DATE | Y |  |
| NEPHROLOGIST_CHECKUP | DATE | Y |  |
| NEPHROLOGIST | VARCHAR2(1000) | Y |  |
| TOTAL_NO_OF_ADMISSIONS | NUMBER | Y |  |
| TOTAL_LENGTH_OF_STAY | NUMBER | Y |  |
| AVERAGE_LENGTH_OF_STAY | NUMBER | Y |  |
| TOTAL_LENGTH_OF_STAY_ICU | NUMBER | Y |  |
| AVERAGE_LENGTH_OF_STAY_ICU | NUMBER | Y |  |
| RADIOTHERAPY_TYPE | VARCHAR2(30) | Y |  |
| LOU | VARCHAR2(30) | Y |  |
| REQUEST_DATE | DATE | Y |  |
| FINAL_SIGN_BY | VARCHAR2(300) | Y |  |
| TOTAL_REPORTS | VARCHAR2(30) | Y |  |
| NULL_CONCLUSION | VARCHAR2(30) | Y |  |


## HRD.PAYROLL_ATTENDANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_START_DATE | DATE | N |  |
| MONTH_END_DATE | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| INCLUDE_IN_PAYROLL | CHAR(1) default 'N' | N |  |
| STATUS | CHAR(1) | Y |  |
| SYSTEM_REMARKS | VARCHAR2(2000) | Y |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| DAYS_PERFORMED | NUMBER(5) | Y |  |
| ADDITIONAL_WORKING_DAYS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(5) | Y |  |
| ACTUAL_SHIFT_MINUTES | NUMBER(8) | Y |  |
| PERFORMED_MINUTES | NUMBER(8) | Y |  |
| CALCULATED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| APPROVED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| PROPER_SWIPES | NUMBER(5) | Y |  |
| IMPROPER_SWIPES | NUMBER(5) | Y |  |
| NO_SWIPES | NUMBER(5) | Y |  |
| LATE_COMING | NUMBER(5) | Y |  |
| AVG_ARRIVAL_OFFSET_MINUTES | NUMBER(4) | Y |  |
| EARLY_LEAVING | NUMBER(5) | Y |  |
| AVG_LEAVING_OFFSET_MINUTES | NUMBER(4) | Y |  |
| USERID | VARCHAR2(10) | Y |  |
| LEAVE_DAYS | NUMBER(4) | Y |  |
| NIGHTS | NUMBER(4) | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| MANUAL | CHAR(1) default 'N' | Y |  |
| ON_CALL_DAYS | NUMBER(4) | Y |  |
| ON_CALL_ALLOWANCE | NUMBER(12,2) | Y |  |
| SALARY_START_DATE | DATE | Y |  |
| SALARY_END_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ABSENT | NUMBER(4) | Y |  |
| OVERTIME_MONTH_ID | VARCHAR2(6) | Y | This column will use for overtime calculation payment |
| DR_LOCATION_WHM | NUMBER | Y | this colum will use to summerized the Work from home location from duty roster |
| DR_LOCATION_OUTSIDE_HOSPITAL | NUMBER | Y | this colum will use to summerized the  location outside the hospital from duty roster |

- **PK** `PK_PAYROLL_ATTENDANCE`: MONTH_START_DATE, MONTH_END_DATE, MRNO
- **FK** `FK_PAYROLL_ATTENDANCE_1`: (MONTH_START_DATE, MONTH_END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE) [disabled]
- **FK** `FK_PAYROLL_ATTENDANCE_2`: (MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **CHECK** `CHK_PAYROLL_ATTENDANCE_1`: INCLUDE_IN_PAYROLL IN ('N','Y')
- **CHECK** `CHK_PAYROLL_ATTENDANCE_2`: STATUS IN ('N','Y')
- **Triggers**: `PAYROLL_ATTENDANCE_DEL` (after delete), `PAYROLL_ATTENDANCE_INS` (before insert), `PAYROLL_ATTENDANCE_UPD` (before update)

## HRD.PA_360_SCORE

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_YEAR | VARCHAR2(4) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PATP_ID | NUMBER(3) | Y |  |
| APPRAISEE_MRNO | VARCHAR2(14) | Y |  |
| TOTAL_SCORE | NUMBER | Y |  |

- **Triggers**: `PA_360_SCORE_DEL` (after delete), `PA_360_SCORE_INS` (before insert), `PA_360_SCORE_UPD` (before update)

## HRD.PA_QUERY_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_QUERY_ID | NUMBER(4) | N |  |
| PA_QUERY_DESC | VARCHAR2(200) | Y |  |
| PA_QUERY | CLOB | Y |  |
| QUERY_TYPE | CHAR(1) | Y | S for summary , D for detail query |
| FORMULA_TYPE_ID | NUMBER(3) | Y |  |
| FORMULA_SOURCE | VARCHAR2(500) | Y |  |
| TEAM_ID | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_QUERY_SETUP`: PA_QUERY_ID

## HRD.PA_QA_CONCEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_QA_PARAM_ID | NUMBER(3) | N |  |
| CONCEPT | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `PK_PA_QA_CONCEPT`: PA_QA_PARAM_ID
- **Triggers**: `PA_QA_CONCEPT_DEL` (after delete), `PA_QA_CONCEPT_INS` (before insert), `PA_QA_CONCEPT_UPD` (before update)

## HRD.PA_QA_INDICATOR

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_QA_PARAM_ID | NUMBER(3) | N |  |
| PERF_INDICATOR | VARCHAR2(4000) | Y |  |
| RATING | NUMBER(6) | Y |  |
| MEASURE | NUMBER(5,2) | Y |  |
| SCORE | NUMBER(5,2) | Y |  |
| PARENT_ID | NUMBER(3) | Y |  |
| PERFORM_ID | NUMBER(3) | Y |  |
| PATPID | NUMBER(3) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| SOURCE_NAME | VARCHAR2(3000) | Y |  |
| GET_VALUE | CHAR(1) default 'N' | Y |  |
| PA_QUERY_ID_DETAIL | NUMBER(4) | Y |  |
| PA_QUERY_ID_SUMMARY | NUMBER(4) | Y |  |
| BENCH_MARK_REQ | CHAR(1) default 'N' | Y |  |
| BENCH_MARK_NO | VARCHAR2(8) | Y |  |
| BENCH_MARK_TITLE | VARCHAR2(200) | Y |  |
| BECH_MARK_DESCRIPTION | VARCHAR2(100) | Y |  |
| PA_QUERY_ID_FORMULA | NUMBER(4) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PA_QUERY_ID_FUNC_QUERY | NUMBER(4) | Y | This column contains function query id |

- **PK** `PK_PA_QA_INDICATOR`: PA_QA_PARAM_ID
- **FK** `FK_PA_QA_PARENT_ID`: (PARENT_ID) -> HRD.PA_QA_CONCEPT(PA_QA_PARAM_ID) [disabled]
- **FK** `FK_PA_QUERY_ID`: (PA_QUERY_ID_DETAIL) -> HRD.PA_QUERY_SETUP(PA_QUERY_ID) [disabled]
- **Triggers**: `PA_QA_INDICATOR_DEL` (after delete), `PA_QA_INDICATOR_INS` (before insert), `PA_QA_INDICATOR_UPD` (before update)

## HRD.PA_CONSULTANT_INDICATOR
this table use to consultants indicator mapping purpose

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| INDICATOR_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| PA_SCORE | NUMBER(10,2) | Y | this column use for Instructor appraisal score |
| BENCHMARK_ALLOW | CHAR(1) default 'Y' | Y |  |
| PATP_ID | NUMBER(3) | N |  |

- **PK** `PK_PA_CONSULTANT_INDICATOR`: MRNO, INDICATOR_ID, PATP_ID
- **FK** `FK_INDICATOR_ID_01`: (INDICATOR_ID) -> HRD.PA_QA_INDICATOR(PA_QA_PARAM_ID) [disabled]
- **Triggers**: `PA_CONSULTANT_INDICATOR_DEL` (after delete), `PA_CONSULTANT_INDICATOR_INS` (before insert), `PA_CONSULTANT_INDICATOR_UPD` (before update)

## HRD.PA_DEF_TEMPLATE

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_TEMPLATE_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REPORT_NAME | VARCHAR2(255) | Y |  |
| FORM_NAME | VARCHAR2(255) | Y | This column use for template wise object will be opened. |
| QPS_DATA_REQUIRED | CHAR(1) default 'N' | Y | This column required 'Y' if QPS data required appraisal wise |
| APEX_OBJECT_CODE | VARCHAR2(255) | Y | will contain the apex object code |

- **PK** `PK_PA_TEMPLATE`: PA_TEMPLATE_ID
- **UK** `UK_PA_TEMPLATE_01`: DESCRIPTION
- **Triggers**: `PA_DEF_TEMPLATE_DEL` (after delete), `PA_DEF_TEMPLATE_INS` (before insert), `PA_DEF_TEMPLATE_UPD` (before update)

## HRD.PA_DEF_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_TYPE_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| PREVIOUS_ROUTING_HIERARCHY | CHAR(1) default 'N' | Y |  |
| IS_WEIGHTAGE_TABLE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PA_DEF_TYPE`: PA_TYPE_ID
- **UK** `UK_PA_DEF_TYPE_01`: DESCRIPTION
- **CHECK** `CHK_PA_DEF_TYPE_01`: ACTIVE IN ('N','Y')
- **Triggers**: `PA_DEF_TYPE_DEL` (after delete), `PA_DEF_TYPE_INS` (before insert), `PA_DEF_TYPE_UPD` (before update)

## HRD.PA_TYPE_PERIOD

| Column | Type | Null | Comment |
|---|---|---|---|
| PATP_ID | NUMBER(3) | N |  |
| PA_TYPE_ID | NUMBER(2) | N |  |
| PA_START_DATE | DATE | N |  |
| PA_END_DATE | DATE | N |  |
| PA_STATUS_ID | VARCHAR2(3) | Y |  |
| PA_ALERT_TEXT | VARCHAR2(4000) | Y |  |
| PA_SENDER_EMAIL | VARCHAR2(100) | Y |  |
| PA_REMINDER_TEXT | VARCHAR2(4000) | Y | Email text send to HOD as reminder |
| PA_CUT_OFF_DATE | DATE | Y | Cut off date to select employees for the specified appraisal period |
| PA_ALERT_SUBJECT | VARCHAR2(300) | Y |  |
| PA_REMINDER_SUBJECT | VARCHAR2(300) | Y |  |
| APP_TYPE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `PK_PA_TYPE_PERIOD`: PATP_ID
- **UK** `UK_PA_TYPE_PERIOD_01`: PA_TYPE_ID, PA_START_DATE, PA_END_DATE
- **FK** `FK_PA_TYPE_PERIOD_01`: (PA_TYPE_ID) -> HRD.PA_DEF_TYPE(PA_TYPE_ID)
- **FK** `FK_PA_TYPE_PERIOD_03`: (PA_STATUS_ID) -> ORDERENTRY.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **Triggers**: `PA_TYPE_PERIOD_DEL` (after delete), `PA_TYPE_PERIOD_INS` (before insert), `PA_TYPE_PERIOD_UPD` (before update)

## HRD.PA_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_ID | VARCHAR2(12) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| APPRAISEE_MRNO | VARCHAR2(14) | Y |  |
| PATP_ID | NUMBER(3) | Y |  |
| PA_TEMPLATE_ID | NUMBER(2) | Y |  |
| REPORT_NAME | VARCHAR2(255) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| HR_DISTRIBUTE | CHAR(1) default 'N' | Y |  |
| MASTER_HIERARCHY_ID | VARCHAR2(12) | Y |  |
| PA_YEAR | VARCHAR2(4) | Y |  |
| EXCLUDE_IN_APPRAISAL | CHAR(1) | Y |  |
| PA_TYPE_ID | NUMBER | Y |  |
| REPORTING_TO | CHAR(1) | Y | This column contains value M for MD and C for CEO |

- **PK** `PK_PA_HIERARCHY`: HIERARCHY_ID
- **FK** `FK_PA_HIERARCHY_01`: (PATP_ID) -> HRD.PA_TYPE_PERIOD(PATP_ID)
- **FK** `FK_PA_HIERARCHY_02`: (PA_TEMPLATE_ID) -> HRD.PA_DEF_TEMPLATE(PA_TEMPLATE_ID) [disabled]
- **FK** `FK_PA_HIERARCHY_03`: (APPRAISEE_MRNO) -> REGISTRATION.PATIENT(MRNO)
- **Triggers**: `PA_HIERARCHY_DEL` (after delete), `PA_HIERARCHY_INS` (before insert), `PA_HIERARCHY_UPD` (before update)

## HRD.PA_PERFORM_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| HIERARCHY_ID | VARCHAR2(12) | Y |  |
| PA_PERFORM_STATUS_ID | VARCHAR2(3) | Y |  |
| TRANS_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| OVERALL_ASSESSMENT | VARCHAR2(5) | Y |  |
| DISTRIBUTED_DATE | DATE | Y |  |
| IS_INCLUDED | CHAR(1) | Y |  |
| PA_SCORE | NUMBER(3) | Y |  |
| RESEARCH_DATA_STATUS | CHAR(1) | Y | 'NULL' MEAN NOT IN-PROCESS 'F' MEAN HR QUEUE 'R' MEAN RESEARCH DEPARTMENT QUEUE |
| IS_MARK_DEDECTED | CHAR(1) | Y | This colum will be mark 'Y' when rating deduct |
| APPRAISAL_MARK_DEDUCATION | NUMBER(3) | Y | This Colum will be use for Appraisal wise Mark deduction |

- **PK** `PK_PA_PERFORM_MASTER`: PA_PERFORM_ID
- **UK** `UK_PA_PERFORM_MASTER_01`: HIERARCHY_ID, PA_PERFORM_ID
- **FK** `FK_PA_PERFORM_MASTER_01`: (HIERARCHY_ID) -> HRD.PA_HIERARCHY(HIERARCHY_ID)
- **FK** `FK_PA_PERFORM_MASTER_02`: (PA_PERFORM_STATUS_ID) -> ORDERENTRY.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **Triggers**: `PA_PERFORM_MASTER_DEL` (after delete), `PA_PERFORM_MASTER_INS` (before insert), `PA_PERFORM_MASTER_UPD` (before update)

## HRD.PA_DEF_RATING_VALUE

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_RATING_VALUE_ID | NUMBER(3) | N |  |
| PA_RATING_TYPE_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| PA_RATING_ACTUAL_VALUE | NUMBER(3) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(3) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| URDU_DESCRIPTION | NVARCHAR2(200) | Y |  |

- **PK** `PK_PA_DEF_RATING_VALUE`: PA_RATING_VALUE_ID, PA_RATING_TYPE_ID
- **CHECK** `CHK_PA_DEF_RATING_VALUE_01`: ACTIVE IN ('N','Y')
- **Triggers**: `PA_DEF_RATING_VALUE_DEL` (after delete), `PA_DEF_RATING_VALUE_INS` (before insert), `PA_DEF_RATING_VALUE_UPD` (before update)

## HRD.PA_PERFORM_APPRAISER

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_APPRAISER_ID | NUMBER(11) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PA_APPRAISER_MRNO | VARCHAR2(14) | N |  |
| PA_STATUS_ID | VARCHAR2(3) | N | Record status |
| TRANS_DATE | DATE | Y | Date on which transaction is made |
| REMARKS_OLD | VARCHAR2(4000) | Y |  |
| HIERARCHY_ID | VARCHAR2(12) | Y |  |
| APPRAISER_ROLE | CHAR(1) default 'R' | N | 'A' = Approve,  'R'= Recommend, 'F'= Final, 'S' = Send Back To Previous Authority |
| ORDER_BY | NUMBER(2) default 0 | N | Store appraisal routing sequence. |
| PA_TEMPLATE_ID | NUMBER(2) | Y | Obsolete |
| EMPLOYEE_REIVEW | CHAR(1) default 'N' | Y | Require review from employee after performance of specified appraiser |
| EMPLOYEE_DECISION | CHAR(1) default 'P' | Y | 'Y' = Agree, 'N' = Disagree, 'P' = Pending |
| APPROVER_AGREEMENT | CHAR(1) default 'N' | Y |  |
| DISAGREEMENT_APPRAISER | CHAR(1) | Y |  |
| REMARKS | CLOB | Y |  |

- **PK** `PK_PERFORM_APPRAISER`: PA_PERFORM_APPRAISER_ID
- **UK** `UK_PERFORM_APPRAISER_01`: HIERARCHY_ID, PA_APPRAISER_MRNO, APPRAISER_ROLE
- **FK** `FK_PERFORM_APPRAISER_01`: (PA_PERFORM_ID) -> HRD.PA_PERFORM_MASTER(PA_PERFORM_ID)
- **FK** `FK_PERFORM_APPRAISER_02`: (PA_STATUS_ID) -> ORDERENTRY.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **CHECK** `CHK_PA_PERFORM_APPRAISER_01`: APPRAISER_ROLE IN ('A','F','R','S')
- **CHECK** `CHK_PA_PERFORM_APPRAISER_02`: EMPLOYEE_REIVEW IN ('N','Y')
- **CHECK** `CHK_PA_PERFORM_APPRAISER_03`: EMPLOYEE_DECISION IN ('N','Y', 'P')
- **Triggers**: `PA_PERFORM_APPRAISER_DEL` (after delete), `PA_PERFORM_APPRAISER_INS` (before insert), `PA_PERFORM_APPRAISER_UPD` (before update)

## HRD.PA_DEF_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_SECTION_ID | NUMBER(2) | N |  |
| PA_ATTRIBUTE_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| PA_SECTION_NAME | VARCHAR2(255) | N |  |
| PA_SECTION_TYPE | CHAR(1) | Y | 'R' = Rating Value, 'O' = Objective , 'T'= Open text |
| PA_OBJECT_CODE | VARCHAR2(11) | Y | Object called for specified section |
| PARENT_SECTION_ID | NUMBER(2) | Y |  |
| NO_OF_EMP_REQ | CHAR(1) | Y |  |
| TAB_ID | NUMBER(3) | Y |  |
| TRAINING_EVALUATION | CHAR(1) | Y |  |

- **PK** `PK_PA_DEF_SECTION`: PA_SECTION_ID
- **FK** `FK_PA_DEF_SECTION_02`: (PA_OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **CHECK** `CHK_PA_DEF_SECTION`: ACTIVE IN ('N','Y')
- **Triggers**: `PA_DEF_SECTION_DEL` (after delete), `PA_DEF_SECTION_INS` (before insert), `PA_DEF_SECTION_UPD` (before update)

## HRD.PA_DEF_SECTION_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PARAMETER_ID | NUMBER(2) | N |  |
| PA_SECTION_ID | NUMBER(2) | N |  |
| PA_PARAMETER_NAME | VARCHAR2(255) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| PA_PARAMETER_TYPE | CHAR(1) | N | 'F' = Fix value, 'O' = Open text, 'T'= Title |
| PA_RATING_TYPE_ID | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| IS_REQUIRED | CHAR(1) default 'N' | N |  |
| PARENT_PARAMETER_ID | NUMBER(2) | Y |  |
| PARENT_SECTION_ID | NUMBER(2) | Y |  |
| LOV_NAME | VARCHAR2(50) | Y |  |
| LOV_ID | VARCHAR2(5) | Y |  |
| IS_QA | CHAR(1) | Y |  |
| NO_OF_NOMINATED | NUMBER(3) | Y |  |
| IS_SUM | CHAR(1) | Y |  |
| PA_QA_ID | NUMBER(3) | Y |  |
| IS_PUBLISHED_RESEARCH | CHAR(1) default 'N' | Y |  |
| HR | CHAR(1) default 'N' | Y |  |
| APPROVAL | CHAR(1) default 'N' | Y |  |
| SOURCE_NAME | VARCHAR2(300) | Y | Procedure / function name |
| GET_VALUE | CHAR(1) default 'N' | Y |  |
| URDU_DESCRIPTION | NVARCHAR2(200) | Y |  |
| IS_MARK_DEDUCTION | CHAR(1) default 'N' | Y |  |
| REPORTING_TO | CHAR(1) | Y | This column contains value M for MD and C for CEO |
| IS_RESEARCH_BLOCK | CHAR(1) default 'N' | Y |  |
| REFRENCE_CANVAS | CHAR(1) | Y | R for refrence and O for Open text |
| PROMOTION | CHAR(1) | Y | This parameter will be use for promotion recomendation |
| HR_TRAINING | CHAR(1) | Y | THIS COLUMN WILL BE USE FOR HR RELATED TRAINING |
| DEPARTMENT_TRAINING | CHAR(1) | Y | This column will be user for department related training |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | Y |  |
| LESS_VALUE | NUMBER | Y | this column will be use if any value of parameter is less then |
| APPRAISEE_REMARKS_REQUIRED | CHAR(1) | Y | appraisee remarks will be required if flag is 'Y' |
| MAPPING_PA_PARAMETER_ID | NUMBER(2) | Y |  |
| MAPPING_PA_SECTION_ID | NUMBER(2) | Y |  |
| IS_NA_VALUE_ALLOW | CHAR(1) | Y |  |

- **PK** `PK_PA_SECTION_PARAMETER`: PA_PARAMETER_ID, PA_SECTION_ID
- **FK** `FK_PA_SECTION_PARAMETER_01`: (PA_SECTION_ID) -> HRD.PA_DEF_SECTION(PA_SECTION_ID) [disabled]
- **FK** `FK_PA_SECTION_PARAMETER_03`: (PARENT_PARAMETER_ID, PARENT_SECTION_ID) -> HRD.PA_DEF_SECTION_PARAMETER(PA_PARAMETER_ID, PA_SECTION_ID) [disabled]
- **CHECK** `CHK_PA_SECTION_PARAMETER_01`: PA_PARAMETER_TYPE IN ('F','O','T','L','C')
- **CHECK** `CHK_PA_SECTION_PARAMETER_02`: IS_REQUIRED IN ('N','Y')
- **CHECK** `CHK_PA_SECTION_PARAMETER_03`: ACTIVE IN ('N','Y')
- **Triggers**: `PA_DEF_SECTION_PARAMETER_DEL` (after delete), `PA_DEF_SECTION_PARAMETER_INS` (before insert), `PA_DEF_SECTION_PARAMETER_UPD` (before update)

## HRD.PA_PERFORM_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PA_SECTION_ID | NUMBER(2) | N |  |

- **PK** `PK_PA_PERFORM_SECTION`: PA_PERFORM_ID, PA_SECTION_ID
- **FK** `FK_PA_PERFORM_SECTION_01`: (PA_PERFORM_ID) -> HRD.PA_PERFORM_MASTER(PA_PERFORM_ID)
- **FK** `FK_PA_PERFORM_SECTION_02`: (PA_SECTION_ID) -> HRD.PA_DEF_SECTION(PA_SECTION_ID) [disabled]
- **Triggers**: `PA_PERFORM_SECTION_DEL` (after delete), `PA_PERFORM_SECTION_INS` (before insert), `PA_PERFORM_SECTION_UPD` (before update)

## HRD.PA_PERFORM_SECTION_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_PARAM_ID | NUMBER(11) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| PA_SECTION_ID | NUMBER(2) | Y |  |
| PA_PARAMETER_ID | NUMBER(2) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_PA_PERFORM_SECTION_PARAM`: PA_PERFORM_PARAM_ID
- **FK** `FK_PA_PERFORM_SECTION_PARAM_01`: (PA_PERFORM_ID, PA_SECTION_ID) -> HRD.PA_PERFORM_SECTION(PA_PERFORM_ID, PA_SECTION_ID) [disabled]
- **FK** `FK_PA_PERFORM_SECTION_PARAM_02`: (PA_PARAMETER_ID, PA_SECTION_ID) -> HRD.PA_DEF_SECTION_PARAMETER(PA_PARAMETER_ID, PA_SECTION_ID) [disabled]
- **Triggers**: `PA_PERFORM_SECTION_PARAM_DATA` (after insert), `PA_PERFORM_SECTION_PARAM_DEL` (after delete), `PA_PERFORM_SECTION_PARAM_INS` (before insert), `PA_PERFORM_SECTION_PARAM_UPD` (before update)

## HRD.PA_PERFORM_VAL_RATING

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_PARAM_ID | NUMBER(11) | N |  |
| PA_PERFORM_APPRAISER_ID | NUMBER(11) | Y |  |
| PA_RATING_VALUE_ID | NUMBER(3) | Y |  |
| PA_RATING_TYPE_ID | NUMBER(2) | Y |  |
| TRANS_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| SIGNED_BY | VARCHAR2(14) | Y |  |
| SIGN_DATE | DATE | Y |  |
| ORGINAL_PA_RATING_VALUE_ID | NUMBER(3) | Y |  |
| PA_VALUE | VARCHAR2(50) | Y |  |
| PA_SCORE | NUMBER | Y |  |
| MAX_RATING_VALUE | NUMBER(3) | Y |  |
| ACTUAL_RATING_VALUE | NUMBER(3) | Y |  |
| IS_VERIFIED | CHAR(1) | Y |  |

- **PK** `PK_PERFORM_VAL_RATING`: PA_PERFORM_PARAM_ID
- **FK** `FK_PERFORM_VAL_RATING_01`: (PA_PERFORM_PARAM_ID) -> HRD.PA_PERFORM_SECTION_PARAM(PA_PERFORM_PARAM_ID)
- **FK** `FK_PERFORM_VAL_RATING_02`: (PA_PERFORM_APPRAISER_ID) -> HRD.PA_PERFORM_APPRAISER(PA_PERFORM_APPRAISER_ID)
- **FK** `FK_PERFORM_VAL_RATING_03`: (PA_RATING_VALUE_ID, PA_RATING_TYPE_ID) -> HRD.PA_DEF_RATING_VALUE(PA_RATING_VALUE_ID, PA_RATING_TYPE_ID) [disabled]
- **Triggers**: `PA_PERFORM_VAL_RATING_DEL` (after delete), `PA_PERFORM_VAL_RATING_INS` (before insert), `PA_PERFORM_VAL_RATING_UPD` (before update)

## HRD.PA_CPD_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| PA_PERFORM_PARAM_ID | NUMBER(12) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(2000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHED_DATE | DATE | Y |  |

- **PK** `PA_CPD_ATTACHMENT_PK`: SR_NO, PA_PERFORM_PARAM_ID, PA_PERFORM_ID
- **FK** `PA_CPD_ATTACHMENT_F2`: (PA_PERFORM_ID) -> HRD.PA_PERFORM_MASTER(PA_PERFORM_ID)
- **FK** `PA_CPD_ATTACHMENT_FK`: (PA_PERFORM_PARAM_ID) -> HRD.PA_PERFORM_VAL_RATING(PA_PERFORM_PARAM_ID)
- **Triggers**: `PA_CPD_ATTACHMENT_DEL` (after delete), `PA_CPD_ATTACHMENT_INS` (before insert), `PA_CPD_ATTACHMENT_UPD` (before update)

## HRD.PA_DEF_TEMPLATE_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_TEMPLATE_ID | NUMBER(2) | N |  |
| PA_SECTION_ID | NUMBER(2) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| ORDER_BY | NUMBER(2) default 0 | N |  |
| PA_SECTION_WEIGHTAGE | NUMBER(3) | Y |  |
| TEMPLATE_RATING_TYPE_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PA_DEF_TEMPLATE_SECTION`: PA_TEMPLATE_ID, PA_SECTION_ID
- **FK** `FK_PA_DEF_TEMPLATE_SECTION_01`: (PA_TEMPLATE_ID) -> HRD.PA_DEF_TEMPLATE(PA_TEMPLATE_ID)
- **FK** `FK_PA_DEF_TEMPLATE_SECTION_02`: (PA_SECTION_ID) -> HRD.PA_DEF_SECTION(PA_SECTION_ID) [disabled]
- **CHECK** `CHK_PA_DEF_TEMPLATE_SECTION`: ACTIVE IN ('N','Y')
- **Triggers**: `PA_DEF_TEMPLATE_SECTION_DEL` (after delete), `PA_DEF_TEMPLATE_SECTION_INS` (before insert), `PA_DEF_TEMPLATE_SECTION_UPD` (before update)

## HRD.PA_DEPT_PARAM_INDICATOR

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_DEPT_PARAM_INDICATOR`: DEPARTMENT_ID, SECTION_ID, PARAMETER_ID
- **Triggers**: `PA_DEPT_PARAM_INDICATOR_DEL` (after delete), `PA_DEPT_PARAM_INDICATOR_INS` (before insert), `PA_DEPT_PARAM_INDICATOR_UPD` (before update)

## HRD.PA_DESIG_PARAM_INDICATOR

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| SECTION_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_DESIG_PARAM_INDICATOR`: DESIGNATION_ID, SECTION_ID, PARAMETER_ID
- **Triggers**: `PA_DESIG_PARAM_INDICATOR_DEL` (after delete), `PA_DESIG_PARAM_INDICATOR_INS` (before insert), `PA_DESIG_PARAM_INDICATOR_UPD` (before update)

## HRD.PA_DESIG_PARAM_INDICATOR_EXPT

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(7) | N |  |
| SECTION_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_DESIG_PARAM_INDICATOR_EXPT`: DESIGNATION_ID, SECTION_ID, PARAMETER_ID
- **Triggers**: `PA_DES_PARM_IND_EXP_DEL` (after delete), `PA_DES_PARM_IND_EXP_INS` (before insert), `PA_DES_PARM_IND_EXP_UPD` (before update)

## HRD.PA_EMP_PARAM_INDICATOR

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| SECTION_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_EMP_PARAM_INDICATOR`: EMPLOYEE_CODE, SECTION_ID, PARAMETER_ID
- **Triggers**: `PA_EMP_PARAM_INDICATOR_DEL` (after delete), `PA_EMP_PARAM_INDICATOR_INS` (before insert), `PA_EMP_PARAM_INDICATOR_UPD` (before update)

## HRD.PA_EMP_PARAM_INDICATOR_EXPT

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| SECTION_ID | NUMBER(3) | N |  |
| PARAMETER_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PA_EMP_PARAM_INDICATOR_EXPT`: EMPLOYEE_CODE, SECTION_ID, PARAMETER_ID
- **Triggers**: `PA_EMP_PA_INDICATR_EXPT_DEL` (after delete), `PA_EMP_PA_INDICATR_EXPT_INS` (before insert), `PA_EMP_PA_INDICATR_EXPT_UPD` (before update)

## HRD.PA_INDICATOR_FINAL_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| PATPID | NUMBER(3) | N |  |
| INDICATOR_ID | NUMBER(3) | N |  |
| PA_SCORE | NUMBER | Y |  |
| PA_REF_DATA | VARCHAR2(5) | Y |  |

- **PK** `PA_INDICATOR_FINAL_DATA`: MRNO, PATPID, INDICATOR_ID
- **Triggers**: `PA_INDICATOR_FINAL_DATA_DEL` (after delete), `PA_INDICATOR_FINAL_DATA_INS` (before insert), `PA_INDICATOR_FINAL_DATA_UPD` (before update)

## HRD.PA_MASTER_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| APPRAISEE_MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| PATP_ID | NUMBER(3) | Y |  |
| TEMPLATE_ID | NUMBER(3) | Y |  |
| REPORT_NAME | VARCHAR2(200) | Y |  |
| PA_MASTER_HIERARCHY_ID | VARCHAR2(12) | N |  |
| EMP_LOCATION_ID | VARCHAR2(3) | Y |  |
| PA_MASTER_STATUS_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PA_MASTER_HIERARCHY`: PA_MASTER_HIERARCHY_ID
- **UK** `UK_PA_MASTER_HIERARCHY`: APPRAISEE_MRNO, PATP_ID
- **Triggers**: `PA_MASTER_HIERARCHY_DEL` (after delete), `PA_MASTER_HIERARCHY_INS` (before insert), `PA_MASTER_HIERARCHY_UPD` (before update)

## HRD.PA_OBJECTIVE_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_OBJECTIVE_ID | NUMBER(7) | N |  |
| PATP_ID | NUMBER(3) | Y |  |
| DESCRIPTION | VARCHAR2(1000) | N |  |
| USER_REMARKS | VARCHAR2(1000) | Y |  |
| OBJ_STATUS_ID | VARCHAR2(3) | Y |  |
| OBJECTIVE_TYPE_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| SPECIFIC | CHAR(1) default 'N' | Y |  |
| MEASURABLE | CHAR(1) default 'N' | Y |  |
| ACHIEVABLE | CHAR(1) default 'N' | Y |  |
| REALISTIC | CHAR(1) default 'N' | Y |  |
| TIME_BOUND | CHAR(1) default 'N' | Y |  |
| REVIEW_PERIOD | CHAR(1) default 'B' | Y | A= Annual, B= Bi-annual; Q = Quarterly ,M = Monthly |
| OBJ_DEFINED_BY | VARCHAR2(14) | Y |  |
| CLOSING_TYPE | CHAR(1) default 'E' | Y | 'E' = Closed by appraiser , 'S' = Closed by System |
| PA_WEIGHTAGE | NUMBER | Y |  |

- **PK** `PK_PA_OBJECTIVE`: PA_OBJECTIVE_ID
- **FK** `FK_PA_OBJECTIVE_01`: (PATP_ID) -> HRD.PA_TYPE_PERIOD(PATP_ID) [disabled]
- **FK** `FK_PA_OBJECTIVE_03`: (OBJ_STATUS_ID) -> ORDERENTRY.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_01`: SPECIFIC IN ('N','Y')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_02`: MEASURABLE IN ('N','Y')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_03`: ACHIEVABLE IN ('N','Y')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_04`: REALISTIC IN ('N','Y')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_05`: TIME_BOUND IN ('N','Y')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_06`: REVIEW_PERIOD IN ('A','B','M','Q')
- **CHECK** `CHK_PA_OBJECTIVE_MASTER_07`: CLOSING_TYPE IN ('E','S')
- **Triggers**: `PA_OBJECTIVE_MASTER_DEL` (after delete), `PA_OBJECTIVE_MASTER_INS` (before insert), `PA_OBJECTIVE_MASTER_UPD` (before update)

## HRD.PA_PEER_LOV

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_SECTION_ID | NUMBER | N |  |
| PA_PARAMETER_ID | NUMBER | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(300) | Y |  |
| PA_YEAR | VARCHAR2(4) | N |  |
| DESIGNATION | VARCHAR2(200) | Y |  |
| DEPARTMENT | VARCHAR2(200) | Y |  |

- **PK** `PK_PA_PEER_LOV`: PA_SECTION_ID, PA_PARAMETER_ID, EMPLOYEE_CODE, PA_YEAR
- **Triggers**: `PA_PEER_LOV_DEL` (after delete), `PA_PEER_LOV_INS` (before insert), `PA_PEER_LOV_UPD` (before update)

## HRD.PA_PEER_LOV_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_SECTION_ID | NUMBER(2) | N |  |
| PA_PARAMETER_ID | NUMBER(2) | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |

- **PK** `PK_PA_PEER_LOV_DESIGNATION_01`: PA_SECTION_ID, PA_PARAMETER_ID, DESIGNATION_CATEGORY_ID
- **FK** `FK_PA_PEER_LOV_DESIGNATION_01`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID) [disabled]
- **Triggers**: `PA_PEER_LOV_DESIGNATION_DEL` (after delete), `PA_PEER_LOV_DESIGNATION_INS` (before insert), `PA_PEER_LOV_DESIGNATION_UPD` (before update)

## HRD.PA_PERFORM_OBJECTIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PA_SERIAL_NO | NUMBER(5) | N |  |
| PA_OBJECTIVE_ID | NUMBER(9) | N |  |
| PA_EXPECTED_VALUE | NUMBER(3) | N |  |

- **PK** `PK_PA_PERFORM_OBJECTIVE`: PA_PERFORM_ID, PA_SERIAL_NO, PA_OBJECTIVE_ID
- **FK** `FK_PA_PERFORM_OBJECTIVE_01`: (PA_PERFORM_ID) -> HRD.PA_PERFORM_MASTER(PA_PERFORM_ID) [disabled]
- **Triggers**: `PA_PERFORM_OBJECTIVE_DEL` (after delete), `PA_PERFORM_OBJECTIVE_INS` (before insert), `PA_PERFORM_OBJECTIVE_UPD` (before update)

## HRD.PA_PERFORM_VAL_OBJ

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_PERFORM_APPRAISER_ID | NUMBER(11) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PA_SERIAL_NO | NUMBER(5) | N |  |
| PA_OBJECTIVE_ID | NUMBER(9) | N |  |
| PA_ACHIEVE_VALUE | NUMBER(3) default 0 | N |  |
| TRANS_DATE | DATE | N |  |
| PA_STATUS_ID | VARCHAR2(3) | N |  |
| VAL_OBJ_SERIAL_NO | NUMBER(11) | N |  |
| REVIEW_PERIOD_ID | CHAR(1) | Y |  |
| R_START_DATE | DATE | Y |  |
| R_END_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| MARK_DELETE | CHAR(1) default 'N' | Y |  |
| PA_ACHIEVE_VALUE_BA | NUMBER(3) | Y |  |
| PA_EXPECTED_VALUE | NUMBER(3) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| PATP_ID | NUMBER(3) | Y |  |
| OBJECTIVE_TYPE_ID | NUMBER(2) | Y |  |
| NOT_APPLICABLE | CHAR(1) | Y |  |
| IS_INDICATOR | CHAR(1) | Y |  |
| SYSTEM_ENTRY | CHAR(1) default 'N' | Y | this column will be use to cantain infortion where record entered |

- **PK** `PK_PA_PERFORM_VAL_OBJ`: VAL_OBJ_SERIAL_NO
- **UK** `UK_PA_PERFORM_VAL_OBJ_01`: PA_PERFORM_ID, PA_SERIAL_NO, PA_OBJECTIVE_ID, REVIEW_PERIOD_ID, R_START_DATE, R_END_DATE
- **FK** `FK_PA_PERFORM_VAL_OBJ_01`: (PA_PERFORM_APPRAISER_ID) -> HRD.PA_PERFORM_APPRAISER(PA_PERFORM_APPRAISER_ID) [disabled]
- **FK** `FK_PA_PERFORM_VAL_OBJ_03`: (PA_STATUS_ID) -> ORDERENTRY.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **FK** `FK_PA_PERFORM_VAL_OBJ_05`: (PA_PERFORM_ID) -> HRD.PA_PERFORM_MASTER(PA_PERFORM_ID)
- **Triggers**: `PA_PERFORM_VAL_OBJ_DEL` (after delete), `PA_PERFORM_VAL_OBJ_INS` (before insert), `PA_PERFORM_VAL_OBJ_UPD` (before update)

## HRD.PA_PERFORM_VAL_TEXT

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_SERIAL_NO | NUMBER(3) | N |  |
| PA_PERFORM_PARAM_ID | NUMBER(11) | N |  |
| PA_PERFORM_APPRAISER_ID | NUMBER(11) | Y |  |
| PA_VALUE | VARCHAR2(4000) | Y |  |
| TRANS_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| PA_VALUE_ID | VARCHAR2(14) | Y |  |
| PA_VALUE_NUMBER | VARCHAR2(10) | Y |  |
| PA_ORIGINAL_VALUE | VARCHAR2(4000) | Y |  |
| APPRAISEE_REMARKS | VARCHAR2(4000) | Y | This column will be use to store appraisee remarks |

- **PK** `PK_PA_PERFORM_VAL_TEXT`: PA_PERFORM_PARAM_ID, PA_SERIAL_NO
- **FK** `FK_PA_PERFORM_VAL_TEXT_01`: (PA_PERFORM_PARAM_ID) -> HRD.PA_PERFORM_SECTION_PARAM(PA_PERFORM_PARAM_ID)
- **FK** `FK_PA_PERFORM_VAL_TEXT_02`: (PA_PERFORM_APPRAISER_ID) -> HRD.PA_PERFORM_APPRAISER(PA_PERFORM_APPRAISER_ID)
- **Triggers**: `PA_PERFORM_VAL_TEXT_DEL` (after delete), `PA_PERFORM_VAL_TEXT_INS` (before insert), `PA_PERFORM_VAL_TEXT_UPD` (before update)

## HRD.PA_PERFORM_VAL_TEXT_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_SERIAL_NO | NUMBER(3) | N |  |
| PA_PERFORM_PARAM_ID | NUMBER(11) | N |  |
| PA_PERFORM_APPRAISER_ID | NUMBER(11) | N |  |
| PA_VALUE | VARCHAR2(1004) | Y |  |
| TRANS_DATE | DATE | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| PA_VALUE_ID | VARCHAR2(14) | Y |  |

- **PK** `PK_PA_PERFORM_VAL_TEXT_HIST`: PA_PERFORM_PARAM_ID, PA_SERIAL_NO, PA_PERFORM_APPRAISER_ID, TRANS_DATE
- **FK** `FK_PA_PERFORM_VAL_TEXT_HIST_01`: (PA_PERFORM_PARAM_ID) -> HRD.PA_PERFORM_SECTION_PARAM(PA_PERFORM_PARAM_ID)
- **FK** `FK_PA_PERFORM_VAL_TEXT_HIST_02`: (PA_PERFORM_APPRAISER_ID) -> HRD.PA_PERFORM_APPRAISER(PA_PERFORM_APPRAISER_ID) [disabled]

## HRD.PA_PORTAL_PATIENT_FEEDBACK

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_FEEDBACK_ID | NUMBER(20) | N |  |
| PA_SECTION_ID | NUMBER(2) | Y |  |
| PA_PARAMETER_ID | NUMBER(2) | Y |  |
| PA_RATING_VALUE_ID | NUMBER(3) | Y |  |
| PA_RATING_TYPE_ID | NUMBER(2) | Y |  |
| TRANS_DATE | DATE | Y |  |
| PATIENT_MRNO | VARCHAR2(14) | Y |  |
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| SR_NO | VARCHAR2(20) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_PA_PORTAL_PATIENT_FEEDBACK`: PATIENT_FEEDBACK_ID
- **FK** `FK_PA_DEF_RATING_VALUE`: (PA_RATING_VALUE_ID, PA_RATING_TYPE_ID) -> HRD.PA_DEF_RATING_VALUE(PA_RATING_VALUE_ID, PA_RATING_TYPE_ID) [disabled]
- **FK** `FK_PA_DEF_SECTION_PARAMETER`: (PA_PARAMETER_ID, PA_SECTION_ID) -> HRD.PA_DEF_SECTION_PARAMETER(PA_PARAMETER_ID, PA_SECTION_ID) [disabled]
- **Triggers**: `PA_PORTAL_PATIENT_FEEDBACK_DEL` (after delete), `PA_PORTAL_PATIENT_FEEDBACK_INS` (before insert), `PA_PORTAL_PATIENT_FEEDBACK_UPD` (before update)

## HRD.PA_QA_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_CAT_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| IS_SHOW_REPORT | CHAR(1) default 'N' | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_PA_CAT`: PA_CAT_ID
- **Triggers**: `PA_QA_CATEGORY_DEL` (after delete), `PA_QA_CATEGORY_INS` (before insert), `PA_QA_CATEGORY_UPD` (before update)

## HRD.PA_QA_MONTHLY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSULTANT_MRNO | VARCHAR2(14) | N |  |
| PA_MONTH | VARCHAR2(12) | N |  |
| PA_YEAR | NUMBER(4) | N |  |
| INDICATOR_ID | NUMBER(3) | N |  |
| SYSTEM_GENERATED_MEASURE | VARCHAR2(10) | Y |  |
| SYSTEM_GENERATED_SCORE | VARCHAR2(10) | Y |  |
| USER_DEFINED_MEASURE | VARCHAR2(10) | Y |  |
| USER_DEFINED_SCORE | VARCHAR2(10) | Y |  |
| DISPLAY_IN_PENDING_TASK | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| COMMENTS | VARCHAR2(1000) | Y |  |

- **PK** `PK_PA_QA_MONTHLY_DETAIL`: CONSULTANT_MRNO, PA_MONTH, PA_YEAR, INDICATOR_ID

## HRD.PA_QA_PARAM_TAB

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_QA_PARAM_ID | NUMBER(3) | Y |  |
| PATPID | NUMBER(3) | Y |  |
| PERFORM_ID | NUMBER(12) | Y |  |
| CONCEPT | VARCHAR2(4000) | Y |  |
| PERF_INDICATOR | VARCHAR2(4000) | Y |  |
| MEASURE_PARAMETER | VARCHAR2(4000) | Y |  |
| RATING | NUMBER(6) | Y |  |
| MEASURE | VARCHAR2(10) | Y |  |
| SCORE | VARCHAR2(10) | Y |  |
| PARENT_ID | NUMBER(3) | Y |  |
| MEASURE1 | VARCHAR2(10) | Y |  |
| SCORE1 | VARCHAR2(10) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| INDICATOR_ID | NUMBER | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

- **Triggers**: `PA_QA_PARAM_TAB_DEL` (after delete), `PA_QA_PARAM_TAB_INS` (before insert), `PA_QA_PARAM_TAB_UPD` (before update)

## HRD.PA_REFERENCE_RESEARCH_PAPER

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_REFERENCE_ID | NUMBER(10) | N |  |
| PA_SERIAL_NO | NUMBER(3) | N |  |
| PA_PERFORM_PARAM_ID | NUMBER(11) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| PA_TITLE | VARCHAR2(500) | Y |  |
| PA_NAME_OF_AUTHOR | VARCHAR2(500) | Y |  |
| PA_NAME_OF_JOURNAL | VARCHAR2(500) | Y |  |
| PA_DATE_YEAR | VARCHAR2(50) | Y |  |
| PA_PAGE_NUMBER_APPLICABLE | VARCHAR2(100) | Y |  |
| IRB_NO | VARCHAR2(20) | Y |  |
| IRB_EXEMPTED | CHAR(1) | Y | A for approved, N for not approved, C for not applicable, E for exempted |
| IRB_REASON | VARCHAR2(500) | Y |  |
| IRB_VERIFIED_STATUS | CHAR(1) | Y |  |
| IRB_VERIFIED_BY | VARCHAR2(14) | Y |  |
| IRB_VERIFIED_REMARKS | VARCHAR2(1000) | Y |  |
| STUDY_STATUS | VARCHAR2(500) | Y | This column is use to save research study status |
| PA_RESEARCH_DATE | DATE | Y | This column is use to save research study date |
| EXAM_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(500) | Y |  |
| EXAM_NAME | VARCHAR2(500) | Y |  |
| PMD | VARCHAR2(500) | Y |  |
| STUDY_NAME | VARCHAR2(500) | Y |  |
| ACTIVITY_NAME | VARCHAR2(500) | Y |  |
| CREDIT_HOURS | VARCHAR2(500) | Y |  |
| AUDIT_NAME | VARCHAR2(500) | Y |  |
| NAME | VARCHAR2(500) | Y |  |
| DESIGNATION | VARCHAR2(500) | Y |  |
| GRANT_NAME | VARCHAR2(500) | Y |  |
| AMOUNT | VARCHAR2(500) | Y |  |
| ARTICLE_NAME | VARCHAR2(500) | Y |  |
| AMOUNT_IN_MILLION | VARCHAR2(500) | Y |  |

- **PK** `PK_REFERENCE_ID`: PA_REFERENCE_ID, PA_PERFORM_PARAM_ID, PA_SERIAL_NO
- **FK** `FK_PERFORM_VAL_TEXT`: (PA_PERFORM_PARAM_ID, PA_SERIAL_NO) -> HRD.PA_PERFORM_VAL_TEXT(PA_PERFORM_PARAM_ID, PA_SERIAL_NO) [disabled]
- **Triggers**: `PA_REFERENCE_RESEARCH_PAPER_DEL` (after delete), `PA_REFERENCE_RESEARCH_PAPER_INS` (before insert), `PA_REFERENCE_RESEARCH_PAPER_UPD` (before update), `PA_REF_RES_PAPER_DEL` (after delete), `PA_REF_RES_PAPER_INS` (before insert), `PA_REF_RES_PAPER_UPD` (before update)

## HRD.PA_TNA_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| TNA_SUBJECT_ID | VARCHAR2(9) | N |  |
| PA_SECTION_ID | NUMBER(2) | N |  |
| PA_PARAMETER_ID | NUMBER(2) | N |  |
| PA_PERFORM_ID | VARCHAR2(12) | N |  |
| PA_SERIAL_NO | NUMBER(3) | Y |  |
| PA_PERFORM_PARAM_ID | NUMBER(11) | Y |  |

- **PK** `PK_TNA_DETAIL`: TNA_SUBJECT_ID, PA_SECTION_ID, PA_PARAMETER_ID, PA_PERFORM_ID
- **Triggers**: `PA_TNA_DETAIL_DEL` (after delete), `PA_TNA_DETAIL_INS` (before insert), `PA_TNA_DETAIL_UPD` (before update)

## HRD.PERSONAL_ATTRIBUTES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| ALLOTMENT_NO | NUMBER default 0 | N |  |

- **PK** `PK_PERSONAL_ATTRIBUTES`: DESIGNATION_CATEGORY_ID, MRNO
- **Triggers**: `PERSONAL_ATTRIBUTES_CEA` (before insert or update or delete), `PERSONAL_ATTRIBUTES_DEL` (after delete), `PERSONAL_ATTRIBUTES_INS` (before insert), `PERSONAL_ATTRIBUTES_UPD` (before update), `TRG_WS_HJP_GR_RH_Q` (after insert or update or delete)

## HRD.PERSON_ONCALL_LOG_SHEET

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(10) | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| ONCALL_DUTY_DATE | DATE | N |  |
| ENTRY_DATE | DATE | Y |  |
| CALLED_BY | VARCHAR2(14) | Y |  |
| CALLED_TIME | DATE | Y |  |
| CALL_SPECIFICS | CLOB | Y |  |
| CORRECTIVE_ACTION | CLOB | Y |  |

- **PK** `PK_PERSON_ONCALL_LOG_SHEET`: SERIAL_NO, EMPLOYEE_CODE, ONCALL_DUTY_DATE
- **Triggers**: `PERSON_ONCALL_LOG_SHEET_DEL` (after delete), `PERSON_ONCALL_LOG_SHEET_INS` (before insert), `PERSON_ONCALL_LOG_SHEET_UPD` (before update)

## HRD.PERSON_ONCALL_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(10) | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| AOC | CHAR(1) | Y | Administrator oncall flage |
| ROSTER_TYPE_ID | NUMBER(3) | Y |  |

- **PK** `PK_PERSON_ONCALL_SETUP`: SERIAL_NO
- **UK** `UK_PERSON_ONCALL_SETUP`: EMPLOYEE_CODE, LOCATION_ID, ROSTER_TYPE_ID
- **Triggers**: `PERSON_ONCALL_SETUP_DEL` (after delete), `PERSON_ONCALL_SETUP_INS` (before insert), `PERSON_ONCALL_SETUP_UPD` (before update)

## HRD.PICTURES

| Column | Type | Null | Comment |
|---|---|---|---|
| PIC_NAME | VARCHAR2(30) | Y |  |

- **Triggers**: `PICTURES_DEL` (after delete), `PICTURES_INS` (before insert), `PICTURES_UPD` (before update)

## HRD.PICTURE_HISTORY_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| PATIENT_MRNO | VARCHAR2(14) | Y |  |
| ENTRY_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.PIC_JOB_STOP

| Column | Type | Null | Comment |
|---|---|---|---|
| JOB_STOP | CHAR(1) | Y |  |


## HRD.POSITION_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | VARCHAR2(3) | N | Store unique position status id |
| STATUS_DESCRIPTION | VARCHAR2(60) | Y | Store position status description |
| POSITION_STATUS_LEVEL | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_POSITION_STATUS`: STATUS_ID
- **Triggers**: `POSITION_STATUS_CEA` (before insert or update or delete), `POSITION_STATUS_DEL` (after delete), `POSITION_STATUS_INS` (before insert), `POSITION_STATUS_UPD` (before update), `TRG_WS_RGW_PQ_ZH_Q` (after insert or update or delete)

## HRD.POSITION
Store information of all type of positions

| Column | Type | Null | Comment |
|---|---|---|---|
| POSITION_ID | VARCHAR2(6) | N | Store unique autogenerated position code |
| DESIGNATION_ID | VARCHAR2(6) | Y | Store designation Id associated with position id |
| DESIGNATION_DESCRIPTION | VARCHAR2(255) | Y | Store designation description associated with position |
| GRADE_FROM | VARCHAR2(6) | Y | Store grade range from which position can be started |
| GRADE_TO | VARCHAR2(6) | Y | Store grade range from which position can be upgraded |
| DEPARTMENT_ID | VARCHAR2(7) | Y | Store department id where position is created |
| DEPARTMENT_NAME | VARCHAR2(60) | Y | Store department name where position is created |
| COMMENTS | VARCHAR2(1000) | Y | Store comments against position |
| POSITION_TYPE | VARCHAR2(1) | Y | Store position type as B (Budgeted) or N (Non Budgeted) |
| SALARY_FROM | VARCHAR2(15) | Y |  |
| SALARY_TO | VARCHAR2(15) | Y |  |
| INITIATED_BY | VARCHAR2(14) | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| APPROVED_DATE | DATE | Y |  |
| ACTUAL_EMPLOYEE_ID | VARCHAR2(14) | Y |  |
| FURTHER_TYPE | CHAR(1) | Y |  |
| FURTHER_EMPLOYEE_ID | VARCHAR2(14) | Y |  |
| FURTHER_FROM_DATE | DATE | Y |  |
| FURTHER_END_DATE | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| POSITION_START_DATE | DATE | Y |  |
| POSITION_END_DATE | DATE | Y |  |
| INITIATED_DATE | DATE | Y | Store date on which position request is initiated |
| CONCERN_DEPARTMENT_APPROVAL | VARCHAR2(14) | Y | Store employee code who request for position creation or any modification in position attributes |
| CONCERN_DEPT_APP_DATE | DATE | Y | Store date on  which request for position creation or any modification in position attributes is made |
| HR_DEPARTMENT_APPROVAL | VARCHAR2(14) | Y | Store human resource department authority  who approve request for  position creation or any modification in position attributes |
| HR_DEPT_APP_DATE | DATE | Y | Store date on which human resource department authority  give approval to applied request against position |
| ACTIVE | VARCHAR2(1) | Y | Store status of position as Y for active and N for inactive |
| DESIGNATION_TYPE_ID | VARCHAR2(3) | Y |  |
| EMPLOYEE_TYPE_ID | VARCHAR2(6) | Y |  |
| POSITION_CATEGORY | VARCHAR2(20) | Y |  |
| REPLACED_MRNO | VARCHAR2(14) | Y |  |
| CATEGORY_TYPE | CHAR(1) | Y |  |
| FINANCIAL_YEAR | NUMBER(4) | Y |  |
| POSITION_LOCATION_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| FURTHER_DESIGNATION_ID | VARCHAR2(6) | Y |  |
| HIRINIG_DESIGNATION_ID | VARCHAR2(6) | Y |  |
| REQUEST_ID | NUMBER | Y |  |
| ASSIGNED_BY | VARCHAR2(14) | Y |  |
| ASSIGN_DATE | DATE | Y |  |

- **PK** `PK_POSITION`: POSITION_ID
- **UK** `UK_POSITION_1`: ACTUAL_EMPLOYEE_ID
- **FK** `FK_POSITION_1`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **FK** `FK_POSITION_10`: (REQUEST_ID) -> HRD.HIRING_REQUEST_MASTER(REQUEST_ID) [disabled]
- **FK** `FK_POSITION_2`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_POSITION_3`: (APPROVED_BY) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **FK** `FK_POSITION_4`: (ACTUAL_EMPLOYEE_ID) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_POSITION_5`: (FURTHER_EMPLOYEE_ID) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **FK** `FK_POSITION_6`: (EMPLOYEE_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_POSITION_7`: (REPLACED_MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **FK** `FK_POSITION_8`: (STATUS_ID) -> HRD.POSITION_STATUS(STATUS_ID) [disabled]
- **FK** `FK_POSITION_9`: (POSITION_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `POSITION_DEL` (after delete), `POSITION_INS` (before insert), `POSITION_UPD` (before update)

## HRD.POSITION_HIRING_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| POSITION_ID | VARCHAR2(6) | N |  |
| FILE_NAME | BLOB | Y |  |
| FILE_FULL_NAME | VARCHAR2(2000) | Y |  |
| SERIAL_NO | NUMBER | N |  |

- **PK** `PK_POSITION_HIRING_REQUEST`: POSITION_ID, SERIAL_NO
- **FK** `FK_POSITION_HIRING_REQUEST`: (POSITION_ID) -> HRD.POSITION(POSITION_ID)

## HRD.POSITION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| HISTORY_ID | VARCHAR2(18) | Y |  |
| HISTORY_DATE | DATE | Y |  |
| POSITION_ID | VARCHAR2(6) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DESIGNATION_DESCRIPTION | VARCHAR2(255) | Y |  |
| GRADE_FROM | VARCHAR2(6) | Y |  |
| GRADE_TO | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT_NAME | VARCHAR2(60) | Y |  |
| COMMENTS | VARCHAR2(1000) | Y |  |
| POSITION_TYPE | VARCHAR2(1) | Y |  |
| SALARY_FROM | VARCHAR2(15) | Y |  |
| SALARY_TO | VARCHAR2(15) | Y |  |
| INITIATED_BY | VARCHAR2(14) | Y |  |
| INITIATED_DATE | DATE | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| APPROVED_DATE | DATE | Y |  |
| ACTUAL_EMPLOYEE_ID | VARCHAR2(14) | Y |  |
| FURTHER_TYPE | VARCHAR2(1) | Y |  |
| FURTHER_EMPLOYEE_ID | VARCHAR2(14) | Y |  |
| FURTHER_FROM_DATE | DATE | Y |  |
| FURTHER_END_DATE | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| POSITION_START_DATE | DATE | Y |  |
| POSITION_END_DATE | DATE | Y |  |
| CONCERN_DEPARTMENT_APPROVAL | VARCHAR2(14) | Y |  |
| CONCERN_DEPT_APP_DATE | DATE | Y |  |
| HR_DEPARTMENT_APPROVAL | VARCHAR2(14) | Y |  |
| HR_DEPT_APP_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DESIGNATION_TYPE_ID | VARCHAR2(3) | Y |  |
| EMPLOYEE_TYPE_ID | VARCHAR2(6) | Y |  |
| DEACTIVATED_BY | VARCHAR2(14) | Y |  |
| POSITION_CATEGORY | VARCHAR2(20) | Y |  |
| REPLACED_MRNO | VARCHAR2(14) | Y |  |
| REF_POSITION_ID | VARCHAR2(6) | Y |  |
| POSITION_LOCATION_ID | VARCHAR2(3) | Y |  |

- **Triggers**: `POSITION_HISTORY_INS` (before insert)

## HRD.PREVIOUS_EMPLOYMENT_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SR_NO | NUMBER(2) | N |  |
| LEAVING_REASON_ID | NUMBER(3) | Y |  |
| DATE_FROM | DATE | Y |  |
| DATE_TO | DATE | Y |  |
| EMPLOYER | VARCHAR2(50) | Y |  |
| POSITION_HELD | VARCHAR2(30) | Y |  |
| ADDRESS | VARCHAR2(2000) | Y |  |
| TELEPHONE | VARCHAR2(15) | Y |  |

- **PK** `PK_PREVIOUS_EMPLOYMENT_HISTORY`: MRNO, SR_NO
- **Triggers**: `PREVIOUS_EMPLOYMENT_HISTORY_DEL` (after delete), `PREVIOUS_EMPLOYMENT_HISTORY_INS` (before insert), `PREVIOUS_EMPLOYMENT_HISTORY_UPD` (before update), `PREV_EMPLOYMENT_HISTORY_DEL` (after delete), `PREV_EMPLOYMENT_HISTORY_INS` (before insert), `PREV_EMPLOYMENT_HISTORY_UPD` (before update)

## HRD.PREVIOUS_HEALTH_CARE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SR_NO | NUMBER(3) | N |  |
| HEALTH_CARE_ID | NUMBER(1) | Y |  |
| CARE_DATE | DATE | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |

- **PK** `PK_PREVIOUS_HEALTH_CARE`: MRNO, SR_NO
- **Triggers**: `PREVIOUS_HEALTH_CARE_DEL` (after delete), `PREVIOUS_HEALTH_CARE_INS` (before insert), `PREVIOUS_HEALTH_CARE_UPD` (before update)

## HRD.PROBATION_REASONS
Store possible probation reason detail

| Column | Type | Null | Comment |
|---|---|---|---|
| PROBATION_REASON_ID | VARCHAR2(3) | N | Store unique probation reason code |
| DESCRIPTION | VARCHAR2(60) | Y | Store probation reason description |
| ACTIVE | VARCHAR2(1) default 'Y' | Y | Store probation reason status as Y for active and N for inactive |
| DEFAULTS | VARCHAR2(1) default 'Y' | Y | Store Y to set probation reason as default else store N |

- **PK** `PK_PROBATION_REASONS`: PROBATION_REASON_ID
- **CHECK** `CK_PROBATION_REASONS_001`: ACTIVE IN ('Y','N')
- **CHECK** `CK_PROBATION_REASONS_002`: DEFAULTS IN ('Y','N')
- **Triggers**: `PROBATION_REASONS_CEA` (before insert or update or delete), `PROBATION_REASONS_DEL` (after delete), `PROBATION_REASONS_INS` (before insert), `PROBATION_REASONS_UPD` (before update), `TRG_WS_NQZ_NX_EX_Q` (after insert or update or delete)

## HRD.PROCESS_CRITERIA

| Column | Type | Null | Comment |
|---|---|---|---|
| CRITERIA_ID | VARCHAR2(1) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |

- **PK** `PK_PROCESS_CRITERIA`: CRITERIA_ID
- **Triggers**: `PROCESS_CRITERIA_DEL` (after delete), `PROCESS_CRITERIA_INS` (before insert), `PROCESS_CRITERIA_UPD` (before update)

## HRD.PROCESS_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| PROCESS_TYPE_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_PROCESS_DEPT`: PROCESS_ID, DEPARTMENT_ID
- **Triggers**: `PROCESS_DEPT_DEL` (after delete), `PROCESS_DEPT_INS` (before insert), `PROCESS_DEPT_UPD` (before update)

## HRD.PROCESS_MESSAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(14) | Y |  |
| ATTEMPT_NO | NUMBER(12) | Y |  |
| PROCESS_DATE | DATE | Y |  |
| EVENT | VARCHAR2(2000) | Y |  |


## HRD.PROCESS_MONTH

| Column | Type | Null | Comment |
|---|---|---|---|
| CURRENT_MONTH | VARCHAR2(6) | N |  |

- **PK** `PK_PROCESS_MONTH`: CURRENT_MONTH
- **Triggers**: `PROCESS_MONTH_DEL` (after delete), `PROCESS_MONTH_INS` (before insert), `PROCESS_MONTH_UPD` (before update)

## HRD.PROCESS_MRNO

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | VARCHAR2(12) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| PROCESS_TYPE_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_PROCESS_MRNO`: PROCESS_ID, MRNO
- **FK** `FK_PROCESS_ID`: (PROCESS_ID) -> HRD.PROCESS(PROCESS_ID)
- **Triggers**: `PROCESS_MRNO_DEL` (after delete), `PROCESS_MRNO_INS` (before insert), `PROCESS_MRNO_UPD` (before update)

## HRD.PROCESS_TYPE
Store salary process types and their details

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_TYPE_ID | VARCHAR2(3) | N | Store unique process type id Ex 001, 002 |
| DESCRIPTION | VARCHAR2(60) | Y | Store process description like Regular, Final etc |
| SHORT_DESC | VARCHAR2(5) | Y | Store short description of process like  F for Final |
| ACTIVE | VARCHAR2(1) | Y | Store process type status as Y for active and N for inactive |
| CONSIDERABLE | VARCHAR2(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| EXECUTABLE | CHAR(1) | Y |  |

- **PK** `PK_PROCESS_TYPE`: PROCESS_TYPE_ID
- **CHECK** `CK_PROCESS_TYPE_001`: CONSIDERABLE IN ('N','Y')
- **Triggers**: `PROCESS_TYPE_CEA` (before insert or update or delete), `PROCESS_TYPE_DEL` (after delete), `PROCESS_TYPE_INS` (before insert), `PROCESS_TYPE_UPD` (before update), `TRG_WS_TDM_GZ_AA_Q` (after insert or update or delete)

## HRD.REGISTRATION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| REGISTRATION_TYPE_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REQUIRE_CATEGORY | CHAR(1) default 'N' | N |  |

- **PK** `PK_REGISTRATION_TYPE`: REGISTRATION_TYPE_ID
- **UK** `UK_REGISTRATION_TYPE_01`: DESCRIPTION
- **CHECK** `CHK_REGISTRATION_TYPE_01`: ACTIVE IN ('N','Y')
- **Triggers**: `REGISTRATION_TYPE_CEA` (before insert or update or delete), `REGISTRATION_TYPE_DEL` (after delete), `REGISTRATION_TYPE_INS` (before insert), `REGISTRATION_TYPE_UPD` (before update), `TRG_WS_TRI_ZS_DH_Q` (after insert or update or delete)

## HRD.REGISTRATION_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| REGISTRATION_CATEGORY_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REGISTRATION_TYPE_ID | NUMBER(5) | N |  |
| VALIDITY_PERIOD | NUMBER(6) default 0 | N | In number of days |

- **PK** `PK_REGISTRATION_CATEGORY`: REGISTRATION_CATEGORY_ID
- **UK** `UK_REGISTRATION_CATEGORY_01`: DESCRIPTION
- **FK** `FK_REGISTRATION_CATEGORY_01`: (REGISTRATION_TYPE_ID) -> HRD.REGISTRATION_TYPE(REGISTRATION_TYPE_ID) [disabled]
- **CHECK** `CHK_REGISTRATION_CATEGORY_01`: ACTIVE IN ('N','Y')

## HRD.PROFESSIONAL_REGISTRATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_CODE | VARCHAR2(14) | N | Registered employee code |
| REGISTRATION_TYPE_ID | NUMBER(5) | N |  |
| REGISTRATION_NUMBER | VARCHAR2(30) | N | Unique number assigned from registered organization |
| REGISTRATION_CATEGORY_ID | NUMBER(5) | Y |  |
| REGISTRATION_DATE | DATE | Y | Date on which license is registered from authorized registration organization |
| ISSUE_DATE | DATE | Y | Date on which license is issued to employee. |
| EXPIRY_DATE | DATE | N | Date on which license will expire. |
| ENTRY_DATE | DATE | Y | Date on which this information will enter in system |
| ENTERED_BY | VARCHAR2(14) | Y | User who save this information |
| VERIFICATION_BY | VARCHAR2(14) | Y | HR personnel who physically verify document |
| VERIFICATION_DATE | DATE | Y | Date on which HR personnel verify the document |
| REMARKS | VARCHAR2(4000) | Y | User remarks |
| DEFAULT_RECORD | CHAR(1) default 'N' | N | This flag will use for  display employee license number on different locations at HIS |
| QUALIFICATION_ID | VARCHAR2(6) | Y |  |
| OSV_STATUS | CHAR(2) default 'N' | N | OSV STATUS AS N ,                     NA,                     P,                     Pending,                     S,                     Slip Submitted,                     O,                     One Attempt,                     T,                     Two Attempts,                     TH,                     Three Attempts,                     V,                     Verified,                     R,                     Renewal Slip Submitted,                     A,                     Additional Qualification Slip Submitted |
| VALIDITY_PERIOD | NUMBER | Y | On Validate of EXPIRY_DATE it will be calculated ROUND(EXPIRY_DATE ISSUE_DATE, 0) |
| REGISTRATION_FROM | VARCHAR2(225) | Y |  |
| SUBMIT_SLIP | CHAR(1) | Y |  |
| SUBMIT_CERTIFICATE | CHAR(1) | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |
| OSV_RECEIVE_DATE | DATE | Y | This column contains OSV RECEIVE DATE |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id from LOB.DOCUMENT_STORE table |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY MRNO |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains ATTACHMENT DESCRIPTION |
| OSV_DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id for OSV from LOB.DOCUMENT_STORE table |
| OSV_ATTACHED_BY | VARCHAR2(14) | Y | This column contains ATTACHED BY  OSV MRNO |
| OSV_DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains OSV ATTACHMENT DESCRIPTION |
| CURRENT_OSV | CHAR(1) | Y | This column used to show current OSV |
| EMP_JOINING_DATE | DATE | Y | This column contains EMPLOYMENT |
| EMP_JOINING_DATE_OSV | DATE | Y | This column contains EMPLOYMENT for OSV |
| SLIP_SUBMIT_DATE | DATE | Y | this column contain information when consultant/nurses submit their new registration slip |
| OSV_SENT_DATE | DATE | Y | this coulumn contains  OSV alert sent date |
| IS_OSV_REQUIRED | CHAR(1) default 'Y' | Y | this coulumn contains  OSV CHECK Y OR N |
| UPDATED_LISCENCE_REC_DATE | DATE | Y |  |
| UPD_DOCUMENT_ID | VARCHAR2(13) | Y |  |
| UP_ATTACHED_BY | VARCHAR2(14) | Y |  |
| LICENSE_RECEIVED_DATE | DATE | Y | This column contains the Employee professional license received date. |
| PROVISIONAL_LICENSE | CHAR(1) default 'N' | Y |  |
| PROV_VALID_TILL | DATE | Y |  |
| PROVISIONAL_QUALIFICATION | VARCHAR2(4000) | Y |  |

- **PK** `PK_PROFESSIONAL_REGISTRATIONS`: EMPLOYEE_CODE, REGISTRATION_TYPE_ID, OSV_STATUS, EXPIRY_DATE
- **UK** `UK_PROFESSIONAL_REG_01`: REGISTRATION_NUMBER, EMPLOYEE_CODE, EXPIRY_DATE
- **FK** `FK_PROFESSIONAL_REG_01`: (EMPLOYEE_CODE) -> REGISTRATION.PATIENT(MRNO)
- **FK** `FK_PROFESSIONAL_REG_02`: (REGISTRATION_TYPE_ID) -> HRD.REGISTRATION_TYPE(REGISTRATION_TYPE_ID) [disabled]
- **FK** `FK_PROFESSIONAL_REG_03`: (REGISTRATION_CATEGORY_ID) -> HRD.REGISTRATION_CATEGORY(REGISTRATION_CATEGORY_ID) [disabled]
- **FK** `FK_PROFESSIONAL_REG_04`: (VERIFICATION_BY) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **CHECK** `CHK_PROFESSIONAL_REG_01`: DEFAULT_RECORD IN ('N','Y')
- **Triggers**: `PROFESSIONAL_REGISTRATIONS_DEL` (after delete), `PROFESSIONAL_REGISTRATIONS_INS` (before insert), `PROFESSIONAL_REGISTRATIONS_UPD` (before update), `PROF_REG_DOCUMENT_ID_UPD` (before insert or update of expiry_date), `PROF_REG_EXPIRY_DATE_UPD` (before insert or update of expiry_date)

## HRD.PROFESSIONAL_REGIS_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | This column contains employee code |
| REGISTRATION_TYPE_ID | NUMBER(5) | Y | This column contains registration type refrence hrd.professional_registratiions table |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document id refrence Lob.dodument_store used for attachment |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains employee code of person who attached file |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y | This column contains attacment description |
| OSV_STATUS | CHAR(2) | Y | This column contains Original source verification status |
| OSV_SLIP_RECEIVE_DATE | DATE | Y | This column contains slip receive date of OSV |
| OSV_SENT_DATE | DATE | Y | This column contains OSV sent date |
| OSV_STATUS_DET | CHAR(2) | Y | This column contains slip receive date of OSV |
| EXPIRY_DATE | DATE | N | This column contains s EXPIRY_DATE |
| SR_NO | NUMBER | N | This column contains  SR NO SERIAL NUMBER |
| ADDITIONAL_QUALIFICATION | VARCHAR2(4000) | Y | This column contains  ADDITIONAL QUALIFICATIONS |

- **PK** `PK_PROF_REGIS_1`: MRNO, SR_NO, EXPIRY_DATE
- **Triggers**: `PROF_REG_SLIP_SUBMIT` (before insert or update)

## HRD.PROFESSIONAL_REG_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(9) | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N |  |
| REGISTRATION_TYPE_ID | NUMBER(5) | N |  |
| REGISTRATION_NUMBER | VARCHAR2(30) | N |  |
| REGISTRATION_CATEGORY_ID | NUMBER(5) | Y |  |
| REGISTRATION_DATE | DATE | Y |  |
| ISSUE_DATE | DATE | Y |  |
| EXPIRY_DATE | DATE | N |  |
| ENTRY_DATE | DATE | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| VERIFICATION_BY | VARCHAR2(14) | N |  |
| VERIFICATION_DATE | DATE | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| DEFAULT_RECORD | CHAR(1) default 'N' | N |  |
| UPDATED_BY | VARCHAR2(14) | Y |  |
| UPDATION_DATE | DATE | Y |  |

- **PK** `PK_PROFESSIONAL_REG_HISTORY`: SERIAL_NO
- **Triggers**: `PROFESSIONAL_REG_HISTORY_SEQ` (before insert)

## HRD.QUERY_TABLE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(15) | N |  |
| MRNO | VARCHAR2(20) | N |  |
| DATE_TIME | DATE | N |  |
| NO_OF | NUMBER | Y |  |

- **PK** `PK_QT`: SERIAL_NO, MRNO, DATE_TIME

## HRD.REEMPLOYMENT
Store employee codes who are reemployed in organization

| Column | Type | Null | Comment |
|---|---|---|---|
| OLD_MRNO | VARCHAR2(14) | N | Store old employee code after reemployment |
| NEW_MRNO | VARCHAR2(14) | N | Store new employee code after reemployment |

- **PK** `PK_REEMPLOYMENT`: OLD_MRNO, NEW_MRNO
- **Triggers**: `REEMPLOYMENT_DEL` (after delete), `REEMPLOYMENT_INS` (before insert), `REEMPLOYMENT_UPD` (before update)

## HRD.REFERENCES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SR_NO | NUMBER(1) | N |  |
| NAME | VARCHAR2(30) | Y |  |
| DESIGNATION | VARCHAR2(30) | Y |  |
| ADDRESS | VARCHAR2(2000) | Y |  |
| TELEPHONE | VARCHAR2(15) | Y |  |
| REFERENCE_TYPE | NUMBER(1) | Y |  |

- **PK** `PK_REFERENCES`: MRNO, SR_NO
- **Triggers**: `REFERENCES_DEL` (after delete), `REFERENCES_INS` (before insert), `REFERENCES_UPD` (before update)

## HRD.REGISTRATION_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| REGISTRATION_TYPE_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| USER_REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_REGISTRATION_DESIGNATION`: DESIGNATION_CATEGORY_ID, REGISTRATION_TYPE_ID
- **FK** `FK_REGISTRATION_DESIGNATION_01`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID)
- **FK** `FK_REGISTRATION_DESIGNATION_02`: (REGISTRATION_TYPE_ID) -> HRD.REGISTRATION_TYPE(REGISTRATION_TYPE_ID) [disabled]
- **Triggers**: `REGISTRATION_DESIGNATION_CEA` (before insert or update or delete), `REGISTRATION_DESIGNATION_DEL` (after delete), `REGISTRATION_DESIGNATION_INS` (before insert), `REGISTRATION_DESIGNATION_UPD` (before update), `TRG_WS_TXB_ZV_ZX_Q` (after insert or update or delete)

## HRD.RELATIVE_IN_HOSPITAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| RELATION_ID | NUMBER(3) | Y |  |
| RELATIVE_MRNO | VARCHAR2(9) | Y |  |

- **PK** `PK_RELATIVE_IN_HOSPITAL`: MRNO
- **Triggers**: `RELATIVE_IN_HOSPITAL_DEL` (after delete), `RELATIVE_IN_HOSPITAL_INS` (before insert), `RELATIVE_IN_HOSPITAL_UPD` (before update)

## HRD.RESIGNED_EMP_PENDING_TASK_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| RESIGNED_EMP_CODE | VARCHAR2(14) | N |  |
| IN_QUEUE_EMP_CODE | VARCHAR2(14) | N |  |
| RESIGNATION_DATE | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| SUBSTITUTE_END_DATE | DATE | Y |  |
| IN_QUEUE_EMP_TYPE | CHAR(1) | Y | S = Substitute, V = Supervisor, H = HOD/Division Head |
| SUBSTITUTE_TYPE | CHAR(1) | Y | Type of substitute. |
| IS_SUBSTITUTE_REQ | CHAR(1) | Y | Y = Substitute required, N = Not required |
| REMARKS | VARCHAR2(2000) | Y |  |
| STATUS | CHAR(1) | Y | P = Pending, C = Completed |
| SUBSTITUTE_FROM_DATE | DATE | Y |  |

- **PK** `PK_RESIGNED_EMP_PENDING_TASK_Q`: RESIGNED_EMP_CODE, IN_QUEUE_EMP_CODE
- **Triggers**: `RESIGNED_EMP_PEND_TASK_Q_DEL` (after delete), `RESIGNED_EMP_PEND_TASK_Q_INS` (after insert), `RES_EMP_PENDING_TASK_Q_DEL` (after delete), `RES_EMP_PENDING_TASK_Q_INS` (before insert), `RES_EMP_PENDING_TASK_Q_UPD` (after update), `SUBSTITUTE_UPDATE_Q` (after update)

## HRD.RESIGNED_EMP_QUEUE_HIERACHY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| HOD_EMP_CODE | VARCHAR2(14) | Y |  |
| DIVISION_HEAD_CODE | VARCHAR2(14) | Y |  |
| SUPERVISOR_CODE | VARCHAR2(14) | Y |  |

- **Triggers**: `RES_EMP_QUEUE_HIERACHY_DEL` (after delete), `RES_EMP_QUEUE_HIERACHY_INS` (before insert), `RES_EMP_QUEUE_HIERACHY_UPD` (before update)

## HRD.RES_EMP_PENDING_TASK_Q_HIS

| Column | Type | Null | Comment |
|---|---|---|---|
| RESIGNED_EMP_CODE | VARCHAR2(14) | Y |  |
| IN_QUEUE_EMP_CODE | VARCHAR2(14) | Y |  |
| RESIGNATION_DATE | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| SUBSTITUTE_END_DATE | DATE | Y |  |
| IN_QUEUE_EMP_TYPE | CHAR(1) | Y |  |
| SUBSTITUTE_TYPE | CHAR(1) | Y |  |
| IS_SUBSTITUTE_REQ | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| STATUS | CHAR(1) | Y |  |
| SUBSTITUTE_FROM_DATE | DATE | Y |  |
| DML_STATUS | VARCHAR2(3) | Y |  |

_No standard audit columns._


## HRD.ROLE_AUTHORITY
Define leave privileges in accordance with leave type

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVE_ROLE_ID | VARCHAR2(3) | N | Define leave role id |
| LEAVE_TYPE_ID | VARCHAR2(3) | N | Define leave type ex 016 for earned leave |
| ACTIVE | CHAR(1) | Y | Define leave role id status as Y for active and N for inactive |
| LEAVE_AUTHORY_ID | CHAR(3) | N | Define leave authority id Ex 001 for Recommendation |
| LEAVE_BAL | NUMBER(10) | Y |  |

- **PK** `PK_ROLE_AUTHORITY`: LEAVE_ROLE_ID, LEAVE_TYPE_ID
- **FK** `FK_ROLE_AUTHORITY_1`: (LEAVE_ROLE_ID) -> HRD.LEAVE_ROLE(LEAVE_ROLE_ID)
- **FK** `FK_ROLE_AUTHORITY_2`: (LEAVE_AUTHORY_ID) -> HRD.LEAVE_AUTHORY(LEAVE_AUTHORY_ID) [disabled]
- **Triggers**: `ROLE_AUTHORITY_CEA` (before insert or update or delete), `TRG_WS_QTB_HC_NQ_Q` (after insert or update or delete)

## HRD.ROSTER_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| FORTNIGHTLY_OFF | DATE | Y |  |
| WEEKLY_OFF_ID | VARCHAR2(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| SAVED_FLAG | VARCHAR2(1) default 'N' | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(6) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ROSTER_PARAMETERS`: MRNO, SERIAL_NO
- **UK** `UK_ROSTER_PARAMETERS_1`: MRNO, FROM_DATE
- **CHECK** `CK_ROSTER_PARAMETERS_001`: SAVED_FLAG IN ('Y','N')
- **Triggers**: `ROSTER_PARAMETERS_DEL` (after delete), `ROSTER_PARAMETERS_INS` (before insert), `ROSTER_PARAMETERS_UPD` (before update)

## HRD.ROSTER_PARAMETERS_OLD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| FORTNIGHTLY_OFF | DATE | Y |  |
| WEEKLY_OFF_ID | VARCHAR2(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |
| SAVED_FLAG | VARCHAR2(1) | Y |  |

- **Triggers**: `ROSTER_PARAMETERS_OLD_DEL` (after delete), `ROSTER_PARAMETERS_OLD_INS` (before insert), `ROSTER_PARAMETERS_OLD_UPD` (before update)

## HRD.SALARY_CAP_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| SALARY_CAP_ID | VARCHAR2(9) | N |  |
| DESIGNATION_ID | VARCHAR2(9) | N |  |
| FROM_DATE | DATE | N |  |
| TO_DATE | DATE | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SALARY_CAP | NUMBER | Y |  |

- **PK** `PK_GL_DIVISION_LOC_HEADS`: DESIGNATION_ID, FROM_DATE, TO_DATE
- **FK** `UK_DSIGNATION_ID`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **Triggers**: `SALARY_CAP_DESIGNATION_DEL` (after delete), `SALARY_CAP_DESIGNATION_INS` (before insert), `SALARY_CAP_DESIGNATION_UPD` (before update)

## HRD.SALARY_CERTIFICATE

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH | VARCHAR2(6) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| PROCESS_ID | VARCHAR2(12) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ACTUAL_WORKING_DAYS | NUMBER(5) | Y |  |
| DAYS_PERFORMED | NUMBER(5) | Y |  |
| ADDITIONAL_WORKING_DAYS | NUMBER(5) | Y |  |
| UNPAID_LEAVES | NUMBER(5) | Y |  |
| ACTUAL_SHIFT_MINUTES | NUMBER(8) | Y |  |
| PERFORMED_MINUTES | NUMBER(8) | Y |  |
| CALCULATED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| APPROVED_OVERTIME_MINUTES | NUMBER(8) | Y |  |
| PROPER_SWIPES | NUMBER(5) | Y |  |
| IMPROPER_SWIPES | NUMBER(5) | Y |  |
| NO_SWIPES | NUMBER(5) | Y |  |
| LATE_COMING | NUMBER(5) | Y |  |
| AVG_ARRIVAL_OFFSET_MINUTES | NUMBER(9) | Y |  |
| EARLY_LEAVING | NUMBER(5) | Y |  |
| AVG_LEAVING_OFFSET_MINUTES | NUMBER(9) | Y |  |
| USERID | VARCHAR2(10) | Y |  |
| LEAVE_DAYS | NUMBER(4) | Y |  |
| NIGHTS | NUMBER(4) | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| MANUAL | CHAR(1) default 'N' | Y |  |
| ON_CALL_DAYS | NUMBER(4) | Y |  |
| ON_CALL_ALLOWANCE | NUMBER(12,2) | Y |  |
| SALARY_START_DATE | DATE | N |  |
| SALARY_END_DATE | DATE | N |  |
| PAYROLL_LOCATION_ID | VARCHAR2(3) | Y | THIS COLUMN WILL BE USE FOR PARENT PAYROLL LOCATION ID |
| EMP_LOCATION_ID | VARCHAR2(3) | Y | THIS COLUMN WILL BE USE FOR EMPLOYEE POSITION LOCATION_ID |
| LOGIN_LOCATION_ID | VARCHAR2(3) | Y | THIS COLUMN WILL BE USE FOR LOGIN LOCATION ID |
| ABSENT | NUMBER(4) | Y |  |
| OVERTIME_MONTH_ID | VARCHAR2(6) | Y | 'This column will use for overtime calculation payment |

- **PK** `PK_SALARY_CERTIFICATE`: MONTH, MRNO
- **FK** `FK_SALARY_CERTIFICATE_2`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **CHECK** `CK_SALARY_CERTIFICATE_001`: MANUAL IN ('Y','N')
- **CHECK** `CK_SALARY_CERTIFICATE_002`: CARD_SWIPE_EXEMPTION IN ('Y','N', 'O')
- **Triggers**: `SALARY_CERTIFICATE_DEL` (after delete), `SALARY_CERTIFICATE_INS` (before insert), `SALARY_CERTIFICATE_UPD` (before update), `SC_INS_UPD_LIMIT` (before insert or update of actual_shift_minutes, performed_minutes, calculated_overtime_minutes, approved_overtime_minutes)

## HRD.SEPRATE_MRNO_EXCEPTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ENTRY_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.SEPRATE_MRNO_REJOINERS_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | N |  |
| PATIENT_CODE | VARCHAR2(14) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |
| STATUS | CHAR(1) default 'I' | Y | I in-process C completed |

- **PK** `PK_QUEUE_01`: EMP_CODE
- **Triggers**: `SEP_MRNO_REJOINERS_Q_DEL` (after delete), `SEP_MRNO_REJOINERS_Q_INS` (before insert), `SEP_MRNO_REJOINERS_Q_UPD` (before update)

## HRD.SERVICE_BOND_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_ID | NUMBER | N |  |
| TRAINING_ID | VARCHAR2(9) | N |  |
| NOMINEES_MRNO | VARCHAR2(14) | N |  |
| IN_QUEUE_OF | VARCHAR2(14) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_ACKNOWLEDGE | CHAR(1) | Y |  |
| ACKNOWLEDGE_BY | VARCHAR2(14) | Y |  |
| ACKNOWLEDGE_DATE | DATE | Y |  |

- **PK** `PK_BOND_SERV_01`: QUEUE_ID, TRAINING_ID, IN_QUEUE_OF, NOMINEES_MRNO
- **Triggers**: `SERVICE_BOND_QUEUE_DEL` (after delete), `SERVICE_BOND_QUEUE_HISTORY_DEL` (after delete), `SERVICE_BOND_QUEUE_INS` (before insert), `SERVICE_BOND_QUEUE_UPD` (before update)

## HRD.SHIFT_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| SHIFT_DATE | DATE | N |  |
| SHIFT_ID | VARCHAR2(2) | N |  |
| SHIFT_START_TIME | DATE | N |  |
| SHIFT_END_TIME | DATE | N |  |
| SHIFT_TIME | NUMBER(5) | Y |  |
| RAMZAN | VARCHAR2(1) default 'N' | Y |  |
| SHIFT_LOWER_LIMIT | DATE | Y |  |
| SHIFT_UPPER_LIMIT | DATE | Y |  |
| SHIFT_LATE_ARRIVAL_MINUTES | NUMBER(3) default 0 | Y |  |
| SHIFT_EARLY_LEAVE_MINUTES | NUMBER(3) default 0 | Y |  |
| NIGHT | NUMBER(1) default 0 | Y |  |

- **PK** `PK_SHIFT_DAYS`: SHIFT_DATE, SHIFT_ID
- **FK** `FK_SHIFT_DAYS_1`: (SHIFT_ID) -> HRD.SHIFT(SHIFT_ID)
- **CHECK** `CHK_SHIF_DAYS_1`: SHIFT_DATE = TRUNC(SHIFT_DATE)
- **CHECK** `CK_SHIFT_DAYS_001`: RAMZAN IN ('Y','N')
- **Triggers**: `SHIFT_DAYS_DEL` (after delete), `SHIFT_DAYS_INS` (before insert), `SHIFT_DAYS_UPD` (before update)

## HRD.SHIFT_TIMING
Store shift id allowance with in a day

| Column | Type | Null | Comment |
|---|---|---|---|
| SHIFT_ID | VARCHAR2(2) | Y | Store shift id like  M, R, ME |
| MORNING | CHAR(1) | Y | Store Y if shift allow in morning else store N |
| EVENING | CHAR(1) | Y | Store Y if shift allow in evening else store N |
| NIGHT | CHAR(1) | Y | Store Y if shift allow in night else store N |


## HRD.SIGNATURE_PIC

| Column | Type | Null | Comment |
|---|---|---|---|
| SIG_PIC | BLOB | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y | This column contains location. |
| IS_DEFAULT | CHAR(1) | Y | This column contains DEFAULT signature for all location. Y for Yes and N for No |
| FROM_DATE | DATE | Y | This column contains Sign from date. |
| TO_DATE | DATE | Y | This column contains Sign to date.. |
| SIGNATURE_ID | VARCHAR2(7) default '0010001' | N |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SIGNATURE_TYPE | CHAR(2) default 'HR' | Y | The HR signature type will be designated for Human Resources, while the DR signature type will be used for Duty Roster signature |

- **PK** `PK_SIGNATURE_PIC`: SIGNATURE_ID
- **CHECK** `CHK_DEFAULT`: IS_DEFAULT IN ('Y','N')
- **Triggers**: `SIGNATURE_PIC_DEL` (after delete), `SIGNATURE_PIC_INS` (before insert), `SIGNATURE_PIC_UPD` (before update)

## HRD.SI_DEPT_COMPARISON

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| PA_QA_ID | NUMBER(5) | Y |  |
| PA_QA_DESCRIPTION | VARCHAR2(400) | Y |  |
| PA_PA_SCORE_PER | NUMBER(5,2) | Y |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| PATP_ID | NUMBER(10) | Y |  |

- **Triggers**: `SI_DEPT_COMPARISON_DEL` (after delete), `SI_DEPT_COMPARISON_INS` (before insert), `SI_DEPT_COMPARISON_UPD` (before update)

## HRD.SLAB_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SLAB_SETUP_ID | NUMBER(5) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MIN_SALARY | NUMBER(8) | Y |  |
| MAX_SALARY | NUMBER(8) | Y |  |
| CONTRIBUTION | NUMBER(5) | Y |  |
| DEDUCTION | NUMBER(5) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y | It may contain values lik Y for Active, N for In Active |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| SSC_ZONE_ID | NUMBER | Y |  |

- **PK** `PK_SLAB_SETUP`: SLAB_SETUP_ID
- **Triggers**: `SLAB_SETUP_DEL` (after delete), `SLAB_SETUP_INS` (before insert), `SLAB_SETUP_UPD` (before update)

## HRD.SLAB_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SLAB_SETUP_ID | NUMBER(5) | N |  |
| EMPLOYEE_TYPE_ID | VARCHAR2(10) | N |  |
| MIN_MONTHS | NUMBER(2) | Y |  |

- **PK** `PK_SLAB_SETUP_DETAIL`: SLAB_SETUP_ID, EMPLOYEE_TYPE_ID
- **FK** `FK_SLAB_SETUP_DETAIL_1`: (SLAB_SETUP_ID) -> HRD.SLAB_SETUP(SLAB_SETUP_ID)

## HRD.SOCIAL_MEDIA_APP

| Column | Type | Null | Comment |
|---|---|---|---|
| SOCIAL_APP_ID | NUMBER | N |  |
| PLATFORM_NAME | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ICON | BLOB | Y |  |

- **PK** `PK_SOCIAL_MEDIA_APP`: SOCIAL_APP_ID
- **Triggers**: `SOCIAL_MEDIA_APP_DEL` (after delete), `SOCIAL_MEDIA_APP_INS` (before insert), `SOCIAL_MEDIA_APP_UPD` (before update)

## HRD.SPECIAL_CTO

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| SR_NO | NUMBER(3) | N |  |
| WORKING_DATE | DATE | Y |  |
| WORKING_HOUR | NUMBER(2) | Y |  |
| UNIT | CHAR(1) | Y |  |

- **PK** `PK_SPECIAL_CTO`: MRNO, SERIAL_NO, SR_NO
- **FK** `FK_SPECIAL_CTO`: (MRNO, SERIAL_NO) -> HRD.EMPLOYEE_LEAVES(MRNO, SERIAL_NO)

## HRD.SPI_ALLOWANCES_DEPT_NATURE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCE_ID | NUMBER | N |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_SPI_ALLOWANCES_DEPT_NATURE_01`: ALLOWANCE_ID, DEPARTMENT_NATURE_ID
- **Triggers**: `SPI_ALLOWANCES_DEPT_NATURE_DEL` (after delete), `SPI_ALLOWANCES_DEPT_NATURE_INS` (before insert), `SPI_ALLOWANCES_DEPT_NATURE_UPD` (before update)

## HRD.SPI_ALLOWANCES_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCE_ID | NUMBER | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SPI_DESIG_01`: ALLOWANCE_ID, DESIGNATION_ID
- **Triggers**: `SPI_ALLOWANCES_DESIGNATION_DEL` (after delete), `SPI_ALLOWANCES_DESIGNATION_INS` (before insert), `SPI_ALLOWANCES_DESIGNATION_UPD` (before update)

## HRD.SPI_ALLOWANCES_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCE_ID | NUMBER | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SPI_EMP_01`: ALLOWANCE_ID, EMP_CODE

## HRD.SPI_ALLOWANCES_EMP_EXEMPT

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCE_ID | NUMBER | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SPI_EMP_EXPT1`: ALLOWANCE_ID, EMP_CODE
- **Triggers**: `SPI_ALLOWANCES_EMP_EXEMPT_DEL` (after delete), `SPI_ALLOWANCES_EMP_EXEMPT_INS` (before insert), `SPI_ALLOWANCES_EMP_EXEMPT_UPD` (before update)

## HRD.SPI_ALLOWANCES_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCES_ID | NUMBER | N |  |
| ALLOWANCES_TYPE | CHAR(1) | Y |  |
| ALLOWANCES_DESC | VARCHAR2(2000) | Y |  |
| ALLOWANCES_AMOUNT | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| IS_DEFAULT | CHAR(1) default 'N' | Y |  |
| ELIGIBILITY_DURATION | NUMBER(4) | Y | Duration should be in months (eligible from the date of joining) |
| INELIGIBILITY_DURATION | NUMBER(4) | Y | Duration should be in months |
| ALLOWANCE_INTERVAL | NUMBER(4) | Y | Number of months between each allowance payment (e.g., 3 means pay after every 3 months) |
| ELIGIBILITY_DURATION_TYPE | CHAR(1) | Y |  |

- **PK** `SPI_ALLOWANCES_SETUP_PK`: ALLOWANCES_ID
- **Triggers**: `SPI_ALLOWANCES_SETUP_DEL` (after delete), `SPI_ALLOWANCES_SETUP_INS` (before insert), `SPI_ALLOWANCES_SETUP_UPD` (before update)

## HRD.SPI_ALLOWANCE_DETAILS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| ALLOWANCES_ID | NUMBER | N |  |
| INCENTIVE_START_DATE | DATE | N |  |
| LAST_INCENTIVE_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(3000) | Y |  |
| ALLOWANCE_STATUS | CHAR(1) | Y |  |
| EXEMPTION_REASON | VARCHAR2(2000) | Y |  |
| INCENTIVE_GIVEN_BY | VARCHAR2(14) | Y |  |
| INCENTIVE_GIVEN_DATE | DATE | Y |  |
| ALLOWANCE_AMOUNT | NUMBER | Y |  |

- **PK** `SPI_ALLOWANCE_DETAILS_PK`: MRNO, INCENTIVE_START_DATE, ALLOWANCES_ID
- **Triggers**: `SPI_ALLOWANCE_DETAILS_DEL` (after delete), `SPI_ALLOWANCE_DETAILS_INS` (before insert), `SPI_ALLOWANCE_DETAILS_UPD` (before update)

## HRD.SP_HIERARCHY_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `SP_HIERARCHY_SETUP_DEL` (after delete), `SP_HIERARCHY_SETUP_INS` (before insert), `SP_HIERARCHY_SETUP_UPD` (before update)

## HRD.SP_INSTRUCTOR

| Column | Type | Null | Comment |
|---|---|---|---|
| LECTURE_INSTRUCTOR | VARCHAR2(14) | N |  |

- **PK** `PK_SP_INSTRUCTOR`: LECTURE_INSTRUCTOR
- **FK** `FK_SP_INSTRUCTOR_01`: (LECTURE_INSTRUCTOR) -> REGISTRATION.PATIENT(MRNO)
- **Triggers**: `SP_INSTRUCTOR_DEL` (after delete), `SP_INSTRUCTOR_INS` (before insert), `SP_INSTRUCTOR_UPD` (before update)

## HRD.SSC_CALCULATION

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_START | DATE | N |  |
| MONTH_END | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| SALARY | NUMBER(8) | Y |  |
| SSC_AMOUNT | NUMBER(8) | Y |  |
| DEDUCTION | NUMBER(5) | Y |  |
| NET_CONTRIBUTION | NUMBER(5) | Y |  |
| INCLUDE | VARCHAR2(1) default 'N' | Y |  |
| POST | VARCHAR2(1) | Y |  |
| SETUP_ID | NUMBER(5) | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(3) | Y |  |
| DUTY_LOCATION | VARCHAR2(150) | Y |  |
| MIN_WAGE_AMOUNT | NUMBER(8) | Y |  |
| INFLATION_AMOUNT | NUMBER(8) | Y |  |
| MERIT_AMOUNT | NUMBER(8) | Y |  |
| SSC_ZONE_ID | NUMBER | Y |  |

- **PK** `PK_SSC_CALCULATION`: MONTH_START, MONTH_END, MRNO
- **Triggers**: `SSC_CALCULATION_DEL` (after delete), `SSC_CALCULATION_INS` (before insert), `SSC_CALCULATION_UPD` (before update)

## HRD.SSC_CALCULATION_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MONTH_START | DATE | Y |  |
| MONTH_END | DATE | Y |  |
| SETUP_ID | NUMBER(5) | Y |  |
| STATUS | CHAR(1) default 'S' | Y | 'S' = SAVED, 'P' = POSTED |
| POST_DATE | DATE | Y |  |
| POSTED_BY | VARCHAR2(14) | Y |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| VOUCHER_NO | VARCHAR2(13) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| SSC_ZONE_ID | NUMBER | Y |  |
| PROCESS_LOCATION_ID | VARCHAR2(3) | Y |  |

- **FK** `FK_SSC_CALCULATION_MASTER_1`: (SETUP_ID) -> HRD.SLAB_SETUP(SLAB_SETUP_ID) [disabled]
- **Triggers**: `SSC_CALCULATION_MASTER_DEL` (after delete), `SSC_CALCULATION_MASTER_INS` (before insert), `SSC_CALCULATION_MASTER_UPD` (before update)

## HRD.SSC_ZONE_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| ZONE_ID | NUMBER | N |  |
| LOCATION_ID | VARCHAR2(2000) | N |  |
| LOCATION_DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `SSC_ZONE_SETUP_DETAIL_PK`: ZONE_ID, LOCATION_ID
- **Triggers**: `SSC_ZONE_SETUP_DETAIL_DEL` (after delete), `SSC_ZONE_SETUP_DETAIL_INS` (before insert), `SSC_ZONE_SETUP_DETAIL_UPD` (before update)

## HRD.STUDY_PROGRAM_NOMINEES

| Column | Type | Null | Comment |
|---|---|---|---|
| PROGRAM_ID | VARCHAR2(10) | Y |  |
| SP_SESSION_ID | NUMBER(6) | Y |  |
| SPS_SUBJECT_ID | NUMBER(6) | Y |  |
| SPSS_LECTURE_ID | NUMBER(6) | Y |  |
| NOMINEE_MRNO | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REASON_FOR_NOMINATION | VARCHAR2(1000) | Y |  |
| SR_NO | NUMBER(14) | N |  |

- **PK** `PK_STUDY_PROGRAM_NOMINEES`: SR_NO
- **FK** `FK_STUDY_LECTURE`: (SPSS_LECTURE_ID) -> HRD.SPSS_LECTURES(SPSS_LECTURE_ID) [disabled]
- **FK** `FK_STUDY_PROGRAM`: (PROGRAM_ID) -> HRD.STUDY_PROGRAMS(PROGRAM_ID) [disabled]
- **FK** `FK_STUDY_SESSION_ID`: (SP_SESSION_ID) -> HRD.SP_SESSION(SP_SESSION_ID) [disabled]
- **FK** `FK_STUDY_SUBJECT`: (SPS_SUBJECT_ID) -> HRD.SPS_SUBJECTS(SPS_SUBJECT_ID) [disabled]
- **Triggers**: `STUDY_PROGRAM_NOMINEES_BEF_INS` (before insert), `STUDY_PROGRAM_NOMINEES_DEL` (after delete), `STUDY_PROGRAM_NOMINEES_INS` (before insert), `STUDY_PROGRAM_NOMINEES_UPD` (before update)

## HRD.STUDY_SCALE

| Column | Type | Null | Comment |
|---|---|---|---|
| SCALE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(180) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_STUDY_SCALE`: SCALE_ID
- **Triggers**: `STUDY_SCALE_CEA` (before insert or update or delete), `STUDY_SCALE_DEL` (after delete), `STUDY_SCALE_INS` (before insert), `STUDY_SCALE_UPD` (before update), `TRG_WS_ATU_XY_KG_Q` (after insert or update or delete)

## HRD.STUDY_SCALE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SCALE_VALUE_ID | VARCHAR2(10) | N |  |
| SCALE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(180) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_STUDY_SCALE_DETAIL`: SCALE_VALUE_ID
- **FK** `FK_STUDY_SCALE_DETAIL_1`: (SCALE_ID) -> HRD.STUDY_SCALE(SCALE_ID) [disabled]
- **Triggers**: `STUDY_SCALE_DETAIL_DEL` (after delete), `STUDY_SCALE_DETAIL_INS` (before insert), `STUDY_SCALE_DETAIL_UPD` (before update)

## HRD.SUMMARY_PROCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| SUMMARY_PROCESS_ID | VARCHAR2(10) | N |  |
| SUMMARY_PROCESS_DATE | DATE | Y |  |
| SUMMARY_PROCESS_TO_DATE | DATE | Y |  |
| SUMMARY_PROCESS_FROM_DATE | DATE | Y |  |
| PROCESS_ID | VARCHAR2(12) | Y |  |

- **PK** `PK_SUMMARY_PROCESS`: SUMMARY_PROCESS_ID
- **FK** `FK_SUMMARY_PROCESS_1`: (PROCESS_ID) -> HRD.PROCESS(PROCESS_ID)
- **Triggers**: `SUMMARY_PROCESS_DEL` (after delete), `SUMMARY_PROCESS_INS` (before insert), `SUMMARY_PROCESS_UPD` (before update)

## HRD.SYMPOSIUM

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(12) | N |  |
| FIRST_NAME | VARCHAR2(60) | N |  |
| MIDDLE_NAME | VARCHAR2(60) | Y |  |
| LAST_NAME | VARCHAR2(60) | Y |  |
| SEX | NUMBER(1) | Y |  |
| DEPARTMENT | VARCHAR2(300) | Y |  |
| INSTITUTE | VARCHAR2(300) | Y |  |
| ADDRESS | VARCHAR2(500) | Y |  |
| CITY | VARCHAR2(60) | Y |  |
| COUNTRY | VARCHAR2(100) | Y |  |
| CONTACT_NO_HOME | VARCHAR2(100) | Y |  |
| CONTACT_NO_MOBILE | VARCHAR2(100) | Y |  |
| EMAIL_ADDRESS | VARCHAR2(100) | Y |  |
| ABSTRACT_ATTACHED | CHAR(1) default 'N' | N |  |
| ABSTRACT_PATH | VARCHAR2(500) | Y |  |
| REGISTRATION_DATE | DATE | N |  |
| DOCUMENT_SERVER_NAME | VARCHAR2(100) | Y |  |
| ABSTRACT_NAME | VARCHAR2(1000) | Y |  |
| PASSWORD | VARCHAR2(100) | Y |  |
| SYMPOSIUM_TYPE_ID | VARCHAR2(3) | Y |  |
| SAL_ID | NUMBER(1) | Y |  |
| PMDC_NO | VARCHAR2(30) | Y |  |
| PARTICIPATION_TYPE | CHAR(1) default 'P' | Y | P:Physical, V:Virtual |

- **PK** `PK_SYMPOSIUM`: SERIAL_NO
- **FK** `FK_SYMPOSIUM_1`: (SYMPOSIUM_TYPE_ID) -> HRD.DEF_SYMPOSIUM_TYPE(SYMPOSIUM_TYPE_ID) [disabled]

## HRD.SYSTEM_CONSTANTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(10000) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| MODULE_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PURPOSE | VARCHAR2(4000) | Y |  |
| IS_LOCATION | CHAR(1) | Y |  |

- **PK** `SYSTEM_CONSTANTS_PK`: CONSTANT_ID
- **Triggers**: `SYSTEM_CONSTANTS_DEL` (after delete), `SYSTEM_CONSTANTS_INS` (before insert), `SYSTEM_CONSTANTS_UPD` (before update)

## HRD.SYSTEM_CONSTANTS_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CONSTANT_ID | NUMBER(4) | Y |  |
| VALUE | VARCHAR2(2000) | Y |  |
| BACKEND_SOURCE | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **FK** `SYSTEM_CONSTANTS_FK`: (CONSTANT_ID) -> HRD.SYSTEM_CONSTANTS(CONSTANT_ID)
- **Triggers**: `SYSTEM_CONSTANTS_DETAIL_DEL` (after delete), `SYSTEM_CONSTANTS_DETAIL_INS` (before insert), `SYSTEM_CONSTANTS_DETAIL_UPD` (before update)

## HRD.TEMP_ACTIVE_DIRECTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| EMAIL | VARCHAR2(400) | Y |  |
| MRNO | VARCHAR2(100) | Y |  |
| STATUS | VARCHAR2(15) | Y |  |

_No standard audit columns._


## HRD.TEMP_ATTENDANCE_SHEET

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TEMP_BAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(80) | Y |  |
| DESIGNATION | VARCHAR2(80) | Y |  |
| DEPARTMENT | VARCHAR2(80) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| OPENING_BALANCE | NUMBER | Y |  |
| CLOSING_BALANCE | NUMBER | Y |  |
| LAPSED_LEAVE | NUMBER | Y |  |
| AVAILED_LEAVE | NUMBER | Y |  |
| REMARKS | VARCHAR2(100) | Y |  |
| ADDED_LEAVE | NUMBER | Y |  |

_No standard audit columns._


## HRD.TEMP_CONSULTANT_COMPARISON

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| PA_QA_ID | NUMBER(5) | Y |  |
| PA_QA_DESCRIPTION | VARCHAR2(400) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| PA_SCORE_PER | NUMBER(5,2) | Y |  |
| COMPARISON_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TEMP_CUNSULTANT_SCORE_DEP

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| PA_QA_ID | NUMBER(5) | Y |  |
| PA_QA_DESCRIPTION | VARCHAR2(400) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| PA_SCORE_PER | NUMBER(5,2) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._


## HRD.TEMP_ELS

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_START | DATE | N |  |
| YEAR_END | DATE | N |  |
| MRNO | VARCHAR2(14) | N |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | N |  |
| CURRENT_YEAR | NUMBER(6,2) | Y |  |
| LAST_YEAR_BALANCE | NUMBER(7,2) | Y |  |
| TOTAL_LEAVES | NUMBER(7,2) | Y |  |
| LEAVE_AVAILED | NUMBER(7,2) | Y |  |
| LEAVE_CARRIED_FORWARD | VARCHAR2(1) | Y |  |
| NO_CARRIED_FORWARD | NUMBER(7,2) | Y |  |

- **PK** `PK_TEMP_ELS`: MRNO, LEAVE_TYPE_ID, YEAR_START, YEAR_END

## HRD.TEMP_EMP_INC_PROPOSAL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(182) | Y |  |
| JOINING_DATE | DATE | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| INCREMENT_DATE | DATE | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| FLAG_INCREMENT | CHAR(1) | Y |  |
| FLAG_ADJUSTMENT | CHAR(1) | Y |  |
| FLAG_DESIGNATION_CHANGE | CHAR(1) | Y |  |
| PREVIOUS_DESIGNATION | VARCHAR2(255) | Y |  |
| PREVIOUS_DESIGNATION_ID | VARCHAR2(7) | Y |  |
| FINAL | CHAR(1) | Y |  |
| TRANS_DATE | DATE | Y |  |
| EFFECTIVE_FROM | DATE | Y |  |
| LETTER_FROM | VARCHAR2(14) | Y |  |
| LETTER_DATE | DATE | Y |  |
| PREVIOUS_GROSS_UPDATED | NUMBER(10) | Y |  |
| YEAR_CODE | NUMBER(4) | Y |  |
| PROPOSAL_NO | NUMBER(2) | Y |  |


## HRD.TEMP_EMP_PICTURE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PICTURE | BLOB | Y |  |

_No standard audit columns._

- **PK** `PK_HRD_TEMP_EMP_PICTURE`: MRNO
- **FK** `FK_HRD_TEMP_EMP_PICTURE`: (MRNO) -> REGISTRATION.PATIENT(MRNO)

## HRD.TEMP_EMP_TURN_OVER

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT_DESC | VARCHAR2(100) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| TOTAL_EMPLOYEES | NUMBER | Y |  |
| TURN_OVER_EMPLOYEES | NUMBER | Y |  |
| TURN_OVER_RATIO | NUMBER(7,3) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TEMP_INC_LETTER_PRINTING

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(182) | Y |  |
| JOINING_DATE | DATE | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| INCREMENT_DATE | DATE | Y |  |
| GRADE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| FLAG_INCREMENT | CHAR(1) | N |  |
| FLAG_ADJUSTMENT | CHAR(1) | N |  |
| FLAG_DESIGNATION_CHANGE | CHAR(1) | N |  |
| PREVIOUS_DESIGNATION | VARCHAR2(255) | Y |  |
| PREVIOUS_DESIGNATION_ID | VARCHAR2(7) | Y |  |
| TRANS_DATE | DATE | Y |  |
| EFFECTIVE_FROM | DATE | Y |  |
| LETTER_FROM | VARCHAR2(14) | Y |  |
| LETTER_FROM_NAME | VARCHAR2(255) | Y |  |
| LETTER_FROM_DESIGNATION | VARCHAR2(255) | Y |  |
| REPORT_NAME | VARCHAR2(60) | Y |  |
| REPORT_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TEMP_JOINER_LEAVER_REPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(182) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT | VARCHAR2(60) | Y |  |
| JOINING_DATE | DATE | Y |  |
| LEAVING_DATE | DATE | Y |  |
| LEAVING_REASON_ID | VARCHAR2(3) | Y |  |
| LEAVING_REASON | VARCHAR2(60) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| PATIENT_TYPE | VARCHAR2(60) | Y |  |
| CHANGED_MRNO | VARCHAR2(14) | Y |  |
| INCLUDE_IN_REPORT | CHAR(1) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| CONTRACT_START_DATE | DATE | Y |  |
| CONTRACT_END_DATE | DATE | Y |  |
| PREFIX | VARCHAR2(3) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| SECTION_DESC | VARCHAR2(60) | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(6) | Y |  |
| DUTY_LOCATION_DESC | VARCHAR2(80) | Y |  |

_No standard audit columns._


## HRD.TEMP_LEAVE_BALANCES

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| EARNED_LEAVE_BALANCES | NUMBER(3) | Y |  |
| GROSS_PAY_PER_DAY | NUMBER(7,2) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._


## HRD.TEMP_LEAVE_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| LEAVE_DATE | DATE | Y |  |
| SERIAL_NO | NUMBER(5) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| VERIFIED | VARCHAR2(1) | Y |  |
| SHORT_LEAVE | VARCHAR2(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |


## HRD.TEMP_MISSED_CARD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| CARD_MISSING_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TEMP_MISSING_ROSTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(255) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT | VARCHAR2(255) | Y |  |
| MISSED_DAY | NUMBER(6) | Y |  |
| MONTH_START_DATE | DATE | Y |  |
| MONTH_END_DATE | DATE | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |

_No standard audit columns._


## HRD.TEMP_ONCALL_EMP_LOV

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ROSTER_DATE | DATE | Y |  |
| ONCALL_ROLE | VARCHAR2(9) | Y |  |
| SHIFT_SOURCE | VARCHAR2(23) | Y |  |
| CREDITED_HOURS | NUMBER | Y |  |
| ACTUAL_SWIPE_HOURS | NUMBER | Y |  |
| SHIFT_START_DT | DATE | Y |  |
| SHIFT_END_DT | DATE | Y |  |
| SWIPE_COUNT | NUMBER | Y |  |
| PRESENCE_STATUS | CHAR(1) | Y |  |
| SCHEDULED_HOURS | NUMBER | Y |  |
| MIN_SWIPE_DT | DATE | Y |  |
| MAX_SWIPE_DT | DATE | Y |  |
| SOURCE_COLUMN | VARCHAR2(9) | Y |  |
| ROSTER_TYPE_ID | NUMBER | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| ROSTER_BATCH_GROUP_ID | VARCHAR2(6) | Y |  |
| ROSTER_BATCH_ID | VARCHAR2(6) | Y |  |
| POST_CALL | CHAR(1) | Y |  |
| SHIFT_KEY | VARCHAR2(35) | Y |  |
| SHIFT_LOWER_BOUND | DATE | Y |  |
| SHIFT_UPPER_BOUND | DATE | Y |  |
| ROSTER_END_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TEMP_ONCALL_ROSTER

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ORDER_BY | NUMBER | Y |  |

_No standard audit columns._


## HRD.TEMP_ONCALL_SWAP_EMP_LOV

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| ROSTER_DATE | DATE | Y |  |
| ONCALL_ROLE | VARCHAR2(9) | Y |  |
| SHIFT_SOURCE | VARCHAR2(23) | Y |  |
| CREDITED_HOURS | NUMBER | Y |  |
| ACTUAL_SWIPE_HOURS | NUMBER | Y |  |
| SHIFT_START_DT | DATE | Y |  |
| SHIFT_END_DT | DATE | Y |  |
| SWIPE_COUNT | NUMBER | Y |  |
| PRESENCE_STATUS | CHAR(1) | Y |  |
| SCHEDULED_HOURS | NUMBER | Y |  |
| MIN_SWIPE_DT | DATE | Y |  |
| MAX_SWIPE_DT | DATE | Y |  |
| SOURCE_COLUMN | VARCHAR2(9) | Y |  |
| ROSTER_TYPE_ID | NUMBER | Y |  |
| SHIFT_ID | VARCHAR2(2) | Y |  |
| ROSTER_BATCH_GROUP_ID | VARCHAR2(6) | Y |  |
| ROSTER_BATCH_ID | VARCHAR2(6) | Y |  |
| POST_CALL | CHAR(1) | Y |  |
| SHIFT_KEY | VARCHAR2(35) | Y |  |
| SHIFT_LOWER_BOUND | DATE | Y |  |
| SHIFT_UPPER_BOUND | DATE | Y |  |
| ROSTER_END_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TEMP_PRIVILEGE_GRANT

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIVILEGES_ID | NUMBER | Y |  |
| PRIVILEGES_DETAIL_ID | NUMBER | Y |  |
| SR_NO | NUMBER | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TEMP_RFID_WISE_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(14) | Y |  |
| MACHINE_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| GENDER | CHAR(1) | Y |  |

_No standard audit columns._


## HRD.TEMP_SERVICE_REWARD

| Column | Type | Null | Comment |
|---|---|---|---|
| EMP_CODE | VARCHAR2(14) | Y |  |
| DOB | DATE | Y |  |
| EMP_NAME | VARCHAR2(255) | Y |  |
| DEPARTMENT | VARCHAR2(255) | Y |  |
| DESIGNATION | VARCHAR2(255) | Y |  |
| JOINING_DATE | DATE | Y |  |
| YEARS | VARCHAR2(2) | Y |  |
| MONTHS | VARCHAR2(2) | Y |  |
| DAYS | VARCHAR2(2) | Y |  |
| EMPLOYEE_TYPE | VARCHAR2(60) | Y |  |
| CONTRACT_START_DATE | DATE | Y |  |
| CONTRACT_END_DATE | DATE | Y |  |
| DUTY_LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._


## HRD.TEMP_TOTAL_SHIFTS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| LEVEL_ID | VARCHAR2(6) | Y |  |
| DUTY_DATE | DATE | Y |  |
| SHIFT | VARCHAR2(7) | Y |  |
| TOTAL | NUMBER(3) | Y |  |

_No standard audit columns._


## HRD.TEMP_YEARLY_LEAVE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(300) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPARTMENT | VARCHAR2(300) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DESIGNATION | VARCHAR2(300) | Y |  |
| YEAR_START | DATE | Y |  |
| YEAR_END | DATE | Y |  |
| OPENING_BALANCE | NUMBER(7,2) | Y |  |
| ACCRUAL | NUMBER(7,2) | Y |  |
| TOTAL_LEAVES | NUMBER(7,2) | Y |  |
| AVAILED_LEAVES | NUMBER(7,2) | Y |  |
| CLOSING_BALANCE | NUMBER(7,2) | Y |  |
| LAPSED | NUMBER(7,2) | Y |  |
| CARRIED_FORWARD | NUMBER(7,2) | Y |  |
| LEAVE_TYPE_ID | VARCHAR2(3) | Y |  |
| LEAVE_DESCRIPTION | VARCHAR2(300) | Y |  |

_No standard audit columns._


## HRD.TEST_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(10) | N |  |
| ID_NAME | VARCHAR2(60) | Y |  |

- **PK** `PK_TEST_MASTER`: ID
- **Triggers**: `TEST_MASTER_INS` (before insert)

## HRD.TEST_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(10) | N |  |
| SERIAL_NO | NUMBER(6) | N |  |
| DETAIL_NAME | VARCHAR2(60) | Y |  |

- **PK** `PK_TEST_DETAIL`: ID, SERIAL_NO
- **FK** `FK_TEST_DETAIL_1`: (ID) -> HRD.TEST_MASTER(ID)
- **Triggers**: `TEST_DETAIL_INS` (before insert)

## HRD.THUMBSCAN
Store thumbscan details

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| REGISTRATION_DATE | DATE | Y |  |
| OBJ_NAME | VARCHAR2(20) | Y |  |
| OBJ_VALUE | BLOB default empty_blob() | Y |  |
| OBJ_VALUE_1200 | BLOB default empty_blob() | Y | This column stores fingerprints value as a string from Digitalpersona |
| THUMB_DATA_KP | VARCHAR2(4000) | Y | This column stores fingerprints value as a string from RFID device |
| IRIS_VALUE | BLOB default empty_blob() | Y | This column stores IRIS features value as a string from RFID device |

- **PK** `PK_ID`: ID
- **UK** `UK_MRNO`: MRNO
- **Triggers**: `THUMBSCAN_DEL` (after delete), `THUMBSCAN_INS` (before insert), `THUMBSCAN_UPD` (before update)

## HRD.TMP_DUTY_ROSTER_MISSING_EMAIL
This table use for temporary basis

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y | Ref Definitions.department.department_id |
| DEPART_NAME | VARCHAR2(100) | Y | Ref Definitions.department.description |
| DUTY_ROSTER_MONTH | VARCHAR2(6) | Y | Ref defnitions.month.month_id |
| DUTY_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TMP_EXCEL_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| COL1 | VARCHAR2(2000) | Y |  |
| COL2 | VARCHAR2(2000) | Y |  |
| COL3 | VARCHAR2(2000) | Y |  |
| COL4 | VARCHAR2(2000) | Y |  |
| COL5 | VARCHAR2(2000) | Y |  |
| COL6 | VARCHAR2(2000) | Y |  |
| COL7 | VARCHAR2(2000) | Y |  |
| COL8 | VARCHAR2(2000) | Y |  |

_No standard audit columns._


## HRD.TMP_EXCEPT_LEAVE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICANT_MRNO | VARCHAR2(14) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TMP_HR_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| COL1 | VARCHAR2(4000) | Y |  |
| COL2 | VARCHAR2(4000) | Y |  |
| COL3 | VARCHAR2(4000) | Y |  |
| COL4 | VARCHAR2(4000) | Y |  |
| COL5 | VARCHAR2(4000) | Y |  |
| COL6 | VARCHAR2(4000) | Y |  |
| COL7 | VARCHAR2(4000) | Y |  |
| COL8 | VARCHAR2(4000) | Y |  |
| COL9 | VARCHAR2(4000) | Y |  |
| COL10 | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## HRD.TMP_LAPS_LEAVE_PROC

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| CALC_TIME | DATE | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| ERROR_TEXT | VARCHAR2(2000) | Y |  |

_No standard audit columns._


## HRD.TMP_LOV

| Column | Type | Null | Comment |
|---|---|---|---|
| PA_TYPE_ID | NUMBER(3) | Y |  |
| PATP_ID | NUMBER(3) | Y |  |
| APPRAISER_MRNO | VARCHAR2(14) | Y |  |
| PA_PERFORM_ID | VARCHAR2(12) | Y |  |
| APPRAISEE_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TMP_NEW_JOINER_ACTIVITY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| NAME | VARCHAR2(255) | Y |  |
| DEPARTMENT_ID | VARCHAR2(11) | Y |  |
| DEPARTMENT_NAME | VARCHAR2(500) | Y |  |
| DESIGNATION_NAME | VARCHAR2(500) | Y |  |
| JOINING_DATE | DATE | Y |  |
| PERFORM_EVENT | VARCHAR2(3) | Y |  |
| DESIGNATION_ID | VARCHAR2(11) | Y |  |

- **PK** `TMP_NEW_JOINER_ACTIVITY_PK`: MRNO
- **Triggers**: `TMP_NEW_JOINER_ACTIVITY_DEL` (after delete), `TMP_NEW_JOINER_ACTIVITY_INS` (before insert), `TMP_NEW_JOINER_ACTIVITY_UPD` (before update)

## HRD.TMP_NEW_JOINER_LIST

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(500) | Y |  |
| DEPARTMENT_ID | VARCHAR2(500) | Y |  |
| DEPARTMENT | VARCHAR2(2000) | Y |  |
| DESIGNATION | VARCHAR2(2000) | Y |  |
| JOINING_DATE | DATE | Y |  |

_No standard audit columns._


## HRD.TMP_NO_CARD_SWIPE_EMAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DEPART_NAME | VARCHAR2(100) | Y |  |
| DUTY_DATE | DATE | Y |  |
| MANAGER_MRNO | VARCHAR2(14) | Y |  |
| SUP_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TMP_RFID_CARD

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TMP_TR_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_NO | NUMBER | N |  |
| REVISION_NO | NUMBER | N |  |
| REQUEST_DATE | DATE | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| DEPARTMENT | VARCHAR2(4000) | Y |  |
| DESIGNATION | VARCHAR2(4000) | Y |  |
| NAME | VARCHAR2(4000) | Y |  |
| AUTHORITY_TYPE | CHAR(2) | Y |  |
| AUTHORITY_ID | VARCHAR2(3) | N |  |

_No standard audit columns._


## HRD.TMP_TURN_OVER_RATIO
This table is use to temporary data save of turnover report

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| REPORT_START_DATE | DATE | Y |  |
| REPORT_END_DATE | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |

_No standard audit columns._


## HRD.TRAINING_DATA

| Column | Type | Null | Comment |
|---|---|---|---|
| NOMINEE_MRNO | VARCHAR2(14) | N |  |
| TRAINING_SUBJECT | VARCHAR2(500) | Y |  |
| ATTENDANCE_DATE | DATE | Y |  |
| SCHEDULE_ID | VARCHAR2(9) | N |  |
| SUBJECT_ID | VARCHAR2(9) | N |  |

- **PK** `PK_TRAINING_DATA`: NOMINEE_MRNO, SCHEDULE_ID, SUBJECT_ID
- **Triggers**: `TRAINING_DATA_DEL` (after delete), `TRAINING_DATA_INS` (before insert), `TRAINING_DATA_UPD` (before update)

## HRD.TRAINING_RECORD

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINING_TYPE | VARCHAR2(10) | Y |  |
| EMPLOYEE_NAME | VARCHAR2(100) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(17) | Y |  |
| DESIGNATION | VARCHAR2(100) | Y |  |
| DEPARTMENT | VARCHAR2(100) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRAINING_COURSE | VARCHAR2(150) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(100) | Y |  |
| TRAINER | VARCHAR2(100) | Y |  |
| ORGANIZER | VARCHAR2(10) | Y |  |
| FROM_DATE | VARCHAR2(20) | Y |  |
| TO_DATE | VARCHAR2(20) | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(20) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(30) | Y |  |
| STATUS | VARCHAR2(30) | Y |  |


## HRD.TRAINING_RECORD_ALL

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINING_TYPE | VARCHAR2(20) | Y |  |
| EMPLOYEE_NAME | VARCHAR2(72) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(17) | Y |  |
| DESIGNATION | VARCHAR2(100) | Y |  |
| DEPARTMENT | VARCHAR2(70) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRAINING_COURSE | VARCHAR2(250) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(70) | Y |  |
| TRAINER | VARCHAR2(150) | Y |  |
| ORGANIZER | VARCHAR2(40) | Y |  |
| FROM_DATE | VARCHAR2(25) | Y |  |
| TO_DATE | VARCHAR2(25) | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(10) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(10) | Y |  |
| PASS_FAIL | VARCHAR2(10) | Y |  |
| DURATION | VARCHAR2(20) | Y |  |
| DURATION_UNIT | VARCHAR2(20) | Y |  |


## HRD.TRAINING_RECORD_ALL_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINING_TYPE | VARCHAR2(20) | Y |  |
| EMPLOYEE_NAME | VARCHAR2(72) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(17) | Y |  |
| DESIGNATION | VARCHAR2(80) | Y |  |
| DEPARTMENT | VARCHAR2(70) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRAINING_COURSE | VARCHAR2(250) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(70) | Y |  |
| TRAINER | VARCHAR2(70) | Y |  |
| ORGANIZER | VARCHAR2(40) | Y |  |
| FROM_DATE | VARCHAR2(12) | Y |  |
| TO_DATE | VARCHAR2(12) | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(10) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(10) | Y |  |
| PASS_FAIL | VARCHAR2(10) | Y |  |

_No standard audit columns._


## HRD.TRAINING_RECORD_CONSULTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINER | VARCHAR2(70) | Y |  |
| TRAINING_COURSE | VARCHAR2(250) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| UNITS | VARCHAR2(10) | Y |  |


## HRD.TRAINING_RECORD_EXCEPTION

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINING_TYPE | VARCHAR2(20) | Y |  |
| EMPLOYEE_NAME | VARCHAR2(70) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(12) | Y |  |
| DESIGNATION | VARCHAR2(100) | Y |  |
| DEPARTMENT | VARCHAR2(70) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRAINING_COURSE | VARCHAR2(250) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(70) | Y |  |
| TRAINER | VARCHAR2(150) | Y |  |
| ORGANIZER | VARCHAR2(40) | Y |  |
| FROM_DATE | VARCHAR2(25) | Y |  |
| TO_DATE | VARCHAR2(25) | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(10) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(10) | Y |  |
| PASS_FAIL | VARCHAR2(10) | Y |  |
| DURATION | VARCHAR2(20) | Y |  |
| DURATION_UNIT | VARCHAR2(20) | Y |  |
| ERROR_TEXT | VARCHAR2(4000) | Y |  |


## HRD.TRAINING_RECORD_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(6) | Y |  |
| TRAINING_TYPE | VARCHAR2(20) | Y |  |
| EMPLOYEE_NAME | VARCHAR2(72) | Y |  |
| EMPLOYEE_CODE | VARCHAR2(17) | Y |  |
| DESIGNATION | VARCHAR2(80) | Y |  |
| DEPARTMENT | VARCHAR2(70) | Y |  |
| JOINING_DATE | DATE | Y |  |
| TRAINING_COURSE | VARCHAR2(250) | Y |  |
| TRAINING_INSTITUTE | VARCHAR2(70) | Y |  |
| TRAINER | VARCHAR2(70) | Y |  |
| ORGANIZER | VARCHAR2(40) | Y |  |
| FROM_DATE | VARCHAR2(12) | Y |  |
| TO_DATE | VARCHAR2(12) | Y |  |
| TRAINING_DURATION | VARCHAR2(30) | Y |  |
| BOND_DURATION | VARCHAR2(10) | Y |  |
| BOND_COST | VARCHAR2(20) | Y |  |
| TOTAL_TRAINING_COST | VARCHAR2(20) | Y |  |
| VALIDITY | VARCHAR2(10) | Y |  |
| PASS_FAIL | VARCHAR2(10) | Y |  |

_No standard audit columns._


## HRD.TR_MODE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MODE_ID | NUMBER | N |  |
| MODE_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| JOB_ROLE | CHAR(1) | Y |  |

- **PK** `MODE_ID_PK`: MODE_ID
- **Triggers**: `TR_MODE_TYPE_DEL` (after delete), `TR_MODE_TYPE_INS` (before insert), `TR_MODE_TYPE_UPD` (before update)

## HRD.TR_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | NUMBER(8) | N |  |
| TYPE_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REQUEST_TYPE | CHAR(1) | Y | 'N' FOR NEW REQUEST, 'C' FOR CHANGED |
| REQUEST_DESC | CHAR(2) | Y |  |

- **PK** `TYPE_ID_PK`: TYPE_ID
- **Triggers**: `TR_TYPE_DEL` (after delete), `TR_TYPE_INS` (before insert), `TR_TYPE_UPD` (before update)

## HRD.TRAVEL_REQUEST

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_NO | NUMBER | N |  |
| REQUEST_DATE | DATE | Y |  |
| TYPE_ID | NUMBER | N |  |
| PLACE_OF_VISIT | VARCHAR2(4000) | Y |  |
| DEPARTURE_DATE | DATE | Y |  |
| RETURN_DATE | DATE | Y |  |
| VISIT_PURPOSE | VARCHAR2(4000) | Y |  |
| TRAVEL_ROUTE | VARCHAR2(4000) | Y |  |
| MODE_ID | NUMBER | Y |  |
| MODE_REMARKS | VARCHAR2(4000) | Y |  |
| TRAVEL_TYPE | CHAR(1) | Y | 'S' SELF, 'O' OFFICIAL |
| ACCOMODATION_TYPE | VARCHAR2(50) | Y |  |
| ACCOMODATION_REMARKS | VARCHAR2(4000) | Y |  |
| REQUEST_DESCRIPTION | VARCHAR2(2000) | Y |  |
| STATUS_ID | NUMBER | Y |  |
| REQUEST_ADVANCE_AMOUNT | NUMBER | Y |  |
| REVISION_NO | NUMBER | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| APPROVAL_DATE | DATE | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| SPONSORED_BY | VARCHAR2(200) | Y |  |
| CEB_DATE | DATE | Y |  |
| ADMIN_SUBTITUTE | VARCHAR2(14) | Y |  |
| CLINICAL_SUBTITUTE | VARCHAR2(14) | Y |  |
| CURRENCY_TYPE | VARCHAR2(3) default '001' | Y |  |
| INTERNATIONAL | CHAR(1) | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| SPECIFY_REASON | VARCHAR2(4000) | Y |  |
| IS_SKM_PESHAWAR | CHAR(1) default 'N' | Y |  |
| ORGANIZATION_LOCATION_ID | VARCHAR2(3) default '000' | Y |  |
| PLACE_OF_VISIT_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_TRAVEL_REQUEST`: REQUEST_NO, REVISION_NO
- **FK** `FK_LOCATION_ID`: (ORGANIZATION_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_TRAVEL_REQUEST_1`: (MODE_ID) -> HRD.TR_MODE_TYPE(MODE_ID) [disabled]
- **FK** `FK_TRAVEL_REQUEST_2`: (TYPE_ID) -> HRD.TR_TYPE(TYPE_ID) [disabled]
- **Triggers**: `EMAIL_SEND_SUBSTITUTE` (before insert), `TRAVEL_REQUEST_DEL` (after delete), `TRAVEL_REQUEST_INS` (before insert), `TRAVEL_REQUEST_UPD` (before update), `TRG_AU_TRAVEL_REQUEST_APPROVAL` (after update of approval_date), `TRG_REMOVE_SUBSTITUE` (after update or delete)

## HRD.TRAVLE_VISIT_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| CLAIM_NO | VARCHAR2(12) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| DOCUMENT_ID | VARCHAR2(15) | Y |  |
| DOCUMENT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |

- **PK** `PK_TRAVLE_VISIT_ATTACHMENT`: SR_NO, CLAIM_NO
- **Triggers**: `TRAVLE_VISIT_ATTACHMENT_DEL` (after delete), `TRAVLE_VISIT_ATTACHMENT_INS` (before insert), `TRAVLE_VISIT_ATTACHMENT_UPD` (before update)

## HRD.TR_AUTHORITY

| Column | Type | Null | Comment |
|---|---|---|---|
| AUTHORITY_ID | VARCHAR2(3) | N |  |
| AUTHORITY_DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| AUTHORITY_REMARKS | VARCHAR2(500) | Y |  |
| AUTHORITY_TYPE | CHAR(2) | Y |  |

- **PK** `AUTHORITY_ID_PK`: AUTHORITY_ID
- **Triggers**: `TR_AUTHORITY_DEL` (after delete), `TR_AUTHORITY_INS` (before insert), `TR_AUTHORITY_UPD` (before update)

## HRD.TR_HIERARCHY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| HIERARCHY_DETAIL_ID | NUMBER | N |  |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| HIERARCHY_ID | NUMBER | N |  |
| AUTHORITY_ID | VARCHAR2(3) | Y |  |

- **PK** `TRHD_ID_PK`: HIERARCHY_DETAIL_ID, HIERARCHY_ID
- **FK** `HIERARCHY_ID_FK`: (HIERARCHY_ID) -> HRD.TR_HIERARCHY(HIERARCHY_ID) [disabled]
- **FK** `TRHD_AUTHORITY_ID_FK`: (AUTHORITY_ID) -> HRD.TR_AUTHORITY(AUTHORITY_ID) [disabled]
- **Triggers**: `TR_HIERARCHY_DETAIL_DEL` (after delete), `TR_HIERARCHY_DETAIL_INS` (before insert), `TR_HIERARCHY_DETAIL_UPD` (before update)

## HRD.TR_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| REQUEST_NO | NUMBER | N |  |
| REVISION_NO | NUMBER | N |  |
| AUTHORITY_ID | VARCHAR2(3) | N |  |
| ENTRY_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| IN_QUEUE_MRNO | VARCHAR2(14) | Y |  |
| ACTING_MRNO | VARCHAR2(14) | Y |  |

- **PK** `TR_QUEUE_PK`: REQUEST_NO, REVISION_NO, AUTHORITY_ID
- **FK** `AUTHORITY_ID_FK`: (AUTHORITY_ID) -> HRD.TR_AUTHORITY(AUTHORITY_ID) [disabled]
- **FK** `TRQ_REQUEST_NO_FK`: (REQUEST_NO, REVISION_NO) -> HRD.TRAVEL_REQUEST(REQUEST_NO, REVISION_NO)
- **Triggers**: `TR_QUEUE_DEL` (after delete), `TR_QUEUE_INS` (before insert), `TR_QUEUE_PT_DEL` (after delete), `TR_QUEUE_PT_INS` (before insert), `TR_QUEUE_PT_UPD` (after update), `TR_QUEUE_UPD` (before update)

## HRD.TR_QUEUE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| HISTORY_ID | NUMBER | N |  |
| REQUEST_NO | NUMBER | Y |  |
| REVISION_NO | NUMBER | Y |  |
| AUTHORITY_ID | VARCHAR2(3) | Y |  |
| ENTRY_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| DECISION | VARCHAR2(20) | Y |  |
| DECISION_DATE | DATE | Y |  |
| DECISION_BY | VARCHAR2(14) | Y |  |
| ACTING_FOR | VARCHAR2(14) | Y |  |

- **PK** `HISTORY_ID_PK`: HISTORY_ID
- **FK** `TRQH_AUTHORITY_ID_FK`: (AUTHORITY_ID) -> HRD.TR_AUTHORITY(AUTHORITY_ID) [disabled]
- **FK** `TRQH_REQUEST_NO_FK`: (REQUEST_NO, REVISION_NO) -> HRD.TRAVEL_REQUEST(REQUEST_NO, REVISION_NO) [disabled]
- **Triggers**: `TR_QUEUE_HISTORY_DEL` (after delete), `TR_QUEUE_HISTORY_INS` (before insert), `TR_QUEUE_HISTORY_UPD` (before update)

## HRD.T_ANUALY_TRUN_OVER_RATIO
Store monthly department wise turn over ratio of employees

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y | Store department code |
| MONTHS | VARCHAR2(6) | Y | Store month like 012006 |
| EMPLOYEE_LEFT | NUMBER(5) | Y | Store number of employees left with in stored month |
| TOTAL_EMPLOYEE | NUMBER(5) | Y | Store total number of existing employees |


## HRD.YEAR_SETUP_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_ID | NUMBER | N |  |
| YEAR_DESC | NUMBER | Y |  |
| DEFAULT_CHECK | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CPD_START_DATE | DATE | Y |  |
| CPD_END_DATE | DATE | Y |  |

- **PK** `YEAR_SETUP_MASTER_PK`: YEAR_ID
- **Triggers**: `YEAR_SETUP_MASTER_DEL` (after delete), `YEAR_SETUP_MASTER_INS` (before insert), `YEAR_SETUP_MASTER_UPD` (before update)

## HRD.YEAR_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_ID | NUMBER | N |  |
| MONTH_ID | NUMBER | N |  |
| MONTH_NAME | VARCHAR2(20) | Y |  |
| MONTH_START | DATE | Y |  |
| MONTH_END | DATE | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `YEAR_SETUP_DETAIL_PK`: YEAR_ID, MONTH_ID
- **FK** `YEAR_SETUP_DETAIL_FK`: (YEAR_ID) -> HRD.YEAR_SETUP_MASTER(YEAR_ID)
- **Triggers**: `YEAR_SETUP_DETAIL_DEL` (after delete), `YEAR_SETUP_DETAIL_INS` (before insert), `YEAR_SETUP_DETAIL_UPD` (before update)

## HRD.YEAR_TYPE
Store different year type that can exists within an annum

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_TYPE_ID | VARCHAR2(1) | N | Store year type id like C, F |
| DESCRIPTION | VARCHAR2(60) | Y | Store year description like Calender year, Financial year |
| YEAR_START | VARCHAR2(5) | Y | Store date from which year starts |
| YEAR_END | VARCHAR2(5) | Y | Store date from which year ends |
| ACTIVE | VARCHAR2(1) default 'Y' | Y | Store status of year type as Y for active and N for Inactive |

- **PK** `PK_YEAR_TYPE`: YEAR_TYPE_ID
- **Triggers**: `TRG_WS_PWS_LS_UE_Q` (after insert or update or delete), `YEAR_TYPE_CEA` (before insert or update or delete), `YEAR_TYPE_DEL` (after delete), `YEAR_TYPE_INS` (before insert), `YEAR_TYPE_UPD` (before update)

## HRD.YEAR_WSIE_WEIGHTAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| YEAR_DESC | NUMBER | Y |  |
| YEAR_CONTARCT_HOUR | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `YEAR_WSIE_WEIGHTAGE_PK`: ID
- **Triggers**: `YEAR_WSIE_WEIGHTAGE_DEL` (after delete), `YEAR_WSIE_WEIGHTAGE_INS` (before insert), `YEAR_WSIE_WEIGHTAGE_UPD` (before update)

