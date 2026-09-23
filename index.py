# ⭐ JSON Handling

# JSON (JavaScript Object Notation) ka use applications ke beech data exchange karne ke liye bahut hota hai.

# Python dictionary vs JSON
# Python: Ye Python dictionary hai.
student = {
    "name": "Ash",
    "age": 24,
    "skills": ["Python", "SQL"]
}

# JSON mein same data:

{
    "name": "Ash",
    "age": 24,
    "skills": ["Python", "SQL"]
}

# Dekhne mein same lagta hai, but important difference:

# Dictionary Python ka object hai; JSON ek data format/string representation hai.

# 2. json module

import json

# Dictionary → JSON

student = {
    "name": "Ash",
    "age": 24
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))

# json.dumps() means: Python object → JSON string

# dict
#  ↓
# json.dumps()
#  ↓
# JSON string

# 3. JSON → Python object

json_data = '{"name": "Ash", "age": 24}'

student = json.loads(json_data)

print(student)
print(type(student))

# json.loads(): JSON string → Python object

# JSON string
#  ↓
# json.loads()
#  ↓
# Python dict

# S = String
# dumps → Python → String
# loads → String → Python

data = {
    "name": "Ash",
    "age": 24
}

result = json.dumps(data)

print(type(data))
print(type(result))

new_data = json.loads(result)

print(type(new_data))
print(new_data["name"])

# data
#  ↓
# Python dictionary
#  ↓ json.dumps()
# JSON string
#  ↓
# result
#  ↓ json.loads()
# Python dictionary
#  ↓
# new_data
#  ↓
# new_data["name"]
#  ↓
# Ash


# ⭐ Interview-ready

# json.dumps()

# Converts a Python object into a JSON-formatted string.

# json.loads()

# Converts a JSON-formatted string into a Python object.


# Real projects mein tumhe ye bhi milega:

# json.dump()
# json.load()

# Difference:

# dumps → string
# loads → string

# dump → file
# load → file

with open("hospital_data.json", "w") as file:
    json.dump(data, file)
# Yahan dictionary directly JSON file mein write ho rahi hai.

with open("student.json", "r") as file:
    data = json.load(file)
# Yahan JSON file ka data Python object mein aa raha hai.

