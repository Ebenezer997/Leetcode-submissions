class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        
        for i in range(len(intervals)):
            if  i + 1< len(intervals):
                if intervals[i][1] > intervals[i+1][0]:
                    return False
                
                
        return True
        
       
        
        
        