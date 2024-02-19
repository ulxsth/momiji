import discord
import chess

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
token: str
with open("token.txt", "r") as f:
    token = f.read()

board = None

@client.event
async def on_ready():
    print('Momiji ONLINE')


@client.event
async def on_message(message):
    content = message.content
    channel = message.channel
    sender = message.author.name
    print(f"{sender}: {content}")

    if "もみじ" in content:
        await channel.send('💕')

client.run(token)
