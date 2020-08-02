import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
#url = requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
url = requests.get("https://en.wikipedia.org/wiki/Michael_Learns_to_Rock")
print(url)

soup = bs(url.content,'html.parser')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    products.append(name.text)
    prices.append(price.text)


print(products,prices)













