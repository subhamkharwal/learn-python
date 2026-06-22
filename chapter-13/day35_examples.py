"""
Chapter 13 - Day 35: Generators with yield
===========================================
Topics: generator functions and the `yield` keyword (pause/resume), how a
        generator is just an iterator, generator expressions vs list
        comprehensions (memory), next() on generators, and when to reach for
        a generator (lazy + infinite sequences). Includes an infinite counter
        and a lazy line/word file reader.

Every infinite generator here is demonstrated SAFELY (with islice/break)
so the script always terminates.

Run me with:  python3 day35_examples.py
"""

import sys
import os
import tempfile
from itertools import islice


# ============================================================
# 1. YOUR FIRST GENERATOR FUNCTION
# ============================================================
# A function that uses `yield` instead of `return` is a GENERATOR function.
# It IS a complete iterator - no class, no StopIteration to write by hand.

print("=== 1. a simple generator function ===")

def count_up(limit):
    """Yield 1, 2, ..., up to and including `limit`."""
    n = 0
    while n < limit:
        n += 1
        yield n          # hand a value to the caller, then PAUSE here

for value in count_up(3):
    print(f"  count_up -> {value}")     # 1, 2, 3


# ============================================================
# 2. yield PAUSES and RESUMES (the magic)
# ============================================================
# Calling a generator function does NOT run its body. You get a generator
# object back. Each next() runs the body until the next `yield`, then freezes.

print("\n=== 2. yield pauses & resumes ===")

def chatty():
    print("  >> body starting (you only see this on the first next())")
    yield 1
    print("  >> resumed after first yield")
    yield 2
    print("  >> resumed after second yield")

g = chatty()                 # nothing printed yet - body has NOT run
print("  generator object created, body still frozen")
print(f"  first  next(): {next(g)}")   # runs up to 'yield 1'
print(f"  second next(): {next(g)}")   # resumes, runs up to 'yield 2'

# A third next() would run to the end and raise StopIteration:
try:
    next(g)
except StopIteration:
    print("  third next(): StopIteration - generator is finished")


# ============================================================
# 3. SAME COUNTER: class way vs generator way
# ============================================================
# Day 34 needed ~10 lines of class. A generator does it in 4. Same behaviour.

print("\n=== 3. generator vs iterator class (same result) ===")

class CountUpClass:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

def count_up_gen(limit):
    n = 0
    while n < limit:
        n += 1
        yield n

print(f"  class    -> {list(CountUpClass(4))}")    # [1, 2, 3, 4]
print(f"  generator-> {list(count_up_gen(4))}")    # [1, 2, 3, 4]


# ============================================================
# 4. GENERATOR EXPRESSION vs LIST COMPREHENSION
# ============================================================
# Square brackets [ ] -> a LIST (all values now, in memory).
# Round brackets  ( ) -> a GENERATOR (one value at a time, lazy).

print("\n=== 4. generator expression vs list comprehension ===")

squares_list = [x * x for x in range(5)]    # a real list
squares_gen = (x * x for x in range(5))     # a generator object

print(f"  list comp : {squares_list}  (type: {type(squares_list).__name__})")
print(f"  gen expr  : {squares_gen}  (type: {type(squares_gen).__name__})")
print(f"  drained   : {list(squares_gen)}")     # [0, 1, 4, 9, 16]


# ============================================================
# 5. THE MEMORY DIFFERENCE (the whole point)
# ============================================================
# A list of a million numbers really stores a million numbers.
# A generator stores only a tiny "recipe" no matter how big the range is.

print("\n=== 5. memory: list vs generator ===")

big_list = [x for x in range(1_000_000)]    # actually builds a million ints
big_gen = (x for x in range(1_000_000))     # just a recipe

print(f"  list  size: {sys.getsizeof(big_list):>10,} bytes")
print(f"  gen   size: {sys.getsizeof(big_gen):>10,} bytes  <- tiny!")


# ============================================================
# 6. GENERATORS ARE SINGLE-USE (no rewind)
# ============================================================

print("\n=== 6. generators are single-use ===")
gen = (x for x in range(3))
print(f"  first  pass: {list(gen)}")    # [0, 1, 2]
print(f"  second pass: {list(gen)}")    # []  - already exhausted


# ============================================================
# 7. HANDS-ON: an INFINITE counter generator (demonstrated safely)
# ============================================================
# `while True` makes this run forever - so we only ever take a few values
# using itertools.islice, which keeps the program terminating.

print("\n=== 7. infinite counter (taken safely with islice) ===")

def counter(start=0, step=1):
    """Infinite generator: start, start+step, start+2*step, ..."""
    n = start
    while True:
        yield n
        n += step

print(f"  first 5 of counter(0, 10): {list(islice(counter(0, 10), 5))}")
print(f"  first 4 of counter(100, -1): {list(islice(counter(100, -1), 4))}")

# We can also pull values one by one with next():
g = counter(0, 5)
print(f"  next/next/next: {next(g)}, {next(g)}, {next(g)}")   # 0, 5, 10


# ============================================================
# 8. INFINITE generator with a for-loop + break
# ============================================================
# Another safe way to consume an infinite generator: stop it ourselves.

print("\n=== 8. infinite evens, stopped with break ===")

def even_numbers():
    """Infinite: 0, 2, 4, 6, ..."""
    n = 0
    while True:
        yield n
        n += 2

for value in even_numbers():
    if value > 10:
        break                 # OUR exit condition - prevents an infinite loop
    print(f"  even -> {value}")   # 0 2 4 6 8 10


# ============================================================
# 9. HANDS-ON: lazy file readers (constant memory)
# ============================================================
# A generator reads ONE line at a time, so memory stays flat even for a
# 10 GB file. We create a small temp file here just to demonstrate.

print("\n=== 9. lazy line & word readers ===")

def read_lines(path):
    """Yield one stripped line at a time."""
    with open(path) as f:
        for line in f:            # the file object itself yields lines lazily
            yield line.rstrip("\n")

def read_words(path):
    """Yield one word at a time across the whole file."""
    with open(path) as f:
        for line in f:
            for word in line.split():
                yield word

# Build a tiny temporary file to read from:
tmp_path = os.path.join(tempfile.gettempdir(), "ch13_demo.txt")
with open(tmp_path, "w") as f:
    f.write("hello generators\n")
    f.write("lazy reading saves memory\n")
    f.write("ERROR something went wrong\n")

print("  lines containing 'ERROR':")
for line in read_lines(tmp_path):
    if "ERROR" in line:
        print(f"    {line}")

print("  first 4 words in the file:")
for word in islice(read_words(tmp_path), 4):
    print(f"    {word}")

os.remove(tmp_path)   # clean up the temp file


# ============================================================
# 10. WHY IT MATTERS: sum without building a list
# ============================================================
# Passing a generator expression straight into sum() never builds a list.

print("\n=== 10. memory-friendly aggregation ===")
total = sum(x * x for x in range(1000))   # no 1000-element list created
print(f"  sum of squares 0..999 = {total}")

print("\nDone! Generators = lazy, memory-friendly iterators made easy.")
