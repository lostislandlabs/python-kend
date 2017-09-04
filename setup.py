import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    content = 'not found'
    try:
        with open(fname) as file:
            content = file.read()
    except:
        print(u'Warning: failed to open file {0}'.format(fname))
        pass
    return content

requires = [
    'lxml',
]

setup(
    name='kend',
    version='0.7.1',
    description='Client package for interacting with the Utopia kend server',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
    ],
    author='David Thorne',
    author_email='davethorne@gmail.com',
    long_description=read('README.md'),
    license=read('LICENSE.md'),
    packages=find_packages(),
    install_requires=requires,
    tests_require=requires,
    test_suite='kend',
)

