import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class React(Cog_Extension):
    @commands.command()
    async def koyori(self, ctx):
        img = discord.File(f'.\\image\\img ({random.randint(1,150)}).jpg')
        await ctx.send(file = img)
    @commands.command()
    async def avatar(self, ctx):
        img = discord.File(f'.\\yandere.jpg')
        await ctx.send(file = img)
    @commands.command()
    async def say(self, ctx, args):
        await ctx.send(args)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(React(bot))