import json
#let's write to the json file 

data = {
    "name": "Alex",
    "age": 30,
    "hobbies": ["reading", "gaming"]
}

with open("pp.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ Data saved to pp.json")
