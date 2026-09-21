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

class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Ash")
s2 = Student("Ash")

print(s1 == s2)