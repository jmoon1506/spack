# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PySplashMdanalysis(PythonPackage):
    """MDAnalysis is a Python toolkit to analyze molecular dynamics
    trajectories generated by a wide range of popular simulation
    packages including DL_Poly, CHARMM, Amber, NAMD, LAMMPS, and
    Gromacs. (See the lists of supported trajectory formats and
    topology formats.)"""

    homepage = "https://lc.llnl.gov/bitbucket/projects/XZR/repos/mdanalysis_0_16_2"
    url      = "https://lc.llnl.gov/bitbucket/projects/XZR/repos/mdanalysis_0_16_2"

    version('2018-12-26', git='ssh://git@cz-bitbucket.llnl.gov:7999/xzr/mdanalysis_0_16_2.git', commit='b723a1c5da6')

    #version('2018-12-26', git='https://github.com/XiaohuaZhangLLNL/mdanalysis.git', commit='6cb4cd308b7108636688d24dd4dc29ff44e4f499')
    #version('0.16.2', '20ddd2838a5bbfc4b1016794f1382938')
    #version('0.15.0', '19e5a8e6c2bfe85f6209d1d7a36e4f20')

    variant('analysis', default=True, 
            description='Enable analysis packages: matplotlib, scipy, seaborn')
    variant('amber', default=False,
            description='Support AMBER netcdf format.')

    build_directory = 'package'

    depends_on('python@2.7:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cython@0.16:', type='build')
    depends_on('py-numpy@1.5.0:', type=('build', 'run'))
    depends_on('py-six@1.4.0:', type=('build', 'run'))
    depends_on('py-biopython@1.59:', type=('build', 'run'))
    depends_on('py-networkx@1.0:', type=('build', 'run'))
    depends_on('py-griddataformats@0.3.2:', type=('build', 'run'))

    depends_on('py-matplotlib', when='+analysis', type=('build', 'run'))
    depends_on('py-scipy', when='+analysis', type=('build', 'run'))
    depends_on('py-seaborn', when='+analysis', type=('build', 'run'))

    depends_on('py-netcdf4@1.0:', when='+amber', type=('build', 'run'))
    depends_on('hdf5', when='+amber', type=('run'))
