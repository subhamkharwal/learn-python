"""
Chapter 12 - Day 32: Inheritance, super(), Overriding, isinstance/issubclass
============================================================================
Topics: inheritance (parent/child classes), reusing parent code with super(),
        overriding methods to specialise behavior, and checking types at
        runtime with isinstance() and issubclass().
"""

# ============================================================
# 1. THE PROBLEM INHERITANCE SOLVES - shared behavior
# ============================================================
# Dogs and cats are both animals. They share a name and age and the
# ability to eat and sleep. Without inheritance we would copy that
# code into every class. Inheritance lets a CHILD class reuse a
# PARENT class's code automatically.

class Animal:
    """Base (parent) class - common behavior for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def speak(self):
        """Generic sound. Children will OVERRIDE this."""
        return f"{self.name} makes a sound."


# 2. A CHILD CLASS that inherits everything from Animal
#    Syntax: class Child(Parent):
class Cat(Animal):
    """A Cat IS-A Animal, so it gets eat() and __init__ for free."""

    def speak(self):                    # OVERRIDE the parent's speak()
        return f"{self.name} says: Meow!"

whiskers = Cat("Whiskers", 4)
print(whiskers.eat())       # inherited from Animal -> Whiskers is eating.
print(whiskers.speak())     # overridden version    -> Whiskers says: Meow!


# ============================================================
# 3. super() - calling the PARENT's version of a method
# ============================================================
# When a child needs to ADD to the parent's setup (not replace it),
# call super().__init__(...) to run the parent constructor first,
# then add the child's own extra data.

class Dog(Animal):
    """A Dog adds a 'breed' on top of Animal's name and age."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)     # let Animal set name + age
        self.breed = breed              # then add the dog-specific bit

    def speak(self):                    # override
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

rex = Dog("Rex", 3, "Labrador")
print(rex.describe())       # Rex is a 3-year-old Labrador.
print(rex.speak())          # Rex says: Woof!
print(rex.eat())            # inherited -> Rex is eating.


# ============================================================
# 4. METHOD OVERRIDING - same name, specialised behavior
# ============================================================
# Each subclass provides its OWN speak(). Python picks the right one
# automatically based on the object's actual type. This is the heart
# of polymorphism: one call, many forms.

animals = [
    Animal("Generic", 1),
    Dog("Buddy", 2, "Beagle"),
    Cat("Luna", 5),
]

print("\n--- Everyone speak! ---")
for a in animals:
    print(a.speak())        # the correct speak() runs for each type


# ============================================================
# 5. super() CAN ALSO EXTEND (not just replace) a method
# ============================================================

class Puppy(Dog):
    """A Puppy is a young Dog that yips after the normal woof."""

    def speak(self):
        base = super().speak()          # reuse Dog's "Rex says: Woof!"
        return f"{base} (yip yip!)"

p = Puppy("Coco", 1, "Bulldog")
print("\n" + p.speak())     # Coco says: Woof! (yip yip!)


# ============================================================
# 6. isinstance() - is this object of a given type?
# ============================================================
# isinstance(obj, Class) is True if obj is that class OR a subclass.

print("\n--- isinstance checks ---")
print(isinstance(rex, Dog))       # True  - rex is a Dog
print(isinstance(rex, Animal))    # True  - a Dog IS-A Animal
print(isinstance(rex, Cat))       # False - a Dog is not a Cat
print(isinstance(p, Dog))         # True  - a Puppy IS-A Dog (and Animal)
print(isinstance(p, Animal))      # True


# ============================================================
# 7. issubclass() - is this CLASS derived from another CLASS?
# ============================================================
# issubclass works on CLASSES, not objects.

print("\n--- issubclass checks ---")
print(issubclass(Dog, Animal))    # True
print(issubclass(Cat, Animal))    # True
print(issubclass(Puppy, Dog))     # True  - Puppy -> Dog -> Animal
print(issubclass(Puppy, Animal))  # True  - inheritance chains through
print(issubclass(Dog, Cat))       # False


# ============================================================
# 8. HANDS-ON - Animal base with Dog and Cat overriding speak()
# ============================================================

class Animal2:
    """Base class with shared name and a default speak()."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a generic sound."


class Dog2(Animal2):
    def speak(self):
        return f"{self.name} barks: Woof!"


class Cat2(Animal2):
    def speak(self):
        return f"{self.name} meows: Meow!"


print("\n--- Day 32 Hands-on ---")
shelter = [Dog2("Rex"), Cat2("Luna"), Animal2("Mystery")]
for creature in shelter:
    label = type(creature).__name__        # the class name as text
    print(f"[{label}] {creature.speak()}")
