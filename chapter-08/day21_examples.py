"""
Chapter 08 - Day 21: Tuples
===========================
Topics: immutability, tuples vs lists, tuple packing/unpacking,
        the single-element tuple gotcha, and practical uses.
"""

# ============================================================
# 1. CREATING TUPLES
# ============================================================
# A tuple is an ORDERED but UNCHANGEABLE collection. Use parentheses ().
# Think of a tuple as a "read-only list".

empty = ()                              # empty tuple
point = (3, 5)                          # a pair of coordinates
rgb = (255, 128, 0)                     # a colour as red, green, blue
mixed = ("Alice", 30, True)             # tuples can mix types too

print("empty :", empty)
print("point :", point)
print("rgb   :", rgb)
print("mixed :", mixed)

# Indexing and slicing work exactly like lists
print("point[0]    :", point[0])        # 3
print("point[-1]   :", point[-1])       # 5
print("rgb[0:2]    :", rgb[0:2])        # (255, 128)


# ============================================================
# 2. IMMUTABILITY - tuples CANNOT be changed
# ============================================================
# This is the headline difference from a list.

print("\n--- Immutability ---")
coords = (10, 20)
print("coords :", coords)

# Trying to change an item raises a TypeError. We catch it here just to
# show the error message without crashing the whole program.
try:
    coords[0] = 99                      # NOT allowed!
except TypeError as error:
    print("Cannot change a tuple:", error)

# A list, by contrast, WOULD allow coords[0] = 99.


# ============================================================
# 3. THE SINGLE-ELEMENT TUPLE GOTCHA
# ============================================================
# To make a tuple with ONE item you MUST add a trailing comma.
# Without the comma, the parentheses are just grouping -- not a tuple!

print("\n--- Single-element tuple ---")
not_a_tuple = (42)                      # this is just the integer 42
real_tuple = (42,)                      # THIS is a one-item tuple

print("not_a_tuple :", not_a_tuple, "->", type(not_a_tuple).__name__)  # int
print("real_tuple  :", real_tuple, "->", type(real_tuple).__name__)    # tuple

# It is actually the COMMA, not the parentheses, that builds a tuple:
also_tuple = 1, 2, 3
print("also_tuple  :", also_tuple, "->", type(also_tuple).__name__)    # tuple


# ============================================================
# 4. TUPLE PACKING and UNPACKING
# ============================================================
# PACKING: putting several values into one tuple.
# UNPACKING: pulling them back out into separate variables.

print("\n--- Packing & unpacking ---")

# Packing (no parentheses needed)
person = "Alice", 30, "Engineer"
print("packed :", person)

# Unpacking - the number of variables must match the number of items
name, age, job = person
print(f"name={name}, age={age}, job={job}")

# Extended unpacking with * to grab "the rest" into a list
first, *rest = (1, 2, 3, 4, 5)
print("first :", first)                 # 1
print("rest  :", rest)                  # [2, 3, 4, 5]


# ============================================================
# 5. SWAPPING VARIABLES VIA UNPACKING
# ============================================================
# A classic Python trick: swap two variables in a single line,
# no temporary variable needed.

print("\n--- Swapping variables ---")
a = 100
b = 200
print(f"before : a={a}, b={b}")

a, b = b, a                             # the right side packs into a tuple,
                                        # then unpacks into a and b
print(f"after  : a={a}, b={b}")


# ============================================================
# 6. WHEN TO USE A TUPLE vs A LIST
# ============================================================
# Use a TUPLE when the collection should NOT change:
#   - coordinates (x, y)
#   - RGB colours
#   - a database record (id, name, email)
#   - returning multiple values from a function
#
# Use a LIST when the collection WILL grow, shrink, or be reordered:
#   - a shopping list
#   - a queue of tasks
#   - search results

print("\n--- Tuple as a fixed record ---")
record = ("U-100", "Alice", "alice@example.com")
user_id, user_name, user_email = record
print(f"id={user_id}, name={user_name}, email={user_email}")


# ============================================================
# 7. USEFUL TUPLE METHODS: .count() and .index()
# ============================================================
# Tuples only have two methods (because they cannot change).

print("\n--- Tuple methods ---")
votes = ("yes", "no", "yes", "yes", "no")
print("count of 'yes' :", votes.count("yes"))   # 3
print("index of 'no'  :", votes.index("no"))     # 1  (first match)
print("length         :", len(votes))            # 5
print("'maybe' in?     :", "maybe" in votes)     # False


# ============================================================
# 8. HANDS-ON: A TINY COORDINATE SYSTEM
# ============================================================
# Coordinates are a perfect use for tuples: a point should not
# accidentally lose its x or y value.

print("\n--- Coordinate System ---")


def make_point(x, y):
    """Packs x and y into an (x, y) tuple."""
    return (x, y)


def distance_from_origin(point):
    """Returns the straight-line distance from (0, 0) to the point."""
    x, y = point                        # unpack the tuple
    return (x ** 2 + y ** 2) ** 0.5     # Pythagoras: sqrt(x^2 + y^2)


def midpoint(p1, p2):
    """Returns the point exactly halfway between p1 and p2."""
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)


home = make_point(0, 0)
shop = make_point(3, 4)

print("home          :", home)
print("shop          :", shop)
print("distance      :", distance_from_origin(shop))      # 5.0
print("midpoint      :", midpoint(home, shop))            # (1.5, 2.0)

# A function returning multiple values is really returning a TUPLE
def min_and_max(numbers):
    """Returns both the smallest and largest number as a tuple."""
    return min(numbers), max(numbers)

lo, hi = min_and_max([8, 2, 9, 1, 5])
print(f"lowest={lo}, highest={hi}")

print("\nDay 21 complete! You now understand tuples.")
