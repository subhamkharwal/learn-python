# Chapter 12: Object-Oriented Programming (OOP)

## Chapter Overview

So far you have written programs as collections of variables and functions. That works
well for small scripts, but as programs grow, the data and the code that acts on it
start to drift apart. You end up with a pile of loose variables (`dog_name`,
`dog_breed`, `dog_age`) and a separate pile of functions that all have to be told which
variables to use.

**Object-Oriented Programming (OOP)** flips this around. It lets you bundle related
**data** and the **behavior** that works on that data into a single unit called an
**object**. Instead of passing a dog's name, breed, and age into every function, you
build one `Dog` object that *knows* its own name and *knows how* to bark.

OOP gives you:
- **Bundling** — data and the functions that use it live together in one tidy package
- **Reuse** — write common behavior once in a parent class, share it with children
- **Modeling** — describe real-world things (a dog, a bank account, a date) directly in code
- **Safety** — guard data behind validation so bad values never sneak in

This chapter spans **4 days**:

| Day | Topics |
|-----|--------|
| Day 30 | What is OOP, `class`, `__init__`, instance variables, `self` |
| Day 31 | Instance methods, `__str__` vs `__repr__`, class vs instance variables |
| Day 32 | Inheritance, `super()`, method overriding, `isinstance()`, `issubclass()` |
| Day 33 | Encapsulation (`_protected`/`__private`), `@property` + setters, `@staticmethod`/`@classmethod` |

---

## Day 30: What is OOP? Classes, Objects, and `self`

### The Big Idea: Objects Bundle Data + Behavior

Think about a real dog. A dog *has* properties (a name, a breed, an age) and a dog
*can do* things (bark, eat, sleep). In OOP we capture both of those in one place:

```
       A DOG OBJECT
  ┌───────────────────────┐
  │  DATA (what it HAS)    │
  │    name  = "Rex"       │
  │    breed = "Labrador"  │
  │    age   = 3           │
  ├───────────────────────┤
  │  BEHAVIOR (what it DOES)│
  │    bark()              │
  │    eat()               │
  └───────────────────────┘
```

### Class vs Object: Blueprint vs House

This is the single most important analogy in OOP. Get it and everything else clicks.

```
   CLASS (the blueprint)              OBJECTS (the actual houses)
  ┌──────────────────────┐
  │  House blueprint:     │  build →   🏠  House at 1 Oak St (blue door)
  │   - has a door        │  build →   🏠  House at 2 Oak St (red door)
  │   - has windows       │  build →   🏠  House at 3 Oak St (green door)
  │   - has a roof        │
  └──────────────────────┘
```

- A **class** is the blueprint. It describes what every object will look like. You
  cannot live in a blueprint — it builds nothing on its own.
- An **object** (also called an **instance**) is a real thing built from the blueprint.
  You can build many houses from one blueprint, and each has its own door color.

| Term | Meaning | Example |
|------|---------|---------|
| Class | The blueprint / template | `Dog` |
| Object / Instance | A real thing made from the class | `rex = Dog("Rex", ...)` |
| Instance variable | Data stored on one specific object | `rex.name` |
| Method | A function that belongs to the class | `rex.bark()` |

---

### The `class` Keyword

You define a class with the `class` keyword. By convention, class names use
**CapWords** (also called PascalCase): `Dog`, `BankAccount`, `ShoppingCart`.

```python
class Dog:
    """A blueprint for creating dog objects."""
    pass        # 'pass' means 'empty body for now'
```

To build an object, **call the class like a function**:

```python
my_dog = Dog()          # builds one real dog object
print(type(my_dog))     # <class '__main__.Dog'>
```

---

### `__init__` — the Constructor

A blank dog is not very useful. We want each dog to start life with a name, breed, and
age. That is the job of `__init__` (pronounced "dunder init" — *d*ouble *under*score).

`__init__` is a special method that Python calls **automatically** the moment you
create an object. Its job is to set up the object's starting data.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name      # store the name ON this object
        self.breed = breed
        self.age = age

rex = Dog("Rex", "Labrador", 3)
```

```
   rex = Dog("Rex", "Labrador", 3)
                │
                ▼
   Python builds a blank object, then calls:
   Dog.__init__(rex, "Rex", "Labrador", 3)
                 │     │        │       │
                self  name    breed    age
                 │
                 └── self IS the new object ("rex")
```

Notice you pass **three** arguments (`"Rex"`, `"Labrador"`, `3`) but `__init__` lists
**four** parameters. Python silently fills in `self` for you — you never pass it yourself.

---

### What Exactly is `self`?

`self` confuses every beginner, so let's make it crystal clear.

> **`self` means "this particular object — the one the method is being called on."**

When you write `rex.bark()`, Python secretly rewrites it as `Dog.bark(rex)`. So inside
the method, `self` *is* `rex`. If you call `luna.bark()`, then `self` *is* `luna`.

```
  rex.bark()    →   Dog.bark(rex)    →   inside bark(), self = rex
  luna.bark()   →   Dog.bark(luna)   →   inside bark(), self = luna
```

Key points about `self`:
- It is **always the first parameter** of every instance method.
- You **never pass it yourself** — Python does it for you automatically.
- `self.name = name` creates an **instance variable** that lives on that object.
- `self` is **not a keyword** — it is just a strong convention. (You *could* name it
  anything, but every Python programmer expects `self`, so always use it.)

---

### Instance Variables — One Copy per Object

Every `self.something = value` creates an **instance variable**. Each object gets its
own independent copy:

```python
rex  = Dog("Rex", "Labrador", 3)
luna = Dog("Luna", "Poodle", 5)

print(rex.name)    # Rex
print(luna.name)   # Luna  — a totally separate value
```

```
        rex                       luna
  ┌──────────────┐          ┌──────────────┐
  │ name = "Rex" │          │ name = "Luna"│
  │ breed= "Lab" │          │ breed= "Poo" │
  │ age  = 3     │          │ age  = 5     │
  └──────────────┘          └──────────────┘
   two independent objects, each with its own data
```

You read and update them with dot notation, exactly like a normal variable:

```python
print(rex.age)        # 3
rex.age = rex.age + 1 # the dog had a birthday
print(rex.age)        # 4
```

---

### Hands-on Day 30

**A `Dog` class with name, breed, and age:**

```python
class Dog:
    """A dog described by its name, breed, and age."""

    def __init__(self, name, breed, age):
        """Set up a new dog with the given details."""
        self.name = name
        self.breed = breed
        self.age = age

rex = Dog("Rex", "Labrador", 3)
print(f"{rex.name} is a {rex.age}-year-old {rex.breed}")
```

**Build a whole pack:**

```python
pack = [
    Dog("Rex", "Labrador", 3),
    Dog("Luna", "Poodle", 5),
    Dog("Coco", "Bulldog", 1),
]

for dog in pack:
    print(f"{dog.name}: {dog.breed}, age {dog.age}")
```

---

### Day 30 Mini Exercises

1. Create a `Car` class with `make`, `model`, and `year`. Build two cars and print their details.
2. Create a `Student` class with `name` and `grade`. Build three students in a list and loop over them.
3. Add a method-free `Rectangle` class with `width` and `height`. Build one and print `rect.width * rect.height` (its area).
4. Create a `BankAccount` class with `owner` and `balance`. Build an account, then update its balance with `account.balance = account.balance + 50`.

> **Common Mistake: Forgetting `self` in `__init__`**
>
> ```python
> class Dog:
>     def __init__(self, name):
>         name = name          # BUG! this assigns the parameter to itself
>                              # and stores NOTHING on the object
>
> rex = Dog("Rex")
> print(rex.name)             # AttributeError: 'Dog' object has no attribute 'name'
> ```
>
> You must write `self.name = name` to attach the value to the object. The left side
> (`self.name`) is the object's storage; the right side (`name`) is the passed-in value.

---

## Day 31: Instance Methods, `__str__` vs `__repr__`, Class Variables

### Instance Methods — Giving Objects Behavior

A **method** is just a function defined *inside* a class. Like `__init__`, its first
parameter is always `self`, which lets it reach the object's own data.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        """self.name tells us WHO is barking."""
        return f"{self.name} says: Woof!"

rex = Dog("Rex", 3)
print(rex.bark())     # Rex says: Woof!
```

Methods can take extra arguments too — they just come *after* `self`:

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learn_trick(self, trick):        # self first, then trick
        self.tricks.append(trick)
        return f"{self.name} learned to {trick}!"
```

---

### `__str__` — a Friendly Printout

By default, printing an object gives you something useless:

```python
print(rex)      # <__main__.Dog object at 0x104790f10>
```

The `__str__` method lets you control what `print()` shows. It should return a
**human-friendly** string:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"

print(Dog("Luna", 5))     # Luna (age 5)   — much nicer!
```

---

### `__str__` vs `__repr__` — and Why Both Exist

Python has **two** ways to turn an object into text, for two different audiences:

| Method | Audience | Used by | Goal |
|--------|----------|---------|------|
| `__str__` | End users | `print()`, `str()`, f-strings | Friendly, readable |
| `__repr__` | Developers | the REPL, containers (lists/dicts), debuggers | Unambiguous; ideally looks like code that recreates the object |

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"          # for users

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age})"   # for developers

d = Dog("Luna", 5)
print(d)          # Luna (age 5)             — uses __str__
print(repr(d))    # Dog(name='Luna', age=5)  — uses __repr__
print([d])        # [Dog(name='Luna', age=5)] — lists use __repr__ per element!
```

```
  print(obj)  / str(obj)  ──►  __str__   (falls back to __repr__ if no __str__)
  repr(obj)   / [obj]     ──►  __repr__  (no fallback to __str__)
```

Two practical rules:
1. **Always define `__repr__`.** It is the safety net — if you skip `__str__`, Python
   falls back to `__repr__`. The reverse is NOT true.
2. The `!r` in an f-string (`{self.name!r}`) calls `repr()` on that value, which is why
   the name shows up quoted as `'Luna'` — exactly how you'd type it in code.

---

### Class Variables vs Instance Variables

There are two places data can live:

- **Instance variable** (`self.x`) — one copy **per object**. Defined inside methods.
- **Class variable** (defined in the class body) — **one shared copy** for *all* objects.

```python
class Dog:
    species = "Canis familiaris"    # CLASS variable — shared by every dog
    count = 0                       # CLASS variable — how many dogs exist

    def __init__(self, name):
        self.name = name            # INSTANCE variable — unique per dog
        Dog.count += 1              # bump the shared counter
```

```
   CLASS Dog (shared by everyone)
   ┌──────────────────────────────────┐
   │  species = "Canis familiaris"     │
   │  count   = 2                      │
   └───────────┬───────────┬──────────┘
               │           │
        ┌──────▼─────┐ ┌───▼────────┐
        │   rex      │ │   luna     │   ◄── each object has its OWN name,
        │ name="Rex" │ │ name="Luna"│       but SHARES species + count
        └────────────┘ └────────────┘
```

```python
a = Dog("Rex")
b = Dog("Luna")
print(a.species)     # Canis familiaris  (shared)
print(b.species)     # Canis familiaris  (same shared value)
print(Dog.count)     # 2                 (both dogs bumped it)
```

Use a **class variable** when the value is the same for every object (a constant, a
shared counter, a default). Use an **instance variable** when each object needs its own.

---

### Hands-on Day 31

**Add `bark()` and a clean `__str__` to the `Dog` class:**

```python
class Dog:
    species = "Canis familiaris"            # shared by every dog

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof! Woof!"

    def __str__(self):
        return f"{self.name} the {self.breed} ({self.age} yrs)"

    def __repr__(self):
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"

rex = Dog("Rex", "Labrador", 3)
print(rex)            # Rex the Labrador (3 yrs)   — __str__
print(rex.bark())     # Rex says: Woof! Woof!
print(repr(rex))      # Dog(name='Rex', ...)       — __repr__
```

---

### Day 31 Mini Exercises

1. Add a `birthday()` method to `Dog` that increases `self.age` by 1 and prints a message.
2. Give `Dog` a `__str__` that prints `"Rex, a 3-year-old Labrador"`.
3. Add a class variable `legs = 4` to `Dog`. Verify two different dogs both report `4` legs.
4. Add a class variable `count` that increments in `__init__`. Create 3 dogs and print the total.
5. Write a `Circle` class with a `radius` instance variable and a class variable `pi = 3.14159`. Add an `area()` method.

> **Common Mistake: Mutating a Class Variable Through an Instance**
>
> ```python
> class Dog:
>     tricks = []          # WRONG — one shared list for ALL dogs!
>     def __init__(self, name):
>         self.name = name
>     def learn(self, t):
>         self.tricks.append(t)   # appends to the SHARED list
>
> a = Dog("Rex")
> b = Dog("Luna")
> a.learn("sit")
> print(b.tricks)          # ['sit']  — SURPRISE! Luna knows Rex's trick
> ```
>
> Mutable per-object data (lists, dicts) must be created **inside `__init__`** as
> `self.tricks = []`, never as a class variable.

---

## Day 32: Inheritance, `super()`, and Method Overriding

### What is Inheritance?

Dogs and cats are both **animals**. They share things: a name, an age, the ability to
eat and sleep. Without inheritance you would copy that shared code into every class.

**Inheritance** lets a **child class** automatically reuse a **parent class's** code.
The relationship is "**is-a**": a Dog *is an* Animal, a Cat *is an* Animal.

```
              Animal              ◄── PARENT (base / superclass)
            (name, age,
             eat, speak)
            ╱          ╲
          ╱              ╲
        Dog               Cat     ◄── CHILDREN (derived / subclasses)
   (adds breed,       (overrides
    overrides speak)    speak)
```

Syntax — put the parent class in parentheses after the child's name:

```python
class Animal:                       # parent
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Animal):                  # child — Cat is-a Animal
    def speak(self):                # OVERRIDE the parent's version
        return f"{self.name} says: Meow!"

whiskers = Cat("Whiskers", 4)
print(whiskers.eat())     # Whiskers is eating.   — inherited for free!
print(whiskers.speak())   # Whiskers says: Meow!  — overridden
```

`Cat` never defined `__init__` or `eat`, yet it has both — they were **inherited** from
`Animal`.

---

### `super()` — Calling the Parent's Version

Often a child needs to *add* to what the parent does, not replace it entirely. A `Dog`
wants everything `Animal.__init__` sets up (name, age) **plus** its own `breed`.
`super()` gives you a handle to the parent so you can call its method:

```python
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)     # run Animal's __init__ first
        self.breed = breed              # then add the dog-specific part
```

```
   Dog("Rex", 3, "Labrador")
        │
        ├─ super().__init__("Rex", 3)   ──► Animal sets self.name, self.age
        │
        └─ self.breed = "Labrador"      ──► Dog adds its own piece
```

Without `super().__init__(...)`, the dog would have a `breed` but **no** `name` or
`age`, because the parent's setup never ran.

---

### Method Overriding & Polymorphism

When a child defines a method with the **same name** as the parent, the child's version
**overrides** the parent's. Python automatically picks the right one based on the
object's actual type:

```python
animals = [Animal("Generic", 1), Dog("Buddy", 2, "Beagle"), Cat("Luna", 5)]

for a in animals:
    print(a.speak())     # the CORRECT speak() runs for each object's type
# Generic makes a sound.
# Buddy says: Woof!
# Luna says: Meow!
```

This is **polymorphism**: one call (`a.speak()`), many forms. You write the loop once and
each object responds in its own way.

`super()` can also *extend* a method (reuse the parent's result, then add to it):

```python
class Puppy(Dog):
    def speak(self):
        base = super().speak()          # "Coco says: Woof!"
        return f"{base} (yip yip!)"      # add the puppy flair
```

---

### `isinstance()` and `issubclass()`

Two built-ins let you ask type questions at runtime.

**`isinstance(object, Class)`** — is this *object* an instance of the class (or a
subclass)?

```python
rex = Dog("Rex", 3, "Labrador")
isinstance(rex, Dog)      # True
isinstance(rex, Animal)   # True  — a Dog IS-A Animal
isinstance(rex, Cat)      # False
```

**`issubclass(ChildClass, ParentClass)`** — is this *class* derived from another? Works
on classes, not objects:

```python
issubclass(Dog, Animal)   # True
issubclass(Cat, Animal)   # True
issubclass(Dog, Cat)      # False
```

```
   isinstance(obj, Cls)     ──► asks about an OBJECT
   issubclass(Cls, Other)   ──► asks about a CLASS
```

---

### Hands-on Day 32

**`Animal` base with `Dog` and `Cat` overriding `speak()`:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a generic sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow!"

shelter = [Dog("Rex"), Cat("Luna"), Animal("Mystery")]
for creature in shelter:
    label = type(creature).__name__       # the class name as text
    print(f"[{label}] {creature.speak()}")
```

---

### Day 32 Mini Exercises

1. Create a `Vehicle` base class with `__init__(self, brand)` and a `move()` method. Make `Car` and `Boat` subclasses that override `move()`.
2. Add a `Bird(Animal)` subclass whose `speak()` returns `"Tweet!"`. Add it to the shelter loop.
3. Make a `Shape` base with an `area()` that returns `0`. Create `Square(Shape)` and `Circle(Shape)` that override `area()` properly.
4. Use `super().__init__()` in a `Manager(Employee)` class where `Employee` has `name` and `Manager` adds `team_size`.
5. Predict the output of `isinstance(Dog("Rex"), Animal)` and `issubclass(Animal, Dog)`, then run them to check.

> **Common Mistake: Forgetting `super().__init__()`**
>
> ```python
> class Animal:
>     def __init__(self, name):
>         self.name = name
>
> class Dog(Animal):
>     def __init__(self, name, breed):
>         self.breed = breed       # forgot super().__init__(name)!
>
> rex = Dog("Rex", "Lab")
> print(rex.name)                  # AttributeError: no attribute 'name'
> ```
>
> When a child defines its own `__init__`, the parent's `__init__` does **not** run
> automatically. You must call `super().__init__(...)` yourself to set up the inherited data.

---

## Day 33: Encapsulation, Properties, and Static/Class Methods

### Encapsulation — Hiding the Internals

**Encapsulation** means bundling data with the methods that guard it, and signalling
which parts are *internal* so users of your class don't poke at them by accident.

Unlike some languages, Python has **no truly private** data. Instead it uses **naming
conventions** that everyone agrees to respect:

| Name | Meaning | Signal |
|------|---------|--------|
| `name` | **Public** | "Use me freely." |
| `_name` | **Protected** | "Internal — please don't touch from outside." (convention only) |
| `__name` | **Private** | "Really internal." Python *name-mangles* it to make accidental access hard. |

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected (convention: leave it alone)
```

---

### `__private` and Name Mangling

A name with **two leading underscores** gets rewritten by Python from `__secret` to
`_ClassName__secret`. This prevents accidental clashes (especially between parent and
child classes) and makes the attribute hard to reach from outside.

```python
class Vault:
    def __init__(self, code):
        self.__secret_code = code       # becomes _Vault__secret_code

    def reveal(self):
        return f"The code is {self.__secret_code}"   # works inside the class

v = Vault("1234")
print(v.reveal())            # The code is 1234
print(v.__secret_code)       # AttributeError! the name was mangled
print(v._Vault__secret_code) # 1234  — still reachable IF you know the trick
```

```
   __secret_code   ──(name mangling)──►   _Vault__secret_code
```

It is **not real security** — it is a strong "keep out" sign. The mangled name still
exists if someone really wants it.

---

### `@property` — Methods That Act Like Attributes

A **property** lets you call a method *without parentheses*, as if it were a plain
attribute. This is perfect for **computed values**:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(10)
print(c.area)        # 314.159   — note: c.area, NOT c.area()
```

---

### `@property` + `@x.setter` — Validated Access

The real power of properties is **validation on assignment**. You expose a clean public
name (`age`), but every read goes through a **getter** and every write goes through a
**setter** that can reject bad values — all while the user just writes `p.age = 31`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age          # this calls the SETTER below (validates!)

    @property                   # the GETTER — defines how to READ p.age
    def age(self):
        return self._age

    @age.setter                 # the SETTER — defines how to WRITE p.age
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value       # store in the internal _age

p = Person("Alice", 30)
print(p.age)        # 30        — runs the getter
p.age = 31          # runs the setter (valid)
p.age = -5          # ValueError: age cannot be negative
```

```
   p.age          ──►  getter runs  ──►  returns self._age
   p.age = 31     ──►  setter runs  ──►  validates, then stores self._age
```

How it fits together:
- The `@property` method and the `@age.setter` method **must have the same name** (`age`).
- The public name is `age`; the actual storage is the private-ish `_age`.
- Because `__init__` does `self.age = age`, **even the constructor's value is validated** —
  bad data can never get in, not even at creation time.

---

### `@staticmethod` — a Helper Grouped Under a Class

A **static method** takes **no `self`** and **no `cls`**. It does not touch any object
or class data — it's just a related utility function that *logically belongs* with the
class. Call it on the class itself.

```python
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathTools.add(3, 4))      # 7
print(MathTools.is_even(10))    # True
```

---

### `@classmethod` — a Method That Receives the Class

A **class method** takes **`cls`** (the class itself) instead of `self`. The classic use
is an **alternative constructor** — a different way to build an object:

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, text):           # cls is the Date class
        year, month, day = (int(p) for p in text.split("-"))
        return cls(year, month, day)       # build and return a Date

d1 = Date(2026, 6, 19)                 # normal constructor
d2 = Date.from_string("2026-12-25")    # alternative constructor
```

Using `cls(...)` instead of `Date(...)` means it still works correctly if someone
subclasses `Date` — a subclass's `from_string` will build the subclass.

---

### When to Use Each: `self` vs `cls` vs Neither

```
   instance method  def method(self, ...)   needs the OBJECT's data
   @classmethod     def method(cls, ...)    needs the CLASS (alt constructors, counters)
   @staticmethod    def method(...)         needs NEITHER (a related helper)
```

| Decorator | First arg | Can read/write instance data? | Can read/write class data? | Typical use |
|-----------|-----------|-------------------------------|----------------------------|-------------|
| (none) | `self` | Yes | Yes (via `ClassName`) | Normal behavior on an object |
| `@classmethod` | `cls` | No | Yes | Alternative constructors, factory methods |
| `@staticmethod` | — | No | No | Utility functions related to the class |

---

### Hands-on Day 33

**Add age validation to `Dog` with a `@property` setter:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age          # routes through the setter → validated

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be a whole number")
        if value < 0:
            raise ValueError("age cannot be negative")
        if value > 30:
            raise ValueError("that is too old for a dog!")
        self._age = value

    def __str__(self):
        return f"{self.name} (age {self.age})"

rex = Dog("Rex", 3)
rex.age = 4              # valid
# rex.age = -1          # ValueError: age cannot be negative
# rex.age = "five"      # TypeError: age must be a whole number
```

---

### Day 33 Mini Exercises

1. Give `BankAccount` a `_balance` and a `deposit(amount)` method that rejects negative amounts.
2. Add a `@property` `balance` (read-only — define only the getter) to `BankAccount`.
3. Add a `@property` setter for `temperature` that refuses values below `-273` (absolute zero).
4. Write a `Temperature` class with a `@classmethod` `from_fahrenheit(cls, f)` alternative constructor that stores Celsius internally.
5. Add a `@staticmethod` `is_valid_name(name)` to `Person` that returns `True` only if the name is non-empty and all letters.

> **Common Mistake: Infinite Recursion in a Property Setter**
>
> ```python
> class Person:
>     @property
>     def age(self):
>         return self.age          # BUG! reading self.age calls THIS getter again
>     @age.setter
>     def age(self, value):
>         self.age = value         # BUG! assigning self.age calls THIS setter again
> ```
>
> A property getter/setter must store data in a **differently named** internal
> attribute (by convention `self._age`), never in `self.age` itself — otherwise it
> calls itself forever and raises `RecursionError`.

---

## Quick Reference Card

```
DEFINING A CLASS
  class Dog:                          # CapWords name
      species = "Canis familiaris"    # CLASS variable (shared by all)

      def __init__(self, name, age):  # constructor, runs on creation
          self.name = name            # INSTANCE variable (per object)
          self.age = age

      def bark(self):                 # instance method (self = the object)
          return f"{self.name}: Woof!"

CREATING & USING OBJECTS
  rex = Dog("Rex", 3)     # build an object (don't pass self)
  rex.bark()              # call a method
  rex.name                # read an instance variable
  rex.age = 4             # update an instance variable

STRING METHODS
  __str__   →  print(obj), str(obj)   (friendly, for users)
  __repr__  →  repr(obj), [obj], REPL (unambiguous, for developers)
             (always define __repr__; print falls back to it)

INHERITANCE
  class Dog(Animal):              # Dog IS-A Animal
      def __init__(self, ...):
          super().__init__(...)   # run parent's constructor
      def speak(self):            # override the parent method
          ...
  isinstance(obj, Class)          # is OBJECT an instance of Class?
  issubclass(Child, Parent)       # is CLASS derived from Parent?

ENCAPSULATION (naming conventions)
  name      → public
  _name     → protected ("internal, please don't touch")
  __name    → private   (mangled to _ClassName__name)

PROPERTIES (validated attribute access)
  @property               # getter:  read  obj.x
  def x(self): return self._x
  @x.setter               # setter:  write obj.x = val (validate here!)
  def x(self, val): self._x = val
  # store in self._x, never self.x → avoids infinite recursion

METHOD TYPES
  def m(self, ...)    instance method  → uses object data
  @classmethod
  def m(cls, ...)     class method     → uses class (alt constructors)
  @staticmethod
  def m(...)          static method    → uses neither (helper)
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 30–33 |
| `day30_examples.py` | Runnable code: classes, `__init__`, instance variables, `self`, the `Dog` class |
| `day31_examples.py` | Runnable code: instance methods, `bark()`, `__str__` vs `__repr__`, class vs instance variables |
| `day32_examples.py` | Runnable code: inheritance, `super()`, overriding `speak()`, `isinstance()`/`issubclass()` |
| `day33_examples.py` | Runnable code: `_protected`/`__private`, `@property` + setter validation, `@staticmethod`/`@classmethod` |
