class Solution:
    def countSubstrings(self, s: str) -> int:
        #count the substrings
        res = 0
        
        #loop through the string
        for i in range(len(s)):
            #initialize two pointers to i
            l = i
            r = i #for odd
            # while : l is grater than zero, r is less than length of string, and s[l]===s[r], we increase res by 1
            while l >=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            # for even
            r = 1+i
            while l >=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
           
        
        return res