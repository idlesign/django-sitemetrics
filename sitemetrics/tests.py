"""This file contains tests for sitemetrics."""
from django.utils import unittest

from sitemetrics.providers import MetricsProvider, METRICS_PROVIDERS
from sitemetrics.utils import get_provider_choices, get_providers_by_alias


class UtilsTest(unittest.TestCase):

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
