/*
1번. last_name과 sal*12사이에 쉼표(,)가 없다. 또한 sal대신 salary라고 써야한다.
또한 띄어쓰기가 있는 별칭은 ""로 묶어주어야한다.
*/
--1번
select employee_id, last_name, salary, 12*salary+100 "ANNUAL SALARY" 
from employees;

--2번
DESCRIBE DEPARTMENTS;
SELECT * FROM departments;

--3번
SELECT EMPLOYEE_ID, LAST_NAME ||' '||FIRST_NAME AS "NAME", JOB_ID, HIRE_DATE "STARTDATE"
FROM EMPLOYEES;

--4번
SELECT LAST_NAME||', '||JOB_ID AS "Employee and Title"
FROM employees;