# IMPORTS
import nextcord
from nextcord.ext import commands
import os
from cogs.Misc import Misc

# TOKEN AND PREFIX
TOKEN = os.getenv('TOKEN')
PREFIX = "."

# BOT
intents = nextcord.Intents.all()
bot = nextcord.Client()
bot = commands.Bot(command_prefix = PREFIX, case_insensitive = True, help_command = None, intents = intents)

# BOT EVENT
@bot.event
async def on_ready():
    print(f"Logged In As {bot.user}")

# PING COMMAND
@bot.command(aliases=['latency'])
async def ping(ctx):
    await ctx.reply(f"**My Ping Is: `{round(bot.latency * 1000)}` Ms.**")

bot.run(TOKEN)