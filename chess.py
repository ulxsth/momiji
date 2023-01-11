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


def create_board_state_text(board_state):
    board_state_text = '```'
    board_state_text += '    a b c d e f g h\n'
    board_state_text += '    - - - - - - - -\n'
    

    for i in range(1, 9):
        board_state_text += f'{i} | '
        line = board_state[i-1]
        
        for peace in line:
            if not peace == '':
                # peace_mark = PEACE_MARKS[peace]
                # board_state_text += peace_mark
                board_state_text += peace
            else:
                board_state_text += ' '
            board_state_text += ' '

        board_state_text += '\n'

    board_state_text += '```'
    return board_state_text
