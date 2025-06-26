import mysql.connector
import datetime
# Connecting to MySQL Database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'i can not write it broo',
    password = 'i can not write it broo',
    database = 'i can not write it broo, use your own DB'
)

# get info about server
print(mydb.get_server_info())

# make a cursor to control and work with th db
mycursor = mydb.cursor()

# SELECT 
mycursor.execute('select * from employees')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

print('----------------------------------------------------------------')

# INSERT 
sql = 'insert into employees (EmployeeID, FirstName, LastName, Email, HireDate) values (%s, %s, %s, %s, %s)'
val = (6, 'Jane', 'Smith', 'jane.smiths1@example.com', datetime.date(2022, 11, 12))
mycursor.execute(sql, val)
mydb.commit()

# select again
mycursor.execute('select * from employees')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

print('----------------------------------------------------------------')

# UPDATE 
sql = 'update employees set EmployeeID = %s where Email = %s'
val = (5, 'jane.smith@example.com')
mycursor.execute(sql, val)
mydb.commit()

# select again
mycursor.execute('select * from employees')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

print('----------------------------------------------------------------')

# DELETE  
sql = 'delete from employees where EmployeeID = %s'
val = (5,)
mycursor.execute(sql, val)
mydb.commit()

# select again
mycursor.execute('select * from employees')
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

mycursor.close()
mydb.close()