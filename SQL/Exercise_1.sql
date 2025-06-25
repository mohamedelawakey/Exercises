/*
	Exercise 1: Write a SQL statement to create a table called “Employees” with columns for employee ID,
    first name, last name, department, and hire date.
*/

create table Employees(
	employeeID int PRIMARY KEY,
    firstname varchar(50) not null,
    lastname varchar(50) not null,
    department varchar(100) unique,
	hiredate date
)