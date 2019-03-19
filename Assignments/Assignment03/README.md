[Assignment instructions](A03.pdf)

#### Abstract Overview

A program that plays the game of checkers with an artificial intelligence agent.

[checkerboard.py](checkers/basicsearch_lib/checkerboard.py) – Contains the checkerboard class

[abstractstrategy.py](checkers/basicsearch_lib/abstract.py) – An abstract Strategy class that should be extended to implement your utility function.

[human.py](checkers/basicsearch_lib/human.py)  - A concrete strategy class derived from AbstractStrategy that lets humans play.

[ai.py](checkers/basicsearch_lib/ai.py) – A class that implements the utility function. It's is a concrete class derived from [abstractstrategy.py](checkers/basicsearch_lib/abstract.py) and follows its interface. Designed using an **alpha-beta search** and **evaluation function**.

##### Checkout
- The assignment instructions linked at the top of this readme to better understand the assignment
- [Code](.)
- The [driver](checkers/basicsearch_lib/checkers.py) for using and interacting with the implementation. 



