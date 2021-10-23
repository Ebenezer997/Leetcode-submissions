class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com in h:
                return( h[com], i)
            else:
                h[nums[i]] = i
        