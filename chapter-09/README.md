# Chapter 09: File I/O

## Chapter Overview

Up to now, every program you wrote forgot everything the moment it stopped running.
Type some input, see some output, close the program — and it is all gone. That is fine
for a calculator, but real programs need to **remember things between runs**: save your
game progress, keep a list of contacts, log what happened, export a spreadsheet.

That memory lives in **files** on your disk. **File I/O** ("Input/Output") is how your
program reads data *from* files and writes data *to* files.

In this chapter you will learn to:
- **Open** a file and choose the right **mode** (`r`, `w`, `a`, `r+`, `rb`)
- **Read** a file three different ways (`.read()`, `.readline()`, `.readlines()`) and loop over it
- Use the **`with` statement** so files always close themselves (no leaks!)
- **Write** and **append** text with `.write()` and `.writelines()`
- Read and write **CSV** files (spreadsheet-style data) with the `csv` module
- Check and build file paths with **`os.path`**

This chapter spans **2 days**:

| Day | Topics |
|-----|--------|
| Day 24 | `open()`, file modes, `.read()`/`.readline()`/`.readlines()`, iterating, the `with` statement |
| Day 25 | Writing & appending, the `csv` module (reader/writer, DictReader/DictWriter), `os.path` basics |

---

## Day 24: Reading Files

### What Is a File, Really?

A file is just a sequence of bytes stored on your disk with a **name** and a **location
(path)**. A *text file* (`.txt`, `.csv`, `.py`) stores human-readable characters; a
*binary file* (`.png`, `.mp3`, `.zip`) stores raw bytes that only certain programs
understand.

To work with a file in Python you follow three steps:

```
   ┌─────────┐      ┌──────────────┐      ┌──────────┐
   │  OPEN   │ ───▶ │ READ / WRITE │ ───▶ │  CLOSE   │
   └─────────┘      └──────────────┘      └──────────┘
   get a "handle"   do your work          release the handle
   to the file                            back to the OS
```

Forgetting to **close** is a real bug: the operating system limits how many files a
program may have open at once, and on some systems your writes are not actually saved
to disk until the file is closed. Soon you will meet the `with` statement, which closes
files for you automatically — but first, let's see the manual way so you understand what
`with` is doing under the hood.

---

### open() and File Modes

`open()` is the one function that starts it all:

```python
file_object = open("notes.txt", "r")
```

- The **first argument** is the path to the file.
- The **second argument** is the **mode** — a short string saying what you intend to do.

The mode you pick matters a lot, because some modes **erase** your file:

| Mode | Name | If file exists | If file missing | Can read? | Can write? |
|------|------|----------------|-----------------|-----------|------------|
| `"r"` | read (default) | opens it | **error** | yes | no |
| `"w"` | write | **erases it!** | creates it | no | yes |
| `"a"` | append | keeps it, adds to end | creates it | no | yes |
| `"r+"` | read + write | opens it | **error** | yes | yes |
| `"rb"` | read binary | opens it | **error** | yes (as bytes) | no |

A handy picture of where the "cursor" starts and what survives:

```
  "r"   ┌───────────────┐   cursor at START, file untouched
        │ existing data │
        └───────────────┘
         ^cursor

  "w"   ┌───────────────┐   file WIPED first, then written
        │   (empty!)    │
        └───────────────┘
         ^cursor

  "a"   ┌───────────────┐   cursor at END, old data kept
        │ existing data │
        └───────────────┘
                         ^cursor
```

> **Common Mistake: Using `"w"` when you meant `"a"`**
>
> ```python
> # You wanted to ADD a line to your log...
> with open("log.txt", "w") as f:   # WRONG - "w" wipes the whole file first!
>     f.write("new entry\n")
> ```
>
> Mode `"w"` deletes everything already in the file the instant you open it.
> If you want to keep the old content and add to it, use `"a"` (append).

A note on **text vs binary**: by default files open in *text mode* and Python hands you
**strings** (`str`). Add a `b` to the mode (like `"rb"`) for *binary mode*, where you get
raw **bytes** instead — used for images, audio, and other non-text data.

---

### Reading: .read(), .readline(), .readlines()

Once a file is open in a readable mode, there are three classic ways to pull data out.
Imagine a file `poem.txt` containing:

```
Roses are red
Violets are blue
```

```python
f = open("poem.txt", "r")

f.read()        # 'Roses are red\nViolets are blue\n'   ← ONE big string (whole file)
f.readline()    # 'Roses are red\n'                     ← just the NEXT line
f.readlines()   # ['Roses are red\n', 'Violets are blue\n']  ← LIST of all lines

f.close()
```

Side-by-side:

| Method | Returns | Best for |
|--------|---------|----------|
| `.read()` | the entire file as **one string** | small files you want all at once |
| `.read(n)` | the next **n characters** as a string | reading in fixed-size chunks |
| `.readline()` | the **next single line** (string) | processing one line at a time, by hand |
| `.readlines()` | a **list** of all lines | when you want a list to index/loop over |

Notice every line keeps its trailing newline character `\n`. To get rid of it, use
`.strip()`:

```python
line = "Roses are red\n"
print(line.strip())     # 'Roses are red'  (newline removed)
```

---

### The Best Way to Read: Just Loop Over the File

You rarely need `.read()` or `.readlines()`. A file object is **iterable**, so the
cleanest, most memory-friendly approach is to loop over it directly — it reads **one line
at a time**, so it works even on a 10 GB file that would never fit in memory:

```python
with open("poem.txt", "r") as f:
    for line in f:                 # one line per loop, automatically
        print(line.strip())
```

Add line numbers with `enumerate`:

```python
with open("poem.txt", "r") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.strip()}")
```

---

### The `with` Statement — and WHY It Matters

Look at all the manual examples above: every one ends with `f.close()`. It is easy to
forget — and if an error happens *before* you reach `close()`, the file never closes at
all.

The **`with` statement** solves this. It is a **context manager**: it opens the file,
runs your block, and **guarantees the file is closed** when the block ends — even if your
code crashes mid-way.

```python
# The old, fragile way
f = open("poem.txt", "r")
data = f.read()
f.close()            # easy to forget; skipped entirely if an error is raised above

# The modern, safe way — ALWAYS prefer this
with open("poem.txt", "r") as f:
    data = f.read()
# file is automatically closed right here, no matter what happened inside
```

```
  with open(...) as f:
  ┌──────────────────────────────────────────┐
  │  ...your code uses f...                   │
  │  (even if this code raises an exception)  │
  └──────────────────────────────────────────┘
        │
        ▼
  file.close() called for you, guaranteed
```

> **Common Mistake: Reading from a file that is already exhausted**
>
> ```python
> with open("poem.txt") as f:
>     print(f.read())    # reads everything, cursor now at END
>     print(f.read())    # prints '' — there's nothing left to read!
> ```
>
> A file has a single moving "cursor". Once you have read to the end, further reads
> return empty. Read it once into a variable, or re-open the file, or use `f.seek(0)`
> to rewind the cursor to the start.

---

### Hands-on Day 24

**Read the whole file at once:**
```python
with open("poem.txt", "r") as f:
    print(f.read())
```

**Read line by line and number each line:**
```python
with open("poem.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")
```

**Count lines and words in a file:**
```python
line_count = 0
word_count = 0

with open("poem.txt", "r") as f:
    for line in f:
        line_count += 1
        word_count += len(line.split())   # split() -> list of words

print(f"Lines: {line_count}, Words: {word_count}")
```

`split()` with no argument breaks a string on any run of whitespace and returns a list
of words, so `len(line.split())` is the number of words on that line.

---

### Day 24 Mini Exercises

1. Create a small text file by hand (or with `"w"` mode), then write a program that prints
   it back out with line numbers, like `1: first line`.
2. Write a function `count_chars(path)` that returns how many characters are in a file.
3. Read a file with `.readlines()` and print the lines in **reverse** order. (Hint: lists
   have a `.reverse()` method, or use slicing `lines[::-1]`.)
4. Write a program that prints **only the longest line** in a file.
5. **Bonus:** Explain in one sentence why looping `for line in f:` is better than
   `f.readlines()` for a 5 GB log file.

> **Common Mistake: Opening a file that does not exist in read mode**
>
> ```python
> with open("does_not_exist.txt", "r") as f:   # FileNotFoundError!
>     ...
> ```
>
> Mode `"r"` requires the file to already exist. Before reading, you can check with
> `os.path.exists(path)` (you'll meet that in Day 25), or handle the error with
> `try`/`except` (a later chapter).

---

## Day 25: Writing Files, CSV, and os.path

### Writing Text: .write() and .writelines()

To put data *into* a file, open it in a writable mode (`"w"` or `"a"`) and call `.write()`:

```python
with open("greeting.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

Two things every beginner must internalize about `.write()`:

1. It takes a **string** — write `str(42)`, not the number `42`.
2. It adds **no newline** for you. If you want lines, put `\n` yourself.

```python
# WITHOUT \n everything runs together on one line:
f.write("Hello")
f.write("World")        # file contains:  HelloWorld

# WITH \n you get separate lines:
f.write("Hello\n")
f.write("World\n")      # file contains:  Hello
                        #                 World
```

`.writelines()` writes a **list of strings** in one call — but, surprisingly, it *also*
does not add newlines. Each string must already include its own `\n`:

```python
lines = ["first\n", "second\n", "third\n"]
with open("out.txt", "w") as f:
    f.writelines(lines)        # note: NOT "write_lines", and NO auto newlines
```

> **Common Mistake: Expecting `.writelines()` to add line breaks**
>
> ```python
> f.writelines(["a", "b", "c"])   # file contains:  abc   (all on one line!)
> ```
>
> Despite the name, `.writelines()` does not insert `\n`. Build your list with the
> newlines already in each string: `["a\n", "b\n", "c\n"]`.

---

### "w" vs "a" — Write vs Append

This is the single most important distinction when writing:

```
  Mode "w"  (write)              Mode "a"  (append)
  ────────────────────          ────────────────────
  ERASES the file first         KEEPS existing content
  then writes from empty        then adds to the END

  Run it twice →                Run it twice →
  file has ONLY the             file has BOTH runs'
  last run's data               data, stacked up
```

Use `"w"` to (re)generate a fresh file each time. Use `"a"` for logs and anything where
each run should *add* to history rather than replace it.

**Hands-on — a tiny log file:**
```python
with open("app.log", "w") as f:        # start fresh
    f.write("Application started\n")

with open("app.log", "a") as f:        # add entries over time
    f.write("User logged in\n")
    f.write("Application stopped\n")
```

---

### CSV Files and the `csv` Module

**CSV** stands for **Comma-Separated Values**. It is the universal plain-text format for
tables — every spreadsheet program (Excel, Google Sheets) can open and save it. Each
**row** is one line; each **column** is separated by a comma:

```
name,score        ← header row (column names)
Alice,90
Bob,75
Charlie,82
```

You *could* split each line on commas yourself, but real CSV files have tricky edge cases
(commas inside quoted text, newlines inside a field). Python's built-in **`csv` module**
handles all of that correctly, so always use it.

> **Common Mistake: Forgetting `newline=""` when opening a CSV**
>
> ```python
> # On Windows this can insert blank lines between rows:
> with open("scores.csv", "w") as f:        # missing newline=""
>     ...
> # CORRECT:
> with open("scores.csv", "w", newline="") as f:
>     ...
> ```
>
> The `csv` module manages line endings itself. Always open CSV files with `newline=""`
> so it can do that correctly on every operating system.

#### Writing CSV: `csv.writer`

```python
import csv

with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])       # write ONE row (a list)
    writer.writerow(["Alice", 90])
    writer.writerows([["Bob", 75],           # write MANY rows at once
                      ["Charlie", 82]])
```

#### Reading CSV: `csv.reader`

`csv.reader` gives you each row as a **list of strings**. Numbers come back as text, so
convert them yourself with `int()` or `float()`:

```python
import csv

with open("scores.csv", "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)            # pull off the first row (the header)
    for row in reader:
        name = row[0]
        score = int(row[1])          # "90" (string) -> 90 (number)
        print(name, score)
```

#### `DictWriter` / `DictReader` — work with dictionaries instead of lists

Lists force you to remember "column 0 is name, column 1 is score". Dictionaries let you
use **column names** instead, which is far more readable.

```python
import csv

people = [
    {"name": "Dana", "score": 88},
    {"name": "Eve",  "score": 95},
]

# WRITE dicts -> CSV
with open("scores.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()             # writes the header row for you
    writer.writerows(people)

# READ CSV -> dicts (uses the header row as keys)
with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "->", row["score"])
```

Quick comparison:

| Tool | Each row is a... | Access columns by |
|------|------------------|-------------------|
| `csv.reader` / `csv.writer` | **list** | position: `row[0]`, `row[1]` |
| `csv.DictReader` / `csv.DictWriter` | **dict** | name: `row["name"]` |

---

### os.path Basics

When you hard-code paths like `"data/scores.csv"`, your program may break on a different
operating system (Windows uses `\`, macOS/Linux use `/`) or when run from a different
folder. The **`os.path`** module builds and inspects paths safely.

```python
import os

os.path.exists("scores.csv")          # -> True / False : does the path exist?
os.path.join("data", "reports", "q1.csv")
                                       # -> "data/reports/q1.csv" (correct separators)
os.path.basename("/home/me/scores.csv")
                                       # -> "scores.csv" (just the file name)
```

| Function | What it does | Example result |
|----------|--------------|----------------|
| `os.path.exists(p)` | Does the file/folder exist? | `True` |
| `os.path.join(a, b, ...)` | Glue path parts with the right separator | `"data/q1.csv"` |
| `os.path.basename(p)` | The final file name, no folders | `"q1.csv"` |
| `os.path.dirname(p)` | The folder part, no file name | `"/home/me"` |

A pattern you will use constantly — make a path **relative to the script itself** so it
works no matter where you run `python3` from:

```python
import os

HERE = os.path.dirname(os.path.abspath(__file__))   # folder this script lives in
data_path = os.path.join(HERE, "scores.csv")         # always next to the script
```

> **Common Mistake: Assuming the "current directory" is the script's folder**
>
> Paths like `open("scores.csv")` are relative to wherever you *ran* the program from,
> not where the `.py` file lives. Run the same script from a different folder and it
> can no longer find the file. Build absolute paths with `os.path.join(HERE, ...)` to
> avoid the surprise.

---

### Hands-on Day 25

**Write a log file, then append to it:**
```python
with open("app.log", "w") as f:
    f.write("Started\n")

with open("app.log", "a") as f:
    f.write("Did some work\n")
    f.write("Finished\n")
```

**Write and read back a CSV of names and scores:**
```python
import csv

# write
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows([["Alice", 90], ["Bob", 75]])

# read and compute the average
total = 0
count = 0
with open("scores.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["score"])
        count += 1

print(f"Average score: {total / count}")
```

---

### Day 25 Mini Exercises

1. Write a program that asks the user for 3 lines of text and saves them to `notes.txt`
   (one per line). Then read the file back and print it.
2. Write a function `log(message, path="app.log")` that **appends** a message plus a
   newline to a log file. Call it several times and inspect the file.
3. Create a CSV with columns `name, age, city` for 3 people using `csv.DictWriter`,
   then read it back with `csv.DictReader` and print one sentence per person:
   `"Alice is 30 and lives in NYC."`
4. Write a program that reads `scores.csv` and prints the name of the person with the
   **highest** score.
5. Use `os.path` to check whether `scores.csv` exists; if it does, print its base name;
   if not, print "no scores yet".

---

## Quick Reference Card

```
OPENING FILES
  with open(path, mode) as f:      # ALWAYS use 'with' - it auto-closes
      ...

FILE MODES
  "r"   read       (default; file must exist)
  "w"   write      (ERASES file first, or creates it)
  "a"   append     (adds to END, or creates it)
  "r+"  read+write (file must exist, not truncated)
  "rb"  read binary (bytes, not text)

READING
  f.read()          -> whole file as one string
  f.read(n)         -> next n characters
  f.readline()      -> next single line (string)
  f.readlines()     -> list of all lines
  for line in f:    -> loop one line at a time (best for big files)
  line.strip()      -> remove the trailing "\n"

WRITING
  f.write("text\n")          # takes a string; NO auto newline
  f.writelines([...])        # list of strings; NO auto newline

CSV MODULE  (always open with newline="")
  import csv
  csv.writer(f).writerow([...])        # row from a list
  csv.writer(f).writerows([[...], ...])
  csv.reader(f)                        # rows -> lists of strings
  csv.DictWriter(f, fieldnames=[...])  # .writeheader(), .writerow(dict)
  csv.DictReader(f)                    # rows -> dicts keyed by header

OS.PATH
  os.path.exists(p)     -> True/False
  os.path.join(a, b)    -> "a/b" with correct separator
  os.path.basename(p)   -> file name only
  os.path.dirname(p)    -> folder only
  HERE = os.path.dirname(os.path.abspath(__file__))   # script's own folder
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — all lesson notes for Days 24–25 |
| `day24_examples.py` | Runnable code: open(), modes, read/readline/readlines, iterating, `with`, count lines/words |
| `day25_examples.py` | Runnable code: write/append, `.writelines()`, csv reader/writer, DictReader/DictWriter, os.path |
