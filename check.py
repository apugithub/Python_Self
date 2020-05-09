import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import datetime
from bs4 import BeautifulSoup as bs
import pandas as pd

a = datetime.datetime.now()
curr_time = a.strftime("%d-%m-%Y, %I:%M:%S %p")    # This is being used in Email subject
time_zone = a.astimezone().tzname()

r = requests.get('https://api.covid19india.org/data.json')
i = r.json()

all_state = i['statewise'][0]  # We know all state info are at 0th index object, or else we have to take help of for loop
#like we have used below for 'West Bengal'

confirmed = all_state['confirmed']
confirmed_delta = all_state['deltaconfirmed']
active = all_state['active']
recovered = all_state['recovered']
recovered_delta = all_state['deltarecovered']
deceased = all_state['deaths']
deceased_delta = all_state['deltadeaths']
last_update = all_state['lastupdatedtime']


# Below loop with search info for west bengal only--

for s in i['statewise']:
    if s['statecode'] == 'WB':  # This object is for total case statistics
        wb_confirmed = s['confirmed']
        wb_active = s['active']
        wb_recovered = s['recovered']
        wb_deaths = s['deaths']
        wb_lastupdatedtime = s['lastupdatedtime']

print(confirmed, confirmed_delta, active, recovered, recovered_delta, '\n',
      'WB_Time: ' , wb_lastupdatedtime)

html = """
<html>
<head>
</head>
<body>
<p>Hello,</p>
<p>Please find below the stat on Covid cases in <em>India</em> &amp; <em>West Bengal</em></p>
<h3><span style="text-decoration: underline;"><strong>India Cases :</strong></span></h3>
<p><strong><span style="color: #ff00ff;">Confirmed</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #00ccff;">Active</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #00ff00;">Recovered</span>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #808080;">Deceased</span></strong></p>
<p><strong><span style="color: #808080;"><span style="color: #ff00ff;">[+{cnf_dlta}]&nbsp; &nbsp;</span> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #00ff00;">[+{rcv_dlta}]&nbsp;</span>&nbsp; &nbsp;[+{dd_dlta}]</span></strong></p>
<p><strong><span style="color: #808080;">{confirmed}</span></strong></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
</body></html>
"""

html_1 = html.format(confirmed=confirmed,cnf_dlta=confirmed_delta,rcv_dlta=recovered_delta,dd_dlta=deceased_delta)

from_addr = '9176833080apu@gmail.com'
to_addr = ["9176833080apu@gmail.com", "ghosh.santanu30@gmail.com"]  #the recipients in sendmail(sender, recipients, message) needs to be a list:

username = from_addr
password = '9176833080'

msg = MIMEMultipart()
msg.attach(MIMEText(html_1,'html'))
#msg = MIMEMultipart("alternative", None, [MIMEText(html_1,'html')])  ## This line is same as above two lines.


# Through multipart you can separate into 'To', 'From' , 'Subject'
msg['From'] = from_addr
msg['To'] = "9176833080apu@gmail.com,ghosh.santanu30@gmail.com"   #msg['To'] needs to be a string, same as next line
#msg["To"] = ",".join(to_addr)  # As #msg['To'] needs to be a string, that's why this line,
# and here no need to append this with double quotes, coz this (",".join(to_addr)) is returning string only
msg['Subject'] = 'My Test | '+ curr_time + '(' + time_zone + ')'


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
