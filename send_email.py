import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = '9176833080apu@gmail.com'
to_addr = '9176833080apu@gmail.com'
text = "Hello this is test mail from Python"

username = from_addr
password = '9176833080'

msg = MIMEMultipart()   # Through multipart you can separate

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test Mail'
msg.attach(MIMEText(text))


server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()

