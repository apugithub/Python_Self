import smtplib
fromaddr = '9176833080apu@gmail.com'
toaddrs = '9176833080apu@gmail.com'
msg = 'Place Message here'

#provide gmail user name and password
username = '9176833080apu@gmail.com'
password = '9176833080'

# functions to send an email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()