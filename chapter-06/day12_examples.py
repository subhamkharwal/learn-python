"""
Chapter 06 — Day 12: The for Loop
==================================
Topics covered:
  - Basic for loop syntax
  - range(stop), range(start, stop), range(start, stop, step)
  - Iterating over a string character by character
  - Index-based loops using range(len(...))
  - Hands-on: Multiplication table & Sum of first N numbers
"""

# ─────────────────────────────────────────────
# Section 1: Basic for loop with a list
# ─────────────────────────────────────────────
print("=" * 40)
print("SECTION 1: for loop over a list")
print("=" * 40)

fruits = ["apple", "banana", "cherry"]

# The loop variable 'fruit' takes each value from the list in order
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry


# ─────────────────────────────────────────────
# Section 2: range(stop)
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 2: range(stop)")
print("=" * 40)

# range(5) produces 0, 1, 2, 3, 4
# Note: stops BEFORE 5
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()  # newline after the row


# ─────────────────────────────────────────────
# Section 3: range(start, stop)
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 3: range(start, stop)")
print("=" * 40)

# range(1, 6) produces 1, 2, 3, 4, 5
# Note: includes 1, stops BEFORE 6
print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")
print()


# ─────────────────────────────────────────────
# Section 4: range(start, stop, step)
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 4: range(start, stop, step)")
print("=" * 40)

# Step of 2 — every other number
print("range(0, 10, 2)  — even numbers:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Negative step — counting backwards
print("range(5, 0, -1)  — countdown:")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Step of 3
print("range(1, 20, 3)  — every 3rd number:")
for i in range(1, 20, 3):
    print(i, end=" ")
print()


# ─────────────────────────────────────────────
# Section 5: Iterating over a string
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 5: Iterating over a string")
print("=" * 40)

word = "Python"

# Each character is visited one at a time
print(f"Characters in '{word}':")
for ch in word:
    print(ch, end=" ")
print()

# Practical use: count how many vowels are in a word
vowels = "aeiouAEIOU"
vowel_count = 0
sentence = "Hello, my name is Python!"

for ch in sentence:
    if ch in vowels:  # 'in' checks if ch is inside the vowels string
        vowel_count += 1

print(f"\nSentence: '{sentence}'")
print(f"Number of vowels: {vowel_count}")


# ─────────────────────────────────────────────
# Section 6: Index-based loop with range(len(...))
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 6: Index-based loop")
print("=" * 40)

word = "Python"

# len("Python") = 6
# range(6) = 0, 1, 2, 3, 4, 5
# word[0] = 'P', word[1] = 'y', ...
print(f"Index-based iteration over '{word}':")
for i in range(len(word)):
    print(f"  Index {i}: '{word[i]}'")


# ─────────────────────────────────────────────
# HANDS-ON 1: Multiplication Table
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 1: Multiplication Table")
print("=" * 40)

# We'll print the multiplication table for the number n
n = 7

print(f"Multiplication table for {n}:")
print("-" * 20)

for i in range(1, 11):      # i goes from 1 to 10 (inclusive)
    result = n * i           # calculate the product
    print(f"  {n} x {i:2d} = {result:3d}")  # :2d pads i to 2 digits

# Output:
#   7 x  1 =   7
#   7 x  2 =  14
#   ...
#   7 x 10 =  70


# ─────────────────────────────────────────────
# HANDS-ON 2: Sum of First N Numbers
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 2: Sum of First N Numbers")
print("=" * 40)

# Add up every number from 1 to N
n = 10

# We use an "accumulator" variable that starts at 0
# and grows as we add each number to it
total = 0

print(f"Adding numbers 1 to {n}:")
for i in range(1, n + 1):   # n+1 so the range INCLUDES n
    total += i               # same as: total = total + i
    print(f"  After adding {i:2d}: total = {total}")

print(f"\nFinal answer: Sum of 1 to {n} = {total}")

# The formula is n*(n+1)/2, let's verify:
formula_result = n * (n + 1) // 2
print(f"Verification using formula n*(n+1)/2 = {formula_result}")


# ─────────────────────────────────────────────
# BONUS: Full multiplication table (all numbers 1–5)
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("BONUS: Mini multiplication table (1-5)")
print("=" * 40)

# Print header row
print("    ", end="")
for j in range(1, 6):
    print(f"{j:4d}", end="")
print()
print("    " + "─" * 20)

# Print each row
for i in range(1, 6):
    print(f"{i:3d}│", end="")     # row label
    for j in range(1, 6):
        print(f"{i * j:4d}", end="")
    print()
