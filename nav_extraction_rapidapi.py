# This api is taken from rapid api and the app link is as below, here I have modified the code as per my need --
# # https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav/

# While adding new fund add the same in 'scheme_code' (get from https://www.mfapi.in/) and 'querystring' as well
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
scheme_num = []

final_dict = {'Fund_Name': fund_name, 'NAV': nav, 'NAV_Date': nav_date, 'Scheme_Code': scheme_num}

url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV"

# Supports multiple comma separated Scheme Code
querystring = {"SchemeCode": '120389, 120503, 119125, 119242, 118551, 118506, 118560, 118473, 111569, 119746, 120166, '
                             '151130, 118701, 118803, 119598, 119609, 119019, 122639, 119063, 151036,121279,119800'}

headers = {
    'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com",
    'x-rapidapi-key': keys['RAPID_API']
    }

response = requests.request("GET", url, headers=headers, params=querystring)
r = response.json()


# The below line will make scheme_code appear in list e.g ['120389', '120503', '119125']
scheme_code = [i.strip() for i in querystring.get("SchemeCode").split(',')]


# Below for loop is to arrange the JSON as per the order of scheme_code
for i in scheme_code:  # Iterating for every scheme code
    for k in r:
        if k['Scheme Code'] == i:
            fund_name.append(k['Scheme Name'])
            nav.append(float(k['Net Asset Value']))  # Converting net asset value to float
            nav_date.append(k['Date'])
            scheme_num.append(i)


df = pd.DataFrame(final_dict)


# This is to check if any of the scheme is missing in output scheme
def list_compare():
    temp = [ii for ii in scheme_code if ii not in df['Scheme_Code'].tolist()]
    return temp


print(df)
print('\n')
print('Total Scheme Requested: ', len(scheme_code))
print('All scheme returned data' if len(df) == len(scheme_code) else
      'Warning : Some scheme did not return data: {}'.format(','.join(t for t in list_compare())))

df.to_excel('D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/Fund_with_NAV.xlsx', index=False, header=True)
# print(df['Scheme_Code'].tolist())
# Not exists: 119807


