import random

class TicTacToeBoard:
    """Draws the ancient game of TicTacToe"""

    def __init__(self, players):
        self.players = players
        self.board_list = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]
        print(self.get_board())

    def get_board(self):
        board = '\n---------\n'
        for row in self.board_list:
            board += '| ' + ' '.join(row) + ' |\n'
        board += '---------'
        return board

    def accept_move(self, player):
        while True:
            if self.players[player] == 'user':
                m = input('Enter the coordinates:')
            else: # later this will have more levels, now by default 'easy'
                m = str(random.randrange(1, 4, 1)) + ' ' + str(random.randrange(1, 4, 1))

            # check move input
            try:
                x = int(m.split()[0])
                y = int(m.split()[1])
                if not 1 <= x <= 3 or not 1 <= y <= 3:
                    print('Coordinates should be from 1 to 3!')
                    continue
                elif self.board_list[x-1][y-1] != '_':
                    if self.players[player] == 'user':
                        print('This cell is occupied! Choose another one!')
                    continue
                else:
                    self.board_list[x - 1][y - 1] = player
                    if self.players[player] == 'easy':
                        print('Making move level "easy"')
                    break
            except ValueError:
                print('You should enter numbers!')

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

class Menu():

    def __init__(self):
        while True:
            try:
                action = input('Input command:').split()
                if action[0] == 'exit':
                    break

                valid_playertypes = ['user', 'easy']
                if action[0] == 'start' and set(action[1:2]).issubset(valid_playertypes):
                    players = {'X': action[1], 'O': action[2]}
                    ttt = TicTacToeBoard(players)
                    next_player = 'X'
                    while ttt.get_score() == 'Game not finished':
                        ttt.accept_move(next_player)
                        if next_player == 'X':
                            next_player = 'O'
                        else:
                            next_player = 'X'
                        print(ttt.get_board())
                    print(ttt.get_score())
            except:
                print('Bad parameters!')
                continue

play = Menu()

