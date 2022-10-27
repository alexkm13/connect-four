from Board import Board

# write your class below.

class Player(Board):

    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """
        Returns a string representing a Player object. 
        The string returned should indicate which checker the Player object is using
        """
        return str('Player ' + self.checker)

    def opponent_checker(self):
        """
        Returns a one-character string representing the checker of the Player object’s opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """
        Returns the column where the player wants to make the next move
        b: Board
        """
        self.num_moves += 1
        while True:
            a = input('Enter a column: ')
            if b.can_add_to(int(a)):
                return int(a)
            else:
                print('Try Again!')