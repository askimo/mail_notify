import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json


#sendmal(title,content)

def sendmail(title="Test  Mail from Python",content="Hello Python SMTP Mail"):
    #load config dict from file:config.json
    with open('config.json','r') as f:
        con_dict=json.loads(f.read())
    print(con_dict)
    server=con_dict['server']
    sender=con_dict['sender']
    password=con_dict['password']
    receivers=con_dict['receivers']
    print(receivers)
    msg=MIMEText(content)
    msg['Subject']=Header(title,'utf-8')
    msg['From']=sender
    msg['To']=','.join(receivers)
    smtp=smtplib.SMTP(server)
    smtp.login(sender,password)
    smtp.sendmail(sender,receivers,msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    sendmail()