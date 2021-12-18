django-sitemetrics
==================
http://github.com/idlesign/django-sitemetrics

.. image:: https://img.shields.io/pypi/v/django-sitemetrics.svg
    :target: https://pypi.python.org/pypi/django-sitemetrics

.. image:: https://img.shields.io/pypi/l/django-sitemetrics.svg
    :target: https://pypi.python.org/pypi/django-sitemetrics

.. image:: https://img.shields.io/coveralls/idlesign/django-sitemetrics/master.svg
    :target: https://coveralls.io/r/idlesign/django-sitemetrics


What's that
-----------

Reusable application for Django providing easy means to integrate site metrics counters into your sites



Built-in site metrics providers
-------------------------------

1. **Yandex Metrika** - http://metrika.yandex.ru/

    Provider alias: `yandex`

2. **Google Analytics** - http://www.google.com/analytics/

    Provider alias: `google`

3. **Openstat** - https://www.openstat.com/

    Provider alias: `openstat`


How to use
----------

1. Add the ``sitemetrics`` application to ``INSTALLED_APPS`` in your settings file (usually ``settings.py``)
2. Add ``{% load sitemetrics %}`` tag to the top of a template (usually base template, e.g. ``_base.html``)

Then you have two options to add metrics counter code to your page:

* Use ``four arguments`` sitemetrics tag notation:

  .. code-block:: html+django

        {% sitemetrics by google for "UA-000000-0" %}


  Here: ``google`` is a metrics provider alias; ``UA-000000-0`` - metrics counter keycode.

  That is how you put Google Analytics counter code (with ``UA-000000-0`` keycode) into page.


* Use ``no arguments`` sitemetrics tag notation:

  .. code-block:: html+django

        {% sitemetrics %}


  That is how you put all counter codes registered and active for the current site.

  Client codes are registered with sites through Django Admin site interface.

  **Admin site** and **Sites** from Django contribs **are required** for this approach to work.

  Use ``./manage.py migrate`` to install sitemetrics tables into your database.



Documentation
-------------

http://django-sitemetrics.readthedocs.org/
