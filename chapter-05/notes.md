# Chapter 05: Control Flow

**Duration:** 2 Days (Day 10 & Day 11)
**Prerequisites:** Variables, data types, operators (Chapters 01–04)

---

## Chapter Overview

So far your Python programs run from top to bottom, one line at a time, without making any decisions. Control flow gives your code the ability to **choose** what to do based on conditions. This is what makes programs actually useful.

Think of it like a GPS: depending on road conditions, it chooses a different route. Your program does the same — it evaluates a condition and follows a different path of code.

By the end of this chapter you will be able to:
- Write `if`, `elif`, and `else` blocks to branch your logic
- Understand Python's indentation-based block system
- Know which values Python considers truthy or falsy
- Write compact single-line decisions using ternary expressions
- Use Python 3.10's `match` statement to handle multiple cases cleanly
- Combine multiple conditions with `and` / `or`

---

## Day 10: if / elif / else

### 1. The Big Picture — How Decisions Work

Before writing any code, let's visualize what a decision looks like. Imagine asking: *"Is it raining?"*

```
          START
            |
            v
    [ Is it raining? ]
       /           \
     YES            NO
      |              |
 Take umbrella    Wear sunglasses
      |              |
       \           /
            v
          END
```

In Python, we express this with an `if` statement.

---

### 2. The `if` Statement

**Syntax:**

```python
if condition:
    # code to run when condition is True
```

**The two rules you MUST follow:**
1. The condition line ends with a **colon** `:`
2. The code inside the block is **indented** (4 spaces or 1 tab — be consistent)

**Example:**

```python
raining = True

if raining:
    print("Take an umbrella!")
```

> If `raining` is `True`, the print runs. If `False`, nothing happens.

---

### 3. Python's Indentation-Based Blocks

Most languages use `{}` curly braces to group code. Python uses **indentation** (whitespace at the start of a line) instead.

```
WRONG (no indent — Python raises IndentationError):
if True:
print("hello")   <-- ERROR

CORRECT (4-space indent):
if True:
    print("hello")   <-- OK
```

Everything at the same indent level belongs to the same block. When the indent goes back out, the block ends.

```python
if True:
    print("Inside the if block")
    print("Still inside — same indent level")
print("Outside the if block — always runs")
```

**Golden rule:** Pick 4 spaces and stick with it. Never mix tabs and spaces.

---

### 4. Adding `else`

`else` is the "otherwise" branch. It runs when the `if` condition is `False`.

```
    [ Condition? ]
       /       \
    True       False
     |           |
  if-block    else-block
       \       /
        v
      (continues)
```

```python
score = 45

if score >= 50:
    print("You passed!")
else:
    print("You did not pass. Try again.")
```

---

### 5. Adding `elif` (else if)

`elif` lets you check multiple conditions in sequence. Python checks them top to bottom and runs the **first** one that is `True`. The rest are skipped.

```
    [ Condition 1? ]
     /           \
  True          False
   |               |
 block 1     [ Condition 2? ]
              /           \
           True           False
            |               |
          block 2     [ Condition 3? ]
                        /         \
                      True        False
                       |            |
                     block 3    else-block
```

**Grade Classifier Example:**

```python
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Output: Grade: C
```

> Notice: once `score >= 70` matches, Python stops. It does NOT check `score >= 60`.

---

### 6. Truthy and Falsy Values

Python does not require a strict `True`/`False` in conditions. It evaluates any value for its "truthiness".

**Values that are FALSY (treated as False):**

| Value       | Type      | Why it's falsy              |
|-------------|-----------|------------------------------|
| `False`     | bool      | Literally false              |
| `0`         | int       | Zero                         |
| `0.0`       | float     | Zero                         |
| `""`        | str       | Empty string                 |
| `[]`        | list      | Empty list                   |
| `{}`        | dict      | Empty dictionary *(you'll learn about dictionaries in Chapter 08)* |
| `()`        | tuple     | Empty tuple *(you'll learn about tuples in Chapter 08)*            |
| `None`      | NoneType  | Absence of a value           |

**Everything else is TRUTHY** — non-zero numbers, non-empty strings, non-empty collections, etc.

**Practical example:**

```python
username = ""

if username:
    print(f"Welcome, {username}!")
else:
    print("Please enter a username.")   # This runs because "" is falsy
```

```python
items = [1, 2, 3]

if items:
    print("Cart has items")    # This runs — list is non-empty (truthy)
else:
    print("Cart is empty")
```

---

### 7. Nested Conditions

You can place an `if` inside another `if`. This is called **nesting**.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted.")
    else:
        print("Please show your ID.")
else:
    print("Sorry, you must be 18 or older.")
```

**ASCII diagram of nesting:**

```
[ age >= 18? ]
   |       \
  YES       NO
   |         \
[ has_id? ]   "You must be 18+"
  /       \
YES        NO
 |          |
"Access    "Show ID"
 granted"
```

**Pitfall — Deep Nesting:**

Nesting more than 2 levels deep becomes very hard to read. This is an anti-pattern:

```python
# BAD: 3+ levels deep is hard to follow
if user_logged_in:
    if user_has_subscription:
        if subscription_not_expired:
            if user_not_banned:
                print("Show content")
```

You will learn to flatten this with `and` in Day 11.

---

### 8. Keeping Conditions Readable

- Use clear variable names: `is_raining`, `has_permission`, `age_is_valid`
- Avoid double negatives: `if not not valid` is confusing
- Compare to nothing when checking truthiness: write `if name:` not `if name != ""`

---

### Day 10 Mini Exercises

1. Ask the user for a number. Print whether it is positive, negative, or zero.
   ```python
   # Expected output (if input is -5): Negative
   # Expected output (if input is 0):  Zero
   # Expected output (if input is 7):  Positive
   ```
2. Ask for a temperature in Celsius. Print "Hot" if above 30, "Warm" if 20–30, "Cool" if 10–19, "Cold" otherwise.
   ```python
   # Expected output (if input is 35): Hot
   # Expected output (if input is 25): Warm
   # Expected output (if input is 15): Cool
   # Expected output (if input is 5):  Cold
   ```
3. Write a login check: if username is `"admin"` AND password is `"1234"`, print "Login successful", else print "Invalid credentials". *(Hint: use `and` to join both conditions — we'll cover this in detail on Day 11)*
   ```python
   # Expected output (username="admin", password="1234"):  Login successful
   # Expected output (username="admin", password="wrong"): Invalid credentials
   ```
4. Given a list `cart = []`, print "Your cart is empty" if it has no items, otherwise print "Proceed to checkout".
   ```python
   # Expected output (cart = []):          Your cart is empty
   # Expected output (cart = ["apple"]):   Proceed to checkout
   ```

---

---

## Day 11: Ternary Expressions, match, and Combining Conditions

### 1. Ternary (Conditional) Expressions

A ternary expression squeezes a simple `if/else` onto **one line**.

**Syntax:**

```
result = value_if_true  if  condition  else  value_if_false
```

**Anatomy of a ternary expression:**

```
label  =  "Adult"   if   age >= 18   else   "Minor"
  ^           ^           ^                    ^
variable  true-value   condition           false-value
```

**Before (3 lines):**

```python
age = 20

if age >= 18:
    label = "Adult"
else:
    label = "Minor"
```

**After (1 line with ternary):**

```python
age = 20
label = "Adult" if age >= 18 else "Minor"
print(label)   # Adult
```

**More examples:**

```python
score = 55
result = "Pass" if score >= 50 else "Fail"

is_raining = False
advice = "Take umbrella" if is_raining else "No umbrella needed"
```

**When to USE ternary:**
- The condition is simple (one comparison)
- Both the true and false branches are short values or expressions
- You are assigning to a variable

**When to AVOID ternary:**
- The condition is complex (multiple `and`/`or`)
- Either branch contains multiple statements
- Nesting ternaries (`x if a else y if b else z`) — very hard to read

```python
# BAD — nested ternary, avoid this
label = "A" if s >= 90 else "B" if s >= 80 else "C"   # confusing

# GOOD — use if/elif instead for this case
```

---

### 2. Combining Conditions: `and`, `or`, `not`

You can join multiple conditions into one using logical operators.

**`and` — BOTH must be True:**

```
Condition A   AND   Condition B   =>   Result
   True              True              True
   True              False             False
   False             True              False
   False             False             False
```

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome to the event!")
```

**`or` — AT LEAST ONE must be True:**

```
Condition A   OR    Condition B   =>   Result
   True              True              True
   True              False             True
   False             True              True
   False             False             False
```

```python
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
```

**`not` — flips True to False and vice versa:**

```
not True   →  False
not False  →  True
```

```python
is_raining = False

if not is_raining:
    print("Great day for a walk!")
```

**Combining multiple conditions — use parentheses:**

Without parentheses, `and` has higher priority than `or`, which can cause bugs.

```python
# Ambiguous — what does this mean?
if a or b and c:         # Python reads it as: a or (b and c)

# Clear — use parentheses
if (a or b) and c:
if a or (b and c):
```

**Flattening deep nesting with `and`:**

```python
# Instead of 4 nested ifs:
if user_logged_in and has_subscription and not subscription_expired and not banned:
    print("Show content")
```

---

### 3. Short-Circuit Evaluation

Python stops evaluating as soon as the result is known.

- In `A and B`: if `A` is False, Python does **not** evaluate `B` (result is already False)
- In `A or B`: if `A` is True, Python does **not** evaluate `B` (result is already True)

This is useful for safety checks:

```python
items = []

# Safe — Python won't evaluate items[0] if items is empty (falsy)
if items and items[0] == "apple":
    print("First item is an apple")
```

---

### 4. The `match` Statement (Python 3.10+)

> Check your Python version with `python --version` in your terminal — this feature requires Python 3.10 or newer.

`match` is Python's modern pattern-matching tool, introduced in Python 3.10. It replaces long chains of `if/elif` when you are comparing one variable against many specific values.

**Syntax:**

```python
match variable:
    case value1:
        # runs when variable == value1
    case value2:
        # runs when variable == value2
    case _:
        # wildcard — runs when nothing else matched (like "else")
```

**Day-of-week example:**

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")
```

> The `|` inside a `case` means "or" — match either value.

**User role classifier example:**

```python
role = "editor"

match role:
    case "admin":
        print("Full access: read, write, and delete.")
    case "editor":
        print("Can read and write, but not delete.")
    case "viewer":
        print("Read-only access.")
    case _:
        print("Unknown role — no access granted.")
```

**`match` vs `if/elif` — when to choose each:**

| Scenario                             | Prefer      |
|--------------------------------------|-------------|
| Comparing one variable to fixed values | `match`   |
| Checking ranges or complex expressions | `if/elif` |
| Python version < 3.10                | `if/elif`   |
| Boolean / truthy checks              | `if/elif`   |

---

### Day 11 Mini Exercises

1. Rewrite the positive/negative/zero checker from Day 10 using ternary expressions.
   ```python
   # Expected output (number = -5): Negative
   # Expected output (number = 0):  Zero
   # Expected output (number = 7):  Positive
   ```
2. HTTP status codes are numbers web servers send back — 200 means OK, 404 means Not Found, 500 means Server Error. Write a `match` statement that takes a HTTP status code (`200`, `404`, `500`) and prints a human-readable message.
   ```python
   # Expected output (code = 200): OK
   # Expected output (code = 404): Not Found
   # Expected output (code = 500): Server Error
   ```
3. Write a condition that checks if a person can vote: age >= 18 AND is a citizen. Use `and`.
   ```python
   # Expected output (age=20, is_citizen=True):  You can vote!
   # Expected output (age=16, is_citizen=True):  You cannot vote.
   # Expected output (age=25, is_citizen=False): You cannot vote.
   ```
4. Write a `match` statement for seasons (use month numbers 1–12, group with `|`).
   ```python
   # Expected output (month = 1):  Winter
   # Expected output (month = 4):  Spring
   # Expected output (month = 7):  Summer
   # Expected output (month = 10): Autumn
   ```
5. Write a condition that checks if a user is NOT banned and IS verified before allowing access. Use `not` and `and`.
   ```python
   # Expected output (is_banned=False, is_verified=True):  Access granted.
   # Expected output (is_banned=True,  is_verified=True):  Access denied.
   # Expected output (is_banned=False, is_verified=False): Access denied.
   ```

---

---

## Common Mistakes

### Mistake 1: Using `=` instead of `==`

```python
# WRONG — this is assignment, not comparison
if x = 5:       # SyntaxError in Python
    print("five")

# CORRECT
if x == 5:
    print("five")
```

### Mistake 2: Forgetting the colon `:`

```python
# WRONG
if x > 0
    print("positive")   # SyntaxError: expected ':'

# CORRECT
if x > 0:
    print("positive")
```

### Mistake 3: Separate `if` instead of `elif`

```python
# WRONG — all three blocks are checked independently
# If score is 95, it prints "A" AND "B" because 95 >= 80 is also True
if score >= 90:
    print("A")
if score >= 80:    # <-- should be elif
    print("B")

# CORRECT — only the first matching branch runs
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
```

### Mistake 4: Wrong indentation

```python
# WRONG — second print is NOT inside the if block
if x > 0:
    print("positive")
  print("this is also positive")   # IndentationError (2 spaces vs 4)

# CORRECT — consistent 4-space indent
if x > 0:
    print("positive")
    print("this is also positive")
```

### Mistake 5: Deep nesting (the pyramid of doom)

```python
# BAD — hard to read, hard to maintain
if a:
    if b:
        if c:
            if d:
                do_something()

# BETTER — flatten with and
if a and b and c and d:
    do_something()
```

### Mistake 6: Comparing to `True`/`False` explicitly

```python
# Unnecessary
if is_active == True:
    ...

# Pythonic
if is_active:
    ...

# For False
if not is_active:
    ...
```

---

## Chapter Summary

| Concept              | Syntax / Notes                                      |
|----------------------|-----------------------------------------------------|
| `if`                 | `if condition:`                                     |
| `elif`               | `elif condition:` — checked only if previous was False |
| `else`               | `else:` — fallback when all conditions are False    |
| Indentation          | 4 spaces; defines code blocks                       |
| Falsy values         | `0`, `""`, `[]`, `{}`, `()`, `None`, `False`        |
| Ternary              | `x if condition else y`                             |
| `match`              | Python 3.10+; pattern match on a single value       |
| `and`                | Both conditions must be True                        |
| `or`                 | At least one condition must be True                 |
| `not`                | Inverts a boolean value                             |
| Short-circuit        | `and`/`or` stop evaluating as soon as result is known |
