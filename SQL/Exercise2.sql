/*
	Exercise 2: Insert a few sample records into the “Employees” table using SQL INSERT statements.
*/

insert into Employees(EmployeeID, FirstName, LastName, Email, HireDate)
values (1, 'John', 'Doe', 'john.doe@example.com', '2022-05-15');
INSERT INTO Employees (EmployeeID, FirstName, LastName, Email, HireDate)
VALUES (2, 'Jane', 'Smith', 'jane.smith@example.com', '2021-08-22'),
       (3, 'Michael', 'Johnson', 'michael.johnson@example.com', '2023-02-01'),
       (4, 'Emily', 'Davis', 'emily.davis@example.com', '2023-03-15');