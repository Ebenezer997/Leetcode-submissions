class Leaderboard:

    def __init__(self):
        self.board = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score
        
        

    def top(self, K: int) -> int:
        top = 0
        for player in self.board.most_common(K):
            top += player[1]
        return top

    def reset(self, playerId: int) -> None:
        self.board.pop(playerId)
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)