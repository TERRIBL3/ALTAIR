import os
import html

import requests
import discord
from discord.ext.commands import Bot

from utils.dolar import dolar_func
from utils.bitcoin import bitcoin_func
from utils.scraping_xvideos import pega_comments
from utils.marquinho_de_marco import pesquisar

bot = Bot(command_prefix='|')
TOKEN = os.environ.get('TOKEN')


@bot.event
async def on_ready():
	print('-- ON --')
	print('{}'.format(bot.user.name))
	print('{}'.format(bot.user.id))
	print('-----------------------\n\n')


bot.remove_command('help') # remover comando padrão
@bot.command(pass_context=True)
async def help(ctx):
	try:
		embed = discord.Embed(
			title = 'LÊ CARAIOOOo',
			color = 0xed2d2d,
			description =
				'**PREFIXO =** `|`   ~~(Usar antes de qualquer comando)~~\n\n'
				'**|xvideos**                              Basicamente, você tem acesso a um comentário randômico \n\nde um vídeo randômico da página "Portuguese" do xvideos.\n\n'
				'**|bitcoin**                              Acessa o preço atual do bictoin ~~pretty much inutil~~.\n\n'
				'**|dolar**                                Acessa o preço atual do dolar pra reais.\n\n'
				'**|tocar *musica* **                      Toca a música escolhida(pesquisa no youtube; É recomendado que você escolha a música, ou então\n'
				'o youtube escolherá o primeiro vídeo da aba inicial; E também se conecte a um canal de voz antes.)\n\n'
				'**|sair**                                 Só funciona se, o bot já estiver conectado a um canal. É forma de tocar outra musica também.\n\n')

		embed.set_author(
			name = 'TERRIBLE',
			icon_url = 'https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')

		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ',
			icon_url = 'https://cdn.discordapp.com/avatars/417397268891828246/8cfa6a53fd6eafb096af1ed3ab4e44e2.png?size=128')

		return await bot.send_message(ctx.message.channel, embed=embed)

	except:
		return await bot.send_message(ctx.message.channel, '<@'+ctx.message.author.id+'>' + 'Deu erro :weary:')


@bot.command(pass_context=True)
async def xvideos(ctx):
	try:
		dicionario = pega_comments()
		pfp = requests.get('https://www.xvideos.com' + dicionario['iu'])

		embed = discord.Embed(
			title = 'Comentário do Xvideos',
			color = 0xed2d2d,
			description = '**Data:** '+'`'+dicionario['d']+'`'+'\n\n**Título:** '+'`'+ dicionario['titulo']+'`'+'\n\n**Usuário:** '+'`'+dicionario['p']+'`'+
			'\n\n**Comentário:** '+'`'+html.unescape(dicionario['c'])+'`'+'\n\n**Link:** '+'`'+dicionario['link']+'`')

		embed.set_thumbnail(url=pfp.url.replace('small.jpg', 'big.jpg'))

		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'https://pbs.twimg.com/profile_images/818181506216628225/EkeBaVUa_400x400.jpg')

		return await bot.send_message(ctx.message.channel,'<@'+ctx.message.author.id+'>', embed=embed )
	except:
		return await bot.send_message(ctx.message.channel, '<@'+ctx.message.author.id+'>' + 'Deu erro :weary:')


@bot.command(pass_context=True)
async def dolar(ctx):
	try:
		resultado = dolar_func()

		embed = discord.Embed(
			title = 'Preço do dolar',
			color = 0x33cc33,
			description = '**Dolar comercial:** '+'`'+resultado['Dólar comercial']+'`'+'\n\n**Dolar turismo:** '+'`'+resultado['Dólar turismo']+'`'+
			'\n\n**Dolar ptax:** '+'`'+resultado['Dólar ptax']+'`'+'\n\n**Euro comercial:** '+'`'+resultado['Euro comercial']+'`'+'\n\n**Euro turismo:** '+'`'+resultado['Euro turismo']+'`'+'\n\n')

		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'http://www.agkcorretora.com.br/media/image/artigos/Frente-dolar-Agk-Corretora-grande.jpg')

		return await bot.send_message(ctx.message.channel, embed=embed)
	except:
		return await bot.send_message(ctx.message.channel, '<@'+ctx.message.author.id+'>' + 'Deu erro :weary:')


@bot.command(pass_context=True)
async def bitcoin(ctx):
	try:
		embed = discord.Embed(
			title = 'Valor do bitcoin',
			color = 0xffff00,
			description = '**'+bitcoin_func()+'**')

		embed.set_footer(
			text = 'ᵗᵉʳʳˡᵇˡᵉ on the beat',
			icon_url = 'http://s2.glbimg.com/HEbW5ZxGZNs7UJeMNs6Pp5m2EKQ=/0x600/s.glbimg.com/po/tt2/f/original/2016/03/22/bitcoin-btc-symbol-d75950754.png')

		return await bot.send_message(ctx.message.channel, embed=embed)
	except:
		return await bot.send_message(ctx.message.channel, '<@'+ctx.message.author.id+'>' + 'Deu erro :weary:')


@bot.command(pass_context=True)
async def tocar(ctx, *, musica):
	try:
		channel = ctx.message.author.voice_channel
		connect_instance = await bot.join_voice_channel(channel)
		musica_escolhida = pesquisar(musica)
		player = await connect_instance.create_ytdl_player('https://www.youtube.com' + musica_escolhida['song'])
		player.start()
		await bot.send_message(ctx.message.channel,'**A tocar:** {}\n\n'.format('https://www.youtube.com' + musica_escolhida['song']))
		if player.is_done():
			player.stop()
			for canal in bot.voice_clients:
				if canal.server == ctx.message.server:
					await canal.disconnect()
		else:
			pass
	except discord.errors.InvalidArgument:
		return await bot.send_message(ctx.message.channel, 'Primeiro tu tem que entra no canal de voz carai')


@bot.command(pass_context=True)
async def sair(ctx):
	for canal in bot.voice_clients:
			if canal.server == ctx.message.server:
				await canal.disconnect()
	return await bot.send_message(ctx.message.channel, 'Eu não to conectada a canal nenhum carai')


bot.run(TOKEN) if TOKEN else print('Token bot not loaded in the environment variables!')
