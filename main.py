
from dotenv import load_dotenv
from discord.ext import commands

import os
import discord

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.all())
        self.load_extension_directories = ["cogs"]

    async def setup_hook(self):
        for load_extension_directory in self.load_extension_directories:
            for root, dirs, files in os.walk(load_extension_directory):
                for file in files:
                    if file.endswith('.py'):
                        load_file = os.path.join(root, file).replace('/', '.').replace('\\', '.')[:-3]
                        await self.load_extension(load_file)
                        print(load_file)

        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged in as {bot.user.name}')

bot = Bot()
bot.run(os.getenv('BOT_TOKEN'))
