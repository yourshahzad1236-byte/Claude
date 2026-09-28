--------------------------------------------------------------------------------
-- Staff Lounge Usage Tracking & Payroll Deduction
-- 02 - Triggers (audit columns, audit trail, data protection)
--------------------------------------------------------------------------------

----------------------------------------
-- Charge master: audit columns
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_CHARGE_MST_BIU
BEFORE INSERT OR UPDATE ON HRD.HRD_LOUNGE_CHARGE_MST
FOR EACH ROW
DECLARE
    V_USER VARCHAR2(255) := COALESCE(SYS_CONTEXT('APEX$SESSION', 'APP_USER'), SYS_CONTEXT('USERENV', 'SESSION_USER'));
BEGIN
    IF INSERTING THEN
        :NEW.CREATED_BY := NVL(:NEW.CREATED_BY, V_USER);
        :NEW.CREATED_ON := SYSTIMESTAMP;
    ELSE
        :NEW.CREATED_BY := :OLD.CREATED_BY;
        :NEW.CREATED_ON := :OLD.CREATED_ON;
        :NEW.UPDATED_BY := V_USER;
        :NEW.UPDATED_ON := SYSTIMESTAMP;
    END IF;
END TRG_LOUNGE_CHARGE_MST_BIU;
/

----------------------------------------
-- Card master: audit columns
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_CARD_MST_BIU
BEFORE INSERT OR UPDATE ON HRD.HRD_LOUNGE_CARD_MST
FOR EACH ROW
DECLARE
    V_USER VARCHAR2(255) := COALESCE(SYS_CONTEXT('APEX$SESSION', 'APP_USER'), SYS_CONTEXT('USERENV', 'SESSION_USER'));
BEGIN
    IF INSERTING THEN
        :NEW.CREATED_BY := NVL(:NEW.CREATED_BY, V_USER);
        :NEW.CREATED_ON := SYSTIMESTAMP;
    ELSE
        :NEW.CREATED_BY := :OLD.CREATED_BY;
        :NEW.CREATED_ON := :OLD.CREATED_ON;
        :NEW.UPDATED_BY := V_USER;
        :NEW.UPDATED_ON := SYSTIMESTAMP;
    END IF;

    IF :NEW.IS_ACTIVE = 'N' AND :NEW.BLOCKED_ON IS NULL THEN
        :NEW.BLOCKED_ON := TRUNC(SYSDATE);
    END IF;
END TRG_LOUNGE_CARD_MST_BIU;
/

----------------------------------------
-- Swipe transactions: audit columns
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_SWIPE_TRN_BI
BEFORE INSERT ON HRD.HRD_LOUNGE_SWIPE_TRN
FOR EACH ROW
BEGIN
    :NEW.CREATED_BY := NVL(:NEW.CREATED_BY,
                           COALESCE(SYS_CONTEXT('APEX$SESSION', 'APP_USER'), SYS_CONTEXT('USERENV', 'SESSION_USER')));
    :NEW.CREATED_ON := SYSTIMESTAMP;
END TRG_LOUNGE_SWIPE_TRN_BI;
/

----------------------------------------
-- Swipe transactions: protect financial data.
-- * Employee, swipe type, time and amount are immutable once recorded.
-- * A DEDUCTED charge can never change again.
-- * A REVERSED charge can never be re-activated.
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_SWIPE_TRN_BU
BEFORE UPDATE ON HRD.HRD_LOUNGE_SWIPE_TRN
FOR EACH ROW
BEGIN
    IF    :NEW.LOUNGE_SWIPE_ID <> :OLD.LOUNGE_SWIPE_ID
       OR :NEW.EMPLOYEE_ID     <> :OLD.EMPLOYEE_ID
       OR :NEW.LOUNGE_CARD_ID  <> :OLD.LOUNGE_CARD_ID
       OR :NEW.SWIPE_TYPE      <> :OLD.SWIPE_TYPE
       OR :NEW.SWIPE_TIMESTAMP <> :OLD.SWIPE_TIMESTAMP
       OR :NEW.CHARGE_AMOUNT   <> :OLD.CHARGE_AMOUNT
    THEN
        RAISE_APPLICATION_ERROR(-20101, 'Lounge swipe details cannot be modified once recorded.');
    END IF;

    IF :OLD.STATUS IN ('DEDUCTED', 'REVERSED') THEN
        RAISE_APPLICATION_ERROR(-20102, 'Lounge swipe ' || :OLD.LOUNGE_SWIPE_ID
                                        || ' is already ' || :OLD.STATUS || ' and cannot be changed.');
    END IF;

    :NEW.CREATED_BY := :OLD.CREATED_BY;
    :NEW.CREATED_ON := :OLD.CREATED_ON;
    :NEW.UPDATED_BY := COALESCE(SYS_CONTEXT('APEX$SESSION', 'APP_USER'), SYS_CONTEXT('USERENV', 'SESSION_USER'));
    :NEW.UPDATED_ON := SYSTIMESTAMP;
END TRG_LOUNGE_SWIPE_TRN_BU;
/

----------------------------------------
-- Swipe transactions: deletes are not allowed (use reversal instead)
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_SWIPE_TRN_BD
BEFORE DELETE ON HRD.HRD_LOUNGE_SWIPE_TRN
FOR EACH ROW
BEGIN
    RAISE_APPLICATION_ERROR(-20103, 'Lounge swipes cannot be deleted. Use PKG_STAFF_LOUNGE.P_REVERSE_SWIPE.');
END TRG_LOUNGE_SWIPE_TRN_BD;
/

----------------------------------------
-- Swipe transactions: audit trail on insert
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_SWIPE_TRN_AI
AFTER INSERT ON HRD.HRD_LOUNGE_SWIPE_TRN
FOR EACH ROW
BEGIN
    INSERT INTO HRD.HRD_LOUNGE_AUDIT_LOG
    (
        LOUNGE_SWIPE_ID, ACTION, OLD_STATUS, NEW_STATUS,
        OLD_CHARGE_AMOUNT, NEW_CHARGE_AMOUNT, PAYROLL_ID, REMARKS,
        ACTION_BY, CLIENT_IP
    )
    VALUES
    (
        :NEW.LOUNGE_SWIPE_ID, 'INSERT', NULL, :NEW.STATUS,
        NULL, :NEW.CHARGE_AMOUNT, :NEW.PAYROLL_ID,
        :NEW.SWIPE_TYPE || ' at ' || :NEW.LOUNGE_CODE || NVL2(:NEW.DEVICE_ID, ' / ' || :NEW.DEVICE_ID, NULL),
        :NEW.CREATED_BY, SYS_CONTEXT('USERENV', 'IP_ADDRESS')
    );
END TRG_LOUNGE_SWIPE_TRN_AI;
/

----------------------------------------
-- Swipe transactions: audit trail on update (status / payroll changes)
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_SWIPE_TRN_AU
AFTER UPDATE ON HRD.HRD_LOUNGE_SWIPE_TRN
FOR EACH ROW
BEGIN
    INSERT INTO HRD.HRD_LOUNGE_AUDIT_LOG
    (
        LOUNGE_SWIPE_ID, ACTION, OLD_STATUS, NEW_STATUS,
        OLD_CHARGE_AMOUNT, NEW_CHARGE_AMOUNT, PAYROLL_ID, REMARKS,
        ACTION_BY, CLIENT_IP
    )
    VALUES
    (
        :NEW.LOUNGE_SWIPE_ID, 'UPDATE', :OLD.STATUS, :NEW.STATUS,
        :OLD.CHARGE_AMOUNT, :NEW.CHARGE_AMOUNT, :NEW.PAYROLL_ID,
        :NEW.REVERSAL_REASON,
        :NEW.UPDATED_BY, SYS_CONTEXT('USERENV', 'IP_ADDRESS')
    );
END TRG_LOUNGE_SWIPE_TRN_AU;
/

----------------------------------------
-- Audit log: append-only
----------------------------------------
CREATE OR REPLACE TRIGGER HRD.TRG_LOUNGE_AUDIT_LOG_BU
BEFORE UPDATE OR DELETE ON HRD.HRD_LOUNGE_AUDIT_LOG
FOR EACH ROW
BEGIN
    RAISE_APPLICATION_ERROR(-20104, 'Lounge audit log is append-only.');
END TRG_LOUNGE_AUDIT_LOG_BU;
/
