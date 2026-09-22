# MRO kya hai?

#⭐ MRO = Method Resolution Order

# Simple language mein:

# Jab Python ko kisi method ya attribute ko find karna hota hai, especially inheritance/multiple inheritance mein, Python jis order mein classes ko search karta hai us order ko MRO kehte hain.

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass

d = D()
d.show()

#⭐ MRO dekh kaise sakte hain?

# Python mein:

print(D.mro())

# ya:

print(D.__mro__)

#⭐ super() aur MRO ka connection 🔥

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(B):
    def show(self):
        print("C")
        super().show()

c = C()
c.show()

# super() ka matlab simply:

# "Parent class ko call karo"

# ye hamesha exact immediate parent ko call kare — multiple inheritance mein ye wording incomplete hai.

# Better:

# super() MRO ke according next class/method ko access karta hai.

# Ye interview mein stronger answer hai.

#⭐ Multiple inheritance mein super() ka magic
class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()

d = D()
d.show()


# D.show()
#  ↓
# print("D")
#  ↓
# super()
#  ↓
# B.show()
#  ↓
# print("B")
#  ↓
# super()
#  ↓
# C.show()
#  ↓
# print("C")
#  ↓
# super()
#  ↓
# A.show()
#  ↓
# print("A")

# ⭐ Important

# Notice:
# B ka parent directly A hai.
# But B ke andar:super().show()
# ne C ko call kiya, A ko directly nahi.
# Why?Because super() MRO follow karta hai.
# MRO:D → B → C → A
# B ke baad MRO mein C hai.That's why C execute hua.

# super() follows the Method Resolution Order. It calls the next class in the MRO rather than simply calling the immediate parent class.


# ⭐Multiple Inheritance ka practical side: super() + Constructor Chaining
# MRO samajh liya, ab dekhte hain ki constructors ke saath MRO kaise work karta hai.

class A:
    def __init__(self):
        print("A constructor")


class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()


class C(A):
    def __init__(self):
        print("C constructor")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D constructor")
        super().__init__()


d = D()

# D.__init__()
#    ↓
# print("D constructor")
#    ↓
# super()
#    ↓
# B.__init__()
#    ↓
# print("B constructor")
#    ↓
# super()
#    ↓
# C.__init__()
#    ↓
# print("C constructor")
#    ↓
# super()
#    ↓
# A.__init__()
#    ↓
# print("A constructor")

# ⭐ Most important point

# Tumne jo bola:

# "super() MRO mein next class ko call karega."

# Exactly.

# Bas interview mein thoda precise bolna:

# super() calls the next implementation according to the class's MRO. It does not simply mean "call my parent."


#⭐ One subtle point

# Agar B ka direct parent A hai, phir bhi:
B.__init__()
    # ↓
super().__init__()

# C ko call kar sakta hai, because B ko D ke context mein execute kiya ja raha hai aur D ka MRO hai: