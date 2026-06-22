"""
Chapter 10 - Day 26: Exceptions and try/except/else/finally
===========================================================
Topics: what exceptions are, common built-in exceptions,
        try / except / else / finally, catching multiple
        exceptions, catching the exception object with 'as e'.

NOTE: Every example here CATCHES its exception, so the script
      runs all the way to the end without crashing.
"""

# ============================================================
# 1. A CRASH WITHOUT HANDLING (shown, then handled)
# ============================================================
# Dividing by zero raises ZeroDivisionError. If we do nothing,
# Python prints a traceback and STOPS the whole program.
# We wrap it in try/except so the script keeps running.

try:
    result = 10 / 0          # <-- this line raises ZeroDivisionError
    print(result)            # <-- never reached
except ZeroDivisionError:
    print("1. Caught it! You cannot divide by zero.")


# ============================================================
# 2. THE try / except BLOCK - basic shape
# ============================================================
# try:    put the risky code here
# except: this runs ONLY if the try block raised an exception

try:
    number = int("hello")    # int() of "hello" raises ValueError
except ValueError:
    print("2. 'hello' is not a valid whole number.")


# ============================================================
# 3. COMMON BUILT-IN EXCEPTIONS - one demo each
# ============================================================
# Each example triggers a different built-in exception and
# catches it so we can see its name and message.

# ValueError - right type, wrong value
try:
    age = int("twenty")
except ValueError as e:
    print(f"3a. ValueError      -> {e}")

# TypeError - wrong TYPE used in an operation
try:
    mixed = "abc" + 5        # cannot add a string and an int
except TypeError as e:
    print(f"3b. TypeError       -> {e}")

# KeyError - asking a dict for a key that does not exist
try:
    person = {"name": "Alice"}
    print(person["age"])     # there is no 'age' key
except KeyError as e:
    print(f"3c. KeyError        -> {e} (this key was not found)")

# IndexError - using a list index that is out of range
try:
    colors = ["red", "green", "blue"]
    print(colors[10])        # only indexes 0,1,2 exist
except IndexError as e:
    print(f"3d. IndexError      -> {e}")

# ZeroDivisionError - dividing by zero
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"3e. ZeroDivisionError -> {e}")

# FileNotFoundError - opening a file that is not there
try:
    with open("this_file_does_not_exist.txt") as f:
        f.read()
except FileNotFoundError as e:
    print(f"3f. FileNotFoundError -> {e}")


# ============================================================
# 4. CATCHING THE EXCEPTION OBJECT WITH 'as e'
# ============================================================
# 'as e' captures the exception object so we can inspect it.
# type(e).__name__ gives the exception's class name as a string.

try:
    value = int("not a number")
except ValueError as e:
    print(f"\n4. Exception type: {type(e).__name__}")
    print(f"   Message       : {e}")


# ============================================================
# 5. CATCHING MULTIPLE EXCEPTIONS
# ============================================================

# 5a. Different handler for each exception type
def safe_lookup(data, key):
    """Looks up key in data; handles two different problems."""
    try:
        return data[key]
    except KeyError:
        return "(no such key)"
    except TypeError:
        return "(data is not look-up-able)"

print("\n5a. Multiple except blocks:")
print(f"   safe_lookup({{'a': 1}}, 'a') -> {safe_lookup({'a': 1}, 'a')}")
print(f"   safe_lookup({{'a': 1}}, 'z') -> {safe_lookup({'a': 1}, 'z')}")
print(f"   safe_lookup(None, 'a')      -> {safe_lookup(None, 'a')}")

# 5b. One handler for several types - group them in a tuple
try:
    risky = int("oops")
except (ValueError, TypeError) as e:
    print(f"5b. Caught ValueError OR TypeError -> {e}")


# ============================================================
# 6. try / except / else / finally - the full flow
# ============================================================
# else    : runs only if NO exception happened in try
# finally : ALWAYS runs (exception or not) - great for cleanup

def divide(a, b):
    """Demonstrates all four blocks working together."""
    print(f"\n6. divide({a}, {b}):")
    try:
        result = a / b
    except ZeroDivisionError:
        print("   except : division by zero!")
    else:
        # only runs when try succeeded
        print(f"   else   : success, result = {result}")
    finally:
        # always runs - whether or not there was an error
        print("   finally: cleaning up (this always runs)")

divide(10, 2)    # try succeeds -> else + finally run
divide(10, 0)    # try fails    -> except + finally run


# ============================================================
# 7. HANDS-ON: a SAFE DIVISION function
# ============================================================
# Returns the result, or a friendly message if anything goes wrong.

def safe_divide(a, b):
    """Divides a by b, returning None and a message on any error."""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"   Cannot divide {a} by zero.")
        return None
    except TypeError:
        print("   Both inputs must be numbers.")
        return None

print("\n7. safe_divide demo:")
print(f"   safe_divide(20, 4)   -> {safe_divide(20, 4)}")
print(f"   safe_divide(20, 0)   -> {safe_divide(20, 0)}")
print(f"   safe_divide(20, 'x') -> {safe_divide(20, 'x')}")


# ============================================================
# 8. HANDS-ON: handle invalid user input (without input())
# ============================================================
# We simulate "user input" with a list of strings, as if they
# had been typed in. parse_age tries to turn each into a number
# and reports which ones are valid.

def parse_age(raw):
    """Turns a raw string into a valid age, or explains the problem."""
    try:
        age = int(raw)
    except ValueError:
        return f"'{raw}' is not a whole number."
    if age < 0:
        return f"'{raw}' is negative - ages cannot be below 0."
    return f"'{raw}' is a valid age: {age}"

print("\n8. Handling 'user input':")
for entry in ["25", "hello", "-3", "0", "100.5"]:
    print(f"   {parse_age(entry)}")


print("\nDone! The script ran to completion despite many errors.")
