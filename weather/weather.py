import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from selenium import webdriver
from phantomjs_bin import executable_path

def New_Taipei_City():
    target_url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm'
    driver = webdriver.PhantomJS(executable_path=executable_path)
    driver.get(target_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = ""
    result = ""
    for data in soup.select('#ftext'):
        title = str(data)
        content = title.split("<br/><br/>")[2]
        result = '新北市天氣: {}'.format(content)

    return result
print(New_Taipei_City())