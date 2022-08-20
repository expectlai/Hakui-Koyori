import discord
from discord.ext import commands
import json
import random
import os

with open("setting.json", "r", encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix = '&')

@bot.event
async def on_ready():
    print("Bot is online...OwO")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')
# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(1010436354137669662)
#     await channel.send(f'歡迎 {member.name} !')

# @bot.event
# async def on_member_remove(member):
#     channel = bot.get_channel(1010436354137669662)
#     await channel.send(f'{member.name} 已經悄悄地離開這個伺服器了... ;_;')
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])