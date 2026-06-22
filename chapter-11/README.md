# Chapter 11: Modules & Packages

## Chapter Overview

So far every program you wrote lived in a single file. That works for small scripts,
but real software is built from many small reusable pieces. **Modules and packages**
are how Python lets you split code across files and reuse code other people wrote.

A **module** is just a `.py` file full of code (functions, variables, classes).
A **package** is a folder of modules. The moment you `import` something, you are
standing on the shoulders of giants — Python ships with hundreds of ready-made
modules (the "standard library"), and millions more are a `pip install` away.

In this chapter you will learn to:
- **Import** code three different ways (`import`, `from ... import`, `import ... as`)
- **Tour the standard library** — `math`, `random`, `datetime`, `os`, `sys`
- Understand the famous **`if __name__ == "__main__":`** idiom and WHY it exists
- Use **pip** to install third-party packages and pin them in `requirements.txt`
- Create **virtual environments** to keep each project's packages isolated
- Write and import **your own module**, and understand what a **package** is

This chapter spans **2 days**:

| Day | Topics |
|-----|--------|
| Day 28 | `import`, `from ... import`, aliases, standard library (`math`, `random`, `datetime`, `os`, `sys`), the `__main__` idiom |
| Day 29 | `pip` (install/list/freeze/requirements.txt), virtual environments, third-party packages (`requests`), writing your own module, packages & `__init__.py` |

---

## Day 28: Importing & the Standard Library

### What Is a Module? What Is a Package?

```
  A MODULE is one file.            A PACKAGE is a folder of modules.

   math.py                          shopping/
   ┌──────────────┐                 ┌──────────────────────────┐
   │ def sqrt():  │                 │  __init__.py  ◄ marks it  │
   │ def floor(): │                 │  cart.py                  │
   │ pi = 3.14159 │                 │  checkout.py              │
   └──────────────┘                 │  payment.py               │
                                    └──────────────────────────┘
```

You have actually *been using* modules already — every time you typed `print()`
or `len()` you used Python's **built-in** functions. Modules are the next step:
named toolboxes you open with `import` only when you need them.

**Why bother?**
- **Reuse** — write a helper once, use it from many files
- **Organisation** — keep related code together, split big programs into pieces
- **The standard library** — thousands of solved problems, free and built in
- **Other people's code** — install and `import` packages from across the world

---

### Three Ways to Import

```
(a) import math                  →  use the full path:   math.sqrt(16)
(b) from math import sqrt        →  use the name alone:   sqrt(16)
(c) import math as m             →  use a nickname:       m.sqrt(16)
```

```python
# (a) Import the whole module. You must prefix every name with the module name.
import math
print(math.sqrt(16))      # 4.0

# (b) Import specific names. Now you use them WITHOUT the prefix.
from math import sqrt, pi
print(sqrt(16))           # 4.0
print(pi)                 # 3.141592653589793

# (c) Import with an alias (a shorter nickname). Common for long names.
import datetime as dt
print(dt.date.today())
```

**Which style should I use?**

| Style | When to use it | Trade-off |
|-------|----------------|-----------|
| `import math` | Most of the time. Keeps it obvious where a name came from. | Slightly longer to type |
| `from math import sqrt` | When you use one or two names a lot | Hides which module the name came from |
| `import numpy as np` | Long module names with a well-known nickname | Only use *standard* aliases people recognise |

> **Common Mistake: `from module import *`**
>
> ```python
> from math import *      # imports EVERYTHING — avoid this!
> ```
>
> The `*` dumps every name from the module into your file. Two modules might
> both define `sqrt` and silently overwrite each other, and a reader can no
> longer tell where a name came from. Import only what you need, by name.

---

### Standard Library Tour

The **standard library** is the collection of modules that come bundled with Python.
No installation required — just `import` and go. Here are five you will use constantly.

#### `math` — numbers, roots, rounding, constants

```python
import math

math.pi              # 3.141592653589793
math.e               # 2.718281828459045
math.sqrt(81)        # 9.0
math.pow(2, 5)       # 32.0  (2 to the power 5)
math.floor(3.7)      # 3     (round DOWN)
math.ceil(3.1)       # 4     (round UP)
math.factorial(5)    # 120   (5 x 4 x 3 x 2 x 1)
math.gcd(12, 18)     # 6     (greatest common divisor)
```

#### `random` — randomness for games and sampling

```python
import random

random.random()              # a float in [0.0, 1.0)
random.randint(1, 6)         # whole number 1..6 INCLUSIVE (great for dice)
random.uniform(1, 10)        # a float between 1.0 and 10.0
random.choice(["a","b","c"]) # pick ONE item at random
random.sample([1,2,3,4], 2)  # pick 2 unique items
random.shuffle(my_list)      # shuffle a list IN PLACE (returns None!)
```

> **Common Mistake: expecting `shuffle` to return a new list**
>
> ```python
> deck = [1, 2, 3]
> shuffled = random.shuffle(deck)   # WRONG — shuffled is None!
> print(shuffled)                   # None
> ```
>
> `random.shuffle` rearranges the list *in place* and returns `None`. Look at
> the original list afterwards — `deck` itself is now shuffled.

#### `datetime` — dates, times, and date math

```python
from datetime import date, datetime, timedelta

today = date.today()                 # e.g. 2026-06-19
today.year, today.month, today.day   # 2026 6 19

now = datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")    # format a date as text

# Date MATH with timedelta (a span of time):
one_week_later = today + timedelta(days=7)
days_between = (date(2027, 1, 1) - today).days   # how many days apart?
```

Common `strftime` format codes:

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2026 |
| `%m` | 2-digit month | 06 |
| `%d` | 2-digit day | 19 |
| `%H` | hour (24h) | 14 |
| `%M` | minute | 05 |
| `%S` | second | 09 |

#### `os` — talk to the operating system

```python
import os

os.getcwd()                       # current working directory
os.listdir(".")                   # list files in a folder
os.path.join("a", "b", "file.txt")# build a path the safe, cross-OS way
os.path.basename("a/b/file.txt")  # "file.txt"
os.path.dirname("a/b/file.txt")   # "a/b"
os.environ.get("HOME", "default") # read an environment variable safely
```

`os.path.join` matters because Windows uses `\` and macOS/Linux use `/`.
Let `os` handle the separator so your code runs everywhere.

#### `sys` — the Python interpreter itself

```python
import sys

sys.version           # the Python version string
sys.platform          # 'darwin' (mac), 'linux', or 'win32'
sys.argv              # list of command-line arguments
```

`sys.argv` holds whatever you typed after the file name. Run
`python3 myscript.py hello 42` and `sys.argv` becomes
`['myscript.py', 'hello', '42']` (note: everything is a string).

---

### The `if __name__ == "__main__":` Idiom

This is one of the most-asked-about lines in all of Python. Here is the whole story.

Every Python file has a hidden built-in variable called `__name__`. Python sets it
for you, and its value depends on **how the file is being used**:

```
  RUN the file directly:          IMPORT the file from another file:
  python3 greeter.py              import greeter

  ┌───────────────────────┐       ┌───────────────────────┐
  │ __name__ == "__main__"│       │ __name__ == "greeter" │
  └───────────────────────┘       └───────────────────────┘
```

So this guard lets a file run "demo" or "test" code **only when run directly**,
and stay quiet when **imported** by another file:

```python
def greet(name):
    return f"Hello, {name}!"

# This runs ONLY if you do `python3 greeter.py`.
# It is SKIPPED when another file does `import greeter`.
if __name__ == "__main__":
    print(greet("World"))
```

**Why does this matter?** Imagine `greeter.py` printed `greet("World")` at the top
level without the guard. The moment another file did `import greeter`, that print
would fire as an unwanted side effect — just from importing! The guard separates
"library code that gets imported" from "script code that runs the program."

```
  WITHOUT the guard                    WITH the guard
  ─────────────────                    ──────────────
  import greeter                       import greeter
    → prints "Hello, World!"             → silent. 
      (surprise side effect!)              You import ONLY the functions you want.
```

Rule of thumb: put reusable functions at the top of the file, and put the code that
*runs the program* inside `if __name__ == "__main__":`.

---

### Hands-on Day 28

**Dice roller with `random`:**
```python
import random

def roll_dice(sides=6):
    """Returns a random roll between 1 and `sides`."""
    return random.randint(1, sides)

print("You rolled a", roll_dice())     # 1..6
print("D20 roll:", roll_dice(20))      # 1..20
```

**Date calculator with `datetime`:**
```python
from datetime import date

birthday = date(2000, 5, 17)
today = date.today()
days_alive = (today - birthday).days
print(f"You have been alive for {days_alive} days!")
```

See `day28_examples.py` for a full runnable tour of all five modules plus the
`__main__` idiom in action.

---

### Day 28 Mini Exercises

1. Use `math` to compute the area of a circle of radius 7 using `math.pi`.
2. Write a `coin_flip()` function that uses `random.choice(["Heads", "Tails"])` and call it 5 times.
3. Use `datetime` to print how many days are left until the next New Year.
4. Use `os.getcwd()` and `os.listdir(".")` to print your current folder and the files in it.
5. Add an `if __name__ == "__main__":` block to one of your earlier scripts. Then `import` that file from a new file and confirm the block does NOT run.

> **Common Mistake: shadowing a module with a file name**
>
> If you name your own file `random.py` or `math.py`, then `import random`
> imports *your* file instead of the real standard-library module — and your
> program breaks in confusing ways. Never name your files after standard modules.

---

## Day 29: pip, Virtual Environments & Your Own Modules

### pip — the Package Manager

The standard library is huge, but it cannot contain everything. **pip** is the tool
that downloads and installs **third-party** packages from **PyPI** (the Python
Package Index at https://pypi.org) — millions of free libraries written by the
community.

> pip commands run in the **terminal**, NOT inside the Python interpreter.

```bash
pip install requests            # install a package
pip install requests==2.31.0    # install an EXACT version (pinning)
pip list                        # show everything installed
pip show requests               # details about one package
pip uninstall requests          # remove a package
pip freeze                      # list installed packages in requirements format
pip freeze > requirements.txt   # SAVE exact versions to a file
pip install -r requirements.txt # REINSTALL everything from that file
```

#### requirements.txt — pin your dependencies

A `requirements.txt` file records the exact packages (and versions) your project
needs, so a teammate (or your future self) can recreate the same environment with
one command. It is just a plain text file:

```
requests==2.31.0
rich==13.7.0
```

```
  YOU                              YOUR TEAMMATE
  ───                              ─────────────
  pip freeze > requirements.txt    git clone the project
  git commit requirements.txt      pip install -r requirements.txt
                                     → gets the EXACT same packages
```

---

### Virtual Environments — Why Isolate?

Here is the problem virtual environments solve:

```
  Project A needs   requests v2.20
  Project B needs   requests v2.31

  Install globally → CLASH! Only one version can win.
```

A **virtual environment** ("venv") gives each project its own private box of
packages, completely separate from the system Python and from other projects.

```
  python3 -m venv .venv      Project A/                Project B/
                             ┌──────────────┐          ┌──────────────┐
                             │ .venv/        │          │ .venv/        │
                             │  requests 2.20│          │  requests 2.31│
                             └──────────────┘          └──────────────┘
                                  isolated — they never see each other
```

**The full workflow:**

```bash
# 1. Create a venv in a folder named .venv
python3 -m venv .venv

# 2. ACTIVATE it (your prompt usually then shows "(.venv)")
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows

# 3. Install packages — they go ONLY inside this venv now
pip install requests

# 4. Work on your project...

# 5. DEACTIVATE when done — back to your global Python
deactivate
```

While the venv is active, `python` and `pip` point at the venv's private copies,
so projects never step on each other's toes. Tip: add `.venv/` to your `.gitignore`
— you commit `requirements.txt`, not the installed packages themselves.

---

### Third-Party Packages — the `requests` Example

`requests` is the most popular library for fetching data over the web. It is **not**
built in, so you must install it first (inside your venv):

```bash
pip install requests
```

Then the usage pattern is always the same — **install with pip, then import, then use:**

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200 means success
print(response.json())        # parse the JSON body into a Python dict
```

(We keep this conceptual — `day29_examples.py` does not actually install or call
`requests`, so it runs with zero setup.)

---

### Writing Your Own Module

A module is just a `.py` file. To reuse code, put your functions in one file and
`import` it from another. We made a module called `utils.py`:

```python
# utils.py
PI = 3.14159

def greet(name):
    return f"Hello, {name}! Welcome."

def add(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

def area_of_circle(radius):
    return PI * radius * radius

if __name__ == "__main__":     # self-test, runs only with `python3 utils.py`
    print(greet("Alice"))
```

Now any file **in the same folder** can use it three ways:

```python
import utils                                   # use utils.greet(...)
from utils import add, is_even                 # use add(...) directly
from utils import area_of_circle as circle_area # import under a nickname

print(utils.greet("Subham"))
print(add(7, 8))
print(circle_area(3))
```

```
  utils.py                      day29_examples.py
  ┌─────────────────┐           ┌──────────────────────────┐
  │ def greet():    │◄──────────┤ import utils              │
  │ def add():      │  import   │ print(utils.greet("Sub")) │
  │ def is_even():  │           │ print(add(7, 8))          │
  └─────────────────┘           └──────────────────────────┘
```

> **Common Mistake: forgetting the `__main__` guard in your module**
>
> ```python
> # utils.py — BAD: this print runs on every import!
> print("Loading utils...")
> ```
>
> Any top-level code runs the instant the module is imported. Wrap demo/test
> code in `if __name__ == "__main__":` so importing stays quiet and side-effect free.

---

### Packages — Many Modules in a Folder

When one file gets too big, group related modules into a **package** — a folder
with a special `__init__.py` file that tells Python "treat this folder as a package":

```
  mytools/
      __init__.py        ◄── marks the folder as a package (can be empty)
      math_helpers.py
      text_helpers.py
```

You then import with **dotted paths**:

```python
from mytools.math_helpers import add
import mytools.text_helpers
```

That is the same idea as our single `utils.py`, just scaled up into an organised,
multi-file collection. (In modern Python the `__init__.py` is sometimes optional,
but including it is the clearest, most compatible choice for beginners.)

---

### Hands-on Day 29

**Create `utils.py` and import its functions** — exactly what we did above. Run the
module by itself to fire its self-test, then import it from another file:

```bash
python3 utils.py            # runs the self-test block
python3 day29_examples.py   # imports utils and uses its functions
```

See `day29_examples.py` for the full runnable demo, plus pip/venv concepts in
comments.

---

### Day 29 Mini Exercises

1. Add a new function `multiply(a, b)` to `utils.py`, then import and use it from a new file.
2. Add a proper Google-style docstring (with `Args:` and `Returns:`) to one `utils.py` function.
3. Write out the terminal commands you would run to: create a venv, activate it, install `requests`, and save `requirements.txt`.
4. Explain in one sentence why `random.py` is a bad name for your own file.
5. **Bonus:** Turn `utils.py` into a package `mytools/` with an `__init__.py` and a module `math_helpers.py`. Import `add` via `from mytools.math_helpers import add`.

---

## Quick Reference Card

```
IMPORT STYLES
  import math                 → math.sqrt(16)
  from math import sqrt       → sqrt(16)
  import datetime as dt       → dt.date.today()
  (avoid:  from math import *  — pollutes your namespace)

STANDARD LIBRARY HIGHLIGHTS
  math      sqrt, pow, floor, ceil, factorial, gcd, pi, e
  random    random(), randint(a,b), choice(seq), sample, shuffle
  datetime  date.today(), datetime.now(), timedelta(days=n), strftime()
  os        getcwd(), listdir(), path.join(), environ.get()
  sys       version, platform, argv

THE __main__ IDIOM
  if __name__ == "__main__":
      main()                  # runs ONLY when the file is run directly,
                              # NOT when it is imported

pip  (run in the TERMINAL)
  pip install <pkg>           pip install <pkg>==1.2.3
  pip list                    pip show <pkg>
  pip freeze > requirements.txt
  pip install -r requirements.txt

VIRTUAL ENVIRONMENTS
  python3 -m venv .venv       # create
  source .venv/bin/activate   # activate (mac/linux)
  .venv\Scripts\activate      # activate (windows)
  deactivate                  # leave

YOUR OWN MODULE / PACKAGE
  module  = one .py file              → import utils
  package = folder + __init__.py      → from mytools.helpers import add
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 28–29 |
| `day28_examples.py` | Runnable code: import styles, `math`/`random`/`datetime`/`os`/`sys`, the `__main__` idiom |
| `utils.py` | A custom module: `greet`, `add`, `is_even`, `area_of_circle` + a `__main__` self-test |
| `day29_examples.py` | Runnable code: imports from local `utils.py`; pip/venv/packages explained in comments |
