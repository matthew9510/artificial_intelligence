"""
ai - search & strategy module
implement a concrete Strategy class and AlphaBetaSearch
"""
import abstractstrategy
from checkerboard import CheckerBoard
import math
########################################################
# Note:
# assert isinstance(object_being_passed_in, true_label_type_of_object)
#   - tells the interpreter that in this particular scope this object being passed in is of a certain type, so go ahead and give him method suggetions
########################################################

class Strategy(abstractstrategy.Strategy):
    def __init__(self, maxplayer, game, maxplies):
        super(Strategy, self).__init__(maxplayer, game, maxplies)
        self.search_algorithm = AlphaBetaSearch(self, self.maxplayer, self.minplayer, self.maxplies, verbose=False)
        #################################################
        # No need to repeat, because Strategy is a sub class of abstractstrategy.Strategy, we would already be able those attributes through the keyword self.
        '''
        self.maxplayer = maxplayer  # Not max player, other player thing
        self.game = game  # checkerboard class
        self.maxplies = maxplies  # use this for a cutoff
        '''
        #################################################

    def play(self, board):  # Note: board is a checkerboard # called in checkers
        """"play - Make a move
                Given a board, return (newboard, action) where newboard is
                the result of having applied action to board and action is
                determined via a game tree search (e.g. minimax with alpha-beta
                pruning).
                """
        # Moved this into the constructor of stategy # search = AlphaBetaSearch(self, self.maxplayer, self.minplayer, self.maxplies, verbose=False)
        assert isinstance(board, CheckerBoard)
        chosen_action = self.search_algorithm.alpha_beta(board)
        new_board = board.move(chosen_action)  # this updates certain attributes, one for example is .movecount which is called in checkers
        return (new_board, chosen_action)

    #def utility(self, board, player): # the board has an attribute which can get the player's index calling maxpindx = board.playeridx(self.maxplayer) # where self.maxplayer is referring to the constructor aka stategy constructor
    def utility(self, board):
        # return the utility cost of the board being passed in
        utility_value = 0
        '''
        Ideas: 
        Number of pawn
        Number of kings 
        count total piece
        Dist to king
        Single jump
        Multiple Jumps 
    
        
                        # action will be in the following format 
                        - simple move [(original_row_num, original_col_num), (new_row_num, new_col_num)]
                        - capture move [(original_row_num, original_col_num), (row_num_of_the_resulting_move, col_num_of_the_resulting_move, (captured_row_num, captured_col_num))]
                        - Multiple capture move [(original_row, original_col), (row_num_of_the_resulting_move_one, col_num_of_the_resulting_move_one, (captured_row_num_of_first_move, captured_col_num_of_first_move)), (row_num_of_the_resulting_move_two, row_num_of_the_resulting_move_two,((captured_row_num_of_second_move, captured_col_num_of_second_move)))]
                        - understand how to use these tuples to remove tiles and create utility....
        
        
        below might come in handy
        try:
            pidx = self.pawns.index(player)
        except ValueError:
            raise ValueError("Unknown player")

        # If we see any captures along the way, we will stop looking
        # for moves that do not capture as they will be filtered out
        # at the end.
        moves = []
        # Scan each square
        for r in range(self.rows):
            for c in range(self.coloffset[r], self.cols, self.step):
                piece = self.board[r][c]
                # If square contains pawn/king of player who will be moving
                if piece in self.players[pidx]:
                    # Determine types of moves that can be made
                    if piece == self.pawns[pidx]:
                        movepaths = self.pawnmoves[player]
                    else:
                        movepaths = self.kingmoves
                    # Generate moves based on possible directions
                    newmoves = self.genmoves(r, c, movepaths, pidx)
                    moves.extend(newmoves)
        '''
        return utility_value

class AlphaBetaSearch:
    """
    This adversarial search algorithm is recursive
    It will find the best possible move to make for a player specified through testing utility after a specified depth
    This search will prune away branches that cannot possibly influence the final decision
    TRICKIEST THING TO SEE, THE STATES, alphas, and betas ARE CHANGING throughout the recursive call!
    """
    ###########################################################
    # class attributes
    ###########################################################
    infinity = float('Infinity')  # <----- class attribute, refer to this as self.infinity
    negative_infinity = float('-Infinity')
    win_utility_const = 1e20
    lose_utility_const = -1e20

    def __init__(self, strategy, max_player, max_plies=3, verbose=False):
        self.strategy = strategy  # for calling the utility function
        self.max_player = max_player  # for cutoff test
        self.max_plies = max_plies  # for cutoff test
        self.verbose = verbose  # for debugging
        self.pruned = list()

    def alpha_beta(self, state):
        """essentially the driver function for the alpha beta minimax search algorithm
        returns the best action to take"""
        assert isinstance(state, CheckerBoard)
        initial_alpha = self.negative_infinity
        initial_beta = self.infinity
        ply = 0 # note a ply is two turns after a move the state.movecount increases once, but only when state.movecount == 2 then ply = 1
        v, best_action = self.max_value(state, initial_alpha, initial_beta, ply) #if verbose print v and action? #
        # note the returned variable v doesn't need to be used, important to know so we can design a function to be utilized in many ways for other functions, ie. recursive use and then driver use!
        return best_action

    def cutoff_test(self, state, ply_num): # we include self function definitions so that we can call our class attributes
        """This method will return a utility value and also whether or not this state is a terminal state"""
        assert isinstance(state, CheckerBoard)
        assert isinstance(self.strategy, Strategy)
        [terminal, winner] = state.is_terminal()
        utility = None # initialize utility in-case node is not a terminal or at cutoff point
        if not terminal: # although the game is not complete, let's test to see if we need to calculate a utility value
            cut_off = ply_num == self.max_plies # do we need to stop searching?
            if cut_off:
                utility = self.strategy.utility(state)
                terminal = True # to stop recursion in Alpha-Beta max_value and min_value scope
        else:
            if winner: # todo, can I remove this line? get this checked
                if winner is self.max_player:
                    utility = self.win_utility_const
                else:
                    utility = self.lose_utility_const
        return(utility, terminal)

    def max_value(self, state, alpha, beta, ply):
        """returns a utility score and whether a state is in a terminal state
         The utility score corresponds with the max utility of a particular action within a set of actions
         generated through the passed in state"""
        assert isinstance(state, CheckerBoard)
        ###########################################################
        # Changing variables throughout algorithm, needed for updating values to make correct decisions along execution
        ###########################################################
        v = float('-Infinity')  # initial value of max_value set to be not found
        decided_action = None
        alpha = alpha
        # beta = beta # Don't need this because a max node would never generate the best min value, only focus is max value stuff

        '''
        Swapped algorithm code in book 
        From this
        # if state.is_terminal()[0] is True:
        #   return self.strategy.utility(state)
        To This
        #if self.cuttoff_test(state, ply):
            #return eval(state) #return the utility and the best decided action
        '''
        [utility, terminal] = self.cutoff_test(state, ply)
        if terminal: # added this to make sure we eventually we handle a game that is over
            return (utility, None)

        if not terminal:  # same as else
            for action in state.get_actions(self.max_player):
                temp_checker_board = state.move(action)
                new_v = max(v, self.min_value(temp_checker_board, alpha, beta, ply + .5)[0])  # ply depth will be incremented/or decremented each recursive call for the recursive cutoff test
                if new_v > v:
                    v = new_v
                    decided_action = action
                    alpha = new_v # Question, is this right place for this
                # possible solution = tab all below by one tab to be fit under if
                # Pruning below
                if v >= beta: # todo get this checked if its greater than and equal to or just greater than
                    '''This is a move that is better than the best move that the minplayer would make on the previous level.
                    Consequently, min_player will never let us get here and it is not worth exploring any more, but were not going to be able to make it because min would not optimally give us this chance'''
                    self.pruned.append([state, temp_checker_board])
                    break # once you've pruned you don't need to compute anything else because its of no use

                else:
                    alpha = max(alpha, v) # this alpha is actually the scopes alpha, This is why we are not returning alpha and beta
                    # todo: NOTICE how we are not updating beta, so we shouldnt instanciate it
            return (v, decided_action) # Question does this have to go one indentbackwards?

    def min_value(self, state, alpha, beta, ply):
        assert isinstance(state, CheckerBoard)
        v = float('Infinity')  # initial value of min_value
        decided_action = None
        alpha = alpha  # is this good practice or is it redundant
        beta = beta

        # if state.is_terminal()[0] is True: # replace this with cutoff
        #return self.strategy.utility(state)
        if self.terminal
        for action in state.get_actions(state):
            v = min(v, self.max_value(state.move(state, action), alpha, beta, ply + .5))
            if v >= alpha:
                return v
            beta = min(beta, v)
        return (v, decided_action)
