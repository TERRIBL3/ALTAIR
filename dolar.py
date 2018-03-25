import requests
import bs4
from bs4 import BeautifulSoup as bs 

def dolar_func():
	pagina = requests.get('https://www.dolarhoje.net.br/')
	pagina_soup = bs(pagina.text,'html.parser')
	soup = pagina_soup.select('table tbody td')
	lista = [i.getText() for i in soup]
	cont1 = 1
	cont0 = 0
	dic = {}
	for i in range(5):
		dic[lista[cont0]] = lista[cont1]
		cont0 += 2
		cont1 += 1
		if cont1 % 2 == 0:
			cont1+= 1
	return dic