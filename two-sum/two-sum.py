class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionay key: 2:1, check if 7-2 complement is in the dictioaty
        h = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in h:
                return( h[com], i)
            else:
                h[nums[i]] = i