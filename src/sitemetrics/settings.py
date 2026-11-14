from django.conf import settings


ON_DEBUG: bool = getattr(settings, 'SITEMETRICS_ON_DEBUG', False)
"""Whether to put metrics counter code in DEBUG mode."""


CACHE_TIMEOUT: int = 31536000
"""sitemetrics keykodes are stored in Django cache for a year (60 * 60 * 24 * 365 = 31536000 sec).
Cache is only invalidated on sitemetrics keycode change.

"""


SITE_BY_REQUEST: bool = getattr(settings, 'SITEMETRICS_SITE_BY_REQUEST', False)
"""Whether to detect the current site from the request's domain (Host header)
instead of SITE_ID from settings. Useful for multisite setups sharing one Django instance.

"""
