"""Doctests for module reloading.

>>> from xreload import xreload
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
>>> # Testing new_annotations usage:
>>> make_mod(CODE_FOR_MAIN_MODULE)
>>> xreload(x) and 'OK'
'OK'
>>> import x
>>> x.__annotations__
{}
>>> x.reload_with_new_annots()
>>> x.__annotations__
{'XRELOADED': True}
"""

import os
import shutil
import sys
import tempfile

CODE_FOR_MODULE_WITH_CLASS_C = """
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

CODE_FOR_MAIN_MODULE = """
import sys
from xreload import xreload

def reload_with_new_annots():
    xreload(sys.modules[__name__], new_annotations={"XRELOADED": True})
"""

TEMPDIR = tempfile.mkdtemp()
SAVE_PATH = list(sys.path)
sys.path.append(TEMPDIR)


def tearDown(unused=None):
    sys.path = SAVE_PATH
    shutil.rmtree(TEMPDIR)


def make_mod(sample=CODE_FOR_MODULE_WITH_CLASS_C, repl=None, subst=None):
    fn = os.path.join(TEMPDIR, "x.py")
    if repl is not None and subst is not None:
        sample = sample.replace(repl, subst)
    with open(fn, "w", encoding="utf-8") as f:
        f.write(sample)
