#Abstruction

# Abstraction is the process of hiding unnecessary implementation details and exposing only the essential features to the user.

# Encapsulation vs Abstraction

# Encapsulation   	                   Abstraction
# Data ko protect karta hai	    Complexity ko hide karta hai
# Focus on data	                Focus on behavior
# private attributes        	Abstract classes / interfaces
# Controlled access	            Simplified interface

#Bank class with abstraction    
class bank:
    name = "Bank of India"

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    @property
    def get_balance(self):
        return self.__balance

bank_account = bank("123456789", 1000)
bank_account.deposit(500)
bank_account.withdraw(200)
print(f"Final balance: {bank_account.get_balance}") 



# Abstraction means hiding the implementation details and showing only the essential functionality to the user. It helps reduce complexity and allows users to focus on what an object does rather than how it works internally.

# Example of Abstraction in Python:
# Suppose hum Vehicle class bana rahe hain.

class Vehicle:

    def start(self):
        pass

# Humare paas ho sakte hain:

# Car
# Bike
# Truck
# Bus

# Sabko start karna hai.
# Lekin Car ka start alag.
# Bike ka alag.
# Truck ka alag.

# Vehicle class ko start() method ka code likhna chahiye?
# Jo bhi meri child class hogi, usko start() method implement karna hi padega.

# Vehicle ko nahi pata Car ka engine kaise start hota hai.
# Vehicle sirf rule banata hai.
# "Har vehicle me start() hona chahiye."

# Agar hum Vehicle class me start() method ka code likhenge, to Car ko start() method ko override karna padega. ham parent class ke methods ko inherit karte hain. Lekin neccessary nahi hai ki har child class ke liye parent class ke methods ka code same ho. Isliye hum start() method ko parent class me define karte hain, lekin uska implementation child class me karte hain.

# Hame ye ensure karna hai ki har vehicle me start() method ho. Isliye hum start() method ko abstract method banate hain. Abstraction ka matlab hai ki hum implementation details ko hide karte hain aur sirf essential features ko expose karte hain. Not neccessary ke ham Bas ek dummy method chal rahe hai ye inheritance se hota hai isse ko ham avoid karte hai aur abstract method banate hai.

# Agar parent class sirf rule define kar rahi hai, implementation nahi...To usko Abstract Class banao. Aur method ko bolo Child class, tumhe ye method likhna hi padega.

#💼 Interview Perspective

# Agar interviewer pooche:

# Why do we need abstraction when we already have inheritance?

# Simple answer:

# Inheritance allows code reuse, but abstraction defines a common contract. It ensures that every child class provides its own implementation of required methods while hiding unnecessary implementation details from the user.  


# pass ka matlab hai:"Method exist karta hai, lekin uske andar koi implementation nahi hai."

# Agar ham inheritance use karte hain to Code softly run ho jayega but problem detect nahi hogi.Yehi abstraction ki sabse badi problem solve karta hai.Agar programmer override karna bhool gaya... program chal jayega.Koi error nahi.Aur bug baad me pata chalega.Isi problem ke liye Python me Abstract Class hai.


# class Animal:

#     def sound(self):
#         pass


# class Dog(Animal):
#     pass


# d = Dog()

# d.sound()

# Tumhari Reasoning Ko Interview Level Banate Hain

# Agar interviewer pooche:

# Why is this design bad?

# Tum aise answer de sakti ho:

# This design is not good because the parent class provides an empty implementation using pass. If a child class forgets to override the method, the program still runs without any error. This can hide bugs. An abstract class solves this problem by forcing every child class to implement the required method.

#----------------------------------------------------------------------

#Abstract Class
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

d = Dog()
print(d.sound())  # Output: "Woof!"



# While regular inheritance allows you to reuse code, an abstract class is needed to enforce a strict blueprint and contract across subclasses. Standard inheritance passes down behavior but cannot guarantee that a child class will implement specific mandatory methods.

from abc import ABC, abstractmethod

# abc ka full form hai: Abstract Base Classes
# Ye Python ka built-in module hai jo abstraction implement karne ke liye tools provide karta hai.
# ABC ek normal Python class hai.Bas uska purpose special hai.

class Animal(ABC): # Animal ABC ko inherit kar rahi hai.

    @abstractmethod # Ye bhi ek decorator hai.
    def sound(self):
        pass

# class Dog(Animal):
#     pass

# d = Dog() # Ye error dega kyunki Dog class ne sound() method ko implement nahi kiya hai.
# Yaani object banne se pehle hi Python check karta hai.Isi wajah se bug turant pakad me aa jata hai. python check karega ke Is class me koi abstract methods abhi bhi implement hone baaki hain kya?

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound() # Output: Bark


# Class Memory

# ABC Class

# ↓

# Animal Class

# ↓

# sound Function

# ↓

# Abstract Flag = True


# Q. What is an Abstract Class?

# An abstract class is a class that cannot be instantiated directly. It is used to define a common blueprint or contract for its child classes.

# Q. What is an Abstract Method?

# An abstract method is a method declared using @abstractmethod that must be implemented by every concrete child class.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.sound()

# 💼 Interview Improvement
# Tumhara answer agar interview me dena ho to main ise thoda polish karunga:

# An abstract class defines a contract for its child classes. By inheriting from ABC and using the @abstractmethod decorator, Python ensures that every concrete child class implements the required methods. If any abstract method remains unimplemented, Python raises a TypeError when an object of that class is created. This helps catch design mistakes early instead of allowing incomplete classes to run silently.






# Pehle Yaad Karo @property

# Humne padha tha:

# @property
# def salary(self):
#     ...

# Internally (conceptually):

# salary = property(salary)

# Yaani Python ne ek naya Property Object bana diya.

# Isliye salary ab function nahi raha.

# Wo property object ban gaya.




# @abstractmethod Yahan Python naya object nahi banata. Wo same function object ko modify karta hai. Technically function object hi return hota hai, lekin uske andar ek special information attach ho jati hai. Yaani function wahi hai, bas uspar ek sticker lag gaya

# Function Object

# Name : sound

# Code : pass

# Abstract Flag = True


# Difference Between @property and @abstractmethod
# @property	|  @abstractmethod
# Function ko Property Object me wrap karta hai |	Function ko abstract mark karta hai
# New property object create hota hai |	Function object hi rehta hai
# Getter/Setter manage karta hai  |	Abstract flag/metadata attach karta hai
# Attribute jaisa access deta hai |	Child ko implementation ke liye force karta hai


# Q. What does @abstractmethod do internally?

# @abstractmethod does not create a new property-like object. It marks the function as abstract by attaching metadata to it. Later, when Python creates an object of a child class, it checks whether all abstract methods have been implemented. If not, it raises a TypeError.


# Interview Gold Question

# Interviewer:

# Can an abstract method have implementation in Python?

# Correct answer:

# Yes. Unlike some languages, Python allows abstract methods to contain implementation. Child classes must still override the method, but they can call the parent implementation using super() if they want to reuse common behavior.