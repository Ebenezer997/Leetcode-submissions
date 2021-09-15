class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         #PU :: if you have two letters have the same number characters  return true  else return false
        
        #Idea:: check the length both strings if they are the same if not we return false
        #       after we sort the two letters which arranging the letters alpabetically. 
        # If they ain't they the same we return false else return true
        #time Com:: Olog(N)
        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
     