"""
Chapter 11 - Day 29: pip, Virtual Environments & Your Own Modules
=================================================================
Topics: importing YOUR OWN module (utils.py), pip package manager,
        virtual environments, third-party packages (requests),
        and packages with __init__.py.

Run me with:  python3 day29_examples.py
This file only imports our LOCAL utils.py, so it runs with zero installs.
The pip/venv parts are explained in COMMENTS only — no commands are run.
"""

# ============================================================
# 1. IMPORTING OUR OWN MODULE
# ============================================================
# utils.py lives in the SAME folder as this file, so Python can find it.
# Three ways to bring it in (we use a mix below to show each style):

import utils                          # (a) whole module, use utils.xxx
from utils import add, is_even        # (b) specific names, no prefix
from utils import area_of_circle as circle_area  # (c) imported name + alias

print("--- 1. Using our custom utils module ---")
print(utils.greet("Subham"))          # called via the module prefix
print("add(7, 8)        =", add(7, 8))            # imported directly
print("is_even(42)      =", is_even(42))          # imported directly
print("circle_area(3)   =", circle_area(3))       # imported under an alias
print("utils.PI constant=", utils.PI)             # modules can hold constants too

# Notice: when we imported utils, its `if __name__ == "__main__":` self-test
# did NOT run. That block only fires when you run `python3 utils.py` directly.


# ============================================================
# 2. COMBINING OUR FUNCTIONS INTO A SMALL PROGRAM
# ============================================================
print("\n--- 2. A mini program built from utils ---")
numbers = [10, 7, 4, 3, 8]
even_numbers = []
for n in numbers:
    if is_even(n):
        even_numbers.append(n)
print("Original numbers:", numbers)
print("Even numbers    :", even_numbers)
print("Sum of evens    :", utils.add(sum(even_numbers), 0))


# ============================================================
# 3. pip — THE PACKAGE MANAGER  (concept only, nothing is installed)
# ============================================================
# pip downloads and installs third-party packages from PyPI
# (the Python Package Index, https://pypi.org). Common commands:
#
#   pip install requests          # install a package
#   pip install requests==2.31.0  # install an EXACT version
#   pip list                      # show all installed packages
#   pip show requests             # details about one package
#   pip uninstall requests        # remove a package
#   pip freeze                    # list packages in requirements format
#   pip freeze > requirements.txt # SAVE the exact versions to a file
#   pip install -r requirements.txt  # REINSTALL everything from that file
#
# A requirements.txt file pins your project's dependencies so a teammate
# can recreate the exact same environment. It looks like:
#
#   requests==2.31.0
#   rich==13.7.0
print("\n--- 3. pip ---")
print("pip is run in the TERMINAL, not inside Python. See the comments above.")


# ============================================================
# 4. VIRTUAL ENVIRONMENTS  (concept only, nothing is created)
# ============================================================
# WHY ISOLATE?
# Project A might need requests v2.20 while Project B needs v2.31.
# Installing everything globally causes version clashes. A virtual
# environment ("venv") gives each project its own private box of packages.
#
#   python3 -m venv .venv      # create a venv in a folder named .venv
#
#   # Activate it (then your terminal prompt usually shows "(.venv)"):
#   source .venv/bin/activate    # macOS / Linux
#   .venv\Scripts\activate       # Windows
#
#   pip install requests         # installs ONLY inside this venv now
#
#   deactivate                   # leave the venv, back to global Python
#
# After activating, `pip install` and `python` point at the venv's private
# copies — so projects never step on each other's toes.
print("\n--- 4. Virtual environments ---")
print("A venv keeps each project's packages separate. See comments above.")


# ============================================================
# 5. THIRD-PARTY PACKAGES — the `requests` example (concept only)
# ============================================================
# `requests` is the most popular library for fetching data over the web.
# It is NOT built in, so you must install it first (inside your venv):
#
#   pip install requests
#
# Then you could use it like this (DO NOT run here — it needs the install
# and an internet connection):
#
#   import requests
#   response = requests.get("https://api.github.com")
#   print(response.status_code)   # 200 means success
#   print(response.json())        # parse the JSON body into a dict
#
# The pattern is always: install with pip -> import -> use.
print("\n--- 5. Third-party packages ---")
print("'requests' would be installed with pip, then imported. Concept only.")


# ============================================================
# 6. PACKAGES — many modules grouped in a folder (__init__.py)
# ============================================================
# A MODULE is one .py file. A PACKAGE is a FOLDER of modules.
# Putting a file named __init__.py inside the folder tells Python
# "treat this folder as a package". Example layout:
#
#   mytools/
#       __init__.py          <- marks the folder as a package (can be empty)
#       math_helpers.py
#       text_helpers.py
#
# Then you import from it with dotted paths:
#
#   from mytools.math_helpers import add
#   import mytools.text_helpers
#
# That's the same idea as our single utils.py module, just scaled up
# into an organised, multi-file collection.
print("\n--- 6. Packages ---")
print("A package is a folder of modules marked by an __init__.py file.")


# ============================================================
# 7. WRAP-UP
# ============================================================
if __name__ == "__main__":
    print("\n--- 7. Done! ---")
    print("You imported a custom module and used its functions successfully.")
