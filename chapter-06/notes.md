# Chapter 06 — Loops

> **Days:** 12, 13, 14  
> **Prerequisite chapters:** 01–05 (variables, data types, operators, strings, control flow)

---

## Chapter Overview

Loops let a program repeat a block of code automatically — without you copying and pasting the same lines over and over. This is one of the most powerful ideas in programming.

```
Without loops                   With loops
─────────────────────           ──────────────────────
print(1)                        for i in range(1, 6):
print(2)                            print(i)
print(3)
print(4)                        (5 numbers, 2 lines!)
print(5)
(5 numbers, 5 lines)
```

By the end of this chapter you will be able to:

- Use `for` loops to iterate over sequences and ranges
- Use `while` loops for condition-driven repetition
- Control loop flow with `break`, `continue`, and `pass`
- Write nested loops to produce patterns and grids
- Apply classic loop patterns (accumulator, counter, flag)

---

## Day 12 — The `for` Loop

### What is a `for` Loop?

A `for` loop says: *"For each item in this collection, do something."*

#### Anatomy of a `for` Loop

```
  for   item   in   collection  :
   │      │          │
   │      │          └─ any sequence: list, string, range, ...
   │      └─ a variable that holds the current item
   └─ keyword that starts the loop

        ┌─────────────────────────────┐
        │  indented block runs once   │
        │  for every item             │
        └─────────────────────────────┘
```

Flowchart:

```
        ┌───────────────────┐
        │  START            │
        └────────┬──────────┘
                 │
        ┌────────▼──────────┐
        │  More items left? │◄────────────────────┐
        └────────┬──────────┘                     │
           YES   │    NO                          │
                 │     └──► END                   │
        ┌────────▼──────────┐                     │
        │  item = next item │                     │
        └────────┬──────────┘                     │
                 │                                │
        ┌────────▼──────────┐                     │
        │  Run loop body    ├─────────────────────┘
        └───────────────────┘
```

#### Simplest Example

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

> **Watch Out! — Do Not Modify a List While Iterating Over It**
> ```python
> numbers = [1, 2, 3, 4, 5]
>
> # DANGEROUS — skips items!
> for n in numbers:
>     if n % 2 == 0:
>         numbers.remove(n)   # modifying the list you're looping over
>
> print(numbers)   # [1, 3, 5]  ← looks right but 4 was skipped!
> ```
> Always loop over a copy (`numbers[:]`) — the `[:]` syntax creates a copy of the list (you'll learn slicing in Chapter 08) — if you need to modify the original list. See the Common Mistakes section for the safe pattern.

---

### The `range()` Function

`range()` generates a sequence of numbers. You don't have to create a list by hand.

#### Three forms of `range()`

```
┌─────────────────────────────────────────────────────────────┐
│  Form 1: range(stop)                                        │
│          0, 1, 2, ..., stop-1                               │
│  Example: range(5) → 0, 1, 2, 3, 4                         │
├─────────────────────────────────────────────────────────────┤
│  Form 2: range(start, stop)                                 │
│          start, start+1, ..., stop-1                        │
│  Example: range(2, 7) → 2, 3, 4, 5, 6                      │
├─────────────────────────────────────────────────────────────┤
│  Form 3: range(start, stop, step)                           │
│          start, start+step, start+2*step, ...               │
│          stops BEFORE reaching stop                         │
│  Example: range(1, 10, 2) → 1, 3, 5, 7, 9                  │
│  Example: range(10, 0, -1) → 10, 9, 8, 7, 6, 5, 4, 3, 2, 1│
└─────────────────────────────────────────────────────────────┘
```

Quick reference table:

| Call                  | Output sequence            |
|-----------------------|----------------------------|
| `range(5)`            | 0 1 2 3 4                  |
| `range(1, 6)`         | 1 2 3 4 5                  |
| `range(0, 10, 2)`     | 0 2 4 6 8                  |
| `range(10, 0, -2)`    | 10 8 6 4 2                 |
| `range(5, 5)`         | (empty — start equals stop)|

> **Key rule:** `range()` always stops *before* the `stop` value.
> `range(1, 6)` gives 1 through **5**, not 6.

> **Watch Out! — Off-by-One Error**
> ```python
> # WRONG: stops at 9, not 10
> for i in range(1, 10):
>     print(i)   # 1..9 only
>
> # CORRECT: stops before 11, so includes 10
> for i in range(1, 11):
>     print(i)   # 1..10
> ```
> Remember: `range(start, stop)` goes up to **but not including** `stop`.

```python
# Counting from 0 to 4
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4

# Counting from 1 to 5
for i in range(1, 6):
    print(i)          # 1, 2, 3, 4, 5

# Every other number
for i in range(0, 10, 2):
    print(i)          # 0, 2, 4, 6, 8

# Counting backwards
for i in range(5, 0, -1):
    print(i)          # 5, 4, 3, 2, 1
```

---

### Iterating Over Strings

A string is a *sequence* of characters. A `for` loop visits each character one by one.

```
  string:  "hello"
            │││││
            h e l l o   ← each character in order
```

```python
word = "hello"

for ch in word:
    print(ch)

# Output:
# h
# e
# l
# l
# o
```

#### Counting specific characters

```python
sentence = "banana"
count = 0

for ch in sentence:
    if ch == "a":
        count += 1

print(f"Number of 'a's: {count}")   # 3
```

---

### Using `len()` with `range()` for Index-Based Loops

Sometimes you need the *index* (position number), not just the value. Combine `range()` with `len()`:

```
  word = "Python"
  index:  0 1 2 3 4 5
  char:   P y t h o n

  len("Python") = 6
  range(6)      = 0, 1, 2, 3, 4, 5
```

```python
word = "Python"

for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

# Output:
# Index 0: P
# Index 1: y
# Index 2: t
# Index 3: h
# Index 4: o
# Index 5: n
```

> **Tip:** When you only need values (not indices), use `for ch in word` directly. Use `range(len(...))` only when you need the position number.

---

### Day 12 Hands-on

#### Exercise 1 — Multiplication Table

Print the multiplication table for any number `n` from 1 to 10.

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Output:
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

#### Exercise 2 — Sum of First N Numbers

Add up all numbers from 1 to N.

```python
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} = {total}")   # 55
```

---

### Bonus: `enumerate()` and `zip()`

#### `enumerate()` — index + value together

Instead of `range(len(...))`, `enumerate()` gives you both the index and the value cleanly.

```python
# enumerate() gives index + value together — no more range(len(...))
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

#### `zip()` — pair two lists together

```python
# zip() pairs two lists together
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 95
# Bob: 87
# Charlie: 78
```

---

### Day 12 Mini Exercises

1. Print all even numbers from 2 to 20 using `range()`.
2. Print each character of your name on a separate line.
3. Print the numbers 10 down to 1 (countdown) using `range()`.
4. Calculate and print the product (multiplication) of all numbers from 1 to 5 (should equal 120).

---

---

## Day 13 — The `while` Loop, `break`, `continue`, `pass`

### What is a `while` Loop?

A `while` loop says: *"Keep repeating as long as this condition is True."*

#### Anatomy of a `while` Loop

```
  while   condition   :
    │          │
    │          └─ any expression that is True or False
    └─ keyword

        ┌─────────────────────────────┐
        │  indented block runs again  │
        │  and again while condition  │
        │  stays True                 │
        └─────────────────────────────┘
```

Flowchart:

```
        ┌───────────────────┐
        │  START            │
        └────────┬──────────┘
                 │
        ┌────────▼──────────┐
   ┌───►│  condition True?  │
   │    └────────┬──────────┘
   │       YES   │    NO
   │             │     └──► END
   │    ┌────────▼──────────┐
   │    │  Run loop body    │
   │    └────────┬──────────┘
   │             │
   │    ┌────────▼──────────┐
   └────┤  Update state     │
        └───────────────────┘
```

```python
count = 1

while count <= 5:
    print(count)
    count += 1      # <-- IMPORTANT: update the variable!

# Output: 1 2 3 4 5
```

#### `for` vs `while` — Which to use?

```
Use `for` when you know how many times to repeat:
    for i in range(10): ...

Use `while` when you repeat until some condition changes:
    while user_input != "quit": ...
```

---

### `break` — Exit the Loop Immediately

`break` stops the loop and jumps past it, no matter what.

```
  Loop running...
  ┌──────────────────────────────┐
  │  iteration 1                 │
  │  iteration 2                 │
  │  iteration 3  ← break here  │───► loop exits, continues after loop
  │  iteration 4  (never runs)  │
  │  iteration 5  (never runs)  │
  └──────────────────────────────┘
```

```python
for i in range(1, 10):
    if i == 5:
        break           # stop when i reaches 5
    print(i)

# Output: 1 2 3 4
# (5 is never printed)
```

---

### `continue` — Skip This Iteration, Keep Going

`continue` skips the rest of the current iteration and goes back to the loop's top.

```
  Loop running...
  ┌──────────────────────────────┐
  │  iteration 1  → runs fully  │
  │  iteration 2  → runs fully  │
  │  iteration 3  ← continue   │───► skip rest of body, go back to top
  │  iteration 4  → runs fully  │
  └──────────────────────────────┘
```

```python
for i in range(1, 8):
    if i % 2 == 0:
        continue        # skip even numbers
    print(i)

# Output: 1 3 5 7
```

---

### `pass` — Do Nothing (Placeholder)

`pass` is a no-op. It tells Python "there's nothing here yet." Useful when you're writing code structure and want to fill in details later.

```python
for i in range(5):
    pass    # placeholder — loop runs but does nothing

# No output. Loop completes silently.
```

Use case — skeleton code:

```python
def process_data():
    pass    # TODO: fill this in later
```

#### Quick Comparison Table

```
┌──────────┬───────────────────────────────────────────────────┐
│ Keyword  │ What it does                                       │
├──────────┼───────────────────────────────────────────────────┤
│ break    │ Exit the loop immediately                          │
│ continue │ Skip to the next iteration                         │
│ pass     │ Do nothing (placeholder)                           │
└──────────┴───────────────────────────────────────────────────┘
```

---

### Infinite Loops — and How to Prevent Them

An **infinite loop** runs forever because its condition never becomes False.

```python
# DANGEROUS — this never stops!
while True:
    print("I will run forever!")
```

Common causes and fixes:

```
┌──────────────────────────────────────────────────────────────┐
│ CAUSE 1: Forgot to update the condition variable             │
│                                                              │
│   BAD:                      GOOD:                           │
│   count = 0                 count = 0                       │
│   while count < 5:          while count < 5:                │
│       print(count)              print(count)                │
│       # forgot count += 1       count += 1  ← update!      │
├──────────────────────────────────────────────────────────────┤
│ CAUSE 2: Condition can never become False                    │
│                                                              │
│   BAD:                      GOOD:                           │
│   x = 1                     x = 1                           │
│   while x > 0:              while x > 0:                    │
│       x += 1  # grows          x -= 1  ← decrements        │
├──────────────────────────────────────────────────────────────┤
│ CAUSE 3: Using = instead of == in condition                  │
│   (a syntax error in Python, but common logical mistake)    │
└──────────────────────────────────────────────────────────────┘
```

**Intentional infinite loop with a break:**

Sometimes `while True` is on purpose — you want to loop until the user does something:

```python
while True:
    answer = input("Type 'quit' to stop: ")
    if answer == "quit":
        break
    print(f"You typed: {answer}")
```

This pattern is legitimate and common for menus and games.

> **Tip:** If your program seems frozen, press Ctrl+C to interrupt it.

---

### Day 13 Hands-on

#### Exercise 1 — Number Guessing Game

```python
secret = 42
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

#### Exercise 2 — Skip Even Numbers

```python
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
```

---

### Day 13 Mini Exercises

1. Print all multiples of 3 from 3 to 30 using a `while` loop.
2. Use `break` to print numbers 1 to 10 but stop if you hit a number divisible by 7.
3. Use `continue` to print every number from 1 to 20 *except* multiples of 5.
4. Write a while loop that asks the user for a positive number; keep asking until they provide one (validate input).
   > **Hint:** use `int(input(...))` to convert user input to a number.

---

---

## Day 14 — Nested Loops, `for/else`, and Loop Patterns

### Nested Loops

A **nested loop** is a loop inside another loop. The inner loop completes all its iterations for every single iteration of the outer loop.

```
Outer loop runs N times
  └─ Inner loop runs M times per outer iteration
     ─────────────────────────────────────────
     Total iterations = N × M
```

Visual example — a 3×4 grid:

```
outer i=0: inner j runs 0,1,2,3   → (0,0) (0,1) (0,2) (0,3)
outer i=1: inner j runs 0,1,2,3   → (1,0) (1,1) (1,2) (1,3)
outer i=2: inner j runs 0,1,2,3   → (2,0) (2,1) (2,2) (2,3)
```

```python
for i in range(3):          # outer loop: rows
    for j in range(4):      # inner loop: columns
        print(f"({i},{j})", end=" ")
    print()                 # newline after each row

# Output:
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
```

#### Printing a Triangle Pattern

```
*
* *
* * *
* * * *
* * * * *
```

```python
rows = 5
for i in range(1, rows + 1):       # outer: controls row number
    for j in range(i):              # inner: prints i stars
        print("*", end=" ")
    print()                         # newline after each row
```

---

### `for/else` and `while/else`

Python has an unusual feature: loops can have an `else` clause. The `else` block runs **only if the loop completed normally (without hitting a `break`)**.

```
for item in collection:
    if condition:
        break           ─── if break fires, else is SKIPPED
else:
    # runs only if loop finished without break
```

Flowchart:

```
        ┌─────────────────────┐
        │  Start loop         │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
   ┌───►│  More items?        │
   │    └──────────┬──────────┘
   │         YES   │    NO ──────────────────────────────────┐
   │               │                                         │
   │    ┌──────────▼──────────┐                              │
   │    │  Run body           │                     ┌────────▼──────┐
   │    └──────────┬──────────┘                     │  Run else     │
   │               │                                └────────┬──────┘
   │    break? ────┤                                         │
   │    NO         │   YES ──► SKIP else, exit loop          │
   └───────────────┘                                         ▼
                                                          (after loop)
```

**Classic use case — searching:**

```python
numbers = [3, 7, 1, 9, 4]
target = 6

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found.")   # runs because no break fired

# Output: 6 was not found.
```

This is much cleaner than setting a `found` flag manually.

**`while/else` works the same way:**

```python
count = 0
while count < 5:
    count += 1
else:
    print("Loop finished normally.")    # prints because no break
```

---

### Classic Loop Patterns

#### Pattern 1 — Accumulator

*Collect or combine values over each iteration.*

```
total = 0          ← start at identity value (0 for addition)

for each number:
    total = total + number   ← accumulate

print total
```

```python
numbers = [4, 7, 2, 9, 1]
total = 0

for n in numbers:
    total += n

print(f"Sum: {total}")   # 23
```

#### Pattern 2 — Counter

*Count how many items satisfy a condition.*

```
count = 0

for each item:
    if condition:
        count += 1

print count
```

```python
words = ["apple", "ant", "banana", "avocado", "cherry"]
count = 0

for word in words:
    if word.startswith("a"):   # .startswith('a') checks if the word begins with 'a' — you'll learn all string methods in Chapter 04
        count += 1

print(f"Words starting with 'a': {count}")   # 3
```

#### Pattern 3 — Flag Variable

*Track whether something has happened yet.*

```
found = False          ← assume "not found" at the start

for each item:
    if condition:
        found = True   ← mark it found
        break

if found:
    print("found!")
else:
    print("not found")
```

```python
numbers = [2, 5, 8, 13, 21]
has_large = False

for n in numbers:
    if n > 15:
        has_large = True
        break

if has_large:
    print("There is a number greater than 15.")
else:
    print("All numbers are 15 or less.")
```

> **Note:** For simple existence checks, `for/else` is often cleaner than a flag variable.

---

### Day 14 Hands-on

#### Exercise 1 — Triangle Pattern

```python
# Right-aligned triangle
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
```

#### Exercise 2 — Prime Number Finder using `for/else`

A prime number is divisible only by 1 and itself. If we find *any* divisor, it's not prime — we `break`. The `else` only runs if no divisor was found.

```python
# Check if a single number is prime using for/else
num = 29
for divisor in range(2, num):
    if num % divisor == 0:
        print(f"{num} is NOT prime (divisible by {divisor})")
        break
else:
    print(f"{num} IS prime")

# Note: In Chapter 07 you'll learn to wrap this in a reusable function.
```

---

### Day 14 Mini Exercises

1. Print a 5×5 grid of `+` characters using nested loops.
2. Use nested loops to print the multiplication table for numbers 1 to 5 (a 5×5 grid).
3. Use `for/else` to check whether the number 17 appears in a list of numbers. Print "found" or "not found".
4. Use the accumulator pattern to find the largest number in a list (without using the built-in `max()`).

---

---

## Common Mistakes

> **Note:** The off-by-one `range()` mistake and the "modifying a list while iterating" mistake have been called out as **Watch Out!** boxes directly in Day 12, where they are most relevant.

### Mistake 1 — Forgetting to Update the `while` Loop Variable

```python
# INFINITE LOOP — count never changes!
count = 0
while count < 5:
    print(count)
    # forgot: count += 1

# FIX:
count = 0
while count < 5:
    print(count)
    count += 1      # always update!
```

---

### Mistake 2 — `else` on a Loop (Misunderstanding When It Runs)

```python
for i in range(5):
    if i == 3:
        break
else:
    print("This will NOT print")   # skipped because break fired

for i in range(5):
    pass
else:
    print("This WILL print")   # prints because loop completed normally
```

---

## Key Takeaways

```
┌──────────────────────────────────────────────────────────────────┐
│  for loop    → iterate over a known sequence / range             │
│  while loop  → repeat while a condition holds                    │
│  break       → exit loop immediately                             │
│  continue    → skip current iteration, resume from top           │
│  pass        → do nothing (placeholder)                          │
│  for/else    → else runs only if no break occurred               │
│  Accumulator → total += item                                     │
│  Counter     → count += 1 when condition met                     │
│  Flag        → found = True when condition met                   │
└──────────────────────────────────────────────────────────────────┘
```
