import requests
from time import sleep
from bs4 import BeautifulSoup

req = requests.get("http://192.168.153.128:5500/src/html/site/index.html")
print(req.text)