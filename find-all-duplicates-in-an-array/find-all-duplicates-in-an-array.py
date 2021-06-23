class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        h = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                h.append(nums[i])
        
        return h
                
        
        