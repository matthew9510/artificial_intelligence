'''
Created on Feb 8, 2018

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        self.dictionary = {}
        
    def exists(self, state):
        """exists(state) - Has this state already been explored?
        Returns True or False, state must be hashable
        """
        temp_list = self.dictionary[state.__hash__()]
        for item in temp_list:
            if item == state:
                return True
        return False
    
    def add(self, state):
        """add(state) - add given state to the explored set.  
        state must be hashable and we asssume that it is not already in set
        """
        
        # The hash function is a Python builtin that generates
        # a hash value from its argument.  Use this to create
        # a dictionary key.  Handle collisions by storing 
        # states that hash to the same key in a bucket list.
        # Note that when you access a Python dictionary by a
        # non existant key, it throws a KeyError

        if isinstance(self.dictionary[state.__hash__()], list):   #if theres something in the spot already (collision)
            temp_list = self.dictionary[state.__hash__()]  #current list
            # make sure the state we are trying to add isn't already a value in the list
            for item in temp_list:
                if item == state:
                    return  #dont add state # todo: get this checked, can we just return
            temp_list.append(state)
            self.dictionary[state.__hash__()] = temp_list

        else:
            # if there is no key in this dictionary already (if no collision occurs)
            temp_list = []
            self.dictionary[state.__hash__()] = temp_list.append(state)
            
