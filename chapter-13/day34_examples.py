"""
Chapter 13 - Day 34: Iterable vs Iterator
==========================================
Topics: the difference between an iterable and an iterator, iter() and next(),
        StopIteration, how a `for` loop really works under the hood, and
        building your own iterator class with __iter__ and __next__.

Run me with:  python3 day34_examples.py
"""

# ============================================================
# 1. ITERABLE vs ITERATOR - the core distinction
# ============================================================
# An ITERABLE is something you CAN loop over (list, str, dict, range...).
# An ITERATOR is the "cursor" that actually walks through it and remembers
# where it is. You get an iterator FROM an iterable using iter().

print("=== 1. iterable vs iterator ===")

nums = [10, 20, 30]        # nums is an ITERABLE (a list)
cursor = iter(nums)        # iter() hands us an ITERATOR (the cursor)

print(f"type of nums   : {type(nums).__name__}")     # list
print(f"type of cursor : {type(cursor).__name__}")   # list_iterator


# ============================================================
# 2. DRIVING AN ITERATOR BY HAND WITH next()
# ============================================================
# next() pulls the next value out of the iterator and advances the cursor.

print("\n=== 2. next() one value at a time ===")
print(next(cursor))        # 10  (first value)
print(next(cursor))        # 20  (cursor advanced)
print(next(cursor))        # 30  (cursor advanced again)


# ============================================================
# 3. StopIteration - the official "we're done" signal
# ============================================================
# When the iterator runs out of values, next() raises StopIteration.
# This is NOT a bug - it is how Python says "the end".

print("\n=== 3. StopIteration when exhausted ===")
try:
    next(cursor)           # nothing left -> raises StopIteration
except StopIteration:
    print("StopIteration raised - the iterator is empty now")


# ============================================================
# 4. A list is ITERABLE but is NOT itself an ITERATOR
# ============================================================
# You cannot call next() directly on a list. You must turn it into an
# iterator first with iter().

print("\n=== 4. list is iterable, not an iterator ===")
try:
    next(nums)             # TypeError: 'list' object is not an iterator
except TypeError as e:
    print(f"next(nums) failed: {e}")

print(f"but next(iter(nums)) works: {next(iter(nums))}")   # 10


# ============================================================
# 5. AN ITERATOR IS SINGLE-USE (it does not rewind)
# ============================================================
# Once an iterator is drained, it stays empty. The original iterable can
# always give you a brand-new iterator though.

print("\n=== 5. iterators are single-use ===")
it = iter([1, 2, 3])
print(f"first pass : {list(it)}")    # [1, 2, 3]  - drains it
print(f"second pass: {list(it)}")    # []         - already exhausted!

# The iterable itself is reusable - ask for a fresh cursor:
data = [1, 2, 3]
print(f"fresh iterator: {list(iter(data))}")   # [1, 2, 3] again


# ============================================================
# 6. HOW A `for` LOOP REALLY WORKS (manual version)
# ============================================================
# This while-loop does EXACTLY what `for x in nums:` does internally.

print("\n=== 6. a for loop, written out by hand ===")
nums = [10, 20, 30]

_it = iter(nums)                 # 1. get an iterator from the iterable
while True:
    try:
        x = next(_it)            # 2. pull the next value
    except StopIteration:        # 3. when there's nothing left...
        break                    #    ...stop the loop quietly
    print(f"  got value: {x}")   # 4. run the loop body


# ============================================================
# 7. BUILDING YOUR OWN ITERATOR CLASS: CountUp
# ============================================================
# Any class with __iter__ and __next__ can be used in a for loop.
#   __iter__  returns the iterator (usually `self`)
#   __next__  returns the next value OR raises StopIteration

print("\n=== 7. custom iterator class: CountUp ===")

class CountUp:
    """An iterator that counts from 1 up to a given limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0          # remembers where we are

    def __iter__(self):
        return self               # an iterator returns itself

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration   # the official "done" signal
        self.current += 1
        return self.current


for n in CountUp(3):
    print(f"  CountUp -> {n}")     # 1, 2, 3


# ============================================================
# 8. HANDS-ON: the Countdown iterator
# ============================================================
# Counts DOWN from `start` to 1. Notice we reset `self.current` inside
# __iter__ so the object can be looped over more than once.

print("\n=== 8. Countdown iterator ===")

class Countdown:
    """Iterator that counts down from `start` to 1."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # reset the cursor each time iteration begins -> re-iterable
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("First launch:")
for number in Countdown(5):
    print(f"  {number}")          # 5 4 3 2 1
print("  Lift off!")

# Because we reset in __iter__, we can loop again with a fresh countdown:
print("Reusing the SAME object again:")
cd = Countdown(3)
print(f"  pass 1: {list(cd)}")    # [3, 2, 1]
print(f"  pass 2: {list(cd)}")    # [3, 2, 1]  - works again!


# ============================================================
# 9. PROOF: built-in types follow the same protocol
# ============================================================
# Strings, tuples, dicts, ranges - all iterable, all hand out iterators.

print("\n=== 9. built-ins use the same protocol ===")
for thing in ["abc", (1, 2), {"a": 1}, range(2)]:
    cursor = iter(thing)
    print(f"  iter({thing!r}) -> {type(cursor).__name__}, first = {next(cursor)}")

print("\nDone! You now know exactly how `for` loops work under the hood.")
