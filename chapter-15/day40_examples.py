"""
Chapter 15 - Day 40: Saving and loading with JSON (add + list)
==============================================================
Today's goal: make our tasks SURVIVE between runs. We do this by writing them
to a file in JSON format, and reading them back later.

JSON is just text that looks like Python dicts/lists. The 'json' module turns
Python objects into that text (dump) and back (load).

This demo writes to a temporary file so it never touches your real tasks.json.
"""

import json
import os
import tempfile


# ============================================================
# 1. A minimal Task (same idea as Day 39)
# ============================================================
class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}

    @staticmethod
    def from_dict(d):
        return Task(d["id"], d["title"], d["done"])

    def __repr__(self):
        mark = "x" if self.done else " "
        return f"#{self.id} [{mark}] {self.title}"


# ============================================================
# 2. SAVE  -  list of Task objects  ->  JSON file
# ============================================================
def save_tasks(tasks, path):
    # JSON can't store Task objects directly, so we convert each to a dict.
    data = [t.to_dict() for t in tasks]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)   # indent=2 -> pretty, readable file


# ============================================================
# 3. LOAD  -  JSON file  ->  list of Task objects
# ============================================================
def load_tasks(path):
    if not os.path.exists(path):
        return []                       # no file yet -> empty list
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)             # data is a list of dicts
    return [Task.from_dict(d) for d in data]


# ============================================================
# 4. DEMO  -  add tasks, save, then load them back
# ============================================================
# Use a temp folder so this demo is self-contained.
demo_file = os.path.join(tempfile.gettempdir(), "demo_tasks.json")

tasks = []
tasks.append(Task(1, "Buy milk"))
tasks.append(Task(2, "Walk the dog", done=True))

print("Saving tasks to:", demo_file)
save_tasks(tasks, demo_file)

print("\nRaw text now inside the file:")
with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read())

print("Loading tasks back from the file:")
loaded = load_tasks(demo_file)
for t in loaded:
    print(" ", t)

# Clean up the demo file so we leave no mess behind.
os.remove(demo_file)
print("\nDay 40 done: tasks now persist to disk and load back.")
