class Animal:
    def make_sound(self):
        print("Generic animal sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

animals = [Dog(), Animal()]
for animal in animals:
    animal.make_sound()
    
########################################################################################

# Polymorphic Behavior with Duck Typing

class Dusk:
    def quack(self):
        return "Duck quacks"
    
class Person:
    def quack(self):
        return "Person imitates duck"

def make_sound(obj):
    return obj.quack()

duck_obj = Dusk()
person_obj = Person()

print(make_sound(duck_obj))
print(make_sound(person_obj))