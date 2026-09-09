# Function
# A function is a reusable block of code created to perform a particular task.

# Now parameters
# def greet(name):
#     print("Hello", name)

# greet("Ash")

# Here:

# name → parameter
# "Ash" → argument
# When greet("Ash") executes, "Ash" is passed to name
# Then print() executes.

# Now return

# result is a local variable inside the function.
# return result takes the value stored in result and sends that value back to the place where the function was called.

# print ≠ return
# def add(a, b):
#     print(a + b)

# This displays the result.

# But:

# def add(a, b):
#     return a + b

# This sends the value back to the caller.


# When Python sees a variable inside a function, it generally searches:

# L → E → G → B

# This is called the LEGB rule:

# L = Local → current function
# E = Enclosing → outer/nested function
# G = Global → module level
# B = Built-in → Python's built-ins like len, print, sum

# Python first looks in the current local scope. If it doesn't find the variable, it looks outward.

# 1. global keyword

x = 100

def test():
    global x
    x = 50

test()

print(x)

# The global keyword allows a function to modify a variable defined in the global scope.

# 2. Enclosing scope

# This happens when we have a function inside another function.
def outer():
    x = 100

    def inner():
        print(x)

    inner()

outer()
# This is the E in LEGB.

# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# 1. *args

# Allows a function to receive multiple positional arguments.

# 2. **kwargs

# Allows a function to receive multiple keyword arguments.

# 3. How Python packs those arguments

# This is the important internal understanding.

def add(*args):
    print(args)

add(10, 20, 30, 40)

# One important distinction

# args itself is just the parameter name. The * tells Python:

# "Take all extra positional arguments and pack them into a tuple."

def add(*args):
    return sum(args)

print(add(10, 20, 30, 40))

# Now **kwargs

def student(**kwargs):
    print(kwargs)

student(name="Ash", age=24, city="Mumbai")

# kwargs → {
#     "name": "Ash",
#     "age": 24,
#     "city": "Mumbai"
# }

# One more important thing: * has two jobs

# You should know this because it comes up constantly.

# Packing
# def test(*args):
#     print(args)

# Here * packs multiple arguments into a tuple.

# Unpacking
# numbers = [10, 20, 30]

# print(*numbers)

# Here * unpacks the list:

# [10, 20, 30]
#      ↓
#    *numbers
#      ↓
# 10 20 30

# Similarly:

# data = {"name": "Ash", "age": 24}

# test(**data)

# def test(*args):
#     print(args)

# data = {"name": "Ash", "age": 24}

# test(**data)

# ** unpacks the dictionary into keyword arguments.
