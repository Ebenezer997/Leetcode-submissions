class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curmax = nums[0]
        for i in nums[1:]:
            curmax = max(i, curmax + i)
            max_sum = max(curmax,max_sum)
        return max_sum
    
        