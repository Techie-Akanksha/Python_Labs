# Concept 1: List Comprehension

# Normal approach:

# numbers = [1, 2, 3, 4, 5]

# squares = []

# for n in numbers:
#     squares.append(n * n)

# print(squares)

# Output:

# [1, 4, 9, 16, 25]

# List comprehension gives us a shorter way:

# numbers = [1, 2, 3, 4, 5]

# squares = [n * n for n in numbers]

# print(squares)

# Same result.

# The basic pattern is:

# [expression for variable in iterable]

# So:

# [n * n for n in numbers]

# means:

# Take each n from numbers
#         ↓
# calculate n * n
#         ↓
# put result into a new list
# With condition
# even = [n for n in numbers if n % 2 == 0]

# Flow:

# 1 → odd → skip
# 2 → even → add
# 3 → odd → skip
# 4 → even → add
# 5 → odd → skip

# Result:

# [2, 4]
# Interview answer

# "List comprehension is a concise way to create a new list by applying an expression to each item of an iterable, optionally using a condition."

# Concept 2: map()

# map() applies a function to every item.

# numbers = [1, 2, 3, 4]

# def square(n):
#     return n * n

# result = map(square, numbers)

# print(list(result))

# Flow:

# numbers
#    ↓
# 1 → square → 1
# 2 → square → 4
# 3 → square → 9
# 4 → square → 16
#    ↓
# [1, 4, 9, 16]

# So:

# map(square, numbers)

# means:

# Apply square() to every element of numbers.

# Interview answer

# "map() applies a function to each item of an iterable and returns a map iterator containing the transformed values."

# Notice that we used:

# list(result)

# because map() returns an iterator-like object, not an ordinary list directly.

# Concept 3: filter()

# filter() keeps only the elements that satisfy a condition.

# numbers = [1, 2, 3, 4, 5, 6]

# def is_even(n):
#     return n % 2 == 0

# result = filter(is_even, numbers)

# print(list(result))

# Flow:

# 1 → is_even → False → reject
# 2 → is_even → True  → keep
# 3 → is_even → False → reject
# 4 → is_even → True  → keep
# 5 → is_even → False → reject
# 6 → is_even → True  → keep

# Result:

# [2, 4, 6]
# Interview answer

# "filter() applies a function to the elements of an iterable and keeps only the elements for which the function returns True."

# 🔥 The difference

# Remember this:

# LIST COMPREHENSION → create/transform a list
# map()              → transform every item
# filter()           → select certain items

# Example:

# numbers = [1, 2, 3, 4, 5]

# Transform:

# [n * 2 for n in numbers]

# → [2, 4, 6, 8, 10]

# Map:

# list(map(lambda n: n * 2, numbers))

# → [2, 4, 6, 8, 10]

# Filter:

# list(filter(lambda n: n % 2 == 0, numbers))

# → [2, 4]

# So we're already learning concepts that connect directly to your previous lambda + higher-order function topic.