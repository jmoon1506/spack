# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGsd(PythonPackage):
    """GSD (General Simulation Data) is a file format specification and a 
       library to read and write it. The package also contains a python 
       module that reads and writes hoomd schema gsd files with an easy 
       to use syntax."""

    homepage = "https://pypi.org/project/gsd/"
    url      = "https://files.pythonhosted.org/packages/db/cf/5f3f94726f2849151764f7e918c710eb912783334bf977c57d368f2a8c3d/gsd-1.7.0.tar.gz"

    version('1.7.0', sha256='778b4c11c5a94e617ed67d7a22f0ce994f786a00492f96e66dde43a67832f33a')

    extends('python@2.7:')    
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy@1.5.0:', type=('build', 'run'))
