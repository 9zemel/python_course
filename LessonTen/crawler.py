import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = requests.get("https://en.wikipedia.org{}".format(articleUrl))
    html = html.text
    bs = BeautifulSoup(html, 'html.parser')
    # links = bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    # print(links)
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Ozon.ru')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    print("https://en.wikipedia.org"+newArticle)
    links = getLinks(newArticle)
