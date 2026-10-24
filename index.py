# ⭐ Lesson: FastAPI learning

# ⭐ Topic: Request data and validation

#⭐ Lesson 1: Response Models and Advanced Validation

# 1: What is response_model?
# So far, you've used Student(BaseModel) to validate data coming into your API. FastAPI also lets you define the structure of data going out of your API.

# Client → API
# The client sends a student's name and age. Pydantic validates the incoming data.

# FastAPI endpoint
# Retrieves the requested student record.

# Response
# API → Client
# response_model validates and filters the returned data to match the declared output schema.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "Aarav", "age": 22},
    2: {"name": "Priya", "age": 23}
}

class Student(BaseModel):
    name : str
    age : int

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

# Here, response_model=Student tells FastAPI that the successful response should follow the Student schema.

# Why is this useful? It makes the response structure predictable and helps generate accurate API documentation. It can also filter out fields that aren't part of the declared model.

# Remember the difference:
# - student: Student — validates incoming request data.
# - response_model=Student — validates and shapes outgoing response data.

# 2: Validate values using Field

class Student(BaseModel):
    name: str
    age: int

# This checks the expected data types, but it doesn't restrict the age to a sensible range or the name to a particular length.

# Let's improve it:

from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=1, le=120)

# What these rules mean:
# Rule	Meaning
# min_length=2	Name must contain at least 2 characters
# max_length=50	Name cannot exceed 50 characters
# ge=1	Age must be greater than or equal to 1
# le=120	Age must be less than or equal to 120

# FastAPI uses Pydantic to validate these constraints automatically. Invalid input normally produces a 422 response before the endpoint function runs.

# These constraints apply wherever this Student model is used for request validation, including your POST and PUT endpoints.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=1, le=120)


class StudentResponse(BaseModel):
    student_id: int
    name: str
    age: int

students = {
    1: {"name": "Aarav", "age": 22},
    2: {"name": "Priya", "age": 23}
}


@app.get("/student/",response_model = StudentResponse, status_code=201)
def get_student(student_id:int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return students[student_id]

@app.post("/student/{student_id}", response_model = Student)
def create_student(student:Student):
    new_id = max(students.keys())+1

    students[new_id]= student.model_dump()

    return {
        "student_id": new_id,
        "name": student.name,
        "age": student.age
    }

# Let's understand the important lines:
# - student: Student — FastAPI validates the incoming JSON.
# - max(students.keys()) + 1 — generates the next ID. With existing IDs 1 and 2, the new ID is 3.
# - student.model_dump() — converts the validated Pydantic model into a Python dictionary.
# - students[new_id] = ... — saves the new record.
# - response_model=StudentResponse — defines the outgoing response structure.
# - status_code=201 — indicates successful resource creation.

# Interview explanation
# “I used Pydantic models to validate incoming student data and define the API response structure. The POST endpoint generates a student ID, stores the record, and returns a 201 Created status.”