#select 5+5

create table Employee (FirstName VARCHAR(50), LastName VARCHAR(50));

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2),
    HireDate DATE
);

insert into Employee(FirstName, LastName) values ('Jack', 'sparrow');

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(1, 'John', 'Doe', 'HR', 50000.00, '2020-01-15'),
(2, 'Jane', 'Smith', 'Finance', 60000.00, '2019-03-23'),
(3, 'Alice', 'Johnson', 'IT', 75000.00, '2021-07-10'),
(4, 'Bob', 'Brown', 'Marketing', 55000.00, '2018-09-30'),
(5, 'Charlie', 'Davis', 'IT', 70000.00, '2022-02-20');

select * from Employees;

select EmployeeID, concat(FirstName, ' ', LastName) as fullname from Employees;

--select FirstName || ' ' || LastName from Employees

--select * from Employees;

--select * from Employees where salary between 60000 and 70000;

--select * from Employees where LastName in ('Smith', 'Davis');

--delete from Employees where Salary > 70000;  

--delete from Employees;  

--Truncate table Employees;

--select * from Employees;

--INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, HireDate)
--VALUES
--(1, 'John', 'Doe', 'HR', 50000.00, '2020-01-15');

select * from Employees;

--Drop table Employees;

--select TOP 3  * from Employees;

--select * from Employees Order by FirstName desc;

select Count(Salary) [MinSalary] from Employees;

--select * from Employees;

Select Department, Count(*) As TotalEmployees from Employees  Group by Department;

select TotalEmployees from Employees;






