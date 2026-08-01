# Topic: Property Objects

# First python ek object banata hai jo class ka object hota hai. Ye object class ke andar defined methods ko access karne ke liye use hota hai. Property objects ka use karke hum class ke attributes ko encapsulate kar sakte hain aur unke access ko control kar sakte hain.

# python mein property objects ka use karne ke liye hum `property()` function ka use karte hain. Ye function ek method ko property mein convert karta hai, jisse hum us method ko attribute ki tarah access kar sakte hain.

class Employee:

    @property
    def salary(self):
        return self.__salary

    
# Explaination:
# Property Object (Ye naya concept hai) Ye class banate waqt Python khud create karta hai. Suppose @property method create kiya to ham sochte hai ke bas ek getter method create ho gaya. Lekin internally Python kuch aur karta hai.Pehle koi bhi function normal function hota hai.@property lagte hi Python bolta hai: Is function ko special bana do. lekin Python khud ek property object create karta hai jisme getter, setter aur deleter methods hote hain. Ye jo special cheez bani...Isko Python bolta hai: Property Object

# property object values store nahi karta. Ye sirf information rakhta hai.
# jaise ke:
# Property Object

# Name : salary

# Getter : salary()

# Setter : None

# Deleter : None


# Ab Setter Aata Hai
    @salary.setter
    def salary(self, value):
        print("Setter")
        self.__salary = value


emp = Employee()

emp.salary = 60000

print(emp.salary)

print(emp.__dict__)

# Python property object ko update karta hai. pehle se jo salary method tha usko update karta hai aur setter method ko add kar deta hai. Ab ye property object ke andar getter aur setter dono methods hote hain.

# Isliye Syntax Hai
# @property

# ↓

# Property Object banao.

# @salary.setter

# ↓

# Us property object ke andar setter attach karo.


# Employee Class

#         │

#         ▼

# salary Property Object

#  ┌───────────────┐
#  │ Getter Method │
#  │ Setter Method │
#  │ Deleter       │
#  └───────────────┘



# 📦 Global Memory

# ↓

# 📦 Class Memory

# ↓

# 📦 Object Memory

# ↓

# 📦 Function Local Memory

# Python ka flow:

# Global Memory

# emp

# ↓

# Object

# ↓

# Class

# ↓

# salary Property Object

# ↓

# Setter Function

# ↓

# Local Memory

# self

# value

# ↓

# Object Memory Update


"""
❗Ek Chhoti Technical Note

Main ek baat intentionally simplify kar raha hoon.

Reality me Python ke andar property ek built-in class hai.

Jab tum likhti ho:

@property
def salary(self):

To Python internally lagbhag aisa karta hai (conceptually):

salary = property(salary)

Yaani property naam ki built-in class ka ek object ban jata hai, jo getter, setter aur deleter ko manage karta hai.

Abhi is implementation ko yaad karne ki zarurat nahi hai. Bas itna yaad rakho ki property object ek manager ki tarah kaam karta hai—wo data store nahi karta, wo batata hai ki read aur write hone par kaunsa method chalana hai. """


# 🎤 Interview Answer 1 (Best for Freshers)

# Q. What is @property in Python?

# @property is a built-in decorator that converts a method into a property. It allows us to access a method like a normal attribute while still executing the method internally. This makes the code cleaner, more readable, and allows validation or other logic without changing how the class is used.

# 🎤 Interview Answer 2 (If Asked: What is a Property Object?)

# A property object is a special object created by Python when we use @property. It does not store the actual data. Instead, it keeps references to the getter, setter, and deleter methods and decides which method to call when an attribute is read, written, or deleted.

# One-line version:

# A property object acts as a manager between attribute access and the actual getter/setter methods.

# 🎤 Interview Answer 3 (Internal Working)

# Q. What happens internally when we use @property?

# When Python sees @property, it creates a property object and attaches the getter method to it. When we use @property_name.setter, Python attaches the setter method to the same property object. Later, when we access or assign the attribute, Python automatically calls the appropriate method.


# @property
# ↓
# Creates a Property Object

# Property Object
# ↓
# Stores references to:
# ✔ Getter
# ✔ Setter
# ✔ Deleter

# It does NOT store the actual data.
# The actual data is stored inside the object.


# Interview Answer

# Agar interviewer pooche:

# Does the property object contain the getter and setter functions?

# Simple answer:

# The property object does not contain separate copies of the getter and setter code. It stores references to those functions and uses them when the property is accessed or modified.







# ✅ Aaj Humne Kya Complete Kiya?
# 1. @property ka purpose
# Method ko attribute ki tarah access kar sakte hain.
# Cleaner aur readable code.
# 2. Getter aur Setter ki internal working
# emp.salary

# Internally:

# Property Object
#       ↓
# Getter
#       ↓
# Local Memory
#       ↓
# Object Memory
#       ↓
# Return Value
# 3. @salary.setter
# emp.salary = 70000

# Internally:

# Property Object
#       ↓
# Setter
#       ↓
# Local Memory
#       ↓
# Object Memory Update
# 4. Property Object

# Ye aaj ka sabse important concept tha.

# Tumne samjha ki:

# ❌ Property object salary ki value store nahi karta.

# ✅ Property object sirf getter, setter aur deleter ke references rakhta hai.

# Actual data:

# Employee Object

# _Employee__salary = 50000
# 5. Memory Model

# Ab tumhare paas complete mental model hai.

# Global Memory
#       │
#       ▼
# Class Memory
#       │
#       ▼
# Property Object
#       │
#       ▼
# Getter / Setter References
#       │
#       ▼
# Function Local Memory
#       │
#       ▼
# Object Memory