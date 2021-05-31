class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            leftsqd = nums[left]**2
            rightsqd = nums[right]**2
            if leftsqd < rightsqd:
                output.append(rightsqd)
                right -= 1
            else:
                output.append(leftsqd)
                left += 1
        
        return reversed(output)
                
                            
                    
#         quare = []
#         for i in range(len(nums)):
#             lo = nums[i]*nums[i]
#             quare.append(lo)
            
#         return sorted(quare)
        