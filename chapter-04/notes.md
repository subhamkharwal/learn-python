# Chapter 04 — Strings In-Depth

> **Days 7–9b** | Prerequisite: Chapter 03 (Operators & Expressions)
>
> Strings are everywhere in Python — user names, file paths, messages, URLs, CSV data.
> This chapter turns you from someone who vaguely knows what a string is into someone
> who can slice, search, format, and manipulate text with confidence.

---

## Chapter Overview

| Day | Topics | Key Concept |
|-----|--------|-------------|
| 7 | Creating strings, indexing, `len()`, immutability, type conversion | Strings are ordered, immutable sequences of characters |
| 8 | Slicing, concatenation, repetition, `in` / `not in` | Slicing extracts any sub-sequence without modifying the original |
| 9a | f-strings, `.format()`, core transformation methods | Methods return new strings; they never change the original |
| 9b | Search methods, `split`/`join`, method chaining, hands-on projects | Compose methods in chains to process text in one pass |

---

---

## Day 7 — String Creation, Indexing, and Immutability

### 7.1 What Is a String?

A **string** is a sequence of characters enclosed in quotes. Characters include letters,
digits, spaces, punctuation, and even emoji — anything you can type (and more).

```python
greeting = "Hello, World!"
```

Python stores each character in a numbered slot, like seats in a row.

---

### 7.2 Three Ways to Create a String

#### Single quotes
```python
name = 'Alice'
```

#### Double quotes
```python
name = "Alice"
```

Single and double quotes are **completely interchangeable** — Python does not care which
you use. Pick one style and be consistent.

**Practical tip:** If your string contains an apostrophe, wrap it in double quotes so
you don't need to escape it:

```python
sentence = "It's a great day!"   # clean
sentence = 'It\'s a great day!'  # works, but the \' is noise
```

Conversely, if your string contains double quotes, wrap in single:

```python
dialogue = 'She said "hello" to me.'
```

#### Triple quotes (multi-line strings)
Triple quotes — either `"""..."""` or `'''...'''` — let a string span multiple lines.

```python
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
```

Triple-quoted strings preserve every newline and leading space exactly as written.
They are also used for **docstrings** (function documentation), which you'll see in Chapter 07.

---

### 7.3 Escape Sequences

Sometimes you need characters that cannot be typed directly. Python uses a backslash `\`
followed by a special letter to represent them.

| Escape | Meaning | Example output |
|--------|---------|----------------|
| `\n` | Newline (go to next line) | `"line1\nline2"` → two lines |
| `\t` | Tab (horizontal indent) | `"col1\tcol2"` → tab-separated |
| `\\` | Literal backslash | `"C:\\Users\\Alice"` → `C:\Users\Alice` |
| `\'` | Literal single quote | `'it\'s'` → `it's` |
| `\"` | Literal double quote | `"say \"hi\""` → `say "hi"` |
| `\r` | Carriage return | (rarely used directly) |

```python
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

print("Name:\tAlice")
# Output:
# Name:   Alice

print("Path: C:\\Users\\Alice\\Desktop")
# Output:
# Path: C:\Users\Alice\Desktop
```

**Raw strings** — prefix with `r` to treat backslashes as literal characters (useful for
file paths on Windows and regular expressions):

```python
path = r"C:\Users\Alice\Desktop"
print(path)   # C:\Users\Alice\Desktop — no escape processing
```

---

### 7.4 The `len()` Function

`len()` returns the **number of characters** in a string, including spaces and punctuation.

```python
word = "Python"
print(len(word))        # 6

sentence = "Hello!"
print(len(sentence))    # 6

empty = ""
print(len(empty))       # 0

spaced = "hi there"
print(len(spaced))      # 8  (space counts!)
```

---

### 7.5 Indexing — Accessing Individual Characters

Each character in a string has an **index** — a number representing its position.

#### Positive indexing (left to right, starts at 0)

```
  String:   P   y   t   h   o   n
  Index:    0   1   2   3   4   5
```

```
  ┌───┬───┬───┬───┬───┬───┐
  │ P │ y │ t │ h │ o │ n │
  └───┴───┴───┴───┴───┴───┘
    0   1   2   3   4   5
```

Access a character with square brackets: `string[index]`

```python
word = "Python"
print(word[0])   # P
print(word[1])   # y
print(word[5])   # n
```

> **Important:** Python counts from 0, not 1. The first character is always at index 0.
> This trips up beginners constantly. Remember: index 0 = position 1.

#### Negative indexing (right to left, starts at -1)

Negative indices let you count backwards from the end — very handy when you need the
last character but don't know the string's length.

```
  String:    P    y    t    h    o    n
  Positive:  0    1    2    3    4    5
  Negative: -6   -5   -4   -3   -2   -1
```

```
  ┌────┬────┬────┬────┬────┬────┐
  │  P │  y │  t │  h │  o │  n │
  └────┴────┴────┴────┴────┴────┘
   -6   -5   -4   -3   -2   -1
```

```python
word = "Python"
print(word[-1])   # n  (last character)
print(word[-2])   # o  (second to last)
print(word[-6])   # P  (same as word[0])
```

**Getting the last character of any string — the pattern:**
```python
text = "Hello, World!"
last_char = text[-1]   # always works regardless of length
print(last_char)        # !
```

#### IndexError — what happens when you go out of bounds

```python
word = "Python"   # indices 0-5
print(word[10])   # IndexError: string index out of range
```

Always make sure your index is between `0` and `len(string) - 1`, or between
`-len(string)` and `-1`.

---

### 7.6 Immutability — Strings Cannot Be Changed

**Immutability** means once a string is created, you cannot change any of its characters.
If you try, Python raises a `TypeError`.

```python
word = "Python"
word[0] = "J"   # TypeError: 'str' object does not support item assignment
```

Think of a string like a **label printed on a brick**.
You can read the label. You can make a new brick with a different label.
But you cannot erase and rewrite the label on the existing brick.

```
  Original brick:   [ P y t h o n ]   ← cannot be erased
  New brick:        [ J y t h o n ]   ← entirely new object in memory
```

To "change" a string, you create a **new string** and reassign the variable:

```python
word = "Python"
word = "J" + word[1:]   # create a new string
print(word)              # Jython
```

The original `"Python"` string still exists in memory until Python's garbage collector
cleans it up — your variable just points to the new one.

**Why immutability is a good thing:**
- Strings can be safely shared between parts of your program (no surprise modifications)
- Python can cache and reuse identical strings for performance
- Strings can be used as dictionary keys (mutable objects cannot)

---

### Day 7 Mini Exercises

1. Create a variable `full_name = "Marie Curie"`. Print the first character, the last
   character, and the total length.

2. What is the index of `'o'` in `"Python"` (positive index)? What is its negative index?
   Verify both by running `"Python"[positive]` and `"Python"[negative]`.

3. Try to run this code. What error do you get, and why?
   ```python
   city = "London"
   city[0] = "l"
   ```

4. Write code that, given `word = "programming"`, prints the character exactly in the
   middle of the word. (Hint: use `len()` and integer division `//`.)

5. Print the file path `C:\new_folder\test.txt` exactly as shown. How many ways can you
   do it? (Hint: try escape sequences and raw strings.)

---

### 7.7 Converting To and From Strings

You will often need to convert between strings and other data types — for example, when
building a message that includes a number, or when reading text input that needs to be
treated as a number.

#### Converting other types TO strings — `str()`

```python
score = 42
pi = 3.14

print(str(score))   # "42"
print(str(pi))      # "3.14"
```

This is essential when using `+` to concatenate a string with a non-string value:

```python
score = 42

# WRONG — TypeError: can only concatenate str (not "int") to str
print("Your score is: " + score)

# RIGHT — convert to string first
print("Your score is: " + str(score))   # Your score is: 42
```

#### Converting strings TO numbers — `int()` and `float()`

```python
text_number = "42"
text_pi = "3.14"

print(int(text_number))     # 42    (integer)
print(float(text_pi))       # 3.14  (float)
print(float(text_number))   # 42.0  (int string → float is fine)
```

#### What happens when conversion fails

If the string doesn't look like a valid number, Python raises a `ValueError`:

```python
int("hello")    # ValueError: invalid literal for int() with base 10: 'hello'
int("3.14")     # ValueError: int() can't convert a float string directly
float("abc")    # ValueError: could not convert string to float: 'abc'
```

You will learn how to handle these errors gracefully in Chapter 08 (Exceptions).
For now, just know that bad input crashes with `ValueError`.

#### Real-world pattern

```python
age_input = "25"              # imagine this came from user input
age = int(age_input)          # convert to int so you can do maths
print("Next year you'll be " + str(age + 1))   # "Next year you'll be 26"
```

---

---

## Day 8 — Slicing, Concatenation, Repetition, and Membership

### 8.1 Slicing — Extracting Substrings

**Slicing** lets you pull out a chunk (a "slice") of a string. The syntax is:

```
string[start : stop : step]
```

- `start` — index where the slice begins (inclusive, default 0)
- `stop`  — index where the slice ends (**exclusive** — the character at `stop` is NOT included)
- `step`  — how many positions to advance each time (default 1)

#### Basic slicing diagram

```
  String:   P   y   t   h   o   n
  Index:    0   1   2   3   4   5
            |           |
            start=0     stop=3  →  "Pyt"  (characters at 0, 1, 2)
```

```
  ┌───┬───┬───┬───┬───┬───┐
  │ P │ y │ t │ h │ o │ n │
  └───┴───┴───┴───┴───┴───┘
    0   1   2   3   4   5

  [0:3]  →  P y t           (stop=3 means "up to but not including index 3")
  [2:5]  →  t h o
  [0:6]  →  P y t h o n     (entire string)
  [3: ]  →  h o n           (from index 3 to end)
  [ :3]  →  P y t           (from start to index 3)
  [ : ]  →  P y t h o n     (full copy)
```

```python
word = "Python"

print(word[0:3])    # Pyt
print(word[2:5])    # tho
print(word[3:])     # hon  (omitting stop = go to end)
print(word[:3])     # Pyt  (omitting start = begin from 0)
print(word[:])      # Python (full copy)
```

#### The `stop` index is exclusive — visualized

```
  "Python"[0:3]

  ┌───┬───┬───║───┬───┬───┐
  │ P │ y │ t ║ h │ o │ n │
  └───┴───┴───║───┴───┴───┘
    0   1   2 ║ 3   4   5
              ↑
          stop=3 (wall here — character at 3 not included)

  Result: "Pyt"
```

#### Slicing with a step

The `step` parameter controls how many positions to jump after each character taken.

```python
word = "Python"

print(word[::2])    # Pto  (every 2nd character: index 0, 2, 4)
print(word[1::2])   # yhn  (every 2nd, starting at index 1)
print(word[::3])    # Ph   (every 3rd character: index 0, 3)
```

Visualized:
```
  P   y   t   h   o   n
  0   1   2   3   4   5

  [::2]  →  P(0)  t(2)  o(4)  →  "Pto"
  [1::2] →  y(1)  h(3)  n(5)  →  "yhn"
```

#### Reversing a string with `[::-1]`

A step of `-1` means "go backwards one character at a time" — from the end to the start.

```python
word = "Python"
print(word[::-1])   # nohtyP

sentence = "Hello"
print(sentence[::-1])   # olleH
```

This is one of the most commonly used Python one-liners. Memorize it.

```
  "Python"[::-1]

  Reads right to left:  n  o  h  t  y  P  →  "nohtyP"
```

#### Negative indices in slices

```python
word = "Python"

print(word[-3:])     # hon  (last 3 characters)
print(word[:-3])     # Pyt  (everything except last 3)
print(word[-4:-1])   # tho
```

#### Summary table: common slice patterns

| Slice | Meaning | Result on `"Python"` |
|-------|---------|----------------------|
| `[:]` | Full copy | `"Python"` |
| `[2:]` | From index 2 to end | `"thon"` |
| `[:4]` | From start to index 4 (exclusive) | `"Pyth"` |
| `[1:4]` | Index 1, 2, 3 | `"yth"` |
| `[-3:]` | Last 3 characters | `"hon"` |
| `[:-2]` | Everything except last 2 | `"Pyth"` |
| `[::2]` | Every 2nd character | `"Pto"` |
| `[::-1]` | Reversed | `"nohtyP"` |

> **Slices never raise IndexError.** If `stop` exceeds the string length, Python just
> stops at the end. `"hi"[0:1000]` returns `"hi"` — no crash.

---

### 8.2 String Concatenation — Joining Strings

Use `+` to join (concatenate) two or more strings into a new string.

```python
first = "Hello"
second = "World"
result = first + ", " + second + "!"
print(result)   # Hello, World!
```

You can also use `+=` to append to a variable:

```python
message = "Good"
message += " morning"
message += ", Alice!"
print(message)   # Good morning, Alice!
```

**Remember:** `+` with strings does NOT add spaces automatically. You must include spaces
explicitly (e.g., `"Hello" + " " + "World"`).

> **Advanced Note — revisit after Chapter 06 (Loops)** *(skippable for now)*
>
> If you are joining many strings in a loop, `+` is slow because it creates a new string
> object at every step. The fast approach is `"separator".join(list_of_strings)`:
>
> ```python
> # Slow (for large N)
> result = ""
> for word in ["one", "two", "three"]:
>     result += word + " "
>
> # Fast — use join()
> words = ["one", "two", "three"]
> result = " ".join(words)
> print(result)   # one two three
> ```
>
> Once you reach Chapter 06, come back here — you'll understand exactly why `join()` is
> faster and when it matters.

---

### 8.3 String Repetition

Use `*` to repeat a string N times:

```python
print("ha" * 3)       # hahaha
print("-" * 20)       # --------------------
print("ab" * 4)       # abababab
```

This is useful for creating dividers, banners, and simple patterns.

```python
title = "WELCOME"
print("*" * 30)
print(title)
print("*" * 30)
# ******************************
# WELCOME
# ******************************
```

---

### 8.4 Membership Testing — `in` and `not in`

The `in` operator checks whether a substring exists inside a string.
It returns `True` or `False`.

```python
text = "Hello, World!"

print("World" in text)     # True
print("world" in text)     # False  (case-sensitive!)
print("xyz" in text)       # False
print("!" in text)         # True
print("not in" not in text) # True
```

`not in` is the inverse:

```python
username = "alice_99"
print("@" not in username)   # True  (no @ symbol — not an email)
```

**Case sensitivity** is a common source of bugs. If you want case-insensitive search,
convert both strings to the same case first (covered in Day 9):

```python
text = "Hello, World!"
print("world" in text.lower())   # True
```

---

### Day 8 Mini Exercises

1. Given `alphabet = "abcdefghijklmnopqrstuvwxyz"`, extract:
   - The first 5 letters
   - The last 5 letters
   - Every other letter (a, c, e, ...)
   - The alphabet reversed

2. Write a one-liner that checks if a string `s` is a palindrome (reads the same forwards
   and backwards). Test it on `"racecar"`, `"hello"`, and `"level"`.

3. Create the string `"PythonPythonPython"` using repetition, then verify with `len()`.

4. Given `sentence = "The quick brown fox"`, use `in` to check if the word `"quick"`
   is in it. Then check if `"slow"` is in it.

---

---

## Day 9a — String Formatting and Core Transformation Methods

### 9.1 String Formatting

You will often need to embed variable values into strings — for user messages, reports,
logs, and more. Python offers two main modern approaches.

#### f-strings (Python 3.6+) — the recommended approach

An f-string is a string literal prefixed with `f` (or `F`). Inside curly braces `{}`,
you write any Python expression, and its value is automatically inserted.

```python
name = "Alice"
age = 30

greeting = f"Hello, {name}! You are {age} years old."
print(greeting)
# Hello, Alice! You are 30 years old.
```

You can put **any valid Python expression** inside `{}`:

```python
price = 19.99
quantity = 3

print(f"Total: ${price * quantity:.2f}")
# Total: $59.97

print(f"Name in uppercase: {name.upper()}")
# Name in uppercase: ALICE

print(f"2 + 2 = {2 + 2}")
# 2 + 2 = 4
```

**Format specifiers** — control how values are displayed:

```python
pi = 3.14159265
print(f"Pi rounded: {pi:.2f}")       # Pi rounded: 3.14  (2 decimal places)
print(f"Pi rounded: {pi:.4f}")       # Pi rounded: 3.1416

score = 42
print(f"Score: {score:05d}")         # Score: 00042  (pad to 5 digits with zeros)

big = 1000000
print(f"Big number: {big:,}")        # Big number: 1,000,000  (comma separator)
```

**Format specifier quick reference:**

| Specifier | Meaning                  | Example              | Output      |
|-----------|--------------------------|----------------------|-------------|
| `.2f`     | 2 decimal places         | `f"{3.14159:.2f}"`   | `3.14`      |
| `05d`     | pad with zeros (width 5) | `f"{42:05d}"`        | `00042`     |
| `,`       | thousands separator      | `f"{1000000:,}"`     | `1,000,000` |
| `>10`     | right-align width 10     | `f"{'hi':>10}"`      | `"        hi"` |

**Debugging with `=` (Python 3.8+):**

```python
x = 42
print(f"{x=}")   # x=42  — prints the variable name AND value (very handy!)
```

#### `.format()` method — for compatibility

Before f-strings (Python < 3.6), `.format()` was the standard:

```python
name = "Bob"
age = 25

# Positional placeholders
msg = "Hello, {}! You are {} years old.".format(name, age)
print(msg)
# Hello, Bob! You are 25 years old.

# Named placeholders
msg = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
print(msg)
# Hello, Bob! You are 25 years old.

# Indexed placeholders
msg = "{0} and {1} and {0} again".format("Alice", "Bob")
print(msg)
# Alice and Bob and Alice again
```

**When to use which:**
- Use **f-strings** for all new code — they are faster, more readable, and more powerful
- Use **`.format()`** when writing code that must run on Python 3.5 or earlier, or when
  building template strings stored in variables (f-strings evaluate immediately)

> You may see `%s`-style formatting in older Python code — you can safely ignore it for now.

---

### 9.2 Key String Methods

A **method** is a function that belongs to an object and is called with dot notation:
`object.method(arguments)`.

**Critical rule:** String methods ALWAYS return a NEW string. They never modify the
original (remember — strings are immutable).

```python
word = "hello"
upper_word = word.upper()
print(word)        # hello  (unchanged)
print(upper_word)  # HELLO  (new string)
```

---

#### `.upper()` and `.lower()`

Convert all characters to uppercase or lowercase.

```python
text = "Hello, World!"

print(text.upper())   # HELLO, WORLD!
print(text.lower())   # hello, world!
```

Useful for **case-insensitive comparisons**:

```python
user_input = "YES"
if user_input.lower() == "yes":
    print("User confirmed.")
```

#### `.title()` and `.capitalize()`

```python
title = "the quick brown fox"
print(title.title())       # The Quick Brown Fox  (first letter of each word)
print(title.capitalize())  # The quick brown fox  (first letter of entire string)
```

---

#### `.strip()`, `.lstrip()`, `.rstrip()`

Remove whitespace (spaces, tabs, newlines) from the edges of a string.

```python
messy = "   hello world   \n"

print(repr(messy.strip()))    # 'hello world'   (both ends)
print(repr(messy.lstrip()))   # 'hello world   \n'  (left only)
print(repr(messy.rstrip()))   # '   hello world'  (right only)
```

`repr()` is used here to show quotes and invisible characters — helpful when debugging.

**This is essential for user input.** When a user types something and presses Enter,
there's often a trailing newline. Always `.strip()` user input:

```python
raw = input("Enter your name: ")
name = raw.strip()   # remove accidental spaces and newline
```

You can also strip specific characters:

```python
print("###hello###".strip("#"))    # hello
print("...wow...".strip("."))      # wow
```

---

#### `.replace()`

Replace all occurrences of a substring with another string.

```python
text = "I like cats. Cats are great. I have two cats."

new_text = text.replace("cats", "dogs")
print(new_text)
# I like dogs. Cats are great. I have two dogs.
# Note: "Cats" (capital C) was NOT replaced — case-sensitive!

# Replace all with empty string = delete
cleaned = "h-e-l-l-o".replace("-", "")
print(cleaned)   # hello

# Limit replacements
text = "aaa"
print(text.replace("a", "b", 2))   # bba  (only first 2 replaced)
```

---

### Day 9a Mini Exercises

1. Given `text = "  Python Programming  "`, write a one-liner that strips whitespace,
   converts to uppercase, and replaces spaces with underscores. Expected: `"PYTHON_PROGRAMMING"`.

2. Given `sentence = "the QUICK brown FOX"`, use `.lower()` and `.title()` to first
   normalize it to all-lowercase, then capitalize each word. Expected: `"The Quick Brown Fox"`.

3. Given `price = 9.5` and `quantity = 12`, use an f-string to print `Total: $114.00`
   with exactly 2 decimal places.

---

---

## Day 9b — Search Methods, Split/Join, and Method Chaining

### 9.3 Search and Inspection Methods

#### `.find()` and `.index()`

Find the position (index) of a substring.

- `.find()` returns the index of the **first occurrence**, or `-1` if not found
- `.index()` is the same but raises `ValueError` if not found (use carefully)

```python
text = "Hello, World!"

print(text.find("World"))    # 7   (starts at index 7)
print(text.find("xyz"))      # -1  (not found — no crash)
print(text.find("l"))        # 2   (first 'l' is at index 2)

# Search within a range: find(sub, start, end)
print(text.find("l", 3))     # 3   (search from index 3 onwards)
print(text.find("l", 4))     # 10  (next 'l' after index 4)
```

Prefer `.find()` over `.index()` when the substring might not be there:

```python
email = "user@example.com"
at_pos = email.find("@")
if at_pos != -1:
    print(f"Domain: {email[at_pos+1:]}")   # Domain: example.com
```

---

#### `.startswith()` and `.endswith()`

Check if a string begins or ends with a specific substring. Returns `True` or `False`.

```python
filename = "report_2024.pdf"

print(filename.startswith("report"))   # True
print(filename.startswith("notes"))    # False
print(filename.endswith(".pdf"))       # True
print(filename.endswith(".txt"))       # False

# Check multiple options with a tuple
print(filename.endswith((".pdf", ".docx", ".txt")))   # True
```

Useful for file extension checks, URL validation, greeting detection, etc.

---

#### `.count()`

Count how many times a substring appears.

```python
text = "banana"
print(text.count("a"))    # 3
print(text.count("an"))   # 2
print(text.count("xyz"))  # 0
```

---

#### `.split()`

Split a string into a **list** of substrings, dividing at a separator.

```python
sentence = "the quick brown fox"
words = sentence.split()           # splits on any whitespace by default
print(words)                        # ['the', 'quick', 'brown', 'fox']
print(len(words))                   # 4

csv_line = "Alice,30,Engineer"
parts = csv_line.split(",")         # split on comma
print(parts)                        # ['Alice', '30', 'Engineer']
print(parts[0])                     # Alice
print(parts[1])                     # 30
print(parts[2])                     # Engineer
```

Limit the number of splits with `maxsplit`:

```python
data = "one:two:three:four"
print(data.split(":", 2))   # ['one', 'two', 'three:four']
```

---

#### `.join()`

Join a list of strings into one string, with a separator between each element.
(This is the inverse of `.split()`.)

```python
words = ["Hello", "World", "Python"]

print(" ".join(words))    # Hello World Python
print("-".join(words))    # Hello-World-Python
print(", ".join(words))   # Hello, World, Python
print("".join(words))     # HelloWorldPython
```

---

#### `.zfill()`

Pad a string with leading zeros to a specified total width. Useful for IDs and codes.
Useful when generating padded IDs like `ORD-00042` or formatted numbers.

```python
print("42".zfill(5))    # 00042
print("7".zfill(3))     # 007
```

---

### 9.4 Method Chaining

Because each method returns a new string, you can chain calls:

```python
raw = "   Hello, World!   "

result = raw.strip().lower().replace("world", "python")
print(result)   # hello, python!
```

Read chains left to right:
1. `.strip()` removes surrounding whitespace → `"Hello, World!"`
2. `.lower()` converts to lowercase → `"hello, world!"`
3. `.replace(...)` substitutes → `"hello, python!"`

Don't chain too many steps in one line if it hurts readability — break it up:

```python
result = raw.strip()
result = result.lower()
result = result.replace("world", "python")
```

---

### 9.5 Hands-on — Name Formatter

```python
# Given a messy raw name, produce a clean, formatted version.

raw_name = "  JOHN   doe  "

# Step 1: remove leading/trailing whitespace
stripped = raw_name.strip()          # "JOHN   doe"

# Step 2: lowercase everything
lowered = stripped.lower()           # "john   doe"

# Step 3: split on whitespace (handles multiple spaces)
parts = lowered.split()              # ["john", "doe"]

# Step 4: title-case each part and join
# Note: 'for part in parts' inside a function call is a generator expression —
# you'll learn this fully in Chapter 09. For now, just read it as 'apply .title() to each word'.
formatted = " ".join(part.title() for part in parts)

print(formatted)   # John Doe
```

---

### 9.6 Hands-on — CSV-like String Parser

```python
# Manually parse a CSV-like line without any library.

csv_line = "  Alice , 30 , Engineer , New York  "

# Split on comma
fields = csv_line.split(",")
# ['  Alice ', ' 30 ', ' Engineer ', ' New York  ']

# Strip whitespace from each field
fields = [field.strip() for field in fields]
# ['Alice', '30', 'Engineer', 'New York']

name     = fields[0]
age      = int(fields[1])     # convert to int
job      = fields[2]
city     = fields[3]

print(f"Name:       {name}")
print(f"Age:        {age}")
print(f"Occupation: {job}")
print(f"City:       {city}")
print(f"Greeting:   Hello, {name}! You're a {age}-year-old {job} from {city}.")
```

---

### Day 9b Mini Exercises

1. You have `data = "2024-06-18"` (an ISO date). Use `.split("-")` to extract the year,
   month, and day as separate variables. Then use an f-string to print `"Day 18 of month 06, year 2024"`.

2. Write a function `is_valid_email(email)` that returns `True` if the email:
   - contains exactly one `@` character (use `.count()`)
   - ends with `.com` or `.org` (use `.endswith()`)

3. Given a list `words = ["hello", "world", "python"]`, use `.join()` to produce the
   string `"hello | world | python"`.

4. Using method chaining, take the string `"  DATA SCIENCE IS FUN  "`, strip whitespace,
   convert to lowercase, and replace spaces with hyphens. Expected: `"data-science-is-fun"`.

---

---

## Common Mistakes and How to Avoid Them

### Mistake 1 — Forgetting that strings are immutable

```python
# WRONG: trying to modify in-place
greeting = "hello"
greeting[0] = "H"   # TypeError!

# RIGHT: create a new string
greeting = "H" + greeting[1:]
print(greeting)   # Hello
```

### Mistake 2 — Off-by-one in slicing

```python
word = "Python"

# WRONG: expecting to get 'P'
print(word[0:0])   # '' (empty — stop=0 means nothing is included)

# RIGHT: stop is exclusive, so use stop=1 to get the first character
print(word[0:1])   # P
print(word[0])     # P (even simpler — just use indexing)
```

```
  Reminder: [start:stop] where stop is EXCLUSIVE (like a fence, not a seat)

  "Python"[0:3]
  ┌───┬───┬───║───┬───┬───┐
  │ P │ y │ t ║ h │ o │ n │
  └───┴───┴───║───┴───┴───┘
               ↑ wall at 3 — NOT included
```

### Mistake 3 — Forgetting `.strip()` on user input

```python
# If user types "Alice " (with trailing space):
name = input("Enter name: ")     # "Alice "
print(name == "Alice")           # False!  ← bug

# Fix:
name = input("Enter name: ").strip()
print(name == "Alice")           # True
```

### Mistake 4 — Case-sensitive comparisons

```python
answer = input("Continue? (yes/no): ")  # user types "YES" or "Yes"

# WRONG:
if answer == "yes":   # only matches exactly lowercase "yes"
    ...

# RIGHT:
if answer.lower() == "yes":
    ...
```

### Mistake 5 — Treating `.split()` result as a string

```python
sentence = "hello world"
words = sentence.split()     # returns a LIST, not a string
print(words[0])               # "hello"  ← correct

print(words.upper())          # AttributeError! lists don't have .upper()
print(words[0].upper())       # "HELLO"  ← correct
```

### Mistake 6 — Confusing `find()` return value

```python
text = "hello"
pos = text.find("x")    # returns -1, not None or False

# WRONG:
if not pos:   # -1 is truthy, 0 is falsy! This logic is broken.
    print("not found")

# RIGHT:
if pos == -1:
    print("not found")
```

---

## Quick Reference Card

```
Creation:       s = "hello"   s = 'hello'   s = """multi
                                                  line"""
Indexing:       s[0]    s[-1]    s[i]
Slicing:        s[start:stop:step]   s[::-1]  (reverse)
Length:         len(s)
Concatenation:  s1 + s2
Repetition:     s * n
Membership:     "sub" in s    "sub" not in s

Formatting:     f"Hello {name}"    "Hello {}".format(name)

Methods (return NEW string — original unchanged):
  s.upper()              → "HELLO"
  s.lower()              → "hello"
  s.title()              → "Hello World"
  s.capitalize()         → "Hello world"
  s.strip()              → removes edge whitespace
  s.strip("x")           → removes edge 'x' chars
  s.split()              → list of words
  s.split(",")           → list split by comma
  s.replace("a","b")     → replace all "a" with "b"
  s.find("sub")          → index or -1
  s.count("sub")         → number of occurrences
  s.startswith("x")      → True/False
  s.endswith("x")        → True/False
  "sep".join(list)       → joined string
  s.zfill(n)             → zero-padded string
```

---

## What's Next

In **Chapter 05 (Control Flow)**, you will use strings inside `if`/`elif`/`else`
statements — checking user input, validating data, and branching your program's logic
based on string values. Everything you learned here (`.lower()`, `in`, `.startswith()`,
etc.) will be used constantly.
