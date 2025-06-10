""" 

Exercise 2: File Handling with FileNotFoundError

Instructions:

Write a program that attempts to open and read data from a file specified by the user.
Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

"""

def file_name():
    filename = input('enter the name file: ')
    try:
        
        with open(filename, 'r') as file:
            content = file.read()
            print('the file content: ', content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
    
file_name()