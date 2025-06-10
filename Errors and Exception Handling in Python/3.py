""" 

Exercise 3: Custom Exception

Instructions:

Create a custom exception class called ValueTooHighError that inherits from the Exception class.
Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

"""

class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return f"it's wrong sorry the {self.number} is greater than 100"

try:
    number = int(input('enter a number: '))
    
    if number > 100:
        raise ValueTooHighError(number)
    print(f"{number} is valid and less than or equal to 100.")

except ValueTooHighError as a:
    print(a)

except TypeError:
    print("Error: Please enter a valid integer.")