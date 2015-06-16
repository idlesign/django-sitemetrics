"""This file contains tests for sitemetrics."""
from django.test import TestCase
from django.template.base import Template, TemplateSyntaxError
from django.template.context import Context
from django.test.utils import override_settings
from django.contrib.sites.models import Site

from sitemetrics.providers import MetricsProvider, get_custom_providers, Yandex
from sitemetrics.utils import get_provider_choices, get_providers_by_alias
from sitemetrics.models import Keycode


class CustomizedProvider(Yandex):

    params = {'some_param': 'some_value',}


def render_string(string, context=None):
    return Template(string).render(Context(context))


class UtilsTest(TestCase):

    def test_provider_choices(self):
        choices = get_provider_choices()
        self.assertTrue(len(choices) > 0)
        self.assertTrue(isinstance(choices[0], tuple))
        self.assertTrue(len(choices[0]), 2)

    def test_provider_by_alias(self):
        by_alias = get_providers_by_alias()
        self.assertTrue(len(by_alias) > 0)
        self.assertTrue(isinstance(by_alias, dict))
        for alias, p_cls in by_alias.items():
            self.assertTrue(issubclass(p_cls, MetricsProvider))

class ProvidersTest(TestCase):

    @override_settings(SITEMETRICS_PROVIDERS = ('sitemetrics.tests.CustomizedProvider',))
    def test_customized(self):
        providers = get_custom_providers()
        self.assertEqual(len(providers), 1)
        self.assertEqual(providers[0].get_params(), CustomizedProvider.params)

class TemplateTagsTest(TestCase):

    def test_simple(self):
        tpl = '{% load sitemetrics %}{% sitemetrics by yandex for "138500" %}'
        self.assertIn('138500', render_string(tpl))

        tpl = '{% load sitemetrics %}{% sitemetrics some %}'
        self.assertRaises(TemplateSyntaxError, render_string, tpl)

        tpl = '{% load sitemetrics %}{% sitemetrics a b c d  %}'
        self.assertRaises(TemplateSyntaxError, render_string, tpl)

    def test_sites_contrib(self):

        site_one = Site.objects.get(pk=1)
        site_two = Site(domain='some.com', name='some.com')
        site_two.save()

        site_two_code = Keycode(site=site_two, provider='google', keycode='222')
        site_two_code.save()

        self.assertIn('222', '%s' % site_two_code)

        tpl = '{% load sitemetrics %}{% sitemetrics %}'

        with override_settings(SITE_ID=1):
            self.assertEqual(render_string(tpl), '')  # Test none code for current site

            site_one_code = Keycode(site=site_one, provider='yandex', keycode='111', active=False)
            site_one_code.save()

            self.assertEqual(render_string(tpl), '')  # Test inactive

            site_one_code.active = True
            site_one_code.save()
            self.assertIn('111', render_string(tpl))  # Test active

            self.assertIn('111', render_string(tpl))  # Test cached hit

        with override_settings(SITE_ID=2):
            self.assertIn('222', render_string(tpl))
