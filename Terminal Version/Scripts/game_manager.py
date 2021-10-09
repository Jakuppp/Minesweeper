from minesweeper import Minesweeper
from other import *

if __name__ == '__main__':

    while True:
        # Create a new game
        game = Minesweeper(5,5)
        game_on = True
        won = True
        while game_on:
            print(game.render())
            inpt = input('cell:\n>>>')
            # Reveals the chosen cell
            # If the chosen cell is the bomb the game loop argument
            # will be set to False
            choice = game.reveal_cell(transform_input(inpt))
            game_on = choice
            if game_on:
                won = game.check_if_won()
                if not won:
                    game_on=won
                else:
                    pass
        # "Game over screen"
        if not won:
            print(game.win())
        else:
            print(game.lose())
        print(game.render())
        print('---------------------\n\n\n')
