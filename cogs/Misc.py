import nextcord
from nextcord.ext import commands

time_format = "%d/%m/%Y at %T %p"


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['ui', 'whois'])
    async def userinfo(self, ctx, member: nextcord.Member):
        if member == None:
            member = ctx.author

            rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
            roles = ", ".join(rolelist)

            hypesquad_class = str(member.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()

            hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])

            perms_string = ""
        for perm, true_false in roles.permissions:
            if true_false is True:
                perms_string += f"{perm}, "

            member = user
            usr = await client.fetch_user(member.id)
            if usr.banner:
                banner = usr.banner.url


            embed = nextcord.Embed(color=000000, title=f"{member.name}#{member.discriminator}'s Information", description=f"**__General information__**\n**Name :** {member.name}\n**ID :** {member.id}\n**Nickname :** {member.nickname}\n**Bot? :** {member.bot}\n**Badges :** {hypesquad_class} **Server Joined :** {member.joined_at.strftime(time_format)}\n**Account Created :** {member.created_at.strftime(time_format)}\n\n**__Role Info__**\n**Highest Role :** {member.top_role}\n**Roles :** {roles}\n**Color :** {member.color}\n\n**__Key Permissions__**\n{perms_string}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_image(url=banner)
            await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Misc(bot))
