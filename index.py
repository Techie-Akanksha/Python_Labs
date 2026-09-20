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