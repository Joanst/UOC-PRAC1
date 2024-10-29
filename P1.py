import requests
import time 
from bs4 import BeautifulSoup 

##Modificar User Agent
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

## Web a la q accedim
##pagina="https://ca.wikipedia.org/wiki/La_guerra_de_les_gal%C3%A0xies"
pagina="https://www.lapastaperalscatalans.cat/pasta/receptes"


##<a href="https://www.lapastaperalscatalans.cat/pasta/receptes/page/22" class="last" title="Last Page">22</a>


##obtenim la pàgina sencera i creem un objecte beautiful soup per treballar-hi
page=requests.get(pagina, headers=headers)
soupPage = BeautifulSoup(page.content, features="html.parser")


##Obtenim el numero màxim de pàgines de receptes que te la web
ultimaPagina= soupPage.find("a", class_="last")
ultimaPagina =int(ultimaPagina.text)

blockReceptes= soupPage.find_all("h2", class_="entry-tittle")





##<a href="https://www.lapastaperalscatalans.cat/receptes/postre/coca-de-sant-juan-a-la-italiana.html" title="Permalink to: &quot;Coca de Sant Joan a la italiana&quot;">Coca de Sant Joan a la italiana</a>

print(receptes)
