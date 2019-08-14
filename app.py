from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('zTVKvRch+94AFPWaOrhNug9Ufmu+O4zmbqc7BbP9+saNd8rTtgWCtLuS0WW9mkSKE4zT/XosFLqegvHomyLBGrN7qQkcUWk6JY60yjr4MaBU5UaQdY56ip568NJg5s8KhCa1vGdScO7lD0gWLvPAJwdB04t89/1O/w1cDnyilFU=N')
# Channel Secret
handler = WebhookHandler('b0041348478140a004fb1b8cebc05ea9')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# movie 
def movie():
  head_Html_movie='https://movies.yahoo.com.tw/'
  res = requests.get(head_Html_movie, timeout=30)
  soup = BeautifulSoup(res.text, 'html.parser')
  content = ""
  for index, data in enumerate(soup.select('div.movielist_info h2 a')):  
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
  return content

# 基金
def fund1():
 head_Html_lotto='https://tw.money.yahoo.com/fund/history/F0HKG05X22:FO'
 res = requests.get(head_Html_lotto, timeout=30)
 soup = BeautifulSoup(res.text, 'html.parser')
 content = []
 content1 = []
 finalResult = ""
 for index, data in enumerate(soup.select('div#recent-price')): 
   for index, date in  enumerate(data.select('td.short-date')) :
     date = date.text
     content.append(date)
     for index, value in  enumerate(data.select('td.zero')) :
      value = value.text
      content1.append(value)
 hash = {k:v for k, v in zip(content, content1)}

 for key, value in hash.items():
    finalResult += "日期: {}, 淨值:{}\n".format(key,value)
 return finalResult
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID
    elif(text=="最新電影"):
        a=movie()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif(text=="安聯台灣科技"):
        a=fund1()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    elif(text=="早安"):
        reply_text = "Good Morning"        
    else:
        reply_text = text
#如果非以上的選項，就會學你說話

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
