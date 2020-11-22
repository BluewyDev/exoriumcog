import discord
import config

from discord.ext import commands # you don't need to import discord.ext again, especially when you're not using it.
from outsources import functions


class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):  # functions will always have "self" as first positional argument in cogs, then ctx and then whatever stuff you want 
        em = discord.Embed(color=config.color)
        em.add_field(name='ping', value=f'{self.bot.latency * 1000} ms')
        await ctx.send(embed=em)

    @commands.command()
    async def test(self, ctx):
        em = discord.Embed(color-config.color)
        em.add_field(name='test', value='affirmative')
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Botinfo(bot))
