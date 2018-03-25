import discord
import asyncio
from scraping_xvideos import pega_comments
import html
import requests
from dolar import dolar_func
from bitcoin import bitcoin_func
client = discord.Client()
prefix = '|'

@client.event
async def on_ready():
	print('-- ON --')
	print('{}'.format(client.user.name))
	print('{}'.format(client.user.id))
	print('-----------------------\n\n')
@client.event
async def on_message(message):
	if message.content.lower().startswith('{}help'.format(prefix)):
		embed=discord.Embed(
			title='LÊ CARAIOOOo',
			color=0xed2d2d,
			description=
			'**PREFIXO =** `|`   ~~(Usar antes de qualquer comando)~~\n\n'
			'**|xvideos**                              Basicamente, você tem acesso a um comentário randômico \n\nde um vídeo randômico da página "Portuguese" do xvideos.\n\n'
			'**|bitcoin**                              Acessa o preço atual do bictoin ~~pretty much inutil~~.\n\n'
			'**|dolar**                                Acessa o preço atual do dolar pra reais.\n\n'
			'\t\t~~mito abaixo kk~~\n\n')
		
		embed.set_author(
				name='TERRIBLE',
				icon_url='https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')
		
		embed.set_footer(
				text='ᵗᵉʳʳˡᵇˡᵉ',
				icon_url='https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')
		await client.send_message(message.channel,embed = embed)
	if message.content.lower().startswith('{}xvideos'.format(prefix)):
		dicionario = pega_comments()
		pfp = requests.get("https://www.xvideos.com"+(str(dicionario['iu'])))
		embed = discord.Embed(
			title = 'Comentário do Xvideos',
			color = 0xed2d2d,
			description= '**Data:** '+'`'+str(dicionario['d'])+'`'+'\n\n**Título:** '+'`'+ str(dicionario['titulo'])+'`'+'\n\n**Usuário:** '+'`'+str(dicionario['p'])+'`'+
			'\n\n**Comentário:** '+'`'+str(html.unescape(str(dicionario['c'])))+'`'
			)
		embed.set_thumbnail(url=str(pfp.url).replace("small.jpg", "big.jpg"))
		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'https://pbs.twimg.com/profile_images/818181506216628225/EkeBaVUa_400x400.jpg'
			)
		await client.send_message(message.channel,'<@'+str(message.author.id)+'>',embed = embed )
	if message.content.lower().startswith('{}dolar'.format(prefix)):
		resultado = dolar_func()
		embed = discord.Embed(
			title = 'Preço do dolar',
			color = 0x33cc33,
			description = '**Dolar comercial:** '+'`'+str(resultado['Dólar comercial'])+'`'+'\n\n**Dolar turismo:** '+'`'+str(resultado['Dólar turismo'])+'`'+
			'\n\n**Dolar ptax:** '+'`'+str(resultado['Dólar ptax'])+'`'+'\n\n**Euro comercial:** '+'`'+str(resultado['Euro comercial'])+'`'+'\n\n**Euro turismo:** '+'`'+str(resultado['Euro turismo'])+'`'+'\n\n'
			)
		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'http://www.agkcorretora.com.br/media/image/artigos/Frente-dolar-Agk-Corretora-grande.jpg'
			)
		await client.send_message(message.channel, embed = embed)
	if message.content.lower().startswith('{}bitcoin'.format(prefix)):
		embed = discord.Embed(
			title = 'Valor do bitcoin',
			color = 0xffff00,
			description = '**'+str(bitcoin_func())+'**'
			)
		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'http://s2.glbimg.com/HEbW5ZxGZNs7UJeMNs6Pp5m2EKQ=/0x600/s.glbimg.com/po/tt2/f/original/2016/03/22/bitcoin-btc-symbol-d75950754.png'
			)
		await client.send_message(message.channel, embed = embed)
