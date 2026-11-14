from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.db.models import signals
from django.template.base import Parser, Token

from ..models import Keycode
from .. import settings as sm_settings
from ..utils import get_providers_by_alias

PROVIDERS_BY_ALIAS = get_providers_by_alias()

signals.post_save.connect(lambda **kwargs: cache.delete('sitemetrics'), sender=Keycode, weak=False)
signals.post_delete.connect(lambda **kwargs: cache.delete('sitemetrics'), sender=Keycode, weak=False)

register = template.Library()


def prepare_keycodes(kcodes) -> list:
    """Enriches keycode data dicts with provider template names and parameters."""
    prepared = []

    for kcode_data in kcodes:

        if kcode_data['provider'] in PROVIDERS_BY_ALIAS:
            p_cls = PROVIDERS_BY_ALIAS[kcode_data['provider']]
            kcode_data['tpl'] = p_cls.get_template_name()
            # Get counter parameters.
            kcode_data.update(p_cls.get_params())
            prepared.append(kcode_data)

    return prepared


def get_keycodes_for_host(host: str) -> list:
    """Returns active keycodes for a site with the given domain (host)."""

    cached = cache.get('sitemetrics') or {'keycodes': {}}
    kcodes = cached['keycodes'].get(host)

    if kcodes is None:

        try:
            site = Site.objects.get(domain__iexact=host)

        except Site.DoesNotExist:
            kcodes = []

        else:
            kcodes = list(site.keycode_set.filter(active=True).values())

        cached['keycodes'][host] = kcodes
        cache.set('sitemetrics', cached, sm_settings.CACHE_TIMEOUT)

    return kcodes


@register.tag
def sitemetrics(parser: Parser, token: Token):
    """Renders sitemetrics counter.
    
    Two notation types are possible:

        1. No arguments:
           {% sitemetrics %} 
           Used to render all metrics counters registered and active for the current site.
           This requires 'Admin site' and 'Sites' Django contribs.
            
        2. Four arguments:
           {% sitemetrics by yandex for "138500" %}
           Used to render custom metrics counter by definite counter id.
           This is a simple template tag with no special requirements.
    
    """
    if settings.DEBUG and not sm_settings.ON_DEBUG:
        return sitemetricsDummyNode()

    tokens = token.split_contents()
    tokens_num = len(tokens)

    if tokens_num == 1:
        # Notation Type 1

        if sm_settings.SITE_BY_REQUEST:
            # The site is detected from the request's domain at render time.
            return sitemetricsNode(None, by_request=True)

        current_site = Site.objects.get_current()

        cached = cache.get('sitemetrics')
        if not cached or current_site.id not in cached['keycodes']:
            kcodes = current_site.keycode_set.filter(active=True).values()
            cache.set('sitemetrics', {'keycodes': {current_site.id: kcodes}}, sm_settings.CACHE_TIMEOUT)
        else:
            kcodes = cached['keycodes'][current_site.id]
        
    elif tokens_num == 5:
        # Notation Type 2
        if tokens[1] == 'by' and tokens[3] == 'for':
            kcodes = [{'provider': tokens[2], 'keycode': tokens[4].strip('"')}]
        else:
            raise template.TemplateSyntaxError(
                'Four arguments `sitemetrics` tag notation should look like '
                '{%% sitemetrics by yandex for "138500" %%}.')
    else:
        raise template.TemplateSyntaxError(
            '`sitemetrics` tag requires four or no arguments. '
            'E.g. {%% sitemetrics by yandex for "138500" %%} or {%% sitemetrics %%}.')

    return sitemetricsNode(kcodes)


class sitemetricsDummyNode(template.Node):
    """Dummy node used on DEBUG to keep stats clean."""

    def render(self, context):
        return '<!-- sitemetrics counter removed on DEBUG -->'


class sitemetricsNode(template.Node):
    """Renders specified site metrics counter from template."""

    def __init__(self, keycodes, *, by_request=False):
        self.keycodes = keycodes
        self.by_request = by_request
        self.template = template.loader.get_template('sitemetrics/sitemetrics.tpl')

    def render(self, context):
        keycodes = self.keycodes

        if self.by_request:
            request = context.get('request')
            keycodes = get_keycodes_for_host(request.get_host().split(':')[0]) if request else []

        return self.template.render({'keycodes': prepare_keycodes(keycodes)})
