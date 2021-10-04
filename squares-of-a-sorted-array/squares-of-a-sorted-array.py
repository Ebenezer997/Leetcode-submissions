class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        new = [0]* len(nums)
        k = len(nums)-1
        
        
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                new[k] = nums[l]**2
                l += 1
            else:
                new[k] = nums[r]**2
                r -= 1
            k -= 1
        return new
        
        
        
        
        
        