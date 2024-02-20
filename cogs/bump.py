import asyncio
from discord.ext import commands

BUMP_COOLDOWN_MINUTE = 0.5


class BumpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == '/bump':
            await message.channel.send("Bump Detected 👀")
            await asyncio.sleep(BUMP_COOLDOWN_MINUTE * 60)
            await message.channel.send("Time to bump!")

        if message.content == '/dissoku up':
            await message.channel.send("Dissoku up detected 👀")
            await asyncio.sleep(BUMP_COOLDOWN_MINUTE * 60)
            await message.channel.send("Time to bump!")


async def setup(bot):
    await bot.add_cog(BumpCog(bot))
