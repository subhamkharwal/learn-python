# ============================================================
# Chapter 05 — Day 10: if / elif / else
# Topics: Conditions, truthiness/falsiness, nested conditions
# ============================================================

# ──────────────────────────────────────────────
# SECTION 1: Basic if statement
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 1: Basic if Statement")
print("=" * 50)

temperature = 35

# The condition after 'if' must end with a colon ':'
# The code inside the block must be indented (4 spaces)
if temperature > 30:
    print("It's hot outside!")   # This runs because 35 > 30 is True

print()  # blank line for readability


# ──────────────────────────────────────────────
# SECTION 2: if / else
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 2: if / else")
print("=" * 50)

score = 45

# else runs when the if-condition is False
if score >= 50:
    print("You passed!")
else:
    print("You did not pass. Try again.")   # This runs because 45 < 50

print()


# ──────────────────────────────────────────────
# SECTION 3: if / elif / else (Grade Classifier)
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 3: Grade Classifier (if/elif/else)")
print("=" * 50)

# Python checks conditions TOP TO BOTTOM.
# The FIRST matching condition wins; the rest are skipped.
# This is why we order from highest to lowest.

def classify_grade(score):
    """Return the letter grade for a given numeric score."""
    if score >= 90:
        grade = "A"
        remark = "Excellent!"
    elif score >= 80:
        grade = "B"
        remark = "Good job!"
    elif score >= 70:
        grade = "C"
        remark = "Average."
    elif score >= 60:
        grade = "D"
        remark = "Below average. Keep trying."
    else:
        # This catches anything below 60
        grade = "F"
        remark = "Failed. Please study harder."
    return grade, remark

# Test several scores to see the classifier in action
test_scores = [95, 83, 71, 62, 45]

for s in test_scores:
    g, r = classify_grade(s)
    print(f"Score: {s:3d}  ->  Grade: {g}  ({r})")

print()


# ──────────────────────────────────────────────
# SECTION 4: Positive / Negative / Zero Checker
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 4: Positive / Negative / Zero Checker")
print("=" * 50)

def check_number(n):
    """Tell us whether n is positive, negative, or zero."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        # The only remaining possibility is exactly 0
        return "zero"

sample_numbers = [42, -7, 0, 100, -0.5, 0.0]

for num in sample_numbers:
    result = check_number(num)
    print(f"  {num:6}  is  {result}")

print()


# ──────────────────────────────────────────────
# SECTION 5: Truthy and Falsy Values
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 5: Truthy and Falsy Values")
print("=" * 50)

# Python treats these values as False (falsy):
#   False, 0, 0.0, "", [], {}, (), None
# Everything else is treated as True (truthy).

falsy_examples = [False, 0, 0.0, "", [], {}, (), None]
truthy_examples = [True, 1, -1, 0.1, "hello", [0], {"a": 1}, (1,)]

print("Falsy values (treated as False in an if):")
for val in falsy_examples:
    if val:
        label = "truthy"
    else:
        label = "falsy"
    print(f"  {repr(val):15}  ->  {label}")

print()
print("Truthy values (treated as True in an if):")
for val in truthy_examples:
    if val:
        label = "truthy"
    else:
        label = "falsy"
    print(f"  {repr(val):15}  ->  {label}")

print()

# Practical use: check if a string or list is empty
username = ""
if username:
    print(f"Welcome, {username}!")
else:
    print("No username provided.")   # runs because "" is falsy

cart = ["apple", "banana"]
if cart:
    print(f"You have {len(cart)} item(s) in your cart.")   # runs
else:
    print("Your cart is empty.")

print()


# ──────────────────────────────────────────────
# SECTION 6: Nested Conditions
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 6: Nested Conditions")
print("=" * 50)

# Nested if: an if inside another if
# Use sparingly — deep nesting is hard to read.

def can_enter_event(age, has_ticket):
    """Check whether a person can enter an event."""
    if age >= 18:
        # We only check for the ticket if the age check passed
        if has_ticket:
            return "Access granted. Enjoy the event!"
        else:
            return "Age OK, but you need a ticket."
    else:
        return f"Sorry, must be 18+. You are {age}."

print(can_enter_event(25, True))    # Access granted
print(can_enter_event(25, False))   # Need ticket
print(can_enter_event(16, True))    # Too young

print()


# ──────────────────────────────────────────────
# SECTION 7: Common Mistake — Separate if vs elif
# ──────────────────────────────────────────────

print("=" * 50)
print("SECTION 7: Common Mistake Demo — if vs elif")
print("=" * 50)

score = 95

# WRONG approach — using separate 'if' statements
# Both "A" and "B" print because 95 >= 90 AND 95 >= 80 are both True
print("Using separate 'if' statements (WRONG for grades):")
if score >= 90:
    print("  Grade: A")
if score >= 80:    # This still runs! 95 >= 80 is True
    print("  Grade: B")

print()

# CORRECT approach — using 'elif' stops after the first match
print("Using 'elif' (CORRECT):")
if score >= 90:
    print("  Grade: A")
elif score >= 80:
    # This does NOT run because the if above already matched
    print("  Grade: B")

print()

# ──────────────────────────────────────────────
# HANDS-ON CHALLENGE (try it yourself)
# ──────────────────────────────────────────────

print("=" * 50)
print("HANDS-ON CHALLENGE")
print("=" * 50)

# Uncomment the lines below to run interactive challenges

# --- Challenge 1: Number Classifier ---
# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# --- Challenge 2: Temperature Advisor ---
# temp = float(input("Enter temperature in Celsius: "))
# if temp > 30:
#     print("Hot — stay hydrated!")
# elif temp >= 20:
#     print("Warm — great weather!")
# elif temp >= 10:
#     print("Cool — bring a jacket.")
# else:
#     print("Cold — bundle up!")

print("(Input challenges are commented out — uncomment to try them!)")
print()
print("Day 10 examples complete.")
