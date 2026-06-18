# ============================================================
# Chapter 03 — Day 5: Arithmetic Operators & Precedence
# ============================================================
# Run this file with:  python day5_examples.py
# ============================================================

# ─────────────────────────────────────────────────────────────
# SECTION 1 — The 7 Arithmetic Operators
# ─────────────────────────────────────────────────────────────

print("=" * 50)
print("SECTION 1 — The 7 Arithmetic Operators")
print("=" * 50)

a = 17
b = 5

print(f"\nWorking with a = {a} and b = {b}")
print(f"  Addition       a + b  = {a + b}")     # 22
print(f"  Subtraction    a - b  = {a - b}")     # 12
print(f"  Multiplication a * b  = {a * b}")     # 85
print(f"  True Division  a / b  = {a / b}")     # 3.4  (always float)
print(f"  Floor Division a // b = {a // b}")    # 3    (rounds down)
print(f"  Modulo         a % b  = {a % b}")     # 2    (remainder)
print(f"  Exponentiation a ** b = {a ** b}")    # 1419857


# ─────────────────────────────────────────────────────────────
# SECTION 2 — True Division vs Floor Division
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("SECTION 2 — True Division / vs Floor Division //")
print("=" * 50)

print("\n--- True Division (/) always returns a float ---")
print(f"  10 / 2  = {10 / 2}")     # 5.0  (note: NOT 5, it's a float)
print(f"  7  / 2  = {7 / 2}")      # 3.5
print(f"  1  / 3  = {1 / 3}")      # 0.333...

print("\n--- Floor Division (//) always rounds DOWN ---")
print(f"  10 // 2  = {10 // 2}")   # 5
print(f"  7  // 2  = {7 // 2}")    # 3  (not 3.5 — floors down)
print(f"  1  // 3  = {1 // 3}")    # 0  (0.33... floors to 0)
print(f"  -7 // 2  = {-7 // 2}")   # -4  (floors TOWARD negative infinity, not -3)

print("\n--- Practical use of floor division ---")
total_minutes = 137
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"  {total_minutes} minutes = {hours} hours and {minutes} minutes")


# ─────────────────────────────────────────────────────────────
# SECTION 3 — Modulo % in Action
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("SECTION 3 — Modulo % in Action")
print("=" * 50)

# Use case 1: Even / Odd checker
print("\n--- Even / Odd Check ---")
for number in [0, 1, 7, 12, 99, 100]:
    if number % 2 == 0:
        print(f"  {number:3d} is EVEN  (remainder: {number % 2})")
    else:
        print(f"  {number:3d} is ODD   (remainder: {number % 2})")

# Use case 2: Clock math (wrap-around)
print("\n--- Clock Math (12-hour wrap-around) ---")
current_hour = 10
for hours_added in [1, 2, 3, 4, 5]:
    new_hour = (current_hour + hours_added) % 12
    # Handle 0 → display as 12
    display_hour = new_hour if new_hour != 0 else 12
    print(f"  {current_hour}:00 + {hours_added} hours = {display_hour}:00")

# Use case 3: Extract digits
print("\n--- Extract Last Two Digits of a Year ---")
year = 2026
last_two_digits = year % 100
print(f"  Year {year}: last two digits = {last_two_digits}")


# ─────────────────────────────────────────────────────────────
# SECTION 4 — Exponentiation **
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("SECTION 4 — Exponentiation **")
print("=" * 50)

print(f"\n  2 ** 10   = {2 ** 10}")      # 1024
print(f"  3 ** 3    = {3 ** 3}")         # 27
print(f"  9 ** 0.5  = {9 ** 0.5}")       # 3.0  (square root)
print(f"  16 ** 0.5 = {16 ** 0.5}")      # 4.0
print(f"  2 ** -1   = {2 ** -1}")        # 0.5  (reciprocal)
print(f"  2 ** 0    = {2 ** 0}")         # 1    (anything to power 0 is 1)

# WARNING: ^ is NOT exponentiation in Python!
print("\n--- WATCH OUT: ^ is NOT power in Python ---")
print(f"  2 ^ 3  = {2 ^ 3}   ← bitwise XOR, NOT power  (do NOT use this for powers)")
print(f"  2 ** 3 = {2 ** 3}  ← this is the correct way  (use ** for power)")


# ─────────────────────────────────────────────────────────────
# SECTION 5 — Operator Precedence (PEMDAS)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("SECTION 5 — Operator Precedence (PEMDAS)")
print("=" * 50)

print("\n--- No parentheses: Python applies PEMDAS ---")
expr1 = 2 + 3 * 4          # multiplication first: 2 + 12 = 14
expr2 = 10 - 4 / 2         # division first: 10 - 2.0 = 8.0
expr3 = 2 ** 3 ** 2        # right-to-left: 3**2=9, then 2**9 = 512
expr4 = 5 + 2 * 3 - 8 / 4  # mult and div first: 5 + 6 - 2.0 = 9.0

print(f"  2 + 3 * 4        = {expr1}    (NOT 20 — multiply before add)")
print(f"  10 - 4 / 2       = {expr2}   (NOT 3.0 — divide before subtract)")
print(f"  2 ** 3 ** 2      = {expr3}   (right-to-left: 2**(3**2)=2**9)")
print(f"  5 + 2 * 3 - 8/4  = {expr4}   (mult/div first, then left-to-right)")

print("\n--- With parentheses: YOU control the order ---")
expr5 = (2 + 3) * 4         # parentheses first: 5 * 4 = 20
expr6 = (10 - 4) / 2        # parentheses first: 6 / 2 = 3.0
expr7 = (2 ** 3) ** 2        # parentheses first: 8 ** 2 = 64

print(f"  (2 + 3) * 4      = {expr5}")
print(f"  (10 - 4) / 2     = {expr6}")
print(f"  (2 ** 3) ** 2    = {expr7}")

print("\n--- Step-by-step trace: 5 + 2 * 3 - 8 / 4 ---")
step1 = 2 * 3               # → 6
step2 = 8 / 4               # → 2.0
step3 = 5 + step1           # → 11
step4 = step3 - step2       # → 9.0
print(f"  Step 1: 2 * 3   = {step1}")
print(f"  Step 2: 8 / 4   = {step2}")
print(f"  Step 3: 5 + 6   = {step3}")
print(f"  Step 4: 11 - 2  = {step4}")
print(f"  Final answer     = {step4}")


# ─────────────────────────────────────────────────────────────
# HANDS-ON PROJECT 1 — Temperature Converter
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("HANDS-ON 1 — Temperature Converter")
print("=" * 50)

# Formulas:
#   Celsius to Fahrenheit: F = (C × 9/5) + 32
#   Fahrenheit to Celsius: C = (F - 32) × 5/9

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# --- Celsius to Fahrenheit ---
print("\nCelsius → Fahrenheit:")
temperatures_c = [0, 20, 37, 100, -40]
for temp_c in temperatures_c:
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"  {temp_c:6.1f} °C  =  {temp_f:7.2f} °F")

# Notable temperatures explained:
#   0 °C   = 32 °F    (freezing point of water)
#   20 °C  = 68 °F    (comfortable room temperature)
#   37 °C  = 98.6 °F  (human body temperature)
#   100 °C = 212 °F   (boiling point of water)
#   -40 °C = -40 °F   (the one temperature where both scales are equal!)

print("\nFahrenheit → Celsius:")
temperatures_f = [32, 68, 98.6, 212, -40]
for temp_f in temperatures_f:
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"  {temp_f:7.2f} °F  =  {temp_c:6.2f} °C")


# ─────────────────────────────────────────────────────────────
# HANDS-ON PROJECT 2 — Area Calculator
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 50)
print("HANDS-ON 2 — Geometry Area Calculator")
print("=" * 50)

import math   # math.pi gives us a precise value of π

# --- Area of a Circle: A = π × r² ---
print("\nArea of a Circle  (A = π × r²):")
for radius in [1, 5, 7, 10]:
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"  radius = {radius:2d}  →  area = {area:8.4f},  circumference = {circumference:.4f}")

# --- Area of a Rectangle: A = l × w ---
print("\nArea of a Rectangle  (A = l × w):")
rectangles = [(4, 6), (10, 3), (7, 7)]   # (length, width) pairs
for length, width in rectangles:
    area = length * width
    perimeter = 2 * (length + width)
    print(f"  {length} × {width}  →  area = {area:3d},  perimeter = {perimeter}")

# --- Area of a Triangle: A = 0.5 × base × height ---
print("\nArea of a Triangle  (A = ½ × base × height):")
triangles = [(6, 4), (10, 5), (3, 8)]    # (base, height) pairs
for base, height in triangles:
    area = 0.5 * base * height
    print(f"  base = {base}, height = {height}  →  area = {area}")

# --- Mini Calculator: Compare circle vs square for same perimeter ---
print("\n--- Bonus: Which shape has more area for the same perimeter? ---")
perimeter = 40

# Square: each side = perimeter / 4
square_side = perimeter / 4
square_area = square_side ** 2

# Circle: circumference = 2πr → r = perimeter / (2π)
circle_radius = perimeter / (2 * math.pi)
circle_area = math.pi * circle_radius ** 2

print(f"  Perimeter/Circumference = {perimeter}")
print(f"  Square area  = {square_area:.4f}")
print(f"  Circle area  = {circle_area:.4f}")
print(f"  Circle has {((circle_area / square_area) - 1) * 100:.1f}% more area than the square!")
# Fun fact: among all shapes with a given perimeter, a circle always has the maximum area!


print("\n" + "=" * 50)
print("End of Day 5 Examples")
print("=" * 50)
