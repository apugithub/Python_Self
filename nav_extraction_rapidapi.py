# This api is taken from rapid api and the app link is as below, here I have modified the code as per my need --
# # https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav/

# While adding new fund add the same in 'scheme_code' and 'querystring' as well
import requests
import pandas as pd
import time
import json
from tqdm import tqdm

# This is to extract the rapid api key
f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)


fund_name = []
nav = []
nav_date = []

final_dict = {'Fund_Name': fund_name, 'NAV': nav, 'NAV_Date': nav_date}

url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV"

scheme_code = ['120389', '120503', '119125', '119242', '118551', '118506', '118560', '118473', '111569', '119746',
               '120166', '129220', '118701', '118803', '119598', '119609', '119019', '122639', '119063', '119807',
               '121279']

# Supports multiple comma separated Scheme Code
querystring = {"SchemeCode": '120389, 120503, 119125, 119242, 118551, 118506, 118560, 118473, 111569, 119746, 120166, '
                             '129220, 118701, 118803, 119598, 119609, 119019, 122639, 119063, 119807,121279'}

headers = {
    'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com",
    'x-rapidapi-key': keys['RAPID_API']
    }

response = requests.request("GET", url, headers=headers, params=querystring)
r = response.json()
# a = json.dumps(r, indent=4, sort_keys=False)
# print(a)


# Below for loop is to arrange the JSON as per the order of scheme_code
for i in scheme_code:  # Iterating for every scheme code
    for k in r:
        if k['Scheme Code'] == i:
            fund_name.append(k['Scheme Name'])
            nav.append(float(k['Net Asset Value']))  # Converting net asset value to float
            nav_date.append(k['Date'])

df = pd.DataFrame(final_dict)
print(df)

df.to_excel('D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/Fund_with_NAV.xlsx', index=False, header=True)
