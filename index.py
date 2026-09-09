# Let's understand First-Class Functions

# You already understand this:

# x = 10

# 10 is a value, and we can store that value in x.

# Python also treats a function as an object.

# Look:

# def greet():
#     print("Hello")

# When Python executes this definition, it creates a function object.

# Conceptually:

# greet ──────────→ Function Object

# Now:

# x = greet

# We are saying:

# "Make x refer to the same function object that greet refers to."

# So:

# greet ───────┐
#              ↓
#         Function Object
#              ↑
#              │
# x ───────────┘

# Now:

# x()

# works.

# Why?

# Because x refers to a function object.

# So x() means:

# Call the function object referred to by x.

# This is the key idea

# Python allows functions to be treated like normal objects/values.

# That's what first-class functions means.

# Interview answer

# If interviewer asks:

# "What are first-class functions in Python?"

# You can say:

# "Python treats functions as first-class objects. This means functions can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures."

# That's a strong interview answer.

# Now Higher-Order Function

# This becomes easy once first-class functions are clear.

# Look:

# def greet():
#     print("Hello")

# def execute(func):
#     func()

# execute(greet)

# Let's follow it.

# Step 1

# Python creates:

# greet → function object
# execute → function object
# Step 2

# We call:

# execute(greet)

# Notice something important:

# greet

# NOT:

# greet()

# We're passing the function itself, not calling it yet.

# So:

# greet ─────→ Function Object
#                   ↓
#               passed to
#                   ↓
# execute(func)

# Inside execute:

# func = greet

# Conceptually:

# func ─────→ same Function Object

# Then:

# func()

# calls that function.

# Therefore:

# execute(greet)
#        ↓
# func refers to greet
#        ↓
# func()
#        ↓
# greet()
#        ↓
# Hello
# Why is execute() called a Higher-Order Function?

# Because it takes another function as an argument.

# def execute(func):

# func is a function received as an argument.

# Therefore:

# A higher-order function is a function that takes another function as an argument or returns a function.

# Interview answer

# "A higher-order function is a function that accepts another function as an argument or returns a function."

# Examples you'll later see:

# map()
# filter()
# sorted()

# These commonly work with functions.

# Now Lambda

# Lambda is actually the easiest of the three.

# Normally:

# def square(x):
#     return x * x

# Lambda:

# square = lambda x: x * x

# Think:

# lambda x: x * x
#        ↓
# input x
#        ↓
# x * x
#        ↓
# returned result

# So:

# square(5)

# returns:

# 25
# Interview answer

# "A lambda function is a small anonymous function written using the lambda keyword. It can take multiple arguments but contains a single expression."

# 🔥 Now connect all 3

# This is where it finally makes sense:

# square = lambda x: x * x

# def execute(func, value):
#     return func(value)

# result = execute(square, 5)

# Think step-by-step:

# lambda
#   ↓
# creates function object
#   ↓
# square refers to it
#   ↓
# square is passed to execute()
#   ↓
# func refers to same function
#   ↓
# func(5)
#   ↓
# 5 * 5
#   ↓
# 25
#   ↓
# result = 25

# So:

# Concept	Meaning
# First-class function	Function can be treated like an object/value
# Higher-order function	Function accepts/returns another function
# Lambda	Short way to create a small anonymous function
# The relationship
# Lambda
#    ↓
# creates a function
#    ↓
# Function is first-class
#    ↓
# can be passed around
#    ↓
# Higher-order function can receive it

# That's the connection you were missing.

# One important correction

# Don't think:

# "func contains the function's output."

# No.

# Here:

# execute(square, 5)

# func refers to the function itself.

# Only when we do:

# func(5)

# does the function execute and produce 25.

# That's a very important interview distinction.