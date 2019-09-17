# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Memsurfer(PythonPackage):
    """MemSurfer is a tool to compute and analyze membrane surfaces found in a
       wide variety of large-scale molecular simulations."""

    homepage = "https://github.com/LLNL/MemSurfer"
    git      = "git@github.com:LLNL/MemSurfer.git"

    version('1.0', tag='v1.0', submodules=True)
    version('master', branch='master', submodules=True)
    version('develop', branch='develop', submodules=True)

    variant('osmesa', default=False, description='Enable OSMesa support (for VTK)')

    extends('python@3.7:')

    depends_on('cmake@3.14:')
    depends_on('swig@3.0.12')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-pip')

    depends_on('eigen@3.3.7')
    depends_on('cgal@4.13 +shared~core~demos~imageio')

    # vtk needs to know whether to build with mesa or opengl
    depends_on('vtk@8.1.2 ~ffmpeg~mpi+opengl2~qt~xdmf +python3 ~osmesa', when='~osmesa')
    depends_on('vtk@8.1.2 ~ffmpeg~mpi+opengl2~qt~xdmf +python3 +osmesa', when='+osmesa')

    # this is needed only to resolve the conflict between
    # the default and netcdf's spec
    depends_on('hdf5 +hl')

    # memsurfer's setup needs path to these deps to build extension modules
    def setup_environment(self, spack_env, run_env):
        spack_env.set('VTK_ROOT', self.spec['vtk'].prefix)
        spack_env.set('CGAL_ROOT', self.spec['cgal'].prefix)
        spack_env.set('BOOST_ROOT', self.spec['boost'].prefix)
        spack_env.set('EIGEN_ROOT', self.spec['eigen'].prefix)
