import cloudscraper
from bs4 import BeautifulSoup
import csv
import re

scraper = cloudscraper.create_scraper()

lista_links = []
with open('./links.csv', 'r') as f:
    for i in f:
        link = i.split(',')
        lista_links.append(link[0])

#print(lista_links)
lista_conteudos = []

for i in lista_links:
    url = i
    page = scraper.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1', class_='name post-title entry-title')
    pub_date = soup.find('article')
    body = soup.find('div', class_='entry')
    m = re.search('Matéria.*[,]', pub_date.text)
    row = []
    row.append(title.text)
    row.append(m.group(0))
    row.append(body.text)
    row.append(url)
    row.append(link[1])
    lista_conteudos.append(row)

with open('./conteudos.csv', 'w') as f:
    writer = csv.writer(f)
    for i in lista_conteudos:
        writer.writerow(i)
f.close()