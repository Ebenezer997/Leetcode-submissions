class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Use sliding window technique
        # have two pointers and loop throu the array while adding
        #Use MAx func to find the maximum sum while it loops
        total_sum = nums[0]
        max_sum = nums[0]
        
        for i in (nums[1:]):
            total_sum = max(i,i+total_sum)
            max_sum = max(max_sum,total_sum)
        return max_sum