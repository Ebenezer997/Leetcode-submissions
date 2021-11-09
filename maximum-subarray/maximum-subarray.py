class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalsum = nums[0]
        maxsum = nums[0]
        
        for i in nums[1:]:
            totalsum = max(i, totalsum+i)
            maxsum = max(totalsum,maxsum)
        return maxsum
        
        