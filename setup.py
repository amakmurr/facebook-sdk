#!/usr/bin/env python
from setuptools import setup

exec(open("facebook_sdk/version.py").read())

setup(
    name='facebook-sdk',
    version='3.0.2',
    description='This client library is designed to support the Facebook '
                'Graph API and the official Facebook JavaScript SDK, which '
                'is the canonical way to implement Facebook authentication.',
    author='Facebook',
    maintainer='Martey Dodoo',
    maintainer_email='martey+facebook-sdk@mobolic.com',
    url='https://github.com/mobolic/facebook-sdk',
    license='Apache',
    packages=["facebook_sdk"],
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'requests',
    ],
)
