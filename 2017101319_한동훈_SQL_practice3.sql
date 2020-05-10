--1번
SELECT SYSDATE "Date"
FROM DUAL;

--2번
SELECT employee_id, last_name, salary, salary*1.15 "New Salary"
FROM employees;

--3번
SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),LOWER(substr(LAST_NAME,2,LENGTH(LAST_NAME)))) AS "NAME", LENGTH(last_name) "LENGTH"
FROM employees
WHERE last_name LIKE 'M%' OR last_name LIKE 'A%' OR last_name LIKE 'J%' 
ORDER BY "NAME";

--4번
SELECT last_name, ROUND((sysdate- hire_date)/7,0) MONTH_WORKED
FROM employees
ORDER BY MONTH_WORKED;

--5번
SELECT last_name || ' earn ' || salary || ' monthly but wants ' || 3* salary "Dream Salaries"
FROM employees;

--6번
SELECT last_name, lpad(SALARY, 15, '$') SALARY
FROM employees;

--7번
SELECT last_name, hire_date, TO_CHAR(NEXT_DAY(ADD_MONTHS(hire_date,6),'월요일'), 'DAY, DDTH "of "MONTH, YYYY') AS "REVIEW"
FROM employees;

--8번
SELECT last_name, hire_date, TO_CHAR(hire_date, 'DAY') "DAY"
FROM employees
ORDER BY TO_CHAR(hire_date-1, 'D');

--9번
SELECT last_name, decode(nvl(commission_pct, 0), 0, 'No Commission', commission_pct) "COMM"
FROM employees;

--10번
SELECT rpad(last_name, TRUNC(salary/1000,0)+length(last_name), '*') EMPLOYEES_AND_THEIR_SALARIES
FROM employees
ORDER BY salary DESC;

--11번
SELECT DECODE(job_id, 'AD_PRES', 'A', 'ST_MAN', 'B', 'IT_PROG', 'C', 'SA_REP', 'D', 'ST_CLERK', 'E' ,to_Char(0)) CONVERTED
FROM employees;

--12번
SELECT CASE job_id WHEN 'AD_PRES' THEN 'A' 
WHEN 'ST_MAN' THEN 'B'
WHEN'IT_PROG' THEN 'C'
WHEN'SA_REP' THEN 'D' 
WHEN'ST_CLERK' THEN 'E' 
ELSE to_Char(0) END AS "CONVERTED"
FROM employees;