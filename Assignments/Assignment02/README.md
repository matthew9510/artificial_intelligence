#### Assignment02 README

[Assignment instructions](A02.pdf)

#### Abstract Overview

Working off of [assignment01](../Assignment01/README.md) we will write a generic graph search routine to find solutions to various npuzzles using search algorithms such as 
 - breadth-first search
 - depth-first search
 - A* using a Manhattan distance heuristic

 Several classes are provided in package basicsearch_lib02 will help in this endeavor.

 [driver02.py](driver02.py) – The driver module will create 31 different tile board puzzles using the implementation of the npuzzle class

 [problemsearch.py](problemsearch.py) – Implementation of a function graph_search.  It takes an instance of NPuzzle and flags for controlling verbosity and debugging (see file for details) and conducts a search. 

[explored.py](explored.py) – Implementation of  class Explored.  Apart from the no argument constructor, it has two methods:  exists(state) and add(state).  Both of these expect state tuples from a TileBoard and use a hash table to determine whether a state has been seen before (exists) and to add new states as they are removed from the frontier set (add). 

[searchstrategies.py](searchstrategies.py) – Implementation of classes BreadthFirst, DepthFirst, and A* using the Manhattan distance heuristic.

[queues.py](basicsearch_lib02/queues.py) uses the class PriorityQueue to maintain the order of the queue

##### Checkout
- The assignment instructions linked at the top of this readme to better understand the assignment
- [Code](.)
- The [driver](driver02.py) for using and interacting with the implementation. 
- [Research done alongside this assignment](Research)


 

 
