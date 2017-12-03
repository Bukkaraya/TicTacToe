import pyTree
from board import Board
from minimax import mini_max

SELF_PIECE = 'X'
OPP_PIECE = 'O'

def main():
    game_board = Board()

    while(not game_board.board_won(SELF_PIECE) and not game_board.board_won(OPP_PIECE)):
        print('Where do you want to enter your piece:')
        x_loc = int(input('Row Location: '))
        y_loc = int(input('Column Location: '))
        game_board.insert_element(x_loc, y_loc, OPP_PIECE)
        print(str(game_board))
        if game_board.board_won(OPP_PIECE):
            print('You won')
            break
        game_board = mini_max(game_board)
        if game_board.board_won(SELF_PIECE):
            print('You Lost')
            break

        print(str(game_board))

        



if __name__ == '__main__':
    main()