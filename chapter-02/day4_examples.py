"""
Chapter 02 — Variables & Data Types
Day 4: Strings (basics), Multiple Assignment, Dynamic Typing,
       Constants by Convention, and Type Conversion

Run this file with:  python day4_examples.py
"""

# ============================================================
# SECTION 1: Strings — Quick Introduction
# ============================================================
# A string is a sequence of characters inside quotes.
# You may use single quotes or double quotes — both work the same.
# Full string coverage is in Chapter 04.

print("--- Section 1: Strings Basics ---")

name = "Alice"
city = 'London'
greeting = "Hello, World!"
empty_string = ""       # valid — a string with zero characters

print("name:", name)
print("city:", city)
print("greeting:", greeting)
print("empty_string:", repr(empty_string))  # repr() shows quotes so we can see it's ""
print("type of name:", type(name))
print()

# String concatenation — joining strings with +
first = "Hello"
second = "World"
message = first + ", " + second + "!"
print("concatenation:", message)

# String repetition — repeat a string N times with *
divider = "-" * 30
print(divider)

# Built-in len() — count the number of characters
print("len('Python'):", len("Python"))    # 6
print("len(''):", len(""))               # 0
print()


# ============================================================
# SECTION 2: Multiple Assignment — Pattern 1 (Chained)
# ============================================================
# Assign the same value to several variables in a single line.

print("--- Section 2a: Chained Assignment ---")

# All three variables receive the same value 0
a = b = c = 0
print("a:", a, " b:", b, " c:", c)
print("type of a:", type(a))
print()

# Real-world use case: initialise several counters to zero
wins = losses = draws = 0
print("wins:", wins, "losses:", losses, "draws:", draws)
print()


# ============================================================
# SECTION 3: Multiple Assignment — Pattern 2 (Tuple Unpacking)
# ============================================================
# Assign different values to several variables in one line.
# The number of variables MUST match the number of values.

print("--- Section 2b: Tuple Unpacking ---")

x, y = 10, 20
print("x:", x, "  y:", y)

first_name, last_name = "Ada", "Lovelace"
print("first_name:", first_name)
print("last_name:", last_name)

# Unpacking works with any values of any types
number, text, flag = 42, "hello", True
print("number:", number, " text:", text, " flag:", flag)
print()

# Classic swap — exchange two variables without a temp variable
alpha = "cat"
beta = "dog"
print("Before swap:  alpha =", alpha, "  beta =", beta)

alpha, beta = beta, alpha   # Python evaluates the right side first, then assigns

print("After swap:   alpha =", alpha, "  beta =", beta)
print()

# What happens if counts don't match?
# Uncomment these lines one at a time to see the errors:
# p, q = 1, 2, 3       # ValueError: too many values to unpack (expected 2)
# p, q, r = 1, 2       # ValueError: not enough values to unpack (expected 3, got 2)


# ============================================================
# SECTION 4: Dynamic Typing
# ============================================================
# Python variables are NOT tied to a fixed type.
# The type is determined by the value currently stored.
# The same variable can hold different types at different times.

print("--- Section 3: Dynamic Typing ---")

data = 42
print("data =", data, "  type:", type(data))    # <class 'int'>

data = "hello"
print("data =", data, "  type:", type(data))    # <class 'str'>

data = 3.14
print("data =", data, "  type:", type(data))    # <class 'float'>

data = True
print("data =", data, "  type:", type(data))    # <class 'bool'>

data = None
print("data =", data, "  type:", type(data))    # <class 'NoneType'>
print()

# Dynamic typing lets you write code quickly, but be careful:
# Changing the type of a variable mid-program can confuse readers.
# Best practice: keep a variable's type consistent throughout its life.


# ============================================================
# SECTION 5: Constants by Convention
# ============================================================
# Python has no built-in constant keyword.
# Use ALL_CAPS to signal "this should not be changed".

print("--- Section 4: Constants by Convention ---")

MAX_SPEED = 300
PI = 3.14159265358979
DATABASE_HOST = "localhost"
APP_VERSION = "1.0.0"
RETRY_LIMIT = 3

print("MAX_SPEED:", MAX_SPEED)
print("PI:", PI)
print("DATABASE_HOST:", DATABASE_HOST)
print("APP_VERSION:", APP_VERSION)
print("RETRY_LIMIT:", RETRY_LIMIT)
print()

# Python will let you re-assign a constant (it's just a convention, not enforced):
# MAX_SPEED = 500  # allowed but BAD practice — violates the ALL_CAPS convention


# ============================================================
# SECTION 6: Type Conversion — int()
# ============================================================
# int() converts a value to an integer.
# It TRUNCATES floats (does not round — it cuts off the decimal part).

print("--- Section 5: Type Conversion — int() ---")

print("int('42')    =", int("42"))       # 42   string of digits → int
print("int(3.9)     =", int(3.9))        # 3    truncates (NOT rounds)
print("int(3.1)     =", int(3.1))        # 3    truncates
print("int(-3.9)    =", int(-3.9))       # -3   truncates toward zero
print("int(True)    =", int(True))       # 1    bool True → 1
print("int(False)   =", int(False))      # 0    bool False → 0
print()

# Contrast truncation vs rounding
print("Truncation vs Rounding:")
print("int(9.99)    =", int(9.99))       # 9   ← truncated
print("round(9.99)  =", round(9.99))     # 10  ← rounded
print()

# Errors — these are shown as try/except so the script keeps running
print("int() error cases:")

try:
    int("3.14")   # can't convert decimal string directly — do float first
except ValueError as e:
    print("int('3.14')  → ValueError:", e)

try:
    int("hello")  # non-numeric string
except ValueError as e:
    print("int('hello') → ValueError:", e)

try:
    int(None)     # None has no numeric meaning
except TypeError as e:
    print("int(None)    → TypeError:", e)

print()


# ============================================================
# SECTION 7: Type Conversion — float()
# ============================================================

print("--- Section 6: Type Conversion — float() ---")

print("float('3.14') =", float("3.14"))   # 3.14
print("float('42')   =", float("42"))     # 42.0
print("float(10)     =", float(10))       # 10.0
print("float(True)   =", float(True))     # 1.0
print("float(False)  =", float(False))    # 0.0
print()

print("float() error cases:")

try:
    float("hello")
except ValueError as e:
    print("float('hello') → ValueError:", e)

try:
    float(None)
except TypeError as e:
    print("float(None)   → TypeError:", e)

print()


# ============================================================
# SECTION 8: Type Conversion — str()
# ============================================================
# str() almost never raises an error — it converts nearly anything.

print("--- Section 7: Type Conversion — str() ---")

print("str(42)       =", str(42))         # "42"
print("str(3.14)     =", str(3.14))       # "3.14"
print("str(True)     =", str(True))       # "True"
print("str(False)    =", str(False))      # "False"
print("str(None)     =", str(None))       # "None"

# str() is what lets you concatenate numbers into text messages:
player = "Alice"
points = 250
result = player + " scored " + str(points) + " points"
print("message:", result)
print()


# ============================================================
# SECTION 9: Type Conversion — bool()
# ============================================================
# Every Python value has a boolean interpretation.
# Falsy values: 0, 0.0, "", None, [], {}, ()
# Everything else is truthy.

print("--- Section 8: Type Conversion — bool() ---")

print("Falsy values:")
print("bool(0)    =", bool(0))        # False
print("bool(0.0)  =", bool(0.0))      # False
print("bool('')   =", bool(""))       # False  (empty string)
print("bool(None) =", bool(None))     # False
print()

print("Truthy values:")
print("bool(1)    =", bool(1))        # True
print("bool(-99)  =", bool(-99))      # True  (any non-zero number)
print("bool(0.01) =", bool(0.01))     # True  (any non-zero float)
print("bool('hi') =", bool("hi"))     # True  (non-empty string)
print("bool(' ')  =", bool(" "))      # True  (space is a character!)
print()


# ============================================================
# SECTION 10: Real-World Example — input() Always Returns str
# ============================================================
# This is the #1 beginner mistake.
# input() reads from the keyboard and ALWAYS returns a string.
# You must convert it before doing arithmetic.

print("--- Section 9: input() is always str ---")

# Simulating what a user would type (we hard-code the values here
# so this script can run without waiting for keyboard input)

raw_age = "25"                # imagine the user typed "25"
print("raw_age:", raw_age, "  type:", type(raw_age))   # <class 'str'>

numeric_age = int(raw_age)    # convert to int so we can do math
print("numeric_age:", numeric_age, "  type:", type(numeric_age))  # <class 'int'>

next_year_age = numeric_age + 1
print("Next year you will be:", next_year_age)
print()

# What if the user types something that can't be converted?
print("Type conversion failure demo:")
bad_input = "twenty-five"
try:
    converted = int(bad_input)
except ValueError as e:
    print("Could not convert input:", e)
print()

# Safe conversion using str.isdigit()
def safe_to_int(text):
    """Convert text to int if it looks like a whole number, else return None."""
    cleaned = text.strip()          # remove leading/trailing whitespace
    if cleaned.isdigit():           # isdigit() returns True if all chars are digits
        return int(cleaned)
    return None

print("safe_to_int('42')    =", safe_to_int("42"))
print("safe_to_int('3.14')  =", safe_to_int("3.14"))   # None — isdigit() is False
print("safe_to_int('abc')   =", safe_to_int("abc"))    # None
print("safe_to_int(' 99 ')  =", safe_to_int(" 99 "))   # 99 — strip() handles spaces
print()


# ============================================================
# SECTION 11: Dynamic Typing Deep-Dive — Experiment
# ============================================================

print("--- Section 10: Dynamic Typing Experiment ---")

# Watch how type() changes as we reassign
item = 100
print(f"item = {item!r:>12}   type = {type(item).__name__}")

item = 100.0
print(f"item = {item!r:>12}   type = {type(item).__name__}")

item = "100"
print(f"item = {item!r:>12}   type = {type(item).__name__}")

item = True
print(f"item = {item!r:>12}   type = {type(item).__name__}")

item = None
print(f"item = {item!r:>12}   type = {type(item).__name__}")
print()


# ============================================================
# SECTION 12: Type Conversion Chain Demo
# ============================================================
# int → float → str → bool (following each step)

print("--- Section 11: Conversion Chain ---")

start = 7                               # int
print("start (int):         ", start)

as_float = float(start)                 # int → float
print("as_float (float):    ", as_float)

as_string = str(as_float)               # float → str
print("as_string (str):     ", as_string)

as_bool = bool(as_string)               # str → bool (non-empty → True)
print("as_bool (bool):      ", as_bool)
print()

# Now try with zero
start_zero = 0
print("start_zero (int):        ", start_zero)
as_float_zero = float(start_zero)
print("as_float_zero (float):   ", as_float_zero)
as_string_zero = str(as_float_zero)
print("as_string_zero (str):    ", as_string_zero)
# "0.0" is a non-empty string → bool is True! Might be surprising.
as_bool_zero = bool(as_string_zero)
print("as_bool_zero (bool):     ", as_bool_zero, " ← non-empty string is True!")
print()


# ============================================================
# SECTION 13: Common Mistake — Shadowing Built-ins
# ============================================================

print("--- Section 12: Shadowing Built-in Names (What NOT to Do) ---")

# GOOD: descriptive names that don't clash with built-ins
my_list = [1, 2, 3]
user_input_text = "hello"
integer_count = 5

print("my_list:", my_list)
print("user_input_text:", user_input_text)
print("integer_count:", integer_count)
print()

# BAD examples — these are commented out to avoid breaking the script:
# list = [1, 2, 3]     # shadows the built-in 'list' constructor
# str = "hello"        # shadows the built-in 'str' type
# input = "test"       # shadows the built-in 'input' function
# type = "unknown"     # shadows the built-in 'type' function

print("Avoid naming variables: list, str, int, float, bool,")
print("input, print, type, len, range, id, sum, min, max, etc.")
print()


# ============================================================
# END OF DAY 4
# ============================================================
print("=" * 50)
print("Day 4 complete! Review the output above.")
print("Next up: Chapter 03 — Operators & Expressions")
print("=" * 50)
