class Board:
    """ 
    a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for r in range(self.height)]

    def __repr__(self):
        """ 
        Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        s += '-' * ((self.width * 2) + 1)

        s += '\n'

        for i in range(self.width):
            s += ' ' + str(i % 10)

        return s

    def add_checker(self, checker, col):
        """ 
        adds the specified checker (either 'X' or 'O') to the
        column with the specified index col in the called Board.
        inputs: checker is either 'X' or 'O'
                col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        for i in range(self.height):
            if self.slots[self.height - 1 - i][col] == ' ':
                self.slots[self.height - 1 - i][col] = checker
                break

    
    ### add your reset method here ###
    def reset(self):
        """
        Resets the Board object on which it is called by setting all slots to contain a space character
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """
        Returns True if it is valid to place a checker in the column col on 
        the calling Board object. Otherwise, it should return False.
        """
        if 0 <= col <= self.width - 1:
            if self.slots[0][col] == ' ':
                return True
            else:
                return False
        else:
            return False

    def is_full(self):
        """
        Returns True if the called Board object is completely full 
        of checkers, and returns False otherwise
        """
        for i in range(self.width):
            if self.can_add_to(i):
                return False
        return True
    
            
    def remove_checker(self, col):
        """
        Removes the top checker from column col of the called Board 
        object. If the column is empty, then the method should do nothing
        """
        for i in range(self.height):
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                break
            
    def is_win_for(self, checker):
        """
        Returns True if there are four consecutive slots containing 
        checker on the board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_diagonal_win(checker) == True or \
           self.is_other_diagonal_win(checker) == True:
            return True
        else:
            return False
        
        
    def is_horizontal_win(self, checker):
        """ 
        Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
        
    def is_vertical_win(self, checker):
        """
        Checks for a vertical win with the specified checker
        checker: Checker
        """
        for i in range(self.height - 3):
            for col in range(self.width):
                if self.slots[i][col] == checker and \
               self.slots[i + 1][col] == checker and \
               self.slots[i + 2][col] == checker and \
               self.slots[i + 3][col] == checker:
                   return True
        return False
    
    def is_diagonal_win(self, checker):
        """
        Checks for a left diagonal win with the specific checker
        checker: Checker
        """
        for i in range(self.height):
            for col in range(self.width - 3):
                if self.slots[i][col] == checker and \
               self.slots[i - 1][col + 1] == checker and \
               self.slots[i - 2][col + 2] == checker and \
               self.slots[i - 3][col + 3] == checker:
                   return True
        return False
    
    def is_other_diagonal_win(self, checker):
        '''
        Checks for a right diagonal win with the specific checker
        checker: Checker
        '''
        for i in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[i][col] == checker and \
               self.slots[i + 1][col + 1] == checker and \
               self.slots[i + 2][col + 2] == checker and \
               self.slots[i + 3][col + 3] == checker:
                   return True
        return False