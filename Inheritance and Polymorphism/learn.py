# Single Inheritance

class Animal():
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print('Generic animal sound')
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("Woof!")

lassie = Dog("Lassie")
lassie.make_sound()

########################################################################################

# Multiple Inheritance

class Flyer():
    def fly(self):
        print("Flying...")
    
class Swimmer:
    def swim(self):
        print("Swimming...")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()

########################################################################################

# Multilevel Inheritance

class Vehicle:
    def move(self):
        print("Moving...")
    
class Car(Vehicle):
    pass

class ElectricCar(Car):
    def charge(self):
        print("Charging...")
    
tesla = ElectricCar()
tesla.move()
tesla.charge()

########################################################################################

# Method Resolution Order (MRO)

class A:
    def greet(self):
        return "Hello from class A"
class B(A):
    def greet(self):
        return "Hello from class B"
class C(A):
    def greet(self):
        return "Hello from class C"
class D(B,C):
    pass

obj = D()
print(obj.greet())
