# -*- coding: utf-8 -*-
import os
import discord
import youtube_dl
import asyncio
import time
import discord
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
commande_oceane1 = os.getenv('commande_oceane1')
commande_oceane2 = os.getenv('commande_oceane2')
client = discord.Client()

bot = commands.Bot(command_prefix='?')

#client = commands.Bot(command_prefix='!')
"""
@client.event
async def on_message(message):
    if message.content == '!ernesto':
        await message.channel.send(commande_hello)
    if message.content == '!bg':
        await message.channel.send("<@!" + format(message.author.id)+"> "+commande_bg)
    if message.content == "!ban":
        await message.channel.send("<@!534721754162266132> "+commande_ban_anthony)
    if message.content == "!gotaga":
        await message.channel.send(commande_gotaga)
"""
"""
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = ctx.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

"""
"""
@bot.command()
async def ernestohelp(ctx):
    await ctx.send("Turbo bg "+"<@!" + format(ctx.message.author.id)+"> essaye les commandes : \n!bg \n!tesbg '@...' \n!ban \n!doigby \n!gotaga \n!ernesto \n!haagrah \n!chef")
"""
@bot.command()
async def tesbg(ctx, id):
    embed = discord.Embed(description=id+" t'es un **turbo bg** !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
"""
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
"""
@bot.command(name='bg')
async def bg(ctx, help="Ton bot pref dit que t'es un turbo bg"):
    embed = discord.Embed(description="<@!" + format(ctx.message.author.id)+"> "+commande_bg, colour=discord.Colour.purple())
        #colour = discord.Colour.purple())
    #embed.add_field(name="<@!" + format(ctx.message.author.id)+"> "+commande_bg,value="")
    await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, help="Affiche les boloss qui sont ban"):
    embed = discord.Embed(description="Malheureusement plus aucun bouf n'est ban !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command()
async def deli(ctx, help="C'est quoi deli"):
    embed = discord.Embed(description="<@!534721754162266132> le bilingue de ce discord\n!deli\n!deily\n!dayly", colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command()
async def bastos(ctx):
    embed = discord.Embed(description="<@!205357566887329792> 'Le **zizou** du ban'\nTu es ``perma ban`` sale bouf, déjà **3** comptes de perma", colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command()
async def james(ctx):
    embed = discord.Embed(description="<@!254978500300111872> Premier ``perma ban`` pour toi,\nSur les traces du grand **Bastos**", colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command()
async def ernesto(ctx, help="C'est moi"):
    embed = discord.Embed(description=commande_hello, colour=discord.Colour.purple())
    await ctx.send(embed=embed)

@bot.command()
async def chef(ctx, help="On a une cheffe"):
    embed = discord.Embed(description="Garde à vous <@!689169698419638357> is in the place !", colour=discord.Colour.purple())
    await ctx.send(embed=embed)
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

"""
@bot.command()
async def haagrah(ctx):
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video("https://www.youtube.com/watch?v=uBPeAp7gxOQ")
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video("https://www.youtube.com/watch?v=uBPeAp7gxOQ")
        musics[ctx.guild] = []
        client = await channel.connect()
        #await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)
    await ctx.send(commande_haagrah)
"""
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
"""
@bot.command()
async def test(ctx):
    channel = bot.get_channel(787749067106156584)
    await channel.send("https://www.youtube.com/watch?v=aaEgiYVEjX4")
"""
@bot.command()
async def gotaga(ctx, help="Je travaille"):
    #print("play")
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

musics = {}
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("Ready")
    embed = discord.Embed(description="Je suis **connecté** mes turbo bg ! \nEssaye la commande ``?help`` pour en savoir plus", colour=discord.Colour.purple())
    channel = bot.get_channel(773689379100033064)
    #voice_channel=bot.get_channel(787438295012343808)
    #vc = await voice_channel.connect()
    await channel.send(embed=embed)
    await bot.change_presence(activity=discord.Game(name="Des chiffres et des lettres"))

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
"""
@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()

"""
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

class bcolors:
    green = '\033[92m' #GREEN
    yellow = '\033[93m' #YELLOW
    red = '\033[91m' #RED
    reset = '\033[0m' #RESET COLOR

import colorama
from colorama import Fore
from colorama import Style

#We delete default help command
bot.remove_command("help")
#Embeded help with list and details of commands
@bot.command(pass_context=True)
async def help(ctx):
    #embed = discord.Embed(
        #colour = discord.Colour.purple())
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
    #embed.add_field(name="**Autor :**", value="<@!286485781688745985>")
    embed.set_footer(text="Dont spam voices commands")
    await ctx.send(embed=embed)
    #print(f"{bcolors.green}?bg{bcolors.reset}")

#client.run(TOKEN)
bot.run(TOKEN)

