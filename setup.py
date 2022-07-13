# -*- coding: utf-8 -*-
import re

from setuptools import setup

from zhonghonghvac.version import __version__

setup(
    name='zhonghonghvac',
    version=__version__,
    description='Python library for interfacing with ZhongHong HVAC controller',
    long_description=
    'Python library for interfacing with ZhongHong HVAC controller',
    url='https://github.com/heculess/zhonghong_hvac',
    author='heculess lau',
    author_email='heculess@hotmail.com',
    license='Apache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='zhonghong hvac',
    packages=["zhonghonghvac"],
    python_requires='>=3.5',
    install_requires=[
        'attrs',
    ])
