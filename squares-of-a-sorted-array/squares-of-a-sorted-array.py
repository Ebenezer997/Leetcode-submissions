class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        quare = []
        for i in range(len(nums)):
            lo = nums[i]*nums[i]
            quare.append(lo)
            
        return sorted(quare)
        