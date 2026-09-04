import json
from abc import ABC, abstractmethod
from pathlib import Path

hospital_data = "hospital_data.json"
data = {"patients":[], "doctors":[]}

if Path(hospital_data).exists():
    with open(hospital_data,"r") as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(hospital_data,"w") as f:
        json.dump(data, f, indent=4)

class Person(ABC):  
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
        while True:
            try:
                age = int(input("Enter patients age:- "))
                break
            except ValueError:
                print("Please enter valid age")

        while True:
            gender = input("Enter patient gender: ")
            if gender.lower() in ("male", "female", "other"):
                break
            print("Please enter gender again!")

        phone = input("Enter patient phone no:- ")
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
        print()
        id = int(input("Enter Patient ID:- "))
        for patient in data["patients"]:
            if patient["id"] == id:
                print()
                print("="*5,"Show Patient Details","="*5)
                print()
                print(f"Name: {patient['name']}")
                print(f"age: {patient['age']}")
                print(f"gender: {patient['gender']}")
                print(f"Email: {patient['email']}")
                print(f"Phone: {patient['phone']}")
                print(f"blood_grp: {patient['blood_grp']}")
                print(f"address: {patient['address']}")
                print(f"medical_history: {patient['medical_history']}")
                print()
                return
        print("Patient not found")

    def search_details(self):
        print()
        blood_grp = input("Enter blood group to search:- ")
        found = False

        for patient in data["patients"]:            
            if patient["blood_grp"].lower() == blood_grp.lower():
                print()        
                print("="*5,"Search Doctors","="*5)
                print()
                print(f"Name: {patient['name']}")
                print(f"age: {patient['age']}")
                print(f"gender: {patient['gender']}")
                print(f"Email: {patient['email']}")
                print(f"Phone: {patient['phone']}")
                print(f"blood_grp: {patient['blood_grp']}")
                print(f"address: {patient['address']}")
                print(f"medical_history: {patient['medical_history']}")
                print()
                found = True

        if not found:
            print("Patient not found")

    def update_details(self):
        pass

    def delete_details(self):
        pass

class Doctor(Person):
    def get_role(self):
        return "Doctor"

    def details(self):
        id = int(input("Enter Doctor ID:- "))
        for i in data["doctors"]:
            if i["id"] == id:
                print("Doctor with this Doctor ID already exists")
                return

        name = input("Enter Doctor name:- ")

        while True:
                specialization = input("Enter doctors specialization:- ")
                if not specialization.strip():
                    print("Specialization cannot be empty!")
                    continue
                break

        phone = input("Enter doctors phone no:- ")
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
        print()
        id = int(input("Enter Doctor ID:- "))
        for doctor in data["doctors"]:
            if doctor["id"] == id:
                print()
                print("="*5,"Show Doctors Details","="*5)
                print()
                print(f"Name: {doctor['name']}")
                print(f"Specialization: {doctor['specialization']}")
                print(f"Email: {doctor['email']}")
                print(f"Phone: {doctor['phone']}")
                print(f"Experience: {doctor['experience']}")
                print()
                return
        print("Doctor not found")

    def search_details(self):
        print()

        specialization = input("Enter specialization to search:- ")
        found = False
        for doctor in data["doctors"]:
            if doctor["specialization"].lower() == specialization.lower():
                print()        
                print("="*5,"Search Doctors","="*5)
                print()
                print(f"Name: {doctor['name']}")
                print(f"Specialization: {doctor['specialization']}")
                print(f"Email: {doctor['email']}")
                print(f"Phone: {doctor['phone']}")
                print(f"Experience: {doctor['experience']}")
                print()
                found = True
        if not found:
            print("Doctor not found")




print("---"*20)
print("   "*5,"Hospital Management System","   "*5)
print("---"*20)
while True:
    print()
    print("Choose the option")
    print("Press 1 Register as patient")
    print("Press 2 Register as doctor")
    print("Press 3 to Exit menu")
    patient = Patient
    doctor = Doctor

    try:
        choice = int(input("Enter your option:- "))
    except ValueError:
        print("Please choose valid option!")
        continue

    if choice == 1:

        print()
        print("Started registration as patient")
        print(" - "*30)

        while True:
            print("Choose your option")
            print("Press 1 to register patient details")
            print("Press 2 to view patient details")
            print("Press 3 to update patient details")
            print("Press 4 to search patient details")
            print("Press 5 to delete patient details")
            print("Press 6 to Exit")
            try:
                choice = int(input("Enter your operation:- "))
                break
            except ValueError:
                print("Please enter valid option.")

            if choice == 1:
                patient.details()

            elif choice == 2:
                patient.show_details()

            elif choice == 3:
                patient.update_details()

            elif choice == 4:
                patient.search_details()

            elif choice == 5:
                patient.delete_details()

            elif choice == 6:
                print("Exiting patient menu...")
                break

            else:
                print("Please enter valid choice")


    elif choice == 2:
        print("Started registration as doctor")
        
        while True:
            print()
            print("Choose your option")
            print("Press 1 to register doctor details")
            print("Press 2 to view patidoctorent details")
            print("Press 3 to search doctor details")
            print("Press 4 to Exit")
            try:
                choice = int(input("Enter your operation:- "))
                break
            except ValueError:
                print("Please enter valid option.")

            if choice == 1:
                patient.details()

            elif choice == 2:
                patient.show_details()

            elif choice == 3:
                patient.search_details()

            elif choice == 4:
                print("Exiting patient menu...")
                break

            else:
                print("Please enter valid choice")

    elif choice == 3:
        print("Exiting menu...")
        break
    else:
        print("Invalid action")
        print("Please enter option again")
    



