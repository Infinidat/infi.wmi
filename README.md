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

Run the following:

    easy_install -U infi.projector
    projector devenv build

Python 3
========

Python 3 support is experimental at this stage.
