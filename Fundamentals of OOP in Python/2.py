""" 

Exercise 2: Creating a Product Catalog

Instruction:

Define a Product class with attributes like name, price, and quantity.
Implement a method to calculate the total value of products in stock.

"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity
    
    def calc_total_in_stock(self):
        print(f'the total value of products in stock = {self.price * self.quantity} $')

pr1 = Product('tea', 500, 1000)
pr1.calc_total_in_stock()