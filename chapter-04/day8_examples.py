# =============================================================================
# Chapter 04 — Strings In-Depth
# Day 8: Slicing, Concatenation, Repetition, and Membership Testing
# =============================================================================
# Run this file: python day8_examples.py
# =============================================================================


# -----------------------------------------------------------------------------
# SECTION 1: Slicing Basics — [start:stop]
# -----------------------------------------------------------------------------

print("=" * 60)
print("SECTION 1: Slicing Basics — [start:stop]")
print("=" * 60)

#   String:   P   y   t   h   o   n
#   Index:    0   1   2   3   4   5
#
# Key rule: stop index is EXCLUSIVE (the character at stop is NOT included)
#
#   [0:3]  grabs indices 0, 1, 2  →  "Pyt"   (stops before index 3)
#   [2:5]  grabs indices 2, 3, 4  →  "tho"   (stops before index 5)

word = "Python"

print(f"word         = '{word}'")
print(f"word[0:3]    = '{word[0:3]}'")     # Pyt
print(f"word[2:5]    = '{word[2:5]}'")     # tho
print(f"word[1:4]    = '{word[1:4]}'")     # yth
print(f"word[0:6]    = '{word[0:6]}'")     # Python (all 6 chars)
print(f"word[0:100]  = '{word[0:100]}'")   # Python (no error — stops at end)

# Visualizing the "stop is exclusive" fence:
#
#   "Python"[0:3]
#   ┌───┬───┬───║───┬───┬───┐
#   │ P │ y │ t ║ h │ o │ n │
#   └───┴───┴───║───┴───┴───┘
#     0   1   2 ║ 3   4   5
#               ↑ fence at 3 — 'h' NOT included
#
print()
print("The 'fence' mental model:")
print(f"  word[0:3] starts before index 0, stops at fence before index 3: '{word[0:3]}'")
print(f"  word[3:6] starts before index 3, stops at fence before index 6: '{word[3:6]}'")


# -----------------------------------------------------------------------------
# SECTION 2: Omitting start or stop
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 2: Omitting start or stop")
print("=" * 60)

word = "Python"

# Omit start → defaults to 0 (beginning)
print(f"word[:3]   = '{word[:3]}'")    # Pyt   (from start, up to but not including 3)
print(f"word[:1]   = '{word[:1]}'")    # P     (just the first character)
print(f"word[:4]   = '{word[:4]}'")    # Pyth

# Omit stop → defaults to len(word) (go all the way to the end)
print(f"word[3:]   = '{word[3:]}'")    # hon   (from index 3 to end)
print(f"word[1:]   = '{word[1:]}'")    # ython (skip first character)
print(f"word[5:]   = '{word[5:]}'")    # n     (just the last character)

# Omit both → full copy of the string
print(f"word[:]    = '{word[:]}'")     # Python

# Practical: extract file extension manually (last 4 characters)
filename = "photo_2024.jpg"
extension = filename[-4:]    # .jpg
print(f"\nFile: '{filename}' → extension: '{extension}'")

# Practical: remove the extension (everything except last 4 chars)
base_name = filename[:-4]    # photo_2024
print(f"Base name: '{base_name}'")


# -----------------------------------------------------------------------------
# SECTION 3: Slicing with negative indices
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 3: Slicing with Negative Indices")
print("=" * 60)

word = "Python"
#   Positive:  0    1    2    3    4    5
#   Negative: -6   -5   -4   -3   -2   -1

print(f"word[-3:]    = '{word[-3:]}'")      # hon   (last 3 characters)
print(f"word[:-3]    = '{word[:-3]}'")      # Pyt   (all except last 3)
print(f"word[-4:-1]  = '{word[-4:-1]}'")    # tho
print(f"word[-5:-2]  = '{word[-5:-2]}'")    # yth

# Pattern: last N characters
sentence = "Hello, World!"
n = 6
print(f"\nLast {n} chars of '{sentence}': '{sentence[-n:]}'")   # orld!

# Pattern: everything except first and last character (strip outer chars)
word = "Python"
inner = word[1:-1]
print(f"Inner chars of '{word}': '{inner}'")   # ytho


# -----------------------------------------------------------------------------
# SECTION 4: Slicing with a step — [start:stop:step]
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 4: Slicing with a Step")
print("=" * 60)

#   Default step is 1 (advance one character at a time).
#   step=2 means "take a character, skip one, take a character, skip one..."

word = "Python"

print(f"word        = '{word}'")
print(f"word[::1]   = '{word[::1]}'")    # Python  (every character)
print(f"word[::2]   = '{word[::2]}'")    # Pto     (indices 0, 2, 4)
print(f"word[1::2]  = '{word[1::2]}'")   # yhn     (indices 1, 3, 5)
print(f"word[::3]   = '{word[::3]}'")    # Ph      (indices 0, 3)

# Visualized:
#   P   y   t   h   o   n
#   0   1   2   3   4   5
#
#   [::2] → takes index 0(P), skips 1(y), takes 2(t), skips 3(h), takes 4(o), skips 5(n)
#          → "Pto"

# Longer string example
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"\nalphabet       = '{alphabet}'")
print(f"alphabet[::2]  = '{alphabet[::2]}'")   # every other letter: acegikmoqsuwy
print(f"alphabet[::5]  = '{alphabet[::5]}'")   # every 5th: afkpuz
print(f"alphabet[1::3] = '{alphabet[1::3]}'")  # starting at b, every 3rd: behknqtwz


# -----------------------------------------------------------------------------
# SECTION 5: Reversing a string with [::-1]
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 5: Reversing a String with [::-1]")
print("=" * 60)

# A step of -1 means "go backwards, one character at a time"
# When step is negative, default start = end, default stop = beginning

word = "Python"
reversed_word = word[::-1]
print(f"'{word}' reversed = '{reversed_word}'")   # nohtyP

# More examples
examples = ["Hello", "racecar", "abcde", "12345", "a"]
for s in examples:
    print(f"  '{s}' reversed = '{s[::-1]}'")

# Palindrome check using [::-1]
words_to_test = ["racecar", "hello", "level", "python", "madam", "noon"]
print()
print("Palindrome check:")
for w in words_to_test:
    is_palindrome = (w == w[::-1])
    print(f"  '{w}' → {is_palindrome}")

# Step of -2: every other character, backwards
word = "Python"
print(f"\n'{word}'[::-2] = '{word[::-2]}'")   # nhy  (backwards, every 2nd)


# -----------------------------------------------------------------------------
# SECTION 6: Extracting Substrings — Practical Patterns
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 6: Extracting Substrings — Practical Patterns")
print("=" * 60)

# Pattern 1: Extract year, month, day from an ISO date string
date_str = "2024-06-18"
year  = date_str[0:4]    # "2024"
month = date_str[5:7]    # "06"
day   = date_str[8:10]   # "18"
print(f"Date: {date_str}  →  year={year}, month={month}, day={day}")

# Pattern 2: Get domain from a URL (simplified)
url = "https://www.example.com"
domain = url[8:]    # "www.example.com"  (skip "https://")
print(f"URL: {url}  →  domain: '{domain}'")

# Pattern 3: Extract initials from a full name
full_name = "Albert Einstein"
first_initial = full_name[0]             # "A"
# Find the space, then take the char after it
# "Albert Einstein": A(0)l(1)b(2)e(3)r(4)t(5) (6)E(7)...  → space is at index 6
space_idx = 6                            # hardcoded here; in real code use .find()
last_initial = full_name[space_idx + 1]  # "E"  (index 7)
print(f"Name: {full_name}  →  initials: {first_initial}.{last_initial}.")

# Pattern 4: Take first N words preview of a long text
long_text = "The quick brown fox jumps over the lazy dog near the river bank"
preview = long_text[:30] + "..."
print(f"Preview: '{preview}'")


# -----------------------------------------------------------------------------
# SECTION 7: String Concatenation with +
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 7: String Concatenation with +")
print("=" * 60)

# Basic concatenation
first = "Hello"
second = "World"
result = first + ", " + second + "!"
print(result)   # Hello, World!

# Building a greeting
first_name = "Jane"
last_name = "Doe"
full_name = first_name + " " + last_name     # space must be explicit
print(f"Full name: {full_name}")

# Using += to build a string incrementally
message = "Good"
message += " morning"
message += ", Alice!"
print(message)   # Good morning, Alice!

# WARNING: + does NOT automatically add spaces
a = "Hello"
b = "World"
print(a + b)         # HelloWorld  (no space)
print(a + " " + b)   # Hello World (space added manually)

# Concatenation only works with strings — mixing types raises TypeError
# Uncomment to see:
# age = 25
# print("I am " + age + " years old.")   # TypeError!

# Fix: convert to string first
age = 25
print("I am " + str(age) + " years old.")   # or use f-string: f"I am {age} years old."

# Performance note: for building strings in a loop, join() is better
print()
print("join() vs += concatenation:")
words = ["one", "two", "three", "four", "five"]
# Slow for large lists (creates a new string object each iteration):
result_slow = ""
for w in words:
    result_slow += w + " "
print(f"  += result:   '{result_slow.rstrip()}'")

# Fast (builds one string at the end):
result_fast = " ".join(words)
print(f"  join result: '{result_fast}'")
# Both produce the same output but join() is more efficient for large data


# -----------------------------------------------------------------------------
# SECTION 8: String Repetition with *
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 8: String Repetition with *")
print("=" * 60)

print("ha" * 3)           # hahaha
print("-" * 30)           # ------------------------------
print("Python! " * 3)    # Python! Python! Python!
print("ab" * 5)           # ababababab

# Practical: create a text banner
title = " WELCOME TO PYTHON "
width = len(title) + 4
print("*" * width)
print("* " + title + " *")
print("*" * width)

# Practical: create a simple table separator
col_width = 12
print("-" * col_width + "+" + "-" * col_width + "+" + "-" * col_width)
print(f"{'Name':<{col_width}}|{'Age':<{col_width}}|{'City':<{col_width}}")
print("-" * col_width + "+" + "-" * col_width + "+" + "-" * col_width)
print(f"{'Alice':<{col_width}}|{'30':<{col_width}}|{'New York':<{col_width}}")
print(f"{'Bob':<{col_width}}|{'25':<{col_width}}|{'London':<{col_width}}")


# -----------------------------------------------------------------------------
# SECTION 9: Membership Testing — in and not in
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 9: Membership Testing — in and not in")
print("=" * 60)

text = "Hello, World!"

# 'in' returns True if the substring is found anywhere
print(f"'World' in text    → {'World' in text}")     # True
print(f"'world' in text    → {'world' in text}")     # False (case-sensitive!)
print(f"'Hello' in text    → {'Hello' in text}")     # True
print(f"'xyz'   in text    → {'xyz' in text}")       # False
print(f"'!'     in text    → {'!' in text}")         # True
print(f"','     in text    → {',' in text}")         # True
print(f"''      in text    → {'' in text}")          # True (empty string is always "in")

# 'not in' — the inverse
print()
print(f"'xyz' not in text  → {'xyz' not in text}")   # True
print(f"'World' not in text → {'World' not in text}") # False

# COMMON MISTAKE: case sensitivity
print()
user_query = "Python"
document = "I love python programming."
print(f"Search '{user_query}' in document: {'Python' in document}")           # False — capital P
print(f"Case-insensitive: {user_query.lower() in document.lower()}")          # True — both lowered

# Practical: check for forbidden words
forbidden_words = ["spam", "scam", "fake"]
email_body = "This is a legitimate offer, not scam content."
contains_forbidden = any(word in email_body.lower() for word in forbidden_words)
print(f"\nEmail contains forbidden word: {contains_forbidden}")   # True (found 'scam')

# Practical: check if a string is a valid identifier (simple check)
identifier = "my_variable"
has_space = " " in identifier
has_digit_start = identifier[0].isdigit()
print(f"\n'{identifier}' has space: {has_space}")         # False
print(f"'{identifier}' starts with digit: {has_digit_start}")  # False


# -----------------------------------------------------------------------------
# SECTION 10: Hands-On — Complete Practice Problems
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 10: Hands-On Practice")
print("=" * 60)

# --- Problem 1: Reverse a string with slicing ---
print("Problem 1: Reverse strings")
strings = ["hello", "Python", "racecar", "12345"]
for s in strings:
    print(f"  '{s}' reversed → '{s[::-1]}'")

# --- Problem 2: Extract substrings ---
print()
print("Problem 2: Extract substrings")
phrase = "The quick brown fox jumps over the lazy dog"
print(f"Original: '{phrase}'")
print(f"  First word:    '{phrase[:3]}'")            # The
print(f"  Last 3 chars:  '{phrase[-3:]}'")           # dog
print(f"  Words 4-8:     '{phrase[4:9]}'")           # quick
print(f"  Every 2nd:     '{phrase[::2]}'")           # alternating chars

# --- Problem 3: Build an acronym from a phrase ---
print()
print("Problem 3: Build acronym")
org_name = "National Aeronautics and Space Administration"
# Split on spaces, take first character of each word
words = org_name.split()
acronym = "".join(word[0].upper() for word in words if word[0].isupper())
print(f"'{org_name}'")
print(f"Acronym: {acronym}")   # NASA (skips 'and' since it's lowercase)

# Simpler version — all words
acronym_all = "".join(word[0].upper() for word in words)
print(f"Acronym (all words): {acronym_all}")   # NAASA

# --- Problem 4: Check if a URL uses HTTPS ---
print()
print("Problem 4: Check URL security")
urls = [
    "https://www.google.com",
    "http://oldsite.com",
    "https://github.com",
    "ftp://files.example.com",
]
for url in urls:
    is_secure = "https" in url[:8]   # only check the prefix, not the full URL
    status = "SECURE" if is_secure else "NOT secure"
    print(f"  {url:35} → {status}")


print()
print("Day 8 complete! Run day9_examples.py next.")
