#!/usr/bin/env python

import json

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('ebagis_ui/static/ebagis_ui/version.json', 'r') as v:
    version = json.load(v)['version']

with open('README.md', 'r') as r:
    readme = r.read()

download_url = (
    'https://github.com/PSU-CSAR/django-ebagis-ui/tarball/%s'
)


setup(
    name='django-ebagis-ui',
    packages=['ebagis_ui'],
    version=version,
    description=('Django app implementing the UI for the server-side portion of the BAGIS project.'),
    long_description=readme,
    author='Portland State University Center for Spatial Analysis and Research',
    author_email='jkeifer@pdx.edu',
    url='https://github.com/PSU-CSAR/django-ebagis-ui',
    download_url=download_url % version,
    install_requires=[
        'django-ebagis>=0.3.0',
    ],
    license='',
)