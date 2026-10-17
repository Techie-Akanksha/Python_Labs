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