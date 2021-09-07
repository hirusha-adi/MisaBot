import os, json
import discord
from platform import python_version
from time import time
from datetime import timedelta
from discord.ext import commands

class Startup(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        # Bot starting time, we find the time delta of this to send the uptime
        self.start_time = None

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
        self.bot_status = botconfigdata["bot-status-message"]


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.client.user.name}')
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {python_version()}')
        global start_time
        start_time = time()

        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{self.bot_status}"))
        print('Bot is ready!')
    

    @commands.command()
    async def uptime(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        
        try:
            current_time = time()
            difference = int(round(current_time - start_time))
            text = str(timedelta(seconds=difference))
            embed=discord.Embed(color=0xff0000)
            embed.set_thumbnail(url="https://tenor.com/view/death-note-misa-amane-begging-i-know-gif-22016751")
            embed.add_field(name="The bot was online for: ", value=f":alarm_clock: {text}", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="MisaBot", icon_url="https://tenor.com/view/misa-amane-misa-death-note-shinigami-eyes-anime-gif-16711123")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    
    @commands.command()
    async def status(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)

        try:
            current_time = time()
            difference = int(round(current_time - start_time))
            text = str(timedelta(seconds=difference))

            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Announcements", value=f"``` -MisaBot {self.bot_current_version}- Hello! I am the moderation bot made for TeamSDS. Use {self.bot_prefix}help to see all the commands! You can join the teamSDS server by this link: teamsds.net/discord ```", inline=False)
            embed.add_field(name="Servers", value=f"{len(self.client.guilds)}", inline=True)
            embed.add_field(name="Uptime", value=f"{text}", inline=True)
            embed.add_field(name="Version", value=f"{self.bot_current_version}", inline=True)
            embed.add_field(name="Source Code", value="https://github.com/hirusha-adi/MisaBot", inline=True)
            embed.add_field(name="Creator", value=f"{self.bot_creator_name}", inline=True)
            embed.add_field(name="Errors", value="``` There are no known bugs so far  ```", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)
        
        except Exception as e:
            embed3=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed3.set_author(name="MisaBot", icon_url="https://tenor.com/view/misa-amane-misa-death-note-shinigami-eyes-anime-gif-16711123")
            embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed3.add_field(name="Error:", value=f"{e}", inline=False)
            embed3.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed3)
    
    @commands.command() 
    async def ping(self, ctx):
        loading_message = await ctx.send(embed=self.please_wait_emb)
        try:
            embed=discord.Embed(title="Response Time", color=0xff0000)
            embed.set_author(name="MisaBot", icon_url="https://tenor.com/view/misa-amane-misa-death-note-shinigami-eyes-anime-gif-16711123")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
            embed.add_field(name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed)

        except Exception as e:
            embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
            embed2.set_author(name="MisaBot", icon_url="https://tenor.com/view/misa-amane-misa-death-note-shinigami-eyes-anime-gif-16711123")
            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed2.add_field(name="Error:", value=f"{e}", inline=False)
            embed2.set_footer(text=f"Requested by {ctx.author.name}")
            await loading_message.delete()
            await ctx.send(embed=embed2)
            





def setup(client: commands.Bot):
    client.add_cog(Startup(client))

