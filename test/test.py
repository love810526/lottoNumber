import requests
from bs4 import BeautifulSoup

def search():  
# Google 搜尋 URL
  google_url = 'https://tw.search.yahoo.com/search'

# 查詢參數
  my_params = {'p': '寒流'}

# 下載 Google 搜尋結果
  r = requests.get(google_url, params = my_params)

# 確認是否下載成功
  if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 原始碼
    soup = BeautifulSoup(r.text, 'html.parser')
  # 觀察 HTML 原始碼
  # print(soup.prettify())> h3 > a[href^="/url"]
    content = ""
  # 以 CSS 的選擇器來抓取 Google 的搜尋結果
    for index, items in enumerate(soup.select('h3.title a.ac-algo')):  
    # 標題
      title = '{}. {}\n'.format(index,items.text)
#     print("標題：" + items.text)
    # 網址
      link = items.get('href')
#     print("網址：" + items.get('href'))
      content += '{}\n{}\n'.format(title, link)
  return content

print(search())
    
