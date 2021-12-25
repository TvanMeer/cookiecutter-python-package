# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "{{cookiecutter.project_name}}"
author = "{{cookiecutter.author_name}}"
copyright = "{% now 'utc', '%Y' %}, {{cookiecutter.author_name}}"

# The full version, including alpha/beta/rc tags
release = "{{cookiecutter.version}}"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "myst_parser"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Furo theme specific options.
# See https://pradyunsg.me/furo/customisation/
#
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "black",
        "color-brand-content": "black",
        "color-admonition-background": "white",
    },
    "dark_css_variables": {
        "color-brand-primary": "lightgray",
        "color-brand-content": "lightgray",
        "color-admonition-background": "#272822",
    },
    # Logo style
    "light_logo": "logo-light-mode.png",
    "dark_logo": "logo-dark-mode.png",
    "sidebar_hide_name": True,
    # Enable keyboard navigation
    "navigation_with_keys": True,
}
# Codeblock style
pygments_style = "sphinx"
pygments_dark_style = "monokai"


# -- Options for sphinx.ext.napoleon Google docstring parser ----------------

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_custom_sections = None
napoleon_attr_annotations = True


# -- Options for sphinx_autodoc_typehints -----------------------------------
# See https://github.com/agronholm/sphinx-autodoc-typehints

always_document_param_types = True

