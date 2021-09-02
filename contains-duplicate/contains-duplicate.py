class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = i
            else:
                return True
        return False
     
                