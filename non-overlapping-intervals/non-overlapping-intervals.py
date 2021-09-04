class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort(key=lambda x:x[1])
        
        output = 0
        max_end = float('-inf')
        
        for start,end in intervals:
            if start >= max_end:
                max_end = end
            else:
                output += 1
        return output
        