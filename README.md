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

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

    and then run in the project directory:

        projector devenv build
