from random import randint as r
from discord.ext import commands

class Game:
    @staticmethod
    def roll_dice():
        return r(0,6)

class Oyunlar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.activities = {}

    @commands.command()
    async def merhaba(self,ctx):
        await ctx.send("Merhaba!")

    @commands.command()
    async def change_status(self, ctx, activity, *, text):
        self.bind_text(text)
        await self.bot.change_presence(**self.activities.get(activity))

    def bind_text(self, text, url=""):
        self.activities = {
            "1":{"activity":discord.Game(name=text)},
            "2": {"activity": discord.Activity(type=discord.ActivityType.listening, name=text)},
            "3": {"activity": discord.Activity(type=discord.ActivityType.watching, name=text)},
            "4": {"activity": discord.Game(name=text)},

        }



