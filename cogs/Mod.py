import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions


with open("config.json","r") as emojis:
    emoji = json.load(emojis)

    tick = emoji["tick"]
    cross = emoji["cross"]
    ban = emoji["ban"]
    kick = emoji["kick"]
    user = emoji["user"]
    reason = emoji["reason"]


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    
    @commands.command(name="kick")
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        if member == None:
            await ctx.reply(f"**{cross} | Please Provide Valid Member To Kick.**")

            mod = f"By {ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) | With Reason: {reason}"

            embed = nextcord.Embed(color=000000, title=f"{kick} | Member Kicked", description=f"**{tick} | Successfully Kicked {member.mention}, Here Are More Info")
            embed.add_field(name="Moderator:", value=f"{ctx.author.mention} | {ctx.author.id}", inline=False)
            embed.add_field(name="Reason:", value=f"{reason}", inline=False)

            await member.kick(reason=mod)

    

def setup(bot):
    bot.add_cog(Mod(bot))
