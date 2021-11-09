class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        
        while n:
            y = 2**x
            if y == n:
                return True
            elif y>n: 
                return False
            else:
                x += 1
                
        