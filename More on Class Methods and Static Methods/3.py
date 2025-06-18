""" 

Exercise 3: Class Method for Factory Creation Instruction:

Create a class Person with attributes name and age.
Implement a class method create_child() to create a new instance representing a child with age set to 0.

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)

child = Person.create_child("Sara")
print(child.name) 
print(child.age) 