#!/usr/bin/env python3
'''Hardware Data Part'''
import psutil
from platform import platform
import re
import urllib.request

from psutil import cpu_times_percent


#Basics
def tem_cpu():
    '''Return CPU temp'''
    import platform
    if platform.system=='Windows':
        import wmi
        current_temp = wmi.WMI(namespace="root\\wmi") #Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯ kann an dem Laptop liegen oder generelles Problem 
        cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15
        return round(cpu_temp, 2)
        # Überarbeiten: https://psutil.readthedocs.io/en/latest/index.html?highlight=sensors_temperatures#sensors

def used_cpu_percent():
    '''Return CPU usage in percet'''
    return psutil.cpu_percent(5)

def used_disk_percent():
    '''Return disk-space usage in percet'''
    return psutil.virtual_memory().percent

def free_disk_gb():
    '''Returns free space on disk'''
    disk_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    fehler = 0
    for i in disk_name:
        try:
            print(i + ":/ hat " + str(round(((((psutil.disk_usage(i + ':/').free) /1024 ) /1024 ) /1024 ),2)),'GB frei')
        except OSError as err:
            # print(i +':/ ist nicht angeschlossen')
            fehler = fehler + 1
    # Überarbeiten: Wofür alle Partitionen? oder alternativ String mit allen partitionen hintereinander

def user():
    '''Retuns registered user/s'''
    user_list=psutil.users()
    user_str="".join(map(str,user_list))
    #username = re.search('=(.+?),', user_str).group(1)
    return user_list #name[1:-1]

def connection(url='http://google.com'):
    '''Ping'''
    try:
        urllib.request.urlopen(url)
        return True
    except ValueError:
        return False


if __name__=='__main__':
    print(str(tem_cpu()) + ' # ' + str(used_cpu_percent()) + ' # ' + str(used_disk_percent()) + ' # ' + str(free_disk_gb()) + ' # ' + str(user()) + ' # ' + str(connection()))

#Ergebnisse der Tests werden ausgegeben

# print(cpu_kurz,'°C warm')
# print('Die CPU Auslastung beträgt: {}%'.format(get_cpu_usage()))
# print('{} MB RAM werden genutzt'.format(int(get_ram_usage() / 1024 / 1024)))
# print('{}% RAM werden genutzt'.format(get_ram_usage_prct()))
# print('Eine Internetverbindung ist vorhanden' if connect() else 'Kein Internet!')
















#Unittests
# class TestBeispieleTestCase(unittest.TestCase):

#     def test_rundung(self):
#         self.assertAlmostEqual(cpu_temp, cpu_kurz, 2)


# if __name__ == '__main__':
#     unittest.main(verbosity=0)