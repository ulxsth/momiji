import discord
import chess

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
token: str
with open("token.txt", "r") as f:
    token = f.read()

is_playing_chess = False

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
        global is_playing_chess
        is_playing_chess = True
        chess.board_state = chess.START_BOARD_STATE
        board_state_text = chess.create_board_state_text()
        await channel.send('☕')
        await channel.send(board_state_text)
        
    if not is_playing_chess:
        return
    
    # /move <before_pos> <after_pos>
    if content.startswith('/move'):
        before_pos_txt, after_pos_txt = content.split()[1:3]
        # validate
        if not chess.validate(before_pos_txt, after_pos_txt):
            await channel.send("```>> その手は打てないよ！```")
            return

        chess.move(before_pos_txt, after_pos_txt)
        board_state_text = chess.create_board_state_text()
        await channel.send(board_state_text)


client.run(token)
