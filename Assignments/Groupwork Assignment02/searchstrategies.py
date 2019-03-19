"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles of an odd length
    with solutions that contain the blank in the middle and numbers going
    from left to right in each row, e.g.:
        123
        4 5
        678
    When mulitple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropritate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
 

class BreadthFirst:
    "BredthFirst - breadthfirst search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        return parentnode.depth + 1
    @classmethod
    def h(cls, state):
        return 0

class DepthFirst:
    "DepthFirst - depth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        return childnode.depth * -1

    @classmethod
    def h(cls, state):
        return 0
        
class Manhattan:
    "Manhattan Block Distance heuristic"

    @classmethod
    def g(cls, parentnode, action, childnode):
        return (parentnode.depth + 2)

    @classmethod
    def h(cls, state):
        manValue = 0
        goal = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        for row in range(state.boardsize):
            for col in range(state.boardsize):
                value = state.board[row][col]
                if(value is None):
                    continue
                elif(value < 5):
                    coordinates = goal[value - 1]
                    manValue = manValue + abs(row-coordinates[0]) + abs(col-coordinates[1])
                else:
                    coordinates = goal[value]
                    manValue = manValue + abs(row-coordinates[0]) + abs(col-coordinates[1])
        return manValue

                

       
