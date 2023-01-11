import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

token: str
with open('token.txt') as f:
    token = f.read()

@client.event
async def on_ready():
    print('Momiji ONLINE')

client.run(token)