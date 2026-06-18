# Python Zero to Hero — Complete Course Plan

> Designed for absolute beginners. Each chapter is broken into daily sessions (~45–60 min/day).
> No prior programming experience required.

---

## Course At a Glance

| Chapter | Title | Days | Cumulative Day |
|---------|-------|------|----------------|
| 01 | Getting Started with Python | 2 | Day 1–2 |
| 02 | Variables & Data Types | 2 | Day 3–4 |
| 03 | Operators & Expressions | 2 | Day 5–6 |
| 04 | Strings In-Depth | 4 | Day 7–10 |
| 05 | Control Flow | 2 | Day 11–12 |
| 06 | Loops | 3 | Day 13–15 |
| 07 | Functions | 4 | Day 16–19 |
| 08 | Data Structures | 4 | Day 20–23 |
| 09 | File I/O | 2 | Day 24–25 |
| 10 | Error Handling | 2 | Day 26–27 |
| 11 | Modules & Packages | 2 | Day 28–29 |
| 12 | Object-Oriented Programming | 4 | Day 30–33 |
| 13 | Iterators & Generators | 2 | Day 34–35 |
| 14 | Functional Programming | 3 | Day 36–38 |
| 15 | Capstone Project | 4 | Day 39–42 |

**Total: 42 days** (~8–9 weeks at 5 days/week with weekends off)

> **What changed from v1:** Chapter 04 (Strings) gained a day — Day 9 was split into Day 9a (formatting + transformation methods) and Day 9b (search methods + hands-on projects) after review. Chapter 07 (Functions) gained a day — Day 17 was split into Day 17 (`*args`/`**kwargs`) and Day 18 (scope + recursion) to reduce cognitive load. All subsequent day numbers shifted by +2.

---

## Detailed Daily Breakdown

---

### Chapter 01 — Getting Started with Python
> Goal: Have Python installed, understand what it is, and run your first program.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 1 | What is Python? Why Python? Where is it used? Installing Python + VS Code. The REPL (interactive shell). | Play in REPL: `print("Hello")`, math expressions |
| 2 | Writing your first `.py` script. Running scripts from terminal. Comments (`#`). `print()` deep dive. | Write `hello_world.py`, print multiple lines, use comments |

---

### Chapter 02 — Variables & Data Types
> Goal: Understand how Python stores and labels data.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 3 | What is a variable? Naming rules. Assigning values. `int`, `float`, `bool`, `None`. `type()`. | Declare 10 variables of different types, inspect with `type()` |
| 4 | `str` basics. Multiple assignment. Dynamic typing. Constants by convention. Type conversion (`int()`, `str()`, `float()`). | Convert user input to int, experiment with type mismatches |

---

### Chapter 03 — Operators & Expressions
> Goal: Do math, compare values, and combine conditions.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 5 | Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`). Operator precedence (PEMDAS). | Calculator script: area of circle, temperature converter |
| 6 | Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`). Logical operators (`and`, `or`, `not`). Assignment operators (`+=`, `-=`, etc.). | Write expressions, predict output before running |

---

### Chapter 04 — Strings In-Depth
> Goal: Master Python's most-used data type.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 7 | String creation (single, double, triple quotes). Indexing & negative indexing. `len()`. Immutability. Converting to/from strings (`str()`, `int()`, `float()`). | Index into names, find last character, print file path using escape sequences & raw strings |
| 8 | Slicing (`[start:stop:step]`). String concatenation & repetition. `in` / `not in`. | Reverse a string with slicing, extract substrings |
| 9a | f-strings (with format specifiers), `.format()`. Core transformation methods: `.upper()`, `.lower()`, `.title()`, `.strip()`, `.replace()`. | f-string price formatter (`Total: $114.00`), name formatter |
| 9b | Search methods: `.find()`, `.startswith()`, `.endswith()`, `.count()`. `split()`, `join()`. Method chaining. | Parse a CSV-like string manually, email domain extractor |

---

### Chapter 05 — Control Flow
> Goal: Make decisions in your code.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 11 | `if`, `elif`, `else`. Truthiness & falsy values. Nested conditions. | Grade classifier, positive/negative/zero checker |
| 12 | Ternary (conditional) expressions. `and`/`or`/`not` with truth tables. Short-circuit evaluation. `match` statement (Python 3.10+). | Refactor if/else to ternary, build a role-based menu with `match` |

---

### Chapter 06 — Loops
> Goal: Repeat actions without repeating code.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 13 | `for` loop. `range()` — start, stop, step. Looping over strings. Bonus: `enumerate()` and `zip()`. | Print multiplication table, sum of first N numbers |
| 14 | `while` loop. `break`, `continue`, `pass`. Infinite loops and how to avoid them. | Guessing game (break on correct answer), skip even numbers |
| 15 | Nested loops. `for`/`else` and `while`/`else`. Loop patterns (accumulator, counter, flag). | Print patterns (triangles, grids), inline prime checker using `for/else` |

---

### Chapter 07 — Functions
> Goal: Write reusable, organized code blocks.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 16 | `def` keyword. Parameters vs arguments. `return`. Calling functions. Void functions. | Write `greet()`, `add()`, `is_even()` functions |
| 17 | Default parameters. Keyword arguments. Multiple return values. Docstrings. | Build a flexible greeting function, swap two numbers |
| 18 | `*args` and `**kwargs`. Complete parameter order rule. | Sum any number of args, `describe_person(**info)` |
| 19 | Variable scope (local vs global). LEGB rule. `global` keyword. Recursion intro. | Scope debugging exercise, factorial with recursion |

---

### Chapter 08 — Data Structures
> Goal: Store and organize collections of data.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 20 | **Lists** — creation, indexing, slicing. `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`. | Shopping list manager (add, remove, view items) |
| 21 | **Tuples** — immutability, when to use tuples. Tuple packing/unpacking. | Coordinate system, swap variables using tuple unpacking |
| 22 | **Dictionaries** — key-value pairs, CRUD operations. `.keys()`, `.values()`, `.items()`. `.get()`, `.update()`. | Build a phonebook, word frequency counter |
| 23 | **Sets** — uniqueness, set operations (`union`, `intersection`, `difference`). Choosing the right structure. | Remove duplicates from list, find common elements between two lists |

---

### Chapter 09 — File I/O
> Goal: Read from and write to files on disk.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 24 | `open()`, file modes (`r`, `w`, `a`, `rb`). `.read()`, `.readline()`, `.readlines()`. `with` statement (context manager). | Read a text file, count lines and words |
| 25 | Writing & appending to files. Working with CSV using the `csv` module. `os.path` basics. | Write a log file, read/write a simple CSV of names and scores |

---

### Chapter 10 — Error Handling
> Goal: Write programs that don't crash unexpectedly.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 26 | What are exceptions? Common built-in exceptions. `try` / `except` / `else` / `finally`. Catching multiple exceptions. | Safe division function, handle invalid user input |
| 27 | `raise` statement. Creating custom exception classes. Best practices (don't silence errors). | Build a custom `ValidationError`, validate age input |

---

### Chapter 11 — Modules & Packages
> Goal: Use Python's ecosystem and organize your own code.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 28 | `import`, `from ... import`, `as` alias. Standard library tour: `math`, `random`, `datetime`, `os`, `sys`. `__name__ == "__main__"`. | Dice roller with `random`, date calculator with `datetime` |
| 29 | `pip` package manager. Virtual environments (`venv`). Installing third-party packages. Writing your own module. | Create a `utils.py` module, install and use `requests` |

---

### Chapter 12 — Object-Oriented Programming (OOP)
> Goal: Model real-world things as code objects.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 30 | What is OOP? Classes vs objects. `class` keyword. `__init__` method. Instance variables. `self`. | Create a `Dog` class with name, breed, and age |
| 31 | Instance methods. `__str__` and `__repr__`. Class variables vs instance variables. | Add `bark()` method, format Dog with `__str__` |
| 32 | Inheritance. `super()`. Method overriding. `isinstance()`, `issubclass()`. | Create `Animal` base class, `Dog` and `Cat` subclasses |
| 33 | Encapsulation (private `_` / `__`). Properties (`@property`, `@setter`). Intro to `@staticmethod` and `@classmethod`. | Add age validation with `@property` setter |

---

### Chapter 13 — Iterators & Generators
> Goal: Understand how Python's `for` loop really works under the hood.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 34 | Iterable vs iterator. `iter()` and `next()`. Building a custom iterator with `__iter__` and `__next__`. | Create a `Countdown` iterator class |
| 35 | Generator functions with `yield`. Generator expressions. `next()` on generators. When to use generators (memory efficiency). | Infinite counter generator, lazy file reader |

---

### Chapter 14 — Functional Programming
> Goal: Write clean, expressive Python using functional patterns.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 36 | List comprehensions. Dict comprehensions. Set comprehensions. Conditional comprehensions. | Rewrite loops as comprehensions, filter even numbers, build a squared-numbers dict |
| 37 | `lambda` functions. `map()`, `filter()`, `sorted()` with key. `zip()`, `enumerate()` revisited. | Sort a list of dicts by value, filter with lambda |
| 38 | Decorators — what they are, writing a simple decorator, `functools.wraps`. `functools.reduce()`. | Write a `@timer` decorator, a `@validate_positive` decorator |

---

### Chapter 15 — Capstone Project
> Goal: Build a complete CLI application that ties all concepts together.

**Project: Personal Task Manager (CLI)**
A command-line task manager that stores tasks in a JSON file with add, list, complete, and delete operations.

| Day | Topics | Hands-on |
|-----|--------|----------|
| 39 | Project setup, plan the architecture, define data model. File structure, `argparse` intro. | Scaffold project, define `Task` class, set up JSON persistence |
| 40 | Implement add, list, and save/load from JSON. | Working `add` and `list` commands with file persistence |
| 41 | Implement complete, delete commands. Error handling throughout. | Full CRUD working, graceful error messages |
| 42 | Polish: color output with `colorama`, input validation, final testing, write README. | Finished, documented, shareable project |

---

## How to Use This Course

1. **One session per day** — each day is ~45–60 minutes of focused learning + coding.
2. **Type the code yourself** — don't copy-paste. Muscle memory matters.
3. **Break things on purpose** — modify examples to see what happens when they fail.
4. **Each chapter has its own folder** — notes, examples, and exercises live there.

---

## Folder Structure

```
learn-python/
├── course-plan/
│   └── README.md              ← this file
├── chapter-01/                ← Day 1–2
│   ├── notes.md
│   ├── day1_examples.py
│   └── day2_examples.py
├── chapter-02/                ← Day 3–4
│   ├── notes.md
│   ├── day3_examples.py
│   └── day4_examples.py
├── chapter-03/                ← Day 5–6
│   ├── notes.md
│   ├── day5_examples.py
│   └── day6_examples.py
├── chapter-04/                ← Day 7–10 (Day 9 split into 9a/9b)
│   ├── notes.md
│   ├── day7_examples.py
│   ├── day8_examples.py
│   └── day9_examples.py
├── chapter-05/                ← Day 11–12
│   ├── notes.md
│   ├── day10_examples.py
│   └── day11_examples.py
├── chapter-06/                ← Day 13–15
│   ├── notes.md
│   ├── day12_examples.py
│   ├── day13_examples.py
│   └── day14_examples.py
├── chapter-07/                ← Day 16–19 (Day 17 split into 17/*args* + 18/scope)
│   ├── notes.md
│   ├── day15_examples.py
│   ├── day16_examples.py
│   └── day17_examples.py
└── chapter-08 to 15/          ← Day 20–42 (to be built)
```

> **Note on file naming:** Example files in chapters 01–07 retain their original day-number filenames (day1 through day17). The +2 day shift applies to the course schedule only — existing filenames are unchanged to avoid confusion.
