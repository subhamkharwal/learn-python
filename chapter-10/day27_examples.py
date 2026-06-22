"""
Chapter 10 - Day 27: raise, Custom Exceptions, and Best Practices
=================================================================
Topics: the raise statement, creating custom exception classes,
        the exception hierarchy, EAFP vs LBYL, and common
        error-handling mistakes to avoid.

NOTE: Every example here CATCHES its exception, so the script
      runs all the way to the end without crashing.
"""

# ============================================================
# 1. THE raise STATEMENT - throwing your own exception
# ============================================================
# 'raise' lets YOU signal that something is wrong, instead of
# waiting for Python to notice. You raise an exception INSTANCE.

def set_age(age):
    """Rejects ages outside a sensible range."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age is unrealistically large.")
    return age

print("1. Using raise:")
for candidate in [30, -5, 200]:
    try:
        print(f"   set_age({candidate}) -> {set_age(candidate)}")
    except ValueError as e:
        print(f"   set_age({candidate}) rejected: {e}")


# ============================================================
# 2. RE-RAISING - catch, react, then let it bubble up
# ============================================================
# A bare 'raise' (no arguments) inside except re-throws the
# SAME exception after we have done something (like logging).

def load_config(value):
    """Logs the problem, then re-raises so the caller still sees it."""
    try:
        return int(value)
    except ValueError:
        print("   (log) bad config value detected, re-raising...")
        raise            # re-raise the original ValueError

print("\n2. Re-raising:")
try:
    load_config("not-a-number")
except ValueError as e:
    print(f"   caller saw the re-raised error: {e}")


# ============================================================
# 3. CUSTOM EXCEPTION CLASSES - subclassing Exception
# ============================================================
# To make your own exception type, define a class that inherits
# from Exception. The 'pass' body is enough for a basic one.

class ValidationError(Exception):
    """Raised when some user data fails validation."""
    pass

def check_username(name):
    """Validates a username, raising ValidationError on failure."""
    if len(name) < 3:
        raise ValidationError(f"'{name}' is too short (min 3 chars).")
    return name

print("\n3. Custom ValidationError:")
for username in ["alice", "ab"]:
    try:
        print(f"   check_username('{username}') -> {check_username(username)}")
    except ValidationError as e:
        print(f"   rejected: {e}")


# ============================================================
# 4. A RICHER CUSTOM EXCEPTION - storing extra data
# ============================================================
# A custom exception can hold extra attributes. We add a custom
# __init__ that stores the offending field name.

class FieldError(Exception):
    """Raised for a specific field; remembers which field failed."""
    def __init__(self, field, message):
        self.field = field                 # extra data we attach
        # super().__init__ sets the standard message text
        super().__init__(f"[{field}] {message}")

try:
    raise FieldError("email", "missing @ symbol")
except FieldError as e:
    print("\n4. Richer custom exception:")
    print(f"   message      : {e}")
    print(f"   failed field : {e.field}")   # our custom attribute


# ============================================================
# 5. THE EXCEPTION HIERARCHY
# ============================================================
# Exceptions form a family tree. Catching a PARENT class also
# catches all of its CHILDREN. Example tree (simplified):
#
#   BaseException
#    └── Exception          <- catch THIS (or more specific), never BaseException
#         ├── ArithmeticError
#         │    └── ZeroDivisionError
#         ├── LookupError
#         │    ├── KeyError
#         │    └── IndexError
#         └── ValueError
#
# Because ZeroDivisionError is a child of ArithmeticError, an
# 'except ArithmeticError' handler catches it too.

try:
    1 / 0
except ArithmeticError as e:    # parent class catches ZeroDivisionError
    print(f"\n5. ArithmeticError caught a ZeroDivisionError: {e}")

# Likewise, LookupError is the parent of KeyError AND IndexError.
for action in ["key", "index"]:
    try:
        if action == "key":
            {"a": 1}["z"]       # KeyError
        else:
            [1, 2][99]          # IndexError
    except LookupError as e:    # one parent handles both children
        print(f"   LookupError caught a {type(e).__name__}: {e}")


# ============================================================
# 6. EAFP vs LBYL
# ============================================================
# LBYL = "Look Before You Leap": check conditions first.
# EAFP = "Easier to Ask Forgiveness than Permission": just try
#         it and handle the exception if it fails. EAFP is the
#         preferred, more Pythonic style.

data = {"name": "Bob"}

# LBYL style - check the key exists before using it
if "age" in data:
    age = data["age"]
else:
    age = "unknown"
print(f"\n6. LBYL result: age = {age}")

# EAFP style - just try, and catch the KeyError
try:
    age = data["age"]
except KeyError:
    age = "unknown"
print(f"   EAFP result: age = {age}")


# ============================================================
# 7. BEST PRACTICES - what NOT to do, and the fix
# ============================================================

# 7a. BAD: a bare 'except: pass' silently swallows EVERYTHING,
#     including typos and bugs. You never learn what broke.
print("\n7. Best practices:")
try:
    risky = int("oops")
except:          # bare except - DON'T do this
    pass         # silent failure - the worst kind of bug
print("   7a. (bad) bare except: pass hid the error - avoid this!")

# 7b. GOOD: catch the SPECIFIC exception you expect, and act on it.
try:
    risky = int("oops")
except ValueError as e:
    print(f"   7b. (good) caught specific ValueError: {e}")


# ============================================================
# 8. HANDS-ON: validate age with a custom ValidationError
# ============================================================
# Combines everything: a custom exception + raise + try/except,
# tested against several hardcoded "inputs" (no input() needed).

class AgeValidationError(ValidationError):
    """Specific validation error for ages (child of ValidationError)."""
    pass

def validate_age(raw):
    """
    Validates a raw age string.

    Raises:
        AgeValidationError: if the value is not a sensible age.
    Returns:
        int: the validated age.
    """
    try:
        age = int(raw)
    except (ValueError, TypeError):
        raise AgeValidationError(f"'{raw}' is not a whole number.")
    if age < 0:
        raise AgeValidationError(f"Age {age} cannot be negative.")
    if age > 150:
        raise AgeValidationError(f"Age {age} is unrealistically large.")
    return age

print("\n8. validate_age demo:")
for entry in ["42", "-7", "abc", "999", "0"]:
    try:
        print(f"   validate_age('{entry}') -> {validate_age(entry)}")
    except AgeValidationError as e:
        print(f"   validate_age('{entry}') rejected: {e}")


print("\nDone! The script ran to completion despite many errors.")
