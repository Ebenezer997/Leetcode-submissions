class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        len_array = len(nums)+1
        a = set([i for i in range(1,len_array)])
        b = set(nums)
        return (a-b)
        
       