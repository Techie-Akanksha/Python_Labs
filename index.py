# ⭐Topic - Generators

# A generator is a simple way to create an iterator using yield.

# Jab Normal function def numbers():return [1, 2, 3] create karte hai to Ye saare values ek saath return karta hai.

# Generator

def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)

# 🧠 Main difference
# return:
# return → function ends
    #      ↓
    #  value returned

# yield:

# yield → one value
#         ↓
#       pause
#         ↓
# next request
#         ↓
# resume
#         ↓
# next yield


# That's why generators are memory efficient when dealing with large sequences.

# Example
# Imagine 10 million records.
# Normal list:Could require a lot of memory.

# Generator
# def get_data():
    # for i in range(10_000_000):
        # yield i
# Values are produced one at a time instead of creating the entire list upfront.

# 🎤 Interview explanation
# A generator is a function that uses yield to produce values one at a time. It pauses its execution after each yield and resumes when the next value is requested. This makes generators memory-efficient for large or streamed data.

# ⚡ Quick challenge
def count():
    yield 1
    yield 2
    yield 3

c = count()

print(next(c))
print(next(c))

for x in c:
    print(x)

# After yield 2 returns the value, the generator pauses immediately after that yield statement. On the next next() call, execution resumes from the next line after yield 2.

# 🎯 Interview answer
# A generator is a function that uses yield to produce values one at a time. It pauses execution after each yield and resumes from the same point when the next value is requested. This makes generators memory-efficient for large amounts of data.


# 🧠 Interview Comparison (Very Important)
# List  |	Generator
# Stores all values in memory |	Produces one value at a time
# More memory usage |	Less memory usage
# Uses [] |	Uses yield
# Good for small data |	Good for large data


# Interview Question
# Q: Why use a generator instead of a list?
# Answer:
# A generator produces values one at a time using yield, so it consumes less memory. It is useful when working with large datasets or streams of data because it doesn't create the entire collection in memory at once.