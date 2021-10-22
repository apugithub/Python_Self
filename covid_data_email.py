import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import datetime

############################### Below part is to fetch timestamp and timezone ###########################
a = datetime.datetime.now()
curr_time = a.strftime("%d-%m-%Y, %I:%M:%S %p")    # This is being used in Email subject
time_zone = a.astimezone().tzname()

print('Initiating...\nDate & Time Captured')
##########################################################################################################

##### Below two lines is to get the response and extract the jason of the same
r = requests.get('https://api.covid19india.org/data.json')
i = r.json()

print("Webserver response received")

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


html = """
<html>
<head>
</head>
<body>
<p>&nbsp;</p>
<p><img src="https://images.financialexpress.com/2020/04/corona-graphics-660.jpg" alt="covid" width="255" height="170" /></p>
<p>&nbsp;</p>
<p>Hello,</p>
<p>Please find below the stat on Covid cases in <strong><em>India</em> &amp; <em>West Bengal</em></strong></p>
<p>&nbsp;</p>
<h3><em><strong><span style="text-decoration: underline;"><span style="background-color: #ffff00; color: #000000; text-decoration: underline;">India Cases</span></span> : as on {last_update}</strong></em></h3>
<table style="height: 187px; border-color: #000000; float: left;" border="#000000" width="549">
<tbody>
<tr style="height: 42px;">
<td style="width: 130.4px; height: 42px; text-align: center;">
<h3 style="text-align: center;"><span style="color: #ff0000;"><strong>Confirmed&nbsp;</strong></span></h3>
</td>
<td style="width: 130.4px; height: 42px;">
<h3 style="text-align: center;"><strong>&nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">Active</span></strong></h3>
</td>
<td style="width: 131.2px; height: 42px;">
<h3 style="text-align: center;"><span style="color: #00ff00;"><strong>Recovered</strong></span></h3>
</td>
<td style="width: 131.2px; height: 42px; text-align: center;">
<h3><span style="color: #808080;"><strong>Deceased</strong></span></h3>
</td>
</tr>
<tr style="height: 31px;">
<td style="width: 130.4px; height: 31px; text-align: center;"><span style="color: #ff00ff;"><strong>[+{confirmed_delta}]</strong></span></td>
<td style="width: 130.4px; height: 31px;">&nbsp;</td>
<td style="width: 131.2px; height: 31px; text-align: center;"><span style="color: #00ff00;"><strong>[+{recovered_delta}]</strong></span></td>
<td style="width: 131.2px; height: 31px; text-align: center;"><span style="color: #808080;"><strong>[+{deceased_delta}]</strong></span></td>
</tr>
<tr style="height: 49.35px;">
<td style="width: 130.4px; height: 49.35px;">
<h2 style="text-align: center;"><span style="color: #ff0000;">{confirmed}</span></h2>
</td>
<td style="width: 130.4px; height: 49.35px; text-align: center;">
<h2><span style="color: #0000ff;">{active}</span></h2>
</td>
<td style="width: 131.2px; height: 49.35px; text-align: center;">
<h2 style="text-align: center;"><span style="color: #00ff00;"><strong>{recovered}</strong></span></h2>
</td>
<td style="width: 131.2px; height: 49.35px;">
<h2 style="text-align: center;"><span style="color: #808080;">{deceased}</span></h2>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3><em><strong><span style="text-decoration: underline;"><span style="background-color: #ffff00;">West Bengal</span></span> Total Cases : as on {wb_lastupdatedtime}</strong></em></h3>
<ul>
<li>
<h3><em><strong><span style="color: #ff0000;">Confirmed</span>:&nbsp; {wb_confirmed}</strong></em></h3>
</li>
<li>
<h3><em><strong><span style="color: #0000ff;">Active</span>:&nbsp; &nbsp;{wb_active}</strong></em></h3>
</li>
<li>
<h3><em><strong><span style="color: #00ff00;">Recovered</span>:&nbsp; {wb_recovered}</strong></em></h3>
</li>
<li>
<h3><em><strong><span style="color: #808080;">Deceased</span>:&nbsp; &nbsp;{wb_deaths}</strong></em></h3>
</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><em>N.B: Data collected from&nbsp;<a href="https://www.covid19india.org/">https://www.covid19india.org</a></em></p>
<p>&nbsp;</p>
<h3>&nbsp;</h3>
<p>&nbsp;</p>
</body></html>
"""

html_1 = html.format(confirmed=confirmed, last_update=last_update, confirmed_delta=confirmed_delta,active=active,
                     recovered=recovered,recovered_delta=recovered_delta,deceased=deceased,deceased_delta=deceased_delta,
                     wb_confirmed=wb_confirmed,wb_active=wb_active, wb_recovered=wb_recovered, wb_deaths=wb_deaths,
                     wb_lastupdatedtime=wb_lastupdatedtime)

print("Message content Ready :)")
################################## The below part is for sending email #############################################

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
msg['Subject'] = 'Covid Stat | '+ curr_time + ' (' + time_zone + ')'


print("Sending Email...")


# If there is a failure use the troubleshoting steps at https://support.google.com/mail/answer/7126229?visit_id=637561422949586344-3167309703&rd=2#cantsignin

server = smtplib.SMTP('smtp.gmail.com:587')   #This can be written as server = SMTP (...)   if you import SMTP already
server.ehlo()
server.starttls()
try:
    server.login(username,password)
    server.sendmail(from_addr,to_addr,msg.as_string())    #Here to_addr has to be a list.
    print ("Covid Stat email sent successfully")
except smtplib.SMTPAuthenticationError:
    print("Couldn't login due to Authentication error")
except :
    print("an error occured")
server.quit()


# If it throws error like ('Couldn't login due to Authentication error')
#  then visit: https://accounts.google.com/DisplayUnlockCaptcha
