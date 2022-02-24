import smtplib  

user = 'test'
pwd = 'test123'
mail_text = 'Hallo,\n\ndas ist ein Test!\n\n:)'
subject = 'Python-Mail :)'
 
MAIL_FROM = 'test@example.com'
RCPT_TO  = 'test@example.com'
DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (MAIL_FROM, RCPT_TO, subject, mail_text)

server = smtplib.SMTP('secure.emailsrvr.com:587')
server.starttls()
server.login(user, pwd)
server.sendmail(MAIL_FROM, RCPT_TO, DATA)
server.quit()
