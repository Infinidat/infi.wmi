__import__("pkg_resources").declare_namespace(__name__)

import sys

PY2 = sys.version_info[0] == 2

if PY2:
    range = xrange

class WmiObject(object):
    def __init__(self, com_object):
        self._properties = None
        self._values = dict()
        self._object = com_object

    def _get_properties(self):
        return self._object.Properties_

    @property
    def properties(self):
        if self._properties is None:
            self._properties = self._get_properties()
        return self._properties

    def _get_property(self, attr):
        return self.properties.Item(attr)

    def _get_cached_value(self, attr):
        if attr not in self._values:
            self._values[attr] = self._get_property(attr).Value
        return self._values[attr]

    def get_wmi_attribute(self, attr):
        return self._get_cached_value(attr)

    def get_path(self):
        return self._object.Path_.Path

def get_comtypes_client(namespace=r"root\cimv2"):
    from comtypes import CoGetObject
    from comtypes.client import GetModule
    wmi_module = GetModule(['{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2])
    client = CoGetObject(r"winmgmts:{}".format(namespace), interface=wmi_module.ISWbemServicesEx)
    return client

class WmiClient(object):
    def __init__(self, namespace=r"root\cimv2"):
        super(WmiClient, self).__init__()
        self._namespace = namespace
        self._reload_client()

    def _reload_client(self):
        from comtypes import CoInitializeEx
        # CoInitialize is per-thread, but comtypes only calls it once on module load. We don't know if it was called
        # for the current thread so we call it again to make sure:
        CoInitializeEx()
        self._client = get_comtypes_client(self._namespace)

    @classmethod
    def _get_item_by_index(cls, results, index):
        return results.ItemIndex(index)

    def execute_query(self, query):
        from _ctypes import COMError
        results = self._client.ExecQuery(query)
        count = 0
        try:
            count = results.Count
        except COMError:
            pass
        for index in range(count):
            yield self._get_item_by_index(results, index)
