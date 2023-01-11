fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

START_BOARD_STATE = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', ],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

PEACE_MARKS = {
    'k': '♔',
    'K': '♚',
    'q': '♕',
    'Q': '♛',
    'r': '♖',
    'R': '♜',
    'b': '♗',
    'B': '♝',
    'n': '♘',
    'N': '♞',
    'p': '♙',
    'P': '♟'
}

def get_board_state_text(board_state):
    board_state_text = '```\n'
    
    for line in board_state:
        for peace in line:
            if not peace == '':
                peace_mark = PEACE_MARKS[peace]
                board_state_text += peace_mark
            else:
                board_state_text += ' '
            board_state_text += ' '
            
        board_state_text += '\n'
        
    board_state_text += '```'
    return board_state_text