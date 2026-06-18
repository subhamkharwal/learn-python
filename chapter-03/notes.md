# Chapter 03 — Operators & Expressions

> **Goal:** Do math, compare values, and combine conditions in Python.
> **Duration:** 2 days (Day 5 & Day 6)
> **Prerequisites:** Chapter 01 (running Python scripts) and Chapter 02 (variables & data types)

---

## Chapter Overview

Think of operators as the **verbs** of a programming language. They *act* on values (called
operands) and produce a result. In this chapter you will learn:

- How Python does arithmetic (addition, division, remainders, powers)
- The order in which Python evaluates a complex expression (precedence)
- How to compare two values and get a `True`/`False` answer
- How to combine multiple conditions with logical operators
- Shorthand ways to update a variable's value

By the end of Day 6 you will be able to write expressions like:

```python
is_adult = (age >= 18) and (age <= 65)
discount = price * 0.10 if is_member else 0
```

---

---

# Day 5 — Arithmetic Operators & Precedence

---

## 1. The 7 Arithmetic Operators

Python has **7 arithmetic operators**. Every one of them works on both integers (`int`) and
floats (`float`).

| Operator | Name             | Example      | Result |
|----------|------------------|--------------|--------|
| `+`      | Addition         | `5 + 3`      | `8`    |
| `-`      | Subtraction      | `5 - 3`      | `2`    |
| `*`      | Multiplication   | `5 * 3`      | `15`   |
| `/`      | True Division    | `5 / 2`      | `2.5`  |
| `//`     | Floor Division   | `5 // 2`     | `2`    |
| `%`      | Modulo (remainder) | `5 % 2`   | `1`    |
| `**`     | Exponentiation   | `5 ** 2`     | `25`   |

---

## 2. Addition, Subtraction, Multiplication

These behave exactly like a calculator:

```python
apples = 10
oranges = 4

total_fruit = apples + oranges   # 14
difference  = apples - oranges   # 6
product     = apples * oranges   # 40
```

**Integer + Integer → Integer**
**Integer + Float → Float** (Python promotes to the more precise type)

```python
print(3 + 2)      # 5   (int)
print(3 + 2.0)    # 5.0 (float)
```

---

## 3. True Division `/` vs Floor Division `//`

This is one of the biggest trip-ups for beginners. Pay attention here.

### True Division `/`

Always returns a **float**, even when the result is a whole number.

```python
print(10 / 2)    # 5.0  ← note the .0 !
print(7 / 2)     # 3.5
print(1 / 3)     # 0.3333333333333333
```

### Floor Division `//`

Divides and then **rounds DOWN** to the nearest whole number (the "floor").

```python
print(10 // 2)   # 5    (exact, no remainder)
print(7 // 2)    # 3    (not 3.5 — it floors down)
print(1 // 3)    # 0    (0.333... floors to 0)
print(-7 // 2)   # -4   (not -3 — floors toward negative infinity!)
```

> **Visual:** Imagine a number line. Floor always moves LEFT (toward negative infinity).
>
> ```
> <-------(-4)----(-3.5)----(-3)----0----3----3.5----4------->
>                   ^                          ^
>             -7 // 2 = -4            7 // 2 = 3
> (floors to -4,                  (floors to 3,
>  not -3)                         not 4)
> ```

**When do you use `//`?**

- Splitting items into equal groups: `cookies // kids`
- Working with integer indices: `mid = (low + high) // 2`
- Converting minutes to hours: `hours = total_minutes // 60`

---

## 4. Modulo `%` — The Remainder Operator

`a % b` gives the **leftover** after you divide `a` by `b`.

```python
print(10 % 3)    # 1   (10 = 3*3 + 1)
print(15 % 5)    # 0   (15 = 5*3 + 0, divides perfectly)
print(7 % 2)     # 1   (7 = 2*3 + 1)
```

### Real-World Use Case 1 — Even/Odd Check

```python
number = 42

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

Why? Every even number divides cleanly by 2 (remainder = 0). Every odd number leaves
remainder 1.

### Real-World Use Case 2 — Clock Math (Wrap-Around)

Imagine a 12-hour clock. What time is 3 hours after 11?

```python
current_hour = 11
hours_to_add = 3
new_hour = (current_hour + hours_to_add) % 12
print(new_hour)   # 2  (not 14!)
```

Modulo is how computers handle anything that "wraps around": clocks, calendar days,
circular buffers.

### Real-World Use Case 3 — Extract Digits

```python
number = 1357
last_digit = number % 10       # 7
second_last = (number // 10) % 10  # 5
```

**Step-by-step breakdown:**

```
1357 % 10       → 7    (remainder when divided by 10 = last digit)
1357 // 10      → 135  (remove last digit)
135 % 10        → 5    (last digit of 135 = second-to-last of 1357)
```

---

## 5. Exponentiation `**`

Raises the left number to the power of the right number.

```python
print(2 ** 10)    # 1024
print(3 ** 3)     # 27  (3 cubed)
print(9 ** 0.5)   # 3.0 (square root! same as √9)
print(2 ** -1)    # 0.5 (negative exponent = reciprocal)
```

> **Tip:** In Python, `**` is the only way to write exponentiation. There is no `^` operator
> for power — `^` means something completely different (bitwise XOR). This catches beginners!

```python
print(2 ^ 3)   # 1  ← NOT 8! This is bitwise XOR, not power
print(2 ** 3)  # 8  ← This is correct
```

---

## 6. Operator Precedence — PEMDAS

When an expression has multiple operators, Python follows a strict order of evaluation.
You may remember **PEMDAS** from school math:

```
P  — Parentheses      ()
E  — Exponentiation   **
M  — Multiplication   *
D  — Division         /  //  %
A  — Addition         +
S  — Subtraction      -
```

In Python, **M, D, A, S** are evaluated **left to right** when they appear at the same level.
Exponentiation `**` is evaluated **right to left** (it is right-associative).

### Full Python Precedence Table (Relevant Operators)

| Priority | Operator(s)          | Notes                          |
|----------|----------------------|--------------------------------|
| Highest  | `()`                 | Parentheses always win         |
| 2nd      | `**`                 | Right-to-left: `2**3**2` = `2**(3**2)` = `512` |
| 3rd      | `*`, `/`, `//`, `%`  | Left to right                  |
| Lowest   | `+`, `-`             | Left to right                  |

### Examples

```python
# Without parentheses:
result = 2 + 3 * 4       # 14, NOT 20  (multiplication before addition)
result = 10 - 4 / 2      # 8.0, NOT 3.0 (division before subtraction)
result = 2 ** 3 ** 2     # 512, NOT 64  (right-to-left: 3**2=9, then 2**9)

# With parentheses (making intent explicit):
result = (2 + 3) * 4     # 20
result = (10 - 4) / 2    # 3.0
result = (2 ** 3) ** 2   # 64
```

### Step-by-step breakdown

```
Expression: 5 + 2 * 3 - 8 / 4

Step 1: multiplication first    →  5 + 6 - 8 / 4
Step 2: division next           →  5 + 6 - 2.0
Step 3: left to right (+, -)    →  11 - 2.0
Step 4: final result            →  9.0
```

---

## 7. Parentheses for Clarity

Even when parentheses are NOT required, use them to make your intention obvious:

```python
# Hard to read:
earnings = hours * rate + overtime * rate * 1.5

# Easy to read (parentheses group related things):
earnings = (hours * rate) + (overtime * rate * 1.5)
```

Python's style guide (PEP 8) encourages using parentheses when it improves readability.

---

## Day 5 — Mini Exercises

Try these yourself before running them. Write down your predicted answer first.

**Exercise 1:** What does `17 % 5` return? What about `20 % 4`?

**Exercise 2:** Without running it, what is the result of `3 + 4 * 2 - 1`? Verify in the REPL.

**Exercise 3:** How many full weeks are in 100 days?
```python
days = 100
full_weeks = days // 7
leftover_days = days % 7
```

**Exercise 4:** A pizza has 8 slices. 3 friends want equal shares. How many slices does each
person get, and how many are left?
```python
slices = 8
people = 3
each_gets = slices // people
leftover = slices % people
```

---

---

# Day 6 — Comparison, Logical & Assignment Operators

---

## 1. Comparison Operators

Comparison operators **ask a question** about two values and always return `True` or `False`.

| Operator | Meaning                  | Example       | Result  |
|----------|--------------------------|---------------|---------|
| `==`     | Equal to                 | `5 == 5`      | `True`  |
| `!=`     | Not equal to             | `5 != 3`      | `True`  |
| `>`      | Greater than             | `7 > 3`       | `True`  |
| `<`      | Less than                | `2 < 1`       | `False` |
| `>=`     | Greater than or equal to | `5 >= 5`      | `True`  |
| `<=`     | Less than or equal to    | `4 <= 3`      | `False` |

### The `==` vs `=` Trap

This is the **number one beginner mistake** in all of programming:

```
=  (single equals)  →  STORE a value   →  age = 18    (put 18 into the box called age)
== (double equals)  →  ASK a question  →  age == 18   (is the value in age equal to 18?)
```

```
=   is the ASSIGNMENT operator   →  puts a value into a variable
==  is the EQUALITY operator     →  checks if two values are the same
```

```python
age = 18          # ASSIGNMENT: "age now holds the value 18"
age == 18         # COMPARISON: "is age equal to 18?" → True
age == 20         # COMPARISON: "is age equal to 20?" → False
```

If you accidentally write `if age = 18:` Python gives you a **SyntaxError** immediately —
so this mistake is thankfully loud and obvious.

### Comparison Works on Strings Too

Python compares strings **alphabetically** (technically by Unicode code point):

```python
print("apple" == "apple")   # True
print("apple" == "Apple")   # False  (case matters!)
print("b" > "a")            # True   (b comes after a)
print("cat" < "dog")        # True   (c comes before d)
```

---

## 2. Logical Operators

Logical operators combine multiple `True`/`False` values into one final `True`/`False`.

### `and` — Both must be True

```python
has_ticket = True
is_adult = True

can_enter = has_ticket and is_adult    # True (both conditions met)
```

**Truth Table for `and`:**

```
A        B        A and B
------   ------   -------
True     True     True
True     False    False
False    True     False
False    False    False
```

Rule: `and` is `True` ONLY when **both** operands are `True`.

### `or` — At least one must be True

```python
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday    # True (one condition met)
```

**Truth Table for `or`:**

```
A        B        A or B
------   ------   ------
True     True     True
True     False    True
False    True     True
False    False    False
```

Rule: `or` is `False` ONLY when **both** operands are `False`.

### `not` — Flips True to False and False to True

```python
is_raining = False
is_not_raining = not is_raining    # True

print(not True)    # False
print(not False)   # True
```

**Truth Table for `not`:**

```
A        not A
------   -----
True     False
False    True
```

### Combining All Three

```python
age = 25
income = 50000
has_debt = False

# Eligible for loan: adult, earns enough, no debt
eligible = (age >= 18) and (income >= 30000) and (not has_debt)
print(eligible)   # True
```

---

## 3. Short-Circuit Evaluation

Python is **lazy** — it stops evaluating as soon as the final answer is determined.

```
False  AND  (...)      True  OR  (...)
  │                      │
  ▼                      ▼
STOP — result is False  STOP — result is True
(right side never runs)  (right side never runs)
```

### Short-circuit with `and`

If the **left** side of `and` is `False`, Python **skips the right side entirely** because
the result is already guaranteed to be `False`.

```python
x = 0
# Python never evaluates (10 / x) because (x != 0) is already False
result = (x != 0) and (10 / x > 1)
print(result)   # False  (no ZeroDivisionError!)
```

### Short-circuit with `or`

If the **left** side of `or` is `True`, Python **skips the right side** because the result
is already `True`.

```python
user_name = "Alice"
# In Python, a non-empty string like "Alice" is treated as True (called "truthy")
# Python never checks the right side because user_name is already truthy
display_name = user_name or "Anonymous"
print(display_name)   # "Alice"

user_name = ""
# In Python, an empty string "" is treated as False (called "falsy")
display_name = user_name or "Anonymous"
print(display_name)   # "Anonymous"  (empty string is falsy)
```

> **Why does this matter?**
> - Performance: avoid expensive computations that aren't needed
> - Safety: guard against division-by-zero and similar errors
> - Default values: the `x or default` pattern is very common in Python

---

## 4. Assignment Operators (Shorthand)

Instead of writing `x = x + 5` you can write `x += 5`. These are called **augmented
assignment operators** or simply **shorthand operators**.

| Shorthand | Equivalent To   | Example                  |
|-----------|-----------------|--------------------------|
| `x += n`  | `x = x + n`     | `score += 10`            |
| `x -= n`  | `x = x - n`     | `lives -= 1`             |
| `x *= n`  | `x = x * n`     | `price *= 1.08`          |
| `x /= n`  | `x = x / n`     | `total /= count`         |
| `x //= n` | `x = x // n`    | `pages //= 2`            |
| `x %= n`  | `x = x % n`     | `angle %= 360`           |
| `x **= n` | `x = x ** n`    | `side **= 2`             |

### Before/After Examples

```python
# Before shorthand:
counter = 0
counter = counter + 1   # counter is now 1
counter = counter + 1   # counter is now 2

# After shorthand:
counter = 0
counter += 1   # counter is now 1
counter += 1   # counter is now 2
```

```python
# Practical: compound interest
balance = 1000.00
interest_rate = 0.05      # 5%

balance *= (1 + interest_rate)   # balance = balance * 1.05
print(f"After year 1: ${balance:.2f}")   # $1050.00

balance *= (1 + interest_rate)
print(f"After year 2: ${balance:.2f}")   # $1102.50
```

---

## 5. Common Mistakes & Gotchas

### Mistake 1 — `=` vs `==` (the classic)

```python
# WRONG — this causes a SyntaxError
if x = 10:
    print("x is ten")

# CORRECT
if x == 10:
    print("x is ten")
```

### Mistake 2 — Integer Division Surprise

```python
# Beginners expect 2.5, but Python 3 gives 2.5 correctly with /
# However, watch out for floor division when you don't want it
total = 5
count = 2

average = total / count     # 2.5  ← correct (true division)
average = total // count    # 2    ← WRONG if you wanted the real average!
```

### Mistake 3 — Float Precision (0.1 + 0.2)

This surprises almost every new programmer:

```python
print(0.1 + 0.2)           # 0.30000000000000004  ← NOT 0.3 !!
print(0.1 + 0.2 == 0.3)    # False  ← !!
```

**Why?** Computers store numbers in binary (base-2). The fraction `0.1` cannot be
represented exactly in binary — just like `1/3` cannot be represented exactly in
decimal (0.333...). A tiny rounding error accumulates.

**Fix:** Use the `round()` function, or the `math.isclose()` function for comparisons:

```python
import math

print(round(0.1 + 0.2, 2))              # 0.3
print(math.isclose(0.1 + 0.2, 0.3))    # True
```

> **Rule of thumb:** Never use `==` to compare floats directly. Always use `round()` or
> `math.isclose()`.

### Mistake 4 — `not` Precedence

```python
# This might not do what you think:
result = not True and False    # True? False?

# Python evaluates `not` before `and`:
# Step 1: not True → False
# Step 2: False and False → False
print(result)   # False

# Use parentheses to be explicit:
result = not (True and False)   # not False → True
```

---

## Day 6 — Mini Exercises

**Exercise 1:** What is the output of the following? Predict before running.
```python
x = 10
y = 3
print(x > y)
print(x == 10 and y < 5)
print(x == 5 or y == 3)
print(not (x > y))
```

**Exercise 2:** What does Python print? Watch out for short-circuit.
```python
# Short-circuit with 'and': second part never evaluated if first is False
x = 0
result = (x != 0) and (10 / x > 1)  # safe! division never happens
print(result)  # False

# Short-circuit with 'or': second part never evaluated if first is True
# In Python, an empty string "" is treated as False (called "falsy")
# A non-empty string like "Alice" is treated as True (called "truthy")
name = "Alice"
display = name or "Anonymous"
print(display)  # Alice
```

**Exercise 3:** Using only assignment operators, update a variable `score` starting at 100:
- Add 25 points
- Multiply by 2
- Subtract 10

```python
score = 100
# your code here — use +=, *=, and -=
```

What is the final value?

**Exercise 4:** Fix the float comparison bug:
```python
# This is broken:
total = 0.1 + 0.2 + 0.3
print(total == 0.6)   # Should be True but isn't. Fix it!
```

**Exercise 5 (Synthesis):** Combine arithmetic, comparison, and logical operators in one expression.
```python
# Exercise: Is the number divisible by both 3 and 5?
number = 45
# Write an expression using % and 'and' that returns True if number is divisible by both 3 and 5
```

---

## Chapter Summary

| Operator Category   | Operators                                  | Return Type       |
|---------------------|--------------------------------------------|-------------------|
| Arithmetic          | `+`, `-`, `*`, `/`, `//`, `%`, `**`        | `int` or `float`  |
| Comparison          | `==`, `!=`, `>`, `<`, `>=`, `<=`           | `bool`            |
| Logical             | `and`, `or`, `not`                         | `bool`            |
| Assignment shorthand| `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`| (modifies in place)|

### Key Takeaways

1. `/` always gives a float; `//` gives an integer (floor).
2. `%` gives the **remainder** — great for even/odd, wrapping, extracting digits.
3. Python follows **PEMDAS**. When in doubt, add parentheses.
4. `=` assigns; `==` compares. These are NOT interchangeable.
5. `and` short-circuits on `False`; `or` short-circuits on `True`.
6. Never compare floats with `==` — use `math.isclose()` instead.

---

## Next Up — Chapter 04: Strings In-Depth

Now that you can compute values and compare them, Chapter 04 dives deep into Python's
most-used type: strings. You will learn indexing, slicing, f-strings, and the most useful
string methods.
