from infi import unittest, wmi

class WmiTestCase(unittest.TestCase):
    def test_query_cimv(self):
        client = wmi.WmiClient()
        query = client.execute_query("SELECT * FROM Win32_ComputerSystemProduct")
        results = [item for item in query]
        self.assertEqual(len(results), 1)

    def test_query_wmi(self):
        client = wmi.WmiClient(r"root\wmi")
        query = client.execute_query("SELECT * FROM MS_SystemInformation")
        results = [item for item in query]
        self.assertEqual(len(results), 1)

