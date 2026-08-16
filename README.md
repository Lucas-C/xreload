[![pypi\_version\_img](https://img.shields.io/pypi/v/xreload.svg?style=flat)](https://pypi.python.org/pypi/xreload) [![Supported Python versions](https://img.shields.io/pypi/pyversions/xreload.svg)](https://pypi.python.org/pypi/xreload) [![build status](https://github.com/Lucas-C/xreload/workflows/build/badge.svg)](https://github.com/Lucas-C/xreload/actions?query=branch%3Amaster)

# xreload
This is Pypi-packaged version of Guido van Rossum original `xreload.py` script:
<http://svn.python.org/projects/sandbox/trunk/xreload/>

It also re-use some changes to this code made on the `plone.reload` package:
<https://github.com/plone/plone.reload/blob/master/plone/reload/xreload.py>

## License
Portions of this code are derived from `plone.reload`, Copyright (C) 2008-2017 Hanno Schlichting.
Licensed under the BSD 3-Clause License.
The `xreload` functionality included in this project is based on the original `xreload.py` script written by Guido van Rossum: http://svn.python.org/projects/sandbox/trunk/xreload/

## Usage
```python
from xreload import xreload
xreload(sys.modules[__name__], new_annotations={'RELOADING': True})
```

## Development
### Releasing a new version
With a valid `~/.pypirc`:

1. edit version in `setup.py`
2. `python setup.py sdist`
3. `twine upload dist/*`
4. `git tag $version && git push && git push --tags`
