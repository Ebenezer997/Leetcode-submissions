class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        
        for k,v in c.items():
            if v== 1:
                return s.index(k)
        else:
            return -1
        