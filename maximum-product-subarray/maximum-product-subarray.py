class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #if it is nums return empty
        if not nums:
            return 0
        #initialize two pointers max_pro and min_pro as initial elements
        max_pro = min_pro = nums[0]
        #initialize result to max_pro
        result = max_pro
        # loop through nums from index 1
        for i in range(1,len(nums)):
            # current element is the nums[i]
            curr = nums[i]
            #this calculate temprory product,
            temp_pro = max(curr, curr*max_pro,curr*min_pro)
            #calculate min product
            min_pro = min(curr,curr*max_pro,curr*min_pro)
            #initialize max_pro = temp_pro
            max_pro = temp_pro
            
            result = max(max_pro,result)
        return result