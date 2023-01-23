import requests
import pandas
import os

path = 'D:\\Essentials\\Blue Bird ==========\\Tracing\\Pycharm_project\\'
response = requests.get('https://api.mfapi.in/mf', stream=True)

fund_name = "'HDFC Money market - Direct'"  # Enter the fund name here, make sure to pass this as string

with open(path+'scheme_code.json', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
response.close()
f.close()

# Converting JSON to data frame
df = pandas.read_json(path+'scheme_code.json')
df['schemeName'] = df['schemeName'].apply(lambda x: x.upper())  # Converting all scheme names to upper
df2 = df.query('schemeName.str.contains({})'.format(fund_name.upper()))

print(df2)

# Deleting stored JSON file
os.remove(path=path+'scheme_code.json')
