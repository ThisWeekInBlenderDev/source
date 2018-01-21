
******************************************************************************
`This Week in Blender Development <https://thisweekinblenderdev.github.io/>`__
******************************************************************************

This purpose of this repository is to try out keeping a log of weekly development activity, similar to:
`This Week in Rust <https://this-week-in-rust.org/>`__
with a focus on development - since there are already news sites for more general topics.


Content Guide
=============


Guidelines for Inclusion
------------------------

- Only include Commits/Diffs/Tasks if they include a change users might notice.
  (that includes internal changes such as optimizations or improvements to algorithms).
- Don't include changes to infrastructure (build-system, build-bot, translation tools or code-cleanups).
- Very minor changes (typo's in text or minor changes to comments or wording can also be left out).

Rule of Thumb
   if you wouldn't tap someone on the shoulder and tell them about this new and interesting change,
   leave it out :) - *assuming that someone is interested in Blender-Dev of course!*


Open Topics
-----------

- Who is the target audience?
  *Suggest developers and technical users, people who don't read commit logs but like to run daily builds.*
- Policy for who contributes?
  *(suggest all Blender devs get automatic access, otherwise handle on case by case basis).*
- Should this use a mailing list?


Contents
--------

- Commit log.
- New diff's.
- New tasks.

Maybe...

- Add-ons repository?
- Add-ons from 3rd party repos?
- Development in feature branches?


Technical Guide
===============


RestructuredText
----------------

This site uses
`Sphinx <sphinx-doc.org>`__ documentation system.

The following customization's have been made.

- Sphinx roles ``rev``, ``task``, ``diff`` roles *(only for Sphinx builds, not online preview)*.
- RSS feed via the ``newsfeed`` extension *(patched to include all weeks without explicitly listing).*
- Hosting on github pages for now *(can easily change)*.
- Theme ``basicstrap`` with customization's is working nicely.


Tools
-----


``log_from_git``
   Is available in the tools directory and helps format commits into RestructuredText.

   See ``log_from_git --help`` for details.


Building Online Docs
--------------------

You will need to have the site's
`git-pages repository <https://github.com/ThisWeekInBlenderDev/ThisWeekInBlenderDev.github.io>`__
checked out just once::

   git clone git@github.com:ThisWeekInBlenderDev/ThisWeekInBlenderDev.github.io.git docs

Then updates can be made by running::

   make upload
