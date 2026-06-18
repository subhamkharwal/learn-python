"""
Chapter 07 - Day 15: Introduction to Functions
================================================
Topics: def keyword, parameters vs arguments, return statement,
        calling functions, void functions.
"""

# ============================================================
# 1. THE SIMPLEST FUNCTION - no parameters, no return value
# ============================================================

def greet():
    """Prints a simple greeting. This is a 'void' function."""
    print("Hello! Welcome to Python Functions!")

# Calling the function - the parentheses () are REQUIRED
greet()


# ============================================================
# 2. FUNCTION WITH A PARAMETER
# ============================================================
# The variable 'name' inside the parentheses is called a PARAMETER.
# A parameter is a placeholder defined in the function signature.

def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}! Nice to meet you.")

# When we CALL the function and pass a real value, that value is the ARGUMENT.
# "Alice" is the ARGUMENT being passed to the PARAMETER 'name'.
greet_person("Alice")
greet_person("Bob")


# ============================================================
# 3. FUNCTION WITH RETURN VALUE
# ============================================================
# 'return' sends a value back to whoever called the function.
# The function call itself becomes that value.

def add(a, b):
    """Adds two numbers and returns the result."""
    result = a + b
    return result           # <-- sends the sum back to the caller

# The returned value can be stored in a variable
total = add(10, 20)
print(f"10 + 20 = {total}")

# Or used directly in an expression
print(f"5 + 7 = {add(5, 7)}")


# ============================================================
# 4. RETURN vs PRINT - the KEY difference
# ============================================================

def return_double(n):
    """Returns the double of n (can be reused)."""
    return n * 2

def print_double(n):
    """Only prints the double of n (result is lost after printing)."""
    print(n * 2)

# return_double gives us the value back so we can DO something with it
doubled = return_double(5)        # doubled = 10
tripled = return_double(doubled)  # we can chain: tripled = 20
print(f"doubled = {doubled}, then tripled = {tripled}")

# print_double only shows on screen - we CANNOT use the result
result = print_double(5)          # prints 10 to screen
print(f"result variable holds: {result}")   # None! Nothing was returned


# ============================================================
# 5. VOID FUNCTIONS RETURN None IMPLICITLY
# ============================================================
# A function with no 'return' statement automatically returns None

def say_bye():
    print("Goodbye!")

return_value = say_bye()
print(f"say_bye() returned: {return_value}")    # None


# ============================================================
# 6. is_even() - demonstrates bool return
# ============================================================

def is_even(number):
    """
    Checks if a number is even.
    Returns True if even, False otherwise.
    """
    if number % 2 == 0:
        return True
    else:
        return False

# A more Pythonic one-liner version (same logic):
# def is_even(number):
#     return number % 2 == 0

print(f"\nChecking even/odd:")
print(f"is_even(4) -> {is_even(4)}")     # True
print(f"is_even(7) -> {is_even(7)}")     # False
print(f"is_even(0) -> {is_even(0)}")     # True  (0 is even)

# Using the function in a conditional
for num in [1, 2, 3, 4, 5]:
    if is_even(num):
        print(f"  {num} is even")
    else:
        print(f"  {num} is odd")


# ============================================================
# 7. FUNCTION STOPS AT FIRST return
# ============================================================

def classify_number(n):
    """Returns a string classification for n."""
    if n < 0:
        return "negative"    # function exits here if n < 0
    if n == 0:
        return "zero"        # function exits here if n == 0
    return "positive"        # only reached if n > 0

print(f"\nclassify_number(-5) -> {classify_number(-5)}")
print(f"classify_number(0)  -> {classify_number(0)}")
print(f"classify_number(42) -> {classify_number(42)}")


# ============================================================
# 8. PUTTING IT ALL TOGETHER - a small program using functions
# ============================================================

def display_separator():
    """Prints a visual line separator."""
    print("-" * 40)

def show_number_info(n):
    """Shows various information about a number."""
    display_separator()
    print(f"Number     : {n}")
    print(f"Is even?   : {is_even(n)}")
    print(f"Doubled    : {return_double(n)}")
    print(f"Category   : {classify_number(n)}")

print("\n--- Number Info Demo ---")
show_number_info(8)
show_number_info(-3)
show_number_info(0)
display_separator()
