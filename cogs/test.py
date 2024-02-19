from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cog.listener()
    async def on_message(self, message):
        content = message.content
        channel = message.channel
        sender = message.author.name
        print(f"{sender}: {content}")

        if "もみじ" in content:
            await channel.send('💕')

    def setup(bot):
        bot.add_cog(TestCog(bot))
