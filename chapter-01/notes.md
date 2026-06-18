# Chapter 01 — Getting Started with Python

> **Goal:** Have Python installed, understand what it is, and run your very first program.
> **Duration:** 2 days (~45–60 minutes each)
> **Prerequisite:** None. Seriously — zero programming experience needed.

---

## Chapter Overview

By the end of these two days you will:

- Know what Python is and why it is worth learning
- Have Python and VS Code installed and working on your machine
- Be comfortable typing code in the Python REPL (interactive shell)
- Have written and run your first `.py` script from the terminal
- Understand how to use `print()` and comments

Think of this chapter as setting up your workshop before you start building things. You are picking up the tools, learning what each one does, and making sure everything is in working order.

---

## Day 1 — What is Python? Installing It. Playing in the REPL.

### 1.1 What is Python?

Python is a **programming language** — a way to give instructions to a computer in a form that is almost readable by humans.

Here is a quick analogy: Imagine you want to ask a friend to make you a sandwich. You speak to them in English. Computers, however, only understand "machine language" (binary — 0s and 1s). Python acts as a **translator** — you write instructions in a language that looks almost like English, and Python converts those instructions into something the computer can execute.

```
You (human)  -->  Python code  -->  Python interpreter  -->  Computer understands
"Make sandwich"  -->  print("Hello")  -->  converts to machine code  --> "Hello" appears on screen
```

Python was created by **Guido van Rossum** and first released in **1991**. The name comes from the British comedy group *Monty Python's Flying Circus* — not the snake (though the snake mascot stuck).

Key design philosophy: **"Readability counts."** Python code is intentionally designed to look clean and close to plain English.

---

### 1.2 Why Learn Python?

#### It is beginner-friendly

Compare Python to another popular language, Java:

**Java — to print "Hello, World!":**
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Python — to print "Hello, World!":**
```python
print("Hello, World!")
```

That is the entire program. One line. No extra ceremony.

#### It is versatile — one language, many worlds

Python is used across nearly every area of technology:

| Field | What Python does there | Famous tools |
|-------|----------------------|--------------|
| **Web Development** | Builds websites and APIs | Django, Flask, FastAPI |
| **Data Science** | Analyzes large datasets | Pandas, NumPy, Matplotlib |
| **Machine Learning / AI** | Trains models, builds AI apps | TensorFlow, PyTorch, scikit-learn |
| **Automation / Scripting** | Automates repetitive tasks | Selenium, PyAutoGUI |
| **DevOps / Cloud** | Manages servers and infrastructure | Ansible, AWS SDKs |
| **Finance** | Algorithmic trading, analysis | Quantlib, yfinance |
| **Science & Research** | Simulations, data analysis | SciPy, Biopython |
| **Education** | Teaching programming | Raspberry Pi projects |

#### It has an enormous community

Python is consistently one of the top 2–3 most popular programming languages in the world (TIOBE index, Stack Overflow surveys). That means:
- Millions of free tutorials, videos, and courses
- Answers to almost every question already on Stack Overflow
- An enormous ecosystem of free libraries (over 500,000 on PyPI)

---

### 1.3 How Python Works — The Big Picture

Before you install anything, it helps to understand what happens when you run Python code.

```
┌─────────────────────────────────────────────────────────┐
│                    HOW PYTHON RUNS                      │
│                                                         │
│   Your .py file        Python          Your Screen      │
│                       Interpreter                       │
│  ┌──────────────┐   ┌───────────┐   ┌──────────────┐  │
│  │ hello.py     │   │           │   │              │  │
│  │              │──>│  Reads &  │──>│ Hello World  │  │
│  │ print(       │   │  Executes │   │              │  │
│  │  "Hello"     │   │   code    │   │              │  │
│  │ )            │   │           │   │              │  │
│  └──────────────┘   └───────────┘   └──────────────┘  │
│                                                         │
│   You write it      Python runs it    Output appears    │
└─────────────────────────────────────────────────────────┘
```

The "Python interpreter" is a program you install on your computer. It reads your Python code line by line, from top to bottom, and executes each instruction.

---

### 1.4 Installing Python

#### Step 1 — Download Python

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow "Download Python 3.x.x" button (use the latest 3.x version)
3. Run the installer

> **Windows users — IMPORTANT:** On the first screen of the installer, check the box that says **"Add Python to PATH"** before clicking Install. If you miss this, Python will install but your terminal won't be able to find it.

> **Note:** If installation takes longer than expected, that is completely normal. Getting your environment set up is a real part of programming — take your time.

> **Mac users:** You may already have an old Python 2 on your system. Always use `python3` in the terminal to make sure you are running the new one.

#### Step 2 — Verify installation

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```
python --version
```

or on Mac/Linux:

```
python3 --version
```

You should see something like:
```
Python 3.12.4
```

If you see a version number, Python is installed successfully.

#### Step 3 — Install VS Code (Visual Studio Code)

VS Code is a free, lightweight code editor made by Microsoft. It is excellent for Python.

1. Go to **https://code.visualstudio.com/**
2. Download and install it
3. Open VS Code
4. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac) to open Extensions
5. Search for **"Python"** and install the extension by Microsoft

> **What is VS Code?** Think of it like Microsoft Word, but for writing code instead of essays. It colors your code to make it easier to read (syntax highlighting), warns you about mistakes, and lets you run programs with a click.

---

### 1.5 The Python REPL — Your Interactive Playground

#### What is the REPL?

REPL stands for **Read-Eval-Print Loop**. It is Python's interactive shell — a place where you type one line of Python, press Enter, and immediately see what happens.

**Analogy:** The REPL is like a calculator that speaks Python. You type an expression, press Enter, and get the result instantly. No files, no saving — just immediate feedback.

```
┌──────────────────────────────────────────────────────────┐
│                   THE REPL CYCLE                         │
│                                                          │
│   ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐         │
│   │ READ │───>│ EVAL │───>│PRINT │───>│ LOOP │         │
│   └──────┘    └──────┘    └──────┘    └──────┘         │
│                                           │              │
│   You type     Python      Python         Back to       │
│   a line       figures     shows          waiting       │
│                it out      the result     for input     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

#### How to open the REPL

Open your terminal and type:

```
python
```

or on Mac/Linux:

```
python3
```

You will see something like this:

```
Python 3.12.4 (main, Jun 6 2024, 18:26:44)
[GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The `>>>` prompt means Python is ready and waiting for your input.

#### How to exit the REPL

Type `exit()` and press Enter, or press `Ctrl+D` (Mac/Linux) / `Ctrl+Z` then Enter (Windows).

---

### 1.6 Playing in the REPL

Once you see `>>>`, try these one at a time. Press Enter after each line.

#### Your first output

```python
>>> print("Hello, World!")
Hello, World!
```

`print()` is a built-in Python function that displays text on the screen. The text you want to display goes inside the parentheses, wrapped in quotes.

#### Python as a calculator

Python can do math directly. No need for `print()` in the REPL — it shows you the result automatically:

```python
>>> 2 + 3
5

>>> 10 - 4
6

>>> 3 * 7
21

>>> 10 / 3
3.3333333333333335

>>> 10 // 3
3

>>> 10 % 3
1

>>> 2 ** 8
256
```

Quick reference for arithmetic operators:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (always gives decimal) | `7 / 2` | `3.5` |
| `//` | Floor division (whole number only) | `7 // 2` | `3` |
| `%` | Modulo (remainder after division) | `7 % 2` | `1` |
| `**` | Exponentiation (power) | `2 ** 10` | `1024` |

#### More REPL experiments

```python
>>> 5 + 3 * 2
11

>>> (5 + 3) * 2
16

>>> print("Python is fun!")
Python is fun!

>>> print(100 + 200)
300
```

> **Notice:** In the REPL, `5 + 3` just shows `8`. But `print(5 + 3)` also shows `8`. In the REPL they look the same — but when you write `.py` scripts (Day 2), you **must** use `print()` to see output. The REPL is special in that it automatically displays values.

---

### Day 1 — Mini Exercises

Try these in the REPL before moving on. No peeking at answers — figure them out by experimenting!

**Exercise 1:** Calculate the number of minutes in a week. (Hint: 7 days × 24 hours × 60 minutes)

**Exercise 2:** What is 2 to the power of 32? (Python can handle very large numbers — try this to see how big they get.)

**Exercise 3:** What is the remainder when you divide 101 by 7? Use the `%` operator. (Hint: if 7 goes into 10 once with 3 left over, the remainder is 3.)

**Exercise 4:** Use `print()` to display your name in the REPL. For example: `print("Guido")`

<details>
<summary>Answers (click to reveal)</summary>

```python
# Exercise 1
>>> 7 * 24 * 60
10080

# Exercise 2
>>> 2 ** 32
4294967296

# Exercise 3
>>> 101 % 7
3

# Exercise 4
>>> print("Your Name Here")
Your Name Here
```
</details>

---

> **Day 1 Recap:** You now know what Python is, have it installed, and can run code in the REPL. Day 2 builds on this by writing permanent files.

---

## Day 2 — Writing Scripts, print() Deep Dive, and Comments

### 2.1 From REPL to Scripts — Why We Need Files

The REPL is great for experimenting, but it has a big limitation: **nothing is saved**. Close the terminal and everything you typed is gone.

Real Python programs are written in `.py` files (called "scripts" or "source files"). You write the instructions once, save them, and can run them any time.

**Analogy:** The REPL is like talking to someone — your words disappear after you say them. A `.py` file is like writing a letter — you write it once, and it can be read and acted upon as many times as you want.

---

### 2.2 Anatomy of a Python Program

A Python file is plain text, read by the interpreter **line by line, top to bottom**.

```
┌─────────────────────────────────────────────────────────┐
│              ANATOMY OF A PYTHON SCRIPT                 │
│                                                         │
│  Line 1:  # This is a comment - Python ignores this     │
│  Line 2:                                                │
│  Line 3:  print("Hello, World!")   <── statement 1      │
│  Line 4:  print("My name is Sam")  <── statement 2      │
│  Line 5:  print(2 + 2)             <── statement 3      │
│                                         │               │
│           Python reads top to bottom ───┘               │
│           Executes each line in order                   │
└─────────────────────────────────────────────────────────┘
```

---

### 2.3 Creating and Running Your First Script

#### Step 1 — Create the file

1. Open VS Code
2. Create a new file: `File > New File` (or `Ctrl+N`)
3. Save it as `hello_world.py` in a folder you can find (like `Desktop/python-practice/`)
4. Make sure the filename ends in `.py` — this tells VS Code and your terminal it is a Python file

#### Step 2 — Write the code

Type this into the file:

```python
print("Hello, World!")
print("Welcome to Python!")
print("This is my first script.")
```

Save the file (`Ctrl+S` or `Cmd+S`).

#### Step 3 — Run from terminal

Open your terminal, navigate to the folder containing your file, and run:

```
python hello_world.py
```

or on Mac/Linux:

```
python3 hello_world.py
```

You should see:

```
Hello, World!
Welcome to Python!
This is my first script.
```

**How to navigate to a folder in the terminal:**

```bash
# Mac/Linux
cd ~/Desktop/python-practice

# Windows
cd C:\Users\YourName\Desktop\python-practice
```

> **VS Code shortcut:** If you have the file open in VS Code, you can right-click in the editor and choose "Run Python File in Terminal". VS Code opens a terminal and runs it for you.

---

### 2.4 The `print()` Function — A Deep Dive

`print()` is one of Python's most used built-in functions. It sends text to the terminal. It is more flexible than it first appears.

#### Basic usage

```python
print("Hello")              # Prints a string
print(42)                   # Prints a number
print(3.14)                 # Prints a decimal
print(True)                 # Prints a boolean
print()                     # Prints a blank line
```

Output:
```
Hello
42
3.14
True

```

(`True` is a boolean and `None` is a special value — both covered in Chapter 02. Just note that Python can print them.)

#### Printing multiple values at once

You can pass multiple things to `print()`, separated by commas. Python adds a space between them by default:

```python
print("My name is", "Alice", "and I am", 25, "years old")
```

Output:
```
My name is Alice and I am 25 years old
```

#### The `sep` parameter — change the separator

By default, `print()` puts a space between multiple values. You can change this with `sep`:

```python
print("2026", "06", "18", sep="-")
print("cat", "dog", "fish", sep=" | ")
print("a", "b", "c", sep="")
```

Output:
```
2026-06-18
cat | dog | fish
abc
```

#### The `end` parameter — change what prints at the end

By default, `print()` adds a newline (`\n`) at the end, which is why each `print()` appears on its own line. You can change this with `end`:

```python
print("Loading", end="")
print("...", end="")
print(" Done!")
```

Output:
```
Loading... Done!
```

Another example — printing items on the same line separated by spaces:

```python
print("apple", end=" ")
print("banana", end=" ")
print("cherry")
```

Output:
```
apple banana cherry
```

#### Escape sequences — special characters in strings

Sometimes you need to print characters that are tricky to type directly:

| Escape sequence | Meaning |
|-----------------|---------|
| `\n` | Newline (go to next line) |
| `\t` | Tab (indent) |
| `\\` | A literal backslash `\` |
| `\"` | A literal double quote `"` |
| `\'` | A literal single quote `'` |

```python
print("Line 1\nLine 2\nLine 3")
print("Name:\tAlice")
print("She said \"Hello!\"")
```

Output:
```
Line 1
Line 2
Line 3
Name:	Alice
She said "Hello!"
```

---

### 2.5 Comments — Talking to Future Readers (Including Yourself)

#### What is a comment?

A **comment** is text in your code that Python completely ignores. It exists for humans — to explain what the code is doing, why a decision was made, or to leave notes.

**Analogy:** Comments are like sticky notes on a piece of paper. They help the reader understand the content, but they are not part of the actual document.

#### Single-line comments

Start with `#`. Everything from `#` to the end of the line is ignored by Python:

```python
# This whole line is a comment
print("Hello")  # This is an inline comment — code runs, then Python ignores the rest

# You can use comments to "disable" code temporarily:
# print("This line won't run")
print("This line will run")
```

#### Multi-line comments

Python does not have a built-in multi-line comment syntax like some other languages. The common approach is to use multiple `#` lines:

```python
# This is line one of a multi-line comment
# This is line two
# This is line three
print("Back to code")
```

There is also a trick using **triple-quoted strings** (`"""..."""` or `'''...'''`). These are technically strings, not comments — but if they are not assigned to a variable, Python evaluates them and immediately discards them. Many programmers use them as block comments:

```python
"""
This is a multi-line string being used
as a block comment. Python creates the
string but throws it away since nobody
stored it.
"""
print("Hello")
```

> **Best practice:** Use `#` for regular comments. Triple-quoted strings are most properly used as **docstrings** — documentation attached to functions and classes (you will learn this in Chapter 07). Relying on this as a comment is considered bad practice — use `#` for all comments.

#### When to write comments

Good comment targets:
- Explain **why** you made a particular choice (not **what** the code does — that should be obvious from the code itself)
- Clarify complex logic
- Mark TODOs and FIXMEs
- Explain a non-obvious formula or algorithm

```python
# Good comment — explains WHY
# We add 1 because humans count from 1, not 0
item_number = index + 1

# Bad comment — just repeats what the code already says
# Print hello
print("hello")
```

---

### 2.6 Putting It All Together — hello_world.py

Here is a well-structured first script combining everything from Day 2:

```python
# hello_world.py
# My very first Python script
# Author: Your Name
# Date: 2026-06-18

# --- Greetings ---
print("Hello, World!")
print("Welcome to Python programming.")

# --- A blank line for visual spacing ---
print()

# --- Using print with multiple values ---
print("Today is:", "Wednesday")

# --- Using sep and end ---
print("Python", "is", "awesome", sep="-")

# --- A multi-line message ---
print("Line 1\nLine 2\nLine 3")
```

---

### Day 2 — Mini Exercises

**Exercise 1:** Write a script that prints your full name on one line, your city on the next line, and your favorite hobby on the third line.

**Exercise 2:** Use a single `print()` statement (with `\n`) to print the following exactly:
```
Monday
Tuesday
Wednesday
```

**Exercise 3:** Print a simple "receipt" that looks like this using `sep` and multiple `print()` calls:
```
Item          Price
--------------------------
Coffee        $3.50
Sandwich      $7.99
--------------------------
Total:        $11.49
```

**Exercise 4:** Write at least 3 comments in your script from Exercise 1 explaining what each section does.

<details>
<summary>Hints for Exercise 3</summary>

- Use spaces or `\t` to align the columns
- **Bonus hint:** To print a row of dashes you can use `print("--------------------------")` (just type 26 dashes), or if you are curious, `print("-" * 26)` does the same thing — you will learn string multiplication properly in Chapter 04.
</details>

<details>
<summary>Sample solution for Exercise 3 (click to reveal)</summary>

```python
print("Item          Price")
print("--------------------------")
print("Coffee        $3.50")
print("Sandwich      $7.99")
print("--------------------------")
print("Total:        $11.49")
```
</details>

---

## Common Mistakes to Avoid

### Mistake 1 — Forgetting parentheses on print

```python
# WRONG — Python 2 style, gives a SyntaxError in Python 3
print "Hello"

# CORRECT
print("Hello")
```

### Mistake 2 — Mismatched quotes

```python
# WRONG — opened with " but closed with '
print("Hello')

# CORRECT — quotes must match
print("Hello")
print('Hello')
```

### Mistake 3 — Wrong filename extension

If you save your file as `hello_world.txt` instead of `hello_world.py`, it will not run as Python.

### Mistake 4 — Running the script from the wrong directory

If your file is in `/Desktop/python-practice/` but your terminal is in `/Desktop/`, running `python hello_world.py` will give a "No such file or directory" error.

**Fix:** Use `cd` to navigate to the correct folder first, or give the full path: `python ~/Desktop/python-practice/hello_world.py`

### Mistake 5 — Confusing `print()` behaviour in REPL vs scripts

In the REPL, just typing `1 + 1` shows `2`. In a script, you must write `print(1 + 1)` — otherwise nothing appears on screen.

### Mistake 6 — Python 2 vs Python 3 confusion

If you see `python` run Python 2.x on your machine, always use `python3` explicitly. The course uses Python 3.

```bash
python --version   # Might show Python 2.x on some systems
python3 --version  # Will show Python 3.x
```

---

## Quick Reference Card

```
┌────────────────────────────────────────────────────────────┐
│                  CHAPTER 01 QUICK REFERENCE                │
│                                                            │
│  Open REPL:          python  (or python3 on Mac/Linux)     │
│  Exit REPL:          exit()  or Ctrl+D                     │
│  Run a script:       python script.py                      │
│                                                            │
│  print basics:                                             │
│    print("text")             → text                        │
│    print(42)                 → 42                          │
│    print("a", "b", "c")      → a b c                      │
│    print("a", "b", sep="-")  → a-b                        │
│    print("hi", end="!")      → hi!  (no newline)           │
│                                                            │
│  Escape sequences:                                         │
│    \n  →  newline                                          │
│    \t  →  tab                                              │
│    \\  →  backslash                                        │
│    \"  →  double quote                                     │
│                                                            │
│  Comments:                                                 │
│    # single line                                           │
│    # multiple                                              │
│    # lines                                                 │
│                                                            │
│  Math operators:                                           │
│    +  -  *  /  //  %  **                                   │
└────────────────────────────────────────────────────────────┘
```

---

## What's Next?

In **Chapter 02 — Variables & Data Types**, you will learn how to store values in named "boxes" (variables), explore Python's core data types (`int`, `float`, `str`, `bool`, `None`), and start building programs that remember information.
