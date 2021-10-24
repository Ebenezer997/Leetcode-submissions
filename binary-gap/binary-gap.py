class Solution:
    def binaryGap(self, n: int) -> int:
        nums = bin(n)[2:]
        print(nums)
        gap = 0
        m = 0
        count = 0
        for i in nums:
            if i == '0':
                gap += 1
            elif i == '1':
                count +=1
                m = max(gap,m)
                gap = 0
        if count ==1:
            return 0
        return m+1
                
                
                
            
        