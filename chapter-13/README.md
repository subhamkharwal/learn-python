# Chapter 13: Iterators & Generators

## Chapter Overview

You have been using `for` loops since the very beginning of this course. Every time you wrote
`for item in something:`, Python was quietly performing a small piece of magic behind the
scenes. This chapter pulls back the curtain and shows you **exactly** how that magic works —
and then teaches you how to build your own.

Why does this matter for a beginner?

- It demystifies the `for` loop. After this chapter, `for x in y:` will never feel like a black box again.
- It unlocks **lazy** computation — producing values **one at a time, on demand**, instead of building giant lists in memory all at once.
- It lets you work with data that is **too big to fit in memory** (huge files, network streams) or even **infinite** (a counter that never stops).
- Generators are one of Python's most loved features. Real-world Python code is full of them.

We will build on what you already know from earlier chapters — especially **classes** (`__init__`,
`self`, dunder methods) from Chapter 12. If `__iter__` and `__next__` look intimidating, remember:
they are just **special methods** on a class, exactly like `__init__` and `__str__`.

This chapter spans **2 days**:

| Day | Topics |
|-----|--------|
| Day 34 | Iterable vs iterator, how a `for` loop *really* works (`iter()` + `next()` + `StopIteration`), building a custom iterator class with `__iter__` / `__next__`, the `Countdown` iterator |
| Day 35 | Generator functions with `yield`, how `yield` pauses/resumes, generator expressions vs list comprehensions (memory), `next()` on generators, when to reach for a generator (lazy + infinite sequences) |

---

## Day 34: Iterable vs Iterator — How `for` Loops Really Work

### The Two Words That Sound the Same (But Aren't)

These two words are the source of endless beginner confusion. Let's nail the difference **right now**:

```
ITERABLE  →  something you CAN loop over.
             It knows how to HAND OUT an iterator when asked.
             Examples: list, tuple, string, dict, set, range.

ITERATOR  →  the thing that actually DOES the looping.
             It remembers WHERE you are and knows how to give the NEXT value.
```

A helpful analogy — think of a **playlist** and a **play head**:

```
  ITERABLE = the playlist (the collection of songs)
  ITERATOR = the play-head / cursor (knows which song is "current"
             and how to advance to the next one)
```

A playlist by itself does not "play" — you need a cursor that walks through it. You can even
have **two** cursors on the same playlist at different positions. Same idea in Python: a list is
an iterable, but it produces a fresh **iterator** each time you start looping over it.

| | Iterable | Iterator |
|---|----------|----------|
| What it is | A container you can loop over | The active loop "cursor" |
| Key method | `__iter__()` (returns an iterator) | `__next__()` (returns the next value) + `__iter__()` (returns itself) |
| Remembers position? | No | **Yes** |
| Built-in to get one | `iter(obj)` | `next(obj)` |
| Examples | `list`, `str`, `dict`, `range` | the object returned by `iter([1,2,3])` |

---

### Turning an Iterable Into an Iterator: `iter()` and `next()`

Python gives you two built-in functions that let you do **by hand** what a `for` loop does
automatically:

- `iter(iterable)` → asks the iterable for a fresh iterator.
- `next(iterator)` → asks the iterator for the next value.

Let's drive a list manually, step by step:

```python
nums = [10, 20, 30]      # a list — this is an ITERABLE

it = iter(nums)          # ask for an ITERATOR (the cursor)
print(type(it))          # <class 'list_iterator'>

print(next(it))          # 10   ← first value
print(next(it))          # 20   ← cursor advanced
print(next(it))          # 30   ← cursor advanced again
print(next(it))          # 💥 StopIteration — nothing left!
```

That final `next(it)` raises a special exception called **`StopIteration`**. This is not an
error in your program — it is Python's official signal that means **"the cursor has reached
the end; there is nothing more to give."**

---

### How a `for` Loop *Really* Works (Under the Hood)

Here is the big reveal. This innocent-looking loop:

```python
for x in [10, 20, 30]:
    print(x)
```

...is actually **shorthand** for this longer code that Python writes for you:

```python
_it = iter([10, 20, 30])     # 1. get an iterator from the iterable
while True:
    try:
        x = next(_it)        # 2. grab the next value
    except StopIteration:    # 3. when there's nothing left...
        break                #    ...quietly stop the loop
    print(x)                 # 4. run the loop body with that value
```

A diagram of the whole cycle:

```
        ┌─────────────────────────────────────────────────────────┐
        │                                                         │
   for x in nums:                                                 │
        │                                                         │
        ▼                                                         │
   ┌──────────────┐    iter(nums)    ┌──────────────────┐         │
   │  ITERABLE    │ ───────────────► │    ITERATOR       │        │
   │  [10,20,30]  │                  │  (remembers pos)  │        │
   └──────────────┘                  └──────────────────┘         │
                                            │                     │
                              next(it) ─────┤                     │
                                            ▼                     │
                                    ┌───────────────┐             │
                                    │  value? ──────┼── yes ──► run loop body ─┘
                                    │               │
                                    │  StopIteration├── no  ──► break (loop ends)
                                    └───────────────┘
```

Read it as a sentence: **"A `for` loop calls `iter()` once to get a cursor, then calls `next()`
over and over to pull values, and stops the instant it sees `StopIteration`."**

Once you internalise this, everything about iterators clicks into place.

> **Common Mistake: Confusing the iterable with the iterator**
>
> ```python
> nums = [1, 2, 3]
> next(nums)         # 💥 TypeError: 'list' object is not an iterator
> ```
>
> A **list is iterable but is NOT itself an iterator** — you cannot call `next()` on it directly.
> You must first turn it into an iterator with `iter()`:
>
> ```python
> next(iter(nums))   # 1  ✅ — iter() gives you the cursor, next() advances it
> ```

---

### An Iterator Is Exhausted After One Pass

An iterator is **single-use**. Once it hands out its last value and raises `StopIteration`,
it is **empty forever** — it does not rewind.

```python
nums = [1, 2, 3]
it = iter(nums)

print(list(it))   # [1, 2, 3]   — drains the iterator completely
print(list(it))   # []          — already exhausted! nothing left
```

The original **iterable** (`nums`) is untouched — you can always call `iter(nums)` again to get
a **brand-new** cursor. But the **iterator** itself is one-and-done.

```
iterable  →  reusable   (ask for a fresh iterator any time)
iterator  →  disposable (good for exactly one pass, then it's empty)
```

---

### Building Your Own Iterator Class

Now the fun part: anything that follows the **iterator protocol** can be used in a `for` loop —
including your own classes! The protocol is just two special methods (remember dunder methods
from Chapter 12?):

| Method | Job |
|--------|-----|
| `__iter__(self)` | Returns the iterator object. For an iterator, this is usually just `return self`. |
| `__next__(self)` | Returns the next value, OR raises `StopIteration` when there is nothing left. |

That's the whole contract. If your object has both, Python's `for` loop will happily drive it.

```python
class CountUp:
    """An iterator that counts from 1 up to a given limit."""

    def __init__(self, limit):
        self.limit = limit
        self.current = 0          # remembers where we are

    def __iter__(self):
        return self               # an iterator returns itself

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration   # the official "we're done" signal
        self.current += 1
        return self.current


for n in CountUp(3):
    print(n)        # 1, then 2, then 3
```

Trace what happens when the `for` loop runs `CountUp(3)`:

```
  for n in CountUp(3):
        │
        ├─ iter(obj)   → __iter__ returns self
        ├─ next(obj)   → current 0→1, returns 1     loop body: print(1)
        ├─ next(obj)   → current 1→2, returns 2     loop body: print(2)
        ├─ next(obj)   → current 2→3, returns 3     loop body: print(3)
        └─ next(obj)   → 3 >= 3, raise StopIteration → loop ends
```

> **Common Mistake: Forgetting to raise `StopIteration`**
>
> ```python
> class BadCounter:
>     def __init__(self):
>         self.n = 0
>     def __iter__(self):
>         return self
>     def __next__(self):
>         self.n += 1
>         return self.n      # never stops! no StopIteration ever raised
>
> for x in BadCounter():     # 💥 infinite loop — your program hangs forever
>     print(x)
> ```
>
> Every `__next__` must have a path that raises `StopIteration`, otherwise the loop runs forever.

---

### Hands-on Day 34

**Drive an iterable manually with `iter()` and `next()`:**
```python
word = "Hi!"
cursor = iter(word)
print(next(cursor))   # H
print(next(cursor))   # i
print(next(cursor))   # !
# next(cursor)        # would raise StopIteration
```

**A `Countdown` iterator class** (counts DOWN from a number to 1):
```python
class Countdown:
    """Iterator that counts down from `start` to 1."""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # reset the cursor to the top each time iteration begins
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for number in Countdown(5):
    print(number)        # 5 4 3 2 1
print("Lift off!")
```

---

### Day 34 Mini Exercises

1. Use `iter()` and `next()` to print the first two items of the list `["a", "b", "c"]` **by hand** (no `for` loop). Then call `next()` a third and fourth time — what happens on the fourth call?
2. Write an iterator class `Evens(limit)` that yields the even numbers `2, 4, 6, ...` up to and including `limit`. Drive it with a `for` loop.
3. Modify the `Countdown` class so it counts down in steps of 2 (e.g. `Countdown(10)` → `10, 8, 6, 4, 2`).
4. Take a string, get an iterator from it with `iter()`, drain half of it with `next()`, then put it in a `for` loop. Does the `for` loop start from the beginning or from where you stopped? Explain why.

> **Common Mistake: Resetting state in the wrong place**
>
> If you initialise `self.current` in `__init__` instead of in `__iter__`, your iterator works
> **once** but cannot be looped over a second time (the cursor is already at the end). Putting the
> reset inside `__iter__` makes the object **re-iterable** — a fresh cursor each `for` loop.

---

## Day 35: Generators — Iterators Made Easy with `yield`

### The Problem Generators Solve

Writing a full iterator class (with `__init__`, `__iter__`, `__next__`, and manual
`StopIteration` handling) is a lot of ceremony for something simple. **Generators** are
Python's shortcut: they let you write an iterator using an ordinary-looking function.

The magic keyword is **`yield`**.

```python
def count_up(limit):
    n = 0
    while n < limit:
        n += 1
        yield n          # ← hand a value to the caller, then PAUSE here

for value in count_up(3):
    print(value)         # 1, 2, 3
```

That tiny function is a **complete, working iterator**. No class, no `StopIteration`, no
`self.current`. Python builds all of that for you automatically.

---

### `yield` vs `return`: How `yield` Pauses and Resumes

This is the heart of the chapter. A normal `return` **ends** a function. `yield` **pauses** it.

```
return  →  "Here is my final answer. I'm DONE — forget everything." (function exits)
yield   →  "Here is the next value. PAUSE me. Remember everything.
            Wake me up later and I'll keep going from right here."
```

When you call a generator function, the body **does not run yet**. You get back a **generator
object** (which is an iterator). Each time you call `next()` on it, the body runs **until it hits
a `yield`**, hands back that value, and **freezes in place** — local variables and all. The next
`next()` **resumes from exactly where it paused**.

```
   def count_up(limit):
       n = 0
       while n < limit:
           n += 1
   ┌──►    yield n        ◄── PAUSE point. Function freezes here.
   │   (all locals like `n` are remembered while frozen)
   │
   │   next() called again ──┐
   └────────────────────────┘ resume right after the yield, loop continues
```

A frame-by-frame trace of `count_up(2)`:

```
  gen = count_up(2)     # nothing runs yet — just creates the generator object

  next(gen)   → runs: n=0, loop check 0<2 ✅, n=1, yield 1   → returns 1, PAUSES
  next(gen)   → resumes after yield: loop check 1<2 ✅, n=2, yield 2 → returns 2, PAUSES
  next(gen)   → resumes: loop check 2<2 ❌, function ends    → raises StopIteration
```

The `for` loop does all those `next()` calls for you and stops cleanly on `StopIteration` — just
like with any other iterator (because a generator **is** an iterator).

> **Common Mistake: Expecting a generator to run when you call it**
>
> ```python
> def chatty():
>     print("starting!")
>     yield 1
>
> g = chatty()          # prints NOTHING — body has not run yet
> print("created")      # "created" prints first
> next(g)               # NOW "starting!" prints, then 1 is yielded
> ```
>
> Calling a generator function just builds the generator object. The code inside runs **lazily**,
> only as you pull values out with `next()` or a `for` loop.

---

### Generators vs Iterator Classes — Same Job, Less Code

Here is the **exact same** counter written both ways. The generator does in 4 lines what the
class needs ~10 lines to do:

```python
# THE CLASS WAY (Day 34 style)
class CountUp:
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

# THE GENERATOR WAY (Day 35 style) — identical behaviour!
def count_up(limit):
    n = 0
    while n < limit:
        n += 1
        yield n
```

Both work in `for n in ...:`. Reach for a **class** only when you need extra methods or complex
state; reach for a **generator** (the common case) for everything else.

---

### Generator Expressions vs List Comprehensions (the Memory Story)

You learned **list comprehensions** in an earlier chapter:

```python
squares_list = [x * x for x in range(5)]    # [0, 1, 4, 9, 16]  — square brackets
```

A **generator expression** looks almost identical but uses **round** brackets:

```python
squares_gen = (x * x for x in range(5))     # <generator object ...>  — parentheses
```

The difference is enormous, and it is all about **memory**:

```
LIST COMPREHENSION  [ ... ]
  → builds the ENTIRE list in memory RIGHT NOW.
  → all 5 (or 5 million) values exist at once.

       ┌───┬───┬───┬───┬────┐
       │ 0 │ 1 │ 4 │ 9 │ 16 │   ← all stored at the same time
       └───┴───┴───┴───┴────┘


GENERATOR EXPRESSION  ( ... )
  → builds NOTHING up front. Stores only a "recipe".
  → produces each value one at a time, ON DEMAND, then forgets it.

       (recipe) ──next──► 0   (forgotten) ──next──► 1   (forgotten) ──► ...
```

| | List comprehension `[ ]` | Generator expression `( )` |
|---|--------------------------|----------------------------|
| Memory used | Stores **all** items at once | Stores **one** item at a time |
| When values are computed | Immediately ("eager") | On demand ("lazy") |
| Can you re-loop over it? | Yes, as many times as you like | No — single use, then exhausted |
| Best for | Small data you need repeatedly | Huge/streaming data, one pass |
| Indexing `result[2]`? | Yes | No (not subscriptable) |

A quick way to *see* the memory difference with `sys.getsizeof`:

```python
import sys

big_list = [x for x in range(1_000_000)]    # ~8 MB — actually builds a million ints
big_gen  = (x for x in range(1_000_000))    # tiny — just the recipe

print(sys.getsizeof(big_list))   # a large number (megabytes)
print(sys.getsizeof(big_gen))    # ~200 bytes regardless of range size!
```

> **Common Mistake: Trying to reuse an exhausted generator**
>
> ```python
> gen = (x for x in range(3))
> print(list(gen))    # [0, 1, 2]
> print(list(gen))    # []  ← already drained! generators do NOT rewind
> print(sum(gen))     # 0  ← still empty
> ```
>
> If you need the data more than once, store it in a list. Otherwise, recreate the generator.

---

### Why Generators? Infinite and Lazy Sequences

Because a generator produces values one at a time and **never has to hold them all**, it can do
something a list simply cannot: represent an **infinite** sequence.

```python
def naturals():
    """An INFINITE generator: 1, 2, 3, 4, ... forever."""
    n = 1
    while True:          # never stops on its own!
        yield n
        n += 1
```

You obviously cannot do `list(naturals())` — that would run forever and crash. Instead you take
just what you need, safely:

```python
gen = naturals()
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3
```

The cleanest tool for grabbing the first *N* items of any iterator is **`itertools.islice`**:

```python
from itertools import islice

first_five = list(islice(naturals(), 5))   # [1, 2, 3, 4, 5] — safe, terminates
```

> **Common Mistake: Looping over an infinite generator with no exit**
>
> ```python
> for n in naturals():
>     print(n)        # 💥 runs forever — your terminal floods until you Ctrl-C
> ```
>
> Always bound an infinite generator with `break`, a counter, or `itertools.islice`.

---

### The Killer Use Case: Lazy File Reading

Imagine a 10 GB log file. Reading it all into a list of lines would blow up your memory:

```python
# DANGER: loads the ENTIRE file into RAM at once
lines = open("huge.log").readlines()    # could be gigabytes!
```

A generator reads **one line at a time**, using almost no memory no matter how big the file is.
In fact, a file object in Python **is already a lazy line generator**:

```python
def read_lines(path):
    """Yield one line at a time — memory stays flat even for a 10 GB file."""
    with open(path) as f:
        for line in f:          # the file object yields lines lazily
            yield line.rstrip("\n")

# Process a giant file using constant memory:
for line in read_lines("huge.log"):
    if "ERROR" in line:
        print(line)
```

At no point do all the lines exist in memory together — only the **current** line does. This is
the single most important practical reason generators exist.

---

### Hands-on Day 35

**Infinite counter generator (demonstrated safely):**
```python
from itertools import islice

def counter(start=0, step=1):
    """Infinite generator: start, start+step, start+2*step, ..."""
    n = start
    while True:
        yield n
        n += step

# Take only the first 5 so the program terminates:
print(list(islice(counter(0, 10), 5)))   # [0, 10, 20, 30, 40]
```

**Lazy line reader (works on any text file):**
```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")

for line in read_lines("notes.txt"):
    print(line)
```

**Generator expression for memory savings:**
```python
# Sum of squares 0..999 WITHOUT building a 1000-element list
total = sum(x * x for x in range(1000))   # generator expression, no list created
print(total)
```

---

### Day 35 Mini Exercises

1. Write a generator function `countdown(n)` that yields `n, n-1, ..., 1`. Loop over `countdown(5)`.
2. Convert this list comprehension into a generator expression and confirm the type: `[c.upper() for c in "hello"]`.
3. Write an **infinite** generator `fibonacci()` that yields `0, 1, 1, 2, 3, 5, 8, ...`. Use `itertools.islice` to print the first 10 numbers safely.
4. Write a generator `even_numbers()` that is infinite (`0, 2, 4, ...`). Use a `for` loop with a `break` to print evens until you reach a number greater than 20.
5. **Bonus:** Write a generator `read_words(path)` that opens a text file and yields one **word** at a time (split each line on spaces). Test it on a small file you create.

> **Common Mistake: Mixing up `[ ]` and `( )`**
>
> ```python
> result = [x for x in range(3)]   # a LIST: [0, 1, 2]
> result = (x for x in range(3))   # a GENERATOR object, NOT a tuple!
> ```
>
> Round brackets in a comprehension make a **generator**, not a tuple. To force a tuple, write
> `tuple(x for x in range(3))`.

---

## Quick Reference Card

```
ITERABLE vs ITERATOR
  iterable  → can be looped over; gives an iterator via iter()
  iterator  → the cursor; gives next value via next(); raises StopIteration at end
  Rule of thumb: lists/strings/dicts are ITERABLE; iter() of them is an ITERATOR.

HOW A FOR LOOP WORKS (under the hood)
  _it = iter(iterable)          # 1. get the cursor
  while True:
      try:
          x = next(_it)         # 2. pull next value
      except StopIteration:     # 3. end signal
          break
      <loop body using x>       # 4. use the value

BUILDING A CUSTOM ITERATOR (a class)
  class MyIter:
      def __iter__(self):  return self            # iterator returns itself
      def __next__(self):
          if <done>: raise StopIteration          # MUST raise to stop
          return <next value>

GENERATOR FUNCTION (the easy way)
  def gen():
      yield value          # hands out a value AND pauses here
      yield another        # resumes here on the next next()
  # 'yield' pauses & remembers locals; 'return' ends for good.

GENERATOR EXPRESSION vs LIST COMPREHENSION
  [x for x in data]   → LIST: all values now, in memory, reusable
  (x for x in data)   → GENERATOR: one value at a time, lazy, single-use

DRIVING / TAMING GENERATORS
  next(gen)                       # pull one value
  for v in gen: ...               # pull all values, stop on StopIteration
  from itertools import islice
  list(islice(gen, 5))            # safely take first 5 from an infinite generator

WHEN TO USE A GENERATOR
  [ ] data is huge or streaming (read one piece at a time)
  [ ] sequence is infinite / lazy
  [ ] you only need to iterate ONCE
  [ ] you want low memory use
  Use a list instead when you need random access, length, or multiple passes.
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 34–35 |
| `day34_examples.py` | Runnable code: iter()/next(), how `for` works, custom iterator classes, `Countdown` |
| `day35_examples.py` | Runnable code: `yield`, generator vs class, generator expressions, infinite counter, lazy file reader |
