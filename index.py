import json
from abc import ABC, abstractmethod
from pathlib import Path

hospital_data = "hospital_data.json"
data = {"patients":[], "doctors":[]}

if Path(hospital_data).exists():
    with open("hospital_data","r") as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open("hospital_data","w") as f:
        json.dump(data, f, indent=4)

class Person:  
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @abstractmethod
    def search_details(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @staticmethod
    def validate_mob(mob):
        return (
            len(mob) == 10 
            and mob.isdigit()
            and mob[0] in "6789"
        )

class Patient(Person):
    def get_role(self):
        return "Patient"

    def details(self):
        id = int(input("Enter patient ID:- "))
        for i in data["patients"]:
            if i["id"] == id:
                print("Patient with this patient ID already exists")
                return

        name = input("Enter patients name:- ")
        try:
            age = int(input("Enter patients age:- "))
        except ValueError:
            print("Please enter valid age")

        gender = input("Enter patient gender:- ")
        if gender.lower() not in ("male", "female","other"):
            print("Please enter gender again!")

        phone = int(input("Enter patient phone no:- "))
        if not Person.validate_mob(phone):
            print("Invalid phone number format.")
            return

        email = input("Enter patient Email:- ")
        if not Person.validate_email(email):
            print("Invalid email format.")
            return

        blood_grp = input("Enter patient blood group:- ")
        address = input("Enter patients address:- ")
        medical_history = input("Enter patients medical history:- ")

        patients_data = {
            "id": id,
            "name" : name,
            "age": age,
            "gender": gender,
            "phone": phone,
            "email": email,
            "blood_grp": blood_grp,
            "address": address,
            "medical_history": medical_history
        }
        data["patients"].append(patients_data)
        save()
        print("Patients details saved successfully!")

    def show_details(self):
       pass

    def search_details(self):
        pass

    def update_details(self):
        pass

    def delete_details(self):
        pass

class Doctor(Person):
    def get_role(self):
        return "Patient"

    def details(self):
        id = int(input("Enter Doctor ID:- "))
        for i in data["doctors"]:
            if i["id"] == id:
                print("Doctor with this patient ID already exists")
                return

        name = input("Enter Doctor name:- ")

        specialization = input("Enter doctors specialization:- ")
        if specialization.lower() not in ("male", "female","other"):
            print("Please enter specialization again!")

        phone = int(input("Enter doctors phone no:- "))
        if not Person.validate_mob(phone):
            print("Invalid phone number format.")
            return

        email = input("Enter doctor Email:- ")
        if not Person.validate_email(email):
            print("Invalid email format.")
            return

        experience = input("Enter doctors experience:- ")

        doctors_data = {
            "id": id,
            "name" : name,
            "specialization": specialization,
            "email": email,
            "phone": phone,
            "experience":experience
        }
        data["doctors"].append(doctors_data)
        save()
        print("Doctors details saved successfully!")

    def show_details(self):
       pass

    def search_details(self):
        pass

