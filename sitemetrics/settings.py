from django.conf import settings

# Keycodes caching time. Invalidates on keycode changing. Default is one year.
CACHE_TIMEOUT = getattr(settings, 'SITEMETRICS_CACHE_TIMEOUT', 31536000)

# Detect site via HTTP_HOST var. Default is SITE_ID from settings.py
SITE_BY_REQUEST = getattr(settings, 'SITEMETRICS_SITE_BY_REQUEST', False)

