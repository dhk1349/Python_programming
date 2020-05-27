--1
ALTER TABLE EMP
ADD CONSTRAINT my_emp_id_pk PRIMARY KEY(ID); 

--2
ALTER TABLE DEPT
ADD CONSTRAINT my_dept_id_pk PRIMARY KEY(ID);

--3
ALTER TABLE EMP
ADD(DEPT_ID NUMBER);

ALTER TABLE EMP
ADD CONSTRAINT my_emp_dept_id_fk 
FOREIGN KEY(DEPT_ID) REFERENCES DEPT(id);

--4
SELECT contraint_name, constraint_type FROM user_constraints
WHERE table_name='EMP' or table_name='DEPT';

--5
ALTER TABLE EMP
ADD commission NUMBER(2,2)
CONSTRAINT my_emp_commission CHECK(commission>0);
