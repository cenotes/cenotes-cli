CENotes library and CLI
=======================

.. image:: https://travis-ci.org/ioparaskev/cenotes-cli.svg?branch=master
    :target: https://travis-ci.org/ioparaskev/cenotes-cli

**C(ryptographical) E(xpendable) Notes**

**Libraries and Command Line Interface**

-  Free software: GNU General Public License v3

-  `Backend & Frontend Demo`_

-  Source code:

   -  `Backend`_
   -  `Frontend`_
   -  `CLI and Libraries`_

-  `Documentation`_

-  `Backend Design`_

What is this?
-------------

This is a **cli and library** project to support encryption/decryption
of expendable notes

An example of a backend that uses the libraries provided here can be
found at https://cenot.es

What this isn’t
---------------

UI/Frontend/Backend. This is a **cli/library** project. Frontend and
backend solutions are different projects. The reason for this is to
allow flexibility in frontend / backend choice and to avoid huge bundle
projects.

-  A **backend** project that uses these libraries can be found `here`_

-  A **frontend** project that communicates with the **backend** can be
   found `here <https://github.com/ioparaskev/cenotes-reaction>`__

Features
--------

-  Symmetric encryption of notes using the `pynacl`_ project

How does this work?
-------------------

See `design`_

How to run
----------

**You will need python >= 3.3**

1. Cloning the repo

  -  Clone the repo

     -  ``git clone https://github.com/ioparaskev/cenotes-cli.git``

  -  Install the requirements with pipenv

     -  ``pip install pipenv``
     -  ``pipenv install``

  -  Set your ``PYTHONPATH`` to include the project

     -  For linux:
        ``export PYTHONPATH=<path-to-the-cloned-repo>:$PYTHONPATH``

  -  See available options

     -  ``python cenotes_cli/cli.py --help``

2. Installing the python package

  -  Ideally inside a virtualenv

     -  ``pip install cenotes-cli``

  -  See available options

     -  ``cenotes-cli --help``

.. _Backend & Frontend Demo: https://cenot.es
.. _Backend: https://github.com/ioparaskev/cenotes
.. _Frontend: https://github.com/ioparaskev/cenotes-reaction
.. _CLI and Libraries: https://github.com/ioparaskev/cenotes-cli
.. _Documentation: https://cenotes.readthedocs.io
.. _Backend Design: https://cenotes.readthedocs.io/en/latest/design.html
.. _here: https://github.com/ioparaskev/cenotes
.. _pynacl: https://pynacl.readthedocs.io/en/latest/
.. _design: https://cenotes.readthedocs.io/en/latest/design.html

