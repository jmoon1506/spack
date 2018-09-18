##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install faiss
#
# You can edit this file again by typing:
#
#     spack edit faiss
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
from os import chdir, system

class Faiss(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    git      = "git@github.com:facebookresearch/faiss.git"

    version('master', branch='master')
    variant('python', default=True, description='Build Python bindings')

    depends_on('blas')
    depends_on('py-pip',   when='+python', type='build')
    depends_on('py-numpy', when='+python',  type=('build', 'run'))

    def build(self, spec, prefix):

        #TODO: filtering is needed only for non-x86 architecture!
        makefile = FileFilter('makefile.inc')
        makefile.filter('CPUFLAGS     = -msse4 -mpopcnt',  '#CPUFLAGS     = -msse4 -mpopcnt')

        make()

        if '+python' in self.spec:
            make('py')

    def install(self, spec, prefix):

        make('install')

        if '+python' in self.spec:
            chdir('python')
            system('pip install .')

