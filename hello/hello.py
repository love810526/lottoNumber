
from bs4 import BeautifulSoup
import requests

head_Html_lotto='https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'
res = requests.get(head_Html_lotto, timeout=30)
print(res.text, file=open('file.txt', 'w'))
