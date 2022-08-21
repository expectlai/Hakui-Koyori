import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if '機率' in msg.content and msg.author != self.bot.user:
            await msg.channel.send(f'{random.randint(1,100)}%')

def setup(bot):
    bot.add_cog(Event(bot))