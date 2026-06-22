"""
Chapter 08 - Day 20: Lists
==========================
Topics: creating lists, indexing, slicing, list methods
        (.append, .insert, .remove, .pop, .sort, .reverse, .extend),
        len(), the 'in' operator, and mutability.
"""

# ============================================================
# 1. CREATING LISTS
# ============================================================
# A list is an ORDERED, CHANGEABLE collection. Use square brackets [].
# Items are separated by commas. A list can hold any type of value.

empty = []                              # an empty list
fruits = ["apple", "banana", "cherry"]  # a list of strings
numbers = [10, 20, 30, 40, 50]          # a list of integers
mixed = ["Alice", 30, True, 3.14]       # lists can mix types

print("empty   :", empty)
print("fruits  :", fruits)
print("numbers :", numbers)
print("mixed   :", mixed)

# You can also build a list from another iterable using list()
letters = list("hello")                 # ['h', 'e', 'l', 'l', 'o']
print("letters :", letters)


# ============================================================
# 2. INDEXING - getting a single item
# ============================================================
# Positions start at 0. The FIRST item is index 0, not 1.
#
#   fruits  =  ["apple", "banana", "cherry"]
#   index       0          1          2
#   negative   -3         -2         -1   <-- counts from the end

print("\n--- Indexing ---")
print("First fruit  :", fruits[0])      # apple
print("Second fruit :", fruits[1])      # banana
print("Last fruit   :", fruits[-1])     # cherry  (negative = from the end)
print("2nd from end :", fruits[-2])     # banana

# Asking for an index that does not exist raises an IndexError.
# print(fruits[99])   # <-- would crash: IndexError


# ============================================================
# 3. SLICING - getting a sub-list
# ============================================================
# Syntax:  list[start : stop : step]
#   - start is INCLUDED
#   - stop is EXCLUDED
#   - step is optional (how many to jump)

print("\n--- Slicing ---")
print("numbers       :", numbers)        # [10, 20, 30, 40, 50]
print("numbers[1:4]  :", numbers[1:4])   # [20, 30, 40]  (index 1,2,3)
print("numbers[:3]   :", numbers[:3])    # [10, 20, 30]  (start defaults to 0)
print("numbers[2:]   :", numbers[2:])    # [30, 40, 50]  (stop defaults to end)
print("numbers[::2]  :", numbers[::2])   # [10, 30, 50]  (every 2nd item)
print("numbers[::-1] :", numbers[::-1])  # [50, 40, 30, 20, 10]  (reversed!)


# ============================================================
# 4. MUTABILITY - lists can be CHANGED in place
# ============================================================
# Unlike strings, you can change an item by assigning to its index.

print("\n--- Mutability ---")
colors = ["red", "green", "blue"]
print("before :", colors)
colors[1] = "yellow"                     # change item at index 1
print("after  :", colors)                # ['red', 'yellow', 'blue']


# ============================================================
# 5. ADDING ITEMS: .append(), .insert(), .extend()
# ============================================================

print("\n--- Adding items ---")
shopping = ["milk", "eggs"]

# .append(x) - adds ONE item to the END
shopping.append("bread")
print("after append :", shopping)        # ['milk', 'eggs', 'bread']

# .insert(index, x) - adds an item at a specific position
shopping.insert(0, "butter")             # put 'butter' at the front
print("after insert :", shopping)        # ['butter', 'milk', 'eggs', 'bread']

# .extend(iterable) - adds EACH item from another list
shopping.extend(["jam", "tea"])
print("after extend :", shopping)        # ['butter', 'milk', 'eggs', 'bread', 'jam', 'tea']

# Careful: .append() adds the whole list as ONE item; .extend() unpacks it.
demo_append = [1, 2]
demo_append.append([3, 4])
print("append a list :", demo_append)    # [1, 2, [3, 4]]  <-- nested!

demo_extend = [1, 2]
demo_extend.extend([3, 4])
print("extend a list :", demo_extend)    # [1, 2, 3, 4]   <-- flattened


# ============================================================
# 6. REMOVING ITEMS: .remove() and .pop()
# ============================================================

print("\n--- Removing items ---")
animals = ["cat", "dog", "fish", "dog"]

# .remove(value) - removes the FIRST matching value
animals.remove("dog")
print("after remove('dog') :", animals)  # ['cat', 'fish', 'dog']

# .pop(index) - removes AND RETURNS the item at index (default: last)
last = animals.pop()                      # removes and returns 'dog'
print("popped item         :", last)      # dog
print("after pop()         :", animals)   # ['cat', 'fish']

first = animals.pop(0)                     # removes and returns index 0
print("popped index 0      :", first)      # cat
print("after pop(0)        :", animals)   # ['fish']


# ============================================================
# 7. SORTING and REVERSING: .sort(), .reverse(), sorted()
# ============================================================

print("\n--- Sorting & reversing ---")
scores = [42, 17, 99, 3, 56]
scores.sort()                             # sorts the list IN PLACE (changes it)
print("sorted ascending  :", scores)      # [3, 17, 42, 56, 99]

scores.sort(reverse=True)                 # sort largest first
print("sorted descending :", scores)      # [99, 56, 42, 17, 3]

scores.reverse()                          # flips the order in place
print("after reverse     :", scores)      # [3, 17, 42, 56, 99]

# sorted() returns a NEW sorted list and leaves the original untouched.
original = [5, 1, 3]
new_sorted = sorted(original)
print("original stays    :", original)    # [5, 1, 3]
print("new sorted list   :", new_sorted)  # [1, 3, 5]


# ============================================================
# 8. len() and the 'in' OPERATOR
# ============================================================

print("\n--- len() and 'in' ---")
inventory = ["sword", "shield", "potion"]
print("number of items :", len(inventory))         # 3
print("'shield' in?    :", "shield" in inventory)   # True
print("'bow' in?       :", "bow" in inventory)      # False
print("'bow' NOT in?   :", "bow" not in inventory)  # True


# ============================================================
# 9. LOOPING OVER A LIST
# ============================================================

print("\n--- Looping ---")
tasks = ["wake up", "code", "sleep"]
for task in tasks:
    print("  TODO:", task)

# Use enumerate() when you also need the index (the position number)
print("\n--- Looping with index ---")
for index, task in enumerate(tasks, start=1):
    print(f"  {index}. {task}")


# ============================================================
# 10. HANDS-ON: A SIMPLE SHOPPING LIST MANAGER
# ============================================================
# This pulls together append, remove, 'in', and len into one tiny program.

print("\n--- Shopping List Manager ---")

shopping_list = []   # start empty


def add_item(item):
    """Adds an item to the shopping list if it is not already there."""
    if item in shopping_list:
        print(f"  '{item}' is already on the list.")
    else:
        shopping_list.append(item)
        print(f"  Added '{item}'.")


def remove_item(item):
    """Removes an item from the list if present."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"  Removed '{item}'.")
    else:
        print(f"  '{item}' was not on the list.")


def view_list():
    """Prints the whole shopping list in a numbered format."""
    if len(shopping_list) == 0:
        print("  (the list is empty)")
        return
    print(f"  You have {len(shopping_list)} item(s):")
    for index, item in enumerate(shopping_list, start=1):
        print(f"    {index}. {item}")


# Simulate a user session
add_item("milk")
add_item("bread")
add_item("eggs")
add_item("milk")        # duplicate - will be refused
view_list()

remove_item("bread")
remove_item("coffee")   # not on the list
view_list()

print("\nDay 20 complete! You now understand lists.")
