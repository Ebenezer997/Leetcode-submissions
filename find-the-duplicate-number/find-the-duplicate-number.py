class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast =nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        while slow != fast:
            slow = nums[slow]
            fast =  nums[nums[fast]]
        slow = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast =  nums[fast]
        return slow
        
#this approach doesn't qualify
#         h = {}
#         for i in nums:
#             if i in h:
#                 return i
#             else:
#                 h[i] = i
#         return None
      
        