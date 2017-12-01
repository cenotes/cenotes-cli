#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pynacl>=1.2.0',
]

setup_requirements = [
]

test_requirements = [
    'pytest',
    'tox',
    'coverage'
]

setup(
    name='cenotes_cli',
    version='0.2.1',
    description="Cenotes command line application and libraries",
    long_description=readme + '\n\n' + history,
    author="John Paraskevopoulos",
    author_email='ioparaskev@gmail.com',
    url='https://github.com/ioparaskev/cenotes_cli',
    packages=[
        'cenotes_lib'
    ],
    package_dir={'cenotes_lib': 'cenotes_cli/cenotes_lib'},
    entry_points={
        'console_scripts': [
            'cenotes-cli=cenotes_cli.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='cenotes_cli',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
