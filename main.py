import discord
import chess

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)

is_playing_chess = False

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

    # chess
    elif content == '/chess':
        is_playing_chess = True
        board_state = chess.START_BOARD_STATE
        board_state_text = chess.create_board_state_text(board_state)
        await channel.send('☕')
        await channel.send(board_state_text)

client.run(token)
