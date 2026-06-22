"""
Chapter 12 - Day 31: Instance Methods, __str__ vs __repr__, Class Variables
===========================================================================
Topics: instance methods (functions that live on objects), the __str__ and
        __repr__ special methods (and when each is used), and the difference
        between class variables (shared) and instance variables (per-object).
"""

# ============================================================
# 1. INSTANCE METHODS - behavior that belongs to the object
# ============================================================
# A method is just a function defined INSIDE a class. Its first
# parameter is always 'self' (the object it is acting on).

class Dog:
    """A dog that knows how to bark."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        """Make this dog bark. Uses self.name to know WHO is barking."""
        return f"{self.name} says: Woof!"

    def description(self):
        """Return a sentence describing this dog."""
        return f"{self.name} is {self.age} years old."

rex = Dog("Rex", 3)
print(rex.bark())          # Rex says: Woof!
print(rex.description())   # Rex is 3 years old.
# rex.bark() is shorthand for Dog.bark(rex) - self becomes rex.


# ============================================================
# 2. METHODS THAT TAKE EXTRA ARGUMENTS
# ============================================================
# 'self' is always first; any other arguments come after it.

class Dog2:
    def __init__(self, name):
        self.name = name
        self.tricks = []        # each dog starts with an empty trick list

    def learn_trick(self, trick):
        """Teach this dog a new trick."""
        self.tricks.append(trick)
        return f"{self.name} learned to {trick}!"

buddy = Dog2("Buddy")
print(buddy.learn_trick("roll over"))
print(buddy.learn_trick("play dead"))
print(f"{buddy.name}'s tricks: {buddy.tricks}")


# ============================================================
# 3. THE PROBLEM __str__ SOLVES
# ============================================================
# By default, printing an object shows an ugly memory address.

class PlainDog:
    def __init__(self, name):
        self.name = name

print("\nWithout __str__:")
print(PlainDog("Rex"))      # <__main__.PlainDog object at 0x...>


# ============================================================
# 4. __str__  vs  __repr__
# ============================================================
# __str__  -> friendly text for END USERS. Used by print() and str().
# __repr__ -> unambiguous text for DEVELOPERS. Used in the REPL,
#             in containers like lists, and as a fallback for print().
# Rule of thumb: __repr__ should ideally look like code that could
# recreate the object.

class NiceDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # Human-friendly: what a user wants to read.
        return f"{self.name} (age {self.age})"

    def __repr__(self):
        # Developer-friendly: looks like how you'd build the object.
        return f"NiceDog(name={self.name!r}, age={self.age})"

d = NiceDog("Luna", 5)
print("\nWith __str__ and __repr__:")
print(d)            # uses __str__  -> Luna (age 5)
print(str(d))       # uses __str__  -> Luna (age 5)
print(repr(d))      # uses __repr__ -> NiceDog(name='Luna', age=5)

# Inside a list, Python uses __repr__ for EACH element:
print([d, NiceDog("Rex", 3)])   # [NiceDog(name='Luna', age=5), NiceDog(name='Rex', age=3)]

# If a class defines ONLY __repr__, print() falls back to it.
class ReprOnly:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return f"ReprOnly({self.x})"

print(ReprOnly(42))     # ReprOnly(42)  - __repr__ used as fallback


# ============================================================
# 5. CLASS VARIABLES vs INSTANCE VARIABLES
# ============================================================
# INSTANCE variable: defined with self.x - one copy PER object.
# CLASS variable:    defined directly in the class body - ONE copy
#                    SHARED by every object of that class.

class Dog3:
    species = "Canis familiaris"    # CLASS variable - shared by all dogs
    count = 0                       # CLASS variable - count of dogs made

    def __init__(self, name):
        self.name = name            # INSTANCE variable - unique per dog
        Dog3.count += 1             # bump the shared counter

a = Dog3("Rex")
b = Dog3("Luna")

# Both objects SHARE the same species value:
print(f"\n{a.name}'s species: {a.species}")     # Canis familiaris
print(f"{b.name}'s species: {b.species}")        # Canis familiaris

# But each has its OWN name:
print(f"a.name={a.name}, b.name={b.name}")        # Rex, Luna

# The shared counter knows how many dogs exist:
print(f"Total dogs created: {Dog3.count}")        # 2


# ============================================================
# 6. THE SHARED-vs-PER-OBJECT GOTCHA
# ============================================================
# Reading a class variable through an instance works. But ASSIGNING
# through an instance creates a NEW instance variable that SHADOWS
# the class variable for that one object only.

a.species = "Good Boy"          # creates an instance var on 'a' ONLY
print(f"\na.species = {a.species}")     # Good Boy   (shadowed)
print(f"b.species = {b.species}")        # Canis familiaris (unchanged)
print(f"Dog3.species = {Dog3.species}")  # Canis familiaris (class var safe)


# ============================================================
# 7. HANDS-ON - Dog with bark() and a clean __str__
# ============================================================

class Dog4:
    """A dog that can bark and prints itself nicely."""

    species = "Canis familiaris"    # shared by every dog

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Return this dog's bark."""
        return f"{self.name} says: Woof! Woof!"

    def __str__(self):
        """Friendly one-line description used by print()."""
        return f"{self.name} the {self.breed} ({self.age} yrs)"

    def __repr__(self):
        return f"Dog4(name={self.name!r}, breed={self.breed!r}, age={self.age})"

print("\n--- Day 31 Hands-on ---")
rex = Dog4("Rex", "Labrador", 3)
print(rex)              # Rex the Labrador (3 yrs)   <- __str__
print(rex.bark())       # Rex says: Woof! Woof!
print(f"Species (shared): {rex.species}")
print(repr(rex))        # Dog4(name='Rex', ...)      <- __repr__
