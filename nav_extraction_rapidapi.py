# This api is taken from rapid api and the app link is as below, here I have modified the code as per my need --
# # https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav/

# While adding new fund add the same in 'scheme_code' (get from https://www.mfapi.in/) as per line 40
# Creation date: 01-01-2022
# Last update date: 15-05-2023
import requests
import pandas as pd
import json
import logging
import win32com.client
# import time

location = 'D:\\Essentials\\Blue Bird ==========\\Tracing\\Pycharm_project\\'
scheme_code_path = 'D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/'

# Setting logging to DEBUG will return every type of message
logging.basicConfig(level=logging.DEBUG, filename=location + 'NAV_Extaction(rapidapi).log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filemode='a')
logger = logging.getLogger()
logging.info('################################# Initiating #################################################')


# This is to extract the rapid api key
f = open('D:/Essentials/Blue Bird ==========/Documents/Todoist/API_Keys.json')
keys = json.load(f)


fund_name = []
nav = []
nav_date = []
scheme_num = []

final_dict = {'Fund_Name': fund_name, 'NAV': nav, 'NAV_Date': nav_date, 'Scheme_Code': scheme_num}

url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchLatestNAV"


df_codes = pd.read_excel(scheme_code_path + 'Codes.xlsx')   # Just add the scheme code in this doc
df_codes_list = df_codes['Scheme_Code'].tolist()
scheme_string = ', '.join(str(x) for x in df_codes_list)

querystring = {"SchemeCode": '{}'.format(scheme_string)}


headers = {
    'x-rapidapi-host': "latest-mutual-fund-nav.p.rapidapi.com",
    'x-rapidapi-key': keys['RAPID_API']
    }


response = requests.request("GET", url, headers=headers, params=querystring)
r = response.json()
logging.info('Received JSON response')

# The below line will make scheme_code appear in list e.g ['120389', '120503', '119125']
scheme_code = [i.strip() for i in querystring.get("SchemeCode").split(',')]


logging.info('Traversing through scheme code')
# Below for loop is to arrange the JSON as per the order of scheme_code
for i in scheme_code:  # Iterating for every scheme code
    for k in r:
        if k['Scheme Code'] == i:
            fund_name.append(k['Scheme Name'])
            nav.append(float(k['Net Asset Value']))  # Converting net asset value to float
            nav_date.append(k['Date'])
            scheme_num.append(i)

logging.info('Scheme code traversal is over')
df = pd.DataFrame(final_dict)
logging.info('Data frame creation is over')


# This is to check if any of the scheme is missing in output scheme
def list_compare():
    temp = [ii for ii in scheme_code if ii not in df['Scheme_Code'].tolist()]
    return temp


print(df)
print('\n')
print('Total Scheme Requested: ', len(scheme_code))
print('All scheme returned data' if len(df) == len(scheme_code) else
      'Warning : Some scheme did not return data: {}'.format(','.join(t for t in list_compare())))
logging.info('All scheme returned data' if len(df) == len(scheme_code) else
             'Warning : Some scheme did not return data: {}'.format(','.join(t for t in list_compare())))

try:
    df.to_excel(scheme_code_path + 'Fund_with_NAV.xlsx', index=False, header=True)
    logging.info('Data written to Excel..')
    print('Data written to excel')
except Exception as e:
    logging.info('There are issue writing in Excel, it may be kept open')
    logging.error(e)
    print('ERROR in wring data to excel')


# This part is to refresh the MF Investment Tracker as per latest NAV
try:
    excelapp = win32com.client.Dispatch("Excel.Application")
    wb = excelapp.Workbooks.Open("D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/MF Investments tracker.xlsx")
    wb.RefreshAll()
    excelapp.CalculateUntilAsyncQueriesDone()  # This will wait till the refresh is complete or use below line
    # time.sleep(1)
    wb.Save()
    excelapp.Quit()
    print('\nData refreshed in - \'MF Investments tracker\' as per latest NAV')
    logging.info('Data refreshed in - MF Investments tracker as per latest NAV')
    print('Operations Complete !!')
except Exception as e1:
    logging.info('There are some issue refreshing - MF Investments tracker')
    logging.error(e1)
    print('There are some issue refreshing - MF Investments tracker')

# print(df['Scheme_Code'].tolist())
# Not exists: 119807
