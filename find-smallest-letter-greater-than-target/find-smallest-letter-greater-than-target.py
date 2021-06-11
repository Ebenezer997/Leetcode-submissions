class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        
        while l<r:
            mid = (l+r)//2
            if letters[mid] > target:
                r = mid
            else:
                l = mid +1
        return letters[l] if letters[l] > target else letters[0]
        
#         l = 0
#         r = len(letters)-1

# 	    while l<r:
#             mid = (l + (r-l))//2
#             if letters[mid] > target:
#                 r = mid
#             else:
#                 l = mid+1
# 	    return letters[l] if letters[l] > target else letters[0]
#         if letters[0]>target or letters[-1] == target:
#             return letters[0]
#         left = 0
#         right = len(letters)-1
#         res = letters[0]
#         # if target == letters[right]:
#         #     return res
        
#         while left <= right:
#             mid = (right+left)//2
#             if letters[mid] <= target:
#                 left = mid +1
#             else:
#                 right = mid -1
#         return res
    
        
        
                