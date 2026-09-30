# DEFINITIONS tables

Audit/multi-location columns (user_id, terminal, trn_date, original_user_id, original_terminal, original_trn_date, org_id, zon_id, loc_id, ws_sync_date) are omitted from the column lists below; every table has them unless noted.

## DEFINITIONS.ABBREVIATIONS_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ABB_TYPE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ABBREVIATIONS_TYPE`: ABB_TYPE_ID
- **Triggers**: `ABBREVIATIONS_TYPE_CEA` (before insert or update or delete), `ABBREVIATIONS_TYPE_DEL` (after delete), `ABBREVIATIONS_TYPE_INS` (before insert), `ABBREVIATIONS_TYPE_UPD` (before update), `TRG_WS_SVB_VJ_KE_Q` (after insert or update or delete)

## DEFINITIONS.ABBREVIATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | N |  |
| ABB_ID | VARCHAR2(50) | Y |  |
| ABB_DESC | VARCHAR2(200) | Y |  |
| APPROVED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| USE_INSTEAD | VARCHAR2(200) | Y |  |
| ABB_TYPE_ID | NUMBER | Y |  |
| ABBREVIATION_CATEGORY | VARCHAR2(3) | Y | C => Chemo Procol, D => Doctor_name O => Others |

- **PK** `ABB_PK`: SERIAL_NO
- **UK** `ABB_UK`: ABB_ID, ABB_DESC, ABBREVIATION_CATEGORY
- **FK** `FK_ABBREVIATIONS_01`: (ABB_TYPE_ID) -> DEFINITIONS.ABBREVIATIONS_TYPE(ABB_TYPE_ID) [disabled]
- **Triggers**: `ABBREVIATIONS_CEA` (before insert or update or delete), `ABBREVIATIONS_DEL` (after delete), `ABBREVIATIONS_INS` (before insert), `ABBREVIATIONS_UPD` (before update), `TRG_WS_OXF_WJ_NP_Q` (after insert or update or delete)

## DEFINITIONS.ABBREVIATION_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(4) | N |  |
| CATEGORY_DESC | VARCHAR2(100) | N |  |
| CATEGORY_SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_ABBREVIATION_CATEGORY_ID`: CATEGORY_ID
- **Triggers**: `ABBREVIATION_CATEGORY_CEA` (before insert or update or delete), `ABBREVIATION_CATEGORY_DEL` (after delete), `ABBREVIATION_CATEGORY_INS` (before insert), `ABBREVIATION_CATEGORY_UPD` (before update), `TRG_WS_CNV_DY_SB_Q` (after insert or update or delete)

## DEFINITIONS.ABSTRACT_EDIT_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER(3) | Y |  |
| STATUS | VARCHAR2(10) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.ACTING_EMPLOYEE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SUPERVISOR_MRNO | VARCHAR2(14) | Y |  |
| ACTING_MRNO | VARCHAR2(14) | Y |  |
| ACTING_ACTIVE | CHAR(1) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_ACTING_EMPLOYEE`: MRNO
- **Triggers**: `TRG_WS_QBJ_KY_JF_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_OBJECT_TYPE`: OBJECT_TYPE_ID
- **Triggers**: `OBJECT_TYPE_CEA` (before insert or update or delete), `OBJECT_TYPE_DEL` (after delete), `OBJECT_TYPE_INS` (before insert), `OBJECT_TYPE_UPD` (before update), `TRG_WS_ASZ_PW_PD_Q` (after insert or update or delete)

## DEFINITIONS.PATHS

| Column | Type | Null | Comment |
|---|---|---|---|
| PATH_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| PATH_GLOBAL_VARIABLE_NAME | VARCHAR2(50) | Y |  |
| PATH_GLOBAL_VARIABLE_VALUE | VARCHAR2(250) | Y |  |
| O_PATH_GLOBAL_VARIABLE_VALUE | VARCHAR2(250) | Y | Old data of PATH_GLOBAL_VARIABLE_VALUE column |
| OLD_DESCRIPTION | VARCHAR2(200) | Y | Old data of DESCRIPTION column |

- **PK** `PK_PATHS`: PATH_ID
- **Triggers**: `PATHS_CEA` (before insert or update or delete), `PATHS_DEL` (after delete), `PATHS_INS` (before insert), `PATHS_UPD` (before update), `TRG_WS_WNR_CK_SV_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_TYPE_ID | VARCHAR2(4) | N | Unique Report Type ID |
| REPORT_TYPE_DESC | VARCHAR2(50) | N | Description of Report Type |
| PAGE_HEIGHT | NUMBER(6,2) | N | Report page height (Inches) |
| PAGE_WIDTH | NUMBER(6,2) | N | Report page width (Inches) |
| ORIENTATION | CHAR(1) default 'P' | N | Flag Information P=Portrait, L=Landscape |
| LEFT_MARGIN | NUMBER(6,2) | Y | Left margin of page setting |
| TOP_MARGIN | NUMBER(6,2) | Y | Top margin of page setting |
| RIGHT_MARGIN | NUMBER(6,2) | Y | Right margin of page setting |
| BOTTOM_MARGIN | NUMBER(6,2) | Y | Bottom margin of page setting |
| ORDER_BY | NUMBER(4) | N | List display order by |
| ACTIVE | CHAR(1) default 'Y' | N | Flag Information Y=Active, N=Inactive |

- **PK** `PK_REPORT_TYPES`: REPORT_TYPE_ID
- **UK** `UK_REPORT_TYPES_01`: REPORT_TYPE_DESC
- **CHECK** `CK_REPORT_TYPES_2`: ORIENTATION IN ('P','L'
- **CHECK** `CK_REPORT_TYPES_3`: ACTIVE IN ('Y','N'
- **Triggers**: `REPORT_TYPES_CEA` (before insert or update or delete), `REPORT_TYPES_DEL` (after delete), `REPORT_TYPES_INS` (before insert), `REPORT_TYPES_UPD` (before update), `TRG_WS_FSH_UM_XJ_Q` (after insert or update or delete)

## DEFINITIONS.DEVELOPMENT_TOOLS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(4) | N |  |
| DEV_TOOL | VARCHAR2(25) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| AUTO_RIGHTS | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEV_TOOL`: SERIAL_NO
- **Triggers**: `DEVELOPMENT_TOOLS_CEA` (before insert or update or delete), `DEVELOPMENT_TOOLS_DEL` (after delete), `DEVELOPMENT_TOOLS_INS` (before insert), `DEVELOPMENT_TOOLS_UPD` (before update), `TRG_WS_RRW_ZM_FB_Q` (after insert or update or delete)

## DEFINITIONS.DB_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_ID | VARCHAR2(4) | N | Unique Server ID |
| SERVICE_NAME | VARCHAR2(50) | N | Unique Node Name |
| DB_TYPE | VARCHAR2(10) | N | DEV=Development, QA=QA Testing, PRE-PROD=Pre Production, STANDBY=Standby/Contingency,PROD=Production |
| NOTE | VARCHAR2(1000) | Y | Comment Note/Descriptive details |
| CREATED_ON | DATE default SYSDATE | N | Transaction created on date |
| DB_LINK_REPORT | VARCHAR2(25) default '@link_report' | Y | DB link to link current database to REPORT database. |
| TNS_NAME | VARCHAR2(20) | Y |  |
| DB_LINK_STANDBY | VARCHAR2(20) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N | This column contains Location ID for Multi-location info |
| ZONE_ID | VARCHAR2(3) | N | This column contains Zone ID for distributed environment |
| ORGANIZATION_ID | VARCHAR2(3) | N | This column contains Organization ID for Multi-location info |
| STANDBY_TNS | VARCHAR2(50) | Y | This column contains Standby DB TNS Name of Db Service |
| DC_TYPE | CHAR(1) | N | This column contains Data Center Type (C=Central Repository, D=Data Center, X=XEDB) |
| CR_ZONE_ID | VARCHAR2(3) | Y | This column contains Zone ID of Centeral Repository (CR) |
| CR_LOCATION_ID | VARCHAR2(3) | Y | This column contains Location ID of Centeral Repository |
| IS_DECRYPTION_RIGHTS | CHAR(1) | Y |  |
| IS_DISTRIBUTED_MODE1 | CHAR(1) default 'N' | Y | This column contains values N or Y and used to check either current database is running distributed mode or not |
| OBSOLETE | CHAR(1) default 'N' | N | This column contains flag status of machine obsolete Y=Obsoleted, N=Functional |
| IS_DISTRIBUTED_MODE | CHAR(1) default 'N' | N | This column contains values N or Y and used to check either current database is running distributed mode or not |

- **PK** `PK_DB_SERVICES`: SERVICE_ID
- **UK** `UK_DB_SERVICES_1`: SERVICE_NAME
- **CHECK** `CK_DB_SERVICES_1`: DB_TYPE IN ('DEV','QA','PRE-PROD','STANDBY','PROD','SNAPSHOT'
- **CHECK** `CK_DB_SERVICES_2`: UPPER(SERVICE_NAME) = SERVICE_NAME
- **CHECK** `CK_DB_SERVICES_3`: DC_TYPE IN ('D','C','X'
- **CHECK** `CK_DB_SERVICES_4`: OBSOLETE IN ('Y','N'
- **CHECK** `CK_DB_SERVICES_5`: IS_DISTRIBUTED_MODE IN ('Y','N'
- **Triggers**: `DB_SERVICES_CHK` (before insert or update), `DB_SERVICES_DEL` (after delete), `DB_SERVICES_INS` (before insert), `DB_SERVICES_UPD` (before update)

## DEFINITIONS.OBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| NAME | VARCHAR2(1000) | N |  |
| PATH_ID | VARCHAR2(5) | Y |  |
| SUPERVISED_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| DISPLAY_NAME | VARCHAR2(60) | N |  |
| INITIAL_SCREEN | CHAR(1) default 'N' | Y |  |
| DEPLOYMENT_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| OTHER_TITLE_TXT | VARCHAR2(30) | Y |  |
| OTHER_COMMENTS_TXT | VARCHAR2(2000) | Y |  |
| DEPLOYED_YN | CHAR(1) default 'Y' | Y |  |
| TERMINAL_TYPE_ID | VARCHAR2(15) | Y |  |
| PURPOSE | VARCHAR2(2500) | Y |  |
| DEV_TOOL | VARCHAR2(4) | N |  |
| CREATE_SESSION | CHAR(1) default 'N' | N | THIS WILL TELL THE SYSTEM OPEN FORM WITH SESSION OR WITHOUT SESSION. |
| IS_JSP | CHAR(1) | Y |  |
| OBSOLETED_OBJECT | CHAR(1) default 'N' | N |  |
| OBSOLETED_BY | VARCHAR2(14) | Y |  |
| RETIRED_6I | CHAR(1) default 'N' | Y | Flag to mark either 6i version of this object will be available in menu or not |
| RESTRICTED | CHAR(1) default 'N' | N |  |
| EMAIL_SEND | CHAR(1) default 'N' | N |  |
| STOP_AUTO_COMPILE | CHAR(1) default 'N' | Y | Flag to use while compilation from HIS to HIS  value will 'N' if want to auto compile and value will 'Y' if do not want to auto compile |
| PARAM_FORM_REQ | CHAR(1) default 'N' | Y |  |
| OBJECT_SKIP_SECURITY | CHAR(1) default 'N' | Y |  |
| WIN_X_POS | NUMBER(5,2) default 0 | Y | X Position on which form will open |
| WIN_Y_POS | NUMBER(5,2) default 0 | Y | Y Position on which form will open |
| WIN_WIDTH | NUMBER(5,2) default 0 | Y | Width of the Form |
| WIN_HEIGHT | NUMBER(5,2) default 0 | Y | Height of the form |
| REPORT_ID | NUMBER(4) | Y |  |
| REPORT_TYPE_ID | VARCHAR2(4) | Y | This colomn contain report type ID foreign key DEFINITIONS.REPORT TYPES |
| OBJECT_NATURE | CHAR(1) default 'T' | Y | Transactional (T), Statistical (S), Setup (P) |
| RUN_FROM_SERVER | VARCHAR2(4) | Y |  |
| SERVER_TYPE | CHAR(1) | Y |  |
| IS_CONFIDENTIAL_OBJ | CHAR(1) | Y |  |
| IS_REPORTING_FORM | CHAR(1) | Y |  |
| OBJECT_OPEN_MAX_TIME | NUMBER | Y | This is the maximum time which one object can take to open, When we open BI report from oracle forms then it behaves Asynchronous and BI generate file at virtual directory which can be opened by using timer/sleep, every object has different time to open that's why it is added at definition level, time will be entered in Seconds (For oracle developer should write formula this column*1000 because time default time is in Ms) |
| MDI_FORM | CHAR(1) default 'N' | Y | This column contains flag information of MDI status Y=MDI form, N=Not a MDI |
| OBJECT_URL | VARCHAR2(256) | Y | Object such as Dashboard's URL will be defined here, This will create the differentiation between object name and object URL |
| OBJECT_URL_USER | VARCHAR2(50) | Y | This user will be used to access the URL object, if user is not defined here then user will be defined at report server level |
| OBJECT_URL_PASSWORD | VARCHAR2(50) | Y | This Password will be used to access the URL object, if User and Password are not defined here then will be defined at report server level |
| OBJECT_BROWSER_EXE_NAME | VARCHAR2(250) | Y | This column will be used to define the browser path/ name in which this object will be opened |
| SPACE_REQ_AFTER_EXE_NAME | CHAR(1) default 'N' | Y | When we call servers some browsers needs symbol and some needs space, will handle with the help of this column value |
| OBJECT_PAGE | VARCHAR2(60) | Y | This column will be used for BI dashboard pages, If we want to open any specific page of dashboard when open then it will be written in this column moreover data should be encrypted, relevant object will read the encrypted data |
| PAGE_ID | NUMBER | Y | This column contains the Oracle Apex page id. |
| APP_ID | NUMBER | Y |  |
| PLATFORM | CHAR(1) default 'W' | Y | M => Mobile, W => Web Browser, B=> Both |
| DISTRIBUTED_MODE | CHAR(2) default 'RO' | Y | NA = Not Applicable, RO = Read Only, RW = Read Write |

- **PK** `PK_OBJECTS`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID
- **UK** `UK_OBJECTS`: OBJECT_CODE
- **UK** `UK_OBJECTS_1`: OBJECT_TYPE_ID, NAME
- **FK** `FK_OBJECTS_2`: (OBJECT_TYPE_ID) -> DEFINITIONS.OBJECT_TYPE(OBJECT_TYPE_ID)
- **FK** `FK_OBJECTS_3`: (PATH_ID) -> DEFINITIONS.PATHS(PATH_ID)
- **FK** `FK_OBJECTS_4`: (REPORT_TYPE_ID) -> DEFINITIONS.REPORT_TYPES(REPORT_TYPE_ID) [disabled]
- **FK** `FK_OBJECTS_5`: (RUN_FROM_SERVER) -> DEFINITIONS.DB_SERVICES(SERVICE_ID) [disabled]
- **FK** `FK_OBJECTS_6`: (DEV_TOOL) -> DEFINITIONS.DEVELOPMENT_TOOLS(SERIAL_NO)
- **CHECK** `CK_OBJECTS_001`: CREATE_SESSION IN ('Y','N'
- **CHECK** `CK_OBJECT_1`: RESTRICTED IN ('Y','N'
- **CHECK** `CK_OBJECT_2`: EMAIL_SEND IN ('Y','N'
- **CHECK** `CK_OBJECT_5`: MDI_FORM IN ('Y','N'
- **Triggers**: `OBJECTS_DEL` (after delete), `OBJECTS_INS` (before insert), `OBJECTS_INSERT` (before insert), `OBJECTS_UPD` (before update), `TRG_WS_NFN_XP_FS_Q` (after insert or update or delete), `TRG_WS_ODK_DO_PB_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_ACTION

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| ACTION | VARCHAR2(2000) | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| FLOW | VARCHAR2(2000) | Y |  |
| IMAGE | LONG RAW | Y |  |

- **PK** `PK_OBJECT_ACTION`: OBJECT_CODE, ACT_SRNO
- **FK** `FK_OBJECT_ACTION_1`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `OBJECT_ACTION_DEL` (after delete), `OBJECT_ACTION_INS` (before insert), `OBJECT_ACTION_UPD` (before update)

## DEFINITIONS.ACTION_POST_OBJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| POST_OBJECT_CODE | VARCHAR2(11) | N |  |
| COMMENTS | VARCHAR2(2000) | Y |  |

- **PK** `PK_ACTION_POST_OBJECT`: OBJECT_CODE, ACT_SRNO, POST_OBJECT_CODE
- **FK** `FK_ACTION_POST_OBJECT_1`: (OBJECT_CODE, ACT_SRNO) -> DEFINITIONS.OBJECT_ACTION(OBJECT_CODE, ACT_SRNO)
- **FK** `FK_ACTION_POST_OBJECT_2`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `ACTION_POST_OBJECT_DEL` (after delete), `ACTION_POST_OBJECT_INS` (before insert), `ACTION_POST_OBJECT_UPD` (before update)

## DEFINITIONS.ACTION_PRE_OBJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| PRE_OBJECT_CODE | VARCHAR2(11) | N |  |
| COMMENTS | VARCHAR2(2000) | Y |  |

- **PK** `PK_ACTION_PRE_OBJECT`: OBJECT_CODE, ACT_SRNO, PRE_OBJECT_CODE
- **FK** `FK_ACTION_PRE_OBJECT_1`: (OBJECT_CODE, ACT_SRNO) -> DEFINITIONS.OBJECT_ACTION(OBJECT_CODE, ACT_SRNO)
- **FK** `FK_ACTION_PRE_OBJECT_2`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `ACTION_PRE_OBJECT_DEL` (after delete), `ACTION_PRE_OBJECT_INS` (before insert), `ACTION_PRE_OBJECT_UPD` (before update)

## DEFINITIONS.ACTION_PROBLEM

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| PRO_SRNO | NUMBER(3) | N |  |
| PROBLEM | VARCHAR2(2000) | Y |  |
| PROBLEM_TYPE_ID | NUMBER(3) | Y |  |

- **PK** `PK_ACTION_PROBLEM`: OBJECT_CODE, ACT_SRNO, PRO_SRNO
- **FK** `FK_ACTION_PROBLEM_1`: (OBJECT_CODE, ACT_SRNO) -> DEFINITIONS.OBJECT_ACTION(OBJECT_CODE, ACT_SRNO)
- **Triggers**: `ACTION_PROBLEM_DEL` (after delete), `ACTION_PROBLEM_INS` (before insert), `ACTION_PROBLEM_UPD` (before update)

## DEFINITIONS.ACTIVE_DIRECTORY_ATTRIBUTES

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTRIBUTE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |

- **Triggers**: `ACTIVE_DIRECT_ATTRIBUTES_DEL` (after delete), `ACTIVE_DIRECT_ATTRIBUTES_INS` (before insert), `ACTIVE_DIRECT_ATTRIBUTES_UPD` (before update)

## DEFINITIONS.ACTIVE_DIRECTORY_GROUPS_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_NAME | VARCHAR2(500) | Y | Name of group |
| DISPLAY_NAME | VARCHAR2(500) | Y | Name of group |
| CN_NAME | VARCHAR2(500) | Y | Name of group |
| SAM_ACCOUNT_NAME | VARCHAR2(500) | Y | Name of group unique username used to log into systems that are part of a Windows domain. |
| DESCRIPTION | VARCHAR2(500) | Y | Short description about group |
| EMAIL_ADDRESS | VARCHAR2(500) | Y | Email address on which email could be delivered |
| EMAIL_NAME_ALIAS | VARCHAR2(500) | Y | Email alias of the user, group, or contact. |
| GROUP_SCOPE | CHAR(1) default 'U' | Y | Where the group can be used (within one domain, across domains, or across forests) Who can be a member of the group (based on domain trust boundaries) G: Global L: Local U: Universal |
| GROUP_TYPE | CHAR(1) default 'D' | Y | Specifies the purpose or function of a group D = Distributed group S = Security group |
| HIDE_FROM_OUTLOOK | CHAR(1) default 'N' | Y | Hide (Y) or Unhide (N) in Outlook |
| MODERATOR_APPROVAL_REQUIRED_FOR_GROUP | CHAR(1) default 'Y' | Y | Any incoming emails to group will be approved by a moderator before being delivered to members |
| ALLOWED_EXTERNAL_EMAILS_TO_GROUP | CHAR(1) default 'Y' | Y | This attribute is used to prevent external (unauthenticated) senders from sending emails to sensitive group |
| ACTION | CHAR(1) default 'A' | Y | A= Add , D=Delete, U=Update |
| COMMITTEE_ID | VARCHAR2(9) | Y |  |
| QUEUE_DATE | DATE default SYSDATE | Y |  |
| PERFORM_DATE | DATE | Y | Will be updated by utility to log time of activity performed |
| REMARKS | VARCHAR2(4000) | Y | Will be updated by utility to log any comments/error |
| JOB_STATUS | CHAR(1) default 'P' | N | P: Pending, I: Inprocess, C: Complete H: Hold, X: Discarded. |
| RETRY_COUNT | NUMBER default 0 | Y | Will be updated by utility. Max 3 retry. |

- **Triggers**: `ACTIVE_DIRECT_GROUPS_QUEUE_DEL` (after delete), `ACTIVE_DIRECT_GROUPS_QUEUE_INS` (before insert), `ACTIVE_DIRECT_GROUPS_QUEUE_UPD` (before update), `ACTIVE_DIR_GROUP_QUEUE_DEL` (after delete)

## DEFINITIONS.ACTIVE_DIRECTORY_GROUP_QUEUE_H

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_NAME | VARCHAR2(500) | Y |  |
| DISPLAY_NAME | VARCHAR2(500) | Y |  |
| CN_NAME | VARCHAR2(500) | Y |  |
| SAM_ACCOUNT_NAME | VARCHAR2(500) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| EMAIL_ADDRESS | VARCHAR2(500) | Y |  |
| EMAIL_NAME_ALIAS | VARCHAR2(500) | Y |  |
| GROUP_SCOPE | CHAR(1) | Y |  |
| GROUP_TYPE | CHAR(1) | Y |  |
| HIDE_FROM_OUTLOOK | CHAR(1) | Y |  |
| MODERATOR_APPROVAL_REQUIRED_FOR_GROUP | CHAR(1) | Y |  |
| ALLOWED_EXTERNAL_EMAILS_TO_GROUP | CHAR(1) | Y |  |
| ACTION | CHAR(1) | Y |  |
| COMMITTEE_ID | VARCHAR2(9) | Y |  |
| QUEUE_DATE | DATE | Y |  |
| PERFORM_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| JOB_STATUS | CHAR(1) | N |  |
| RETRY_COUNT | NUMBER | Y |  |

_No standard audit columns._


## DEFINITIONS.ACTIVE_DIRECTORY_MEMBERS_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y | Email address of user/employee |
| ACTION | CHAR(1) default 'I' | Y | A= Add , D=Delete, U=Update |
| USER_NAME | VARCHAR2(500) | Y | Alias of user, mostly username without @domain_name |
| IS_GROUP_MEDERATOR | CHAR(1) default 'N' | Y | Y: Add  N: Remove - User being a moderator is authorized to approve or reject messages sent to the group.  (msExchModeratedByLink) |
| IS_AUTHORIZED_MODERATOR | CHAR(1) default 'N' | Y | Y: Add  N: Remove - By-Pass Moderation Rule - all incoming messages are sent for approval - except if the sender is listed in this attribute (msExchBypassModerationLink) |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) default 'N' | Y | Y: Add  N: Remove - The authOrig attribute lists the users or groups who are allowed to send emails to this distribution group.  (authOrig) |
| SAMACCOUNTNAME | VARCHAR2(500) | Y | The SAM account name of the group on which activity is to be performed for the current user. |
| QUEUE_DATE | DATE default SYSDATE | Y |  |
| PERFORM_DATE | DATE | Y | Will be updated by utility to log time of activity performed |
| REMARKS | VARCHAR2(4000) | Y | Will be updated by utility to log any comments/error |
| JOB_STATUS | CHAR(1) default 'P' | N | P: Pending, I: Inprocess, C: Complete H: Hold, X: Discarded. |
| RETRY_COUNT | NUMBER default 0 | Y | Will be updated by utility. Max 3 retry. |

- **Triggers**: `ACTIVE_DIRECTORY_MEMBER_Q_DEL` (after delete), `ACTIVE_DIRECT_MEMBER_QUEUE_DEL` (after delete), `ACTIVE_DIRECT_MEMBER_QUEUE_INS` (before insert), `ACTIVE_DIRECT_MEMBER_QUEUE_UPD` (before update)

## DEFINITIONS.ACTIVE_DIRECTORY_MEMBER_Q_HIST

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |
| ACTION | CHAR(1) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y |  |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y |  |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y |  |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| QUEUE_DATE | DATE | Y |  |
| PERFORM_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| JOB_STATUS | CHAR(1) | N |  |
| RETRY_COUNT | NUMBER | Y |  |

_No standard audit columns._


## DEFINITIONS.ADDICTION

| Column | Type | Null | Comment |
|---|---|---|---|
| ADDICTION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |

- **PK** `PK_ADDICTION`: ADDICTION_ID

## DEFINITIONS.ADDICTION_BUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ADDICTION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |

- **PK** `PK_ADDICTION_BUP`: ADDICTION_ID
- **Triggers**: `ADDICTION_BUP_CEA` (before insert or update or delete), `TRG_WS_TZB_SA_YB_Q` (after insert or update or delete)

## DEFINITIONS.ADDICTION_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| ADDICTION_STATUS_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |

- **PK** `PK_ADDICTION_STATUS`: ADDICTION_STATUS_ID
- **Triggers**: `ADDICTION_STATUS_CEA` (before insert or update or delete), `TRG_WS_MKM_YZ_MA_Q` (after insert or update or delete)

## DEFINITIONS.ADDITIONAL_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| STATUS | CHAR(1) | Y | O for optional , M for mandatory and L for link cpt |
| ACTIVE | CHAR(1) | Y |  |
| ALERT_TEXT | VARCHAR2(512) | Y |  |
| PROCESS | CHAR(1) | Y | A for automatically insertion, S for selection and P for previous saved orders |
| ANESTHESIA_CPT | CHAR(1) default 'N' | Y |  |
| AUTO_ORDER | CHAR(1) default 'N' | Y | Use  for location wise and order location Link CPT functional |

- **PK** `PK_ADDITIONAL_CPT_1`: CPT_ID
- **CHECK** `ADDITIONAL_CPT_1`: ACTIVE IN ('Y','N'
- **Triggers**: `ADDITIONAL_CPT_CEA` (before insert or update or delete), `ADDITIONAL_CPT_DEL` (after delete), `ADDITIONAL_CPT_INS` (before insert), `ADDITIONAL_CPT_UPD` (before update), `TRG_WS_HNO_JM_YI_Q` (after insert or update or delete)

## DEFINITIONS.ADDITIONAL_CPT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| SERIAL_NO | NUMBER(3) | N |  |
| LINKED_CPT_ID | VARCHAR2(18) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CPT_LINK_DETAIL`: CPT_ID, SERIAL_NO
- **FK** `FK_CPT_LINK_DETAIL_1`: (CPT_ID) -> DEFINITIONS.ADDITIONAL_CPT(CPT_ID)
- **Triggers**: `ADDITIONAL_CPT_DETAIL_CEA` (before insert or update or delete), `ADDITIONAL_CPT_DETAIL_DEL` (after delete), `ADDITIONAL_CPT_DETAIL_INS` (before insert), `ADDITIONAL_CPT_DETAIL_UPD` (before update), `TRG_WS_YNF_AN_AT_Q` (after insert or update or delete)

## DEFINITIONS.ADDITIONAL_CPT_LOCATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ADDITIONAL_CPT_LOCATIONS`: CPT_ID, LOCATION_ID
- **Triggers**: `ADDITIONAL_CPT_LOCATIONS_CEA` (before insert or update or delete), `ADDITIONAL_CPT_LOCATIONS_DEL` (after delete), `ADDITIONAL_CPT_LOCATIONS_INS` (before insert), `ADDITIONAL_CPT_LOCATIONS_UPD` (before update), `TRG_WS_INH_HI_UY_Q` (after insert or update or delete)

## DEFINITIONS.ADDRESS_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ADDRESS_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ADDRESS_TYPE`: ADDRESS_TYPE_ID
- **Triggers**: `ADDRESS_TYPE_CEA` (before insert or update or delete), `ADDRESS_TYPE_DEL` (after delete), `ADDRESS_TYPE_INS` (before insert), `ADDRESS_TYPE_UPD` (before update), `TRG_WS_QLQ_QK_WK_Q` (after insert or update or delete)

## DEFINITIONS.ADD_CPT_ORDER_LOCATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| RESTRICTION_TYPE | VARCHAR2(1) | Y | A for Allowed, R for Restrict |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ADD_CPT_ORDER_LOCATIONS`: CPT_ID, LOCATION_ID, ORDER_LOCATION_ID
- **Triggers**: `ADD_CPT_ORDER_LOCATIONS_CEA` (before insert or update or delete), `ADD_CPT_ORDER_LOCATIONS_DEL` (after delete), `ADD_CPT_ORDER_LOCATIONS_INS` (before insert), `ADD_CPT_ORDER_LOCATIONS_UPD` (before update), `TRG_WS_ZZM_NE_FO_Q` (after insert or update or delete)

## DEFINITIONS.ADJUSTMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ADJ_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ADJUSTMENT_TYPE`: ADJ_TYPE_ID, LOCATION_ID
- **Triggers**: `ADJUSTMENT_TYPE_CEA` (before insert or update or delete), `TRG_WS_RBA_AJ_QR_Q` (after insert or update or delete)

## DEFINITIONS.ADMIN_COSTING

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| REFFER_TO_SHARE_HOLDER | VARCHAR2(1) | Y |  |
| DISTRIBUTABLE | VARCHAR2(1) | N |  |
| SHARE_FLAG | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PRINTABLE | CHAR(1) default 'N' | Y |  |
| COSTING_CATEGORY | CHAR(1) default 'O' | N | 'D Doctor', 'T Tech', 'O Other', 'S Supplies', 'R Room Charges' |
| PRACTICE_INCOME | CHAR(1) default 'N' | N | Y means that is a share that can be paid to the performer N Means its not a share distributable |

- **PK** `PK_ADMIN_COSTING`: ADMIN_COSTING_ID
- **CHECK** `CHK_ADMIN_COSTING_02`: DISTRIBUTABLE = UPPER(DISTRIBUTABLE
- **CHECK** `CHK_ADMIN_COSTING_03`: DISTRIBUTABLE IN ('Y','N'
- **CHECK** `CHK_ADMIN_COSTING_1`: COSTING_CATEGORY IN ('D','T','O','S','R'
- **Triggers**: `ADMIN_COSTING_CEA` (before insert or update or delete), `ADMIN_COSTING_DEL` (after delete), `ADMIN_COSTING_INS` (before insert), `ADMIN_COSTING_UPD` (before update), `TRG_WS_GCI_OT_JF_Q` (after insert or update or delete)

## DEFINITIONS.ADMISSION_CANCEL_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | N |  |
| ADM_CANCEL_REASON_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **CHECK** `CK_ADMISSION_CANCEL_REASON_001`: ACTIVE IN ('N','Y'

## DEFINITIONS.ADMISSION_FOR_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMISSION_FOR_ID | NUMBER(4) | N |  |
| ADMISSION_FOR_DESC | VARCHAR2(100) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ENTERED_BY | VARCHAR2(14) | N |  |
| ENTERED_DATE | DATE | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_ADMISSION_FOR_SETUP`: ADMISSION_FOR_ID
- **Triggers**: `ADMISSION_FOR_SETUP_CEA` (before insert or update or delete), `ADMISSION_FOR_SETUP_DEL` (after delete), `ADMISSION_FOR_SETUP_INS` (before insert), `ADMISSION_FOR_SETUP_UPD` (before update), `TRG_WS_UDK_HB_XL_Q` (after insert or update or delete)

## DEFINITIONS.ADMISSION_GOALS
Goals Of Admission will be entered in this setup table.

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(5) | N |  |
| GOAL_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ADMISSION_GOALS`: REASON_ID, GOAL_ID
- **Triggers**: `ADMISSION_GOALS_CEA` (before insert or update or delete), `TRG_WS_BWG_RP_GP_Q` (after insert or update or delete)

## DEFINITIONS.ADMISSION_REASONS
Admission Reasons will be entered in this setup table.

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ADMSSION_REASONS`: REASON_ID
- **Triggers**: `ADMISSION_REASONS_CEA` (before insert or update or delete), `TRG_WS_XIY_PV_NQ_Q` (after insert or update or delete)

## DEFINITIONS.ADMISSION_TYPE_CPT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMISSION_TYPE | VARCHAR2(3) | N |  |
| CPT_ID | VARCHAR2(20) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_ADMISSION_TYPE_CPT_SETUP`: ADMISSION_TYPE, CPT_ID
- **Triggers**: `ADMISSION_TYPE_CPT_SETUP_CEA` (before insert or update or delete), `TRG_WS_CMO_MS_AR_Q` (after insert or update or delete)

## DEFINITIONS.ADR_REPORTING_VALIDITY

| Column | Type | Null | Comment |
|---|---|---|---|
| ADR_REPORTED | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_ADR_REPORTING_VALIDITY`: ADR_REPORTED
- **Triggers**: `ADR_REPORTING_VALIDITY_CEA` (before insert or update or delete), `ADR_REPORTING_VALIDITY_DEL` (after delete), `ADR_REPORTING_VALIDITY_INS` (before insert), `ADR_REPORTING_VALIDITY_UPD` (before update), `TRG_WS_EFO_CM_PJ_Q` (after insert or update or delete)

## DEFINITIONS.ADVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_ADVICES`: ID
- **Triggers**: `ADVICES_CEA` (before insert or update or delete), `ADVICES_DEL` (after delete), `ADVICES_INS` (before insert), `ADVICES_UPD` (before update), `TRG_WS_OVT_RE_UP_Q` (after insert or update or delete)

## DEFINITIONS.AD_COMMITTEE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DESCRIPTION | VARCHAR2(4000) | N |  |
| SHORT_DESC | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| TYPE_ID | NUMBER | Y |  |
| ORGANIZING_DEPT_ID | VARCHAR2(7) | Y |  |
| AD_ATTRIBUTE_ID | NUMBER | Y |  |
| SAM_ACCOUNT_NAME | VARCHAR2(500) | N | Name of group unique username used to log into systems that are part of a Windows domain. |
| EMAIL_ADDRESS | VARCHAR2(500) | N | Email address on which email could be delivered |
| EMAIL_NAME_ALIAS | VARCHAR2(500) | N | Email alias of the user, group, or contact. |
| GROUP_SCOPE | CHAR(1) default 'U' | Y | Where the group can be used (within one domain, across domains, or across forests) Who can be a member of the group (based on domain trust boundaries) G: Global L: Local U: Universal |
| GROUP_TYPE | CHAR(1) default 'D' | Y | Specifies the purpose or function of a group D = Distributed group S = Security group |
| HIDE_FROM_OUTLOOK | CHAR(1) default 'N' | Y |  |
| MODERATOR_APPROVAL_REQUIRED_FOR_GROUP | CHAR(1) default 'Y' | Y | Any incoming emails to group will be approved by a moderator before being delivered to members |
| ALLOWED_EXTERNAL_EMAILS_TO_GROUP | CHAR(1) default 'Y' | Y | This attribute is used to prevent external (unauthenticated) senders from sending emails to sensitive |
| ORGANIZER_EMAIL | VARCHAR2(500) | Y | If more than one email than kindly add ; separated |

- **UK** `UK_EMAIL_01`: EMAIL_ADDRESS
- **UK** `UK_EMAIL_ALIAS_01`: EMAIL_NAME_ALIAS
- **UK** `UK_SAM_NAME_01`: SAM_ACCOUNT_NAME
- **Triggers**: `AD_COMMITTEE_DEL` (after delete), `AD_COMMITTEE_GROUPS_QUEUE_TRG` (after insert or update or delete), `AD_COMMITTEE_INS` (before insert), `AD_COMMITTEE_UPD` (before update), `TRG_AD_COMMITTEE_ID` (before insert)

## DEFINITIONS.AD_COMMITTEE_DEPARTMENT_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_AD_COMMITTEE_DEPARTMENT_WISE_01`: COMMITTEE_ID, DEPARTMENT_ID
- **Triggers**: `AD_COMMITTEE_DEPARTMENT_WISE_QUEUE_DEL` (after delete), `AD_COMMITTEE_DEPARTMENT_WISE_QUEUE_INS` (before insert), `AD_COMMITTEE_DEPT_WISE_DEL` (after delete), `AD_COMMITTEE_DEPT_WISE_INS` (before insert), `AD_COMMITTEE_DEPT_WISE_UPD` (before update), `AD_COMMIT_DEPT_WISE_QUEUE_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_DEPT_SECTION_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y |  |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y |  |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y |  |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |
| SECTION_ID | VARCHAR2(7) | N |  |

- **PK** `PK_AD_COMMITTEE_DEPT_SECTION_WISE_01`: COMMITTEE_ID, DEPARTMENT_ID, SECTION_ID
- **Triggers**: `AD_COMMITTEE_DEPT_SECTION_WISE_UPD` (before update), `AD_COMMITTEE_DEPT_SEC_Q_INS` (before insert), `AD_COMMITTEE_DEPT_SEC_WISE_DEL` (after delete), `AD_COMT_DEPT_SEC_WISE_DEL` (after delete), `AD_COMT_DEPT_SEC_WISE_INS` (before insert), `AD_COMT_DEPT_SEC_WISE_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_DESIGNATION_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_AD_COMMITTEE_DESIGNATION_WISE_01`: COMMITTEE_ID, DESIGNATION_ID
- **Triggers**: `AD_COMMITTEE_DESIGNATION_WISE_QUEUE_DEL` (after delete), `AD_COMMITTEE_DESIGNATION_WISE_QUEUE_INS` (before insert), `AD_COMMITTEE_DESIGNATION_WISE_UPD` (before update), `AD_COMMITTEE_DESIG_WISE_DEL` (after delete), `AD_COMMITTEE_DESIG_WISE_INS` (before insert), `AD_COMMITTEE_DESIG_WISE_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_DESIG_CATEG_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DESIGNATION_CATEGOTY_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_AD_COMMITTEE_DESIG_CATEG_WISE_01`: COMMITTEE_ID, DESIGNATION_CATEGOTY_ID
- **Triggers**: `AD_COMMITTEE_DESIG_CATEG_WISE_QUEUE_DEL` (after delete), `AD_COMMITTEE_DESIG_CATEG_WISE_QUEUE_INS` (before insert), `AD_COMMITTEE_DESIG_CATEG_WISE_UPD` (before update), `AD_COMMIT_DESIG_CAT_WISE_DEL` (after delete), `AD_COMMIT_DESIG_CAT_WISE_INS` (before insert), `AD_COMMIT_DESIG_CAT_WISE_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_EXEMPTION_LIST

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_AD_COMMITTEE_EXEMPTION_LIST_01`: COMMITTEE_ID, EMP_CODE
- **Triggers**: `AD_COMMITTEE_EXEMPT_LIST_Q_DEL` (after delete), `AD_COMMITTEE_EXEMPT_LIST_Q_INS` (before insert), `AD_COMMITTEE_EXEMP_LIST_DEL` (after delete), `AD_COMMITTEE_EXEMP_LIST_INS` (before insert), `AD_COMMITTEE_EXEMP_LIST_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_EXEMPT_LIST_DESIG

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_EXP_DESG_AD_01`: COMMITTEE_ID, DESIGNATION_ID
- **Triggers**: `AD_COMMITTEE_EXEMPT_LIST_DESIG_Q_INS` (before insert), `AD_COMMIT_EXMPT_LIST_DESIG_DEL` (after delete), `AD_COMMIT_EXMPT_LIST_DESIG_INS` (before insert), `AD_COMMIT_EXMPT_LIST_DESIG_UPD` (before update), `AD_COMT_EXMPT_LIST_DESIG_Q_DEL` (after delete)

## DEFINITIONS.AD_COMMITTEE_MEMBERS

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Y: Add user N: Remove user |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Y: Add user in list of by-passed moderators N: Remove User in list of by-passed moderators |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y | N/A It is a multi-valued attribute that holds the Distinguished Names (DNs) of authorized senders |
| SAMACCOUNTNAME | VARCHAR2(500) | Y |  |
| USER_NAME | VARCHAR2(500) | Y |  |
| USER_EMAIL | VARCHAR2(500) | Y |  |

- **PK** `PK_AD_COMMITTEE_MEMBERS_01`: COMMITTEE_ID, EMP_CODE
- **Triggers**: `AD_COMMITTEE_MEMBERS_DEL` (after delete), `AD_COMMITTEE_MEMBERS_INS` (before insert), `AD_COMMITTEE_MEMBERS_QUEUE_DEL` (after delete), `AD_COMMITTEE_MEMBERS_QUEUE_INS` (before insert), `AD_COMMITTEE_MEMBERS_QUEUE_UPD` (before update), `AD_COMMITTEE_MEMBERS_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_AD_COMMITTEE_RIGHTS_01`: COMMITTEE_ID, EMP_CODE
- **Triggers**: `AD_COMMITTEE_RIGHTS_DEL` (after delete), `AD_COMMITTEE_RIGHTS_INS` (before insert), `AD_COMMITTEE_RIGHTS_UPD` (before update)

## DEFINITIONS.AD_COMMITTEE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AD_COMMITTEE_TYPE_01`: TYPE_ID
- **Triggers**: `AD_COMMITTEE_TYPE_DEL` (after delete), `AD_COMMITTEE_TYPE_INS` (before insert), `AD_COMMITTEE_TYPE_UPD` (before update), `TRG_AD_COMMITTEE_TYPE_ID` (before insert)

## DEFINITIONS.AD_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| GROUP_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_AD_GROUPS_01`: GROUP_ID
- **Triggers**: `TRG_AD_GROUPS_ID` (before insert)

## DEFINITIONS.AD_GROUPS_CREATION_QUEUE
Queue table for managing Active Directory group creation requests

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_NAME | VARCHAR2(500) | Y | Internal group name |
| DISPLAY_NAME | VARCHAR2(500) | Y | Display name shown to users |
| CN_NAME | VARCHAR2(500) | Y | Common Name (CN) in Active Directory |
| SAM_ACCOUNT_NAME | VARCHAR2(500) | Y | SAM account name (unique in AD) |
| DESCRIPTION | VARCHAR2(500) | Y | Description of the group |
| EMAIL_ADDRESS | VARCHAR2(500) | Y | Associated email address |
| EMAIL_NAME_ALIAS | VARCHAR2(500) | Y | Email alias |
| GROUP_SCOPE | CHAR(1) | Y | D=Domain Local, G=Global, U=Universal |
| GROUP_TYPE | CHAR(1) | Y | S=Security, D=Distribution |
| HIDE_FROM_OUTLOOK | CHAR(1) | Y | Y/N flag to hide group from Outlook |
| MODERATOR_APPROVAL_REQUIRED_FOR_GROUP | CHAR(1) | Y | Y/N flag indicating if moderator approval is required |
| ALLOWED_EXTERNAL_EMAILS_TO_GROUP | CHAR(1) | Y | Y/N flag for allowing external emails |
| ACTION | CHAR(1) | Y | I=Insert, U=Update, D=Delete |
| COMMITTEE_ID | VARCHAR2(9) | Y | Linked committee ID |
| QUEUE_DATE | DATE | Y | Date when the record was queued |
| PERFORM_DATE | DATE | Y | Date when the action should be performed |
| REMARKS | VARCHAR2(4000) | Y | Processing remarks or error details |
| JOB_STATUS | CHAR(1) | N | Status of the job: Pending, In Progress, Completed, Failed |
| RETRY_COUNT | NUMBER | Y | Number of retry attempts |
| IS_ACKNOWLEDGED | CHAR(1) default 'N' | Y | Y/N flag indicating acknowledgment |
| ACKNOWLEDGED_BY | VARCHAR2(14) | Y | User who acknowledged the record |
| ACKNOWLEDGED_DATE | DATE | Y | Date when the record was acknowledged |

_No standard audit columns._


## DEFINITIONS.AD_GROUPS_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_AD_GROUPS_DEPT_01`: GROUP_ID
- **Triggers**: `TRG_AD_GROUPS_DEPT_ID` (before insert)

## DEFINITIONS.AD_GROUPS_DESIG

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._

- **PK** `PK_AD_GROUPS_DESIG_01`: GROUP_ID
- **Triggers**: `TRG_AD_GROUPS_DESIG_ID` (before insert)

## DEFINITIONS.AD_GROUP_DEPT_MEMBERS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## DEFINITIONS.AD_GROUP_DEPT_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## DEFINITIONS.AD_GROUP_DESIG_MEMBERS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## DEFINITIONS.AD_GROUP_DESIG_RIGHTS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(9) | Y |  |
| EMP_CODE | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## DEFINITIONS.AD_MEMBER_CHANGE_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMITTEE_ID | VARCHAR2(9) | Y | ID of the committee the member belongs to |
| EMP_CODE | VARCHAR2(14) | Y | Employee code associated with the member |
| USER_EMAIL | VARCHAR2(500) | Y | Email address of the user |
| ACTION | CHAR(1) | Y | Action performed on the member: A (Add), D (Delete), U (Update) |
| USER_NAME | VARCHAR2(500) | Y | Full name of the user |
| IS_GROUP_MEDERATOR | CHAR(1) | Y | Indicates if the user is a group moderator (Y/N) |
| IS_AUTHORIZED_MODERATOR | CHAR(1) | Y | Indicates if the user is an authorized moderator (Y/N) |
| IS_AUTHORIZED_ORIGINATOR | VARCHAR2(50) | Y |  |
| SAMACCOUNTNAME | VARCHAR2(500) | Y | SAMAccountName (unique identifier) for the user in Active Directory |
| QUEUE_DATE | DATE | Y | Date when the change was queued |
| PERFORM_DATE | DATE | Y | Date when the change is to be performed |
| REMARKS | VARCHAR2(4000) | Y | Additional remarks regarding the change |
| JOB_STATUS | CHAR(1) | N | Status of the job: Pending, In Progress, Completed, Failed |
| RETRY_COUNT | NUMBER | Y | Number of retry attempts if the job fails |
| IS_ACKNOWLEDGED | CHAR(1) default 'N' | Y | Flag indicating whether the change has been acknowledged (Y/N) |
| ACKNOWLEDGED_BY | VARCHAR2(14) | Y | User who acknowledged the change |
| ACKNOWLEDGED_DATE | DATE | Y | Date when the change was acknowledged |

_No standard audit columns._


## DEFINITIONS.AFFILIATION

| Column | Type | Null | Comment |
|---|---|---|---|
| AFFILIATION_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESC | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AFFILIATION`: AFFILIATION_ID
- **CHECK** `CK_AFFILIATION_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `AFFILIATION_CEA` (before insert or update or delete), `AFFILIATION_TS` (before insert or update or delete), `TRG_WS_GRA_PF_AC_Q` (after insert or update or delete)

## DEFINITIONS.AGENT_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| AGENT_ID | NUMBER | N |  |
| AGENT_NAME | VARCHAR2(50) | N |  |
| AGENT_PURPOSE | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

_No standard audit columns._

- **PK** `PK_AGENT_MASTER`: AGENT_ID

## DEFINITIONS.AGENT_DETAILS

| Column | Type | Null | Comment |
|---|---|---|---|
| AGENT_ID | NUMBER | N |  |
| AGENT_DETAIL_ID | NUMBER | N |  |
| TASK_DETAILS | VARCHAR2(100) | N |  |
| DATA_CRITERIA_QUERY | CLOB | N |  |
| DATA_SELECTION_QUERY | CLOB | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SUMMARY_TYPE | VARCHAR2(1) | Y |  |
| REDUCE_PROMPT | CLOB | Y |  |
| MAP_PROMPT | CLOB | Y |  |

_No standard audit columns._

- **PK** `PK_AGENT_DETAILS`: AGENT_ID, AGENT_DETAIL_ID
- **FK** `FK_AGENT_DETAILS_01`: (AGENT_DETAIL_ID) -> DEFINITIONS.AGENT_MASTER(AGENT_ID)

## DEFINITIONS.AGENT_SCHEDULE

| Column | Type | Null | Comment |
|---|---|---|---|
| AGENT_SCHEDULE_ID | NUMBER | N |  |
| AGENT_ID | NUMBER | Y |  |
| AGENT_DETAIL_ID | NUMBER | Y |  |
| AGENT_TIME | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |

_No standard audit columns._

- **PK** `PK_AGENT_SCHEDULE`: AGENT_SCHEDULE_ID
- **FK** `FK_AGENT_SCHEDULE_01`: (AGENT_ID, AGENT_DETAIL_ID) -> DEFINITIONS.AGENT_DETAILS(AGENT_ID, AGENT_DETAIL_ID)

## DEFINITIONS.AGE_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| AGE_GROUP_ID | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| SHORT_DESC | VARCHAR2(10) | Y |  |
| AGE_LOWER_LIMIT | NUMBER(6,3) | Y |  |
| AGE_UPPER_LIMIT | NUMBER(6,3) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AGE_GROUPS`: AGE_GROUP_ID
- **CHECK** `CK_AGE_GROUPS_001`: ACTIVE IN ('Y','N'
- **Triggers**: `AGE_GROUPS_CEA` (before insert or update or delete), `TRG_WS_FFI_VF_JK_Q` (after insert or update or delete)

## DEFINITIONS.AI_MODELS

| Column | Type | Null | Comment |
|---|---|---|---|
| MODEL_ID | NUMBER | N |  |
| MODEL_NAME | VARCHAR2(200) | Y |  |
| MODEL_TYPE | VARCHAR2(10) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| MODEL_PROVIDER_ID | NUMBER | Y |  |

- **PK** `PK_AI_MODELS`: MODEL_ID

## DEFINITIONS.AI_MODELS_APPS_DETAILS

| Column | Type | Null | Comment |
|---|---|---|---|
| MODEL_DETAILS_ID | NUMBER | N |  |
| APP_ID | NUMBER | Y |  |
| MODEL_ID | NUMBER | Y |  |
| PURPOSE | VARCHAR2(2000) | Y |  |
| SEED | NUMBER default 0 | Y |  |
| URL | VARCHAR2(500) | Y |  |
| MAX_RETRIES | NUMBER default 3 | Y |  |
| KEEP_ALIVE | VARCHAR2(50) default '1m' | Y |  |
| TEMPERATURE | FLOAT default 0 | Y |  |
| CONTEXT_SIZE | NUMBER | Y |  |
| NUM_PREDICT | NUMBER | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_AI_MODELS_APPS_DETAILS`: MODEL_DETAILS_ID
- **FK** `FK_AI_MODELS`: (MODEL_ID) -> DEFINITIONS.AI_MODELS(MODEL_ID)

## DEFINITIONS.AI_MODEL_PROVIDER

| Column | Type | Null | Comment |
|---|---|---|---|
| MODEL_PROVIDER_ID | NUMBER | Y |  |
| MODEL_PROVIDER | VARCHAR2(50) | Y |  |

_No standard audit columns._


## DEFINITIONS.ALERT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | N |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_ALERT_TYPE`: ALERT_TYPE_ID
- **Triggers**: `ALERT_TYPE_CEA` (before insert or update or delete), `ALERT_TYPE_DEL` (after delete), `ALERT_TYPE_INS` (before insert), `ALERT_TYPE_UPD` (before update), `TRG_WS_WUK_LJ_LK_Q` (after insert or update or delete)

## DEFINITIONS.ALERT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | NUMBER(3) | N |  |
| ALERT_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | N |  |
| SHORT_DESC | VARCHAR2(100) | N |  |
| SEVERITY | VARCHAR2(50) | Y |  |
| COLOR_CODE | VARCHAR2(20) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ASSIGNMENT_ID | NUMBER(3) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ALERT_TEXT | VARCHAR2(1000) | Y | Alert Text to display on user screen will be stored in this column. |
| APP_ID | NUMBER | Y |  |
| PAGE_ID | NUMBER | Y |  |

- **PK** `PK_ALERT_SETUP`: ALERT_ID
- **FK** `FK_ALERT_SETUP_01`: (ALERT_TYPE_ID) -> DEFINITIONS.ALERT_TYPE(ALERT_TYPE_ID) [disabled]
- **FK** `FK_ALERT_SETUP_02`: (ASSIGNMENT_ID) -> HIS.USER_ASSIGNMENT(ASSIGNMENT_ID) [disabled]
- **FK** `FK_ALERT_SETUP_03`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **Triggers**: `ALERT_SETUP_CEA` (before insert or update or delete), `ALERT_SETUP_DEL` (after delete), `ALERT_SETUP_INS` (before insert), `ALERT_SETUP_UPD` (before update), `TRG_WS_TFW_RE_OB_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N | Specify already defined object code as 'S07FRM00076' |
| PARAM_ID | NUMBER | N | Auto generated from sequence DEFINITIONS.OBJECT_PARAM_ID |
| PARAM_NAME | VARCHAR2(100) | Y | Enter parameter name as declared on object as 'P_MRNO' |
| PARAM_DISPLAY_NAME | VARCHAR2(100) | Y | Enter parameter display name; a meaningful text that will be comprehensive for user as 'Employee Code' for parameter name 'P_MRNO' |
| PARAM_DATA_TYPE | VARCHAR2(100) | Y | Store paraneter data type ex. varchar2, date, number etc |
| PARAM_REQUIRED | CHAR(1) default 'N' | Y | Enter 'Y' or 'N' to specify; selected parameter is mandatory or not |
| PARAM_REQUIRED_ALERT | VARCHAR2(2000) | Y | If Param_required is set to 'Y' then enter text that will appear to user like 'Enter employee code' |
| PARAM_CHECK_DEFAULT | CHAR(1) default 'N' | Y | Enter 'Y' or 'N' to specify if selected parameter is default value wants to use |
| PARAM_DEFAULT_VALUE | VARCHAR2(100) | Y | Enter default value of parameter value (Ex: for P_LOCATION_ID it will be 'SKMCH & RC') |
| PARAM_QUERY | VARCHAR2(3000) | Y | Specify query as to appear on column in form of LOV. It should contains 2 fields; ID and description |
| PARAM_DISPLAY | CHAR(1) default 'N' | Y | Enter 'Y' or 'N' to specify if selected parameter is display on form |
| FRONTEND_SOURCE | VARCHAR2(100) | Y | Field name as passed from form (Ex. PARAMETER.FROM_DATE) |
| PARAM_ORDER_BY | NUMBER | Y | Specify parameter order number as appear to user |
| PARAM_DEFAULT_RG_ID | VARCHAR2(100) | Y | Enter default value of parameter id (Ex: for P_LOCATION_ID it will be '001') |
| CONSTANT_ID | NUMBER(2) | Y |  |
| CONSTANT_NAME | VARCHAR2(100) | Y |  |
| CONSTANT_DATA_TYPE | VARCHAR2(100) | Y |  |

- **PK** `PK_OBJECT_PARAMETERS`: PARAM_ID
- **UK** `UK_OBJECT_PARAMETERS_1`: OBJECT_CODE, PARAM_NAME
- **FK** `FK_OBJECT_PARAMETERS_01`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **CHECK** `CK_OBJECT_PARAMETERS_1`: PARAM_REQUIRED IN ('Y','N'
- **CHECK** `CK_OBJECT_PARAMETERS_2`: PARAM_CHECK_DEFAULT IN ('Y','N'
- **CHECK** `CK_OBJECT_PARAMETERS_3`: PARAM_DISPLAY IN ('Y','N'
- **CHECK** `CK_OBJECT_PARAMETERS_4`: PARAM_NAME = UPPER(PARAM_NAME
- **Triggers**: `OBJECT_PARAMETERS_DEL` (after delete), `OBJECT_PARAMETERS_INS` (before insert), `OBJECT_PARAMETERS_NEW_ID` (before insert), `OBJECT_PARAMETERS_UPD` (before update)

## DEFINITIONS.ALERT_OBJECT_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | NUMBER(3) | N |  |
| PARAM_ID | NUMBER | N |  |
| PARAM_VALUE_TYPE | CHAR(1) | Y | Define parameter value as 'S' for static and 'D' for Dynamic. Static means value will not be changed and for Dynamic you have to define the source either in DEFAULT_VALUE or FRONTEND_SOURCE column |
| DEFAULT_VALUE | VARCHAR2(100) | Y | define default value for the parameter like 001 |
| FRONTEND_SOURCE | VARCHAR2(100) | Y | Mention item name thats value will be passed to this parameter like CONTROL.USER_MRNO |
| DYNAMIC_STATEMENT | VARCHAR2(4000) | Y |  |

- **PK** `PK_ALERT_OBJECT_PARAM`: ALERT_ID, PARAM_ID
- **FK** `FK_ALERT_OBJECT_PARAM_01`: (ALERT_ID) -> DEFINITIONS.ALERT_SETUP(ALERT_ID)
- **FK** `FK_ALERT_OBJECT_PARAM_02`: (PARAM_ID) -> DEFINITIONS.OBJECT_PARAMETERS(PARAM_ID) [disabled]
- **CHECK** `CHK_ALERT_OBJECT_PARAM_01`: PARAM_VALUE_TYPE IN ('S','D'
- **Triggers**: `ALERT_OBJECT_PARAM_DEL` (after delete), `ALERT_OBJECT_PARAM_INS` (before insert), `ALERT_OBJECT_PARAM_UPD` (before update)

## DEFINITIONS.ALERT_OBJECT_PARAM_COPY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | NUMBER(3) | N |  |
| PARAM_ID | NUMBER | N |  |
| PARAM_VALUE_TYPE | CHAR(1) | Y |  |
| DEFAULT_VALUE | VARCHAR2(100) | Y |  |
| FRONTEND_SOURCE | VARCHAR2(100) | Y |  |
| DYNAMIC_STATEMENT | VARCHAR2(4000) | Y |  |

- **Triggers**: `ALERT_OBJECT_PARAM_COPY_R_CEA` (before insert or update or delete), `TRG_WS_FSU_MC_KS_Q` (after insert or update or delete)

## DEFINITIONS.ALLERGY_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLERGY_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_ALLERGY_TYPE`: ALLERGY_TYPE_ID
- **Triggers**: `ALLERGY_TYPE_CEA` (before insert or update or delete), `ALLERGY_TYPE_DEL` (after delete), `ALLERGY_TYPE_INS` (before insert), `ALLERGY_TYPE_UPD` (before update), `TRG_WS_UGI_XH_LD_Q` (after insert or update or delete)

## DEFINITIONS.ALLERGY_REVIEW_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLERGY_TYPE_ID | VARCHAR2(3) | N | 001-> DRUG ALLERGY, 002-> FOOD ALERGY, 003-> UNLISTED ALLERGIES |
| ROLE_ID | NUMBER(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ALLERGY_REVIEW_SETUP`: ALLERGY_TYPE_ID, ROLE_ID, LOC_ID
- **FK** `FK_ALLERGY_REVIEW_SETUP`: (ALLERGY_TYPE_ID) -> DEFINITIONS.ALLERGY_TYPE(ALLERGY_TYPE_ID)
- **Triggers**: `ALLERGY_REVIEW_SETUP_DEL` (after delete), `ALLERGY_REVIEW_SETUP_INS` (before insert), `ALLERGY_REVIEW_SETUP_UPD` (before update)

## DEFINITIONS.ALLOWANCE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALLOWANCE_TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SHORT_DESC | VARCHAR2(25) | Y |  |
| SEQ_NO | NUMBER(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ALLOWANCE_TYPE`: ALLOWANCE_TYPE_ID
- **Triggers**: `ALLOWANCE_TYPE_CEA` (before insert or update or delete), `ALLOWANCE_TYPE_DEL` (after delete), `ALLOWANCE_TYPE_INS` (before insert), `ALLOWANCE_TYPE_UPD` (before update), `TRG_WS_BVV_HV_DC_Q` (after insert or update or delete)

## DEFINITIONS.ALL_CURRENCIES

| Column | Type | Null | Comment |
|---|---|---|---|
| SHORT_DESCRIPTION | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SYMBOL | VARCHAR2(4) | Y |  |

- **PK** `PK_ALL_CURRENCIES`: SHORT_DESCRIPTION
- **Triggers**: `ALL_CURRENCIES_CEA` (before insert or update or delete), `ALL_CURRENCIES_DEL` (after delete), `ALL_CURRENCIES_INS` (before insert), `ALL_CURRENCIES_UPD` (before update), `TRG_WS_SQD_FJ_IL_Q` (after insert or update or delete)

## DEFINITIONS.ANSWERS

| Column | Type | Null | Comment |
|---|---|---|---|
| ANSWER_ID | VARCHAR2(9) | N |  |
| ANSWER_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ANSWER`: ANSWER_ID
- **Triggers**: `ANSWERS_CEA` (before insert or update or delete), `ANSWERS_DEL` (after delete), `ANSWERS_INS` (before insert), `ANSWERS_UPD` (before update), `TRG_WS_ODT_DC_DY_Q` (after insert or update or delete)

## DEFINITIONS.APACHE_IV_CHISYS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| NAME | VARCHAR2(100) | Y |  |

_No standard audit columns._


## DEFINITIONS.APACHE_IV_CHIDIA

| Column | Type | Null | Comment |
|---|---|---|---|
| SYSTEM_ID | NUMBER | N |  |
| DETAIL_ID | NUMBER | N |  |
| DIAGNOSIS | VARCHAR2(100) | Y |  |
| VCHIDIA | NUMBER | Y |  |
| V2CHIDIA | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_APACHE_IV_CHISYS`: SYSTEM_ID, DETAIL_ID
- **FK** `FK_APACHE_IV_CHISYS`: (SYSTEM_ID) -> DEFINITIONS.APACHE_IV_CHISYS(ID)

## DEFINITIONS.APACHE_IV_MEDSYS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| NAME | VARCHAR2(100) | Y |  |

_No standard audit columns._


## DEFINITIONS.APACHE_IV_MEDDIA

| Column | Type | Null | Comment |
|---|---|---|---|
| SYSTEM_ID | NUMBER | N |  |
| DETAIL_ID | NUMBER | N |  |
| DIAGNOSIS | VARCHAR2(100) | Y |  |
| VMEDDIA | NUMBER | Y |  |
| V2MEDDIA | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_MEDDIA_SYSTEM`: SYSTEM_ID, DETAIL_ID
- **FK** `FK_MEDDIA_SYSTEM`: (SYSTEM_ID) -> DEFINITIONS.APACHE_IV_MEDSYS(ID)

## DEFINITIONS.API_CONFIGURATION_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| API_NAME | VARCHAR2(500) | N |  |
| APP_URL | VARCHAR2(100) | N |  |
| PROC_NAME | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| API_CONFIG_ID | NUMBER | N |  |

_No standard audit columns._

- **PK** `PK_API_CONFIGURATION_MASTER`: API_CONFIG_ID

## DEFINITIONS.API_CONFIGURATION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| API_CONFIG_ID | NUMBER | Y |  |
| VARIABLE_NAME | VARCHAR2(200) | Y | JSON api keys |
| DISPLAY_ORDER | NUMBER | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| API_CONFIG_DETAIL_ID | NUMBER | N |  |
| COLUMN_NAME | VARCHAR2(50) | Y | Column reference of Table or Page Item |
| REFERENCE_OBJECT | VARCHAR2(100) | Y | Contain Object Name e.g. Table, View , Application ,Page etc. |

_No standard audit columns._

- **PK** `PK_API_CONFIGURATION_DETAIL`: API_CONFIG_DETAIL_ID
- **FK** `FK_API_CONFIGURATION_DETAIL`: (API_CONFIG_ID) -> DEFINITIONS.API_CONFIGURATION_MASTER(API_CONFIG_ID)

## DEFINITIONS.API_REGISTRY

| Column | Type | Null | Comment |
|---|---|---|---|
| API_ID | VARCHAR2(10) | N |  |
| API_NAME | VARCHAR2(500) | Y |  |
| AS_NAME | VARCHAR2(500) | Y |  |
| IS_SECURE_LINK | CHAR(1) | Y |  |
| API_PROTOCOL | VARCHAR2(50) | Y |  |
| API_ACCESS | VARCHAR2(50) | Y |  |
| API_HOST | VARCHAR2(4000) | Y |  |
| API_PORT | VARCHAR2(6) | Y |  |
| API_CONTEXT_PATH | VARCHAR2(4000) | Y |  |
| FULL_API_URL | VARCHAR2(4000) | Y |  |
| HTTP_METHOD | VARCHAR2(50) | Y |  |
| API_EXAMPLE | CLOB | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| FILE_NAME | VARCHAR2(500) | Y |  |
| IS_ACTIVE | CHAR(1) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_API_REGISTRY`: API_ID
- **Triggers**: `API_REGISTRY_INS` (before insert), `API_REGISTRY_NEW_ID` (before insert)

## DEFINITIONS.APPEARANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPEARANCE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_APPEARANCE`: APPEARANCE_ID
- **CHECK** `CK_APPEARANCE_001`: ACTIVE IN ('Y','N')
- **Triggers**: `APPEARANCE_CEA` (before insert or update or delete), `APPEARANCE_DEL` (after delete), `APPEARANCE_INS` (before insert), `APPEARANCE_UPD` (before update), `TRG_WS_KFN_KK_RL_Q` (after insert or update or delete)

## DEFINITIONS.APPLICATION_ID_R

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICATION_ID | VARCHAR2(5) | N | 6i, 10g, 11g |


## DEFINITIONS.APPLICATION_MESSAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| MESSAGE_ID | NUMBER(4) | N |  |
| MESSAGE | VARCHAR2(256) | Y |  |

- **PK** `PK_APPLICATION_MESSAGES`: MESSAGE_ID
- **Triggers**: `APPLICATION_MESSAGES_CEA` (before insert or update or delete), `APPLICATION_MESSAGES_TS` (before insert or update or delete), `TRG_WS_RWE_LH_JQ_Q` (after insert or update or delete)

## DEFINITIONS.APPLICATION_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICATION_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| DEV_TOOL_ID | VARCHAR2(4) | N |  |
| APPLICATION_PREFIX | VARCHAR2(10) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| CHECK_AUTHENTICATION | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_APPLICATION_SETUP`: APPLICATION_ID
- **UK** `UK_APPLICATION_SETUP_1`: SHORT_DESC
- **UK** `UK_APPLICATION_SETUP_2`: APPLICATION_PREFIX
- **FK** `FK_APPLICATION_SETUP_1`: (DEV_TOOL_ID) -> DEFINITIONS.DEVELOPMENT_TOOLS(SERIAL_NO) [disabled]

## DEFINITIONS.APPLICATION_OBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| APPLICATION_ID | NUMBER(3) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_APPLICATION_OBJECTS`: APPLICATION_ID, OBJECT_CODE
- **FK** `FK_APPLICATION_OBJECTS_1`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **FK** `FK_APPLICATION_OBJECTS_2`: (APPLICATION_ID) -> DEFINITIONS.APPLICATION_SETUP(APPLICATION_ID)

## DEFINITIONS.APPLICATION_SERVERS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVER_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| DEV_TOOL_ID | VARCHAR2(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CHECK_AUTHENTICATION | CHAR(1) default 'N' | Y |  |
| EXTERNAL_IP_ADDRESS | VARCHAR2(15) | Y |  |
| EXTERNAL_URL | VARCHAR2(100) | Y |  |
| INTERNAL_IP_ADDRESS | VARCHAR2(15) | Y |  |
| INTERNAL_URL | VARCHAR2(100) | Y |  |
| AUTO_RIGHTS | CHAR(1) default 'N' | Y | ON AUTO USER CREATION GRANT DEFAULT LOCATION FOR LOGIN |
| VIEWER_PATH | VARCHAR2(150) | Y | PATH OF ASP WEBSITE TO VIEW ARCHIVED CHARTS FROM LAN |
| VIEWER_PATH_LIVE | VARCHAR2(150) | Y | PATH OF ASP WEBSITE TO VIEW ARCHIVED CHARTS FROM WAN |
| IS_SECURE_SEVER | CHAR(1) default 'N' | Y | TO CHECK WHETHER SERVER IS SECURE OR NOT |
| OS_PLATFORM | VARCHAR2(15) | Y | This column contains OS Platform e.g WINDOWS,LINUX,UNIX |
| ICON | BLOB | Y |  |
| PATH | VARCHAR2(500) | Y | This column contain directory path of forms/reports etc of Linux Server |

- **PK** `PK_APPLICATION_SERVERS`: SERVER_ID
- **UK** `UK_APPLICATION_SERVERS_1`: SHORT_DESC
- **FK** `FK_APPLICATION_SERVERS_1`: (DEV_TOOL_ID) -> DEFINITIONS.DEVELOPMENT_TOOLS(SERIAL_NO) [disabled]
- **Triggers**: `APPLICATION_SERVERS_CEA` (before insert or update or delete), `APPLICATION_SERVERS_DEL` (after delete), `APPLICATION_SERVERS_INS` (before insert), `APPLICATION_SERVERS_UPD` (before update), `TRG_WS_XKO_ZG_IL_Q` (after insert or update or delete)

## DEFINITIONS.APPLICATION_SERVERS_ICONS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVER_ID | NUMBER(3) | N |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| ICON | BLOB | Y |  |

- **PK** `PK_APPLICATION_SERVERS_ICONS`: SERVER_ID
- **Triggers**: `APPLICATION_SERVERS_ICONS_DEL` (after delete), `APPLICATION_SERVERS_ICONS_INS` (before insert), `APPLICATION_SERVERS_ICONS_UPD` (before update)

## DEFINITIONS.APPLICATION_SETTINGS

| Column | Type | Null | Comment |
|---|---|---|---|
| NAME | VARCHAR2(200) | Y |  |
| VALUE | VARCHAR2(60) | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| SR_NO | NUMBER(12) | N |  |

- **PK** `PK_APPLICATION_SETTINGS`: SR_NO

## DEFINITIONS.APPOINTMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| APPOINTMENT_TYPE_ID | VARCHAR2(6) | N | Location ID + Counter |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| SEND_SMS | CHAR(1) | Y |  |
| APPOINTMENT_TIME_REQUIRED | CHAR(1) default 'Y' | Y |  |
| PHYSICIAN_NOTE_ENTRY_REQ | CHAR(1) default 'N' | Y |  |
| PHYSICIAN_NOTE_TYPE | CHAR(1) default 'O' | Y |  |
| DEFAULT_PHYSICIAN_NOTE | VARCHAR2(4000) | Y |  |
| REMARKS_REQUIRED | CHAR(1) default 'N' | Y |  |
| ADMISSION_REQUEST_MAPPING_REQ | CHAR(1) default 'N' | Y |  |

- **PK** `PK_APPOINTMENT_TYPE`: APPOINTMENT_TYPE_ID
- **Triggers**: `APPOINTMENT_TYPE_CEA` (before insert or update or delete), `APPOINTMENT_TYPE_DEL` (after delete), `APPOINTMENT_TYPE_INS` (before insert), `APPOINTMENT_TYPE_UPD` (before update), `TRG_WS_MWO_YO_FI_Q` (after insert or update or delete)

## DEFINITIONS.APPOINTMENT_MESSAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| MESSAGE_ID | NUMBER(6) | N |  |
| APPOINTMENT_TYPE_ID | VARCHAR2(6) | N |  |
| MESSAGE_TEXT | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| SMS_ALERT_ID | NUMBER(2) | Y |  |
| SMS_TYPE | CHAR(1) default 'E' | Y | E => English, U =>Urdu, B => Both Languages |

- **PK** `PK_APPOINTMENT_MESSAGE`: MESSAGE_ID
- **FK** `FK_APPOINTMENT_MESSAGE_1`: (APPOINTMENT_TYPE_ID) -> DEFINITIONS.APPOINTMENT_TYPE(APPOINTMENT_TYPE_ID) [disabled]
- **Triggers**: `APPOINTMENT_MESSAGE_DEL` (after delete), `APPOINTMENT_MESSAGE_INS` (before insert), `APPOINTMENT_MESSAGE_UPD` (before update)

## DEFINITIONS.APPROVAL_QUEUE_ROLE_WISE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_TYPE_ID | NUMBER(4) | N |  |
| ROLE_ID | NUMBER(4) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_APPROVAL_QUEUE_ROLE_WISE`: QUEUE_TYPE_ID, ROLE_ID, LOCATION_ID
- **Triggers**: `APPROVAL_QUEUE_ROLE_WISE_CEA` (before insert or update or delete), `TRG_WS_ZYC_LS_AI_Q` (after insert or update or delete)

## DEFINITIONS.APPROVAL_QUEUE_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_TYPE_ID | NUMBER(4) | N |  |
| QUEUE_TYPE_DESC | VARCHAR2(255) | Y |  |
| EVENT | VARCHAR2(255) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_APPROVAL_QUEUE_TYPES`: QUEUE_TYPE_ID
- **Triggers**: `APPROVAL_QUEUE_TYPES_CEA` (before insert or update or delete), `TRG_WS_VBI_SR_JQ_Q` (after insert or update or delete)

## DEFINITIONS.APP_CANCEL_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| CANCEL_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| APPT_CANCEL_POLICY_ALWD | CHAR(1) | Y | This column will check the reson for cancel policy |
| SHOW_IN_CANCEL_CLINIC | CHAR(1) | Y |  |
| SHOW_IN_APPOINTMENTS | CHAR(1) | Y |  |
| NO_SHOW_TELEMDICINE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_APP_CANCEL_REASON`: CANCEL_ID
- **Triggers**: `APP_CANCEL_REASON_CEA` (before insert or update or delete), `APP_CANCEL_REASON_DEL` (after delete), `APP_CANCEL_REASON_INS` (before insert), `APP_CANCEL_REASON_UPD` (before update), `TRG_WS_OTZ_XY_HR_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_ARMS

| Column | Type | Null | Comment |
|---|---|---|---|
| ARM_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ARMY_SERVICE_ID | NUMBER | Y |  |

- **PK** `PK_ARMY_ARMS`: ARM_ID
- **Triggers**: `ARMY_ARMS_CEA` (before insert or update or delete), `ARMY_ARMS_DEL` (after delete), `ARMY_ARMS_INS` (before insert), `ARMY_ARMS_UPD` (before update), `TRG_WS_NVA_AL_IQ_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(10) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| LONG_DESCRIPTION | VARCHAR2(4000) | Y |  |

- **PK** `PK_ARMY_CATEGORY`: CATEGORY_ID
- **Triggers**: `ARMY_CATEGORY_CEA` (before insert or update or delete), `ARMY_CATEGORY_DEL` (after delete), `ARMY_CATEGORY_INS` (before insert), `ARMY_CATEGORY_UPD` (before update), `TRG_WS_RES_BM_YR_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_FORMATION

| Column | Type | Null | Comment |
|---|---|---|---|
| FORMATION_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(50) | Y |  |
| FORMATION_ORDER | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_ARMY_FORMATION`: FORMATION_ID
- **Triggers**: `ARMY_FORMATION_DEL` (after delete), `ARMY_FORMATION_INS` (before insert), `ARMY_FORMATION_UPD` (before update)

## DEFINITIONS.ARMY_RANKS
This table contains definitions of Armay ranks (System Constant Level table)

| Column | Type | Null | Comment |
|---|---|---|---|
| RANK_ID | VARCHAR2(6) | N | This column contains Unique Rank ID (Primary Key) |
| NAME | VARCHAR2(50) | N | This column contains Descrition/Name/Ttitle of army ranks |
| RANK_ABBREVIATION | VARCHAR2(20) | N | This column contains Abbriviation/Title for Full Name of rank |
| ACTIVE | CHAR(1) default 'Y' | Y | This column contains flag of Active, Inactive state (Y=Active, N=Inactive) |
| ORDER_NO | NUMBER(4) | Y |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| RANK_TYPE | VARCHAR2(10) | Y |  |
| RANK_CAT_ID | VARCHAR2(6) | Y |  |
| FORCE_TYPE_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_ARMY_RANKS`: RANK_ID
- **CHECK** `CK_ARMY_RANKS_1`: ACTIVE IN ('Y','N'
- **Triggers**: `ARMY_RANKS_CEA` (before insert or update or delete), `ARMY_RANKS_DEL` (after delete), `ARMY_RANKS_INS` (before insert), `ARMY_RANKS_UPD` (before update), `TRG_WS_SKX_BI_WR_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_RANKS_NAVY

| Column | Type | Null | Comment |
|---|---|---|---|
| RANK_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(50) | N |  |
| RANK_ABBREVIATION | VARCHAR2(20) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_NO | NUMBER(4) | Y |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| RANK_TYPE | VARCHAR2(10) | Y |  |
| RANK_CAT_ID | VARCHAR2(6) | Y |  |
| FORCE_TYPE_ID | VARCHAR2(6) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |

- **PK** `PK_AR_NAVY`: ZONE_ID, RANK_ID

## DEFINITIONS.ARMY_RANKS_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| RANK_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(50) | N |  |
| RANK_ABBREVIATION | VARCHAR2(20) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_NO | NUMBER(4) | Y |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| RANK_TYPE | VARCHAR2(10) | Y |  |
| RANK_CAT_ID | VARCHAR2(6) | Y |  |
| FORCE_TYPE_ID | VARCHAR2(6) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_RANK_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_ARMY_RANKS_ZONE`: ZONE_ID, RANK_ID

## DEFINITIONS.ARMY_SERVICE

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| NAME | VARCHAR2(20) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | N |  |

- **PK** `PK_ARMY_SERVICE`: ID
- **Triggers**: `ARMY_SERVICE_CEA` (before insert or update or delete), `ARMY_SERVICE_DEL` (after delete), `ARMY_SERVICE_INS` (before insert), `ARMY_SERVICE_UPD` (before update), `TRG_WS_EXZ_GE_MH_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_SERVICE_PREFIX

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| NAME | VARCHAR2(20) | Y |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| SERVICE_ID | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_NO | NUMBER(4) | Y |  |

- **PK** `PK_ARMY_SERVICE_PREFIX`: ID
- **FK** `FK_ARMY_SERVICE_PREFIX_1`: (SERVICE_ID) -> DEFINITIONS.ARMY_SERVICE(ID) [disabled]
- **Triggers**: `ARMY_SERVICE_PREFIX_CEA` (before insert or update or delete), `ARMY_SERVICE_PREFIX_DEL` (after delete), `ARMY_SERVICE_PREFIX_INS` (before insert), `ARMY_SERVICE_PREFIX_UPD` (before update), `TRG_WS_SRK_CV_WN_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_SERVICE_RANKS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| SERVICE_ID | NUMBER | Y |  |
| RANK_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_ARMY_SERVICE_RANKS`: ID
- **FK** `FK_ARMY_SERVICE_RANKS_1`: (SERVICE_ID) -> DEFINITIONS.ARMY_SERVICE(ID) [disabled]
- **FK** `FK_ARMY_SERVICE_RANKS_2`: (RANK_ID) -> DEFINITIONS.ARMY_RANKS(RANK_ID) [disabled]
- **Triggers**: `ARMY_SERVICE_RANKS_CEA` (before insert or update or delete), `ARMY_SERVICE_RANKS_DEL` (after delete), `ARMY_SERVICE_RANKS_INS` (before insert), `ARMY_SERVICE_RANKS_UPD` (before update), `TRG_WS_WOS_ME_AZ_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_SERVICE_RANKS_NAVY

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| SERVICE_ID | NUMBER | Y |  |
| RANK_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |


## DEFINITIONS.ARMY_SERVICE_RANKS_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| SERVICE_ID | NUMBER | Y |  |
| RANK_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_ID | NUMBER(22) | Y |  |
| NAME | VARCHAR2(20) | Y |  |
| NEW_SERVICE_ID | NUMBER | Y |  |
| NEW_RANK_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_ARMY_SERVICE_RANKS_ZONE`: ZONE_ID, ID

## DEFINITIONS.ARMY_SERVICE_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| NAME | VARCHAR2(20) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | N |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_ID | NUMBER(22) | Y |  |

- **PK** `PK_ARMY_SERVICE_ZONE`: ZONE_ID, ID

## DEFINITIONS.ARMY_UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| UNIT_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_ARMY_UNIT`: UNIT_ID
- **Triggers**: `ARMY_UNIT_CEA` (before insert or update or delete), `ARMY_UNIT_DEL` (after delete), `ARMY_UNIT_INS` (before insert), `ARMY_UNIT_UPD` (before update), `TRG_WS_XZR_CV_XB_Q` (after insert or update or delete)

## DEFINITIONS.ARMY_UNIT_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| UNIT_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_UNIT_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_ARMY_UNIT_ZONE`: ZONE_ID, UNIT_ID

## DEFINITIONS.ASSET

| Column | Type | Null | Comment |
|---|---|---|---|
| ASSET_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_ASSET`: ASSET_ID
- **Triggers**: `ASSET_CEA` (before insert or update or delete), `ASSET_DEL` (after delete), `ASSET_INS` (before insert), `ASSET_UPD` (before update), `TRG_WS_HKW_DO_AT_Q` (after insert or update or delete)

## DEFINITIONS.ATTACHMENT_DOCUMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_TYPE_ID | NUMBER | N | this columns conatins document type id , numeric |
| DESCRIPTION | VARCHAR2(500) | Y | this columns conatins document description |
| ACTIVE | CHAR(1) | Y | this columns conatins active y or n |
| DEPARTMENT_ID | VARCHAR2(10) | Y |  |
| SECTION_ID | VARCHAR2(10) | Y |  |

- **PK** `PK_ATTCHMENT_DOC_TYPE`: DOC_TYPE_ID
- **UK** `UK_ATTCHMENT_DOC_TYPE`: DESCRIPTION, DEPARTMENT_ID, SECTION_ID
- **Triggers**: `ATTACHMENT_DOCUMENT_TYPE_CEA` (before insert or update or delete), `ATTACHMENT_DOCUMENT_TYPE_DEL` (after delete), `ATTACHMENT_DOCUMENT_TYPE_INS` (before insert), `ATTACHMENT_DOCUMENT_TYPE_UPD` (before update), `TRG_WS_NMF_AF_MR_Q` (after insert or update or delete)

## DEFINITIONS.ATTACHMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_ATTACHMENT_TYPE`: TYPE_ID
- **Triggers**: `ATTACHMENT_TYPE_CEA` (before insert or update or delete), `ATTACHMENT_TYPE_DEL` (after delete), `ATTACHMENT_TYPE_INS` (before insert), `ATTACHMENT_TYPE_UPD` (before update), `TRG_WS_XGS_TZ_XU_Q` (after insert or update or delete)

## DEFINITIONS.ATTACHMENT_SUBTYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SUBTYPE_ID | VARCHAR2(7) | N |  |
| TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_ATTACHMENT_SUBTYPE`: SUBTYPE_ID, TYPE_ID
- **FK** `FK_ATTACHMENT_SUBTYPE_1`: (TYPE_ID) -> DEFINITIONS.ATTACHMENT_TYPE(TYPE_ID) [disabled]
- **Triggers**: `ATTACHMENT_SUBTYPE_CEA` (before insert or update or delete), `ATTACHMENT_SUBTYPE_DEL` (after delete), `ATTACHMENT_SUBTYPE_INS` (before insert), `ATTACHMENT_SUBTYPE_UPD` (before update), `TRG_WS_SLS_VU_JO_Q` (after insert or update or delete)

## DEFINITIONS.REGION

| Column | Type | Null | Comment |
|---|---|---|---|
| REGION_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESC | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| REGION_TYPE_ID | VARCHAR2(3) default '001' | N | 001 Means its a marketing region. and 002 for HSM regions |

- **PK** `PK_REGION`: REGION_ID
- **CHECK** `CK_REGION_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `REGION_CEA` (before insert or update or delete), `TRG_WS_ROX_FJ_AO_Q` (after insert or update or delete)

## DEFINITIONS.COUNTRY

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(100) | Y |  |
| NATIONALITY | VARCHAR2(30) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| REGION_ID | VARCHAR2(4) | Y |  |
| OFFICE_ID | NUMBER(3) | Y |  |
| CALLING_CODE | VARCHAR2(5) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ISO_CC_2_DIGIT | CHAR(2) | Y | 2 digit country code as per ISO standard |
| WEB_VIEW | CHAR(1) default 'N' | N |  |
| FINAL_DESTINATION | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_COUNTRY`: COUNTRY_ID
- **FK** `FK_COUNTRY_1`: (REGION_ID) -> DEFINITIONS.REGION(REGION_ID) [disabled]
- **Triggers**: `COUNTRY_CEA` (before insert or update or delete), `COUNTRY_DEL` (after delete), `COUNTRY_INS` (before insert), `COUNTRY_TS` (before insert or update or delete), `COUNTRY_UPD` (before update), `TRG_WS_DDD_ZJ_CC_Q` (after insert or update or delete)

## DEFINITIONS.STATE

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |

- **PK** `PK_STATE`: COUNTRY_ID, STATE_ID
- **FK** `FK_S01_T032_S01_T008_1`: (COUNTRY_ID) -> DEFINITIONS.COUNTRY(COUNTRY_ID)
- **Triggers**: `STATE_CEA` (before insert or update or delete), `STATE_DEL` (after delete), `STATE_INS` (before insert), `STATE_TS` (before insert or update or delete), `STATE_UPD` (before update), `TRG_WS_CNI_RB_EL_Q` (after insert or update or delete)

## DEFINITIONS.DISTRICT

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| OFFICE_ID | NUMBER(3) | Y |  |

- **PK** `PK_DISTRICT`: COUNTRY_ID, STATE_ID, DISTRICT_ID
- **FK** `FK_S01_T016_S01_T032_1`: (COUNTRY_ID, STATE_ID) -> DEFINITIONS.STATE(COUNTRY_ID, STATE_ID)
- **Triggers**: `DISTRICT_CEA` (before insert or update or delete), `DISTRICT_DEL` (after delete), `DISTRICT_INS` (before insert), `DISTRICT_TS` (before insert or update or delete), `DISTRICT_UPD` (before update), `TRG_WS_MME_IA_YG_Q` (after insert or update or delete)

## DEFINITIONS.TEHSIL

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| CBR_CITY_CODE | NUMBER(11) | Y |  |
| CALLING_CODE | NUMBER(6) | Y |  |
| SUB_AREA_REQUIRED | CHAR(1) default 'N' | Y | This column will use for patient registration if tehsil wise flag yes , sub area will be mondatory on registration |
| MKT_SUB_AREA_REQUIRED | CHAR(1) default 'N' | Y |  |

- **PK** `PK_TEHSIL`: COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID
- **FK** `FK_S01_T034_S01_T016_1`: (COUNTRY_ID, STATE_ID, DISTRICT_ID) -> DEFINITIONS.DISTRICT(COUNTRY_ID, STATE_ID, DISTRICT_ID)
- **FK** `FK_TEHSIL_2`: (CBR_CITY_CODE) -> CBR.CITIES(CITY_CODE) [disabled]
- **Triggers**: `TEHSIL_CEA` (before insert or update or delete), `TEHSIL_DEL` (after delete), `TEHSIL_INS` (before insert), `TEHSIL_TS` (before insert or update or delete), `TEHSIL_UPD` (before update), `TRG_WS_KMB_QH_JA_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(150) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ADDRESS | VARCHAR2(2000) | Y |  |
| NTN | VARCHAR2(13) | Y |  |
| SALES_TAX_REG_NO | VARCHAR2(17) | Y |  |
| SHORT_DESC | VARCHAR2(15) | Y |  |
| TIME_GAP | NUMBER(5) default 0 | N |  |
| CLIENT_ID | VARCHAR2(10) | Y |  |
| PHONE | VARCHAR2(40) | Y |  |
| FAX | VARCHAR2(40) | Y |  |
| COUNTER | NUMBER(38) | Y |  |
| HRD_DESCRIPTION | VARCHAR2(200) | Y |  |
| EMAIL | VARCHAR2(100) | Y |  |
| REPORT_RESULT_ONLINE | CHAR(1) default 'N' | N |  |
| REPORT_RESULT_EMAIL | CHAR(1) default 'N' | N |  |
| VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| CC_TYPE | CHAR(1) | N | 'N-Not a Collection Centre','F-Franchised Collection Centre','S-Shaukat Khanum Collection Centre','P-Collection Point' ,'D-Third Party Diagnostic Service','K-Kiosks Centre' |
| WEBSITE | VARCHAR2(60) | Y |  |
| LOGO | BLOB | Y |  |
| REPORT_HEADER | VARCHAR2(200) | Y |  |
| LAB_LOCATION | CHAR(1) default 'N' | Y |  |
| CONTINGENCY_FLAG | CHAR(1) default 'N' | Y |  |
| TIMER_CHECKING | CHAR(1) default 'N' | N |  |
| ORIGINAL_EMAIL | VARCHAR2(100) | Y |  |
| INVOICE_ADDRESS | VARCHAR2(2000) | Y |  |
| YEAR | CHAR(2) | Y |  |
| PATHOLOGY_SECTION_CHARACTER | VARCHAR2(2) | Y |  |
| INVOICE_REPORT_HEADER | VARCHAR2(200) | Y |  |
| WALKIN_CLINIC | CHAR(1) default 'N' | N |  |
| INVOICE_VOUCHER | CHAR(1) default 'Y' | N |  |
| COPY_RIGHT | VARCHAR2(255) | Y |  |
| NAME | VARCHAR2(100) | Y | Hospital short display name |
| AVAILABLE_LOCATIONS | CHAR(1) default 'N' | Y |  |
| LIFE_THREATENING_EMERGENCY | CHAR(1) default 'N' | Y |  |
| LTE_HOURS | NUMBER(5) | Y |  |
| OPD_SCREEN_TIME | NUMBER(10) default 5000 | Y |  |
| TERMINAL_WISE_BATCH | CHAR(1) | N |  |
| LOCATION_STATUS | CHAR(1) default 'Y' | Y |  |
| FETCH_PCR_DATA | CHAR(1) default 'N' | Y |  |
| REPORT_VALIDATION_DURATION | NUMBER(3) default 7 | Y | This column contains the number of days for which a report will be available for online PDF downloading system |
| ON_LINE | CHAR(1) default 'N' | N | Value Y means collection centre is online usning WCCIS applicaiton, and N means it is offline |
| CONTINGENCY_REMARKS | VARCHAR2(500) | Y |  |
| PARTY_ID | VARCHAR2(14) | Y |  |
| APPLICATION_LOGGING_ON | CHAR(1) default 'U' | Y |  |
| POSITION | NUMBER(2) | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| STATE_ID | NUMBER(4) | Y |  |
| DISTRICT_ID | NUMBER(4) | Y |  |
| SEND_ALERTS | CHAR(1) default 'N' | N | This Column contains Y/N Flag for order/test cancellation alerts |
| SEND_ALERTS_EMAIL | VARCHAR2(200) | Y | This column contains email address for order/test cancellation alerts |
| BATCH_RECEIVE_LOCATION_ID | VARCHAR2(3) default '001' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y | This column contains Organization ID for Multi-location info. |
| PARENT_LOCATION_ID | VARCHAR2(3) | Y |  |
| REPORTS_ENVID | VARCHAR2(20) | Y |  |
| MANUAL_DISCOUNT | CHAR(1) default 'N' | N | This Column is added after discussion with Mr. Idrees, Columns values must be Y or N, If Values is Y  then Manual discount at this Location is allowed else not allowed, If Values is Y then user can enter discount percentage or discount  amount |
| SHOW_PENDING_TASKS | CHAR(1) default 'Y' | Y |  |
| PSSC_LOCATIONS | CHAR(1) default 'N' | Y | Locations included in Punjab Social Security Contributions. |
| PAYROLL_LOCATION | CHAR(1) | Y | If  Payroll Reports Generate then Y else N |
| PATIENT_CNIC_MANDATORY | CHAR(1) default 'N' | Y | Values will be Y or N, Y means CNIC is mandatory at the time of Patient Registeration and N means CNIC is not mandatory |
| MARK_ATTENDANCE | CHAR(1) default 'N' | Y |  |
| XE_LOCATION_ID | VARCHAR2(3) | Y | This column contains Buffer/XE Location ID for Machine Interfacing. |
| MOBILE_NO | VARCHAR2(20) | Y | This column contains info abour Mobile Number |
| SETUP_LOCATION_ID | VARCHAR2(3) | Y | Which Location ID you want to use. |
| WHITE_LABEL | CHAR(1) default 'N' | Y | This column specify print white label scheme (Y= Blank Header footer, N = Print Header Footer) |
| CITY_ID | NUMBER(4) | Y | Added this column to show city of cc on cc employee card |
| LOCATION_CODE | VARCHAR2(10) | Y | Data will be as CC01, CC200, CK25 etc. |
| SEND_EMAIL | CHAR(1) default 'N' | Y | This column contains flag to use email solution |
| CPT_COUNTER_ORDERENTRY_ALLOWED | VARCHAR2(1) default 'N' | Y | If value is Y then CPT orderentry, insertion and updation is allowed, If value is N then only invoicing is allowed |
| GATE_PASS_ALLOW | CHAR(1) default 'N' | Y |  |
| NON_LTE_HOURS | NUMBER(5) | Y |  |
| ALLOW_HOME_SAMPLING | VARCHAR2(1) default 'N' | Y |  |
| RESTRICT_CALL_LEAD | VARCHAR2(1) default 'N' | Y |  |
| IS_CARD_PRINTING | CHAR(1) | Y |  |
| HF_LOCATION_ID | VARCHAR2(3) | Y | This column contains location id for report header footer |
| ACTIVE_DIRECTORY_LOCATION | VARCHAR2(20) | Y | This column contains active directory location |
| LOCATION_NAME_IN_SMS | VARCHAR2(50) | Y | This column will be use for get the name of location for SMS |
| SECTION_NUMBERING_ALLOW | CHAR(1) | Y | This Column contains Y/N flag If  this flage is Y then section_numbering perform other wise No |

- **PK** `PK_LOCATION`: LOCATION_ID
- **UK** `UK_LOCATION_02`: HRD_DESCRIPTION
- **UK** `UK_LOCATION_03`: LOCATION_CODE
- **FK** `FK_CITY`: (COUNTRY_ID, STATE_ID, DISTRICT_ID, CITY_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]
- **FK** `FK_LOCATION_2`: (PARTY_ID) -> PARTY.PARTY(PARTY_ID) [disabled]
- **FK** `FK_LOCATION_3`: (BATCH_RECEIVE_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **CHECK** `CK_LOCATION_01`: LAB_LOCATION IN ('Y','N'
- **CHECK** `CK_LOCATION_02`: CONTINGENCY_FLAG IN ('Y','N'
- **CHECK** `CK_LOCATION_03`: TIMER_CHECKING IN('Y','N'
- **CHECK** `CK_LOCATION_04`: SEND_ALERTS IN ('Y','N'
- **CHECK** `CK_LOCATION_05`: TERMINAL_WISE_BATCH IN ('Y','N'
- **CHECK** `CK_LOCATION_06`: ON_LINE IN ('Y','N'
- **CHECK** `CK_LOCATION_07`: INVOICE_VOUCHER IN ('Y','N'
- **CHECK** `CK_LOCATION_08`: CC_TYPE IN('N','F','S','K','D','P'
- **CHECK** `CK_LOCATION_09`: ACTIVE IN ('N','Y'
- **CHECK** `CK_LOCATION_10`: APPLICATION_LOGGING_ON IN ('Y','N','U'
- **CHECK** `CK_LOCATION_11`: LIFE_THREATENING_EMERGENCY IN ('N','Y'
- **CHECK** `CK_LOCATION_12`: LOCATION_ID <> BATCH_RECEIVE_LOCATION_ID
- **CHECK** `CK_LOCATION_13`: SUBSTR(LOCATION_CODE,1,1) IN ('0','1','2','3','4','5','6','7','8','9'
- **Triggers**: `BEFORE_LOCATION_INS_UPD_DEL` (before insert or delete or update), `CONTINGENCY_FLAG_HIST` (before insert or update of contingency_flag), `LOCATION_AFTER_INS` (after insert), `LOCATION_CEA` (before insert or update or delete), `LOCATION_DEL` (after delete), `LOCATION_INS` (before insert), `LOCATION_TS` (before insert or update or delete), `LOCATION_UPD` (before update), `TRG_WS_UMF_MV_UF_Q` (after insert or update or delete)

## DEFINITIONS.DIVISIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIVISION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| DIVISION_HEAD | VARCHAR2(14) | Y |  |

- **PK** `PK_DIVISIONS`: DIVISION_ID
- **Triggers**: `DIVISIONS_CEA` (before insert or update or delete), `DIVISIONS_DEL` (after delete), `DIVISIONS_INS` (before insert), `DIVISIONS_UPD` (before update), `TRG_WS_ZXM_TK_CE_Q` (after insert or update or delete)

## DEFINITIONS.COST_PROFIT_CENTER

| Column | Type | Null | Comment |
|---|---|---|---|
| DIVISION_ID | VARCHAR2(3) | N |  |
| COST_CENTER_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |

- **PK** `PK_COST_PROFIT_CENTER`: DIVISION_ID, COST_CENTER_ID
- **UK** `UK_COST_PROFIT_CENTER_001`: COST_CENTER_ID
- **FK** `FK_CC_DIVISIONS`: (DIVISION_ID) -> DEFINITIONS.DIVISIONS(DIVISION_ID)
- **Triggers**: `COST_PROFIT_CENTER_CEA` (before insert or update or delete), `COST_PROFIT_CENTER_DEL` (after delete), `COST_PROFIT_CENTER_INS` (before insert), `COST_PROFIT_CENTER_UPD` (before update), `TRG_WS_RCK_SY_LE_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| COST_CENTER_ID | VARCHAR2(3) | Y |  |
| CAPACITY | NUMBER(6) default 0 | N |  |
| DEFAULTS | VARCHAR2(1) default 'N' | Y |  |
| CHART_ISSUE_LOCATION | CHAR(1) default 'N' | Y |  |
| CHART_MASTER_LOCATION | CHAR(1) default 'N' | N |  |
| INPATIENT_UNIT | CHAR(1) default 'N' | N |  |
| INTERNAL_EMAIL | VARCHAR2(60) | Y |  |
| RECEIPT_AUTHORISE | CHAR(1) default 'N' | Y |  |
| PHYSICIAN_NOTES_ENTRY | CHAR(1) | Y |  |
| DEFAULT_CPT_ID | VARCHAR2(18) | Y | Default consultancy cpt_id as per order location of computer. |
| NOTES_LOCATION_ID | VARCHAR2(3) | Y |  |
| DEFAULT_ORDER_LOCATION | CHAR(1) default 'N' | N | Default order location attached with specified location id |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| EMERGENCY_LOCATION | CHAR(1) default 'N' | N | This Column is added on Request of Mr. Idrees Khokhar (Director MIS and Medical Record), In invoice procedure we shall remove the hard coding of the order location id we shall check the emergency location with the help of this flag |
| CASH_ENTRY_B4_POPULATE_SUMMARY | CHAR(1) default 'N' | Y | This column is related to Billing Cash Summary Close , If Value is 'Y' then Cashier has to enter the Cash Amount before Pressing the 'Populate Cash Summary' button otherwise Cashier can populate the Cash Summary without entry of Phyiscal Cash |
| ORDER_MASTER_LOCATION | VARCHAR2(3) | Y | Consider sublocation of this Master Location |
| NATURE_ID | VARCHAR2(3) | Y | This field will use for sorting CPT LOV on ordering forms against Terminal |
| PATIENT_CNIC_MANDATORY | CHAR(1) default 'N' | Y | Values will be Y or N, Y means CNIC is mandatory at the time of Patient Registeration and N means CNIC is not mandatory |
| IBP_LOCATION | CHAR(1) default 'N' | N | This column will be used to identify that Order Location will be used for IBP or not, Values will be Y for IBP and N for Non IBP |
| STOCK_LOCATION_ID | VARCHAR2(3) | Y |  |
| STAT | VARCHAR2(1) default 'N' | Y | This column will cotain flag that ordered CPT from this Ordering Location is by default Mark as STAT |
| BED_SELECTION | VARCHAR2(1) | Y | This column will be used to handle bed selection in EAR. A means bed will be auto selected, M means manual selection |
| ORDER_LOCATION_DISPLAY_DESC | VARCHAR2(150) | Y | This column will be used to add the display name of the order location, IPD team hardcoded the EAR in code but on dashboard, name should be displayed differently |
| AUTO_CONSULT | VARCHAR2(1) default 'N' | Y | Y mean auto consult will be sent to specialty through job |
| LOCATION_TYPE | VARCHAR2(3) | Y | I for ICU, OR for OR etc. |
| APPROPRIATENESS_REV_GUIDELINE | VARCHAR2(1000) | Y | This column will be used to save the link for Emergency Stock Medicine templates according to the patient location |
| AUTO_DISCHARGE | VARCHAR2(1) default 'N' | Y | Y means auto discharge for this location will be enable N means auto discharge for this order location is disable |
| COVID | VARCHAR2(1) default 'N' | Y | Y -> COVID order location, N ->Non COVID order location |
| MR_LOCATION_ID | VARCHAR2(3) | Y | Default medical record room location Id as linked with the specified order location |
| MR_ORDER_LOCATION_ID | VARCHAR2(3) | Y | Default medical record room order location Id as linked with the specified order location |
| CHART_DAYS | NUMBER(5) default 25 | Y |  |
| CHART_LOCATION_ID | VARCHAR2(3) | Y |  |
| SNP_LOCATION | CHAR(1) default 'N' | Y | This column will be used to identify that Section Numbering Perform Location or not, Values will be Y for SNP and N for Non SNP |
| RESTRICT_NURSE_ADMIN | VARCHAR2(1) default 'N' | Y | Will Be Use To Restrict Nurse Administration if Pharmacist Verification is pending. Allwed Values:  Y -> Check Pharmacist Verication Before Drug administration. N -> Do Not Check Pharmacist Verication Before Drug administration. |
| AGE_GROUP | VARCHAR2(1) | Y | A => ADULTS, P => PAEDS, B =>BOTH |
| MEDICINE_RECEIVING_FLOOR | VARCHAR2(1) default 'N' | Y |  |
| ADMISSION_HOLDING_BAY | VARCHAR2(1) default 'N' | Y | This column will contain flag admission holding bay order location |
| CHEMO_LOCATION_ID | VARCHAR2(3) | Y | Chemobay Location is defined |
| CHEMO_ORDER_LOCATION_ID | VARCHAR2(3) | Y | Chemobay Order Location is defined which is allowed for resident verification and token acknowledgement |
| OPAT_FLOOR | VARCHAR2(1) default 'N' | Y |  |
| WASTE_COLLECTION | VARCHAR2(1) | Y |  |
| AHB_TRANSFER_ALLOWED | VARCHAR2(1) default 'N' | Y | This column will contains admission holding bay transfer allowed or not |

- **PK** `PK_ORDER_LOCATION`: LOCATION_ID, ORDER_LOCATION_ID
- **UK** `UK_ORDER_LOCATION`: SHORT_DESC
- **FK** `FK_ORDER_LOCATION_2`: (COST_CENTER_ID) -> DEFINITIONS.COST_PROFIT_CENTER(COST_CENTER_ID)
- **FK** `FK_S01_T067_S01_T064_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **CHECK** `CHK_ORDER_LOCATION_04`: DEFAULT_ORDER_LOCATION IN ('N','Y'
- **CHECK** `CK_ORDER_LOCATION_001`: CHART_ISSUE_LOCATION IN ('N','Y'
- **CHECK** `CK_ORDER_LOCATION_002`: CHART_MASTER_LOCATION IN ('N','Y'
- **CHECK** `CK_ORDER_LOCATION_3`: INPATIENT_UNIT IN ('N','Y'
- **CHECK** `CK_ORDER_LOCATION_5`: CASH_ENTRY_B4_POPULATE_SUMMARY IN ('N','Y'
- **CHECK** `CK_ORDER_LOCATION_6`: EMERGENCY_LOCATION IN ('N','Y'
- **Triggers**: `ORDER_LOCATION_CEA` (before insert or update or delete), `ORDER_LOCATION_DEL` (after delete), `ORDER_LOCATION_INS` (before insert), `ORDER_LOCATION_TS` (before insert or update or delete), `ORDER_LOCATION_UPD` (before update), `TRG_WS_SAG_LH_LT_Q` (after insert or update or delete), `UPD_COVID_ORDER_LOCATION` (before update)

## DEFINITIONS.AUTO_SIGN_ORD_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| SIGN_OPTION | CHAR(1) | Y | N->NEVER, A->ALWAYS, T->TIME BASE |
| TIME_IN_HRS | NUMBER(6,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AUTO_SIGN_ORD_LOCATION`: LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_AUTO_SIGN_ORD_LOCATION_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **CHECK** `CK_AUTO_SIGN_ORD_LOCATION_1`: SIGN_OPTION IN ('N','A','T'
- **Triggers**: `AUTO_SIGN_ORD_LOCATION_DEL` (after delete), `AUTO_SIGN_ORD_LOCATION_INS` (before insert), `AUTO_SIGN_ORD_LOCATION_UPD` (before update)

## DEFINITIONS.AUTO_SIGN_TERMINAL

| Column | Type | Null | Comment |
|---|---|---|---|
| TERMINAL_NAME | VARCHAR2(30) | N |  |
| SIGN_OPTION | CHAR(1) | Y | N->NEVER, A->ALWAYS, T->TIME BASE |
| TIME_IN_HRS | NUMBER(6,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AUTO_SIGN_TERMINAL`: TERMINAL_NAME
- **CHECK** `CK_AUTO_SIGN_TERMINAL_1`: SIGN_OPTION IN ('N','A','T'
- **Triggers**: `AUTO_SIGN_TERMINAL_CEA` (before insert or update or delete), `AUTO_SIGN_TERMINAL_DEL` (after delete), `AUTO_SIGN_TERMINAL_INS` (before insert), `AUTO_SIGN_TERMINAL_UPD` (before update), `TRG_WS_RDH_DW_QX_Q` (after insert or update or delete)

## DEFINITIONS.AUTO_SIGN_USER

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_MRNO | VARCHAR2(14) | N |  |
| SIGN_OPTION | CHAR(1) | Y | 'N->NEVER, A->ALWAYS, T->TIME BASE' |
| TIME_IN_HRS | NUMBER(6,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_AUTO_SIGN_USER`: USER_MRNO
- **FK** `FK_AUTO_SIGN_USER_1`: (USER_MRNO) -> REGISTRATION.PATIENT(MRNO)
- **CHECK** `CK_AUTO_SIGN_USER`: SIGN_OPTION IN ('N','A','T'
- **Triggers**: `AUTO_SIGN_USER_DEL` (after delete), `AUTO_SIGN_USER_INS` (before insert), `AUTO_SIGN_USER_UPD` (before update)

## DEFINITIONS.BANK

| Column | Type | Null | Comment |
|---|---|---|---|
| BANK_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| FOREIGN_FLAG | CHAR(1) | Y | Incase of overseas Bank Foreign Flag will be True (Y/N) |
| IMD_IBFT_NO | NUMBER(12) | Y | This column contains the IBFT no that is generated against the bank |
| BIC_RTGS_CODE | VARCHAR2(30) | Y | This column contains the RTGC code that is generated against the bank |
| BIN_ID_DIGITS | NUMBER(2) default 6 | Y |  |
| DISPLAY_CODE | VARCHAR2(32) | Y |  |

- **PK** `PK_BANK`: BANK_ID
- **Triggers**: `BANK_CEA` (before insert or update or delete), `BANK_DEL` (after delete), `BANK_INS` (before insert), `BANK_TS` (before insert or update or delete), `BANK_UPD` (before update), `TRG_WS_NJN_RH_HH_Q` (after insert or update or delete)

## DEFINITIONS.BANK_ACCOUNT_BREAKUP

| Column | Type | Null | Comment |
|---|---|---|---|
| AC_BREAKUP_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `AC_BREAKUP_ID`: AC_BREAKUP_ID
- **Triggers**: `BANK_ACCOUNT_BREAKUP_DEL` (after delete), `BANK_ACCOUNT_BREAKUP_INS` (before insert), `BANK_ACCOUNT_BREAKUP_UPD` (before update)

## DEFINITIONS.BANK_ACCOUNT_BREAKUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| BANK_ID | VARCHAR2(6) | Y |  |
| AC_BREAKUP_ID | NUMBER(2) | Y |  |
| FROM_DIGIT | NUMBER(2) | Y |  |
| TO_DIGIT | NUMBER(2) | Y |  |


## DEFINITIONS.BANK_BRANCH

| Column | Type | Null | Comment |
|---|---|---|---|
| BRANCH_ID | VARCHAR2(3) | N |  |
| BANK_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ADDRESS | VARCHAR2(255) | Y |  |
| PHONE_NO | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | N |  |
| SWIFT_CODE | VARCHAR2(25) | Y | SWIFT_CODE FOR FOREIGN BANK |
| ACCOUNT_CODE | CHAR(25) | Y | FOR FOREIGN BANK |
| LC_BANK | CHAR(1) | Y | FLAG FOR LC OPENDING BANK FOR SKM |
| PARENT_BRANCH_ID | VARCHAR2(3) | Y |  |
| DISPLAY_CODE | VARCHAR2(32) | Y |  |

- **PK** `PK_BANK_BRANCH`: BRANCH_ID, BANK_ID
- **FK** `FK_BANK_BRANCH_1`: (BANK_ID) -> DEFINITIONS.BANK(BANK_ID) [disabled]
- **CHECK** `CK_BANK_BRANCH_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `BANK_BRANCH_CEA` (before insert or update or delete), `BANK_BRANCH_DEL` (after delete), `BANK_BRANCH_INS` (before insert), `BANK_BRANCH_TS` (before insert or update or delete), `BANK_BRANCH_UPD` (before update), `TRG_WS_CHR_PE_GA_Q` (after insert or update or delete)

## DEFINITIONS.BASIC_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | VARCHAR2(6) | N |  |
| PARAMETER_TYPE | VARCHAR2(1) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_BASIC_PARAMETERS`: PARAMETER_ID
- **Triggers**: `BASIC_PARAMETERS_CEA` (before insert or update or delete), `BASIC_PARAMETERS_DEL` (after delete), `BASIC_PARAMETERS_INS` (before insert), `BASIC_PARAMETERS_UPD` (before update), `TRG_WS_GYA_UH_JE_Q` (after insert or update or delete)

## DEFINITIONS.BASIC_UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| BASIC_UNIT_ID | VARCHAR2(5) | N |  |
| UNIT_DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ZONE_ID | VARCHAR2(30) | Y |  |

- **PK** `PK_BASIC_UNIT`: BASIC_UNIT_ID

## DEFINITIONS.BATCH_R

| Column | Type | Null | Comment |
|---|---|---|---|
| BATCH_NO | VARCHAR2(9) | Y |  |
| BATCH_DATE | DATE | Y |  |


## DEFINITIONS.BUILDING_BLOCK

| Column | Type | Null | Comment |
|---|---|---|---|
| BUILDING_BLOCK_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| BUILDING_LOCATION_ID | VARCHAR2(3) | Y |  |
| INPATIENT_BLOCK | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_BUILDING_BLOCK`: BUILDING_BLOCK_ID
- **FK** `FK_BUILDING_FLOOR_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `BUILDING_BLOCK_CEA` (before insert or update or delete), `BUILDING_BLOCK_DEL` (after delete), `BUILDING_BLOCK_INS` (before insert), `BUILDING_BLOCK_UPD` (before update), `TRG_WS_HNM_MB_PV_Q` (after insert or update or delete)

## DEFINITIONS.BUILDING_FLOOR

| Column | Type | Null | Comment |
|---|---|---|---|
| BUILDING_FLOOR_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| ORDER_BY | NUMBER(3) default 0 | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_BUILDING_FLOOR`: BUILDING_FLOOR_ID
- **UK** `UK_BUILDING_FLOOR_1`: DESCRIPTION
- **Triggers**: `BUILDING_FLOOR_CEA` (before insert or update or delete), `BUILDING_FLOOR_DEL` (after delete), `BUILDING_FLOOR_INS` (before insert), `BUILDING_FLOOR_UPD` (before update), `TRG_WS_XMN_ND_SX_Q` (after insert or update or delete)

## DEFINITIONS.BUILDING_BLOCK_FLOORS

| Column | Type | Null | Comment |
|---|---|---|---|
| BUILDING_BLOCK_FLOOR_ID | VARCHAR2(10) | N |  |
| BUILDING_BLOCK_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| BUILDING_FLOOR_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_BUILDING_BLOCK_FOOR`: BUILDING_BLOCK_FLOOR_ID
- **FK** `FK_BUILDING_FLOOR`: (BUILDING_BLOCK_ID) -> DEFINITIONS.BUILDING_BLOCK(BUILDING_BLOCK_ID) [disabled]
- **FK** `FK_BUILDING_FLOOR1`: (BUILDING_FLOOR_ID) -> DEFINITIONS.BUILDING_FLOOR(BUILDING_FLOOR_ID) [disabled]
- **FK** `FK_BUILDING_FLOOR2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **Triggers**: `BUILDING_BLOCK_FLOORS_CEA` (before insert or update or delete), `BUILDING_BLOCK_FLOORS_DEL` (after delete), `BUILDING_BLOCK_FLOORS_INS` (before insert), `BUILDING_BLOCK_FLOORS_UPD` (before update), `TRG_WS_IPK_NU_QS_Q` (after insert or update or delete)

## DEFINITIONS.ROOMS

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_ID | VARCHAR2(7) | N |  |
| CATEGORY_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| CAPACITY | NUMBER(4) | N |  |
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N |  |
| CHARGES_PER_DAY | NUMBER(10) | Y |  |
| BUILDING_BLOCK_FLOOR_ID | VARCHAR2(10) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| COVID | VARCHAR2(1) default 'N' | Y | This flag is used to mark Room as Y= COVID, N= Non-COVID |
| SEX_ID | NUMBER(1) | Y | this column is used to save the sex of patient |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| COVERED_AREA | NUMBER | Y | This column is used to store the covered area of building in square feet |
| MASTER_INPATIENT_UNIT | VARCHAR2(3) | Y |  |

- **PK** `PK_ROOMS`: ROOM_ID
- **FK** `FK_ROOMS1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **FK** `FK_ROOMS_02`: (BUILDING_BLOCK_FLOOR_ID) -> DEFINITIONS.BUILDING_BLOCK_FLOORS(BUILDING_BLOCK_FLOOR_ID) [disabled]
- **CHECK** `CHK_ROOMS_01`: ACTIVE IN ('Y','N'
- **Triggers**: `ROOMS_DEL` (after delete), `ROOMS_INS` (before insert), `ROOMS_POST_INSERT` (after insert), `ROOMS_UPD` (before update), `ROOMS_UPDT` (before update), `UPD_COVID_ROOMS` (before update of covid)

## DEFINITIONS.BED_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| EVENT_ID | VARCHAR2(3) | N |  |
| EVENT_DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_BED_STATUS`: EVENT_ID
- **Triggers**: `BED_STATUS_CEA` (before insert or update or delete), `BED_STATUS_DEL` (after delete), `BED_STATUS_INS` (before insert), `BED_STATUS_UPD` (before update), `TRG_WS_LKU_SR_JI_Q` (after insert or update or delete)

## DEFINITIONS.DEF_BED

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| ROOM_ID | VARCHAR2(7) | N |  |
| BED_START_DATE | DATE | N |  |
| AVAILABLE | CHAR(1) default 'Y' | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| CATEGORY_ID | VARCHAR2(6) | N |  |
| BED_END_DATE | DATE | Y |  |
| BED_ID_ORDER_BY | NUMBER(9) | Y |  |
| BED_CLEANING | CHAR(1) default 'N' | Y |  |
| BED_MAINTENANCE | CHAR(1) default 'N' | Y |  |
| BED_READY | CHAR(1) default 'N' | Y |  |
| CLEANING_DATE | DATE | Y |  |
| MAINTENANCE_DATE | DATE | Y |  |
| READY_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| BED_DESC | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| MAINTENANCE_BY | VARCHAR2(14) | Y |  |
| READY_BY | VARCHAR2(14) | Y |  |
| READY_MINUTES | NUMBER(9) | Y |  |
| EVENT_ID | VARCHAR2(3) | Y |  |
| EVENT_DATE | DATE | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| FRAT_REQUIRED | CHAR(1) default 'U' | N | 'Y' = Yes , "N' = No, 'U' = Unknown |
| FCP_REQUIRED | CHAR(1) default 'U' | N | 'Y' = Yes , "N' = No, 'U' = Unknown |
| VIRTUAL | VARCHAR2(1) default 'N' | Y |  |
| SIGNED_DATE | DATE | Y |  |
| BED_ISOLATION | VARCHAR2(1) default 'N' | Y | Flag use for bed isolation |
| ISOLATION_DATE | DATE | Y |  |
| ISOLATION_BY | VARCHAR2(14) | Y |  |
| RESERVED_FOR_TRANSFER | VARCHAR2(1) default 'N' | Y | Flag use for bed researved EAR to IPD,OR and OR to IPD transferred with same admission |
| MAINTENANCE_TYPE_ID | VARCHAR2(5) | Y |  |
| FUNCTIONAL_ORD_LOCATION_ID | VARCHAR2(3) | Y | This column contains FUNCTIONAL ORDER LOCATION ID OF BED |
| FUNCTIONAL_PAYMENT_CAT_ID | VARCHAR2(3) | Y | This column contains FUNCTIONAL PAYMENT CATEGORY OF BED |
| FUNCTIONAL_CATEGORY_ID | VARCHAR2(6) | Y | This column contains FUNCTIONAL CATEGORY OF BED |
| FUNCTIONAL_ROOM_ID | VARCHAR2(7) | Y | This column contains FUNCTIONAL ROOM INFORMATION |
| EXCLUDE | VARCHAR2(1) | Y |  |

- **PK** `PK_DEF_BED`: BED_ID, LOCATION_ID
- **FK** `FK_DEF_BED_01`: (ROOM_ID) -> DEFINITIONS.ROOMS(ROOM_ID) [disabled]
- **FK** `FK_DEF_BED_02`: (EVENT_ID) -> DEFINITIONS.BED_STATUS(EVENT_ID) [disabled]
- **CHECK** `CHK_DEF_BED_01`: AVAILABLE IN ('Y','N'
- **CHECK** `CHK_DEF_BED_02`: ACTIVE IN ('Y','N'
- **CHECK** `CHK_DEF_BED_03`: FRAT_REQUIRED IN ('N','U','Y'
- **CHECK** `CHK_DEF_BED_04`: FCP_REQUIRED IN ('N','U','Y'
- **Triggers**: `DEF_BED_AFTER_UPD` (after update), `DEF_BED_CEA` (before insert or update or delete), `DEF_BED_DEL` (after delete), `DEF_BED_INS` (before insert), `DEF_BED_PENDING_Q` (after update), `DEF_BED_UPD` (before update), `DEF_BED_UPT` (before update), `MAINTAIN_BEDS_DESC_HISTORY` (after update of bed_desc), `TRG_WS_DWW_GE_MI_Q` (after insert or update or delete)

## DEFINITIONS.DOCTOR

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | N | First Three digits show location_id and rest 4 digits use for counter |
| NAME | VARCHAR2(500) | Y |  |
| SPECIALITY | VARCHAR2(200) | Y |  |
| DEGREES | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| HIS_USERID | VARCHAR2(10) | Y |  |
| CONSULTANT | VARCHAR2(1) default 'N' | N |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DIAGNOSTIC_DOCTOR | VARCHAR2(1) default 'N' | Y |  |
| RESIDENT_DOCTOR | VARCHAR2(1) | Y |  |
| FULL_NAME | VARCHAR2(500) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |
| ONCOLOGIST | CHAR(1) default 'N' | Y |  |
| LETTER_HEAD1 | VARCHAR2(500) | Y |  |
| LETTER_HEAD2 | VARCHAR2(1000) | Y |  |
| EXTENSION | VARCHAR2(45) | Y |  |
| FAX | VARCHAR2(45) | Y |  |
| EMAIL | VARCHAR2(45) | Y |  |
| DORTOR_INITIALS | VARCHAR2(5) | Y |  |
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| DR_SURNAME | VARCHAR2(10) | Y |  |
| HOSPITALIST | CHAR(1) default 'N' | Y |  |
| CLIENT_ID | VARCHAR2(10) | Y |  |
| SHARE_ON_PERFORM | CHAR(1) default 'N' | Y |  |
| LETTER_HEAD2_DRAFT | VARCHAR2(1000) | Y |  |
| FULL_NAME_DRAFT | VARCHAR2(180) | Y |  |
| PANEL_SENIORITY | NUMBER(3) | Y |  |
| PANEL_DR_NAME | VARCHAR2(180) | Y |  |
| REMARKS | VARCHAR2(250) | Y |  |
| FELLOW_DOCTOR | VARCHAR2(1) default 'N' | Y |  |
| PRINT_FEEDBACK_ON_WORKORDER | CHAR(1) default 'N' | Y | This flag indicates if feedback form will be printed on work order or not. 'Y' for Yes and 'N' for No. |
| CANOAT_CHECK | CHAR(1) default 'N' | Y | Y mean this doctor is authorized to order CA/NonCA |
| PERIODLY_STATUS_ALLOWED | CHAR(1) | Y | Y means, this consultant can change patient status for specific time duration |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| IH_PRACTITIONER | VARCHAR2(1) default 'N' | Y |  |
| IS_ENCRYPTED | CHAR(1) default 'N' | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| DOCTOR_TYPE | CHAR(1) | Y |  |

- **PK** `PK_DOCTOR`: DOCTOR_ID
- **FK** `FK_DOCTOR`: (DOCTOR_MRNO) -> REGISTRATION.PATIENT(MRNO)
- **CHECK** `CHK_ACTIVE_DOTOR`: ACTIVE IN ('H','Y','N','Z'
- **CHECK** `CK_DOCTOR_1`: ONCOLOGIST IN ('Y','N'
- **CHECK** `CK_DOCTOR_2`: CONSULTANT IN ('Y','N'
- **CHECK** `CK_DOCTOR_3`: HOSPITALIST IN ('Y','N'
- **CHECK** `CK_DOCTOR_5`: PRINT_FEEDBACK_ON_WORKORDER IN ('Y','N'
- **Triggers**: `DOCOTR_ID_SEQ_INSERT` (before insert), `DOCTOR_CEA` (before insert or update or delete), `DOCTOR_CHECK_MRNO` (before insert or update of doctor_mrno, dr_surname), `DOCTOR_CHECK_UPD_INS` (before insert or update), `DOCTOR_HIST_INSERTION` (before insert or update of doctor_mrno,full_name,letter_head1,letter_head2,extension,fax,email), `DOCTOR_INS` (before insert), `DOCTOR_MRNO_UPD_INS` (before insert or update of doctor_mrno), `DOCTOR_NAME_UPD_INS` (before insert or update of name, full_name), `DOCTOR_TS` (before insert or update or delete), `SETUP_REVIEW_ALERT_DR_INS` (after insert), `SETUP_REVIEW_ALERT_DR_UPD` (after update of consultant, diagnostic_doctor, resident_doctor), `TRG_WS_XSS_DT_IF_Q` (after insert or update or delete)

## DEFINITIONS.BEDS

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ORDER_TYPE_ID | VARCHAR2(3) | Y |  |
| ORDER_NO | VARCHAR2(9) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| ADMISSION_NO | VARCHAR2(14) | N |  |
| DOCTOR_ID | VARCHAR2(7) | N |  |
| DOCTOR_DISCHARGE | CHAR(1) default 'N' | Y |  |
| DISCHARGE_START | CHAR(1) default 'N' | Y |  |
| NAME | VARCHAR2(183) | Y |  |
| SEX | VARCHAR2(15) | Y |  |
| DOB | DATE | Y |  |
| ADMISSION_DATE | DATE | N |  |
| BBK_CLEARED | CHAR(1) default 'N' | N |  |
| ADMISSION_FINAL | VARCHAR2(1) default 'N' | N |  |
| PHARMACY_BLOCKED | CHAR(1) default 'N' | N |  |
| NURSE_MRNO | VARCHAR2(14) | Y |  |
| HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| HOSPITALIST_NAME | VARCHAR2(193) | Y |  |
| COVERING_HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| TEMP_BS_DISCHARGE | CHAR(1) default 'N' | N |  |
| MARKED_FOR_ALERT | CHAR(1) default 'N' | N |  |
| NUTRITIONIST_MRNO | VARCHAR2(14) | Y |  |
| BED_STATUS | CHAR(1) default 'N' | N | F Free,  N Not Free |
| SEND_ALERT | CHAR(1) default 'N' | N | Y Send  N not send |
| NURSE_CLEARANCE | CHAR(1) default 'N' | Y |  |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | Y | This column will be  upated on (discharge summary sign by doctor,pharmacy clearance,Nursing clearance and null on admission off  final discharge) events |
| PHARMACIST_NOTE | CHAR(1) default 'N' | Y | Y mean pharmacist has entered notes |
| ADMISSION_TYPE | VARCHAR2(3) default 'IPD' | Y | 'IPD' for Inpatient and 'EAR' for Emergency assessment room dummy Admission |
| BED_LOCATION_ID | VARCHAR2(3) | N |  |
| SUPPLIES_CLEARANCE | CHAR(1) default 'N' | N | Y MEAN USER HAS CLEARED SUPPLIES |
| FORMER_MRNO | VARCHAR2(14) | Y |  |
| TRANSFER_SERVICE_DATE | DATE | Y | This column is using for transfer service type of "EAR TO IPD" or "EAR TO OR" transfer |
| PREVIOUS_ADMISSION_TYPE | VARCHAR2(3) | Y | This column contains value of admission_type after change admission_type |
| CURRENT_ADMISSION_LOCATION | VARCHAR2(3) | Y | This column contains value of  current admission_location |
| PREVIOUS_ADMISSION_LOCATION | VARCHAR2(3) | Y | This column contains value of admission_location after change admission_location |

- **PK** `BEDS_ASSIGN_1`: MRNO
- **UK** `UK_ORDER_KEY`: ORDER_TYPE_ID, ORDER_NO, LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_BEDS_02`: (BED_ID, BED_LOCATION_ID) -> DEFINITIONS.DEF_BED(BED_ID, LOCATION_ID) [disabled]
- **FK** `FK_BEDS_1`: (DOCTOR_ID) -> DEFINITIONS.DOCTOR(DOCTOR_ID) [disabled]
- **CHECK** `CK_BEDS1`: DOCTOR_DISCHARGE IN ('Y','N'
- **CHECK** `CK_BEDS_001`: DISCHARGE_START IN ('Y','N'
- **CHECK** `CK_BEDS_002`: ADMISSION_FINAL IN ('N','Y'
- **CHECK** `CK_BEDS_2`: BBK_CLEARED IN ('N','Y'
- **CHECK** `CK_BEDS_3`: DISCHARGE_START IN ('N','Y'
- **CHECK** `CK_BEDS_4`: BED_STATUS IN('F','N'
- **CHECK** `CK_BEDS_5`: SEND_ALERT IN('Y','N'
- **Triggers**: `AHB_PATIENTS_PQ` (after insert or update or delete), `BEDS_ADMISSION_TYPE_UPD` (before update), `BEDS_DEL` (after delete), `BEDS_INS` (before insert), `BEDS_INSERT` (before insert), `BEDS_PENDING_Q` (after insert or update), `BEDS_UPD` (before update), `BEDS_UPDT` (before update), `DISCHARGE_PATIENT_PENDING_QUEUE` (before update of designation_category_id), `INP_DISCHARGE_FINAL` (before delete), `IPD_DISCHARGE_EVENT_UPD` (after update), `PENDING_QUEUE_DNR_DELETE` (after delete), `SEND_DISCHARGE_ALERTS` (after update), `TRG_WS_ZNW_OL_NQ_Q` (after insert or update or delete)

## DEFINITIONS.BEDS_ACTIVE_HISTORY
This is transaction table to store bed activation history. Never delete data from here. Idrees.

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_BEDS_ACTIVE_HISTORY`: BED_ID, TRN_DATE
- **Triggers**: `BEDS_ACTIVE_HISTORY_DEL` (after delete), `BEDS_ACTIVE_HISTORY_INS` (before insert), `BEDS_ACTIVE_HISTORY_UPD` (before update)

## DEFINITIONS.BEDS_CATEGORY_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_BEDS_CATEGORY_HISTORY`: BED_ID, TRN_DATE
- **Triggers**: `BEDS_CATEGORY_HISTORY_DEL` (after delete), `BEDS_CATEGORY_HISTORY_INS` (before insert), `BEDS_CATEGORY_HISTORY_UPD` (before update)

## DEFINITIONS.BEDS_DESC_HISTORY
This is transaction table to store bed description history.

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ROOM_ID | VARCHAR2(7) | Y |  |
| BED_DESC | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| START_DATE | DATE | Y |  |
| OUT_DATE | DATE | Y |  |
| OUTDATE_USER | VARCHAR2(14) | Y |  |
| OUTDATE_TERMINAL | VARCHAR2(30) | Y |  |
| SERIAL_NO | NUMBER(6) | N |  |

- **PK** `PK_BED_DESC_HIST`: BED_ID, LOCATION_ID, SERIAL_NO

## DEFINITIONS.BEDS_FUNCTIONAL_UNIT_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| BED_DESC | VARCHAR2(7) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| ROOM_ID | VARCHAR2(7) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| PAYMENT_CATEGORY_ID | VARCHAR2(3) | Y |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| FUNCTIONAL_ORD_LOCATION_ID | VARCHAR2(3) | Y |  |
| FUNCTIONAL_PAYMENT_CAT_ID | VARCHAR2(3) | Y |  |
| FUNCTIONAL_CATEGORY_ID | VARCHAR2(6) | Y |  |
| FUNCTIONAL_START_DATE | DATE | Y |  |
| FUNCTIONAL_END_DATE | DATE | Y |  |
| FUNCTIONAL_MARKED_BY | VARCHAR2(14) | Y |  |
| FUNCTIONAL_UNMARKED_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| SIGNED_DATE | DATE | Y |  |
| FUNCTIONAL_ROOM_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_BEDS_FUNCTIONAL_UNIT_HISTORY`: BED_ID, LOCATION_ID, SERIAL_NO

## DEFINITIONS.BED_LAST_MRNO_R

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| ROOM_ID | VARCHAR2(7) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| ORDER_TYPE_ID | VARCHAR2(3) | Y |  |
| ORDER_NO | VARCHAR2(9) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| ADMISSION_NO | VARCHAR2(14) | Y |  |
| NEW_USER_ID | VARCHAR2(30) | Y |  |
| NEW_TERMINAL | VARCHAR2(30) | Y |  |
| NEW_TRN_DATE | DATE | Y |  |
| TRN_STATUS | VARCHAR2(3) | Y |  |
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| ADMISSION_DATE | DATE | Y |  |
| ADMISSION_FINAL | VARCHAR2(1) | Y |  |
| BBK_CLEARED | CHAR(1) | Y |  |
| DISCHARGE_START | CHAR(1) | Y |  |
| DOB | DATE | Y |  |
| DOCTOR_DISCHARGE | CHAR(1) | Y |  |
| NAME | VARCHAR2(183) | Y |  |
| SEX | VARCHAR2(15) | Y |  |
| NURSE_MRNO | VARCHAR2(14) | Y |  |
| PHARMACY_BLOCKED | CHAR(1) | Y |  |
| BED_START_DATE | DATE | Y |  |
| AVAILABLE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| HOSPITALIST_NAME | VARCHAR2(193) | Y |  |
| COVERING_HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| TEMP_BS_DISCHARGE | CHAR(1) | Y |  |
| MARKED_FOR_ALERT | CHAR(1) | Y |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| BED_END_DATE | DATE | Y |  |
| NUTRITIONIST_MRNO | VARCHAR2(14) | Y |  |


## DEFINITIONS.BED_START_R

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_ID | VARCHAR2(7) | N |  |
| ROOM_ID | VARCHAR2(7) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| ORDER_TYPE_ID | VARCHAR2(3) | Y |  |
| ORDER_NO | VARCHAR2(9) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| ADMISSION_NO | VARCHAR2(14) | Y |  |
| NEW_USER_ID | VARCHAR2(30) | Y |  |
| NEW_TERMINAL | VARCHAR2(30) | Y |  |
| NEW_TRN_DATE | DATE | Y |  |
| TRN_STATUS | VARCHAR2(3) | Y |  |
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| ADMISSION_DATE | DATE | Y |  |
| ADMISSION_FINAL | VARCHAR2(1) | Y |  |
| BBK_CLEARED | CHAR(1) | Y |  |
| DISCHARGE_START | CHAR(1) | Y |  |
| DOB | DATE | Y |  |
| DOCTOR_DISCHARGE | CHAR(1) | Y |  |
| NAME | VARCHAR2(183) | Y |  |
| SEX | VARCHAR2(15) | Y |  |
| NURSE_MRNO | VARCHAR2(14) | Y |  |
| PHARMACY_BLOCKED | CHAR(1) | Y |  |
| BED_START_DATE | DATE | Y |  |
| AVAILABLE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| HOSPITALIST_NAME | VARCHAR2(193) | Y |  |
| COVERING_HOSPITALIST_MRNO | VARCHAR2(14) | Y |  |
| TEMP_BS_DISCHARGE | CHAR(1) | Y |  |
| MARKED_FOR_ALERT | CHAR(1) | Y |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| BED_END_DATE | DATE | Y |  |
| NUTRITIONIST_MRNO | VARCHAR2(14) | Y |  |


## DEFINITIONS.BENEFITS

| Column | Type | Null | Comment |
|---|---|---|---|
| BENEFIT_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_BENEFITS`: BENEFIT_ID
- **Triggers**: `BENEFITS_CEA` (before insert or update or delete), `BENEFITS_DEL` (after delete), `BENEFITS_INS` (before insert), `BENEFITS_UPD` (before update), `TRG_WS_XUD_TE_MM_Q` (after insert or update or delete)

## DEFINITIONS.BILL

| Column | Type | Null | Comment |
|---|---|---|---|
| BILL_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_BILL`: BILL_ID
- **Triggers**: `BILL_DEL` (after delete), `BILL_INS` (before insert), `BILL_UPD` (before update)

## DEFINITIONS.BLOOD_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| BLOOD_GROUP_ID | VARCHAR2(50) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| BARCODE | VARCHAR2(50) | N |  |
| ORDER_BY | NUMBER(2) | Y |  |
| UPDATED_BY | VARCHAR2(30) | Y |  |
| UPDATED_DATE | DATE | Y |  |
| ABO | VARCHAR2(50) | Y | This column add on request of Dr. Zeyd. |
| RHD | VARCHAR2(50) | Y | This column add on request of Dr. Zeyd. |
| ALLOWED_FOR_ALIQUOTING | CHAR(1) | Y |  |
| ALLOWED_FOR_POOLING | CHAR(1) | Y |  |
| POOL_ABO | VARCHAR2(50) | Y |  |
| POOL_RHD | VARCHAR2(50) | Y |  |

- **PK** `PK_BLOOD_GROUP`: BLOOD_GROUP_ID
- **UK** `UK_BLOOD_GROUP_1`: BARCODE
- **CHECK** `CK_BLOOD_GROUP_001`: ACTIVE IN ('Y','N'
- **Triggers**: `BLOOD_GROUP_CEA` (before insert or update or delete), `BLOOD_GROUP_DEL` (after delete), `BLOOD_GROUP_INS` (before insert), `BLOOD_GROUP_TS` (before insert or update or delete), `BLOOD_GROUP_UPD` (before update), `TRG_WS_QQS_YK_KP_Q` (after insert or update or delete)

## DEFINITIONS.BMT_ABO_MISMATCH

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N | It will contain protocol list |
| ABO_MISMATCH_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y | It will contain to order the record in transaction screen and setup screen |
| AGE_GROUP | VARCHAR2(1) | Y |  |

- **PK** `PK_BMT_ABO_MISATCH`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, ABO_MISMATCH_ID
- **Triggers**: `BMT_ABO_MISMATCH_CEA` (before insert or update or delete), `BMT_ABO_MISMATCH_DEL` (after delete), `BMT_ABO_MISMATCH_INS` (before insert), `BMT_ABO_MISMATCH_UPD` (before update), `TRG_WS_SGA_VW_OE_Q` (after insert or update or delete)

## DEFINITIONS.BMT_BLOOD_PRODUCT

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N |  |
| BLOOD_PRODUCT_ID | VARCHAR2(3) | N | It will contain blood product id from setup list |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y | It will contain to order the record in transaction screen and setup screen |
| AGE_GROUP | VARCHAR2(1) | Y |  |

- **PK** `PK_BMT_BLOOD_PRODUCT`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, BLOOD_PRODUCT_ID
- **Triggers**: `BMT_BLOOD_PRODUCT_CEA` (before insert or update or delete), `BMT_BLOOD_PRODUCT_DEL` (after delete), `BMT_BLOOD_PRODUCT_INS` (before insert), `BMT_BLOOD_PRODUCT_UPD` (before update), `TRG_WS_XFP_ZT_NF_Q` (after insert or update or delete)

## DEFINITIONS.BMT_HLA_TYPING

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N |  |
| HLA_TYPING_ID | VARCHAR2(3) | N | It will contain blood product id from setup list |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| RESTRICTION_ALLOWED | VARCHAR2(1) | Y |  |
| INITIAL_VALUE | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y | It will contain to order the record in transaction screen and setup screen |
| AGE_GROUP | VARCHAR2(1) | Y |  |

- **PK** `PK_BMT_HLA_TYPING`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, HLA_TYPING_ID
- **Triggers**: `BMT_HLA_TYPING_CEA` (before insert or update or delete), `BMT_HLA_TYPING_DEL` (after delete), `BMT_HLA_TYPING_INS` (before insert), `BMT_HLA_TYPING_UPD` (before update), `TRG_WS_AAG_TV_JO_Q` (after insert or update or delete)

## DEFINITIONS.BMT_PROTOCOL_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N | It will contain protocol id from setup list |
| DAY_NO | NUMBER | N |  |
| MAJOR_EVENT_DESC | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y | It will contain to order the record in transaction screen and setup screen |
| VALIDATE_RECORD | VARCHAR2(1) default 'N' | Y | It will contain value to validate the record on transaction screen or not |
| AGE_GROUP | VARCHAR2(1) | N |  |

- **PK** `PK_BMT_PROTOCOL_DAYS`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, DAY_NO, AGE_GROUP
- **Triggers**: `BMT_PROTOCOL_DAYS_CEA` (before insert or update or delete), `BMT_PROTOCOL_DAYS_DEL` (after delete), `BMT_PROTOCOL_DAYS_INS` (before insert), `BMT_PROTOCOL_DAYS_UPD` (before update), `TRG_WS_LVF_EK_ER_Q` (after insert or update or delete)

## DEFINITIONS.BMT_PROTOCOL_DAYS_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N |  |
| DAY_NO | NUMBER | N |  |
| PARAM_ID | NUMBER | Y |  |
| PARAM_VALUE | VARCHAR2(100) | N | It will contain parameter id defined, this string will be used to replace on transaction screen with number value |

- **PK** `PK_BMT_PROTOCOL_DAYS_DTL`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, DAY_NO, PARAM_VALUE
- **Triggers**: `BMT_PROTOCOL_DAYS_DTL_CEA` (before insert or update or delete), `BMT_PROTOCOL_DAYS_DTL_DEL` (after delete), `BMT_PROTOCOL_DAYS_DTL_INS` (before insert), `BMT_PROTOCOL_DAYS_DTL_UPD` (before update), `TRG_WS_QVO_QM_OB_Q` (after insert or update or delete)

## DEFINITIONS.BMT_SEROLOGY

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N | It will contain protocol list |
| SEROLOGY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y | It will contain to order the record in transaction screen and setup screen |
| AGE_GROUP | VARCHAR2(1) | Y |  |

- **PK** `PK_BMT_SEROLOGY`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, SEROLOGY_ID
- **Triggers**: `BMT_SEROLOGY_CEA` (before insert or update or delete), `BMT_SEROLOGY_DEL` (after delete), `BMT_SEROLOGY_INS` (before insert), `BMT_SEROLOGY_UPD` (before update), `TRG_WS_AXA_JJ_XK_Q` (after insert or update or delete)

## DEFINITIONS.BMT_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N |  |
| SR_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DETAIL_TYPE | VARCHAR2(100) | Y |  |
| AGE_GROUP | VARCHAR2(1) | Y |  |
| RAD_THERAPY_DOSE | NUMBER | Y |  |
| FRACTIONS | NUMBER | Y |  |
| REMARKS_MANDATORY | VARCHAR2(1) default 'N' | Y |  |
| TREATMENT_TYPE | VARCHAR2(2) | N |  |
| VALUE | NUMBER(2) | Y |  |
| DEFAULT_VALUE | VARCHAR2(1) default 'N' | Y |  |
| DONOR | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_BMT_SETUP_DETAIL`: SETUP_TYPE_ID, SR_NO, TREATMENT_TYPE
- **Triggers**: `BMT_SETUP_DETAIL_CEA` (before insert or update or delete), `BMT_SETUP_DETAIL_DEL` (after delete), `BMT_SETUP_DETAIL_INS` (before insert), `BMT_SETUP_DETAIL_UPD` (before update), `TRG_WS_LDW_JB_YC_Q` (after insert or update or delete)

## DEFINITIONS.BMT_SETUP_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_BMT_SETUP_MASTER`: SETUP_TYPE_ID
- **Triggers**: `BMT_SETUP_MASTER_CEA` (before insert or update or delete), `BMT_SETUP_MASTER_DEL` (after delete), `BMT_SETUP_MASTER_INS` (before insert), `BMT_SETUP_MASTER_UPD` (before update), `TRG_WS_HTV_LF_VL_Q` (after insert or update or delete)

## DEFINITIONS.BMT_TEMPLATE_PROTOCOLS

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_TYPE_ID | VARCHAR2(3) | N | It will contain PK value |
| SETUP_SR_NO | NUMBER | N | It will contain serial no against setup type id |
| PROTOCOL_ID | VARCHAR2(50) | N | It will contain protocol list |
| CONDITIONING | VARCHAR2(4000) | Y |  |
| GVH_PROPHYLAXIS | VARCHAR2(4000) | Y |  |
| PROPHYLACTIC_MEDICATIONS | VARCHAR2(4000) | Y |  |
| GROWTH_FACTOR | VARCHAR2(4000) | Y |  |
| PREVIOUS_INFECTIONS | VARCHAR2(4000) | Y |  |
| EMPIRIC_ANTIBIOTICS | VARCHAR2(4000) | Y |  |
| NUTRITINAL_SUPPORT | VARCHAR2(4000) | Y |  |
| POST_DISCHARGE_REMARKS | VARCHAR2(4000) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| AGE_GROUP | VARCHAR2(1) | N |  |
| BLOOD_PRODUCT_REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_TEMPLATE_PROTOCOLS`: SETUP_TYPE_ID, SETUP_SR_NO, PROTOCOL_ID, AGE_GROUP
- **Triggers**: `BMT_TEMPLATE_PROTOCOLS_CEA` (before insert or update or delete), `BMT_TEMPLATE_PROTOCOLS_DEL` (after delete), `BMT_TEMPLATE_PROTOCOLS_INS` (before insert), `BMT_TEMPLATE_PROTOCOLS_UPD` (before update), `TRG_WS_XKO_CZ_IA_Q` (after insert or update or delete)

## DEFINITIONS.BODY_SITE

| Column | Type | Null | Comment |
|---|---|---|---|
| BODY_SITE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_BODY_SITE`: BODY_SITE_ID
- **CHECK** `CK_BODY_SITE_001`: ACTIVE IN ('Y','N'
- **Triggers**: `BODY_SITE_CEA` (before insert or update or delete), `BODY_SITE_DEL` (after delete), `BODY_SITE_INS` (before insert), `BODY_SITE_UPD` (before update), `TRG_WS_IGF_RJ_RC_Q` (after insert or update or delete)

## DEFINITIONS.BONUS_ALLOWED_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |

- **PK** `PK_BONUS_ALLOWED_SECTION`: DEPARTMENT_ID, SECTION_ID

## DEFINITIONS.BONUS_RESTRICTED_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |

- **PK** `PK_BONUS_RESTRICTED_CPT`: CPT_ID
- **Triggers**: `BONUS_RESTRICTED_CPT_CEA` (before insert or update or delete), `TRG_WS_MLA_EA_FW_Q` (after insert or update or delete)

## DEFINITIONS.BRIEF_NOTE_RESTRICTED_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(7) | N |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

_No standard audit columns._


## DEFINITIONS.BS_REVISED_CPT1_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CHANGE_DATE | DATE | Y |  |
| CPT | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| OLD_PRICE | NUMBER | Y |  |
| NEW_PRICE | NUMBER | Y |  |
| DEPARTMENT | VARCHAR2(255) | Y |  |
| SECTION | VARCHAR2(255) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| OLD_COST | NUMBER | Y |  |
| NEW_COST | NUMBER | Y |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | Y |  |


## DEFINITIONS.BUSINESS_CPT_CODES_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CODE | VARCHAR2(10) | Y |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| CPT_RATE | NUMBER(10,2) | Y |  |
| QTY_FAC | NUMBER(4) | Y |  |
| DOCTOR_SHARE | NUMBER(10,2) | Y |  |
| DEPARTMENT_ID | VARCHAR2(4) | Y |  |
| GROUP_CODE | VARCHAR2(2) | Y |  |
| DEFAULT_DOCTOR | VARCHAR2(5) | Y |  |


## DEFINITIONS.CALLED_OBJECT_PARAMETERS
If a form is calling within another form then we have to define x position and y position of called form, we will enter the values in this form, this table is detail of the definitions.objects , a form may be called from more than one form then more than one rows will be entered

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N | Refrence key |
| CALLING_OBJECT_CODE | VARCHAR2(11) | N | Form code which is calling this object |
| WIN_X_POS | NUMBER(5,2) default 0 | N | X position on which called form will be open |
| WIN_Y_POS | NUMBER(5,2) default 0 | N | Y position on which called form will be open |
| WIN_WIDTH | NUMBER(5,2) default 0 | N | Width of the Window |
| WIN_HEIGHT | NUMBER(5,2) default 0 | N | Height of the Window |

- **PK** `PK_CALLED_OBJECT_PARAMETERS`: OBJECT_CODE, CALLING_OBJECT_CODE
- **FK** `FK_CALLED_OBJECT_PARAMETERS_1`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **FK** `FK_CALLED_OBJECT_PARAMETERS_2`: (CALLING_OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **Triggers**: `CALLED_OBJECT_PARAMETERS_DEL` (after delete), `CALLED_OBJECT_PARAMETERS_INS` (before insert), `CALLED_OBJECT_PARAMETERS_UPD` (before update)

## DEFINITIONS.CALL_CENTER_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| CC_DESIGNATION_ID | NUMBER(10) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ACTING_DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DESIGNATION_TYPE | VARCHAR2(1) | Y |  |

- **PK** `PK_CALL_CENTER_DESIGNATION`: CC_DESIGNATION_ID
- **Triggers**: `CALL_CENTER_DESIGNATION_DEL` (after delete), `CALL_CENTER_DESIGNATION_INS` (before insert), `CALL_CENTER_DESIGNATION_UPD` (before update), `TRG_WS_KYT_CN_SE_Q` (after insert or update or delete)

## DEFINITIONS.CALL_CENTER_PATIENT_QUERY

| Column | Type | Null | Comment |
|---|---|---|---|
| QUERY_ID | NUMBER(10) | N |  |
| QUERY_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CALL_CENTER_PATIENT_QUERY`: QUERY_ID
- **Triggers**: `CALL_CENTER_PATIENT_QUERY_DEL` (after delete), `CALL_CENTER_PATIENT_QUERY_INS` (before insert), `CALL_CENTER_PATIENT_QUERY_UPD` (before update), `TRG_WS_NXP_NK_WQ_Q` (after insert or update or delete)

## DEFINITIONS.CALL_CENTER_REQUEST_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | VARCHAR2(3) | N |  |
| STATUS_DESC | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CALL_CENTER_REQUEST_STATUS`: STATUS_ID
- **Triggers**: `CALL_CENTER_REQUEST_STATUS_DEL` (after delete), `CALL_CENTER_REQUEST_STATUS_INS` (before insert), `CALL_CENTER_REQUEST_STATUS_UPD` (before update)

## DEFINITIONS.CANCER_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| CANCER_GROUP_ID | NUMBER(3) | N |  |
| CANCER_GROUP_DESC | VARCHAR2(300) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CANCER_GROUPS`: CANCER_GROUP_ID
- **UK** `UK_CANCER_GROUPS`: CANCER_GROUP_DESC
- **CHECK** `CK_CANCER_GROUPS_1`: CANCER_GROUP_DESC IS NOT NULL
- **CHECK** `CK_CANCER_GROUPS_2`: ACTIVE IN ('Y','N'
- **Triggers**: `CANCER_GROUPS_CEA` (before insert or update or delete), `CANCER_GROUPS_DEL` (after delete), `CANCER_GROUPS_INS` (before insert), `CANCER_GROUPS_UPD` (before update), `TRG_WS_ZAL_HA_UX_Q` (after insert or update or delete)

## DEFINITIONS.CANCER_GROUPS_MORPH_PRECEDENCE

| Column | Type | Null | Comment |
|---|---|---|---|
| MORPH_CODE_FROM | VARCHAR2(7) | N |  |
| MORPH_CODE_TO | VARCHAR2(7) | N |  |
| PRECEDENCE_OVER_ICD | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CANCER_GROUPS_MORPH_PREC`: MORPH_CODE_FROM, MORPH_CODE_TO
- **CHECK** `CK_PRECEDENCE_OVER_ICD`: PRECEDENCE_OVER_ICD IN ('Y', 'N'
- **Triggers**: `CANCER_GROUPS_MORPH_PRECEDENCE_CEA` (before insert or update or delete), `CANCER_GRP_MORPH_PRECDNS_DEL` (after delete), `CANCER_GRP_MORPH_PRECDNS_INS` (before insert), `CANCER_GRP_MORPH_PRECDNS_UPD` (before update), `TRG_WS_RYQ_LS_EJ_Q` (after insert or update or delete)

## DEFINITIONS.CANCER_GROUPS_OF_PATIENT_DET

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| CANCER_GROUP_ID | NUMBER(3) | Y |  |
| ICD_ID | VARCHAR2(11) | Y |  |
| MORPH_CODE | VARCHAR2(11) | Y |  |
| AGE_GROUP | CHAR(1) | N |  |
| ICD_CHAPTER_ID | VARCHAR2(3) | Y |  |
| ICD_GROUP_ID | VARCHAR2(3) | Y |  |
| ICD_CATEGORY_ID | VARCHAR2(3) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **UK** `PK_CANCER_GROUPS_OF_PAT_DET`: MRNO, CANCER_GROUP_ID, ICD_ID, MORPH_CODE
- **FK** `FK_CANCER_GROUPS_OF_PAT_DET_2`: (MRNO) -> REGISTRATION.PATIENT(MRNO)
- **CHECK** `CHK_CGOPD_01`: AGE_GROUP IN ('A', 'P'
- **Triggers**: `CANCER_GRP_OF_PAT_DET_DEL` (after delete), `CANCER_GRP_OF_PAT_DET_INS` (before insert), `CANCER_GRP_OF_PAT_DET_UPD` (before update)

## DEFINITIONS.CANCER_GROUPS_OF_PATIENT_SUM

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| CANCER_GROUP_ID | NUMBER(3) | N |  |
| AGE_GROUP | CHAR(1) | N |  |
| ICD_CHAPTER_ID | VARCHAR2(3) | Y |  |
| ICD_GROUP_ID | VARCHAR2(3) | Y |  |
| ICD_CATEGORY_ID | VARCHAR2(3) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_CANCER_GROUPS_OF_PAT_SUM`: MRNO, CANCER_GROUP_ID
- **CHECK** `CHK_CGOPS_01`: AGE_GROUP IN ('A', 'P'
- **Triggers**: `CANCER_GRPS_OF_PAT_SUM_DEL` (after delete), `CANCER_GRPS_OF_PAT_SUM_INS` (before insert), `CANCER_GRPS_OF_PAT_SUM_UPD` (before update), `TRG_WS_EUW_GY_VC_Q` (after insert or update or delete), `TRG_WS_TAQ_CM_XE_Q` (after insert or update or delete)

## DEFINITIONS.CANCER_GROUP_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| CANCER_GRUOP_ID | NUMBER(3) | Y |  |
| VERSION | NUMBER(2) | Y |  |
| AGE_GROUP | CHAR(1) | Y | 'B' IS FOR BOTH ADULTS AND PAEDS, 'P' IS FOR PAEDS AND 'A' FOR ADULTS |
| ICD_ID_FROM | VARCHAR2(11) | Y |  |
| ICD_ID_TO | VARCHAR2(11) | Y |  |
| MORPH_CODE_FROM | VARCHAR2(7) | Y |  |
| MORPH_CODE_TO | VARCHAR2(7) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SERIAL_NO | NUMBER | N |  |

- **PK** `PK_CANCER_GROUP_SETUP`: CANCER_GRUOP_ID, SERIAL_NO
- **UK** `UK_CANCER_GROUP_SETUP`: CANCER_GRUOP_ID, VERSION, AGE_GROUP, ICD_ID_FROM, ICD_ID_TO, MORPH_CODE_FROM, MORPH_CODE_TO, ACTIVE
- **FK** `FK_CANCER_GROUP_SETUP_1`: (CANCER_GRUOP_ID) -> DEFINITIONS.CANCER_GROUPS(CANCER_GROUP_ID)
- **CHECK** `CK_CANCER_GROUP_SETUP_1`: AGE_GROUP IN ('B','A','P'
- **CHECK** `CK_CANCER_GROUP_SETUP_2`: ACTIVE IN ('Y','N'
- **CHECK** `CK_CANCER_GROUP_SETUP_3`: CANCER_GRUOP_ID IS NOT NULL
- **CHECK** `CK_CANCER_GROUP_SETUP_4`: VERSION IS NOT NULL
- **Triggers**: `CANCER_GROUP_SETUP_CEA` (before insert or update or delete), `CANCER_GROUP_SETUP_DEL` (after delete), `CANCER_GROUP_SETUP_INS` (before insert), `CANCER_GROUP_SETUP_UPD` (before update), `TRG_WS_KBA_JX_XP_Q` (after insert or update or delete)

## DEFINITIONS.CANVAS_OBJECTS

| Column | Type | Null | Comment |
|---|---|---|---|
| P_SCHEMA_ID | VARCHAR2(3) | N |  |
| P_OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| P_OBJECT_ID | VARCHAR2(5) | N |  |
| C_SCHEMA_ID | VARCHAR2(3) | N |  |
| C_OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| C_OBJECT_ID | VARCHAR2(5) | N |  |
| O_CALL | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CALL_LABEL | VARCHAR2(200) | Y |  |

- **PK** `PK_CANVAS_OBJECTS_1`: P_SCHEMA_ID, P_OBJECT_TYPE_ID, P_OBJECT_ID, C_SCHEMA_ID, C_OBJECT_TYPE_ID, C_OBJECT_ID
- **Triggers**: `CANVAS_OBJECTS_CEA` (before insert or update or delete), `TRG_WS_HEH_OQ_QC_Q` (after insert or update or delete)

## DEFINITIONS.CARD_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CARD_REASONS`: REASON_ID
- **UK** `UK_CARD_REASONS`: DESCRIPTION
- **Triggers**: `CARD_REASONS_CEA` (before insert or update or delete), `CARD_REASONS_DEL` (after delete), `CARD_REASONS_INS` (before insert), `CARD_REASONS_UPD` (before update), `TRG_WS_XNF_VX_PO_Q` (after insert or update or delete)

## DEFINITIONS.CARE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CARE_TYPE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CARE_TYPE`: CARE_TYPE_ID
- **Triggers**: `CARE_TYPE_DEL` (after delete), `CARE_TYPE_INS` (before insert), `CARE_TYPE_UPD` (before update)

## DEFINITIONS.CATEGORY_CODE

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_CODE | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CATEGORY_CODE`: CATEGORY_CODE

## DEFINITIONS.CATEGORY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **Triggers**: `CATEGORY_R_CEA` (before insert or update or delete), `TRG_WS_BZW_CN_KH_Q` (after insert or update or delete)

## DEFINITIONS.OCCUPATION

| Column | Type | Null | Comment |
|---|---|---|---|
| OCCUPATION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PROFESSION | CHAR(1) default 'N' | Y |  |

- **PK** `PK_OCCUPATION`: OCCUPATION_ID
- **Triggers**: `OCCUPATION_CEA` (before insert or update or delete), `OCCUPATION_DEL` (after delete), `OCCUPATION_INS` (before insert), `OCCUPATION_TS` (before insert or update or delete), `OCCUPATION_UPD` (before update), `TRG_WS_RYH_EH_NL_Q` (after insert or update or delete)

## DEFINITIONS.DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| CARD_SWIPE_EXEMPTION | VARCHAR2(1) default 'N' | Y |  |
| DUPLICATE | CHAR(1) default 'N' | N |  |
| PARENT_DESIGNATION_ID | VARCHAR2(6) | N |  |
| PARAMEDICAL_STAFF | CHAR(1) | Y |  |
| EMPLOYEE_NATURE | CHAR(1) | Y | O for Others, C for Consultants, D for Doctors, N for Nurses |
| EMAIL_REQUIRED | CHAR(1) default 'P' | Y |  |
| OCCUPATION_ID | VARCHAR2(6) | Y |  |
| IS_OSV_REQUIRED | CHAR(1) default 'N' | Y | This columns contains Y or N , either OSV is required or not against specific designation |
| OSV_TYPE | CHAR(1) | Y | This columns contain initiak three values Degree D, License L and Both B |
| JOB_TITLE | CHAR(1) | Y | This column should be used for travel request on Travel Request mode |
| JOB_ID | NUMBER | Y |  |
| INCENTIVE_ALLOWED | CHAR(1) | Y | 'Y' indicates that incentives are allowed for the designation, while 'N' indicates they are not. |
| LEAVE_RESTRICTION | CHAR(1) | Y |  |
| EMPLOYEE_CATEGORY | CHAR(1) | Y |  |
| OVERTIME_ALLOWED | CHAR(1) default 'N' | Y |  |
| JOB_DOCUMENT_REQUIRED | CHAR(1) default 'N' | Y | This column will be use for job web portal to check that is license/document required |

- **PK** `PK_DESIGNATION`: DESIGNATION_ID
- **UK** `U_DESCRIPTION`: DESCRIPTION
- **FK** `FK_OCCUPATION`: (OCCUPATION_ID) -> DEFINITIONS.OCCUPATION(OCCUPATION_ID) [disabled]
- **FK** `FK_OCCUPATION_1`: (PARENT_DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **CHECK** `CHK_DESIGNATION_1`: ACTIVE IN ('N','Y'
- **CHECK** `CK_DESIGNATION_001`: CARD_SWIPE_EXEMPTION IN ('Y','N'
- **CHECK** `CK_DESIGNATION_002`: DUPLICATE IN ('N','Y'
- **Triggers**: `DESIGNATION_CEA` (before insert or update or delete), `DESIGNATION_TS` (before insert or update or delete), `SETUP_REVIEW_ALERT_INS` (after insert), `TRG_WS_MFL_GP_BG_Q` (after insert or update or delete)

## DEFINITIONS.DESIGNATION_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| CLINICAL | CHAR(1) default 'N' | Y |  |
| FINANCIAL | CHAR(1) default 'N' | Y |  |
| DOCTOR_RELATED | CHAR(1) default 'N' | N |  |
| ON_CALL | CHAR(1) default 'N' | N |  |
| INCREMENT_RELATED | CHAR(1) default 'N' | Y | Flag for increment porpose only |
| REG_NO_REQ | CHAR(1) | Y |  |
| PAYROLL | CHAR(1) default 'N' | Y |  |
| HR_DOCUMENT | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DESIGNATION_CATEGORY`: DESIGNATION_CATEGORY_ID
- **CHECK** `CK_DESIGNATION_CATEGORY`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DESIGNATION_CATEGORY_001`: DOCTOR_RELATED IN ('N','Y'
- **CHECK** `CK_DESIGNATION_CATEGORY_002`: ON_CALL IN ('N','Y'
- **CHECK** `CK_DESIGNATION_CATEGORY_1`: CLINICAL IN ('Y', 'N'
- **CHECK** `CK_DESIGNATION_CATEGORY_2`: FINANCIAL IN ('Y', 'N'
- **Triggers**: `DESIGNATION_CATEGORY_CEA` (before insert or update or delete), `DESIGNATION_CATEGORY_DEL` (after delete), `DESIGNATION_CATEGORY_INS` (before insert), `DESIGNATION_CATEGORY_UPD` (before update), `TRG_WS_GIW_AM_QL_Q` (after insert or update or delete)

## DEFINITIONS.CATEGORY_WISE_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |

- **PK** `PK_CATEGORY_WISE_DESIGNATION`: DESIGNATION_CATEGORY_ID, DESIGNATION_ID
- **FK** `FK_CATEGORY_WISE_DESIGNATION_1`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID)
- **FK** `FK_CATEGORY_WISE_DESIGNATION_2`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **Triggers**: `CATEGORY_WISE_DESIGNATION_CEA` (before insert or update or delete), `CATEGORY_WISE_DESIGNATION_DEL` (after delete), `CATEGORY_WISE_DESIGNATION_INS` (before insert), `CATEGORY_WISE_DESIGNATION_UPD` (before update), `TRG_WS_CIQ_HL_FG_Q` (after insert or update or delete)

## DEFINITIONS.CAUTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CAUTION_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SEND_NOTE | VARCHAR2(1) default 'N' | Y | This column contains N by default for precautions for Label and  Y for precautions for Note Entry and |

- **PK** `PK_CAUTION_TYPE`: CAUTION_TYPE_ID
- **Triggers**: `CAUTION_TYPE_CEA` (before insert or update or delete), `CAUTION_TYPE_DEL` (after delete), `CAUTION_TYPE_INS` (before insert), `CAUTION_TYPE_UPD` (before update), `TRG_WS_HNQ_YC_XP_Q` (after insert or update or delete)

## DEFINITIONS.CAUTION_TYPE_OLD_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CAUTION_TYPE_ID | VARCHAR2(5) | Y |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.CC_DESTINATION_TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| DESTINATION_TABLE | VARCHAR2(150) | N |  |

- **PK** `PK_CC_DESTINATION_TABLES`: DESTINATION_TABLE
- **CHECK** `CHK_CC_DESTINATION_TABLES`: DESTINATION_TABLE = UPPER(DESTINATION_TABLE
- **Triggers**: `CC_DESTINATION_TABLES_CEA` (before insert or update or delete), `CC_DESTINATION_TABLES_DEL` (after delete), `CC_DESTINATION_TABLES_INS` (before insert), `CC_DESTINATION_TABLES_UPD` (before update), `TRG_WS_ICT_GM_MA_Q` (after insert or update or delete)

## DEFINITIONS.CC_SOURCE_TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| SOURCE_TABLE | VARCHAR2(150) | N |  |

- **PK** `PK_CC_SOURCE_TABLES`: SOURCE_TABLE
- **CHECK** `CHK_SOURCE_TABLES_1`: SOURCE_TABLE = UPPER(SOURCE_TABLE
- **Triggers**: `CC_SOURCE_TABLES_CEA` (before insert or update or delete), `CC_SOURCE_TABLES_DEL` (after delete), `CC_SOURCE_TABLES_INS` (before insert), `CC_SOURCE_TABLES_UPD` (before update), `TRG_WS_JPQ_AS_HL_Q` (after insert or update or delete)

## DEFINITIONS.CDM_DOMAIN

| Column | Type | Null | Comment |
|---|---|---|---|
| DOMAIN_ID | NUMBER generated always as identity | Y |  |
| DOMAIN_NAME | VARCHAR2(255) | N |  |
| LOV_ID | VARCHAR2(5) | Y |  |

_No standard audit columns._


## DEFINITIONS.CERTIFICATES

| Column | Type | Null | Comment |
|---|---|---|---|
| CERTIFICATE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_CERTIFICATES`: CERTIFICATE_ID
- **Triggers**: `CERTIFICATES_DEL` (after delete), `CERTIFICATES_INS` (before insert), `CERTIFICATES_UPD` (before update)

## DEFINITIONS.CHAMPIONSHIP

| Column | Type | Null | Comment |
|---|---|---|---|
| CHAMPIONSHIP_ID | NUMBER(4) | N |  |
| CHAMPIONSHIP_DES | VARCHAR2(250) | Y |  |
| CS_SHORT_DES | VARCHAR2(10) | Y |  |
| CATEGORY | VARCHAR2(3) | Y | INT is using for International, DOM is using for Domestic |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHAMPIONSHIP`: CHAMPIONSHIP_ID
- **Triggers**: `CHAMPIONSHIP_CEA` (before insert or update or delete), `CHAMPIONSHIP_DEL` (after delete), `CHAMPIONSHIP_INS` (before insert), `CHAMPIONSHIP_UPD` (before update), `TRG_WS_JKK_AO_VJ_Q` (after insert or update or delete)

## DEFINITIONS.CHAMPIONSHIP_DESIGNATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CS_DESIGNATION_ID | NUMBER(4) | N |  |
| DESIGNATION | VARCHAR2(250) | Y |  |
| CS_SHORT_DESIGNATION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHAMPIONSHIP_DESIGNATIONS`: CS_DESIGNATION_ID
- **Triggers**: `CHAMPIONSHIP_DESIGNATIONS_CEA` (before insert or update or delete), `CHAMPIONSHIP_DESIGNATIONS_DEL` (after delete), `CHAMPIONSHIP_DESIGNATIONS_INS` (before insert), `CHAMPIONSHIP_DESIGNATIONS_UPD` (before update), `TRG_WS_QGC_NH_TJ_Q` (after insert or update or delete)

## DEFINITIONS.CHAMPIONSHIP_TEAMS

| Column | Type | Null | Comment |
|---|---|---|---|
| TEAM_ID | NUMBER(4) | N |  |
| TEAM_DES | VARCHAR2(250) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHAMPIONSHIP_TEAMS`: TEAM_ID
- **Triggers**: `CHAMPIONSHIP_TEAMS_CEA` (before insert or update or delete), `CHAMPIONSHIP_TEAMS_DEL` (after delete), `CHAMPIONSHIP_TEAMS_INS` (before insert), `CHAMPIONSHIP_TEAMS_UPD` (before update), `TRG_WS_COC_FY_NX_Q` (after insert or update or delete)

## DEFINITIONS.CHAMPIONSHIP_TROPHY

| Column | Type | Null | Comment |
|---|---|---|---|
| TROPHY_ID | NUMBER(4) | N |  |
| CHAMPIONSHIP_ID | NUMBER(4) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| SESSION_NO | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHAMPIONSHIP_TROPHY`: TROPHY_ID
- **FK** `FK_CHAMPIONSHIP_TROPHY`: (CHAMPIONSHIP_ID) -> DEFINITIONS.CHAMPIONSHIP(CHAMPIONSHIP_ID)
- **Triggers**: `CHAMPIONSHIP_TROPHY_CEA` (before insert or update or delete), `CHAMPIONSHIP_TROPHY_DEL` (after delete), `CHAMPIONSHIP_TROPHY_INS` (before insert), `CHAMPIONSHIP_TROPHY_UPD` (before update), `TRG_WS_NUP_WF_DY_Q` (after insert or update or delete)

## DEFINITIONS.CHAMP_TEAMS_TROPHY

| Column | Type | Null | Comment |
|---|---|---|---|
| TROPHY_ID | NUMBER(4) | N |  |
| TEAM_ID | NUMBER(4) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHAMP_TEAMS_TROPHY`: TROPHY_ID, TEAM_ID
- **Triggers**: `CHAMP_TEAMS_TROPHY_CEA` (before insert or update or delete), `CHAMP_TEAMS_TROPHY_DEL` (after delete), `CHAMP_TEAMS_TROPHY_INS` (before insert), `CHAMP_TEAMS_TROPHY_UPD` (before update), `TRG_WS_XWT_UE_IL_Q` (after insert or update or delete)

## DEFINITIONS.CHANGE_DIAGNOSIS_STATUS_TIME_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CHANGE_DIAGNOSIS_STATUS_TYPE | VARCHAR2(20) | Y |  |
| CHANGE_DIAGNOSIS_STATUS_DAYS | NUMBER(5) | Y |  |


## DEFINITIONS.CHARGES

| Column | Type | Null | Comment |
|---|---|---|---|
| CHARGE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CHARGES`: CHARGE_ID
- **UK** `UK_CHARGES_1`: DESCRIPTION
- **Triggers**: `CHARGES_CEA` (before insert or update or delete), `CHARGES_DEL` (after delete), `CHARGES_INS` (before insert), `CHARGES_UPD` (before update), `TRG_WS_NDB_YK_EC_Q` (after insert or update or delete)

## DEFINITIONS.CHECKING_GLOBAL_VARIABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| SESSION_ID | NUMBER | Y |  |
| OLD_GV_VALUE | VARCHAR2(4000) | Y |  |
| NEW_GV_VALUE | VARCHAR2(4000) | Y |  |
| GV_NAME | VARCHAR2(50) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| OBJECT_NAME | VARCHAR2(100) | Y |  |
| LOGIN_SESSIONID | VARCHAR2(30) | Y |  |
| LOGIN_MRNO | VARCHAR2(14) | Y |  |
| LOGIN_TERMINAL | VARCHAR2(30) | Y |  |
| CHANGED_GV_VALUE | VARCHAR2(4000) | Y |  |


## DEFINITIONS.CHECKLIST

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECKLIST_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CHECKLIST`: CHECKLIST_ID
- **Triggers**: `CHECKLIST_CEA` (before insert or update or delete), `CHECKLIST_DEL` (after delete), `CHECKLIST_INS` (before insert), `CHECKLIST_UPD` (before update), `TRG_WS_VDO_PT_JU_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_ADMIN_CHECKPOINTS
This setup table is created to store the setup data of chemo receiving and verification checkpoints

| Column | Type | Null | Comment |
|---|---|---|---|
| CHECKPOINT_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| CHECKPOINT_TYPE | VARCHAR2(3) | Y |  |
| CHECKPOINT_ANSWER | VARCHAR2(2) | Y | This column is used to store the checkpoint answer value Y - only Y value will be allowed against this checkpoint,   O - value will be Optional for this checkpoint |
| REMARKS_MANDATORY | VARCHAR2(1) default 'N' | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y | This column is used to store the Active value Y - Yes, N - No |

- **PK** `PK_CHECKPOINTS`: CHECKPOINT_ID
- **Triggers**: `CHEMO_ADMIN_CHECKPOINTS_CEA` (before insert or update or delete), `CHEMO_ADMIN_CHECKPOINTS_DEL` (after delete), `CHEMO_ADMIN_CHECKPOINTS_INS` (before insert), `CHEMO_ADMIN_CHECKPOINTS_UPD` (before update), `TRG_WS_VTX_FT_SH_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_BASELINE_TEST_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| TEST_ID | VARCHAR2(7) | N |  |
| PARAMETER_ID | VARCHAR2(9) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DISPLAY_ORDER | NUMBER(3) | Y |  |

- **PK** `PK_CHEMO_BASELINE_TEST_PARAMET`: TEST_ID, PARAMETER_ID
- **Triggers**: `CHEMO_BASELINE_TEST_PARAMETER_CEA` (before insert or update or delete), `TRG_WS_CZO_PF_HM_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_CANCELLATION_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| CANCELLATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHEMO_CANCELLATION_REASON`: CANCELLATION_ID
- **Triggers**: `CHEMO_CANCELLATION_REASON_CEA` (before insert or update or delete), `TRG_WS_JKH_JI_WV_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_DISPENSING_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_CHEMO_DISPENSING_LOCATION`: LOCATION_ID, ORDER_LOCATION_ID
- **Triggers**: `CHEMO_DISPENSING_LOCATION_CEA` (before insert or update or delete), `CHEMO_DISPENSING_LOCATION_DEL` (after delete), `CHEMO_DISPENSING_LOCATION_INS` (before insert), `CHEMO_DISPENSING_LOCATION_UPD` (before update), `TRG_WS_ZWM_EU_IS_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_INTERVENTION_DEC

| Column | Type | Null | Comment |
|---|---|---|---|
| DECISION_ID | VARCHAR2(3) | N | This column is used to keep the chemo intervention decision IDs... |
| DESCRIPTION | VARCHAR2(200) | Y | This column is used to keep the chemo intervention decision IDs descriptions... |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CHEMO_INTERVENTION_DECISION`: DECISION_ID
- **Triggers**: `CHEMO_INTERVENTION_DEC_CEA` (before insert or update or delete), `CHEMO_INTERVENTION_DEC_DEL` (after delete), `CHEMO_INTERVENTION_DEC_INS` (before insert), `CHEMO_INTERVENTION_DEC_UPD` (before update), `TRG_WS_ZMA_RB_EF_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_PRIORITY

| Column | Type | Null | Comment |
|---|---|---|---|
| CHEMO_PRIORITY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PRIORITY_DAYS_START | NUMBER(3) | Y |  |
| PRIORITY_DAYS_FINISH | NUMBER(3) | Y |  |
| ORDER_BY | NUMBER(2) | Y |  |

- **PK** `PK_CHEMO_PRIORITY`: CHEMO_PRIORITY_ID
- **Triggers**: `CHEMO_PRIORITY_CEA` (before insert or update or delete), `TRG_WS_DFL_MT_UI_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CHEMO_REASON_ID | CHAR(5) | N |  |
| DESCRIPTION | VARCHAR2(150) | Y |  |
| REASON_TYPE | VARCHAR2(15) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CHEMO_REASONS`: CHEMO_REASON_ID
- **Triggers**: `CHEMO_REASONS_CEA` (before insert or update or delete), `TRG_WS_QOZ_MS_DK_Q` (after insert or update or delete)

## DEFINITIONS.CHEMO_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| START_AUTO_SCHEDULING_YN | CHAR(1) | Y |  |
| START_AUTO_SCHEDULING_DATE | DATE | Y |  |

- **PK** `PK_CHEMO_SETUP`: ORG_ID, LOC_ID, START_AUTO_SCHEDULING_DATE
- **Triggers**: `CHEMO_SETUP_CEA` (before insert or update or delete), `TRG_WS_LKZ_HT_CT_Q` (after insert or update or delete), `UPD_CHEMO_SETUP_AUTO_SCHEDULE` (after update)

## DEFINITIONS.CHEMO_SMS_SENDING_SETUP
It will be used as setup table for Chemobay SMS sending utility

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| LOCAL_OUTSIDE | VARCHAR2(1) | Y | L-> value is used for local patients, O-> value is user for outside patients. |
| REMAINDER_DURATION | NUMBER | Y |  |
| SMS_ON_APPOINTMENT | VARCHAR2(1) | Y |  |
| EVENT | VARCHAR2(1) | Y | A-> value is used for Appointment Confirmation, C-> value is used for Appointment Cancellation |
| ACTIVE | VARCHAR2(1) | Y |  |
| APPOINTEMENT_TEXT | VARCHAR2(4000) | Y | This column is used for APPOINTEMENT SMS text, P_PATIENT_NAME is used to show Patient Name, P_PATIENT_MRNO is used to show Patient MRNO, P_APPT_DATE is used to show Appointment Date with Time,P_MEDICATION will show Protocol... Please do not change/alter keywords P_PATIENT_NAME, P_PATIENT_MRNO, P_APPT_DATE and P_MEDICATION, otherwise message string can cause error |
| REMINDER_TEXT | VARCHAR2(4000) | Y | This column is used for APPOINTEMENT SMS text, P_PATIENT_NAME is used to show Patient Name, P_PATIENT_MRNO is used to show Patient MRNO, P_APPT_DATE is used to show Appointment Date with Time,P_MEDICATION will show Protocol... Please do not change/alter keywords P_PATIENT_NAME, P_PATIENT_MRNO, P_APPT_DATE and P_MEDICATION, otherwise message string can cause error |
| CANCELLATION_TEXT | VARCHAR2(4000) | Y | This column is used for APPOINTEMENT SMS text, P_PATIENT_NAME is used to show Patient Name, P_PATIENT_MRNO is used to show Patient MRNO, P_APPT_DATE is used to show Appointment Date with Time,P_MEDICATION will show Protocol... Please do not change/alter keywords P_PATIENT_NAME, P_PATIENT_MRNO, P_APPT_DATE and P_MEDICATION, otherwise message string can cause error |

- **PK** `PK_CHEMO_SMS_SENDING_SETUP`: SERIAL_NO
- **UK** `UK_CHEMO_SMS_SENDING_SETUP`: ORG_ID, ZON_ID, LOC_ID, CLINIC_ID, LOCAL_OUTSIDE, EVENT
- **Triggers**: `CHEMO_SMS_SENDING_SETUP_CEA` (before insert or update or delete), `CHEMO_SMS_SENDING_SETUP_DEL` (after delete), `CHEMO_SMS_SENDING_SETUP_INS` (before insert), `CHEMO_SMS_SENDING_SETUP_UPD` (before update), `TRG_WS_EHZ_OG_FA_Q` (after insert or update or delete)

## DEFINITIONS.CITY

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| CITY_ID | NUMBER(4) | N |  |
| CITY_NAME | VARCHAR2(300) | Y |  |
| CALLING_CODE | VARCHAR2(5) | Y |  |

- **PK** `PK_CITY`: COUNTRY_ID, CITY_ID
- **Triggers**: `CITY_DEL` (after delete), `CITY_INS` (before insert), `CITY_UPD` (before update)

## DEFINITIONS.CLASS_OF_CASE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLASS_ID | VARCHAR2(14) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CLASS_ID`: CLASS_ID
- **Triggers**: `CLASS_OF_CASE_DEL` (after delete), `CLASS_OF_CASE_INS` (before insert), `CLASS_OF_CASE_UPD` (before update)

## DEFINITIONS.CLASS_OF_CASE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CLASS_ID | VARCHAR2(14) | N |  |
| CLASS_DETAIL | VARCHAR2(4000) | Y |  |
| HB_REGISTRY | VARCHAR2(500) | Y |  |
| INCLUDE_AS_CA_PATIENT | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CLASS_DETAIL_ID`: CLASS_ID
- **Triggers**: `CLASS_OF_CASE_DETAIL_CEA` (before insert or update or delete), `CLASS_OF_CASE_DETAIL_DEL` (after delete), `CLASS_OF_CASE_DETAIL_INS` (before insert), `CLASS_OF_CASE_DETAIL_UPD` (before update), `TRG_WS_ZZS_RJ_YL_Q` (after insert or update or delete)

## DEFINITIONS.ORGANIZATION

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| DEFAULT_LOCATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MRNO_ALLOWED | CHAR(1) | Y |  |
| SHOW_EMP_PIC | CHAR(1) default 'N' | Y |  |
| SHOW_PENDING_TASKS | CHAR(1) default 'Y' | Y |  |
| ALERT_EXPIRY_DAYS | NUMBER(3) default 0 | Y |  |
| PSWD_EXPIRY_DAYS | NUMBER(3) default 0 | Y |  |
| NO_OF_WRONG_TRIES | NUMBER(3) default 0 | Y |  |
| PATIENT_CNIC_MANDATORY | CHAR(1) default 'N' | Y | Values will be Y or N, Y means CNIC is mandatory at the time of Patient Registeration and N means CNIC is not mandatory |
| DEFAULT_ORG | CHAR(1) default 'N' | N | This column contains flag information to mark an organization as default Y=Yes, N=No |
| SHORT_DESC | VARCHAR2(25) | N | This column contains short descriotion of an organization |
| ORDER_BY | NUMBER(3) | Y | This column contains Display Order of Oraganization List |
| SEND_EMAIL | CHAR(1) default 'Y' | Y | This column contains flag to use email solution |
| EMAIL_DOMAIN | VARCHAR2(50) | Y | Email Domain (or Comma Saperated Domains) |
| COMPLEX_PASSWORD | CHAR(1) default 'N' | Y |  |
| MIN_PASSWORD_LENGTH | NUMBER | Y |  |
| MAX_PASSWORD_LENGTH | NUMBER | Y |  |
| CHECK_PSWRD_HISTORY | CHAR(1) default 'N' | Y | This flage use for checking user password history when user change password |
| CHECK_ALREADY_LOGIN | CHAR(1) default 'N' | Y | This flage use to check user already login to any other system |
| QR_SERVER_PATH | VARCHAR2(400) | Y | This column contains info about qr_server_path |

- **PK** `PK_ORGANIZATION`: ORGANIZATION_ID
- **CHECK** `CK_ORGANIZATION_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_ORGANIZATION_2`: DEFAULT_ORG IN ('Y','N'
- **CHECK** `CK_ORGANIZATION_3`: PATIENT_CNIC_MANDATORY IN ('Y','N'
- **Triggers**: `ORGANIZATION_CEA` (before insert or update or delete), `ORGANIZATION_DEL` (after delete), `ORGANIZATION_INS` (before insert), `ORGANIZATION_UPD` (before update), `TRG_WS_SZZ_XI_WS_Q` (after insert or update or delete)

## DEFINITIONS.GL_CC_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| COST_CENTRE_GROUP_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_GL_CC_GROUPS`: COST_CENTRE_GROUP_CODE
- **CHECK** `CK_GL_CC_GROUPS_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_CC_GROUPS_CEA` (before insert or update or delete), `GL_CC_GROUPS_DEL` (after delete), `GL_CC_GROUPS_INS` (before insert), `GL_CC_GROUPS_UPD` (before update), `TRG_WS_KCE_DC_EI_Q` (after insert or update or delete)

## DEFINITIONS.GL_COST_CENTRES

| Column | Type | Null | Comment |
|---|---|---|---|
| COST_CENTRE_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| COST_CENTRE_GROUP_CODE | CHAR(3) | Y |  |
| COST_CENTRE_TYPE | CHAR(1) default 'C' | Y |  |
| COST_CENTRE_CATEGORY | CHAR(1) default 'O' | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CURRENT_CODE | CHAR(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_GL_COST_CENTRES`: COST_CENTRE_CODE
- **FK** `FK_GL_COST_CENTRES_1`: (COST_CENTRE_GROUP_CODE) -> DEFINITIONS.GL_CC_GROUPS(COST_CENTRE_GROUP_CODE) [disabled]
- **FK** `FK_GL_COST_CENTRES_2`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_GL_COST_CENTRES_3`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **CHECK** `CK_GL_COST_CENTRES_1`: COST_CENTRE_TYPE IN ('C', 'P'
- **CHECK** `CK_GL_COST_CENTRES_2`: COST_CENTRE_CATEGORY IN ('D', 'S', 'O'
- **CHECK** `CK_GL_COST_CENTRES_3`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_COST_CENTRES_CEA` (before insert or update or delete), `GL_COST_CENTRES_DEL` (after delete), `GL_COST_CENTRES_INS` (before insert), `GL_COST_CENTRES_UPD` (before update), `TRG_WS_EVV_IM_GM_Q` (after insert or update or delete)

## DEFINITIONS.GL_DEPARTMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| GROUP_CODE | CHAR(3) | Y |  |
| SERVICE_CODE | CHAR(3) | Y |  |
| AREA | NUMBER(20,2) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CURRENT_CODE | CHAR(3) | Y |  |
| FIN_DEPT_NAME | VARCHAR2(150) | Y |  |
| FIN_DEPT_ORDER | NUMBER(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_GL_DEPARTMENTS`: DEPARTMENT_CODE
- **FK** `FK_GL_DEPARTMENTS`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_GL_DEPARTMENTS_1`: (GROUP_CODE) -> DEFINITIONS.GL_DEPT_GROUPS(GROUP_CODE) [disabled]
- **FK** `FK_GL_DEPARTMENTS_2`: (SERVICE_CODE) -> DEFINITIONS.GL_DEPT_SERVICES(SERVICE_CODE) [disabled]
- **CHECK** `CK_GL_DEPARTMENTS_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DEPARTMENTS_CEA` (before insert or update or delete), `GL_DEPARTMENTS_DEL` (after delete), `GL_DEPARTMENTS_INS` (before insert), `GL_DEPARTMENTS_UPD` (before update), `TRG_WS_NDH_DO_AN_Q` (after insert or update or delete)

## DEFINITIONS.GL_DIVISIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIVISION_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CURRENT_CODE | CHAR(3) | Y |  |
| HEAD_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_GL_DIVISIONS`: DIVISION_CODE
- **CHECK** `CK_GL_DIVISIONS_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DIVISIONS_CEA` (before insert or update or delete), `GL_DIVISIONS_DEL` (after delete), `GL_DIVISIONS_INS` (before insert), `GL_DIVISIONS_UPD` (before update), `TRG_WS_PGF_HW_YW_Q` (after insert or update or delete)

## DEFINITIONS.GL_DIV_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| DIVISION_CODE | CHAR(3) | N |  |
| DEPARTMENT_CODE | CHAR(3) | N |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_GL_DIV_DEPT`: DIVISION_CODE, DEPARTMENT_CODE
- **FK** `FK_GL_DIV_DEPT_1`: (DIVISION_CODE) -> DEFINITIONS.GL_DIVISIONS(DIVISION_CODE)
- **FK** `FK_GL_DIV_DEPT_2`: (DEPARTMENT_CODE) -> DEFINITIONS.GL_DEPARTMENTS(DEPARTMENT_CODE) [disabled]
- **CHECK** `CK_GL_DIV_DEPT_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DIV_DEPT_CEA` (before insert or update or delete), `GL_DIV_DEPT_DEL` (after delete), `GL_DIV_DEPT_INS` (before insert), `GL_DIV_DEPT_UPD` (before update), `TRG_WS_OYJ_ST_HJ_Q` (after insert or update or delete)

## DEFINITIONS.GL_DIV_DEPT_CC

| Column | Type | Null | Comment |
|---|---|---|---|
| COST_CENTRE_ID | CHAR(10) | N |  |
| DIVISION_CODE | CHAR(3) | Y |  |
| DEPARTMENT_CODE | CHAR(3) | Y |  |
| COST_CENTRE_CODE | CHAR(3) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| NEW_COST_CENTRE_ID | VARCHAR2(10) | Y |  |

- **PK** `PK_GL_DIV_DEPT_CC`: COST_CENTRE_ID
- **FK** `FK_GL_DIV_DEPT_CC_1`: (COST_CENTRE_CODE) -> DEFINITIONS.GL_COST_CENTRES(COST_CENTRE_CODE) [disabled]
- **FK** `FK_GL_DIV_DEPT_CC_2`: (DIVISION_CODE, DEPARTMENT_CODE) -> DEFINITIONS.GL_DIV_DEPT(DIVISION_CODE, DEPARTMENT_CODE) [disabled]
- **CHECK** `CK_GL_DIV_DEPT_CC_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DIV_DEPT_CC_CEA` (before insert or update or delete), `GL_DIV_DEPT_CC_DEL` (after delete), `GL_DIV_DEPT_CC_INS` (before insert), `GL_DIV_DEPT_CC_UPD` (before update), `TRG_WS_AKQ_QU_WF_Q` (after insert or update or delete)

## DEFINITIONS.DEPARTMENT_NATURE

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| IS_DEPT_NATURE_CENTRAL | CHAR(1) | Y | This column will be use for mark the department central if this flage = 'Y' |

- **PK** `PK_DEPARTMENT_NATURE`: DEPARTMENT_NATURE_ID
- **UK** `UK_DEPARTMENT_NATURE`: DESCRIPTION
- **Triggers**: `DEPARTMENT_NATURE_CEA` (before insert or update or delete), `DEPARTMENT_NATURE_DEL` (after delete), `DEPARTMENT_NATURE_INS` (before insert), `DEPARTMENT_NATURE_UPD` (before update), `HOD_UPDATE_DIRECTORY` (after update), `TRG_WS_TMU_SZ_IW_Q` (after insert or update or delete)

## DEFINITIONS.DEPARTMENT
This table contains List of departments

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N | This column contains Y/N Status of Activation Y=Yes, N=No |
| STAT_PERCENTAGE | NUMBER(5,2) | Y |  |
| HR_REP_ORDER | NUMBER(3) | Y |  |
| CASH_SUMMARY_AGGREGATE | VARCHAR2(1) default 'N' | Y |  |
| DEPARTMENT_HEAD | VARCHAR2(14) | Y | 'This column contains MRNO of Doctor who is HEAD of Section |
| DEPARTMENT_MANAGER | VARCHAR2(14) | Y |  |
| COST_CENTRE_ID | CHAR(10) | N |  |
| INPATIENT_DESCRIPTION | VARCHAR2(255) | Y |  |
| ORDERBY | NUMBER(2) | Y |  |
| INPATIENT_CODE | VARCHAR2(3) | Y |  |
| ALLOW_LEAVE_ENTRY | CHAR(1) | Y |  |
| REPORTS_DISPLAY_NAME | VARCHAR2(60) | Y |  |
| FIN_DEPT_NAME | VARCHAR2(60) | Y |  |
| FIN_DEPT_ORDER | NUMBER(3) | Y |  |
| DOCTOR_REQUIRED | CHAR(1) | Y |  |
| DIVISION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_EMAIL | VARCHAR2(30) | Y |  |
| BLOCK_DR_VISITS | CHAR(1) default 'N' | Y |  |
| OVERTIME_ALLOWED | CHAR(1) default 'Y' | N |  |
| ALLOW_DRT | CHAR(1) | Y | In order top make DUTY ROSTER TABULAR form access privileges to specified departments only |
| CLINICAL_REPORT | CHAR(1) default 'N' | Y | This column contains Information either This department is generating Reports Y/N Y=Yes, N=No |
| GENERAL_DEPARTMENT | CHAR(1) default 'N' | N | Possible values Y or N. Y means for CPTs with doctor required Y system shall use doctors cost centre/department instead of CPT department Section |
| DEFAULT_DOCTOR | VARCHAR2(18) | Y | Default doctor Specified for this CPT |
| REPORTING_PANEL | CHAR(1) default 'N' | N | This column contains Y/N information of reporting panel Y=Yes, N=No |
| ACCESS_CODE_GEN | CHAR(1) default 'N' | N | If the Value is Y then we will generate the Access code for online reprt viewing for the CPTs of this department other wise NO |
| DEPARTMENT_NAME_INITIAL | VARCHAR2(4) | Y |  |
| ALLOW_NIGHTS | CHAR(1) default 'Y' | Y |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| ALERT_EXPIRY_DAYS | NUMBER(3) default 0 | Y |  |
| PSWD_EXPIRY_DAYS | NUMBER default 0 | Y |  |
| NO_OF_WRONG_TRIES | NUMBER(3) default 0 | Y |  |
| EYE | VARCHAR2(25) | Y |  |
| DENTAL | CHAR(1) default 'N' | Y |  |
| ITEM_TYPE_ID | VARCHAR2(3) | Y | This column will be used to link the Department with the Billing Item Type for Final Invoice and Departmental Share |
| IS_GENERATE_ABSENTIEEISM_QUEUE | VARCHAR2(1) default 'N' | Y |  |
| IS_SERVICES_REQ_AUTH | CHAR(1) default 'N' | N | For Services Expense Request Work Flow, Y=Yes, N=No, This Check Allow Only Authorized Users. |
| CLINICAL_INFORMATION_REQUIRED | VARCHAR2(1) default 'N' | Y | Clinical information required 'Y' mean clinical information is mandatory to Order CPT. |
| PERFORMER_REQUIRED | VARCHAR2(1) default 'N' | Y | Performer Required 'Y' mean performer selection is mandatory to Order CPT. |
| COMPLEX_PASSWORD | CHAR(1) default 'N' | Y |  |
| MIN_PASSWORD_LENGTH | NUMBER | Y |  |
| MAX_PASSWORD_LENGTH | NUMBER | Y |  |
| CHECK_PSWRD_HISTORY | CHAR(1) default 'N' | Y | This flage use for checking user password history when user change password |
| CHECK_ALREADY_LOGIN | CHAR(1) default 'N' | Y | This flage use to check user already login to any other system |
| SERVICES | VARCHAR2(3) | Y |  |
| ADMIN_ALLOWED | VARCHAR2(1) | Y | Y-> Allow to admin OPD online orders at this department(to filter departments on pharmacy order screen (LOV_ADMINSTER_AT)), N -> Donot allow to admin OPD onlice orders at this department. |
| SHOW_ACGME | CHAR(1) default 'N' | Y |  |
| SMS_ON_INVOICE | CHAR(1) default 'N' | N |  |

- **PK** `PK_DEPARTMENT`: DEPARTMENT_ID
- **FK** `FK_DEPARTMENT_03`: (DEPARTMENT_NATURE_ID) -> DEFINITIONS.DEPARTMENT_NATURE(DEPARTMENT_NATURE_ID) [disabled]
- **FK** `FK_DEPARTMENT_1`: (DEPARTMENT_HEAD) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_DEPARTMENT_2`: (COST_CENTRE_ID) -> DEFINITIONS.GL_DIV_DEPT_CC(COST_CENTRE_ID) [disabled]
- **FK** `FK_DEPARTMENT_3`: (DIVISION_ID) -> DEFINITIONS.DIVISIONS(DIVISION_ID) [disabled]
- **FK** `FK_DEPARTMENT_6`: (ITEM_TYPE_ID) -> BILLING.ITEM_TYPE(ITEM_TYPE_ID)
- **CHECK** `CK_DEPARTMENT_001`: OVERTIME_ALLOWED IN ('N','Y'
- **CHECK** `CK_DEPARTMENT_1`: CASH_SUMMARY_AGGREGATE IN ('Y', 'N'
- **CHECK** `CK_DEPARTMENT_2`: DOCTOR_REQUIRED IN ('Y', 'N'
- **CHECK** `CK_DEPARTMENT_3`: GENERAL_DEPARTMENT IN ('N','Y'
- **CHECK** `CK_DEPARTMENT_4`: REPORTING_PANEL IN ('Y', 'N'
- **CHECK** `CK_DEPARTMENT_5`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DEPARTMENT_6`: CLINICAL_REPORT IN ('Y', 'N'
- **Triggers**: `DEPARTMENT_CEA` (before insert or update or delete), `DEPARTMENT_DEL` (after delete), `DEPARTMENT_INS` (before insert), `DEPARTMENT_TS` (before insert or update or delete), `DEPARTMENT_UPD` (before update), `TRG_WS_OHM_PX_HD_Q` (after insert or update or delete)

## DEFINITIONS.GL_DEPT_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_GL_DEPT_GROUPS`: GROUP_CODE
- **CHECK** `CK_GL_DEPT_GROUPS_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DEPT_GROUPS_CEA` (before insert or update or delete), `GL_DEPT_GROUPS_DEL` (after delete), `GL_DEPT_GROUPS_INS` (before insert), `GL_DEPT_GROUPS_UPD` (before update), `TRG_WS_XBK_YI_FI_Q` (after insert or update or delete)

## DEFINITIONS.GL_DEPT_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_CODE | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SHORT_DESCRPTION | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_GL_DEPT_SERVICES`: SERVICE_CODE
- **CHECK** `CK_GL_DEPT_SERVICES_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DEPT_SERVICES_CEA` (before insert or update or delete), `GL_DEPT_SERVICES_DEL` (after delete), `GL_DEPT_SERVICES_INS` (before insert), `GL_DEPT_SERVICES_UPD` (before update), `TRG_WS_PRZ_OF_RD_Q` (after insert or update or delete)

## DEFINITIONS.SPECIALITY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIALITY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| COST_CENTRE_ID | CHAR(10) | N |  |
| ADMISSION_ALLOWED | CHAR(1) default 'N' | N |  |
| BG_COLOR | VARCHAR2(20) | Y |  |
| CNOAT_SUPPORT | VARCHAR2(1) | Y |  |

- **PK** `PK_SPECIALITY_MASTER`: SPECIALITY_ID
- **UK** `UK_SPECIALITY_MASTER_1`: DESCRIPTION
- **FK** `FK_SPECIALITY_MASTER_1`: (COST_CENTRE_ID) -> DEFINITIONS.GL_DIV_DEPT_CC(COST_CENTRE_ID) [disabled]
- **CHECK** `CK_SPECIALITY_MASTER_1`: ACTIVE IN ('N','Y'
- **Triggers**: `SPECIALITY_MASTER_CEA` (before insert or update or delete), `SPECIALITY_MASTER_DEL` (after delete), `SPECIALITY_MASTER_INS` (before insert), `SPECIALITY_MASTER_UPD` (before update), `TRG_WS_COA_EA_GJ_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_SPECIALITY

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | N |  |
| DOCTOR_SPECIALITY_FLAG | CHAR(1) default 'N' | N |  |
| SHORT_DESC | VARCHAR2(15) | Y |  |
| BLOCK_DR_VISITS | CHAR(1) default 'N' | Y |  |
| SUPPORTABLE | CHAR(1) default 'N' | Y |  |
| ADMISSION_ALLOWED | CHAR(1) default 'Y' | Y |  |
| CHECK_ROSTER | CHAR(1) default 'N' | Y | Y mean need to check oncall roster before sending consult |
| FELLOW_ALLOWED_CONSULTS | CHAR(1) default 'N' | Y |  |
| BG_COLOR | VARCHAR2(20) default 'Black' | Y |  |
| DELAY_ADMISSION | VARCHAR2(1) default 'N' | N |  |
| AUTO_CONSULT | VARCHAR2(1) default 'N' | Y | Y mean auto consult will be sent to specialty through job |
| CHECK_ADDITIONAL_POLICY | VARCHAR2(1) default 'N' | Y | Y-> SYSTEM WILL IMPLEMENT ADDITIONAL POLICY ON PHYSICIAN NOTES ENTRY I.E. MARKED AS PROTECTED NOTE CLINIC SPECIALITY WISE,  N-> NO CHANGE IN THIS CASE |
| SEND_CONSULT_EMAIL | VARCHAR2(1) default 'C' | Y | C => Consultant, S=>Specialty, F=> Consultant and Fellow, E=> Specialty and Fellow, N=> Not send |
| CNOAT_SUPPORT | VARCHAR2(1) | Y |  |
| BRIEF_NOTE_ALLOW | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CLINIC_SPECIALITY`: CLINIC_SPECIALITY_ID
- **FK** `FK_CLINIC_SPECIALITY_01`: (SPECIALITY_ID) -> DEFINITIONS.SPECIALITY_MASTER(SPECIALITY_ID) [disabled]
- **CHECK** `CK_CLINIC_SPECIALITY_1`: DOCTOR_SPECIALITY_FLAG IN ('N','Y'
- **CHECK** `CK_CLINIC_SPECIALITY_2`: "ADMISSION_ALLOWED"='Y' OR "ADMISSION_ALLOWED"='N'
- **Triggers**: `CLINIC_SPECIALITY_CEA` (before insert or update or delete), `CLINIC_SPECIALITY_DEL` (after delete), `CLINIC_SPECIALITY_INS` (before insert), `CLINIC_SPECIALITY_TS` (before insert or update or delete), `CLINIC_SPECIALITY_UPD` (before update), `TRG_WS_ITF_HD_RH_Q` (after insert or update or delete)

## DEFINITIONS.CPT_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CATEGORY_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| PRICE | NUMBER(12,2) default 0 | N |  |
| ACTIVE | VARCHAR2(1) | N |  |
| ACTIVATION_DATE | DATE | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_CPT_CATEGORY`: CPT_CATEGORY_ID
- **FK** `FK_CPT_CATEGORY_01`: (CLINIC_SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID) [disabled]
- **CHECK** `CHK_CPT_CATEGORY_01`: ACTIVE IN ('Y','N'
- **Triggers**: `CPT_CATEGORY_CEA` (before insert or update or delete), `CPT_CATEGORY_DEL` (after delete), `CPT_CATEGORY_INS` (before insert), `CPT_CATEGORY_UPD` (before update), `TRG_WS_QIR_CT_OU_Q` (after insert or update or delete)

## DEFINITIONS.DEPARTMENT_NATURE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| NATURE_ID | VARCHAR2(3) | N | This column contains inforamation department Nature ID (reference: DEFINITIONS.DEPARTMENT_NATURE) |
| NATURE_DETAIL_ID | VARCHAR2(3) | N | This column contains Detail ID of department Nature ID (Unique Nature+Serial) |
| NATURE_DETAIL_DESC | VARCHAR2(255) | N | This column contains description of Nature detail |
| ORDER_BY | NUMBER(3) | Y | This column contains order by sequence to display list of nature details |
| ACTIVE | CHAR(1) default 'Y' | Y | Flag Information to contain status of active (Y=Active, N=Inactive) |
| DEFAULT_ID | CHAR(1) default 'N' | Y | Flag Information to mark default bature details ID for any department nature |

- **PK** `PK_DEPARTMENT_NATURE_DETAIL`: NATURE_ID, NATURE_DETAIL_ID
- **FK** `FK_DEPARTMENT_NATURE_DETAIL_1`: (NATURE_ID) -> DEFINITIONS.DEPARTMENT_NATURE(DEPARTMENT_NATURE_ID)
- **Triggers**: `DEPARTMENT_NATURE_DETAIL_CEA` (before insert or update or delete), `DEPARTMENT_NATURE_DETAIL_DEL` (after delete), `DEPARTMENT_NATURE_DETAIL_INS` (before insert), `DEPARTMENT_NATURE_DETAIL_UPD` (before update), `TRG_WS_ZDP_AH_WJ_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_STATUS_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_GROUP_ID | VARCHAR2(2) | N | Unique Status group ID |
| STATUS_GROUP_DESC | VARCHAR2(50) | Y | Status group Description |

- **PK** `PK_ORDER_STATUS_GROUP`: STATUS_GROUP_ID
- **Triggers**: `ORDER_STATUS_GROUP_CEA` (before insert or update or delete), `ORDER_STATUS_GROUP_DEL` (after delete), `ORDER_STATUS_GROUP_INS` (before insert), `ORDER_STATUS_GROUP_UPD` (before update), `TRG_WS_WDP_EV_TE_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| ORDER_STATUS_ID | VARCHAR2(3) | N | Unique Status ID |
| DESCRIPTION | VARCHAR2(60) | N | This column contains status Description |
| SPECIAL_DESC | VARCHAR2(60) | Y | This column contains Special description of order to display |
| STATUS_GROUP_ID | VARCHAR2(2) default '00' | N | This column is used to group different status into similar group |
| ACTIVE | CHAR(1) | N | Flag Information Y=Active, N=Inactive |

- **PK** `PK_ORDER_STATUS`: ORDER_STATUS_ID
- **FK** `FK_ORDER_STATUS_1`: (STATUS_GROUP_ID) -> DEFINITIONS.ORDER_STATUS_GROUP(STATUS_GROUP_ID) [disabled]
- **Triggers**: `ORDER_STATUS_CEA` (before insert or update or delete), `ORDER_STATUS_DEL` (after delete), `ORDER_STATUS_INS` (before insert), `ORDER_STATUS_UPD` (before update), `TRG_WS_MHJ_FS_KC_Q` (after insert or update or delete)

## DEFINITIONS.PATHOLOGY_COMMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PATHOLOGY_COMMENT_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PATHOLOGY_COMMENT_TYPE`: PATHOLOGY_COMMENT_TYPE_ID
- **Triggers**: `PATHOLOGY_COMMENT_TYPE_CEA` (before insert or update or delete), `PATHOLOGY_COMMENT_TYPE_DEL` (after delete), `PATHOLOGY_COMMENT_TYPE_INS` (before insert), `PATHOLOGY_COMMENT_TYPE_UPD` (before update), `TRG_WS_URB_UE_HX_Q` (after insert or update or delete)

## DEFINITIONS.PAT_REPORT_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| PAT_REPORT_CATEGORY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PAT_REPORT_CATEGORY`: PAT_REPORT_CATEGORY_ID
- **Triggers**: `PAT_REPORT_CATEGORY_CEA` (before insert or update or delete), `PAT_REPORT_CATEGORY_DEL` (after delete), `PAT_REPORT_CATEGORY_INS` (before insert), `PAT_REPORT_CATEGORY_UPD` (before update), `TRG_WS_QOH_XO_YD_Q` (after insert or update or delete)

## DEFINITIONS.CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| CPT_TYPE | VARCHAR2(1) | N | M Manual, A Performed on Machine or Automatic, U undefined |
| PRICE | NUMBER(12,2) | N |  |
| CPT_BONUS | VARCHAR2(1) | Y |  |
| EMPLOYEE_ENTITLEMENT | VARCHAR2(1) | Y |  |
| IN_HOUSE_PERFORMED | VARCHAR2(1) | Y |  |
| COST | NUMBER(12,2) | Y |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| CONSULTANCY | VARCHAR2(1) | Y |  |
| STAT_CHARGEABLE | VARCHAR2(1) default 'N' | N |  |
| CLEARANCE | VARCHAR2(1) default 'N' | N |  |
| MOST_COMMONLY_USED | VARCHAR2(1) default 'N' | N |  |
| NO_OF_PROCEDURES | NUMBER(2) default 1 | N |  |
| REP_ORDER | NUMBER(10) | Y |  |
| PAT_REPORT_CATEGORY_ID | VARCHAR2(3) | Y |  |
| DOCTOR_REQUIRED | VARCHAR2(1) default 'N' | N |  |
| PATHOLOGY_COMMENT_TYPE_ID | VARCHAR2(3) | Y |  |
| MAX_QUANTITY_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| REPORTING_CASE | NUMBER(2) | Y |  |
| NO_OF_REPORTS | NUMBER(2) | Y |  |
| DUPLICATE_ACKNOWLEDGE | VARCHAR2(1) default 'Y' | N |  |
| SPECIMEN_NATURE_REQUIRED | CHAR(1) default 'N' | N |  |
| SPECIMEN_SITE_REQUIRED | CHAR(1) default 'N' | N |  |
| WORK_ORDER_PRINT | CHAR(1) default 'Y' | Y |  |
| TECH_NORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Technologist reporting authority for Normal Result |
| TECH_ABNORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Technologist reporting authority for Abnormal Result |
| DOCTOR_NORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Doctor reporting authority for Normal Result |
| DOCTOR_ABNORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Doctor reporting authority for Abnormal Result |
| CONSULTANT_NORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Consultant reporting authority for Normal Result |
| NOT_REPORTABLE | CHAR(1) default 'N' | Y | Possible Values 'Y', 'N'  'Y' will mean that this CPT will be considered performed, when the invoice is made as so far no report is written by any doctor against this CPT.   Practice Income Calculation call will be made at the time of invoice. This column and PI_CONSIDERATION values should be considered collectively while making practice income calls. |
| CONSULTANT_ABNORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N for Consultant reporting authority for Abnormal Result |
| COMBINED_REPORT | CHAR(1) default 'N' | N |  |
| REPORT_HEADING | VARCHAR2(100) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| SURGERY_REGION_ID | VARCHAR2(5) | Y |  |
| LENGTH_OF_STAY | NUMBER(2) default 0 | Y |  |
| AFTER_DEATH_ENTRY | CHAR(1) | Y |  |
| OPEN_PRICE | CHAR(1) default 'N' | N |  |
| PERFORM_LOCATION_ID | VARCHAR2(3) default '001' | Y |  |
| MODALITY_ID | VARCHAR2(10) | Y |  |
| ACK_PERFORMANCE_REQ | CHAR(1) default 'Y' | N |  |
| IMAGE_REQUIRED | VARCHAR2(1) default 'N' | N |  |
| SHARE_ON_PERFORM | CHAR(1) | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| ACTIVATED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| USER_DEFINED_DEPT | CHAR(1) default 'N' | N | This is Added to Hold that if the cpt will be having to specific dept but the cpt dept will be entered by user at runtime. ( Courier Charges) |
| COMBINED_REPORT_NORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N to enforce Verification Steps by All Persons for Normal Result |
| COMBINED_REPORT_ABNORMAL | CHAR(1) default 'N' | N | This column conatins flag Y/N to enforce Verification Steps by All Persons for Abnormal Result |
| BLOCK_AUTO_INP_INVOICE | CHAR(1) default 'Y' | N | N mean system allow to make invoice at ordering time, Y mean system allow to do order only for this procedure |
| PRE_REQUISITES_CHK | CHAR(1) | Y | Y means we have checked the basic requirement before the cpt is activated , N means we havnt. |
| INITIALIZED_YN | CHAR(1) default 'N' | Y | Value 'Y' shows that CPT has been finalized from Finance department. Value 'N' shows that surgeon/consultant has changed package ID but CPT is yet to be finalized by finance dept. |
| CPT_CATEGORY_ID_NEW | VARCHAR2(7) | Y | New category ID entered\proposed by surgeon/consultant, but not finalized by Finance Dept. |
| INITIALIZED_DATE | DATE | Y | Long description of the CPT. |
| LONG_DESC | VARCHAR2(4000) | Y | Long description of the CPT. |
| DEFAULT_DOCTOR | VARCHAR2(18) | Y | Default doctor Specified for this CPT |
| CONSENT_TYPE | CHAR(1) default 'N' | Y |  |
| LIMITED_IMAGES | CHAR(1) default 'Y' | N | 'Y' means 5mm and 10mm slices are generated by machine |
| PI_CONSIDERATION | CHAR(1) default 'P' | Y | The practice income calculation critrea:  P for on Performance in HIS,   N for at the entry of Notes,  I at the Time of invioce |
| CONSULTANT_ONLY | CHAR(1) default 'N' | N |  |
| LAST_ORDER_VALUE_INHOUR | NUMBER(5) default 0 | N |  |
| NO_OF_IMAGES | NUMBER(3) default 0 | Y | Save minimum number of images required for specified procedure |
| ORDER_RESTRICTION | CHAR(1) default 'Y' | N | Y: Means that CPT can be ordered by through special approval by the User from MD. N Means the CPT will be ordered after checking the user role. (Reference: Credentials system) |
| EAR_ALLOWED | CHAR(1) | Y | 'Y' CPT allowed in Emergency Assessment room |
| CLINICAL_REPORT | CHAR(1) default 'N' | N | This column contains Information either diagnostic report is being generated Y/N |
| CONTRAST | CHAR(1) default 'N' | N | Flag M/O/N to enforce 'M=Mandatory , O = Optional , N= No' |
| MANUAL_PERFROMACE | CHAR(1) | Y | 'Y' means specified CPT has not defined performance work flow in system |
| ASSESSMENT_REQUIRED | CHAR(1) default 'Y' | N | This Column was added for the Invoices of the WIC, In WIC we shall provide the support to the patient but we shall not check the assessment, if Values of this shall be N then We shall not check the Assessment/Support Matrix etc. and provide the support according to the contract attached (Donation Contract) with the patient, We shall make the support decision according to the Support column of Contract |
| FORMAT_ID | VARCHAR2(6) | Y | This column is used to mark Reporting format |
| OPEN_QUANTITY | CHAR(1) default 'N' | N | This column is used to edit quantity at order level |
| INCLUDE_IN_CONTRACT_BY_DEFAULT | CHAR(1) default 'Y' | N | Values of this column must be Y or N, If value is 'N' then this CPT will not be considered as Part of the Contract in Default, however If Values is 'Y'  then CPT will be considered as part of the contract but Invoice will be generated according the Contract |
| NATURE_ID | VARCHAR2(3) | N | This column contains CPT clinical Nature ID (e.g. 096=Lab,029=Radiology,030=Nuclear Medicine,055=Endoscopy etc) |
| DEPARTMENT_NATURE_ID | as ("NATURE_ID"\|\|'') | Y | Virtual column i.e. contains same value NATURE_ID |
| NATURE_DETAIL_ID | VARCHAR2(3) | N | This column contains CPT clinical Nature detail ID (e.g. 096.002=HEM, 096.001=ACM, 029.001=MRI etc) |
| INVOICE_STATUS_ID | VARCHAR2(3) default '002' | N | This column will be used to save the Order Status Id which invoice procedure will update in orderentry.order_cpt.order_status_id , Value of this table may be any from base table (orderentry.order_status), however in routine for Reportable CPTs status will be '002' and for not reportable status will be '015' |
| ITEM_TYPE_ID | VARCHAR2(3) | Y | This column will be used to link the CPT Id. with the Billing Item Type for Billing Final Invoice and Departmenal Share |
| SKM_CPT_DESCRIPTION | VARCHAR2(250) | Y | This column contains  SKM  CPT Description in case of  client changes description  as per his/her demand |
| ALLOW_USER | CHAR(1) default 'N' | Y | Values of this column is Y or N,N means user is not authorized to verify CPT |
| CONSENT_EVENT_ID | NUMBER(3) | Y | Consent required before this event |
| CONSENT_VALIDITY_DAYS | NUMBER(3) | Y | Consent validity in no. of days |
| EMR_RESTRICTED | VARCHAR2(1) default 'N' | Y | it will be used to mark CPT EMR Restricted or not. |
| DURATION_RESTRICTED | CHAR(1) default 'N' | Y | Use for duration restricted authorization |
| STAT_ALLOW | CHAR(1) default 'N' | Y | Values of this column must be Y or N, Y for Allow Stat N for not |
| PATIENT_TYPE_RESTRICTION | VARCHAR2(1) default 'N' | Y | Use for Patient type Restrictions |
| MULTIPLE_QTY_ALLOWED | CHAR(1) default 'N' | Y | This column will used to made decision about multiple cpt qty allowed at IPD service procedure form |
| CONSENT_FORM_NAME | VARCHAR2(3) | Y |  |
| SITE_MARKING_REQUIRED | VARCHAR2(1) default 'N' | Y | This column will contain the value Y/N. Operators will have to document if there is a need for site marking or not. In case there is a CPT where site marking is possibly needed, system will prompt if N/A is marked against the question on site marking asking the operator to document a reason for that. |
| PREGNANCY_SCREENING_REQUIRED | VARCHAR2(1) default 'N' | Y | This column will contain the value Y/N. Y for required pregnancy screening before scan performance. |
| CPT_ABBREVIATION | VARCHAR2(10) | Y | This column will contain the value of CPT abbreviation |
| HIDE_WORK_ORDER | CHAR(1) | Y | This column will contain Flag Y . If Y then CPT will not show on work order. |
| IS_CNOAT | CHAR(1) default 'N' | Y |  |

- **PK** `PK_CPT_1`: CPT_ID
- **UK** `UK_CPT_ABBREVIATION`: CPT_ABBREVIATION
- **FK** `FK_CPT_06`: (NATURE_ID, NATURE_DETAIL_ID) -> DEFINITIONS.DEPARTMENT_NATURE_DETAIL(NATURE_ID, NATURE_DETAIL_ID) [disabled]
- **FK** `FK_CPT_1`: (INVOICE_STATUS_ID) -> DEFINITIONS.ORDER_STATUS(ORDER_STATUS_ID) [disabled]
- **FK** `FK_CPT_2`: (PAT_REPORT_CATEGORY_ID) -> DEFINITIONS.PAT_REPORT_CATEGORY(PAT_REPORT_CATEGORY_ID)
- **FK** `FK_CPT_3`: (PATHOLOGY_COMMENT_TYPE_ID) -> DEFINITIONS.PATHOLOGY_COMMENT_TYPE(PATHOLOGY_COMMENT_TYPE_ID)
- **FK** `FK_CPT_5`: (MODALITY_ID) -> RADIOLOGY.MODALITY(MODALITY_ID) [disabled]
- **FK** `FK_CPT_6`: (ITEM_TYPE_ID) -> BILLING.ITEM_TYPE(ITEM_TYPE_ID)
- **FK** `FK_S01_T009_S01_T100_1`: (CPT_CATEGORY_ID) -> DEFINITIONS.CPT_CATEGORY(CPT_CATEGORY_ID)
- **CHECK** `CHK_CPT_IMAGE_REQUIRED`: IMAGE_REQUIRED IN ('N','Y'
- **CHECK** `CH_CPT_17`: CPT_TYPE IN ('A','M','U'
- **CHECK** `CK_CPT_001`: MAX_QUANTITY_ALLOWED IN ('Y','N'
- **CHECK** `CK_CPT_002`: ACK_PERFORMANCE_REQ IN ('Y','N'
- **CHECK** `CK_CPT_025`: INVOICE_STATUS_ID IN ('002','015'
- **CHECK** `CK_CPT_1`: NO_OF_PROCEDURES>=1
- **CHECK** `CK_CPT_10`: CONSULTANT_NORMAL IN ('Y','N'
- **CHECK** `CK_CPT_11`: NOT_REPORTABLE IN ('Y', 'N'
- **CHECK** `CK_CPT_12`: COMBINED_REPORT IN ('', 'N'
- **CHECK** `CK_CPT_13`: OPEN_PRICE IN ('Y', 'N'
- **CHECK** `CK_CPT_14`: CONSULTANT_ABNORMAL IN ('Y', 'N'
- **CHECK** `CK_CPT_15`: COMBINED_REPORT_NORMAL IN ('Y', 'N'
- **CHECK** `CK_CPT_16`: COMBINED_REPORT_ABNORMAL IN ('Y', 'N'
- **CHECK** `CK_CPT_18`: USER_DEFINED_DEPT IN ('Y','N'
- **CHECK** `CK_CPT_19`: BLOCK_AUTO_INP_INVOICE IN('Y','N'
- **CHECK** `CK_CPT_2`: INSTR(NO_OF_PROCEDURES,'.')=0
- **CHECK** `CK_CPT_20`: CONSENT_TYPE IN ('V','W','N'
- **CHECK** `CK_CPT_21`: LIMITED_IMAGES IN ('Y','N'
- **CHECK** `CK_CPT_22`: CONSULTANT_ONLY IN ('Y','N'
- **CHECK** `CK_CPT_23`: CONTRAST IN ('M','O','N'
- **CHECK** `CK_CPT_24`: INCLUDE_IN_CONTRACT_BY_DEFAULT IN ('Y','N'
- **CHECK** `CK_CPT_3`: SPECIMEN_NATURE_REQUIRED IN ('Y', 'N'
- **CHECK** `CK_CPT_4`: SPECIMEN_SITE_REQUIRED IN ('Y', 'N'
- **CHECK** `CK_CPT_5`: WORK_ORDER_PRINT IN ('Y', 'N'
- **CHECK** `CK_CPT_6`: TECH_NORMAL IN ('Y','N'
- **CHECK** `CK_CPT_7`: TECH_ABNORMAL IN ('Y','N'
- **CHECK** `CK_CPT_8`: DOCTOR_NORMAL IN ('Y','N'
- **CHECK** `CK_CPT_9`: DOCTOR_ABNORMAL IN ('Y','N'
- **CHECK** `NN_CPT_1`: NOT_REPORTABLE IS NOT NULL
- **CHECK** `NN_CPT_2`: WORK_ORDER_PRINT IS NOT NULL)
- **Triggers**: `BEFORE_CPT_PRICE_UPD` (before update), `CPT_CEA` (before insert or update or delete), `CPT_DEL` (after delete), `CPT_INS` (before insert), `CPT_PRICE_HISTORY_INS` (after insert), `CPT_TS` (before insert or update or delete), `CPT_UPD` (before update), `TRG_WS_QXK_QJ_RH_Q` (after insert or update or delete)

## DEFINITIONS.CLIENT_CPT_PRICE
This table will be used to define the CPT Client Wise

| Column | Type | Null | Comment |
|---|---|---|---|
| CLIENT_ID | VARCHAR2(10) | N | client Ref |
| CPT_ID | VARCHAR2(18) | N | CPT For which below Price will be charged |
| PRICE | NUMBER(12,2) | N | Amount which will be charged against this Item |

- **PK** `PK_CLIENT_CPT_PRICE`: CLIENT_ID, CPT_ID
- **FK** `FK_CLIENT_CPT_PRICE_1`: (CLIENT_ID) -> BILLING.CLIENT(CLIENT_ID)
- **FK** `FK_CLIENT_CPT_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_CLIENT_CPT_PRICE_1`: PRICE>0
- **Triggers**: `CLIENT_CPT_PRICE_DEL` (after delete), `CLIENT_CPT_PRICE_INS` (before insert), `CLIENT_CPT_PRICE_UPD` (before update)

## DEFINITIONS.CLIENT_EXCEL_REPORT_TASK

| Column | Type | Null | Comment |
|---|---|---|---|
| TASK_ID | NUMBER | N |  |
| CLIENTID | VARCHAR2(100) | N |  |
| CLIENT_MRNO | VARCHAR2(14) | Y |  |
| PREVIOUS_RUN_TIME | DATE | N |  |
| NEXT_RUN_TIME | DATE | N |  |
| APPLICATION_ID | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| PDF_PATH | VARCHAR2(300) | N |  |
| EMAIL_TO | VARCHAR2(700) | N |  |
| EMAIL_CC | VARCHAR2(700) | Y |  |
| CLIENT_NAME | VARCHAR2(100) | N |  |
| EMAIL_BCC | VARCHAR2(700) | Y |  |
| REPORT_DURATION_INTERVAL | NUMBER default 6 | N | Specify Hourly Report Duration Interval for client |

- **PK** `CLIENT_EXCEL_REPORT_TASK_PK`: CLIENTID, TASK_ID
- **Triggers**: `CLIENT_EXCEL_REPORT_TASK_DEL` (after delete), `CLIENT_EXCEL_REPORT_TASK_INS` (before insert), `CLIENT_EXCEL_REPORT_TASK_UPD` (before update)

## DEFINITIONS.CLINICAL_PATHWAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| CP_ID | NUMBER(5) | N |  |
| CP_DESC | VARCHAR2(500) | N |  |
| CP_ENTERED_BY | VARCHAR2(14) | Y |  |
| CP_DATE | DATE | Y |  |
| CP_ACTIVE | CHAR(1) | Y |  |
| CP_TITLE | VARCHAR2(500) | N |  |
| CP_ELIGIBILITY_LABEL | VARCHAR2(200) | Y |  |
| CP_ELIGIBILITY_TEXT | VARCHAR2(500) | Y |  |
| CONSULTANT | CHAR(1) default 'N' | Y |  |
| FELLOW | CHAR(1) default 'N' | Y |  |
| RESIDENT | CHAR(1) default 'N' | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| MAIN_FLOW_ID | NUMBER(3) | Y |  |
| WORK_FLOW_ID | NUMBER(4) | Y |  |
| OCCURRENCE | NUMBER | Y |  |
| EVENT_ID | NUMBER(3) | Y |  |
| FORMULA | VARCHAR2(4000) | Y |  |
| EMAIL | CHAR(1) default 'N' | Y |  |
| NOTES | CHAR(1) default 'N' | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `CLINICAL_PATHWAY_PK`: CP_ID, LOC_ID
- **Triggers**: `CLINICAL_PATHWAYS_CEA` (before insert or update or delete), `CLINICAL_PATHWAYS_DEL` (after delete), `CLINICAL_PATHWAYS_INS` (before insert), `CLINICAL_PATHWAYS_INSERT` (before insert), `CLINICAL_PATHWAYS_UPD` (before update), `TRG_WS_QBI_RU_CG_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_PATHWAY_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPA_ID | NUMBER(5) | N |  |
| CP_ID | NUMBER(5) | Y |  |
| CPA_DESC | VARCHAR2(500) | N |  |
| CPA_DATE | DATE | Y |  |
| CPA_ENTERED_BY | VARCHAR2(14) | Y |  |
| CPA_ACTIVE | CHAR(1) | Y |  |
| CPA_EVENT | VARCHAR2(100) | N |  |

- **PK** `CPA_PK`: CPA_ID, LOC_ID
- **FK** `CPA_FK`: (CP_ID, LOC_ID) -> DEFINITIONS.CLINICAL_PATHWAYS(CP_ID, LOC_ID) [disabled]
- **Triggers**: `CLINICAL_PATHWAY_ALERTS_CEA` (before insert or update or delete), `CLINICAL_PATHWAY_ALERTS_DEL` (after delete), `CLINICAL_PATHWAY_ALERTS_INS` (before insert), `CLINICAL_PATHWAY_ALERTS_INSERT` (before insert), `CLINICAL_PATHWAY_ALERTS_UPD` (before update), `TRG_WS_UTM_UL_OZ_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_PATHWAY_ANSWERS

| Column | Type | Null | Comment |
|---|---|---|---|
| CP_ID | NUMBER | N |  |
| CPA_ID | VARCHAR2(9) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_CPA`: CPA_ID, CP_ID
- **Triggers**: `CLINICAL_PATHWAY_ANSWERS_CEA` (before insert or update or delete), `CLINICAL_PATHWAY_ANSWERS_DEL` (after delete), `CLINICAL_PATHWAY_ANSWERS_INS` (before insert), `CLINICAL_PATHWAY_ANSWERS_UPD` (before update), `TRG_WS_VWZ_JR_NL_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_PATHWAY_CONDITIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPC_ID | NUMBER(5) | N |  |
| CP_ID | NUMBER(5) | N |  |
| TEST_ID | VARCHAR2(7) | Y |  |
| TEST_VALUES | VARCHAR2(500) | N |  |
| CPC_DATE | DATE | Y |  |
| CPC_ENTERED_BY | VARCHAR2(14) | Y |  |
| CPC_ACTIVE | CHAR(1) | Y |  |
| DURATION | NUMBER(5) | N | Duration will be wrote in hours only |
| PARAMETER_ID | VARCHAR2(9) | Y |  |
| REFERENCE_TABLE | VARCHAR2(100) | Y |  |
| ADD_CONDITION | CHAR(1) | Y |  |
| TYPE | CHAR(1) | Y | V for vitals and L for labs |
| VS_ID | VARCHAR2(30) | Y |  |
| CONDITIONAL_OPERATOR | VARCHAR2(50) | Y |  |
| COMPARISON_OPERATOR | VARCHAR2(100) | Y |  |
| MAX_VALUE | NUMBER(9,4) | Y |  |
| MIN_VALUE | NUMBER(9,4) | Y |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| QUERY_STATEMENT | CLOB | Y |  |

- **PK** `CPC_PK`: CPC_ID, CP_ID, LOC_ID
- **FK** `CPC_FK`: (CP_ID, LOC_ID) -> DEFINITIONS.CLINICAL_PATHWAYS(CP_ID, LOC_ID) [disabled]
- **Triggers**: `CLINICAL_PATHWAY_CONDITIONS_CEA` (before insert or update or delete), `CLINICAL_PATHWAY_COND_INSERT` (before insert), `CLINIC_PATHWAY_CON_DEL` (after delete), `CLINIC_PATHWAY_CON_INS` (before insert), `CLINIC_PATHWAY_CON_UPD` (before update), `TRG_WS_SLC_CU_NT_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_PATHWAY_QUESTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CP_ID | NUMBER(5) | N |  |
| CPQ_ID | VARCHAR2(9) | N |  |
| PARENT_CPQ_ID | VARCHAR2(9) | Y |  |
| PARENT_CPA_ID | VARCHAR2(9) | Y |  |
| CPC_ID | VARCHAR2(9) | Y |  |
| CPQ_DETAILS | VARCHAR2(4000) | Y |  |
| CPQ_NOTES | VARCHAR2(1) default 'Y' | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |

- **PK** `PK_CPQ`: CP_ID, CPQ_ID
- **Triggers**: `CLINICAL_PATHWAY_QUESTIONS_CEA` (before insert or update or delete), `CLINICAL_PATHWAY_QUESTIONS_DEL` (after delete), `CLINICAL_PATHWAY_QUESTIONS_INS` (before insert), `CLINICAL_PATHWAY_QUESTIONS_UPD` (before update), `TRG_WS_BKE_ZK_HU_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_PATHWAY_RECOMMEND

| Column | Type | Null | Comment |
|---|---|---|---|
| CPR_ID | NUMBER(5) | N |  |
| CP_ID | NUMBER(5) | N |  |
| CPR_DESC | VARCHAR2(500) | Y |  |
| CPR_DATE | DATE | Y |  |
| CPR_ENTERED_BY | VARCHAR2(14) | Y |  |
| CPR_ACTIVE | CHAR(1) | Y |  |
| CPC_ID | NUMBER(5) | Y |  |

- **PK** `CPR_PK`: CP_ID, CPR_ID, LOC_ID
- **FK** `CPR_FK`: (CP_ID, LOC_ID) -> DEFINITIONS.CLINICAL_PATHWAYS(CP_ID, LOC_ID) [disabled]
- **Triggers**: `CLINICAL_PATHWAY_RECMND_INSERT` (before insert), `CLINICAL_PATHWAY_RECOMMEND_CEA` (before insert or update or delete), `CLINICAL_PATHWAY_RECOMMEND_DEL` (after delete), `CLINICAL_PATHWAY_RECOMMEND_INS` (before insert), `CLINICAL_PATHWAY_RECOMMEND_UPD` (before update), `TRG_WS_ZUV_YV_UJ_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_POPUP_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| POPUP_ALERT_ID | NUMBER(5) | N |  |
| ALERT_TYPE_ID | NUMBER(4) | N |  |
| POPUP_TEXT | VARCHAR2(4000) | N |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `CLINICAL_POPUP_PK`: POPUP_ALERT_ID, ALERT_TYPE_ID
- **Triggers**: `CLINICAL_POPUP_ALERTS_CEA` (before insert or update or delete), `CLINICAL_POPUP_ALERTS_DEL` (after delete), `CLINICAL_POPUP_ALERTS_INS` (before insert), `CLINICAL_POPUP_ALERTS_UPD` (before update), `TRG_WS_LQY_OQ_QS_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_SERVICE_PRICE
This table will be used to save the Clinical Service Type wise Price

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Location within an organization |
| CPT_ID | VARCHAR2(18) | N | CPT / Service Code |
| CLINICAL_SERVICE_TYPE | CHAR(1) | N | Clinical Service represents the O for OPD, E for EAR and I for IPD, B for IBP |
| PRICE | NUMBER(12,2) default 0 | N | Price of the Item / CPT / Service |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_CLINICAL_SERVICE_PRICE`: LOCATION_ID, PATIENT_TYPE_ID, CPT_ID, CLINICAL_SERVICE_TYPE
- **FK** `FK_CLINICAL_SERVICE_PRICE_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_CLINICAL_SERVICE_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_CLINICAL_SERVICE_PRICE_1`: CLINICAL_SERVICE_TYPE IN ('O','E','I','B'
- **Triggers**: `CLINICAL_SERVICE_PRICE_CEA` (before insert or update or delete), `CLINICAL_SERVICE_PRICE_DEL` (after delete), `CLINICAL_SERVICE_PRICE_INS` (before insert), `CLINICAL_SERVICE_PRICE_UPD` (before update), `TRG_WS_ATY_IP_HN_Q` (after insert or update or delete)

## DEFINITIONS.CLINICAL_SERVICE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINICAL_SERVICE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CLINICAL_SERVICE_TYPE`: CLINICAL_SERVICE_TYPE_ID
- **CHECK** `CHK_CLINICAL_SERVICE_TYPE`: ACTIVE IN ('Y','N'

## DEFINITIONS.CLINICAL_SP_PRIVILEGES_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SP_PRIVILEGE_ID | NUMBER | N |  |
| SP_DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| HEADING | CHAR(1) default 'N' | Y |  |
| PRIVILEGE_TYPE | CHAR(1) | Y | 'C' FOR CORE, 'S' FOR SPECIAL |
| PRIVILEGES_ID | NUMBER | Y |  |

- **PK** `PK_SP_PRIVILEGE`: SP_PRIVILEGE_ID
- **UK** `UK_SP_DESCRIPTION`: SP_DESCRIPTION, PRIVILEGES_ID
- **Triggers**: `CLINICAL_SP_PRIVILEGES_SETUP_CEA` (before insert or update or delete), `CLINIC_SP_PRIVILEGES_SETUP_DEL` (after delete), `CLINIC_SP_PRIVILEGES_SETUP_INS` (before insert), `CLINIC_SP_PRIVILEGES_SETUP_UPD` (before update), `TRG_WS_UFV_MT_WQ_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_CPT_PRICE
This table will be used to define the Clinic Wise CPT Prices

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_ID | VARCHAR2(7) | N | Clinic for whom Price will be added |
| CPT_ID | VARCHAR2(18) | N | CPT whose Price will be added |
| PRICE | NUMBER(12,2) | N | CPT Price |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_CLINIC_CPT_PRICE`: CLINIC_ID, PATIENT_TYPE_ID, CPT_ID
- **FK** `FK_CLINIC_CPT_PRICE_1`: (CLINIC_ID) -> REGISTRATION.CLINIC(CLINIC_ID)
- **FK** `FK_CLINIC_CPT_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_CLINIC_CPT_PRICE_1`: PRICE>0
- **Triggers**: `CLINIC_CPT_PRICE_DEL` (after delete), `CLINIC_CPT_PRICE_INS` (before insert), `CLINIC_CPT_PRICE_UPD` (before update)

## DEFINITIONS.FORCE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| FORCE_TYPE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_FORCE_TYPE`: FORCE_TYPE_ID
- **UK** `UK_FORCE_TYPE_01`: DESCRIPTION

## DEFINITIONS.PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| COUNTER | NUMBER(6) | Y |  |
| PREFIX | VARCHAR2(3) | N |  |
| INTER_CONVERSION | NUMBER(3) | Y |  |
| FS_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| SPONSORSHIP_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| DISCOUNT_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| BONUS_TEST_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| REFUND_ALLOWED | VARCHAR2(1) default 'N' | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| TYPE_GROUP | VARCHAR2(3) | Y |  |
| DISPLAY_ALLOWED | VARCHAR2(1) | Y |  |
| BOOKING_ALLOWED | VARCHAR2(1) default ('Y') | Y |  |
| EMPLOYEE | VARCHAR2(1) | Y |  |
| MEDICAL_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| SHORT_DESC | VARCHAR2(5) | Y |  |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| CHILDREN_MEDICAL_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| LEAVE_CONTRACT_ID | VARCHAR2(3) | Y |  |
| ORDERABLE | VARCHAR2(1) default 'N' | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| INHOUSE_ORDER | CHAR(1) default 'N' | N |  |
| CARD_SWIPER | CHAR(1) default 'N' | N |  |
| SALARY_ALLOWED | CHAR(1) default 'N' | N |  |
| PATHOLOGY_CRITICAL_ALERT | CHAR(1) default 'N' | Y |  |
| DEFAULT_DIAGNOSIS_STATUS | CHAR(1) | Y |  |
| DIAGNOSTIC_PATIENT | CHAR(1) default 'N' | N |  |
| INCLUDE_IN_HR_REPORTS | CHAR(1) default 'N' | N |  |
| REF_LETTER_REQ | CHAR(1) | Y |  |
| CREATE_MRNO | CHAR(1) default 'M' | N | Check whether MRNO needs to be created for specified patient type or not. 'M' for manual and 'A' for automatic. For 'A' system will create MRNO & 'M' user will enter MRNO (If patient type location id is not equal to global location id) |
| BLOCK_ACCESS_CODE_VIEW | CHAR(1) default 'N' | Y | To block unblock the patient type for viewing its reports via web |
| ATTACH_COMPANY | CHAR(1) default 'N' | Y | Store company can be attached with specified patient type or not |
| REQUIRE_COMPANY | CHAR(1) default 'N' | Y | Store company attachment will be mandatory for specified patient type or not |
| IS_DEPENDANT | CHAR(1) | Y |  |
| REPORT_DESTINATION_REQ | CHAR(1) default 'N' | Y | Y mean Report destination is required against this patient type id  and N mean not required |
| EOBI_ELIGIBLE | CHAR(1) default 'N' | Y |  |
| CLEARANCE_STATUS_ID | VARCHAR2(3) | Y |  |
| CATEGORY_ID | VARCHAR2(10) | Y |  |
| SERVICE_STATUS_ID | VARCHAR2(6) | Y |  |
| RELATION_CAT_ID | VARCHAR2(3) | Y |  |
| SERVICE_INFORMATION_REQ | CHAR(1) default 'N' | Y |  |
| SEND_ALERT | CHAR(1) | Y | This column contain value of Y='Yes' N='No' for critical notification |
| ORDER_BY | NUMBER | Y |  |
| REQUIRED_QRCODE | CHAR(1) default 'N' | Y | This column use for generate employee card qrcode against patient type |
| URGENT_SCAN | CHAR(1) | Y | This column contain value of Y='Yes' N='No' for patient urgent scan |
| SIGN_REQUIRE | VARCHAR2(1) default 'N' | Y | Column will use to check sign required on cpt order forms |
| HP_EXEMPT | VARCHAR2(1) default 'N' | Y | Used for H Note Exempt in pre procedure assessment |
| WIC_CONSULTANCY_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| SELF_EMR_ALLOWED | VARCHAR2(1) | Y |  |
| ADULT_DEPENDANT_ALLOWED | VARCHAR2(1) | Y |  |
| PAEDS_DEPENDANT_ALLOWED | VARCHAR2(1) | Y |  |
| BS_STATUS_CHECK | VARCHAR2(1) default 'N' | Y | N means BS status will not check & Y means BS status will check. |
| PATIENT_TYPE_OTHER | VARCHAR2(6) | Y |  |
| PATIENT_TYPE_INACTIVE | VARCHAR2(6) | Y | If an employee is marked as Inactive, its associated patient's type will also be changed and it will be defined in this column. |
| EMPLOYEE_PATIENT | CHAR(1) | Y | This patient type is used for patients who are employees against Employee MRNO |
| DUTY_ROSTER | CHAR(1) | Y | This flag will be use for duty roster |
| PATIENT_FOLDER | CHAR(1) | Y |  |
| EXEMPT_ADVANCE_PAYMENT | CHAR(1) default 'N' | Y | This column will check charge in advance exempted or not |
| AUTO_ORDER | VARCHAR2(1) default 'N' | Y | If Y Then Linked CPT will auto enter against this patient type |
| RESEARCH_CONSENT | CHAR(1) default 'N' | Y | patient¿s consent used by hospital for research purposes. |
| PATIENT_TYPE_RESTRICTION | VARCHAR2(1) default 'N' | Y | Use for Patient type Restrictions |
| EXCLUDE_FROM_ICD_VERIFICATION | VARCHAR2(1) default 'N' | Y |  |
| AUTO_CANCEL_COVID_PCR | VARCHAR2(1) default 'N' | Y |  |
| OSD_RESTRICTION | VARCHAR2(1) | Y | OSD -> Outside Dispensing Restriction. |
| REF_INHOUSE_DR_REQUIRED | VARCHAR2(1) default 'Y' | Y | If Y then  ORDER_MASTER.REFERRING_INHOUSE_DOCTOR_ID is required on Counter Order screen |
| CNIC_REQUIRED | CHAR(1) default 'N' | Y | This column contain value of Y='Yes' N='No'  'N FOR CNIC NOT REQUIRED' |
| SMS_ON_INVOICE | CHAR(1) default 'N' | N |  |
| FORCE_TYPE_ID | VARCHAR2(6) | Y |  |
| EXPIRY_DAYS | NUMBER | Y |  |
| IS_STUDENT | CHAR(1) | Y |  |
| CONSENT_REQUIRED | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PATIENT_TYPE`: PATIENT_TYPE_ID
- **FK** `FK_PATIENT_TYPE_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_PATIENT_TYPE_3`: (FORCE_TYPE_ID) -> DEFINITIONS.FORCE_TYPE(FORCE_TYPE_ID) [disabled]
- **CHECK** `CK_PATIENT_TYPE_001`: MEDICAL_ALLOWED IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_002`: SPOUSE_MEDICAL_ALLOWED IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_003`: CHILDREN_MEDICAL_ALLOWED IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_004`: INCLUDE_IN_HR_REPORTS IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_1`: INHOUSE_ORDER IN ('Y', 'N'
- **CHECK** `CK_PATIENT_TYPE_2`: CARD_SWIPER IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_3`: SALARY_ALLOWED IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_4`: CREATE_MRNO IN ('A','M'
- **CHECK** `CK_PATIENT_TYPE_6`: ATTACH_COMPANY IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_7`: REQUIRE_COMPANY IN ('N','Y'
- **CHECK** `CK_PATIENT_TYPE_9`: SIGN_REQUIRE IN ('Y','N'
- **Triggers**: `PATIENT_TYPE_CEA` (before insert or update or delete), `PATIENT_TYPE_DEL` (after delete), `PATIENT_TYPE_INS` (before insert), `PATIENT_TYPE_TS` (before insert or update or delete), `PATIENT_TYPE_UPD` (before update), `TRG_WS_NNK_VQ_MU_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_PATIENT_TYPE
Save allowed patient types that can be appointed in specified clinic

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_ID | VARCHAR2(7) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_CLINIC_PATIENT_TYPE`: CLINIC_ID, PATIENT_TYPE_ID
- **FK** `FK_CLINIC_PATIENT_TYPE_1`: (CLINIC_ID) -> REGISTRATION.CLINIC(CLINIC_ID)
- **FK** `FK_CLINIC_PATIENT_TYPE_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **Triggers**: `CLINIC_PATIENT_TYPE_CEA` (before insert or update or delete), `TRG_WS_IMC_RV_XT_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_RESTRICTED_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_ID | VARCHAR2(7) | N | Refernece Column of REGISTRATION.CLINIC |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | N | Reference Column of DEFINITIONS.CPT_GROUP_TYPE |
| ACTIVE | VARCHAR2(1) | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_CLINIC_RESTRICT_GROUP`: CLINIC_ID, CPT_GROUP_TYPE_ID, ACTIVE
- **Triggers**: `CLINIC_RESTRICTED_GROUP_CEA` (before insert or update or delete), `CLINIC_RESTRICTED_GROUP_DEL` (after delete), `CLINIC_RESTRICTED_GROUP_INS` (before insert), `CLINIC_RESTRICTED_GROUP_UPD` (before update), `CLINIC_RSTRCT_GRP_INSRT` (before insert), `TRG_WS_HAX_WB_DX_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_ROOM

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_ID | NUMBER(5) | Y |  |
| ROOM_NO | NUMBER(5) | Y |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| DEFAULT_ROOM | CHAR(1) | Y |  |


## DEFINITIONS.CLINIC_SPECIALITY_INSTRCTN

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N |  |
| INSTRUCTION_ID | NUMBER | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CS_INSTRUCTIONS`: CLINIC_SPECIALITY_ID, INSTRUCTION_ID
- **Triggers**: `CLINIC_SPECIALITY_INSTRCTN_CEA` (before insert or update or delete), `CLINIC_SPECIALITY_INSTRCTN_DEL` (after delete), `CLINIC_SPECIALITY_INSTRCTN_INS` (before insert), `CLINIC_SPECIALITY_INSTRCTN_UPD` (before update), `TRG_WS_RSQ_CQ_UY_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_STOP_CODE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_STOP_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CLINIC_STOP_CODE`: CLINIC_STOP_ID
- **Triggers**: `CLINIC_STOP_CODE_CEA` (before insert or update or delete), `CLINIC_STOP_CODE_DEL` (after delete), `CLINIC_STOP_CODE_INS` (before insert), `CLINIC_STOP_CODE_UPD` (before update), `TRG_WS_LKD_XA_JU_Q` (after insert or update or delete)

## DEFINITIONS.CLINIC_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CLINIC_TYPE`: CLINIC_TYPE_ID
- **Triggers**: `CLINIC_TYPE_DEL` (after delete), `CLINIC_TYPE_INS` (before insert), `CLINIC_TYPE_UPD` (before update)

## DEFINITIONS.CLINIC_VISIT_PROCEDURE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_ID | VARCHAR2(7) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| P_DEFAULT | CHAR(1) default 'N' | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CLINIC_CPT`: CLINIC_ID, CPT_ID
- **FK** `FK_CLINIC_ID`: (CLINIC_ID) -> REGISTRATION.CLINIC(CLINIC_ID)
- **FK** `FK_CPT_ID`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CHECK_DEFAULT`: P_DEFAULT IN ('Y','N'

## DEFINITIONS.CL_CLEARANCE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CLEARANCE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(1000) | N |  |
| CATEGORY | VARCHAR2(1000) | Y |  |

- **PK** `CL_TYPE_ID`: CLEARANCE_TYPE_ID
- **Triggers**: `CL_CLEARANCE_TYPE_DEL` (after delete), `CL_CLEARANCE_TYPE_INS` (before insert), `CL_CLEARANCE_TYPE_UPD` (before update)

## DEFINITIONS.COLLECTION_SUB_CENTRE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| SERIAL_NO | NUMBER | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| ADDRESS | VARCHAR2(250) | Y |  |
| PHONE | VARCHAR2(250) | Y |  |
| EMAIL | VARCHAR2(250) | Y |  |
| FAX | VARCHAR2(250) | Y |  |
| BATCH_NO_FROM | NUMBER(4) | Y |  |
| BATCH_NO_TO | NUMBER(4) | Y |  |
| MRNO_FROM | NUMBER(6) | Y |  |
| MRNO_TO | NUMBER(6) | Y |  |
| INVOICE_NO_FROM | NUMBER(7) | Y |  |
| INVOICE_NO_TO | NUMBER(7) | Y |  |
| CPT_RETURN_FROM | NUMBER(7) | Y |  |
| CPT_RETURN_TO | NUMBER(7) | Y |  |
| EXTERNAL_DOCTOR_FROM | NUMBER(4) | Y |  |
| EXTERNAL_DOCTOR_TO | NUMBER(4) | Y |  |
| ORDER_NO_FROM | NUMBER(6) | Y |  |
| ORDER_NO_TO | NUMBER(6) | Y |  |
| RECEIPT_NO_FROM | NUMBER(7) | Y |  |
| CPT_REFUND_FROM | NUMBER(7) | Y |  |
| CPT_REFUND_TO | NUMBER(7) | Y |  |
| RECEIPT_NO_TO | NUMBER(7) | Y |  |
| LAST_MRNO | NUMBER(6) default 0 | N | This column  is being used as counter in CCWEB application |

- **PK** `PK_COLLECTION_SUB_CENTRE`: LOCATION_ID, SERIAL_NO

## DEFINITIONS.COLOURS

| Column | Type | Null | Comment |
|---|---|---|---|
| COLOUR_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_COLOURS`: COLOUR_ID
- **CHECK** `CK_COLOURS_001`: ACTIVE IN ('Y','N')
- **Triggers**: `COLOURS_CEA` (before insert or update or delete), `COLOURS_DEL` (after delete), `COLOURS_INS` (before insert), `COLOURS_UPD` (before update), `TRG_WS_QYZ_SX_RT_Q` (after insert or update or delete)

## DEFINITIONS.TABLE_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_ID | NUMBER(4) | N | This is actually representing combination of SOURCE_TABLE AND DESTINATION_TABLE |
| SOURCE_TABLE | VARCHAR2(150) | N | SOURCE_TABLE AND DESTINATION_TABLE COMBINATION SHOULD BE UNIQUE |
| DESTINATION_TABLE | VARCHAR2(150) | N | SOURCE_TABLE AND DESTINATION_TABLE COMBINATION SHOULD BE UNIQUE |

- **PK** `PK_TABLE_MAPPING`: TABLE_ID
- **UK** `UK_TABLE_MAPPING_1`: SOURCE_TABLE, DESTINATION_TABLE
- **FK** `FK_TABLE_MAPPING_1`: (SOURCE_TABLE) -> DEFINITIONS.CC_SOURCE_TABLES(SOURCE_TABLE)
- **FK** `FK_TABLE_MAPPING_2`: (DESTINATION_TABLE) -> DEFINITIONS.CC_DESTINATION_TABLES(DESTINATION_TABLE) [disabled]
- **Triggers**: `TABLE_MAPPING_CEA` (before insert or update or delete), `TABLE_MAPPING_DEL` (after delete), `TABLE_MAPPING_INS` (before insert), `TABLE_MAPPING_UPD` (before update), `TRG_WS_OOY_OT_SZ_Q` (after insert or update or delete)

## DEFINITIONS.COLUMN_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_ID | NUMBER(4) | N |  |
| SOURCE_COLUMN | VARCHAR2(100) | N |  |
| DESTINATION_COLUMN | VARCHAR2(50) | N |  |
| COLUMN_TYPE | VARCHAR2(50) | N |  |

- **PK** `PK_COLUMN_MAPPING`: TABLE_ID, SOURCE_COLUMN, DESTINATION_COLUMN
- **UK** `UK_COLUMN_MAPPING_1`: TABLE_ID, SOURCE_COLUMN
- **FK** `FK_COLUMN_MAPPING_1`: (TABLE_ID) -> DEFINITIONS.TABLE_MAPPING(TABLE_ID)
- **Triggers**: `COLUMN_MAPPING_CEA` (before insert or update or delete), `TRG_WS_NEG_BK_OW_Q` (after insert or update or delete)

## DEFINITIONS.COMMENT_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMENT_TYPE_ID | VARCHAR2(4) | N | Unique comments type ID |
| DESCRIPTION | VARCHAR2(200) | N | Description of comments type id |
| MODULE_ID | VARCHAR2(3) | N | HIS Module ID |
| ACTIVE | CHAR(1) default 'N' | N | Active Status (Y=Active, N=Inactive) |

- **PK** `PK_COMMENT_TYPES`: COMMENT_TYPE_ID
- **UK** `UK_COMMENT_TYPES_1`: MODULE_ID, DESCRIPTION
- **CHECK** `CK_COMMENT_TYPES_1`: ACTIVE IN ('Y','N'
- **Triggers**: `COMMENT_TYPES_CEA` (before insert or update or delete), `COMMENT_TYPES_DEL` (after delete), `COMMENT_TYPES_INS` (before insert), `COMMENT_TYPES_UPD` (before update), `TRG_WS_DNX_WN_ET_Q` (after insert or update or delete)

## DEFINITIONS.COMMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| COMMENT_ID | VARCHAR2(6) | N | Unique comment ID |
| COMMENT_DESC | VARCHAR2(1000) | N | Description of comments |
| COMMENT_TYPE_ID | VARCHAR2(4) | N | Type of comment foreign key reference to DEFINITIONS.COMMENT_TYPES |
| ACTIVE | CHAR(1) default 'N' | N | This column contain flag shows active status (Y=active, N=inactive) |
| CANCEL_REASON_ID_OLD | VARCHAR2(3) | Y |  |
| REASON_CATEGORY | CHAR(1) | Y | This column contain reason category, i.e A,B,C and D etc |

- **PK** `PK_COMMENTS`: COMMENT_ID
- **UK** `UK_COMMENTS_1`: COMMENT_TYPE_ID, COMMENT_DESC
- **FK** `FK_COMMENTS_1`: (COMMENT_TYPE_ID) -> DEFINITIONS.COMMENT_TYPES(COMMENT_TYPE_ID)
- **CHECK** `CK_COMMENTS_1`: COMMENT_DESC = UPPER(COMMENT_DESC
- **CHECK** `CK_COMMENTS_2`: ACTIVE IN ('Y','N'
- **Triggers**: `COMMENTS_CEA` (before insert or update or delete), `COMMENTS_DEL` (after delete), `COMMENTS_INS` (before insert), `COMMENTS_UPD` (before update), `TRG_WS_HZC_YY_CT_Q` (after insert or update or delete)

## DEFINITIONS.COMPANY

| Column | Type | Null | Comment |
|---|---|---|---|
| COMPANY_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| ADDRESS | VARCHAR2(200) | Y |  |
| PHONE_NO | VARCHAR2(30) | Y |  |
| FAX | VARCHAR2(30) | Y |  |
| EMAIL | VARCHAR2(30) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| CONTACT_PERSON | VARCHAR2(60) | Y |  |
| CONTACT_PHONE | VARCHAR2(30) | Y |  |

- **PK** `PK_COMPANY`: COMPANY_ID
- **Triggers**: `COMPANY_DEL` (after delete), `COMPANY_INS` (before insert), `COMPANY_TS` (before insert or update or delete), `COMPANY_UPD` (before update)

## DEFINITIONS.COMPARISON_OPERATORS

| Column | Type | Null | Comment |
|---|---|---|---|
| OPERATOR_ID | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| SHORT_DESC | VARCHAR2(10) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_COMPARISON_OPERATORS`: OPERATOR_ID
- **CHECK** `CK_COMPARISON_OPERATORS_001`: ACTIVE IN ('Y','N'
- **Triggers**: `COMPARISON_OPERATORS_CEA` (before insert or update or delete), `TRG_WS_HNH_JK_BC_Q` (after insert or update or delete)

## DEFINITIONS.COMPLIANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| COMPLIANCE_ID | VARCHAR2(4) | N |  |
| COMPLIANCE_DESC | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_COMPLIANCE_ID`: COMPLIANCE_ID
- **Triggers**: `COMPLIANCE_DEL` (after delete), `COMPLIANCE_INS` (before insert), `COMPLIANCE_UPD` (before update)

## DEFINITIONS.CONCEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONCEPT_ID | NUMBER(10) | N |  |
| CONCEPT_NAME | VARCHAR2(255) | N |  |
| DOMAIN_ID | VARCHAR2(20) | N |  |
| VOCABULARY_ID | VARCHAR2(20) | N |  |
| CONCEPT_CLASS_ID | VARCHAR2(20) | N |  |
| STANDARD_CONCEPT | VARCHAR2(1) | Y |  |
| CONCEPT_CODE | VARCHAR2(50) | N |  |
| VALID_START_DATE | DATE | N |  |
| VALID_END_DATE | DATE | N |  |
| INVALID_REASON | VARCHAR2(5) | Y |  |

_No standard audit columns._

- **PK** `XPK_CONCEPT`: CONCEPT_ID

## DEFINITIONS.CONSENT_CANCELLATION_EVENTS
It is used for configuration of events for consent cancellation.

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSENT_EVENT | VARCHAR2(3) | N | 001-> Draft, 002-> Pending for Review, 003-> Pending for Printing, 015-> Complete, 009-> Consent Cancelled |
| EVENT_DESC | VARCHAR2(4000) | Y |  |
| CANCELLATION_ALLOWED | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CONSENT_CANCEL_EVENT`: CONSENT_EVENT
- **Triggers**: `CONSENT_CANCELLATION_EVENTS_CEA` (before insert or update or delete), `CONSENT_CAN_EVENTS_DEL` (after delete), `CONSENT_CAN_EVENTS_INS` (before insert), `CONSENT_CAN_EVENTS_UPD` (before update), `TRG_WS_QEQ_US_UX_Q` (after insert or update or delete)

## DEFINITIONS.CONSENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y | Consent full name |
| CONSENT_FORM_TYPE | VARCHAR2(2) | Y | Consent unique flag, parent consent will be represented by one character where as child consent types will be represented by two characters and       its First character will be of parent consent type |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CONSENT_TYPE`: SERIAL_NO
- **UK** `UK_CONSENT_TYPE`: CONSENT_FORM_TYPE
- **Triggers**: `CONSENT_TYPE_CEA` (before insert or update or delete), `CONSENT_TYPE_DEL` (after delete), `CONSENT_TYPE_INS` (before insert), `CONSENT_TYPE_UPD` (before update), `TRG_WS_IWL_OX_RV_Q` (after insert or update or delete)

## DEFINITIONS.CONSULTANT_PRIVILEGES_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIVILEGES_ID | NUMBER | N |  |
| PRIVILEGES_DETAIL_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| IS_NUMBER_REQUIRED | CHAR(1) default 'N' | Y |  |
| NUMBER_REQUIRED | NUMBER | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| BOLD | CHAR(1) | Y |  |
| SP_PRIVILEGE_ID | NUMBER | Y |  |
| SR_NO | NUMBER | Y |  |

- **PK** `PK_PRIVILEGES_DETAIL`: PRIVILEGES_ID, PRIVILEGES_DETAIL_ID
- **FK** `FK_PRIVILEGE_DETAIL_02`: (SP_PRIVILEGE_ID) -> DEFINITIONS.CLINICAL_SP_PRIVILEGES_SETUP(SP_PRIVILEGE_ID) [disabled]
- **FK** `FK_PRIVILEGE_ID`: (PRIVILEGES_ID) -> HRD.PRIVILEGES_SETUP(PRIVILEGES_ID)
- **Triggers**: `CONSNT_PRIVILEGES_DET_DEL` (after delete), `CONSNT_PRIVILEGES_DET_INS` (before insert), `CONSNT_PRIVILEGES_DET_UPD` (before update), `CONSULTANT_PRIVILEGES_DETAIL_CEA` (before insert or update or delete), `TRG_WS_RUT_GC_RL_Q` (after insert or update or delete)

## DEFINITIONS.CONSULTANT_PRIVILEGES_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIVILEGES_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CONSULTANT_PRIVILEGES_SETUP`: PRIVILEGES_ID
- **UK** `UK_CONSULTANT_PRIVILEGES_SETUP`: DESCRIPTION
- **Triggers**: `CONSULTANT_PRIVILEGES_SETUP_CEA` (before insert or update or delete), `CONS_PRI_SETUP_DEL` (after delete), `CONS_PRI_SETUP_INS` (before insert), `CONS_PRI_SETUP_UPD` (before update), `TRG_WS_DZS_FW_TQ_Q` (after insert or update or delete)

## DEFINITIONS.CONTACT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTACT_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CONTACT_TYPE`: CONTACT_TYPE_ID
- **Triggers**: `CONTACT_TYPE_CEA` (before insert or update or delete), `CONTACT_TYPE_DEL` (after delete), `CONTACT_TYPE_INS` (before insert), `CONTACT_TYPE_UPD` (before update), `TRG_WS_FDK_AG_II_Q` (after insert or update or delete)

## DEFINITIONS.CONTINGENCY_FLAG_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| FLAG_VALUE | CHAR(1) | Y |  |
| ENTRY_DATE | DATE default SYSDATE | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| USERID | VARCHAR2(30) | Y |  |
| DML_STATUS | VARCHAR2(10) | Y |  |
| HISTORY_ID | VARCHAR2(10) | N |  |

- **PK** `PK_CONTINGENCY_FLAG_HISTORY`: HISTORY_ID
- **Triggers**: `CONTINGENCY_FLAG_HISTORY_CEA` (before insert or update or delete), `CONTINGENCY_FLAG_HISTORY_DEL` (after delete), `CONTINGENCY_FLAG_HISTORY_INS` (before insert), `CONTINGENCY_FLAG_HISTORY_T` (before insert), `CONTINGENCY_FLAG_HISTORY_UPD` (before update), `TRG_WS_HNJ_BZ_ER_Q` (after insert or update or delete)

## DEFINITIONS.CONTRACT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CONTRACT`: CONTRACT_ID
- **Triggers**: `CONTRACT_CEA` (before insert or update or delete), `CONTRACT_DEL` (after delete), `CONTRACT_INS` (before insert), `CONTRACT_UPD` (before update), `TRG_WS_MZJ_MX_IX_Q` (after insert or update or delete)

## DEFINITIONS.CONTRACT_FACILITIES

| Column | Type | Null | Comment |
|---|---|---|---|
| CONTRACT_FACILITY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_CONTRACT_FACILITIES`: CONTRACT_FACILITY_ID
- **Triggers**: `CONTRACT_FACILITIES_CEA` (before insert or update or delete), `CONTRACT_FACILITIES_DEL` (after delete), `CONTRACT_FACILITIES_INS` (before insert), `CONTRACT_FACILITIES_UPD` (before update), `TRG_WS_HOG_HP_DO_Q` (after insert or update or delete)

## DEFINITIONS.DEPARTMENT_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| CPT_PERFORM | VARCHAR2(1) default 'N' | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ON_CALL_ALLOWANCE | NUMBER(5) default 0 | N |  |
| PHONE_EXTENSION | VARCHAR2(20) | Y |  |
| EMAIL | VARCHAR2(60) | Y |  |
| REPORTS_DISPLAY_NAME | VARCHAR2(60) | Y |  |
| NAME_AS_DEPARTMENT | CHAR(1) default 'N' | N |  |
| SHARE_ON_PERFORM | CHAR(1) default 'N' | Y |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| SECTION_HEAD | VARCHAR2(14) | Y | This column contains MRNO of Doctor who is HEAD of Section |
| CLINICAL_REPORT | CHAR(1) default 'N' | Y |  |
| DEFAULT_DOCTOR | VARCHAR2(18) | Y | Default doctor Specified for this CPT |
| NATURE_DETAIL_ID | VARCHAR2(3) | N |  |
| NATURE_ID | VARCHAR2(3) | N |  |
| PRACTICE_INCOME | CHAR(1) default 'Y' | N | This column contains Flage  ('Y' = 'Yes' and 'N' = 'No')  that practice income to be paid. |
| ITEM_TYPE_ID | VARCHAR2(3) | Y | This column will be used to link the Item Type with the Department Section for Billing Final Invoice and Departmenal Share |
| CLINICAL_INFORMATION_REQUIRED | VARCHAR2(1) default 'N' | Y | Clinical information required 'Y' mean clinical information is mandatory to Order CPT. |
| PERFORMER_REQUIRED | VARCHAR2(1) default 'N' | Y | Performer Required 'Y' mean performer selection is mandatory to Order CPT. |

- **PK** `PK_DEPARTMENT_SECTION`: DEPARTMENT_ID, SECTION_ID
- **FK** `FK_DEPARTMENT_SECTION_01`: (NATURE_ID, NATURE_DETAIL_ID) -> DEFINITIONS.DEPARTMENT_NATURE_DETAIL(NATURE_ID, NATURE_DETAIL_ID) [disabled]
- **FK** `FK_DEPARTMENT_SECTION_2`: (ITEM_TYPE_ID) -> BILLING.ITEM_TYPE(ITEM_TYPE_ID)
- **FK** `FK_S01_T015_S01_T014_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **CHECK** `CK_DEPARTMENT_SECTION_1`: NAME_AS_DEPARTMENT IN('Y','N'
- **Triggers**: `DEPARTMENT_SECTION_CEA` (before insert or update or delete), `DEPARTMENT_SECTION_DEL` (after delete), `DEPARTMENT_SECTION_INS` (before insert), `DEPARTMENT_SECTION_UPD` (before update), `TRG_WS_PYL_YT_OL_Q` (after insert or update or delete)

## DEFINITIONS.COST_CENTER

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| COST_CENTER_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_COST_CENTER`: DEPARTMENT_ID, SECTION_ID, COST_CENTER_ID
- **FK** `FK_S01_T085_S01_T015_1`: (DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.DEPARTMENT_SECTION(DEPARTMENT_ID, SECTION_ID)
- **Triggers**: `COST_CENTER_DEL` (after delete), `COST_CENTER_INS` (before insert), `COST_CENTER_UPD` (before update)

## DEFINITIONS.COUNTING_R
This table is in use of chemo administration sheets.

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTING_ID | NUMBER(3) | Y |  |


## DEFINITIONS.COUNTRY_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(100) | Y |  |
| NATIONALITY | VARCHAR2(30) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| REGION_ID | VARCHAR2(4) | Y |  |
| OFFICE_ID | NUMBER(3) | Y |  |
| CALLING_CODE | VARCHAR2(5) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ISO_CC_2_DIGIT | CHAR(2) | Y |  |
| WEB_VIEW | CHAR(1) | N |  |
| FINAL_DESTINATION | VARCHAR2(1) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_COUNTRY_ID | NUMBER(22) | Y |  |

- **PK** `PK_COUNTRY_ZONE`: ZONE_ID, COUNTRY_ID

## DEFINITIONS.COURIER_CPT_DISTRICT

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_COURIER`: COUNTRY_ID, STATE_ID, DISTRICT_ID, CPT_ID
- **FK** `FK_COURIER`: (COUNTRY_ID, STATE_ID, DISTRICT_ID) -> DEFINITIONS.DISTRICT(COUNTRY_ID, STATE_ID, DISTRICT_ID)
- **CHECK** `CHECK_ACTIVE`: ACTIVE IN('Y','N'
- **Triggers**: `COURIER_CPT_DISTRICT_CEA` (before insert or update or delete), `TRG_WS_SES_VH_QJ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_ADMIN_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | Y |  |


## DEFINITIONS.CPT_ARCHIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N | This column contains CPT ID |
| DOCUMENT_TYPE_ID | NUMBER | Y | This column contains document TYPE id from HRD.DOCUMENT_TYPE table |
| DOCUMENT_ID | VARCHAR2(13) | N | Year based Unique document ID from LOB.DOCUMENTS_STORE |
| REMARKS | VARCHAR2(2000) | Y | other comments about document |
| ATTACHED_BY | VARCHAR2(14) | Y | MRNO who attached file |
| ACTIVE | CHAR(1) default 'N' | Y | For active 'Y' and 'N' for inactive |
| SRNO | NUMBER | N | Serial Number |
| ATTACHED_DATE | DATE | Y | Storage Date and Time when DOCUMENT is attached |

- **PK** `PK_CPT_ARCH`: CPT_ID, SRNO
- **Triggers**: `CPT_ARCHIVE_DEL` (after delete), `CPT_ARCHIVE_INS` (before insert), `CPT_ARCHIVE_UPD` (before update)

## DEFINITIONS.CPT_BAN_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| BAN_TYPE_ID | VARCHAR2(6) | N |  |
| BAN_TYPE_DESC | VARCHAR2(100) | N |  |
| MODULE_ID | VARCHAR2(3) | N |  |

- **PK** `PK_CPT_BAN_TYPES`: BAN_TYPE_ID
- **Triggers**: `CPT_BAN_TYPES_CEA` (before insert or update or delete), `TRG_WS_DWT_XZ_HC_Q` (after insert or update or delete)

## DEFINITIONS.CPT_BAN

| Column | Type | Null | Comment |
|---|---|---|---|
| BAN_ID | VARCHAR2(6) | N | Unique BAN ID |
| CPT_ID | VARCHAR2(18) | N | CPT ID foreign key reference to DEFINITIONS.CPT |
| START_DATE | DATE | N | CPT BAN restriction appliable from |
| END_DATE | DATE | Y | CPT BAN restriction expired on |
| BAN_TYPE_ID | VARCHAR2(6) | N | Module/Domain ID as BAN Type ID |
| BAN_FACTOR | CHAR(1) default 'D' | N | This BAN factor is appliable for details table D=disbale, B=BAN apply, E=Exampted |
| REMARKS | VARCHAR2(1000) | N | Remarks display to user |

- **PK** `PK_CPT_BAN`: BAN_ID
- **UK** `UK_CPT_BAN_1`: CPT_ID, START_DATE
- **FK** `FK_CPT_BAN_1`: (BAN_TYPE_ID) -> DEFINITIONS.CPT_BAN_TYPES(BAN_TYPE_ID) [disabled]
- **FK** `FK_CPT_BAN_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **CHECK** `CK_CPT_BAN_1`: BAN_FACTOR IN ('D','B','E'
- **Triggers**: `CPT_BAN_CEA` (before insert or update or delete), `CPT_BAN_DEL` (after delete), `CPT_BAN_INS` (before insert), `CPT_BAN_UPD` (before update), `TRG_WS_IOT_YR_ST_Q` (after insert or update or delete)

## DEFINITIONS.CPT_BAN_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| BAN_ID | VARCHAR2(6) | N | BAN ID foreign reference to DEFINITIONS.CPT_BAN |
| SERIAL_NO | NUMBER(3) | N | Unique Serial composite with BAN |
| BAN_FACTOR | CHAR(1) default 'E' | N | BAN Factor B=BAN Apply, E=BAN Exampted |
| LOCATION_ID | VARCHAR2(3) | Y | Location ID foreign key reference to DEFINITIONS.LOCATION |
| ORDER_TYPE_ID | VARCHAR2(3) | Y | Order Type ID(e.g. 050=Inpatient, 001=Outpatient) |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y | Patient Type ID (e.g. Ragular,Employee, Diagnostic etc.) |
| PATIENT_MRNO | VARCHAR2(14) | Y | Patient MRNO foreign key reference to registration.patient |
| CLIENT_ID | VARCHAR2(10) | Y | Company/Client ID |
| USER_MRNO | VARCHAR2(14) | Y | User MRNO/Employee Code |
| ACTIVE | CHAR(1) default 'Y' | N | Active Status(Y=Yes,N=No) |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_CPT_BAN_DETAIL`: BAN_ID, SERIAL_NO
- **FK** `FK_CPT_BAN_DETAIL_1`: (BAN_ID) -> DEFINITIONS.CPT_BAN(BAN_ID)
- **FK** `FK_CPT_BAN_DETAIL_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_CPT_BAN_DETAIL_3`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_CPT_BAN_DETAIL_4`: (PATIENT_MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]
- **FK** `FK_CPT_BAN_DETAIL_5`: (CLIENT_ID) -> BILLING.CLIENT(CLIENT_ID) [disabled]
- **FK** `FK_CPT_BAN_DETAIL_6`: (USER_MRNO) -> SECURITY.USERS(MRNO) [disabled]
- **CHECK** `CK_CPT_BAN_DETAIL_1`: BAN_FACTOR IN ('B','E'
- **CHECK** `CK_CPT_BAN_DETAIL_2`: LENGTH(LOCATION_ID||'~'||ORDER_TYPE_ID||'~'||PATIENT_TYPE_ID||'~'||PATIENT_MRNO||'~'||CLIENT_ID||'~'||USER_MRNO)>5
- **Triggers**: `CPT_BAN_DETAIL_DEL` (after delete), `CPT_BAN_DETAIL_INS` (before insert), `CPT_BAN_DETAIL_UPD` (before update), `TRG_WS_IWF_XF_EG_Q` (after insert or update or delete)

## DEFINITIONS.CPT_BODY_REGION_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| SONMED_CODE | VARCHAR2(20) | Y |  |


## DEFINITIONS.CPT_CANCELLATION_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SURGERY_APPT_REQ | VARCHAR2(1) | Y | This column will be used to store Flag Y If Surgery order required after cancellation of CPT - N In case when no surgery re-order required. |

- **PK** `PK_CANCEL_REASON`: REASON_ID
- **Triggers**: `CPT_CANCELLATION_REASON_CEA` (before insert or update or delete), `TRG_WS_JAE_OU_LH_Q` (after insert or update or delete)

## DEFINITIONS.CPT_CATEGORY_COSTING

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CATEGORY_ID | VARCHAR2(7) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| QTY | NUMBER(9,2) default 1 | N |  |
| UNIT_ID | CHAR(18) | Y |  |
| PRICE | NUMBER(12,2) default 0 | N |  |

- **PK** `PK_CPT_CATEGORY_COSTING`: CPT_CATEGORY_ID, ADMIN_COSTING_ID
- **FK** `FK_S01_T101_S01_T100_2`: (CPT_CATEGORY_ID) -> DEFINITIONS.CPT_CATEGORY(CPT_CATEGORY_ID)
- **FK** `FK_S01_T101_S01_T104_1`: (ADMIN_COSTING_ID) -> DEFINITIONS.ADMIN_COSTING(ADMIN_COSTING_ID)
- **Triggers**: `CPT_CATEGORY_COSTING_CEA` (before insert or update or delete), `CPT_CATEGORY_COSTING_DEL` (after delete), `CPT_CATEGORY_COSTING_INS` (before insert), `CPT_CATEGORY_COSTING_UPD` (before update), `TRG_WS_FBW_OZ_YV_Q` (after insert or update or delete)

## DEFINITIONS.CPT_CATEGORY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CATEGORY_DETAIL_ID | VARCHAR2(7) | N |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CPT_CATEGORY_DETAIL`: CPT_CATEGORY_DETAIL_ID
- **FK** `FK_CPT_CATEGORY_DETAIL_1`: (CPT_CATEGORY_ID) -> DEFINITIONS.CPT_CATEGORY(CPT_CATEGORY_ID) [disabled]
- **CHECK** `CK_CPT_CATEGORY_DETAIL_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `CPT_CATEGORY_DETAIL_CEA` (before insert or update or delete), `CPT_CATEGORY_DETAIL_DEL` (after delete), `CPT_CATEGORY_DETAIL_INS` (before insert), `CPT_CATEGORY_DETAIL_UPD` (before update), `TRG_WS_YOX_FO_GG_Q` (after insert or update or delete)

## DEFINITIONS.CPT_CAT_PRICE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CATEGORY_ID | VARCHAR2(7) | N |  |
| SR_NO | NUMBER(3) | N | Revision Number |
| NEW_PRICE | NUMBER(12,2) | N | Suggested/New Price of the  CPT Category |
| OLD_PRICE | NUMBER(12,2) | N | Current price of the CPT Category |
| CHANGE_DATE | DATE | Y | Date on which this New Price Became Effective |
| EFFECTIVE_DATE | DATE | N | Date on which new price should become Effective |

- **PK** `PK_CPT_CAT_PR_HT_01`: CPT_CATEGORY_ID, SR_NO
- **FK** `FK_CPT_CAT_PR_HT_01`: (CPT_CATEGORY_ID) -> DEFINITIONS.CPT_CATEGORY(CPT_CATEGORY_ID)
- **Triggers**: `CPT_CAT_PRICE_HISTORY_CEA` (before insert or update or delete), `CPT_CAT_PRICE_HISTORY_DEL` (after delete), `CPT_CAT_PRICE_HISTORY_INS` (before insert), `CPT_CAT_PRICE_HISTORY_UPD` (before update), `TRG_WS_KCQ_RR_DC_Q` (after insert or update or delete)

## DEFINITIONS.CPT_CAT_COSTING_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CATEGORY_ID | VARCHAR2(7) | N |  |
| SR_NO | NUMBER(3) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| NEW_PRICE | NUMBER(12,2) | N |  |
| OLD_PRICE | NUMBER(12,2) | N |  |
| NEW_QTY | NUMBER(9,2) default 1 | N |  |
| NEW_UNIT_ID | CHAR(18) | Y |  |
| OLD_QTY | NUMBER(9,2) default 1 | N |  |
| OLD_UNIT_ID | CHAR(18) | Y |  |

- **PK** `PK_CPT_CAT_COST_HIST_01`: CPT_CATEGORY_ID, SR_NO, ADMIN_COSTING_ID
- **FK** `FK_CPT_CAT_COST_HIST_01`: (CPT_CATEGORY_ID, SR_NO) -> DEFINITIONS.CPT_CAT_PRICE_HISTORY(CPT_CATEGORY_ID, SR_NO)
- **FK** `FK_CPT_CAT_COST_HIST_02`: (ADMIN_COSTING_ID) -> DEFINITIONS.ADMIN_COSTING(ADMIN_COSTING_ID) [disabled]
- **Triggers**: `CPT_CAT_COSTING_HISTORY_CEA` (before insert or update or delete), `CPT_CAT_COSTING_HISTORY_DEL` (after delete), `CPT_CAT_COSTING_HISTORY_INS` (before insert), `CPT_CAT_COSTING_HISTORY_UPD` (before update), `TRG_WS_HOU_MV_UU_Q` (after insert or update or delete)

## DEFINITIONS.CPT_COSTING

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| COST | NUMBER(12,2) | N |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_CPT_COSTING`: CPT_ID, ADMIN_COSTING_ID
- **FK** `FK_S01_T097_S01_T009_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_S01_T097_S01_T104_2`: (ADMIN_COSTING_ID) -> DEFINITIONS.ADMIN_COSTING(ADMIN_COSTING_ID)
- **Triggers**: `CPT_COSTING_CEA` (before insert or update or delete), `CPT_COSTING_DEL` (after delete), `CPT_COSTING_HISTORY_INS` (after insert), `CPT_COSTING_INS` (before insert), `CPT_COSTING_UPD` (before update), `TRG_WS_BKT_LB_OZ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PRICE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| NEW_PRICE | NUMBER(12,2) | Y |  |
| CHANGE_DATE | DATE | Y |  |
| OLD_PRICE | NUMBER(12,2) | N |  |
| SR_NO | NUMBER(3) | N |  |
| EFFECTIVE_DATE | DATE | Y |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| CPT_CATEGORY_SR_NO | NUMBER(3) | Y |  |
| PROPOSAL_ID | VARCHAR2(12) | Y |  |
| PROPOSAL_SRNO | VARCHAR2(5) | Y |  |
| ACKNOWLEDGE | CHAR(1) default 'N' | Y | If user acknowledge the CPT Price revison then system will allow to change the CPT Price. |

- **PK** `PK_CPT_PRICE_HISTORY`: CPT_ID, SR_NO
- **Triggers**: `CPT_PRICE_HISTORY_AUDINS` (before insert), `CPT_PRICE_HISTORY_CEA` (before insert or update or delete), `CPT_PRICE_HISTORY_DEL` (after delete), `CPT_PRICE_HISTORY_UPD` (before update), `TRG_WS_TUS_MK_JC_Q` (after insert or update or delete)

## DEFINITIONS.CPT_COSTING_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CHANGE_DATE | DATE | N |  |
| SR_NO | NUMBER(3) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| NEW_COST | NUMBER(12,2) | N |  |
| OLD_COST | NUMBER(12,2) | N |  |

- **PK** `PK_CPT_COSTING_HISTORY`: CPT_ID, SR_NO, ADMIN_COSTING_ID
- **FK** `FK_CPT_COSTING_HISTORY_01`: (CPT_ID, SR_NO) -> DEFINITIONS.CPT_PRICE_HISTORY(CPT_ID, SR_NO)
- **Triggers**: `CPT_COSTING_HISTORY_AUDINS` (before insert), `CPT_COSTING_HISTORY_CEA` (before insert or update or delete), `CPT_COSTING_HISTORY_DEL` (after delete), `CPT_COSTING_HISTORY_UPD` (before update), `TRG_WS_JLI_KO_HS_Q` (after insert or update or delete)

## DEFINITIONS.CPT_COSTING_UPDATION_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| COST | NUMBER(12,2) | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |


## DEFINITIONS.CPT_COSTING_UPD_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| COST | NUMBER(12,2) | Y |  |


## DEFINITIONS.CPT_CURRENCY_EXCHANGE

| Column | Type | Null | Comment |
|---|---|---|---|
| CUR_EX_SETUP_ID | VARCHAR2(12) | N |  |
| CURRENCY_ID | VARCHAR2(3) | N |  |
| CURRENT_EXCHANGE_RATE | NUMBER(7,4) | Y |  |
| REMARKS | VARCHAR2(250) | Y |  |

- **Triggers**: `CPT_CURRENCY_EXCHANGE_DEL` (after delete), `CPT_CURRENCY_EXCHANGE_INS` (before insert), `CPT_CURRENCY_EXCHANGE_UPD` (before update)

## DEFINITIONS.CPT_DEPARTMENT_CONSENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CPT_DEPARTMENT_CONSENT`: SERIAL_NO, DEPARTMENT_ID, SECTION_ID
- **Triggers**: `CPT_DEPARTMENT_CONSENT_DEL` (before delete), `CPT_DEPARTMENT_CONSENT_INS` (before insert), `CPT_DEPARTMENT_CONSENT_UPD` (before update)

## DEFINITIONS.CPT_DEPARTMENT_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N | Unique key on this single column should not be removed -- Idrees |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |
| DEFAULT_SECTION | VARCHAR2(1) | Y |  |
| CPT_HEAD | VARCHAR2(14) | Y | This column contains MRNO of Doctor who is HEAD to Look after performance of Test |
| ACTIVE | CHAR(1) default 'Y' | N | This column contains flag status of Active.Y=Active, N=Inactive |
| CLINICAL_INFORMATION_REQUIRED | VARCHAR2(1) default 'N' | Y | Clinical information required 'Y' mean clinical information is mandatory to Order CPT. |
| PERFORMER_REQUIRED | VARCHAR2(1) default 'N' | Y | Performer Required 'Y' mean performer selection is mandatory to Order CPT. |

- **PK** `PK_CPT_DEPARTMENT_SECTION`: CPT_ID, DEPARTMENT_ID, SECTION_ID
- **UK** `UK_CPT_ID`: CPT_ID
- **FK** `FK_S01_T092_S01_T009_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_S01_T092_S01_T015_2`: (DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.DEPARTMENT_SECTION(DEPARTMENT_ID, SECTION_ID)
- **CHECK** `CK_CPT_DEPARTMENT_SECTION_1`: ACTIVE IN ('Y','N'
- **Triggers**: `CPT_DEPARTMENT_SECTION_CEA` (before insert or update or delete), `CPT_DEPARTMENT_SECTION_DEL` (after delete), `CPT_DEPARTMENT_SECTION_INS` (before insert), `CPT_DEPARTMENT_SECTION_UPD` (before update), `TRG_WS_RCK_VP_MR_Q` (after insert or update or delete)

## DEFINITIONS.CPT_DEPARTMENT_SECTION_UPD_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |
| DEFAULT_SECTION | VARCHAR2(1) | Y |  |


## DEFINITIONS.CPT_DESC

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CPT | VARCHAR2(250) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DEPARTMENT_DESC | VARCHAR2(60) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| SECTION_DESC | VARCHAR2(60) | Y |  |
| CPT_DESC_IMRAN | VARCHAR2(4000) | Y |  |

- **PK** `PK_CPT_DESC`: CPT_ID

## DEFINITIONS.CPT_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| CPT_GROUP_TYPE | VARCHAR2(1) | Y |  |
| AMOUNT | NUMBER(12,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| USED_IN_VOUCHER | CHAR(1) default 'N' | Y |  |

- **PK** `PK_CPT_GROUP`: GROUP_ID
- **Triggers**: `CPT_GROUP_CEA` (before insert or update or delete), `CPT_GROUP_DEL` (after delete), `CPT_GROUP_INS` (before insert), `CPT_GROUP_UPD` (before update), `TRG_WS_DWL_KG_FI_Q` (after insert or update or delete)

## DEFINITIONS.CPT_GROUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| GROUP_ID | VARCHAR2(7) | N |  |

- **PK** `PK_CPT_GROUP_DETAIL`: CPT_ID, GROUP_ID
- **FK** `FK_S01_T094_S01_T009_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_S01_T094_S01_T093_2`: (GROUP_ID) -> DEFINITIONS.CPT_GROUP(GROUP_ID)
- **Triggers**: `CPT_GROUP_DETAIL_CEA` (before insert or update or delete), `CPT_GROUP_DETAIL_DEL` (after delete), `CPT_GROUP_DETAIL_INS` (before insert), `CPT_GROUP_DETAIL_UPD` (before update), `TRG_WS_DLF_KN_VP_Q` (after insert or update or delete)

## DEFINITIONS.CPT_GROUP_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| AMOUNT | NUMBER(12,2) | Y |  |
| FIXED | VARCHAR2(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `CPT_GROUP_HISTORY`: GROUP_ID
- **Triggers**: `CPT_GROUP_HISTORY_CEA` (before insert or update or delete), `CPT_GROUP_HISTORY_DEL` (after delete), `CPT_GROUP_HISTORY_INS` (before insert), `CPT_GROUP_HISTORY_UPD` (before update), `TRG_WS_DMT_DH_EQ_Q` (after insert or update or delete)

## DEFINITIONS.SHARE_HOLDER

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMIN_COSTING_ID | VARCHAR2(8) | Y |  |
| SHARE_HOLDER_ID | VARCHAR2(14) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_SHARE_HOLDER`: SHARE_HOLDER_ID
- **Triggers**: `SHARE_HOLDER_CEA` (before insert or update or delete), `SHARE_HOLDER_DEL` (after delete), `SHARE_HOLDER_INS` (before insert), `SHARE_HOLDER_UPD` (before update), `TRG_WS_TOT_HJ_KA_Q` (after insert or update or delete)

## DEFINITIONS.CPT_GROUP_SHARE_HOLDER

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(7) | N |  |
| SHARE_HOLDER_ID | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| AMOUNT | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_GROUP_SHARE_HOLDER`: GROUP_ID, SHARE_HOLDER_ID, START_DATE
- **FK** `FK_S01_T095_S01_T093_1`: (GROUP_ID) -> DEFINITIONS.CPT_GROUP(GROUP_ID)
- **FK** `FK_S01_T095_S01_T099_2`: (SHARE_HOLDER_ID) -> DEFINITIONS.SHARE_HOLDER(SHARE_HOLDER_ID)
- **Triggers**: `CPT_GROUP_SHARE_HOLDER_CEA` (before insert or update or delete), `CPT_GROUP_SHARE_HOLDER_DEL` (after delete), `CPT_GROUP_SHARE_HOLDER_INS` (before insert), `CPT_GROUP_SHARE_HOLDER_UPD` (before update), `TRG_WS_VBL_DH_WE_Q` (after insert or update or delete)

## DEFINITIONS.CPT_GROUP_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | N |  |
| CPT_GROUP_DESC | VARCHAR2(100) | Y |  |
| CPT_GROUP_PURPOSE | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_CPT_GROUP_TYPE`: CPT_GROUP_TYPE_ID
- **Triggers**: `CPT_GROUP_TYPE_CEA` (before insert or update or delete), `CPT_GROUP_TYPE_DEL` (after delete), `CPT_GROUP_TYPE_INS` (before insert), `CPT_GROUP_TYPE_UPD` (before update), `TRG_WS_WKH_KS_CE_Q` (after insert or update or delete)

## DEFINITIONS.CPT_HISTORY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(13) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| CPT_TYPE | VARCHAR2(1) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| DOCTOR_SHARE | NUMBER(12,2) | Y |  |
| CPT_BONUS | VARCHAR2(1) | Y |  |
| CPT_ENTITLED | VARCHAR2(1) | Y |  |
| CPT_INDOOR | VARCHAR2(1) | Y |  |
| COST | NUMBER(12,2) | N |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.CPT_ITEM_LINK

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ITEM_ID | VARCHAR2(25) | N |  |
| STORE_ID | VARCHAR2(25) | Y |  |
| QTY | NUMBER(4) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CPT_ITEM_LINK`: CPT_ID, ITEM_ID

## DEFINITIONS.CPT_LAST_INVOICE_RECEIPT_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(20) | Y |  |
| MAX_DATE | DATE | Y |  |
| MAX_UNIT_PRICE | VARCHAR2(10) | Y |  |

_No standard audit columns._


## DEFINITIONS.CPT_MT_ACCTUAL_FREQ
TEMPORARY TABLE FOR CPT CONSUMED

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(12) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| TOTAL_CONSUMED | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_CPT_MT_ACCTUAL_FREQ`: SETUP_ID, LOCATION_ID, CPT_ID

## DEFINITIONS.CPT_MT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| MATERIAL_SETUP_ID | VARCHAR2(12) | N |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| EFFECTIVE_FROM | DATE | Y |  |
| EFFECTIVE_TO | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) | Y |  |
| SIGN_BY | VARCHAR2(14) | Y |  |
| SIGN_DATE | DATE | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| SETUP_TYPE | VARCHAR2(1) | Y |  |

- **PK** `PK_CPT_MT_SETUP`: MATERIAL_SETUP_ID
- **Triggers**: `CPT_MT_SETUP_DEL` (after delete), `CPT_MT_SETUP_INS` (before insert), `CPT_MT_SETUP_UPD` (before update)

## DEFINITIONS.CPT_MT_ITEMS_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MATERIAL_SETUP_ID | VARCHAR2(12) | N |  |
| ITEM_ID | VARCHAR2(25) | N |  |
| PACK_UNIT_ID | VARCHAR2(5) | Y |  |
| PACK_SIZE | NUMBER(8,2) | Y |  |
| EFFECTIVE_PACK_SIZE | NUMBER(8,2) | Y |  |
| PACK_PRICE | NUMBER(15,4) | Y |  |
| PRICE_PER_UNIT | NUMBER(15,4) | Y |  |
| CURRENCY | VARCHAR2(3) | Y |  |
| MMD_UNIT_COST | NUMBER(15,4) | Y |  |
| OTHER_AMOUNT | NUMBER(15,4) | Y |  |
| QUOTATION_PRICE | NUMBER(15,4) | Y |  |
| MMD_DATE | DATE | Y |  |
| NEW_PACK_UNIT_ID | VARCHAR2(5) | Y |  |
| NEW_PACK_SIZE | NUMBER(8,2) | Y |  |
| STORE_ID | VARCHAR2(25) | Y |  |
| CONSUMED_QUANTITY | NUMBER(15,4) | Y |  |
| MATERIAL_EXPIRED | NUMBER | Y |  |

- **PK** `PK_CPT_MT_ITEMS_DETAIL`: MATERIAL_SETUP_ID, ITEM_ID
- **FK** `FK_CPT_MT_ITEMS_DETAIL`: (MATERIAL_SETUP_ID) -> DEFINITIONS.CPT_MT_SETUP(MATERIAL_SETUP_ID)
- **Triggers**: `CPT_MT_ITEMS_DETAIL_DEL` (after delete), `CPT_MT_ITEMS_DETAIL_INS` (before insert), `CPT_MT_ITEMS_DETAIL_UPD` (before update)

## DEFINITIONS.CPT_MT_CPT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MATERIAL_SETUP_ID | VARCHAR2(12) | N |  |
| ITEM_ID | VARCHAR2(25) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| PROPORTIONATE | NUMBER(8,3) | Y |  |
| ACTUAL_UNIT_CONSUMED | NUMBER | Y |  |
| PRICE_PER_CPT | NUMBER(15,4) | Y |  |
| STAND_UNIT_CONSUMED | NUMBER | Y |  |
| USED_CPT | NUMBER | Y |  |

- **PK** `UC_CPT_MT_CPT_DETAIL`: MATERIAL_SETUP_ID, ITEM_ID, CPT_ID
- **FK** `FK_CPT_MT_CPT_DETAIL`: (MATERIAL_SETUP_ID, ITEM_ID) -> DEFINITIONS.CPT_MT_ITEMS_DETAIL(MATERIAL_SETUP_ID, ITEM_ID)
- **Triggers**: `CPT_MT_CPT_DETAIL_DEL` (after delete), `CPT_MT_CPT_DETAIL_INS` (before insert), `CPT_MT_CPT_DETAIL_UPD` (before update)

## DEFINITIONS.CPT_MT_SETUP_LOC

| Column | Type | Null | Comment |
|---|---|---|---|
| MATERIAL_SETUP_ID | VARCHAR2(12) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_CPT_MT_SETUP_LOC`: MATERIAL_SETUP_ID, LOCATION_ID
- **FK** `FK_CPT_MT_SETUP_LOC`: (MATERIAL_SETUP_ID) -> DEFINITIONS.CPT_MT_SETUP(MATERIAL_SETUP_ID)
- **Triggers**: `CPT_MT_SETUP_LOC_DEL` (after delete), `CPT_MT_SETUP_LOC_INS` (before insert), `CPT_MT_SETUP_LOC_UPD` (before update)

## DEFINITIONS.CPT_NATURE_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| SETUP_NATURE_ID | VARCHAR2(3) | N |  |
| SETUP_DETAIL_ID | VARCHAR2(3) | N |  |
| PENDING_TASK | CHAR(1) | Y |  |
| NOTIFICATION | CHAR(1) | Y |  |
| STOP_PROCEEDING | CHAR(1) | Y |  |
| SETUP_LEVEL | CHAR(1) | Y | This column contain values L="Location Level Setup", O=Organization Level" |
| REMARKS | VARCHAR2(4000) | Y |  |
| SETUP_STATUS_ID | VARCHAR2(3) | Y | This column contain values 000="Unknown", 001="Required", 002="Not Required" |

- **PK** `PK_CPT_NATURE_MAPPING_001`: CPT_ID, SETUP_NATURE_ID, SETUP_DETAIL_ID
- **Triggers**: `CPT_NATURE_MAPPING_CEA` (before insert or update or delete), `CPT_NATURE_MAPPING_INS` (before insert), `TRG_WS_UAG_GI_WC_Q` (after insert or update or delete)

## DEFINITIONS.CPT_NATURE_WISE_REST_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(5) | N |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| RESTRICTION_TYPE_ID | NUMBER(4) | Y |  |
| RESTRICTION_ID | NUMBER(4) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_CPT_NAT_REST_SETUP`: SETUP_ID
- **Triggers**: `CPT_NATURE_REST_INSERT` (before insert), `CPT_NATURE_WISE_REST_SETUP_CEA` (before insert or update or delete), `CPT_NATURE_WISE_REST_SETUP_DEL` (after delete), `CPT_NATURE_WISE_REST_SETUP_INS` (before insert), `CPT_NATURE_WISE_REST_SETUP_UPD` (before update), `TRG_WS_ZYW_VL_KR_Q` (after insert or update or delete)

## DEFINITIONS.CPT_NEW_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_CODE | VARCHAR2(18) | Y |  |
| STARRED | VARCHAR2(18) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(4000) | Y |  |
| LONG_DESCRIPTION | VARCHAR2(4000) | Y |  |
| FULL_DESCRIPTION | VARCHAR2(4000) | Y |  |
| NF_TOTAL_RVU | VARCHAR2(4000) | Y |  |
| FAC_TOTAL_RVU | VARCHAR2(4000) | Y |  |
| STATUS | VARCHAR2(4000) | Y |  |
| SURGICAL | VARCHAR2(1) default 'N' | Y |  |
| SIMILAR | VARCHAR2(1) default 'U' | Y |  |

- **CHECK** `CK_CPT_NEW_R_001`: SURGICAL IN ('Y','N'
- **CHECK** `CK_CPT_NEW_R_002`: SIMILAR IN ('Y','N','U'

## DEFINITIONS.PACKAGE_TYPE
This table will be used to define the Package Category, This table is Constant Table

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_TYPE_ID | VARCHAR2(3) | N | Primary key |
| DESCRIPTION | VARCHAR2(120) | N | Full Name of the Package Category |
| SHORT_DESC | VARCHAR2(60) | N | Short Name of the Package Category |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Package Category |

- **PK** `PK_PACKAGE_TYPE`: PACKAGE_TYPE_ID
- **UK** `UK_PACKAGE_TYPE_1`: DESCRIPTION
- **UK** `UK_PACKAGE_TYPE_2`: SHORT_DESC
- **CHECK** `CK_PACKAGE_TYPE_1`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_TYPE_CEA` (before insert or update or delete), `PACKAGE_TYPE_DEL` (after delete), `PACKAGE_TYPE_INS` (before insert), `PACKAGE_TYPE_UPD` (before update), `TRG_WS_CLJ_RG_SL_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Primary key ( First Three characters will be location Id and remaining will be counter, Counter must be reset on new location_id) |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| PRICE | NUMBER(12,2) | Y | This column will represents the Total Price of the Package, Package price must be greater than zero |
| COST | NUMBER(12,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PACKAGE_TYPE | VARCHAR2(1) default 'D' | Y |  |
| TRANS_DATE | DATE default SYSDATE | N |  |
| HIDE_INVOICE_DETAIL | CHAR(1) default 'N' | Y | IF THE COLUMN IS SET TO Y THEN WE WILL NOT SHOW THE CPTS DETAIL ON INVOICE. ONLY THE PACKAGE HEADING WILL BE SHOWN WITH TOTAL AMOUNT |
| CPT_PRICE_SOURCE | CHAR(1) default 'C' | N | This Column is added on requirement of Mr. Idrees, Currently we are getting  CPT Price from CPT Table and Package Price from Package Table, Now for Package Price we will check from this Column if Values of this Column is P then get Price from Package else get price from CPT Table |
| PACKAGE_TYPE_ID | VARCHAR2(3) | Y | This column will be used to link the Package with the Package Category |
| PRICE_SOURCE | CHAR(1) default 'I' | Y | Values of this column will be P or I, P means Invoice will use the Item price from Package and I means Invoice will use the Item Price from their relevants tables/functions |
| SHOW_ITEM_PRICE | CHAR(1) default 'N' | Y | THIS COLUMN WILL BE USED TO SHOW ITEM PRICE OF PACKAGE WHEN Y |

- **PK** `PK_PACKAGES`: PACKAGE_ID
- **FK** `FK_PACKAGES_1`: (PACKAGE_TYPE_ID) -> DEFINITIONS.PACKAGE_TYPE(PACKAGE_TYPE_ID) [disabled]
- **Triggers**: `PACKAGES_CEA` (before insert or update or delete), `PACKAGES_DEL` (after delete), `PACKAGES_INS` (before insert), `PACKAGES_UPD` (before update), `TRG_WS_TEY_LX_BA_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PACKAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| PACKAGE_ID | VARCHAR2(10) | N |  |
| COST | NUMBER(12,2) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| CPT_QTY | NUMBER(3) | Y |  |

- **PK** `PK_CPT_PACKAGE`: PACKAGE_ID, CPT_ID
- **FK** `FK_S01_T010_S01_T009_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_S01_T010_S01_T023_2`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **Triggers**: `CPT_PACKAGE_CEA` (before insert or update or delete), `CPT_PACKAGE_DEL` (after delete), `CPT_PACKAGE_INS` (before insert), `CPT_PACKAGE_UPD` (before update), `TRG_WS_BSS_RT_MZ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PACKAGE_COSTING

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| COST | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_PACKAGE_COSTING`: PACKAGE_ID, CPT_ID, ADMIN_COSTING_ID
- **FK** `FK_S01_T102_S01_T010_1`: (PACKAGE_ID, CPT_ID) -> DEFINITIONS.CPT_PACKAGE(PACKAGE_ID, CPT_ID) [disabled]
- **FK** `FK_S01_T102_S01_T104_2`: (ADMIN_COSTING_ID) -> DEFINITIONS.ADMIN_COSTING(ADMIN_COSTING_ID)
- **Triggers**: `CPT_PACKAGE_COSTING_CEA` (before insert or update or delete), `CPT_PACKAGE_COSTING_DEL` (after delete), `CPT_PACKAGE_COSTING_INS` (before insert), `CPT_PACKAGE_COSTING_UPD` (before update), `TRG_WS_GGJ_AV_SH_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PACKAGE_COSTING_TMP_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | Y |  |
| COST | NUMBER(12,2) | Y |  |


## DEFINITIONS.CPT_PACKAGE_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| PACKAGE_ID | VARCHAR2(10) | N |  |
| NEW_PRICE | NUMBER(12,2) | Y |  |
| OLD_PRICE | NUMBER(12,2) | Y |  |
| CHANGE_DATE | DATE | N |  |

- **PK** `PK_CPT_PACKAGE_HISTORY`: PACKAGE_ID, CPT_ID, CHANGE_DATE

## DEFINITIONS.CPT_PACKAGE_TMP_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| PACKAGE_ID | VARCHAR2(10) | Y |  |
| COST | NUMBER(12,2) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| CPT_QTY | NUMBER(3) | Y |  |


## DEFINITIONS.CPT_PERFORM_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N | 18 digit CPT ID reference to DEFINITIONS.CPT |
| LOCATION_ID | VARCHAR2(3) | N | Location ID reference to DEFINITIONS.LOCATION |
| START_DATE | DATE | N | Effective from |
| END_DATE | DATE | Y | Expiry Date |

- **PK** `PK_CPT_PERFORM_LOCATION`: CPT_ID, LOCATION_ID
- **FK** `FK_CPT_PERFORM_LOCATION_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_CPT_PERFORM_LOCATION_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `CPT_PERFORM_LOCATION_CEA` (before insert or update or delete), `TRG_WS_LFY_BC_AR_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PERFORM_TIMING

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| PERFORM_TIMING | VARCHAR2(500) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| REPORTING_CASE | NUMBER(2) | Y |  |
| EVENT | VARCHAR2(7) | Y | This column will cotain  Events (Start Turn Around Time Calculations). |
| STAT | VARCHAR2(1) default 'N' | Y | This column will cotain flag that Stat is allow or not for this CPT. |

- **PK** `PK_CPT_PERFORM_TIMING`: LOCATION_ID, CPT_ID
- **FK** `FK_CPT_PERFORM_TIMING_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **Triggers**: `CPT_PERFORM_TIMING_DEL` (after delete), `CPT_PERFORM_TIMING_INS` (before insert), `CPT_PERFORM_TIMING_UPD` (before update)

## DEFINITIONS.CPT_PRE_INSTRUCTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| INSTRUCTIONS | VARCHAR2(3000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_CPT_PRE_INSTRUCTIONS`: CPT_ID
- **FK** `FK_CPT_PRE_INSTRUCTIONS_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)

## DEFINITIONS.CPT_PRE_REQUISITES_ERRORS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ERROR_TEXT | VARCHAR2(4000) | Y |  |
| ERROR_DATE | DATE | Y |  |
| ERROR_ID | VARCHAR2(10) | N |  |

- **PK** `PK_CPT_PRE_REQUISITES_ERRORS`: ERROR_ID
- **FK** `FK_CPT_PRE_REQUISITES_ERRORS`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **Triggers**: `CPT_PRE_REQUISITES_ERRORS_T` (before insert)

## DEFINITIONS.CPT_PRICE_EXCEL

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| NEW_PRICE | NUMBER(12,2) | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| HOSPITAL_SHARE | NUMBER(12,2) | Y |  |
| CONSULTANT | NUMBER(12,2) | Y |  |
| ANAESTHETIST | NUMBER(12,2) | Y |  |
| SURGEON | NUMBER(12,2) | Y |  |
| GOVERNMENT_CHARGES | NUMBER(12,2) | Y |  |
| ADDITIONAL_CHARGES | NUMBER(12,2) | Y |  |
| GOVT_CHARGES | NUMBER(12,2) | Y |  |
| OPERATION_SUP_RECOVER | NUMBER(12,2) | Y |  |

_No standard audit columns._


## DEFINITIONS.CPT_PRICE_REVISION_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(4) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| EFECTIVE_DATE | DATE | Y |  |
| OLD_PRICE | NUMBER(12,2) | Y |  |
| NEW_PRICE | NUMBER(12,2) | Y |  |
| UPDATED_PRICE | NUMBER(12,2) | Y |  |
| ACKNOWLEDGE | CHAR(1) default 'N' | Y |  |
| JOB_ERROR | VARCHAR2(4000) | Y |  |
| ACKNOWLEDGE_BY | VARCHAR2(30) | Y |  |
| ACKNOWLEDGE_DATE | DATE | Y |  |

- **PK** `PK_CPT_PRICE_REVISION_QUEUE`: CPT_ID, SERIAL_NO
- **Triggers**: `CPT_PRICE_REVISION_QUEUE_CEA` (before insert or update or delete), `TRG_WS_UPA_TI_ZZ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_PRICE_REVISION_VERI_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(3) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| SR_NO | NUMBER(3) | N |  |
| EFECTIVE_DATE | DATE | Y |  |
| HOSPITAL_SHARE_OLD | NUMBER(12,2) | Y |  |
| HOSPITAL_SHARE_NEW | NUMBER(12,2) | Y |  |
| CONSULTANT_SHARE_OLD | NUMBER(12,2) | Y |  |
| CONSULTANT_SHARE_NEW | NUMBER(12,2) | Y |  |
| ANAESTHETIST_OLD | NUMBER(12,2) | Y |  |
| ANAESTHETIST_NEW | NUMBER(12,2) | Y |  |
| SURGEON_SHAR_OLD | NUMBER(12,2) | Y |  |
| SURGEON_SHAR_NEW | NUMBER(12,2) | Y |  |
| OPERATION_RECOV_ROOM_SUPP_OLD | NUMBER(12,2) | Y |  |
| OPERATION_RECOV_ROOM_SUPP_NEW | NUMBER(12,2) | Y |  |
| TOTAL_OLD_PRICE | NUMBER(12,2) | Y |  |
| TOTAL_NEW_PRICE | NUMBER(12,2) | Y |  |
| SHARE_PERCENTAGE | NUMBER(12,2) | Y |  |
| ACKNOWLEDGE | CHAR(1) default 'N' | Y |  |
| ACKNOWLEDGE_BY | VARCHAR2(30) | Y |  |
| ACKNOWLEDGE_DATE | DATE | Y |  |

- **PK** `PK_CPT_PRICE_REVISION_VERI_Q`: SERIAL_NO, CPT_ID, SR_NO
- **Triggers**: `CPT_PRICE_REVISION_VERI_Q_DEL` (after delete), `CPT_PRICE_REVISION_VERI_Q_INS` (before insert), `CPT_PRICE_REVISION_VERI_Q_UPD` (before update)

## DEFINITIONS.CPT_PROPOSAL

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| TRN_TYPE | CHAR(1) default 'R' | N | N: New, R: Revision |
| PROPOSAL_DATE | DATE | Y |  |
| NATURE_ID | VARCHAR2(3) | N |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| EFFECTIVE_FROM | DATE | Y |  |
| STATUS_ID | VARCHAR2(3) default '100' | N |  |
| WFE_NO | NUMBER(3) | Y |  |
| ADD_ANES_FEE | CHAR(1) default 'N' | N |  |
| ADD_HOSPITAL_SHARE | CHAR(1) default 'N' | N |  |
| ADD_COMMISSION | CHAR(1) default 'N' | N |  |
| DEP_APPROVAL_DATE | DATE | Y |  |
| FINALIZED_DATE | DATE | Y |  |

- **PK** `PK_CPT_PROPOSAL`: PROPOSAL_ID

## DEFINITIONS.CPT_PROP_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| CPT_DESC | VARCHAR2(250) | Y |  |
| PRICE_HIST_SRNO | NUMBER(3) | Y |  |
| COST_WO_DR | NUMBER(12,2) | Y |  |
| DR_FEE | NUMBER(12,2) | Y |  |
| ANES_FEE | NUMBER(12,2) | Y |  |
| HOSPITAL_SHARE | NUMBER(12,2) | Y |  |
| SELLING_PRICE | NUMBER(12,2) | Y |  |
| COMMISION | NUMBER(12,2) | Y |  |
| REALISED_PRICE | NUMBER(12,2) | Y |  |
| EFFECTIVE_FROM | DATE | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| LAST_PROPOSAL_ID | VARCHAR2(12) | Y |  |
| LAST_PROPOSAL_SRNO | NUMBER(5) | Y |  |
| FINALIZED | CHAR(1) default 'N' | N |  |
| SELECT_FLAG | CHAR(1) default 'N' | N |  |
| POSTED | CHAR(1) default 'N' | N |  |

- **PK** `PK_CPT_PROP_DTL`: PROPOSAL_ID, PROPOSAL_SRNO
- **FK** `FK_CPT_PROP_DTL_1`: (PROPOSAL_ID) -> DEFINITIONS.CPT_PROPOSAL(PROPOSAL_ID)

## DEFINITIONS.CPT_PROP_DTL_COSTING

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| COST | NUMBER(12,2) | N |  |
| PERCENTAGE | NUMBER(5,2) | Y |  |

- **PK** `PK_CPT_PROP_DTL_COSTING`: PROPOSAL_ID, PROPOSAL_SRNO, ADMIN_COSTING_ID
- **FK** `FK_CPT_PROP_DTL_COSTING`: (PROPOSAL_ID, PROPOSAL_SRNO) -> DEFINITIONS.CPT_PROP_DTL(PROPOSAL_ID, PROPOSAL_SRNO)

## DEFINITIONS.CPT_PROP_DTL_DEPR

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| TOTAL_COST_PREV | NUMBER(12,2) | Y |  |
| TOTAL_COST | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_PROP_DTL_DEPR`: PROPOSAL_ID, PROPOSAL_SRNO
- **FK** `FK_CPT_PROP_DTL_DEPR`: (PROPOSAL_ID, PROPOSAL_SRNO) -> DEFINITIONS.CPT_PROP_DTL(PROPOSAL_ID, PROPOSAL_SRNO)

## DEFINITIONS.CPT_PROP_DTL_MANPOWER

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| DESIGNATION_ID_1 | VARCHAR2(6) | Y |  |
| DESIGNATION_ID_2 | VARCHAR2(6) | Y |  |
| DESIGNATION_ID_3 | VARCHAR2(6) | Y |  |
| DESIGNATION_ID_4 | VARCHAR2(6) | Y |  |
| DESIGNATION_ID_5 | VARCHAR2(6) | Y |  |
| TOTAL_TIME | NUMBER(10,2) | Y |  |
| NO_OF_TESTS | NUMBER(5) | Y |  |
| TIME_CONSUMED_PER_TEST | NUMBER(8,2) | Y |  |
| TOTAL_COST_PREV | NUMBER(12,2) | Y |  |
| PAYROLL_COST | NUMBER(12,2) | Y |  |
| TOTAL_COST | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_PROP_DTL_MAN`: PROPOSAL_ID, PROPOSAL_SRNO, DESIGNATION_ID
- **FK** `FK_CPT_PROP_DTL_MAN`: (PROPOSAL_ID, PROPOSAL_SRNO) -> DEFINITIONS.CPT_PROP_DTL(PROPOSAL_ID, PROPOSAL_SRNO)

## DEFINITIONS.CPT_PROP_DTL_MATERIAL

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| ITEM_ID | VARCHAR2(18) | N |  |
| ITEM_TYPE | CHAR(1) | Y |  |
| PACK_SIZE | NUMBER(5) | Y |  |
| EFFECTIVE_SIZE | NUMBER(5) | Y |  |
| TOTAL_COST_PREV | NUMBER(12,2) | Y |  |
| UNIT_COST | NUMBER(12,2) | Y |  |
| QUANTITY | NUMBER(5) | Y |  |
| TOTAL_COST | NUMBER(12,2) | Y |  |
| PACK_PRICE | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_PROP_DTL_MAT`: PROPOSAL_ID, PROPOSAL_SRNO, ITEM_ID
- **FK** `FK_CPT_PROP_DTL_MAT`: (PROPOSAL_ID, PROPOSAL_SRNO) -> DEFINITIONS.CPT_PROP_DTL(PROPOSAL_ID, PROPOSAL_SRNO)

## DEFINITIONS.CPT_PROP_DTL_OVERHEAD

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| PROPOSAL_SRNO | NUMBER(5) | N |  |
| COA_CODE | VARCHAR2(100) | Y |  |
| COA_CODE_1 | VARCHAR2(100) | Y |  |
| COA_CODE_2 | VARCHAR2(100) | Y |  |
| COA_CODE_3 | VARCHAR2(100) | Y |  |
| TOTAL_COST_PREV | NUMBER(12,2) | Y |  |
| TOTAL_COST | NUMBER(12,2) | Y |  |
| OVERHEAD_RATIO | NUMBER(7,3) | Y |  |

- **PK** `PK_CPT_PROP_DTL_OVERHEAD`: PROPOSAL_ID, PROPOSAL_SRNO
- **FK** `FK_CPT_PROP_DTL_OVERHEAD`: (PROPOSAL_ID, PROPOSAL_SRNO) -> DEFINITIONS.CPT_PROP_DTL(PROPOSAL_ID, PROPOSAL_SRNO)

## DEFINITIONS.CPT_PROP_WORKFLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | Y |  |
| WORK_FLOW_ID | NUMBER(4) | Y |  |
| EVENT_ID | NUMBER(3) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |

- **PK** `PK_CPT_PROP_WORKFLOW`: PROPOSAL_ID, WFE_NO

## DEFINITIONS.CPT_PROP_WORKFLOW_Q

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPOSAL_ID | VARCHAR2(12) | N |  |
| WFE_NO | NUMBER(3) | N |  |
| ASSIGNEE_MRNO | VARCHAR2(14) | N |  |

- **PK** `PK_CPT_PROP_WF_Q`: PROPOSAL_ID, WFE_NO, ASSIGNEE_MRNO

## DEFINITIONS.SPECIMEN

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIMEN_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| DEFAULTS | CHAR(1) default 'N' | N |  |
| COMPOUND | CHAR(1) default 'N' | N |  |
| PHLEBOTOMIST_SPECIMEN | CHAR(1) default 'N' | N |  |

- **PK** `PK_SPECIMEN`: SPECIMEN_ID
- **CHECK** `CK_SPECIMEN_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_SPECIMEN_2`: DEFAULTS IN ('Y','N'
- **CHECK** `CK_SPECIMEN_3`: COMPOUND IN ('Y','N'
- **CHECK** `CK_SPECIMEN_4`: PHLEBOTOMIST_SPECIMEN IN ('Y','N'
- **Triggers**: `SPECIMEN_CEA` (before insert or update or delete), `SPECIMEN_DEL` (after delete), `SPECIMEN_INS` (before insert), `SPECIMEN_TS` (before insert or update or delete), `SPECIMEN_UPD` (before update), `TRG_WS_TXD_AF_NP_Q` (after insert or update or delete)

## DEFINITIONS.CPT_REPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_REPORT_ID | VARCHAR2(18) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| REPETITION | NUMBER(2) default 1 | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| SPECIMEN_ID | VARCHAR2(5) | Y |  |
| REPORT_PUBLISH | CHAR(1) default 'N' | N | This column contains flag information of report publish Y=visible in report view screen, N=Not visible outside of pathology |

- **PK** `PK_CPT_REPORT`: CPT_REPORT_ID, CPT_ID
- **FK** `FK_CPT_REPORT_1`: (SPECIMEN_ID) -> DEFINITIONS.SPECIMEN(SPECIMEN_ID)
- **CHECK** `CK_CPT_REPORT_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_CPT_REPORT_2`: REPORT_PUBLISH IN ('Y','N'
- **Triggers**: `CPT_REPORT_CEA` (before insert or update or delete), `CPT_REPORT_DEL` (after delete), `CPT_REPORT_INS` (before insert), `CPT_REPORT_UPD` (before update), `TRG_WS_ZPT_OQ_AU_Q` (after insert or update or delete)

## DEFINITIONS.DEPARTMENTAL_REPORTING_PANEL
This table contains information of departmaental Reporting panel/fotter detail

| Column | Type | Null | Comment |
|---|---|---|---|
| PANEL_ID | VARCHAR2(5) | N | This column contains Unique Panel ID |
| DEPARTMENT_ID | VARCHAR2(7) | N | This column contains department ID to whole panel belongs to |
| ADDITIONAL_TEXT | VARCHAR2(120) | Y | This column contains additional text/note about panel |
| ACTIVE | CHAR(1) default 'N' | N | This column is contains Active Status of Panel (Y=Yes, N=No) |
| PANEL_STRING | VARCHAR2(100) | Y |  |
| FINAL | CHAR(1) default 'N' | N | This column is used to Finalize Panel Member, Y=Yes, N=No |
| FINAL_DATE | DATE | Y | This column contains date of Panel finalization |
| FINAL_USER | VARCHAR2(30) | Y | This column contains panel finalizing User ID |
| FINAL_TERMINAL | VARCHAR2(30) | Y | This column contains panel finalizing Terminal |
| ACTIVE_DATE | DATE | Y | This column contains date of Panel Activation |
| ACTIVE_USER | VARCHAR2(30) | Y | This column contains panel activating User ID |
| ACTIVE_TERMINAL | VARCHAR2(30) | Y | This column contains panel activating Terminal |

- **PK** `PK_DEPT_REPORTING_PANEL`: PANEL_ID
- **FK** `FK_DEPT_REPORTING_PANEL_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **CHECK** `CK_DEPT_REPORTING_PANEL_1`: FINAL IN ('Y','N'
- **CHECK** `CK_DEPT_REPORTING_PANEL_2`: ACTIVE IN ('Y','N'
- **Triggers**: `DEPARTMENTAL_REPORTING_PANEL_CEA` (before insert or update or delete), `DEPARTMENTAL_RPRTNG_PNL_DEL` (after delete), `DEPARTMENTAL_RPRTNG_PNL_INS` (before insert), `DEPARTMENTAL_RPRTNG_PNL_UPD` (before update), `REPORTING_PANEL_FINAL` (before insert or update), `TRG_WS_MEK_TH_CP_Q` (after insert or update or delete)

## DEFINITIONS.CPT_REPORT_NAME

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| REPORT_NAME | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) | N |  |
| PANEL_ID | VARCHAR2(5) | Y |  |

- **UK** `UK_CPT_REPORT_NAME`: CPT_ID, REPORT_NAME, ACTIVE
- **FK** `FK_CPT_REPORT_NAME_1`: (PANEL_ID) -> DEFINITIONS.DEPARTMENTAL_REPORTING_PANEL(PANEL_ID) [disabled]
- **FK** `FK_CPT_REPORT_NAME_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **CHECK** `CHK_CPT_REPORT_NAME_1`: ACTIVE IN ('N','Y'

## DEFINITIONS.CPT_RESTRICTED

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ALLOWED_DURATION | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'DUR' | N | DUR mean Duration Restricted,PTR Patient Type Restriction |

- **PK** `PK_CPT_DURATION_RESTRICTED`: PATIENT_TYPE_ID, CPT_ID, RESTRICTION_CATEGORY
- **Triggers**: `CPT_RESTRICTED_CEA` (before insert or update or delete), `CPT_RESTRICTED_INSERT` (before insert), `TRG_WS_YVO_ZF_AO_Q` (after insert or update or delete)

## DEFINITIONS.CPT_RESTRICTED_DISTRICT

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |

- **PK** `PK_CPT_RESTRICTED_DISTRICT`: SR_NO

## DEFINITIONS.CPT_RESTRICTED_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ALLOWED_DURATION | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'DUR' | N | DUR mean Duration Restricted,PTR Patient Type Restriction |

- **PK** `PK_CPT_RESTRICTED_LOC`: PATIENT_TYPE_ID, CPT_ID, LOCATION_ID, RESTRICTION_CATEGORY
- **Triggers**: `CPT_RESTRICTED_LOCATION_CEA` (before insert or update or delete), `CPT_REST_LOC_INSERT` (before insert), `TRG_WS_DYL_ER_VZ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_RESTRICTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| CPT_GROUP_TYPE_ID | VARCHAR2(5) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |

- **PK** `PK_CPT_RESTRICTION_TYPE`: CPT_RESTRICTION_TYPE_ID
- **FK** `FK_CPT_RESTRICTION_TYPE_1`: (CPT_GROUP_TYPE_ID) -> DEFINITIONS.CPT_GROUP_TYPE(CPT_GROUP_TYPE_ID)
- **CHECK** `CK_CPT_RESTRICTION_TYPE_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `CPT_RESTRICTION_TYPE_CEA` (before insert or update or delete), `CPT_RESTRICTION_TYPE_DEL` (after delete), `CPT_RESTRICTION_TYPE_INS` (before insert), `CPT_RESTRICTION_TYPE_UPD` (before update), `TRG_WS_AAA_ZP_BQ_Q` (after insert or update or delete)

## DEFINITIONS.RESTRICTED_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | N |  |
| IS_GENERATE_PENDING_Q | CHAR(1) | Y | 'Y' for generate missing filed queue 'N' for validation only |
| STATE_DISTRICT_WISE_REST | VARCHAR2(1) default 'N' | Y |  |
| PATIENT_TYPE_REST | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_RESTRICTED_CPT`: CPT_ID, CPT_RESTRICTION_TYPE_ID
- **FK** `FK_RESTRICTED_CPT_1`: (CPT_RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID)
- **CHECK** `CK_RESTRICTED_CPT_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `RESTRICTED_CPT_CEA` (before insert or update or delete), `RESTRICTED_CPT_DEL` (after delete), `RESTRICTED_CPT_INS` (before insert), `RESTRICTED_CPT_UPD` (before update), `TRG_WS_ZWX_OS_GR_Q` (after insert or update or delete)

## DEFINITIONS.CPT_RESTRICTED_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N |  |
| SRNO | NUMBER | N |  |
| PARAMETER | VARCHAR2(250) | Y |  |
| DISPLAY_ORDER | NUMBER(4) | Y |  |
| REQUIRED_VALUE | CHAR(1) | Y |  |
| LOV_VALIDATE | CHAR(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CPT_RESTRICTED_PARAM`: CPT_ID, CPT_RESTRICTION_TYPE_ID, SRNO
- **FK** `FK_CPT_RESTRICTED_PARAM`: (CPT_ID, CPT_RESTRICTION_TYPE_ID) -> DEFINITIONS.RESTRICTED_CPT(CPT_ID, CPT_RESTRICTION_TYPE_ID)

## DEFINITIONS.CPT_RESTRICTED_PARAM_VALUE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | N |  |
| SRNO | NUMBER | N |  |
| VALUE_ID | NUMBER | N |  |
| VALUE_DS | VARCHAR2(250) | Y |  |

- **PK** `PK_CPT_RESTRICTED_PARAM_VALUE`: CPT_ID, CPT_RESTRICTION_TYPE_ID, SRNO, VALUE_ID
- **FK** `FK_CPT_RESTRICTED_PARAM_VALUE`: (CPT_ID, CPT_RESTRICTION_TYPE_ID, SRNO) -> DEFINITIONS.CPT_RESTRICTED_PARAM(CPT_ID, CPT_RESTRICTION_TYPE_ID, SRNO)

## DEFINITIONS.CPT_RESTRICTED_PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |

- **PK** `PK_CPT_RESTRICTED_PATIENT_TYPE`: SR_NO

## DEFINITIONS.CPT_RESTRICTED_STATE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(5) | Y |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |

- **PK** `PK_CPT_RESTRICTED_STATE`: SR_NO

## DEFINITIONS.CPT_REVIEW_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| REVIEW_DATE | DATE | N |  |
| REVIEWED_BY | VARCHAR2(14) | Y |  |
| REVIEW_REMARKS | VARCHAR2(2000) | Y |  |
| NEW_PRICE | NUMBER(12,2) | Y |  |
| OLD_PRICE | NUMBER(12,2) | Y |  |

- **PK** `PK_CPT_REVIEW_HISTORY`: CPT_ID, REVIEW_DATE
- **CHECK** `CK_CPT_REVIEW_HISTORY_001`: REVIEW_DATE = TRUNC(REVIEW_DATE))
- **Triggers**: `CPT_REVIEW_HISTORY_CEA` (before insert or update or delete), `CPT_REVIEW_HISTORY_DEL` (after delete), `CPT_REVIEW_HISTORY_INS` (before insert), `CPT_REVIEW_HISTORY_UPD` (before update), `TRG_WS_CNG_FG_JQ_Q` (after insert or update or delete)

## DEFINITIONS.CPT_ROLE_REST_PERMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ROLE_ID | NUMBER(10) | N |  |
| RESTRICTION_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'DUR' | N | DUR mean Duration Restricted,PTR Patient Type Restriction |

- **PK** `PK_CPT_DUR_ROLE_REST`: CPT_ID, ROLE_ID, RESTRICTION_CATEGORY
- **Triggers**: `CPT_ROLE_PERM_INSERT` (before insert), `CPT_ROLE_REST_PERMIT_CEA` (before insert or update or delete), `TRG_WS_FHW_RD_VM_Q` (after insert or update or delete)

## DEFINITIONS.CPT_SCRIPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| CPT_TYPE | VARCHAR2(1) | Y |  |
| PRICE | NUMBER | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |

_No standard audit columns._


## DEFINITIONS.CPT_SPECIALTIES
To link a CPT with multiple specialties of the same department

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CPT_SPECIALTIES`: CPT_ID, CLINIC_SPECIALITY_ID
- **FK** `FK_CPT_SPECIALTIES_01`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_CPT_SPECIALTIES_02`: (CLINIC_SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID) [disabled]
- **CHECK** `CHK_CPT_SPECIALTIES_01`: ACTIVE IN ('N','Y'
- **Triggers**: `CPT_SPECIALTIES_CEA` (before insert or update or delete), `CPT_SPECIALTIES_DEL` (after delete), `CPT_SPECIALTIES_INS` (before insert), `CPT_SPECIALTIES_UPD` (before update), `TRG_WS_DVE_DH_EU_Q` (after insert or update or delete)

## DEFINITIONS.CPT_SPECIMEN

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| SPECIMEN_ID | VARCHAR2(5) | N |  |
| DEFAULTS | VARCHAR2(1) default 'N' | N | This column contains flag information of default specimen during orderentry (Y=Yes,N=No) |
| ACTIVE | VARCHAR2(1) default 'Y' | N | This column contains flag information of active state (Y=Active,N=Inactive) |
| REMARKS_REQUIRED | VARCHAR2(1) default 'N' | N |  |
| LABEL_CLASS | NUMBER(1) default 1 | N |  |
| COLOR_DEFAULT | CHAR(1) default 'N' | N | This column contains either default specimen color select automatically during reporting (Y=Yes, N=No) |
| APPEARANCE_DEFAULT | CHAR(1) default 'N' | N | This column contains either default specimen appearance select automatically during reporting (Y=Yes, N=No) |
| PRINT_LABEL | CHAR(1) default 'Y' | Y | Label printing flag Y=Yes,N=No |
| PRINT_COPIES | NUMBER(2) | Y |  |

- **PK** `PK_CPT_SPECIMEN`: CPT_ID, SPECIMEN_ID
- **FK** `FK_S01_T078_S01_T009_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_S01_T078_S01_T071_2`: (SPECIMEN_ID) -> DEFINITIONS.SPECIMEN(SPECIMEN_ID)
- **CHECK** `CK_CPT_SPECIMEN_1`: DEFAULTS IN ('Y', 'N'
- **CHECK** `CK_CPT_SPECIMEN_2`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_CPT_SPECIMEN_3`: (DEFAULTS = 'Y' AND ACTIVE = 'Y' OR DEFAULTS = 'N' AND ACTIVE = 'N' OR DEFAULTS = 'N' AND ACTIVE = 'Y'
- **CHECK** `CK_CPT_SPECIMEN_4`: REMARKS_REQUIRED IN ('Y','N'
- **CHECK** `CK_CPT_SPECIMEN_5`: COLOR_DEFAULT IN ('Y','N'
- **CHECK** `CK_CPT_SPECIMEN_6`: APPEARANCE_DEFAULT IN ('Y','N'
- **CHECK** `CK_CPT_SPECIMEN_7`: PRINT_LABEL IN ('Y','N'
- **Triggers**: `CPT_SPECIMEN_CEA` (before insert or update or delete), `CPT_SPECIMEN_DEL` (after delete), `CPT_SPECIMEN_INS` (before insert), `CPT_SPECIMEN_TS` (before insert or update or delete), `CPT_SPECIMEN_UPD` (before update), `TRG_WS_DFC_WC_QH_Q` (after insert or update or delete)

## DEFINITIONS.CPT_SURGERY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |


## DEFINITIONS.CPT_TEMP_MATIX_TABLE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| CHANGE_DATE | DATE | Y |  |
| OLD_PRICE | NUMBER(22,2) | Y |  |
| NEW_PRICE | NUMBER(22,2) | Y |  |
| DR_FEE_OLD | NUMBER(22,2) | Y |  |
| DR_FEE_NEW | NUMBER(22,2) | Y |  |
| ANES_SHARE_NEW | NUMBER(22,2) | Y |  |
| ANES_SHARE_OLD | NUMBER(22,2) | Y |  |


## DEFINITIONS.CPT_UPD_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| CPT_TYPE | VARCHAR2(1) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| CPT_BONUS | VARCHAR2(1) | Y |  |
| EMPLOYEE_ENTITLEMENT | VARCHAR2(1) | Y |  |
| IN_HOUSE_PERFORMED | VARCHAR2(1) | Y |  |
| COST | NUMBER(12,2) | Y |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| CONSULTANCY | VARCHAR2(1) | Y |  |
| STAT_CHARGEABLE | VARCHAR2(1) | Y |  |
| CLEARANCE | VARCHAR2(1) | Y |  |
| MOST_COMMONLY_USED | VARCHAR2(1) | Y |  |
| NO_OF_PROCEDURES | NUMBER(2) | N |  |
| REP_ORDER | NUMBER(10) | Y |  |


## DEFINITIONS.CPT_VARIABLE_HOLDER_SHARE

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| ADMIN_COSTING_ID | VARCHAR2(8) | N |  |
| SHARE_HOLDER_ID | VARCHAR2(14) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | Y |  |
| SHARE_PERCENTAGE | NUMBER(5,2) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CPT_VARIABLE_HOLDER_SHARE`: CPT_ID, ADMIN_COSTING_ID, SHARE_HOLDER_ID, START_DATE
- **FK** `FK_S01_T098_S01_T097_1`: (CPT_ID, ADMIN_COSTING_ID) -> DEFINITIONS.CPT_COSTING(CPT_ID, ADMIN_COSTING_ID)
- **FK** `FK_S01_T098_S01_T099_2`: (SHARE_HOLDER_ID) -> DEFINITIONS.SHARE_HOLDER(SHARE_HOLDER_ID)
- **Triggers**: `CPT_VARIABLE_HOLDER_SHARE_DEL` (after delete), `CPT_VARIABLE_HOLDER_SHARE_INS` (before insert), `CPT_VARIABLE_HOLDER_SHARE_UPD` (before update)

## DEFINITIONS.CPT_VIEW

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| VIEW_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `CPT_VIEW_PK`: CPT_ID, VIEW_ID
- **Triggers**: `CPT_VIEW_INS` (before insert), `CPT_VIEW_UPD` (before update)

## DEFINITIONS.CPT_WISE_DISTRICT_REST

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CPT_WISE_DISTRICT_REST`: SR_NO
- **Triggers**: `CPT_WISE_DISTRICT_REST_CEA` (before insert or update or delete), `CPT_WISE_DISTRICT_REST_DEL` (after delete), `CPT_WISE_DISTRICT_REST_INS` (before insert), `CPT_WISE_DISTRICT_REST_UPD` (before update), `TRG_WS_XOL_VL_LI_Q` (after insert or update or delete)

## DEFINITIONS.CPT_WISE_DOCUMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_TYPE_ID | NUMBER | N | This column contain document ID active flag. |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| AUTO_ATTACH_ALLOWED | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CPT_WISE_DOCUMENT_TYPE`: DOC_TYPE_ID
- **Triggers**: `CPT_WISE_DOCUMENT_TYPE_CEA` (before insert or update or delete), `CPT_WISE_DOCUMENT_TYPE_DEL` (after delete), `CPT_WISE_DOCUMENT_TYPE_INS` (before insert), `CPT_WISE_DOCUMENT_TYPE_UPD` (before update), `TRG_WS_VPS_DF_PR_Q` (after insert or update or delete)

## DEFINITIONS.CPT_WISE_DOC_ATTACH_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N | This column contain unique CPT ID. |
| SR_NO | NUMBER | N | This column contain SR #. |
| DOC_TYPE_ID | NUMBER | N | This column contain document ID. |
| REMARKS | VARCHAR2(4000) | Y | This column contain remarks against document ID. |
| ACTIVE | VARCHAR2(1) default 'N' | Y | This column contain active flag. |
| LOCATION_WISE_REST | VARCHAR2(1) default 'N' | Y |  |
| PATIENT_TYPE_REST | VARCHAR2(1) | Y |  |

- **PK** `PK_CPT_WISE_DOC_ATTACH_SETUP`: CPT_ID, SR_NO, DOC_TYPE_ID
- **UK** `UK_CPT_WISE_DOC_ATTACH_SETUP`: CPT_ID, DOC_TYPE_ID
- **FK** `FK_CPT_WISE_DOC_ATTACH_SETUP`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **Triggers**: `CPT_WISE_DOC_ATTACH_SETUP_CEA` (before insert or update or delete), `CPT_WISE_DOC_ATTACH_SETUP_DEL` (after delete), `CPT_WISE_DOC_ATTACH_SETUP_INS` (before insert), `CPT_WISE_DOC_ATTACH_SETUP_UPD` (before update), `TRG_WS_QEM_ED_WP_Q` (after insert or update or delete)

## DEFINITIONS.CPT_WISE_PATIENT_TYPE_REST

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DOC_TYPE_ID | NUMBER | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | VARCHAR2(18) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_CPT_WISE_PATIENT_TYPE_REST`: SR_NO, DOC_TYPE_ID, CPT_ID, PATIENT_TYPE_ID, OBJECT_CODE

## DEFINITIONS.CPT_WISE_REST_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(5) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| RESTRICTION_TYPE_ID | NUMBER(4) | Y |  |
| RESTRICTION_ID | NUMBER(4) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_CPT_REST_SETUP`: SETUP_ID, CPT_ID
- **Triggers**: `CPT_RESTRICTION_INSERT` (before insert), `CPT_WISE_REST_SETUP_CEA` (before insert or update or delete), `CPT_WISE_REST_SETUP_DEL` (after delete), `CPT_WISE_REST_SETUP_INS` (before insert), `CPT_WISE_REST_SETUP_UPD` (before update), `TRG_WS_LTS_NQ_HO_Q` (after insert or update or delete)

## DEFINITIONS.CPT_WISE_STATE_REST

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_CPT_WISE_STATE_REST`: SR_NO
- **Triggers**: `CPT_WISE_STATE_REST_CEA` (before insert or update or delete), `CPT_WISE_STATE_REST_DEL` (after delete), `CPT_WISE_STATE_REST_INS` (before insert), `CPT_WISE_STATE_REST_UPD` (before update), `TRG_WS_MJA_MM_QF_Q` (after insert or update or delete)

## DEFINITIONS.CPT_WISE_USER

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| EMPLOYEE_CODE | VARCHAR2(14) | N | PAT_CONSULTANT,PAT_DOCTOR AND PAT_TECH employees to verify CPT |
| START_DATE | DATE | Y | Starting date to verify Cpt verification |
| END_DATE | DATE | Y | Ending date to verify Cpt verification |

- **PK** `PK_CPT_EMPCODE`: CPT_ID, EMPLOYEE_CODE
- **Triggers**: `CPT_WISE_USER_CEA` (before insert or update or delete), `CPT_WISE_USER_DEL` (after delete), `CPT_WISE_USER_INS` (before insert), `CPT_WISE_USER_UPD` (before update), `TRG_WS_JFD_PK_AN_Q` (after insert or update or delete)

## DEFINITIONS.CURRENCY

| Column | Type | Null | Comment |
|---|---|---|---|
| CURRENCY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SYMBOL | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(3) | Y |  |
| CURRENT_EXCHANGE_RATE | NUMBER(7,4) | Y |  |
| MARKETING_EXCHANGE_RATE | NUMBER(7,4) | Y |  |
| MARKETING_SHORT_DESC | VARCHAR2(3) | Y |  |

- **PK** `PK_CURRENCY`: CURRENCY_ID
- **Triggers**: `CURRENCY_CEA` (before insert or update or delete), `CURRENCY_DEL` (after delete), `CURRENCY_INS` (before insert), `CURRENCY_TS` (before insert or update or delete), `CURRENCY_UPD` (before update), `CURRENCY_UPD_NEW` (after update), `TRG_WS_ZVC_ZM_DG_Q` (after insert or update or delete)

## DEFINITIONS.DATA_CHECKING_R

| Column | Type | Null | Comment |
|---|---|---|---|
| BATCH_NO | VARCHAR2(9) | Y |  |
| TABLE_NAME | VARCHAR2(60) | Y |  |
| COUNT_IMPORTED | NUMBER | Y |  |
| COUNT_EXPORTED | NUMBER | Y |  |


## DEFINITIONS.DATA_NOTES_R

| Column | Type | Null | Comment |
|---|---|---|---|
| A | NUMBER(10) | Y |  |
| B | VARCHAR2(4000) | Y |  |
| C | VARCHAR2(4000) | Y |  |
| D | VARCHAR2(4000) | Y |  |
| E | VARCHAR2(4000) | Y |  |
| F | VARCHAR2(4000) | Y |  |
| G | VARCHAR2(4000) | Y |  |
| H | VARCHAR2(4000) | Y |  |
| I | VARCHAR2(4000) | Y |  |
| J | VARCHAR2(4000) | Y |  |
| K | VARCHAR2(4000) | Y |  |
| L | VARCHAR2(4000) | Y |  |
| M | VARCHAR2(4000) | Y |  |
| N | VARCHAR2(4000) | Y |  |


## DEFINITIONS.DATA_SYNC_ERROR_MODEL

| Column | Type | Null | Comment |
|---|---|---|---|
| RULE_ID | VARCHAR2(6) | N | This column contain rule, this column will be primary key |
| QUEUE_NAME | VARCHAR2(250) | Y | This column contain queue name EMR Queue,EMR Queue detail and Except EMR |
| DML_EVENT | VARCHAR2(30) | Y | This column contain Insert,Delete and Update |
| ERROR | VARCHAR2(4000) | Y | This column contain Error |
| ROWS_AFFECTED | VARCHAR2(30) | Y | This column contain affected rows |
| QUEUE_STATUS | CHAR(1) | Y | This column contain queue status like E=Error,S=Sucess |
| ACTION_FOR_PROCEDURE | VARCHAR2(100) | Y | This column contain action for procedure |
| MAIN_PROCEDURE | VARCHAR2(500) | Y | This column contain main componet of sub procedure |
| SUB_PROCEDURE | VARCHAR2(500) | Y | This column contain value of sub procedure |
| FIND_PARENT | CHAR(1) | Y | This column contain action for parent record  Y=Yes,N=No |
| FIND_CHILD | CHAR(1) | Y | This column contain action for child record  Y=Yes,N=No |
| CONVERT_DML | CHAR(1) | Y | This column contain regenerate DML   Y=Yes,N=No |
| INSERT_HISTORY | CHAR(1) | Y | This column contain insert row history table Y=Yes,N=No |
| INCREASE_ATTEMPTS | CHAR(1) | Y | This column contain increase no of movement attempts  Y=Yes,N=No |
| UPD_LAST_ERROR | CHAR(1) | Y | This column contain update last error  Y=Yes,N=No |
| ERROR_IN_TABLE | VARCHAR2(150) | Y | This column contain save error in table like admin queue |
| EMR_Q_INS | CHAR(1) | Y | This column contain emr queue insert  Y=Yes,N=No |
| EMR_Q_DETAIL_INS | CHAR(1) | Y | This column contain emr queue insert in detail  Y=Yes,N=No |
| DELETE_FROM_Q | CHAR(1) | Y | This column contain remove for actuall queue  Y=Yes,N=No |
| INFORM_ADMIN | CHAR(1) | Y | This column contain inform to admin insert row in admin queue Y=Yes,N=No |
| STOP_PROCESSING | CHAR(1) | Y | This column contain processing stop Y=Yes,N=No |
| ERROR_CODE | VARCHAR2(100) | Y | This column contain Error oracle and customize code |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_DATA_SYNC_ERROR_MODEL_001`: RULE_ID
- **UK** `UK_DATA_SYNC_ERROR_MODEL_001`: QUEUE_NAME, DML_EVENT, ERROR

## DEFINITIONS.DATA_SYNC_MODEL

| Column | Type | Null | Comment |
|---|---|---|---|
| DB_USER | VARCHAR2(30) | N | This column contain value of  data model sync |
| DB_TYPE | VARCHAR2(10) | N | This column contain value of  data model data type |
| NETWORK_TOPOLOGY | VARCHAR2(30) | N | This column contain value of  data model network toplogy |
| ACTION_FOR_TIGGER | VARCHAR2(30) | Y | This column contain value of  data model data action for trigger |
| ACTION_FOR_PROCEDURE | VARCHAR2(30) | Y | This column contain value of  data model data action for procedure |
| MODEL_TYPE_ID | NUMBER(2) | N | This column contain value of  data model type id |

- **PK** `PK_DATA_SYNC_MODEL_001`: DB_USER, DB_TYPE, NETWORK_TOPOLOGY, MODEL_TYPE_ID
- **CHECK** `CH_DATA_SYNC_MODEL_01`: NETWORK_TOPOLOGY IN ('STAR','MESH'
- **CHECK** `CH_DATA_SYNC_MODEL_02`: ACTION_FOR_TIGGER IN ('NONE','DC-TO-CR','DC-TO-ALL'
- **CHECK** `CH_DATA_SYNC_MODEL_03`: ACTION_FOR_PROCEDURE IN ('NONE','DC-TO-ALL','DC-TO-BUFFER'

## DEFINITIONS.DATA_SYNC_MODEL_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| MODEL_TYPE_ID | NUMBER(2) | N | This column contain values of Model type id |
| DESCRIPTIONS | VARCHAR2(200) | Y | This column contain values of data sync model name |
| SHORT_DESC | VARCHAR2(100) | Y | This column contain values of data sync model short desc |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_DATA_SYNC_MDL_TYPES_001`: MODEL_TYPE_ID

## DEFINITIONS.DATES

| Column | Type | Null | Comment |
|---|---|---|---|
| DATE_COLUMN | DATE | N |  |

- **PK** `PK_DATES`: DATE_COLUMN
- **CHECK** `CK_DATES_001`: DATE_COLUMN = TRUNC(DATE_COLUMN

## DEFINITIONS.DAY

| Column | Type | Null | Comment |
|---|---|---|---|
| DAY_ID | NUMBER(1) | N |  |
| DESCRIPTION | VARCHAR2(10) | Y |  |
| STATUS | VARCHAR2(1) | Y |  |
| NORMAL_FROM_TIME | VARCHAR2(5) default '08:00' | N |  |
| NORMAL_TO_TIME | VARCHAR2(5) default '17:00' | N |  |
| RAMZAN_FROM_TIME | VARCHAR2(5) default '08:00' | N |  |
| RAMZAN_TO_TIME | VARCHAR2(5) default '15:30' | N |  |
| WORKING_DAY | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DAY`: DAY_ID
- **CHECK** `CK_DAY_001`: WORKING_DAY IN ('Y','N'
- **Triggers**: `DAY_CEA` (before insert or update or delete), `DAY_DEL` (after delete), `DAY_INS` (before insert), `DAY_UPD` (before update), `TRG_WS_HWP_RJ_FK_Q` (after insert or update or delete)

## DEFINITIONS.DAY_LANGUAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| DAY_ID | NUMBER(1) | N | Key of DEFINITIONS.DAY |
| LABEL_DESC | NVARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DAY_LANGUAGE_SETUP`: LANGUAGE_ID, DAY_ID
- **Triggers**: `DAY_LANGUAGE_SETUP_CEA` (before insert or update or delete), `DAY_LANGUAGE_SETUP_DEL` (after delete), `DAY_LANGUAGE_SETUP_INS` (before insert), `DAY_LANGUAGE_SETUP_UPD` (before update), `TRG_WS_YSH_VZ_DH_Q` (after insert or update or delete)

## DEFINITIONS.DAY_MINUTES

| Column | Type | Null | Comment |
|---|---|---|---|
| MINUTE_NUMBER | NUMBER(4) | N |  |

- **PK** `PK_DAY_MINUTES`: MINUTE_NUMBER

## DEFINITIONS.DAY_SESSION

| Column | Type | Null | Comment |
|---|---|---|---|
| SESSION_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DAY_SESSION`: SESSION_ID
- **Triggers**: `DAY_SESSION_CEA` (before insert or update or delete), `DAY_SESSION_DEL` (after delete), `DAY_SESSION_INS` (before insert), `DAY_SESSION_UPD` (before update), `TRG_WS_CBX_QO_DP_Q` (after insert or update or delete)

## DEFINITIONS.DAY_SESSION_LANG_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUGAE_ID | VARCHAR2(6) | N |  |
| SESSION_ID | NUMBER | N |  |
| LABEL_DESC | NVARCHAR2(50) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DAY_SESSION_LANG_SETUP`: LANGUGAE_ID, SESSION_ID
- **Triggers**: `DAY_SESSION_LANG_SETUP_CEA` (before insert or update or delete), `DAY_SESSION_LANG_SETUP_DEL` (after delete), `DAY_SESSION_LANG_SETUP_INS` (before insert), `DAY_SESSION_LANG_SETUP_UPD` (before update), `TRG_WS_KIY_UD_JW_Q` (after insert or update or delete)

## DEFINITIONS.DAY_WISE_RESOURCE_SCHEDULE

| Column | Type | Null | Comment |
|---|---|---|---|
| DAY_ID | NUMBER(1) | N |  |
| RESOURCE_ID | NUMBER(4) | N |  |
| AVAILABLE_FROM | DATE | Y |  |
| AVAILABLE_TO | DATE | Y |  |
| OVER_BOOKING_MINUTES | NUMBER(4) | Y |  |
| OVER_BOOKING | CHAR(1) | Y |  |
| EMERGENCY_BED | CHAR(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DAY_WISE_RESOURCE_SCHEDULE`: DAY_ID, RESOURCE_ID

## DEFINITIONS.DB_SERVICES_MODE

| Column | Type | Null | Comment |
|---|---|---|---|
| DISTRIBUTED_LOCATION_ID | VARCHAR2(3) | Y |  |
| SERVICES_MODE | CHAR(1) | Y | D for distributed, S for waiting for syncing |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |

- **Triggers**: `DB_SERVICES_MODE_DEL` (after delete), `DB_SERVICES_MODE_INS` (before insert), `DB_SERVICES_MODE_UPD` (before update)

## DEFINITIONS.DB_USERS
The purpose of this table is to store the information of all database users and to identify them by types i.e. system users or application users etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| USERNAME | VARCHAR2(60) | N | Database user name |
| CREATED | DATE | Y | Store the creation date of database user |
| USER_TYPE | CHAR(1) | Y | identify the type of users i.e. "S" for system users, "A" for application users i.e. registration,orderentry etc., "U" for MIS users and "D" for auditing user "C" for connection users |
| ACTIVE | CHAR(1) | Y | value "Y" shows that user is active and "N" shows that user is inactive or leave the organization |

- **PK** `PK_DB_USERS`: USERNAME

## DEFINITIONS.DC_MEDICINE_FILTERS
This table is used to store then setup data of medicine filters.

| Column | Type | Null | Comment |
|---|---|---|---|
| FILTER_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y | This column is used to store the short description of medicine filter. |
| ORDER_BY | NUMBER | Y | This column is used to store the order by value. |
| ACTIVE | VARCHAR2(1) | Y | Y - Active, N - Inactive. |
| VALUE | NUMBER | Y |  |
| DEFAULT_VALUE | VARCHAR2(1) default 'N' | Y |  |

- **Triggers**: `DC_MEDICINE_FILTERS_DEL` (after delete), `DC_MEDICINE_FILTERS_INS` (before insert), `DC_MEDICINE_FILTERS_UPD` (before update)

## DEFINITIONS.DECISION

| Column | Type | Null | Comment |
|---|---|---|---|
| DECISION_ID | VARCHAR2(10) | N |  |
| DECISION_DESC | VARCHAR2(100) | Y |  |
| DECISION_SHORT_DESC | VARCHAR2(10) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DECISION`: DECISION_ID

## DEFINITIONS.FILES_SERVERS_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVER_TYPE_ID | VARCHAR2(3) | N |  |
| TYPE_DESC | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N | Y: ACTIVE, N: INACTIVE |

- **PK** `PK_FILES_SERVERS_TYPES`: SERVER_TYPE_ID
- **CHECK** `CK_FILES_SERVERS_TYPES_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_SERVERS_TYPES_DEL` (after delete), `FILES_SERVERS_TYPES_INS` (before insert), `FILES_SERVERS_TYPES_UPD` (before update), `TRG_WS_SAM_LJ_CS_Q` (after insert or update or delete)

## DEFINITIONS.FILES_SERVERS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVER_ID | VARCHAR2(10) | N | Unique key of server ID 000=Location ID + YY=Current Year + 99999=Counter) |
| SERVER_NAME | VARCHAR2(100) | N | This column contains unique server name |
| ACCESS_PATH | VARCHAR2(1000) | N | This column contains full qualifying acess path of machine |
| REMARKS | VARCHAR2(200) | Y | Remarks note |
| OBJECT_CODE | VARCHAR2(11) | N | This column contains row creator object code |
| CREATED_BY | VARCHAR2(20) | N | This column contains row creator user information |
| ACTIVE | CHAR(1) default 'Y' | N | Flag column (Y=active, N=Inactive) |
| SERVER_TYPE_ID | VARCHAR2(3) | N | This column contains Server Type ID reference to DEFINITIONS.SERVER_TYPES |
| LOCATION_ID | VARCHAR2(3) | N | This column contains Physical Location ID of server (e.g. 001,007,C01 etc) |

- **PK** `PK_FILES_SERVERS`: SERVER_ID
- **UK** `UK_FILES_SERVERS_1`: ACCESS_PATH
- **FK** `FK_FILES_SERVERS_1`: (SERVER_TYPE_ID) -> DEFINITIONS.FILES_SERVERS_TYPES(SERVER_TYPE_ID)
- **CHECK** `CK_FILES_SERVERS_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_SERVERS_DEL` (after delete), `FILES_SERVERS_INS` (before insert), `FILES_SERVERS_NEW_ID` (before insert or update), `FILES_SERVERS_UPD` (before update), `TRG_WS_RID_CQ_BR_Q` (after insert or update or delete)

## DEFINITIONS.FILES_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| FILE_TYPE_ID | VARCHAR2(3) | N | Unique ID for File Type ID |
| FILE_DESC | VARCHAR2(60) | N | Description of File Description |
| COMMENTS | VARCHAR2(100) | Y |  |
| STORAGE_TYPE | VARCHAR2(2) | Y | Storage type is used to preserve document (DB=database, OS=Operating system) |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |
| DEFAULT_TEMPORARY_PATH | VARCHAR2(1000) | Y | This column contains default temporary path to copy the attached file on the allocated default server |
| OPEN_WITH | VARCHAR2(3) | Y |  |
| FILE_SIZE | NUMBER(8,2) | Y | This column contains the uploading file maximum size limit in MBs. Null or zero means no limit on size of uploading file |
| DELETE_SOURCE_FILE | CHAR(1) default 'Y' | Y | This column contains the flag value (Y/N) |
| OPEN_FILE_AFTER_DOWNLOAD | CHAR(1) default 'Y' | Y | This column contains the flag value (Y/N) to decide whether the file to be opend after downloading? |

- **PK** `PK_FILES_TYPES`: FILE_TYPE_ID
- **UK** `UK_FILES_TYPES`: FILE_DESC
- **CHECK** `CK_FILES_TYPES_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_TYPES_DEL` (after delete), `FILES_TYPES_INS` (before insert), `FILES_TYPES_UPD` (before update), `TRG_WS_IBA_SJ_YY_Q` (after insert or update or delete)

## DEFINITIONS.DEFAULT_FILES_SERVERS
This table is used to assign servers to specific locations according to the modality and server type. Server Priority is also assigned

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Location ID for which the server setting is being made. |
| SERVER_TYPE_ID | VARCHAR2(3) | N | Server Type ID for the Location and File_Type_ID for which the server setting is being made. |
| SERVER_ID | VARCHAR2(10) | N | Server ID assigned to the specified location according to File_Type_ID and Server Type. |
| PRIORITY | NUMBER(2) | N | Priority of the assigned server |
| ACTIVE | CHAR(1) | N | Y:Active, N:Inactive |
| FILE_TYPE_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DEFAULT_FILES_SERVERS`: LOCATION_ID, SERVER_TYPE_ID, SERVER_ID, FILE_TYPE_ID
- **UK** `UK_DEFAULT_FILES_SERVERS_1`: PRIORITY, SERVER_TYPE_ID, LOCATION_ID, FILE_TYPE_ID
- **FK** `FK_DEFAULT_FILES_SERVERS_1`: (SERVER_TYPE_ID) -> DEFINITIONS.FILES_SERVERS_TYPES(SERVER_TYPE_ID) [disabled]
- **FK** `FK_DEFAULT_FILES_SERVERS_2`: (SERVER_ID) -> DEFINITIONS.FILES_SERVERS(SERVER_ID) [disabled]
- **FK** `FK_DEFAULT_FILES_SERVERS_3`: (FILE_TYPE_ID) -> DEFINITIONS.FILES_TYPES(FILE_TYPE_ID) [disabled]
- **Triggers**: `DEFAULT_FILES_SERVERS_DEL` (after delete), `DEFAULT_FILES_SERVERS_INS` (before insert), `DEFAULT_FILES_SERVERS_UPD` (before update)

## DEFINITIONS.DEFAULT_MEDICINE_ORDER

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| MEDICAL_ITEM | VARCHAR2(1) | N |  |
| FREQUENCY_ID | VARCHAR2(5) | Y |  |
| DURATION | NUMBER(6,2) | Y |  |
| DURATION_UNIT_ID | VARCHAR2(5) | Y |  |
| ROUTE_ID | VARCHAR2(5) | Y |  |

- **PK** `PK_DEFAULT_MEDICINE_ORDER`: LOCATION_ID, MEDICAL_ITEM
- **Triggers**: `DEFAULT_MEDICINE_ORDER_DEL` (after delete), `DEFAULT_MEDICINE_ORDER_INS` (before insert), `DEFAULT_MEDICINE_ORDER_UPD` (before update)

## DEFINITIONS.DEFAULT_ONCOLOGIST

| Column | Type | Null | Comment |
|---|---|---|---|
| ONCOLOGIST_MRNO | VARCHAR2(14) | N |  |
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| DEFAULT_ONCOLOGIST | VARCHAR2(1) default 'N' | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DEFAULT_ONCOLOGIST`: ORG_ID, ZON_ID, LOC_ID, ONCOLOGIST_MRNO
- **Triggers**: `DEFAULT_ONCOLOGIST_CEA` (before insert or update or delete), `DEFAULT_ONCOLOGIST_DEL` (after delete), `DEFAULT_ONCOLOGIST_INS` (before insert), `DEFAULT_ONCOLOGIST_UPD` (before update), `TRG_WS_TDD_DB_YI_Q` (after insert or update or delete)

## DEFINITIONS.DEFAULT_REPORT_DESTINATION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| TRANSACTION_TYPE_ID | VARCHAR2(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| REPORT_DESTINATION_ID | VARCHAR2(5) | N |  |
| CONSULTANT_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_DEFAULT_REPORT_DESTINATION`: LOCATION_ID, ORDER_LOCATION_ID, TRANSACTION_TYPE_ID, PATIENT_TYPE_ID, REPORT_DESTINATION_ID
- **Triggers**: `DEFAULT_REPORT_DESTINATION_CEA` (before insert or update or delete), `TRG_WS_ZOT_YX_UX_Q` (after insert or update or delete)

## DEFINITIONS.DEFAULT_USER_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_MRNO | VARCHAR2(14) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| RESTRICTION_TYPE_ID | VARCHAR2(10) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_DEFAULT_USER_CPT`: USER_MRNO, CPT_ID, RESTRICTION_TYPE_ID, ORGANIZATION_ID
- **Triggers**: `DEFAULT_USER_CPT_DEL` (after delete), `DEFAULT_USER_CPT_INS` (before insert), `DEFAULT_USER_CPT_UPD` (before update)

## DEFINITIONS.DEF_BED_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_NO | VARCHAR2(9) | N |  |
| TRANSACTION_DATE | DATE | Y |  |
| BED_ID | VARCHAR2(7) | Y |  |
| ROOM_ID | VARCHAR2(7) | Y |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| CURRENT_EVENT_ID | VARCHAR2(3) | Y |  |
| CURRENT_EVENT_DATE | DATE | Y |  |
| CURRENT_PERFORM_BY | VARCHAR2(14) | Y |  |
| OLD_EVENT_ID | VARCHAR2(3) | Y |  |
| OLD_EVENT_DATE | DATE | Y |  |
| OLD_PERFORM_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_DEF_BED_DETAIL`: TRANSACTION_NO, LOC_ID
- **Triggers**: `DEF_BED_DETAIL_DEL` (after delete), `DEF_BED_DETAIL_INS` (before insert), `DEF_BED_DETAIL_UPD` (before update), `TRG_WS_AZA_JY_FX_Q` (after insert or update or delete)

## DEFINITIONS.DEF_BED_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| BED_SR_NO | VARCHAR2(9) | N |  |
| TRANS_DATE | DATE default SYSDATE | Y |  |
| BED_ID | VARCHAR2(7) | N |  |
| ROOM_ID | VARCHAR2(7) | N |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| BED_ID_ORDER_BY | NUMBER(9) | Y |  |
| CLEANING_DATE | DATE | Y |  |
| READY_DATE | DATE | Y |  |
| MAINTENANCE_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| BED_DESC | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| MAINTENANCE_BY | VARCHAR2(14) | Y |  |
| READY_BY | VARCHAR2(14) | Y |  |
| BED_ISOLATION | VARCHAR2(1) | Y |  |
| ISOLATION_DATE | DATE | Y |  |
| ISOLATION_BY | VARCHAR2(14) | Y |  |

- **PK** `PK_DEF_BED_HISTORY`: BED_SR_NO, LOCATION_ID
- **Triggers**: `DEF_BED_HISTORY_DEL` (after delete), `DEF_BED_HISTORY_INS` (before insert), `DEF_BED_HISTORY_UPD` (before update)

## DEFINITIONS.DEF_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| SHORT_DESC | VARCHAR2(25) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DEF_CATEGORY`: CATEGORY_ID
- **Triggers**: `DEF_CATEGORY_CEA` (before insert or update or delete), `TRG_WS_MTC_MC_YN_Q` (after insert or update or delete)

## DEFINITIONS.DEF_CATEGORY_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(5) | N |  |
| CATEGORY_TYPE_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| SHORT_DESC | VARCHAR2(25) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REFERENCE_NO | VARCHAR2(2) | Y |  |

- **PK** `PK_DEF_CATEGORY_TYPE`: CATEGORY_ID, CATEGORY_TYPE_ID
- **FK** `FK_DEF_CATEGORY_1`: (CATEGORY_ID) -> DEFINITIONS.DEF_CATEGORY(CATEGORY_ID)
- **Triggers**: `DEF_CATEGORY_TYPE_CEA` (before insert or update or delete), `TRG_WS_EOU_JX_WC_Q` (after insert or update or delete)

## DEFINITIONS.DEF_CPT_PROP_WORKFLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| NATURE_ID | VARCHAR2(3) default 'ALL' | N |  |
| NATURE_DETAIL_ID | VARCHAR2(3) default 'ALL' | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| WORKFLOW_TYPE_ID | NUMBER(3) | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

_No standard audit columns._

- **PK** `PK_DEF_CPT_PROP_WORKFLOW`: ORGANIZATION_ID, LOCATION_ID, NATURE_ID, NATURE_DETAIL_ID

## DEFINITIONS.DEF_DP_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(100) | N |  |
| DISPLAY_ORDER | NUMBER(2) | Y |  |
| FIX_VALUE | CHAR(1) default 'N' | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `DEF_DP_PARAMETER_PK`: PARAMETER_ID, ORGANIZATION_ID
- **Triggers**: `DEF_DP_PARAMETER_CEA` (before insert or update or delete), `DEF_DP_PARAMETER_DEL` (after delete), `DEF_DP_PARAMETER_INS` (before insert), `DEF_DP_PARAMETER_INSERT` (before insert), `DEF_DP_PARAMETER_UPD` (before update), `TRG_WS_VYO_NI_NQ_Q` (after insert or update or delete)

## DEFINITIONS.DEF_DP_PARAMETER_VALUE

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER(2) | N |  |
| PARAMETER_VALUE | VARCHAR2(100) | N |  |
| DISPLAY_ORDER | NUMBER(2) | Y |  |
| DEFAULT_VALUE | CHAR(1) default 'N' | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `DEF_DP_PARAMETER_VALUE_PK`: PARAMETER_ID, PARAMETER_VALUE, ORGANIZATION_ID
- **FK** `FK_DEF_DP_PARAMETER`: (PARAMETER_ID, ORGANIZATION_ID) -> DEFINITIONS.DEF_DP_PARAMETER(PARAMETER_ID, ORGANIZATION_ID) [disabled]
- **Triggers**: `DEF_DP_PARAMETER_VALUE_CEA` (before insert or update or delete), `DEF_DP_PARAMETER_VALUE_DEL` (after delete), `DEF_DP_PARAMETER_VALUE_INS` (before insert), `DEF_DP_PARAMETER_VALUE_INSERT` (before insert), `DEF_DP_PARAMETER_VALUE_UPD` (before update), `TRG_WS_OFY_MW_JW_Q` (after insert or update or delete)

## DEFINITIONS.DEF_ENCOUNTER_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| EN_CATEGORY_ID | VARCHAR2(6) | N |  |
| EN_CATEGORY_NAME | VARCHAR2(250) | N |  |
| EN_SHORT_DESC | VARCHAR2(50) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DEF_ENCOUNTER_CAT`: EN_CATEGORY_ID
- **UK** `UK_DEF_ENCOUNTER_CAT1`: EN_CATEGORY_NAME
- **Triggers**: `DEF_ENCOUNTER_CATEGORY_DEL` (after delete), `DEF_ENCOUNTER_CATEGORY_INS` (before insert), `DEF_ENCOUNTER_CATEGORY_UPD` (before update)

## DEFINITIONS.DEF_ENC_TREATMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER(4) | N |  |
| TREATMENT_NAME | VARCHAR2(50) | N |  |
| TREATMENT_DESC | VARCHAR2(500) | Y |  |
| IS_ACTIVE | CHAR(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_DEF_ENC_TREATMENT`: ID

## DEFINITIONS.DEF_FLAGS

| Column | Type | Null | Comment |
|---|---|---|---|
| FLAG_ID | VARCHAR2(5) | N |  |
| FLAG_DESC | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REVIEW_DURATION | NUMBER | Y | Review duration will be the first time when patient is marked and alert will appear after review duration, its value is in days |
| REPEAT_REVIEW_DURATION | NUMBER | Y | Repeat Review duration will be used to repear the duration, its value is in days |
| AUTO_REMOVAL_DURATION | NUMBER | Y | Review duration will be used to auto cancel the results, its value is in days |
| RESTRICT_REMOVAL_DURATION | NUMBER | Y | This column will be used to apply restriction to remove flag on Patient flag screen. It will be in days |

- **PK** `PK_FLAG`: FLAG_ID
- **Triggers**: `DEF_FLAGS_CEA` (before insert or update or delete), `DEF_FLAGS_DEL` (after delete), `DEF_FLAGS_INS` (before insert), `DEF_FLAGS_UPD` (before update), `TRG_WS_DYD_IX_SO_Q` (after insert or update or delete)

## DEFINITIONS.DEF_FLAGS_ALERT_ROLES

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N | SR# will be generated. |
| FLAG_ID | VARCHAR2(5) | N | Flag id i.e. COVID. |
| ROLE_ID | NUMBER(20) | Y | Role id against which alert will be generated. |
| ALERT | VARCHAR2(1) default 'N' | Y | Role alert flag will be used for alert. |
| REVIEW | VARCHAR2(1) default 'N' | Y | Role review flag will be used to review the alert. |
| ACTIVE | VARCHAR2(1) default 'N' | Y | Active/In-active. |

- **PK** `PK_FLAG_ROLES`: SR_NO, FLAG_ID
- **Triggers**: `DEF_FLAGS_ALERT_ROLES_CEA` (before insert or update or delete), `DEF_FLAGS_ALERT_ROLES_DEL` (after delete), `DEF_FLAGS_ALERT_ROLES_INS` (before insert), `DEF_FLAGS_ALERT_ROLES_UPD` (before update), `TRG_WS_XYC_JH_SL_Q` (after insert or update or delete)

## DEFINITIONS.DEF_INSTRUCTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| INSTRUCTION_ID | NUMBER | N |  |
| INSTRUCTION_PRE_TEXT | VARCHAR2(500) | Y |  |
| INSTRUCTION_POST_TEXT | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| INSTRUCTION_TYPE | VARCHAR2(1) | Y | S-> STATIC, D-> DYNAMIC (PARAMETERS WILL BE DEFINED) |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_DEF_INSTRUCTIONS`: INSTRUCTION_ID
- **Triggers**: `DEF_INSTRUCTIONS_CEA` (before insert or update or delete), `DEF_INSTRUCTIONS_DEL` (after delete), `DEF_INSTRUCTIONS_INS` (before insert), `DEF_INSTRUCTIONS_UPD` (before update), `TRG_WS_ELS_TW_KG_Q` (after insert or update or delete)

## DEFINITIONS.DEF_INSTRUCTIONS_LANG_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | Y |  |
| INSTRUCTION_ID | NUMBER | Y |  |
| LANGUAGE_ID | VARCHAR2(6) | Y |  |
| LABEL_DESC | NVARCHAR2(500) | Y |  |
| LABEL_DESC1 | NVARCHAR2(500) | Y |  |
| LABEL_DESC2 | NVARCHAR2(500) | Y |  |
| LABEL_DESC3 | NVARCHAR2(500) | Y |  |
| LABEL_DESC4 | NVARCHAR2(500) | Y |  |
| LABEL_DESC5 | NVARCHAR2(500) | Y |  |
| LABEL_DESC6 | NVARCHAR2(500) | Y |  |
| LABEL_DESC7 | NVARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **Triggers**: `DEF_INSTRUCTIONS_LANG_SETUP_CEA` (before insert or update or delete), `DEF_INST_LANG_SETUP_DEL` (after delete), `DEF_INST_LANG_SETUP_INS` (before insert), `DEF_INST_LANG_SETUP_UPD` (before update), `TRG_WS_XCW_YP_UI_Q` (after insert or update or delete)

## DEFINITIONS.DEF_MRN_TRAN_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRN_TYPE_ID | VARCHAR2(1) | N |  |
| DESCRIPTION | VARCHAR2(50) | N |  |
| TRANS_TYPE | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_DEF_MRN_TRAN_TYPE`: MRN_TYPE_ID
- **Triggers**: `DEF_MRN_TRAN_TYPE_CEA` (before insert or update or delete), `DEF_MRN_TRAN_TYPE_DEL` (after delete), `DEF_MRN_TRAN_TYPE_INS` (before insert), `DEF_MRN_TRAN_TYPE_UPD` (before update), `TRG_WS_OOI_MF_DA_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_CATEGORY_GROUP
This table will be used to define the Service Category Group e.g. CPT, Pharmacy, Consultation, Supplies etc. Data of this table is Constant

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_CATEGORY_GROUP_ID | VARCHAR2(3) | N | Counter of the Service Category Group which will start from 001, however this value is constant |
| DESCRIPTION | VARCHAR2(60) | N | Name of the Service Category Group |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_CATEGORY_GROUP`: SERVICE_CATEGORY_GROUP_ID
- **CHECK** `CK_SERVICE_CATEGORY_GROUP_1`: DESCRIPTION=UPPER(DESCRIPTION
- **CHECK** `CK_SERVICE_CATEGORY_GROUP_2`: ACTIVE IN ('Y','N'
- **CHECK** `CK_SERVICE_CATEGORY_GROUP_3`: ORG_ID='SKM'
- **Triggers**: `SERVICE_CATEGORY_GROUP_CEA` (before insert or update or delete), `SERVICE_CATEGORY_GROUP_DEL` (after delete), `SERVICE_CATEGORY_GROUP_INS` (before insert), `SERVICE_CATEGORY_GROUP_UPD` (before update), `TRG_WS_NQF_NK_UU_Q` (after insert or update or delete)

## DEFINITIONS.DEF_SERVICE_CATEGORY
This table will be used to define the Service Types e.g. CPT, Pharmacy, Consultation etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_CATEGORY_ID | VARCHAR2(3) | N | Counter of the Table which will start from 001 |
| DESCRIPTION | VARCHAR2(60) | N | Name of the Service Category |
| SERVICE_CATEGORY_GROUP_ID | VARCHAR2(3) | N | Service Category e.g. C for CPT, T for Consultation |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_DEF_SERVICE_CATEGORY`: SERVICE_CATEGORY_ID
- **FK** `FK_DEF_SERVICE_CATEGORY_1`: (SERVICE_CATEGORY_GROUP_ID) -> DEFINITIONS.SERVICE_CATEGORY_GROUP(SERVICE_CATEGORY_GROUP_ID) [disabled]
- **CHECK** `CK_DEF_SERVICE_CATEGORY_1`: ACTIVE IN ('Y','N'
- **Triggers**: `DEF_SERVICE_CATEGORY_CEA` (before insert or update or delete), `DEF_SERVICE_CATEGORY_DEL` (after delete), `DEF_SERVICE_CATEGORY_INS` (before insert), `DEF_SERVICE_CATEGORY_UPD` (before update), `TRG_WS_ZYZ_DG_TM_Q` (after insert or update or delete)

## DEFINITIONS.DEF_SYS_CONSTANTS_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_TYPE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_DEF_SYS_CONST_TYPE`: CONSTANT_TYPE_ID
- **Triggers**: `DEF_SYS_CONSTANTS_TYPE_CEA` (before insert or update or delete), `DEF_SYS_CONSTANTS_TYPE_DEL` (after delete), `DEF_SYS_CONSTANTS_TYPE_INS` (before insert), `DEF_SYS_CONSTANTS_TYPE_UPD` (before update), `TRG_WS_EYY_JF_UQ_Q` (after insert or update or delete)

## DEFINITIONS.DEF_TREATMENT_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| TR_CATEGORY_ID | VARCHAR2(6) | N |  |
| TR_CATEGORY_NAME | VARCHAR2(250) | N |  |
| TR_SHORT_DESC | VARCHAR2(50) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DEF_TREATMENT_CAT`: TR_CATEGORY_ID
- **UK** `UK_DEF_TREATMENT_CAT1`: TR_CATEGORY_NAME
- **UK** `UK_DEF_TREATMENT_CAT2`: TR_SHORT_DESC
- **Triggers**: `DEF_TREATMENT_CATEGORY_DEL` (after delete), `DEF_TREATMENT_CATEGORY_INS` (before insert), `DEF_TREATMENT_CATEGORY_UPD` (before update)

## DEFINITIONS.DEF_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| VALUE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_DEF_VALUES`: VALUE_ID
- **UK** `UK_DEF_VALUES_001`: DESCRIPTION
- **UK** `UK_DEF_VALUES_002`: SHORT_DESC
- **Triggers**: `DEF_VALUES_DEL` (after delete), `DEF_VALUES_INS` (before insert), `DEF_VALUES_UPD` (before update)

## DEFINITIONS.DEF_YEARS

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(4) | N |  |

- **PK** `DEF_YEAR_PK_1`: YEAR_ID
- **UK** `DEF_YEAR_UK_1`: DESCRIPTION

## DEFINITIONS.DELAYED_APPT_FORWARD_TO_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(3) | N |  |
| GROUP_ID | VARCHAR2(10) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |


## DEFINITIONS.DELAY_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(500) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| TRANSACTION_TYPE | VARCHAR2(10) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| REMARKS_REQUIRED | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_DELAY_REASONS`: REASON_ID
- **Triggers**: `DELAY_REASONS_CEA` (before insert or update or delete), `DELAY_REASONS_DEL` (after delete), `DELAY_REASONS_INS` (before insert), `DELAY_REASONS_UPD` (before update), `TRG_WS_ABL_FH_JS_Q` (after insert or update or delete)

## DEFINITIONS.DEL_R

| Column | Type | Null | Comment |
|---|---|---|---|
| VAL | VARCHAR2(3000) | Y |  |


## DEFINITIONS.DEPARTMENTAL_HOLIDAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| HOLIDAY_ID | NUMBER | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| HOLIDAY_DATE | DATE | Y |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DEPARTMENTAL_HOLIDAYS`: HOLIDAY_ID
- **UK** `UK_DEPARTMENTAL_HOLIDAYS`: ORGANIZATION_ID, LOCATION_ID, DEPARTMENT_ID, HOLIDAY_DATE
- **FK** `FK_DEPARTMENTAL_HOLIDAYS_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID)
- **FK** `FK_DEPARTMENTAL_HOLIDAYS_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_DEPARTMENTAL_HOLIDAYS_3`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **Triggers**: `DEPARTMENTAL_HOLIDAYS_DEL` (after delete), `DEPARTMENTAL_HOLIDAYS_INS` (before insert), `DEPARTMENTAL_HOLIDAYS_UPD` (before update)

## DEFINITIONS.DEPARTMENT_NATURE_ARCHIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| NATURE_ID | VARCHAR2(3) | N | This column contains inforamation department Nature ID (reference: DEFINITIONS.DEPARTMENT_NATURE) |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y | This column contains Detail ID of department Nature ID (Unique Nature+Serial) |
| DOCUMENT_TYPE_ID | NUMBER | Y | This column contains document TYPE id from HRD.DOCUMENT_TYPE table |
| DOCUMENT_ID | VARCHAR2(13) | Y | Year based Unique document ID from LOB.DOCUMENTS_STORE |
| REMARKS | VARCHAR2(2000) | Y | other comments about document |
| ATTACHED_BY | VARCHAR2(14) | Y | MRNO who attached file |
| ACTIVE | CHAR(1) default 'N' | Y | For active 'Y' and 'N' for inactive |
| SRNO | NUMBER | N | Serial Number |
| ATTACHED_DATE | DATE | Y | Storage Date and Time when DOCUMENT is attached |

- **PK** `PK_NATURE_ARCH`: NATURE_ID, SRNO
- **Triggers**: `DEPARTMENT_NATURE_ARCHIVE_DEL` (after delete), `DEPARTMENT_NATURE_ARCHIVE_INS` (before insert), `DEPARTMENT_NATURE_ARCHIVE_UPD` (before update)

## DEFINITIONS.DEPARTMENT_SECRATORY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECRATORY_MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DEPARTMENT_SECRATORY`: DEPARTMENT_ID, SECRATORY_MRNO
- **FK** `FK_DEPARTMENT_SECRATORY`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **Triggers**: `DEPARTMENT_SECRATORY_DEL` (after delete), `DEPARTMENT_SECRATORY_INS` (before insert), `DEPARTMENT_SECRATORY_UPD` (before update)

## DEFINITIONS.DEPARTMENT_WISE_CPTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_DEPARTMENT_WISE_CPTS_01`: CPT_ID, DEPARTMENT_ID

## DEFINITIONS.DEPARTMENT_WISE_ROLE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ROLE_ID | NUMBER(10) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DEPT_WISE_ROLE_SETUP`: SR_NO
- **UK** `UK_DEPT_WISE_ROLE_SETUP`: DEPARTMENT_ID, ROLE_ID
- **FK** `FK_DEPT_WISE_ROLE_SETUP`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **Triggers**: `DEPARTMENT_ROLE_SETUP_INSERT` (before insert), `DEPARTMENT_WISE_ROLE_SETUP_DEL` (after delete), `DEPARTMENT_WISE_ROLE_SETUP_INS` (before insert), `DEPARTMENT_WISE_ROLE_SETUP_UPD` (before update)

## DEFINITIONS.DEPENDENT_WISE_RELATION

| Column | Type | Null | Comment |
|---|---|---|---|
| RELATION_ID | VARCHAR2(6) | N |  |
| MRNO | VARCHAR2(14) | Y |  |
| DEPENDENT_MRNO | VARCHAR2(14) | N |  |
| AGE | NUMBER | Y |  |
| VALIDITY_DURATION | NUMBER(5,1) | Y |  |
| VALIDITY_DURATION_UNIT_ID | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MEDICAL_ALLOWED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `DEPENDENT_WISE_RELATION_PK`: RELATION_ID, DEPENDENT_MRNO
- **Triggers**: `DEPENDENT_WISE_RELATION_DEL` (after delete), `DEPENDENT_WISE_RELATION_INS` (before insert), `DEPENDENT_WISE_RELATION_UPD` (before update)

## DEFINITIONS.DESIGNATION_CAREER_PATH_R

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CAREER_ID | VARCHAR2(6) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| REQUIRED_EXPERIENCE_IN_YEARS | NUMBER | Y |  |
| CAREER_LEVEL | NUMBER | Y |  |


## DEFINITIONS.DESIGNATION_EXPERTISE

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| SKILL_ID | NUMBER | N |  |
| SKILL_LEVEL | VARCHAR2(30) | Y |  |

- **PK** `PK_DESIGNATION_EXPERTISE`: DESIGNATION_ID, SKILL_ID
- **Triggers**: `DESIGNATION_EXPERTISE_CEA` (before insert or update or delete), `TRG_WS_YSQ_HL_DM_Q` (after insert or update or delete)

## DEFINITIONS.DESIGNATION_ROLE

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ROLE_ID | NUMBER(10) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| PRIMARY_ROLE | CHAR(1) default 'N' | Y | 'N' for None, 'C' for Clinical, 'A' for Administrative, 'G' for General |

- **PK** `PK_DESIGNATION_ROLE`: DESIGNATION_ID, ROLE_ID
- **FK** `FK_DESIGNATION_ROLE_1`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID)
- **FK** `FK_DESIGNATION_ROLE_2`: (ROLE_ID) -> SECURITY.ROLE(ROLE_ID) [disabled]
- **CHECK** `CHK_USER_ROLE_1`: PRIMARY_ROLE IN ('N','C','A','G'
- **Triggers**: `DESIGNATION_ROLE_CEA` (before insert or update or delete), `DESIGNATION_ROLE_DEL` (after delete), `DESIGNATION_ROLE_DELETE` (before delete), `DESIGNATION_ROLE_INS` (before insert), `DESIGNATION_ROLE_UPD` (before update), `TRG_WS_WCJ_HB_RZ_Q` (after insert or update or delete)

## DEFINITIONS.DESIGNATION_STRUCTURE

| Column | Type | Null | Comment |
|---|---|---|---|
| STRUCTURE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

_No standard audit columns._


## DEFINITIONS.DESIGNATION_WISE_CPTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_DESIGNATION_WISE_CPTS_01`: CPT_ID, DESIGNATION_ID

## DEFINITIONS.DESIGNATION_WISE_CPTS_EXEMPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_DESIGNATION_WISE_CPTS_EXEMPT_01`: CPT_ID, DESIGNATION_ID

## DEFINITIONS.DESIGNATION_WISE_PRIVILEGES

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| DESIGNATION_ID | VARCHAR2(7) | Y |  |
| PRIVILEGES_ID | NUMBER | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| DOCUMENT_ID | VARCHAR2(13) | Y |  |
| DISPLAY | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ATTACHED_BY | VARCHAR2(14) | Y |  |
| ATTACHED_DATE | DATE | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ON_PROBATION | CHAR(1) default 'N' | Y | Either Y or N |

- **PK** `PK_SR_DESIG_W_P`: SR_NO
- **UK** `UK_PRIV_DESIG_ON_PROBATION`: DESIGNATION_ID, PRIVILEGES_ID, ON_PROBATION, LOCATION_ID
- **FK** `FK_DOCUMENT_ID`: (DOCUMENT_ID) -> LOB.DOCUMENTS_STORE(DOCUMENT_ID) [disabled]
- **Triggers**: `DESIG_WISE_PRIVILEGES_DEL` (after delete), `DESIG_WISE_PRIVILEGES_INS` (before insert), `DESIG_WISE_PRIVILEGES_UPD` (before update)

## DEFINITIONS.DESIGNATION_WISE_RFID_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | NUMBER(5) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DESIG_WISE_RFID_CATEGORY`: CATEGORY_ID, DESIGNATION_ID
- **FK** `FK_DESIG_WISE_RFID_CATEGORY`: (CATEGORY_ID) -> RFID.RFID_CATEGORY(CATEGORY_ID)
- **FK** `FK_DESIG_WISE_RFID_CATEGORY_02`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **Triggers**: `DESIG__RFID_CAT_DEL` (after delete), `DESIG__RFID_CAT_INS` (before insert), `DESIG__RFID_CAT_UPD` (before update)

## DEFINITIONS.DESIG_CATEGOTY_WISE_CPTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| CATEGORY_ID | VARCHAR2(3) | N |  |
| DESIGNATION_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_DESIG_CATEGOTY_WISE_CPTS_01`: CPT_ID, CATEGORY_ID, DESIGNATION_ID

## DEFINITIONS.DESIG_CAT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N |  |
| SUB_DESIG_CAT_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DESIG_CAT_DETAIL`: DESIGNATION_CATEGORY_ID, SUB_DESIG_CAT_ID
- **FK** `FK_DESIG_CAT_DETAIL_1`: (DESIGNATION_CATEGORY_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID)
- **FK** `FK_DESIG_CAT_DETAIL_2`: (SUB_DESIG_CAT_ID) -> DEFINITIONS.DESIGNATION_CATEGORY(DESIGNATION_CATEGORY_ID) [disabled]

## DEFINITIONS.DESIG_SPECIALITY_PRIVILEGES

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N | Clinical Speciality ID from DEFINITIONS.CLINIC_SPECIALITY |
| DESIGNATION_ID | VARCHAR2(6) | N | Designation ID from DEFINITIONS.DESIGNATION |
| ON_PROBATION | CHAR(1) default 'N' | N | Either Y or N |
| PRIVILEGES_ID | NUMBER | Y | Privileges ID from DEFINITIONS.CONSULTANT_PRIVILEGES_SETUP |
| DOCUMENT_ID | VARCHAR2(13) | Y | DOCUMENT_ID from LOB.DOCUMENTS_STORE |
| DISPLAY | CHAR(1) | Y | Either Privilege Document should display or Not |
| ACTIVE | CHAR(1) | Y | Either Y or N |
| ATTACHED_BY | VARCHAR2(14) | Y | USER_ID who aatcahed Document |
| ATTACHMENT_DATE | DATE | Y | Date on which document was attached |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| LOCATION_ID | VARCHAR2(3) default '001' | Y |  |
| SERIAL_NO | NUMBER(8) | N |  |

- **PK** `PK_DESIG_SPECIALITY_PRIVILEGES`: SERIAL_NO
- **FK** `FK_DESIG_SPECIALITY_PRIV_1`: (CLINIC_SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID) [disabled]
- **FK** `FK_DESIG_SPECIALITY_PRIV_2`: (PRIVILEGES_ID) -> DEFINITIONS.CONSULTANT_PRIVILEGES_SETUP(PRIVILEGES_ID) [disabled]
- **FK** `FK_DESIG_SPECIALITY_PRIV_3`: (DOCUMENT_ID) -> LOB.DOCUMENTS_STORE(DOCUMENT_ID) [disabled]
- **FK** `FK_DESIG_SPECIALITY_PRIV_4`: (ATTACHED_BY) -> HRD.INFORMATION(MRNO) [disabled]
- **FK** `FK_DESIG_SPECIALITY_PRIV_5`: (DESIGNATION_ID) -> DEFINITIONS.DESIGNATION(DESIGNATION_ID) [disabled]
- **CHECK** `CHK_DESIG_SPECIALITY_PRIV_1`: ACTIVE IN ('Y','N'
- **CHECK** `CHK_DESIG_SPECIALITY_PRIV_2`: ON_PROBATION IN ('Y','N'
- **CHECK** `CHK_DESIG_SPECIALITY_PRIV_3`: DISPLAY IN ('Y','N'
- **Triggers**: `DESIG_SPLY_PRIVILEGES_DEL` (after delete), `DESIG_SPLY_PRIVILEGES_INS` (before insert), `DESIG_SPLY_PRIVILEGES_UPD` (before update)

## DEFINITIONS.DETAIL_TEMPLATE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| PARAMETER_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DTS`: TEMPLATE_ID, PARAMETER_ID
- **Triggers**: `DETAIL_TEMPLATE_SETUP_DEL` (after delete), `DETAIL_TEMPLATE_SETUP_INS` (before insert), `DETAIL_TEMPLATE_SETUP_UPD` (before update)

## DEFINITIONS.DEVELOPERS

| Column | Type | Null | Comment |
|---|---|---|---|
| DEVELOPER_ID | VARCHAR2(14) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SUPERVISOR | CHAR(1) | Y |  |

- **PK** `PK_DEVELOPERS`: DEVELOPER_ID
- **Triggers**: `DEVELOPERS_CEA` (before insert or update or delete), `TRG_WS_NTW_LI_XI_Q` (after insert or update or delete)

## DEFINITIONS.DEVICE_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| DEVICE_CATEGORY_ID | NUMBER(3) | N |  |
| DEVICE_NAME | VARCHAR2(60) | N |  |
| DETAIL_DESCRIPTION | VARCHAR2(150) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(30) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_DEVICE_CATEGORY_1`: DEVICE_CATEGORY_ID
- **Triggers**: `DEVICE_CATEGORY_CEA` (before insert or update or delete), `TRG_WS_QPY_CG_UR_Q` (after insert or update or delete)

## DEFINITIONS.DIAGNOSIS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIAGNOSIS_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) | N |  |
| PRIMARY_REGIMENS | NUMBER(2) default 0 | N |  |
| RELAPSED_REGIMENS | NUMBER(2) default 0 | N |  |
| ICD_ID | VARCHAR2(11) | Y |  |
| PATIENT_TO_BE_EXAMINED_BY | CHAR(1) | N | IT MAY CONTAIN VALUES LIKE R/F/O "R" FOR RESIDENT, "F" FOR FELLOW AND "O" FOR ONCOLOGIST |

- **PK** `PK_DIAGNOSIS`: DIAGNOSIS_ID
- **CHECK** `CK_DIAGNOSIS_1`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_DIAGNOSIS_2`: PATIENT_TO_BE_EXAMINED_BY IN ('R','F','O'
- **Triggers**: `DIAGNOSIS_CEA` (before insert or update or delete), `DIAGNOSIS_DEL` (after delete), `DIAGNOSIS_INS` (before insert), `DIAGNOSIS_UPD` (before update), `TRG_WS_DWE_KO_OV_Q` (after insert or update or delete)

## DEFINITIONS.DIAGNOSIS_REPORT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER | N |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| HEADING_LABEL | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_DIAGNOSIS_REPORT_SETUP`: SETUP_ID
- **FK** `FK_D_REPORT_SETUP_01`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]

## DEFINITIONS.ICD

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO | VARCHAR2(11) | N |  |
| ICD_NO | VARCHAR2(11) | Y |  |
| SHORT_EQUAL | VARCHAR2(1) | Y |  |
| ICD_NO_4 | VARCHAR2(5) | Y |  |
| ICD_NO_3 | VARCHAR2(3) | Y |  |
| ESTIMATED_COST | NUMBER(10,2) | Y |  |
| ESTIMATED_DURATION | NUMBER(4) | Y |  |
| ADDITIONAL_ICD | VARCHAR2(1) default 'N' | N |  |
| LONG_DESC | VARCHAR2(250) | N |  |
| ICD_CHAPTER_ID | VARCHAR2(3) | Y |  |
| ICD_GROUP_ID | VARCHAR2(3) | Y |  |
| ICDO_3_DESC | VARCHAR2(45) | Y |  |
| ICD_TYPE | VARCHAR2(25) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ICDNO_FOR_CANCER | CHAR(1) default 'N' | N |  |
| BACK_GROUND_DIAGNOSIS | CHAR(1) default 'N' | N |  |
| FU_FOR_LIFE | CHAR(1) | Y | Y mean for life time follow up treatment |
| VERSION | NUMBER(2) | N |  |
| ICD10_SERIAL_NO | VARCHAR2(10) | N |  |
| ICD_O3 | CHAR(1) | Y | Y mean ICD for O3 and N mean ICD not for O3 |
| REPORTABLE | CHAR(1) default 'N' | N | Y mean Reportable & N mean not Reportable |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ICD_1`: ICDNO, VERSION, LOCATION_ID
- **CHECK** `CHECK_ICD`: ADDITIONAL_ICD IN ('Y','N'
- **CHECK** `CHECK_ICD_1`: ACTIVE IN ('Y','N'
- **CHECK** `CHK_ICD_TYPE`: ICD_TYPE IN ('SURGICAL PROCEDURE','DIAGNOSTIC CODE','PROCEDURE','E CODE','V CODE'))
- **CHECK** `CK_ICD_001`: ICDNO_FOR_CANCER IN ('N','Y'
- **Triggers**: `ICD_CEA` (before insert or update or delete), `ICD_DEL` (after delete), `ICD_INS` (before insert), `ICD_INSRT` (before insert), `ICD_UPD` (before update), `MAINTAIN_ICD_VERSION_HISTORY` (after update of long_desc), `TRG_WS_RNV_BL_VA_Q` (after insert or update or delete)

## DEFINITIONS.DIAGNOSIS_REPORT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER | N |  |
| ICDNO | VARCHAR2(11) | N |  |
| VERSION | NUMBER(2) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_FK_D_REPORT_DET_0`: SETUP_ID, ICDNO, VERSION, LOCATION_ID
- **FK** `FK_D_REPORT_DET_01`: (SETUP_ID) -> DEFINITIONS.DIAGNOSIS_REPORT_SETUP(SETUP_ID)
- **FK** `FK_D_REPORT_DET_02`: (ICDNO, VERSION, LOCATION_ID) -> DEFINITIONS.ICD(ICDNO, VERSION, LOCATION_ID) [disabled]

## DEFINITIONS.DIAGNOSIS_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIAGNOSIS_STATUS_ID | VARCHAR2(1) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| DETAILS | VARCHAR2(200) | Y |  |
| RESTRICT_ORAL_CHEMO | VARCHAR2(1) default 'N' | Y | Y => Restrict user to Prescribe Oral Chemo Drug , N => No restriction |

- **PK** `PK_DS`: DIAGNOSIS_STATUS_ID
- **Triggers**: `DIAGNOSIS_STATUS_CEA` (before insert or update or delete), `DIAGNOSIS_STATUS_DEL` (after delete), `DIAGNOSIS_STATUS_INS` (before insert), `DIAGNOSIS_STATUS_UPD` (before update), `TRG_WS_FNG_TB_MD_Q` (after insert or update or delete)

## DEFINITIONS.DIAGNOSIS_STATUS_CONVERSION

| Column | Type | Null | Comment |
|---|---|---|---|
| DIAGNOSIS_STATUS_ID | VARCHAR2(1) | N |  |
| CONVERTABLE_TO_DIAGNOSIS | VARCHAR2(1) | N |  |
| PURPOSE | VARCHAR2(30) | N |  |

- **PK** `PK_DIAGNOSIS_STATUS_CONVERSION`: DIAGNOSIS_STATUS_ID, CONVERTABLE_TO_DIAGNOSIS, PURPOSE
- **Triggers**: `DIAGNOSIS_STATUS_CONVERSION_CEA` (before insert or update or delete), `TRG_WS_QOT_HS_EO_Q` (after insert or update or delete)

## DEFINITIONS.PHONE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PHONE_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| FLAG | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| IS_SMS_ALLOW | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PHONE_TYPE`: PHONE_TYPE_ID
- **UK** `UK_PHONE_TYPE_1`: DESCRIPTION
- **CHECK** `CHK_PHONE_TYPE_1`: ACTIVE IN ('N','Y'
- **CHECK** `CK_PHONE_TYPE_001`: FLAG IN ('C','A'
- **Triggers**: `PHONE_TYPE_CEA` (before insert or update or delete), `PHONE_TYPE_DEL` (after delete), `PHONE_TYPE_INS` (before insert), `PHONE_TYPE_UPD` (before update), `TRG_WS_ALS_RD_TG_Q` (after insert or update or delete)

## DEFINITIONS.DIALING_CODES

| Column | Type | Null | Comment |
|---|---|---|---|
| CITY | VARCHAR2(200) | Y |  |
| CODE_NUMBER | VARCHAR2(20) | N |  |
| PHONE_TYPE_ID | VARCHAR2(5) | N |  |
| COUNTRY_CALLING_CODE | VARCHAR2(5) default 92 | N |  |
| PHONE_DIGITS | NUMBER(2) | Y |  |

- **PK** `PK_DIALING_CODES`: CODE_NUMBER, COUNTRY_CALLING_CODE
- **FK** `FK_DIALING_CODES_01`: (PHONE_TYPE_ID) -> DEFINITIONS.PHONE_TYPE(PHONE_TYPE_ID) [disabled]
- **Triggers**: `DIALING_CODES_CEA` (before insert or update or delete), `DIALING_CODES_DEL` (after delete), `DIALING_CODES_INS` (before insert), `DIALING_CODES_UPD` (before update), `TRG_WS_KQY_CV_ZU_Q` (after insert or update or delete)

## DEFINITIONS.DIET_PRECAUTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| PRECAUTION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DIET_PRECAUTIONS`: PRECAUTION_ID
- **Triggers**: `DIET_PRECAUTIONS_DEL` (after delete), `DIET_PRECAUTIONS_INS` (before insert), `DIET_PRECAUTIONS_UPD` (before update)

## DEFINITIONS.DIFFERENTIATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DIFF_CODE | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ICDO_3_GRADE | VARCHAR2(10) | Y |  |
| ICDO_3_DESC | VARCHAR2(60) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DIFFERENTIATION`: DIFF_CODE, LOCATION_ID
- **Triggers**: `DIFFERENTIATION_CEA` (before insert or update or delete), `DIFFERENTIATION_DEL` (after delete), `DIFFERENTIATION_INS` (before insert), `DIFFERENTIATION_INSRT` (before insert), `DIFFERENTIATION_UPD` (before update), `TRG_WS_IXY_KU_ER_Q` (after insert or update or delete)

## DEFINITIONS.DISCARD_METHOD

| Column | Type | Null | Comment |
|---|---|---|---|
| METHOD_ID | VARCHAR2(7) | N |  |
| METHOD_DESC | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_DISCARD_METHOD`: METHOD_ID
- **Triggers**: `DISCARD_METHOD_DEL` (after delete), `DISCARD_METHOD_INS` (before insert), `DISCARD_METHOD_UPD` (before update)

## DEFINITIONS.DISCHARGE_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| DISCHARGE_STATUS_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| VITAL_SIGN_IN_EAR | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_DISCHARGE_STATUS`: DISCHARGE_STATUS_ID, LOCATION_ID
- **Triggers**: `DISCHARGE_STATUS_CEA` (before insert or update or delete), `DISCHARGE_STATUS_DEL` (after delete), `DISCHARGE_STATUS_INS` (before insert), `DISCHARGE_STATUS_UPD` (before update), `TRG_WS_PNH_WE_HH_Q` (after insert or update or delete)

## DEFINITIONS.DISCIPLINARY_ACTION

| Column | Type | Null | Comment |
|---|---|---|---|
| DISCIPLINARY_ACTION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N |  |

- **PK** `PK_DISCIPLINARY_ACTION`: DISCIPLINARY_ACTION_ID
- **Triggers**: `DISCIPLINARY_ACTION_CEA` (before insert or update or delete), `DISCIPLINARY_ACTION_DEL` (after delete), `DISCIPLINARY_ACTION_INS` (before insert), `DISCIPLINARY_ACTION_UPD` (before update), `TRG_WS_BHN_XR_TO_Q` (after insert or update or delete)

## DEFINITIONS.DISCIPLINARY_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| DISCIPLINARY_REASON_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| TERMINATION | VARCHAR2(1) default 'N' | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N |  |

- **PK** `PK_DISCIPLINARY_REASON`: DISCIPLINARY_REASON_ID
- **Triggers**: `DISCIPLINARY_REASON_CEA` (before insert or update or delete), `DISCIPLINARY_REASON_DEL` (after delete), `DISCIPLINARY_REASON_INS` (before insert), `DISCIPLINARY_REASON_UPD` (before update), `TRG_WS_ITN_SH_SB_Q` (after insert or update or delete)

## DEFINITIONS.DISEASES

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_ID | NUMBER(6) | N |  |
| DISEASE_NAME | VARCHAR2(300) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| DISEASE_GROUP_ID | NUMBER(4) | Y |  |
| DISEASE_TYPE | VARCHAR2(1) | Y | Y = CANCER, N = NON CANCER, Q = QUERY CANCER,U = UNDIAGNOSED |
| DISEASES_CATEGORY | NUMBER(2) | Y | 1 = Cancer Patient, 2=Non Cancer Patient, 3=Indigent Patient, 4= LOU Patient,  5= Query Cancer, 6=Undiagnosed |

- **PK** `PK_DISEASES`: DISEASE_ID
- **CHECK** `CHK_DISEASES_ACTIVE`: ACTIVE IN ('Y','N'
- **Triggers**: `DISEASES_CEA` (before insert or update or delete), `DISEASES_DEL` (after delete), `DISEASES_INS` (before insert), `DISEASES_UPD` (before update), `TRG_WS_WUL_UK_FZ_Q` (after insert or update or delete)

## DEFINITIONS.DISEASE_AGE_LIMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_ID | NUMBER(6) | N |  |
| FROM_AGE | NUMBER(3) | N |  |
| TO_AGE | NUMBER(3) | N |  |
| RESTRICTED_FLAG | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DISEASE_AGE_LIMIT`: DISEASE_ID, FROM_AGE, TO_AGE
- **FK** `FK_DISEASE_AGE_LIMIT_1`: (DISEASE_ID) -> DEFINITIONS.DISEASES(DISEASE_ID)
- **CHECK** `CHK_DIEASE_AGE_LIMIT`: RESTRICTED_FLAG IN ('N','Y'
- **Triggers**: `DISEASE_AGE_LIMIT_DEL` (after delete), `DISEASE_AGE_LIMIT_INS` (before insert), `DISEASE_AGE_LIMIT_UPD` (before update)

## DEFINITIONS.DISEASE_FLOWSHEET_PARAMS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIS_FLWSH_PARAM_ID | VARCHAR2(10) | N |  |
| PARAM_NAME | VARCHAR2(200) | N |  |
| SHORT_CODE | VARCHAR2(20) | N |  |
| PARAM_DESCRIPTION | VARCHAR2(500) | N |  |
| ACTIVE_FLAG | CHAR(1) default 'N' | N |  |
| RESTRICT_MANUAL_ENTRY | CHAR(1) default 'N' | Y |  |
| SELECT_CLAUSE | VARCHAR2(2000) | Y |  |
| FROM_CLAUSE | VARCHAR2(2000) | Y |  |
| WHERE_CLAUSE | VARCHAR2(2000) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| CATEGORY_CODE | VARCHAR2(6) | Y |  |
| ORDER_BY | NUMBER | N |  |
| PATH_PARAMETER_ID | VARCHAR2(100) | Y |  |
| PATH_TEST_ID | VARCHAR2(100) | Y |  |
| NOTE_CLAUSE | VARCHAR2(2000) | Y |  |
| PARAM_TYPE | VARCHAR2(200) | Y |  |

- **PK** `PK_DIS_FLWSH_PARAMS`: DIS_FLWSH_PARAM_ID
- **UK** `UK_PARAM_NAME`: DIS_FLWSH_PARAM_ID, PARAM_NAME, CATEGORY_CODE
- **FK** `FK_CATEGORY_CODE`: (CATEGORY_CODE) -> ICU.SCORE_PARAMETERS(SCORE_PARAMETER_ID) [disabled]
- **Triggers**: `DISEASE_FLOWSHEET_PARAMS_DEL` (after delete), `DISEASE_FLOWSHEET_PARAMS_INS` (before insert), `DISEASE_FLOWSHEET_PARAMS_UPD` (before update)

## DEFINITIONS.DISEASE_FLOWSHEET_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| FLWSH_SETUP_ID | VARCHAR2(10) | N |  |
| DISEASE_ID | NUMBER | Y |  |
| SETUP_NAME | VARCHAR2(200) | Y |  |
| SETUP_DESCRIPTION | VARCHAR2(500) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE_FLAG | CHAR(1) default 'Y' | Y |  |
| SETUP_USER_MRNO | VARCHAR2(14) | Y |  |
| DEFAULT_FLAG | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DISEASE_FLOWSHEET_SETUP`: FLWSH_SETUP_ID
- **UK** `UK_SETUP_NAME`: SETUP_NAME, SETUP_USER_MRNO
- **Triggers**: `DISEASE_FLOWSHEET_SETUP_DEL` (after delete), `DISEASE_FLOWSHEET_SETUP_INS` (before insert), `DISEASE_FLOWSHEET_SETUP_UPD` (before update)

## DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST

| Column | Type | Null | Comment |
|---|---|---|---|
| FLWSH_SETUP_ID | VARCHAR2(10) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CUST_USER_MRNO | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CUST_FLWSH_SETUP_ID | VARCHAR2(10) | N |  |

- **PK** `PK_DIS_FLWSH_SETUP_CUST`: CUST_FLWSH_SETUP_ID
- **Triggers**: `DIS_FLOWSHEET_SETUP_CUST_DEL` (after delete), `DIS_FLOWSHEET_SETUP_CUST_INS` (before insert), `DIS_FLOWSHEET_SETUP_CUST_UPD` (before update)

## DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_FLOW_TRX_ID | VARCHAR2(12) | N |  |
| DIS_FLWSH_PARAM_ID | VARCHAR2(10) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| REPORT_DATE | DATE | N |  |
| RESULT_VALUE | VARCHAR2(2000) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ASSIGNMENT_ID | VARCHAR2(10) | Y |  |
| USER_MRNO | VARCHAR2(14) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_DISEASE_FLOWSHEET_TRN`: DISEASE_FLOW_TRX_ID
- **UK** `UK_DIS_FLWSH_PARAM_ID`: DIS_FLWSH_PARAM_ID, REPORT_DATE, USER_MRNO, MRNO
- **Triggers**: `DIS_FLOWSHEET_TRAN_DEL` (after delete), `DIS_FLOWSHEET_TRAN_INS` (before insert), `DIS_FLOWSHEET_TRAN_UPD` (before update), `TRG_WS_ATS_GH_ZB_Q` (after insert or update or delete)

## DEFINITIONS.DISEASE_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_GROUP_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DISEASE_GROUP`: DISEASE_GROUP_ID
- **CHECK** `CHK_DISEASE_GROUP_ACTIVE`: ACTIVE IN ('Y','N'

## DEFINITIONS.DISPENSARY

| Column | Type | Null | Comment |
|---|---|---|---|
| DISPENSARY_ID | VARCHAR2(6) | N |  |
| DISPENSARY_DES | VARCHAR2(255) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DISPENSARY`: DISPENSARY_ID
- **Triggers**: `DISPENSARY_INS` (before insert)

## DEFINITIONS.DISPLAY_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | NUMBER | N |  |
| TYPE_DESC | VARCHAR2(50) | Y |  |

- **PK** `PK_DISPLAY_TYPE`: TYPE_ID
- **Triggers**: `DISPLAY_TYPE_DEL` (after delete), `DISPLAY_TYPE_INS` (before insert), `DISPLAY_TYPE_UPD` (before update)

## DEFINITIONS.DISTRICT_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| OFFICE_ID | NUMBER(3) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_COUNTRY_ID | NUMBER(4) | Y |  |

- **PK** `PK_DISTRICT_ZONES`: ZONE_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID

## DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| ARCHIVE_ID | NUMBER | N |  |
| DISEASE_FLOW_TRX_ID | NUMBER | N |  |
| DOC_SR_NO | VARCHAR2(11) | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| MRNO | VARCHAR2(14) | N |  |
| DOC_ARCHIVE_DATE | DATE | N |  |
| DOC_ARCHIVER_ID | VARCHAR2(14) | Y |  |
| DOC_ARCHIVE_LOC_ID | NUMBER | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_DIS_FLWSH_DOC_ARCHIVE`: ARCHIVE_ID
- **UK** `UK_DIS_FLWSH_DOC_ARCHIVE`: DOC_SR_NO, MRNO, DOC_ARCHIVE_DATE, DISEASE_FLOW_TRX_ID
- **Triggers**: `DIS_FLWSH_DOC_ARCHIVE_DEL` (after delete), `DIS_FLWSH_DOC_ARCHIVE_INS` (before insert), `DIS_FLWSH_DOC_ARCHIVE_UPD` (before update)

## DEFINITIONS.DIS_FLWSH_PARAM_ASSG

| Column | Type | Null | Comment |
|---|---|---|---|
| FLWSH_SETUP_ID | VARCHAR2(10) | Y |  |
| DIS_FLWSH_PARAM_ID | VARCHAR2(10) | Y |  |
| RESTRICT_MANUAL_ENTRY | CHAR(1) | Y |  |
| ACTIVE_FLAG | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ASSIGNMENT_ID | VARCHAR2(10) | N |  |
| LOCATION_ID | VARCHAR2(3) default 001 | N |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_DIS_FLWSH_PARAM_ASSG`: ASSIGNMENT_ID, LOCATION_ID
- **UK** `UK_DIS_FLWSH_PARAM_ASSG`: FLWSH_SETUP_ID, DIS_FLWSH_PARAM_ID
- **Triggers**: `DIS_FLWSH_PARAM_ASSG_DEL` (after delete), `DIS_FLWSH_PARAM_ASSG_INS` (before insert), `DIS_FLWSH_PARAM_ASSG_UPD` (before update)

## DEFINITIONS.DIS_FLWSH_PARAM_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| DIS_FLWSH_PARAM_ID | VARCHAR2(10) | N |  |
| LAST_REFRESH_DATE | DATE | Y |  |
| REFERENCE_KEY | VARCHAR2(100) | Y |  |
| PARAM_TYPE | VARCHAR2(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `DIS_FLWSH_PARAM_MASTER_PK`: MRNO, DIS_FLWSH_PARAM_ID, PARAM_TYPE, LOCATION_ID
- **Triggers**: `DIS_FLWSH_PARAM_MASTER_DEL` (after delete), `DIS_FLWSH_PARAM_MASTER_INS` (before insert), `DIS_FLWSH_PARAM_MASTER_UPD` (before update)

## DEFINITIONS.DIS_FLWSH_PARAM_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| RESULT_VALUE | VARCHAR2(4000) | Y |  |
| RESULT_DATE | DATE | N |  |
| DIS_FLWSH_PARAM_ID | VARCHAR2(10) | N |  |
| REFERENCE_KEY | VARCHAR2(100) | N |  |
| PARAM_TYPE | VARCHAR2(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `DIS_FLWSH_PARAM_DETAIL_PK`: MRNO, DIS_FLWSH_PARAM_ID, PARAM_TYPE, RESULT_DATE
- **FK** `DIS_FLWSH_PARAM_DETAIL_FK`: (MRNO, DIS_FLWSH_PARAM_ID, PARAM_TYPE, LOCATION_ID) -> DEFINITIONS.DIS_FLWSH_PARAM_MASTER(MRNO, DIS_FLWSH_PARAM_ID, PARAM_TYPE, LOCATION_ID) [disabled]
- **Triggers**: `DIS_FLWSH_PARAM_DETAIL_DEL` (after delete), `DIS_FLWSH_PARAM_DETAIL_INS` (before insert), `DIS_FLWSH_PARAM_DETAIL_UPD` (before update), `TRG_WS_YLZ_RI_OE_Q` (after insert or update or delete)

## DEFINITIONS.DOCTOR_APPT_DECISIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| DECISION_ID | VARCHAR2(6) | Y |  |
| DECISION_DESC | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

_No standard audit columns._


## DEFINITIONS.DOCTOR_CPT_PRICE
This table will be used to define the CPT Doctor Wise

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | N | Doctor Ref |
| CPT_ID | VARCHAR2(18) | N | CPT For which below Price will be charged |
| PRICE | NUMBER(12,2) | N | Amount which will be charged against this Item |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_DOCTOR_CPT_PRICE`: DOCTOR_ID, PATIENT_TYPE_ID, CPT_ID
- **FK** `FK_DOCTOR_CPT_PRICE_1`: (DOCTOR_ID) -> DEFINITIONS.DOCTOR(DOCTOR_ID)
- **FK** `FK_DOCTOR_CPT_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_DOCTOR_CPT_PRICE_1`: PRICE>0
- **Triggers**: `DOCTOR_CPT_PRICE_DEL` (after delete), `DOCTOR_CPT_PRICE_INS` (before insert), `DOCTOR_CPT_PRICE_UPD` (before update)

## DEFINITIONS.DOCTOR_EXTERNAL

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(10) | N |  |
| NAME | VARCHAR2(55) | N |  |
| SPECIALITY | VARCHAR2(55) | Y |  |
| DEGREES | VARCHAR2(100) | Y |  |
| ADDRESS1 | VARCHAR2(200) | Y |  |
| ADDRESS2 | VARCHAR2(200) | Y |  |
| PHONE1 | VARCHAR2(15) | Y |  |
| PHONE2 | VARCHAR2(15) | Y |  |
| EMAIL1 | VARCHAR2(45) | Y |  |
| EMAIL2 | VARCHAR2(45) | Y |  |
| FAX | VARCHAR2(15) | Y |  |
| HOSPITAL | VARCHAR2(100) | Y |  |
| CLINIC_CITY | VARCHAR2(100) | Y |  |
| HOSPITAL_CITY | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| PANEL_DOCTOR | CHAR(1) default 'N' | Y |  |
| MASTER_DOCTOR_ID | VARCHAR2(7) | Y |  |
| HOSPITAL_ID | VARCHAR2(7) | Y |  |
| SPECIALITY_ID | VARCHAR2(8) | Y |  |
| BATCH_NO | VARCHAR2(11) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| TITLE_ID | NUMBER(4) | Y | store the title of the name i.e. Mr. Dr. etc |
| DOCTOR_ID_T | VARCHAR2(10) | N | To Store Doctor ID temporarily |
| DOCTOR_ID_OLD | VARCHAR2(7) | Y | This column contains copy of doctor_id |
| PMDC | VARCHAR2(30) | Y |  |

- **PK** `PK_DOCTOR_EXTERNAL`: DOCTOR_ID
- **Triggers**: `DOCTOR_EXTERNAL_DEL` (after delete), `DOCTOR_EXTERNAL_INS` (before insert), `DOCTOR_EXTERNAL_NEW_ID` (before insert), `DOCTOR_EXTERNAL_T` (before insert), `DOCTOR_EXTERNAL_TS` (before insert or update or delete), `DOCTOR_EXTERNAL_UPD` (before update)

## DEFINITIONS.DOCTOR_EXTERNAL_ERRORS

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | N |  |
| NAME | VARCHAR2(55) | Y |  |
| SPECIALITY | VARCHAR2(55) | Y |  |
| DEGREES | VARCHAR2(100) | Y |  |
| ADDRESS1 | VARCHAR2(200) | Y |  |
| ADDRESS2 | VARCHAR2(200) | Y |  |
| PHONE1 | VARCHAR2(15) | Y |  |
| PHONE2 | VARCHAR2(15) | Y |  |
| EMAIL1 | VARCHAR2(45) | Y |  |
| EMAIL2 | VARCHAR2(45) | Y |  |
| FAX | VARCHAR2(15) | Y |  |
| BATCH_NO | VARCHAR2(9) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PANEL_DOCTOR | CHAR(1) | Y |  |
| MASTER_DOCTOR_ID | VARCHAR2(7) | Y |  |
| HOSPITAL_ID | VARCHAR2(7) | Y |  |
| SPECIALITY_ID | VARCHAR2(8) | Y |  |
| EXISTS_ON_HIS | CHAR(1) | Y |  |
| ERROR_RAISED | VARCHAR2(4000) | Y |  |
| ERROR_ID | NUMBER(9) | N |  |

- **PK** `PK_DOCTOR_EXTERNAL_ERRORS`: ERROR_ID
- **Triggers**: `DOCTOR_EXTERNAL_ERRORS_ID_UPD` (before insert)

## DEFINITIONS.DOCTOR_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| FULL_NAME | VARCHAR2(500) | Y |  |
| LETTER_HEAD1 | VARCHAR2(500) | Y |  |
| LETTER_HEAD2 | VARCHAR2(1000) | Y |  |
| EXTENSION | VARCHAR2(45) | Y |  |
| FAX | VARCHAR2(45) | Y |  |
| EMAIL | VARCHAR2(45) | Y |  |
| HISTORY_ID | VARCHAR2(10) | N |  |

- **PK** `PK_DOCTOR_HISTORY`: HISTORY_ID
- **Triggers**: `DOCTOR_HISTORY_INS` (before insert), `DOCTOR_HISTORY_T` (before insert), `DOCTOR_HIST_CHECK` (before delete or update)

## DEFINITIONS.DOCTOR_IDS_R

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| CHILD_DOCTOR_ID | VARCHAR2(7) | Y |  |


## DEFINITIONS.SERVICE_HOSPITAL

| Column | Type | Null | Comment |
|---|---|---|---|
| HOSPITAL_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_SERVICE_HOSPITAL`: HOSPITAL_ID
- **Triggers**: `SERVICE_HOSPITAL_CEA` (before insert or update or delete), `TRG_WS_BSL_PT_JO_Q` (after insert or update or delete)

## DEFINITIONS.DOCTOR_MARKETING

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | Y |  |
| NAME | VARCHAR2(55) | Y |  |
| SPECIALITY | VARCHAR2(55) | Y |  |
| DEGREES | VARCHAR2(100) | Y |  |
| CLINIC_ADDRESS | VARCHAR2(200) | Y |  |
| HOSPITAL_ADDRESS | VARCHAR2(200) | Y |  |
| CLINIC_PHONE | VARCHAR2(15) | Y |  |
| HOSPITAL_PHONE | VARCHAR2(15) | Y |  |
| EMAIL1 | VARCHAR2(45) | Y |  |
| EMAIL2 | VARCHAR2(45) | Y |  |
| FAX | VARCHAR2(15) | Y |  |
| HOSPITAL | VARCHAR2(100) | Y |  |
| CLINIC_CITY | VARCHAR2(100) | Y |  |
| HOSPITAL_CITY | VARCHAR2(100) | Y |  |
| MARKETING_DOCTOR | CHAR(1) | Y |  |
| HOSPITAL_ID | NUMBER(4) | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **FK** `FK_MARKETING_DOCOTOR_1`: (HOSPITAL_ID) -> DEFINITIONS.SERVICE_HOSPITAL(HOSPITAL_ID) [disabled]
- **FK** `FK_MARKETING_DOCOTOR_2`: (CLINIC_SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID) [disabled]
- **CHECK** `CK_DOCOTR_MARKETING_1`: ACTIVE IN ('Y', 'N'
- **CHECK** `CK_MARKETING_DOCTOR_1`: MARKETING_DOCTOR IN ('Y', 'N'

## DEFINITIONS.DOCTOR_MULTI_SPECIALTY

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(7) | N |  |
| DOCTOR_MRNO | VARCHAR2(14) | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULT_SPECIALTY | VARCHAR2(1) | Y |  |

- **PK** `PK_DOCTOR_MULTI_SPECIALITY`: DOCTOR_ID, CLINIC_SPECIALITY_ID

## DEFINITIONS.DOCTOR_SPECIALITY

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIALITY_ID | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DOCTOR_SPECIALITY`: SPECIALITY_ID
- **CHECK** `CK_DOCTOR_SPECIALITY_1`: ACTIVE IN('N','Y'
- **Triggers**: `DOCTOR_SPECIALITY_CEA` (before insert or update or delete), `TRG_WS_OAN_XS_UQ_Q` (after insert or update or delete)

## DEFINITIONS.DOCUMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDERED_BY | NUMBER(3) | Y |  |
| VIEW_HISTORY | CHAR(1) | Y |  |
| DOC_GROUP_ID | VARCHAR2(3) default 001 | Y | 001 - For All other document, 002 - SIUT Medical Records Scanning and Archiving Application Document |
| DOC_TYPE | VARCHAR2(1) default 'A' | Y | A - For All Type Document, T - Treatment Guidline Document , E - Patient Education Document |

- **PK** `PK_DOCUMENT_TYPE`: DOC_TYPE_ID
- **UK** `UK_DOCUMENT_TYPE`: DESCRIPTION
- **Triggers**: `DOCUMENT_TYPE_CEA` (before insert or update or delete), `TRG_WS_SFY_OE_OM_Q` (after insert or update or delete)

## DEFINITIONS.DOMAIN

| Column | Type | Null | Comment |
|---|---|---|---|
| DOMAIN_ID | NUMBER generated always as identity | Y |  |
| DOMAIN_NAME | VARCHAR2(255) | N |  |

_No standard audit columns._


## DEFINITIONS.DOSAGE_TYPE_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| DOSAGE_GROUP_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| DISPENSE_UNIT_REQUIRED | VARCHAR2(1) | Y |  |

- **PK** `PK_DOSAGE_TYPE_GROUPS`: DOSAGE_GROUP_ID
- **Triggers**: `DOSAGE_TYPE_GROUPS_CEA` (before insert or update or delete), `DOSAGE_TYPE_GROUPS_DEL` (after delete), `DOSAGE_TYPE_GROUPS_INS` (before insert), `DOSAGE_TYPE_GROUPS_UPD` (before update), `TRG_WS_WOA_LA_JJ_Q` (after insert or update or delete)

## DEFINITIONS.DOSAGE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOSAGE_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| LABLE_DESC | VARCHAR2(60) | Y |  |
| LABEL_DESC1 | VARCHAR2(60) | Y |  |
| DOSE_REQUIRED_YN | CHAR(1) default 'Y' | Y |  |
| LABEL_TYPE | VARCHAR2(1) default 'I' | Y | I->IPD, O->OPD, A->ALL |
| SHOW_EXPIRY | VARCHAR2(1) default 'Y' | Y | Y-> Show Expiry Date on Medicine label, N-> Show See Medicine on Medicine label |
| DOSAGE_GROUP_ID | VARCHAR2(5) | Y |  |

- **PK** `PK_DOSAGE_TYPE`: DOSAGE_TYPE_ID
- **UK** `UK_DOSAGE_TYPE`: DOSAGE_TYPE_ID, DOSAGE_GROUP_ID
- **FK** `FK_DOSAGE_TYPE`: (DOSAGE_GROUP_ID) -> DEFINITIONS.DOSAGE_TYPE_GROUPS(DOSAGE_GROUP_ID) [disabled]
- **Triggers**: `DOSAGE_TYPE_CEA` (before insert or update or delete), `DOSAGE_TYPE_DEL` (after delete), `DOSAGE_TYPE_INS` (before insert), `DOSAGE_TYPE_UPD` (before update), `TRG_WS_DRV_RF_IW_Q` (after insert or update or delete)

## DEFINITIONS.DOSAGE_TYPE_LANGUAGE_SETUP
THIS TABLE IS USED TO DEFINE MULTILINGUAL DOSAGE TYPE INSTRUCTIONS WHICH WILL BE PRINTED ON PHARMACY PRESCRIPTION AND LABEL

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| DOSAGE_TYPE_ID | VARCHAR2(5) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR SINGULAR INSTRUCTIONS |
| LABEL_DESC1 | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR PLURAL INSTRUCTIONS |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_DOSAGE_TYPE_LANGUAGE_SETUP`: LANGUAGE_ID, DOSAGE_TYPE_ID
- **Triggers**: `DOSAGE_TYPE_LANGUAGE_SETUP_CEA` (before insert or update or delete), `DOSAGE_TYPE_LANGUAGE_SETUP_DEL` (after delete), `DOSAGE_TYPE_LANGUAGE_SETUP_INS` (before insert), `DOSAGE_TYPE_LANGUAGE_SETUP_UPD` (before update), `TRG_WS_YBQ_WB_JI_Q` (after insert or update or delete)

## DEFINITIONS.DOSE_TIME

| Column | Type | Null | Comment |
|---|---|---|---|
| DOSE_TIME | VARCHAR2(5) | N |  |

- **PK** `PK_DOSE_TIME`: DOSE_TIME
- **Triggers**: `DOSE_TIME_CEA` (before insert or update or delete), `TRG_WS_YTT_ET_CV_Q` (after insert or update or delete)

## DEFINITIONS.DRUG_ADMIN_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| DRUG_ADMIN_STATUS_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_DRUG_ADMIN_STATUS_ID`: DRUG_ADMIN_STATUS_ID
- **Triggers**: `DRUG_ADMIN_STATUS_CEA` (before insert or update or delete), `TRG_WS_SID_XI_EJ_Q` (after insert or update or delete)

## DEFINITIONS.DRUG_PREPARATION_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(3) | N | This column contains ID |
| SETUP_TYPE | VARCHAR2(1) | N | This column contains setup type - R- Requirement, M-Method |
| DESCRIPTION | VARCHAR2(4000) | Y | This column contains descriptions |
| SHORT_DESC | VARCHAR2(50) | Y | This column contains short descriptions |
| REMARKS | VARCHAR2(4000) | Y | This column contains remarks |
| ACTIVE | VARCHAR2(1) default 'N' | Y | This column contains active/in-active flag |

- **PK** `PK_DRUG_PREPARATION_SETUP`: SETUP_ID, SETUP_TYPE
- **Triggers**: `DRUG_PREPARATION_SETUP_CEA` (before insert or update or delete), `DRUG_PREPARATION_SETUP_DEL` (after delete), `DRUG_PREPARATION_SETUP_INS` (before insert), `DRUG_PREPARATION_SETUP_UPD` (before update), `TRG_WS_KKE_JA_CW_Q` (after insert or update or delete)

## DEFINITIONS.DRUG_THERAPY_PROBLEMS

| Column | Type | Null | Comment |
|---|---|---|---|
| DRUG_THERAPY_PROBLEM_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_DRUG_THERAPY_PROBLEMS`: DRUG_THERAPY_PROBLEM_ID
- **Triggers**: `DRUG_THERAPY_PROBLEMS_CEA` (before insert or update or delete), `DRUG_THERAPY_PROBLEMS_DEL` (after delete), `DRUG_THERAPY_PROBLEMS_INS` (before insert), `DRUG_THERAPY_PROBLEMS_UPD` (before update), `TRG_WS_SHL_BW_NN_Q` (after insert or update or delete)

## DEFINITIONS.DUMMY

| Column | Type | Null | Comment |
|---|---|---|---|
| BANK_ID | VARCHAR2(6) | Y |  |
| BANK | VARCHAR2(100) | Y |  |
| BRANCH_ID | VARCHAR2(3) | Y |  |
| BRANCH | VARCHAR2(100) | Y |  |
| ACCOUNT_NO | VARCHAR2(50) | Y |  |
| CODE_BREAK_UP | VARCHAR2(50) | Y |  |
| BRANCH_NO | VARCHAR2(50) | Y |  |
| ACCOUNT_TYPE | VARCHAR2(50) | Y |  |
| CUSTOMER_NO | VARCHAR2(50) | Y |  |
| NET_PAYABLE | VARCHAR2(500) | Y |  |
| RUN_NUMBER | VARCHAR2(50) | Y |  |
| CHECK_DIGIT | VARCHAR2(50) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| NAME | VARCHAR2(500) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |


## DEFINITIONS.DUTY_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_LOCATION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DUTY_LOCATION`: DUTY_LOCATION_ID
- **Triggers**: `DUTY_LOCATION_DEL` (after delete), `DUTY_LOCATION_INS` (before insert), `DUTY_LOCATION_UPD` (before update)

## DEFINITIONS.EAR_PATHWAY_INIT

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| DES | VARCHAR2(300) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| AGE_GROUP | VARCHAR2(1) | Y |  |

- **PK** `PK_EAR_PATHWAY_INIT`: ID
- **Triggers**: `EAR_PATHWAY_INIT_INS` (before insert)

## DEFINITIONS.EDIT_ADMISSION_REQ_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(4) | N |  |
| USER_DEPARTMENT | VARCHAR2(7) | Y | Login user doctor department, doctor which will edit admission request. |
| USER_CLINIC_SPECIALITY | VARCHAR2(6) | Y | Login user doctor admitting speciality, doctor which will edit admission request. |
| ADMITTING_DOCTOR_DEPARTMENT | VARCHAR2(7) | Y | admitting doctor department against admission request enter. |
| ADMITTING_DR_CLINIC_SPECIALITY | VARCHAR2(6) | Y | admitting doctor sepciality against admission request enter. |
| REMARKS | VARCHAR2(500) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| EDIT_TYPE | VARCHAR2(1) default 'D' | N | D= Allow to edit admission request by comparing user departmnt and admitting doctor department      ,S= Allow to edit admission request by comparing user clinic sepciality and admitting doctor clinic speciality |
| RESTRICTION_TYPE | VARCHAR2(1) default 'A' | N | A= Allow to edit admission request, R= Restrict to edit admission request. |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_ADMISSION_REQ_SETUP`: SETUP_ID, LOCATION_ID
- **Triggers**: `EDIT_ADMISSION_REQ_SETUP_CEA` (before insert or update or delete), `TRG_WS_KOK_LO_SI_Q` (after insert or update or delete)

## DEFINITIONS.EFFECT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| EFFECT_TYPE_ID | VARCHAR2(3) | N |  |
| ET_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_EFFECT_TYPE`: EFFECT_TYPE_ID
- **Triggers**: `EFFECT_TYPE_DEL` (after delete), `EFFECT_TYPE_INS` (before insert), `EFFECT_TYPE_UPD` (before update)

## DEFINITIONS.EMAIL_ALERT
This table contains information of list of Email Events

| Column | Type | Null | Comment |
|---|---|---|---|
| LIST_ID | VARCHAR2(5) | N | Unique key of Email List ID |
| DESCRIPTION | VARCHAR2(500) | Y | This column contains information of description of Email Events |
| EMAIL_SUBJECT | VARCHAR2(160) | Y | This column contains information of Email Subject |
| ACTIVE | CHAR(1) | Y | This column contains flag information of activate status (Y=Active, N=Inactive) |
| EMAIL_SENDER | VARCHAR2(50) | Y | This column contains email address of sender |

- **PK** `PK_EMAIL_ALERT`: LIST_ID
- **Triggers**: `EMAIL_ALERT_DEL` (after delete), `EMAIL_ALERT_INS` (before insert), `EMAIL_ALERT_UPD` (before update)

## DEFINITIONS.EMAIL_ALERT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| LIST_ID | VARCHAR2(5) | N | Auto generated number. |
| EMAIL_SERIAL | VARCHAR2(60) | N | Auto generated number. |
| RECIPIENT_MRNO | VARCHAR2(14) | Y | Email recipient's MRNO number. |
| RECIPIENT_EMAIL | VARCHAR2(60) | Y | Email recipient's email address.. |
| SENDER_MRNO | VARCHAR2(14) | Y | Email sender's MRNO number. |
| SENDER_EMAIL | VARCHAR2(60) | Y | Email senders's email address.. |
| ACTIVE | CHAR(1) | Y | Flag to mark if the record is Active or not. |
| MOBILE_NUMBER | VARCHAR2(100) | Y | SMS recipient's mobile number. |
| SEND_SMS_YN | CHAR(1) | Y | Flag to mark if the SMS should be sent or not. |
| EMAIL_LOCATION_ID | VARCHAR2(3) | Y | This column contains Email Location ID |

- **PK** `PK_EMAIL_ALERT_DETAIL`: LIST_ID, EMAIL_SERIAL
- **FK** `FK_EMAIL_ALERT_DETAIL_1`: (LIST_ID) -> DEFINITIONS.EMAIL_ALERT(LIST_ID)
- **CHECK** `CK_EMAIL_ALERT_DETAIL_1`: SEND_SMS_YN IN ('Y','N'
- **Triggers**: `EMAIL_ALERT_DETAIL_DEL` (after delete), `EMAIL_ALERT_DETAIL_INS` (before insert), `EMAIL_ALERT_DETAIL_UPD` (before update)

## DEFINITIONS.EMPLOYER

| Column | Type | Null | Comment |
|---|---|---|---|
| EMPLOYER_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_EMPLOYER`: EMPLOYER_ID
- **CHECK** `CK_EMPLOYER_1`: ACTIVE IN ('Y','N'

## DEFINITIONS.EMP_TRAINING_DOCUMENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| DOC_TYPE_ID | NUMBER | N | DOCUMENT TYPE WILL BE STORED HERE |
| DESCRIPTION | VARCHAR2(500) | Y | DOCUMENT TYPE DESCRIPTION WILL BE STORED HERE |
| ACTIVE | CHAR(1) | Y | VALUES Y OR N |
| OBJECT_CODE | VARCHAR2(20) | Y |  |

- **PK** `PK_1`: DOC_TYPE_ID
- **Triggers**: `EMP_TRAINING_DOCUMENT_TYPE_DEL` (after delete), `EMP_TRAINING_DOCUMENT_TYPE_INS` (before insert), `EMP_TRAINING_DOCUMENT_TYPE_UPD` (before update)

## DEFINITIONS.EMP_WISE_CPTS

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_EMP_WISE_CPT_01`: CPT_ID, EMP_CODE

## DEFINITIONS.EMP_WISE_CPTS_EXEMPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| EMP_CODE | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_EMP_WISE_CPTS_EXEMPT_01`: CPT_ID, EMP_CODE

## DEFINITIONS.EMR_TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| OWNER | VARCHAR2(20) | N |  |
| TABLE_NAME | VARCHAR2(50) | N |  |
| COLUMN_NAME | VARCHAR2(30) | N |  |
| DATA_TYPE | VARCHAR2(20) | Y |  |
| SAVE_ORIGINAL_VALUE | CHAR(1) default 'N' | Y |  |
| ORDER_BY | NUMBER default 0 | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| DEFAULT_WHERE | VARCHAR2(2000) default 'WHERE 1 = 1' | Y |  |
| INSERT_REQUIRED | CHAR(1) default 'N' | Y | IF value = Y , it means we have to insert record first in master table and then update data in child table |
| IS_PARENT_TABLE | CHAR(1) default 'N' | Y | this column is used to mark parent/master table |
| PARENT_OWNER_NAME | VARCHAR2(20) | N | this column is used for parent/master owner name |
| PARENT_TABLE_NAME | VARCHAR2(100) | N | this column is used for parent/master table name |

- **PK** `PK_EMR_TABLES`: OWNER, TABLE_NAME, COLUMN_NAME
- **Triggers**: `EMR_TABLES_DEL` (after delete), `EMR_TABLES_INS` (before insert), `EMR_TABLES_UPD` (before update)

## DEFINITIONS.ENCOUNTER_TREATMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| EN_CATEGORY_ID | VARCHAR2(6) | N |  |
| TR_CATEGORY_ID | VARCHAR2(6) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ENCOUNTER_TREATMENT`: EN_CATEGORY_ID, TR_CATEGORY_ID
- **FK** `FK_ENCOUNTER_TREATMENT_1`: (EN_CATEGORY_ID) -> DEFINITIONS.DEF_ENCOUNTER_CATEGORY(EN_CATEGORY_ID)
- **FK** `FK_ENCOUNTER_TREATMENT_2`: (TR_CATEGORY_ID) -> DEFINITIONS.DEF_TREATMENT_CATEGORY(TR_CATEGORY_ID)
- **Triggers**: `ENCOUNTER_TREATMENT_DEL` (after delete), `ENCOUNTER_TREATMENT_INS` (before insert), `ENCOUNTER_TREATMENT_UPD` (before update)

## DEFINITIONS.ENCRYPTED_TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(60) | N |  |
| ENCRYPTION_ALLOWED | CHAR(1) | Y |  |

- **PK** `PK_ENC_TABLES_01`: SCHEMA_ID, TABLE_ID
- **Triggers**: `ENCRYPTED_TABLES_DEL` (after delete), `ENCRYPTED_TABLES_INS` (before insert), `ENCRYPTED_TABLES_UPD` (before update)

## DEFINITIONS.ENCRYPTED_TABLE_COLUMNS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| COLUMN_NAME | VARCHAR2(30) | Y |  |
| COLUMN_ID | VARCHAR2(5) | N |  |
| DATA_TYPE | VARCHAR2(30) | Y |  |
| ENCRYPTION_ALLOWED | CHAR(1) | Y |  |
| ENCRYPTION_KEY | VARCHAR2(500) | Y |  |

- **PK** `PK_ENC_SCH_TAB_COL_01`: SCHEMA_ID, TABLE_ID, COLUMN_ID
- **Triggers**: `ENCRYPTED_TABLE_COLUMNS_DEL` (after delete), `ENCRYPTED_TABLE_COLUMNS_INS` (before insert), `ENCRYPTED_TABLE_COLUMNS_UPD` (before update)

## DEFINITIONS.ENTITY_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| ENTITY_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ENTITY_SOURCE_TABLE | VARCHAR2(255) | Y | Store entity type source table name ex/ REGISTRATION.PATIENT |
| ENTITY_SOURCE_COLUMN | VARCHAR2(255) | Y | Store source table key column name ex/ MRNO |
| ENTITY_COLUMN_VALUE | VARCHAR2(255) | Y | Store column name to get entity value name/description ex/ NAME |

- **PK** `PK_ENTITY_TYPES`: ENTITY_TYPE_ID
- **UK** `UK_ENTITY_TYPES_1`: DESCRIPTION
- **Triggers**: `ENTITY_TYPES_CEA` (before insert or update or delete), `ENTITY_TYPES_DEL` (after delete), `ENTITY_TYPES_INS` (before insert), `ENTITY_TYPES_UPD` (before update), `TRG_WS_LFT_NX_BU_Q` (after insert or update or delete)

## DEFINITIONS.ERROR_MESSAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| ERROR_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_ERROR_MESSAGES`: ERROR_ID
- **Triggers**: `ERROR_MESSAGES_DEL` (after delete), `ERROR_MESSAGES_INS` (before insert), `ERROR_MESSAGES_UPD` (before update)

## DEFINITIONS.ESI_PRIORITY
This table will be used to save ESI Priority

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIORITY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y | this column is used to save priority description |
| SHORT_DESC | VARCHAR2(3) | Y | this column is used to save priority short description |
| ORDER_BY | NUMBER(2) | Y | Y - Yes, N - No |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ESI_PRIORITY`: PRIORITY_ID
- **Triggers**: `ESI_PRIORITY_CEA` (before insert or update or delete), `ESI_PRIORITY_DEL` (after delete), `ESI_PRIORITY_INS` (before insert), `ESI_PRIORITY_UPD` (before update), `TRG_WS_XOZ_TI_ZX_Q` (after insert or update or delete)

## DEFINITIONS.EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| EVENT_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| EMAIL_SUBJECT | VARCHAR2(100) | Y |  |
| EMAIL_BODY | VARCHAR2(500) | Y |  |
| USER_RUNTIME | VARCHAR2(1) default 'N' | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y | Column for Calling Event Object Code |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| COLOR_CODE | VARCHAR2(20) | Y |  |
| SHORT_DESC | CHAR(4) | Y |  |
| OUTPUT | VARCHAR2(1) default 'O' | Y |  |
| NOTE_ENTRY | VARCHAR2(1) default 'N' | Y |  |
| LABEL_DESC | VARCHAR2(255) | Y |  |
| RESTRICT_REPEAT_EVENT | VARCHAR2(1) default 'N' | Y | This column is used to restrict the repetition of events |
| SEND_EMAIL | CHAR(1) default 'N' | Y | This column contains flag to use email solution for specific event |
| REMINDER_DAYS | NUMBER | Y | This column is used to save no of days for first reminder |
| NEXT_REMINDER_DAYS | NUMBER | Y | This column is used to save no of days for second reminder |
| REMINDER_FREQUENCY | NUMBER | Y | This column is used to save alert frequency, how many time alert will be generate |
| CUSTOM_REMINDER_DAYS | CHAR(1) default 'N' | Y | This column is used to save a flag for customizr reminder days(manually enter by any authority) |

- **PK** `PK_EVENT`: EVENT_ID
- **CHECK** `CHK_EVENT_USER`: USER_RUNTIME IN ('N','Y'
- **Triggers**: `EVENT_CEA` (before insert or update or delete), `EVENT_DEL` (after delete), `EVENT_INS` (before insert), `EVENT_UPD` (before update), `TRG_WS_LWB_MW_YA_Q` (after insert or update or delete)

## DEFINITIONS.EVENT_DECISION

| Column | Type | Null | Comment |
|---|---|---|---|
| PURCHASE_TYPE_ID | NUMBER | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| EVENT_ID | NUMBER(3) | N |  |
| DECISION_ID | NUMBER(3) | N |  |
| ORDER_STATUS_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_EVENT_DECISION`: PURCHASE_TYPE_ID, WORK_FLOW_ID, SCHEMA_ID, EVENT_ID, DECISION_ID

## DEFINITIONS.EVENT_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| NATURE_ID | VARCHAR2(3) | N | This column contains CPT Nature ID e.g. 096=Lab, 029, radiology, 030=NM (Reference to DEFINITIONS.DEPARTMENT_NATURE) |
| EVENT_ID | NUMBER(4) | N | This column contains Event ID (Reference to DEFINITIONS.EVENT) |
| STATUS_ID | VARCHAR2(3) | N | This column contains Order Status ID (e.g. 001=Order, 002 Invoiced, 019=Under process, 015 complete) |
| ORDER_BY | NUMBER(2) | N | This column contains order by thsi can be used to display events in reports |
| ACTIVE | CHAR(1) | N | This column contains active status of Event group(Y=Active, N=Inactive) |
| LOG_EVENT | CHAR(1) | N | This column contains Flag Information to log Event (O=Order CPT, D=Module/Detail) |
| LOG_DEPT | CHAR(1) | N | This column contains Flag Information to log Department (C=CPT, U=User, O=Order) |

- **PK** `PK_EVENT_GROUPS`: NATURE_ID, EVENT_ID
- **CHECK** `CK_EVENT_GROUPS_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_EVENT_GROUPS_2`: LOG_EVENT IN ('O','D'
- **CHECK** `CK_EVENT_GROUPS_3`: LOG_DEPT IN ('C','U','O'

## DEFINITIONS.EVENT_USER

| Column | Type | Null | Comment |
|---|---|---|---|
| PURCHASE_TYPE_ID | NUMBER | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| EVENT_ID | NUMBER(3) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | N | HIS MODULE_ID |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_EVENT_USER`: PURCHASE_TYPE_ID, WORK_FLOW_ID, EVENT_ID, MRNO, SCHEMA_ID
- **Triggers**: `EVENT_USER_DEL` (after delete), `EVENT_USER_INS` (before insert), `EVENT_USER_UPD` (before update), `TRG_WS_IXZ_PI_QZ_Q` (after insert or update or delete)

## DEFINITIONS.EVENT_WISE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER(3) | N | This column contains parameter id (Reference from definitions.event_wise_parameter) |
| PURCHASE_TYPE_ID | NUMBER | N | This column contains purchase type id (Reference from mms.def_purchase_type) |
| WORK_FLOW_ID | NUMBER(4) | N | This column contains work flow id (Reference from definitions.pr_type_flow) |
| EVENT_ID | NUMBER(3) | N | This column contains event id (Reference from definitions.pr_type_flow_event) |
| SCHEMA_ID | VARCHAR2(3) | N | This column contains schema id (Reference from definitions.schemas) |
| PARAMETER_VALUE | VARCHAR2(150) | Y | This column contains parameter value (Reference from definitions.event_wise_parameter) |
| EMAIL | CHAR(1) | Y | This column contains flag of email in Y/ N format |
| ORDER_BY | NUMBER(3) | Y | This column contains execution order of parameters |
| AUTO_PERFORM | CHAR(1) | Y | This column contains flag of auto perform |
| ACTIVE | CHAR(1) | Y | This column contains flag of active |

- **PK** `PK_EVENT_WISE_DETAIL`: PURCHASE_TYPE_ID, SCHEMA_ID, WORK_FLOW_ID, EVENT_ID, PARAMETER_ID

## DEFINITIONS.EVENT_WISE_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER(3) | N | This column contains parameter id in number format. |
| PARAMETER_DESC | VARCHAR2(150) | Y | This column contains parameter description. |
| PARAMETER_TYPE | VARCHAR2(5) | Y | This column contains parameter type. |
| ACTIVE | CHAR(1) | Y | This column contains ACTIVE flag. |

- **PK** `PK_EVENT_WISE_PARAM`: PARAMETER_ID

## DEFINITIONS.EXCEPTIONAL_LEAVE_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| REF_MRNO | VARCHAR2(14) | N |  |
| LEAVE_ROLE_ID | VARCHAR2(3) | Y |  |
| ORDER_BY | NUMBER(2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `UK_EXCEPTIONAL_LEAVE_HIERARCHY`: MRNO, REF_MRNO
- **FK** `FK_EXCEPTIONAL_LEAVE_HIERARCHY`: (LEAVE_ROLE_ID) -> HRD.LEAVE_ROLE(LEAVE_ROLE_ID) [disabled]
- **Triggers**: `EXCEP_LEAVE_HIERARCHY_DEL` (after delete), `EXCEP_LEAVE_HIERARCHY_INS` (before insert), `EXCEP_LEAVE_HIERARCHY_UPD` (before update), `TRG_WS_JYQ_AK_CC_Q` (after insert or update or delete)

## DEFINITIONS.EXCEPTION_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(3) | N | This column contain value of Exception types |
| EXCEPTION_DESC | VARCHAR2(500) | Y | This column contain value of Exception description |
| CODE_ERROR | VARCHAR2(100) | Y | This column contain value of Exception code |

- **PK** `PK_EXCEPTION_TYPES_001`: TYPE_ID

## DEFINITIONS.EXPENSE

| Column | Type | Null | Comment |
|---|---|---|---|
| EXPENSE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_EXPENSE`: EXPENSE_ID
- **Triggers**: `EXPENSE_DEL` (after delete), `EXPENSE_INS` (before insert), `EXPENSE_UPD` (before update)

## DEFINITIONS.EXTERNAL_DOCTOR_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| DOCTOR_ID | VARCHAR2(10) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| CONTRACT_STRT_DATE | DATE | Y |  |
| CONTRACT_END_DATE | DATE | Y |  |
| TEST_REQ_FOR_BONUS | NUMBER | Y |  |
| BONUS | NUMBER | Y |  |
| TOT_TESTS | NUMBER | Y |  |
| BONUS_DUE | NUMBER | Y |  |
| BONUS_AVAILED | NUMBER | Y |  |
| BONUS_BAL | NUMBER | Y |  |

- **PK** `PK_EXTERNAL_DOCTOR_DETAIL`: DOCTOR_ID, DEPARTMENT_ID, SECTION_ID
- **FK** `FK_EXTERANL_DOCTOR_DETAIL`: (DOCTOR_ID) -> DEFINITIONS.DOCTOR_EXTERNAL(DOCTOR_ID)

## DEFINITIONS.EXTRA_SKILLS_R

| Column | Type | Null | Comment |
|---|---|---|---|
| EXTRA_SKILL_ID | VARCHAR2(5) | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| DEFAULTS | CHAR(1) default 'N' | Y |  |


## DEFINITIONS.FIELD_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| FIELD_TYPE_ID | NUMBER | N |  |
| NAME | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| APEX_NAME | VARCHAR2(100) | Y |  |

- **PK** `PK_FIELD_TYPE`: FIELD_TYPE_ID
- **Triggers**: `FIELD_TYPE_DEL` (after delete), `FIELD_TYPE_INS` (before insert), `FIELD_TYPE_UPD` (before update)

## DEFINITIONS.FILES_EXTENSIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| EXT_ID | VARCHAR2(3) | N | Unique ID for specific File Extension |
| EXT_DESC | VARCHAR2(5) | N | Unique Extension Description |
| ORDER_BY | NUMBER | Y | Order by numbers |
| COMMENTS | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |

- **PK** `PK_FILES_EXTENSIONS`: EXT_ID
- **UK** `UK_FILES_EXTENSIONS`: EXT_DESC
- **CHECK** `CK_FILES_EXTENSIONS_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_EXTENSIONS_DEL` (after delete), `FILES_EXTENSIONS_INS` (before insert), `FILES_EXTENSIONS_UPD` (before update), `TRG_WS_MVM_OZ_RC_Q` (after insert or update or delete)

## DEFINITIONS.FILES_SERVERS_SYNC_SETUP
This table contains Servers Replication Setup for Attached/Uploaded FILES

| Column | Type | Null | Comment |
|---|---|---|---|
| SOURCE_SERVER_ID | VARCHAR2(10) | N | Source server ID; study is being copied from |
| TARGET_SERVER_ID | VARCHAR2(10) | N | Destination server ID; study is being copied to |
| ACCESS_MODE | VARCHAR2(1) | N | Flag Information (L=LAN, W=WAN) |
| PRIORITY | NUMBER(2) | N | request processing priority sequence |
| ACTIVE | CHAR(1) default 'Y' | N | Flag Y=Active, N=Inactive |
| START_DATE | DATE default SYSDATE | N | Start date of Activation |
| END_DATE | DATE | Y | End/Epiiry date of Activation |
| SYNC_MODE | CHAR(1) | N | Flag Information (N=No, A=Automatic, M=Manual) |

- **PK** `PK_FILES_SERVERS_SYNC_SETUP`: SOURCE_SERVER_ID, TARGET_SERVER_ID
- **FK** `FK_FILES_SERVERS_SYNC_SETUP_1`: (SOURCE_SERVER_ID) -> DEFINITIONS.FILES_SERVERS(SERVER_ID)
- **FK** `FK_FILES_SERVERS_SYNC_SETUP_2`: (TARGET_SERVER_ID) -> DEFINITIONS.FILES_SERVERS(SERVER_ID) [disabled]
- **CHECK** `CK_FILES_SERVERS_SYNC_SETUP_1`: ACCESS_MODE IN ('L','W'
- **CHECK** `CK_FILES_SERVERS_SYNC_SETUP_2`: ACTIVE IN ('Y','N'
- **CHECK** `CK_FILES_SERVERS_SYNC_SETUP_3`: SYNC_MODE IN ('N','A','M'
- **Triggers**: `FILES_SERVERS_SYNC_SETUP_DEL` (after delete), `FILES_SERVERS_SYNC_SETUP_INS` (before insert), `FILES_SERVERS_SYNC_SETUP_UPD` (before update), `TRG_WS_YHA_JH_AB_Q` (after insert or update or delete)

## DEFINITIONS.FILES_TEMPORARY_PATHS
This is a setup table FILES_TEMPORARY_PATHS contains setup values for all location with temporary physical paths for temporarily placing the file(s)/document(s) for archiving purpose at differenct physical paths

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | This column conatins Location Id, Reference:DEFINITIONS.LOCATION.LOCATION_ID |
| PHYSICAL_PATH | VARCHAR2(500) | N | This column conatins temporary physical paths defined for the file(s)/document(s) to be placed on temporarily, which will be moved on permanent physical paths |
| ACTIVE | CHAR(1) default 'Y' | Y | This column contains Flag (N=No, Y=Yes) |

- **PK** `PK_FILES_TEMPORARY_PATHS`: LOCATION_ID
- **FK** `FK_FILES_TEMPORARY_PATHS`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **Triggers**: `FILES_TEMPORARY_PATHS_DEL` (after delete), `FILES_TEMPORARY_PATHS_INS` (before insert), `FILES_TEMPORARY_PATHS_UPD` (before update)

## DEFINITIONS.FILES_TYPES_ASSOCIATE_WITH
It is setup table; and contains Associated Files Type

| Column | Type | Null | Comment |
|---|---|---|---|
| FTAW_ID | VARCHAR2(10) | N | It contains PK Id Unique ID for File Type ID |
| FILE_TYPE_ID | VARCHAR2(3) | N | Unique ID for File Type ID |
| FILE_DESC | VARCHAR2(100) | N | Description of File Description |
| COMMENTS | VARCHAR2(500) | Y | Description of File Description |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y | Description of File Description |
| LOCATION_ID | VARCHAR2(3) | Y | Description of File Description |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |

- **PK** `PK_FILES_TYPES_ASSOCIATE_WITH`: FTAW_ID
- **UK** `UK_FILES_TYPES_ASSOCIATE_WITH`: FILE_DESC

## DEFINITIONS.FILES_TYPES_ASSOCIATE_WITH_DET
It is setup table; and contains Associated Files Type

| Column | Type | Null | Comment |
|---|---|---|---|
| FTAW_DET_ID | VARCHAR2(10) | N |  |
| FTAW_ID | VARCHAR2(10) | N | It contains PK Id Unique ID for File Type ID |
| FILE_TYPE_ID | VARCHAR2(3) | N | Unique ID for File Type ID |
| DOCUMENT_DESCRIPTION | VARCHAR2(200) | Y |  |
| COMPULSORY_ATTACHMENT | CHAR(1) | N |  |
| COMMENTS | VARCHAR2(500) | Y | Description of File Description |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |

- **PK** `PK_FTAW_DET`: FTAW_DET_ID

## DEFINITIONS.FILES_TYPES_DET

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(3) | N | Unique ID for specific File Type Id |
| FILE_TYPE_ID | VARCHAR2(3) | N | Foreign Key reference column of Table DEFINITIONS.FILES_TYPES |
| TYPE_DESC | VARCHAR2(10) | N | Description of specific file type |
| COMMENTS | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |
| STORAGE_TYPE | VARCHAR2(2) | Y | Storage type is used to preserve document (DB=database, OS=Operating system) |
| COUNT_PAGES | CHAR(1) default 'N' | N | Flag column to contain status Y=Yes,N=No |
| OPEN_WITH | VARCHAR2(3) | Y |  |
| FILE_SIZE | NUMBER(8,2) | Y | This column contains the uploading file maximum size limit in MBs. Null or zero means no limit on size of uploading file |
| DELETE_SOURCE_FILE | CHAR(1) default 'Y' | Y | This column contains the flag value (Y/N) |
| FILE_TYPE_DESCRIPTION | VARCHAR2(500) | Y | This column is used for file(s) filteration using extension(s) |
| OPEN_FILE_AFTER_DOWNLOAD | CHAR(1) default 'Y' | Y | This column contains the flag value (Y/N) to decide whether the file to be opend after downloading? |

- **PK** `PK_FILES_TYPES_DET`: TYPE_ID, FILE_TYPE_ID
- **UK** `UK_FILES_TYPES_DET`: FILE_TYPE_ID, TYPE_DESC
- **FK** `FK_FILES_TYPES_DET_1`: (FILE_TYPE_ID) -> DEFINITIONS.FILES_TYPES(FILE_TYPE_ID) [disabled]
- **CHECK** `CK_FILES_TYPES_DET_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_TYPES_DET_DEL` (after delete), `FILES_TYPES_DET_INS` (before insert), `FILES_TYPES_DET_UPD` (before update), `TRG_WS_TYZ_EL_JR_Q` (after insert or update or delete)

## DEFINITIONS.FILES_VIEWERS
This is setup table and is used to define softwares to be used to view specific files e.g. *.chm

| Column | Type | Null | Comment |
|---|---|---|---|
| VIEWER_ID | VARCHAR2(3) | N | Unique ID for File Viewer ID |
| VIEWER_NAME | VARCHAR2(60) | N | Complete Name of the Viewer which will be used to view the file |
| VIEWER_PATH | VARCHAR2(1000) | Y | Complete Path where the Viewer is installed, and will be used to view the file |
| COMMENTS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | N | Flag column to contain status Y=Active,N=Inactive |

- **PK** `PK_FILES_VIEWERS`: VIEWER_ID
- **CHECK** `CK_FILES_VIEWERS_1`: ACTIVE IN ('Y','N'
- **Triggers**: `FILES_VIEWERS_DEL` (after delete), `FILES_VIEWERS_INS` (before insert), `FILES_VIEWERS_UPD` (before update), `TRG_WS_ROZ_KT_IB_Q` (after insert or update or delete)

## DEFINITIONS.FILE_UPLOADS

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER generated always as identity | Y |  |
| FILE_NAME | VARCHAR2(255) | Y |  |
| FILE_CONTENT | BLOB | Y |  |
| FILE_TEXT | CLOB | Y |  |
| UPLOAD_DATE | DATE default SYSDATE | Y |  |

_No standard audit columns._


## DEFINITIONS.FILM_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N | PROCEDURE CPT |
| FILM_CPT_ID | VARCHAR2(18) | N | PROCEDURE FILM CPT |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_FILM_CPT`: CPT_ID, FILM_CPT_ID
- **FK** `FK_FILM_CPT_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID)
- **FK** `FK_FILM_CPT_2`: (FILM_CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **Triggers**: `FILM_CPT_CEA` (before insert or update or delete), `FILM_CPT_DEL` (after delete), `FILM_CPT_INS` (before insert), `FILM_CPT_UPD` (before update), `TRG_WS_AZR_ZE_MG_Q` (after insert or update or delete)

## DEFINITIONS.FINANCIAL_YEAR_R

| Column | Type | Null | Comment |
|---|---|---|---|
| FROM_DATE | DATE | Y |  |
| TO_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **CHECK** `CK_FINANCIAL_YEAR_1`: ACTIVE IN ('Y','N'

## DEFINITIONS.FONT_ATTRIBUTE

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTRIBUTE_ID | NUMBER(8) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ATTRIBUTE_NAME | VARCHAR2(255) | Y |  |
| FONT_NAME | VARCHAR2(100) | Y |  |
| FONT_SIZE | NUMBER(6) | Y |  |
| FONT_WEIGHT | NUMBER | Y | FONT_MEDIUM FONT_ULTRALIGHT FONT_EXTRALIGHT FONT_LIGHT FONT_DEMILIGHT FONT_DEMIBOLD FONT_BOLD FONT_EXTRABOLD FONT_ULTRABOLD |
| FONT_STYLE | NUMBER | Y | FONT_PLAIN FONT_ITALIC FONT_OBLIQUE FONT_UNDERLINE FONT_OUTLINE FONT_SHADOW FONT_INVERTED FONT_OVERSTRIKE FONT_BLINK |
| FONT_SPACING | NUMBER | Y | FONT_NORMAL FONT_ULTRADENSE FONT_EXTRADENSE FONT_DENSE FONT_SEMIDENSE FONT_SEMIEXPAND FONT_EXPAND FONT_EXTRAEXPAND FONT_ULTRAEXPAND |
| BACKGROUND_COLOR | VARCHAR2(100) | Y |  |
| FOREGROUND_COLOR | VARCHAR2(100) | Y |  |
| FILL_PATTERN | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_FONT_ATTRIBUTE`: ATTRIBUTE_ID
- **Triggers**: `FONT_ATTRIBUTE_DEL` (after delete), `FONT_ATTRIBUTE_INS` (before insert), `FONT_ATTRIBUTE_UPD` (before update)

## DEFINITIONS.FONT_ATTRIBUTE_OBJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| ATTRIBUTE_ID | NUMBER(8) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_FONT_ATTRIBUTE_OBJECT`: ATTRIBUTE_ID, OBJECT_CODE
- **Triggers**: `FONT_ATTRIBUTE_OBJECT_DEL` (after delete), `FONT_ATTRIBUTE_OBJECT_INS` (before insert), `FONT_ATTRIBUTE_OBJECT_UPD` (before update)

## DEFINITIONS.FOOD_ALERGIES

| Column | Type | Null | Comment |
|---|---|---|---|
| FOOD_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_FOOD_ALERGIES`: FOOD_ID
- **Triggers**: `FOOD_ALERGIES_CEA` (before insert or update or delete), `TRG_WS_WAP_RW_RJ_Q` (after insert or update or delete)

## DEFINITIONS.FORMATE

| Column | Type | Null | Comment |
|---|---|---|---|
| FORMATE_ID | VARCHAR2(6) | N |  |
| NAME | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_FORMATE`: FORMATE_ID
- **Triggers**: `FORMATE_DEL` (after delete), `FORMATE_INS` (before insert), `FORMATE_UPD` (before update)

## DEFINITIONS.FREQUENCY

| Column | Type | Null | Comment |
|---|---|---|---|
| FREQUENCY_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(12) | Y |  |
| FREQUENCY_VALUE | NUMBER(7,2) | Y |  |
| LABLE_DESC | VARCHAR2(60) | Y |  |
| HOUR_GAP | NUMBER(5,2) | Y |  |
| WHEN_REQUIRED | CHAR(1) default 'N' | N |  |
| ALTERNATE_DAYS | CHAR(1) default 'N' | N |  |
| PRINT_ON_LABEL | CHAR(1) default 'N' | Y |  |
| TAPERING_ALLOWED | CHAR(1) default 'N' | Y |  |
| COMPLEX_FREQUENCY | VARCHAR2(1) default 'N' | Y |  |
| SHOW_FREQUENCY | CHAR(1) default 'Y' | Y |  |
| DAY_GAP | NUMBER(5,2) | Y |  |
| ALLOWED_IN_OPAT | CHAR(1) default 'N' | Y |  |

- **PK** `PK_FREQUENCY`: FREQUENCY_ID
- **UK** `UK_SHORT_DESCRIPTION`: SHORT_DESCRIPTION
- **Triggers**: `FREQUENCY_CEA` (before insert or update or delete), `FREQUENCY_DEL` (after delete), `FREQUENCY_INS` (before insert), `FREQUENCY_UPD` (before update), `TRG_WS_CCN_CB_MX_Q` (after insert or update or delete)

## DEFINITIONS.FREQUENCY_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| FREQUENCY_ID | VARCHAR2(5) | N |  |
| DAY_ID | NUMBER(1) | N |  |
| DESCRIPTION | VARCHAR2(10) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `FREQUENCY_DAYS_PK`: FREQUENCY_ID, DAY_ID
- **FK** `FREQUENCY_DAYS_FK`: (FREQUENCY_ID) -> DEFINITIONS.FREQUENCY(FREQUENCY_ID)

## DEFINITIONS.FREQUENCY_DOSE_TIME

| Column | Type | Null | Comment |
|---|---|---|---|
| FREQUENCY_ID | VARCHAR2(5) | N |  |
| DOSE_TIME | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| PROVISION_TIME | CHAR(1) | Y |  |

- **PK** `PK_FREQUENCY_DOSE_TIME`: FREQUENCY_ID, DOSE_TIME
- **FK** `FK_FREQUENCY_DOSE_TIME_1`: (FREQUENCY_ID) -> DEFINITIONS.FREQUENCY(FREQUENCY_ID)
- **Triggers**: `FREQUENCY_DOSE_TIME_CEA` (before insert or update or delete), `FREQUENCY_DOSE_TIME_DEL` (after delete), `FREQUENCY_DOSE_TIME_INS` (before insert), `FREQUENCY_DOSE_TIME_UPD` (before update), `TRG_WS_EIJ_PY_GT_Q` (after insert or update or delete)

## DEFINITIONS.FREQUENCY_LANGUAGE_SETUP
THIS TABLE IS USED TO DEFINE MULTILINGUAL FREQUENCY INSTRUCTIONS WHICH WILL BE PRINTED ON PHARMACY PRESCRIPTION AND LABEL

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| FREQUENCY_ID | VARCHAR2(5) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR SINGULAR INSTRUCTIONS |
| LABEL_DESC1 | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR PLURAL INSTRUCTIONS |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_FREQUENCY_LANGUAGE_SETUP`: LANGUAGE_ID, FREQUENCY_ID
- **Triggers**: `FREQUENCY_LANGUAGE_SETUP_CEA` (before insert or update or delete), `FREQUENCY_LANGUAGE_SETUP_DEL` (after delete), `FREQUENCY_LANGUAGE_SETUP_INS` (before insert), `FREQUENCY_LANGUAGE_SETUP_UPD` (before update), `TRG_WS_UQF_UP_JI_Q` (after insert or update or delete)

## DEFINITIONS.FSA_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| FSA_REASON_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_FSA_REASONS`: FSA_REASON_ID
- **Triggers**: `FSA_REASONS_CEA` (before insert or update or delete), `FSA_REASONS_DEL` (after delete), `FSA_REASONS_INS` (before insert), `FSA_REASONS_UPD` (before update), `TRG_WS_BXW_HZ_BB_Q` (after insert or update or delete)

## DEFINITIONS.GENDER_MAP

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(1) | N |  |
| MAP_SEXID | NUMBER(1) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **UK** `UK_GENDER_MAP`: SEX_ID
- **CHECK** `CHK_ACTIVE_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GENDER_MAP_DEL` (after delete), `GENDER_MAP_INS` (before insert), `GENDER_MAP_NEW_ID` (before insert), `GENDER_MAP_UPD` (before update)

## DEFINITIONS.GENERIC_CATEGORY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(3) | N |  |
| GENERIC_CATEGORY | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_GENERIC_CATEGORY`: SR_NO, GENERIC_CATEGORY
- **Triggers**: `GENERIC_CATEGORY_MASTER_CEA` (before insert or update or delete), `GENERIC_CATEGORY_MASTER_DEL` (after delete), `GENERIC_CATEGORY_MASTER_INS` (before insert), `GENERIC_CATEGORY_MASTER_UPD` (before update), `TRG_WS_HAR_PX_TG_Q` (after insert or update or delete)

## DEFINITIONS.GENERIC_CATEGORY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(3) | Y |  |
| GENERIC_CATEGORY | VARCHAR2(2) | Y |  |
| GENERIC_ID | VARCHAR2(8) | Y |  |
| SHOW_IN_HISTORY | VARCHAR2(1) default 'Y' | Y | Show in History flag |
| ADULT_PEADS | VARCHAR2(1) | Y | A -> Adults, P -> Peads |
| SHOW_DISPENSING_DOSE | VARCHAR2(1) default 'N' | Y |  |

- **UK** `UK_GENERIC_CATEGORY`: SR_NO, GENERIC_CATEGORY, GENERIC_ID
- **FK** `FK_GENERIC_CATEGORY`: (SR_NO, GENERIC_CATEGORY) -> DEFINITIONS.GENERIC_CATEGORY_MASTER(SR_NO, GENERIC_CATEGORY)
- **Triggers**: `GENERIC_CATEGORY_DETAIL_CEA` (before insert or update or delete), `GENERIC_CATEGORY_DETAIL_DEL` (after delete), `GENERIC_CATEGORY_DETAIL_INS` (before insert), `GENERIC_CATEGORY_DETAIL_UPD` (before update), `TRG_WS_GUR_BC_XK_Q` (after insert or update or delete)

## DEFINITIONS.GENERIC_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| GENERIC_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_GENERIC_TYPE`: GENERIC_TYPE_ID
- **Triggers**: `GENERIC_TYPE_CEA` (before insert or update or delete), `GENERIC_TYPE_DEL` (after delete), `GENERIC_TYPE_INS` (before insert), `GENERIC_TYPE_UPD` (before update), `TRG_WS_ZOI_ZJ_DU_Q` (after insert or update or delete)

## DEFINITIONS.GLOBAL_VARIABLES
This table contains definitions of Global variable those are mainatained at Application level This setup replicates variable values from context data to Db Global variables  and Application Global variables

| Column | Type | Null | Comment |
|---|---|---|---|
| VARIABLE_ID | NUMBER | N | Store system generated variable ID |
| VARIABLE_NAME | VARCHAR2(30) | N | Store variable name that will be used by HIS as Global Variable |
| DEFAULT_VALUE | VARCHAR2(300) | Y | Store default constant value of variable |
| INITIALIZE_FROM | VARCHAR2(3000) | Y | Store function name that can be used to initialize value of global variable |
| CHANGEABLE | CHAR(1) default 'N' | Y | Store N or Y to check whether this variable value can be changed within a session of HIS |
| REMARKS | VARCHAR2(1000) | Y | Store user remarks for specified global variable |
| ACTIVE | CHAR(1) default 'Y' | N | Active state of Variable Y/N |
| DATA_SOURCE | CHAR(1) | Y | This column contains flag information to know data source of this global variable (F=Front-End, C=Context, Q=Query) |
| ORDER_BY | VARCHAR2(4) | Y | This coolumn contains order by position to display variable list is sequence |
| MANDATORY | CHAR(1) default 'N' | Y | This column contains information that this global variable is mondatory for login time |

- **PK** `PK_GLOBAL_VARIABLES`: VARIABLE_ID
- **UK** `UK_GLOBAL_VARIABLES_1`: VARIABLE_NAME
- **CHECK** `CK_GLOBAL_VARIABLES_1`: CHANGEABLE IN ('N','Y'
- **CHECK** `CK_GLOBAL_VARIABLES_2`: VARIABLE_NAME = UPPER(VARIABLE_NAME
- **CHECK** `CK_GLOBAL_VARIABLES_3`: ACTIVE IN ('Y','N'
- **CHECK** `CK_GLOBAL_VARIABLES_4`: DATA_SOURCE IN ('F','C','Q'
- **Triggers**: `GLOBAL_VARIABLES_CEA` (before insert or update or delete), `GLOBAL_VARIABLES_DEL` (after delete), `GLOBAL_VARIABLES_INS` (before insert), `GLOBAL_VARIABLES_UPD` (before update), `TRG_WS_QUS_UA_HQ_Q` (after insert or update or delete)

## DEFINITIONS.GL_DIVISION_LOC_HEADS

| Column | Type | Null | Comment |
|---|---|---|---|
| DIVISION_CODE | CHAR(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| HEAD_MRNO | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_GL_DIVISION_LOC_HEADS`: DIVISION_CODE, LOCATION_ID
- **FK** `FK_GL_DIVISION_LOC_HEADS_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_GL_DIVISION_LOC_HEADS_2`: (DIVISION_CODE) -> DEFINITIONS.GL_DIVISIONS(DIVISION_CODE)
- **CHECK** `CK_GL_DIVISION_LOC_HEADS`: ACTIVE IN ('Y', 'N'
- **Triggers**: `GL_DIVISION_LOC_HEADS_DEL` (after delete), `GL_DIVISION_LOC_HEADS_INS` (before insert), `GL_DIVISION_LOC_HEADS_UPD` (before update)

## DEFINITIONS.GRADES

| Column | Type | Null | Comment |
|---|---|---|---|
| GRADE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| OVER_TIME_ALLOWED | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_GRADES`: GRADE_ID
- **CHECK** `CK_GRADES_001`: OVER_TIME_ALLOWED IN ('Y','N'
- **Triggers**: `GRADES_CEA` (before insert or update or delete), `GRADES_DEL` (after delete), `GRADES_INS` (before insert), `GRADES_UPD` (before update), `TRG_WS_FFF_LL_CP_Q` (after insert or update or delete)

## DEFINITIONS.GRANT_TABS

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| MAIN_CANVAS | VARCHAR2(50) | Y |  |
| TAB_CANVAS_ID | VARCHAR2(5) | N |  |
| TAB_CANVAS_NAME | VARCHAR2(50) | N |  |
| TAB_DISPLAY_NAME | VARCHAR2(50) | N |  |
| ACTIVE | CHAR(1) | Y | This column contain Active Y='Yes', N='No' |
| ORDER_BY | VARCHAR2(2) | Y |  |

- **PK** `GRANT_TABS_002`: TAB_CANVAS_ID
- **UK** `GRANT_TABS_001`: TAB_CANVAS_NAME
- **Triggers**: `GRANT_TABS_CEA` (before insert or update or delete), `TRG_WS_FZS_HK_JQ_Q` (after insert or update or delete)

## DEFINITIONS.GROUP_ALERT

| Column | Type | Null | Comment |
|---|---|---|---|
| LIST_ID | VARCHAR2(5) | N | Auto generated number (FK) |
| DESIGNATION_CATEGORY_ID | VARCHAR2(3) | N | Designation category ID from DEFINITIONS.DESIGNATION_CATEGORY. |
| EMAIL | CHAR(1) | Y | Flag to mark if EMAIL should be sent. |
| SMS | CHAR(1) | Y | Flag to mark if SMS should be sent. |
| ACTIVE | CHAR(1) | Y | Flag to mark if record is Active or not. |

- **PK** `PK_GROUP_ALERT`: LIST_ID, DESIGNATION_CATEGORY_ID
- **FK** `FK_GROUP_ALERT_3`: (LIST_ID) -> DEFINITIONS.EMAIL_ALERT(LIST_ID)
- **CHECK** `CK_GROUP_ALERT_1`: EMAIL IN ('Y','N'
- **CHECK** `CK_GROUP_ALERT_2`: SMS IN ('Y','N'
- **CHECK** `CK_GROUP_ALERT_3`: ACTIVE IN ('Y','N'

## DEFINITIONS.GROUP_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(6) | N |  |
| GROUP_NAME | VARCHAR2(100) | Y |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| SECTION_PREFIX | VARCHAR2(3) | N |  |
| ORDER_BY | NUMBER(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_DEF_GROUP_CPT`: GROUP_ID, SECTION_PREFIX
- **Triggers**: `GROUP_CPT_CEA` (before insert or update or delete), `TRG_WS_LWR_JK_AI_Q` (after insert or update or delete)

## DEFINITIONS.GROUP_CPT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| GROUP_ID | VARCHAR2(6) | N |  |
| SECTION_PREFIX | VARCHAR2(3) | N |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **PK** `PK_GROUP_CPT_DETAIL`: CPT_ID, GROUP_ID, SECTION_PREFIX
- **Triggers**: `GROUP_CPT_DETAIL_CEA` (before insert or update or delete), `TRG_WS_PYK_CZ_IS_Q` (after insert or update or delete)

## DEFINITIONS.TEMPLATE_GROUP_TYPE_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| MAPPING_ID | NUMBER | N |  |
| TEMPLATE_ID | VARCHAR2(6) | Y |  |
| GROUP_TYPE_ID | NUMBER | Y |  |
| GROUP_ID | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| PARENT_MAPPING_ID | NUMBER | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_GROUP_TYPE_MAPPING`: MAPPING_ID
- **UK** `UK_GROUP_TYPE_MAPPING_1`: TEMPLATE_ID, GROUP_TYPE_ID, GROUP_ID
- **Triggers**: `TEMP_GROUP_TYPE_MAPPING_DEL` (after delete), `TEMP_GROUP_TYPE_MAPPING_INS` (before insert), `TEMP_GROUP_TYPE_MAPPING_UPD` (before update)

## DEFINITIONS.TREATMENT_ELEMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ELEMENT_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TREATMENT_ELEMENTS`: ELEMENT_ID
- **Triggers**: `TREATMENT_ELEMENTS_DEL` (after delete), `TREATMENT_ELEMENTS_INS` (before insert), `TREATMENT_ELEMENTS_UPD` (before update)

## DEFINITIONS.GROUP_ELEMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_MAPPING_ID | NUMBER | N |  |
| ELEMENT_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | Y |  |
| PARENT_ELEMENT | NUMBER | Y |  |
| DETAIL_AVAILABLE | CHAR(1) default 'N' | Y |  |
| DISPLAY_THE_SUMMARY | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_GROUP_ELEMENTS`: GROUP_MAPPING_ID, ELEMENT_ID
- **FK** `FK_GROUP_ELEMENTS_1`: (GROUP_MAPPING_ID) -> DEFINITIONS.TEMPLATE_GROUP_TYPE_MAPPING(MAPPING_ID)
- **FK** `FK_GROUP_ELEMENTS_2`: (ELEMENT_ID) -> DEFINITIONS.TREATMENT_ELEMENTS(ELEMENT_ID) [disabled]
- **Triggers**: `GROUP_ELEMENTS_DEL` (after delete), `GROUP_ELEMENTS_INS` (before insert), `GROUP_ELEMENTS_UPD` (before update)

## DEFINITIONS.GROUP_MAPPING_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_MAPPING_ID | VARCHAR2(3) | N |  |
| REFERENCE_KEY | VARCHAR2(500) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_GROUP_MAP_DETAIL`: GROUP_MAPPING_ID, REFERENCE_KEY
- **Triggers**: `GROUP_MAPPING_DETAIL_CEA` (before insert or update or delete), `TRG_WS_FAE_SN_ZJ_Q` (after insert or update or delete)

## DEFINITIONS.GROUP_MAPPING_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_MAPPING_ID | VARCHAR2(3) | N |  |
| DETAIL_DESCRIPTION | VARCHAR2(4000) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_GROUP_MAP_MASTER`: GROUP_MAPPING_ID
- **Triggers**: `GROUP_MAPPING_MASTER_CEA` (before insert or update or delete), `TRG_WS_MGX_UF_VO_Q` (after insert or update or delete)

## DEFINITIONS.GT_OBJECT_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| PARAM_ID | NUMBER | N |  |
| PARAM_NAME | VARCHAR2(100) | Y |  |
| PARAM_DISPLAY_NAME | VARCHAR2(100) | Y |  |
| PARAM_DATA_TYPE | VARCHAR2(100) | Y |  |
| PARAM_REQUIRED | CHAR(1) default 'N' | Y |  |
| PARAM_REQUIRED_ALERT | VARCHAR2(2000) | Y |  |
| PARAM_CHECK_DEFAULT | CHAR(1) default 'N' | Y |  |
| PARAM_DEFAULT_VALUE | VARCHAR2(100) | Y |  |
| PARAM_QUERY | VARCHAR2(3000) | Y |  |
| PARAM_DISPLAY | CHAR(1) default 'N' | Y |  |
| PARAM_VALUE | VARCHAR2(1000) | Y |  |
| RG_ID | VARCHAR2(100) | Y |  |
| PARAM_ORDER_BY | NUMBER | Y |  |

_No standard audit columns._


## DEFINITIONS.HEADING_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| HEADING_ID | NUMBER(4) | N |  |
| HEADING_DESC | VARCHAR2(250) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_HEADING_MASTER_01`: HEADING_ID
- **Triggers**: `HEADING_MASTER_CEA` (before insert or update or delete), `HEADING_MASTER_DEL` (after delete), `HEADING_MASTER_INS` (before insert), `HEADING_MASTER_UPD` (before update), `TRG_WS_JRF_UR_AK_Q` (after insert or update or delete)

## DEFINITIONS.HEADING_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER(4) | N |  |
| HEADING_ID | NUMBER(4) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| PARAM_DESC | VARCHAR2(250) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| TOXICITY | CHAR(1) | Y |  |
| TOXICITY_ORDER_BY | VARCHAR2(4) | Y |  |
| AGE_GROUP | VARCHAR2(1) default 'B' | Y | A = Adults , P = Peads , B = Both |

- **PK** `PK_HEADING_DETAIL_01`: PARAM_ID
- **FK** `FK_HEADING_DETAIL_1`: (HEADING_ID) -> DEFINITIONS.HEADING_MASTER(HEADING_ID) [disabled]
- **Triggers**: `HEADING_DETAIL_CEA` (before insert or update or delete), `HEADING_DETAIL_DEL` (after delete), `HEADING_DETAIL_INS` (before insert), `HEADING_DETAIL_UPD` (before update), `TRG_WS_WKN_CK_SU_Q` (after insert or update or delete)

## DEFINITIONS.HEALTH_CARE

| Column | Type | Null | Comment |
|---|---|---|---|
| HEALTH_CARE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_HEALTH_CARE`: HEALTH_CARE_ID
- **Triggers**: `HEALTH_CARE_DEL` (after delete), `HEALTH_CARE_INS` (before insert), `HEALTH_CARE_UPD` (before update)

## DEFINITIONS.RPT_HF_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| RPT_HF_SETUP_ID | CHAR(12) | N |  |
| ADDRESS | VARCHAR2(2000) | Y |  |
| PHONE | VARCHAR2(40) | Y |  |
| FAX | VARCHAR2(40) | Y |  |
| EMAIL | VARCHAR2(100) | Y |  |
| WEBSITE | VARCHAR2(60) | Y |  |
| L_HEADER_IMAGE | BLOB | Y | Landscape Header Image |
| L_FOOTER_IMAGE | BLOB | Y | Landscape Footer Image |
| HEADER_TYPE | CHAR(1) | N | I:Image, T:Text, B:Both |
| FOOTER_TYPE | CHAR(1) | N | I:Image, T:Text, B:Both |
| REPORT_HEADER | VARCHAR2(200) | Y |  |
| COPY_RIGHT | VARCHAR2(255) | Y |  |
| P_HEADER_IMAGE | BLOB | Y | Portrait Header Image |
| P_FOOTER_IMAGE | BLOB | Y | Portrait Footer Image |
| LOGO | BLOB | Y | Logo Image |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| L_HEADER_IMAGE_TYPE | VARCHAR2(4) | Y | File type e.g. JPEG, BMP, GIF etc |
| P_HEADER_IMAGE_TYPE | VARCHAR2(4) | Y | File type e.g. JPEG, BMP, GIF etc |
| L_FOOTER_IMAGE_TYPE | VARCHAR2(4) | Y | File type e.g. JPEG, BMP, GIF etc |
| P_FOOTER_IMAGE_TYPE | VARCHAR2(4) | Y | File type e.g. JPEG, BMP, GIF etc |
| LOGO_TYPE | VARCHAR2(4) | Y | File type e.g. JPEG, BMP, GIF etc |

- **PK** `PK_RPT_HF_SETUP`: RPT_HF_SETUP_ID
- **FK** `FK_RPT_HF_SETUP_01`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_RPT_HF_SETUP_02`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **Triggers**: `RPT_HF_SETUP_CEA` (before insert or update or delete), `RPT_HF_SETUP_DEL` (after delete), `RPT_HF_SETUP_INS` (before insert), `RPT_HF_SETUP_UPD` (before update), `TRG_WS_BHF_DD_GZ_Q` (after insert or update or delete)

## DEFINITIONS.HF_REMARKS_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| RPT_HF_SETUP_ID | CHAR(12) | N | This column is part of Primary key. It is a unique column. |
| REMARKS | VARCHAR2(600) | Y | This column contains remarks e.g accrediated remarks of CAP |
| ACTIVE | CHAR(1) | Y | This column containts Y=YES,N=NO |

- **PK** `PK_REMARKS__HF_SETUP_ID`: RPT_HF_SETUP_ID
- **FK** `FK_RPT_HF_SETUP_ID`: (RPT_HF_SETUP_ID) -> DEFINITIONS.RPT_HF_SETUP(RPT_HF_SETUP_ID)
- **Triggers**: `HF_REMARKS_SETUP_DEL` (after delete), `HF_REMARKS_SETUP_INS` (before insert), `HF_REMARKS_SETUP_UPD` (before update)

## DEFINITIONS.HISCURRENCY_RATE

| Column | Type | Null | Comment |
|---|---|---|---|
| CURRENCY_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| SYMBOL | VARCHAR2(10) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |
| EXCHANGE_RATE | NUMBER(7,4) | Y |  |
| CURRENCY_UPDATED | DATE | Y |  |

- **PK** `PK_HISCURRENT_SECURITY`: CURRENCY_ID
- **Triggers**: `HISCURRENCYRATE_TR` (before insert)

## DEFINITIONS.HIS_DOWNTIME_REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |

- **PK** `PK_HIS_DOWNTIME_REASON`: REASON_ID
- **CHECK** `CHK_HIS_DOWNTIME_REASON`: ACTIVE IN ('Y','N'

## DEFINITIONS.HIS_PROCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | NUMBER(7) | N |  |
| PROCESS_NAME | VARCHAR2(255) | Y |  |

- **PK** `PK_HIS_PROCESS`: PROCESS_ID
- **Triggers**: `HIS_PROCESS_CEA` (before insert or update or delete), `TRG_WS_EGR_LG_WV_Q` (after insert or update or delete)

## DEFINITIONS.HIS_PROCESS_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_ID | NUMBER(7) | N |  |
| MONTH | CHAR(6) | Y |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| EXECUTED | CHAR(1) | Y |  |

- **PK** `PK_HIS_PROCESS_STATUS`: PROCESS_ID, START_DATE, END_DATE
- **FK** `FK_HIS_PROCESS_STATUS_1`: (PROCESS_ID) -> DEFINITIONS.HIS_PROCESS(PROCESS_ID)

## DEFINITIONS.SCHEMAS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| NAME | VARCHAR2(30) | N |  |
| SCHEMA_TYPE_FLAG | CHAR(1) default 'T' | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| RTM_REQUIRED | CHAR(1) default 'Y' | N |  |
| RTM_CHECK | CHAR(1) default 'Y' | N |  |
| SCHEMA_LEVEL | NUMBER(3) default 999 | Y |  |
| SEND_EMAIL | CHAR(1) default 'N' | Y | This column contains flag to use email solution for specific module |
| EMAIL | VARCHAR2(30) | Y |  |
| AUDIT_SCHEMA_NAME | VARCHAR2(30) | Y |  |
| APP_ID | NUMBER | Y | This column contains the Oracle Apex application id. |
| ORDERBY_FROM_SEQ | NUMBER | Y | This column contains the ORDER BY FROM SEQUENCE USED IN MERGE MRNO PROCESS |
| ORDERBY_TO_SEQ | NUMBER | Y | This column contains the ORDER BY TO SEQUENCE USED IN MERGE MRNO PROCESS |

- **PK** `PK_SCHEMAS`: SCHEMA_ID
- **UK** `UK_SCHEMAS_01`: NAME
- **CHECK** `CK_SCHEMA_02`: NAME = UPPER(NAME
- **CHECK** `CK_SCHEMA_1`: SCHEMA_TYPE_FLAG IN ('T','D'
- **Triggers**: `SCHEMAS_CEA` (before insert or update or delete), `SCHEMAS_DEL` (after delete), `SCHEMAS_INS` (before insert), `SCHEMAS_UPD` (before update), `TRG_WS_CFE_JL_HL_Q` (after insert or update or delete)

## DEFINITIONS.HIS_SETUP_FORMS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| SETUP_DESC | VARCHAR2(200) | Y |  |
| COMMENTS | VARCHAR2(1000) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| DEV_TOOL | VARCHAR2(25) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_HIS_SETUP_FORMS_1`: SERIAL_NO, SCHEMA_ID
- **FK** `FK_HIS_SETUP_FORM_1`: (SCHEMA_ID) -> DEFINITIONS.SCHEMAS(SCHEMA_ID) [disabled]
- **Triggers**: `HIS_SETUP_FORMS_CEA` (before insert or update or delete), `TRG_WS_BGR_VJ_LM_Q` (after insert or update or delete)

## DEFINITIONS.HIS_TO_AD_OU_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| MAPPING_ID | NUMBER | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| OU_NAME | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_DEFAULT | CHAR(1) default 'N' | Y |  |

_No standard audit columns._


## DEFINITIONS.HOBBIES

| Column | Type | Null | Comment |
|---|---|---|---|
| HOBBY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_HOBBIES`: HOBBY_ID
- **Triggers**: `HOBBIES_CEA` (before insert or update or delete), `HOBBIES_DEL` (after delete), `HOBBIES_INS` (before insert), `HOBBIES_UPD` (before update), `TRG_WS_FSC_DS_DC_Q` (after insert or update or delete)

## DEFINITIONS.HOLIDAY

| Column | Type | Null | Comment |
|---|---|---|---|
| HOLIDAY_DATE | DATE | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_HOLIDAY`: HOLIDAY_DATE
- **Triggers**: `HOLIDAY_CEA` (before insert or update or delete), `HOLIDAY_DEL` (after delete), `HOLIDAY_INS` (before insert), `HOLIDAY_UPD` (before update), `TRG_WS_FWN_RA_DG_Q` (after insert or update or delete)

## DEFINITIONS.HOSPITAL

| Column | Type | Null | Comment |
|---|---|---|---|
| HOSPITAL_ID | VARCHAR2(7) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| ADDRESS | VARCHAR2(200) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_HOSPITAL`: HOSPITAL_ID
- **Triggers**: `HOSPITAL_DEL` (after delete), `HOSPITAL_INS` (before insert), `HOSPITAL_UPD` (before update)

## DEFINITIONS.ICD10TO9_I10GEM_2013

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO_10 | VARCHAR2(11) | N |  |
| ICDNO_9 | VARCHAR2(11) | N |  |
| ICD_FLAG | VARCHAR2(11) | N |  |


## DEFINITIONS.ICD10_CM_2014

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(10) | N |  |
| ICDNO | VARCHAR2(11) | N |  |
| CHAPTER_NO | VARCHAR2(5) | N |  |
| SHORT_DESC | VARCHAR2(500) | N |  |
| LONG_DESC | VARCHAR2(1000) | N |  |

- **PK** `PK_ICD10_CM`: SERIAL_NO

## DEFINITIONS.ICD10_PCS_2014

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(10) | N |  |
| ICDNO | VARCHAR2(11) | N |  |
| CHAPTER_NO | VARCHAR2(5) | N |  |
| SHORT_DESC | VARCHAR2(500) | N |  |
| LONG_DESC | VARCHAR2(1000) | N |  |

- **PK** `PK_ICD10_PCS`: SERIAL_NO

## DEFINITIONS.ICD9TO10_GEM_PCSI9_2013_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO_9 | VARCHAR2(11) | N |  |
| ICDNO_10 | VARCHAR2(11) | N |  |
| ICD_FLAG | VARCHAR2(11) | N |  |


## DEFINITIONS.ICD9TO10_I9GEM_2013_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO_9 | VARCHAR2(11) | N |  |
| ICDNO_10 | VARCHAR2(11) | N |  |
| ICD_FLAG | VARCHAR2(11) | N |  |


## DEFINITIONS.ICDO_3_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_GROUP_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_GROUP`: ICDO_3_GROUP_ID, LOCATION_ID
- **Triggers**: `ICDO_3_GROUP_CEA` (before insert or update or delete), `ICDO_3_GROUP_DEL` (after delete), `ICDO_3_GROUP_INS` (before insert), `ICDO_3_GROUP_INSRT` (before insert), `ICDO_3_GROUP_UPD` (before update), `TRG_WS_FQC_OK_ND_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_SYSTEM

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_SYSTEM_ID | VARCHAR2(3) | N |  |
| DESCRTPTION | VARCHAR2(60) | Y |  |
| GROUP_FROM | VARCHAR2(3) | Y |  |
| GROUP_TO | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_SYSTEM`: ICDO_3_SYSTEM_ID, LOCATION_ID
- **Triggers**: `ICDO_3_SYSTEM_CEA` (before insert or update or delete), `ICDO_3_SYSTEM_DEL` (after delete), `ICDO_3_SYSTEM_INS` (before insert), `ICDO_3_SYSTEM_INSRT` (before insert), `ICDO_3_SYSTEM_UPD` (before update), `TRG_WS_NSH_BY_ZA_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_ORGAN

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_SYSTEM_ID | VARCHAR2(3) | N |  |
| ICDO_3_ORGAN_ID | VARCHAR2(3) | N |  |
| ICDO_3_GROUP_ID | VARCHAR2(5) | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_ORGAN`: ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, LOCATION_ID
- **FK** `FK_ICDO_3_ORGAN_1`: (ICDO_3_GROUP_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_GROUP(ICDO_3_GROUP_ID, LOCATION_ID) [disabled]
- **FK** `FK_ICDO_3_ORGAN_2`: (ICDO_3_SYSTEM_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_SYSTEM(ICDO_3_SYSTEM_ID, LOCATION_ID) [disabled]
- **Triggers**: `ICDO_3_ORGAN_CEA` (before insert or update or delete), `ICDO_3_ORGAN_DEL` (after delete), `ICDO_3_ORGAN_INS` (before insert), `ICDO_3_ORGAN_INSRT` (before insert), `ICDO_3_ORGAN_UPD` (before update), `TRG_WS_YUR_DW_UB_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_PART

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_SYSTEM_ID | VARCHAR2(3) | N |  |
| ICDO_3_ORGAN_ID | VARCHAR2(3) | N |  |
| ICDO_3_PART_ID | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_PART`: ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, ICDO_3_PART_ID, LOCATION_ID
- **FK** `FK_ICDO_3_PART_1`: (ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_ORGAN(ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, LOCATION_ID) [disabled]
- **Triggers**: `ICDO_3_PART_CEA` (before insert or update or delete), `ICDO_3_PART_DEL` (after delete), `ICDO_3_PART_INS` (before insert), `ICDO_3_PART_INSRT` (before insert), `ICDO_3_PART_UPD` (before update), `TRG_WS_VXN_QD_FR_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_SYSTEM_ID | VARCHAR2(3) | N |  |
| ICDO_3_ORGAN_ID | VARCHAR2(3) | N |  |
| ICDO_3_PART_ID | VARCHAR2(2) | N |  |
| ICDO_3_CATEGORY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(150) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_CATEGORY`: ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, ICDO_3_PART_ID, ICDO_3_CATEGORY_ID, LOCATION_ID
- **FK** `FK_ICDO_3_CATEGORY_1`: (ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, ICDO_3_PART_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_PART(ICDO_3_SYSTEM_ID, ICDO_3_ORGAN_ID, ICDO_3_PART_ID, LOCATION_ID) [disabled]
- **Triggers**: `ICDO_3_CATEGORY_CEA` (before insert or update or delete), `ICDO_3_CATEGORY_INSRT` (before insert), `TRG_WS_VSF_BZ_BV_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_GROUP_STAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDO_3_GROUP_ID | VARCHAR2(5) | N |  |
| LINE_NO | NUMBER(2) | Y |  |
| STAGE_TYPE_ID | VARCHAR2(3) | N |  |
| STAGE_ID | VARCHAR2(5) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **FK** `FK_ICDO_3_GROUP_STAGE_1`: (ICDO_3_GROUP_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_GROUP(ICDO_3_GROUP_ID, LOCATION_ID) [disabled]
- **Triggers**: `ICDO_3_GROUP_STAGE_INSRT` (before insert)

## DEFINITIONS.ICDO_3_METASTASIS

| Column | Type | Null | Comment |
|---|---|---|---|
| METASTASIS_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_METASTASIS`: METASTASIS_ID, LOCATION_ID
- **Triggers**: `ICDO_3_METASTASIS_CEA` (before insert or update or delete), `ICDO_3_METASTASIS_INSRT` (before insert), `TRG_WS_XGD_OZ_BE_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_STAGE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| STAGE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_STAGE_TYPE`: STAGE_TYPE_ID, LOCATION_ID
- **Triggers**: `ICDO_3_STAGE_TYPE_CEA` (before insert or update or delete), `ICDO_3_STAGE_TYPE_DEL` (after delete), `ICDO_3_STAGE_TYPE_INS` (before insert), `ICDO_3_STAGE_TYPE_INSRT` (before insert), `ICDO_3_STAGE_TYPE_UPD` (before update), `TRG_WS_EIL_EX_WY_Q` (after insert or update or delete)

## DEFINITIONS.ICDO_3_STAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| STAGE_ID | VARCHAR2(5) | N |  |
| STAGE_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_ICDO_3_STAGE`: STAGE_ID, STAGE_TYPE_ID, LOCATION_ID
- **FK** `FK_ICDO_3_STAGE_1`: (STAGE_TYPE_ID, LOCATION_ID) -> DEFINITIONS.ICDO_3_STAGE_TYPE(STAGE_TYPE_ID, LOCATION_ID) [disabled]
- **Triggers**: `ICDO_3_STAGE_CEA` (before insert or update or delete), `ICDO_3_STAGE_DEL` (after delete), `ICDO_3_STAGE_INS` (before insert), `ICDO_3_STAGE_INSRT` (before insert), `ICDO_3_STAGE_UPD` (before update), `TRG_WS_RJG_XK_PL_Q` (after insert or update or delete)

## DEFINITIONS.ICD_BACKUP_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO | VARCHAR2(11) | Y |  |
| SHORT_DESC | VARCHAR2(4000) | Y |  |
| ICD_NO | VARCHAR2(11) | Y |  |
| LONG_DESC | VARCHAR2(4000) | Y |  |
| INCLUDES | VARCHAR2(2000) | Y |  |
| EXCLUDES | VARCHAR2(2000) | Y |  |
| SHORT_EQUAL | VARCHAR2(1) | Y |  |
| ICD_NO_4 | VARCHAR2(5) | Y |  |
| ICD_NO_3 | VARCHAR2(3) | Y |  |
| ESTIMATED_COST | NUMBER(10,2) | Y |  |
| ESTIMATED_DURATION | NUMBER(4) | Y |  |


## DEFINITIONS.ICD_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_CHAPTER_ID | VARCHAR2(3) | Y |  |
| ICD_GROUP_ID | VARCHAR2(3) | Y |  |
| ICD_CATEGORY_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ICD_CODE | VARCHAR2(11) | Y |  |
| VERSION | NUMBER default 10 | N |  |


## DEFINITIONS.ICD_CHAPTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_CHAPTER_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(120) | Y |  |
| ICD_CHAPTER_RANGE_FROM | VARCHAR2(11) | Y |  |
| ICD_CHAPTER_RANGE_TO | VARCHAR2(11) | Y |  |
| VERSION | NUMBER(2) default 10 | N |  |

- **PK** `PK_ICD_CHAPTER`: ICD_CHAPTER_ID, VERSION
- **Triggers**: `ICD_CHAPTER_CEA` (before insert or update or delete), `TRG_WS_VYJ_KR_GW_Q` (after insert or update or delete)

## DEFINITIONS.ICD_CONFIRMED_BY

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_CONFIRMED_BY_ID | VARCHAR2(11) | N |  |
| ICD_CONFIRMED_BY_DESC | VARCHAR2(60) | N |  |

- **PK** `PK_ICD_CONFIRMED_BY`: ICD_CONFIRMED_BY_ID
- **Triggers**: `ICD_CONFIRMED_BY_CEA` (before insert or update or delete), `ICD_CONFIRMED_BY_DEL` (after delete), `ICD_CONFIRMED_BY_INS` (before insert), `ICD_CONFIRMED_BY_UPD` (before update), `TRG_WS_YEA_EC_VG_Q` (after insert or update or delete)

## DEFINITIONS.ICD_DATA_UPDATE

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO | VARCHAR2(11) | Y |  |
| VERSION_NO | NUMBER(2) | Y |  |
| ICD_LONG_DESC | VARCHAR2(250) | Y |  |
| ICD_TYPE | VARCHAR2(25) | Y |  |
| PROCESS_STATUS | VARCHAR2(1) | Y | Value will be import through excel sheet values are : A -> Add,  D -> Inactive , R -> Revision |
| REMARKS | VARCHAR2(2000) | Y |  |
| PROCESS_DATE | DATE | Y |  |
| SR_NO | NUMBER(9) | N |  |

- **PK** `PK_ICD_DATA_UPDATE`: SR_NO
- **CHECK** `CHCK_ICD_TYPE`: ICD_TYPE IN('SURGICAL PROCEDURE','V CODE','PROCEDURE','E CODE','DIAGNOSTIC CODE','DIAGNOSIS CODE'
- **Triggers**: `ICD_DATA_UPDATE_DEL` (after delete), `ICD_DATA_UPDATE_INS` (before insert), `ICD_DATA_UPDATE_SR_NO` (before insert), `ICD_DATA_UPDATE_UPD` (before update)

## DEFINITIONS.ICD_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_CHAPTER_ID | VARCHAR2(3) | N |  |
| ICD_GROUP_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(120) | Y |  |
| ICD_GROUP_RANGE_FROM | VARCHAR2(11) | Y |  |
| ICD_GROUP_RANGE_TO | VARCHAR2(11) | Y |  |
| VERSION | NUMBER(2) default 10 | N |  |

- **PK** `PK_ICD_GROUP`: ICD_CHAPTER_ID, ICD_GROUP_ID, VERSION
- **Triggers**: `ICD_GROUP_CEA` (before insert or update or delete), `TRG_WS_TUR_EI_RF_Q` (after insert or update or delete)

## DEFINITIONS.ICD_LEVEL3

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_CHAPTER_ID | VARCHAR2(3) | N |  |
| ICD_GROUP_ID | VARCHAR2(3) | N |  |
| ICD_LEVEL3_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(120) | Y |  |
| ICD_RANGE_FROM | VARCHAR2(11) | Y |  |
| ICD_RANGE_TO | VARCHAR2(11) | Y |  |
| VERSION | NUMBER(2) default 10 | N |  |

- **PK** `PK_ICD_LEVEL3`: ICD_CHAPTER_ID, ICD_GROUP_ID, ICD_LEVEL3_ID, VERSION
- **Triggers**: `ICD_LEVEL3_CEA` (before insert or update or delete), `TRG_WS_TAI_HL_FS_Q` (after insert or update or delete)

## DEFINITIONS.ICD_MAPPING

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| OLD_ICDNO | VARCHAR2(11) | N |  |
| OLD_VERSION | NUMBER(2) | N |  |
| NEW_ICDNO | VARCHAR2(11) | N |  |
| NEW_VERSION | NUMBER(2) | N |  |
| ICD_FLAG | VARCHAR2(11) | Y |  |
| ICD_TYPE | VARCHAR2(25) | N |  |

- **PK** `PK_SR_OLDNEW_ICDNO`: SERIAL_NO, OLD_ICDNO, OLD_VERSION, NEW_ICDNO, NEW_VERSION
- **CHECK** `CHK_MAP_ICD_TYPE`: ICD_TYPE IN ('SURGICAL PROCEDURE','DIAGNOSTIC CODE','PROCEDURE','E CODE','V CODE'))
- **Triggers**: `ICD_MAPPING_CEA` (before insert or update or delete), `ICD_MAPPING_DEL` (after delete), `ICD_MAPPING_INS` (before insert), `ICD_MAPPING_UPD` (before update), `TRG_WS_KTT_RS_KU_Q` (after insert or update or delete)

## DEFINITIONS.ICD_O_3_ACTIVE_YEAR

| Column | Type | Null | Comment |
|---|---|---|---|
| YEAR_ID | CHAR(4) | N |  |
| ACTIVE_YEAR | CHAR(4) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_ICD_O_3_ACTIVE_YEAR`: YEAR_ID
- **UK** `UK_ICD_O_3_ACTIVE_YEAR_1`: ACTIVE_YEAR
- **CHECK** `CK_ICD_O_3_ACTIVE_YEAR_1`: ACTIVE IN ('Y','N'
- **Triggers**: `ICD_O_3_ACTIVE_YEAR_CEA` (before insert or update or delete), `TRG_WS_QDP_RW_TU_Q` (after insert or update or delete)

## DEFINITIONS.ICD_TEST_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO | VARCHAR2(11) | Y |  |
| ICD_NO | VARCHAR2(11) | Y |  |
| INCLUDES | VARCHAR2(2000) | Y |  |
| EXCLUDES | VARCHAR2(2000) | Y |  |
| SHORT_EQUAL | VARCHAR2(1) | Y |  |
| ICD_NO_4 | VARCHAR2(5) | Y |  |
| ICD_NO_3 | VARCHAR2(3) | Y |  |
| ESTIMATED_COST | NUMBER(10,2) | Y |  |
| ESTIMATED_DURATION | NUMBER(4) | Y |  |
| ADDITIONAL_ICD | VARCHAR2(1) | Y |  |
| SHORT_DESC_OLD | VARCHAR2(20) | Y |  |
| LONG_DESC_OLD | VARCHAR2(250) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| LONG_DESC | VARCHAR2(250) | Y |  |
| MED_DESC | VARCHAR2(100) | Y |  |


## DEFINITIONS.ICD_VERSION_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ICDNO | VARCHAR2(11) | Y |  |
| LONG_DESC | VARCHAR2(250) | Y |  |
| SERIAL_NO | NUMBER(4) | Y |  |
| OUTDATE | DATE | Y |  |
| OUTDATE_USER | VARCHAR2(30) | Y |  |
| OUTDATE_TERMINAL | VARCHAR2(30) | Y |  |
| SR_NO | NUMBER(9) | N |  |
| START_DATE | DATE | Y |  |

- **PK** `PK_ICD_VERSION_HISTORY`: SR_NO
- **Triggers**: `ICD_VERSION_HISTORY_SR_NO` (before insert)

## DEFINITIONS.IMMUNIZATION

| Column | Type | Null | Comment |
|---|---|---|---|
| IMMUNIZATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |

- **PK** `PK_IMMUNIZATION`: IMMUNIZATION_ID

## DEFINITIONS.IMMUNIZATION_BUP

| Column | Type | Null | Comment |
|---|---|---|---|
| IMMUNIZATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | N |  |

- **PK** `PK_IMMUNIZATION_BUP`: IMMUNIZATION_ID

## DEFINITIONS.INCOME

| Column | Type | Null | Comment |
|---|---|---|---|
| INCOME_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_INCOME`: INCOME_ID
- **Triggers**: `INCOME_CEA` (before insert or update or delete), `INCOME_DEL` (after delete), `INCOME_INS` (before insert), `INCOME_UPD` (before update), `TRG_WS_VFI_XW_HG_Q` (after insert or update or delete)

## DEFINITIONS.INCOME_SOURCE

| Column | Type | Null | Comment |
|---|---|---|---|
| INCOME_SOURCE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_INCOME_SOURCE`: INCOME_SOURCE_ID
- **Triggers**: `INCOME_SOURCE_CEA` (before insert or update or delete), `INCOME_SOURCE_DEL` (after delete), `INCOME_SOURCE_INS` (before insert), `INCOME_SOURCE_UPD` (before update), `TRG_WS_HCW_TG_GC_Q` (after insert or update or delete)

## DEFINITIONS.INELIGIBILITY_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| INELIGIBILITY_REASON_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_INELIGIBILITY_REASONS`: INELIGIBILITY_REASON_ID
- **Triggers**: `INELIGIBILITY_REASONS_CEA` (before insert or update or delete), `INELIGIBILITY_REASONS_DEL` (after delete), `INELIGIBILITY_REASONS_INS` (before insert), `INELIGIBILITY_REASONS_UPD` (before update), `TRG_WS_OPF_YY_IW_Q` (after insert or update or delete)

## DEFINITIONS.INFECTION_LIKELY_SOURCE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_INFECTION_LIKELY_SOURCE`: SERIAL_NO
- **Triggers**: `INFECTION_LIKELY_SOURCE_DEL` (after delete), `INFECTION_LIKELY_SOURCE_INS` (before insert), `INFECTION_LIKELY_SOURCE_UPD` (before update)

## DEFINITIONS.INFECTION_SCREENING_ANSWER

| Column | Type | Null | Comment |
|---|---|---|---|
| ANSWER_ID | VARCHAR2(6) | N |  |
| ANSWER_DESC | VARCHAR2(4000) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | Y |  |
| ANSWER_TYPE | VARCHAR2(1) | Y | G = Gneral , P = Patient Type Wise , D = User Department Nature Wise |
| ORDER_NO | NUMBER(6) | Y |  |
| NOTE_TEXT_QUESTION | VARCHAR2(4000) | Y |  |
| NOTE_TEXT_ANSWER | VARCHAR2(4000) | Y |  |

- **PK** `PK_SCREENING_ANSWER`: ANSWER_ID
- **Triggers**: `INFECTION_SCREENING_ANSWER_INS` (before insert), `INFECTION_SCREENING_ANSWER_UPD` (before update)

## DEFINITIONS.INITIAL_SCREEN_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| SETUP_TYPE | VARCHAR2(1) | N |  |
| SCREEN_ORDER | NUMBER(2) | Y |  |
| INITIAL_SCREEN | VARCHAR2(11) | N |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_INITIAL_SCREEN_SETUP`: MRNO, SETUP_TYPE, INITIAL_SCREEN
- **Triggers**: `INITIAL_SCREEN_SETUP_CEA` (before insert or update or delete), `TRG_WS_YGK_VJ_IN_Q` (after insert or update or delete), `TRG_WS_YHX_EP_YI_Q` (after insert or update or delete)

## DEFINITIONS.INQUIRY_EXTENSION

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | N | Department ID |
| EXTENSION_TYPE | CHAR(1) | N | Designationwise type like (Resident Doctor =R ) |
| EXTENSION | VARCHAR2(100) | Y | Using Extension |
| ACTIVE | CHAR(1) default 'N' | N | Y for active  N for inactive |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_DEPT_EXT_TYPE`: DEPARTMENT_ID, EXTENSION_TYPE, LOCATION_ID
- **FK** `FK_DEPT`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID)
- **Triggers**: `INQUIRY_EXTENSION_CEA` (before insert or update or delete), `INQUIRY_EXTENSION_INSERT` (before insert), `TRG_WS_EIQ_CE_LX_Q` (after insert or update or delete)

## DEFINITIONS.INSTRUCTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER(3) | N | Serial No. |
| ORDER_BY | NUMBER(3) | N | Display ordering |
| PRE_TEXT | VARCHAR2(200) | N | Display text Before Extension |
| POST_TEXT | VARCHAR2(300) | Y | Display text After Extension |
| EXTENSION_TYPE | CHAR(1) | N | Designationwise Extension |
| DR_SHOW_FIELD | VARCHAR2(500) | N | This field wil show Dr.Entry Screen |
| ACTIVE | CHAR(1) default 'N' | N | Y for Active and N for inactive |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_SR_NO`: SR_NO, LOCATION_ID
- **Triggers**: `INSTRUCTIONS_CEA` (before insert or update or delete), `INSTRUCTIONS_DEL` (after delete), `INSTRUCTIONS_INS` (before insert), `INSTRUCTIONS_INSERT` (before insert), `INSTRUCTIONS_UPD` (before update), `TRG_WS_ANA_II_UE_Q` (after insert or update or delete)

## DEFINITIONS.INVENTORY_CERTIFICATION

| Column | Type | Null | Comment |
|---|---|---|---|
| CERTIFICATION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_INVENTORY_CERTIFICATION`: CERTIFICATION_ID
- **Triggers**: `INVENTORY_CERTIFICATION_CEA` (before insert or update or delete), `INVENTORY_CERTIFICATION_DEL` (after delete), `INVENTORY_CERTIFICATION_INS` (before insert), `INVENTORY_CERTIFICATION_UPD` (before update), `TRG_WS_JCV_MJ_IX_Q` (after insert or update or delete)

## DEFINITIONS.INVESTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| INVESTMENT_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_INVESTMENT`: INVESTMENT_ID
- **Triggers**: `INVESTMENT_CEA` (before insert or update or delete), `INVESTMENT_DEL` (after delete), `INVESTMENT_INS` (before insert), `INVESTMENT_UPD` (before update), `TRG_WS_OWD_HO_MI_Q` (after insert or update or delete)

## DEFINITIONS.INVOICE_TOKEN_PRINT

| Column | Type | Null | Comment |
|---|---|---|---|
| INVOICE_TYPE_ID | VARCHAR2(3) | N |  |
| STORE_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_INV_TOKEN_PRINT`: INVOICE_TYPE_ID, STORE_ID, LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_INVOICE_TOKEN_PRINT_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **FK** `FK_INVOICE_TOKEN_PRINT_2`: (STORE_ID) -> ITEM.STORE(STORE_ID)
- **CHECK** `CK_INV_TOKEN_PRINT_1`: ACTIVE IN ('Y','N'
- **Triggers**: `INVOICE_TOKEN_PRINT_DEL` (after delete), `INVOICE_TOKEN_PRINT_INS` (before insert), `INVOICE_TOKEN_PRINT_UPD` (before update)

## DEFINITIONS.IPD_DISCHARGE_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(3) | N |  |
| EVENT_ID | NUMBER(3) | Y |  |
| EVENT_DESC | VARCHAR2(100) | Y |  |
| EVENT_SHORT | VARCHAR2(3) | Y |  |

- **PK** `IPD_DISCHARGE_EVENT_PK1`: SERIAL_NO
- **Triggers**: `IPD_DISCHARGE_EVENT_CEA` (before insert or update or delete), `IPD_DISCHARGE_EVENT_DEL` (after delete), `IPD_DISCHARGE_EVENT_INS` (before insert), `IPD_DISCHARGE_EVENT_UPD_2` (before update), `TRG_WS_LNT_YZ_MM_Q` (after insert or update or delete)

## DEFINITIONS.IP_ADDRESS

| Column | Type | Null | Comment |
|---|---|---|---|
| IP_ADDRESS | VARCHAR2(15) | N |  |
| IP_ROLE | VARCHAR2(60) | Y |  |
| COMMENTS | VARCHAR2(1000) | Y |  |

- **PK** `PK_IP_ADDRESS`: IP_ADDRESS
- **Triggers**: `IP_ADDRESS_DEL` (after delete), `IP_ADDRESS_INS` (before insert), `IP_ADDRESS_UPD` (before update)

## DEFINITIONS.ISOLATION_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| ISOLATION_STATUS_ID | VARCHAR2(3) | N |  |
| STATUS_DESCRIPTION | VARCHAR2(100) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_ISOLATION_STATUS`: ISOLATION_STATUS_ID
- **Triggers**: `ISOLATION_STATUS_CEA` (before insert or update or delete), `ISOLATION_STATUS_DEL` (after delete), `ISOLATION_STATUS_INS` (before insert), `ISOLATION_STATUS_UPD` (before update), `TRG_WS_IIS_XK_IR_Q` (after insert or update or delete)

## DEFINITIONS.ITEM_PROPERTY

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPERTY_ID | NUMBER(2) | N | This column contains Object Item Property ID(Unique ID) |
| PROPERTY_NAME | VARCHAR2(20) | N | This column contains Object Item Property Name |
| KEY_NAME | VARCHAR2(20) | N | This column contains Object Property Key Name i.e used in coding |
| STATIC_VALUE | CHAR(1) | N | This column contains Flag Information of Static Value property (Y=Static, N=Non Static) |
| ACTIVE | CHAR(1) | N | This column contains Flag Information of Status (Y=Active, N=Inactive) |

- **PK** `PK_ITEM_PROPERTY`: PROPERTY_ID
- **UK** `UK_ITEM_PROPERTY_1`: KEY_NAME
- **CHECK** `CK_ITEM_PROPERTY_1`: UPPER(KEY_NAME) = KEY_NAME
- **CHECK** `CK_ITEM_PROPERTY_2`: STATIC_VALUE IN ('Y','N'
- **CHECK** `CK_ITEM_PROPERTY_3`: ACTIVE IN ('Y','N'
- **Triggers**: `ITEM_PROPERTY_DEL` (after delete), `ITEM_PROPERTY_INS` (before insert), `ITEM_PROPERTY_UPD` (before update)

## DEFINITIONS.ITEM_PROPERTY_SOURCES

| Column | Type | Null | Comment |
|---|---|---|---|
| VALUE_SOURCE | CHAR(1) | N |  |
| SOURCE_DESC | VARCHAR2(200) | Y |  |
| STATIC_VALUE | CHAR(1) | Y |  |

- **PK** `PK_ITEM_PROPERTY_SOURCES`: VALUE_SOURCE
- **Triggers**: `ITEM_PROPERTY_SOURCES_DEL` (after delete), `ITEM_PROPERTY_SOURCES_INS` (before insert), `ITEM_PROPERTY_SOURCES_UPD` (before update)

## DEFINITIONS.ITEM_PROPERTY_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPERTY_ID | NUMBER(2) | N | Property ID Reference to DEFINITIONS.ITEM_PROPERTY |
| SERIAL_NO | NUMBER(2) | N | Property ID+Value Serial No (Unique ID) |
| VALUE_DESC | VARCHAR2(20) | N | This column contains Name/Description of Property Value |
| VALUE_KEY | VARCHAR2(10) | N | This column contains Value Key to apply |
| ACTIVE | CHAR(1) | N | This column contains Flag Information of Status (Y=Active, N=Inactive) |

- **PK** `PK_ITEM_PROPERTY_VALUES`: PROPERTY_ID, SERIAL_NO
- **UK** `UK_ITEM_PROPERTY_VALUE_1`: PROPERTY_ID, VALUE_KEY
- **FK** `FK_ITEM_PROPERTY_VALUES_1`: (PROPERTY_ID) -> DEFINITIONS.ITEM_PROPERTY(PROPERTY_ID)
- **CHECK** `CK_ITEM_PROPERTY_VALUES_1`: ACTIVE IN ('Y','N'
- **Triggers**: `ITEM_PROPERTY_VALUES_DEL` (after delete), `ITEM_PROPERTY_VALUES_INS` (before insert), `ITEM_PROPERTY_VALUES_UPD` (before update)

## DEFINITIONS.ITEM_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | NUMBER(3) | N | This column contains Object Item Type ID (Unique ID) |
| TYPE_NAME | VARCHAR2(20) | N | This column contains Object Item Type Description |
| ACTIVE | CHAR(1) | N | This column contains Flag Information of Status (Y=Active, N=Inactive) |

- **PK** `PK_ITEM_TYPES`: TYPE_ID
- **UK** `UK_ITEM_TYPES`: TYPE_NAME
- **CHECK** `CK_ITEM_TYPES_1`: ACTIVE IN ('Y','N'
- **Triggers**: `ITEM_TYPES_DEL` (after delete), `ITEM_TYPES_INS` (before insert), `ITEM_TYPES_UPD` (before update)

## DEFINITIONS.ITEM_TYPES_PROPERTY

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | NUMBER(3) | N | This column contains Item Type ID (Rerference DEFINITIONS.ITEM_TYPES) |
| PROPERTY_ID | NUMBER(2) | N | This column contains Item Property ID (Rerference DEFINITIONS.ITEM_PROPERTY) |
| VALUE_SOURCE | CHAR(1) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_ITEM_TYPES_PROPERTY`: TYPE_ID, PROPERTY_ID
- **FK** `FK_ITEM_TYPES_PROPERTY_1`: (TYPE_ID) -> DEFINITIONS.ITEM_TYPES(TYPE_ID)
- **FK** `FK_ITEM_TYPES_PROPERTY_2`: (PROPERTY_ID) -> DEFINITIONS.ITEM_PROPERTY(PROPERTY_ID) [disabled]
- **CHECK** `CK_ITEM_TYPES_PROPERTY_1`: VALUE_SOURCE IN ('O','D','S'
- **CHECK** `CK_ITEM_TYPES_PROPERTY_2`: ACTIVE IN ('Y','N'
- **Triggers**: `ITEM_TYPES_PROPERTY_DEL` (after delete), `ITEM_TYPES_PROPERTY_INS` (before insert), `ITEM_TYPES_PROPERTY_UPD` (before update)

## DEFINITIONS.JU

| Column | Type | Null | Comment |
|---|---|---|---|
| CLIENT_ID | VARCHAR2(10) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| PRICE | NUMBER(12,2) | N |  |


## DEFINITIONS.KCI_DECISIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| DECISION_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_KCI_DECISIONS`: DECISION_ID
- **Triggers**: `KCI_DECISIONS_DEL` (after delete), `KCI_DECISIONS_INS` (before insert), `KCI_DECISIONS_UPD` (before update)

## DEFINITIONS.KILL_PROCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| PROCESS_TYPE | VARCHAR2(12) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| CLOSING_COUNTER | NUMBER(4) | Y |  |
| FILE_PATH | VARCHAR2(1000) | Y |  |

- **PK** `PK_KILL_PROCESS`: PROCESS_TYPE

## DEFINITIONS.ZONES

| Column | Type | Null | Comment |
|---|---|---|---|
| ZONE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| SHORT_DESC | VARCHAR2(50) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ZONE_DISPLAY_NAME | VARCHAR2(60) | Y |  |
| ZONE_DISPLAY_ORDER | NUMBER(5) | Y |  |
| TERRITORY_KEY | NUMBER(3) | Y |  |
| ICON | BLOB | Y |  |
| SEPARATE_DB | CHAR(1) default 'Y' | N |  |

- **PK** `PK_ZONES`: ZONE_ID
- **UK** `UK_ZONES_03`: ORGANIZATION_ID, ZONE_ID
- **UK** `UK_ZONES_1`: DESCRIPTION
- **UK** `UK_ZONES_2`: SHORT_DESC
- **FK** `FK_ZONES_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **CHECK** `CHK_ZONES_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `ZONES_DEL` (after delete), `ZONES_INS` (before insert), `ZONES_UPD` (before update)

## DEFINITIONS.LABEL_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| LABEL_TYPE | VARCHAR2(1) | N |  |
| LABEL_DESCRIPTION | VARCHAR2(200) | Y |  |
| SHORT_DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| SHOW_EXPIRY | VARCHAR2(1) default 'Y' | Y | Y-> Show Expiry Date on Medicine Label, N -> Read Dosage Type Level Setup to show expiry |

- **PK** `PK_LABEL_TYPE`: LABEL_TYPE, ORG_ID, ZON_ID, LOC_ID
- **FK** `FK_LABEL_TYPE_01`: (ORG_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_LABEL_TYPE_02`: (ZON_ID) -> DEFINITIONS.ZONES(ZONE_ID) [disabled]
- **FK** `FK_LABEL_TYPE_03`: (LOC_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]

## DEFINITIONS.LANGUAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| LANGUAGE_TYPE | CHAR(1) | Y |  |

- **PK** `PK_LANGUAGES`: LANGUAGE_ID
- **Triggers**: `LANGUAGES_CEA` (before insert or update or delete), `LANGUAGES_DEL` (after delete), `LANGUAGES_INS` (before insert), `LANGUAGES_UPD` (before update), `TRG_WS_AWS_BU_WG_Q` (after insert or update or delete)

## DEFINITIONS.LANGUAGE_DETAIL_OBJECTWISE

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `LANGUAGE_DTL_OBJ_PK`: LANGUAGE_ID, OBJECT_CODE
- **Triggers**: `LANGUAGE_DETAIL_OBJECTWISE_CEA` (before insert or update or delete), `LANGUAGE_DETAIL_OBJECTWISE_DEL` (after delete), `LANGUAGE_DETAIL_OBJECTWISE_INS` (before insert), `LANGUAGE_DETAIL_OBJECTWISE_UPD` (before update), `TRG_WS_VKK_DQ_KN_Q` (after insert or update or delete)

## DEFINITIONS.LANGUAGE_WISE_COUNTING
THIS TABLE IS USED TO DEFINE MULTILINGUAL DOSAGE TYPE INSTRUCTIONS WHICH WILL BE PRINTED ON PHARMACY PRESCRIPTION AND LABEL

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| COUNTS | VARCHAR2(10) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR SINGULAR INSTRUCTIONS |
| LABEL_DESC1 | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR PLURAL INSTRUCTIONS |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_LANGUAGE_WISE_COUNTING`: LANGUAGE_ID, COUNTS
- **Triggers**: `LANGUAGE_WISE_COUNTING_CEA` (before insert or update or delete), `LANGUAGE_WISE_COUNTING_DEL` (after delete), `LANGUAGE_WISE_COUNTING_INS` (before insert), `LANGUAGE_WISE_COUNTING_UPD` (before update), `TRG_WS_JKA_VX_LL_Q` (after insert or update or delete)

## DEFINITIONS.LANKY_SCALE

| Column | Type | Null | Comment |
|---|---|---|---|
| RATING_ID | NUMBER | N |  |
| RATING_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y | Y-> Yes, N-> No |

- **PK** `PK_LANKY_SCALE`: RATING_ID

## DEFINITIONS.LEAVING_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| LEAVING_REASON_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_LEAVING_REASONS`: LEAVING_REASON_ID
- **Triggers**: `LEAVING_REASONS_CEA` (before insert or update or delete), `LEAVING_REASONS_DEL` (after delete), `LEAVING_REASONS_INS` (before insert), `LEAVING_REASONS_UPD` (before update), `TRG_WS_DNN_OO_FO_Q` (after insert or update or delete)

## DEFINITIONS.LINKED_CPT_RESTRICTION

| Column | Type | Null | Comment |
|---|---|---|---|
| NODE_ID | VARCHAR2(9) | N |  |
| PARENT_NODE_ID | VARCHAR2(9) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| LINK_CPT_ID | VARCHAR2(18) | Y |  |
| DURATION | NUMBER | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| SERVICE_TYPE | VARCHAR2(3) | Y |  |
| SETUP_TYPE | VARCHAR2(3) default 'LCR' | Y | LCR Link CPT Restriction with Duration, ROR Re-Ordering Restriction,CLR for CPT Link Restrction without Duration, FIS for Frat Infection Screening |
| ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| MESSAGE | VARCHAR2(1000) | Y |  |
| MESSAGE_TYPE | VARCHAR2(1) | Y |  |
| QUESTIONS | VARCHAR2(500) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| FRAT | VARCHAR2(1) default 'N' | Y |  |
| INFECTION_SCREENING | VARCHAR2(1) default 'N' | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_LINKED_CPT_RESTRICTION`: NODE_ID
- **FK** `FK_LINKED_CPT_RESTRICTION`: (PARENT_NODE_ID) -> DEFINITIONS.LINKED_CPT_RESTRICTION(NODE_ID)

## DEFINITIONS.LINKED_FREQUENCY

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | VARCHAR2(5) | Y |  |
| FREQUENCY_ID | VARCHAR2(5) | N |  |
| LINKED_FREQUENCY_ID | VARCHAR2(5) | N |  |
| SHORT_DESCRIPTION | VARCHAR2(15) | Y |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_FREQUENCY_ID`: FREQUENCY_ID, LINKED_FREQUENCY_ID
- **FK** `FK_FREQUENCY_ID`: (FREQUENCY_ID) -> DEFINITIONS.FREQUENCY(FREQUENCY_ID)
- **Triggers**: `LINKED_FREQUENCY_CEA` (before insert or update or delete), `LINKED_FREQUENCY_DEL` (after delete), `LINKED_FREQUENCY_INS` (before insert), `LINKED_FREQUENCY_UPD` (before update), `TRG_WS_AZZ_NN_JX_Q` (after insert or update or delete)

## DEFINITIONS.LINK_CPT_PACKAGE_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| CPT_TYPE | VARCHAR2(1) | N |  |
| PRICE | NUMBER(12,2) | N |  |
| CPT_BONUS | VARCHAR2(1) | Y |  |
| EMPLOYEE_ENTITLEMENT | VARCHAR2(1) | Y |  |
| IN_HOUSE_PERFORMED | VARCHAR2(1) | Y |  |
| COST | NUMBER(12,2) | Y |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| CONSULTANCY | VARCHAR2(1) | Y |  |
| STAT_CHARGEABLE | VARCHAR2(1) | N |  |
| CLEARANCE | VARCHAR2(1) | N |  |
| MOST_COMMONLY_USED | VARCHAR2(1) | N |  |
| NO_OF_PROCEDURES | NUMBER(2) | N |  |
| REP_ORDER | NUMBER(10) | Y |  |
| PAT_REPORT_CATEGORY_ID | VARCHAR2(3) | Y |  |
| DOCTOR_REQUIRED | VARCHAR2(1) | N |  |
| PATHOLOGY_COMMENT_TYPE_ID | VARCHAR2(3) | Y |  |
| MAX_QUANTITY_ALLOWED | VARCHAR2(1) | N |  |
| REPORTING_CASE | NUMBER(2) | Y |  |
| NO_OF_REPORTS | NUMBER(2) | Y |  |
| DUPLICATE_ACKNOWLEDGE | VARCHAR2(1) | N |  |
| SPECIMEN_NATURE_REQUIRED | CHAR(1) | N |  |
| SPECIMEN_SITE_REQUIRED | CHAR(1) | N |  |
| WORK_ORDER_PRINT | CHAR(1) | N |  |
| TECH_NORMAL | CHAR(1) | N |  |
| TECH_ABNORMAL | CHAR(1) | N |  |
| DOCTOR_NORMAL | CHAR(1) | N |  |
| DOCTOR_ABNORMAL | CHAR(1) | N |  |
| CONSULTANT_NORMAL | CHAR(1) | N |  |
| NOT_REPORTABLE | CHAR(1) | N |  |
| CONSULTANT_ABNORMAL | CHAR(1) | N |  |
| COMBINED_REPORT | CHAR(1) | N |  |
| REPORT_HEADING | VARCHAR2(100) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| SURGERY_REGION_ID | VARCHAR2(5) | Y |  |
| LENGTH_OF_STAY | NUMBER(2) | Y |  |
| AFTER_DEATH_ENTRY | CHAR(1) | Y |  |
| OPEN_PRICE | CHAR(1) | N |  |
| PERFORM_LOCATION_ID | VARCHAR2(3) | Y |  |
| MODALITY_ID | VARCHAR2(10) | Y |  |
| ACK_PERFORMANCE_REQ | CHAR(1) | N |  |
| IMAGE_REQUIRED | VARCHAR2(1) | N |  |
| SHARE_ON_PERFORM | CHAR(1) | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| ACTIVATED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| USER_DEFINED_DEPT | CHAR(1) | N |  |
| COMBINED_REPORT_NORMAL | CHAR(1) | N |  |
| COMBINED_REPORT_ABNORMAL | CHAR(1) | N |  |
| BLOCK_AUTO_INP_INVOICE | CHAR(1) | N |  |
| PRE_REQUISITES_CHK | CHAR(1) | Y |  |
| CPT_CATEGORY_ID_NEW | VARCHAR2(7) | Y |  |


## DEFINITIONS.LIST_DETAIL
This table is used to insert list detail values

| Column | Type | Null | Comment |
|---|---|---|---|
| LIST_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| TYPE | VARCHAR2(1) | Y | S - Smoking Status, P - Pain |
| ORDER_BY | NUMBER(3) | Y |  |
| ENABLE_OPEN_TEXT | VARCHAR2(1) | Y | This column is used to enable the the fields for open text |
| ACTIVE | VARCHAR2(1) | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_LIST_DETAIL`: LIST_ID
- **Triggers**: `LIST_DETAIL_CEA` (before insert or update or delete), `LIST_DETAIL_DEL` (after delete), `LIST_DETAIL_INS` (before insert), `LIST_DETAIL_UPD` (before update), `TRG_WS_CHA_JT_UE_Q` (after insert or update or delete)

## DEFINITIONS.LIST_ITEM_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOV_TYPE_ID | VARCHAR2(5) | N |  |
| LOV_TYPE_DESC | VARCHAR2(100) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| REMARKS | VARCHAR2(200) | Y |  |

- **PK** `PK_LOV_TYPE_ID`: LOV_TYPE_ID
- **UK** `UK_LOV_TYPE_DESC`: LOV_TYPE_DESC
- **CHECK** `CH_ACTIVE_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `LIST_ITEM_TYPE_CEA` (before insert or update or delete), `LIST_ITEM_TYPE_DEL` (after delete), `LIST_ITEM_TYPE_INS` (before insert), `LIST_ITEM_TYPE_UPD` (before update), `LOV_TYPE_NEW_ID` (before insert), `TRG_WS_TGT_QH_HN_Q` (after insert or update or delete)

## DEFINITIONS.LIST_ITEM_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| LOV_ID | VARCHAR2(7) | N |  |
| LOV_TYPE_ID | VARCHAR2(5) | N |  |
| LOV_DESC | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_LIST_ITEM_DETAIL_01`: LOV_ID
- **UK** `UK_LIST_ITEM_DETAIL_01`: LOV_TYPE_ID, LOV_DESC
- **FK** `FK_LIST_ITEM_DETAIL_01`: (LOV_TYPE_ID) -> DEFINITIONS.LIST_ITEM_TYPE(LOV_TYPE_ID)
- **CHECK** `CK_LIST_ITEM_DETAIL_01`: ACTIVE IN ('Y', 'N'
- **Triggers**: `LIST_ITEM_DETAIL_CEA` (before insert or update or delete), `LIST_ITEM_DETAIL_DEL` (after delete), `LIST_ITEM_DETAIL_INS` (before insert), `LIST_ITEM_DETAIL_UPD` (before update), `LOV_NEW_ID` (before insert), `TRG_WS_FOR_GD_BS_Q` (after insert or update or delete)

## DEFINITIONS.LIST_ITEM_DETAIL_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LOV_DETAIL | VARCHAR2(7) | N | This column contains Unique ID |
| LOV_ID | VARCHAR2(7) | N |  |
| NATURE_ID | VARCHAR2(3) | N |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | N |  |
| SECTION_PREFIX | VARCHAR2(3) | Y |  |
| PRINT_REPORT | VARCHAR2(1) default 'Y' | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_LIST_ITEM_DETAIL_S`: LOV_DETAIL
- **FK** `FK_LIST_ITEM_DETAIL_S_01`: (LOV_ID) -> DEFINITIONS.LIST_ITEM_DETAIL(LOV_ID)
- **CHECK** `CK_LIST_ITEM_DETAIL_S_01`: ACTIVE IN ('Y', 'N'
- **Triggers**: `LIST_ITEM_DETAIL_SETUP_CEA` (before insert or update or delete), `LIST_ITEM_DETAIL_SETUP_DEL` (after delete), `LIST_ITEM_DETAIL_SETUP_INS` (before insert), `LIST_ITEM_DETAIL_SETUP_UPD` (before update)

## DEFINITIONS.LLM_API_KEYS

| Column | Type | Null | Comment |
|---|---|---|---|
| LLM_API_ID | NUMBER | N |  |
| API_KEY | VARCHAR2(2000) | Y |  |
| EMAIL_ID | VARCHAR2(200) | Y |  |
| AUTH_KEY | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| API_TYPE | VARCHAR2(5) | Y |  |
| MODEL_PROVIDER_ID | NUMBER | Y |  |
| MAX_HIT | VARCHAR2(10) | Y |  |

- **PK** `PK_LLM_API_KEYS`: LLM_API_ID

## DEFINITIONS.LOCATION_ATTENDANCE_PROCESS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_GROUP_ID | NUMBER(5) | N |  |
| TRANSACTION_TYPE_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_LOCATION_ATTENDANCE_PROCESS`: LOCATION_GROUP_ID
- **Triggers**: `LOC_ATTENDANCE_PROCESS_DEL` (after delete), `LOC_ATTENDANCE_PROCESS_INS` (before insert), `LOC_ATTENDANCE_PROCESS_UPD` (before update)

## DEFINITIONS.LOCATION_EXTERNAL

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(300) | N |  |

- **PK** `PK_LOCATION_EXTERNAL`: LOCATION_ID
- **UK** `UK_LOCATION_EXTERNAL_1`: DESCRIPTION

## DEFINITIONS.LOCATION_PACKAGE_TYPE
This table will be used to link the Package Type with the Location

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Location Ref |
| PACKAGE_TYPE_ID | VARCHAR2(3) | N | Package Type Ref |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_LOCATION_PACKAGE_TYPE`: LOCATION_ID, PACKAGE_TYPE_ID
- **FK** `FK_LOCATION_PACKAGE_TYPE_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_LOCATION_PACKAGE_TYPE_2`: (PACKAGE_TYPE_ID) -> DEFINITIONS.PACKAGE_TYPE(PACKAGE_TYPE_ID) [disabled]
- **CHECK** `CK_LOCATION_PACKAGE_TYPE_1`: ACTIVE IN ('Y','N'
- **Triggers**: `LOCATION_PACKAGE_TYPE_DEL` (after delete), `LOCATION_PACKAGE_TYPE_INS` (before insert), `LOCATION_PACKAGE_TYPE_UPD` (before update)

## DEFINITIONS.PATIENT_CATEGORY
This Table will be used to define the Patient Categories, This table will be considered as System Constant

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_CATEGORY_ID | VARCHAR2(8) | N | This column will represents the Patient Category, Counter will start from 001 and increase with 1 |
| DESCRIPTION | VARCHAR2(120) | N | Name of the Patient Category e.g. Executive, Labour etc. |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PATIENT_CATEGORY`: PATIENT_CATEGORY_ID
- **UK** `UK_CATEGORY_DESC`: DESCRIPTION
- **CHECK** `CK_CATEGORY_1`: ACTIVE IN ('Y','N'
- **Triggers**: `PATIENT_CATEGORY_CEA` (before insert or update or delete), `PATIENT_CATEGORY_DEL` (after delete), `PATIENT_CATEGORY_INS` (before insert), `PATIENT_CATEGORY_UPD` (before update), `TRG_WS_JYY_CD_FM_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_PATIENT_CATEGORY
This table will be used to link the Patient Category with the Location

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | This column will represents the Location within an organization |
| PATIENT_CATEGORY_ID | VARCHAR2(8) | N | This column will represents the Patient Category |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_LOCATION_PATIENT_CATEGORY`: LOCATION_ID, PATIENT_CATEGORY_ID
- **FK** `FK_LOCATION_PATIENT_CATEGORY_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_LOCATION_PATIENT_CATEGORY_2`: (PATIENT_CATEGORY_ID) -> DEFINITIONS.PATIENT_CATEGORY(PATIENT_CATEGORY_ID) [disabled]
- **CHECK** `CK_LOCATION_PATIENT_CATEGORY_1`: ACTIVE IN ('Y','N'
- **Triggers**: `LOCATION_PATIENT_CATEGORY_DEL` (after delete), `LOCATION_PATIENT_CATEGORY_INS` (before insert), `LOCATION_PATIENT_CATEGORY_UPD` (before update)

## DEFINITIONS.LOCATION_RADIOLOGY

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Radiology Location ID Reference to definitions.location |
| LOCATION_DESC | VARCHAR2(60) | Y | Option Description of Location to Display |
| ACTIVE | CHAR(1) default 'N' | N | Active status of Locaiton (Y=Active,N=Inactive) |
| CONTINGENCY_FLAG | CHAR(1) default 'N' | N | Coningency status of Locaiton (Y=Active,N=Inactive) |
| CONTINGENCY_REMARKS | VARCHAR2(500) | Y | Coningency remarks |
| REPORTS_ONLINE | CHAR(1) default 'N' | N | Report of this Locaiton are available at Website( Y=Yes, N=No) |
| SEND_REPORTS | CHAR(1) default 'N' | N | Send reports to location/patient directly as PDF File |
| SEND_REPORTS_EMAIL | VARCHAR2(200) | Y | Send reports to location/patient Email Address |
| SEND_ALERTS | CHAR(1) default 'N' | N | Send Alerts to location |
| SEND_ALERTS_EMAIL | VARCHAR2(200) | Y | Send Alerts to location |

- **PK** `PK_LOCATION_RADIOLOGY`: LOCATION_ID
- **FK** `FK_LOCATION_RADIOLOGY_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **CHECK** `CK_LOCATION_RADIOLOGY_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_LOCATION_RADIOLOGY_2`: CONTINGENCY_FLAG IN ('Y','N'
- **CHECK** `CK_LOCATION_RADIOLOGY_3`: REPORTS_ONLINE IN ('Y','N'
- **CHECK** `CK_LOCATION_RADIOLOGY_4`: SEND_REPORTS IN ('Y','N'
- **CHECK** `CK_LOCATION_RADIOLOGY_5`: SEND_ALERTS IN ('Y','N'

## DEFINITIONS.LOCATION_SCHEMAS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | This column contains unique Location ID for Radiology service facility |
| SCHEMA_ID | VARCHAR2(3) | N | Module/Schema reference ID (eg S25=Pathology,S12=Radiology ) |
| LOCATION_DESC | VARCHAR2(150) | Y | This column contains Location Description/Name |
| SHORT_DESC | VARCHAR2(15) | Y | This column contains Short Description |
| PHONE_NO | VARCHAR2(40) | Y |  |
| FAX_NO | VARCHAR2(40) | Y |  |
| EMAIL | VARCHAR2(100) | Y | This column contains Email Address for Radiology Location |
| START_DATE | DATE | Y | Make active for transaction from date |
| CLOSE_DATE | DATE | Y | End date limit to keep active for transaction |
| SHOW_IN_REPORTS | CHAR(1) default 'Y' | N | Flag Information (Y=Show in reports menu,N=Do not show) |
| ORDER_BY | NUMBER(3) | N | This column contains order by information to display locations |

- **PK** `PK_LOCATION_SCHEMAS`: LOCATION_ID, SCHEMA_ID
- **FK** `FK_LOCATION_SCHEMAS_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **Triggers**: `LOCATION_SCHEMAS_CEA` (before insert or update or delete), `LOCATION_SCHEMAS_DEL` (after delete), `LOCATION_SCHEMAS_INS` (before insert), `LOCATION_SCHEMAS_UPD` (before update), `TRG_WS_ICK_FV_KR_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_WISE_BRAND

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| BRAND_ID | VARCHAR2(12) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_LOCATION_WISE_BRAND`: LOCATION_ID, BRAND_ID
- **CHECK** `CK_LOCATION_WISE_BRAND_1`: ACTIVE IN ('Y','N'

## DEFINITIONS.LOCATION_WISE_CC_RIDERS

| Column | Type | Null | Comment |
|---|---|---|---|
| DUTY_LOCATION_ID | VARCHAR2(3) | N |  |
| CC_RIDER_MRNO | VARCHAR2(14) | N |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_LOC_WISE_CC_RIDERS`: DUTY_LOCATION_ID, CC_RIDER_MRNO
- **Triggers**: `LOCATION_WISE_CC_RIDERS_DEL` (after delete), `LOCATION_WISE_CC_RIDERS_INS` (before insert), `LOCATION_WISE_CC_RIDERS_UPD` (before update)

## DEFINITIONS.LOCATION_WISE_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N | Active status flag Y=Yes,N=No |
| MAX_LIMIT | NUMBER(6) | Y | Location wise CPT maximum ordering limit |
| ORGANIZATION_ID | VARCHAR2(3) | Y | New Column is added by Billing Team , Purpose of this Column is to get CPT Price Organization Wise |
| PRICE | NUMBER(12,2) default 0 | Y |  |
| CONSENT_EVENT_ID | NUMBER(3) | Y | Consent required before this event |
| CONSENT_VALIDITY_DAYS | NUMBER(3) | Y | Consent validity in no. of days |
| DURATION_RESTRICTED | CHAR(1) default 'N' | Y | Use for duration restricted authorization |
| LAST_ORDER_VALUE_INHOUR | NUMBER(5) default 0 | N |  |
| PATIENT_TYPE_RESTRICTION | VARCHAR2(1) default 'N' | Y | Use for Patient type Restrictions |
| ORDER_STATUS_ID | VARCHAR2(3) default '001' | Y | Use for Location wise Order Status |
| PRICE_ACTIVE | CHAR(1) | Y | This column will be used to activate/ de-activate price of a cpt at specific location. |

- **PK** `PK_LOCATION_WISE_CPT`: LOCATION_ID, CPT_ID
- **CHECK** `CK_LOCATION_WISE_CPT_1`: ACTIVE IN ('Y','N'
- **Triggers**: `LOCATION_WISE_CPT_CEA` (before insert or update or delete), `LOCATION_WISE_CPT_DEL` (after delete), `LOCATION_WISE_CPT_INS` (before insert), `LOCATION_WISE_CPT_TS` (before insert or update or delete), `LOCATION_WISE_CPT_UPD` (before update), `TRG_WS_RMM_UV_FZ_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| CLINICAL_INFORMATION_REQUIRED | VARCHAR2(1) default 'N' | Y | Clinical information required 'Y' mean clinical information is mandatory to Order CPT. |
| PERFORMER_REQUIRED | VARCHAR2(1) default 'N' | Y | Performer Required 'Y' mean performer selection is mandatory to Order CPT. |

- **PK** `PK_LOCATION_WISE_CPT_DEPT_SECT`: LOCATION_ID, CPT_ID, DEPARTMENT_ID, SECTION_ID
- **UK** `UK_LOC_WISE_CPT_DEPT_SECT_01`: LOCATION_ID, CPT_ID, DEPARTMENT_ID
- **FK** `FK_LOC_WISE_CPT_DEPT_SECT_01`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_LOC_WISE_CPT_DEPT_SECT_02`: (DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.DEPARTMENT_SECTION(DEPARTMENT_ID, SECTION_ID) [disabled]
- **Triggers**: `LOCATION_WISE_CPT_DEPT_SECT_CEA` (before insert or update or delete), `SYS_LOC_WISE_CPT_DEPT_SECT_DEL` (after delete), `SYS_LOC_WISE_CPT_DEPT_SECT_INS` (before insert), `SYS_LOC_WISE_CPT_DEPT_SECT_UPD` (before update), `TRG_WS_RBO_QX_BC_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_WISE_CPT_PRICE_UPDATE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ITEM_ID | VARCHAR2(18) | N |  |
| EFFECTIVE_DATE | DATE | N |  |
| NEW_PRICE | NUMBER | N |  |
| PRICE_ACTIVE | CHAR(1) | Y |  |
| TRANS_DATE | DATE | Y |  |
| STATUS | CHAR(1) default 'P' | Y | "P" for Pending and "C"  for Completed |
| STATUS_UPDATE_DATE | DATE | Y |  |

_No standard audit columns._

- **PK** `PK_LOC_WISE_CPT_PRICE_UPDATE`: LOCATION_ID, ITEM_ID, EFFECTIVE_DATE

## DEFINITIONS.LOCATION_WISE_DBSERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| SERVICE_ID | VARCHAR2(4) | N |  |
| STANDBY_SERVICE_ID | VARCHAR2(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **FK** `FK_LOC_DBSERVICES1`: (SERVICE_ID) -> DEFINITIONS.DB_SERVICES(SERVICE_ID) [disabled]
- **FK** `FK_LOC_DBSERVICES2`: (STANDBY_SERVICE_ID) -> DEFINITIONS.DB_SERVICES(SERVICE_ID) [disabled]
- **Triggers**: `LOCATION_WISE_DBSERVICES_DEL` (after delete), `LOCATION_WISE_DBSERVICES_INS` (before insert), `LOCATION_WISE_DBSERVICES_UPD` (before update)

## DEFINITIONS.LOCATION_WISE_DIMENSIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| NAME | VARCHAR2(500) | Y |  |
| ADDRESS | VARCHAR2(1000) | Y |  |
| LATITUDE | VARCHAR2(50) | N |  |
| LONGITUDE | VARCHAR2(50) | N |  |
| PLUS_CODE | VARCHAR2(250) | Y |  |

- **PK** `PK_LOC_DIMENSION`: LOCATION_ID
- **FK** `FK_LOC_DIMENSION`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **Triggers**: `LOCATION_WISE_DIMENSIONS_DEL` (after delete), `LOCATION_WISE_DIMENSIONS_INS` (before insert), `LOCATION_WISE_DIMENSIONS_UPD` (before update)

## DEFINITIONS.LOCATION_WISE_GENERIC

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| GENERIC_ID | VARCHAR2(8) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_LOCATION_WISE_GENERIC`: LOCATION_ID, GENERIC_ID
- **CHECK** `CK_LOCATION_WISE_GENERIC_1`: ACTIVE IN ('Y','N'

## DEFINITIONS.LOCATION_WISE_MONTHS

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| MONTH | CHAR(6) | N |  |
| MON_START_DATE | DATE | N |  |
| MON_END_DATE | DATE | N |  |
| FLAG | VARCHAR2(1) | Y |  |
| MONTH_CLOSED | VARCHAR2(1) default 'N' | Y |  |
| NEXT_MONTH | VARCHAR2(1) default 'N' | Y |  |
| CURRENT_MONTH | VARCHAR2(1) default 'N' | Y |  |
| SHORT_DESC | VARCHAR2(15) | Y |  |
| PAY_FLAG | CHAR(1) | Y |  |
| PAY_PROCESS | CHAR(1) | Y |  |
| PAY_CALC_DATE | DATE | Y |  |
| PAY_POST_DATE | DATE | Y |  |
| PAY_START_DATE | DATE | Y |  |
| PAY_END_DATE | DATE | Y |  |
| LEAVE_BALANCE_CALC | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_LOCATION_WISE_MONTHS`: ORGANIZATION_ID, LOCATION_ID, MONTH
- **Triggers**: `LOCATION_WISE_MONTHS_CEA` (before insert or update or delete), `LOCATION_WISE_MONTHS_DEL` (after delete), `LOCATION_WISE_MONTHS_INS` (before insert), `LOCATION_WISE_MONTHS_UPD` (before update), `MONTHS_SYNC_INS` (before insert), `MONTHS_SYNC_UPD` (before update), `TRG_WS_YNC_SH_IK_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_WISE_OBJECT_SCHEDULE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| DAY_ID | NUMBER(1) | N |  |
| RESTRICTED_FROM | DATE | Y | use only time factor |
| RESTRICTED_UPTO | DATE | Y | use only time factor |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| STANDBY_RESTRICTED_FROM | DATE | Y | use only time factor |
| STANDBY_RESTRICTED_TO | DATE | Y | use only time factor |

- **PK** `LOC_ID_OBJ_CODE_PK`: LOCATION_ID, OBJECT_CODE, DAY_ID
- **FK** `DAY_ID_FK`: (DAY_ID) -> DEFINITIONS.DAY(DAY_ID) [disabled]
- **Triggers**: `LOC_OBJ_SCHEDULE_DEL` (after delete), `LOC_OBJ_SCHEDULE_INS` (before insert), `LOC_OBJ_SCHEDULE_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_CONSTANT

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_PATIENT_TYPE_CONSTANT`: CONSTANT_ID
- **Triggers**: `PATIENT_TYPE_CONSTANT_CEA` (before insert or update or delete), `PATIENT_TYPE_CONSTANT_DEL` (after delete), `PATIENT_TYPE_CONSTANT_INS` (before insert), `PATIENT_TYPE_CONSTANT_UPD` (before update), `TRG_WS_FTU_NC_CM_Q` (after insert or update or delete)

## DEFINITIONS.LOCATION_WISE_PATIENT_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| PREFIX_LOCTION_ID | VARCHAR2(3) | Y |  |
| DEFAULT_PATIENT_TYPE | CHAR(1) | Y |  |
| CONSTANT_ID | NUMBER(2) | Y |  |
| COUNTER | NUMBER(6) | Y |  |
| PREFIX | VARCHAR2(3) | Y |  |
| INTER_CONVERSION | NUMBER(3) | Y |  |
| YEAR_WISE_COUNTER | CHAR(1) default 'N' | N |  |
| DEFAULT_LOCATION | CHAR(1) | Y |  |
| CONTRACT_AT_RUNTIME | CHAR(1) | N | Values of this column must be Y and N. If vlaues of this column will be "N" then system will not attach the contracts at runtime, otherwise Invoice Procedure will attach the contracts at runtime and generate the invoice accordingly |
| CAFE_FACILITY_ALLOWED | CHAR(1) default 'N' | N | Values of this column must be Y or N, Y means Employee of this patient Type is allowed to buy food items from Cafe on Credit |
| EMP_SALARY_CHECK | CHAR(1) default 'Y' | N | It is a Common Business Rule that We will allow the employees who are on our payroll to buy Food Items from Cafe but there is some exception When a doctor is not on payroll then no need to check the Salary of that patient, in such cases Values of this column will be N |
| CREDIT_LIMIT_SAL_PERCENT | NUMBER(3) default 10 | N | How much an employee can avail of his/her salary as a Credit, This column is dependant of  above column (EMP_SALARY_CHECK), if values of the above column will be Y then this column is applicable |
| PROVIDENT_FUND_CHECK | CHAR(1) default 'Y' | N | If value of this column is Y then This Employee must be member of Provident Fund otherwise he/she is not eligible for Credit , if value of this column is N then System will not check the Provident Fund Membership |
| CAFE_FACILITY_ALLOW_PROBATION | CHAR(1) default 'N' | N | This column will be used to stop or allow the Employee for Cafe Facilities during Probation |
| PI_PAYMENT_GL_PAYROLL | CHAR(1) default 'N' | N | This column will be used for handling of Performer Practice Income through Payroll or GL, Practice Income Process will make decision on based of this flag and add payroll.allowance_deduction_detail table in case of G and Generate the GL voucher in case of G |
| CAFE_DEDUCTION_GL_PAYROLL | CHAR(1) default 'P' | N | This column will be used to define the setup whether Cafe Deduction of this Patient Type will be made through Payroll or GL. Values must be P and G, P for Payroll and G for GL |
| REG_VERIFICATION_REQUIRED | CHAR(1) default 'N' | Y | PURPOSE: Y -> REGISTRATION REQUIRED FOR PATIENT,   N-> NO REGISTRATION REQUIRED FOR PATIENT. |
| FOOD_COUPON_ALLOW | CHAR(1) default 'N' | N | Values of this Column will be Y or N, In case of Y system will generate the Food Coupon from invoice if other conditions meets, If values of this column is N then System will not generate the Food Coupon |
| REG_VERIFICATION_REQUIED | CHAR(1) default 'N' | Y |  |
| INVOICE_RETURN_PREFIX | CHAR(1) | Y | This column will be used to define the Invoice\ Return Prefix If New Invoice\ Return No. Counter is required for this  Patient Type, If Value of this column is not null then System will generate the Separate Invoice Counte for This patient Type and Add the Value of this column  in Invoice\ Return No. format :  LLL\|\|YY\|\|INVOICE_RETURN_PREFIX\|\|COUNTER_NO, Same Values will be added in Invoice and Return No. |
| ALLOW_BBK_PRODUCT_ORDERING | CHAR(1) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y | This Column will be used to save object code of form or report if any decision required based on patient type and location |
| URGENT | CHAR(1) default 'N' | Y | This column contains info about urgent applicable for Radiology and Nuclear Medicine if its value is Y |
| PATIENT_EDUCATION | CHAR(1) default 'N' | Y | This column contains info about patient education applicable for physician Notes |
| REPORT_VIEWED | CHAR(1) default 'N' | Y | This column contains info about patient report viewed by any doctor. Y=Viewed , N=Not Viewed |
| HIDE_TIME_GIVEN_PT_WO | CHAR(1) default 'N' | Y | This column contains flag Y=Yes , N=Not Time given to Patient need to be Hide or not |
| ADMISSION_ALLOWED | CHAR(1) default 'N' | N | This column will be used to restrict/ allow the admission on specific location for specific patient type, by default Admission is restricted for all patient types, user has to allow manually |
| CONTARCT_DAYS_FOR_CAFE | NUMBER default 0 | Y |  |
| TAX_EXEMPTION | CHAR(1) | Y |  |

- **PK** `PK_LOCATION_WISE_PATIENT_TYPES`: LOCATION_ID, PATIENT_TYPE_ID
- **FK** `FK_LOCATION_WISE_PATIENT_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_LOCATION_WISE_PATIENT_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_LOCATION_WISE_PATIENT_4`: (CONSTANT_ID) -> DEFINITIONS.PATIENT_TYPE_CONSTANT(CONSTANT_ID) [disabled]
- **CHECK** `CK_LOC_WISE_PATIENT_TYPES_01`: YEAR_WISE_COUNTER IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_09`: CREDIT_LIMIT_SAL_PERCENT BETWEEN 0 AND 100
- **CHECK** `CK_PATIENT_TYPE_10`: CAFE_FACILITY_ALLOWED IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_11`: EMP_SALARY_CHECK IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_12`: PROVIDENT_FUND_CHECK IN ('Y','N'
- **CHECK** `CK_PATIENT_TYPE_13`: PI_PAYMENT_GL_PAYROLL IN ('P','G','N'
- **CHECK** `CK_PATIENT_TYPE_14`: CAFE_DEDUCTION_GL_PAYROLL IN ('P','G'
- **CHECK** `CK_PATIENT_TYPE_8`: CONTRACT_AT_RUNTIME IN ('N','Y'
- **Triggers**: `LOC_WISE_PATIENT_DEL` (after delete), `LOC_WISE_PATIENT_INS` (before insert), `LOC_WISE_PATIENT_UPD` (before update)

## DEFINITIONS.LOCATION_WISE_RELATION

| Column | Type | Null | Comment |
|---|---|---|---|
| RELATION_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| AGE | NUMBER | Y |  |
| VALIDITY_DURATION | NUMBER(5,1) | Y |  |
| VALIDITY_DURATION_UNIT_ID | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MEDICAL_ALLOWED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `LOCATION_WISE_RELATION_PK`: RELATION_ID, LOCATION_ID
- **Triggers**: `LOCATION_WISE_RELATION_DEL` (after delete), `LOCATION_WISE_RELATION_INS` (before insert), `LOCATION_WISE_RELATION_UPD` (before update)

## DEFINITIONS.LOCATION_WISE_USERS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| USER_MRNO | VARCHAR2(14) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_LOCATION_WISE_USERS`: LOCATION_ID, USER_MRNO
- **FK** `FK_LOCATION_WISE_USERS_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_LOCATION_WISE_USERS_2`: (USER_MRNO) -> SECURITY.USERS(MRNO) [disabled]

## DEFINITIONS.LOC_ATTENDANCE_PROCESS_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_GROUP_ID | NUMBER(5) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_LOCATION_ATT_PROCESS_DTL`: LOCATION_GROUP_ID, LOCATION_ID

## DEFINITIONS.LOC_CPT_ROLE_REST_PERMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ROLE_ID | NUMBER(10) | N |  |
| RESTRICTION_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'DUR' | N | DUR mean Duration Restricted,PTR Patient Type Restriction |

- **PK** `PK_LOC_CPT_DUR_ROLE_REST`: CPT_ID, LOCATION_ID, ROLE_ID, RESTRICTION_CATEGORY
- **Triggers**: `LOC_CPT_ROLE_PERM_INSERT` (before insert), `LOC_CPT_ROLE_REST_PERMIT_CEA` (before insert or update or delete), `TRG_WS_UEC_RX_SG_Q` (after insert or update or delete)

## DEFINITIONS.LOC_DOSAGE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DOSAGE_TYPE_ID | VARCHAR2(5) | Y |  |
| SUCCESS | VARCHAR2(1) | Y |  |
| TRANS_DATTM | DATE | Y |  |

- **PK** `PK_LOC_DOSAGE_TYPE`: LOCATION_ID, DOSAGE_TYPE_ID
- **Triggers**: `LOC_DOSAGE_TYPE_DEL` (after delete), `LOC_DOSAGE_TYPE_INS` (before insert), `LOC_DOSAGE_TYPE_UPD` (before update)

## DEFINITIONS.LOC_HF_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| FROM_DATE | DATE | N |  |
| RPT_HF_SETUP_ID | CHAR(12) | N |  |

- **PK** `PK_LOC_HF_SETUP`: LOCATION_ID, FROM_DATE
- **FK** `FK_LOC_HF_SETUP_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_LOC_HF_SETUP_2`: (RPT_HF_SETUP_ID) -> DEFINITIONS.RPT_HF_SETUP(RPT_HF_SETUP_ID) [disabled]
- **Triggers**: `LOC_HF_SETUP_DEL` (after delete), `LOC_HF_SETUP_INS` (before insert), `LOC_HF_SETUP_UPD` (before update)

## DEFINITIONS.LOC_UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| UNIT_ID | VARCHAR2(5) | N |  |
| SUCCESS | VARCHAR2(1) | Y |  |
| TRANS_DATTM | DATE | Y |  |

- **PK** `PK_LOC_UNIT`: LOCATION_ID, UNIT_ID

## DEFINITIONS.LOC_WISE_CONSENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| CONSENT_FORM_TYPE | VARCHAR2(2) | Y | T -> Transfusion of Blood Products A -> Anaesthesia & Sedation Services O -> Operation / Procedure C -> Chemotherapy Administration R -> Radionuclide Therapy P -> Therapeutic Apheresis PP -> Plasmapheresis (Plasma Exchange) PT -> Therapeutic Plateletpheresis PL -> Leukapheresis |
| QUEUE_GENERATION | VARCHAR2(1) default 'N' | Y | This flag will return either generate consent queues org loc wise or not, if flag reflects Y mean generate queues for N no queue will be generated and consent will be complete on sign |
| DIGITALLY_SIGN | VARCHAR2(1) default 'N' | Y | Y => DIGITALLY SIGN REQUIRED , N => NOT REQUIRED |

- **PK** `PK_LOC_WISE_CONSENT_TYPE`: SR_NO
- **UK** `UK_LOC_WISE_CONSENT_TYPE`: CONSENT_FORM_TYPE, LOC_ID
- **FK** `FK_LOC_WISE_CONSENT_TYPE`: (CONSENT_FORM_TYPE) -> DEFINITIONS.CONSENT_TYPE(CONSENT_FORM_TYPE)
- **Triggers**: `LOC_WISE_CONSENT_TYPE_INS` (before insert), `LOC_WISE_CONSENT_TYPE_UPD` (before update)

## DEFINITIONS.LOC_WISE_PAT_TYPE_RESTRICTION

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PATIENT_TYPE_RESTRICTION | VARCHAR2(1) default 'N' | Y | Use for Patient type Restrictions |

- **PK** `PK_LOC_PAT_TYPE_RESTRICTION`: PATIENT_TYPE_ID, LOCATION_ID
- **Triggers**: `LOC_WISE_PAT_TYPE_RESTRICTION_CEA` (before insert or update or delete), `TRG_WS_XOY_UU_FC_Q` (after insert or update or delete)

## DEFINITIONS.LOC_WISE_PHARMACY_STORE

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| PHYSICAL_LOCATION_ID | VARCHAR2(3) | N |  |
| STORE_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_LOC_WISE_PHARMACY_STORE`: ORGANIZATION_ID, PHYSICAL_LOCATION_ID, STORE_ID
- **Triggers**: `LOC_WISE_PHARMACY_STORE_CEA` (before insert or update or delete), `TRG_WS_ZKH_ZA_WB_Q` (after insert or update or delete)

## DEFINITIONS.LOC_WISE_RECEIVE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N | Active status flag Y=Yes,N=No |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_LOC_WISE_RECEIVE_SETUP`: LOCATION_ID, CPT_ID
- **CHECK** `CK_LOC_WISE_RECEIVE_SETUP_1`: ACTIVE IN ('Y','N'
- **Triggers**: `LOC_WISE_RECEIVE_SETUP_DEL` (after delete), `LOC_WISE_RECEIVE_SETUP_INS` (before insert), `LOC_WISE_RECEIVE_SETUP_UPD` (before update)

## DEFINITIONS.LOOKUP_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOOKUP_TYPE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(40) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_LOOKUP_TYPE`: LOOKUP_TYPE_ID
- **Triggers**: `LOOKUP_TYPE_DEL` (after delete), `LOOKUP_TYPE_INS` (before insert), `LOOKUP_TYPE_UPD` (before update)

## DEFINITIONS.LOOKUP_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| VALUE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(40) | N |  |
| LOOKUP_TYPE_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_LOOKUP_VALUES`: VALUE_ID
- **FK** `FK_LOOKUP_VALUES_1`: (LOOKUP_TYPE_ID) -> DEFINITIONS.LOOKUP_TYPE(LOOKUP_TYPE_ID) [disabled]
- **Triggers**: `LOOKUP_VALUES_DEL` (after delete), `LOOKUP_VALUES_INS` (before insert), `LOOKUP_VALUES_UPD` (before update)

## DEFINITIONS.LOU_SERVICES_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_ID | VARCHAR2(5) | N |  |
| SERVICE_DESC | VARCHAR2(500) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CLEARANCE_STATUS_ID | VARCHAR2(3) | Y |  |
| SPECIALTY_ID | VARCHAR2(6) | Y |  |
| ALERT_TEXT | VARCHAR2(1000) | Y |  |

- **PK** `PK_LOU_SERVICE_SETUP`: SERVICE_ID
- **Triggers**: `LOU_SERVICES_SETUP_DEL` (after delete), `LOU_SERVICES_SETUP_INS` (before insert), `LOU_SERVICES_SETUP_UPD` (before update)

## DEFINITIONS.LOU_SERVICES_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIALTY_ID | VARCHAR2(6) | N |  |
| SERVICE_ID | VARCHAR2(5) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_LOU_SERV_DET`: SPECIALTY_ID, SERVICE_ID
- **FK** `FK_LOU_SERV_DET`: (SERVICE_ID) -> DEFINITIONS.LOU_SERVICES_SETUP(SERVICE_ID) [disabled]
- **Triggers**: `LOU_SERVICES_SETUP_DETAIL_DEL` (after delete), `LOU_SERVICES_SETUP_DETAIL_INS` (before insert), `LOU_SERVICES_SETUP_DETAIL_UPD` (before update)

## DEFINITIONS.LOV_SHORT

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| LOV_NAME | VARCHAR2(30) | Y |  |
| LOV_PK | VARCHAR2(60) | Y |  |

_No standard audit columns._


## DEFINITIONS.MAC_ADDRESS

| Column | Type | Null | Comment |
|---|---|---|---|
| MAC_ADDRESS | VARCHAR2(50) | N |  |

- **PK** `PK_MAC_ADDRESS`: MAC_ADDRESS
- **Triggers**: `MAC_ADDRESS_DEL` (after delete), `MAC_ADDRESS_INS` (before insert), `MAC_ADDRESS_UPD` (before update)

## DEFINITIONS.MAINTENANCE_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(7) | N |  |
| CATEGORY_DESC | VARCHAR2(1000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_CATEGORY_ID`: CATEGORY_ID
- **Triggers**: `MAINTENANCE_CATEGORY_DEL` (after delete), `MAINTENANCE_CATEGORY_INS` (before insert), `MAINTENANCE_CATEGORY_UPD` (before update)

## DEFINITIONS.MAINTENANCE_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(7) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_MAINTENANCE_DPET_ID`: CATEGORY_ID, DEPARTMENT_ID
- **UK** `UK_MAINTENANCE_DPT`: DEPARTMENT_ID
- **Triggers**: `MAINTENANCE_DEPARTMENT_DEL` (after delete), `MAINTENANCE_DEPARTMENT_INS` (before insert), `MAINTENANCE_DEPARTMENT_UPD` (before update)

## DEFINITIONS.MAPPING_NATURE_ID

| Column | Type | Null | Comment |
|---|---|---|---|
| NATURE_ID | VARCHAR2(3) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_DEFINITIONS_001`: NATURE_ID, DEPARTMENT_ID, DEPARTMENT_NATURE_ID
- **Triggers**: `MAPPING_NATURE_ID_INS` (before insert), `MAPPING_NATURE_ID_UPD` (before update)

## DEFINITIONS.MARITAL_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| MARITAL_STATUS_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| STATUS | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| MARRIED_STATUS | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_MARITAL_STATUS`: MARITAL_STATUS_ID
- **CHECK** `CK_MARITAL_STATUS_001`: STATUS IN ('M','U'
- **Triggers**: `MARITAL_STATUS_CEA` (before insert or update or delete), `MARITAL_STATUS_DEL` (after delete), `MARITAL_STATUS_INS` (before insert), `MARITAL_STATUS_UPD` (before update), `TRG_WS_CQI_NW_TT_Q` (after insert or update or delete)

## DEFINITIONS.MASTER_TEMPLATE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| REF_TEMPLATE_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ALERT_TEXT | VARCHAR2(1000) | Y |  |

- **PK** `PK_MTS`: TEMPLATE_ID, REF_TEMPLATE_ID
- **Triggers**: `MASTER_TEMPLATE_SETUP_DEL` (after delete), `MASTER_TEMPLATE_SETUP_INS` (before insert), `MASTER_TEMPLATE_SETUP_UPD` (before update)

## DEFINITIONS.MEDICAL_ABBREVIATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| ABBREVIATION | VARCHAR2(15) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |

- **PK** `PK_MEDICAL_ABBREVIATIONS`: ABBREVIATION
- **Triggers**: `MEDICAL_ABBREVIATIONS_CEA` (before insert or update or delete), `TRG_WS_BRA_DP_PY_Q` (after insert or update or delete)

## DEFINITIONS.MEDICAL_CONDITIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| ICD_NO | VARCHAR2(11) | N |  |
| MEDICAL_CONDITION_DESC | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_MEDICAL_CONDITIONS`: ICD_NO
- **Triggers**: `MEDICAL_CONDITIONS_CEA` (before insert or update or delete), `MEDICAL_CONDITIONS_DEL` (after delete), `MEDICAL_CONDITIONS_INS` (before insert), `MEDICAL_CONDITIONS_UPD` (before update), `TRG_WS_JOB_YD_LK_Q` (after insert or update or delete)

## DEFINITIONS.MEDICAL_DEVICES
This table is used to store then setup data of medicine devices.

| Column | Type | Null | Comment |
|---|---|---|---|
| MEDICAL_DEVICE_ID | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y | Y - Active, N - Inactive. |
| ORDER_BY | NUMBER | Y | This column is used to store the order by value. |

- **PK** `PK_MEDICAL_DEVICES`: MEDICAL_DEVICE_ID
- **Triggers**: `MEDICAL_DEVICES_DEL` (after delete), `MEDICAL_DEVICES_INS` (before insert), `MEDICAL_DEVICES_UPD` (before update)

## DEFINITIONS.MEDICATION_ADMIN_TIME

| Column | Type | Null | Comment |
|---|---|---|---|
| MEDICATION_ADMIN_TIME_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| HOURS | NUMBER(10,4) | Y | Numeric value in hours using formula as ROUND(required_hours/24_hours,2) |
| ACTIVE | CHAR(1) | Y |  |
| HOURS_TO_SHOW | VARCHAR2(50) | Y | Data to show in message etc. |
| HOURS_N | NUMBER(8,2) | Y |  |

- **PK** `PK_MEDICATION_ADMIN_TIME`: MEDICATION_ADMIN_TIME_ID
- **Triggers**: `MEDICATION_ADMIN_TIME_DEL` (after delete), `MEDICATION_ADMIN_TIME_INS` (before insert), `MEDICATION_ADMIN_TIME_UPD` (before update)

## DEFINITIONS.MEDICINE_REVIEW_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| REVIEW_TYPE_ID | VARCHAR2(3) | N | 001-> Appropriateness review of emergency stocked medicines |
| SERIAL_NO | NUMBER | N |  |
| GENERIC_ID | VARCHAR2(8) | Y |  |
| DOSAGE_TYPE_ID | VARCHAR2(5) | Y |  |
| IPD_OPD | VARCHAR2(1) | Y | I-> IPD , O-> OPD |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y | Currently it will be used as patient location id for inpatient |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_MEDICINE_REVIEW_SETUP`: REVIEW_TYPE_ID, SERIAL_NO
- **Triggers**: `MEDICINE_REVIEW_SETUP_DEL` (after delete), `MEDICINE_REVIEW_SETUP_INS` (before insert), `MEDICINE_REVIEW_SETUP_UPD` (before update)

## DEFINITIONS.MEDICINE_REV_EXEMPTED_LOC

| Column | Type | Null | Comment |
|---|---|---|---|
| REVIEW_TYPE_ID | VARCHAR2(3) | N | 001-> Appropriateness review of emergency stocked medicines |
| SERIAL_NO | NUMBER | N | Reference of DEFINITIONS.MEDICINE_REVIEW_SETUP.SERIAL_NO |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_MEDICINE_REV_EXEMPTED_LOC`: REVIEW_TYPE_ID, SERIAL_NO, ORG_ID, LOC_ID, ORDER_LOCATION_ID
- **FK** `FK_MEDICINE_REV_EXEMPTED_LOC`: (REVIEW_TYPE_ID, SERIAL_NO) -> DEFINITIONS.MEDICINE_REVIEW_SETUP(REVIEW_TYPE_ID, SERIAL_NO)
- **Triggers**: `MEDICINE_REV_EXEMPTED_LOC_DEL` (after delete), `MEDICINE_REV_EXEMPTED_LOC_INS` (before insert), `MEDICINE_REV_EXEMPTED_LOC_UPD` (before update)

## DEFINITIONS.MED_REVIEW_SETUP_CLINIC

| Column | Type | Null | Comment |
|---|---|---|---|
| REVIEW_TYPE_ID | VARCHAR2(3) | N | 001-> Appropriateness review of emergency stocked medicines |
| SERIAL_NO | NUMBER | N |  |
| GENERIC_ID | VARCHAR2(8) | Y |  |
| DOSAGE_TYPE_ID | VARCHAR2(5) | Y |  |
| IPD_OPD | VARCHAR2(1) | Y | I-> IPD , O-> OPD |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_MED_REVIEW_CLINIC_SETUP`: REVIEW_TYPE_ID, SERIAL_NO
- **Triggers**: `MED_REVIEW_SETUP_CLINIC_DEL` (after delete), `MED_REVIEW_SETUP_CLINIC_INS` (before insert), `MED_REVIEW_SETUP_CLINIC_UPD` (before update)

## DEFINITIONS.MED_REVIEW_SETUP_DEPT

| Column | Type | Null | Comment |
|---|---|---|---|
| REVIEW_TYPE_ID | VARCHAR2(3) | N | 001-> Appropriateness review of emergency stocked medicines |
| SERIAL_NO | NUMBER | N |  |
| GENERIC_ID | VARCHAR2(8) | Y |  |
| DOSAGE_TYPE_ID | VARCHAR2(5) | Y |  |
| IPD_OPD | VARCHAR2(1) | Y | I-> IPD , O-> OPD |
| DEPT_ID | VARCHAR2(7) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_MED_REVIEW_SETUP`: REVIEW_TYPE_ID, SERIAL_NO
- **Triggers**: `MED_REVIEW_SETUP_DEPT_DEL` (after delete), `MED_REVIEW_SETUP_DEPT_INS` (before insert), `MED_REVIEW_SETUP_DEPT_UPD` (before update)

## DEFINITIONS.MENU_SHORT_KEYS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(4) | Y |  |
| SHORT_KEY | VARCHAR2(5) | N |  |

- **PK** `PK_MENU_SHORT_KEY`: SHORT_KEY
- **Triggers**: `MENU_SHORT_KEYS_CEA` (before insert or update or delete), `MENU_SHORT_KEYS_DEL` (after delete), `MENU_SHORT_KEYS_INS` (before insert), `MENU_SHORT_KEYS_UPD` (before update), `TRG_WS_CAT_ZH_JI_Q` (after insert or update or delete)

## DEFINITIONS.MESSAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| MESSAGE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_DEF_MESSAGE_ID`: OBJECT_CODE, MESSAGE_ID
- **FK** `FK_DEF_MESSAGE_OBJECT_CODE`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `MESSAGE_DEL` (after delete), `MESSAGE_INS` (before insert), `MESSAGE_UPD` (before update)

## DEFINITIONS.METHOD

| Column | Type | Null | Comment |
|---|---|---|---|
| METHOD | VARCHAR2(20) | N | WEBLOGIC/API Name |

- **PK** `PK_METHOD`: METHOD
- **CHECK** `CK_PK_METHOD_1`: METHOD = UPPER(METHOD
- **Triggers**: `METHOD_CEA` (before insert or update or delete), `TRG_WS_JLD_IS_HJ_Q` (after insert or update or delete)

## DEFINITIONS.MI

| Column | Type | Null | Comment |
|---|---|---|---|
| CLIENT_ID | VARCHAR2(10) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| PRICE | NUMBER(12,2) | N |  |


## DEFINITIONS.MICRO_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_ID | VARCHAR2(9) | N |  |
| SERVICE_NAME | VARCHAR2(100) | Y |  |
| SERVICE_DESC | VARCHAR2(100) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| PARENT_LOCATION | VARCHAR2(3) | Y |  |
| CURRENT_LOCATION | CHAR(1) default 'N' | N |  |
| APPLICATION_ID | VARCHAR2(50) | Y |  |
| SERVICE_URL_PUBLIC | VARCHAR2(1000) | Y |  |
| SERVICE_URL_LOCAL | VARCHAR2(1000) | Y |  |
| IS_URL_PUBLIC | CHAR(1) default 'N' | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `MICRO_SERVICES_PK`: SERVICE_ID

## DEFINITIONS.MLOG$_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| M_ROW$$ | VARCHAR2(255) | Y |  |
| DMLTYPE$$ | VARCHAR2(1) | Y |  |
| OLD_NEW$$ | VARCHAR2(1) | Y |  |
| CHANGE_VECTOR$$ | RAW(255) | Y |  |
| XID$$ | NUMBER | Y |  |


## DEFINITIONS.MLOG$_GL_DEPARTMENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| M_ROW$$ | VARCHAR2(255) | Y |  |
| DMLTYPE$$ | VARCHAR2(1) | Y |  |
| OLD_NEW$$ | VARCHAR2(1) | Y |  |
| CHANGE_VECTOR$$ | RAW(255) | Y |  |
| XID$$ | NUMBER | Y |  |


## DEFINITIONS.MLOG$_GL_DEPT_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| M_ROW$$ | VARCHAR2(255) | Y |  |
| DMLTYPE$$ | VARCHAR2(1) | Y |  |
| OLD_NEW$$ | VARCHAR2(1) | Y |  |
| CHANGE_VECTOR$$ | RAW(255) | Y |  |
| XID$$ | NUMBER | Y |  |


## DEFINITIONS.MLOG$_UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| M_ROW$$ | VARCHAR2(255) | Y |  |
| SNAPTIME$$ | DATE | Y |  |
| DMLTYPE$$ | VARCHAR2(1) | Y |  |
| OLD_NEW$$ | VARCHAR2(1) | Y |  |
| CHANGE_VECTOR$$ | RAW(255) | Y |  |
| XID$$ | NUMBER | Y |  |


## DEFINITIONS.MOBILE_CODES

| Column | Type | Null | Comment |
|---|---|---|---|
| MOBILE_CODE_NO | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |

- **PK** `PK_MOBILE_CODES`: MOBILE_CODE_NO
- **CHECK** `CHK_MOBILE_CODES`: DESCRIPTION IN ('MOBILINK','WARID','INSTAPHONE','TELENOR','ZONG','UFONE','SCOM','ETISALAT','OTHERS'

## DEFINITIONS.MOBILITY_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| MOBILITY_STATUS_ID | VARCHAR2(7) | N |  |
| MOBILITY_STATUS | CHAR(1) | N |  |
| MOBILITY_DESC | VARCHAR2(200) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |
| ENTERED_TERMINAL | VARCHAR2(30) | Y |  |

- **PK** `PK_MOBILITY_STATUS`: MOBILITY_STATUS_ID, LOC_ID
- **UK** `UK_MOBILITY_STATUS1`: MOBILITY_DESC, LOC_ID
- **UK** `UK_MOBILITY_STATUS2`: MOBILITY_STATUS, LOC_ID
- **Triggers**: `MOBILITY_STATUS_CEA` (before insert or update or delete), `MOBILITY_STATUS_DEL` (after delete), `MOBILITY_STATUS_INS` (before insert), `MOBILITY_STATUS_UPD` (before update), `TRG_WS_RSJ_BT_BX_Q` (after insert or update or delete)

## DEFINITIONS.MODIFY_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| MODIFY_REASON_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_MODIFY_REASONS`: MODIFY_REASON_ID
- **Triggers**: `MODIFY_REASONS_CEA` (before insert or update or delete), `MODIFY_REASONS_DEL` (after delete), `MODIFY_REASONS_INS` (before insert), `MODIFY_REASONS_UPD` (before update), `TRG_WS_RAA_OH_XR_Q` (after insert or update or delete)

## DEFINITIONS.MODULE_REPORT_NAME

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_NAME | VARCHAR2(30) | Y |  |
| MODULE_NAME | VARCHAR2(60) | Y |  |
| PIC_FLAG | CHAR(1) default 'N' | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| PDF_REPORT_NAME | VARCHAR2(30) | Y |  |
| PDF_REPORT_SERVER | VARCHAR2(30) | Y |  |
| PDF_REPORT_PATH | VARCHAR2(60) | Y |  |
| RDF_REPORT_SERVER | VARCHAR2(30) | Y |  |
| RDF_REPORT_PATH | VARCHAR2(60) | Y |  |
| JPEG_REPORT_SERVER | VARCHAR2(30) | Y |  |
| JPEG_REPORT_PATH | VARCHAR2(30) | Y |  |
| RDF_REPORT_NAME | VARCHAR2(200) | Y |  |
| PDF_DESNAME | VARCHAR2(200) | Y |  |
| REPORT_NAME_ID | NUMBER(3) | N | Primary Key |

- **PK** `PK_MODULE_REPORT_NAME`: REPORT_NAME_ID
- **Triggers**: `MODULE_REPORT_NAME_CEA` (before insert or update or delete), `TRG_WS_BZI_WC_TU_Q` (after insert or update or delete)

## DEFINITIONS.MONTHS

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N | Store attendance month start date |
| END_DATE | DATE | N | Store attendance month end date |
| FLAG | VARCHAR2(1) | Y | This column can contain 'Y' or 'N'. It's value will be 'Y' only for current month |
| MONTH_CLOSED | VARCHAR2(1) default 'N' | Y | This column will save whether month is closed or not for payroll processing |
| NEXT_MONTH | VARCHAR2(1) default 'N' | Y | This column will be 'Y' for next month. Only one month can be selected as 'Y' |
| CURRENT_MONTH | VARCHAR2(1) default 'N' | Y | This column will be 'Y' for current month. Only one month can be selected as 'Y' |
| SHORT_DESC | VARCHAR2(15) | Y | Store month short description as Jan, 2010 |
| PAY_FLAG | CHAR(1) | Y |  |
| PAY_GL_VOUCHER | CHAR(1) | Y |  |
| PAY_PF_VOUCHER | CHAR(1) | Y |  |
| PAY_PROCESS | CHAR(1) | Y | Store whether payroll is processed for specified month or not |
| PAY_CALC_DATE | DATE | Y | Store date on which payroll is executed for specified month |
| PAY_POST_DATE | DATE | Y |  |
| PAY_START_DATE | DATE | Y | Store month start date for payroll |
| PAY_END_DATE | DATE | Y | Store month end date for payroll |
| MONTH | CHAR(6) | Y | Store month Id as '012010' for Jan 2010 |
| LEAVE_BALANCE_CALC | CHAR(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(1000) | Y | To save comments when monthly regular process is executed for payroll to avoid any data manipulation on dependant table |
| CISCO_PROCESS_DATE | DATE | Y |  |
| CISCO_POST_DATE | DATE | Y |  |

- **PK** `PK_MONTHS`: START_DATE, END_DATE
- **CHECK** `CK_MONTHS_001`: MONTH_CLOSED IN ('N','Y'
- **CHECK** `CK_MONTHS_002`: NEXT_MONTH IN ('N','Y'
- **CHECK** `CK_MONTHS_003`: CURRENT_MONTH IN ('N','Y'
- **CHECK** `CK_MONTHS_004`: LEAVE_BALANCE_CALC IN ('Y','N'
- **Triggers**: `LOC_WISE_MONTHS_SYNC_INS` (after insert), `MONTHS_DEL` (after delete), `MONTHS_INS` (before insert), `MONTHS_UPD` (before update)

## DEFINITIONS.MONTH_RFID_DATA_TRANSFER

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| TRANSFER_ID | NUMBER(1) | N |  |
| RFID_DATA_TRANSFERRED | CHAR(1) default 'N' | Y |  |
| RFID_DATA_COMMENTS | VARCHAR2(1000) | Y |  |
| TRANSFERED_BY | VARCHAR2(14) | Y |  |
| TRANSFER_DATE | DATE | Y |  |

- **PK** `PK_MONTH_RFID_DATA_TRANSFER`: START_DATE, END_DATE, TRANSFER_ID
- **FK** `FK_MONTH_RFID_DATA_TRANSFER_1`: (START_DATE, END_DATE) -> DEFINITIONS.MONTHS(START_DATE, END_DATE)

## DEFINITIONS.MORPHOLOGY

| Column | Type | Null | Comment |
|---|---|---|---|
| MORPH_CODE | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ICD_O_3_CODE | CHAR(4) | Y |  |
| ICD_O_3_GRADE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| FU_FOR_LIFE | CHAR(1) | Y | Y mean for life time follow up treatment |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_MORPHOLOGY`: MORPH_CODE, LOCATION_ID
- **Triggers**: `MORPHOLOGY_CEA` (before insert or update or delete), `MORPHOLOGY_DEL` (after delete), `MORPHOLOGY_INS` (before insert), `MORPHOLOGY_INSRT` (before insert), `MORPHOLOGY_UPD` (before update), `TRG_WS_KLZ_NI_CD_Q` (after insert or update or delete)

## DEFINITIONS.MOVEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| MOVEMENT_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_MOVEMENT`: MOVEMENT_ID
- **UK** `UK_MOVEMENT_1`: DESCRIPTION
- **CHECK** `CK_MOVEMENT_1`: ACTIVE IN ('N','Y'
- **Triggers**: `MOVEMENT_CEA` (before insert or update or delete), `TRG_WS_DFB_TO_XX_Q` (after insert or update or delete)

## DEFINITIONS.MRN_TRAN_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| MRN_TYPE_ID | VARCHAR2(1) | N |  |
| DESCRIPTION | VARCHAR2(50) | N |  |
| TRANS_TYPE | VARCHAR2(3) | N |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |

- **PK** `PK_MRN_TRAN_TYPE`: ORGANIZATION_ID, SCHEMA_ID, MRN_TYPE_ID
- **Triggers**: `MRN_TRAN_TYPE_CEA` (before insert or update or delete), `MRN_TRAN_TYPE_DEL` (after delete), `MRN_TRAN_TYPE_INS` (before insert), `MRN_TRAN_TYPE_UPD` (before update), `TRG_WS_TPC_MW_VK_Q` (after insert or update or delete)

## DEFINITIONS.M_CODES

| Column | Type | Null | Comment |
|---|---|---|---|
| M_CODE_ID | VARCHAR2(10) | N | Snomed M-Code ID |
| ACTIVE | CHAR(1) default 'N' | Y | This column contains the Active Status. (Y=ACTIVE, N=Not-Active) |

- **PK** `PK_M_CODES`: M_CODE_ID
- **Triggers**: `M_CODES_CEA` (before insert or update or delete), `M_CODES_DEL` (after delete), `M_CODES_INS` (before insert), `M_CODES_UPD` (before update), `TRG_WS_IYQ_MY_VB_Q` (after insert or update or delete)

## DEFINITIONS.NC_ACTION_TAKEN

| Column | Type | Null | Comment |
|---|---|---|---|
| ACTION_TAKEN_ID | VARCHAR2(4) | N |  |
| ACTION_TAKEN_DESC | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_NC_ACTION_TAKEN`: ACTION_TAKEN_ID
- **Triggers**: `NC_ACTION_TAKEN_DEL` (after delete), `NC_ACTION_TAKEN_INS` (before insert), `NC_ACTION_TAKEN_UPD` (before update)

## DEFINITIONS.NC_CLINICAL_AREA

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINICAL_AREA_ID | VARCHAR2(4) | N |  |
| CLINICAL_AREA_DESC | VARCHAR2(500) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| COMPLIANCE_TYPE | VARCHAR2(3) default 'OCA' | N | OCA for Open Chart Audit CCA for Close Chart Audit |
| CATEGORY_ID | VARCHAR2(4) | Y |  |

- **PK** `PK_NC_CLINICAL_AREA`: CLINICAL_AREA_ID
- **Triggers**: `NC_CLINICAL_AREA_DEL` (after delete), `NC_CLINICAL_AREA_INS` (before insert), `NC_CLINICAL_AREA_UPD` (before update)

## DEFINITIONS.NC_QUESTION_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(4) | N |  |
| CATEGORY_DESC | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |

- **PK** `PK_NC_QUESTION_CATEGORY`: CATEGORY_ID
- **Triggers**: `NC_QUESTION_CATEGORY_DEL` (after delete), `NC_QUESTION_CATEGORY_INS` (before insert), `NC_QUESTION_CATEGORY_UPD` (before update)

## DEFINITIONS.NC_QUESTION_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| QUESTION_ID | VARCHAR2(6) | N |  |
| QUESTION_DESC | VARCHAR2(500) | N |  |
| CLINICAL_AREA_ID | VARCHAR2(4) | N |  |
| CATEGORY_ID | VARCHAR2(4) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N |  |
| ORDER_BY | NUMBER(6) | Y |  |

- **PK** `PK_NC_QUESTION_SETUP`: QUESTION_ID
- **Triggers**: `NC_QUESTION_SETUP_DEL` (after delete), `NC_QUESTION_SETUP_INS` (before insert), `NC_QUESTION_SETUP_UPD` (before update)

## DEFINITIONS.NGINX_CONFIGURATION

| Column | Type | Null | Comment |
|---|---|---|---|
| APP_NAME | VARCHAR2(100) | N |  |
| APP_URL | VARCHAR2(255) | Y |  |
| APP_VERSION | VARCHAR2(20) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| CONFIG_TYPE | CHAR(1) default 'D' | N |  |
| NGNIX_CONFIG | CLOB | Y |  |
| PORT | NUMBER(4) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| APP_ID | NUMBER | Y |  |

_No standard audit columns._

- **PK** `PK_APPLICATIONS`: APP_NAME
- **CHECK** `CHK_ACTIVE_YN`: ACTIVE IN ('Y', 'N'
- **CHECK** `CHK_CONFIG_TYPE_DS`: CONFIG_TYPE IN ('D', 'S'

## DEFINITIONS.NHSN_SETUP_RATIO_M

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |

- **PK** `PK_SETUP_ID`: ID

## DEFINITIONS.NHSN_SETUP_RATIO_D

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(3) | N |  |
| INFECTION_TYPE_ID | VARCHAR2(7) | N |  |
| RATIO_VALUE | NUMBER(3,2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_INFECTION_TYPE_ID`: ID, INFECTION_TYPE_ID
- **FK** `FK_SETUP_ID`: (ID) -> DEFINITIONS.NHSN_SETUP_RATIO_M(ID)

## DEFINITIONS.NOTES_ALERT_PARAM

| Column | Type | Null | Comment |
|---|---|---|---|
| NOTES_ID | NUMBER(3) | N |  |
| PARAM_ID | NUMBER(3) | N |  |
| TEXT | VARCHAR2(30) | Y |  |
| REPLACE_WITH_PARAM | VARCHAR2(30) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_NOTES_ALERT_PARAM`: NOTES_ID, PARAM_ID
- **Triggers**: `NOTES_ALERT_PARAM_DEL` (after delete), `NOTES_ALERT_PARAM_INS` (before insert), `NOTES_ALERT_PARAM_UPD` (before update)

## DEFINITIONS.NOTES_TEMPLATE

| Column | Type | Null | Comment |
|---|---|---|---|
| NOTES_ID | NUMBER(3) | N |  |
| NOTES_DESC | VARCHAR2(60) | Y |  |
| NOTES_TEXT | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_NOTES_TEMPLATE`: NOTES_ID
- **Triggers**: `NOTES_TEMPLATE_CEA` (before insert or update or delete), `NOTES_TEMPLATE_DEL` (after delete), `NOTES_TEMPLATE_INS` (before insert), `NOTES_TEMPLATE_UPD` (before update), `TRG_WS_XIC_JD_OY_Q` (after insert or update or delete)

## DEFINITIONS.NOTE_TEMPLATE_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| POPUP_ALERT_ID | NUMBER(5) | N |  |
| ALERT_TYPE_ID | NUMBER(5) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_NOTE_TEMPLATE_ALERT`: TEMPLATE_ID, POPUP_ALERT_ID, ALERT_TYPE_ID
- **FK** `FK_NOTE_TEMPLATE_ALERT`: (POPUP_ALERT_ID, ALERT_TYPE_ID) -> DEFINITIONS.CLINICAL_POPUP_ALERTS(POPUP_ALERT_ID, ALERT_TYPE_ID) [disabled]
- **Triggers**: `NOTE_TEMPLATE_ALERTS_CEA` (before insert or update or delete), `NOTE_TEMPLATE_ALERTS_DEL` (after delete), `NOTE_TEMPLATE_ALERTS_INS` (before insert), `NOTE_TEMPLATE_ALERTS_UPD` (before update), `TRG_WS_JQD_PS_VW_Q` (after insert or update or delete)

## DEFINITIONS.NOTE_TEMPLATE_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| PARAMETER_ID | VARCHAR2(6) | Y |  |
| CPT_ID | VARCHAR2(18) | N |  |
| MAKE_ORDER | CHAR(1) default 'N' | Y | Y mean make order  master/cpt against specified CPT ID |
| IPD_VISIT_CHARGE | CHAR(1) default 'N' | Y | Y mean IPD visit charging entery make into system  against specified CPT ID |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_DEF_NTC_1`: TEMPLATE_ID, CPT_ID
- **Triggers**: `NOTE_TEMPLATE_CPT_CEA` (before insert or update or delete), `NOTE_TEMPLATE_CPT_DEL` (after delete), `NOTE_TEMPLATE_CPT_INS` (before insert), `NOTE_TEMPLATE_CPT_UPD` (before update), `TRG_WS_HNY_PY_ZR_Q` (after insert or update or delete)

## DEFINITIONS.NOTE_TEMPLATE_REPORT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER(6) | N |  |
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_TEMPLATE_REPORT_SETUP`: SETUP_ID
- **UK** `UK_TEMPLATE_REPORT_SETUP`: TEMPLATE_ID, OBJECT_CODE, LOC_ID
- **Triggers**: `NOTE_TEMPLATE_REPORT_SETUP_CEA` (before insert or update or delete), `NOTE_TEMPLATE_REPORT_SETUP_DEL` (after delete), `NOTE_TEMPLATE_REPORT_SETUP_INS` (before insert), `NOTE_TEMPLATE_REPORT_SETUP_UPD` (before update), `TRG_WS_SZI_AC_PX_Q` (after insert or update or delete)

## DEFINITIONS.NOTE_USERS

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_TYPE | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| PARENT_USER_TYPE | VARCHAR2(3) | N |  |

- **PK** `PK_NOTE_USERS`: USER_TYPE, PARENT_USER_TYPE
- **Triggers**: `NOTE_USERS_CEA` (before insert or update or delete), `TRG_WS_HUV_FX_XK_Q` (after insert or update or delete)

## DEFINITIONS.NURSING_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_NURSING_SETUP`: SETUP_ID

## DEFINITIONS.NURSING_SETUP_DEFINITION

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(3) | Y |  |
| DEFINITION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_NURSING_SETUP_DEFINITION`: DEFINITION_ID
- **FK** `FK_NURSING_SETUP_DEFINITION_1`: (SETUP_ID) -> DEFINITIONS.NURSING_SETUP(SETUP_ID) [disabled]

## DEFINITIONS.NURSING_SETUP_DEFINITION_DTL

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(3) | Y |  |
| DEFINITION_ID | VARCHAR2(6) | Y |  |
| CATEGORY_ID | VARCHAR2(9) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| RANGE_FROM | NUMBER(5,2) | Y |  |
| RANGE_TO | NUMBER(5,2) | Y |  |
| CATEGORY_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_NURSING_SETUP_DEFINITION_DT`: CATEGORY_ID
- **FK** `FK_NURSING_SETUP_DEF_DTL_1`: (DEFINITION_ID) -> DEFINITIONS.NURSING_SETUP_DEFINITION(DEFINITION_ID) [disabled]

## DEFINITIONS.OBJECTS_ALIKE

| Column | Type | Null | Comment |
|---|---|---|---|
| P_OBJECT_CODE | VARCHAR2(11) | N |  |
| C_OBJECT_CODE | VARCHAR2(11) | N |  |
| COMMENTS | VARCHAR2(500) | Y |  |

- **PK** `PK_OBJECTS_ALIKE`: P_OBJECT_CODE, C_OBJECT_CODE
- **FK** `FK_OBJECTS_ALIKE`: (P_OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **FK** `FK_OBJECTS_ALIKE_1`: (C_OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]

## DEFINITIONS.OBJECTS_BACKUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | Y |  |
| OBJECT_ID | VARCHAR2(5) | Y |  |
| NAME | VARCHAR2(1000) | N |  |
| PATH_ID | VARCHAR2(5) | Y |  |
| SUPERVISED_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| DISPLAY_NAME | VARCHAR2(60) | Y |  |
| INITIAL_SCREEN | CHAR(1) | Y |  |
| DEPLOYMENT_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| OTHER_TITLE_TXT | VARCHAR2(30) | Y |  |
| OTHER_COMMENTS_TXT | VARCHAR2(2000) | Y |  |
| DEPLOYED_YN | CHAR(1) | Y |  |
| TERMINAL_TYPE_ID | VARCHAR2(15) | Y |  |
| PURPOSE | VARCHAR2(2500) | Y |  |
| DEV_TOOL | VARCHAR2(4) | N |  |
| CREATE_SESSION | CHAR(1) | N |  |
| IS_JSP | CHAR(1) | Y |  |
| OBSOLETED_OBJECT | CHAR(1) | N |  |
| OBSOLETED_BY | VARCHAR2(14) | Y |  |
| RETIRED_6I | CHAR(1) | Y |  |
| RESTRICTED | CHAR(1) | N |  |
| EMAIL_SEND | CHAR(1) | N |  |
| STOP_AUTO_COMPILE | CHAR(1) | Y |  |
| PARAM_FORM_REQ | CHAR(1) | Y |  |
| OBJECT_SKIP_SECURITY | CHAR(1) | Y |  |
| WIN_X_POS | NUMBER(5,2) | Y |  |
| WIN_Y_POS | NUMBER(5,2) | Y |  |
| WIN_WIDTH | NUMBER(5,2) | Y |  |
| WIN_HEIGHT | NUMBER(5,2) | Y |  |
| REPORT_ID | NUMBER(4) | Y |  |
| REPORT_TYPE_ID | VARCHAR2(4) | Y |  |
| OBJECT_NATURE | CHAR(1) | Y |  |
| RUN_FROM_SERVER | VARCHAR2(4) | Y |  |
| SERVER_TYPE | CHAR(1) | Y |  |
| IS_CONFIDENTIAL_OBJ | CHAR(1) | Y |  |
| IS_REPORTING_FORM | CHAR(1) | Y |  |
| OBJECT_OPEN_MAX_TIME | NUMBER | Y |  |
| MDI_FORM | CHAR(1) | Y |  |
| OBJECT_URL | VARCHAR2(256) | Y |  |
| OBJECT_URL_USER | VARCHAR2(50) | Y |  |
| OBJECT_URL_PASSWORD | VARCHAR2(50) | Y |  |
| OBJECT_BROWSER_EXE_NAME | VARCHAR2(250) | Y |  |
| SPACE_REQ_AFTER_EXE_NAME | CHAR(1) | Y |  |
| OBJECT_PAGE | VARCHAR2(60) | Y |  |
| PAGE_ID | NUMBER | Y |  |
| APP_ID | NUMBER | Y |  |
| PLATFORM | CHAR(1) | Y |  |
| DISTRIBUTED_MODE | CHAR(2) | Y |  |


## DEFINITIONS.OBJECTS_IMAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| OBJECT_IMAGE | BLOB | Y |  |
| IMAGE_NAME | VARCHAR2(200) | Y |  |

- **PK** `PK_OBJECTS_IMAGES`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID
- **Triggers**: `OBJECTS_IMAGES_CEA` (before insert or update or delete), `TRG_WS_SAG_JU_RY_Q` (after insert or update or delete)

## DEFINITIONS.OBJECTS_TEMP

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | Y |  |
| OBJECT_ID | VARCHAR2(5) | Y |  |
| NAME | VARCHAR2(1000) | N |  |
| PATH_ID | VARCHAR2(5) | Y |  |
| SUPERVISED_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| DISPLAY_NAME | VARCHAR2(60) | Y |  |
| INITIAL_SCREEN | CHAR(1) | Y |  |
| DEPLOYMENT_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| OTHER_TITLE_TXT | VARCHAR2(30) | Y |  |
| OTHER_COMMENTS_TXT | VARCHAR2(2000) | Y |  |
| DEPLOYED_YN | CHAR(1) | Y |  |
| TERMINAL_TYPE_ID | VARCHAR2(15) | Y |  |
| PURPOSE | VARCHAR2(2500) | Y |  |
| DEV_TOOL | VARCHAR2(4) | N |  |
| CREATE_SESSION | CHAR(1) | N |  |
| IS_JSP | CHAR(1) | Y |  |
| OBSOLETED_OBJECT | CHAR(1) | N |  |
| OBSOLETED_BY | VARCHAR2(14) | Y |  |
| RETIRED_6I | CHAR(1) | Y |  |
| RESTRICTED | CHAR(1) | N |  |
| EMAIL_SEND | CHAR(1) | N |  |
| STOP_AUTO_COMPILE | CHAR(1) | Y |  |
| PARAM_FORM_REQ | CHAR(1) | Y |  |
| OBJECT_SKIP_SECURITY | CHAR(1) | Y |  |
| WIN_X_POS | NUMBER(5,2) | Y |  |
| WIN_Y_POS | NUMBER(5,2) | Y |  |
| WIN_WIDTH | NUMBER(5,2) | Y |  |
| WIN_HEIGHT | NUMBER(5,2) | Y |  |
| REPORT_ID | NUMBER(4) | Y |  |
| REPORT_TYPE_ID | VARCHAR2(4) | Y |  |
| OBJECT_NATURE | CHAR(1) | Y |  |
| RUN_FROM_SERVER | VARCHAR2(4) | Y |  |
| SERVER_TYPE | CHAR(1) | Y |  |
| IS_CONFIDENTIAL_OBJ | CHAR(1) | Y |  |
| IS_REPORTING_FORM | CHAR(1) | Y |  |
| OBJECT_OPEN_MAX_TIME | NUMBER | Y |  |
| MDI_FORM | CHAR(1) | Y |  |
| OBJECT_URL | VARCHAR2(256) | Y |  |
| OBJECT_URL_USER | VARCHAR2(50) | Y |  |
| OBJECT_URL_PASSWORD | VARCHAR2(50) | Y |  |
| OBJECT_BROWSER | VARCHAR2(250) | Y |  |


## DEFINITIONS.OBJECT_BLOCK

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| BLOCK_NAME | VARCHAR2(40) | Y |  |
| BLOCK_ID | NUMBER | N |  |

- **PK** `PK_OBJECT_BLOCK`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID, BLOCK_ID
- **FK** `FK_OBJECT_BLOCK_1`: (SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID) -> DEFINITIONS.OBJECTS(SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID)
- **Triggers**: `OBJECT_BLOCK_CEA` (before insert or update or delete), `OBJECT_BLOCK_DEL` (after delete), `OBJECT_BLOCK_INS` (before insert), `OBJECT_BLOCK_UPD` (before update), `TRG_WS_MCD_NB_EX_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_BUTTON

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| BTTN_ID | VARCHAR2(3) | N |  |
| BTTN_NAME | VARCHAR2(100) | Y |  |

- **PK** `PK_OBJECT_BUTTON`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID, BTTN_ID
- **Triggers**: `OBJECT_BUTTON_CEA` (before insert or update or delete), `OBJECT_BUTTON_DEL` (after delete), `OBJECT_BUTTON_UPD` (after update), `TRG_WS_GGD_ST_JM_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_CALL
Setup table contains information about organization , location base calling objects. 

| Column | Type | Null | Comment |
|---|---|---|---|
| BASE_OBJECT_CODE | VARCHAR2(11) | N | This column contains info about parrent object code |
| CHILD_OBJECT_CODE | VARCHAR2(11) | N | This column contains info about child object code |
| ACTIVE | CHAR(1) | N | This column contains info about status(Y = Active, N =  In Active) |

- **UK** `PK_DEF_OBJECT_CALL`: BASE_OBJECT_CODE, ORG_ID, LOC_ID

## DEFINITIONS.OBJECT_DEVELOPER

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| DEVELOPER_ID | VARCHAR2(14) | N |  |
| EXPECTED_START_DATE | DATE | Y |  |
| EXPECTED_END_DATE | DATE | Y |  |
| ACTUAL_END_DATE | DATE | Y |  |

- **PK** `PK_OBJECT_DEVELOPER`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID, DEVELOPER_ID
- **FK** `FK_OBJECT_DEVELOPER_1`: (SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID) -> DEFINITIONS.OBJECTS(SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID)
- **Triggers**: `OBJECT_DEVELOPER_CEA` (before insert or update or delete), `TRG_WS_ZEJ_HT_AZ_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_FROM_LIVE

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | Y |  |
| OBJECT_ID | VARCHAR2(5) | Y |  |
| NAME | VARCHAR2(1000) | N |  |
| PATH_ID | VARCHAR2(5) | Y |  |
| SUPERVISED_BY | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| DISPLAY_NAME | VARCHAR2(60) | Y |  |
| INITIAL_SCREEN | CHAR(1) | Y |  |
| DEPLOYMENT_DATE | DATE | Y |  |
| COMMENTS | VARCHAR2(2000) | Y |  |
| OTHER_TITLE_TXT | VARCHAR2(30) | Y |  |
| OTHER_COMMENTS_TXT | VARCHAR2(2000) | Y |  |
| DEPLOYED_YN | CHAR(1) | Y |  |
| TERMINAL_TYPE_ID | VARCHAR2(15) | Y |  |
| PURPOSE | VARCHAR2(2500) | Y |  |
| DEV_TOOL | VARCHAR2(4) | N |  |
| CREATE_SESSION | CHAR(1) | N |  |
| IS_JSP | CHAR(1) | Y |  |
| OBSOLETED_OBJECT | CHAR(1) | N |  |
| OBSOLETED_BY | VARCHAR2(14) | Y |  |
| RETIRED_6I | CHAR(1) | Y |  |
| RESTRICTED | CHAR(1) | N |  |
| EMAIL_SEND | CHAR(1) | N |  |
| STOP_AUTO_COMPILE | CHAR(1) | Y |  |
| PARAM_FORM_REQ | CHAR(1) | Y |  |
| OBJECT_SKIP_SECURITY | CHAR(1) | Y |  |
| WIN_X_POS | NUMBER(5,2) | Y |  |
| WIN_Y_POS | NUMBER(5,2) | Y |  |
| WIN_WIDTH | NUMBER(5,2) | Y |  |
| WIN_HEIGHT | NUMBER(5,2) | Y |  |
| REPORT_ID | NUMBER(4) | Y |  |
| REPORT_TYPE_ID | VARCHAR2(4) | Y |  |
| OBJECT_NATURE | CHAR(1) | Y |  |
| RUN_FROM_SERVER | VARCHAR2(4) | Y |  |
| SERVER_TYPE | CHAR(1) | Y |  |
| IS_CONFIDENTIAL_OBJ | CHAR(1) | Y |  |
| IS_REPORTING_FORM | CHAR(1) | Y |  |
| OBJECT_OPEN_MAX_TIME | NUMBER | Y |  |
| MDI_FORM | CHAR(1) | Y |  |
| OBJECT_URL | VARCHAR2(256) | Y |  |
| OBJECT_URL_USER | VARCHAR2(50) | Y |  |
| OBJECT_URL_PASSWORD | VARCHAR2(50) | Y |  |
| OBJECT_BROWSER_EXE_NAME | VARCHAR2(250) | Y |  |
| SPACE_REQ_AFTER_EXE_NAME | CHAR(1) | Y |  |
| OBJECT_PAGE | VARCHAR2(60) | Y |  |
| PAGE_ID | NUMBER | Y |  |
| APP_ID | NUMBER | Y |  |
| PLATFORM | CHAR(1) | Y |  |
| DISTRIBUTED_MODE | CHAR(2) | Y |  |


## DEFINITIONS.OBJECT_ITEM
This Table contains Object Items List that are used in Forms

| Column | Type | Null | Comment |
|---|---|---|---|
| ITEM_ID | NUMBER(6) | N | Unique Item ID |
| ITEM_TYPE_ID | NUMBER(3) | N | This column contains Item Type ID (Reference to DEFINITIONS.ITEM_TYPES) |
| OBJECT_CODE | VARCHAR2(11) | N | This column contains Object Code (Reference to DEFINITIONS.OBJECTS) |
| ITEM_NAME | VARCHAR2(65) | N | This column contains Item Name that is used in Objects as Identifier (BLOCK_NAME.ITEM_NAME) |
| ITEM_DESC | VARCHAR2(100) | Y | This column contains Descriptive Name of Item that is used in Objects |
| ACTIVE | CHAR(1) | N | This column contains Flag Information of Status (Y=Active, N=Inactive) |

- **PK** `PK_OBJECT_ITEM`: ITEM_ID
- **UK** `UK_OBJECT_ITEM_1`: OBJECT_CODE, ITEM_NAME
- **UK** `UK_OBJECT_ITEM_2`: ITEM_ID, ITEM_TYPE_ID
- **FK** `FK_OBJECT_ITEM_01`: (ITEM_TYPE_ID) -> DEFINITIONS.ITEM_TYPES(TYPE_ID) [disabled]
- **FK** `FK_OBJECT_ITEM_02`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **CHECK** `FK_OBJECT_ITEM_1`: ITEM_NAME = UPPER(ITEM_NAME
- **CHECK** `FK_OBJECT_ITEM_2`: ACTIVE IN ('Y','N'
- **Triggers**: `OBJECT_ITEM_DEL` (after delete), `OBJECT_ITEM_INS` (before insert), `OBJECT_ITEM_UPD` (before update)

## DEFINITIONS.OBJECT_ITEM_PROPERTY

| Column | Type | Null | Comment |
|---|---|---|---|
| ITEM_ID | NUMBER(6) | N |  |
| PROPERTY_ID | NUMBER(2) | N |  |
| VALUE_SOURCE | CHAR(1) | N | 'O' in case of open text, 'D' is denominating that the value is from Dictionary table (Definitions.Terminology), 'X' means that the value is from fixed values table(Definitions.Item_Property_values) |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_OBJECT_ITEM_PROPERTY`: ITEM_ID, PROPERTY_ID
- **FK** `FK_OBJECT_ITEM_PROPERTY_1`: (ITEM_ID) -> DEFINITIONS.OBJECT_ITEM(ITEM_ID)
- **FK** `FK_OBJECT_ITEM_PROPERTY_2`: (PROPERTY_ID) -> DEFINITIONS.ITEM_PROPERTY(PROPERTY_ID) [disabled]
- **FK** `FK_OBJECT_ITEM_PROPERTY_3`: (VALUE_SOURCE) -> DEFINITIONS.ITEM_PROPERTY_SOURCES(VALUE_SOURCE) [disabled]
- **CHECK** `CK_OBJECT_ITEM_PROPERTY_1`: VALUE_SOURCE IN ('X','D','O'
- **CHECK** `CK_OBJECT_ITEM_PROPERTY_2`: ACTIVE IN ('Y','N'
- **Triggers**: `OBJECT_ITEM_PROPERTY_DEL` (after delete), `OBJECT_ITEM_PROPERTY_INS` (before insert), `OBJECT_ITEM_PROPERTY_UPD` (before update)

## DEFINITIONS.OBJECT_MAPPING_APEX

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE_LEGACY | VARCHAR2(11) | N |  |
| OBJECT_CODE_APEX | VARCHAR2(11) | N |  |
| PLATE_FORM | VARCHAR2(1) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| RIGHTS_COPY_STATUS | CHAR(1) default 'N' | Y |  |

- **PK** `PK_OBJECT_MAPPRING_APEX`: OBJECT_CODE_LEGACY, OBJECT_CODE_APEX
- **FK** `FK_OBJECT_MAPPRING_APEX`: (OBJECT_CODE_LEGACY) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `OBJECT_MAPPING_APEX_DEL` (after delete), `OBJECT_MAPPING_APEX_INS` (before insert), `OBJECT_MAPPING_APEX_UPD` (before update)

## DEFINITIONS.OBJECT_NOTE_PRINT
This table will be used to Add the Different Notes which will be printed on Reports, Notes will be Organization+Location+Object Code Wise

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N | Organization for whom Note Setup will be entered |
| LOCATION_ID | VARCHAR2(3) | N | Location for whom Note Setup will be entered |
| OBJECT_CODE | VARCHAR2(11) | N | Object Code on which Notes will be printed |
| SR_NO | NUMBER(1) | N | This column was added because more than one Note can be entered on the Same Object |
| TRANS_DATE | DATE default SYSDATE | N | Date When Transaction will be added |
| NOTE | VARCHAR2(1000) | N | Note which will be printed on Report |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction, Values will be Y or N |

- **PK** `PK_OBJECT_NOTE_PRINT`: ORGANIZATION_ID, LOCATION_ID, OBJECT_CODE, SR_NO
- **FK** `FK_OBJECT_NOTE_PRINT_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID)
- **FK** `FK_OBJECT_NOTE_PRINT_2`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_OBJECT_NOTE_PRINT_3`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE) [disabled]
- **Triggers**: `OBJECT_NOTE_PRINT_DEL` (after delete), `OBJECT_NOTE_PRINT_INS` (before insert), `OBJECT_NOTE_PRINT_UPD` (before update)

## DEFINITIONS.OBJECT_PARAMETERS_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER | N |  |
| PARAM_NAME | VARCHAR2(100) | N |  |
| PARAM_VALUE | VARCHAR2(300) | Y |  |
| PARAM_LENGTH | NUMBER(2) | Y |  |
| PARAM_ORDER_BY | NUMBER(2) | Y |  |
| PARAM_DATA_TYPE | VARCHAR2(1) default 'N' | Y | Specify parameter data type 'N' for number, 'D' for Date & 'C' for character |

- **PK** `PK_OBJECT_PARAMETERS_DETAIL`: PARAM_ID, PARAM_NAME
- **FK** `FK_OBJECT_PARAMETERS_DETAIL_1`: (PARAM_ID) -> DEFINITIONS.OBJECT_PARAMETERS(PARAM_ID)
- **CHECK** `CHK_OBJECT_PARAMETERS_01`: PARAM_DATA_TYPE IN ('N','C','D'
- **Triggers**: `OBJECT_PARAMETERS_DETAIL_CEA` (before insert or update or delete), `TRG_WS_CYX_JG_MD_Q` (after insert or update or delete)

## DEFINITIONS.OBJECT_PARAMETERS_DETAIL_COPY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER | N |  |
| PARAM_NAME | VARCHAR2(100) | N |  |
| PARAM_VALUE | VARCHAR2(300) | Y |  |
| PARAM_LENGTH | NUMBER(2) | Y |  |
| PARAM_ORDER_BY | NUMBER(2) | Y |  |
| PARAM_DATA_TYPE | VARCHAR2(1) | Y |  |


## DEFINITIONS.OBJECT_PARAMETERS_SOURCE
This table contains parent/calling object wise front end value source of parameters

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER(7) | N | This column referes to parent table DEFINITIONS.OBJECT_PARAMETERS (PK) |
| CALLING_OBJECT_CODE | VARCHAR2(11) | N | This column contains parent calling obejct code (PK) |
| ACTIVE | CHAR(1) default 'N' | N | This column contains flag inforamtion of active status Y=Active, N=Inactive |
| CHECK_DEFAULT | CHAR(1) default 'N' | N | This column contains flag inforamtion of default value application in case of null values |
| FRONTEND_SOURCE | VARCHAR2(100) | Y | This column contains string to access front end values source |
| DEFAULT_VALUE | VARCHAR2(100) | Y | This column contains default value if frontend value does not defined |

- **PK** `PK_OBJECT_PARAMETERS_SOURCE`: PARAM_ID, CALLING_OBJECT_CODE
- **FK** `FK_OBJECT_PARAMETERS_SOURCE_1`: (PARAM_ID) -> DEFINITIONS.OBJECT_PARAMETERS(PARAM_ID)
- **CHECK** `CK_OBJECT_PARAMETERS_SOURCE_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_OBJECT_PARAMETERS_SOURCE_2`: CHECK_DEFAULT IN ('Y','N'

## DEFINITIONS.OBJECT_PARAMETERS_SOURCE_COPY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAM_ID | NUMBER(7) | N |  |
| CALLING_OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTIVE | CHAR(1) | N |  |
| CHECK_DEFAULT | CHAR(1) | N |  |
| FRONTEND_SOURCE | VARCHAR2(100) | Y |  |
| DEFAULT_VALUE | VARCHAR2(100) | Y |  |


## DEFINITIONS.OBJECT_PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_OBJECT_PATIENT_TYPE`: SERIAL_NO
- **UK** `UK_OBJECT_PATIENT_TYPE_01`: OBJECT_CODE, PATIENT_TYPE_ID
- **FK** `FK_OBJECT_PATIENT_TYPE_01`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **FK** `FK_OBJECT_PATIENT_TYPE_02`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **Triggers**: `OBJECT_PATIENT_TYPE_DEL` (after delete), `OBJECT_PATIENT_TYPE_INS` (before insert), `OBJECT_PATIENT_TYPE_UPD` (before update)

## DEFINITIONS.OBJECT_PREREQUISITES

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(3) | N | Serial No for the each prerequisit against Object Code |
| SOURCE_NAME | VARCHAR2(500) | N | Function Name |
| DESCRIPTION | VARCHAR2(100) | Y | Detail description of prerequisit |
| ACTIVE | CHAR(1) | Y | Y for active, N for not active |
| OBJECT_CODE | VARCHAR2(11) | N | Refer from DEFINITIONS.OBJECTS table |
| HELP_TEXT | VARCHAR2(1000) | Y | Help text for MIS Helpline |

- **PK** `PK_OBJECT_PREREQUISITES`: OBJECT_CODE, SERIAL_NO
- **FK** `FK_OBJECT_PREREQUISITES_1`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)

## DEFINITIONS.OBJECT_RULES

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| OBJECT_TYPE_ID | VARCHAR2(3) | N |  |
| OBJECT_ID | VARCHAR2(5) | N |  |
| RULE_DESCRIPTION | VARCHAR2(1000) | N |  |
| RULE_DATE | DATE | Y |  |
| CR_ID | VARCHAR2(100) | Y |  |
| CR_DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_OBJECT_RULES_1`: SCHEMA_ID, OBJECT_TYPE_ID, OBJECT_ID, RULE_DESCRIPTION
- **Triggers**: `OBJECT_RULES_DEL` (after delete), `OBJECT_RULES_INS` (before insert), `OBJECT_RULES_UPD` (before update)

## DEFINITIONS.PHY_NOTES_PLAN

| Column | Type | Null | Comment |
|---|---|---|---|
| PLAN_ID | NUMBER | N |  |
| NAME | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(1500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PHY_NOTES_PLAN_PK`: PLAN_ID
- **Triggers**: `PHY_NOTES_PLAN_DEL` (after delete), `PHY_NOTES_PLAN_INS` (before insert), `PHY_NOTES_PLAN_UPD` (before update)

## DEFINITIONS.OBJECT_WISE_NOTES_PLAN

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_WISE_PLAN_ID | NUMBER | N |  |
| PLAN_ID | NUMBER | Y |  |
| OBJECT_CODE | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(1500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `OBJECT_WISE_NOTES_PLAN_PK`: OBJECT_WISE_PLAN_ID
- **FK** `OBJECT_WISE_NOTES_PLAN_FK`: (PLAN_ID) -> DEFINITIONS.PHY_NOTES_PLAN(PLAN_ID)
- **Triggers**: `OBJECT_WISE_NOTES_PLAN_DEL` (after delete), `OBJECT_WISE_NOTES_PLAN_INS` (before insert), `OBJECT_WISE_NOTES_PLAN_UPD` (before update)

## DEFINITIONS.OFFICE_CITIES

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| OFFICE_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_OFFICE_CITIES`: COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID, OFFICE_ID
- **FK** `FK_OFFICE_CITIES_1`: (COUNTRY_ID, STATE_ID, DISTRICT_ID) -> DEFINITIONS.DISTRICT(COUNTRY_ID, STATE_ID, DISTRICT_ID)

## DEFINITIONS.OLD_DATA_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | CHAR(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | CHAR(2) | Y |  |

- **PK** `PK_OLD_DATA_COUNTER`: TRANSACTION_TYPE_ID

## DEFINITIONS.OLD_DATA_COUNTER_HUSSAIN_R

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | CHAR(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | CHAR(2) | Y |  |


## DEFINITIONS.ONLINE_SURVEY_ANSWERS

| Column | Type | Null | Comment |
|---|---|---|---|
| ANSWER_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| DISPLAY_ORDER | NUMBER(3) | Y |  |

- **PK** `PK_ONLINE_SURVEY_ANSWERS`: ANSWER_ID
- **CHECK** `CK_ONLINE_SURVEY_ANSWERS_1`: ACTIVE IN ('N','Y'

## DEFINITIONS.ONLINE_SURVEY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SURVEY_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |

- **PK** `PK_ONLINE_SURVEY_MASTER`: SURVEY_ID

## DEFINITIONS.ONLINE_SURVEY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SURVEY_ID | NUMBER(3) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |

- **PK** `PK_ONLINE_SURVEY_DETAIL`: SURVEY_ID, START_DATE, END_DATE
- **FK** `FK_ONLINE_SURVEY_DETAIL_1`: (SURVEY_ID) -> DEFINITIONS.ONLINE_SURVEY_MASTER(SURVEY_ID)

## DEFINITIONS.ONLINE_SURVEY_QUESTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| QUESTION_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_ONLINE_SURVEY_QUESTIONS`: QUESTION_ID
- **CHECK** `CK_ONLINE_SURVEY_QUESTIONS_1`: ACTIVE IN ('N','Y'

## DEFINITIONS.OPEN_QUESTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUESTION_TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_OPEN_QUESTION_TYPE`: QUESTION_TYPE_ID
- **Triggers**: `OPEN_QUESTION_TYPE_DEL` (after delete), `OPEN_QUESTION_TYPE_INS` (before insert), `OPEN_QUESTION_TYPE_UPD` (before update)

## DEFINITIONS.OPEN_QUESTION_SUBTYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SUBTYPE_ID | VARCHAR2(7) | N |  |
| QUESTION_TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_OPEN_QUESTION_SUBTYPE`: SUBTYPE_ID, QUESTION_TYPE_ID
- **FK** `FK_OPEN_QUESTION_SUBTYPE_1`: (QUESTION_TYPE_ID) -> DEFINITIONS.OPEN_QUESTION_TYPE(QUESTION_TYPE_ID) [disabled]
- **Triggers**: `OPEN_QUESTION_SUBTYPE_DEL` (after delete), `OPEN_QUESTION_SUBTYPE_INS` (before insert), `OPEN_QUESTION_SUBTYPE_UPD` (before update)

## DEFINITIONS.OPERATORS_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| OPERATOR_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y | check in (Y¿,`N¿)  Default `Y¿ |

- **PK** `PKOPERATOR_TYPE_ID`: OPERATOR_TYPE_ID
- **Triggers**: `OPERATORS_TYPE_CEA` (before insert or update or delete), `OPERATORS_TYPE_DEL` (after delete), `OPERATORS_TYPE_INS` (before insert), `OPERATORS_TYPE_UPD` (before update), `TRG_WS_RRJ_OF_ZI_Q` (after insert or update or delete)

## DEFINITIONS.OPERATORS

| Column | Type | Null | Comment |
|---|---|---|---|
| OPERATOR_ID | NUMBER(5) | N |  |
| OPERATOR_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(200) | N |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y | check in (Y¿,`N¿)  Default `Y¿ |

- **PK** `PK_OPERATOR_ID`: OPERATOR_ID
- **UK** `UK_OPERATOR_SHORT_DESC`: SHORT_DESC
- **FK** `FK_OPERATOR_TYPE_ID`: (OPERATOR_TYPE_ID) -> DEFINITIONS.OPERATORS_TYPE(OPERATOR_TYPE_ID) [disabled]
- **Triggers**: `OPERATORS_CEA` (before insert or update or delete), `OPERATORS_DEL` (after delete), `OPERATORS_INS` (before insert), `OPERATORS_UPD` (before update), `TRG_WS_AQW_FQ_AV_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCATION_CLINIC

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| CLINIC_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULT_CLINIC | VARCHAR2(1) default 'N' | N |  |
| STAT_CLINIC | VARCHAR2(1) default 'N' | N |  |
| ADMIN_DEPARTMENT | VARCHAR2(1) default 'N' | Y |  |
| PCHS | CHAR(1) | Y | Palliative Care Home Services |

- **PK** `PK_ORDER_LOCATION_CLINIC`: LOCATION_ID, ORDER_LOCATION_ID, CLINIC_ID
- **Triggers**: `ORDER_LOCATION_CLINIC_CEA` (before insert or update or delete), `ORDER_LOCATION_CLINIC_DEL` (after delete), `ORDER_LOCATION_CLINIC_INS` (before insert), `ORDER_LOCATION_CLINIC_UPD` (before update), `TRG_WS_SQR_DV_VD_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCATION_CPT_PRICE
This table will be used to define the Order Location (Invoice Location CPT Price)

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Unique Id of the Institute |
| ORDER_LOCATION_ID | VARCHAR2(3) | N | Invoice Location/Order Location/Counter for which User wants to change the Price of the CPT |
| CPT_ID | VARCHAR2(18) | N | CPT Code for which Price will be added |
| PRICE | NUMBER(12,2) | N | Unit Price which will be charged against CPT from this Invoice Location |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_ORDER_LOCATION_CPT_PRICE`: LOCATION_ID, ORDER_LOCATION_ID, PATIENT_TYPE_ID, CPT_ID
- **FK** `FK_ORDER_LOCATION_CPT_PRICE_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **FK** `FK_ORDER_LOCATION_CPT_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_ORDER_LOCATION_CPT_PRICE_1`: PRICE>0
- **Triggers**: `ORDER_LOCATION_CPT_PRICE_CEA` (before insert or update or delete), `ORDER_LOCATION_CPT_PRICE_DEL` (after delete), `ORDER_LOCATION_CPT_PRICE_INS` (before insert), `ORDER_LOCATION_CPT_PRICE_UPD` (before update), `TRG_WS_ZHN_OU_IN_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCATION_RECEPTION

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| RECEPTION_NAME | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RECEPTION_ID | NUMBER(10) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_ORDER_LOCATION_RECEPTION`: RECEPTION_ID, LOCATION_ID, ORDER_LOCATION_ID
- **UK** `UK_ORDER_LOCATION_RECEPTION`: LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_ORDER_LOCATION_RECEPTION_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **Triggers**: `ORDER_LOCATION_RECEPTION_CEA` (before insert or update or delete), `ORDER_LOCATION_RECEPTION_DEL` (after delete), `ORDER_LOCATION_RECEPTION_INS` (before insert), `ORDER_LOCATION_RECEPTION_UPD` (before update), `TRG_WS_IXJ_CL_TH_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCATION_ROOM

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_RECEPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `ORDER_LOCATION_ROOM_PK`: LOCATION_ID, ORDER_LOCATION_ID
- **Triggers**: `ORDER_LOCATION_ROOM_DEL` (after delete), `ORDER_LOCATION_ROOM_INS` (before insert), `ORDER_LOCATION_ROOM_UPD` (before update)

## DEFINITIONS.ORDER_LOCATION_STORE

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| STORE_ID | VARCHAR2(6) | N |  |
| DISPENSING_LOCATION | CHAR(1) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| PRIORITY | NUMBER | Y |  |
| DISPOSABLE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_ORDER_LOCATION_STORE`: LOCATION_ID, ORDER_LOCATION_ID, STORE_ID, DISPENSING_LOCATION
- **FK** `FK_ORDER_LOCATION_STORE_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **Triggers**: `ORDER_LOCATION_STORE_CEA` (before insert or update or delete), `ORDER_LOCATION_STORE_DEL` (after delete), `ORDER_LOCATION_STORE_INS` (before insert), `ORDER_LOCATION_STORE_UPD` (before update), `TRG_WS_ACC_KD_FR_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_LOCAT_R

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(20) | Y |  |


## DEFINITIONS.ORDER_LOC_LANGUAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUGAE_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | Label Desc field will be used to show langugae wise text on Discharge Instruction report on discharge card |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ORDER_LOC_LANGUAGE_SETUP`: LANGUGAE_ID, LOCATION_ID, ORDER_LOCATION_ID
- **Triggers**: `ORDER_LOC_LANGUAGE_SETUP_CEA` (before insert or update or delete), `ORDER_LOC_LANGUAGE_SETUP_DEL` (after delete), `ORDER_LOC_LANGUAGE_SETUP_INS` (before insert), `ORDER_LOC_LANGUAGE_SETUP_UPD` (before update), `TRG_WS_EGB_MY_WC_Q` (after insert or update or delete)

## DEFINITIONS.ORDER_RESTRICTED_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| RESTRICTED_CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_RESTRICT`: CPT_ID, RESTRICTED_CPT_ID
- **Triggers**: `ORDER_RESTRICTED_CPT_CEA` (before insert or update or delete), `ORDER_RESTRICTED_CPT_DEL` (after delete), `ORDER_RESTRICTED_CPT_INS` (before insert), `ORDER_RESTRICTED_CPT_UPD` (before update), `TRG_WS_RNC_KM_JW_Q` (after insert or update or delete)

## DEFINITIONS.ORGSETUP_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | NUMBER | Y |  |
| ORG_SETUP_ID | NUMBER | N |  |
| HIS_ROLE_ID | VARCHAR2(10) | N |  |

- **PK** `PK_ORGSETUP_GROUPS_1`: ORG_SETUP_ID, HIS_ROLE_ID

## DEFINITIONS.ORG_FILE_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ORG_FILE_NO | CHAR(1) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| LEVELS | NUMBER(2) | N |  |
| NO_OF_DIGITS | NUMBER(2) | N |  |
| LOCKED | CHAR(1) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_ORG_FILE_MASTER`: ORG_FILE_NO
- **Triggers**: `ORG_FILE_MASTER_DEL` (after delete), `ORG_FILE_MASTER_INS` (before insert), `ORG_FILE_MASTER_UPD` (before update)

## DEFINITIONS.ORG_SETUP_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ORG_SETUP_ID | NUMBER(2) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_ORG_SETUP_MASTER`: ORG_SETUP_ID
- **Triggers**: `ORG_SETUP_MASTER_CEA` (before insert or update or delete), `ORG_SETUP_MASTER_DEL` (after delete), `ORG_SETUP_MASTER_INS` (before insert), `ORG_SETUP_MASTER_UPD` (before update), `TRG_WS_FXH_HL_UR_Q` (after insert or update or delete)

## DEFINITIONS.ORG_FILE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| ORG_FILE_NO | CHAR(1) | N |  |
| ORG_FILE_DETAIL_ID | NUMBER(1) | N |  |
| WIDTH | NUMBER(1) | N |  |
| ORG_SETUP_ID | NUMBER(2) | N |  |
| KEY_AUTO_MANUAL | CHAR(1) | N |  |
| LEVEL_TYPE | CHAR(1) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_ORG_FILE_DETAIL`: ORG_FILE_NO, ORG_FILE_DETAIL_ID
- **FK** `FK_ORG_FILE_DETAIL_1`: (ORG_SETUP_ID) -> DEFINITIONS.ORG_SETUP_MASTER(ORG_SETUP_ID) [disabled]
- **FK** `FK_ORG_FILE_DETAIL_2`: (ORG_FILE_NO) -> DEFINITIONS.ORG_FILE_MASTER(ORG_FILE_NO)
- **Triggers**: `ORG_FILE_DETAIL_DEL` (after delete), `ORG_FILE_DETAIL_INS` (before insert), `ORG_FILE_DETAIL_UPD` (before update)

## DEFINITIONS.ORG_HF_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| FROM_DATE | DATE | N |  |
| RPT_HF_SETUP_ID | CHAR(12) | N |  |

- **PK** `PK_ORG_HF_SETUP`: ORGANIZATION_ID, FROM_DATE
- **FK** `FK_ORG_HF_SETUP_1`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID)
- **FK** `FK_ORG_HF_SETUP_2`: (RPT_HF_SETUP_ID) -> DEFINITIONS.RPT_HF_SETUP(RPT_HF_SETUP_ID) [disabled]
- **Triggers**: `ORG_HF_SETUP_DEL` (after delete), `ORG_HF_SETUP_INS` (before insert), `ORG_HF_SETUP_UPD` (before update)

## DEFINITIONS.ORG_SETUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| ORG_SETUP_ID | NUMBER(2) | N |  |
| ORG_DETAIL_ID | NUMBER(6) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ADDRESS | VARCHAR2(255) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ORG_UNIT_ID | VARCHAR2(20) | Y |  |

- **PK** `PK_ORG_SETUP_DETAIL`: ORG_SETUP_ID, ORG_DETAIL_ID
- **UK** `UK_ORG_SETUP_DETAIL_01`: ORG_DETAIL_ID
- **FK** `FK_ORG_SETUP_DETAIL_1`: (ORG_SETUP_ID) -> DEFINITIONS.ORG_SETUP_MASTER(ORG_SETUP_ID)
- **FK** `FK_ORG_SETUP_DETAIL_2`: (COUNTRY_ID, STATE_ID, DISTRICT_ID) -> DEFINITIONS.DISTRICT(COUNTRY_ID, STATE_ID, DISTRICT_ID) [disabled]
- **Triggers**: `ORG_SETUP_DETAIL_CEA` (before insert or update or delete), `ORG_SETUP_DETAIL_DEL` (after delete), `ORG_SETUP_DETAIL_INS` (before insert), `ORG_SETUP_DETAIL_UPD` (before update), `TRG_WS_KOG_SR_HP_Q` (after insert or update or delete)

## DEFINITIONS.ORG_WISE_OBJECT_ITEM_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ITEM_ID | NUMBER(6) | N |  |
| PROPERTY_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | N |  |
| VALUE | VARCHAR2(50) | Y |  |

- **UK** `UK_ORG_WISE_OBJ_ITEM_SETUP_1`: ITEM_ID, PROPERTY_ID, ORG_ID
- **Triggers**: `ORG_WISE_OBJECT_ITEM_SETUP_DEL` (after delete), `ORG_WISE_OBJECT_ITEM_SETUP_INS` (before insert), `ORG_WISE_OBJECT_ITEM_SETUP_UPD` (before update)

## DEFINITIONS.OSV_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | CHAR(2) | Y |  |
| OSV_STATUS | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ALERT_DAYS | NUMBER | Y |  |
| IS_OSV_REQUIRED | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| IS_SLIP_RECEIVED | CHAR(1) | Y | This column will be use for linces expiry slip received purpose |

- **Triggers**: `OSV_STATUS_DEL` (after delete), `OSV_STATUS_INS` (before insert), `OSV_STATUS_UPD` (before update)

## DEFINITIONS.OUTSIDE_HOSPITALS

| Column | Type | Null | Comment |
|---|---|---|---|
| HOSPITAL_ID | VARCHAR2(3) | N | Unique Hospital ID |
| DESCRIPTION | VARCHAR2(1000) | N | Description of Hospital |
| ACTIVE | CHAR(1) default 'N' | N | Active Status (Y=Active, N=Inactive) |

- **PK** `PK_OUTSIDE_HOSPITAL`: HOSPITAL_ID

## DEFINITIONS.SERVICE_TYPE
This is a System Constant Table, We shall define the Service Types in this table

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Primary Key, Auto Generated Number |
| DESCRIPTION | VARCHAR2(60) | N | Name of the Service Type |
| SERVICE_CATEGORY_ID | VARCHAR2(3) | Y | Value of this column will create the differentiate between the Services e.g. CPT, Pharmacy, Supplies, Gym etc. |
| ACTIVE | CHAR(1) | N | Status of the Service Type |

- **PK** `PK_SERVICE_TYPE`: SERVICE_TYPE_ID
- **UK** `UK_SERVICE_TYPE_01`: DESCRIPTION, SERVICE_CATEGORY_ID
- **FK** `FK_SERVICE_TYPE_1`: (SERVICE_CATEGORY_ID) -> DEFINITIONS.DEF_SERVICE_CATEGORY(SERVICE_CATEGORY_ID) [disabled]
- **CHECK** `CK_SERVICE_TYPE_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_SERVICE_TYPE_2`: ACTIVE=UPPER(ACTIVE
- **Triggers**: `SERVICE_TYPE_CEA` (before insert or update or delete), `SERVICE_TYPE_DEL` (after delete), `SERVICE_TYPE_INS` (before insert), `SERVICE_TYPE_UPD` (before update), `TRG_WS_WUX_LS_BM_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_CPT_INCLUDE_ITEM
This table will be used to setup the Supplies already added in Costing of the CPT, This will also handle the Printing of the Package in Detail or Summary like other packages

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Id Ref |
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This column was added to differentiate between This kind of packages and other Packages e.g. Rehab , Radiotherapy, Surgery etc. |
| CPT_ID | VARCHAR2(18) | N | CPT Code for Reference to whom Supplies cost is added |
| ITEM_ID | VARCHAR2(25) | N | Supplies/Item whose Cost is added into CPT Price |
| QUANTITY | NUMBER(5) default 1 | N | Total Quantity which will be ordered as Free |
| TRANS_DATE | DATE default SYSDATE | N | Date when Transaction was added |
| REMARKS | VARCHAR2(250) | N | Remarks if any |

- **PK** `PK_PACKAGE_CPT_INCLUDE_ITEM`: PACKAGE_ID, SERVICE_TYPE_ID, CPT_ID, ITEM_ID
- **FK** `FK_PACKAGE_CPT_INCLUDE_ITEM_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **FK** `FK_PACKAGE_CPT_INCLUDE_ITEM_2`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID) [disabled]
- **FK** `FK_PACKAGE_CPT_INCLUDE_ITEM_3`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **FK** `FK_PACKAGE_CPT_INCLUDE_ITEM_4`: (ITEM_ID) -> ITEM.ITEM(ITEM_ID) [disabled]
- **Triggers**: `PACKAGE_CPT_INCLUDE_ITEM_CEA` (before insert or update or delete), `PACKAGE_CPT_INCLUDE_ITEM_DEL` (after delete), `PACKAGE_CPT_INCLUDE_ITEM_INS` (before insert), `PACKAGE_CPT_INCLUDE_ITEM_UPD` (before update), `TRG_WS_ZRS_VT_AR_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_DETAIL
This table is almost parallel of definitions.package (1:1 relation), ADF team was using definitions.packages for C4I, as per ADF Team, if i shall add the column in definitions.packages there application will become invalid that's why Billing Team have created new table

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Ref of Package |
| TREATMENT_COVER | CHAR(1) default 'I' | N | Values will be O/I/E, O means OPD and I means IPD, E means EAR |
| VALIDATION_PERIOD_REQUIRED | CHAR(1) default 'N' | N | Values of this column must be Y or N, In case of Y User has to enter the Start and End Date |
| START_DATE | DATE | Y | Start date of the Package |
| END_DATE | DATE | Y | End date of the Package |
| FROM_TIME | VARCHAR2(5) | Y | From time of the Package |
| TO_TIME | VARCHAR2(5) | Y | To time of the Package |
| HIDE_INVOICE_DETAIL | CHAR(1) default 'N' | N | Values of this column must be Y or N, Y means Hide the CPT Detail on Invoice Report and Show only Package Name, N means Show CPT Detail |
| PRICE_SOURCE | CHAR(1) default 'I' | Y |  |
| PROCESS_METHOD | VARCHAR2(6) default 'PREINV' | Y | PRE INVOICE, POST INVOICE |
| LIFE_SPAN | NUMBER(3) default 0 | Y | Number of days for which a package can be availed after linked to patient. |
| DEFAULT_PKG | CHAR(1) default 'N' | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |

- **PK** `PK_PACKAGE_DETAIL`: PACKAGE_ID, TREATMENT_COVER
- **FK** `FK_PACKAGE_DETAIL_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **CHECK** `CK_PACKAGE_DETAIL_1`: PRICE_SOURCE IN ('P','I'))
- **Triggers**: `PACKAGE_DETAIL_CEA` (before insert or update or delete), `PACKAGE_DETAIL_DEL` (after delete), `PACKAGE_DETAIL_INS` (before insert), `PACKAGE_DETAIL_UPD` (before update), `TRG_WS_GGE_OE_HP_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_EXCLUDE
This table will be used to Add the items as Execluded

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| SERIAL_NO | NUMBER(3) | N | Counter which will reset on New Package |
| ITEM_LIST | VARCHAR2(500) | N | Item's list which is excluded from package |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_EXCLUDE`: PACKAGE_ID, SERIAL_NO
- **FK** `FK_PACKAGE_EXCLUDE_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **Triggers**: `PACKAGE_EXCLUDE_CEA` (before insert or update or delete), `PACKAGE_EXCLUDE_DEL` (after delete), `PACKAGE_EXCLUDE_INS` (before insert), `PACKAGE_EXCLUDE_UPD` (before update), `TRG_WS_WBA_ZS_KC_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_FREE_ITEM
This table will be used to save the Free Items within Package, This table should be considered as Master level  which means If any item is defined in this table then it will be free all  the patients to whom This Package is attached

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| ITEM_ID | VARCHAR2(18) | N | CPT or Brand or Item which is free due to Package |
| TRANS_DATE | DATE default SYSDATE | N | Date when Transaction was made |
| NO_OF_ITEM | NUMBER(4) default 0 | N | Total No. of Items allowed Free, Zero means unlimited |
| REMARKS | VARCHAR2(250) | Y | Remarks if any |
| ACTIVE | CHAR(1) default 'Y' | Y | Status of the Transaction, Y means Active and N means Inactive |
| CLIENT_ID | VARCHAR2(10) | Y | Which Client contract will be used for Free Items |
| CONTRACT_ID | VARCHAR2(8) | Y | Which Client contract will be used for Free Items |
| CONTRACT_SERIAL_NO | NUMBER(3) | Y | Which Client contract will be used for Free Items |
| CC_ID | VARCHAR2(3) | Y | Which Client contract will be used for Free Items |

- **PK** `PK_PACKAGE_FREE_ITEM`: PACKAGE_ID, ITEM_ID
- **FK** `FK_PACKAGE_FREE_ITEM_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **CHECK** `CK_PACKAGE_FREE_ITEM_1`: NO_OF_ITEM BETWEEN 0 AND 9999
- **CHECK** `CK_PACKAGE_FREE_ITEM_2`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_FREE_ITEM_CEA` (before insert or update or delete), `PACKAGE_FREE_ITEM_DEL` (after delete), `PACKAGE_FREE_ITEM_INS` (before insert), `PACKAGE_FREE_ITEM_UPD` (before update), `TRG_WS_ZJX_AK_ZK_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_FUND
This table will be used to define funds of a package(to be shared by service types)

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref key |
| PACKAGE_FUND_ID | VARCHAR2(3) | N | This Column will represents the fund ID |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| AMOUNT | NUMBER | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_FUND`: PACKAGE_ID, PACKAGE_FUND_ID
- **FK** `FK_PACKAGE_FUND_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **CHECK** `CK_PACKAGE_FUND_1`: AMOUNT>0
- **CHECK** `CK_PACKAGE_FUND_2`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_FUND_CEA` (before insert or update or delete), `PACKAGE_FUND_DEL` (after delete), `PACKAGE_FUND_INS` (before insert), `PACKAGE_FUND_UPD` (before update), `TRG_WS_WAW_FW_GD_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_FUND_DETAIL
This table will be used to define package fund details

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref key |
| PACKAGE_FUND_ID | VARCHAR2(3) | N |  |
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This Column will represents the Service Type |
| ACTIVE | VARCHAR2(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_FUND_DETAIL`: PACKAGE_ID, PACKAGE_FUND_ID, SERVICE_TYPE_ID
- **FK** `FK_PACKAGE_FUND_DETAIL_1`: (PACKAGE_ID, PACKAGE_FUND_ID) -> DEFINITIONS.PACKAGE_FUND(PACKAGE_ID, PACKAGE_FUND_ID)
- **CHECK** `CK_PACKAGE_FUND_DETAIL_1`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_FUND_DETAIL_CEA` (before insert or update or delete), `PACKAGE_FUND_DETAIL_DEL` (after delete), `PACKAGE_FUND_DETAIL_INS` (before insert), `PACKAGE_FUND_DETAIL_UPD` (before update), `TRG_WS_NXP_NI_IZ_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_INCLUDE
This table will be used to add the Item Include in Free text, No decision will be made on this table, this is just for Reporting purpose

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| SERIAL_NO | NUMBER(3) | N | Part of the Primary key |
| ITEM_LIST | VARCHAR2(500) | N | Item Name / List in the form of the Free Text |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_INCLUDE`: PACKAGE_ID, SERIAL_NO
- **Triggers**: `PACKAGE_INCLUDE_CEA` (before insert or update or delete), `PACKAGE_INCLUDE_DEL` (after delete), `PACKAGE_INCLUDE_INS` (before insert), `PACKAGE_INCLUDE_UPD` (before update), `TRG_WS_OTH_UH_GQ_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_ITEM
This table will be used to link the Items with the package

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref key |
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This Column will represents the Service Type |
| ITEM_ID | VARCHAR2(18) | N | Item/CPT/Service which will be linked with the package OR which is part of the package |
| QUANTITY | NUMBER(6) default 1 | N | Total Quantity which will be ordered when this Package will be used |
| PRICE | NUMBER(12,2) | N | This column will be used to save the Price of the Item (CPT, Drug, Item) within a Package, it can be different from original Table e.g.  CBC is 100 in definitions.cpt but it can 110 or 90 in this table |
| NO_OF_ITEM_ALLOWED | NUMBER default 1 | N | Total Number of Item Allowed will be entered, if value is zero then it is unlimited |
| NO_OF_ITEM_AVAILED | NUMBER default 0 | N | This column will represents the No. of Item Availed, it must be less or equal to NO_OF_ITEM_ALLOWED |
| ACTIVE | VARCHAR2(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_ITEM`: PACKAGE_ID, SERVICE_TYPE_ID, ITEM_ID
- **FK** `FK_PACKAGE_ITEM_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **FK** `FK_PACKAGE_ITEM_2`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID) [disabled]
- **CHECK** `CK_PACKAGE_ITEM_1`: QUANTITY>=1
- **CHECK** `CK_PACKAGE_ITEM_2`: NO_OF_ITEM_ALLOWED>=1
- **CHECK** `CK_PACKAGE_ITEM_3`: NO_OF_ITEM_ALLOWED>=NO_OF_ITEM_AVAILED
- **CHECK** `CK_PACKAGE_ITEM_4`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_ITEM_CEA` (before insert or update or delete), `PACKAGE_ITEM_DEL` (after delete), `PACKAGE_ITEM_INS` (before insert), `PACKAGE_ITEM_UPD` (before update), `TRG_WS_YTP_YK_UT_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_ITEM_ERRLOG

| Column | Type | Null | Comment |
|---|---|---|---|
| ORA_ERR_NUMBER$ | NUMBER | Y |  |
| ORA_ERR_MESG$ | VARCHAR2(2000) | Y |  |
| ORA_ERR_ROWID$ | ROWID | Y |  |
| ORA_ERR_OPTYP$ | VARCHAR2(2) | Y |  |
| ORA_ERR_TAG$ | VARCHAR2(2000) | Y |  |
| PACKAGE_ID | VARCHAR2(10) | N |  |
| SERVICE_TYPE_ID | VARCHAR2(3) | N |  |
| ITEM_ID | VARCHAR2(18) | N |  |

- **PK** `PK_PACKAGE_ITEM_ERRLOG`: PACKAGE_ID, SERVICE_TYPE_ID, ITEM_ID
- **Triggers**: `PACKAGE_ITEM_ERRLOG_CEA` (before insert or update or delete), `TRG_WS_TPL_WL_VO_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_ITEM_EXTRA_CHARGE
This table will be used to add the Item list which will be separately charged (If they necessary for the Surgery)

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| SERIAL_NO | NUMBER(3) | N | Counter of the Table which will reset on every new Package |
| ITEM_LIST | VARCHAR2(500) | N | Item List |
| ESTIMATED_AMOUNT | VARCHAR2(60) | N | Minimu to Maximum Cost of the Item List |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_ITEM_EXTRA_CHARGE`: PACKAGE_ID, SERIAL_NO
- **FK** `FK_PACKAGE_ITEM_EXTRA_CHARGE_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **Triggers**: `PACKAGE_ITEM_EXTRA_CHARGE_CEA` (before insert or update or delete), `PACKAGE_ITEM_EXTRA_CHARGE_DEL` (after delete), `PACKAGE_ITEM_EXTRA_CHARGE_INS` (before insert), `PACKAGE_ITEM_EXTRA_CHARGE_UPD` (before update), `TRG_WS_SSJ_RW_BR_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_KEY_OBJECT
This table will be used to add the key objects of the Package

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| SERIAL_NO | NUMBER(3) | N | Counter of the Table which will reset on every new package |
| ITEM_LIST | VARCHAR2(500) | N | Items list |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_PACKAGE_KEY_OBJECT`: PACKAGE_ID, SERIAL_NO
- **FK** `FK_PACKAGE_KEY_OBJECT_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **Triggers**: `PACKAGE_KEY_OBJECT_CEA` (before insert or update or delete), `PACKAGE_KEY_OBJECT_DEL` (after delete), `PACKAGE_KEY_OBJECT_INS` (before insert), `PACKAGE_KEY_OBJECT_UPD` (before update), `TRG_WS_WKY_BA_XB_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_PERFORMER
This table will be used to link the Packages with the performer

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Package Ref |
| PERFORMER_MRNO | VARCHAR2(14) | N | User /Performer to whom this Package is linked |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |
| COPIED_FAVOURITE | CHAR(1) default 'N' | Y | This column's value is 'Y' when copied favourites from other user. |
| COPIED_FROM | VARCHAR2(14) | Y | User Mrno from where favourites is copied. |

- **PK** `PK_PACKAGE_PERFORMER`: PACKAGE_ID, PERFORMER_MRNO
- **CHECK** `CK_PACKAGE_PERFORMER_1`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_PERFORMER_CEA` (before insert or update or delete), `PACKAGE_PERFORMER_DEL` (after delete), `PACKAGE_PERFORMER_INS` (before insert), `PACKAGE_PERFORMER_UPD` (before update), `TRG_WS_DMB_IT_HG_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_SERVICES
This table will be used link the Services Type with the Package

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | This column will represents the Package |
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This Column will represents the Service Type attached with the Package e.g. Consultation, Radiology etc. |
| ALL_SERVICES | CHAR(1) default 'N' | N | Value of This column will be Y/N, if Y then All Items of these services are allowed |
| TREATMENT_LIMIT_APPLY | CHAR(1) default 'N' | N | Values of this column will be Y/N, If value is Y for more than one Services then Amount will be sum up except Medicine/Supplies/Consultation |
| TREATMENT_LIMIT_AMOUNT | NUMBER(7) default 0 | N | Total Amount which will be used for this services or sum up with other services |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |
| NO_OF_ITEM_ALLOWED | NUMBER | Y | Total Number of Item Allowed will be entered, if value is zero or null  then it is unlimited |
| FREQUENCY | CHAR(1) | Y | D FOR DAYS W FOR WEEKS F FORTNIGHTLY  M MONTHLY  Y YEARLY |

- **PK** `PK_PACKAGE_SERVICES`: PACKAGE_ID, SERVICE_TYPE_ID
- **FK** `FK_PACKAGE_SERVICES_1`: (PACKAGE_ID) -> DEFINITIONS.PACKAGES(PACKAGE_ID)
- **FK** `FK_PACKAGE_SERVICES_2`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID) [disabled]
- **CHECK** `CK_PACKAGE_SERVICES_1`: ALL_SERVICES IN ('Y','N'
- **CHECK** `CK_PACKAGE_SERVICES_2`: TREATMENT_LIMIT_APPLY IN ('Y','N'
- **CHECK** `CK_PACKAGE_SERVICES_3`: ACTIVE IN ('Y','N'
- **Triggers**: `PACKAGE_SERVICES_CEA` (before insert or update or delete), `PACKAGE_SERVICES_DEL` (after delete), `PACKAGE_SERVICES_INS` (before insert), `PACKAGE_SERVICES_UPD` (before update), `TRG_WS_JRW_FO_RA_Q` (after insert or update or delete)

## DEFINITIONS.ROOM_PAYMENT_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| CPT_ID_SUPPORTED | VARCHAR2(18) | N |  |
| PARENT_PAYMENT_CATEGORY_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ROOM_PAYMENT_CATEGORY`: ROOM_PAYMENT_CATEGORY_ID
- **UK** `UK_ROOM_PAYMENT_CATEGORY`: DESCRIPTION
- **FK** `FK_ROOM_PAYMENT_CATEGORY_1`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_ROOM_PAYMENT_CATEGORY`: ACTIVE IN ('N','Y'
- **Triggers**: `ROOM_PAYMENT_CATEGORY_CEA` (before insert or update or delete), `ROOM_PAYMENT_CATEGORY_DEL` (after delete), `ROOM_PAYMENT_CATEGORY_INS` (before insert), `ROOM_PAYMENT_CATEGORY_UPD` (before update), `TRG_WS_HAF_RS_JO_Q` (after insert or update or delete)

## DEFINITIONS.PACKAGE_STAY
This table is child of DEFINITIONS.PACKAGE_DETAIL, which contains information about multiple types of stay included in package.

| Column | Type | Null | Comment |
|---|---|---|---|
| PACKAGE_ID | VARCHAR2(10) | N | Ref of Package Detail PK |
| TREATMENT_COVER | CHAR(1) default 'I' | N | Ref of Package Detail PK |
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N | Ref of Room_Payment_Category |
| DAYS | NUMBER(2) | Y | Number of days |

- **PK** `PK_PACKAGE_STAY`: PACKAGE_ID, TREATMENT_COVER, ROOM_PAYMENT_CATEGORY_ID
- **FK** `FK_PACKAGE_STAY_1`: (PACKAGE_ID, TREATMENT_COVER) -> DEFINITIONS.PACKAGE_DETAIL(PACKAGE_ID, TREATMENT_COVER)
- **FK** `FK_PACKAGE_STAY_2`: (ROOM_PAYMENT_CATEGORY_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID) [disabled]
- **Triggers**: `PACKAGE_STAY_CEA` (before insert or update or delete), `PACKAGE_STAY_DEL` (after delete), `PACKAGE_STAY_INS` (before insert), `PACKAGE_STAY_UPD` (before update), `TRG_WS_SZY_ZV_RE_Q` (after insert or update or delete)

## DEFINITIONS.PAGERS_R

| Column | Type | Null | Comment |
|---|---|---|---|
| CAP_CODE | NUMBER(9) | Y |  |
| LOCAL_ID | NUMBER(3) | Y |  |
| FIRST_NAME | VARCHAR2(30) | Y |  |
| LAST_NAME | VARCHAR2(30) | Y |  |
| PARENT_ID | VARCHAR2(15) | Y |  |


## DEFINITIONS.PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER | N |  |
| LONG_DESC | VARCHAR2(120) | N |  |
| SHORT_DESC | VARCHAR2(120) | Y |  |
| FIELD_TYPE_ID | NUMBER | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DISPLAY_ORDER | NUMBER(4) | Y |  |

- **PK** `PK_PARAMETERS`: PARAMETER_ID
- **UK** `UK_PARAMETERS_001`: LONG_DESC
- **UK** `UK_PARAMETERS_002`: LONG_DESC, FIELD_TYPE_ID
- **FK** `FK_PARAMETERS_1`: (FIELD_TYPE_ID) -> DEFINITIONS.FIELD_TYPE(FIELD_TYPE_ID) [disabled]
- **Triggers**: `PARAMETERS_DEL` (after delete), `PARAMETERS_INS` (before insert), `PARAMETERS_UPD` (before update)

## DEFINITIONS.SECTION_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | VARCHAR2(6) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| FIX_VALUE | VARCHAR2(1) | Y |  |
| DISPLAY_ORDER | NUMBER(2) | Y |  |

- **PK** `PK_SECTION_PARAMETER`: PARAMETER_ID, DEPARTMENT_ID, SECTION_ID
- **FK** `FK_SECTION_PARAMETER_1`: (PARAMETER_ID) -> DEFINITIONS.BASIC_PARAMETERS(PARAMETER_ID)
- **Triggers**: `SECTION_PARAMETER_CEA` (before insert or update or delete), `SECTION_PARAMETER_DEL` (after delete), `SECTION_PARAMETER_INS` (before insert), `SECTION_PARAMETER_UPD` (before update), `TRG_WS_LBG_WB_BK_Q` (after insert or update or delete)

## DEFINITIONS.PARAMETER_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | VARCHAR2(6) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| VALUE | VARCHAR2(500) | N |  |
| DEFAULT_VALUE | VARCHAR2(1) | Y |  |
| VALUE_ORDER | NUMBER(2) | Y |  |

- **PK** `PK_PARAMETER_VALUES`: PARAMETER_ID, DEPARTMENT_ID, SECTION_ID, VALUE
- **FK** `FK_PV_1`: (PARAMETER_ID, DEPARTMENT_ID, SECTION_ID) -> DEFINITIONS.SECTION_PARAMETER(PARAMETER_ID, DEPARTMENT_ID, SECTION_ID)
- **Triggers**: `PARAMETER_VALUES_CEA` (before insert or update or delete), `TRG_WS_EMJ_HB_XD_Q` (after insert or update or delete)

## DEFINITIONS.SYMPTOMS

| Column | Type | Null | Comment |
|---|---|---|---|
| SYMPTOM_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SYMPTOM_TYPE | VARCHAR2(2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_SYMPTOMS`: SYMPTOM_ID
- **Triggers**: `SYMPTOMS_CEA` (before insert or update or delete), `SYMPTOMS_DEL` (after delete), `SYMPTOMS_INS` (before insert), `SYMPTOMS_UPD` (before update), `TRG_WS_RTD_YE_AV_Q` (after insert or update or delete)

## DEFINITIONS.PARAM_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER | N |  |
| VALUE_ID | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | Y |  |
| SYMPTOM_ID | NUMBER(4) | Y |  |
| ID | NUMBER | Y |  |

- **PK** `PK_PARAM_VALUES`: ID
- **UK** `UK_PARAM_VALUES_1`: PARAMETER_ID, VALUE_ID, SYMPTOM_ID
- **FK** `FK_PARAM_VALUES_1`: (VALUE_ID) -> DEFINITIONS.DEF_VALUES(VALUE_ID) [disabled]
- **FK** `FK_PARAM_VALUES_2`: (PARAMETER_ID) -> DEFINITIONS.PARAMETERS(PARAMETER_ID)
- **FK** `FK_PARAM_VALUES_3`: (SYMPTOM_ID) -> DEFINITIONS.SYMPTOMS(SYMPTOM_ID) [disabled]
- **Triggers**: `PARAM_VALUES_DEL` (after delete), `PARAM_VALUES_INS` (before insert), `PARAM_VALUES_UPD` (before update)

## DEFINITIONS.PARENT_CLINIC

| Column | Type | Null | Comment |
|---|---|---|---|
| PARENT_CLINIC_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PARENT_CLINIC`: PARENT_CLINIC_ID
- **Triggers**: `PARENT_CLINIC_CEA` (before insert or update or delete), `PARENT_CLINIC_DEL` (after delete), `PARENT_CLINIC_INS` (before insert), `PARENT_CLINIC_UPD` (before update), `TRG_WS_HMZ_ZR_XQ_Q` (after insert or update or delete)

## DEFINITIONS.PATHOLOGY_EVENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| EVENT_ID | NUMBER(4) | N |  |
| EVENT_DESCRIPTION | VARCHAR2(100) | Y |  |
| STATUS_ID | VARCHAR2(3) | N |  |
| NATURE_ID | VARCHAR2(3) | N |  |
| ORDER_BY | NUMBER(2) | N |  |
| ACTIVE | CHAR(1) | Y | This column contain flag shows active status (Y=active, N=inactive) |
| LOG_EVENT | CHAR(1) | Y | This column contains Flag Information to log Event (O=Order CPT, D=Module/Detail) |

- **PK** `PK_PATHOLOGY_EVENTS`: EVENT_ID
- **Triggers**: `PATHOLOGY_EVENTS_DEL` (after delete), `PATHOLOGY_EVENTS_INS` (before insert), `PATHOLOGY_EVENTS_UPD` (before update)

## DEFINITIONS.PATIENT_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_DESIGNATION_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |
| STRUCTURE_ID | VARCHAR2(3) | N |  |
| BASIC_PAY_SCALE | VARCHAR2(6) | Y |  |

- **PK** `PK_PATIENT_DESIGNATION`: PATIENT_DESIGNATION_ID
- **UK** `UK_PATIENT_DESIGNATION`: DESCRIPTION
- **CHECK** `CHK_PATIENT_DESIGNATION`: ACTIVE IN ('N','Y'

## DEFINITIONS.PATIENT_DOC_ATTACHMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N | This column contains patient MRNO |
| SR_NO | NUMBER | N | This column contains srno |
| DOCUMENT_ID | VARCHAR2(13) | Y | This column contains document ID ref lob.document store |
| DESCRIPTION | VARCHAR2(4000) | Y | This column contains description |
| ENTRY_DATE | DATE | Y | This column contains entry date |
| ATTACHED_BY | VARCHAR2(14) | Y | This column contains attached by mrno |
| REMARKS | VARCHAR2(4000) | Y | This column contains remarks |
| DOC_TYPE_ID | NUMBER | Y | This column contains document type ID |

- **PK** `PK_PAT_DOC_ATTACHMENT_1`: MRNO, SR_NO
- **FK** `FK_PAT_DOC_ATTACHMENT_1`: (DOCUMENT_ID) -> LOB.DOCUMENTS_STORE(DOCUMENT_ID) [disabled]
- **FK** `FK_PAT_DOC_ATTACHMENT_2`: (DOC_TYPE_ID) -> DEFINITIONS.ATTACHMENT_DOCUMENT_TYPE(DOC_TYPE_ID) [disabled]
- **Triggers**: `PATIENT_DOC_ATTACHMENT_DEL` (after delete), `PATIENT_DOC_ATTACHMENT_INS` (before insert), `PATIENT_DOC_ATTACHMENT_UPD` (before update)

## DEFINITIONS.PATIENT_ED_PARAMETER

| Column | Type | Null | Comment |
|---|---|---|---|
| PARAMETER_ID | NUMBER(3) | N | This col contains parameter id |
| PARAMETER_DESC | VARCHAR2(100) | N | This col contains Parameter Description |
| ORDER_BY | NUMBER(3) | Y | This col is used to view the records according to this col |
| ACTIVE | CHAR(1) default 'Y' | Y | Y=Active N=Inactive |
| OBJECT_CODE | VARCHAR2(11) | Y | This column contains object_code of calling form |

- **PK** `DEF_PATIENT_ED_PARAMETER_PK`: PARAMETER_ID, ORG_ID
- **Triggers**: `PATIENT_ED_PARAMETER_CEA` (before insert or update or delete), `TRG_WS_FSZ_HD_VJ_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(5) | N | Category/Group ID |
| GROUP_DESC | VARCHAR2(100) | N | Category/Group Description (e.g. Indigent, Diagnostic, Employee etc) |
| ORDER_BY | NUMBER(3) | N | Display order by |
| DEPARTMENT_ID | VARCHAR2(7) | N | department id foreign key reference DEFINITIONS.DEPARTMENT |
| ACTIVE | CHAR(1) default 'Y' | N | Y=Active, N=Inactive |
| CATEGORY_ID | VARCHAR2(3) | N |  |
| GROUP_CODE | VARCHAR2(3) | Y | Unique prefix/identifier for group code |

- **PK** `PK_PATIENT_GROUPS`: GROUP_ID
- **UK** `UK_PATIENT_GROUPS_1`: CATEGORY_ID, GROUP_DESC
- **FK** `FK_PATIENT_GROUPS_1`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **CHECK** `CK_PATIENT_GROUPS_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_PATIENT_GROUPS_2`: GROUP_DESC = UPPER(GROUP_DESC
- **Triggers**: `PATIENT_GROUPS_CEA` (before insert or update or delete), `TRG_WS_PCT_TP_WZ_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_GROUPS_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(5) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N | Department id |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_PATIENT_GROUPS_DETAIL`: GROUP_ID, PATIENT_TYPE_ID
- **UK** `UK_PATIENT_GROUPS_DETAIL_1`: DEPARTMENT_ID, PATIENT_TYPE_ID
- **FK** `FK_PATIENT_GROUPS_DETAIL_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **CHECK** `CK_PATIENT_GROUPS_DETAIL_1`: ACTIVE IN ('Y','N'
- **Triggers**: `PATIENT_GROUPS_DETAIL_CEA` (before insert or update or delete), `TRG_WS_DBN_KP_DU_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_RESULT_VALUE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | VARCHAR2(5) | N |  |
| DURATION | NUMBER(5) | Y |  |
| DURATION_UNIT_ID | VARCHAR2(5) | Y |  |
| DURATION_UNIT_VALUE | NUMBER(8,4) | Y |  |
| USAGE_AREA | VARCHAR2(15) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| EVENT | VARCHAR2(4) | Y | This Column use to insert data event wise. HIST - will be use for Chemo History form,      RDSN - will be use for Resident Verification. |

- **PK** `PK_PATIENT_RESULT_VALUE_SETUP`: SETUP_ID

## DEFINITIONS.PATIENT_SENSUS_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PERFORM_DATE | DATE | Y |  |
| BLOOD_PRESSURE_HIGH | VARCHAR2(4) | Y |  |
| BLOOD_PRESSURE_LOW | VARCHAR2(4) | Y |  |
| TEMP_CENTIGRADE | VARCHAR2(4) | Y |  |
| TEMP_FAHRENHEIT | VARCHAR2(4) | Y |  |
| WEIGHT_POUNDS | NUMBER(4) | Y |  |
| WEIGHT_KG | NUMBER(4) | Y |  |
| HEIGHT_INCHES | NUMBER(4) | Y |  |
| HEIGHT_CM | NUMBER(5) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **FK** `FK_PATIENT_SENSUS`: (MRNO) -> REGISTRATION.PATIENT(MRNO) [disabled]

## DEFINITIONS.PATIENT_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | CHAR(1) | N |  |
| STATUS_DESCRIPTION | VARCHAR2(255) | Y |  |

- **PK** `PK_PATIENT_STATUS`: STATUS_ID
- **UK** `UK_PATIENT_STATUS`: STATUS_DESCRIPTION
- **Triggers**: `PATIENT_STATUS_CEA` (before insert or update or delete), `PATIENT_STATUS_DEL` (after delete), `PATIENT_STATUS_INS` (before insert), `PATIENT_STATUS_UPD` (before update), `TRG_WS_ZVZ_KP_XD_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_STATUS_DISEASES

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_ID | NUMBER(6) | N |  |
| STATUS_ID | CHAR(1) | N |  |

- **PK** `PK_PATIENT_STATUS_DISEASES`: DISEASE_ID, STATUS_ID
- **FK** `FK_PAT_STATUS_DISEASES_1`: (DISEASE_ID) -> DEFINITIONS.DISEASES(DISEASE_ID)
- **FK** `FK_PAT_STATUS_DISEASES_2`: (STATUS_ID) -> DEFINITIONS.PATIENT_STATUS(STATUS_ID) [disabled]
- **Triggers**: `PATIENT_STATUS_DISEASES_CEA` (before insert or update or delete), `PATIENT_STATUS_DISEASES_DEL` (after delete), `PATIENT_STATUS_DISEASES_INS` (before insert), `PATIENT_STATUS_DISEASES_UPD` (before update), `TRG_WS_WCD_JQ_DK_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_TRANSFER_MODE

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(3) | N |  |
| TRANSFER_MODE_DESC | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_PATIENT_TRANSFER_MODE`: SERIAL_NO
- **CHECK** `CHK_1`: ACTIVE IN ('N','Y'
- **Triggers**: `PATIENT_TRANSFER_MODE_CEA` (before insert or update or delete), `TRG_WS_KTM_JC_EQ_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_TYPE_BASE

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_BASE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_PATIENT_TYPE_BASE`: PATIENT_TYPE_BASE_ID
- **Triggers**: `PATIENT_TYPE_BASE_CEA` (before insert or update or delete), `PATIENT_TYPE_BASE_DEL` (after delete), `PATIENT_TYPE_BASE_INS` (before insert), `PATIENT_TYPE_BASE_UPD` (before update), `TRG_WS_MCD_UA_KS_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_TYPE_BK_EMP_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| COUNTER | NUMBER(6) | Y |  |
| PREFIX | VARCHAR2(3) | N |  |
| INTER_CONVERSION | NUMBER(3) | Y |  |
| FS_ALLOWED | VARCHAR2(1) | N |  |
| SPONSORSHIP_ALLOWED | VARCHAR2(1) | N |  |
| DISCOUNT_ALLOWED | VARCHAR2(1) | N |  |
| BONUS_TEST_ALLOWED | VARCHAR2(1) | N |  |
| REFUND_ALLOWED | VARCHAR2(1) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| TYPE_GROUP | VARCHAR2(3) | Y |  |
| DISPLAY_ALLOWED | VARCHAR2(1) | Y |  |
| BOOKING_ALLOWED | VARCHAR2(1) | Y |  |
| EMPLOYEE | VARCHAR2(1) | Y |  |
| MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(5) | Y |  |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| CHILDREN_MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| LEAVE_CONTRACT_ID | VARCHAR2(3) | Y |  |
| ORDERABLE | VARCHAR2(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| INHOUSE_ORDER | CHAR(1) | N |  |
| CARD_SWIPER | CHAR(1) | N |  |
| SALARY_ALLOWED | CHAR(1) | N |  |
| PATHOLOGY_CRITICAL_ALERT | CHAR(1) | Y |  |
| DEFAULT_DIAGNOSIS_STATUS | CHAR(1) | Y |  |
| DIAGNOSTIC_PATIENT | CHAR(1) | N |  |
| INCLUDE_IN_HR_REPORTS | CHAR(1) | N |  |
| REF_LETTER_REQ | CHAR(1) | Y |  |
| CREATE_MRNO | CHAR(1) | N |  |
| BLOCK_ACCESS_CODE_VIEW | CHAR(1) | Y |  |


## DEFINITIONS.PATIENT_TYPE_BK_R

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| COUNTER | NUMBER(6) | Y |  |
| PREFIX | VARCHAR2(3) | N |  |
| INTER_CONVERSION | NUMBER(3) | Y |  |
| FS_ALLOWED | VARCHAR2(1) | N |  |
| SPONSORSHIP_ALLOWED | VARCHAR2(1) | N |  |
| DISCOUNT_ALLOWED | VARCHAR2(1) | N |  |
| BONUS_TEST_ALLOWED | VARCHAR2(1) | N |  |
| REFUND_ALLOWED | VARCHAR2(1) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| TYPE_GROUP | VARCHAR2(3) | Y |  |
| DISPLAY_ALLOWED | VARCHAR2(1) | Y |  |
| BOOKING_ALLOWED | VARCHAR2(1) | Y |  |
| EMPLOYEE | VARCHAR2(1) | Y |  |
| MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(5) | Y |  |
| SPOUSE_MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| CHILDREN_MEDICAL_ALLOWED | VARCHAR2(1) | Y |  |
| LEAVE_CONTRACT_ID | VARCHAR2(3) | Y |  |
| ORDERABLE | VARCHAR2(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| INHOUSE_ORDER | CHAR(1) | N |  |
| CARD_SWIPER | CHAR(1) | N |  |
| SALARY_ALLOWED | CHAR(1) | N |  |
| PATHOLOGY_CRITICAL_ALERT | CHAR(1) | Y |  |
| DEFAULT_DIAGNOSIS_STATUS | CHAR(1) | Y |  |
| DIAGNOSTIC_PATIENT | CHAR(1) | N |  |
| INCLUDE_IN_HR_REPORTS | CHAR(1) | N |  |
| REF_LETTER_REQ | CHAR(1) | Y |  |
| CREATE_MRNO | CHAR(1) | N |  |
| BLOCK_ACCESS_CODE_VIEW | CHAR(1) | Y |  |


## DEFINITIONS.PATIENT_TYPE_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| PREFIX_LOCATION | VARCHAR2(3) | N |  |
| COUNTER | NUMBER(10) | Y |  |
| PREFIX | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_PATIENT_TYPE_COUNTER`: PREFIX_LOCATION, ORGANIZATION_ID, PREFIX
- **FK** `FK_PATIENT_TYPE_COUNTER_2`: (PREFIX_LOCATION) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_PATIENT_TYPE_COUNTER_3`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **Triggers**: `PATIENT_TYPE_COUNTER_DEL` (after delete), `PATIENT_TYPE_COUNTER_INS` (before insert), `PATIENT_TYPE_COUNTER_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_CPTS

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| CARD_FEE_CPT_ID | VARCHAR2(18) | Y | This field will be used to save the Patient's Card Fee CPT Id |

- **PK** `PK_PATIENT_TYPE_CPTS`: LOCATION_ID, PATIENT_TYPE_ID, CPT_ID
- **FK** `FK_PATIENT_TYPE_CPTS_1`: (LOCATION_ID, PATIENT_TYPE_ID) -> DEFINITIONS.LOCATION_WISE_PATIENT_TYPES(LOCATION_ID, PATIENT_TYPE_ID)
- **FK** `FK_PATIENT_TYPE_CPTS_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **FK** `FK_PATIENT_TYPE_CPTS_3`: (CARD_FEE_CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **Triggers**: `PATIENT_TYPE_CPTS_DEL` (after delete), `PATIENT_TYPE_CPTS_INS` (before insert), `PATIENT_TYPE_CPTS_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_EMPLOYER

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| EMPLOYER_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PATIENT_TYPE_EMPLOYER`: PATIENT_TYPE_ID, EMPLOYER_ID
- **CHECK** `CHK_PATIENT_TYPE_EMPLOYER_1`: ACTIVE IN ('N','Y'

## DEFINITIONS.PATIENT_TYPE_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| PATIENT_TYPE_BASE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_PATIENT_TYPE_GROUP`: PATIENT_TYPE_ID, PATIENT_TYPE_BASE_ID
- **FK** `FK_PATIENT_TYPE_GROUP_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **FK** `FK_PATIENT_TYPE_GROUP_2`: (PATIENT_TYPE_BASE_ID) -> DEFINITIONS.PATIENT_TYPE_BASE(PATIENT_TYPE_BASE_ID)
- **Triggers**: `PATIENT_TYPE_GROUP_CEA` (before insert or update or delete), `TRG_WS_RJY_IZ_WU_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_TYPE_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PATIENT_TYPE_GROUPS`: GROUP_ID
- **Triggers**: `PATIENT_TYPE_GROUPS_DEL` (after delete), `PATIENT_TYPE_GROUPS_INS` (before insert), `PATIENT_TYPE_GROUPS_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_GROUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(3) | Y |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **Triggers**: `PATIENT_TYPE_GROUP_DETAIL_DEL` (after delete), `PATIENT_TYPE_GROUP_DETAIL_INS` (before insert), `PATIENT_TYPE_GROUP_DETAIL_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_ITEM_PRICE
This table will be used to define the Item Prices Patient Type Wise

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N | Patient Type Ref |
| ITEM_ID | VARCHAR2(18) | N | Item which include Pharmacy, CPT, Supplies, one CPT can be charged of Rs. 100/- to Regular Patient Type but Rs. 200/- to Private Patient |
| PRICE | NUMBER(12,2) | N | Amount which will be charged against this Item |
| LOCATION_ID | VARCHAR2(3) | N | This column will be the part of primary key along with patient type id |

- **PK** `PK_PATIENT_TYPE_ITEM_PRICE`: LOCATION_ID, PATIENT_TYPE_ID, ITEM_ID
- **FK** `FK_PATIENT_TYPE_ITEM_PRICE_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **CHECK** `CK_PATIENT_TYPE_ITEM_PRICE_1`: PRICE>0
- **Triggers**: `PATIENT_TYPE_ITEM_PRICE_DEL` (after delete), `PATIENT_TYPE_ITEM_PRICE_INS` (before insert), `PATIENT_TYPE_ITEM_PRICE_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_MAP

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(100) | N |  |
| HEAD_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| ORDER_BY | NUMBER | Y |  |
| SUB_GROUP_ID | NUMBER | N |  |
| SERVICE_ID | NUMBER | Y | This column is reference of DEFINITIONS.ARMY_SERVICE.ID column |

- **PK** `PK_PATIENT_TYPE_MAP`: HEAD_ID, SUB_GROUP_ID, PATIENT_TYPE_ID
- **Triggers**: `PATIENT_TYPE_MAP_INS` (before insert)

## DEFINITIONS.PATIENT_TYPE_PREFIX

| Column | Type | Null | Comment |
|---|---|---|---|
| PREFIX | VARCHAR2(3) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_PATIENT_TYPE_PREFIX`: PREFIX, PATIENT_TYPE_ID, LOCATION_ID, ORGANIZATION_ID
- **FK** `FK_PATIENT_TYPE_PREFIX_1`: (LOCATION_ID, PATIENT_TYPE_ID) -> DEFINITIONS.LOCATION_WISE_PATIENT_TYPES(LOCATION_ID, PATIENT_TYPE_ID) [disabled]
- **Triggers**: `PATIENT_TYPE_PREFIX_DEL` (after delete), `PATIENT_TYPE_PREFIX_INS` (before insert), `PATIENT_TYPE_PREFIX_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_REST_PERMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| ROLE_ID | NUMBER(10) | N |  |
| RESTRICTION_TYPE | CHAR(1) | N |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'PTR' | N | DUR mean Duration Restricted,PTR Patient Type Restriction |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PATIENT_TYPE_REST`: PATIENT_TYPE_ID, ROLE_ID, RESTRICTION_TYPE, RESTRICTION_CATEGORY
- **Triggers**: `PATIENT_TYPE_PERM_INSERT` (before insert), `PATIENT_TYPE_REST_PERMIT_CEA` (before insert or update or delete), `TRG_WS_QPI_OR_OC_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_TYPE_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| SERVICE_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_PATIENT_TYPE_SERVICES`: PATIENT_TYPE_ID, SERVICE_ID
- **FK** `FK_PATIENT_TYPE_SERVICES_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **FK** `FK_PATIENT_TYPE_SERVICES_2`: (SERVICE_ID) -> DEFINITIONS.ARMY_SERVICE(ID) [disabled]
- **Triggers**: `PATIENT_TYPE_SERVICES_DEL` (after delete), `PATIENT_TYPE_SERVICES_INS` (before insert), `PATIENT_TYPE_SERVICES_UPD` (before update)

## DEFINITIONS.PATIENT_TYPE_TMP

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |


## DEFINITIONS.PATIENT_TYPE_WISE_DISEASES

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE_ID | NUMBER(6) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| RESTRICTED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PATIENT_TYPE_DISEASE`: DISEASE_ID, PATIENT_TYPE_ID
- **FK** `FK_DISEASE_ID`: (DISEASE_ID) -> DEFINITIONS.DISEASES(DISEASE_ID)
- **FK** `PK_PATIENT_TYPE_ID`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **Triggers**: `PATIENT_TYPE_WISE_DISEASES_CEA` (before insert or update or delete), `PATIENT_TYPE_WISE_DISEASES_DEL` (after delete), `PATIENT_TYPE_WISE_DISEASES_INS` (before insert), `PATIENT_TYPE_WISE_DISEASES_UPD` (before update), `TRG_WS_QUC_BR_RP_Q` (after insert or update or delete)

## DEFINITIONS.PATIENT_VITALS
This setup table will be used to enable the patient vitals information object wise and age group wise.

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| PARAMETER_ID | VARCHAR2(3) | Y | This colun will be used to store the vitals parameter for example: HT - Height, WT - Weight, etc. |
| PARAMETER_DESC | VARCHAR2(100) | Y | This colun will be used to store the vitals parameter description for example Height, Weight, etc. |
| AGE_GROUP | VARCHAR2(1) | Y | This colun will be used to store the age group wise setup information. |
| OBJECT_CODE | VARCHAR2(30) | Y | This colun will be used to store the object code wise setup information. |
| ACTIVE | VARCHAR2(1) | Y | Y - Active, N - Inactive. |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_PATIENT_VITALS`: SR_NO
- **Triggers**: `PATIENT_VITALS_DEL` (after delete), `PATIENT_VITALS_INS` (before insert), `PATIENT_VITALS_UPD` (before update)

## DEFINITIONS.PATIENT_VULNERABILITIES

| Column | Type | Null | Comment |
|---|---|---|---|
| VUL_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(2000) | N |  |
| SHORT_DESCP | VARCHAR2(500) | N |  |
| ACTIVE | VARCHAR2(1) default 'N' | N |  |
| FILE_ADDRESS | VARCHAR2(200) | Y |  |

- **PK** `PK_PATIENT_VULNERABILITIES`: VUL_ID
- **UK** `UK_PATIENT_VULNERABILITES_1`: DESCRIPTION
- **UK** `UK_PATIENT_VULNERABILITES_2`: SHORT_DESCP
- **Triggers**: `PATIENT_VULNERABILITIES_DEL` (after delete), `PATIENT_VULNERABILITIES_INS` (before insert), `PATIENT_VULNERABILITIES_UPD` (before update)

## DEFINITIONS.PATIENT_WISE_RELATION

| Column | Type | Null | Comment |
|---|---|---|---|
| RELATION_ID | VARCHAR2(6) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| AGE | NUMBER | Y |  |
| VALIDITY_DURATION | NUMBER(5,1) | Y |  |
| VALIDITY_DURATION_UNIT_ID | CHAR(1) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| MEDICAL_ALLOWED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PATIENT_WISE_RELATION_PK`: RELATION_ID, PATIENT_TYPE_ID
- **Triggers**: `PATIENT_WISE_RELATION_DEL` (after delete), `PATIENT_WISE_RELATION_INS` (before insert), `PATIENT_WISE_RELATION_UPD` (before update)

## DEFINITIONS.PAT_TYPE_LOC_REST_PERMIT

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ROLE_ID | NUMBER(10) | Y |  |
| RESTRICTION_TYPE | CHAR(1) | Y |  |
| RESTRICTION_CATEGORY | VARCHAR2(3) default 'PTR' | Y | DUR mean Duration Restricted,PTR Patient Type Restriction |
| ACTIVE | CHAR(1) | Y |  |

- **Triggers**: `PAT_TYPE_LOC_PERM_INSERT` (before insert)

## DEFINITIONS.PCR_CENTRE

| Column | Type | Null | Comment |
|---|---|---|---|
| CENTRE_ID | VARCHAR2(8) | N |  |
| COUNTRY_ID | NUMBER(4) | Y |  |
| STATE_ID | NUMBER(4) | Y |  |
| DISTRICT_ID | NUMBER(4) | Y |  |
| TEHSIL_ID | NUMBER(4) | Y |  |
| DESCRIPTION | VARCHAR2(120) | Y |  |
| ADDRESS | VARCHAR2(500) | Y |  |
| CONTACT_PERSON | VARCHAR2(120) | Y |  |
| PHONE | VARCHAR2(120) | Y |  |
| FAX | VARCHAR2(60) | Y |  |
| EMAIL | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | N |  |
| CENTRE_COUNTER | NUMBER(14) | Y |  |
| REPORTING_TAB_ALLOWED | CHAR(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_PCR_CENTRE`: CENTRE_ID, LOCATION_ID
- **FK** `FK_PCR_CENTRE_1`: (COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]

## DEFINITIONS.PCR_CENTRE_WISE_DISTRICT

| Column | Type | Null | Comment |
|---|---|---|---|
| CENTRE_ID | VARCHAR2(8) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_PCR_CENTRE_WISE_DISTRICT`: CENTRE_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID, LOCATION_ID

## DEFINITIONS.PERFORMANCE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PERFORM_TYPE_ID | VARCHAR2(3) | N |  |
| PERFORM_DESC | VARCHAR2(200) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PERFORMANCE_TYPE`: PERFORM_TYPE_ID

## DEFINITIONS.TRANSACTION_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_GROUP_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ZONE_ID | VARCHAR2(3) | N |  |

- **PK** `PK_TRANSACTION_GROUP`: TRANSACTION_GROUP_ID
- **FK** `FK_TRANSACTION_GROUP_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_TRANSACTION_GROUP_2`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_TRANSACTION_GROUP_3`: (ZONE_ID) -> DEFINITIONS.ZONES(ZONE_ID) [disabled]
- **Triggers**: `TRANSACTION_GROUP_CEA` (before insert or update or delete), `TRANSACTION_GROUP_DEL` (after delete), `TRANSACTION_GROUP_INS` (before insert), `TRANSACTION_GROUP_UPD` (before update), `TRG_WS_MIX_YZ_IJ_Q` (after insert or update or delete)

## DEFINITIONS.TRANSACTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | VARCHAR2(2) | Y |  |
| CLINIC | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | N | Why this column has value A? -- Idrees 21-02-2013 |
| PHARMACY | VARCHAR2(1) | N |  |
| INVOICE | VARCHAR2(1) | N | Is this Transaction Type relevant to some kind of invoice? Y mean Yes, N mean No |
| INVOICE_TYPE | VARCHAR2(1) | N |  |
| TABLE_REFERENCE | VARCHAR2(60) | Y |  |
| SEQUENCE_NAME | VARCHAR2(60) | Y |  |
| MMS_VOUCHER_TYPE | VARCHAR2(5) | Y |  |
| IN_OUT | CHAR(2) | Y | II' Means IPD IN  , 'IO' Means IPD Out , 'OI'  OPD In, 'OO' Means OPD Out, 'PI'  Means Purchase IN , 'PO' Purchase Out |
| TRANSACTION_GROUP_ID | NUMBER(3) | Y | Transaction group ID referenced from Transaction Group |
| MOVE_TYPE_ID | NUMBER(3) | Y | used for mapping of move type id with transaction type |
| DEFAULT_STOCK_LOCATION | VARCHAR2(1) default 'Y' | Y | 'Y' := Default stock location of store,  'N' := Transaction order location |

- **PK** `PK_TRANSACTION_TYPE`: TRANSACTION_TYPE_ID
- **FK** `FK_TRANSACTION_GROUP`: (TRANSACTION_GROUP_ID) -> DEFINITIONS.TRANSACTION_GROUP(TRANSACTION_GROUP_ID) [disabled]
- **FK** `FK_TRANSACTION_TYPE`: (MOVE_TYPE_ID) -> MMS.DEF_MOVE_TYPE(MOVE_TYPE_ID) [disabled]
- **CHECK** `CHK_TRANSACTION_TYPE_01`: INVOICE IN ('Y','N'
- **CHECK** `CHK_TRANSACTION_TYPE_02`: INVOICE_TYPE IN ('Y','N'
- **CHECK** `CHK_TRANSACTION_TYPE_03`: PHARMACY IN ('Y','N'
- **CHECK** `CHK_TRANSACTION_TYPE_04`: ACTIVE IN ('Y','N','A'
- **Triggers**: `TRANSACTION_TYPE_DEL` (after delete), `TRANSACTION_TYPE_INS` (before insert), `TRANSACTION_TYPE_UPD` (before update)

## DEFINITIONS.PHARMACY_DISPENSING_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| PHYSICAL_LOCATION_ID | VARCHAR2(3) | N |  |
| DISPENSING_LOCATION_ID | VARCHAR2(3) | N |  |
| TRANSACTION_TYPE_ID | VARCHAR2(3) | N |  |
| TRANS_TYPE | VARCHAR2(1) default 'B' | N | C = 'Clinical operations' ,  D= 'Dispensing' , B = Both |
| ORDER_BY | NUMBER(2) | Y |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| IPD_OPD | CHAR(1) | N | O= 'OPD' , I = 'IPD', B='Both' |

- **PK** `PK_PHAR_DISPENSING_SETUP`: ORGANIZATION_ID, PHYSICAL_LOCATION_ID, DISPENSING_LOCATION_ID, TRANSACTION_TYPE_ID, IPD_OPD
- **FK** `FK_DISPENSING_LOCATION_ID`: (DISPENSING_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_PHYSICAL_LOCATION_ID`: (PHYSICAL_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_TRANS_TYPE_ID`: (TRANSACTION_TYPE_ID) -> DEFINITIONS.TRANSACTION_TYPE(TRANSACTION_TYPE_ID) [disabled]
- **Triggers**: `PHARMACY_DISPENSING_SETUP_CEA` (before insert or update or delete), `TRG_WS_TIW_PY_XJ_Q` (after insert or update or delete)

## DEFINITIONS.PHYSICAL_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| PHYSICAL_LOCATION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PHYSICAL_LOCATION`: PHYSICAL_LOCATION_ID
- **Triggers**: `PHYSICAL_LOCATION_CEA` (before insert or update or delete), `PHYSICAL_LOCATION_DEL` (after delete), `PHYSICAL_LOCATION_INS` (before insert), `PHYSICAL_LOCATION_UPD` (before update), `TRG_WS_WLL_DB_UD_Q` (after insert or update or delete)

## DEFINITIONS.PHYSICIAN_ORDER_FOR_NURSE
This table is used to define physician orders for nurses (Non Medication).

| Column | Type | Null | Comment |
|---|---|---|---|
| ORDER_ID | VARCHAR2(9) | N | Define Order ID auto incremental from application |
| DESCRIPTION | VARCHAR2(200) | Y | Non Medication Order description |
| REMARKS | VARCHAR2(200) | Y | Remarks for defined description |
| ACTIVE | CHAR(1) | Y | Mark a definition Active or In-Active |

- **PK** `PK_PHYSICIAN_ORDER_FOR_NURSE_1`: ORDER_ID
- **Triggers**: `PHYSICIAN_ORDER_FOR_NURSE_CEA` (before insert or update or delete), `TRG_WS_BXO_TR_PL_Q` (after insert or update or delete)

## DEFINITIONS.POIDD

| Column | Type | Null | Comment |
|---|---|---|---|
| RT | VARCHAR2(10) | N |  |
| DR | VARCHAR2(18) | N |  |
| PRICE | NUMBER(12,2) | N |  |


## DEFINITIONS.POPULATION_CANCER_REGISTRY

| Column | Type | Null | Comment |
|---|---|---|---|
| PCR_ID | NUMBER(3) | N |  |
| PCR_DESC | VARCHAR2(1000) | N |  |
| PCR_SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_POPULATION_CANCER_REGISTRY_01`: PCR_ID
- **Triggers**: `POPULATION_CANCER_REGISTRY_DEL` (after delete), `POPULATION_CANCER_REGISTRY_INS` (before insert), `POPULATION_CANCER_REGISTRY_UPD` (before update), `POPULATION_CR_INSERT` (before insert)

## DEFINITIONS.POPULATION_CR_STATES

| Column | Type | Null | Comment |
|---|---|---|---|
| PCRS_ID | NUMBER(3) | N |  |
| PCR_ID | NUMBER(3) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| PCRS_STATE_NAME | VARCHAR2(100) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| CENTRE_ID | VARCHAR2(8) | N |  |

- **PK** `PK_POPULATION_CR_STATES_01`: PCRS_ID
- **FK** `FK_PCRS`: (COUNTRY_ID, STATE_ID) -> DEFINITIONS.STATE(COUNTRY_ID, STATE_ID) [disabled]
- **Triggers**: `POPULATION_CR_STATES_DEL` (after delete), `POPULATION_CR_STATES_INS` (before insert), `POPULATION_CR_STATES_INSERT` (before insert), `POPULATION_CR_STATES_UPD` (before update)

## DEFINITIONS.POPUP_ALERTS_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_TYPE_ID | NUMBER(4) | N |  |
| TYPE_DESC | VARCHAR2(100) | N |  |
| TYPE_CATEGORY | VARCHAR2(50) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | Y |  |

- **PK** `POPUP_ALERTS_TYPE_PK`: ALERT_TYPE_ID
- **Triggers**: `POPUP_ALERTS_TYPE_CEA` (before insert or update or delete), `POPUP_ALERTS_TYPE_DEL` (after delete), `POPUP_ALERTS_TYPE_INS` (before insert), `POPUP_ALERTS_TYPE_UPD` (before update), `TRG_WS_FXX_UX_NW_Q` (after insert or update or delete)

## DEFINITIONS.POS_RESPONSE_MESSAGE

| Column | Type | Null | Comment |
|---|---|---|---|
| RESPONSE_DATE | DATE | Y |  |
| RESPONSE_TIME | DATE | Y |  |
| RESPONSE_TID | NUMBER | Y |  |
| RESPONSE_MID | NUMBER | Y |  |
| RESPONSE_BATCH_NO | NUMBER | Y |  |
| INVOICE_NO | VARCHAR2(20) | Y |  |
| CARD_NO | VARCHAR2(50) | Y |  |
| CARD_ENTRY | VARCHAR2(20) | Y |  |
| CARD_HOLDER_NAME | VARCHAR2(50) | Y |  |
| TIP_AMOUNT | NUMBER(12,2) | Y |  |
| TXN_AMOUNT | NUMBER(12,2) | Y |  |
| RESPONSE_CODE | NUMBER | Y |  |
| RRN_NO | NUMBER | Y |  |
| AUTH_CODE | NUMBER | Y |  |
| AID | VARCHAR2(50) | Y |  |
| TC | VARCHAR2(50) | Y |  |
| CARD_BRAND | VARCHAR2(20) | Y |  |
| VERIFIED_BY | VARCHAR2(20) | Y |  |
| VERSION | VARCHAR2(10) | Y |  |
| RESERVE1 | VARCHAR2(100) | Y |  |
| RESERVE2 | VARCHAR2(100) | Y |  |
| PATIENT_INV_NO | VARCHAR2(14) | Y |  |
| RESPONSE | VARCHAR2(50) | Y |  |
| DISCOUNT_NAME | VARCHAR2(50) | Y |  |
| DISCOUNT_VALUE | VARCHAR2(50) | Y |  |
| DISCOUNT_AMOUNT | NUMBER(12,2) | Y |  |
| FBR_POS_FEE | NUMBER(12,2) | Y |  |
| TO_BE_PAID | NUMBER(12,2) | Y |  |
| TAX_AMOUNT | NUMBER(12,2) | Y |  |
| BILL_AMOUNT | NUMBER(12,2) | Y |  |
| IS_SERVICE_CHARGES | VARCHAR2(50) | Y |  |
| SERVICE_CHARGE | VARCHAR2(50) | Y |  |
| SERVICE_CHARGE_AMOUNT | NUMBER(12,2) | Y |  |
| PRODUCT_NAME | VARCHAR2(50) | Y |  |

_No standard audit columns._


## DEFINITIONS.PREFERENCES

| Column | Type | Null | Comment |
|---|---|---|---|
| PREFERENCE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| VERSION | VARCHAR2(6) default '11g' | Y |  |
| APPLICATION_ID | NUMBER(3) | Y |  |

- **PK** `PK_PREFERENCES`: PREFERENCE_ID
- **UK** `UK_PREFERENCES_1`: DESCRIPTION
- **FK** `FK_PREFERENCES_1`: (APPLICATION_ID) -> DEFINITIONS.APPLICATION_SETUP(APPLICATION_ID) [disabled]
- **CHECK** `CHK_PREFERENCES_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `PREFERENCES_DEL` (after delete), `PREFERENCES_INS` (before insert), `PREFERENCES_UPD` (before update)

## DEFINITIONS.PREFERENCE_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| PREFERENCE_ID | NUMBER | N |  |
| VALUE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(1000) | Y |  |
| VALUE | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| DEFAULT_VALUE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PREFERENCE_VALUES`: PREFERENCE_ID, VALUE_ID
- **FK** `FK_PREFERENCE_VALUES_1`: (PREFERENCE_ID) -> DEFINITIONS.PREFERENCES(PREFERENCE_ID)
- **CHECK** `CHK_PK_PREFERENCE_VALUES_1`: ACTIVE IN ('Y', 'N'
- **Triggers**: `PREFERENCE_VALUES_DEL` (after delete), `PREFERENCE_VALUES_INS` (before insert), `PREFERENCE_VALUES_UPD` (before update)

## DEFINITIONS.PREGNANCY_RISK_FACTORS

| Column | Type | Null | Comment |
|---|---|---|---|
| PREGNANCY_RISK_FACTOR_ID | VARCHAR2(2) | N |  |
| SHORT_DESC | CHAR(1) | Y |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| SCORE | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PREGNANCY_RISK_FACTORS`: PREGNANCY_RISK_FACTOR_ID
- **UK** `UK_PREGNANCY_RISK_FACTORS`: SHORT_DESC
- **Triggers**: `PREGNANCY_RISK_FACTORS_CEA` (before insert or update or delete), `PREGNANCY_RISK_FACTORS_DEL` (after delete), `PREGNANCY_RISK_FACTORS_INS` (before insert), `PREGNANCY_RISK_FACTORS_UPD` (before update), `TRG_WS_SUY_IT_SU_Q` (after insert or update or delete)

## DEFINITIONS.PREGNANCY_RULED_OUT

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_PREGNANCY_RULED_OUT`: SERIAL_NO

## DEFINITIONS.PRESCRIPTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PT_ID | NUMBER | N |  |
| SHORT_DESCRIPTION | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| COMPLEX_DOSING | VARCHAR2(1) default 'N' | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| ADV_PRESCRIPTION_ALLOWED_DAYS | NUMBER(6,3) | Y |  |

- **PK** `PK_PRESCRIPTION_TYPE`: PT_ID, SHORT_DESCRIPTION
- **Triggers**: `PRESCRIPTION_TYPE_DEL` (after delete), `PRESCRIPTION_TYPE_INS` (before insert), `PRESCRIPTION_TYPE_UPD` (before update)

## DEFINITIONS.PRESENTATION_TYPE_R

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(1) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **Triggers**: `PRESENTATION_TYPE_R_CEA` (before insert or update or delete), `TRG_WS_ZAP_RV_SC_Q` (after insert or update or delete)

## DEFINITIONS.PRESENTING_COMPLAINTS

| Column | Type | Null | Comment |
|---|---|---|---|
| PRESENTING_COMPLAINTS_ID | VARCHAR2(5) | N |  |
| PRESENTING_COMPLAINTS | VARCHAR2(2000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.PREVIOUS_HOSPITALIZATION

| Column | Type | Null | Comment |
|---|---|---|---|
| HOSPITALIZATION_HISTORY_ID | VARCHAR2(5) | N |  |
| HOSPITALIZATION_HISTORY | VARCHAR2(2000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **Triggers**: `PREVIOUS_HOSPITALIZATION_CEA` (before insert or update or delete), `TRG_WS_GIK_HZ_AW_Q` (after insert or update or delete)

## DEFINITIONS.PREVIOUS_TREATMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| ACTIVE | VARCHAR2(1) | N |  |
| PREVIOUS_TREATMENT_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_PREVIOUS_TREATMENT`: PREVIOUS_TREATMENT_ID
- **Triggers**: `PREVIOUS_TREATMENT_CEA` (before insert or update or delete), `TRG_WS_ZZB_UT_PM_Q` (after insert or update or delete)

## DEFINITIONS.PREVIOUS_TREATMENT_BUP

| Column | Type | Null | Comment |
|---|---|---|---|
| ACTIVE | VARCHAR2(1) | N |  |
| PREVIOUS_TREATMENT_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |


## DEFINITIONS.PRE_PROC_ASSESSMENT_CPT_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_ID | NUMBER | N |  |
| SR_NO | NUMBER | N |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| TEMPLATE_ID | VARCHAR2(6) | Y |  |
| VALIDITY_DAYS | NUMBER | Y |  |
| REFERENCE_TABLE | VARCHAR2(500) | Y |  |
| REFERENCE_COLUMN | VARCHAR2(500) | Y |  |
| REFERENCE_WHERE | VARCHAR2(500) | Y |  |
| ASSESSMENT_TYPE | VARCHAR2(50) | Y |  |
| MANDATORY | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_PRE_PROCEDURE_SETUP`: SETUP_ID, SR_NO
- **Triggers**: `PRE_PROC_CPT_INSERT` (before insert), `PRE_P_ASS_CPT_SETUP_DEL` (after delete), `PRE_P_ASS_CPT_SETUP_INS` (before insert), `PRE_P_ASS_CPT_SETUP_UPD` (before update)

## DEFINITIONS.PRIORITY
This table contains information of priority definitons to perform/teart orderequest on priority basis

| Column | Type | Null | Comment |
|---|---|---|---|
| PRIORITY_ID | CHAR(1) | N | This column contains unique Priority ID |
| PRIORITY_DESC | VARCHAR2(30) | N | This column contains Priority full description |
| SHORT_DESC | VARCHAR2(5) | N | This column contains Priority short description |
| SHOW_SIGN | CHAR(1) default 'N' | N | Flag information, Y=Show warning sign in order queue for priority/urgancy, N=Routine |
| BY_DEFAULT | CHAR(1) default 'N' | N | Flag information, Y=Default priority if nothing mentioned by user, |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **PK** `PK_PRIORITY`: PRIORITY_ID
- **CHECK** `CK_PRIORITY_1`: PRIORITY_ID BETWEEN '0' AND '9'
- **CHECK** `CK_PRIORITY_2`: SHOW_SIGN IN ('Y','N'
- **CHECK** `CK_PRIORITY_3`: BY_DEFAULT IN ('Y','N'
- **Triggers**: `PRIORITY_CEA` (before insert or update or delete), `TRG_WS_WLR_DF_UB_Q` (after insert or update or delete)

## DEFINITIONS.PROBLEM_HLP_OBJECT

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| PRO_SRNO | NUMBER(3) | N |  |
| HLP_OBJECT_CODE | VARCHAR2(11) | N |  |
| COMMENTS | VARCHAR2(2000) | Y |  |

- **PK** `PK_PROBLEM_HLP_OBJECT`: OBJECT_CODE, ACT_SRNO, PRO_SRNO, HLP_OBJECT_CODE
- **FK** `FK_PROBLEM_HLP_OBJECT_1`: (OBJECT_CODE, ACT_SRNO, PRO_SRNO) -> DEFINITIONS.ACTION_PROBLEM(OBJECT_CODE, ACT_SRNO, PRO_SRNO)
- **FK** `FK_PROBLEM_HLP_OBJECT_2`: (OBJECT_CODE) -> DEFINITIONS.OBJECTS(OBJECT_CODE)
- **Triggers**: `PROBLEM_HLP_OBJECT_DEL` (after delete), `PROBLEM_HLP_OBJECT_INS` (before insert), `PROBLEM_HLP_OBJECT_UPD` (before update)

## DEFINITIONS.PROBLEM_SOLUTION

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| PRO_SRNO | NUMBER(3) | N |  |
| SOL_SRNO | NUMBER(3) | N |  |
| SOLUTION | VARCHAR2(2000) | Y |  |

- **PK** `PK_PROBLEM_SOLUTION`: OBJECT_CODE, ACT_SRNO, PRO_SRNO, SOL_SRNO
- **FK** `FK_PROBLEM_SOLUTION_1`: (OBJECT_CODE, ACT_SRNO, PRO_SRNO) -> DEFINITIONS.ACTION_PROBLEM(OBJECT_CODE, ACT_SRNO, PRO_SRNO)
- **Triggers**: `PROBLEM_SOLUTION_DEL` (after delete), `PROBLEM_SOLUTION_INS` (before insert), `PROBLEM_SOLUTION_UPD` (before update)

## DEFINITIONS.PROBLEM_SUGGESTION

| Column | Type | Null | Comment |
|---|---|---|---|
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACT_SRNO | NUMBER(3) | N |  |
| PRO_SRNO | NUMBER(3) | N |  |
| SUG_SRNO | NUMBER(3) | N |  |
| SUGGESTION | VARCHAR2(2000) | Y |  |
| FORWARD_DATE | DATE | Y |  |
| FORWARD_TO | VARCHAR2(14) | Y |  |
| COMPLETION_DATE | DATE | Y |  |
| COMPLETION_BY | VARCHAR2(14) | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |

- **PK** `PK_PROBLEM_SUGGESTION`: OBJECT_CODE, ACT_SRNO, PRO_SRNO, SUG_SRNO
- **FK** `FK_PROBLEM_SUGGESTION_1`: (OBJECT_CODE, ACT_SRNO, PRO_SRNO) -> DEFINITIONS.ACTION_PROBLEM(OBJECT_CODE, ACT_SRNO, PRO_SRNO)
- **Triggers**: `PROBLEM_SUGGESTION_DEL` (after delete), `PROBLEM_SUGGESTION_INS` (before insert), `PROBLEM_SUGGESTION_UPD` (before update)

## DEFINITIONS.PROBLEM_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PROBLEM_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |

- **PK** `PK_PROBLEM_TYPE_ID`: PROBLEM_TYPE_ID
- **UK** `UK_DESCRIPTION`: DESCRIPTION
- **Triggers**: `PROBLEM_TYPE_DEL` (after delete), `PROBLEM_TYPE_INS` (before insert), `PROBLEM_TYPE_UPD` (before update)

## DEFINITIONS.PROCEDURE_CHECKLIST

| Column | Type | Null | Comment |
|---|---|---|---|
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | N |  |
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| EVENT_ID | NUMBER(3) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| DEFAULT_TEMPLATE | CHAR(1) | Y |  |

- **PK** `PK_PROCEDURE_CHECKLIST`: CLINIC_SPECIALITY_ID, TEMPLATE_ID, EVENT_ID
- **FK** `FK_PROCEDURE_CHECKLIST_1`: (CLINIC_SPECIALITY_ID) -> DEFINITIONS.CLINIC_SPECIALITY(CLINIC_SPECIALITY_ID)
- **FK** `FK_PROCEDURE_CHECKLIST_3`: (EVENT_ID) -> DEFINITIONS.EVENT(EVENT_ID) [disabled]

## DEFINITIONS.PROCEDURE_SETUP_DTL_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | Y |  |
| SETUP_ID | NUMBER | N |  |
| SR_NO | NUMBER | N |  |

- **PK** `PK_PROCEDURE_SETUP_DTL`: SETUP_ID, SR_NO, LOC_ID
- **Triggers**: `PROC_SETUP_DTL_LOCATION_DEL` (after delete), `PROC_SETUP_DTL_LOCATION_INS` (before insert), `PROC_SETUP_DTL_LOCATION_UPD` (before update)

## DEFINITIONS.PROFICIENCY_LEVEL

| Column | Type | Null | Comment |
|---|---|---|---|
| PROFICIENCY_LEVEL_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PROFICIENCY_LEVEL`: PROFICIENCY_LEVEL_ID
- **Triggers**: `PROFICIENCY_LEVEL_CEA` (before insert or update or delete), `PROFICIENCY_LEVEL_DEL` (after delete), `PROFICIENCY_LEVEL_INS` (before insert), `PROFICIENCY_LEVEL_UPD` (before update), `TRG_WS_ZHO_QN_HD_Q` (after insert or update or delete)

## DEFINITIONS.PROPERTY_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PROPERTY_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_PROPERTY_TYPE`: PROPERTY_TYPE_ID
- **Triggers**: `PROPERTY_TYPE_CEA` (before insert or update or delete), `PROPERTY_TYPE_DEL` (after delete), `PROPERTY_TYPE_INS` (before insert), `PROPERTY_TYPE_UPD` (before update), `TRG_WS_IHH_MU_UX_Q` (after insert or update or delete)

## DEFINITIONS.PROTOCOL_GUIDELINES_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | N |  |
| PROTOCOL_STATUS | CHAR(1) | Y |  |
| ENTERED_BY | VARCHAR2(14) | Y |  |
| ENTERED_DATE | DATE | N |  |
| DOC_TYPE_ID | VARCHAR2(5) | Y |  |
| PROTOCOL_DESC | VARCHAR2(200) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_PROTOCOL_GUIDELINES_HISTORY`: MRNO, ENTERED_DATE
- **Triggers**: `TRG_WS_WIJ_ZM_EW_Q` (after insert or update or delete)

## DEFINITIONS.WORK_FLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| WORK_FLOW_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| FROM_AMOUNT | NUMBER(15,4) | Y |  |
| TO_AMOUNT | NUMBER(15,4) | Y |  |
| BUDGETED | CHAR(1) | Y |  |
| BGT_WORK_FLOW_ID | NUMBER(4) | Y |  |
| APPROVAL_PATH | VARCHAR2(500) | Y |  |
| MEDICAL_ITEM | CHAR(1) default 'N' | Y |  |
| LC_WORK_FLOW | CHAR(1) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| SEND_EMAIL | CHAR(1) default 'N' | Y | This column contains flag to use email solution for specific work flow |
| WORK_FLOW_TYPE | VARCHAR2(3) | Y |  |

- **PK** `PK_WORK_FLOW`: WORK_FLOW_ID
- **UK** `UN_WORK_FLOW`: LC_WORK_FLOW
- **FK** `FK_WORK_FLOW`: (ORGANIZATION_ID) -> DEFINITIONS.ORGANIZATION(ORGANIZATION_ID) [disabled]
- **FK** `FK_WORK_FLOW_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **FK** `FK_WORK_FLOW_2`: (ZONE_ID) -> DEFINITIONS.ZONES(ZONE_ID) [disabled]
- **CHECK** `CK_BUDGETED`: BUDGETED IN ('N','Y'
- **CHECK** `CK_MEDICAL_ITEM`: MEDICAL_ITEM IN ('N','Y'
- **Triggers**: `TRG_WS_LAH_YM_MZ_Q` (after insert or update or delete), `WORK_FLOW_CEA` (before insert or update or delete), `WORK_FLOW_DEL` (after delete), `WORK_FLOW_INS` (before insert), `WORK_FLOW_UPD` (before update)

## DEFINITIONS.PR_TYPE_FLOW

| Column | Type | Null | Comment |
|---|---|---|---|
| PURCHASE_TYPE_ID | NUMBER | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| SCHEMA_ID | VARCHAR2(3) | N | Used as HIS Module ID |
| PARENT_WORKFLOW_ID | NUMBER(4) | Y |  |
| RESTRICTION_TYPE | VARCHAR2(2) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| SHORT_DESC | VARCHAR2(5) | Y |  |

- **PK** `PK_PR_TYPE_FLOW`: PURCHASE_TYPE_ID, WORK_FLOW_ID, SCHEMA_ID
- **FK** `FK_PR_TYPE_FLOW_1`: (WORK_FLOW_ID) -> DEFINITIONS.WORK_FLOW(WORK_FLOW_ID) [disabled]
- **Triggers**: `PR_TYPE_FLOW_DEL` (after delete), `PR_TYPE_FLOW_INS` (before insert), `PR_TYPE_FLOW_UPD` (before update)

## DEFINITIONS.PR_TYPE_FLOW_EVENT

| Column | Type | Null | Comment |
|---|---|---|---|
| PURCHASE_TYPE_ID | NUMBER | N |  |
| WORK_FLOW_ID | NUMBER(4) | N |  |
| EMAIL | CHAR(1) | Y |  |
| EVENT_ID | NUMBER(3) | N |  |
| ORDER_BY | NUMBER(3) | Y |  |
| DURATION_IMPORT | NUMBER(3) | Y |  |
| DURATION_LOCAL | NUMBER(3) | Y |  |
| REMINDER_TO | VARCHAR2(14) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | N | HIS MODULE_ID |
| AUTO_PERFORM | CHAR(1) | Y | IF 'Y' THEN EVENT WILL BE SKIP  AND IF 'N' THEN EVEN WILL BE PERFORM ACCORDING TO CURRENT FLOW |
| QUEUE_REQ | CHAR(1) | Y |  |
| REMINDER_DAYS | NUMBER | Y | This column is used to save no of days for first reminder |
| NEXT_REMINDER_DAYS | NUMBER | Y | This column is used to save no of days for second reminder |
| REMINDER_FREQUENCY | NUMBER | Y | This column is used to save alert frequency, how many time alert will be generate |

- **PK** `PK_PR_TYPE_FLOW_EVENT`: PURCHASE_TYPE_ID, WORK_FLOW_ID, EVENT_ID, SCHEMA_ID
- **FK** `FK_PR_TYPE_FLOW_EVENT_2`: (EVENT_ID) -> DEFINITIONS.EVENT(EVENT_ID) [disabled]
- **Triggers**: `PR_TYPE_FLOW_EVENT_CEA` (before insert or update or delete), `PR_TYPE_FLOW_EVENT_DEL` (after delete), `PR_TYPE_FLOW_EVENT_INS` (before insert), `PR_TYPE_FLOW_EVENT_UPD` (before update), `TRG_WS_IGY_GO_RQ_Q` (after insert or update or delete)

## DEFINITIONS.QUALIFICATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| QUALIFICATION_ID | VARCHAR2(6) | N |  |
| QUALIFICATION_TYPE_ID | VARCHAR2(6) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_QUALIFICATIONS`: QUALIFICATION_ID
- **Triggers**: `QUALIFICATIONS_CEA` (before insert or update or delete), `QUALIFICATIONS_DEL` (after delete), `QUALIFICATIONS_INS` (before insert), `QUALIFICATIONS_UPD` (before update), `TRG_WS_DJZ_QK_GD_Q` (after insert or update or delete)

## DEFINITIONS.QUALIFICATION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| QUALIFICATION_TYPE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_QUALIFICATION_TYPE`: QUALIFICATION_TYPE_ID
- **Triggers**: `QUALIFICATION_TYPE_CEA` (before insert or update or delete), `QUALIFICATION_TYPE_DEL` (after delete), `QUALIFICATION_TYPE_INS` (before insert), `QUALIFICATION_TYPE_UPD` (before update), `TRG_WS_ZXD_EW_TN_Q` (after insert or update or delete)

## DEFINITIONS.QUESTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| QUESTION_ID | VARCHAR2(9) | N |  |
| QUESTION_DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_QUESTION`: QUESTION_ID
- **Triggers**: `QUESTIONS_DEL` (after delete), `QUESTIONS_INS` (before insert), `QUESTIONS_UPD` (before update)

## DEFINITIONS.QUEUE_TYPES
This table contains information of differnt queues types

| Column | Type | Null | Comment |
|---|---|---|---|
| QUEUE_TYPE_ID | VARCHAR2(4) | N | Unique identifier of queue type |
| QUEUE_DESC | VARCHAR2(60) | N | This column contains description/Label of queue type |
| REMARKS | VARCHAR2(100) | Y | This column contains open text remarks/other information about quetype |
| ACTIVE | CHAR(1) default 'Y' | N | Thic column contains Flag Information for Active status of queue type Y=ACTIVE,N=INACTIVE |
| AUTO_DEL | CHAR(1) default 'N' | N | Thic column contains Flag Information for Auto Deletion of record wrt retain limit defined, Y=Auto Delete is ON, N=Off |
| RETAIN_LIMIT_TYPE | CHAR(1) default 'X' | N | Thic column contains Retain Unit Type X=Not Applicable, D=Days, H=Hours, M=Minutes, (Applicable for Auto Delete =Yes) |
| RETAIN_LIMIT | NUMBER(5) | Y | Thic column contains Expiry of Limit wrt retain Unit Type (Applicable for Auto Delete =Yes) |

- **PK** `PK_QUEUE_TYPES`: QUEUE_TYPE_ID
- **CHECK** `CK_QUEUE_TYPES_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_QUEUE_TYPES_2`: AUTO_DEL IN ('Y','N'
- **CHECK** `CK_QUEUE_TYPES_3`: RETAIN_LIMIT_TYPE IN ('X','D','H','M'

## DEFINITIONS.RACKS

| Column | Type | Null | Comment |
|---|---|---|---|
| RACK_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| RACK_CATEGORY_ID | NUMBER(5) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RACK_SIZE | VARCHAR2(15) | Y |  |
| RACK_AREA | VARCHAR2(25) | Y |  |
| ROOM_ID | VARCHAR2(7) | N |  |

- **PK** `PK_RACKS_RACK_ID`: RACK_ID, ROOM_ID
- **UK** `UK_RACK_DESC`: DESCRIPTION, ROOM_ID
- **FK** `FK_ROOMS_ROOM_ID`: (ROOM_ID) -> DEFINITIONS.ROOMS(ROOM_ID)
- **Triggers**: `RACKS_DEL` (after delete), `RACKS_INS` (before insert), `RACKS_UPD` (before update)

## DEFINITIONS.RACK_LEVEL

| Column | Type | Null | Comment |
|---|---|---|---|
| RACK_LEVEL_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| LEVEL_CATEGORY_ID | NUMBER(5) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RACK_ID | NUMBER(5) | N |  |
| ROOM_ID | VARCHAR2(7) | N |  |

- **PK** `PK_RACK_LEVEL_LEVEL_ID`: RACK_LEVEL_ID, RACK_ID, ROOM_ID
- **Triggers**: `RACK_LEVEL_DEL` (after delete), `RACK_LEVEL_INS` (before insert), `RACK_LEVEL_UPD` (before update)

## DEFINITIONS.RACK_LEVEL_PARTITIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| PARTITION_ID | NUMBER(5) | N |  |
| DESCRIPTION | VARCHAR2(255) | N |  |
| PARTITION_CATEGORY_ID | NUMBER(5) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| RACK_LEVEL_ID | NUMBER(5) | N |  |
| ROOM_ID | VARCHAR2(7) | N |  |
| RACK_ID | NUMBER(5) | N |  |

- **PK** `PK_PARTATION_ID`: PARTITION_ID, ROOM_ID, RACK_LEVEL_ID, RACK_ID
- **Triggers**: `RACK_LEVEL_PARTITIONS_DEL` (after delete), `RACK_LEVEL_PARTITIONS_INS` (before insert), `RACK_LEVEL_PARTITIONS_UPD` (before update)

## DEFINITIONS.RADIATION_ENERGY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| ENERGY | VARCHAR2(10) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CLINIC_ID | VARCHAR2(7) | Y |  |

- **FK** `FK_RADIATION_ENERGY`: (CLINIC_ID) -> REGISTRATION.CLINIC(CLINIC_ID) [disabled]

## DEFINITIONS.RADIOLOGY_EVENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| EVENT_TYPE_ID | VARCHAR2(3) | N |  |
| EVENT_DESCRIPTION | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| EVENT_NAME | VARCHAR2(60) | N |  |

- **PK** `PK_RADIOLOGY_EVENTS`: EVENT_TYPE_ID
- **UK** `UK_RADIOLOGY_EVENTS_01`: EVENT_NAME
- **CHECK** `CHK_RADIOLOGY_EVENTS_01`: ACTIVE IN ('N','Y'
- **Triggers**: `RADIOLOGY_EVENTS_CEA` (before insert or update or delete), `RADIOLOGY_EVENTS_DEL` (after delete), `RADIOLOGY_EVENTS_INS` (before insert), `RADIOLOGY_EVENTS_UPD` (before update), `TRG_WS_QKB_ZJ_XM_Q` (after insert or update or delete)

## DEFINITIONS.RADIOLOGY_IMAGE_GUIDELINE

| Column | Type | Null | Comment |
|---|---|---|---|
| GUIDELINE_ID | VARCHAR2(5) | N |  |
| DISEASE | VARCHAR2(500) | Y |  |
| AREA_TO_BE_EXAM | VARCHAR2(500) | Y |  |
| LOCALISATION | VARCHAR2(500) | Y |  |
| STAGING | VARCHAR2(500) | Y |  |
| PLANNING | VARCHAR2(500) | Y |  |
| SPECIAL_ISSUES | VARCHAR2(500) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |

- **PK** `PK_RADIOLOGY_IMAGE_GUIDELINE`: GUIDELINE_ID
- **UK** `UK_RADIOLOGY_IMAGE_GUIDELINE`: DISEASE
- **Triggers**: `RADIOLOGY_IMAGE_GUIDELINE_CEA` (before insert or update or delete), `TRG_WS_ZVV_PJ_IT_Q` (after insert or update or delete)

## DEFINITIONS.RADIOLOGY_VIEW

| Column | Type | Null | Comment |
|---|---|---|---|
| VIEW_ID | NUMBER | N |  |
| VIEW_DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `RADIOLOGY_VIEW_PK`: VIEW_ID

## DEFINITIONS.RAMZAN_DATES

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |

- **PK** `PK_RAMZAN_DATE`: START_DATE, END_DATE
- **UK** `UK_RAMZAN_DATES`: START_DATE
- **Triggers**: `RAMZAN_DATES_CEA` (before insert or update or delete), `RAMZAN_DATES_DEL` (after delete), `RAMZAN_DATES_INS` (before insert), `RAMZAN_DATES_UPD` (before update), `TRG_WS_VRJ_UE_HV_Q` (after insert or update or delete)

## DEFINITIONS.RANKS_PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| RANK_ID | VARCHAR2(6) | N |  |

- **PK** `PK_RANKS_PATIENT_TYPE`: PATIENT_TYPE_ID, RANK_ID
- **FK** `FK_RANKS_PATIENT_TYPE_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **FK** `FK_RANKS_PATIENT_TYPE_2`: (RANK_ID) -> DEFINITIONS.ARMY_RANKS(RANK_ID)

## DEFINITIONS.RANK_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| RANK_CAT_ID | VARCHAR2(6) | N |  |
| RANK_CAT_DESC | VARCHAR2(200) | N |  |
| SHORT_DESC | VARCHAR2(50) | N |  |
| RANK_TYPE_ID | NUMBER(3) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| FORCE_TYPE_ID | VARCHAR2(6) | N |  |

- **PK** `PK_RANK_CATEGORY`: RANK_CAT_ID
- **CHECK** `CHK_RANK_CATEGORY`: ACTIVE IN ('N','Y'

## DEFINITIONS.RANK_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| RANK_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SHORT_DESC | VARCHAR2(50) | Y |  |

- **PK** `RANK_TYPE_PK`: RANK_TYPE_ID

## DEFINITIONS.REASON_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_TYPE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| T_GROUP_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_REASON_TYPE`: REASON_TYPE_ID
- **Triggers**: `REASON_TYPE_CEA` (before insert or update or delete), `REASON_TYPE_DEL` (after delete), `REASON_TYPE_INS` (before insert), `REASON_TYPE_UPD` (before update), `TRG_WS_TKH_ME_KP_Q` (after insert or update or delete)

## DEFINITIONS.REASON

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | NUMBER(3) | N |  |
| REASON_TYPE_ID | NUMBER(3) | Y |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACCEPTED_REJECTED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_REASON`: REASON_ID
- **FK** `FK_REASON_1`: (REASON_TYPE_ID) -> DEFINITIONS.REASON_TYPE(REASON_TYPE_ID) [disabled]
- **Triggers**: `REASON_CEA` (before insert or update or delete), `REASON_DEL` (after delete), `REASON_INS` (before insert), `REASON_UPD` (before update), `TRG_WS_VFH_GC_HW_Q` (after insert or update or delete)

## DEFINITIONS.REASON_FOR_ADMISSION

| Column | Type | Null | Comment |
|---|---|---|---|
| ADMISSION_REASON_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_REASON_FOR_ADMISSION`: ADMISSION_REASON_ID
- **UK** `UK_REASON_FOR_ADMISSION`: DESCRIPTION
- **Triggers**: `REASON_FOR_ADMISSION_CEA` (before insert or update or delete), `REASON_FOR_ADMISSION_DEL` (after delete), `REASON_FOR_ADMISSION_INS` (before insert), `REASON_FOR_ADMISSION_UPD` (before update), `TRG_WS_RSZ_ZV_VV_Q` (after insert or update or delete)

## DEFINITIONS.REFERENCE

| Column | Type | Null | Comment |
|---|---|---|---|
| REFERENCE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| REFERENCE_TYPE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_REFERENCE`: REFERENCE_ID
- **CHECK** `CK_REFERENCE_1`: REFERENCE_TYPE IN ('I','O','B'
- **CHECK** `CK_REFERENCE_2`: ACTIVE IN ('Y','N'
- **Triggers**: `REFERENCE_INS` (before insert)

## DEFINITIONS.UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| UNIT_ID | VARCHAR2(5) | N |  |
| UNIT_TYPE | VARCHAR2(2) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(11) | Y |  |
| UNIT_VALUE | NUMBER(8,4) | Y |  |
| FLUIDS_UNIT | VARCHAR2(1) default 'N' | Y |  |
| COMPLEX_DOSING | VARCHAR2(1) default 'N' | Y |  |
| UNIT_FACTOR | NUMBER(9) | Y |  |
| BASIC_UNIT_ID | VARCHAR2(5) | Y |  |
| TITRATION_UNIT | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_UNIT`: UNIT_ID
- **FK** `FK_BASIC_UNIT`: (BASIC_UNIT_ID) -> DEFINITIONS.BASIC_UNIT(BASIC_UNIT_ID)
- **Triggers**: `TRG_WS_WGM_WP_HT_Q` (after insert or update or delete), `UNIT_CEA` (before insert or update or delete), `UNIT_DEL` (after delete), `UNIT_INS` (before insert), `UNIT_TS` (before insert or update or delete), `UNIT_UPD` (before update)

## DEFINITIONS.REFILL_UNIT

| Column | Type | Null | Comment |
|---|---|---|---|
| REFILL_UNIT_ID | VARCHAR2(5) | N |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| DURATION | NUMBER(8) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_REFILL_UNIT`: REFILL_UNIT_ID
- **FK** `FK_REFILL_UNIT`: (UNIT_ID) -> DEFINITIONS.UNIT(UNIT_ID) [disabled]

## DEFINITIONS.REGION_DISTRICTS

| Column | Type | Null | Comment |
|---|---|---|---|
| REGION_ID | VARCHAR2(4) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| REMARKS | VARCHAR2(256) | Y |  |

- **PK** `PK_REGION_DISTRICT`: REGION_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID
- **UK** `UNIQUE_DISTRICT_CONSTRAINT`: COUNTRY_ID, STATE_ID, DISTRICT_ID, ACTIVE
- **FK** `FK_REGION_DISTRICT`: (REGION_ID) -> DEFINITIONS.REGION(REGION_ID)

## DEFINITIONS.REGION_WISE_HOSPITAL

| Column | Type | Null | Comment |
|---|---|---|---|
| REGION_ID | VARCHAR2(4) | N |  |
| DISPENSARY_ID | VARCHAR2(6) | N |  |
| HOSPITAL_TYPE | VARCHAR2(1) | N | D for dispensary H for hospital |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_REGION_WISE_HOSPITAL`: REGION_ID, DISPENSARY_ID, HOSPITAL_TYPE
- **Triggers**: `REGION_WISE_HOSPITAL_DEL` (after delete), `REGION_WISE_HOSPITAL_INS` (before insert), `REGION_WISE_HOSPITAL_UPD` (before update)

## DEFINITIONS.REJECT_REASONS

| Column | Type | Null | Comment |
|---|---|---|---|
| REJECT_REASON_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(120) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| FLAG | VARCHAR2(1) | Y |  |

- **PK** `PK_REJECT_REASONS`: REJECT_REASON_ID
- **Triggers**: `REJECT_REASONS_DEL` (after delete), `REJECT_REASONS_INS` (before insert), `REJECT_REASONS_UPD` (before update)

## DEFINITIONS.RELATION
This table contains definitions of relations of persons (System Constant Level table)

| Column | Type | Null | Comment |
|---|---|---|---|
| RELATION_ID | VARCHAR2(6) | N | Unique Primary Key Relation ID |
| DESCRIPTION | VARCHAR2(60) | N | This column contains Name/Description of relation |
| DEFAULTS | VARCHAR2(1) | N | This column contains flag of Default to choice relation by choice during  registration |
| ACTIVE | VARCHAR2(1) | N | This column contains flag of Active, Inactive state (Y=Active, N=Inactive) |
| SHORT_DESC | VARCHAR2(10) | Y | This column contains Short description/Abbriviations of Relation (e.g. S/O=Son of, W/O=Wife of) |
| FOR_QA_CONSENTS | CHAR(1) default 'N' | N |  |
| EMP_DEPENDANT | CHAR(1) default 'N' | N | This column contains flag eaither this relation is of dependant (Y=Dependant, N=Not dependant) |
| RELATION_CAT_ID | VARCHAR2(3) | Y |  |
| CHECK_AGE_FOR_MEDICAL | CHAR(1) default 'N' | Y | This flag will check if age limit required to check or not |
| AGE_LIMIT | NUMBER | Y | This column will store age limit for medical |
| RELATION_CATEGORY_ID | VARCHAR2(3) | Y | This column contains Relation Category Id Ref. DEFINITIONS.RELATION_CATEGORY |

- **PK** `PK_RELATION`: RELATION_ID
- **CHECK** `CK_RELATION_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_RELATION_2`: DEFAULTS IN ('Y','N'
- **CHECK** `CK_RELATION_3`: EMP_DEPENDANT IN ('N','Y'
- **CHECK** `CK_RELATION_4`: FOR_QA_CONSENTS IN ('N','Y'
- **Triggers**: `RELATION_CEA` (before insert or update or delete), `RELATION_DEL` (after delete), `RELATION_INS` (before insert), `RELATION_TS` (before insert or update or delete), `RELATION_UPD` (before update), `TRG_WS_IED_GD_KW_Q` (after insert or update or delete)

## DEFINITIONS.RELATIONSHIP_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_RELATIONSHIP_CATEGORY`: ID
- **Triggers**: `RELATIONSHIP_CATEGORY_CEA` (before insert or update or delete), `RELATIONSHIP_CATEGORY_DEL` (after delete), `RELATIONSHIP_CATEGORY_INS` (before insert), `RELATIONSHIP_CATEGORY_UPD` (before update), `TRG_WS_UJY_WG_NK_Q` (after insert or update or delete)

## DEFINITIONS.RELATION_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| RELATION_CATEGORY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_RELATION_CATEGORY`: RELATION_CATEGORY_ID
- **Triggers**: `RELATION_CATEGORY_INS` (before insert)

## DEFINITIONS.RELIGION

| Column | Type | Null | Comment |
|---|---|---|---|
| RELIGION_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_RELIGION`: RELIGION_ID
- **Triggers**: `RELIGION_CEA` (before insert or update or delete), `RELIGION_DEL` (after delete), `RELIGION_INS` (before insert), `RELIGION_TS` (before insert or update or delete), `RELIGION_UPD` (before update), `TRG_WS_YZS_JE_KS_Q` (after insert or update or delete)

## DEFINITIONS.REPORTING_PANEL_WISE_DOCTOR

| Column | Type | Null | Comment |
|---|---|---|---|
| PANEL_ID | VARCHAR2(5) | N |  |
| DOCTOR_MRNO | VARCHAR2(14) | N |  |
| DOCTOR_NAME | VARCHAR2(30) | Y |  |
| LETTER_HEAD1 | VARCHAR2(15) | Y |  |
| LETTER_HEAD2 | VARCHAR2(200) | Y |  |
| ORDER_BY | NUMBER(2) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_REPORTING_PANEL_WISE_DOCTOR`: PANEL_ID, DOCTOR_MRNO
- **FK** `FK_REPORTING_PANEL_WISE_DOC_1`: (PANEL_ID) -> DEFINITIONS.DEPARTMENTAL_REPORTING_PANEL(PANEL_ID)
- **CHECK** `CHK_ACTIVE`: ACTIVE IN ('H','Y','N'
- **Triggers**: `REPORTING_PANEL_WISE_DOCTOR_CEA` (before insert or update or delete), `REPORTING_PANEL_WISE_DR_DEL` (after delete), `REPORTING_PANEL_WISE_DR_INS` (before insert), `REPORTING_PANEL_WISE_DR_UPD` (before update), `TRG_WS_BBN_AG_AM_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_CONFIGURATION

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_ID | NUMBER | N |  |
| DISPLAY_NAME | VARCHAR2(50) | Y |  |
| REFERENCE_NAME | VARCHAR2(50) | Y |  |
| DESTINATION_TYPE | VARCHAR2(50) | Y |  |
| DESTINATION_FORMAT | VARCHAR2(50) | Y |  |
| PRINTER_TYPE | VARCHAR2(50) | Y |  |

- **PK** `PK_REPORT_CONFIGURATION`: REPORT_ID
- **UK** `UK_REPORT_CONFIGURATION_1`: DISPLAY_NAME
- **UK** `UK_REPORT_CONFIGURATION_2`: REFERENCE_NAME
- **Triggers**: `REPORT_CONFIGURATION_CEA` (before insert or update or delete), `REPORT_CONFIGURATION_TS` (before insert or update or delete), `TRG_WS_NMM_EP_OY_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_DESFORMAT

| Column | Type | Null | Comment |
|---|---|---|---|
| FORMAT_ID | VARCHAR2(3) | N | This column contains Unique Format ID |
| FORMAT_DESC | VARCHAR2(50) | N | This column contains Name or Description of Report Format |
| KEYWORD | VARCHAR2(25) | N | This column contains Valid Des Format Identifier i.e. understandable for report server engine |
| ACTIVE | CHAR(1) | N | This column contains Active status of Entry (Y=Active, N=Inactive) |
| RP2RRO | CHAR(1) default 'N' | N | This column contains Flag Status Y/N either it is used in RP2RRO Library |
| DIAGNOSTIC | CHAR(1) default 'N' | N | This column contains Flag Status Y/N either this format is used in Diagnostic Reports |

- **PK** `PK_REPORT_DESFORMAT`: FORMAT_ID
- **UK** `UK_REPORT_DESFORMAT_1`: KEYWORD
- **CHECK** `CK_REPORT_DESFORMAT_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_REPORT_DESFORMAT_2`: RP2RRO IN ('Y','N'
- **CHECK** `CK_REPORT_DESFORMAT_3`: DIAGNOSTIC IN ('Y','N'
- **Triggers**: `REPORT_DESFORMAT_CEA` (before insert or update or delete), `REPORT_DESFORMAT_DEL` (after delete), `REPORT_DESFORMAT_INS` (before insert), `REPORT_DESFORMAT_UPD` (before update), `TRG_WS_WAC_DZ_YN_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_DESTINATION

| Column | Type | Null | Comment |
|---|---|---|---|
| DESTINATION_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| ACTIVE | VARCHAR2(1) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| DEFAULT_DESTINATION | VARCHAR2(5) | N |  |

- **PK** `PK_REPORT_DESTINATION`: DESTINATION_ID
- **UK** `UK_REPORT_DESTINATION_2`: LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_REPORT_DESTINATION_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **Triggers**: `REPORT_DESTINATION_DEL` (after delete), `REPORT_DESTINATION_INS` (before insert), `REPORT_DESTINATION_UPD` (before update)

## DEFINITIONS.REPORT_DESTYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| TYPE_ID | VARCHAR2(3) | N | This column contains Unique ID for Report Destination Types |
| TYPE_DESC | VARCHAR2(20) | N | This column contains Unique ID for Report Destination Description |
| FORMAT_ID | VARCHAR2(3) | N | Reference key to DEFINITIONS.REPORT_DESFORMAT |
| OUTPUT_AT | VARCHAR2(10) | N | This column contains information of output source e.g. (CACHE, SCREEN, PRINTER, FILE, MAIL etc) |
| ORDER_BY | NUMBER(2) | N | Order by column to manage display order of des types |
| ACTIVE | CHAR(1) | N | This column contain flag information for Active of inactive state (Y=Active, N=Inactive) |
| DEFAULT_TYPE | CHAR(1) | N | This column contain flag information for destination type marked as defualt (Y=Yes, N=No) |

- **PK** `PK_REPORT_DESTYPES`: TYPE_ID
- **FK** `FK_REPORT_DESTYPES_1`: (FORMAT_ID) -> DEFINITIONS.REPORT_DESFORMAT(FORMAT_ID) [disabled]
- **CHECK** `CK_REPORT_DESTYPES_1`: OUTPUT_AT IN ('SCREEN','PRINTER','FILE','CACHE'
- **CHECK** `CK_REPORT_DESTYPES_2`: ACTIVE IN ('Y','N'
- **CHECK** `CK_REPORT_DESTYPES_3`: DEFAULT_TYPE IN ('Y','N'
- **Triggers**: `REPORT_DESTYPES_CEA` (before insert or update or delete), `REPORT_DESTYPES_DEL` (after delete), `REPORT_DESTYPES_INS` (before insert), `REPORT_DESTYPES_UPD` (before update), `TRG_WS_XDK_AF_KH_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_DEST_RESTRICTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| RESTRICTION_TYPE_ID | CHAR(2) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_REPT_DEST_RESTRIC_TYPE`: RESTRICTION_TYPE_ID
- **Triggers**: `REPORT_DEST_RESTRICTION_TYPE_CEA` (before insert or update or delete), `TRG_WS_DLI_OD_PR_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_DOCUMENT_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_ID | NUMBER(4) | Y |  |
| REPORT_DESCRIPTION | VARCHAR2(55) | N |  |
| DOCUMENT_TYPE | VARCHAR2(55) | N |  |
| LABEL | CHAR(1) | Y |  |

- **PK** `PK_REPORT_DOCUMENT_TYPES`: REPORT_DESCRIPTION
- **UK** `UK_REPORT_DOCUMENT_TYPES_1`: REPORT_ID
- **Triggers**: `REPORT_DOCUMENT_TYPES_CEA` (before insert or update or delete), `REPORT_DOCUMENT_TYPES_TS` (before insert or update or delete), `TRG_WS_CBL_TV_WO_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_SEARCH_FIELDS

| Column | Type | Null | Comment |
|---|---|---|---|
| FIELD_ID | NUMBER | N |  |
| REPORT_ID | NUMBER | Y |  |
| FIELD_NAME | VARCHAR2(50) | Y |  |
| TYPE | VARCHAR2(20) | N |  |
| VARIABLE_NAME | VARCHAR2(50) | Y |  |
| ORDER_NO | NUMBER | Y |  |
| REQUIRED | CHAR(1) | Y |  |
| LOOKUP_NAME | VARCHAR2(50) | Y |  |
| MAX_LENGTH | VARCHAR2(5) | Y |  |
| DEFAULT_VALUE | VARCHAR2(50) | Y |  |
| LOOKUP_QUERY | VARCHAR2(1000) | Y |  |
| HIDDEN | CHAR(1) | Y |  |
| IS_DEFAULT_FUNCTION | CHAR(1) | Y |  |

- **PK** `PK_REPORT_SEARCH_FIELDS`: FIELD_ID
- **Triggers**: `REPORT_SEARCH_FIELDS_CEA` (before insert or update or delete), `TRG_WS_MVO_JK_JD_Q` (after insert or update or delete)

## DEFINITIONS.REPORT_SERVER

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_SERVER_ID | NUMBER(3) | N |  |
| NAME | VARCHAR2(50) | Y |  |
| URL | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ENVIRONMENT_ID | VARCHAR2(256) | Y |  |
| AS_NAME | VARCHAR2(30) | Y |  |
| AS_REPORT_PORT | NUMBER(4) | Y |  |
| DEFAULT_REPORT_FORMAT | VARCHAR2(15) | Y |  |
| REMARKS | VARCHAR2(500) | Y |  |
| ACTIVE_FOR_PDF_GENERATION | CHAR(1) default 'N' | N |  |
| SERVER_TYPE | CHAR(1) | Y |  |
| AUTHENTICATION_USER | VARCHAR2(50) | Y |  |
| AUTHENTICATION_PASSWORD | VARCHAR2(64) | Y |  |
| LOCAL_DIRECTORY_PATH | VARCHAR2(500) | Y | Path of Virtual Directory will be saved into this column, path of every server may differ, It is path of OBIEE installation which will be mapped as virtual directory |
| VIRTUAL_DIRECTORY | VARCHAR2(500) | Y | OBIEE installation path after mapping as virtual directory |
| APPLICATION_BROWSER | VARCHAR2(250) | Y | This column will be used to define the browser path/ name in which this application will be opened |
| SPACE_REQ_AFTER_EXE_NAME | CHAR(1) default 'N' | Y |  |
| URL_SSL | VARCHAR2(500) | Y | Used to  enter secure url of the server |
| REPORT_WS_URL | VARCHAR2(500) | Y | URL Used in calling report in Oracle Apex |
| EXTERNAL_URL | VARCHAR2(500) | Y | Report server url for apex cloud application |

- **PK** `PK_REPORT_SERVER`: REPORT_SERVER_ID
- **Triggers**: `REPORT_SERVER_DEL` (after delete), `REPORT_SERVER_INS` (before insert), `REPORT_SERVER_UPD` (before update)

## DEFINITIONS.REPORT_SIGNING_AUTHORITIES

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| AUTHORITY_1 | VARCHAR2(14) | Y |  |
| AUTHORITY_2 | VARCHAR2(14) | Y |  |
| AUTHORITY_3 | VARCHAR2(14) | Y |  |
| AUTHORITY_4 | VARCHAR2(14) | Y |  |
| AUTHORITY_5 | VARCHAR2(14) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ZONE_ID | VARCHAR2(3) | Y |  |
| ICON_ID1 | VARCHAR2(3) | Y | This column is used to save signature reference of authority 1 |

- **PK** `PK_REPORT_SIGNING_AUTHORITIES`: SR_NO, OBJECT_CODE, SCHEMA_ID
- **Triggers**: `REPORT_SIGNING_AUTHORITIES_DEL` (after delete), `REPORT_SIGNING_AUTHORITIES_INS` (before insert), `REPORT_SIGNING_AUTHORITIES_UPD` (before update)

## DEFINITIONS.REPORT_TIMINGS_OFFSET

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Unique Location ID |
| SERIAL_NO | NUMBER(3) | N | Unique Serial No |
| TIME_FROM | VARCHAR2(5) | N | This column contains time to batch start |
| TIME_TO | VARCHAR2(5) | N | This column contains time to batch end |
| TIME_HOSPITAL | VARCHAR2(5) | N | This column contains batch reach time to lab/hospital |
| DAY_GAP | NUMBER(2) default 0 | N | This column contains value to jump calculated date for next day |
| SAMPLE_REPORT | CHAR(1) | N |  |
| PERFORM_LOCATION_ID | VARCHAR2(3) default '001' | N | This column contains perform location time of batch |
| PROCESS_TIME | NUMBER(4) default 0 | N | This column contains time in minutes to reach sampel from CCofice to relevant section |
| ACTIVE | CHAR(1) default 'Y' | N | Active status Flag Y=Yes,N=No |

- **PK** `PK_REPORT_TIMINGS_OFFSET`: PERFORM_LOCATION_ID, LOCATION_ID, SERIAL_NO
- **FK** `FK_REPORT_TIMINGS_OFFSET_1`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID) [disabled]
- **CHECK** `CK_REPORT_TIMINGS_OFFSET_1`: SAMPLE_REPORT IN ('S', 'R'
- **CHECK** `CK_REPORT_TIMINGS_OFFSET_5`: ACTIVE IN ('Y','N'
- **Triggers**: `REPORT_TIMINGS_OFFSET_DEL` (after delete), `REPORT_TIMINGS_OFFSET_INS` (before insert), `REPORT_TIMINGS_OFFSET_UPD` (before update)

## DEFINITIONS.REPORT_TIMINGS_OFFSET_IDR_R

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | Y |  |
| SERIAL_NO | NUMBER(3) | Y |  |
| TIME_FROM | VARCHAR2(5) | N |  |
| TIME_TO | VARCHAR2(5) | N |  |
| TIME_HOSPITAL | VARCHAR2(5) | N |  |
| DAY_GAP | NUMBER(2) | N |  |
| SAMPLE_REPORT | CHAR(1) | N |  |
| PERFORM_LOCATION_ID | VARCHAR2(3) | Y |  |


## DEFINITIONS.REPORT_VIEW_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| VIEW_TYPE_ID | VARCHAR2(6) | N | Unique Identifier of view type id |
| VIEW_TYPE_DESC | VARCHAR2(30) | N | This colmn contains description of report view type |
| SHORT_DESC | VARCHAR2(6) | N | This colmn contains short description of report view type |
| REMARKS | VARCHAR2(100) | Y | This colmn contains note/remarks |

- **PK** `PK_REPORT_VIEW_TYPES`: VIEW_TYPE_ID

## DEFINITIONS.RESOURCE_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| RESOURCE_TYPE | VARCHAR2(1) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_RESOURCE_TYPE`: RESOURCE_TYPE
- **Triggers**: `RESOURCE_TYPE_CEA` (before insert or update or delete), `RESOURCE_TYPE_DEL` (after delete), `RESOURCE_TYPE_INS` (before insert), `RESOURCE_TYPE_UPD` (before update), `TRG_WS_APR_SU_NX_Q` (after insert or update or delete)

## DEFINITIONS.RESTRICTION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| RESTRICTION_TYPE | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RESTRICTION_TYPE`: RESTRICTION_TYPE
- **Triggers**: `RESTRICTION_TYPE_CEA` (before insert or update or delete), `RESTRICTION_TYPE_DEL` (after delete), `RESTRICTION_TYPE_INS` (before insert), `RESTRICTION_TYPE_UPD` (before update), `TRG_WS_ONO_MF_WR_Q` (after insert or update or delete)

## DEFINITIONS.RESTRICTION_TYPE_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| RESTRICTION_TYPE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ALERT_MESSAGE | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_RESTRICTION_TYPE_CPT`: RESTRICTION_TYPE_ID
- **Triggers**: `RESTRICTION_TYPE_CPT_CEA` (before insert or update or delete), `RESTRICTION_TYPE_CPT_DEL` (after delete), `RESTRICTION_TYPE_CPT_INS` (before insert), `RESTRICTION_TYPE_CPT_UPD` (before update), `RESTRICTION_TYPE_INSERT` (before insert), `TRG_WS_PGZ_KY_FZ_Q` (after insert or update or delete)

## DEFINITIONS.RESTRICTION_TYPE_CPT_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| RESTRICTION_TYPE_ID | NUMBER(4) | N |  |
| RESTRICTION_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| RANGE_FROM | NUMBER(3) | Y |  |
| RANGE_TO | NUMBER(3) | Y |  |
| VALUE | VARCHAR2(10) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| ALERT_TYPE | VARCHAR2(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_RESTRICTION_CPT_DETAIL`: RESTRICTION_TYPE_ID, RESTRICTION_ID
- **FK** `FK_RESTRICTION_CPT_DETAIL`: (RESTRICTION_TYPE_ID) -> DEFINITIONS.RESTRICTION_TYPE_CPT(RESTRICTION_TYPE_ID)
- **Triggers**: `RESTRICTION_DETAIL_INSERT` (before insert), `RESTRICTION_TYPE_CPT_DETAIL_CEA` (before insert or update or delete), `REST_TYPE_CPT_DETAIL_DEL` (after delete), `REST_TYPE_CPT_DETAIL_INS` (before insert), `REST_TYPE_CPT_DETAIL_UPD` (before update), `TRG_WS_ALA_XD_QX_Q` (after insert or update or delete)

## DEFINITIONS.RETURN_REASONS
This table used to enter Return Reasons

| Column | Type | Null | Comment |
|---|---|---|---|
| REASON_ID | VARCHAR2(3) | N |  |
| REASON_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_RETURN_REASONS`: REASON_ID
- **Triggers**: `RETURN_REASONS_DEL` (after delete), `RETURN_REASONS_INS` (before insert), `RETURN_REASONS_UPD` (before update)

## DEFINITIONS.REVISIT_DAYS

| Column | Type | Null | Comment |
|---|---|---|---|
| REVISIT_ID | VARCHAR2(4) | N |  |
| REVISIT_DAYS | NUMBER(6) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

- **PK** `PK_REVISIT_DAYS`: REVISIT_ID
- **Triggers**: `REVISIT_DAYS_DEL` (after delete), `REVISIT_DAYS_INS` (before insert), `REVISIT_DAYS_UPD` (before update)

## DEFINITIONS.RFID_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | NUMBER(5) | Y |  |
| DEPARTMENT_NAME | VARCHAR2(100) | Y |  |
| DEPT_ID | VARCHAR2(7) | Y |  |


## DEFINITIONS.ROOMS_CATEGORY_HISTORY

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_ID | VARCHAR2(7) | N |  |
| CATEGORY_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_ROOMS_CATEGORY_HISTORY`: ROOM_ID, TRN_DATE
- **Triggers**: `ROOMS_CATEGORY_HISTORY_DEL` (after delete), `ROOMS_CATEGORY_HISTORY_INS` (before insert), `ROOMS_CATEGORY_HISTORY_UPD` (before update)

## DEFINITIONS.ROOM_CATEGORY

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| REPORT_ORDER | NUMBER(4) default 0 | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| TABLE_REFERENCE | VARCHAR2(60) | Y |  |
| COULMN_REFERENCE | VARCHAR2(60) | Y |  |
| KEY_COULMN | VARCHAR2(60) | Y |  |
| REPORT_ORDER_IBOC | NUMBER(4) | Y |  |
| MASTER_CATEGORY_ID | VARCHAR2(6) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| CATEGORY_COLOR | VARCHAR2(20) default 'Black' | Y |  |

- **PK** `PK_ROOM_CAT`: CATEGORY_ID, ORGANIZATION_ID
- **CHECK** `CK_ROOM_CATEGORY_001`: ACTIVE IN ('Y','N'
- **Triggers**: `ROOM_CATEGORY_CEA` (before insert or update or delete), `ROOM_CATEGORY_DEL` (after delete), `ROOM_CATEGORY_INS` (before insert), `ROOM_CATEGORY_UPD` (before update), `TRG_WS_XWO_KL_AM_Q` (after insert or update or delete)

## DEFINITIONS.ROOM_CATEGORY_CPT_PRICE
This table will be used to define the Ward Wise Prices

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_ID | VARCHAR2(6) | N | Room Category or Ward e.g. General Ward, Private etc. |
| CPT_ID | VARCHAR2(18) | N | CPT Code for whom Price is being changed due to Change in Ward |
| PRICE | NUMBER(12,2) | N | Price which will be used due to change in Ward |

- **PK** `PK_ROOM_CATEGORY_CPT_PRICE`: CATEGORY_ID, CPT_ID
- **FK** `FK_ROOM_CATEGORY_CPT_PRICE_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_ROOM_CATEGORY_CPT_PRICE_1`: PRICE >=1
- **Triggers**: `ROOM_CATEGORY_CPT_PRICE_DEL` (after delete), `ROOM_CATEGORY_CPT_PRICE_INS` (before insert), `ROOM_CATEGORY_CPT_PRICE_UPD` (before update)

## DEFINITIONS.ROOM_CATEGORY_SPECIALITY

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_CATEGORY_ID | VARCHAR2(6) | N |  |
| SPECIALITY_ID | VARCHAR2(6) | N |  |

- **PK** `PK_ROOM_CATEGORY_SPECIALITY`: ROOM_CATEGORY_ID, SPECIALITY_ID
- **Triggers**: `ROOM_CATEGORY_SPECIALITY_CEA` (before insert or update or delete), `TRG_WS_ATK_BC_WL_Q` (after insert or update or delete)

## DEFINITIONS.ROOM_ENTITLEMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_ID | VARCHAR2(9) | N |  |
| ROOM_DESCRIPTIONS | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ENTITLEMENT`: ROOM_ID
- **Triggers**: `ROOM_ENTITLEMENT_DEL` (after delete), `ROOM_ENTITLEMENT_INS` (before insert), `ROOM_ENTITLEMENT_UPD` (before update)

## DEFINITIONS.ROOM_PAYMENT_CAT_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(10) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N |  |
| P_DUTY_TIME | VARCHAR2(3) | N |  |
| FIRST_FOLLOW_UP | VARCHAR2(20) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_ROOM_PC_CPT`: CPT_RESTRICTION_TYPE_ID, ORGANIZATION_ID, ROOM_PAYMENT_CATEGORY_ID, P_DUTY_TIME, FIRST_FOLLOW_UP
- **FK** `FK_ROOM_PC_CPT_01`: (CPT_RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID)
- **FK** `FK_ROOM_PC_CPT_02`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **FK** `FK_ROOM_PC_CPT_03`: (ROOM_PAYMENT_CATEGORY_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID) [disabled]
- **CHECK** `CHK_ROOM_PC_CPT_01`: P_DUTY_TIME IN ('ON','OFF'
- **CHECK** `CHK_ROOM_PC_CPT_02`: FIRST_FOLLOW_UP IN ('FIRST','FOLLOW_UP'
- **Triggers**: `ROOM_PAYMENT_CAT_CPT_DEL` (after delete), `ROOM_PAYMENT_CAT_CPT_INS` (before insert), `ROOM_PAYMENT_CAT_CPT_UPD` (before update)

## DEFINITIONS.ROOM_PAYMENT_CAT_ROLE_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(10) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N |  |
| USER_ROLE_ID | NUMBER(10) | N |  |
| P_DUTY_TIME | VARCHAR2(3) | N |  |
| FIRST_FOLLOW_UP | VARCHAR2(20) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_ROOM_PCR_CPT`: CPT_RESTRICTION_TYPE_ID, ORGANIZATION_ID, ROOM_PAYMENT_CATEGORY_ID, USER_ROLE_ID, P_DUTY_TIME, FIRST_FOLLOW_UP
- **FK** `FK_ROOM_PCR_CPT_01`: (CPT_RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID)
- **FK** `FK_ROOM_PCR_CPT_02`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **FK** `FK_ROOM_PCR_CPT_03`: (ROOM_PAYMENT_CATEGORY_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID) [disabled]
- **FK** `FK_ROOM_PCR_CPT_04`: (USER_ROLE_ID) -> SECURITY.ROLE(ROLE_ID) [disabled]
- **CHECK** `CHK_ROOM_PCR_CPT_01`: P_DUTY_TIME IN ('ON','OFF'
- **CHECK** `CHK_ROOM_PCR_CPT_02`: FIRST_FOLLOW_UP IN ('FIRST','FOLLOW_UP'
- **Triggers**: `ROOM_PAYMENT_CAT_ROLE_CPT_DEL` (after delete), `ROOM_PAYMENT_CAT_ROLE_CPT_INS` (before insert), `ROOM_PAYMENT_CAT_ROLE_CPT_UPD` (before update)

## DEFINITIONS.ROOM_PAYMENT_CAT_USER_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_RESTRICTION_TYPE_ID | VARCHAR2(10) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| ROOM_PAYMENT_CATEGORY_ID | VARCHAR2(3) | N |  |
| USER_MRNO | VARCHAR2(14) | N |  |
| P_DUTY_TIME | VARCHAR2(3) | N |  |
| FIRST_FOLLOW_UP | VARCHAR2(20) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| ACTIVE | CHAR(1) | N |  |

- **PK** `PK_ROOM_PCU_CPT`: CPT_RESTRICTION_TYPE_ID, ORGANIZATION_ID, ROOM_PAYMENT_CATEGORY_ID, USER_MRNO, P_DUTY_TIME, FIRST_FOLLOW_UP
- **FK** `FK_ROOM_PCU_CPT_01`: (CPT_RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID)
- **FK** `FK_ROOM_PCU_CPT_02`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **FK** `FK_ROOM_PCU_CPT_03`: (ROOM_PAYMENT_CATEGORY_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID) [disabled]
- **FK** `FK_ROOM_PCU_CPT_04`: (USER_MRNO) -> HRD.INFORMATION(MRNO) [disabled]
- **CHECK** `CHK_ROOM_PCUC_01`: P_DUTY_TIME IN ('ON','OFF'
- **CHECK** `CHK_ROOM_PCUC_02`: FIRST_FOLLOW_UP IN ('FIRST','FOLLOW_UP'
- **Triggers**: `ROOM_PAYMENT_CAT_USER_CPT_DEL` (after delete), `ROOM_PAYMENT_CAT_USER_CPT_INS` (before insert), `ROOM_PAYMENT_CAT_USER_CPT_UPD` (before update)

## DEFINITIONS.ROOM_SEQUENCE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| ROOM_ID | VARCHAR2(11) | N |  |

- **PK** `ROOM_SEQUENCE_SETUP_PK`: ROOM_ID
- **FK** `ROOM_SEQUENCE_SETUP_FK`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION_ROOM(LOCATION_ID, ORDER_LOCATION_ID)
- **Triggers**: `ROOM_SEQUENCE_SETUP_DEL` (after delete), `ROOM_SEQUENCE_SETUP_UPD` (before update)

## DEFINITIONS.ROUTE

| Column | Type | Null | Comment |
|---|---|---|---|
| ROUTE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(25) | Y |  |
| LABEL_DESCRIPTION | VARCHAR2(100) | Y | Purpose of this column is to show the route_label_desc on discharge summary |
| RT_ALERT | VARCHAR2(1) default 'N' | Y |  |
| SHOW_EXPIRY_ON_CHEMO | VARCHAR2(1) default 'N' | Y |  |
| CHEMO_QUANTITY_LIMIT | NUMBER | Y |  |

- **PK** `PK_ROUTE`: ROUTE_ID
- **Triggers**: `ROUTE_CEA` (before insert or update or delete), `ROUTE_DEL` (after delete), `ROUTE_INS` (before insert), `ROUTE_UPD` (before update), `TRG_WS_XOS_PJ_IX_Q` (after insert or update or delete)

## DEFINITIONS.ROUTE_LANGUAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| ROUTE_ID | VARCHAR2(5) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y |  |
| LABEL_DESC1 | NVARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_ROUTE_LANGUAGE_SETUP`: LANGUAGE_ID, ROUTE_ID

## DEFINITIONS.RPC_CPT
This table contains info about  Cpt setup Room Payment Cat wise

| Column | Type | Null | Comment |
|---|---|---|---|
| RPC_ID | VARCHAR2(3) | N | This column contains info about Room Payment Cat Id |
| RPCC_SER | NUMBER(5) | N | This column contains serial no |
| RESTRICTION_TYPE_ID | VARCHAR2(10) | N | This column contains info about Restriction Type Id |
| ORGANIZATION_ID | VARCHAR2(3) | N | This col contains info about Organization Id |
| VISIT_TYPE | CHAR(1) | N | This column contains info about Visit Type (F For First, O for Followup) |
| DUTY_TIME | CHAR(1) | N | This column contains info about Duty Time (1 for ON , 0 for Off) |
| CPT_ID | VARCHAR2(18) | N | This column contains info about CPT |
| ACTIVE | CHAR(1) | N | This column contains info about Active or In Active (Y for Active, N for In Active) |
| ORDER_BY | NUMBER(2) | N | This column contains info about record priority |

- **PK** `PK_RPC_CPT`: RPC_ID, RPCC_SER
- **UK** `UK_RPC_CPT_1`: RPC_ID, RESTRICTION_TYPE_ID, ORGANIZATION_ID, VISIT_TYPE, DUTY_TIME, CPT_ID
- **FK** `FK_RPC_CPT_1`: (RPC_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID)
- **FK** `FK_RPC_CPT_2`: (RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID) [disabled]
- **CHECK** `CK_RPC_CPT_1`: VISIT_TYPE IN ('F','O'
- **CHECK** `CK_RPC_CPT_2`: DUTY_TIME IN ('0','1'
- **CHECK** `CK_RPC_CPT_3`: ACTIVE IN ('Y','N'
- **Triggers**: `RPC_CPT_INS` (before insert)

## DEFINITIONS.RPC_ROLE
This table contains info about Role Level Cpt setup Room Payment Cat wise

| Column | Type | Null | Comment |
|---|---|---|---|
| RPC_ID | VARCHAR2(3) | N | This column contains info about Room Payment Cat Id |
| RPCR_SER | NUMBER(5) | N | This column contains serial no |
| RESTRICTION_TYPE_ID | VARCHAR2(10) | N | This column contains info about Restriction Type Id |
| ORGANIZATION_ID | VARCHAR2(3) | N | This col contains info about Organization Id |
| VISIT_TYPE | CHAR(1) | N | This column contains info about Visit Type (F For First, O for Followup) |
| DUTY_TIME | CHAR(1) | N | This column contains info about Duty Time (1 for ON , 0 for Off) |
| ROLE_ID | NUMBER(3) | N | This column contains info about User Role Id |
| CPT_ID | VARCHAR2(18) | N | This column contains info about CPT |
| ACTIVE | CHAR(1) | N | This column contains info about Active or In Active (Y for Active, N for In Active) |
| ORDER_BY | NUMBER(2) | N | This column contains info about record priority |

- **PK** `PK_RPC_ROLE`: RPC_ID, RPCR_SER
- **UK** `UK_RPC_ROLE_1`: RPC_ID, RESTRICTION_TYPE_ID, ORGANIZATION_ID, VISIT_TYPE, DUTY_TIME, ROLE_ID, CPT_ID
- **FK** `FK_RPC_ROLE_1`: (RPC_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID)
- **FK** `FK_RPC_ROLE_2`: (RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID) [disabled]
- **CHECK** `CK_RPC_ROLE_1`: VISIT_TYPE IN ('F','O'
- **CHECK** `CK_RPC_ROLE_2`: DUTY_TIME IN ('0','1'
- **CHECK** `CK_RPC_ROLE_3`: ACTIVE IN ('Y','N'
- **Triggers**: `RPC_ROLE_DEL` (after delete), `RPC_ROLE_INS` (before insert), `RPC_ROLE_UPD` (before update)

## DEFINITIONS.RPC_USER
This table contains info about User Level Cpt setup Room Payment Cat wise

| Column | Type | Null | Comment |
|---|---|---|---|
| RPC_ID | VARCHAR2(3) | N | This column contains info about Room Payment Cat Id |
| RPCU_SER | NUMBER(5) | N | This column contains serial no |
| RESTRICTION_TYPE_ID | VARCHAR2(10) | N | This column contains info about Restriction Type Id |
| ORGANIZATION_ID | VARCHAR2(3) | N | This col contains info about Organization Id |
| VISIT_TYPE | CHAR(1) | N | This column contains info about Visit Type (F For First, O for Followup) |
| DUTY_TIME | CHAR(1) | N | This column contains info about Duty Time (1 for ON , 0 for Off) |
| USER_MRNO | VARCHAR2(14) | N | This Column contains info about User Mrno |
| CPT_ID | VARCHAR2(18) | N | This column contains info about CPT |
| ACTIVE | CHAR(1) | N | This column contains info about Active or In Active (Y for Active, N for In Active) |
| ORDER_BY | NUMBER(2) | N | This column contains info about record priority |

- **PK** `PK_RPC_USER`: RPC_ID, RPCU_SER
- **UK** `UK_RPC_USER_1`: RPC_ID, RESTRICTION_TYPE_ID, ORGANIZATION_ID, VISIT_TYPE, DUTY_TIME, USER_MRNO, CPT_ID
- **FK** `FK_RPC_USER_1`: (RPC_ID) -> DEFINITIONS.ROOM_PAYMENT_CATEGORY(ROOM_PAYMENT_CATEGORY_ID)
- **FK** `FK_RPC_USER_2`: (RESTRICTION_TYPE_ID) -> DEFINITIONS.CPT_RESTRICTION_TYPE(CPT_RESTRICTION_TYPE_ID) [disabled]
- **CHECK** `CK_RPC_USER_1`: VISIT_TYPE IN ('F','O'
- **CHECK** `CK_RPC_USER_2`: DUTY_TIME IN ('0','1'
- **CHECK** `CK_RPC_USER_3`: ACTIVE IN ('Y','N'
- **Triggers**: `RPC_USER_DEL` (after delete), `RPC_USER_INS` (before insert), `RPC_USER_UPD` (before update)

## DEFINITIONS.SALUTATION

| Column | Type | Null | Comment |
|---|---|---|---|
| SAL_ID | NUMBER(1) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_SALUTATIONS`: SAL_ID

## DEFINITIONS.SC

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |

- **PK** `PK_SC`: CPT_ID

## DEFINITIONS.SCHEMAS_PIC

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| NAME | VARCHAR2(30) | N |  |
| SCHEMA_TYPE_FLAG | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | N |  |
| RTM_REQUIRED | CHAR(1) | N |  |
| RTM_CHECK | CHAR(1) | N |  |
| SCHEMA_LEVEL | NUMBER(3) | Y |  |
| SEND_EMAIL | CHAR(1) | Y |  |
| EMAIL | VARCHAR2(30) | Y |  |


## DEFINITIONS.SCHEMAS_SIUT

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| NAME | VARCHAR2(30) | N |  |
| SCHEMA_TYPE_FLAG | CHAR(1) default 'T' | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| RTM_REQUIRED | CHAR(1) default 'Y' | N |  |
| RTM_CHECK | CHAR(1) default 'Y' | N |  |
| SCHEMA_LEVEL | NUMBER(3) default 999 | Y |  |
| SEND_EMAIL | CHAR(1) default 'N' | Y | This column contains flag to use email solution for specific module |
| EMAIL | VARCHAR2(30) | Y |  |


## DEFINITIONS.SCHEMAS_WISE_DOMAIN_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| GROUP_ID | VARCHAR2(6) | N |  |
| GROUP_TYPE | VARCHAR2(2) | N | RO mean Read Only , RW mean Read Write,ST mean Setup |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_SCHEMA_GROUP`: SCHEMA_ID, GROUP_ID
- **Triggers**: `SCHEMAS_WISE_DOMAIN_GROUPS_DEL` (after delete), `SCHEMAS_WISE_DOMAIN_GROUPS_INS` (before insert), `SCHEMAS_WISE_DOMAIN_GROUPS_UPD` (before update)

## DEFINITIONS.SCREEN_DISPLAY_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| DISPLAY_ID | NUMBER | N |  |
| DISPLAY_DESC | VARCHAR2(200) | N |  |
| STATUS | CHAR(1) default 'Y' | Y |  |
| DISPLAY_ORDER | NUMBER | Y |  |
| DISPLAY_TYPE_ID | NUMBER | Y |  |
| DISPLAY_TIME | NUMBER default 5 | Y |  |
| URL | VARCHAR2(500) | Y |  |

- **PK** `PK_SCREEN_DISPLAY_MASTER`: DISPLAY_ID
- **FK** `SCREEN_DISPLAY_MASTER_FK`: (DISPLAY_TYPE_ID) -> DEFINITIONS.DISPLAY_TYPE(TYPE_ID) [disabled]
- **Triggers**: `SCREEN_DISPLAY_MASTER_DEL` (after delete), `SCREEN_DISPLAY_MASTER_INS` (before insert), `SCREEN_DISPLAY_MASTER_UPD` (before update)

## DEFINITIONS.SCREEN_DISPLAY_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| DETAIL_ID | NUMBER | N |  |
| DISPLAY_ID | NUMBER | N |  |
| SCREEN_PATH | VARCHAR2(200) | Y |  |
| STATUS | CHAR(1) default 'Y' | Y |  |
| DISPLAY_ORDER | NUMBER | Y |  |

- **PK** `SCREEN_DISPLAY_DETAIL_PK`: DETAIL_ID, DISPLAY_ID
- **FK** `SCREEN_DISPLAY_DETAIL_FK`: (DISPLAY_ID) -> DEFINITIONS.SCREEN_DISPLAY_MASTER(DISPLAY_ID) [disabled]
- **Triggers**: `SCREEN_DISPLAY_DETAIL_DEL` (after delete), `SCREEN_DISPLAY_DETAIL_INS` (before insert), `SCREEN_DISPLAY_DETAIL_UPD` (before update)

## DEFINITIONS.SEQUENCE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SEQ_ID | NUMBER(10) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| FROM_SEQ | VARCHAR2(5) | Y |  |
| TO_SEQ | VARCHAR2(5) | Y |  |
| DURATION | DATE | Y |  |
| IMAGE | LONG RAW | Y |  |
| REMARKS | VARCHAR2(2000) | Y |  |
| PREFIX | VARCHAR2(3) | Y |  |
| RESET_TIME | NUMBER(5) | Y |  |
| IS_SHOW_REPORT | CHAR(1) | Y |  |
| RECEPTION_ID | NUMBER(10) | N |  |
| ORDERED_BY | NUMBER(2) | Y |  |
| IS_DUPLICATE | CHAR(1) | Y |  |
| IS_SOUND | CHAR(1) | Y |  |
| TOKEN_STATUS | CHAR(1) | Y |  |
| IS_ANY | CHAR(1) | Y |  |
| AUTO_GET | CHAR(1) | Y |  |
| GET_LOCATION_TERMINAL | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| TOKEN_TYPE_ID | NUMBER(16) | Y |  |
| AUTO_PRINT | CHAR(1) default 'N' | Y |  |
| SERVICE_REMARKS | CHAR(1) default 'N' | Y |  |
| SMS_REQUIRED | CHAR(1) default 'N' | Y |  |
| DISPLAY_TIME_TOKEN | CHAR(1) default 'N' | Y |  |
| IS_PHARMACY | CHAR(1) default 'N' | Y |  |
| IS_TOKEN_TIME_EXCEED | CHAR(1) default 'N' | Y |  |
| TOKEN_TIME_EXCEED | NUMBER | Y |  |

- **PK** `PK_SEQUENCE_SETUP`: SEQ_ID, LOCATION_ID, RECEPTION_ID
- **FK** `FK_SEQUENCE_SETUP`: (RECEPTION_ID, LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION_RECEPTION(RECEPTION_ID, LOCATION_ID, ORDER_LOCATION_ID) [disabled]
- **Triggers**: `SEQUENCE_SETUP_DEL` (after delete), `SEQUENCE_SETUP_INS` (before insert), `SEQUENCE_SETUP_UPD` (before update)

## DEFINITIONS.SEQ_TOKEN_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SEQ_ID | NUMBER(10) | N |  |
| TOKEN_TYPE_ID | NUMBER(16) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| RECEPTION_ID | NUMBER(10) | N |  |
| ORDERED_BY | NUMBER(2) | Y |  |

- **PK** `PK_SEQ_TOKEN_TYPE`: TOKEN_TYPE_ID, LOCATION_ID, RECEPTION_ID, SEQ_ID
- **Triggers**: `SEQ_TOKEN_TYPE_DEL` (after delete), `SEQ_TOKEN_TYPE_INS` (before insert), `SEQ_TOKEN_TYPE_UPD` (before update)

## DEFINITIONS.SERVER_WISE_APPLICATION

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVER_ID | NUMBER(3) | N |  |
| APPLICATION_ID | NUMBER(3) | N |  |
| START_DATE | DATE | Y |  |
| END_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_SERVER_WISE_APPLICATION`: SERVER_ID, APPLICATION_ID
- **FK** `FK_SERVER_WISE_APP_1`: (SERVER_ID) -> DEFINITIONS.APPLICATION_SERVERS(SERVER_ID)
- **FK** `FK_SERVER_WISE_APP_2`: (APPLICATION_ID) -> DEFINITIONS.APPLICATION_SETUP(APPLICATION_ID) [disabled]

## DEFINITIONS.SERVICE_STATUS
This table contains definitions of Army Service Status (System Constant Level table)

| Column | Type | Null | Comment |
|---|---|---|---|
| STATUS_ID | VARCHAR2(6) | N | Unique Primary Key Status ID |
| DESCRIPTION | VARCHAR2(255) | N | This column contains Name/Description of servcies status |
| ACTIVE | CHAR(1) default 'N' | N | This column contains flag of Active, Inactive state (Y=Active, N=Inactive) |
| RETIRED | CHAR(1) default 'N' | N | This column contains flag of Retired status (Y=Retired, N=Non Retired) |
| SHORT_DESCRIPTION | VARCHAR2(20) | N | This column contains Short description of service status |
| CAPTION_IN_NAME | VARCHAR2(10) | Y | This column contains caption to be displayed in Full Name of  person |
| ORDER_NO | NUMBER(4) | Y |  |

- **PK** `PK_SERVICE_STATUS`: STATUS_ID
- **UK** `UK_SERVICE_STATUS`: DESCRIPTION
- **CHECK** `CHK_SERVICE_STATUS_1`: ACTIVE IN ('N','Y'
- **CHECK** `CHK_SERVICE_STATUS_2`: RETIRED IN ('N','Y'
- **Triggers**: `SERVICE_STATUS_CEA` (before insert or update or delete), `SERVICE_STATUS_DEL` (after delete), `SERVICE_STATUS_INS` (before insert), `SERVICE_STATUS_UPD` (before update), `TRG_WS_UWO_MF_CI_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_CATEGORY_RELATION

| Column | Type | Null | Comment |
|---|---|---|---|
| CATEGORY_CODE | VARCHAR2(20) | N |  |
| SERVICE_STATUS_ID | VARCHAR2(6) | N |  |
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_SERVICE_CATEGORY_RELATION`: CATEGORY_CODE
- **UK** `UK_SERVICE_CATEGORY_RELATION_1`: PATIENT_TYPE_ID, SERVICE_STATUS_ID
- **FK** `FK_SERVICE_CATEGORY_RELATION_1`: (SERVICE_STATUS_ID) -> DEFINITIONS.SERVICE_STATUS(STATUS_ID) [disabled]
- **FK** `FK_SERVICE_CATEGORY_RELATION_2`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **Triggers**: `SERVICE_CATEGORY_RELATION_DEL` (after delete), `SERVICE_CATEGORY_RELATION_INS` (before insert), `SERVICE_CATEGORY_RELATION_UPD` (before update)

## DEFINITIONS.SERVICE_STATUS_PAT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| PATIENT_TYPE_ID | VARCHAR2(6) | N |  |
| STATUS_ID | CHAR(1) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |

_No standard audit columns._

- **PK** `PK_SERVICE_STATUS_PAT_TYPE`: PATIENT_TYPE_ID, STATUS_ID
- **FK** `FK_SERVICE_STATUS_PAT_TYPE_1`: (PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID)
- **CHECK** `CHK_SERVICE_STATUS_PAT_TYPE_1`: ACTIVE IN ('N','Y'

## DEFINITIONS.SERVICE_SUB_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This column will represents the Service Type |
| THERAPEUTIC_GROUP_ID | VARCHAR2(3) | N | This column will represents the Therapeutic Group |
| SUB_GROUP_ID | VARCHAR2(3) | N | This column will represents the Therapeutic Sub Group |
| ALL_SERVICE | CHAR(1) default 'N' | N | Values of this column must be Y or N, Y means all the Item Group and Items are allowed no need to check from detail level, If N then check from detail tables individually |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_SUB_GROUP`: SERVICE_TYPE_ID, THERAPEUTIC_GROUP_ID, SUB_GROUP_ID
- **FK** `FK_SERVICE_SUB_GROUP_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_SUB_GROUP_2`: (THERAPEUTIC_GROUP_ID, SUB_GROUP_ID) -> PHARMACY.TG_SUBGROUP(T_GROUP_ID, T_SUBGROUP_ID) [disabled]
- **Triggers**: `SERVICE_SUB_GROUP_CEA` (before insert or update or delete), `SERVICE_SUB_GROUP_DEL` (after delete), `SERVICE_SUB_GROUP_INS` (before insert), `SERVICE_SUB_GROUP_UPD` (before update), `TRG_WS_XIE_CY_LX_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_THERAPEUTIC_GROUP
This table will be used to link the Therapeutic Group with the Service Type

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | This column will represents the Service Type |
| THERAPEUTIC_GROUP_ID | VARCHAR2(3) | N | This column will represents the Therapeutic Group |
| ALL_SERVICE | CHAR(1) default 'N' | N | Values of this column must be Y or N, Y means all the Therapeutic Sub Group, Item Group and Items are allowed no need to check from detail level, If N then check from detail tables individually |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_THERAPEUTIC_GROUP`: SERVICE_TYPE_ID, THERAPEUTIC_GROUP_ID
- **FK** `FK_SERVICE_THERAPEUTIC_GROUP_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_THERAPEUTIC_GROUP_2`: (THERAPEUTIC_GROUP_ID) -> PHARMACY.THERAPEUTIC_GROUP(T_GROUP_ID) [disabled]
- **Triggers**: `SERVICE_THERAPEUTIC_GROUP_CEA` (before insert or update or delete), `SERVICE_THERAPEUTIC_GROUP_DEL` (after delete), `SERVICE_THERAPEUTIC_GROUP_INS` (before insert), `SERVICE_THERAPEUTIC_GROUP_UPD` (before update), `TRG_WS_HEY_CO_VB_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_CPT
This table will be used to define the Service Type wise CPTs

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Service Type Ref |
| CPT_ID | VARCHAR2(18) | N | CPT Code |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_TYPE_CPT`: SERVICE_TYPE_ID, CPT_ID
- **FK** `FK_SERVICE_TYPE_CPT_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_TYPE_CPT_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_SERVICE_TYPE_CPT_1`: ACTIVE IN ('Y','N'
- **Triggers**: `SERVICE_TYPE_CPT_CEA` (before insert or update or delete), `SERVICE_TYPE_CPT_DEL` (after delete), `SERVICE_TYPE_CPT_INS` (before insert), `SERVICE_TYPE_CPT_UPD` (before update), `TRG_WS_RYO_LP_GS_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_DEPARTMENT_NATURE
This table will be used to link the Service Type with the Department Nature

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N |  |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N |  |
| ALL_SERVICES | CHAR(1) default 'N' | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_SERVICE_TYPE_DEPT_NATURE`: SERVICE_TYPE_ID, DEPARTMENT_NATURE_ID
- **FK** `FK_SERVICE_TYPE_DEPT_NATURE_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_TYPE_DEPT_NATURE_2`: (DEPARTMENT_NATURE_ID) -> DEFINITIONS.DEPARTMENT_NATURE(DEPARTMENT_NATURE_ID) [disabled]
- **CHECK** `CK_SERVICE_TYPE_DEPT_NATURE_1`: ALL_SERVICES IN ('Y','N'
- **CHECK** `CK_SERVICE_TYPE_DEPT_NATURE_2`: ACTIVE IN ('Y','N'
- **Triggers**: `SERVICE_TYPE_DEPARTMENT_NATURE_CEA` (before insert or update or delete), `SERV_TYPE_DEP_NATURE_DEL` (after delete), `SERV_TYPE_DEP_NATURE_INS` (before insert), `SERV_TYPE_DEP_NATURE_UPD` (before update), `TRG_WS_HOZ_NV_IZ_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_ITEM
This Table will be used to define the Service Type wise Item / Brand

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Service Type Ref |
| ITEM_GROUP_ID | VARCHAR2(25) | N | Item Group / Generic Ref |
| ITEM_ID | VARCHAR2(25) | N | Item / Brand |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_TYPE_ITEM`: SERVICE_TYPE_ID, ITEM_GROUP_ID, ITEM_ID
- **FK** `FK_SERVICE_TYPE_ITEM_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_TYPE_ITEM_2`: (ITEM_GROUP_ID) -> ITEM.ITEM_GROUP(ITEM_GROUP_ID) [disabled]
- **FK** `FK_SERVICE_TYPE_ITEM_3`: (ITEM_ID) -> ITEM.ITEM(ITEM_ID) [disabled]
- **CHECK** `CK_SERVICE_TYPE_ITEM_1`: ACTIVE IN ('Y','N'
- **Triggers**: `SERVICE_TYPE_ITEM_CEA` (before insert or update or delete), `SERVICE_TYPE_ITEM_DEL` (after delete), `SERVICE_TYPE_ITEM_INS` (before insert), `SERVICE_TYPE_ITEM_UPD` (before update), `TRG_WS_VJQ_SQ_BG_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_ITEM_GROUP
This table will be used to define the Service Type wise Item Group

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Service Type Ref |
| ITEM_GROUP_ID | VARCHAR2(25) | N | Item Group / Generic Ref |
| ALL_SERVICES | CHAR(1) default 'N' | N | Values must be Y or N, Y means All Item/Brand of this Item Group are included |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_TYPE_ITEM_GROUP`: SERVICE_TYPE_ID, ITEM_GROUP_ID
- **FK** `FK_SERVICE_TYPE_ITEM_GROUP_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **FK** `FK_SERVICE_TYPE_ITEM_GROUP_2`: (ITEM_GROUP_ID) -> ITEM.ITEM_GROUP(ITEM_GROUP_ID) [disabled]
- **Triggers**: `SERVICE_TYPE_ITEM_GROUP_CEA` (before insert or update or delete), `SERVICE_TYPE_ITEM_GROUP_DEL` (after delete), `SERVICE_TYPE_ITEM_GROUP_INS` (before insert), `SERVICE_TYPE_ITEM_GROUP_UPD` (before update), `TRG_WS_RWD_YM_MN_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_SECTION_NATURE
This table will be used to define the Section Nature wise Service Type

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Service Type Ref |
| DEPARTMENT_NATURE_ID | VARCHAR2(3) | N | Department Nature Ref |
| SECTION_NATURE_ID | VARCHAR2(3) | N | Section Nature |
| ALL_SERVICES | CHAR(1) default 'N' | N | Values must be Y or N, Y means all CPT of this Section Nature are included |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the transaction |

- **PK** `PK_SERVICE_TYPE_SEC_NATURE`: SERVICE_TYPE_ID, DEPARTMENT_NATURE_ID, SECTION_NATURE_ID
- **FK** `FK_SERVICE_TYPE_SEC_NATURE_1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **CHECK** `CK_SERVICE_TYPE_SEC_NATURE_1`: ALL_SERVICES IN ('Y','N'
- **CHECK** `CK_SERVICE_TYPE_SEC_NATURE_2`: ACTIVE IN ('Y','N'
- **Triggers**: `SERVICE_TYPE_SECTION_NATURE_CEA` (before insert or update or delete), `SERVICE_TYP_SEC_NATURE_DEL` (after delete), `SERVICE_TYP_SEC_NATURE_INS` (before insert), `SERVICE_TYP_SEC_NATURE_UPD` (before update), `TRG_WS_YEX_WN_BM_Q` (after insert or update or delete)

## DEFINITIONS.SERVICE_TYPE_STORE
This table will be used to define the Service Type Stores

| Column | Type | Null | Comment |
|---|---|---|---|
| SERVICE_TYPE_ID | VARCHAR2(3) | N | Service Type Ref |
| STORE_ID | VARCHAR2(25) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_SERVICE_TYPE_STORE`: SERVICE_TYPE_ID, STORE_ID
- **FK** `FK_SERVICE_TYPE_STORE1`: (SERVICE_TYPE_ID) -> DEFINITIONS.SERVICE_TYPE(SERVICE_TYPE_ID)
- **CHECK** `CK_SERVICE_TYPE_STORE_1`: ACTIVE IN ('Y','N'
- **Triggers**: `SERVICE_TYPE_STORE_CEA` (before insert or update or delete), `SERVICE_TYPE_STORE_DEL` (after delete), `SERVICE_TYPE_STORE_INS` (before insert), `SERVICE_TYPE_STORE_UPD` (before update), `TRG_WS_KVI_RK_JK_Q` (after insert or update or delete)

## DEFINITIONS.SESSION_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SESSION_TYPE | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| MARGIN_TIME | NUMBER(3) | Y |  |

- **PK** `PK_SESSION_TYPE`: SESSION_TYPE
- **Triggers**: `SESSION_TYPE_CEA` (before insert or update or delete), `SESSION_TYPE_DEL` (after delete), `SESSION_TYPE_INS` (before insert), `SESSION_TYPE_UPD` (before update), `TRG_WS_YXE_ME_WB_Q` (after insert or update or delete)

## DEFINITIONS.SESSIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| SESSION_TYPE | NUMBER(3) | N |  |
| SESSION_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| SHORT_DESC | VARCHAR2(15) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SESSION_TIME_FROM | CHAR(5) | Y |  |
| SESSION_TIME_TO | CHAR(5) | Y |  |
| SHIFT_TYPE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_SESSIONS`: SESSION_TYPE, SESSION_ID
- **FK** `FK_SESSIONS_1`: (SESSION_TYPE) -> DEFINITIONS.SESSION_TYPE(SESSION_TYPE)
- **Triggers**: `SESSIONS_CEA` (before insert or update or delete), `SESSIONS_DEL` (after delete), `SESSIONS_INS` (before insert), `SESSIONS_UPD` (before update), `TRG_WS_PUR_YR_HC_Q` (after insert or update or delete)

## DEFINITIONS.SETUP_DETAIL_ADMIN

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_NATURE_ID | VARCHAR2(3) | N |  |
| SETUP_DETAIL_ID | VARCHAR2(3) | N |  |
| DEPT_NATURE_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ADMIN_BY | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SETUP_DETAIL_ADMIN_001`: SETUP_NATURE_ID, SETUP_DETAIL_ID, LOCATION_ID
- **Triggers**: `SETUP_DETAIL_ADMIN_INS` (before insert)

## DEFINITIONS.SETUP_NATURE

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_NATURE_ID | VARCHAR2(3) | N |  |
| DEPT_NATURE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ORGANIZATION_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SETUP_NATURE_001`: SETUP_NATURE_ID
- **UK** `UK_SETUP_NATURE_002`: DEPT_NATURE_ID, SETUP_NATURE_ID
- **UK** `UK_SETUP_NATURE_003`: DESCRIPTION
- **Triggers**: `SETUP_NATURE_INS` (before insert)

## DEFINITIONS.SETUP_NATURE_ADMIN

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_NATURE_ID | VARCHAR2(3) | N |  |
| DEPT_NATURE_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ADMIN_BY | VARCHAR2(14) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `SETUP_NATURE_ADMIN_001`: SETUP_NATURE_ID, DEPT_NATURE_ID, LOCATION_ID
- **Triggers**: `SETUP_NATURE_ADMIN_INS` (before insert)

## DEFINITIONS.SETUP_NATURE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SETUP_DETAIL_ID | VARCHAR2(3) | N |  |
| SETUP_NATURE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| MODULE_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SETUP_NATURE_DETAIL_001`: SETUP_DETAIL_ID, SETUP_NATURE_ID
- **UK** `UK_SETUP_NATURE_DETAIL_001`: DESCRIPTION
- **Triggers**: `SETUP_NATURE_DETAIL_INS` (before insert)

## DEFINITIONS.SEX

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(1) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_SEX`: SEX_ID
- **Triggers**: `SEX_CEA` (before insert or update or delete), `SEX_DEL` (after delete), `SEX_INS` (before insert), `SEX_TS` (before insert or update or delete), `SEX_UPD` (before update), `TRG_WS_ZIE_TZ_FT_Q` (after insert or update or delete)

## DEFINITIONS.SEX_MARITAL_STATUS

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(1) | N |  |
| MARITAL_STATUS_ID | VARCHAR2(6) | N |  |

- **PK** `PK_SEX_MARITAL_STATUS`: SEX_ID, MARITAL_STATUS_ID
- **Triggers**: `SEX_MARITAL_STATUS_DEL` (after delete), `SEX_MARITAL_STATUS_INS` (before insert), `SEX_MARITAL_STATUS_UPD` (before update)

## DEFINITIONS.SIDE_EFFECT

| Column | Type | Null | Comment |
|---|---|---|---|
| EFFECT_ID | VARCHAR2(5) | N |  |
| EFFECT_TYPE_ID | VARCHAR2(3) | Y |  |
| EFFECT_DESCRIPTION | VARCHAR2(2000) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| SEQ_NO | NUMBER(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_SIDE_EFFECT`: EFFECT_ID
- **FK** `FK_SIDE_EFFECT`: (EFFECT_TYPE_ID) -> DEFINITIONS.EFFECT_TYPE(EFFECT_TYPE_ID) [disabled]
- **Triggers**: `SIDE_EFFECT_DEL` (after delete), `SIDE_EFFECT_INS` (before insert), `SIDE_EFFECT_UPD` (before update)

## DEFINITIONS.SINGLE_COLUMN_KEY_TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| OWNER | VARCHAR2(128) | N |  |
| CONSTRAINT_NAME | VARCHAR2(128) | N |  |
| TABLE_NAME | VARCHAR2(128) | N |  |
| COLUMN_NAME | VARCHAR2(4000) | Y |  |
| POSITION | NUMBER | Y |  |
| DATA_TYPE | VARCHAR2(60) | Y |  |

_No standard audit columns._


## DEFINITIONS.SKILLS

| Column | Type | Null | Comment |
|---|---|---|---|
| SKILL_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_SKILLS`: SKILL_ID
- **Triggers**: `SKILLS_CEA` (before insert or update or delete), `SKILLS_DEL` (after delete), `SKILLS_INS` (before insert), `SKILLS_UPD` (before update), `TRG_WS_HRG_HL_XS_Q` (after insert or update or delete)

## DEFINITIONS.SNOMED_CODES

| Column | Type | Null | Comment |
|---|---|---|---|
| DISEASE | VARCHAR2(100) | Y | This column contains information of disease |
| CODES | VARCHAR2(20) | N | This column contains Snomed Code (T-Code, M Code) (PK) |
| DETAIL1 | VARCHAR2(1000) | Y | This column contains other details of snomed code in details1 |
| DETAIL2 | VARCHAR2(100) | Y | This column contains other details of snomed code in details2 |
| DETAIL3 | VARCHAR2(1000) | Y | This column contains other details of snomed code in details2 |
| COMMENTS | VARCHAR2(200) | Y | This column contains other comments field |
| PUNJAB_CANCER_REGISTRY | CHAR(1) default 'N' | Y | This column contains flag information of Punjab Cancer Registey |
| SER | NUMBER(3) default 1 | N | This column contains subsidoery serial # codes (PK) |
| CANCER | CHAR(1) default 'N' | Y | This column contains flag information Cancer Code  ('Y' = 'Yes','N' = 'No') |

- **PK** `PK_SNOMED_CODES`: CODES, SER
- **CHECK** `CK_SNOMED_CODES_1`: PUNJAB_CANCER_REGISTRY IN ('Y','N'
- **CHECK** `CK_SNOMED_CODES_2`: CANCER IN ('Y','N'
- **Triggers**: `SNOMED_CODES_CEA` (before insert or update or delete), `SNOMED_CODES_DEL` (after delete), `SNOMED_CODES_INS` (before insert), `SNOMED_CODES_UPD` (before update), `TRG_WS_BEP_YV_UX_Q` (after insert or update or delete)

## DEFINITIONS.SOFTWARE_CATEGORY
This table will be used to define the Category of Software --- It is constant table,  reason of this table is that we have many software of same category such as browsers, browser will be defined as category in this table and firefox, IE etc will be defined the child table

| Column | Type | Null | Comment |
|---|---|---|---|
| SOFTWARE_CATEGORY_ID | NUMBER(3) | N |  |
| CATEGORY_DESC | VARCHAR2(50) | N | Name of the Software Category such as browsers |
| ACTIVE | CHAR(1) default 'Y' | N |  |

- **PK** `PK_SOFTWARE_CATEGORY`: SOFTWARE_CATEGORY_ID
- **Triggers**: `SOFTWARE_CATEGORY_DEL` (after delete), `SOFTWARE_CATEGORY_INS` (before insert), `SOFTWARE_CATEGORY_UPD` (before update)

## DEFINITIONS.SOFTWARE_VERSION_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| SOFWARE_ID | VARCHAR2(5) | N | This column contains info about software ID |
| SOFTWARE_NAME | VARCHAR2(100) | Y | This column cantains info about software name |
| REMARKS | VARCHAR2(500) | Y | This column contains info about remarks |
| ACTIVE | CHAR(1) | Y | This column conatins info about active or in-active |
| PATHOLOGY_FLAG | CHAR(1) default 'N' | Y | This column contains info about pathology Flag for bar tender |
| SOFTWARE_CATEGORY_ID | NUMBER(3) | N |  |

- **PK** `PK_SOFTWARE_VERSION_MASTER`: SOFWARE_ID
- **Triggers**: `SOFTWARE_VERSION_MASTER_CEA` (before insert or update or delete), `SOFTWARE_VERSION_MASTER_DEL` (after delete), `SOFTWARE_VERSION_MASTER_INS` (before insert), `SOFTWARE_VERSION_MASTER_UPD` (before update), `TRG_WS_RGG_NA_LM_Q` (after insert or update or delete)

## DEFINITIONS.SOFTWARE_VERSION_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SOFWARE_ID | VARCHAR2(5) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| INSTALLATION_PATH | VARCHAR2(500) | N |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| SOFTWARE_NAME | VARCHAR2(100) | Y | This column will be used to define the name of the software |
| EXE_NAME | VARCHAR2(250) | Y | Name of the executable file |
| VESION_NO | VARCHAR2(30) | Y | As per Version rule, it can be version name or version number |
| SPACE_REQ_AFTER_EXE_NAME | CHAR(1) default 'N' | N | When we call servers some browsers needs symbol and some needs space, will handle with the help of this column value |
| LOCATION_ID | VARCHAR2(3) | Y | This column will contain Multilocation location values for Installation Path. |
| SHORT_ORG | VARCHAR2(20) | Y | Thio column is used to contains information of short orgnization description |

- **PK** `PK_SOFTWARE_VERSION_DETAIL`: SOFWARE_ID, SERIAL_NO
- **FK** `FK_SOFTWARE_VERSION_DETAIL_1`: (SOFWARE_ID) -> DEFINITIONS.SOFTWARE_VERSION_MASTER(SOFWARE_ID)
- **Triggers**: `SOFTWARE_VERSION_DETAIL_CEA` (before insert or update or delete), `SOFTWARE_VERSION_DETAIL_DEL` (after delete), `SOFTWARE_VERSION_DETAIL_INS` (before insert), `SOFTWARE_VERSION_DETAIL_NEW_ID` (before insert), `SOFTWARE_VERSION_DETAIL_UPD` (before update), `TRG_WS_LUI_UN_NN_Q` (after insert or update or delete)

## DEFINITIONS.SOURCE_TO_CONCEPT_MAP

| Column | Type | Null | Comment |
|---|---|---|---|
| SOURCE_CODE | VARCHAR2(50) | N |  |
| SOURCE_CONCEPT_ID | NUMBER(10) default 0 | Y |  |
| SOURCE_VOCABULARY_ID | VARCHAR2(20) | N |  |
| SOURCE_CODE_DESCRIPTION | VARCHAR2(4000) | Y |  |
| TARGET_CONCEPT_ID | NUMBER(10) | N |  |
| TARGET_VOCABULARY_ID | VARCHAR2(20) | N |  |
| VALID_START_DATE | DATE | N |  |
| VALID_END_DATE | DATE | N |  |
| INVALID_REASON | VARCHAR2(1) | Y |  |
| MAPPED_BY | VARCHAR2(14) | Y |  |
| MAPPED_DATE | TIMESTAMP(6) default SYSTIMESTAMP | Y |  |
| APPROVED_BY | VARCHAR2(14) | Y |  |
| APPROVED_DATE | TIMESTAMP(6) | Y |  |
| STATUS | VARCHAR2(1) | Y |  |
| TARGET_CONCEPT_DESC | VARCHAR2(500) | Y |  |

_No standard audit columns._

- **PK** `PK_SOURCE_TO_CONCEPT_MAP`: SOURCE_VOCABULARY_ID, SOURCE_CODE, TARGET_CONCEPT_ID

## DEFINITIONS.SPECIALTY_SHARE

| Column | Type | Null | Comment |
|---|---|---|---|
| SHARE_ID | VARCHAR2(3) | N | Will be autogenerate |
| CLINIC_SPECIALTY_ID | VARCHAR2(6) | Y |  |
| ORDERING_SHARE | NUMBER | Y |  |
| SHARE_TYPE | CHAR(1) default 'F' | Y | F for fixed and V for variable |
| PERFORMER_SHARE | NUMBER | Y |  |
| ACTIVE | CHAR(1) | Y | Y mean active N mean not active |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |

- **PK** `PK_SPECIALTY_SHARE`: SHARE_ID
- **UK** `UK_SPECIALTY_SHARE`: CLINIC_SPECIALTY_ID
- **Triggers**: `SPECIALTY_SHARE_DEL` (after delete), `SPECIALTY_SHARE_INS` (before insert), `SPECIALTY_SHARE_UPD` (before update)

## DEFINITIONS.SPECIALTY_SHARE_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| SR | NUMBER | N |  |
| SHARE_ID | VARCHAR2(3) | N |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_SPECIALTY_SHARE_DETAIL`: SR, SHARE_ID
- **FK** `FK_SPECIALTY_SHARE_DETAIL`: (SHARE_ID) -> DEFINITIONS.SPECIALTY_SHARE(SHARE_ID) [disabled]
- **Triggers**: `SPECIALTY_SHARE_DETAIL_DEL` (after delete), `SPECIALTY_SHARE_DETAIL_INS` (before insert), `SPECIALTY_SHARE_DETAIL_UPD` (before update)

## DEFINITIONS.SPECIAL_INSTRUCTION

| Column | Type | Null | Comment |
|---|---|---|---|
| INSTRUCTION_ID | NUMBER | N |  |
| INSTRUCTION_DESC | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_SPECIAL_INSTRUCTION`: INSTRUCTION_ID
- **UK** `UK_SPECIAL_INSTRUCTION`: INSTRUCTION_DESC
- **Triggers**: `SPECIAL_INSTRUCTION_CEA` (before insert or update or delete), `SPECIAL_INSTRUCTION_DEL` (after delete), `SPECIAL_INSTRUCTION_INS` (before insert), `SPECIAL_INSTRUCTION_UPD` (before update), `TRG_WS_VJO_RE_TI_Q` (after insert or update or delete)

## DEFINITIONS.SPECIMEN_APPEARANCE

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIMEN_ID | VARCHAR2(5) | N |  |
| APPEARANCE_ID | VARCHAR2(5) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |

- **PK** `PK_SPECIMEN_APPEARANCE`: SPECIMEN_ID, APPEARANCE_ID
- **FK** `FK_SPECIMEN_APPEARANCE_1`: (SPECIMEN_ID) -> DEFINITIONS.SPECIMEN(SPECIMEN_ID)
- **FK** `FK_SPECIMEN_APPEARANCE_2`: (APPEARANCE_ID) -> DEFINITIONS.APPEARANCE(APPEARANCE_ID)
- **CHECK** `CK_SPECIMEN_APPEARANCE_001`: ACTIVE IN ('Y','N')
- **Triggers**: `SPECIMEN_APPEARANCE_CEA` (before insert or update or delete), `TRG_WS_XEJ_QG_OE_Q` (after insert or update or delete)

## DEFINITIONS.SPECIMEN_COLOURS

| Column | Type | Null | Comment |
|---|---|---|---|
| SPECIMEN_ID | VARCHAR2(5) | N |  |
| COLOUR_ID | VARCHAR2(5) | N |  |
| ACTIVE | VARCHAR2(1) default 'Y' | N | Active status Y=Yes,N=No |
| DEFAULTS | VARCHAR2(1) default 'N' | N | Default selection status Y=Yes,N=No |

- **PK** `PK_SPECIMEN_COLOURS`: SPECIMEN_ID, COLOUR_ID
- **FK** `FK_SPECIMEN_COLOURS_1`: (SPECIMEN_ID) -> DEFINITIONS.SPECIMEN(SPECIMEN_ID)
- **FK** `FK_SPECIMEN_COLOURS_2`: (COLOUR_ID) -> DEFINITIONS.COLOURS(COLOUR_ID)
- **CHECK** `SPECIMEN_COLOURS_1`: ACTIVE IN ('Y','N'
- **CHECK** `SPECIMEN_COLOURS_2`: DEFAULTS IN ('Y','N'
- **Triggers**: `SPECIMEN_COLOURS_CEA` (before insert or update or delete), `TRG_WS_GFC_BD_UA_Q` (after insert or update or delete)

## DEFINITIONS.STATE_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_COUNTRY_ID | NUMBER(4) | Y |  |

- **PK** `PK_STATE_ZONE`: ZONE_ID, COUNTRY_ID, STATE_ID

## DEFINITIONS.STATUSWISE_PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| REC_ID | NUMBER | N |  |
| SERVICE_STATUS_ID | VARCHAR2(6) | Y |  |
| RELATION_ID | VARCHAR2(6) | Y |  |
| OLD_PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |
| NEW_PATIENT_TYPE_ID | VARCHAR2(6) | Y |  |

- **PK** `PK_STATUSWISE_PTYPE`: REC_ID
- **UK** `CONS_STATUSWISE_PTYPE_UNIQUE`: SERVICE_STATUS_ID, RELATION_ID, OLD_PATIENT_TYPE_ID, NEW_PATIENT_TYPE_ID
- **FK** `FK_NEW_PATIENT_TYPE_ID`: (NEW_PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_OLD_PATIENT_TYPE_ID`: (OLD_PATIENT_TYPE_ID) -> DEFINITIONS.PATIENT_TYPE(PATIENT_TYPE_ID) [disabled]
- **FK** `FK_RELATION_ID`: (RELATION_ID) -> DEFINITIONS.RELATION(RELATION_ID) [disabled]
- **FK** `FK_SERVICE_STATUS_ID`: (SERVICE_STATUS_ID) -> DEFINITIONS.SERVICE_STATUS(STATUS_ID)
- **Triggers**: `STATUSWISE_PATIENT_TYPE_DEL` (after delete), `STATUSWISE_PATIENT_TYPE_INS` (before insert), `STATUSWISE_PATIENT_TYPE_UPD` (before update)

## DEFINITIONS.SUB_LOCATIONS
Any user working in a sub location will have all powers as of its PROJECT/MAIN LOCATION/HEAD OFFICE users. In other words, staff working in a sub location will be considered employee of the same PROJECT/LOCATION/HEAD OFFICE etc.

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | N | Project or Head Office -- e.g. for SKM 001 will be populated in this field -- This project will be child of some Organization -- SKMT, structure will be defined soon. This value will be assigned to GLOBAL.LOCATION_ID variable on Forms/Backend Session wise Global variables Table at the time of login. |
| SUB_LOCATION_ID | VARCHAR2(3) | N | Offices working under a Project or Main/Head Office -- e.g. C01 JRDC, 007 KDC, self owned CCs  etc (But not Franchised CCs)  This value will be assigned to GLOBAL.PHYSICAL_LOCATION_ID variable on Forms/Backend Session wise Global variables Table at the time of login. |

- **PK** `PK_SUB_LOCATIONS`: LOCATION_ID, SUB_LOCATION_ID
- **UK** `UK_SUB_LOCATIONS_01`: SUB_LOCATION_ID
- **FK** `FK_SUB_LOCATIONS_01`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **FK** `FK_SUB_LOCATIONS_02`: (SUB_LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **Triggers**: `SUB_LOCATIONS_DEL` (after delete), `SUB_LOCATIONS_INS` (before insert), `SUB_LOCATIONS_UPD` (before update)

## DEFINITIONS.SUB_SERVICES

| Column | Type | Null | Comment |
|---|---|---|---|
| SUB_SERVICE_ID | NUMBER(3) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| SERVICE_CODE | CHAR(3) | N |  |
| INPATIENT | CHAR(1) | Y |  |
| BUSINESS_SERVICES | CHAR(1) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| TRANS_TYPE | CHAR(1) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| CASH | CHAR(1) | Y |  |
| NARRATION | VARCHAR2(1000) | Y |  |
| COA_CODE | VARCHAR2(100) | Y |  |
| LEDGER_TYPE_CODE | NUMBER(4) | Y |  |
| SUB_LDGR_ITEM_CODE | VARCHAR2(18) | Y |  |
| CC | CHAR(1) | N | This Column is added to distinguish Collection Centre Services, If Value is Y then This Service is available for Collection Centre, if N then not Available |

- **PK** `PK_SUB_SERVICES`: SERVICE_CODE, SUB_SERVICE_ID
- **FK** `FK_SUB_SERVICES_1`: (SERVICE_CODE) -> DEFINITIONS.GL_DEPT_SERVICES(SERVICE_CODE)
- **FK** `FK_SUB_SERVICES_2`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **FK** `FK_SUB_SERVICES_3`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **Triggers**: `SUB_SERVICES_CEA` (before insert or update or delete), `SUB_SERVICES_DEL` (after delete), `SUB_SERVICES_INS` (before insert), `SUB_SERVICES_UPD` (before update), `TRG_WS_BPG_OD_VR_Q` (after insert or update or delete)

## DEFINITIONS.SUPERNATANT

| Column | Type | Null | Comment |
|---|---|---|---|
| SUPERNATANT_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_SUPERNATANT`: SUPERNATANT_ID
- **Triggers**: `SUPERNATANT_CEA` (before insert or update or delete), `TRG_WS_LRF_VD_SI_Q` (after insert or update or delete)

## DEFINITIONS.SUPPLIER_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| SUPPLIER_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_SUPPLIER_TYPE`: SUPPLIER_TYPE_ID
- **Triggers**: `SUPPLIER_TYPE_CEA` (before insert or update or delete), `SUPPLIER_TYPE_DEL` (after delete), `SUPPLIER_TYPE_INS` (before insert), `SUPPLIER_TYPE_UPD` (before update), `TRG_WS_NJJ_SQ_PU_Q` (after insert or update or delete)

## DEFINITIONS.SURGERY_BLOOD_LOSS_R

| Column | Type | Null | Comment |
|---|---|---|---|
| BLOOD_LOSS_ID | VARCHAR2(5) | Y |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| ACTIVE | CHAR(1) | Y |  |


## DEFINITIONS.SURGERY_IMAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| IMAGE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |
| IMAGE | BLOB | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| IMAGE_FILE_LONGRAW | LONG RAW | Y |  |

- **PK** `PK_SURGERY_IMAGES`: IMAGE_ID
- **Triggers**: `SURGERY_IMAGES_CEA` (before insert or update or delete), `TRG_WS_KWD_UL_UP_Q` (after insert or update or delete)

## DEFINITIONS.SURGERY_REGIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| SURGERY_REGION_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(200) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| CLINIC_SPECIALITY_ID | VARCHAR2(6) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_SURGERY_REGIONS`: SURGERY_REGION_ID, LOCATION_ID
- **CHECK** `CK_SURGERY_REGIONS_1`: ACTIVE IN ('Y','N'
- **Triggers**: `SURGERY_REGIONS_CEA` (before insert or update or delete), `SURGERY_REGIONS_DEL` (after delete), `SURGERY_REGIONS_INS` (before insert), `SURGERY_REGIONS_INSERT` (before insert), `SURGERY_REGIONS_UPD` (before update), `TRG_WS_XPV_AF_DN_Q` (after insert or update or delete)

## DEFINITIONS.SURGERY_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | VARCHAR2(3) | N | Antibiotics Main Group |
| SUB_GROUP_ID | VARCHAR2(3) | N | Antibiotics Sub Group |
| PAT_SECTION_ID | VARCHAR2(10) | Y | Pathalogy Microbiology Section for SSI |

- **PK** `PK_SURGERY_SETUP`: GROUP_ID, SUB_GROUP_ID

## DEFINITIONS.SYMPOSIUM_USER_TITLE

| Column | Type | Null | Comment |
|---|---|---|---|
| SEX_ID | NUMBER(1) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_SYMPOSIUM_USER_TITLE`: SEX_ID

## DEFINITIONS.SYMPTOMS_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| SYMPTOM_ID | NUMBER(4) | N |  |
| PARAMETER_ID | NUMBER | N |  |
| ACTIVE | CHAR(1) | Y |  |
| ORDER_BY | NUMBER | Y |  |

- **PK** `PK_SYMPTOMS_PARAMETERS`: SYMPTOM_ID, PARAMETER_ID
- **Triggers**: `SYMPTOMS_PARAMETERS_DEL` (after delete), `SYMPTOMS_PARAMETERS_INS` (before insert), `SYMPTOMS_PARAMETERS_UPD` (before update)

## DEFINITIONS.SYSTEM_CONSTANTS_DEF

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(10000) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| MODULE_ID | VARCHAR2(3) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| CONSTANT_LEVEL | VARCHAR2(1) default 'O' | Y | column used to set the status of constant level.O for organizaiton, L for Location |
| CONSTANT_TYPE_ID | NUMBER default 1 | Y |  |
| PURPOSE | VARCHAR2(4000) | Y |  |

- **PK** `PK_SYSTEM_CONSTANTS`: CONSTANT_ID
- **Triggers**: `SYSTEM_CONSTANTS_DEF_CEA` (before insert or update or delete), `SYSTEM_CONSTANTS_DEF_DEL` (after delete), `SYSTEM_CONSTANTS_DEF_INS` (before insert), `SYSTEM_CONSTANTS_DEF_UPD` (before update), `SYSTEM_CONSTANTS_STOP_DEL` (after delete), `TRG_WS_PTH_BO_BK_Q` (after insert or update or delete)

## DEFINITIONS.SYSTEM_CONSTANTS_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LOCATION_ID | VARCHAR2(3) | Y |  |
| CONSTANT_ID | NUMBER(4) | N |  |
| VALUE | VARCHAR2(2000) | Y |  |
| VALUE_UNIT_ID | VARCHAR2(5) | Y |  |
| VALUE_TYPE | VARCHAR2(100) | Y |  |
| BACKEND_SOURCE | VARCHAR2(100) | Y |  |
| RUNTIME_CALCULATE | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| SERIAL_NO | NUMBER(5) | N |  |
| ORGANIZATION_ID | VARCHAR2(3) | N |  |
| EFFECTIVE_DATE | DATE | Y |  |

- **PK** `PK_SYSTEM_CONSTANTS_SETUP`: CONSTANT_ID, SERIAL_NO
- **FK** `FK_SYSTEM_CONSTANT_SETUP`: (CONSTANT_ID) -> DEFINITIONS.SYSTEM_CONSTANTS_DEF(CONSTANT_ID)
- **Triggers**: `SYSTEM_CONSTANTS_SETUP_DEL` (after delete), `SYSTEM_CONSTANTS_SETUP_INS` (before insert), `SYSTEM_CONSTANTS_SETUP_UPD` (before update), `UPDATE_EFFECTIVE_DATE` (before update)

## DEFINITIONS.SYSTEM_CONSTANTS_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(4) | N |  |
| PARAM_ID | NUMBER(2) | N |  |
| PARAM_NAME | VARCHAR2(100) | N |  |
| PARAM_TYPE | VARCHAR2(30) | N |  |
| PARAM_DATA_TYPE | VARCHAR2(100) | N |  |
| PARAM_DEFAULT_VALUE | VARCHAR2(100) | Y |  |
| PARAM_SEQUENCE | NUMBER | N |  |
| SERIAL_NO | NUMBER(5) | N |  |

- **PK** `PK_SYSTEM_CONSTANTS_PARAMETERS`: CONSTANT_ID, SERIAL_NO, PARAM_ID
- **FK** `FK_SYSTEM_CONSTANTS_SETUP`: (CONSTANT_ID, SERIAL_NO) -> DEFINITIONS.SYSTEM_CONSTANTS_SETUP(CONSTANT_ID, SERIAL_NO)
- **Triggers**: `SYN_SYSTEM_CONST_PARAM_DEL` (after delete), `SYN_SYSTEM_CONST_PARAM_INS` (before insert), `SYN_SYSTEM_CONST_PARAM_UPD` (before update), `SYSTEM_CONSTANTS_PARAMETERS_DEL` (after delete), `SYSTEM_CONSTANTS_PARAMETERS_UPD` (before update)

## DEFINITIONS.SYSTEM_CONSTANTS_SETUP_USER

| Column | Type | Null | Comment |
|---|---|---|---|
| CONSTANT_ID | NUMBER(4) | N |  |
| SERIAL_NO | NUMBER(5) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| VALUE | VARCHAR2(100) | N |  |
| VALUE_UNIT_ID | VARCHAR2(5) | Y |  |
| VALUE_TYPE | VARCHAR2(20) | Y |  |
| ACTIVE | VARCHAR2(1) default 'N' | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_SYSTEM_CONSTANTS_SETUP_USER`: CONSTANT_ID, SERIAL_NO, MRNO
- **Triggers**: `SYN_SYSTEM_CONSTANTS_USER_DEL` (after delete), `SYN_SYSTEM_CONSTANTS_USER_INS` (before insert), `SYN_SYSTEM_CONSTANTS_USER_UPD` (before update), `TRG_WS_IKD_AY_TF_Q` (after insert or update or delete)

## DEFINITIONS.SYSTEM_CURRENT_YEAR

| Column | Type | Null | Comment |
|---|---|---|---|
| CURRENT_YEAR | VARCHAR2(2) | N |  |

- **PK** `PK_SYSTEM_CURRENT_YEAR`: CURRENT_YEAR
- **Triggers**: `SYSTEM_CURRENT_YEAR_CEA` (before insert or update or delete), `TRG_WS_QCM_JR_XW_Q` (after insert or update or delete)

## DEFINITIONS.TABLE_TYPES
'T' Transaction, 'D' Location Setup, 'S' System Setup, 'O' Organizational Setup, 'Q' Transaction_Setup_Query_Required_to_Copy_data;

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_TYPE_ID | CHAR(1) | N |  |
| TABLE_TYPE_DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_TABLE_TYPES`: TABLE_TYPE_ID
- **UK** `UK_TABLE_TYPES_01`: TABLE_TYPE_DESCRIPTION
- **CHECK** `CK_TABLE_TYPES_01`: TABLE_TYPE_ID = UPPER(TABLE_TYPE_ID

## DEFINITIONS.TTMT_MATRIX

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_TYPE_ID | CHAR(1) | N |  |
| MODEL_TYPE_ID | NUMBER(2) | N |  |

- **PK** `PK_TTMT_MATRIX`: TABLE_TYPE_ID, MODEL_TYPE_ID
- **FK** `FK_TTMT_MATRIX_01`: (TABLE_TYPE_ID) -> DEFINITIONS.TABLE_TYPES(TABLE_TYPE_ID)
- **FK** `FK_TTMT_MATRIX_02`: (MODEL_TYPE_ID) -> DEFINITIONS.DATA_SYNC_MODEL_TYPES(MODEL_TYPE_ID) [disabled]

## DEFINITIONS.TABLES

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(60) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | N |  |
| USELESS_FLAG | CHAR(1) | N |  |
| AUDITING_CHECKED | CHAR(1) | Y |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |
| REQUIRED_ON_NEW_LOCATION | CHAR(1) | Y |  |
| PROCEDURE_NAME | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| TABLE_LEVEL | NUMBER(4) | Y |  |
| MODEL_TYPE_ID | NUMBER(2) | Y |  |
| OWNER | VARCHAR2(60) | N |  |
| IS_NOT_A_COLLECTION_CENTRE | CHAR(1) | Y | CC TYPE |
| IS_FRANCHISED_COLLECTION_CNTR | CHAR(1) | Y | CC TYPE |
| IS_SKM_COLLECTION_CNTR | CHAR(1) | Y | CC TYPE |
| IS_KIOSKS_CENTRE | CHAR(1) | Y | CC TYPE |
| WT_TRIGGER_REQUIRED | CHAR(1) default 'N' | Y |  |
| OLD_TABLE_ID | VARCHAR2(4) | Y |  |

- **PK** `PK_TABLES_01`: SCHEMA_ID, TABLE_ID
- **UK** `UK_TABLES_01`: OWNER, NAME
- **FK** `FK_TABLES_01`: (OWNER) -> DEFINITIONS.SCHEMAS(NAME)
- **FK** `FK_TABLES_02`: (MODEL_TYPE_ID) -> DEFINITIONS.DATA_SYNC_MODEL_TYPES(MODEL_TYPE_ID) [disabled]
- **FK** `FK_TABLES_03`: (TABLE_TYPE_FLAG) -> DEFINITIONS.TABLE_TYPES(TABLE_TYPE_ID) [disabled]
- **FK** `FK_TABLES_04`: (TABLE_TYPE_FLAG, MODEL_TYPE_ID) -> DEFINITIONS.TTMT_MATRIX(TABLE_TYPE_ID, MODEL_TYPE_ID) [disabled]
- **CHECK** `CK_TABLE_03`: NAME = UPPER(NAME
- **Triggers**: `TABLES_TRG` (before insert or update), `TRG_WS_TAZ_CS_MU_Q` (after insert or update or delete)

## DEFINITIONS.TABLES_FMH

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| TABLE_ID | VARCHAR2(4) | Y |  |
| NAME | VARCHAR2(30) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | Y |  |
| USELESS_FLAG | CHAR(1) | Y |  |
| AUDITING_CHECKED | CHAR(1) | N |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |
| REQUIRED_ON_NEW_LOCATION | CHAR(1) | Y |  |
| PROCEDURE_NAME | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| TABLE_LEVEL | NUMBER(4) | Y |  |


## DEFINITIONS.TABLES_HIERARCY

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_NAME | VARCHAR2(60) | Y |  |
| TABLE_LEVEL | NUMBER(5) | Y |  |
| TABLE_ORDER | NUMBER(10) | Y |  |
| PARENT_TABLE_NAME | VARCHAR2(60) | Y |  |
| PARENT_TABLE_LEVEL | NUMBER(5) | Y |  |
| PARENT_TABLE_ORDER | NUMBER(10) | Y |  |
| ROWNUMBER | NUMBER | Y |  |
| BASE_TABLE_NAME | VARCHAR2(60) | Y |  |
| SR_NO | NUMBER(9) | Y |  |

- **PK** `PK_TABLES_HIERARCY`: SR_NO
- **Triggers**: `TABLES_HIERARCY_UPDATE` (before insert)

## DEFINITIONS.TABLES_JBC_R

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(30) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | Y |  |
| USELESS_FLAG | CHAR(1) | Y |  |
| AUDITING_CHECKED | CHAR(1) | N |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |
| REQUIRED_ON_NEW_LOCATION | CHAR(1) | Y |  |
| PROCEDURE_NAME | VARCHAR2(200) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| TABLE_LEVEL | NUMBER(4) | Y |  |


## DEFINITIONS.TABLES_MASTER_DETAIL_HIERARCY

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_NAME | VARCHAR2(60) | Y |  |
| TABLE_LEVEL | NUMBER(5) | Y |  |
| TABLE_ORDER | NUMBER(10) | Y |  |
| PARENT_TABLE_NAME | VARCHAR2(60) | Y |  |
| PARENT_TABLE_LEVEL | NUMBER(5) | Y |  |
| PARENT_TABLE_ORDER | NUMBER(10) | Y |  |
| ROWNUMBER | NUMBER | Y |  |


## DEFINITIONS.TABLES_OVERALL_HIERARCHY

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_NAME | VARCHAR2(100) | N |  |
| TABLE_ORDER | NUMBER | Y |  |

- **PK** `PK_TABLES_OVERALL_HIERARCHY`: TABLE_NAME
- **UK** `UK_TABLES_OVERALL_HIERARCHY_001`: TABLE_ORDER

## DEFINITIONS.TABLES_PARENTS_HIERARCY

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_NAME | VARCHAR2(60) | Y |  |
| TABLE_LEVEL | NUMBER(5) | Y |  |
| TABLE_ORDER | NUMBER(10) | Y |  |
| CHILD_TABLE_NAME | VARCHAR2(60) | Y |  |
| CHILD_TABLE_LEVEL | NUMBER(5) | Y |  |
| CHILD_TABLE_ORDER | NUMBER(10) | Y |  |
| ROWNUMBER | NUMBER | Y |  |
| BASE_TABLE_NAME | VARCHAR2(60) | Y |  |

- **PK** `PK_TABLE_PARENT_HIER`: BASE_TABLE_NAME, TABLE_NAME, CHILD_TABLE_NAME, TABLE_LEVEL, TABLE_ORDER

## DEFINITIONS.TABLES_PIC

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(60) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | N |  |
| USELESS_FLAG | CHAR(1) | N |  |
| AUDITING_CHECKED | CHAR(1) | N |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |
| REQUIRED_ON_NEW_LOCATION | CHAR(1) | Y |  |
| PROCEDURE_NAME | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| TABLE_LEVEL | NUMBER(4) | Y |  |
| MODEL_TYPE_ID | NUMBER(2) | Y |  |
| OWNER | VARCHAR2(60) | N |  |


## DEFINITIONS.TABLES_SIUT

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| NAME | VARCHAR2(60) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | N |  |
| USELESS_FLAG | CHAR(1) | N |  |
| AUDITING_CHECKED | CHAR(1) | N |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |
| REQUIRED_ON_NEW_LOCATION | CHAR(1) | Y |  |
| PROCEDURE_NAME | VARCHAR2(4000) | Y |  |
| ORDER_BY | NUMBER(4) | Y |  |
| TABLE_LEVEL | NUMBER(4) | Y |  |
| MODEL_TYPE_ID | NUMBER(2) | Y |  |
| OWNER | VARCHAR2(60) | N |  |


## DEFINITIONS.TABLES_TEST_R

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| TABLE_ID | VARCHAR2(4) | Y |  |
| NAME | VARCHAR2(30) | N |  |
| TABLE_TYPE_FLAG | CHAR(1) | Y |  |
| USELESS_FLAG | CHAR(1) | Y |  |
| AUDITING_CHECKED | CHAR(1) | N |  |
| WHERE_CLAUSE | VARCHAR2(4000) | Y |  |
| WHERE_CLAUSE_2 | VARCHAR2(4000) | Y |  |


## DEFINITIONS.TABLE_COLUMNS

| Column | Type | Null | Comment |
|---|---|---|---|
| SCHEMA_ID | VARCHAR2(3) | N |  |
| TABLE_ID | VARCHAR2(4) | N |  |
| COLUMN_NAME | VARCHAR2(30) | Y |  |
| COUNTER_COLUMN | CHAR(1) default 'N' | N |  |
| COLUMN_ID | VARCHAR2(5) | N |  |
| DATA_TYPE | VARCHAR2(30) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| USER_DEFINED_DESCRIPTION | VARCHAR2(500) | Y |  |

- **PK** `PK_TABLE_COLUMNS`: SCHEMA_ID, TABLE_ID, COLUMN_ID
- **CHECK** `CHK_TABLE_COLUMNS_1`: COUNTER_COLUMN IN ('Y','N'
- **Triggers**: `TABLE_COLUMNS_CEA` (before insert or update or delete), `TABLE_COLUMNS_DEL` (after delete), `TABLE_COLUMNS_INS` (before insert), `TABLE_COLUMNS_UPD` (before update), `TRG_WS_FOJ_CU_AB_Q` (after insert or update or delete)

## DEFINITIONS.TABLE_NAME

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_NAME | VARCHAR2(500) | Y |  |

_No standard audit columns._


## DEFINITIONS.TABLE_TIME_STAMP

| Column | Type | Null | Comment |
|---|---|---|---|
| TABLE_ID | NUMBER(4) | N |  |
| TABLE_NAME | VARCHAR2(50) | N |  |
| TIME_STAMP | DATE | N |  |

- **PK** `PK_TABLE_TIME_STAMP`: TABLE_ID
- **UK** `UK_TABLE_TIME_STAMP_1`: TABLE_ID, TABLE_NAME
- **FK** `FK_TABLE_TIME_STAMP_1`: (TABLE_ID) -> DEFINITIONS.TABLE_MAPPING(TABLE_ID)
- **FK** `FK_TABLE_TIME_STAMP_2`: (TABLE_NAME) -> DEFINITIONS.CC_SOURCE_TABLES(SOURCE_TABLE) [disabled]
- **CHECK** `CHK_TABLE_TIME_STAMP_1`: TABLE_NAME = UPPER(TABLE_NAME
- **Triggers**: `TABLE_TIME_STAMP_CEA` (before insert or update or delete), `TRG_WS_EGB_BQ_IT_Q` (after insert or update or delete)

## DEFINITIONS.TAX_PAYMENT_SECTIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| TAX_RATE | NUMBER | N |  |
| PAYMENT_SECTION | VARCHAR2(25) | N |  |
| PAYMENT_SEC_MONTH | VARCHAR2(25) | Y |  |
| PAYMENT_NATURE | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| TAX_RATE_NF | NUMBER | Y | This column is used to save tax rate of non filer |

- **PK** `PK_TAX_PAYMENT_SECTIONS`: TAX_RATE, PAYMENT_SECTION
- **Triggers**: `TAX_PAYMENT_SECTIONS_DEL` (after delete), `TAX_PAYMENT_SECTIONS_INS` (before insert), `TAX_PAYMENT_SECTIONS_UPD` (before update)

## DEFINITIONS.TECHNICIAN

| Column | Type | Null | Comment |
|---|---|---|---|
| TECH_ID | VARCHAR2(7) | N |  |
| TECH_NAME | VARCHAR2(55) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_TECHNICIAN`: TECH_ID

## DEFINITIONS.TEHSIL_AREA

| Column | Type | Null | Comment |
|---|---|---|---|
| AREA_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |
| OFFICE_ID | NUMBER(3) | Y |  |

- **PK** `PK_TEHSIL_AREA`: AREA_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID
- **FK** `FK_TEHSIL_AREA`: (COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) -> DEFINITIONS.TEHSIL(COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID) [disabled]
- **Triggers**: `TEHSIL_AREA_CEA` (before insert or update or delete), `TEHSIL_AREA_TS` (before insert or update or delete), `TRG_WS_ZED_WT_HK_Q` (after insert or update or delete)

## DEFINITIONS.TEHSIL_SUB_AREA

| Column | Type | Null | Comment |
|---|---|---|---|
| SUB_AREA_ID | NUMBER(7) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| AREA_ID | NUMBER(4) | N |  |
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |

- **PK** `PK_TEHSIL_SUB_AREA`: SUB_AREA_ID, AREA_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID
- **Triggers**: `TEHSIL_SUB_AREA_DEL` (after delete), `TEHSIL_SUB_AREA_INS` (before insert), `TEHSIL_SUB_AREA_UPD` (before update)

## DEFINITIONS.TEHSIL_ZONE

| Column | Type | Null | Comment |
|---|---|---|---|
| COUNTRY_ID | NUMBER(4) | N |  |
| STATE_ID | NUMBER(4) | N |  |
| DISTRICT_ID | NUMBER(4) | N |  |
| TEHSIL_ID | NUMBER(4) | N |  |
| NAME | VARCHAR2(60) | Y |  |
| CBR_CITY_CODE | NUMBER(11) | Y |  |
| CALLING_CODE | NUMBER(6) | Y |  |
| SUB_AREA_REQUIRED | CHAR(1) | Y |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| NEW_COUNTRY_ID | NUMBER(4) | Y |  |

- **PK** `PK_TEHSIL_ZONE`: ZONE_ID, COUNTRY_ID, STATE_ID, DISTRICT_ID, TEHSIL_ID

## DEFINITIONS.TEMPLATE_GROUPS

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_ID | NUMBER | N |  |
| NAME | VARCHAR2(255) | Y |  |
| DESCRIPTION | VARCHAR2(2000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TEMPLATE_GROUPS`: GROUP_ID

## DEFINITIONS.TEMPLATE_GROUP_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_TYPE_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TEMPLATE_GROUP_TYPES`: GROUP_TYPE_ID
- **Triggers**: `TEMPLATE_GROUP_TYPES_DEL` (after delete), `TEMPLATE_GROUP_TYPES_INS` (before insert), `TEMPLATE_GROUP_TYPES_UPD` (before update)

## DEFINITIONS.TEMPLATE_IMAGES

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_ID | VARCHAR2(6) | N |  |
| IMAGE_ID | NUMBER | N |  |
| IMAGE | BLOB | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_TEMPLATE_IMAGES`: TEMPLATE_ID, IMAGE_ID, LOCATION_ID
- **FK** `FK_TEMPLATE_IMAGES_1`: (TEMPLATE_ID, LOCATION_ID) -> ORDERENTRY.NOTE_TEMPLATE_MASTER(TEMPLATE_ID, LOCATION_ID) [disabled]
- **Triggers**: `TEMPLATE_IMAGES_DEL` (after delete), `TEMPLATE_IMAGES_INS` (before insert), `TEMPLATE_IMAGES_UPD` (before update)

## DEFINITIONS.TEMPLATE_TYPES

| Column | Type | Null | Comment |
|---|---|---|---|
| TEMPLATE_TYPE_ID | VARCHAR2(7) | N |  |
| DESCRIPTION | VARCHAR2(300) | Y |  |
| MODULE_NAME | VARCHAR2(100) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| REMARKS | VARCHAR2(1000) | Y |  |

- **PK** `PK_TEMPLATE_TYPES`: TEMPLATE_TYPE_ID
- **Triggers**: `TEMPLATE_TYPES_CEA` (before insert or update or delete), `TRG_WS_MBK_EJ_TU_Q` (after insert or update or delete)

## DEFINITIONS.TEMP_CPT
This table was created on temporary basis and will be dropped soon when CPTs will be synchronized

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | N |  |
| DESCRIPTION | VARCHAR2(250) | Y |  |
| CPT_CATEGORY_ID | VARCHAR2(7) | Y |  |
| CPT_TYPE | VARCHAR2(1) | Y |  |
| PRICE | NUMBER(12,2) | Y |  |
| CPT_BONUS | VARCHAR2(1) | Y |  |
| EMPLOYEE_ENTITLEMENT | VARCHAR2(1) | Y |  |
| IN_HOUSE_PERFORMED | VARCHAR2(1) | Y |  |
| COST | NUMBER(12,2) | Y |  |
| DOCTOR_SHARE_TYPE | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| SHORT_DESC | VARCHAR2(60) | Y |  |
| CONSULTANCY | VARCHAR2(1) | Y |  |
| STAT_CHARGEABLE | VARCHAR2(1) default 'N' | Y |  |
| CLEARANCE | VARCHAR2(1) default 'N' | Y |  |
| MOST_COMMONLY_USED | VARCHAR2(1) default 'N' | Y |  |
| NO_OF_PROCEDURES | NUMBER(2) default 1 | Y |  |
| REP_ORDER | NUMBER(10) | Y |  |
| PAT_REPORT_CATEGORY_ID | VARCHAR2(3) | Y |  |
| DOCTOR_REQUIRED | VARCHAR2(1) default 'N' | Y |  |
| PATHOLOGY_COMMENT_TYPE_ID | VARCHAR2(3) | Y |  |
| MAX_QUANTITY_ALLOWED | VARCHAR2(1) default 'N' | Y |  |
| REPORTING_CASE | NUMBER(2) | Y |  |
| NO_OF_REPORTS | NUMBER(2) | Y |  |
| DUPLICATE_ACKNOWLEDGE | VARCHAR2(1) default 'Y' | Y |  |
| SPECIMEN_NATURE_REQUIRED | CHAR(1) default 'N' | Y |  |
| SPECIMEN_SITE_REQUIRED | CHAR(1) default 'N' | Y |  |
| WORK_ORDER_PRINT | CHAR(1) default 'Y' | Y |  |
| TECH_NORMAL | CHAR(1) default 'N' | Y |  |
| TECH_ABNORMAL | CHAR(1) default 'N' | Y |  |
| DOCTOR_NORMAL | CHAR(1) default 'N' | Y |  |
| DOCTOR_ABNORMAL | CHAR(1) default 'N' | Y |  |
| CONSULTANT_NORMAL | CHAR(1) default 'N' | Y |  |
| NOT_REPORTABLE | CHAR(1) default 'N' | Y |  |
| CONSULTANT_ABNORMAL | CHAR(1) default 'N' | Y |  |
| COMBINED_REPORT | CHAR(1) default 'N' | Y |  |
| REPORT_HEADING | VARCHAR2(100) | Y |  |
| SPECIALITY_ID | VARCHAR2(6) | Y |  |
| SURGERY_REGION_ID | VARCHAR2(5) | Y |  |
| LENGTH_OF_STAY | NUMBER(2) default 0 | Y |  |
| AFTER_DEATH_ENTRY | CHAR(1) | Y |  |
| OPEN_PRICE | CHAR(1) default 'N' | Y |  |
| PERFORM_LOCATION_ID | VARCHAR2(3) default '001' | Y |  |
| MODALITY_ID | VARCHAR2(10) | Y |  |
| ACK_PERFORMANCE_REQ | CHAR(1) default 'Y' | Y |  |
| IMAGE_REQUIRED | VARCHAR2(1) default 'N' | Y |  |
| SHARE_ON_PERFORM | CHAR(1) | Y |  |
| EFFECTIVE_DATE | DATE | Y |  |
| ACTIVATED_DATE | DATE | Y |  |
| REMARKS | VARCHAR2(255) | Y |  |
| USER_DEFINED_DEPT | CHAR(1) default 'N' | Y |  |
| COMBINED_REPORT_NORMAL | CHAR(1) default 'N' | Y |  |
| COMBINED_REPORT_ABNORMAL | CHAR(1) default 'N' | Y |  |
| BLOCK_AUTO_INP_INVOICE | CHAR(1) default 'Y' | Y |  |
| PRE_REQUISITES_CHK | CHAR(1) | Y |  |
| INITIALIZED_YN | CHAR(1) default 'N' | Y |  |
| CPT_CATEGORY_ID_NEW | VARCHAR2(7) | Y |  |
| INITIALIZED_DATE | DATE | Y |  |
| LONG_DESC | VARCHAR2(4000) | Y |  |
| DEFAULT_DOCTOR | VARCHAR2(18) | Y |  |
| CONSENT_TYPE | CHAR(1) default 'N' | Y |  |
| LIMITED_IMAGES | CHAR(1) default 'Y' | Y |  |
| PI_CONSIDERATION | CHAR(1) default 'P' | Y |  |
| CONSULTANT_ONLY | CHAR(1) default 'N' | Y |  |
| LAST_ORDER_VALUE_INHOUR | NUMBER(5) default 0 | Y |  |
| NO_OF_IMAGES | NUMBER(3) default 0 | Y |  |
| ORDER_RESTRICTION | CHAR(1) default 'Y' | Y |  |
| EAR_ALLOWED | CHAR(1) | Y |  |
| CLINICAL_REPORT | CHAR(1) default 'N' | Y |  |
| CONTRAST | CHAR(1) default 'N' | Y |  |
| MANUAL_PERFROMACE | CHAR(1) | Y |  |
| ASSESSMENT_REQUIRED | CHAR(1) default 'Y' | Y |  |
| FORMAT_ID | VARCHAR2(6) | Y |  |
| OPEN_QUANTITY | CHAR(1) default 'N' | Y |  |
| INCLUDE_IN_CONTRACT_BY_DEFAULT | CHAR(1) default 'Y' | Y |  |
| NATURE_ID | VARCHAR2(3) | Y |  |
| NATURE_DETAIL_ID | VARCHAR2(3) | Y |  |
| INVOICE_STATUS_ID | VARCHAR2(3) default '002' | Y |  |
| NEW_CPT_ID | VARCHAR2(18) | Y |  |

- **PK** `PK_TEMP_CPT`: CPT_ID
- **UK** `UK_TEMP_CPT_1`: NEW_CPT_ID

## DEFINITIONS.TEMP_LOCATION_ID

| Column | Type | Null | Comment |
|---|---|---|---|
| P_ID | VARCHAR2(14) | Y |  |
| P_NAME | VARCHAR2(100) | Y |  |


## DEFINITIONS.TEMP_PARAM_RG

| Column | Type | Null | Comment |
|---|---|---|---|
| RG_COLUMN_ID | VARCHAR2(100) | Y |  |
| RG_COLUMN_DESC | VARCHAR2(300) | Y |  |


## DEFINITIONS.TENDER_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TENDER_TYPE_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_TENDER_TYPE`: TENDER_TYPE_ID
- **Triggers**: `TENDER_TYPE_CEA` (before insert or update or delete), `TENDER_TYPE_DEL` (after delete), `TENDER_TYPE_INS` (before insert), `TENDER_TYPE_UPD` (before update), `TRG_WS_RZW_FU_IA_Q` (after insert or update or delete)

## DEFINITIONS.TERMINALS

| Column | Type | Null | Comment |
|---|---|---|---|
| TERMINAL_ID_OLD | VARCHAR2(15) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| NAME | VARCHAR2(30) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PRINTER_ID | VARCHAR2(6) | Y |  |
| OLD_IP_ADDRESS | VARCHAR2(15) | Y |  |
| RIS_TERMINAL | CHAR(1) default 'N' | Y |  |
| AP_TERMINAL_ID | VARCHAR2(7) | Y |  |
| CONTINGENCY_FLAG | CHAR(1) default 'N' | Y |  |
| APP_CONVRT_NXT_VER | CHAR(1) default 'N' | N |  |
| IP_ADDRESS | VARCHAR2(15) | Y |  |
| JDK_STATUS | CHAR(1) default 'N' | Y | To check java status (JDK) for rendering images from terminal |
| NETWORK_CONTINGENCY | CHAR(1) default 'N' | Y | This column contains Y/N. If Y is selected then IP ADDRESS authentication will be by passed at time of HIS login |
| TERMINAL_ID | VARCHAR2(15) | N | PK of table according to the new format |

- **PK** `PK_TERMINALS1`: TERMINAL_ID
- **UK** `UK_TERMINAL_NAME`: NAME
- **FK** `FK_S01_T016_S01_T067_1`: (LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.ORDER_LOCATION(LOCATION_ID, ORDER_LOCATION_ID)
- **CHECK** `CHK_TERMINALS_2`: NETWORK_CONTINGENCY IN ('N','Y'
- **CHECK** `CHK_TERMINALS_JDK`: JDK_STATUS IN ('N','Y'
- **Triggers**: `TERMINALS_DEL` (after delete), `TERMINALS_INS` (before insert), `TERMINALS_UPD` (before update)

## DEFINITIONS.TERMINAL_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TERMINAL_TYPE_ID | VARCHAR2(15) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |

- **PK** `PK_TERMINAL_TYPE`: TERMINAL_TYPE_ID
- **Triggers**: `TERMINAL_TYPE_CEA` (before insert or update or delete), `TERMINAL_TYPE_DEL` (after delete), `TERMINAL_TYPE_INS` (before insert), `TERMINAL_TYPE_UPD` (before update), `TRG_WS_TGG_QI_CP_Q` (after insert or update or delete)

## DEFINITIONS.TERMINAL_WISE_DISPLAY_SETTINGS

| Column | Type | Null | Comment |
|---|---|---|---|
| PC_ID_OLD | VARCHAR2(30) | Y |  |
| DISPLAY_ID | NUMBER | N |  |
| PC_ID | VARCHAR2(15) | N |  |

- **PK** `TERMINAL_WISE_DISPLAY_PK`: DISPLAY_ID, PC_ID
- **FK** `TERMINAL_WISE_DISPLAY_FK2`: (DISPLAY_ID) -> DEFINITIONS.SCREEN_DISPLAY_MASTER(DISPLAY_ID)
- **Triggers**: `TERMINL_WISE_DIS_SET_DEL` (after delete), `TERMINL_WISE_DIS_SET_INS` (before insert), `TERMINL_WISE_DIS_SET_UPD` (before update)

## DEFINITIONS.TERMINOLOGY

| Column | Type | Null | Comment |
|---|---|---|---|
| TERM_ID | VARCHAR2(12) | N | This column contains Unique Terminology ID |
| TERM_NAME | VARCHAR2(50) | N | This column contains Short name of Terminology |
| TERM_DESC | VARCHAR2(200) | Y | This column contains Long description of Terminology |
| ACTIVE | CHAR(1) | Y | This column contains Flag Information of Status (Y=Active, N=Inactive) |

- **Triggers**: `TERMINOLOGY_DEL` (after delete), `TERMINOLOGY_INS` (before insert), `TERMINOLOGY_UPD` (before update)

## DEFINITIONS.TERRITORY
This table will be used to define the Territories within an organization

| Column | Type | Null | Comment |
|---|---|---|---|
| TERRITORY_KEY | NUMBER(3) | N |  |
| TERRITORY_NAME | VARCHAR2(60) | N |  |
| TERRITORY_SHORT_NAME | VARCHAR2(10) | N |  |
| TERRITORY_DISPLAY_NAME | VARCHAR2(60) | N |  |
| TERRITORY_DISPLAY_ORDER | NUMBER(3) | N |  |

- **PK** `PK_TERRITORY`: TERRITORY_KEY
- **UK** `UK_TERRITORY_1`: TERRITORY_NAME
- **UK** `UK_TERRITORY_2`: TERRITORY_DISPLAY_ORDER
- **Triggers**: `TERRITORY_DEL` (after delete), `TERRITORY_INS` (before insert), `TERRITORY_UPD` (before update)

## DEFINITIONS.TERRITORY_ZONE_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| TERRITORY_ZONE_LOCATION_KEY | NUMBER(5) | N |  |
| TRANS_DATE | DATE | N |  |
| TERRITORY_KEY | NUMBER(3) | N |  |
| ZONE_ID | VARCHAR2(3) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |

- **PK** `PK_TERRITORY_ZONE_LOCATION`: TERRITORY_ZONE_LOCATION_KEY
- **FK** `FK_TERRITORY_ZONE_LOCATION_1`: (TERRITORY_KEY) -> DEFINITIONS.TERRITORY(TERRITORY_KEY)
- **FK** `FK_TERRITORY_ZONE_LOCATION_2`: (ZONE_ID) -> DEFINITIONS.ZONES(ZONE_ID)
- **FK** `FK_TERRITORY_ZONE_LOCATION_3`: (LOCATION_ID) -> DEFINITIONS.LOCATION(LOCATION_ID)
- **CHECK** `CK_TERRITORY_ZONE_LOCATION_1`: END_DATE>START_DATE
- **Triggers**: `TERRITORY_ZONE_LOCATION_DEL` (after delete), `TERRITORY_ZONE_LOCATION_INS` (before insert), `TERRITORY_ZONE_LOCATION_UPD` (before update)

## DEFINITIONS.TESTING

| Column | Type | Null | Comment |
|---|---|---|---|
| CLIENT_ID | VARCHAR2(10) | N |  |
| CPT_ID | VARCHAR2(18) | N |  |
| PRICE | NUMBER(12,2) | N |  |


## DEFINITIONS.TEST_MERGE

| Column | Type | Null | Comment |
|---|---|---|---|
| MARITAL_STATUS_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| STATUS | VARCHAR2(1) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| MARRIED_STATUS | VARCHAR2(1) | Y |  |

- **PK** `PK_TEST`: MARITAL_STATUS_ID

## DEFINITIONS.TIMESTAMP_VALUES

| Column | Type | Null | Comment |
|---|---|---|---|
| DESCRIPTION | VARCHAR2(5) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |


## DEFINITIONS.TITLE

| Column | Type | Null | Comment |
|---|---|---|---|
| TITLE_ID | NUMBER(4) | N |  |
| DESCRIPTION | VARCHAR2(255) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_TITLE`: TITLE_ID

## DEFINITIONS.TOKEN_DISPLAY_COUNTER_MASTER

| Column | Type | Null | Comment |
|---|---|---|---|
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |

- **PK** `PK_TOKEN_DISPLAY_COUNTER_MAST`: TERMINAL, LOCATION_ID

## DEFINITIONS.TOKEN_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| TOKEN_TYPE_ID | NUMBER(16) | N |  |
| TOKEN_TYPE_DESCRIPTION | VARCHAR2(50) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| BUTTON_LABEL | NVARCHAR2(30) | Y |  |
| BUTTON_DESCRIPTION | NVARCHAR2(100) | Y |  |
| MRNO_IS_REQUIRED | CHAR(1) | Y |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| BUTTON_LABEL_URDU | NVARCHAR2(30) | Y |  |
| BUTTON_IMAGE | BLOB | Y |  |
| SHOW_CLINIC_NAME | CHAR(1) default 'N' | Y | To show clinic name on display screen button |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| IS_OPTIONAL | CHAR(1) | Y |  |

- **PK** `PK_TOKEN_TYPE`: TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID
- **FK** `FK_TOKEN_TYPE`: (DEPARTMENT_ID) -> DEFINITIONS.DEPARTMENT(DEPARTMENT_ID) [disabled]
- **Triggers**: `TOKEN_TYPE_CEA` (before insert or update or delete), `TOKEN_TYPE_DEL` (after delete), `TOKEN_TYPE_INS` (before insert), `TOKEN_TYPE_UPD` (before update), `TRG_WS_IIA_NK_QX_Q` (after insert or update or delete)

## DEFINITIONS.TOKEN_TYPE_DISPLAY_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| TOKEN_TYPE_ID | NUMBER(16) | N |  |
| ACTIVE | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| PROMPT_TEXT | VARCHAR2(100) | Y |  |

- **PK** `PK_TOK_TYPE_DISP_COUNTER`: TERMINAL, TOKEN_TYPE_ID
- **FK** `FK_TOK_TYPE_DISP_COUNT_1`: (TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.TOKEN_TYPE(TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID) [disabled]
- **FK** `FK_TOK_TYPE_DISP_COUNT_2`: (TERMINAL, LOCATION_ID) -> DEFINITIONS.TOKEN_DISPLAY_COUNTER_MASTER(TERMINAL, LOCATION_ID) [disabled]

## DEFINITIONS.TOKEN_DISPLAY_COUNTER

| Column | Type | Null | Comment |
|---|---|---|---|
| TERMINAL_NAME | VARCHAR2(60) | N |  |
| ORDER_BY | NUMBER(3) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| TOKEN_TYPE_ID | NUMBER(16) | N |  |
| PARENT_TERMINAL_NAME | VARCHAR2(60) | Y |  |
| TERMINAL_DESCRIPTION | VARCHAR2(100) | Y |  |
| PROMPT_TEXT | VARCHAR2(100) | Y |  |
| IP_ADDRESS | VARCHAR2(50) | Y |  |

- **PK** `PK_TOKEN_DISPLAY_COUNTER`: TERMINAL_NAME, TOKEN_TYPE_ID
- **FK** `FK_TOKEN_DISPLAY_COUNTER`: (PARENT_TERMINAL_NAME, TOKEN_TYPE_ID) -> DEFINITIONS.TOKEN_TYPE_DISPLAY_COUNTER(TERMINAL, TOKEN_TYPE_ID) [disabled]

## DEFINITIONS.TOKEN_QUEUE

| Column | Type | Null | Comment |
|---|---|---|---|
| TOKEN_QUEUE_ID | NUMBER(10) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | Y |  |
| TOKEN_TYPE_ID | NUMBER(16) | Y |  |
| ENTRY_DATE | DATE | N |  |
| TOKEN_STATUS | CHAR(1) | Y |  |
| TOKEN_NO | VARCHAR2(3) | Y |  |
| MRNO | VARCHAR2(14) | Y |  |
| TERMINAL_NAME | VARCHAR2(30) | Y |  |
| STATUS_CHANGE_TERMINAL | VARCHAR2(30) | Y |  |
| RECEPTION_ID | NUMBER(10) | Y |  |
| SEQ_ID | NUMBER(10) | Y |  |
| HOLDED_BY | VARCHAR2(14) | Y |  |
| UP_RECORD_DATETIME | DATE | Y |  |
| DEPARTMENT_ID | VARCHAR2(9) | Y |  |
| COUNTER | NUMBER | Y |  |
| HOLD_REMARKS | VARCHAR2(1000) | Y |  |
| FORMER_MRNO | VARCHAR2(14) | Y |  |

- **PK** `PK_TOKEN_QUEUE`: TOKEN_QUEUE_ID, ENTRY_DATE, LOCATION_ID
- **Triggers**: `TRG_WS_GQH_UW_MG_Q` (after insert or update or delete)

## DEFINITIONS.TOKEN_SEQ_SMS_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SEQ_ID | NUMBER(10) | N |  |
| RECEPTION_ID | NUMBER(10) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| SMS_ALERT_ID | NUMBER | N |  |
| TOKEN_EVENT | CHAR(1) | Y |  |
| SMS_SEND_BEFORE | NUMBER | Y |  |
| SMS_PROMPT | VARCHAR2(50) | Y |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |

- **FK** `TOKEN_SEQ_SMS_SETUP_FK`: (SEQ_ID, LOCATION_ID, RECEPTION_ID) -> DEFINITIONS.SEQUENCE_SETUP(SEQ_ID, LOCATION_ID, RECEPTION_ID)
- **Triggers**: `TOKEN_SEQ_SMS_SETUP_DEL` (after delete), `TOKEN_SEQ_SMS_SETUP_INS` (before insert), `TOKEN_SEQ_SMS_SETUP_UPD` (before update)

## DEFINITIONS.TOKEN_SYTEM_HOLD_REMARKS

| Column | Type | Null | Comment |
|---|---|---|---|
| REMARKS_ID | NUMBER(5) | N |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| TOKEN_REASON | CHAR(1) default 'H' | Y |  |

- **PK** `PK_TOKEN_SYTEM_HOLD_REMARKS`: REMARKS_ID
- **Triggers**: `TOKEN_SYTEM_HOLD_REMARKS_DEL` (after delete), `TOKEN_SYTEM_HOLD_REMARKS_INS` (before insert), `TOKEN_SYTEM_HOLD_REMARKS_UPD` (before update)

## DEFINITIONS.TOKEN_TYPE_TERMINALS

| Column | Type | Null | Comment |
|---|---|---|---|
| TERMINAL_NAME | VARCHAR2(30) | N |  |
| IS_TOKEN | CHAR(1) | Y |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| RECEPTION_ID | NUMBER(10) | N |  |
| SEQ_ID | NUMBER(10) | N |  |
| IS_QUEUE | CHAR(1) | Y |  |
| GET_TERMINAL_LOCATION | CHAR(1) | Y |  |

- **PK** `PK_TOKEN_TYPE_TERMINALS`: TERMINAL_NAME, LOCATION_ID, RECEPTION_ID, SEQ_ID
- **FK** `FK_TOKEN_TYPE_TERMINALS`: (SEQ_ID, LOCATION_ID, RECEPTION_ID) -> DEFINITIONS.SEQUENCE_SETUP(SEQ_ID, LOCATION_ID, RECEPTION_ID) [disabled]
- **Triggers**: `TOKEN_TYPE_TERMINALS_DEL` (after delete), `TOKEN_TYPE_TERMINALS_INS` (before insert), `TOKEN_TYPE_TERMINALS_UPD` (before update)

## DEFINITIONS.TOKEN_TYPE_WISE_CLINICS

| Column | Type | Null | Comment |
|---|---|---|---|
| TOKEN_TYPE_ID | NUMBER(16) | N | this column contains token type id |
| LOCATION_ID | VARCHAR2(3) | N | this column contains location id |
| ORDER_LOCATION_ID | VARCHAR2(3) | N | this column contains order location id |
| CLINIC_ID | VARCHAR2(7) | N | this column contains clinic id |
| ACTIVE | CHAR(1) | Y | this column contains Y or N |
| BUTTON_LABEL | VARCHAR2(20) | Y | this column contains the label of button to be displayed on token generation form |
| PROMPT_TEXT | VARCHAR2(4000) | Y |  |

- **PK** `PK_TOKEN_TYPE_WISE_CL`: TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID, CLINIC_ID
- **FK** `FK_TOKEN_TYE_1`: (TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.TOKEN_TYPE(TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID)

## DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE

| Column | Type | Null | Comment |
|---|---|---|---|
| TOKEN_TYPE_ID | NUMBER(16) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| ORDER_LOCATION_ID | VARCHAR2(3) | N |  |
| OBJECT_CODE | VARCHAR2(11) | N |  |
| ACTION | CHAR(1) | Y |  |
| BUTTON_LABEL | VARCHAR2(15) | Y |  |
| APEX_PAGE_ID | NUMBER | Y |  |
| APEX_APP_ID | NUMBER | Y |  |

- **PK** `TOKEN_TYPE_WISE_PK`: OBJECT_CODE, TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID
- **FK** `TOKEN_TYPE_WISE_FK`: (TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID) -> DEFINITIONS.TOKEN_TYPE(TOKEN_TYPE_ID, LOCATION_ID, ORDER_LOCATION_ID) [disabled]
- **Triggers**: `TOKEN_TYPE_WISE_OBJCODE_DEL` (after delete), `TOKEN_TYPE_WISE_OBJCODE_INS` (before insert), `TOKEN_TYPE_WISE_OBJCODE_UPD` (before update)

## DEFINITIONS.TRANSACTION_TYPE_COPY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | VARCHAR2(2) | Y |  |
| CLINIC | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PHARMACY | VARCHAR2(1) | Y |  |
| INVOICE | VARCHAR2(1) | Y |  |
| INVOICE_TYPE | VARCHAR2(1) | Y |  |


## DEFINITIONS.TRANSACTION_TYPE_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_NAME | VARCHAR2(60) | N |  |

- **PK** `PK_TRANSACTION_TYPE_GROUP`: GROUP_NAME
- **Triggers**: `TRANSACTION_TYPE_GROUP_CEA` (before insert or update or delete), `TRANSACTION_TYPE_GROUP_DEL` (after delete), `TRANSACTION_TYPE_GROUP_INS` (before insert), `TRANSACTION_TYPE_GROUP_UPD` (before update), `TRG_WS_QBX_MY_ZH_Q` (after insert or update or delete)

## DEFINITIONS.TRANSACTION_TYPE_GROUP_DETAIL

| Column | Type | Null | Comment |
|---|---|---|---|
| GROUP_NAME | VARCHAR2(60) | N |  |
| TRANSACTION_TYPE_ID | VARCHAR2(3) | N |  |

- **PK** `PK_TRAN_TYPE_GROUP_DETAIL`: GROUP_NAME, TRANSACTION_TYPE_ID
- **FK** `FK_TRAN_TYPE_GROUP_DETAIL_1`: (GROUP_NAME) -> DEFINITIONS.TRANSACTION_TYPE_GROUP(GROUP_NAME)
- **FK** `FK_TRAN_TYPE_GROUP_DETAIL_2`: (TRANSACTION_TYPE_ID) -> DEFINITIONS.TRANSACTION_TYPE(TRANSACTION_TYPE_ID) [disabled]
- **Triggers**: `TRANSACTION_TYPE_GROUP_DETAIL_CEA` (before insert or update or delete), `TRG_WS_ISI_EN_KA_Q` (after insert or update or delete)

## DEFINITIONS.TRANSACTION_TYPE_HISTORY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | VARCHAR2(2) | Y |  |
| CLINIC | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |
| PHARMACY | VARCHAR2(1) | Y |  |
| INVOICE | VARCHAR2(1) | Y |  |
| INVOICE_TYPE | VARCHAR2(1) | Y |  |
| TABLE_REFERENCE | VARCHAR2(60) | Y |  |


## DEFINITIONS.TRANSPORT

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSPORT_ID | VARCHAR2(5) | N |  |
| DESCRIPTION | VARCHAR2(60) | N |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_TRANSPORT`: TRANSPORT_ID
- **Triggers**: `TRANSPORT_CEA` (before insert or update or delete), `TRANSPORT_DEL` (after delete), `TRANSPORT_INS` (before insert), `TRANSPORT_UPD` (before update), `TRG_WS_SFV_KR_HX_Q` (after insert or update or delete)

## DEFINITIONS.TRANSPORT_ROUTE

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSPORT_ROUTE_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) | Y |  |

- **PK** `PK_TRANSPORT_ROUTE`: TRANSPORT_ROUTE_ID
- **Triggers**: `TRANSPORT_ROUTE_CEA` (before insert or update or delete), `TRG_WS_KXB_IQ_SP_Q` (after insert or update or delete)

## DEFINITIONS.TREATMENT_ELEMENT_PARAMETERS

| Column | Type | Null | Comment |
|---|---|---|---|
| TEP_ID | NUMBER | N |  |
| ELEMENT_ID | NUMBER | Y |  |
| PARAMETER_ID | VARCHAR2(6) | Y |  |
| ORDER_BY | NUMBER | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |

- **PK** `PK_TRTMNT_ELMNT_PARAMETERS`: TEP_ID
- **UK** `UK_TRTMNT_ELMNT_PARAMETERS_1`: ELEMENT_ID, PARAMETER_ID
- **FK** `FK_TRTMNT_ELMNT_PARAMETERS_2`: (PARAMETER_ID) -> ORDERENTRY.NOTE_PARAMETER(PARAMETER_ID) [disabled]
- **Triggers**: `TREAT_ELEMENT_PARAM_DEL` (after delete), `TREAT_ELEMENT_PARAM_INS` (before insert), `TREAT_ELEMENT_PARAM_UPD` (before update)

## DEFINITIONS.TREATMENT_GUIDELINES

| Column | Type | Null | Comment |
|---|---|---|---|
| FILE_ID | VARCHAR2(5) | N | A unique File ID. |
| NAME | VARCHAR2(256) | N | Original / Physical file name. |
| DISPLAY_NAME | VARCHAR2(100) | N | Label or caption of a file to display on screen. |
| PATH | VARCHAR2(200) | N | Physical path of a file. |
| REMARKS | VARCHAR2(500) | Y | Remarks for a file. |
| ONLINE_DATE | DATE | Y | Date Time on which file made online. |
| ACTIVE | CHAR(1) | N | A flag to mark a file Active for use or not. |
| FILE_TYPE | CHAR(3) | N | File extension. |
| DOC_TYPE_ID | VARCHAR2(5) | N |  |
| DOC_TYPE | VARCHAR2(1) default 'A' | Y | A - For All Type Document, T - Treatment Guidline Document , E - Patient Education Document |

- **PK** `PK_TREATMENT_GUIDELINES`: FILE_ID
- **FK** `FK_TREATMENT_GUIDELINES_1`: (DOC_TYPE_ID) -> DEFINITIONS.DOCUMENT_TYPE(DOC_TYPE_ID) [disabled]
- **CHECK** `CHK_TREATMENT_GUIDELINES`: ACTIVE IN ('Y','N'
- **Triggers**: `TREATMENT_GUIDELINES_CEA` (before insert or update or delete), `TREATMENT_GUIDELINES_DEL` (after delete), `TREATMENT_GUIDELINES_INS` (before insert), `TREATMENT_GUIDELINES_UPD` (before update), `TRG_WS_FSM_SV_MG_Q` (after insert or update or delete)

## DEFINITIONS.TRIAGE_LEVELS

| Column | Type | Null | Comment |
|---|---|---|---|
| SERIAL_NO | NUMBER(3) | N |  |
| TRIAGE_LEVEL | VARCHAR2(500) | N |  |
| TRIAGE_COLOR | VARCHAR2(200) | N |  |
| TRIAGE_TIME | VARCHAR2(100) | N |  |
| ACTIVE | CHAR(1) default 'N' | Y |  |
| RGB_VALUE | VARCHAR2(15) | Y |  |

- **PK** `PK_TRIAGE_LEVELS_01`: SERIAL_NO
- **Triggers**: `TRIAGE_LEVELS_DEL` (after delete), `TRIAGE_LEVELS_INS` (before insert), `TRIAGE_LEVELS_INSERT` (before insert), `TRIAGE_LEVELS_UPD` (before update)

## DEFINITIONS.TRMP_CPT

| Column | Type | Null | Comment |
|---|---|---|---|
| CPT_ID | VARCHAR2(18) | Y |  |
| DESCRIPTION | VARCHAR2(4000) | Y |  |
| SHORT_DESC | VARCHAR2(4000) | Y |  |

_No standard audit columns._


## DEFINITIONS.TT_HISTORY_R

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | VARCHAR2(2) | Y |  |
| CLINIC | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.TT_R

| Column | Type | Null | Comment |
|---|---|---|---|
| TRANSACTION_TYPE_ID | VARCHAR2(3) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| COUNTER | NUMBER(7) | Y |  |
| TRN_YEAR | VARCHAR2(2) | Y |  |
| CLINIC | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |


## DEFINITIONS.TUBES

| Column | Type | Null | Comment |
|---|---|---|---|
| TUBE_ID | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_TUBE_ID`: TUBE_ID

## DEFINITIONS.T_CODES

| Column | Type | Null | Comment |
|---|---|---|---|
| T_CODE_ID | VARCHAR2(10) | N | Snomed T-Code ID |
| ACTIVE | CHAR(1) default 'N' | Y | This column contains the Active Status. (Y=ACTIVE, N=Not-Active) |

- **PK** `PK_T_CODES`: T_CODE_ID
- **Triggers**: `TRG_WS_HGY_MS_RJ_Q` (after insert or update or delete), `T_CODES_CEA` (before insert or update or delete), `T_CODES_DEL` (after delete), `T_CODES_INS` (before insert), `T_CODES_UPD` (before update)

## DEFINITIONS.UNIFIED_CONTACT_INFO

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N |  |
| SETUP_DATE | DATE | Y |  |
| INSTRUCTIONS_TEXT | VARCHAR2(4000) | Y |  |
| PRE_INSTRUCTION_TEXT | VARCHAR2(4000) | Y |  |
| POST_INSTRUCTION_TEXT | VARCHAR2(4000) | Y |  |
| URDU_TEXT_IMG | BLOB | Y |  |
| ORDER_BY | NUMBER | Y |  |
| EXTENSION1 | VARCHAR2(50) | Y |  |
| EXTENSION2 | VARCHAR2(50) | Y |  |
| EXTENSION3 | VARCHAR2(50) | Y |  |
| PHONE_NO1 | VARCHAR2(50) | Y |  |
| PHONE_NO2 | VARCHAR2(50) | Y |  |
| PHONE_NO3 | VARCHAR2(50) | Y |  |
| OBJECT_COE | VARCHAR2(50) | Y |  |
| UAN | VARCHAR2(50) | Y |  |
| VALID_FROM_DATE | DATE | Y |  |
| VALID_TO_DATE | DATE | Y |  |
| ACTIVE | CHAR(1) default 'Y' | Y |  |
| LOCATION_ID | VARCHAR2(50) | Y |  |
| ORGANIZATION_ID | VARCHAR2(50) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_UNIFIED_CONTACT_INFO`: SR_NO
- **UK** `UNIFIED_CONTACT_INFO_UK`: ORDER_BY, LOCATION_ID
- **Triggers**: `UNIFIED_CONTACT_INFO_DEL` (after delete), `UNIFIED_CONTACT_INFO_INS` (before insert), `UNIFIED_CONTACT_INFO_UPD` (before update)

## DEFINITIONS.UNIT_LANGUAGE_SETUP
THIS TABLE IS USED TO DEFINE MULTILINGUAL UNIT INSTRUCTIONS WHICH WILL BE PRINTED ON PHARMACY PRESCRIPTION AND LABEL

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUAGE_ID | VARCHAR2(6) | N |  |
| UNIT_ID | VARCHAR2(5) | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR SINGULAR INSTRUCTIONS |
| LABEL_DESC1 | NVARCHAR2(500) | Y | THIS COLUMN IS USED FOR PLURAL INSTRUCTIONS |
| ACTIVE | VARCHAR2(1) | Y |  |
| LABEL_DISCHARGE | NVARCHAR2(500) | Y | This Column will be used on Discharge Card report |

- **PK** `PK_UNIT_LANGUAGE_SETUP`: LANGUAGE_ID, UNIT_ID
- **Triggers**: `TRG_WS_FTI_WV_ZM_Q` (after insert or update or delete), `UNIT_LANGUAGE_SETUP_CEA` (before insert or update or delete), `UNIT_LANGUAGE_SETUP_DEL` (after delete), `UNIT_LANGUAGE_SETUP_INS` (before insert), `UNIT_LANGUAGE_SETUP_UPD` (before update)

## DEFINITIONS.UNIT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| UNIT_TYPE | VARCHAR2(2) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |

- **PK** `PK_UNIT_TYPE`: UNIT_TYPE
- **Triggers**: `TRG_WS_IVD_NY_RL_Q` (after insert or update or delete), `UNIT_TYPE_CEA` (before insert or update or delete), `UNIT_TYPE_DEL` (after delete), `UNIT_TYPE_INS` (before insert), `UNIT_TYPE_UPD` (before update)

## DEFINITIONS.UPD_R

| Column | Type | Null | Comment |
|---|---|---|---|
| VAL | VARCHAR2(3000) | Y |  |


## DEFINITIONS.USERS_TASKS

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| TASK_COUNT | NUMBER | Y |  |
| PATH | VARCHAR2(500) | Y |  |
| TASK_DESCRIPTION | VARCHAR2(255) | Y |  |
| PROJECT | VARCHAR2(255) | Y |  |
| ACTING_FOR_MRNO | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ASSIGNMENT_ID | NUMBER(3) | Y |  |
| LAST_EXE_TIME | DATE | Y |  |
| DISPLAY_SEQUENCE | NUMBER(3) | Y |  |

_No standard audit columns._


## DEFINITIONS.USERS_TASKS_APEX

| Column | Type | Null | Comment |
|---|---|---|---|
| MRNO | VARCHAR2(14) | Y |  |
| TASK_COUNT | NUMBER | Y |  |
| PATH | VARCHAR2(500) | Y |  |
| TASK_DESCRIPTION | VARCHAR2(255) | Y |  |
| PROJECT | VARCHAR2(255) | Y |  |
| ACTING_FOR_MRNO | VARCHAR2(14) | Y |  |
| OBJECT_CODE | VARCHAR2(11) | Y |  |
| ASSIGNMENT_ID | NUMBER(3) | Y |  |
| LAST_EXE_TIME | DATE | Y |  |
| DISPLAY_SEQUENCE | NUMBER(3) | Y |  |

_No standard audit columns._


## DEFINITIONS.USER_ALERTS

| Column | Type | Null | Comment |
|---|---|---|---|
| ALERT_ID | NUMBER | N |  |
| ALERT_DESC | VARCHAR2(600) | Y |  |
| OBJECTS | VARCHAR2(4000) | Y |  |

- **PK** `PK_USER_ALERTS`: ALERT_ID
- **Triggers**: `TRG_WS_TFD_VR_PN_Q` (after insert or update or delete), `USER_ALERTS_CEA` (before insert or update or delete)

## DEFINITIONS.USER_GUI

| Column | Type | Null | Comment |
|---|---|---|---|
| MAIN_BGCOLOR | VARCHAR2(25) | Y |  |
| TABLE_BGCOLOR | VARCHAR2(25) | Y |  |
| TABLE_BRDCOLOR | VARCHAR2(25) | Y |  |
| TABLE_LBLCOLOR | VARCHAR2(25) | Y |  |
| BTNPANEL_BGCOLOR | VARCHAR2(25) | Y |  |
| MENU_BGCOLOR | VARCHAR2(25) | Y |  |
| MENU_ALNKCOLOR | VARCHAR2(25) | Y |  |
| MENU_VLNKCOLOR | VARCHAR2(25) | Y |  |
| MAIN_HDCOLOR | VARCHAR2(25) | Y |  |
| MAIN_HLPCOLOR | VARCHAR2(25) | Y |  |
| MENU_HDCOLOR | VARCHAR2(25) | Y |  |
| MENU_HDBGCOLOR | VARCHAR2(25) | Y |  |
| MENU_HLNKCOLOR | VARCHAR2(25) | Y |  |

- **PK** `PK_USER_GUI`: USER_ID
- **Triggers**: `TRG_WS_NPO_GS_OY_Q` (after insert or update or delete), `USER_GUI_CEA` (before insert or update or delete)

## DEFINITIONS.USER_OBJECT_PATIENT_TYPE

| Column | Type | Null | Comment |
|---|---|---|---|
| USER_MRNO | VARCHAR2(14) | N |  |
| SERIAL_NO | NUMBER | N |  |
| INCLUDE_IN_REPORT | CHAR(1) default 'Y' | N |  |

- **PK** `PK_USER_OBJECT_PATIENT_TYPE`: USER_MRNO, SERIAL_NO
- **FK** `FK_USER_OBJECT_PATIENT_TYPE_01`: (SERIAL_NO) -> DEFINITIONS.OBJECT_PATIENT_TYPE(SERIAL_NO) [disabled]
- **CHECK** `CHK_USER_OBJECT_PAT_TYPE_01`: INCLUDE_IN_REPORT IN ('N','Y'

## DEFINITIONS.VACANCY_SOURCE

| Column | Type | Null | Comment |
|---|---|---|---|
| VACANCY_SOURCE_ID | VARCHAR2(6) | N |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| DEFAULTS | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_VACANCY_SOURCE`: VACANCY_SOURCE_ID
- **Triggers**: `TRG_WS_FOQ_GT_QR_Q` (after insert or update or delete), `VACANCY_SOURCE_CEA` (before insert or update or delete), `VACANCY_SOURCE_DEL` (after delete), `VACANCY_SOURCE_INS` (before insert), `VACANCY_SOURCE_UPD` (before update)

## DEFINITIONS.VACCINATION
This table is used to store the information of vaccine.

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| REPORT_FOOTER | VARCHAR2(4000) | Y |  |
| OBJECTIVE | VARCHAR2(4000) | Y |  |
| RATIONALE | VARCHAR2(4000) | Y |  |
| TOTAL_DOSES | NUMBER | Y | This column is used to store the total no. of doses of vaccine. |
| MIN_AGE | NUMBER | Y | This column is used to store the minimum age required for vaccine. |
| MAX_AGE | NUMBER | Y | This column is used to store the maximum age required for vaccine. |
| DRUG_ID | VARCHAR2(18) | Y |  |
| CPT_ID | VARCHAR2(18) | Y |  |
| AGE_CRITERIA_QUEST | VARCHAR2(4000) | Y | This column is used to store the age criteria question. |
| GUIDELINE_DOCUMENT | VARCHAR2(1000) | Y | This column is used to store the link guideline document. |
| ACTIVE | VARCHAR2(1) | Y | Y - Yes, N - No. |
| VACCINE_GROUP_ID | VARCHAR2(4) | Y |  |
| BOOSTER_DOSE | VARCHAR2(1) default 'N' | Y |  |

- **PK** `PK_VACCINATION`: VACCINE_ID
- **Triggers**: `TRG_WS_ITQ_EZ_RV_Q` (after insert or update or delete), `VACCINATION_CEA` (before insert or update or delete), `VACCINATION_DEL` (after delete), `VACCINATION_INS` (before insert), `VACCINATION_UPD` (before update)

## DEFINITIONS.VACCINATION_DEPARTMENT

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DURATION | NUMBER | Y |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_VACCINATION_DEPARTMENT`: VACCINE_GROUP_ID, DEPARTMENT_ID
- **Triggers**: `TRG_WS_KCY_XP_PQ_Q` (after insert or update or delete), `VACCINATION_DEPARTMENT_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_DEPARTMENT_SECTION

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| DEPARTMENT_ID | VARCHAR2(7) | N |  |
| SECTION_ID | VARCHAR2(7) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DURATION | NUMBER | Y |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_VACCINATION_DEPT_SEC`: VACCINE_GROUP_ID, DEPARTMENT_ID, SECTION_ID
- **Triggers**: `TRG_WS_YIY_OM_TS_Q` (after insert or update or delete), `VACCINATION_DEPARTMENT_SECTION_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_DESIGNATION

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | Y |  |
| DESIGNATION_ID | VARCHAR2(6) | Y |  |
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| DURATION | NUMBER | Y |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **Triggers**: `TRG_WS_VGB_BX_GD_Q` (after insert or update or delete), `VACCINATION_DESIGNATION_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_DOSE_SCHEDULES
This table is used to store the information of vaccine schedules.

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_ID | VARCHAR2(4) | N |  |
| SCHEDULE_NO | NUMBER | N | This column is used to store the Dose# of vaccine. |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| DOSE_GAP | NUMBER | Y | This column is used to store the dose gap for the next dose to be administer. |
| PATIENT_TRANSFER_QUEST | VARCHAR2(4000) | Y | This column is used to store the patient transfer question description. |
| PATIENT_DISCHAGED_QUEST_1 | VARCHAR2(4000) | Y | This column is used to store the discharge question no. 1 description. |
| PATIENT_DISCHAGED_QUEST_2 | VARCHAR2(4000) | Y | This column is used to store the discharge question no. 2 description. |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y | Y - Yes, N - No. |
| VALIDITY | NUMBER | Y |  |

- **PK** `PK_VACCINATION_DOSE_SCH`: VACCINE_ID, SCHEDULE_NO
- **Triggers**: `TRG_WS_HSI_KK_XB_Q` (after insert or update or delete), `VACCINATION_DOSE_SCHEDULES_CEA` (before insert or update or delete), `VACCINATION_DOSE_SCHEDULES_DEL` (after delete), `VACCINATION_DOSE_SCHEDULES_INS` (before insert), `VACCINATION_DOSE_SCHEDULES_UPD` (before update)

## DEFINITIONS.VACCINATION_EMPLOYEES

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| MRNO | VARCHAR2(14) | N |  |
| LOCATION_ID | VARCHAR2(3) | Y |  |
| DURATION | NUMBER | Y |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_VACCINATION_EMPLOYEES`: VACCINE_GROUP_ID, MRNO
- **Triggers**: `TRG_WS_DSK_VE_TE_Q` (after insert or update or delete), `VACCINATION_EMPLOYEES_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_GROUP

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| DESCRIPTION | VARCHAR2(150) | Y |  |
| VACCINE_DOSE_DAY | NUMBER(6) default 2 | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_VACCINATION_GROUP`: VACCINE_GROUP_ID
- **Triggers**: `TRG_WS_XPV_CT_WJ_Q` (after insert or update or delete), `VACCINATION_GROUP_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_INSTRUCTIONS
This table is used to store the information of vaccine instructions.

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_ID | VARCHAR2(4) | N |  |
| INSTRUCTION_TYPE | VARCHAR2(3) | N |  |
| SR_NO | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y | Y - Yes, N - No. |

- **PK** `PK_VACCINATION_INSTRUCTIONS`: VACCINE_ID, INSTRUCTION_TYPE, SR_NO
- **Triggers**: `TRG_WS_CGF_VO_MP_Q` (after insert or update or delete), `VACCINATION_INSTRUCTIONS_CEA` (before insert or update or delete), `VACCINATION_INSTRUCTIONS_DEL` (after delete), `VACCINATION_INSTRUCTIONS_INS` (before insert), `VACCINATION_INSTRUCTIONS_UPD` (before update)

## DEFINITIONS.VACCINATION_LOCATIONS

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| ORGANIZATION_ID | VARCHAR2(7) | N |  |
| LOCATION_ID | VARCHAR2(3) | N |  |
| VACCINE_RESPONSIBILITY | VARCHAR2(1) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |
| PENDING_DURATION | NUMBER | Y | Needle Stick & Vaccination Pending List  wil display befor Nth no of days. (Needle Stick & Vaccination Pending Duration in Days. System Constant - 316) |
| FOLLOWUP_DURATION | NUMBER | Y | Needle Stick & Vaccination followup email will be send before given N days. (Needle Stick & Vaccination Followup Email Sending Duration. System Constant 317) |
| EXTENSION_NO | VARCHAR2(100) | Y | Extension No, In case of any query regarding Needle Stick/Vaccination. (Extension No, In case of any query regarding Needle Stick/Vaccination. System Constant - 524) |
| VACCINATION_TIME | VARCHAR2(200) | Y | Vaccination time (Vaccination time will be mentioned in system constant value. System Constant - 1025) |
| VACCINATION_ROOM | VARCHAR2(200) | Y | Vaccination room (Vaccination room will be mentioned in system constant value. System Constant - 1026) |

- **PK** `PK_VACCINATION_LOCATIONS`: VACCINE_GROUP_ID, ORGANIZATION_ID, LOCATION_ID
- **Triggers**: `TRG_WS_NDS_ND_DF_Q` (after insert or update or delete), `VACCINATION_LOCATIONS_CEA` (before insert or update or delete)

## DEFINITIONS.VACCINATION_QUESTIONS
This table is used to store the vaccine questions for patient evaluation.

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_ID | VARCHAR2(4) | N |  |
| QUESTION_TYPE | VARCHAR2(3) | N | This column is used to store type of question. 001 - Evaluation 002- checklist |
| QUESTION_NO | NUMBER | N | This column is used to store the serial number of question |
| PARENT_QUESTION_NO | NUMBER | Y |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| SHORT_DESC | VARCHAR2(100) | Y |  |
| AUTO_FILL | VARCHAR2(1) default 'N' | Y |  |
| REMARKS | VARCHAR2(4000) | Y |  |
| ACTIVE | VARCHAR2(1) | Y | Y - Yes, N - No. |

- **PK** `PK_VACCINATION_QUESTIONS`: VACCINE_ID, QUESTION_TYPE, QUESTION_NO
- **Triggers**: `TRG_WS_IKS_LX_VT_Q` (after insert or update or delete), `VACCINATION_QUESTIONS_CEA` (before insert or update or delete), `VACCINATION_QUESTIONS_DEL` (after delete), `VACCINATION_QUESTIONS_INS` (before insert), `VACCINATION_QUESTIONS_UPD` (before update)

## DEFINITIONS.VACCINATION_ROLE

| Column | Type | Null | Comment |
|---|---|---|---|
| VACCINE_GROUP_ID | VARCHAR2(4) | N |  |
| ROLE_ID | NUMBER(10) | N |  |
| DURATION | NUMBER | Y |  |
| UNIT_ID | VARCHAR2(5) | Y |  |
| ACTIVE | VARCHAR2(1) default 'Y' | Y |  |

_No standard audit columns._

- **PK** `PK_VACCINATION_ROLE`: VACCINE_GROUP_ID, ROLE_ID

## DEFINITIONS.VISIT_LOCATION

| Column | Type | Null | Comment |
|---|---|---|---|
| VISIT_LOC_ID | NUMBER | N |  |
| DESCRIPTION | VARCHAR2(100) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_VISIT_LOCATION`: VISIT_LOC_ID
- **Triggers**: `TRG_WS_XEB_PM_WV_Q` (after insert or update or delete), `VISIT_LOCATION_CEA` (before insert or update or delete), `VISIT_LOCATION_DEL` (after delete), `VISIT_LOCATION_INS` (before insert), `VISIT_LOCATION_UPD` (before update)

## DEFINITIONS.VISIT_LOC_LANGUAGE_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| LANGUGAE_ID | VARCHAR2(6) | N |  |
| VISIT_LOC_ID | NUMBER | N |  |
| LABEL_DESC | NVARCHAR2(500) | Y | Label Desc field will be used to show langugae wise text on Discharge Instruction report on discharge card |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_VISIT_LOC_LANGUAGE_SETUP`: LANGUGAE_ID, VISIT_LOC_ID
- **Triggers**: `TRG_WS_DBD_IV_CY_Q` (after insert or update or delete), `VISIT_LOC_LANGUAGE_SETUP_CEA` (before insert or update or delete), `VISIT_LOC_LANGUAGE_SETUP_DEL` (after delete), `VISIT_LOC_LANGUAGE_SETUP_INS` (before insert), `VISIT_LOC_LANGUAGE_SETUP_UPD` (before update)

## DEFINITIONS.VITAL_SIGNS

| Column | Type | Null | Comment |
|---|---|---|---|
| VS_ID | VARCHAR2(30) | N |  |
| VS_DESCRIPTION | VARCHAR2(200) | N |  |
| ACTIVE | CHAR(1) default 'N' | N |  |
| VS_SHORT_DESC | VARCHAR2(200) | N |  |

- **PK** `PK_VITAL_SIGNS`: VS_ID
- **UK** `UK_VITAL_SIGNS`: VS_DESCRIPTION
- **Triggers**: `VITAL_SIGNS_DEL` (after delete), `VITAL_SIGNS_INS` (before insert), `VITAL_SIGNS_INSERT` (before insert), `VITAL_SIGNS_UPD` (before update)

## DEFINITIONS.VRIII_PROTOCOL_SETUP

| Column | Type | Null | Comment |
|---|---|---|---|
| SR_NO | NUMBER | N | This column contains Unique indetifier |
| BSL_MIN_RANGE | NUMBER | Y | This column contains value for minimum range |
| BSL_MAX_RANGE | NUMBER | Y | This column contains value for maximum range |
| BSL_RANGE_DESC | VARCHAR2(15) | Y | This column contains BSL range value |
| INSULIN_VALUE | NUMBER(5,2) | Y | This column contains BSL value for specific range |
| REMARKS | VARCHAR2(4000) | Y |  |

- **PK** `PK_VRIII_PROTOCOL_SETUP`: SR_NO
- **Triggers**: `VRIII_PROTOCOL_SETUP_DEL` (after delete), `VRIII_PROTOCOL_SETUP_INS` (before insert), `VRIII_PROTOCOL_SETUP_UPD` (before update)

## DEFINITIONS.VRIII_SUBSTRATE_SETS

| Column | Type | Null | Comment |
|---|---|---|---|
| SUBSTRATE_SET_ID | VARCHAR2(3) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ORDER_NO | NUMBER | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

_No standard audit columns._

- **PK** `PK_VRIII_SUBSTRATE_SETS`: SUBSTRATE_SET_ID

## DEFINITIONS.WALKING_AID

| Column | Type | Null | Comment |
|---|---|---|---|
| AID_ID | VARCHAR2(8) | N |  |
| DESCRIPTION | VARCHAR2(500) | Y |  |
| ACTIVE | VARCHAR2(1) | Y |  |

- **PK** `PK_AID_ID`: AID_ID
- **Triggers**: `TRG_WS_XPU_SZ_GO_Q` (after insert or update or delete), `WALKING_AID_CEA` (before insert or update or delete)

## DEFINITIONS.WARD_WISE_CPT
This table will be used to define the Ward wise CPTs

| Column | Type | Null | Comment |
|---|---|---|---|
| ROOM_ID | VARCHAR2(7) | N | Ward Id for which below CPT(s) will be charged |
| CPT_ID | VARCHAR2(18) | N | CPT Code which will be charged against Ward |
| TRANS_DATE | DATE default SYSDATE | N | Date when transaction was made |
| ACTIVE | CHAR(1) default 'Y' | N | Status of the Transaction |

- **PK** `PK_WARD_WISE_CPT`: ROOM_ID, CPT_ID
- **FK** `FK_WARD_WISE_CPT_1`: (ROOM_ID) -> DEFINITIONS.ROOMS(ROOM_ID)
- **FK** `FK_WARD_WISE_CPT_2`: (CPT_ID) -> DEFINITIONS.CPT(CPT_ID) [disabled]
- **CHECK** `CK_WARD_WISE_CPT_1`: ACTIVE IN ('Y','N'
- **Triggers**: `WARD_WISE_CPT_DEL` (after delete), `WARD_WISE_CPT_INS` (before insert), `WARD_WISE_CPT_UPD` (before update)

## DEFINITIONS.WEB_REPORT_SERVER_R

| Column | Type | Null | Comment |
|---|---|---|---|
| REPORT_SERVER_NAME | VARCHAR2(30) | Y |  |
| REPORT_SERVER_DOMAIN | VARCHAR2(30) | Y |  |
| ACTIVE | CHAR(1) | Y |  |


## DEFINITIONS.WHISPER_DATASET

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER generated by default as identity | Y |  |
| AUDIO_BLOB | BLOB | Y |  |
| TEXT | CLOB | N |  |
| STATUS | VARCHAR2(50) default 'pending' | Y |  |
| LOCKED_BY | VARCHAR2(100) | Y |  |
| LOCK_TIMESTAMP | TIMESTAMP(6) | Y |  |
| UPDATED_AT | TIMESTAMP(6) default CURRENT_TIMESTAMP | Y |  |

_No standard audit columns._


## DEFINITIONS.WHISPER_DATASET_SYNTH

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| AUDIO_BLOB | BLOB | Y |  |
| TEXT | CLOB | N |  |
| STATUS | VARCHAR2(50) | Y |  |
| LOCKED_BY | VARCHAR2(100) | Y |  |
| LOCK_TIMESTAMP | TIMESTAMP(6) | Y |  |
| UPDATED_AT | TIMESTAMP(6) | Y |  |

_No standard audit columns._

- **PK** `PK_WHISPER_DATASET_SYNTH`: ID

## DEFINITIONS.WHISPER_DATASET_SYNTH_CLEANED

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| TEXT | CLOB | N |  |

_No standard audit columns._


## DEFINITIONS.WHISPER_DATASET_SYNTH_COMPLETED

| Column | Type | Null | Comment |
|---|---|---|---|
| ID | NUMBER | N |  |
| AUDIO_BLOB | BLOB | Y |  |
| TEXT | CLOB | N |  |

_No standard audit columns._


## DEFINITIONS.WORKFLOW_NOTE_EXEMPTION

| Column | Type | Null | Comment |
|---|---|---|---|
| PURCHASE_TYPE_ID | NUMBER(3) | Y |  |
| SCHEMA_ID | VARCHAR2(3) | Y |  |
| WORK_FLOW_ID | NUMBER(4) | Y |  |
| EVENT_ID | NUMBER(3) | Y |  |

- **PK** `PK_WORKFLOW_NOTE_EXEMPTION`: PURCHASE_TYPE_ID, SCHEMA_ID, WORK_FLOW_ID, EVENT_ID
- **Triggers**: `WORKFLOW_NOTE_EXEMPTION_DEL` (after delete), `WORKFLOW_NOTE_EXEMPTION_INS` (before insert), `WORKFLOW_NOTE_EXEMPTION_UPD` (before update)

## DEFINITIONS.WORKING_AREA

| Column | Type | Null | Comment |
|---|---|---|---|
| DEPARTMENT_ID | VARCHAR2(7) | Y |  |
| SECTION_ID | VARCHAR2(7) | Y |  |
| WORKING_AREA_ID | VARCHAR2(5) | Y |  |
| DESCRIPTION | VARCHAR2(60) | Y |  |
| ACTIVE | CHAR(1) default 'Y' | N |  |
| ORDER_BY | NUMBER(3) | Y |  |

- **CHECK** `CK_WORKING_AREA_1`: ACTIVE IN ('Y','N'
- **CHECK** `CK_WORKING_AREA_2`: DESCRIPTION IS NOT NULL)
- **Triggers**: `TRG_WS_HVF_MV_UH_Q` (after insert or update or delete), `WORKING_AREA_CEA` (before insert or update or delete)

## DEFINITIONS.WORK_FLOW_EVENTS

| Column | Type | Null | Comment |
|---|---|---|---|
| WORK_FLOW_ID | NUMBER(4) | N |  |
| TRANSACTION_TYPE_ID | VARCHAR2(3) | N |  |
| EVENT_ID | VARCHAR2(4) | N |  |

- **PK** `PK_WORK_FLOW_EVENTS`: WORK_FLOW_ID, TRANSACTION_TYPE_ID, EVENT_ID
- **FK** `FK_WORK_FLOW_ID`: (WORK_FLOW_ID) -> DEFINITIONS.WORK_FLOW(WORK_FLOW_ID)
- **Triggers**: `TRG_WS_DMJ_NZ_QZ_Q` (after insert or update or delete), `WORK_FLOW_EVENTS_CEA` (before insert or update or delete), `WORK_FLOW_EVENTS_DEL` (after delete), `WORK_FLOW_EVENTS_INS` (before insert), `WORK_FLOW_EVENTS_UPD` (before update)

## DEFINITIONS.YEARS

| Column | Type | Null | Comment |
|---|---|---|---|
| START_DATE | DATE | N |  |
| END_DATE | DATE | N |  |
| FLAG | VARCHAR2(1) | Y |  |

- **Triggers**: `YEARS_DEL` (after delete), `YEARS_INS` (before insert), `YEARS_UPD` (before update)

