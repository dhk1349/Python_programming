select last_name, salary, 12*salary+100 as "anual salary" 
from employees;

select last_name, salary, 12*salary* commission_pct as "anual salary" 
from employees;

select last_name || ' is a ' || job_id as "employ_data" 
from employees;

select DISTINCT job_id 
from employees;

SELECT DISTINCT department_name 
from departments;

DESCRIBE DEPARTMENTS;
SELECT * FROM departments;

describe EMPLOYEES;
SELECT EMPLOYEE_ID, LAST_NAME ||' '||FIRST_NAME AS "NAME", JOB_ID, HIRE_DATE "STARTDATE"
FROM EMPLOYEES;

SELECT LAST_NAME||', '||JOB_ID AS "Employee and Title"
FROM employees;