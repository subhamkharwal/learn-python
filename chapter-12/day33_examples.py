"""
Chapter 12 - Day 33: Encapsulation, Properties, @staticmethod, @classmethod
===========================================================================
Topics: encapsulation with _protected and __private (name mangling),
        controlled access using @property and @x.setter with validation,
        and the difference between @staticmethod and @classmethod.
"""

# ============================================================
# 1. ENCAPSULATION - hiding internal details
# ============================================================
# Encapsulation means bundling data with the methods that guard it,
# and signalling which parts are 'internal'. Python uses NAMING
# CONVENTIONS rather than hard locks:
#   name      -> public      (use freely)
#   _name     -> protected   (convention: "internal, please don't touch")
#   __name    -> private     (name-mangled to avoid accidental access)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # public: anyone may read/write
        self._balance = balance     # protected: internal by convention

acc = Account("Alice", 100)
print(acc.owner)            # Alice  - public, totally fine
print(acc._balance)         # 100    - Python lets you, but the _ warns "internal"


# ============================================================
# 2. __private AND NAME MANGLING
# ============================================================
# A name starting with TWO underscores gets "mangled" to
# _ClassName__name. This prevents accidental clashes in subclasses.
# It is NOT true security - just a strong "keep out" signal.

class Vault:
    def __init__(self, code):
        self.__secret_code = code       # becomes _Vault__secret_code

    def reveal(self):
        return f"The code is {self.__secret_code}"

v = Vault("1234")
print(v.reveal())           # works from inside the class

# Trying the original name from outside fails:
try:
    print(v.__secret_code)
except AttributeError as e:
    print(f"Blocked: {e}")

# The mangled name still exists (proof it's a convention, not a lock):
print(f"Mangled access: {v._Vault__secret_code}")


# ============================================================
# 3. @property - turn a method into a read-only attribute
# ============================================================
# A property lets a method be ACCESSED like a plain attribute
# (no parentheses), which is great for computed/derived values.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        """Computed on the fly, read like an attribute."""
        return 3.14159 * self._radius ** 2

c = Circle(10)
print(f"\nCircle area: {c.area}")   # note: c.area, NOT c.area()


# ============================================================
# 4. @property + @setter - controlled writes WITH VALIDATION
# ============================================================
# The getter exposes a clean public name (age). The setter runs
# validation every time someone assigns to it, protecting the
# internal _age from bad values.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age          # this calls the SETTER below (validates!)

    @property
    def age(self):
        """Read the age."""
        return self._age

    @age.setter
    def age(self, value):
        """Validate before storing the age."""
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value

p = Person("Alice", 30)
print(f"\n{p.name} is {p.age}")     # uses the getter
p.age = 31                          # uses the setter (valid) -> ok
print(f"{p.name} is now {p.age}")

# Invalid assignments are rejected by the setter:
try:
    p.age = -5
except ValueError as e:
    print(f"Rejected: {e}")


# ============================================================
# 5. @staticmethod - a function grouped under a class
# ============================================================
# A static method takes NO self and NO cls. It does not touch any
# object or class data - it's just a helper that logically belongs
# with the class. Use it for utility functions related to the class.

class MathTools:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(f"\nMathTools.add(3, 4) = {MathTools.add(3, 4)}")
print(f"MathTools.is_even(10) = {MathTools.is_even(10)}")


# ============================================================
# 6. @classmethod - receives the CLASS as the first argument
# ============================================================
# A class method takes 'cls' (the class itself) instead of 'self'.
# The classic use is an ALTERNATIVE CONSTRUCTOR - a different way to
# build an object. cls() works correctly even for subclasses.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, text):
        """Alternative constructor: build a Date from 'YYYY-MM-DD'."""
        year, month, day = (int(part) for part in text.split("-"))
        return cls(year, month, day)        # cls is Date here

d1 = Date(2026, 6, 19)              # normal constructor
d2 = Date.from_string("2026-12-25") # alternative constructor
print(f"\nDate 1: {d1}")
print(f"Date 2: {d2}")


# When to use which (quick guide):
#   instance method (self) -> needs the object's data
#   @classmethod    (cls)  -> needs the class (e.g. alt constructors, counters)
#   @staticmethod   (none) -> a related helper that needs neither


# ============================================================
# 7. HANDS-ON - Dog with a validated age property
# ============================================================

class Dog:
    """A dog whose age is protected by validation."""

    def __init__(self, name, age):
        self.name = name
        self.age = age          # routes through the setter -> validated

    @property
    def age(self):
        """Return the dog's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Reject silly ages before storing."""
        if not isinstance(value, int):
            raise TypeError("age must be a whole number")
        if value < 0:
            raise ValueError("age cannot be negative")
        if value > 30:
            raise ValueError("that is too old for a dog!")
        self._age = value

    def __str__(self):
        return f"{self.name} (age {self.age})"

print("\n--- Day 33 Hands-on ---")
rex = Dog("Rex", 3)
print(rex)                  # Rex (age 3)
rex.age = 4                 # valid update
print(rex)                  # Rex (age 4)

for bad in (-1, 99, "five"):
    try:
        rex.age = bad
    except (ValueError, TypeError) as e:
        print(f"Setting age to {bad!r} rejected: {e}")
