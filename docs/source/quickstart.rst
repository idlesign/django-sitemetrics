Getting started
===============

* Add the **sitemetrics** application to INSTALLED_APPS in your settings file (usually 'settings.py').
* Add `{% load sitemetrics %}` tag to the top of a template (usually base template, e.g. `_base.html`).
* Use **./manage.py syncdb** to install sitemetrics tables into your database.


Quick example
-------------

You have two options to add metrics counters code to your pages:


1. Let's add Google Analytics counter without Admin Contrib involvement add 
   a `four arguments` sitemetrics tag into your template::

     {% sitemetrics by google for "UA-000000-0" %}


   Here: `google` is a metrics provider alias; `UA-000000-0` - metrics counter keycode.


2. Now let's use `no arguments` sitemetrics tag notation to place metrics counter 
   code associated through the Admin Contrib with the current site (if any)::

     {% sitemetrics %}

You're done.


.. note:: Since v0.6.0 counter code in DEBUG mode is replaced with
   ``<!-- sitemetrics counter removed on DEBUG -->`` to keep stats clean.
   If you wish to see counter code in DEBUG set `SITEMETRICS_ON_DEBUG` to `True` in project settings file.

