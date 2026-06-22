"""
Chapter 09 - Day 25: Writing Files, CSV, and os.path
====================================================
Topics: writing & appending with .write()/.writelines(),
        the csv module (reader, writer, DictReader, DictWriter),
        and os.path basics (exists, join, basename).

This script is fully self-contained:
  - It WRITES a log file and a CSV file inside this chapter folder,
  - reads them back to prove they worked,
  - and DELETES them at the end so the folder stays clean.

Run it with:  python3 day25_examples.py
"""

import os
import csv

# Build absolute paths that sit next to this script.
HERE = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(HERE, "app.log")
SCORES_CSV = os.path.join(HERE, "scores.csv")
SCORES_DICT_CSV = os.path.join(HERE, "scores_dict.csv")


# ============================================================
# 1. WRITING A FILE WITH MODE "w"
# ============================================================
# Mode "w" (write):
#   - CREATES the file if it does not exist
#   - TRUNCATES (empties) the file if it DOES exist  <-- be careful!
# .write() takes a string and does NOT add a newline for you,
# so we add "\n" ourselves where we want line breaks.

with open(LOG_FILE, "w") as f:
    f.write("Application started\n")
    f.write("Loading configuration\n")

print("1. Wrote 2 lines to the log with mode 'w'.")


# ============================================================
# 2. APPENDING WITH MODE "a"
# ============================================================
# Mode "a" (append):
#   - CREATES the file if it does not exist
#   - ADDS to the END of the file without erasing what's there
# Perfect for log files where each run adds new entries.

with open(LOG_FILE, "a") as f:
    f.write("User logged in\n")
    f.write("Application stopped\n")

print("2. Appended 2 more lines with mode 'a'.")


# ============================================================
# 3. .writelines() - write a LIST of strings at once
# ============================================================
# IMPORTANT: .writelines() does NOT add newlines automatically.
# Each string must already contain its own "\n" if you want
# separate lines.

extra_lines = [
    "Cleanup task started\n",
    "Cleanup task finished\n",
]
with open(LOG_FILE, "a") as f:
    f.writelines(extra_lines)

print("3. Used .writelines() to append a list of lines.\n")


# ------------------------------------------------------------
# Read the log back so we can SEE the result of steps 1-3.
# ------------------------------------------------------------
print("   Final contents of app.log:")
with open(LOG_FILE, "r") as f:
    for line in f:
        print(f"      {line.strip()}")
print()


# ============================================================
# 4. WRITING A CSV WITH csv.writer
# ============================================================
# CSV = Comma-Separated Values. A plain-text table where each row
# is a line and columns are separated by commas.
#
# IMPORTANT: open CSV files with newline="" so the csv module can
# handle line endings correctly on every operating system.

rows = [
    ["name", "score"],     # header row
    ["Alice", 90],
    ["Bob", 75],
    ["Charlie", 82],
]

with open(SCORES_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])    # write ONE row
    writer.writerows(rows[1:])            # write MANY rows at once

print("4. Wrote scores.csv with csv.writer.")


# ============================================================
# 5. READING A CSV WITH csv.reader
# ============================================================
# csv.reader yields each row as a LIST of strings.
# Note: numbers come back as STRINGS ("90"), so convert if needed.

print("5. Reading scores.csv with csv.reader:")
with open(SCORES_CSV, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)                 # grab the first row as the header
    print(f"   Header: {header}")
    for row in reader:
        name = row[0]
        score = int(row[1])               # convert text "90" -> number 90
        print(f"   {name} scored {score}")
print()


# ============================================================
# 6. csv.DictWriter - write rows from DICTIONARIES
# ============================================================
# DictWriter lets you work with dicts instead of bare lists, which
# is far more readable. You must declare the column names up front
# via fieldnames.

people = [
    {"name": "Dana", "score": 88},
    {"name": "Eve", "score": 95},
]

with open(SCORES_DICT_CSV, "w", newline="") as f:
    fieldnames = ["name", "score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()                  # writes the header row automatically
    writer.writerows(people)

print("6. Wrote scores_dict.csv with csv.DictWriter.")


# ============================================================
# 7. csv.DictReader - read rows AS DICTIONARIES
# ============================================================
# DictReader uses the header row as keys, so each row becomes a dict
# like {"name": "Dana", "score": "88"}. Access columns by name.

print("7. Reading scores_dict.csv with csv.DictReader:")
with open(SCORES_DICT_CSV, "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"   {row['name']} -> {row['score']}")
print()


# ============================================================
# 8. os.path BASICS - exists, join, basename
# ============================================================
# os.path.exists(path)   -> True/False, does the path exist?
# os.path.join(a, b)     -> joins parts with the correct separator
# os.path.basename(path) -> just the file name, no folders

print("8. os.path basics:")
print(f"   os.path.exists(LOG_FILE)      -> {os.path.exists(LOG_FILE)}")
print(f"   os.path.basename(SCORES_CSV)  -> {os.path.basename(SCORES_CSV)}")
joined = os.path.join("data", "reports", "q1.csv")
print(f"   os.path.join('data','reports','q1.csv') -> {joined}\n")


# ============================================================
# 9. CLEANUP - remove every file we created
# ============================================================
for path in (LOG_FILE, SCORES_CSV, SCORES_DICT_CSV):
    if os.path.exists(path):
        os.remove(path)
        print(f"9. Cleaned up - deleted {os.path.basename(path)}.")

print("   All done. Chapter folder is tidy again.")
