# # # #Dunder Method

# # # Double Underscore + Name + Double Underscore

# # # Isliye:

# # # Dunder = Double UNDERscore

# # # Ye special methods hote hain jinko Python automatically call karta hai specific situations me.

# # # __init__ → Object create hone par.
# # # __str__ → print(obj) hone par.
# # # __len__ → len(obj) hone par.
# # # __add__ → obj1 + obj2 hone par.
# # # __eq__ → obj1 == obj2 hone par.

# # Hum in methods ko directly call nahi karte.

# # Python khud call karta hai.

# # Isi liye inhe Magic Methods bhi bolte hain.




class Student:

    def __init__(self, name):
        self.name = name

s = Student("Ash")

print(s)


# > `self` mein object ka reference store hoga.

# Thoda precise way:

# `self` **object ke andar permanently store nahi hota**. Jab method call hota hai, function ki **local execution memory/frame** me `self` parameter current object ko refer karta hai.

# Constructor:

# ```python
# def __init__(self, name):
#     self.name = name
# ```

# Jab:

# ```python
# s = Student("Ash")
# ```

# hota hai:

# ```text
# Student object create
#         ↓
# __init__(s, "Ash") conceptually
#         ↓
# self → s object
# name → "Ash"
#         ↓
# self.name = "Ash"
#         ↓
# Object Memory:
# {
#     name: "Ash"
# }
# ```

# `__init__` finish hone ke baad uski local execution memory destroy ho jaati hai, lekin:

# ```text
# name = "Ash"
# ```

# **object memory me permanently rehta hai** because `self.name` object ka attribute hai.

# ---

# # Ab `print(s)` par wapas aao

# Tumne bola:

# > object ka reference print hoga.

# ✅ **Default behavior me approximately wahi hoga.**

# Agar `Student` me `__str__` define nahi hai, Python inherited/default object representation deta hai, something like:

# ```text
# <__main__.Student object at 0x000001...>
# ```

# Exact address fixed nahi hota.

# Lekin yahan se hamara **Dunder Methods ka main concept** start hota hai.

# ---

# # 🔥 `print(s)` actually kya kar raha hai?

# Tum normally likhti ho:

# ```python
# print(s)
# ```

# Lekin Python ko decide karna hai:

# > "Is Student object ko screen par **string ke form me kaise represent karun?**"

# Python special method ko use karta hai:

# ```python
# __str__
# ```

# Conceptually:

# ```python
# print(s)
# ```

# → Python `s.__str__()` ki representation obtain karta hai.

# Aur agar tumne apna `__str__` nahi banaya, to inherited/default implementation use hoti hai.

# ---

# # Ab Dunder Method ka real meaning

# Tumne pehle padha tha:

# ```python
# __init__
# ```

# Ab connection dekho:

# | Tum kya karte ho           | Python special method |
# | -------------------------- | --------------------- |
# | Object initialize hota hai | `__init__`            |
# | `print(obj)`               | `__str__`             |
# | `len(obj)`                 | `__len__`             |
# | `obj1 + obj2`              | `__add__`             |
# | `obj1 == obj2`             | `__eq__`              |

# Isliye Dunder Methods ko hum bolte hain:

# > **Special methods that allow Python's built-in operations to work with our objects.**

# ---

# ## Ek important distinction

# Ye mat sochna:

# > "Python har baar magic se automatically random function call karta hai."

# Actually Python ke **data model me defined special methods** hote hain. Specific operation ke according interpreter unhe invoke karta hai.

# Yaani:

# ```python
# a + b
# ```

# aur

# ```python
# a.__add__(b)
# ```

# conceptually connected hain.

# Isi tarah:

# ```python
# a == b
# ```

# → `__eq__`

# Aur:

# ```python
# len(a)
# ```

# → `__len__`

# ---

# # 🧠 Gap ke baad Quick Memory Reset

# Bas ye 5 points yaad rakho:

# 1. **Class** → methods/attributes ka blueprint.
# 2. **Object** → class ka instance; instance attributes object memory me.
# 3. **self** → current object ka reference, method ki execution ke waqt.
# 4. **self.name** → object ka attribute.
# 5. **Dunder method** → Python ke special operations ke liye defined method.

