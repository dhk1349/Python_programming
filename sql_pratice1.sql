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
