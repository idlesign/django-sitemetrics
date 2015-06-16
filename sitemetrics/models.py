from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from .utils import get_provider_choices


@python_2_unicode_compatible
class Keycode(models.Model):

    site = models.ForeignKey(Site, verbose_name=_('Site'), help_text=_('Site for which metrics keycode is registered.'))

    provider = models.CharField(
        _('Provider'), max_length=50, choices=get_provider_choices(),
        help_text=_('Metrics service provider name.'))

    keycode = models.CharField(
        _('Keycode'), max_length=80,
        help_text=_('Keycode or identifier given by metrics service provider for site(s).'))

    active = models.BooleanField(_('Active'), default=True, help_text=_('Whether this keycode is available to use.'))

    class Meta(object):
        verbose_name = _('Keycode')
        verbose_name_plural = _('Keycodes')

    def __str__(self):
        return u'Keycode by %s: %s' % (self.provider, self.keycode)
