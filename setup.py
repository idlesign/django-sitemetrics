import os
from setuptools import setup, find_packages
from sitemetrics import VERSION

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-sitemetrics',
    version=".".join(map(str, VERSION)),
    description='This reusable Django app can help you to site metrics (Yandex Metrika, Google Analytics)',
    long_description=readme,
    author="Igor 'idle sign' Starikov",
    author_email='idlesign@yandex.ru',
    url='http://github.com/idlesign/django-sitemetrics',
    packages=find_packages(),
    classifiers=[
	'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',

    ],
)
