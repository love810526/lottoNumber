
from bs4 import BeautifulSoup
import requests

def test(name):
  head_Html_lotto=""
  foudName = ""
  if (name=="安聯台灣科技"):
    foudName = name
    head_Html_lotto='https://wms.firstbank.com.tw/w/wr/wr02.djhtm?a=ACDD04-47AD'
  elif (name=="貝萊德世界科技"):
   foudName = name
   head_Html_lotto='https://wms.firstbank.com.tw/w/wb/wb02.djhtm?a=SHZ71-LA37'
  elif (name=="統一全球"):
   foudName = name
   head_Html_lotto='https://wms.firstbank.com.tw/w/wr/wr02.djhtm?a=ACPS38-56BF'
  elif (name=="野村優質"):
   foudName = name
   head_Html_lotto='https://wms.firstbank.com.tw/w/wr/wr02.djhtm?a=ACIC01-52BA'
  res = requests.get(head_Html_lotto, timeout=30)
  soup = BeautifulSoup(res.text, 'html.parser')
  content = []
  content1 = []
  finalResult = ""

  for index, date in enumerate(soup.find('tbody').select('td.text-center')) :
    date = date.text
    content.append(date)
  for index, value in  enumerate(soup.find('tbody').select('td.text-right') ) :
    if (foudName =="貝萊德世界科技"):
      if (index % 2 ==0):
          value1 = value.text.strip()
    elif (foudName !="貝萊德世界科技"):
      if (index % 3 ==0):
          value1 = value.text.strip()
    content1.append(value1)

  hash = {k:v for k, v in zip(content, content1)}
  for key, value in hash.items():
     finalResult += "日期: {}, 淨值:{}\n".format(key,value)
  return name
  # for key, value in hash.items():
  #    finalResult += "日期: {}, 淨值:{}\n".format(key,value)

  # for index, data in enumerate(soup.find('tbody')): 
  #   for index, date in  enumerate(data.select('td.text-center')) :
  #    date = date.text
  #    content.append(date)
  #    for index, value in  enumerate(data.select('td.text-right')) :
  #     value = value.text
  #     content1.append(value)
  # hash = {k:v for k, v in zip(content, content1)}

  # for key, value in hash.items():
  #    finalResult += "日期: {}, 淨值:{}\n".format(key,value)
  # return finalResult

print(test("貝萊德世界科技"))