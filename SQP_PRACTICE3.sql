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
SELECT last_name, hire_date, TO_CHAR(hire_date)
FROM employees;