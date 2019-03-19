from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from backtrack import backtracking_search
from csp_lib.backtrack_util import mrv, mac

easy_puzzle = Sudoku(easy1)
easy_puzzle.display(easy_puzzle.infer_assignment())
print(AC3(easy_puzzle))
easy_puzzle.display(easy_puzzle.infer_assignment())


hard_puzzle = Sudoku(harder1)
hard_puzzle.display(hard_puzzle.infer_assignment())
print(AC3(easy_puzzle))
result = backtracking_search(hard_puzzle, select_unassigned_variable=mrv, inference=mac)
#print("result = " + str(result))
hard_puzzle.display(hard_puzzle.infer_assignment())



#easy_puzzle.display(easy_puzzle.infer_assignment())
'''
print("\n")
print("Domains Stuff")
print("print(easy_puzzle.domains)")
print(easy_puzzle.domains)
print("print(len(easy_puzzle.domains))")
print(len(easy_puzzle.domains))
print("print(type(easy_puzzle.domains[0]))")
print(type(easy_puzzle.domains[0]))
print("print(type(easy_puzzle.domains[2]))")
print(type(easy_puzzle.domains[2]))
print("print(easy_puzzle.domains[2][0])")
print(easy_puzzle.domains[2][0])
print("print(type(easy_puzzle.domains[2][0]))")
print(type(easy_puzzle.domains[2][0]))
print("print(easy_puzzle.domains[1][0])")
print(easy_puzzle.domains[1][0])
print("print(type(easy_puzzle.domains[1][0]))")
print(type(easy_puzzle.domains[1][0]))
print("print(easy_puzzle.domains[3][0])")
print(easy_puzzle.domains[3][0])
print("print(type(easy_puzzle.domains[3][0]))")
print(type(easy_puzzle.domains[3][0]))

print("Assignment of 'var' curr_domains, which is what we'll be mutating not 'var' domains.")
print("easy_puzzle.curr_domains[0][8] = str(34) # assignment")
easy_puzzle.curr_domains[0][8] = str(34) # assignment
print("print(easy_puzzle.curr_domains[0])")
print(easy_puzzle.curr_domains[0])
print("print(type(easy_puzzle.curr_domains[0]))")
print(type(easy_puzzle.curr_domains[0]))
print("print(easy_puzzle.curr_domains[2])")
print(easy_puzzle.curr_domains[2])
print("print(type(easy_puzzle.curr_domains[2]))")
print(type(easy_puzzle.curr_domains[2]))
print(easy_puzzle.curr_domains)
print("Mutated curr_domain[0][8]: ")
print("print(easy_puzzle.curr_domains[0][8])")
print(easy_puzzle.curr_domains[0][8])
print("print(type(easy_puzzle.curr_domains[0][8]))")
print(type(easy_puzzle.curr_domains[0][8]))
print("\n")
print("Variables Stuff")
print("print(type(easy_puzzle.variables))")
print(type(easy_puzzle.variables))
print("print(easy_puzzle.variables[0])")
print(easy_puzzle.variables[0])
print("print(type(easy_puzzle.variables[0])) # 0(index) corresponds to 0(var)")
print(type(easy_puzzle.variables[0]))  # 0(index) corresponds to 0(var)
print("\n")
print("Neighbors Stuff")
print("print(easy_puzzle.neighbors)")
print(easy_puzzle.neighbors)
print("print(type(easy_puzzle.neighbors))")
print(type(easy_puzzle.neighbors))
print("print(easy_puzzle.neighbors[0])")
print(easy_puzzle.neighbors[0]) # Output {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 30, 33, 54, 57, 60}
print("print(type(easy_puzzle.neighbors[0]))")
print(type(easy_puzzle.neighbors[0]))  # output <class 'set'>
#print(easy_puzzle.neighbors[0][0]) # TypeError: 'set' object does not support indexing
#print(type(easy_puzzle.neighbors[0].pop().pop()))  # AttributeError: 'int' object has no attribute 'pop'
print("print(easy_puzzle.neighbors[0].pop())")
print(easy_puzzle.neighbors[0].pop())
print("print(type(easy_puzzle.neighbors[0].pop()))")
print(type(easy_puzzle.neighbors[0].pop()))
print("\n"*5)
'''

