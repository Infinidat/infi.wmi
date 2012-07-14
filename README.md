Overview
========

A WMI Client in Python on top of a WMI-optimized version of comtypes.

This module uses a private version of comtypes for improving performance.

Usage
-----

Here's an example on how to use this module:

```python
from infi.wmi import WmiClient
client = WmiClient
results = client.execute_query("SELECT * FROM MPIO_GET_DESCRIPTOR")
```

Checking out the code
=====================

This project uses buildout, and git to generate setup.py and __version__.py.
In order to generate these, run:

    python -S bootstrap.py -d -t
    bin/buildout -c buildout-version.cfg
    python setup.py develop

In our development environment, we use isolated python builds, by running the following instead of the last command:

    bin/buildout install development-scripts

