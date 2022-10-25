class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        startings = sorted([i[0] for i in intervals])
        endings = sorted([i[1] for i in intervals])
        l = len(intervals)
        used_rooms = 0
        
        sp= 0
        ep = 0
        
        while sp < l:
            if startings[sp] >=  endings[ep]:
                used_rooms -= 1
                ep += 1
            
            used_rooms += 1
            sp += 1
        
        return used_rooms