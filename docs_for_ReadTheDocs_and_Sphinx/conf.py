# This is Configuration file for the Sphinx documentation builder.

# End users never touch conf.py at all. 
# It's not in the wheel they download. 
# It's not even in the source distribution 
# - it lives in our repo.
# pip doesn't install repo-only files as part of the package.

# ---------------

#
# For the full list of built-in Sphinx configuration values,
# see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# For information on Sphinx Syntax used in this file,
# see the information:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# ===================================================================================================
# ===================================================================================================
# ===================================================================================================



# ------------------------- [1] PROJECT IMPORTS : ---------------------------------------------------

# -------------
# [1.i]
# Load Python's os module - to get the tools required for working with 
# file paths, directories, and the operating system

import os

# -------------
# [1.ii]
# Load Python's sys module - to get the tools required for controlling 
# how Python itself runs, including its list of "where to look for code"

import sys

# -------------
# [1.iii]
# What this line accomplishes: 
# it tells Python "when you look for importable modules, 
#                  look in the parent folder first."

sys.path.insert(0, os.path.abspath('..'))
# sys.path                - A list of folder paths that Python searches
#                            when we write import something
# os.path.abspath('..')	  - Converts the relative path ".." 
#                            (the parent folder) into a full absolute 
#                            path like "/mnt/e/brics_project/dark_energy_evidence_github"
# .insert(0, ...)	      - Adds that full path to the start of the list

# Why we need it here: 
# when Sphinx reads our .rst files and hits the line 
# ".. automodule:: dark_energy_evidence_package.data_loader",
# it needs to actually import our package. 
# Sphinx runs from inside "docs_for_ReadTheDocs_and_Sphinx/" folder,
# and by default it wouldn't know our package lives one folder up.
# This line points it there.
 
# Why ".insert(0, ...)" and not ".append(...)"?
# Inserting at position 0 puts the path at the front of the search order,
# so it takes priority over anything already installed system-wide.
# If we had a stale version of our package installed elsewhere,
# the local one wins. That's what we want during development.
 
# Alternative we didn't use: 
# some projects write "sys.path.append(...)" instead of ".insert(0, ...)".
# That also works, but is searched last. Fine in most cases, 
# but ".insert(0, ...)" is the more deliberate choice.
# -------------


# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


# ------------------------- [2] PROJECT METADATA : ---------------------------------------------------

# -------------
# [2.i]
# Defining the name displayed in the documentation's title bar and in 
# the HTML <title> tag
project = 'dark_energy_evidence_package'

# Alternatively, read the project name from "pyproject.toml" file -
#
# Method-1:
# # Convert "dark_energy_evidence_package" → "Dark Energy Evidence Package"
# _pip_name = _pyproject_data["project"]["name"]
# project = " ".join(word.capitalize() for word in _pip_name.split("_"))
#
#  OR
#
# Method-2:
# # Display name for the docs site - chosen separately in case if the 
# pip name (dark_energy_evidence_package) is not what I want shown 
# as a page title.
# project = "Dark Energy Evidence"
#
# -------------
# [2.ii]
# Coyright Shown in the footer of every generated page
copyright = '2026, ANUSHKA SANJAY TILEKAR'

# Alternatively, read the author name part from pyproject.toml file -
# copyright = f"2026, {author}"

# -------------
# [2.iii]
# This author name wil be The name shown in various places - 
# such as, the page footer, the <meta> tags, etc.
author = 'ANUSHKA SANJAY TILEKAR'

# Alternatively, read the author name from pyproject.toml file -
# author = _pyproject_data["project"]["authors"][0]["name"]

# -------------
# [2.iv]
# Telling Sphinx "the entry point of my documentation is "index.rst" file." 
# Without this, Sphinx might guess wrong in newer versions.
root_doc = "index"

# NOTE:
# Why root_doc = "index" 
# - Older Sphinx used a variable called "master_doc". 
# Newer versions renamed it "root_doc". 
# Setting it explicitly avoids a warning during the build. 
# The value "index" (without .rst) means 
# "the file index.rst in this folder is the top-level page."


# -------------
# [2.v] Project Release and Version Data -
#
# release = '0.1.4'
# Instead -
# Reading the verison dynamically from pyproject.toml as below :

# .TOML = Tom's Obvious, Minimal Language.
# It's a file format for configuration.
# It is a way to store settings in a plain text file that's easy for 
# both humans and programs to read.
# The format was created by Tom Preston-Werner (co-founder of GitHub) 
# in 2013. "Tom's Obvious, Minimal Language" is a playful name - the 
# joke being that it's "obvious" because the syntax looks like 
# what you'd naturally guess.
# TOML has very few syntax rules:
# (1) Key = value                     e.g.: version = "0.1.4"
# (2) Strings use quotes.             e.g.: name = "Anushka"
# (3) Numbers don't use quotes.       e.g.: major = 1
# (4) Booleans are true / false.      e.g.: enabled = true
# (5) Lists use square brackets.      e.g.: extensions = ["a", "b", "c"]
# (6) Sections use square brackets.   e.g.: [project] starts a new section
# (7) Comments start with #.          e.g.: # this is ignored
# (8) Nested sections use dots.       e.g.: [tool.setuptools.packages.find]
# That's essentially the whole language. There's no logic, no loops, 
# no functions - it's purely a way to store structured data.


# We have exactly one TOML file: pyproject.toml at the repo root.
# This pyproject.toml file tells Python's packaging tools:
#    (i) What this package is called ("dark_energy_evidence_package"),
#    (ii) What version it is ("0.1.4"),
#    (iii) Who made it ("Anushka Sanjay Tilekar"),
#    (iv) What dependencies it needs (numpy, astropy, matplotlib, pandas, etc.),
#    (v) How to find this package folder ([tool.setuptools.packages.find])
# So basically, everything that gets shown on our PyPI page, and 
# everything 'pip' needs to know to install this package, 
# comes from the pyproject.toml file.

# -------------
# [2.v.A]
from pathlib import Path

# (i) pathlib = Python module
# (ii) Path = A class from the Python's module named "pathlib". 
#              It represents a file path as an object with useful 
#              methods.

# -------------
# [2.v.B]
# What this try-except block does: 
# Python 3.11 and newer ship with a built-in library called "tomllib" 
# for reading ".toml" files. 
# Python 3.10 doesn't have it. 
# This try-except block says: 
# "try to use tomllib. If it's not available, fall back to tomli,
# which does the same thing."

# Why do I need this this fallback design (i.e., the try-except block) 
# at all? 
# Because I created a local environment on my machine to create this 
# repository using VS Code and named that environment "brics_project". 
# I am on Python 3.10 in my brics_project environment, and "tomllib" 
# doesn't exist there. So without this fallback design 
# (i.e., the try-except block), the import would fail. 
# But if this this fallback design (i.e., the try-except block) is 
# present, the same "conf.py" file works on Python 3.10, 3.11, 3.12, 
# and beyond - which is what I want if someone ever builds this on a 
# different machine.

# tomli vs tomllib:
# Both are libraries that read TOML files. 
# They're essentially the same library, released at different times.
# (i)  tomli   - A third-party Python library launched in year 2020 
#                and can be installed with command "pip install tomli" 
# (ii) tomllib - A offical Python module, but actually is a copy of the 
#                original "tomli" Python library, that was adopted into 
#                Python's regular  standard library, in newer Python 
#                versions (Python 3.11), launched in year 2022
# The original "tomli" Python library was created by a developer named 
# Taneli Hukkinen to fill a gap - Python had no built-in way to read 
# TOML files !
# It became popular quickly because it was well-written and fast.
# The Python core team noticed this. Rather than write their own TOML 
# reader from scratch, they adopted tomli directly into the standard 
# library in Python 3.11, renaming it tomllib. 
# The original tomli still exists on PyPI for people using Python 3.10 
# and older.
# So tomli and tomllib aren't competitors - they're the same code, 
# just distributed differently:
#   tomllib - a standard Python module that comes free with Python 3.11+
#   tomli - a Pytohn library PyPI package you install separately on 
#             older Python versions
# When I asked Google Gemini about the authorship and credit history 
# about tomli and tomli, it replied: 
# "
# The Author of original "tomli" Taneli Hukkinen was given proper  
# and complete credit for the inclusion of the tomli package into 
# the Python standard library as tomllib in Python 3.11, and 
# Taneli Hukkinen himself co-authored PEP 680, the official proposal 
# that integrated the parser into Python.
# And, the main parsing module in the CPython repository, 
# "Lib/tomllib/_parser.py", explicitly includes the SPDX copyright 
# header: "# SPDX-FileCopyrightText: 2021 Taneli Hukkinen".
# Reference:
# (i) https://www.google.com/url?sa=i&source=web&rct=j&url=https://peps.python.org/pep-0680/&ved=2ahUKEwiz_qbl9Y-XAxUVaHADHdkaCFEQ0YISeggIAggBCA0QBA&opi=89978449&cd&psig=AOvVaw1zt7l9GOOe-RJkcNXWh5u2&ust=1790638345494000
# (ii) https://www.google.com/url?sa=i&source=web&rct=j&url=https://github.com/python/cpython/blob/main/Lib/tomllib/_parser.py&ved=2ahUKEwiz_qbl9Y-XAxUVaHADHdkaCFEQ0YISeggIAggBCA0QCg&opi=89978449&cd&psig=AOvVaw1zt7l9GOOe-RJkcNXWh5u2&ust=1790638345494000
# "


try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python 3.10 nd earlier (tomli is already installed as a Sphinx dependency)

# The "as tomllib" part - 
# This aliases tomli under the name tomllib, so the rest of the code
# can just use the name tomllib regardless of which one was actually
# imported. Both libraries have identical APIs for reading TOML,
# so this works.

# The logic is:
# (1st) Try to use "tomllib" first - if the machine is on Python 3.11 
#       or newer, this succeeds and everything's fine.
# (2nd) If that fails (Python 3.10, where tomllib doesn't exist), 
#       fall back to "tomli".
# (3rd) Alias "tomli" as "tomllib" so the rest of the code can just say 
#       "tomllib.load(...)" regardless of which one actually got 
#       imported.
# Because both libraries have the exact same function names and 
# arguments, the rest of the code doesn't need to know which one 
# it's using.

# Why I can rely on tomli being installed already ?
# Because Sphinx depends on tomli under the hood, 
# so it's already in my environment when I installed Sphinx earlier 
# on my machine (by doing "pip install sphinx sphinx-rtd-theme"). 
# so I don't need to add "tomli" seperately to docs/requirements.txt files.

# When "Python 3.11" becomes the minimum supported version 
# (probably in a few years), this block could be simplified to just 
# import "tomllib". 
# But for now, it keeps our "conf.py" file usable on a wider range 
# of systems.

# Why this pattern matters?
# This is called a "compatibility shim" 
# - It is a small block of code that lets the same file run on 
# multiple versions of a library or the language. 
# The general shape is:

# (in python)
#
# try:
#     import new_thing
# except ImportError:
#     import old_thing as new_thing
#
#
# -------------
# [2.v.C]
_pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"

# -------------
# [2.v.D]
with open(_pyproject_path, "rb") as f:
    _pyproject_data = tomllib.load(f)

# -------------
# [2.v.E]
release = _pyproject_data["project"]["version"]   # e.g.: "0.1.4"

# -------------
# [2.v.F]
version = ".".join(release.split(".")[:2])        # e.g.: "0.1"

# -------------

# ===================================================================================================
# ===================================================================================================
# ===================================================================================================

# [2]
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


# [3]
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']



# ===================================================================================================
# ===================================================================================================
# ===================================================================================================
