""" 

Exercise 2: Multiple Inheritance Instruction:

Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods

"""

class Bird:
    def fly(self):
        print(f'the {self.name} is flying')
    
class Mammal:
    def run(self):
        print(f'the {self.name} is running')
    
class Bat(Bird, Mammal):
     def __init__(self, name):
        self.name = name

bat = Bat('bat')

bat.fly()
bat.run()