class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        N = len(nums)
        
        result = set()
        
        for i in range(N-2):
            left = i+1
            right = N-1
            while left < right:
                sum_value = nums[i]+nums[left]+nums[right]
                
                if sum_value == 0:
                    result.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif sum_value <0:
                    left += 1
                    
                else:
                    right -= 1
        return result
        