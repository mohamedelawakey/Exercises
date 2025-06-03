""" 

Exercise 3: Write a program to generate a random set of numbers between 1 and ten.
Use set operations to remove duplicates and display the unique numbers.

"""

import random
random_numbers = [random.randint(1,10) for _ in range(15)]
unique_numbers = set(random_numbers)

print("Original numbers with duplicates:", random_numbers)
print("Unique numbers (no duplicates):", unique_numbers)