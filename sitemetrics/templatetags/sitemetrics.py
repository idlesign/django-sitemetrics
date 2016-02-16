from django import template
from django.core.cache import cache
from django.db.models import signals
from django.contrib.sites.models import Site
from ..models import Keycode
from ..utils import get_providers_by_alias
from .. import settings

signals.post_save.connect(
    lambda **kwargs: cache.delete('sitemetrics'),
    sender=Keycode,
    weak=False
)
signals.post_delete.connect(
    lambda **kwargs: cache.delete('sitemetrics'),
    sender=Keycode,
    weak=False
)

register = template.Library()


@register.tag
def sitemetrics(parser, token):
    """Renders sitemetrics counter.

    Two notation types are possible:

        1. No arguments:
           {% sitemetrics %}
           Used to render all metrics counters registered and activated
           for the current site in the Django admin interface.
           This requires 'Admin site' and 'Sites' Django contribs.

        2. Four arguments:
           {% sitemetrics by yandex for "138500" %}
           Used to render custom metrics counter by definite counter id.
           This is a simple template tag with no special requirements.

    """

    tokens = token.split_contents()

    if len(tokens) != 1 and len(tokens) != 5:
        raise template.TemplateSyntaxError(
            '`sitemetrics` tag requires four or no arguments. E.g.:'
            '{% sitemetrics by yandex for "138500" %} or {% sitemetrics %}'
        )

    if len(tokens) == 5 and (tokens[1] != 'by' or tokens[3] != 'for'):
        raise template.TemplateSyntaxError(
            'Four arguments `sitemetrics` tag notation should look like '
            '{% sitemetrics by yandex for "138500" %}.'
        )

    try:
        # Notation Type 2
        return SitemetricsNode(tokens[2], tokens[4])
    except IndexError:
        # Notation Type 1
        return SitemetricsNode()


class SitemetricsNode(template.Node):
    """Renders specified site metrics counter from template."""

    def __init__(self, provider=None, keycode=None):
        self.provider = provider
        self.keycode = keycode
        self.template = template.loader.get_template(
            'sitemetrics/sitemetrics.tpl'
        )

    def get_keycodes(self, context):
        if self.provider and self.keycode:
            kcodes = [
                {'provider': self.provider, 'keycode': self.keycode.strip('"')}
            ]
        else:
            if settings.SITE_BY_REQUEST:
                request = context.get('request')
                current_site = Site.objects.get(domain=request.get_host())
            else:
                current_site = Site.objects.get_current()

            cached = cache.get('sitemetrics')

            if not cached or current_site.id not in cached['keycodes']:
                kcodes = current_site.keycode_set.filter(active=True).values()
                cache.set(
                    'sitemetrics',
                    {'keycodes': {current_site.id: kcodes}},
                    settings.CACHE_TIMEOUT
                )
            else:
                kcodes = cached['keycodes'][current_site.id]

        _kcodes = []
        providers = get_providers_by_alias()
        for kcode_data in kcodes:
            if kcode_data['provider'] in providers:
                p_cls = providers[kcode_data['provider']]
                kcode_data['tpl'] = p_cls.get_template_name()
                # Get counter parameters.
                kcode_data.update(p_cls.get_params())
                _kcodes.append(kcode_data)

        return _kcodes

    def render(self, context):
        return self.template.render(
            template.Context({'keycodes': self.get_keycodes(context)})
        )
