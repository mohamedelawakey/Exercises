/*
	Write a SQL query to retrieve the names and email addresses of all customers from the “Customers” table.
	Create a query to select the product names and prices from the “Products” table where the price is greater than $50.
	Filter the orders table to show only those orders that were placed after January 1, 2023, and are in the “Shipped” status.
	Use a subquery to find products whose unit price is greater than the average unit price of all products.
	Calculate the total number of employees in each department from the “Employees” table.
*/

SELECT Name, Email
FROM Customers;

SELECT ProductName, Price
FROM Products
WHERE Price > 50;

SELECT *
FROM Orders
WHERE OrderDate > '2023-01-01'
AND OrderStatus = 'Shipped';

SELECT ProductName
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);

SELECT Department, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY Department;
