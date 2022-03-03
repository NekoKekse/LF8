#!/usr/bin/env python3
'''Hardware Data Part'''
import platform
import urllib.request
import psutil

def tem_cpu():
    '''Return CPU temp'''
    if platform.system()=='Windows':
        from wmi import WMI
        current_temp = WMI(namespace="root\\wmi") #Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯ kann an dem Laptop liegen oder generelles Problem
        cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)-273.15
        return round(cpu_temp, 2)
    elif platform.system()=='Linux':
        return None
    else:
        return None

def used_cpu_percent():
    '''Return CPU usage in percet'''
    if platform.system()=='Windows' or 'Linux':
        return psutil.cpu_percent(5)
    else:
        return None

def ram():
    '''Return RAM usage'''
    if platform.system()=='Windows' or 'Linux':
        return psutil.virtual_memory().percent
    else:
        return None

def disk():
    '''Return all '''
    if platform.system()=='Windows' or 'Linux':
        all_disk_data = {}
        for all_data in psutil.disk_partitions():
            used_percentage = psutil.disk_usage(all_data.mountpoint).percent
            all_disk_data.update({all_data.mountpoint:used_percentage})
        return all_disk_data
    else:
        return None

def user():
    '''Retuns registered user/s'''
    if platform.system()=='Windows' or 'Linux':
        try:
            return psutil.users()[0].name
        except:
            pass
        return None
    else:
        return None

def connection(url='http://google.com'):
    '''Ping'''
    if platform.system()=='Windows' or 'Linux':
        try:
            urllib.request.urlopen(url)
            return True
        except:
            pass
        return False
    else:
        return None

if __name__=='__main__':
    print(str(tem_cpu()) + ' # ' + str(used_cpu_percent()) + ' # ' + str(ram()) + ' # ' + str(disk()) + ' # ' + str(user()) + ' # ' + str(connection()))


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
