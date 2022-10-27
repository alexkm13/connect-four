import random  
from Connect4 import *

class AIPlayer(Player):
    """
    Represents an AI player for Connect Four
    """
    def __init__(self, checker, tiebreak, lookahead):
        """
        Constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """
        Returns a string representing an AIPlayer object
        """
        return super().__repr__() + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

    def max_score_column(self, scores):
        """
        Takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score
        """
        score = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                score += [i]
        if self.tiebreak == 'LEFT':
            return score[0]
        elif self.tiebreak == 'RIGHT':
            return score[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(score)

    def scores_for(self, b):
        """
        Determines the called AIPlayer‘s scores for the columns in b
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead)
                opponent_scores = opponent.scores_for(b)
                if max(opponent_scores) == 0:
                    scores[col] = 100
                elif max(opponent_scores) == 100:
                    scores[col] = 0
                elif max(opponent_scores) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores

    def next_move(self, b):
        """
        Returns the called AIPlayer‘s judgment of its best possible move
        b: Board
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        return self.max_score_column(scores)