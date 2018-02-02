from basicsearch_lib.board import Board
from math import sqrt
from random import shuffle


class TileBoard(Board):
    """Tile Board is an object that
    is a representation of a n-puzzles"""

    def __init__(self, n, forced_state=None):
        """This is a constructor that will
        create a board of a particular size
        @param n and will allow a list to be
        specifically assigned if desired"""
        self.n = n
        self.total_number_of_tiles = n + 1
        self.odd_half_way_point = n // 2 + 1 # todo do I need to have self.
        self.sqrt_total_number_of_tiles = int(sqrt(self.total_number_of_tiles))
        self.forced_state = forced_state
        super().__init__(self.sqrt_total_number_of_tiles, self.sqrt_total_number_of_tiles)
        if forced_state is not None:
            idx = 0
            while idx <= self.total_number_of_tiles - 1:
                for i in range(self.sqrt_total_number_of_tiles):
                    for j in range(self.sqrt_total_number_of_tiles):
                        self.place(i, j, forced_state[idx])
                        idx += 1

    def solved(self):  ##self == thing before the dot todo think of 4*4
        goal_state = TileBoard.get_goal_state(self.n)
        return self.board.__eq__(goal_state.board)

    def solvable(self, board_as_list):
        """Using the Inversion order technique we can
        figure out if a particular board instance is solvable or not.
        The inversion number is the sum of all permutation inversions
        for each tile.
        If the board has an even number of rows, then the row of the
        blank must be added to the _____(inversion number ).
        Condition: Two elements a[i] and a[j] form an inversion
        if i < j and a[i] > a[j]
        Note: The board will be solvable if the inversion number is even.
        Board is reshuffled if not solvable"""

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
        test_board = TileBoard(n)
        item = 1
        for i in range(test_board.rows):
            for j in range(test_board.cols):
                if item == test_board.odd_half_way_point:
                    test_board.place(i, j, None)
                else:
                    if item >= test_board.odd_half_way_point+1: # Note: <= saved the day
                        test_board.place(i, j, item-1)
                    else:
                        test_board.place(i, j, item)
                item += 1
        return test_board


print(TileBoard.get_goal_state(24))
#test_board = TileBoard(24,[1,2,3,4,None,5,6,7,8])  # todo throw an error on this
test_board = TileBoard(8,[1,2,3,4,5,None,6,7,8])
print(test_board)
print(test_board.solved())
