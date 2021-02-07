from bs4 import BeautifulSoup
import requests

head_Html_gold='https://rate.bot.com.tw/gold?Lang=zh-TW'
res = requests.get(head_Html_gold, timeout=30)
soup = BeautifulSoup(res.text, 'html.parser')
content = ""
date = ""
sell = ""
sold = ""
for index, data in enumerate(soup.select('div.cf div')):
    date = data.text.strip()  

for index, detail in enumerate(soup.select('div.hasscript-div td.text-right')):
    if index < 1:
        sell = detail.text.strip()
    if index < 2:
        sold = detail.text.strip()
content += "{}\n本行賣出:{}\n本行買進:{}\n".format(date, sell, sold)
print(content)