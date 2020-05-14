# Напишите парсер картинок с любого раздела сайта OZON,
# который их сохраняет на компьютер

import requests
from bs4 import BeautifulSoup
import re
import os

path = os.getcwd()
URL = 'https://www.ozon.ru/highlight/47069/'

name_folder = 'test_folder'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('img', src = re.compile('^https:+\S+\.jpg$'))


for i in range (len(results)):
    link = results[i]['src']
    img_data = requests.get(link)
    with open (name_folder+ "/"+str(i)+".jpg", "wb") as handler:
        handler.write(img_data.content)