#⭐ Topic: Exception Handling — try, except, else, finally

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Calculation successful.")

finally:
    print("Program finished.")


# 1. try

# Risky code yahan:

# try:
#     num = int(input())
#     result = 10 / num

# Python normally execute karega.


# 2. except

# Agar try ke andar error aaya, matching except execute hota hai.

# For example:

# input → "abc"
# int("abc")

# raises:

# ValueError

# So:

# except ValueError:

# execute hoga.

# 3. Multiple except

# Different errors ko separately handle kar sakte ho:

# except ValueError:
#     ...

# except ZeroDivisionError:
#     ...

# For:

# input → 0

# int(0) works, but:

# 10 / 0

# gives ZeroDivisionError.

# 4. else

# else tab execute hota hai jab try successfully complete ho jaye aur koi exception na aaye.

# try successful
#       ↓
#     else
# 5. finally

# finally almost always execute hota hai, chahe error aaye ya na aaye.

# Common use:

# file close karna
# database connection cleanup
# resources release karna

# Flow:

#               try
#              /   \
#         success   error
#            ↓        ↓
#          else    except
#              \    /
#               finally

# 🎯 Interview answer

# Q: What is exception handling in Python?

# Exception handling is a mechanism used to handle runtime errors without abruptly terminating the program. Python provides try, except, else, and finally blocks for this purpose.

try:
    print("A")
    x = 10 / 0
    print("B")

except ZeroDivisionError:
    print("C")

else:
    print("D")

finally:
    print("E")

print("F")

# try
#  ↓
# A print
#  ↓
# 10 / 0
#  ↓
# ZeroDivisionError
#  ↓
# B ❌ skip
#  ↓
# except
#  ↓
# C print
#  ↓
# else ❌ skip
#  ↓
# finally
#  ↓
# E print
#  ↓
# F print

# One important interview point

# else sirf tab execute hota hai jab try mein exception nahi aata.

# finally ka purpose cleanup hota hai, aur normal exception flow mein woh execute hota hi hai—even when an exception occurs.


#⭐ Next concept: raise

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount

# Yahan Python automatically error nahi de raha tha. Humne condition check karke khud exception raise ki.

# amount > balance?
#        ↓
#       YES
#        ↓
# raise ValueError
#        ↓
# function stops

try:
    balance = withdraw(5000, 7000)
except ValueError as e:
    print(e)

# Interview answer

# raise is used to explicitly trigger an exception when a specific condition occurs.

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Eligible"


try:
    print(check_age(16))
except ValueError as e:
    print(e)

# check_age(16)
#       ↓
# age < 18  → True
#       ↓
# raise ValueError(...)
#       ↓
# function stops
#       ↓
# "Eligible" ❌ nahi chalega
#       ↓
# except ValueError as e
#       ↓
# e = ValueError object
#       ↓
# print(e)

# ⭐ as e ko specifically samjho
# except ValueError as e:
#     print(e)

# Yahan e error/exception object ka reference hai.

# Agar hum likhte:

# except ValueError:
#     print("Something went wrong")

# toh hum exception ko directly access nahi kar rahe.

# as e useful hota hai jab hume actual error message/details inspect ya log karni ho.

# Interview answer

# raise explicitly raises an exception, while except ... as e allows us to capture the exception object and access its details.



# ⭐Next: Custom Exceptions

# Instead of:

# raise ValueError("Age must be 18 or above")

# we can create our own exception:
class InvalidAgeError(Exception):
    pass

# Then:
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    return "Eligible"

# And handle it:
try:
    print(check_age(16))

except InvalidAgeError as e:
    print(e)


#   Why custom exception?

# Generic ValueError se pata chalta hai ki value invalid hai.

# Custom:

# InvalidAgeError

# se code ka meaning immediately clear hota hai.

# Interview line:

# Custom exceptions allow us to create application-specific error types that make error handling more meaningful and organized.


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

    return balance - amount


try:
    balance = withdraw(5000, 7000)
    print(balance)

except InsufficientBalanceError as e:
    print(e)

print("Transaction completed")


# withdraw(5000, 7000)
#         ↓
# 7000 > 5000 → True
#         ↓
# raise InsufficientBalanceError
#         ↓
# function stops
#         ↓
# except catches exception
#         ↓
# e = exception object
#         ↓
# print(e)
#         ↓
# Insufficient balance
#         ↓
# Transaction completed


# ⭐ Why custom exception?

# Tum interview mein bol sakti ho:

# Custom exceptions make application-specific errors easier to identify, handle, and maintain.