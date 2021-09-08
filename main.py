import os, discord
from discord.ext import commands
from json import load as jsonload

botconfigdata = jsonload(open("config.json", "r"))
bot_prefix = botconfigdata["msg-prefix"]
bot_token = botconfigdata["bot-token"]
bot_owner_id = botconfigdata["ownerid"]

client = commands.Bot(command_prefix=bot_prefix)

@client.command()
async def load(ctx, extension):
    if ctx.author.id == bot_owner_id:
        client.load_extension(f'cogs.{extension}')
    else:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="MisaBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/885143153550688266/1234.gif")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed2)

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == bot_owner_id:
        client.unload_extension(f'cogs.{extension}')
    else:
        embed2=discord.Embed(title=":red_square: Error!", description="The command was unable to run successfully! ", color=0xff0000)
        embed2.set_author(name="MisaBot", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/885143153550688266/1234.gif")
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
        embed2.add_field(name="Error:", value=f"```You don't have permission to use this command!```", inline=False)
        embed2.set_footer(text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed2)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bot_token)