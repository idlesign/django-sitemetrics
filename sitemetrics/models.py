from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Keycode(models.Model):
    KEYCODE_PROVIDERS = (
        ('yandex', 'Yandex Metrika'),
        ('google', 'Google Analytics'),
    )
    site = models.ForeignKey(Site, verbose_name=_('Site'), help_text=_('Site for which metrics keycode is registered.'))
    provider = models.CharField(_('Provider'), max_length=50, choices=KEYCODE_PROVIDERS, help_text=_('Metrics service provider name.'))
    keycode = models.CharField(_('Keycode'), max_length=80, help_text=_('Keycode or identifier given by metrics service provider for site(s).'))
    active = models.BooleanField(_('Active'), default=True, help_text=_('Whether this keycode is available to use.'))

    class Meta:
        verbose_name = _('Keycode')
        verbose_name_plural = _('Keycodes')

    def __unicode__(self):
        return u'Keycode by %s for %s' % (self.provider, self.keycode)
