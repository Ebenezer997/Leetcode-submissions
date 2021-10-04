class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #since the array is a cycle; We find the modulo of k :
        
        k %= len(nums)
        #manipulation the array. we will cut where the end of the k is and add it to the beginning of the nums
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]