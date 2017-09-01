# -*- coding: utf-8 -*-
"""
    extlinks_plus
    ~~~~~~~~

    Extension to save typing and prevent hard-coding of base URLs in the reST
    files.

    This adds a new config value called ``extlinks_plus`` that is created like this::

       extlinks_plus = {'exmpl': ('http://example.com/%s.html', title_fmt, rev_fmt), ...}

    Now you can use e.g. :exmpl:`foo` in your documents.  This will create a
    link to ``http://example.com/foo.html``.  The link caption depends on the
    *prefix* value given:

    - If it is ``None``, the caption will be the revision.
    - If it is a string (empty or not), the caption will be formatted
      with the revision using ``title_fmt``.
    - The revision will be formatted with ``rev_fmt`` typically used to
      abbreviate long SHA1's.

    You can also give an explicit caption, e.g. :exmpl:`Foo <foo>`.

    :copyright: Copyright 2007-2017 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Works similar 
from six import iteritems
from docutils.nodes import reference
from docutils.utils import unescape
from docutils.parsers.rst.roles import set_classes
from sphinx.util.nodes import split_explicit_title

def make_ref_role(base_url, title_fmt, rev_fmt):
    def role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
        text = unescape(text)
        has_explicit_title, title, slug = split_explicit_title(text)
        if " " in slug:
            msg = inliner.reporter.error(
                '"%s" role expected a revision; '
                '"%s" is invalid.' % (typ, text), line=lineno)
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [prb], [msg]
        slug_pretty = (rev_fmt % slug)
        if has_explicit_title:
            title = title_fmt % (title, slug_pretty)
        else:
            title = slug_pretty
        ref = base_url % slug
        set_classes(options)
        node = reference(rawtext, title, refuri=ref, **options)
        return [node], []
    return role


def setup_link_roles(app):
    for name, (base_url, title_fmt, rev_fmt) in iteritems(app.config.extlinks_plus):
        app.add_role(name, make_ref_role(base_url, title_fmt, rev_fmt))


def setup(app):
    app.add_config_value('extlinks_plus', {}, 'env')
    app.connect('builder-inited', setup_link_roles)
    return {'version': '0.1', 'parallel_read_safe': True}
