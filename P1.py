import requests
import time 
import csv
from bs4 import BeautifulSoup 

#Modificar User Agent
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

# Web a la q accedim
#pagina="https://ca.wikipedia.org/wiki/La_guerra_de_les_gal%C3%A0xies"
pagina="https://www.lapastaperalscatalans.cat/pasta/receptes"

#obtenim la pàgina sencera i creem un objecte beautiful soup per treballar-hi
page= requests.get(pagina, headers=headers)
soupPage= BeautifulSoup(page.content, features="html.parser")

#Definim la llista per a desar els links de totes les receptes
linksReceptes=[]

#Obtenir el numero de pàgines de receptes
ultimaPagina= soupPage.find("a", class_="last")
ultimaPagina= int(ultimaPagina.text)

for i in range(1,ultimaPagina+1):
    pagina="https://www.lapastaperalscatalans.cat/pasta/receptes/page/"+str(i)
    page= requests.get(pagina, headers=headers)
    soupPage= BeautifulSoup(page.content, features="html.parser")
    receptes =soupPage.find_all("h2", class_="entry-title")
    for recepta in receptes :
        linkRecepta= recepta.find("a").get("href")
        ## Prenem nomes les receptes, eliminem els articles que no ho son.
        if linkRecepta.split("/")[3] == "receptes":
            linksReceptes.append(linkRecepta)
    

##Aqui desarem totes les receptes
llistaReceptes=[]

#Rastregem totes les receptes de la pàgina i les desem en una llista de diccionaris
for linkRecepta in linksReceptes:
    #Explorem la pàgina de la recepta
    pagina= linkRecepta
    page= requests.get(pagina, headers=headers)
    soupPage= BeautifulSoup(page.content, features="html.parser")
    
    #Obtenim el nom de la recepta
    nomRecepta =soupPage.find("h1", class_="entry-title")
    nomRecepta=nomRecepta.get_text()

    #Obtenim la categoria
    nomCategoria = linkRecepta.split("/")[4]
    
    #Obtenim els ingredients
    ingredients_ =soupPage.find("div", class_="entry-content content") 
    ingredients_ = ingredients_.find_all("li")

    ingredients=[]
    for ingredient in ingredients_:
        ingredient=ingredient.get_text().strip("\n")
        ingredients.append(ingredient)

    #Obtenim la preparacio 
    #Falta treure el text introductori
    passos=soupPage.find("div", class_="entry-content content") 
    passos=passos.find_all("p")
    preparacio=""
    for pas in passos:
        preparacio=preparacio+"\n"+pas.get_text()

    #Obtenim els tags
    tags=[]
    tags_ = soupPage.find("footer", class_="entry-footer cf" )
    if tags_ is not None:
        tags_ = tags_.find_all("a")
        for tag in tags_:
            tags.append(tag.get_text())
    
    #Creem el diccionari
    recepta = {
        "Nom":nomRecepta,
        "Link":linkRecepta,
        "Categoria":nomCategoria,
        "Ingredients": ingredients,
        "Preparacio": preparacio,
        "Tags": tags
        }
    #afegim a la llista de diccionaris

    llistaReceptes.append(recepta)

'''
#Només amb una recepta per a provar
pagina= "https://www.lapastaperalscatalans.cat/tipus-de-pasta/macarrons/penne-rigate-amb-ragu-blanc-de-botifarra.html"
page= requests.get(pagina, headers=headers)
soupPage= BeautifulSoup(page.content, features="html.parser")

#Obtenim el nom de la recepta
nomRecepta =soupPage.find("h1", class_="entry-title")
nomRecepta=nomRecepta.get_text()

#Obtenim els ingredients
ingredients_ =soupPage.find("div", class_="entry-content content") 
ingredients_ = ingredients_.find_all("li")
ingredients=""
for ingredient in ingredients_:
    ingredient=ingredient.get_text().strip("\n")
    ingredients = ingredients +ingredient+", "

#Obtenim la preparacio 
#Falta treure el text introductori
passos=soupPage.find("div", class_="entry-content content") 
passos=passos.find_all("p")
preparacio=""
for pas in passos:
    preparacio=preparacio+"\n"+pas.get_text()

#Obtenim els tags
tags=[]
tags_ = soupPage.find("footer", class_="entry-footer cf" )
tags_ = tags_.find_all("a")
for tag in tags_:
    tags.append(tag.get_text())



#Creem el diccionari
recepta = {
    "Nom":nomRecepta,
    "Link":linkRecepta,
    "Ingredients": ingredients,
    "Preparacio": preparacio,
    "Tags": tags
    }
#afegim a la llista de diccionaris
llistaReceptes.append(recepta)

'''
#Creem l'arxiu csv i exportem tota la llista de diccionaris
with open('receptes.csv', mode='w', newline='', encoding='utf-8') as arxiu_csv:
    camps=llistaReceptes[0].keys()
    escriptor_csv = csv.DictWriter(arxiu_csv, fieldnames=camps)
    
    escriptor_csv.writeheader()
    escriptor_csv.writerows(llistaReceptes)
    


