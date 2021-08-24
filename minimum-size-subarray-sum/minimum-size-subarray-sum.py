class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) == target:
            return len(nums)
        if sum(nums) < target :
            return 0
        right = 0
        left = 0
        Sum = 0
        m = len(nums)
        for right in range(len(nums)):
            Sum += nums[right]
            while Sum >= target:
                
                m = min(m,right-left+1)
                Sum -= nums[left]
                left += 1
        return m
        