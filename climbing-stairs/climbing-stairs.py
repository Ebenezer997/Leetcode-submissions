class Solution:
    def climbStairs(self, n: int) -> int:
        # 1,2,3,4,5
        #steps:1,2,3,5,8,13
        #according to the approach the steps looks at fibonacci sequence:
        #The approach is to add successive steps.
        
        if n <= 2:return n
        prev1 = 1
        prev2 = 2
        current = 0
        for i in range(2,n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
            
        return current
            
        