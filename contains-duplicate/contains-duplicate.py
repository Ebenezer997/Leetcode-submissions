class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #convert the nums into a set: since a set does not take duplicates
        #if the length of the set nums and length of nums is still the same that means there is not duplicate.
        #if not that means there is duplicate.
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True
        
        #         h = {}
         
#         for i in nums:
#             if i in h:
#                 return True
#             else:
#                 h[i] = i
    
    