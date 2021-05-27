class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = []
        for i in range (1,len(nums)+1):
            s.append(i)
        return (set(s)-set(nums))
            
        