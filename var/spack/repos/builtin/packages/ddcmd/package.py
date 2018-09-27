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
from os import chdir, listdir, getcwd, rename
from shutil import copy
from glob import glob

class Ddcmd(MakefilePackage):
    """DDCMD."""

    homepage = "https://lc.llnl.gov/bitbucket/projects/DDCMDY"
    git      = "ssh://git@cz-bitbucket.llnl.gov:7999/ddcmdy/ddcmd.git"

    #version('temp', commit='4c9c4cfc740', submodules=True)
    version('develop', branch='develop', submodules=True)
    version('hycop', branch='hycop-tomaso', submodules=True)
    version('gbell', tag='Gorden-Bell', submodules=True)
    version('jun8', tag='jun-8', submodules=True)

    depends_on('mpi')

    # older versions depend upon v1.0.0
    depends_on('ddcmdconverter@1.0.0', when='@jun8')

    build_directory = 'src'
    
    def install(self, spec, prefix):

        print 'doing custom install'
        print '\t prefix =', prefix
        print '\t cwd =', getcwd()
        print '\t ls =', listdir('.')

        mkdir(prefix.bin)

        # the install target was added on Sep 07
        # so, gbell and jun8 versions do not have that
        if spec.satisfies('@gbell') or spec.satisfies('@jun8'):
            print '-> doing explicit copy for older versions without install target'
           
            chdir('bin')
            files = listdir('.')
            print 'found', len(files), 'file(s) in', getcwd()
            print files
            
            for f in files:
                print 'copying', f
                copy(f, prefix.bin)

        else:
            # go back to the build directory
            chdir('src')
            make('install', 'INSTALL_DIR={}'.format(prefix.bin))

        # the above will create the executable named as ddcMD-[arch]
        # for simplicity, we will move to 'ddcmd' or 'ddcmd-hycop'
        target_name = 'ddcmd-hycop' if spec.satisfies('@hycop') else 'ddcmd'

        chdir(prefix.bin)
        files = listdir('.')
        if len(files) == 1:
            print '-> renaming {} to {}'.format(files[0], target_name)
            rename(files[0], target_name)

        else:
            print '-> found', len(files), 'file(s) in', getcwd()
            print '  ', files
            print '-> cannot rename files. exiting'
            exit(1)
