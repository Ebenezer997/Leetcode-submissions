class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals : return 0
        used_rooms = 0
        startlists = sorted([i[0] for i in intervals])
        endlists = sorted([i[1] for i in intervals])
        
        
        l = len(intervals)
        sp = 0
        ep = 0
        
        while sp < l:
            if startlists[sp] >= endlists[ep]:
                used_rooms -= 1
                ep += 1
        
        
            used_rooms += 1
            sp += 1

        return used_rooms
                