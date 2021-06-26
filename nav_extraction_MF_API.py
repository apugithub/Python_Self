import requests
import pandas as pd

#Mutual Fund API = https://www.mfapi.in/

scheme_code = ['120389', '120503', '119125', '119242', '118551', '118506', '118560', '118473', '111569', '119746',
               '120166', '129220', '118701', '118803', '119598', '119609', '119019', '122639', '119063', '119807',
               '121279']

fund_name = []
nav = []
nav_date = []

final_dict = {'Fund_Name': fund_name, 'NAV': nav, 'NAV_Date': nav_date}

for items in scheme_code:
    r = requests.get('https://api.mfapi.in/mf/{}'.format(items))
    i = r.json()

    fund_name.append(i['meta']['scheme_name'])
    nav.append(float(i['data'][0]['nav']))
    nav_date.append(i['data'][0]['date'])

df = pd.DataFrame(final_dict)
print(df)

df.to_excel('D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/Fund_with_NAV.xlsx', index=False, header= True)
