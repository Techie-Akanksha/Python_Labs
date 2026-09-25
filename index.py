# ⭐Topic - Modules & Packages
# ⭐ Modules
# What is a Module?
# A module is simply a Python file (.py) containing reusable code.

# for example
# project/
# │
# ├── calculator.py
# └── main.py

# calculator.py:

# def add(a, b):
#     return a + b

# main.py:
# import calculator

# result = calculator.add(10, 20)
# print(result)

# 🧠 What happens internally?
# When Python sees:
# Python:
# 1. Finds calculator.py
# 2. Executes/load its definitions
# 3. Creates a module object
# 4. Gives your program access to its functions/classes

# means:
# Go to the calculator module and access its add() function.


#  from ... import
# Instead of:

# import calculator

# calculator.add(10, 20)

# you can write:

# from calculator import add

# print(add(10, 20))

# Now you can directly use add().
# Interview answer
# A module is a Python file containing reusable code such as functions, classes, and variables. Modules help organize code and promote code reuse.

# ⭐ Package
# A package is a directory used to organize multiple modules.

# myproject/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     ├── calculator.py
#     └── validator.py

# Here:
# - utilities → package
# - calculator.py → module
# - validator.py → module

# you can import 
# from utilities.calculator import add

# Interview answer
# A package is a directory that organizes related Python modules into a structured unit.


