'''
driver for graph search problem
Created on Feb 10, 2018

@author: mroch
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer
import collections
# todo: why import collections
from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import time

def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t

def solve(puzzle):
    start_time = tic()
    (solved_path, number_of_nodes_explored) = graph_search(puzzle)
    elapsed_time = tock(start_time)
    return (solved_path, number_of_nodes_explored, elapsed_time)

def driver() :
    start_overall_time= tic()
    sec_per_min = 60.0
    number_of_tileboard_instances = 2
    puzzle_size = 8
    methods = [BreadthFirst, DepthFirst, Manhattan]
    list_of_paths = list()
    list_of_number_of_nodes_explored = list()
    list_of_times = list()

    for n in range(number_of_tileboard_instances):
        board = TileBoard(puzzle_size)
        state_tuple = board.state_tuple()  # do this becuase we din't want to modify the original board
        for method in methods:
            puzzle = NPuzzle(puzzle_size, forced_state=state_tuple, g=method.g, h=method.h)
            (list_of_paths[n], list_of_number_of_nodes_explored[n], list_of_times[n]) = solve(puzzle)

    # print out data stored in lists

if __name__ == '__main__':
    driver()
