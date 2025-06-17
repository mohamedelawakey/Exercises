""" 

Exercise 3: Class Inheritance Instructions:

Create a base class Animal with methods like eat and sleep.
Create a subclass Dog that inherits from Animal and adds a method bark.
Create instances of both classes and demonstrate method inheritance.

"""

class Animal:
    def eat(self):
        print('the animal is eat')
    
    def sleep(self):
        print('the animal is sleeping')
        
class Dog(Animal):
    def bark(self):
        print('the dog is barking')

animal_1 = Animal()
dog_1 = Dog()

animal_1.eat()
animal_1.sleep()
dog_1.bark()
dog_1.eat()
dog_1.sleep()