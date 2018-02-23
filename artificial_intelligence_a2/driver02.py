'''
driver for graph search problem
Created on Feb 10, 2018

@author: mroch
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t
    
def driver() :

    #raise NotImplemented
    puzzle_size = 8
    puzzle = NPuzzle(puzzle_size, g=BreadthFirst.g, h=BreadthFirst.h)
    (solution, nodesexpanded) = graph_search(puzzle)
    print(solution)

    '''
    tileboards = []
    for i in range(0,2):
        tileboards.append(TileBoard(8))

    for tileboard in tileboards:
        NPuzzle(len(tileboard.board), tileboard, goals=[1,2,3,4,None,5,6,7,8], g=BreadthFirst.g, h=BreadthFirst.h)
        NPuzzle(len(tileboard.board), tileboard, goals=[1,2,3,4,None,5,6,7,8], g=DepthFirst.g, h=DepthFirst.h)
        #NPuzzle(len(tileboard.board), tileboard, goals=[1,2,3,4,None,5,6,7,8], g=Manhattan.g, h=Manhattan.h)
    '''

if __name__ == '__main__':
    driver()
