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
        if not Registration.validate_email(email):
            print("Invalid email format.")
            return
        roll_no = input("Enter student roll number: ")


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
        roll_no = input("Enter student roll number: ")
        for student in data["students"]:
            if student["roll_no"] == roll_no:
                avg = sum(student["grades"].values()) / len(student["grades"]) if student["grades"] else 0
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Email: {student['email']}")
                print(f"Roll Number: {student['roll_no']}")
                print(f"Grades: {student['grades']}")
                print(f"Average Grade: {avg}")
                return
        print("Student not found.")
        pass

    def grade(self):
        roll_no = input("Enter student roll number:")
        subject = input("Enter subject:")
        grade = input("Enter grade:")
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                i["grades"][subject] = grade
                save_data()
                print("Grade added successfully.")
                return
        print("Student not found.")


class Teacher(Registration):
    def get_roles(self):
        return "Teacher"

    def register(self):
        name = input("Enter teacher name:")
        subject = input("Enter teacher subject:")
        email = input("Enter teacher email:")
        teacher_id = input("Enter teacher ID:")

        if not Registration.validate_email(email):
            print("Invalid email format.")
            return

        for i in data["teachers"]:
            if teacher_id == i["teacher_id"]:
                print("Teacher with this ID already exists.")
                return

        teacher_data = {
            "name": name,
            "subject": subject,
            "email": email,
            "teacher_id": teacher_id
        }
        data["teachers"].append(teacher_data)
        save_data()
        print("Teacher registered successfully.")

    def show_details(self):
        teacher_id = input("Enter teacher ID: ")
        for teacher in data["teachers"]:
            if teacher["teacher_id"] == teacher_id:
                print(f"Name: {teacher['name']}")
                print(f"Subject: {teacher['subject']}")
                print(f"Email: {teacher['email']}")
                print(f"Teacher ID: {teacher['teacher_id']}")
                return
        print("Teacher not found.")


            
print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show a student details")
print("press 5 to show a teachers details")

choice =  int(input("Enter your choice:- "))

student = Student()
teacher = Teacher()
if choice == 1:
    student.register()

elif choice == 2:
    teacher.register()

elif choice == 3:
    student.grade()

elif choice == 4:
    student.show_details()

elif choice == 5:
    teacher.show_details()