""" 

Exercise 3: Polymorphism with Duck Typing Instruction:

Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.

"""

class Dog:
    def make_sound(self):
        print('the Dog is hoooooow')
class Cat:
    def make_sound(self):
        print('the Cat is moooooow')
class Bird:
    def make_sound(self):
        print('the Bird is sooooow')
    
def let_them_speak(list_odj):
    for animal in list_odj:
        animal.make_sound()

animals = [Dog(), Cat(), Bird()]
let_them_speak(animals)