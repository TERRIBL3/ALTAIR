import requests
from bs4 import BeautifulSoup as bs 

def bitcoin_func():
	pagina = requests.get('http://www.infomoney.com.br/mercados/bitcoin')
	soup = bs(pagina.text,'html.parser')
	soup_ = soup.select('div .crypto__summary-quote')
	soup_2 = soup.select('div .cm-pad-5-t')
	lista = [i.getText() for i in soup_]
	lista2 = [i.getText().strip() for i in soup_2]
	final = lista[0] +'\n'+ lista2[0]
	return final
