"""
Chapter 12 - Day 30: What is OOP? Classes, Objects, __init__, and self
======================================================================
Topics: the idea of objects (data + behavior), class vs object (blueprint
        vs house), the `class` keyword, the __init__ constructor, instance
        variables, and the meaning of `self`.
"""

# ============================================================
# 1. THE SIMPLEST CLASS - a blueprint with no data yet
# ============================================================
# A class is a BLUEPRINT. It describes what every object of this
# type will look like. By itself it builds nothing - just like a
# house blueprint is not a house you can live in.

class Dog:
    """A blueprint for creating dog objects."""
    pass        # 'pass' means 'empty body for now'

# Creating an OBJECT (also called an INSTANCE) from the blueprint.
# Calling the class like a function builds one real dog.
my_dog = Dog()
print(my_dog)               # something like <__main__.Dog object at 0x...>
print(type(my_dog))         # <class '__main__.Dog'>


# ============================================================
# 2. ADDING DATA WITH __init__ (THE CONSTRUCTOR)
# ============================================================
# __init__ runs automatically every time you create an object.
# Its job: set up the starting data for that specific object.
# 'self' is the object being built right now.

class Dog2:
    """A dog with a name, breed, and age."""

    def __init__(self, name, breed, age):
        # self.name creates an INSTANCE VARIABLE living on THIS object.
        self.name = name        # store the passed-in name on the object
        self.breed = breed
        self.age = age

# We pass name, breed, age. We do NOT pass self - Python fills it in.
rex = Dog2("Rex", "Labrador", 3)
luna = Dog2("Luna", "Poodle", 5)

# Each object carries its OWN copy of the data.
print(f"{rex.name} is a {rex.age}-year-old {rex.breed}")
print(f"{luna.name} is a {luna.age}-year-old {luna.breed}")


# ============================================================
# 3. WHAT IS 'self'? - it is just 'this particular object'
# ============================================================
# When you call a method like rex.some_method(), Python turns it into
# Dog2.some_method(rex) behind the scenes. So inside the method, 'self' IS rex.
# 'self' is not a keyword - it is just a naming convention. But ALWAYS
# use 'self' so other Python programmers understand your code.

class Counter:
    """Shows that self points at the specific object."""

    def __init__(self, start):
        self.value = start

# Two independent counters - each has its own self.value
a = Counter(0)
b = Counter(100)
print(f"a.value = {a.value}, b.value = {b.value}")   # 0 and 100


# ============================================================
# 4. OBJECTS BUNDLE DATA TOGETHER (vs loose variables)
# ============================================================
# Without OOP we might track a dog with three separate variables:
dog_name = "Buddy"
dog_breed = "Beagle"
dog_age = 2
print(f"\nLoose variables: {dog_name}, {dog_breed}, {dog_age}")

# That gets messy fast with many dogs. An object keeps related data
# neatly bundled into one tidy package:
buddy = Dog2("Buddy", "Beagle", 2)
print(f"Bundled object : {buddy.name}, {buddy.breed}, {buddy.age}")


# ============================================================
# 5. CHANGING AN OBJECT'S DATA AFTER CREATION
# ============================================================
# Instance variables are just variables - you can read and update them.

print(f"\nBefore birthday: {rex.name} is {rex.age}")
rex.age = rex.age + 1           # the dog had a birthday!
print(f"After birthday : {rex.name} is {rex.age}")


# ============================================================
# 6. PUTTING IT TOGETHER - the Day 30 hands-on Dog class
# ============================================================

class Dog3:
    """A dog described by its name, breed, and age."""

    def __init__(self, name, breed, age):
        """Set up a new dog with the given details."""
        self.name = name
        self.breed = breed
        self.age = age

# Build a small pack of dogs and describe each one.
pack = [
    Dog3("Rex", "Labrador", 3),
    Dog3("Luna", "Poodle", 5),
    Dog3("Coco", "Bulldog", 1),
]

print("\n--- Our Dog Pack ---")
for dog in pack:
    print(f"{dog.name:5} | breed: {dog.breed:9} | age: {dog.age}")
