"""
Chapter 14 - Day 36: Comprehensions
===================================
Topics: list comprehensions (map + filter form), dict comprehensions,
        set comprehensions, conditional comprehensions (if-filter and
        ternary-in-expression), nested comprehensions.
"""

# ============================================================
# 1. THE PROBLEM: a for-loop that builds a list
# ============================================================
# A very common pattern: start with an empty list, loop over something,
# transform each item, and append the result.

numbers = [1, 2, 3, 4, 5]

squares_loop = []                 # 1) start empty
for n in numbers:                 # 2) loop
    squares_loop.append(n * n)    # 3) transform + append

print(f"Loop result   : {squares_loop}")   # [1, 4, 9, 16, 25]


# ============================================================
# 2. THE SAME THING AS A LIST COMPREHENSION
# ============================================================
# A comprehension packs "loop + transform + collect" into ONE expression.
#
#     [ n * n   for n in numbers ]
#       ^^^^^   ^^^^^^^^^^^^^^^^^
#       output      the loop
#
# Read it left-to-right: "give me n*n FOR each n IN numbers".

squares_comp = [n * n for n in numbers]
print(f"Comp result   : {squares_comp}")    # [1, 4, 9, 16, 25]
print(f"Same answer?  : {squares_loop == squares_comp}")   # True


# ============================================================
# 3. THE "MAP" FORM - transform every item
# ============================================================
# Just an output expression and a loop. No filtering.

names = ["alice", "bob", "carol"]
upper_names = [name.upper() for name in names]
print(f"\nUppercased    : {upper_names}")     # ['ALICE', 'BOB', 'CAROL']

lengths = [len(name) for name in names]
print(f"Name lengths  : {lengths}")           # [5, 3, 5]


# ============================================================
# 4. THE "FILTER" FORM - keep only some items (if at the END)
# ============================================================
# Add `if condition` AFTER the loop. Items where the condition is
# False are skipped entirely (they never reach the output).
#
#     [ n   for n in numbers   if n % 2 == 0 ]
#       ^                       ^^^^^^^^^^^^^^
#     output                     the filter
#
# This filter `if` decides WHETHER an item is included.

all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in all_numbers if n % 2 == 0]
print(f"\nEven numbers  : {evens}")           # [2, 4, 6, 8, 10]

odds = [n for n in all_numbers if n % 2 != 0]
print(f"Odd numbers   : {odds}")              # [1, 3, 5, 7, 9]


# ============================================================
# 5. MAP + FILTER TOGETHER
# ============================================================
# Square only the even numbers. Transform happens on the left,
# filter happens on the right.

even_squares = [n * n for n in all_numbers if n % 2 == 0]
print(f"\nSquares of evens: {even_squares}")  # [4, 16, 36, 64, 100]


# ============================================================
# 6. TERNARY INSIDE THE EXPRESSION (if-else on the LEFT)
# ============================================================
# This is DIFFERENT from the filter `if`. Here the if-else chooses
# WHICH VALUE to output for every item (nothing is skipped).
#
#     [ ("even" if n % 2 == 0 else "odd")   for n in numbers ]
#       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#       a value is chosen for EVERY item
#
# Rule of thumb:
#   * if-else BEFORE `for`  -> choose a value (keeps every item)
#   * plain if AFTER `for`  -> filter (drops some items)

labels = ["even" if n % 2 == 0 else "odd" for n in all_numbers]
print(f"\nLabels        : {labels}")
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']


# ============================================================
# 7. DICT COMPREHENSIONS
# ============================================================
# Same idea, but you produce key: value pairs inside { }.
#
#     { key_expr : value_expr   for item in iterable }

# Build a dict mapping each number to its square.
squares_dict = {n: n * n for n in range(1, 6)}
print(f"\nSquares dict  : {squares_dict}")
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Map each name to its length.
name_lengths = {name: len(name) for name in names}
print(f"Name lengths  : {name_lengths}")
# {'alice': 5, 'bob': 3, 'carol': 5}

# Swap keys and values of an existing dict.
prices = {"apple": 3, "banana": 1, "cherry": 5}
flipped = {price: fruit for fruit, price in prices.items()}
print(f"Flipped dict  : {flipped}")
# {3: 'apple', 1: 'banana', 5: 'cherry'}

# Dict comprehension with a filter: keep only cheap items.
cheap = {fruit: price for fruit, price in prices.items() if price < 5}
print(f"Cheap items   : {cheap}")             # {'apple': 3, 'banana': 1}


# ============================================================
# 8. SET COMPREHENSIONS
# ============================================================
# Same as a list comprehension but with { } and NO key:value.
# The result is a set, so duplicates are automatically removed.

words = ["hi", "hello", "hey", "hi", "yo", "hello"]
unique_lengths = {len(w) for w in words}
print(f"\nUnique lengths: {unique_lengths}")   # {2, 5, 3} (order may vary)

# Distinct first letters.
first_letters = {w[0] for w in words}
print(f"First letters : {first_letters}")      # {'h', 'y'} (order may vary)


# ============================================================
# 9. NESTED COMPREHENSIONS (briefly)
# ============================================================
# Two `for` clauses = a loop inside a loop. The LEFT-most `for`
# is the OUTER loop, just like reading nested for-loops top to bottom.

# Flatten a 2D grid (list of rows) into a single flat list.
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [value for row in grid for value in row]
print(f"\nFlattened grid: {flat}")            # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Equivalent nested for-loop (for comparison):
flat_loop = []
for row in grid:
    for value in row:
        flat_loop.append(value)
print(f"Same as loop? : {flat == flat_loop}")  # True

# Build a multiplication-style grid using a nested comprehension.
pairs = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print(f"Coordinate set: {pairs}")
# [(1, 1), (1, 2), (2, 1), (2, 2)]


# ============================================================
# 10. HANDS-ON: rewrite loops as comprehensions
# ============================================================

# (a) Rewrite a "double every number" loop.
data = [10, 20, 30]
doubled = [x * 2 for x in data]
print(f"\nDoubled       : {doubled}")          # [20, 40, 60]

# (b) Filter even numbers from a range.
evens_1_to_20 = [n for n in range(1, 21) if n % 2 == 0]
print(f"Evens 1..20   : {evens_1_to_20}")

# (c) Build a squared-numbers dict for 1..5.
squared_numbers = {n: n ** 2 for n in range(1, 6)}
print(f"Squared dict  : {squared_numbers}")
