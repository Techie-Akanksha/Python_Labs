# ⭐Topic - Lambda

# syntax
# function_name = lambda parameter: expression

# Lambda is basically a small anonymous function.

# Normal function
def square(x):
    return x * x

#Lambda Function
square = lambda x: x*x

square(5)

add = lambda a, b : a+b
print(add(5,6))


# 🎤 Interview explanation
# A lambda function is a small anonymous function written using the lambda keyword. It can take multiple arguments but contains a single expression whose result is returned automatically.


# When to use: Usually for short, simple operations, especially with functions like map(), filter(), and sorted().