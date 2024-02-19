
from dotenv import load_dotenv
from discord.ext import commands

import os
import discord

load_dotenv()

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

def load_cogs(bot):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog = filename[:-3]
            print(cog)
            bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

load_cogs(bot)
bot.run(os.getenv('BOT_TOKEN'))
