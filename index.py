# @property ka actual syntax

#Step 1: without @property
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary

emp = Employee(50000)

print(emp.get_salary())

emp.set_salary(60000)

print(emp.get_salary())

# Lekin Python bolta hai "Ye method jaisa nahi lagna chahiye."

# Step 2: Actual Syntax

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Invalid Salary")

# Step 3: Har Line Ka Meaning

class Employee:

    def __init__(self, salary): 
        self.__salary = salary # Object me private attribute create hua.

    @property # Is method ko normal method ki tarah mat treat karo.
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Invalid Salary")

emp = Employee(50000)

emp.salary #Aur Python automatically getter execute karega.



# jab aap object create karte hain tab constructor (Python mein __init__ method) automatically run hota hai, aur memory mein ek naya object ban kar uske variables save hote hain.Constructor Kab Run Hota Hai?Jab aap obj = ClassName() likh kar naya object banate hain, tab Python pehle memory mein ek khali object banata hai (__new__ method se).Uske turant baad, Python automatic tarike se __init__ method (constructor) ko call kar deta hai, jisme object ki initial values ya data set hota hai.

class Demo:

    def __init__(self):
        self.x = 10

    def change(self):

        x = self.x

        x = 50

d = Demo()

d.change()

print(d.x)


# 

class Employee:

    def __init__(self):
        self.__salary = 50000

    @property
    def salary(self):
        print("Getter")
        return self.__salary

    @salary.setter
    def salary(self, value):
        print("Setter")
        self.__salary = value


emp = Employee()

x = emp.salary

print(x)

print(emp.salary)


# print()
# Screen par output dikhata hai.
# Return value None hoti hai.
# Koi data permanently store nahi karta.
# return
# Function se value bahar bhejta hai.
# Caller us value ko variable me store kar sakta hai.