import random


class TicTacToeBoard:
    """Draws the ancient game of TicTacToe"""

    def __init__(self, players):
        self.players = players
        self.board_list = [['_', '_', '_'],
                           ['_', '_', '_'],
                           ['_', '_', '_']]

    def get_board(self):
        board = '\n---------\n'
        for row in self.board_list:
            board += '| ' + ' '.join(row) + ' |\n'
        board += '---------'
        return board

    def accept_move(self, player):
        possible_moves = []
        for x in range(3):
            for y in range(3):
                if self.board_list[x][y] == '_':
                    possible_moves += [str(x + 1) + ' ' + str(y + 1)]

        if self.players[player] == 'user':
            while True:
                m = input('Enter the coordinates:')

                try:
                    x = int(m.split()[0])
                    y = int(m.split()[1])
                    if not 1 <= x <= 3 or not 1 <= y <= 3:
                        print('Coordinates should be from 1 to 3!')
                        continue
                    elif m not in possible_moves:
                        print('This cell is occupied! Choose another one!')
                        continue
                    else:
                        self.board_list[x - 1][y - 1] = player
                        break
                except (ValueError, IndexError):
                    print('You should enter numbers!')

        elif self.players[player] == 'easy':
            m = random.choice(possible_moves)

        else:  # 'medium'
            win_move = self.find_win_move(player)
            defense_move = self.find_win_move('X' if player == 'O' else 'O')
            if win_move is not None:
                m = win_move
            elif defense_move is not None:
                m = defense_move
            else:  # play easy
                m = random.choice(possible_moves)

        if self.players[player] in ['easy', 'medium']:
            print(f'Making move level "{self.players[player]}"')
            x = int(m.split()[0])
            y = int(m.split()[1])
            self.board_list[x - 1][y - 1] = player

    def find_win_move(self, player):
        # check horizontal for possible win moves
        x = 1
        for row in self.board_list:
            if row.count(player) == 2 and row.count('_') == 1:
                # find the index (+1) for column (=y)
                return str(x) + ' ' + str([y for y in range(3) if row[y] == '_'][0] + 1)
            x += 1

        # check vertical for possible win moves
        cols = ['', '', '']
        for x in range(3):
            for y in range(3):
                cols[y] += self.board_list[x][y]
        y = 1
        for col in cols:
            if col.count(player) == 2 and col.count('_') == 1:
                # find the index (+1) for row (=x)
                return str([x for x in range(3) if col[x] == '_'][0] + 1) + ' ' + str(y)
            y += 1

        # check diagonal for possible win moves
        diagonals = [['_', '_', '_'], ['_', '_', '_']]
        diagonals[0] = self.board_list[0][0] + self.board_list[1][1] + self.board_list[2][2]
        diagonals[1] = self.board_list[0][2] + self.board_list[1][1] + self.board_list[2][0]
        if diagonals[0].count(player) == 2 and diagonals[0].count('_') == 1:
            if diagonals[0][0] == '_':
                return '1 1'
            elif diagonals[1][1] == '_':
                return '2 2'
            else:
                return '3 3'

        if diagonals[1].count(player) == 2 and diagonals[1].count('_') == 1:
            if diagonals[1][2] == '_':
                return '1 3'
            elif diagonals[1][1] == '_':
                return '2 2'
            else:
                return '3 1'

    def is_win(self, xo):
        # check horizontal for a win of xo
        for row in self.board_list:
            if row.count(xo) == 3:
                return True

        # check vertical for a win of xo
        cols = ['', '', '']
        for x in range(3):
            for y in range(3):
                cols[y] += self.board_list[x][y]
        for col in cols:
            if col.count(xo) == 3:
                return True

        # check diagonal for a win of xo
        diagonals = [['_', '_', '_'], ['_', '_', '_']]
        diagonals[0] = self.board_list[0][0] + self.board_list[1][1] + self.board_list[2][2]
        diagonals[1] = self.board_list[0][2] + self.board_list[1][1] + self.board_list[2][0]
        for diagonal in diagonals:
            if diagonal.count(xo) == 3:
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


class Menu:

    def __init__(self):
        while True:
            try:
                action = input('Input command:').split()
                if action[0] == 'exit':
                    break

                valid_player_types = ['user', 'easy', 'medium']
                if action[0] == 'start' and set(action[1:2]).issubset(valid_player_types):
                    players = {'X': action[1], 'O': action[2]}
                    ttt = TicTacToeBoard(players)
                    print(ttt.get_board())
                    next_player = 'X'
                    while ttt.get_score() == 'Game not finished':
                        ttt.accept_move(next_player)
                        print(ttt.get_board())
                        if next_player == 'X':
                            next_player = 'O'
                        else:
                            next_player = 'X'
                    print(ttt.get_score())
            except IndexError:
                print('Bad parameters!')
                continue


play = Menu()
