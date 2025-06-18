""" 

Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

Takes a dictionary (data) and a filename (filename) as input.
Serializes the dictionary to a JSON file with the given filename.
Deserializes the JSON file back into a dictionary.
Returns the deserialized dictionary.

"""
import json

def process_json(data: dict, filename: str) -> dict:
    with open(filename, 'w') as file:
        json.dump(data, file)
        
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    
    return loaded_data