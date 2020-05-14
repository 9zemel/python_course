# Сделать с помощью requests программу, в которой можно задавать
# Запрос и регион в Yandex поиске в input.
# Полезные ссылки она сохраняет в файле,
# В названии которого есть текст запроса и код области.
# Сохраняет она только ссылки с абсолютным путем типа https://

import requests
import re
from bs4 import BeautifulSoup

search_query = input('Введите поисковый запрос: ')
search_code = input('Введите код региона для поиска: ')
payload = {'text': "ozon", 'lr': "159"}
payload['text'] = search_query
payload['lr'] = search_code

r = requests.get("https://yandex.ru/search/", params=payload)

soup = BeautifulSoup(r.text, 'html.parser')
filename = ', '.join(list(payload.values()))
with open(filename, 'a') as file:
    for link in soup.find_all("a", href=re.compile('^https:\/\/+\S{1,}')):
        file.write(link.get("href") + "\n")
