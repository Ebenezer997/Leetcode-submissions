class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return None
        self.acc = [0]*len(nums) 
        self.acc[0] = nums[0]
        for i in range(1, len(nums)):
            self.acc[i] = self.acc[i - 1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.acc[right] - self.acc[left-1]
        return self.acc[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)