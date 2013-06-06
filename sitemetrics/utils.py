from .providers import METRICS_PROVIDERS


def get_provider_choices():
    """Returns a list of currently available metrics providers
    suitable for use as model fields choices.

    """
    choices = []
    for provider in METRICS_PROVIDERS:
        choices.append((provider.alias, provider.title))
    return choices


def get_providers_by_alias():
    """Returns a dictionary with currently available metrics providers
    classes indexed by their aliases.

    """
    providers = {}
    for provider in METRICS_PROVIDERS:
        providers[provider.alias] = provider
    return providers
