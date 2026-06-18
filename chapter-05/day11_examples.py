# ============================================================
# Chapter 05 — Day 11: Ternary Expressions, match, and/or
# Topics: Conditional expressions, match statement, combining
#         conditions with and/or/not
# Requires: Python 3.10+ for match examples
# ============================================================

import sys

# ──────────────────────────────────────────────
# SECTION 1: Ternary (Conditional) Expressions
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 1: Ternary Expressions")
print("=" * 55)

# Syntax:  result = value_if_true  if  condition  else  value_if_false

# --- Before ternary (standard if/else, 4 lines) ---
age = 20
if age >= 18:
    label = "Adult"
else:
    label = "Minor"
print(f"Standard if/else: {label}")

# --- After ternary (same logic, 1 line) ---
label = "Adult" if age >= 18 else "Minor"
print(f"Ternary:          {label}")

print()

# --- More ternary examples ---

score = 55
result = "Pass" if score >= 50 else "Fail"
print(f"Score {score}: {result}")   # Pass

is_raining = False
advice = "Take umbrella" if is_raining else "No umbrella needed"
print(f"Weather advice: {advice}")  # No umbrella needed

number = -3
sign = "non-negative" if number >= 0 else "negative"
print(f"{number} is {sign}")        # negative

# Ternary works inside f-strings too
items = []
print(f"Cart: {'has items' if items else 'is empty'}")   # is empty

print()

# ──────────────────────────────────────────────
# SECTION 2: Refactoring if/else → Ternary
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 2: Refactoring if/else to Ternary")
print("=" * 55)

# Original positive/negative/zero checker from Day 10
# Using nested ternary for a 3-way check
# NOTE: nested ternary is acceptable for simple 3-way cases,
#       but keep it easy to read.

def check_number_ternary(n):
    """Compact version using ternary expressions."""
    # Read as: "positive" if n>0, else ("negative" if n<0, else "zero")
    return "positive" if n > 0 else ("negative" if n < 0 else "zero")

sample_numbers = [42, -7, 0, 100, -0.5]
print("Number  →  Sign (ternary version)")
for num in sample_numbers:
    print(f"  {num:6}  →  {check_number_ternary(num)}")

print()

# ──────────────────────────────────────────────
# SECTION 3: The match Statement (Python 3.10+)
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 3: match Statement")
print("=" * 55)

# match compares one variable against several specific values (patterns).
# The wildcard  _  acts like 'else' — it matches anything not caught above.

python_version = sys.version_info
print(f"Python version: {python_version.major}.{python_version.minor}")

if python_version < (3, 10):
    print("match requires Python 3.10+. Showing code only.")
    print("""
    match day:
        case 'Monday':
            print('Start of the work week.')
        case 'Friday':
            print('Almost the weekend!')
        case 'Saturday' | 'Sunday':
            print("It's the weekend!")
        case _:
            print('Just another weekday.')
    """)
else:
    # --- Example 1: Day of the Week ---
    print("--- Day of the Week ---")
    days = ["Monday", "Friday", "Saturday", "Wednesday", "Sunday"]

    for day in days:
        match day:
            case "Monday":
                message = "Start of the work week. Coffee time!"
            case "Friday":
                message = "Almost the weekend. Hang in there!"
            case "Saturday" | "Sunday":
                # The | operator inside case means "OR"
                message = "It's the weekend! Time to relax."
            case _:
                # _ is the wildcard — catches everything else
                message = "Just another weekday. You've got this."
        print(f"  {day:<12}  →  {message}")

    print()

    # --- Example 2: Season Classifier (by month number) ---
    print("--- Season Classifier ---")

    def get_season(month):
        """Return the season for a given month number (1–12)."""
        match month:
            case 12 | 1 | 2:
                return "Winter"
            case 3 | 4 | 5:
                return "Spring"
            case 6 | 7 | 8:
                return "Summer"
            case 9 | 10 | 11:
                return "Autumn"
            case _:
                return "Invalid month (use 1–12)"

    for month_num in range(1, 13):
        print(f"  Month {month_num:2d}  →  {get_season(month_num)}")

    print()

    # --- Example 3: Simple Text Menu with match ---
    print("--- Simple Menu (match) ---")

    def handle_menu(choice):
        """Simulate a simple app menu."""
        match choice:
            case "1":
                return "Opening new file..."
            case "2":
                return "Saving current file..."
            case "3":
                return "Printing document..."
            case "4":
                return "Exiting application. Goodbye!"
            case _:
                return f"Unknown option '{choice}'. Try 1, 2, 3, or 4."

    print("Menu: 1=New  2=Save  3=Print  4=Exit")
    test_choices = ["1", "3", "4", "9", "abc"]
    for c in test_choices:
        print(f"  User enters '{c}'  →  {handle_menu(c)}")

    print()

    # --- Example 4: HTTP Status Codes ---
    print("--- HTTP Status Code Handler ---")

    def describe_status(code):
        """Return a human-readable description of an HTTP status code."""
        match code:
            case 200:
                return "OK — request succeeded"
            case 201:
                return "Created — resource successfully created"
            case 301 | 302:
                return "Redirect — page has moved"
            case 400:
                return "Bad Request — check your input"
            case 401:
                return "Unauthorized — please log in"
            case 403:
                return "Forbidden — you don't have permission"
            case 404:
                return "Not Found — page doesn't exist"
            case 500:
                return "Internal Server Error — server crashed"
            case _:
                return f"Unknown status code: {code}"

    status_codes = [200, 201, 302, 404, 500, 418]
    for code in status_codes:
        print(f"  HTTP {code}  →  {describe_status(code)}")

    print()


# ──────────────────────────────────────────────
# SECTION 4: Combining Conditions with and / or / not
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 4: Combining Conditions (and / or / not)")
print("=" * 55)

# --- and: BOTH must be True ---
print("--- 'and' examples ---")

age = 25
has_ticket = True
print(f"age={age}, has_ticket={has_ticket}")
if age >= 18 and has_ticket:
    print("  Welcome to the event!")   # Both are True, so this runs

age2 = 15
has_ticket2 = True
print(f"age={age2}, has_ticket={has_ticket2}")
if age2 >= 18 and has_ticket2:
    print("  Welcome to the event!")
else:
    print("  Sorry, you cannot enter.")   # age < 18 makes and fail

print()

# --- or: AT LEAST ONE must be True ---
print("--- 'or' examples ---")

is_weekend = False
is_holiday = True
print(f"is_weekend={is_weekend}, is_holiday={is_holiday}")
if is_weekend or is_holiday:
    print("  No work today!")   # is_holiday is True, so or succeeds

is_weekend2 = False
is_holiday2 = False
print(f"is_weekend={is_weekend2}, is_holiday={is_holiday2}")
if is_weekend2 or is_holiday2:
    print("  No work today!")
else:
    print("  Back to work.")   # Both False, so or fails

print()

# --- not: flips True ↔ False ---
print("--- 'not' examples ---")

is_raining = False
print(f"is_raining={is_raining}")
if not is_raining:
    print("  Great day for a walk!")   # not False == True, so this runs

is_logged_in = True
if not is_logged_in:
    print("  Please log in.")
else:
    print("  Welcome back!")   # is_logged_in is True, runs the else

print()

# ──────────────────────────────────────────────
# SECTION 5: Using Parentheses for Complex Conditions
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 5: Complex Conditions with Parentheses")
print("=" * 55)

# 'and' has HIGHER precedence than 'or'.
# Without parentheses: A or B and C  means  A or (B and C)
# Use parentheses to make your intent crystal clear.

# Scenario: user can see premium content if:
#   (they are a subscriber OR they are an admin) AND their account is active

is_subscriber = False
is_admin = True
is_active = True

# Without parentheses — easy to misread
check1 = is_subscriber or is_admin and is_active
# Python evaluates as: is_subscriber or (is_admin and is_active) = True
print(f"Without parens: {check1}  (ambiguous intent)")

# With parentheses — explicit and readable
check2 = (is_subscriber or is_admin) and is_active
print(f"With parens:    {check2}  (clear intent)")

print()

# Flattening deep nesting with 'and'
print("--- Flattening nested ifs with 'and' ---")

user_logged_in = True
has_subscription = True
subscription_expired = False
is_banned = False

# NESTED version (hard to read):
# if user_logged_in:
#     if has_subscription:
#         if not subscription_expired:
#             if not is_banned:
#                 print("Show content")

# FLAT version with 'and' (much cleaner):
if user_logged_in and has_subscription and not subscription_expired and not is_banned:
    print("  Showing premium content.")
else:
    print("  Access denied.")

print()

# ──────────────────────────────────────────────
# SECTION 6: Short-Circuit Evaluation
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 6: Short-Circuit Evaluation")
print("=" * 55)

# Python stops evaluating as soon as the result is determined.
# This is useful for safety checks.

# Example: only access items[0] if the list is not empty
print("--- Safe list access ---")
cart = []

# Without short-circuit check: cart[0] would raise IndexError
# With short-circuit: if cart is falsy, Python never evaluates cart[0]
if cart and cart[0] == "apple":
    print("  First item is apple")
else:
    print("  Cart is empty — skipping cart[0] safely")

cart2 = ["apple", "banana"]
if cart2 and cart2[0] == "apple":
    print("  First item is apple")   # Safe to access now

print()

# ──────────────────────────────────────────────
# SECTION 7: Putting It All Together
# ──────────────────────────────────────────────

print("=" * 55)
print("SECTION 7: Putting It All Together")
print("=" * 55)

def evaluate_loan_application(age, income, credit_score, has_existing_loan):
    """
    Decide whether to approve a loan application.
    Combines ternary, and/or, and a clear if/elif/else structure.
    """
    # Quick disqualifiers using 'or'
    if age < 18 or income < 20000:
        return "REJECTED: Age under 18 or income too low."

    # Credit score tiers — uses elif chain
    if credit_score >= 750:
        rate = 3.5
        tier = "Excellent"
    elif credit_score >= 650:
        rate = 5.0
        tier = "Good"
    elif credit_score >= 550:
        rate = 8.0
        tier = "Fair"
    else:
        return "REJECTED: Credit score too low (minimum 550)."

    # Surcharge if existing loan — ternary
    surcharge = 1.0 if has_existing_loan else 0.0
    final_rate = rate + surcharge

    return (
        f"APPROVED | Credit: {tier} | "
        f"Base rate: {rate}% | "
        f"Surcharge: {surcharge}% | "
        f"Final rate: {final_rate}%"
    )

applications = [
    (25, 50000, 780, False),
    (30, 45000, 670, True),
    (22, 35000, 590, False),
    (17, 15000, 700, False),
    (40, 60000, 500, False),
]

print("Loan Application Results:")
print("-" * 55)
for age, income, credit, existing_loan in applications:
    result = evaluate_loan_application(age, income, credit, existing_loan)
    print(f"  Age:{age} Income:{income} Credit:{credit}  →  {result}")

print()

# ──────────────────────────────────────────────
# HANDS-ON CHALLENGE
# ──────────────────────────────────────────────

print("=" * 55)
print("HANDS-ON CHALLENGE")
print("=" * 55)

# Uncomment to try interactive challenges

# --- Challenge 1: Ternary version of number checker ---
# n = int(input("Enter a number: "))
# result = "positive" if n > 0 else ("negative" if n < 0 else "zero")
# print(f"{n} is {result}")

# --- Challenge 2: match for HTTP codes (Python 3.10+) ---
# code = int(input("Enter HTTP status code: "))
# describe_status(code)   # defined above

print("(Input challenges are commented out — uncomment to try them!)")
print()
print("Day 11 examples complete.")
