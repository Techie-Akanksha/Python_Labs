import json
from pathlib import Path
from abc import ABC, abstractmethod 

database = "school_database.json"
data = {"students": [], "teachers": []}

if Path(database).exists():
    with open(database, "r") as file:
        content = file.read()
        if content:
            data = json.loads(content)

def save_data():
    with open(database, "w") as file:
        json.dump(data, file, indent=4)

class Registration(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

class Student(Registration):
    def get_roles(self):
        return "Student"

    def register(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        email = input("Enter student email: ")
        roll_no = input("Enter student roll number: ")

        if not Registration.validate_email(email):
            print("Invalid email format.")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("Student with this roll number already exists.")
                return
        

        student_data = {
            "name": name, 
            "age": age,
            "email": email,
            "roll_no": roll_no,
            "grades": {}
        }
        data["students"].append(student_data)
        save_data()
        print("Student registered successfully.")

    def show_details(self):
        # roll_no = input("Enter student roll number: ")
        # for student in data["students"]:
        #     if student["roll_no"] == roll_no:
        #         print(f"Name: {student['name']}")
        #         print(f"Age: {student['age']}")
        #         print(f"Email: {student['email']}")
        #         print(f"Roll Number: {student['roll_no']}")
        #         print(f"Grades: {student['grades']}")
        #         return
        # print("Student not found.")
        pass

print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show a student details")
print("press 5 to show a teachers details")

choice =  int(input("Enter your choice:- "))

if choice == 1:
    student = Student()
    student.register()