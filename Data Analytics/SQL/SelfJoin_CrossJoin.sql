-- create a table
CREATE TABLE employee (
  emp_id PRIMARY KEY,
  name VARCHAR(50),
  dept_id INT
);
-- insert some values
INSERT INTO employee VALUES 
    (1, 'Ryan', 10),
    (2, 'Joanna', 20),
    (3, 'Alice', 30),
    (4, 'bob', Null),
    (5, 'charlie', 10);

SELECT * FROM employee;

CREATE TABLE department (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);
-- insert some values
INSERT INTO department VALUES 
    (10, 'HR'),
    (20, 'IT'),
    (30, 'Finance'),
    (40, 'Sales');

select * from department;

--SELF JOIN it use to join the table to itself

Select 
    e1.name as employee1,
    e2.name as employee2,
    e1.dept_id
FROM employee e1
JOIN
    employee e2 ON e1.dept_id = e2.dept_id AND e1.emp_id < e2.emp_id;

SELECT 
    e.name as employee,
    d.dept_name as department
FROM
    employee e
CROSS JOIN
    department d ON e.dept_id = d.dept_id;

Select name, dept_id from employee
UNION
Select dept_id, dept_name from department;














