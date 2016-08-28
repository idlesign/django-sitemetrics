from django.conf import settings


ON_DEBUG = getattr(settings, 'SITEMETRICS_ON_DEBUG', False)
"""Whether to put metrics counter code in DEBUG mode."""


CACHE_TIMEOUT = 31536000
"""sitemetrics keykodes are stored in Django cache for a year (60 * 60 * 24 * 365 = 31536000 sec).
Cache is only invalidated on sitemetrics keycode change.

"""
