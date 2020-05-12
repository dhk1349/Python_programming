--1
SELECT e.last_name, e.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id=d.department_id;

--2
SELECT DISTINCT(e.job_id), d.location_id
FROM employees e, departments d
WHERE e.department_id=d.department_id and d.department_id=80;

--3
SELECT e.last_name, d.department_name, d.location_id, l.city, e.commission_pct
FROM employees e, departments d, locations l
WHERE e.department_id=d.department_id AND
d.location_id = l.location_id AND e.commission_pct <>0;

--4
SELECT e.last_name, d.department_name
FROM employees e, departments d
WHERE e.department_id=d.department_id AND e.last_name like '%a%';

--5
SELECT e.last_name, e.job_id, e.department_id, d.department_name
FROM employees e JOIN departments d ON(e.department_id= d.department_id) JOIN  
locations l ON (d.location_id= l.location_id)
WHERE l.city='Toronto';

--6
SELECT worker.last_name "Employee", worker.employee_id "EMP#", manager.last_name "Manager", manager.employee_id "Mgr#"
FROM employees worker,  employees manager
WHERE worker.manager_id=manager.employee_id(+);

--7
SELECT department_id DEPARTMENT, last_name EMPLOYEE, last_name COLLEAGUE
FROM employees 
WHERE (SELECT department_id FROM employees WHERE 
--아래 줄에 사원 이름을 지정
last_name='Bates')
-----------------------
= department_id; 

--8
SELECT e.last_name, TO_CHAR(e.hire_date, 'DD-MON-YY') HIRE_DATE
FROM employees e WHERE (
SELECT hire_date FROM employees WHERE last_name='Davies')<e.hire_date;

--9
SELECT worker.last_name, TO_CHAR(worker.hire_date, 'DD-MON-YY') HIRE_DATE, manager.last_name, TO_CHAR(manager.hire_date, 'DD-MON-YY') HIRE_DATE
FROM employees worker, employees manager
WHERE worker.manager_id=manager.employee_id and worker.hire_date< manager.hire_date;
