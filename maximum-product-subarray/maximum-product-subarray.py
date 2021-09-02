class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        max_pro = nums[0]
        min_pro = nums[0]
        
        result = max_pro
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_pro = max(curr,max_pro*curr, min_pro*curr)
            min_pro = min(curr,max_pro*curr, min_pro*curr )
            max_pro = temp_pro
            result = max(max_pro, result)
        return result
            