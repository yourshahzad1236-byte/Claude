# HRD.HRD_EMPLOYEE_MST

Employee master

Source: tables/hrd_employee_mst.sql

| Column | Type | Null | Default | PK | Comment |
|---|---|---|---|---|---|
| EMPLOYEE_ID | NUMBER(10) | N |  | PK |  |
| EMP_NAME | VARCHAR2(100) | N |  |  |  |
| DEPT_ID | NUMBER(6) | Y |  |  |  |
| REPORTING_MGR_ID | NUMBER(10) | Y |  |  |  |
| STATUS | VARCHAR2(1) | N | 'A' |  | A=Active, I=Inactive |
| CREATED_ON | DATE | Y | SYSDATE |  |  |

## Foreign keys
- FK_EMP_MGR: (REPORTING_MGR_ID) → HRD_EMPLOYEE_MST (EMPLOYEE_ID)

## Referenced by foreign keys from
- HRD_EMPLOYEE_MST (REPORTING_MGR_ID)
- HRD_LEAVE_REQUEST (EMPLOYEE_ID)

## Indexes
- IDX_EMP_DEPT (DEPT_ID)

## Referenced by (code, views, APEX pages)
- VIEW VW_PENDING_LEAVES
