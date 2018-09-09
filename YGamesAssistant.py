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
    await Client.change_status(game=discord.Game(name="!help | MegaMineBot"))
	
@Client.command(pass_context=True, no_pm=True)
async def servericon(ctx):
    """Guild Icon"""
    await Client.reply("{}".format(ctx.message.server.icon_url))

@Client.command(pass_context=True, no_pm=True)
async def membericon(ctx, member: discord.Member):
    """User Avatar"""
    await Client.reply("{}".format(member.avatar_url))

@Client.command()
async def say(output):
    await Client.say(output)
	
@Client.command()
async def help():
        embed = discord.Embed(title="Main Help עזרה ראשית", description="""

""", color=0xe88af4)
        await Client.say(embed=embed)

	
Client.run(os.getenv("TOKEN"))
