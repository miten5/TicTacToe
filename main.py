from IPython.display import clear_output
import random


def display(board):
    clear_output()

    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])


def player_input():
    marker = ''

    while marker not in ['x', 'o']:
        marker = input('Player 1, Choose your marker (X or O) ').lower()

    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_turn():
    if random.randint(1, 2) == 1:
        return 'Player_1'
    else:
        return 'Player_2'


def place_marker(board, position, marker):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, turn):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f'{turn}, Choose your next position (1-9): '))

    return position


def replay():
    return input('Do you want to play again? (Y or N) ').lower().startswith('y')


print('Welcome to Tic Tac Toe Game!')

while True:
    board = [' '] * 10
    player_1_marker, player_2_marker = player_input()
    turn = choose_turn()
    print(turn + ' Will go first!')

    play_game = input(
        'Are you ready to play (Y or N): ').lower().startswith('y')

    if play_game:
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player_1':
            display(board)
            position = player_choice(board, turn)
            place_marker(board, position, player_1_marker)

            if win_check(board, player_1_marker):
                display(board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display(board)
                    print('The game is Draw!')
                    game_on = False
                else:
                    turn = 'Player_2'
        else:
            display(board)
            position = player_choice(board, turn)
            place_marker(board, position, player_2_marker)

            if win_check(board, player_2_marker):
                display(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display(board)
                    print('The game is Draw!')
                    game_on = False
                else:
                    turn = 'Player_1'

    if not replay():
        break
