class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.B = {}
        for p in [1,2]:
            self.B[p] = {}
            self.B[p]['rows'] = [0]*n
            self.B[p]['cols'] = [0]*n
            self.B[p]['diags'] = [0,0]
        

    def move(self, row: int, col: int, player: int) -> int:
        self.B[player]['rows'][row]+=1
        if self.B[player]['rows'][row]==self.n:
            return player
        
        self.B[player]['cols'][col]+=1
        if self.B[player]['cols'][col]==self.n:
            return player
        
        if row==col:
            self.B[player]['diags'][0]+=1
            if self.B[player]['diags'][0]==self.n:
                return player
        
        if (row+col)==self.n-1:
            self.B[player]['diags'][1]+=1
            if self.B[player]['diags'][1]==self.n:
                return player
            
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)