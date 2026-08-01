# Topic: @property.setter Deep Dive

# Aaj ka goal:

# Python ko kaise pata chalta hai ki emp.salary = 50000 likhne par setter method call karni hai?

# Ye internal working samajhna hai.

class Employee:

    def __init__(self):
        self.__salary = 50000

    @property
     #Ab class ke andar salary naam ka property object aa gaya.
     #Ab salary ek normal function nahi raha.
    def salary(self):
        return self.__salary

    @salary.setter
    #Jo upar salary property bani thi, uske saath ye setter attach kar do
    def salary(self, value):
        self.__salary = value

# Dono methods ka naam salary hi hai.

# salary Property

# ↓

# Setter Exist?

# ↓

# Yes

# ↓

# Call Setter

# ↓

# value = 70000

# ↓

# self.__salary = value

emp = Employee()
emp.salary = 70000 #Pehle wale me setter call hoti hai.
emp.__salary = 70000 #Class ke bahar __salary likhne par name mangling apply nahi hoti.

# To Python object me ek naya attribute bana dega:

# {
#     "_Employee__salary":50000,

#     "__salary":70000
# }


# 🧠 Memory Rule

# Aaj ka golden rule:

# Ye
emp.salary = 50000

# Matlab:

# Setter ko request bhejo.
# Ye
emp.__salary = 50000

# Matlab:

# Object me naya attribute banao.


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

emp.salary = 60000

print(emp.salary)

print(emp.__dict__)


# 💼 Interview Perspective

# Interviewer:

# Why do getter and setter methods have the same name when using @property?

# Expected answer:

# Because both methods belong to the same property. @property creates the property, and @property_name.setter attaches the setter to that existing property. Python then automatically calls the getter when reading the attribute and the setter when assigning to it.

# Encapsulation → Data ko protect karta hai.
# Property → Controlled access deta hai.
# Abstraction → Unnecessary implementation details ko hide karta hai.


#Property ka use karne se hum data ko protect kar sakte hai aur controlled access provide kar sakte hai. Getter aur setter methods ke through hum data ko read aur write kar sakte hai bina direct access ke.

# property object ke andar getter aur setter methods attach hote hai. Jab hum property ko read karte hai to getter call hoti hai aur jab hum property ko write karte hai to setter call hoti hai. Isse hum data ko encapsulate kar sakte hai aur unnecessary implementation details ko hide kar sakte hai.

