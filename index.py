from pathlib import Path
from abc import ABC, abstractmethod
import json 

database = "database.json"
data = {"students": [], "teachers":[]}

if Path(database).exists():
    with open(database, "r") as file:
        content = file.read()
        if content:
            data = json.loads(content)

def save_data():
    with open(database,"w") as file:
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

class student(Registration):
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

        student_data ={
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
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print(f"Name: {i['name']}")
                print(f"Age: {i['age']}")
                print(f"Email: {i['email']}")
                print(f"Roll Number: {i['roll_no']}")
                print(f"Grades: {i['grades']}")
                return
        print("Student not found.")

    def update_grades(self):
        roll_no = input("Enter student roll number: ")
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                subject = input("Enter subject name: ")
                grade = float(input("Enter grade: "))
                i["grades"][subject] = grade
                save_data()
                print("Grade updated successfully.")
                return
        print("Student not found.")

class teacher(Registration):
    def get_roles(self):
        return "Teacher"

    def register(self):
        name = input("Enter teacher name: ")
        subject = input("Enter teacher subject: ")
        email = input("Enter teacher email: ")
        if not Registration.validate_email(email):
            print("Invalid email format.")
            return

        roll_no = input("Enter teacher roll number: ")
        for i in data["teachers"]:
            if i["roll_no"] == roll_no:
                print("Teacher with this roll number already exists.")
                return

        teacher_data = {
            "name": name,
            "subject": subject,
            "email": email,
            "roll_no": roll_no
        }
        data["teachers"].append(teacher_data)
        save_data()
        print("Teacher registered successfully.")

    def show_details(self):
        roll_no = input("Enter teacher roll number: ")
        for i in data["teachers"]:
            if i["roll_no"] == roll_no:
                print(f"Name: {i['name']}")
                print(f"Subject: {i['subject']}")
                print(f"Email: {i['email']}")
                print(f"Roll Number: {i['roll_no']}")
                return
        print("Teacher not found.")

print("press 1 to register as a student")
print("press 2 to register as a teacher")   
print("press 3 to update grades of a student")
print("press 4 to view details of a student")
print("press 5 to view details of a teacher")

choice = int(input("Enter your choice: "))
student = student()
teacher = teacher()
if choice == 1:
    student.register()

elif choice == 2:
    teacher.register()
elif choice == 3:
    student.update_grades()
elif choice == 4:
    student.show_details()
elif choice == 5:
    teacher.show_details()
else:
    print("Invalid choice. Please select a valid option.")
