# -*- encoding: utf-8 -*-
import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='xreload',
    version='1.0.1',
    description='Provide modules hot-reloading',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Guido Van Rossum',
    url='https://github.com/Lucas-C/xreload',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(i))[0] for i in glob.glob('src/*.py')],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ]
)
