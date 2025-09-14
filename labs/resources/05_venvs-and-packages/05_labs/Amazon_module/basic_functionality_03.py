import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.co.uk/dp/ASINCODE'
headers = {'User-Agent':'some browser UA string'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find(id='productTitle').get_text().strip()
price = soup.find('span', {'class':'priceblock_ourprice'}).get_text().strip()
print(title, price)
