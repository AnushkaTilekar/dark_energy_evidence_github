# This is Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values,
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
project = 'Dark Energy Evidence'

# -------------
# [2.ii]
# Coyright Shown in the footer of every generated page
copyright = '2026, Anushka Sanjay Tilekar'

# -------------
# [2.iii]
# This author name wil be The name shown in various places - 
# the page footer, the <meta> tags, etc.
author = 'Anushka Sanjay Tilekar'

# -------------
# [2.iv]
# Telling Sphinx "the entry point of my documentation is index.rst." 
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

from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python 3.10 nd earlier (tomli is already installed as a Sphinx dependency)

_pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
with open(_pyproject_path, "rb") as f:
    _pyproject_data = tomllib.load(f)

release = _pyproject_data["project"]["version"]   # e.g. "0.1.4"
version = ".".join(release.split(".")[:2])        # e.g. "0.1"


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
