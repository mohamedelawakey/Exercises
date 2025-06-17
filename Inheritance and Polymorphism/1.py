""" 

Exercise 1: Single Inheritance Instruction:

Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape and overrides calculate_area() to calculate the area of a rectangle.

"""

class Shape:
    def calculate_area(self):
        print("Area calculation not defined for generic shape.")

class Rectangle(Shape):
    def calculate_area(self, length, wigth):
        print(f'the area of rectangle is: {length * wigth}')
    
shape = Shape()
rectangle = Rectangle()

shape.calculate_area()
rectangle.calculate_area(10,20)