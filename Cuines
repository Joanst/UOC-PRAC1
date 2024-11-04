# -*- coding: utf-8 -*-
"""
@author: Joan i Victor
"""

from bs4 import BeautifulSoup 
import requests
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import random

#Modificar User Agent

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
]

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": random.choice(user_agents)
}
    
# Web a la que accedim
pagina="https://www.3cat.cat/tv3/cuines/receptes/"

# Obtenim la pàgina sencera i creem un objecte beautiful soup per treballar-hi
page= requests.get(pagina, headers=headers)
soupPage= BeautifulSoup(page.content, features="html.parser")

# Obtenir el numero de pàgines de receptes
ultimaPagina = soupPage.find("p", class_="numeracio")
ultimaPagina = ultimaPagina.text.split(" ")[3]
ultimaPagina = int(ultimaPagina)
print("Tenim un total de", ultimaPagina, "pagines! \n")

#'''

def extreure_receptes(website, numpag):
    receptes = website.find_all("div", class_ = "M-destacat cuines T-cuinesTema")

    for recepta in receptes:

        nom = recepta.find("a", {"class": "titol--a"})
        img = recepta.find("img", class_="foto")
        
        pagina_url = "https://www.3cat.cat" + nom["href"]
        try:
            pagina_img = img["src"]
        except:
            pagina_img = None
        urls.append((pagina_url, pagina_img, numpag))

urls = []
i = 1

driver = webdriver.Chrome()
driver.get(pagina)
time.sleep(1)

cookies = driver.find_element(By.ID, "didomi-notice-disagree-button")
cookies.click()

print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), "\n")

while i <=3:# ultimaPagina:
    print("Queden:", ultimaPagina - i, "pagines\n")
    website = BeautifulSoup(driver.page_source, features="html.parser")
    extreure_receptes(website, i)
    if i != ultimaPagina:
        try:
            seguent = driver.find_element(By.CSS_SELECTOR, "li.R-seg a[data-toggle='tab']")
            seguent.click()
        except:
            break
        time.sleep(random.uniform(2, 4))
    i += 1

driver.quit()

print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), "\n")
numreceptes = len(urls)
print("Tenim", numreceptes, "receptes.")

with open('urls.txt', 'w') as f:
    for url, img, numpag in urls:
        f.write(f"{url}, ")
        f.write(f"{img}, ")
        f.write(f"{numpag}\n")
        
llistaReceptes = []
numrecepta = 0
       
for linkRecepta, img_url, numpag in urls:
    numrecepta += 1
    
    page = requests.get(linkRecepta, headers=headers)
    soupPage = BeautifulSoup(page.content, features="html.parser")
    
    # Obtenim el nom de la recepta
    nomRecepta = soupPage.find_all("h1")[1]
    nomRecepta = nomRecepta.string
    print(nomRecepta)
    print("(",numrecepta,"/",numreceptes,")\n")
    
    # Obtenim els tags
    try:
        div_tags = soupPage.find("div", class_ = "llistat-tags")
        a_tags = div_tags.find_all("a")
        Etiquetes = [tag.string for tag in a_tags]
    except:
        Etiquetes = None
#    print(Etiquetes)
    
    # Obtenim la info basica
    div_info = soupPage.find("div", class_ = "span4 informacio-basica")
    li_info = div_info.find_all("li")
    
    # Obtenim la dificultat
    try:
        Dificultat_bloc = div_info.find("span", string="Dificultat: ")
        Dificultat = Dificultat_bloc.next_sibling.strip()
    except:
        Dificultat = None
        
    # Obtenim el temps
    try:
        Temps_bloc = div_info.find("span", string="Temps: ")
        Temps = Temps_bloc.next_sibling.strip()        
    except:
        Temps = None
    
    # Obtenim la dieta
    try:
        Dieta_bloc = div_info.find("span", string="Dieta: ")
        Dieta = Dieta_bloc.next_sibling.string
    except:
        Dieta = None
    
#    print(Dificultat)
#    print(Temps)
#    print(Dieta)
    
    # Obtenim els ingredients
    div_ingredients = soupPage.find("div", class_ = "ingredients")
    li_ingredients = div_ingredients.find_all(["li", "p"])
    Ingredients = [ingredient.get_text(strip = True) for ingredient in li_ingredients]
#    print(Ingredients)
    
    # Obtenim la preparacio
    preparacio = soupPage.find("h2", string="PREPARACIÓ")
    pasos = preparacio.find_next_sibling().find_all(["li", "p", "div"])
    Preparacio = [pas.string for pas in pasos]
#    print(Preparacio)
    
    # Obtenim la fotografia
    try:
        Imatge = img_url
    except: 
        Imatge = None
#    print(Imatge)
#'''    
    # Creem el diccionari
    recepta = {
        "Nom":nomRecepta,
        "Link":linkRecepta,
        "Pagina": numpag,
        "Imatge": img_url,
        "Dificultat": Dificultat,
        "Temps": Temps,
        "Dieta": Dieta,
        "Ingredients": Ingredients,
        "Preparacio": Preparacio,
        "Tags": Etiquetes
        }
    #afegim a la llista de diccionaris

    llistaReceptes.append(recepta)

# Creem l'arxiu csv i exportem tota la llista de diccionaris
with open('receptes.csv', mode='w', newline='', encoding='utf-8') as arxiu_csv:
    camps=llistaReceptes[0].keys()
    escriptor_csv = csv.DictWriter(arxiu_csv, fieldnames=camps)
    
    escriptor_csv.writeheader()
    escriptor_csv.writerows(llistaReceptes)
#'''
