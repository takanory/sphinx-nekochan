# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys

from sphinx_nekochan import __version__ as version

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-nekochan'
copyright = '2025, Takanori Suzuki'
author = 'Takanori Suzuki'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx_revealjs",
    "sphinx_nekochan",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'snippets']

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = f"{project} v{release}"
html_short_title = project
html_logo = "_static/work-nya.png"
html_favicon = "_static/work-nya.png"
html_last_updated_fmt = "%Y-%m-%d"
html_static_path = ["_static"]

html_theme_options = {
    "source_repository": "https://github.com/takanory/sphinx-nekochan/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/takanory/sphinx-nekochan",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css",
]

# https://sphinxext-opengraph.readthedocs.io/
ogp_site_url = "http://sphinx-nekochan.readthedocs.io/"

# https://sphinxext-opengraph.readthedocs.io/en/latest/socialcards.html
ogp_social_cards = {
    "image": "_static/work-nya.png",
    "font": "Noto Sans CJK JP",
}

# font settings for macOS and Windows
if sys.platform == "darwin":
    ogp_social_cards["font"] = "Hiragino Maru Gothic Pro"
elif sys.platform == "win32":
    ogp_social_cards["font"] = "MS Gothic"

# https://github.com/attakei/sphinx-revealjs/blob/master/demo/revealjs4/conf.py

revealjs_style_theme = "white"
revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
]

revealjs_static_path = html_static_path

revealjs_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css",
    'slides.css',
]
