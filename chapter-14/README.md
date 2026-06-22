# Chapter 14: Functional Programming

## Chapter Overview

So far you have written Python in a fairly "imperative" style: you tell the computer
*step by step* exactly what to do — create a list, loop over it, append things one at
a time. That works, but it can be wordy and repetitive.

**Functional programming** is a different mindset. Instead of describing every step, you
*describe the transformation* you want and let Python handle the looping. You treat
functions as values you can pass around, and you build powerful one-line tools out of
small reusable pieces.

In this chapter you will learn to:
- **Replace common loops** with crisp, readable comprehensions
- **Pass behaviour around** using `lambda`, `map()`, `filter()`, and `sorted(key=...)`
- **Wrap and extend functions** without touching their code, using decorators

None of this gives you new *powers* — anything here can be written with the loops and
functions you already know from Chapters 1–13. What it gives you is **clarity and
brevity**: the same job in less code, with intent that reads almost like English.

This chapter spans **3 days**:

| Day | Topics |
|-----|--------|
| Day 36 | List / dict / set comprehensions, conditional (filter & ternary) comprehensions, nested comprehensions |
| Day 37 | `lambda`, `map()`, `filter()`, `sorted(key=...)`, `zip()` and `enumerate()` revisited |
| Day 38 | Decorators (step by step), `functools.wraps`, decorators with arguments, `functools.reduce()` |

---

## Day 36: Comprehensions

### The Problem Comprehensions Solve

You have written this exact pattern dozens of times: start with an empty list, loop over
something, transform each item, and append the result.

```python
numbers = [1, 2, 3, 4, 5]

squares = []                 # 1) start empty
for n in numbers:            # 2) loop
    squares.append(n * n)    # 3) transform + append

print(squares)               # [1, 4, 9, 16, 25]
```

Three lines, three moving parts, and a mutable list you have to manage by hand. A
**list comprehension** packs all three steps into a single expression.

---

### From a For-Loop to a Comprehension

Here is the same transform, shown side by side so you can see exactly which piece moves
where:

```
   FOR-LOOP                              COMPREHENSION

   squares = []                          squares = [ n * n  for n in numbers ]
   for n in numbers:                                  ▲▲▲▲▲  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
       squares.append( n * n )                          │          │
                          │                          OUTPUT       THE LOOP
                          └──────────────────────────┘  (what you   (where the
                          the transform moves up front    collect)   values come from)
```

Read it left to right, almost like English:

> "Give me **`n * n`** **for** each **`n`** **in** `numbers`."

```python
squares = [n * n for n in numbers]
print(squares)               # [1, 4, 9, 16, 25]
```

The result is a brand-new list. There is no `append`, no empty list to set up, and the
whole intent fits on one line.

---

### The Three Comprehension Types

The square brackets `[ ]` build a **list**. Swap the brackets (and add a `key: value`
for dicts) and the same idea builds a dict or a set.

| You write | You get | Shape |
|-----------|---------|-------|
| `[expr for x in it]` | `list` | `[ ... ]` |
| `{key: val for x in it}` | `dict` | `{ k: v, ... }` |
| `{expr for x in it}` | `set` | `{ ... }` (no `key:`, duplicates removed) |

**Dict comprehension** — produce `key: value` pairs:

```python
# Map each number to its square.
squares_dict = {n: n * n for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Swap an existing dict's keys and values.
prices = {"apple": 3, "banana": 1, "cherry": 5}
flipped = {price: fruit for fruit, price in prices.items()}
# {3: 'apple', 1: 'banana', 5: 'cherry'}
```

**Set comprehension** — same as a list, but with `{ }` and no `key:`. Because the result
is a set, duplicates vanish automatically:

```python
words = ["hi", "hello", "hey", "hi", "yo", "hello"]
unique_lengths = {len(w) for w in words}   # {2, 3, 5}  (order may vary)
first_letters  = {w[0] for w in words}     # {'h', 'y'} (order may vary)
```

---

### Conditional Comprehensions — Two Different `if`s

This is the part beginners trip over most, so look carefully. There are **two completely
different** ways an `if` can appear in a comprehension, and they do opposite things.

#### 1. The filter `if` — comes AFTER the loop, DROPS items

```
[ n   for n in numbers   if n % 2 == 0 ]
  ▲                       ▲▲▲▲▲▲▲▲▲▲▲▲▲▲
output                     THE FILTER
                    (decides WHETHER an item is included)
```

Items where the condition is `False` are skipped entirely — they never reach the output.

```python
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in all_numbers if n % 2 == 0]   # [2, 4, 6, 8, 10]
odds  = [n for n in all_numbers if n % 2 != 0]   # [1, 3, 5, 7, 9]
```

#### 2. The ternary `if-else` — comes BEFORE the loop, KEEPS every item

```
[ ("even" if n % 2 == 0 else "odd")   for n in numbers ]
  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
  a value is CHOSEN for every item (nothing is dropped)
```

Here the `if-else` chooses *which value* to output for each item. Every item still
appears in the result.

```python
labels = ["even" if n % 2 == 0 else "odd" for n in all_numbers]
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

**The rule of thumb:**

```
  if-else BEFORE the `for`  →  CHOOSE a value (keeps every item)
  plain if AFTER the `for`  →  FILTER          (drops some items)
```

You can even combine both — transform on the left, filter on the right:

```python
even_squares = [n * n for n in all_numbers if n % 2 == 0]
# [4, 16, 36, 64, 100]   (squared, but only the evens survived)
```

Dict comprehensions take a filter `if` too:

```python
cheap = {fruit: price for fruit, price in prices.items() if price < 5}
# {'apple': 3, 'banana': 1}
```

---

### Nested Comprehensions (Briefly)

Two `for` clauses in one comprehension is a loop inside a loop. The **left-most `for` is
the outer loop** — read it top to bottom exactly like nested for-loops.

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [value for row in grid for value in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

That single line is the same as:

```python
flat = []
for row in grid:           # outer loop  (left-most for)
    for value in row:      # inner loop  (next for)
        flat.append(value)
```

Nested comprehensions are handy, but they get hard to read fast. If you find yourself
nesting three levels deep, a plain loop is usually kinder to the next reader.

---

### Hands-on Day 36

**Rewrite a loop as a comprehension:**
```python
data = [10, 20, 30]
doubled = [x * 2 for x in data]
print(doubled)             # [20, 40, 60]
```

**Filter even numbers from a range:**
```python
evens_1_to_20 = [n for n in range(1, 21) if n % 2 == 0]
print(evens_1_to_20)       # [2, 4, 6, ..., 20]
```

**Build a squared-numbers dict:**
```python
squared_numbers = {n: n ** 2 for n in range(1, 6)}
print(squared_numbers)     # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### Day 36 Mini Exercises

1. Rewrite this loop as a list comprehension:
   ```python
   result = []
   for word in ["cat", "dog", "bird"]:
       result.append(word.upper())
   ```
2. Build a list of the cubes (`n ** 3`) of the numbers 1 through 10.
3. From `range(1, 31)`, build a list containing only the multiples of 3.
4. Build a dict mapping each word in `["apple", "banana", "kiwi"]` to its length.
5. Given `["a", 1, "b", 2, "c", 3]`, use a set comprehension to collect just the items
   that are strings. (Hint: `isinstance(x, str)` as a filter.)
6. Build a list of labels for `range(1, 11)` that says `"fizz"` for multiples of 3 and
   the number itself otherwise (use the ternary form).

> **Common Mistake: Confusing the filter `if` with the ternary `if-else`**
>
> ```python
> # WRONG — putting an if-else AFTER the for to try to filter
> [n for n in nums if n % 2 == 0 else 0]   # SyntaxError!
>
> # If you want to DROP items → filter `if` goes AFTER the for, no else:
> [n for n in nums if n % 2 == 0]
>
> # If you want to KEEP every item but CHANGE some → ternary BEFORE the for:
> [n if n % 2 == 0 else 0 for n in nums]
> ```
>
> Remember: a filter `if` never has an `else`. A ternary `if-else` always does, and it
> sits in front of the `for`.

---

## Day 37: lambda, map, filter, sorted, zip, enumerate

### What Is a `lambda`?

A **lambda** is a tiny, one-line, **anonymous** function — a function with no name.

```
lambda parameters: expression
  ▲▲▲▲▲ ▲▲▲▲▲▲▲▲▲▲  ▲▲▲▲▲▲▲▲▲▲
keyword   inputs    the single value it returns (there is no `return` word)
```

These two definitions do **exactly** the same thing:

```python
def double_def(x):
    return x * 2

double_lambda = lambda x: x * 2

print(double_def(5))      # 10
print(double_lambda(5))   # 10
```

A lambda automatically returns the value of its single expression — you never write
`return`. It can take several parameters:

```python
add = lambda a, b: a + b
print(add(3, 4))          # 7
```

---

### When to Use (and NOT use) a `lambda`

```
USE a lambda     → when you need a small throwaway function to PASS INTO
                   another function (sorted, map, filter) and naming it
                   would just be noise.

DON'T use one    → don't assign a lambda to a variable to reuse it. If it
                   needs a name, write a normal `def`. It is clearer and it
                   shows up properly in error tracebacks.
```

```python
# Discouraged — a named lambda:
square = lambda x: x * x

# Preferred — a real def:
def square(x):
    return x * x
```

A lambda can hold **only one expression** — no statements, no loops, no multi-line body.
That limit is intentional: it keeps lambdas tiny. The moment you want more, reach for
`def`.

---

### `map()` — Apply a Function to Every Item

`map(function, iterable)` calls `function` on each item. It returns a lazy "map object",
so wrap it in `list()` to see the results. It is the function-form of the "map"
comprehension.

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))   # [1, 4, 9, 16, 25]

# The equivalent comprehension — often the more readable choice:
squared = [x * x for x in numbers]              # [1, 4, 9, 16, 25]
```

`map` can even walk **two** iterables at once, pairing items up:

```python
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))      # [11, 22, 33]
```

---

### `filter()` — Keep Items Where the Function Returns True

`filter(function, iterable)` keeps each item for which `function(item)` is truthy. It is
the function-form of the "filter" comprehension.

```python
all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda n: n % 2 == 0, all_nums))   # [2, 4, 6, 8, 10]

# Equivalent comprehension:
evens = [n for n in all_nums if n % 2 == 0]            # [2, 4, 6, 8, 10]

# Drop empty / falsy strings:
words = ["python", "", "rocks", "", "!"]
non_empty = list(filter(lambda w: w != "", words))     # ['python', 'rocks', '!']
```

| Tool | Comprehension equivalent |
|------|--------------------------|
| `map(f, it)` | `[f(x) for x in it]` |
| `filter(f, it)` | `[x for x in it if f(x)]` |

For most everyday code the comprehension reads more clearly. `map`/`filter` shine when
you already *have* a named function to plug in (e.g. `map(str.upper, names)`).

---

### `sorted()` with `key=` — the Real Workhorse

`sorted(iterable, key=function)` sorts items. The `key` function is called on **each
item** to decide what to sort *by*. The original items end up in the result — the key is
only used for comparison, it does not replace the data.

```python
# Sort words by LENGTH instead of alphabetically.
words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda w: len(w))
# ['fig', 'kiwi', 'apple', 'banana']

# Sort numbers by DISTANCE from 10.
nums = [3, 14, 8, 22, 11]
by_closeness = sorted(nums, key=lambda n: abs(n - 10))
# [11, 8, 14, 3, 22]

# reverse=True flips the order.
descending = sorted(nums, reverse=True)        # [22, 14, 11, 8, 3]
```

---

### `zip()` and `enumerate()` Revisited

**`zip(a, b, ...)`** walks several iterables together, producing tuples. It stops at the
**shortest** iterable.

```python
names = ["Alice", "Bob", "Carol"]
ages  = [30, 25, 35]

paired = list(zip(names, ages))
# [('Alice', 30), ('Bob', 25), ('Carol', 35)]

# A classic use — build a dict from two parallel lists:
people_dict = dict(zip(names, ages))
# {'Alice': 30, 'Bob': 25, 'Carol': 35}

# Loop over both at once:
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

**`enumerate(iterable, start=0)`** gives `(index, item)` pairs so you never need a manual
counter:

```python
for index, name in enumerate(names):
    print(f"{index}: {name}")        # 0: Alice, 1: Bob, ...

# start=1 makes a human-friendly numbered list:
for rank, name in enumerate(names, start=1):
    print(f"{rank}. {name}")         # 1. Alice, 2. Bob, ...
```

---

### Hands-on Day 37

**Sort a list of dicts by a value:**
```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Carol", "age": 35},
]

# The key pulls the 'age' out of each dict.
by_age = sorted(people, key=lambda person: person["age"])
for p in by_age:
    print(f"{p['name']:6} -> {p['age']}")   # Bob, Alice, Carol (youngest first)

# Sort alphabetically by name instead:
by_name = sorted(people, key=lambda person: person["name"])
```

**Filter with a lambda:**
```python
all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, all_nums))   # [2, 4, 6, 8, 10]
```

---

### Day 37 Mini Exercises

1. Use `map` and a lambda to turn `[1, 2, 3, 4]` into `[1, 8, 27, 64]` (each item cubed).
2. Use `filter` and a lambda to keep only the words longer than 4 letters from
   `["sun", "moon", "galaxy", "star", "planet"]`.
3. Sort `["Banana", "apple", "Cherry"]` case-insensitively. (Hint: `key=lambda s: s.lower()`.)
4. Given `scores = [("Alice", 88), ("Bob", 95), ("Carol", 72)]`, sort it so the highest
   score comes first.
5. Use `zip` to combine `["x", "y", "z"]` and `[1, 2, 3]` into the dict
   `{'x': 1, 'y': 2, 'z': 3}`.
6. Use `enumerate(..., start=1)` to print a numbered shopping list from
   `["milk", "eggs", "bread"]`.

> **Common Mistake: Forgetting that `map`/`filter` are lazy**
>
> ```python
> result = map(lambda x: x * 2, [1, 2, 3])
> print(result)        # <map object at 0x...>  — NOT a list!
> print(list(result))  # [2, 4, 6]              — wrap it in list()
>
> # And a map/filter object is exhausted after ONE pass:
> doubled = map(lambda x: x * 2, [1, 2, 3])
> print(list(doubled))  # [2, 4, 6]
> print(list(doubled))  # []  — already used up!
> ```
>
> If you need to iterate more than once, convert to a list first — or just use a
> comprehension, which gives you a real list right away.

---

## Day 38: Decorators and functools.reduce

### Functions Are Objects (the Idea Behind Decorators)

Before decorators make sense, you need one key fact: in Python a function is just a
**value**. You can store it in a variable, pass it to another function, and return it
from a function — exactly like an `int` or a `str`.

```python
def shout(text):
    return text.upper() + "!"

yell = shout              # NOT calling it — just a second name for the same function
print(yell("hello"))      # HELLO!
```

A function can even **return another function**:

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet          # hand the inner function back

say_hi = make_greeter("Hi")
print(say_hi("Alice"))    # Hi, Alice!
```

---

### What Is a Decorator?

A **decorator is a function that wraps another function** to add behaviour *without*
changing the original function's code. This syntax:

```python
@my_decorator
def original():
    ...
```

is simply shorthand for:

```python
original = my_decorator(original)
```

The `@` line says "pass `original` through `my_decorator`, and let the result take over
the name `original`."

Picture the wrapping like a sandwich around the real function:

```
   call ───► ┌─────────────────────────────────┐
             │ wrapper: do something BEFORE     │
             └────────────────┬────────────────┘
                              │
                              ▼
             ┌─────────────────────────────────┐
             │   the ORIGINAL function runs     │
             └────────────────┬────────────────┘
                              │
                              ▼
             ┌─────────────────────────────────┐
             │ wrapper: do something AFTER      │
             └────────────────┬────────────────┘
                              │
                              ▼  return the result back to the caller
```

---

### Writing a Simple Decorator, Step by Step

A decorator takes a function (`func`) and returns a **new** function (`wrapper`) that
calls the original somewhere in the middle.

```python
def announce(func):                       # 1) takes the function to wrap
    def wrapper(*args, **kwargs):         # 2) accepts ANY arguments
        print(">> before the function runs")
        result = func(*args, **kwargs)    # 3) call the original
        print(">> after the function runs")
        return result                     # 4) pass its result back
    return wrapper                        # 5) return the wrapper

@announce
def add(a, b):
    print(f"computing {a} + {b}")
    return a + b

total = add(2, 3)
# >> before the function runs
# computing 2 + 3
# >> after the function runs
print(total)   # 5
```

Why `*args, **kwargs` in the wrapper? Because the wrapper must work for *any* function,
no matter how many arguments it takes. `*args, **kwargs` soaks up whatever is passed and
forwards it untouched to the real function. (You met `*args`/`**kwargs` back in
Chapter 7.)

---

### Why `functools.wraps`?

There is a subtle catch. Once you decorate `add`, the name `add` now points at `wrapper`.
So introspection — `__name__`, `__doc__`, `help()` — reports the *wrapper*, not your
original function. Its real identity is lost.

`functools.wraps` fixes this by copying the original's metadata onto the wrapper so the
decorated function still "looks like itself".

```python
import functools

def announce_bad(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def announce_good(func):
    @functools.wraps(func)               # copies name, docstring, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@announce_bad
def task_bad():
    """Does an important task."""

@announce_good
def task_good():
    """Does an important task."""

print(task_bad.__name__)   # wrapper                  ← lost!
print(task_bad.__doc__)    # None                     ← lost!
print(task_good.__name__)  # task_good                ← preserved
print(task_good.__doc__)   # Does an important task.  ← preserved
```

**Rule:** always put `@functools.wraps(func)` on your wrapper. It costs one line and
saves confusing debugging later.

---

### Hands-on Day 38

**`@timer` — measure how long a function takes:**
```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()        # record start time
        result = func(*args, **kwargs)     # run the real function
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.05)                       # pretend this is slow work
    return a + b

print(slow_add(10, 20))   # prints the timing, then 30
```

**`@validate_positive` — guard arguments before the function runs:**
```python
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError(
                    f"{func.__name__} requires positive numbers, got {value}"
                )
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def area_of_rectangle(width, height):
    return width * height

print(area_of_rectangle(3, 4))    # 12
area_of_rectangle(-2, 5)          # raises ValueError: ... got -2
```

This is the real power of decorators: the validation logic lives in *one* place and you
can reuse it on any function just by adding `@validate_positive` above it — no copy-paste,
no edits to the function body.

---

### Decorators With Arguments (Briefly)

What if you want to *configure* a decorator, e.g. "run this function 3 times"? You add
**one more layer**: a function that takes the configuration and *returns* a decorator. So
there are three nested functions.

```
repeat(times)        →  the configurable outer layer (takes the arg)
  decorator(func)    →  the actual decorator
    wrapper(...)     →  the replacement function
```

```python
def repeat(times):                           # 1) takes the config value
    def decorator(func):                     # 2) the real decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):        # 3) the wrapper
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def wave():
    print("wave!")

wave()    # prints "wave!" three times
```

Notice `@repeat(times=3)` has parentheses — you are *calling* `repeat` to get back the
real decorator, which then wraps `wave`.

---

### `functools.reduce()` — Boil a Sequence Down to One Value

Where `map` produces a list and `filter` shrinks a list, **`reduce` collapses an entire
sequence into a single value**. It applies a two-argument function cumulatively, carrying
the running result forward:

```
reduce(f, [a, b, c, d])  ==  f(f(f(a, b), c), d)
```

```python
import functools

numbers = [1, 2, 3, 4, 5]

product = functools.reduce(lambda running, n: running * n, numbers)
print(product)   # 120

# How it unfolds:
#   start: 1
#   1 * 2 = 2
#   2 * 3 = 6
#   6 * 4 = 24
#   24 * 5 = 120
```

You can pass a **starting value** as a third argument:

```python
total = functools.reduce(lambda running, n: running + n, numbers, 100)
print(total)     # 115   (100 + 1 + 2 + 3 + 4 + 5)
```

A note on taste: `reduce` is powerful but often *less* readable than a plain loop or a
built-in. For sums use `sum()`, for the largest use `max()` — reach for `reduce` only
when no built-in fits and a loop would be more verbose.

---

### Day 38 Mini Exercises

1. Write a decorator `@debug` that prints the function's name and arguments before calling
   it, then prints the return value. Use `functools.wraps`.
2. Write a decorator `@uppercase_result` that takes a function returning a string and
   makes it return that string upper-cased.
3. Apply your `@timer` from the hands-on to a function that sums `range(1, 1_000_000)`.
4. Use `functools.reduce` to concatenate `["a", "b", "c", "d"]` into the string `"abcd"`.
5. Use `functools.reduce` with a starting value of `1` to compute the factorial of 5
   (`reduce` over `range(1, 6)`).
6. **Bonus:** write `@repeat(times=n)` and decorate a function that prints `"hello"`.
   Confirm it prints `n` times.

> **Common Mistake: Forgetting to return the wrapper (or forgetting to return the result)**
>
> ```python
> # WRONG — the decorator returns None, so the decorated name becomes None
> def announce(func):
>     def wrapper(*args, **kwargs):
>         return func(*args, **kwargs)
>     # forgot:  return wrapper
>
> @announce
> def add(a, b): return a + b
>
> add(2, 3)   # TypeError: 'NoneType' object is not callable
> ```
>
> Two returns are easy to drop and easy to forget:
> 1. the **decorator** must `return wrapper`
> 2. the **wrapper** must `return func(...)`'s result if you want a value back
>
> If a decorated function suddenly returns `None` or raises "NoneType is not callable",
> check both `return` statements first.

---

## Quick Reference Card

```
COMPREHENSIONS
  list :  [ expr        for x in it  if cond ]
  dict :  { k: v        for x in it  if cond }
  set  :  { expr        for x in it  if cond }

  filter  if  (AFTER for)   → drops items        [x for x in it if cond]
  ternary if-else (BEFORE)  → chooses a value    [a if cond else b for x in it]
  nested  : left-most for is the OUTER loop       [v for row in grid for v in row]

LAMBDA (anonymous one-line function)
  lambda params: expression          # auto-returns the expression
  Use only for tiny throwaway functions passed into map/filter/sorted.

FUNCTIONAL BUILT-INS
  map(f, it)        → apply f to every item        (lazy → wrap in list())
  filter(f, it)     → keep items where f is truthy (lazy → wrap in list())
  sorted(it, key=f) → sort BY f(item); add reverse=True to flip
  zip(a, b, ...)    → pair iterables; stops at the shortest
  enumerate(it, start=0) → (index, item) pairs

DECORATORS
  @my_decorator            # same as:  func = my_decorator(func)
  def func(): ...

  def my_decorator(func):
      @functools.wraps(func)           # preserve __name__ / __doc__
      def wrapper(*args, **kwargs):
          # ... before ...
          result = func(*args, **kwargs)
          # ... after ...
          return result
      return wrapper                   # don't forget this!

  With arguments → 3 layers: config(args) → decorator(func) → wrapper(...)

functools.reduce
  reduce(f, [a, b, c])      ==  f(f(a, b), c)
  reduce(f, it, start)      ==  start fed in as the first running value
  Prefer sum()/max()/loops when they read more clearly.
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 36–38 |
| `day36_examples.py` | Runnable code: list/dict/set comprehensions, conditional & nested comprehensions |
| `day37_examples.py` | Runnable code: lambda, map, filter, sorted(key=), zip, enumerate |
| `day38_examples.py` | Runnable code: decorators step by step, functools.wraps, decorators with args, functools.reduce |
