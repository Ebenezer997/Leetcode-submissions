class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #big(O) O(n) and O(n)
        #sliding window question
        #create an empty set
        char = set()
        #initialize first pointer to zero
        l = 0
        #res will update the length of the substring
        res = 0
        #loop thru the substring
        for r in range(len(s)):
            #while s[r] is in the set we remove the elements using l as the current index
            while s[r] in char:
                char.remove(s[l])
                l +=1
            #if not we add the element to the set
            char.add(s[r])
            #compare the max of the current res to the previous res
            res = max(res,r-l+1)
        return res
        