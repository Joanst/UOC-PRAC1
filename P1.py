import requests
import time 
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
'''
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
        linksReceptes.append(linkRecepta)
    

for linkRecepta in linksReceptes:
    print(linkRecepta)

print("Tenim "+str(len(linksReceptes))+" Receptes")

'''


#Explorem la pàgina de la recepta
pagina= "https://www.lapastaperalscatalans.cat/receptes/peix/pasta-amb-carbassons-tonyina-llimona-i-perfum-dalfabrega-i-menta.html"

page= requests.get(pagina, headers=headers)
soupPage= BeautifulSoup(page.content, features="html.parser")

#Obtenim el nom de la recepta
nomRecepta =soupPage.find("h1", class_="entry-title")
nomRecepta=nomRecepta.get_text()
#Obtenim els ingredients
ingredients =soupPage.find("div", class_="entry-content content") 
ingredients = ingredients.find_all("li")
llistaIngredients =[]
for ingredient in ingredients:
    llistaIngredients.append(ingredient.get_text())






'''
#Obtenim el numero màxim de pàgines de receptes que te la web
ultimaPagina= soupPage.find("a", class_="last")
ultimaPagina= int(ultimaPagina.text)
print("el document té "+str(ultimaPagina)+" pàgines de receptes")


#Obtenim el titol de la primera recepta
recepta =soupPage.find("h2", class_="entry-title")
titolRecepta= recepta.get_text()
print("el nom de la primera recepta és: "+titolRecepta)

#Obtenim el link de la primera recepta
linkRecepta= recepta.find("a")
linkRecepta= linkRecepta.get("href")
print("el link de la recepta és: "+linkRecepta)

'''
''' La primera pagina està inclosa dins el proper loop
#afegim tots els links de la primera pàgina de receptes en una llista
receptes =soupPage.find_all("h2", class_="entry-title")
for recepta in receptes :
    #nomRecepta= recepta.get_text().strip("\n")
    linkRecepta= recepta.find("a").get("href")
    #print(nomRecepta)
    #print(linkRecepta+"\n")
    linksReceptes.append(linkRecepta)
'''
