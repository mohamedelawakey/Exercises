""" 

Exercise 1: Creating a Student Class

Instructions:

Define a Student class with attributes like name and age. Include a method to display student information.

"""

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def display_student_information(self):
        print(f'the name is {self.name} and the age is {self.age}')

std1 = Student('mohamed mostafa', 20)

std1.display_student_information()