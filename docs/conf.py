import sys
import os
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon']

master_doc = 'index'
autosummary_generate = True
autoclass_content = "class"
autodoc_default_flags = ["members", "no-special-members"]

project = u'greeter'
author = u'Kyle Barbary, Phil Marshall and contributors'
copyright = u'2016, ' + author
version = "0.1"
release = "0.1.0"
