class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        final = []
        
        for i in intervals:
            if not final or final[-1][1] < i[0]:
                final.append(i)
            else:
                final[-1][1] = max(final[-1][1], i[1])
        return final
        
        