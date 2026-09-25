# ⭐Topic - Iterators

# Iterator ko simple way mein samjho:
# An iterator is an object that gives you elements one at a time.

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

# Internal flow
# numbers
#    ↓
# iter(numbers)
#    ↓
# iterator
#    ↓
# next() → 10
#    ↓
# next() → 20
#    ↓
# next() → 30

# Iterator current position maintain karta hai.
# Agar:
print(next(it))
# again karoge, ab koi next element nahi hai, so:
StopIteration

# 🎤 Interview explanation
# An iterator is an object that allows us to traverse through elements one at a time using the next() function. It maintains its current state during iteration.

# ⭐ iter() vs next()

# iter() → creates/gets iterator
# next() → gets next element


numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))

for x in it:
    print(x)

# 🎤 Interview explanation
# An iterator maintains its current position, so after calling next() twice, the for loop continues from the next remaining element instead of starting again.