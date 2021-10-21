class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create an empty list to the compliement
        h = {}
        
        #loop through the array
        for i in range(len(nums)):
            
            #calculate the compliment
            com = target - nums[i]
            #check if the compliment is in the dictionary(h)
            if com in h:
                #return it if it is in the dictionary
                return (h[com],i)
            # append this in dictionary
            else:
                h[nums[i]]= i
            #big 0(n)
        
            
        