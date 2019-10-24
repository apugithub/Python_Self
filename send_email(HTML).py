import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = '9176833080apu@gmail.com'
to_addr = ["9176833080apu@gmail.com", "ghosh.santanu30@gmail.com"]  #the recipients in sendmail(sender, recipients, message) needs to be a list:
text = "Hello this is test mail from Python in PLAIN format"

username = from_addr
password = '9176833080'

msg = MIMEMultipart()   # Through multipart tou can separate

msg['From'] = from_addr
msg['To'] = "9176833080apu@gmail.com, ghosh.santanu30@gmail.com"   #msg['To'] needs to be a string
msg['Subject'] = 'Test Mail_HTML'

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

#'Attach' can be done multiple times. And the format is   msg.attach(MIMEText(<variable_name>, '<format>'))
msg.attach(MIMEText(html, 'html'))
msg.attach(MIMEText(text, 'plain'))


server = smtplib.SMTP('smtp.gmail.com:587')   #This can be written as server = SMTP (...)   if you import SMTP already
server.ehlo()
server.starttls()
try:
    server.login(username,password)
    server.sendmail(from_addr,to_addr,msg.as_string())    #Here to_addr has to be a list.
    print ("Email sent successfully")
except smtplib.SMTPAuthenticationError:
    print("Couldn't login due to Authentication error")
except :
    print("an error occured")
server.quit()

