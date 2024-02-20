import asyncio
from datetime import datetime, timedelta  # 修正: datetime と timedelta を直接インポート
from discord.ext import commands
from zoneinfo import ZoneInfo

jst = ZoneInfo("Asia/Tokyo")

BUMP_COOLDOWN_MINUTE = 120
DISSOKU_COOLDOWN_MINUTE = 60

bump_message = "Time to /bump !"
dissoku_message = "Time to /dissoku up !"


class BumpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == '/bump':
            # 修正: datetime.datetime から datetime へ
            next_bump_time = datetime.now(
                jst) + timedelta(minutes=BUMP_COOLDOWN_MINUTE)
            await message.channel.send(f"次の /bump は {next_bump_time.strftime('%H:%M')} です ☕")

            await asyncio.sleep(BUMP_COOLDOWN_MINUTE * 60)
            await message.channel.send(bump_message)  # 変数を使用

        if message.content == '/dissoku up':
            # 修正: datetime.datetime から datetime へ
            next_bump_time = datetime.now(
                jst) + timedelta(minutes=DISSOKU_COOLDOWN_MINUTE)
            await message.channel.send(f"次の /dissoku up は {next_bump_time.strftime('%H:%M')} です ☕")

            await asyncio.sleep(DISSOKU_COOLDOWN_MINUTE * 60)
            await message.channel.send(dissoku_message)  # 変数を使用


async def setup(bot):
    await bot.add_cog(BumpCog(bot))
