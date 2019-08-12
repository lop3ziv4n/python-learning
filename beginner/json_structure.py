# JSON
import json

# Convert Python dictionary to JSON
product = {"name": "silla", "color": "blanco", "price": 80}
json_structure = json.dumps(product)
print(json_structure)

# Convert JSON to Python dictionary
product2 = json.load(json_structure)
print(product2)



