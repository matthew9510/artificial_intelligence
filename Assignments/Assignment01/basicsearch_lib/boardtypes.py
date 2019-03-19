from math import sqrt
from random import shuffle
import random
from copy import deepcopy
from basicsearch_lib.board import Board


class TileBoard(Board):
    def __init__(self, n, forced_state=None):
        self.n = n
        self.total_number_of_tiles = n + 1
        self.odd_half_way_point = n // 2 + 1
        self.sqrt_total_number_of_tiles = int(sqrt(self.total_number_of_tiles))
        self.forced_state = forced_state
        super().__init__(self.sqrt_total_number_of_tiles, self.sqrt_total_number_of_tiles)

        if self.forced_state is not None:
            self.board = self.convert_to_board(self.forced_state)
            if not self.solvable():
                print("Not solvable")# todo: Throw error - The forced state you passed in is unsolvable # CHECK throw error if not numbers
        else:
            self.board = self.create_random_instance_of_board()
            while not self.solvable():
                self.board = self.create_random_instance_of_board()

    def convert_to_board(self, list_to_convert):
        """ This method converts a one dimensional list to a multi-dimensional board
        :param list_to_convert
        :type list_to_convert: one dimensional list
        :return: Board.board: multi-dimensional list
        """
        temp_board = Board(self.sqrt_total_number_of_tiles, self.sqrt_total_number_of_tiles)
        current_idx = 0
        for i in range(temp_board.get_rows()):
            for j in range(temp_board.get_cols()):
                temp_board.place(i, j, list_to_convert[current_idx])
                current_idx += 1
        return temp_board.board

    def create_random_instance_of_board(self):
        """ This method will create a instance of a Board.board object, with a random shuffled order.
        This method does not check if the new board object is solvable
        :return: Board.board object"""
        temp_list = []
        temp_board = Board(self.sqrt_total_number_of_tiles, self.sqrt_total_number_of_tiles)
        for i in range(self.n):
            temp_list.append(i + 1)
        temp_list.append(None)
        random.shuffle(temp_list)
        temp_board.board = self.convert_to_board(temp_list)  # todo: The clarification list needs to be called ON, since we need to use self. to get access to method.
        return temp_board.board

    def get_goal_state(self, size_of_board):
        """ This method returns a board with the N-puzzle goal state
        :param size_of_board: does not include the addition blank tile; size_of_board = N in an N puzzle, which is one less than the total amount of tiles on the board
        :type size_of_board: int
        :return: Board object"""
        #todo : maybe I want to return a Board.board
        total_num_of_tiles = size_of_board + 1
        sqrt_of_total_number_of_tiles = int(sqrt(total_num_of_tiles))
        row_num = sqrt_of_total_number_of_tiles
        col_num = sqrt_of_total_number_of_tiles
        odd_halfway_point = total_num_of_tiles // 2 + 1

        # temp_tile_board = TileBoard(self.n)  # CANNOT create object of a class inside a method of that class, todo: Why is this not good practice; recursion?
        temp_board = Board(row_num, col_num)
        item_value = 1  # item being placed in Board.board
        for i in range(temp_board.get_rows()):
            for j in range(temp_board.get_cols()):
                if item_value == odd_halfway_point:
                    temp_board.place(i, j, None)
                else:
                    if item_value >= odd_halfway_point + 1:  # Note: <= saved the day
                        temp_board.place(i, j, item_value - 1)
                    else:
                        temp_board.place(i, j, item_value)
                item_value += 1
        return temp_board

    def randomize_list(self, list_to_manip):
        """This method will take in a list and return a shuffled instance of that list
        :param list_to_manip
        :type list_to_manip: list: one-dimensional list
        :return temp_list: one-dimensional list"""
        temp_list = list_to_manip
        random.shuffle(temp_list)
        return temp_list


    def solvable(self):
        """Method will be called on Board object.
        Using the Inversion order technique we can
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
        flattened_board_as_list = list(self.state_tuple())  # No need to rewrite a method if we can just cast3 todo: working on

        for idx in range(len(flattened_board_as_list) - 1):  # Note: length != last_element_index
            for compare_idx in range((idx + 1), len(flattened_board_as_list)):  # Note: stop is closed form [not included]; range(start, stop)
                count = 0
                if flattened_board_as_list[idx] and flattened_board_as_list[compare_idx] is not None:
                    if flattened_board_as_list[idx] > flattened_board_as_list[compare_idx]:
                        count += 1
                inversion_order += count

        if self.get_rows() % 2 == 0:
            inversion_order += self.board.find_item_idx(target_value)[0]  # todo: check this

        if inversion_order % 2 == 0:
            return True

        else:
            return False

    def solved(self):
        """ This method will determine if the Board.board object is solved
        :return true if board is in goal state
        :return false if board is not in goal state
        """
        return self.__eq__(self.get_goal_state(self.n).board)

    def state_tuple(self):
        """ When this method is called, it will turn a Board.board object into a flattened one dimensional tuple
        :return: tuple of flattened Board.board
        """

        temp_list = []
        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                temp_list.append(self.get(i, j))
        return tuple(temp_list)

    def find_item_idx(self, target_item):
        """ This method will scan through a Board.board object and return the index of that item in a form of a tuple
        :param target_item to find
        :return: tuple, in the form (row, col)
        If not found it will return false"""
        # todo: confirm that there will not be duplicate tiles, and no missing tiles
        for row_idx in range(self.get_rows()):
            if self.board[row_idx].__contains__(target_item):
                idx_of_target_item = (row_idx, self.board[row_idx].index(target_item))
                return idx_of_target_item
        return False  # QUESTION: todo - throw error or return false """can you return two different types if one condition isn't met"""

    def __eq__(self, other_object): # todo: GET CLARIFIED, should param be Board or Board.board obj
        """This will overload the == operator to
        check if two boards have the exact same state
        :param other_object
        :type other_object: """
        return self.board == other_object

    def get_actions(self):
        """ This method will locate the Blank tile in a Board object and will determine all possible moves the blank tile can move to
        :return: tuple with possible moves in from ((row_shift ,col_shift))
        """
        current_idx_of_blank = self.find_item_idx(None)
        current_blank_row = current_idx_of_blank[0]
        current_blank_col = current_idx_of_blank[1]
        list_of_actions = []
        """ list of list with element values in the form of [row_shift, col_shift], where based on which index,
         -1 means left or down, 1 means right or down, 0 means stay """

        if current_blank_row == 0:  # None is on first row, meaning it cannot be shifted up
            if current_blank_col == 0:
                list_of_actions.append([0, 1])
                list_of_actions.append([-1, 0])
            elif current_blank_col == self.get_cols() - 1:
                list_of_actions.append([0, -1])
                list_of_actions.append([-1, 0])
            else:
                list_of_actions.append([0, 1])
                list_of_actions.append([0, -1])
                list_of_actions.append([-1, 0])

        elif current_blank_row == self.get_rows() - 1:  # None on last row, meaning it cannot be shifted down
            if current_blank_col == 0:
                list_of_actions.append([0, 1])
                list_of_actions.append([-1, 0])  # changed
            elif current_blank_col == self.get_cols() - 1:
                list_of_actions.append([0, -1])
                list_of_actions.append([1, 0])
            else:
                list_of_actions.append([0, 1])
                list_of_actions.append([0, -1])
                list_of_actions.append([1, 0])

        else:
            if current_blank_col == 0:
                list_of_actions.append([0, 1])
                list_of_actions.append([1, 0])
                list_of_actions.append([-1, 0])
            elif current_blank_col == self.get_cols() - 1:
                list_of_actions.append([0, -1])
                list_of_actions.append([1, 0])
                list_of_actions.append([-1, 0])
            else:
                list_of_actions.append([0, 1])
                list_of_actions.append([0, -1])
                list_of_actions.append([1, 0])
                list_of_actions.append([-1, 0])

        return tuple(list_of_actions)

    def move(self, shift_as_list):
        """
        :param shift_as_list: a list that specifies how to manipulate the Board.board object, in form [row_shift, col_shift]
        :return: New Board object
        """
        new_board = deepcopy(self)
        # row_shift = shift_as_list[0]  # Error in the logic
        row_shift = shift_as_list[0] * -1  # This will allow the right logic to be applied to the shift,
        # i.e. moving a row down should increase the current row, and moving up a row should actually decrease the current row
        col_shift = shift_as_list[1]
        blank_row_index = self.find_item_idx(None)[0]
        blank_col_index = self.find_item_idx(None)[1]
        index_of_element_to_move = [blank_row_index + row_shift, blank_col_index + col_shift]  # error
        temp_element_value = self.get(index_of_element_to_move[0], index_of_element_to_move[1])
        new_board.place(index_of_element_to_move[0], index_of_element_to_move[1], None)
        new_board.place(blank_row_index, blank_col_index, temp_element_value)
        return new_board