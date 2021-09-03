class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 sort the array
        #2 create an empty set for result
        #3 asign N for length of nums : len(nums)
        #4 loop thru array and decreasing -2 becos of two pointers(N-2)
        #5 create two pointers left ahead of current i by 1(left= i+1) and Right is the last element[right = N-1]
        #6 While left is less than right: calculate sum_value = i + left+right
        #7 if sum_value = 0  Add the three sets to results
        #if sum_value <0 move left to next value since is close to small values
        #if sum_value>0 reduce the right by 1 because that is where the big values are.
        #return results at the end
        nums.sort()
        N = len(nums)
        result = set()
        
        for i in range(N-2):
            left = i+1
            right = N-1
            while left < right:
                sum_value = nums[i]+nums[left]+nums[right]
                
                if sum_value == 0:
                    result.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif sum_value < 0:
                    left += 1
                
                else:
                    right -= 1
        return result
       