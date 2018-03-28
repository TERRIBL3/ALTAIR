import requests
from bs4 import BeautifulSoup as bs 

def pesquisar(*music):
	string = ''
	for i in music:
		string = ''.join(i)
	string = string.replace(' ','+')
	pagina = requests.get('https://www.youtube.com/results?search_query='+str(string))
	soup_pagina = bs(pagina.text,'html.parser')
	soup = soup_pagina.select('h3 a')
	titulo_link = {}
	for link in soup:
		titulo_link['song'] = link.get('href')
		break
	return titulo_link
