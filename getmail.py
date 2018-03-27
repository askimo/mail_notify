import poplib
email="yu_ch@126.com"
password="abcd****"
server="pop.126.com"

s=poplib.POP3(server)
print(s.getwelcome())
s.user(email)
s.pass_(password)
print('Messages: %s. Size: %s' % s.stat())
resp, mails, octets = s.list()
print(mails)