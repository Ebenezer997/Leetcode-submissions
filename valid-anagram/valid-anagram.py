class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         Idea behind this solution is to count the letters in two strings and check if they are same. First loop counts. Second loop substracts. Third loop checks if balanced.
        
        dicts = {}
        
        for i in s:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        
        for i in t:
            if i in dicts:
                dicts[i] -= 1
            else:
                return False
        
        for value in dicts.values():
            if value != 0:
                return False
        
        return True
         
        
        
        #for eg like s="a" & t="ab"
        # if len(s) != len(t):
            # return False
	    #creating a set to cut the time of looping
        # for i in set(s):
		#counting whether the letters are repeted the same no of time
            # if s.count(i) != t.count(i):
            #     return False
        # return True
        
        #big 0(n)
#         if len(s) != len(t):
#             return False
#         elif sorted(s) == sorted(t):
#             return True
#         else:
#             return False


       
        
        