# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPyrsistent(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/tobgu/pyrsistent"
    url      = "https://github.com/tobgu/pyrsistent/archive/v0.16.0.tar.gz"

    version('0.16.0', sha256='4bd7cca9756458c91b3124e9c67aecd0aea0f2a13d077a54d08b30dc0c658fc2')


    depends_on('py-six')
    depends_on('py-setuptools')
    depends_on('py-pytest')    
    depends_on('py-tox')
    depends_on('py-sphinx')
    depends_on('py-sphinx-rtd-theme@0.1.5')
    depends_on('py-memory-profiler')
    depends_on('py-psutil@2.1.1')
    #depends_on('py-pyperform')
    depends_on('py-hypothesis')

