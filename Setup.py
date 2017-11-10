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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
