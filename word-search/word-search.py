class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # check for the width of board
        N = len(board[0])
        # check for the height of the board
        M = len(board)
        # Check for the length of the word
        P = len(word)
        
        #create helper function
        def helper(r,c,pos):
            
            if pos >= P:
                return True
            elif 0 <= r <M and 0 <= c<N and board[r][c] == word[pos]:
                temp = board[r][c]
                board[r][c] = None
                if helper(r-1,c, pos+1)or helper(r+1,c, pos+1)or helper(r,c-1, pos+1)or helper(r,c+1, pos+1) : return True
                board[r][c] = temp
                
            
          # check if the length of the word is not greater than the board
        
          # check if we inside our grid and check if the word is the same as we are checking for
          # backtrack for every word search
        
            
            
            
        
        
        #create a condition to loop thru the board
        
        for r in range(M):
            for c in range(N):
                if helper(r,c,0):
                    return True
        
       
        
       
                
        