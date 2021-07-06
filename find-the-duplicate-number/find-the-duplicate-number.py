class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #intialize the two pointers to the first element in the index
        turtle = hare = nums[0]
        #turtle is a slow pointer moves one step at a time
        turtle = nums[turtle]
        #hare is the fast pointer moves two steps at a time
        hare = nums[nums[hare]]
        #while turtle and hare has not meet. They will be moving in their pace
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
        #when they meet turtle will start again and both will move at the same pace.
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
      
        