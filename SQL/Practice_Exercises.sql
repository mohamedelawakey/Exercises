/*
	Practice Exercises:
	Create a new table:

	Create a new table called “Orders” with columns for OrderID (primary key), CustomerID (foreign key referencing the Students table), OrderDate, and Total.
	Insert data into the Orders table:

	Insert at least three new orders for different customers.
	Read data from the Orders table:

	Retrieve all orders placed on a specific date.
	Retrieve orders for a specific customer, including the customer’s name and email from the Students table (using a JOIN).
	Update data in the Orders table:

	Update the Total column for a specific order.
	Delete data from the Orders table:

	Delete an order with a specific OrderID.
*/

create table Orders(
	OrderID int primary key,
    CustomerID int,
    OrderDate Date not null,
    Total int not null,
    foreign key (CustomerID) REFERENCES Students(CustomerID)
);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, Total)
VALUES
(1, 101, '2023-06-01', 250),
(2, 102, '2023-06-02', 320),
(3, 103, '2023-06-03', 150);

select 
	*
from 
	Orders
where 
	OrderDate = '2023-06-01';
    
select
	o.OrderID, o.CustomerID, o.Total, s.FirstName, s.LastName, s.Email
from
	Orders o
join 
	Students s on o.CustomerID = s.CustomerID
where
	o.CustomerID = 101;
    
update 
	orders
set
	Total = 400
where
	OrderID = 2;

delete from Orders
where
	OrderID = 3;
