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
from os import chdir, listdir, rename#, symlink

class Ddcmd(MakefilePackage):
    """DDCMD."""

    homepage = "https://lc.llnl.gov/bitbucket/projects/DDCMDY"
    git      = "ssh://git@cz-bitbucket.llnl.gov:7999/ddcmdy/ddcmd.git"

    version('develop', branch='develop', submodules=True)
    version('hycop', branch='hycop-tomaso', submodules=True)

    depends_on('mpi')

    build_directory = 'src'
    def install(self, spec, prefix):

        # go back to the build directory
        chdir('src')
        mkdir(prefix.bin)
        make('install', 'INSTALL_DIR={}'.format(prefix.bin))

        # the above will create the executable named as ddcMD-[arch]
        # for simplicity, we will move to 'ddcmd' or 'ddcmd-hycop'
        target_name = 'ddcMD-hycop' if spec.satisfies('@hycop') else 'ddcMD'

        chdir(prefix.bin)
        files = listdir('.')
        if len(files) == 1:
            rename(files[0], target_name)
            #symlink(files[0], target_name)
