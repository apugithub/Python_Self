import requests
from bs4 import BeautifulSoup as bs

url = requests.get('https://covidstat.info')
soup = bs(url.content,'html.parser')

print(soup)

for i in soup.findAll('link'):
    #print(i.get('href'))
    j = i.get('href')
    if j[0:3] == 'htt':  #Here only links with starting 'http' will be fetched
        print(j)









