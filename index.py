import json
# ⭐ JSON File Handling

# ⭐ JSON file mein data read karna 
# Suppose student.json file mein ye data hai:

# {
#     "name": "Ash",
#     "age": 24,
#     "skills": ["Python", "SQL"]
# }

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["skills"])

# student.json
#      ↓
# open(..., "r")
#      ↓
# json.load(file)
#      ↓
# Python dictionary
#      ↓
# data
#      ↓
# data["name"]
#      ↓
# Ash

# ⭐ JSON file mein data write karna

import json

student = {
    "name": "Ash",
    "age": 24,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

#⭐ indent=4 ka purpose sirf JSON ko human-readable / nicely formatted banana hai.

# Python dictionary
#        ↓
# json.dump()
#        ↓
# JSON file

# 🎯 Challenge
# Assume students.json contains:
# [
#     {"name": "Ash", "age": 24},
#     {"name": "Rahul", "age": 22},
#     {"name": "Priya", "age": 25}
# ]

import json

with open("students.json", "r") as file:
    students = json.load(file)

print(type(students))
print(students[0]["name"])
print(students[2]["age"])

# print(type(students))
# Output: <class 'list'>

# Because the JSON starts with:
# [
#     {...},
#     {...},
#     {...}
# ]
# [ ] means JSON array → Python list.

# students is a list containing multiple dictionaries, where each dictionary represents one student's data using key-value pairs.