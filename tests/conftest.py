from pytest_djangoapp import configure_djangoapp_plugin


pytest_plugins = configure_djangoapp_plugin({
    'SITEMETRICS_PROVIDERS': [
        'sitemetrics.tests.testapp.providers.CustomizedProvider',
        'sitemetrics.providers.Google',
    ],
    'INSTALLED_APPS': ['django.contrib.sites'],
})
