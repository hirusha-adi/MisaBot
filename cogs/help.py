import os, json
import discord
from discord.ext import commands

class HelpCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Bot starting time, we find the time delta of this to send the uptime
        self.start_time = None
        self.client.remove_command('help')

        # This is the please-wait/Loading embed
        self.please_wait_emb = discord.Embed(title="Please Wait", description="``` Processing Your Request ```", color=0xff0000)
        self.please_wait_emb.set_author(name="MisaBot")
        self.please_wait_emb.set_thumbnail(url="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif")
        self.please_wait_emb.set_footer(text="Bot created by ZeaCeR#5641")

        # Bot Config Data from ../config.json
        botconfigdata = json.load(open("config.json", "r"))
        self.bot_creator_name = botconfigdata["bot-creator-name"]
        self.bot_current_version = botconfigdata["bot-version"]
        self.bot_prefix = botconfigdata["msg-prefix"]

    @commands.command(aliases=['help'])
    async def Help(self, ctx):
        bp = self.bot_prefix
        embed=discord.Embed(title="help for MisaBot", color=0xff0000)
        embed.set_author(name="MisaBot", icon_url="https://tenor.com/view/misa-amane-misa-death-note-shinigami-eyes-anime-gif-16711123")
        embed.set_thumbnail(url="https://tenor.com/view/death-note-misa-amane-begging-i-know-gif-22016751")
        embed.add_field(name="Basic", value=f"`{bp}ping` \n`{bp}status` \n`{bp}uptime`", inline=False)
        embed.add_field(name="Moderation", value=f"`{bp}accdate [@user=optional]` \n`{bp}addrole [@user] [Role-Name]` \n`{bp}av [@user=optional]` \n`{bp}ban [@user] [reason]` \n`{bp}changeprefix [new-prefix]` \n`{bp}clean [amount]` \n`{bp}clear [number] [@user=optional]` \n`{bp}cnick [@user] [new-nickname]` \n`{bp}servericon` \n`{bp}infoserver` \n`{bp}kick [@user] [Reason=Optional]` \n`{bp}mute [@user] [reason='Reason not Provided']` \n`{bp}newav [@user=optional]` \n`{bp}newemoji [name] [link(below-256KB)] [filetype='png']` \n`{bp}nuke [@user] [reason='You have been nuked! Bye Bye loser']` \n`{bp}piethrow [@user] [reason=optional]` \n`{bp}removerole [@user] [role-name]` \n`{bp}shell_clear` \n`{bp}shell_info` \n`{bp}shell_run` \n`{bp}slap [@user] [reason='Reason is not given']` \n`{bp}slowmode [time]` \n`{bp}tempmute [@user] [time-number='3'] [time-unit='m'] [reason='No reason is provided']` \n`{bp}unban [user#id]` \n`{bp}unmute [@user]` \n`{bp}userinfo [@user=optional]`", inline=True)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)









def setup(client: commands.Bot):
    client.add_cog(HelpCommands(client))



