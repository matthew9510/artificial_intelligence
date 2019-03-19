from math import sqrt
from basicsearch_lib.board import Board
#from basicsearch_lib.boardtypes import TileBoard


######################################################################
# List comprehension
######################################################################
print([x for x in range(10)])
print([x for x in 'abcdef' if x not in 'abc'])
print({x: x**2 for x in range(5)})
print([x**2 for x in range(5)])
print([[None for i in range(3)] for j in range(3)])
######################################################################
# New line assignment
######################################################################
x = \
    8
print(x)

#######################################################################
# String Formatting
######################################################################
string = "s"
#print(string.ascii_value)
print('{2}, {1}, {0}, {2}'.format('a', 'b', 'c'))  # print parameters at specific indices, Note: repeated indice
print('{2}, {1}, {0}'.format(*'abc'))  # unpacking argument sequence
## List unpacking not double assignemnt
z, y = (3,4)
print(z)
print(y)

######################################################################
# Iterable
######################################################################
list = [x for x in range(10)]
list_iter = iter(list) # todo use list_iter
print(list)
for i in list:
    print(i)
print(list.__contains__(3))


######################################################################
# Lists
######################################################################
two_dimension_list = [[i for i in range(3)] for j in range(3)]
print(two_dimension_list)
print(len(two_dimension_list))
two_dimension_list[0].insert(1, None)  # two_dimension_list elements are <List> objects
print(two_dimension_list)
# two_dimension_list.remove(None)  # error
print(two_dimension_list)
# finding index of multi dimensional list