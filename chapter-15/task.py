"""
Chapter 15 - Task Manager: the Task model and JSON storage
==========================================================
This module is the "data layer" of our app. It knows two things:

  1. What a single task looks like        -> the Task class
  2. How to read/write a list of tasks     -> load_tasks() / save_tasks()

We deliberately keep ALL the "screen output" (print, colors, menus) OUT of
this file. This file only deals with data. That separation is what makes a
program easy to read and easy to change later.

Concepts reused from earlier chapters:
  - Classes & objects        (Chapter 14: OOP)
  - Dictionaries & lists      (Chapter 06 / 08: data structures)
  - File I/O                  (Chapter 12: reading/writing files)
  - The json module          (Chapter 13: modules & standard library)
  - Error handling            (Chapter 11: try/except)
"""

import json
import os
from datetime import datetime


# ============================================================
# WHERE DO WE STORE THE DATA?
# ============================================================
# We build an absolute path that sits NEXT TO this file, so the program
# works no matter which folder you run it from.
#   __file__              -> the path to THIS task.py file
#   os.path.dirname(...)  -> the folder that contains it
#   os.path.join(...)     -> safely glue folder + filename together
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "tasks.json")


# ============================================================
# THE Task CLASS  -  the blueprint for one task
# ============================================================
class Task:
    """
    Represents a single to-do item.

    Attributes:
        id (int):      A unique number for this task.
        title (str):   What needs to be done, e.g. "Buy milk".
        done (bool):   True if completed, False otherwise.
        created (str): When the task was created (ISO timestamp text).
    """

    def __init__(self, id, title, done=False, created=None):
        # 'self' is the specific task object being built right now.
        self.id = id
        self.title = title
        self.done = done
        # If no creation time was given, stamp it with "now".
        self.created = created or datetime.now().isoformat(timespec="seconds")

    # ----- Converting between Task objects and plain dictionaries -----
    # JSON cannot store a Python object directly. It CAN store dictionaries.
    # So we teach our Task how to turn itself into a dict and back.

    def to_dict(self):
        """Turns this Task into a plain dictionary (JSON-friendly)."""
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "created": self.created,
        }

    @staticmethod
    def from_dict(data):
        """Builds a Task back from a dictionary loaded from JSON."""
        return Task(
            id=data["id"],
            title=data["title"],
            done=data.get("done", False),
            created=data.get("created"),
        )

    def __repr__(self):
        # A developer-friendly preview, handy when debugging.
        status = "x" if self.done else " "
        return f"Task(#{self.id} [{status}] {self.title!r})"


# ============================================================
# STORAGE HELPERS  -  load and save the whole list of tasks
# ============================================================
def load_tasks(path=DATA_FILE):
    """
    Reads all tasks from the JSON file and returns a list of Task objects.

    If the file does not exist yet (first run), we simply return an empty
    list instead of crashing. If the file exists but is corrupted, we warn
    and start fresh rather than blow up.
    """
    if not os.path.exists(path):
        return []                      # first run - no file yet, that's fine

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)         # raw is a list of dicts
    except json.JSONDecodeError:
        # The file exists but isn't valid JSON (maybe edited by hand badly).
        print(f"Warning: {path} is corrupted. Starting with an empty list.")
        return []

    # Turn each dict back into a Task object.
    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks, path=DATA_FILE):
    """
    Writes the given list of Task objects to the JSON file.

    'indent=2' makes the file human-readable so you can open tasks.json
    and actually see what's inside.
    """
    data = [task.to_dict() for task in tasks]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def next_id(tasks):
    """
    Works out the next free id. If the list is empty -> start at 1.
    Otherwise -> one higher than the current biggest id.
    """
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
