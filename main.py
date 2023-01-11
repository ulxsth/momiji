import discord

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

token: str
with open('token.txt') as f:
    token = f.read()

@client.event
async def on_ready():
    print('Momiji ONLINE')

@client.event
async def on_message(message):
    if "もみじ" in message.content:
        await message.channel.send('💕')

client.run(token)