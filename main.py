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

    if "ใใฟใ" in content:
        await channel.send('๐')

    # chess
    elif content == '/chess':
        global board
        board = chess.Board() # ใใผใใ็ๆ
        await channel.send('โ')
        await channel.send(board.get_board_state_text())
        print("[CHESS] board created successful.")
    
    if board == None:
        return
    
    # /move <before_pos> <after_pos>
    if content.startswith('/move'):
        args = content.split()[1:]
        if len(args) != 2:
            await channel.send("""
                                ```ใคใใใใ๏ผ/move <ๅใใใณใใฎใใใใน> <็งปๅๅใฎใใน>
                                ไพ๏ผ/move b7 b6 ... b7ใฎใณใใb6ใซ็งปๅใใใใ```
                                """.replace("    ", ""))
            return
        before_pos_txt, after_pos_txt = args
        
        # validate
        if not board.validate(before_pos_txt, after_pos_txt):
            await channel.send("```>> ใใฎๆใฏๆใฆใชใใ๏ผ```")
            return

        board.move(before_pos_txt, after_pos_txt)
        board_state_text = board.get_board_state_text()
        await channel.send(board_state_text)


client.run(token)
