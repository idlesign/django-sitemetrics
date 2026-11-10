from typing import List, Type

from django.conf import settings
from django.utils.module_loading import import_module
from django.utils.translation import gettext_lazy as _


class MetricsProvider:
    """Base class for metrics providers."""

    alias: str = 'generic'
    title: str = 'Generic Provider'

    # This can be a dictionary with metrics counter parameters.
    # Those parameters will be passed into counter template file -
    # templates/sitemetrics/{alias}.html (where `alias` is a provider alias, see above).
    params: dict = None

    @classmethod
    def get_template_name(cls) -> str:
        """Returns js counter code template path."""
        return f'sitemetrics/{cls.alias}.html'

    @classmethod
    def get_params(cls) -> dict:
        """Returns counter parameters dictionary."""
        return cls.params or {}


class Yandex(MetricsProvider):
    """Yandex Metrika - http://metrika.yandex.ru/"""

    alias: str = 'yandex'
    title: str = _('Yandex Metrika')

    params: dict = {
        'webvisor': True,
        'clickmap': True,
        'track_links': True,
        'accurate_bounce': True,
        'no_index': False,
        'track_hash': True,
        'xml': False,
        'user_params': False,
    }


class Openstat(MetricsProvider):
    """Openstat - https://www.openstat.com/"""

    alias: str = 'openstat'
    title: str = _('Openstat')

    params: dict = {
        'image': None,
        'color': None,
        'next': 'openstat',
    }


class Google(MetricsProvider):
    """Google Analytics - http://www.google.com/analytics/"""

    alias: str = 'google'
    title: str = _('Google Analytics')


def get_custom_providers() -> List[Type[MetricsProvider]]:
    """Imports providers classes by paths given in SITEMETRICS_PROVIDERS setting."""

    providers = getattr(settings, 'SITEMETRICS_PROVIDERS', False)

    if not providers:
        return []

    p_clss = []
    for provider_path in providers:
        path_splitted = provider_path.split('.')
        mod = import_module('.'.join(path_splitted[:-1]))
        p_cls = getattr(mod, path_splitted[-1])
        p_clss.append(p_cls)

    return p_clss


BUILTIN_PROVIDERS = (
    Yandex,
    Google,
    Openstat,
)

METRICS_PROVIDERS = get_custom_providers() or BUILTIN_PROVIDERS
