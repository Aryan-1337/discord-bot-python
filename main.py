# IMPORTS
import nextcord
from nextcord.ext import commands
import os

# TOKEN AND PREFIX
TOKEN = os.getenv('TOKEN')
PREFIX = "."

# BOT
intents = nextcord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix = PREFIX, case_insensitive = True, help_command = None, intents = intents)

# BOT EVENT
@client.event
async def on_ready():
    print(f"Logged In As {client.user}")

# PING COMMAND
@client.command(aliases=['latency'])
async def ping(ctx):
    await ctx.reply(f"**My Ping Is: `{round(client.latency * 1000)}` Ms.**")

client.run(TOKEN)