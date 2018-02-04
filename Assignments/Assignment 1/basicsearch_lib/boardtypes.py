from basicsearch_lib.board import Board
from math import sqrt
from random import shuffle

#######################################################################
# Todo List:
#   todo - Inversion Number
#   todo - get_actions()
#   todo - move()
#   todo - is my way of inheritance calling super correct?
#######################################################################


class TileBoard(Board):  # does Board inside () mean TileBoard is a Board ?
    """Tile Board is an object that
    is a representation of a n-puzzles"""

    def __init__(self, n, forced_state=None):
        """This is a constructor that will
        create a board of a particular size
        @param n and will allow a list to be
        specifically assigned if desired"""
        self.n = n
        self.total_number_of_tiles = n + 1
        self.odd_half_way_point = n // 2 + 1
        self.sqrt_total_number_of_tiles = int(sqrt(self.total_number_of_tiles))
        self.forced_state = forced_state  # <List>
        super().__init__(self.sqrt_total_number_of_tiles, self.sqrt_total_number_of_tiles)  # todo: does this have to be super(TileBoard, self)?

        if forced_state is not None:
            self.board = forced_state.list_to_board() # todo: this might not work
            if not self.board.solvable():
                # todo: throw error

        #else: # todo: shuffle board and make sure it's solvable

    def solved(self): # todo: test with different number of rows and cols
        goal_state = TileBoard.get_goal_state(self.n)
        return self.board.__eq__(goal_state.board)

    def __eq__(self, other_object):
        """This will overload the == operator to
        check if two boards have the exact same state"""
        return self == other_object

    def state_tuple(self):
        """This will convert a board to a tuple"""
        temp_list = []
        for i in range(self.rows):
            for j in range(self.cols):
                temp_list.append(self.get(i,j))
        return tuple(temp_list)

    def get_goal_state(n):  # static method todo: why do I need to pass in a Tileboard object??
        temp_board = TileBoard(n)
        item = 1
        for i in range(temp_board.rows):
            for j in range(temp_board.cols):
                if item == temp_board.odd_half_way_point:
                    temp_board.place(i, j, None)
                else:
                    if item >= temp_board.odd_half_way_point+1: # Note: <= saved the day
                        temp_board.place(i, j, item-1)
                    else:
                        temp_board.place(i, j, item)
                item += 1
        return temp_board

    def solvable(self):
        """Using the Inversion order technique we can
        figure out if a particular board (<List> object) instance is solvable or not.

        The inversion order is the sum of all permutation inversions for each tile.
        Conditions:
        - Two elements a[i] and a[j] form an inversion if i < j and a[i] > a[j]
        If the <Board> object has an even number of rows, then the row of the
        blank must be added to the inversion number.

        Note: The board will be solvable if the inversion order is even.
        """
        inversion_order = 0
        target_value = None
        board_as_list = list(self.state_tuple())
        for idx in range(len(board_as_list)-1): #  todo check if minus 1 is correct
            for compare_idx in range((idx+1), len(board_as_list)):
                count = 0
                if board_as_list[idx] and board_as_list[compare_idx] is not None:  # really important for future comparing
                    if board_as_list[idx] > board_as_list[compare_idx]:
                        count += 1
                inversion_order += count
        if self.get_rows() % 2 == 0:
            inversion_order += board_as_list.find_item_idx(target_value)[0]  # todo - should I catch False?
        if inversion_order % 2 == 0:
            return True
        else:
            return False

    def find_item_idx(self, target_item):
        """Returns a tuple containing the index of the found item, in the form (row, col)
        If not found it will return false"""
        # todo - confirm that there will not be duplicate tiles
        for row_idx in range(self.get_rows()):
            if self.board[row_idx].__contains__(target_item):
                idx_of_target_item = (row_idx, self.board[row_idx].index(target_item)) # todo - does .index return the first instance?
                return idx_of_target_item
        return False #  todo - throw error , should I do this?


    def list_to_board(self): # todo: check logic
        idx = 0
        temp_board = Board(self.rows, self.cols)
        while idx <= len(self.forced_state):  # self.total_number_of_tiles - 1:
            for i in range(self.sqrt_total_number_of_tiles):
                for j in range(self.sqrt_total_number_of_tiles):
                    temp_board.place(i, j, self[idx])
                    idx += 1
        return temp_board  # todo: check if this is right

    def get_actions(self):
        # """This will return a list of possible actions that can be called on the board"""

    def move(self, offset):
        #  Note: Make sure this is a deep copy, so we don't manipulate the pointer



print(TileBoard.get_goal_state(24))
#test_board = TileBoard(24,[1,2,3,4,None,5,6,7,8])  # todo throw an error on this
test_tile_board = TileBoard(8, [1, 2, 3, 4, 5, None, 6, 8, 7])
print(test_tile_board)
print(test_tile_board.solved())
print(test_tile_board.find_item_idx(None)[1])
print(test_tile_board.solvable())




######################################################################
#  Self Note:
######################################################################
d = [[1,2], [1,3], [3,None]]
# print(d.find_item_idx(None)) # Won't work because d does not have attributes .get_rows
test_board = Board(3,3)
# print(test_board.find_item_index(None))  #<Board> Objects wont work either becuase doesn't contain children classes