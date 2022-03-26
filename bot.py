import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>Bot is online<<")



bot.run("OTU3MjMzNTk3MDk2NTU0NTE2.Yj7zQg.YGIIxwwvFCpVp7yVLBKY99aOkBw")
