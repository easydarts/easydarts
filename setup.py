# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = "Steel darts calibration and score recognition system"

setup(
    name="easydarts",
    version="0.0.1",
    description="Steel darts calibration and score recognition system",
    long_description=long_description,
    license="MIT",
    author="Cidevant Von Goethe",
    author_email="cidevant@mail.ru",
    url="https://github.com/easydarts/easydarts",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'easydarts = easydarts.cli.cli:main',
        ]
    },
    install_requires=[
		'opencv-python',
        'numpy',
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ]
)
