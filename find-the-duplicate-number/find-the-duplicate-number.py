class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = hare = nums[0]
        turtle = nums[turtle]
        hare = nums[nums[hare]]
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
        
        turtle = nums[0]
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]
        
        return turtle
            
#this approach doesn't qualify
#         h = {}
#         for i in nums:
#             if i in h:
#                 return i
#             else:
#                 h[i] = i
#         return None
      
        