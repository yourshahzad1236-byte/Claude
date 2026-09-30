# PAYROLL views

## PAYROLL.PAD_DR_FEE
```sql
create or replace force view payroll.pad_dr_fee as
select mrno, start_date, end_date, ad_code, pad.actual_amount, pad.calc_amount, pad.calc_amount_guarantee, pad.pending_amount
from payroll.pay_allowance_deduction pad
where pad.ad_code in ('007','043');
```

## PAYROLL.PAYMASTER_VIEW
```sql
create or replace force view payroll.paymaster_view as
select MRNo, P_Fund_Amount, P_Fund_Loan, posted
from payroll.pay_master;
```

## PAYROLL.PM_DR_FEE
```sql
create or replace force view payroll.pm_dr_fee as
select mrno, start_date, end_date, practice_income, practice_income_tax
from payroll.pay_master;
```

## PAYROLL.VU_PAY_STATUS
```sql
CREATE OR REPLACE FORCE VIEW PAYROLL.VU_PAY_STATUS AS
SELECT p.serial_no,
       p.mrno,
       p.date_from,
       p.date_to,
       p.status,
       p.disciplinary_reason_id,
       p.original_user_id,
       p.original_terminal,
       p.original_trn_date,
       p.user_id,
       p.terminal,
       p.trn_date,
       p.user_comments,
       substr(p.mrno, -11) emp_code,
       i.name,
       i.department,
       i.department_id,
       i.designation,
       m.pay_calc_date,
       m.pay_process,
       m.month
  FROM payroll.pay_status p, hrd.vu_information i, definitions.months m
 WHERE p.mrno = i.mrno
   AND p.date_from = m.pay_start_date
   AND p.date_to = m.pay_end_date;
```

## PAYROLL.V_PAYMASTER
```sql
CREATE OR REPLACE FORCE VIEW PAYROLL.V_PAYMASTER AS
SELECT MRNO, P_FUND_LOAN FROM PAYROLL.PAY_MASTER;
```

