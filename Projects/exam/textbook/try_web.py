import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
reponse= requests.get('https://www.lounge-b.com/', headers=headers)
soup= BeautifulSoup(reponse.text,'html.parser')
# print(reponse.text)
div_element= soup.select_one('#anchorBoxId_20923 > div > div.description > div.descInfo > ul > li.optimum_discount_price.xans-record- > span')

print(div_element.string)
