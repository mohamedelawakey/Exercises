""" 

Exercise 1: Creating and Using Modules

Instructions:

1. Create a custom Python module named calculator.py that contains functions for basic arithmetic operations
(addition, subtraction, multiplication, division).
2. Create functions add, subtract, multiply, and divide in the calculator.py module.
3. Import the calculator module into a separate Python script main.py and use its functions to perform arithmetic operations on numbers like 5 and 3.

"""

def add(n1, n2):
    print(n1 + n2)

def subtract(n1, n2):
    print(n1 - n2)

def multiply(n1, n2):
    print(n1 * n2)

def divide(n1, n2):
    
    if n2 == 0:
        print("you can't devide with 0")
    else:
        print(n1 / n2)

