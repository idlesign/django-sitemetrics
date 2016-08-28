from django.conf import settings


ON_DEBUG = getattr(settings, 'SITEMETRICS_ON_DEBUG', False)
"""Whether to put metrics counter code in DEBUG mode."""
