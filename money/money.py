
from bs4 import BeautifulSoup
import requests

head_Html_lotto='https://tw.money.yahoo.com/fund/history/F0HKG05X22:FO'
res = requests.get(head_Html_lotto, timeout=30)
soup = BeautifulSoup(res.text, 'html.parser')
content = []
content1 = []
for index, data in enumerate(soup.select('div#recent-price')): 
  for index, date in  enumerate(data.select('td.short-date')) :
    date = date.text
    content.append(date)
    for index, value in  enumerate(data.select('td.zero')) :
     value = value.text
     content1.append(value)
hash = {k:v for k, v in zip(content, content1)}
for key, value in hash.items():
    print( "日期: {}, 淨值:{}".format(key,value)  )
     