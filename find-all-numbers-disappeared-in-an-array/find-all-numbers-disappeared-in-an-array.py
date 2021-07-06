class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # without an extra space
        len_array = len(nums)+1
        a = set([i for i in range(1,len_array)])
        b = set(nums)
        return (a-b)
#         s = []
#         for i in range(1,len(nums)+1):
#             s.append(i)
#         return (set(s)-set(nums))
# without an extra space
 
        