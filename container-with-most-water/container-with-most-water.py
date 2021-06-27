class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            a = w * h
            max_area = max(max_area, a)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
#         res = 0
#         l,r = 0, len(height)-1
        
#         while l < r: 
#             area = (r - 1) * min(height[l], height[r])
#             res = max(res, area)
            
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
#         return res
        