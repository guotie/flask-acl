"""
flask.ext.acl
=============

This extension provides an Access Control implementation for `tipfy <http://www.tipfy.org/>`_.

Links
-----
* `Documentation <http://www.tipfy.org/wiki/extensions/acl/>`_
* `Source Code Repository <http://code.google.com/p/tipfy-ext-acl/>`_
* `Issue Tracker <http://code.google.com/p/tipfy-ext-acl/issues/list>`_

About tipfy
-----------
* `Home page <http://www.tipfy.org/>`_
* `Extension list <http://www.tipfy.org/wiki/extensions/>`_
* `Discussion Group <http://groups.google.com/group/tipfy>`_
"""
from setuptools import setup

setup(
    name = 'flask.ext.acl',
    version = '0.6',
    license = 'BSD',
    url = 'https://github.com/guotie/flask-acl',
    description = 'Access Control extension for flask',
    long_description = __doc__,
    author = 'guotie',
    author_email = 'guotie.9@gmail.com',
    zip_safe = False,
    platforms = 'any',
    packages = [
        'flask',
        'flask.ext',
    ],
    namespace_packages = [
        'flask',
        'flask.ext',
    ],
    include_package_data = True,
    install_requires = [
        'flask',
        'flask.ext.sqlalchemy',
        'flask.ext.cache',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
