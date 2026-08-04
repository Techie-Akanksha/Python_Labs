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


class Animal:

    def sound(self):
        pass


class Dog(Animal):
    pass


d = Dog()

d.sound()

# Tumhari Reasoning Ko Interview Level Banate Hain

# Agar interviewer pooche:

# Why is this design bad?

# Tum aise answer de sakti ho:

# This design is not good because the parent class provides an empty implementation using pass. If a child class forgets to override the method, the program still runs without any error. This can hide bugs. An abstract class solves this problem by forcing every child class to implement the required method.

