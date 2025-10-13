import sys
import ctypes
from os.path import basename

from dladdr import dladdr
from dladdr import libcname  # only for testing

if sys.platform in ('darwin', 'ios',):
    libname = 'libiconv.2.dylib'
else:
    libname = 'libstdc++.so.6'

def test_dladdr():
    libstdcxx = ctypes.CDLL(libname)
    fp = libstdcxx.printf  # dlsym("printf") succeeds, but it should be from libc, not libstdc++.
    dlinfo = dladdr(fp)
    assert basename(dlinfo.dli_fname).decode('utf-8') == libcname
