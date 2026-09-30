# DEFINITIONS code objects

## Sequences
- DIS_FLWSH_DOC_ARC_SEQ
- DIS_FLWSH_TRANSACTIONS_SEQ
- HISCURRENCY_RATE_SEQ
- ICD_MAPPING_SEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- ISEQ
- OBJECT_PARAM_ID
- ONLINE_SURVEY_ANS_ID
- ONLINE_SURVEY_MASTER_SURVEY_ID
- ONLINE_SURVEY_QUEST_ID
- SEQ_APPLICATION_SETTINGS
- SEQ_CONT_FLAG_HISTORY
- SEQ_CPT_PRE_REQUISITES_ERRORS
- SEQ_DEF_PACKAGE
- SEQ_DOCTOR_HISTORY
- SEQ_ENTITY_TYPE
- SEQ_FILES_SERVERS_ID
- SEQ_SEARCH_HISTORY
- STATUSWISE_PTYPE_SEQ

## Packages (specifications)

### DEFINITIONS.DESCRIPTIONS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.DESCRIPTIONS AS

  PROCEDURE BLOOD_GROUP(P_BLOOD_GROUP_ID IN VARCHAR2,
                        P_DESCRIPTION    OUT VARCHAR2,
                        P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE DEPARTMENT(P_DEPARTMENT_ID IN VARCHAR2,
                       P_DESCRIPTION   OUT VARCHAR2,
                       P_ALERT_TEXT    OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE DESIGNATION(P_DESIGNATION_ID IN VARCHAR2,
                        P_DESCRIPTION    OUT VARCHAR2,
                        P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE DUTY_SHIFT(P_SHIFT_ID    IN HRD.SHIFT.SHIFT_ID%TYPE,
                       P_DESCRIPTION OUT HRD.SHIFT.DESCRIPTION%TYPE,
                       P_ALERT_TEXT  OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE GENDER(P_GENDER_ID   IN VARCHAR2,
                   P_DESCRIPTION OUT VARCHAR2,
                   P_ALERT_TEXT  OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE GEOGRAPHICAL_DATA(P_TEHSIL_ID   IN NUMBER,
                              P_DISTRICT_ID IN NUMBER,
                              P_STATE_ID    IN NUMBER,
                              P_COUNTRY_ID  IN NUMBER,
                              P_TEHSIL      OUT VARCHAR2,
                              P_DISTRICT    OUT VARCHAR2,
                              P_STATE       OUT VARCHAR2,
                              P_COUNTRY     OUT VARCHAR2,
                              P_ALERT_TEXT  OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE GRADE(P_GRADE_ID   IN VARCHAR2,
                  P_GRADE      OUT VARCHAR2,
                  P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE JOB_LEAVING_REASON(P_JOB_LEAVING_ID IN VARCHAR2,
                               P_JOB_LEAVING    OUT VARCHAR2,
                               P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE MARITAL_STATUS(P_MARITAL_STATUS_ID IN VARCHAR2,
                           P_DESCRIPTION       OUT VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE PATIENT_TYPE(P_PATIENT_TYPE_ID IN VARCHAR2,
                         P_DESCRIPTION     OUT VARCHAR2,
                         P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE RECEIVE_MEDIA(P_RECEIVE_MEDIA_ID   IN VARCHAR2,
                          P_RECEIVE_MEDIA_DESC OUT VARCHAR2,
                          P_ALERT_TEXT         OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE SOURCE_MEDIA(P_SOURCE_MEDIA_ID   IN VARCHAR2,
                         P_SOURCE_MEDIA_DESC OUT VARCHAR2,
                         P_ALERT_TEXT        OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE SOURCE_MEDIA_DETAIL(P_SOURCE_MEDIA_ID   IN VARCHAR2,
                                P_SERIAL_NO         IN NUMBER,
                                P_SOURCE_MEDIA_DESC OUT VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_INSTITUTE(P_INSTITUTE_ID   IN VARCHAR2,
                            P_INSTITUTE_DESC OUT VARCHAR2,
                            P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_PROGRAM(P_TYPE_ID      IN VARCHAR2,
                          P_PROGRAM_ID   IN VARCHAR2,
                          P_PROGRAM_DESC OUT VARCHAR2,
                          P_ALERT_TEXT   OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_SCALE(P_SCALE_ID   IN VARCHAR2,
                        P_SCALE_DESC OUT VARCHAR2,
                        P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_SCALE_VALUE(P_SCALE_ID       IN VARCHAR2,
                              P_SCALE_VALUE_ID IN VARCHAR2,
                              P_SCALE_VAL_DESC OUT VARCHAR2,
                              P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_SUBJECT(P_SUBJECT_ID   IN VARCHAR2,
                          P_SUBJECT_DESC OUT VARCHAR2,
                          P_ALERT_TEXT   OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  PROCEDURE STUDY_TYPE(P_TYPE_ID    IN VARCHAR2,
                       P_TYPE_DESC  OUT VARCHAR2,
                       P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------------
  /*******************************************************************************/
  -- Author  : MIRZA WASIM UDDIN(3875)
  -- Created : 26-05-2010
  -- Purpose : To GET THE DESCRIPTION OF COLOURS
  -- SCOPE   : VENTILATOR_FLOW_SHEET (VENTILATOR MGMT.)
  FUNCTION F_GET_COLOUR_DESCRIPTION(P_COLOUR_ID IN VARCHAR2) RETURN VARCHAR2;

  -------------------------------------------------------------------------------------
  /*******************************************************************************/
  -- Author  : HAYAT ULLAH(4862)
  -- Created : 09-01-2013
  -- Purpose : To GET THE DESCRIPTION OF CURRENCY
  -- SCOPE   :
  /*******************************************************************************/
  FUNCTION F_GET_CURRENCY_SHORT_DESC(P_CURRENCY_ID IN VARCHAR2)
    RETURN VARCHAR2;

  -------------------------------------------------------------------------------------
  /*******************************************************************************/
  -- Author  : NADIA OMER(3501)
  -- Created : 30-01-2013
  -- Purpose : To GET THE DESCRIPTION OF CPT
  -- SCOPE   :
  /*******************************************************************************/
  FUNCTION F_GET_CPT_DESCRIPTION(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.DESCRIPTION%TYPE;

  /*******************************************************************************/
  -- Author  : RAZA HASSAN(5782)
  -- Created : 27-11-2018
  -- Purpose : To GET THE PRICE OF CPT
  -- SCOPE   :
  /*******************************************************************************/
  FUNCTION F_GET_CPT_PRICE(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.PRICE%TYPE;

  /******************************************************************************/
  -- Author    : MIRZA WASIM UDDIN (3875)
  -- Created on: 12-MAR-2013
  -- Scope     : VACCINATION TYPES 
  -- Purpose   : The following function will return description of vaccination types
  /******************************************************************************/
  FUNCTION F_GET_DAY_DESC(P_DAY_ID IN DEFINITIONS.DAY.DAY_ID%TYPE)
    RETURN DEFINITIONS.DAY.DESCRIPTION%TYPE;

  /******************************************************************************/
  -- Author    : MIRZA WASIM UDDIN (3875)
  -- Created on: 05-APR-2013
  -- Scope     : SURGICAL INSTRUMENT TRAY SETS 
  -- Purpose   : The following function will return description of ITEMS
  /******************************************************************************/
  FUNCTION F_GET_ITEM_DESC(P_ITEM_ID IN ITEM.ITEM.ITEM_ID%TYPE)
    RETURN ITEM.ITEM.DESCRIPTION%TYPE;

  /******************************************************************************/
  -- Author    : ABRAR AHMED (5901)
  -- Created on: 11-APR-2013
  -- Scope     : CARDIOPULMONARY RESUSCITATION 
  -- Purpose   : The following function will return description of CPR DIAGNOSIS
  /******************************************************************************/
  FUNCTION F_GET_DIAGNOSIS_DESC(P_DIAGNOSIS_ID IN DEFINITIONS.DIAGNOSIS.DIAGNOSIS_ID%TYPE)
    RETURN DEFINITIONS.DIAGNOSIS.DESCRIPTION%TYPE;

  ---------------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 15-04-2013
  -- Scope     : NURSING.PKG_OP_NURSING_NOTES_MASTER 
  -- Purpose   : The following function will be used to fetch PATIENT_LOCATION_DESC.  
  FUNCTION F_GET_ORDER_LOCATION_DESC(P_LOCATION_ID       DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                                     P_ORDER_LOCATION_ID DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE)
    RETURN VARCHAR2;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : MIRZA WASIM (6-3875)
  -- Created on: 28-08-2014
  -- Scope     : ALL HIS 
  -- Purpose   : The following function will be used TO GET SHORT DESCRIPTION OF ORDER LOCATION..
  /******************************************************************************/
  FUNCTION F_GET_ORDER_LOC_SHORT_DESC(P_LOCATION_ID       DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                                      P_ORDER_LOCATION_ID DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE)
    RETURN VARCHAR2;

  /******************************************************************************/
  -- Author  : Nadia Omer (6 - 3501)
  -- Date    : 10-Feb-2014 10:21 AM  
  -- Purpose : This function will return description of the organization
  /******************************************************************************/
  FUNCTION F_GET_ORGANIZATION_DESC(P_ORGANIZATION_ID DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE)
    RETURN DEFINITIONS.ORGANIZATION.DESCRIPTION%TYPE;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author  : Nadia Omer (6 - 3501)
  -- Date    : 10-Feb-2014 12:55 PM  
  -- Purpose : This function will return name of the schema
  /******************************************************************************/
  FUNCTION F_GET_SCHEMA_NAME(P_SCHEMA_ID DEFINITIONS.SCHEMAS.SCHEMA_ID%TYPE)
    RETURN DEFINITIONS.SCHEMAS.NAME%TYPE;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author  : Nadia Omer (6 - 3501)
  -- Date    : 14-Feb-2014 12:55 PM  
  -- Purpose : This function will return name of the schema
  /******************************************************************************/
  FUNCTION F_GET_OBJECT_NAME(P_SCHEMA_ID      DEFINITIONS.OBJECTS.SCHEMA_ID%TYPE,
                             P_OBJECT_TYPE_ID DEFINITIONS.OBJECTS.OBJECT_TYPE_ID%TYPE,
                             P_OBJECT_ID      DEFINITIONS.OBJECTS.OBJECT_ID%TYPE)
    RETURN DEFINITIONS.OBJECTS.NAME%TYPE;

  --------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author  : Khizar Khalid (6020)
  -- Date    : 28-Nov-2014   
  -- Purpose : This function will return short description of the location
  /******************************************************************************/
  FUNCTION F_GET_LOC_SHORT_DESC(P_LOCATION_ID DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN DEFINITIONS.LOCATION.SHORT_DESC%TYPE;

  --------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author  : Khizar Khalid (6020)
  -- Date    : 30-Jan-2015   
  -- Purpose : This function will return description of the department
  /******************************************************************************/
  FUNCTION F_GET_DEPT_DESC(P_DEPARTMENT_ID DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE)
    RETURN DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE;

  --------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author  : Shahid Anwar
  -- Date    : 04-Aug-2015   
  -- Purpose : This function will return description of the order status
  /******************************************************************************/
  FUNCTION GET_ORDER_STATUS_DESC(P_ORDER_STATUS_ID IN ORDERENTRY.ORDER_STATUS.ORDER_STATUS_ID%TYPE)
    RETURN ORDERENTRY.ORDER_STATUS.DESCRIPTION%TYPE;

  /*******************************************************************************/
  -- Author  : SHUMAILA SHAHID(2870)
  -- Created : 07-01-2019
  -- Purpose : To extract the short CPT ID for the specified CPT
  -- SCOPE   : Surgery/Anesthesia
  /*******************************************************************************/
  FUNCTION F_GET_SHORT_CPT_ID(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN VARCHAR2;

END;
```

### DEFINITIONS.PKG_DOCTOR_NEW
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DOCTOR_NEW AS
  /*******FUNCTION FOR COUNT SCHEDULE VISIT********************************************************/

  /*************************************************************************************************************/
  ------------------------------------------------------------------------------------------------
  FUNCTION F_PATIENT_BOOKING(P_DOCTOR_ID IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE)
    RETURN NUMBER;

  /*************************************************************************************************************/
  FUNCTION F_NO_OF_ENCOUNTER(P_DOCTOR_ID IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE)
    RETURN NUMBER;
  /*************************************************************************************************************/
  FUNCTION F_CREATION_DATE(P_DOCTOR_ID IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE)
    RETURN DATE;
  /*************************************************************************************************************/
  FUNCTION F_CREATION_LOCATION(P_DOCTOR_ID IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE)
    RETURN VARCHAR2;
  /*************************************************************************************************************/
  FUNCTION F_GET_CLINIC_SPECIALITY(P_DOCTOR_ID           IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE,
                                   P_CLINIC_SPEIALITY_ID IN DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE)
    RETURN VARCHAR2;
  /*************************************************************************************************************/
  FUNCTION F_GET_COUNT_BEDS(P_DOCTOR_ID IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE)
    RETURN NUMBER;
  /*************************************************************************************************************/
  PROCEDURE P_CHECK_DOCTOR(P_DOCTOR_ID   IN DEFINITIONS.DOCTOR.DOCTOR_ID%TYPE,
                           P_DOCTOR_MRNO IN DEFINITIONS.DOCTOR.DOCTOR_MRNO %TYPE,
                           P_DR_SURNAME  IN DEFINITIONS.DOCTOR.DR_SURNAME%TYPE,
                           P_EVENT       IN CHAR, --- I FOR INSERT , U FOR UPDATE
                           P_STOP        OUT CHAR,
                           P_ALERT_TEXT  out VARCHAR2);

END;
```

### DEFINITIONS.APACHE_CALCULATOR_PKG
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.APACHE_CALCULATOR_PKG
AS
    -- Define a record type to hold the results
    TYPE ApacheResult_RT IS RECORD (
        apache_score        NUMBER,
        aps_score           NUMBER,
        predicted_mortality NUMBER,
        predicted_los       NUMBER
    );

    -- Define nested table types for the data arrays
    TYPE StringArray_T IS TABLE OF VARCHAR2(255);
    TYPE NestedStringArray_T IS TABLE OF StringArray_T;
    TYPE NumberArray_T IS TABLE OF NUMBER;
    TYPE NestedNumberArray_T IS TABLE OF NumberArray_T;

    -- Function to calculate APACHE IV scores
    FUNCTION APACHECALC (
        p_age           NUMBER,
        p_tem           NUMBER,
        p_map           NUMBER,
        p_hr            NUMBER,
        p_rr            NUMBER,
        p_fio           NUMBER,
        p_oxy           NUMBER,
        p_pco           NUMBER,
        p_pha           NUMBER,
        p_nas           NUMBER,
        p_ure           NUMBER,
        p_cre           NUMBER,
        p_uri           NUMBER,
        p_bsl           NUMBER,
        p_alb           NUMBER,
        p_bil           NUMBER,
        p_hto           NUMBER,
        p_wbc           NUMBER,
        p_gce           NUMBER,
        p_gcv           NUMBER,
        p_gcm           NUMBER,
        p_quo           NUMBER,
        p_patm          NUMBER,
        p_los           NUMBER,
        p_ori           NUMBER, -- 1: Non-Operative, 2: Emergency Operative, 3: Elective Operative
        p_rea           NUMBER, -- 1: Readmission, 0: Not Readmission
        p_eme           NUMBER, -- 1: Emergency, 0: Not Emergency
        p_thr           NUMBER, -- Number of Therapies
        p_typ_val       NUMBER, -- 1: Medical, 2: Surgical
        p_sys_idx       NUMBER,
        p_gno_idx       NUMBER,
        p_vent_mode     VARCHAR2, -- 'a': Not Ventilated, 'b': Ventilated
        p_crf_checked   BOOLEAN,
        p_sed_checked   BOOLEAN,
        p_aid_checked   BOOLEAN,
        p_hep_checked   BOOLEAN,
        p_lym_checked   BOOLEAN,
        p_met_checked   BOOLEAN,
        p_leu_checked   BOOLEAN,
        p_imm_checked   BOOLEAN,
        p_cir_checked   BOOLEAN
    ) RETURN ApacheResult_RT;

END APACHE_CALCULATOR_PKG;
```

### DEFINITIONS.APACHE_IV_ARRAYS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.apache_iv_arrays AS
    -- Arrays for diagnosis systems
    TYPE sys_array IS TABLE OF VARCHAR2(50);
    medsys_arr sys_array := sys_array(
        'System', 'Cardiovascular', 'Respiratory', 'Digestive', 'Neurologic', 
        'Metabolic', 'Hematologic', 'Genitourinary', 'Sepsis', 'Trauma', 'Miscellaneous'
    );
    chisys_arr sys_array := sys_array(
        'System', 'Cardiovascular', 'Respiratory', 'Digestive', 
        'Neurosurgery', 'Genitourinary', 'Trauma', 'Miscellaneous'
    );
    
    -- Arrays for diagnoses and coefficients
    TYPE dia_array IS TABLE OF VARCHAR2(100);
    TYPE dia_array_arr IS TABLE OF dia_array;
    TYPE coeff_array IS TABLE OF NUMBER;
    TYPE coeff_array_arr IS TABLE OF coeff_array;
    
    -- Medical diagnoses
    meddia_arr dia_array_arr := dia_array_arr(
        dia_array('Diagnosis'),
        dia_array('Diagnosis','AMI Ant','AMI Inf/Lat','AMI Non-Q','AMI Other','Cardiac Arrest','Cardiogenic Shock','Cardiomyopathy','Congestive HF','Chest Pain, rule out MI','Hypertension','Hypovolemia','Hemorrhage','Aortic Aneuysm','Peripheral Vascular Disease','Rythm Disturbance','Cardiac Drug Toxicity','Unstable Angina','Other'),
        dia_array('Diagnosis','Airway Obstruction','Asthma','Aspiration Pneumonia','Bacterial Pneumonia','Viral Pneumonia','Parasitic/Fungal Pneumonia','COPD','Pleural Effusion','Edema noncardiac','Embolism','Respiratory Arrest','Cancer (lung, ENT)','Restrictive Disease','Other'),
        dia_array('Diagnosis','Upper Bleeding','Lower Bleeding','Variceal Bleeding','Inflammatory Disease','Neoplasm','Obstruction','Perforation','Vascular Insufficiency','Hepatic Failure','Intra/Retroperitoneal Bleeding','Pancreatitis','Other'),
        dia_array('Diagnosis','Intracerebral Hemorrhage','Neoplasm','Infection','Neuromuscular Disease','Drug Overdose','Subdural/Epidural Hematoma','SAH, Aneurysm','Seizure','Stroke','Other'),
        dia_array('Diagnosis','Acid-base/Electrolyte Disorder','Diabetic Ketoacidosis','Hyperosmolar Diabetic Coma','Other'),
        dia_array('Diagnosis','Coagulopathy, Neutro-/Thrombocyto-/Pancytopenia','Other'),
        dia_array('Diagnosis','Renal/Other'),
        dia_array('Diagnosis','Cutaneous','Gastrointestinal','Pulmonary','Urinary','Other','Unknown'),
        dia_array('Diagnosis','Head with Chest/Abdomen/Pelvis/Spine','Head with Face/Extremity','Head only','Head with multi-trauma','Chest and Spine','Spine only','Multitrauma (no Head)'),
        dia_array('Diagnosis','General/Other')
    );
    
    -- Medical diagnosis coefficients (v)
    vmeddia_arr coeff_array_arr := coeff_array_arr(
        coeff_array(0),
        coeff_array(0,0.085768512,-0.036016015,-0.057916835,0,-0.751470488,0.329989886,0.557005388,-0.219091549,-0.520128136,-0.067961418,-0.389881468,-0.381155309,1.310621507,0.844326529,-0.302546395,-0.882634505,-0.368981979,-0.132883369),
        coeff_array(0,0.347148464,-0.542185912,0.860258427,1.306744601,1.156064757,1.619700546,-0.446092483,0.810093029,1.44275094,0.106834049,-0.053291846,-0.140474342,1.024903996,0.240490909),
        coeff_array(0,0.021360405,0.185696594,-0.083385343,0.532982522,1.336831287,2.06861446,2.208699567,1.944060834,0.194945835,0.165265635,2.762688675,0.556588745),
        coeff_array(0,0.86329482,0.974847187,1.16556532,3.92566043,-0.89006849,1.195315097,3.00860876,-0.330810671,0.313233793,0.357504381),
        coeff_array(0,-0.382017407,-0.58421484,-0.081962609,-0.363969853),
        coeff_array(0,0.399817416,-0.126173954),
        coeff_array(0,-0.152233731),
        coeff_array(0,1.56421957,1.245313673,1.926647999,0.453137242,0.649077107,0.402590257),
        coeff_array(0,2.128908172,0.860033343,0.834081141,3.637560295,2.574268317,2.168142671,1.521187936),
        coeff_array(0,-0.420843422)
    );
    
    -- Medical diagnosis coefficients (v2)
    v2meddia_arr coeff_array_arr := coeff_array_arr(
        coeff_array(0),
        coeff_array(0,0.102949765,-0.152525079,-0.270872458,0,0.416919141,0.239711427,0.059962444,-0.422587793,-1.122354572,-0.813921325,-0.622592285,-0.656757432,0.649149305,-0.502752032,-0.603060945,-0.690943246,-1.212730735,-0.369658509),
        coeff_array(0,-0.977669154,-1.540678498,-0.37223658,-0.043365914,0.254374904,1.056187347,-0.398697453,0.189900524,-0.2416873,-0.051527401,-0.390631425,0.966313802,1.55529658,-0.202823617),
        coeff_array(0,-0.551832894,-0.579471867,-0.527719358,-0.211771894,0.195130291,-0.369945003,-0.327171182,0.714879336,-0.119675791,-0.659544401,-0.513627563,-0.252586643),
        coeff_array(0,0.945056155,0.018952727,-0.535783229,-0.550653067,-1.55261952,0.295093901,0.615950385,-0.942170992,0.519453035,-0.176828697),
        coeff_array(0,-0.640575517,-1.775702142,-0.927156778,-0.986438209),
        coeff_array(0,0.258172435,-0.342352862),
        coeff_array(0,-0.54158014),
        coeff_array(0,0.126440315,-0.13010935,-0.258766455,-0.732788506,-0.04233671,-0.093377498),
        coeff_array(0,-0.372350315,-0.364128015,0.595869416,-0.067960926,-0.717432122,0.033769484,-0.678110274),
        coeff_array(0,-0.667576408)
    );
    
    -- Surgical diagnoses
    chidia_arr dia_array_arr := dia_array_arr(
        dia_array('Diagnosis'),
        dia_array('Diagnosis','Heart Valve','CABG with double/redo Valve','CABG with Single Valve','Aortic Aneurysm, Elective','Aortic Aneurysm, Ruptured','Aortic Aneurysm, Dissection','Femoro-popeliteal Bypass','Aorto-iliac/-femoral Bypass','Peripheral Ischemia','Carotid','Other'),
        dia_array('Diagnosis','Thoracotomy (Malignancy)','ENT Neoplasm','Thoracotomy (Lung biopy/Pleural Disease)','Thoracotomy (Infection)','Other'),
        dia_array('Diagnosis','Malignancy','Bleeding','Fistula/Abcess','Cholecystitis/Cholangitis','GI Inflammation','Obstruction','Perforation','Ischemia','Liver Transplant','Other'),
        dia_array('Diagnosis','Neoplasm (Craniotomy/Transphenoidal)','Intracranial Hemorrhage','SAH (Aneurysm/AVM)','Subdural/Epidural Hematoma','Spinal Cord Surgery','Other'),
        dia_array('Diagnosis','Neoplasm (Renal/Bladder/Prostate)','Renal Transplant','Hysterectomy','Other'),
        dia_array('Diagnosis','Head Only','Multitrauma with Head','Extremity','Multitrauma (no Head)'),
        dia_array('Diagnosis','Amputation (nontraumatic)')
    );
    
    -- Surgical diagnosis coefficients (v)
    vchidia_arr coeff_array_arr := coeff_array_arr(
        coeff_array(0),
        coeff_array(0,-2.076438218,-0.332456954,-1.358289429,0.773946463,2.77663888,1.110021457,-0.204188913,0.52392239,0.102293462,-0.14649332,-1.28358348),
        coeff_array(0,0.199925455,-0.053892181,0.185974867,0.044451048,-0.359443815),
        coeff_array(0,0.324865875,-0.045403893,0.719937797,-0.588512311,0.686936442,0.187304735,1.055374625,0.62069525,-0.848656603,0.217044719),
        coeff_array(0,0.319065119,2.949869569,2.599592539,1.342344962,-0.251392367,0.551331225),
        coeff_array(0,-0.423760975,-0.556650506,-0.162493249,-0.58901834),
        coeff_array(0,2.102182643,3.20631279,-0.481004907,1.485430308),
        coeff_array(0,-0.325703861)
    );
    
    -- Surgical diagnosis coefficients (v2)
    v2chidia_arr coeff_array_arr := coeff_array_arr(
        coeff_array(0),
        coeff_array(0,-1.371763972,-0.155141644,-1.99434806,-0.760703396,0.204404736,-0.178456475,-0.786571016,-0.831194514,-0.504208244,-1.332642438,-0.59044574),
        coeff_array(0,0.086933576,-1.152870135,0.405738008,-0.005937516,-0.249217228),
        coeff_array(0,0.136282662,-0.329679773,-0.556661177,-0.593293673,-0.165585527,-0.189005132,-0.189960264,0.498328014,-1.370278559,-0.295894316),
        coeff_array(0,-0.437737676,0.52671741,0.318905704,0.715682622,-0.628609547,0.003996339),
        coeff_array(0,-1.397212695,-1.308449407,-0.795847883,-0.693574061),
        coeff_array(0,1.088819324,0.357797735,-0.180386981,-0.377807998),
        coeff_array(0,0.604910303)
    );
END apache_iv_arrays;
```

### DEFINITIONS.PKG_ADMISSION_TYPE_CPT_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ADMISSION_TYPE_CPT_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : FIAZ AHMAD
  -- Created : 09-May-2017 11:25
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
  FUNCTION F_SELECT(P_ADMISSION_TYPE IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%TYPE,
                    P_CPT_ID         IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.ADMISSION_TYPE_CPT_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_ADMISSION_TYPE IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%TYPE,
                  P_CPT_ID         IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.ADMISSION_TYPE_CPT_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_ADMISSION_TYPE IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%TYPE,
                    P_CPT_ID         IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.ADMISSION_TYPE_CPT_SETUP%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_ADMISSION_TYPE IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%TYPE,
                    P_CPT_ID         IN DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_ADMISSION_TYPE_CPT_SETUP;
```

### DEFINITIONS.PKG_BEDS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_BEDS IS

  -- Author  : MISLAM
  -- Created : 28-Aug-09 9:07:09 AM
  -- Purpose : will use for insertion,updation and deletion data from definitions.beds

  /***********************************************************************************************

         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
         1.1        13-Jun-2023  Shahid Anwar            1. Change procedure parameters.

  ************************************************************************************************/

  FUNCTION F_SELECT(P_MRNO           IN DEFINITIONS.BEDS.MRNO%TYPE,
                    P_ROW            OUT DEFINITIONS.BEDS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_MRNO           IN DEFINITIONS.BEDS.MRNO%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.BEDS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_MRNO           IN DEFINITIONS.BEDS.MRNO%TYPE,
                    P_ROW            IN OUT DEFINITIONS.BEDS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_MRNO           IN DEFINITIONS.BEDS.MRNO%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  PROCEDURE INSERTION_IN_BED(P_MRNO              IN VARCHAR2,
                             P_BED_ID            IN VARCHAR2,
                             P_ORDER_TYPE_ID     IN VARCHAR2,
                             P_ORDER_NO          IN VARCHAR2,
                             P_LOCATION_ID       IN VARCHAR2,
                             P_ORDER_LOCATION_ID IN VARCHAR2,
                             P_ADMISSION_NO      IN VARCHAR2,
                             P_DOCTOR_ID         IN VARCHAR2,
                             P_USER_MRNO         IN VARCHAR2,
                             P_EVENT             IN VARCHAR2,
                             P_OBJECT_ID         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT VARCHAR2);

  -------------------------------------
  PROCEDURE UPDATION_IN_BED(P_MRNO_1           IN VARCHAR2,
                            P_MRNO_2           IN VARCHAR2,
                            P_BED_ID_1         IN VARCHAR2,
                            P_BED_ID_2         IN VARCHAR2,
                            P_DOCTOR_ID        IN VARCHAR2,
                            P_HOSPITALIST_MRNO IN VARCHAR2,
                            P_HOSPITALIST_NAME IN VARCHAR2,
                            P_USER_MRNO        IN VARCHAR2,
                            P_EVENT            IN VARCHAR2,
                            P_OBJECT_ID        IN VARCHAR2,
                            P_TERMINAL         IN VARCHAR2,
                            P_ALERT_TEXT       OUT VARCHAR2,
                            P_STOP             OUT VARCHAR2);

  --------------------------------------
  PROCEDURE DELETION_FROM_BED(P_MRNO       IN VARCHAR2,
                              P_USER_MRNO  IN VARCHAR2,
                              P_EVENT      IN VARCHAR2,
                              P_OBJECT_ID  IN VARCHAR2,
                              P_TERMINAL   IN VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2,
                              P_STOP       OUT VARCHAR2);

  ------------------------------------------
  FUNCTION GET_BED_LOCATION(P_BED_ID      IN VARCHAR2,
                            P_LOCATION_ID IN VARCHAR2) RETURN VARCHAR2;

  -------------------------------------------
  FUNCTION GET_PHARMACY_CLEARANCE(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  -------------------------------------------
  FUNCTION GET_NURSE_CLEARANCE(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

  -------------------------------------------
  PROCEDURE UPDATE_BEDS(P_MRNO        IN VARCHAR2,
                        P_DOCTOR_ID   IN VARCHAR2,
                        P_BED_ID      IN VARCHAR2,
                        P_USER_MRNO   IN VARCHAR2,
                        P_OBJECT_CODE IN VARCHAR2,
                        P_TERMINAL    IN VARCHAR2,
                        P_ALERT_TEXT  OUT VARCHAR2,
                        P_STOP        OUT VARCHAR2);
  -------------------------------------------
  PROCEDURE DELETE_FROM_BED(P_MRNO              IN VARCHAR2,
                            P_ADMISSION_NO      IN VARCHAR2,
                            P_ORDER_TYPE_ID     IN VARCHAR2 DEFAULT '005',
                            P_ORDER_NO          IN VARCHAR2 DEFAULT NULL,
                            P_LOCATION_ID       IN VARCHAR2 DEFAULT SYS_CONTEXT('GLOBAL_CONTEXT',
                                                                                'PHYSICAL_LOCATION_ID'),
                            P_ORDER_LOCATION_ID IN VARCHAR2 DEFAULT SYS_CONTEXT('GLOBAL_CONTEXT',
                                                                                'ORDER_LOCATION_ID'),
                            P_USER_MRNO         IN VARCHAR2 DEFAULT SECURITY.CURRENTUSER(SECURITY.GET_TERMINAL),
                            P_EVENT             IN VARCHAR2 DEFAULT NULL,
                            P_OBJECT_ID         IN VARCHAR2 DEFAULT NULL,
                            P_TERMINAL          IN VARCHAR2,
                            P_ALERT_TEXT        OUT VARCHAR2,
                            P_STOP              OUT VARCHAR2);

  TYPE R_BED IS RECORD(
    BED_ID            DEFINITIONS.BEDS.BED_ID%TYPE,
    ROOM_ID           DEFINITIONS.ROOMS.ROOM_ID%TYPE,
    ORDER_TYPE_ID     DEFINITIONS.BEDS.ORDER_TYPE_ID%TYPE,
    ORDER_NO          DEFINITIONS.BEDS.ORDER_NO%TYPE,
    LOCATION_ID       DEFINITIONS.BEDS.LOCATION_ID%TYPE,
    ORDER_LOCATION_ID DEFINITIONS.BEDS.ORDER_LOCATION_ID%TYPE,
    ADMISSION_FINAL   DEFINITIONS.BEDS.ADMISSION_FINAL%TYPE,
    ADMISSION_NO      DEFINITIONS.BEDS.ADMISSION_NO%TYPE,
    ADMISSION_DATE    DEFINITIONS.BEDS.ADMISSION_DATE%TYPE,
    ADMISSION_TYPE    DEFINITIONS.BEDS.ADMISSION_TYPE%TYPE,
    DOCTOR_ID         DEFINITIONS.BEDS.DOCTOR_ID%TYPE,
    BED_DESC          VARCHAR2(300));

  TYPE T_BED IS TABLE OF R_BED;
  FUNCTION GET_BED_INFO(P_MRNO IN VARCHAR2) RETURN T_BED
    PIPELINED;

  PROCEDURE BED_SWAP(P_MRNO_1ST    IN VARCHAR2,
                     P_MRNO_2ND    IN VARCHAR2,
                     P_USER_MRNO   IN VARCHAR2 DEFAULT SECURITY.CURRENTUSER(SECURITY.GET_TERMINAL),
                     P_EVENT       IN VARCHAR2 DEFAULT NULL,
                     P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL,
                     P_TERMINAL    IN VARCHAR2,
                     P_ALERT_TEXT  OUT VARCHAR2,
                     P_STOP        OUT VARCHAR2);

  PROCEDURE AHB_TO_IPD_BED_UPD(P_MRNO        IN VARCHAR2,
                               P_BED_ID      IN VARCHAR2,
                               P_LOCATION_ID IN VARCHAR2,
                               P_USER_MRNO   IN VARCHAR2,
                               P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL,
                               P_TERMINAL    IN VARCHAR2 DEFAULT NULL,
                               P_ALERT_TEXT  OUT VARCHAR2,
                               P_STOP        OUT VARCHAR2);

  PROCEDURE REVERT_BED_RESERVATION(P_MRNO        IN VARCHAR2,
                                   P_BED_ID      IN VARCHAR2,
                                   P_LOCATION_ID IN VARCHAR2,
                                   P_USER_MRNO   IN VARCHAR2,
                                   P_OBJECT_CODE IN VARCHAR2 DEFAULT NULL,
                                   P_TERMINAL    IN VARCHAR2 DEFAULT NULL,
                                   P_ALERT_TEXT  OUT VARCHAR2,
                                   P_STOP        OUT VARCHAR2);

END PKG_BEDS;
```

### DEFINITIONS.PKG_BUILDING_BLOCK
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_BUILDING_BLOCK IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 06:33
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
  FUNCTION F_SELECT(P_BUILDING_BLOCK_ID IN DEFINITIONS.BUILDING_BLOCK.BUILDING_BLOCK_ID%TYPE,
                    P_ROW               OUT DEFINITIONS.BUILDING_BLOCK%ROWTYPE,
                    P_IGNORE_NO_DATA    IN CHAR DEFAULT NULL,
                    P_LOCATION_ID       IN VARCHAR2,
                    P_CALLING_OBJECT    IN VARCHAR2,
                    P_CALLING_USER      IN VARCHAR2,
                    P_CALLING_EVENT     IN VARCHAR2,
                    P_ERROR             OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_BUILDING_BLOCK_ID IN DEFINITIONS.BUILDING_BLOCK.BUILDING_BLOCK_ID%TYPE,
                  P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID       IN VARCHAR2,
                  P_CALLING_OBJECT    IN VARCHAR2,
                  P_CALLING_USER      IN VARCHAR2,
                  P_CALLING_EVENT     IN VARCHAR2,
                  P_ROWID             OUT ROWID,
                  P_ERROR             OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.BUILDING_BLOCK%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_BUILDING_BLOCK_ID IN DEFINITIONS.BUILDING_BLOCK.BUILDING_BLOCK_ID%TYPE,
                    P_ROW               IN OUT DEFINITIONS.BUILDING_BLOCK%ROWTYPE,
                    P_UPDATE_NULL       IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID       IN VARCHAR2,
                    P_CALLING_OBJECT    IN VARCHAR2,
                    P_CALLING_USER      IN VARCHAR2,
                    P_CALLING_EVENT     IN VARCHAR2,
                    P_ERROR             OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_BUILDING_BLOCK_ID IN DEFINITIONS.BUILDING_BLOCK.BUILDING_BLOCK_ID%TYPE,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID       IN VARCHAR2,
                    P_CALLING_OBJECT    IN VARCHAR2,
                    P_CALLING_USER      IN VARCHAR2,
                    P_CALLING_EVENT     IN VARCHAR2,
                    P_ERROR             OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_BUILDING_BLOCK;
```

### DEFINITIONS.PKG_BUILDING_BLOCK_FLOORS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_BUILDING_BLOCK_FLOORS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 06:49 
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
  FUNCTION F_SELECT(P_BUILDING_BLOCK_FLOOR_ID IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_BLOCK_FLOOR_ID%TYPE,
                    P_BUILDING_FLOOR_ID       IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_FLOOR_ID%TYPE,
                    P_ROW                     OUT DEFINITIONS.BUILDING_BLOCK_FLOORS%ROWTYPE,
                    P_IGNORE_NO_DATA          IN CHAR DEFAULT NULL,
                    P_LOCATION_ID             IN VARCHAR2,
                    P_CALLING_OBJECT          IN VARCHAR2,
                    P_CALLING_USER            IN VARCHAR2,
                    P_CALLING_EVENT           IN VARCHAR2,
                    P_ERROR                   OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_BUILDING_BLOCK_FLOOR_ID IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_BLOCK_FLOOR_ID%TYPE,
                  P_BUILDING_FLOOR_ID       IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_FLOOR_ID%TYPE,
                  P_IGNORE_NO_DATA          IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID             IN VARCHAR2,
                  P_CALLING_OBJECT          IN VARCHAR2,
                  P_CALLING_USER            IN VARCHAR2,
                  P_CALLING_EVENT           IN VARCHAR2,
                  P_ROWID                   OUT ROWID,
                  P_ERROR                   OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.BUILDING_BLOCK_FLOORS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_BUILDING_BLOCK_FLOOR_ID IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_BLOCK_FLOOR_ID%TYPE,
                    P_BUILDING_FLOOR_ID       IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_FLOOR_ID%TYPE,
                    P_ROW                     IN OUT DEFINITIONS.BUILDING_BLOCK_FLOORS%ROWTYPE,
                    P_UPDATE_NULL             IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA          IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID             IN VARCHAR2,
                    P_CALLING_OBJECT          IN VARCHAR2,
                    P_CALLING_USER            IN VARCHAR2,
                    P_CALLING_EVENT           IN VARCHAR2,
                    P_ERROR                   OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_BUILDING_BLOCK_FLOOR_ID IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_BLOCK_FLOOR_ID%TYPE,
                    P_BUILDING_FLOOR_ID       IN DEFINITIONS.BUILDING_BLOCK_FLOORS.BUILDING_FLOOR_ID%TYPE,
                    P_IGNORE_NO_DATA          IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID             IN VARCHAR2,
                    P_CALLING_OBJECT          IN VARCHAR2,
                    P_CALLING_USER            IN VARCHAR2,
                    P_CALLING_EVENT           IN VARCHAR2,
                    P_ERROR                   OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_BUILDING_BLOCK_FLOORS;
```

### DEFINITIONS.PKG_BUILDING_FLOOR
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_BUILDING_FLOOR IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 07:09  
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
 FUNCTION F_SELECT(P_BUILDING_FLOOR_ID IN DEFINITIONS.BUILDING_FLOOR.BUILDING_FLOOR_ID%TYPE,
                                        P_ROW  OUT DEFINITIONS.BUILDING_FLOOR%ROWTYPE,
                                        P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
     FUNCTION F_LOCK(P_BUILDING_FLOOR_ID IN DEFINITIONS.BUILDING_FLOOR.BUILDING_FLOOR_ID%TYPE,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ROWID          OUT ROWID,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_INSERT(P_ROW IN OUT DEFINITIONS.BUILDING_FLOOR%ROWTYPE,
                                        P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                                        P_LOCATION_ID      IN VARCHAR2,
                                        P_CALLING_OBJECT   IN VARCHAR2,
                                        P_CALLING_USER     IN VARCHAR2,
                                        P_CALLING_EVENT    IN VARCHAR2,
                                        P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_UPDATE(P_BUILDING_FLOOR_ID IN DEFINITIONS.BUILDING_FLOOR.BUILDING_FLOOR_ID%TYPE,
                                        P_ROW IN OUT DEFINITIONS.BUILDING_FLOOR%ROWTYPE,
                                        P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_DELETE(P_BUILDING_FLOOR_ID IN DEFINITIONS.BUILDING_FLOOR.BUILDING_FLOOR_ID%TYPE,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
END PKG_BUILDING_FLOOR;
```

### DEFINITIONS.PKG_CLINIC_BOOKING_SPECS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CLINIC_BOOKING_SPECS AS

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : The following record type, table types will be used
  --             for dml of REGISTRATION.CLINIC
  /******************************************************************************/

  TYPE BOOKING_SPECS_REC IS RECORD(
    CLINIC_ID REGISTRATION.CLINIC.CLINIC_ID%TYPE,
    NAME      REGISTRATION.CLINIC.NAME%TYPE);

  TYPE CLINICS_TBL IS TABLE OF BOOKING_SPECS_REC INDEX BY PLS_INTEGER;
  TYPE CLINICS_TBL_PF IS TABLE OF BOOKING_SPECS_REC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : The following record type, table types will be used
  --             for QUERY of REGISTRATION.CLINIC_BOOKING_SPECS
  /******************************************************************************/
  TYPE BOOKING_SPECS_RCC IS RECORD(
    clinic_id       REGISTRATION.CLINIC_BOOKING_SPECS.clinic_id%TYPE,
    day_id          REGISTRATION.CLINIC_BOOKING_SPECS.day_id%TYPE,
    day_desc        DEFINITIONS.DAY.DESCRIPTION%TYPE,
    specs_morning   REGISTRATION.CLINIC_BOOKING_SPECS.specs_morning%TYPE,
    specs_afternoon REGISTRATION.CLINIC_BOOKING_SPECS.specs_afternoon %TYPE,
    specs_evening   REGISTRATION.CLINIC_BOOKING_SPECS.specs_evening %TYPE,
    ACTIVE          REGISTRATION.CLINIC_BOOKING_SPECS.ACTIVE%TYPE);

  TYPE BOOKING_SPECS_TLL IS TABLE OF BOOKING_SPECS_RCC INDEX BY PLS_INTEGER;
  TYPE BOOKING_SPECS_TLL_PF IS TABLE OF BOOKING_SPECS_RCC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : The following record type, table types will be used
  --             for dml of REGISTRATION.CLINIC_BOOKING_SPECS
  /******************************************************************************/
  TYPE BOOKING_SPECS_RC IS RECORD(
    clinic_id REGISTRATION.CLINIC_BOOKING_SPECS.clinic_id%TYPE,
    day_id    REGISTRATION.CLINIC_BOOKING_SPECS.day_id%TYPE,
    -- day_desc        DEFINITIONS.DAY.DESCRIPTION%TYPE,
    specs_morning   REGISTRATION.CLINIC_BOOKING_SPECS.specs_morning%TYPE,
    specs_afternoon REGISTRATION.CLINIC_BOOKING_SPECS.specs_afternoon %TYPE,
    specs_evening   REGISTRATION.CLINIC_BOOKING_SPECS.specs_evening %TYPE,
    ACTIVE          REGISTRATION.CLINIC_BOOKING_SPECS.ACTIVE%TYPE);

  TYPE BOOKING_SPECS_TL IS TABLE OF BOOKING_SPECS_RC INDEX BY PLS_INTEGER;
  TYPE BOOKING_SPECS_TL_PF IS TABLE OF BOOKING_SPECS_RC; /* FOR PIPLINED FUNCTION */

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : The following pipelined function will return table of records
  --             REGISTRATION.CLINIC.
  /******************************************************************************/

  FUNCTION F_CLINICS_QRY(P_CLINIC_ID IN REGISTRATION.CLINIC.CLINIC_ID%TYPE,
                         P_NAME      IN REGISTRATION.CLINIC.NAME%TYPE)
    RETURN CLINICS_TBL_PF
    PIPELINED;

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for querying data of
  --             REGISTRATION.CLINIC.
  /******************************************************************************/

  PROCEDURE P_CLINICS_QRY(P_CLINIC_ID  IN REGISTRATION.CLINIC.CLINIC_ID%TYPE,
                          P_NAME       IN REGISTRATION.CLINIC.NAME%TYPE,
                          P_DATA       IN OUT CLINICS_TBL,
                          P_STOP       OUT VARCHAR2,
                          P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for locking data of
  --             REGISTRATION.CLINIC.
  /******************************************************************************/

  PROCEDURE P_CLINICS_LCK(P_DATA       IN OUT CLINICS_TBL,
                          P_STOP       OUT VARCHAR2,
                          P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : REGISTRATION.CLINIC_BOOKING_SPECS
  -- Purpose   : The following pipelined function will return table of records
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  FUNCTION F_BOOKING_SPECS_QY(P_CLINIC_ID       IN REGISTRATION.CLINIC_BOOKING_SPECS.CLINIC_ID%TYPE,
                              P_DAY_ID          IN REGISTRATION.CLINIC_BOOKING_SPECS.DAY_ID%TYPE,
                              P_DAY             IN DEFINITIONS.DAY.DESCRIPTION%TYPE,
                              P_SPECS_MORNING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_MORNING%TYPE,
                              P_SPECS_AFTERNOON IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_AFTERNOON%TYPE,
                              P_SPECS_EVENING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_EVENING%TYPE,
                              
                              P_ACTIVE IN REGISTRATION.CLINIC_BOOKING_SPECS.ACTIVE%TYPE)
    RETURN BOOKING_SPECS_TLL_PF
    PIPELINED;

  PROCEDURE P_BOOKING_SPECS_QY(P_CLINIC_ID       IN REGISTRATION.CLINIC_BOOKING_SPECS.CLINIC_ID%TYPE,
                               P_DAY_ID          IN REGISTRATION.CLINIC_BOOKING_SPECS.DAY_ID%TYPE,
                               P_DAY             IN DEFINITIONS.DAY.DESCRIPTION%TYPE,
                               P_SPECS_MORNING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_MORNING%TYPE,
                               P_SPECS_AFTERNOON IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_AFTERNOON%TYPE,
                               P_SPECS_EVENING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_EVENING%TYPE,
                               
                               P_ACTIVE     IN REGISTRATION.CLINIC_BOOKING_SPECS.ACTIVE%TYPE,
                               P_DATA       IN OUT BOOKING_SPECS_TLL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for checking data validations of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                                P_DATA            IN BOOKING_SPECS_RCC,
                                P_STOP            OUT VARCHAR2,
                                P_ALERT_TEXT      OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for inserting data in
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_INS(P_CLINIC_ID  OUT REGISTRATION.CLINIC_BOOKING_SPECS.CLINIC_ID%TYPE,
                                P_DAY_ID     OUT REGISTRATION.CLINIC_BOOKING_SPECS.DAY_ID%TYPE,
                                P_DATA       IN OUT BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for locking data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_LCK(P_DATA       IN OUT BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for updating data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_UPD(P_DATA       IN OUT BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : ASMA HASHMI (4806)
  -- Created on: 14-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for deleting data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_DEL(P_DATA       IN OUT BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

END PKG_CLINIC_BOOKING_SPECS;
```

### DEFINITIONS.PKG_COMMON
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_COMMON AS

  --function created by m.abbas on 08.09.2014
  --purpose: it will return constant value for given constant id
  --if constant level is for organization, it will look only at organization column, otherwise at locatoin column
  --if any error or exception occurs, it will return default value given by user
  --if value is to ve calculated at run time then it execute backend source to get that value
  FUNCTION GET_CONSTANT_VALUE(P_CONSTANT_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.CONSTANT_ID%TYPE,
                              P_ORGANIZATION_ID IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.LOCATION_ID%TYPE,
                              P_DEFAULT_VAL     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE)
    RETURN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE;
  ---
  FUNCTION get_constant_value(P_CONSTANT_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.CONSTANT_ID%TYPE,
                              P_MRNO            IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP_USER.MRNO%TYPE,
                              P_ORGANIZATION_ID IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.ORGANIZATION_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.LOCATION_ID%TYPE,
                              P_DEFAULT_VAL     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE)
    RETURN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE;

  PROCEDURE GET_CONSTANT_VALUE(P_CONSTANT_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.CONSTANT_ID%TYPE,
                               P_ORGANIZATION_ID IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.ORGANIZATION_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.LOCATION_ID%TYPE,
                               P_DEFAULT_VAL     IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE,
                               P_OBJECT_CODE     IN VARCHAR2,
                               P_USERNAME        IN VARCHAR2,
                               P_TERMINAL        IN VARCHAR2,
                               P_SESSION_ID      IN VARCHAR2,
                               P_EVENT           IN VARCHAR2,
                               P_PROCESS_ID      IN VARCHAR2,
                               P_VALUE           OUT DEFINITIONS.SYSTEM_CONSTANTS_SETUP.VALUE%TYPE,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);
  FUNCTION GET_ORGANIZATION_DESC(P_ORGANIZATION_ID IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE)
    RETURN DEFINITIONS.ORGANIZATION.DESCRIPTION%TYPE;
  --it return currrency description
  -- C --> complete S --> Short
  FUNCTION GET_CURRENCY_DESC(P_CURRENCY_ID IN DEFINITIONS.CURRENCY.CURRENCY_ID%TYPE,
                             P_TYPE        IN VARCHAR2 DEFAULT 'C')
    RETURN DEFINITIONS.CURRENCY.DESCRIPTION%TYPE;
  /********************************************************************/
  FUNCTION GET_IS_FOOD_COUPON_ALLOW(P_PATIENT_TYPE_ID   DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                                    P_LOGIN_LOCATION_ID DEFINITIONS.PATIENT_TYPE.LOCATION_ID%TYPE)
    RETURN CHAR;
  /*********************************************************/

  FUNCTION F_GET_DIVISION_HEAD_MRNO(P_DIVISIONS_CODE DEFINITIONS.DIVISIONS.DIVISION_ID%TYPE,
                                    P_LOCATION_ID    DEFINITIONS.GL_DIVISION_LOC_HEADS.LOCATION_ID%TYPE)
    RETURN VARCHAR2;

  /********************************************************/
  -------------------------------------------------------------------------------------
  --MUHAMMAD YASAR NASEER
  --30-JUL-2015 AM 10:28
  --THIS FUNCTION WILL RETURN PATIENT CURRENT STATUS AGAINST SERVICE ID OF LOU PATIENT.
  FUNCTION GET_CLEARANCE_STATUS_ID(P_SERVICE_ID DEFINITIONS.LOU_SERVICES_SETUP.SERVICE_ID%TYPE)
    RETURN DEFINITIONS.LOU_SERVICES_SETUP.CLEARANCE_STATUS_ID%TYPE;

  /************************************************************/
  --------------------------------------------------------------------------------------
  --Muhammad Usman Tahir
  --08-MAR-2016 PM 3:32
  --THIS FUNCTION WILL RETURN PACKAGE SHORT DESC.
  FUNCTION GET_PACKAGE_SHORT_DESC(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGES.SHORT_DESC%TYPE;
  /***********************************************************/
  --------------------------------------------------------------------------------------
  --MUHAMMAD USMAN TAHIR
  --08-MAR-2016 PM 3:40
  --THIS FUNCTION WILL RETURN PACKAGE DESC.
  FUNCTION GET_PACKAGE_DESC(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGES.DESCRIPTION%TYPE;
  /***********************************************************/
  --------------------------------------------------------------------------------------
  --SHAHZAD
  --30-MAR-2016 
  FUNCTION GET_PARENT_LOCATION_ID(P_SUB_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN DEFINITIONS.LOCATION.LOCATION_ID%TYPE;
-----
    FUNCTION GET_UNIT_VALUE(P_UNIT_ID IN NUMBER) RETURN NUMBER;
END;
```

### DEFINITIONS.PKG_CPT
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT IS

  -- Author  : ASAEED
  -- Created : 3/15/2011 10:42:02 AM
  -- Purpose : a general purpose Package for CPT related information
  -- Public function and procedure declarations
  --/*--------------------------------*/--
  FUNCTION GET_CPT_DEPARTMENT_ID(P_CPT_ID DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN VARCHAR2;

  --/*--------------------------------*/--
  FUNCTION GET_CPT_SECTION_ID(P_CPT_ID DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN VARCHAR2;

  --/*--------------------------------*/--
  -- ===================================================================== --
  FUNCTION CPT_ALLOW(P_CHECK_TYPE_ID  IN VARCHAR2,
                     P_CPT_ID         IN VARCHAR2,
                     P_LOCATION_ID    IN VARCHAR2,
                     P_PATIENT_MRNO   IN VARCHAR2,
                     P_ORDER_TYPE_ID  IN VARCHAR2,
                     P_CALLING_OBJECT IN VARCHAR2,
                     P_CALLING_USER   IN VARCHAR2,
                     P_CALLING_EVENT  IN VARCHAR2,
                     P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ===================================================================== --
  FUNCTION CHK_ORDER_ENTRY(P_CPT_ID         IN VARCHAR2,
                           P_LOCATION_ID    IN VARCHAR2,
                           P_PATIENT_MRNO   IN VARCHAR2,
                           P_ORDER_TYPE_ID  IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ===================================================================== --
  ---------------------------------------------------
  -- This Function will return the CPT description --
  ---------------------------------------------------
  FUNCTION GET_CPT_NAME(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.DESCRIPTION%TYPE;

  ----------------------------------------------
  -- This Function will return the Open Price --
  ----------------------------------------------
  FUNCTION GET_OPEN_PRICE(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.OPEN_PRICE%TYPE;

  -------------------------------------------------
  -- This Function will return the Open Quantity --
  -------------------------------------------------
  FUNCTION GET_OPEN_QUANTITY(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.OPEN_QUANTITY%TYPE;

  ---------------------------------------------------
  -- This Function will return the Doctor Required --
  ---------------------------------------------------
  FUNCTION GET_DOCTOR_REQUIRED(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.DOCTOR_REQUIRED%TYPE;

  -------------------------------------------------------------
  -- This function will return DEPARTMENT NATURE DESCRIPTION --
  -------------------------------------------------------------
  FUNCTION GET_DEPARTMENT_NATURE(P_ORGANIZATION_ID      IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE)
    RETURN DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE;

  --------------------------------------------------------------------
  -- This function will return DEPARTMENT NATURE DETAIL DESCRIPTION --
  --------------------------------------------------------------------
  FUNCTION GET_DEPARTMENT_NATURE_DETAIL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                        P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_NATURE_ID         IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_ID%TYPE,
                                        P_NATURE_DETAIL_ID  IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE)
    RETURN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE;

  ------------------------------
  -- Get Department Nature ID --
  ------------------------------
  FUNCTION GET_DEPARTMENT_NATURE_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_CPT_ID            IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE;

  --------------------------
  -- Get Nature Detail ID --
  --------------------------
  FUNCTION GET_NATURE_DETAIL_ID(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CPT_ID            IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE;
  ------------------------------
  -- Get ADMIN COSTING AMOUNT --
  ------------------------------
  FUNCTION GET_ADMIN_COSTING_AMOUNT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_CPT_ID            IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT_COSTING.COST%TYPE;
  -----------------------------
  -- Get multiple qty allowed --
  -----------------------------
  FUNCTION GET_MULTIPLE_QTY_ALLOWED(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_CPT_ID            IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.MULTIPLE_QTY_ALLOWED%TYPE;
  -------------------------
  FUNCTION F_IS_SITE_MARKING_REQUIRED(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT.SITE_MARKING_REQUIRED%TYPE;

END PKG_CPT;
```

### DEFINITIONS.PKG_CPT_ACTIVATE_EFECTIVE_DATE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_ACTIVATE_EFECTIVE_DATE AS

  /***********************************************************************************************
         OBJECTIVE := THIS PACKAGE WILL BE USED TO ACTIVATE THE EFFECT DATE OF THE PRICE
                      REVISION, THIS PACKAGE WILL BE CALLED IN A JOB PROCEDURE
                      WHICH WILL BE EXECUTED ON HIS AT SOME FIXED TIME
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        16-APR-2013   RAI QAISER HUSSAIN     1. CREATED THIS PACKAGE
         1.1        08-FEB-2019   SHAHID JAMAL           1. ADDED GENERATE TOKEN PROCEDURE AND
                                                            USER AUTHORIZATION FUNCTION IN ORDER
                                                            TO CHECK THE USER RIGHTS TO UPDATE CPT
                                                            PRICE IN DEFINITIONS.CPT TABLE.
         2.0        15-APR-2019   MUHAMMAD ALI KHUBAIB   1. CHANGED TABLE CPT_PACKAGE WITH PACKAGE_ITEM
         2.1        02-JAN-2020   SHAHID JAMAL           1. ADDED CONDITION TO UPDATE PACKAGE PRICE ONLY
                                                            IF PRICE SOURCE IS INVOICE IN PROCESS_CPT_ACTIVATE PROCEDURE.
  ************************************************************************************************/
  -------------------------------
  -- RECORD TYPE FOR FETCH CPT --
  -------------------------------
  TYPE FETCH_CPT_REC IS RECORD(
    CPT_ID         DEFINITIONS.CPT.CPT_ID%TYPE,
    EFFECTIVE_DATE DATE,
    NEW_PRICE      DEFINITIONS.CPT_PRICE_HISTORY.NEW_PRICE%TYPE,
    PRICE          DEFINITIONS.CPT.PRICE%TYPE,
    SR_NO          DEFINITIONS.CPT_PRICE_HISTORY.SR_NO%TYPE);

  -- ARRAY --
  TYPE FETCH_CPT_TAB IS TABLE OF FETCH_CPT_REC;

  ---------------------------------------------------------------------------------------
  -- FETCHING NEW AND REVISED CPTS. NEW CPTS WILL ALSO BE INSERTED INTO CPT HIST TABLE --
  ---------------------------------------------------------------------------------------
  FUNCTION GET_FETCH_CPT(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN FETCH_CPT_TAB
    PIPELINED;

  ---------------------------------
  -- RECORD TYPE FOR CPT COSTING --
  ---------------------------------
  TYPE CPT_COSTING_REC IS RECORD(
    CPT_ID           DEFINITIONS.CPT.CPT_ID%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.CPT_COSTING.ADMIN_COSTING_ID%TYPE,
    NEW_COST         DEFINITIONS.CPT_COSTING.COST%TYPE);

  -- ARRAY --
  TYPE CPT_COSTING_TAB IS TABLE OF CPT_COSTING_REC;

  ---------------------------------------------------------------------
  -- INSERTING DATA INTO CPT COSTING FROM CPT COSTING HISTORY TABLES --
  ---------------------------------------------------------------------
  FUNCTION GET_CPT_COSTING_HISTORY(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN CPT_COSTING_TAB
    PIPELINED;

  ------------------------------
  -- RECORD TYPE FOR CONTRACT --
  ------------------------------
  TYPE CONTRACT_REC IS RECORD(
    CONTRACT_ID BILLING.CONTRACT.CONTRACT_ID%TYPE);

  -- ARRAY --
  TYPE CONTRACT_TAB IS TABLE OF CONTRACT_REC;

  ---------------------------------------------------------------
  -- COLLECTION CENTRE CONTRACTS WHERE CPT IS PART OF CONTRACT --
  ---------------------------------------------------------------
  FUNCTION GET_CONTRACT_ID(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN CONTRACT_TAB
    PIPELINED;

  --------------------------------
  -- CPT COST PRICE RECORD TYPE --
  --------------------------------
  TYPE CPT_COST_PRICE_REC IS RECORD(
    CPT_ID           DEFINITIONS.CPT.CPT_ID%TYPE,
    PACKAGE_ID       DEFINITIONS.CPT_PACKAGE.PACKAGE_ID%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.CPT_COSTING.ADMIN_COSTING_ID%TYPE,
    NEW_COST         DEFINITIONS.CPT_COSTING.COST%TYPE);

  -- ARRAY --
  TYPE CPT_COST_PRICE_TAB IS TABLE OF CPT_COST_PRICE_REC;

  ----------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE PACKAGES AND CPT --
  ----------------------------------------------------
  FUNCTION GET_CPT_COST_PRICE(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN CPT_COST_PRICE_TAB
    PIPELINED;

  ------------------------------------------------------------
  -- THIS PROCEDURE WILL ACTIVATE THE CPT ON EFFECTIVE DATE --
  ------------------------------------------------------------
  PROCEDURE PROCESS_CPT_ACTIVATE(P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                 P_ALERT_TEXT OUT VARCHAR2,
                                 P_STOP       OUT CHAR);
  -----------------------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO GENERATE THE TOKEN FOR GIVEN USER WHO CAN UPDATE CPT TABLE --
  -----------------------------------------------------------------------------------------------
  PROCEDURE GENERATE_TOKEN_FOR_CPT_UPDATE(P_USER_MRNO  IN REGISTRATION.PATIENT.MRNO%TYPE,
                                          P_ALERT_TEXT OUT VARCHAR2,
                                          P_STOP       OUT VARCHAR2);
  -------------------------------------------------------------------------------------------------
  -- THIS FUNCTION WILL BE USED TO CHECK WHETHER USER IS AUTHORIZED FOR CPT PRICE UPDATE OR NOT. --
  -------------------------------------------------------------------------------------------------
  FUNCTION CHECK_USER_AUTHORIZATION(P_USER_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN BOOLEAN;

  PROCEDURE CPT_PRICE_QUEUE_INSERTION(P_CPT_ID         DEFINITIONS.CPT.CPT_ID%TYPE,
                                      P_EFFECTIVE_DATE DEFINITIONS.CPT_PRICE_HISTORY.EFFECTIVE_DATE%TYPE,
                                      P_PRICE          DEFINITIONS.CPT.PRICE%TYPE,
                                      P_NEW_PRICE      DEFINITIONS.CPT.PRICE%TYPE,
                                      P_STOP           OUT CHAR,
                                      P_ALERT_TEXT     OUT VARCHAR2);

  PROCEDURE CPT_PRICE_QUEUE_UPDATION(P_CPT_ID         DEFINITIONS.CPT.CPT_ID%TYPE,
                                     P_EFFECTIVE_DATE DEFINITIONS.CPT_PRICE_HISTORY.EFFECTIVE_DATE%TYPE,
                                     P_ERROR          VARCHAR2,
                                     P_STOP           OUT CHAR,
                                     P_ALERT_TEXT     OUT VARCHAR2);

  ---------------------------------------------------------------------------------------------------------------------------------
  -- This procedure will be employed to insert the queue in case a price revision is entered for verification before activation. --
  ---------------------------------------------------------------------------------------------------------------------------------

  PROCEDURE CPT_PRICE_QUEUE_VERIFICATION(P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                         P_SR_NO      IN DEFINITIONS.CPT_COSTING_HISTORY.SR_NO%TYPE,
                                         P_STOP       OUT CHAR,
                                         P_ALERT_TEXT OUT VARCHAR2);

END PKG_CPT_ACTIVATE_EFECTIVE_DATE;
```

### DEFINITIONS.PKG_CPT_ARCHIVE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_ARCHIVE IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Faran Munawar Ghouri
  -- Created : 14-Oct-2020 18:17
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
  FUNCTION F_SELECT(P_CPT_ID         IN DEFINITIONS.CPT_ARCHIVE.CPT_ID%TYPE,
                    P_SRNO           IN DEFINITIONS.CPT_ARCHIVE.SRNO%TYPE,
                    P_ROW            OUT DEFINITIONS.CPT_ARCHIVE%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CPT_ID         IN DEFINITIONS.CPT_ARCHIVE.CPT_ID%TYPE,
                  P_SRNO           IN DEFINITIONS.CPT_ARCHIVE.SRNO%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.CPT_ARCHIVE%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CPT_ID         IN DEFINITIONS.CPT_ARCHIVE.CPT_ID%TYPE,
                    P_SRNO           IN DEFINITIONS.CPT_ARCHIVE.SRNO%TYPE,
                    P_ROW            IN OUT DEFINITIONS.CPT_ARCHIVE%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CPT_ID         IN DEFINITIONS.CPT_ARCHIVE.CPT_ID%TYPE,
                    P_SRNO           IN DEFINITIONS.CPT_ARCHIVE.SRNO%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_CPT_ARCHIVE;
```

### DEFINITIONS.PKG_CPT_AUTOMATION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_AUTOMATION IS

   --PRAGMA SERIALLY_REUSABLE;
	-- Author  : MISLAM
	-- Created : 6/12/2017 11:32:49 AM
	-- Purpose : Store all Procedures and Functions related to CPT mapping,creation

	PROCEDURE ORG_CPT_DATA_POPULATE(P_ORG_ID           IN DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
																	P_ORG_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
																	P_CALLING_USER     IN REGISTRATION.PATIENT.MRNO%TYPE,
																	P_CALLING_OBJECT   IN VARCHAR2,
																	P_CALLING_TERMINAL IN VARCHAR2,
																	P_EVENT            IN VARCHAR2,
																	P_ALERT_TEXT       OUT VARCHAR2,
																	P_STOP             OUT CHAR);

  PROCEDURE CHECK_CPT_ACTIVATION(  P_CPT_ID   IN DEFINITIONS.CPT.CPT_ID%TYPE,
    P_ORG_ID           IN DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
                                  P_ORG_LOCATION_ID  IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_CPT_NATURE_ID    IN DEFINITIONS.CPT.DEPARTMENT_NATURE_ID%TYPE,
                                  P_CPT_NATURE_DETAIL_ID IN DEFINITIONS.CPT.NATURE_DETAIL_ID%TYPE,
                                  P_CPT_DEPARTMENT_ID IN DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                                  P_CPT_SECTION_ID  IN DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                  P_CALLING_USER     IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_CALLING_OBJECT   IN VARCHAR2,
                                  P_CALLING_TERMINAL IN VARCHAR2,
                                  P_EVENT            IN VARCHAR2,
                                  P_ALERT_TEXT       OUT VARCHAR2,
                                  P_STOP             OUT CHAR);

END PKG_CPT_AUTOMATION;
```

### DEFINITIONS.PKG_CPT_BC
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.pkg_CPT_BC IS

  -- Author  : Muhammad Abid Nazir
  -- Created : 02-Nov-2017 04:24:07 PM
  -- Purpose : Contains Procedure and Functions related to DEFINITIONS.CPT
  --           This package is Business Component for CPTs. This package
  --           contains business logic procedures/function related to CPT

  -- Public type declarations
  --type <TypeName> is <Datatype>;

  -- Public constant declarations
  --<ConstantName> constant <Datatype> := <Value>;

  -- Public variable declarations
  --<VariableName> <Datatype>;

  -- ======================================================================================== --
  FUNCTION F_DEF_SPECIMEN(P_CPT_ID         IN DEFINITIONS.CPT_SPECIMEN.CPT_ID%TYPE,
                          P_SPECIMEN_ID    OUT DEFINITIONS.CPT_SPECIMEN.SPECIMEN_ID%TYPE,
                          P_LOCATION_ID    IN VARCHAR2,
                          P_CALLING_OBJECT IN VARCHAR2,
                          P_CALLING_USER   IN VARCHAR2,
                          P_CALLING_EVENT  IN VARCHAR2,
                          P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ======================================================================================== --
  FUNCTION F_DEF_DEPARTMENT(P_CPT_ID         IN DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
                            P_DEPARTMENT_ID  OUT DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                            P_SECTION_ID     OUT DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
                            P_LOCATION_ID    IN VARCHAR2,
                            P_CALLING_OBJECT IN VARCHAR2,
                            P_CALLING_USER   IN VARCHAR2,
                            P_CALLING_EVENT  IN VARCHAR2,
                            P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ======================================================================================== --
  FUNCTION F_LOC_DEPARTMENT(P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.CPT_ID%TYPE,
                            P_CPT_LOC        IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.LOCATION_ID%TYPE,
                            P_DEPARTMENT_ID  OUT DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                            P_SECTION_ID     OUT DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
                            P_LOCATION_ID    IN VARCHAR2,
                            P_CALLING_OBJECT IN VARCHAR2,
                            P_CALLING_USER   IN VARCHAR2,
                            P_CALLING_EVENT  IN VARCHAR2,
                            P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ======================================================================================== --
  FUNCTION F_NATURE(P_CPT_ID         IN DEFINITIONS.CPT.CPT_ID%TYPE,
                    P_NATURE_ID      OUT DEFINITIONS.CPT.NATURE_ID%TYPE,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ======================================================================================== --
  FUNCTION F_NATURE_DETAIL(P_CPT_ID         IN DEFINITIONS.CPT.CPT_ID%TYPE,
                           P_NATURE_ID      OUT DEFINITIONS.CPT.NATURE_ID%TYPE,
                           P_DETAIL_ID      OUT DEFINITIONS.CPT.NATURE_DETAIL_ID%TYPE,
                           P_LOCATION_ID    IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

-- ======================================================================================== --

END;
```

### DEFINITIONS.PKG_CPT_CAT_PRICE_ACTIVATION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_CAT_PRICE_ACTIVATION AS
  /***********************************************************************************************
         OBJECTIVE := This Package will be used to activate the Effect date of the price
                      Revision for CPT Categories, This Package will be called in a Job Procedure
                      which will be executed on HIS at some fixed time
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        07-Jan-2014   Usman Afzal(5784)     1. Created this Package
  ************************************************************************************************/
  -- Record Type For CPT Category Price --
  TYPE CPT_CAT_PRICE_REC IS RECORD(
    CPT_CATEGORY_ID DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    EFFECTIVE_DATE  DATE,
    NEW_PRICE       DEFINITIONS.CPT_CAT_PRICE_HISTORY.NEW_PRICE%TYPE,
    OLD_PRICE       DEFINITIONS.CPT_CAT_PRICE_HISTORY.OLD_PRICE%TYPE,
    SR_NO           DEFINITIONS.CPT_CAT_PRICE_HISTORY.SR_NO%TYPE);
  -- Associative Array --
  TYPE CPT_CAT_PRICE_TAB IS TABLE OF CPT_CAT_PRICE_REC;
  ---------------------------------------------------------------------------------
  -- This Function will return the List of CPT Categories whose price is Updated --
  ---------------------------------------------------------------------------------
  FUNCTION GET_CPT_CAT_PRICE_HISTORY(P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE)
    RETURN CPT_CAT_PRICE_TAB
    PIPELINED;
  -- Recrod Type for CPT Category Costing --
  TYPE CPT_CAT_COSTING_REC IS RECORD(
    CPT_CATEGORY_ID  DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.ADMIN_COSTING.ADMIN_COSTING_ID%TYPE,
    NEW_PRICE        DEFINITIONS.CPT_CAT_COSTING_HISTORY.NEW_PRICE%TYPE,
    OLD_PRICE        DEFINITIONS.CPT_CAT_COSTING_HISTORY.OLD_PRICE%TYPE);
  -- Associative Array --
  TYPE CPT_CAT_COSTING_TAB IS TABLE OF CPT_CAT_COSTING_REC;

  ------------------------------------------------------------
  -- This Function will return the New CPT Category Costing --
  ------------------------------------------------------------
  FUNCTION GET_CPT_CAT_COSTING(P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                               P_SR_NO           IN DEFINITIONS.CPT_CAT_PRICE_HISTORY.SR_NO%TYPE)
    RETURN CPT_CAT_COSTING_TAB
    PIPELINED;

  ---------------------------------------------------------------------------
  -- This Procedure will Activate the CPT Category Price on Effective Date --
  ---------------------------------------------------------------------------
  PROCEDURE ACTIVATE_CPT_CAT_PRICE(P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                                   P_ALERT_TEXT      OUT VARCHAR2,
                                   P_STOP            OUT CHAR);
  -- Record Type for CPT Price History --
  TYPE CPT_PRICE_HISTORY_REC IS RECORD(
    CPT_ID          DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_CATEGORY_ID DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    PRICE           DEFINITIONS.CPT.PRICE%TYPE);
  -- Associative Array --
  TYPE CPT_PRICE_HISTORY_TAB IS TABLE OF CPT_PRICE_HISTORY_REC;

  --------------------------------------------------------------------
  -- This Fuction will return CPTs attached with the given Category --                                 
  --------------------------------------------------------------------
  FUNCTION GET_CPT_LIST(P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE)
    RETURN CPT_PRICE_HISTORY_TAB
    PIPELINED;

  --------------------------------------------------------------------------------
  -- This Function will return Max Sr No. From CPT Price History against CPT ID --
  --------------------------------------------------------------------------------
  FUNCTION GET_MAX_SR_NO(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN DEFINITIONS.CPT_PRICE_HISTORY.SR_NO%TYPE;
END PKG_CPT_CAT_PRICE_ACTIVATION;
```

### DEFINITIONS.PKG_CPT_DEPARTMENT_SECTION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_DEPARTMENT_SECTION IS
	-- Author  : MUHAMMAD  ISLAM
	-- Created : 21-Jun-2017 12:39
	-- Purpose :
	-- ******************************************************************************************************--
	FUNCTION F_SELECT(P_CPT_ID         IN DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
										P_DEPARTMENT_ID  IN DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
										P_SECTION_ID     IN DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
										P_ROW            OUT DEFINITIONS.CPT_DEPARTMENT_SECTION%ROWTYPE,
										P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
										P_LOCATION_ID    IN VARCHAR2,
										P_CALLING_OBJECT IN VARCHAR2,
										P_CALLING_USER   IN VARCHAR2,
										P_CALLING_EVENT  IN VARCHAR2,
										P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

	-- ******************************************************************************************************--
	FUNCTION F_LOCK(P_CPT_ID         IN DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
									P_DEPARTMENT_ID  IN DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
									P_SECTION_ID     IN DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
									P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
									P_LOCATION_ID    IN VARCHAR2,
									P_CALLING_OBJECT IN VARCHAR2,
									P_CALLING_USER   IN VARCHAR2,
									P_CALLING_EVENT  IN VARCHAR2,
									P_ROWID          OUT ROWID,
									P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

	-- ******************************************************************************************************--
	FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.CPT_DEPARTMENT_SECTION%ROWTYPE,
										P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
										P_LOCATION_ID      IN VARCHAR2,
										P_CALLING_OBJECT   IN VARCHAR2,
										P_CALLING_USER     IN VARCHAR2,
										P_CALLING_EVENT    IN VARCHAR2,
										P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;

	-- ******************************************************************************************************--
	FUNCTION F_UPDATE(P_CPT_ID         IN DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
										P_DEPARTMENT_ID  IN DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
										P_SECTION_ID     IN DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
										P_ROW            IN OUT DEFINITIONS.CPT_DEPARTMENT_SECTION%ROWTYPE,
										P_UPDATE_NULL    IN CHAR DEFAULT NULL,
										P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
										P_LOCATION_ID    IN VARCHAR2,
										P_CALLING_OBJECT IN VARCHAR2,
										P_CALLING_USER   IN VARCHAR2,
										P_CALLING_EVENT  IN VARCHAR2,
										P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

	-- ******************************************************************************************************--
	FUNCTION F_DELETE(P_CPT_ID         IN DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
										P_DEPARTMENT_ID  IN DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
										P_SECTION_ID     IN DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
										P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
										P_LOCATION_ID    IN VARCHAR2,
										P_CALLING_OBJECT IN VARCHAR2,
										P_CALLING_USER   IN VARCHAR2,
										P_CALLING_EVENT  IN VARCHAR2,
										P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

	-- ******************************************************************************************************--
END PKG_CPT_DEPARTMENT_SECTION;
```

### DEFINITIONS.PKG_CPT_NATURE_MAPPING
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_NATURE_MAPPING IS
  -- Author  : Syed Gohar li
  -- Created : 19-Aug-2019 14:33
  -- Purpose :
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_CPT_ID          IN DEFINITIONS.CPT_NATURE_MAPPING.CPT_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_DETAIL_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.CPT_NATURE_MAPPING%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;  
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CPT_ID          IN DEFINITIONS.CPT_NATURE_MAPPING.CPT_ID%TYPE,
                  P_SETUP_NATURE_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_NATURE_ID%TYPE,
                  P_SETUP_DETAIL_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_DETAIL_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID     IN VARCHAR2,
                  P_CALLING_OBJECT  IN VARCHAR2,
                  P_CALLING_USER    IN VARCHAR2, 
                  P_CALLING_EVENT   IN VARCHAR2,  
                  P_ROWID           OUT ROWID,
                  P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.CPT_NATURE_MAPPING%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2, 
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CPT_ID          IN DEFINITIONS.CPT_NATURE_MAPPING.CPT_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_DETAIL_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.CPT_NATURE_MAPPING%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CPT_ID          IN DEFINITIONS.CPT_NATURE_MAPPING.CPT_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID IN DEFINITIONS.CPT_NATURE_MAPPING.SETUP_DETAIL_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_CPT_NATURE_MAPPING;
```

### DEFINITIONS.PKG_CPT_PERFORM_TIMING
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_PERFORM_TIMING IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 07:13
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
  FUNCTION F_SELECT(P_CPT_ID         IN DEFINITIONS.CPT_PERFORM_TIMING.CPT_ID%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.CPT_PERFORM_TIMING.LOCATION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.CPT_PERFORM_TIMING%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CPT_ID         IN DEFINITIONS.CPT_PERFORM_TIMING.CPT_ID%TYPE,
                  P_LOCATION_ID    IN DEFINITIONS.CPT_PERFORM_TIMING.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.CPT_PERFORM_TIMING%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CPT_ID         IN DEFINITIONS.CPT_PERFORM_TIMING.CPT_ID%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.CPT_PERFORM_TIMING.LOCATION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.CPT_PERFORM_TIMING%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CPT_ID         IN DEFINITIONS.CPT_PERFORM_TIMING.CPT_ID%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.CPT_PERFORM_TIMING.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_CPT_PERFORM_TIMING;
```

### DEFINITIONS.PKG_CPT_PROPOSAL
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_PROPOSAL IS

  /***********************************************************************************************
         OBJECTIVE := This package was created for CPT PRICE REVISION
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        15-DEC-2021   Muhammad Ali Khubaib   1. Created
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ---------------------------------------------------------
  -- This procedure will be used to generate proposal ID --
  ---------------------------------------------------------
  PROCEDURE GEN_COUNTER_CPT_PROPOSAL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                     P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_PROPOSAL_ID       OUT DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                     P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                     P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                                     P_ALERT_TEXT        OUT VARCHAR2,
                                     P_STOP              OUT VARCHAR2);
  ---------------------------------------------
  -- This procedure will initialize workflow --
  ---------------------------------------------
  PROCEDURE INITIALIZE_WORKFLOW(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  PROCEDURE POPULATE_QUEUE(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_EVENT_ID          IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                           P_WFE_NO            IN DEFINITIONS.CPT_PROP_WORKFLOW_Q.WFE_NO%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);

  ---------------------------------------------------------
  -- This function will be used to get event description --
  ---------------------------------------------------------
  FUNCTION GET_EVENT_DESC(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                          P_WFE_NO      IN DEFINITIONS.CPT_PROP_WORKFLOW.WFE_NO%TYPE)
    RETURN DEFINITIONS.EVENT.DESCRIPTION%TYPE;

  --------------------------------------------------
  -- This function will be used to get event Id --
  --------------------------------------------------
  FUNCTION GET_EVENT_ID(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                        P_WFE_NO      IN DEFINITIONS.CPT_PROP_WORKFLOW.WFE_NO%TYPE)
    RETURN DEFINITIONS.EVENT.EVENT_ID%TYPE;

  PROCEDURE POST_WORKFLOW_EVENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                P_EVENT_ID          IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                                P_WORKFLOW_REMARKS  IN DEFINITIONS.CPT_PROP_WORKFLOW.REMARKS%TYPE,
                                P_USER_MRNO         IN VARCHAR2,
                                P_TERMINAL          IN VARCHAR2,
                                P_OBJECT_CODE       IN VARCHAR2,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ----------------------------------------------------------
  -- This procedure is used to get future action buttons  --
  ----------------------------------------------------------
  PROCEDURE GET_ACTION_BTN3(P_SCHEMA_ID        IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE,
                            P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE,
                            P_WORK_FLOW_ID     IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE,
                            P_EVENT_ID         IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                            P_USER_MRNO        IN HRD.INFORMATION.MRNO%TYPE DEFAULT NULL,
                            P_LOV_NAME         IN SECURITY.LOVS.LOVNAME%TYPE DEFAULT NULL,
                            P_BUTTONS          OUT RADIATION.PKG_WORKFLOW.T_BTN_TAB,
                            P_ALERT_TEXT       OUT VARCHAR2,
                            P_STOP             OUT VARCHAR2);
  FUNCTION GET_PARAMETER_VALUE(P_SCHEMA_ID        IN DEFINITIONS.PR_TYPE_FLOW_EVENT.SCHEMA_ID%TYPE,
                               P_WORKFLOW_TYPE_ID IN DEFINITIONS.PR_TYPE_FLOW_EVENT.PURCHASE_TYPE_ID%TYPE,
                               P_WORK_FLOW_ID     IN DEFINITIONS.PR_TYPE_FLOW_EVENT.WORK_FLOW_ID%TYPE,
                               P_EVENT_ID         IN DEFINITIONS.PR_TYPE_FLOW_EVENT.EVENT_ID%TYPE,
                               P_PARAMETER_TYPE   IN DEFINITIONS.EVENT_WISE_PARAMETER.PARAMETER_TYPE%TYPE)
    RETURN DEFINITIONS.EVENT_WISE_DETAIL.PARAMETER_VALUE%TYPE;
  --------------------------------------------------------
  -- Following function will return total material cost --
  --------------------------------------------------------
  FUNCTION GET_MATERIAL_COST(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE;
  --------------------------------------------------------
  -- Following function will return total manpower cost --
  --------------------------------------------------------
  FUNCTION GET_MANPOWER_COST(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE;
  --------------------------------------------------------
  -- Following function will return total material cost --
  --------------------------------------------------------
  FUNCTION GET_OVERHEAD_COST(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE;
  --------------------------------------------------------
  -- Following function will return total material cost --
  --------------------------------------------------------
  FUNCTION GET_DEPRECIATION_COST(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                 P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE;
  --------------------------------------------------------
  -- Following function will return total direct cost --
  --------------------------------------------------------
  FUNCTION GET_DIRECT_COST(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE;
  --------------------------------------------------------
  -- Following function will return total SELLING cost --
  --------------------------------------------------------
  FUNCTION GET_SELLING_PRICE(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE;
  PROCEDURE SEND_TO_LAST_EVENT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_WORKFLOW_REMARKS  IN DEFINITIONS.CPT_PROP_WORKFLOW.REMARKS%TYPE,
                               P_USER_MRNO         IN VARCHAR2,
                               P_TERMINAL          IN VARCHAR2,
                               P_OBJECT_CODE       IN VARCHAR2,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  PROCEDURE VALIDATE_CPT_ID(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                            P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                            P_ALERT_TEXT  OUT VARCHAR2,
                            P_STOP        OUT CHAR);
  PROCEDURE SHEET_LEVEL_VALIDATIONS(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                    P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                    P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                    P_SHEET_TYPE        IN VARCHAR2,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  PROCEDURE FINALIZE_CPT_COSTING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                 P_USER_MRNO         IN VARCHAR2,
                                 P_TERMINAL          IN VARCHAR2,
                                 P_OBJECT_CODE       IN VARCHAR2,
                                 P_ALERT_TEXT        OUT VARCHAR2,
                                 P_STOP              OUT CHAR);
  PROCEDURE POST_CPT_COSTING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_OBJECT_CODE       IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  ---------------------------------------------------------------
  -- This Procedure will enter the count for user pending task --
  ---------------------------------------------------------------
  PROCEDURE PENDING_TASK_CPT(P_MRNO          IN VARCHAR2,
                             P_ACTING_FOR    IN VARCHAR2,
                             P_OBJECT_CODE   IN VARCHAR2,
                             P_PROCESS_ID    IN VARCHAR2,
                             P_TERMINAL      IN VARCHAR2,
                             P_EVENT         IN VARCHAR2,
                             P_ASSIGNMENT_ID IN NUMBER);
  --------------------------------------------------------
  -- Following function will return material pack price --
  --------------------------------------------------------
  FUNCTION GET_MATERIAL_PACK_PRICE(P_ITEM_ID        IN DEFINITIONS.CPT_MT_items_DETAIL.ITEM_ID%TYPE,
                                   P_STORE_ID       IN DEFINITIONS.CPT_MT_items_DETAIL.STORE_ID%TYPE,
                                   P_EFFECTIVE_DATE IN DEFINITIONS.CPT_MT_SETUP.EFFECTIVE_FROM%TYPE)
    RETURN DEFINITIONS.CPT_MT_items_DETAIL.PACK_PRICE%TYPE;
  ---------------------------------------------------------
  -- This Procedure is used to populate Item on Material Price List --
  ---------------------------------------------------------
  PROCEDURE POPULATE_ITEM_LIST(P_MATERIAL_SETUP_ID IN Definitions.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT CHAR);
  ---------------------------------------------------------
  -- This Procedure is used to populate Previous Sheet --
  ---------------------------------------------------------
  PROCEDURE POPULATE_PREVIOUS_SHEET(P_MATERIAL_SETUP_ID IN Definitions.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                                    P_NATURE_ID         IN Definitions.CPT_MT_SETUP.NATURE_ID%TYPE,
                                    P_NATURE_DETAIL_ID  IN Definitions.CPT_MT_SETUP.NATURE_DETAIL_ID%TYPE,
                                    P_ALERT_TEXT        OUT VARCHAR2,
                                    P_STOP              OUT CHAR);
  ---------------------------------------------------------
  -- This Procedure is used to Update Item Price
  ---------------------------------------------------------
  PROCEDURE UPDATE_ITEM_PRICE(P_MATERIAL_SETUP_ID IN Definitions.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                              P_NATURE_ID         IN Definitions.CPT_MT_SETUP.NATURE_ID%TYPE,
                              P_NATURE_DETAIL_ID  IN Definitions.CPT_MT_SETUP.NATURE_DETAIL_ID%TYPE,
                              P_PROPOSAL_ID       IN NUMBER,
                              P_ALERT_TEXT        OUT VARCHAR2,
                              P_STOP              OUT CHAR);

  PROCEDURE POPULATE_FREQ_CONSM(P_MATERIAL_SETUP_ID IN DEFINITIONS.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                                P_ALERT_TEXT        OUT VARCHAR2,
                                P_STOP              OUT CHAR);
  ---------------------------------------------------------
  -- This Procedure is used to update CPT Actual Unit --
  ---------------------------------------------------------
  PROCEDURE UPDATE_CPT_ACTUAL_UNIT(P_MATERIAL_SETUP_ID IN DEFINITIONS.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                                   P_ITEM_ID           IN DEFINITIONS.CPT_MT_ITEMS_DETAIL.ITEM_ID%TYPE,
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  PROCEDURE CALCULATE_PROPOTIONATE(P_MATERIAL_SETUP_ID IN DEFINITIONS.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                                   P_ITEM_ID           IN DEFINITIONS.CPT_MT_ITEMS_DETAIL.ITEM_ID%TYPE,
                                   P_DISTRIBUTION_TYPE IN CHAR, -- 'C', 'E', 'R'
                                   P_ALERT_TEXT        OUT VARCHAR2,
                                   P_STOP              OUT CHAR);
  ---------------------------------------------------------
-- THIS PROCEDURE IS USED TO UPDATE IN-PROCESS PROPOSAL --
---------------------------------------------------------

END PKG_CPT_PROPOSAL;
```

### DEFINITIONS.PKG_CPT_SPECIALTIES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_CPT_SPECIALTIES IS

  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : 00160000002870 SHUMAILA SHAHID
  -- Created : 24-Jun-2021 18:10
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
  FUNCTION F_SELECT(P_CPT_ID               IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,
                    P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CPT_SPECIALTIES.CLINIC_SPECIALITY_ID%TYPE,
                    P_ROW                  OUT DEFINITIONS.CPT_SPECIALTIES%ROWTYPE,
                    P_IGNORE_NO_DATA       IN CHAR DEFAULT NULL,
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;

  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CPT_ID               IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,
                  P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CPT_SPECIALTIES.CLINIC_SPECIALITY_ID%TYPE,
                  P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID          IN VARCHAR2,
                  P_CALLING_OBJECT       IN VARCHAR2,
                  P_CALLING_USER         IN VARCHAR2,
                  P_CALLING_EVENT        IN VARCHAR2,
                  P_ROWID                OUT ROWID,
                  P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;

  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.CPT_SPECIALTIES%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;

  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CPT_ID               IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,
                    P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CPT_SPECIALTIES.CLINIC_SPECIALITY_ID%TYPE,
                    P_ROW                  IN OUT DEFINITIONS.CPT_SPECIALTIES%ROWTYPE,
                    P_UPDATE_NULL          IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;

  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CPT_ID               IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,
                    P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CPT_SPECIALTIES.CLINIC_SPECIALITY_ID%TYPE,
                    P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;

  -- ******************************************************************************************************--
END PKG_CPT_SPECIALTIES;
```

### DEFINITIONS.PKG_DEFAULT_FILES_SERVERS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DEFAULT_FILES_SERVERS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : HAFIZ ABRAR AHMED
  -- Created : 24-Mar-2016 12:39
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
  FUNCTION F_SELECT(P_LOCATION_ID    IN DEFINITIONS.DEFAULT_FILES_SERVERS.LOCATION_ID%TYPE,
                    P_SERVER_TYPE_ID IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                    P_SERVER_ID      IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.DEFAULT_FILES_SERVERS.FILE_TYPE_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.DEFAULT_FILES_SERVERS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOC_ID         IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID    IN DEFINITIONS.DEFAULT_FILES_SERVERS.LOCATION_ID%TYPE,
                  P_SERVER_TYPE_ID IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                  P_SERVER_ID      IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_ID%TYPE,
                  P_FILE_TYPE_ID   IN DEFINITIONS.DEFAULT_FILES_SERVERS.FILE_TYPE_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOC_ID         IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.DEFAULT_FILES_SERVERS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOC_ID           IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID    IN DEFINITIONS.DEFAULT_FILES_SERVERS.LOCATION_ID%TYPE,
                    P_SERVER_TYPE_ID IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                    P_SERVER_ID      IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.DEFAULT_FILES_SERVERS.FILE_TYPE_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.DEFAULT_FILES_SERVERS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOC_ID         IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID    IN DEFINITIONS.DEFAULT_FILES_SERVERS.LOCATION_ID%TYPE,
                    P_SERVER_TYPE_ID IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                    P_SERVER_ID      IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.DEFAULT_FILES_SERVERS.FILE_TYPE_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOC_ID         IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEFAULT_FILES_SERVERS;
```

### DEFINITIONS.PKG_DEFAULT_ONCOLOGIST
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DEFAULT_ONCOLOGIST IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Abdul Wadood
  -- Created : 01-Dec-2019 18:56
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
 FUNCTION F_SELECT(P_ORG_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ORG_ID%TYPE,
                                        P_ZON_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ZON_ID%TYPE,
                                        P_LOC_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.LOC_ID%TYPE,
                                        P_ONCOLOGIST_MRNO IN DEFINITIONS.DEFAULT_ONCOLOGIST.ONCOLOGIST_MRNO%TYPE,
                                        P_ROW  OUT DEFINITIONS.DEFAULT_ONCOLOGIST%ROWTYPE,
                                        P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
     FUNCTION F_LOCK(P_ORG_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ORG_ID%TYPE,
                                        P_ZON_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ZON_ID%TYPE,
                                        P_LOC_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.LOC_ID%TYPE,
                                        P_ONCOLOGIST_MRNO IN DEFINITIONS.DEFAULT_ONCOLOGIST.ONCOLOGIST_MRNO%TYPE,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ROWID          OUT ROWID,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_INSERT(P_ROW IN OUT DEFINITIONS.DEFAULT_ONCOLOGIST%ROWTYPE,
                                        P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                                        P_LOCATION_ID      IN VARCHAR2,
                                        P_CALLING_OBJECT   IN VARCHAR2,
                                        P_CALLING_USER     IN VARCHAR2,
                                        P_CALLING_EVENT    IN VARCHAR2,
                                        P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_UPDATE(P_ORG_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ORG_ID%TYPE,
                                        P_ZON_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ZON_ID%TYPE,
                                        P_LOC_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.LOC_ID%TYPE,
                                        P_ONCOLOGIST_MRNO IN DEFINITIONS.DEFAULT_ONCOLOGIST.ONCOLOGIST_MRNO%TYPE,
                                        P_ROW IN OUT DEFINITIONS.DEFAULT_ONCOLOGIST%ROWTYPE,
                                        P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
 FUNCTION F_DELETE(P_ORG_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ORG_ID%TYPE,
                                        P_ZON_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.ZON_ID%TYPE,
                                        P_LOC_ID IN DEFINITIONS.DEFAULT_ONCOLOGIST.LOC_ID%TYPE,
                                        P_ONCOLOGIST_MRNO IN DEFINITIONS.DEFAULT_ONCOLOGIST.ONCOLOGIST_MRNO%TYPE,
                                        P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                                        P_LOCATION_ID    IN VARCHAR2,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
-- ******************************************************************************************************--
END PKG_DEFAULT_ONCOLOGIST;
```

### DEFINITIONS.PKG_DELETE_OLD_ARCHIVE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DELETE_OLD_ARCHIVE IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : 00160000005787 DEVDB
  -- Created : 17-Jun-2019 15:07
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
  FUNCTION F_SELECT(P_OWNER          IN DBSOURCE.DELETE_OLD_ARCHIVE.OWNER%TYPE,
                    P_OBJECT_NAME    IN DBSOURCE.DELETE_OLD_ARCHIVE.OBJECT_NAME%TYPE,
                    P_ROW            OUT DBSOURCE.DELETE_OLD_ARCHIVE%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_OWNER          IN DBSOURCE.DELETE_OLD_ARCHIVE.OWNER%TYPE,
                  P_OBJECT_NAME    IN DBSOURCE.DELETE_OLD_ARCHIVE.OBJECT_NAME%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DBSOURCE.DELETE_OLD_ARCHIVE%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_OWNER          IN DBSOURCE.DELETE_OLD_ARCHIVE.OWNER%TYPE,
                    P_OBJECT_NAME    IN DBSOURCE.DELETE_OLD_ARCHIVE.OBJECT_NAME%TYPE,
                    P_ROW            IN OUT DBSOURCE.DELETE_OLD_ARCHIVE%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_OWNER          IN DBSOURCE.DELETE_OLD_ARCHIVE.OWNER%TYPE,
                    P_OBJECT_NAME    IN DBSOURCE.DELETE_OLD_ARCHIVE.OBJECT_NAME%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DELETE_OLD_ARCHIVE;
```

### DEFINITIONS.PKG_DEPARTMENT
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DEPARTMENT IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 07:16
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
  FUNCTION F_SELECT(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.DEPARTMENT%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.DEPARTMENT%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.DEPARTMENT%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEPARTMENT;
```

### DEFINITIONS.PKG_DEPARTMENTAL_HOLIDAYS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DEPARTMENTAL_HOLIDAYS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 07:57
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
  FUNCTION F_SELECT(P_HOLIDAY_ID     IN DEFINITIONS.DEPARTMENTAL_HOLIDAYS.HOLIDAY_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.DEPARTMENTAL_HOLIDAYS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_HOLIDAY_ID     IN DEFINITIONS.DEPARTMENTAL_HOLIDAYS.HOLIDAY_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.DEPARTMENTAL_HOLIDAYS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_HOLIDAY_ID     IN DEFINITIONS.DEPARTMENTAL_HOLIDAYS.HOLIDAY_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.DEPARTMENTAL_HOLIDAYS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_HOLIDAY_ID     IN DEFINITIONS.DEPARTMENTAL_HOLIDAYS.HOLIDAY_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEPARTMENTAL_HOLIDAYS;
```

### DEFINITIONS.PKG_DEPARTMENT_SECTION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DEPARTMENT_SECTION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 08:00
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
  FUNCTION F_SELECT(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.DEPARTMENT_SECTION%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                  P_SECTION_ID     IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.DEPARTMENT_SECTION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.DEPARTMENT_SECTION%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DEPARTMENT_ID  IN DEFINITIONS.DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DEPARTMENT_SECTION;
```

### DEFINITIONS.PKG_DISEASE_FLOWSHEET_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DISEASE_FLOWSHEET_SETUP IS

  -- AUTHOR  : RAZAHASSAN
  -- CREATED : 11/19/2018 12:58:33 PM
  -- PURPOSE :

  TYPE DIS_FLWSH_STP_RECORD IS RECORD(
    FLWSH_SETUP_ID    DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
    DISEASE_ID        DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DISEASE_ID%TYPE,
    SETUP_NAME        DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_NAME%TYPE,
    SETUP_DESCRIPTION DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_DESCRIPTION%TYPE,
    DISEASE_NAME      DEFINITIONS.DISEASES.DISEASE_NAME%TYPE,
    SETUP_USER_MRNO   DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_USER_MRNO%TYPE,
    USER_NAME         SECURITY.USERS.FULL_NAME%TYPE,
    ACTIVE_FLAG       DEFINITIONS.DISEASE_FLOWSHEET_SETUP.ACTIVE_FLAG%TYPE,
    LOCATION_ID       DEFINITIONS.DISEASE_FLOWSHEET_SETUP.LOCATION_ID%TYPE,
    ORGANIZATION_ID   DEFINITIONS.DISEASE_FLOWSHEET_SETUP.ORGANIZATION_ID%TYPE,
    DEFAULT_FLAG      DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DEFAULT_FLAG%TYPE
    -----------------------------------------------------------
    );

  TYPE DIS_FLWSH_STP_CUR IS REF CURSOR RETURN DIS_FLWSH_STP_RECORD;
  TYPE DIS_FLWSH_STP_TAB IS TABLE OF DIS_FLWSH_STP_RECORD INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_STP_REFCUR(DIS_FLWSH_STP_DATA IN OUT DIS_FLWSH_STP_CUR,
                                   P_FLWSH_SETUP_ID   DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                   P_DISEASE_NAME     DEFINITIONS.DISEASES.DISEASE_NAME%TYPE,
                                   P_SETUP_NAME       DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_NAME%TYPE,
                                   P_SETUP_DESC       DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_DESCRIPTION%TYPE,
                                   P_ACTIVE_FLAG      DEFINITIONS.DISEASE_FLOWSHEET_SETUP.ACTIVE_FLAG%TYPE,
                                   P_DEFAULT_FLAG     DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DEFAULT_FLAG%TYPE,
                                   P_SETUP_USER_MRNO  DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_USER_MRNO%TYPE);

  PROCEDURE P_DIS_FLWSH_STP_INSERT(P_TAB_DATA             IN DIS_FLWSH_STP_TAB,
                                   P_FLWSH_SETUP_ID       OUT DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                   P_LOCATION_ID          IN VARCHAR2,
                                   P_PHYSICAL_LOCATION_ID IN VARCHAR2,
                                   P_USER_MRNO            IN VARCHAR2,
                                   P_OBJECT_CODE          IN VARCHAR2,
                                   P_STOP                 OUT VARCHAR2,
                                   P_ALERT_TEXT           OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_STP_LOCK(P_TAB_DATA   IN OUT DIS_FLWSH_STP_TAB,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_STP_UPDATE(P_TAB_DATA   IN DIS_FLWSH_STP_TAB,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_STP_DELETE(P_TAB_DATA   IN DIS_FLWSH_STP_TAB,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  TYPE DIS_FLWSH_PARAM_ASSG_REC IS RECORD(
    DIS_FLWSH_PARAM_ID    DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
    PARAM_NAME            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
    SHORT_CODE            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
    PARAM_DESCRIPTION     DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_DESCRIPTION%TYPE,
    ACTIVE_FLAG           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ACTIVE_FLAG%TYPE,
    RESTRICT_MANUAL_ENTRY DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.RESTRICT_MANUAL_ENTRY%TYPE,
    FLWSH_SETUP_ID        DEFINITIONS.DIS_FLWSH_PARAM_ASSG.FLWSH_SETUP_ID%TYPE,
    ORDER_BY              DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ORDER_BY%TYPE,
    ASSIGNMENT_ID         DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ASSIGNMENT_ID%TYPE,
    LOCATION_ID           DEFINITIONS.DIS_FLWSH_PARAM_ASSG.LOCATION_ID%TYPE,
    REMARKS               DEFINITIONS.DIS_FLWSH_PARAM_ASSG.REMARKS%TYPE);

  TYPE DIS_FLWSH_PARAM_ASSG_CUR IS REF CURSOR RETURN DIS_FLWSH_PARAM_ASSG_REC;
  TYPE DIS_FLWSH_PARAM_ASSG_TAB IS TABLE OF DIS_FLWSH_PARAM_ASSG_REC INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_PARAM_ASSG_RFCR(DIS_FLWSH_PARAM_ASSG_DATA IN OUT DIS_FLWSH_PARAM_ASSG_CUR,
                                        P_FLWSH_SETUP_ID          DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                        P_ASSIGNMENT_ID           DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ASSIGNMENT_ID%TYPE,
                                        P_PARAM_NAME              DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
                                        P_SHORT_CODE              DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
                                        P_PARAM_DESCRIPTION       DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_DESCRIPTION%TYPE,
                                        P_ACTIVE_FLAG             DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ACTIVE_FLAG%TYPE,
                                        P_RESTRICT_MANUAL_ENTRY   DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.RESTRICT_MANUAL_ENTRY%TYPE,
                                        P_ORDER_BY                DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ORDER_BY%TYPE);

  PROCEDURE P_DIS_FLWSH_PARAM_ASSG_INS(P_TAB_DATA                IN DIS_FLWSH_PARAM_ASSG_TAB,
                                       P_DIS_FLWSH_PARAM_ASSG_ID OUT DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ASSIGNMENT_ID%TYPE,
                                       P_LOCATION_ID             IN VARCHAR2,
                                       P_PHYSICAL_LOCATION_ID    IN VARCHAR2,
                                       P_USER_MRNO               IN VARCHAR2,
                                       P_OBJECT_CODE             IN VARCHAR2,
                                       P_STOP                    OUT VARCHAR2,
                                       P_ALERT_TEXT              OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_PARAM_ASSG_LCK(P_TAB_DATA   IN OUT DIS_FLWSH_PARAM_ASSG_TAB,
                                       P_STOP       OUT VARCHAR2,
                                       P_ALERT_TEXT OUT VARCHAR2);
  PROCEDURE P_DIS_FLWSH_PARAM_ASSG_UPD(P_TAB_DATA   IN DIS_FLWSH_PARAM_ASSG_TAB,
                                       P_STOP       OUT VARCHAR2,
                                       P_ALERT_TEXT OUT VARCHAR2);
  PROCEDURE P_DIS_FLWSH_PARAM_ASSG_DEL(P_TAB_DATA   IN DIS_FLWSH_PARAM_ASSG_TAB,
                                       P_STOP       OUT VARCHAR2,
                                       P_ALERT_TEXT OUT VARCHAR2);
END;
```

### DEFINITIONS.PKG_DIS_FLWSH_PARAMS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DIS_FLWSH_PARAMS IS

  -- AUTHOR  : RAZAHASSAN
  -- CREATED : 12/10/2018 11:28:24 AM
  -- PURPOSE :

  TYPE DIS_FLWSH_PARAMS_RECORD IS RECORD(
    DIS_FLWSH_PARAM_ID    DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
    PARAM_NAME            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
    SHORT_CODE            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
    PARAM_DESCRIPTION     DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_DESCRIPTION%TYPE,
    ACTIVE_FLAG           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ACTIVE_FLAG%TYPE,
    RESTRICT_MANUAL_ENTRY DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.RESTRICT_MANUAL_ENTRY%TYPE,
    SELECT_CLAUSE         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SELECT_CLAUSE%TYPE,
    FROM_CLAUSE           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.FROM_CLAUSE%TYPE,
    WHERE_CLAUSE          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.WHERE_CLAUSE%TYPE,
    REMARKS               DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.REMARKS%TYPE,
    --FLWSH_SETUP_ID        DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.FLWSH_SETUP_ID%TYPE,
    CATEGORY_CODE     DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.CATEGORY_CODE%TYPE,
    CATEGORY_DESC     ICU.SCORE_PARAMETERS.DESCRIPTION%TYPE,
    NOTE_CLAUSE       DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.NOTE_CLAUSE%TYPE,
    ORDER_BY          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ORDER_BY%TYPE,
    PATH_PARAMETER_ID DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PATH_PARAMETER_ID%TYPE,
    PATH_TEST_ID      DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PATH_TEST_ID%TYPE,
    PARAM_TYPE        DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_TYPE%TYPE);

  TYPE DIS_FLWSH_PARAMS_CUR IS REF CURSOR RETURN DIS_FLWSH_PARAMS_RECORD;
  TYPE DIS_FLWSH_PARAMS_TAB IS TABLE OF DIS_FLWSH_PARAMS_RECORD INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_PARAMS_REFCUR(DIS_FLWSH_PARAMS_DATA   IN OUT DIS_FLWSH_PARAMS_CUR,
                                      P_PARAM_NAME            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
                                      P_SHORT_CODE            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
                                      P_PARAM_DESCRIPTION     DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_DESCRIPTION%TYPE,
                                      P_ACTIVE_FLAG           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ACTIVE_FLAG%TYPE,
                                      P_RESTRICT_MANUAL_ENTRY DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.RESTRICT_MANUAL_ENTRY%TYPE,
                                      P_CATEGORY              ICU.SCORE_PARAMETERS.DESCRIPTION%TYPE,
                                      P_PARAM_TYPE            DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_TYPE%TYPE,
                                      P_SELECT_CLAUSE         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SELECT_CLAUSE%TYPE,
                                      P_FROM_CLAUSE           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.FROM_CLAUSE%TYPE,
                                      P_NOTE_CLAUSE           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.NOTE_CLAUSE%TYPE,
                                      P_WHERE_CLAUSE          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.WHERE_CLAUSE%TYPE,
                                      P_PATH_PARAMETER_ID     DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PATH_PARAMETER_ID%TYPE,
                                      P_PATH_TEST_ID          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PATH_TEST_ID%TYPE,
                                      P_DIS_FLWSH_PARAM_ID    DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
                                      P_ORDER_BY              DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ORDER_BY%TYPE);

  PROCEDURE P_DIS_FLWSH_PARAMS_INSERT(P_TAB_DATA             IN DIS_FLWSH_PARAMS_TAB,
                                      P_DIS_FLWSH_PARAM_ID   OUT DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
                                      P_LOCATION_ID          IN VARCHAR2,
                                      P_PHYSICAL_LOCATION_ID IN VARCHAR2,
                                      P_USER_MRNO            IN VARCHAR2,
                                      P_OBJECT_CODE          IN VARCHAR2,
                                      P_STOP                 OUT VARCHAR2,
                                      P_ALERT_TEXT           OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_PARAMS_LOCK(P_TAB_DATA   IN OUT DIS_FLWSH_PARAMS_TAB,
                                    P_STOP       OUT VARCHAR2,
                                    P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_PARAMS_UPDATE(P_TAB_DATA   IN DIS_FLWSH_PARAMS_TAB,
                                      P_STOP       OUT VARCHAR2,
                                      P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_PARAMS_DELETE(P_TAB_DATA   IN DIS_FLWSH_PARAMS_TAB,
                                      P_STOP       OUT VARCHAR2,
                                      P_ALERT_TEXT OUT VARCHAR2);

END;
```

### DEFINITIONS.PKG_DIS_FLWSH_SETUP_CUST
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DIS_FLWSH_SETUP_CUST IS

  -- AUTHOR  : RAZAHASSAN
  -- CREATED : 05/14/2018 09:45:33 PM
  -- PURPOSE :

  TYPE DIS_FLWSH_STP_RECORD IS RECORD(
    CUST_FLWSH_SETUP_ID DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.CUST_FLWSH_SETUP_ID%TYPE,
    FLWSH_SETUP_ID      DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.FLWSH_SETUP_ID%TYPE,
    SETUP_NAME          DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_NAME%TYPE,
    SETUP_DESCRIPTION   DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_DESCRIPTION%TYPE,
    SETUP_USER_MRNO     DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_USER_MRNO%TYPE,
    USER_NAME           SECURITY.USERS.FULL_NAME%TYPE,
    DEFAULT_FLAG        DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DEFAULT_FLAG%TYPE,
    LOCATION_ID         DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.LOCATION_ID%TYPE,
    CUST_USER_MRNO      DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.CUST_USER_MRNO%TYPE,
    ACTIVE              DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.ACTIVE%TYPE
    -----------------------------------------------------------
    );

  TYPE DIS_FLWSH_STP_CUR IS REF CURSOR RETURN DIS_FLWSH_STP_RECORD;
  TYPE DIS_FLWSH_STP_TAB IS TABLE OF DIS_FLWSH_STP_RECORD INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_CUST_STP_REFCUR(DIS_FLWSH_STP_DATA    IN OUT DIS_FLWSH_STP_CUR,
                                        P_FLWSH_SETUP_CUST_ID DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                        P_SETUP_NAME          DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_NAME%TYPE,
                                        P_ACTIVE              DEFINITIONS.DISEASE_FLOWSHEET_SETUP.ACTIVE_FLAG%TYPE,
                                        P_DEFAULT_FLAG        DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DEFAULT_FLAG%TYPE,
                                        P_SETUP_USER_MRNO     DEFINITIONS.DISEASE_FLOWSHEET_SETUP.SETUP_USER_MRNO%TYPE,
                                        P_SETUP_USER_NAME     DEFINITIONS.DOCTOR.NAME%TYPE);

  PROCEDURE P_DIS_FLWSH_CUST_STP_INSERT(P_TAB_DATA             IN DIS_FLWSH_STP_TAB,
                                        P_CUST_FLWSH_SETUP_ID  OUT DEFINITIONS.DISEASE_FLOWSHEET_SETUP_CUST.CUST_FLWSH_SETUP_ID%TYPE,
                                        P_LOCATION_ID          IN VARCHAR2,
                                        P_PHYSICAL_LOCATION_ID IN VARCHAR2,
                                        P_USER_MRNO            IN VARCHAR2,
                                        P_OBJECT_CODE          IN VARCHAR2,
                                        P_STOP                 OUT VARCHAR2,
                                        P_ALERT_TEXT           OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_CUST_STP_LOCK(P_TAB_DATA    IN OUT DIS_FLWSH_STP_TAB,
                                      P_OBJECT_CODE IN VARCHAR2,
                                      P_USER_MRNO   IN VARCHAR2,
                                      P_STOP        OUT VARCHAR2,
                                      P_ALERT_TEXT  OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_CUST_STP_UPDATE(P_TAB_DATA    IN DIS_FLWSH_STP_TAB,
                                        P_OBJECT_CODE IN VARCHAR2,
                                        P_USER_MRNO   IN VARCHAR2,
                                        P_STOP        OUT VARCHAR2,
                                        P_ALERT_TEXT  OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_CUST_STP_DELETE(P_TAB_DATA    IN DIS_FLWSH_STP_TAB,
                                        P_OBJECT_CODE IN VARCHAR2,
                                        P_USER_MRNO   IN VARCHAR2,
                                        P_STOP        OUT VARCHAR2,
                                        P_ALERT_TEXT  OUT VARCHAR2);

END;
```

### DEFINITIONS.PKG_DIS_FLWSH_TRX_N
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DIS_FLWSH_TRX_N IS

  -- AUTHOR  : RAZAHASSAN
  -- CREATED : 12/1/2018 09:30:33 PM
  -- PURPOSE :
  TYPE DIS_FLWSH_TRX_MON_REC IS RECORD(
    REPORT_DATE DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.REPORT_DATE%TYPE,
    MRNO        DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE);

  TYPE DIS_FLWSH_MON_CUR IS REF CURSOR RETURN DIS_FLWSH_TRX_MON_REC;
  TYPE DIS_FLWSH_MON_CUR_APEX IS TABLE OF DIS_FLWSH_TRX_MON_REC;

  PROCEDURE P_DIS_FLWSH_TRX_MON_REFCUR(DIS_FLWSH_MON_DATA IN OUT DIS_FLWSH_MON_CUR,
                                       P_MRNO             DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE,
                                       P_DISEASE_ID       DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DISEASE_ID%TYPE,
                                       P_FLWSH_SETUP_ID   DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                       P_USER_MRNO        VARCHAR2,
                                       P_LOCATION_ID      VARCHAR2,
                                       P_TERMINAL         VARCHAR2,
                                       P_OBJECT_OBJECT    VARCHAR2);

  TYPE DIS_FLWSH_TRX_RECORD IS RECORD(
    DISEASE_FLOW_TRX_ID DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DISEASE_FLOW_TRX_ID%TYPE,
    DIS_FLWSH_PARAM_ID  DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DIS_FLWSH_PARAM_ID%TYPE,
    MRNO                DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE,
    REPORT_DATE         DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.REPORT_DATE%TYPE,
    RESULT_VALUE        DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.RESULT_VALUE%TYPE,
    REMARKS             DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.REMARKS%TYPE,
    LOCATION_ID         DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.REMARKS%TYPE,
    PARAM_NAME          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
    SHORT_CODE          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
    ASSIGNMENT_ID       DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ASSIGNMENT_ID%TYPE,
    PARAM_TYPE          DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_TYPE%TYPE
    -----------------------------------------------------------
    );

  TYPE DIS_FLWSH_TRX_CUR IS REF CURSOR RETURN DIS_FLWSH_TRX_RECORD;

  TYPE DIS_FLWSH_TRX_TAB IS TABLE OF DIS_FLWSH_TRX_RECORD INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_TRX_REFCUR(DIS_FLWSH_TRX_DATA IN OUT DIS_FLWSH_TRX_CUR,
                                   P_MRNO             DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE,
                                   P_REPORT_DATE      DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.REPORT_DATE%TYPE,
                                   P_ASSIGNMENT_ID    DEFINITIONS.DIS_FLWSH_PARAM_ASSG.ASSIGNMENT_ID%TYPE,
                                   P_USER_MRNO        DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.USER_MRNO%TYPE);

  PROCEDURE P_DIS_FLWSH_TRX_INSERT(P_TAB_DATA             IN DIS_FLWSH_TRX_TAB,
                                   P_FLWSH_TRX_ID         OUT DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DISEASE_FLOW_TRX_ID%TYPE,
                                   P_LOCATION_ID          IN VARCHAR2,
                                   P_PHYSICAL_LOCATION_ID IN VARCHAR2,
                                   P_USER_MRNO            IN VARCHAR2,
                                   P_OBJECT_CODE          IN VARCHAR2,
                                   P_STOP                 OUT VARCHAR2,
                                   P_ALERT_TEXT           OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_TRX_LOCK(P_TAB_DATA   IN OUT DIS_FLWSH_TRX_TAB,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_TRX_UPDATE(P_TAB_DATA   IN DIS_FLWSH_TRX_TAB,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_TRX_DELETE(P_TAB_DATA   IN DIS_FLWSH_TRX_TAB,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  TYPE DIS_FLWSH_DOC_REC IS RECORD(
    ARCHIVE_ID             DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.ARCHIVE_ID%TYPE,
    DISEASE_FLOW_TRX_ID    DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.DISEASE_FLOW_TRX_ID%TYPE,
    DOC_SR_NO              DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.DOC_SR_NO%TYPE,
    DOC_ATTACHED           VARCHAR2(1),
    REMARKS                DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.REMARKS%TYPE,
    MRNO                   DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.MRNO%TYPE,
    DOC_ARCHIVE_DATE       DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.DOC_ARCHIVE_DATE%TYPE,
    DOC_ARCHIVER_ID        DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.DOC_ARCHIVER_ID%TYPE,
    DOC_ARCHIVE_LOC_ID     DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.DOC_ARCHIVE_LOC_ID%TYPE,
    DOCUMENT_SCANNED       PATIENTCHART.DOCUMENT_SCANNING.DOCUMENT_SCANNED%TYPE,
    SCAN_DATE              PATIENTCHART.DOCUMENT_SCANNING.SCAN_DATE%TYPE,
    INDEXING               PATIENTCHART.DOCUMENT_SCANNING.INDEXING%TYPE,
    INDEXING_DATE          PATIENTCHART.DOCUMENT_SCANNING.INDEXING_DATE%TYPE,
    DOCUMENT_SERVER        PATIENTCHART.DOCUMENT_SCANNING.DOCUMENT_SERVER%TYPE,
    DOCUMENT_PATH          PATIENTCHART.DOCUMENT_SCANNING.DOCUMENT_PATH%TYPE,
    SCANNER_ID             PATIENTCHART.DOCUMENT_SCANNING.SCANNER_ID%TYPE,
    INDEXER_ID             PATIENTCHART.DOCUMENT_SCANNING.INDEXER_ID%TYPE,
    BACKUP_SERVER          PATIENTCHART.DOCUMENT_SCANNING.BACKUP_SERVER%TYPE,
    TOTAL_PAGES            PATIENTCHART.DOCUMENT_SCANNING.TOTAL_PAGES%TYPE,
    FILE_SIZE              PATIENTCHART.DOCUMENT_SCANNING.FILE_SIZE%TYPE,
    HARDDISK_SERVER        PATIENTCHART.DOCUMENT_SCANNING.HARDDISK_SERVER%TYPE,
    DOCUMENT_NAME          PATIENTCHART.DOCUMENT_SCANNING.DOCUMENT_NAME%TYPE,
    SRNO                   PATIENTCHART.DOCUMENT_SCANNING.SRNO%TYPE,
    TX_FROM_DATE           PATIENTCHART.DOCUMENT_SCANNING.TX_FROM_DATE%TYPE,
    TX_TO_DATE             PATIENTCHART.DOCUMENT_SCANNING.TX_TO_DATE%TYPE,
    TRANSFERRED            PATIENTCHART.DOCUMENT_SCANNING.TRANSFERRED%TYPE,
    SCAN_LOCATION_ID       PATIENTCHART.DOCUMENT_SCANNING.SCAN_LOCATION_ID%TYPE,
    DOCUMENT_CREATION_DATE PATIENTCHART.DOCUMENT_SCANNING.DOCUMENT_CREATION_DATE%TYPE,
    BACKUP_SERVER_1        PATIENTCHART.DOCUMENT_SCANNING.BACKUP_SERVER_1%TYPE,
    BACKUP_SERVER_2        PATIENTCHART.DOCUMENT_SCANNING.BACKUP_SERVER_2%TYPE,
    SELECT_DOC             VARCHAR2(1));

  TYPE DIS_FLWSH_DOC_CUR IS REF CURSOR RETURN DIS_FLWSH_DOC_REC;

  TYPE DIS_FLWSH_DOC_TAB IS TABLE OF DIS_FLWSH_DOC_REC INDEX BY BINARY_INTEGER;

  PROCEDURE P_DIS_FLWSH_DOC_REFCUR(DIS_FLWSH_DOC_DATA    IN OUT DIS_FLWSH_DOC_CUR,
                                   P_MRNO                DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE,
                                   P_DISEASE_FLOW_TRX_ID DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DISEASE_FLOW_TRX_ID%TYPE);

  PROCEDURE P_DIS_FLWSH_DOC_INSERT(P_TAB_DATA   IN DIS_FLWSH_DOC_TAB,
                                   P_ARCHIVE_ID OUT DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.ARCHIVE_ID%TYPE,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_DOC_UPDATE(P_TAB_DATA            IN DIS_FLWSH_DOC_TAB,
                                   P_DISEASE_FLOW_TRX_ID DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DISEASE_FLOW_TRX_ID%TYPE,
                                   P_ARCHIVE_ID          OUT DEFINITIONS.DIS_FLWSH_DOC_ARCHIVE.ARCHIVE_ID%TYPE,
                                   P_STOP                OUT VARCHAR2,
                                   P_ALERT_TEXT          OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_DOC_LOCK(P_TAB_DATA   IN OUT DIS_FLWSH_DOC_TAB,
                                 P_STOP       OUT VARCHAR2,
                                 P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE P_DIS_FLWSH_DOC_DELETE(P_TAB_DATA   IN DIS_FLWSH_DOC_TAB,
                                   P_STOP       OUT VARCHAR2,
                                   P_ALERT_TEXT OUT VARCHAR2);

  TYPE DIS_FLWSH_ITEMS_REC IS RECORD(
    SR                 NUMBER,
    PARAM_NAME         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
    SHORT_CODE         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
    DIS_FLWSH_PARAM_ID DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
    CATEGORY_CODE      ICU.SCORE_CATEGORY.DESCRIPTION%TYPE,
    PARAM_TYPE         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_TYPE%TYPE,
    DESCRIPTION        ICU.SCORE_PARAMETERS.DESCRIPTION%TYPE,
    ORDER_BY           DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.ORDER_BY%TYPE);

  TYPE DIS_FLWSH_ITEMS_CUR IS REF CURSOR RETURN DIS_FLWSH_ITEMS_REC;

  TYPE DIS_FLWSH_ITEMS_TAB IS TABLE OF DIS_FLWSH_ITEMS_REC;

  TYPE DIS_FLWSH_PARAMS_M_REC IS RECORD(
    MRNO               DEFINITIONS.DIS_FLWSH_PARAM_MASTER.MRNO%TYPE,
    DIS_FLWSH_PARAM_ID DEFINITIONS.DIS_FLWSH_PARAM_MASTER.DIS_FLWSH_PARAM_ID%TYPE,
    LAST_REFRESH_DATE  DEFINITIONS.DIS_FLWSH_PARAM_MASTER.LAST_REFRESH_DATE%TYPE,
    REFERENCE_KEY      DEFINITIONS.DIS_FLWSH_PARAM_MASTER.REFERENCE_KEY%TYPE,
    PARAM_TYPE         DEFINITIONS.DIS_FLWSH_PARAM_MASTER.PARAM_TYPE%TYPE);

  TYPE DIS_FLWSH_PARAMS_M_TAB IS TABLE OF DIS_FLWSH_PARAMS_M_REC;

  /*TYPE DIS_FLWSH_PARAMS_D_REC IS RECORD(
    MRNO               DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.MRNO%TYPE,
    DIS_FLWSH_PARAM_ID DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.DIS_FLWSH_PARAM_ID%TYPE,
    REFERENCE_KEY      DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.REFERENCE_KEY%TYPE,
    PARAM_TYPE         DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.PARAM_TYPE%TYPE,
    RESULT_VALUE       DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.RESULT_VALUE%TYPE,
    RESULT_DATE        DEFINITIONS.DIS_FLWSH_PARAM_DETAIL.RESULT_DATE%TYPE);
  TYPE DIS_FLWSH_PARAMS_D_TAB IS TABLE OF DIS_FLWSH_PARAMS_D_REC INDEX BY BINARY_INTEGER;*/
  PROCEDURE P_REFRESH_DATA(P_MRNO        VARCHAR2,
                           P_USER_MRNO   VARCHAR2,
                           P_TERMINAL    VARCHAR,
                           P_LOCATION_ID VARCHAR2,
                           P_ALERT_TEXT  OUT VARCHAR2,
                           P_STOP        OUT CHAR);

  FUNCTION GET_RESULT_VALUE(P_SELECT_CLAUSE VARCHAR2,
                            P_FROM_CLAUSE   VARCHAR2,
                            P_WHERE_CLAUSE  VARCHAR2,
                            P_PARAM_TYPE    IN VARCHAR2,
                            P_REFERENCE_KEY IN VARCHAR2,
                            P_MRNO          IN VARCHAR2,
                            P_RPT_DATE      IN DATE) RETURN VARCHAR2;

  /*  PROCEDURE P_REFRESH_DATA(P_USER_MRNO   VARCHAR2,
  P_TERMINAL    VARCHAR,
  P_LOCATION_ID VARCHAR2,
  P_ALERT_TEXT  OUT VARCHAR2,
  P_STOP        OUT CHAR);*/
  FUNCTION F_PARAMETER_ALREADY_EXISTS(P_MRNO               VARCHAR2,
                                      P_RESULT_DATE        DATE,
                                      P_DIS_FLWSH_PARAM_ID VARCHAR2,
                                      P_PARAM_TYPE         VARCHAR2)
    RETURN VARCHAR2;

  TYPE DIS_FLWSH_TRX_MON_D_REC IS RECORD(
    DIS_FLWSH_PARAM_ID DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.DIS_FLWSH_PARAM_ID%TYPE,
    PARAM_NAME         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.PARAM_NAME%TYPE,
    SHORT_CODE         DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.SHORT_CODE%TYPE,
    MRNO               DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE);

  TYPE DIS_FLWSH_MON_D_CUR IS REF CURSOR RETURN DIS_FLWSH_TRX_MON_D_REC;

  PROCEDURE P_DIS_FLWSH_TRX_MON_REFCUR_D(DIS_FLWSH_MON_DATA   IN OUT DIS_FLWSH_MON_D_CUR,
                                         P_MRNO               DEFINITIONS.DISEASE_FLOWSHEET_TRANSACTIONS.MRNO%TYPE,
                                         P_DISEASE_ID         DEFINITIONS.DISEASE_FLOWSHEET_SETUP.DISEASE_ID%TYPE,
                                         P_FLWSH_SETUP_ID     DEFINITIONS.DISEASE_FLOWSHEET_SETUP.FLWSH_SETUP_ID%TYPE,
                                         P_DIS_FLWSH_PARAM_ID DEFINITIONS.DISEASE_FLOWSHEET_PARAMS.DIS_FLWSH_PARAM_ID%TYPE,
                                         P_USER_MRNO          VARCHAR2,
                                         P_LOCATION_ID        VARCHAR2,
                                         P_TERMINAL           VARCHAR2,
                                         P_OBJECT_OBJECT      VARCHAR2);

END;
```

### DEFINITIONS.PKG_DOCTOR_EXTERNAL
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_DOCTOR_EXTERNAL IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : FIAZ AHMAD
  -- Created : 26-Feb-2016 09:34
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
  FUNCTION F_SELECT(P_DOCTOR_ID      IN DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.DOCTOR_EXTERNAL%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DOCTOR_ID      IN DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.DOCTOR_EXTERNAL%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DOCTOR_ID      IN DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.DOCTOR_EXTERNAL%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DOCTOR_ID      IN DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_DOCTOR_EXTERNAL;
```

### DEFINITIONS.PKG_EXTERNAL_DOCTOR_DETAIL
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_EXTERNAL_DOCTOR_DETAIL IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : FIAZ AHMAD
  -- Created : 29-Feb-2016 11:29
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
  FUNCTION F_SELECT(P_DOCTOR_ID      IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DOCTOR_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.SECTION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.EXTERNAL_DOCTOR_DETAIL%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DOCTOR_ID      IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DOCTOR_ID%TYPE,
                  P_DEPARTMENT_ID  IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DEPARTMENT_ID%TYPE,
                  P_SECTION_ID     IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.SECTION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.EXTERNAL_DOCTOR_DETAIL%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DOCTOR_ID      IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DOCTOR_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.SECTION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.EXTERNAL_DOCTOR_DETAIL%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DOCTOR_ID      IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DOCTOR_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.SECTION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_EXTERNAL_DOCTOR_DETAIL;
```

### DEFINITIONS.PKG_FILES_SERVERS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FILES_SERVERS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : HAFIZ ABRAR AHMED
  -- Created : 22-Mar-2016 10:34
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

  PROCEDURE P_NEW(P_SERVER_PATH        IN VARCHAR2,
                  P_SERVER_NAME        IN VARCHAR2,
                  P_SERVER_TYPE_ID     IN CHAR,
                  P_SERVER_LOCATION_ID IN VARCHAR2,
                  P_REMARKS            IN VARCHAR2,
                  P_ACTIVE             IN CHAR,
                  P_IGNORE_DUPLICATE   IN CHAR DEFAULT NULL,
                  P_LOCATION_ID        IN VARCHAR2,
                  P_CALLING_OBJECT     IN VARCHAR2,
                  P_CALLING_USER       IN VARCHAR2,
                  P_CALLING_EVENT      IN VARCHAR2,
                  P_SERVER_ID          OUT CHAR,
                  P_STOP               OUT CHAR,
                  P_ERROR              OUT VARCHAR2);
  -- ******************************************************************************************************--

  FUNCTION F_SELECT(P_SERVER_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.FILES_SERVERS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_SELECT(P_ACCESS_PATH    IN DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
                    P_ROW            OUT DEFINITIONS.FILES_SERVERS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_LOCK(P_SERVER_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.FILES_SERVERS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT 'N',
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_UPDATE(P_SERVER_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.FILES_SERVERS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_DELETE(P_SERVER_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--

  FUNCTION F_GET_FILE_SERVER_ID(P_SERVER_PATH        IN VARCHAR2,
                                P_SERVER_NAME        IN VARCHAR2,
                                P_SERVER_TYPE_ID     IN VARCHAR2,
                                P_SERVER_LOCATION_ID IN VARCHAR2,
                                P_REMARKS            IN VARCHAR2,
                                P_ACTIVE             IN CHAR,
                                P_LOCATION_ID        IN VARCHAR2,
                                P_CALLING_OBJECT     IN VARCHAR2,
                                P_CALLING_USER       IN VARCHAR2,
                                P_CALLING_EVENT      IN VARCHAR2,
                                P_ERROR              OUT VARCHAR2)
    RETURN CHAR;
  -- ******************************************************************************************************--

END PKG_FILES_SERVERS;
```

### DEFINITIONS.PKG_FILES_SERVERS_SYNC_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FILES_SERVERS_SYNC_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : IRFAN  ALI
  -- Created : 06-Sep-2021 15:19
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
  FUNCTION F_SELECT(P_SOURCE_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.SOURCE_SERVER_ID%TYPE,
                    P_TARGET_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.TARGET_SERVER_ID%TYPE,
                    P_ROW              OUT DEFINITIONS.FILES_SERVERS_SYNC_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA   IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SOURCE_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.SOURCE_SERVER_ID%TYPE,
                  P_TARGET_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.TARGET_SERVER_ID%TYPE,
                  P_IGNORE_NO_DATA   IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID      IN VARCHAR2,
                  P_CALLING_OBJECT   IN VARCHAR2,
                  P_CALLING_USER     IN VARCHAR2,
                  P_CALLING_EVENT    IN VARCHAR2,
                  P_ROWID            OUT ROWID,
                  P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.FILES_SERVERS_SYNC_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SOURCE_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.SOURCE_SERVER_ID%TYPE,
                    P_TARGET_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.TARGET_SERVER_ID%TYPE,
                    P_ROW              IN OUT DEFINITIONS.FILES_SERVERS_SYNC_SETUP%ROWTYPE,
                    P_UPDATE_NULL      IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA   IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SOURCE_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.SOURCE_SERVER_ID%TYPE,
                    P_TARGET_SERVER_ID IN DEFINITIONS.FILES_SERVERS_SYNC_SETUP.TARGET_SERVER_ID%TYPE,
                    P_IGNORE_NO_DATA   IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_FILES_SERVERS_SYNC_SETUP;
```

### DEFINITIONS.PKG_FILES_SERVERS_TYPES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FILES_SERVERS_TYPES IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : HAFIZ ABRAR AHMED
  -- Created : 22-Mar-2016 10:17
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
  FUNCTION F_SELECT(P_SERVER_TYPE_ID IN DEFINITIONS.FILES_SERVERS_TYPES.SERVER_TYPE_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.FILES_SERVERS_TYPES%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SERVER_TYPE_ID IN DEFINITIONS.FILES_SERVERS_TYPES.SERVER_TYPE_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.FILES_SERVERS_TYPES%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SERVER_TYPE_ID IN DEFINITIONS.FILES_SERVERS_TYPES.SERVER_TYPE_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.FILES_SERVERS_TYPES%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SERVER_TYPE_ID IN DEFINITIONS.FILES_SERVERS_TYPES.SERVER_TYPE_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_FILES_SERVERS_TYPES;
```

### DEFINITIONS.PKG_FILES_TYPES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FILES_TYPES IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : HAFIZ ABRAR AHMED
  -- Created : 22-Mar-2016 10:47
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
  FUNCTION F_SELECT(P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.FILES_TYPES%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.FILES_TYPES%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.FILES_TYPES%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_FILES_TYPES;
```

### DEFINITIONS.PKG_FILES_TYPES_DET
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FILES_TYPES_DET IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : HAFIZ ABRAR AHMED
  -- Created : 01-Apr-2016 15:48
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
  FUNCTION F_SELECT(P_TYPE_ID        IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.FILES_TYPES_DET%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_TYPE_ID        IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                  P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.FILES_TYPES_DET%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_TYPE_ID        IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.FILES_TYPES_DET%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_TYPE_ID        IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                    P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_FILES_TYPES_DET;
```

### DEFINITIONS.PKG_FOOD_ALERGIES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_FOOD_ALERGIES IS

	FUNCTION F_GET_DESCRIPTION(P_FOOD_ID DEFINITIONS.FOOD_ALERGIES.FOOD_ID%TYPE)
		RETURN DEFINITIONS.FOOD_ALERGIES.DESCRIPTION%TYPE;

END;
```

### DEFINITIONS.PKG_GENDER_MAP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_GENDER_MAP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  :Faran Munawar Ghouri
  -- Created : 27-Aug-2018 12:03
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
  FUNCTION F_SELECT(P_SEX_ID         IN DEFINITIONS.GENDER_MAP.SEX_ID%TYPE,
                    P_MAP_SEXID      IN DEFINITIONS.GENDER_MAP.MAP_SEXID%TYPE,
                    P_ROW            OUT DEFINITIONS.GENDER_MAP%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SEX_ID         IN DEFINITIONS.GENDER_MAP.SEX_ID%TYPE,
                  P_MAP_SEXID      IN DEFINITIONS.GENDER_MAP.MAP_SEXID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.GENDER_MAP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SEX_ID         IN DEFINITIONS.GENDER_MAP.SEX_ID%TYPE,
                    P_MAP_SEXID      IN DEFINITIONS.GENDER_MAP.MAP_SEXID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.GENDER_MAP%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SEX_ID         IN DEFINITIONS.GENDER_MAP.SEX_ID%TYPE,
                    P_MAP_SEXID      IN DEFINITIONS.GENDER_MAP.MAP_SEXID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_GENDER_MAP;
```

### DEFINITIONS.PKG_ICD_COMMON
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ICD_COMMON IS

  -- AUTHOR  : MUHAMMAD YASAR NASEER
  -- CREATED : 03/09/2015 16:04:54 PM
  -- PURPOSE : TO CREATE ICD RELATED FUNCTIONS, PROCEDURES AND OBJECTS
  -------------------------------------------------------------------------------------------------------
  FUNCTION GET_ICD_DESCRIPTION(P_ICDNO           IN DEFINITIONS.ICD.ICDNO%TYPE,
                               P_LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_ORGANIZATION_ID DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE)
    RETURN VARCHAR2;

  -------------------------------------------------------------------------------------------------------
  -- AUTHOR  : MUHAMMAD ISLAM
  -- CREATED : 21/11/2016
  -- PURPOSE : TO CHECK EITHER NASO ENDOSCOPY PROCEDURE DONE ON THIS PATIENT WITHIN 30 DAYS OR NOT
  FUNCTION F_PAT_NASO_ENDOSCOPY_DONE(P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_DATE           IN DATE,
                                     P_CALLING_USER   IN REGISTRATION.PATIENT.MRNO%TYPE,
                                     P_CALLING_OBJECT IN VARCHAR2)
    RETURN BOOLEAN;

  ---------------------------------------------------------------------
  -- AUTHOR  : MUHAMMAD ISLAM
  -- CREATED : 21/11/2016
  -- PURPOSE : TO CHECK EITHER PATIENT HAS DIABETIC OR NOT
  FUNCTION F_CHECK_PAT_DIABETEC(P_MRNO           IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_CALLING_USER   IN REGISTRATION.PATIENT.MRNO%TYPE,
                                P_CALLING_OBJECT IN VARCHAR2) RETURN BOOLEAN;

  -----------------------------------
  -- AUTHOR  : ALLAH RAKHA
  -- CREATED : 06/11/2019
  -- PURPOSE : TO GET THE ICD DESCRIPTION DATE WISE  
  FUNCTION GET_ICD_DESCRIPTION(P_ICDNO IN DEFINITIONS.ICD.ICDNO%TYPE,
                               P_DATE  IN DEFINITIONS.ICD.TRN_DATE%TYPE)
    RETURN DEFINITIONS.ICD.LONG_DESC%TYPE;
FUNCTION EXCLUDE_FROM_ICD_VERIFY (P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
  RETURN VARCHAR2;
END PKG_ICD_COMMON;
```

### DEFINITIONS.PKG_INQUIRY_EXTENSION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_INQUIRY_EXTENSION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 09:51
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
  FUNCTION F_SELECT(P_DEPARTMENT_ID  IN DEFINITIONS.INQUIRY_EXTENSION.DEPARTMENT_ID%TYPE,
                    P_EXTENSION_TYPE IN DEFINITIONS.INQUIRY_EXTENSION.EXTENSION_TYPE%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INQUIRY_EXTENSION.LOCATION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.INQUIRY_EXTENSION%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DEPARTMENT_ID  IN DEFINITIONS.INQUIRY_EXTENSION.DEPARTMENT_ID%TYPE,
                  P_EXTENSION_TYPE IN DEFINITIONS.INQUIRY_EXTENSION.EXTENSION_TYPE%TYPE,
                  P_LOCATION_ID    IN DEFINITIONS.INQUIRY_EXTENSION.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.INQUIRY_EXTENSION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DEPARTMENT_ID  IN DEFINITIONS.INQUIRY_EXTENSION.DEPARTMENT_ID%TYPE,
                    P_EXTENSION_TYPE IN DEFINITIONS.INQUIRY_EXTENSION.EXTENSION_TYPE%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INQUIRY_EXTENSION.LOCATION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.INQUIRY_EXTENSION%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DEPARTMENT_ID  IN DEFINITIONS.INQUIRY_EXTENSION.DEPARTMENT_ID%TYPE,
                    P_EXTENSION_TYPE IN DEFINITIONS.INQUIRY_EXTENSION.EXTENSION_TYPE%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INQUIRY_EXTENSION.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_INQUIRY_EXTENSION;
```

### DEFINITIONS.PKG_INSTRUCTIONS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_INSTRUCTIONS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 09:54
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
  FUNCTION F_SELECT(P_SR_NO          IN DEFINITIONS.INSTRUCTIONS.SR_NO%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INSTRUCTIONS.LOCATION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.INSTRUCTIONS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SR_NO          IN DEFINITIONS.INSTRUCTIONS.SR_NO%TYPE,
                  P_LOCATION_ID    IN DEFINITIONS.INSTRUCTIONS.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.INSTRUCTIONS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SR_NO          IN DEFINITIONS.INSTRUCTIONS.SR_NO%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INSTRUCTIONS.LOCATION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.INSTRUCTIONS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SR_NO          IN DEFINITIONS.INSTRUCTIONS.SR_NO%TYPE,
                    P_LOCATION_ID    IN DEFINITIONS.INSTRUCTIONS.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_INSTRUCTIONS;
```

### DEFINITIONS.PKG_ITEM_PROPERTIES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ITEM_PROPERTIES IS
  FUNCTION GET_OBJECT_ITEM_ID RETURN NUMBER;
  PROCEDURE GET_OBJECT_NAME(P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                            P_OBJECT_DESC OUT DEFINITIONS.OBJECTS.DISPLAY_NAME%TYPE,
                            P_ALERT_TEXT  OUT VARCHAR2);
  PROCEDURE GET_ITEM_TYPE_NAME(P_ITEM_TYPE_ID   IN DEFINITIONS.ITEM_TYPES.TYPE_ID%TYPE,
                               P_ITEM_TYPE_DESC OUT DEFINITIONS.ITEM_TYPES.TYPE_NAME%TYPE,
                               P_ALERT_TEXT     OUT VARCHAR2);
  PROCEDURE GET_ITEM_PROPERTY_DESC(P_PROPERTY_ID   IN DEFINITIONS.ITEM_PROPERTY.PROPERTY_ID%TYPE,
                                   P_PROPERTY_DESC OUT DEFINITIONS.ITEM_PROPERTY.KEY_NAME%TYPE,
                                   P_ALERT_TEXT    OUT VARCHAR2);
  PROCEDURE GET_TERMINOLOGY_VALUE(P_TERM_ID    IN DEFINITIONS.TERMINOLOGY.TERM_ID%TYPE,
                                  P_TERM_DESC  OUT DEFINITIONS.TERMINOLOGY.TERM_NAME%TYPE,
                                  P_ALERT_TEXT OUT VARCHAR2);
  PROCEDURE GET_FIXED_VALUE(P_VALUE_KEY   IN DEFINITIONS.ITEM_PROPERTY_VALUES.VALUE_KEY%TYPE,
                            P_PROPERTY_ID IN DEFINITIONS.ITEM_PROPERTY.PROPERTY_ID%TYPE,
                            P_VALUE_DESC  OUT DEFINITIONS.ITEM_PROPERTY_VALUES.VALUE_DESC%TYPE,
                            P_ALERT_TEXT  OUT VARCHAR2);
  FUNCTION IS_BLOCK_ITEM_NAME(P_BLOCK_ITEM_NAME VARCHAR2) RETURN CHAR;
  FUNCTION GET_SETUP_VAL_COUNT(P_ITEM_ID     DEFINITIONS.ORG_WISE_OBJECT_ITEM_SETUP.ITEM_ID%TYPE,
                               P_PROPERTY_ID DEFINITIONS.ORG_WISE_OBJECT_ITEM_SETUP.PROPERTY_ID%TYPE)
    RETURN NUMBER;
  FUNCTION GET_PROPERTY_ID RETURN NUMBER;
  FUNCTION GET_PROPERTY_SERIAL_NO(P_PROPERTY_ID DEFINITIONS.ITEM_PROPERTY.PROPERTY_ID%TYPE)
    RETURN NUMBER;
  FUNCTION GET_ITEM_TYPE_ID RETURN NUMBER;
  FUNCTION GET_TERM_ID RETURN NUMBER;
END;
```

### DEFINITIONS.PKG_LOCATION_RADIOLOGY
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOCATION_RADIOLOGY IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 09:57
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
  FUNCTION F_SELECT(P_LOCATION_ID    IN DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.LOCATION_RADIOLOGY%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID    IN DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOCATION_RADIOLOGY%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.LOCATION_RADIOLOGY%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOCATION_RADIOLOGY;
```

### DEFINITIONS.PKG_LOCATION_SCHEMAS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOCATION_SCHEMAS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 10:30
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
  FUNCTION F_SELECT(P_LOCATION_ID    IN DEFINITIONS.LOCATION_SCHEMAS.LOCATION_ID%TYPE,
                    P_SCHEMA_ID      IN DEFINITIONS.LOCATION_SCHEMAS.SCHEMA_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.LOCATION_SCHEMAS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID    IN DEFINITIONS.LOCATION_SCHEMAS.LOCATION_ID%TYPE,
                  P_SCHEMA_ID      IN DEFINITIONS.LOCATION_SCHEMAS.SCHEMA_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOCATION_SCHEMAS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_SCHEMAS.LOCATION_ID%TYPE,
                    P_SCHEMA_ID      IN DEFINITIONS.LOCATION_SCHEMAS.SCHEMA_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.LOCATION_SCHEMAS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_SCHEMAS.LOCATION_ID%TYPE,
                    P_SCHEMA_ID      IN DEFINITIONS.LOCATION_SCHEMAS.SCHEMA_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOCATION_SCHEMAS;
```

### DEFINITIONS.PKG_LOCATION_WISE_CPT
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOCATION_WISE_CPT IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 12:59
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
  FUNCTION F_SELECT(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT.CPT_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.LOCATION_WISE_CPT%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT.LOCATION_ID%TYPE,
                  P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT.CPT_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOCATION_WISE_CPT%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT.CPT_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.LOCATION_WISE_CPT%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT.CPT_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOCATION_WISE_CPT;
```

### DEFINITIONS.PKG_LOC_HF_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOC_HF_SETUP AS
  ---------------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 07-01-2013
  -- Scope     :
  -- Purpose   : The following record type, table types will be used
  --             for dml of DEFINITIONS.LOC_HF_SETUP
  /******************************************************************************/
  TYPE LOC_HF_SETUP_REC IS RECORD(
    LOCATION_ID     DEFINITIONS.LOC_HF_SETUP.LOCATION_ID%TYPE,
    DESCRIPTION     DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    FROM_DATE       DEFINITIONS.LOC_HF_SETUP.FROM_DATE%TYPE,
    RPT_HF_SETUP_ID DEFINITIONS.LOC_HF_SETUP.RPT_HF_SETUP_ID%TYPE);

  TYPE LOC_HF_SETUP_TAB IS TABLE OF LOC_HF_SETUP_REC INDEX BY PLS_INTEGER;
  TYPE LOC_HF_SETUP_TB IS TABLE OF LOC_HF_SETUP_REC;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : The following pipelined function will return table of records
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  FUNCTION F_LOC_HF_SETUP_QRY(P_LOCATION_ID IN DEFINITIONS.LOC_HF_SETUP.LOCATION_ID%TYPE,
                              P_FROM_DATE   IN DEFINITIONS.LOC_HF_SETUP.FROM_DATE%TYPE)
    RETURN LOC_HF_SETUP_TB
    PIPELINED;
  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_QRY(P_LOCATION_ID IN DEFINITIONS.LOC_HF_SETUP.LOCATION_ID%TYPE,
                               P_FROM_DATE   IN DEFINITIONS.LOC_HF_SETUP.FROM_DATE%TYPE,
                               P_DATA        IN OUT LOC_HF_SETUP_TAB,
                               P_STOP        OUT VARCHAR2,
                               P_ALERT_TEXT  OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for validating data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN LOC_HF_SETUP_REC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_INS(P_DATA       IN OUT LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_LCK(P_DATA       IN OUT LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_UPD(P_DATA       IN OUT LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_LOC_HF_SETUP_DEL(P_DATA       IN OUT LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
END PKG_LOC_HF_SETUP;
```

### DEFINITIONS.PKG_LOC_WISE_CPT_DEPT_SECT
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOC_WISE_CPT_DEPT_SECT IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 13:10
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
  FUNCTION F_SELECT(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.CPT_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.SECTION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.LOCATION_ID%TYPE,
                  P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.CPT_ID%TYPE,
                  P_DEPARTMENT_ID  IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.DEPARTMENT_ID%TYPE,
                  P_SECTION_ID     IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.SECTION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.CPT_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.SECTION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID    IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.LOCATION_ID%TYPE,
                    P_CPT_ID         IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.CPT_ID%TYPE,
                    P_DEPARTMENT_ID  IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.DEPARTMENT_ID%TYPE,
                    P_SECTION_ID     IN DEFINITIONS.LOCATION_WISE_CPT_DEPT_SECT.SECTION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOC_WISE_CPT_DEPT_SECT;
```

### DEFINITIONS.PKG_LOC_WISE_PATIENT_TYPES
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOC_WISE_PATIENT_TYPES IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 13:17
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
  FUNCTION F_SELECT(P_LOCATION_ID     IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.LOCATION_ID%TYPE,
                    P_PATIENT_TYPE_ID IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.PATIENT_TYPE_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.LOCATION_WISE_PATIENT_TYPES%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID     IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.LOCATION_ID%TYPE,
                  P_PATIENT_TYPE_ID IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.PATIENT_TYPE_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOCATION_WISE_PATIENT_TYPES%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID     IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.LOCATION_ID%TYPE,
                    P_PATIENT_TYPE_ID IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.PATIENT_TYPE_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.LOCATION_WISE_PATIENT_TYPES%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID     IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.LOCATION_ID%TYPE,
                    P_PATIENT_TYPE_ID IN DEFINITIONS.LOCATION_WISE_PATIENT_TYPES.PATIENT_TYPE_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOC_WISE_PATIENT_TYPES;
```

### DEFINITIONS.PKG_LOC_WISE_PHARMACY_STORE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_LOC_WISE_PHARMACY_STORE IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Abdul Wadood
  -- Created : 01-Dec-2019 18:33
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
  FUNCTION F_SELECT(P_ORGANIZATION_ID      IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.PHYSICAL_LOCATION_ID%TYPE,
                    P_STORE_ID             IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.STORE_ID%TYPE,
                    P_ROW                  OUT DEFINITIONS.LOC_WISE_PHARMACY_STORE%ROWTYPE,
                    P_IGNORE_NO_DATA       IN CHAR DEFAULT NULL,
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_ORGANIZATION_ID      IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.ORGANIZATION_ID%TYPE,
                  P_PHYSICAL_LOCATION_ID IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.PHYSICAL_LOCATION_ID%TYPE,
                  P_STORE_ID             IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.STORE_ID%TYPE,
                  P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID          IN VARCHAR2,
                  P_CALLING_OBJECT       IN VARCHAR2,
                  P_CALLING_USER         IN VARCHAR2,
                  P_CALLING_EVENT        IN VARCHAR2,
                  P_ROWID                OUT ROWID,
                  P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.LOC_WISE_PHARMACY_STORE%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_ORGANIZATION_ID      IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.PHYSICAL_LOCATION_ID%TYPE,
                    P_STORE_ID             IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.STORE_ID%TYPE,
                    P_ROW                  IN OUT DEFINITIONS.LOC_WISE_PHARMACY_STORE%ROWTYPE,
                    P_UPDATE_NULL          IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_ORGANIZATION_ID      IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.PHYSICAL_LOCATION_ID%TYPE,
                    P_STORE_ID             IN DEFINITIONS.LOC_WISE_PHARMACY_STORE.STORE_ID%TYPE,
                    P_IGNORE_NO_DATA       IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID          IN VARCHAR2,
                    P_CALLING_OBJECT       IN VARCHAR2,
                    P_CALLING_USER         IN VARCHAR2,
                    P_CALLING_EVENT        IN VARCHAR2,
                    P_ERROR                OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_LOC_WISE_PHARMACY_STORE;
```

### DEFINITIONS.PKG_MODULE_REPORT_NAME
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_MODULE_REPORT_NAME IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 13:29
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
  FUNCTION F_SELECT(P_REPORT_NAME_ID IN DEFINITIONS.MODULE_REPORT_NAME.REPORT_NAME_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.MODULE_REPORT_NAME%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_REPORT_NAME_ID IN DEFINITIONS.MODULE_REPORT_NAME.REPORT_NAME_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.MODULE_REPORT_NAME%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_REPORT_NAME_ID IN DEFINITIONS.MODULE_REPORT_NAME.REPORT_NAME_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.MODULE_REPORT_NAME%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_REPORT_NAME_ID IN DEFINITIONS.MODULE_REPORT_NAME.REPORT_NAME_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_MODULE_REPORT_NAME;
```

### DEFINITIONS.PKG_ORDER_LOCATION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ORDER_LOCATION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 13:38
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
  FUNCTION F_SELECT(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                    P_ROW               OUT DEFINITIONS.ORDER_LOCATION%ROWTYPE,
                    P_IGNORE_NO_DATA    IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                  P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.ORDER_LOCATION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                    P_ROW               IN OUT DEFINITIONS.ORDER_LOCATION%ROWTYPE,
                    P_UPDATE_NULL       IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_ORDER_LOCATION;
```

### DEFINITIONS.PKG_ORDER_LOCATION_RECEPTION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ORDER_LOCATION_RECEPTION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 14:00
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
  FUNCTION F_SELECT(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION_RECEPTION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION_RECEPTION.ORDER_LOCATION_ID%TYPE,
                    P_RECEPTION_ID      IN DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
                    P_ROW               OUT DEFINITIONS.ORDER_LOCATION_RECEPTION%ROWTYPE,
                    P_IGNORE_NO_DATA    IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION_RECEPTION.LOCATION_ID%TYPE,
                  P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION_RECEPTION.ORDER_LOCATION_ID%TYPE,
                  P_RECEPTION_ID      IN DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
                  P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.ORDER_LOCATION_RECEPTION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION_RECEPTION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION_RECEPTION.ORDER_LOCATION_ID%TYPE,
                    P_RECEPTION_ID      IN DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
                    P_ROW               IN OUT DEFINITIONS.ORDER_LOCATION_RECEPTION%ROWTYPE,
                    P_UPDATE_NULL       IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID       IN DEFINITIONS.ORDER_LOCATION_RECEPTION.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION_RECEPTION.ORDER_LOCATION_ID%TYPE,
                    P_RECEPTION_ID      IN DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
                    P_IGNORE_NO_DATA    IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_ORDER_LOCATION_RECEPTION;
```

### DEFINITIONS.PKG_ORDER_LOCATION_STORE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ORDER_LOCATION_STORE IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Abdul Wadood
  -- Created : 01-Dec-2019 16:44
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
  FUNCTION F_SELECT(P_LOCATION_ID         IN DEFINITIONS.ORDER_LOCATION_STORE.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID   IN DEFINITIONS.ORDER_LOCATION_STORE.ORDER_LOCATION_ID%TYPE,
                    P_STORE_ID            IN DEFINITIONS.ORDER_LOCATION_STORE.STORE_ID%TYPE,
                    P_DISPENSING_LOCATION IN DEFINITIONS.ORDER_LOCATION_STORE.DISPENSING_LOCATION%TYPE,
                    P_ROW                 OUT DEFINITIONS.ORDER_LOCATION_STORE%ROWTYPE,
                    P_IGNORE_NO_DATA      IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID         IN DEFINITIONS.ORDER_LOCATION_STORE.LOCATION_ID%TYPE,
                  P_ORDER_LOCATION_ID   IN DEFINITIONS.ORDER_LOCATION_STORE.ORDER_LOCATION_ID%TYPE,
                  P_STORE_ID            IN DEFINITIONS.ORDER_LOCATION_STORE.STORE_ID%TYPE,
                  P_DISPENSING_LOCATION IN DEFINITIONS.ORDER_LOCATION_STORE.DISPENSING_LOCATION%TYPE,
                  P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_LOCATION_ID IN VARCHAR2,
                  P_CALLING_OBJECT      IN VARCHAR2,
                  P_CALLING_USER        IN VARCHAR2,
                  P_CALLING_EVENT       IN VARCHAR2,
                  P_ROWID               OUT ROWID,
                  P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.ORDER_LOCATION_STORE%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID         IN DEFINITIONS.ORDER_LOCATION_STORE.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID   IN DEFINITIONS.ORDER_LOCATION_STORE.ORDER_LOCATION_ID%TYPE,
                    P_STORE_ID            IN DEFINITIONS.ORDER_LOCATION_STORE.STORE_ID%TYPE,
                    P_DISPENSING_LOCATION IN DEFINITIONS.ORDER_LOCATION_STORE.DISPENSING_LOCATION%TYPE,
                    P_ROW                 IN OUT DEFINITIONS.ORDER_LOCATION_STORE%ROWTYPE,
                    P_UPDATE_NULL         IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID         IN DEFINITIONS.ORDER_LOCATION_STORE.LOCATION_ID%TYPE,
                    P_ORDER_LOCATION_ID   IN DEFINITIONS.ORDER_LOCATION_STORE.ORDER_LOCATION_ID%TYPE,
                    P_STORE_ID            IN DEFINITIONS.ORDER_LOCATION_STORE.STORE_ID%TYPE,
                    P_DISPENSING_LOCATION IN DEFINITIONS.ORDER_LOCATION_STORE.DISPENSING_LOCATION%TYPE,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_ORDER_LOCATION_STORE;
```

### DEFINITIONS.PKG_ORG_HF_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ORG_HF_SETUP AS
  ---------------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 07-01-2013
  -- Scope     :
  -- Purpose   : The following record type, table types will be used
  --             for dml of DEFINITIONS.ORG_HF_SETUP
  /******************************************************************************/
  TYPE ORG_HF_SETUP_REC IS RECORD(
    ORGANIZATION_ID DEFINITIONS.ORG_HF_SETUP.ORGANIZATION_ID%TYPE,
    DESCRIPTION     DEFINITIONS.ORGANIZATION.DESCRIPTION%TYPE,
    FROM_DATE       DEFINITIONS.ORG_HF_SETUP.FROM_DATE%TYPE,
    RPT_HF_SETUP_ID DEFINITIONS.ORG_HF_SETUP.RPT_HF_SETUP_ID%TYPE);

  TYPE ORG_HF_SETUP_TAB IS TABLE OF ORG_HF_SETUP_REC INDEX BY PLS_INTEGER;
  TYPE ORG_HF_SETUP_TB IS TABLE OF ORG_HF_SETUP_REC;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : The following pipelined function will return table of records
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  FUNCTION F_ORG_HF_SETUP_QRY(P_ORGANIZATION_ID IN DEFINITIONS.ORG_HF_SETUP.ORGANIZATION_ID%TYPE,
                              P_FROM_DATE       IN DEFINITIONS.ORG_HF_SETUP.FROM_DATE%TYPE)
    RETURN ORG_HF_SETUP_TB
    PIPELINED;
  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_QRY(P_ORGANIZATION_ID IN DEFINITIONS.ORG_HF_SETUP.ORGANIZATION_ID%TYPE,
                               P_FROM_DATE       IN DEFINITIONS.ORG_HF_SETUP.FROM_DATE%TYPE,
                               P_DATA            IN OUT ORG_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for validating data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN ORG_HF_SETUP_REC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_INS(P_DATA       IN OUT ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_LCK(P_DATA       IN OUT ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_UPD(P_DATA       IN OUT ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 25-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_ORG_HF_SETUP_DEL(P_DATA       IN OUT ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
END PKG_ORG_HF_SETUP;
```

### DEFINITIONS.PKG_PACKAGE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_PACKAGE AS

  /***********************************************************************************************
         OBJECTIVE := 1. THIS PACKAGE WILL BE USED TO GENERATE ORDERENTRY FOR OPD PACKAGES
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        27-APR-2017   FARHAN AKRAM           1. CREATED THIS PACKAGE.
         2.0        03-APR-2019   M. ALI KHUBAIB         1. ADDED NEW PROCEDURE UPDATE_PACKAGE_PRICE
         3.0        16-MAR-2020   M.USMAN TAHIR          1. ADDED NEW FUNCION FOR HIDE INVOICE DETAIL
  ************************************************************************************************/
  -----------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE VERSION OF THIS PACKAGE --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  --------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN SERVICE TYPE AGAINST SERVICE TYPE ID --
  --------------------------------------------------------------------
  FUNCTION GET_SERVICE_CATEGORY_GROUP_ID(P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.SERVICE_CATEGORY_GROUP.SERVICE_CATEGORY_GROUP_ID%TYPE;
  -----------------------------------------------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN IS VALIDATION PERIOD REQUIRED OR NOT AGAINST PACKAGE_TYPE_ID AND PACKAGE_ID --
  -----------------------------------------------------------------------------------------------------------
  FUNCTION IS_VALIDATION_PERIOD_REQUIRED(P_PACKAGE_ID DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN SYS_REFCURSOR;
  ---------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE NO. OF ITEM ALLOWED FOR THIS ITEM --
  ---------------------------------------------------------------------
  FUNCTION GET_NO_OF_ITEMS_ALLOWED(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                   P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                                   P_ITEM_ID         IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                   P_STAY_CPT        IN BOOLEAN)
    RETURN DEFINITIONS.PACKAGE_ITEM.NO_OF_ITEM_ALLOWED%TYPE;
  -----------------------------------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE TREATMENT LIMIT CHECK AGAINST PACKAGE ID AND SERVICE TYPE   --
  -----------------------------------------------------------------------------------------------
  FUNCTION GET_TREATMENT_LIMIT_APPLY(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                     P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_APPLY%TYPE;
  -----------------------------------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE TREATMENT LIMIT AMOUNT AGAINST PACKAGE ID AND CONTRACT TYPE --
  -----------------------------------------------------------------------------------------------
  FUNCTION GET_SERVICE_TYPE_LIMIT_AMOUNT(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                         P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_AMOUNT%TYPE;
  -------------------------------------------------------------------------------
  -- THIS FUNCTION WILL RETURN THE TREATMENT LIMIT QUANTITY AGAINST PACKAGE ID --
  ---------------------------------------------------------------------------------
  FUNCTION GET_SERVICE_TYPE_LIMIT_QTY(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                      P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGE_SERVICES.NO_OF_ITEM_ALLOWED%TYPE;
  --------------------------------------------------------------
  -- THIS PROCEDURE WILL CHECK THE MISCELLANEOUS SERVICE TYPE --
  -- ONE MISCELLANEOUS SERIVCE TYPE MUST BE DEFINED
  --------------------------------------------------------------
  PROCEDURE CHECK_MISC_SERVICE_TYPE_ID(P_SERVICE_TYPE_ID OUT DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                                       P_ALERT_TEXT      OUT VARCHAR2,
                                       P_STOP            OUT CHAR);
  ------------------------------
  -- GET PACKAGE STAY DETAILS --
  ------------------------------
  TYPE T_PAKAGE_STAY_TAB IS TABLE OF DEFINITIONS.PACKAGE_STAY.DAYS%TYPE INDEX BY DEFINITIONS.CPT.CPT_ID%TYPE;
  FUNCTION GET_PACKAGE_STAY_DETAILS(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN T_PAKAGE_STAY_TAB;
  ---------------------------------------------
  -- CHECK ITEM EXISTS AND ACTIVE IN PACKAGE --
  ---------------------------------------------
  FUNCTION IS_ITEM_INCLUDED(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                            P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                            P_ITEM_ID         IN DEFINITIONS.PACKAGE_ITEM.ITEM_ID%TYPE,
                            P_STORE_ID        IN DEFINITIONS.SERVICE_TYPE_STORE.STORE_ID%TYPE)
    RETURN BOOLEAN;
  -----------------------------------------------------------
  -- GET ACTIVE FUND ID FOR THE GIVEN SERVICE TYPE PACKAGE --
  -----------------------------------------------------------
  FUNCTION GET_PACKAGE_FUND_ID(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                               P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGE_FUND.PACKAGE_FUND_ID%TYPE;
  -----------------------------------------------------------
  --        GET AMOUNT FOR GIVEN FUND ID AND PACKAGE       --
  -----------------------------------------------------------
  FUNCTION GET_PACKAGE_FUND_AMOUNT(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                   P_PACKAGE_FUND_ID IN DEFINITIONS.PACKAGE_FUND.PACKAGE_FUND_ID%TYPE)
    RETURN DEFINITIONS.PACKAGE_FUND.AMOUNT%TYPE;
  -------------------------------------------------------------
  --        IF GIVEN STORE IS LINKED WITH SERVICE TYPE       --
  -------------------------------------------------------------
  FUNCTION IS_STORE_ALLOWED(P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                            P_STORE_ID        IN DEFINITIONS.SERVICE_TYPE_STORE.STORE_ID%TYPE)
    RETURN BOOLEAN;
  -------------------------------------------------------------
  --                 GET_PACKAGE_SHORT_DESC                  --
  -------------------------------------------------------------
  FUNCTION GET_PACKAGE_SHORT_DESC(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGES.SHORT_DESC%TYPE;
  -------------------------------------------------------------
  --                    GET_PACKAGE_DESC                      --
  -------------------------------------------------------------
  FUNCTION GET_PACKAGE_DESC(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGES.DESCRIPTION%TYPE;
  -------------------------------------------------------------
  --         GET_PACKAGE_PROCESSING_METHOD                   --
  -------------------------------------------------------------
  FUNCTION GET_PACKAGE_PROCESSING_METHOD(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN DEFINITIONS.PACKAGES.DESCRIPTION%TYPE;
  -------------------------------------------------------------
  --              GET_PACKAGE_PRICE                          --
  -------------------------------------------------------------
  FUNCTION GET_PACKAGE_PRICE(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                             P_PRICE_DATE IN DATE)
    RETURN DEFINITIONS.PACKAGES.PRICE%TYPE;

  ----------------------------------------------------------------
  --                 GET_DEFUALT_PACKAGE_PRICE                  --
  ----------------------------------------------------------------
  FUNCTION GET_DEFUALT_EAR_PACKAGE_PRICE
    RETURN DEFINITIONS.PACKAGES.PRICE%TYPE;

  ---------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE PACKAGE PRICE --
  ---------------------------------------------------------
  PROCEDURE UPDATE_PACKAGE_PRICE(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                 P_ALERT_TEXT OUT VARCHAR2,
                                 P_STOP       OUT CHAR);
  -----------------------------------------------------------
  -- THIS FUNCTION WILL RETURN INVOICE_DETAIL HIDE OR NOT  --
  -----------------------------------------------------------
  FUNCTION F_HIDE_INVOICE_DETAIL(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE)
    RETURN VARCHAR2;                               
END PKG_PACKAGE;
```

### DEFINITIONS.PKG_PATIENT_TYPE_COUNTER
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_PATIENT_TYPE_COUNTER IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 18:41
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
  FUNCTION F_SELECT(P_PREFIX_LOCATION IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX_LOCATION%TYPE,
                    P_PREFIX          IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX%TYPE,
                    P_ORGANIZATION_ID IN DEFINITIONS.PATIENT_TYPE_COUNTER.ORGANIZATION_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.PATIENT_TYPE_COUNTER%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_PREFIX_LOCATION IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX_LOCATION%TYPE,
                  P_PREFIX          IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX%TYPE,
                  P_ORGANIZATION_ID IN DEFINITIONS.PATIENT_TYPE_COUNTER.ORGANIZATION_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID     IN VARCHAR2,
                  P_CALLING_OBJECT  IN VARCHAR2,
                  P_CALLING_USER    IN VARCHAR2,
                  P_CALLING_EVENT   IN VARCHAR2,
                  P_ROWID           OUT ROWID,
                  P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.PATIENT_TYPE_COUNTER%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_PREFIX_LOCATION IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX_LOCATION%TYPE,
                    P_PREFIX          IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX%TYPE,
                    P_ORGANIZATION_ID IN DEFINITIONS.PATIENT_TYPE_COUNTER.ORGANIZATION_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.PATIENT_TYPE_COUNTER%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_PREFIX_LOCATION IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX_LOCATION%TYPE,
                    P_PREFIX          IN DEFINITIONS.PATIENT_TYPE_COUNTER.PREFIX%TYPE,
                    P_ORGANIZATION_ID IN DEFINITIONS.PATIENT_TYPE_COUNTER.ORGANIZATION_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_PATIENT_TYPE_COUNTER;
```

### DEFINITIONS.PKG_PHARMACY_DISPENSING_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_PHARMACY_DISPENSING_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 02-Dec-2019 06:10
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
  FUNCTION F_SELECT(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_ROW                    OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA         IN CHAR DEFAULT NULL,
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                  P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                  P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                  P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                  P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                  P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID            IN VARCHAR2,
                  P_CALLING_OBJECT         IN VARCHAR2,
                  P_CALLING_USER           IN VARCHAR2,
                  P_CALLING_EVENT          IN VARCHAR2,
                  P_ROWID                  OUT ROWID,
                  P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_ROW                    IN OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_UPDATE_NULL            IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_PHARMACY_DISPENSING_SETUP;
```

### DEFINITIONS.PKG_PHARMACY_DISPENS_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_PHARMACY_DISPENS_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 02-Dec-2019 06:10
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
  FUNCTION F_SELECT(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_ROW                    OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA         IN CHAR DEFAULT NULL,
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                  P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                  P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                  P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                  P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                  P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID            IN VARCHAR2,
                  P_CALLING_OBJECT         IN VARCHAR2,
                  P_CALLING_USER           IN VARCHAR2,
                  P_CALLING_EVENT          IN VARCHAR2,
                  P_ROWID                  OUT ROWID,
                  P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_ROW                    IN OUT DEFINITIONS.PHARMACY_DISPENSING_SETUP%ROWTYPE,
                    P_UPDATE_NULL            IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_ORGANIZATION_ID        IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.ORGANIZATION_ID%TYPE,
                    P_PHYSICAL_LOCATION_ID   IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.PHYSICAL_LOCATION_ID%TYPE,
                    P_DISPENSING_LOCATION_ID IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.DISPENSING_LOCATION_ID%TYPE,
                    P_TRANSACTION_TYPE_ID    IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.TRANSACTION_TYPE_ID%TYPE,
                    P_IPD_OPD                IN DEFINITIONS.PHARMACY_DISPENSING_SETUP.IPD_OPD%TYPE,
                    P_IGNORE_NO_DATA         IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID            IN VARCHAR2,
                    P_CALLING_OBJECT         IN VARCHAR2,
                    P_CALLING_USER           IN VARCHAR2,
                    P_CALLING_EVENT          IN VARCHAR2,
                    P_ERROR                  OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_PHARMACY_DISPENS_SETUP;
```

### DEFINITIONS.PKG_REPORT_DESTINATION
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_REPORT_DESTINATION IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 18:54
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
  FUNCTION F_SELECT(P_DESTINATION_ID IN DEFINITIONS.REPORT_DESTINATION.DESTINATION_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.REPORT_DESTINATION%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_DESTINATION_ID IN DEFINITIONS.REPORT_DESTINATION.DESTINATION_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.REPORT_DESTINATION%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_DESTINATION_ID IN DEFINITIONS.REPORT_DESTINATION.DESTINATION_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.REPORT_DESTINATION%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_DESTINATION_ID IN DEFINITIONS.REPORT_DESTINATION.DESTINATION_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_REPORT_DESTINATION;
```

### DEFINITIONS.PKG_ROOM_PAYMENT_CATEGORY
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_ROOM_PAYMENT_CATEGORY IS

  -- Author  : MISLAM
  -- Created : 7/7/2017 3:02:39 PM
  -- Purpose : Contains all  Room Payment Category related Store Procedures and Functions 
  ----CREATED BY  MUHAMMAD ISLAM ON DATED 07-JUL-2017--------
  ----PURPOSE:  THIS FUNCTION WILL RETURN ROOM PAYMENT CATEGORY ID AGAINST BED_ID,lOCATION_ID

  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_BED_ID         IN VARCHAR2,
                        P_BED_LOC_ID     IN VARCHAR2,
                        P_LOCATION_ID    IN VARCHAR2,
                        P_CALLING_OBJECT IN VARCHAR,
                        P_CALLING_USER   IN VARCHAR,
                        P_CALLING_EVENT  IN VARCHAR2,
                        P_RPC_ID         OUT VARCHAR2,
                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_ADMISSION_NO   IN VARCHAR2,
                        P_LOCATION_ID    IN VARCHAR2,
                        P_CALLING_OBJECT IN VARCHAR,
                        P_CALLING_USER   IN VARCHAR,
                        P_CALLING_EVENT  IN VARCHAR2,
                        P_RPC_ID         OUT VARCHAR2,
                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_MRNO           IN VARCHAR2,
                        P_LOCATION_ID    IN VARCHAR2,
                        P_CALLING_OBJECT IN VARCHAR,
                        P_CALLING_USER   IN VARCHAR,
                        P_CALLING_EVENT  IN VARCHAR2,
                        P_RPC_ID         OUT VARCHAR2,
                        P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_BED_ID IN VARCHAR2, P_BED_LOC_ID IN VARCHAR2)
    RETURN VARCHAR2;

  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_ADMISSION_NO IN VARCHAR2) RETURN VARCHAR2;

  -- ----------------------------------------------------------------------------------------
  FUNCTION F_GET_RPC_ID(P_MRNO IN VARCHAR2) RETURN VARCHAR2;

-- ----------------------------------------------------------------------------------------

END PKG_ROOM_PAYMENT_CATEGORY;
```

### DEFINITIONS.PKG_RPT_HF_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_RPT_HF_SETUP AS
  ---------------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : The following record type, table types will be used
  --             for dml of DEFINITIONS.
  /******************************************************************************/
  TYPE RPT_HF_SETUP_REC IS RECORD(
    RPT_HF_SETUP_ID DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
    ADDRESS         DEFINITIONS.RPT_HF_SETUP.ADDRESS%TYPE,
    PHONE           DEFINITIONS.RPT_HF_SETUP.PHONE%TYPE,
    FAX             DEFINITIONS.RPT_HF_SETUP.FAX%TYPE,
    EMAIL           DEFINITIONS.RPT_HF_SETUP.EMAIL%TYPE,
    WEBSITE         DEFINITIONS.RPT_HF_SETUP.WEBSITE%TYPE,
    --L_HEADER_IMAGE  DEFINITIONS.RPT_HF_SETUP.L_HEADER_IMAGE%TYPE,
    --L_FOOTER_IMAGE  DEFINITIONS.RPT_HF_SETUP.L_FOOTER_IMAGE%TYPE,
    HEADER_TYPE     DEFINITIONS.RPT_HF_SETUP.HEADER_TYPE%TYPE,
    FOOTER_TYPE     DEFINITIONS.RPT_HF_SETUP.FOOTER_TYPE%TYPE,
    REPORT_HEADER   DEFINITIONS.RPT_HF_SETUP.REPORT_HEADER%TYPE,
    COPY_RIGHT      DEFINITIONS.RPT_HF_SETUP.COPY_RIGHT%TYPE,
    --P_HEADER_IMAGE  DEFINITIONS.RPT_HF_SETUP.P_HEADER_IMAGE%TYPE,
    --P_FOOTER_IMAGE  DEFINITIONS.RPT_HF_SETUP.P_FOOTER_IMAGE%TYPE,
    --LOGO            DEFINITIONS.RPT_HF_SETUP.LOGO%TYPE,
    ORGANIZATION_ID DEFINITIONS.RPT_HF_SETUP.ORGANIZATION_ID%TYPE,
    LOCATION_ID     DEFINITIONS.RPT_HF_SETUP.LOCATION_ID%TYPE);

  TYPE RPT_HF_SETUP_TAB IS TABLE OF RPT_HF_SETUP_REC INDEX BY PLS_INTEGER;
  TYPE RPT_HF_SETUP_TB IS TABLE OF RPT_HF_SETUP_REC;

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : The following pipelined function will return table of records
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

    FUNCTION F_RPT_HF_SETUP_QRY(P_RPT_HF_SETUP_ID IN DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                              P_LOCATION_ID     IN DEFINITIONS.RPT_HF_SETUP.LOCATION_ID%TYPE)
    RETURN RPT_HF_SETUP_TB
    PIPELINED;
  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for querying data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_QRY(P_RPT_HF_SETUP_ID IN DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.RPT_HF_SETUP.LOCATION_ID%TYPE,
                               P_DATA            IN OUT RPT_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for validating data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_VAL(P_VALIDATION_TYPE IN VARCHAR2,
                               P_DATA            IN RPT_HF_SETUP_REC,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for inserting data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_INS(P_RPT_HF_SETUP_ID OUT DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                               P_DATA            IN OUT RPT_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for validating data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_LCK(P_DATA       IN OUT RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_UPD(P_DATA       IN OUT RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 24-01-2014
  -- Scope     : RPT_HF_SETUP
  -- Purpose   : This procedure will be used for deleting data of
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/

  PROCEDURE P_RPT_HF_SETUP_DEL(P_DATA       IN OUT RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);
END PKG_RPT_HF_SETUP;
```

### DEFINITIONS.PKG_RPT_HF_TMP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.pkg_rpt_hf_tmp IS
  -- Record type for header and footer fields for all reports
  TYPE rpt_hf_rec IS RECORD(
    org_nme            VARCHAR2(60),
    address_txt        VARCHAR2(2000),
    ph_fax_txt         VARCHAR2(94),
    email_website_txt  VARCHAR2(178),
    rep_title_txt      VARCHAR2(250),
    copy_right_txt     VARCHAR2(255),
    rep_dte            VARCHAR2(20),
    other_title_txt    VARCHAR2(30),
    other_comments_txt VARCHAR2(2000));

  TYPE rpt_hf_cur IS REF CURSOR RETURN rpt_hf_rec;

  -- Procedure for generating field values of header and footer of all reports
  PROCEDURE pro_rpt_hf(p_object_code IN VARCHAR2,
                       p_process_id  IN VARCHAR2,
                       p_user_name   IN VARCHAR2,
                       p_terminal    IN VARCHAR2,
                       p_event       IN VARCHAR2,
                       p_allert_txt  OUT VARCHAR2,
                       p_stop_yn     OUT CHAR,
                       p_location_id IN VARCHAR2,
                       p_fields      OUT rpt_hf_cur);
END pkg_rpt_hf_tmp;
```

### DEFINITIONS.PKG_S01FRM00020
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00020 AS

  /***********************************************************************************************
         OBJECTIVE := This package will be used for synchronize CPT from HIS to DEVCOM 0
         -----------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date        Author                     Description
         ---------  ----------  ---------------------      ----------------------------------
         1.0        25-11-2014  Mudassar Iqbal (6814)      1. Created this Package. 
         1.1        11-DEC-2014 Muhammad Younas (4808)     2. Design Procedure based form Definitions.CPT, add new procedures , user define types and funtions.
         1.2        12-NOV-2015 Muhammad Younas (4808)     3. add department_nature_id and nature_detail_id
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;
  -------------------------------------------
  -- Record type for Definitions.CPT Table --
  -------------------------------------------
  TYPE CPT_REC IS RECORD(
    CPT_ID                    DEFINITIONS.CPT.CPT_ID%TYPE,
    DESCRIPTION               DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_CATEGORY_ID           DEFINITIONS.CPT.CPT_CATEGORY_ID%TYPE,
    CATEGORY                  DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE,
    INVOICE_STATUS_ID         DEFINITIONS.CPT.INVOICE_STATUS_ID%TYPE,
    INVOICE_STATUS            DEFINITIONS.ORDER_STATUS.DESCRIPTION%TYPE,
    CPT_TYPE                  DEFINITIONS.CPT.CPT_TYPE%TYPE,
    PRICE                     DEFINITIONS.CPT.PRICE%TYPE,
    IN_HOUSE_PERFORMED        DEFINITIONS.CPT.IN_HOUSE_PERFORMED%TYPE,
    COST                      DEFINITIONS.CPT.COST%TYPE,
    DOCTOR_SHARE_TYPE         DEFINITIONS.CPT.DOCTOR_SHARE_TYPE%TYPE,
    ACTIVE                    DEFINITIONS.CPT.ACTIVE%TYPE,
    SHORT_DESC                DEFINITIONS.CPT.SHORT_DESC%TYPE,
    CONSULTANCY               DEFINITIONS.CPT.CONSULTANCY%TYPE,
    STAT_CHARGEABLE           DEFINITIONS.CPT.STAT_CHARGEABLE%TYPE,
    MOST_COMMONLY_USED        DEFINITIONS.CPT.MOST_COMMONLY_USED%TYPE,
    NO_OF_PROCEDURES          DEFINITIONS.CPT.NO_OF_PROCEDURES%TYPE,
    REP_ORDER                 DEFINITIONS.CPT.REP_ORDER%TYPE,
    PAT_REPORT_CATEGORY_ID    DEFINITIONS.CPT.PAT_REPORT_CATEGORY_ID%TYPE,
    DOCTOR_REQUIRED           DEFINITIONS.CPT.DOCTOR_REQUIRED%TYPE,
    PATHOLOGY_COMMENT_TYPE_ID DEFINITIONS.CPT.PATHOLOGY_COMMENT_TYPE_ID%TYPE,
    MAX_QUANTITY_ALLOWED      DEFINITIONS.CPT.MAX_QUANTITY_ALLOWED%TYPE,
    REPORTING_CASE            DEFINITIONS.CPT.REPORTING_CASE%TYPE,
    NO_OF_REPORTS             DEFINITIONS.CPT.NO_OF_REPORTS%TYPE,
    DUPLICATE_ACKNOWLEDGE     DEFINITIONS.CPT.DUPLICATE_ACKNOWLEDGE%TYPE,
    SPECIMEN_NATURE_REQUIRED  DEFINITIONS.CPT.SPECIMEN_NATURE_REQUIRED%TYPE,
    SPECIMEN_SITE_REQUIRED    DEFINITIONS.CPT.SPECIMEN_SITE_REQUIRED%TYPE,
    TECH_NORMAL               DEFINITIONS.CPT.TECH_NORMAL%TYPE,
    TECH_ABNORMAL             DEFINITIONS.CPT.TECH_ABNORMAL%TYPE,
    DOCTOR_NORMAL             DEFINITIONS.CPT.DOCTOR_NORMAL%TYPE,
    DOCTOR_ABNORMAL           DEFINITIONS.CPT.DOCTOR_ABNORMAL%TYPE,
    CONSULTANT_NORMAL         DEFINITIONS.CPT.CONSULTANT_NORMAL%TYPE,
    NOT_REPORTABLE            DEFINITIONS.CPT.NOT_REPORTABLE%TYPE,
    CONSULTANT_ABNORMAL       DEFINITIONS.CPT.CONSULTANT_ABNORMAL%TYPE,
    COMBINED_REPORT           DEFINITIONS.CPT.COMBINED_REPORT%TYPE,
    REPORT_HEADING            DEFINITIONS.CPT.REPORT_HEADING%TYPE,
    SPECIALITY_ID             DEFINITIONS.CPT.SPECIALITY_ID%TYPE,
    ND_SPECIALITY             DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
    SURGERY_REGION_ID         DEFINITIONS.CPT.SURGERY_REGION_ID%TYPE,
    LENGTH_OF_STAY            DEFINITIONS.CPT.LENGTH_OF_STAY%TYPE,
    AFTER_DEATH_ENTRY         DEFINITIONS.CPT.AFTER_DEATH_ENTRY%TYPE,
    OPEN_PRICE                DEFINITIONS.CPT.OPEN_PRICE%TYPE,
    PERFORM_LOCATION_ID       DEFINITIONS.CPT.PERFORM_LOCATION_ID%TYPE,
    MODALITY_ID               DEFINITIONS.CPT.MODALITY_ID%TYPE,
    IMAGE_REQUIRED            DEFINITIONS.CPT.IMAGE_REQUIRED%TYPE,
    SHARE_ON_PERFORM          DEFINITIONS.CPT.SHARE_ON_PERFORM%TYPE,
    EFFECTIVE_DATE            DEFINITIONS.CPT.EFFECTIVE_DATE%TYPE,
    ACTIVATED_DATE            DEFINITIONS.CPT.ACTIVATED_DATE%TYPE,
    REMARKS                   DEFINITIONS.CPT.REMARKS%TYPE,
    USER_DEFINED_DEPT         DEFINITIONS.CPT.USER_DEFINED_DEPT%TYPE,
    COMBINED_REPORT_NORMAL    DEFINITIONS.CPT.COMBINED_REPORT_NORMAL%TYPE,
    COMBINED_REPORT_ABNORMAL  DEFINITIONS.CPT.COMBINED_REPORT_ABNORMAL%TYPE,
    BLOCK_AUTO_INP_INVOICE    DEFINITIONS.CPT.BLOCK_AUTO_INP_INVOICE%TYPE,
    PRE_REQUISITES_CHK        DEFINITIONS.CPT.PRE_REQUISITES_CHK%TYPE,
    PRE_REQUISITES            VARCHAR2(30),
    EMPLOYEE_ENTITLEMENT      DEFINITIONS.CPT.EMPLOYEE_ENTITLEMENT%TYPE,
    CPT_BONUS                 DEFINITIONS.CPT.CPT_BONUS%TYPE,
    WORK_ORDER_PRINT          DEFINITIONS.CPT.WORK_ORDER_PRINT%TYPE,
    ACK_PERFORMANCE_REQ       DEFINITIONS.CPT.ACK_PERFORMANCE_REQ%TYPE,
    CLEARANCE                 DEFINITIONS.CPT.CLEARANCE%TYPE,
    INITIALIZED_YN            DEFINITIONS.CPT.INITIALIZED_YN%TYPE,
    CPT_CATEGORY_ID_NEW       DEFINITIONS.CPT.CPT_CATEGORY_ID_NEW%TYPE,
    INITIALIZED_DATE          DEFINITIONS.CPT.INITIALIZED_DATE%TYPE,
    LONG_DESC                 DEFINITIONS.CPT.LONG_DESC%TYPE,
    DEFAULT_DOCTOR            DEFINITIONS.CPT.DEFAULT_DOCTOR%TYPE,
    CONSENT_TYPE              DEFINITIONS.CPT.CONSENT_TYPE%TYPE,
    LIMITED_IMAGES            DEFINITIONS.CPT.LIMITED_IMAGES%TYPE,
    PI_CONSIDERATION          DEFINITIONS.CPT.PI_CONSIDERATION%TYPE,
    CONSULTANT_ONLY           DEFINITIONS.CPT.CONSULTANT_ONLY%TYPE,
    LAST_ORDER_VALUE_INHOUR   DEFINITIONS.CPT.LAST_ORDER_VALUE_INHOUR%TYPE,
    NO_OF_IMAGES              DEFINITIONS.CPT.NO_OF_IMAGES%TYPE,
    ORDER_RESTRICTION         DEFINITIONS.CPT.ORDER_RESTRICTION%TYPE,
    EAR_ALLOWED               DEFINITIONS.CPT.EAR_ALLOWED%TYPE,
    CLINICAL_REPORT           DEFINITIONS.CPT.CLINICAL_REPORT%TYPE,
    CONTRAST                  DEFINITIONS.CPT.CONTRAST%TYPE,
    MANUAL_PERFROMACE         DEFINITIONS.CPT.MANUAL_PERFROMACE%TYPE,
    ASSESSMENT_REQUIRED       DEFINITIONS.CPT.ASSESSMENT_REQUIRED%TYPE,
    ORIGINAL_TRN_DATE         DEFINITIONS.CPT.ORIGINAL_TRN_DATE%TYPE,
    DISP_LOCATION_TOT         VARCHAR2(60),
    DISP_LOCATION_CPT         VARCHAR2(60),
    DEPARTMENT_NATURE_ID      DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
    DEPARTMENT_NATURE         DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
    NATURE_DETAIL_ID          DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
    NATURE_DETAIL             DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    MULTIPLE_QTY_ALLOWED      DEFINITIONS.CPT.MULTIPLE_QTY_ALLOWED%TYPE,
    SITE_MARKING_REQUIRED     DEFINITIONS.CPT.SITE_MARKING_REQUIRED%TYPE,
    IS_CNOAT                  DEFINITIONS.CPT.IS_CNOAT%TYPE); --ADDED BY SAIF UL ISLAM DATED: 29-11-2022

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CPT_TAB IS TABLE OF CPT_REC INDEX BY BINARY_INTEGER;
  ---------------------------------------------
  -- This Procedure will query the CPT Table --
  ---------------------------------------------
  PROCEDURE QUERY_CPT(P_RESULT     IN OUT CPT_REF,
                      P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_ALERT_TEXT OUT VARCHAR2);

  -----------------                            
  -- Insert CPT  --
  -----------------
  PROCEDURE INSERT_CPT(P_BLOCK_DATA IN OUT CPT_TAB,
                       P_ALERT_TEXT OUT VARCHAR);
  -----------------
  -- Update CPT  --
  -----------------
  PROCEDURE UPDATE_CPT(P_BLOCK_DATA IN OUT CPT_TAB,
                       P_ALERT_TEXT OUT VARCHAR);
  ----------------
  -- Delete CPT --
  ----------------
  PROCEDURE DELETE_CPT(P_BLOCK_DATA IN OUT CPT_TAB,
                       P_ALERT_TEXT OUT VARCHAR);
  --------------
  -- Lock CPT --
  --------------
  PROCEDURE LOCK_CPT(P_BLOCK_DATA IN OUT CPT_TAB, P_ALERT_TEXT OUT VARCHAR);

  ------------------------------------------------------------
  -- This Procedure will synchronize CPT from HIS to DEVCOM --
  ------------------------------------------------------------
  PROCEDURE SYNCHRONIZE_CPT_HIS_TO_DEVCOM(P_CPT_ID          IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                          P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                                          P_ALERT_TEXT      OUT VARCHAR2,
                                          P_STOP            OUT CHAR);

  ------------------------------------------------------------
  -- This Procedure will synchronize CPT from HIS to QACOM --
  ------------------------------------------------------------

  PROCEDURE SYNCHRONIZE_CPT_HIS_TO_QACOM(P_CPT_ID          IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                         P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                                         P_ALERT_TEXT      OUT VARCHAR2,
                                         P_STOP            OUT CHAR);
  ----------------------------------------------                                      
  -- This Procedure will check CPT Validation --
  ----------------------------------------------
  PROCEDURE VALIDATE_CPT(P_SEND_MAIL_YN  IN CHAR,
                         P_OBJECT_CODE   IN VARCHAR2,
                         P_USER          IN VARCHAR2,
                         P_EVENT         IN VARCHAR2,
                         P_LOCATION_ID   IN VARCHAR2,
                         P_DEPARTMENT_ID IN VARCHAR2,
                         P_SECTION_ID    IN VARCHAR2,
                         P_CPT_ID        IN VARCHAR2,
                         P_ALERT_TEXT    OUT VARCHAR2,
                         P_STOP          OUT VARCHAR2);

END PKG_S01FRM00020;
```

### DEFINITIONS.PKG_S01FRM00022
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00022 AS

  /****************************************************************************************************************
         OBJECTIVE := THIS PACKAGE IS WRITTEN TO DEVELOP COPY OPTION FOR RADIATION CPT PACKAGES 
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE         AUTHOR                  DESCRIPTION
         ---------  ----------   ---------------         -----------------------------------
         1.0        22-JUN-2016  USMAN AFZAL(5784)      1. CREATED THIS PACKAGE.
         1.1        12-MAR-2017  FARHAN AKRAM           1. REDEVELOPMENT
         1.2        02-APR-2019  MUHAMMAD ALI KHUBAIB   1. MODIFICATIONS
  ****************************************************************************************************************/
  ------------------------------------
  -- RECORD GROUP FOR MASTER --
  ------------------------------------
  TYPE PACKAGE_REC IS RECORD(
    -------
    PACKAGE_ID          DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
    TRANS_DATE          DEFINITIONS.PACKAGES.TRANS_DATE%TYPE,
    DESCRIPTION         DEFINITIONS.PACKAGES.DESCRIPTION%TYPE,
    SHORT_DESC          DEFINITIONS.PACKAGES.SHORT_DESC%TYPE,
    HIDE_INVOICE_DETAIL DEFINITIONS.PACKAGE_DETAIL.HIDE_INVOICE_DETAIL%TYPE,
    PRICE               DEFINITIONS.PACKAGES.PRICE%TYPE,
    PRICE_SOURCE        DEFINITIONS.PACKAGE_DETAIL.PRICE_SOURCE%TYPE,
    SERVICE_TYPE_ID     DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
    PACKAGE_TYPE_ID     DEFINITIONS.PACKAGE_TYPE.PACKAGE_TYPE_ID%TYPE,
    SHOW_ITEM_PRICE     DEFINITIONS.PACKAGES.SHOW_ITEM_PRICE%TYPE,
    ACTIVE              DEFINITIONS.PACKAGES.ACTIVE%TYPE,
    USER_ID             DEFINITIONS.PACKAGES.USER_ID%TYPE,
    TERMINAL            DEFINITIONS.PACKAGES.TERMINAL%TYPE);

  ----------------------
  -- REF CURSOR  --
  ----------------------
  TYPE PACKAGE_REF IS REF CURSOR RETURN PACKAGE_REC;
  ----------------------
  -- ASSOCIATIVE ARRAY--
  ----------------------
  TYPE PACKAGE_TAB IS TABLE OF PACKAGE_REC INDEX BY BINARY_INTEGER;
  ----------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA--
  ----------------------------------------------
  PROCEDURE QUERY_PACKAGE(PIO_RESULT         IN OUT PACKAGE_REF,
                          PI_PACKAGE_TYPE_ID IN OUT DEFINITIONS.PACKAGE_TYPE.PACKAGE_TYPE_ID%TYPE,
                          PIO_PACKAGE_ID     IN OUT DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE);

  ------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO INSERT DATA --
  ------------------------------------------------
  PROCEDURE INSERT_PACKAGE(PIO_BLOCK_DATA       IN OUT PACKAGE_TAB,
                           PI_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           PI_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           PI_USER_MRNO         IN VARCHAR2,
                           PI_OBJECT_CODE       IN VARCHAR2,
                           PI_TERMINAL          IN VARCHAR2);
  ----------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE DATA INTO PACKAGE BLOCK --
  ----------------------------------------------------------------
  PROCEDURE UPDATE_PACKAGE(PIO_BLOCK_DATA IN OUT PACKAGE_TAB);
  --------------------------------------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO LOCK ROW WHILE UPDATING DATA INTO PACKAGE AND PACKAGE DETAIL TABLES --
  --------------------------------------------------------------------------------------------------------
  PROCEDURE LOCK_PACKAGE(PIO_BLOCK_DATA IN OUT PACKAGE_TAB);
  ------------------------------------------------------------------------
  -- THIS PROCEDURE WILL GENERATE NEW PACKAGE BASED ON EXISTING PACKAGE --
  ------------------------------------------------------------------------
  PROCEDURE GENERATE_CPT_PACKAGE_TEMPLATE(PI_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                          PI_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                          PI_BASE_PACKAGE_ID   IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                          PO_NEW_PACKAGE_ID    OUT DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                          PO_ALERT_TEXT        OUT VARCHAR2,
                                          PO_STOP              OUT CHAR);
  ------------------------------------
  -- RECORD GROUP FOR MASTER --
  ------------------------------------
  TYPE PACKAGE_ITEM_REC IS RECORD(
    -------
    PACKAGE_ID      DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
    SERVICE_TYPE_ID DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
    ITEM_ID         DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_ITEM_ID    DEFINITIONS.CPT.CPT_ID%TYPE,
    ITEM_DESC       DEFINITIONS.CPT.DESCRIPTION%TYPE,
    QUANTITY        DEFINITIONS.PACKAGE_ITEM.QUANTITY%TYPE,
    PRICE           DEFINITIONS.PACKAGES.PRICE%TYPE,
    ACTIVE          DEFINITIONS.PACKAGES.ACTIVE%TYPE);

  ----------------------
  -- REF CURSOR  --
  ----------------------
  TYPE PACKAGE_ITEM_REF IS REF CURSOR RETURN PACKAGE_ITEM_REC;
  ----------------------
  -- ASSOCIATIVE ARRAY--
  ----------------------
  TYPE PACKAGE_ITEM_TAB IS TABLE OF PACKAGE_ITEM_REC INDEX BY BINARY_INTEGER;
  ----------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA--
  ----------------------------------------------
  PROCEDURE QUERY_PACKAGE_ITEM(PIO_RESULT     IN OUT PACKAGE_ITEM_REF,
                               PIO_PACKAGE_ID IN OUT DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                               PIO_ITEM_ID    IN OUT DEFINITIONS.CPT.CPT_ID%TYPE);
  ------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO INSERT DATA --
  ------------------------------------------------
  PROCEDURE INSERT_PACKAGE_ITEM(PIO_BLOCK_DATA       IN OUT PACKAGE_ITEM_TAB,
                                PI_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                                PI_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                PI_USER_MRNO         IN VARCHAR2,
                                PI_OBJECT_CODE       IN VARCHAR2,
                                PI_TERMINAL          IN VARCHAR2);
  ------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO UPDATE DATA --
  ------------------------------------------------
  PROCEDURE UPDATE_PACKAGE_ITEM(PIO_BLOCK_DATA IN OUT PACKAGE_ITEM_TAB);
  ------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO DELETE DATA --
  ------------------------------------------------
  PROCEDURE DELETE_PACKAGE_ITEM(PIO_BLOCK_DATA IN OUT PACKAGE_ITEM_TAB);
  -----------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO LOCK ROW WHILE UPDATING DATA --
  -----------------------------------------------------------------
  PROCEDURE LOCK_PACKAGE_ITEM(PIO_BLOCK_DATA IN OUT PACKAGE_ITEM_TAB);
  FUNCTION GET_SERVICE_TYPE_ID(P_PACKAGE_TYPE_ID DEFINITIONS.PACKAGE_TYPE.PACKAGE_TYPE_ID%TYPE)
    RETURN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE;

END PKG_S01FRM00022;
```

### DEFINITIONS.PKG_S01FRM00029_ROLE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00029_ROLE IS
  /*===================================================================
   created by := Mahboob alam
   when new role add in designation_role then automaticaly all assigned right to those users who have same designation.
  ==================================================================*/
  PROCEDURE GRANT_ROLE_AND_GROUP(P_DESIGNATION_ID IN VARCHAR2,
                                 P_ROLE_ID        IN VARCHAR2,
                                 P_STOP           OUT CHAR,
                                 P_ALERT_TEXT     OUT VARCHAR2);
  /**********************************************************************/
  /*===================================================================
   created by := Mahboob alam
   when role DELETE in designation_role then automaticaly all REVOKED rightS to those users who have same designation.
  ==================================================================*/
  PROCEDURE REVOKE_ROLE_AND_GROUP(P_DESIGNATION_ID IN VARCHAR2,
                                  P_ROLE_ID        IN VARCHAR2,
                                  P_STOP           OUT CHAR,
                                  P_ALERT_TEXT     OUT VARCHAR2);

  /************************************************************************/
  PROCEDURE CHILD_GRANT_ROLE_GROUP(P_ROLE_ID IN VARCHAR2,
                                   P_MRNO    IN VARCHAR2,
                                   --  P_USER_ID    IN VARCHAR2,
                                   P_STOP       OUT CHAR,
                                   P_ALERT_TEXT OUT VARCHAR2);
  /************************************************************************/
  PROCEDURE CHILD_REVOKE_ROLE_GROUP(P_ROLE_ID IN VARCHAR2,
                                    P_MRNO    IN VARCHAR2,
                                    --  P_USER_ID     IN VARCHAR2,
                                    P_LOCATION_ID IN VARCHAR2,
                                    P_STOP        OUT CHAR,
                                    P_ALERT_TEXT  OUT VARCHAR2);
  /**********************************************************************/
END;
```

### DEFINITIONS.PKG_S01FRM00039
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00039 IS
  /**************************************************************************************************
  -- Author  : Fiaz Ahmad
  -- Created : 10/02/2016 11:09:55 AM
  -- Purpose :
  ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
        1.0        21-Aug-2024   Shahid                  1. Changed as per CLI-26808
  -----------------------------------------------------------------------------------
  **************************************************************************************************/
  TYPE REC_DED IS RECORD(
    DOCTOR_ID          DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DOCTOR_ID%TYPE,
    DEPARTMENT_ID      DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.DEPARTMENT_ID%TYPE,
    SECTION_ID         DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.SECTION_ID%TYPE,
    SECTION_DESC       DEFINITIONS.DEPARTMENT_SECTION.DESCRIPTION%TYPE,
    CONTRACT_STRT_DATE DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.CONTRACT_STRT_DATE%TYPE,
    CONTRACT_END_DATE  DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.CONTRACT_END_DATE%TYPE,
    TEST_REQ_FOR_BONUS DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.TEST_REQ_FOR_BONUS%TYPE,
    BONUS              DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.BONUS%TYPE,
    TOT_TESTS          DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.TOT_TESTS%TYPE,
    BONUS_DUE          DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.BONUS_DUE%TYPE,
    BONUS_AVAILED      DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.BONUS_AVAILED%TYPE,
    BONUS_BAL          DEFINITIONS.EXTERNAL_DOCTOR_DETAIL.BONUS_BAL%TYPE);
  -------------------------------------------------------------------------- 
  TYPE CUR_DED IS REF CURSOR; -- RETURN REC_DED;

  TYPE TAB_DED IS TABLE OF REC_DED INDEX BY BINARY_INTEGER;
  ---------------------------------------------------------------------
  PROCEDURE P_DED_QUERY(P_RECORD      IN OUT CUR_DED,
                        P_DOCTOR_ID   IN VARCHAR2,
                        P_LOCATION_ID IN VARCHAR2,
                        P_OBJECT_CODE IN VARCHAR2,
                        P_USER_MRNO   IN VARCHAR2,
                        P_EVENT       IN VARCHAR2);
  -------------------------------------------------------------------------
  PROCEDURE P_DED_UPDATE(P_RECORD      IN OUT TAB_DED,
                         P_LOCATION_ID IN VARCHAR2,
                         P_OBJECT_CODE IN VARCHAR2,
                         P_USER_MRNO   IN VARCHAR2,
                         P_EVENT       IN VARCHAR2);
  ------------------------------------------------------------------------
  PROCEDURE P_DED_LOCK(P_RESULT IN TAB_DED);
  ------------------------------------------------------------------------
  TYPE REC_DE IS RECORD(
    
    DOCTOR_ID       DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID%TYPE,
    NAME            DEFINITIONS.DOCTOR_EXTERNAL.NAME%TYPE,
    SPECIALITY      DEFINITIONS.DOCTOR_EXTERNAL.SPECIALITY%TYPE,
    DEGREES         DEFINITIONS.DOCTOR_EXTERNAL.DEGREES%TYPE,
    ADDRESS1        DEFINITIONS.DOCTOR_EXTERNAL.ADDRESS1%TYPE,
    ADDRESS2        DEFINITIONS.DOCTOR_EXTERNAL.ADDRESS2%TYPE,
    PHONE1          DEFINITIONS.DOCTOR_EXTERNAL.PHONE1%TYPE,
    PHONE2          DEFINITIONS.DOCTOR_EXTERNAL.PHONE2%TYPE,
    EMAIL1          DEFINITIONS.DOCTOR_EXTERNAL.EMAIL1%TYPE,
    EMAIL2          DEFINITIONS.DOCTOR_EXTERNAL.EMAIL2%TYPE,
    FAX             DEFINITIONS.DOCTOR_EXTERNAL.FAX%TYPE,
    HOSPITAL        DEFINITIONS.DOCTOR_EXTERNAL.HOSPITAL%TYPE,
    CLINIC_CITY     DEFINITIONS.DOCTOR_EXTERNAL.CLINIC_CITY%TYPE,
    HOSPITAL_CITY   DEFINITIONS.DOCTOR_EXTERNAL.HOSPITAL_CITY%TYPE,
    ACTIVE          DEFINITIONS.DOCTOR_EXTERNAL.ACTIVE%TYPE,
    PANEL_DOCTOR    DEFINITIONS.DOCTOR_EXTERNAL.PANEL_DOCTOR%TYPE,
    HOSPITAL_ID     DEFINITIONS.DOCTOR_EXTERNAL.HOSPITAL_ID%TYPE,
    HOSPITAL_NAME   DEFINITIONS.HOSPITAL.NAME%TYPE,
    SPECIALITY_ID   DEFINITIONS.DOCTOR_EXTERNAL.SPECIALITY_ID%TYPE,
    SPECIALITY_DESC DEFINITIONS.DOCTOR_SPECIALITY.DESCRIPTION%TYPE,
    TITLE_ID        DEFINITIONS.DOCTOR_EXTERNAL.TITLE_ID%TYPE,
    TITLE_DESC      DEFINITIONS.TITLE.DESCRIPTION%TYPE,
    DOCTOR_ID_T     DEFINITIONS.DOCTOR_EXTERNAL.DOCTOR_ID_T%TYPE,
    PMDC            DEFINITIONS.DOCTOR_EXTERNAL.PMDC%TYPE);

  -----------------------------
  TYPE CUR_DE IS REF CURSOR; --  RETURN REC_DE;

  TYPE TAB_DE IS TABLE OF REC_DE INDEX BY BINARY_INTEGER;

  --------------------- DEFINING PROCEDURE TO QUERY RECORD --------------------------

  PROCEDURE P_DE_QUERY(P_RECORD      IN OUT CUR_DE,
                       P_LOCATION_ID IN VARCHAR2,
                       P_OBJECT_CODE IN VARCHAR2,
                       P_USER_MRNO   IN VARCHAR2,
                       P_DOCTOR_ID   IN VARCHAR2,
                       P_DOCTOR_NAME IN VARCHAR2,
                       P_ADDRESS     IN VARCHAR2,
                       P_PHONE1      IN VARCHAR2,
                       P_EVENT       IN VARCHAR2);

  ------------------------------
  PROCEDURE P_DE_UPDATE(P_RECORD      IN OUT TAB_DE,
                        P_LOCATION_ID IN VARCHAR2,
                        P_OBJECT_CODE IN VARCHAR2,
                        P_USER_MRNO   IN VARCHAR2,
                        P_EVENT       IN VARCHAR2);

  ----------------------------------
  PROCEDURE P_DE_INSERT(P_RECORD      IN OUT TAB_DE,
                        P_LOCATION_ID IN VARCHAR2,
                        P_OBJECT_CODE IN VARCHAR2,
                        P_USER_MRNO   IN VARCHAR2,
                        P_EVENT       IN VARCHAR2,
                        P_DOCTOR_ID   OUT VARCHAR2);
  ----------------------------------
  PROCEDURE P_DE_LOCK(P_RESULT IN TAB_DE);

  ------------------------------
  TYPE REC_DES IS RECORD(
    LOCATION_ID          WCCIS.DOCTOR_EXTERNAL_SETUP.LOCATION_ID%TYPE,
    LOCATION_DESC        DEFINITIONS.LOCATION.DESCRIPTION %TYPE,
    DOCTOR_LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    DOCTOR_LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION %TYPE,
    LOC_ACTIVE           WCCIS.DOCTOR_EXTERNAL_SETUP.ACTIVE%TYPE);

  TYPE CUR_DES IS REF CURSOR RETURN REC_DES;

  TYPE TAB_DES IS TABLE OF REC_DES INDEX BY BINARY_INTEGER;

  --------------------- DEFINING PROCEDURE TO QUERY RECORD --------------------------

  PROCEDURE P_DES_QUERY(P_RECORD      IN OUT CUR_DES,
                        P_LOCATION_ID IN VARCHAR2,
                        P_OBJECT_CODE IN VARCHAR2,
                        P_USER_MRNO   IN VARCHAR2,
                        P_EVENT       IN VARCHAR2);

  -------------------------DEFINING PROCEDURE OF LOCK-------------------------------

  PROCEDURE P_DES_LOCK(P_RESULT IN TAB_DES);

  -------------------------DEFINING PROCEDURE OF UPDATE-----------------------------

  PROCEDURE P_DES_UPDATE(P_RECORD      IN OUT TAB_DES,
                         P_LOCATION_ID IN VARCHAR2,
                         P_OBJECT_CODE IN VARCHAR2,
                         P_USER_MRNO   IN VARCHAR2,
                         P_EVENT       IN VARCHAR2);
  -------------------------------------------------------------------------------------

  FUNCTION F_INITIAL_FORM(P_USER_MRNO         IN VARCHAR2,
                          P_OBJECT_CODE       IN VARCHAR2,
                          P_TERMINAL          IN VARCHAR2,
                          P_EVENT             IN VARCHAR2,
                          P_LOCATION_DESC     OUT VARCHAR2,
                          P_SETUP_LOCATION_ID OUT VARCHAR2,
                          P_ERROR             OUT VARCHAR2) RETURN BOOLEAN;

END PKG_S01FRM00039;
```

### DEFINITIONS.PKG_S01FRM00052
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00052 AS

  /***********************************************************************************************
         OBJECTIVE := This package will be used ICD's form
         -----------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date        Author                     Description
         ---------  ----------  ---------------------      ----------------------------------
         1.0        21-12-2018  Allah Rakha (10671)      1. Created this Package.

  ************************************************************************************************/
  PROCEDURE INSERT_ICD_PROCESS_DATA(P_STOP       OUT VARCHAR2,
                                    P_ALERT_TEXT OUT VARCHAR2);

END PKG_S01FRM00052;
```

### DEFINITIONS.PKG_S01FRM00114
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00114 IS

  -- Author  : MUHAMMAD YASAR NASEER
  -- Created : 10/04/2015 12:04:17 PM
  -- Purpose : PROCEDURE BASE FORM PATIENT_CLEARANCE STATUS

  --REGISTRATION.PATIENT_CLEARANCE_STATUS
  TYPE REC_PAT_CLR_STATUS IS RECORD(
    CLEARANCE_STATUS_ID     REGISTRATION.PATIENT_CLEARANCE_STATUS.CLEARANCE_STATUS_ID%TYPE,
    DESCRIPTION             REGISTRATION.PATIENT_CLEARANCE_STATUS.DESCRIPTION%TYPE,
    STOP_BILLING            REGISTRATION.PATIENT_CLEARANCE_STATUS.STOP_BILLING%TYPE,
    STOP_NORMAL_ORDERS      REGISTRATION.PATIENT_CLEARANCE_STATUS.STOP_NORMAL_ORDERS%TYPE,
    STOP_EMERGENCY_ORDERS   REGISTRATION.PATIENT_CLEARANCE_STATUS.STOP_EMERGENCY_ORDERS%TYPE,
    STOP_CONSULTANCY_ORDERS REGISTRATION.PATIENT_CLEARANCE_STATUS.STOP_CONSULTANCY_ORDERS%TYPE,
    STOP_ADMISSION          REGISTRATION.PATIENT_CLEARANCE_STATUS.STOP_ADMISSION%TYPE,
    ACTIVE                  REGISTRATION.PATIENT_CLEARANCE_STATUS.ACTIVE%TYPE,
    ALERT_TEXT              REGISTRATION.PATIENT_CLEARANCE_STATUS.ALERT_TEXT%TYPE,
    SHOW_IN_LOV             REGISTRATION.PATIENT_CLEARANCE_STATUS.SHOW_IN_LOV%TYPE);
  TYPE REFCUR_PAT_CLR_STATUS IS REF CURSOR RETURN REC_PAT_CLR_STATUS;
  TYPE TAB_PAT_CLR_STATUS IS TABLE OF REC_PAT_CLR_STATUS INDEX BY BINARY_INTEGER;
  TYPE TAB_PATIENT_CLR_STATUS_APEX IS TABLE OF REC_PAT_CLR_STATUS;

  --REGISTRATION.MODULE_TYPES
  TYPE REC_MODULE_TYPES IS RECORD(
    MODULE_TYPE_ID REGISTRATION.MODULE_TYPES.MODULE_TYPE_ID%TYPE);
  TYPE REFCUR_MODULE_TYPES IS REF CURSOR RETURN REC_MODULE_TYPES;
  TYPE TAB_MODULE_TYPES IS TABLE OF REC_MODULE_TYPES INDEX BY BINARY_INTEGER;

  --REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE
  TYPE REC_PAT_CLR_MODULE IS RECORD(
    CLEARANCE_STATUS_ID REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.CLEARANCE_STATUS_ID%TYPE,
    MODULE_TYPE_ID      REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.MODULE_TYPE_ID%TYPE,
    PROCEED             REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.PROCEED%TYPE,
    SPECIAL_COMMENTS    REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SPECIAL_COMMENTS%TYPE,
    SHOW_ALERT          REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SHOW_ALERT%TYPE);

  TYPE REFCUR_PAT_CLR_MODULE IS REF CURSOR RETURN REC_PAT_CLR_MODULE;
  TYPE TAB_PAT_CLR_MODULE IS TABLE OF REC_PAT_CLR_MODULE INDEX BY BINARY_INTEGER;
  TYPE TAB_PATIENT_MODULE_APX IS TABLE OF REC_PAT_CLR_MODULE;
  
  ---PROCEDURE FOR QUERY REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  PROCEDURE PATIENT_CLEARANCE_STATUS_QRY(P_RESULT IN OUT REFCUR_PAT_CLR_STATUS, P_CLR_STATUS_ID IN REGISTRATION.PATIENT_CLEARANCE_STATUS.CLEARANCE_STATUS_ID%TYPE, P_DESCRIPTION IN REGISTRATION.PATIENT_CLEARANCE_STATUS.DESCRIPTION%TYPE, P_ALERT IN REGISTRATION.PATIENT_CLEARANCE_STATUS.ALERT_TEXT%TYPE, P_ACTIVE IN REGISTRATION.PATIENT_CLEARANCE_STATUS.ACTIVE%TYPE, P_SHOW_IN_LOV IN REGISTRATION.PATIENT_CLEARANCE_STATUS.SHOW_IN_LOV%TYPE);

  ---PROCEDURE FOR QUERY REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  FUNCTION PATIENT_CLR_STATUS_QRY_APX(P_CLR_STATUS_ID IN REGISTRATION.PATIENT_CLEARANCE_STATUS.CLEARANCE_STATUS_ID%TYPE,
                                            P_DESCRIPTION   IN REGISTRATION.PATIENT_CLEARANCE_STATUS.DESCRIPTION%TYPE,
                                            P_ALERT         IN REGISTRATION.PATIENT_CLEARANCE_STATUS.ALERT_TEXT%TYPE,
                                            P_ACTIVE        IN REGISTRATION.PATIENT_CLEARANCE_STATUS.ACTIVE%TYPE,
                                            P_SHOW_IN_LOV   IN REGISTRATION.PATIENT_CLEARANCE_STATUS.SHOW_IN_LOV%TYPE)
    RETURN TAB_PATIENT_CLR_STATUS_APEX
    PIPELINED;
  ---FOR INSERT DATA IN REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  PROCEDURE PATIENT_CLEARANCE_STATUS_INS(P_RESULT     IN OUT TAB_PAT_CLR_STATUS,
                                         P_STOP       OUT VARCHAR2,
                                         P_ALERT_TEXT OUT VARCHAR2);

  ---PROCEDURE FOR UPDATE REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  PROCEDURE PATIENT_CLEARANCE_STATUS_UPD(P_RESULT      IN OUT TAB_PAT_CLR_STATUS,
                                         P_OBJECT_CODE IN VARCHAR2,
                                         P_TERMINAL    IN VARCHAR2,
                                         P_STOP        OUT VARCHAR2,
                                         P_ALERT_TEXT  OUT VARCHAR2);

  ---PROCEDURE FOR DELETE REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  PROCEDURE PATIENT_CLEARANCE_STATUS_DLT(P_RESULT      IN OUT TAB_PAT_CLR_STATUS,
                                         P_OBJECT_CODE IN VARCHAR2,
                                         P_TERMINAL    IN VARCHAR2,
                                         P_STOP        OUT VARCHAR2,
                                         P_ALERT_TEXT  OUT VARCHAR2);

  ---PROCEDURE FOR LOCK REGISTRATION.PATIENT_CLEARANCE_STATUS TABLE
  PROCEDURE PATIENT_CLEARANCE_STATUS_LCK(P_RESULT     IN OUT TAB_PAT_CLR_STATUS,
                                         P_STOP       OUT VARCHAR2,
                                         P_ALERT_TEXT OUT VARCHAR2);

  --------------------------------------------------------------------------------
  ---PROCEDURE FOR QUERY REGISTRATION.MODULE_TYPES TABLE
  PROCEDURE MODULE_TYPES_QRY(P_RESULT         IN OUT REFCUR_MODULE_TYPES,
                             P_MODULE_TYPE_ID IN REGISTRATION.MODULE_TYPES.MODULE_TYPE_ID%TYPE);
  ---PROCEDURE FOR INSERT REGISTRATION.MODULE_TYPES TABLE
  PROCEDURE MODULE_TYPES_INS(P_RESULT         IN OUT TAB_MODULE_TYPES,
                             P_MODULE_TYPE_ID IN REGISTRATION.MODULE_TYPES.MODULE_TYPE_ID%TYPE,
                             P_OBJECT_CODE    IN VARCHAR2,
                             P_TERMINAL       IN VARCHAR2,
                             P_STOP           OUT VARCHAR2,
                             P_ALERT_TEXT     OUT VARCHAR2);
  ---PROCEDURE FOR UPDATE REGISTRATION.MODULE_TYPES TABLE
  PROCEDURE MODULE_TYPES_UPD(P_RESULT         IN OUT TAB_MODULE_TYPES,
                             P_MODULE_TYPE_ID IN REGISTRATION.MODULE_TYPES.MODULE_TYPE_ID%TYPE,
                             P_OBJECT_CODE    IN VARCHAR2,
                             P_TERMINAL       IN VARCHAR2,
                             P_STOP           OUT VARCHAR2,
                             P_ALERT_TEXT     OUT VARCHAR2);
  ---PROCEDURE FOR DELETE REGISTRATION.MODULE_TYPES TABLE
  PROCEDURE MODULE_TYPES_DLT(P_RESULT         IN OUT TAB_MODULE_TYPES,
                             P_MODULE_TYPE_ID IN REGISTRATION.MODULE_TYPES.MODULE_TYPE_ID%TYPE,
                             P_OBJECT_CODE    IN VARCHAR2,
                             P_TERMINAL       IN VARCHAR2,
                             P_STOP           OUT VARCHAR2,
                             P_ALERT_TEXT     OUT VARCHAR2);
  ---PROCEDURE FOR LOCK REGISTRATION.MODULE_TYPES TABLE
  PROCEDURE MODULE_TYPES_LCK(P_RESULT     IN OUT TAB_MODULE_TYPES,
                             P_STOP       OUT VARCHAR2,
                             P_ALERT_TEXT OUT VARCHAR2);
  ----------------------------------------------------------------------------------------------------
  ---PROCEDURE FOR QUERY REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE TABLE
  PROCEDURE PAT_CLR_MODULE_TYPE_QRY(P_RESULT              IN OUT REFCUR_PAT_CLR_MODULE,
                                    P_CLEARANCE_STATUS_ID IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.CLEARANCE_STATUS_ID%TYPE,
                                    P_MODULE_TYPE_ID      IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.MODULE_TYPE_ID%TYPE,
                                    P_PROCEED             IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.PROCEED%TYPE,
                                    P_SPECIAL_COMMENTS    IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SPECIAL_COMMENTS%TYPE,
                                    P_SHOW_ALERT          IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SHOW_ALERT%TYPE);

  FUNCTION PAT_CLR_MODULE_TYPE_QRY_APX(P_CLEARANCE_STATUS_ID IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.CLEARANCE_STATUS_ID%TYPE,
                                       P_MODULE_TYPE_ID      IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.MODULE_TYPE_ID%TYPE,
                                       P_PROCEED             IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.PROCEED%TYPE,
                                       P_SPECIAL_COMMENTS    IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SPECIAL_COMMENTS%TYPE,
                                       P_SHOW_ALERT          IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.SHOW_ALERT%TYPE)
    RETURN TAB_PATIENT_MODULE_APX
    PIPELINED;

  ---PROCEDURE FOR INSERT REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE TABLE
  PROCEDURE PAT_CLR_MODULE_TYPE_INS(P_RESULT      IN OUT TAB_PAT_CLR_MODULE,
                                    P_OBJECT_CODE IN VARCHAR2,
                                    P_TERMINAL    IN VARCHAR2,
                                    P_STOP        OUT VARCHAR2,
                                    P_ALERT_TEXT  OUT VARCHAR2);
  ---PROCEDURE FOR UPDATE REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE TABLE
  PROCEDURE PAT_CLR_MODULE_TYPE_UPD(P_RESULT      IN OUT TAB_PAT_CLR_MODULE,
                                    P_OBJECT_CODE IN VARCHAR2,
                                    P_TERMINAL    IN VARCHAR2,
                                    P_STOP        OUT VARCHAR2,
                                    P_ALERT_TEXT  OUT VARCHAR2);
  ---PROCEDURE FOR DELETE REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE TABLE
  PROCEDURE PAT_CLR_MODULE_TYPE_DLT(P_RESULT      IN OUT TAB_PAT_CLR_MODULE,
                                    P_OBJECT_CODE IN VARCHAR2,
                                    P_TERMINAL    IN VARCHAR2,
                                    P_STOP        OUT VARCHAR2,
                                    P_ALERT_TEXT  OUT VARCHAR2);
  ---PROCEDURE FOR LOCK REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE TABLE
  PROCEDURE PAT_CLR_MODULE_TYPE_LCK(P_RESULT     IN OUT TAB_PAT_CLR_MODULE,
                                    P_STOP       OUT VARCHAR2,
                                    P_ALERT_TEXT OUT VARCHAR2);
  ----------------------------------------------------------------------------------------------------
  --POPULATE BUTTON
  PROCEDURE POPULATE_MODULE_TYPE(P_CLEARANCE_STATUS_ID IN REGISTRATION.PATIENT_CLEARANCE_MODULE_TYPE.CLEARANCE_STATUS_ID%TYPE,
                                 P_STOP                OUT VARCHAR2,
                                 P_ALERT_TEXT          OUT VARCHAR2);

END PKG_S01FRM00114;
```

### DEFINITIONS.PKG_S01FRM00172
```sql
create or replace package definitions.PKG_S01FRM00172 is
  -- Author  : IRFAN ALI
  -- Created : 10/16/2017 3:29:43 PM
  -- Purpose :

  ---------------- New panel ------------------

  TYPE REPORTING_PANEL_REC IS RECORD(
    NATURE_ID       DIAGNOSTIC.REPORTING_PANEL.DEPARTMENT_NATURE_ID%TYPE,
    PANEL_ID        DIAGNOSTIC.REPORTING_PANEL.PANEL_ID%TYPE,
    PANEL_DESC      DIAGNOSTIC.REPORTING_PANEL.PANEL_DESC%TYPE,
    CHECK_BOX_FINAL DIAGNOSTIC.REPORTING_PANEL.FINAL%TYPE,
    ACTIVE          DIAGNOSTIC.REPORTING_PANEL.ACTIVE%TYPE,
    ACTIVE_DATE     DIAGNOSTIC.REPORTING_PANEL.ACTIVE_DATE%TYPE,
    LOCATION_ID     DIAGNOSTIC.REPORTING_PANEL.LOCATION_ID%TYPE,
    LOCATION_DESC   DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  TYPE REPORTING_PANEL_REF IS REF CURSOR; --RETURN REPORTING_PANEL_REC;
  TYPE REPORTING_PANEL_TAB IS TABLE OF REPORTING_PANEL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE REPORTING_PANEL_QRY(P_RESULT          IN OUT REPORTING_PANEL_REF,
                                P_NATURE_ID       IN VARCHAR2,
                                P_PANEL_ID        IN VARCHAR2,
                                P_PANEL_DESC      IN VARCHAR2,
                                P_CHECK_BOX_FINAL IN VARCHAR2,
                                P_ACTIVE          IN VARCHAR2,
                                P_ACTIVE_DATE     IN VARCHAR2,
                                P_CALLING_OBJECT  IN VARCHAR2,
                                P_CALLING_USER    IN VARCHAR2,
                                P_ERROR           OUT VARCHAR2,
                                P_CALLING_EVENT   IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_INSERT(P_RESULT         IN OUT REPORTING_PANEL_TAB,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2,
                                   P_ERROR          OUT VARCHAR2,
                                   P_PANEL_ID       OUT VARCHAR2);

  PROCEDURE REPORTING_PANEL_UPDATE(P_RESULT         IN OUT REPORTING_PANEL_TAB,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_ERROR          OUT VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_DELETE(P_RESULT         IN OUT REPORTING_PANEL_TAB,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_ERROR          OUT VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_LOCK(P_RESULT         IN OUT REPORTING_PANEL_TAB,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_ERROR          OUT VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2);

  ----------------------------------------------------------------

  ---------------- Doctor associated with panel ------------------

  TYPE REPORTING_PANEL_DETAIL_REC IS RECORD(
    PANEL_ID        DIAGNOSTIC.REPORTING_PANEL_DETAIL.PANEL_ID%TYPE,
    DOCTOR_MRNO     DIAGNOSTIC.REPORTING_PANEL_DETAIL.DOCTOR_MRNO%TYPE,
    DOCTOR_MRNO_OLD DIAGNOSTIC.REPORTING_PANEL_DETAIL.DOCTOR_MRNO%TYPE,
    DISP_MRNO       DIAGNOSTIC.REPORTING_PANEL_DETAIL.DOCTOR_MRNO%TYPE,
    DOCTOR_NAME     DIAGNOSTIC.REPORTING_PANEL_DETAIL.DOCTOR_NAME%TYPE,
    TITLE           DIAGNOSTIC.REPORTING_PANEL_DETAIL.TITLE%TYPE,
    DESCRIPTION     DIAGNOSTIC.REPORTING_PANEL_DETAIL.DESCRIPTION%TYPE,
    ORDER_BY        DIAGNOSTIC.REPORTING_PANEL_DETAIL.ORDER_BY%TYPE);

  TYPE REPORTING_PANEL_DETAIL_REF IS REF CURSOR RETURN REPORTING_PANEL_DETAIL_REC;
  TYPE REPORTING_PANEL_DETAIL_TAB IS TABLE OF REPORTING_PANEL_DETAIL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE REPORTING_PANEL_DETAIL_QRY(P_RESULT         IN OUT REPORTING_PANEL_DETAIL_REF,
                                       P_PANEL_ID       IN VARCHAR2,
                                       P_DOCTOR_MRNO    IN VARCHAR2,
                                       P_DOCTOR_NAME    IN VARCHAR2,
                                       P_CALLING_OBJECT IN VARCHAR2,
                                       P_CALLING_USER   IN VARCHAR2,
                                       P_ERROR          OUT VARCHAR2,
                                       P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_DETAIL_INSERT(P_RESULT         IN OUT REPORTING_PANEL_DETAIL_TAB,
                                          P_CALLING_OBJECT IN VARCHAR2,
                                          P_CALLING_USER   IN VARCHAR2,
                                          P_ERROR          OUT VARCHAR2,
                                          P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_DETAIL_UPDATE(P_RESULT         IN OUT REPORTING_PANEL_DETAIL_TAB,
                                          P_CALLING_OBJECT IN VARCHAR2,
                                          P_CALLING_USER   IN VARCHAR2,
                                          P_ERROR          OUT VARCHAR2,
                                          P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_DETAIL_DELETE(P_RESULT         IN OUT REPORTING_PANEL_DETAIL_TAB,
                                          P_CALLING_OBJECT IN VARCHAR2,
                                          P_CALLING_USER   IN VARCHAR2,
                                          P_ERROR          OUT VARCHAR2,
                                          P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE REPORTING_PANEL_DETAIL_LOCK(P_RESULT         IN OUT REPORTING_PANEL_DETAIL_TAB,
                                        P_CALLING_OBJECT IN VARCHAR2,
                                        P_CALLING_USER   IN VARCHAR2,
                                        P_ERROR          OUT VARCHAR2,
                                        P_CALLING_EVENT  IN VARCHAR2);

  --------------------------------------------------------------------

  ------------------------- Nature detail panel -----------------------

  TYPE NATURE_DETAIL_PANEL_REC IS RECORD(
    NATURE_ID          DIAGNOSTIC.NATURE_DETAIL_PANEL.DEPARTMENT_NATURE_ID%TYPE,
    NATURE_DETAIL_ID   DIAGNOSTIC.NATURE_DETAIL_PANEL.NATURE_DETAIL_ID%TYPE,
    NATURE_DETAIL_DESC DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    PANEL_ID           DIAGNOSTIC.NATURE_DETAIL_PANEL.PANEL_ID%TYPE,
    ACTIVE_DATE        DIAGNOSTIC.NATURE_DETAIL_PANEL.ACTIVE_DATE%TYPE,
    DEACTIVE_DATE      DIAGNOSTIC.NATURE_DETAIL_PANEL.DEACTIVE_DATE%TYPE);

  TYPE NATURE_DETAIL_PANEL_REF IS REF CURSOR RETURN NATURE_DETAIL_PANEL_REC;
  TYPE NATURE_DETAIL_PANEL_TAB IS TABLE OF NATURE_DETAIL_PANEL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE NATURE_DETAIL_PANEL_QRY(P_RESULT             IN OUT NATURE_DETAIL_PANEL_REF,
                                    P_NATURE_ID          IN VARCHAR2,
                                    P_NATURE_DETAIL_ID   IN VARCHAR2,
                                    P_NATURE_DETAIL_DESC IN VARCHAR2,
                                    P_PANEL_ID           IN VARCHAR2,
                                    P_ACTIVE_DATE        IN VARCHAR2,
                                    P_DEACTIVE_DATE      IN VARCHAR2,
                                    P_CALLING_OBJECT     IN VARCHAR2,
                                    P_CALLING_USER       IN VARCHAR2,
                                    P_ERROR              OUT VARCHAR2,
                                    P_CALLING_EVENT      IN VARCHAR2);

  PROCEDURE NATURE_DETAIL_PANEL_INSERT(P_RESULT         IN OUT NATURE_DETAIL_PANEL_TAB,
                                       P_CALLING_OBJECT IN VARCHAR2,
                                       P_CALLING_USER   IN VARCHAR2,
                                       P_ERROR          OUT VARCHAR2,
                                       P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE NATURE_DETAIL_PANEL_UPDATE(P_RESULT         IN OUT NATURE_DETAIL_PANEL_TAB,
                                       P_CALLING_OBJECT IN VARCHAR2,
                                       P_CALLING_USER   IN VARCHAR2,
                                       P_ERROR          OUT VARCHAR2,
                                       P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE NATURE_DETAIL_PANEL_DELETE(P_RESULT         IN OUT NATURE_DETAIL_PANEL_TAB,
                                       P_CALLING_OBJECT IN VARCHAR2,
                                       P_CALLING_USER   IN VARCHAR2,
                                       P_ERROR          OUT VARCHAR2,
                                       P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE NATURE_DETAIL_PANEL_LOCK(P_RESULT         IN OUT NATURE_DETAIL_PANEL_TAB,
                                     P_CALLING_OBJECT IN VARCHAR2,
                                     P_CALLING_USER   IN VARCHAR2,
                                     P_ERROR          OUT VARCHAR2,
                                     P_CALLING_EVENT  IN VARCHAR2);

  --------------------------------------------------------------------------

  ------------------- Department wise panel ---------------------------------

  TYPE DEPT_PANEL_REC IS RECORD(
    NATURE_ID       DIAGNOSTIC.DEPT_WISE_PANEL.DEPARTMENT_NATURE_ID%TYPE,
    DEPARTMENT_ID   DIAGNOSTIC.DEPT_WISE_PANEL.DEPARTMENT_ID%TYPE,
    DEPARTMENT_DESC DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    PANEL_ID        DIAGNOSTIC.DEPT_WISE_PANEL.PANEL_ID%TYPE,
    ACTIVE_DATE     DIAGNOSTIC.DEPT_WISE_PANEL.ACTIVE_DATE%TYPE,
    DEACTIVE_DATE   DIAGNOSTIC.DEPT_WISE_PANEL.DEACTIVE_DATE%TYPE);

  TYPE DEPT_PANEL_REF IS REF CURSOR RETURN DEPT_PANEL_REC;
  TYPE DEPT_PANEL_TAB IS TABLE OF DEPT_PANEL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE DEPT_PANEL_QRY(P_RESULT         IN OUT DEPT_PANEL_REF,
                           P_NATURE_ID      IN VARCHAR2,
                           P_DEPARTMENT_ID  IN VARCHAR2,
                           P_DEPT_DESC      IN VARCHAR2,
                           P_PANEL_ID       IN VARCHAR2,
                           P_ACTIVE_DATE    IN VARCHAR2,
                           P_DEACTIVE_DATE  IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE DEPT_PANEL_INSERT(P_RESULT         IN OUT DEPT_PANEL_TAB,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_ERROR          OUT VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE DEPT_PANEL_UPDATE(P_RESULT         IN OUT DEPT_PANEL_TAB,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_ERROR          OUT VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE DEPT_PANEL_DELETE(P_RESULT         IN OUT DEPT_PANEL_TAB,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_ERROR          OUT VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE DEPT_PANEL_LOCK(P_RESULT         IN OUT DEPT_PANEL_TAB,
                            P_CALLING_OBJECT IN VARCHAR2,
                            P_CALLING_USER   IN VARCHAR2,
                            P_ERROR          OUT VARCHAR2,
                            P_CALLING_EVENT  IN VARCHAR2);

  ---------------------------------------------------------------------

  -------------------- Section wise panel ------------------------------

  TYPE SECTION_PANEL_REC IS RECORD(
    DEPARTMENT_NATURE_ID DIAGNOSTIC.SECTION_WISE_PANEL.DEPARTMENT_NATURE_ID%TYPE,
    DEPARTMENT_ID        DIAGNOSTIC.SECTION_WISE_PANEL.DEPARTMENT_ID%TYPE,
    SECTION_ID           DIAGNOSTIC.SECTION_WISE_PANEL.SECTION_ID%TYPE,
    DESCRIPTION          DEFINITIONS.DEPARTMENT_SECTION.DESCRIPTION%TYPE,
    PANEL_ID             DIAGNOSTIC.SECTION_WISE_PANEL.PANEL_ID%TYPE,
    ACTIVE_DATE          DIAGNOSTIC.SECTION_WISE_PANEL.ACTIVE_DATE%TYPE,
    DEACTIVE_DATE        DIAGNOSTIC.SECTION_WISE_PANEL.DEACTIVE_DATE%TYPE);

  TYPE SECTION_PANEL_REF IS REF CURSOR RETURN SECTION_PANEL_REC;
  TYPE SECTION_PANEL_TAB IS TABLE OF SECTION_PANEL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE SECTION_PANEL_QRY(P_RESULT         IN OUT SECTION_PANEL_REF,
                              P_NATURE_ID      IN VARCHAR2,
                              P_DEPARTMENT_ID  IN VARCHAR2,
                              P_SECTION_ID     IN VARCHAR2,
                              P_DESCRIPTION    IN VARCHAR2,
                              P_PANEL_ID       IN VARCHAR2,
                              P_ACTIVE_DATE    IN VARCHAR2,
                              P_DEACTIVE_DATE  IN VARCHAR2,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_ERROR          OUT VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE SECTION_PANEL_INSERT(P_RESULT         IN OUT SECTION_PANEL_TAB,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_ERROR          OUT VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE SECTION_PANEL_UPDATE(P_RESULT         IN OUT SECTION_PANEL_TAB,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_ERROR          OUT VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE SECTION_PANEL_DELETE(P_RESULT         IN OUT SECTION_PANEL_TAB,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_ERROR          OUT VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE SECTION_PANEL_LOCK(P_RESULT         IN OUT SECTION_PANEL_TAB,
                               P_CALLING_OBJECT IN VARCHAR2,
                               P_CALLING_USER   IN VARCHAR2,
                               P_ERROR          OUT VARCHAR2,
                               P_CALLING_EVENT  IN VARCHAR2);

  ----------------------------------------------------------------

  -------------------- CPT wise panel -----------------------------

  TYPE CPT_PANEL_REC IS RECORD(
    CPT_ID        DIAGNOSTIC.CPT_WISE_PANEL.CPT_ID%TYPE,
    CPT_CODE      DIAGNOSTIC.CPT_WISE_PANEL.CPT_ID%TYPE,
    CPT_DESC      DEFINITIONS.CPT.SHORT_DESC%TYPE,
    PANEL_ID      DIAGNOSTIC.CPT_WISE_PANEL.PANEL_ID%TYPE,
    ACTIVE_DATE   DIAGNOSTIC.CPT_WISE_PANEL.ACTIVE_DATE%TYPE,
    DEACTIVE_DATE DIAGNOSTIC.CPT_WISE_PANEL.DEACTIVE_DATE%TYPE);

  TYPE CPT_PANEL_REF IS REF CURSOR RETURN CPT_PANEL_REC;
  TYPE CPT_PANEL_TAB IS TABLE OF CPT_PANEL_REC INDEX BY BINARY_INTEGER;

  PROCEDURE CPT_PANEL_QRY(P_RESULT         IN OUT CPT_PANEL_REF,
                          P_CPT_ID         IN VARCHAR2,
                          P_CPT_CODE       IN VARCHAR2,
                          P_PANEL_ID       IN VARCHAR2,
                          P_ACTIVE_DATE    IN VARCHAR2,
                          P_DEACTIVE_DATE  IN VARCHAR2,
                          P_CALLING_OBJECT IN VARCHAR2,
                          P_CALLING_USER   IN VARCHAR2,
                          P_ERROR          OUT VARCHAR2,
                          P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE CPT_PANEL_INSERT(P_RESULT         IN OUT CPT_PANEL_TAB,
                             P_CALLING_OBJECT IN VARCHAR2,
                             P_CALLING_USER   IN VARCHAR2,
                             P_ERROR          OUT VARCHAR2,
                             P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE CPT_PANEL_UPDATE(P_RESULT         IN OUT CPT_PANEL_TAB,
                             P_CALLING_OBJECT IN VARCHAR2,
                             P_CALLING_USER   IN VARCHAR2,
                             P_ERROR          OUT VARCHAR2,
                             P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE CPT_PANEL_DELETE(P_RESULT         IN OUT CPT_PANEL_TAB,
                             P_CALLING_OBJECT IN VARCHAR2,
                             P_CALLING_USER   IN VARCHAR2,
                             P_ERROR          OUT VARCHAR2,
                             P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE CPT_PANEL_LOCK(P_RESULT         IN OUT CPT_PANEL_TAB,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2);

  -----------------------------------------------------------------
  FUNCTION PANEL_MEMBERS_LIMIT(P_NATURE_ID IN VARCHAR2,
                               P_RECORD_NO IN NUMBER,
                               P_ERROR     OUT VARCHAR2) RETURN BOOLEAN;
  -----------------------------------------------------------------
  FUNCTION DUPLICATE_PANEL(P_SOURCE_PANEL_ID IN VARCHAR2,
                           P_NEW_NATURE_ID   IN VARCHAR2,
                           P_CALLING_OBJECT  IN VARCHAR2,
                           P_CALLING_USER    IN VARCHAR2,
                           P_CAlLING_EVENT   IN VARCHAR2,
                           P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  --------------------------------------------------------------------
  FUNCTION ACTIVATE_PANEL(P_PANEL_ID       IN VARCHAR2,
                          P_CALLING_OBJECT IN VARCHAR2,
                          P_CALLING_USER   IN VARCHAR2,
                          P_CAlLING_EVENT  IN VARCHAR2,
                          P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  ---------------------------------------------------------------------

  --------------------------------------------------------------------

  ------------------------- Nature detail panel -----------------------

  TYPE LP_REC IS RECORD(
    PANEL_LOCATION_ID DIAGNOSTIC.LOCATION_WISE_PANEL.PANEL_LOCATION_ID%TYPE,
    LOCATION_DESC     VARCHAR2(160),
    PANEL_ID          DIAGNOSTIC.LOCATION_WISE_PANEL.PANEL_ID%TYPE,
    NATURE_ID         DIAGNOSTIC.NATURE_DETAIL_PANEL.DEPARTMENT_NATURE_ID%TYPE,
    ACTIVE_DATE       DIAGNOSTIC.LOCATION_WISE_PANEL.ACTIVE_DATE%TYPE,
    DEACTIVE_DATE     DIAGNOSTIC.LOCATION_WISE_PANEL.DEACTIVE_DATE%TYPE);

  TYPE LP_REF IS REF CURSOR RETURN LP_REC;
  TYPE LP_TAB IS TABLE OF LP_REC INDEX BY BINARY_INTEGER;

  PROCEDURE LP_QUERY(P_RESULT         IN OUT LP_REF,
                     P_NATURE_ID      IN VARCHAR2,
                     P_PANEL_ID       IN VARCHAR2,
                     P_LOCATION_ID    IN VARCHAR2,
                     P_CALLING_OBJECT IN VARCHAR2,
                     P_CALLING_USER   IN VARCHAR2,
                     P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE LP_INSERT(P_RESULT         IN OUT LP_TAB,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE LP_UPDATE(P_RESULT         IN OUT LP_TAB,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE LP_DELETE(P_RESULT         IN OUT LP_TAB,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2);

  PROCEDURE LP_LOCK(P_RESULT IN OUT LP_TAB);

END PKG_S01FRM00172;
```

### DEFINITIONS.PKG_S01FRM00292
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00292 AS

  /*---------------------------
  OBJECTIVE: THIS PACKAGE IS WRITTEN FOR S01FRM00292 IN WHICH WE DEFINES THE LOCATION PARAMERTERS OF CHILD FORM
  DEVELOPED BY: FARHAN AKRAM (6-5156)
  SUPERVISED BY: QAISER HUSSAIN
  DATED: 07/10/2011
  ----------------------------*/
  TYPE TYPE_OBJ_PARAM_REC IS RECORD(
    ROW_ID              ROWID,
    OBJECT_CODE         DEFINITIONS.CALLED_OBJECT_PARAMETERS.OBJECT_CODE%TYPE,
    OBJECT_DESC         definitions.objects.name%TYPE,
    CALLING_OBJECT_CODE DEFINITIONS.CALLED_OBJECT_PARAMETERS.CALLING_OBJECT_CODE%TYPE,
    CALLING_OBJECT_DESC definitions.objects.name%TYPE,
    WIN_X_POS           DEFINITIONS.CALLED_OBJECT_PARAMETERS.WIN_X_POS%TYPE,
    WIN_Y_POS           DEFINITIONS.CALLED_OBJECT_PARAMETERS.WIN_Y_POS%TYPE,
    WIN_WIDTH           DEFINITIONS.CALLED_OBJECT_PARAMETERS.WIN_WIDTH%TYPE,
    WIN_HEIGHT          DEFINITIONS.CALLED_OBJECT_PARAMETERS.WIN_HEIGHT%TYPE);

  TYPE TYPE_OBJ_PARAM_TABLE IS TABLE OF TYPE_OBJ_PARAM_REC INDEX BY BINARY_INTEGER;

  PROCEDURE QUERY_OBJ_PARAM(P_RESULT   IN OUT TYPE_OBJ_PARAM_TABLE,
                            P_WHERE    IN VARCHAR2,
                            P_ORDER_BY IN VARCHAR2);

  PROCEDURE INSERT_OBJ_PARAM(P_BLOCK_DATA IN OUT TYPE_OBJ_PARAM_TABLE,
                             P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE UPDATE_OBJ_PARAM(P_BLOCK_DATA IN OUT TYPE_OBJ_PARAM_TABLE,
                             P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE DELETE_OBJ_PARAM(P_BLOCK_DATA IN OUT TYPE_OBJ_PARAM_TABLE,
                             P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE LOCK_OBJ_PARAM(P_BLOCK_DATA IN OUT TYPE_OBJ_PARAM_TABLE,
                           P_ALERT_TEXT OUT VARCHAR2);

END PKG_S01FRM00292;
```

### DEFINITIONS.PKG_S01FRM00293
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00293 AS
  --------------------------------------------------------------------------
  --
  -- MODULE NAME: DEFINITIONS
  -- DESCRIPTION: THIS FORM WILL BE USED FOR THE SETUP FOR SURGERY AND SURGICAL SITE INFECTION
  --              THIS FORM MUST CONTAIN ONLY ONE ROW
  -- Revision:    1.0
  -- Date:        14-OCT-11
  -- Author:      RIZWAN MUGHAL
  -- DESCRIPTION: THIS PACKAGE WILL BE USED IN S01FRM00293 FORM
  --
  -- CHANGE HISTORY
  -- Date        Author                     Version    Change
  --
  --------------------------------------------------------------------------
  TYPE REC_SURGERY_SETUP IS RECORD(
    GROUP_ID       DEFINITIONS.SURGERY_SETUP.GROUP_ID%TYPE,
    GROUP_DESC     PHARMACY.THERAPEUTIC_GROUP.DESCRIPTION%TYPE,
    SUB_GROUP_ID   DEFINITIONS.SURGERY_SETUP.SUB_GROUP_ID%TYPE,
    SUB_GROUP_DESC PHARMACY.THERAPEUTIC_SUBGROUP.DESCRIPTION%TYPE,
    PAT_SECTION_ID DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE);
  -- Reference Cursor  
  TYPE REF_SURGERY_SETUP IS REF CURSOR RETURN REC_SURGERY_SETUP;
  -- Query Procedure
  PROCEDURE QUERY_SURGERY_SETUP(P_RESULT       IN OUT REF_SURGERY_SETUP,
                                P_GROUP_ID     IN  VARCHAR2,
                                P_SUB_GROUP_ID IN  VARCHAR2,
                                P_ALERT_TEXT   OUT VARCHAR2);
  -- Table of Records
  TYPE SURGERY_SETUP_TAB IS TABLE OF REC_SURGERY_SETUP INDEX BY BINARY_INTEGER;
  -- Insert Procedure
  PROCEDURE INSERT_SURGERY_SETUP(P_RESULT     IN OUT SURGERY_SETUP_TAB,
                                 P_ALERT_TEXT OUT VARCHAR2);
  
  -- Update Procedure                              
  PROCEDURE UPDATE_SURGERY_SETUP(P_RESULT     IN OUT SURGERY_SETUP_TAB,
                                 P_ALERT_TEXT OUT VARCHAR2);
  -- Lock Procedure
  PROCEDURE LOCK_SURGERY_SETUP(P_RESULT     IN OUT SURGERY_SETUP_TAB,
                               P_ALERT_TEXT OUT VARCHAR2);
END;
```

### DEFINITIONS.PKG_S01FRM00303
```sql
create or replace package definitions.PKG_S01FRM00303 is

  -- Author  : RAZAHASSAN
  -- Created : 1/17/2013 10:58:48 AM
  -- Purpose :
  TYPE APP_SERVER_REC IS RECORD(
    SERVER_ID            DEFINITIONS.APPLICATION_SERVERS.SERVER_ID%TYPE,
    DESCRIPTION          DEFINITIONS.APPLICATION_SERVERS.DESCRIPTION%TYPE,
    SHORT_DESC           DEFINITIONS.APPLICATION_SERVERS.SHORT_DESC%TYPE,
    DEV_TOOL_ID          DEFINITIONS.APPLICATION_SERVERS.DEV_TOOL_ID%TYPE,
    ACTIVE               DEFINITIONS.APPLICATION_SERVERS.ACTIVE%TYPE,
    CHECK_AUTHENTICATION DEFINITIONS.APPLICATION_SERVERS.CHECK_AUTHENTICATION%TYPE,
    EXTERNAL_IP_ADDRESS  DEFINITIONS.APPLICATION_SERVERS.EXTERNAL_IP_ADDRESS%TYPE,
    EXTERNAL_URL         DEFINITIONS.APPLICATION_SERVERS.EXTERNAL_URL%TYPE,
    INTERNAL_IP_ADDRESS  DEFINITIONS.APPLICATION_SERVERS.INTERNAL_IP_ADDRESS%TYPE,
    INTERNAL_URL         DEFINITIONS.APPLICATION_SERVERS.INTERNAL_URL%TYPE,
    DEV_TOOL             DEFINITIONS.DEVELOPMENT_TOOLS.DEV_TOOL%TYPE,
    AUTO_RIGHTS          DEFINITIONS.APPLICATION_SERVERS.AUTO_RIGHTS%TYPE);

  TYPE APP_SERVER_CUR IS REF CURSOR RETURN APP_SERVER_REC;
  TYPE APP_SERVER_TAB IS TABLE OF APP_SERVER_REC INDEX BY BINARY_INTEGER;

  PROCEDURE APP_SERVER_QUERY_REFCUR(APP_SERVER_DATA        IN OUT APP_SERVER_CUR,
                                    P_DESCRIPTION          DEFINITIONS.APPLICATION_SERVERS.DESCRIPTION%TYPE,
                                    P_SHORT_DESC           DEFINITIONS.APPLICATION_SERVERS.SHORT_DESC%TYPE,
                                    P_DEV_TOOL_ID          DEFINITIONS.APPLICATION_SERVERS.DEV_TOOL_ID%TYPE,
                                    P_ACTIVE               DEFINITIONS.APPLICATION_SERVERS.ACTIVE%TYPE,
                                    P_CHECK_AUTHENTICATION DEFINITIONS.APPLICATION_SERVERS.CHECK_AUTHENTICATION%TYPE,
                                    P_DEV_TOOL             DEFINITIONS.DEVELOPMENT_TOOLS.DEV_TOOL%TYPE,
                                    P_SERVER_ID            DEFINITIONS.APPLICATION_SERVERS.SERVER_ID%TYPE,
                                    P_INTERNAL_IP          DEFINITIONS.APPLICATION_SERVERS.INTERNAL_IP_ADDRESS%TYPE,
                                    P_EXTERNAL_IP          DEFINITIONS.APPLICATION_SERVERS.EXTERNAL_IP_ADDRESS%TYPE,
                                    P_AUTO_RIGHTS          DEFINITIONS.APPLICATION_SERVERS.AUTO_RIGHTS%TYPE);
  PROCEDURE APP_SERVER_INSERT(R            IN OUT APP_SERVER_TAB,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_SERVER_LOCK(R            IN OUT APP_SERVER_TAB,
                            P_STOP       OUT VARCHAR2,
                            P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_SERVER_UPDATE(T            IN OUT APP_SERVER_TAB,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_SERVER_DELETE(T            IN OUT APP_SERVER_TAB,
                              P_STOP       OUT VARCHAR2,
                              P_ALERT_TEXT OUT VARCHAR2);

end;
```

### DEFINITIONS.PKG_S01FRM00304
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00304 IS

  -- Author  : ABDOON ORIAM
  -- Created : 15-FEBRARY-2013 11:00:50 AM
  -- Purpose : This Package contains two Functions used in SYSTEM_CONSTANTS.fmb 
  -----------------------------------------------------------------------------------
  FUNCTION GET_OBJECT_NAME(P_OBJECT_CODE VARCHAR2) RETURN VARCHAR2;
  -----------------------------------------------------------------------------------
  FUNCTION GET_SCHEMA_NAME(P_SCHEMA_ID VARCHAR2) RETURN VARCHAR2;
  -----------------------------------------------------------------------------------
  FUNCTION GET_UNIT_DESC(P_UNIT_ID VARCHAR2) RETURN VARCHAR2;
END PKG_S01FRM00304;
```

### DEFINITIONS.PKG_S01FRM00306
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00306 IS

  TYPE OR_MASTER_RECORD IS RECORD(
    ORGANIZATION_ID     DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
    DESCRIPTION         DEFINITIONS.ORGANIZATION.DESCRIPTION%TYPE,
    DEFAULT_LOCATION_ID DEFINITIONS.ORGANIZATION.DEFAULT_LOCATION_ID%TYPE,
    ACTIVE              DEFINITIONS.ORGANIZATION.ACTIVE%TYPE,
    SHOW_PENDING_TASKS  DEFINITIONS.ORGANIZATION.SHOW_PENDING_TASKS%TYPE,
    SHOW_EMP_PIC        DEFINITIONS.ORGANIZATION.SHOW_EMP_PIC%TYPE
    
    );

  TYPE OR_MASTER_CUR IS REF CURSOR RETURN OR_MASTER_RECORD;
  TYPE OR_MASTER_TAB IS TABLE OF OR_MASTER_RECORD INDEX BY BINARY_INTEGER;

/******************************************************************************/
  -- Author    : ASMA HASHMI (4806)  Created on: 17-APR-2013
  -- Scope     : DEFINITIONS.ORGANIZATION
  -- Purpose   : This procedure will be used for defining new organizations in the system.
/******************************************************************************/

  PROCEDURE OR_MASTER_REFCUR(OR_MASTER_DATA        IN OUT OR_MASTER_CUR,
                             P_ORGANIZATION_ID     DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_DESCRIPTION         DEFINITIONS.ORGANIZATION.DESCRIPTION%TYPE,
                             P_DEFAULT_LOCATION_ID DEFINITIONS.ORGANIZATION.DEFAULT_LOCATION_ID%TYPE,
                             P_ACTIVE              DEFINITIONS.ORGANIZATION.ACTIVE%TYPE);

/******************************************************************************/
  -- Author    : ASMA HASHMI (4806)  Created on: 17-APR-2013
  -- Scope     : DEFINITIONS.ORGANIZATION
  -- Purpose   : INSERTING RECORD.
/******************************************************************************/

  PROCEDURE OR_MASTER_INSERT(R                     IN OR_MASTER_TAB,
                             P_STOP                OUT VARCHAR2,
                             P_ALERT_TEXT          OUT VARCHAR2,
                             P_ORGANIZATION_ID_OUT OUT NUMBER);

/******************************************************************************/
  -- Author    : ASMA HASHMI (4806)  Created on: 17-APR-2013
  -- Scope     : DEFINITIONS.ORGANIZATION
  -- Purpose   : FOR LOCKING.
/******************************************************************************/

  PROCEDURE OR_MASTER_LOCK(R            IN OUT OR_MASTER_TAB,
                           P_STOP       OUT VARCHAR2,
                           P_ALERT_TEXT OUT VARCHAR2);

/******************************************************************************/
  -- Author    : ASMA HASHMI (4806)  Created on: 17-APR-2013
  -- Scope     : DEFINITIONS.ORGANIZATION
  -- Purpose   : UPDATING RECORD.
/******************************************************************************/

  PROCEDURE OR_MASTER_UPDATE(T            IN OR_MASTER_TAB,
                             P_STOP       OUT VARCHAR2,
                             P_ALERT_TEXT OUT VARCHAR2);

/******************************************************************************/
  -- Author    : ASMA HASHMI (4806)  Created on: 17-APR-2013
  -- Scope     : DEFINITIONS.ORGANIZATION
  -- Purpose   : DELETING RECORD.
/******************************************************************************/

  PROCEDURE OR_MASTER_DELETE(T            IN OR_MASTER_TAB,
                             P_STOP       OUT VARCHAR2,
                             P_ALERT_TEXT OUT VARCHAR2);

END;
```

### DEFINITIONS.PKG_S01FRM00308
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00308 IS

  -- Author  : KHIZAR KHALID
  -- Created : 7/5/2013 5:16:48 PM
  -- Purpose :

  TYPE APP_TOKEN_TYPE_REC IS RECORD(
    TOKEN_TYPE_ID          DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
    TOKEN_TYPE_DESCRIPTION DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_DESCRIPTION%TYPE,
    DEPARTMENT_ID          DEFINITIONS.TOKEN_TYPE.DEPARTMENT_ID%TYPE,
    BUTTON_LABEL           DEFINITIONS.TOKEN_TYPE.BUTTON_LABEL%TYPE,
    BUTTON_DESCRIPTION     DEFINITIONS.TOKEN_TYPE.BUTTON_DESCRIPTION%TYPE,
    MRNO_IS_REQUIRED       DEFINITIONS.TOKEN_TYPE.MRNO_IS_REQUIRED%TYPE,
    ACTIVE                 DEFINITIONS.TOKEN_TYPE.ACTIVE%TYPE,
    LOCATION_ID            DEFINITIONS.TOKEN_TYPE.LOCATION_ID%TYPE,
    ORDER_LOCATION_ID      DEFINITIONS.TOKEN_TYPE.ORDER_LOCATION_ID%TYPE,
    BUTTON_LABEL_URDU      DEFINITIONS.TOKEN_TYPE.BUTTON_LABEL_URDU%TYPE,
    LOCATION               DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
    DEPARTMENT_NAME        DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    SHOW_CLINIC_NAME       DEFINITIONS.TOKEN_TYPE.SHOW_CLINIC_NAME%TYPE);

  TYPE APP_TOKEN_TYPE_REFCUR IS REF CURSOR RETURN APP_TOKEN_TYPE_REC;
  TYPE APP_TOKEN_TYPE_TAB IS TABLE OF APP_TOKEN_TYPE_REC INDEX BY BINARY_INTEGER;
  TYPE APP_TOKEN_TYPE_TAB_PF IS TABLE OF APP_TOKEN_TYPE_REC;

  FUNCTION F_TOKEN_TYPE_QRY(P_TOKEN_TYPE_ID          DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
                            P_TOKEN_TYPE_DESCRIPTION DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_DESCRIPTION%TYPE,
                            P_DEPARTMENT_ID          DEFINITIONS.TOKEN_TYPE.DEPARTMENT_ID%TYPE,
                            P_BUTTON_DESCRIPTION     DEFINITIONS.TOKEN_TYPE.BUTTON_DESCRIPTION%TYPE,
                            P_MRNO_IS_REQUIRED       DEFINITIONS.TOKEN_TYPE.MRNO_IS_REQUIRED%TYPE,
                            P_ACTIVE                 DEFINITIONS.TOKEN_TYPE.ACTIVE%TYPE,
                            P_ORDER_LOCATION         DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
                            P_DEPARTMENT             DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                            P_BUTTON_LABEL           DEFINITIONS.TOKEN_TYPE.BUTTON_LABEL%TYPE)
    RETURN APP_TOKEN_TYPE_TAB_PF
    PIPELINED;
  PROCEDURE APP_TOKEN_TYPE_QRY(QUERY_DATA               IN OUT APP_TOKEN_TYPE_TAB,
                               P_TOKEN_TYPE_ID          DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
                               P_TOKEN_TYPE_DESCRIPTION DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_DESCRIPTION%TYPE,
                               P_DEPARTMENT_ID          DEFINITIONS.TOKEN_TYPE.DEPARTMENT_ID%TYPE,
                               P_BUTTON_DESCRIPTION     DEFINITIONS.TOKEN_TYPE.BUTTON_DESCRIPTION%TYPE,
                               P_MRNO_IS_REQUIRED       DEFINITIONS.TOKEN_TYPE.MRNO_IS_REQUIRED%TYPE,
                               P_ACTIVE                 DEFINITIONS.TOKEN_TYPE.ACTIVE%TYPE,
                               P_ORDER_LOCATION         DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
                               P_DEPARTMENT             DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                               P_BUTTON_LABEL           DEFINITIONS.TOKEN_TYPE.BUTTON_LABEL%TYPE);

  PROCEDURE APP_TOKEN_TYPE_QUERY_REFCUR(QUERY_DATA               IN OUT APP_TOKEN_TYPE_REFCUR,
                                        P_TOKEN_TYPE_ID          DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
                                        P_TOKEN_TYPE_DESCRIPTION DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_DESCRIPTION%TYPE,
                                        P_DEPARTMENT_ID          DEFINITIONS.TOKEN_TYPE.DEPARTMENT_ID%TYPE,
                                        P_BUTTON_DESCRIPTION     DEFINITIONS.TOKEN_TYPE.BUTTON_DESCRIPTION%TYPE,
                                        P_MRNO_IS_REQUIRED       DEFINITIONS.TOKEN_TYPE.MRNO_IS_REQUIRED%TYPE,
                                        P_ACTIVE                 DEFINITIONS.TOKEN_TYPE.ACTIVE%TYPE,
                                        P_ORDER_LOCATION         DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
                                        P_DEPARTMENT             DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
                                        P_BUTTON_LABEL           DEFINITIONS.TOKEN_TYPE.BUTTON_LABEL%TYPE,
                                        P_SHOW_CLINIC_NAME       DEFINITIONS.TOKEN_TYPE.SHOW_CLINIC_NAME%TYPE);

  PROCEDURE APP_TOKEN_TYPE_INSERT(TAB          IN OUT APP_TOKEN_TYPE_TAB,
                                  P_STOP       OUT VARCHAR2,
                                  P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_LOCK(TAB          IN OUT APP_TOKEN_TYPE_TAB,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_UPDATE(TAB          IN OUT APP_TOKEN_TYPE_TAB,
                                  P_STOP       OUT VARCHAR2,
                                  P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_DELETE(TAB          IN OUT APP_TOKEN_TYPE_TAB,
                                  P_STOP       OUT VARCHAR2,
                                  P_ALERT_TEXT OUT VARCHAR2);
  --------------------------------------------------------------------------------------
  TYPE APP_TOKEN_TYPE_OBJCODE_REC IS RECORD(
    TOKEN_TYPE_ID     DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.TOKEN_TYPE_ID%TYPE,
    LOCATION_ID       DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.LOCATION_ID%TYPE,
    ORDER_LOCATION_ID DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.ORDER_LOCATION_ID%TYPE,
    OBJECT_CODE       DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.OBJECT_CODE%TYPE,
    ACTION            DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.ACTION%TYPE,
    OBJECT_NAME       DEFINITIONS.OBJECTS.NAME%TYPE,
    BUTTON_LABEL      DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.BUTTON_LABEL%TYPE,
    APEX_APP_ID       DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.APEX_APP_ID%TYPE,
    APEX_PAGE_ID       DEFINITIONS.TOKEN_TYPE_WISE_OBJCODE.APEX_PAGE_ID%TYPE);

  TYPE APP_TOKEN_TYPE_OBJCODE_REFCUR IS REF CURSOR RETURN APP_TOKEN_TYPE_OBJCODE_REC;
  TYPE APP_TOKEN_TYPE_OBJCODE_TAB IS TABLE OF APP_TOKEN_TYPE_OBJCODE_REC INDEX BY BINARY_INTEGER;

  PROCEDURE APP_TOKEN_TYPE_OBJCODE_QUERY(QUERY_DATA          IN OUT APP_TOKEN_TYPE_OBJCODE_REFCUR,
                                         p_token_type_id     definitions.token_type.token_type_id%type,
                                         p_location_id       definitions.token_type.location_id%type,
                                         p_order_location_id definitions.token_type.order_location_id%type);

  PROCEDURE APP_TOKEN_TYPE_OBJCODE_INSERT(TAB          IN OUT APP_TOKEN_TYPE_OBJCODE_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_OBJCODE_LOCK(TAB          IN OUT APP_TOKEN_TYPE_OBJCODE_TAB,
                                        P_STOP       OUT VARCHAR2,
                                        P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_OBJCODE_UPDATE(TAB          IN OUT APP_TOKEN_TYPE_OBJCODE_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE APP_TOKEN_TYPE_OBJCODE_DELETE(TAB          IN OUT APP_TOKEN_TYPE_OBJCODE_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************************/
  -- Author  : AQIB KHALID
  -- Created : 03-06-2020
  -- Purpose : TOKEN TYPE WISE CLINICS FOR SIUT

  TYPE TOKEN_TYPE_WISE_CLINIC_REC IS RECORD(
    TOKEN_TYPE_ID     DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
    LOCATION_ID       DEFINITIONS.TOKEN_TYPE.LOCATION_ID%TYPE,
    ORDER_LOCATION_ID DEFINITIONS.TOKEN_TYPE.ORDER_LOCATION_ID%TYPE,
    CLINIC_ID         REGISTRATION.CLINIC.CLINIC_ID%TYPE,
    CLINIC_NAME       REGISTRATION.CLINIC.NAME%TYPE,
    BUTTON_LABEL      DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.BUTTON_LABEL%TYPE,
    ACTIVE            DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.ACTIVE%TYPE);

  TYPE TOKEN_TYPE_WISE_CLINIC_REFCUR IS REF CURSOR RETURN TOKEN_TYPE_WISE_CLINIC_REC;
  TYPE TOKEN_TYPE_WISE_CLINIC_TAB IS TABLE OF TOKEN_TYPE_WISE_CLINIC_REC INDEX BY BINARY_INTEGER;

  PROCEDURE TOKEN_TYPE_WISE_CLINIC_QRY(QUERY_DATA          IN OUT TOKEN_TYPE_WISE_CLINIC_REFCUR,
                                       P_TOKEN_TYPE_ID     DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
                                       P_LOCATION_ID       DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.LOCATION_ID%TYPE,
                                       P_ORDER_LOCATION_ID DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.ORDER_LOCATION_ID%TYPE,
                                       P_CLINIC_ID         DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.CLINIC_ID%TYPE,
                                       P_CLINIC_NAME       REGISTRATION.CLINIC.NAME%TYPE,
                                       P_ACTIVE            DEFINITIONS.TOKEN_TYPE_WISE_CLINICS.ACTIVE%TYPE);

  PROCEDURE TOKEN_TYPE_WISE_CLINIC_INSERT(TAB          IN OUT TOKEN_TYPE_WISE_CLINIC_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE TOKEN_TYPE_WISE_CLINIC_LOCK(TAB          IN OUT TOKEN_TYPE_WISE_CLINIC_TAB,
                                        P_STOP       OUT VARCHAR2,
                                        P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE TOKEN_TYPE_WISE_CLINIC_UPDATE(TAB          IN OUT TOKEN_TYPE_WISE_CLINIC_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE TOKEN_TYPE_WISE_CLINIC_DELETE(TAB          IN OUT TOKEN_TYPE_WISE_CLINIC_TAB,
                                          P_STOP       OUT VARCHAR2,
                                          P_ALERT_TEXT OUT VARCHAR2);
  /*********************
  CREATE BY : AQIB (7346)
  FUNCTION : GET CLINIC NAME ORDER LOCATION WISE AS BUTTON DISPLAY NAME
    DATE : 04-06-2020
  *********************/
  FUNCTION F_GET_BUTTON_DISPLAY_NAME(P_TOKEN_TYPE_ID DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE)
    RETURN VARCHAR2;
  /***************************************************************************************/
  FUNCTION F_SHOW_TOKEN_TYPE(P_TOKEN_TYPE_ID DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE)
    RETURN VARCHAR2;
  /***************************************************************************************/
  --========================================================================
  TYPE COUNTER_QUEUE_PAT_REC IS RECORD(
    TOKEN_QUEUE_ID    HIS.TOKEN_QUEUE.TOKEN_QUEUE_ID%TYPE,
    TOKEN_NO          HIS.TOKEN_QUEUE.TOKEN_NO%TYPE,
    TOKEN_TYPE_ID     HIS.TOKEN_QUEUE.TOKEN_TYPE_ID%TYPE,
    CLINIC_NAME       VARCHAR2(500),
    LOCATION_ID       VARCHAR2(3),
    ORDER_LOCATION_ID VARCHAR2(3),
    TERMINAL_NAME     HIS.TOKEN_QUEUE.TERMINAL_NAME%TYPE,
    ENTRY_DATE        DATE,
    TOKEN_STATUS      HIS.TOKEN_QUEUE.TOKEN_STATUS%TYPE,
    COUNTER           MIS_INFO.PC_INFORMATION.COUNTER_NO%TYPE,
    RECEPTION_ID      DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
    SEQ_ID            DEFINITIONS.SEQUENCE_SETUP.SEQ_ID%TYPE,
    PROMPT_TEXT       DEFINITIONS.TOKEN_DISPLAY_COUNTER.PROMPT_TEXT%TYPE);

  TYPE COUNTER_QUEUE_PAT_CUR IS REF CURSOR RETURN COUNTER_QUEUE_PAT_REC;
  --
  --==================================================================
  PROCEDURE COUNTER_QUEUE_PAT_QUERY(COUNTER_ACT_PAT_DATA IN OUT COUNTER_QUEUE_PAT_CUR,
                                    P_ENTRY_DATE         IN DATE,
                                    P_LOCATION_ID        IN VARCHAR2,
                                    P_TERMINAL           IN VARCHAR2,
                                    P_ORDER_LOCATION_ID  IN VARCHAR2);
  --=====================================================================
  /***************************************************************************************/
  FUNCTION F_CHK_TOKEN_TYPE(P_TOKEN_TYPE_ID DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE,
                            P_CLINIC_ID     REGISTRATION.CLINIC.CLINIC_ID%TYPE)
    RETURN VARCHAR2;
  /***************************************************************************************/
  FUNCTION F_GET_CLINIC_DISPLAY_NAME(P_TOKEN_TYPE_ID DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE)
    RETURN VARCHAR2;
  /*********************/
  FUNCTION F_GET_BUTTON_DSPLY_NM_URDU(P_TOKEN_TYPE_ID DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_ID%TYPE)
    RETURN VARCHAR2;
  /***************************************************************************************/

END;
```

### DEFINITIONS.PKG_S01FRM00310
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00310 IS
  TYPE LOCATION_REC IS RECORD(
    LOCATION_ID   VARCHAR2(3),
    LOCATION_DESC VARCHAR2(100));
  TYPE LOCATION_CUR IS REF CURSOR RETURN LOCATION_REC;
  --=========================================================================
  PROCEDURE LOCATION_QUERY_REFCUR(LOCATION_DATA   IN OUT LOCATION_CUR,
                                  P_LOCATION_ID   IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                  P_LOCATION_DESC IN DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  --=========================================================================================
  TYPE ORDER_LOC_RECEPT_REC IS RECORD(
    LOCATION_ID         VARCHAR2(3),
    ORDER_LOCATION_DESC VARCHAR2(100),
    ORDER_LOCATION_ID   VARCHAR2(3),
    RECEPTION_NAME      VARCHAR2(100),
    RECEPTION_ID        NUMBER(10),
    ACTIVE              CHAR(1),
    REMARKS             VARCHAR2(4000));
  TYPE ORDER_LOC_RECEPT_CUR IS REF CURSOR RETURN ORDER_LOC_RECEPT_REC;
  TYPE ORDER_LOC_RECEPT_TAB IS TABLE OF ORDER_LOC_RECEPT_REC INDEX BY BINARY_INTEGER;
  --=========================================================================
  PROCEDURE ORDER_LOC_RECEPT_QUERY_REFCUR(RECEPT_DATA           IN OUT ORDER_LOC_RECEPT_CUR,
                                          P_LOCATION_ID         IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                          P_ORDER_LOCATION_DESC IN DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
                                          P_RECEPTION_NAME      IN DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_NAME%TYPE,
                                          P_ORDER_LOCATION_ID   IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                                          P_ACTIVE              IN CHAR);
  --=============================================================================
  PROCEDURE ORDER_LOC_RECEPT_LOCK(R            IN OUT ORDER_LOC_RECEPT_TAB,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE ORDER_LOC_RECEPT_UPDATE(T IN ORDER_LOC_RECEPT_TAB);
  --=================================================================
  PROCEDURE ORDER_LOC_RECEPT_INSERT(R            IN ORDER_LOC_RECEPT_TAB,
                                    P_ALERT_TEXT OUT VARCHAR2,
                                    P_STOP       OUT CHAR);
  --====================================================================
  PROCEDURE ORDER_LOC_RECEPT_DELETE(T            IN ORDER_LOC_RECEPT_TAB,
                                    P_STOP       OUT CHAR,
                                    P_ALERT_TEXT OUT VARCHAR2);
  --===================SEQUENCE SETUP========================================
  TYPE SEQUENCE_SETUP_REC IS RECORD(
    SEQ_ID                NUMBER(10),
    LOCATION_ID           VARCHAR2(3),
    ORDER_LOCATION_ID     VARCHAR2(3),
    SEQ_DESCRIPTION       VARCHAR2(100),
    FROM_SEQ              DEFINITIONS.SEQUENCE_SETUP.FROM_SEQ%TYPE,
    TO_SEQ                DEFINITIONS.SEQUENCE_SETUP.TO_SEQ%TYPE,
    DURATION              DATE,
    REMARKS               VARCHAR2(2000),
    PREFIX                VARCHAR2(3),
    RESET_TIME            NUMBER(5),
    RECEPTION_ID          NUMBER(10),
    ORDERED_BY            NUMBER(2),
    IS_DUPLICATE          CHAR(1),
    IS_SOUND              CHAR(1),
    TOKEN_STATUS          DEFINITIONS.SEQUENCE_SETUP.TOKEN_STATUS%TYPE,
    IS_ANY                CHAR(1),
    AUTO_GET              CHAR(1),
    GET_LOCATION_TERMINAL CHAR(1),
    AUTO_PRINT            CHAR(1),
    SERVICE_REMARKS       CHAR(1),
    SMS_REQUIRED          CHAR(1),
    display_time_token    CHAR(1),
    IS_PHARMACY           CHAR(1),
    IS_TOKEN_TIME_EXCEED  CHAR(1),
    TOKEN_TIME_EXCEED     DEFINITIONS.SEQUENCE_SETUP.TOKEN_TIME_EXCEED%TYPE);
  TYPE SEQUENCE_SETUP_CUR IS REF CURSOR RETURN SEQUENCE_SETUP_REC;
  TYPE SEQUENCE_SETUP_TAB IS TABLE OF SEQUENCE_SETUP_REC INDEX BY BINARY_INTEGER;
  --=========================================================================
  PROCEDURE SEQUENCE_SETUP_QUERY_REFCUR(SEQUENCE_SETUP_DATA     IN OUT SEQUENCE_SETUP_CUR,
                                        P_SEQ_ID                IN DEFINITIONS.SEQUENCE_SETUP.SEQ_ID%TYPE,
                                        P_LOCATION_ID           IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                        P_ORDER_LOCATION_ID     IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                                        P_SEQ_DESCRIPTION       IN DEFINITIONS.SEQUENCE_SETUP.DESCRIPTION%TYPE,
                                        P_FROM_SEQ              IN DEFINITIONS.SEQUENCE_SETUP.FROM_SEQ%TYPE,
                                        P_TO_SEQ                IN DEFINITIONS.SEQUENCE_SETUP.TO_SEQ%TYPE,
                                        P_PREFIX                IN DEFINITIONS.SEQUENCE_SETUP.PREFIX%TYPE,
                                        P_RECEPTION_ID          DEFINITIONS.ORDER_LOCATION_RECEPTION.RECEPTION_ID%TYPE,
                                        P_ORDER_BY              DEFINITIONS.SEQUENCE_SETUP.ORDERED_BY%TYPE,
                                        P_IS_DUPLICATE          DEFINITIONS.SEQUENCE_SETUP.IS_DUPLICATE%TYPE,
                                        P_IS_SOUND              DEFINITIONS.SEQUENCE_SETUP.IS_SOUND%TYPE,
                                        P_IS_ANY                DEFINITIONS.SEQUENCE_SETUP.IS_ANY%TYPE,
                                        P_AUTO_GET              DEFINITIONS.SEQUENCE_SETUP.AUTO_GET%TYPE,
                                        P_GET_LOCATION_TERMINAL DEFINITIONS.SEQUENCE_SETUP.GET_LOCATION_TERMINAL%TYPE);
  --=========================================================================
  PROCEDURE SEQUENCE_SETUP_LOCK(R            IN OUT SEQUENCE_SETUP_TAB,
                                P_STOP       OUT CHAR,
                                P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE SEQUENCE_SETUP_UPDATE(T            IN SEQUENCE_SETUP_TAB,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE SEQUENCE_SETUP_INSERT(R            IN SEQUENCE_SETUP_TAB,
                                  P_ALERT_TEXT OUT VARCHAR2,
                                  P_STOP       OUT CHAR);
  --====================================================================
  PROCEDURE SEQUENCE_SETUP_DELETE(T            IN SEQUENCE_SETUP_TAB,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR2);
  --===================SEQUENCE TOKEN TYPE ========================================
  TYPE SEQUENCE_TOKEN_TYPE_REC IS RECORD(
    SEQ_ID                 NUMBER(10),
    TOKEN_TYPE_ID          NUMBER(16),
    TOKEN_TYPE_DESCRIPTION VARCHAR2(50),
    DEPARTMENT             VARCHAR2(100),
    ACTIVE                 CHAR(1),
    LOCATION_ID            VARCHAR2(3),
    RECEPTION_ID           NUMBER(10),
    ORDERED_BY             NUMBER(2));
  TYPE SEQUENCE_TOKEN_TYPE_CUR IS REF CURSOR RETURN SEQUENCE_TOKEN_TYPE_REC;
  TYPE SEQUENCE_TOKEN_TYPE_TAB IS TABLE OF SEQUENCE_TOKEN_TYPE_REC INDEX BY BINARY_INTEGER;
  --=========================================================================
  PROCEDURE SEQ_TOKEN_TYPE_QUERY_REFCUR(SEQ_TOKEN_TYPE_DATA      IN OUT SEQUENCE_TOKEN_TYPE_CUR,
                                        P_SEQ_ID                 IN DEFINITIONS.SEQUENCE_SETUP.SEQ_ID%TYPE,
                                        P_TOKEN_TYPE_DESCRIPTION IN DEFINITIONS.TOKEN_TYPE.TOKEN_TYPE_DESCRIPTION%TYPE,
                                        P_DEPARTMENT             IN VARCHAR2,
                                        P_RECEPTION_ID           IN NUMBER,
                                        P_LOCATION_ID            IN VARCHAR2);
  --=========================================================================
  PROCEDURE SEQ_TOKEN_TYPE_LOCK(R            IN OUT SEQUENCE_TOKEN_TYPE_TAB,
                                P_STOP       OUT CHAR,
                                P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE SEQ_TOKEN_TYPE_UPDATE(T IN SEQUENCE_TOKEN_TYPE_TAB);
  --=================================================================
  PROCEDURE SEQ_TOKEN_TYPE_INSERT(R            IN SEQUENCE_TOKEN_TYPE_TAB,
                                  P_ALERT_TEXT OUT VARCHAR2,
                                  P_STOP       OUT CHAR);
  --====================================================================
  PROCEDURE SEQ_TOKEN_TYPE_DELETE(T            IN SEQUENCE_TOKEN_TYPE_TAB,
                                  P_STOP       OUT CHAR,
                                  P_ALERT_TEXT OUT VARCHAR2);
  --===================TOKEN TYPE TERMINALS========================================
  TYPE TOKEN_TYPE_TERMINAL_REC IS RECORD(
    TERMINAL_NAME         VARCHAR2(30),
    IS_TOKEN              CHAR(1),
    IS_QUEUE              CHAR(1),
    LOCATION_ID           VARCHAR2(3),
    RECEPTION_ID          NUMBER(10),
    SEQ_ID                NUMBER(10),
    GET_TERMINAL_LOCATION CHAR(1));
  TYPE TOKEN_TYPE_TERMINAL_CUR IS REF CURSOR RETURN TOKEN_TYPE_TERMINAL_REC;
  TYPE TOKEN_TYPE_TERMINAL_TAB IS TABLE OF TOKEN_TYPE_TERMINAL_REC INDEX BY BINARY_INTEGER;
  --=======================================================================
  PROCEDURE TOK_TYPE_TERM_QUERY_REFCUR(TOKEN_TYPE_TERMINAL_DATA IN OUT TOKEN_TYPE_TERMINAL_CUR,
                                       P_SEQ_ID                 IN NUMBER,
                                       P_LOCATION_ID            IN VARCHAR2,
                                       P_TERMINAL_NAME          IN VARCHAR2,
                                       P_RECEPTION_ID           IN NUMBER,
                                       P_IS_TOKEN               IN CHAR,
                                       P_IS_QUEUE               IN CHAR,
                                       GET_TERMINAL_LOCATION    IN CHAR);
  --==========================================================================
  --=========================================================================
  PROCEDURE TOKEN_TYPE_TERMINAL_LOCK(R            IN OUT TOKEN_TYPE_TERMINAL_TAB,
                                     P_STOP       OUT CHAR,
                                     P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE TOKEN_TYPE_TERMINAL_UPDATE(T IN TOKEN_TYPE_TERMINAL_TAB);
  --=================================================================
  PROCEDURE TOKEN_TYPE_TERMINAL_INSERT(R            IN TOKEN_TYPE_TERMINAL_TAB,
                                       P_ALERT_TEXT OUT VARCHAR2,
                                       P_STOP       OUT CHAR);
  --====================================================================
  PROCEDURE TOKEN_TYPE_TERMINAL_DELETE(T            IN TOKEN_TYPE_TERMINAL_TAB,
                                       P_STOP       OUT CHAR,
                                       P_ALERT_TEXT OUT VARCHAR2);

  /********TOKEN SEQ SMS SETUP **************************************/

  --=========================================================================================
  TYPE TOKEN_LOC_RECEPT_REC IS RECORD(

    SEQ_ID            DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SEQ_ID%TYPE,
    RECEPTION_ID      DEFINITIONS.TOKEN_SEQ_SMS_SETUP.RECEPTION_ID%TYPE,
    LOCATION_ID       DEFINITIONS.TOKEN_SEQ_SMS_SETUP.LOCATION_ID%TYPE,
    ORDER_LOCATION_ID DEFINITIONS.TOKEN_SEQ_SMS_SETUP.ORDER_LOCATION_ID%TYPE,
    SMS_ALERT_ID      DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SMS_ALERT_ID%TYPE,
    SMS_ALERT_DESC    HIS.SMS_ALERT_SETUP.DESCRIPTION%TYPE,
    TOKEN_EVENT       DEFINITIONS.TOKEN_SEQ_SMS_SETUP.TOKEN_EVENT%TYPE,
    SMS_SEND_BEFORE   DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SMS_SEND_BEFORE%TYPE,
    SMS_PROMPT        DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SMS_PROMPT%TYPE,
    ACTIVE            DEFINITIONS.TOKEN_SEQ_SMS_SETUP.TOKEN_EVENT%TYPE);
  TYPE TOKEN_LOC_RECEPT_CUR IS REF CURSOR RETURN TOKEN_LOC_RECEPT_REC;
  TYPE TOKEN_LOC_RECEPT_TAB IS TABLE OF TOKEN_LOC_RECEPT_REC INDEX BY BINARY_INTEGER;
  --=========================================================================
  PROCEDURE P_TOKEN_SMS_QUERY_REFCUR(RECEPT_DATA         IN OUT TOKEN_LOC_RECEPT_CUR,
                                     P_SEQ_ID            IN DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SEQ_ID%TYPE,
                                     P_RECEPTION_ID      IN DEFINITIONS.TOKEN_SEQ_SMS_SETUP.LOCATION_ID%TYPE,
                                     P_LOCATION_ID       IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                     P_ORDER_LOCATION_ID IN DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
                                     p_SMS_ALERT_ID      IN DEFINITIONS.TOKEN_SEQ_SMS_SETUP.SMS_ALERT_ID%TYPE);
  --=============================================================================
  PROCEDURE P_TOKEN_SMS_LOCK(R            IN OUT TOKEN_LOC_RECEPT_TAB,
                             P_STOP       OUT CHAR,
                             P_ALERT_TEXT OUT VARCHAR2);
  --=================================================================
  PROCEDURE P_TOKEN_SMS_UPDATE(T IN TOKEN_LOC_RECEPT_TAB);
  --=================================================================
  PROCEDURE P_TOKEN_SMS_INSERT(R            IN TOKEN_LOC_RECEPT_TAB,
                               P_ALERT_TEXT OUT VARCHAR2,
                               P_STOP       OUT CHAR);
  --====================================================================
  PROCEDURE P_TOKEN_SMS_DELETE(T            IN TOKEN_LOC_RECEPT_TAB,
                               P_STOP       OUT CHAR,
                               P_ALERT_TEXT OUT VARCHAR2);

END PKG_S01FRM00310;
```

### DEFINITIONS.PKG_S01FRM00311
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00311 IS

  /*
  -- Author  : NM
  -- Created : 09/13/2013 5:58:02 PM
  -- Purpose : Move code to backend
  
  
     REVISIONS:
          VER        DATE         AUTHOR                  DESCRIPTION
          ---------  ----------   ---------------         -----------------------------------
          1.0        Sep-13-2013   NM                     1. PACKAGE Created .
          1.1        Oct-03-2022   Shahid Anwar           1. Create function GET_QUERY_ICDMAPPING
         
  
  ***********************************************************************************************************/

  TYPE REC_ICDMAP IS RECORD(
    SERIAL_NO    DEFINITIONS.ICD_MAPPING.SERIAL_NO%TYPE,
    OLD_ICDNO    DEFINITIONS.ICD_MAPPING.OLD_ICDNO%TYPE,
    OLD_ICD_DESC DEFINITIONS.ICD.LONG_DESC%TYPE,
    OLD_VERSION  DEFINITIONS.ICD_MAPPING.OLD_VERSION%TYPE,
    NEW_ICDNO    DEFINITIONS.ICD_MAPPING.NEW_ICDNO%TYPE,
    NEW_ICD_DESC DEFINITIONS.ICD.LONG_DESC%TYPE,
    NEW_VERSION  DEFINITIONS.ICD_MAPPING.NEW_VERSION%TYPE,
    ICD_FLAG     DEFINITIONS.ICD_MAPPING.ICD_FLAG%TYPE,
    ICD_TYPE     DEFINITIONS.ICD_MAPPING.ICD_TYPE%TYPE
    --,DESCRIPTION      DEFINITIONS.ICD.LONG_DESC%TYPE
    );

  TYPE REF_ICDMAP IS REF CURSOR RETURN REC_ICDMAP;
  TYPE TAB_ICDMAP IS TABLE OF REC_ICDMAP INDEX BY BINARY_INTEGER;

  TYPE TAB_ICD_MAP IS TABLE OF REC_ICDMAP;

  ---- Procedure to Query Data
  PROCEDURE QUERY_ICDMAPPING(P_RESULT    IN OUT REF_ICDMAP,
                             P_OLD_ICDNO IN DEFINITIONS.ICD_MAPPING.OLD_ICDNO%TYPE,
                             P_NEW_ICDNO IN DEFINITIONS.ICD_MAPPING.NEW_ICDNO%TYPE,
                             P_ICD_TYPE  IN DEFINITIONS.ICD_MAPPING.ICD_TYPE%TYPE);

  ---- Procedure for Updation
  PROCEDURE UPDATE_ICDMAPPING(P_RESULT     IN OUT TAB_ICDMAP,
                              P_ALERT_TEXT OUT VARCHAR2);

  --- Procedure for Insertion
  PROCEDURE INSERT_ICDMAPPING(P_RESULT     IN OUT TAB_ICDMAP,
                              P_ALERT_TEXT OUT VARCHAR2);

  ---- Procedure for Locking
  PROCEDURE LOCK_ICDMAPPING(P_RESULT     IN OUT TAB_ICDMAP,
                            P_ALERT_TEXT OUT VARCHAR2);

  ---- Procedure to Delete Data
  PROCEDURE DELETE_ICDMAPPING(P_RESULT     IN OUT TAB_ICDMAP,
                              P_ALERT_TEXT OUT VARCHAR2);

  FUNCTION GET_QUERY_ICDMAPPING(P_OLD_ICDNO IN DEFINITIONS.ICD_MAPPING.OLD_ICDNO%TYPE,
                                P_NEW_ICDNO IN DEFINITIONS.ICD_MAPPING.NEW_ICDNO%TYPE,
                                P_ICD_TYPE  IN DEFINITIONS.ICD_MAPPING.ICD_TYPE%TYPE)
    RETURN TAB_ICD_MAP
    PIPELINED;

END PKG_S01FRM00311;
```

### DEFINITIONS.PKG_S01FRM00321
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00321 AS
  /***********************************************************************************************
    OBJECTIVE := This form will be used to update CPT Categories
         
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
         1.0        26-Dec-2013  Usman Afzal(5784)      1. Created this Package.
  ************************************************************************************************/
  -- Record Type --
  TYPE CPT_CATEGORY_REC IS RECORD(
    DEPARTMENT_ID        DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT_NAME      DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT_ID          DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT                  DEFINITIONS.CPT.DESCRIPTION%TYPE,
    PRICE                DEFINITIONS.CPT.PRICE%TYPE,
    CLINIC_SPECIALITY_ID DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE,
    CLINIC_SPECIALITY    DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
    CPT_CATEGORY_ID      DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    CPT_CATEGORY         DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE,
    CATEGORY_PRICE       DEFINITIONS.CPT_CATEGORY.PRICE%TYPE);
  -- Associative Array --  
  TYPE CPT_CATEGORY_TAB IS TABLE OF CPT_CATEGORY_REC INDEX BY PLS_INTEGER;
  -- Ref Cursor --
  TYPE CPT_CATEGORY_REF IS REF CURSOR RETURN CPT_CATEGORY_REC;

  -----------------------------------------------
  -- This Procedure will query the CPT Records --
  -----------------------------------------------
  PROCEDURE QUERY_CPT_CATEGORY(P_RESULT          IN OUT CPT_CATEGORY_REF,
                               P_DEPARTMENT_ID   IN DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
                               P_CPT_ID          IN DEFINITIONS.CPT.CPT_ID%TYPE,
                               P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE);

  -----------------------------------------------
  -- This Procedure will update the CPT Category --
  -----------------------------------------------
  PROCEDURE UPDATE_CPT_CATEGORY(P_BLOCK_DATA IN OUT CPT_CATEGORY_TAB,
                                P_TERMINAL   IN DEFINITIONS.TERMINALS.TERMINAL%TYPE,
                                P_USER_MRNO  IN VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  -----------------------------------------------
  -- This Procedure will Lock the CPT Category --
  -----------------------------------------------
  PROCEDURE LOCK_CPT_CATEGORY(P_BLOCK_DATA IN OUT CPT_CATEGORY_TAB,
                              P_ALERT_TEXT OUT VARCHAR2);
END PKG_S01FRM00321;
```

### DEFINITIONS.PKG_S01FRM00322
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00322 AS
  /***********************************************************************************************
    OBJECTIVE := This form will be used to revise CPT Category Price and its Admin Costing
                 and keep history of the revision.
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date         Author                  Description
         ---------  ----------   ---------------         -----------------------------------
         1.0        30-Dec-2013  Usman Afzal(5784)      1. Created this Package.
  ************************************************************************************************/

  ---------------------
  -- 1. CPT Category --
  ---------------------
  -- Record Type --
  TYPE CPT_CATEGORY_REC IS RECORD(
    CPT_CATEGORY_ID      DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    DESCRIPTION          DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE,
    CLINIC_SPECIALITY_ID DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE,
    CLINIC_SPECIALITY    DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE);
  -- Ref Cursor --
  TYPE CPT_CATEGORY_REC_REF IS REF CURSOR RETURN CPT_CATEGORY_REC;

  ------------------------------------------------
  -- This Procedure will query the CPT Category --
  ------------------------------------------------
  PROCEDURE QUERY_CPT_CATEGORY(P_RESULT               IN OUT CPT_CATEGORY_REC_REF,
                               P_CPT_CATEGORY_ID      IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                               P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE);

  -----------------------------------
  -- 2. CPT Category Price History --
  -----------------------------------
  -- Record Type --
  TYPE CAT_PRICE_HISTORY_REC IS RECORD(
    CPT_CATEGORY_ID DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    SR_NO           DEFINITIONS.CPT_CAT_PRICE_HISTORY.SR_NO%TYPE,
    NEW_PRICE       DEFINITIONS.CPT_CAT_PRICE_HISTORY.NEW_PRICE%TYPE,
    OLD_PRICE       DEFINITIONS.CPT_CAT_PRICE_HISTORY.OLD_PRICE%TYPE,
    CHANGE_DATE     DATE,
    EFFECTIVE_DATE  DATE);
  -- Ref Cursor --
  TYPE CAT_PRICE_HISTORY_REF IS REF CURSOR RETURN CAT_PRICE_HISTORY_REC;
  -- Associative Array --
  TYPE CAT_PRICE_HISTORY_TAB IS TABLE OF CAT_PRICE_HISTORY_REC INDEX BY PLS_INTEGER;

  --------------------------------------------------------------
  -- This Procedure will query the CPT Category Price History --
  --------------------------------------------------------------
  PROCEDURE QUERY_CAT_PRICE_HISTORY(P_RESULT          IN OUT CAT_PRICE_HISTORY_REF,
                                    P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE);

  ---------------------------------------------------------------
  -- This Procedure will Insert the CPT Category Price History --
  ---------------------------------------------------------------
  PROCEDURE INSERT_CAT_PRICE_HISTORY(P_BLOCK_DATA      IN OUT CAT_PRICE_HISTORY_TAB,
                                     P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                                     P_TERMINAL        IN DEFINITIONS.TERMINALS.TERMINAL%TYPE,
                                     P_USER_MRNO       IN VARCHAR2,
                                     P_ALERT_TEXT      OUT VARCHAR2);

  ---------------------------------------------------------------
  -- This Procedure will Update the CPT Category Price History --
  ---------------------------------------------------------------
  PROCEDURE UPDATE_CAT_PRICE_HISTORY(P_BLOCK_DATA IN OUT CAT_PRICE_HISTORY_TAB,
                                     P_TERMINAL   IN DEFINITIONS.TERMINALS.TERMINAL%TYPE,
                                     P_USER_MRNO  IN VARCHAR2,
                                     P_ALERT_TEXT OUT VARCHAR2);

  ---------------------------------------------------------------
  -- This Procedure will Delete the CPT Category Price History --
  ---------------------------------------------------------------
  PROCEDURE DELETE_CAT_PRICE_HISTORY(P_BLOCK_DATA IN OUT CAT_PRICE_HISTORY_TAB,
                                     P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------
  -- This Procedure will Lock the CPT Category Price History --
  -------------------------------------------------------------
  PROCEDURE LOCK_CAT_PRICE_HISTORY(P_BLOCK_DATA IN OUT CAT_PRICE_HISTORY_TAB,
                                   P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------
  -- 3. CPT Category Costing History --
  -------------------------------------
  -- Record Type --
  TYPE CAT_COSTING_HISTORY_REC IS RECORD(
    CPT_CATEGORY_ID  DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    SR_NO            DEFINITIONS.CPT_CAT_COSTING_HISTORY.SR_NO%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.ADMIN_COSTING.ADMIN_COSTING_ID%TYPE,
    ADMIN_COSTING    DEFINITIONS.ADMIN_COSTING.DESCRIPTION%TYPE,
    NEW_PRICE        DEFINITIONS.CPT_CAT_COSTING_HISTORY.NEW_PRICE%TYPE,
    OLD_PRICE        DEFINITIONS.CPT_CAT_COSTING_HISTORY.OLD_PRICE%TYPE,
    NEW_QTY          DEFINITIONS.CPT_CAT_COSTING_HISTORY.NEW_QTY%TYPE,
    NEW_UNIT_ID      DEFINITIONS.CPT_CAT_COSTING_HISTORY.NEW_UNIT_ID%TYPE,
    OLD_QTY          DEFINITIONS.CPT_CAT_COSTING_HISTORY.OLD_QTY%TYPE,
    OLD_UNIT_ID      DEFINITIONS.CPT_CAT_COSTING_HISTORY.OLD_UNIT_ID%TYPE);
  -- Ref Cursor --
  TYPE CAT_COSTING_HISTORY_REF IS REF CURSOR RETURN CAT_COSTING_HISTORY_REC;
  -- Associative Array --
  TYPE CAT_COSTING_HISTORY_TAB IS TABLE OF CAT_COSTING_HISTORY_REC INDEX BY PLS_INTEGER;

  ----------------------------------------------------------------
  -- This Procedure will query the CPT Category Costing History --
  ----------------------------------------------------------------
  PROCEDURE QUERY_CAT_COSTING_HISTORY(P_RESULT          IN OUT CAT_COSTING_HISTORY_REF,
                                      P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CAT_PRICE_HISTORY.CPT_CATEGORY_ID%TYPE,
                                      P_SR_NO           IN DEFINITIONS.CPT_CAT_PRICE_HISTORY.SR_NO%TYPE);

  -----------------------------------------------------------------
  -- This Procedure will Insert the CPT Category Costing History --
  -----------------------------------------------------------------
  PROCEDURE INSERT_CAT_COSTING_HISTORY(P_BLOCK_DATA IN OUT CAT_COSTING_HISTORY_TAB,
                                       P_TERMINAL   IN DEFINITIONS.TERMINALS.TERMINAL%TYPE,
                                       P_USER_MRNO  IN VARCHAR2,
                                       P_ALERT_TEXT OUT VARCHAR2);

  -----------------------------------------------------------------
  -- This Procedure will Update the CPT Category Costing History --
  -----------------------------------------------------------------
  PROCEDURE UPDATE_CAT_COSTING_HISTORY(P_BLOCK_DATA IN OUT CAT_COSTING_HISTORY_TAB,
                                       P_TERMINAL   IN DEFINITIONS.TERMINALS.TERMINAL%TYPE,
                                       P_USER_MRNO  IN VARCHAR2,
                                       P_ALERT_TEXT OUT VARCHAR2);

  -----------------------------------------------------------------
  -- This Procedure will Delete the CPT Category Costing History --
  -----------------------------------------------------------------
  PROCEDURE DELETE_CAT_COSTING_HISTORY(P_BLOCK_DATA IN OUT CAT_COSTING_HISTORY_TAB,
                                       P_ALERT_TEXT OUT VARCHAR2);

  ---------------------------------------------------------------
  -- This Procedure will Lock the CPT Category Costing History --
  ---------------------------------------------------------------
  PROCEDURE LOCK_CAT_COSTING_HISTORY(P_BLOCK_DATA IN OUT CAT_COSTING_HISTORY_TAB,
                                     P_ALERT_TEXT OUT VARCHAR2);
END PKG_S01FRM00322;
```

### DEFINITIONS.PKG_S01FRM00323
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00323 AS

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 27-01-2014
  -- Scope     : S01FRM00323
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_RPT_HF_SETUP_QRY(P_RPT_HF_SETUP_ID IN DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.RPT_HF_SETUP.LOCATION_ID%TYPE,
                               P_DATA            IN OUT DEFINITIONS.PKG_RPT_HF_SETUP.RPT_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 27-01-2014
  -- Scope     : S01FRM00323
  -- Purpose   : This procedure will be used for inserting data of 
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_RPT_HF_SETUP_INS(P_RPT_HF_SETUP_ID OUT DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                               P_DATA            IN OUT DEFINITIONS.PKG_RPT_HF_SETUP.RPT_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 27-01-2014
  -- Scope     : S01FRM00323
  -- Purpose   : This procedure will be used for validating data of 
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_RPT_HF_SETUP_LCK(P_DATA       IN OUT DEFINITIONS.PKG_RPT_HF_SETUP.RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 27-01-2014
  -- Scope     : S01FRM00323
  -- Purpose   : This procedure will be used for updating data of 
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_RPT_HF_SETUP_UPD(P_DATA       IN OUT DEFINITIONS.PKG_RPT_HF_SETUP.RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 27-01-2014
  -- Scope     : S01FRM00323
  -- Purpose   : This procedure will be used for deleting data of 
  --             DEFINITIONS.RPT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_RPT_HF_SETUP_DEL(P_DATA       IN OUT DEFINITIONS.PKG_RPT_HF_SETUP.RPT_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

END PKG_S01FRM00323;
```

### DEFINITIONS.PKG_S01FRM00324
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00324 AS

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_ORG_HF_SETUP_QRY(P_ORGANIZATION_ID IN DEFINITIONS.ORG_HF_SETUP.ORGANIZATION_ID%TYPE,
                               P_FROM_DATE       IN DEFINITIONS.ORG_HF_SETUP.FROM_DATE%TYPE,
                               P_DATA            IN OUT DEFINITIONS.PKG_ORG_HF_SETUP.ORG_HF_SETUP_TAB,
                               P_STOP            OUT VARCHAR2,
                               P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_ORG_HF_SETUP_INS(P_DATA       IN OUT DEFINITIONS.PKG_ORG_HF_SETUP.ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_ORG_HF_SETUP_LCK(P_DATA       IN OUT DEFINITIONS.PKG_ORG_HF_SETUP.ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_ORG_HF_SETUP_UPD(P_DATA       IN OUT DEFINITIONS.PKG_ORG_HF_SETUP.ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             DEFINITIONS.ORG_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_ORG_HF_SETUP_DEL(P_DATA       IN OUT DEFINITIONS.PKG_ORG_HF_SETUP.ORG_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_HF_SETUP_QRY(P_LOCATION_ID IN DEFINITIONS.LOC_HF_SETUP.LOCATION_ID%TYPE,
                               P_FROM_DATE   IN DEFINITIONS.LOC_HF_SETUP.FROM_DATE%TYPE,
                               P_DATA        IN OUT DEFINITIONS.PKG_LOC_HF_SETUP.LOC_HF_SETUP_TAB,
                               P_STOP        OUT VARCHAR2,
                               P_ALERT_TEXT  OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_HF_SETUP_INS(P_DATA       IN OUT DEFINITIONS.PKG_LOC_HF_SETUP.LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for validating data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_HF_SETUP_LCK(P_DATA       IN OUT DEFINITIONS.PKG_LOC_HF_SETUP.LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_HF_SETUP_UPD(P_DATA       IN OUT DEFINITIONS.PKG_LOC_HF_SETUP.LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             DEFINITIONS.LOC_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_HF_SETUP_DEL(P_DATA       IN OUT DEFINITIONS.PKG_LOC_HF_SETUP.LOC_HF_SETUP_TAB,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             SECURITY.LOC_WISE_SCHEMA_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_SCHEMA_HF_SETUP_QRY(P_ORGANIZATION_ID IN SECURITY.LOC_WISE_SCHEMA_HF_SETUP.ORGANIZATION_ID%TYPE,
                                           P_LOCATION_ID     IN SECURITY.LOC_WISE_SCHEMA_HF_SETUP.LOCATION_ID%TYPE,
                                           P_SCHEMA_ID       IN SECURITY.LOC_WISE_SCHEMA_HF_SETUP.SCHEMA_ID%TYPE,
                                           P_FROM_DATE       IN SECURITY.LOC_WISE_SCHEMA_HF_SETUP.FROM_DATE%TYPE,
                                           P_DATA            IN OUT SECURITY.PKG_LOC_WISE_SCHEMA_HF_SETUP.LOC_WISE_SCHEMA_HF_SETUP_TAB,
                                           P_STOP            OUT VARCHAR2,
                                           P_ALERT_TEXT      OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             SECURITY.LOC_WISE_SCHEMA_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_SCHEMA_HF_SETUP_INS(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_SCHEMA_HF_SETUP.LOC_WISE_SCHEMA_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for locking data of
  --             SECURITY.LOC_WISE_SCHEMA_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_SCHEMA_HF_SETUP_LCK(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_SCHEMA_HF_SETUP.LOC_WISE_SCHEMA_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             SECURITY.LOC_WISE_SCHEMA_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_SCHEMA_HF_SETUP_UPD(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_SCHEMA_HF_SETUP.LOC_WISE_SCHEMA_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             SECURITY.LOC_WISE_SCHEMA_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_SCHEMA_HF_SETUP_DEL(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_SCHEMA_HF_SETUP.LOC_WISE_SCHEMA_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for querying data of
  --             SECURITY.LOC_WISE_OBJECT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_OBJECT_HF_SETUP_QRY(P_SCHEMA_ID      IN SECURITY.LOC_WISE_OBJECT_HF_SETUP.SCHEMA_ID%TYPE,
                                           P_OBJECT_TYPE_ID IN SECURITY.LOC_WISE_OBJECT_HF_SETUP.OBJECT_TYPE_ID%TYPE,
                                           P_OBJECT_ID      IN SECURITY.LOC_WISE_OBJECT_HF_SETUP.OBJECT_ID%TYPE,
                                           P_LOCATION_ID    IN SECURITY.LOC_WISE_OBJECT_HF_SETUP.LOCATION_ID%TYPE,
                                           P_FROM_DATE      IN SECURITY.LOC_WISE_OBJECT_HF_SETUP.FROM_DATE%TYPE,
                                           P_DATA           IN OUT SECURITY.PKG_LOC_WISE_OBJECT_HF_SETUP.LOC_WISE_OBJECT_HF_SETUP_TAB,
                                           P_STOP           OUT VARCHAR2,
                                           P_ALERT_TEXT     OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for inserting data of
  --             SECURITY.LOC_WISE_OBJECT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_OBJECT_HF_SETUP_INS(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_OBJECT_HF_SETUP.LOC_WISE_OBJECT_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for locking data of
  --             SECURITY.LOC_WISE_OBJECT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_OBJECT_HF_SETUP_LCK(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_OBJECT_HF_SETUP.LOC_WISE_OBJECT_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for updating data of
  --             SECURITY.LOC_WISE_OBJECT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_OBJECT_HF_SETUP_UPD(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_OBJECT_HF_SETUP.LOC_WISE_OBJECT_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 29-01-2014
  -- Scope     :
  -- Purpose   : This procedure will be used for deleting data of
  --             SECURITY.LOC_WISE_OBJECT_HF_SETUP.
  /******************************************************************************/
  PROCEDURE P_LOC_WISE_OBJECT_HF_SETUP_DEL(P_DATA       IN OUT SECURITY.PKG_LOC_WISE_OBJECT_HF_SETUP.LOC_WISE_OBJECT_HF_SETUP_TAB,
                                           P_STOP       OUT VARCHAR2,
                                           P_ALERT_TEXT OUT VARCHAR2);

  -------------------------------------------------------------------------------
  /******************************************************************************/
  -- Author    : NADIA OMER (3501)
  -- Created on: 08-02-2014
  -- Scope     : REPORT_HEADER_FOOTER_SETUP (S01REP00116)
  -- Purpose   : This procedure will be used for populating header/footer of
  --             Sample Report(S01REP00116)
  /******************************************************************************/
  PROCEDURE FETCH_RPT_HF(P_RPT_HF_SETUP_ID IN DEFINITIONS.RPT_HF_SETUP.RPT_HF_SETUP_ID%TYPE,
                         P_ORIENTATION     IN VARCHAR2,
                         P_ALLERT_TXT      OUT VARCHAR2,
                         P_STOP_YN         OUT CHAR,
                         P_FIELDS          OUT HIS.PKG_REPORT_HF.RPT_HF_CUR);
  -------------------------------------------------

  FUNCTION F_GET_PARENT_LOCATION_ID(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN DEFINITIONS.LOCATION.PARENT_LOCATION_ID%TYPE;

END PKG_S01FRM00324;
```

### DEFINITIONS.PKG_S01FRM00327
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00327 AS

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for querying data of
  --             REGISTRATION.CLINIC
  /******************************************************************************/

  PROCEDURE P_CLINICS_QRY(P_CLINIC_ID  IN REGISTRATION.CLINIC.CLINIC_ID%TYPE,
                          P_NAME       IN REGISTRATION.CLINIC.NAME%TYPE,
                          P_DATA       IN OUT definitions.pkg_clinic_booking_specs.CLINICS_TBL,
                          P_STOP       OUT VARCHAR2,
                          P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC
  -- Purpose   : This procedure will be used for locking data of
  --             REGISTRATION.CLINIC.
  /******************************************************************************/

  PROCEDURE P_CLINICS_LCK(P_DATA       IN OUT definitions.pkg_clinic_booking_specs.CLINICS_TBL,
                          P_STOP       OUT VARCHAR2,
                          P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC_BOOKING_SPECS
  -- Purpose   : This procedure will be used for querying data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_QY(P_CLINIC_ID       IN REGISTRATION.CLINIC_BOOKING_SPECS.CLINIC_ID%TYPE,
                               P_DAY_ID          IN REGISTRATION.CLINIC_BOOKING_SPECS.DAY_ID%TYPE,
                               P_DAY             IN DEFINITIONS.DAY.DESCRIPTION%TYPE,
                               P_SPECS_MORNING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_MORNING%TYPE,
                               P_SPECS_AFTERNOON IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_AFTERNOON%TYPE,
                               P_SPECS_EVENING   IN REGISTRATION.CLINIC_BOOKING_SPECS.SPECS_EVENING%TYPE,
                               
                               P_ACTIVE     IN REGISTRATION.CLINIC_BOOKING_SPECS.ACTIVE%TYPE,
                               P_DATA       IN OUT definitions.pkg_clinic_booking_specs.BOOKING_SPECS_TLL,
                               P_STOP       OUT VARCHAR2,
                               P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC_BOOKING_SPECS
  -- Purpose   : This procedure will be used for inserting data in
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_INS(P_CLINIC_ID  OUT REGISTRATION.CLINIC_BOOKING_SPECS.CLINIC_ID%TYPE,
                                P_DAY_ID     OUT REGISTRATION.CLINIC_BOOKING_SPECS.DAY_ID%TYPE,
                                P_DATA       IN OUT definitions.pkg_clinic_booking_specs.BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC_BOOKING_SPECS
  -- Purpose   : This procedure will be used for locking data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_LCK(P_DATA       IN OUT definitions.pkg_clinic_booking_specs.BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC_BOOKING_SPECS
  -- Purpose   : This procedure will be used for updating data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_UPD(P_DATA       IN OUT definitions.pkg_clinic_booking_specs.BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

  /******************************************************************************/
  -- Author    : Asma Hashmi (4806)
  -- Created on: 13-MARCH-2014
  -- Scope     : CLINIC_BOOKING_SPECS
  -- Purpose   : This procedure will be used for deleting data of
  --             REGISTRATION.CLINIC_BOOKING_SPECS.
  /******************************************************************************/

  PROCEDURE P_BOOKING_SPECS_DEL(P_DATA       IN OUT definitions.pkg_clinic_booking_specs.BOOKING_SPECS_TLL,
                                P_STOP       OUT VARCHAR2,
                                P_ALERT_TEXT OUT VARCHAR2);

/******************************************************************************/

END PKG_S01FRM00327;
```

### DEFINITIONS.PKG_S01FRM00336
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00336 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This package was created for Registration Fee pending for Invoice
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-DEC-2014   Muhammad Younas        1. Created this Package.
  ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -------------------------
  -- Record Type for CPT --
  -------------------------
  TYPE CPT_REC IS RECORD(
    CPT_ID      DEFINITIONS.CPT.CPT_ID%TYPE,
    DESCRIPTION DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  TYPE CPT_TAB IS TABLE OF CPT_REC;

  -----------------------------------
  -- This Procedure will query CPT --
  -----------------------------------
  PROCEDURE QUERY_CPT(P_RESULT     IN OUT CPT_REF,
                      P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_ALERT_TEXT OUT VARCHAR2);

  FUNCTION GET_QUERY_CPT(P_CPT_ID IN VARCHAR2 DEFAULT NULL) RETURN CPT_TAB
    PIPELINED;
  --------------------------------------------------------------
  -- Record type for Definitions.CPT_DEPARTMENT_SECTION Table --
  --------------------------------------------------------------
  TYPE CDS_REC IS RECORD(
    CPT_ID           DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_ID%TYPE,
    DEPARTMENT_ID    DEFINITIONS.CPT_DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
    DEPARTMENT       DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    SECTION_ID       DEFINITIONS.CPT_DEPARTMENT_SECTION.SECTION_ID%TYPE,
    SECTION          DEFINITIONS.DEPARTMENT_SECTION.DESCRIPTION%TYPE,
    SHARE_PERCENTAGE DEFINITIONS.CPT_DEPARTMENT_SECTION.SHARE_PERCENTAGE%TYPE,
    DEFAULT_SECTION  DEFINITIONS.CPT_DEPARTMENT_SECTION.DEFAULT_SECTION%TYPE,
    CPT_HEAD         DEFINITIONS.CPT_DEPARTMENT_SECTION.CPT_HEAD%TYPE,
    ACTIVE           DEFINITIONS.CPT_DEPARTMENT_SECTION.ACTIVE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CDS_REF IS REF CURSOR RETURN CDS_REC;

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CDS_TAB IS TABLE OF CDS_REC INDEX BY BINARY_INTEGER;
  ----------------------------------------------------------------
  -- This Procedure will query the CPT DEPARTMENT SECTION Table --
  ----------------------------------------------------------------
  PROCEDURE QUERY_CPT_DEPT_SECCTION(P_RESULT     IN OUT CDS_REF,
                                    P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                    P_ALERT_TEXT OUT VARCHAR2);
  -----------------------------------                            
  -- Insert CPT DEPARTMENT SECTION --
  -----------------------------------
  PROCEDURE INSERT_CPT_DEPT_SECCTION(P_BLOCK_DATA IN OUT CDS_TAB,
                                     P_ALERT_TEXT OUT VARCHAR);
  -----------------------------------
  -- Update CPT DEPARTMENT SECTION --
  -----------------------------------
  PROCEDURE UPDATE_CPT_DEPT_SECCTION(P_BLOCK_DATA IN OUT CDS_TAB,
                                     P_ALERT_TEXT OUT VARCHAR);
  -----------------------------------
  -- Delete CPT DEPARTMENT SECTION --
  -----------------------------------
  PROCEDURE DELETE_CPT_DEPT_SECCTION(P_BLOCK_DATA IN OUT CDS_TAB,
                                     P_ALERT_TEXT OUT VARCHAR);
  ---------------------------------
  -- Lock CPT DEPARTMENT SECTION --
  ---------------------------------
  PROCEDURE LOCK_CPT_DEPT_SECCTION(P_BLOCK_DATA IN OUT CDS_TAB,
                                   P_ALERT_TEXT OUT VARCHAR);
  ------------------------------------                                 
  -- Check Department Active or not --
  ------------------------------------
  PROCEDURE P_CHECK_DEPT_SEC_ACTIVE(P_CPT_ID        IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                    P_DEPARTMENT_ID IN DEFINITIONS.DEPARTMENT_SECTION.DEPARTMENT_ID%TYPE,
                                    P_SECTION_ID    IN DEFINITIONS.DEPARTMENT_SECTION.SECTION_ID%TYPE,
                                    P_ALERT_TEXT    OUT VARCHAR2,
                                    P_STOP          OUT CHAR);

END PKG_S01FRM00336;
```

### DEFINITIONS.PKG_S01FRM00337
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00337 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This package was created for Registration Fee pending for Invoice
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-DEC-2014   Muhammad Younas        1. Created this Package.
  ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -------------------------
  -- Record Type for CPT --
  -------------------------
  TYPE CPT_REC IS RECORD(
    CPT_ID      DEFINITIONS.CPT.CPT_ID%TYPE,
    DESCRIPTION DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  -----------------------------------
  -- This Procedure will query CPT --
  -----------------------------------
  PROCEDURE QUERY_CPT(P_RESULT     IN OUT CPT_REF,
                      P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_ALERT_TEXT OUT VARCHAR2);
  ----------------------------------------------------
  -- Record type for Definitions.CPT_SPECIMEN Table --
  ----------------------------------------------------
  TYPE CS_REC IS RECORD(
    CPT_ID           DEFINITIONS.CPT_SPECIMEN.CPT_ID%TYPE,
    SPECIMEN_ID      DEFINITIONS.CPT_SPECIMEN.SPECIMEN_ID%TYPE,
    SPECIMEN         DEFINITIONS.SPECIMEN.DESCRIPTION%TYPE,
    DEFAULTS         DEFINITIONS.CPT_SPECIMEN.DEFAULTS%TYPE,
    ACTIVE           DEFINITIONS.CPT_SPECIMEN.ACTIVE%TYPE,
    REMARKS_REQUIRED DEFINITIONS.CPT_SPECIMEN.REMARKS_REQUIRED%TYPE,
    LABEL_CLASS      DEFINITIONS.CPT_SPECIMEN.LABEL_CLASS%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CS_REF IS REF CURSOR RETURN CS_REC;

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CS_TAB IS TABLE OF CS_REC INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This Procedure will query the CPT SPECIMEN Table --
  ------------------------------------------------------
  PROCEDURE QUERY_CPT_SPECIMEN(P_RESULT     IN OUT CS_REF,
                               P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                               P_ALERT_TEXT OUT VARCHAR2);
  -------------------------                            
  -- Insert CPT SPECIMEN --
  -------------------------
  PROCEDURE INSERT_CPT_SPECIMEN(P_BLOCK_DATA IN OUT CS_TAB,
                                P_ALERT_TEXT OUT VARCHAR);
  -------------------------
  -- Update CPT SPECIMEN --
  -------------------------
  PROCEDURE UPDATE_CPT_SPECIMEN(P_BLOCK_DATA IN OUT CS_TAB,
                                P_ALERT_TEXT OUT VARCHAR);
  -------------------------
  -- Delete CPT SPECIMEN --
  -------------------------
  PROCEDURE DELETE_CPT_SPECIMEN(P_BLOCK_DATA IN OUT CS_TAB,
                                P_ALERT_TEXT OUT VARCHAR);
  -----------------------
  -- Lock CPT SPECIMEN --
  -----------------------
  PROCEDURE LOCK_CPT_SPECIMEN(P_BLOCK_DATA IN OUT CS_TAB,
                              P_ALERT_TEXT OUT VARCHAR);
  ----------------------------------                                 
  -- Check Specimen Active or not --
  ----------------------------------
  PROCEDURE P_CHECK_SPECIMEN_ACTIVE(P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                    P_ALERT_TEXT OUT VARCHAR2,
                                    P_STOP       OUT CHAR);

END PKG_S01FRM00337;
```

### DEFINITIONS.PKG_S01FRM00338
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00338 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This package was created for Registration Fee pending for Invoice
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        17-DEC-2014   Muhammad Younas        1. Created this Package.
  ************************************************************************************************/

  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  -------------------------
  -- Record Type for CPT --
  -------------------------
  TYPE CPT_REC IS RECORD(
    CPT_ID      DEFINITIONS.CPT.CPT_ID%TYPE,
    DESCRIPTION DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  -----------------------------------
  -- This Procedure will query CPT --
  -----------------------------------
  PROCEDURE QUERY_CPT(P_RESULT     IN OUT CPT_REF,
                      P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_ALERT_TEXT OUT VARCHAR2);
  ----------------------------------------------------
  -- Record type for Definitions.CPT_COSTING Table --
  ----------------------------------------------------
  TYPE CC_REC IS RECORD(
    CPT_ID           DEFINITIONS.CPT_COSTING.CPT_ID%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.CPT_COSTING.ADMIN_COSTING_ID%TYPE,
    ADMIN_COSTING    DEFINITIONS.ADMIN_COSTING.DESCRIPTION%TYPE,
    COST             DEFINITIONS.CPT_COSTING.COST%TYPE,
    PERCENTAGE       DEFINITIONS.CPT_COSTING.PERCENTAGE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE CC_REF IS REF CURSOR RETURN CC_REC;

  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CC_TAB IS TABLE OF CC_REC INDEX BY BINARY_INTEGER;
  ------------------------------------------------------
  -- This Procedure will query the CPT COSTING Table --
  ------------------------------------------------------
  PROCEDURE QUERY_CPT_COSTING(P_RESULT     IN OUT CC_REF,
                              P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                              P_ALERT_TEXT OUT VARCHAR2);
  ------------------------                            
  -- Insert CPT COSTING --
  ------------------------
  PROCEDURE INSERT_CPT_COSTING(P_BLOCK_DATA IN OUT CC_TAB,
                               P_ALERT_TEXT OUT VARCHAR);
  ------------------------
  -- Update CPT COSTING --
  ------------------------
  PROCEDURE UPDATE_CPT_COSTING(P_BLOCK_DATA IN OUT CC_TAB,
                               P_ALERT_TEXT OUT VARCHAR);
  ------------------------
  -- Delete CPT COSTING --
  ------------------------
  PROCEDURE DELETE_CPT_COSTING(P_BLOCK_DATA IN OUT CC_TAB,
                               P_ALERT_TEXT OUT VARCHAR);
  ----------------------
  -- Lock CPT COSTING --
  ----------------------
  PROCEDURE LOCK_CPT_COSTING(P_BLOCK_DATA IN OUT CC_TAB,
                             P_ALERT_TEXT OUT VARCHAR);
  -----------------------------------------------                          
  -- Function to get Admin Costing Description --
  -----------------------------------------------                          
  FUNCTION GET_ADMIN_COSTING(P_ADMIN_COSTING_ID IN DEFINITIONS.ADMIN_COSTING.ADMIN_COSTING_ID%TYPE)
    RETURN DEFINITIONS.ADMIN_COSTING.DESCRIPTION%TYPE;
  --------------------------------------------                                 
  -- Update CPT Selling Price in CPT table  --
  --------------------------------------------
  PROCEDURE P_UPDATE_CPT_SELLING_PRICE(P_CPT_ID     IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                       P_ALERT_TEXT OUT VARCHAR2,
                                       P_STOP       OUT CHAR);

END PKG_S01FRM00338;
```

### DEFINITIONS.PKG_S01FRM00354
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00354 AS

  /***********************************************************************************************
          OBJECTIVE := This package was created for Clinical Service Price Procedures/Functions
               1. All Independent Procedures/Functions will be written this package
               2. We will call the functions from this Package
          ----------------------------------------------------------------------------------
          REVISIONS:
          Ver        Date          Author                 Description
          ---------  -----------   -------------------    -----------------------------------
          1.0        25-MAR-2016   MUHAMMAD ALI KHUBAIB   1. Created this Package.
          1.1        06-APR-2017   FARHAN AKRAM           1. Added IBP column.
          1.2        12-APR-2018   MUHAMMAD USMAN TAHIR   1. PROCEDURE PATIENT TYPE
          1.3        31-OCT-2019   MUHAMMAD USMAN TAHIR   1. ADD PROCEDURE FOR GET CPT PRICE FROM MULTI PROCEDURES
  *************************************************************************************************/

  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE LOCATION_REC IS RECORD(
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE LOCATION_CUR IS REF CURSOR RETURN LOCATION_REC;

  ------------------------------------------------------------------------- 
  -- Purpose   : This Procedure is used to Query Data for Location Block --
  -------------------------------------------------------------------------
  PROCEDURE QUERY_LOCATION(P_RESULT          IN OUT LOCATION_CUR,
                           P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_LOCATION_DESC   IN DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
                           P_ORGANIZATION_ID IN DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
                           P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                           P_ALERT_TEXT      OUT VARCHAR2,
                           P_STOP            OUT VARCHAR2);

  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_PATIENT_TYPE IS RECORD(
    PATIENT_TYPE_ID DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    DESCRIPTION     DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
    LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_PATIENT_TYPE IS REF CURSOR RETURN REC_PATIENT_TYPE;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_PATIENT_TYPE IS TABLE OF REC_PATIENT_TYPE INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.PATIENT_TYPE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_PATIENT_TYPE(P_DATA            IN OUT REF_PATIENT_TYPE,
                               P_PATIENT_TYPE_ID IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                               P_DESCRIPTION     IN DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE);

  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    OPD_PRICE          DEFINITIONS.CPT.PRICE%TYPE,
    IPD_PRICE          DEFINITIONS.CPT.PRICE%TYPE,
    EAR_PRICE          DEFINITIONS.CPT.PRICE%TYPE,
    ALLOWED            VARCHAR2(5)
    /*IBP_PRICE       DEFINITIONS.CPT.PRICE%TYPE*/);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_CPT IS REF CURSOR RETURN REC_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_CPT IS TABLE OF REC_CPT INDEX BY BINARY_INTEGER;

  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.CLINICAL_SERVICE_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_CS_PRICE(P_DATA                 IN OUT REF_CPT,
                           P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                           P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                           P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                           P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                           P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                           P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);

  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.CLINICAL_SERVICE_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_CS_PRICE(P_BLOCK_DATA IN OUT TAB_CPT);

  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.CLINICAL_SERVICE_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_CS_PRICE(P_BLOCK_DATA IN OUT TAB_CPT);

  ------------------------------------------------
  -- RECORD GROUP FOR CLNIC CPT PRICE --
  ------------------------------------------------
  TYPE CLINIC_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    CLINIC_NAME        REGISTRATION.CLINIC.NAME%TYPE,
    CLINIC_ID          REGISTRATION.CLINIC.CLINIC_ID%TYPE,
    PRICE              DEFINITIONS.CLINIC_CPT_PRICE.PRICE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_CLINIC_CPT IS REF CURSOR RETURN CLINIC_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_CLINIC_CPT IS TABLE OF CLINIC_CPT INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.CLINIC_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_CLINIC_PRICE(P_DATA                 IN OUT REF_CLINIC_CPT,
                               P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                               P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                               P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                               P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                               P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                               P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.CLINIC_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_CLINIC_PRICE(P_BLOCK_DATA IN OUT TAB_CLINIC_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.CLINIC_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_CLINIC_PRICE(P_BLOCK_DATA IN OUT TAB_CLINIC_CPT);
  ------------------------------------------------
  -- RECORD GROUP FOR ORDER LOCATION CPT PRICE --
  ------------------------------------------------
  TYPE ORDER_LOCATION_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    ORDER_DESC         DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
    ORDER_LOCATION_ID  DEFINITIONS.ORDER_LOCATION.ORDER_LOCATION_ID%TYPE,
    PRICE              DEFINITIONS.CLINIC_CPT_PRICE.PRICE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_ORDER_CPT IS REF CURSOR RETURN ORDER_LOCATION_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_ORDER_CPT IS TABLE OF ORDER_LOCATION_CPT INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.ORDER_LOCATION_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_ORDER_PRICE(P_DATA                 IN OUT REF_ORDER_CPT,
                              P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                              P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                              P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                              P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                              P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                              P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                              P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.ORDER_LOCATION_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_ORDER_PRICE(P_BLOCK_DATA IN OUT TAB_ORDER_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.ORDER_LOCATION_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_ORDER_PRICE(P_BLOCK_DATA IN OUT TAB_ORDER_CPT);
  ----------------------------------------
  -- RECORD GROUP FOR DOCTOR CPT PRICE --
  ----------------------------------------
  TYPE DOCTOR_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    DOCTOR_NAME        DEFINITIONS.DOCTOR.NAME%TYPE,
    DOCTOR_ID          REGISTRATION.CLINIC.CLINIC_ID%TYPE,
    PRICE              DEFINITIONS.CLINIC_CPT_PRICE.PRICE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_DOCTOR_CPT IS REF CURSOR RETURN DOCTOR_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_DOCTOR_CPT IS TABLE OF DOCTOR_CPT INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.DOCTOR_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_DOCTOR_PRICE(P_DATA                 IN OUT REF_DOCTOR_CPT,
                               P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                               P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                               P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                               P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                               P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                               P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.DOCTOR_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_DOCTOR_PRICE(P_BLOCK_DATA IN OUT TAB_DOCTOR_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.DOCTOR_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_DOCTOR_PRICE(P_BLOCK_DATA IN OUT TAB_DOCTOR_CPT);
  ------------------------------------------------
  -- RECORD GROUP FOR PATIENT TYPE CPT PRICE --
  ------------------------------------------------
  TYPE PATIENT_TYPE_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    PATIENT_TYPE_ID    DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    PRICE              DEFINITIONS.CLINIC_CPT_PRICE.PRICE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_PATIENT_CPT IS REF CURSOR RETURN PATIENT_TYPE_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_PATIENT_CPT IS TABLE OF PATIENT_TYPE_CPT INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.CLINIC_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_PATIENT_PRICE(P_DATA                 IN OUT REF_PATIENT_CPT,
                                P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                                P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                                P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                                P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                                P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.CLINIC_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_PATIENT_PRICE(P_BLOCK_DATA IN OUT TAB_PATIENT_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.CLINIC_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_PATIENT_PRICE(P_BLOCK_DATA IN OUT TAB_PATIENT_CPT);
  --------------------------------------
  -- RECORD GROUP FOR ROOM CPT PRICE --
  --------------------------------------
  TYPE ROOM_TYPE_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    CATEGORY_ID        DEFINITIONS.ROOM_CATEGORY_CPT_PRICE.CATEGORY_ID%TYPE,
    CATEGORY_DESC      DEFINITIONS.ROOM_CATEGORY.DESCRIPTION%TYPE,
    PRICE              DEFINITIONS.CLINIC_CPT_PRICE.PRICE%TYPE);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_ROOM_CPT IS REF CURSOR RETURN ROOM_TYPE_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_ROOM_CPT IS TABLE OF ROOM_TYPE_CPT INDEX BY BINARY_INTEGER;
  ---------------------------------------------------
  -- This Function will return the ROOM description --
  ---------------------------------------------------
  FUNCTION GET_ROOM_DESC(P_CATEGORY_ID IN DEFINITIONS.ROOM_CATEGORY.CATEGORY_ID%TYPE)
    RETURN DEFINITIONS.ROOM_CATEGORY.DESCRIPTION%TYPE;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.ROOM_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_ROOM_PRICE(P_DATA                 IN OUT REF_ROOM_CPT,
                             P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                             P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                             P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                             P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                             P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
                             P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.ROOM_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_ROOM_PRICE(P_BLOCK_DATA IN OUT TAB_ROOM_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.ROOM_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_ROOM_PRICE(P_BLOCK_DATA IN OUT TAB_ROOM_CPT);
  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_LOCATION_CPT IS RECORD(
    LOCATION_ID        DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    DISP_CPT           DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_ORIGINAL_PRICE DEFINITIONS.CPT.PRICE%TYPE,
    PRICE              DEFINITIONS.CPT.PRICE%TYPE,
    ALLOWED            VARCHAR2(5),
		PRICE_ACTIVE       DEFINITIONS.LOCATION_WISE_CPT.PRICE_ACTIVE%TYPE
		);

  ----------------
  -- Ref Cursor --
  ----------------
  TYPE REF_LOCATION_CPT IS REF CURSOR RETURN REC_LOCATION_CPT;

  ----------------
  -- PL-SQL TABLE --
  ----------------
  TYPE TAB_LOCATION_CPT IS TABLE OF REC_LOCATION_CPT INDEX BY BINARY_INTEGER;
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for querying data of 
  --             DEFINITIONS.LOCATION_CPT_PRICE. 
  -------------------------------------------------------------------------
  PROCEDURE QUERY_LOCATION_PRICE(P_DATA                 IN OUT REF_LOCATION_CPT,
                                 P_LOCATION_ID          IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                                 P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                 P_DEPARTMENT_NATURE_ID IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                                 P_SECTION_NATURE_ID    IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                                 P_DESCRIPTION          IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
                                 P_PATIENT_TYPE_ID      IN DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
																 P_PRICE_ACTIVE           IN DEFINITIONS.LOCATION_WISE_CPT.PRICE_ACTIVE%TYPE,
                                 P_OBJECT_CODE          IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);
  ------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for locking data of
  --             DEFINITIONS.LOCATION_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE LOCK_LOCATION_PRICE(P_BLOCK_DATA IN OUT TAB_LOCATION_CPT);
  -------------------------------------------------------------------------
  -- Purpose   : This procedure will be used for updating data of
  --             DEFINITIONS.LOCATION_CPT_PRICE.
  -------------------------------------------------------------------------
  PROCEDURE UPDATE_LOCATION_PRICE(P_BLOCK_DATA IN OUT TAB_LOCATION_CPT);

END PKG_S01FRM00354;
```

### DEFINITIONS.PKG_S01FRM00355
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00355 AS

  /************************************************************************************************
         OBJECTIVE := This package was created for PACKAGE TYPE
         ----------------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date            Author                   Description
         ---------  -----------     -------------------      ----------------------------
         1.0        1024-JUN-2016   M. ALI KHUBAIB           1. Created this Package.
  ************************************************************************************************/
  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_PKG_TYPE IS RECORD(
    PACKAGE_TYPE_ID DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
    DESCRIPTION     DEFINITIONS.PACKAGE_TYPE.DESCRIPTION%TYPE,
    SHORT_DESC      DEFINITIONS.PACKAGE_TYPE.SHORT_DESC%TYPE,
    ACTIVE          DEFINITIONS.PACKAGE_TYPE.ACTIVE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PKG_TYPE IS REF CURSOR RETURN REC_PKG_TYPE;

  -----------------
  -- PLSQL TABLE --
  -----------------
  TYPE TAB_PKG_TYPE IS TABLE OF REC_PKG_TYPE INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PACKGE_TYPE --
  -------------------------------------------
  PROCEDURE QUERY_PKG_TYPE(P_RESULT          IN OUT REF_PKG_TYPE,
                           P_PACKAGE_TYPE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                           P_DESCRIPTION     IN DEFINITIONS.PACKAGE_TYPE.DESCRIPTION%TYPE,
                           P_SHORT_DESC      IN DEFINITIONS.PACKAGE_TYPE.SHORT_DESC%TYPE,
                           P_ACTIVE          IN DEFINITIONS.PACKAGE_TYPE.ACTIVE%TYPE);

  --------------------------------------------
  -- This procedure will insert PACKGE_TYPE --
  --------------------------------------------
  PROCEDURE INSERT_PKG_TYPE(P_RESULT IN OUT TAB_PKG_TYPE);

  --------------------------------------------
  -- This procedure will update PACKGE_TYPE --
  --------------------------------------------
  PROCEDURE UPDATE_PKG_TYPE(P_RESULT IN OUT TAB_PKG_TYPE);

  --------------------------------------------
  -- This procedure will delete PACKGE_TYPE --
  --------------------------------------------
  PROCEDURE DELETE_PKG_TYPE(P_RESULT IN OUT TAB_PKG_TYPE);

  ------------------------------------------
  -- This procedure will lock PACKGE_TYPE --
  ------------------------------------------
  PROCEDURE LOCK_PKG_TYPE(P_RESULT IN OUT TAB_PKG_TYPE);

  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_LOC_PKG_TYPE IS RECORD(
    PACKAGE_TYPE_ID DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
    LOCATION_ID     DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    DESCRIPTION     DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    ACTIVE          DEFINITIONS.LOCATION_PACKAGE_TYPE.ACTIVE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_LOC_PKG_TYPE IS REF CURSOR RETURN REC_LOC_PKG_TYPE;

  -----------------
  -- PLSQL TABLE --
  -----------------
  TYPE TAB_LOC_PKG_TYPE IS TABLE OF REC_LOC_PKG_TYPE INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query PACKGE_TYPE --
  -------------------------------------------
  PROCEDURE QUERY_LOC_PKG_TYPE(P_RESULT          IN OUT REF_LOC_PKG_TYPE,
                               P_PACKAGE_TYPE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                               P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_DESCRIPTION     IN DEFINITIONS.LOCATION.DESCRIPTION%TYPE);

  --------------------------------------------
  -- This procedure will update PACKGE_TYPE --
  --------------------------------------------
  PROCEDURE UPDATE_LOC_PKG_TYPE(P_RESULT IN OUT TAB_LOC_PKG_TYPE);

  ------------------------------------------
  -- This procedure will lock PACKGE_TYPE --
  ------------------------------------------
  PROCEDURE LOCK_LOC_PKG_TYPE(P_RESULT IN OUT TAB_LOC_PKG_TYPE);

END;
```

### DEFINITIONS.PKG_S01FRM00357
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00357 IS
  --PRAGMA SERIALLY_REUSABLE;

  -- Author  : Hafiz Abrar Ahmed
  -- Created : 11-May-2016 1:18:15 pm
  -- Purpose : This Package contains Procedures and Functions related with FILES SERVERS
  --         : FILES_SERVERS.FMX
  -- =======================================================================  

  TYPE REC_FILES_TYPES IS RECORD(
    FILE_TYPE_ID           DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
    FILE_DESC              DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
    COMMENTS               DEFINITIONS.FILES_TYPES.COMMENTS%TYPE,
    STORAGE_TYPE           DEFINITIONS.FILES_TYPES.STORAGE_TYPE%TYPE,
    FILE_SIZE              DEFINITIONS.FILES_TYPES.FILE_SIZE%TYPE,
    DELETE_SOURCE_FILE     DEFINITIONS.FILES_TYPES.DELETE_SOURCE_FILE%TYPE,
    ACTIVE                 DEFINITIONS.FILES_TYPES.ACTIVE%TYPE,
    OPEN_WITH_ID           DEFINITIONS.FILES_VIEWERS.VIEWER_ID%TYPE,
    OPEN_WITH_DESC         DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
    DEFAULT_TEMPORARY_PATH DEFINITIONS.FILES_TYPES.DEFAULT_TEMPORARY_PATH%TYPE);

  TYPE TAB_FILES_TYPES IS TABLE OF REC_FILES_TYPES INDEX BY PLS_INTEGER;
  TYPE TAB_FILES_TYPES_PF IS TABLE OF REC_FILES_TYPES;
  -- ********************************************************************** --

  TYPE REC_FILES_TYPES_DET IS RECORD(
    TYPE_ID            DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
    FILE_TYPE_ID       DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
    FILE_DESC          DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
    TYPE_DESC          DEFINITIONS.FILES_TYPES_DET.TYPE_DESC%TYPE,
    COMMENTS           DEFINITIONS.FILES_TYPES_DET.COMMENTS%TYPE,
    DELETE_SOURCE_FILE DEFINITIONS.FILES_TYPES_DET.DELETE_SOURCE_FILE%TYPE,
    ACTIVE             DEFINITIONS.FILES_TYPES_DET.ACTIVE%TYPE,
    OPEN_WITH_ID       DEFINITIONS.FILES_VIEWERS.VIEWER_ID%TYPE,
    OPEN_WITH_DESC     DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
    FILE_TYPE_DESC     DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_DESCRIPTION%TYPE,
    STORAGE_TYPE       DEFINITIONS.FILES_TYPES_DET.STORAGE_TYPE%TYPE,
    FILE_SIZE          DEFINITIONS.FILES_TYPES_DET.FILE_SIZE%TYPE,
    COUNT_PAGES        DEFINITIONS.FILES_TYPES_DET.COUNT_PAGES%TYPE);

  TYPE TAB_FILES_TYPES_DET IS TABLE OF REC_FILES_TYPES_DET INDEX BY PLS_INTEGER;
  TYPE TAB_FILES_TYPES_DET_PF IS TABLE OF REC_FILES_TYPES_DET;
  -- ********************************************************************** --

  PROCEDURE P_FILES_TYPES_QUERY(P_RECORDSET              IN OUT TAB_FILES_TYPES,
                                P_FILE_TYPE_ID           IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                                P_FILE_DESC              IN DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
                                P_COMMENTS               IN DEFINITIONS.FILES_TYPES.COMMENTS%TYPE,
                                P_STORAGE_TYPE           IN DEFINITIONS.FILES_TYPES.STORAGE_TYPE%TYPE,
                                P_FILE_SIZE              IN DEFINITIONS.FILES_TYPES.FILE_SIZE%TYPE,
                                P_DELETE_SOURCE_FILE     IN DEFINITIONS.FILES_TYPES.DELETE_SOURCE_FILE%TYPE,
                                P_ACTIVE                 IN DEFINITIONS.FILES_TYPES.ACTIVE%TYPE,
                                P_DEFAULT_TEMPORARY_PATH IN DEFINITIONS.FILES_TYPES.DEFAULT_TEMPORARY_PATH%TYPE,
                                P_OPEN_WITH_DESC         IN DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
                                P_LOC_ID                 IN VARCHAR2,
                                P_CALLING_OBJECT         IN VARCHAR2,
                                P_CALLING_USER           IN VARCHAR2,
                                P_CALLING_EVENT          IN VARCHAR2,
                                P_STOP                   OUT CHAR,
                                P_ERROR                  OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_INSERT(P_RECORDSET      IN OUT TAB_FILES_TYPES,
                                 P_LOC_ID         IN VARCHAR2,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2,
                                 P_STOP           OUT CHAR,
                                 P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_LOCK(P_RECORDSET      IN OUT TAB_FILES_TYPES,
                               P_LOC_ID         IN VARCHAR2,
                               P_CALLING_OBJECT IN VARCHAR2,
                               P_CALLING_USER   IN VARCHAR2,
                               P_CALLING_EVENT  IN VARCHAR2,
                               P_STOP           OUT CHAR,
                               P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_UPDATE(P_RECORDSET      IN OUT TAB_FILES_TYPES,
                                 P_LOC_ID         IN VARCHAR2,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2,
                                 P_STOP           OUT CHAR,
                                 P_ERROR          OUT VARCHAR2);
  -- =======================================================================                                   

  PROCEDURE P_FILES_TYPES_DELETE(P_RECORDSET      IN OUT TAB_FILES_TYPES,
                                 P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                                 P_LOC_ID         IN VARCHAR2,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2,
                                 P_STOP           OUT CHAR,
                                 P_ERROR          OUT VARCHAR2);
  -- =======================================================================                                   

  PROCEDURE P_FILES_TYPES_DET_QUERY(P_RECORDSET          IN OUT TAB_FILES_TYPES_DET,
                                    P_TYPE_ID            IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                                    P_FILE_TYPE_ID       IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                                    P_FILE_DESC          IN DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
                                    P_TYPE_DESC          IN DEFINITIONS.FILES_TYPES_DET.TYPE_DESC%TYPE,
                                    P_COMMENTS           IN DEFINITIONS.FILES_TYPES_DET.COMMENTS%TYPE,
                                    P_DELETE_SOURCE_FILE IN DEFINITIONS.FILES_TYPES_DET.DELETE_SOURCE_FILE%TYPE,
                                    P_ACTIVE             IN DEFINITIONS.FILES_TYPES_DET.ACTIVE%TYPE,
                                    P_STORAGE_TYPE       IN DEFINITIONS.FILES_TYPES_DET.STORAGE_TYPE%TYPE,
                                    P_FILE_SIZE          IN DEFINITIONS.FILES_TYPES_DET.FILE_SIZE%TYPE,
                                    P_COUNT_PAGES        IN DEFINITIONS.FILES_TYPES_DET.COUNT_PAGES%TYPE,
                                    P_OPEN_WITH_DESC     IN DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
                                    P_FILE_TYPE_DESC     IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_DESCRIPTION%TYPE,
                                    P_LOC_ID             IN VARCHAR2,
                                    P_CALLING_OBJECT     IN VARCHAR2,
                                    P_CALLING_USER       IN VARCHAR2,
                                    P_CALLING_EVENT      IN VARCHAR2,
                                    P_STOP               OUT CHAR,
                                    P_ERROR              OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_DET_INSERT(P_RECORDSET      IN OUT TAB_FILES_TYPES_DET,
                                     P_LOC_ID         IN VARCHAR2,
                                     P_CALLING_OBJECT IN VARCHAR2,
                                     P_CALLING_USER   IN VARCHAR2,
                                     P_CALLING_EVENT  IN VARCHAR2,
                                     P_STOP           OUT CHAR,
                                     P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_DET_LOCK(P_RECORDSET      IN OUT TAB_FILES_TYPES_DET,
                                   P_LOC_ID         IN VARCHAR2,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2,
                                   P_STOP           OUT CHAR,
                                   P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_TYPES_DET_UPDATE(P_RECORDSET      IN OUT TAB_FILES_TYPES_DET,
                                     P_LOC_ID         IN VARCHAR2,
                                     P_CALLING_OBJECT IN VARCHAR2,
                                     P_CALLING_USER   IN VARCHAR2,
                                     P_CALLING_EVENT  IN VARCHAR2,
                                     P_STOP           OUT CHAR,
                                     P_ERROR          OUT VARCHAR2);
  -- =======================================================================                                   

  PROCEDURE P_FILES_TYPES_DET_DELETE(P_RECORDSET      IN OUT TAB_FILES_TYPES_DET,
                                     P_TYPE_ID        IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                                     P_FILE_TYPE_ID   IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                                     P_LOC_ID         IN VARCHAR2,
                                     P_CALLING_OBJECT IN VARCHAR2,
                                     P_CALLING_USER   IN VARCHAR2,
                                     P_CALLING_EVENT  IN VARCHAR2,
                                     P_STOP           OUT CHAR,
                                     P_ERROR          OUT VARCHAR2);
  -- =======================================================================  

  FUNCTION F_FILE_TYPES_APEX_QRY(P_FILE_TYPE_ID           IN DEFINITIONS.FILES_TYPES.FILE_TYPE_ID%TYPE,
                                 P_FILE_DESC              IN DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
                                 P_COMMENTS               IN DEFINITIONS.FILES_TYPES.COMMENTS%TYPE,
                                 P_STORAGE_TYPE           IN DEFINITIONS.FILES_TYPES.STORAGE_TYPE%TYPE,
                                 P_FILE_SIZE              IN DEFINITIONS.FILES_TYPES.FILE_SIZE%TYPE,
                                 P_DELETE_SOURCE_FILE     IN DEFINITIONS.FILES_TYPES.DELETE_SOURCE_FILE%TYPE,
                                 P_ACTIVE                 IN DEFINITIONS.FILES_TYPES.ACTIVE%TYPE,
                                 P_DEFAULT_TEMPORARY_PATH IN DEFINITIONS.FILES_TYPES.DEFAULT_TEMPORARY_PATH%TYPE,
                                 P_OPEN_WITH_DESC         IN DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
                                 P_LOC_ID                 IN VARCHAR2,
                                 P_CALLING_OBJECT         IN VARCHAR2,
                                 P_CALLING_USER           IN VARCHAR2,
                                 P_CALLING_EVENT          IN VARCHAR2)
    RETURN TAB_FILES_TYPES_PF
    PIPELINED;
    
  -- =======================================================================   
  FUNCTION F_FILE_TYPES_DET_APEX_QRY(P_TYPE_ID            IN DEFINITIONS.FILES_TYPES_DET.TYPE_ID%TYPE,
                                     P_FILE_TYPE_ID       IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_ID%TYPE,
                                     P_FILE_DESC          IN DEFINITIONS.FILES_TYPES.FILE_DESC%TYPE,
                                     P_TYPE_DESC          IN DEFINITIONS.FILES_TYPES_DET.TYPE_DESC%TYPE,
                                     P_COMMENTS           IN DEFINITIONS.FILES_TYPES_DET.COMMENTS%TYPE,
                                     P_DELETE_SOURCE_FILE IN DEFINITIONS.FILES_TYPES_DET.DELETE_SOURCE_FILE%TYPE,
                                     P_ACTIVE             IN DEFINITIONS.FILES_TYPES_DET.ACTIVE%TYPE,
                                     P_STORAGE_TYPE       IN DEFINITIONS.FILES_TYPES_DET.STORAGE_TYPE%TYPE,
                                     P_FILE_SIZE          IN DEFINITIONS.FILES_TYPES_DET.FILE_SIZE%TYPE,
                                     P_COUNT_PAGES        IN DEFINITIONS.FILES_TYPES_DET.COUNT_PAGES%TYPE,
                                     P_OPEN_WITH_DESC     IN DEFINITIONS.FILES_VIEWERS.VIEWER_NAME%TYPE,
                                     P_FILE_TYPE_DESC     IN DEFINITIONS.FILES_TYPES_DET.FILE_TYPE_DESCRIPTION%TYPE,
                                     P_LOC_ID             IN VARCHAR2,
                                     P_CALLING_OBJECT     IN VARCHAR2,
                                     P_CALLING_USER       IN VARCHAR2,
                                     P_CALLING_EVENT      IN VARCHAR2)
    RETURN TAB_FILES_TYPES_DET_PF
    PIPELINED;

END PKG_S01FRM00357;
```

### DEFINITIONS.PKG_S01FRM00358
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00358 IS
  --PRAGMA SERIALLY_REUSABLE;

  -- Author  : Hafiz Abrar Ahmed
  -- Created : 11-May-2016 8:42:09 am
  -- Purpose : This Package contains Procedures and Functions related with FILES SERVERS
  --         : FILES_SERVERS.FMX
  -- =======================================================================

  TYPE REC_FILES_SERVERS IS RECORD(
    SERVER_ID        DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
    SERVER_NAME      DEFINITIONS.FILES_SERVERS.SERVER_NAME%TYPE,
    ACCESS_PATH      DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
    SERVER_TYPE_ID   DEFINITIONS.FILES_SERVERS.SERVER_TYPE_ID%TYPE,
    SERVER_TYPE_DESC DEFINITIONS.Files_Servers_Types.TYPE_DESC%TYPE,
    LOCATION_ID      DEFINITIONS.FILES_SERVERS.LOCATION_ID%TYPE,
    LOCATION_DESC    VARCHAR2(200),
    REMARKS          DEFINITIONS.FILES_SERVERS.REMARKS%TYPE,
    OBJECT_CODE      DEFINITIONS.FILES_SERVERS.OBJECT_CODE%TYPE,
    OBJECT_NAME      VARCHAR2(200),
    CREATED_BY       VARCHAR2(100),
    ACTIVE           DEFINITIONS.FILES_SERVERS.ACTIVE%TYPE);

  TYPE TAB_FILES_SERVERS IS TABLE OF REC_FILES_SERVERS INDEX BY PLS_INTEGER;
  TYPE TAB_FILE_SERVERS_PF IS TABLE OF REC_FILES_SERVERS;
  --*******************************************************************************

  PROCEDURE P_FILES_SERVERS_QUERY(P_DATA             IN OUT TAB_FILES_SERVERS,
                                  P_LOCATION_DESC    IN DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
                                  P_SERVER_TYPE_DESC IN DEFINITIONS.FILES_SERVERS_TYPES.TYPE_DESC%TYPE,
                                  P_SERVER_ID        IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                                  P_SERVER_TYPE_ID   IN DEFINITIONS.FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                                  P_SERVER_NAME      IN DEFINITIONS.FILES_SERVERS.SERVER_NAME%TYPE,
                                  P_ACCESS_PATH      IN DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
                                  P_REMARKS          IN DEFINITIONS.FILES_SERVERS.REMARKS%TYPE,
                                  P_OBJECT_NAME      IN DEFINITIONS.OBJECTS.NAME%TYPE,
                                  P_CREATED_BY       IN REGISTRATION.PATIENT.NAME%TYPE,
                                  P_LOCATION_ID      IN DEFINITIONS.FILES_SERVERS.LOCATION_ID%TYPE,
                                  P_LOC_ID           IN VARCHAR2,
                                  P_CALLING_OBJECT   IN VARCHAR2,
                                  P_CALLING_USER     IN VARCHAR2,
                                  P_CALLING_EVENT    IN VARCHAR2,
                                  P_STOP             OUT CHAR,
                                  P_ERROR            OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_SERVERS_INSERT(P_DATA           IN OUT TAB_FILES_SERVERS,
                                   P_LOC_ID         IN VARCHAR2,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2,
                                   P_STOP           OUT CHAR,
                                   P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_SERVERS_LOCK(P_DATA           IN OUT TAB_FILES_SERVERS,
                                 P_LOC_ID         IN VARCHAR2,
                                 P_CALLING_OBJECT IN VARCHAR2,
                                 P_CALLING_USER   IN VARCHAR2,
                                 P_CALLING_EVENT  IN VARCHAR2,
                                 P_STOP           OUT CHAR,
                                 P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_SERVERS_UPDATE(P_DATA           IN OUT TAB_FILES_SERVERS,
                                   P_LOC_ID         IN VARCHAR2,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2,
                                   P_STOP           OUT CHAR,
                                   P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_FILES_SERVERS_DELETE(P_DATA           IN OUT TAB_FILES_SERVERS,
                                   P_LOC_ID         IN VARCHAR2,
                                   P_CALLING_OBJECT IN VARCHAR2,
                                   P_CALLING_USER   IN VARCHAR2,
                                   P_CALLING_EVENT  IN VARCHAR2,
                                   P_STOP           OUT CHAR,
                                   P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  TYPE REC_SYNCHRONIZE IS RECORD(
    SOURCE_ID     DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.SOURCE_ID%TYPE,
    SOURCE_PATH   DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.SOURCE_PATH%TYPE,
    SOURCE_ACTIVE DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.SOURCE_ACTIVE%TYPE,
    TARGET_ID     DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.TARGET_ID%TYPE,
    TARGET_PATH   DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.TARGET_PATH%TYPE,
    TARGET_ACTIVE DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.TARGET_ACTIVE%TYPE,
    STATUS        DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.STATUS%TYPE,
    SYNC_MODE     DEFINITIONS.V_FILES_SERVERS_SYNC_SETUP.SYNC_MODE%TYPE,
    ACCESS_MODE   VARCHAR2(30));
  TYPE TAB_SYNCHRONIZE IS TABLE OF REC_SYNCHRONIZE INDEX BY PLS_INTEGER;
  TYPE TAB_SYNCHRONIZE_PF IS TABLE OF REC_SYNCHRONIZE;
  -- =======================================================================

  PROCEDURE P_SERVER_SYNC_QUERY(P_DATA           IN OUT TAB_SYNCHRONIZE,
                                P_TARGET_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                                P_ACTIVE_ONLY    IN VARCHAR2,
                                P_ORG_ID         IN VARCHAR2,
                                P_LOC_ID         IN VARCHAR2,
                                P_CALLING_OBJECT IN VARCHAR2,
                                P_CALLING_USER   IN VARCHAR2,
                                P_CALLING_EVENT  IN VARCHAR2,
                                P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_SERVER_SYNC_INS(P_DATA           IN OUT TAB_SYNCHRONIZE,
                              P_LOC_ID         IN VARCHAR2,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2,
                              P_STOP           OUT CHAR,
                              P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_SERVER_SYNC_UPD(P_DATA           IN OUT TAB_SYNCHRONIZE,
                              P_LOC_ID         IN VARCHAR2,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2,
                              P_STOP           OUT CHAR,
                              P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_SERVER_SYNC_DEL(P_DATA           IN OUT TAB_SYNCHRONIZE,
                              P_LOC_ID         IN VARCHAR2,
                              P_CALLING_OBJECT IN VARCHAR2,
                              P_CALLING_USER   IN VARCHAR2,
                              P_CALLING_EVENT  IN VARCHAR2,
                              P_STOP           OUT CHAR,
                              P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  PROCEDURE P_SERVER_SYNC_LOCK(P_DATA           IN OUT TAB_SYNCHRONIZE,
                               P_LOC_ID         IN VARCHAR2,
                               P_CALLING_OBJECT IN VARCHAR2,
                               P_CALLING_USER   IN VARCHAR2,
                               P_CALLING_EVENT  IN VARCHAR2,
                               P_STOP           OUT CHAR,
                               P_ERROR          OUT VARCHAR2);
  -- =======================================================================

  FUNCTION F_SYNCHRONIZE(P_SOURCE_ID      IN LOB.DOCUMENTS_STORE_SERVERS.SERVER_ID%TYPE,
                         P_TARGET_ID      IN LOB.DOCUMENTS_STORE_SERVERS.SERVER_ID%TYPE,
                         P_DOCUMENT_ID    IN LOB.DOCUMENTS_STORE.DOCUMENT_ID%TYPE,
                         P_FROM_DATE      IN DATE,
                         P_TO_DATE        IN DATE,
                         P_ACTIVE_ONLY    IN VARCHAR2,
                         P_ORG_ID         IN VARCHAR2,
                         P_LOC_ID         IN VARCHAR2,
                         P_CALLING_OBJECT IN VARCHAR2,
                         P_CALLING_USER   IN VARCHAR2,
                         P_CALLING_EVENT  IN VARCHAR2,
                         P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- =======================================================================

  /*PROCEDURE P_FETCH_QUERY(P_LIST_NAME      IN VARCHAR2,
  P_QUERY          OUT VARCHAR2,
  P_CALLING_OBJECT IN VARCHAR2,
  P_LOC_ID         IN VARCHAR2,
  P_CALLING_USER   IN VARCHAR2,
  P_CALLING_EVENT  IN VARCHAR2,
  P_ERROR          OUT VARCHAR2);*/
  -- =======================================================================

  /*FUNCTION F_VALIDATE_PARAM(P_PARAM_NAME     IN VARCHAR2,
  P_PARAM_VALUE    IN OUT VARCHAR2,
  P_PARAM_DESC     IN OUT VARCHAR2,
  P_ORG_ID         IN VARCHAR2,
  P_LOC_ID         IN VARCHAR2,
  P_CALLING_OBJECT IN VARCHAR2,
  P_CALLING_USER   IN VARCHAR2,
  P_CALLING_EVENT  IN VARCHAR2,
  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;*/

  -- =======================================================================

  FUNCTION F_GET_SERVER_NAME(P_SERVER_ID IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE)
    RETURN DEFINITIONS.FILES_SERVERS.SERVER_NAME%TYPE;

  -- =======================================================================

  FUNCTION F_GET_SERVER_TYPE_DESC(P_SERVER_TYPE_ID IN DEFINITIONS.FILES_SERVERS_TYPES.SERVER_TYPE_ID%TYPE)
    RETURN DEFINITIONS.FILES_SERVERS_TYPES.TYPE_DESC%TYPE;

  -- =======================================================================

  FUNCTION F_GET_LOCATION_DESC(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN DEFINITIONS.LOCATION.DESCRIPTION%TYPE;
  -- =======================================================================

  FUNCTION F_GET_OBJECT_NAME(P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE)
    RETURN DEFINITIONS.OBJECTS.NAME%TYPE;
  -- =======================================================================
  
    FUNCTION F_FILE_SERVERS_APEX_QRY(P_LOCATION_DESC    IN DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
                                     P_SERVER_TYPE_DESC IN DEFINITIONS.FILES_SERVERS_TYPES.TYPE_DESC%TYPE,
                                     P_SERVER_ID        IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                                     P_SERVER_TYPE_ID   IN DEFINITIONS.FILES_SERVERS.SERVER_TYPE_ID%TYPE,
                                     P_SERVER_NAME      IN DEFINITIONS.FILES_SERVERS.SERVER_NAME%TYPE,
                                     P_ACCESS_PATH      IN DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
                                     P_REMARKS          IN DEFINITIONS.FILES_SERVERS.REMARKS%TYPE,
                                     P_OBJECT_NAME      IN DEFINITIONS.OBJECTS.NAME%TYPE,
                                     P_CREATED_BY       IN REGISTRATION.PATIENT.NAME%TYPE,
                                     P_LOCATION_ID      IN DEFINITIONS.FILES_SERVERS.LOCATION_ID%TYPE,
                                     P_LOC_ID           IN VARCHAR2,
                                     P_CALLING_OBJECT   IN VARCHAR2,
                                     P_CALLING_USER     IN VARCHAR2,
                                     P_CALLING_EVENT    IN VARCHAR2)
    RETURN TAB_FILE_SERVERS_PF
    PIPELINED;
    
  -- =======================================================================  
    
  FUNCTION F_SERVER_SYNC_APEX_QRY(P_TARGET_ID      IN DEFINITIONS.FILES_SERVERS.SERVER_ID%TYPE,
                                  P_ACTIVE_ONLY    IN VARCHAR2,
                                  P_ORG_ID         IN VARCHAR2,
                                  P_LOC_ID         IN VARCHAR2,
                                  P_CALLING_OBJECT IN VARCHAR2,
                                  P_CALLING_USER   IN VARCHAR2,
                                  P_CALLING_EVENT  IN VARCHAR2)
    RETURN TAB_SYNCHRONIZE_PF
    PIPELINED;

END PKG_S01FRM00358;
```

### DEFINITIONS.PKG_S01FRM00360
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00360 IS

  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Hafiz Abrar Ahmed
  -- Created : 24-Mar-2016 1:00:00 pm
  -- Purpose : This Package contains Procedures and Functions related with DEFAULT_FILES_SERVERS
  --         : DEFAULT_FILES_SERVERS.FMB

  TYPE REC_DEFAULT_FILES_SERVERS IS RECORD(
    LOCATION_ID         HIS.FILES_SERVERS_ACCESS_DET.LOCATION_ID%TYPE,
    GRANTED_LOCATION_ID HIS.FILES_SERVERS_ACCESS_DET.GRANTED_LOCATION_ID%TYPE,
    SERVER_ID           HIS.FILES_SERVERS_ACCESS_DET.SERVER_ID%TYPE,
    SERVER_NAME         DEFINITIONS.FILES_SERVERS.SERVER_NAME%TYPE,
    ACCESS_VIA          HIS.FILES_SERVERS_ACCESS_DET.ACCESS_VIA%TYPE,
    ACCESS_VIA_DESC     VARCHAR2(20),
    ACCESS_MODE         HIS.FILES_SERVERS_ACCESS_DET.ACCESS_MODE%TYPE,
    ACCESS_MODE_DESC    VARCHAR2(50),
    ALLOW               HIS.FILES_SERVERS_ACCESS_DET.ACTIVE%TYPE,
    ACTIVE              DEFINITIONS.FILES_SERVERS.ACTIVE%TYPE,
    PRIORITY            HIS.FILES_SERVERS_ACCESS_DET.PRIORITY%TYPE,
    REMARKS             HIS.FILES_SERVERS_ACCESS_DET.REMARKS%TYPE);

  TYPE TAB_DEFAULT_FILES_SERVERS IS TABLE OF REC_DEFAULT_FILES_SERVERS INDEX BY PLS_INTEGER;

  -- =======================================================================   
  /*  PROCEDURE P_DEFAULT_FILES_SERVERS_QUERY(RESULTSET             IN OUT \*REF_FILES_SERVERS_ACCESS_DET, --*\TAB_DEFAULT_FILES_SERVERS,
                                          P_LOCATION_ID         IN HIS.FILES_SERVERS_ACCESS_DET.LOCATION_ID%TYPE,
                                          P_GRANTED_LOCATION_ID IN HIS.FILES_SERVERS_ACCESS_DET.GRANTED_LOCATION_ID%TYPE,
                                          P_SHOW_ALL            IN VARCHAR2,
                                          P_LOC_ID IN VARCHAR2,
                                          P_CALLING_OBJECT      IN VARCHAR2,
                                          P_CALLING_USER        IN VARCHAR2,
                                          P_CALLING_EVENT       IN VARCHAR2,
                                          P_STOP                OUT CHAR,
                                          P_ERROR               OUT VARCHAR2,
                                          P_ORDER_BY            IN VARCHAR2);
  
  -- =======================================================================
  PROCEDURE P_DEFAULT_FILES_SERVERS_INSERT(P_DATA                IN OUT TAB_FILES_SERVERS_ACCESS_DET,
                                           P_LOC_ID IN VARCHAR2,
                                           P_CALLING_OBJECT      IN VARCHAR2,
                                           P_CALLING_USER        IN VARCHAR2,
                                           P_CALLING_EVENT       IN VARCHAR2,
                                           P_STOP                OUT CHAR,
                                           P_ERROR               OUT VARCHAR2);
  
  -- =======================================================================
  PROCEDURE P_DEFAULT_FILES_SERVERS_LOCK(P_DATA                IN OUT TAB_FILES_SERVERS_ACCESS_DET,
                                         P_LOC_ID IN VARCHAR2,
                                         P_CALLING_OBJECT      IN VARCHAR2,
                                         P_CALLING_USER        IN VARCHAR2,
                                         P_CALLING_EVENT       IN VARCHAR2,
                                         P_STOP                OUT CHAR,
                                         P_ERROR               OUT VARCHAR2);
  
  -- =======================================================================
  PROCEDURE P_DEFAULT_FILES_SERVERS_UPDATE(P_DATA                IN OUT TAB_FILES_SERVERS_ACCESS_DET,
                                           P_LOC_ID IN VARCHAR2,
                                           P_CALLING_OBJECT      IN VARCHAR2,
                                           P_CALLING_USER        IN VARCHAR2,
                                           P_CALLING_EVENT       IN VARCHAR2,
                                           P_STOP                OUT CHAR,
                                           P_ERROR               OUT VARCHAR2);
  
  -- =======================================================================                                   
  PROCEDURE P_DEFAULT_FILES_SERVERS_DELETE(P_DATA                IN OUT TAB_FILES_SERVERS_ACCESS_DET,
                                           P_LOC_ID IN VARCHAR2,
                                           P_CALLING_OBJECT      IN VARCHAR2,
                                           P_CALLING_USER        IN VARCHAR2,
                                           P_CALLING_EVENT       IN VARCHAR2,
                                           P_STOP                OUT CHAR,
                                           P_ERROR               OUT VARCHAR2); */
  -- =======================================================================  
  PROCEDURE P_FETCH_QUERY(P_LIST_NAME      IN VARCHAR2,
                          P_QUERY          OUT VARCHAR2,
                          P_CALLING_OBJECT IN VARCHAR2,
                          P_LOC_ID         IN VARCHAR2,
                          P_CALLING_USER   IN VARCHAR2,
                          P_CALLING_EVENT  IN VARCHAR2,
                          P_ERROR          OUT VARCHAR2);

  -- =======================================================================
  PROCEDURE P_GET_DISPLAY_DATA(P_SERVER_ID            IN DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_ID%TYPE,
                               P_ACCESS_PATH          OUT DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
                               P_SERVER_LOCATION_ID   OUT DEFINITIONS.FILES_SERVERS.LOCATION_ID%TYPE,
                               P_SERVER_LOCATION_DESC OUT VARCHAR2,
                               P_SERVER_ACTIVE        OUT VARCHAR2);

  -- =======================================================================

  TYPE REC_FILES_SERVERS_ACCESS IS RECORD(
    LOCATION_ID    DEFINITIONS.DEFAULT_FILES_SERVERS.LOCATION_ID%TYPE,
--    MODALITY       DEFINITIONS.DEFAULT_FILES_SERVERS.MODALITY_ID%TYPE,
    SERVER_TYPE_ID DEFINITIONS.DEFAULT_FILES_SERVERS.SERVER_TYPE_ID%TYPE,
    SERVER_PATH1   DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
    SERVER_PATH2   DEFINITIONS.FILES_SERVERS.ACCESS_PATH%TYPE,
    MODE_TYPE      VARCHAR2(30));
  TYPE TAB_FILES_SERVERS_ACCESS IS TABLE OF REC_FILES_SERVERS_ACCESS;

  -- =======================================================================
  FUNCTION F_DEFAULT_SERVERS(P_LOCATION_ID    IN VARCHAR2 DEFAULT NULL,
                             P_SERVER_TYPE_ID IN VARCHAR2 DEFAULT NULL)
    RETURN TAB_FILES_SERVERS_ACCESS
    PIPELINED;

END PKG_S01FRM00360;
```

### DEFINITIONS.PKG_S01FRM00364
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00364 AS

	/***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for SERVICE TYPE
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        14-JUN-2016   M. ALI KHUBAIB            1. Created this Package.
  ************************************************************************************************/
	------------------
	-- Record Group --
	------------------
	TYPE REC_SERVICE_TYPE IS RECORD(
		SERVICE_TYPE_ID           DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		DESCRIPTION               DEFINITIONS.SERVICE_TYPE.DESCRIPTION%TYPE,
		SERVICE_CATEGORY_GROUP_ID DEFINITIONS.SERVICE_CATEGORY_GROUP.SERVICE_CATEGORY_GROUP_ID%TYPE,
		SERVICE_CATEGORY_ID       DEFINITIONS.DEF_SERVICE_CATEGORY.SERVICE_CATEGORY_ID%TYPE,
		SERVICE_CATEGORY          DEFINITIONS.DEF_SERVICE_CATEGORY.DESCRIPTION%TYPE,
		ACTIVE                    DEFINITIONS.SERVICE_TYPE.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SERVICE_TYPE IS REF CURSOR RETURN REC_SERVICE_TYPE;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SERVICE_TYPE IS TABLE OF REC_SERVICE_TYPE INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE --
	-----------------------------------------------
	PROCEDURE QUERY_SERVICE_TYPE(P_RESULT           IN OUT REF_SERVICE_TYPE,
															 P_SERVICE_TYPE_ID  IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
															 P_SERVICE_CATEGORY IN DEFINITIONS.SERVICE_CATEGORY_GROUP.DESCRIPTION%TYPE,
															 P_DESCRIPTION      IN DEFINITIONS.SERVICE_TYPE.DESCRIPTION%TYPE,
															 P_ACTIVE           IN DEFINITIONS.SERVICE_TYPE.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE --
	------------------------------------------------
	PROCEDURE INSERT_SERVICE_TYPE(P_RESULT IN OUT TAB_SERVICE_TYPE);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE --
	------------------------------------------------
	PROCEDURE UPDATE_SERVICE_TYPE(P_RESULT IN OUT TAB_SERVICE_TYPE);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE --
	------------------------------------------------
	PROCEDURE DELETE_SERVICE_TYPE(P_RESULT IN OUT TAB_SERVICE_TYPE);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE --
	----------------------------------------------
	PROCEDURE LOCK_SERVICE_TYPE(P_RESULT IN OUT TAB_SERVICE_TYPE);

	------------------
	-- Record Group --
	------------------
	TYPE REC_DEPARTMENT IS RECORD(
		SERVICE_TYPE_ID      DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
		DESCRIPTION          DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
		ALL_SERVICES         DEFINITIONS.SERVICE_TYPE_DEPARTMENT_NATURE.ALL_SERVICES%TYPE,
		ACTIVE               DEFINITIONS.SERVICE_TYPE_DEPARTMENT_NATURE.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_DEPARTMENT IS REF CURSOR RETURN REC_DEPARTMENT;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_DEPARTMENT IS TABLE OF REC_DEPARTMENT INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_DEPARTMENT_NATURE --
	-----------------------------------------------
	PROCEDURE QUERY_DEPARTMENT_NATURE(P_RESULT          IN OUT REF_DEPARTMENT,
																		P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
																		P_DESCRIPTION     IN DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
																		P_ALL_SERVICES    IN DEFINITIONS.SERVICE_TYPE_DEPARTMENT_NATURE.ALL_SERVICES%TYPE,
																		P_ACTIVE          IN DEFINITIONS.SERVICE_TYPE_DEPARTMENT_NATURE.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_DEPARTMENT_NATURE --
	------------------------------------------------
	PROCEDURE INSERT_DEPARTMENT_NATURE(P_RESULT IN OUT TAB_DEPARTMENT);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_DEPARTMENT_NATURE --
	------------------------------------------------
	PROCEDURE UPDATE_DEPARTMENT_NATURE(P_RESULT IN OUT TAB_DEPARTMENT);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_DEPARTMENT_NATURE --
	------------------------------------------------
	PROCEDURE DELETE_DEPARTMENT_NATURE(P_RESULT IN OUT TAB_DEPARTMENT);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_DEPARTMENT_NATURE --
	----------------------------------------------
	PROCEDURE LOCK_DEPARTMENT_NATURE(P_RESULT IN OUT TAB_DEPARTMENT);

	------------------
	-- Record Group --
	------------------
	TYPE REC_SECTION IS RECORD(
		SERVICE_TYPE_ID      DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
		SECTION_NATURE_ID    DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
		DESCRIPTION          DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
		ALL_SERVICES         DEFINITIONS.SERVICE_TYPE_SECTION_NATURE.ALL_SERVICES%TYPE,
		ACTIVE               DEFINITIONS.SERVICE_TYPE_SECTION_NATURE.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SECTION IS REF CURSOR RETURN REC_SECTION;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SECTION IS TABLE OF REC_SECTION INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_SECTION_NATURE --
	-----------------------------------------------
	PROCEDURE QUERY_SECTION_NATURE(P_RESULT          IN OUT REF_SECTION,
																 P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
																 P_DESCRIPTION     IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
																 P_ALL_SERVICES    IN DEFINITIONS.SERVICE_TYPE_SECTION_NATURE.ALL_SERVICES%TYPE,
																 P_ACTIVE          IN DEFINITIONS.SERVICE_TYPE_SECTION_NATURE.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_SECTION_NATURE --
	------------------------------------------------
	PROCEDURE INSERT_SECTION_NATURE(P_RESULT IN OUT TAB_SECTION);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_SECTION_NATURE --
	------------------------------------------------
	PROCEDURE UPDATE_SECTION_NATURE(P_RESULT IN OUT TAB_SECTION);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_SECTION_NATURE --
	------------------------------------------------
	PROCEDURE DELETE_SECTION_NATURE(P_RESULT IN OUT TAB_SECTION);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_SECTION_NATURE --
	----------------------------------------------
	PROCEDURE LOCK_SECTION_NATURE(P_RESULT IN OUT TAB_SECTION);

	------------------
	-- Record Group --
	------------------
	TYPE REC_CPT IS RECORD(
		SERVICE_TYPE_ID DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		CPT_ID          DEFINITIONS.CPT.CPT_ID%TYPE,
		CPT_ID_DISP     DEFINITIONS.CPT.CPT_ID%TYPE,
		DESCRIPTION     DEFINITIONS.CPT.DESCRIPTION%TYPE,
		ACTIVE          DEFINITIONS.SERVICE_TYPE_CPT.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_CPT IS REF CURSOR RETURN REC_CPT;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_CPT IS TABLE OF REC_CPT INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_CPT --
	-----------------------------------------------
	PROCEDURE QUERY_CPT(P_RESULT          IN OUT REF_CPT,
											P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
											P_CPT_ID          IN DEFINITIONS.CPT.CPT_ID%TYPE,
											P_DESCRIPTION     IN DEFINITIONS.CPT.DESCRIPTION%TYPE,
											P_ACTIVE          IN DEFINITIONS.SERVICE_TYPE_CPT.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_CPT --
	------------------------------------------------
	PROCEDURE INSERT_CPT(P_RESULT IN OUT TAB_CPT);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_CPT --
	------------------------------------------------
	PROCEDURE UPDATE_CPT(P_RESULT IN OUT TAB_CPT);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_CPT --
	------------------------------------------------
	PROCEDURE DELETE_CPT(P_RESULT IN OUT TAB_CPT);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_CPT --
	----------------------------------------------
	PROCEDURE LOCK_CPT(P_RESULT IN OUT TAB_CPT);

	------------------
	-- Record Group --
	------------------
	TYPE REC_SERVICE_THERAPEUTIC_GROUP IS RECORD(
		SERVICE_TYPE_ID      DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		THERAPEUTIC_GROUP_ID PHARMACY.THERAPEUTIC_SUBGROUP.T_SUBGROUP_ID%TYPE,
		THERAPEUTIC_DESC     PHARMACY.THERAPEUTIC_GROUP.DESCRIPTION%TYPE,
		ALL_SERVICE          DEFINITIONS.SERVICE_THERAPEUTIC_GROUP.ALL_SERVICE%TYPE,
		ACTIVE               DEFINITIONS.SERVICE_THERAPEUTIC_GROUP.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SERVICE_THERAPEUTIC_GROUP IS REF CURSOR RETURN REC_SERVICE_THERAPEUTIC_GROUP;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SERVICE_THERAPEUTIC_GROUP IS TABLE OF REC_SERVICE_THERAPEUTIC_GROUP INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_SERVICE_THERAPEUTIC_GROUP --
	-----------------------------------------------
	PROCEDURE QUERY_THERAPEUTIC_GROUP(P_RESULT               IN OUT REF_SERVICE_THERAPEUTIC_GROUP,
																		P_SERVICE_TYPE_ID      IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
																		P_THERAPEUTIC_GROUP_ID IN PHARMACY.THERAPEUTIC_SUBGROUP.T_SUBGROUP_ID%TYPE,
																		P_DESCRIPTION          IN PHARMACY.THERAPEUTIC_GROUP.DESCRIPTION%TYPE,
																		P_ALL_SERVICES         IN DEFINITIONS.SERVICE_THERAPEUTIC_GROUP.ALL_SERVICE%TYPE,
																		P_ACTIVE               IN DEFINITIONS.SERVICE_THERAPEUTIC_GROUP.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_SERVICE_THERAPEUTIC_GROUP --
	------------------------------------------------
	PROCEDURE INSERT_THERAPEUTIC_GROUP(P_RESULT IN OUT TAB_SERVICE_THERAPEUTIC_GROUP);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_SERVICE_THERAPEUTIC_GROUP --
	------------------------------------------------
	PROCEDURE UPDATE_THERAPEUTIC_GROUP(P_RESULT IN OUT TAB_SERVICE_THERAPEUTIC_GROUP);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_SERVICE_THERAPEUTIC_GROUP --
	------------------------------------------------
	PROCEDURE DELETE_THERAPEUTIC_GROUP(P_RESULT IN OUT TAB_SERVICE_THERAPEUTIC_GROUP);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_SERVICE_THERAPEUTIC_GROUP --
	----------------------------------------------
	PROCEDURE LOCK_THERAPEUTIC_GROUP(P_RESULT IN OUT TAB_SERVICE_THERAPEUTIC_GROUP);

	------------------
	-- Record Group --
	------------------
	TYPE REC_SERVICE_SUB_GROUP IS RECORD(
		SERVICE_TYPE_ID      DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		THERAPEUTIC_GROUP_ID PHARMACY.THERAPEUTIC_SUBGROUP.T_SUBGROUP_ID%TYPE,
		SUB_GROUP_ID         PHARMACY.TG_SUBGROUP.T_SUBGROUP_ID%TYPE,
		SUB_GROUP_DESC       PHARMACY.THERAPEUTIC_SUBGROUP.DESCRIPTION%TYPE,
		ALL_SERVICE          DEFINITIONS.SERVICE_SUB_GROUP.ALL_SERVICE%TYPE,
		ACTIVE               DEFINITIONS.SERVICE_SUB_GROUP.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SERVICE_SUB_GROUP IS REF CURSOR RETURN REC_SERVICE_SUB_GROUP;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SERVICE_SUB_GROUP IS TABLE OF REC_SERVICE_SUB_GROUP INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_SUB_GROUP --
	-----------------------------------------------
	PROCEDURE QUERY_SUB_GROUP(P_RESULT          IN OUT REF_SERVICE_SUB_GROUP,
														P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
														P_SUB_GROUP_ID    IN PHARMACY.TG_SUBGROUP.T_SUBGROUP_ID%TYPE,
														P_DESCRIPTION     IN PHARMACY.THERAPEUTIC_SUBGROUP.DESCRIPTION%TYPE,
														P_ALL_SERVICES    IN DEFINITIONS.SERVICE_SUB_GROUP.ALL_SERVICE%TYPE,
														P_ACTIVE          IN DEFINITIONS.SERVICE_SUB_GROUP.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_SUB_GROUP --
	------------------------------------------------
	PROCEDURE INSERT_SUB_GROUP(P_RESULT IN OUT TAB_SERVICE_SUB_GROUP);

	------------------------------------------------
	-- This procedure will update SERVICE_SUB_GROUP --
	------------------------------------------------
	PROCEDURE UPDATE_SUB_GROUP(P_RESULT IN OUT TAB_SERVICE_SUB_GROUP);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_SUB_GROUP --
	------------------------------------------------
	PROCEDURE DELETE_SUB_GROUP(P_RESULT IN OUT TAB_SERVICE_SUB_GROUP);

	----------------------------------------------
	-- This procedure will lock SERVICE_SUB_GROUP --
	----------------------------------------------
	PROCEDURE LOCK_SUB_GROUP(P_RESULT IN OUT TAB_SERVICE_SUB_GROUP);

	------------------
	-- Record Group --
	------------------
	TYPE REC_SERVICE_TYPE_ITEM_GROUP IS RECORD(
		SERVICE_TYPE_ID DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		ITEM_GROUP_ID   ITEM.ITEM_GROUP.ITEM_GROUP_ID%TYPE,
		DESCRIPTION     ITEM.ITEM_GROUP.DESCRIPTION%TYPE,
		ALL_SERVICES    DEFINITIONS.SERVICE_TYPE_ITEM_GROUP.ALL_SERVICES%TYPE,
		ACTIVE          DEFINITIONS.SERVICE_TYPE_ITEM_GROUP.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SERVICE_TYPE_ITEM_GROUP IS REF CURSOR RETURN REC_SERVICE_TYPE_ITEM_GROUP;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SERVICE_TYPE_ITEM_GROUP IS TABLE OF REC_SERVICE_TYPE_ITEM_GROUP INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_ITEM_GROUP --
	-----------------------------------------------
	PROCEDURE QUERY_TYPE_ITEM_GROUP(P_RESULT          IN OUT REF_SERVICE_TYPE_ITEM_GROUP,
																	P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
																	P_ITEM_GROUP_ID   IN ITEM.ITEM_GROUP.ITEM_GROUP_ID%TYPE,
																	P_DESCRIPTION     IN ITEM.ITEM_GROUP.DESCRIPTION%TYPE,
																	P_ALL_SERVICES    IN DEFINITIONS.SERVICE_TYPE_ITEM_GROUP.ALL_SERVICES%TYPE,
																	P_ACTIVE          IN DEFINITIONS.SERVICE_TYPE_ITEM_GROUP.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_ITEM_GROUP --
	------------------------------------------------
	PROCEDURE INSERT_TYPE_ITEM_GROUP(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM_GROUP);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_ITEM_GROUP --
	------------------------------------------------
	PROCEDURE UPDATE_TYPE_ITEM_GROUP(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM_GROUP);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_ITEM_GROUP --
	------------------------------------------------
	PROCEDURE DELETE_TYPE_ITEM_GROUP(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM_GROUP);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_ITEM_GROUP --
	----------------------------------------------
	PROCEDURE LOCK_TYPE_ITEM_GROUP(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM_GROUP);

	------------------
	-- Record Group --
	------------------
	TYPE REC_SERVICE_TYPE_ITEM IS RECORD(
		SERVICE_TYPE_ID DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
		ITEM_GROUP_ID   ITEM.ITEM_GROUP.ITEM_GROUP_ID%TYPE,
		ITEM_ID         ITEM.ITEM.ITEM_ID%TYPE,
		DESCRIPTION     ITEM.ITEM.DESCRIPTION%TYPE,
		ACTIVE          DEFINITIONS.SERVICE_TYPE_ITEM.ACTIVE%TYPE);

	----------------
	-- REF CURSOR --
	----------------
	TYPE REF_SERVICE_TYPE_ITEM IS REF CURSOR RETURN REC_SERVICE_TYPE_ITEM;

	------------------
	-- PL-SQL TABLE --
	------------------
	TYPE TAB_SERVICE_TYPE_ITEM IS TABLE OF REC_SERVICE_TYPE_ITEM INDEX BY BINARY_INTEGER;

	-----------------------------------------------
	-- This procedure will query SERVICE_TYPE_ITEM --
	-----------------------------------------------
	PROCEDURE QUERY_TYPE_ITEM(P_RESULT          IN OUT REF_SERVICE_TYPE_ITEM,
														P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
														P_ITEM_ID         IN ITEM.ITEM.ITEM_ID%TYPE,
														P_DESCRIPTION     IN ITEM.ITEM.DESCRIPTION%TYPE,
														P_ACTIVE          IN DEFINITIONS.SERVICE_TYPE_ITEM.ACTIVE%TYPE);

	------------------------------------------------
	-- This procedure will insert SERVICE_TYPE_ITEM --
	------------------------------------------------
	PROCEDURE INSERT_TYPE_ITEM(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM);

	------------------------------------------------
	-- This procedure will update SERVICE_TYPE_ITEM --
	------------------------------------------------
	PROCEDURE UPDATE_TYPE_ITEM(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM);

	------------------------------------------------
	-- This procedure will DELETE SERVICE_TYPE_ITEM --
	------------------------------------------------
	PROCEDURE DELETE_TYPE_ITEM(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM);

	----------------------------------------------
	-- This procedure will lock SERVICE_TYPE_ITEM --
	----------------------------------------------
	PROCEDURE LOCK_TYPE_ITEM(P_RESULT IN OUT TAB_SERVICE_TYPE_ITEM);

	-------------------------------------------------------------------------------------------------
	-- This procedure will be called on Post event and it will log changes against SERVICE_TYPE_ID --
	-------------------------------------------------------------------------------------------------
	PROCEDURE POST_SERVICE_TYPE(P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
															P_SERVICE_TYPE    IN DEFINITIONS.SERVICE_CATEGORY_GROUP .SERVICE_CATEGORY_GROUP_ID%TYPE,
															P_ALERT_TEXT      OUT VARCHAR2,
															P_STOP            OUT CHAR);

	---------------------------------------------------------------------------------------------------
	-- This procedure will be called on Unpost event and it will log changes against SERVICE_TYPE_ID --
	---------------------------------------------------------------------------------------------------
	PROCEDURE UNPOST_SERVICE_TYPE(P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
																P_ALERT_TEXT      OUT VARCHAR2,
																P_STOP            OUT CHAR);

END;
```

### DEFINITIONS.PKG_S01FRM00365
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00365 AS

  /***********************************************************************************************
         OBJECTIVE := 1. This Package will be used for Package Service Type
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        06-Jun-2016   M. Ali Khubaib         1. Created this Package.
  ************************************************************************************************/
  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PACKAGES IS RECORD(
    PACKAGE_ID         DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
    PACKAGE_NAME       DEFINITIONS.PACKAGES.DESCRIPTION%TYPE,
    PACKAGE_SHORT_DESC DEFINITIONS.PACKAGES.SHORT_DESC%TYPE,
    TRANS_DATE         DEFINITIONS.PACKAGES.TRANS_DATE%TYPE,
    PACKAGE_TYPE       DEFINITIONS.PACKAGE_TYPE.DESCRIPTION%TYPE,
    PACKAGE_PRICE      DEFINITIONS.PACKAGES.PRICE%TYPE,
    ACTIVE             DEFINITIONS.PACKAGES.ACTIVE%TYPE,
    TREATMENT_COVER    VARCHAR2(32),
    PRICE_SOURCE       VARCHAR2(32),
    PROCESS_METHOD     DEFINITIONS.PACKAGE_DETAIL.PROCESS_METHOD%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PACKAGES IS REF CURSOR RETURN REC_PACKAGES;

  ----------------------------------------
  -- This procedure will query packages --
  ----------------------------------------
  PROCEDURE QUERY_PACKAGES(P_RESULT     IN OUT REF_PACKAGES,
                           P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                           P_NAME       IN DEFINITIONS.PACKAGES.DESCRIPTION%TYPE,
                           P_PRICE      IN DEFINITIONS.PACKAGES.PRICE%TYPE);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PACKAGE_SERVICES IS RECORD(
    PACKAGE_ID             DEFINITIONS.PACKAGE_SERVICES.PACKAGE_ID%TYPE,
    SERVICE_TYPE_ID        DEFINITIONS.PACKAGE_SERVICES.SERVICE_TYPE_ID%TYPE,
    SERVICE_NAME           DEFINITIONS.SERVICE_TYPE.DESCRIPTION%TYPE,
    CONTRACT_TYPE          DEFINITIONS.SERVICE_CATEGORY_GROUP.SERVICE_CATEGORY_GROUP_ID%TYPE,
    CONTRACT_TYPE_DISP     DEFINITIONS.DEF_SERVICE_CATEGORY.DESCRIPTION%TYPE,
    ALL_SERVICES           DEFINITIONS.PACKAGE_SERVICES.ALL_SERVICES%TYPE,
    TREATMENT_LIMIT_APPLY  DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_APPLY%TYPE,
    TREATMENT_LIMIT_AMOUNT DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_AMOUNT%TYPE,
    ACTIVE                 DEFINITIONS.PACKAGE_SERVICES.ACTIVE%TYPE,
    NO_OF_ITEM_ALLOWED     DEFINITIONS.PACKAGE_SERVICES.NO_OF_ITEM_ALLOWED%TYPE,
    FREQUENCY              DEFINITIONS.PACKAGE_SERVICES.FREQUENCY%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PACKAGES_SERVICES IS REF CURSOR RETURN REC_PACKAGE_SERVICES;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PACKAGES_SERVICES IS TABLE OF REC_PACKAGE_SERVICES INDEX BY BINARY_INTEGER;

  -------------------------------------------------
  -- This procedure will query packages_services --
  -------------------------------------------------
  PROCEDURE QUERY_PACKAGES_SERVICES(P_RESULT          IN OUT REF_PACKAGES_SERVICES,
                                    P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                                    P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                                    P_SERVICE_NAME    IN DEFINITIONS.SERVICE_TYPE.DESCRIPTION%TYPE,
                                    P_ALL_SERVICES    IN DEFINITIONS.PACKAGE_SERVICES.ALL_SERVICES%TYPE,
                                    P_APPLY_CL        IN DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_APPLY%TYPE,
                                    P_LIMIT           IN DEFINITIONS.PACKAGE_SERVICES.TREATMENT_LIMIT_AMOUNT%TYPE,
                                    P_ACTIVE          IN DEFINITIONS.PACKAGE_SERVICES.ACTIVE%TYPE);

  --------------------------------------------------
  -- This procedure will insert packages_services --
  --------------------------------------------------
  PROCEDURE INSERT_PACKAGES_SERVICES(P_RESULT IN OUT TAB_PACKAGES_SERVICES);

  ----------------------------------------------------
  -- This procedure will update packages_services --
  --------------------------------------------------
  PROCEDURE UPDATE_PACKAGES_SERVICES(P_RESULT IN OUT TAB_PACKAGES_SERVICES);

  ----------------------------------------------------
  -- This procedure will DELETE packages_services --
  --------------------------------------------------
  PROCEDURE DELETE_PACKAGES_SERVICES(P_RESULT IN OUT TAB_PACKAGES_SERVICES);

  --------------------------------------------------
  -- This procedure will lock packages_services --
  ------------------------------------------------
  PROCEDURE LOCK_PACKAGES_SERVICES(P_RESULT IN OUT TAB_PACKAGES_SERVICES);

  ------------------
  -- Record Group --
  ------------------
  TYPE REC_PACKAGE_ITEM IS RECORD(
    PACKAGE_ID         DEFINITIONS.PACKAGE_ITEM.PACKAGE_ID%TYPE,
    SERVICE_TYPE_ID    DEFINITIONS.PACKAGE_ITEM.SERVICE_TYPE_ID%TYPE,
    ITEM_ID            DEFINITIONS.PACKAGE_ITEM.ITEM_ID%TYPE,
    ITEM_NAME          VARCHAR2(250),
    PRICE              DEFINITIONS.PACKAGE_ITEM.PRICE%TYPE,
    QUANTITY           DEFINITIONS.PACKAGE_ITEM.QUANTITY%TYPE,
    NO_OF_ITEM_ALLOWED DEFINITIONS.PACKAGE_ITEM.NO_OF_ITEM_ALLOWED%TYPE,
    NO_OF_ITEM_AVAILED DEFINITIONS.PACKAGE_ITEM.NO_OF_ITEM_AVAILED%TYPE,
    ACTIVE             DEFINITIONS.PACKAGE_ITEM.ACTIVE%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_PACKAGE_ITEM IS REF CURSOR RETURN REC_PACKAGE_ITEM;

  ------------------
  -- PL-SQL TABLE --
  ------------------
  TYPE TAB_PACKAGE_ITEM IS TABLE OF REC_PACKAGE_ITEM INDEX BY BINARY_INTEGER;

  --------------------------------------------
  -- This procedure will query PACKAGE_ITEM --
  --------------------------------------------
  PROCEDURE QUERY_PACKAGE_ITEM(P_RESULT          IN OUT REF_PACKAGE_ITEM,
                               P_PACKAGE_ID      IN DEFINITIONS.PACKAGE_SERVICES.PACKAGE_ID%TYPE,
                               P_SERVICE_TYPE_ID IN DEFINITIONS.PACKAGE_SERVICES.SERVICE_TYPE_ID%TYPE,
                               P_ITEM_ID         IN DEFINITIONS.PACKAGE_ITEM.ITEM_ID%TYPE,
                               P_PRICE           IN DEFINITIONS.PACKAGE_ITEM.PRICE%TYPE,
                               P_QUANTITY        IN DEFINITIONS.PACKAGE_ITEM.QUANTITY%TYPE,
                               P_ITEM_ALLOWED    IN DEFINITIONS.PACKAGE_ITEM.NO_OF_ITEM_ALLOWED%TYPE,
                               P_ACTIVE          IN DEFINITIONS.PACKAGE_ITEM.ACTIVE%TYPE,
                               P_ITEM_NAME       IN ITEM.ITEM.DESCRIPTION%TYPE);

  ---------------------------------------------
  -- This procedure will insert PACKAGE_ITEM --
  ---------------------------------------------
  PROCEDURE INSERT_PACKAGE_ITEM(P_RESULT IN OUT TAB_PACKAGE_ITEM);

  ---------------------------------------------
  -- This procedure will update PACKAGE_ITEM --
  ---------------------------------------------
  PROCEDURE UPDATE_PACKAGE_ITEM(P_RESULT IN OUT TAB_PACKAGE_ITEM);

  ---------------------------------------------
  -- This procedure will DELETE PACKAGE_ITEM --
  ---------------------------------------------
  PROCEDURE DELETE_PACKAGE_ITEM(P_RESULT IN OUT TAB_PACKAGE_ITEM);

  -------------------------------------------
  -- This procedure will lock PACKAGE_ITEM --
  -------------------------------------------
  PROCEDURE LOCK_PACKAGE_ITEM(P_RESULT IN OUT TAB_PACKAGE_ITEM);

  ----------------------------------------
  -- This procedure will POPULATE ITEMS --
  ----------------------------------------
  PROCEDURE POPULATE_ITEMS(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                           P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                           P_SERVICE_TYPE    IN DEFINITIONS.SERVICE_CATEGORY_GROUP.SERVICE_CATEGORY_GROUP_ID%TYPE,
                           P_ORGANIZATION_ID IN DEFINITIONS.LOCATION.ORGANIZATION_ID%TYPE,
                           P_LOCATION_ID     IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_ALERT_TEXT      OUT VARCHAR2,
                           P_STOP            OUT VARCHAR2);

  --------------------------------------------------------------------------------------------
  -- This procedure will be called on Post event and it will log changes against PACKAGE_ID --
  --------------------------------------------------------------------------------------------
  PROCEDURE POST(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                 P_ALERT_TEXT OUT VARCHAR2,
                 P_STOP       OUT CHAR);

  ----------------------------------------------------------------------------------------------
  -- This procedure will be called on Unpost event and it will log changes against PACKAGE_ID --
  ----------------------------------------------------------------------------------------------
  PROCEDURE UNPOST(P_PACKAGE_ID IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                   P_ALERT_TEXT OUT VARCHAR2,
                   P_STOP       OUT CHAR);
  ----------------------------------------
  -- This procedure will Delete ITEMS   --
  ----------------------------------------
  PROCEDURE DELETE_ALL_ITEMS(P_PACKAGE_ID      IN DEFINITIONS.PACKAGES.PACKAGE_ID%TYPE,
                             P_SERVICE_TYPE_ID IN DEFINITIONS.SERVICE_TYPE.SERVICE_TYPE_ID%TYPE,
                             P_ALERT_TEXT      OUT VARCHAR2,
                             P_STOP            OUT VARCHAR2);

END;
```

### DEFINITIONS.PKG_S01FRM00377
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00377 IS

  /***********************************************************************************************
         FUNCTION NAME: F_GET_CANCER_GROUP
         PURPOSE: THIS FUNCTION IS USED TO GET CANCER GROUP NAME AGAINST CANCER GROUP ID 
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE         AUTHOR                  DESCRIPTION
         ---------  ----------   ---------------         -----------------------------------
         1.0       28-APR-2020   QAISER MAJEED          1. CREATED THIS FUNCTION
  ************************************************************************************************/
  FUNCTION F_GET_CANCER_GROUP(P_CANCER_GROUP_ID   IN DEFINITIONS.CANCER_GROUPS.CANCER_GROUP_ID%TYPE)
           RETURN VARCHAR2;

END PKG_S01FRM00377;
```

### DEFINITIONS.PKG_S01FRM00385
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00385 IS

  -- Author  : Fiaz Ahmad
  -- Created : 09/05/2017 11:09:55 AM
  -- Purpose :

  TYPE REC_CPT_SETUP IS RECORD(
    ADMISSION_TYPE     DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%type,
    CPT_ID             DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%type,
    ADMISSION_TYPE_REC DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ADMISSION_TYPE%type,
    CPT_ID_REC         DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.CPT_ID%type,
    CPT_CODE           VARCHAR2(10),
    CPT_DESC           DEFINITIONS.CPT.DESCRIPTION%TYPE,
    ACTIVE             DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ACTIVE%TYPE,
    ORDER_BY           DEFINITIONS.ADMISSION_TYPE_CPT_SETUP.ORDER_BY%TYPE);

  --------------------------------------------------------------------------
  TYPE CUR_CPT_SETUP IS REF CURSOR RETURN REC_CPT_SETUP;

  TYPE TAB_CPT_SETUP IS TABLE OF REC_CPT_SETUP INDEX BY BINARY_INTEGER;
  ---------------------------------------------------------------------
  PROCEDURE P_CPT_SETUP_QUERY(P_RECORD      IN OUT CUR_CPT_SETUP,
                              P_CPT_CODE    IN VARCHAR2,
                              P_CPT_DESC    IN VARCHAR2,
                              P_ACTIVE      IN VARCHAR2,
                              P_LOCATION_ID IN VARCHAR2,
                              P_OBJECT_CODE IN VARCHAR2,
                              P_USER_MRNO   IN VARCHAR2,
                              P_EVENT       IN VARCHAR2);
  -------------------------------------------------------------------------
  PROCEDURE P_CPT_SETUP_INSERT(P_RECORD      IN OUT TAB_CPT_SETUP,
                               P_LOCATION_ID IN VARCHAR2,
                               P_OBJECT_CODE IN VARCHAR2,
                               P_USER_MRNO   IN VARCHAR2,
                               P_EVENT       IN VARCHAR2);
  -------------------------------------------------------------------------
  PROCEDURE P_CPT_SETUP_UPDATE(P_RECORD      IN OUT TAB_CPT_SETUP,
                               P_LOCATION_ID IN VARCHAR2,
                               P_OBJECT_CODE IN VARCHAR2,
                               P_USER_MRNO   IN VARCHAR2,
                               P_EVENT       IN VARCHAR2);
  -------------------------------------------------------------------------
  PROCEDURE P_CPT_SETUP_DELETE(P_RECORD      IN OUT TAB_CPT_SETUP,
                               P_LOCATION_ID IN VARCHAR2,
                               P_OBJECT_CODE IN VARCHAR2,
                               P_USER_MRNO   IN VARCHAR2,
                               P_EVENT       IN VARCHAR2);
  ------------------------------------------------------------------------
  PROCEDURE P_CPT_SETUP_LOCK(P_RESULT IN TAB_CPT_SETUP);
  ------------------------------------------------------------------------
END PKG_S01FRM00385;
```

### DEFINITIONS.PKG_S01FRM00411
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00411 IS
  -- AUTHOR  : Faran Munawar Ghouri 
  -- CREATED : 8/27/2018 07:39:55 PM
  -- PURPOSE : SETUP FORM REQUIRED TO DEFINE SETUP OF GENDER MAP
  -------------------------------------------------------------------------
  TYPE REC_GMAP IS RECORD(
    GENDER_ID       DEFINITIONS.GENDER_MAP.SEX_ID%TYPE,
    GENDER_DESC     DEFINITIONS.SEX.DESCRIPTION%TYPE,
    MAP_GENDER_ID   DEFINITIONS.GENDER_MAP.MAP_SEXID%TYPE,
    MAP_GENDER_DESC DEFINITIONS.SEX.DESCRIPTION%TYPE,
    ACTIVE          DEFINITIONS.GENDER_MAP.ACTIVE%TYPE,
    M_ROWID         ROWID);

  TYPE CUR_GMAP IS REF CURSOR; --- RETURN REC_GMAP;
  TYPE TAB_GMAP IS TABLE OF REC_GMAP INDEX BY BINARY_INTEGER;

  --------------------- DEFINING PROCEDURE TO QUERY RECORD ---------------------------------------------------------------------------------
  PROCEDURE P_QUERY(P_RESULT              IN OUT CUR_GMAP,
                    P_SEX_ID              IN VARCHAR2,
                    P_MAP_SEXID           IN VARCHAR2,
                    P_ACTIVE              IN VARCHAR2,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2);
  ----------------------------DEFINING PROCEDURE OF INSERT-----------------------------------------------------------------------------------
  PROCEDURE P_INSERT(P_RESULT              IN OUT TAB_GMAP,
                     P_CALLING_LOCATION_ID IN VARCHAR2,
                     P_CALLING_OBJECT      IN VARCHAR2,
                     P_CALLING_USER        IN VARCHAR2,
                     P_CALLING_EVENT       IN VARCHAR2,
                     P_ERROR               OUT VARCHAR2);
  ----------------------------DEFINING PROCEDURE OF UPDATE------------------------------------------------------------------------------------
  PROCEDURE P_UPDATE(P_RESULT              IN OUT TAB_GMAP,
                     P_CALLING_LOCATION_ID IN VARCHAR2,
                     P_CALLING_OBJECT      IN VARCHAR2,
                     P_CALLING_USER        IN VARCHAR2,
                     P_CALLING_EVENT       IN VARCHAR2,
                     P_ERROR               OUT VARCHAR2);
  -----------------------------------------------------------------------------------------------------------------------------------------
  PROCEDURE P_DELETE(P_RESULT              IN OUT TAB_GMAP,
                     P_CALLING_LOCATION_ID IN VARCHAR2,
                     P_CALLING_OBJECT      IN VARCHAR2,
                     P_CALLING_USER        IN VARCHAR2,
                     P_CALLING_EVENT       IN VARCHAR2,
                     P_ERROR               OUT VARCHAR2);
  ----------------------- DEFINING PROCEDURE TO LOCK RECORD -------------------------------------------------------------------------------
  PROCEDURE P_LOCK(P_RESULT IN OUT TAB_GMAP);

END PKG_S01FRM00411;
```

### DEFINITIONS.PKG_S01FRM00421
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00421 IS

  -- AUTHOR  : IRFANALI
  -- CREATED : 3/12/2019 4:57:30 PM
  -- PURPOSE : GENERATE THE SCRIPT FOR COUNTERS
  /*******************************************************/
  FUNCTION F_GENERATE_SCRIPT(P_COUNTER_ID     IN COUNTERS.SYSTEM_COUNTERS.COUNTER_ID%TYPE,
                             P_KEY            IN COUNTERS.SYSTEM_COUNTERS.COUNTER_KEY%TYPE,
                             P_BODY           OUT LONG,
                             P_LOC_ID         IN VARCHAR2,
                             P_CALLING_OBJECT IN VARCHAR2,
                             P_CALLING_USER   IN VARCHAR2,
                             P_CALLING_EVENT  IN VARCHAR2,
                             P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;

END PKG_S01FRM00421;
```

### DEFINITIONS.PKG_S01FRM00423
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00423 AS
  -- Author AB.Wadood            
  -- Purpose : This package uesd for online reports and related.
  --         :   
  --*****************************************************************************************
  --                                   Block  online reports                            --
  --*****************************************************************************************
  TYPE REC_RA IS RECORD(
    LOCATION_ID         DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_ID %TYPE,
    LOCATION_DESC       DEFINITIONS.LOCATION_RADIOLOGY.LOCATION_DESC%TYPE,
    ACTIVE              DEFINITIONS.LOCATION_RADIOLOGY.ACTIVE%TYPE,
    CONTINGENCY_FLAG    DEFINITIONS.LOCATION_RADIOLOGY.CONTINGENCY_FLAG%TYPE,
    CONTINGENCY_REMARKS DEFINITIONS.LOCATION_RADIOLOGY.CONTINGENCY_REMARKS%TYPE,
    REPORTS_ONLINE      DEFINITIONS.LOCATION_RADIOLOGY.REPORTS_ONLINE %TYPE,
    SEND_REPORTS        DEFINITIONS.LOCATION_RADIOLOGY.SEND_REPORTS%TYPE,
    SEND_REPORTS_EMAIL  DEFINITIONS.LOCATION_RADIOLOGY.SEND_REPORTS_EMAIL%TYPE,
    SEND_ALERTS         DEFINITIONS.LOCATION_RADIOLOGY.SEND_ALERTS%TYPE,
    SEND_ALERTS_EMAIL   DEFINITIONS.LOCATION_RADIOLOGY.SEND_ALERTS_EMAIL%TYPE);

  TYPE CUR_RA IS REF CURSOR; --  RETURN REC_RA ;
  TYPE TAB_RA IS TABLE OF REC_RA INDEX BY BINARY_INTEGER;
  --*****************************************************************************************
  PROCEDURE RA_QUERY(P_RECORD         IN OUT CUR_RA,
                     P_LOCATION_ID    IN VARCHAR2,
                     P_LOCATION_DESC  IN VARCHAR2,
                     P_CALLING_OBJECT IN VARCHAR2,
                     P_CALLING_USER   IN VARCHAR2,
                     P_CALLING_EVENT  IN VARCHAR2,
                     P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************

  PROCEDURE RA_INSERT(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_UPDATE(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_DELETE(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_LOCK(P_RECORD         IN OUT TAB_RA,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2);

--************************************************************************************---

END PKG_S01FRM00423;
```

### DEFINITIONS.PKG_S01FRM00424
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00424 AS
  -- Author AB.Haseeb
  -- Purpose : This package uesd for online reports and related.
  --         :
  --*****************************************************************************************
  --                                   Block  DELETE_OLD_ARCHIVE                            --
  --*****************************************************************************************
  TYPE REC_RA IS RECORD(
    OWNER        DBSOURCE.DELETE_OLD_ARCHIVE.OWNER%TYPE,
    OBJECT_NAME  DBSOURCE.DELETE_OLD_ARCHIVE.OBJECT_NAME%TYPE,
    COLUMN_NAME  DBSOURCE.DELETE_OLD_ARCHIVE.COLUMN_NAME%TYPE,
    DAYS_LIMIT   DBSOURCE.DELETE_OLD_ARCHIVE.DAYS_LIMIT%TYPE,
    ATTEMPT_LOCK DBSOURCE.DELETE_OLD_ARCHIVE.ATTEMPT_LOCK%TYPE,
    ACTIVE       DBSOURCE.DELETE_OLD_ARCHIVE.ACTIVE%TYPE);

  TYPE CUR_RA IS REF CURSOR; -- RETURN REC_RA;
  TYPE TAB_RA IS TABLE OF REC_RA INDEX BY BINARY_INTEGER;
  --*****************************************************************************************
  PROCEDURE RA_QUERY(P_RECORD         IN OUT CUR_RA,
                     P_OWNER          IN VARCHAR2,
                     P_OBJECT_NAME    IN VARCHAR2,
                     P_LOCATION_ID    IN VARCHAR2,
                     P_CALLING_OBJECT IN VARCHAR2,
                     P_CALLING_USER   IN VARCHAR2,
                     P_CALLING_EVENT  IN VARCHAR2,
                     P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_INSERT(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_UPDATE(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_DELETE(P_RECORD         IN OUT TAB_RA,
                      P_LOCATION_ID    IN VARCHAR2,
                      P_CALLING_OBJECT IN VARCHAR2,
                      P_CALLING_USER   IN VARCHAR2,
                      P_CALLING_EVENT  IN VARCHAR2,
                      P_ERROR          OUT VARCHAR2);
  --*****************************************************************************************
  PROCEDURE RA_LOCK(P_RECORD         IN OUT TAB_RA,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2);

--************************************************************************************---

END PKG_S01FRM00424;
```

### DEFINITIONS.PKG_S01FRM00429
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00429 AS
  /***********************************************************************************************
         OBJECTIVE := THIS PACKAGE WAS CREATED FOR DOCUMENT ATTACHMENT.
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        15-OCT-2019   FURQAN AKRAM           1. CREATED THIS PACKAGE.
  ************************************************************************************************/

  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_DOCUMENT_ATTACHMENT IS RECORD(
    TABLE_NAME       HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
    REFERENCE_KEY    HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
    SERIAL_NUMBER    HIS.DOCUMENT_ATTACHMENT.SERIAL_NUMBER%TYPE,
    OBJECT_CODE      HIS.DOCUMENT_ATTACHMENT.OBJECT_CODE%TYPE,
    TRANSACTION_TYPE HIS.DOCUMENT_ATTACHMENT.TRANSACTION_TYPE%TYPE,
    DOCUMENT_NAME    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_NAME%TYPE,
    DOCUMENT_PATH    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_PATH%TYPE,
    ATTACHED_BY      REGISTRATION.PATIENT.MRNO%TYPE,
    ATTACHED_BY_NAME VARCHAR2(2000),
    ATTACHED_DATE    DATE,
    REMARKS          HIS.DOCUMENT_ATTACHMENT.REMARKS%TYPE,
    DELETED_BY       REGISTRATION.PATIENT.MRNO%TYPE,
    DELETED_DATE     DATE,
    DELETED_TERMINAL HIS.DOCUMENT_ATTACHMENT.DELETED_TERMINAL%TYPE,
    STATUS_ID        HIS.DOCUMENT_ATTACHMENT.STATUS_ID%TYPE,
    ORG_ID           HIS.DOCUMENT_ATTACHMENT.ORG_ID%TYPE,
    ZON_ID           HIS.DOCUMENT_ATTACHMENT.ZON_ID%TYPE,
    LOC_ID           HIS.DOCUMENT_ATTACHMENT.LOC_ID%TYPE,
    --
    DOCUMENT_ID         HIS.DOCUMENT_ATTACHMENT.DOCUMENT_ID%TYPE,
    DOC_TYPE_ID         HIS.DOCUMENT_ATTACHMENT.DOC_TYPE_ID%TYPE,
    ATTACH_EMP_DOCUMENT HIS.DOCUMENT_ATTACHMENT.ATTACH_EMP_DOCUMENT%TYPE);

  ----------------
  -- REF CURSOR --
  ----------------
  TYPE REF_DOCUMENT_ATTACHMENT IS REF CURSOR RETURN REC_DOCUMENT_ATTACHMENT;

  -----------------
  -- PLSQL TABLE --
  -----------------
  TYPE TAB_DOCUMENT_ATTACHMENT IS TABLE OF REC_DOCUMENT_ATTACHMENT INDEX BY BINARY_INTEGER;
  TYPE TAB_DOC_ATTACHMENT IS TABLE OF REC_DOCUMENT_ATTACHMENT;

  ---------------------------------------------------------
  -- THIS PROCEDURE WILL BE USE TO QUERY DOCUMENT'S DATA --
  ---------------------------------------------------------
  PROCEDURE QUERY_DOCUMENT_ATTACHMENT(P_RESULT        IN OUT REF_DOCUMENT_ATTACHMENT,
                                      P_TABLE_NAME    IN HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
                                      P_REFERENCE_KEY IN HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE);

  FUNCTION F_QUERY_DOCUMENT_ATTACHMENT(P_TABLE_NAME    IN HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
                                       P_REFERENCE_KEY IN HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE)
    RETURN TAB_DOC_ATTACHMENT
    PIPELINED;

  ------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USE TO LOCK DOCUMENT_ATTACHMENT TABLE --
  ------------------------------------------------------------------
  PROCEDURE LOCK_DOCUMENT_ATTACHMENT(P_RESULT IN OUT TAB_DOCUMENT_ATTACHMENT);

  -------------------------------------------------------
  -- THIS PROCEDURE WILL LOCK DRUG_ADMIN_SCHEDULE_OPAT --
  -------------------------------------------------------
  PROCEDURE INSERT_DOCUMENT_ATTACHMENT(P_RESULT IN OUT TAB_DOCUMENT_ATTACHMENT);

  --------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USE TO UPDATE DOCUMENT_ATTACHMENT --
  --------------------------------------------------------------
  PROCEDURE UPDATE_DOCUMENT_ATTACHMENT(P_RESULT IN OUT TAB_DOCUMENT_ATTACHMENT);

  --------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USE TO DELETE DOCUMENT_ATTACHMENT --
  --------------------------------------------------------------
  PROCEDURE DELETE_DOCUMENT_ATTACHMENT(P_RESULT IN OUT TAB_DOCUMENT_ATTACHMENT);
  -------------------------------------------------
  -- THIS FUNCTION WILL CHECK DELETION AUTHORITY --
  -------------------------------------------------
  FUNCTION IS_DELETION_ALLOWED(P_USER_MRNO   IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_ATTACHED_BY IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN VARCHAR2;

  /***********************************************************************************************
           PROCEDURE NAME: UPD_DOCUMENT_FLAGS
           PURPOSE: THIS PROCEDURE IS USED TO UPDATE THE DOCUMENT FLAG WITH PROCESSED VALUE
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        10-JUN-2021  SALMAN(7236)            1. Created this Procedure(CR:21-474)
  ************************************************************************************************/
  PROCEDURE UPD_DOCUMENT_FLAGS(P_TABLE_NAME     IN HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
                               P_REFERENCE_KEY  IN HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
                               P_SERIAL_NO      IN HIS.DOCUMENT_ATTACHMENT.SERIAL_NUMBER%TYPE,
                               P_DOCUMENT_ID    IN VARCHAR2,
                               P_FILE_PROCESSED IN VARCHAR2,
                               P_STOP           OUT VARCHAR2,
                               P_ALERT_TEXT     OUT VARCHAR2);
  ------------------
  -- RECORD GROUP --
  ------------------
  TYPE REC_QRY_ATTACHMENT IS RECORD(
    TABLE_NAME       HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
    REFERENCE_KEY    HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
    SERIAL_NUMBER    HIS.DOCUMENT_ATTACHMENT.SERIAL_NUMBER%TYPE,
    OBJECT_CODE      HIS.DOCUMENT_ATTACHMENT.OBJECT_CODE%TYPE,
    TRANSACTION_TYPE HIS.DOCUMENT_ATTACHMENT.TRANSACTION_TYPE%TYPE,
    DOCUMENT_NAME    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_NAME%TYPE,
    DOCUMENT_PATH    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_PATH%TYPE,
    ATTACHED_BY      REGISTRATION.PATIENT.MRNO%TYPE,
    ATTACHED_DATE    DATE,
    REMARKS          HIS.DOCUMENT_ATTACHMENT.REMARKS%TYPE,
    DELETED_BY       REGISTRATION.PATIENT.MRNO%TYPE,
    DELETED_DATE     DATE,
    DELETED_TERMINAL HIS.DOCUMENT_ATTACHMENT.DELETED_TERMINAL%TYPE,
    STATUS_ID        HIS.DOCUMENT_ATTACHMENT.STATUS_ID%TYPE,
    ATTACH_DOCUMENT  HIS.DOCUMENT_ATTACHMENT.ATTACH_DOCUMENT%TYPE,
    --
    ORG_ID HIS.DOCUMENT_ATTACHMENT.ORG_ID%TYPE,
    ZON_ID HIS.DOCUMENT_ATTACHMENT.ZON_ID%TYPE,
    LOC_ID HIS.DOCUMENT_ATTACHMENT.LOC_ID%TYPE);

  TYPE REF_QRY_ATTACHMENT IS REF CURSOR RETURN REC_QRY_ATTACHMENT;
  -- *************************************************************************************************** --

  TYPE REC_QRY_ATTACHMENT_APX IS RECORD(
    TABLE_NAME       HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
    REFERENCE_KEY    HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
    SERIAL_NUMBER    HIS.DOCUMENT_ATTACHMENT.SERIAL_NUMBER%TYPE,
    OBJECT_CODE      HIS.DOCUMENT_ATTACHMENT.OBJECT_CODE%TYPE,
    TRANSACTION_TYPE HIS.DOCUMENT_ATTACHMENT.TRANSACTION_TYPE%TYPE,
    DOCUMENT_NAME    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_NAME%TYPE,
    DOCUMENT_PATH    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_PATH%TYPE,
    ATTACHED_BY      REGISTRATION.PATIENT.MRNO%TYPE,
    ATTACHED_DATE    DATE,
    REMARKS          HIS.DOCUMENT_ATTACHMENT.REMARKS%TYPE,
    DELETED_BY       REGISTRATION.PATIENT.MRNO%TYPE,
    DELETED_DATE     DATE,
    DELETED_TERMINAL HIS.DOCUMENT_ATTACHMENT.DELETED_TERMINAL%TYPE,
    STATUS_ID        HIS.DOCUMENT_ATTACHMENT.STATUS_ID%TYPE,
    ATTACH_DOCUMENT  HIS.DOCUMENT_ATTACHMENT.ATTACH_DOCUMENT%TYPE,
    DOCUMENT_ID      HIS.DOCUMENT_ATTACHMENT.DOCUMENT_ID%TYPE,
    FILE_TYPE_ID     HIS.DOCUMENT_ATTACHMENT.FILE_TYPE_ID%TYPE,
    DOCUMENT_TYPE    HIS.DOCUMENT_ATTACHMENT.DOCUMENT_TYPE%TYPE,
    LOCATION_ID      HIS.DOCUMENT_ATTACHMENT.LOCATION_ID%TYPE,
    ORG_ID           HIS.DOCUMENT_ATTACHMENT.ORG_ID%TYPE,
    ZON_ID           HIS.DOCUMENT_ATTACHMENT.ZON_ID%TYPE,
    LOC_ID           HIS.DOCUMENT_ATTACHMENT.LOC_ID%TYPE);

  TYPE REF_QRY_ATTACHMENT_APX IS REF CURSOR RETURN REC_QRY_ATTACHMENT_APX;
  -- *************************************************************************************************** --

  /***********************************************************************************************
           PROCEDURE NAME: REF_QRY_ATTACHMENT
           PURPOSE: THIS PROCEDURE IS USED TO QUERY THE DOCUMENTS
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        10-JUN-2021  SALMAN(7236)            1. Created this Procedure(CR:21-474)
  ************************************************************************************************/
  PROCEDURE QRY_DOCUMENT_ATTACHMENT(P_RESULT    IN OUT REF_QRY_ATTACHMENT,
                                    P_FROM_DATE IN DATE,
                                    P_TO_DATE   IN DATE,
                                    P_ROWS      IN NUMBER DEFAULT NULL);

  -- =================================================================================================== --
  --
  --

  /********************************************************************************************************
     PROCEDURE NAME: QRY_DOCUMENT_ATTACHMENT_APX
     PURPOSE: THIS PROCEDURE IS USED TO QUERY THE DOCUMENTS
     ---------------------------------------------------------------------------------------------------
     REVISIONS:
     Ver         Date             Author                  Description
     ---------   --------------   ---------------------   ----------------------------------------------
     1.0         22-AUG-2024      Hafiz Abrar Ahmed       1. Created this procedure
  ********************************************************************************************************/
  PROCEDURE QRY_DOCUMENT_ATTACHMENT_APX(P_RESULT    IN OUT REF_QRY_ATTACHMENT_APX,
                                        P_FROM_DATE IN DATE,
                                        P_TO_DATE   IN DATE,
                                        P_ROWS      IN NUMBER DEFAULT NULL);
  -- =================================================================================================== --
  --
  --

  /***********************************************************************************************
           FUNCTION NAME: GET_DOCUMENT_PATH_AND_NAME
           PURPOSE: THIS FUNCTION IS USED TO GET THE DOCUMENT FINAL PATH
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        15-JUN-2021  SALMAN(7236)            1. Created this Procedure(CR:21-474)
  ************************************************************************************************/
  FUNCTION GET_DOCUMENT_PATH_AND_NAME(P_DOCUMENT_ID IN HIS.DOCUMENT_ATTACHMENT.DOCUMENT_ID%TYPE)
    RETURN VARCHAR2;

  /***********************************************************************************************
           PROCEDURE NAME: DOC_ATTACHMENT_SETUP_WISE
           PURPOSE: This procedure is used to insert/update document attachment in DB
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        23-APR-2021  Salman (7236)           1. Created this PROCEDURE(CR:).
  ************************************************************************************************/
  PROCEDURE DOC_ATTACHMENT_SETUP_WISE(P_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                                      P_TABLE_NAME    IN HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
                                      P_REFERENCE_KEY IN HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
                                      P_OBJECT_CODE   IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                      P_STOP          OUT VARCHAR2,
                                      P_ALERT_TEXT    OUT VARCHAR2);

  /***********************************************************************************************
           FUNCTION NAME: GET_NATIONALITY
           PURPOSE: This function is used to get patient nationality
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        07-MAY-2021  Salman (7236)           1. Created this PROCEDURE(CR:).
  ************************************************************************************************/
  FUNCTION GET_NATIONALITY(P_MRNO IN REGISTRATION.PATIENT.MRNO%TYPE)
    RETURN VARCHAR2;

  /***********************************************************************************************
           FUNCTION NAME: CPT_DOCUMENT_SETUP_EXIST
           PURPOSE: This function is used to return record of doucments attachment if exists in setup
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        26-APR-2021  Salman (7236)           1. Created this Function(CR:).
  ************************************************************************************************/
  FUNCTION CPT_DOCUMENT_SETUP_EXIST(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN VARCHAR2;

  /***********************************************************************************************
           FUNCTION NAME: IS_DOCUMENT_ATTACHED
           PURPOSE: This function is used to return record of doucments attached
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        27-APR-2021  Salman (7236)           1. Created this Function(CR:210000474)
  ************************************************************************************************/
  FUNCTION IS_DOCUMENT_ATTACHED(P_ORDER_TYPE_ID     IN ORDERENTRY.ORDER_CPT.ORDER_TYPE_ID%TYPE,
                                P_ORDER_NO          IN ORDERENTRY.ORDER_CPT.ORDER_NO%TYPE,
                                P_LOCATION_ID       IN ORDERENTRY.ORDER_CPT.LOCATION_ID %TYPE,
                                P_ORDER_LOCATION_ID IN ORDERENTRY.ORDER_CPT.ORDER_LOCATION_ID%TYPE,
                                P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE)
    RETURN LONG;

  /***********************************************************************************************
           FUNCTION NAME: IS_DOCUMENT_EXT_VALID
           PURPOSE: This function is used to return record of doucments attached
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        29-JUN-2021  Salman (7236)           1. Created this Function(CR:210000474)
  ************************************************************************************************/
  FUNCTION IS_DOCUMENT_EXT_VALID(P_PATH IN VARCHAR2) RETURN VARCHAR2;

  /***********************************************************************************************
           PROCEDURE NAME: DEL_NONATTACH_DOCS
           PURPOSE: This procedure is used to delete the rows when nationality is changed on WCCIS
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        02-JUL-2021  Salman (7236)           1. Created this Function(CR:210000474)
  ************************************************************************************************/
  PROCEDURE DEL_NONATTACH_DOCS(P_ORDER_TYPE_ID     IN VARCHAR2,
                               P_ORDER_NO          IN VARCHAR2,
                               P_LOCATION_ID       IN VARCHAR2,
                               P_ORDER_LOCATION_ID IN VARCHAR2);

  /***********************************************************************************************
           PROCEDURE NAME: ATTACH_AUTO_DOCS
           PURPOSE: This procedure is used to auto linked the rows if any attachment exists
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        14-SEP-2021  Salman (7236)           1. Created this Function(CR:210000474)
  ************************************************************************************************/
  PROCEDURE ATTACH_AUTO_DOCS(P_MRNO          IN REGISTRATION.PATIENT.MRNO%TYPE,
                             P_TABLE_NAME    IN HIS.DOCUMENT_ATTACHMENT.TABLE_NAME%TYPE,
                             P_REFERENCE_KEY IN HIS.DOCUMENT_ATTACHMENT.REFERENCE_KEY%TYPE,
                             P_OBJECT_CODE   IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE);

  /***********************************************************************************************
           FUNCTION NAME: IS_CPT_RESTRICTED
           PURPOSE: This function is used to check cpt restriction location wise
           ----------------------------------------------------------------------------------
           REVISIONS:
           Ver        Date         Author                  Description
           ---------  ----------   ---------------         -----------------------------------
           1.0        14-SEP-2021  Salman (7236)           1. Created this Function(CR:210000474)
  ************************************************************************************************/
  FUNCTION IS_CPT_RESTRICTED(P_CPT_ID IN ORDERENTRY.ORDER_CPT.CPT_ID%TYPE)
    RETURN VARCHAR2;
  /***********************************************************************************************
       FUNCTION NAME: IS_CPT_PRESCRIPTION_ATTACHED
       PURPOSE: This function is used to check prescription attached with cpt order master
       ---------------------------------------------------------------------------------------
       REVISIONS:
       Ver        Date          Author                   Description
       ---------  -----------   ---------------------    -------------------------------------
       1.0        12-AUG-2024   Muhammad Yasar Naseer    1. Created this Function(CR:240000748)
  ************************************************************************************************/
  FUNCTION IS_CPT_PRESCRIPTION_ATTACHED(P_ORDER_TYPE_ID     IN ORDERENTRY.ORDER_CPT.ORDER_TYPE_ID%TYPE,
                                        P_ORDER_NO          IN ORDERENTRY.ORDER_CPT.ORDER_NO%TYPE,
                                        P_LOCATION_ID       IN ORDERENTRY.ORDER_CPT.LOCATION_ID %TYPE,
                                        P_ORDER_LOCATION_ID IN ORDERENTRY.ORDER_CPT.ORDER_LOCATION_ID%TYPE,
                                        P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE)
    RETURN VARCHAR2;

  FUNCTION IS_ORDER_SIGNED_BY_DR(P_ORDER_TYPE_ID     IN ORDERENTRY.ORDER_CPT.ORDER_TYPE_ID%TYPE,
                                 P_ORDER_NO          IN ORDERENTRY.ORDER_CPT.ORDER_NO%TYPE,
                                 P_LOCATION_ID       IN ORDERENTRY.ORDER_CPT.LOCATION_ID %TYPE,
                                 P_ORDER_LOCATION_ID IN ORDERENTRY.ORDER_CPT.ORDER_LOCATION_ID%TYPE,
                                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE)
    RETURN VARCHAR2;

  FUNCTION IS_ORDER_INVOICED(P_ORDER_TYPE_ID     IN ORDERENTRY.ORDER_CPT.ORDER_TYPE_ID%TYPE,
                             P_ORDER_NO          IN ORDERENTRY.ORDER_CPT.ORDER_NO%TYPE,
                             P_LOCATION_ID       IN ORDERENTRY.ORDER_CPT.LOCATION_ID %TYPE,
                             P_ORDER_LOCATION_ID IN ORDERENTRY.ORDER_CPT.ORDER_LOCATION_ID%TYPE,
                             P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE)
    RETURN VARCHAR2;

  FUNCTION IS_PAT_TYPE_WISE_DOC_REQUIRED(P_PATIENT_TYPE_ID IN REGISTRATION.PATIENT.PATIENT_TYPE_ID%TYPE,
                                         P_CPT_ID          IN DEFINITIONS.CPT.CPT_ID%TYPE,
                                         P_OBJECT_CODE     IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                                         P_DOC_TYPE_ID     IN DEFINITIONS.CPT_WISE_PATIENT_TYPE_REST.DOC_TYPE_ID%TYPE)
    RETURN VARCHAR2;

END;
```

### DEFINITIONS.PKG_S01FRM00436
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00436 AS
  -- Author  : Syed Gohar Ali
  -- Purpose : This package uesd manage queues.
  --*****************************************************************************************--
  TYPE REC_MP IS RECORD(
    ZON_ID             MIS.PROCEDURES.ZON_ID%TYPE,
    ORGANIZATION_ID    MIS.PROCEDURES.ORGANIZATION%TYPE,
    ORGANIZATION       MIS.PROCEDURES.ORGANIZATION%TYPE,
    LOCATION_ID        MIS.PROCEDURES.LOCATION_ID%TYPE,
    LOCATION           MIS.PROCEDURES.LOCATION%TYPE,
    SUMMARY_DATE       DATE,
    NATURE_ID          MIS.PROCEDURES.NATURE_ID%TYPE,
    NATURE_DESC        MIS.PROCEDURES.NATURE_DESC%TYPE,
    NATURE_DETAIL_ID   MIS.PROCEDURES.NATURE_DETAIL_ID%TYPE,
    NATURE_DETAIL_DESC MIS.PROCEDURES.NATURE_DETAIL_DESC%TYPE,
    DEPARTMENT_ID      MIS.PROCEDURES.DEPARTMENT_ID%TYPE,
    DEPARTMENT         MIS.PROCEDURES.DEPARTMENT%TYPE,
    SECTION_ID         MIS.PROCEDURES.SECTION_ID%TYPE,
    SECTION            MIS.PROCEDURES.SECTION%TYPE,
    CPT_ID             MIS.PROCEDURES.CPT_ID%TYPE,
    CPT                MIS.PROCEDURES.CPT%TYPE,
    SUM_CPT_VALUE      MIS.PROCEDURES.SUM_CPT_VALUE%TYPE,
    COUNT_PROCEDURES   MIS.PROCEDURES.COUNT_PROCEDURES%TYPE,
    CLINIC_ID          MIS.PROCEDURES.CLINIC_ID%TYPE,
    CLINIC_NAME        MIS.PROCEDURES.CLINIC_NAME%TYPE,
    DOCTOR_ID          MIS.PROCEDURES.DOCTOR_ID%TYPE,
    DOCTOR_NAME        MIS.PROCEDURES.DOCTOR_NAME%TYPE,
    DOCTOR_MRNO        MIS.PROCEDURES.DOCTOR_MRNO%TYPE,
    ORDER_STATUS_ID    MIS.PROCEDURES.ORDER_STATUS_ID%TYPE,
    MRNO               MIS.PROCEDURES.MRNO%TYPE,
    ORDER_TYPE_ID      MIS.PROCEDURES.ORDER_TYPE_ID%TYPE,
    REPORT_TYPE        MIS.PROCEDURES.REPORT_TYPE%TYPE,
    ORDER_STATE        MIS.PROCEDURES.ORDER_STATE%TYPE,
    SR_NO              MIS.PROCEDURES.SR_NO%TYPE,
    RESULT_STATUS      MIS.PROCEDURES.RESULT_STATUS%TYPE,
    ORDER_STATUS       MIS.PROCEDURES.ORDER_STATUS%TYPE);

  TYPE CUR_MP IS REF CURSOR;-- RETURN REC_MP;
  TYPE TAB_MP IS TABLE OF REC_MP INDEX BY BINARY_INTEGER;
  --****************************************************************--
  PROCEDURE MP_QUERY(P_RECORD              IN OUT CUR_MP,
                     P_ZON_ID              IN VARCHAR2,
                     P_LOCATION_ID         IN VARCHAR2,
                     P_NATURE_ID           IN VARCHAR2,
                     P_NATURE_DETAIL_ID    IN VARCHAR2,
                     P_ORDER_STATUS        IN VARCHAR2,
                     P_FROM_DATE           IN VARCHAR2,
                     P_TO_DATE             IN VARCHAR2,
                     P_CPT_DESC            IN VARCHAR2,
                     P_CLINIC_NAME         IN VARCHAR2,
                     P_DOCTOR_NAME         IN VARCHAR2,
                     P_RESULT_STATUS       IN VARCHAR2,
                     P_ORDER_STATE         IN VARCHAR2,
                     P_REPORT_TYPE         IN VARCHAR2,
                     P_CALLING_LOCATION_ID IN VARCHAR2,
                     P_CALLING_OBJECT      IN VARCHAR2,
                     P_CALLING_USER        IN VARCHAR2,
                     P_CALLING_EVENT       IN VARCHAR2,
                     P_ERROR               OUT VARCHAR2);
  --****************************************************************--
  PROCEDURE MP_LOCK(P_RECORD              IN OUT TAB_MP,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2);
  --****************************************************************--
END PKG_S01FRM00436;
```

### DEFINITIONS.PKG_S01FRM00444
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00444 AS

  TYPE RG_PHYSICIAN_NOTES IS RECORD(
    MRNO             ORDERENTRY.PHYSICIAN_NOTES.MRNO%TYPE,
    NOTE_ID          ORDERENTRY.PHYSICIAN_NOTES.NOTE_ID%TYPE,
    REFERENCE_TABLE  VARCHAR2(100),
    EMR_CATEGORY     VARCHAR2(1),
    WRITTEN_BY       ORDERENTRY.PHYSICIAN_NOTES.WRITTEN_BY%TYPE,
    WRITTEN_BY_NAME  REGISTRATION.PATIENT.NAME%TYPE,
    NOTE_SIGNED_DATE DATE, --ORDERENTRY.PHYSICIAN_NOTES.SIGNED_DATE%TYPE,
    PROTECTED_NOTE   ORDERENTRY.PHYSICIAN_NOTES.PROTECTED_NOTE%TYPE,
    --NOTES            ORDERENTRY.PHYSICIAN_NOTES.NOTES%TYPE,
    RESTRICTION HIS.EMR_TRANSACTION_RSTRCT.ACTIVE%TYPE);

  TYPE REF_PHYSICIAN_NOTES IS REF CURSOR RETURN RG_PHYSICIAN_NOTES;
  TYPE TAB_PHYSICIAN_NOTES IS TABLE OF RG_PHYSICIAN_NOTES INDEX BY BINARY_INTEGER;

  /******************************************************************************************************
            PROCEDURE NAME: QUERY_PHYSICIAN_NOTES
            PURPOSE: This procedure is used to query PHYSICIAN NOTES
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        18-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/

  PROCEDURE QUERY_PHYSICIAN_NOTES(P_RESULT       IN OUT REF_PHYSICIAN_NOTES,
                                  P_FROM_DATE    IN DATE,
                                  P_TO_DATE      IN DATE,
                                  P_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                                  P_NOTE_TYPE_ID IN ORDERENTRY.PHYSICIAN_NOTE_TYPE.NOTE_TYPE_ID%TYPE);

  /******************************************************************************************************
            PROCEDURE NAME: UPD_EMR_TRANSACTION_RSTRCT
            PURPOSE: This procedure is used to update/insert EMR transaction restrct
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  PROCEDURE UPD_EMR_TRANS_RSTRCT_NOTES(P_RESULT          IN OUT TAB_PHYSICIAN_NOTES,
                                       P_MRNO            IN VARCHAR2,
                                       P_REFERENCE_KEY   IN VARCHAR2,
                                       P_REFERENCE_TABLE IN VARCHAR2,
                                       P_EMR_CATEGORY    IN VARCHAR2,
                                       P_ACTIVE          IN VARCHAR2);

  /******************************************************************************************************
            PROCEDURE NAME: UPD_EMR_TRANSACTION_RSTRCT
            PURPOSE: This procedure is used to update/insert EMR transaction restrct
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  PROCEDURE LCK_EMR_TRANS_RSTRCT_NOTES(P_RESULT          IN OUT TAB_PHYSICIAN_NOTES,
                                       P_MRNO            IN VARCHAR2,
                                       P_REFERENCE_KEY   IN VARCHAR2,
                                       P_REFERENCE_TABLE IN VARCHAR2,
                                       P_EMR_CATEGORY    IN VARCHAR2,
                                       P_ACTIVE          IN VARCHAR2);

  /******************************************************************************************************
            FUNCTION NAME: QRY_NOTES
            PURPOSE: This function is used to get notes
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  FUNCTION GET_NOTES(P_NOTE_ID IN ORDERENTRY.PHYSICIAN_NOTES.NOTE_ID%TYPE)
    RETURN ORDERENTRY.PHYSICIAN_NOTES.NOTES%TYPE;

  /******************************************************************************************************
            FUNCTION NAME: GET_ROLE_DESC
            PURPOSE: This function is used to get role desc
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  FUNCTION GET_ROLE_DESC(P_ROLE_ID IN SECURITY.ROLE.ROLE_ID%TYPE)
    RETURN SECURITY.ROLE.DESCRIPTION%TYPE;

  /******************************************************************************************************
            FUNCTION NAME: QUERY_CPT
            PURPOSE: This function is used to get CPT
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/

  TYPE RG_ORDER_CPT IS RECORD(
    MRNO            ORDERENTRY.PHYSICIAN_NOTES.MRNO%TYPE,
    ORDER_DATE      DATE,
    REFERENCE_KEY   VARCHAR2(100),
    REFERENCE_TABLE VARCHAR2(100),
    CPT_DESC        DEFINITIONS.CPT.DESCRIPTION%TYPE,
    EMR_CATEGORY    VARCHAR2(1),
    RESTRICTION     HIS.EMR_TRANSACTION_RSTRCT.ACTIVE%TYPE);

  TYPE REF_ORDER_CPT IS REF CURSOR RETURN RG_ORDER_CPT;
  TYPE TAB_ORDER_CPT IS TABLE OF RG_ORDER_CPT INDEX BY BINARY_INTEGER;

  PROCEDURE QUERY_CPT(P_RESULT    IN OUT REF_ORDER_CPT,
                      P_FROM_DATE IN DATE,
                      P_TO_DATE   IN DATE,
                      P_MRNO      IN REGISTRATION.PATIENT.MRNO%TYPE);

  /******************************************************************************************************
            PROCEDURE NAME: UPD_EMR_TRANS_RSTRCT_CPT
            PURPOSE: This procedure is used to update/insert EMR transaction restrct
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  PROCEDURE UPD_EMR_TRANS_RSTRCT_CPT(P_RESULT          IN OUT TAB_ORDER_CPT,
                                     P_MRNO            IN VARCHAR2,
                                     P_REFERENCE_KEY   IN VARCHAR2,
                                     P_REFERENCE_TABLE IN VARCHAR2,
                                     P_EMR_CATEGORY    IN VARCHAR2,
                                     P_ACTIVE          IN VARCHAR2);

  /******************************************************************************************************
            PROCEDURE NAME: LCK_EMR_TRANS_RSTRCT_CPT
            PURPOSE: This procedure is used to update/insert EMR transaction restrct
            --------------------------------------------------------------------------------------
            REVISIONS:
            Ver        Date         Author                 Description
            ---------  ----------   ---------------        ---------------------------------------
            1.0        19-MAY-2019  Salman(6-7236)         1. Created this Procedure CR: ???
  *******************************************************************************************************/
  PROCEDURE LCK_EMR_TRANS_RSTRCT_CPT(P_RESULT          IN OUT TAB_ORDER_CPT,
                                     P_MRNO            IN VARCHAR2,
                                     P_REFERENCE_KEY   IN VARCHAR2,
                                     P_REFERENCE_TABLE IN VARCHAR2,
                                     P_EMR_CATEGORY    IN VARCHAR2,
                                     P_ACTIVE          IN VARCHAR2);

END PKG_S01FRM00444;
```

### DEFINITIONS.PKG_S01FRM00462
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00462 IS


  TYPE CPT_SPECIALITY_REC IS RECORD(
    CPT_ID                   DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,                                        
    CLINIC_SPECIALITY_ID     DEFINITIONS.CPT_SPECIALTIES.CLINIC_SPECIALITY_ID%TYPE,
    CLINIC_SPECIALITY_DESC   DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
    ACTIVE                   DEFINITIONS.CPT_SPECIALTIES.ACTIVE%TYPE,
    REMARKS                   DEFINITIONS.CPT_SPECIALTIES.REMARKS%TYPE);

  TYPE CPT_SPECIALITY_TBL IS TABLE OF CPT_SPECIALITY_REC INDEX BY PLS_INTEGER;

  TYPE CPT_SPECIALITY_TBL_PF IS TABLE OF CPT_SPECIALITY_REC; -- INDEX BY PLS_INTEGER;
  
  FUNCTION F_CPT_SPECIALITY_QRY(P_CPT_ID     IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE)
    RETURN CPT_SPECIALITY_TBL_PF
    PIPELINED;

  -------------------------------------------------------------------------------------------------------
  PROCEDURE P_CPT_SPECIALITY_QRY(P_RESULT         IN OUT CPT_SPECIALITY_TBL,
                           P_CPT_ID     IN DEFINITIONS.CPT_SPECIALTIES.CPT_ID%TYPE,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2);

  -------------------------------------------------------------------------------------------------------
  PROCEDURE P_CPT_SPECIALITY_INS(P_RESULT         IN OUT CPT_SPECIALITY_TBL,
    
                           P_LOCATION_ID    IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2);

  -------------------------------------------------------------------------------------------------------
  PROCEDURE P_CPT_SPECIALITY_UPD(P_RESULT         IN OUT CPT_SPECIALITY_TBL,
                           P_LOCATION_ID    IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2);

  -------------------------------------------------------------------------------------------------------
  PROCEDURE P_CPT_SPECIALITY_DEL(P_RESULT         IN OUT CPT_SPECIALITY_TBL,
                           P_LOCATION_ID    IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2);

  -------------------------------------------------------------------------------------------------------
  PROCEDURE P_CPT_SPECIALITY_LCK(P_RESULT         IN CPT_SPECIALITY_TBL,
                           P_LOCATION_ID    IN VARCHAR2,
                           P_CALLING_OBJECT IN VARCHAR2,
                           P_CALLING_USER   IN VARCHAR2,
                           P_CALLING_EVENT  IN VARCHAR2,
                           P_ERROR          OUT VARCHAR2);

TYPE LOV_CPT_SPECIALITY_REC IS RECORD(
SPECIALTY                      DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
CLINIC_SPECIALITY_ID           DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE
);

  TYPE LOV_CPT_SPECIALITY_TAB IS TABLE OF LOV_CPT_SPECIALITY_REC;

-- ADDED BY ZAFAR IQBAL 10014 DATED : 04-MAY-2021 AGAINST TASK ID 210000411
FUNCTION F_GET_CPT_SPECIALITY_LOV(
  P_NATURE_ID    IN VARCHAR2,
  P_CPT_ID       IN VARCHAR2,
  P_USER_MRNO   IN VARCHAR2,
                       P_LOC_ID      IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                       P_ORG_ID      IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                       P_OBJECT_CODE IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                       P_EVENT       IN VARCHAR2) RETURN LOV_CPT_SPECIALITY_TAB
    PIPELINED;
---------
FUNCTION F_GET_CLINIC_SPEC_DESC(P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE)
  RETURN DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE;

END PKG_S01FRM00462;
```

### DEFINITIONS.PKG_S01FRM00472
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00472 IS

  /***********************************************************************************************
         OBJECTIVE := This package will be used for Fixed Asset Depreciation
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        14-Dec-2021   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------
  -- record group --
  ------------------
  TYPE CPT_REC IS RECORD(
    PROPOSAL_ID        DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    DESCRIPTION        DEFINITIONS.CPT_PROPOSAL.DESCRIPTION%TYPE,
    TRN_TYPE           DEFINITIONS.CPT_PROPOSAL.TRN_TYPE%TYPE,
    NATURE_ID          DEFINITIONS.CPT_PROPOSAL.NATURE_ID%TYPE,
    NATURE_DESC        DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
    NATURE_DETAIL_ID   DEFINITIONS.CPT_PROPOSAL.NATURE_DETAIL_ID%TYPE,
    NATURE_DETAIL_DESC DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    EFFECTIVE_FROM     DEFINITIONS.CPT_PROPOSAL.EFFECTIVE_FROM%TYPE,
    STATUS_ID          DEFINITIONS.CPT_PROPOSAL.STATUS_ID%TYPE,
    STATUS_DESC        VARCHAR2(250),
    PROPOSAL_DATE      DEFINITIONS.CPT_PROPOSAL.PROPOSAL_DATE%TYPE,
    WFE_NO             DEFINITIONS.CPT_PROPOSAL.WFE_NO%TYPE,
    WF_STATUS          VARCHAR2(250),
    ADD_ANES_FEE       DEFINITIONS.CPT_PROPOSAL.ADD_ANES_FEE%TYPE,
    ADD_HOSPITAL_SHARE DEFINITIONS.CPT_PROPOSAL.ADD_HOSPITAL_SHARE%TYPE,
    ADD_COMMISSION     DEFINITIONS.CPT_PROPOSAL.ADD_COMMISSION%TYPE,
    EVENT_ID           DEFINITIONS.EVENT.EVENT_ID%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  ----------------------------------
  -- plsql table for CPT question --
  ----------------------------------
  TYPE CPT_TAB IS TABLE OF CPT_REC INDEX BY BINARY_INTEGER;

  --------------------------------------------
  -- This procedure will query CPT_PROPOSAL --
  --------------------------------------------
  PROCEDURE QUERY_CPT_PROPOSAL(P_RESULT      IN OUT CPT_REF,
                               P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_DESCRIPTION IN DEFINITIONS.CPT_PROPOSAL.DESCRIPTION%TYPE);

  ---------------------------------------------
  -- This procedure will insert CPT_PROPOSAL --
  ---------------------------------------------
  PROCEDURE INSERT_CPT_PROPOSAL(P_BLOCK_DATA IN OUT CPT_TAB);

  ---------------------------------------------
  -- This procedure will update CPT_PROPOSAL --
  ---------------------------------------------
  PROCEDURE UPDATE_CPT_PROPOSAL(P_BLOCK_DATA IN OUT CPT_TAB);

  ---------------------------------------------
  -- This procedure will delete CPT_PROPOSAL --
  ---------------------------------------------
  PROCEDURE DELETE_CPT_PROPOSAL(P_BLOCK_DATA IN OUT CPT_TAB);

  -------------------------------------------
  -- This procedure will lock CPT_PROPOSAL --
  -------------------------------------------
  PROCEDURE LOCK_CPT_PROPOSAL(P_BLOCK_DATA IN OUT CPT_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE CPT_DT_REC IS RECORD(
    PROPOSAL_ID   DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    
    CPT_ID             DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    PRICE_HIST_SRNO    DEFINITIONS.CPT_PROP_DTL.PRICE_HIST_SRNO%TYPE,
    CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    REALISED_PRICE     DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE,
    REALISED_PRICE_P   DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE,
    SELECT_FLAG        DEFINITIONS.CPT_PROP_DTL.SELECT_FLAG%TYPE,
    LAST_PROPOSAL_ID   DEFINITIONS.CPT_PROP_DTL.PROPOSAL_ID%TYPE,
    LAST_PROPOSAL_SRNO DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_DT_REF IS REF CURSOR RETURN CPT_DT_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE CPT_DT_TAB IS TABLE OF CPT_DT_REC INDEX BY BINARY_INTEGER;

  -------------------------------------------
  -- This procedure will query CPT_PROP_DT --
  -------------------------------------------
  PROCEDURE QUERY_CPT_DT(P_RESULT      IN OUT CPT_DT_REF,
                         P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                         P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                         P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE);

  --------------------------------------------
  -- This procedure will insert CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE INSERT_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  --------------------------------------------
  -- This procedure will update CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE UPDATE_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  --------------------------------------------
  -- This procedure will delete CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE DELETE_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  ------------------------------------------
  -- This procedure will lock CPT_PROP_DT --
  ------------------------------------------
  PROCEDURE LOCK_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  --------------------------------------------------
  -- This procedure will be used to populate cpts --
  --------------------------------------------------
  PROCEDURE POPULATE_CPT(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                         P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                         P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                         P_NATURE_ID         IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                         P_NATURE_DETAIL_ID  IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                         P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                         P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                         P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                         P_ALERT_TEXT        OUT VARCHAR2,
                         P_STOP              OUT VARCHAR2);
  PROCEDURE REVISE_CPT_MT_COST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                               P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                               P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_NATURE_ID         IN DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                               P_NATURE_DETAIL_ID  IN DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_ID%TYPE,
                               P_FIN_SETUP_ID      IN DEFINITIONS.CPT_MT_SETUP.MATERIAL_SETUP_ID%TYPE,
                               P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                               P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                               P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                               P_ALERT_TEXT        OUT VARCHAR2,
                               P_STOP              OUT VARCHAR2);
  PROCEDURE SIGN(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                 P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                 P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                 P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                 P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                 P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                 P_ALERT_TEXT        OUT VARCHAR2,
                 P_STOP              OUT VARCHAR2);
  PROCEDURE CANCEL(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                   P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                   P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                   P_OBJECT_CODE       IN DEFINITIONS.OBJECTS.OBJECT_CODE%TYPE,
                   P_USER_MRNO         IN REGISTRATION.PATIENT.MRNO%TYPE,
                   P_TERMINAL          IN DEFINITIONS.TERMINALS.NAME%TYPE,
                   P_ALERT_TEXT        OUT VARCHAR2,
                   P_STOP              OUT VARCHAR2);

END PKG_S01FRM00472;
```

### DEFINITIONS.PKG_S01FRM00473
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01FRM00473 IS

  /***********************************************************************************************
         OBJECTIVE := This package will be used for Fixed Asset Depreciation
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        14-Dec-2021   Muhammad Ali Khubaib   1. Created this Package.
  ************************************************************************************************/
  -----------------------------------------------------------
  -- This Function will return the Version of this Package --
  -----------------------------------------------------------
  FUNCTION GET_VERSION RETURN VARCHAR2;

  ------------------
  -- record group --
  ------------------
  TYPE CPT_REC IS RECORD(
    PROPOSAL_ID        DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    DESCRIPTION        DEFINITIONS.CPT_PROPOSAL.DESCRIPTION%TYPE,
    TRN_TYPE           DEFINITIONS.CPT_PROPOSAL.TRN_TYPE%TYPE,
    NATURE_ID          DEFINITIONS.CPT_PROPOSAL.NATURE_ID%TYPE,
    NATURE_DESC        DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
    NATURE_DETAIL_ID   DEFINITIONS.CPT_PROPOSAL.NATURE_DETAIL_ID%TYPE,
    NATURE_DETAIL_DESC DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    EFFECTIVE_FROM     DEFINITIONS.CPT_PROPOSAL.EFFECTIVE_FROM%TYPE,
    STATUS_ID          DEFINITIONS.CPT_PROPOSAL.STATUS_ID%TYPE,
    STATUS_DESC        VARCHAR2(500),
    PROPOSAL_DATE      DEFINITIONS.CPT_PROPOSAL.PROPOSAL_DATE%TYPE,
    SCHEMA_ID          DEFINITIONS.CPT_PROP_WORKFLOW.SCHEMA_ID%TYPE,
    WORKFLOW_TYPE_ID   DEFINITIONS.CPT_PROP_WORKFLOW.WORKFLOW_TYPE_ID%TYPE,
    WORK_FLOW_ID       DEFINITIONS.CPT_PROP_WORKFLOW.WORK_FLOW_ID%TYPE,
    EVENT_ID           DEFINITIONS.CPT_PROP_WORKFLOW.EVENT_ID%TYPE,
    ADD_ANES_FEE       DEFINITIONS.CPT_PROPOSAL.ADD_ANES_FEE%TYPE,
    ADD_HOSPITAL_SHARE DEFINITIONS.CPT_PROPOSAL.ADD_HOSPITAL_SHARE%TYPE,
    ADD_COMMISSION     DEFINITIONS.CPT_PROPOSAL.ADD_COMMISSION%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_REF IS REF CURSOR RETURN CPT_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE CPT_TAB IS TABLE OF CPT_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_CPT_PROPOSAL_TAB_APEX IS TABLE OF CPT_REC;

  --------------------------------------------
  -- This procedure will query CPT_PROPOSAL --
  --------------------------------------------
  PROCEDURE QUERY_CPT_PROPOSAL(P_RESULT      IN OUT CPT_REF,
                               P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_DESCRIPTION IN DEFINITIONS.CPT_PROPOSAL.DESCRIPTION%TYPE);

  ------------------------------------------------------
  -- Table function used to query Report Master --
  ------------------------------------------------------
  FUNCTION QUERY_CPT_PROPOSAL_APEX(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                   P_DESCRIPTION IN DEFINITIONS.CPT_PROPOSAL.DESCRIPTION%TYPE)
    RETURN QUERY_CPT_PROPOSAL_TAB_APEX
    PIPELINED;
  ------------------
  -- record group --
  ------------------
  TYPE CPT_DT_REC IS RECORD(
    PROPOSAL_ID           DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO         DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    CPT_ID                DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    PRICE_HIST_SRNO       DEFINITIONS.CPT_PROP_DTL.PRICE_HIST_SRNO%TYPE,
    CPT_DESCRIPTION       DEFINITIONS.CPT.DESCRIPTION%TYPE,
    MATERIAL              DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    MANPOWER              DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    OVERHEAD              DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    DEPRECIATION          DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    PROFIT_LOSS           DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    COST_WO_DR            DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    DR_FEE                DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    ANES_FEE              DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    HOSPITAL_SHARE        DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    SELLING_PRICE         DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    COMMISION             DEFINITIONS.CPT_PROP_DTL.COMMISION%TYPE,
    REALISED_PRICE        DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE,
    EFFECTIVE_FROM        DEFINITIONS.CPT_PROP_DTL.EFFECTIVE_FROM%TYPE,
    LAST_PROPOSAL_ID      DEFINITIONS.CPT_PROP_DTL.PROPOSAL_ID%TYPE,
    LAST_PROPOSAL_SRNO    DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    FINALIZED             DEFINITIONS.CPT_PROP_DTL.FINALIZED%TYPE,
    SELECT_FLAG           DEFINITIONS.CPT_PROP_DTL.SELECT_FLAG%TYPE,
    F_CPT_DESCRIPTION     DEFINITIONS.CPT.DESCRIPTION%TYPE,
    F_PREV_COST_WO_DR     DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    F_PREV_DR_FEE         DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    F_PREV_ANES_FEE       DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    F_PREV_HOSPITAL_SHARE DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    F_PREV_SELLING_PRICE  DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    F_PREV_COMMISION      DEFINITIONS.CPT_PROP_DTL.COMMISION%TYPE,
    F_COST_WO_DR          DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    F_DR_FEE              DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    F_ANES_FEE            DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    F_HOSPITAL_SHARE      DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    F_SELLING_PRICE       DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    F_COMMISION           DEFINITIONS.CPT_PROP_DTL.COMMISION%TYPE,
    F_REALISED_PRICE      DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE,
    A_CPT_ID              DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    A_CPT_DESCRIPTION     DEFINITIONS.CPT.DESCRIPTION%TYPE,
    A_NATURE_DETAIL_ID    DEFINITIONS.CPT_PROPOSAL.NATURE_DETAIL_ID%TYPE,
    A_NATURE_DETAIL_DESC  DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    A_SELLING_PRICE       DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    A_POSTED              DEFINITIONS.CPT_PROP_DTL.POSTED%TYPE,
    F_PREV_REALISED_PRICE DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_DT_REF IS REF CURSOR RETURN CPT_DT_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE CPT_DT_TAB IS TABLE OF CPT_DT_REC INDEX BY BINARY_INTEGER;

  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_CPT_DT_TAB_APEX IS TABLE OF CPT_DT_REC;

  -------------------------------------------
  -- This procedure will query CPT_PROP_DT --
  -------------------------------------------
  PROCEDURE QUERY_CPT_DT(P_RESULT      IN OUT CPT_DT_REF,
                         P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                         P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                         P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ------------------------------------------------------
  -- Table function used to query CPT_PROP_DT --
  ------------------------------------------------------
  FUNCTION QUERY_CPT_DT_APEX(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                             P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE)
    RETURN QUERY_CPT_DT_TAB_APEX
    PIPELINED;

  --------------------------------------------
  -- This procedure will update CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE UPDATE_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  --------------------------------------------
  -- This procedure will delete CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE DELETE_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  ------------------------------------------
  -- This procedure will lock CPT_PROP_DT --
  ------------------------------------------
  PROCEDURE LOCK_CPT_DT(P_BLOCK_DATA IN OUT CPT_DT_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE CPT_DT_ACTIVATION_REC IS RECORD(
    PROPOSAL_ID          DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO        DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    CPT_ID               DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    CPT_DESCRIPTION      DEFINITIONS.CPT.DESCRIPTION%TYPE,
    A_CPT_ID             DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    A_CPT_DESCRIPTION    DEFINITIONS.CPT.DESCRIPTION%TYPE,
    A_NATURE_DETAIL_ID   DEFINITIONS.CPT_PROPOSAL.NATURE_DETAIL_ID%TYPE,
    A_NATURE_DETAIL_DESC DEFINITIONS.DEPARTMENT_NATURE_DETAIL.NATURE_DETAIL_DESC%TYPE,
    EFFECTIVE_FROM       DEFINITIONS.CPT_PROP_DTL.EFFECTIVE_FROM%TYPE,
    A_SELLING_PRICE      DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    A_POSTED             DEFINITIONS.CPT_PROP_DTL.POSTED%TYPE);
  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_DT_ACTIVATION_REF IS REF CURSOR RETURN CPT_DT_ACTIVATION_REC;
  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE CPT_DT_ACTIVATION_TAB IS TABLE OF CPT_DT_ACTIVATION_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_CPT_DT_ACTIVATION_TAB_APEX IS TABLE OF CPT_DT_ACTIVATION_REC;

  -------------------------------------------
  -- This procedure will query CPT_PROP_DT --
  -------------------------------------------
  PROCEDURE QUERY_CPT_DT_ACTIVATION(P_RESULT      IN OUT CPT_DT_ACTIVATION_REF,
                                    P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                    P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                                    P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ------------------------------------------------------
  -- Table function used to query CPT_PROP_DT --
  ------------------------------------------------------
  FUNCTION QUERY_CPT_DT_ACTIVATION_APEX(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                        P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                                        P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE)
    RETURN QUERY_CPT_DT_ACTIVATION_TAB_APEX
    PIPELINED;

  --------------------------------------------
  -- This procedure will update CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE UPDATE_CPT_DT_ACTIVATION(P_BLOCK_DATA IN OUT CPT_DT_ACTIVATION_TAB);

  --------------------------------------------
  -- This procedure will delete CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE DELETE_CPT_DT_ACTIVATION(P_BLOCK_DATA IN OUT CPT_DT_ACTIVATION_TAB);

  ------------------------------------------
  -- This procedure will lock CPT_PROP_DT --
  ------------------------------------------
  PROCEDURE LOCK_CPT_DT_ACTIVATION(P_BLOCK_DATA IN OUT CPT_DT_ACTIVATION_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE CPT_DT_FINAL_SHEET_REC IS RECORD(
    PROPOSAL_ID           DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO         DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    CPT_ID                DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
    CPT_DESCRIPTION       DEFINITIONS.CPT.DESCRIPTION%TYPE,
    F_CPT_DESCRIPTION     DEFINITIONS.CPT.DESCRIPTION%TYPE,
    F_PREV_COST_WO_DR     DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    F_PREV_DR_FEE         DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    F_PREV_ANES_FEE       DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    F_PREV_HOSPITAL_SHARE DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    F_PREV_SELLING_PRICE  DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    F_PREV_COMMISION      DEFINITIONS.CPT_PROP_DTL.COMMISION%TYPE,
    F_COST_WO_DR          DEFINITIONS.CPT_PROP_DTL.COST_WO_DR%TYPE,
    F_DR_FEE              DEFINITIONS.CPT_PROP_DTL.DR_FEE%TYPE,
    F_ANES_FEE            DEFINITIONS.CPT_PROP_DTL.ANES_FEE%TYPE,
    F_HOSPITAL_SHARE      DEFINITIONS.CPT_PROP_DTL.HOSPITAL_SHARE%TYPE,
    F_SELLING_PRICE       DEFINITIONS.CPT_PROP_DTL.SELLING_PRICE%TYPE,
    F_COMMISION           DEFINITIONS.CPT_PROP_DTL.COMMISION%TYPE,
    F_REALISED_PRICE      DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE,
    F_PREV_REALISED_PRICE DEFINITIONS.CPT_PROP_DTL.REALISED_PRICE%TYPE);
  ----------------
  -- ref cursor --
  ----------------
  TYPE CPT_DT_FINAL_SHEET_REF IS REF CURSOR RETURN CPT_DT_FINAL_SHEET_REC;
  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE CPT_DT_FINAL_SHEET_TAB IS TABLE OF CPT_DT_FINAL_SHEET_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_CPT_DT_FINAL_SHEET_TAB_APEX IS TABLE OF CPT_DT_FINAL_SHEET_REC;

  -------------------------------------------
  -- This procedure will query CPT_PROP_DT --
  -------------------------------------------
  PROCEDURE QUERY_CPT_DT_FINAL_SHEET(P_RESULT      IN OUT CPT_DT_FINAL_SHEET_REF,
                                     P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                     P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                                     P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE);

  ------------------------------------------------------
  -- Table function used to query CPT_PROP_DT --
  ------------------------------------------------------
  FUNCTION QUERY_CPT_DT_FINAL_SHEET_APEX(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                         P_CPT_ID      IN DEFINITIONS.CPT_PROP_DTL.CPT_ID%TYPE,
                                         P_CPT_DESC    IN DEFINITIONS.CPT.DESCRIPTION%TYPE)
    RETURN QUERY_CPT_DT_FINAL_SHEET_TAB_APEX
    PIPELINED;

  --------------------------------------------
  -- This procedure will update CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE UPDATE_CPT_DT_FINAL_SHEET(P_BLOCK_DATA IN OUT CPT_DT_FINAL_SHEET_TAB);

  --------------------------------------------
  -- This procedure will delete CPT_PROP_DT --
  --------------------------------------------
  PROCEDURE DELETE_CPT_DT_FINAL_SHEET(P_BLOCK_DATA IN OUT CPT_DT_FINAL_SHEET_TAB);

  ------------------------------------------
  -- This procedure will lock CPT_PROP_DT --
  ------------------------------------------
  PROCEDURE LOCK_CPT_DT_FINAL_SHEET(P_BLOCK_DATA IN OUT CPT_DT_FINAL_SHEET_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE MANPOWER_REC IS RECORD(
    PROPOSAL_ID        DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO      DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    DESIGNATION_ID     DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION        DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    TOTAL_TIME         DEFINITIONS.CPT_PROP_DTL_MANPOWER.TOTAL_TIME%TYPE,
    NO_OF_TESTS        DEFINITIONS.CPT_PROP_DTL_MANPOWER.NO_OF_TESTS%TYPE,
    TIME_CONSUMED_PREV DEFINITIONS.CPT_PROP_DTL_MANPOWER.TIME_CONSUMED_PER_TEST%TYPE,
    TIME_CONSUMED      DEFINITIONS.CPT_PROP_DTL_MANPOWER.TIME_CONSUMED_PER_TEST%TYPE,
    PAYROLL_COST_PREV  DEFINITIONS.CPT_PROP_DTL_MANPOWER.PAYROLL_COST%TYPE,
    PAYROLL_COST       DEFINITIONS.CPT_PROP_DTL_MANPOWER.PAYROLL_COST%TYPE,
    TOTAL_COST_PREV    DEFINITIONS.CPT_PROP_DTL_MANPOWER.TOTAL_COST_PREV%TYPE,
    TOTAL_COST         DEFINITIONS.CPT_PROP_DTL_MANPOWER.TOTAL_COST%TYPE,
    DESIGNATION_ID_1   DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION_1      DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DESIGNATION_ID_2   DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION_2      DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DESIGNATION_ID_3   DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION_3      DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DESIGNATION_ID_4   DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION_4      DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE,
    DESIGNATION_ID_5   DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
    DESIGNATION_5      DEFINITIONS.DESIGNATION.DESCRIPTION%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE MANPOWER_REF IS REF CURSOR RETURN MANPOWER_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE MANPOWER_TAB IS TABLE OF MANPOWER_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_MANPOWER_TAB_APEX IS TABLE OF MANPOWER_REC;

  ----------------------------------------
  -- This procedure will query MANPOWER --
  ----------------------------------------
  PROCEDURE QUERY_MANPOWER(P_RESULT        IN OUT MANPOWER_REF,
                           P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);
  ------------------------------------------------------
  -- Table function used to query Marerial --
  ------------------------------------------------------
  FUNCTION QUERY_MANPOWER_APEX(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN QUERY_MANPOWER_TAB_APEX
    PIPELINED;
  -----------------------------------------
  -- This procedure will insert MANPOWER --
  -----------------------------------------
  PROCEDURE INSERT_MANPOWER(P_BLOCK_DATA IN OUT MANPOWER_TAB);

  -----------------------------------------
  -- This procedure will update MANPOWER --
  -----------------------------------------
  PROCEDURE UPDATE_MANPOWER(P_BLOCK_DATA IN OUT MANPOWER_TAB);

  -----------------------------------------
  -- This procedure will delete MANPOWER --
  -----------------------------------------
  PROCEDURE DELETE_MANPOWER(P_BLOCK_DATA IN OUT MANPOWER_TAB);

  ---------------------------------------
  -- This procedure will lock MANPOWER --
  ---------------------------------------
  PROCEDURE LOCK_MANPOWER(P_BLOCK_DATA IN OUT MANPOWER_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE MATERIAL_REC IS RECORD(
    PROPOSAL_ID     DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO   DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    ITEM_ID         DEFINITIONS.CPT_PROP_DTL_MATERIAL.ITEM_ID%TYPE,
    ITEM_DESC       ITEM.ITEM.DESCRIPTION%TYPE,
    ITEM_TYPE       DEFINITIONS.CPT_PROP_DTL_MATERIAL.ITEM_TYPE%TYPE,
    ITEM_TYPE_DESC  VARCHAR2(500),
    PACK_SIZE       DEFINITIONS.CPT_PROP_DTL_MATERIAL.PACK_SIZE%TYPE,
    EFFECTIVE_SIZE  DEFINITIONS.CPT_PROP_DTL_MATERIAL.EFFECTIVE_SIZE%TYPE,
    TOTAL_COST_PREV DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST_PREV%TYPE,
    UNIT_COST_PREV  DEFINITIONS.CPT_PROP_DTL_MATERIAL.UNIT_COST%TYPE,
    UNIT_COST       DEFINITIONS.CPT_PROP_DTL_MATERIAL.UNIT_COST%TYPE,
    QUANTITY_PREV   DEFINITIONS.CPT_PROP_DTL_MATERIAL.QUANTITY%TYPE,
    QUANTITY        DEFINITIONS.CPT_PROP_DTL_MATERIAL.QUANTITY%TYPE,
    TOTAL_COST      DEFINITIONS.CPT_PROP_DTL_MATERIAL.TOTAL_COST%TYPE,
    PACK_PRICE      DEFINITIONS.CPT_PROP_DTL_MATERIAL.PACK_PRICE%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE MATERIAL_REF IS REF CURSOR RETURN MATERIAL_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE MATERIAL_TAB IS TABLE OF MATERIAL_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_MATERIAL_TAB_APEX IS TABLE OF MATERIAL_REC;
  ----------------------------------------
  -- This procedure will query MATERIAL --
  ----------------------------------------
  PROCEDURE QUERY_MATERIAL(P_RESULT        IN OUT MATERIAL_REF,
                           P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);

  ------------------------------------------------------
  -- Table function used to query Marerial --
  ------------------------------------------------------
  FUNCTION QUERY_MATERIAL_APEX(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN QUERY_MATERIAL_TAB_APEX
    PIPELINED;

  -----------------------------------------
  -- This procedure will insert MATERIAL --
  -----------------------------------------
  PROCEDURE INSERT_MATERIAL(P_BLOCK_DATA IN OUT MATERIAL_TAB);

  -----------------------------------------
  -- This procedure will update MATERIAL --
  -----------------------------------------
  PROCEDURE UPDATE_MATERIAL(P_BLOCK_DATA IN OUT MATERIAL_TAB);

  -----------------------------------------
  -- This procedure will delete MATERIAL --
  -----------------------------------------
  PROCEDURE DELETE_MATERIAL(P_BLOCK_DATA IN OUT MATERIAL_TAB);

  ---------------------------------------
  -- This procedure will lock MATERIAL --
  ---------------------------------------
  PROCEDURE LOCK_MATERIAL(P_BLOCK_DATA IN OUT MATERIAL_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE OVERHEAD_REC IS RECORD(
    PROPOSAL_ID     DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO   DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    TOT_DIRECT_COST DEFINITIONS.CPT_PROP_DTL_OVERHEAD.TOTAL_COST%TYPE,
    OVERHEAD_RATIO  DEFINITIONS.CPT_PROP_DTL_OVERHEAD.OVERHEAD_RATIO%TYPE,
    TOTAL_COST_PREV DEFINITIONS.CPT_PROP_DTL_OVERHEAD.TOTAL_COST_PREV%TYPE,
    TOTAL_COST      DEFINITIONS.CPT_PROP_DTL_OVERHEAD.TOTAL_COST%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE OVERHEAD_REF IS REF CURSOR RETURN OVERHEAD_REC;

  -------------------------------------
  -- plsql table for CPT question --
  -------------------------------------
  TYPE OVERHEAD_TAB IS TABLE OF OVERHEAD_REC INDEX BY BINARY_INTEGER;

  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_OVERHEAD_TAB_APEX IS TABLE OF OVERHEAD_REC;

  ----------------------------------------
  -- This procedure will query OVERHEAD --
  ----------------------------------------
  PROCEDURE QUERY_OVERHEAD(P_RESULT        IN OUT OVERHEAD_REF,
                           P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);
  ------------------------------------------------------
  -- Table function used to query Overhead --
  ------------------------------------------------------
  FUNCTION QUERY_OVERHEAD_APEX(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN QUERY_OVERHEAD_TAB_APEX
    PIPELINED;
  -----------------------------------------
  -- This procedure will insert OVERHEAD --
  -----------------------------------------
  PROCEDURE INSERT_OVERHEAD(P_BLOCK_DATA IN OUT OVERHEAD_TAB);

  -----------------------------------------
  -- This procedure will update OVERHEAD --
  -----------------------------------------
  PROCEDURE UPDATE_OVERHEAD(P_BLOCK_DATA IN OUT OVERHEAD_TAB);

  -----------------------------------------
  -- This procedure will delete OVERHEAD --
  -----------------------------------------
  PROCEDURE DELETE_OVERHEAD(P_BLOCK_DATA IN OUT OVERHEAD_TAB);

  ---------------------------------------
  -- This procedure will lock OVERHEAD --
  ---------------------------------------
  PROCEDURE LOCK_OVERHEAD(P_BLOCK_DATA IN OUT OVERHEAD_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE DEPRECIATION_REC IS RECORD(
    PROPOSAL_ID       DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO     DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
    DIRECT_MATERIAL   DEFINITIONS.CPT_PROP_DTL_DEPR.TOTAL_COST%TYPE,
    PAYROLL           DEFINITIONS.CPT_PROP_DTL_DEPR.TOTAL_COST%TYPE,
    TOTAL_DIRECT_COST DEFINITIONS.CPT_PROP_DTL_DEPR.TOTAL_COST%TYPE,
    TOTAL_COST_PREV   DEFINITIONS.CPT_PROP_DTL_DEPR.TOTAL_COST_PREV%TYPE,
    TOTAL_COST        DEFINITIONS.CPT_PROP_DTL_DEPR.TOTAL_COST%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE DEPRECIATION_REF IS REF CURSOR RETURN DEPRECIATION_REC;

  ----------------------------------
  -- plsql table for CPT question --
  ----------------------------------
  TYPE DEPRECIATION_TAB IS TABLE OF DEPRECIATION_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_DEPRECIATION_TAB_APEX IS TABLE OF DEPRECIATION_REC;
  --------------------------------------------
  -- This procedure will query DEPRECIATION --
  --------------------------------------------
  PROCEDURE QUERY_DEPRECIATION(P_RESULT        IN OUT DEPRECIATION_REF,
                               P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                               P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);

  ------------------------------------------------------
  -- Table function used to query DEPRECIATION --
  ------------------------------------------------------
  FUNCTION QUERY_DEPRECIATION_APEX(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                   P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN QUERY_DEPRECIATION_TAB_APEX
    PIPELINED;
  ---------------------------------------------
  -- This procedure will insert DEPRECIATION --
  ---------------------------------------------
  PROCEDURE INSERT_DEPRECIATION(P_BLOCK_DATA IN OUT DEPRECIATION_TAB);

  ---------------------------------------------
  -- This procedure will update DEPRECIATION --
  ---------------------------------------------
  PROCEDURE UPDATE_DEPRECIATION(P_BLOCK_DATA IN OUT DEPRECIATION_TAB);

  ---------------------------------------------
  -- This procedure will delete DEPRECIATION --
  ---------------------------------------------
  PROCEDURE DELETE_DEPRECIATION(P_BLOCK_DATA IN OUT DEPRECIATION_TAB);

  -------------------------------------------
  -- This procedure will lock DEPRECIATION --
  -------------------------------------------
  PROCEDURE LOCK_DEPRECIATION(P_BLOCK_DATA IN OUT DEPRECIATION_TAB);

  ------------------
  -- record group --
  ------------------
  TYPE ADMIN_COST_REC IS RECORD(
    PROPOSAL_ID      DEFINITIONS.CPT_PROP_DTL_COSTING.PROPOSAL_ID%TYPE,
    PROPOSAL_SRNO    DEFINITIONS.CPT_PROP_DTL_COSTING.PROPOSAL_SRNO%TYPE,
    ADMIN_COSTING_ID DEFINITIONS.CPT_PROP_DTL_COSTING.ADMIN_COSTING_ID%TYPE,
    COST_DESC        DEFINITIONS.ADMIN_COSTING.DESCRIPTION%TYPE,
    COST             DEFINITIONS.CPT_PROP_DTL_COSTING.COST%TYPE,
    PERCENTAGE       DEFINITIONS.CPT_PROP_DTL_COSTING.PERCENTAGE%TYPE);

  ----------------
  -- ref cursor --
  ----------------
  TYPE ADMIN_COST_REF IS REF CURSOR RETURN ADMIN_COST_REC;

  ----------------------------------
  -- plsql table for CPT question --
  ----------------------------------
  TYPE ADMIN_COST_TAB IS TABLE OF ADMIN_COST_REC INDEX BY BINARY_INTEGER;
  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_ADMIN_COST_TAB_APEX IS TABLE OF ADMIN_COST_REC;

  --------------------------------------------
  -- This procedure will query ADMIN_COST --
  --------------------------------------------
  PROCEDURE QUERY_ADMIN_COST(P_RESULT        IN OUT ADMIN_COST_REF,
                             P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE);
  ------------------------------------------------------
  -- Table function used to query DEPRECIATION --
  ------------------------------------------------------
  FUNCTION QUERY_ADMIN_COST_APEX(P_PROPOSAL_ID   IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                                 P_PROPOSAL_SRNO IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE)
    RETURN QUERY_ADMIN_COST_TAB_APEX
    PIPELINED;
  ---------------------------------------------
  -- This procedure will insert ADMIN_COST --
  ---------------------------------------------
  PROCEDURE INSERT_ADMIN_COST(P_BLOCK_DATA IN OUT ADMIN_COST_TAB);

  ---------------------------------------------
  -- This procedure will update ADMIN_COST --
  ---------------------------------------------
  PROCEDURE UPDATE_ADMIN_COST(P_BLOCK_DATA IN OUT ADMIN_COST_TAB);

  ---------------------------------------------
  -- This procedure will delete ADMIN_COST --
  ---------------------------------------------
  PROCEDURE DELETE_ADMIN_COST(P_BLOCK_DATA IN OUT ADMIN_COST_TAB);

  -------------------------------------------
  -- This procedure will lock ADMIN_COST --
  -------------------------------------------
  PROCEDURE LOCK_ADMIN_COST(P_BLOCK_DATA IN OUT ADMIN_COST_TAB);

  ----------------------------------------------------
  -- RECORD TYPE DECLARATION FOR PROJECT TABLE DATA --
  ----------------------------------------------------
  TYPE CPT_PROP_TRACK_REC IS RECORD(
    PROPOSAL_ID    DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
    WFE_NO         DEFINITIONS.CPT_PROPOSAL.WFE_NO%TYPE,
    EVENT          DEFINITIONS.EVENT.DESCRIPTION%TYPE,
    PERFORMED_MRNO REGISTRATION.PATIENT.MRNO%TYPE,
    PERFORMED_BY   REGISTRATION.PATIENT.NAME%TYPE,
    DATETIME       DATE,
    REMARKS        DEFINITIONS.CPT_PROP_WORKFLOW.REMARKS%TYPE,
    IN_QUEUE       VARCHAR2(1000));
  -- REF CURSOR --
  TYPE CPT_PROP_TRACK_REF IS REF CURSOR RETURN CPT_PROP_TRACK_REC;
  -- ASSOCIATIVE ARRAY --
  TYPE CPT_PROP_TRACK_TAB IS TABLE OF CPT_PROP_TRACK_REC INDEX BY BINARY_INTEGER;

  -------------------------
  -- Associative Array --
  -------------------------
  TYPE QUERY_CPT_PROP_TRACK_TAB_APEX IS TABLE OF CPT_PROP_TRACK_REC;

  -----------------------------------------------------------------------------
  -- THIS PROCEDURE WILL BE USED TO QUERY DATA FROM CPT PROPOSAL QUEUE TABLE --
  -----------------------------------------------------------------------------
  PROCEDURE QUERY_CPT_PROP_TRACK(P_RESULT      IN OUT CPT_PROP_TRACK_REF,
                                 P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE);
  ------------------------------------------------------
  -- Table function used to query DEPRECIATION --
  ------------------------------------------------------
  FUNCTION QUERY_CPT_PROP_TRACK_APEX(P_PROPOSAL_ID IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE)
    RETURN QUERY_CPT_PROP_TRACK_TAB_APEX
    PIPELINED;

  PROCEDURE SET_ITEM_COST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                          P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                          P_PROPOSAL_SRNO     IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
                          P_ITEM_ID           IN DEFINITIONS.CPT_PROP_DTL_MATERIAL.ITEM_ID%TYPE,
                          P_AMOUNT            IN DEFINITIONS.CPT_PROP_DTL_MATERIAL.UNIT_COST%TYPE,
                          P_USER_MRNO         IN VARCHAR2,
                          P_TERMINAL          IN VARCHAR2,
                          P_OBJECT_CODE       IN VARCHAR2,
                          P_ALERT_TEXT        OUT VARCHAR2,
                          P_STOP              OUT CHAR);
  PROCEDURE SET_PAYROLL_COST(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                             P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                             P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                             P_PROPOSAL_SRNO     IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
                             P_DESIGNATION_ID    IN DEFINITIONS.CPT_PROP_DTL_MANPOWER.DESIGNATION_ID%TYPE,
                             P_AMOUNT            IN DEFINITIONS.CPT_PROP_DTL_MANPOWER.PAYROLL_COST%TYPE,
                             P_USER_MRNO         IN VARCHAR2,
                             P_TERMINAL          IN VARCHAR2,
                             P_OBJECT_CODE       IN VARCHAR2,
                             P_ALERT_TEXT        OUT VARCHAR2,
                             P_STOP              OUT CHAR);
  PROCEDURE UPDATE_COSTING(P_ORGANIZATION_ID   IN DEFINITIONS.ORGANIZATION.ORGANIZATION_ID%TYPE,
                           P_LOGIN_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                           P_PROPOSAL_ID       IN DEFINITIONS.CPT_PROPOSAL.PROPOSAL_ID%TYPE,
                           P_PROPOSAL_SRNO     IN DEFINITIONS.CPT_PROP_DTL.PROPOSAL_SRNO%TYPE,
                           P_USER_MRNO         IN VARCHAR2,
                           P_TERMINAL          IN VARCHAR2,
                           P_OBJECT_CODE       IN VARCHAR2,
                           P_ALERT_TEXT        OUT VARCHAR2,
                           P_STOP              OUT CHAR);
END PKG_S01FRM00473;
```

### DEFINITIONS.PKG_S01REP00071
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00071 IS
  /***********************************************************************************************
         OBJECTIVE := THIS PACKAGE WAS CREATED FOR BED RESERVATION HISTORY .
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        12-MAY-2020   ALLAH RAKHA           1. CREATED THIS PACKAGE.
  ************************************************************************************************/

  -----------------------------------------------
  --Record for BED RESERVATION HISTORY--
  -----------------------------------------------
  TYPE REC_BRH IS RECORD(
    RESERVED_NO ORDERENTRY.BED_RESERVATION_HISTORY.RESERVED_NO%TYPE,
    BED_ID      ORDERENTRY.BED_RESERVATION_HISTORY.BED_ID%TYPE,
    MRNO        REGISTRATION.PATIENT.MRNO%TYPE,
    CATEGORY    DEFINITIONS.ROOM_CATEGORY.DESCRIPTION%TYPE,
    FROM_DATE   DATE,
    TO_DATE     DATE,
    PATIENT     REGISTRATION.PATIENT.NAME%TYPE);

  TYPE TAB_BRH IS TABLE OF REC_BRH;
  -----------------------------------------------
  --Function for BED RESERVATION HISTORY Report--
  -----------------------------------------------
  FUNCTION F_BED_RESERVATION_HISTORY(P_FROM_DATE IN DATE) RETURN TAB_BRH
    PIPELINED;

END PKG_S01REP00071;
```

### DEFINITIONS.PKG_S01REP00072
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00072 IS
  /***********************************************************************************************
         OBJECTIVE := THIS PACKAGE WAS CREATED FOR BED RESERVATION STATUS .
         ----------------------------------------------------------------------------------
         REVISIONS:
         VER        DATE          AUTHOR                 DESCRIPTION
         ---------  -----------   -------------------    -----------------------------------
         1.0        12-MAY-2020   ALLAH RAKHA           1. CREATED THIS PACKAGE.
  ************************************************************************************************/

  -----------------------------------------------
  --Record for BED RESERVATION STATUS--
  -----------------------------------------------
  TYPE REC_BRH IS RECORD(
    RESERVED_NO  ORDERENTRY.BED_RESERVATION_HISTORY.RESERVED_NO%TYPE,
    BED_DESC     DEFINITIONS.DEF_BED.BED_DESC%TYPE,
    WARD_DESC    DEFINITIONS.ROOMS.DESCRIPTION%TYPE,
    MRNO         REGISTRATION.PATIENT.MRNO%TYPE,
    PATIENT_NAME REGISTRATION.PATIENT.NAME%TYPE,
    FROM_DATE    DATE,
    CATEGORY     DEFINITIONS.ROOM_CATEGORY.DESCRIPTION%TYPE);

  TYPE TAB_BRH IS TABLE OF REC_BRH;
  -----------------------------------------------
  --Function for BED RESERVATION STATUS Report--
  -----------------------------------------------
  FUNCTION F_BED_RESERVATION_STATUS(P_LOCATION_ID IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
    RETURN TAB_BRH
    PIPELINED;

END PKG_S01REP00072;
```

### DEFINITIONS.PKG_S01REP00114
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00114 AS
  /***********************************************************************************************
         OBJECTIVE := This report will show the Clinic Specailities and there related CPT Categories
                      with price groups
                                             
              1. Develop the report using pipelined function
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        26-Dec-2013   Muhammad Usman Afzal     1. Created this Package.
  ************************************************************************************************/
  -- Record Type --
  TYPE SPECIALITY_CATEGORY_REC IS RECORD(
    CLINIC_SPECIALITY_ID DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE,
    CLINIC_SPECIALITY    DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
    CPT_CATEGORY_ID      DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    CPT_CATEGORY         DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE,
    CATEGORY_PRICE       DEFINITIONS.CPT_CATEGORY.PRICE%TYPE,
    ADMIN_COSTING_ID     DEFINITIONS.CPT_CATEGORY_COSTING.ADMIN_COSTING_ID%TYPE,
    ADMIN_COSTING        DEFINITIONS.ADMIN_COSTING.DESCRIPTION%TYPE,
    ADMIN_COSTING_PRICE  DEFINITIONS.CPT_CATEGORY_COSTING.PRICE%TYPE);

  -- Associative Array --
  TYPE SPEC_CATEGORY_TAB IS TABLE OF SPECIALITY_CATEGORY_REC;

  ----------------------------------------------------------------------------------------
  -- This Function will return the Clinic Specailities and there related CPT Categories --
  ----------------------------------------------------------------------------------------
  FUNCTION GET_SPECIALITY_CATEGORY(P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE,
                                   P_CPT_CATEGORY_ID      IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE)
    RETURN SPEC_CATEGORY_TAB
    PIPELINED;
END PKG_S01REP00114;
```

### DEFINITIONS.PKG_S01REP00115
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00115 AS
  /***********************************************************************************************
         OBJECTIVE := This report will show the Clinic Specailities and there related CPT Categories
                      with price groups
                                             
              1. Develop the report using pipelined function
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        26-Dec-2013   Muhammad Usman Afzal     1. Created this Package.
  ************************************************************************************************/
  -- Record Type --
  TYPE SPECIALITY_PRICE_CATEGORY_REC IS RECORD(
    DEPARTMENT_ID      DEFINITIONS.DEPARTMENT.DEPARTMENT_ID%TYPE,
    DEPARTMENT         DEFINITIONS.DEPARTMENT.DESCRIPTION%TYPE,
    SPECIALITY_ID      DEFINITIONS.CLINIC_SPECIALITY.SPECIALITY_ID%TYPE,
    CLINICAL_SPECIALTY DEFINITIONS.CLINIC_SPECIALITY.DESCRIPTION%TYPE,
    CPT_CATEGORY_ID    DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
    PRICE_CATEGORY     DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE,
    CATEGORY_PRICE     DEFINITIONS.CPT_CATEGORY.PRICE%TYPE,
    CPT_ID             DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT                DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_PRICE          DEFINITIONS.CPT.PRICE%TYPE);

  -- Associative Array --
  TYPE SPEC_PRICE_CATEGORY_TAB IS TABLE OF SPECIALITY_PRICE_CATEGORY_REC;

  ----------------------------------------------------------------------------------------
  -- This Function will return the Clinic Specailities and there related CPT Categories --
  ----------------------------------------------------------------------------------------
  FUNCTION GET_SPECIALITY_PRICE_CATEGORY(P_CLINIC_SPECIALITY_ID IN DEFINITIONS.CLINIC_SPECIALITY.CLINIC_SPECIALITY_ID%TYPE,
                                         P_CPT_CATEGORY_ID      IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE,
                                         P_CPT_ID               IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN SPEC_PRICE_CATEGORY_TAB
    PIPELINED;
END PKG_S01REP00115;
```

### DEFINITIONS.PKG_S01REP00120
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00120 AS
  /****************************************************************************
      OBJECTIVE := This package was created for Clinical Service Price Report
      -----------------------------------------------------------------------
      Ver     Date         Author             Description
      ----   -----------   ----------------    -------------------
      1.0    30-MAR-2016   M. Ali Khubaib      1. Created this Package.
      2.0    29-JUN-2021  M.Usman Tahir        2.Add CPT Tables
  *****************************************************************************/
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE CPT_REC IS RECORD(
    LOCATION_ID          DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC        DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
    DEPARTMENT_NATURE    DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
    CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC             DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OPD_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    IPD_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    EAR_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CPT_TAB IS TABLE OF CPT_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION GET_RECORD(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                      P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE /*,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            P_PATIENT_TYPE_ID      IN DEFINITIONS.CLINICAL_SERVICE_PRICE.PATIENT_TYPE_ID%TYPE*/)
  
   RETURN CPT_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE ORDER_REC IS RECORD(
    ORDER_LOCATION_ID    DEFINITIONS.ORDER_LOCATION_CPT_PRICE.ORDER_LOCATION_ID%TYPE,
    ORDER_DESC           DEFINITIONS.ORDER_LOCATION.DESCRIPTION%TYPE,
    LOCATION_ID          DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC        DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
    DEPARTMENT_NATURE    DEFINITIONS.DEPARTMENT_NATURE.DESCRIPTION%TYPE,
    CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC             DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE ORDER_TAB IS TABLE OF ORDER_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION ORDER_LOCATION(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                          P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                          P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                          P_PATIENT_TYPE_ID      IN DEFINITIONS.CLINICAL_SERVICE_PRICE.PATIENT_TYPE_ID%TYPE)
  
   RETURN ORDER_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE CLINIC_REC IS RECORD(
    CLINIC_ID     DEFINITIONS.CLINIC_CPT_PRICE.CLINIC_ID%TYPE,
    CLINC_DESC    REGISTRATION.CLINIC.CLINIC_FULL_NAME%TYPE,
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    CPT_ID        DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC      DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CLINIC_TAB IS TABLE OF CLINIC_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION CLINIC_CPT(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                      P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                      P_PATIENT_TYPE_ID      IN DEFINITIONS.CLINICAL_SERVICE_PRICE.PATIENT_TYPE_ID%TYPE)
  
   RETURN CLINIC_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE DOCTOR_REC IS RECORD(
    DOCTOR_ID     DEFINITIONS.Doctor_Cpt_Price.DOCTOR_ID%TYPE,
    DOCTOR_NAME   DEFINITIONS.DOCTOR.NAME%TYPE,
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    CPT_ID        DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC      DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE DOCTOR_TAB IS TABLE OF DOCTOR_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION DOCTOR_CPT(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                      P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                      P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                      P_PATIENT_TYPE_ID      IN DEFINITIONS.CLINICAL_SERVICE_PRICE.PATIENT_TYPE_ID%TYPE)
  
   RETURN DOCTOR_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE PATIENT_REC IS RECORD(
    PATIENT_TYPE_ID     DEFINITIONS.PATIENT_TYPE.PATIENT_TYPE_ID%TYPE,
    PATIENT_DESCRIPTION DEFINITIONS.PATIENT_TYPE.DESCRIPTION%TYPE,
    LOCATION_ID         DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC       DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    CPT_ID              DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC            DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE           DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE           DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE PATIENT_TAB IS TABLE OF PATIENT_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION PATIENT_CPT(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                       P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                       P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
                       P_PATIENT_TYPE_ID      IN DEFINITIONS.CLINICAL_SERVICE_PRICE.PATIENT_TYPE_ID%TYPE)
  
   RETURN PATIENT_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE CATEGORY_REC IS RECORD(
    CATEGORY_ID          DEFINITIONS.ROOM_CATEGORY.CATEGORY_ID%TYPE,
    CATEGORY_DESCRIPTION DEFINITIONS.ROOM_CATEGORY.DESCRIPTION%TYPE,
    LOCATION_ID          DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC        DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC             DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE            DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE CATEGORY_TAB IS TABLE OF CATEGORY_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION CATEGORY_CPT(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                        P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                        P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
  
   RETURN CATEGORY_TAB
    PIPELINED;
  ------------------------------------
  -- Record Group --
  ------------------------------------
  TYPE LOCATION_REC IS RECORD(
    LOCATION_ID   DEFINITIONS.LOCATION.LOCATION_ID%TYPE,
    LOCATION_DESC DEFINITIONS.LOCATION.DESCRIPTION%TYPE,
    CPT_ID        DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESC      DEFINITIONS.CPT.DESCRIPTION%TYPE,
    OLD_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE,
    NEW_PRICE     DEFINITIONS.CLINICAL_SERVICE_PRICE.PRICE%TYPE);
  -----------------------
  -- Associative Array --
  -----------------------
  TYPE LOCATION_TAB IS TABLE OF LOCATION_REC;

  -----------------------------------------------------------------------------------
  -- This function will return the Clinical Service Price against given Parameters --
  -----------------------------------------------------------------------------------
  FUNCTION LOCATION_CPT(P_CPT_ID               DEFINITIONS.CPT.CPT_ID%TYPE,
                        P_DEPARTMENT_NATURE_ID DEFINITIONS.DEPARTMENT_NATURE.DEPARTMENT_NATURE_ID%TYPE,
                        P_LOGIN_LOCATION_ID    IN DEFINITIONS.LOCATION.LOCATION_ID%TYPE)
  
   RETURN LOCATION_TAB
    PIPELINED;

END PKG_S01REP00120;
```

### DEFINITIONS.PKG_S01REP00132
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_S01REP00132 AS

  /***********************************************************************************************
         OBJECTIVE := This package is created for Corporate Client Invoice Detail Reprot
              1. Develop the report using pipelined function
         ----------------------------------------------------------------------------------
         REVISIONS:
         Ver        Date          Author                 Description
         ---------  -----------   -------------------    -----------------------------------
         1.0        28-Apr-2021   Muhammad Fahad Hassan  1. Created this Package.
  ************************************************************************************************/
  TYPE REC_CPT IS RECORD(
    CPT_ID            DEFINITIONS.CPT.CPT_ID%TYPE,
    CPT_DESCRIPTION   DEFINITIONS.CPT.DESCRIPTION%TYPE,
    CPT_SHORT_DESC    DEFINITIONS.CPT.SHORT_DESC%TYPE,
    CPT_CATEGORY_DESC DEFINITIONS.CPT_CATEGORY.DESCRIPTION%TYPE);
  -- Associative Array --
  TYPE TAB_CPT IS TABLE OF REC_CPT;

  -- Pipelined Function which will return the Data of the Report Detail on given parameters --
  FUNCTION GET_CPT_DATA(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN TAB_CPT
    PIPELINED;
  ----------------------------------------------------
  TYPE REC_CPT_REVISION_HIST IS RECORD(
    SRNO           DEFINITIONS.CPT_PRICE_HISTORY.SR_NO%TYPE,
    OLD_PRICE      DEFINITIONS.CPT_PRICE_HISTORY.OLD_PRICE%TYPE,
    NEW_PRICE      DEFINITIONS.CPT_PRICE_HISTORY.NEW_PRICE%TYPE,
    EFFECTIVE_DATE DEFINITIONS.CPT_PRICE_HISTORY.EFFECTIVE_DATE%TYPE,
    ACTIVATE_DATE  DEFINITIONS.CPT_PRICE_HISTORY.CHANGE_DATE%TYPE,
    REVIEW_DATE    DEFINITIONS.CPT_REVIEW_HISTORY.REVIEW_DATE%TYPE,
    REVIEW_REMARKS DEFINITIONS.CPT_REVIEW_HISTORY.REVIEW_REMARKS%TYPE);
  -- Associative Array --
  TYPE TAB_CPT_REVISION_HIST IS TABLE OF REC_CPT_REVISION_HIST;

  -- Pipelined Function which will return the Data of the Report Detail on given parameters --
  FUNCTION GET_PRICE_REVISION_HIST(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE)
    RETURN TAB_CPT_REVISION_HIST
    PIPELINED;
  --

END PKG_S01REP00132;
```

### DEFINITIONS.PKG_SETUP_DETAIL_ADMIN
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SETUP_DETAIL_ADMIN IS
  -- Author  : Syed Gohar Ali
  -- Created : 19-Aug-2019 15:01
  -- Purpose :
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_DETAIL_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_DETAIL_ADMIN.LOCATION_ID%TYPE,
                    P_ROW                 OUT DEFINITIONS.SETUP_DETAIL_ADMIN%ROWTYPE,
                    P_IGNORE_NO_DATA      IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2, 
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_NATURE_ID%TYPE,
                  P_SETUP_DETAIL_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_DETAIL_ID%TYPE,
                  P_LOCATION_ID         IN DEFINITIONS.SETUP_DETAIL_ADMIN.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_LOCATION_ID IN VARCHAR2,
                  P_CALLING_OBJECT      IN VARCHAR2,
                  P_CALLING_USER        IN VARCHAR2,  
                  P_CALLING_EVENT       IN VARCHAR2,
                  P_ROWID               OUT ROWID,
                  P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;  
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW                 IN OUT DEFINITIONS.SETUP_DETAIL_ADMIN%ROWTYPE,
                    P_IGNORE_DUPLICATE    IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN; 
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_DETAIL_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_DETAIL_ADMIN.LOCATION_ID%TYPE,
                    P_ROW                 IN OUT DEFINITIONS.SETUP_DETAIL_ADMIN%ROWTYPE,
                    P_UPDATE_NULL         IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_SETUP_DETAIL_ID     IN DEFINITIONS.SETUP_DETAIL_ADMIN.SETUP_DETAIL_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_DETAIL_ADMIN.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SETUP_DETAIL_ADMIN;
```

### DEFINITIONS.PKG_SETUP_NATURE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SETUP_NATURE IS
  -- Author  : Syed Gohr Ali
  -- Created : 19-Aug-2019 13:05
  -- Purpose :
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE.SETUP_NATURE_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.SETUP_NATURE%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE.SETUP_NATURE_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID     IN VARCHAR2,
                  P_CALLING_OBJECT  IN VARCHAR2,
                  P_CALLING_USER    IN VARCHAR2,
                  P_CALLING_EVENT   IN VARCHAR2,
                  P_ROWID           OUT ROWID,
                  P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.SETUP_NATURE%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE.SETUP_NATURE_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.SETUP_NATURE%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE.SETUP_NATURE_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SETUP_NATURE;
```

### DEFINITIONS.PKG_SETUP_NATURE_ADMIN
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SETUP_NATURE_ADMIN IS
  -- Author  : Syed Gohar Ali
  -- Created : 19-Aug-2019 14:46
  -- Purpose :
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_NATURE_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_DEPT_NATURE_ID      IN DEFINITIONS.SETUP_NATURE_ADMIN.DEPT_NATURE_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_NATURE_ADMIN.LOCATION_ID%TYPE,
                    P_ROW                 OUT DEFINITIONS.SETUP_NATURE_ADMIN%ROWTYPE,
                    P_IGNORE_NO_DATA      IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_NATURE_ADMIN.SETUP_NATURE_ID%TYPE,
                  P_DEPT_NATURE_ID      IN DEFINITIONS.SETUP_NATURE_ADMIN.DEPT_NATURE_ID%TYPE,
                  P_LOCATION_ID         IN DEFINITIONS.SETUP_NATURE_ADMIN.LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                  P_CALLING_LOCATION_ID IN VARCHAR2,
                  P_CALLING_OBJECT      IN VARCHAR2,
                  P_CALLING_USER        IN VARCHAR2, 
                  P_CALLING_EVENT       IN VARCHAR2,    
                  P_ROWID               OUT ROWID,
                  P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW                 IN OUT DEFINITIONS.SETUP_NATURE_ADMIN%ROWTYPE,
                    P_IGNORE_DUPLICATE    IN CHAR DEFAULT NULL,
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN; 
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_NATURE_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_DEPT_NATURE_ID      IN DEFINITIONS.SETUP_NATURE_ADMIN.DEPT_NATURE_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_NATURE_ADMIN.LOCATION_ID%TYPE,
                    P_ROW                 IN OUT DEFINITIONS.SETUP_NATURE_ADMIN%ROWTYPE,
                    P_UPDATE_NULL         IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SETUP_NATURE_ID     IN DEFINITIONS.SETUP_NATURE_ADMIN.SETUP_NATURE_ID%TYPE,
                    P_DEPT_NATURE_ID      IN DEFINITIONS.SETUP_NATURE_ADMIN.DEPT_NATURE_ID%TYPE,
                    P_LOCATION_ID         IN DEFINITIONS.SETUP_NATURE_ADMIN.LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA      IN VARCHAR2 DEFAULT 'N',
                    P_CALLING_LOCATION_ID IN VARCHAR2,
                    P_CALLING_OBJECT      IN VARCHAR2,
                    P_CALLING_USER        IN VARCHAR2,
                    P_CALLING_EVENT       IN VARCHAR2,
                    P_ERROR               OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SETUP_NATURE_ADMIN;
```

### DEFINITIONS.PKG_SETUP_NATURE_DETAIL
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SETUP_NATURE_DETAIL IS
  -- Author  : Syed Gohar Ali
  -- Created : 19-Aug-2019 14:22
  -- Purpose :
  -- ******************************************************************************************************--
  FUNCTION F_SELECT(P_SETUP_DETAIL_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_DETAIL_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_NATURE_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.SETUP_NATURE_DETAIL%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;  
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_SETUP_DETAIL_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_DETAIL_ID%TYPE,
                  P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_NATURE_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID     IN VARCHAR2,
                  P_CALLING_OBJECT  IN VARCHAR2,
                  P_CALLING_USER    IN VARCHAR2,   
                  P_CALLING_EVENT   IN VARCHAR2,
                  P_ROWID           OUT ROWID,
                  P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.SETUP_NATURE_DETAIL%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2, 
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_SETUP_DETAIL_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_DETAIL_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_NATURE_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.SETUP_NATURE_DETAIL%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_SETUP_DETAIL_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_DETAIL_ID%TYPE,
                    P_SETUP_NATURE_ID IN DEFINITIONS.SETUP_NATURE_DETAIL.SETUP_NATURE_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID     IN VARCHAR2,
                    P_CALLING_OBJECT  IN VARCHAR2,
                    P_CALLING_USER    IN VARCHAR2,
                    P_CALLING_EVENT   IN VARCHAR2,
                    P_ERROR           OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SETUP_NATURE_DETAIL;
```

### DEFINITIONS.PKG_SUB_LOCATIONS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SUB_LOCATIONS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 19:06
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
  FUNCTION F_SELECT(P_LOCATION_ID     IN DEFINITIONS.SUB_LOCATIONS.LOCATION_ID%TYPE,
                    P_SUB_LOCATION_ID IN DEFINITIONS.SUB_LOCATIONS.SUB_LOCATION_ID%TYPE,
                    P_ROW             OUT DEFINITIONS.SUB_LOCATIONS%ROWTYPE,
                    P_IGNORE_NO_DATA  IN CHAR DEFAULT NULL,

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_LOCATION_ID     IN DEFINITIONS.SUB_LOCATIONS.LOCATION_ID%TYPE,
                  P_SUB_LOCATION_ID IN DEFINITIONS.SUB_LOCATIONS.SUB_LOCATION_ID%TYPE,
                  P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.SUB_LOCATIONS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_LOCATION_ID     IN DEFINITIONS.SUB_LOCATIONS.LOCATION_ID%TYPE,
                    P_SUB_LOCATION_ID IN DEFINITIONS.SUB_LOCATIONS.SUB_LOCATION_ID%TYPE,
                    P_ROW             IN OUT DEFINITIONS.SUB_LOCATIONS%ROWTYPE,
                    P_UPDATE_NULL     IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_LOCATION_ID     IN DEFINITIONS.SUB_LOCATIONS.LOCATION_ID%TYPE,
                    P_SUB_LOCATION_ID IN DEFINITIONS.SUB_LOCATIONS.SUB_LOCATION_ID%TYPE,
                    P_IGNORE_NO_DATA  IN VARCHAR2 DEFAULT 'N',

                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SUB_LOCATIONS;
```

### DEFINITIONS.PKG_SYSTEM_CONSTANTS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SYSTEM_CONSTANTS AS

  PROCEDURE SYNC_CONSTANTS(P_STOP OUT VARCHAR2, P_ALERT_TEXT OUT VARCHAR2);
  PROCEDURE GEN_SYS_CONSTANT_MAIL(P_CONSTANT_ID IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.CONSTANT_ID%TYPE,
                                  P_DESCRIPTION IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.DESCRIPTION%TYPE,
                                  P_MODULE      IN DEFINITIONS.SCHEMAS.NAME%TYPE,
                                  P_PURPOSE     IN DEFINITIONS.SYSTEM_CONSTANTS_DEF.PURPOSE%TYPE,
                                  P_USER_MRNO   IN VARCHAR2,
                                  P_TERMINAL    IN VARCHAR2,
                                  P_TRN_DATE    IN DATE,
                                  P_LIST_ID     IN VARCHAR2,
                                  P_STOP        OUT VARCHAR2,
                                  P_ALERT_TEXT  OUT VARCHAR2);

END;
```

### DEFINITIONS.PKG_SYSTEM_CONSTANTS_SETUP
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_SYSTEM_CONSTANTS_SETUP IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 19:18
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
  FUNCTION F_SELECT(P_CONSTANT_ID    IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.CONSTANT_ID%TYPE,
                    P_SERIAL_NO      IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.SERIAL_NO%TYPE,
                    P_ROW            OUT DEFINITIONS.SYSTEM_CONSTANTS_SETUP%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_CONSTANT_ID    IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.CONSTANT_ID%TYPE,
                  P_SERIAL_NO      IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.SERIAL_NO%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.SYSTEM_CONSTANTS_SETUP%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_CONSTANT_ID    IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.CONSTANT_ID%TYPE,
                    P_SERIAL_NO      IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.SERIAL_NO%TYPE,
                    P_ROW            IN OUT DEFINITIONS.SYSTEM_CONSTANTS_SETUP%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_CONSTANT_ID    IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.CONSTANT_ID%TYPE,
                    P_SERIAL_NO      IN DEFINITIONS.SYSTEM_CONSTANTS_SETUP.SERIAL_NO%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_SYSTEM_CONSTANTS_SETUP;
```

### DEFINITIONS.PKG_TERMINALS
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_TERMINALS IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 19:32
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
  FUNCTION F_SELECT(P_TERMINAL_ID    IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.TERMINALS%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_TERMINAL_ID    IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.TERMINALS%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_TERMINAL_ID    IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.TERMINALS%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_TERMINAL_ID    IN DEFINITIONS.TERMINALS.TERMINAL_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_TERMINALS;
```

### DEFINITIONS.PKG_USER_PREFRENECE
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_USER_PREFRENECE IS
    PROCEDURE PROC_USER_PREFRENCES(P_PREFRENCE_TAB IN SECURITY.PREFRENCE_TAB,
                                                                 P_STOP          OUT VARCHAR2,
                                                                 P_ALERT_TEXT    OUT VARCHAR2);
END PKG_USER_PREFRENECE;
```

### DEFINITIONS.PKG_WORK_FLOW
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PKG_WORK_FLOW IS
  --PRAGMA SERIALLY_REUSABLE;
  -- Author  : Sajid Ali
  -- Created : 01-Dec-2019 19:51
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
  FUNCTION F_SELECT(P_WORK_FLOW_ID   IN DEFINITIONS.WORK_FLOW.WORK_FLOW_ID%TYPE,
                    P_ROW            OUT DEFINITIONS.WORK_FLOW%ROWTYPE,
                    P_IGNORE_NO_DATA IN CHAR DEFAULT NULL,
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_LOCK(P_WORK_FLOW_ID   IN DEFINITIONS.WORK_FLOW.WORK_FLOW_ID%TYPE,
                  P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                  P_LOCATION_ID    IN VARCHAR2,
                  P_CALLING_OBJECT IN VARCHAR2,
                  P_CALLING_USER   IN VARCHAR2,
                  P_CALLING_EVENT  IN VARCHAR2,
                  P_ROWID          OUT ROWID,
                  P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_INSERT(P_ROW              IN OUT DEFINITIONS.WORK_FLOW%ROWTYPE,
                    P_IGNORE_DUPLICATE IN CHAR DEFAULT NULL,
                    P_LOCATION_ID      IN VARCHAR2,
                    P_CALLING_OBJECT   IN VARCHAR2,
                    P_CALLING_USER     IN VARCHAR2,
                    P_CALLING_EVENT    IN VARCHAR2,
                    P_ERROR            OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_UPDATE(P_WORK_FLOW_ID   IN DEFINITIONS.WORK_FLOW.WORK_FLOW_ID%TYPE,
                    P_ROW            IN OUT DEFINITIONS.WORK_FLOW%ROWTYPE,
                    P_UPDATE_NULL    IN CHAR DEFAULT NULL,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
  FUNCTION F_DELETE(P_WORK_FLOW_ID   IN DEFINITIONS.WORK_FLOW.WORK_FLOW_ID%TYPE,
                    P_IGNORE_NO_DATA IN VARCHAR2 DEFAULT 'N',
                    P_LOCATION_ID    IN VARCHAR2,
                    P_CALLING_OBJECT IN VARCHAR2,
                    P_CALLING_USER   IN VARCHAR2,
                    P_CALLING_EVENT  IN VARCHAR2,
                    P_ERROR          OUT VARCHAR2) RETURN BOOLEAN;
  -- ******************************************************************************************************--
END PKG_WORK_FLOW;
```

### DEFINITIONS.PRESENTING_EXAMINATION_APEX
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PRESENTING_EXAMINATION_APEX IS
  PROCEDURE PRESENTING_EXAMINATION_APEX(P_TEMPLATE_ID IN NUMBER,
                                        P_GROUP_TYPE_ID NUMBER,
                                        P_GROUP_ID    IN NUMBER,
                                        P_ELEMENT_ID  IN NUMBER
                                        );
/*  PROCEDURE ADD_EH(P_OUT OUT CHAR, P_ALERT_TEXT OUT VARCHAR2);

  PROCEDURE ADD_EH_GROUP_TYPE(P_GROUP_TYPE_ID   IN NUMBER,
                              P_GROUP_TYPE_NAME IN VARCHAR2,
                              P_TYPE            IN VARCHAR2,
                              P_REMARKS         IN VARCHAR2,
                              P_OUT             OUT CHAR,
                              P_ALERT_TEXT      OUT VARCHAR2);

  PROCEDURE ADD_EH_GROUP(P_GROUP_TYPE_ID IN NUMBER,
                         P_GROUP_ID      IN NUMBER,
                         P_GROUP_NAME    IN VARCHAR2,
                         P_REMARKS         IN VARCHAR2,
                         P_OUT           OUT CHAR,
                         P_ALERT_TEXT    OUT VARCHAR2);
*/

END;
```

### DEFINITIONS.PRESENTING_SYMPTOMS_APEX
```sql
CREATE OR REPLACE PACKAGE DEFINITIONS.PRESENTING_SYMPTOMS_APEX IS
  PROCEDURE PRESENTING_SYMPTOMS_APEX(P_SYMPTOM_ID IN NUMBER);
END;
```

## Standalone procedures and functions (headers)

### DEFINITIONS.CALCULATE_APACHE_IV_1 (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.calculate_apache_iv_1(
    p_age NUMBER, p_tem NUMBER, p_map NUMBER, p_hr NUMBER, p_rr NUMBER,
    p_fio NUMBER, p_oxy NUMBER, p_pco NUMBER, p_pha NUMBER, p_nas NUMBER,
    p_ure NUMBER, p_cre NUMBER, p_uri NUMBER, p_bsl NUMBER, p_alb NUMBER,
    p_bil NUMBER, p_hto NUMBER, p_wbc NUMBER,
    p_gce NUMBER, p_gcv NUMBER, p_gcm NUMBER,
    p_quo NUMBER DEFAULT 0.8, p_patm NUMBER DEFAULT 760,
    p_los NUMBER, p_ori NUMBER, p_rea NUMBER, p_eme NUMBER, p_thr NUMBER,
    p_crf NUMBER, p_typ NUMBER, p_sys NUMBER, p_dia NUMBER,
    p_ven VARCHAR2, p_sed VARCHAR2,
    p_aps OUT NUMBER, p_mor OUT NUMBER, p_sej OUT NUMBER
) RETURN NUMBER IS
```

### DEFINITIONS.DEFAULT_CURRENCY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.DEFAULT_CURRENCY RETURN VARCHAR2  AS
```

### DEFINITIONS.ERROR_MESSAGE (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.ERROR_MESSAGE(P_Error_Number NUMBER) RETURN CHAR
 IS
```

### DEFINITIONS.FUNC_HOLIDAY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.FUNC_HOLIDAY(P_DATE DATE) RETURN CHAR  AS
```

### DEFINITIONS.FUN_ORDER_BY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.fun_order_by(V_MRNO registration.patient.mrno%type)
RETURN
NUMBER IS
```

### DEFINITIONS.F_BED_ACTIVE (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_BED_ACTIVE(P_BED_ID      VARCHAR2,
                                                    P_DATE        DATE,
                                                    P_LOCATION_ID IN VARCHAR2)
  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_ROOM_CATEGORY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_ROOM_CATEGORY(P_ROOM_ID     VARCHAR2,
                                                       P_DATE        DATE,
                                                       P_LOCATION_ID VARCHAR2)
  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_BED_CATEGORY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_BED_CATEGORY(P_BED_ID      VARCHAR2,
                                                      P_DATE        DATE,
                                                      P_LOCATION_ID IN VARCHAR2)
  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_DB_SERVICES_CHECK (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_DB_SERVICES_CHECK(P_ROW_OLD      DEFINITIONS.DB_SERVICES%ROWTYPE,
                                                           P_ROW_NEW      DEFINITIONS.DB_SERVICES%ROWTYPE,
                                                           P_SERVICE_NAME IN VARCHAR2,
                                                           P_ACTION       IN VARCHAR2,
                                                           P_ERROR        OUT VARCHAR2)
  RETURN BOOLEAN IS
```

### DEFINITIONS.F_DISPLAY_CPT_DESC (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_DISPLAY_CPT_DESC(P_CPT_REPORT_ID IN VARCHAR2,
                                                          P_CPT_ID        IN VARCHAR2)
/*****************************************************************************************
         FUNCTION NAME:F_DISPLAY_CPT_ID
         PURPOSE: This Function is
```

### DEFINITIONS.F_DISPLAY_CPT_ID (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_DISPLAY_CPT_ID(P_CPT_REPORT_ID IN VARCHAR2,
                                                        P_CPT_ID        IN VARCHAR2)
/*****************************************************************************************
         FUNCTION NAME:F_DISPLAY_CPT_ID
         PURPOSE: This Function is
```

### DEFINITIONS.F_DOCTOR_NAME (function)
```sql
create or replace function definitions.f_doctor_name(P_doctor_id VARCHAR2) return varchar2 is
```

### DEFINITIONS.F_GET_APPEARANCE_DESC (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_GET_APPEARANCE_DESC(P_APPEARANCE_ID IN VARCHAR2)
/*****************************************************************************************
         Function name:F_GET_APPEARANCE_DESC
         Purpose: This function is
```

### DEFINITIONS.F_GET_COLOR_NAME (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_GET_COLOR_NAME(P_COLOR_ID IN VARCHAR2)
/*****************************************************************************************
         FUNCTION NAME:F_GET_COLOR_NAME
         PURPOSE: This Function is
```

### DEFINITIONS.F_GET_DESC (function)
```sql
create or replace function definitions.f_get_desc(cpt_id definitions.cpt.cpt_id%type)
return definitions.cpt.description is
```

### DEFINITIONS.F_GET_PATIENT_ICDS (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_GET_PATIENT_ICDS(P_MRNO       VARCHAR2,
                                                          P_REPORTABLE CHAR)
  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_GET_SPECIMEN_DESC (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_GET_SPECIMEN_DESC(P_SPECIMEN_ID IN VARCHAR2)
/*****************************************************************************************
         FUNCTION NAME:F_GET_SPECIMEN_DESC
         PURPOSE: This Function is
```

### DEFINITIONS.F_GET_SUPERNATANT_DESC (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_GET_SUPERNATANT_DESC(P_SUPERNATANT_ID IN VARCHAR2)
/*****************************************************************************************
         Function Name:F_GET_SUPERNATANT_DESC
         Purpose: This function is
```

### DEFINITIONS.F_NEXT_COUNTER (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_NEXT_COUNTER(P_COUNTER_TYPE   IN VARCHAR2,
                                                      P_WHERE_CLAUSE   IN VARCHAR2 DEFAULT NULL,
                                                      P_LOCATION_ID    IN VARCHAR2 DEFAULT NULL,
                                                      P_CALLING_OBJECT IN VARCHAR2,
                                                      P_CALLING_USER   IN VARCHAR2,
                                                      P_CAlLING_EVENT  IN VARCHAR2,
                                                      P_ERROR          OUT VARCHAR2)
  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_PHY_DEFAULT_STORE (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_PHY_DEFAULT_STORE(P_LOCATION_ID       VARCHAR2,

                                                           P_ORDER_LOCATION_ID VARCHAR2)

  RETURN VARCHAR2 AS
```

### DEFINITIONS.F_REPORT_TYPE (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.F_REPORT_TYPE(P_REPORT_TYPE VARCHAR2)
  RETURN VARCHAR2 IS
```

### DEFINITIONS.GET_APACHE_CHIDIA1_VALUES (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.get_apache_chidia1_values (
    p_system_id IN NUMBER,
    p_detail_id IN NUMBER
) RETURN NUMBER AS
```

### DEFINITIONS.GET_APACHE_CHIDIA2_VALUES (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.get_apache_chidia2_values (
    p_system_id IN NUMBER,
    p_detail_id IN NUMBER
) RETURN NUMBER AS
```

### DEFINITIONS.GET_APACHE_MEDDIA1_VALUES (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.get_apache_meddia1_values (
    p_system_id IN NUMBER,
    p_detail_id IN NUMBER
) RETURN NUMBER AS
```

### DEFINITIONS.GET_APACHE_MEDDIA2_VALUES (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.get_apache_meddia2_values (
    p_system_id IN NUMBER,
    p_detail_id IN NUMBER
) RETURN NUMBER AS
```

### DEFINITIONS.GET_LOCAL_CURRENCY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.GET_LOCAL_CURRENCY RETURN VARCHAR2 AS
```

### DEFINITIONS.GET_USER_ALERT (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.get_user_alert(p_alert_id IN NUMBER)
	RETURN VARCHAR2 IS
```

### DEFINITIONS.LOCAL_CURRENCY (function)
```sql
CREATE OR REPLACE FUNCTION DEFINITIONS.LOCAL_CURRENCY RETURN CHAR AS
```

### DEFINITIONS.BULK_CPT_PRICE_UDPATION (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.BULK_CPT_PRICE_UDPATION(P_USER_ID      IN VARCHAR2,
                                                                P_OBJECT_CODE  IN VARCHAR2, -- CALLING FORM
                                                                P_PROCESS_ID   IN VARCHAR2, -- NULL INITIALLY
                                                                P_TERMINAL     IN VARCHAR2, -- TERMINAL NAME
                                                                P_EVENT        IN VARCHAR2, -- MAKING OF INVOICE
                                                                P_CALL_PURPOSE IN VARCHAR2, -- NULL
                                                                P_ALERT_TEXT   OUT VARCHAR2, -- OUT ALERT TEXT
                                                                P_STOP         OUT CHAR -- OUT STOP Y/N
                                                                ) IS
```

### DEFINITIONS.CPT_CAT_PRICE_ACTIVATE (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.CPT_CAT_PRICE_ACTIVATE(P_CPT_CATEGORY_ID IN DEFINITIONS.CPT_CATEGORY.CPT_CATEGORY_ID%TYPE DEFAULT NULL) IS
```

### DEFINITIONS.CPT_ACTIVATE_EFFECTIVE_DATE (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.CPT_ACTIVATE_EFFECTIVE_DATE(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE) IS
```

### DEFINITIONS.CPT_CATAGORY_REVISION (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.CPT_CATAGORY_REVISION(P_CPT_ID          IN VARCHAR2,
                                                              P_EFFECTIVE_DATE  IN DATE,
                                                              P_CPT_CATEGORY_ID IN VARCHAR2,

                                                              P_USER_ID      IN VARCHAR2,
                                                              P_OBJECT_CODE  IN VARCHAR2, -- calling form
                                                              P_PROCESS_ID   IN VARCHAR2, -- null initially
                                                              P_TERMINAL     IN VARCHAR2, -- Terminal name
                                                              P_EVENT        IN VARCHAR2, -- making of invoice
                                                              P_CALL_PURPOSE IN VARCHAR2, -- null
                                                              P_ALERT_TEXT   OUT VARCHAR2, -- OUT alert TExt
                                                              P_STOP         OUT CHAR -- OUT STOP Y/N
                                                              ) IS
```

### DEFINITIONS.CPT_DATA_UPDATE_DEC_2007 (procedure)
```sql
CREATE OR REPLACE Procedure DEFINITIONS.CPT_DATA_UPDATE_DEC_2007 as
```

### DEFINITIONS.CPT_REVIEW_ACTIVATE_MAILS (procedure)
```sql
create or replace procedure definitions.CPT_REVIEW_ACTIVATE_MAILS

(P_LIST_ID IN varchar) -- List ID on HIS '00038' and 00010 on DEVDB

 as
```

### DEFINITIONS.CPT_TEMP_MATIX_TABLE_POPULATE (procedure)
```sql
create or replace procedure definitions.CPT_TEMP_MATIX_TABLE_POPULATE(p_user_id in varchar2,
                                                                      P_Report  Varchar2) as
```

### DEFINITIONS.LOCATION_WISE_CPT_PRICE_REV (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.LOCATION_WISE_CPT_PRICE_REV(P_CPT_ID IN DEFINITIONS.CPT.CPT_ID%TYPE) IS
```

### DEFINITIONS.POPULATE_TASKS (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.populate_tasks(p_mrno hrd.information.mrno%TYPE) IS
```

### DEFINITIONS.PROC_POS_RESPONSE_MESSAGE (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.PROC_POS_RESPONSE_MESSAGE(P_RESPONSE_DATE      IN varchar2,
                                                                  P_RESPONSE_TIME      IN VARCHAR2,
                                                                  P_RESPONSE_TID       IN NUMBER,
                                                                  P_RESPONSE_MID       IN NUMBER,
                                                                  P_RESPONSE_BATCH_NO  IN NUMBER,
                                                                  P_INVOICE_NO         IN VARCHAR2,
                                                                  P_CARD_NO            IN VARCHAR2,
                                                                  P_CARD_ENTRY         IN VARCHAR2,
                                                                  P_CARD_HOLDER_NAME   IN VARCHAR2,
                                                                  P_TIP_AMOUNT         IN NUMBER,
                                                                  P_TXN_AMOUNT         IN NUMBER,
                                                                  P_RESPONSE_CODE      IN NUMBER,
                                                                  P_RESPONSE           IN VARCHAR2,
                                                                  P_RRN_NO             IN NUMBER,
                                                                  P_AUTH_CODE          IN NUMBER,
                                                                  P_AID                IN VARCHAR2,
                                                                  P_TC                 IN VARCHAR2,
                                                                  P_CARD_BRAND         IN VARCHAR2,
                                                                  P_VERIFIED_BY        IN VARCHAR2,
                                                                  P_VERSION            IN VARCHAR2,
                                                                  P_RESERVE1           IN VARCHAR2,
                                                                  P_RESERVE2           IN VARCHAR2,
                                                                  P_PATIENT_INV_NO     IN VARCHAR2,
                                                                  P_DISC_NAME          IN VARCHAR2,
                                                                  P_DISC_VALUE         IN VARCHAR2,
                                                                  P_DISC_AMT           IN NUMBER,
                                                                  P_FBR_POS_FEE        IN NUMBER,
                                                                  P_TO_PAID            IN NUMBER,
                                                                  P_TAX_AMT            IN NUMBER,
                                                                  P_BILL_AMT           IN NUMBER,
                                                                  P_IS_SERVICE_CHARGE  IN VARCHAR2,
                                                                  P_SERVICE_CHARGE     IN VARCHAR2,
                                                                  P_SERVICE_CHARGE_AMT IN NUMBER,
                                                                  P_PRODUCT_NAME       IN VARCHAR2,
                                                                  P_ALERT_TEXT         OUT VARCHAR2,
                                                                  P_STOP               OUT CHAR) AS
```

### DEFINITIONS.P_DISTRIBUTED_MODE_ENTRY (procedure)
```sql
CREATE OR REPLACE PROCEDURE DEFINITIONS.P_DISTRIBUTED_MODE_ENTRY(P_EVENT                   CHAR,
                                                                 P_DISTRIBUTED_LOCATION_ID DEFINITIONS.DB_SERVICES_MODE.DISTRIBUTED_LOCATION_ID%TYPE,
                                                                 P_SERVICES_MODE           DEFINITIONS.DB_SERVICES_MODE.SERVICES_MODE%TYPE,
                                                                 P_IS_DISTRIBUTED_MODE     DEFINITIONS.DB_SERVICES.IS_DISTRIBUTED_MODE%TYPE,
                                                                 P_SERVICE_ID              DEFINITIONS.DB_SERVICES.SERVICE_ID%TYPE,
                                                                 P_STOP                    OUT CHAR,
                                                                 P_ALERT_TEXT              OUT VARCHAR2) AS
```

