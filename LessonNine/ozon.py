import requests
import re
from bs4 import BeautifulSoup

payload = {'text': "ozon", 'lr': "159"}

r =requests.get("https://yandex.ru/search/", params=payload)

# print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# filename = str(dict.values(payload))
filename = ', '.join(list(payload.values()))
print('filename', filename)
# with open ('result.txt', 'a') as file:
#     for link in soup.find_all("a", href = re.compile('^https://')):
#         # print(link.get("href"))
#         file.write(link.get("href") + "\n")



