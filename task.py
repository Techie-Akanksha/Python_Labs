import json
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime

hospital_data = "hospital_data.json"
data = {"patients": [], "doctors": [], "appointments":[]}

if Path(hospital_data).exists():
    with open(hospital_data, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


data.setdefault("patients", [])
data.setdefault("doctors", [])
data.setdefault("appointments", [])

def save():
    with open(hospital_data, "w") as f:
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

    @staticmethod
    def valid_bloodgrp(blood_grp):
        valid_groups = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        return blood_grp.upper() in valid_groups


class Patient(Person):
    def get_role(self):
        return "Patient"

    def details(self):
        while True:
            try:
                patient_id = int(input("Enter patient ID:- "))
                break
            except ValueError:
                print("Please enter a valid patient ID.")

        for patient in data["patients"]:
            if patient["patient_id"] == patient_id:
                print("Patient with this patient ID already exists")
                return

        name = input("Enter patients name:- ")

        while True:
            try:
                age = int(input("Enter patients age:- "))
                if age > 0 and age < 120:
                    break
                print("Please enter valid age")
            except ValueError:
                print("Please enter valid age")

        while True:
            gender = input("Enter patient gender: ")
            if gender.lower() in ("male", "female", "other"):
                break
            print("Please enter gender again!")

        while True:
            phone = input("Enter patient phone no:- ")
            if not Person.validate_mob(phone):
                print("Invalid phone number format.")
                continue
            break

        while True:
            email = input("Enter patient Email:- ")
            if not Person.validate_email(email):
                print("Invalid email format.")
                continue
            break

        while True:
            blood_grp = input("Enter patient blood group:- ").strip().upper()

            if Person.valid_bloodgrp(blood_grp):
                break

            print("Invalid blood group. Please enter a valid blood group.")

        while True:
            address = input("Enter patients address:- ")
            if not address.strip():
                print("Address cannot be empty!")
                continue
            break

        medical_history = input("Enter patients medical history:- ")

        patients_data = {
            "patient_id": patient_id,
            "name": name,
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
        print()

    def show_details(self):
        print()

        try:
            patient_id = int(input("Enter Patient ID:- "))
        except ValueError:
            print("Please enter a valid Patient ID.")
            return

        for patient in data["patients"]:
            if patient["patient_id"] == patient_id:
                print()
                print("=" * 5, "Show Patient Details", "=" * 5)
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
                print("=" * 5, "Search Patients", "=" * 5)
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
        print()

        try:
            patient_id = int(input("Enter Patient ID:- "))
        except ValueError:
            print("Please enter a valid Patient ID.")
            return

        for patient in data["patients"]:
            if patient["patient_id"] == patient_id:
                print()
                print("Patient found.")

                while True:
                    print()
                    print("What do you want to update?")
                    print("1. Name")
                    print("2. Age")
                    print("3. Gender")
                    print("4. Phone")
                    print("5. Email")
                    print("6. Blood Group")
                    print("7. Address")
                    print("8. Medical History")
                    print("9. Exit")

                    try:
                        choice = int(input("Enter your choice:- "))
                    except ValueError:
                        print("Please enter a valid choice.")
                        continue

                    if choice == 1:
                        name = input("Enter Patient Name:- ")
                        patient["name"] = name
                        save()
                        print("Patient name updated successfully!")

                    elif choice == 2:
                        while True:
                            try:
                                age = int(input("Enter patients age:- "))
                                if age > 0 and age < 120:
                                    break
                                print("Please enter valid age")
                            except ValueError:
                                print("Please enter valid age")

                        patient['age'] = age
                        save()
                        print("Patient age updated successfully!")

                    elif choice == 3:
                        while True:
                            gender = input("Enter patient gender: ")
                            if gender.lower() in ("male", "female", "other"):
                                break
                            print("Please enter gender again!")

                        patient['gender'] = gender
                        save()
                        print("Patient gender updated successfully!")

                    elif choice == 4:
                        while True:
                            phone = input("Enter patient phone no:- ")
                            if not Person.validate_mob(phone):
                                print("Invalid phone number format.")
                                continue
                            break

                        patient['phone'] = phone
                        save()
                        print("Patients phone no updated successfully!")

                    elif choice == 5:
                        while True:
                            email = input("Enter patient Email:- ")
                            if not Person.validate_email(email):
                                print("Invalid email format.")
                                continue
                            break

                        patient["email"] = email
                        save()
                        print("Patients email updated successfully!")

                    elif choice == 6:
                        while True:
                            blood_grp = input(
                                "Enter patient blood group:- "
                            ).strip().upper()

                            if Person.valid_bloodgrp(blood_grp):
                                break

                            print(
                                "Invalid blood group. "
                                "Please enter a valid blood group."
                            )

                        patient['blood_grp'] = blood_grp
                        save()
                        print("Patients blood group updated successfully!")

                    elif choice == 7:
                        while True:
                            address = input("Enter patients address:- ")

                            if not address.strip():
                                print("Address cannot be empty!")
                                continue

                            break

                        patient['address'] = address
                        save()
                        print("Patients address updated successfully!")

                    elif choice == 8:
                        medical_history = input(
                            "Enter patients medical history:- "
                        )

                        patient['medical_history'] = medical_history
                        save()
                        print("Patients medical history updated successfully!")

                    elif choice == 9:
                        print("Exiting update menu...")
                        return

                    else:
                        print("Please enter a valid choice.")

        print("Patient not found")

    def delete_details(self):
        print()

        try:
            patient_id = int(input("Enter Patient ID:- "))
        except ValueError:
            print("Please enter a valid Patient ID.")
            return

        for patient in data['patients']:
            if patient['patient_id'] == patient_id:
                print()
                print("Patient found.")

                confirm = input(
                    "Are you sure you want to delete this patient? (yes/no):- "
                )

                if confirm.lower() == "yes":
                    data['patients'].remove(patient)
                    save()
                    print("Patient deleted successfully!")
                    return

                else:
                    print("Patient deletion cancelled.")
                    return

        print("Patient not found")


class Doctor(Person):
    def get_role(self):
        return "Doctor"

    def details(self):
        try:
            doctor_id = int(input("Enter Doctor ID:- "))
        except ValueError:
            print("Please enter a valid Doctor ID.")
            return

        for doctor in data["doctors"]:
            if doctor["doctor_id"] == doctor_id:
                print("Doctor with this Doctor ID already exists")
                return

        name = input("Enter Doctor name:- ")

        while True:
            specialization = input("Enter doctors specialization:- ")

            if not specialization.strip():
                print("Specialization cannot be empty!")
                continue

            break

        while True:
            phone = input("Enter doctors phone no:- ")

            if not Person.validate_mob(phone):
                print("Invalid phone number format.")
                continue

            break

        while True:
            email = input("Enter doctor Email:- ")

            if not Person.validate_email(email):
                print("Invalid email format.")
                continue

            break

        experience = input("Enter doctors experience:- ")

        doctors_data = {
            "doctor_id": doctor_id,
            "name": name,
            "specialization": specialization,
            "email": email,
            "phone": phone,
            "experience": experience
        }

        data["doctors"].append(doctors_data)
        save()

        print("Doctors details saved successfully!")

    def show_details(self):
        print()

        try:
            doctor_id = int(input("Enter Doctor ID:- "))
        except ValueError:
            print("Please enter a valid Doctor ID.")
            return

        for doctor in data["doctors"]:
            if doctor["doctor_id"] == doctor_id:
                print()
                print("=" * 5, "Show Doctors Details", "=" * 5)
                print()
                print(f"Name: {doctor['name']}")
                print(f"Specialization: {doctor['specialization']}")
                print(f"Email: {doctor['email']}")
                print(f"Phone: {doctor['phone']}")
                print(f"Experience: {doctor['experience']}")
                print()
                return

        print("Doctor not found")

    def update_details(self):
        print()

        try:
            doctor_id = int(input("Enter Doctor ID:- "))
        except ValueError:
            print("Please enter a valid Doctor ID.")
            return

        for doctor in data['doctors']:
            if doctor['doctor_id'] == doctor_id:
                print()
                print("Doctor found.")

                while True:
                    print()
                    print("What do you want to update?")
                    print("1. Name")
                    print("2. Specialization")
                    print("3. Phone")
                    print("4. Email")
                    print("5. Experience")
                    print("6. Exit")

                    try:
                        choice = int(input("Enter your choice:- "))
                    except ValueError:
                        print("Please enter a valid choice.")
                        continue

                    if choice == 1:
                        name = input("Enter Doctor Name:- ")
                        doctor["name"] = name
                        save()
                        print("Doctor name updated successfully!")

                    elif choice == 2:
                        while True:
                            specialization = input(
                                "Enter doctors specialization:- "
                            )

                            if not specialization.strip():
                                print("Specialization cannot be empty!")
                                continue

                            break

                        doctor["specialization"] = specialization
                        save()
                        print(
                            "Doctor specialization updated successfully!"
                        )

                    elif choice == 3:
                        while True:
                            phone = input("Enter doctor phone no:- ")

                            if not Person.validate_mob(phone):
                                print("Invalid phone number format.")
                                continue

                            break

                        doctor['phone'] = phone
                        save()
                        print("Doctors phone no updated successfully!")

                    elif choice == 4:
                        while True:
                            email = input("Enter doctors Email:- ")

                            if not Person.validate_email(email):
                                print("Invalid email format.")
                                continue

                            break

                        doctor["email"] = email
                        save()
                        print("Doctors email updated successfully!")

                    elif choice == 5:
                        while True:
                            experience = input(
                                "Enter doctors experience:- "
                            )

                            if not experience.strip():
                                print("Experience cannot be empty!")
                                continue

                            break

                        doctor['experience'] = experience
                        save()
                        print("Doctors experience updated successfully!")

                    elif choice == 6:
                        print("Exiting update menu...")
                        return

                    else:
                        print("Please enter a valid choice.")

        print("Doctor not found")

    def search_details(self):
        print()

        specialization = input("Enter specialization to search:- ")
        found = False

        for doctor in data["doctors"]:
            if doctor["specialization"].lower() == specialization.lower():
                print()
                print("=" * 5, "Search Doctors", "=" * 5)
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

    def delete_details(self):
        print()

        try:
            doctor_id = int(input("Enter Doctor ID:- "))
        except ValueError:
            print("Please enter a valid Doctor ID.")
            return

        for doctor in data['doctors']:
            if doctor['doctor_id'] == doctor_id:
                print()
                print("Doctor found.")

                confirm = input(
                    "Are you sure you want to delete this doctor? (yes/no):- "
                )

                if confirm.lower() == "yes":
                    data['doctors'].remove(doctor)
                    save()
                    print("Doctor deleted successfully!")
                    return

                else:
                    print("Doctor deletion cancelled.")
                    return

        print("Doctor not found")

class Appointment:
    def book_appointment(self):
        try:
            patient_id = int(input("Enter Patient ID:- "))
            found = False
        except ValueError:
            print("Please enter a valid Patient ID.")
            return

        for patient in data["patients"]:
            if patient["patient_id"] == patient_id:
                found = True
                break

        if not found:
            print("Patient not found!")
            return

        try:
            doctor_id = int(input("Enter Doctor ID:- "))
            found = False
        except ValueError:
            print("Please enter a valid Doctor ID.")
            return

        for doctor in data["doctors"]:
            if doctor["doctor_id"] == doctor_id:
                found = True
                break

        if not found:
            print("Doctor not found!")
            return

        while True:
            date = input("Enter appointment date (YYYY-MM-DD): ")

            try:
                appointment_date = datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date! Please enter date in YYYY-MM-DD format.")
                continue

        while True:
            time = input("Enter appointment time (HH:MM): ")

            try:
                appointment_time = datetime.strptime(time, "%H:%M")
                break
            except ValueError:
                print("Invalid time! Please enter time in HH:MM format.")
                continue

        reason = input("Enter reason for appointment: ")

        for appointment in data["appointments"]:
            if (
                appointment["doctor_id"] == doctor_id
                and appointment["appointment_date"] == date
                and appointment["appointment_time"] == time
            ):
                print("Doctor is already booked at this date and time!")
                return

        appointment_data = {
            "patient_id": patient_id,   
            "doctor_id": doctor_id,
            "appointment_date": date,
            "appointment_time" : time,
            "reason": reason
        }
        data["appointments"].append(appointment_data)
        save()

        print("Appointment details saved successfully!")

print("---" * 20)
print("   " * 5, "Hospital Management System", "   " * 5)
print("---" * 20)

while True:
    print()
    print("Choose the option")
    print("Press 1 Register as patient")
    print("Press 2 Register as doctor")
    print("Press 3 Book an appointment")
    print("Press 4 to Exit menu")

    patient = Patient()
    doctor = Doctor()
    appointment = Appointment()

    try:
        choice = int(input("Enter your option:- "))
    except ValueError:
        print("Please choose valid option!")
        continue

    if choice == 1:

        print()
        print("Started registration as patient")
        print(" - " * 30)

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
            except ValueError:
                print("Please enter valid option.")
                continue

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

        print()
        print("Started registration as doctor")
        print(" - " * 30)

        while True:
            print("Choose your option")
            print("Press 1 to register doctor details")
            print("Press 2 to view doctors details")
            print("Press 3 to update doctor details")
            print("Press 4 to search doctor details")
            print("Press 5 to delete doctor details")
            print("Press 6 to Exit")

            try:
                choice = int(input("Enter your operation:- "))
            except ValueError:
                print("Please enter valid option.")
                continue

            if choice == 1:
                doctor.details()

            elif choice == 2:
                doctor.show_details()

            elif choice == 3:
                doctor.update_details()

            elif choice == 4:
                doctor.search_details()

            elif choice == 5:
                doctor.delete_details()

            elif choice == 6:
                print("Exiting doctor menu...")
                break

            else:
                print("Please enter valid choice")

    elif choice == 3:
        print()
        print("Book an appointment")
        print(" - " * 30)

        appointment.book_appointment()


    elif choice == 4:
        print("Exiting menu...")
        break

    else:
        print("Invalid action")
        print("Please enter option again")

