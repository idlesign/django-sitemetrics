import os
from setuptools import setup
from sitemetrics import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-sitemetrics',
    version='.'.join(map(str, VERSION)),
    description='Reusable application for Django providing easy means to integrate site metrics counters into your sites',
    long_description=readme,
    author="Igor 'idle sign' Starikov",
    author_email='idlesign@yandex.ru',
    url='http://github.com/idlesign/django-sitemetrics',
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
    ],
)
