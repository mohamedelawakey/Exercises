"""

Exercise 3: Develop a function to check if a number is even or odd.

Instructions:

Define a function that takes one parameter, number.
Inside the function,check the remainder after dividing the number by 2 is equal to zero.
If the remainder is zero, the number is even. Print a message indicating the number is even.
If the remainder is not zero, the number is odd. Print a message indicating the number is odd.

"""

def even_odd(number):
    if number %2 == 0:
        print('even')
    else:
        print('odd')

even_odd(1)