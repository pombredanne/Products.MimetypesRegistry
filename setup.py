# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '2.1.0.dev0'

setup(
    name='Products.MimetypesRegistry',
    version=version,
    description="MIME type handling for Zope",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read(),
    classifiers=[
        "Framework :: Zope2",
        "Operating System :: OS Independent",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Zope mimetype registry',
    author='Benjamin Saller',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/Products.MimetypesRegistry',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'AccessControl>=3.0.0'
        'Acquisition',
        'Products.CMFCore',
        'setuptools',
        'ZODB3',
        'zope.contenttype',
        'zope.deferredimport',
        'zope.interface',
        'Zope2',
    ],
    extras_require=dict(
        test=[
            'plone.app.testing',
        ]
    ),
)
