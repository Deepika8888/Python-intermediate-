#let's read from a json file 

import json 

with open ("pp.json", 'r') as file:
    loaded_data = json.load(file)

print("Data from json file:")
print(loaded_data)
