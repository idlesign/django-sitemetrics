import pytest

from django.contrib.sites.models import Site
from django.template.base import TemplateSyntaxError

from sitemetrics.models import Keycode
from sitemetrics.providers import MetricsProvider, get_custom_providers
from sitemetrics.utils import get_provider_choices, get_providers_by_alias
from sitemetrics import settings as sm_settings


class TestUtils:

    def test_provider_choices(self):
        choices = get_provider_choices()
        
        assert len(choices) > 0
        assert isinstance(choices[0], tuple)
        assert len(choices[0]) == 2

    def test_provider_by_alias(self):
        by_alias = get_providers_by_alias()

        assert len(by_alias) > 0
        assert isinstance(by_alias, dict)
        
        for alias, p_cls in by_alias.items():
            assert issubclass(p_cls, MetricsProvider)


class TestProviders:

    def test_customized(self):
        from .testapp.providers import CustomizedProvider

        providers = get_custom_providers()
        assert len(providers) == 2
        assert providers[0].get_params() == CustomizedProvider.params


class TestTemplateTagsDummy:

    def test_counter_removed(self, settings, template_render_tag):
        settings.DEBUG = True
        assert 'counter removed' in template_render_tag('sitemetrics', 'sitemetrics by yandex for "138500"')

    def test_on_debug(self, settings, template_render_tag):
        sm_settings.ON_DEBUG = True
        assert '138500' in template_render_tag('sitemetrics', 'sitemetrics by yandex for "138500"')


class TestTemplateTags:

    def test_simple(self, template_render_tag):
        assert '138500' in template_render_tag('sitemetrics', 'sitemetrics by yandex for "138500"')

        with pytest.raises(TemplateSyntaxError):
            template_render_tag('sitemetrics', 'sitemetrics some')

        with pytest.raises(TemplateSyntaxError):
            template_render_tag('sitemetrics', 'sitemetrics a b c d')

    def test_sites_contrib(self, settings, template_render_tag):

        def render():
            return template_render_tag('sitemetrics', 'sitemetrics')

        site_one = Site.objects.get(pk=1)
        site_two = Site(domain='some.com', name='some.com')
        site_two.save()

        site_two_code = Keycode(site=site_two, provider='google', keycode='222')
        site_two_code.save()

        assert '222' in '%s' % site_two_code

        tpl = '{% load sitemetrics %}{% sitemetrics %}'

        settings.SITE_ID = 1

        assert render() == ''  # Test none code for current site

        site_one_code = Keycode(site=site_one, provider='yandex', keycode='111', active=False)
        site_one_code.save()

        assert render() == ''  # Test inactive

        site_one_code.active = True
        site_one_code.save()

        assert '111' in render()  # Test active
        assert '111' in render()  # Test cached hit

        settings.SITE_ID = 2

        assert '222' in render()
