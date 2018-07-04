from sitemetrics.providers import Yandex


class CustomizedProvider(Yandex):

    params = {'some_param': 'some_value'}
