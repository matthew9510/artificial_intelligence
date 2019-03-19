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

    frontier = PriorityQueue(order=min, f=lambda x: x.get_f()) # todo Sort this out
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
            break
        child_nodes = node.expand(problem)
        if explored.add(node.state):
            counter = counter + 1
        for child_node in child_nodes:
            if child_node not in frontier and not explored.exists(child_node.state):
                frontier.append(child_node)

    path = node.solution()
    node_path = node.path()
    if verbose:
        print("Solution in " + str(len(node_path) - 1) + " moves.")
        i = 0
        for sol in node_path:
            if i is 0:
                print("Initial state")
                print(sol.state)
                i = i + 1
                continue
            print("Move " + str(i) + " - " + str(path[i-1]))
            print(sol.state)
            i = i + 1
    nodes_explored = counter
    return_tuple = (path, nodes_explored)
    return return_tuple









