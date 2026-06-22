#!/usr/bin/env python3
"""
Chapter 15 - Personal Task Manager (CLI)
========================================
This is the MAIN program - the "front door" of the app. You run it from a
terminal like this:

    python3 task_manager.py add "Buy milk"
    python3 task_manager.py list
    python3 task_manager.py complete 1
    python3 task_manager.py delete 1

It uses 'argparse' (Python's standard command-line parser) to understand the
words you type. All the data work (saving/loading) lives in task.py, so this
file is mostly about: reading commands -> doing the action -> printing nicely.

Concepts reused from earlier chapters:
  - Functions               (Chapter 07)
  - Conditionals & loops    (Chapter 04 / 05)
  - The argparse module     (Chapter 13: standard library)
  - try/except error handling (Chapter 11)
  - Importing our own module (Chapter 13)
"""

import argparse
import sys

from task import Task, load_tasks, save_tasks, next_id


# ============================================================
# COLORS  -  tiny ANSI helpers for friendlier output
# ============================================================
# ANSI escape codes are special text sequences terminals understand as
# "change the color". We wrap them in helpers so the rest of the code stays
# clean. (For a cross-platform library, see 'colorama' - mentioned in README.)
class C:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


def color(text, code):
    """Wrap text in a color code, then reset back to normal."""
    return f"{code}{text}{C.RESET}"


# ============================================================
# COMMAND HANDLERS  -  one function per command
# ============================================================
def cmd_add(title):
    """Adds a new task with the given title."""
    title = title.strip()
    if not title:
        print(color("Error: task title cannot be empty.", C.RED))
        return 1

    tasks = load_tasks()
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)
    save_tasks(tasks)
    print(color(f"Added task #{task.id}: {task.title}", C.GREEN))
    return 0


def cmd_list(show_all=True):
    """Prints all tasks in a tidy table."""
    tasks = load_tasks()
    if not tasks:
        print(color("No tasks yet. Add one with: ", C.YELLOW)
              + 'python3 task_manager.py add "My first task"')
        return 0

    print(color("\n  ID   STATUS    TASK", C.BOLD))
    print("  " + "-" * 40)
    for t in tasks:
        if t.done:
            mark = color("[done]", C.GREEN)
            title = color(t.title, C.DIM)
        else:
            mark = color("[ todo]", C.YELLOW)
            title = t.title
        print(f"  {t.id:<4} {mark}   {title}")
    print()

    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    print(color(f"  {done}/{total} completed.\n", C.CYAN))
    return 0


def cmd_complete(task_id):
    """Marks the task with the given id as done."""
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            if t.done:
                print(color(f"Task #{task_id} is already completed.", C.YELLOW))
                return 0
            t.done = True
            save_tasks(tasks)
            print(color(f"Completed task #{task_id}: {t.title}", C.GREEN))
            return 0

    print(color(f"Error: no task found with id {task_id}.", C.RED))
    return 1


def cmd_delete(task_id):
    """Removes the task with the given id."""
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(color(f"Deleted task #{task_id}: {t.title}", C.GREEN))
            return 0

    print(color(f"Error: no task found with id {task_id}.", C.RED))
    return 1


# ============================================================
# ARGUMENT PARSER  -  describes the commands the program accepts
# ============================================================
def build_parser():
    """Creates and configures the argparse parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="task_manager.py",
        description="A simple personal task manager that saves to tasks.json.",
    )
    # Subparsers let us have separate 'verbs': add / list / complete / delete.
    subs = parser.add_subparsers(dest="command")

    p_add = subs.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="The task description, e.g. \"Buy milk\"")

    subs.add_parser("list", help="List all tasks")

    p_done = subs.add_parser("complete", help="Mark a task as done")
    p_done.add_argument("id", type=int, help="The id of the task to complete")

    p_del = subs.add_parser("delete", help="Delete a task")
    p_del.add_argument("id", type=int, help="The id of the task to delete")

    return parser


# ============================================================
# MAIN  -  glue everything together
# ============================================================
def main(argv=None):
    """
    Entry point. We accept 'argv' as a parameter (defaulting to the real
    command line) so that tests can call main(["add", "Test"]) directly.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    # No command given -> show the help text instead of doing nothing.
    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "add":
        return cmd_add(args.title)
    if args.command == "list":
        return cmd_list()
    if args.command == "complete":
        return cmd_complete(args.id)
    if args.command == "delete":
        return cmd_delete(args.id)

    parser.print_help()
    return 0


if __name__ == "__main__":
    # sys.exit forwards our return code (0 = success, 1 = error) to the shell.
    sys.exit(main())
