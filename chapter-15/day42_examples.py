"""
Chapter 15 - Day 42: Polish - colored output and input validation
==================================================================
A working program is great. A program that's pleasant to use is greater.
Today we add two finishing touches:

  1. Colored terminal output using ANSI escape codes.
  2. Input validation - cleaning and checking what the user gives us.

(For Windows-proof colors, the 'colorama' library does the same thing across
all platforms: pip install colorama, then colorama.init(). We use plain ANSI
here so there's nothing to install.)
"""


# ============================================================
# 1. ANSI COLOR CODES
# ============================================================
# An ANSI code is a magic text sequence the terminal reads as "change color".
# It starts with \033[ , has a number, and ends with m. \033[0m resets.
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def color(text, code):
    """Wrap text so it prints in a color, then reset to normal."""
    return f"{code}{text}{RESET}"


print(color("This is a success message.", GREEN))
print(color("This is an error message.", RED))
print(color("This is a warning.", YELLOW))
print(color("This is bold.", BOLD))


# ============================================================
# 2. INPUT VALIDATION
# ============================================================
# Never trust input blindly. Clean it, then check it.

def clean_title(raw):
    """
    Validates a task title.
    Returns the cleaned title, or None if it is not acceptable.
    """
    title = raw.strip()                 # remove leading/trailing spaces
    if not title:                       # empty after stripping?
        return None
    if len(title) > 100:                # too long? trim it.
        title = title[:100]
    return title


print("\nValidating titles:")
for sample in ["  Buy milk  ", "", "   ", "Read a book"]:
    cleaned = clean_title(sample)
    if cleaned is None:
        print(color(f"  {sample!r:15} -> rejected (empty)", RED))
    else:
        print(color(f"  {sample!r:15} -> accepted: {cleaned!r}", GREEN))


# ============================================================
# 3. VALIDATING AN ID IS A POSITIVE NUMBER
# ============================================================
def parse_id(raw):
    """Returns a positive int, or None if the input is invalid."""
    try:
        value = int(raw)
    except (ValueError, TypeError):
        return None
    return value if value > 0 else None


print("\nValidating ids:")
for sample in ["1", "0", "-3", "abc", "42"]:
    result = parse_id(sample)
    label = result if result is not None else "rejected"
    print(f"  {sample!r:6} -> {label}")

print("\nDay 42 done: the app is colorful, validated, and ready to share.")
