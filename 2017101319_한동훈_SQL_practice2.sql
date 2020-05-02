--1��
SELECT last_name, salary
FROM employees
WHERE salary>12000;

--2��
SELECT last_name, department_id 
FROM employees
WHERE employee_id=176;

--3��
SELECT last_name, salary
FROM employees
where salary NOT BETWEEN 5000 and 12000;

--4��
SELECT last_name, employee_id, hire_date
FROM employees
where hire_date between DATE'2007-02-20' AND DATE'2007-05-01'
order by hire_date;

--5��
SELECT LAST_NAME, DEPARTMENT_ID
FROM employees
WHERE department_id=20 OR department_id=50
ORDER BY last_name;

--6��
SELECT last_name "Employee", salary "Monthly Salary"
FROM employees
WHERE (salary between 5000 and 12000) and (department_id=20 or department_id=50);

--7��
SELECT last_name, hire_date
FROM employees
WHERE hire_date>='1994-01-01' and  hire_date<'1995-01-01';

--8��
SELECT last_name, job_id
FROM employees
WHERE manager_id is NULL;

--9��
SELECT last_name, salary, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL
order by salary, commission_pct;

--10��
SELECT last_name
FROM employees
WHERE last_name LIKE '__a%';

--11��
SELECT last_name
FROM employees
WHERE last_name LIKE '%a%' and last_name LIKE '%e%';

--12��
SELECT last_name, job_id, salary
FROM employees
WHERE job_id IN ('SA_REP', 'ST_CLERK') and salary NOT IN (2500, 3500, 7000);

--13��
SELECT last_name, salary, commission_pct
FROM employees
WHERE commission_pct>=0.2;
