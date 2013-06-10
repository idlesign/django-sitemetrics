django-sitemetrics
==================
http://github.com/idlesign/django-sitemetrics


What's that
-----------

django-sitemetrics is a reusable application for Django 1.1+ that offers easy integration with different site metrics service providers.



Built-in site metrics providers
-------------------------------

1. **Yandex Metrika** — http://metrika.yandex.ru/

    Provider alias: 'yandex'

2. **Google Analytics** — http://www.google.com/analytics/

    Provider alias: 'google'



How to use
----------

1. Add the `sitemetrics` application to `INSTALLED_APPS` in your settings file (usually `settings.py`)
2. Add `{% load sitemetrics %}` tag to the top of a template (usually base template, e.g. `_base.html`)

Then you have two options to add metrics counter code to your page:

* Use `four arguments` sitemetrics tag notation:

  ::

  {% sitemetrics by google for "UA-000000-0" %}


  Here: `google` - provider alias; `UA-000000-0` - keycode argument.

  That is how you put Google Analytics counter code (with 'UA-000000-0' keycode) into page.


* Use `no arguments` sitemetrics tag notation:

  ::

  {% sitemetrics %}


  That is how you put all counter codes registered and active for the current site.

  Client codes are registered with sites through Django Admin site interface.

  **Admin site** and **Sites** from Django contribs **are required** for this approach to work.

  Use **./manage.py syncdb** to install sitemetrics tables into your database.

