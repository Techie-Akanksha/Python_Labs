import requests

url = "https://jsonplaceholder.typicode.com/users"

student = {
    "name": "Ash",
    "age": 24
}

response = requests.post(
    url,
    json=student
)

print(response.status_code)
print(response.json())


# GET is generally used to retrieve data from an API, while POST is commonly used to submit data to the server, often for creating a new resource. In Python requests, JSON data can be sent using the json parameter.


import requests

url = "https://jsonplaceholder.typicode.com/users"

student = {
    "name": "Ash",
    "age": 24
}

response = requests.post(url, json=student)

print(response.status_code)

data = response.json()

print(data["name"])


# 201 Created indicates that the server successfully processed the request and created a new resource.


# student
#    ↓
# Python dictionary
#    ↓
# json=student
#    ↓
# JSON request body
#    ↓
# POST request
#    ↓
# API Server
#    ↓
# Response Object
#    ↓
# response
#    ↓
# status_code → 201
#    ↓
# response.json()
#    ↓
# Python dictionary
#    ↓
# data["name"]
#    ↓
# "Ash"


# In a POST request, I can send a Python dictionary as a JSON request body using the json parameter. The server processes the request and returns a response object, which I can inspect using the status code and parse using response.json().