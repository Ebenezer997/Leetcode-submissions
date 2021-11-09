class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        
        prev1 = 0
        prev2 = 1
        
        for i in range(2,n+1):
            output = prev1 + prev2
            prev1 = prev2
            prev2 = output
        
        return output
        
        
        
#         if n == 0: return 0
#         if n == 1: return 1
        
#         return (self.fib(n-1)+self.fib(n-2))
#           if n == 0: return 0
#           if n == 1: return 1
        
#           prev1 = 0,prev2 = 1
        
       