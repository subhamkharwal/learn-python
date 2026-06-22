"""
Chapter 11 - Day 28: Importing & the Standard Library
=====================================================
Topics: import, from ... import, import ... as alias,
        math / random / datetime / os / sys modules,
        and the if __name__ == "__main__": idiom.

Run me with:  python3 day28_examples.py
Everything here uses only Python's BUILT-IN standard library,
so nothing needs to be installed first.
"""

# ============================================================
# 1. THREE WAYS TO IMPORT
# ============================================================
# (a) import the whole module — access names with the module prefix
import math

# (b) import specific names — use them WITHOUT the module prefix
from random import randint, choice

# (c) import with an alias (a nickname) — handy for long module names
import datetime as dt

print("--- 1. Import styles ---")
print("math.sqrt(16) =", math.sqrt(16))      # whole module + prefix
print("randint(1, 6) =", randint(1, 6))      # imported name, no prefix
print("dt module alias works:", dt.date.today())  # alias prefix


# ============================================================
# 2. THE math MODULE — numbers, roots, rounding, constants
# ============================================================
print("\n--- 2. math module ---")
print("math.pi      =", math.pi)             # the constant pi
print("math.e       =", math.e)              # Euler's number
print("math.sqrt(81)=", math.sqrt(81))       # square root
print("math.pow(2,5)=", math.pow(2, 5))      # 2 to the power 5 -> 32.0
print("math.floor(3.7)=", math.floor(3.7))   # round DOWN -> 3
print("math.ceil(3.1) =", math.ceil(3.1))    # round UP   -> 4
print("math.factorial(5) =", math.factorial(5))  # 5! -> 120
print("math.gcd(12, 18)  =", math.gcd(12, 18))    # greatest common divisor


# ============================================================
# 3. THE random MODULE — randomness for games & sampling
# ============================================================
# NOTE: we do NOT set a seed, so values change every run. That's fine!
import random

print("\n--- 3. random module ---")
print("random.random()    =", random.random())       # float in [0.0, 1.0)
print("random.randint(1,6)=", random.randint(1, 6))   # int 1..6 (inclusive)
print("random.uniform(1,10)=", random.uniform(1, 10)) # float 1.0..10.0

colors = ["red", "green", "blue", "yellow"]
print("random.choice(colors)  =", random.choice(colors))     # pick one
print("random.sample(colors,2)=", random.sample(colors, 2))  # pick 2 unique

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)          # shuffles the list IN PLACE
print("shuffled deck         =", deck)


# ============================================================
# 4. THE datetime MODULE — dates, times, and date math
# ============================================================
from datetime import date, datetime, timedelta

print("\n--- 4. datetime module ---")
today = date.today()
print("Today is        :", today)
print("Year / Month / Day:", today.year, today.month, today.day)

now = datetime.now()
print("Right now       :", now.strftime("%Y-%m-%d %H:%M:%S"))  # formatted

# Date math with timedelta — "how many days from now?"
one_week_later = today + timedelta(days=7)
print("One week later  :", one_week_later)

# How many days until a future date?
new_year = date(today.year + 1, 1, 1)
days_left = (new_year - today).days
print(f"Days until next New Year: {days_left}")


# ============================================================
# 5. THE os MODULE — talk to the operating system
# ============================================================
import os

print("\n--- 5. os module ---")
print("Current working directory:", os.getcwd())     # where am I?
print("Files here (first 5):", os.listdir(".")[:5])   # list this folder
# os.path helps build/inspect file paths safely across operating systems
path = os.path.join("folder", "subfolder", "file.txt")
print("os.path.join ->", path)
print("Base name    ->", os.path.basename(path))      # file.txt
print("Directory    ->", os.path.dirname(path))       # folder/subfolder
# Reading an environment variable (with a fallback if it's missing)
print("HOME env var :", os.environ.get("HOME", "not set"))


# ============================================================
# 6. THE sys MODULE — the Python interpreter itself
# ============================================================
import sys

print("\n--- 6. sys module ---")
print("Python version :", sys.version.split()[0])   # just the number part
print("Platform       :", sys.platform)             # 'darwin', 'linux', 'win32'
print("Script name    :", sys.argv[0])              # the file being run
# sys.argv is a list of command-line arguments. Try:  python3 day28_examples.py hello
print("All arguments  :", sys.argv)


# ============================================================
# 7. THE if __name__ == "__main__": IDIOM
# ============================================================
# Every Python file has a hidden variable called __name__.
#   * When you RUN a file directly:      __name__ == "__main__"
#   * When the file is IMPORTED elsewhere: __name__ == the module's name
#
# So this block only runs when THIS file is the program being executed,
# not when someone does `import day28_examples`. Use it to keep "demo" or
# "test" code from firing on import.
def main():
    """Entry point for the demo when run directly."""
    print("\n--- 7. __main__ idiom ---")
    print(f"__name__ is currently: {__name__!r}")
    print("Because that equals '__main__', this main() ran.")
    roll = random.randint(1, 6)
    print(f"Bonus dice roll: you rolled a {roll}!")


if __name__ == "__main__":
    main()
