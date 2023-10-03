import requests

from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/html/env/index.html"

response = requests.get(url)
html_code = response.text
soup = BeautifulSoup(response.content, 'html.parser')

print(html_code)

#Code HTML Source
#print(response.content)

#Récupère les éléments du HTML
print(soup.title)

#Récupère toutes les listes avec la class
list_bs = soup.find_all("li", class_= "list")
print(list_bs)

lists = []
for displist in list_bs:
    lists.append(displist.string)

print(lists)
    