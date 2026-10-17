# ⭐ Lesson: FastAPI learning

# ⭐ Topic: FastAPI Fundamentals

# Lesson 1: Understand FastAPI and create your first API

# We'll learn three concepts today:
# 1. What FastAPI is and how it works.
# 2. How to install FastAPI and run a server.
# 3. How to create your first API endpoint.

# Concept 1: What is FastAPI?
# FastAPI is a Python framework used to build APIs. It allows other applications to communicate with your Python code over HTTP.

# For example, imagine you build an AI application that summarizes meeting transcripts. Instead of allowing users to access your Python function directly, you can expose it through an API.

# Client / Frontend
# Sends an HTTP request
    # |
# FastAPI application
# Receives the request and runs Python logic
    # |
# Data or AI model
# Processes the request when needed

# FastAPI vs requests
# You have already used the requests library. Understand this important difference:

# requests  |	FastAPI
# Sends HTTP requests to an API  |		Creates an API server
# Acts as an API client  |		Acts as an API provider
# requests.get(url)  |		@app.get("/")

# Interview answer:
# “FastAPI is a modern Python web framework used to build APIs. It supports request validation, automatic interactive API documentation, and Python type hints.”


# Concept 2: Install FastAPI
# Open your VS Code terminal or Windows PowerShell in your project folder.

# Step 1 — Create a project folder
# You can use your existing Python Labs folder or create a new folder called fastapi_learning.

# Step 2 — Create and activate a virtual environment
# Run these commands in PowerShell:
# python -m venv venv
# .\venv\Scripts\Activate.ps1


# If your virtual environment is already activated, don't create or activate another one.

# Step 3 — Install the required packages
# python -m pip install "fastapi[standard]"


# This installs FastAPI and the standard tools needed to run a development server.

# Concept 3: Create your first API

# Create a file named main.py.
# Write this code yourself rather than copying it without understanding it:


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first API"}

# Let's understand each line.

# - from fastapi import FastAPI — imports the FastAPI class.
# - app = FastAPI() — creates your application object.
# - @app.get("/") — registers a route that handles HTTP GET requests to /.
# - def home(): — defines the Python function that runs when this route is requested.
# - return {"message": "Welcome to my first API"} — returns a Python dictionary that FastAPI converts into a JSON response.


# Run your application
# In the terminal, run:
# fastapi dev main.py


# Once the server starts, open the local URL displayed in your terminal, usually http://127.0.0.1:8000.

# You should receive a JSON response similar to:
# {
#   "message": "Welcome to my first API"
# }

# Now open http://127.0.0.1:8000/docs.
# This is FastAPI's interactive Swagger documentation, where you can inspect and test your endpoints directly—so we can postpone Postman.


# Q1. requests vs FastAPI
# Correct. requests sends HTTP requests; FastAPI creates API endpoints.

# Q2. @app.get("/")
# Correct. It registers a GET route for the root URL /.


# Q3. app = FastAPI()
# Correct. It creates the application instance on which we register routes.

# Lesson 2: Routes, Path Parameters and Query Parameters

# Concept 1: Multiple routes
# An API can provide multiple endpoints for different purposes.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/about")
def about():
    return {"message": "This is my first API"}

# Here:
# - GET / calls the home() function.
# - GET /about calls the about() function.
# Each route connects an HTTP method and URL to a Python function.

# Concept 2: Path parameters
# Path parameters identify a particular resource.

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# If you visit /users/5, FastAPI passes 5 to the function and returns:
# {
#   "user_id": 5
# }

# Notice user_id: int. This is a type hint. FastAPI uses it to validate the input and convert valid values to integers.

# If you visit /users/abc, FastAPI returns a validation error, usually with status code 422, because abc is not a valid integer.

# Concept 3: Query parameters
# Query parameters pass optional filters or extra information in the URL.

@app.get("/products")
def get_products(category: str = "all", limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }

# Try these URLs:

# URL   |	Result
# /products   |		category = all, limit = 10
# /products?category=books   |		category = books, limit = 10
# /products?category=books&limit=5   |	category = books, limit = 5

# The ? starts the query string, and & separates multiple query parameters.

# Remember the difference:
# - Path parameter: identifies which resource you want, such as /users/5.
# - Query parameter: filters or modifies the result, such as /products?limit=5.

# Interview-ready explanation:
# “Path parameters identify a specific resource, while query parameters are commonly used to filter, sort, or limit API results. FastAPI uses Python type hints to validate incoming parameters.”
# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/about")
def about():
    return {"message": "This is my first API"}

@app.get("/students/{student_id}")
def get_user(student_id: int):
    return {"student_id": student_id}

@app.get("/courses")
def get_courses(course: str = "Python", limit: int = 5):
    return{
        "course": course,
        "limit" : limit
    }
# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐


# Code review
# GET / and GET /about
# Both routes return the expected dictionaries.


# GET /students/{student_id}
# Correct path parameter and integer type hint. Your function name get_user is valid, though get_student would describe its purpose more clearly.


# GET /courses
# Correct query parameters, default values, and response dictionary. Your spacing around the return dictionary is also valid Python.

# 2. Test your API in the browser

# If you haven't started your server, run this in your activated virtual environment:

# fastapi dev main.py

# Open http://127.0.0.1:8000/docs and test these endpoints.

# Try these requests
# GET
# /students/25

# Expected response: {"student_id": 25}


# GET
# /courses
# Expected defaults: course = Python, limit = 5.


# GET
# /courses?course=SQL&limit=3
# Expected response: {"course": "SQL", "limit": 3}


# 3. One important concept: what happens internally?
# When a request reaches /students/25, the execution flow is:
# 1. FastAPI matches the URL with the registered route.
# 2. It extracts "25" from the URL.
# 3. It validates and converts "25" to the integer 25.
# 4. It calls get_user(student_id=25).
# 5. The returned Python dictionary is serialized into a JSON response.
# This is useful for interviews because it explains more than just the syntax.

# Interview-ready answer:
# “FastAPI maps incoming HTTP requests to route functions. It extracts path and query parameters, validates them using Python type hints, executes the corresponding function, and serializes the returned data into a response.”

# Lesson 3 — Request bodies and POST endpoints

# Next, we'll learn how an API receives data from a client. This is essential for registration forms, creating database records, and sending input to AI models.

# Concept 1: GET vs POST
# - GET is commonly used to retrieve data.
# - POST is commonly used to submit data or create a resource.
# For example, a client may send a new student's name and age to your API.

# Concept 2: Pydantic models
# FastAPI commonly uses Pydantic models to define and validate JSON request bodies.

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int

# This defines the expected structure of the incoming data. It doesn't create a database table.

# Concept 3: Build a POST endpoint
# Add this code to your existing main.py:
# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }
# ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐

# Keep your existing routes and app = FastAPI() line. Add the BaseModel import near your other imports and put the model and endpoint at the top level, not inside another function.

# In /docs, expand POST /students and try this request body:
# {
#   "name": "Aarav",
#   "age": 22
# }

# FastAPI validates the incoming data against Student and returns the response.

# Q1. Purpose of BaseModel
# Correct. It defines the expected structure and validates incoming data. It does not automatically create a database table.

# Q2. Invalid age
# Correct. Sending "age": "hello" normally produces a 422 Unprocessable Entity response because the value cannot be validated as an integer.

# Q3. Purpose of POST
# Correct. POST commonly submits data to the server to create a resource or perform an operation.

# 2. Let's test your POST endpoint

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student
    }

# Step 1 — Start the server
# In the VS Code terminal, from your project directory, run:
# fastapi dev main.py

# Step 2 — Open the interactive API documentation
# Open this URL in your browser:
# http://127.0.0.1:8000/docs
# Find POST /students, expand it, and click Try it out.

# Step 3 — Send valid JSON
# Enter this in the request body:
# {
#   "name": "Aarav",
#   "age": 22
# }


# Click Execute.
# Your response should be similar to:
# {
#   "message": "Student created successfully",
#   "student": {
#     "name": "Aarav",
#     "age": 22
#   }
# }

# The HTTP status should normally be 200 OK, because we haven't explicitly configured a different success status code. FastAPI doesn't automatically save this student in a database; for now, the endpoint validates and returns the submitted data.

# Step 4 — Test invalid input
# Try changing the request body to:
# {
#   "name": "Aarav",
#   "age": "hello"
# }


# You should receive a validation error, usually status code 422. The function won't run because FastAPI rejects the request before calling it.

# Then try omitting the age field:
# {
#   "name": "Aarav"
# }


# This should also produce a validation error because age is a required field.

# 3. Understand what happens internally
# Client sends POST request
# JSON: name and age

# FastAPI validates the request
# Checks required fields and data types

# Valid input
# Calls create_student() and returns a response.


# Invalid input
# Returns a validation error without calling the function.

# Interview-ready explanation:
# “I used a Pydantic model to define the expected JSON request body. FastAPI validates the incoming data before executing the endpoint function and automatically returns validation errors for invalid input.”