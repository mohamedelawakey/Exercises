import mysql.connector

# Connect to MySQL Database
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="mysql1234",  
            database="library"     
        )
        print("Connected to database")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to add a new book
def add_book(title, author, isbn):
    mydb = connect_to_db()
    if mydb is not None:
        mycursor = mydb.cursor()
        sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
        val = (title, author, isbn)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Book '{title}' by {author} added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

# Function to search for a book by title
def search_book_by_title(title):
    mydb = connect_to_db()
    if mydb is not None:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM books WHERE title LIKE %s"
        val = ('%' + title + '%',) 
        try:
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            if myresult:
                print(f"Books matching '{title}':")
                for book in myresult:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
            else:
                print(f"No books found with title '{title}'.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

# Function to list all books
def list_all_books():
    mydb = connect_to_db()
    if mydb is not None:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM books"
        try:
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if myresult:
                print("All books in the library:")
                for book in myresult:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
            else:
                print("No books available in the library.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

# Bonus: Function to delete a book by ID
def delete_book_by_id(book_id):
    mydb = connect_to_db()
    if mydb is not None:
        mycursor = mydb.cursor()
        sql = "DELETE FROM books WHERE id = %s"
        val = (book_id,)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            if mycursor.rowcount > 0:
                print(f"Book with ID {book_id} deleted successfully!")
            else:
                print(f"No book found with ID {book_id}.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

search_book_by_title("Catcher")

list_all_books()

delete_book_by_id(1)

list_all_books()