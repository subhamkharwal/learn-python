# Chapter 02 — Variables & Data Types

> **Course:** Python Zero to Hero
> **Days:** Day 3 & Day 4
> **Goal:** Understand how Python stores and labels data, and how to work with different kinds of values.

---

## Chapter Overview

Every program works with data. A user's name, an age, a price, a test score — all of it is data. Python needs a way to hold that data in memory so you can use it later. That is exactly what **variables** are for.

By the end of this chapter you will:
- Know what a variable is and how to create one
- Understand the four primitive (simple) data types: `int`, `float`, `bool`, `None`
- Know the basics of strings (`str`)
- Use `type()` to inspect any value
- Assign multiple variables at once
- Understand Python's dynamic typing model
- Convert values from one type to another safely

---

## Day 3 — Variables, Primitive Types, and `type()`

### What Is a Variable?

Imagine your computer's memory (RAM) as a giant warehouse full of identical storage boxes.

```
 ┌─────────────────────────────────────────────────────┐
 │                   MEMORY (RAM)                      │
 │                                                     │
 │   ┌─────────┐   ┌─────────┐   ┌─────────┐          │
 │   │         │   │         │   │         │          │
 │   │   25    │   │  3.14   │   │  True   │  ...     │
 │   │         │   │         │   │         │          │
 │   └────┬────┘   └────┬────┘   └────┬────┘          │
 │        │             │             │                │
 │      "age"        "pi"         "is_open"            │
 │     (label)      (label)        (label)             │
 └─────────────────────────────────────────────────────┘
```

A **variable** is just a **label** you stick on a box so you can find the value again later. The label is the variable name; the contents of the box is the value.

```python
age = 25        # label "age" points to the box holding 25
pi = 3.14       # label "pi" points to the box holding 3.14
is_open = True  # label "is_open" points to the box holding True
```

The `=` symbol is the **assignment operator**. It means "store the value on the right into the box and attach the label on the left". It does NOT mean "is equal to" (that is `==`).

---

### Naming Rules

Python has strict rules about variable names. Breaking them causes a `SyntaxError`.

| Rule | Good example | Bad example |
|------|-------------|-------------|
| Only letters, digits, and underscores | `user_name`, `score2` | `user-name`, `score!` |
| Cannot start with a digit | `item1` | `1item` |
| Cannot be a Python keyword | `total` | `for`, `if`, `class` |
| Case-sensitive | `Age` and `age` are different | — |

#### Convention: snake_case

Python programmers use **snake_case** for variable names — all lowercase with underscores separating words.

```
good:  first_name, total_price, is_logged_in
avoid: firstName, TotalPrice, ISLOGGEDIN
```

This is not a syntax rule — Python accepts `firstName` — but it is the agreed-upon style across the entire Python community (PEP 8 style guide).

---

### The Four Primitive Types

Python has four simple single-value built-in types you will use constantly.

#### 1. `int` — Integer (whole numbers)

Any positive or negative whole number, including zero. No decimal point.

```python
score = 100
temperature = -5
year = 2026
zero = 0
big_number = 1_000_000  # underscores are allowed as visual separators
```

> **Note:** Python ignores the underscores — they are only there to make large numbers easier to read, like commas in `1,000,000`.

Memory picture:
```
  label        box
 ┌───────┐   ┌───────┐
 │ score │──▶│  100  │
 └───────┘   └───────┘
```

#### 2. `float` — Floating-Point Number (decimals)

Any number with a decimal point. Called "float" because the decimal point can "float" to different positions.

```python
price = 19.99
gravity = 9.81
temperature = -3.5
whole_as_float = 5.0   # still a float even though it looks whole
```

Memory picture:
```
  label        box
 ┌───────┐   ┌────────┐
 │ price │──▶│  19.99 │
 └───────┘   └────────┘
```

> **Heads up:** Floats can have tiny rounding surprises:
> ```python
> print(0.1 + 0.2)  # prints 0.30000000000000004, not 0.3
> ```
> This is normal in all programming languages (not a Python bug). We will handle this properly later once you have more tools available.

#### 3. `bool` — Boolean (True or False)

There are only two possible values: `True` and `False`. Note the capital first letter — Python is case-sensitive.

```python
is_raining = True
has_passed = False
```

Booleans are used to make decisions in your program (covered in Chapter 05 — Control Flow).

**Truthiness preview:** Every value in Python has a boolean character. The following values are considered `False`:
- `0` (integer zero)
- `0.0` (float zero)
- `""` (empty string)
- `None`

Everything else is considered `True`. You do not need to memorise this now — just know it exists.

#### 4. `None` — The Absence of a Value

`None` is Python's way of saying "there is no value here". It is not zero, not an empty string, not `False` — it literally means "nothing".

```python
result = None       # we don't have a result yet
middle_name = None  # this person has no middle name
```

Use `None` as a placeholder when you want a variable to exist but you have no value to put in it yet.

---

### The `type()` Function

`type()` tells you the data type of any value or variable.

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
print(type(None))     # <class 'NoneType'>
print(type("hello"))  # <class 'str'>
```

You can also pass a variable:

```python
age = 30
print(type(age))  # <class 'int'>
```

Think of `type()` as asking Python "what kind of thing is this?".

---

### Reassigning a Variable

You can change what value a variable points to at any time:

```python
score = 0
print(score)   # 0

score = 95
print(score)   # 95
```

The old box (holding `0`) is forgotten (Python garbage-collects it). The label `score` now points to a new box holding `95`.

```
Before:                        After:
 score ──▶ [ 0 ]               score ──▶ [ 95 ]   [ 0 ] (discarded)
```

---

### Day 3 Mini Exercises

Try these in the Python REPL or in a `.py` file:

1. **Box labelling:** Create 5 variables — one of each type (`int`, `float`, `bool`, `None`) and one string. Print each variable and its type.

2. **Swap investigation:** What happens if you do:
   ```python
   x = 10
   x = x + 5
   print(x)
   ```
   What is `x` now? Why?

3. **Name checker:** Which of these variable names are valid? Test them:
   ```
   my_score   2ndPlace   total-cost   _private   for   MAX_SIZE
   ```

4. **Type surprise:** Without running the code, guess what `type(True + 1)` produces. Then run it and see if your guess was right. What type does it return?

---

## Day 4 — Strings, Multiple Assignment, Dynamic Typing, Constants, Type Conversion

### Strings — A Quick Introduction

A **string** (`str`) is a sequence of characters enclosed in quotes. You can use single quotes `'...'` or double quotes `"..."` — both work identically.

```python
name = "Alice"
city = 'London'
greeting = "Hello, World!"
empty = ""          # empty string is still a string
```

> **Full string coverage:** Chapter 04 covers strings in depth — slicing, methods, f-strings, multiline strings, and more. Today we just need the basics.

#### A few things you can do with strings right now:

```python
first = "Hello"
second = "World"

# Concatenation (joining)
message = first + ", " + second + "!"
print(message)          # Hello, World!

# Repetition
line = "-" * 20
print(line)             # --------------------

# Length
print(len("Python"))    # 6
```

---

### Multiple Assignment

#### Pattern 1 — Chained Assignment

Assign the same value to multiple variables in one line:

```python
a = b = c = 0
print(a, b, c)  # 0 0 0
```

This creates one value (`0`) and three labels all pointing to it.

```
 a ──┐
 b ──┼──▶ [ 0 ]
 c ──┘
```

#### Pattern 2 — Tuple Unpacking (Parallel Assignment)

Assign different values to multiple variables in one line:

```python
x, y = 10, 20
print(x)  # 10
print(y)  # 20

# Works with strings too
first_name, last_name = "Ada", "Lovelace"
print(first_name)  # Ada
```

The number of variables on the left must match the number of values on the right — otherwise you get a `ValueError`.

```python
a, b = 1, 2, 3   # ValueError: too many values to unpack
a, b, c = 1, 2   # ValueError: not enough values to unpack
```

#### Classic Swap Trick

Swapping two variable values without a temporary variable:

```python
x = 5
y = 10

x, y = y, x     # swap in one line!

print(x)  # 10
print(y)  # 5
```

In most other languages you need a third temp variable. Python's tuple unpacking makes this elegant.

---

### Dynamic Typing

Python is **dynamically typed**. This means:
- You do NOT declare the type of a variable upfront
- Python figures out the type from the value you assign
- The same variable can hold different types at different times

```python
data = 42           # data is an int
print(type(data))   # <class 'int'>

data = "hello"      # now data is a str
print(type(data))   # <class 'str'>

data = 3.14         # now data is a float
print(type(data))   # <class 'float'>
```

```
Step 1:  data ──▶ [ 42    ]  (int)
Step 2:  data ──▶ [ "hi"  ]  (str)
Step 3:  data ──▶ [ 3.14  ]  (float)
```

In some other languages you have to declare the type upfront and it can never change. Python figures it out for you and lets you reassign to any type.

This works fine in Python (though doing it haphazardly in real code makes programs confusing to read).

#### Why does this matter?

It makes Python faster to write. But it also means Python cannot catch certain type errors until the code actually runs. Always write clear, readable code so the type of a variable is obvious from context.

---

### Constants by Convention

Python does not have a built-in constant keyword (unlike some other languages). By convention, if a variable should never be changed, you name it in `ALL_CAPS_WITH_UNDERSCORES`:

```python
MAX_SPEED = 300
PI = 3.14159265358979
DATABASE_URL = "localhost:5432"
APP_NAME = "MyApp"
```

Python will NOT prevent you from changing these. The all-caps name is a **signal to other programmers** (and to your future self) that this value should be treated as read-only.

```python
MAX_SPEED = 300
MAX_SPEED = 400   # Python allows this, but it's bad practice
```

---

### Type Conversion (Type Casting)

Sometimes you have a value of one type and need it in another type. Python provides built-in functions for this.

#### `int()` — Convert to integer

```python
int("42")       # 42    (string → int)
int(3.9)        # 3     (float → int, truncates — does NOT round)
int(3.1)        # 3     (truncates toward zero)
int(-3.9)       # -3    (truncates toward zero, NOT -4)
int(True)       # 1
int(False)      # 0
```

**Edge cases and errors:**
```python
int("3.14")     # ValueError — can't convert decimal string directly to int
int("hello")    # ValueError — can't convert non-numeric string
int("")         # ValueError — can't convert empty string
int(None)       # TypeError  — None has no numeric meaning
```

#### `float()` — Convert to float

```python
float("3.14")   # 3.14   (string → float)
float("42")     # 42.0   (string → float)
float(10)       # 10.0   (int → float)
float(True)     # 1.0
float(False)    # 0.0
```

**Edge cases and errors:**
```python
float("hello")  # ValueError
float(None)     # TypeError
```

#### `str()` — Convert to string

`str()` almost never raises an error — it can convert almost anything to its text representation:

```python
str(42)         # "42"
str(3.14)       # "3.14"
str(True)       # "True"
str(None)       # "None"
```

#### `bool()` — Convert to boolean

```python
bool(1)         # True
bool(0)         # False
bool(-99)       # True   (any non-zero int is True)
bool(0.0)       # False
bool("")        # False  (empty string is False)
bool("hello")   # True   (non-empty string is True)
bool(None)      # False
```

#### Type conversion at a glance

```
"42"  ──int()──▶  42  ──float()──▶  42.0  ──str()──▶  "42.0"
(str)             (int)              (float)             (str)
```

#### Real-world example: reading user input

`input()` always returns a **string**, even if the user types a number. This is a very common source of beginner bugs.

```python
user_input = input("Enter your age: ")
print(type(user_input))   # <class 'str'>  ← always a string!

age = int(user_input)     # convert to int so we can do math
print(type(age))          # <class 'int'>

next_year_age = age + 1
print("Next year you will be", next_year_age)
```

What happens with a bad input?

```python
user_input = "abc"
age = int(user_input)   # ValueError: invalid literal for int() with base 10: 'abc'
```

Handling these errors properly is covered in Chapter 10 (Error Handling). For now, just be aware they exist.

---

### Common Mistakes

#### 1. Shadowing built-in names

Python has many built-in names like `list`, `str`, `int`, `input`, `print`, `type`, `len`. If you use one as a variable name, you "shadow" (hide) the original.

```python
# DON'T do this:
list = [1, 2, 3]       # now 'list' refers to your value, not the built-in
print(list([1, 2, 3])) # TypeError! 'list' is no longer the built-in function
```

```python
# DO this instead:
my_list = [1, 2, 3]
numbers = [1, 2, 3]
```

Other names to avoid: `id`, `type`, `input`, `range`, `str`, `int`, `float`, `bool`, `sum`, `min`, `max`, `map`, `filter`, `zip`.

#### 2. Forgetting that `input()` returns a string

```python
age = input("Your age: ")
if age > 18:            # TypeError: '>' not supported between 'str' and 'int'
    print("Adult")
```

Fix:
```python
age = int(input("Your age: "))
if age > 18:
    print("Adult")
```

#### 3. Mixing incompatible types

```python
name = "Alice"
greeting = "Hello " + 42    # TypeError: can only concatenate str (not "int") to str
```

Fix:
```python
greeting = "Hello " + str(42)
```

#### 4. `int()` truncates, it does not round

```python
int(9.99)   # returns 9, NOT 10
```

If you need rounding:
```python
round(9.99)   # returns 10
round(9.5)    # returns 10
round(9.44)   # returns 9
```

#### 5. Thinking `=` means "is equal to"

```python
x = 5     # ASSIGNMENT — stores 5 into x
x == 5    # COMPARISON — checks if x equals 5, returns True or False
```

---

### Day 4 Mini Exercises

1. **Input converter:** Write a small script that asks the user for two numbers and prints their sum. Remember: `input()` returns a string.

2. **Dynamic typing demo:** Create one variable and reassign it four times — each time to a different type. After each assignment, print the value and its type.

3. **Type conversion table:** Create variables of each type and convert them in a chain: `int` → `float` → `str` → `bool`. Print each step. What result do you expect for `bool('42')`? Run it and see if you're surprised.

4. **Trap the error:** Try running `int("hello")`. Read the error message carefully. What does it tell you? Think about what would happen if you tried to convert a word to an integer. We'll learn proper validation in Chapter 10.

---

## Quick Reference Card

| Concept | Example | Notes |
|---------|---------|-------|
| Variable assignment | `x = 10` | `=` is assignment, not equality |
| Integer | `age = 25` | Whole numbers only |
| Float | `price = 9.99` | Decimal numbers |
| Boolean | `flag = True` | Must capitalise: `True`, `False` |
| None | `result = None` | Represents "no value" |
| String | `name = "Alice"` | Single or double quotes |
| Check type | `type(x)` | Returns `<class '...'>` |
| Multiple assign (same) | `a = b = 0` | All point to same value |
| Multiple assign (diff) | `x, y = 1, 2` | Tuple unpacking |
| Swap | `x, y = y, x` | Pythonic one-liner |
| Constant convention | `MAX = 100` | ALL_CAPS is just a signal |
| To integer | `int("42")` | Truncates floats; errors on non-numeric |
| To float | `float("3.14")` | Errors on non-numeric |
| To string | `str(42)` | Almost never errors |
| To boolean | `bool(0)` | False; `bool(1)` → True |

---

*Next up: Chapter 03 — Operators & Expressions (Days 5–6)*
