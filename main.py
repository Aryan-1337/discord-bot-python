import discord
import os
from discord.ext import commands
import tracemalloc

tracemalloc.start()

TOKEN = os.getenv('TOKEN')
PREFIX = '.'

intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix = PREFIX, intents = intents, case_insesitive = True, help_command = None)

@client.event
async def on_ready():
  print(f"Successfully Logged In As {client.user}")
  

@client.command(aliases=['latency'])
async def ping(ctx):
  await ctx.reply(f"**My Ping Is `{round(client.latency * 1000)}` Ms.**")
  
  
client.run(TOKEN)
