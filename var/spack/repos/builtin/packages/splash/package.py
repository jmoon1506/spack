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
#     spack install splash
#
# You can edit this file again by typing:
#
#     spack edit splash
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Splash(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://code.ornl.gov/v33/pilot2-splash-app"
    git      = "git@code.ornl.gov:v33/pilot2-splash-app.git"

    # use this for the actual code!
    version('develop', branch='develop')
    #version('1.0.1', tag='v1.0.1')
    #version('2014-10-08', commit='9d38cd4e2c94c3cea97d0e2924814acc')
    #version('1.0', 'f43fb8126c138db96b489655914ed2bd5a469412')

    build_directory = 'pysplash'

    variant('dbr',      default=True,  description='Support databroker')
    variant('flux',     default=False, description='Support flux')
    #variant('moose',    default=False, description='Support MOOSE')
    #variant('ddcmd',    default=False, description='Support ddcmd')
    #variant('analysis', default=True,  description='Support analysis and plotting')
    variant('mltrain',  default=False, description='Support ML training with GPU')

    '''
    # can we use other things as resources?
    resource(
        name='cargo',
        git='https://github.com/rust-lang/cargo.git',
        tag='0.10.0',
        destination='cargo'
    )
    '''

    extends('python@2.7:')

    # build dependencies
    depends_on('cmake@3.12.1',  type='build')
    depends_on('swig@3.0.12',   type='build')
    depends_on('py-setuptools', type='build')

    # generic
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))

    # mdanalysis
    depends_on('py-mdanalysis@0.16.2',  type=('build', 'run'))

    # maestrowf
    depends_on('py-maestrowf',          type=('build', 'run'))

    # databroker
    depends_on('databroker +python', when='+dbr', type='run')

    # machine learning dependencies
    depends_on('faiss +python',                  type=('build', 'run'))
    depends_on('py-theano',     when='~mltrain', type=('build', 'run'))
    depends_on('py-theano+gpu', when='+mltrain', type=('build', 'run'))
    depends_on('py-keras',                       type=('build', 'run'))
    depends_on('py-h5py+mpi',                    type=('build', 'run'))
    #depends_on('py-configparser', when='+mltrain', type=('build', 'run'))

    # flux
    depends_on('lua@5.1.5',           when='+flux', type=('build', 'run'))
    depends_on('lua-luaposix@33.4.0', when='+flux', type=('build', 'run'))
