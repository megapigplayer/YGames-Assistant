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
**!help** - this command.
**!discord** - the discord server of the bot owner. 
**!youtube** - the youtube channel of the bot owner. 

__General Commands:__
**!avataricon @TAG** - give the avatar icon of who you tag. 
**!servericon** - the server icon.
**!question [a question] - the bot answer to your questions.

__Staff Commands:__
**!kick @TAG** - kick member from the server.
**!ban @TAG** - ban member from the server.
""")

@Client.command(pass_context=True)
async def question(ctx):

	possible_responses = ["לא", "כן", "אני לא בטוח, תשאל שוב אולי אני יחליט"]

	current_response = random.choice(possible_responses)

	await Client.say(current_response)

@Client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.kick_members or ctx.message.author.id == '194151340090327041':
       await Client.kick(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Kicked!", description="**{0}** was kick by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant kick this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

@Client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
       await Client.ban(userName)
       await Client.add_roles(member, role)
       embed=discord.Embed(title="User Baned!", description="**{0}** was ban by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
    else:
        embed=discord.Embed(title="You cant ban this user!", description="You don't have permission to use this command.", color=0xff00f6)
        await Client.say(embed=embed)

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
