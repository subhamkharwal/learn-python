"""
Chapter 14 - Day 37: lambda, map, filter, sorted, zip, enumerate
=================================================================
Topics: anonymous (lambda) functions, map(), filter(), sorted() with key=,
        zip() and enumerate() revisited.
"""

# ============================================================
# 1. WHAT IS A lambda?
# ============================================================
# A lambda is a tiny, one-line, ANONYMOUS function (it has no name).
#
#     lambda parameters: expression
#       ^^^^^ ^^^^^^^^^^  ^^^^^^^^^^
#       keyword  inputs   the single value it returns (no `return` word)
#
# These two definitions do EXACTLY the same thing:

def double_def(x):
    return x * 2

double_lambda = lambda x: x * 2     # assigned to a name just to demo it

print(f"def version    : {double_def(5)}")       # 10
print(f"lambda version : {double_lambda(5)}")     # 10

# A lambda with two parameters.
add = lambda a, b: a + b
print(f"lambda add     : {add(3, 4)}")            # 7


# ============================================================
# 2. WHEN TO USE (and NOT use) a lambda
# ============================================================
# USE a lambda when you need a small throwaway function to pass into
# another function (like sorted, map, filter) and naming it would be noise.
#
# DO NOT assign a lambda to a variable just to reuse it - if it needs a
# name, write a normal `def`. It is clearer and shows up in tracebacks.
#
#   # Discouraged:  square = lambda x: x * x
#   # Preferred:    def square(x): return x * x
#
# Lambdas can only hold ONE expression - no statements, no loops, no
# multi-line bodies. That limitation is intentional: keep them tiny.


# ============================================================
# 3. map() - apply a function to EVERY item
# ============================================================
# map(function, iterable) returns a lazy "map object". Wrap it in list()
# to see the results. It is the function-form of the "map" comprehension.

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))
print(f"\nmap squared    : {squared}")            # [1, 4, 9, 16, 25]

# Equivalent list comprehension (often the more readable choice):
squared_comp = [x * x for x in numbers]
print(f"comp squared   : {squared_comp}")         # [1, 4, 9, 16, 25]

# map can walk TWO iterables at once, pairing items up.
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"map pairwise   : {sums}")                 # [11, 22, 33]


# ============================================================
# 4. filter() - keep items where the function returns True
# ============================================================
# filter(function, iterable) keeps each item for which function(item)
# is truthy. It is the function-form of the "filter" comprehension.

all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda n: n % 2 == 0, all_nums))
print(f"\nfilter evens   : {evens}")              # [2, 4, 6, 8, 10]

# Equivalent comprehension:
evens_comp = [n for n in all_nums if n % 2 == 0]
print(f"comp evens     : {evens_comp}")           # [2, 4, 6, 8, 10]

# Filter out empty / falsy strings.
words = ["python", "", "rocks", "", "!"]
non_empty = list(filter(lambda w: w != "", words))
print(f"non-empty      : {non_empty}")            # ['python', 'rocks', '!']


# ============================================================
# 5. sorted() with key= - the real workhorse
# ============================================================
# sorted(iterable, key=function) sorts items. The `key` function is
# called on EACH item to decide what to sort BY (the item itself is
# what ends up in the result, not the key).

# Sort words by LENGTH instead of alphabetically.
words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda w: len(w))
print(f"\nby length      : {by_length}")          # ['fig', 'kiwi', 'apple', 'banana']

# Sort numbers by DISTANCE from 10.
nums = [3, 14, 8, 22, 11]
by_closeness = sorted(nums, key=lambda n: abs(n - 10))
print(f"closest to 10  : {by_closeness}")         # [11, 8, 14, 3, 22]

# reverse=True flips the order (largest / last first).
descending = sorted(nums, reverse=True)
print(f"descending     : {descending}")           # [22, 14, 11, 8, 3]


# ============================================================
# 6. HANDS-ON: sort a list of dicts by a value
# ============================================================
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 35},
]

# Sort by age (youngest first). The key pulls the 'age' out of each dict.
by_age = sorted(people, key=lambda person: person["age"])
print("\nSorted by age (youngest first):")
for p in by_age:
    print(f"  {p['name']:6} -> {p['age']}")

# Sort by name alphabetically.
by_name = sorted(people, key=lambda person: person["name"])
print("Sorted by name:")
for p in by_name:
    print(f"  {p['name']:6} -> {p['age']}")


# ============================================================
# 7. zip() revisited - pair up multiple iterables
# ============================================================
# zip(a, b, ...) walks the iterables together, producing tuples.
# It stops at the SHORTEST iterable.

names = ["Alice", "Bob", "Carol"]
ages = [30, 25, 35]

paired = list(zip(names, ages))
print(f"\nzipped         : {paired}")
# [('Alice', 30), ('Bob', 25), ('Carol', 35)]

# A classic use: build a dict from two parallel lists.
people_dict = dict(zip(names, ages))
print(f"zip -> dict    : {people_dict}")
# {'Alice': 30, 'Bob': 25, 'Carol': 35}

# Loop over both lists at the same time.
print("Pairing names and ages:")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")


# ============================================================
# 8. enumerate() revisited - get index AND item
# ============================================================
# enumerate(iterable, start=0) gives (index, item) pairs so you do not
# need a manual counter.

print("\nUsing enumerate:")
for index, name in enumerate(names):
    print(f"  {index}: {name}")

# start=1 makes a human-friendly 1-based list.
print("Numbered list:")
for rank, name in enumerate(names, start=1):
    print(f"  {rank}. {name}")
