<!-- Copied from skills/oracle-plsql-apex-hrd-standards/SKILL.md by scripts/package_skills.py. Edit the original, not this copy. -->
# 1. Schema Standard

## Schema Name

```sql
HRD
```

Example:

```sql
HRD.PKG_EMPLOYEE
```

---

# 2. Package Naming Convention

## Rule

All package names must start with:

```sql
PKG_
```

## Format

```sql
PKG_<MODULE_NAME>
```

## Examples

```sql
PKG_EMPLOYEE
PKG_PAYROLL
PKG_ATTENDANCE
PKG_LEAVE_MANAGEMENT
PKG_APEX_UTILS
```

## Example Template

```sql
CREATE OR REPLACE PACKAGE HRD.PKG_EMPLOYEE AS

END PKG_EMPLOYEE;
/
```

---

# 3. Procedure Naming Convention

## Rule

All procedure names must start with:

```sql
P_
```

## Format

```sql
P_<ACTION_NAME>
```

## Examples

```sql
P_SAVE_EMPLOYEE
P_UPDATE_SALARY
P_DELETE_RECORD
P_PROCESS_PAYROLL
P_SEND_EMAIL
```

## Example

```sql
CREATE OR REPLACE PROCEDURE HRD.P_SAVE_EMPLOYEE
(
    p_emp_id IN NUMBER
)
AS
BEGIN
    NULL;
END;
/
```

---

# 4. Function Naming Convention

## Rule

All function names must start with:

```sql
F_
```

## Format

```sql
F_<ACTION_NAME>
```

## Examples

```sql
F_GET_EMP_NAME
F_CALCULATE_TAX
F_GET_DEPARTMENT
F_IS_ACTIVE
F_TOTAL_SALARY
```

## Example

```sql
CREATE OR REPLACE FUNCTION HRD.F_GET_EMP_NAME
(
    p_emp_id IN NUMBER
)
RETURN VARCHAR2
AS
BEGIN
    RETURN NULL;
END;
/
```

---

# 5. Variable Naming Convention

## Rule

All local variables must start with:

```sql
V_
```

## Format

```sql
V_<VARIABLE_NAME>
```

## Examples

```sql
V_EMP_NAME
V_TOTAL_AMOUNT
V_COUNT
V_START_DATE
V_ERROR_MSG
```

## Example

```sql
DECLARE
    V_EMP_NAME   VARCHAR2(100);
    V_TOTAL      NUMBER;
BEGIN
    NULL;
END;
/
```

---

# 6. Parameter Naming Convention

## Rule

All parameters must start with:

```sql
P_
```

## Format

```sql
P_<PARAMETER_NAME>
```

## Examples

```sql
P_EMP_ID
P_DEPTNO
P_START_DATE
P_USER_NAME
```

## Example

```sql
PROCEDURE P_SAVE_EMPLOYEE
(
    P_EMP_ID     IN NUMBER,
    P_EMP_NAME   IN VARCHAR2
)
```

---

# 7. Cursor Naming Convention

## Rule

All cursors must start with:

```sql
CUR_
```

## Examples

```sql
CUR_EMPLOYEE
CUR_PAYROLL
CUR_PENDING_REQUESTS
```

## Example

```sql
CURSOR CUR_EMPLOYEE IS
SELECT *
FROM EMPLOYEES;
```

---

# 8. Constant Naming Convention

## Rule

All constants must start with:

```sql
C_
```

## Examples

```sql
C_STATUS_ACTIVE
C_COMPANY_NAME
C_MAX_LIMIT
```

## Example

```sql
C_STATUS_ACTIVE CONSTANT VARCHAR2(1) := 'Y';
```

---

# 9. Record Type Naming Convention

## Rule

All record types should start with:

```sql
R_
```

## Examples

```sql
R_EMPLOYEE
R_PAYROLL
```

---

# 10. Collection Naming Convention

## Rule

All collections should start with:

```sql
T_
```

## Examples

```sql
T_EMPLOYEE_LIST
T_PAYROLL_DATA
```

---

# 11. Table Naming Convention

## Rule

Use meaningful business names.

## Recommended Format

```sql
<MODULE>_<ENTITY>_<TYPE>
```

## Examples

```sql
HRD_EMPLOYEE_MST
HRD_EMPLOYEE_DTL
HRD_PAYROLL_MST
HRD_PAYROLL_DTL
HRD_LEAVE_REQUEST
```

## Suffix Standards

| Suffix | Meaning           |
| ------ | ----------------- |
| MST    | Master Table      |
| DTL    | Detail Table      |
| LOG    | Log Table         |
| TMP    | Temporary Table   |
| HIS    | History Table     |
| TRN    | Transaction Table |

---

# 12. Primary Key Naming Convention

## Rule

Primary key columns should follow:

```sql
<TABLE_NAME>_ID
```

## Examples

```sql
EMPLOYEE_ID
PAYROLL_ID
LEAVE_REQUEST_ID
```

---

# 13. Sequence Naming Convention

## Rule

All sequence names must end with:

```sql
_SEQ
```

## Examples

```sql
EMPLOYEE_SEQ
PAYROLL_SEQ
LEAVE_REQ_SEQ
```

---

# 14. Trigger Naming Convention

## Rule

All trigger names must start with:

```sql
TRG_
```

## Examples

```sql
TRG_EMPLOYEE_BI
TRG_PAYROLL_AU
```

## Trigger Suffix Standards

| Suffix | Meaning       |
| ------ | ------------- |
| BI     | Before Insert |
| BU     | Before Update |
| BD     | Before Delete |
| AI     | After Insert  |
| AU     | After Update  |
| AD     | After Delete  |

---

# 15. View Naming Convention

## Rule

All view names should start with:

```sql
VW_
```

## Examples

```sql
VW_EMPLOYEE_SUMMARY
VW_PAYROLL_REPORT
```

---

# 16. Index Naming Convention

## Rule

All index names should start with:

```sql
IDX_
```

## Examples

```sql
IDX_EMPLOYEE_NAME
IDX_PAYROLL_DATE
```

---

# 17. Oracle APEX Naming Convention

## Page Names

Use meaningful page names.

Examples:

```
Employee Management
Payroll Processing
Leave Approval
```

## Static IDs

### Region

```
REG_<NAME>
```

Examples:

```
REG_EMPLOYEE
REG_PAYROLL
```

### Item

```
P<PageNo>_<ITEM_NAME>
```

Examples:

```
P10_EMP_ID
P20_DEPTNO
```

### Button

```
BTN_<ACTION>
```

Examples:

```
BTN_SAVE
BTN_CANCEL
BTN_SEARCH
```

### Dynamic Action

```
DA_<ACTION>
```

Examples:

```
DA_REFRESH_GRID
DA_VALIDATE_FORM
```

### LOV

```
LOV_<NAME>
```

Examples:

```
LOV_DEPARTMENT
LOV_EMPLOYEE
```

---

# 18. Exception Naming Convention

## Rule

Custom exceptions should start with:

```sql
EX_
```

## Examples

```sql
EX_INVALID_USER
EX_DATA_NOT_FOUND
```

---

# 19. General Development Standards

## Use Uppercase for

* SQL Keywords
* Table Names
* Column Names
* Package Names
* Procedure Names
* Function Names

## Example

```sql
SELECT EMPLOYEE_ID,
       EMP_NAME
FROM HRD_EMPLOYEE_MST
WHERE STATUS = 'ACTIVE';
```

---

# 20. Best Practices

* Use meaningful and readable names.
* Avoid short abbreviations.
* Keep naming consistent across all modules.
* Use standard prefixes and suffixes.
* Follow modular package-based development.
* Maintain reusable procedures and functions.
* Use exception handling in all procedures.
* Add proper comments in packages and procedures.

---

# 21. Sample Standard Package Structure

```sql
CREATE OR REPLACE PACKAGE HRD.PKG_EMPLOYEE AS

    PROCEDURE P_SAVE_EMPLOYEE
    (
        P_EMP_ID     IN NUMBER,
        P_EMP_NAME   IN VARCHAR2
    );

    FUNCTION F_GET_EMP_NAME
    (
        P_EMP_ID IN NUMBER
    ) RETURN VARCHAR2;

END PKG_EMPLOYEE;
/

CREATE OR REPLACE PACKAGE BODY HRD.PKG_EMPLOYEE AS

    PROCEDURE P_SAVE_EMPLOYEE
    (
        P_EMP_ID     IN NUMBER,
        P_EMP_NAME   IN VARCHAR2
    )
    AS
        V_COUNT NUMBER;
    BEGIN
        NULL;
    END P_SAVE_EMPLOYEE;

    FUNCTION F_GET_EMP_NAME
    (
        P_EMP_ID IN NUMBER
    ) RETURN VARCHAR2
    AS
        V_EMP_NAME VARCHAR2(100);
    BEGIN
        RETURN V_EMP_NAME;
    END F_GET_EMP_NAME;

END PKG_EMPLOYEE;
/
```

---

# Document Version

| Version | Date     | Author         |
| ------- | -------- | -------------- |
| 1.0     | May 2026 | Shahzad Farooq |
