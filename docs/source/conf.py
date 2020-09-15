import os
import sys
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "Workshop Amazon SageMaker"
author = "Gabriel Bella Martini"

# -- General configuration ---------------------------------------------------

extensions = ["sphinx_rtd_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
pygments_style = "default"
language = "pt"
exclude_patterns = []
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_show_copyright = False
html_show_sourcelink = False
html_show_sphinx = False
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo.png"
html_theme_options = {
    "logo_only": True,
    "navigation_depth": 3,
}
html_context = {}
html_static_path = ["_static"]
