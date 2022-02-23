import wmi
import psutil
import unittest
import re

current_temp = wmi.WMI(namespace="root\\wmi")            #Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯
cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15

cpu_kurz=round(cpu_temp, 2)

def get_cpu_usage():
    return psutil.cpu_percent(5)

user_list=psutil.users()

user_str="".join(map(str,user_list))

username = re.search('=(.+?),', user_str).group(1)
print(username)



#print(user_str)
print(cpu_kurz)
#print(psutil.sensors_battery())
#print(user_list)
print('Die CPU Auslastung beträgt: {}%'.format(get_cpu_usage()))





class TestBeispieleTestCase(unittest.TestCase):

    def test_rundung(self):
        self.assertAlmostEqual(cpu_temp, cpu_kurz, 2)










if __name__ == '__main__':
    unittest.main(verbosity=2)
