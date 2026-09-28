# First Real API Call
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data["name"])
print(data["email"])

# I use the requests library to send an HTTP GET request to an API endpoint. The server returns a response object containing the status code and response body. If the body is JSON, I can use response.json() to convert it into a Python object such as a dictionary or list.


# URL / Endpoint
#       ↓
# GET Request
#       ↓
# API Server
#       ↓
# Response Object
#       ↓
# Status Code + Body
#       ↓
# response.json()
#       ↓
# Python Dictionary/List
#       ↓
# Access data