#!/usr/bin/env python

# import statements
try:
    # First try to load most advanced setuptools setup.
    from setuptools import setup
except:
    # Fall back if setuptools is not installed.
    from distutils.core import setup

# Do setup
classif = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GPLv3 License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.4',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]

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
