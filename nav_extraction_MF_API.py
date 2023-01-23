import requests
import pandas as pd

# Mutual Fund API = https://www.mfapi.in/

scheme_code_path = 'D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/'

df_codes = pd.read_excel(scheme_code_path + 'Codes.xlsx')   # Just add the scheme code in this doc
df_codes_list = df_codes['Scheme_Code'].tolist()
scheme_string = ', '.join(str(x) for x in df_codes_list)

querystring = {"SchemeCode": '{}'.format(scheme_string)}

querystring_1 = {"SchemeCode": '120389, 120503, 119125, 119242, 118551, 118506, 118560, 118473, 111569, 119746, '
                               '120166, 151130, 118701, 118803, 119598, 119609, 119019, 122639, 119063, 151036,121279,'
                               '119800, 119092'}

scheme_code = [i.strip() for i in querystring.get("SchemeCode").split(',')]

fund_name = []
nav = []
nav_date = []
scheme_cd = []

final_dict = {'Fund_Name': fund_name, 'NAV': nav, 'NAV_Date': nav_date, 'Scheme_Code': scheme_cd}

for items in scheme_code:
    r = requests.get('https://api.mfapi.in/mf/{}'.format(items))
    i = r.json()

    fund_name.append(i['meta']['scheme_name'])
    nav.append(float(i['data'][0]['nav']))
    nav_date.append(i['data'][0]['date'])
    scheme_cd.append(items)


def list_compare():
    temp = [ii for ii in scheme_code if ii not in df['Scheme_Code'].tolist()]
    return temp


df = pd.DataFrame(final_dict)
print(df)
print('\n')
print('Total Scheme Requested: ', len(scheme_code))
print('All scheme returned data' if len(df) == len(scheme_code) else
      'Warning : Some scheme did not return data: {}'.format(','.join(t for t in list_compare())))

# df.to_excel('D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/Fund_with_NAV.xlsx', index=False, header= True)
