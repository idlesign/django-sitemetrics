from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class MetricsProvider(object):
    """Base class for metrics providers."""

    @classmethod
    def get_template_name(cls):
        """Returns js counter code template path."""
        return 'sitemetrics/%s.html' % cls.alias


class Yandex(MetricsProvider):
    """Yandex Metrika - http://metrika.yandex.ru/"""

    alias = 'yandex'
    title = _('Yandex Metrika')


class Google(MetricsProvider):
    """Google Analytics - http://www.google.com/analytics/"""

    alias = 'google'
    title = _('Google Analytics')


BUILTIN_PROVIDERS = (Yandex, Google)
METRICS_PROVIDERS = getattr(settings, 'SITEMETRICS_PROVIDERS', False) or BUILTIN_PROVIDERS
