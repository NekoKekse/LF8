# repo Import
import psutil
import unittest
import re
import urllib.request


# Temperatur Check
class monitor:

    def temp():
        # Temperatur Check
        #if platform.system == 'Windows':
            import wmi
            current_temp = wmi.WMI(
                namespace="root\\wmi")  # Die Temperatur funktioniert nicht wirklich es wird immer der selbe wert angezeigt...¯\_(ツ)_/¯ kann an dem Laptop liegen oder generelles Problem
            cpu_temp = (current_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0) - 273.15
            return round(cpu_temp, 2)

    def user():
        # User Check
        user_list = psutil.users()
        user_str = "".join(map(str, user_list))
        username = re.search('=(.+?),', user_str).group(1)
        return username[1:-1] + ' ist eingeloggt'

    def disk_prct():
        # Variablen für Speicherplatz Abfrage
        disk_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
        fehler = 0
        for i in disk_name:
            try:
                print(i + ":/ benutzt" , psutil.disk_usage(i + ':/').percent , "% Festplattenspeicher")
            except OSError as err:
                # print(i +':/ ist nicht angeschlossen')
                fehler = fehler + 1

    def disk_GB():
        disk_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
        fehler = 0
        for i in disk_name:
            try:
                print(i + ":/ hat " + str(round(((((psutil.disk_usage(i + ':/').total) /1024 ) /1024 ) /1024 ),2)),'GB')
            except OSError as err:
                # print(i +':/ ist nicht angeschlossen')
                fehler = fehler + 1

    def disk_GB_free():
        disk_name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
        fehler = 0
        for i in disk_name:
            try:
                print(i + ":/ hat " + str(round(((((psutil.disk_usage(i + ':/').free) /1024 ) /1024 ) /1024 ),2)),'GB frei')
            except OSError as err:
                # print(i +':/ ist nicht angeschlossen')
                fehler = fehler + 1

    def get_cpu_usage():
        # CPU Auslastung Abfrage
        return psutil.cpu_percent(5)

    def get_ram_usage():
        # RAM Auslastung Abfrage in MB
        return int(((psutil.virtual_memory().total - psutil.virtual_memory().available) /1024) /1024)

    def get_ram_usage_prct():
        # RAM Auslastung Abfrage in Prozent
        return psutil.virtual_memory().percent

    def get_ram_total():
        return int((((psutil.virtual_memory().total) /1024 ) /1024 ) /1024 )

    def connect(google='http://google.com'):
        # Netzwerk Test (ist Google erreichbar?)
        try:
            urllib.request.urlopen(google)
            return True
        except:
            return False


#print(psutil.users())


# monitor.temp
# monitor.user
# monitor.

# Ergebnisse der Tests werden ausgegeben

# print(cpu_kurz,'°C warm')
# print('Die CPU Auslastung beträgt: {}%'.format(get_cpu_usage()))
# print('{} MB RAM werden genutzt'.format(int(get_ram_usage() / 1024 / 1024)))
# print('{}% RAM werden genutzt'.format(get_ram_usage_prct()))
# print('Eine Internetverbindung ist vorhanden' if connect() else 'Kein Internet!')


# Unittests
class TestBeispieleTestCase(unittest.TestCase):

    def test_rundung(self):
        self.assertAlmostEqual(cpu_temp, cpu_kurz, 2)


if __name__ == '__main__':
    unittest.main(verbosity=0)
