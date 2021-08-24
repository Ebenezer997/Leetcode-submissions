class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Use sliding window technique
        # have two pointers and loop throu the array while adding
        #Use MAx func to find the maximum sum while it loops
        Total_sum = nums[0]
        max_sum = nums[0]
        
        for i in (nums[1:]):
            Total_sum = max(i, Total_sum+i)
            max_sum = max(Total_sum, max_sum)
        return max_sum