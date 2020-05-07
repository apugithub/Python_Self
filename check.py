import requests
from bs4 import BeautifulSoup as bs


url = requests.get('https://www.google.com/')

soup = bs(url.content,'html.parser')

a = soup.find('a',  attrs={'class':'gb_g'})
#c = a.find('h5').text
b = a.text

print (b)





