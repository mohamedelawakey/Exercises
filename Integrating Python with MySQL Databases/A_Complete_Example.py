import mysql.connector

# Connecting to MySQL Database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'i can not write it broo',
    password = 'i can not write it broo',
    database = 'i can not write it broo, use your own DB'
)

mycursor = mydb.cursor()

# Create a table named customers (if it doesn't exist)
mycursor.execute("""
    create table if not exists customers(
        id int AUTO_INCREMENT primary key,
        name varchar(255) not null,
        email varchar(255) not null
    )
    """)

print("Table created successfully!")

# Insert some customer data
sql = 'insert into customers (name, email) values (%s, %s)'
val = ("John Doe", "john.doe@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

val = ("Jane Smith", "jane.smith@example.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

# Read all customer data
mycursor.execute('select * from customers')
myresult = mycursor.fetchall()

for i in myresult:
    print(i)
    
# Update a customer's email
sql = 'update customers set email = %s where id = %s'
val = ("updated.email@example.com", 1)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated.")

# Read the updated customer data
mycursor.execute('select * from customers where id = 1')
myresult  = mycursor.fetchone()

print("Updated customer:")
print(myresult)

# Delete a customer
sql = 'delete from customers where id = 0'
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()
print("Database connection closed.")