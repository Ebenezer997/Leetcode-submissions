class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
    
        count = 0
        n = len(s)
        max_count = 0
        for i in range(n):
            count = 0
            for j in range(i,n):
                if s[j] not in res:
                    res.append(s[j])
                    count += 1
                elif count > max_count :
                    max_count = count
                    res = []
                    break
                else:
                    res = []
                    break
            if count > max_count:
                max_count = count
        if len(res)>max_count:
            return len(res)
        
                    
        return max_count
        