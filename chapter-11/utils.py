"""
utils.py — Our very first custom module
========================================
This file is a MODULE we wrote ourselves. A module is simply a .py file
containing Python code (functions, variables, classes) that other files
can reuse with an `import` statement.

The functions below are small, reusable "helpers". Once this file exists,
any other script in the same folder can do:

    import utils
    print(utils.greet("Alice"))

or pull in specific functions:

    from utils import add, is_even

The `if __name__ == "__main__":` block at the bottom only runs when you
execute this file DIRECTLY (python3 utils.py). It does NOT run when this
module is imported by another file. That makes it a perfect spot for a
quick self-test.
"""

# A module can also hold constants (values that never change).
PI = 3.14159


def greet(name):
    """
    Builds a friendly greeting for a person.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting string, e.g. "Hello, Alice! Welcome."
    """
    return f"Hello, {name}! Welcome."


def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of a and b.
    """
    return a + b


def is_even(number):
    """
    Checks whether a whole number is even.

    Args:
        number (int): The number to test.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0


def area_of_circle(radius):
    """
    Computes the area of a circle from its radius.

    The formula is: area = PI * radius * radius

    Args:
        radius (int | float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return PI * radius * radius


# ============================================================
# SELF-TEST BLOCK
# ============================================================
# This only runs when you do:  python3 utils.py
# It is skipped when another file does:  import utils
if __name__ == "__main__":
    print("Running utils.py self-test...")
    print(greet("Alice"))
    print("add(2, 3) =", add(2, 3))
    print("is_even(10) =", is_even(10))
    print("is_even(7)  =", is_even(7))
    print("area_of_circle(5) =", area_of_circle(5))
    print("All self-tests finished.")
