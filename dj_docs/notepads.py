CONF = """
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path Configuration --
import os
import sys

# Set the path to your Django project directory
django_project_path = os.path.abspath('../../')

# Add the path to your project directory to sys.path
sys.path.insert(0, django_project_path)

# Now import Django-related modules
import django
django.setup()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '{project}'
copyright = '{copyright}'
author = '{author}'
release = '{release}'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# myst_parser for markdown support

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'myst_parser',
    'sphinxcontrib.ansi',
]
ansi_lexer = 'console'
templates_path = ['_templates']
exclude_patterns = {exclude_patterns}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_theme_options = {{
    'style_nav_header_background': '#2c3e50',
    'canonical_url': 'https://example.com',
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'navigation_with_keys': True,
}}


# -- Markdown support --
source_parsers = {{
    '.md': 'recommonmark.parser.CommonMarkParser'
}}
source_suffix = {{
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}}
"""

