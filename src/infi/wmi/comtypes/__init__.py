__import__("pkg_resources").declare_namespace(__name__)

import sys
from os.path import dirname, abspath

COMTYPES_MODULE = abspath(dirname(__file__))

def _add_this_to_sys_path():
    sys.path.append(COMTYPES_MODULE)

def _remove_other_comtypes():
    for comtypes in filter(lambda path: 'comtypes' in path, sys.path):
        comtypes.remove(comtypes)

if COMTYPES_MODULE not in sys.path:
    _remove_other_comtypes()
    _add_this_to_sys_path()

