# RFID code objects

## Sequences
- ISEQ
- SEQ_RFID_ACCESS_SYNC_LOG
- SEQ_RFID_ACCESS_SYNC_RUN
- SEQ_RFID_CLEANUP_RUN
- SEQ_RFID_DELETED_ACCESS_AUDIT

## Packages (specifications)

### RFID.PKG_COMMON
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_COMMON IS

  PROCEDURE FOR_CHANGE_RFID_CARD(P_MRNO      IN VARCHAR2,
                                 P_RFID_CODE IN VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_DESIG_WISE_RFID_RIGHTS(P_DESIGNATION_ID   IN VARCHAR2,
                                       P_RFID_CATAGORY_ID IN NUMBER,
                                       P_MRNO             IN VARCHAR2,
                                       P_STOP             OUT VARCHAR2,
                                       P_ALERT_TEXT       OUT VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_CATEGORY_WISE_RFID_RIGHTS(P_RFID_CATAGORY_ID IN NUMBER,
                                          P_MRNO             IN VARCHAR2,
                                          P_STOP             OUT VARCHAR2,
                                          P_ALERT_TEXT       OUT VARCHAR2);

  /*****************************************************************/
  PROCEDURE PRO_DEPART_WISE_RFID_RIGHTS(P_DEPARTMENT_ID    IN VARCHAR2,
                                        P_RFID_CATAGORY_ID IN NUMBER,
                                        P_MACHINE_ID       IN NUMBER,
                                        P_MRNO             IN VARCHAR2,
                                        P_STOP             OUT VARCHAR2,
                                        P_ALERT_TEXT       OUT VARCHAR2);

  /**********************************************************************/
  /*****************************************************************/
  PROCEDURE PRO_RFID_REVOKE_RIGHTS(P_MRNO       IN VARCHAR2,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  /**********************************************************************/
  FUNCTION F_GET_RFID_CODE(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  /**********************************************************************/
  PROCEDURE P_ASSIGN_RFID_RIGHTS_TO_EMP(P_MRNO        IN VARCHAR2,
                                        P_STOP        OUT VARCHAR2,
                                        P_ALERT_TEXT  OUT VARCHAR2,
                                        P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL);

  /**********************************************************************/
  -------------------------------------------------------------------------------------------------
  -- THIS FUNCTION IS USED TO IDENTIFY EITHER MARKING ATTENDANCE ON A MACHINE IS ALLOWED OR NOT ---
  -------------------------------------------------------------------------------------------------
  FUNCTION F_IS_MARK_ATTENDANCE_ALLOWED(P_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                        P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE)
    RETURN CHAR;

  -----------------------------------------------------------------------------------------------------------
  -- THIS PROCEDURE IS USED TO ASSIGN DEPARTMENTAL/SECTION WIDE RIGHTS TO THE EMPLOYEES ON RFID MACHINE  ---
  -----------------------------------------------------------------------------------------------------------
  PROCEDURE P_INSERT_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                         P_SECTION_ID    IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                         P_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                         P_ALERT_TEXT    OUT VARCHAR2,
                                         P_STOP          OUT CHAR);

  -----------------------------------------------------------------------------------------------------------
  -- THIS PROCEDURE IS USED TO REVERT DEPARTMENTAL/SECTION WIDE RIGHTS TO THE EMPLOYEES ON RFID MACHINE  ---
  -----------------------------------------------------------------------------------------------------------
  PROCEDURE P_REVOKE_DEPARTMENTAL_RIGHTS(P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                         P_SECTION_ID    IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                         P_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                         P_ALERT_TEXT    OUT VARCHAR2,
                                         P_STOP          OUT CHAR);

  /*****************************************************************************************/
  PROCEDURE PRO_POPULATE_RFID_DEPARTMENT(P_MACHINE_ID  IN VARCHAR2,
                                         P_LOCATION_ID IN VARCHAR2,
                                         P_ALERT_TEXT  OUT VARCHAR2,
                                         P_STOP        OUT VARCHAR2);

  /*****************************************************************************************/
  FUNCTION F_EMP_CODE_FROM_RFID(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2;
  /*****************************************************************************************/
  PROCEDURE P_INSERT_RFID_ATTENDANCE(P_CHECK_TIME        IN DATE,
                                     P_MACHINE_CODE      IN VARCHAR2,
                                     P_RFID_CODE         IN VARCHAR2,
                                     P_CHECK_TYPE        IN VARCHAR2,
                                     P_VERIFICATION_MODE IN VARCHAR2,
                                     P_STOP              OUT CHAR,
                                     P_ALERT_TEXT        OUT VARCHAR2);
  /*****************************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2,
                               P_LOCATION_ID        IN VARCHAR2)
    RETURN VARCHAR2;
  /*****************************************************************************************/
  PROCEDURE P_GET_RFID_MACHINE_CODE(P_RFID_CODE          IN VARCHAR2,
                                    P_MACHINE_CODE       IN OUT VARCHAR2,
                                    P_MACHINE_IDENTIFIER IN OUT VARCHAR2,
                                    P_LOCATION_ID        IN VARCHAR2,
                                    P_IP_ADDRESS         IN VARCHAR2,
                                    P_MACHINE_CATEGORY   OUT VARCHAR2,
                                    P_EMPLOYEE_CODE      OUT VARCHAR2);
  /*****************************************************************************************/
  FUNCTION F_IS_TRANSPORT_POOL_CARD(P_RFID_CODE IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************************/
  FUNCTION F_MACHINE_CODE_FROM_IP(P_IP_ADDRESS IN VARCHAR2) RETURN VARCHAR2;
  /**************************************************************************/
  FUNCTION F_GET_IDENTIFIER(P_MRNO         IN VARCHAR2,
                            P_MACHINE_CODE IN VARCHAR2,
                            P_LOCATION_ID  IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION GET_IDENTIFIER_FROM_RFIDCODE(P_RFID_CODE    IN VARCHAR2,
                                        P_MACHINE_CODE IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_RFID_MACHINE_LOCATION_ID(P_MACHINE_CODE IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_RFID_FROM_MAPPING(P_MACHINE_CODE IN VARCHAR2,
                                   P_MRNO         IN VARCHAR2)
    RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_TYPE(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_CHECH_VEHICLE_MACHINE_RIGHTS(P_MACHINE_ID IN VARCHAR2,
                                          P_MRNO       IN VARCHAR2)
    RETURN CHAR;
  /********************************************************************************/
  FUNCTION F_CHECK_ACTIVE_EMP(P_RFID_CODE IN VARCHAR2) RETURN CHAR;
  /********************************************************************************/
  PROCEDURE P_INS_ATTENDANCE_PAT(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                                 P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                                 P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_REASON             VARCHAR2,
                                 P_STOP               OUT CHAR,
                                 P_ALERT_TEXT         OUT VARCHAR2);
  /***************************************/
  PROCEDURE FOR_REMOVE_RFID_CARD(P_MRNO          IN VARCHAR2,
                                 P_OLD_RFID_CODE IN VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_INS_RFID_QUEUE(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                             P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                             P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                             P_MRNO               VARCHAR2,
                             P_STOP               OUT CHAR,
                             P_ALERT_TEXT         OUT VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_DEL_ALERT_QUEUE(P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                              P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                              P_SRNO               NUMBER,
                              P_STOP               OUT CHAR,
                              P_ALERT_TEXT         OUT VARCHAR2);
  /********************************************************************************/
  FUNCTION F_GET_MACH_IS_CONF(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  PROCEDURE P_INS_TEMP_CARD(P_MRNO        HRD.VU_INFORMATION.MRNO%TYPE,
                            P_ACTUAL_RFID HRD.VU_INFORMATION.RFID_CODE %TYPE,
                            P_TEMP_RFID   VARCHAR2,
                            P_DAY         NUMBER,
                            P_STOP        OUT CHAR,
                            P_ALERT_TEXT  OUT VARCHAR2);
  /********************************************************************************/
  PROCEDURE P_UPDATE_RFID_CODE(P_MRNO       HRD.VU_INFORMATION.MRNO%TYPE,
                               P_RFID_ID    VARCHAR2,
                               P_STOP       OUT CHAR,
                               P_ALERT_TEXT OUT VARCHAR2);
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_LOC_ID(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /********************************************************************************/
  FUNCTION F_GET_MACHINE_LOC_DESC(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;

  /**********************************************************************************/

  PROCEDURE P_INS_ATTENDANCE_EMP(P_CHECKTIME          RFID.ATTENDANCE.CHECK_TIME%TYPE,
                                 P_MACHINE_IDENTIFIER RFID.ATTENDANCE.USER_ID %TYPE,
                                 P_MACHINE_ID         RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_MRNO               VARCHAR2,
                                 P_REASON             VARCHAR2,
                                 P_FROM_DATE          DATE,
                                 P_TO_DATE            DATE,
                                 P_LOCATION_ID        RFID.ATTENDANCE.LOCATION_ID%TYPE,
                                 P_STOP               OUT CHAR,
                                 P_ALERT_TEXT         OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_IS_RFID_NEW_SCHEME(P_DEPARTMENT_ID IN VARCHAR2) RETURN CHAR;

  /***********************************************************************************/
  PROCEDURE P_GRANT_RFID_ACCESS_NEW_SCHEME(P_MRNO        IN VARCHAR2,
                                           P_OBJECT_CODE IN VARCHAR2,
                                           P_STOP        OUT CHAR,
                                           P_ALERT_TEXT  OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_GET_EMP_SEX_ID(P_MRNO IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************************/
  FUNCTION F_GET_RFID_MACHINE_SEX_ID(P_MACHINE_ID IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************************/
  PROCEDURE P_INS_TRAINING_ATTENDANCE_STG(P_CHECKTIME  RFID.ATTENDANCE_EMPLOYEE.CHECK_TIME%TYPE,
                                          P_MACHINE_ID RFID.ATTENDANCE_EMPLOYEE.MACHINE_ID%TYPE,
                                          P_MRNO       VARCHAR2,
                                          P_REASON     VARCHAR2,
                                          P_RFID_CODE  RFID.ATTENDANCE_EMPLOYEE.rfid_code%TYPE,
                                          P_STOP       OUT CHAR,
                                          P_ALERT_TEXT OUT VARCHAR2);
  /***********************************************************************************/
  FUNCTION F_GET_TRAINING_ATTEND_MARK(P_MACHINE_ID RFID.RFID_MACHINES.MACHINE_ID%TYPE)
    RETURN CHAR;

END PKG_COMMON;
```

### RFID.PKG_RFID_MACHINES
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_MACHINES AS

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.RFID_MACHINES
  /******************************************************************************/

  TYPE RFID_MACHINES_REC IS RECORD(
    MACHINE_ID   RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    ACTIVE       RFID.RFID_MACHINES.ACTIVE%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO      RFID.RFID_MACHINES.PORT_NO%TYPE,
    ORDER_BY     RFID.RFID_MACHINES.ORDER_BY%TYPE,
    CATEGORY_ID  RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  TYPE RFID_MACHINES_TBL IS TABLE OF RFID_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE RFID_MACHINES_TBL_PF IS TABLE OF RFID_MACHINES_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/
  TYPE DEPT_MACHINES_RC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);

  TYPE DEPT_MACHINES_TL IS TABLE OF DEPT_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE DEPT_MACHINES_TL_PF IS TABLE OF DEPT_MACHINES_RC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/
  TYPE DEPT_MACHINES_REC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);

  TYPE DEPT_MACHINES_TBL IS TABLE OF DEPT_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE DEPT_MACHINES_TBL_PF IS TABLE OF DEPT_MACHINES_REC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_REC IS RECORD(
    MACHINE_ID RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO       RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE     RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE);

  TYPE EMP_MACHINES_TBL IS TABLE OF EMP_MACHINES_REC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TBL_PF IS TABLE OF EMP_MACHINES_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID  RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO        RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    NAME        HRD.V_INFORMATION.NAME%TYPE,
    DISP_MRNO   HRD.V_INFORMATION.DISP_MRNO%TYPE,
    DEPARTMENT  HRD.V_INFORMATION.DEPARTMENT%TYPE,
    DESIGNATION HRD.V_INFORMATION.DESIGNATION%TYPE,
    ACTIVE      RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE   HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : The following pipelined function will return table of records
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  FUNCTION F_RFID_MACHINES_QRY(P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                               P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                               P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                               P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                               P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                               P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                               P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                               P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE)
    RETURN RFID_MACHINES_TBL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_QRY(P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                                P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                                P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                P_DATA         IN OUT RFID_MACHINES_TBL,
                                P_STOP         OUT VARCHAR2,
                                P_ALERT_TEXT   OUT VARCHAR2,
                                P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                P_DATA            IN RFID_MACHINES_REC,
                                P_STOP            OUT VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_INS(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_LCK(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_UPD(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_DEL(P_DATA       IN OUT RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID.MACHINE_COMPLETE_DEPARTMENT
  -- Purpose   : The following pipelined function will return table of records
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  FUNCTION F_DEPT_MACHINES_QY(P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                              P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                              P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                              P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE)
    RETURN DEPT_MACHINES_TL_PF
    PIPELINED;

  PROCEDURE P_DEPT_MACHINES_QY(P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                               P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                               P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                               P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE,
                               P_DATA          IN OUT DEPT_MACHINES_TL,
                               P_STOP          OUT VARCHAR2,
                               P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                P_DATA            IN DEPT_MACHINES_RC,
                                P_STOP            OUT VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_INS(P_MACHINE_ID    OUT RFID.MACHINE_COMPLETE_DEPARTMENT .MACHINE_ID%TYPE,
                                P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_DATA          IN OUT DEPT_MACHINES_TL,
                                P_STOP          OUT VARCHAR2,
                                P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_LCK(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_UPD(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_DEL(P_DATA       IN OUT DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  FUNCTION F_EMP_MACHINES_QY(P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                             P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                             P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                             P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                             P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                             P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                             P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                             P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE)
    RETURN EMP_MACHINES_TL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                              P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                              P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                              P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                              P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_DATA        IN OUT EMP_MACHINES_TL,
                              P_STOP        OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for checking data validations of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : USMAN SHAUKAT (3821)
  -- Created on: 17-JUN-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to put data in RFID.RFID_DATA_TRANSFER
  --             for utility to send to machines.
  /******************************************************************************/

  PROCEDURE P_SEND_DATA_TO_MACHINE_V2(P_MACHINE_ID           IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_MRNO                 IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                      P_ACTION               IN CHAR,
                                      P_RFID_CODE            IN VARCHAR2 DEFAULT NULL,
                                      P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                      P_MACHINE_CODE         IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                      P_IP_ADDRESS           IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                      P_PORT_NO              IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                      P_MACHINE_LOCATION_ID  IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                                      P_MACHINE_CATEGORY     IN RFID.RFID_MACHINES.MACHINE_CATEGORY%TYPE,
                                      P_STOP                 OUT VARCHAR2,
                                      P_ALERT_TEXT           OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE P_SEND_DATA_TO_MACHINE(P_MACHINE_ID           IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                   P_MRNO                 IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                   P_ACTION               IN CHAR,
                                   P_STOP                 OUT VARCHAR2,
                                   P_ALERT_TEXT           OUT VARCHAR2,
                                   P_RFID_CODE            IN VARCHAR2 DEFAULT NULL,
                                   P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                   P_OBJECT_CODE          IN VARCHAR2 DEFAULT NULL,
                                   P_ACCESS_GRANT_EVENT   IN VARCHAR2 DEFAULT NULL);
  /*******************************************************************************/
  PROCEDURE P_COPY_MACHINE_RIGHTS(P_TYPE                 IN CHAR,
                                  P_MRNO                 IN VARCHAR2,
                                  P_MASTER_MRNO          IN VARCHAR2,
                                  P_MACHINE_ID           IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_MASTER_MACHINE_ID    IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_RFID_ATTENDANCE_TYPE IN VARCHAR2 DEFAULT 'A',
                                  P_STOP                 OUT CHAR,
                                  P_ALERT_TEXT           OUT VARCHAR);

  /******************************************************************************/
  -- Author    : USMAN SHAUKAT (3821)
  -- Created on: 17-JUN-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to reload already saved data to machine storage.
  /******************************************************************************/
  PROCEDURE P_RELOAD_MACHINE_DATA(P_MACHINE_ID IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-SEP-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to get rfid code against emp mrno.
  /******************************************************************************/

  FUNCTION f_get_rfid_code(P_MRNO IN VARCHAR2) return varchar;
  /*******************************************************************/
  PROCEDURE P_INACTIVE_CARD_CATAGORY(P_CARD_TYPE_ID IN RFID.RFID_CARD_TYPE.CARD_TYPE_ID%TYPE,
                                     P_CATEGORY_ID  IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
                                     P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                     P_RFID_CARD_NO IN RFID.RFID_CARDS.RFID_CARD_NO%TYPE,
                                     P_ACTION       IN VARCHAR2,
                                     P_STOP         OUT CHAR,
                                     P_ALERT_TEXT   OUT VARCHAR);
  /*******************************************************************/
  PROCEDURE P_DELETE_EMP_MACHINE_DATA(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO %TYPE,
                                      P_MACHINE_ID IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_STOP       OUT CHAR,
                                      P_ALERT_TEXT OUT VARCHAR);
  /*********************************************************************************/
  PROCEDURE P_REVOKE_MACHINE_RIGHTS(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                    P_STOP       OUT CHAR,
                                    P_ALERT_TEXT OUT VARCHAR);
  /*************************************************************************************/
  FUNCTION F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO       IN VARCHAR2,
                                          P_MACHINE_ID IN VARCHAR2)
    RETURN VARCHAR2;
  /************************************************************************************/
  FUNCTION F_IS_RFID_REQUIRED(P_MACHINE_ID IN VARCHAR2) RETURN CHAR;
  /**********************************************************************************/
  FUNCTION F_IS_ALREADY_FOUND_IN_MAPPING(P_MACHINE_ID IN VARCHAR2,
                                         P_MRNO       IN VARCHAR2)
    RETURN CHAR;
  /**********************************************************************************/
  FUNCTION F_GET_RFID_CODE_FROM_MAPPING(P_MACHINE_ID IN VARCHAR2,
                                        P_MRNO       IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/
  FUNCTION F_GET_MACHINE_WISE_MAX_COUNTER(P_MACHINE_ID IN VARCHAR2)
    RETURN NUMBER;
  /*********************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/
  FUNCTION F_GET_EMPLOYEE_CODE(P_MACHINE_CODE       IN VARCHAR2,
                               P_MACHINE_IDENTIFIER IN VARCHAR2,
                               P_LOCATION_ID        IN VARCHAR2)
    RETURN VARCHAR2;
  /**********************************************************************************/

  PROCEDURE P_NEW_MACHINE_SUPERCARD_ADD(P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_MACHINE_CODE        IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                        P_IP_ADDRESS          IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                        P_PORT_NO             IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                        P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                                        P_MACHINE_CATEGORY    IN RFID.RFID_MACHINES.MACHINE_CATEGORY%TYPE,
                                        P_EVENT               IN VARCHAR2,
                                        P_STOP                OUT CHAR,
                                        P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/
  PROCEDURE J_MISSED_MACHINE_IN_SUPERCARD(P_ALERT_TEXT OUT VARCHAR2,
                                          P_STOP       OUT VARCHAR2);
  /********************************************************************************************/
  PROCEDURE P_SYN_ATTENDANCE_EMP(P_MACHINE_ID RFID.ATTENDANCE.MACHINE_ID%TYPE,
                                 P_FROM_DATE  DATE,
                                 P_TO_DATE    DATE,
                                 P_STOP       OUT CHAR,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /********************************************************************************************/
  FUNCTION RFID_CARD_CODE_CONVERSION(P_STRING_VALUE IN VARCHAR2,
                                     P_MRNO         IN VARCHAR2,
                                     P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE)
    RETURN VARCHAR2;
  /********************************************************************************************/

END PKG_RFID_MACHINES;
```

### RFID.PKG_48FRM00102
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_48FRM00102 AS
  /**************************************************************************/
  PROCEDURE PRO_POPULATE_DESIGNATION(P_DEPARTMENT_ID IN VARCHAR2,
                                     P_STOP          OUT CHAR,
                                     P_ALERT_TEXT    OUT VARCHAR2);
  /**************************************************************************/
  FUNCTION F_GET_ALREADY_POPULATED(P_DEPARTMENT_ID IN VARCHAR2) RETURN NUMBER;
  /***********************************************************************/
  PROCEDURE P_REFRESH_DEPARTMENT(P_DEPARTMENT_ID IN VARCHAR2,
                                 P_LOCATION_ID   IN VARCHAR2,
                                 P_OBJECT_CODE   IN VARCHAR2,
                                 P_STOP          OUT CHAR,
                                 P_ALERT_TEXT    OUT VARCHAR2);
  /***********************************************************************/
  FUNCTION F_GET_IS_SUPER_CARD(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  /***********************************************************************/
  PROCEDURE P_GRANT_DEFAULT_ACCESS(P_MACHINE_ID         IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                   P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                   P_OBJECT_CODE        IN VARCHAR2,
                                   P_EVENT              IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                   P_ACCESS_GRANT_EVENT IN VARCHAR2,
                                   P_STOP               OUT VARCHAR2,
                                   P_ALERT_TEXT         OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REVOKE_DEFAULT_ACCESS(P_MACHINE_ID         IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                    P_LOCATION_ID        IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_OBJECT_CODE        IN VARCHAR2,
                                    P_EVENT              IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                    P_ACCESS_GRANT_EVENT IN VARCHAR2,
                                    P_STOP               OUT VARCHAR2,
                                    P_ALERT_TEXT         OUT VARCHAR2);
  /***************************************************************************************/
  PROCEDURE P_REVOKE_DEPT_DESIG_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                       P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                       P_OBJECT_CODE         IN VARCHAR2,
                                       P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                       P_DEPARTMENT_ID       IN VARCHAR2,
                                       P_DESIGNATION_ID      IN VARCHAR2,
                                       P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                       P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                       P_STOP                OUT VARCHAR2,
                                       P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_GRANT_DEPT_DESIG_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                      P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                      P_OBJECT_CODE         IN VARCHAR2,
                                      P_DEPARTMENT_ID       IN VARCHAR2,
                                      P_DESIGNATION_ID      IN VARCHAR2,
                                      P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                      P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                      P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                      P_STOP                OUT VARCHAR2,
                                      P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_GRANT_REVOKE_EMP_WISE_ACCESS(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                                           P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                           P_OBJECT_CODE         IN VARCHAR2,
                                           P_EMPLOYEE_CODE       IN VARCHAR2,
                                           P_EVENT               IN VARCHAR2, ---- THIS PARAMENTER WILL BE USE TO GRANT AND REVOKE RIGHTS
                                           P_ACCESS_GRANT_EVENT  IN VARCHAR2,
                                           P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                                           P_STOP                OUT VARCHAR2,
                                           P_ALERT_TEXT          OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REFRESH_EMP_WISE_ACCESS(P_MRNO        IN VARCHAR2,
                                      P_OBJECT_CODE IN VARCHAR2,
                                      P_STOP        OUT CHAR,
                                      P_ALERT_TEXT  OUT VARCHAR2);
  /****************************************************************************/
  PROCEDURE P_REFRESH_EMP_WISE_ACCESS(P_MRNO           IN VARCHAR2,
                                      P_DEPARTMENT_ID  IN VARCHAR2,
                                      P_DESIGNATION_ID IN VARCHAR2,
                                      P_OBJECT_CODE    IN VARCHAR2,
                                      P_STOP           OUT CHAR,
                                      P_ALERT_TEXT     OUT VARCHAR2);
  /****************************************************************************/
END;
```

### RFID.PKG_ACCESS_CONTROL_REPORTS
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_ACCESS_CONTROL_REPORTS AS
  /***********************************************************************************************
        PACKAGE NAME: RFID.PKG_ACCESS_CONTROL_REPORTS
        PURPOSE: THIS PACKAGE WILL AUTOMATE REPORTS
        ----------------------------------------------------------------------------------
        REVISIONS:
        VER        DATE         AUTHOR                  DESCRIPTION
        ---------  ----------   ---------------         -----------------------------------
       1.0        10-MAY-2024   AQIB KHALID             1. CREATED THIS PACKAGE.
  ************************************************************************************************/
  TYPE ISSUED_CARDS_REC IS RECORD(
    CATERGORY_DESCRIPTION   RFID.V_RFID_CARD_ISSUE_ACS.CATERGORY_DESCRIPTION%TYPE,
    SR                      RFID.V_RFID_CARD_ISSUE_ACS.SR%TYPE,
    RFID_CARD_NO            RFID.V_RFID_CARD_ISSUE_ACS.RFID_CARD_NO%TYPE,
    NAME                    RFID.V_RFID_CARD_ISSUE_ACS.NAME%TYPE,
    MRNO                    RFID.V_RFID_CARD_ISSUE_ACS.MRNO%TYPE,
    PATIENT_NAME            RFID.V_RFID_CARD_ISSUE_ACS.PATIENT_NAME%TYPE,
    ARMY_RANK               REGISTRATION.V_RFID_PATIENT.ARMY_RANK%TYPE,
    service_no              REGISTRATION.V_RFID_PATIENT.service_no%TYPE,
    WARD_ID                 RFID.V_RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    WARD                    RFID.V_RFID_CARD_ISSUE_ACS.WARD%TYPE,
    ISSUE_DATE              RFID.V_RFID_CARD_ISSUE_ACS.ISSUE_DATE%TYPE,
    RECEIVE_DATE            RFID.V_RFID_CARD_ISSUE_ACS.RECEIVE_DATE%TYPE,
    RETURN                  RFID.V_RFID_CARD_ISSUE_ACS.RETURN%TYPE,
    CARD_CATEGORY_ID        RFID.V_RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE,
    ISSUED_BY               RFID.V_RFID_CARD_ISSUE_ACS.ISSUED_BY%TYPE,
    REMARKS                 RFID.V_RFID_CARD_ISSUE_ACS.REMARKS%TYPE,
    NIC                     RFID.V_RFID_CARD_ISSUE_ACS.NIC%TYPE,
    RELATION_ID             RFID.V_RFID_CARD_ISSUE_ACS.RELATION_ID%TYPE,
    ADDRESS                 RFID.V_RFID_CARD_ISSUE_ACS.ADDRESS%TYPE,
    RETURN_DATE             RFID.V_RFID_CARD_ISSUE_ACS.RETURN_DATE%TYPE,
    RIGHTS_STATUS           RFID.V_RFID_CARD_ISSUE_ACS.RIGHTS_STATUS%TYPE,
    CARD_DESCRIPTION        RFID.V_RFID_CARD_ISSUE_ACS.CARD_DESCRIPTION%TYPE,
    RELATION                RFID.V_RFID_CARD_ISSUE_ACS.RELATION%TYPE,
    ISSUED_BY_NAME          RFID.V_RFID_CARD_ISSUE_ACS.ISSUED_BY_NAME%TYPE,
    MACHINE_CATEGORY        RFID.V_RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY%TYPE,
    MACHINE_CATEGORY_ID     RFID.V_RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY_ID%TYPE,
    IS_EXTENDED             RFID.V_RFID_CARD_ISSUE_ACS.IS_EXTENDED%TYPE,
    CONTACT_NO              RFID.V_RFID_CARD_ISSUE_ACS.CONTACT_NO%TYPE,
    location_id             RFID.V_RFID_CARD_ISSUE_ACS.location_id%TYPE,
    BUILDING_BLOCK_ID       RFID.V_RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
    BUILDING_BLOCK_FLOOR_ID RFID.V_RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_FLOOR_ID%TYPE,
    card_valid_till         RFID.V_RFID_CARD_ISSUE_ACS.card_valid_till%TYPE);
  --------------------------------------------------------------------
  TYPE ISSUED_CARDS_TAB IS TABLE OF ISSUED_CARDS_REC;
  -----------------------------------------------------------------------------------
  FUNCTION ISSUED_CARDS_REPORT(P_FROM_DATE   DATE,
                               P_TO_DATE     DATE,
                               P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                               P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                               P_CARD_CAT_ID IN RFID.RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.ISSUED_CARDS_TAB
    PIPELINED;
  ---------------------------------------------------------------------------------
  TYPE BUILD_WISE_WARD_REC IS RECORD(
    WARD              VARCHAR2(4000),
    WARD_ID           RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    LOCATION_ID       RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
    BUILDING_BLOCK_ID RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
    IN_COUNT          NUMBER,
    OUT_COUNT         NUMBER);
  -------------------------------------------------------------------------------------------------------------------------
  TYPE BUILD_WISE_WARD_TAB IS TABLE OF BUILD_WISE_WARD_REC;
  --------------------------------------------------------------------------------------------------------------------------
  FUNCTION BUILDING_WISE_WARDS_COUNT(P_FROM_DATE   DATE,
                                     P_TO_DATE     DATE,
                                     P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                     P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                                     P_WARD_ID     IN RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.BUILD_WISE_WARD_TAB
    PIPELINED;
  /************************************************************************************************/
  TYPE EMP_CARD_INOUT_REC IS RECORD(
    MRNO                RFID.ATTENDANCE_EMPLOYEE.MRNO%TYPE,
    EMP_NAME            VARCHAR2(4000),
    NAME                VARCHAR2(4000),
    ARMY_RANK           VARCHAR2(4000),
    service_no          VARCHAR2(4000),
    IN_TIME             DATE,
    OUT_TIME            DATE,
    MACHINE_LOCATION_ID RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE);
  -------------------------------------------------------------------------------------------------------------------------
  TYPE EMP_CARD_INOUT_TAB IS TABLE OF EMP_CARD_INOUT_REC;
  ----------------------------------------------------------
  FUNCTION EMP_CARD_INOUT_DETAIL(P_FROM_DATE   DATE,
                                 P_TO_DATE     DATE,
                                 P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                 P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.EMP_CARD_INOUT_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------------------------------------
  TYPE TOP_TEN_VISITORS_REC IS RECORD(
    NAME         RFID.V_RFID_CARD_SWIPE_DETAILS.NAME%TYPE,
    NIC          RFID.V_RFID_CARD_SWIPE_DETAILS.NIC%TYPE,
    CONTACT_NO   RFID.V_RFID_CARD_SWIPE_DETAILS.CONTACT_NO%TYPE,
    RFID_CARD_NO RFID.V_RFID_CARD_SWIPE_DETAILS.RFID_CARD_NO%TYPE,
    MRNO         RFID.V_RFID_CARD_SWIPE_DETAILS.MRNO%TYPE,
    PATIENT_NAME RFID.V_RFID_CARD_SWIPE_DETAILS.PATIENT_NAME%TYPE,
    ARMY_RANK    RFID.V_RFID_CARD_SWIPE_DETAILS.ARMY_RANK%TYPE,
    LOCATION_ID  RFID.V_RFID_CARD_SWIPE_DETAILS.LOCATION_ID%TYPE,
    VISITS_COUNT NUMBER);
  -----------------------------------------------------------------------------
  TYPE TOP_TEN_VISITORS_TAB IS TABLE OF TOP_TEN_VISITORS_REC;
  ----------------------------------------------------------------------------------
  FUNCTION TOP_TEN_VISITORS(P_FROM_DATE   DATE,
                            P_TO_DATE     DATE,
                            P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                            P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_TEN_VISITORS_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------------------------------------
  TYPE TOP_FIVE_WARD_REC IS RECORD(
    WARD           RFID.V_RFID_CARD_ISSUE_ACS.WARD%TYPE,
    WARD_ID        RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
    LOCATION_ID    RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
    VISITORS_COUNT NUMBER);
  -----------------------------------------------------------------------------
  TYPE TOP_FIVE_WARD_TAB IS TABLE OF TOP_FIVE_WARD_REC;
  ----------------------------------------------------------------------------------
  FUNCTION TOP_FIVE_WARDS(P_FROM_DATE   DATE,
                          P_TO_DATE     DATE,
                          P_LOCATION_ID IN RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                          P_BUILDING_ID IN RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE)
    RETURN RFID.PKG_ACCESS_CONTROL_REPORTS.TOP_FIVE_WARD_TAB
    PIPELINED;
  ------------------------------------------------------------------------------------------
  FUNCTION F_WARD_WISE_CARD_SWIPE_COUNT(P_LOCATION_ID       RFID.RFID_CARD_ISSUE_ACS.LOCATION_ID%TYPE,
                                        P_BUILDING_BLOCK_ID RFID.RFID_CARD_ISSUE_ACS.BUILDING_BLOCK_ID%TYPE,
                                        P_WARD_ID           RFID.RFID_CARD_ISSUE_ACS.WARD_ID%TYPE,
                                        -- P_MACHINE_ID        RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_MACHINE_TYPE RFID.RFID_MACHINES.DEFAULT_CHECK_IN_OUT%TYPE)
    RETURN NUMBER;
END;
```

### RFID.PKG_MACHINE_WISE_EMPLOYEE
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_MACHINE_WISE_EMPLOYEE AS

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following record type, table types will be used
  --             for dml of HRD.INFORMATION
  /******************************************************************************/

  TYPE HRD_INFO IS RECORD(
    DESIGNATION_ID HRD.INFORMATION.DESIGNATION_ID%TYPE,
    MRNO           HRD.INFORMATION.MRNO%TYPE,
    DISP_MRNO      VARCHAR2(11),
    NAME           REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT     DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DEPARTMENT_ID  DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    JOINING_DATE   HRD.INFORMATION.JOINING_DATE%TYPE,
    RFID_CODE      HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE HRD_INFO_TBL IS TABLE OF HRD_INFO INDEX BY PLS_INTEGER;
  TYPE HRD_INFO_TBL_PF IS TABLE OF HRD_INFO; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following record type, table types will be used
  --             for dml of RFID.machine_wise_employee
  /******************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID   RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    MRNO         RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE       RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE    HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : The following pipelined function will return table of records
  --             HRD.INFORMATION.
  /******************************************************************************/

  FUNCTION F_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                          P_MRNO           IN HRD.INFORMATION.MRNO%TYPE,
                          P_DISP_MRNO      IN VARCHAR2,
                          P_NAME           IN REGISTRATION.PATIENT.NAME%TYPE,
                          P_DESIGNATION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                          P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                          P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE)

   RETURN HRD_INFO_TBL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for querying data of
  --             HRD.INFORMATION.
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_QRY(P_DESIGNATION_ID IN HRD.INFORMATION.DESIGNATION_ID%TYPE,
                           P_MRNO           IN HRD.INFORMATION.MRNO%TYPE,
                           P_DISP_MRNO      IN VARCHAR2,
                           P_NAME           IN REGISTRATION.PATIENT.NAME%TYPE,
                           P_DESIGNATION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                           P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                           P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                           P_DATA           IN OUT HRD_INFO_TBL,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for locking of
  --             HRD.INFORMATION.
  /******************************************************************************/
  /*
  PROCEDURE P_EMP_INFO_LCK(P_DATA       IN OUT HRD_INFO_TBL,
                           P_STOP       OUT VARCHAR2,
                           P_ALERT_TEXT OUT VARCHAR2);*/
  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for checking data validations of
  --             HRD.INFORMATION.
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                           P_DATA            IN HRD_INFO,
                           P_STOP            OUT VARCHAR2,
                           P_ALERT_TEXT      OUT VARCHAR2);

  FUNCTION F_EMP_MACHINES_QY(P_MACHINE_ID   IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                             P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                             P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                             P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                             P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                             P_MRNO         IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                             P_ACTIVE       IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                             P_RFID_CODE    IN HRD.INFORMATION.RFID_CODE%TYPE)
    RETURN EMP_MACHINES_TL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for querying data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID   IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                              P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                              P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                              P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                              P_MRNO         IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_ACTIVE       IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE    IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_DATA         IN OUT EMP_MACHINES_TL,
                              P_STOP         OUT VARCHAR2,
                              P_ALERT_TEXT   OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for checking data validations of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for inserting data in
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for locking data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for updating data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 06-June-2013
  -- Scope     : EMP INFORMATION
  -- Purpose   : This procedure will be used for deleting data of
  --             rfid.machine_wise_employee.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 30-SEP-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used to get rfid code against emp mrno.
  /******************************************************************************/

  FUNCTION f_get_rfid_code(P_MRNO IN VARCHAR2) return varchar;
  /******************************************************************************/
  -- Author    : MAHBOOB ALAM (6579)
  -- Created on: 04-11-2015
  -- Scope     : RFID MACHINES FOR SUPER CARD
  /******************************************************************************/
  PROCEDURE P_SUPER_CARD_MACHINE_INS(P_MRNO       IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                                     P_EVENT      IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                                     P_STOP       OUT CHAR,
                                     P_ALERT_TEXT OUT VARCHAR2);
  /**************************************************************************/
  FUNCTION F_IS_CONFIDENTIAL(P_MACHINE_ID IN VARCHAR2) RETURN VARCHAR2;
  /**************************************************************************/
PROCEDURE P_REVOKE_SUP_CARD_ACCESS(P_MRNO        IN VARCHAR2,
                                     P_OBJECT_CODE IN VARCHAR2,
                                     P_STOP        OUT CHAR,
                                     P_ALERT_TEXT  OUT VARCHAR2);
  /**************************************************************************/

END PKG_MACHINE_WISE_EMPLOYEE;
```

### RFID.PKG_RFID
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID IS

  ----------------------------------------------------------------------
  TYPE RFID_MACHINE_RECORD IS RECORD(
    MACHINE_ID RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    ACCESS_LEVEL CHAR(6));

  ------------------
  -- PL/SQL Array --
  ------------------
  TYPE RFID_MACHINE_TAB IS TABLE OF RFID.PKG_RFID.RFID_MACHINE_RECORD;

  -----------------------------------------------------------------------
  -- Pipelined Function which will return the RFID MACHINES LIST --
  -----------------------------------------------------------------------
  FUNCTION GET_RFID_MACHINES(P_EMP_CODE IN HRD.INFORMATION.MRNO%TYPE)
    RETURN RFID_MACHINE_TAB
    PIPELINED;

END PKG_RFID;
```

### RFID.PKG_RFID_ACCESS_SYNC
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_ACCESS_SYNC AS

  PROCEDURE LOG_EVENT
  (
      P_RUN_ID              IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE,
      P_EVENT_TYPE          IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE,
      P_EVENT_SOURCE        IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE,
      P_MRNO                IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE,
      P_MACHINE_ID          IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE,
      P_EMP_LOCATION_ID     IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID       IN RFID.RFID_ACCESS_SYNC_LOG.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID      IN RFID.RFID_ACCESS_SYNC_LOG.DESIGNATION_ID%TYPE,
      P_SEX_ID              IN RFID.RFID_ACCESS_SYNC_LOG.SEX_ID%TYPE,
      P_RFID_SUPER_CARD     IN RFID.RFID_ACCESS_SYNC_LOG.RFID_SUPER_CARD%TYPE,
      P_MACHINE_ACCESS_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ACCESS_TYPE%TYPE,
      P_ACCESS_GRANT_EVENT  IN RFID.RFID_ACCESS_SYNC_LOG.ACCESS_GRANT_EVENT%TYPE,
      P_REMARKS             IN RFID.RFID_ACCESS_SYNC_LOG.REMARKS%TYPE,
      P_OLD_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.OLD_ROW_JSON%TYPE,
      P_NEW_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.NEW_ROW_JSON%TYPE
  );

  PROCEDURE GET_EMP_CONTEXT
  (
      P_MRNO             IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_LOCATION_ID      OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID    OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID   OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
      P_RFID_SUPER_CARD  OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
      P_SEX_ID           OUT REGISTRATION.PATIENT.SEX_ID%TYPE
  );

  FUNCTION FN_EFFECTIVE_SETUP_RIGHTS
  (
      P_MRNO             IN HRD.VU_INFORMATION.MRNO%TYPE,
      P_LOCATION_ID      IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
      P_DEPARTMENT_ID    IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
      P_DESIGNATION_ID   IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
      P_RFID_SUPER_CARD  IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
      P_SEX_ID           IN REGISTRATION.PATIENT.SEX_ID%TYPE
  ) RETURN RFID.TAB_SETUP_RIGHT PIPELINED;

  PROCEDURE PR_PREVIEW_EMPLOYEE_SYNC
  (
      P_MRNO               IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_MISSING_IN_MWE     OUT SYS_REFCURSOR,
      P_MWE_MINUS_SETUP    OUT SYS_REFCURSOR
  );

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS
  (
      P_MRNO           IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_DO_COMMIT      IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID         OUT NUMBER --RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS_FAST
  (
      P_MRNO           IN  HRD.VU_INFORMATION.MRNO%TYPE,
      P_DO_COMMIT      IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID         OUT NUMBER --RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

  PROCEDURE PR_SYNC_LOCATION_ACCESS
  (
      P_EMP_LOCATION_ID IN  HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL,
      P_DO_COMMIT       IN  VARCHAR2 DEFAULT 'Y',
      P_RUN_ID          OUT NUMBER -- RFID.RFID_ACCESS_SYNC_RUN.RUN_ID%TYPE
  );

PROCEDURE PR_CLEANUP_REDUNDANT_RFID_SETUP
(
    P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,   -- NULL = all active employee locations
    P_COMMIT          IN VARCHAR2 DEFAULT 'Y'     -- Y/N
);



END PKG_RFID_ACCESS_SYNC;
```

### RFID.PKG_RFID_ACCESS_SYNC01
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_ACCESS_SYNC01 AS

  PROCEDURE LOG_EVENT(P_RUN_ID              IN RFID.RFID_ACCESS_SYNC_LOG.RUN_ID%TYPE,
                      P_EVENT_TYPE          IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_TYPE%TYPE,
                      P_EVENT_SOURCE        IN RFID.RFID_ACCESS_SYNC_LOG.EVENT_SOURCE%TYPE,
                      P_MRNO                IN RFID.RFID_ACCESS_SYNC_LOG.MRNO%TYPE,
                      P_MACHINE_ID          IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ID%TYPE,
                      P_EMP_LOCATION_ID     IN RFID.RFID_ACCESS_SYNC_LOG.EMP_LOCATION_ID%TYPE,
                      P_DEPARTMENT_ID       IN RFID.RFID_ACCESS_SYNC_LOG.DEPARTMENT_ID%TYPE,
                      P_DESIGNATION_ID      IN RFID.RFID_ACCESS_SYNC_LOG.DESIGNATION_ID%TYPE,
                      P_SEX_ID              IN RFID.RFID_ACCESS_SYNC_LOG.SEX_ID%TYPE,
                      P_RFID_SUPER_CARD     IN RFID.RFID_ACCESS_SYNC_LOG.RFID_SUPER_CARD%TYPE,
                      P_MACHINE_ACCESS_TYPE IN RFID.RFID_ACCESS_SYNC_LOG.MACHINE_ACCESS_TYPE%TYPE,
                      P_ACCESS_GRANT_EVENT  IN RFID.RFID_ACCESS_SYNC_LOG.ACCESS_GRANT_EVENT%TYPE,
                      P_REMARKS             IN RFID.RFID_ACCESS_SYNC_LOG.REMARKS%TYPE,
                      P_OLD_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.OLD_ROW_JSON%TYPE,
                      P_NEW_ROW_JSON        IN RFID.RFID_ACCESS_SYNC_LOG.NEW_ROW_JSON%TYPE);

  PROCEDURE GET_EMP_CONTEXT(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                            P_LOCATION_ID     OUT HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
                            P_DEPARTMENT_ID   OUT HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
                            P_DESIGNATION_ID  OUT HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
                            P_RFID_SUPER_CARD OUT HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                            P_SEX_ID          OUT REGISTRATION.PATIENT.SEX_ID%TYPE);

  FUNCTION FN_EFFECTIVE_SETUP_RIGHTS(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                                     P_LOCATION_ID     IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE,
                                     P_DEPARTMENT_ID   IN HRD.VU_INFORMATION.DEPARTMENT_ID%TYPE,
                                     P_DESIGNATION_ID  IN HRD.VU_INFORMATION.DESIGNATION_ID%TYPE,
                                     P_RFID_SUPER_CARD IN HRD.INFORMATION.RFID_SUPER_CARD%TYPE,
                                     P_SEX_ID          IN REGISTRATION.PATIENT.SEX_ID%TYPE)
    RETURN RFID.TAB_SETUP_RIGHT
    PIPELINED;

  PROCEDURE PR_PREVIEW_EMPLOYEE_SYNC(P_MRNO            IN HRD.VU_INFORMATION.MRNO%TYPE,
                                     P_MISSING_IN_MWE  OUT SYS_REFCURSOR,
                                     P_MWE_MINUS_SETUP OUT SYS_REFCURSOR);

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS(P_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                    P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y',
                                    P_RUN_ID    OUT NUMBER);

  PROCEDURE PR_SYNC_EMPLOYEE_ACCESS_FAST(P_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                         P_DO_COMMIT IN VARCHAR2 DEFAULT 'Y',
                                         P_RUN_ID    OUT NUMBER);

  PROCEDURE PR_SYNC_LOCATION_ACCESS(P_EMP_LOCATION_ID IN HRD.VU_INFORMATION.EMP_LOCATION_ID%TYPE DEFAULT NULL,
                                    P_DO_COMMIT       IN VARCHAR2 DEFAULT 'Y',
                                    P_RUN_ID          OUT NUMBER);

  ------------------------------------------------------------------
  -- NEW CLEANUP & PREVIEW PROCEDURES
  ------------------------------------------------------------------

  PROCEDURE PR_PREVIEW_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                             P_RESULT          OUT SYS_REFCURSOR);

  PROCEDURE PR_PREVIEW_REDUNDANT_RFID_ACCESS_SUMMARY(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                                     P_RESULT          OUT SYS_REFCURSOR);

  PROCEDURE PR_CLEANUP_REDUNDANT_RFID_ACCESS(P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,
                                             P_COMMIT          IN VARCHAR2 DEFAULT 'Y');

END PKG_RFID_ACCESS_SYNC01;
```

### RFID.PKG_RFID_CARD_ISSUE_ACS
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_CARD_ISSUE_ACS AS

  /******************************************************************************/
  -- Author    : AQIB KHALID (7346)
  -- Created on: 30-JAN-2024
  -- Purpose   : RFID.PKG_RFID_CARD_ISSUE_ACS.
  /******************************************************************************/

  PROCEDURE P_RFID_CARD_ISSUE(P_EVENT               IN CHAR,
                              P_SR                  IN RFID.RFID_CARD_ISSUE_ACS.SR%TYPE,
                              P_RFID_CARD_NO        IN RFID.RFID_CARD_ISSUE_ACS.RFID_CARD_NO%TYPE,
                              P_NAME                IN RFID.RFID_CARD_ISSUE_ACS.NAME%TYPE,
                              P_MRNO                IN RFID.RFID_CARD_ISSUE_ACS.MRNO%TYPE,
                              P_ISSUE_DATE          IN RFID.RFID_CARD_ISSUE_ACS.ISSUE_DATE%TYPE,
                              P_RECEIVE_DATE        IN RFID.RFID_CARD_ISSUE_ACS.RECEIVE_DATE%TYPE,
                              P_RETURN              IN RFID.RFID_CARD_ISSUE_ACS.RETURN%TYPE,
                              P_CARD_CATEGORY_ID    IN RFID.RFID_CARD_ISSUE_ACS.CARD_CATEGORY_ID%TYPE,
                              P_machine_CATEGORY_ID IN RFID.RFID_CARD_ISSUE_ACS.MACHINE_CATEGORY_ID%TYPE,
                              P_ISSUED_BY           IN RFID.RFID_CARD_ISSUE_ACS.ISSUED_BY%TYPE,
                              P_REMARKS             IN RFID.RFID_CARD_ISSUE_ACS.REMARKS%TYPE,
                              P_NIC                 IN RFID.RFID_CARD_ISSUE_ACS.NIC%TYPE,
                              P_RELATION_ID         IN RFID.RFID_CARD_ISSUE_ACS.RELATION_ID%TYPE,
                              P_ADDRESS             IN RFID.RFID_CARD_ISSUE_ACS.ADDRESS%TYPE,
                              P_CONTACT_NO          IN RFID.RFID_CARD_ISSUE_ACS.CONTACT_NO%TYPE,
                              P_RETURN_DATE         IN RFID.RFID_CARD_ISSUE_ACS.RETURN_DATE%TYPE,
                              P_CARD_DESC           IN RFID.RFID_CARD_ISSUE_ACS.CARD_DESC%TYPE,
                              P_LOCATION_ID         IN VARCHAR2,
                              P_STOP                OUT VARCHAR2,
                              P_ALERT_TEXT          OUT VARCHAR2);

  PROCEDURE JOB_RFID_CARD_RIGHTS_ACS(P_MRNO                IN VARCHAR2 DEFAULT NULL,
                                     P_MACHINE_CATEGORY_ID IN NUMBER DEFAULT NULL);
END PKG_RFID_CARD_ISSUE_ACS;
```

### RFID.PKG_RFID_DATA_TRANSFER
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_RFID_DATA_TRANSFER AS

  TYPE V_RFID_REC IS RECORD(
    MACHINE_CODE  RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
    IP_ADDRESS    RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
    PORT_NO       RFID.RFID_DATA_TRANSFER.PORT_NO%TYPE,
    MRNO          RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
    USER_NAME     RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
    USER_PASSWORD RFID.RFID_DATA_TRANSFER.USER_PASSWORD%TYPE,
    PRIVILEGE     RFID.RFID_DATA_TRANSFER.PRIVILEGE%TYPE,
    ENABLED       RFID.RFID_DATA_TRANSFER.ENABLED%TYPE,
    RFID_CARD_NO  RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
    MACHINE_NAME  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    MACHINE_TYPE  RFID.RFID_MACHINES.MACHINE_TYPE%TYPE--- COLUMN ADDED BY ASMA HASHMI (6-4806) DATED 30-03-2015 11:40AM
    );

  TYPE V_RFID_TBL IS TABLE OF V_RFID_REC INDEX BY PLS_INTEGER;
  TYPE V_RFID_TBL_PF IS TABLE OF V_RFID_REC; /* FOR PIPLINED FUNCTION */

  FUNCTION F_V_RFID_QRY(P_MRNO         IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
                        P_USER_NAME    IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                        P_RFID_CODE    IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                        P_IP_ADDRESS   IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                        P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE)
    RETURN V_RFID_TBL_PF
    PIPELINED;

  PROCEDURE P_V_RFID_QRY(P_MRNO         IN RFID.RFID_DATA_TRANSFER.MRNO%TYPE,
                         P_USER_NAME    IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                         P_RFID_CODE    IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                         P_IP_ADDRESS   IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                         P_MACHINE_CODE RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
                         P_DATA         IN OUT V_RFID_TBL,
                         P_STOP         OUT VARCHAR2,
                         P_ALERT_TEXT   OUT VARCHAR2);

  PROCEDURE P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                         P_DATA            IN V_RFID_REC,
                         P_STOP            OUT VARCHAR2,
                         P_ALERT_TEXT      OUT VARCHAR2);

  PROCEDURE P_V_RFID_INS(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_LCK(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_UPD(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_DEL(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

END;
```

### RFID.PKG_S07FRM00031
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S07FRM00031 AS

  TYPE V_RFID_REC IS RECORD(
    MACHINE_CODE         RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
    IP_ADDRESS           RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
    PORT_NO              RFID.RFID_DATA_TRANSFER.PORT_NO%TYPE,
    MACHINE_IDENTIFIER   RFID.RFID_DATA_TRANSFER.MACHINE_IDENTIFIER%TYPE,
    USER_NAME            RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
    USER_PASSWORD        RFID.RFID_DATA_TRANSFER.USER_PASSWORD%TYPE,
    PRIVILEGE            RFID.RFID_DATA_TRANSFER.PRIVILEGE%TYPE,
    ENABLED              RFID.RFID_DATA_TRANSFER.ENABLED%TYPE,
    RFID_CARD_NO         RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
    MACHINE_NAME         RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    MACHINE_TYPE         RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
    COMPLETE_MRNO        RFID.RFID_DATA_TRANSFER.COMPLETE_MRNO%TYPE,
    RFID_ATTENDANCE_TYPE RFID.RFID_DATA_TRANSFER.RFID_ATTENDANCE_TYPE%TYPE);

  TYPE V_RFID_REC_CUR IS REF CURSOR RETURN V_RFID_REC;
  TYPE V_RFID_TBL IS TABLE OF V_RFID_REC INDEX BY PLS_INTEGER;

  PROCEDURE P_V_RFID_QRY(P_MRNO               IN HRD.V_INFORMATION.MRNO%TYPE,
                         P_USER_NAME          IN RFID.RFID_DATA_TRANSFER.USER_NAME%TYPE,
                         P_RFID_CODE          IN RFID.RFID_DATA_TRANSFER.RFID_CARD_NO%TYPE,
                         P_IP_ADDRESS         IN RFID.RFID_DATA_TRANSFER.IP_ADDRESS%TYPE,
                         P_MACHINE_CODE       IN RFID.RFID_DATA_TRANSFER.MACHINE_CODE%TYPE,
                         P_MACHINE_IDENTIFIER IN RFID.RFID_DATA_TRANSFER.MACHINE_IDENTIFIER%TYPE,
                         P_MACHINE_LOCATION_ID IN RFID.RFID_MACHINES.MACHINE_LOCATION_ID%TYPE,
                         P_DATA               IN OUT V_RFID_REC_CUR,
                         P_STOP               OUT VARCHAR2,
                         P_ALERT_TEXT         OUT VARCHAR2);

  PROCEDURE P_V_RFID_INS(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_LCK(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_UPD(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_V_RFID_DEL(P_DATA       IN OUT V_RFID_TBL,
                         P_STOP       OUT VARCHAR2,
                         P_ALERT_TEXT OUT VARCHAR2);
  /**********************************************************************************************/

  PROCEDURE P_V_RFID_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                         P_DATA            IN V_RFID_REC,
                         P_STOP            OUT VARCHAR2,
                         P_ALERT_TEXT      OUT VARCHAR2);
END;
```

### RFID.PKG_S48FRM00024
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00024 AS

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.RFID_MACHINES
  /******************************************************************************/

  /*add by Mahboob Alam */
  TYPE RFID_MACHINES_REC IS RECORD(
    MACHINE_ID   RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    DESCRIPTION  RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC   RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    ACTIVE       RFID.RFID_MACHINES.ACTIVE%TYPE,
    MACHINE_CODE RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS   RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO      RFID.RFID_MACHINES.PORT_NO%TYPE,
    ORDER_BY     RFID.RFID_MACHINES.ORDER_BY%TYPE,
    CATEGORY_ID  RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  -----------------------------------------------------------------------
  TYPE RFID_MACHINES_REC_REFCUR IS REF CURSOR RETURN RFID_MACHINES_REC;
  ----------------------------------------------------------------------
  PROCEDURE P_RFID_MACHINES_QRY(P_DATA         IN OUT RFID_MACHINES_REC_REFCUR,
                                P_MACHINE_ID   IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                P_DESCRIPTION  IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                P_SHORT_DESC   IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                                P_ACTIVE       IN RFID.RFID_MACHINES.ACTIVE%TYPE,
                                P_MACHINE_CODE IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                                P_IP_ADDRESS   IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                P_PORT_NO      IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                 P_STOP         OUT VARCHAR2,
                                 P_ALERT_TEXT   OUT VARCHAR2,
                                P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_INS(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : RFID MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.RFID_MACHINES.
  /******************************************************************************/

  PROCEDURE P_RFID_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.RFID_MACHINES_TBL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT
  /******************************************************************************/

  -------------------------------------------------------------------------------------
  /* ADD BY MAHBOOB ALAM*/
  TYPE RFID_DEPT_MACHINES_RC IS RECORD(
    MACHINE_ID    RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
    DEPARTMENT_ID RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT    DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    ACTIVE        RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE);
  ------------------------------------------------------------
  TYPE RFID_DEPT_MACHINES_REFCUR IS REF CURSOR RETURN RFID_DEPT_MACHINES_RC;

  PROCEDURE P_DEPT_MACHINES_QY(P_DATA          IN OUT RFID_DEPT_MACHINES_REFCUR,
                               P_MACHINE_ID    IN RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                               P_DEPARTMENT_ID IN RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                               P_DEPARTMENT    IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                               P_ACTIVE        IN RFID.MACHINE_COMPLETE_DEPARTMENT.ACTIVE%TYPE,
                               P_STOP          OUT VARCHAR2,
                               P_ALERT_TEXT    OUT VARCHAR2

                               );

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_INS(P_MACHINE_ID    OUT RFID.MACHINE_COMPLETE_DEPARTMENT.MACHINE_ID%TYPE,
                                P_DEPARTMENT_ID OUT RFID.MACHINE_COMPLETE_DEPARTMENT.DEPARTMENT_ID%TYPE,
                                P_DATA          IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP          OUT VARCHAR2,
                                P_ALERT_TEXT    OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : DEPT MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_COMPLETE_DEPARTMENT.
  /******************************************************************************/

  PROCEDURE P_DEPT_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.DEPT_MACHINES_TL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_WISE_EMPLOYEE
  /******************************************************************************/

  /* ADD BY MAHBOOB ALAM*/
  ------------------------------------------------------------------------------
    TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID  RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    MRNO        RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    NAME        HRD.V_INFORMATION.NAME%TYPE,
    DISP_MRNO   HRD.V_INFORMATION.DISP_MRNO%TYPE,
    DEPARTMENT  HRD.V_INFORMATION.DEPARTMENT%TYPE,
    DESIGNATION HRD.V_INFORMATION.DESIGNATION%TYPE,
    ACTIVE      RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE   HRD.INFORMATION.RFID_CODE%TYPE);
    ------------------------------------------------------------------------
  TYPE RFID_EMP_MACHINES_REFCUR IS REF CURSOR RETURN EMP_MACHINES_RC;
  -------------------------------------------------------------------------
  PROCEDURE P_EMP_MACHINES_QY(P_DATA        IN OUT RFID_EMP_MACHINES_REFCUR,
                              P_MACHINE_ID  IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_MRNO        IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_NAME        IN HRD.V_INFORMATION.NAME%TYPE,
                              P_DISP_MRNO   IN HRD.V_INFORMATION.DISP_MRNO%TYPE,
                              P_DEPARTMENT  IN HRD.V_INFORMATION.DEPARTMENT%TYPE,
                              P_DESIGNATION IN HRD.V_INFORMATION.DESIGNATION%TYPE,
                              P_ACTIVE      IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE   IN HRD.INFORMATION.RFID_CODE%TYPE ,
                             P_STOP        OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2
                             );

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 27-MAY-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT RFID.PKG_RFID_MACHINES.EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  TYPE RFID_CATEGORY_REC IS RECORD(
    CATEGORY_ID       RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
    DESCRIPTION       RFID.RFID_CATEGORY.DESCRIPTION%TYPE,
    SHORT_DESCRIPTION RFID.RFID_CATEGORY.SHORT_DESCRIPTION%TYPE,
    IS_DEFAULT        RFID.RFID_CATEGORY.IS_DEFAULT%TYPE,
    ACTIVE            RFID.RFID_CATEGORY.ACTIVE%TYPE);
  TYPE RFID_CATEGORY_TBL IS TABLE OF RFID_CATEGORY_REC INDEX BY PLS_INTEGER;
  TYPE RFID_CATEGORY_CUR IS REF CURSOR RETURN RFID_CATEGORY_REC;
  /******************************************************************************/
  PROCEDURE P_RFID_CATEGORY_QRY(P_DATA        IN OUT RFID_CATEGORY_CUR,
                                P_CATEGORY_ID IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE,
                                P_DESCRIPTION IN RFID.RFID_CATEGORY.DESCRIPTION%TYPE,
                                P_SHORT_DESC  IN RFID.RFID_CATEGORY.SHORT_DESCRIPTION%TYPE,
                                P_DEFAULT     IN RFID.RFID_CATEGORY.IS_DEFAULT%TYPE,
                                P_ACTIVE      IN RFID.RFID_CATEGORY.ACTIVE%TYPE);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_INSERT(R            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_LOCK(R            IN OUT RFID_CATEGORY_TBL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_UPDATE(T            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  PROCEDURE RFID_CATEGORY_DELETE(T            IN RFID_CATEGORY_TBL,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  TYPE RFID_DESIGNATION_REC IS RECORD(
    DESIGNATION_ID DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
    DESCRIPTION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    CATEGORY_ID    RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  TYPE RFID_DESIGNATION_CUR IS REF CURSOR RETURN RFID_DESIGNATION_REC;
  /******************************************************************************/
  PROCEDURE RFID_DESIGNATION_QRY(P_DATA           IN OUT RFID_DESIGNATION_CUR,
                                 P_DESIGNATION_ID IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                 P_DESCRIPTION    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                                 P_CATEGORY_ID    IN RFID.RFID_CATEGORY.CATEGORY_ID%TYPE);
  /******************************************************************************/

END PKG_S48FRM00024;
```

### RFID.PKG_S48FRM00025
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00025 AS

  TYPE HRD_INFO IS RECORD(
    DESIGNATION_ID HRD.INFORMATION.DESIGNATION_ID%TYPE,
    MRNO           HRD.INFORMATION.MRNO%TYPE,
    DISP_MRNO      VARCHAR2(11),
    NAME           REGISTRATION.PATIENT.NAME%TYPE,
    DESIGNATION    DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DEPARTMENT     DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    DEPARTMENT_ID  DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    JOINING_DATE   HRD.INFORMATION.JOINING_DATE%TYPE,
    RFID_CODE      HRD.INFORMATION.RFID_CODE%TYPE);

  TYPE HRD_INFO_TBL IS TABLE OF HRD_INFO INDEX BY PLS_INTEGER;
  TYPE HRD_INFO_TBL_PF IS TABLE OF HRD_INFO; /* FOR PIPLINED FUNCTION */
  TYPE HRD_INFO_REFCUR IS REF CURSOR RETURN HRD_INFO;
  /***************************************************************************/
  TYPE EMP_MACHINES_RC IS RECORD(
    MACHINE_ID           RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
    DESCRIPTION          RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    SHORT_DESC           RFID.RFID_MACHINES.SHORT_DESC%TYPE,
    MACHINE_CODE         RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
    IP_ADDRESS           RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    MRNO                 RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
    ACTIVE               RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
    RFID_CODE            HRD.INFORMATION.RFID_CODE%TYPE,
    MACHINE_INDENTIFIER  RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
    RFID_ATTENDANCE_TYPE RFID.MACHINE_WISE_EMPLOYEE.RFID_ATTENDANCE_TYPE%TYPE,
    MARK_ATTENDANCE      RFID.MACHINE_WISE_EMPLOYEE.MARK_ATTENDANCE%TYPE,
    machine_access_type  VARCHAR2(300));

  TYPE EMP_MACHINES_TL IS TABLE OF EMP_MACHINES_RC INDEX BY PLS_INTEGER;
  TYPE EMP_MACHINES_TL_PF IS TABLE OF EMP_MACHINES_RC; /* FOR PIPLINED FUNCTION */
  TYPE EMP_MACHINE_REFCUR IS REF CURSOR RETURN EMP_MACHINES_RC;
  /******************************************************************************/

  PROCEDURE P_EMP_INFO_QRY(P_DATA           IN OUT HRD_INFO_REFCUR,
                           P_designation_id IN hrd.information.designation_id%TYPE,
                           P_MRNO           IN hrd.information.mrno%TYPE,
                           P_DISP_MRNO      IN VARCHAR2,
                           P_NAME           IN registration.patient.name%TYPE,
                           P_designation    IN DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
                           P_RFID_CODE      IN HRD.INFORMATION.RFID_CODE%TYPE,
                           P_DEPARTMENT     IN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                           P_STOP           OUT VARCHAR2,
                           P_ALERT_TEXT     OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : HRD.INFORMATION
  -- Purpose   : This procedure will be used for locking data of
  --             HRD.INFORMATION.
  /******************************************************************************/

  /*  PROCEDURE P_EMP_INFO_LCK(P_DATA       IN OUT rfid.PKG_machine_wise_employee.HRD_INFO_TBL,
  P_STOP       OUT VARCHAR2,
  P_ALERT_TEXT OUT VARCHAR2);*/

  /******************************************************************************/

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for querying data of
  --             RFID.MACHINE_WISE_EMPLOYEE
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_QY(P_MACHINE_ID          IN RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                              P_DESCRIPTION         IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                              P_SHORT_DESC          IN RFID.RFID_MACHINES.SHORT_DESC%TYPE,
                              P_MACHINE_CODE        IN RFID.RFID_MACHINES.MACHINE_CODE%TYPE,
                              P_IP_ADDRESS          IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                              P_MRNO                IN RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                              P_ACTIVE              IN RFID.MACHINE_WISE_EMPLOYEE.ACTIVE%TYPE,
                              P_RFID_CODE           IN HRD.INFORMATION.RFID_CODE%TYPE,
                              P_MACHINE_ACCESS_TYPE IN VARCHAR2,
                              P_DATA                IN OUT EMP_MACHINE_REFCUR,
                              P_STOP                OUT VARCHAR2,
                              P_ALERT_TEXT          OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for inserting data in
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_INS(P_MACHINE_ID OUT RFID.MACHINE_WISE_EMPLOYEE.MACHINE_ID%TYPE,
                               P_MRNO       OUT RFID.MACHINE_WISE_EMPLOYEE.MRNO%TYPE,
                               P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for locking data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_LCK(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for updating data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/

  PROCEDURE P_EMP_MACHINES_UPD(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 03-JUNE-2013
  -- Scope     : EMP MACHINES
  -- Purpose   : This procedure will be used for deleting data of
  --             RFID.MACHINE_WISE_EMPLOYEE.
  /******************************************************************************/
  PROCEDURE P_EMP_MACHINES_DEL(P_DATA       IN OUT EMP_MACHINES_TL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
  /************************************************************************************/
  PROCEDURE P_EMP_INFO_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                           P_DATA            IN HRD_INFO,
                           P_STOP            OUT VARCHAR2,
                           P_ALERT_TEXT      OUT VARCHAR2);
  /**************************************************************************************/
  PROCEDURE P_EMP_MACHINES_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN EMP_MACHINES_RC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);
  /**********************************************************************************/
  FUNCTION f_get_rfid_code(p_mrno IN VARCHAR2) return varchar;
  /******************************************************************************/
  FUNCTION F_GET_EMPLOYEE_WISE_IDENTIFIER(P_MRNO       IN VARCHAR2,
                                          P_MACHINE_ID IN VARCHAR2)
    RETURN NUMBER;

END PKG_S48FRM00025;
```

### RFID.PKG_S48FRM00060
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00060 AS
  ----------------------------------------------------------
  TYPE RFID_MACHINE_MAPPING_RECORD IS RECORD(
    ORGANIZATION_ID    DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    MACHINE_ID         RFID.RFID_MACHINES.MACHINE_ID%TYPE,
    MACHINE_NAME       RFID.RFID_MACHINES.DESCRIPTION%TYPE,
    IP_ADDRESS         RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
    PORT_NO            RFID.RFID_MACHINES.PORT_NO%TYPE,
    RFID_CARD_NO       HRD.INFORMATION.RFID_CODE%TYPE,
    MACHINE_TYPE       RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
    MACHINE_IDENTIFIER RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
    ORIGINAL_MRNO      HRD.VU_INFORMATION.MRNO%TYPE,
    EMPLOYEE_NAME      HRD.VU_INFORMATION.NAME%TYPE);

  TYPE RFID_MACHINE_MAPPING_CUR IS REF CURSOR RETURN RFID_MACHINE_MAPPING_RECORD;

  PROCEDURE RFID_MACHINE_MAPPING_QY(Q_DATA               IN OUT RFID_MACHINE_MAPPING_CUR,
                                    P_MACHINE_ID         IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                    P_MACHINE_NAME       IN RFID.RFID_MACHINES.DESCRIPTION%TYPE,
                                    P_IP_ADDRESS         IN RFID.RFID_MACHINES.IP_ADDRESS%TYPE,
                                    P_PORT_NO            IN RFID.RFID_MACHINES.PORT_NO%TYPE,
                                    P_RFID_CARD_NO       IN HRD.INFORMATION.RFID_CODE%TYPE,
                                    P_MACHINE_TYPE       IN RFID.RFID_MACHINES.MACHINE_TYPE%TYPE,
                                    P_MACHINE_IDENTIFIER IN RFID.RFID_MACHIN_IDENTIFIER_MAPPING.MACHINE_IDENTIFIER%TYPE,
                                    P_ORIGINAL_MRNO      IN HRD.VU_INFORMATION.MRNO%TYPE,
                                    P_EMPLOYEE_NAME      IN HRD.VU_INFORMATION.NAME%TYPE,
                                    P_STOP               OUT VARCHAR2,
                                    P_ALERT_TEXT         OUT VARCHAR2);

END;
```

### RFID.PKG_S48FRM00100
```sql
CREATE OR REPLACE PACKAGE RFID.PKG_S48FRM00100 AS

  /******************************************************************************/
  -- Author    : Irfan Ali
  -- Created on: 16-NOV-2023
  -- Purpose   : RFID MACHINES GRANT AND REVOKE RIGHTS
  /******************************************************************************************/

  PROCEDURE P_RFID_CATEGORY_WISE_RIGHTS(P_CATEGORY_ID         IN NUMBER,
                                        P_DESIGNATION_ID      IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                        P_EVENT               IN VARCHAR2,
                                        P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                        P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                        P_MACHINE_ACCESS_TYPE IN CHAR,
                                        P_STOP                OUT CHAR,
                                        P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/

  PROCEDURE P_RFID_CATEGORY_REVOKE_RIGHTS(P_CATEGORY_ID         IN NUMBER,
                                          P_DESIGNATION_ID      IN DEFINITIONS.DESIGNATION.DESIGNATION_ID%TYPE,
                                          P_EVENT               IN VARCHAR2,
                                          P_MACHINE_ID          IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                          P_DEPARTMENT_ID       IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                                          P_MACHINE_ACCESS_TYPE IN CHAR,
                                          P_STOP                OUT CHAR,
                                          P_ALERT_TEXT          OUT VARCHAR2);
  /********************************************************************************************/
END PKG_S48FRM00100;
```

## Standalone procedures and functions (headers)

### RFID.F_GET_MRNO (function)
```sql
CREATE OR REPLACE FUNCTION RFID.F_GET_MRNO(P_RFID_CODE HRD.INFORMATION.RFID_CODE%TYPE)
  RETURN VARCHAR2
--AUTHOR:           Muhammad Farhan (TSE) 7098
  --SUPPERVISED BY: Sir Shahzad Farooq (TL), Mahboob Alam (SE)
  --QA BY:          Junaid Mahmood (SQA)
  --DESCRIPTION:    Return MRNO against RFID code
  --AS
```

### RFID.PR_CLEANUP_REDUNDANT_RFID_ACCESS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.PR_CLEANUP_REDUNDANT_RFID_ACCESS
(
    P_EMP_LOCATION_ID IN VARCHAR2 DEFAULT NULL,   -- NULL = all active employee locations
    P_COMMIT          IN VARCHAR2 DEFAULT 'Y'     -- Y/N
)
AS
```

### RFID.PR_RFID_ACCESS_DIFFS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.PR_RFID_ACCESS_DIFFS(P_MRNO                            IN VARCHAR2,
                                                      P_LOCATION_WISE_MINUS_COMPLETE    OUT SYS_REFCURSOR, --1
                                                      P_DEPARTMENT_WISE_MINUS_COMPLETE  OUT SYS_REFCURSOR, --2
                                                      P_DESIGNATION_WISE_MINUS_COMPLETE OUT SYS_REFCURSOR, --3
                                                      P_EMPLOYEE_WISE_MINUS_COMPLETE    OUT SYS_REFCURSOR, --4
                                                      P_SETUP_MINUS_COMPLETE            OUT SYS_REFCURSOR, --5
                                                      P_COMPLETE_MINUS_SETUP            OUT SYS_REFCURSOR --6

                                                      ) AS
```

### RFID.P_COPY_MACHINE_RIGHTS (procedure)
```sql
CREATE OR REPLACE PROCEDURE RFID.P_COPY_MACHINE_RIGHTS(P_MRNO        IN VARCHAR2,
                                                       P_MASTER_MRNO IN VARCHAR2,
                                                       P_MACHINE_ID  IN RFID.RFID_MACHINES.MACHINE_ID%TYPE,
                                                       P_STOP        OUT CHAR,
                                                       P_ALERT_TEXT  OUT VARCHAR) IS
```

