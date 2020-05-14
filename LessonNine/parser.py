import requests
from bs4 import BeautifulSoup
import re
import os

path = os.getcwd()
URL = input("Enter URL for parsing: ")

name_folder = input("Enter folder's name: ")
os.mkdir(name_folder)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('img', src = re.compile('\/[a-z]+\/\d+\/\d+\.jpg'))
results = soup.find_all('img', src = re.compile('\S+.jpg'))
print(results)
print(len(results))

for i in range (len(results)):
    link = results[i]['src']
    img_data = requests.get("https://www.combook.ru/" + link)
    with open (name_folder+ "/"+str(i)+".jpg", "wb") as handler:
        handler.write(img_data.content)