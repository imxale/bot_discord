# -*- coding: utf-8 -*-
import os
import discord
import youtube_dl
import asyncio
import time
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord.errors import Forbidden
from playsound import playsound 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
commande_hello = os.getenv('commande_hello')
commande_bg = os.getenv('commande_bg')
commande_ban_anthony = os.getenv('commande_ban_anthony')
commande_ban_steven = os.getenv('commande_ban_steven')
commande_ban_nathan = os.getenv('commande_ban_nathan')
commande_gotaga = os.getenv('commande_gotaga')
commande_doigby = os.getenv('commande_doigby')
commande_haagrah = os.getenv('commande_haagrah')
client = discord.Client()

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("Je suis connecté")
    embed = discord.Embed(description="Je suis **connecté** mes turbo bg ! \nEssaye la commande ``?help`` pour en savoir plus", 
    colour=discord.Colour.purple())
    channel = bot.get_channel(773689379100033064)
    await channel.send(embed=embed)
    await bot.change_presence(activity=discord.Game(name="Des chiffres et des lettres"))

@bot.command()
async def tesbg(ctx, id):
    embed = discord.Embed(description=id+" t'es un **turbo bg** !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?tesbg'")

@bot.command(name='bg')
async def bg(ctx, help="Ton bot pref dit que t'es un turbo bg"):
    embed = discord.Embed(description="<@!" + format(ctx.message.author.id)+"> "+commande_bg, colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?bg'")

@bot.command()
async def ban(ctx, help="Affiche les boloss qui sont ban"):
    embed = discord.Embed(description="Malheureusement plus aucun bouf n'est ban !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?ban'")

@bot.command()
async def deli(ctx, help="C'est quoi deli ?"):
    embed = discord.Embed(description="<@!534721754162266132> le bilingue de ce discord\n``!deli``\n``!deily``\n``!dayly``", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?deli'")

@bot.command()
async def bastos(ctx):
    embed = discord.Embed(description="<@!205357566887329792> 'Le **zizou** du ban'\nTu es ``perma ban`` sale bouf, déjà **3** comptes de perma", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?bastos'")

@bot.command()
async def james(ctx):
    embed = discord.Embed(description="<@!254978500300111872> Premier ``perma ban`` pour toi,\nSur les traces du grand **Bastos**", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?james'")

@bot.command()
async def ernesto(ctx, help="C'est moi"):
    embed = discord.Embed(description=commande_hello, colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?ernesto'")

@bot.command()
async def chef(ctx, help="On a une cheffe"):
    embed = discord.Embed(description="Garde à vous <@!689169698419638357> is in the place !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?chef'")

@bot.command()
async def kebab(ctx, help="Petit kebab"):
    embed = discord.Embed(description="Keeeebaaaab\nun ptit kebab\nkebab kebab", colour=discord.Colour.purple())
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    await ctx.send(embed=embed)
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("C:/Bot_Discord/song/kebab.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(9)
        await vc.disconnect()
    else:
        await ctx.send("<@!" + format(ctx.message.author.id)+"> is not in a channel.")
    # Delete command after the audio is done playing.
    #await ctx.message.delete()
    print(format(ctx.author.name)+" à utilisé la commande '?kebab'")

@bot.command()
async def fusee(ctx, help="C'est ma fusée"):
    embed = discord.Embed(description="Ça c'est ma **fusée** enculé", colour=discord.Colour.purple())
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    await ctx.send(embed=embed)
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("C:/Bot_Discord/song/fusee.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(9)
        await vc.disconnect()
    else:
        await ctx.send("<@!" + format(ctx.message.author.id)+"> is not in a channel.")
    # Delete command after the audio is done playing.
    #await ctx.message.delete()
    print(format(ctx.author.name)+" à utilisé la commande '?fusee'")

@bot.command()
async def mbappe(ctx, help="C'est moi wsh"):
    embed = discord.Embed(description="C'est **Mbappé**, c'est **Mbappé**", colour=discord.Colour.purple())
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    await ctx.send(embed=embed)
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("C:/Bot_Discord/song/mbappe.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(10)
        await vc.disconnect()
    else:
        await ctx.send("<@!" + format(ctx.message.author.id)+"> is not in a channel.")
    # Delete command after the audio is done playing.
    #await ctx.message.delete()
    print(format(ctx.author.name)+" à utilisé la commande '?mbappe'")

@bot.command()
async def tki(ctx, help="Jiraya ?"):
    embed = discord.Embed(description="**PTDR** t ki ?", colour=discord.Colour.purple())
    voice_channel = ctx.author.voice.channel
    await ctx.send(embed=embed)
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("C:/Bot_Discord/song/tki.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(3)
        await vc.disconnect()
    else:
        await ctx.send("<@!" + format(ctx.message.author.id)+"> is not in a channel.")
    # Delete command after the audio is done playing.
    #await ctx.message.delete()
    print(format(ctx.author.name)+" à utilisé la commande '?tki'")

@bot.command()
async def haagrah(ctx, help="Fait moi dire haagrah"):
    embed = discord.Embed(description=commande_haagrah, colour=discord.Colour.purple())
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    await ctx.send(embed=embed)
    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("C:/Bot_Discord/song/haagrah.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            time.sleep(8)
        await vc.disconnect()
    else:
        await ctx.send("<@!" + format(ctx.message.author.id)+"> is not in a channel.")
    # Delete command after the audio is done playing.
    #await ctx.message.delete()
    print(format(ctx.author.name)+" à utilisé la commande '?haagrah'")

@bot.command()
async def doigby(ctx, help="Je te lance l'hymne"):
    #print("play")
    client = ctx.guild.voice_client
    embed = discord.Embed(description=commande_doigby, colour=discord.Colour.purple())

    if client and client.channel:
        video = Video("https://www.youtube.com/watch?v=aaEgiYVEjX4")
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video("https://www.youtube.com/watch?v=aaEgiYVEjX4")
        musics[ctx.guild] = []
        client = await channel.connect()
        #await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?doigby'")

@bot.command()
async def gotaga(ctx, help="Je travaille"):
    client = ctx.guild.voice_client
    embed = discord.Embed(description=commande_gotaga, colour=discord.Colour.purple())
    if client and client.channel:
        video = Video("https://www.youtube.com/watch?v=hhuvQGoGNWw")
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video("https://www.youtube.com/watch?v=hhuvQGoGNWw")
        musics[ctx.guild] = []
        client = await channel.connect()
        #await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?gotaga'")

musics = {}
ytdl = youtube_dl.YoutubeDL()

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def leave(ctx, help="Fait moi quitté le vocal"):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def skip(ctx, help="Je te skip le prochain son mon frérot"):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 0"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)

@bot.command()
async def play(ctx, url, help="Je lance le son que tu veux avec un lien YT"):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)

#We delete default help command
bot.remove_command("help")

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="La liste de mes commandes frérot", colour=discord.Colour.purple())
    embed.set_author(name='Autor : Amiral - imxale', url="https://github.com/imxale")
    embed.add_field(name='``?bg``', value="Ton bot pref dit que t'es un turbo bg", inline=False)
    embed.add_field(name='``?tesbg [member]``', value="Dit à ton frérot que c'est un turbo bg", inline=False)
    embed.add_field(name='``?chef``', value="On a une cheffe", inline=False)
    embed.add_field(name='``?ban``', value="Affiche les boloss qui sont ban", inline=False)
    embed.add_field(name='``?deli``', value="C'est quoi deli ?", inline=False)
    embed.add_field(name='``?bastos``', value="Le zizou du ban", inline=False)
    embed.add_field(name='``?james``', value="Un bouf du ban", inline=False)
    embed.add_field(name='``?ernesto``', value="Tu me connait pas ?", inline=False)
    embed.add_field(name='``?haagrah``', value="Fait moi dire haagrah", inline=False)
    embed.add_field(name='``?doigby``', value="Je te lance l'hymne du navire", inline=False)
    embed.add_field(name='``?gotaga``', value="Je travaille comme Gotaga", inline=False)
    embed.add_field(name='``?mbappe``', value="C'est moi wsh", inline=False)
    embed.add_field(name='``?fusee``', value="C'est ma fusée", inline=False)
    embed.add_field(name='``?tki``', value="PTDR t ki ?", inline=False)
    embed.add_field(name='``?kebab``', value="Qui veut un kebab ?", inline=False)
    embed.set_footer(text="Dont spam voices commands")
    await ctx.send(embed=embed)
    print(format(ctx.author.name)+" à utilisé la commande '?help'")

bot.run(TOKEN)