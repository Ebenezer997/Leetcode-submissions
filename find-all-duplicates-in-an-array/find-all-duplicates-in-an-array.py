class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ouput = []
        
        for n in nums:
            m = abs(n)
            if nums[m-1] < 0:
                ouput.append(m)
            else:
                nums[m-1] *= -1
        return ouput
        
        