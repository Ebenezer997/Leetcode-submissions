class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = bin(n)
        count = 0
        
        for i in bin_num:
            if i  == '1':
                count += 1
        return count
        
        
        