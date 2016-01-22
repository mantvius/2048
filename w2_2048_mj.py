"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random
# try:
#     import simplegui
# except ImportError:
#     import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


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
        for dummy_cell in range(len(line) - len(temp_list)):
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
        self._height = grid_height
        self._width = grid_width

        self._list_up = []
        for col in range(grid_width):
            cell = (0, col)
            self._list_up.append(cell)

        self._list_down = []
        for col in range(grid_width):
            cell = (grid_height - 1, col)
            self._list_down.append(cell)

        self._list_right = []
        for row in range(grid_height):
            cell = (row, grid_width - 1)
            self._list_right.append(cell)

        self._list_left = []
        for row in range(grid_height):
            cell = (row, 0)
            self._list_left.append(cell)

        self._init_lists = {UP: self._list_up, DOWN: self._list_down, RIGHT: self._list_right, LEFT: self._list_left}

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        representation = "The values of the grid:\n"
        for row in range(self._height):
            representation += str(self._grid[row]) + "\n"
        return representation

    def game_over(self, win):
        """
        Function announcing that the game has ended
        """
        if win:
            print "You won!"
        else:
            print "You lost!"
        self.reset()

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        move_made = False
        init_list = self._init_lists[direction]
        print "init_list", init_list
        direction_tuple = OFFSETS[direction]
        print "direction_tuple", direction_tuple

        if direction == 1 or direction == 2:
            num_steps = self._height
        else:
            num_steps = self._width

        for init_tile in init_list:
            #print "starting with tile " + str(init_tile)
            list_values = []
            for step in range(num_steps):
                row = init_tile[0] + step * direction_tuple[0]
                col = init_tile[1] + step * direction_tuple[1]
                #print "Processing cell", (row, col),
                #print "with value", self._grid[row][col]
                list_values.append(self._grid[row][col])
            #print "list_values", list_values
            merged_line = merge(list_values)
            for tile in merged_line:
                if tile == 2048:
                    self.game_over(True)
            #print "merged_line", merged_line
            if merged_line != list_values:
                move_made = True
            for step in range(num_steps):
                row = init_tile[0] + step * direction_tuple[0]
                col = init_tile[1] + step * direction_tuple[1]
                self.set_tile(row, col, merged_line[step])

        if move_made:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty square.
        The tile should be 2 90% of the time and 4 10% of the time.
        """
        empty_cells = []
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    empty_cells.append((row, col))
        if not empty_cells:
            print "no empty cells"
            self.game_over(False)

        value_randomize = random.randint(1, 10)
        if value_randomize == 5:
            tile_value = 4
        else:
            tile_value = 2

        random_cell = random.choice(empty_cells)
        self._grid[random_cell[0]][random_cell[1]] = tile_value

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

# While you are implementing the TwentyFortyEight class, you should comment out these two lines
# and test each method individually using your test suite.
# Once your code has passed these tests, you can uncomment the two lines that import and run the GUI.
# poc_2048_gui.run_gui(TwentyFortyEight(5, 4))

# New_grid = TwentyFortyEight(3, 5)
# print str(New_grid)
#
# while True:
#     print "UP = 1"
#     print "DOWN = 2"
#     print "LEFT = 3"
#     print "RIGHT = 4"
#
#     direct = raw_input('Enter direction: ')
#     New_grid.move(direct)
#     print str(New_grid)

# New_grid.move(UP)
# print str(New_grid)
# New_grid.move(DOWN)
# print str(New_grid)
# New_grid.move(RIGHT)
# print str(New_grid)
# New_grid.move(LEFT)
# print str(New_grid)

# print str(new_grid)
# print new_grid._list_up
# print new_grid._list_down
# print new_grid._list_right
# print new_grid._list_left
# print new_grid._init_lists
# print type(new_grid._init_lists)
#
# for dummy in range(new_grid.get_grid_height()*4):
#     new_grid.new_tile()
#     print str(new_grid)
