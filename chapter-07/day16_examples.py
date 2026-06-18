"""
Chapter 07 - Day 16: Default Parameters, Keyword Arguments,
                     Multiple Return Values, and Docstrings
=============================================================
Topics: Default parameter values, keyword arguments, multiple return values
        (tuple unpacking), docstrings, help() function.
"""

# ============================================================
# 1. DEFAULT PARAMETERS
# ============================================================
# A default value is used when the caller doesn't pass that argument.
# RULE: parameters WITH defaults must come AFTER those without defaults.

def greet_flexible(name, greeting="Hello", punctuation="!"):
    """
    Greets a person with a flexible message.

    Args:
        name (str): The person's name. Required.
        greeting (str): The greeting word. Defaults to "Hello".
        punctuation (str): Ending punctuation. Defaults to "!".
    """
    print(f"{greeting}, {name}{punctuation}")

# Different ways to call the same function:
greet_flexible("Alice")                          # uses all defaults
greet_flexible("Bob", "Hi")                      # overrides greeting
greet_flexible("Charlie", "Hey", ".")            # overrides both defaults
greet_flexible("Diana", punctuation="?")         # skips greeting, changes punctuation


# ============================================================
# 2. POSITIONAL vs KEYWORD ARGUMENTS
# ============================================================
# Positional: values matched by position (left to right)
# Keyword:    values matched by parameter name (can be in any order)

def describe_pet(animal, name, age):
    """Describes a pet with animal type, name, and age."""
    print(f"I have a {age}-year-old {animal} named {name}.")

# Positional - ORDER matters
describe_pet("dog", "Rex", 3)

# Keyword - ORDER doesn't matter
describe_pet(name="Luna", age=5, animal="cat")

# Mix: positional FIRST, then keyword
describe_pet("parrot", age=10, name="Polly")


# ============================================================
# 3. WHY KEYWORD ARGUMENTS ARE USEFUL
# ============================================================

def create_user(username, email, is_admin=False, is_active=True):
    """Creates a user record (simplified demo)."""
    print(f"User: {username} | Email: {email} | Admin: {is_admin} | Active: {is_active}")

# Without keyword args - easy to mix up booleans
create_user("alice", "alice@example.com", False, True)   # hard to read

# With keyword args - clear what each value means
create_user("bob", "bob@example.com", is_admin=True, is_active=False)


# ============================================================
# 4. MULTIPLE RETURN VALUES
# ============================================================
# Python functions can return multiple values separated by commas.
# Under the hood this is a TUPLE - Python's way of grouping values.

def swap(a, b):
    """Swaps two values. Returns both in reversed order."""
    return b, a     # this is shorthand for: return (b, a)

# Method 1: Capture as a single tuple
swapped_tuple = swap(10, 20)
print(f"\nswap(10, 20) returns: {swapped_tuple}")         # (20, 10)
print(f"Type: {type(swapped_tuple)}")                     # <class 'tuple'>

# Method 2: Tuple unpacking (most common and Pythonic)
x, y = swap(10, 20)
print(f"After swap: x={x}, y={y}")


# ============================================================
# 5. PRACTICAL MULTIPLE RETURN - min/max/average
# ============================================================

def analyze_numbers(numbers):
    """
    Analyzes a list of numbers.

    Returns:
        tuple: (minimum, maximum, average) as three separate values.
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average    # returns a tuple of 3

data = [4, 7, 2, 9, 1, 5, 8]

# Unpack all three at once
lo, hi, avg = analyze_numbers(data)
print(f"\nData: {data}")
print(f"Min: {lo}, Max: {hi}, Average: {avg:.2f}")

# You can also capture just the tuple and index into it
stats = analyze_numbers(data)
print(f"Only the max: {stats[1]}")


# ============================================================
# 6. DOCSTRINGS - documenting your functions
# ============================================================
# A docstring is a string literal as the FIRST statement in a function.
# It describes what the function does, its parameters, and return value.
# Python stores it in the function's __doc__ attribute.

def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    The conversion formula is: F = (C * 9/5) + 32

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9 / 5) + 32

# Accessing the docstring directly
print(f"\nDocstring via __doc__:")
print(celsius_to_fahrenheit.__doc__)

# Using the built-in help() function
print("help() output:")
help(celsius_to_fahrenheit)

# Using the function
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"37°C = {celsius_to_fahrenheit(37):.1f}°F  (body temperature)")


# ============================================================
# 7. SINGLE-LINE DOCSTRINGS (for simple functions)
# ============================================================

def square(n):
    """Returns the square of n."""
    return n ** 2

def cube(n):
    """Returns the cube of n."""
    return n ** 3

print(f"\nsquare(5) = {square(5)}")
print(f"cube(3)   = {cube(3)}")


# ============================================================
# 8. FLEXIBLE GREETING - combining defaults + keywords + docstring
# ============================================================

def send_message(recipient, message, sender="System", urgent=False, times=1):
    """
    Sends a formatted message from a sender to a recipient.

    Args:
        recipient (str): Who receives the message.
        message (str): The message body.
        sender (str): Who sends it. Defaults to "System".
        urgent (bool): If True, adds [URGENT] prefix. Defaults to False.
        times (int): How many times to repeat. Defaults to 1.

    Returns:
        str: The fully formatted message string.
    """
    prefix = "[URGENT] " if urgent else ""
    full_message = f"{prefix}To: {recipient} | From: {sender} | Msg: {message}"
    for _ in range(times):
        print(full_message)
    return full_message

print("\n--- Messaging Demo ---")
send_message("Alice", "Your report is ready.")
send_message("Bob", "System going down!", urgent=True, sender="Admin")
send_message("Charlie", "Hello!", times=3, sender="Alice")
