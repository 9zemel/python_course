from bs4 import BeautifulSoup

# with open("simpleHtml.html") as html_doc:
#     content = html_doc.read()


with open('ozon.htm') as html_doc:
    content = html_doc.read()

soup = BeautifulSoup(content, 'html.parser')

print(type(soup.find_all('a')))

print(soup.h1)

