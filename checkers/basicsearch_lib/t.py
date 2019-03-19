# uncompyle6 version 3.0.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\mroch\Documents\tensorflow\checkers-for-students\tonto.py
# Compiled at: 2018-02-26 20:49:12
# Size of source mod 2**32: 9484 bytes
import checkerboard, abstractstrategy

class AlphaBetaSearch(object):
    posinf = float('inf')
    neginf = float('-inf')
    win = 1e+25
    lose = -1e+25

    def __init__(self, strategy, maxplayer, minplayer, maxplies=3, verbose=False):
        """"alphabeta_search - Initialize a class capable of alphabeta search
        problem - problem representation
        maxplayer - name of player that will maximize the utility function
        minplayer - name of player that will minimize the uitlity function
        maxplies- Maximum ply depth to search
        verbose - Output debugging information
        """
        self.strategy = strategy
        self.maxplayer = maxplayer
        self.minplayer = minplayer
        self.maxplies = maxplies
        self.verbose = verbose
        self.pruned = []

    def alphabeta(self, state):
        alpha = self.neginf
        beta = self.posinf
        ply = 1
        value, action = self.maxvalue(state, alpha, beta, ply)
        if self.verbose:
            print(('alphabeta result utility = %d action = ' % value), end=' ')
            print(action)
        return action

    def __cutoff(self, state, ply):
        """Check for terminal node or cutoff
        returns (cutoffPred, utility)
        cutoffPred - True/False
        utility - utility of node"""
        terminal, winner = state.is_terminal()
        if not terminal:
            terminal = ply == self.maxplies
        if terminal:
            if winner:
                if winner == self.maxplayer:
                    utility = self.win
                else:
                    utility = self.lose
            else:
                utility = self.strategy.utility(state)
            if self.verbose:
                msg = 'winner %s ' % winner if winner else 'cutoff '
                print('%sply %d utility %.1f' % (msg, ply, utility))
                print(state)
            else:
                utility = None
        return (terminal, utility)

    def maxvalue(self, state, alpha, beta, ply):
        """"maxvalue - alpha/beta search from a maximum node
        Find the best possible move knowing that the next move will try to
        minimize utility.
        state - current state
        alpha - utility of best move max player can make
        beta - utility of best move min player can make from previous level
            (so far, we don't know it completely until we finish all
             children in the previous ply)
        """
        terminal, utility = self._AlphaBetaSearch__cutoff(state, ply)
        if terminal:
            return (utility, None)
        else:
            if self.verbose:
                print('maxvalue [%.1f,%1f] ply=%d' % (alpha, beta, ply))
                print(state)
            actions = state.get_actions(self.maxplayer)
            v = self.neginf
            maxaction = None
            for a in actions:
                child = state.move(a)
                newv, _ = self.minvalue(child, alpha, beta, ply + 1)
                if self.verbose:
                    print(('%s->%s minchild [%.1f,%.1f] max(v=%2.f,child=%.2f)' % (
                     state, child, alpha, beta, v, newv)), end=' ')
                    print(' prune = %s' % (max([newv, v]) >= beta))
                    print(child)
                if newv > v:
                    v = newv
                    maxaction = a
                if v >= beta:
                    if self.verbose:
                        self.pruned.append([state, child])
                    break
                else:
                    alpha = max(alpha, v) # this alpha is actually the scopes alpha

            return (
             v, maxaction)

    def minvalue(self, state, alpha, beta, ply):
        """"minvalue - alpha/beta search from a minimum node
        state - current state
        alpha - utility of best move max player can make from previous level
        beta - utility of best move min player can make
        """
        terminal, utility = self._AlphaBetaSearch__cutoff(state, ply)
        if terminal:
            return (utility, None)
        else:
            if self.verbose:
                print('maxvalue [%.1f,%1f] ply=%d' % (alpha, beta, ply))
                print(state)
            actions = state.get_actions(self.minplayer)
            v = self.posinf
            minaction = None
            for a in actions:
                child = state.move(a)
                newv, _ = self.maxvalue(child, alpha, beta, ply + 1)
                if self.verbose:
                    print(('%s->%s maxchild [%.1f,%.1f] min(v=%2.f,child=%.2f)' % (
                     state, child, alpha, beta, v, newv)), end=' ')
                    print(' prune = %s' % (min([newv, v]) <= alpha))
                if newv < v:
                    v = newv
                    minaction = a
                if v <= alpha:
                    if self.verbose:
                        self.pruned.append([state, child])
                    break
                else:
                    beta = min(beta, v)

            return (
             v, minaction)


class Strategy(abstractstrategy.Strategy):
    """Tonto - a very simple strategy for playing checkers"""
    kingval = 200
    pawnval = 100
    edgeval = 10
    enemyterritoryval = 1

    def __init__(self, maxplayer, game, maxplies):
        super(Strategy, self).__init__(maxplayer, game, maxplies)
        self.search = AlphaBetaSearch(self, maxplayer, (self.minplayer), maxplies=maxplies, verbose=False)

    def play(self, board):
        """play(board) - Find best move on current board for the maxplayer"""
        print('%s thinking using tonto strategy...' % self.maxplayer)
        action = self.search.alphabeta(board)
        if action:
            newboard = board.move(action)
        else:
            newboard = board
        return (newboard, action)

    def utility(self, state):
        """utility of state"""
        value = 0
        maxidx = state.edgesize - 1
        maxpidx = state.playeridx(self.maxplayer)
        minpidx = (maxpidx + 1) % 2
        pawnsN = state.get_pawnsN()
        kingsN = state.get_kingsN()
        value += self.kingval * kingsN[maxpidx]
        value += self.pawnval * pawnsN[maxpidx]
        value -= self.kingval * kingsN[minpidx]
        value -= self.pawnval * pawnsN[minpidx]
        thisval = 0
        for r, c, piece in state:
            playeridx, kingP = state.identifypiece(piece)
            if not kingP:
                thisval += maxidx - state.disttoking(piece, r)
            if r == 0 or c == 0 or r == maxidx or c == maxidx:
                thisval += self.edgeval
            if thisval:
                if playeridx == self.maxplayer:
                    value += thisval
                else:
                    value -= thisval
                thisval = 0

        return value


if __name__ == '_main_':
    import boardlibrary
    b = boardlibrary.boards['StrategyTest1']
    redTonto = Strategy('r', b, 6)
    blackTonto = Strategy('b', b, 6)
    print(b)
    nb, action = redTonto.play(b)
    print('Red would select ', action)
    print(nb)
    nb, action = blackTonto.play(b)
    print('Black would select ', action)
    print(nb)
# okay decompiling C:\dev\artificial_intelligence_a3\checkers\__pycache__\tonto.cpython-36.pyc