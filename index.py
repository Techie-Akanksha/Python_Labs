# ⭐Topic - map()

# map() ka purpose:
# Iterable ke har element par ek function apply karna.

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# numbers
#  ↓
# 1 → lambda → 1
# 2 → lambda → 4
# 3 → lambda → 9
# 4 → lambda → 16
#  ↓
# [1, 4, 9, 16]

# 🎤 Interview explanation
# map() applies a given function to every item of an iterable and returns a map object containing the results. We often convert it to a list when we want to see or store the results as a list.

# Quick challenge
# Convert this using map() + lambda:
numbers = [2, 4, 6, 8]
# Expected:[4, 8, 12, 16]

calculation = list(map(lambda x:x*2, numbers))
print(calculation)

# numbers = [2, 4, 6, 8]

# 2 → x*2 → 4
# 4 → x*2 → 8
# 6 → x*2 → 12
# 8 → x*2 → 16

# → map object
# → list()
# → [4, 8, 12, 16]

# 🎤 Interview explanation
# map() applies a function to every element of an iterable and returns a map object containing the transformed values.