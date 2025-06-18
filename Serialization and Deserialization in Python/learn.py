import json
import pickle

""" 

# Serialize the object to a JSON string
data = {'name':'Alice', 'age': 30, 'city': 'Kampala'}
json_string = json.dumps(data)
with open('data.json', 'w') as file:
    json.dump(data, file)
    
# Deserialize the JSON string back into a Python object
data = json.load(json_string)
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

"""

data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}

# Serialize the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
    
# Deserialize the object from the file
with open('data.pkl', 'rb') as file: 
    loaded_data = pickle.load(file)
    print(loaded_data)