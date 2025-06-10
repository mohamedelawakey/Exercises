""" 

Exercise 1: Handling ZeroDivisionError

Instructions:

Write a program that takes two numbers as input from the user and divides the first number by the second number.
Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

"""

# way 1 :
""" 

def devision(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("you can't devision by zero")
    else:
        print(num1 / num2)

div = devision(20,10)
div2 = devision(20,0)

"""

# way 2 :

def devision(num1, num2):
    try:
        result = num1 / num2
        print(f'result = {result}')
    except ZeroDivisionError :
        print("sorry, you can't devide by 0")

try:
    num1 = int(input('enter number 1 : '))
    num2 = int(input('enter number 2 : '))
    devision(num1, num2)
except ValueError:
    print('Error: Please enter valid integers only.')