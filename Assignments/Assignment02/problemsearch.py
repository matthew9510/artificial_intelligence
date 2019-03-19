'''
Created on Feb 10, 2018

@author: mroch
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from explored import Explored
import time


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.

    If debug is True, debugging information will be displayed.

    if verbose is True, the following information will be displayed:

        Number of moves to solution
        List of moves and resulting puzzle states
        Example:

            Solution in 25 moves
            Initial state
                  0        1        2
            0     4        8        7
            1     5        .        2
            2     3        6        1
            Move 1 -  [0, -1]
                  0        1        2
            0     4        8        7
            1     .        5        2
            2     3        6        1
            Move 2 -  [1, 0]
                  0        1        2
            0     4        8        7
            1     3        5        2
            2     .        6        1

            ... more moves ...

                  0        1        2
            0     1        3        5
            1     4        2        .
            2     6        7        8
            Move 22 -  [-1, 0]
                  0        1        2
            0     1        3        .
            1     4        2        5
            2     6        7        8
            Move 23 -  [0, -1]
                  0        1        2
            0     1        .        3
            1     4        2        5
            2     6        7        8
            Move 24 -  [1, 0]
                  0        1        2
            0     1        2        3
            1     4        .        5
            2     6        7        8

        If no solution were found (not possible with the puzzles we
        are using), we would display:

            No solution found

    Returns a tuple (path, nodes_explored) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    """

    path = []
    nodes_explored = 0
    return_tuple = ()

    node = Node(problem, problem.initial)  # root node

    frontier = PriorityQueue(order=min, f=lambda x: x.get_f())
    explored = Explored()
    frontier.append(node)

    if problem.goal_test(node.state):
        path = node.solution()
        return_tuple = (path, nodes_explored)
        return return_tuple

    counter = 0

    while True:
        if frontier.__len__() == 0:
            path = node.solution()
            nodes_explored = counter
            return_tuple = (path, nodes_explored)
            return return_tuple
        node = frontier.pop()
        if problem.goal_test(node.state):
            path = node.solution()
            nodes_explored = counter
            return_tuple = (path, nodes_explored)
            return return_tuple
        explored.add(node.state)
        child_nodes = node.expand(problem)
        frontier.extend(child_nodes)
        counter = counter + 1


"""
    nodes = []
    for i in range(0,4):
        node = frontier.pop()
        nodes.append(node)
    print_nodes(nodes)
    # loop do: # essentially keep running until we find goal state else return failure
    if frontier.__len__() == 0:
        return_tuple = (None, nodes_explored)
        return return_tuple
    else:
        return_tuple = (path, nodes_explored)
        return return_tuple
"""
