class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # Deal with null case
        if(grid == None and grid == [[]]):
            return 0
        
        numOfIslands = 0
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if(grid[i][j] == "1"):
                    numOfIslands += 1
                    self.travelConnectedAdjacentNodesAroundIt(grid, r, c, i, j)
                    
        return numOfIslands
    
    def travelConnectedAdjacentNodesAroundIt(self, grid, r, c, i, j):
        q = deque()
        q.append([i,j])
        while(len(q) != 0):
            pos = q.pop();
            ii = pos[0]
            jj = pos[1]
            
            if(grid[ii][jj] == "1"):
                grid[ii][jj] = "2"
                self.appendIfNotBoundaryCase(grid, q, r, c, ii+1, jj)
                self.appendIfNotBoundaryCase(grid, q, r, c, ii, jj-1)
                self.appendIfNotBoundaryCase(grid, q, r, c, ii-1, jj)
                self.appendIfNotBoundaryCase(grid, q, r, c, ii, jj+1)    
            
    def appendIfNotBoundaryCase(self, grid, q, r, c, ii, jj):
        if(ii >= 0 and ii < r and jj >= 0 and jj < c and grid[ii][jj] == "1"):
            q.append([ii,jj])
        