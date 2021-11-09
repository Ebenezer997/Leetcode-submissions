class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows ==2:
            return [[1],[1,1]]
        for i in range(2,numRows):
            curr = [1]
            prev = solution[-1]
            for j in range(len(prev)-1):
                curr.append(prev[j]+prev[j+1])
            curr.append(1)
            solution.append(curr)
        return solution
            
            
        