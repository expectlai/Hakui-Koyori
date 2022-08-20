import discord
from discord.ext import commands
import json

with open("setting.json", "r", encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '&')

@bot.event
async def on_ready():
    print("Bot is online...OwO")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(1010436354137669662)
#     await channel.send(f'歡迎 {member.name} !')

# @bot.event
# async def on_member_remove(member):
#     channel = bot.get_channel(1010436354137669662)
#     await channel.send(f'{member.name} 已經悄悄地離開這個伺服器了... ;_;')

bot.run(jdata["TOKEN"])