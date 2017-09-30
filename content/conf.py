
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join('..', 'exts')))

extensions = [
    # general
    'youtube',
    'newsfeed',
    'extlinks_plus',
    # sphinx extensions
    'sphinx.ext.githubpages',
    # installed with pip
    'sphinxjp.themes.basicstrap',
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
html_copy_source = False
html_show_sourcelink = False


def setup(app):
    app.add_stylesheet("theme_overrides.css")

html_theme = 'basicstrap'
html_theme_options = {
    'header_inverse': False,
    'relbar_inverse': False,
    'inner_theme': True,
    'inner_theme_name': 'bootswatch-flatly',
}
