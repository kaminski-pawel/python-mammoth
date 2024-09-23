#!/usr/bin/env python

import os
from setuptools import setup


setup(
    name='mammoth',
    version='1.6.0@1.0.1',
    description='Convert Word documents from docx to simple and clean HTML and Markdown',
    author='Michael Williamson, Pawel Kaminski',
    author_email='pawel.kaminski@uni.lu',
    url='https://github.com/kaminski-pawel/python-mammoth',
    packages=['mammoth', 'mammoth.docx', 'mammoth.html', 'mammoth.styles', 'mammoth.styles.parser', 'mammoth.writers'],
    entry_points={
        "console_scripts": [
            "mammoth=mammoth.cli:main"
        ]
    },
    keywords="docx word office clean html markdown md",
    install_requires=[
        "cobble>=0.1.3,<0.2",
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    license="BSD-2-Clause",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)

