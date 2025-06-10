# Custom Exceptions

""" 

class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""
    def __init__(self,item_name):
        self.item_name = item_name
    
    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."
    
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  
    "grapes": 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")
            
try:
    purchase_item("apple", 3) 
    purchase_item("orange", 1)  
    purchase_item("watermelon", 1) 
except OutOfStockError as e:
    print(e)
    
"""

