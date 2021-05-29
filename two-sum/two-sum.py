class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if com not in h:
                h[nums[i]]=i
            else:
                return (i, h[com])
        