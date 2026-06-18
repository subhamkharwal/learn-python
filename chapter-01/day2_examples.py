# =============================================================================
# Chapter 01 — Day 2 Examples
# Topic: Writing scripts, print() deep dive, and comments
#
# How to run this file:
#   Open your terminal, navigate to this folder, then run:
#       python day2_examples.py
#   or:
#       python3 day2_examples.py
#
# This file IS the example — it demonstrates comments and print() by using them.
# =============================================================================


# -----------------------------------------------------------------------------
# SECTION 1: This script itself demonstrates how comments work
# -----------------------------------------------------------------------------

# A comment starts with # and Python ignores everything after # on that line.
# Comments are notes for humans reading the code — not instructions for Python.

# Python executes the print() below, but ignores the comment next to it:
print("Comments don't appear in the output")  # This part is a comment

# You can "comment out" a line to temporarily disable it:
# print("This line is commented out — it will NOT run")
print("This line is NOT commented out — it WILL run")


# -----------------------------------------------------------------------------
# SECTION 2: Basic print() — printing different types of values
# -----------------------------------------------------------------------------

print("\n=== Section 2: Basic print() ===")

# Printing a string (text surrounded by quotes)
print("Hello, World!")         # Output: Hello, World!
print('Single quotes work too') # Output: Single quotes work too

# Printing numbers — no quotes needed for numbers
print(42)                       # Output: 42
print(3.14159)                  # Output: 3.14159

# Printing the result of a calculation
print(100 - 37)                 # Output: 63
print(2 ** 8)                   # Output: 256

# Printing a boolean (True/False — capital T and F matter!)
print(True)                     # Output: True
print(False)                    # Output: False

# Printing nothing — creates a blank line in the output
print()                         # Output: (blank line)


# -----------------------------------------------------------------------------
# SECTION 3: print() with multiple arguments
# -----------------------------------------------------------------------------

print("=== Section 3: Multiple Arguments ===")

# You can pass multiple values to print(), separated by commas.
# Python automatically puts a SPACE between each value.

print("My name is", "Alice")
# Output: My name is Alice

print("The answer is", 42)
# Output: The answer is 42

print("Sum:", 10 + 5, "Difference:", 10 - 5)
# Output: Sum: 15 Difference: 5

# Mixing strings and numbers — Python handles the formatting
print("I have", 3, "cats and", 2, "dogs")
# Output: I have 3 cats and 2 dogs


# -----------------------------------------------------------------------------
# SECTION 4: The sep parameter — customize the separator
# -----------------------------------------------------------------------------

print("\n=== Section 4: sep parameter ===")

# By default, print() separates multiple values with a space.
# The sep parameter lets you change this.

# Default behavior (sep=" " — a space)
print("apple", "banana", "cherry")
# Output: apple banana cherry

# Using a custom separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

print("apple", "banana", "cherry", sep=" | ")
# Output: apple | banana | cherry

# Useful for dates, file paths, etc.
print("2024", "06", "18", sep="-")         # Output: 2024-06-18
print("Users", "alice", "Desktop", sep="/") # Output: Users/alice/Desktop

# Using an empty string separator — values are joined with nothing between them
print("a", "b", "c", sep="")
# Output: abc

# Printing a grid/table-like row
print("Name", "Age", "City", sep="\t")  # \t is a tab character
# Output: Name	Age	City


# -----------------------------------------------------------------------------
# SECTION 5: The end parameter — customize the line ending
# -----------------------------------------------------------------------------

print("\n=== Section 5: end parameter ===")

# By default, print() ends with a newline (\n), putting the next output
# on a new line. The end parameter lets you change this.

# Default behavior — each print is on its own line
print("First")
print("Second")
print("Third")
# Output:
# First
# Second
# Third

print()  # blank line to separate examples

# Using end="" — no newline, next print continues on the SAME line
print("First", end="")
print("Second", end="")
print("Third")
# Output: FirstSecondThird

print()  # blank line

# Using end=" " — space at end instead of newline
print("First", end=" ")
print("Second", end=" ")
print("Third")
# Output: First Second Third

print()  # blank line

# Practical example: printing a progress-style message
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Done!")
# Output: Loading... Done!

print()  # blank line

# Combining sep and end
print("a", "b", "c", sep="-", end="!\n")
# Output: a-b-c!


# -----------------------------------------------------------------------------
# SECTION 6: Escape sequences inside strings
# -----------------------------------------------------------------------------

print("=== Section 6: Escape Sequences ===")

# \n — newline character: moves to the next line
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

print()

# \t — tab character: adds a horizontal indent
print("Name:\tAlice")
print("Age:\t30")
print("City:\tNew York")
# Output:
# Name:	Alice
# Age:	30
# City:	New York

print()

# \" — lets you include double quotes inside a double-quoted string
print("She said \"Hello!\"")
# Output: She said "Hello!"

# \' — lets you include single quotes inside a single-quoted string
print('It\'s a great day!')
# Output: It's a great day!
# (Alternative: use double quotes on the outside)
print("It's a great day!")
# Output: It's a great day!

# \\ — a literal backslash
print("Folder path: C:\\Users\\Alice\\Desktop")
# Output: Folder path: C:\Users\Alice\Desktop


# -----------------------------------------------------------------------------
# SECTION 7: Triple-quoted strings for multi-line output
# -----------------------------------------------------------------------------

print("\n=== Section 7: Triple-Quoted Strings ===")

# Triple quotes (""" or ''') let you write text across multiple lines
# without needing \n escape sequences.

print("""This text
spans multiple
lines automatically.""")
# Output:
# This text
# spans multiple
# lines automatically.

print()

# Useful for printing formatted blocks of text
print("""
+---------------------------+
|  Welcome to Python!       |
|  Let's learn together.    |
+---------------------------+
""")


# -----------------------------------------------------------------------------
# SECTION 8: Inline comments — good style practices
# -----------------------------------------------------------------------------

print("=== Section 8: Comment Style ===")

# Good: comment explains WHY, not WHAT (the code already says what)
total_seconds = 60 * 60 * 24  # seconds in one day
print(total_seconds)  # Output: 86400

# Acceptable: comment clarifies a non-obvious value
max_retries = 3  # industry standard; don't increase without testing
print(max_retries)

# Bad practice (avoid): comment just repeats the code
# print hello
print("hello")  # This comment adds no value — the code is already clear


# Multi-line comment using multiple # lines
# This section demonstrates that Python has no dedicated
# multi-line comment syntax like /* ... */ in other languages.
# We simply start each line with #.
print("Multi-line comment above — Python ignored all of it.")


# -----------------------------------------------------------------------------
# SECTION 9: hello_world.py — putting it all together
# -----------------------------------------------------------------------------

print("\n=== Section 9: hello_world.py Demonstration ===")

# This section mimics what a real hello_world.py script would look like.
# It is a small, complete program that shows off everything from Day 2.

# --- Header ---
print("=" * 40)         # Print 40 = signs  (string repetition — covered in Ch.04)
print("  My First Python Program")
print("  Author: Your Name Here")
print("=" * 40)

# --- Greeting ---
print()
print("Hello, World!")
print("Welcome to Python programming.")
print()

# --- Some output using sep ---
print("Today is:", "Wednesday, June 18, 2026")
print("Python version:", "3.x")
print()

# --- Multi-line message with \n ---
print("Python is:\n  - Easy to learn\n  - Powerful\n  - Fun!")
print()

# --- Closing ---
print("-" * 40)
print("End of program. Goodbye!")
print("-" * 40)


# =============================================================================
# END OF DAY 2 EXAMPLES
#
# Key takeaways:
#   1. .py files are saved Python code that you run from the terminal
#   2. Comments start with # and are ignored by Python
#   3. print() shows output, and accepts sep= and end= keyword arguments
#   4. \n adds a newline, \t adds a tab, inside strings
#   5. Always run scripts with: python script.py  (or python3 on Mac/Linux)
# =============================================================================
