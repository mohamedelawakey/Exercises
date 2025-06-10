""" 

Exercise 1: Understanding the Importance of Testing

Instruction:

Write a small Python function (e.g., a function to calculate the square of a number)
and intentionally introduce a bug (e.g., incorrect calculation logic).

"""

import unittest

def square(n):
    return n * 3

class test_Square(unittest.TestCase):
    def test_square_of_4(self):
        self.assertEqual(square(4), 16)

if __name__ == "__main__":
  unittest.main()