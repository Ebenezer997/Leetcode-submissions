class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #make it set to remove any duplicate value
        nums_set = set(nums)
        #loop thru length of array add 1 to it
        for i in range(len(nums)+1):
            #compare if i not in nums_set return i.
            if i not in nums_set:
                return i
            
        