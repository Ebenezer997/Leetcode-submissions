class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        else:
            return True
#         h = {}
         
#         for i in nums:
#             if i in h:
#                 return True
#             else:
#                 h[i] = i
        return False
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return  True
        # return False
        
       