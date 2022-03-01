#!/usr/bin/env python3
'''Init file for program'''
import sys
from time import sleep
from datetime import datetime
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

    config.server.starttls()
    config.server.login(config.user, config.pwd)
    config.server.sendmail(config.MAIL_FROM, config.RCPT_TO, data)
    config.server.quit()

class ValueTest:
    '''Test values above max.'''
    def __init__(self, tem_cpu, used_cpu_percent, used_disk_percent, connection):
        self.__tem_cpu=tem_cpu
        self.__used_cpu_percent=used_cpu_percent
        self.__used_disk_percent=used_disk_percent
        self.__connection=connection

    def test_tem_cpu(self, max_tmp):
        '''Return TRUE if CPU over max_tmp'''
        return bool(self.__tem_cpu < max_tmp)

    def test_used_cpu_percent(self, max_used):
        '''Return TRUE if CPU percent over max_used'''
        return bool(self.__used_cpu_percent < max_used)

    def test_used_disk_percent(self, max_used):
        '''Return TRUE if Disk percent over max_used'''
        return bool(self.__used_disk_percent < max_used)

    def test_connection(self):
        '''Return TRUE if Network is NOT reachable'''
        return np.invert(self.__connection)

def main_service():
    '''Get data from HardwareMonitoring.py, check if they are higher than the max values in
    main_config.py (responsible class: ValueTest) and send an e-mail if this is the case.
    Then save the data in the database (responsible function: DB.add) and start again (loop)'''
    while True:
        # Read Data
        #data = [config.filename, current_time(), current_date(), monitor.tem_cpu(), monitor.used_cpu_percent(), monitor.used_disk_percent(), monitor.free_disk_gb(), monitor.user(), monitor.connection()]

        # Create Object
        data_log = [ValueTest(data[3], data[4], data[5], data[8])]

        #### Test Objekt #########################################
        data = 'main.db', current_time, current_date, 50, 54, 650, 1, 'test', True
        data_log = ValueTest(50, 54, 650, True)#
        ##########################################################

        #Test if all tests are False
        tests=[ValueTest.test_tem_cpu(data_log, config.tem_cpu_max), ValueTest.test_used_cpu_percent(data_log, config.used_cpu_percent), ValueTest.test_used_disk_percent(data_log, config.used_disk_percent), ValueTest.test_connection(data_log)]

        if not all(tests) is True:
            print('Value(s) above max!!!')
            #email(data)
            sleep(5)
        else:
            print('All values ok!')

        # Save Data in DB
        db.add(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

        # Delete Object
        del data_log

        sleep(1)



if __name__ == '__main__':
    if len(sys.argv)==1:
        main_service()
    elif sys.argv[1] == '-L':
        raise NotImplementedError
    else:
        raise NotImplementedError
        