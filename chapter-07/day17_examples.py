"""
Chapter 07 - Day 17: *args, **kwargs, Variable Scope, and Recursion
=====================================================================
Topics: *args (variable positional arguments), **kwargs (variable keyword
        arguments), parameter order rule, local vs global scope,
        global keyword, recursion with base case.
"""

# ============================================================
# 1. *args - ACCEPT ANY NUMBER OF POSITIONAL ARGUMENTS
# ============================================================
# The * collects all extra positional arguments into a TUPLE.
# 'args' is the conventional name - you could use *anything,
# but *args is universally understood by Python developers.

def sum_all(*args):
    """
    Sums any number of numeric arguments.

    *args collects all positional arguments into a tuple.

    Args:
        *args: Variable number of numbers to sum.

    Returns:
        int/float: The total sum.
    """
    print(f"  args received: {args}  (type: {type(args).__name__})")
    total = 0
    for number in args:
        total += number
    return total

print("--- *args demo ---")
print(f"sum_all(1, 2, 3)       = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20)        = {sum_all(10, 20)}")
print(f"sum_all(1,2,3,4,5,6,7) = {sum_all(1, 2, 3, 4, 5, 6, 7)}")
print(f"sum_all()              = {sum_all()}")    # zero arguments is valid too


# ============================================================
# 2. MIXING REGULAR PARAMETERS WITH *args
# ============================================================

def multiply_all(multiplier, *args):
    """Multiplies each number in args by the multiplier."""
    results = [multiplier * n for n in args]
    print(f"  Multiplier: {multiplier} | Numbers: {args} -> {results}")
    return results

print("\n--- mixing regular + *args ---")
multiply_all(3, 1, 2, 3, 4)    # 3 is multiplier, rest go into args
multiply_all(10, 5, 6)


# ============================================================
# 3. **kwargs - ACCEPT ANY NUMBER OF KEYWORD ARGUMENTS
# ============================================================
# The ** collects extra keyword arguments into a DICTIONARY.
# Keys are the parameter names (strings), values are the passed values.

def print_profile(**kwargs):
    """
    Prints any key-value profile information.

    **kwargs collects all keyword arguments into a dict.
    """
    print(f"  kwargs received: {kwargs}  (type: {type(kwargs).__name__})")
    print("  --- Profile ---")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("\n--- **kwargs demo ---")
print_profile(name="Alice", age=30, city="New York", role="Engineer")
print()
print_profile(title="Python Book", pages=350, language="English")


# ============================================================
# 4. THE COMPLETE PARAMETER ORDER RULE
# ============================================================
# Python requires this exact order when mixing parameter types:
#
#   def func(positional, *args, keyword_only, **kwargs):
#
# 1. Regular positional parameters
# 2. *args (variable positional)
# 3. Keyword-only parameters (come AFTER *args)
# 4. **kwargs (variable keyword)

def full_demo(name, *scores, separator="-", **extra):
    """
    Demonstrates all parameter types together.

    Args:
        name (str): Person's name (regular positional).
        *scores: Any number of scores (variable positional).
        separator (str): Display separator (keyword-only, after *).
        **extra: Any additional info (variable keyword).
    """
    print(f"\n  Name: {name}")
    print(f"  Scores: {scores}")
    print(f"  Separator: '{separator}'")
    print(f"  Extra info: {extra}")
    if scores:
        avg = sum(scores) / len(scores)
        print(f"  Average score: {avg:.1f}")

print("\n--- Full parameter order demo ---")
full_demo("Alice", 85, 92, 78, separator="=", grade="A", subject="Python")
full_demo("Bob", 70, 65)   # only required and *args


# ============================================================
# 5. VARIABLE SCOPE - LOCAL vs GLOBAL
# ============================================================
# Scope = where in your code a variable is visible/accessible.
#
# LOCAL variable:  created inside a function, only lives there.
# GLOBAL variable: created outside all functions, visible everywhere.

planet = "Earth"        # GLOBAL variable

def explore_scope():
    moon = "Luna"       # LOCAL variable - only exists inside this function
    print(f"  Inside function - planet (global): {planet}")
    print(f"  Inside function - moon (local):    {moon}")

print("\n--- Scope demo ---")
explore_scope()
print(f"Outside function - planet: {planet}")

# Trying to access the local variable outside causes NameError:
# print(moon)   # <-- would raise: NameError: name 'moon' is not defined


# ============================================================
# 6. SHADOWING - local name hides global name
# ============================================================

color = "blue"      # global

def paint():
    color = "red"   # this is a NEW local variable, NOT changing the global
    print(f"  Inside paint() - color: {color}")   # red

paint()
print(f"After paint() - color: {color}")     # still blue - global unchanged


# ============================================================
# 7. THE global KEYWORD - modifying a global from inside a function
# ============================================================
# USE SPARINGLY - global state makes code hard to debug and test.
# Most of the time, use return instead.

counter = 0     # global counter

def increment():
    global counter          # tells Python: use the GLOBAL counter, not local
    counter += 1
    print(f"  counter is now: {counter}")

print("\n--- global keyword demo ---")
increment()
increment()
increment()
print(f"Final counter: {counter}")


# ============================================================
# 8. BETTER APPROACH: use return instead of global
# ============================================================

def increment_value(current):
    """Returns current + 1. No global state needed."""
    return current + 1

score = 0
score = increment_value(score)
score = increment_value(score)
print(f"\nScore with return approach: {score}")  # 2, clean and testable


# ============================================================
# 9. RECURSION - a function that calls itself
# ============================================================
# Every recursive function needs TWO things:
#   1. BASE CASE  - the condition to STOP (prevents infinite loop)
#   2. RECURSIVE CASE - the function calling itself with a SMALLER input

def factorial(n):
    """
    Calculates n! (n factorial) using recursion.

    n! = n * (n-1) * (n-2) * ... * 2 * 1
    e.g. 5! = 5 * 4 * 3 * 2 * 1 = 120

    Call stack trace for factorial(4):
        factorial(4)
          └─> 4 * factorial(3)
                    └─> 3 * factorial(2)
                                └─> 2 * factorial(1)
                                              └─> BASE CASE: return 1
                                          returns: 2 * 1 = 2
                              returns: 3 * 2 = 6
                  returns: 4 * 6 = 24

    Args:
        n (int): Non-negative integer.

    Returns:
        int: n factorial.
    """
    # BASE CASE: factorial of 0 or 1 is 1 (stops the recursion)
    if n <= 1:
        return 1

    # RECURSIVE CASE: n! = n * (n-1)!
    return n * factorial(n - 1)

print("\n--- Recursion: factorial ---")
for i in range(8):
    print(f"  {i}! = {factorial(i)}")


# ============================================================
# 10. RECURSION WITH VISIBLE CALL TRACE
# ============================================================
# This version prints indented output so you can SEE the call stack

def factorial_verbose(n, depth=0):
    """Factorial with indented call trace for learning purposes."""
    indent = "  " * depth
    print(f"{indent}factorial_verbose({n}) called")

    if n <= 1:
        print(f"{indent}  -> BASE CASE reached, returning 1")
        return 1

    result = n * factorial_verbose(n - 1, depth + 1)
    print(f"{indent}  -> returning {n} * ... = {result}")
    return result

print("\n--- Factorial call trace for factorial(5) ---")
answer = factorial_verbose(5)
print(f"\nFinal answer: 5! = {answer}")


# ============================================================
# 11. COMBINING *args + RECURSION - recursive sum
# ============================================================

def recursive_sum(numbers):
    """
    Sums a list recursively (educational - normally use sum() or a loop).

    Base case: empty list -> 0
    Recursive: first element + sum of the rest
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

print(f"\nrecursive_sum([1,2,3,4,5]) = {recursive_sum([1, 2, 3, 4, 5])}")
