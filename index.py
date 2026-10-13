#Topic - Rest API

# API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. REST (Representational State Transfer) is an architectural style for designing networked applications, and it uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

# Endpoints are specific URLs that represent resources in a RESTful API. Each endpoint corresponds to a specific resource or collection of resources, and clients can interact with these endpoints using standard HTTP methods such as GET, POST, PUT, and DELETE.

# API Fundamentals:

# GET is generally used to retrieve data.
# POST is commonly used to submit data for processing or create a resource.
# PUT is generally used to replace a resource.
# PATCH is generally used to partially update a resource.
# DELETE is used to delete a resource.

# Lesson 2: HTTP status codes
# We have discussed:
# - 200 OK
# - 201 Created
# - 400 Bad Request
# - 401 Unauthorized
# - 403 Forbidden
# - 404 Not Found
# - 429 Too Many Requests
# - 500 Internal Server Error

# Lesson 3: HTTP request structure
# We have introduced:
# - HTTP method and URL
# - Request headers
# - Request body
# - Response body
# - JSON
# - Content-Type: application/json

# Lesson 4: URL parameters
# We have introduced:
# - Path parameters, such as /meetings/101.
# - Query parameters, such as /meetings?status=completed.


# Step 1: Python client
# requests.get(url) execute hota hai

# Step 2: HTTP request
# Request network ke through server tak jaati hai

# Step 3: API server
# Request process hoti hai aur response prepare hota hai

# Step 4: HTTP response
# Status code, headers aur optionally response body return hoti hai

# Step 5: Python receives the response
# Response object ko inspect kar sakte hain

# Expression	Kya milega?
# response.status_code	HTTP status code, jaise 200
# response.headers	Response headers
# response.text	Response body as text
# response.json()	JSON body ko Python data structure mein convert karta hai, agar body valid JSON ho


# Q.
# 1. requests library import karo.
# 2. https://jsonplaceholder.typicode.com/posts/1 par GET request bhejo.
# 3. Response ko variable mein store karo.
# 4.Status code print karo.
# 5.JSON response parse karke print karo.


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
print(response.status_code)
print(response.json())



#Q.2  Your next exercise — code khud modify karo
# Abhi main complete solution nahi dunga. Apne existing index.py ko modify karke ye teen tasks complete karo:
# 1. Status code print karne ke bajaye Status Code: 200 jaisa labelled output print karo.
# 2. JSON response ko data variable mein store karo.
# 3. Sirf post ka title print karo, poori dictionary nahi.

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
if response.status_code == 200:
    print("Request successful!")
else:
    print("Request failed with status code:", response.status_code)

print("Status Code:", response.status_code)
data = response.json()
print("Title:", data["title"])



# Next concept: Query parameters

# API endpoint:
# https://jsonplaceholder.typicode.com/posts?userId=1

# Yahan:
# - /posts resource collection hai.
# - userId=1 query parameter hai.
# - ? query parameters ko URL path se separate karta hai.

# Python mein query parameters ko manually URL mein jodne ke bajaye params argument use kar sakte hain:

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

# requests query string construct karega aur request mein userId=1 bhejega.
# Ye approach multiple parameters aur special characters ke liye bhi useful hai.


# Q.independent coding exercise
# Apne index.py ko modify karo. Is baar endpoint /posts use karna hai, aur sirf userId=1 ki posts retrieve karni hain.
# Requirements:
# 1. requests.get() mein params argument use karo.
# 2. Status code print karo.
# 3. Response JSON ko data variable mein store karo.
# 4. Total returned posts print karo using len(data).
# 5. Pehli post ka title print karo.


response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
print("Status Code:", response.status_code)
data = response.json()
print("Number of posts for userId=1:", len(data))
print("First Titles of posts for userId=1:", data[0]["title"])