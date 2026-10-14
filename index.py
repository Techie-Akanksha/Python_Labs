#Topic - Rest API

# ⭐ API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. REST (Representational State Transfer) is an architectural style for designing networked applications, and it uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

# ⭐Endpoints are specific URLs that represent resources in a RESTful API. Each endpoint corresponds to a specific resource or collection of resources, and clients can interact with these endpoints using standard HTTP methods such as GET, POST, PUT, and DELETE.

#⭐ API Fundamentals:

# GET is generally used to retrieve data.
# POST is commonly used to submit data for processing or create a resource.
# PUT is generally used to replace a resource.
# PATCH is generally used to partially update a resource.
# DELETE is used to delete a resource.

# ⭐Lesson 2: HTTP status codes
# We have discussed:
# - 200 OK
# - 201 Created
# - 400 Bad Request
# - 401 Unauthorized
# - 403 Forbidden
# - 404 Not Found
# - 429 Too Many Requests
# - 500 Internal Server Error

# ⭐ Lesson 3: HTTP request structure
# We have introduced:
# - HTTP method and URL
# - Request headers
# - Request body
# - Response body
# - JSON
# - Content-Type: application/json

# ⭐ Lesson 4: URL parameters
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



# ⭐ Next concept: Query parameters

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


# ⭐ Request Body
# Isliye POST request mein data Request Body mein jaata hai.

# Client

# POST /summarize

# Headers
# Content-Type: application/json

# Body
# {
#    "transcript": "Today we discussed..."
# }

# Server body read karta hai.
# Phir summarize karta hai.
# Phir response bhejta hai.

#⭐ POST Request
response = requests.post(
    url,
    json={
        "title": "REST API Learning",
        "completed": False
    }
)

# Humne json= use kiya.
# Why?
# Because requests automatically:
# - JSON create karta hai.
# - Content-Type: application/json header set karta hai.
# - Server ko JSON body bhejta hai.

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "Learning REST API",
        "body": "This is my first POST request",
        "userId": 1
    }
)

print("Status Code:", response.status_code)
if response.status_code == 201:
    print("Post created successfully!")
else:
    print("Failed to create post. Status code:", response.status_code)

data = response.json()
print("Response id:", data["id"])
print("Response title:", data["title"])

# Interview-ready:
# “I implemented a POST request using Python's requests library to send a JSON payload to a test API. I inspected the HTTP response and parsed the returned JSON data.”

# Request body prepare hoti hai
# json={...} tumhari Python dictionary ko JSON format mein serialize karta hai.


# 2

# POST request send hoti hai
# Request URL /posts hai. Data request body mein jaata hai, aur JSON content type header set hota hai.


# 3

# Server response deta hai
# JSONPlaceholder normally 201 Created aur submitted fields ke saath ek generated id return karta hai.

# Question: Why do we usually use POST requests for submitting data?

# Answer:
# "A POST request is used to send data from the client to the server for processing or creating a new resource. The data is typically sent in the request body, often in JSON format."


#⭐ timeout — server slow ho toh kya karein?

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=5)

print(response.status_code)

# timeout=5: connection ya response wait ke liye timeout limit set karta hai.

# Agar timeout exceed hota hai, requests ek exception raise kar sakta hai: requests.exceptions.Timeout.

# Yeh HTTP status code nahi hai. Is situation mein response object milna zaroori nahi, kyunki request ko usable response mila hi nahi.


# Interview answer: “I use the timeout parameter to prevent HTTP requests from waiting indefinitely when a server is slow or unresponsive.”

# ⭐ raise_for_status() — HTTP error ko detect karna
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=5)
response.raise_for_status()

data = response.json()
print(data["title"])

# Samjho execution flow:
# requests.get(url, timeout=5)


# response.raise_for_status()

# Success path
# HTTP 2xx/3xx response
# Next line execute ho sakti hai.


# Error path
# HTTP 4xx/5xx response
# HTTPError raise hota hai.

# Important: raise_for_status() har non-2xx status ko error nahi maanta. Yeh HTTP 4xx aur 5xx responses ke liye HTTPError raise karta hai. Agar tumhe specifically 201 chahiye, toh us status ko separately check karna padega.



# ⭐ Exception handling — try and except
# Ab maan lo teen problems ho sakti hain:
# - Server slow hai → timeout.
# - Server 404 ya 500 return karta hai → HTTP error.
# - Internet ya connection mein problem hai → connection error.


import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    print("Title:", data["title"])

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

except requests.exceptions.ConnectionError:
    print("Could not connect to the server.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


#   Code ka mental model
# - try: woh code jisme failure ho sakta hai.
# - except: specific failure aaye toh kya karna hai.
# - as error: exception ki details ko error variable mein rakhna.
# - RequestException: Requests library ke kai request-related errors ke liye general parent exception.

# ⭐ improvement: Tumhare current exception handling code mein do additional cases consider karne chahiye:
# Lekin production-level code mein do additional cases consider karenge:
# - Invalid JSON: Server successful HTTP status de sakta hai, lekin response body valid JSON na ho. response.json() decoding error raise kar sakta hai, jise tumhare current handlers explicitly handle nahi karte.
# - Unexpected response structure: Valid JSON mein title key na ho, toh data['title'] par KeyError aa sakta hai.


# Q2. Agar request timeout ho jaye, toh kya response.status_code check karna hamesha possible hoga?
# Request timeout hone par usable Response object milna zaroori nahi. Isliye timeout handler mein response.status_code assume nahi karna chahiye.

# Q3. raise_for_status() call nahi kiya, aur server 404 deta hai. Kya requests.get() normally Response object return kar sakta hai?
# requests.get() normally 404 par bhi Response object return karta hai. raise_for_status() automatic nahi hota; tumhe khud call karna padta hai.