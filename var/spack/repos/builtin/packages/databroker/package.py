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
from os import system, chdir 

class Databroker(CMakePackage):
    """IBM's databroker."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/IBM/data-broker"
    git      = "git@github.com:IBM/data-broker.git"

    version('0.5.1', version='0.5.1')
    version('master', branch='master')
    variant('python', default=False, description='Build Python bindings')

    depends_on('cmake',          type='build')
    depends_on('redis@5.0.2:',   type=('build', 'run'))
    #depends_on('redis@4.0.8:',   type=('build', 'run'))
    depends_on('ruby@2.2.9:',     type=('build', 'run'))
    depends_on('libevent@2.1.8', type=('build', 'run'))

    extends('python@2.7:',        when='+python')
    depends_on('py-pip',          when='+python', type='build')
    depends_on('py-setuptools',   when='+python', type=('build', 'run'))
    depends_on('libffi@3.2.1',    when='+python', type=('build', 'run'))
    depends_on('py-cffi@1.11.5',  when='+python', type=('build', 'run'))
    depends_on('py-enum34@1.1.6', when='+python', type=('build', 'run'))

    parallel = False

    def cmake_args(self):
        args = []
        if '+python' in self.spec:
            args.append('-DPYDBR=true')
        return args

    def install(self, spec, prefix):

        '''
        print ' which ruby: ', 
        system('which ruby')
        print 'which gem : ',
        system('which gem')
        system('`which gem` env')
        system('`which gem` install -V redis')
        
        exit()
        '''
        system('pip install rdbtools python-lzf')

        chdir(self.build_directory)
        make('install')
