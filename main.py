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

    if "もみじ" in content:
        await channel.send('💕')

    # chess
    elif content == '/chess':
        global board
        board = chess.Board() # ボードを生成
        await channel.send('☕')
        await channel.send(board.get_board_state_text())
    
    if board == None:
        return
    
    # /move <before_pos> <after_pos>
    if content.startswith('/move'):
        args = content.split()[1:]
        if len(args) != 2:
            await channel.send("""
                                ```つかいかた：/move <動かすコマのあるマス> <移動先のマス>
                                例：/move b7 b6 ... b7のコマをb6に移動させるよ```
                                """.replace("    ", ""))
            return
        before_pos_txt, after_pos_txt = args
        
        # validate
        if not board.validate(before_pos_txt, after_pos_txt):
            await channel.send("```>> その手は打てないよ！```")
            return

        board.move(before_pos_txt, after_pos_txt)
        board_state_text = board.get_board_state_text()
        await channel.send(board_state_text)


client.run(token)
