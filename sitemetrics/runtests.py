#! /usr/bin/env python
import sys
import os

from django.conf import settings, global_settings


def main():
    current_dir = os.path.dirname(__file__)
    app_name = os.path.basename(current_dir)
    sys.path.insert(0, os.path.join(current_dir, '..'))

    if not settings.configured:
        configure_kwargs = dict(
            INSTALLED_APPS=('django.contrib.sites', app_name),
            DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
            MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES,  # Prevents Django 1.7 warning.
        )

        try:
            configure_kwargs['TEMPLATE_CONTEXT_PROCESSORS'] = tuple(global_settings.TEMPLATE_CONTEXT_PROCESSORS) + (
                'django.core.context_processors.request',
            )

        except AttributeError:  # Django 1.10+
            configure_kwargs['TEMPLATES'] = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'APP_DIRS': True,
                },
            ]

        settings.configure(**configure_kwargs)

    try:  # Django 1.7 +
        from django import setup
        setup()
    except ImportError:
        pass

    from django.test.utils import get_runner
    runner = get_runner(settings)()
    failures = runner.run_tests((app_name,))

    sys.exit(failures)


if __name__ == '__main__':
    main()
