from django import template
from django.core.cache import cache
from django.db.models import signals
from django.contrib.sites.models import Site

from ..models import Keycode
from ..utils import get_providers_by_alias


# sitemetrics keykodes are stored in Django cache for a year (60 * 60 * 24 * 365 = 31536000 sec).
# Cache is only invalidated on sitemetrics keycode change.
CACHE_TIMEOUT = 31536000
PROVIDERS_BY_ALIAS = get_providers_by_alias()

signals.post_save.connect(lambda **kwargs: cache.delete('sitemetrics'), sender=Keycode, weak=False)
signals.post_delete.connect(lambda **kwargs: cache.delete('sitemetrics'), sender=Keycode, weak=False)

register = template.Library()


@register.tag
def sitemetrics(parser, token):
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
    tokens = token.split_contents()
    tokens_num = len(tokens)

    if tokens_num == 1:
        # Notation Type 1
        current_site = Site.objects.get_current()

        cached = cache.get('sitemetrics')
        if not cached or current_site.id not in cached['keycodes']:
            kcodes = current_site.keycode_set.filter(active=True).values()
            cache.set('sitemetrics', {'keycodes': {current_site.id: kcodes}}, CACHE_TIMEOUT)
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

    _kcodes = []
    for kcode_data in kcodes:
        if kcode_data['provider'] in PROVIDERS_BY_ALIAS:
            p_cls = PROVIDERS_BY_ALIAS[kcode_data['provider']]
            kcode_data['tpl'] = p_cls.get_template_name()
            # Get counter parameters.
            kcode_data.update(p_cls.get_params())
            _kcodes.append(kcode_data)

    return sitemetricsNode(_kcodes)


class sitemetricsNode(template.Node):
    """Renders specified site metrics counter from template."""

    def __init__(self, keycodes):
        self.keycodes = keycodes
        self.template = template.loader.get_template('sitemetrics/sitemetrics.tpl')

    def render(self, context):
        return self.template.render(template.Context({'keycodes': self.keycodes}))
