# -*- coding: utf-8 -*-
# Copyright (c) 2023, Enrico Development Team.
# Distributed under the LGPLv2.1+ License.
from codecs import open as openc
import pathlib
from setuptools import setup, find_namespace_packages


def get_requirements():
    """Read requirements.txt and return a list of requirements."""
    here = pathlib.Path(__file__).absolute().parent
    requirements = []
    filename = here.joinpath('requirements.txt')
    with openc(filename, encoding='utf-8') as fileh:
        for lines in fileh:
            package = lines.split('>=')[1].strip()
            requirements.append(lines.strip())
    return requirements


setup(
    name='dataproc',
    version='0.0.1.dev0',
    description='A Neutron data post processing package',
    author='Parisa Roshaninejad',
    author_email='parisa.roshaninejad@uis.no',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Python Programming Students',
        ('License :: MIT'),
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: MOD905',
    ],
    keywords='cuts and fits for Neutron data',
    packages=find_namespace_packages(),
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'dataproc = dataproc.bin.dataprocrun:entry_point',
        ]
    },
)
