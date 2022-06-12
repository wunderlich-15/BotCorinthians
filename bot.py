import os
from decouple import config
from email import utils
from attr import fields
from click import pass_context
import discord
from discord.ext import commands
from GoogleNews import GoogleNews
from datetime import *
import random

prefix = '!'
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print('tamo pronto carai bora')
    await client.change_presence(activity=discord.Game(name=f"!comandos"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "palmeiras" in message.content:
        await message.channel.send(f'Vai se fuder palmeirense safado{message.author.mention}')
    if "Palmeiras" in message.content:
        await message.channel.send(f'Vai se fuder palmeirense safado{message.author.mention}')
    if "verdao" in message.content:
        await message.channel.send(f'Time merda esse ai hein mano KKKKKKKKKKKKKKK{message.author.mention}')
    if "Verdao" in message.content:
        await message.channel.send(f'KKKKKKKKKKKKKK time bosta{message.author.mention}')
    if "Verdão" in message.content:
        await message.channel.send(f'verdão teu cu na minha mão{message.author.mention}')
    if "verdão" in message.content:
        await message.channel.send(f'verdão teu cu na minha mão{message.author.mention}')
    if "trikas" in message.content:
        await message.channel.send(f'ih ala o cara é trikasKKKKKKKKKKKK{message.author.mention} fudido')
    if "Trikas" in message.content:
        await message.channel.send(f'ih ala o cara é trikasKKKKKKKKKKKK{message.author.mention} fudido')
    if "São Paulo" in message.content:
        await message.channel.send(f'KKKKKKKKKKK time de fudido esse ai{message.author.mention}')
    if "Santos" in message.content:
        await message.channel.send(f'time falido esse ai hein {message.author.mention} KKKKKKKKKKKKKKK')
    if "sao paulo" in message.content:
        await message.channel.send(f'KKKKKKKKKKK time de fudido esse ai{message.author.mention}')
    if "são paulo" in message.content:
        await message.channel.send(f'KKKKKKKKKKK time de fudido esse ai{message.author.mention}')
    if "santos" in message.content:
        await message.channel.send(f'time falido esse ai hein {message.author.mention} KKKKKKKKKKKKKKK')
    if "peixe" in message.content:
        await message.channel.send(f'ih ala o time de pobre{message.author.mention} KKKKKKKKKKKKKKK')
    if "Peixão" in message.content:
        await message.channel.send(f'ultimo torcedor desse ai morreu em 1984 {message.author.mention} KKKKKKKKKKKKKKK')

    await client.process_commands(message)

#Oia os comando aqui:
googlenews = GoogleNews()

@client.command()
async def comandos(ctx):
    url_image = "https://i.pinimg.com/originals/e8/1e/0b/e81e0bcf99242191d4dd7a89758615da.jpg"
    embed = discord.Embed(
        content = 'opa pra já carai',
        title = 'Comandos',
        description ='Saca os comando do paikkkkkkkk',
        colour = discord.Colour.red()

    )
    embed.add_field(name="!salve", value="Vou te mandar um salve a qualquer Hora do dia", inline=True)
    embed.add_field(name="!xingo", value="Use o comando e marque alguém pra eu ta xingando o cuzão", inline=False)
    embed.add_field(name="!hino", value="Entre numa call e use o comando pra escutar o belo hino do timão", inline=False)
    embed.add_field(name= "!sair", value="Se quiser parar o hino antes da hora só usar esse aqui", inline=False)
    embed.add_field(name="!ultimosjogos", value="Use para ver os resultados dos ultimos jogos do timão", inline=False)
    embed.add_field(name="!proximosjogos", value="Quase a mesma coisa do de cima mas pra ver os proximos né porra", inline=False)
    embed.add_field(name="!placaraovivo", value="Pra ver o placar ao vivo se tiver rolando jogo do campeão dos       campeões", inline=False)
    embed.add_field(name="!noticias", value="Pra ver as ultimas noticias do nosso gigante Corinthians", inline=False)
    embed.add_field(name="!comandos", value="Não preciso nem falar né porra", inline=False)
    embed.add_field(name="!convite", value="Me adiciona no seu servidor parça", inline=False)
    embed.add_field(name="!criador", value="As rede social do noia que me crio", inline=False)
    embed.set_footer(text="sepa vai ter comando novo mais pra frente meu criador é meio vagabundo")
    embed.set_thumbnail(url = url_image)
    await ctx.send(embed = embed)
@client.command()
async def xingo(ctx, membro:discord.Member):
        inicio = ['Vai toma no cu ', 'Vai se Fuder ', 'Vai pra casa do caralho ', 'Me mama ', 'Me da uma sugada ', 'Pobre ']
        meio = ['Palmeirense ', 'Santista ', 'trikasKKKKKKKKKKK ', 'Flamenguista ', 'Pobre ', 'esquisito ']
        fim = ['De merda ', 'Arrombado ', 'Chifrudo ', 'Corno ', 'Pobre ', 'Filho da puta ', 'Nerdola ', 'Fudido '] 
        await ctx.send(f'{random.choice(inicio)}{random.choice(meio)}{random.choice(fim)}{membro.mention}')

@client.command(pass_context=True)
async def hino(ctx):
    try:
        canal = ctx.author.voice.channel
        await ctx.channel.send(f'{ctx.author.mention}: - O Cascão solta o Hino do Curintia')
        await canal.connect()
        voice = discord.VoiceClient = discord.utils.get(client.voice_clients)
        audio_source = discord.FFmpegPCMAudio('hino.mp3')
        voice.play(audio_source, after=None), print('Deus é Bom o tempo todo')
    except:
        await ctx.channel.send(f'Cê não tá em nenhum canal moscão do carai {ctx.author.mention}')

@client.command()
async def sair(ctx):
    try:    
        voice = discord.utils.get(client.voice_clients)
        if voice.is_connected():
            await voice.disconnect()
            await ctx.channel.send('Tchau seus oreiudo')
    except:
        await ctx.channel.send(f'Já sai do call mano ta chapando carai {ctx.author.mention}?')

@client.command()
async def convite(ctx):
    await ctx.channel.send('Me adiciona la no seu server mano pprt n vai se arrepende')
    await ctx.channel.send('https://discord.com/api/oauth2/authorize?client_id=952333732608618527&permissions=431644736576&scope=bot')

@client.command()
async def criador(ctx):
    criador_tumb = "https://i.pinimg.com/474x/fe/d5/e9/fed5e9b4813f101f2d8dfc68283a07bc.jpg"
    embed = discord.Embed(
        title ='Segue meu criador ae mano',
        description = 'mlk é gente fina',
        color = discord.Colour.red()
    )
    embed.add_field(name='Twitter:', value='https://twitter.com/Wunderlich_', inline=False),
    embed.add_field(name='GitHub:', value='https://github.com/wunderlich-15', inline=False),
    embed.add_field(name='Insta:', value='https://instagram.com/guilhermewunderlich', inline=False)
    embed.set_thumbnail(url=criador_tumb)
    await ctx.channel.send(embed = embed)

@client.command()
async def salve(ctx):
    hora = datetime.now()
    if hora.hour >= 5 and hora.hour < 12:
        await ctx.channel.send(f'Bom dia lindão fé em Deus que vai da td certo hj VAI TIMÃO {ctx.author.mention}')
    elif hora.hour >= 12 and hora.hour < 18:
        await ctx.channel.send(f'Bom Tarde meu mano fé em Deus e VAI CORINTHIANS {ctx.author.mention}')
    elif hora.hour >= 18:
        await ctx.channel.send(f'Bom Noite cheiroso hr do descanso meu mano fé com fé e PRA CIMA DELES CORINTHIANS{ctx.author.mention}')
    elif hora.hour >= 1 and hora.hour < 5:
        await ctx.channel.send(f'Salve ai parça mai vai dormi mano tardão já e madrugada é só depressão slk {ctx.author.mention}')


@client.command()
async def ultimosjogos(ctx):
    await ctx.channel.send("Os Ultimos jogos do Timão")
    import crawler
    resultados = crawler.ultimos_jogos(cache = False)
    for resultado in resultados:
        partida = resultado.get('Partida')
        data = resultado.get('Data')
        placar = resultado.get('Placar')
        campeonato = resultado.get('Campeonato')

        embed = discord.Embed(
            title = f"{partida}", 
            description = f"""Placar: {placar}
                            Campeonato: {campeonato}""",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed = embed)

@client.command()
async def proximosjogos(ctx):
    await ctx.channel.send("Os próximos jogos do Timão")
    await ctx.channel.send("Correções futuras")
    import crawler
    resultados = crawler.proximos_jogos(cache = False)
    for resultado in resultados:
        partida = resultado.get('Partida')
        data = resultado.get('Data')
        campeonato = resultado.get('Campeonato')

        embed = discord.Embed(
            title = f"{partida}", 
            description = f"""Data: {data}
                            Campeonato: {campeonato}""",
            colour = discord.Colour.blue()
        )
        await ctx.send(embed = embed)

@client.command()
async def placaraovivo(ctx):
    import crawler
    resultados = crawler.buscar_jogo_por_time('Corinthians', cache = False)
    if not resultados:
        await ctx.channel.send("Não tem jogo rolando agora não mano")
    else:
        for resultado in resultados:
            partida = resultado.get('match')
            tempo = resultado.get('status')
            placar = resultado.get('scoreboard')
            campeonato = resultado.get('league')

            embed = discord.Embed(
                title = f"{partida}", 
                description = f"""Tempo de Jogo: {tempo}
                                Placar: {placar}
                                Campeonato: {campeonato}""",
                colour = discord.Colour.blue()
            )
            await ctx.send(embed = embed)

@client.command()
async def noticias(ctx):
    agr = date.today()
    td = timedelta(7)
    ontem= agr - td
    googlenews.setperiod('7d')
    googlenews.set_time_range(ontem.strftime('%m/%d/%y'), agr.strftime('%m/%d/%y'))
    googlenews.setlang('pt')
    googlenews.get_news('Corinthians')

    result = googlenews.get_links()
    await ctx.channel.send(f'As principais noticias do timão:')
    await ctx.channel.send(f'https://{result[0]}')
    await ctx.channel.send(f'https://{result[1]}')
    await ctx.channel.send(f'https://{result[2]}')
TOKEN = config("TOKEN_SECRETO")
client.run(TOKEN)