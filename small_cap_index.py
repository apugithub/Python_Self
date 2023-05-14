from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time

URL = 'https://trendlyne.com/equity/technical-analysis/BSESMALLCAP/4489/bse-small-cap/'
# driver = webdriver.Firefox()
# driver.get(URL)
# time.sleep(3)
# driver.refresh()

# The below line added as the request must look like its coming from browser, else will throw connection error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.76 Safari/537.36'}  # **Refer page below

try:
    url_req = requests.get(URL, headers=headers)
    if url_req.raise_for_status(): # This method is to check if there is any 403 connect issue
        print('There is an issue')

    else:
        print('Connected successfully')
        soup = bs(url_req.content, 'lxml')   # html.parser

        price_tag = soup.find('div', attrs={'class': 'col-xs-12 col-lg-4 p0 pull-left pr05r m-r-1-md-up pt05r'})
        current_price = price_tag.find('span', attrs={'class': 'fs1p5rem fw700 LpriceCP stock-info-ho'})
        current_price_timestamp = current_price.get('data-title')
        print(current_price.text.strip() + ' || ' + current_price_timestamp)

        price_status_tag = soup.find('span', attrs={'class': 'fs085rem insight pt025r ls09px positive'})
        price_status = price_status_tag.get('data-title')
        print(price_status)  # Eg. 'BSE Small Cap is near it's 52 week high'

        ema_26_days = soup.find_all('div') # , attrs={'class': 'two-column-container p-y-0p6'})
        print(ema_26_days)


except requests.exceptions.RequestException as e:
    print("Connection refused", e)

# ** https://stackoverflow.com/questions/41946166/requests-get-returns-403-while-the-same-url-works-in-browser
