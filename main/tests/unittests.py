import unittest
import hardware_monitoring as monitor

print(monitor.used_disk_percent())

class HardwareUnittests(unittest.TestCase):

    def test_ram_prct(self):
        self.assertLess(monitor.get_ram_usage_prct(), 100.0)

    def test_cpu_prct(self):
        self.assertLess(monitor.used_cpu_percent(), 100.0)

    def test_cpu_temp(self):
        self.assertLess(monitor.tem_cpu(), 150.0)


if __name__ == '__main__':
    unittest.main()
