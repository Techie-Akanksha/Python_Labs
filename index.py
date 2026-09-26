# # ⭐Topic - APIs + requests

# Bilkul. 👍 Since **APIs tumhare liye new hain**, is topic ko sirf `requests.get()` tak nahi rakhenge. Tumhare **Python interview + AI project** ke liye jitna actually required hai, utna complete karenge—HTTP basics, API, JSON, GET/POST, parameters, headers, status codes, authentication, error handling, aur tumhare PDF Q&A project mein API ka role.

# # 🌐 Python APIs — From Scratch

# Pehle ek simple idea samjho:

# > **API ek bridge hai jo ek software ko doosre software se communicate karne deta hai.**

# Example:

# ```text
# Your Python Program
#        ↓
#       API
#        ↓
#   Another Server
#        ↓
#      Response
#        ↓
# Your Python Program
# ```

# Tumhara Python program directly doosre application's internal code ko access nahi karta. Woh API ke through request karta hai.

# ---

# # 1. Real-life example

# Maan lo tum restaurant app bana rahi ho.

# Tumhare app ko restaurant ke server se menu chahiye.

# Tumhara app bolega:

# > "Mujhe restaurant ka menu do."

# Server response dega:

# ```json
# {
#     "restaurant": "ABC",
#     "items": [
#         "Pizza",
#         "Burger",
#         "Pasta"
#     ]
# }
# ```

# Yahi communication API ke through hoti hai.

# ### Simple analogy

# Restaurant mein:

# ```text
# You → Waiter → Kitchen → Waiter → You
# ```

# Software mein:

# ```text
# Python → API → Server → API → Python
# ```

# API = **communication interface**

# ---

# # 2. API ka full form

# **API = Application Programming Interface**

# Interview mein:

# > **An API is an interface that allows different software applications to communicate and exchange data with each other.**

# Bas itna definition interview ke liye enough hai.

# ---

# # 3. API aur website mein difference

# Ye important hai.

# Jab tum browser mein website open karti ho:

# ```text
# Browser → Server → HTML page
# ```

# API mein:

# ```text
# Python → API → Data
# ```

# API generally structured data return karti hai, commonly **JSON**.

# Example:

# ```json
# {
#     "name": "Ash",
#     "age": 24
# }
# ```

# Python usko:

# ```python
# {
#     "name": "Ash",
#     "age": 24
# }
# ```

# ke form mein use kar sakta hai.

# ---

# # 4. HTTP kya hai?

# Ab ek important term:

# **HTTP = HyperText Transfer Protocol**

# Ye rules define karta hai ki client aur server ke beech communication kaise hogi.

# Usually:

# ```text
# Client
#   ↓
# HTTP Request
#   ↓
# Server
#   ↓
# HTTP Response
#   ↓
# Client
# ```

# ### Client kya hai?

# Jo request bhej raha hai.

# Tumhare case mein:

# ```python
# requests
# ```

# library use karke Python application client ban sakti hai.

# ### Server kya hai?

# Jo request receive karke response deta hai.

# ---

# # 5. Request kya hoti hai?

# Jab Python server ko kuch maangta ya bhejta hai, woh **request** hai.

# Example:

# ```python
# requests.get(url)
# ```

# Meaning:

# > "Server, mujhe ye resource/data do."

# ---

# # 6. Response kya hota hai?

# Server request process karne ke baad response bhejta hai.

# ```python
# response = requests.get(url)
# ```

# `response` mein server ka response aa jata hai.

# Response ke important parts:

# ```python
# response.status_code
# response.text
# response.json()
# ```

# ---

# # 7. GET request

# **GET = data retrieve karna.**

# Example:

# ```python
# import requests

# response = requests.get(url)
# ```

# Conceptually:

# ```text
# Python
#   ↓
# GET /users
#   ↓
# Server
#   ↓
# Users data
# ```

# GET ka main purpose:

# > **Retrieve data**

# Example APIs:

# ```text
# Get users
# Get products
# Get weather data
# Get student records
# ```

# ---

# # 8. `response.status_code`

# Server batata hai request successful hui ya nahi.

# Example:

# ```python
# print(response.status_code)
# ```

# Important status codes:

# | Code | Meaning |
# |---|---|
# | `200` | OK / Success |
# | `201` | Created |
# | `400` | Bad Request |
# | `401` | Unauthorized |
# | `403` | Forbidden |
# | `404` | Not Found |
# | `500` | Internal Server Error |

# ### Memory trick

# ```text
# 2xx → Success
# 4xx → Client/request problem
# 5xx → Server problem
# ```

# You don't need to memorize every HTTP code for fresher interviews. These are enough.

# ---

# # 9. `response.text`

# Suppose server returns:

# ```json
# {
#     "name": "Ash",
#     "age": 24
# }
# ```

# Then:

# ```python
# print(response.text)
# ```

# gives the response body as **text/string**.

# Important:

# ```python
# response.text
# ```

# → text/string representation

# ---

# # 10. `response.json()`

# Suppose API returns:

# ```json
# {
#     "name": "Ash",
#     "age": 24
# }
# ```

# Then:

# ```python
# data = response.json()
# ```

# Python converts the JSON response into a Python object.

# Conceptually:

# ```text
# JSON response
#       ↓
# response.json()
#       ↓
# Python dictionary
# ```

# Then:

# ```python
# print(data["name"])
# ```

# Output:

# ```text
# Ash
# ```

# ### Important connection with what you already learned

# You already learned:

# ```python
# json.loads()
# ```

# and:

# ```python
# json.dumps()
# ```

# `response.json()` is a convenient way of decoding the JSON response received from an HTTP API into a Python object.

# ---

# # 11. Let's understand complete GET flow

# ```python
# import requests

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("API request failed")
# ```

# Execution flow:

# ### Step 1

# ```python
# import requests
# ```

# Python loads the `requests` library.

# ### Step 2

# ```python
# response = requests.get(url)
# ```

# Python sends an HTTP GET request.

# ### Step 3

# Server processes request.

# ### Step 4

# Server sends response.

# ### Step 5

# Response object is stored in:

# ```python
# response
# ```

# ### Step 6

# ```python
# response.status_code
# ```

# checks whether request succeeded.

# ### Step 7

# If `200`:

# ```python
# response.json()
# ```

# converts JSON response into Python data.

# ### Step 8

# We can now work with that data.

# ---

# # 12. API endpoint kya hota hai?

# This word you'll hear constantly.

# Suppose API has:

# ```text
# https://api.example.com/users
# ```

# This is an **endpoint**.

# An endpoint is a specific URL through which an API provides a particular resource/function.

# For example:

# ```text
# /users
# /products
# /orders
# /login
# ```

# Conceptually:

# ```text
# Base URL
#    +
# Endpoint
#    ↓
# API resource
# ```

# ---

# # 13. URL samjho

# Example:

# ```text
# https://api.example.com/users
# ```

# Break it down:

# ```text
# https://        → protocol
# api.example.com → server/domain
# /users          → endpoint/path
# ```

# You don't need deep networking knowledge right now.

# ---

# # 14. Query Parameters

# Suppose API has:

# ```text
# /users?name=Ash
# ```

# Here:

# ```text
# ?name=Ash
# ```

# is a query parameter.

# Python mein:

# ```python
# params = {
#     "name": "Ash"
# }

# response = requests.get(url, params=params)
# ```

# `requests` URL conceptually bana dega:

# ```text
# /users?name=Ash
# ```

# Another example:

# ```python
# params = {
#     "page": 2,
#     "limit": 10
# }

# response = requests.get(url, params=params)
# ```

# Meaning:

# > Give me page 2 with 10 records.

# ---

# # 15. POST request

# GET mostly:

# > **Give me data.**

# POST commonly:

# > **Here is some data; process/create something.**

# Example:

# ```python
# payload = {
#     "name": "Ash",
#     "age": 24
# }

# response = requests.post(
#     url,
#     json=payload
# )
# ```

# Flow:

# ```text
# Python
#   ↓
# POST request
#   +
# JSON data
#   ↓
# Server
#   ↓
# Process data
#   ↓
# Response
# ```

# For example, creating a new user.

# ---

# # 16. GET vs POST

# This is an extremely common interview question.

# | GET | POST |
# |---|---|
# | Retrieve data | Send/create/process data |
# | Usually no request body | Commonly sends request body |
# | Parameters often in URL | Data commonly in body |
# | Example: get users | Example: create user |

# ### Interview answer

# > **GET is generally used to retrieve data, while POST is commonly used to send data to a server for processing or creating a resource.**

# Don't say "GET can never send data"—query parameters can be sent with GET.

# ---

# # 17. Headers

# Now one of the most important things for your AI project.

# A request can contain **headers**.

# Headers provide additional information about the request.

# Example:

# ```python
# headers = {
#     "Authorization": "Bearer YOUR_API_KEY",
#     "Content-Type": "application/json"
# }
# ```

# Then:

# ```python
# response = requests.post(
#     url,
#     headers=headers,
#     json=payload
# )
# ```

# Think:

# ```text
# Request
# │
# ├── URL
# ├── Method
# ├── Headers
# └── Body
# ```

# ---

# # 18. API Key / Authentication

# Suppose you are using an AI API.

# The provider doesn't want random people using the service.

# So you receive an **API key**.

# Conceptually:

# ```text
# Python
#    ↓
# API request
#    ↓
# "Here is my API key"
#    ↓
# Server verifies
#    ↓
# Response
# ```

# Usually we DON'T write the actual API key directly in source code.

# Bad:

# ```python
# api_key = "sk-something-secret"
# ```

# Better:

# ```python
# import os

# api_key = os.getenv("API_KEY")
# ```

# And `.env`:

# ```text
# API_KEY=your_secret_key
# ```

# This connects directly to what you've already used in your PDF Q&A project:

# ```python
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("GROQ_API_KEY")
# ```

# ---

# # 19. Why `.env`?

# Because API keys are **secrets**.

# You don't want this:

# ```text
# GitHub
#    ↓
# Your source code
#    ↓
# API KEY exposed
# ```

# Instead:

# ```text
# .env
#    ↓
# Secret API key
#    ↓
# os.getenv()
#    ↓
# Python program
# ```

# And `.env` should normally be added to `.gitignore`.

# ---

# # 20. Error Handling

# Real API calls can fail.

# Internet problem:

# ```text
# ConnectionError
# ```

# Timeout:

# ```text
# Timeout
# ```

# Invalid URL:

# ```text
# Request error
# ```

# Server returns:

# ```text
# 404
# 500
# ```

# So production-style code should handle errors.

# Example:

# ```python
# import requests

# try:
#     response = requests.get(url, timeout=10)

#     response.raise_for_status()

#     data = response.json()
#     print(data)

# except requests.exceptions.RequestException as e:
#     print("API request failed:", e)
# ```

# ### `raise_for_status()`

# This is useful.

# If response is:

# ```text
# 200
# ```

# nothing happens.

# If response is:

# ```text
# 404
# 500
# ```

# it raises an HTTP-related exception.

# So:

# ```python
# response.raise_for_status()
# ```

# means approximately:

# > "If the HTTP response indicates an error, raise an exception."

# ---

# # 21. Why `timeout`?

# Imagine your program sends request:

# ```python
# requests.get(url)
# ```

# and server never responds.

# Your program could keep waiting.

# Instead:

# ```python
# requests.get(url, timeout=10)
# ```

# means:

# > Don't wait indefinitely; use a timeout.

# This is important in real applications.

# ---

# # 22. Now connect this to YOUR AI PDF Q&A project

# Your project has roughly this architecture:

# ```text
#               PDF
#                ↓
#         PyPDF2 extracts text
#                ↓
#           Text chunks
#                ↓
#       Sentence Transformer
#                ↓
#           Embeddings
#                ↓
#              FAISS
#                ↓
#         Relevant chunks
#                ↓
#          User Question
#                ↓
#           Groq API
#                ↓
#           LLM Response
#                ↓
#           Streamlit UI
# ```

# The **Groq API** part is where your Python application communicates with an external AI service.

# So the concept you are learning now is directly connected to your project.

# ---

# # 23. The most important API vocabulary

# You should be comfortable with these:

# ```text
# API
# HTTP
# Client
# Server
# Request
# Response
# Endpoint
# GET
# POST
# Status code
# Headers
# Query parameters
# Request body / payload
# JSON
# Authentication
# API key
# Timeout
# Exception handling
# ```

# You **do not need deep networking** like TCP packet structure, DNS internals, sockets, etc. for your current fresher Python goal.

# ---

# # 🎤 Interview Questions You Should Know

# ### Q1. What is an API?

# > An API is an interface that allows different software applications to communicate and exchange data.

# ### Q2. What is an HTTP request?

# > An HTTP request is a message sent by a client to a server to retrieve or send information.

# ### Q3. What is a response?

# > An HTTP response is the data and status information returned by the server after processing a request.

# ### Q4. GET vs POST?

# > GET is generally used to retrieve data, while POST is commonly used to send data for processing or resource creation.

# ### Q5. What is JSON?

# > JSON is a lightweight data-interchange format commonly used for communication between applications and APIs.

# ### Q6. What does `response.json()` do?

# > It parses a JSON response and converts it into a corresponding Python object, such as a dictionary or list.

# ### Q7. What is an API key?

# > An API key is a credential used by an API provider to identify or authenticate an application making API requests.

# ### Q8. Why use environment variables for API keys?

# > To keep sensitive credentials out of source code and reduce the risk of exposing them.

# ---

# # 🧠 Now YOUR Challenge

# Don't look back at the explanation. Try to reason through this:

# ```python
# import requests

# url = "https://api.example.com/users"

# params = {
#     "page": 2
# }

# headers = {
#     "Authorization": "Bearer SECRET_KEY"
# }

# response = requests.get(
#     url,
#     params=params,
#     headers=headers,
#     timeout=10
# )

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Request failed")
# ```

# Explain this in your preferred **memory/execution-flow style**:

# ### Step 1:
# What does `requests.get()` send to the server?

# ### Step 2:
# What are `params` doing?

# ### Step 3:
# What are `headers` doing?

# ### Step 4:
# What is stored inside `response`?

# ### Step 5:
# What does `response.json()` do?

# ### Step 6:
# Why do we check `status_code == 200`?

# Once you explain this correctly, **API basics will be done**, and we'll move to the remaining high-value Python topic: **decorators**.