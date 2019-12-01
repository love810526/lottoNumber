
# #
from bs4 import BeautifulSoup
import requests


head_Html_movie='https://movies.yahoo.com.tw/'
res = requests.get(head_Html_movie, timeout=30)
soup = BeautifulSoup(res.text, 'html.parser')
content = ""
for index, data in enumerate(soup.select('div.movielist_info h2 a')):  
        if index > 8:
                break;
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
print(content)
