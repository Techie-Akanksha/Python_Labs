# ⭐ Next Python topic: Comprehensions

# ⭐List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# Same thing list comprehension se:

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]
# For every num in numbers, calculate num * num and put the result into a new list.

print(squares)

# 🎯 Challenge
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# list comprehension is:

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# [what_to_store  for  variable  in  collection  if  condition]

# 1. What is Comprehension in Python?

# Comprehension is a concise way to create a new collection in Python using an existing iterable, usually with a loop and an optional condition.

# 2. What is List Comprehension?

# List comprehension is a concise way to create a new list by applying an expression to each item of an iterable, optionally filtering items using a condition.
#List comprehension is a concise way to create a new list by applying an expression to items from an iterable, optionally with a condition.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers_squares = [num*num for num in numbers if num % 2 == 0]
print(even_numbers_squares)

# ⭐ Important distinction

# Comprehension mein:

# [num * num for num in numbers if num % 2 == 0]
# for → kis data par iterate karna hai
# if → kaunse elements select karne hain
# num * num → selected element ke saath kya karna hai 