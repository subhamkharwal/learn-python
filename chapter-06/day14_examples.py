"""
Chapter 06 — Day 14: Nested Loops, for/else, Loop Patterns
===========================================================
Topics covered:
  - Nested loops (loop inside a loop)
  - for/else — else runs only when no break occurred
  - while/else — same behaviour for while loops
  - Classic loop patterns: accumulator, counter, flag
  - Hands-on: Triangle patterns, grid patterns, prime number finder
"""

# ─────────────────────────────────────────────
# Section 1: Nested Loops
# ─────────────────────────────────────────────
print("=" * 40)
print("SECTION 1: Nested loops")
print("=" * 40)

# A nested loop is simply a loop inside another loop.
# The INNER loop completes ALL its iterations for EVERY
# single iteration of the OUTER loop.
#
# Total iterations = outer_count × inner_count

print("3 x 4 grid of coordinates:")
for i in range(3):          # outer loop  — controls rows (i = 0,1,2)
    for j in range(4):      # inner loop  — controls columns (j = 0,1,2,3)
        print(f"({i},{j})", end=" ")
    print()                 # newline after each row completes

# Output:
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)


# ─────────────────────────────────────────────
# Section 2: Triangle Pattern (right-aligned)
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 2: Triangle pattern")
print("=" * 40)

# Row 1: *
# Row 2: * *
# Row 3: * * *
# Row 4: * * * *
# Row 5: * * * * *
#
# Notice: on row i, we print i stars.
# The outer loop controls the row number.
# The inner loop prints that many stars.

rows = 5
print("Right-growing triangle:")
for i in range(1, rows + 1):       # i goes 1, 2, 3, 4, 5
    for j in range(i):             # j goes 0..i-1 (i repetitions)
        print("*", end=" ")
    print()                        # move to the next line

print("\nInverted triangle:")
for i in range(rows, 0, -1):      # i goes 5, 4, 3, 2, 1
    for j in range(i):
        print("*", end=" ")
    print()


# ─────────────────────────────────────────────
# Section 3: More Patterns
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 3: More patterns with nested loops")
print("=" * 40)

# Solid rectangle
print("Solid rectangle (4 wide × 3 tall):")
for row in range(3):
    for col in range(4):
        print("#", end=" ")
    print()

# Number staircase
print("\nNumber staircase:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Square border (hollow)
print("\nHollow square (5×5):")
size = 5
for row in range(size):
    for col in range(size):
        # Print '#' on the edges, space in the middle
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()


# ─────────────────────────────────────────────
# Section 4: for/else — The Unusual Python Feature
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 4: for/else")
print("=" * 40)

# Python loops can have an 'else' clause.
# The else block runs ONLY if the loop finished without hitting a break.
# If break fired → else is SKIPPED.

# Example A: no break → else RUNS
print("Example A: searching for 9 in [1, 2, 3, 4, 5]")
numbers = [1, 2, 3, 4, 5]
target = 9

for num in numbers:
    if num == target:
        print(f"  Found {target}!")
        break
else:
    # This runs because we never broke out of the loop
    print(f"  {target} was NOT found in the list.")

# Example B: break fires → else SKIPPED
print("\nExample B: searching for 3 in [1, 2, 3, 4, 5]")
target = 3

for num in numbers:
    if num == target:
        print(f"  Found {target}! (break fires → else is skipped)")
        break
else:
    print(f"  {target} was NOT found.")   # this line will NOT run


# ─────────────────────────────────────────────
# Section 5: while/else
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 5: while/else")
print("=" * 40)

# while/else works the same as for/else.

print("while/else — loop completes normally → else runs:")
count = 0
while count < 4:
    print(f"  count = {count}")
    count += 1
else:
    print("  Loop finished without break → else runs!")

print("\nwhile/else — break fires → else is skipped:")
count = 0
while count < 10:
    if count == 3:
        print(f"  break at count = {count} → else is skipped!")
        break
    print(f"  count = {count}")
    count += 1
else:
    print("  This will NOT print because break fired.")


# ─────────────────────────────────────────────
# Section 6: Classic Pattern — Accumulator
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 6: Accumulator pattern")
print("=" * 40)

# An accumulator starts at a neutral value (0 for sum, 1 for product)
# and collects a running total as the loop progresses.

numbers = [4, 7, 2, 9, 1, 5, 3]

# Sum accumulator
total = 0                       # identity for addition is 0
for n in numbers:
    total += n                  # total = total + n

print(f"Numbers: {numbers}")
print(f"Sum:     {total}")      # 31

# Product accumulator
product = 1                     # identity for multiplication is 1
for n in numbers:
    product *= n                # product = product * n

print(f"Product: {product}")    # 4*7*2*9*1*5*3 = 7560

# Maximum value (without using built-in max())
largest = numbers[0]            # start with the first element
for n in numbers:
    if n > largest:
        largest = n             # update if we found something bigger

print(f"Largest: {largest}")    # 9


# ─────────────────────────────────────────────
# Section 7: Classic Pattern — Counter
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 7: Counter pattern")
print("=" * 40)

# A counter starts at 0 and increments whenever
# a condition is satisfied.

words = ["apple", "ant", "banana", "avocado", "cherry", "almond"]
count_a = 0                     # count words starting with 'a'

for word in words:
    if word.startswith("a"):
        count_a += 1            # increment the counter

print(f"Words: {words}")
print(f"Words starting with 'a': {count_a}")   # 4


# ─────────────────────────────────────────────
# Section 8: Classic Pattern — Flag Variable
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 8: Flag variable pattern")
print("=" * 40)

# A flag is a boolean (True/False) variable that records
# whether some condition was ever triggered during a loop.

scores = [72, 85, 91, 68, 55, 88]
has_failing_score = False       # assume no failure at the start

for score in scores:
    if score < 60:
        has_failing_score = True    # raise the flag
        break                       # no need to check further

if has_failing_score:
    print("Warning: at least one failing score found!")
else:
    print("All scores are passing.")

# Note: the for/else pattern can replace the flag in many cases:
print("\nSame check using for/else (cleaner):")
for score in scores:
    if score < 60:
        print("Warning: at least one failing score found!")
        break
else:
    print("All scores are passing.")


# ─────────────────────────────────────────────
# HANDS-ON 1: Triangle Patterns
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 1: Triangle Patterns")
print("=" * 40)

# Pattern 1: Right-aligned star triangle
print("Right-aligned star triangle:")
rows = 6
for i in range(1, rows + 1):
    print("* " * i)

# Pattern 2: Right-justified number triangle
print("\nRight-justified number triangle (spaces added):")
for i in range(1, rows + 1):
    # Print leading spaces so numbers align to the right
    spaces = " " * (rows - i)
    numbers_part = " ".join(str(j) for j in range(1, i + 1))
    print(spaces + numbers_part)

# Pattern 3: Diamond (combine growing + shrinking triangles)
print("\nDiamond:")
half = 4
for i in range(1, half + 1):
    print(" " * (half - i) + "* " * i)
for i in range(half - 1, 0, -1):
    print(" " * (half - i) + "* " * i)


# ─────────────────────────────────────────────
# HANDS-ON 2: Prime Number Finder using for/else
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 2: Prime Number Finder")
print("=" * 40)

# A prime number is divisible ONLY by 1 and itself.
#
# Algorithm:
#   For n >= 2, try every potential divisor from 2 to n-1.
#   If any divisor divides n evenly → n is NOT prime (break).
#   If the loop finishes without finding a divisor → n IS prime (else).

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False            # 0 and 1 are not prime by definition

    # Try every number from 2 up to (but not including) n
    for divisor in range(2, n):
        if n % divisor == 0:   # divisor divides n evenly → not prime
            break              # no need to check further
    else:
        # The for loop completed WITHOUT hitting break
        # → no divisors found → n is prime
        return True

    # If we reach here, break fired → n is NOT prime
    return False


# Optimised version: only check up to √n
# (any factor larger than √n would pair with one smaller than √n)
import math

def is_prime_fast(n):
    """Faster primality check — only tests divisors up to sqrt(n)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False            # quickly reject all even numbers > 2

    # Only check odd divisors from 3 up to √n
    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False
    return True


print("Prime numbers from 2 to 50 (basic method):")
primes = []
for num in range(2, 51):
    if is_prime(num):
        primes.append(num)
print(primes)

print("\nPrime numbers from 2 to 50 (fast method):")
primes_fast = []
for num in range(2, 51):
    if is_prime_fast(num):
        primes_fast.append(num)
print(primes_fast)

print(f"\nBoth methods agree: {primes == primes_fast}")

# Count primes up to 100
count = sum(1 for n in range(2, 101) if is_prime_fast(n))
print(f"\nNumber of primes between 2 and 100: {count}")


# ─────────────────────────────────────────────
# BONUS: Full multiplication table using nested loops
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("BONUS: Full 10×10 multiplication table")
print("=" * 40)

# Print a neatly formatted 10×10 grid

# Header row
print("    ", end="")
for j in range(1, 11):
    print(f"{j:4d}", end="")
print()
print("    " + "─" * 40)

# Data rows
for i in range(1, 11):
    print(f"{i:3d}│", end="")      # row number
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
