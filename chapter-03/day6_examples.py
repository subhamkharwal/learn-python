# ============================================================
# Chapter 03 — Day 6: Comparison, Logical & Assignment Operators
# ============================================================
# Run this file with:  python day6_examples.py
# ============================================================

# ─────────────────────────────────────────────────────────────
# SECTION 1 — Comparison Operators
# ─────────────────────────────────────────────────────────────

print("=" * 55)
print("SECTION 1 — Comparison Operators")
print("=" * 55)

# Every comparison produces True or False (a bool)
x = 10
y = 3

print(f"\nComparing x = {x} and y = {y}")
print(f"  x == y   →  {x == y}")    # False  (10 is not equal to 3)
print(f"  x != y   →  {x != y}")    # True   (10 is NOT equal to 3)
print(f"  x >  y   →  {x > y}")     # True
print(f"  x <  y   →  {x < y}")     # False
print(f"  x >= y   →  {x >= y}")    # True
print(f"  x <= y   →  {x <= y}")    # False

# Edge cases — same value on both sides
z = 10
print(f"\nComparing x = {x} and z = {z}  (both are 10)")
print(f"  x == z   →  {x == z}")    # True
print(f"  x >= z   →  {x >= z}")    # True  (>= means equal OR greater)
print(f"  x <= z   →  {x <= z}")    # True

# IMPORTANT: = (assignment) vs == (comparison)
print("\n--- = vs == ---")
score = 100          # = assigns the value 100 to 'score'
print(f"  score = 100  →  score is now {score}  (assignment)")
print(f"  score == 100 →  {score == 100}           (comparison: is it equal?)")
print(f"  score == 50  →  {score == 50}          (comparison: is it equal?)")

# String comparisons (alphabetical order)
print("\n--- String Comparisons ---")
word1 = "apple"
word2 = "banana"
word3 = "Apple"     # capital A

print(f"  'apple' == 'apple'   →  {'apple' == 'apple'}")
print(f"  'apple' == 'Apple'   →  {'apple' == 'Apple'}  (case-sensitive!)")
print(f"  'apple'  < 'banana'  →  {'apple' < 'banana'}   (a comes before b)")
print(f"  'banana' > 'apple'   →  {'banana' > 'apple'}")


# ─────────────────────────────────────────────────────────────
# SECTION 2 — Logical Operators: and, or, not
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 2 — Logical Operators: and, or, not")
print("=" * 55)

# --- AND: both sides must be True ---
print("\n--- AND Truth Table ---")
print("  True  and True  →", True  and True)   # True
print("  True  and False →", True  and False)  # False
print("  False and True  →", False and True)   # False
print("  False and False →", False and False)  # False

# --- OR: at least one side must be True ---
print("\n--- OR Truth Table ---")
print("  True  or True   →", True  or True)    # True
print("  True  or False  →", True  or False)   # True
print("  False or True   →", False or True)    # True
print("  False or False  →", False or False)   # False

# --- NOT: flips True to False and False to True ---
print("\n--- NOT Truth Table ---")
print("  not True   →", not True)    # False
print("  not False  →", not False)   # True

# --- Practical examples ---
print("\n--- Practical: Concert Entry Check ---")
has_ticket = True
is_adult   = False

can_enter_vip  = has_ticket and is_adult    # Must have ticket AND be adult
can_enter_gen  = has_ticket or is_adult     # Ticket OR adult (either works)
cannot_enter   = not has_ticket             # Doesn't have ticket

print(f"  has_ticket={has_ticket}, is_adult={is_adult}")
print(f"  VIP entry (ticket AND adult): {can_enter_vip}")
print(f"  Gen entry (ticket OR adult) : {can_enter_gen}")
print(f"  Blocked   (not has_ticket)  : {cannot_enter}")

print("\n--- Practical: Loan Eligibility ---")
age     = 25
income  = 55000
has_debt = False

# Eligible if: age 18-65, income >= 30000, no existing debt
is_eligible = (age >= 18) and (age <= 65) and (income >= 30000) and (not has_debt)
print(f"  age={age}, income={income}, has_debt={has_debt}")
print(f"  Loan eligible: {is_eligible}")

# Change one condition to see it fail
age_minor = 16
is_eligible_minor = (age_minor >= 18) and (age_minor <= 65) and (income >= 30000) and (not has_debt)
print(f"\n  age={age_minor}, income={income}, has_debt={has_debt}")
print(f"  Loan eligible (minor): {is_eligible_minor}")   # False — age fails


# ─────────────────────────────────────────────────────────────
# SECTION 3 — Short-Circuit Evaluation
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 3 — Short-Circuit Evaluation")
print("=" * 55)

# Python stops evaluating as soon as it knows the final answer.
# This is called "short-circuit" evaluation.

# --- AND short-circuits on False ---
print("\n--- AND short-circuit: stops at first False ---")

# Normally, dividing by zero causes a ZeroDivisionError.
# Short-circuit saves us here: because (divisor != 0) is False,
# Python never evaluates (10 / divisor), so no error occurs.
divisor = 0
safe_result = (divisor != 0) and (10 / divisor > 1)
print(f"  divisor = 0")
print(f"  (divisor != 0) and (10 / divisor > 1) = {safe_result}")
print("  No ZeroDivisionError! Python stopped at (divisor != 0) = False.")

# --- OR short-circuits on True ---
print("\n--- OR short-circuit: stops at first True ---")

# Helper function that announces when it runs
def expensive_check():
    print("    [expensive_check() was called!]")
    return True

print("  Case 1: left side is True → right side is SKIPPED")
result = True or expensive_check()      # expensive_check never runs
print(f"  Result: {result}")

print("\n  Case 2: left side is False → right side IS evaluated")
result = False or expensive_check()     # expensive_check runs this time
print(f"  Result: {result}")

# --- The "or default" pattern (very common in Python) ---
print("\n--- The 'or default' Pattern ---")
# Empty string, 0, None, [] are all "falsy" in Python.
# A non-empty string, non-zero number, etc. are "truthy".

user_input = ""                              # Simulate empty input
display_name = user_input or "Anonymous"     # Falsy → use the default
print(f"  user_input='' →  display_name = '{display_name}'")

user_input = "Alice"
display_name = user_input or "Anonymous"     # Truthy → use the input
print(f"  user_input='Alice' →  display_name = '{display_name}'")


# ─────────────────────────────────────────────────────────────
# SECTION 4 — Assignment Operators (Shorthand)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 4 — Assignment Operators (Shorthand)")
print("=" * 55)

print("\n--- All shorthand operators demonstrated ---")
n = 20
print(f"  Starting value: n = {n}")

n += 5        # same as: n = n + 5
print(f"  After n += 5    →  n = {n}")    # 25

n -= 3        # same as: n = n - 3
print(f"  After n -= 3    →  n = {n}")    # 22

n *= 2        # same as: n = n * 2
print(f"  After n *= 2    →  n = {n}")    # 44

n /= 4        # same as: n = n / 4  (result becomes float)
print(f"  After n /= 4    →  n = {n}")    # 11.0

n //= 2       # same as: n = n // 2  (floor division in place)
print(f"  After n //= 2   →  n = {n}")    # 5.0

n **= 3       # same as: n = n ** 3
print(f"  After n **= 3   →  n = {n}")    # 125.0

n %= 100      # same as: n = n % 100
print(f"  After n %= 100  →  n = {n}")    # 25.0

# --- Practical 1: Score counter ---
print("\n--- Practical: Game Score Counter ---")
score = 0
print(f"  Initial score: {score}")

score += 10   # picked up a coin
print(f"  Picked up coin (+10): {score}")

score += 50   # defeated enemy
print(f"  Defeated enemy (+50): {score}")

score -= 20   # took damage
print(f"  Took damage (-20): {score}")

score *= 2    # double points bonus!
print(f"  Double points! (×2): {score}")

# --- Practical 2: Compound interest ---
print("\n--- Practical: Compound Interest ---")
balance = 1000.00
annual_rate = 0.05        # 5% per year
print(f"  Initial balance: ${balance:.2f}")

for year in range(1, 6):  # 5 years
    balance *= (1 + annual_rate)   # same as: balance = balance * 1.05
    print(f"  Year {year}: ${balance:.2f}")

# --- Practical 3: Angle wrap-around using %= ---
print("\n--- Practical: Angle Wrap-Around ---")
angle = 0
print(f"  Start angle: {angle}°")
for step in range(7):
    angle += 60           # rotate 60° each step
    angle %= 360          # wrap around at 360°
    print(f"  After step {step + 1} (+60°): {angle}°")


# ─────────────────────────────────────────────────────────────
# SECTION 5 — Predict the Output Challenge
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 5 — Predict the Output Challenge")
print("  (Cover the answers, predict first, then look!)")
print("=" * 55)

# Challenge 1
a = 5
b = 10
c = 5
print(f"\nChallenge 1: a={a}, b={b}, c={c}")
print(f"  a == c           →  {a == c}")          # True
print(f"  a != b           →  {a != b}")          # True
print(f"  b > a and b > c  →  {b > a and b > c}") # True
print(f"  a == c or a > b  →  {a == c or a > b}") # True (short-circuits at a==c)
print(f"  not (a > b)      →  {not (a > b)}")     # True  (a is NOT > b)

# Challenge 2
x = 0
print(f"\nChallenge 2: x = {x}")
print(f"  bool(x)          →  {bool(x)}")         # False (0 is falsy)
print(f"  x or 'default'   →  {x or 'default'}")  # 'default' (0 is falsy)
print(f"  x and 1/0        →  {x and 'wont crash'}") # False (short-circuit saves us)

# Challenge 3 — precedence + comparison
val = 2 + 3 > 4 and 10 / 2 == 5
print(f"\nChallenge 3: 2 + 3 > 4 and 10 / 2 == 5")
print(f"  Step 1: 2 + 3     = 5")
print(f"  Step 2: 10 / 2    = 5.0")
print(f"  Step 3: 5 > 4     = True")
print(f"  Step 4: 5.0 == 5  = True")
print(f"  Step 5: True and True = True")
print(f"  Answer: {val}")


# ─────────────────────────────────────────────────────────────
# SECTION 6 — Common Mistakes Demonstrated
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("SECTION 6 — Common Mistakes & Gotchas")
print("=" * 55)

# Mistake 1: Float precision  (0.1 + 0.2 is NOT 0.3)
print("\n--- Float Precision Gotcha ---")
result = 0.1 + 0.2
print(f"  0.1 + 0.2           = {result}")          # 0.30000000000000004  !!
print(f"  0.1 + 0.2 == 0.3    = {0.1 + 0.2 == 0.3}")  # False  !!

# Fix 1: round()
print(f"  round(0.1+0.2, 10)  = {round(0.1 + 0.2, 10)}")  # 0.3 (rounded)
print(f"  round(0.1+0.2, 10) == 0.3  = {round(0.1 + 0.2, 10) == 0.3}")  # True

# Fix 2: math.isclose()
import math
print(f"  math.isclose(0.1+0.2, 0.3) = {math.isclose(0.1 + 0.2, 0.3)}")  # True
print("  --> Always use math.isclose() or round() when comparing floats!")

# Mistake 2: not precedence
print("\n--- 'not' Precedence ---")
result_without_parens = not True and False    # not binds tighter than and
result_with_parens    = not (True and False)

print(f"  not True and False    = {result_without_parens}")  # False
print(f"  not (True and False)  = {result_with_parens}")     # True
print("  --> Different results! Use parentheses to be explicit.")

# Mistake 3: chained comparisons (Python supports them correctly)
print("\n--- Chained Comparisons (Python does this right!) ---")
age = 25
# Most languages would require: age >= 18 and age <= 65
# Python allows this nicer form:
in_working_age = 18 <= age <= 65
print(f"  18 <= {age} <= 65  =  {in_working_age}")   # True

temperature = 150
dangerously_hot = 100 < temperature < 200
print(f"  100 < {temperature} < 200  =  {dangerously_hot}")  # True


print("\n" + "=" * 55)
print("End of Day 6 Examples")
print("=" * 55)
