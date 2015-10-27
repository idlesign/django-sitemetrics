import os
import io
from setuptools import setup

from sitemetrics import VERSION


def read(*parts):
    with io.open(os.path.join(os.path.dirname(__file__), *parts)) as f:
        return f.read()


setup(
    name='django-sitemetrics',
    version='.'.join(map(str, VERSION)),
    url='http://github.com/idlesign/django-sitemetrics',

    description='Reusable application for Django providing easy means to integrate site metrics counters into your sites',
    long_description=read('README.rst'),
    license='BSD 3-Clause License',

    author='Igor `idle sign` Starikov',
    author_email='idlesign@yandex.ru',

    packages=['sitemetrics'],
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
