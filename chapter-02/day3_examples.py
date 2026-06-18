"""
Chapter 02 — Variables & Data Types
Day 3: Variables, int, float, bool, None, and type()

Run this file with:  python day3_examples.py
"""

# ============================================================
# SECTION 1: What Is a Variable?
# ============================================================
# A variable is a label attached to a value stored in memory.
# The '=' operator means ASSIGNMENT, not "is equal to".

name = "Alice"          # label 'name' points to the string "Alice"
age = 30                # label 'age' points to the integer 30
height = 1.75           # label 'height' points to the float 1.75

print("--- Section 1: Basic Variables ---")
print(name)
print(age)
print(height)
print()  # blank line for readability


# ============================================================
# SECTION 2: The int Type (whole numbers)
# ============================================================
# Integers can be positive, negative, or zero.
# Python integers have no size limit — they can be as big as needed.

print("--- Section 2: int ---")

score = 100
lives = 3
temperature = -10
year = 2026
zero = 0
big_number = 1_000_000   # underscores are just visual separators (ignored by Python)

print("score:", score)
print("lives:", lives)
print("temperature:", temperature)
print("year:", year)
print("zero:", zero)
print("big_number:", big_number)
print("type of score:", type(score))
print()


# ============================================================
# SECTION 3: The float Type (decimal numbers)
# ============================================================
# Any number with a decimal point is a float.
# Note: 5.0 is a float, even though it has no fractional part.

print("--- Section 3: float ---")

price = 19.99
gravity = 9.81
pi_approx = 3.14159
negative_float = -2.5
whole_as_float = 5.0     # still a float!

print("price:", price)
print("gravity:", gravity)
print("pi_approx:", pi_approx)
print("negative_float:", negative_float)
print("whole_as_float:", whole_as_float)
print("type of price:", type(price))
print()

# Floating-point quirk — a famous behaviour in all programming languages
print("Float precision quirk:")
print("0.1 + 0.2 =", 0.1 + 0.2)   # outputs 0.30000000000000004
print("(This is normal! Not a Python bug.)")
print()


# ============================================================
# SECTION 4: The bool Type (True or False)
# ============================================================
# Only two possible values: True and False (capital first letter required).
# Booleans are used for decision-making (see Chapter 05).

print("--- Section 4: bool ---")

is_raining = True
has_passed = False
light_on = True
door_locked = False

print("is_raining:", is_raining)
print("has_passed:", has_passed)
print("type of is_raining:", type(is_raining))
print()

# Interesting: In Python, bool is a subtype of int.
# True behaves like 1, and False behaves like 0.
print("True + 1 =", True + 1)    # 2
print("False + 5 =", False + 5)  # 5
print()


# ============================================================
# SECTION 5: None — The Absence of a Value
# ============================================================
# None means "no value" or "nothing here yet".
# It is NOT zero, NOT False, NOT an empty string.

print("--- Section 5: None ---")

result = None          # we don't have a result yet
middle_name = None     # this person has no middle name
winner = None          # no winner declared yet

print("result:", result)
print("middle_name:", middle_name)
print("type of result:", type(result))   # <class 'NoneType'>
print()


# ============================================================
# SECTION 6: The type() Function
# ============================================================
# type(x) returns the data type of x.
# Use it anytime you're unsure what kind of value something is.

print("--- Section 6: type() ---")

print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type(True))         # <class 'bool'>
print(type(False))        # <class 'bool'>
print(type(None))         # <class 'NoneType'>
print(type("hello"))      # <class 'str'>
print()

# You can pass a variable to type() as well
mystery_value = 999
print("mystery_value is:", mystery_value)
print("Its type is:", type(mystery_value))
print()


# ============================================================
# SECTION 7: Declaring 10 Variables of Different Types
# ============================================================
# Hands-on exercise: 10 variables, all different values and types.

print("--- Section 7: 10 Variables Hands-On ---")

var_01 = 42                  # int
var_02 = -7                  # int (negative)
var_03 = 3.14                # float
var_04 = -0.001              # float (tiny negative)
var_05 = True                # bool (True)
var_06 = False               # bool (False)
var_07 = None                # NoneType
var_08 = "Python"            # str
var_09 = 1_000_000           # int with underscore separator
var_10 = 0.0                 # float zero

# Print each variable alongside its type using a formatted column
variables = [
    ("var_01", var_01),
    ("var_02", var_02),
    ("var_03", var_03),
    ("var_04", var_04),
    ("var_05", var_05),
    ("var_06", var_06),
    ("var_07", var_07),
    ("var_08", var_08),
    ("var_09", var_09),
    ("var_10", var_10),
]

print(f"{'Name':<10} {'Value':<15} {'Type'}")
print("-" * 45)
for var_name, value in variables:
    print(f"{var_name:<10} {str(value):<15} {type(value)}")
print()


# ============================================================
# SECTION 8: Reassigning a Variable
# ============================================================
# A variable label can be moved to a new value at any time.

print("--- Section 8: Reassigning ---")

counter = 0
print("counter starts at:", counter)

counter = 10
print("counter is now:", counter)

counter = counter + 1    # read current value, add 1, store the result back
print("counter after +1:", counter)

# Shorthand (augmented assignment)
counter += 1             # same as: counter = counter + 1
print("counter after +=1:", counter)
print()


# ============================================================
# SECTION 9: Naming Rules Demo
# ============================================================

print("--- Section 9: Naming Rules ---")

# Valid names (snake_case convention)
user_name = "Bob"
total_score = 500
is_active = True
_private_var = "internal use"    # leading underscore is valid
MAX_RETRIES = 3                  # all-caps is valid (constant convention)

print("user_name:", user_name)
print("total_score:", total_score)
print("is_active:", is_active)
print("_private_var:", _private_var)
print("MAX_RETRIES:", MAX_RETRIES)
print()

# The lines below are commented out because they would cause SyntaxErrors:
# 2nd_place = "Silver"       # SyntaxError: starts with a digit
# user-name = "Bob"          # SyntaxError: hyphen not allowed
# for = 5                    # SyntaxError: 'for' is a keyword


# ============================================================
# END OF DAY 3
# ============================================================
print("=" * 45)
print("Day 3 complete! Review the output above.")
print("=" * 45)
