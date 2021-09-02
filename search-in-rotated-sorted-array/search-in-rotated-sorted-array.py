class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #using binary Search
        #if nums(array) is empty return -1
        if not nums :
            return -1
        #initializing pointers start and end
        start = 0
        end = len(nums) - 1
        
        # while the loop has not ended
        while start <= end:
            #find mid
            mid = (end + start)//2
            #check if mid is the target and return it if it is.
            if  target == nums[mid]:
                return mid
            #if the value of nums[start] is less than nums[mid]
            if nums[start] <= nums[mid]:
                #if target is between nums[start] and nums[mid]
                if target >=nums[start] and target < nums[mid]:
                    #update end pointer to  value before mid
                    end = mid - 1
                #else update the star pointer to the next value after mid
                else:
                    start = mid + 1
            #if nums[start] > nums[end]
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
                
            
        