class Solution:
    def isPalindrome(self, s: str) -> bool:
         #PU:: if you remove spaces, puntuaciations from a sentence and reverse it will be the same as the original sentece.
        # create an empty string and loop thro the string .
        # you only consider only alphanumeric characters and also lower their case and add it to the empty string.
        #create two pointers one at the beginning index and other at the end. compare them every level if they ain't the same return false or after the end return true
        
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        
        l = len(res)-1
        r = 0
        
        while l > r:
            if res[l]== res[r]:
                l -=1
                r += 1
            else:
                return False
        return True
            