# ⭐Topic - filter()

# map() = transform
# filter() = select

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# 🎤 Interview explanation
# filter() selects elements from an iterable based on a condition. It returns a filter object containing the elements for which the function returns True.

# map()    → change/transform every item
# filter() → select some items


# ⚡ Quick challenge
# Given:
numbers = [10, 15, 20, 25, 30, 35]
# Using filter() + lambda, get numbers divisible by 10.Expected:[10, 20, 30]
calculation = list(filter(lambda x: x % 10 == 0, numbers))
print(calculation)

# 🎤 Interview explanation
# filter() takes a function and an iterable, tests each element against the condition, and returns only the elements for which the function returns True.

# 🔥 Lock this difference
# Function	Purpose
# map()	Transform every element
# filter()	Select elements based on condition
# lambda	Small anonymous function

# Example:
map(lambda x: x * 2, numbers) # → change values
filter(lambda x: x % 10 == 0, numbers) # → select values