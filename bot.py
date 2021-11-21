import random
import aiohttp
import asyncio
import logging
import gc
import sys
import random
import re
import aiohttp
import discord
from discord.ext import commands

f=open("clientid.txt", "r")
if f.mode == 'r':
    clientid = f.read()

f=open("clientsecret.txt", "r")
if f.mode == 'r':
    clientsec = f.read()

Client = discord.Client()
#bot = commands.Bot(command_prefix = ";")
log = logging.getLogger('LOG')
bot = commands.Bot(command_prefix=';', description="Bot for the WWF UZH ersti Discord, Author: Mert Erol")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(';help for a list of Commands'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='help : list of commands available.')
    embed.add_field(name=';ping', value='Returns bot respond time in milliseconds', inline=False)
    await ctx.send(embed = embed)

with open("TOKEN.txt") as f:
  token = f.read()


bot.run(token)
