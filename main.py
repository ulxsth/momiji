
from dotenv import load_dotenv
from discord.ext import commands

import os
import discord

load_dotenv()

class Bot(commands.bot):
    def __init__(self):
        super.__init__(command_prefix="/", intents=discord.Intents.all())
        self.load_extension_directories = ['cogs']

    @commands.command()
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.display_name}")

    async def setup(bot):
        bot.add_command(hello)

bot = Bot()
bot.run(os.getenv('BOT_TOKEN'))
