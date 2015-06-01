#!/usr/bin/python
#http://elinux.org/RPi_Email_IP_On_Boot_Debian
import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import datetime
import sys
 
# Change to your own account information
# sys.argv[1] has the to, 
# sys.argv[2] has the gmail_user
# sys.argv[3] has your password
if (len(sys.argv) != 4):
  print "missing arguments for sending ip email"
  exit()
to = sys.argv[1]
gmail_user = sys.argv[2]
gmail_password = sys.argv[3]
print "sending email to " + to
 
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
 
today = datetime.date.today()
 
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
my_ip = 'BB: Your ip is %s' %  ipaddr
 
msg = MIMEText(my_ip)
msg['Subject'] = 'IP from BBB on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
 
smtpserver.sendmail(gmail_user, [to], msg.as_string())
 
smtpserver.quit()
