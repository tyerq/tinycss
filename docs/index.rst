.. include:: ../README.rst


Requirements
------------

tinycss is tested on CPython 2.6, 2.7, 3.1 and 3.2 as well as PyPy 1.8;
it should work on any implementation of **Python 2.6 or later version
(including 3.x)** of the language.

Cython_ is used for optional accelerators but is only required for
development versions on tinycss.

.. _Cython: http://cython.org/


Installation
------------

Installing with `pip <http://www.pip-installer.org/>`_ should Just Work:

.. code-block:: sh

    pip install tinycss

The release tarballs contain pre-*cythoned* C files for the accelerators:
you will not need Cython to install like this.
If the accelerators fail to build for some reason, tinycss will
print a warning and fall back to a pure-Python installation.


Documentation
-------------

.. Have this page in the sidebar, but do not show a link to itself here:

.. toctree::
    :hidden:

    self

.. toctree::
    :maxdepth: 2

    parsing
    css3
    extending
    hacking
    changelog
