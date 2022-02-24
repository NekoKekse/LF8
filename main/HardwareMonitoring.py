import wmi
import psutil
import unittest
import re
import urllib.request

#Temperatur Check
current_temp = wmi.WMI(namespace="root\\wmi")#Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯
cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15
cpu_kurz=round(cpu_temp, 2)

#User wird von Liste in String umgewandelt (kann evtl gekürzt werden) und der Interessante Teil wird rausgefiltert
user_list=psutil.users() 
user_str="".join(map(str,user_list))
username = re.search('=(.+?),', user_str).group(1)

#Festplattenspeicher wird als String gespeichert
disk_prct = str(get_disk_usage())

#Object "get_cpu_usage" wird erstellt
def get_cpu_usage():
    return psutil.cpu_percent(5)

 #Object "get_disk_usage" wird erstellt
def get_disk_usage():
    return psutil.disk_usage('C:/')

#Object "get_ram_usage" wird erstellt
def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

#Object "get_ram_usage_prct" wird erstellt
def get_ram_usage_prct():
    return psutil.virtual_memory().percent

#Object "connect" wird erstellt und es wird getestet ob "http://google.com" erreichbar ist
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

#Die Ergebnisse aller Checks werden ausgegeben
print(username[1:-1],'ist eingeloggt')
print(cpu_kurz,'°C warm')
print('Die CPU Auslastung beträgt: {}%'.format(get_cpu_usage()))
print(disk_prct.partition('percent=')[2][0:-1],"% Festplattenspeicher sind belegt")
print('{} MB RAM werden genutzt'.format(int(get_ram_usage() / 1024 / 1024)))
print('{}% RAM werden genutzt'.format(get_ram_usage_prct()))
print('Eine Internetverbindung ist vorhanden' if connect() else 'Kein Internet!')


#Unittests (folgen noch)
class TestBeispieleTestCase(unittest.TestCase):

    def test_rundung(self):
        self.assertAlmostEqual(cpu_temp, cpu_kurz, 2)


if __name__ == '__main__':
    unittest.main(verbosity=0)
