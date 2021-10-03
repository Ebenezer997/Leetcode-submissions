class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Problem check if a person can attend indivdual meetings : this can only appen if the intervals does not merge if intervals merge return false.
        intervals.sort()
        
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        
        return True
        