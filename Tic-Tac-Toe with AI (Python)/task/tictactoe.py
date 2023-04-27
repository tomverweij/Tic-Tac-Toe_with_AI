class TicTacToeBoard:
    """Draws the ancient game of TicTacToe"""

    def __init__(self):
        b = input('Enter the cells:')
        # check initial state input
        if not all((c in 'XO_') for c in b)\
                or not len(b) == 9:
            print('Incorrect initial state - must contain only ''X'',''O'',''_'' and be 9 characters long')
        self.board_list = [list(b[0:3]), list(b[3:6]), list(b[6:9])]
        print(self.get_board())

    def get_board(self):
        board = '\n---------\n'
        for row in self.board_list:
            board += '| ' + ' '.join(row) + ' |\n'
        board += '---------'
        return board

    def accept_move(self):
        while True:
            m = input('Enter the coordinates:')
            # check move input
            try:
                x = int(m.split()[0])
                y = int(m.split()[1])
                if not 1 <= x <= 3 or not 1 <= y <= 3:
                    print('Coordinates should be from 1 to 3!')
                    continue
                elif self.board_list[x-1][y-1] != '_':
                    print('This cell is occupied! Choose another one!')
                    continue
                else:
                    self.board_list[x-1][y-1] = self.get_player()
                    # self.assess_state()
                    break
            except ValueError:
                print('You should enter numbers!')

    def get_player(self):
        xx = 0
        oo = 0
        for row in self.board_list:
            xx += row.count('X')
            oo += row.count('O')
        return 'X' if xx == oo else 'O'

    def is_win(self, xo):
        # check horizontal for a win of xo
        for row in self.board_list:
            if row.count(xo) == 3:
                return True

        # check vertical for a win of xo
        cols = ['','','']
        for x in range(3):
            for y in range(3):
                cols[y] += self.board_list[x][y]
        for col in cols:
            if col.count(xo) == 3:
                return True

        # check diagonal for a win of xo
        diags = [['_','_','_'],['_','_','_']]
        diags[0] = self.board_list[0][0] + self.board_list[1][1] + self.board_list[2][2]
        diags[1] = self.board_list[0][2] + self.board_list[1][1] + self.board_list[2][0]
        for diag in diags:
            if diag.count(xo) == 3:
                return True

        # no win
        return False

    def has_empty(self):
        for row in self.board_list:
            if row.count('_') > 0:
                return True
        return False

    def get_score(self):
        if self.is_win('X'):
            return 'X wins'
        elif self.is_win('O'):
            return 'O wins'
        elif self.has_empty():
            return 'Game not finished'
        else:
            return 'Draw'


ttt = TicTacToeBoard()
ttt.accept_move()
print(ttt.get_board())
print(ttt.get_score())