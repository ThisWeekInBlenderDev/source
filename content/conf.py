
import sys
import os
import ablog

sys.path.insert(0, os.path.abspath(os.path.join('..', 'exts')))

extensions = [
    # general
    'youtube',
    ## Remove if ablog is used.
    # 'newsfeed',
    'extlinks_plus',

    'ablog',
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

templates_path = [ablog.get_html_templates_path()]

master_doc = 'index'

# General information about the project.
project = 'This Week in Blender Development'
copyright = 'Creative Commons'

# without this it calls it 'documentation', which it's not
html_title = 'This Week in Blender Development'
html_short_title = 'This Week in Blender Dev'

# visual noise for my purpose
html_show_copyright = False
html_show_sphinx = False
html_show_sourcelink = False

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
}
import alabaster
print(alabaster.__file__)
html_theme_path = [alabaster.get_path()]
