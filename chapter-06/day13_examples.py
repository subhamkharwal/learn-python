"""
Chapter 06 — Day 13: while Loop, break, continue, pass
=======================================================
Topics covered:
  - while loop syntax and flowchart
  - Comparing for vs while
  - break — exit a loop immediately
  - continue — skip current iteration
  - pass — do nothing placeholder
  - Infinite loops and how to prevent them
  - Hands-on: Number guessing game & skip-even-numbers
"""

# ─────────────────────────────────────────────
# Section 1: Basic while Loop
# ─────────────────────────────────────────────
print("=" * 40)
print("SECTION 1: Basic while loop")
print("=" * 40)

# A while loop runs as long as its condition is True.
# Always make sure the condition can eventually become False!

count = 1
while count <= 5:       # condition: keep going while count is <= 5
    print(count)
    count += 1          # IMPORTANT: update count or loop runs forever

# Output: 1  2  3  4  5


# ─────────────────────────────────────────────
# Section 2: while vs for
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 2: while vs for — equivalent loops")
print("=" * 40)

# These two loops do the exact same thing:

print("Using for loop:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("Using while loop:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# Rule of thumb:
#   - Know how many iterations? → use for
#   - Repeat until something happens? → use while


# ─────────────────────────────────────────────
# Section 3: break — Exit the Loop Immediately
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 3: break")
print("=" * 40)

# break stops the loop the moment it is reached.
# All remaining iterations are cancelled.

print("Loop with break at i == 5:")
for i in range(1, 10):
    if i == 5:
        print(f"  → break fired at i={i}, exiting loop")
        break           # exit the loop right now
    print(f"  i = {i}")

# Output: i=1, i=2, i=3, i=4, then break

print("\nwhile loop with break:")
number = 10
while number > 0:
    print(number, end=" ")
    if number == 7:
        print(f"\n  → break fired at number={number}")
        break           # stop when we hit 7
    number -= 1
print()


# ─────────────────────────────────────────────
# Section 4: continue — Skip to Next Iteration
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 4: continue")
print("=" * 40)

# continue jumps back to the top of the loop immediately.
# The rest of the loop body is skipped for this one iteration,
# but the loop itself keeps running.

print("Print odd numbers from 1 to 10 using continue:")
for i in range(1, 11):
    if i % 2 == 0:      # if i is even...
        continue        # ...skip it and move to the next i
    print(i, end=" ")   # only reached for odd numbers
print()

# Output: 1 3 5 7 9

print("\nSkip multiples of 3 in range 1-15:")
for i in range(1, 16):
    if i % 3 == 0:
        continue        # skip 3, 6, 9, 12, 15
    print(i, end=" ")
print()


# ─────────────────────────────────────────────
# Section 5: pass — Do Nothing
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 5: pass")
print("=" * 40)

# pass is a no-op: it tells Python "there's nothing here".
# Useful as a placeholder when you're sketching code structure.

# Example: loop that currently does nothing (skeleton)
print("Loop with pass — no output:")
for i in range(5):
    pass    # placeholder: will add logic here later

print("(loop ran silently with pass)")

# Common use case: empty function or class body
# def todo_function():
#     pass    # will implement later


# ─────────────────────────────────────────────
# Section 6: Infinite Loops — Safe vs Dangerous
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("SECTION 6: Infinite loops")
print("=" * 40)

# DANGEROUS pattern (DO NOT run without a termination condition):
#
#   while True:
#       print("forever")   ← never stops, press Ctrl+C to interrupt
#
# SAFE pattern: while True combined with break
print("Safe while True loop (terminates after 3 iterations for demo):")

iteration = 0
while True:
    iteration += 1
    print(f"  Iteration {iteration}")
    if iteration >= 3:      # a real program would check user input
        print("  → Condition met, breaking out")
        break

print("Loop ended safely.\n")

# How to prevent accidental infinite loops:
#   1. Always update the variable the condition checks
#   2. Make sure the condition CAN become False
#   3. Consider adding a safety counter (max_iterations)

print("Safe while loop with a maximum-iterations guard:")
count = 0
max_iterations = 100    # safety ceiling — loop can never run > 100 times
dangerous_value = 999   # pretend this is user input that won't change

while dangerous_value != 0 and count < max_iterations:
    count += 1
    # normally we'd change dangerous_value here based on user input
    if count == 5:          # simulate stopping early for this demo
        dangerous_value = 0

print(f"  Loop exited after {count} iterations")


# ─────────────────────────────────────────────
# HANDS-ON 1: Number Guessing Game
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 1: Number Guessing Game")
print("=" * 40)

# The computer has a secret number.
# The player keeps guessing until they get it right.
# We use while True + break to keep looping until success.

# NOTE: input() pauses the program and waits for keyboard entry.
# For this demo we'll simulate it automatically if running without
# a terminal (non-interactive mode). In your own terminal, the
# interactive version will ask you to type.

import sys

SECRET_NUMBER = 42

def run_guessing_game_interactive():
    """Interactive version — run in a terminal."""
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue        # skip the rest, ask again

        attempts += 1

        if guess == SECRET_NUMBER:
            print(f"Correct! You found it in {attempts} attempt(s)!")
            break           # exit the loop — game over
        elif guess < SECRET_NUMBER:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

def run_guessing_game_demo():
    """Simulated version for non-interactive environments."""
    print("I'm thinking of a number between 1 and 100.")
    print("(Demo mode: auto-guessing)\n")

    # Simulate a binary-search strategy
    low, high = 1, 100
    attempts = 0

    while True:
        guess = (low + high) // 2   # guess the middle
        attempts += 1
        print(f"Guess #{attempts}: {guess}", end="  ")

        if guess == SECRET_NUMBER:
            print(f"→ Correct! Found in {attempts} attempt(s)!")
            break
        elif guess < SECRET_NUMBER:
            print("→ Too low!")
            low = guess + 1
        else:
            print("→ Too high!")
            high = guess - 1

# Detect whether we're running interactively
if sys.stdin.isatty():
    run_guessing_game_interactive()
else:
    run_guessing_game_demo()


# ─────────────────────────────────────────────
# HANDS-ON 2: Skip Even Numbers with continue
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("HANDS-ON 2: Skip Even Numbers")
print("=" * 40)

# Print only ODD numbers from 1 to 20 using continue

print("Odd numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:      # modulo 2 == 0 means even
        continue        # skip even numbers — go back to top of loop
    print(i, end=" ")
print()

# Output: 1 3 5 7 9 11 13 15 17 19


# ─────────────────────────────────────────────
# BONUS: FizzBuzz using continue and special cases
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("BONUS: FizzBuzz 1–20")
print("=" * 40)

# Classic problem:
#   Divisible by 3 → print "Fizz"
#   Divisible by 5 → print "Buzz"
#   Divisible by both → print "FizzBuzz"
#   Otherwise → print the number

for i in range(1, 21):
    if i % 15 == 0:     # divisible by both 3 and 5 (check FIRST)
        print("FizzBuzz", end=" ")
        continue
    if i % 3 == 0:
        print("Fizz", end=" ")
        continue
    if i % 5 == 0:
        print("Buzz", end=" ")
        continue
    print(i, end=" ")   # none of the above — just print the number
print()


# ─────────────────────────────────────────────
# BONUS: while loop — collecting valid user input
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("BONUS: Input validation loop (simulated)")
print("=" * 40)

# In real code you'd use input() and check the user's actual response.
# Here we simulate a few "inputs" to show the pattern.

simulated_inputs = [-5, 0, -1, 7]   # pretend these came from the user
input_index = 0

print("Asking for a positive number (simulated inputs:", simulated_inputs, ")")

positive_number = None
while positive_number is None:
    # Simulate getting a value
    value = simulated_inputs[input_index]
    input_index += 1
    print(f"  User entered: {value}", end="  ")

    if value > 0:
        positive_number = value
        print("→ Valid! Accepted.")
    else:
        print("→ Invalid. Please enter a positive number.")

print(f"Accepted value: {positive_number}")
