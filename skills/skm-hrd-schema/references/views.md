# HRD views

## HRD.VU_APPLICANTS
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_APPLICANTS AS
SELECT substr(ar.applicant_no, -11) disp_applicant_no,
       ar.applicant_no,
       ar.name,
       ar.address,
       ar.contact_no,
       ai.designation_id,
       ai.department_id,
       d.description designation,
       dept.description department,
       sa.description applicant_status,
       ai.applied_date,
       ar.registration_date,
       ar.registered_by,
       ar.title_id,
       (SELECT description
          FROM marketing.donor_title
         WHERE title_id = ar.title_id) title_desc,
       ai.status_id,
       ai.clearance_date,
       ai.remarks
  FROM hrd.applicant_information  ai,
       hrd.applicant_registration ar,
       definitions.designation    d,
       hrd.applicant_status       sa,
       definitions.department     dept
 WHERE ar.applicant_no = ai.applicant_no
   AND ai.serial_no =
       (SELECT MAX(serial_no)
          FROM hrd.applicant_information
         WHERE applicant_no = ai.applicant_no)
   AND ai.designation_id = d.designation_id
   AND ai.status_id = sa.status_id(+)
   AND ai.department_id = dept.department_id;
```

## HRD.VU_CARD_SWIPE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_CARD_SWIPE AS
SELECT c.serial_no,
       c.mrno,
       c.date_time,
       c.reason_id,
       c.remarks,
       c.flag,
       c.terminal,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(C.MRNO) name,
       HRD.F_GET_DEPARTMENT_ID(C.MRNO) department_id,
       HRD.F_GET_DEPARTMENT_NAME(C.MRNO) department,
       hrd.f_get_designation_id(c.mrno) designation_id,
       hrd.f_get_designation_desc(c.mrno) designation,
       i.card_swipe_exemption,
       i.active,
       i.joining_date,
       i.patient_type_id,
       substr(c.mrno, -11) disp_mrno,
       i.duty_location_id,
       (SELECT nvl(hrd_description, description)
          FROM definitions.location
         WHERE location_id = i.duty_location_id) duty_location_desc
  FROM hrd.card_swipe c, hrd.information i
 WHERE c.mrno = i.mrno;
```

## HRD.VU_INFORMATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_INFORMATION AS
SELECT HRD.F_GET_DESIGNATION_ID(I.MRNO, SYSDATE) DESIGNATION_ID,
       --I.DESIGNATION_ID,
       I.MRNO,
       I.PATIENT_MRNO,
       I.CONTRACT_ID,
       I.EMPLOYEE_TYPE,
       I.GRADE_ID GRADE_ID,
       (SELECT G.DESCRIPTION FROM DEFINITIONS.GRADES   G
       WHERE G.GRADE_ID = I.GRADE_ID) GRADES,
       --       I.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_ID(I.MRNO, SYSDATE) DEPARTMENT_ID,
       HRD.F_GET_JOINING_DATE(I.MRNO) JOINING_DATE,
       --I.JOINING_DATE,
       I.PROBATION_PERIOD_DAYS,
      --- HRD.F_GET_LEAVING_DATE(I.MRNO) LEAVING_DATE,
       I.LEAVING_DATE,
       I.SERVICE_BOND_WITH_PREV_EMPL,
       I.PREPARE_TO_WORK_ANYWHERE_IN_PK,
       I.PREPARE_FOR_EXTENSIVE_TRAVEL,
       I.HAVE_DRIVING_LICENCE,
       I.EVER_DISMISSED_OR_ASK_TO_LEAVE,
       I.DUTY_LOCATION_ID,
       I.MAY_SKMT_APPROACH_EMPLOYER_NOW,
       I.NATIONALITY,
       I.ACTIVE,
       HRD.F_GET_LEAVE_CONTRACT_ID(I.MRNO, SYSDATE) CONTRACT_TYPE_ID,
       --I.CONTRACT_TYPE_ID,
       I.REASON_ID,
       I.REMARKS,
       I.PARAMEDICAL_STAFF,
       I.SHIFT_TYPE_ID,
       I.CONFIRMATION_DATE,
       HRD.F_GET_CONTRACT_START_DATE(I.MRNO, SYSDATE) CONTRACT_START_DATE,
       --    I.CONTRACT_START_DATE,
       HRD.F_GET_CONTRACT_END_DATE(I.MRNO, SYSDATE) CONTRACT_END_DATE,
       --I.CONTRACT_END_DATE,
       HRD.F_GET_CARD_EXP_STATUS(I.MRNO,SYSDATE) CARD_SWIPE_EXEMPTION,
       I.SALARY,
       I.DISCIPLINARY_ACTION,
       I.HIRE_TYPE,
       I.PREDECESSOR_MRNO,
       I.BUDGET_TYPE,
       I.SPOUSE_MEDICAL_ALLOWED,
       I.CHILDREN_MEDICAL_ALLOWED,
       I.USER_ID,
       I.TERMINAL,
       I.TRN_DATE,
       I.INTERNAL_EMAIL,
       INITCAP(HIS.PKG_PATIENT.GET_PATIENT_NAME(I.MRNO)) NAME,
       I.PATIENT_TYPE_ID,
       I.SECTION_ID,
       I.WORKING_AREA_ID,
       I.FAMILY_CODE,
       I.MANAGER_MRNO,
       I.LEAVE_ROLE_ID,
       I.PMDC_PNC_NO,
       I.PMDC_PNC_DATE,
       I.BLACK_LISTED,
       I.EMAIL,
       I.NEW_JOINING_FOR_LEAVES,
       I.TRANSPORT_ALLOWED,
       I.TRANSPORT_ROUTE_ID,
       I.TRANSPORT_ALLOWED_EMERGENCY,
       I.TRANSPORT_COMMENTS,
       I.HR_REFFERNCE,
       I.APPOINTMENT_DATE,
       I.NOTICE_PERIOD_DAYS,
       I.TRANSPORT_ALLOWANCE,
       I.LFA_ALLOWED,
        (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT
         WHERE DEPARTMENT_ID =
               NVL(HRD.F_GET_DEPARTMENT_ID(I.MRNO, SYSDATE), I.DEPARTMENT_ID)) DEPARTMENT,
     /*  HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT,*/
--       I.DEPARTMENT_ID DEPARTMENT,
            HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE) DESIGNATION,
--       I.DESIGNATION_ID DESIGNATION,
       (SELECT G.DESCRIPTION FROM DEFINITIONS.GRADES   G
       WHERE G.GRADE_ID = I.GRADE_ID) GRADE,
       (SELECT C.NATIONALITY
          FROM DEFINITIONS.COUNTRY C
         WHERE C.COUNTRY_ID = I.NATIONALITY) NATIONALITY_DESC,
       PT.DESCRIPTION PATIENT_TYPE,
       INITCAP(P.FATHER_NAME) FATHER_NAME,
       JLR.DESCRIPTION JOB_LEAVING_REASON,
       P.SEX_ID,
       (SELECT DESCRIPTION FROM DEFINITIONS.SEX S WHERE S.SEX_ID = P.SEX_ID) GENDER,
       P.DOB DATE_OF_BIRTH,
       P.MARITAL_STATUS_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.MARITAL_STATUS MS
         WHERE MS.MARITAL_STATUS_ID = P.MARITAL_STATUS_ID) MARITAL_STATUS,
       HIS.PKG_PATIENT.GET_PATIENT_NIC_NEW(P.MRNO) NIC,
       P.NIC_EXPIRY_DATE,
       P.BLOOD_GROUP_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.BLOOD_GROUP BG
         WHERE BG.BLOOD_GROUP_ID = P.BLOOD_GROUP_ID) BLOOD_GROUP,
       DOC.DOCTOR_ID,
       DOC.CONSULTANT,
       P.RELIGION_ID,
       HRD.F_GET_EMPLOYEE_LOCATION(P_MRNO => I.MRNO) EMP_LOCATION_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.RELIGION R
         WHERE R.RELIGION_ID = P.RELIGION_ID) RELIGION,
       PT.EMPLOYEE,
       DS.DESCRIPTION DEPARTMENT_SECTION,
       WA.DESCRIPTION WORKING_AREA,
       PT.SALARY_ALLOWED,
       PT.INCLUDE_IN_HR_REPORTS,
       PT.MEDICAL_ALLOWED,
       I.RFID_CODE,
       I.ORDER_LOCATION_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.ORDER_LOCATION
         WHERE LOCATION_ID = I.DUTY_LOCATION_ID
           AND ORDER_LOCATION_ID = I.ORDER_LOCATION_ID) ORDER_LOCATION_DESC,
       (SELECT NVL(HRD_DESCRIPTION, DESCRIPTION)
          FROM DEFINITIONS.LOCATION
         WHERE LOCATION_ID = I.DUTY_LOCATION_ID) DUTY_LOCATION_DESC
  FROM HRD.INFORMATION                I,
       DEFINITIONS.PATIENT_TYPE       PT,
       REGISTRATION.PATIENT           P,
       DEFINITIONS.DOCTOR             DOC,
       HRD.JOB_LEAVING_REASON         JLR,
       DEFINITIONS.DEPARTMENT_SECTION DS,
       DEFINITIONS.WORKING_AREA       WA
 WHERE I.MRNO = P.MRNO
   AND I.PATIENT_TYPE_ID = PT.PATIENT_TYPE_ID(+)
   AND I.MRNO = DOC.DOCTOR_MRNO(+)
   AND I.REASON_ID = JLR.REASON_ID(+)
   AND I.DEPARTMENT_ID = DS.DEPARTMENT_ID(+)
   AND I.SECTION_ID = DS.SECTION_ID(+)
   AND I.DEPARTMENT_ID = WA.DEPARTMENT_ID(+)
   AND I.SECTION_ID = WA.SECTION_ID(+)
   AND I.WORKING_AREA_ID = WA.WORKING_AREA_ID(+)
   AND SUBSTR(I.MRNO, 4, 3) NOT LIKE '%DUM%'
;
```

## HRD.VU_CONSULTANTS
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_CONSULTANTS AS
SELECT I.DOCTOR_ID, I.MRNO, I.NAME, I.DEPARTMENT, I.DESIGNATION
                  FROM HRD.VU_INFORMATION                    I,
                       DEFINITIONS.CATEGORY_WISE_DESIGNATION D

                 WHERE I.DESIGNATION_ID = D.DESIGNATION_ID
                   AND D.DESIGNATION_CATEGORY_ID = '060'
                   AND I.ACTIVE = 'Y'
                   AND I.JOINING_DATE IS NOT NULL
                   AND HIS.PKG_DOCTOR.IS_CONSULTANT(I.MRNO) = 'Y';
```

## HRD.V_INFORMATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_INFORMATION AS
SELECT NVL(HRD.F_GET_DESIGNATION_ID(I.MRNO, SYSDATE), I.DESIGNATION_ID) DESIGNATION_ID,
       --       I.DESIGNATION_ID,
       I.MRNO,
       I.CONTRACT_ID,
       I.EMPLOYEE_TYPE,
       I.GRADE_ID,
       I.EMP_NATURE_TYPE,
       NVL(HRD.F_GET_DEPARTMENT_ID(I.MRNO, SYSDATE), I.DEPARTMENT_ID) DEPARTMENT_ID,
       --       I.DEPARTMENT_ID,
       HRD.F_GET_JOINING_DATE(I.MRNO) JOINING_DATE,
       --       I.JOINING_DATE,
       HRD.F_GET_PROBATION_PERIOD_DAYS(I.MRNO) PROBATION_PERIOD_DAYS,
       --I.PROBATION_PERIOD_DAYS,
       ---- HRD.F_GET_LEAVING_DATE(I.MRNO) LEAVING_DATE,
       I.LEAVING_DATE,
       I.SERVICE_BOND_WITH_PREV_EMPL,
       I.PREPARE_TO_WORK_ANYWHERE_IN_PK,
       I.PREPARE_FOR_EXTENSIVE_TRAVEL,
       I.HAVE_DRIVING_LICENCE,
       I.EVER_DISMISSED_OR_ASK_TO_LEAVE,
       I.DUTY_LOCATION_ID,
       I.MAY_SKMT_APPROACH_EMPLOYER_NOW,
       I.NATIONALITY,
       I.ACTIVE,
       HRD.F_GET_LEAVE_CONTRACT_ID(I.MRNO, SYSDATE) CONTRACT_TYPE_ID,
       --       I.CONTRACT_TYPE_ID,
       I.REASON_ID,
       I.REMARKS,
       I.PARAMEDICAL_STAFF,
       I.SHIFT_TYPE_ID,
       I.CONFIRMATION_DATE,
       --I.CONTRACT_START_DATE,
       HRD.F_GET_CONTRACT_START_DATE(I.MRNO, SYSDATE) CONTRACT_START_DATE,
       --I.CONTRACT_END_DATE,
       HRD.F_GET_CONTRACT_END_DATE(I.MRNO, SYSDATE) CONTRACT_END_DATE,
       HRD.F_GET_CARD_EXP_STATUS(I.MRNO, SYSDATE) CARD_SWIPE_EXEMPTION,
       I.SALARY,
       I.DISCIPLINARY_ACTION,
       I.HIRE_TYPE,
       I.PREDECESSOR_MRNO,
       I.BUDGET_TYPE,
       I.SPOUSE_MEDICAL_ALLOWED,
       I.CHILDREN_MEDICAL_ALLOWED,
       I.USER_ID,
       I.TERMINAL,
       I.TRN_DATE,
       I.INTERNAL_EMAIL,
       --I.NAME,
       I.PATIENT_TYPE_ID,
       I.SECTION_ID,
       I.WORKING_AREA_ID,
       I.FAMILY_CODE,
       I.MANAGER_MRNO,
       I.LEAVE_ROLE_ID,
       I.PMDC_PNC_NO,
       I.PMDC_PNC_DATE,
       I.BLACK_LISTED,
       I.EMAIL,
       I.NEW_JOINING_FOR_LEAVES,
       I.TRANSPORT_ALLOWED,
       I.TRANSPORT_ROUTE_ID,
       I.TRANSPORT_ALLOWED_EMERGENCY,
       I.TRANSPORT_COMMENTS,
       I.HR_REFFERNCE,
       I.APPOINTMENT_DATE,
       I.NOTICE_PERIOD_DAYS,
       I.TRANSPORT_ALLOWANCE,
       I.LFA_ALLOWED,
       I.RFID_CODE,
       I.SSC_DEDUCTION,
       I.SSC_START_DATE,
       I.SSC_NO,
       HIS.PKG_PATIENT.F_IS_MEDICAL_ALLOWED(I.MRNO) MEDICAL_ALLOWED,
       SUBSTR(I.MRNO, -11) DISP_MRNO,
       -- HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT
         WHERE DEPARTMENT_ID =
               NVL(HRD.F_GET_DEPARTMENT_ID(I.MRNO, SYSDATE), I.DEPARTMENT_ID)) DEPARTMENT,
       /*  NVL(HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE),
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT
         WHERE DEPARTMENT_ID = I.DEPARTMENT_ID)) null DEPARTMENT,*/
       --      I.DEPARTMENT_ID DEPARTMENT,
       NVL(HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE),
           (SELECT DESCRIPTION
              FROM DEFINITIONS.DESIGNATION
             WHERE DESIGNATION_ID = I.DESIGNATION_ID)) DESIGNATION,
       --             I.DESIGNATION_ID DESIGNATION,
       G.DESCRIPTION GRADE,
       INITCAP(HIS.PKG_PATIENT.GET_PATIENT_NAME(I.MRNO)) NAME,
       INITCAP(HIS.PKG_PATIENT.GET_PATIENT_FATHER_NAME(I.MRNO)) FATHER_NAME,
       I.ORDER_LOCATION_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.ORDER_LOCATION
         WHERE LOCATION_ID = I.DUTY_LOCATION_ID
           AND ORDER_LOCATION_ID = I.ORDER_LOCATION_ID) ORDER_LOCATION_DESC,
       I.DOCUMENT_ID,
       I.ATTACHED_BY,
       I.DOCUMENT_DESCRIPTION,
       I.MEDICAL_DATE,
       I.IS_OSV_REQUIRED,
       I.OSV_TYPE,
       i.SENIOR_INSTRUCTOR,
       i.ANCILLARY_WORKER,
       i.PARAMEDICAL
  FROM HRD.INFORMATION I, DEFINITIONS.GRADES G
 WHERE I.GRADE_ID = G.GRADE_ID(+)
;
```

## HRD.VU_PA_HIERARCHY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_HIERARCHY AS
SELECT H.HIERARCHY_ID,
                  H.DESCRIPTION,
                  H.APPRAISEE_MRNO,
                  H.PATP_ID,
                  H.PA_TEMPLATE_ID,
                  H.REPORTING_TO,
                  PM.PA_PERFORM_STATUS_ID PA_STATUS_ID,
                  (SELECT DESCRIPTION
                              FROM ORDERENTRY.ORDER_STATUS
                        WHERE ORDER_STATUS_ID = PM.PA_PERFORM_STATUS_ID) PA_STATUS_DESC,
                  SUBSTR(H.APPRAISEE_MRNO, -11) EMP_CODE,
                  I.NAME,
                  I.DESIGNATION_ID,
                  I.DESIGNATION,
                  H.DEPARTMENT_ID,
                  HRD.PKG_COMMON.GET_DEPARTMENT_NAME(P_DEPARTMENT_ID => H.DEPARTMENT_ID) DEPARTMENT,
                  I.JOINING_DATE,
                  (SELECT T.DESCRIPTION FROM HRD.PA_DEF_TEMPLATE T WHERE T.PA_TEMPLATE_ID = H.PA_TEMPLATE_ID) TEMPLATE_NAME,
                  TP.PA_START_DATE APPRAISAL_START_PERIOD,
                  TP.PA_END_DATE APPRAISAL_END_PERIOD,
                  (SELECT DT.DESCRIPTION FROM HRD.PA_DEF_TYPE DT WHERE DT.PA_TYPE_ID = TP.PA_TYPE_ID) PA_TYPE_DESCRIPTION,
                  TP.PA_TYPE_ID,
                  I.DUTY_LOCATION_ID,
                  I.ORDER_LOCATION_ID,
                  I.ORDER_LOCATION_DESC,
                  (SELECT DESCRIPTION FROM DEFINITIONS.PATIENT_TYPE WHERE PATIENT_TYPE_ID = I.PATIENT_TYPE_ID) EMPLOYEE_TYPE,
                  I.PATIENT_TYPE_ID,
                  H.REPORT_NAME,
                  I.ACTIVE,
                  I.LEAVING_DATE,
                  PM.PA_PERFORM_ID,
                  TP.PA_STATUS_ID PA_PERIOD_STATUS_ID,
                  PM.DISTRIBUTED_DATE ,
                  HRD.PKG_COMMON.GET_CONTINUOUS_JOINING_DATE(I.MRNO) CONTINUOUS_JOINING_DATE,
                  H.HR_DISTRIBUTE,
                  HRD.F_GET_DEPARTMENT_LOCATION_ID(P_DEPARTMENT_ID => H.DEPARTMENT_ID) LOCATION_ID,
                  H.PA_YEAR,
                  H.EXCLUDE_IN_APPRAISAL
      FROM HRD.PA_HIERARCHY      H,
                  HRD.V_INFORMATION     I,
                  HRD.PA_TYPE_PERIOD    TP,
                  HRD.PA_PERFORM_MASTER PM,
                  HRD.PA_EMPLOYEE_TYPE  ET
WHERE H.APPRAISEE_MRNO = I.MRNO
      AND H.PATP_ID = TP.PATP_ID
      AND H.PATP_ID = ET.PATP_ID
      AND I.PATIENT_TYPE_ID = ET.PATIENT_TYPE_ID
      AND H.HIERARCHY_ID = PM.HIERARCHY_ID
      AND NVL(I.LEAVING_DATE, '31-Dec-9999') > CASE
                        WHEN HRD.PKG_PERFORMANCE_APPRAISAL.GET_REVIEW_PERIOD_ID(H.PATP_ID) = 'A' THEN
                              TP.PA_START_DATE
                        ELSE
                              TO_DATE('30-Dec-9999', 'DD-MON-RRRR')
                  END;
```

## HRD.VU_CONSULTANT_COMPARISON
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_CONSULTANT_COMPARISON AS
SELECT h.APPRAISEE_MRNO EMPLOYEE_CODE,
         H.NAME,
         H.PATP_ID,
         H.DEPARTMENT,
         H.DESIGNATION,
         PM.PA_PERFORM_ID,
         HRD.F_GET_EMPLOYEE_LOCATION(H.APPRAISEE_MRNO) EMP_LOCATION,
         H.PA_TEMPLATE_ID,
         H.DEPARTMENT_ID
    FROM HRD.VU_PA_HIERARCHY H, HRD.PA_PERFORM_MASTER PM
   WHERE  H.HIERARCHY_ID = PM.HIERARCHY_ID
     AND H.DESIGNATION_ID IN
         (SELECT CWD.DESIGNATION_ID
            FROM DEFINITIONS.CATEGORY_WISE_DESIGNATION CWD
           WHERE CWD.DESIGNATION_CATEGORY_ID = '060');
```

## HRD.VU_EMPLOYEE_CLEARANCE
```sql
create or replace force view hrd.vu_employee_clearance as
select EC.mrno,
       EC.joining_serial_no,
       EC.clearance_type_id,
       C.DESCRIPTION,
       EC.status_id,
       EC.approved,
       EC.remarks,
       c.alert_message
  from hrd.employee_clearance EC, HRD.CLEARANCE_SETUP C
 WHERE EC.CLEARANCE_TYPE_ID = C.CLEARANCE_TYPE_ID;
```

## HRD.VU_EMPLOYEE_JOINING_HISTORY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_EMPLOYEE_JOINING_HISTORY AS
SELECT j.serial_no,
       j.mrno,
       his.pkg_patient.get_patient_name(j.mrno) name,
       j.offer_date,
       j.medical_date,
       j.joining_date,
       j.leaving_date,
       j.medical_rejection_id,
       (SELECT description
          FROM hrd.medical_rejection_reaon
         WHERE reason_id = j.medical_rejection_id) medical_rejection_desc,
       j.leaving_reason_id,
       (SELECT description
          FROM hrd.job_leaving_reason
         WHERE reason_id = j.leaving_reason_id) leaving_reason_desc,
       j.remarks,
       j.status
  FROM hrd.employee_joining_history j;
```

## HRD.VU_EMP_RESIGNATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_EMP_RESIGNATION AS
SELECT er.mrno,
             substr(er.mrno, -11) emp_code,
             er.resignation_date,
             er.notification_days,
             er.leaving_date,
            er.approval_date,
             er.remarks,
             i.NAME,
             i.department,
             i.designation,
             (SELECT p.position_id
             FROM hrd.position  p
             WHERE er.mrno = nvl(p.actual_employee_id,p.further_employee_id))position_id,
             i.joining_date
  FROM hrd.employee_resignation er,
             hrd.vu_information       i
WHERE NVL(i.active,'N') = 'Y'
AND   er.resignation_date =
             (SELECT MAX(resignation_date)
                   FROM hrd.employee_resignation
                  WHERE mrno = er.mrno
                    AND approved = 'A')
      AND er.approved = 'A'
  and er.leaving_date >= i.joining_date
      AND er.mrno = i.mrno;
```

## HRD.VU_EMP_SUPERVISOR
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_EMP_SUPERVISOR AS
SELECT io.mrno,
       substr(io.mrno, -11) emp_code,
       i.NAME,
       io.designation_id,
       io.department_id,
       io.active,
       io.patient_type_id,
       io.joining_date,
       i.department,
       i.designation,
       io.manager_mrno,
       io.leave_role_id,
       j.mrno supervisor_mrno,
       substr(j.mrno, -11) supervisor_code,
       j.NAME supervisor_name,
       j.designation supervisor_designation,
       lr.description leave_role_desc_emp,
       lrj.description leave_role_desc_sup
  FROM hrd.v_information i,
       hrd.v_information   io,
       hrd.v_information j,
       hrd.leave_role    lr,
       hrd.leave_role    lrj
 WHERE i.manager_mrno = j.mrno(+)
   AND i.mrno = io.mrno
   AND i.leave_role_id = lr.leave_role_id(+)
   AND j.leave_role_id = lrj.leave_role_id(+);
```

## HRD.VU_EMP_WISE_DOCUEMENT_REQUIRED
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_EMP_WISE_DOCUEMENT_REQUIRED AS
SELECT T.DOC_CATEGORY_ID,
       T.DOCUMENT_TYPE_ID,
       T.MRNO,
       T.DOCUMENTS_STATUS,
       T.EMP_WISE,
       T.DEPT_WISE,
       T.DESIG_WISE,
       T.DESIG_CAT_WISE
        FROM HRD.EMP_WISE_DOCUEMENT_REQUIRED T
WHERE HRD.PKG_HR_DOCUMENT_RECORD.F_IS_DOC_EXEMPT(P_MRNO => T.MRNO,
                                                        P_DOC_CATEGORY_ID => T.DOC_CATEGORY_ID,
                                                        P_DOCUMENT_TYPE_ID => T.DOCUMENT_TYPE_ID) = 'N';
```

## HRD.VU_EOBI_CALCULATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_EOBI_CALCULATION AS
SELECT I.MRNO,
       I.NAME,
       I.DEPARTMENT,
       HIS.PKG_PATIENT.F_GET_PATIENT_NIC(I.MRNO)NIC,
      /* SUBSTR(I.NIC, 1, 5) || '-' ||
                  SUBSTR(I.NIC, 6, 7) || '-' ||
                  SUBSTR(I.NIC, -1) NIC,*/
       C.JOINING_DATE,
       i.LEAVING_DATE,
       I.GENDER,
       HIS.PKG_PATIENT.GET_AGE(C.MRNO) AGE,
       C.WORKING_DAYS,
       C.MONTH_START,
       C.MONTH_END,
       C.POSITION_LOCATION_ID,
       C.DUTY_LOCATION_ID,
       I.DUTY_LOCATION_DESC,
       C.IS_POSTED,
       C.IS_NEW_JOINER,
       C.IS_LEAVER,
       c.entry_date,
       CASE
         WHEN C.IS_NEW_JOINER = 'Y' THEN
          'New Joiner'
         WHEN C.IS_LEAVER = 'Y' THEN
          'Leaver'
         ELSE
          'Regular'
       END EMP_STATUS,
       I.FATHER_NAME,
       HIS.PKG_PATIENT.GET_PERMANENT_ADDRESS(I.MRNO)PERMANENT_ADDRESS
  FROM HRD.EOBI_CALCULATION C, HRD.VU_INFORMATION I
 WHERE I.MRNO = C.MRNO
 ORDER BY I.DEPARTMENT, I.MRNO;
```

## HRD.VU_HR_APPROVAL_QUEUE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_HR_APPROVAL_QUEUE AS
SELECT Q.REQUEST_ID,
       Q.REQUEST_DATE,
       Q.DEPARTMENT_ID,
       DP.DESCRIPTION DEPARTMENT,
       Q.DESIGNATION_ID,
       (SELECT D.DESCRIPTION
          FROM DEFINITIONS.DESIGNATION D
         WHERE D.DESIGNATION_ID = Q.DESIGNATION_ID) DESIGNATION,
       Q.HIRING_DESIGNATION_ID,
       (SELECT D.DESCRIPTION
          FROM DEFINITIONS.DESIGNATION D
         WHERE D.DESIGNATION_ID = Q.HIRING_DESIGNATION_ID) HIRING_DESIGNATION,
       DECODE(Q.POSITION_CATEGORY, 'N', 'New Position', 'R', 'Replacement') POSITION_CATEGORY,
       DECODE(Q.POSITION_TYPE, 'B', 'Budgeted', 'N', 'Non-Budgeted') POSITION_TYPE,
       Q.POSITION_CATEGORY POSITION_CATEGORY_ID,
       Q.POSITION_TYPE POSITION_TYPE_ID,
       Q.FINANCIAL_YEAR,
       Q.STATUS_ID,
       OS.DESCRIPTION STATUS,
       Q.APPROVED_NO_OF_POSITION
  FROM HRD.HIRING_REQUEST_MASTER Q,
       ORDERENTRY.ORDER_STATUS   OS,
       DEFINITIONS.DEPARTMENT    DP
 WHERE Q.STATUS_ID = OS.ORDER_STATUS_ID
   AND Q.DEPARTMENT_ID = DP.DEPARTMENT_ID
   AND Q.STATUS_ID = '010';
```

## HRD.VU_HR_DOC_REC_ATTACH_MRNO
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_HR_DOC_REC_ATTACH_MRNO AS
SELECT DISTINCT T.MRNO,
                HIS.PKG_PATIENT.GET_PATIENT_NAME(T.MRNO) NAME,
                HRD.F_GET_DEPARTMENT_NAME(T.MRNO) DEPARTMENT_NAME,
                HRD.F_GET_DESIGNATION_DESC(T.MRNO) DESIGNATION_DESC,
                HRD.F_GET_JOINING_DATE(T.MRNO) JOINING_DATE,
                HRD.F_GET_EMPLOYEE_LOCATION(T.MRNO) EMP_LOCATION

  FROM HRD.HR_DOC_REC_TRACK T
  WHERE T.DOCUMENTS_STATUS = 'A'
  AND T.STATUS ='F'
  AND HRD.F_IS_ACTIVE_ONLY_EMP_CODE(T.MRNO) = 'Y'
  AND  HRD.PKG_HR_DOCUMENT_RECORD.F_IS_DOC_EXEMPT(P_MRNO             => T.MRNO,
                                                                  P_DOC_CATEGORY_ID  => T.DOC_CATEGORY_ID,
                                                                  P_DOCUMENT_TYPE_ID => T.DOCUMENT_TYPE_ID) = 'N'
  AND HRD.F_GET_EMPLOYEE_LOCATION(T.MRNO) IN ('001' , '006')
 ORDER BY 3, 1;
```

## HRD.VU_HR_DOC_REC_MISS_MRNO
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_HR_DOC_REC_MISS_MRNO AS
SELECT DISTINCT T.MRNO,
                HIS.PKG_PATIENT.GET_PATIENT_NAME(T.MRNO) NAME,
                HRD.F_GET_DEPARTMENT_NAME(T.MRNO) DEPARTMENT_NAME,
                HRD.F_GET_DESIGNATION_DESC(T.MRNO) DESIGNATION_DESC,
                HRD.F_GET_JOINING_DATE(T.MRNO) JOINING_DATE
  FROM HRD.HR_DOC_REC_TRACK T
 WHERE T.STATUS NOT IN ('F','V')
 AND HRD.PKG_HR_DOCUMENT_RECORD.F_IS_DOC_EXEMPT(P_MRNO => T.MRNO,
                                                        P_DOC_CATEGORY_ID => T.DOC_CATEGORY_ID,
                                                        P_DOCUMENT_TYPE_ID => T.DOCUMENT_TYPE_ID) = 'N';
```

## HRD.VU_HR_DOC_REC_VERIFY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_HR_DOC_REC_VERIFY AS
SELECT T.MRNO,
       T.DOCUMENT_TYPE_ID,
       T.DOCUMENT_ID,
       T.DOC_CATEGORY_ID,
       T.DOC_DATE,
       T.STATUS,
       T.SECTION_ID,
       T.OBJECT_CODE,
       T.HR_EMP_DEPARTMENT_ID DEPARTMENT_ID,
       T.GROUP_ID,
       T.DOCUMENTS_STATUS,
       T.REMARKS
FROM HRD.HR_DOC_REC_TRACK T
WHERE HRD.PKG_HR_DOCUMENT_RECORD.F_IS_DOC_EXEMPT(P_MRNO => T.MRNO,
                                                        P_DOC_CATEGORY_ID => T.DOC_CATEGORY_ID,
                                                        P_DOCUMENT_TYPE_ID => T.DOCUMENT_TYPE_ID) = 'N';
```

## HRD.VU_INFORMATION_PAT
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_INFORMATION_PAT AS
SELECT HRD.F_GET_DESIGNATION_ID(I.MRNO, SYSDATE) DESIGNATION_ID,
       --I.DESIGNATION_ID,
       I.MRNO,
       I.PATIENT_MRNO,
       I.CONTRACT_ID,
       I.EMPLOYEE_TYPE,
       I.GRADE_ID GRADE_ID,
       (SELECT G.DESCRIPTION FROM DEFINITIONS.GRADES   G
       WHERE G.GRADE_ID = I.GRADE_ID) GRADES,
       --       I.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_ID(I.MRNO, SYSDATE) DEPARTMENT_ID,
       HRD.F_GET_JOINING_DATE(I.MRNO) JOINING_DATE,
       --I.JOINING_DATE,
       I.PROBATION_PERIOD_DAYS,
       HRD.F_GET_LEAVING_DATE(I.MRNO) LEAVING_DATE,
       --  I.LEAVING_DATE,
       I.SERVICE_BOND_WITH_PREV_EMPL,
       I.PREPARE_TO_WORK_ANYWHERE_IN_PK,
       I.PREPARE_FOR_EXTENSIVE_TRAVEL,
       I.HAVE_DRIVING_LICENCE,
       I.EVER_DISMISSED_OR_ASK_TO_LEAVE,
       I.DUTY_LOCATION_ID,
       I.MAY_SKMT_APPROACH_EMPLOYER_NOW,
       I.NATIONALITY,
       I.ACTIVE,
       HRD.F_GET_LEAVE_CONTRACT_ID(I.MRNO, SYSDATE) CONTRACT_TYPE_ID,
       --I.CONTRACT_TYPE_ID,
       I.REASON_ID,
       I.REMARKS,
       I.PARAMEDICAL_STAFF,
       I.SHIFT_TYPE_ID,
       I.CONFIRMATION_DATE,
       HRD.F_GET_CONTRACT_START_DATE(I.MRNO, SYSDATE) CONTRACT_START_DATE,
       --    I.CONTRACT_START_DATE,
       HRD.F_GET_CONTRACT_END_DATE(I.MRNO, SYSDATE) CONTRACT_END_DATE,
       --I.CONTRACT_END_DATE,
       HRD.F_GET_CARD_EXP_STATUS(I.MRNO,SYSDATE) CARD_SWIPE_EXEMPTION,
       I.SALARY,
       I.DISCIPLINARY_ACTION,
       I.HIRE_TYPE,
       I.PREDECESSOR_MRNO,
       I.BUDGET_TYPE,
       I.SPOUSE_MEDICAL_ALLOWED,
       I.CHILDREN_MEDICAL_ALLOWED,
       I.USER_ID,
       I.TERMINAL,
       I.TRN_DATE,
       I.INTERNAL_EMAIL,
       INITCAP(P.NAME) NAME,
       I.PATIENT_TYPE_ID,
       I.SECTION_ID,
       I.WORKING_AREA_ID,
       I.FAMILY_CODE,
       I.MANAGER_MRNO,
       I.LEAVE_ROLE_ID,
       I.PMDC_PNC_NO,
       I.PMDC_PNC_DATE,
       I.BLACK_LISTED,
       I.EMAIL,
       I.NEW_JOINING_FOR_LEAVES,
       I.TRANSPORT_ALLOWED,
       I.TRANSPORT_ROUTE_ID,
       I.TRANSPORT_ALLOWED_EMERGENCY,
       I.TRANSPORT_COMMENTS,
       I.HR_REFFERNCE,
       I.APPOINTMENT_DATE,
       I.NOTICE_PERIOD_DAYS,
       I.TRANSPORT_ALLOWANCE,
       I.LFA_ALLOWED,
       HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT,
--       I.DEPARTMENT_ID DEPARTMENT,
            HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE) DESIGNATION,
--       I.DESIGNATION_ID DESIGNATION,
       (SELECT G.DESCRIPTION FROM DEFINITIONS.GRADES   G
       WHERE G.GRADE_ID = I.GRADE_ID) GRADE,
       (SELECT C.NATIONALITY
          FROM DEFINITIONS.COUNTRY C
         WHERE C.COUNTRY_ID = I.NATIONALITY) NATIONALITY_DESC,
       PT.DESCRIPTION PATIENT_TYPE,
       INITCAP(P.FATHER_NAME) FATHER_NAME,
       JLR.DESCRIPTION JOB_LEAVING_REASON,
       P.SEX_ID,
       (SELECT DESCRIPTION FROM DEFINITIONS.SEX S WHERE S.SEX_ID = P.SEX_ID) GENDER,
       P.DOB DATE_OF_BIRTH,
       P.MARITAL_STATUS_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.MARITAL_STATUS MS
         WHERE MS.MARITAL_STATUS_ID = P.MARITAL_STATUS_ID) MARITAL_STATUS,
       P.NIC_NEW NIC,
       P.NIC_EXPIRY_DATE,
       P.BLOOD_GROUP_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.BLOOD_GROUP BG
         WHERE BG.BLOOD_GROUP_ID = P.BLOOD_GROUP_ID) BLOOD_GROUP,
       DOC.DOCTOR_ID,
       DOC.CONSULTANT,
       P.RELIGION_ID,
       HRD.F_GET_EMPLOYEE_LOCATION(P_MRNO => I.MRNO) EMP_LOCATION_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.RELIGION R
         WHERE R.RELIGION_ID = P.RELIGION_ID) RELIGION,
       PT.EMPLOYEE,
       DS.DESCRIPTION DEPARTMENT_SECTION,
       WA.DESCRIPTION WORKING_AREA,
       PT.SALARY_ALLOWED,
       PT.INCLUDE_IN_HR_REPORTS,
       PT.MEDICAL_ALLOWED,
       I.RFID_CODE,
       I.ORDER_LOCATION_ID,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.ORDER_LOCATION
         WHERE LOCATION_ID = I.DUTY_LOCATION_ID
           AND ORDER_LOCATION_ID = I.ORDER_LOCATION_ID) ORDER_LOCATION_DESC,
       (SELECT NVL(HRD_DESCRIPTION, DESCRIPTION)
          FROM DEFINITIONS.LOCATION
         WHERE LOCATION_ID = I.DUTY_LOCATION_ID) DUTY_LOCATION_DESC
  FROM HRD.INFORMATION                I,
       DEFINITIONS.PATIENT_TYPE       PT,
       REGISTRATION.PATIENT           P,
       DEFINITIONS.DOCTOR             DOC,
       HRD.JOB_LEAVING_REASON         JLR,
       DEFINITIONS.DEPARTMENT_SECTION DS,
       DEFINITIONS.WORKING_AREA       WA
 WHERE NVL(I.PATIENT_MRNO,I.MRNO) = P.MRNO
   AND I.PATIENT_TYPE_ID = PT.PATIENT_TYPE_ID(+)
   AND I.MRNO = DOC.DOCTOR_MRNO(+)
   AND I.REASON_ID = JLR.REASON_ID(+)
   AND I.DEPARTMENT_ID = DS.DEPARTMENT_ID(+)
   AND I.SECTION_ID = DS.SECTION_ID(+)
   AND I.DEPARTMENT_ID = WA.DEPARTMENT_ID(+)
   AND I.SECTION_ID = WA.SECTION_ID(+)
   AND I.WORKING_AREA_ID = WA.WORKING_AREA_ID(+)
   AND SUBSTR(I.MRNO, 4, 3) NOT LIKE '%DUM%'
;
```

## HRD.VU_LEAVE_REENTERED
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_LEAVE_REENTERED AS
SELECT el.entered_date,
         i.NAME,
         el.leave_reason,
         lt.description leave_type,
         el.from_date,
         el.to_date,
         el.mrno,
         el.serial_no,
         el.total_leave_days,
         el.approved
  FROM hrd.employee_leaves el,
         hrd.V_information     i,
         hrd.leave_type      lt
 WHERE el.entered_by = i.mrno
    AND el.leave_type_id = lt.leave_type_id
    AND el.approved = 'N'
    AND (el.mrno, el.from_date, el.to_date) IN
         (SELECT mrno,
                    from_date,
                    to_date
             FROM hrd.employee_leaves
            WHERE total_leave_days = 0
              AND approved = 'N'
            GROUP BY mrno,
                        from_date,
                        to_date
          HAVING COUNT(*) >= 1)
 ORDER BY el.entered_date;
```

## HRD.VU_MEDICAL_DATE_MISSING_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_MEDICAL_DATE_MISSING_Q AS
SELECT I.MRNO,

       HIS.PKG_PATIENT.GET_PATIENT_NAME (I.MRNO) NAME,

       HRD.F_GET_DESIGNATION_DESC(I.MRNO) DESIGNATION,

       HRD.F_GET_DEPARTMENT_NAME(I.MRNO) DEPARTMENT,

       I.MEDICAL_DATE,

       P.REGISTRATION_DATE,

       P.PATIENT_TYPE_ID,

       D.LOCATION_ID,

       I.ACTIVE

  FROM HRD.INFORMATION I, REGISTRATION.PATIENT P,DEFINITIONS.DEPARTMENT D

WHERE I.MRNO = P.MRNO

AND P.REGISTRATION_DATE > '01-JAN-2021'

   AND I.MEDICAL_DATE IS NULL

   AND D.DEPARTMENT_ID = I.DEPARTMENT_ID

   AND I.MRNO NOT LIKE '%D%'

   AND P.PATIENT_TYPE_ID IN (SELECT T.PATIENT_TYPE_ID FROM DEFINITIONS.PATIENT_TYPE T

   WHERE T.PATIENT_TYPE_ID = P.PATIENT_TYPE_ID

   AND T.SALARY_ALLOWED = 'Y');
```

## HRD.VU_MISSING_EMAILS
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_MISSING_EMAILS AS
SELECT I.MRNO, I.NAME, I.DESIGNATION, I.DEPARTMENT, II.EMAIL
  FROM HRD.VU_INFORMATION I,HRD.INFORMATION II, DEFINITIONS.DESIGNATION D
 WHERE I.DESIGNATION_ID = D.DESIGNATION_ID
 AND NVL(D.EMAIL_REQUIRED ,'N')= 'Y'
 AND I.MRNO = II.MRNO
   AND  I.ACTIVE = 'Y'
   AND I.JOINING_DATE IS NOT NULL
   AND I.LEAVING_DATE IS NULL
   AND I.MRNO NOT LIKE '%EX%'
      AND I.MRNO NOT LIKE '%D%'
   AND II.EMAIL IS NULL;
```

## HRD.VU_NEW_JOINERS_QUEUE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_NEW_JOINERS_QUEUE AS
SELECT SUBSTR(EC.MRNO, -11) DISP_MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(I.MRNO) DISP_NAME,
       DECODE(HRD.PKG_COMMON.IS_REJOINER(I.MRNO),
              'N',
              HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE),
              (SELECT D.DESCRIPTION
                 FROM DEFINITIONS.DESIGNATION D
                WHERE D.DESIGNATION_ID = I.DESIGNATION_ID)) DESIGNATION,
       HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT,
       HIS.PKG_PATIENT.GET_CONTACT_NUMBER(I.MRNO) PHONE_NO,
       EC.MRNO MRNO,
       EC.JOINING_DATE,
       EC.GRADE_ID,
       (SELECT G.DESCRIPTION
          FROM DEFINITIONS.GRADES G
         WHERE G.GRADE_ID = EC.GRADE_ID) GRADE,
       EC.INITIAL_GROSS,
       EC.CONTRACT_START_DATE,
       EC.CONTRACT_END_DATE,
       EC.PROBATION_PERIOD,
       EC.NOTICE_PERIOD,
       EC.ACCEPTANCE_DAYS,
       EC.SALARY_RAISE_AFTER_PROBATION,
       EC.MEDICALLY_FIT,
       EC.ACTIVE,
       EC.IN_QUEUE_HR_SECTION_ID,
       EC.DESIGNATION_ID,
       EC.PATIENT_TYPE_ID,
       EC.ORIENTATION_DATE,
       EC.IS_JOINED,
       EC.CONTRACT_YEAR,
       (SELECT LOCATION_ID
          FROM DEFINITIONS.DEPARTMENT D
         WHERE D.DEPARTMENT_ID = I.DEPARTMENT_ID) LOCATION_ID,
       --  HRD.F_GET_EMPLOYEE_LOCATION(P_MRNO => P.MRNO) LOCATION_ID,
       EC.MEDICALLY_UNFIT_REMARKS,
       EC.INACTIVE_REMARKS,
       (SELECT MAX(S.OSV_STATUS)
          FROM HRD.EMPLOYEE_OSV_STATUS S
         WHERE NVL(S.ACTIVE, 'N') = 'Y'
           AND S.MRNO = I.MRNO) OSV_STATUS,
       (SELECT MAX(S.SENT_DATE)
          FROM HRD.EMPLOYEE_OSV_STATUS S
         WHERE NVL(S.ACTIVE, 'N') = 'Y'
           AND S.MRNO = I.MRNO) OSV_VERIFICATION_SENT_DATE,
       (SELECT MAX(S.RECEIVE_DATE)
          FROM HRD.EMPLOYEE_OSV_STATUS S
         WHERE NVL(S.ACTIVE, 'N') = 'Y'
           AND S.MRNO = I.MRNO) OSV_VERIFICATION_REC_DATE,
       I.CONTRACT_TEMPLATE_ID,
       I.CONTRACT_CHANGE_REMARKS REMARKS,
       EC.IS_ORIENTATION_DONE,
       EC.ACTUAL_ORIENTATION_DATE,
       EC.IS_EXPENSE_SUBMITTED,
       EC.FARWARD_TO_EHC,
       EC.EHC_BACK_TO_HR,
      CASE
        WHEN HRD.PKG_NEW_JOINER.F_MEDICAL_REQUIRED(I.PATIENT_MRNO) = 'Y' THEN
            HRD.PKG_NEW_JOINER.F_GET_MEDICAL_DATE(I.PATIENT_MRNO)
        ELSE
            HRD.PKG_NEW_JOINER.F_GET_APPOINMENT_DATE(I.PATIENT_MRNO)
    END AS APPOINMENT_DATE,
       I.PATIENT_MRNO,
       EC.MEDICAL_DATE
  FROM HRD.INFORMATION         I,
       REGISTRATION.PATIENT    P,
       HRD.EMPLOYMENT_CONTRACT EC
 WHERE P.MRNO = EC.MRNO
   AND I.MRNO = P.MRNO
   AND I.ACTIVE = 'Y'
   AND P.ACTIVE = 'Y'
     -- AND EC.FARWARD_TO_EHC ='N'
    -- AND EC.EHC_BACK_TO_HR ='Y'
   AND P.MRNO NOT LIKE '%DUM%'
 ORDER BY P.MRNO
;
```

## HRD.VU_PAYROLL_ATTENDANCE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PAYROLL_ATTENDANCE AS
SELECT pa.month_start_date,
       pa.month_end_date,
       pa.mrno,
       pa.include_in_payroll,
       pa.status,
       substr(pa.mrno, -11) disp_mrno,
       i.name,
       i.department,
       i.designation,
       pa.system_remarks,
       i.department_id,
       i.designation_id,
       pa.actual_working_days,
       pa.days_performed,
       pa.additional_working_days,
       pa.unpaid_leaves,
       pa.actual_shift_minutes,
       pa.performed_minutes,
       pa.calculated_overtime_minutes,
       pa.approved_overtime_minutes,
       pa.proper_swipes,
       pa.improper_swipes,
       pa.no_swipes,
       pa.late_coming,
       pa.early_leaving,
       pa.leave_days,
       pa.nights,
       pa.manual,
       pa.salary_start_date,
       pa.salary_end_date,
       nvl(trunc(pa.actual_shift_minutes / 60), 0) || ':' ||
       nvl(lpad(MOD(pa.actual_shift_minutes, 60), 2, '0'), 0) shift_hrs,
       nvl(trunc(pa.performed_minutes / 60), 0) || ':' ||
       nvl(lpad(MOD(pa.performed_minutes, 60), 2, '0'), 0) performed_hrs,
       nvl(trunc(pa.calculated_overtime_minutes / 60), 0) || ':' ||
       nvl(lpad(MOD(pa.calculated_overtime_minutes, 60), 2, '0'), 0) cal_overtime_hrs,
       nvl(trunc(pa.approved_overtime_minutes / 60), 0) || ':' ||
       nvl(lpad(MOD(pa.approved_overtime_minutes, 60), 2, '0'), 0) verified_overtime_hrs,
       i.joining_date,
       i.leaving_date,
       i.card_swipe_exemption,
       hrd.attendance.get_month_process_id(pa.month_start_date,
                                           pa.month_end_date) process_id,
       hrd.pkg_static_values.get_regular_process_type process_type_id,
       hrd.attendance.get_month_id(pa.month_start_date,
                                           pa.month_end_date) month_id,
PA.LOCATION_ID    ,
I.EMP_LOCATION_ID                                                                                  
  FROM hrd.payroll_attendance pa, hrd.vu_information i
 WHERE pa.mrno = i.mrno;
```

## HRD.VU_PA_ALERT
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_ALERT AS
SELECT A.PA_ALERT_ID,
       A.PATP_ID,
       A.DEPARTMENT_ID,
       A.DEPT_HEAD_CODE,
       A.DEPT_HEAD_EMAIL,
       A.ACTING_DEPT_HEAD_CODE,
       A.ACTING_DEPT_HEAD_EMAIL,
       A.IS_REMINDER,
       A.SEND_BY,
       A.SEND_DATE_TIME,
       A.REMARKS,
       A.SEND_ALERT,
       A.PA_REMINDER_TEXT,
       A.PA_REMINDER_SUBJECT,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT D
         WHERE D.DEPARTMENT_ID = A.DEPARTMENT_ID) DEPARTMENT_NAME,
       SUBSTR(A.DEPT_HEAD_CODE, -11) DISP_DEPT_HEAD_CODE,
       HRD.EMPLOYEE.GET_NAME(A.DEPT_HEAD_CODE) DEPT_HEAD_NAME,
       SUBSTR(A.ACTING_DEPT_HEAD_CODE, -11) DISP_ACTING_HEAD_CODE,
       HRD.EMPLOYEE.GET_NAME(A.ACTING_DEPT_HEAD_CODE) ACTING_DEPT_HEAD_NAME,
       (SELECT DESIGNATION
          FROM HRD.V_INFORMATION I
         WHERE I.MRNO = A.DEPT_HEAD_CODE) DEPT_HEAD_DESIGNATION,
       (SELECT DESIGNATION
          FROM HRD.V_INFORMATION I
         WHERE I.MRNO = A.ACTING_DEPT_HEAD_CODE) ACTING_DEPT_HEAD_DESIGNATION
  FROM HRD.PA_TYPE_PERIOD_ALERT A;
```

## HRD.VU_PA_CATEGORY_TYPE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_CATEGORY_TYPE AS
SELECT ct.pa_type_id,
       ct.pa_category_id,
       ct.active,
       (SELECT description
          FROM hrd.pa_def_type t
         WHERE t.pa_type_id = ct.pa_type_id) type_desc,
       (SELECT description
          FROM hrd.pa_def_category c
         WHERE c.pa_category_id = ct.pa_category_id) category_desc
  FROM hrd.pa_category_type ct;
```

## HRD.VU_PA_DEF_SECTION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_DEF_SECTION AS
SELECT s.pa_section_id,
       s.pa_attribute_id,
       S.TAB_ID,
       s.description,
       s.active,
       s.pa_section_name,
       s.pa_section_type,
       s.pa_object_code,
       s.no_of_emp_req ,
       (SELECT description
          FROM hrd.pa_def_section_attribute a
         WHERE a.pa_attribute_id = s.pa_attribute_id) attribute_name,
       (SELECT display_name
          FROM definitions.objects o
         WHERE o.object_code = s.pa_object_code) object_name,
       decode(s.pa_section_type,
              'O',
              'Open Text',
              'R',
              'Rating Value',
              s.pa_section_type) pa_section_type_desc,
     (SELECT TAB_NAME FROM HRD.PA_TAB_SETUP
     WHERE TAB_ID = S.TAB_ID) TAB_NAME        
  FROM hrd.pa_def_section s;
```

## HRD.VU_PA_DEF_TEMPLATE_SECTION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_DEF_TEMPLATE_SECTION AS
SELECT T.PA_TEMPLATE_ID,
       T.PA_SECTION_ID,
       T.ACTIVE,
       T.ORDER_BY,
       T.PA_SECTION_WEIGHTAGE,
       S.DESCRIPTION SECTION_DESCRIPTION,
       S.PA_SECTION_NAME,
       DECODE(S.PA_SECTION_TYPE,'R','Rating Type','T','Open Text','O','Objective',S.PA_SECTION_TYPE) PA_SECTION_TYPE_DESC,
       T.TEMPLATE_RATING_TYPE_ID
  FROM HRD.PA_DEF_TEMPLATE_SECTION T, HRD.PA_DEF_SECTION S
 WHERE T.PA_SECTION_ID = S.PA_SECTION_ID;
```

## HRD.VU_PA_DEF_TYPE_TEMPLATE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_DEF_TYPE_TEMPLATE AS
SELECT t.pa_type_id, t.pa_template_id, t.active,
          (SELECT description
             FROM hrd.pa_def_type pt
            WHERE pt.pa_type_id = t.pa_type_id) pa_type_desc,
          (SELECT description
             FROM hrd.pa_def_template p
            WHERE p.pa_template_id = t.pa_template_id) pa_template_desc
     FROM hrd.pa_def_type_template t;
```

## HRD.VU_PA_EMPLOYEE_TYPE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_EMPLOYEE_TYPE AS
SELECT e.patp_id,
       e.patient_type_id,
       (SELECT description
          FROM definitions.patient_type
         WHERE patient_type_id = e.patient_type_id) employee_type,
       p.pa_start_date,
       p.pa_end_date,
       (SELECT t.description
          FROM hrd.pa_def_type t
         WHERE t.pa_type_id = p.pa_type_id) pa_type_desc
  FROM hrd.pa_employee_type e, hrd.pa_type_period p
 WHERE e.patp_id = p.patp_id;
```

## HRD.VU_PA_MASTER_HIERARCHY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_MASTER_HIERARCHY AS
SELECT H.PA_MASTER_HIERARCHY_ID,
                  H.APPRAISEE_MRNO,
                  H.PATP_ID,
                  H.TEMPLATE_ID,
                  SUBSTR(H.APPRAISEE_MRNO, -11) EMP_CODE,
                  I.NAME,
                  I.DESIGNATION_ID,
                  I.DESIGNATION,
                  --          i.department_id,
                  H.DEPARTMENT_ID,
                  HRD.PKG_COMMON.GET_DEPARTMENT_NAME(P_DEPARTMENT_ID => H.DEPARTMENT_ID) DEPARTMENT,
                  --          i.department,
                  I.JOINING_DATE,
                  H.PA_MASTER_STATUS_ID,
                   (SELECT DESCRIPTION
                              FROM ORDERENTRY.ORDER_STATUS
                        WHERE ORDER_STATUS_ID = H.PA_MASTER_STATUS_ID) PA_STATUS_DESC,
                  (SELECT T.DESCRIPTION FROM HRD.PA_DEF_TEMPLATE T WHERE T.PA_TEMPLATE_ID = H.TEMPLATE_ID) TEMPLATE_NAME,
                  TP.PA_START_DATE APPRAISAL_START_PERIOD,
                  TP.PA_END_DATE APPRAISAL_END_PERIOD,
                  (SELECT DT.DESCRIPTION FROM HRD.PA_DEF_TYPE DT WHERE DT.PA_TYPE_ID = TP.PA_TYPE_ID) PA_TYPE_DESCRIPTION,
                  TP.PA_TYPE_ID,
                  I.DUTY_LOCATION_ID,
                  I.ORDER_LOCATION_ID,
                  I.ORDER_LOCATION_DESC,
                  (SELECT DESCRIPTION FROM DEFINITIONS.PATIENT_TYPE WHERE PATIENT_TYPE_ID = I.PATIENT_TYPE_ID) EMPLOYEE_TYPE,
                  I.PATIENT_TYPE_ID,
                  H.REPORT_NAME,
                  I.ACTIVE,
                  I.LEAVING_DATE,
                  HRD.PKG_COMMON.GET_CONTINUOUS_JOINING_DATE(I.MRNO) CONTINUOUS_JOINING_DATE
      FROM HRD.PA_MASTER_HIERARCHY      H,
                  HRD.V_INFORMATION     I,
                  HRD.PA_TYPE_PERIOD    TP,
                  HRD.PA_EMPLOYEE_TYPE  ET
WHERE H.APPRAISEE_MRNO = I.MRNO
      AND H.PATP_ID = TP.PATP_ID
      AND H.PATP_ID = ET.PATP_ID
      AND I.PATIENT_TYPE_ID = ET.PATIENT_TYPE_ID
      AND NVL(I.LEAVING_DATE, '31-Dec-9999') > CASE
                        WHEN HRD.PKG_PERFORMANCE_APPRAISAL.GET_REVIEW_PERIOD_ID(H.PATP_ID) = 'A' THEN
                              TP.PA_START_DATE
                        ELSE
                              TO_DATE('30-Dec-9999', 'DD-MON-RRRR')
                  END
;
```

## HRD.VU_PA_OBJECTIVE_DETAIL
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_OBJECTIVE_DETAIL AS
SELECT D.PA_SERIAL_NO,
       D.PA_OBJECTIVE_ID,
       D.PA_LOCATION_ID,
       D.PA_DIVISION_ID,
       D.PA_DEPARTMENT_ID,
       D.PA_DESIGNATION_ID,
       D.PA_MRNO,
       D.DESIG_WISE_DEPT_ID,
       SUBSTR(D.PA_MRNO, -11) DISP_PA_MRNO,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.LOCATION
         WHERE LOCATION_ID = D.PA_LOCATION_ID) ORG_NAME,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DIVISIONS
         WHERE DIVISION_ID = D.PA_DIVISION_ID) DIVISION_NAME,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT
         WHERE DEPARTMENT_ID = D.PA_DEPARTMENT_ID) DEPARTMENT_NAME,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DESIGNATION
         WHERE DESIGNATION_ID = D.PA_DESIGNATION_ID) DESIGNATION_NAME,
       HRD.EMPLOYEE.GET_NAME(D.PA_MRNO) PA_MRNO_NAME,
       (SELECT DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT
         WHERE DEPARTMENT_ID = D.DESIG_WISE_DEPT_ID) DESIGNATION_DEPARTMENT_NAME,
         D.PA_WEIGHTAGE
  FROM HRD.PA_OBJECTIVE_DETAIL D, HRD.PA_OBJECTIVE_MASTER M
 WHERE D.PA_OBJECTIVE_ID = M.PA_OBJECTIVE_ID;
```

## HRD.VU_PA_OBJECTIVE_MASTER
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_OBJECTIVE_MASTER AS
SELECT OM.PA_OBJECTIVE_ID,
       OM.PATP_ID,
       OM.DESCRIPTION,
       OM.USER_REMARKS,
       OM.OBJ_STATUS_ID,
       OM.OBJECTIVE_TYPE_ID,
       OM.ACTIVE,
       OM.SPECIFIC,
       OM.MEASURABLE,
       OM.REALISTIC,
       OM.ACHIEVABLE,
       OM.TIME_BOUND,
       OM.REVIEW_PERIOD,
       OM.OBJ_DEFINED_BY,
       (SELECT DESCRIPTION
          FROM ORDERENTRY.ORDER_STATUS OS
         WHERE OS.ORDER_STATUS_ID = OM.OBJ_STATUS_ID) STATUS_DESC,
       HRD.EMPLOYEE.GET_NAME(OM.OBJ_DEFINED_BY) OBJ_DEFINED_BY_NAME,
       OM.PA_WEIGHTAGE
  FROM HRD.PA_OBJECTIVE_MASTER OM;
```

## HRD.VU_PA_PARAMETER
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PARAMETER AS
SELECT h.hierarchy_id,
       m.pa_perform_id,
       h.appraisee_mrno,
       h.patp_id,
       h.pa_template_id,
       psp.pa_section_id,
       psp.pa_perform_param_id,
       dsp.pa_parameter_name,
       dsp.description parameter_desc,
       dsp.pa_parameter_name || chr(10) || dsp.description display_parameter,
       dsp.pa_parameter_type,
       dsp.is_required,
       dsp.order_by param_order_by,
       dsp.pa_parameter_id,
       (SELECT t.pa_section_weightage
          FROM hrd.pa_def_template_section t
         WHERE t.pa_template_id = h.pa_template_id
           AND t.pa_section_id = psp.pa_section_id) section_weightage
  FROM hrd.pa_perform_section       ps,
       hrd.pa_perform_section_param psp,
       hrd.pa_def_section_parameter dsp,
       hrd.pa_hierarchy             h,
       hrd.pa_perform_master        m
WHERE ps.pa_perform_id = psp.pa_perform_id
   AND ps.pa_section_id = psp.pa_section_id
   AND psp.pa_parameter_id = dsp.pa_parameter_id
   AND psp.pa_section_id = dsp.pa_section_id
   AND psp.pa_perform_id = m.pa_perform_id
   AND m.hierarchy_id = h.hierarchy_id;
```

## HRD.VU_PA_PERFORM_OBJECTIVE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PERFORM_OBJECTIVE AS
SELECT o.pa_perform_id,
       o.pa_serial_no,
       o.pa_objective_id,
       o.pa_expected_value,
       null pa_location_id,
       null pa_division_id,
       null pa_department_id,
       null pa_mrno,
       null disp_pa_mrno,
       null org_name,
       null division_name,
       null department_name,
       null pa_mrno_name,
       o.description objective_description,
       o.patp_id,
       o.remarks user_remarks,
      null objective_type_id,
       null active,
       o.review_period_id review_period,
       null obj_defined_by,
       null status_desc,
       null obj_defined_by_name,
       --om.pa_start_date,
       o.r_start_date pa_start_date,
       --om.pa_end_date,
       o.r_end_date pa_end_date,
       null pa_type_id,
       null pa_type_desc, o.pa_status_id obj_status_id--OM.obj_status_id
  FROM hrd.pa_perform_val_obj o
;
```

## HRD.VU_PA_PERFORM_QUEUE
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PERFORM_QUEUE AS
SELECT T.PA_PERFORM_ID,
       HRD.F_GET_DEPARTMENT_LOCATION_ID(H.DEPARTMENT_ID) LOCATION_ID,
       T.PA_PERFORM_APPRAISER_ID,
       T.PA_IN_QUEUE_OF,
       T.PA_ACTING_FOR,
       T.PA_IN_QUEUE_OF_ROLE,
       T.PA_QUEUE_REMARKS,
       T.PA_QUEUE_ENTRY_DATE,
       PM.HIERARCHY_ID,
       PM.PA_PERFORM_STATUS_ID,
       PM.TRANS_DATE,
       PM.DISTRIBUTED_DATE,
       PM.REMARKS,
       H.APPRAISEE_MRNO,
       H.PATP_ID,
       HRD.PKG_APPRAISAL_COMMON.F_GET_PA_STATUS(PM.PA_PERFORM_STATUS_ID) PA_STATUS_DESC,
       SUBSTR(H.APPRAISEE_MRNO, -11) EMP_CODE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(H.APPRAISEE_MRNO) NAME,
       HRD.F_GET_DESIGNATION_ID(H.APPRAISEE_MRNO,
                                NVL(PM.DISTRIBUTED_DATE, SYSDATE)) DESIGNATION_ID,
       HRD.F_GET_DESIGNATION_DESC(H.APPRAISEE_MRNO,
                                  NVL(PM.DISTRIBUTED_DATE, SYSDATE)) DESIGNATION,
       H.DEPARTMENT_ID,
       (SELECT D.DESCRIPTION
          FROM DEFINITIONS.DEPARTMENT D
         WHERE D.DEPARTMENT_ID = H.DEPARTMENT_ID) DEPARTMENT,
       HRD.F_GET_JOINING_DATE(H.APPRAISEE_MRNO) JOINING_DATE,
       NULL ORDER_LOCATION_DESC,
       NULL EMPLOYEE_TYPE,
       PT.PA_START_DATE APPRAISAL_START_PERIOD,
       PT.PA_END_DATE APPRAISAL_END_PERIOD,
       HRD.PKG_APPRAISAL_COMMON.F_GET_PA_TEMPLATE(H.PA_TEMPLATE_ID) TEMPLATE_NAME,
       DT.DESCRIPTION PA_TYPE_DESCRIPTION,
       PT.PA_TYPE_ID,
       SUBSTR(T.PA_IN_QUEUE_OF, -11) DISP_IN_QUEUE_OF,
       HRD.EMPLOYEE.GET_NAME(T.PA_IN_QUEUE_OF) IN_QUEUE_OF_NAME,
       SUBSTR(T.PA_ACTING_FOR, -11) DISP_ACTING_FOR,
       HRD.EMPLOYEE.GET_NAME(T.PA_ACTING_FOR) ACTING_FOR_NAME,
       H.REPORT_NAME,
       H.PA_TEMPLATE_ID,
       PT.PA_STATUS_ID
  FROM HRD.PA_PERFORM_QUEUE    T,
       HRD.PA_PERFORM_MASTER   PM,
       HRD.PA_HIERARCHY        H,
       HRD.PA_TYPE_PERIOD      PT,
       HRD.PA_DEF_TYPE         DT
 WHERE  T.PA_PERFORM_ID = PM.PA_PERFORM_ID
   AND PM.HIERARCHY_ID = H.HIERARCHY_ID
   AND H.PATP_ID = PT.PATP_ID
   AND HRD.F_IS_ACTIVE_ONLY_EMP_CODE(H.APPRAISEE_MRNO) = 'Y'
   AND PT.PA_TYPE_ID = DT.PA_TYPE_ID
   AND PT.PA_STATUS_ID <> HRD.PKG_PERFORMANCE_APPRAISAL.GET_CLOSE_STATUS_ID;
```

## HRD.VU_PA_PERFORM_QUEUE_HISTORY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PERFORM_QUEUE_HISTORY AS
SELECT h.pa_queue_id,
       h.pa_perform_id,
       h.pa_perform_appraiser_id,
       substr(h.pa_in_queue_of, -11) disp_in_queue_of,
       hrd.employee.get_name(h.pa_in_queue_of) in_queue_of_name,
       h.pa_in_queue_of,
       h.pa_acting_for,
       substr(h.pa_acting_for, -11) disp_acting_for,
       hrd.employee.get_name(h.pa_acting_for) acting_for_name,
       h.pa_in_queue_of_role,
       decode(h.pa_in_queue_of_role,
              'A',
              'Approved',
              'R',
              'Recommend',
              'S',
              'Self',
              'F',
              'Final',
              h.pa_in_queue_of_role) in_queue_of_role_desc,
       h.pa_queue_remarks,
       h.pa_queue_entry_date,
       h.pa_decision_date
  FROM hrd.pa_perform_queue_history h;
```

## HRD.VU_PA_PERFORM_VAL_TEXT
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PERFORM_VAL_TEXT AS
SELECT R.PA_SERIAL_NO,
       r.pa_value,
       r.remarks pa_user_remarks,
       AP.PA_PERFORM_APPRAISER_ID,
       ap.pa_appraiser_mrno pa_enter_by,
       r.trans_date pa_entry_date,
       ap.pa_status_id pa_perform_status_id,
       h.appraisee_mrno,
       h.patp_id,
       h.pa_template_id,
       d.pa_section_id,
       m.pa_perform_id,
       sp.pa_parameter_name,
       sp.description parameter_desc,
       sp.pa_parameter_name || chr(10) || sp.description display_parameter,
       sp.pa_parameter_type,
       sp.is_required,
       sp.order_by param_order_by,
       sp.pa_parameter_id,
       hrd.employee.get_name(ap.pa_appraiser_mrno) pa_enter_by_name,
       (SELECT t.pa_section_weightage
          FROM hrd.pa_def_template_section t
         WHERE t.pa_template_id = h.pa_template_id
           AND t.pa_section_id = d.pa_section_id) section_weightage
  FROM hrd.pa_perform_val_text r,
       hrd.pa_perform_section_param     d,
       hrd.pa_perform_master        m,
       hrd.pa_hierarchy             h,
       hrd.pa_def_section_parameter sp,
       hrd.pa_perform_appraiser ap
 WHERE r.pa_perform_param_id = d.pa_perform_param_id
   AND d.pa_perform_id = m.pa_perform_id
   AND m.hierarchy_id = h.hierarchy_id
   AND d.pa_parameter_id = sp.pa_parameter_id
   AND d.pa_section_id = sp.pa_section_id
   and r.pa_perform_appraiser_id = ap.pa_perform_appraiser_id;
```

## HRD.VU_PA_PERIOD
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_PERIOD AS
SELECT PP.pa_start_date,
                PP.pa_end_date,
                PP.remarks,
                PP.pa_status_id,
                PTP.PA_TYPE_ID,
                PP.PA_YEAR,
                (SELECT description
                   FROM orderentry.order_status
                  WHERE order_status_id = PP.pa_status_id) status_desc
  FROM hrd.pa_period PP, HRD.PA_TYPE_PERIOD PTP
 WHERE PP.PA_START_DATE = PTP.PA_START_DATE
   AND PP.Pa_End_Date = PTP.PA_END_DATE;
```

## HRD.VU_PA_ROUTING
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_ROUTING AS
SELECT P.PA_PERFORM_APPRAISER_ID,
       P.PA_PERFORM_ID,
       P.EMPLOYEE_REIVEW,
       P.HIERARCHY_ID,
       P.PA_APPRAISER_MRNO PA_APPRAISER_MRNO,
       P.PA_APPRAISER_MRNO APPRAISER_CODE,
       P.APPRAISER_ROLE,
       P.ORDER_BY,
       H.DESCRIPTION HIERARCHY_NAME,
       H.APPRAISEE_MRNO,
       H.PATP_ID,
       H.PA_TEMPLATE_ID,
       I.NAME,
       I.DEPARTMENT_ID,
       I.DEPARTMENT,
       I.DESIGNATION_ID,
       I.DESIGNATION,
       P.PA_TEMPLATE_ID APPRAISER_TEMPLATE_ID,
       H.REPORTING_TO,
       (SELECT DESCRIPTION
          FROM HRD.PA_DEF_TEMPLATE T
         WHERE T.PA_TEMPLATE_ID = P.PA_TEMPLATE_ID) TEMPLATE_NAME,
       P.PA_STATUS_ID,
       (SELECT PM.PA_PERFORM_STATUS_ID
          FROM HRD.PA_PERFORM_MASTER PM
         WHERE PM.PA_PERFORM_ID = P.PA_PERFORM_ID
           AND PM.HIERARCHY_ID = H.HIERARCHY_ID) PA_PERFORM_STATUS_ID
  FROM HRD.PA_PERFORM_APPRAISER P, HRD.PA_HIERARCHY H, HRD.V_INFORMATION I
WHERE P.HIERARCHY_ID = H.HIERARCHY_ID
   AND P.PA_APPRAISER_MRNO = I.MRNO;
```

## HRD.VU_PA_SECTION_PARAMETER
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_SECTION_PARAMETER AS
SELECT SP.PA_PARAMETER_NAME || ' ' || SP.DESCRIPTION DISPLAY_PARAMETER,
       SP.PA_PARAMETER_ID,
       SP.PA_SECTION_ID,
       SP.PA_PARAMETER_NAME,
       SP.DESCRIPTION,
       SP.PA_PARAMETER_TYPE,
       SP.PA_RATING_TYPE_ID,
       SP.ACTIVE,
       SP.ORDER_BY,
       SP.IS_QA ,
       SP.IS_REQUIRED,
       SP.PARENT_PARAMETER_ID,
       SP.PARENT_SECTION_ID,
       SP.LOV_ID,
       SP.IS_SUM ,
       SP.NO_OF_NOMINATED ,
       SP.PA_QA_ID,
       SP.IS_PUBLISHED_RESEARCH,
       SP.HR,
       SP.APPROVAL,
       SP.SOURCE_NAME,
       SP.GET_VALUE,
       SP.PROMOTION,
       SP.HR_TRAINING,
       SP.DEPARTMENT_TRAINING,
        SP.REPORTING_TO,
        SP.DESIGNATION_CATEGORY_ID,
        (SELECT C.DESCRIPTION FROM DEFINITIONS.DESIGNATION_CATEGORY  C
        WHERE C.DESIGNATION_CATEGORY_ID = SP.DESIGNATION_CATEGORY_ID)DESIGNATION_CATEGORY,
       (SELECT L.LOV_DESC FROM SECURITY.LOVS L WHERE L.LOV_ID = SP.LOV_ID) LOV_DESC,
       (SELECT S.DESCRIPTION
          FROM HRD.PA_DEF_SECTION S
         WHERE S.PA_SECTION_ID = SP.PA_SECTION_ID) SECTION_DESC,
       (SELECT S.PA_SECTION_NAME
          FROM HRD.PA_DEF_SECTION S
         WHERE S.PA_SECTION_ID = SP.PA_SECTION_ID) SECTION_NAME,
       (SELECT DESCRIPTION
          FROM HRD.PA_DEF_RATING_TYPE
         WHERE PA_RATING_TYPE_ID = SP.PA_RATING_TYPE_ID) RATING_TYPE,
       (SELECT P.PA_PARAMETER_NAME
          FROM HRD.PA_DEF_SECTION_PARAMETER P
         WHERE P.PA_PARAMETER_ID = SP.PARENT_PARAMETER_ID
           AND P.PA_SECTION_ID = SP.PA_SECTION_ID) PARENT_PARAM,
           IS_MARK_DEDUCTION,
           SP.IS_RESEARCH_BLOCK,
           SP.REFRENCE_CANVAS,
           SP.LESS_VALUE,
           SP.APPRAISEE_REMARKS_REQUIRED
  FROM HRD.PA_DEF_SECTION_PARAMETER SP;
```

## HRD.VU_PA_TYPE_PERIOD
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PA_TYPE_PERIOD AS
SELECT p.patp_id,
       p.pa_type_id,
       p.pa_start_date,
       p.pa_end_date,
       p.pa_status_id,
       p.pa_alert_text,
       p.pa_sender_email,
       (SELECT description
          FROM hrd.pa_def_type t
         WHERE t.pa_type_id = p.pa_type_id) pa_type_desc,
       (SELECT description
          FROM orderentry.order_status
         WHERE order_status_id = p.pa_status_id) pa_type_status,
       p.pa_reminder_text,
       p.pa_cut_off_date,
       p.pa_alert_subject,
       p.pa_reminder_subject,
       p.app_type , order_by
  FROM hrd.pa_type_period p;
```

## HRD.VU_PERFORM_VAL_RATING
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PERFORM_VAL_RATING AS
SELECT r.pa_perform_param_id,
       r.pa_rating_value_id,
       r.pa_rating_type_id,
       rv.pa_rating_actual_value,
       r.remarks pa_user_remarks,
       ap.pa_appraiser_mrno pa_enter_by,
       r.trans_date pa_entry_date,
       M.PA_PERFORM_STATUS_ID pa_perform_status_id,
       h.appraisee_mrno,
       h.patp_id,
       R.PA_PERFORM_APPRAISER_ID,
       h.pa_template_id,
       d.pa_section_id,
       m.pa_perform_id,
       (SELECT rv.description
          FROM hrd.pa_def_rating_value rv
         WHERE rv.pa_rating_value_id = r.pa_rating_value_id
           AND rv.pa_rating_type_id = r.pa_rating_type_id) rating_desc,
       sp.pa_parameter_name,
       sp.description parameter_desc,
       sp.pa_parameter_name || chr(10) || sp.description display_parameter,
       sp.pa_parameter_type,
       sp.is_required,
       sp.order_by param_order_by,
       sp.pa_parameter_id,
       hrd.employee.get_name(ap.pa_appraiser_mrno) pa_enter_by_name,
       (SELECT t.pa_section_weightage
          FROM hrd.pa_def_template_section t
         WHERE t.pa_template_id = h.pa_template_id
           AND t.pa_section_id = d.pa_section_id) section_weightage
  FROM hrd.pa_perform_val_rating    r,
       hrd.pa_perform_section_param        d,
       hrd.pa_perform_master        m,
       hrd.pa_hierarchy             h,
       hrd.pa_def_section_parameter sp,
       hrd.pa_perform_appraiser ap,
       hrd.pa_def_rating_value rv
 WHERE r.pa_perform_param_id = d.pa_perform_param_id
    AND d.pa_perform_id = m.pa_perform_id
   AND m.hierarchy_id = h.hierarchy_id
   AND d.pa_parameter_id = sp.pa_parameter_id
   AND d.pa_section_id = sp.pa_section_id
   and r.pa_rating_value_id = rv.pa_rating_value_id
   and r.pa_rating_type_id = rv.pa_rating_type_id
   and r.pa_perform_appraiser_id = ap.pa_perform_appraiser_id;
```

## HRD.VU_POSITION_HIST
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_POSITION_HIST AS
SELECT p.position_start_date position_date,
       p.position_id,
       p.designation_id,
       (SELECT description
          FROM definitions.designation
         WHERE designation_id = p.designation_id) designation_desc,
       p.department_id,
       (SELECT description
          FROM definitions.department
         WHERE department_id = p.department_id) department_desc,
       decode(p.position_type, 'B', 'Budgeted', 'Non Budgeted') position_type,
       p.approved_date,
       p.actual_employee_id,
       (his.pkg_patient.get_patient_name(p.actual_employee_id)) actual_employee_name,
       p.further_employee_id,
       p.further_from_date,
       p.further_end_date,
       p.status_id,
       p.replaced_mrno,
       (his.pkg_patient.get_patient_name(p.replaced_mrno)) replaced_by_name,
       p.position_category,
       p.designation_type_id,
       p.employee_type_id
  FROM hrd.position p
UNION
SELECT history_date position_date,
       p.position_id,
       p.designation_id,
       (SELECT description
          FROM definitions.designation
         WHERE designation_id = p.designation_id) designation_desc,
       p.department_id,
       (SELECT description
          FROM definitions.department
         WHERE department_id = p.department_id) department_desc,
       decode(p.position_type, 'B', 'Budgeted', 'Non Budgeted') position_type,
       p.approved_date,
       p.actual_employee_id,
       (his.pkg_patient.get_patient_name(p.actual_employee_id)) actual_employee_name,
       p.further_employee_id,
       p.further_from_date,
       p.further_end_date,
       p.status_id,
       p.replaced_mrno,
       (his.pkg_patient.get_patient_name(p.replaced_mrno)) replaced_by_name,
       p.position_category,
       p.designation_type_id,
       p.employee_type_id
  FROM hrd.position_history p;
```

## HRD.VU_PROFESSIONAL_REGISTRATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PROFESSIONAL_REGISTRATION AS
SELECT PR.EMPLOYEE_CODE,
       PR.REGISTRATION_TYPE_ID,
       PR.REGISTRATION_NUMBER,
       PR.REGISTRATION_CATEGORY_ID,
       PR.REGISTRATION_DATE,
       PR.ISSUE_DATE,
       PR.EXPIRY_DATE,
       PR.ENTRY_DATE,
       PR.ENTERED_BY,
       PR.VERIFICATION_BY,
       PR.VERIFICATION_DATE,
       PR.REMARKS,
       PR.DEFAULT_RECORD,
       SUBSTR(PR.EMPLOYEE_CODE, -11) EMP_CODE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(P_MRNO => PR.EMPLOYEE_CODE) NAME,
       I.DEPARTMENT_ID,
              HRD.F_GET_DEPARTMENT_NAME(P_MRNO => PR.EMPLOYEE_CODE,P_DATE => SYSDATE)  DEPARTMENT,
       I.DESIGNATION_ID,
       HRD.F_GET_DESIGNATION_DESC(P_MRNO => PR.EMPLOYEE_CODE,P_DATE => SYSDATE) DESIGNATION,
       I.ACTIVE,
       I.JOINING_DATE,
       I.LEAVING_DATE,
       I.duty_location_id,
       (SELECT DESCRIPTION
          FROM HRD.REGISTRATION_TYPE RT
         WHERE RT.REGISTRATION_TYPE_ID = PR.REGISTRATION_TYPE_ID) REGISTRATION_TYPE,
       (SELECT DESCRIPTION
          FROM HRD.REGISTRATION_CATEGORY RC
         WHERE RC.REGISTRATION_CATEGORY_ID = PR.REGISTRATION_CATEGORY_ID) REGISTRATION_CATEGORY,
       HRD.EMPLOYEE.GET_NAME(PR.VERIFICATION_BY) VERIFIED_BY,
       HRD.EMPLOYEE.GET_NAME(PR.ENTERED_BY) ENTERED_BY_NAME,
       DECODE(PR.OSV_STATUS,'Y','Yes','I','Inprocess','No') OSV_STATUS,
       I.PMDC_PNC_NO,
       I.PMDC_PNC_DATE,
       I.PATIENT_TYPE_ID,
       (SELECT DESCRIPTION
       FROM DEFINITIONS.QUALIFICATIONS WHERE
       QUALIFICATION_ID=PR.QUALIFICATION_ID) QUALIFICATION,
       PR.VALIDITY_PERIOD,
       PR.SUBMIT_SLIP,
       PR.SUBMIT_CERTIFICATE,
       PR.SLIP_SUBMIT_DATE,
       I.EMP_LOCATION_ID,
       PR.CURRENT_OSV
  FROM HRD.PROFESSIONAL_REGISTRATIONS PR, HRD.VU_INFORMATION I
WHERE PR.EMPLOYEE_CODE = I.MRNO(+);
```

## HRD.VU_PROFESSIONAL_REG_HISTORY
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_PROFESSIONAL_REG_HISTORY AS
SELECT p.serial_no,
       p.employee_code,
       p.registration_type_id,
       p.registration_number,
       p.registration_category_id,
       p.registration_date,
       p.issue_date,
       p.expiry_date,
       p.entry_date,
       p.entered_by,
       p.verification_by,
       p.verification_date,
       p.remarks,
       p.default_record,
       p.updated_by,
       p.updation_date,
       substr(p.employee_code, -11) emp_code,
       i.name,
       i.department_id,
       i.department,
       i.designation_id,
       i.designation,
       (SELECT description
          FROM hrd.registration_type rt
         WHERE rt.registration_type_id = p.registration_type_id) registration_type,
       (SELECT description
          FROM hrd.registration_category rc
         WHERE rc.registration_category_id = p.registration_category_id) registration_category,
       hrd.employee.get_name(p.verification_by) verified_by_name,
       hrd.employee.get_name(p.updated_by) changed_by_name,
       hrd.employee.get_name(p.entered_by) entered_by_name
  FROM hrd.professional_reg_history p, hrd.v_information i
 WHERE p.employee_code = i.mrno;
```

## HRD.VU_QR_CONTACT_INFO
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_QR_CONTACT_INFO AS
select INFO_TYPE Contact_type ,INFO_VALUE CONTACT  , INFO_KEY EMPLOYEE_CODE ,'Y' ACTIVE from
(
SELECT 'E-mail' AS INFO_TYPE,
       I.EMAIL AS INFO_VALUE,
       I.MRNO AS INFO_KEY
  FROM HRD.VU_INFORMATION I
 --WHERE I.MRNO = '00160000004997'
UNION all
SELECT (case  EPN.PHONE_TYPE when 'SELF' then 'Mobile No.' else EPN.PHONE_TYPE end),
       EPN.CONTACT_NUMBER,
       EPN.ENTITY_VALUE
  FROM REGISTRATION.VU_ENTITY_PHONE_NUMBER EPN
  --where epn.ENTITY_VALUE='00160000004997'
  union all

  select 'Tell',
  '+92 42 35905000 Ext. '||to_char(o.extension_no) extension_no ,
  o.mrno
  from mis_info.cisco_employee_extension o
 --WHERE o.mrno = '00160000004997'
 )
;
```

## HRD.VU_REGISTRATION_DESIGNATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_REGISTRATION_DESIGNATION AS
SELECT rd.designation_category_id,
       rd.registration_type_id,
       rd.active,
       rd.user_remarks,
       dc.description             designation_category,
       rt.description             registration_type
  FROM hrd.registration_designation     rd,
       definitions.designation_category dc,
       hrd.registration_type            rt
 WHERE rd.designation_category_id = dc.designation_category_id
   AND rd.registration_type_id = rt.registration_type_id;
```

## HRD.VU_STUDY_PROGRAM
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_STUDY_PROGRAM AS
SELECT SP.TYPE_ID,
       SP.PROGRAM_ID,
       SP.DESCRIPTION TRAINING_CATEGORY,
       'CME' TRAINING_TYPE,
       I.NAME EMPLOYEE_NAME,
       SUBSTR(SA.MRNO, -5) EMP_CODE,
       I.DESIGNATION,
       I.DEPARTMENT,
       I.JOINING_DATE,
       NVL(SL.LECTURE_TITLE, SSB.DESCRIPTION) TRAINING_COURSE,
       SL.LECTURE_INSTRUCTOR,
       nvl(SL.TRAINER_NAME,
           HIS.PKG_PATIENT.GET_PATIENT_NAME(SL.LECTURE_INSTRUCTOR)) TRAINER,
       SL.SPSS_LECTURE_ID,
       SL.SPS_SUBJECT_ID,
       SL.LSD LECTURE_FROM_DATE,
       SL.LED LECTURE_TO_DATE,
       SL.LECTURE_CREDIT_HOURS,
       I.DEPARTMENT_ID,
       I.DESIGNATION_ID,
       SA.MRNO,
       SSS.LECTURE_DURATION_UNIT,
       SL.TRAINER_NAME,
       NVL(ET.TRAINING_DURATION,'60 Minutes')TRAINING_DURATION,
       ET.BOND_DURATION,
       ET.BOND_COST,
       ET.TOTAL_TRAINING_COST,
       ET.VALIDITY,
       ET.STATUS,
       ET.ORGANIZER,
       'CME' DATA_SOURCE,
       'N' is_mandatory,
       NULL CATEGORY_ID
  FROM HRD.STUDY_PROGRAMS          SP,
       HRD.SP_SESSION              SS,
       HRD.SPS_SUBJECTS            SSS,
       HRD.STUDY_SUBJECTS          SSB,
       HRD.SPSS_LECTURES           SL,
       HRD.SPSSL_ATTENDANCE        SA,
       HRD.V_INFORMATION           I,
       HRD.EMP_TRAINING_OTHER_INFO ET
 WHERE SP.TYPE_ID IN ('TRG', 'CME', 'MDT')
   AND SS.PROGRAM_ID = SP.PROGRAM_ID
   AND SSS.SP_SESSION_ID = SS.SP_SESSION_ID
   AND SSB.SUBJECT_ID = SSS.SUBJECT_ID
   AND SL.SPS_SUBJECT_ID = SSS.SPS_SUBJECT_ID
   AND SA.SPSS_LECTURE_ID = SL.SPSS_LECTURE_ID
   AND SA.DATE_TIME between SL.LECTURE_START_DATE and sl.lecture_end_date
   AND SA.MRNO = I.MRNO
   AND SA.MRNO = ET.MRNO(+)
   AND SA.SPSS_LECTURE_ID = ET.SPSS_LECTURE_ID(+)
UNION ALL
SELECT 'TRG' TYPE_ID,
       SM.SUBJECT_ID PROGRAM_ID,
       (SELECT S.DESCRIPTION
          FROM ICU.SCORE_PARAMETERS S
         WHERE S.SCORE_CATEGORY_ID = 'TCG'
           AND S.SCORE_PARAMETER_ID = TS.CATEGORY_ID) TRAINING_CATEGORY,
       --NVL(TO_CHAR(SM.BRIEF_DESCRIPTION),TO_CHAR(TS.DESCRIPTION)) PROGRAM_DESC,
       INITCAP(TT.DESCRIPTION) TRAINING_TYPE,
       I.NAME EMPLOYEE_NAME,
       SUBSTR(I.MRNO, -5) EMP_CODE,
       I.DESIGNATION DESIGNATION,
       I.DEPARTMENT DEPARTMENT,
       I.JOINING_DATE JOINING_DATE,
       NVL(TO_CHAR(SM.TRAINING_TOPIC), TO_CHAR(TS.DESCRIPTION)) TRAINING_COURSE,
       NULL LECTURE_INSTRUCTOR,
       TRAINING.F_GET_TRAINER_MASTER(SM.SCHEDULE_MASTER_ID) TRAINER,
       NULL SPSS_LECTURE_ID,
       NULL SPS_SUBJECT_ID,
       --  HRD.PKG_HR_EMPLOYEE_RECORD.F_GET_TR_ATTENDED_DATE(SN.NOMINEE_MRNO,TS.SUBJECT_ID)
       SM.ACTUAL_FROM_DATE
     /*  (SELECT MAX(TA.DATETIME)
          FROM TRAINING.TRAINING_ATTENDANCE TA
         WHERE TA.SCHEDULE_MASTER_ID = SM.SCHEDULE_MASTER_ID)*/ LECTURE_FROM_DATE,
       SM.ACTUAL_TO_DATE LECTURE_TO_DATE,
       NULL LECTURE_CREDIT_HOURS,
       I.DEPARTMENT_ID DEPARTMENT_ID,
       I.DESIGNATION_ID DESIGNATION_ID,
       I.MRNO MRNO,
       NULL LECTURE_DURATION_UNIT,
       TRAINING.F_GET_TRAINER_MASTER(SM.SCHEDULE_MASTER_ID) TRAINER_NAME,
       (SELECT T.TRAINING_DURATION || ' ' || U.DESCRIPTION
          FROM TRAINING.Training_Subject T, DEFINITIONS.UNIT U
         WHERE T.TRAINING_DURATION_UNIT_ID = U.UNIT_ID(+)
           AND T.SUBJECT_ID = TS.SUBJECT_ID) TRAINING_DURATION,
       NULL BOND_DURATION,
       NULL BOND_COST,
       NULL TOTAL_TRAINING_COST,
     --  TO_CHAR(SM.TRAINING_VALIDITY_DATE)
        TO_CHAR(HRD.PKG_HR_EMPLOYEE_RECORD.F_GET_VALIDITY_DATE(SM.SCHEDULE_MASTER_ID,SN.NOMINEE_MRNO,TS.SUBJECT_ID),'DD-MON-RRRR') VALIDITY,
       NULL STATUS,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(SM.ORGANIZER_CODE) ORGANIZER,
       'TRG' DATA_SOURCE,
       TS.IS_MANDATORY,
       TS.CATEGORY_ID
  FROM TRAINING.SUBJECT_NOMINEES SN,
       TRAINING.SCHEDULE_MASTER  SM,
       TRAINING.TRAINING_SUBJECT TS,
       TRAINING.TRAINING_TYPE    TT,
       HRD.VU_INFORMATION        I
 WHERE SN.SCHEDULE_ID = SM.SCHEDULE_MASTER_ID
   AND SM.SUBJECT_ID = TS.SUBJECT_ID
   AND TS.TRAINING_TYPE_ID = TT.TRAINING_TYPE_ID(+)
   AND SN.NOMINEE_MRNO = I.MRNO
   AND SN.ACTIVE = 'Y'
      --   AND SN.NOMINEE_MRNO = '00160000007346'
   AND SM.ACTUAL_FROM_DATE IS NOT NULL
   AND SM.ACTUAL_FROM_DATE <= SYSDATE
;
```

## HRD.VU_SYMPOSIUM
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_SYMPOSIUM AS
SELECT ST.DESCRIPTION  SYMPOSIUM_DESC,
       AB.DESCRIPTION  BODY_SYSTEM_DESC,
       ALS.DESCRIPTION SPECIALITY,
       OAS.SYMPOSIUM_TYPE_ID,
       OAS.ABSTRACT_ID,
       OAS.EMAIL_ADDRESS,
       OAS.CONTACT_NO,
       OAS.TITLE,
       OAS.OBJECTIVE,
       OAS.METHOD,
       OAS.RESULTS,
       OAS.CONCLUSION,
       OAS.AUTHORS,
       OAS.INSTITUTE,
       OAS.BODY_SYSTEM_ID,
       OAS.OTHER_BODY_SYSTEM,
       OAS.SPECIALITY_ID,
       OAS.OTHER_SPECIALITY,
       OAS.MEDAL_SESSION,
       OAS.FREE_PAPER,
       OAS.POSTER_PRESENTATION,
       OAS.SUBMISSION_DATE
  FROM HRD.ONLINE_ABSTRACT_SUBMISSION OAS,
       HRD.ABSTRACT_LOV_BODY_SYSTEM   AB,
       HRD.ABSTRACT_LOV_SPECIALITY    ALS,
       HRD.DEF_SYMPOSIUM_TYPE         ST
 WHERE OAS.SYMPOSIUM_TYPE_ID = ST.SYMPOSIUM_TYPE_ID
   AND OAS.BODY_SYSTEM_ID = AB.BODY_SYSTEM_ID
   AND OAS.SPECIALITY_ID = ALS.SPECIALITY_ID;
```

## HRD.VU_TR_STUDY_PROGRAM
```sql
CREATE OR REPLACE FORCE VIEW HRD.VU_TR_STUDY_PROGRAM AS
SELECT 'TRG' TYPE_ID,
 HRD.PKG_HR_EMPLOYEE_RECORD.F_GET_TR_ATTENDED_DATE(SN.NOMINEE_MRNO,ts.parent_subject_id,SN.SCHEDULE_ID) DATE_ATTENDED,
       SM.SUBJECT_ID PROGRAM_ID,
       (SELECT S.DESCRIPTION
         FROM ICU.SCORE_PARAMETERS S
        WHERE S.SCORE_CATEGORY_ID = 'TCG'
        AND S.SCORE_PARAMETER_ID = TS.CATEGORY_ID) TRAINING_CATEGORY,
       --NVL(TO_CHAR(SM.BRIEF_DESCRIPTION),TO_CHAR(TS.DESCRIPTION)) PROGRAM_DESC,
       INITCAP(TT.DESCRIPTION) TRAINING_TYPE,
       I.NAME EMPLOYEE_NAME,
       SUBSTR(I.MRNO, -5) EMP_CODE,
       I.DESIGNATION DESIGNATION,
       I.DEPARTMENT DEPARTMENT,
       I.JOINING_DATE JOINING_DATE,
       NVL(TO_CHAR(SM.TRAINING_TOPIC), TO_CHAR(TS.DESCRIPTION)) TRAINING_COURSE,
       NULL LECTURE_INSTRUCTOR,
       TRAINING.F_GET_TRAINER_MASTER(SM.SCHEDULE_MASTER_ID)  TRAINER,
       NULL SPSS_LECTURE_ID,
       NULL SPS_SUBJECT_ID,
       SM.ACTUAL_FROM_DATE LECTURE_FROM_DATE,
       SM.ACTUAL_TO_DATE LECTURE_TO_DATE,
       NULL LECTURE_CREDIT_HOURS,
       I.DEPARTMENT_ID DEPARTMENT_ID,
       I.DESIGNATION_ID DESIGNATION_ID,
       I.MRNO MRNO,
       NULL LECTURE_DURATION_UNIT,
       TRAINING.F_GET_TRAINER_MASTER(SM.SCHEDULE_MASTER_ID)   TRAINER_NAME,
      (SELECT T.TRAINING_DURATION || ' ' || U.DESCRIPTION
        FROM TRAINING.Training_Subject T, DEFINITIONS.UNIT U
       WHERE T.TRAINING_DURATION_UNIT_ID = U.UNIT_ID(+)
       AND T.SUBJECT_ID = TS.SUBJECT_ID) TRAINING_DURATION,
       NULL BOND_DURATION,
       NULL BOND_COST,
       NULL TOTAL_TRAINING_COST,
       TO_CHAR(SM.TRAINING_VALIDITY_DATE) VALIDITY,
       NULL STATUS,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(SM.ORGANIZER_CODE) ORGANIZER,
       'TRG' DATA_SOURCE,
       HRD.PKG_HR_EMPLOYEE_RECORD.F_GET_TR_VALIDITY_DATE(P_MRNO => SN.NOMINEE_MRNO,
                                                         P_SUBJECT_ID => ts.parent_subject_id) VALIDITY_DATE
  FROM TRAINING.SUBJECT_NOMINEES SN,
       TRAINING.SCHEDULE_MASTER  SM,
       TRAINING.TRAINING_SUBJECT TS,
       TRAINING.TRAINING_TYPE    TT,
       HRD.VU_INFORMATION        I
WHERE SN.SCHEDULE_ID = SM.SCHEDULE_MASTER_ID
   AND SM.SUBJECT_ID = TS.SUBJECT_ID
   AND TS.TRAINING_TYPE_ID = TT.TRAINING_TYPE_ID(+)
   AND SN.NOMINEE_MRNO = I.MRNO
   AND SN.ACTIVE = 'Y'
--   AND SN.NOMINEE_MRNO = '00160000007346'
   AND SM.ACTUAL_FROM_DATE IS NOT NULL
   AND SM.ACTUAL_FROM_DATE <= SYSDATE
;
```

## HRD.V_APPLICANT_CONSULTANT_PRIV
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_APPLICANT_CONSULTANT_PRIV AS
SELECT ACP.APPLICANT_ID,
ACP.PRIVILEGE_ID,
PS.DESCRIPTION,
ACP.APP_EXEMPTED,
AC.APPLICANT_NAME AS NAME,
AC.RECD_PHYSICIAN_DATE,
PS.DESCRIPTION    TAB_DESCRIPTION,
PS.REPORT_HEADER  REPORT_HEADING
  FROM HRD.APPLICANT_CONSULTANT_PRIVILEGE ACP, HRD.PRIVILEGES_SETUP PS, HRD.APPLICANT_CONSULTANTS AC
 WHERE PS.PRIVILEGES_ID = ACP.PRIVILEGE_ID
 AND AC.APPLICANT_ID = ACP.APPLICANT_ID
 AND 0 < CASE WHEN AC.RECD_PHYSICIAN_DATE IS NOT NULL THEN (SELECT COUNT(1) FROM HRD.APPLICANT_PRIV_DETAIL D
WHERE D.APPLICANT_ID = ACP.APPLICANT_ID
AND D.PRIVILEGES_ID = ACP.PRIVILEGE_ID
AND D.REQUESTED = 'Y')
ELSE
  1
END;
```

## HRD.V_APPLICANT_PRIV_DETAIL
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_APPLICANT_PRIV_DETAIL AS
SELECT
CSP.SP_DESCRIPTION,
       PD.APPLICANT_ID,
       PD.PRIVILEGES_ID,
       CPD.PRIVILEGES_DETAIL_ID,
       PD.NUMBER_REQUIRED,
       CPD.ORDER_BY,
       PD.BOLD,
       PD.SP_PRIVILEGE_ID,
       PD.PRIVILEGE_OFFERED,
       PD.PERFORMED_PROCEDURE,
       PD.REQUESTED,
       PD.VERIFIED_YN,
       CSP.PRIVILEGE_TYPE,
       PD.VERIFY_PERFOMED ,
       CPD.IS_NUMBER_REQUIRED,
       pd.SR_NO,
       PD.Granted,
       csp.heading
        FROM HRD.APPLICANT_PRIV_DETAIL PD, DEFINITIONS.CLINICAL_SP_PRIVILEGES_SETUP CSP, DEFINITIONS.CONSULTANT_PRIVILEGES_DETAIL CPD
       WHERE CSP.SP_PRIVILEGE_ID = PD.SP_PRIVILEGE_ID
       AND CPD.PRIVILEGES_ID = PD.PRIVILEGES_ID
       AND CPD.PRIVILEGES_DETAIL_ID = PD.PRIVILEGES_DETAIL_ID
       AND CPD.SP_PRIVILEGE_ID = PD.SP_PRIVILEGE_ID;
```

## HRD.V_APPRAISAL_CONTRACT_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_APPRAISAL_CONTRACT_Q AS
SELECT T.MRNO,
       T.NAME,
       T.DESIG,
       T.DEPT,
       HRD.F_GET_JOINING_DATE(T.MRNO) JOINING_DATE,
       NVL(T.EMP_LOCATION_ID, HRD.F_GET_EMPLOYEE_LOCATION(T.MRNO)) EMP_LOCATION,
       T.EMPLOYEE_ANNIVERSARY_DATE,
       T.EMP_LOCATION_ID,
       T.HR_ACKNOWLEDGE,
       T.HR_ACKNOWLEDGE_DATE,
       T.Q_ENTRY_DATE,
       T.DISTRIBUTION_DATE,
       T.IS_DISTRIBUTED
  FROM HRD.EMP_CONTRACT_PENDING_Q T
 ORDER BY T.MRNO;
```

## HRD.V_APPRAISAL_LOCATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_APPRAISAL_LOCATION AS
SELECT DISTINCT T1.LOV_ID,
       T2.LOCATION_ID,
       T2.LOCATION_DESC,
       T2.SHORT_DESC,
       T4.USERID USER_ID,
       T4.MRNO USER_MRNO,
       T4.FULL_NAME USER_NAME,
       T2.STATUS,
       T2.SHOW_IN_REPORTS,
       T2.ACTUAL_LOCATION,
       T2.ORDER_BY,
       T2.ZON_ID,
       T2.ORG_ID
  FROM SECURITY.LOVS_DETAIL T1,
       HRD.V_LOCATION T2,
       SECURITY.MEMBER      T3,
       SECURITY.USERS       T4
 WHERE T1.LOV_ID = '00186'
   AND (CASE WHEN T1.VALUE=SYS_CONTEXT('GLOBAL_CONTEXT','ORGANIZATION_ID') THEN T2.LOCATION_ID WHEN T2.ACTUAL_LOCATION='NO' THEN T2.LOCATION_ID ELSE T1.VALUE END) = T2.LOCATION_ID
   AND T1.GROUP_ID = T3.GROUPID
   AND T1.ACTIVE = 'Y'
   AND T3.USERID = T4.USERID
   AND T4.ACTIVE = 'Y'
   AND T4.MRNO= SYS_CONTEXT('GLOBAL_CONTEXT','USER_MRNO')
  /***********************************************************************************************
         PURPOSE: This View is used to list of Granted Appraisal Location
         RESULT: User wise Location
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
         1.0        09-JUL--2024  Muhammad Kamran             1. Created this View
  ************************************************************************************************/
;
```

## HRD.V_BOND_TRAINING_GURANTEE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_BOND_TRAINING_GURANTEE AS
SELECT BT.SR_NO,
       BT.MRNO,
       BT.TRAINING_ID   ,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(BT.MRNO)  NAME,
       HRD.F_GET_DEPARTMENT_NAME(BT.MRNO) DEPARTMENT,
       HRD.F_GET_DEPARTMENT_ID(BT.MRNO) DEPARTMENT_ID,
       HRD.F_GET_DESIGNATION_DESC(BT.MRNO) DESIGNATION,
       HRD.F_GET_DESIGNATION_ID(BT.MRNO) DESIGNATION_ID,
       HRD.F_GET_JOINING_DATE(BT.MRNO) JOINING_DATE,
       BT.ACTIVE,
       nominees_mrno,
       BT.REMARKS
       FROM HRD.BOND_TRAINING_GURANTEE BT;
```

## HRD.V_BOND_TRAINING_NOMINEES
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_BOND_TRAINING_NOMINEES AS
SELECT BT.SR_NO,
       BT.MRNO,
       BT.TRAINING_ID,
       TS.DESCRIPTION TRAINING_NAME,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(BT.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(BT.MRNO) DEPARTMENT,
       HRD.F_GET_DEPARTMENT_ID(BT.MRNO) DEPARTMENT_ID,
       HRD.F_GET_DESIGNATION_DESC(BT.MRNO) DESIGNATION,
       HRD.F_GET_DESIGNATION_ID(BT.MRNO) DESIGNATION_ID,
       HRD.F_GET_JOINING_DATE(BT.MRNO) JOINING_DATE,
       BT.BOND_FEES,
       bt.FEE_UNIT,
       BT.BOND_DURATION,
       BT.BOND_DURATION_UNIT,
       BT.BOND_START_DATE,
       BT.BOND_END_DATE,
       BT.ACTIVE,
       BT.REMARKS,
       BT.VISA_FEES,
       BT.TRAVEL_AMOUNT,
       BT.ACCOMODATION,
       BT.DAILY_ALLOWANCE,
       BT.STATUS,
       BT.SR_NO_MASTER,
       VISA_FEES_UNIT,
       TRAVEL_FEES_UNIT,
       ACCOMODATION_UNIT,
       DAILY_ALLOWANCE_UNIT,
       BT.BOND_FEES_TWO,
       BT.BOND_FEE_UNIT_TWO
  FROM HRD.BOND_TRAINING_NOMINEES BT, TRAINING.TRAINING_SUBJECT TS
 WHERE BT.TRAINING_ID = TS.SUBJECT_ID;
```

## HRD.V_BUDGETED_POSITIONS_DEPT_WISE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_BUDGETED_POSITIONS_DEPT_WISE AS
SELECT B.FINANCIAL_YEAR,
B.DEPARTMENT_ID,
B.DESIGNATION_ID,
D.DESCRIPTION DESIGNATION,
B.NO_OF_POSITIONS,
B.REMARKS,
LOCATION_ID,
HRD.F_GET_LOCATION_DESC(LOCATION_ID)LOCATION_DESC,
HRD.PKG_BUDGETED_POSITIONS .F_GET_AVAILED_POSITIONS(P_FINANCIAL_YEAR => B.FINANCIAL_YEAR,
                                                                P_DEPARTMENT_ID => B.DEPARTMENT_ID,
                                                                P_DESIGNATION_ID => B.DESIGNATION_ID)
                                                                POSITIONS_AVAILED,
HRD.PKG_BUDGETED_POSITIONS.F_GET_RJECTED_POSITIONS(P_FINANCIAL_YEAR => B.FINANCIAL_YEAR,
                                                                P_DEPARTMENT_ID => B.DEPARTMENT_ID,
                                                                P_DESIGNATION_ID => B.DESIGNATION_ID)
                                                                REJECTED_POSITIONS,
HRD.PKG_BUDGETED_POSITIONS.F_GET_INPROCESS_POSITIONS(P_FINANCIAL_YEAR => B.FINANCIAL_YEAR,
                                                                P_DEPARTMENT_ID => B.DEPARTMENT_ID,
                                                                P_DESIGNATION_ID => B.DESIGNATION_ID)
                                                                INPROCESS_POSITIONS,
HRD.PKG_BUDGETED_POSITIONS.F_GET_HOLD_POSITIONS(P_FINANCIAL_YEAR => B.FINANCIAL_YEAR,
                                                                P_DEPARTMENT_ID => B.DEPARTMENT_ID,
                                                                P_DESIGNATION_ID => B.DESIGNATION_ID)
                                                                HOLD_POSITIONS
FROM HRD.BUDGETED_POSITIONS_DEPT_WISE B, DEFINITIONS.DESIGNATION D
WHERE D.DESIGNATION_ID = B.DESIGNATION_ID;
```

## HRD.V_CC_EMP_ACTIVATE_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_CC_EMP_ACTIVATE_Q AS
SELECT Q.CC_EMP_CODE,
       Q.CC_EMP_NAME,
       Q.JOINING_DATE,
       Q.DESIGNATION_ID,
       HRD.PKG_S07FRM00271.GET_DESIGNATION(P_DESIGNATION_ID => Q.DESIGNATION_ID) DESIGNATION,
       Q.CC_LOCATION,
       L.DESCRIPTION LOC_DEC,
       Q.REQUEST_DATE,
       Q.STATUS_REMARKS,
       Q.PREVIOUS_STATUS,
        DECODE(PREVIOUS_STATUS,
              'A',
              'Active',
              'N',
              'In-Active',
              'P',
              'Pending for Activation',
              'R','Resigned',
              'F','Fired',
              'B','Blacklist',
              'T','Terminated',
              'J','Rejected') PREVIOUS_STATUS_DESC,
       Q.ACCEPT,
       Q.REJECT,
       Q.Status,
       Q.LEAVE_DATE,
       Q.IN_ACTIVE_REMARKS,
       Q.REASON_ID,
       (SELECT JL.DESCRIPTION FROM HRD.JOB_LEAVING_REASON JL
       WHERE JL.REASON_ID = Q.REASON_ID ) RESON_DESC
  FROM HRD.CC_EMP_ACTIVATE_Q Q, DEFINITIONS.LOCATION L
 WHERE Q.CC_LOCATION = L.LOCATION_ID
 AND Q.STATUS = 'P';
```

## HRD.V_COLUMN_WISE_HINTS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_COLUMN_WISE_HINTS AS
SELECT O.OBJECT_CODE, O.BLOCK_NAME, O.DISPLAY_NAME, H.HINT_DESC
  FROM HRD.COLUMN_WISE_HINTS H, HRD.OBJECT_WISE_COLUMNS O
 WHERE O.OBJECT_CODE = H.OBJECT_CODE(+)
   AND O.BLOCK_NAME = H.BLOCK_NAME(+)
   AND O.COLUMN_NAME = H.COLUMN_NAME(+)
   AND H.ACTIVE = 'Y';
```

## HRD.V_CONSULTANT_PRIVIG_GRANT_D
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_CONSULTANT_PRIVIG_GRANT_D AS
SELECT D.MRNO,
D.PRIVILEGES_ID,
D.SR_NO,
D.DOC_TYPE_ID,
D.INITIAL_EFFECTIVE_DATE,
D.FROM_DATE,
D.TO_DATE,
D.PRIVILEGES_DETAIL_ID,
D.IS_NUMBER_REQUIRED,
D.NUMBER_REQUIRED,
D.SP_PRIVILEGE_ID,
D.GRANTED,
D.PRIVILEGE_TYPE,
CPD.ORDER_BY,
D.SP_DESCRIPTION,
CPD.BOLD,
D.APPLICANT_ID,
D.PSB_DATE,
D.is_send_email
FROM HRD.CONSULTANT_PRIVIG_GRANT_D D,DEFINITIONS.CONSULTANT_PRIVILEGES_DETAIL CPD
WHERE CPD.PRIVILEGES_ID = D.PRIVILEGES_ID
AND CPD.PRIVILEGES_DETAIL_ID = D.PRIVILEGES_DETAIL_ID;
```

## HRD.V_CONSULTANT_PRIVIG_GRANT_M
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_CONSULTANT_PRIVIG_GRANT_M AS
SELECT GM.MRNO,
       GM.PRIVILEGE_ID,
       S.DESCRIPTION,
       S.PATIENT_CATEGORY,
       DECODE(S.PATIENT_CATEGORY,
                      'A',
                      'All',
                      'D',
                      'Adults',
                      'P',
                      'Peads') PATIENT_CATEGORY_DESC
        FROM HRD.CONSULTANT_PRIVIG_GRANT_M GM, HRD.PRIVILEGES_SETUP S
       WHERE S.PRIVILEGES_ID = GM.PRIVILEGE_ID;
```

## HRD.V_CURRENT_EMPLOYEE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_CURRENT_EMPLOYEE AS
SELECT T.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(T.MRNO) NAME,
       T.DEPARTMENT_ID,
       HRD.F_GET_DESIGNATION_DESC(T.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(T.MRNO) JOINING_DATE,
       RFID.PKG_COMMON.F_GET_RFID_CODE(T.MRNO) RFID_CODE
  FROM HRD.CURRENT_EMPLOYEES T
 WHERE SUBSTR(T.MRNO, 4, 3) != 'EXT'
   AND SUBSTR(T.MRNO, 1, 6) != '001222';
```

## HRD.V_DEPT_WISE_CV_SHORTLIST_EMP
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_DEPT_WISE_CV_SHORTLIST_EMP AS
SELECT
       DP.MRNO ,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(DP.MRNO) EMPLOYEE_NAME,
       HRD.F_GET_DESIGNATION_DESC(DP.MRNO) DESIGNATION,
       DP.ACTIVE,
       DP.DEPARTMENT_ID
       FROM  HRD.DEPT_WISE_CV_SHORTLIST_EMP DP;
```

## HRD.V_DUTY_ROSTER
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_DUTY_ROSTER AS
SELECT lt.short_desc leave_type_desc,
       l.hrd_description short_desc,
       s.short_desc shift_desc,
       dr.mrno,
       dr.duty_date,
       dr.shift_id,
       dr.remarks,
       dr.over_time_allowed,
       dr.leave_type_id,
       dr.short_leave,
       null user_id,
       null terminal,
       null trn_date,
       --dr.user_id,
--       dr.terminal,
  --     dr.trn_date,
       --DR.LEAVE_TYPE_DESC, -- REMOVE THIS COLUMN FROM DUTY_ROSTER
       --DR.SHIFT_DESC -- REMOVE THIS COLUMN FROM DUTY_ROSTER
       nvl(sd.shift_start_time, to_date(s.start_time, 'HH24:MI')) start_time,
       nvl(sd.shift_end_time, to_date(s.end_time, 'HH24:MI')) end_time,
       --DR.START_TIME, -- REMOVE THIS COLUMN FROM DUTY_ROSTER
       --DR.END_TIME, -- REMOVE THIS COLUMN FROM DUTY_ROSTER
       dr.location_id,
       decode(dr.leave_type_desc,
              'F',
              'FORTNIGHTLY_OFF',
              'W',
              'WEEKLY_OFF',
              'DD',
              'NORMAL',
              'G',
              'NORMAL',
              'LEAVE') v_attribute,
       d.description edh_department
  FROM hrd.duty_roster                 dr,
       hrd.leave_type                  lt,
       definitions.location            l,
       hrd.shift                       s,
       hrd.shift_days                  sd,
       hrd.employee_department_history edh,
       definitions.department          d
 WHERE --DR.MRNO = '00160000001654'
--AND DR.DUTY_DATE BETWEEN '23-JUN-2008' AND '22-JUL-2008'
--AND
 dr.duty_date BETWEEN edh.start_date AND
 nvl(edh.end_date, dr.duty_date + 1)
 AND dr.leave_type_id = lt.leave_type_id
 AND dr.location_id = l.location_id
 AND dr.shift_id = s.shift_id
 AND dr.duty_date = sd.shift_date(+)
 AND dr.shift_id = sd.shift_id(+)
 AND dr.mrno = edh.mrno(+)
 AND edh.department_id = d.department_id(+)
;
```

## HRD.V_EMPLOYEE_INFORMATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMPLOYEE_INFORMATION AS
SELECT I.MRNO EMPLOYEE_CODE,
       I.NAME,
       I.DEPARTMENT,
       i.DEPARTMENT_ID,
       I.DUTY_LOCATION_ID,
       I.EMP_LOCATION_ID,
       I.DESIGNATION,
       I.NIC CNIC_NO,
       HIS.PKG_PATIENT.GET_CONTACT_NUMBER(I.MRNO) CONTACT_NUMBER,
       HIS.PKG_PATIENT.GET_PERMANENT_ADDRESS(I.MRNO) PERMANENT_ADDRESS,

       (SELECT MAX(PD.CONTACT_PERSON)
          FROM REGISTRATION.PATIENT_ADDRESS_INFO PD
         WHERE PD.ADDRESS_TYPE = 'E'
           AND PD.MRNO = I.MRNO) EMERGENCY_CONTACT_PERSON,
       (SELECT MAX(R.DESCRIPTION)
          FROM REGISTRATION.PATIENT_ADDRESS_INFO PD, DEFINITIONS.RELATION R
         WHERE PD.ADDRESS_TYPE = 'E'
           AND R.RELATION_ID = PD.RELATION_ID
           AND PD.MRNO = I.MRNO) EMERGENCY_RELATION,
       HIS.PKG_PATIENT.GET_EMERGENCY_ADDRESS(I.MRNO) EMERGENCY_ADDRESS,
       HRD.F_GET_LOCATION_DESC(I.EMP_LOCATION_ID) EMPLOYEE_LOCATION,
       I.DUTY_LOCATION_DESC DUTY_LOCATION,

       (SELECT SUBSTR(SYS_CONNECT_BY_PATH(CONTACT_NUMBER, ','), 2)

          FROM (SELECT ENTITY_VALUE,
                       CONTACT_NUMBER,
                       COUNT(*) OVER(PARTITION BY ENTITY_VALUE) CNT,
                       ROW_NUMBER() OVER(PARTITION BY ENTITY_VALUE ORDER BY CONTACT_NUMBER) SEQ
                  FROM REGISTRATION.VU_ENTITY_PHONE_NUMBER
                 WHERE ENTITY_VALUE = I.MRNO
                   AND PHONE_TYPE_ID = '00102')
         WHERE SEQ = CNT
         START WITH SEQ = 1
        CONNECT BY PRIOR SEQ + 1 = SEQ
               AND PRIOR ENTITY_VALUE = ENTITY_VALUE) SELF_MOBILE,

       (SELECT SUBSTR(SYS_CONNECT_BY_PATH(CONTACT_NUMBER, ','), 2)

          FROM (SELECT ENTITY_VALUE,
                       CONTACT_NUMBER,
                       COUNT(*) OVER(PARTITION BY ENTITY_VALUE) CNT,
                       ROW_NUMBER() OVER(PARTITION BY ENTITY_VALUE ORDER BY CONTACT_NUMBER) SEQ
                  FROM REGISTRATION.VU_ENTITY_PHONE_NUMBER
                 WHERE ENTITY_VALUE = I.MRNO
                   AND PHONE_TYPE_ID = '00109')
         WHERE SEQ = CNT
         START WITH SEQ = 1
        CONNECT BY PRIOR SEQ + 1 = SEQ
               AND PRIOR ENTITY_VALUE = ENTITY_VALUE) EMERGENCY_CONTACT
  FROM HRD.VU_INFORMATION I
 WHERE I.ACTIVE = 'Y'
   AND I.JOINING_DATE IS NOT NULL
   AND I.MRNO NOT IN ('00167100000006', '00167100000004')
   AND I.MRNO NOT LIKE ('%EXT%')
   AND I.MRNO NOT LIKE ('%D%');
```

## HRD.V_EMP_CARD_SWIPE_ADJUSTMENT
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_CARD_SWIPE_ADJUSTMENT AS
SELECT
        A.SR_NO,
        A.MRNO,
        A.ENTER_BY,
        HIS.PKG_PATIENT.GET_PATIENT_NAME(A.ENTER_BY)ENTER_BY_NAME,
        A.ENTRY_DATE,
        A.ORIGIONAL_TIME_IN,
        A.ORIGIONAL_TIME_OUT,
        A.ADJUSTED_TIME_IN,
        A.ADJUSTED_TIME_OUT,
        A.REASON_ID,
        R.DESCRIPTION REASON_DESC,
        A.STATUS,
        DECODE(A.STATUS,'D','Drafted','F','Forwarded','A','Approved','R','Rejected','W','Withdrawn')STATUS_DESC,
        A.REAMRKS,
        A.DUTY_DATE,
        A.SHIFT_ID
        FROM HRD.EMP_CARD_SWIPE_ADJUSTMENT A ,  DEFINITIONS.CARD_REASONS R
        WHERE A.REASON_ID = R.REASON_ID;
```

## HRD.V_EMP_CARD_SWIPE_Q_DETAIL
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_CARD_SWIPE_Q_DETAIL AS
SELECT Q.APPLICANT_MRNO,
        HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.APPLICANT_MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(Q.APPLICANT_MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(Q.APPLICANT_MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(Q.APPLICANT_MRNO) JOINING_DATE,
       Q.EMP_ADJUST_SR_NO,
       Q.FORWARD_TO,
       Q.ACTING_FOR,
       Q.REMARKS,
       Q.AUTHORITY_LEVEL_ID,
       Q.AUTORITY_APPROVE_DATE,
       Q.LEAVE_HIERARCHY_AUTH_ID,
       Q.HR_REMARKS,
       Q.Q_ENTRY_DATE,
       Q.ADJUSTED_TIME_IN,
       Q.ADJUSTED_TIME_OUT,
       Q.ORIGIONAL_TIME_IN,
       Q.ORIGIONAL_TIME_OUT,
       Q.DUTY_DATE,
       Q.STATUS,
       Q.REJECTTION_REMARKS,
       Q.REASON_ID,
       R.DESCRIPTION REASON_DESC,
       Q.SHIFT_ID
       FROM HRD.EMP_CARD_SWIPE_ADJUSTMENT_Q Q , DEFINITIONS.CARD_REASONS R
       WHERE Q.REASON_ID = R.REASON_ID;
```

## HRD.V_EMP_CLEARANCE_HR_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_CLEARANCE_HR_Q AS
SELECT DISTINCT(Q.MRNO),
        HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(Q.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(Q.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(Q.MRNO) JOINING_DATE,
       Q.IS_FORWARD_FINANCE,
       Q.STATUS,
       Q.CLEARANCE_CERTIFICATE_ID,
       Q.PROCESS_ID
       , DECODE(STATUS,
                 'H', 'HR Queue',
                 'F', 'Finance Queue',
                 'C', 'Complete',
                 'S', 'Finance Back to HR',
                 'Unknown')STATUS_DESC
       FROM HRD.EMP_CLEARANCE_DETAIL_EVENT Q
       WHERE Q.IS_FORWARD_FINANCE = 'Y'
       AND Q.IS_BACK_HR='Y'
       AND Q.STATUS= 'S';
```

## HRD.V_EMP_CONTRACT_PENDING_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_CONTRACT_PENDING_Q AS
SELECT Q.MRNO,
       Q.NAME,
       Q.DEPT_ID,
       Q.DEPT DEPARTMENT,
       Q.ALERT_ID,
       Q.CC_EMAIL,
       Q.BCC_EMAIL,
       Q.RECIPIENT_EMAIL,
       Q.DESIG_ID,
       Q.DESIG DESIGNATION,
       Q.START_DATE,
       Q.END_DATE,
       NVL(Q.EMP_LOCATION_ID, HRD.F_GET_EMPLOYEE_LOCATION(Q.MRNO)) EMP_LOCATION,
       Q.MANGER_CODE
  FROM HRD.EMP_CONTRACT_PENDING_Q Q;
```

## HRD.V_EMP_DEPARTMENT_HISTORY
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_DEPARTMENT_HISTORY AS
SELECT H.MRNO,
       H.START_DATE,
       H.END_DATE,
       H.DEPARTMENT_ID,
       D.DESCRIPTION DEPARTMENT,
       'N' DEPT_TYPE,
       'Normal' DEPT_TYPE_DESC,
       D.LOCATION_ID
  FROM HRD.EMPLOYEE_DEPARTMENT_HISTORY H, DEFINITIONS.DEPARTMENT D
 WHERE H.DEPARTMENT_ID = D.DEPARTMENT_ID
 AND SYSDATE BETWEEN H.START_DATE AND NVL(H.END_DATE,SYSDATE)+1
UNION
SELECT AD.MRNO,
       AD.START_DATE,
       AD.END_DATE,
       AD.DEPARTMENT_ID,
       D.DESCRIPTION DEPARTMENT,
       'A' DEPT_TYPE,
       'Additional' DEPT_TYPE_DESC,
       D.LOCATION_ID
  FROM HRD.EMP_ADDITIONAL_DEPT AD, DEFINITIONS.DEPARTMENT D
 WHERE AD.DEPARTMENT_ID = D.DEPARTMENT_ID
 AND SYSDATE BETWEEN AD.START_DATE AND NVL(AD.END_DATE,SYSDATE)+1;
```

## HRD.V_EMP_FINANCE_CLEARANCE_M_Q
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_FINANCE_CLEARANCE_M_Q AS
SELECT DISTINCT (Q.MRNO),
                HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.MRNO) NAME,
                HRD.F_GET_DEPARTMENT_NAME(Q.MRNO) DEPARTMENT,
                HRD.F_GET_DESIGNATION_DESC(Q.MRNO) DESIGNATION,
                HRD.F_GET_JOINING_DATE(Q.MRNO) JOINING_DATE,
                Q.IS_FORWARD_FINANCE,
                Q.STATUS,
                DECODE(STATUS,
                       'H',
                       'HR Queue',
                       'F',
                       'Finance Queue',
                       'C',
                       'Complete',
                       'S',
                       'Finance Back to HR',
                       'Unknown') STATUS_DESC,
                Q.REMARKS
  FROM HRD.EMP_CLEARANCE_PENDING_Q Q
 WHERE Q.IS_FORWARD_FINANCE = 'Y'
   AND Q.IS_BACK_HR = 'N';
```

## HRD.V_EMP_FINANCE_CLEARANCE_Q_D
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_FINANCE_CLEARANCE_Q_D AS
SELECT Q.MRNO,
        HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(Q.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(Q.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(Q.MRNO) JOINING_DATE,
       Q.IS_FORWARD_FINANCE,
       Q.FORWARD_BY_FINANCE,
       Q.FORWARD_FINANCE_DATE,
       Q.STATUS,
       Q.SETUP_ID,
       Q.EVENT_DETIAL_DESC ,
       Q.COUNT,
       Q.MANUAL_COUNT,
       Q.REMARKS,
       Q.FORWARD_BACK_HR,
       Q.FORWARD_BACK_HR_DATE,
       Q.PROCESS_ID,
       Q.CLEARANCE_CERTIFICATE_ID,
       Q.LAST_WORKING_DAY
       FROM HRD.EMP_CLEARANCE_PENDING_Q Q
       WHERE Q.IS_FORWARD_FINANCE = 'Y';
```

## HRD.V_EMP_INCENTIVE_QUEUE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_INCENTIVE_QUEUE AS
SELECT Q.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(Q.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(Q.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(Q.MRNO) JOINING_DATE,
       Q.PROBATION_START_DATE,
       Q.PROBATION_END_DATE,
       Q.STATUS,
       Q.Q_ENTRY_DATE,
       Q.VERIFY_BY,
       Q.VERIFY_DATE,
       Q.FORWARD_HR,
       Q.REMARKS,
       Q.ALLOWANCE_STATUS,
       ALLOWANCES_ID,
       HRD.F_GET_EMPLOYEE_LOCATION(Q.MRNO) EMP_LOCATION
  FROM HRD.EMP_INCENTIVE_QUEUE Q
 WHERE Q.FORWARD_HR = 'N'
   AND Q.STATUS = 'I';
```

## HRD.V_EMP_INCENTIVE_Q_HR
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_INCENTIVE_Q_HR AS
SELECT Q.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(Q.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(Q.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(Q.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(Q.MRNO) JOINING_DATE,
       Q.PROBATION_START_DATE,
       Q.PROBATION_END_DATE,
       Q.STATUS,
       Q.Q_ENTRY_DATE,
       Q.FORWARD_HR,
       Q.INCENTIVE_START_DATE,
       Q.REMARKS,
       Q.HR_VERIFY_BY,
       Q.HR_VERIFY_DATE,
       Q.ALLOWANCE_STATUS,
       HRD.F_GET_EMPLOYEE_LOCATION(Q.MRNO) EMP_LOCATION,
       Q.ALLOWANCES_ID
  FROM HRD.EMP_INCENTIVE_QUEUE Q
 WHERE Q.FORWARD_HR = 'Y'
 AND Q.STATUS='I';
```

## HRD.V_STAFF_COMBINED_DUTY
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_STAFF_COMBINED_DUTY AS
SELECT 'ON_CALL_DUTY_ROSTER_NEW' AS SHIFT_SOURCE,
       'PRIMARY' AS SOURCE_COLUMN,
       CASE
         WHEN N.POST_CALL = 'Y' THEN
          'POST_CALL'
         ELSE
          'ON_CALL'
       END AS ONCALL_ROLE,
       'ONCALL|' || ROWIDTOCHAR(N.ROWID) || '|PRIMARY' AS SHIFT_KEY,
       N.ROSTER_DATE,
       N.ROSTER_END_DATE,
       N.ROSTER_TYPE_ID,
       'UK' AS SHIFT_ID,
       N.ROSTER_BATCH_GROUP_ID,
       N.ROSTER_BATCH_ID,
       N.POST_CALL,
       N.ROSTER_PRIMARY_MRNO AS MRNO,
       N.START_TIME AS SHIFT_START_DT,
       TRUNC(N.ROSTER_END_DATE) + (N.END_TIME - TRUNC(N.END_TIME)) AS SHIFT_END_DT
  FROM HRD.ON_CALL_DUTY_ROSTER_NEW N
 WHERE N.ROSTER_PRIMARY_MRNO IS NOT NULL

UNION ALL

SELECT 'ON_CALL_DUTY_ROSTER_NEW' AS SHIFT_SOURCE,
       'COVERING' AS SOURCE_COLUMN,
       CASE
         WHEN N.POST_CALL = 'Y' THEN
          'POST_CALL'
         ELSE
          'ON_CALL'
       END AS ONCALL_ROLE,
       'ONCALL|' || ROWIDTOCHAR(N.ROWID) || '|COVERING' AS SHIFT_KEY,
       N.ROSTER_DATE,
       N.ROSTER_END_DATE,
       N.ROSTER_TYPE_ID,
       'UK' AS SHIFT_ID,
       N.ROSTER_BATCH_GROUP_ID,
       N.ROSTER_BATCH_ID,
       N.POST_CALL,
       N.ROSTER_COVERING_MRNO AS MRNO,
       N.START_TIME AS SHIFT_START_DT,
       TRUNC(N.ROSTER_END_DATE) + (N.END_TIME - TRUNC(N.END_TIME)) AS SHIFT_END_DT
  FROM HRD.ON_CALL_DUTY_ROSTER_NEW N
 WHERE N.ROSTER_COVERING_MRNO IS NOT NULL

UNION ALL

SELECT 'ON_CALL_DUTY_ROSTER_NEW' AS SHIFT_SOURCE,
       'SECONDARY' AS SOURCE_COLUMN,
       CASE
         WHEN N.POST_CALL = 'Y' THEN
          'POST_CALL'
         ELSE
          'ON_CALL'
       END AS ONCALL_ROLE,
       'ONCALL|' || ROWIDTOCHAR(N.ROWID) || '|SECONDARY' AS SHIFT_KEY,
       N.ROSTER_DATE,
       N.ROSTER_END_DATE,
       N.ROSTER_TYPE_ID,
       'UK' AS SHIFT_ID,
       N.ROSTER_BATCH_GROUP_ID,
       N.ROSTER_BATCH_ID,
       N.POST_CALL,
       N.ROSTER_SECONDARY_MRNO AS MRNO,
       N.START_TIME AS SHIFT_START_DT,
       TRUNC(N.ROSTER_END_DATE) + (N.END_TIME - TRUNC(N.END_TIME)) AS SHIFT_END_DT
  FROM HRD.ON_CALL_DUTY_ROSTER_NEW N
 WHERE N.ROSTER_SECONDARY_MRNO IS NOT NULL

UNION ALL

SELECT 'ON_CALL_DUTY_ROSTER_NEW' AS SHIFT_SOURCE,
       'PERSON_4' AS SOURCE_COLUMN,
       CASE
         WHEN N.POST_CALL = 'Y' THEN
          'POST_CALL'
         ELSE
          'ON_CALL'
       END AS ONCALL_ROLE,
       'ONCALL|' || ROWIDTOCHAR(N.ROWID) || '|PERSON4' AS SHIFT_KEY,
       N.ROSTER_DATE,
       N.ROSTER_END_DATE,
       N.ROSTER_TYPE_ID,
       'UK' AS SHIFT_ID,
       N.ROSTER_BATCH_GROUP_ID,
       N.ROSTER_BATCH_ID,
       N.POST_CALL,
       N.ONCALL_PERSON_4 AS MRNO,
       N.START_TIME AS SHIFT_START_DT,
       TRUNC(N.ROSTER_END_DATE) + (N.END_TIME - TRUNC(N.END_TIME)) AS SHIFT_END_DT
  FROM HRD.ON_CALL_DUTY_ROSTER_NEW N
 WHERE N.ONCALL_PERSON_4 IS NOT NULL

UNION ALL

SELECT 'ON_CALL_DUTY_ROSTER_NEW' AS SHIFT_SOURCE,
       'PERSON_5' AS SOURCE_COLUMN,
       CASE
         WHEN N.POST_CALL = 'Y' THEN
          'POST_CALL'
         ELSE
          'ON_CALL'
       END AS ONCALL_ROLE,
       'ONCALL|' || ROWIDTOCHAR(N.ROWID) || '|PERSON5' AS SHIFT_KEY,
       N.ROSTER_DATE,
       N.ROSTER_END_DATE,
       N.ROSTER_TYPE_ID,
       'UK' AS SHIFT_ID,
       N.ROSTER_BATCH_GROUP_ID,
       N.ROSTER_BATCH_ID,
       N.POST_CALL,
       N.ONCALL_PERSON_5 AS MRNO,
       N.START_TIME AS SHIFT_START_DT,
       TRUNC(N.ROSTER_END_DATE) + (N.END_TIME - TRUNC(N.END_TIME)) AS SHIFT_END_D
  FROM HRD.ON_CALL_DUTY_ROSTER_NEW N
 WHERE N.ONCALL_PERSON_5 IS NOT NULL

UNION ALL

SELECT 'DUTY_ROSTER' AS SHIFT_SOURCE,
       'SHIFT_ID' AS SOURCE_COLUMN,
       'REGULAR' AS ONCALL_ROLE,
       'DUTY|' || ROWIDTOCHAR(DR.ROWID) AS SHIFT_KEY,
       DR.DUTY_DATE AS ROSTER_DATE,
       DR.DUTY_DATE AS ROSTER_END_DATE,
       0 AS ROSTER_TYPE_ID,
       DR.SHIFT_ID,
       NULL AS ROSTER_BATCH_GROUP_ID,
       NULL AS ROSTER_BATCH_ID,
       NULL AS POST_CALL,
       DR.MRNO AS MRNO,
       SD.SHIFT_START_TIME AS SHIFT_START_DT,
       SD.SHIFT_END_TIME AS SHIFT_END_DT
  FROM HRD.DUTY_ROSTER DR
  LEFT JOIN HRD.SHIFT_DAYS SD
    ON DR.DUTY_DATE = SD.SHIFT_DATE
   AND DR.SHIFT_ID = SD.SHIFT_ID
 WHERE DR.MRNO IS NOT NULL
   AND DR.LEAVE_TYPE_ID = '001';
```

## HRD.V_EMP_ONCALL_LFA_LEAVES
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_ONCALL_LFA_LEAVES AS
SELECT DISTINCT LD.MRNO,
       LD.FROM_DATE,
       LD.TO_DATE,
       LD.LEAVE_TYPE_ID,
       LT.DESCRIPTION AS LEAVE_TYPE,
       V.ROSTER_TYPE_ID,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(LD.MRNO)  NAME,
       HRD.F_GET_DEPARTMENT_NAME(LD.MRNO) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(LD.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(LD.MRNO) JOINING_DATE
  FROM HRD.EMPLOYEE_LEAVES LD
  JOIN HRD.LEAVE_TYPE LT
    ON LT.LEAVE_TYPE_ID = LD.LEAVE_TYPE_ID
  JOIN HRD.V_STAFF_COMBINED_DUTY V
    ON V.MRNO = LD.MRNO
   AND V.ROSTER_DATE BETWEEN LD.FROM_DATE AND LD.TO_DATE
WHERE V.ROSTER_TYPE_ID IN (185, 186, 187, 188, 189)
--   AND V.ROSTER_DATE BETWEEN  '01-JAN-2026' AND '30-APR-2026'
   AND LD.LEAVE_TYPE_ID IN ('018')
--ORDER BY LD.FROM_DATE,LD.MRNO
;
```

## HRD.V_EMP_PROMOTION_REPORT
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_PROMOTION_REPORT AS
SELECT H.PA_TEMPLATE_ID,
       H.APPRAISEE_MRNO EMP_CODE,
       MAX(HRD.EMPLOYEE.GET_NAME(H.APPRAISEE_MRNO)) EMP_NAME,
       MAX(HRD.EMPLOYEE.GET_DESIGNATION(H.APPRAISEE_MRNO)) EMP_DESIG,
       MAX(HRD.EMPLOYEE.GET_DEPARTMENT(H.APPRAISEE_MRNO)) EMP_DEPT,
       SUM(PR.PA_RATING_VALUE_ID) ACTUAL_VALUE,
       HRD.PKG_PERFORMANCE_APPRAISAL.F_GET_PA_SCORE(H.PATP_ID, H.APPRAISEE_MRNO) SCORE,
       HRD.PKG_APPRAISAL_COMMON.F_FAR_GRADE(HRD.PKG_PERFORMANCE_APPRAISAL
                                            .F_GET_PA_SCORE(H.PATP_ID,
                                                           H.APPRAISEE_MRNO)) GRADING,
       --H.PA_TEMPLATE_ID,
       PM.PA_PERFORM_ID,
       (SELECT LISTAGG(T.PA_VALUE,'-')
          FROM HRD.PA_PERFORM_VAL_TEXT      T,
               HRD.PA_PERFORM_SECTION_PARAM SP,
               HRD.PA_PERFORM_APPRAISER     PA,
                HRD.PA_DEF_SECTION_PARAMETER PDSP
         WHERE SP.PA_PERFORM_PARAM_ID = T.PA_PERFORM_PARAM_ID
           AND T.PA_PERFORM_APPRAISER_ID = PA.PA_PERFORM_APPRAISER_ID
           AND SP.PA_SECTION_ID = PDSP.PA_SECTION_ID
           AND SP.PA_PARAMETER_ID = PDSP.PA_PARAMETER_ID
           AND PDSP.PROMOTION ='Y'
           AND SP.PA_PERFORM_ID = PM.PA_PERFORM_ID) PROMOTION_RECOMENDATION,
       (SELECT LISTAGG(T.PA_VALUE,'-')
          FROM HRD.PA_PERFORM_VAL_TEXT      T,
               HRD.PA_PERFORM_SECTION_PARAM SP,
               HRD.PA_PERFORM_APPRAISER     PA,
                HRD.PA_DEF_SECTION_PARAMETER PDSP
         WHERE SP.PA_PERFORM_PARAM_ID = T.PA_PERFORM_PARAM_ID
           AND T.PA_PERFORM_APPRAISER_ID = PA.PA_PERFORM_APPRAISER_ID
           AND SP.PA_SECTION_ID = PDSP.PA_SECTION_ID
           AND SP.PA_PARAMETER_ID = PDSP.PA_PARAMETER_ID
           AND PDSP.HR_TRAINING ='Y'
           AND SP.PA_PERFORM_ID = PM.PA_PERFORM_ID) HR_TRAINING_RECOMENDATION,
       (SELECT LISTAGG(T.PA_VALUE,'-')
          FROM HRD.PA_PERFORM_VAL_TEXT      T,
               HRD.PA_PERFORM_SECTION_PARAM SP,
               HRD.PA_PERFORM_APPRAISER     PA,
                HRD.PA_DEF_SECTION_PARAMETER PDSP
         WHERE SP.PA_PERFORM_PARAM_ID = T.PA_PERFORM_PARAM_ID
           AND T.PA_PERFORM_APPRAISER_ID = PA.PA_PERFORM_APPRAISER_ID
           AND SP.PA_SECTION_ID = PDSP.PA_SECTION_ID
           AND SP.PA_PARAMETER_ID = PDSP.PA_PARAMETER_ID
           AND PDSP.DEPARTMENT_TRAINING ='Y'
           AND SP.PA_PERFORM_ID = PM.PA_PERFORM_ID) DEPARTMENT_TRAINING_RECOMEND,

       (SELECT LISTAGG('Appraiser:' ||
                       HIS.PKG_PATIENT.GET_PATIENT_NAME(AP.PA_APPRAISER_MRNO) || ':' ||
                       TO_CHAR(AP.REMARKS),
                       ' , ') WITHIN GROUP(ORDER BY TO_CHAR(AP.REMARKS)) AS SUBJECTS
          FROM HRD.PA_PERFORM_APPRAISER AP
         WHERE AP.PA_PERFORM_ID = PM.PA_PERFORM_ID
           AND AP.APPRAISER_ROLE IN ('R')) RECOMMEND_PERSON_REMARKS,
       (SELECT LISTAGG('Appraiser:' ||
                       HIS.PKG_PATIENT.GET_PATIENT_NAME(AP.PA_APPRAISER_MRNO) || ':' ||
                       TO_CHAR(AP.REMARKS),
                       ' , ') WITHIN GROUP(ORDER BY TO_CHAR(AP.REMARKS)) AS SUBJECTS
          FROM HRD.PA_PERFORM_APPRAISER AP
         WHERE AP.PA_PERFORM_ID = PM.PA_PERFORM_ID
           AND AP.APPRAISER_ROLE IN ('A')) APPROVAL_PERSON_REMARKS,
       (SELECT LISTAGG('Appraisee:' ||
                       HIS.PKG_PATIENT.GET_PATIENT_NAME(AP.PA_APPRAISER_MRNO) || ':' ||
                       TO_CHAR(AP.REMARKS),
                       ' , ') WITHIN GROUP(ORDER BY TO_CHAR(AP.REMARKS)) AS SUBJECTS
          FROM HRD.PA_PERFORM_APPRAISER AP
         WHERE AP.PA_PERFORM_ID = PM.PA_PERFORM_ID
           AND AP.APPRAISER_ROLE IN ('S')) APPRAISEE_REMARKS,

    H.DEPARTMENT_ID,
    H.PATP_ID

  FROM HRD.PA_HIERARCHY             H,
       HRD.PA_PERFORM_MASTER        PM,
       HRD.PA_PERFORM_APPRAISER     PA,
       HRD.PA_PERFORM_SECTION       PS,
       HRD.PA_PERFORM_SECTION_PARAM PSP,
       HRD.PA_DEF_SECTION           DS,
       HRD.PA_DEF_SECTION_PARAMETER SP,
       HRD.PA_PERFORM_VAL_RATING    PR,
       HRD.PA_DEF_RATING_VALUE      PV
 WHERE H.HIERARCHY_ID = PM.HIERARCHY_ID
   AND PM.PA_PERFORM_ID = PA.PA_PERFORM_ID
   AND PM.PA_PERFORM_ID = PS.PA_PERFORM_ID
   AND PS.PA_PERFORM_ID = PSP.PA_PERFORM_ID
   AND PS.PA_SECTION_ID = PSP.PA_SECTION_ID
   AND PSP.PA_SECTION_ID = DS.PA_SECTION_ID
   AND SP.PA_PARAMETER_ID = PSP.PA_PARAMETER_ID
   AND SP.PA_SECTION_ID = PSP.PA_SECTION_ID
      --  AND H.APPRAISEE_MRNO = '00160000004997'
   AND PSP.PA_PERFORM_PARAM_ID = PR.PA_PERFORM_PARAM_ID
   AND PR.PA_RATING_TYPE_ID = PV.PA_RATING_TYPE_ID
   AND PR.PA_RATING_VALUE_ID = PV.PA_RATING_VALUE_ID
   AND DS.PA_SECTION_TYPE = 'R'
   AND PA.PA_PERFORM_ID NOT IN
       (SELECT NVL(Q.PA_PERFORM_ID, PA.PA_PERFORM_ID)
          FROM HRD.VU_PA_PERFORM_QUEUE Q
         WHERE Q.PA_IN_QUEUE_OF_ROLE = 'S'
           AND Q.PA_PERFORM_ID = PM.PA_PERFORM_ID)
      --   AND H.PA_YEAR = '2022'
   AND PA.APPRAISER_ROLE = 'A'
   AND PA.PA_STATUS_ID = '214'
   AND HRD.PKG_PERFORMANCE_APPRAISAL
.F_GET_PA_QUEUE_HR(H.PATP_ID, H.APPRAISEE_MRNO) = 'Y'
AND H.PA_TYPE_ID = 1
--AND H.PATP_ID = 3
--- AND H.APPRAISEE_MRNO = '10060000003830'
---  AND H.PA_TEMPLATE_ID = 1
--   AND H.DEPARTMENT_ID = '0012700'
--- AND H
 GROUP BY H.PA_TEMPLATE_ID,
          PM.PA_PERFORM_ID,
          H.APPRAISEE_MRNO,
          HRD.PKG_PERFORMANCE_APPRAISAL.F_GET_PA_SCORE(H.PATP_ID,
                                                       H.APPRAISEE_MRNO),
          TO_CHAR(PA.REMARKS),
          H.DEPARTMENT_ID,
    H.PATP_ID
 ORDER BY H.APPRAISEE_MRNO
;
```

## HRD.V_EMP_TYPE_CONVERSION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_EMP_TYPE_CONVERSION AS
SELECT patient_type_id type_id,
       (SELECT description
          FROM definitions.patient_type
         WHERE patient_type_id = t.patient_type_id) type_desc,
       mrno original_mrno,
       start_date,
       end_date,
       mrno final_mrno,
       remarks
  FROM hrd.employee_type_history t;
```

## HRD.V_HINT_OBJECTS
```sql
create or replace force view hrd.v_hint_objects as
select O.SCHEMA_ID,
       S.NAME SCHEMA_NAME,
       O.OBJECT_CODE,
       OB.NAME OBJECT_NAME,
       O.DISPLAY_NAME,
       O.ACTIVE
 from HRD.HINT_OBJECTS O , DEFINITIONS.SCHEMAS S , DEFINITIONS.OBJECTS OB
 WHERE O.SCHEMA_ID = S.SCHEMA_ID
 AND O.OBJECT_CODE = OB.OBJECT_CODE;
```

## HRD.V_HOD_REPLACEMENT_EVENT
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_HOD_REPLACEMENT_EVENT AS
SELECT HRE.SR_NO HRE ,EVENT_DESCRIPTION, HRED.EVENT_DETIAL_DESC, HRED.TABLE_SOURCE, HRSV.SUB_EVENT_ID
  FROM HRD.HOD_REPLACEMENT_EVENT         HRE,
       HRD.HOD_REPLACEMENT_EVENT_DETAILS HRED,
       HRD.HOD_REPLACEMENT_SUB_EVENT_DET HRSV
 WHERE HRE.SR_NO = HRED.SR_NO
   AND HRED.SR_NO = HRSV.SR_NO
   AND HRED.DETIAL_SR_NO = HRSV.DETIAL_SR_NO
   AND HRE.SR_NO =2
ORDER BY HRE.SR_NO;
```

## HRD.V_HR_EMP_DOCUMENTS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_HR_EMP_DOCUMENTS AS
SELECT D.MRNO,
             D.DESCRIPTION,
             D.DOC_CATEGORY_ID,
             D.DOCUMENT_TYPE_ID,
             D.DOCUMENT_ID,
             'EMPLOYEE_DOCUMENTS' TABLE_SOURCE
        FROM HRD.EMPLOYEE_DOCUMENTS D
       WHERE D.Active = 'Y'

      /*******************************************/
      UNION
      SELECT ER.MRNO,
             ER.DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             ER.DOCUMENT_ID,
             'EMPLOYEE_REFRENCES' TABLE_SOURCE
        FROM HRD.EMPLOYEE_REFRENCES ER, LOB.DOCUMENTS_STORE L
       WHERE ER.DOCUMENT_ID = L.DOCUMENT_ID

      /*******************************************/
      UNION
      SELECT ER.MRNO,
             ER.DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             ER.DOCUMENT_ID,
             'EMPLOYEE_WORK_EXPERIENCE' TABLE_SOURCE
        FROM HRD.EMPLOYEE_WORK_EXPERIENCE ER, LOB.DOCUMENTS_STORE L
       WHERE ER.DOCUMENT_ID = L.DOCUMENT_ID
      /*******************************************/
      UNION
      SELECT I.MRNO,
             'Employee Ntional Identity Card' DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             I.DOCUMENT_ID,
             'INFORMATION' TABLE_SOURCE
        FROM HRD.INFORMATION I, LOB.DOCUMENTS_STORE L
       WHERE I.DOCUMENT_ID = L.DOCUMENT_ID

      /*******************************************/
      UNION
      SELECT S.MRNO,
             SP.DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             S.DOCUMENT_ID,
             'Employee_Study_History' TABLE_SOURCE
        FROM HRD.Employee_Study_History s,
             HRD.STUDY_PROGRAMS         SP,
             LOB.DOCUMENTS_STORE        L
       WHERE S.Document_Id = L.DOCUMENT_ID
         AND S.STUDY_PROGRAM_ID = SP.PROGRAM_ID

      /*******************************************/
      UNION
      SELECT S.MRNO,
             SP.DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             S.OSV_DOCUMENT_ID,
             'Employee_Study_History_OSV' TABLE_SOURCE
        FROM HRD.Employee_Study_History s,
             HRD.STUDY_PROGRAMS         SP,
             LOB.DOCUMENTS_STORE        L
       WHERE S.OSV_DOCUMENT_ID = L.DOCUMENT_ID
         AND S.STUDY_PROGRAM_ID = SP.PROGRAM_ID

      /*****************************************/
      UNION
      SELECT S.MRNO,
             SP.DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             S.DOCUMENT_ID,
             'Employee_Study_History_Detail' TABLE_SOURCE
        FROM HRD.Employee_Study_History_Detail s,
             HRD.EMPLOYEE_STUDY_HISTORY        SH,
             HRD.STUDY_PROGRAMS                SP,
             LOB.DOCUMENTS_STORE               L
       WHERE S.DOCUMENT_ID = L.DOCUMENT_ID
         AND S.STUDY_PROGRAM_ID = SP.PROGRAM_ID
         AND S.MRNO = SH.MRNO
         AND S.OSV_STATUS = SH.OSV_STATUS
         AND S.INSTITUTION_ID = SH.INSTITUTION_ID
         AND S.STUDY_TYPE_ID = SH.STUDY_TYPE_ID
         AND S.STUDY_PROGRAM_ID = SH.STUDY_PROGRAM_ID

      /*******************************************/
      UNION
      SELECT PR.EMPLOYEE_CODE,
             RT.DESCRIPTION || ', Reg # ' || PR.REGISTRATION_NUMBER ||
             ', OSV Status: ' || O.OSV_STATUS || ', Reg Date ' ||
             PR.REGISTRATION_DATE || ', Issue Date ' || PR.ISSUE_DATE ||
             ' ,Expiry Date ' || PR.EXPIRY_DATE || ' ' ||
             DECODE(PR.CURRENT_OSV, 'Y', '(Current)') DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             PR.DOCUMENT_ID,
             'PROFESSIONAL_REGISTRATIONS' TABLE_SOURCE
        FROM HRD.PROFESSIONAL_REGISTRATIONS PR,
             HRD.REGISTRATION_TYPE          RT,
             LOB.DOCUMENTS_STORE            L,
             DEFINITIONS.OSV_STATUS         O
       WHERE PR.Document_Id = L.DOCUMENT_ID
         AND PR.REGISTRATION_TYPE_ID = RT.REGISTRATION_TYPE_ID
           AND PR.OSV_STATUS = O.STATUS_ID

      /*******************************************/
      UNION
      SELECT PR.EMPLOYEE_CODE,
             RT.DESCRIPTION || ', Reg # ' || PR.REGISTRATION_NUMBER ||
             ', OSV Status: ' || O.OSV_STATUS || ', Reg Date ' ||
             PR.REGISTRATION_DATE || ', Issue Date ' || PR.ISSUE_DATE ||
             ' ,Expiry Date ' || PR.EXPIRY_DATE || ' ' ||
             DECODE(PR.CURRENT_OSV, 'Y', '(Current)') DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             PR.OSV_DOCUMENT_ID,
             'PROFESSIONAL_REGISTRATIONS_OSV' TABLE_SOURCE
        FROM HRD.PROFESSIONAL_REGISTRATIONS PR,
             HRD.REGISTRATION_TYPE          RT,
             LOB.DOCUMENTS_STORE            L,
             DEFINITIONS.OSV_STATUS         O
       WHERE PR.OSV_DOCUMENT_ID = L.DOCUMENT_ID
         AND PR.REGISTRATION_TYPE_ID = RT.REGISTRATION_TYPE_ID
         AND PR.OSV_STATUS = O.STATUS_ID

      /*******************************************/
      UNION
      SELECT R.EMPLOYEE_CODE,
             RT.DESCRIPTION || ', Reg # ' || R.REGISTRATION_NUMBER ||
             ', OSV Sent Date # ' || PR.OSV_SENT_DATE || ', OSV Status: ' ||
           O.OSV_STATUS || ', Reg Date ' || R.REGISTRATION_DATE ||
             ', Issue Date ' || R.ISSUE_DATE || ' ,Expiry Date ' ||
             PR.EXPIRY_DATE DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             PR.DOCUMENT_ID,
             'PROFESSIONAL_REGISTRATIONS_ISSUE' TABLE_SOURCE
        FROM HRD.PROFESSIONAL_REGISTRATIONS R,
             HRD.PROFESSIONAL_REGIS_HISTORY PR,
             HRD.REGISTRATION_TYPE          RT,
             LOB.DOCUMENTS_STORE            L,
             DEFINITIONS.OSV_STATUS         O
       WHERE PR.Document_Id = L.DOCUMENT_ID
         AND PR.REGISTRATION_TYPE_ID = R.REGISTRATION_TYPE_ID
         AND PR.OSV_STATUS_DET = O.STATUS_ID
         AND PR.EXPIRY_DATE = R.EXPIRY_DATE
         AND PR.OSV_STATUS = R.OSV_STATUS
         AND PR.REGISTRATION_TYPE_ID = RT.REGISTRATION_TYPE_ID

      /*******************************************/
      UNION
      SELECT ER.MRNO,
             NVL(ER.LEAVING_REASON, ER.REMARKS) || ' Leaving Date:' ||ER.LEAVING_DATE DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             ER.DOCUMENT_ID,
             'EMPLOYEE_RESIGNATION' TABLE_SOURCE
        FROM HRD.EMPLOYEE_RESIGNATION ER, LOB.DOCUMENTS_STORE L
       WHERE ER.DOCUMENT_ID = L.DOCUMENT_ID

      /*******************************************/
      UNION
      SELECT EC.MRNO,
             C.DESCRIPTION || '. From: ' || EC.START_DATE || ' - ' ||EC.END_DATE DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             EC.DOCUMENT_ID,
             'EMPLOYEE_CONTRACT_HISTORY' TABLE_SOURCE
        FROM HRD.EMPLOYEE_CONTRACT_HISTORY EC,
             HRD.CONTRACT_TYPE             C,
             LOB.DOCUMENTS_STORE           L
       WHERE EC.DOCUMENT_ID = L.DOCUMENT_ID
         AND EC.CONTRACT_ID = C.CONTRACT_TYPE_ID

      /*******************************************/
      UNION
      SELECT EJ.MRNO,
             D.DESCRIPTION || ' || ' || EJ.DESCRIPTION DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             EJ.DOCUMENT_ID,
             'EMPLOYEE_JDS' TABLE_SOURCE
        FROM HRD.EMPLOYEE_JDS        EJ,
             DEFINITIONS.DESIGNATION D,
             LOB.DOCUMENTS_STORE     L
       WHERE EJ.DOCUMENT_ID = L.DOCUMENT_ID
         AND EJ.DESIGNATION_ID = D.DESIGNATION_ID

      /*******************************************/
      UNION --HRD.EMPLOYEE_EVALUATION_ATTACHMENT
      SELECT EE.MRNO,
             ee.document_description DESCRIPTION,
             L.DOCUMENT_CATEGORY_ID,
             L.DOCUMENT_TYPE_ID,
             EE.DOCUMENT_ID,
             'EMPLOYEE_EVALUATION_HISTORY_PROB' TABLE_SOURCE
        FROM HRD.EMPLOYEE_EVALUATION_HISTORY    E,
             LOB.DOCUMENTS_STORE                L,
             HRD.EMPLOYEE_EVALUATION_ATTACHMENT EE
       WHERE EE.DOCUMENT_ID = L.DOCUMENT_ID
         AND E.MRNO = EE.MRNO
         AND E.START_DATE = EE.START_DATE
         AND E.EVALUATION_TYPE = EE.EVALUATION_TYPE
```

## HRD.V_JOB_APPLIED_USERS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_JOB_APPLIED_USERS AS
SELECT DISTINCT A.FIRST_NAME || ' ' || A.MIDDLE_NAME || ' ' || A.LAST_NAME APPLICANT_NAME,
                A.EMAIL_ID EMAIL,
                A.CNIC,
                TS.NAME CITY,
                jd.jd_title,
                JC.DESCRIPTION JOB_CATEGORY,
                JPQ.PUBLISH_DATE,
                JPQ.EXPIRY_DATE,
                JPQ.JD_ID,
                JPQ.CATEGORY_ID,
                TRUNC(JA.ENTRY_DATE) SUBMISSION_DATE,
                JPQ.DEPARTMENT_ID,
                JPQ.DESIGNATION_ID,
                A.SEX_ID,
                JD.LOCATION_ID,
                A.CV_PATH,
                JA.IS_CV_DOWNLOAD,
                JPQ.QUEUE_ID,
               AC.MOBILE_NUMBER
  FROM CCWEB.APPLICANT_INFO         A,
       CCWEB.APPLICANT_CONTACT_INFO AC,
       DEFINITIONS.TEHSIL           TS,
       HRD.JD_MASTER                JD,
       HRD.JOB_POSTING_QUEUE        JPQ,
       CCWEB.APPLICANT_JD_APPLIED   JA,
       HRD.JOB_CATEGORY             JC
 WHERE JPQ.JD_ID = JD.JD_ID
   AND UPPER(A.EMAIL_ID) = UPPER(JA.EMAIL_ID)
   AND UPPER(A.EMAIL_ID) = UPPER(AC.EMAIL_ID)
   AND JA.CATEGORY_ID = JPQ.CATEGORY_ID
   AND JA.JD_ID(+) = JPQ.JD_ID
   AND AC.COUNTRY = TS.COUNTRY_ID
   AND AC.STATE = TS.STATE_ID
   AND AC.CITY = TS.TEHSIL_ID
   AND AC.DISTRICT_ID = TS.DISTRICT_ID
   AND JC.CATEGORY_ID = JPQ.CATEGORY_ID
   AND TRUNC(JA.ENTRY_DATE) BETWEEN JPQ.PUBLISH_DATE AND
       NVL(JPQ.EXPIRY_DATE, SYSDATE)
 ORDER BY APPLICANT_NAME;
```

## HRD.V_JOB_CATEGORY_SHORTLIST
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_JOB_CATEGORY_SHORTLIST AS
SELECT DISTINCT V.CATEGORY_ID,
                JC.DESCRIPTION      AS JOB_CATEGORY,
                JPQ.JD_ID,
                JD.JD_TITLE,
                V.DEPARTMENT_ID,
                D.DESCRIPTION       AS DEPARTMENT,
                V.DESIGNATION_ID,
                DD.DESCRIPTION      AS DESIGNATION,
                V.HIRING_REQUEST_ID,
                V.POSITION_ID,
                JPQ.PUBLISH_DATE,
                JPQ.EXPIRY_DATE,
                V.QUEUE_ID
  FROM HRD.JD_SHORTLIST_CV V
  JOIN HRD.JOB_POSTING_QUEUE JPQ
    ON JPQ.QUEUE_ID = V.QUEUE_ID
   AND JPQ.CATEGORY_ID = V.CATEGORY_ID
   AND JPQ.JD_ID = V.JD_ID
  JOIN HRD.JD_MASTER JD
    ON JD.JD_ID = JPQ.JD_ID
  JOIN HRD.JOB_CATEGORY JC
    ON JC.CATEGORY_ID = JPQ.CATEGORY_ID
  JOIN DEFINITIONS.DEPARTMENT D
    ON D.DEPARTMENT_ID = V.DEPARTMENT_ID
  JOIN DEFINITIONS.DESIGNATION DD
    ON DD.DESIGNATION_ID = V.DESIGNATION_ID
 WHERE V.IS_REJECTED IS NULL
   AND V.IS_FORWARDED_TO_HR IS NULL
--- AND V.DEPARTMENT_ID ='0010100'
 ORDER BY V.CATEGORY_ID
;
```

## HRD.V_LOCATION_EMP_MENU
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_LOCATION_EMP_MENU AS
SELECT DISTINCT T1.LOV_ID,
       T2.LOCATION_ID,
       T2.LOCATION_DESC,
       T2.SHORT_DESC,
       T4.USERID USER_ID,
       T4.MRNO USER_MRNO,
       T4.FULL_NAME USER_NAME,
       T2.STATUS,
       T2.SHOW_IN_REPORTS,
       T2.ACTUAL_LOCATION,
       T2.ORDER_BY,
       T2.ZON_ID,
       T2.ORG_ID
  FROM SECURITY.LOVS_DETAIL T1,
       HRD.V_LOCATION T2,
       SECURITY.MEMBER      T3,
       SECURITY.USERS       T4
 WHERE T1.LOV_ID = '00172'
   AND (CASE WHEN T1.VALUE=SYS_CONTEXT('GLOBAL_CONTEXT','ORGANIZATION_ID') THEN T2.LOCATION_ID WHEN T2.ACTUAL_LOCATION='NO' THEN T2.LOCATION_ID ELSE T1.VALUE END) = T2.LOCATION_ID
   AND T1.GROUP_ID = T3.GROUPID
   AND T1.ACTIVE = 'Y'
   AND T3.USERID = T4.USERID
   AND T4.ACTIVE = 'Y'
   AND T4.MRNO= SYS_CONTEXT('GLOBAL_CONTEXT','USER_MRNO')
  /***********************************************************************************************
         PURPOSE: This View is used to list of Granted PITB EMPLOYEE MENU  MODULE WISE LOCATIONS
         RESULT: User wise Location
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
         1.0        10-JAN-2023  Muhammad Kamran             1. Created this View
  ************************************************************************************************/
;
```

## HRD.V_MONTH_WISE_EMP_LEAVE_SUMMARY
```sql
create or replace force view hrd.v_month_wise_emp_leave_summary as
select t.month,
       t.year_start,
       t.year_end,
       t.leave_type_id,
       t.mrno,
       t.current_year,
       t.last_year_balance,
       t.total_leaves,
       t.leave_availed,
       t.balance,
       t.no_carried_forward,
       T.LAPSED_LEAVES,
       T.ADJUSTED_LEAVES,
       t.transaction_date,
       hrd.f_get_department_id(t.mrno) department_id,
       hrd.f_get_department_name(t.mrno) department_name,
       hrd.f_get_department_location_id(hrd.f_get_department_id(t.mrno)) dept_loc_id,
       hrd.f_get_location_desc(hrd.f_get_department_location_id(hrd.f_get_department_id(t.mrno))) dept_loc_desc,
       his.pkg_patient.GET_PATIENT_NAME(t.mrno) employee_name

      -- hrd.f_get_location_id()
       from HRD.MONTH_WISE_EMP_LEAVE_SUMMARY t
;
```

## HRD.V_NEW_JOINERS_QUEUE_EHC
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_NEW_JOINERS_QUEUE_EHC AS
SELECT SUBSTR(EC.MRNO, -11) DISP_MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(I.MRNO) DISP_NAME,
       DECODE(HRD.PKG_COMMON.IS_REJOINER(I.MRNO),
              'N',
              HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE),
              (SELECT D.DESCRIPTION
                 FROM DEFINITIONS.DESIGNATION D
                WHERE D.DESIGNATION_ID = I.DESIGNATION_ID)) DESIGNATION,
       HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT,
       HIS.PKG_PATIENT.GET_CONTACT_NUMBER(I.MRNO) PHONE_NO,
       EC.MRNO MRNO,
       EC.JOINING_DATE,
       EC.GRADE_ID,
       (SELECT G.DESCRIPTION
          FROM DEFINITIONS.GRADES G
         WHERE G.GRADE_ID = EC.GRADE_ID) GRADE,
       EC.INITIAL_GROSS,
       EC.CONTRACT_START_DATE,
       EC.CONTRACT_END_DATE,
       EC.PROBATION_PERIOD,
       EC.NOTICE_PERIOD,
       EC.ACCEPTANCE_DAYS,
       EC.SALARY_RAISE_AFTER_PROBATION,
       EC.MEDICALLY_FIT,
       EC.ACTIVE,
       EC.IN_QUEUE_HR_SECTION_ID,
       EC.DESIGNATION_ID,
       EC.PATIENT_TYPE_ID,
       EC.ORIENTATION_DATE,
       EC.IS_JOINED,
       EC.CONTRACT_YEAR,
       (SELECT LOCATION_ID
          FROM DEFINITIONS.DEPARTMENT D
         WHERE D.DEPARTMENT_ID = I.DEPARTMENT_ID) LOCATION_ID,
       --  HRD.F_GET_EMPLOYEE_LOCATION(P_MRNO => P.MRNO) LOCATION_ID,
       EC.MEDICALLY_UNFIT_REMARKS,
       EC.INACTIVE_REMARKS,
       I.CONTRACT_TEMPLATE_ID,
       I.CONTRACT_CHANGE_REMARKS  REMARKS,
       EC.IS_ORIENTATION_DONE,
       EC.ACTUAL_ORIENTATION_DATE,
       EC.IS_EXPENSE_SUBMITTED,
       EC.FARWARD_TO_EHC,
       EC.EHC_BACK_TO_HR,
       I.PATIENT_MRNO,
       EC.MEDICAL_REMAKRS,
       HRD.PKG_NEW_JOINER.F_COLOR_VISION_IS_REQ(P.MRNO) COLOR_VISION_TEST_REQ,
       HRD.PKG_NEW_JOINER.F_AUDIOMETRY_IS_REQ(P.MRNO) AUDIOMETRY_REQ,
       HRD.PKG_NEW_JOINER .F_VISION_CHK_IS_REQ(P.MRNO) VISION_CHK_REQ,
       HRD.PKG_NEW_JOINER.F_HEARING_TEST_IS_REQ(P.MRNO) HEARING_TEST_REQ,
       EC.COLOR_VISION_TEST_RESULT,
       EC.AUDIOMETRY_TEST_RESULT,
       EC.VISION_CHK_RESULT,
       EC.HEARING_TEST,
       CASE
        WHEN HRD.PKG_NEW_JOINER.F_MEDICAL_REQUIRED(I.PATIENT_MRNO) = 'Y' THEN
            HRD.PKG_NEW_JOINER.F_GET_MEDICAL_DATE(I.PATIENT_MRNO)
        ELSE
            HRD.PKG_NEW_JOINER.F_GET_APPOINMENT_DATE(I.PATIENT_MRNO)
    END AS APPOINMENT_DATE,
       EC.EXTERNAL_REPORT_REVIEWED,
       EC.MEDICAL_RECORD_ACKNOWLEDGE,
       EC.EHC_ACKNOWLEDGE_BY ,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(EC.EHC_ACKNOWLEDGE_BY) EHC_ACKNOWLEDGE_NAME
  FROM HRD.INFORMATION         I,
       REGISTRATION.PATIENT    P,
       HRD.EMPLOYMENT_CONTRACT EC
WHERE P.MRNO = EC.MRNO
   AND I.MRNO = P.MRNO
   AND I.ACTIVE = 'Y'
   AND P.ACTIVE = 'Y'
   AND EC.FARWARD_TO_EHC = 'Y'
   AND EC.EHC_BACK_TO_HR = 'N'
   AND P.MRNO NOT LIKE '%DUM%'
ORDER BY P.MRNO
;
```

## HRD.V_NEW_JOINERS_QUEUE_HR
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_NEW_JOINERS_QUEUE_HR AS
SELECT SUBSTR(EC.MRNO, -11) DISP_MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(I.MRNO) DISP_NAME,
       DECODE(HRD.PKG_COMMON.IS_REJOINER(I.MRNO),
              'N',
              HRD.F_GET_DESIGNATION_DESC(I.MRNO, SYSDATE),
              (SELECT D.DESCRIPTION
                 FROM DEFINITIONS.DESIGNATION D
                WHERE D.DESIGNATION_ID = I.DESIGNATION_ID)) DESIGNATION,
       HRD.F_GET_DEPARTMENT_NAME(I.MRNO, SYSDATE) DEPARTMENT,
       HIS.PKG_PATIENT.GET_CONTACT_NUMBER(I.MRNO) PHONE_NO,
       EC.MRNO MRNO,
       EC.JOINING_DATE,
       EC.GRADE_ID,
       (SELECT G.DESCRIPTION
          FROM DEFINITIONS.GRADES G
         WHERE G.GRADE_ID = EC.GRADE_ID) GRADE,
       EC.INITIAL_GROSS,
       EC.CONTRACT_START_DATE,
       EC.CONTRACT_END_DATE,
       EC.PROBATION_PERIOD,
       EC.NOTICE_PERIOD,
       EC.ACCEPTANCE_DAYS,
       EC.SALARY_RAISE_AFTER_PROBATION,
       EC.MEDICALLY_FIT,
       EC.ACTIVE,
       EC.IN_QUEUE_HR_SECTION_ID,
       EC.DESIGNATION_ID,
       EC.PATIENT_TYPE_ID,
       EC.ORIENTATION_DATE,
       EC.IS_JOINED,
       EC.CONTRACT_YEAR,
       (SELECT LOCATION_ID
          FROM DEFINITIONS.DEPARTMENT D
         WHERE D.DEPARTMENT_ID = I.DEPARTMENT_ID) LOCATION_ID,
       --  HRD.F_GET_EMPLOYEE_LOCATION(P_MRNO => P.MRNO) LOCATION_ID,
       EC.MEDICALLY_UNFIT_REMARKS,
       EC.INACTIVE_REMARKS,
       I.CONTRACT_TEMPLATE_ID,
       I.CONTRACT_CHANGE_REMARKS  REMARKS,
       EC.IS_ORIENTATION_DONE,
       EC.ACTUAL_ORIENTATION_DATE,
       EC.IS_EXPENSE_SUBMITTED,
       EC.FARWARD_TO_EHC,
       EC.EHC_BACK_TO_HR,
       EC.HR_COMPLETE ,
       I.PATIENT_MRNO,
       EC.MEDICAL_REMAKRS,
       EC.EXTERNAL_REPORT_REVIEWED,
       EC.MEDICAL_RECORD_ACKNOWLEDGE,
       EC.EHC_ACKNOWLEDGE_BY ,
       CASE
        WHEN HRD.PKG_NEW_JOINER.F_MEDICAL_REQUIRED(I.PATIENT_MRNO) = 'Y' THEN
            HRD.PKG_NEW_JOINER.F_GET_MEDICAL_DATE(I.PATIENT_MRNO)
        ELSE
            HRD.PKG_NEW_JOINER.F_GET_APPOINMENT_DATE(I.PATIENT_MRNO)
    END AS APPOINMENT_DATE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(EC.EHC_ACKNOWLEDGE_BY) EHC_ACKNOWLEDGE_NAME
  FROM HRD.INFORMATION         I,
       REGISTRATION.PATIENT    P,
       HRD.EMPLOYMENT_CONTRACT EC
 WHERE P.MRNO = EC.MRNO
   AND I.MRNO = P.MRNO
   AND I.ACTIVE = 'Y'
   AND P.ACTIVE = 'Y'
 --  AND EC.FARWARD_TO_EHC = 'Y'
  -- AND EC.EHC_BACK_TO_HR = 'Y'
   AND EC.HR_COMPLETE = 'N'
   AND P.MRNO NOT LIKE '%DUM%'
 ORDER BY P.MRNO
;
```

## HRD.V_NURSING_SUPVISOR_SUMMARY
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_NURSING_SUPVISOR_SUMMARY AS
SELECT S.SUPERVISOR_MRNO,
       S.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(S.MRNO) EMP_NAME,
       S.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_NAME(S.MRNO)DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(S.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(S.MRNO) JOINING_DATE,
       S.ACCME,
       S.CURRENT_YEAR,
       S.CURRENT_MONTH_HOUR,
       S.MONTH_NAME,
       S.MONTH_START,
       S.MONTH_END,
       S.REMARKS,
       TO_DATE(TRIM(S.MONTH_NAME),'Month')MONTH_ORDER
        FROM
       HRD.NURSING_SUP_HIERARCHY_SUMMARY S;
```

## HRD.V_NURSING_SUP_HIERARCHY_DETAIL
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_NURSING_SUP_HIERARCHY_DETAIL AS
SELECT M.SUPERVISOR_MRNO,
       M.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(M.MRNO) EMP_NAME,
       M.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_NAME(M.MRNO)DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(M.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(M.MRNO) JOINING_DATE,
       M.ACTIVE
  FROM HRD.NURSING_SUP_HIERARCHY_DETAIL M;
```

## HRD.V_NURSING_SUP_HIERARCHY_MASTER
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_NURSING_SUP_HIERARCHY_MASTER AS
SELECT M.SUPERVISOR_MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(M.SUPERVISOR_MRNO) SUPERVISOR_NAME,
       M.DEPARTMENT_ID,
       HRD.F_GET_DEPARTMENT_NAME(M.SUPERVISOR_MRNO)DEPARTMENT,
       M.ACTIVE,
       HRD.F_GET_DESIGNATION_DESC(M.SUPERVISOR_MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(M.SUPERVISOR_MRNO) JOINING_DATE
  FROM HRD.NURSING_SUP_HIERARCHY_MASTER M;
```

## HRD.V_OPD_LOCATION_GRANT
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_OPD_LOCATION_GRANT AS
SELECT DISTINCT T1.LOV_ID,
       T2.LOCATION_ID,
       T2.LOCATION_DESC,
       T2.SHORT_DESC,
       T4.USERID USER_ID,
       T4.MRNO USER_MRNO,
       T4.FULL_NAME USER_NAME,
       T2.STATUS,
       T2.SHOW_IN_REPORTS,
       T2.ACTUAL_LOCATION,
       T2.ORDER_BY,
       T2.ZON_ID,
       T2.ORG_ID
  FROM SECURITY.LOVS_DETAIL T1,
       HRD.V_LOCATION T2,
       SECURITY.MEMBER      T3,
       SECURITY.USERS       T4
 WHERE T1.LOV_ID = '00086'
   AND (CASE WHEN T1.VALUE=SYS_CONTEXT('GLOBAL_CONTEXT','ORGANIZATION_ID') THEN T2.LOCATION_ID WHEN T2.ACTUAL_LOCATION='NO' THEN T2.LOCATION_ID ELSE T1.VALUE END) = T2.LOCATION_ID
   AND T1.GROUP_ID = T3.GROUPID
   AND T1.ACTIVE = 'Y'
   AND T3.USERID = T4.USERID
   AND T4.ACTIVE = 'Y'
   AND T4.MRNO= SYS_CONTEXT('GLOBAL_CONTEXT','USER_MRNO');
```

## HRD.V_PA_CONSULTANT_INDICATOR
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PA_CONSULTANT_INDICATOR AS
SELECT CI.MRNO, QI.PERF_INDICATOR, CI.INDICATOR_ID, CI.ACTIVE, CI.PATP_ID
  FROM HRD.PA_CONSULTANT_INDICATOR CI, HRD.PA_QA_INDICATOR QI
 WHERE CI.INDICATOR_ID = QI.PA_QA_PARAM_ID;
```

## HRD.V_PA_CPD
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PA_CPD AS
SELECT PA_REFERENCE_ID,
             PA_SERIAL_NO,
             PA_PERFORM_PARAM_ID,
             PA_PERFORM_ID,
             PA_TITLE,
             PA_NAME_OF_AUTHOR,
             PA_NAME_OF_JOURNAL,
             PA_DATE_YEAR,
             PA_PAGE_NUMBER_APPLICABLE,
             IRB_NO,
             IRB_EXEMPTED,
             IRB_REASON,
             STUDY_STATUS,
             PA_RESEARCH_DATE,
             EXAM_DATE,
             COMMENTS,
	     EXAM_NAME,
	     PMD,
	     STUDY_NAME,
	     ACTIVITY_NAME,
	     CREDIT_HOURS,
	     AUDIT_NAME,
	     NAME,
	     DESIGNATION,
	     GRANT_NAME,
	     AMOUNT,
	     ARTICLE_NAME,
             AMOUNT_IN_MILLION
        FROM HRD.PA_REFERENCE_RESEARCH_PAPER PRR
      -- WHERE PRR.PA_PERFORM_ID = P_PA_PERFORM_ID
     --  AND PRR.PA_PERFORM_PARAM_ID = P_PA_PERFORM_PARAM_ID
;
```

## HRD.V_PA_INDICATOR_FINAL_DATA
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PA_INDICATOR_FINAL_DATA AS
SELECT PD.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(PD.MRNO) Consultat_name,
       I.PERF_INDICATOR,
       PD.PA_PERFORM_ID,
       PD.PATPID,
       PD.INDICATOR_ID,
       PD.PA_SCORE,
       PD.PA_REF_DATA
        FROM HRD.PA_INDICATOR_FINAL_DATA PD, HRD.PA_QA_INDICATOR I
        WHERE PD.INDICATOR_ID = I.PA_QA_PARAM_ID;
```

## HRD.V_PA_PEER_LOV_DESIGNATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PA_PEER_LOV_DESIGNATION AS
SELECT D.DESIGNATION_CATEGORY_ID,
       HRD.PKG_HR_DOCUMENT_RECORD.F_GET_DESIG_CATEGORY(P_DESIG_CATEGORY_ID => D.DESIGNATION_CATEGORY_ID)DESIGNATION_CATEGORY,
       P.PA_SECTION_ID,
       P.PA_SECTION_NAME PA_SECTION,
       PA.PA_PARAMETER_ID,
       PA.PA_PARAMETER_NAME
  FROM HRD.PA_PEER_LOV_DESIGNATION  D,
       HRD.PA_DEF_SECTION           P,
       HRD.PA_DEF_SECTION_PARAMETER PA
 WHERE D.PA_SECTION_ID = P.PA_SECTION_ID
   AND D.PA_PARAMETER_ID = PA.PA_PARAMETER_ID
   AND P.PA_SECTION_ID = PA.PA_SECTION_ID;
```

## HRD.V_PERSON_ONCALL_SETUP
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PERSON_ONCALL_SETUP AS
SELECT S.SERIAL_NO,
       S.EMPLOYEE_CODE,
       S.LOCATION_ID,
       S.ACTIVE,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(S.EMPLOYEE_CODE) EMP_NAME,
       HRD.F_GET_DEPARTMENT_NAME(S.EMPLOYEE_CODE) DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(S.EMPLOYEE_CODE) DESIGNATION,
       HIS.PKG_PATIENT.GET_CONTACT_NUMBER(S.EMPLOYEE_CODE) CONTACT_NUMBER,
       HRD.F_GET_LOCATION_DESC(S.LOCATION_ID) LOCATION_DESC,
       S.AOC,
       s.roster_type_id,
       (SELECT OC.DESCRIPTION
       FROM HRD.ON_CALL_ROSTER_TYPE OC
       where oc.roster_type_id = s.roster_type_id
       and oc.location_id = SYS_CONTEXT('GLOBAL_CONTEXT','LOCATION_ID')
       ) roster_type_desc
FROM HRD.PERSON_ONCALL_SETUP S;
```

## HRD.V_PMDC_REGISTRATION_EXPIRED
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_PMDC_REGISTRATION_EXPIRED AS
SELECT PR.EMPLOYEE_CODE,
       PR.EMP_CODE,
       PR.NAME,
       PR.DEPARTMENT,
       PR.DESIGNATION,
       PR.REGISTRATION_TYPE,
       PR.REGISTRATION_NUMBER,
       PR.EXPIRY_DATE,
       PR.REGISTRATION_CATEGORY,
       PR.REGISTRATION_CATEGORY_ID,
       PR.REGISTRATION_DATE,
       PR.ENTRY_DATE,
       PR.ENTERED_BY,
       PR.VERIFICATION_BY,
       PR.VERIFICATION_DATE,
       PR.REMARKS,
       PR.DEFAULT_RECORD,
       PR.DEPARTMENT_ID,
       PR.DESIGNATION_ID,
       PR.ACTIVE,
       PR.JOINING_DATE,
       PR.LEAVING_DATE,
       PR.VERIFIED_BY,
       PR.ENTERED_BY_NAME,
       PR.PMDC_PNC_NO,
       PR.PMDC_PNC_DATE,
       PR.PATIENT_TYPE_ID,
       PR.REGISTRATION_TYPE_ID,
       PR.SUBMIT_SLIP,
       PR.SUBMIT_CERTIFICATE,
       PR.ISSUE_DATE,
       PR.SLIP_SUBMIT_DATE
  FROM HRD.PMDC_ALERT_QUEUE Q, HRD.VU_PROFESSIONAL_REGISTRATION PR
 WHERE PR.EMPLOYEE_CODE = Q.MRNO
   AND REGISTRATION_TYPE_ID = hrd.pkg_static_values.get_pmdc_reg_type_id;
```

## HRD.V_REFEREE_DETAIL
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_REFEREE_DETAIL AS
SELECT D.APPLICANT_ID,
                       D.PRIVILEGES_ID,
                       D.PRIVILEGES_DETAIL_ID,
                       D.SP_DESCRIPTION,
                       D.PRIVILEGE_TYPE,
                       D.IS_NUMBER_REQUIRED,
                       D.NUMBER_REQUIRED,
                       D.REQUESTED,
                       D.PERFORMED_PROCEDURE APPLICANT_PERFORMED_P,
                        D.BOLD,
                       D.ORDER_BY,
                       R.REFEREE_EMAIL,
       (SELECT RD.NO_PERFORMED_P
          FROM HRD.APP_CONSULTANT_REF_DTL RD
         WHERE RD.APPLICANT_ID = R.APPLICANT_ID
           AND RD.PRIVILEGE_ID = R.PRIVILEGE_ID
           AND RD.PRIVILEGES_DETAIL_ID = D.PRIVILEGES_DETAIL_ID
           AND RD.REFEREE_EMAIL = R.REFEREE_EMAIL
          ) REF_VERIFIED_PERFORMED,
       (SELECT RD.VERIFIED
          FROM HRD.APP_CONSULTANT_REF_DTL RD
         WHERE RD.APPLICANT_ID = R.APPLICANT_ID
           AND RD.PRIVILEGE_ID = R.PRIVILEGE_ID
           AND RD.PRIVILEGES_DETAIL_ID = D.PRIVILEGES_DETAIL_ID
           AND RD.REFEREE_EMAIL = R.REFEREE_EMAIL
          ) REF_VERIFIED,
           R.REF_COMMENTS AS REFREE_COMMENTS,
           d.heading
  FROM HRD.V_APPLICANT_PRIV_DETAIL D, HRD.APPLICANT_CONSULTANT_REF R
WHERE D.APPLICANT_ID = R.APPLICANT_ID
   AND D.PRIVILEGES_ID = R.PRIVILEGE_ID;
```

## HRD.V_REGISTRATION_EXPIRED
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_REGISTRATION_EXPIRED AS
SELECT PR.EMPLOYEE_CODE,
       PR.EMP_CODE,
       PR.NAME,
       PR.DEPARTMENT,
       PR.DESIGNATION,
       PR.REGISTRATION_TYPE,
       PR.REGISTRATION_NUMBER,
       PR.EXPIRY_DATE,
       PR.REGISTRATION_CATEGORY,
       PR.REGISTRATION_CATEGORY_ID,
       PR.REGISTRATION_DATE,
       PR.ENTRY_DATE,
       PR.ENTERED_BY,
       PR.VERIFICATION_BY,
       PR.VERIFICATION_DATE,
       PR.REMARKS,
       PR.DEFAULT_RECORD,
       PR.DEPARTMENT_ID,
       PR.DESIGNATION_ID,
       PR.ACTIVE,
       PR.JOINING_DATE,
       PR.LEAVING_DATE,
       PR.VERIFIED_BY,
       PR.ENTERED_BY_NAME,
       PR.PMDC_PNC_NO,
       PR.PMDC_PNC_DATE,
       PR.PATIENT_TYPE_ID,
       PR.REGISTRATION_TYPE_ID,
       PR.SUBMIT_SLIP,
       PR.SUBMIT_CERTIFICATE,
       PR.ISSUE_DATE,
       PR.SLIP_SUBMIT_DATE,
       PR.EMP_LOCATION_ID,
       PR.CURRENT_OSV,
       (SELECT DECODE(U.ACTIVE,'Y', 'Active','N','In-active') HIS_USER_STATUS FROM SECURITY.USERS U
       WHERE U.MRNO = PR.EMPLOYEE_CODE) HIS_USER_STATUS
  FROM HRD.EXPIRED_REGISTRATION_QUEUE Q, HRD.VU_PROFESSIONAL_REGISTRATION PR
 WHERE PR.EMPLOYEE_CODE = Q.MRNO
 and pr.REGISTRATION_TYPE_ID = q.registration_type_id;
```

## HRD.V_SAL_CAP_DESIGNATION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SAL_CAP_DESIGNATION AS
SELECT s.salary_cap_id, S.DESIGNATION_ID, D.DESCRIPTION, S.FROM_DATE, S.TO_DATE, S.ACTIVE, S.SALARY_CAP
  FROM HRD.SALARY_CAP_DESIGNATION S, DEFINITIONS.DESIGNATION D
 WHERE D.DESIGNATION_ID = S.DESIGNATION_ID;
```

## HRD.V_SERVICE_BOND_QUEUE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SERVICE_BOND_QUEUE AS
SELECT  DISTINCT(BQ.NOMINEES_MRNO),
       HIS.PKG_PATIENT.GET_PATIENT_NAME(BQ.NOMINEES_MRNO)  NAME,
       HRD.F_GET_DEPARTMENT_NAME(BQ.NOMINEES_MRNO) DEPARTMENT,
       HRD.F_GET_DEPARTMENT_ID(BQ.NOMINEES_MRNO) DEPARTMENT_ID,
       HRD.F_GET_DESIGNATION_DESC(BQ.NOMINEES_MRNO) DESIGNATION,
       HRD.F_GET_DESIGNATION_ID(BQ.NOMINEES_MRNO) DESIGNATION_ID,
       HRD.F_GET_JOINING_DATE(BQ.NOMINEES_MRNO) JOINING_DATE,
       BQ.IN_QUEUE_OF,
       BQ.IS_ACKNOWLEDGE,
       BQ.ACKNOWLEDGE_BY,
       BQ.ACKNOWLEDGE_DATE
        FROM HRD.SERVICE_BOND_QUEUE BQ;
```

## HRD.V_SERVICE_BOND_TRAINING
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SERVICE_BOND_TRAINING AS
SELECT ST.SR_NO,
        ST.TRAINING_ID,
        S.DESCRIPTION TRAINING_NAME,
        ST.START_DATE,
        ST.END_DATE,
        ST.TRAINING_FEES,
        ST.FEE_UNIT,
        ST.COUNTRY_ID,
        C.NAME COUNTRY,
        ST.REMARKS,
        ST.ACTIVE,
        ST.TRAINING_VENUE,
        ST.INSTITUTE,
        ST.STATUS,
        DECODE(ST.STATUS ,'D','Draft','P','Posted','W','With Draw')STATUS_DESC,
        ST.BOND_FEES,
        ST.BOND_FEE_UNIT
   FROM HRD.SERVICE_BOND_TRAINING ST , TRAINING.TRAINING_SUBJECT S, DEFINITIONS.COUNTRY C
WHERE ST.TRAINING_ID = S.SUBJECT_ID
AND ST.COUNTRY_ID = C.COUNTRY_ID;
```

## HRD.V_SPI_ALLOWANCE_DETAILS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SPI_ALLOWANCE_DETAILS AS
SELECT D.SR_NO,
       D.MRNO,
       HIS.PKG_PATIENT.GET_PATIENT_NAME(D.MRNO) NAME,
       HRD.F_GET_DEPARTMENT_NAME(D.MRNO)DEPARTMENT,
       HRD.F_GET_DESIGNATION_DESC(D.MRNO) DESIGNATION,
       HRD.F_GET_JOINING_DATE(D.MRNO) JOINING_DATE,
       D.INCENTIVE_START_DATE,
       D.LAST_INCENTIVE_DATE,
       D.REMARKS,
       D.ALLOWANCE_STATUS,
       D.EXEMPTION_REASON,
       D.INCENTIVE_GIVEN_BY,
       D.ALLOWANCES_ID,
       D.INCENTIVE_GIVEN_DATE,
       D.ALLOWANCE_AMOUNT FROM HRD.SPI_ALLOWANCE_DETAILS D;
```

## HRD.V_SPI_ALLOWANCE_MEMBERS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SPI_ALLOWANCE_MEMBERS AS
SELECT "ALLOWANCE_ID","MRNO"
  FROM (SELECT D.ALLOWANCE_ID, C.MRNO
          FROM HRD.SPI_ALLOWANCES_DEPARTMENTS D, HRD.CURRENT_EMPLOYEES C
         WHERE D.DEPARTMENT_ID = C.DEPARTMENT_ID
           AND D.ACTIVE = 'Y'
        UNION ALL
        SELECT SN.ALLOWANCE_ID, C.MRNO
          FROM HRD.SPI_ALLOWANCES_DEPT_NATURE SN,
               DEFINITIONS.DEPARTMENT         D,
               HRD.CURRENT_EMPLOYEES          C
         WHERE SN.DEPARTMENT_NATURE_ID = D.DEPARTMENT_NATURE_ID
           AND D.DEPARTMENT_ID = C.DEPARTMENT_ID
           AND SN.ACTIVE = 'Y'
        UNION ALL
        SELECT D.ALLOWANCE_ID, C.MRNO
          FROM HRD.SPI_ALLOWANCES_DESIGNATION D, HRD.CURRENT_EMPLOYEES C
         WHERE D.DESIGNATION_ID = HRD.F_GET_DESIGNATION_ID(C.MRNO)
           AND D.ACTIVE = 'Y'
        UNION ALL
        SELECT E.ALLOWANCE_ID, E.EMP_CODE MRNO
          FROM HRD.SPI_ALLOWANCES_EMPLOYEES E
         WHERE E.ACTIVE = 'Y') A
 WHERE A.MRNO NOT IN (SELECT EX.EMP_CODE
                        FROM HRD.SPI_ALLOWANCES_EMP_EXEMPT EX
                       WHERE EX.ALLOWANCE_ID = A.ALLOWANCE_ID
                         AND EX.EMP_CODE = A.MRNO);
```

## HRD.V_SPSSL_ATTENDANCE
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SPSSL_ATTENDANCE AS
SELECT substr(a.mrno, 4) attendee_mrno,
         a.mrno,
         his.pkg_patient.get_patient_name(a.mrno) attended_by,
         a.date_time,
         a.terminal,
         a.spss_lecture_id,
         a.submit_evaluation
    FROM hrd.spssl_attendance a;
```

## HRD.V_SPSS_LECTURES
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SPSS_LECTURES AS
SELECT l.spss_lecture_id,
       l.sps_subject_id,
       sub.description subject,
       l.lecture_title,
       l.active,
       l.lsd,
       l.lecture_start_date,
       l.led,
       l.lecture_end_date,
       l.lecture_instructor,
       pt.name instructor,
       l.location_id,
       l.order_location_id,
       ol.description class_room,
       l.remarks,
       l.lecture_credit_hours,
       l.cancelled_spss_lecture_id,
       (SELECT l.lsd
          FROM hrd.spss_lectures sp
         WHERE sp.spss_lecture_id = l.cancelled_spss_lecture_id) cancelled_start_date,
       (SELECT l.led
          FROM hrd.spss_lectures sp
         WHERE sp.spss_lecture_id = l.cancelled_spss_lecture_id) cancelled_end_date
  FROM hrd.spss_lectures          l,
       hrd.sps_subjects           s,
       hrd.study_subjects         sub,
       registration.patient       pt,
       definitions.order_location ol
 WHERE l.sps_subject_id = s.sps_subject_id
   AND s.subject_id = sub.subject_id
   AND l.lecture_instructor = pt.mrno(+)
   AND l.location_id = ol.location_id(+)
   AND l.order_location_id = ol.order_location_id(+);
```

## HRD.V_SPS_SUBJECTS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SPS_SUBJECTS AS
SELECT p.sps_subject_id,
       p.sp_session_id,
       p.subject_id,
       sub.description subject,
       p.subject_from_time,
       p.subject_to_time,
       p.day_id,
       d.description DAY,
       p.subject_instructor,
       his.pkg_patient.get_patient_name(p.subject_instructor) instructor,
       p.subject_credit_hours,
       p.lecture_duration
  FROM hrd.sps_subjects p, hrd.study_subjects sub, definitions.day d
 WHERE p.subject_id = sub.subject_id
   AND p.day_id = d.day_id(+);
```

## HRD.V_SP_SESSION
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_SP_SESSION AS
SELECT s.sp_session_id,
         s.program_id,
         sp.description study_program,
         s.session_start_date,
         s.session_end_date
    FROM hrd.sp_session s, hrd.study_programs sp
   WHERE s.program_id = sp.program_id;
```

## HRD.V_STUDY_PROGRAMS
```sql
CREATE OR REPLACE FORCE VIEW HRD.V_STUDY_PROGRAMS AS
SELECT sp.program_id,
         sp.description,
         sp.type_id,
         upper(st.description) study_type,
         sp.remarks,
         sp.active
    FROM hrd.study_programs sp, hrd.study_type st
   WHERE st.type_id = sp.type_id;
```

