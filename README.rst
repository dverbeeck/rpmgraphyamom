.. -*- mode: rst -*-

=================
rpmgraph
=================

----------------------------------------------------------
Display RPM Package Dependency Graph from RPM-database
----------------------------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Copyright: 2013 by Hartmut Goebel
:Licence:   GNU Public Licence v3 (GPLv3), but not for military use


This utility is slightly different from the one coming with RPM:

* it is working on installed packages not on package-files,
* it is building a tree of all dependencies of the packages named on
  the command line.


Usage
~~~~~~~~~~~~~

::

  rpmgraph.py [-h] [--depth DEPTH] pkgname [pkgname ...]

positional arguments
----------------------

  pkgname

optional arguments
--------------------

  -h, --help     show this help message and exit
  --depth DEPTH  walk the tree that deep, default: 5


Requirements
~~~~~~~~~~~~

* Python 2.7
* rpm
