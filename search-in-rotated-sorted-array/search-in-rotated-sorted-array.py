class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start]<=target and target <nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
                    
                    
                    
                
       
            
        