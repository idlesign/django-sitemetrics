from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.importlib import import_module


class MetricsProvider(object):
    """Base class for metrics providers."""

    alias = 'generic'
    title = 'Generic Provider'

    # This can be a dictionary with metrics counter parameters.
    # Those parameters will be passed into counter template file -
    # templates/sitemetrics/{alias}.html (where `alias` is a provider alias, see above).
    params = None

    @classmethod
    def get_template_name(cls):
        """Returns js counter code template path."""
        return 'sitemetrics/%s.html' % cls.alias

    @classmethod
    def get_params(cls):
        """Returns counter parameters dictionary."""
        return cls.params or {}


class Yandex(MetricsProvider):
    """Yandex Metrika - http://metrika.yandex.ru/"""

    alias = 'yandex'
    title = _('Yandex Metrika')

    params = {
        'webvisor': True,
        'clickmap': True,
        'track_links': True,
        'accurate_bounce': True,
        'no_index': False,
        'track_hash': True,
        'xml': False,
        'user_params': False,
    }


class Google(MetricsProvider):
    """Google Analytics - http://www.google.com/analytics/"""

    alias = 'google'
    title = _('Google Analytics')


def get_custom_providers():
    """Imports providers classes by paths given in SITEMETRICS_PROVIDERS setting."""

    providers = getattr(settings, 'SITEMETRICS_PROVIDERS', False)

    if not providers:
        return None

    p_clss = []
    for provider_path in providers:
        path_splitted = provider_path.split('.')
        mod = import_module('.'.join(path_splitted[:-1]))
        p_cls = getattr(mod, path_splitted[-1])
        p_clss.append(p_cls)
    return p_clss


BUILTIN_PROVIDERS = (Yandex, Google)
METRICS_PROVIDERS = get_custom_providers() or BUILTIN_PROVIDERS
