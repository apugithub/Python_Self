import requests
from bs4 import BeautifulSoup as bs  #is required to parse HT
import pandas as pd

url_list = ['https://www.moneycontrol.com/mutual-funds/nav/axis-liquid-fund-direct-plan-growth/MAA190',
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
            'https://www.moneycontrol.com/mutual-funds/nav/nippon-india-tax-saver-fund-direct-plan-growth/MRC938',
            'https://www.moneycontrol.com/mutual-funds/nav/sbi-blue-chip-fund-direct-plan-growth/MSB532',
            'https://www.moneycontrol.com/mutual-funds/nav/sbi-equity-hybrid-fund-direct-plan-growth/MSB516',
            'https://www.moneycontrol.com/mutual-funds/nav/dsp-equity-bond-fund-direct-plan-growth/MDS608',
            'https://www.moneycontrol.com/mutual-funds/nav/parag-parikh-flexi-cap-fund-direct-plan/MPP002',
            'https://www.moneycontrol.com/mutual-funds/nav/hdfc-index-fund-direct-plan-nifty-50-plan/MHD1152',
            'https://www.moneycontrol.com/mutual-funds/nav/l-t-midcap-fund-direct-plan/MCC275',
            'https://www.moneycontrol.com/mutual-funds/nav/idfc-banking-psu-debt-fund-direct-plan-growth/MAG841'
            ]

fund_name = []  # Array to store all fund names, separated by coma
fund_nav = []  # Array to store all fund NAVs, separated by coma
nav_date = []  # Array to store all NAV dates, separated by coma

for i in url_list:
    url = requests.get(i)

    soup = bs(url.content, 'html.parser')

    #a = soup.find('div', attrs={'class': 'common_left'})
    #name = a.find('h1', attrs={'class': 'page_heading'})
    name = soup.find('h1', attrs={'class': 'page_heading'})  # we can get from h1 directly as with h1 and the same class
    # there are no other values, other than the fund name

    b = soup.find('div', attrs={'class': 'leftblok'})  # Going into main HTML block
    nav = b.find('span', attrs={'class': 'amt'})   # inside block b, appropriate class is chosen
    date = b.find('div', attrs={'class': 'grayvalue'})

    #print (name, nav)


    nav_float = float(nav.text[1:]) # As first letter  of the extracted NAV is rupee sign, hence discarding the first letter,
    #then converting the same to a floating number, to avoid casting issue at excel

    fund_name.append(name.text) # we are appending only the text part of extracted field 'name'
    fund_nav.append(nav_float)  # just appending nav_float value
    nav_date.append(date.text) # we are appending only the text part of extracted field 'date'


df = pd.DataFrame({'Fund Name':fund_name, 'Fund NAV':fund_nav, 'NAV Date': nav_date})
df.to_excel(r'D:/Essentials/Blue Bird ==========/Banks/Mutual Funds/Fund_with_NAV.xlsx', index= False, header=True)

print(df)


