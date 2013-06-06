django-sitemetrics
==================
http://github.com/idlesign/django-sitemetrics


What's that
-----------
django-sitemetrics is a reusable application for Django 1.1+ that offers easy integration with different site metrics service providers.



Currently supported site metrics providers
------------------------------------------
1. **Yandex Metrika** — http://metrika.yandex.ru/

    Provider alias: 'yandex'

2. **Google Analytics** — http://www.google.com/analytics/

    Provider alias: 'google'



How to use
----------
1. Add the 'sitemetrics' application to 'INSTALLED_APPS' in your settings file (usually 'settings.py')
2. Add '{% load sitemetrics %}' tag to the top of a template (usually base template, e.g. 'base.html')

Then you have two options that add metrics client code to your page:

* Use so-called 'four arguments' sitemetrics tag notation:

  ::

  {% sitemetrics by google for "UA-000000-0" %}

  Here: 'google' — provider alias; 'UA-000000-0' — keycode argument.  
  That's how you put Google Analytics client code (with 'UA-000000-0' keycode) into page.  

* Use so-called 'no arguments' sitemetrics tag notation:

  ::

  {% sitemetrics %}

  That's how you put all client codes registered and active for the current site.

  | Client codes are registered with sites through Django Admin site interface.
  | '**Admin site**' and '**Sites**' from Django contrib **are required** for this option to work.
  | '**./manage.py syncdb**' is required just once for this option to work (it installs sitemetrics table into database).

