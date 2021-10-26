class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        
        for i in s:
            if i.isalnum():
                res += i.lower()
                
                
        l = len(res)-1
        r = 0
        
        while l > r:
            if res[l] == res[r]:
                l -= 1
                r += 1
            else:
                return False
        return True
            
        