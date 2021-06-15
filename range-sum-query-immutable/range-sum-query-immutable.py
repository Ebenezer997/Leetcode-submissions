class NumArray:
    def __init__(self, nums: List[int]):
        self.length=len(nums)
        self.nums=[0]
        for i in range(self.length):
            self.nums.append(self.nums[i]+nums[i])
        

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1]-self.nums[i]
   

