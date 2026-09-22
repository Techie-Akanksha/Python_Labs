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