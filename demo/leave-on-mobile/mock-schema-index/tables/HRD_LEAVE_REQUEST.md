# HRD.HRD_LEAVE_REQUEST

Source: tables/hrd_leave_request.sql

| Column | Type | Null | Default | PK | Comment |
|---|---|---|---|---|---|
| LEAVE_REQUEST_ID | NUMBER(12) | N |  | PK |  |
| EMPLOYEE_ID | NUMBER(10) | N |  |  |  |
| LEAVE_TYPE | VARCHAR2(3) | N |  |  |  |
| FROM_DATE | DATE | N |  |  |  |
| TO_DATE | DATE | N |  |  |  |
| STATUS | VARCHAR2(10) | Y | 'SUBMITTED' |  |  |
| APPROVED_BY | NUMBER(10) | Y |  |  |  |
| APPROVED_ON | DATE | Y |  |  |  |

## Foreign keys
- (inline): (EMPLOYEE_ID) → HRD_EMPLOYEE_MST

## Triggers
- TRG_LEAVE_REQUEST_BI (BEFORE INSERT)

## Referenced by (code, views, APEX pages)
- PACKAGE BODY PKG_LEAVE_MANAGEMENT (BODY)
- TRIGGER TRG_LEAVE_REQUEST_BI
- VIEW VW_PENDING_LEAVES
