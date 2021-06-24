class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_sum =nums[0]
        
        for i in nums[1:]:
            curr = max(i,curr+i)
            max_sum = max(curr,max_sum)
        
        return max_sum
            