class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #if the  list of intervals is less than 2 we return it
        if len(intervals)< 2: return intervals
        #sort the list of intervals for easily merging
        intervals.sort()
        
        #initialize an output storage for intervals. it contains the first elements
        output = [intervals[0]]
        
        #Loop thru array for start,end in intervals the second element
        for start,end in intervals[1:]:
            #if the start of the current element is greater than the end of the prevous elements we append the current interval
            if start > output[-1][1]:
                output.append([start,end])
            #elif if the start of the current is not greater than the previous but the end is greater than the end of the previous that means it merges.
            elif end > output[-1][1]:
                output[-1][1] = end
        #return output
        return output
            
            
            