import json

def save_product(product: dict, filename: str):
    with open(filename, 'w') as file:
        json.dump(product, file)
    
def load_product(filename: str) -> dict:
    with open(filename, 'r') as file:
        return json.load(file)
    
def update_price(filename: str, new_price: float):
    with open(filename, 'r') as file:
        product = json.load(file)
        
    product['price'] = new_price
    
    with open(filename, 'w') as file:
        json.dump(product, file)