import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('こんこよ〜!\nホロライブ6期生、holoXの〜…頭脳〜！\n博衣こよりだよ〜！')

def setup(bot):
    bot.add_cog(Main(bot))