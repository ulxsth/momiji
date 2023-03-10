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


def notation_to_line(notation):
    return ord(notation) - ord('a') + 1


def line_to_notation(line):
    return chr(ord('a') + line - 1)


def txt_to_pos(pos_txt):
    column = notation_to_line(pos_txt[0])
    line = int(pos_txt[1])
    return line, column


def pos_to_txt(pos):
    column = line_to_notation(pos[0])
    line = str(pos[1])
    return column + line


def pos_to_index(pos):
    return list(map(lambda x: x-1, pos))


def calc_pos_diff(before_pos, after_pos):
    return list([after_pos[0] - before_pos[0], after_pos[1] - before_pos[1]])


def is_white(peace):
    return peace.isupper()


def is_black(peace):
    return peace.islower()


class Board():
    def __init__(self):
        self.board_state = START_BOARD_STATE
        
    def broadcast(self, str):
        print(f"[CHESS] {str}")
    
    
    def is_exist(self, pos):
        return self.get_peace_by_pos(pos) != ' '
        
    
    def get_peace_by_pos(self, pos):
        index = pos_to_index(pos)
        return self.board_state[index[0]][index[1]]
    
    
    def set_peace_by_pos(self, peace, pos):
        index = pos_to_index(pos)
        self.board_state[index[0]][index[1]] = peace
        
        
    def get_board_state_text(self):
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
            line = self.board_state[i-1]
            
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
    
    
    def validate(self, before_pos_txt, after_pos_txt) -> bool:
        # 不正な引数（座標を指定していない）
        if len(before_pos_txt) != 2 or len(after_pos_txt) != 2:
            return False
        
        before_pos, after_pos = txt_to_pos(before_pos_txt), txt_to_pos(after_pos_txt)
        before_peace, after_peace = self.get_peace_by_pos(before_pos), self.get_peace_by_pos(after_pos)
        self.broadcast(f"before: {before_pos_txt}({before_peace}) -> {after_pos_txt}")
        
        # before_pos に駒がない
        if before_peace == '':
            return False
        
        pos_diff = calc_pos_diff(before_pos, after_pos)
        
        # *ポーン
        # 黒
        if before_peace == 'p':
            # 縦1マス
            if pos_diff == [1, 0] and not self.is_exist(after_pos):
                return True
            
            # 縦2マス（初動のみ）
            elif pos_diff == [2, 0] and before_pos[0] == 2:
                return True
            
            # 斜め前（相手コマがあるときのみ）
            elif pos_diff in [[1, 1], [1, -1]] and self.is_exist(after_pos) and is_white(after_peace):
                return True
        
        # 白    
        elif before_peace == 'P':
            # 縦1マス
            if pos_diff == [-1, 0] and not self.is_exist(after_pos):
                return True
            
            # 縦2マス（初動のみ）
            elif pos_diff == [-2, 0] and before_pos[0] == 7:
                return True
            
            # 斜め前（相手コマがあるときのみ）
            elif pos_diff in [[-1, 1], [-1, -1]] and self.is_exist(after_pos) and is_black(after_peace):
                return True
        
        return False


    def move(self, before_pos_txt, after_pos_txt):
        before_pos = txt_to_pos(before_pos_txt)
        after_pos = txt_to_pos(after_pos_txt)
        peace = self.get_peace_by_pos(before_pos)
        self.set_peace_by_pos(peace, after_pos)
        self.set_peace_by_pos(' ', before_pos)
