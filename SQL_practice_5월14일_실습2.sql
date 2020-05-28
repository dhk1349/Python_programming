--1
SELECT last_name, hire_date
FROM employees
WHERE department_id=(SELECT department_id 
                    FROM employees 
                    WHERE last_name='Zlotkey') AND last_name <> 'Zlotkey';
--2                    
SELECT employee_id, last_name, salary
FROM employees
WHERE salary> (SELECT AVG(salary) FROM employees)
ORDER BY salary;

--3
SELECT employee_id, last_name
FROM employees
WHERE department_id in (SELECT department_id
                        FROM Employees
                        WHERE last_name like '%u%');

--4
SELECT last_name, department_id, job_id
FROM employees
WHERE department_id in (SELECT department_id 
                        FROM departments 
                        WHERE location_id=1700);
                        
                        
--5
SELECT last_name, salary
FROM employees
WHERE manager_id in (SELECT employee_id 
                  FROM employees 
                  WHERE last_name='King');
                  
--6
SELECT department_id, last_name, job_id
FROM employees
WHERE department_id = (SELECT department_id 
                        FROM departments
                        WHERE department_name='Executive');
                        
--7
SELECT employee_id, last_name, salary
FROM employees
WHERE salary>(SELECT AVG(salary) FROM employees) AND
      department_id in (SELECT department_id FROM employees WHERE last_name like '%u%');
      
--8
SELECT employee_id, last_name, salary
FROM employees
WHERE salary>(SELECT AVG(salary)
              FROM employees
              WHERE department_id in (SELECT department_id 
                                    FROM departments
                                    WHERE location_id in (SELECT location_id 
                                                        FROM locations 
                                                        WHERE country_id='US')));
--9
SELECT employee_id, last_name, salary, department_id
FROM   employees e1
WHERE  salary >= ALL(SELECT salary
                     FROM   employees e2
                     WHERE  e1.department_id = e2.department_id)
ORDER BY department_id;

--10
SELECT e1.employee_id, e1.last_name, e1.salary, e1.department_id
FROM   employees e1 INNER JOIN (SELECT department_id, max(salary) AS msal
                                FROM employees 
                                GROUP BY department_id) e2
        ON e1.salary=e2.msal and e1.department_id=e2.department_id
ORDER BY department_id;

--11
SELECT department_id, department_name
FROM departments d
WHERE exists(SELECT department_id FROM employees e WHERE e.department_id=d.department_id);

--12
select rownum, employee_id, last_name, salary
from (SELECT * FROM employees ORDER BY salary)
where rownum <= 5;
