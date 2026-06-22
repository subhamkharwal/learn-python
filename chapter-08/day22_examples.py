"""
Chapter 08 - Day 22: Dictionaries
=================================
Topics: key-value pairs, CRUD (create/read/update/delete),
        .keys(), .values(), .items(), .get(), .update(), .pop(),
        looping over a dictionary, and practical mini-projects.
"""

# ============================================================
# 1. CREATING DICTIONARIES
# ============================================================
# A dictionary stores data as KEY: VALUE pairs. Use curly braces {}.
# Keys must be unique; values can repeat. Keys are usually strings,
# but can be any immutable type (string, number, tuple).

empty = {}                              # an empty dictionary
person = {                              # a person described by named fields
    "name": "Alice",
    "age": 30,
    "city": "London",
}

print("empty  :", empty)
print("person :", person)

# You can also build one with dict()
scores = dict(math=90, science=85, art=70)
print("scores :", scores)


# ============================================================
# 2. READING VALUES - by key, and with .get()
# ============================================================
# Look up a value by putting its key in square brackets.

print("\n--- Reading values ---")
print("name :", person["name"])         # Alice
print("age  :", person["age"])          # 30

# Asking for a key that does not exist raises a KeyError.
# print(person["email"])   # <-- would crash: KeyError

# .get() is the SAFE way to read - it returns None (or a default) instead of crashing
print("email (get) :", person.get("email"))                  # None
print("email (get) :", person.get("email", "not provided"))  # not provided


# ============================================================
# 3. CREATE & UPDATE - dictionaries are MUTABLE
# ============================================================
# Assigning to a key either adds it (if new) or overwrites it (if it exists).

print("\n--- Create & update ---")
person["email"] = "alice@example.com"   # NEW key -> added
person["age"] = 31                      # EXISTING key -> overwritten
print("after edits :", person)

# .update() merges another dictionary in one go
person.update({"city": "Paris", "job": "Engineer"})
print("after update:", person)


# ============================================================
# 4. DELETE - .pop() and del
# ============================================================

print("\n--- Delete ---")
# .pop(key) removes the pair AND returns its value
removed = person.pop("job")
print("popped value :", removed)        # Engineer
print("after pop    :", person)

# del removes a pair but returns nothing
del person["email"]
print("after del    :", person)


# ============================================================
# 5. CHECKING FOR KEYS with 'in'
# ============================================================

print("\n--- Membership ---")
print("'name' in?  :", "name" in person)    # True  ('in' checks KEYS)
print("'email' in? :", "email" in person)   # False
print("length      :", len(person))         # number of pairs


# ============================================================
# 6. .keys(), .values(), .items()
# ============================================================
# These give you views you can loop over.

print("\n--- keys / values / items ---")
print("keys   :", list(person.keys()))      # ['name', 'age', 'city']
print("values :", list(person.values()))    # ['Alice', 31, 'Paris']
print("items  :", list(person.items()))     # [('name', 'Alice'), ...]


# ============================================================
# 7. LOOPING OVER A DICTIONARY
# ============================================================

print("\n--- Looping over keys ---")
for key in person:                      # looping a dict gives its KEYS
    print(f"  {key} -> {person[key]}")

print("\n--- Looping over items (best way) ---")
for key, value in person.items():       # unpack each pair into key, value
    print(f"  {key}: {value}")


# ============================================================
# 8. HANDS-ON #1: A PHONEBOOK
# ============================================================
# A dictionary is the perfect tool for "look something up by name".

print("\n--- Phonebook ---")

phonebook = {}                          # name -> number


def add_contact(name, number):
    """Adds or updates a contact."""
    phonebook[name] = number
    print(f"  Saved {name}: {number}")


def find_contact(name):
    """Looks up a contact safely with .get()."""
    number = phonebook.get(name)
    if number is None:
        print(f"  {name} is not in the phonebook.")
    else:
        print(f"  {name}: {number}")


def delete_contact(name):
    """Removes a contact if present."""
    if name in phonebook:
        phonebook.pop(name)
        print(f"  Deleted {name}.")
    else:
        print(f"  {name} is not in the phonebook.")


add_contact("Alice", "555-1234")
add_contact("Bob", "555-5678")
find_contact("Alice")
find_contact("Charlie")     # not found
delete_contact("Bob")
print("  Final phonebook:", phonebook)


# ============================================================
# 9. HANDS-ON #2: WORD FREQUENCY COUNTER
# ============================================================
# Counting how often each word appears is THE classic dictionary task.

print("\n--- Word Frequency Counter ---")

sentence = "the cat sat on the mat the cat is happy"
words = sentence.split()                # split into a list of words

frequency = {}
for word in words:
    # .get(word, 0) returns the current count, or 0 if we have not seen it yet
    frequency[word] = frequency.get(word, 0) + 1

print("Sentence :", sentence)
print("Counts   :")
for word, count in frequency.items():
    print(f"  {word:5} -> {count}")

# Find the most common word
most_common = max(frequency, key=frequency.get)
print(f"Most common word: '{most_common}' ({frequency[most_common]} times)")

print("\nDay 22 complete! You now understand dictionaries.")
