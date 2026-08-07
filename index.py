# isinstance()

# Ye Python ka ek built-in function hai.Iska kaam hai: Check karna ki koi object kisi particular class ka hai ya nahi.

# Syntax:

# isinstance(object, ClassName)

# Ye hamesha return karta hai:

# True
# False

class Dog:
    pass

d = Dog()

print(isinstance(d, Dog)) #True : Kyuki d Dog class ka object hai.

class Dog:
    pass

class Cat:
    pass

d = Dog()

print(isinstance(d, Cat)) #False : Kyuki d Dog class ka object hai, Cat class ka nahi.


#Ab Duck Typing Wala Example

class Pen:
    def write(self):
        print("Writing")


class Keyboard:
    def write(self):
        print("Typing")

# Agar kisi ko Duck Typing nahi pata ho, to wo aisa code likh sakta hai:

def create_notes(device):
    if isinstance(device, Pen):
        device.write()
    elif isinstance(device, Keyboard):
        device.write()
    else:
        print("Device not supported")

        # Dono cases me same kaam ho raha hai.

    # Duck Typing kehta hai:

def create_notes(device):
    device.write()


class AIWriter:
    def write(self):
        print("AI is writing...")

# isinstance() wala code Ab tumhe function modify karna padega.

def create_notes(device):

    if isinstance(device, Pen):
        device.write()

    elif isinstance(device, Keyboard):
        device.write()

    elif isinstance(device, AIWriter):
        device.write()

# Har nayi class ke saath function badalna padega.

# Duck Typing

# Function me kuch bhi change nahi.

# def create_notes(device):
#     device.write()

# Bas AIWriter me write() hona chahiye.

# Isliye Duck Typing code ko zyada flexible banata hai.







# Interview Ke Liye Bas Itna Yaad Rakhna

# isinstance():

# Checks whether an object is an instance of a particular class (or its subclasses). It returns True or False.