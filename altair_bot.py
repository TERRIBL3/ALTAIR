import os
import html

import requests
import discord
from discord.ext.commands import Bot

from dolar import dolar_func
from bitcoin import bitcoin_func
from scraping_xvideos import pega_comments

bot = Bot(command_prefix='|')
TOKEN = os.environ['TOKEN']


@bot.event
async def on_ready():
	print('-- ON --')
	print('{}'.format(bot.user.name))
	print('{}'.format(bot.user.id))
	print('-----------------------\n\n')


bot.remove_command("help") # remover comando padrão
@bot.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(
		title = 'LÊ CARAIOOOo',
		color = 0xed2d2d,
		description =
			'**PREFIXO =** `|`   ~~(Usar antes de qualquer comando)~~\n\n'
			'**|xvideos**                              Basicamente, você tem acesso a um comentário randômico \n\nde um vídeo randômico da página "Portuguese" do xvideos.\n\n'
			'**|bitcoin**                              Acessa o preço atual do bictoin ~~pretty much inutil~~.\n\n'
			'**|dolar**                                Acessa o preço atual do dolar pra reais.\n\n'
			'\t\t~~mito abaixo kk~~\n\n')

	embed.set_author(
		name = 'TERRIBLE',
		icon_url = 'https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')

	embed.set_footer(
		text = 'ᵗᵉʳʳˡᵇˡᵉ',
		icon_url = 'https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')

	return await bot.send_message(ctx.message.channel, embed=embed)


@bot.command(pass_context=True)
async def xvideos(ctx):
	dicionario = pega_comments()
	pfp = requests.get("https://www.xvideos.com" + str(dicionario['iu']))

	embed = discord.Embed(
		title = 'Comentário do Xvideos',
		color = 0xed2d2d,
		description = '**Data:** '+'`'+str(dicionario['d'])+'`'+'\n\n**Título:** '+'`'+ str(dicionario['titulo'])+'`'+'\n\n**Usuário:** '+'`'+str(dicionario['p'])+'`'+
		'\n\n**Comentário:** '+'`'+str(html.unescape(str(dicionario['c'])))+'`')

	embed.set_thumbnail(url=str(pfp.url).replace("small.jpg", "big.jpg"))

	embed.set_footer(
		text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
		icon_url = 'https://pbs.twimg.com/profile_images/818181506216628225/EkeBaVUa_400x400.jpg')

	return await bot.send_message(ctx.message.channel,'<@'+str(ctx.message.author.id)+'>', embed=embed )


@bot.command(pass_context=True)
async def dolar(ctx):
	resultado = dolar_func()
	embed = discord.Embed(
		title = 'Preço do dolar',
		color = 0x33cc33,
		description = '**Dolar comercial:** '+'`'+str(resultado['Dólar comercial'])+'`'+'\n\n**Dolar turismo:** '+'`'+str(resultado['Dólar turismo'])+'`'+
		'\n\n**Dolar ptax:** '+'`'+str(resultado['Dólar ptax'])+'`'+'\n\n**Euro comercial:** '+'`'+str(resultado['Euro comercial'])+'`'+'\n\n**Euro turismo:** '+'`'+str(resultado['Euro turismo'])+'`'+'\n\n')

	embed.set_footer(
		text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
		icon_url = 'http://www.agkcorretora.com.br/media/image/artigos/Frente-dolar-Agk-Corretora-grande.jpg')

	return await bot.send_message(ctx.message.channel, embed=embed)


@bot.command(pass_context=True)
async def bitcoin(ctx):
	embed = discord.Embed(
		title = 'Valor do bitcoin',
		color = 0xffff00,
		description = '**'+str(bitcoin_func())+'**')

	embed.set_footer(
		text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
		icon_url = 'http://s2.glbimg.com/HEbW5ZxGZNs7UJeMNs6Pp5m2EKQ=/0x600/s.glbimg.com/po/tt2/f/original/2016/03/22/bitcoin-btc-symbol-d75950754.png')

	return await bot.send_message(ctx.message.channel, embed=embed)


bot.run(TOKEN)
