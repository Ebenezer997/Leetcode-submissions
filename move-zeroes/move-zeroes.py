class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # will take two pointer i and j.  initialize i = 0
        # I will increase i if and only if I am swaping nums[j], nums[i]
        #and I will swap nums[j],nums[i] when nums[j] is not zero
        
        #[0,1,0,3,12] -> intial nums[j] =0, nums[i]=0
        # [0,1,0,3,12] -> intial nums[j] =1, nums[i] =0
        # [1,0,0,3,12] -> swapped nums[j] and nums[i]
        
        i=0
        for j in range (len(nums)):
            if nums[j] !=0:
                nums[i], nums[j]=nums[j],nums[i]
                i+=1
