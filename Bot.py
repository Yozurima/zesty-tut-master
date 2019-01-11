import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Thankyou for Using this bot")
    await client.change_presece(game=discord.Game(name="League"))
@client.event
async def on_message(message):
    if message.content.startswith('!Hello')
        msg = 'Heya {o.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!bye')
        msg = 'Goodbye {o.author.mention} Hope To See You Again Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)
client.run(os.getenv('TOKEN'))
