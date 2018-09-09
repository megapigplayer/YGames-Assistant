import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
import os
import time


Client = commands.Bot(command_prefix = "!")
Client.remove_command("help")
owner = ["Insert-Owner-ID"]

@Client.event
async def on_ready():
    print(".Bot Is ready!")
    await Client.change_status(game=discord.Game(name="!help <> YGamesAssistant"))
	
@Client.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await Client.reply("{}".format(ctx.message.server.icon_url))

@Client.command(pass_context=True, no_pm=True)
async def avataricon(ctx, member: discord.Member):
    """User Avatar"""
    await Client.reply("{}".format(member.avatar_url))

@Client.command()
async def say(output):
    await Client.say(output)
	
@Client.command()
async def help():
    await Client.say("""
**Bot prefix- !**
```YGames Assistant Commands list```
__Information Commands:__
!help - this command.
!discord - the discord server of the bot owner. 
!youtube - the youtube channel of the bot owner. 

__General Commands:__
!avataricon @TAG - give the avatar icon of who you tag. 
!servericon - the server icon.
""")

@Client.command()
async def youtube():
    await Client.say("""
```The Server Youtube Channel```
**Subscribe to the channel and do like to my videos!**
Link: https://www.youtube.com/channel/UCBaFupHLmyMWSQ4vLvOVPrA
""")

@Client.command()
async def discord():
    await Client.say("""
```My Discord Server```
**Join to the server today!**
Link: https://discord.gg/Fz5avXn
""")

Client.run(os.getenv("TOKEN"))
