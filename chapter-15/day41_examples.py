"""
Chapter 15 - Day 41: complete, delete, and graceful error handling
===================================================================
Today we add the last two operations - completing and deleting a task - and,
just as importantly, we make the program FAIL NICELY.

A beginner program crashes with a scary traceback when something is wrong.
A polished program prints a calm, clear message instead. The tool for that is
try/except (Chapter 11) plus careful "what if?" thinking.
"""


class Task:
    def __init__(self, id, title, done=False):
        self.id = id
        self.title = title
        self.done = done

    def __repr__(self):
        mark = "x" if self.done else " "
        return f"#{self.id} [{mark}] {self.title}"


# Start with a small in-memory list (no file needed for the demo).
tasks = [Task(1, "Buy milk"), Task(2, "Walk the dog")]


# ============================================================
# 1. COMPLETE  -  find by id, mark done
# ============================================================
def complete(tasks, task_id):
    for t in tasks:
        if t.id == task_id:
            t.done = True
            return True            # found and updated
    return False                   # not found


# ============================================================
# 2. DELETE  -  find by id, remove
# ============================================================
def delete(tasks, task_id):
    for t in tasks:
        if t.id == task_id:
            tasks.remove(t)
            return True
    return False


# ============================================================
# 3. GRACEFUL ERRORS  -  what could go wrong?
# ============================================================
# Case A: a valid id
print("Completing task 1:", complete(tasks, 1))
print("Tasks now:", tasks)

# Case B: an id that does not exist -> we DON'T crash, we report it.
ok = delete(tasks, 99)
if not ok:
    print("Could not delete: no task with id 99 (handled gracefully).")

# Case C: the user typed text where a number was expected.
# argparse with type=int catches this for us, but here is the idea by hand:
user_input = "abc"
try:
    task_id = int(user_input)
    delete(tasks, task_id)
except ValueError:
    print(f"Could not delete: '{user_input}' is not a valid number.")

# Case D: deleting from an empty list should also be safe.
empty = []
print("Delete from empty list:", delete(empty, 1))   # False, no crash

print("\nDay 41 done: full CRUD works and bad input is handled cleanly.")
