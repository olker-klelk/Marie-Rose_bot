import discord
from discord.ext import commands
bot=commands.Bot(command_prefix='$')
@bot.event
async def on_read():
 print("Marie Rose Comeing!!")

@bot.event
async def in_member_join(member):
 print(f'[member] join')
 
@bot.command()
async def comehere(ctx):
 await ctx.send("olkerklelk")

@bot.command()
async def howhandsome(ctx):
 await ctx.send("olkerklelk")

bot.run('NjQ1NDI3MDM0ODM4OTI1MzMy.XdDZxA.5i01dsq3sekam8y8vbL3J5MiPbQ')
