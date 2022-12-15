import cloudscraper
from bs4 import BeautifulSoup
import csv

#fazer lista de termos de busca

#precisamos usar cloudscrapper para passar pelo bloqueio do cloudfare
scraper = cloudscraper.create_scraper()


busca = ['Volkswagen', 'Jaguar']

#transformar em função
for palavra in busca:
    lista_links = []
    p = 1
    while True:
        try:
            url = "https://diariodovale.com.br/page/"+ str(p) +"/?s=" + palavra
            page = scraper.get(url)
            p += 1
            print ('Página ' + str(p))

            #usamos beautiful soup para trabalhar no texto
            soup = BeautifulSoup(page.content, 'html.parser')
            h2s = soup.find_all('h2', class_='post-box-title')
            
            if len(h2s) < 1: #garante que não vai continuar se a pagina nao contiver nada
                break
            
            for i in h2s:
                lista_links.append(i.a['href'])
        except:
            break

    #salvar links em lista (preciso especificar a empresa)
    with open('./links.csv', 'a') as f:
        writer = csv.writer(f)
        for i in lista_links:
            lista = list([i])
            lista.append(palavra)
            print(lista)
            writer.writerow(lista) #coloco a string numa lista para ele iterar apenas uma vez
    f.close()
