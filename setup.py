#!/usr/bin/env python

# import statements
try:
    # First try to load most advanced setuptools setup.
    from setuptools import setup
except:
    # Fall back if setuptools is not installed.
    from distutils.core import setup

# Do setup
setup(
    name='elemlib',
    version='0.0.1',
    description='Library for element operation',
    author='Fpemud',
    author_email='fpemud@sina.com',
    license='GPLv3 License',
    platforms='Linux',
    classifiers=classif,
    url='http://github.com/fpemud/elemlib',
    download_url='',
    py_modules=['elemlib'],
    package_dir=package_dir,
    )
