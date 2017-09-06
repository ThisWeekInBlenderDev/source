
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join('..', 'exts')))

extensions = [
    # general
    'youtube',
    'newsfeed',
    'extlinks_plus',
    # sphinx extensions
    'sphinx.ext.githubpages',
]
extlinks_plus = {
    'task': ('http://developer.blender.org/T%s', '%s: (%s)', 'T%s'),
    'diff': ('http://developer.blender.org/D%s', '%s: (%s)', 'D%s'),
    # Show 9 chars of revision (typically there is a B prefix, so 8 chars or SHA1).
    'rev': ('http://developer.blender.org/r%s', '%s: (%s)', 'r%.9s'),
}


# The suffix of source filenames.
source_suffix = '.rst'

exclude_patterns = ['template.rst']
master_doc = 'index'

# General information about the project.
project = 'This Week in Blender Development'
copyright = 'Creative Commons'

# include at end of every file
rst_epilog = """
----

.. |vertical_separator| unicode:: U+02758

`rss feed <rss.xml>`__
|vertical_separator|
:doc:`all weeks <feed>`
|vertical_separator|
`source code <https://github.com/ThisWeekInBlenderDev/source>`__
|vertical_separator|
`cc-by-sa 4.0 <https://creativecommons.org/licenses/by-sa/4.0>`__
"""

# without this it calls it 'documentation', which it's not
html_title = 'This Week in Blender Development'
html_short_title = 'This Week in Blender Dev'

# Socket logo from: https://www.blender.org/about/logo
html_logo = "../theme/blender-logo.svg"
html_favicon = "../theme/favicon.ico"
html_static_path = ["../theme"]

# visual noise for my purpose
html_show_copyright = False
html_show_sphinx = False
html_show_sourcelink = False


def setup(app):
    app.add_stylesheet("theme_overrides.css")

'''
try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
else:
    html_theme = 'haiku'

if sphinx_rtd_theme:
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
'''

html_theme = 'alabaster'
html_theme_options = {
    "show_powered_by": False,
    "analytics_id": "UA-105840115-1"
}
import alabaster
print(alabaster.__file__)
html_theme_path = [alabaster.get_path()]
