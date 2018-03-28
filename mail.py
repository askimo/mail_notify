import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver="smtp.126.com"
username="yu_ch@126.com"
password="abcd****"

receiver="48407273@qq.com"
sender="yu_ch@126.com"

#sendmal(title,content)

def sendmail(title="Test  Mail from Python",content="Hello Python SMTP Mail"):
    msg=MIMEText(content)
    msg['Subject']=Header(title,'utf-8')
    msg['From']=sender
    msg['To']=receiver
    smtp=smtplib.SMTP(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    sendmail()