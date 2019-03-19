import csp_lib.sudoku as CSP
from csp_lib.backtrack_util import (first_unassigned_variable,
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    '''Instead of passing more variables just nest functions
    e.g.
    #return backtrack({}, csp, select_unassigned_variable, order_domain_values, inference)
    #return backtrack({}, csp)
    #def backtrack(assignment, csp, select_unassigned_variable, order_domain_values, inference):
    '''

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
            Returns None if there is no solution.  Otherwise, the
            csp should be in a goal state.
        """
        # assert isinstance(csp, CSP)
        # if csp.nassigns == len(csp.variables):
        if len(assignment) == len(csp.variables):
            return assignment
        variable = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(variable, assignment, csp):
            csp.assign(variable, value, assignment)  # assigns variables dictionary{}, doesn't manipulate curr_domains
            removals = csp.suppose(variable, value)  # list of tuples; tuple (var, domain_item_removed)  this is incase the assignemnt doesnt work out, its a way to go back
            if csp.nconflicts(variable, value, assignment) == 0:
                # i.e. if removals = [] then its curr_domain[var] is len(1) meaning it's assigned; else removals == [(0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8)] # Note that the value chosen for assignment in this case would be 9
                inferences = inference(csp, variable, value, assignment, removals)  # is this no_inference because we have are maintaining arc consistency therefor we dont need to forward check
                # todo - last thing would be to make mac work
                if inferences:  # if inferences != failure:
                    # todo - add inferences to assignment
                    result = backtrack(assignment)  # recursive call if consistency is kept
                    if result is not None:
                        return result
                ''' essentially every line below in def is the else condition of (if inferences:) b/c return statement inside if condition scope'''
                #csp.restore(removals) # essentially if variable assignement was not right # todo - make sure this updates assignment at fix the domains of the removals # log this so we can fix domains of var asssigment manip
            csp.restore(removals)  # essentially if variable assignement was not right # todo - make sure this updates assignment at fix the domains of the removals # log this so we can fix domains of var asssigment manip
        csp.unassign(variable, assignment)
        return None

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python) i.e. csp and function handles
    result = backtrack({})  # initial backtrack function(search procedure) called/invoked
    assert result is None or csp.goal_test(result)
    return result

