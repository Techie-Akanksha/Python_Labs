# topic : Composition vs Inheritance

# "IS-A" relationship hai?

# → Inheritance

# "HAS-A" relationship hai?

# → Composition

# ⭐ Inheritance = IS-A
# Dog IS-A Animal

class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")

dog = Dog()

dog.eat()
dog.bark()

# Dog ko Animal ke behavior mil sakte hain.

# Inheritance ka matlab:

# Ek class doosri class se properties/behaviors inherit karti hai because there is an IS-A relationship.

# ⭐ Composition = HAS-A
# Car HAS-A Engine

class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()

car.engine.start()

# Car object ke andar ek Engine object ka reference rakha gaya hai.

# Interview:
# "When should you use composition instead of inheritance?"

# Use inheritance when there is a genuine IS-A relationship and the child should follow the parent abstraction. Use composition when one object needs to contain or use another object, representing a HAS-A relationship.

# Aur ek common design principle:
# Prefer composition over inheritance when inheritance doesn't represent a natural IS-A relationship.

# Ek important practical point

class Car:
    def __init__(self):
        self.engine = Engine()

# Composition mein generally hum object ko attribute ke andar rakhte hain:

# Car Object
#     │
#     └── engine → Engine Object

# Composition = object contains/uses another object.
# Inheritance = class extends another class.