import sys
import ctypes
from os.path import basename

from dladdr import dladdr

if sys.platform in ('darwin', 'ios',):
    libcname = 'libSystem.B.dylib'
    libname = 'libiconv.2.dylib'
else:
    libcname = 'libc.so.6'
    libname = 'libstdc++.so.6'

def test_dladdr():
    libstdcxx = ctypes.CDLL(libname)
    fp = libstdcxx.printf  # dlsym("printf") succeeds, but it should be from libc, not libstdc++.
    dlinfo = dladdr(fp)
    assert basename(dlinfo.dli_fname).decode('utf-8') == libcname
