import requests
from bs4 import BeautifulSoup as bs

url = requests.get('https://covidstat.info')
soup = bs(url.content,'html.parser')

a = soup.find('div', attrs={'class':'nk-cov-data'})
b = a.find('div', attrs={'class':'amount'})

print(b.text)

