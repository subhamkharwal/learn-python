# Chapter 10: Error Handling

## Chapter Overview

Up to now, when something went wrong in your program, Python printed a scary red
message and **stopped everything**. A single bad value — a typo, a missing file, a
divide-by-zero — could crash your whole program.

Real software cannot work like that. A calculator should not die because you typed
"ten" instead of `10`. A file reader should not explode because a file is missing.
**Error handling** is how we write programs that *expect* things to go wrong and
respond gracefully instead of crashing.

In this chapter you will learn to:
- **Recognise** the difference between a syntax error (broken code) and an exception (runtime problem)
- **Catch** errors with `try` / `except` so your program keeps running
- **Run cleanup** code reliably with `finally`
- **Raise** your own errors when something is invalid
- **Design** custom exception types for your own programs
- **Follow best practices** so your error handling helps you instead of hiding bugs

This chapter spans **2 days**:

| Day | Topics |
|-----|--------|
| Day 26 | What exceptions are (vs syntax errors), common built-in exceptions, `try`/`except`/`else`/`finally`, catching multiple exceptions, `as e` |
| Day 27 | The `raise` statement, custom exception classes, the exception hierarchy, best practices (EAFP vs LBYL, no bare `except`) |

---

## Day 26: Exceptions and the try/except Family

### Syntax Errors vs Exceptions — Two Very Different Problems

Beginners often lump all errors together, but Python has **two distinct kinds**, and
they happen at different times.

```
SYNTAX ERROR                          EXCEPTION (runtime error)
-----------------------------         -----------------------------
Code is grammatically broken.         Code is grammatically fine,
Python cannot even START it.          but something goes wrong WHILE running.

  print("hello"                         print(10 / 0)
        ^ missing )                            ^ runs, then explodes

Detected BEFORE the program runs.     Detected WHILE the program runs.
You must FIX the code.                You can CATCH and handle it.
```

| | Syntax Error | Exception |
|---|---|---|
| When? | Before the program runs | While the program is running |
| Cause | Broken grammar (missing `:`, `)`, bad indentation) | Valid code hitting a bad situation |
| Can you catch it? | No — you must fix the code | Yes — with `try`/`except` |
| Example | `if x = 5:` | `int("hello")` |

This chapter is about the **second kind** — exceptions. A syntax error is something you
fix in your editor; an exception is something your *running* program can deal with.

---

### What Happens When an Exception Is Not Handled?

When an exception occurs and nobody catches it, Python prints a **traceback** and stops:

```
Traceback (most recent call last):
  File "demo.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```

Read a traceback **from the bottom up**:
- The **last line** is the exception type and message: `ZeroDivisionError: division by zero`
- The lines above show *where* it happened (the file, line number, and code)

The exception type (`ZeroDivisionError`) is the single most useful piece of information —
it tells you exactly which problem occurred.

---

### Common Built-in Exceptions

Python ships with many exception types. These six show up constantly:

| Exception | Happens when… | Example that triggers it |
|-----------|---------------|--------------------------|
| `ValueError` | Right type, **wrong value** | `int("hello")` |
| `TypeError` | **Wrong type** for an operation | `"abc" + 5` |
| `KeyError` | A dict key does not exist | `{"a": 1}["z"]` |
| `IndexError` | A list/tuple index is out of range | `[1, 2, 3][10]` |
| `ZeroDivisionError` | You divide by zero | `5 / 0` |
| `FileNotFoundError` | You open a file that isn't there | `open("missing.txt")` |

> **Common Mistake: Confusing `ValueError` and `TypeError`**
>
> ```python
> int("hello")   # ValueError  - "hello" is the right TYPE (str) but a bad VALUE
> "abc" + 5      # TypeError    - you used the WRONG TYPE (str + int)
> ```
>
> Remember: `TypeError` is about *what kind of thing* it is; `ValueError` is about
> *what the value actually is*.

---

### The `try` / `except` Block

The core tool. Put risky code in `try`; put the rescue plan in `except`:

```python
try:
    number = int("hello")        # this line might fail
    print(number)                # skipped if the line above failed
except ValueError:
    print("That was not a valid number!")
```

How it flows:
- Python runs the `try` block line by line.
- If **no** exception happens, the `except` block is **skipped** entirely.
- If an exception happens, Python **jumps immediately** to the matching `except` block.
  Any remaining lines in the `try` block are skipped.

---

### Catching the Exception Object with `as e`

Add `as e` to grab the exception object itself, so you can read its message:

```python
try:
    int("hello")
except ValueError as e:
    print(f"Type   : {type(e).__name__}")   # ValueError
    print(f"Message: {e}")                  # invalid literal for int()...
```

- `e` is the exception object.
- `type(e).__name__` gives the exception's class name as a string.
- Printing `e` shows the human-readable message.

---

### Catching Multiple Exceptions

A single `try` can have **several** `except` blocks — one per problem you anticipate:

```python
try:
    value = data[key]
except KeyError:
    print("That key does not exist.")
except TypeError:
    print("That object cannot be indexed.")
```

Python checks the `except` blocks **top to bottom** and runs the **first** one that
matches. If you want one handler for several types, group them in a **tuple**:

```python
try:
    value = int(user_text)
except (ValueError, TypeError) as e:
    print(f"Bad input: {e}")
```

---

### The Full Flow: `try` / `except` / `else` / `finally`

The complete structure has four parts. Two are optional but powerful:

```
        ┌─────────────────────────────────────────────┐
        │  try:                                        │
        │      <risky code>                            │
        └───────────────┬─────────────────────────────┘
                        │
          did an exception happen?
                        │
          ┌─────────────┴─────────────┐
          ▼ YES                        ▼ NO
   ┌──────────────┐            ┌────────────────┐
   │  except:     │            │  else:         │
   │  handle it   │            │  runs only if  │
   │              │            │  try SUCCEEDED │
   └──────┬───────┘            └────────┬───────┘
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 ┌────────────────┐
                 │   finally:     │
                 │  ALWAYS runs   │  ◄── cleanup, no matter what
                 └────────────────┘
```

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")     # runs only on error
    else:
        print(f"Result is {result}")        # runs only on success
    finally:
        print("Done dividing.")             # ALWAYS runs
```

| Block | When it runs |
|-------|--------------|
| `try` | Always — this is the code you are protecting |
| `except` | Only if a matching exception was raised |
| `else` | Only if the `try` block finished with **no** exception |
| `finally` | **Always** — success, failure, even if you `return` early |

**Why `else` instead of just putting the code in `try`?** Code in `else` is "the
success path." Keeping it out of `try` means an unexpected error there won't be
accidentally swallowed by your `except`.

**Why `finally`?** It guarantees cleanup (closing files, releasing locks) runs no
matter what happens.

---

### Hands-on Day 26

**Safe division function** — never crashes, returns `None` on bad input:
```python
def safe_divide(a, b):
    """Divides a by b, returning None on any error."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except TypeError:
        print("Both inputs must be numbers.")
        return None

print(safe_divide(20, 4))    # 5.0
print(safe_divide(20, 0))    # message, then None
print(safe_divide(20, "x"))  # message, then None
```

**Handle invalid input** — turn raw strings into ages, reporting problems:
```python
def parse_age(raw):
    try:
        age = int(raw)
    except ValueError:
        return f"'{raw}' is not a whole number."
    if age < 0:
        return f"'{raw}' is negative."
    return f"Valid age: {age}"

for entry in ["25", "hello", "-3"]:
    print(parse_age(entry))
```

---

### Day 26 Mini Exercises

1. Write `safe_int(text)` that returns `int(text)`, or `None` if the text isn't a valid number. Test with `"42"`, `"abc"`, `""`.
2. Write a function that reads `students[index]` from a list and returns `"out of range"` if the index is too big (catch `IndexError`).
3. Write `get_value(d, key)` that returns `d[key]`, or `"not found"` if the key is missing (catch `KeyError`).
4. Add a `finally` block to `safe_divide` that prints `"division attempt finished"` every time. Confirm it runs on both success and failure.

> **Common Mistake: Putting too much code inside `try`**
>
> ```python
> # WRONG - if the print line raised an error, it'd be blamed on int()
> try:
>     n = int(text)
>     print(some_undefined_variable)   # NameError - hidden by the except!
> except ValueError:
>     print("bad number")
> ```
>
> Keep the `try` block as **small as possible** — only the one risky line. Put the
> rest in `else` or after the block, so unrelated bugs aren't accidentally caught.

---

## Day 27: Raising, Custom Exceptions, and Best Practices

### The `raise` Statement — Throwing Your Own Errors

So far Python raised exceptions *for* us. With `raise`, **you** signal a problem
yourself — useful when a value is technically valid Python but wrong for your program:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

set_age(-5)   # raises ValueError: Age cannot be negative.
```

You `raise` an **instance** of an exception class, usually with a helpful message:

```python
raise ValueError("clear, specific message here")
```

**Re-raising** — sometimes you catch an error, do something (like log it), then want it
to keep travelling up. A bare `raise` (no arguments) re-throws the current exception:

```python
try:
    risky()
except ValueError:
    print("logging the problem...")
    raise            # re-raise the SAME exception unchanged
```

---

### Creating Custom Exception Classes

Built-in exceptions are great, but for your own programs a **custom exception** makes
your code clearer and lets callers catch *your* specific error. You make one by
**subclassing `Exception`**:

```python
class ValidationError(Exception):
    """Raised when user data fails validation."""
    pass        # the body can be empty - it inherits everything it needs

# Now use it like any built-in exception:
def check_username(name):
    if len(name) < 3:
        raise ValidationError(f"'{name}' is too short.")
    return name
```

Callers can catch it by name:

```python
try:
    check_username("ab")
except ValidationError as e:
    print(f"Rejected: {e}")
```

You can also store **extra data** on the exception by writing a custom `__init__`:

```python
class FieldError(Exception):
    def __init__(self, field, message):
        self.field = field                      # extra attribute
        super().__init__(f"[{field}] {message}")  # set the standard message

try:
    raise FieldError("email", "missing @ symbol")
except FieldError as e:
    print(e)         # [email] missing @ symbol
    print(e.field)   # email  <- our custom attribute
```

> **Common Mistake: Inheriting from the wrong base class**
>
> ```python
> # WRONG - never subclass BaseException directly
> class MyError(BaseException):
>     pass
> ```
>
> Always subclass **`Exception`** (or a more specific built-in). `BaseException` is the
> root that also includes things like `KeyboardInterrupt` and `SystemExit`, which you
> usually do *not* want your custom error mixed up with.

---

### The Exception Hierarchy

Exceptions form a **family tree**. This matters because catching a **parent** class
also catches all of its **children**.

```
BaseException                 ◄── the root (don't catch this directly)
 └── Exception                ◄── catch THIS (or something more specific)
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── KeyError
      │    └── IndexError
      ├── ValueError
      ├── TypeError
      └── OSError
           └── FileNotFoundError
```

Because `ZeroDivisionError` is a child of `ArithmeticError`:

```python
try:
    1 / 0
except ArithmeticError as e:   # the PARENT catches the child
    print(f"caught: {e}")      # caught: division by zero
```

And because both `KeyError` and `IndexError` are children of `LookupError`, one handler
can catch both:

```python
try:
    [1, 2, 3][99]
except LookupError as e:
    print(f"caught a {type(e).__name__}")   # caught an IndexError
```

> **Common Mistake: Ordering `except` from general to specific**
>
> ```python
> # WRONG - the broad handler catches everything first;
> #         the ValueError block can NEVER run.
> try:
>     ...
> except Exception:
>     print("general")
> except ValueError:        # unreachable!
>     print("specific")
> ```
>
> List **specific exceptions first**, broad ones last. Python uses the first match.

---

### Best Practices

**1. Catch specific exceptions, not everything.**

```python
# BAD - catches typos, bugs, even Ctrl-C; you never learn what broke
try:
    risky()
except:
    pass

# GOOD - you state exactly what you expect and react to it
try:
    risky()
except ValueError as e:
    print(f"bad value: {e}")
```

**2. Never silence errors with a bare `except: pass`.** It hides bugs and makes
debugging miserable. If you truly must ignore something, at least catch the *specific*
type and leave a comment explaining why.

**3. EAFP vs LBYL — prefer EAFP in Python.**

- **LBYL** = "Look Before You Leap": check conditions *before* acting.
- **EAFP** = "Easier to Ask Forgiveness than Permission": just try it, handle failure.

```python
data = {"name": "Bob"}

# LBYL - check first
if "age" in data:
    age = data["age"]
else:
    age = "unknown"

# EAFP - just try (the preferred, more Pythonic style)
try:
    age = data["age"]
except KeyError:
    age = "unknown"
```

EAFP is favoured in Python because it avoids a subtle race (the key could change
between the check and the access) and often reads more cleanly.

**4. Give exceptions clear messages.** `raise ValueError("Age cannot be negative")`
helps far more than `raise ValueError()`.

---

### Hands-on Day 27

**Build a custom `ValidationError` and validate age:**
```python
class ValidationError(Exception):
    """Raised when user data fails validation."""
    pass

def validate_age(raw):
    try:
        age = int(raw)
    except (ValueError, TypeError):
        raise ValidationError(f"'{raw}' is not a whole number.")
    if age < 0:
        raise ValidationError(f"Age {age} cannot be negative.")
    if age > 150:
        raise ValidationError(f"Age {age} is unrealistically large.")
    return age

for entry in ["42", "-7", "abc", "999"]:
    try:
        print(f"valid: {validate_age(entry)}")
    except ValidationError as e:
        print(f"rejected: {e}")
```

---

### Day 27 Mini Exercises

1. Write a function `withdraw(balance, amount)` that raises `ValueError` if `amount` is negative or greater than `balance`. Test it in a `try`/`except`.
2. Define a custom exception `NegativeNumberError(Exception)`. Write `square_root(n)` that raises it for negative `n`, otherwise returns `n ** 0.5`.
3. Define `TooShortError(ValidationError)` (subclass of your own `ValidationError`). Show that catching `ValidationError` also catches `TooShortError` (hierarchy in action).
4. Take a piece of code that uses a bare `except:` and rewrite it to catch the specific exception with a clear message.
5. **Bonus:** Write `validate_password(pw)` that raises a custom `ValidationError` with a *different message* for each rule it breaks (too short, no digit, no uppercase).

---

## Quick Reference Card

```
SYNTAX ERROR vs EXCEPTION
  Syntax error  -> broken grammar, caught BEFORE running, you must fix it
  Exception     -> valid code, problem WHILE running, you can CATCH it

THE FULL try BLOCK
  try:
      <risky code>          # always attempted
  except SomeError as e:    # runs if that error happens; e = the object
      <handle it>
  except (ErrA, ErrB):      # one handler for several types (tuple)
      <handle it>
  else:
      <success path>        # runs only if try had NO error
  finally:
      <cleanup>             # ALWAYS runs

COMMON BUILT-IN EXCEPTIONS
  ValueError          right type, wrong value      int("hello")
  TypeError           wrong type for operation      "abc" + 5
  KeyError            dict key missing              {"a":1}["z"]
  IndexError          list index out of range       [1,2,3][10]
  ZeroDivisionError   division by zero              5 / 0
  FileNotFoundError   file does not exist           open("missing.txt")

RAISING
  raise ValueError("clear message")    # throw your own
  raise                                # bare raise = re-raise current one

CUSTOM EXCEPTIONS
  class ValidationError(Exception):    # subclass Exception (NOT BaseException)
      pass
  raise ValidationError("what went wrong")

HIERARCHY (catching a parent catches its children)
  Exception
   ├── ArithmeticError -> ZeroDivisionError
   ├── LookupError     -> KeyError, IndexError
   └── ValueError, TypeError, OSError -> FileNotFoundError

BEST PRACTICES
  [ ] Catch SPECIFIC exceptions, not bare 'except:'
  [ ] Never silence errors with 'except: pass'
  [ ] List specific excepts BEFORE general ones
  [ ] Prefer EAFP (try/except) over LBYL (check-first)
  [ ] Give exceptions clear, helpful messages
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 26–27 |
| `day26_examples.py` | Runnable code: built-in exceptions, try/except/else/finally, multiple excepts, `as e` |
| `day27_examples.py` | Runnable code: raise, custom exception classes, hierarchy, EAFP vs LBYL, best practices |
