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


board_state = START_BOARD_STATE
def create_board_state_text():
    """board_stateから表示用のテキストを生成する

    Args:
        board_state (list): ボード状態を示す二次元配列

    Returns:
        str: ボード状態を示すテキスト
    """
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


def notation_to_pos(notation):
    return ord(notation) - ord('a') + 1


def txt_to_pos(pos_txt):
    line = notation_to_pos(pos_txt[0])
    column = int(pos_txt[1])
    return column, line


def pos_to_index(pos):
    return list(map(lambda x: x-1, pos))


def get_peace_by_pos(pos):
    index = pos_to_index(pos)
    return board_state[index[0]][index[1]]


def set_peace_by_pos(peace, pos):
    global board_state
    index = pos_to_index(pos)
    board_state[index[0]][index[1]] = peace


def validate(before_pos_txt, after_pos_txt) -> bool:
    return True


def move(before_pos_txt, after_pos_txt):
    before_pos = txt_to_pos(before_pos_txt)
    after_pos = txt_to_pos(after_pos_txt)
    peace = get_peace_by_pos(before_pos)
    set_peace_by_pos(peace, after_pos)
    set_peace_by_pos(' ', before_pos)