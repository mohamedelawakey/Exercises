""" 

Exercise 2: Static Method for Utility Calculation Instruction:

Create a class Calculator with static methods for basic mathematical operations like addition and multiplication.
Implement static methods add() and multiply() to perform these operations.

"""

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

calc = Calculator()

print(calc.add(10, 20))
print(calc.multiply(10, 20))