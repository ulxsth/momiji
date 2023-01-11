import discord
import chess

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
    content = message.content
    channel = message.channel
    
    if "もみじ" in content:
        await channel.send('💕')
        
    elif content == '/chess':
        board_state_text = chess.get_board_state_text(chess.START_BOARD_STATE)
        await channel.send(board_state_text)

client.run(token)