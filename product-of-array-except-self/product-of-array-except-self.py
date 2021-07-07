class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
    												 	  # [1, 2, 3, 4]
        answer = [1] * array_length # [1, 1, 1, 1]
    
    # first for loop (forward)
        for i in range (1, array_length):
            answer[i] = nums[i-1] * answer[i-1]
            rightProduct = 1
      
    # second for loop (backwards)
        for i in range (array_length - 1, -1, -1):
            answer[i] *= rightProduct
            rightProduct = rightProduct * nums[i]
        return answer
        