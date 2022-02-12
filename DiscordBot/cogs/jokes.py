import asyncio
import discord
from discord.ext import commands
from random import *

yoMumma = ['Yo momma is so stupid she brought a spoon to the super bowl.']

dadJokes = ["3.14% of sailors are pi-rates."]

mixJokes = ["Q: What do you get if you cross cat with an elephant? A: A flat cat."]

knockknock = ["Knock, knock. Who’s there? Luke. Luke who? Luke through the the peep hole and find out."]
              
              
class Jokes:
    """The bot's funny side"""

    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True, description="Tells a joke")
    async def joke(self, ctx):
        """Tells a joke"""
        channel = ctx.message.channel
        await self.bot.send_typing(channel)
        jokes = dadJokes+mixJokes+knockknock+yoMumma
        joke = choice(jokes)
        await self.bot.say(joke)
        
