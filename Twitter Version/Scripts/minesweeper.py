class Minesweeper():

    def __init__(self, height: int, width: int): # height = number of rows; width = number of columns

        import random

        # Create the grid
        grid = dict()
        for row in range(height):
            for col in range(width):
                grid[(row, col)] = [random.randint(0,4), (row, col), 0, 0]

        # Check how many bombs there are

        bomb_amount=0
        for cell, params in grid.items():
            if not params[0]:
                bomb_amount+=1

        self.grid = grid
        self.columns = width
        self.rows = height
        self.bombs = bomb_amount

        for cell, params in grid.items():
            tile_value = 0
            neighbors = self.neighbor_detection(params[1])
            for neighbor_cell, neighbor_params in neighbors.items():
                if neighbor_params[0] == 0:
                    tile_value+=1
            self.grid[cell][3] = tile_value

    def neighbor_detection(self, coords: tuple) -> dict:

        #  X X X
        #  X 0 X        - Search for the Xs
        #  X X X

        neighbors = {cell: params for (cell, params) in self.grid.items()
        if params[1] == (coords[0]-1, coords[1]-1) 
        or params[1] == (coords[0]-1, coords[1])
        or params[1] == (coords[0]-1, coords[1]+1)
        or params[1] == (coords[0], coords[1]-1)
        or params[1] == (coords[0], coords[1]+1)
        or params[1] == (coords[0]+1, coords[1]-1)
        or params[1] == (coords[0]+1, coords[1])
        or params[1] == (coords[0]+1, coords[1]+1)}

        return neighbors

    def render(self, ID) -> str:

        unindented_grid = ''

        # Decide where each one of the characters are displayed
        for cell, params in self.grid.items():

            if params[2] == 0:
                unindented_grid = unindented_grid + '\u25FC'
            else:
                if params[0] == 0:
                    unindented_grid = unindented_grid + '💣'
                else:
                    unindented_grid = unindented_grid + f'{params[3]}'

        board=''

        # Put the characters in a grid structure
        for row in range(self.rows):
            i=0
            while i <= self.columns-1:
                board = board + ' ' + unindented_grid[i+row*(self.columns)]
                i+=1
            board = board + '\n'

        return '\n' + board + '\n\n\n' + ID

    def reveal_cell(self, coords: tuple, isRecursion=False) -> bool: # True = the chosen cell was safe; False = the chosen cell was a bomb
        
        try:
            # Reveal the chosen cell, then reveal all of the neighbouring cells that
            # don't have more than one bomb around them, then do the same for the neighbouring cells
            if not isRecursion:
                self.grid[coords][2] = 1 # Uncovers the chosen cell
            for neighbor_cell, neighbor_params in self.neighbor_detection(coords).items():
                if not neighbor_params[2] and neighbor_params[0] and neighbor_params[3] <= 1:
                    neighbor_params[2] = 1
                    self.reveal_cell(neighbor_cell, True)
                    
        except:
            return True # If the chosen coordinates don't exist, the game continues
        
        if not isRecursion:
            if self.grid[coords][0]:
                return True
            else:
                return False

    def lose(self, ID) -> str:
        for cell, params in self.grid.items():
            params[2] = 1
        return f'You\'ve lost! \n\n\n {ID}'

    def win(self, ID) -> str:
        for cell, params in self.grid.items():
            params[2] = 1
        return f'You\'ve won, there were {self.bombs} bombs! \n\n\n {ID}'

    def check_if_won(self) -> bool: # True = the game continues; False = the game has ended
        moves_amount=0
        for cell, params in self.grid.items():
            if params[2]:
                moves_amount+=1
        
        if moves_amount+self.bombs == self.columns*self.rows:
            return False
        else:
            return True