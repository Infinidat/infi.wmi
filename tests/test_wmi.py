from infi import unittest, wmi

class WmiTestCase(unittest.TestCase):
    def test_query_cimv(self):
        client = wmi.WmiClient()
        self.assertEqual(len(client.execute_query("SELECT * FROM Win32_ComputerSystemProduct")), 1)

    def test_query_wmi(self):
        client = wmi.WmiClient(r"root\wmi")
        self.assertEqual(len(client.execute_query("SELECT * FROM MS_SystemInformation")), 1)

