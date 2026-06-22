# Chapter 15: Capstone Project — Personal Task Manager (CLI)

## Chapter Overview

You made it. This is the final chapter — the one where all fourteen chapters
before it come together into a single, real program you can actually use and
share with friends.

So far you have learned the *pieces*: variables, conditionals, loops,
functions, data structures, file I/O, error handling, modules, and OOP. A
beginner learns the pieces. A developer **assembles them into something
useful.** That is exactly what this chapter does.

We are going to build a **Personal Task Manager** — a command-line app that
remembers your to-do list between runs. You type commands like:

```
python3 task_manager.py add "Buy milk"
python3 task_manager.py list
python3 task_manager.py complete 1
python3 task_manager.py delete 1
```

...and the tasks are saved to a `tasks.json` file so they're still there
tomorrow.

This chapter spans **4 days**:

| Day | Topics |
|-----|--------|
| Day 39 | Project setup, plan the architecture, the data model, `argparse` intro |
| Day 40 | Implement `add` and `list`, save/load with JSON persistence |
| Day 41 | Implement `complete` and `delete`, error handling throughout |
| Day 42 | Polish: colored output, input validation, final testing, project README |

### Which earlier chapters power this project?

This is the payoff. Every box below is a concept you already learned:

```
  ┌──────────────────────────────────────────────────────────────┐
  │  PERSONAL TASK MANAGER                                         │
  │                                                                │
  │  Functions ......... Ch 07  (cmd_add, cmd_list, save_tasks...) │
  │  Conditionals ...... Ch 04  (if task found / not found)        │
  │  Loops ............. Ch 05  (for t in tasks: ...)              │
  │  Lists & dicts ..... Ch 06/08 (the task list, to_dict())      │
  │  File I/O .......... Ch 12  (open(), read/write tasks.json)    │
  │  Error handling .... Ch 11  (try/except for bad files & ids)   │
  │  Modules ........... Ch 13  (json, argparse, our own task.py)  │
  │  Classes / OOP ..... Ch 14  (the Task class)                   │
  └──────────────────────────────────────────────────────────────┘
```

---

## Day 39: Project Setup, Architecture, and the Data Model

### Step 1 — Think before you type

Professional developers plan first. Before writing code we answer three
questions:

1. **What does the app do?** Store a list of tasks; add, list, complete, delete.
2. **What is the "thing" we manage?** A *task*. Each task has an id, a title,
   a done/not-done flag, and a created date.
3. **Where does the data live?** In a `tasks.json` file on disk, so it survives
   after the program closes.

### Step 2 — File structure (separation of concerns)

We split the program into two files, each with one job. This is called
**separation of concerns** — keep the "what is a task / how is it stored" part
away from the "what does the user see" part.

```
chapter-15/
│
├── task.py            ← the DATA layer: the Task class + JSON load/save
├── task_manager.py    ← the APP layer: argparse + commands + colored output
├── tasks.json         ← created at runtime; your saved tasks
│
├── day39_examples.py  ← argparse demo + Task skeleton
├── day40_examples.py  ← json save/load demo
├── day41_examples.py  ← complete/delete + error handling demo
├── day42_examples.py  ← colors + input validation demo
└── README.md          ← this file
```

Why two files instead of one big one? Because if you later want to store tasks
in a database instead of a file, you only touch `task.py`. The command code in
`task_manager.py` doesn't even need to know. Small, focused files are easier to
read, test, and change.

### Step 3 — The data model: the `Task` class

A **class** (Chapter 14) is a blueprint. From the one `Task` blueprint we can
make as many task objects as we like, each carrying its own data:

```
        Task BLUEPRINT                  Task OBJECTS made from it
   ┌──────────────────────┐         ┌─────────────────────────────┐
   │  id                   │   ───►  │  #1 [ ] "Buy milk"           │
   │  title                │   ───►  │  #2 [x] "Walk the dog"       │
   │  done                 │   ───►  │  #3 [ ] "Read a book"        │
   │  created              │         └─────────────────────────────┘
   └──────────────────────┘
```

```python
class Task:
    def __init__(self, id, title, done=False, created=None):
        self.id = id
        self.title = title
        self.done = done
        self.created = created or datetime.now().isoformat(timespec="seconds")
```

### Step 4 — The JSON persistence design

JSON cannot store a Python *object* directly — it stores plain text that looks
like dictionaries and lists. So we give the `Task` two translation methods:

```
   Task object  ──.to_dict()──►   {"id":1,"title":"Buy milk","done":false}
   Task object  ◄─.from_dict()──  {"id":1,"title":"Buy milk","done":false}
```

The whole file is just a **list of these dictionaries**:

```json
[
  {"id": 1, "title": "Buy milk", "done": false, "created": "2026-06-19T09:00:00"},
  {"id": 2, "title": "Walk the dog", "done": true,  "created": "2026-06-19T09:01:00"}
]
```

### Step 5 — `argparse` intro

`argparse` is a standard-library module (Chapter 13) that reads the words you
type after the program name and turns them into Python values. We use
**subcommands** so one program can do several jobs:

```
  python3 task_manager.py   add   "Buy milk"
  └──────────┬───────────┘  └┬┘   └────┬────┘
         program          subcommand  argument
```

```python
parser = argparse.ArgumentParser()
subs = parser.add_subparsers(dest="command")
p_add = subs.add_parser("add")
p_add.add_argument("title")          # the text after "add"
args = parser.parse_args()           # reads the real command line
# args.command == "add", args.title == "Buy milk"
```

### Hands-on Day 39

Run the day's demo — it builds Task objects and parses fake commands without
needing you to type anything:

```bash
python3 day39_examples.py
```

> **Common Mistake: Forgetting `dest="command"`**
>
> ```python
> subs = parser.add_subparsers()            # no dest!
> ...
> if args.command == "add":                 # AttributeError later
> ```
>
> Always add `dest="command"` so you can later ask "which subcommand did the
> user pick?" via `args.command`.

---

## Day 40: Implement `add` and `list` with JSON Persistence

### Saving: Python objects → JSON text

`json.dump()` writes Python data into a file as JSON text. Because it can't
handle our `Task` objects, we first convert each one to a dict:

```python
def save_tasks(tasks, path):
    data = [task.to_dict() for task in tasks]   # list of Task -> list of dict
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)            # indent=2 -> human readable
```

The `with open(...)` form (Chapter 12) auto-closes the file even if something
goes wrong. `indent=2` makes `tasks.json` nicely formatted so you can open it
and read it yourself.

### Loading: JSON text → Python objects

`json.load()` reads the file back into a list of dicts; we then rebuild each
dict into a real `Task`:

```python
def load_tasks(path):
    if not os.path.exists(path):
        return []                                # first run -> empty list
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task.from_dict(item) for item in data]
```

```
   ON DISK (tasks.json)            IN MEMORY (Python)
   ┌─────────────────────┐  load   ┌─────────────────────┐
   │ [{"id":1,...},      │ ──────► │ [Task(1,...),        │
   │  {"id":2,...}]      │ ◄────── │  Task(2,...)]        │
   └─────────────────────┘  save   └─────────────────────┘
```

### Working out the next id

Each task needs a unique id. The rule: empty list → start at 1; otherwise one
more than the biggest existing id.

```python
def next_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
```

### The `add` command

```python
def cmd_add(title):
    tasks = load_tasks()                  # 1. read current tasks
    task = Task(id=next_id(tasks), title=title)
    tasks.append(task)                    # 2. add the new one
    save_tasks(tasks)                     # 3. write it all back
    print(f"Added task #{task.id}: {task.title}")
```

The pattern is always **load → change → save**. Because we save immediately,
nothing is ever lost.

### Hands-on Day 40

```bash
python3 day40_examples.py            # see save/load in action on a temp file

# Then use the real app:
python3 task_manager.py add "Buy milk"
python3 task_manager.py add "Walk the dog"
python3 task_manager.py list
```

> **Common Mistake: Forgetting to save after changing**
>
> ```python
> tasks.append(task)        # changed the list in memory...
> # ...forgot save_tasks(tasks) — the change vanishes when the program ends!
> ```
>
> In a CLI app each run starts fresh, so an in-memory change that isn't saved
> to disk is gone the moment the program exits. Always save after a change.

---

## Day 41: `complete`, `delete`, and Error Handling Everywhere

### The `complete` command

Find the task by id, flip `done` to `True`, save. If no task matches, say so
calmly instead of crashing.

```python
def cmd_complete(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_tasks(tasks)
            print(f"Completed task #{task_id}: {t.title}")
            return 0
    print(f"Error: no task found with id {task_id}.")   # graceful, no crash
    return 1
```

### The `delete` command

Same idea, but `tasks.remove(t)` drops the task from the list:

```python
def cmd_delete(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Deleted task #{task_id}: {t.title}")
            return 0
    print(f"Error: no task found with id {task_id}.")
    return 1
```

### Error handling: think "what could go wrong?"

A polished program never shows a scary red traceback to the user. For every
action, ask "what could go wrong?" and handle it:

| What could go wrong | How we handle it |
|---------------------|------------------|
| `tasks.json` doesn't exist yet (first run) | `load_tasks` returns `[]` |
| `tasks.json` is corrupted / not valid JSON | catch `JSONDecodeError`, warn, start fresh |
| User asks to complete/delete an id that doesn't exist | print a clear "no task found" message |
| User types text instead of a number for the id | `argparse type=int` rejects it before our code runs |
| User adds an empty title | `cmd_add` checks and refuses |

The corrupted-file guard lives in `task.py`:

```python
try:
    raw = json.load(f)
except json.JSONDecodeError:
    print(f"Warning: {path} is corrupted. Starting with an empty list.")
    return []
```

### Hands-on Day 41

```bash
python3 day41_examples.py                 # see CRUD + error handling demo

python3 task_manager.py complete 1        # mark task 1 done
python3 task_manager.py delete 2          # delete task 2
python3 task_manager.py complete 999      # graceful "no task found"
python3 task_manager.py delete abc        # argparse rejects non-numbers
```

> **Common Mistake: Modifying a list while looping over it**
>
> ```python
> for t in tasks:
>     if t.done:
>         tasks.remove(t)   # changing the list mid-loop skips items!
> ```
>
> In our `delete` we `return` immediately after `remove`, so the loop stops
> right away — safe. But if you ever need to remove *several* items, build a
> new list instead: `tasks = [t for t in tasks if not t.done]`.

---

## Day 42: Polish — Colors, Validation, Testing, and the README

### Colored output with ANSI codes

A terminal understands special text sequences called **ANSI escape codes** as
"change the color". We wrap them in tiny helpers so the rest of the code stays
clean:

```python
GREEN = "\033[92m"
RED   = "\033[91m"
RESET = "\033[0m"          # always reset back to normal afterwards

def color(text, code):
    return f"{code}{text}{RESET}"

print(color("Added task!", GREEN))    # shows in green
```

```
  \033[92m   Added task!   \033[0m
  └───┬───┘  └────┬────┘  └──┬──┘
  start green   your text   reset
```

> **`colorama` for cross-platform color**
>
> Plain ANSI codes work in macOS/Linux terminals and modern Windows ones. For
> guaranteed colors everywhere, install `colorama`:
> ```bash
> pip install colorama
> ```
> ```python
> import colorama
> colorama.init()           # makes ANSI codes work on older Windows too
> ```

### Input validation: never trust input blindly

Always **clean** input, then **check** it:

```python
def clean_title(raw):
    title = raw.strip()              # remove stray spaces
    if not title:                    # empty after cleaning?
        return None                  # reject it
    return title
```

In the real app, `cmd_add` strips the title and refuses empty ones, so you can
never create a blank task.

### Final testing checklist

Run through every command and confirm the JSON file updates correctly:

```bash
python3 task_manager.py add "Buy milk"     # add
python3 task_manager.py add "Walk the dog"
python3 task_manager.py list               # see both, both "todo"
python3 task_manager.py complete 1         # mark #1 done
python3 task_manager.py list               # #1 now shows "done"
python3 task_manager.py delete 2           # remove #2
python3 task_manager.py list               # only #1 left
cat tasks.json                             # confirm the file matches
```

### Hands-on Day 42

```bash
python3 day42_examples.py        # see colors and validation demos
```

---

## Project Usage (the "shareable" README section)

> **Personal Task Manager** — a tiny command-line to-do app written in pure
> Python. No installation needed beyond Python 3.

### Commands

| Command | What it does | Example |
|---------|--------------|---------|
| `add "<title>"` | Add a new task | `python3 task_manager.py add "Buy milk"` |
| `list` | Show all tasks with status | `python3 task_manager.py list` |
| `complete <id>` | Mark a task as done | `python3 task_manager.py complete 1` |
| `delete <id>` | Remove a task | `python3 task_manager.py delete 1` |
| *(no command)* | Show help | `python3 task_manager.py` |

### Example session

```bash
$ python3 task_manager.py add "Buy milk"
Added task #1: Buy milk

$ python3 task_manager.py add "Walk the dog"
Added task #2: Walk the dog

$ python3 task_manager.py list

  ID   STATUS    TASK
  ----------------------------------------
  1    [ todo]   Buy milk
  2    [ todo]   Walk the dog

  0/2 completed.

$ python3 task_manager.py complete 1
Completed task #1: Buy milk

$ python3 task_manager.py delete 2
Deleted task #2: Walk the dog
```

Tasks are stored in `tasks.json` next to the program, so they persist between
runs.

---

## Quick Reference Card

```
PROJECT LAYOUT
  task.py          -> Task class + load_tasks/save_tasks/next_id (DATA layer)
  task_manager.py  -> argparse + cmd_* functions + colors      (APP layer)
  tasks.json       -> created at runtime, stores the task list

THE CORE PATTERN  (every command follows this)
  load -> change -> save
    tasks = load_tasks()
    ... add / complete / delete ...
    save_tasks(tasks)

ARGPARSE SUBCOMMANDS
  parser = argparse.ArgumentParser()
  subs = parser.add_subparsers(dest="command")
  p = subs.add_parser("add"); p.add_argument("title")
  args = parser.parse_args()       # args.command, args.title

JSON PERSISTENCE
  json.dump(data, file, indent=2)  # Python  -> JSON text
  data = json.load(file)           # JSON text -> Python
  Task.to_dict() / Task.from_dict()  bridge objects <-> dicts

ERROR HANDLING CHECKLIST
  [ ] file missing on first run?       -> return []
  [ ] file corrupted?                  -> except JSONDecodeError
  [ ] id not found?                    -> clear message, return 1
  [ ] non-number id?                   -> argparse type=int
  [ ] empty title?                     -> reject in cmd_add

ANSI COLORS
  GREEN="\033[92m"  RED="\033[91m"  RESET="\033[0m"
  print(f"{GREEN}done{RESET}")     # colorama for Windows-safe color
```

---

## Files in this Chapter

| File | Description |
|------|-------------|
| `README.md` | This file — teaching notes for Days 39–42 + project usage |
| `task.py` | The `Task` class and JSON load/save/next_id helpers (data layer) |
| `task_manager.py` | Main CLI: argparse subcommands, command handlers, colored output |
| `tasks.json` | Created at runtime; stores your saved tasks |
| `day39_examples.py` | Runnable: Task skeleton + argparse demo |
| `day40_examples.py` | Runnable: JSON save/load round-trip on a temp file |
| `day41_examples.py` | Runnable: complete/delete + graceful error handling |
| `day42_examples.py` | Runnable: ANSI colors + input validation |

---

## Congratulations

You started this course not knowing what a variable was. You are finishing it
by building a complete, persistent, error-handled, colorful command-line
application that ties together functions, data structures, file I/O, error
handling, modules, and object-oriented programming.

That is the difference between knowing Python and *using* Python. Well done —
you are no longer a beginner.
