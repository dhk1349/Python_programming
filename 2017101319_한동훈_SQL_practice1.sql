/*
1��. last_name�� sal*12���̿� ��ǥ(,)�� ����. ���� sal��� salary��� ����Ѵ�.
���� ���Ⱑ �ִ� ��Ī�� ""�� �����־���Ѵ�.
*/
--1��
select employee_id, last_name, salary, 12*salary+100 "ANNUAL SALARY" 
from employees;

--2��
DESCRIBE DEPARTMENTS;
SELECT * FROM departments;

--3��
SELECT EMPLOYEE_ID, LAST_NAME ||' '||FIRST_NAME AS "NAME", JOB_ID, HIRE_DATE "STARTDATE"
FROM EMPLOYEES;

--4��
SELECT LAST_NAME||', '||JOB_ID AS "Employee and Title"
FROM employees;