"""
Chapter 09 - Day 24: Reading Files
==================================
Topics: open() and file modes, .read()/.readline()/.readlines(),
        iterating over a file line by line, the 'with' statement
        (context manager) and why it auto-closes files for you.

This script is fully self-contained:
  - It CREATES a sample text file inside this chapter folder,
  - reads it back in several different ways,
  - and finally DELETES the sample file so the folder stays clean.

Run it with:  python3 day24_examples.py
"""

import os

# ------------------------------------------------------------
# Build an absolute path that always points NEXT TO this script,
# no matter what directory you run python3 from.
# __file__ is the path of this .py file; dirname() gives its folder.
# ------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "sample.txt")


# ============================================================
# 0. SETUP - create a sample file so the rest of the demo works
# ============================================================
# We use mode "w" (write) here just to lay down some content.
# Writing is the Day 25 topic; for now think of this as "make a file
# we can read in the examples below".

with open(SAMPLE, "w") as f:
    f.write("Roses are red\n")
    f.write("Violets are blue\n")
    f.write("Python is great\n")
    f.write("And so are you\n")

print(f"Created sample file at: {SAMPLE}\n")


# ============================================================
# 1. open() AND THE PLAIN .read() METHOD
# ============================================================
# open(path, mode) opens a file and returns a "file object".
# Mode "r" means READ (this is also the default if you omit it).
# .read() with no argument returns the ENTIRE file as ONE big string.

f = open(SAMPLE, "r")
whole_text = f.read()
f.close()                      # <-- we MUST close manually when not using 'with'

print("1. Entire file as one string (.read()):")
print(whole_text)
print(f"   (type is {type(whole_text).__name__}, length is {len(whole_text)} chars)\n")


# ============================================================
# 2. THE 'with' STATEMENT - the recommended way
# ============================================================
# 'with open(...) as f:' opens the file and GUARANTEES it gets closed
# at the end of the block - even if an error happens inside.
# This is called a "context manager". You should use it ALWAYS.
#
# Notice: no f.close() needed. Python does it for us.

with open(SAMPLE, "r") as f:
    content = f.read()

print("2. Same file, read inside a 'with' block (auto-closes):")
print(content)


# ============================================================
# 3. .readline() - read ONE line at a time
# ============================================================
# Each call to .readline() returns the next line, INCLUDING its
# trailing newline "\n". When there are no more lines it returns "".

print("3. Reading line-by-line with .readline():")
with open(SAMPLE, "r") as f:
    first = f.readline()
    second = f.readline()
    print(f"   first line  : {first!r}")    # !r shows the \n clearly
    print(f"   second line : {second!r}")
print()


# ============================================================
# 4. .readlines() - read ALL lines into a LIST
# ============================================================
# Returns a list where each element is one line (newline included).

with open(SAMPLE, "r") as f:
    lines = f.readlines()

print("4. .readlines() returns a list of lines:")
print(f"   {lines}")
print(f"   There are {len(lines)} lines in the list.\n")


# ============================================================
# 5. ITERATING OVER A FILE LINE BY LINE (the best way for big files)
# ============================================================
# A file object is "iterable" - you can loop over it directly.
# This reads ONE line at a time, so it works even for huge files
# that would not fit in memory all at once.
# .strip() removes the trailing "\n" (and any surrounding whitespace).

print("5. Looping over the file directly (memory-friendly):")
with open(SAMPLE, "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"   Line {line_number}: {line.strip()}")
print()


# ============================================================
# 6. HANDS-ON - count lines AND words in the file
# ============================================================
# Classic beginner exercise: open a text file and report stats.

line_count = 0
word_count = 0
char_count = 0

with open(SAMPLE, "r") as f:
    for line in f:
        line_count += 1
        words = line.split()          # split() breaks on whitespace -> list of words
        word_count += len(words)
        char_count += len(line)

print("6. Hands-on: file statistics")
print(f"   Lines : {line_count}")
print(f"   Words : {word_count}")
print(f"   Chars : {char_count}\n")


# ============================================================
# 7. FILE MODES - a quick tour (the "r+" read-and-write example)
# ============================================================
# "r+" opens for BOTH reading and writing without truncating the file.
# (We'll cover "w" and "a" in Day 25.)
# Here we just demonstrate that "r+" can read the existing content.

with open(SAMPLE, "r+") as f:
    print("7. Opened with mode 'r+' (read + write). First line is:")
    print(f"   {f.readline().strip()}\n")


# ============================================================
# 8. CLEANUP - remove the sample file we created
# ============================================================
# os.remove() deletes a file. We check it exists first to be safe.

if os.path.exists(SAMPLE):
    os.remove(SAMPLE)
    print(f"8. Cleaned up - deleted {os.path.basename(SAMPLE)}.")
    print("   The chapter folder is tidy again.")
