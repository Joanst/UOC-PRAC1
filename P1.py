import requests
from bs4 import BeautifulSoup 

page=requests.get("https://ca.wikipedia.org/wiki/La_guerra_de_les_gal%C3%A0xies")
##print(page.status_code)
soup = BeautifulSoup(page.content, features="html.parser")
print(soup.prettify())
