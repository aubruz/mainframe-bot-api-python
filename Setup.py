# _*_ coding: utf-8 _*_
from distutils.core import setup
from setuptools import find_packages

setup(
    name="mainframe-bot-api",
    version="1.0.0",
    author="aubruz",
    packages=find_packages(),
    url="https://github.com/aubruz/mainframe-api-python",
    license="MIT License",
    description="Communicate easily with Mainframe API",
    long_description='Mainframe API includes a Client to make calls easily, '
                     'responses objects and a complete set of UI components to '
                     'build forms, dialogs and messages.',
    zip_false=False,
    keywords='mainframe bot api',
)
