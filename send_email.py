import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = '9176833080apu@gmail.com'
to_addr = ["9176833080apu@gmail.com", "ghosh.santanu30@gmail.com"]  #the recipients in sendmail(sender, recipients, message) needs to be a list:
text = "Hello this is test mail from Python"

username = from_addr
password = '9176833080'

msg = MIMEMultipart()   # Through multipart you can separate

msg['From'] = from_addr
msg['To'] = "9176833080apu@gmail.com,ghosh.santanu30@gmail.com"   #msg['To'] needs to be a string, same as next line
#msg["To"] = ",".join(to_addr)  # As #msg['To'] needs to be a string, that's why this line,
                                # and here no need to append this with double quotes,
                                # coz this (",".join(to_addr)) is returning string only
msg['Subject'] = 'Test Mail_Test'
msg.attach(MIMEText(text))

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

