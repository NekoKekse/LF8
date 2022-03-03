#!/usr/bin/env python3
'''Init file for program'''
import sys
from time import sleep
from datetime import datetime
import smtplib
import numpy as np

import hardware_monitoring as monitor
import db
import main_config as config

def current_date():
    '''Return date(yyyy mm dd).'''
    date = datetime.now()
    return date.strftime("%Y-%m-%d")

def current_time():
    '''Return time(HH MM SS).'''
    date = datetime.now()
    return date.strftime("%H:%M:%S")

def email(log):
    '''Send E-mail to Admin'''
    mail_text = '### Monitoring ###,\n\n' + str(log) + '\n\n:)'
    data = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (config.MAIL_FROM, config.RCPT_TO, config.subject, mail_text)
    server = smtplib.SMTP(config.server)
    server.starttls()
    server.login(config.user, config.pwd)
    server.sendmail(config.MAIL_FROM, config.RCPT_TO, data)
    server.quit()

class ValueTest:
    '''Test values above max.'''
    def __init__(self, tem_cpu, used_cpu_percent, ram,  disk, connection):
        self.__tem_cpu=tem_cpu
        self.__used_cpu_percent=used_cpu_percent
        self.__used_ram_percent=ram
        self.__used_disk_percent=disk
        self.__connection=connection

    def test_tem_cpu(self, max_tmp):
        '''Return True if CPU over max_tmp'''
        if self.__tem_cpu is None:
            print('CPU Temp is not readable')
            return False
        return bool(self.__tem_cpu > max_tmp)

    def test_used_cpu_percent(self, max_used):
        '''Return True if CPU usage percent over max_used'''
        if self.__used_cpu_percent is None:
            print('Used diskspace is not readable')
            return False
        return bool(self.__used_cpu_percent > max_used)

    def test_used_ram_percent(self, max_used):
        '''Return True if RAM usage percent over max_used'''
        if self.__used_ram_percent is None:
            print('Used RAM space percent is not readable')
            return False
        return bool(self.__used_ram_percent > max_used)

    def test_used_disk_percent(self, max_used):
        '''Return True if Diskspace usage percent over max_used'''
        if self.__used_disk_percent is None:
            print('Used Disk space percent is not readable')
            return False
        for mountpoints, use_percent in dict(self.__used_disk_percent).items():
            test_result = bool(use_percent > max_used)
            if test_result is True:
                return True
        return False

    def test_connection(self):
        '''Return True if Network is NOT reachable'''
        if self.__connection is None:
            print('Test Conection is not posible')
            return False
        return np.invert(self.__connection)

def main_service():
    '''Get data from HardwareMonitoring.py, check if they are higher than the max values in
    main_config.py (responsible class: ValueTest) and send an e-mail if this is the case.
    Then save the data in the database (responsible function: DB.add) and start again (loop)'''
    while True:
        # Read Data
        data = [config.filename, current_date(), current_time(), monitor.tem_cpu(), monitor.used_cpu_percent(), monitor.ram(), monitor.disk(), monitor.user(), monitor.connection()]
        # Create Object
        data_log = ValueTest(data[3], data[4], data[5], data[6], data[8])

        #Test if all tests are False
        tests=[data_log.test_tem_cpu(config.tem_cpu_max), data_log.test_used_cpu_percent(config.used_cpu_percent), data_log.test_used_ram_percent(config.used_ram_percent), data_log.test_used_disk_percent(config.used_disk_percent), data_log.test_connection()]
        if any(tests) is True:
            if tests[0]==True:
                print('CPU over max_tmp!')
                #email('CPU over max_tmp! \n -'' + data)
                sleep(10)
            elif tests[1]==True:
                print('CPU usage percent over max_used!')
                #email('CPU usage percent over max_used! \n -'' + data)
            elif tests[2]==True:
                print('RAM usage percent over max_used')
                #email('RAM usage percent over max_used! \n -'' + data)
            elif tests[3]==True:
                print('Disk space usage percent is not readable!')
                #email('Disk space usage percent is not readable! \n -'' + data)
            elif tests[4]==True:
                print('Network is NOT reachable!')
                #email('Network is NOT reachable! \n -'' + data)
            else:
                NotImplementedError
            pritn(' \n -')
            sleep(5)
        else:
            print('All values ok! \n -')

        # Save Data in DB
        db.build(config.filename)
        db.add(config.filename, data[1], data[2], data[3], data[4], data[5], str(data[6]), data[7], data[8])

        # Delete Object
        del data_log

        sleep(1)

if __name__ == '__main__':
    if len(sys.argv)==1:
        main_service()
    elif sys.argv[1] == '-L' and len(sys.argv)==4:
        for logdata in db.select(config.filename, sys.argv[3]):
            datei = open(sys.argv[2],'a')
            datei.write( '\r\n' + 'Date: ' + str(logdata[0]) + ' | Time: ' + str(logdata[1]) + ' | Temp of CPU: ' + str(logdata[2]) + '°C | CPU Usage: ' + str(logdata[3]) + '% | RAM: ' + str(logdata[4]) + ' | Disk: ' + str(logdata[5]) + ' | User: ' + str(logdata[6]) + ' | Connection: ' + str(bool(logdata[7])))
    else:
        print('-L tssest.txt 2022-03-02')
        raise NotImplementedError
        