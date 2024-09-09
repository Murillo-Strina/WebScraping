import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=value+of+bitcoin+to+real"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

req_novo = requests.get(link, headers = headers)

site_bitcoin = BeautifulSoup(req_novo.text,'html.parser')

value_bitcoin = site_bitcoin.find("span",class_ = "pclqee")

bitcoin_value = value_bitcoin.get_text()

print("==================================")
print("Bitcoin to Real: R$ ",bitcoin_value)
print("==================================")

