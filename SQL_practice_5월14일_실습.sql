--1
SELECT ROUND(MAX(salary),0) "Maximum", 
            ROUND(MIN(salary),0) "Minimum",
            ROUND(SUM(salary),0) "Sum", 
            ROUND(AVG(salary),0) "Average"
FROM employees;
--2
SELECT job_id, ROUND(MAX(salary),0) "Maximum", 
            ROUND(MIN(salary),0) "Minimum",
            ROUND(SUM(salary),0) "Sum", 
            ROUND(AVG(salary),0) "Average"
FROM employees
GROUP BY job_id;
--3
SELECT job_id, count(*) 
FROM employees
GROUP BY job_id;
--4
SELECT COUNT(DISTINCT manager_id) "Number of Managers"
FROM employees;
--5
SELECT MAX(salary)-MIN(salary) DIFFERENCE
FROM employees;

--6
SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id is not null
GROUP BY manager_id
HAVING MIN(salary)>=6000
ORDER BY MIN(salary) DESC;

--7
SELECT d.department_name "Name", d.location_id "Location", COUNT(*) "Number of People", ROUND(AVG(salary), 2) "Salary"
FROM employees e, departments d
WHERE e.department_id=d.department_id
GROUP BY d.department_name, d.location_id;

--8
SELECT count(*) total, SUM(DECODE(TO_CHAR(hire_date, 'YYYY'), 2005, 1, 0)) "2005",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'), 2006, 1, 0)) "2006",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'), 2007, 1, 0)) "2007",
SUM(DECODE(TO_CHAR(hire_date, 'YYYY'), 2008, 1, 0)) "2008"
FROM employees;

--9
SELECT job_id "Job",
SUM(DECODE(department_id, 20, salary)) "Dept20",
SUM(DECODE(department_id, 50, salary)) "Dept50",
SUM(DECODE(department_id, 80, salary)) "Dept80",
SUM(DECODE(department_id, 90, salary)) "Dept90", 
SUM(salary) "Total"
FROM employees
GROUP BY job_id;