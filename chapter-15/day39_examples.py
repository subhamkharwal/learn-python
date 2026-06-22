"""
Chapter 15 - Day 39: Project setup, the data model, and argparse intro
======================================================================
Today we plan the shape of the app. Two ideas:

  1. A Task object - the "thing" our app manages.
  2. argparse      - how a program reads commands typed in the terminal.

This file is runnable and self-contained. It does NOT require typing anything
in - we feed argparse a fake command line so the demo just runs.
"""

import argparse


# ============================================================
# 1. THE Task CLASS SKELETON
# ============================================================
# Think of a class as a blueprint. From one blueprint (Task) we can stamp out
# many task objects, each with its own id, title and done-status.

class Task:
    """A single to-do item."""

    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self):
        """A task knows how to describe itself as a dictionary."""
        return {"id": self.id, "title": self.title, "done": self.done}

    def __repr__(self):
        mark = "x" if self.done else " "
        return f"#{self.id} [{mark}] {self.title}"


# Build a couple of tasks and look at them.
t1 = Task(1, "Buy milk")
t2 = Task(2, "Walk the dog", done=True)

print("Two task objects:")
print(" ", t1)
print(" ", t2)
print("As a dictionary:", t1.to_dict())


# ============================================================
# 2. argparse - reading commands from the terminal
# ============================================================
# argparse turns words like:  add "Buy milk"
# into neat Python values you can use. We use SUBCOMMANDS (add/list/...) so
# the one program can do several different jobs.

def build_parser():
    parser = argparse.ArgumentParser(description="Task manager demo")
    subs = parser.add_subparsers(dest="command")

    p_add = subs.add_parser("add", help="Add a task")
    p_add.add_argument("title")

    subs.add_parser("list", help="List tasks")
    return parser


parser = build_parser()

# Normally argparse reads the REAL command line. For a self-running demo we
# hand it a fake list of arguments instead.
print("\nParsing the fake command:  add \"Learn argparse\"")
args = parser.parse_args(["add", "Learn argparse"])
print("  command =", args.command)
print("  title   =", args.title)

print("\nParsing the fake command:  list")
args = parser.parse_args(["list"])
print("  command =", args.command)

print("\nDay 39 done: we have a Task blueprint and we can read commands.")
