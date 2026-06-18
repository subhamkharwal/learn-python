# =============================================================================
# Chapter 04 — Strings In-Depth
# Day 7: String Creation, Indexing, len(), and Immutability
# =============================================================================
# Run this file: python day7_examples.py
# Every section is clearly labeled so you can follow along with the notes.
# =============================================================================


# -----------------------------------------------------------------------------
# SECTION 1: Creating Strings
# -----------------------------------------------------------------------------

print("=" * 60)
print("SECTION 1: Creating Strings")
print("=" * 60)

# Single quotes
name_single = 'Alice'
print(name_single)         # Alice

# Double quotes — identical to single quotes
name_double = "Alice"
print(name_double)         # Alice

# Single and double are interchangeable
print(name_single == name_double)   # True — same string

# Using double quotes to include an apostrophe without escaping
sentence = "It's a great day to learn Python!"
print(sentence)

# Using single quotes to include double quotes without escaping
dialogue = 'She said "Python is amazing!"'
print(dialogue)

# Triple double quotes — multi-line string
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)

# Triple single quotes — same as triple double quotes
haiku = '''An old silent pond
A frog jumps into the pond
Splash! Silence again.'''
print(haiku)

# Triple-quoted strings are useful for long text blocks
description = """Python is a high-level, general-purpose programming language.
It was created by Guido van Rossum and first released in 1991.
Known for its clean syntax and readability."""
print(description)


# -----------------------------------------------------------------------------
# SECTION 2: Escape Sequences
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 2: Escape Sequences")
print("=" * 60)

# \n — newline: moves to the next line
print("Line 1\nLine 2\nLine 3")

# \t — tab: inserts a horizontal tab (useful for columns)
print("Name:\tAlice")
print("Age:\t30")
print("City:\tNew York")

# \\ — literal backslash
print("Windows path: C:\\Users\\Alice\\Documents")

# \' — literal single quote inside single-quoted string
print('It\'s a beautiful day!')

# \" — literal double quote inside double-quoted string
print("She said \"hello\" to me.")

# Combining multiple escape sequences
print("Item:\tApple\nPrice:\t$1.50\nQty:\t3")

# Raw strings — the r prefix disables escape processing
# Useful for file paths (Windows) and regular expressions
raw_path = r"C:\Users\Alice\new_folder\test.py"
print(raw_path)      # C:\Users\Alice\new_folder\test.py  — \n not treated as newline

normal_path = "C:\\Users\\Alice\\new_folder\\test.py"
print(normal_path)   # Same output but harder to read


# -----------------------------------------------------------------------------
# SECTION 3: The len() Function
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 3: The len() Function")
print("=" * 60)

# len() counts every character — letters, spaces, punctuation, digits
word = "Python"
print(f"'{word}' has {len(word)} characters")         # 6

sentence = "Hello, World!"
print(f"'{sentence}' has {len(sentence)} characters") # 13

# Spaces count!
with_spaces = "hi there"
print(f"'{with_spaces}' has {len(with_spaces)} characters")  # 8

# Empty string has length 0
empty = ""
print(f"Empty string length: {len(empty)}")   # 0

# Triple-quoted strings include the newlines
multiline = """line1
line2"""
print(f"Multiline string length: {len(multiline)}")   # 11 (5 + 1 newline + 5)

# Practical: check if a password meets minimum length
password = "mysecret123"
min_length = 8
if len(password) >= min_length:
    print(f"Password length {len(password)} is acceptable.")
else:
    print(f"Password too short! Need at least {min_length} characters.")


# -----------------------------------------------------------------------------
# SECTION 4: Positive Indexing
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 4: Positive Indexing (left to right, starts at 0)")
print("=" * 60)

#   String:   P   y   t   h   o   n
#   Index:    0   1   2   3   4   5

word = "Python"

print(f"word[0] = {word[0]}")   # P  — first character
print(f"word[1] = {word[1]}")   # y
print(f"word[2] = {word[2]}")   # t
print(f"word[3] = {word[3]}")   # h
print(f"word[4] = {word[4]}")   # o
print(f"word[5] = {word[5]}")   # n  — last character (index = len - 1)

# First and last character of a name
first_name = "Leonardo"
print(f"First character: {first_name[0]}")                      # L
print(f"Last character by exact index: {first_name[7]}")        # o
print(f"Last character using len-1: {first_name[len(first_name) - 1]}")  # o

# Iterating over each character with its index
for i in range(len(word)):
    print(f"  Index {i}: '{word[i]}'")


# -----------------------------------------------------------------------------
# SECTION 5: Negative Indexing
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 5: Negative Indexing (right to left, starts at -1)")
print("=" * 60)

#   String:    P    y    t    h    o    n
#   Positive:  0    1    2    3    4    5
#   Negative: -6   -5   -4   -3   -2   -1

word = "Python"

print(f"word[-1] = {word[-1]}")   # n  — last character
print(f"word[-2] = {word[-2]}")   # o  — second to last
print(f"word[-3] = {word[-3]}")   # h
print(f"word[-4] = {word[-4]}")   # t
print(f"word[-5] = {word[-5]}")   # y
print(f"word[-6] = {word[-6]}")   # P  — same as word[0]

# The power of -1: get last character without knowing the length
names = ["Alice", "Bob", "Christopher", "Li"]
for name in names:
    print(f"  Last char of '{name}': {name[-1]}")

# Checking the last character — practical use cases
filename = "report_2024.pdf"
print(f"Last char of filename: {filename[-1]}")   # f
# You'd usually use .endswith() for this, but -1 is educational

# Negative index arithmetic
word = "Hello"
print(f"\nword[-1] same as word[{len(word) - 1}]: {word[-1] == word[len(word) - 1]}")  # True


# -----------------------------------------------------------------------------
# SECTION 6: Combining len() and Indexing
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 6: Combining len() and Indexing")
print("=" * 60)

# Find the middle character of a word
word = "Python"
mid_index = len(word) // 2
print(f"Word: {word}")
print(f"Length: {len(word)}")
print(f"Middle index: {mid_index}")
print(f"Middle character: {word[mid_index]}")   # t

# First, middle, and last character of any word
word = "programming"
first   = word[0]
middle  = word[len(word) // 2]
last    = word[-1]
print(f"\nWord: {word}")
print(f"  First:  '{first}'")
print(f"  Middle: '{middle}'")
print(f"  Last:   '{last}'")


# -----------------------------------------------------------------------------
# SECTION 7: Immutability
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 7: Immutability — Strings Cannot Be Changed In-Place")
print("=" * 60)

# Demonstrating immutability — attempting to change a character
word = "python"
print(f"Original word: {word}")
print(f"id of original: {id(word)}")   # memory address

# This would cause an error — uncomment to see:
# word[0] = "P"   # TypeError: 'str' object does not support item assignment

# To "change" a string: create a new one
new_word = "P" + word[1:]       # "P" + "ython" = "Python"
print(f"New word:       {new_word}")
print(f"id of new word: {id(new_word)}")   # different memory address
print(f"Original still: {word}")            # "python" — unchanged!

# Reassigning a variable does NOT change the original string object
greeting = "hello"
print(f"\nOriginal greeting: {greeting}")
greeting = "Hello"   # 'greeting' now points to a new string "Hello"
print(f"After reassignment: {greeting}")
# The string "hello" still exists in memory until garbage collected

# Why immutability matters: you can safely share strings
a = "shared text"
b = a               # both point to the same string
a = "different"     # a now points to new string; b is unchanged
print(f"\na = '{a}'")
print(f"b = '{b}'")   # still "shared text"


# -----------------------------------------------------------------------------
# SECTION 8: Hands-On Practice — Putting it All Together
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 8: Hands-On Practice")
print("=" * 60)

# Exercise A: Index into names
full_name = "Marie Curie"
print(f"Full name: {full_name}")
print(f"  First character: {full_name[0]}")
print(f"  Character at index 5: {full_name[5]}")
print(f"  Last character: {full_name[-1]}")
print(f"  Second to last: {full_name[-2]}")
print(f"  Length: {len(full_name)}")

# Exercise B: Find last character of several strings
strings_to_check = ["banana", "programming", "Python", "Hello!"]
print()
for s in strings_to_check:
    print(f"  Last char of '{s}' (length {len(s)}): '{s[-1]}'")

# Exercise C: Measure string lengths — notice what counts
test_strings = [
    "hello",
    "hello world",
    "hello\tworld",    # tab is one character
    "hello\nworld",    # newline is one character
    "",
    " ",
    "   ",
]
print()
for s in test_strings:
    print(f"  len({repr(s)}) = {len(s)}")

# Exercise D: Character at each position in a word
word = "index"
print(f"\nCharacter positions in '{word}':")
print(f"  {'Positive':>8}  {'Negative':>8}  {'Char':>4}")
print(f"  {'-'*8}  {'-'*8}  {'-'*4}")
for i in range(len(word)):
    pos_idx = i
    neg_idx = i - len(word)
    print(f"  {pos_idx:>8}  {neg_idx:>8}  {word[i]:>4}")


print()
print("Day 7 complete! Run day8_examples.py next.")
