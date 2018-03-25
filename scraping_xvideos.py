import requests
from bs4 import BeautifulSoup as bs
import random
import json

def pega_comments():
	var = True
	while var:
		try:
			pagina = requests.get('https://www.xvideos.com/porn/portugues/' + str(random.randint(1,30)))
			soup = bs(pagina.text,'html.parser')

			linkElems = soup.select('p a')
			titulo_link = {}
			for link in linkElems:
				titulo_link[link.get('title')] = link.get('href')
			titulo = [i for i in titulo_link.keys()]
			escolhido = random.choice(titulo)

			pagina_coment = requests.get('https://www.xvideos.com/video-get-comments/'+str(titulo_link[escolhido][6:14])+'/0')
			texto_json = json.loads(str(pagina_coment.text))
			cont = False
			dicionario = {}
			for key,value in texto_json.items():
				if type(value) is list:
					cont = True
					dicionario = value
			lista = [i for i in dicionario]
			dict_end = lista[random.randint(1,len(lista))-1]

			while cont is False:
				pagina_coment = requests.get('https://www.xvideos.com/video-get-comments/'+str(titulo_link[escolhido][6:14])+'/0')
				texto_json = json.loads(str(pagina_coment.text))
				cont = False
				dicionario = {}
				for key,value in texto_json.items():
					if type(value) is list:
						cont = True
						dicionario = value
				lista = [i for i in dicionario]
				dict_end = lista[random.randint(1,len(lista))-1]
				dict_end['titulo'] = escolhido
			dict_end['titulo'] = escolhido
			#print('https://www.xvideos.com/video-get-comments/'+str(titulo_link[escolhido][6:14])+'/0')
			#return dict_end
			print(dict_end)
			break
		except:
			pass
pega_comments()