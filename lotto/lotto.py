
from bs4 import BeautifulSoup
import requests

head_Html_lotto='https://movies.yahoo.com.tw/'
res = requests.get(head_Html_lotto, timeout=30)
print(res.text)
print(res.text, file=open('file.txt', 'w'))
