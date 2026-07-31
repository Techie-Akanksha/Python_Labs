# # 📚 Aaj Tak Humne Kya Seekha?

# ### ✅ Encapsulation

# * Data ko direct access se protect karna.
# * Controlled access provide karna.
# * `__` security ke liye nahi, **name mangling** ke liye hai.
# * Accidental access se bachata hai.

# ---

# ### ✅ Getter & Setter

# Getter

# ```python
# emp.get_salary()
# ```

# * Data read karta hai.
# * Validation, logging, calculation kar sakta hai.

# Setter

# ```python
# emp.set_salary(50000)
# ```

# * Data update karta hai.
# * Validation laga sakta hai.

# ---

# ### ✅ `@property`

# Without property

# ```python
# emp.get_salary()
# emp.set_salary(50000)
# ```

# With property

# ```python
# print(emp.salary)

# emp.salary = 50000
# ```

# Internally:

# ```text
# emp.salary
#      ↓
# Getter execute
# ```

# ```text
# emp.salary = 50000
#         ↓
# Setter execute
# ```

# ---

# # 🧠 Sabse Important Concept

# Ab tumhe ye difference clear hona chahiye.

# ### Object Memory

# ```python
# self.salary
# ```

# Matlab:

# ```text
# Object ke andar attribute
# ```

# ---

# ### Local Memory

# ```python
# salary = self.salary
# ```

# Matlab:

# ```text
# Ek naya local variable
# ```

# ---

# ### Direct Return

# ```python
# return self.salary
# ```

# Matlab:

# ```text
# Object se value lekar directly return.
# ```

# Koi naya local variable create nahi hota.
