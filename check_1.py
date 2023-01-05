import requests
import pandas

path = 'D:\\Essentials\\Blue Bird ==========\\Tracing\\Pycharm_project\\'
response = requests.get('https://api.mfapi.in/mf', stream=True)

fund_name = "'HDFC Money Market'"  # Enter the fund name here, make sure to pass this as string
print(fund_name)
with open(path+'scheme_code.json', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
response.close()
f.close()

df = pandas.read_json(path+'scheme_code.json')
df2 = df.query('schemeName.str.contains({})'.format(fund_name))

print(df2)
