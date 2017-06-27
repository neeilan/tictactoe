class MinimaxTTT():
    
    def __init__(self):
        self.board = [None] * 9
        self.computer = 1
        self.human = -1

    def user_move(self, cell):
        '''
        0 <= cell <= 8
        '''
        self.board[cell] = self.human
        
        if self.get_winner() is None:
            self._computer_move()

    def _computer_move(self):
        max_score = -2  # will change as minimax score >= -1
        ideal_cell = None
        
        for cell in range(9):
            if self.is_occupied(cell):
                continue
            
            board_copy = self.board.copy()
            board_copy[cell] = self.computer
            score = self._minimax_score(board_copy, self.human)

            if score > max_score:
                max_score = score
                ideal_cell = cell
                
        self.board[ideal_cell] = self.computer
     
    def get_cell(self, i):
        return self.board[i]
    
    def is_occupied(self, cell):
        return self.board[cell] is not None       

    def _minimax_score(self, board, player):
        _winner = self.get_winner(board)
    
        if _winner in [player, -player, 0]:  # game over
            return _winner
    
        state_score = -1 if player == self.computer else 1
        
        for i in range(9):
            
            if board[i] is None:
                next_board = board.copy()
                next_board[i] = player
                next_score = self._minimax_score(next_board, -player)
                
                # human minimizes computer's score; computer maximizes it
                if player == self.computer and next_score > state_score:
                    state_score = next_score
                elif player == self.human and next_score < state_score:
                    state_score = next_score
                    
        return state_score

    def get_winner(self, board = None):
        if board is None:
            board = self.board

        for i in range(3):
            # rows
            if board[i*3] == board[i*3 + 1] == board[i*3 + 2]:
                if board[i * 3] is not None:
                    return board[i * 3]
            # columns
            if board[i] == board[i+3] == board[i+6]:
                if board[i] is not None:
                    return board[i]
        # diagonals
        if (board[0] == board[4] == board[8]):
            if board[0] is not None:
                return board[0]
        if (board[2] == board[4] == board[6]):
            if board[2] is not None:
                return board[2]
        # tie
        if None not in board:
            return 0
        
        # in progress
        return None


    def __str__(self):
        return str(self.board)

