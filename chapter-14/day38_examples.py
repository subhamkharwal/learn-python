"""
Chapter 14 - Day 38: Decorators and functools.reduce
=====================================================
Topics: what a decorator is, writing a decorator step by step,
        functools.wraps, decorators with arguments, functools.reduce.
"""

import time
import functools


# ============================================================
# 1. FUNCTIONS ARE OBJECTS (the idea behind decorators)
# ============================================================
# In Python, a function is just a value. You can store it in a variable,
# pass it to another function, and return it from a function.

def shout(text):
    return text.upper() + "!"

yell = shout                 # NOT calling it - just another name for it
print(f"Stored function: {yell('hello')}")    # HELLO!

# A function can RETURN another function.
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet             # hand the inner function back

say_hi = make_greeter("Hi")
print(f"Returned func  : {say_hi('Alice')}")  # Hi, Alice!


# ============================================================
# 2. WHAT IS A DECORATOR?
# ============================================================
# A decorator is a function that WRAPS another function to add behaviour
# WITHOUT changing the original function's code.
#
#     @my_decorator
#     def original():
#         ...
#
# is just shorthand for:
#
#     original = my_decorator(original)
#
# Picture the wrapping like this:
#
#     call ---> [ wrapper: do something BEFORE ]
#                       |
#                       v
#               [ original function runs ]
#                       |
#                       v
#               [ wrapper: do something AFTER ]
#                       |
#                       v  return result back to caller


# ============================================================
# 3. WRITING A SIMPLE DECORATOR, STEP BY STEP
# ============================================================
# A decorator takes a function (`func`) and returns a NEW function
# (`wrapper`) that calls the original somewhere in the middle.

def announce(func):                       # 1) takes the function to wrap
    def wrapper(*args, **kwargs):         # 2) accepts ANY arguments
        print("  >> before the function runs")
        result = func(*args, **kwargs)    # 3) call the original
        print("  >> after the function runs")
        return result                     # 4) pass its result back
    return wrapper                        # 5) return the wrapper

@announce
def add(a, b):
    print(f"  computing {a} + {b}")
    return a + b

print("\nCalling decorated add(2, 3):")
total = add(2, 3)
print(f"Result         : {total}")
# >> before the function runs
# computing 2 + 3
# >> after the function runs
# Result : 5


# ============================================================
# 4. WHY functools.wraps?
# ============================================================
# Without help, the wrapper REPLACES the original's name and docstring,
# so introspection (__name__, __doc__, help()) reports the wrapper.
# functools.wraps copies that metadata across so the decorated function
# still "looks like itself".

def announce_bad(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def announce_good(func):
    @functools.wraps(func)               # copies name, docstring, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@announce_bad
def task_bad():
    """Does an important task."""

@announce_good
def task_good():
    """Does an important task."""

print("\nWithout functools.wraps:")
print(f"  name = {task_bad.__name__}")   # wrapper  (lost!)
print(f"  doc  = {task_bad.__doc__}")    # None     (lost!)

print("With functools.wraps:")
print(f"  name = {task_good.__name__}")  # task_good (preserved)
print(f"  doc  = {task_good.__doc__}")   # Does an important task.


# ============================================================
# 5. HANDS-ON: a @timer decorator
# ============================================================
# Measures how long the wrapped function takes to run.
# We use a tiny time.sleep so the demo runs fast.

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()          # record start time
        result = func(*args, **kwargs)       # run the real function
        elapsed = time.perf_counter() - start
        print(f"  [timer] {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.05)                         # pretend this is slow work
    return a + b

print("\nCalling timed slow_add(10, 20):")
print(f"Result         : {slow_add(10, 20)}")


# ============================================================
# 6. HANDS-ON: a @validate_positive decorator
# ============================================================
# Checks that every numeric argument is positive BEFORE running the
# function. If not, it raises a clear error.

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(
                    f"{func.__name__} requires positive numbers, got {value}"
                )
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def area_of_rectangle(width, height):
    return width * height

print("\nValidate-positive decorator:")
print(f"  area(3, 4) = {area_of_rectangle(3, 4)}")   # 12

# This call raises ValueError because -2 is not positive.
try:
    area_of_rectangle(-2, 5)
except ValueError as error:
    print(f"  caught error: {error}")


# ============================================================
# 7. DECORATORS WITH ARGUMENTS (briefly)
# ============================================================
# To configure a decorator, add ONE more layer: a function that takes the
# arguments and RETURNS a decorator. So there are three nested functions.
#
#     repeat(times)      -> the configurable outer layer
#       decorator(func)  -> the actual decorator
#         wrapper(...)   -> the replacement function

def repeat(times):                           # 1) takes the config value
    def decorator(func):                     # 2) the real decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):        # 3) the wrapper
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def wave():
    print("  wave!")

print("\nrepeat(times=3) decorator:")
wave()                                       # prints "wave!" three times


# ============================================================
# 8. functools.reduce - boil a sequence down to ONE value
# ============================================================
# reduce(function, iterable) applies a two-argument function cumulatively,
# carrying the running result forward.
#
#     reduce(f, [a, b, c, d])  ==  f(f(f(a, b), c), d)
#
# Multiply all numbers together (a "product").

numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda running, n: running * n, numbers)
print(f"\nreduce product : {product}")       # 120  (1*2*3*4*5)

# How it unfolds step by step:
#   start: 1
#   1 * 2 = 2
#   2 * 3 = 6
#   6 * 4 = 24
#   24 * 5 = 120

# Find the maximum with reduce (just to illustrate the pattern;
# in real code you would simply use the built-in max()).
biggest = functools.reduce(lambda a, b: a if a > b else b, numbers)
print(f"reduce max     : {biggest}")         # 5

# You can give reduce a starting value as a third argument.
total = functools.reduce(lambda running, n: running + n, numbers, 100)
print(f"reduce sum+100 : {total}")           # 115  (100 + 1+2+3+4+5)
