# Chapter 07: Functions

## Chapter Overview

Functions are the single most important tool for writing clean, reusable Python code.
Before functions, every program was one long list of instructions — like reading a recipe
where every ingredient and step is repeated in full every time you cook.

Functions let you:
- **Name** a block of code so you can run it again by name
- **Reuse** logic without copy-pasting
- **Organise** your program into small, understandable pieces
- **Test** individual pieces of logic in isolation

This chapter spans **4 days**:

| Day | Topics |
|-----|--------|
| Day 15 | `def`, parameters vs arguments, `return`, void functions |
| Day 16 | Default parameters, keyword arguments, multiple return values, docstrings |
| Day 17 | `*args`, `**kwargs`, complete parameter order rule |
| Day 18 | Variable scope (local/global/LEGB/shadowing/`global` keyword), recursion, common mistakes |

---

## Day 15: Your First Functions

### Why Functions? The DRY Principle

**DRY = Don't Repeat Yourself**

Imagine you need to print a welcome banner in 5 different places in your program:

```
# WITHOUT functions — repeated code
print("=" * 30)
print("    Welcome to MyApp!")
print("=" * 30)

# ... 50 lines later ...
print("=" * 30)
print("    Welcome to MyApp!")
print("=" * 30)
```

Now imagine the text changes to "Hello from MyApp!". You have to find and change every copy.

**WITH a function**, you define it once and call it anywhere:

```python
def show_banner():
    print("=" * 30)
    print("    Welcome to MyApp!")
    print("=" * 30)

show_banner()   # use it anywhere, change it in one place
```

Change the function once → all call sites updated automatically. That is DRY.

---

### Anatomy of a Function

```
  def  greet_person  (  name  )  :
   |        |            |
keyword    name      parameter
           |
    ┌──────┴────────────────────────────┐
    │  def greet_person(name):          │
    │      """Greets a person."""  ◄── docstring (optional but recommended)
    │      message = "Hello, " + name  ◄── function body (indented 4 spaces)
    │      print(message)              ◄── more body
    │      return message              ◄── return value (optional)
    └───────────────────────────────────┘
```

Breaking each part down:

| Part | What it is | Required? |
|------|-----------|-----------|
| `def` | Keyword that starts a function definition | Yes |
| `greet_person` | The function name (follows same rules as variables) | Yes |
| `(name)` | Parameter list (can be empty `()`) | Yes (parentheses always needed) |
| `:` | Colon — ends the function header | Yes |
| Indented body | The code to run when called | Yes (at least one line) |
| `return` | Sends a value back to the caller | No |

---

### Parameters vs Arguments — the Difference

These two words are often used interchangeably, but they mean different things:

```
DEFINITION time — you use PARAMETERS (placeholders):

    def add(a, b):       ← 'a' and 'b' are PARAMETERS
        return a + b


CALL time — you pass ARGUMENTS (real values):

    result = add(10, 20) ← 10 and 20 are ARGUMENTS
```

A helpful analogy:
- The **parameter** is the label on a jar: "Sugar"
- The **argument** is the actual sugar you pour into the jar

---

### The `return` Statement

`return` does two things at once:
1. **Stops** the function immediately (no more code in the function runs)
2. **Sends a value** back to whoever called the function

```
                          ┌─────────────────────┐
    result = add(3, 4)    │  def add(a, b):      │
         ▲                │      sum = a + b     │
         │                │      return sum  ────┼──► 7 sent back
         └────────────────┤                     │
              7 lands here└─────────────────────┘
```

A function can have **multiple return statements**, but only the FIRST one reached will execute:

```python
def absolute_value(n):
    if n < 0:
        return -n    # exits here if n is negative
    return n         # only reached if n >= 0
```

---

### return vs print — a Common Source of Confusion

This trips up almost every beginner. Here is the key distinction:

```
print()  →  shows something on screen. The value is GONE after display.
return   →  hands the value back to the caller to USE.
```

```python
def print_double(n):
    print(n * 2)      # shows 10 but throws it away

def return_double(n):
    return n * 2      # gives 10 back to caller


x = print_double(5)   # prints 10 to screen
print(x)              # prints None — nothing was returned!

y = return_double(5)  # y is now 10
z = return_double(y)  # z is now 20 — we can CHAIN return values!
print(z)              # prints 20
```

Rule of thumb: **use `return`** when you need the value for more computation.
Use `print` only for final display to the user.

---

### Void Functions and None

A function that has no `return` statement (or a bare `return` with no value)
automatically returns the special value **`None`**.

```python
def say_hello():
    print("Hello!")         # no return statement

result = say_hello()        # Hello! is printed
print(result)               # None
```

`None` is Python's way of saying "there is no value here". It is not zero, not
an empty string — it is the explicit absence of a value.

---

### Hands-on Day 15

**greet()** — simplest void function:
```python
def greet():
    print("Hello! Welcome to Python!")

greet()
```

**add(a, b)** — two parameters, one return:
```python
def add(a, b):
    return a + b

total = add(10, 20)
print(total)   # 30
```

**is_even(number)** — returns a boolean:
```python
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
```

---

### Day 15 Mini Exercises

1. Write a function `square(n)` that returns n squared. Call it with 5, 10, 0.
2. Write a function `greet_user(name)` that prints "Welcome, {name}!". Call it with your name.
3. Write a function `is_positive(n)` that returns `True` if n > 0, else `False`.
4. Write a function `max_of_two(a, b)` that returns the larger of the two numbers WITHOUT using the built-in `max()`.

> **Common Mistake: Forgetting to `return`**
>
> ```python
> def add(a, b):
>     result = a + b
>     # forgot to return result!
>
> total = add(3, 4)
> print(total)    # None — not 7!
> ```
>
> If you find a function returns `None` unexpectedly, check that every code path has a `return` statement.

---

## Day 16: Default Parameters, Keyword Arguments, Multiple Return Values, and Docstrings

### Default Parameter Values

Sometimes a parameter has a sensible "usual" value. You can bake that in as a default:

```python
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                   # Hello, Alice!    (uses both defaults)
greet("Bob", "Hi")               # Hi, Bob!          (overrides greeting)
greet("Charlie", "Hey", ".")     # Hey, Charlie.     (overrides both)
```

**The Golden Rule for Defaults: non-default parameters must come BEFORE defaulted ones.**

```python
# WRONG - Python does not know which "Alice" goes where
def greet(greeting="Hello", name):    # SyntaxError!
    ...

# CORRECT - required parameters come first
def greet(name, greeting="Hello"):
    ...
```

Why this rule? Python fills parameters **left to right**. If a defaulted parameter came
first, Python would have no way to decide: "Is this value for the default param or the
required one?"

---

### Keyword Arguments

When calling a function you can name each argument explicitly:

```python
def describe_pet(animal, name, age):
    print(f"I have a {age}-year-old {animal} named {name}.")

# Positional — order matters
describe_pet("dog", "Rex", 3)

# Keyword — order does NOT matter
describe_pet(name="Luna", age=5, animal="cat")
```

Keyword arguments make function calls **self-documenting**:

```python
# Which boolean means what? Hard to tell.
create_user("alice", "alice@example.com", True, False)

# Now it is crystal clear:
create_user("alice", "alice@example.com", is_admin=True, is_active=False)
```

**Mixing rule:** positional arguments must always come **before** keyword arguments in a call.

```python
describe_pet("parrot", name="Polly", age=10)   # OK — positional first
describe_pet(name="Polly", "parrot", 10)       # SyntaxError — keyword before positional
```

---

### Multiple Return Values

Python allows you to return more than one value separated by commas.
Under the hood, Python wraps them into a **tuple**.

```python
def swap(a, b):
    return b, a       # same as: return (b, a)

result = swap(10, 20)
print(result)         # (20, 10)  — it's a tuple
print(type(result))   # <class 'tuple'>
```

The real power comes from **tuple unpacking** — assigning each value to its own variable:

```python
x, y = swap(10, 20)
print(x)    # 20
print(y)    # 10
```

Practical example — returning min, max, and average:

```python
def analyze(numbers):
    # min(), max(), sum() are Python built-ins — they do exactly what their names say.
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

lo, hi, avg = analyze([4, 7, 2, 9, 1])
print(f"Min: {lo}, Max: {hi}, Avg: {avg}")
```

---

### Docstrings

A **docstring** is a string literal written as the **very first statement** inside a function.
It explains what the function does, what it expects, and what it returns.

```python
def celsius_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    The conversion formula is: F = (C * 9/5) + 32

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9 / 5) + 32
```

Docstring styles:
- **Single-line** — for obvious, short functions: `"""Returns the square of n."""`
- **Multi-line (Google style)** — uses `Args:` / `Returns:` sections (shown above)
- **Multi-line (NumPy style)** — uses `Parameters` / `Returns` sections with underlines

**Why write docstrings?**

1. Your future self will thank you when you read the code in 3 months
2. Tools like IDEs show them as tooltips as you type
3. The built-in `help()` function reads them:

```python
help(celsius_to_fahrenheit)   # prints the docstring in a formatted way
```

4. Documentation generators (Sphinx, pdoc) build entire websites from docstrings

---

### The help() Function

`help()` works on anything — built-in functions, your functions, modules, types:

```python
help(len)
help(print)
help(str.upper)
help(celsius_to_fahrenheit)   # shows YOUR docstring
```

---

### Hands-on Day 16

**Flexible greeting function:**
```python
def greet_flexible(name, greeting="Hello", punctuation="!"):
    """Greets a person with configurable greeting and punctuation."""
    print(f"{greeting}, {name}{punctuation}")

greet_flexible("Alice")
greet_flexible("Bob", greeting="Hey", punctuation="?")
```

**Swap two numbers:**
```python
def swap(a, b):
    """Returns (b, a) — the two values swapped."""
    return b, a

x, y = 5, 10
x, y = swap(x, y)
print(f"x={x}, y={y}")   # x=10, y=5
```

---

### Day 16 Mini Exercises

1. Write `power(base, exponent=2)` — default is squaring, but caller can choose any power.
2. Write `full_name(first, last, title="")` — if title is given, prepend it: "Dr. Jane Doe".
3. Write `divide_info(a, b)` that returns both the quotient and the remainder of `a / b`.
4. Add a proper multi-line docstring (with Args and Returns sections) to one of your Day 15 functions.
5. **Bonus:** Write `circle_info(radius, pi=3.14159)` with a proper Google-style docstring that returns both the area and the circumference of the circle.

> **Common Mistake: Mutable Default Argument Trap**
>
> ```python
> # WRONG — the list is created ONCE when the function is defined, not each call
> def add_item(item, container=[]):
>     container.append(item)
>     return container
>
> print(add_item("apple"))    # ['apple']
> print(add_item("banana"))   # ['apple', 'banana']  — SURPRISE! old list reused
>
> # CORRECT — use None as default, create fresh object each time
> def add_item(item, container=None):
>     if container is None:
>         container = []
>     container.append(item)
>     return container
> ```
>
> Rule: **never use a mutable object (list, dict, set) as a default parameter value.**

---

## Day 17: *args, **kwargs, and the Complete Parameter Order Rule

### *args — Variable Positional Arguments

What if you want a function that can accept **any number** of arguments?

```python
def sum_all(*args):
    print(args)         # it's a tuple!
    return sum(args)

sum_all(1, 2, 3)        # args = (1, 2, 3)
sum_all(10, 20)         # args = (10, 20)
sum_all()               # args = ()
```

The `*` in the definition says: "collect all remaining positional arguments into a tuple
and name it `args`". You can iterate over it with a `for` loop, index into it, pass it
to other functions — it behaves exactly like a regular tuple.

The name `args` is just a convention. `*numbers`, `*values`, `*items` are equally valid.
But `*args` is what every Python developer expects to see.

**Mixing regular parameters with *args:**

```python
def multiply_all(multiplier, *args):
    #               ▲            ▲
    #               |            |
    #           required      variable
    #            (first)       (rest)
    results = []
    for n in args:
        results.append(multiplier * n)
    return results
    # Bonus: the above loop can be written as [multiplier * n for n in args]
    # You'll learn list comprehensions in Chapter 09

multiply_all(3, 1, 2, 3, 4)   # multiplier=3, args=(1,2,3,4)
```

The regular parameter takes the first argument; everything else goes into `args`.

---

### **kwargs — Variable Keyword Arguments

`**kwargs` collects any extra **keyword** arguments into a **dictionary**:

```python
def print_profile(**kwargs):
    print(kwargs)           # it's a dict!
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=30, city="NYC")
# kwargs = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
```

Again, `kwargs` is just a convention. The `**` is what matters — it signals "collect
all extra keyword arguments into a dict".

---

### The Complete Parameter Order Rule

Python enforces a strict ordering when you combine all types:

```
def function(positional, *args, keyword_only, **kwargs):
               ①            ②         ③           ④

① Regular positional parameters (required, filled left-to-right)
② *args — soaks up leftover positional arguments into a tuple
③ Keyword-only parameters — come AFTER *args, must be passed by name
   (After *args, any listed parameters are keyword-only — they can only
    be passed by name. Example: def f(a, *args, sep=','): — here sep is keyword-only.)
④ **kwargs — soaks up leftover keyword arguments into a dict
```

Visual example:

```
def full_demo(name, *scores, separator="-", **extra):
               ①      ②           ③             ④

Call:  full_demo("Alice", 85, 92, 78, separator="=", grade="A")
                   ①      └──②──┘       ③               ④
```

---

### Hands-on Day 17

**sum_all with *args:**
```python
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all())               # 0
```

**print_profile with **kwargs:**
```python
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=30, city="NYC")
```

---

### Day 17 Mini Exercises

1. Write `product_all(*args)` that multiplies all given numbers together (use `*args`).
2. Write `describe_person(**info)` that prints each key-value pair on its own line.
   Example: `describe_person(name='Alice', age=30, city='NYC')` should print:
   ```
   name: Alice
   age: 30
   city: NYC
   ```
3. Write a function `tag_text(content, *tags)` that prints the content once for each tag provided. Example: `tag_text("Python", "python", "programming")` prints "Python" twice.

---

## Day 18: Variable Scope, Recursion, and Common Mistakes

### Variable Scope: Local vs Global

**Scope** is where in the code a variable is visible (can be read or written).

```
  GLOBAL SCOPE
  ┌──────────────────────────────────────────────┐
  │  planet = "Earth"    ◄── visible everywhere  │
  │                                              │
  │  def explore():                              │
  │    ┌──────────────────────────────────────┐  │
  │    │  LOCAL SCOPE of explore()           │  │
  │    │  moon = "Luna"  ◄── local only      │  │
  │    │  print(planet)  ◄── can see global  │  │
  │    └──────────────────────────────────────┘  │
  │                                              │
  │  print(moon)  ← ERROR! moon doesn't exist   │
  │               here in global scope          │
  └──────────────────────────────────────────────┘
```

Rules Python follows (LEGB Rule):

| Order | Scope | Meaning |
|-------|-------|---------|
| L | Local | Inside the current function |
| E | Enclosing | Inside any enclosing function (for nested functions) |
| G | Global | Module-level, outside all functions |
| B | Built-in | Python's own names like `print`, `len`, `range` |

Python looks up a name in this order: L → E → G → B.

**Enclosing scope** — when a function is defined inside another function, the inner
function can read variables from the outer function's scope:

```python
def outer():
    x = 10          # enclosing scope
    def inner():
        print(x)    # inner can read outer's variable
    inner()

outer()   # prints 10
```

You will explore nested functions more in a later chapter. For now, just remember: E
in LEGB means "a variable defined in an outer function that wraps this one."

**Shadowing** — a local variable hides a global with the same name:

```python
color = "blue"    # global

def paint():
    color = "red"           # NEW local variable — does NOT change global
    print(color)            # red (sees the local one)

paint()
print(color)                # blue (global unchanged)
```

---

### The global Keyword

If you genuinely need to modify a global variable from inside a function, use `global`:

```python
counter = 0

def increment():
    global counter        # tells Python: 'counter' here refers to the global one
    counter += 1

increment()
increment()
print(counter)            # 2
```

**Use `global` sparingly.** It creates invisible connections between functions and
global state, which makes bugs hard to find. The cleaner pattern is almost always to
pass the value in and return the new value out:

```python
# Preferred approach — no global needed
def increment(current):
    return current + 1

counter = 0
counter = increment(counter)
counter = increment(counter)
print(counter)    # 2
```

---

### Recursion

A **recursive function** is a function that calls itself. It is a powerful technique
for problems that have a naturally repetitive structure.

Every recursive function must have exactly two types of logic:

```
1. BASE CASE   — the stopping condition. Returns a direct answer.
                 Without this, the function calls itself forever → RecursionError

2. RECURSIVE CASE — reduces the problem and calls itself on the smaller version.
```

**Factorial** is the classic first recursion example:
```
5! = 5 × 4 × 3 × 2 × 1 = 120

Notice:  5! = 5 × 4!
              4! = 4 × 3!
                   3! = 3 × 2!
                        2! = 2 × 1!
                             1! = 1  ← BASE CASE (by definition)
```

In code:

```python
def factorial(n):
    if n <= 1:           # BASE CASE
        return 1
    return n * factorial(n - 1)    # RECURSIVE CASE
```

**The call stack for `factorial(4)`:**

```
factorial(4)
  │
  └── returns 4 * factorial(3)
                    │
                    └── returns 3 * factorial(2)
                                      │
                                      └── returns 2 * factorial(1)
                                                        │
                                                        └── returns 1  (BASE CASE)
                                          ┌─────────────────────────────
                                          ▼  now unwinding...
                                      2 * 1 = 2
                          3 * 2 = 6
              4 * 6 = 24
factorial(4) = 24
```

The call stack is a pile of function calls stacked up. Each call waits for the one
below it to return. When the base case returns, the stack "unwinds" upward, combining
the results.

---

### Common Mistakes

#### 1. Trying to modify a global without global keyword

```python
count = 0

def broken_increment():
    count += 1      # UnboundLocalError! Python sees the assignment and treats
                    # count as local, but it was never created locally.
```

#### 2. Infinite recursion (forgetting the base case)

```python
def countdown(n):
    print(n)
    countdown(n - 1)    # never stops! no base case

# Python has a recursion limit (~1000 calls) and will raise:
# RecursionError: maximum recursion depth exceeded
```

Fix:
```python
def countdown(n):
    if n <= 0:          # BASE CASE
        print("Done!")
        return
    print(n)
    countdown(n - 1)    # RECURSIVE CASE
```

---

### Day 18 Mini Exercises

1. **Scope debugging** — the following code is intentionally broken. Run it, read the error message, understand why it fails, then fix it two ways (once with `global`, once by passing and returning the value):

```python
total = 0  # global variable

def broken_add(n):
    total += n   # run this — what error do you get? why? fix it two ways.

broken_add(5)
print(total)
```

2. Write a recursive function `sum_digits(n)` that sums all digits of a number. For example, `sum_digits(1234)` → `10`. Hint: `1234 % 10` gives the last digit.
3. Write a recursive function `count_down(n)` that prints numbers from `n` down to 1, then prints "Blast off!". Include a proper base case.
4. Trace through `factorial(3)` by hand (on paper). Draw the call stack showing each function call waiting for the one below it to finish.

---

## Quick Reference Card

```
DEFINING A FUNCTION
  def function_name(param1, param2=default, *args, **kwargs):
      """Docstring."""
      body
      return value

  Parameter order:
    ① positional  ② *args  ③ keyword-only (after *args)  ④ **kwargs

  Keyword-only note: any parameter listed AFTER *args must be
  passed by name. Example: def f(a, *args, sep=','): — sep is
  keyword-only and cannot be filled by position.

CALLING A FUNCTION
  result = function_name(arg1, arg2)           # positional
  result = function_name(param2=val, param1=v) # keyword
  result = function_name(val1, val2, val3)     # extra go to *args

SCOPE RULES (LEGB)
  L → Local (inside current function)
  E → Enclosing (outer function, for nested functions)
  G → Global (module level)
  B → Built-in (print, len, range, ...)

RECURSION CHECKLIST
  [ ] Does it have a BASE CASE?
  [ ] Does the RECURSIVE CASE make the problem smaller?
  [ ] Will it eventually reach the base case for all valid input?
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `notes.md` | This file — all lesson notes for Days 15–18 |
| `day15_examples.py` | Runnable code: greet, add, is_even, void functions |
| `day16_examples.py` | Runnable code: defaults, kwargs, multiple returns, docstrings |
| `day17_examples.py` | Runnable code: *args, **kwargs, parameter order |
| `day18_examples.py` | Runnable code: scope, global keyword, recursion |
