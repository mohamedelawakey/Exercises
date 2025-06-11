""" 

Exercise 2: Writing Basic Unit Tests

Instruction:

Use the unittest module in Python to create a test case for the buggy function from Exercise 1.
Write test methods to check different scenarios (e.g., valid input, invalid input) and verify expected behavior.

"""

import unittest

def square(n):
    return n * n 

class testSquare(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(4), 16)
    
    def test_negative(self):
        self.assertEqual(square(-3), 9)
        
    def test_zero(self):
        self.assertEqual(square(0), 0)
        
    def test_type_error(self):
        with self.assertEqual(TypeError):
            square('a')
            
if __name__ == "__main__":
    unittest.main()