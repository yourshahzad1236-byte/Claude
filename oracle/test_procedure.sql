-- Oracle 19c+ compatible. Self-contained: no tables required.
-- Run in SQL*Plus / SQLcl / SQL Developer with: SET SERVEROUTPUT ON

-- Unit under test: a simple pure function.
CREATE OR REPLACE FUNCTION calc_discount(
  p_amount   IN NUMBER,
  p_pct      IN NUMBER
) RETURN NUMBER
DETERMINISTIC
IS
  c_err_bad_input CONSTANT PLS_INTEGER := -20001;
BEGIN
  IF p_amount IS NULL OR p_pct IS NULL OR p_amount < 0 OR p_pct NOT BETWEEN 0 AND 100 THEN
    RAISE_APPLICATION_ERROR(c_err_bad_input, 'Invalid amount or percentage');
  END IF;
  RETURN ROUND(p_amount * p_pct / 100, 2);
END calc_discount;
/

-- Test procedure: runs assertions, reports PASS/FAIL per case, and raises
-- if any case failed so a CI job or scheduler sees a non-zero result.
-- It performs no COMMIT/ROLLBACK and touches no data.
CREATE OR REPLACE PROCEDURE test_calc_discount
IS
  c_err_tests_failed CONSTANT PLS_INTEGER := -20900;

  l_run    PLS_INTEGER := 0;
  l_failed PLS_INTEGER := 0;

  PROCEDURE report(p_name IN VARCHAR2, p_ok IN BOOLEAN, p_detail IN VARCHAR2 DEFAULT NULL) IS
  BEGIN
    l_run := l_run + 1;
    IF NOT p_ok THEN
      l_failed := l_failed + 1;
    END IF;
    DBMS_OUTPUT.PUT_LINE(CASE WHEN p_ok THEN 'PASS  ' ELSE 'FAIL  ' END
                         || p_name || CASE WHEN p_detail IS NOT NULL THEN ' - ' || p_detail END);
  END report;

  PROCEDURE assert_equals(p_name IN VARCHAR2, p_expected IN NUMBER, p_actual IN NUMBER) IS
  BEGIN
    report(p_name,
           p_expected = p_actual,
           'expected=' || p_expected || ' actual=' || p_actual);
  END assert_equals;

  -- Expects calc_discount to raise the given ORA error code.
  PROCEDURE assert_raises(p_name IN VARCHAR2, p_amount IN NUMBER, p_pct IN NUMBER,
                          p_expected_code IN PLS_INTEGER) IS
    l_dummy NUMBER;
  BEGIN
    l_dummy := calc_discount(p_amount, p_pct);
    report(p_name, FALSE, 'no exception raised');
  EXCEPTION
    WHEN OTHERS THEN
      report(p_name, SQLCODE = p_expected_code, 'sqlcode=' || SQLCODE);
  END assert_raises;
BEGIN
  DBMS_APPLICATION_INFO.SET_MODULE('test_calc_discount', 'running');

  -- Happy paths
  assert_equals('10% of 200',        20,    calc_discount(200, 10));
  assert_equals('0% discount',       0,     calc_discount(100, 0));
  assert_equals('100% discount',     100,   calc_discount(100, 100));
  assert_equals('rounds to 2 dp',    3.33,  calc_discount(33.33, 10));

  -- Boundary / error paths
  assert_equals('zero amount',       0,     calc_discount(0, 50));
  assert_raises('negative amount',   -1,    10,   -20001);
  assert_raises('pct over 100',      100,   101,  -20001);
  assert_raises('pct below 0',       100,   -1,   -20001);
  assert_raises('NULL amount',       NULL,  10,   -20001);
  assert_raises('NULL pct',          100,   NULL, -20001);

  DBMS_OUTPUT.PUT_LINE('Ran ' || l_run || ' tests, ' || l_failed || ' failed');
  DBMS_APPLICATION_INFO.SET_MODULE(NULL, NULL);

  IF l_failed > 0 THEN
    RAISE_APPLICATION_ERROR(c_err_tests_failed, l_failed || ' of ' || l_run || ' tests failed');
  END IF;
END test_calc_discount;
/

-- Execute:
-- SET SERVEROUTPUT ON
-- EXEC test_calc_discount;
