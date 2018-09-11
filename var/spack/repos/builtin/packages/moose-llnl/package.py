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

from spack import *
from os import system, getcwd, chdir, listdir

class MooseLlnl(MakefilePackage):
    """MOOSE customizations for LLNL's pilot2 project."""

    homepage = "http://www.example.com"
    git      = "ssh://git@cz-bitbucket.llnl.gov:7999/~tomaso/moose-llnl.git"

    version('master', branch='llnl-master', submodules=True)

    depends_on('mpi')
    depends_on('ddcmd@hycop', type='run')
    depends_on('petsc@3.6.4 +mumps', type=('build', 'run'))

    def build(self, spec, prefix):

        print 'doing custom build'
        print '\t prefix =', prefix
        #print '\t spec   =', spec
        print '\t cwd =', getcwd()
        print '\t ls =', listdir('.')

        system('JOBS=20 ./scripts/update_and_rebuild_libmesh.sh')

        subdirs = ['moose-hycop-req-res', 'framework', 'modules/phase_field']
        for subdir in subdirs:
            chdir(subdir)
            make()
            chdir('..')


    def install(self, spec, prefix):

        print 'doing custom install'
        print '\t prefix =', prefix
        #print '\t spec   =', spec
        print '\t cwd =', getcwd()
        print '\t ls =', listdir('.')

        mkdir(prefix.bin)
        mkdir(prefix.lib)

        # libraries and binaries to be installed
        install_bins = ['modules/phase_field/phase_field-opt',
                        #'libmesh/installed/bin/*'
                       ]

        install_libs = [#'libmesh/installed/lib/lib*.la',
                        'libmesh/installed/lib/lib*.so*',
                        'modules/tensor_mechanics/lib*.so*',
                        'modules/phase_field/lib/lib*.so*',
                        #'framework/libmoose*.la',
                        'framework/libmoose*.so*',
                        'framework/contrib/pcre/libpcre-opt*.so*'
                       ]

        for lib in install_libs:
            system('cp -P {} {}'.format(lib, prefix.lib))

        for bin in install_bins:
            system('cp {} {}'.format(bin, prefix.bin))
