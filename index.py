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


# ⭐ Very Important: __name__

# You'll commonly see:
# if __name__ == "__main__":
#     print("Program started")

# Suppose calculator.py contains:
# def add(a, b):
#     return a + b


# if __name__ == "__main__":
#     print(add(10, 20))

# If you run: python calculator.py

# Python sets : __name__ = "__main__"

# So the code executes.
# But if another file does: import calculator
# then: __name__ = "calculator"

# So the code inside: if __name__ == "__main__": 
# doesn't execute.


# Interview answer
# if __name__ == "__main__": is used to ensure that certain code runs only when the Python file is executed directly, not when it is imported as a module.

# 🎯 Quick Challenge
# Predict the output:

# # calculator.py

# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     print("Calculator started")

# Then another file:

# # main.py

# import calculator

# print(calculator.add(5, 3))


# Your execution flow was correct:
# main.py
#    ↓
# import calculator
#    ↓
# calculator module loaded
#    ↓
# __name__ = "calculator"
#    ↓
# if block skipped
#    ↓
# calculator.add(5, 3)
#    ↓
# 8



# 🎤 Interview Question
# Q: Why do we use if __name__ == "__main__":?
# Your answer can be:
# "if __name__ == '__main__': ensures that a block of code runs only when the Python file is executed directly, and not when the file is imported as a module."