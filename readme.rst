
**********************************************************************************
`This Week in Blender Development <https://thisweekinblenderdev.github.io/news>`__
**********************************************************************************

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

- Policy for who contributes?
  *(suggest all Blender devs get automatic access, otherwise handle on case by case basis).*
- Policy for what is an interesting commit?
  *(lets see if we need one)*.
- Should this use a mailing list?
- What theme to use, currently using ``alabaster``, could change later
  (see `Awesome Sphinx Themes <https://github.com/yoloseem/awesome-sphinxdoc#themes>`__)


To Do
=====

Test week.


Building Online Docs
====================

You will need to have the site's
`git-pages repository <https://github.com/ThisWeekInBlenderDev/news>`__ checked out just once::

   git clone git@github.com:ThisWeekInBlenderDev/news.git docs

Then updates can be made by running::

   make upload
