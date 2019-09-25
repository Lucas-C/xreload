"""Doctests for module reloading.

>>> from xreload import xreload
>>> from test_xreload import make_mod
>>> make_mod()
>>> import x
>>> C = x.C
>>> Cfoo = C.foo
>>> Cbar = C.bar
>>> Cstomp = C.stomp
>>> b = C()
>>> bfoo = b.foo
>>> b.foo()
42
>>> bfoo()
42
>>> Cfoo(b)
42
>>> Cbar()
42 42
>>> Cstomp()
42 42 42
>>> make_mod(repl="42", subst="24")
>>> xreload(x) and 'OK'
'OK'
>>> b.foo()
24
>>> bfoo()
24
>>> Cfoo(b)
24
>>> C.bar()
24 24
>>> C.stomp()
24 24 24
>>> # Limitation: variables referencing class methods
>>> Cbar()
42 42
"""

import os
import sys
import shutil
import doctest
from xreload import xreload
import tempfile

SAMPLE_CODE = """
class C:
    def foo(self):
        print(42)
    @classmethod
    def bar(cls):
        print(42, 42)
    @staticmethod
    def stomp():
        print (42, 42, 42)
"""

TEMPDIR = None
SAVE_PATH = None


def setUp(unused=None):
    global TEMPDIR, SAVE_PATH
    TEMPDIR = tempfile.mkdtemp()
    SAVE_PATH = list(sys.path)
    sys.path.append(TEMPDIR)


def tearDown(unused=None):
    global TEMPDIR, SAVE_PATH
    if SAVE_PATH is not None:
        sys.path = SAVE_PATH
        SAVE_PATH = None
    if TEMPDIR is not None:
        shutil.rmtree(TEMPDIR)
        TEMPDIR = None
        

def make_mod(name="x", repl=None, subst=None):
    if not TEMPDIR:
        setUp()
        assert TEMPDIR
    fn = os.path.join(TEMPDIR, name + ".py")
    sample = SAMPLE_CODE
    if repl is not None and subst is not None:
        sample = sample.replace(repl, subst)
    with open(fn, "w") as f:
        f.write(sample)
