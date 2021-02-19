import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from tabulate import tabulate
import datetime

import requests
from bs4 import BeautifulSoup as bs  #is required to parse HT

a = datetime.datetime.now()
curr_time = a.strftime("%d-%m-%Y, %I:%M:%S %p")    # This is being used in Email subject
time_zone = a.astimezone().tzname()    #Displays local timezone name

from_addr = '9176833080apu@gmail.com'
to_addr = ["9176833080apu@gmail.com", "ghosh.santanu30@gmail.com"]  #the recipients in sendmail(sender, recipients, message) needs to be a list:

username = from_addr
password = '9176833080'

########################################## Data Frame Creation through web Scrapping ##########################
url_list = ['https://www.moneycontrol.com/mutual-funds/nav/axis-liquid-fund-direct-plan/MAA190',
            'https://www.moneycontrol.com/mutual-funds/nav/axis-long-term-equity-fund-direct-plan/MAA192',
            'https://www.moneycontrol.com/mutual-funds/nav/dsp-liquidity-fund-direct-plan/MDS613',
            'https://www.moneycontrol.com/mutual-funds/nav/dsp-tax-saver-fund-direct-plan/MDS572',
            'https://www.moneycontrol.com/mutual-funds/nav/franklin-india-feeder-franklin-u-s-opportunities-fund-direct-plan/MTE305',
            'https://www.moneycontrol.com/mutual-funds/nav/franklin-india-savings-fund-direct-growth/MTE365',
            'https://www.moneycontrol.com/mutual-funds/nav/franklin-india-ultra-short-bond-fund-super-institutional-direct-growth/MTE379',
            'https://www.moneycontrol.com/mutual-funds/nav/idfc-tax-advantage-elss-fund-direct-plan/MAG741',
            'https://www.moneycontrol.com/mutual-funds/nav/idfc-tax-advantage-elss-fund-regular-plan/MAG303',
            'https://www.moneycontrol.com/mutual-funds/nav/kotak-money-market-scheme-direct-plan/MKM556',
            'https://www.moneycontrol.com/mutual-funds/nav/kotak-standard-multicap-fund-direct-plan/MKM520',
            'https://www.moneycontrol.com/mutual-funds/nav/l-t-emerging-businesses-fund-direct-plan/MCC492',
            'https://www.moneycontrol.com/mutual-funds/nav/nippon-india-liquid-fund-direct-plan-growth/MRC978',
            'https://www.moneycontrol.com/mutual-funds/nav/nippon-india-tax-saver-fund-direct-plan-growth/MRC938'
            'https://www.moneycontrol.com/mutual-funds/nav/sbi-blue-chip-fund-direct-plan-growth/MSB532',
            'https://www.moneycontrol.com/mutual-funds/nav/sbi-equity-hybrid-fund-direct-plan-growth/MSB516',
            'https://www.moneycontrol.com/mutual-funds/nav/dsp-equity-bond-fund-direct-plan-growth/MDS608'
            ]

fund_name = [] # Array to store all fund names, separated by coma
fund_nav = [] # Array to store all fund NAVs, separated by coma
nav_date = [] # Array to store all NAV dates, separated by coma

for i in url_list:
    url = requests.get(i)

    soup = bs(url.content,'html.parser')

    name = soup.find('h1', attrs={'class': 'page_heading'}) # we can get from h1 directly as with h1 and the same class
    # there are no other values, other than the fund name

    b = soup.find('div', attrs={'class':'leftblok'}) #Going into mail HTML block
    nav = b.find('span', attrs={'class':'amt'})   # inside block b, appropriate class is chosen
    date = b.find('div', attrs= {'class':'grayvalue'})

    nav_float = float(nav.text[1:]) # As first letter  of the extracted NAV is rupee sign, hence discarding the first letter,
    #then converting the same to a floating number, to avoid casting issue at excel

    fund_name.append(name.text) # we are appending only the text part of extracted field 'name'
    fund_nav.append(nav_float)  # just appending nav_float value
    nav_date.append(date.text) # we are appending only the text part of extracted field 'date'


df = pd.DataFrame({'Fund Name':fund_name, 'Fund NAV':fund_nav, 'NAV Date': nav_date})
col_list = list(df.columns.values)
data = df

################################################################################################################

html = """
<html>
<head>
<style> 
 table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
  th, td {{ padding: 5px; }}
</style>
</head>
<body><p>Hello, </p>
<p><b>This data is from</b> <i style="color:DodgerBlue;">MoneyControl.com</i></p> <br></br>
{table}
<p>Regards,</p>
<p>Me</p>
</body></html>
"""

html_1 = html.format(table = tabulate(data, headers=col_list, tablefmt="html"))

msg = MIMEMultipart()
msg.attach(MIMEText(html_1,'html'))
#msg = MIMEMultipart("alternative", None, [MIMEText(html_1,'html')])  ## This line is same as above two lines.


# Through multipart you can separate into 'To', 'From' , 'Subject'
msg['From'] = from_addr
msg['To'] = "9176833080apu@gmail.com,ghosh.santanu30@gmail.com"   #msg['To'] needs to be a string, same as next line
#msg["To"] = ",".join(to_addr)  # As #msg['To'] needs to be a string, that's why this line,
# and here no need to append this with double quotes, coz this (",".join(to_addr)) is returning string only
msg['Subject'] = 'My Funds NAV Update | '+ curr_time + '(' + time_zone + ')'


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



# ** If you are unable to send due to SMTP error tyr the below two links from your browser
# https://www.google.com/settings/security/lesssecureapps    # this is to enable less secure apps to connect
# https://accounts.google.com/DisplayUnlockCaptcha    # this is to avoid 'location unknown' error