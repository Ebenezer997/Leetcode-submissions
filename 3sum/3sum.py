class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        N = len(nums)
        
        for i in range(N-2):
            l = i+1
            r = N-1
            while l<r:
                same = nums[i]+nums[r]+nums[l]
                if same == 0:
                    res.add((nums[i],nums[r],nums[l]))
                    l += 1
                    r -= 1
                elif same < 0:
                    l += 1
                else:
                    r -= 1
        return res
                
        