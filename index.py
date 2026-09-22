# Magic/ Dunder Methods

# 1) __str__() :- __str__() batata hai ki object ko string/text ke form mein represent karna ho to kya return karna hai.

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
s = Student("Ash")

print(s)

#Conceptually Python object ko print karte waqt uski string representation maangta hai.

# print(s)
#    ↓
# Python asks for string representation
#    ↓
# __str__() runs
#    ↓
# self → s
#    ↓
# self.name → "Ash"
#    ↓
# return "Ash"
#    ↓
# print "Ash"

# Interview mein simple answer:
# __str__() is a special method that defines the human-readable string representation of an object. It is called when we use str(object) or normally when we print the object.



# self is a parameter/reference that refers to the current object while the method is executing.

# print(s) mein Python ko object ko string representation mein convert karna padta hai. Isi process mein __str__() ka role aata hai.

# "__str__() is a special method used to define the human-readable string representation of an object. It is commonly used when an object is passed to print() or str()."


# 2)__len__():- __len__() Python ko batata hai: Jab mere object par len() use kiya jaye, toh kaunsi value return karni hai.

# Normally: Python ko pata hai ki list ki length kaise nikalni hai.Lekin agar hum apna class banayein: 

class Student:
    def __init__(self, name):
        self.name = name

s = Student("Ash")

# print(len(s)) #TypeError: object of type 'Student' has no len()

# Toh Python ko automatically nahi pata ki Student object ki "length" kya hai. Yahan hum __len__() define kar sakte hain.


class Students:

    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

s = Students(["Ash", "Rahul", "Priya"])

print(len(s))


# len(s)
#    ↓
# Python looks for __len__()
#    ↓
# __len__(s)
#    ↓
# self.students
#    ↓
# ["Ash", "Rahul", "Priya"]
#    ↓
# len(...) → 3
#    ↓
# return 3


# Suppose tum ek ShoppingCart class bana rahi ho:

class ShoppingCart:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()

cart.items.append("Laptop")
cart.items.append("Mouse")

print(len(cart))

# So instead of: len(cart.items)

# we can simply write: len(cart)
# That's the practical benefit of a dunder method.

# __len__() is a special method that defines the behavior of len() for a custom object.

class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["Ash", "Rahul", "Priya", "Neha"])

print(len(team))

# __len__() mein hum len() function ko define nahi kar rahe, balki ye define kar rahe hain ki hamare custom Team object par len(team) use hone par kya result milega.


# len(team)
#    ↓
# __len__(team)
#    ↓
# self → team
#    ↓
# self.players
#    ↓
# ["Ash", "Rahul", "Priya", "Neha"]
#    ↓
# len(self.players)
#    ↓
# 4


# __len__() is a special method that defines what len() should return when it is used with a custom object.




# 3) __eq__()
class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


s1 = Student("Ash")
s2 = Student("Ash")

print(s1 == s2)


# Normally agar yaha ham __eq__() nahi lagate to s1 == s2 ka output false hoga. kyuki name ke value chahe same ho par unke objects alag hai to final output false hoga.

# s1 == s2
#    ↓
# __eq__(s1, s2)
#    ↓
# self.name == other.name
#    ↓
# "Ash" == "Ash"
#    ↓
# True


# Interview answer

# __eq__() is a special method used to define how two objects should be compared using the == operator.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.name == other.name


e1 = Employee("Ash", 30000)
e2 = Employee("Ash", 50000)
e3 = Employee("Rahul", 30000)

print(e1 == e2)
print(e1 == e3)

# == operator object different hone ki wajah se false return karta hai. Ye jab custom __eq__() define nahi hota tab generally default behavior ko describe karta hai.

#Lekin __eq__() define karne ke baad: e1 == e2

#Python effectively: e1.__eq__(e2) call karta hai.

# mein objects compare nahi ho rahe, balki humne specifically names compare karne ka rule define kiya hai.

# e1 == e2
#    ↓
# __eq__(e1, e2)
#    ↓
# self       → e1
# other      → e2
#    ↓
# self.name == other.name
#    ↓
# "Ash" == "Ash"
#    ↓
# True




# __eq__() sirf "comparison karne wala method" nahi hai.

# More accurately:

# It allows us to define what equality means for our custom objects.

# 4) __add()__
# Python ko pata hai numbers ke liye + ka meaning addition hai. Strings ke liye: Yahan + ka meaning concatenation hai.

# Lekin custom objects? Yahan Python ke paas automatically koi meaningful rule nahi hai ki:"Do Product objects ko + karne ka matlab kya hai?"

# __add__() defines what should happen when the + operator is used with objects of our class.

class Product:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price 

p1 = Product(100)
p2 = Product(200)

print(p1 + p2) #Product.__add__(p1, p2)


# p1 + p2
#    ↓
# __add__(p1, p2)
#    ↓
# self → p1
# other → p2
#    ↓
# self.price + other.price
#    ↓
# 100 + 200
#    ↓
# 300
#    ↓
# print(300)

# Real-world use

# Suppose tum Cart class bana rahi ho:

class Cart:

    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return self.total + other.total

cart1 = Cart(500)
cart2 = Cart(700)

print(cart1 + cart2)

# Two Cart objects ko add karna = unke total amounts ko add karna.

# What is __add__() in Python?
# "__add__() is a special method that defines the behavior of the + operator for custom objects. It allows us to specify how two objects of a class should be added."


# __add__() ka distinction clear karte hain.__add__() result number de sakta hai ya new object bhi de sakta hai?

# Case A — __add__() returns a normal value
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance
a1 = BankAccount(5000)
a2 = BankAccount(3000)

result = a1 + a2

# result BankAccount object nahi hai. It's just an integer.

# a1 + a2
#    ↓
# __add__(a1, a2)
#    ↓
# self.balance + other.balance
#    ↓
# 5000 + 3000
#    ↓
# 8000 result → 8000

# Case B — __add__() returns a new object

# Hum likh sakte hain:

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)
    
result = a1 + a2

print(result.balance)

# a1 + a2
#    ↓
# __add__(a1, a2)
#    ↓
# 5000 + 3000
#    ↓
# BankAccount(8000)
#    ↓
# NEW OBJECT

# ⭐ The distinction

# __add__() ka job sirf "addition karna" nahi hai. 
# Its job is: Define what + means for your custom objects.


# __add__() takes self and other. self refers to the first object and other refers to the second object involved in the + operation. The method defines what should happen when two BankAccount objects are added.