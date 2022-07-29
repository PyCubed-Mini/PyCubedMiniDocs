# Configuration file for the Sphinx documentation builder.

# -- Path Setup
import sys
sys.path.insert(0, '../flight_software/state_machine/applications/flight/')

# -- Project information

project = 'Pycubed-Mini'
copyright = '2022'
author = 'REX-Lab'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx-favicon',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Favicons
html_static_path = ['_static']
favicons = [
    'favicon-16x16.png',
    'favicon-32x32.png',
    'favicon.ico',
    'apple-touch-icon.png',
    'android-chrome-192x192.png',
    'android-chrome-512x512.png',
]
