"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def remove_zeros(zero_list):
    """
    Supplementary function for 2048 game to remove zeros from the list.
    """
    temp_list = []
    for indx in zero_list:
        if indx != 0:
            temp_list.append(indx)
    return temp_list


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    if len(line) < 2:
        return line

    temp_list = remove_zeros(line)

    if len(temp_list) < 2:
        for dummy in range(len(line) - len(temp_list)):
            temp_list.append(0)
        return temp_list

    new_list = []
    indx = 0
    while indx < len(temp_list) - 1:
        if temp_list[indx] == temp_list[indx + 1]:
            new_list.append(temp_list[indx] + temp_list[indx])
            new_list.append(0)
            indx += 2
        else:
            new_list.append(temp_list[indx])
            indx += 1

    if len(new_list) < len(line):
        if len(temp_list) > 2:
            if (temp_list[-1] != temp_list[-2]) or (temp_list[-1] == temp_list[-2] and temp_list[-3] == temp_list[-2]):
                new_list.append(temp_list[-1])
        else:
            if temp_list[-1] != temp_list[-2]:
                new_list.append(temp_list[-1])

    temp_list = remove_zeros(new_list)

    for indx in range(len(temp_list), len(line)):
        temp_list.append(0)

    return temp_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.width)] for dummy_row in range(self.height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        representation = "Print out values in grid\n"
        for row in range(self.height):
            representation += str(self.grid[row]) + "\n"
        return representation


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty square.
        The tile should be 2 90% of the time and 4 10% of the time.
        """
        empty_cells = []
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    empty_cells.append((row,col))
        print "empty", empty_cells
        if not empty_cells:
            print "no empty cells"
            return

        value_randomize = random.randint(1, 10)
        if value_randomize == 5: tile_value = 4
        else: tile_value = 2
        print "value", tile_value

        random_cell = random.choice(empty_cells)
        print "random cell", random_cell
        self.grid[random_cell[0]][random_cell[1]] = tile_value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

# While you are implementing the TwentyFortyEight class, you should comment out these two lines
# and test each method individually using your test suite.
# Once your code has passed these tests, you can uncomment the two lines that import and run the GUI.
# poc_2048_gui.run_gui(TwentyFortyEight(5, 4))

new_grid = TwentyFortyEight(5,4)

print str(new_grid)

for dummy in range(new_grid.get_grid_height()*4):
    new_grid.new_tile()
    print str(new_grid)


