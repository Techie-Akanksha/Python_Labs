# @property allows a method to be accessed like an attribute while still keeping full control over the logic.

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person(20)

print(p.age)
p.age = 30


# Developer ko lag raha hai ki woh variable access kar raha hai.

# Lekin actually internally methods call ho rahe hain.

# p.age

# ↓

# p.age()

# (jaisa behavior, lekin automatically)

# Aur

# p.age = 30

# ↓

# age.setter(30)

# Automatically.

# @property lets us expose a method as if it were a normal attribute, while still keeping the control and validation inside the method.




# Lekin Abhi Tumhe Confusion Kyu Ho Raha Hai?

# Kyunki tum soch rahi ho:

# Agar getter/setter already hai...

# To property ki zarurat hi kya hai?






# python wants Agar koi cheez data ki tarah behave karti hai, to usse data ki tarah hi access karna chahiye.

# Golden Rule
# Agar object sirf information de raha hai tab ➡️ property use karte hai

# Agar object koi kaam kar raha hai koi action perform ho rahi hai to ➡️ method use karte hai
#  emp.calculate_bonus()
# student.send_email()
# car.start_engine()



# Ek Aur Interesting Point

# Maan lo aaj tumhari class me sirf variable hai.

class Employee:
    def __init__(self):
        self.salary = 50000

# Poore project me sab likh rahe hain:
emp = Employee()
print(emp.salary)

# Ek saal baad requirement aayi:

# Salary read karte waqt access log bhi save karo.

# Agar tumne shuru se salary property use ki hoti...

# To?

# Tum andar ki implementation change kar sakti ho.

# Lekin bahar ka code:

print(emp.salary)

# Bilkul same rahega.

# 💡 Yahi @property ka sabse bada advantage hai.

# Public interface same rehta hai.

# Internal implementation change ho sakti hai.




# Interview Perspective

# Agar interviewer pooche:

# Why use @property instead of get_salary()?

# Strong answer:

# "@property provides a cleaner and more Pythonic interface. It lets users access data like a normal attribute while allowing the class to keep validation, logging, lazy computation, or other logic inside the getter method. This also preserves the public interface even if the internal implementation changes."


# What is @property in Python?

# Tum ye answer de sakti ho:

# @property is a Python decorator that allows us to access a method like a normal attribute. It helps us keep validation and other logic inside the class while providing a clean and readable interface to the user.

# Agar Interviewer Puche

# Why do we use @property when getter and setter already exist?

# Tum answer aise dena:

# Getter and setter already provide controlled access to data, but @property makes the code more readable and Pythonic. It lets users access data like a normal attribute while still allowing the developer to perform validation, logging, or calculations internally. It also keeps the public interface unchanged even if the internal implementation changes.

# We use @property to make getter and setter methods look like normal attributes. This makes the code cleaner, more readable, and allows validation without changing how users access the data.

# Interviewer:

# Why not use a normal public variable?

# Tum:

# Initially a normal variable may be enough, but later we may need validation, logging, permission checks, or calculated values. With @property, we can add that logic without changing the code that uses the class.

# "@property improves readability while preserving encapsulation and allowing future changes without affecting the code that uses the class."