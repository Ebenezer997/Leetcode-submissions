class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
           #find the leftmost value and rightmost value: 
        #leftmost= zero and rightmost= totalSum
        #every loop we subtract the current index value from the totalSum(rightmost) and check if leftmost and rightmost are the same.
        #If not we add the current index value to 
        #time = 0(n) and Spacs = 0(1)
        
        totalsum = sum(nums)
        right = totalsum
        
        left = 0
        
        for i in range(len(nums)):
            right -= nums[i]
            
            if left == right:
                return i
            else:
                left += nums[i]
        
        return -1
        