class Solution:
    def judgeCircle(self, moves: str) -> bool:
        row = 0
        col = 0
        
        for move in moves:
            if move == "U":
                row += 1
            elif move == "D":
                row -= 1
            elif move == "R":
                col += 1
            elif move == "L":
                col -= 1
                
        if row == 0 and  col== 0:
            return True
        else:return False
        