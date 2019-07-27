# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMsgpack(PythonPackage):
    """MessagePack is an efficient binary serialization format."""

    homepage = "https://pypi.org/project/msgpack"
    url      = "https://files.pythonhosted.org/packages/81/9c/0036c66234482044070836cc622266839e2412f8108849ab0bfdeaab8578/msgpack-0.6.1.tar.gz"

    version('0.6.1', sha256='4008c72f5ef2b7936447dcb83db41d97e9791c83221be13d5e19db0796df1972')

    #depends_on('py-pbr@0.11:', type=('build', 'run'))
    #depends_on('py-six@1.7:',  type=('build', 'run'))
    #depends_on('py-six@1.9:',  type=('build', 'run'), when='@2.0.0:')
    # requirements.txt references @1:, but 0.4 is newest available..
    #depends_on('py-funcsigs',  type=('build', 'run'), when='^python@:3.2.99')
    depends_on('py-setuptools@17.1:', type='build')
