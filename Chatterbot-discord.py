import time as t
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("bot is ready")
    chat = client.get_channel(775230000542515232)
    await chat.send("I'm online  command lists, 1.hello, 2.what is the version, 3.who are you")


@client.event
async def on_message(message):
    if message.content == 'who are you':
        chat = client.get_channel(775230000542515232)
        await chat.send("a bot made by @incognito and I don't know what to do till now")
    
    elif message.content == 'what is the version':
        chat = client.get_channel(775230000542515232)
        await chat.send("version 1.0 beta")
    
    elif message.content == 'hello':
        chat = client.get_channel(775230000542515232)
        await chat.send("hi")

    elif message.content == 'hmmm':
        chat = client.get_channel(775230000542515232)
        await chat.send("hmmmmmmm")

    elif message.content == 'what':
        chat = client.get_channel(775230000542515232)
        await chat.send("what??")
    
    elif message.content == 'go offline':
        chat = client.get_channel(775230000542515232)
        await chat.send("shutting down system...")



client.run('my token here')



