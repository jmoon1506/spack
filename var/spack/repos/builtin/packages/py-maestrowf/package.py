# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMaestrowf(PythonPackage):
    """A general purpose workflow conductor for running multi-step
       simulation studies."""

    homepage = "https://github.com/LLNL/maestrowf/"
    git      = "https://github.com/LLNL/maestrowf.git"

    version('1.1.4dev1.1', tag='1.1.4dev1.1')
    version('flux-dev', branch='bugfix/flux_broker')
    version('develop', branch='develop')
    version('1.1.4', tag='v1.1.4') 
    version('1.1.2', tag='v1.1.2')
    version('flux-sched', branch='bugfix/flux_broker')

    extends('python@3.7.3')

    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml',     type=('build', 'run'))
    depends_on('py-six',        type=('build', 'run'))
    depends_on('py-enum34',     type=('build', 'run'))
    depends_on('py-tabulate',   type=('build', 'run'), when='@1.1.0:')
    depends_on('py-filelock',   type=('build', 'run'), when='@1.1.0:')
