# Chapter 08: Data Structures

## Chapter Overview

Up to now your programs have juggled values one at a time — a single name, a single
number, a single boolean. But real programs deal with *collections*: a list of students,
a phonebook of contacts, the unique tags on a blog post, a fixed (x, y) coordinate.

A **data structure** is a container that holds many values and gives you tools to add,
remove, find, and organise them. Python ships with four built-in collection types, and
choosing the right one is one of the biggest skills that separates a beginner from a
confident programmer.

| Structure | Looks like | Ordered? | Changeable? | Duplicates? |
|-----------|-----------|----------|-------------|-------------|
| **List** | `[1, 2, 3]` | Yes | Yes | Yes |
| **Tuple** | `(1, 2, 3)` | Yes | **No** | Yes |
| **Dict** | `{"a": 1}` | Yes* | Yes | Keys unique |
| **Set** | `{1, 2, 3}` | **No** | Yes | **No** |

> *Dictionaries remember insertion order since Python 3.7, but you should not *rely* on
> position the way you do with a list — you look things up by key, not by index.

This chapter spans **4 days**:

| Day | Topics |
|-----|--------|
| Day 20 | Lists: indexing, slicing, methods, mutability |
| Day 21 | Tuples: immutability, packing/unpacking, when to use them |
| Day 22 | Dictionaries: key-value pairs, CRUD, looping |
| Day 23 | Sets: uniqueness, set operations, choosing the right structure |

---

## Day 20: Lists

### What Is a List?

A **list** is an ordered, changeable collection of items written inside square brackets
`[]`, with items separated by commas. It is the workhorse collection of Python — when in
doubt, you probably want a list.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Alice", 30, True, 3.14]   # a list can hold any mix of types
empty = []                           # a list can start empty
```

---

### Indexing — Grabbing One Item

Every item has a **position number** called its index. The catch that trips up *every*
beginner: **counting starts at 0, not 1.**

```
   fruits  =  [ "apple" , "banana" , "cherry" ]
   index         0          1          2
   negative     -3         -2         -1     ◄── negative counts from the end
```

```python
fruits[0]    # 'apple'   — the FIRST item
fruits[1]    # 'banana'
fruits[-1]   # 'cherry'  — the LAST item (handy when you don't know the length)
fruits[-2]   # 'banana'
```

> **Common Mistake: Off-by-one with index**
>
> ```python
> fruits = ["apple", "banana", "cherry"]
> print(fruits[3])    # IndexError: list index out of range
> ```
>
> A list of 3 items has indexes `0`, `1`, `2`. The highest valid index is always
> `len(list) - 1`. Index `3` does not exist.

---

### Slicing — Grabbing a Sub-list

Slicing pulls out a *range* of items using `list[start:stop:step]`.

```
   numbers = [10, 20, 30, 40, 50]
   index       0   1   2   3   4

   numbers[1:4]   →  [20, 30, 40]      start INCLUDED, stop EXCLUDED
   numbers[:3]    →  [10, 20, 30]      start defaults to 0
   numbers[2:]    →  [30, 40, 50]      stop defaults to the end
   numbers[::2]   →  [10, 30, 50]      step of 2 (every other item)
   numbers[::-1]  →  [50, 40, 30, 20, 10]   step of -1 reverses the list
```

The golden rule of slicing: **start is included, stop is excluded.** `numbers[1:4]` gives
you indexes 1, 2, and 3 — not 4.

---

### Mutability — Lists Can Change

Unlike a string, you can change a list *after* it is created. This property is called
**mutability**.

```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"     # change the item at index 1
print(colors)            # ['red', 'yellow', 'blue']
```

---

### The Essential List Methods

A **method** is a function attached to an object, called with a dot: `mylist.append(x)`.

| Method | What it does | Example | Result |
|--------|--------------|---------|--------|
| `.append(x)` | Add one item to the end | `[1,2].append(3)` | `[1, 2, 3]` |
| `.insert(i, x)` | Insert at position `i` | `[1,3].insert(1, 2)` | `[1, 2, 3]` |
| `.extend(other)` | Add each item from another list | `[1,2].extend([3,4])` | `[1, 2, 3, 4]` |
| `.remove(x)` | Remove first matching value | `[1,2,1].remove(1)` | `[2, 1]` |
| `.pop(i)` | Remove **and return** item at `i` (default last) | `[1,2,3].pop()` | returns `3` |
| `.sort()` | Sort in place | `[3,1,2].sort()` | `[1, 2, 3]` |
| `.reverse()` | Reverse in place | `[1,2,3].reverse()` | `[3, 2, 1]` |
| `len(list)` | Count items (built-in, not a method) | `len([1,2,3])` | `3` |
| `x in list` | Membership test | `2 in [1,2,3]` | `True` |

**append vs extend** is a classic confusion:

```python
a = [1, 2]
a.append([3, 4])    # [1, 2, [3, 4]]  — adds the list as ONE nested item
b = [1, 2]
b.extend([3, 4])    # [1, 2, 3, 4]    — adds each item separately
```

**sort() vs sorted()**: `.sort()` changes the list in place and returns `None`; `sorted()`
leaves the original alone and returns a brand-new sorted list.

```python
nums = [3, 1, 2]
nums.sort()            # nums is now [1, 2, 3]

original = [3, 1, 2]
new = sorted(original) # original stays [3, 1, 2]; new is [1, 2, 3]
```

> **Common Mistake: `x = mylist.sort()`**
>
> ```python
> nums = [3, 1, 2]
> nums = nums.sort()   # nums is now None! .sort() returns nothing
> ```
>
> `.sort()` sorts *in place* and returns `None`. If you want a new sorted list, use
> `sorted()`. If you want to sort the existing list, just call `nums.sort()` on its own line.

---

### Looping Over a List

```python
tasks = ["wake up", "code", "sleep"]

for task in tasks:               # each loop, 'task' is one item
    print(task)

for i, task in enumerate(tasks, start=1):   # need the position too?
    print(f"{i}. {task}")        # 1. wake up   2. code   3. sleep
```

---

### Hands-on Day 20: Shopping List Manager

```python
shopping_list = []

def add_item(item):
    if item in shopping_list:
        print(f"'{item}' is already on the list.")
    else:
        shopping_list.append(item)
        print(f"Added '{item}'.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}'.")
    else:
        print(f"'{item}' was not on the list.")

def view_list():
    if len(shopping_list) == 0:
        print("(the list is empty)")
        return
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")

add_item("milk")
add_item("bread")
add_item("milk")     # refused — already there
view_list()
remove_item("bread")
view_list()
```

Run the full version in `day20_examples.py`.

---

### Day 20 Mini Exercises

1. Create a list of your 5 favourite movies. Print the first, the last (using `-1`), and the middle one.
2. Start with `[5, 3, 8, 1, 9]`. Sort it ascending, then descending. Print both.
3. Given `nums = [1, 2, 3, 4, 5, 6, 7, 8]`, use slicing to print: the first 3, the last 3, and every other number.
4. Write a function `add_unique(my_list, item)` that appends `item` only if it is not already in the list.
5. **Bonus:** Given a list of numbers, print the second-largest value WITHOUT sorting the whole list (hint: track two variables as you loop).

---

## Day 21: Tuples

### What Is a Tuple?

A **tuple** is just like a list, with one giant difference: it is **immutable** — once
created, it can never be changed. Think of it as a *read-only list*. Tuples use
parentheses `()`.

```python
point = (3, 5)
rgb = (255, 128, 0)
record = ("U-100", "Alice", "alice@example.com")
```

Indexing and slicing work exactly like lists:

```python
point[0]      # 3
point[-1]     # 5
rgb[0:2]      # (255, 128)
```

---

### Immutability — The Whole Point of Tuples

```python
coords = (10, 20)
coords[0] = 99    # TypeError: 'tuple' object does not support item assignment
```

Why would you *want* a collection you can't change? Because immutability is a **safety
guarantee**. If you store a coordinate as a tuple, no buggy code anywhere can accidentally
lose its `y` value. Tuples can also be used as dictionary keys and set members (lists
cannot, because they can change).

---

### The Single-Element Tuple Gotcha

This is the single most surprising tuple rule. To make a tuple with **one** item, you
*must* add a trailing comma:

```python
not_a_tuple = (42)    # this is just the integer 42!
real_tuple  = (42,)   # THIS is a one-item tuple
```

It is actually the **comma**, not the parentheses, that creates a tuple:

```python
also_a_tuple = 1, 2, 3      # (1, 2, 3) — no parentheses needed at all
```

> **Common Mistake: Forgetting the trailing comma**
>
> ```python
> coords = (5)        # you THINK this is a tuple...
> print(type(coords)) # <class 'int'> — it's just the number 5!
>
> coords = (5,)       # add the comma to make a real 1-tuple
> ```

---

### Packing and Unpacking

**Packing** bundles values into a tuple. **Unpacking** spreads them back out.

```python
person = "Alice", 30, "Engineer"     # packing
name, age, job = person              # unpacking — count must match
```

Use `*` to grab "the rest" into a list:

```python
first, *rest = (1, 2, 3, 4, 5)
# first = 1,  rest = [2, 3, 4, 5]
```

---

### Swapping Variables — The Famous Python Trick

In most languages, swapping two variables needs a temporary third variable. In Python,
tuple unpacking does it in one elegant line:

```python
a, b = 100, 200
a, b = b, a          # the right side packs into (200, 100), then unpacks
print(a, b)          # 200 100
```

---

### When to Use a Tuple vs a List

```
Use a TUPLE when the data should NOT change:
   • coordinates (x, y)        • RGB colours (r, g, b)
   • a database record         • returning multiple values from a function

Use a LIST when the data WILL change:
   • a shopping list           • a queue of tasks
   • search results            • anything you'll append to or sort
```

Tuples have only **two** methods, because there is nothing to add or remove:

```python
votes = ("yes", "no", "yes", "yes")
votes.count("yes")    # 3
votes.index("no")     # 1  (position of first match)
```

---

### Hands-on Day 21: Coordinate System

```python
def make_point(x, y):
    return (x, y)

def distance_from_origin(point):
    x, y = point                       # unpack
    return (x ** 2 + y ** 2) ** 0.5    # Pythagoras

def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

home = make_point(0, 0)
shop = make_point(3, 4)
print(distance_from_origin(shop))   # 5.0
print(midpoint(home, shop))         # (1.5, 2.0)
```

Run the full version in `day21_examples.py`.

---

### Day 21 Mini Exercises

1. Create a tuple `rgb = (255, 100, 50)`. Unpack it into `red`, `green`, `blue` and print each.
2. Swap two variables `x = "left"` and `y = "right"` using tuple unpacking. Print before and after.
3. Make a single-element tuple containing only the number `7`. Print its `type` to prove it really is a tuple.
4. Write a function `min_max(numbers)` that returns BOTH the smallest and largest as a tuple, then unpack the result at the call site.
5. **Bonus:** Try to change an item in a tuple and wrap it in a `try/except TypeError` so your program prints a friendly message instead of crashing.

---

## Day 22: Dictionaries

### What Is a Dictionary?

A **dictionary** stores data as **key → value** pairs, written inside curly braces `{}`.
Instead of looking things up by position (like a list), you look them up by a meaningful
**key**. Think of a real dictionary: you look up a *word* (the key) to find its
*definition* (the value).

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "London",
}
```

```
   ┌─────────────── KEY ─────── VALUE ───┐
   │   "name"    →    "Alice"             │
   │   "age"     →    30                  │
   │   "city"    →    "London"            │
   └──────────────────────────────────────┘
```

Keys must be **unique** and **immutable** (strings, numbers, or tuples). Values can be
anything and can repeat.

---

### CRUD — Create, Read, Update, Delete

CRUD is the four things you do to almost any data store.

**Create / Update** — assigning to a key adds it if new, overwrites it if it exists:

```python
person["email"] = "alice@example.com"   # CREATE (new key)
person["age"] = 31                       # UPDATE (existing key)
person.update({"city": "Paris", "job": "Engineer"})   # update many at once
```

**Read** — square brackets, or the safer `.get()`:

```python
person["name"]               # 'Alice'
person["missing"]            # KeyError! crashes
person.get("missing")        # None — no crash
person.get("missing", "n/a") # 'n/a' — supply your own default
```

**Delete** — `.pop()` returns the value, `del` does not:

```python
removed = person.pop("job")  # removes 'job' and returns its value
del person["email"]          # removes 'email', returns nothing
```

> **Common Mistake: KeyError on missing keys**
>
> ```python
> scores = {"math": 90}
> print(scores["science"])   # KeyError: 'science'
> ```
>
> If a key *might* be missing, use `.get()`:
> ```python
> print(scores.get("science", 0))   # 0 — safe default, no crash
> ```

---

### `.keys()`, `.values()`, `.items()`

```python
person = {"name": "Alice", "age": 31}

person.keys()     # dict_keys(['name', 'age'])
person.values()   # dict_values(['Alice', 31])
person.items()    # dict_items([('name', 'Alice'), ('age', 31)])
```

Wrap them in `list(...)` if you want a real list, but most of the time you just loop over
them directly.

---

### Looping Over a Dictionary

```python
person = {"name": "Alice", "age": 31, "city": "Paris"}

for key in person:                 # looping a dict gives its KEYS
    print(key, "->", person[key])

for key, value in person.items():  # the BEST way — unpack each pair
    print(f"{key}: {value}")
```

The `in` operator checks **keys**, not values:

```python
"name" in person     # True
"Alice" in person    # False — 'Alice' is a value, not a key
```

---

### Hands-on Day 22 #1: Phonebook

```python
phonebook = {}

def add_contact(name, number):
    phonebook[name] = number

def find_contact(name):
    number = phonebook.get(name)
    print(f"{name}: {number}" if number else f"{name} not found")

add_contact("Alice", "555-1234")
find_contact("Alice")     # Alice: 555-1234
find_contact("Bob")       # Bob not found
```

### Hands-on Day 22 #2: Word Frequency Counter

The single most useful dictionary pattern — counting things with `.get(key, 0)`:

```python
sentence = "the cat sat on the mat the cat"
frequency = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)   # {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

most_common = max(frequency, key=frequency.get)
print(most_common)   # 'the'
```

Run the full versions in `day22_examples.py`.

---

### Day 22 Mini Exercises

1. Create a dictionary `prices` mapping `"apple" → 50`, `"banana" → 30`, `"cherry" → 80`. Print the price of a banana.
2. Add a new fruit, update an existing price, and delete one fruit. Print the dict after each step.
3. Loop over `prices` and print each line as `"apple costs 50"`.
4. Write a function that counts how many times each LETTER appears in a word (use `.get(letter, 0) + 1`).
5. **Bonus:** Given two dictionaries, write code that merges them into a third without changing either original (hint: `.update()` on a copy, or `{**a, **b}`).

---

## Day 23: Sets

### What Is a Set?

A **set** is an **unordered** collection of **unique** items. It uses curly braces `{}`,
like a dictionary, but holds plain values instead of key-value pairs. The headline
features: **no duplicates** and **lightning-fast membership tests**.

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 2, 3, 3, 3}      # becomes {1, 2, 3} — duplicates dropped
```

> **Common Mistake: `{}` is an empty dict, not an empty set**
>
> ```python
> empty = {}            # this is an empty DICTIONARY
> print(type(empty))    # <class 'dict'>
>
> empty = set()         # THIS is how you make an empty set
> ```

Because sets are unordered, you **cannot index** them — `myset[0]` raises a `TypeError`.
You can still loop over a set and test membership with `in`.

---

### Adding and Removing

```python
colors = {"red", "green"}
colors.add("blue")        # add one item
colors.add("red")         # adding a duplicate does nothing
colors.remove("green")    # removes — KeyError if missing
colors.discard("purple")  # safe remove — no error if missing
```

Use `.discard()` when you are not sure the item exists; use `.remove()` when you want a
loud error if it doesn't.

---

### Set Operations — Venn Diagram Math

This is where sets shine. Imagine two overlapping circles:

```
        A = {1, 2, 3, 4}            B = {3, 4, 5, 6}

        union          A | B   →  {1, 2, 3, 4, 5, 6}   (everything)
        intersection   A & B   →  {3, 4}               (in BOTH)
        difference     A - B   →  {1, 2}               (in A, not B)
        symmetric      A ^ B   →  {1, 2, 5, 6}         (in one, not both)
```

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B   # union           {1, 2, 3, 4, 5, 6}    or A.union(B)
A & B   # intersection    {3, 4}                or A.intersection(B)
A - B   # difference      {1, 2}                or A.difference(B)
A ^ B   # symmetric diff  {1, 2, 5, 6}          or A.symmetric_difference(B)
```

---

### Choosing the Right Data Structure

This decision comes up constantly. Here is the full comparison table for all four:

| Question | List | Tuple | Dict | Set |
|----------|------|-------|------|-----|
| Keeps order? | Yes | Yes | Yes* | **No** |
| Can change after creation? | Yes | **No** | Yes | Yes |
| Allows duplicates? | Yes | Yes | Keys: no | **No** |
| Access by position? | Yes `[0]` | Yes `[0]` | By key | **No** |
| Access by key? | No | No | Yes `["a"]` | No |
| Fast membership (`in`)? | Slow | Slow | Fast (keys) | **Fast** |
| Syntax | `[ ]` | `( )` | `{k: v}` | `{ }` |

A quick decision guide:

```
Need order + duplicates + ability to change?   →  LIST
Need a fixed record that must never change?     →  TUPLE
Need to look things up by a name/key?           →  DICT
Need uniqueness or set math (overlap, etc.)?    →  SET
```

---

### Hands-on Day 23 #1: Remove Duplicates From a List

```python
visitors = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

unique = list(set(visitors))         # fast, but order is NOT preserved
unique_ordered = list(dict.fromkeys(visitors))   # keeps first-seen order

print(len(visitors))        # 5 total visits
print(len(set(visitors)))   # 3 unique people
```

### Hands-on Day 23 #2: Find Common Elements

```python
class_a = {"Alice", "Bob", "Charlie", "Diana"}
class_b = {"Charlie", "Diana", "Eve"}

both   = class_a & class_b    # {'Charlie', 'Diana'}  — in both classes
only_a = class_a - class_b    # {'Alice', 'Bob'}      — only in class A
either = class_a | class_b    # everyone, once each
```

Run the full versions in `day23_examples.py`.

---

### Day 23 Mini Exercises

1. Turn the list `[1, 2, 2, 3, 3, 3, 4]` into a set, then back into a sorted list of unique values.
2. Given `a = {1, 2, 3, 4, 5}` and `b = {4, 5, 6, 7}`, print their union, intersection, difference, and symmetric difference.
3. Write a function `is_unique(my_list)` that returns `True` if a list has no duplicates (hint: compare `len(list)` and `len(set(list))`).
4. Two friends list their hobbies. Print the hobbies they share and the ones unique to each.
5. **Bonus:** Given a paragraph of text, count how many *distinct* words it contains.

---

## Quick Reference Card

```
LISTS  [ordered, changeable, duplicates OK]
  nums = [1, 2, 3]
  nums[0]            first item        nums[-1]   last item
  nums[1:3]          slice (stop excluded)
  nums.append(x)     add to end        nums.insert(i, x)  add at i
  nums.extend(other) add each item     nums.remove(x)     delete by value
  nums.pop(i)        remove & return   nums.sort()        sort in place
  sorted(nums)       NEW sorted list   len(nums)   x in nums

TUPLES  [ordered, IMMUTABLE, duplicates OK]
  point = (3, 5)               one_item = (7,)   ← trailing comma!
  a, b = b, a                  swap via unpacking
  first, *rest = (1, 2, 3)     extended unpacking
  t.count(x)   t.index(x)      the only two methods

DICTS  [key -> value, keys unique]
  d = {"name": "Alice"}
  d["name"]          read (KeyError if missing)
  d.get("x", 0)      safe read with default
  d["x"] = 1         create or update
  d.update({...})    merge
  d.pop("x")         remove & return       del d["x"]
  d.keys()  d.values()  d.items()
  for k, v in d.items(): ...

SETS  [UNORDERED, UNIQUE, fast membership]
  s = {1, 2, 3}      empty_set = set()   ← NOT {}
  s.add(x)   s.remove(x)   s.discard(x)  (discard = safe)
  A | B  union          A & B  intersection
  A - B  difference     A ^ B  symmetric difference

CHOOSING:  ordered+change -> list | fixed record -> tuple
           lookup by key -> dict  | uniqueness/math -> set
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 20–23 |
| `day20_examples.py` | Runnable code: lists, indexing, slicing, methods, shopping list manager |
| `day21_examples.py` | Runnable code: tuples, immutability, packing/unpacking, coordinate system |
| `day22_examples.py` | Runnable code: dictionaries, CRUD, phonebook, word frequency counter |
| `day23_examples.py` | Runnable code: sets, set operations, dedupe & common elements |
