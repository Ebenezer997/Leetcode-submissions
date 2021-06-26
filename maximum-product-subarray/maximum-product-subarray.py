class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_pro = min_pro = nums[0]
        result = max_pro
        
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_pro = max(curr, curr*max_pro,curr*min_pro)
            min_pro = min(curr,curr*max_pro,curr*min_pro)
            max_pro = temp_pro
            result = max(max_pro,result)
        return result