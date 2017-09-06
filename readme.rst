
******************************************************************************
`This Week in Blender Development <https://thisweekinblenderdev.github.io/>`__
******************************************************************************

This purpose of this repository is to try out keeping a log of weekly development activity, similar to:
`This Week in Rust <https://this-week-in-rust.org/>`__
with a focus on development - since there are already news sites for more general topics.


Working
=======

- ``rev``, ``task``, ``diff`` roles *(only for Sphinx builds, not online preview)*.
- RSS feed via the ``newsfeed`` extension *(patched to include all weeks without explicitly listing).*
- Hosting on github pages for now *(can easily change)*.


Open Topics
===========

- Who is the target audience?
  *Suggest developers and technical users, people who don't read commit logs but like to run daily builds.*
- Policy for who contributes?
  *(suggest all Blender devs get automatic access, otherwise handle on case by case basis).*
- Policy for what is an interesting commit?
  *(lets see if we need one)*.
- Should this use a mailing list?
- What theme to use, currently using ``alabaster``, could change later
  (see `Awesome Sphinx Themes <https://github.com/yoloseem/awesome-sphinxdoc#themes>`__)


Contents
========

- Commit log.
- New diff's.
- New tasks.

Maybe...

- Add-ons repository?
- Add-ons from 3rd party repos?
- Development in feature branches?


To Do
=====

Test week.


Building Online Docs
====================

You will need to have the site's
`git-pages repository <https://github.com/ThisWeekInBlenderDev/ThisWeekInBlenderDev.github.io>`__
checked out just once::

   git clone git@github.com:ThisWeekInBlenderDev/ThisWeekInBlenderDev.github.io.git docs

Then updates can be made by running::

   make upload
