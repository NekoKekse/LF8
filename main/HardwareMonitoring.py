import wmi
import psutil
import unittest
import re
import urllib.request

current_temp = wmi.WMI(namespace="root\\wmi")#Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯
cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15
cpu_kurz=round(cpu_temp, 2)

user_list=psutil.users()
user_str="".join(map(str,user_list))
username = re.search('=(.+?),', user_str).group(1)

disk_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
fehler = 0

def get_cpu_usage():
    return psutil.cpu_percent(5)

for i in disk_name:
    try:
        print(i + ":/ benutzt " + str(psutil.disk_usage(i + ':/')).partition('percent=')[2][0:-1] + "% Festplattenspeicher")
    except OSError as err:
        #print(i +':/ ist nicht angeschlossen')
        fehler = fehler + 1

def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

def get_ram_usage_prct():
    return psutil.virtual_memory().percent

def connect(google='http://google.com'):
    try:
        urllib.request.urlopen(google)
        return True
    except:
        return False


print(username[1:-1],'ist eingeloggt')
print(cpu_kurz,'°C warm')
print('Die CPU Auslastung beträgt: {}%'.format(get_cpu_usage()))
print('{} MB RAM werden genutzt'.format(int(get_ram_usage() / 1024 / 1024)))
print('{}% RAM werden genutzt'.format(get_ram_usage_prct()))
print('Eine Internetverbindung ist vorhanden' if connect() else 'Kein Internet!')


class TestBeispieleTestCase(unittest.TestCase):

    def test_rundung(self):
        self.assertAlmostEqual(cpu_temp, cpu_kurz, 2)


if __name__ == '__main__':
    unittest.main(verbosity=0)
