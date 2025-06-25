# Create (INSERT)

CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE
);

INSERT INTO Students (StudentID, FirstName, LastName, Email, EnrollmentDate)
values (1, 'John', 'Doe', 'john.doe@example.com', '2022-05-15');
INSERT INTO Students (StudentID, FirstName, LastName, Email, EnrollmentDate)
VALUES (2, 'Jane', 'Smith', 'jane.smith@example.com', '2021-08-22'),
       (3, 'Michael', 'Johnson', 'michael.johnson@example.com', '2023-02-01'),
       (4, 'Emily', 'Davis', 'emily.davis@example.com', '2023-03-15');
       
# Read (SELECT)

select 
	FirstName, LastName, Email
from 
	Students
where
	EnrollmentDate > '2022-01-01'
order by LastName ASC;

# Update (UPDATE)

update Students
	set 
		Email = 'updated@example.com'
	where
		StudentID = 1;

# Delete (DELETE)

delete from 
	Students
where 
	EnrollmentDate < '2021-01-01';