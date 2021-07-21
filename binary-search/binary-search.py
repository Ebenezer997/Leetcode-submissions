class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two pointers one is the index of the first element(left) and index of the last element(right)
        #We loop through and find the middle value: if the middle value is the target we return it if not 
        #if the middle value is greater the tagert value we move left to the middle +1 index and continue our binary search else if it is less than the tagert we mmove right equal to middle-1. Till we find our element
        N = len(nums)
        l= 0
        r = N-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
      
        return -1
                
                
        