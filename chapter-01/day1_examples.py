# =============================================================================
# Chapter 01 — Day 1 Examples
# Topic: Python REPL, basic output, and arithmetic
#
# How to use this file:
#   These examples are written to mimic REPL sessions.
#   You can run this whole file: python day1_examples.py
#   Or open the Python REPL and type each expression one by one.
# =============================================================================


# -----------------------------------------------------------------------------
# SECTION 1: Your very first Python output
# -----------------------------------------------------------------------------

# print() is a built-in function that displays text on the screen.
# Whatever you put inside the parentheses gets shown.

print("Hello, World!")         # Expected output: Hello, World!
print("Hello, Python!")        # Expected output: Hello, Python!
print("My first program!")     # Expected output: My first program!


# -----------------------------------------------------------------------------
# SECTION 2: Python as a calculator — arithmetic operators
# -----------------------------------------------------------------------------

# In the REPL you can type just: 2 + 3
# and Python shows 5 immediately.
# In a script, you need print() to see the result.

print("--- Basic Arithmetic ---")

# Addition
print(2 + 3)        # Expected output: 5
print(100 + 200)    # Expected output: 300

# Subtraction
print(10 - 4)       # Expected output: 6
print(50 - 75)      # Expected output: -25

# Multiplication
print(3 * 7)        # Expected output: 21
print(12 * 12)      # Expected output: 144


# -----------------------------------------------------------------------------
# SECTION 3: Division — two kinds
# -----------------------------------------------------------------------------

print("--- Division ---")

# Regular division — always gives a decimal (float)
print(10 / 3)       # Expected output: 3.3333333333333335
print(8 / 2)        # Expected output: 4.0  <-- notice the .0, it's still a float

# Floor division (//) — divides and throws away the decimal part
# Think of it as "how many WHOLE times does 3 go into 10?"
print(10 // 3)      # Expected output: 3
print(8 // 2)       # Expected output: 4
print(7 // 2)       # Expected output: 3  (not 3.5 — the decimal is dropped)


# -----------------------------------------------------------------------------
# SECTION 4: Modulo — the remainder operator
# -----------------------------------------------------------------------------

print("--- Modulo (Remainder) ---")

# % gives you the REMAINDER after division.
# "What is left over after dividing as many whole times as possible?"

# 10 divided by 3 = 3 remainder 1
print(10 % 3)       # Expected output: 1

# 7 divided by 2 = 3 remainder 1
print(7 % 2)        # Expected output: 1

# 10 divided by 5 = 2 remainder 0
print(10 % 5)       # Expected output: 0

# Practical use: checking if a number is even or odd
# Even numbers have remainder 0 when divided by 2
print(4 % 2)        # Expected output: 0  (4 is even)
print(7 % 2)        # Expected output: 1  (7 is odd)


# -----------------------------------------------------------------------------
# SECTION 5: Exponentiation — powers
# -----------------------------------------------------------------------------

print("--- Exponentiation (Powers) ---")

# ** is the power operator
# 2 ** 3 means 2 raised to the power of 3 = 2 * 2 * 2 = 8

print(2 ** 3)       # Expected output: 8
print(5 ** 2)       # Expected output: 25   (5 squared)
print(10 ** 0)      # Expected output: 1    (any number to the power of 0 is 1)
print(2 ** 10)      # Expected output: 1024 (1 KB in bytes)
print(2 ** 32)      # Expected output: 4294967296 (max value of a 32-bit number)


# -----------------------------------------------------------------------------
# SECTION 6: Operator precedence — order of operations
# -----------------------------------------------------------------------------

print("--- Operator Precedence ---")

# Python follows PEMDAS / BODMAS:
# Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction

# Without parentheses: multiplication happens before addition
print(5 + 3 * 2)    # Expected output: 11   (3*2=6, then 5+6=11)

# With parentheses: parentheses go first
print((5 + 3) * 2)  # Expected output: 16   (5+3=8, then 8*2=16)

# More examples
print(2 + 3 ** 2)   # Expected output: 11   (3**2=9, then 2+9=11)
print(10 - 6 / 2)   # Expected output: 7.0  (6/2=3.0, then 10-3.0=7.0)
print(10 / 2 + 3)   # Expected output: 8.0  (10/2=5.0, then 5.0+3=8.0)


# -----------------------------------------------------------------------------
# SECTION 7: Combining print with math
# -----------------------------------------------------------------------------

print("--- Combining print() with math ---")

# print() can show the result of a calculation
print(7 * 24 * 60)          # Minutes in a week → Expected output: 10080

# You can mix text and numbers in separate print arguments
# (We'll cover mixing text + numbers more in Chapter 02 with variables)
print("2 + 2 =", 2 + 2)     # Expected output: 2 + 2 = 4
print("10 squared:", 10 ** 2) # Expected output: 10 squared: 100


# -----------------------------------------------------------------------------
# SECTION 8: Blank lines in output
# -----------------------------------------------------------------------------

# Calling print() with nothing inside prints a blank line.
# Useful for visual spacing in your output.

print("First block of output")
print()                         # Blank line
print("Second block of output")
print()
print()                         # Two blank lines
print("Third block of output")


# =============================================================================
# REPL SESSION SIMULATOR
# The block below shows you what a real REPL session looks like.
# If you type these expressions directly into the REPL (not a script),
# Python shows the result WITHOUT needing print().
# =============================================================================

print("\n--- End of Day 1 Examples ---")
print("Tip: Open the REPL (type 'python' in terminal) and try these yourself!")
print("In the REPL, just type: 2 + 3  (no print needed) and press Enter.")
