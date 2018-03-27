import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver="smtp.126.com"
username="yu_ch@126.com"
password="abcd****"

receiver="48407273@qq.com"
sender="yu_ch@126.com"

subject="Test  Mail from Python"


msg=MIMEText("Text")
msg['Subject']=Header(subject,'utf-8')
msg['From']=sender
msg['To']=receiver

print msg.as_string()
smtp=smtplib.SMTP(smtpserver)

smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())

smtp.quit()
