class Solution:
    def findMin(self, nums: List[int]) -> int:
         # if not nums or len(nums) == 0:
         #    return 0 
        # we have to think about two scenarios here.
        #we rotated and the middle value is greater  than the value at the last index: means min
        #value is between the middle and the end.
        #else if the last middle value is lesser than the end : means the min value is between the fisrt and middle.
        #initialize two pointers first and last
        first = 0
        last = len(nums)-1
        #we loop through the array While first is less than last
        while first < last:
            #we calucalate the mid
            mid = (first +last)//2
            #check our scenarios if mid is greater than last we update the first element to value after mid
            if nums[mid]>nums[last]:
                first= mid +1
            #if is not we update our last value to mid
            else:
                last = mid
            #return mid
        return nums[first]
        
        
        