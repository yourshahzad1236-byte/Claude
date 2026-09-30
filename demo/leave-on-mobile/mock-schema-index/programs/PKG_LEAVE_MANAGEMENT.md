# HRD.PKG_LEAVE_MANAGEMENT

Type: PACKAGE  
Source: packages/pkg_leave_management.pks

## Public program units (spec)
- `PROCEDURE P_SUBMIT_LEAVE(P_EMPLOYEE_ID IN NUMBER, P_LEAVE_TYPE IN VARCHAR2, P_FROM IN DATE, P_TO IN DATE)`
- `FUNCTION F_LEAVE_BALANCE(P_EMPLOYEE_ID IN NUMBER, P_LEAVE_TYPE IN VARCHAR2) RETURN NUMBER`

## Tables / views referenced
- none found

## Calls packages / procedures / functions
- none found

## Called by (code, APEX pages)
- APEX 200:20 Apply Leave
