import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
respone = requests.get(url)
print(respone.status_code)

soup = BeautifulSoup(respone.text,features="html.parser")
print(f"hasil pemanggilan url {url}")
print(f"Title : {soup.h1.string}")