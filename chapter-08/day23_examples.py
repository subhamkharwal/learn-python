"""
Chapter 08 - Day 23: Sets
=========================
Topics: uniqueness, creating sets, .add()/.remove()/.discard(),
        set operations (union, intersection, difference,
        symmetric difference), and choosing the right data structure.
"""

# ============================================================
# 1. CREATING SETS
# ============================================================
# A set is an UNORDERED collection of UNIQUE items. Use curly braces {}.
# Duplicates are automatically thrown away.

empty = set()                           # NOTE: {} makes an empty DICT, not a set!
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 2, 3, 3, 3}            # duplicates removed automatically

print("empty   :", empty)
print("fruits  :", fruits)
print("numbers :", numbers)             # {1, 2, 3}  -- only unique values

# Build a set from a list to instantly drop duplicates
raw = [1, 1, 2, 3, 3, 3, 4]
unique = set(raw)
print("unique  :", unique)              # {1, 2, 3, 4}


# ============================================================
# 2. SETS ARE UNORDERED AND UNINDEXED
# ============================================================
# Because items have no position, you CANNOT index a set.

print("\n--- No indexing ---")
try:
    print(fruits[0])                    # NOT allowed!
except TypeError as error:
    print("Cannot index a set:", error)

# You CAN still check membership and loop over it.
print("'apple' in fruits :", "apple" in fruits)   # True  (very fast!)
for fruit in fruits:
    print("  fruit:", fruit)


# ============================================================
# 3. ADDING and REMOVING items
# ============================================================

print("\n--- Add & remove ---")
colors = {"red", "green"}
colors.add("blue")                      # add one item
print("after add     :", colors)

colors.add("red")                       # adding a duplicate does nothing
print("add duplicate :", colors)

colors.remove("green")                  # remove - ERRORS if item missing
print("after remove  :", colors)

colors.discard("purple")                # discard - SAFE, no error if missing
print("after discard :", colors)        # unchanged, no crash


# ============================================================
# 4. SET OPERATIONS - the real superpower of sets
# ============================================================
# These mirror the math you may have seen in Venn diagrams.
#
#        A = {1, 2, 3, 4}        B = {3, 4, 5, 6}
#
#        union (A | B)        -> everything in either   {1,2,3,4,5,6}
#        intersection (A & B) -> only what's in BOTH    {3,4}
#        difference (A - B)   -> in A but NOT in B       {1,2}
#        symmetric (A ^ B)    -> in one but not both     {1,2,5,6}

print("\n--- Set operations ---")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A                  :", A)
print("B                  :", B)
print("union (A | B)      :", A | B)            # or A.union(B)
print("intersection (A&B) :", A & B)            # or A.intersection(B)
print("difference (A - B) :", A - B)            # or A.difference(B)
print("difference (B - A) :", B - A)
print("symmetric (A ^ B)  :", A ^ B)            # or A.symmetric_difference(B)

# Subset / superset checks
small = {1, 2}
print("small <= A (subset)?  :", small <= A)    # True
print("A >= small (superset)?:", A >= small)    # True


# ============================================================
# 5. CHOOSING THE RIGHT DATA STRUCTURE
# ============================================================
# A quick mental checklist:
#   LIST  -> ordered, changeable, allows duplicates        [1, 2, 2, 3]
#   TUPLE -> ordered, UNchangeable, allows duplicates       (1, 2, 2, 3)
#   DICT  -> key -> value lookups, keys are unique          {"a": 1}
#   SET   -> unordered, UNIQUE items, fast membership       {1, 2, 3}

print("\n--- Picking a structure ---")
print("Need order + duplicates + change? -> list")
print("Need a fixed record that never changes? -> tuple")
print("Need to look things up by a key? -> dict")
print("Need uniqueness or set math? -> set")


# ============================================================
# 6. HANDS-ON #1: REMOVE DUPLICATES FROM A LIST
# ============================================================
# Converting to a set and back is the simplest way to dedupe.

print("\n--- Remove duplicates ---")
visitors = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
print("with duplicates :", visitors)

unique_visitors = list(set(visitors))   # set drops duplicates; list() restores a list
print("unique (any order) :", unique_visitors)

# If you must KEEP the original order, use dict.fromkeys() instead:
unique_ordered = list(dict.fromkeys(visitors))
print("unique (ordered)   :", unique_ordered)

print("Total visits :", len(visitors))
print("Unique people:", len(set(visitors)))


# ============================================================
# 7. HANDS-ON #2: FIND COMMON ELEMENTS
# ============================================================
# Intersection answers "who/what is in BOTH groups?"

print("\n--- Find common elements ---")
class_a = {"Alice", "Bob", "Charlie", "Diana"}
class_b = {"Charlie", "Diana", "Eve", "Frank"}

both = class_a & class_b                # in both classes
only_a = class_a - class_b              # only in class A
either = class_a | class_b              # in at least one class

print("In both classes :", both)        # {'Charlie', 'Diana'}
print("Only in class A :", only_a)      # {'Alice', 'Bob'}
print("In either class :", either)
print("Total unique students :", len(either))


# ============================================================
# 8. HANDS-ON #3: SHARED HOBBIES
# ============================================================

print("\n--- Shared hobbies ---")
alice_hobbies = {"reading", "cycling", "cooking", "chess"}
bob_hobbies = {"chess", "gaming", "cooking", "running"}

shared = alice_hobbies & bob_hobbies
unique_to_alice = alice_hobbies - bob_hobbies

print("Shared hobbies         :", shared)
print("Unique to Alice        :", unique_to_alice)
print("Anything in common?    :", len(shared) > 0)

print("\nDay 23 complete! You now understand sets and how to choose a structure.")
