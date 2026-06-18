# =============================================================================
# Chapter 04 — Strings In-Depth
# Day 9: String Formatting and Key String Methods
# =============================================================================
# Run this file: python day9_examples.py
# =============================================================================


# -----------------------------------------------------------------------------
# SECTION 1: f-strings (Python 3.6+) — the modern standard
# -----------------------------------------------------------------------------

print("=" * 60)
print("SECTION 1: f-strings")
print("=" * 60)

# Basic f-string: prefix the string with f, put expressions inside {}
name = "Alice"
age = 30
city = "New York"

print(f"Hello, {name}!")
print(f"Name: {name}, Age: {age}, City: {city}")

# Any Python expression is valid inside {}
price = 19.99
quantity = 3
print(f"Unit price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity}")           # arithmetic expression
print(f"Total rounded: ${price * quantity:.2f}")   # 2 decimal places

# Calling methods inside {}
raw_name = "  bob smith  "
print(f"Clean name: {raw_name.strip().title()}")   # Bob Smith

# Using conditionals inside {}
score = 87
grade = "Pass" if score >= 50 else "Fail"
print(f"Score: {score} → {grade}")

# f-string with format specifiers
pi = 3.14159265358979
print(f"\nFormat specifier examples:")
print(f"  Pi (default):        {pi}")
print(f"  Pi (2 decimals):     {pi:.2f}")
print(f"  Pi (4 decimals):     {pi:.4f}")
print(f"  Pi (scientific):     {pi:.2e}")

# Integer formatting
number = 42
large  = 1_000_000
print(f"  Zero-padded:         {number:05d}")     # 00042
print(f"  Right-aligned (10):  {number:>10}")     # spaces on left
print(f"  Left-aligned (10):   {number:<10}|")    # spaces on right
print(f"  Centered (10):       {number:^10}|")    # spaces both sides
print(f"  With commas:         {large:,}")         # 1,000,000
print(f"  With underscores:    {large:_}")         # 1_000_000

# String alignment (useful for building tables)
print()
print("Name table using f-string alignment:")
print(f"  {'Name':<15} {'Age':>4} {'City':<12}")
print(f"  {'-'*15} {'-'*4} {'-'*12}")
people = [("Alice", 30, "New York"), ("Bob", 25, "London"), ("Charlie", 35, "Tokyo")]
for p_name, p_age, p_city in people:
    print(f"  {p_name:<15} {p_age:>4} {p_city:<12}")

# Debugging with = (Python 3.8+)
x = 42
y = 3.14
print(f"\nDebugging output:")
print(f"  {x=}")        # x=42  — prints name AND value
print(f"  {y=}")        # y=3.14
print(f"  {x + y = }")  # x + y = 45.14  — works with expressions too


# -----------------------------------------------------------------------------
# SECTION 2: .format() method — for compatibility with older Python
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 2: .format() method")
print("=" * 60)

# Positional placeholders (order matters)
msg = "Hello, {}! You are {} years old.".format("Alice", 30)
print(msg)

# Named placeholders (order doesn't matter)
msg = "Hello, {name}! You are {age} years old.".format(age=30, name="Alice")
print(msg)

# Indexed placeholders (reuse values)
msg = "{0} loves {1}. {0} also loves {2}.".format("Alice", "Python", "coffee")
print(msg)   # Alice loves Python. Alice also loves coffee.

# Format specifiers work the same as in f-strings
print("{:.2f}".format(3.14159))    # 3.14
print("{:>10}".format("right"))    # right-aligned
print("{:05d}".format(42))         # 00042

# When to use .format() vs f-strings:
# - f-strings:   readable, fast, evaluates immediately — use for NEW code
# - .format():   template stored as a variable — handy for reusable templates

template = "Dear {name}, your order #{order_id} has shipped to {city}."
print(template.format(name="Bob", order_id=12345, city="London"))

# f-strings cannot store templates (they evaluate when written):
# template = f"Dear {name}..."  ← 'name' must exist NOW when this line runs


# -----------------------------------------------------------------------------
# SECTION 3: Case Methods — upper(), lower(), title(), capitalize()
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 3: Case Methods")
print("=" * 60)

text = "hello, world!"
print(f"Original:    '{text}'")
print(f"upper():     '{text.upper()}'")       # HELLO, WORLD!
print(f"lower():     '{text.lower()}'")       # hello, world!

mixed = "the quick BROWN fox"
print(f"\nOriginal:    '{mixed}'")
print(f"title():     '{mixed.title()}'")      # The Quick Brown Fox (first letter of each word)
print(f"capitalize():'{mixed.capitalize()}'") # The quick brown fox (first letter of string)

# IMPORTANT: methods return NEW strings — original is unchanged
word = "python"
upper = word.upper()
print(f"\nAfter calling .upper():")
print(f"  original: '{word}'")    # still 'python'
print(f"  upper:    '{upper}'")   # 'PYTHON'

# Practical: case-insensitive comparison
user_input = "YES"
if user_input.lower() == "yes":
    print("\nUser said yes!")

# Practical: normalize a tag for a database
raw_tag = "  Machine LEARNING  "
normalized_tag = raw_tag.strip().lower().replace(" ", "_")
print(f"\nTag: '{raw_tag}' → '{normalized_tag}'")   # machine_learning


# -----------------------------------------------------------------------------
# SECTION 4: strip(), lstrip(), rstrip()
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 4: strip() — Remove Edge Whitespace")
print("=" * 60)

# Whitespace = spaces, tabs, newlines
messy = "   hello world   \n"
print(f"Original (repr):  {repr(messy)}")
print(f"strip():  {repr(messy.strip())}")     # 'hello world'
print(f"lstrip(): {repr(messy.lstrip())}")    # 'hello world   \n'
print(f"rstrip(): {repr(messy.rstrip())}")    # '   hello world'

# Strip specific characters
print()
print("Strip specific characters:")
bordered = "###hello###"
print(f"  '{bordered}'.strip('#') = '{bordered.strip('#')}'")       # hello

dotted = "...wow..."
print(f"  '{dotted}'.strip('.') = '{dotted.strip('.')}'")           # wow

mixed_border = "---=== TITLE ===---"
print(f"  '{mixed_border}'.strip('-=') = '{mixed_border.strip('-=')}'")   # ' TITLE '

# CRITICAL: always strip user input
print()
print("Why .strip() matters for user input:")
# Simulate: user types "Alice " with a trailing space
user_name_raw = "Alice "
user_name_clean = user_name_raw.strip()
print(f"  Raw input:   '{user_name_raw}' == 'Alice' → {user_name_raw == 'Alice'}")   # False!
print(f"  Stripped:    '{user_name_clean}' == 'Alice' → {user_name_clean == 'Alice'}")  # True


# -----------------------------------------------------------------------------
# SECTION 5: split() — Break a String Into Parts
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 5: split()")
print("=" * 60)

# Default: split on any whitespace (spaces, tabs, newlines)
sentence = "The quick brown fox"
words = sentence.split()
print(f"Sentence: '{sentence}'")
print(f"split():  {words}")          # ['The', 'quick', 'brown', 'fox']
print(f"Words:    {len(words)}")     # 4

# Split on a specific separator
csv_line = "Alice,30,Engineer,New York"
parts = csv_line.split(",")
print(f"\nCSV line: '{csv_line}'")
print(f"split(','): {parts}")        # ['Alice', '30', 'Engineer', 'New York']

# Access individual fields
print(f"  Name:       {parts[0]}")
print(f"  Age:        {parts[1]}")
print(f"  Job:        {parts[2]}")
print(f"  City:       {parts[3]}")

# Split with maxsplit: limit number of splits
data = "one:two:three:four:five"
print(f"\n'{data}'.split(':')          = {data.split(':')}")
print(f"'{data}'.split(':', 2)       = {data.split(':', 2)}")    # ['one', 'two', 'three:four:five']
print(f"'{data}'.split(':', 1)       = {data.split(':', 1)}")    # ['one', 'two:three:four:five']

# Splitting handles multiple spaces correctly (default split)
messy = "  hello   world   python  "
print(f"\nMessy string: '{messy}'")
print(f"split():       {messy.split()}")    # ['hello', 'world', 'python']  — no empty strings!
print(f"split(' '):    {messy.split(' ')}")  # includes empty strings!

# split() + strip() combo: parse a header line from a file
header_line = "  Name  |  Age  |  City  "
columns = [col.strip() for col in header_line.split("|")]
print(f"\nHeader: '{header_line}'")
print(f"Columns: {columns}")   # ['Name', 'Age', 'City']


# -----------------------------------------------------------------------------
# SECTION 6: replace() — Substitute Substrings
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 6: replace()")
print("=" * 60)

text = "I like cats. Cats are great. I have two cats."
print(f"Original: '{text}'")

# Replace all occurrences
new_text = text.replace("cats", "dogs")
print(f"replace('cats','dogs'): '{new_text}'")
# Note: 'Cats' (capital C) was NOT replaced — case-sensitive!

# Replace with empty string to delete
messy = "h-e-l-l-o"
clean = messy.replace("-", "")
print(f"\n'{messy}'.replace('-','') = '{clean}'")   # hello

# Remove all spaces
with_spaces = "hello world python"
no_spaces = with_spaces.replace(" ", "")
print(f"'{with_spaces}'.replace(' ','') = '{no_spaces}'")   # helloworldpython

# Replace only N occurrences with the count argument
text = "aaa bbb aaa ccc aaa"
print(f"\nOriginal: '{text}'")
print(f"replace('aaa','XXX'):    '{text.replace('aaa', 'XXX')}'")       # all
print(f"replace('aaa','XXX',1): '{text.replace('aaa', 'XXX', 1)}'")    # first only
print(f"replace('aaa','XXX',2): '{text.replace('aaa', 'XXX', 2)}'")    # first two

# Case-insensitive replace: must lower/upper first or use re module
sentence = "I LOVE Python. Python is great. python rocks!"
# Replace all case variants — simplified approach
result = sentence.replace("Python", "Rust").replace("python", "Rust").replace("PYTHON", "Rust")
# Proper approach would use re.sub(r'(?i)python', 'Rust', sentence)
print(f"\nAfter manual case replacement: '{result}'")


# -----------------------------------------------------------------------------
# SECTION 7: find() — Locate a Substring
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 7: find()")
print("=" * 60)

text = "Hello, World! Hello, Python!"

# Returns index of FIRST occurrence, or -1 if not found
print(f"text: '{text}'")
print(f"find('Hello'):   {text.find('Hello')}")     # 0
print(f"find('World'):   {text.find('World')}")     # 7
print(f"find('Python'):  {text.find('Python')}")    # 21
print(f"find('xyz'):     {text.find('xyz')}")       # -1  (not found — no error!)

# find with a start position: find(sub, start)
print(f"\nFind 'Hello' starting from index 5:")
print(f"  find('Hello', 5) = {text.find('Hello', 5)}")   # 14 (second 'Hello')

# Find all occurrences manually
print(f"\nAll positions of 'l' in '{text}':")
positions = []
idx = 0
while True:
    pos = text.find("l", idx)
    if pos == -1:
        break
    positions.append(pos)
    idx = pos + 1
print(f"  Positions: {positions}")

# Practical: extract domain from email
email = "alice@example.com"
at_pos = email.find("@")
if at_pos != -1:
    username = email[:at_pos]
    domain   = email[at_pos + 1:]
    print(f"\nEmail: '{email}'")
    print(f"  Username: '{username}'")
    print(f"  Domain:   '{domain}'")

# rfind(): find the LAST occurrence (searches right to left)
text = "apple banana cherry banana apple"
print(f"\ntext: '{text}'")
print(f"find('banana'):  {text.find('banana')}")    # 6  (first)
print(f"rfind('banana'): {text.rfind('banana')}")   # 20 (last)


# -----------------------------------------------------------------------------
# SECTION 8: startswith() and endswith()
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 8: startswith() and endswith()")
print("=" * 60)

filename = "report_2024_final.pdf"
print(f"filename: '{filename}'")
print(f"startswith('report'): {filename.startswith('report')}")    # True
print(f"startswith('notes'):  {filename.startswith('notes')}")     # False
print(f"endswith('.pdf'):     {filename.endswith('.pdf')}")         # True
print(f"endswith('.txt'):     {filename.endswith('.txt')}")         # False

# Check multiple options with a tuple
print(f"endswith(('.pdf','.docx','.txt')): {filename.endswith(('.pdf', '.docx', '.txt'))}")  # True

# Practical: categorize files by extension
file_list = [
    "photo.jpg", "report.pdf", "song.mp3", "video.mp4",
    "data.csv", "script.py", "archive.zip", "image.png"
]
images    = [f for f in file_list if f.endswith((".jpg", ".png", ".gif"))]
documents = [f for f in file_list if f.endswith((".pdf", ".docx", ".txt", ".csv"))]
code      = [f for f in file_list if f.endswith((".py", ".js", ".ts"))]

print(f"\nImages:    {images}")
print(f"Documents: {documents}")
print(f"Code:      {code}")

# Practical: check URL protocol
urls = ["https://secure.com", "http://old.com", "ftp://files.com"]
for url in urls:
    if url.startswith("https"):
        print(f"  SECURE:  {url}")
    elif url.startswith("http"):
        print(f"  PLAIN:   {url}")
    else:
        print(f"  OTHER:   {url}")


# -----------------------------------------------------------------------------
# SECTION 9: count(), join(), zfill(), and other useful methods
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 9: More String Methods")
print("=" * 60)

# count(): number of non-overlapping occurrences
text = "banana"
print(f"'{text}'.count('a')  = {text.count('a')}")     # 3
print(f"'{text}'.count('an') = {text.count('an')}")    # 2
print(f"'{text}'.count('na') = {text.count('na')}")    # 2

# Practical: count vowels
sentence = "Hello World Python"
vowels = "aeiouAEIOU"
vowel_count = sum(sentence.count(v) for v in vowels)
print(f"\nVowels in '{sentence}': {vowel_count}")

# join(): the reverse of split()
words = ["Python", "is", "awesome"]
print(f"\nwords = {words}")
print(f"' '.join(words)  = '{' '.join(words)}'")    # Python is awesome
print(f"'-'.join(words)  = '{'-'.join(words)}'")    # Python-is-awesome
print(f"''.join(words)   = {''.join(words)}")       # Pythonisawesome
print(f"', '.join(words) = '{', '.join(words)}'")   # Python, is, awesome

# Practical: join path components
path_parts = ["Users", "Alice", "Documents", "report.pdf"]
path = "/".join(path_parts)
print(f"\nPath: '/{path}'")    # /Users/Alice/Documents/report.pdf

# zfill(): pad with leading zeros
print("\nzfill() examples:")
print(f"  '42'.zfill(5)   = '{'42'.zfill(5)}'")      # 00042
print(f"  '7'.zfill(3)    = '{'7'.zfill(3)}'")        # 007
print(f"  '1234'.zfill(3) = '{'1234'.zfill(3)}'")     # 1234 (no truncation)

# isdigit(), isalpha(), isalnum(), isspace() — check string content
tests = ["12345", "hello", "hello123", "   ", "Hello World", "3.14"]
print("\nContent checks:")
for t in tests:
    print(f"  {repr(t):15} isdigit={str(t.isdigit()):5}  isalpha={str(t.isalpha()):5}  isalnum={str(t.isalnum()):5}  isspace={str(t.isspace()):5}")


# -----------------------------------------------------------------------------
# SECTION 10: Method Chaining
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 10: Method Chaining")
print("=" * 60)

# Each method returns a new string, so you can chain them
raw = "   Hello, World!   "

# Step by step (equivalent, more readable for learning):
step1 = raw.strip()                        # "Hello, World!"
step2 = step1.lower()                      # "hello, world!"
step3 = step2.replace("world", "python")   # "hello, python!"

print(f"After strip():   '{step1}'")
print(f"After lower():   '{step2}'")
print(f"After replace(): '{step3}'")

# Chained (same result, fewer variables):
result = raw.strip().lower().replace("world", "python")
print(f"\nChained result:  '{result}'")

# More chain examples
print()
user_tag = "  Machine LEARNING  "
clean_tag = user_tag.strip().lower().replace(" ", "-")
print(f"Tag '{user_tag}' → '{clean_tag}'")     # machine-learning

# Clean a messy CSV field value
field = '  "  New York  "  '
clean_field = field.strip().strip('"').strip()
print(f"Field {repr(field)} → '{clean_field}'")   # New York

# Be careful not to over-chain — hard to read
complex_result = (
    "  hello WORLD python  "
    .strip()
    .title()
    .replace("World", "Universe")
    .split()
)
print(f"\nComplex chain result: {complex_result}")   # ['Hello', 'Universe', 'Python']


# -----------------------------------------------------------------------------
# SECTION 11: Hands-On — Name Formatter
# =============================================================================
# Goal: Take a messy raw name in any format and produce a clean "First Last" string.
# Handles: leading/trailing whitespace, extra internal spaces, mixed case.
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 11: Hands-On — Name Formatter")
print("=" * 60)


def format_name(raw_name):
    """
    Format a raw name string to 'First Last' (Title Case).

    Args:
        raw_name (str): Name in any format (messy whitespace, wrong case).

    Returns:
        str: Cleaned, properly capitalized name.

    Examples:
        format_name("  JOHN   doe  ")  →  "John Doe"
        format_name("alice")           →  "Alice"
        format_name("BOB SMITH")       →  "Bob Smith"
    """
    # Step 1: Remove leading and trailing whitespace
    stripped = raw_name.strip()

    # Step 2: Split on whitespace — handles multiple spaces between words
    parts = stripped.split()

    # Step 3: Title-case each part, then join with a single space
    formatted = " ".join(part.title() for part in parts)

    return formatted


# Test the formatter
raw_names = [
    "  JOHN   doe  ",
    "alice",
    "BOB SMITH",
    "  mary   JANE   watson  ",
    "FIRSTNAME",
    "  first  second  third  ",
]

print("Name Formatter Results:")
print(f"  {'Raw Input':<30}  {'Formatted Output'}")
print(f"  {'-'*30}  {'-'*20}")
for raw in raw_names:
    formatted = format_name(raw)
    print(f"  {repr(raw):<30}  '{formatted}'")


# Extended: format_full_name with title and suffix
def format_full_name(first, last, title=None, suffix=None):
    """Format a full name with optional title and suffix."""
    first_clean = first.strip().title()
    last_clean  = last.strip().title()

    name = f"{first_clean} {last_clean}"
    if title:
        name = f"{title.strip()}. {name}"
    if suffix:
        name = f"{name}, {suffix.strip()}"
    return name


print()
print("Extended Name Formatter:")
print(format_full_name("john",   "doe"))                   # John Doe
print(format_full_name("jane",   "smith",  title="Dr"))   # Dr. Jane Smith
print(format_full_name("robert", "brown",  suffix="Jr"))  # Robert Brown, Jr
print(format_full_name("alice",  "jones",  title="Prof", suffix="PhD"))  # Prof. Alice Jones, PhD


# -----------------------------------------------------------------------------
# SECTION 12: Hands-On — CSV-like String Parser
# =============================================================================
# Goal: Manually parse a CSV (Comma-Separated Values) line without any library.
# Demonstrates: split(), strip(), type conversion, f-strings, and error handling.
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 12: Hands-On — CSV-like String Parser")
print("=" * 60)


def parse_person_csv(csv_line):
    """
    Parse a CSV line in the format: name, age, job, city

    Args:
        csv_line (str): Comma-separated string with optional extra whitespace.

    Returns:
        dict: Dictionary with keys 'name', 'age', 'job', 'city'.

    Raises:
        ValueError: If the line does not have exactly 4 fields.
    """
    # Step 1: Split on comma to get raw fields
    raw_fields = csv_line.split(",")

    # Step 2: Validate field count
    if len(raw_fields) != 4:
        raise ValueError(
            f"Expected 4 fields, got {len(raw_fields)}. Line: '{csv_line}'"
        )

    # Step 3: Strip whitespace from each field
    fields = [field.strip() for field in raw_fields]

    # Step 4: Extract and convert each field to the right type
    name = fields[0]
    age  = int(fields[1])      # convert string "30" → integer 30
    job  = fields[2]
    city = fields[3]

    return {"name": name, "age": age, "job": job, "city": city}


def print_person(person):
    """Print a person dictionary in a nice format."""
    print(f"  Name:       {person['name']}")
    print(f"  Age:        {person['age']}")
    print(f"  Occupation: {person['job']}")
    print(f"  City:       {person['city']}")
    print(
        f"  Summary:    {person['name']} is a {person['age']}-year-old "
        f"{person['job']} from {person['city']}."
    )


# Test with a single line
csv_line = "  Alice , 30 , Software Engineer , New York  "
print(f"Input: '{csv_line}'")
print()
person = parse_person_csv(csv_line)
print_person(person)

# Parse a small "CSV file" (list of lines)
csv_data = """Alice, 30, Software Engineer, New York
Bob, 25, Data Scientist, London
Charlie, 35, Product Manager, Tokyo
Diana, 28, DevOps Engineer, Berlin"""

print()
print("Parsing a multi-line CSV:")
print("=" * 50)
lines = csv_data.strip().split("\n")   # split file content into individual lines
for i, line in enumerate(lines, start=1):
    print(f"\nRecord {i}: '{line}'")
    try:
        person = parse_person_csv(line)
        print_person(person)
    except ValueError as e:
        print(f"  ERROR: {e}")

# Error handling: malformed line
print()
print("Testing error handling:")
bad_lines = [
    "Alice, 30, Engineer",           # only 3 fields
    "Bob, 25, Analyst, London, UK",  # 5 fields
]
for bad_line in bad_lines:
    print(f"\nInput: '{bad_line}'")
    try:
        parse_person_csv(bad_line)
    except ValueError as e:
        print(f"  Caught error: {e}")


# Bonus: build the CSV back from parsed data
print()
print("Bonus: Reconstructing CSV from parsed data:")
csv_lines = [
    "Alice, 30, Software Engineer, New York",
    "Bob, 25, Data Scientist, London",
]
records = [parse_person_csv(line) for line in csv_lines]

# Reconstruct — join fields with ", "
print("Reconstructed CSV:")
for rec in records:
    reconstructed = ", ".join([rec["name"], str(rec["age"]), rec["job"], rec["city"]])
    print(f"  {reconstructed}")


# -----------------------------------------------------------------------------
# SECTION 13: Summary — All Methods at a Glance
# -----------------------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 13: Quick Method Reference")
print("=" * 60)

sample = "  Hello, World!  "
print(f"Sample string: {repr(sample)}")
print()

demo_cases = [
    ("upper()",          sample.strip().upper()),
    ("lower()",          sample.strip().lower()),
    ("title()",          sample.strip().title()),
    ("capitalize()",     sample.strip().capitalize()),
    ("strip()",          sample.strip()),
    ("lstrip()",         sample.lstrip()),
    ("rstrip()",         sample.rstrip()),
    ("split()",          str(sample.strip().split())),
    ("split(',')",       str(sample.strip().split(","))),
    ("replace('!','')",  sample.strip().replace("!", "")),
    ("find('World')",    str(sample.strip().find("World"))),
    ("count('l')",       str(sample.strip().count("l"))),
    ("startswith('H')",  str(sample.strip().startswith("H"))),
    ("endswith('!')",    str(sample.strip().endswith("!"))),
]

for method, result in demo_cases:
    print(f"  .{method:<25} → {result}")


print()
print("Day 9 complete! Chapter 04 done. On to Chapter 05: Control Flow!")
