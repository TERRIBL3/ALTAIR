from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup as bs

def pesquisar(music):
	pagina = requests.get('https://www.youtube.com/results?search_query=' + quote_plus(music))
	soup_pagina = bs(pagina.text, 'html.parser')
	link = soup_pagina.body.find_all('a', class_='yt-uix-tile-link')[1].get('href')
	return link
