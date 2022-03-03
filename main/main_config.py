#!/usr/bin/env python3
'''Config for monitoring software'''
import smtplib

### Max Values ###
tem_cpu_max=90
used_cpu_percent=70
used_ram_percent=70
used_disk_percent=70

### DB filename ###
filename='main.db'


### Mail Config ###
user = 'test'
pwd = 'test123'
subject = 'Python-Mail :)'
MAIL_FROM = 'test@example.com'
RCPT_TO  = 'test@example.com'
server = 'secure.emailsrvr.com:587'